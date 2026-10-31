/**
 * evidence-library.js - Interactive Evidence & Data Library for PPRI Pakistan
 * Zero-dependency client-side search, multi-facet filtering, topic clustering,
 * direct download management, and academic citation generation for 187 datasets.
 */

(function () {
  'use strict';

  const CATALOG_URL = '/assets/data/pakistan_library_catalog.json';

  let libraryData = null;
  let allCatalog = [];
  let downloadQueue = [];
  let topicMap = [];
  let workflow = [];
  let topStack = [];
  let credibilityRules = {};

  // Active Filter State
  const state = {
    view: 'catalog', // 'catalog' | 'queue' | 'topic-map' | 'workflow'
    search: '',
    grade: 'all',
    priority: 'all',
    topic: 'all',
    format: 'all',
    sort: 'priority' // 'priority' | 'id' | 'title' | 'publisher'
  };

  // DOM Elements
  const el = {};

  function initElements() {
    el.tabs = document.querySelectorAll('.el-tab-btn');
    el.views = {
      catalog: document.getElementById('view-catalog'),
      queue: document.getElementById('view-queue'),
      topicMap: document.getElementById('view-topic-map'),
      workflow: document.getElementById('view-workflow')
    };
    el.search = document.getElementById('el-search-input');
    el.clearSearch = document.getElementById('el-clear-search');
    el.gradePills = document.querySelectorAll('[data-grade]');
    el.priorityPills = document.querySelectorAll('[data-priority]');
    el.topicSelect = document.getElementById('el-topic-select');
    el.formatSelect = document.getElementById('el-format-select');
    el.sortSelect = document.getElementById('el-sort-select');
    el.resetFilters = document.getElementById('el-reset-filters');
    el.countDisplay = document.getElementById('el-result-count');
    el.grid = document.getElementById('el-catalog-grid');
    el.queueTableBody = document.getElementById('el-queue-tbody');
    el.topicMapContainer = document.getElementById('el-topic-map-list');
    el.workflowContainer = document.getElementById('el-workflow-list');
    el.modal = document.getElementById('el-detail-modal');
    el.modalBody = document.getElementById('el-modal-body');
    el.modalClose = document.getElementById('el-modal-close');
  }

  function fetchCatalog() {
    fetch(CATALOG_URL)
      .then(function (res) {
        if (!res.ok) throw new Error('Failed to load library catalog: ' + res.status);
        return res.json();
      })
      .then(function (data) {
        libraryData = data;
        allCatalog = data.catalog || [];
        downloadQueue = data.download_queue || [];
        topicMap = data.topic_map || [];
        workflow = data.workflow || [];
        topStack = data.top_stack || [];
        credibilityRules = data.metadata.credibility_rules || {};

        populateTopicDropdown();
        renderQueueTable();
        renderTopicMap();
        renderWorkflow();
        applyFilters();
        handleHashNavigation();
      })
      .catch(function (err) {
        console.error('[PPRI Library] Error loading catalog JSON:', err);
        if (el.countDisplay) {
          el.countDisplay.textContent = 'Unable to load interactive index. Showing archived sources.';
        }
      });
  }

  function populateTopicDropdown() {
    if (!el.topicSelect) return;
    const topics = new Set();
    allCatalog.forEach(function (item) {
      if (item.topic) {
        const topCluster = item.topic.split('/')[0].trim();
        topics.add(topCluster);
      }
    });

    const sortedTopics = Array.from(topics).sort();
    sortedTopics.forEach(function (t) {
      const opt = document.createElement('option');
      opt.value = t;
      opt.textContent = t;
      el.topicSelect.appendChild(opt);
    });
  }

  function switchView(newView) {
    state.view = newView;
    if (el.tabs) {
      el.tabs.forEach(function (btn) {
        const isActive = btn.dataset.view === newView;
        btn.classList.toggle('active', isActive);
        btn.setAttribute('aria-selected', isActive ? 'true' : 'false');
      });
    }

    Object.keys(el.views).forEach(function (vKey) {
      if (el.views[vKey]) {
        el.views[vKey].hidden = vKey !== newView;
      }
    });

    // Update controls visibility: filters are primary in catalog view
    const filterBar = document.getElementById('el-filter-controls');
    if (filterBar) {
      filterBar.style.display = newView === 'catalog' ? 'block' : 'none';
    }
  }

  function filterCatalog() {
    const q = state.search.toLowerCase().trim();
    const grade = state.grade;
    const prio = state.priority;
    const topic = state.topic;
    const fmt = state.format;

    // Fast top-stack ID lookup
    const topStackNames = topStack.map(function (s) { return s.resource.toLowerCase(); });

    return allCatalog.filter(function (item) {
      // Grade filter
      if (grade !== 'all' && item.grade !== grade) return false;

      // Priority filter
      if (prio === 'top15') {
        const titleLow = item.title.toLowerCase();
        const matchesTop = topStackNames.some(function (ts) {
          return titleLow.indexOf(ts) !== -1 || ts.indexOf(titleLow) !== -1;
        });
        if (!matchesTop) return false;
      } else if (prio !== 'all' && item.suggested_priority !== prio) {
        return false;
      }

      // Topic filter
      if (topic !== 'all') {
        if (!item.topic || item.topic.toLowerCase().indexOf(topic.toLowerCase()) === -1) {
          return false;
        }
      }

      // Format filter
      if (fmt !== 'all') {
        const fLow = (item.formats_access || '').toLowerCase();
        const hasFmt = item.direct_entries && item.direct_entries.some(function (e) {
          return e.format.toLowerCase() === fmt.toLowerCase();
        });
        if (!hasFmt && fLow.indexOf(fmt.toLowerCase()) === -1) return false;
      }

      // Text Search
      if (q) {
        const corpus = [
          item.id,
          item.title,
          item.publisher,
          item.topic,
          item.research_uses,
          item.geographic_detail,
          item.formats_access,
          item.caveats
        ].join(' ').toLowerCase();

        if (corpus.indexOf(q) === -1) return false;
      }

      return true;
    });
  }

  function sortCatalog(items) {
    const s = state.sort;
    return items.slice().sort(function (a, b) {
      if (s === 'priority') {
        const pOrder = { P1: 1, P2: 2, P3: 3 };
        const pa = pOrder[a.suggested_priority] || 4;
        const pb = pOrder[b.suggested_priority] || 4;
        if (pa !== pb) return pa - pb;
        return a.id.localeCompare(b.id);
      }
      if (s === 'title') return a.title.localeCompare(b.title);
      if (s === 'publisher') return (a.publisher || '').localeCompare(b.publisher || '');
      if (s === 'id') return a.id.localeCompare(b.id);
      return 0;
    });
  }

  function applyFilters() {
    const filtered = filterCatalog();
    const sorted = sortCatalog(filtered);
    renderCatalogGrid(sorted);

    if (el.countDisplay) {
      el.countDisplay.innerHTML = 'Showing <strong>' + sorted.length + '</strong> of ' + allCatalog.length + ' datasets';
    }
  }

  function renderCatalogGrid(items) {
    if (!el.grid) return;

    if (items.length === 0) {
      el.grid.innerHTML = '<div class="el-empty-state"><p>No datasets match your active filters.</p><button type="button" class="btn btn-outline" id="el-empty-reset">Reset all filters</button></div>';
      const rBtn = document.getElementById('el-empty-reset');
      if (rBtn) rBtn.addEventListener('click', resetAllFilters);
      return;
    }

    let html = '';
    items.forEach(function (item) {
      const gradeClass = 'grade-' + item.grade.toLowerCase();
      const directBadge = item.direct_urls && item.direct_urls.length > 0
        ? '<span class="el-badge el-badge-direct">Direct Download (' + item.direct_urls.length + ')</span>'
        : '<span class="el-badge el-badge-portal">Portal Access</span>';

      const prioClass = 'prio-' + (item.suggested_priority || 'p2').toLowerCase();

      // Format badges
      let fmtBadges = '';
      if (item.direct_entries && item.direct_entries.length) {
        const uniqueFmts = Array.from(new Set(item.direct_entries.map(function (e) { return e.format; })));
        fmtBadges = uniqueFmts.map(function (f) {
          return '<span class="el-fmt-badge">' + f + '</span>';
        }).join(' ');
      }

      html += '<article class="el-card ' + prioClass + '" data-id="' + item.id + '">';
      html += '  <div class="el-card-header">';
      html += '    <div class="el-card-tags">';
      html += '      <span class="el-badge ' + gradeClass + '" title="' + getGradeTooltip(item.grade) + '">' + item.grade + ' Official</span>';
      html += '      <span class="el-badge el-badge-prio">' + item.suggested_priority + '</span>';
      html += '      ' + directBadge;
      html += '    </div>';
      html += '    <span class="el-card-id">' + item.id + '</span>';
      html += '  </div>';

      html += '  <h3 class="el-card-title"><a href="#' + item.id + '" class="el-open-detail" data-id="' + item.id + '">' + escapeHtml(item.title) + '</a></h3>';
      html += '  <p class="el-card-meta"><strong>' + escapeHtml(item.publisher || 'Official') + '</strong> &middot; <span>' + escapeHtml(item.period_coverage || 'Latest release') + '</span></p>';
      
      if (item.topic) {
        html += '  <p class="el-card-topic">' + escapeHtml(item.topic) + '</p>';
      }

      if (item.research_uses) {
        html += '  <p class="el-card-desc">' + escapeHtml(truncateText(item.research_uses, 130)) + '</p>';
      }

      html += '  <div class="el-card-footer">';
      html += '    <div class="el-card-fmts">' + fmtBadges + '</div>';
      html += '    <div class="el-card-actions">';
      if (item.direct_entries && item.direct_entries.length === 1) {
        html += '      <a href="' + item.direct_entries[0].url + '" target="_blank" rel="noopener noreferrer" class="el-btn-link el-btn-dl" title="Direct File Download">&#x2913; ' + escapeHtml(item.direct_entries[0].label) + '</a>';
      } else if (item.direct_entries && item.direct_entries.length > 1) {
        html += '      <button type="button" class="el-btn-link el-open-detail" data-id="' + item.id + '">&#x2913; Download (' + item.direct_entries.length + ')</button>';
      } else if (item.landing_page) {
        html += '      <a href="' + item.landing_page + '" target="_blank" rel="noopener noreferrer" class="el-btn-link" title="Open Official Portal">Portal &rarr;</a>';
      }
      html += '      <button type="button" class="el-btn-link el-btn-details el-open-detail" data-id="' + item.id + '">Details &rarr;</button>';
      html += '    </div>';
      html += '  </div>';
      html += '</article>';
    });

    el.grid.innerHTML = html;
  }

  function renderQueueTable() {
    if (!el.queueTableBody) return;
    let html = '';
    downloadQueue.forEach(function (q) {
      let downloadLinks = '';
      if (q.direct_entries && q.direct_entries.length) {
        downloadLinks = q.direct_entries.map(function (e) {
          return '<a href="' + e.url + '" target="_blank" rel="noopener noreferrer" class="el-queue-link">&#x2913; ' + escapeHtml(e.label) + ' (' + e.format + ')</a>';
        }).join('<br>');
      } else if (q.landing_page) {
        downloadLinks = '<a href="' + q.landing_page + '" target="_blank" rel="noopener noreferrer" class="el-queue-link">Portal Link &rarr;</a>';
      }

      html += '<tr>';
      html += '  <td><strong>' + q.queue_id + '</strong></td>';
      html += '  <td><span class="el-badge grade-' + q.grade.toLowerCase() + '">' + q.grade + '</span></td>';
      html += '  <td><span class="el-badge el-badge-prio">' + q.priority + '</span></td>';
      html += '  <td><strong>' + escapeHtml(q.resource_family) + '</strong><br><small class="text-muted">' + escapeHtml(q.topic) + '</small></td>';
      html += '  <td>' + escapeHtml(q.coverage || '') + '</td>';
      html += '  <td>' + downloadLinks + '</td>';
      html += '  <td><small class="text-caution">' + escapeHtml(q.caution || 'None noted') + '</small></td>';
      html += '</tr>';
    });
    el.queueTableBody.innerHTML = html;
  }

  function renderTopicMap() {
    if (!el.topicMapContainer) return;
    let html = '';
    topicMap.forEach(function (t, idx) {
      html += '<div class="el-topic-card">';
      html += '  <div class="el-topic-header">';
      html += '    <span class="el-topic-idx">' + (idx + 1) + '</span>';
      html += '    <h3>' + escapeHtml(t.domain) + '</h3>';
      html += '  </div>';
      html += '  <div class="el-topic-body">';
      html += '    <div class="el-topic-col">';
      html += '      <h4>Official Primary Sources (A1)</h4>';
      html += '      <p>' + escapeHtml(t.primary_official) + '</p>';
      html += '      <h4>Target File / Structure</h4>';
      html += '      <p><code>' + escapeHtml(t.target_official_file) + '</code></p>';
      html += '    </div>';
      html += '    <div class="el-topic-col">';
      html += '      <h4>Harmonized / External Comparators (A2)</h4>';
      html += '      <p>' + escapeHtml(t.external_comparators) + '</p>';
      html += '      <h4>Geographic Detail</h4>';
      html += '      <p>' + escapeHtml(t.geographic_detail) + '</p>';
      html += '    </div>';
      html += '  </div>';
      if (t.analytical_uses || t.method_caveats) {
        html += '  <div class="el-topic-notes">';
        if (t.analytical_uses) html += '<div><strong>Analytical Uses:</strong> ' + escapeHtml(t.analytical_uses) + '</div>';
        if (t.method_caveats) html += '<div class="el-trap-box"><strong>Caution / Method Pitfall:</strong> ' + escapeHtml(t.method_caveats) + '</div>';
        html += '  </div>';
      }
      html += '</div>';
    });
    el.topicMapContainer.innerHTML = html;
  }

  function renderWorkflow() {
    if (!el.workflowContainer) return;
    let html = '';
    workflow.forEach(function (step) {
      html += '<div class="el-workflow-step">';
      html += '  <div class="el-step-badge">Step ' + step.step + '</div>';
      html += '  <div class="el-step-content">';
      html += '    <h4>' + escapeHtml(step.checkpoint) + '</h4>';
      html += '    <p class="el-step-desc">' + escapeHtml(step.what_to_do) + '</p>';
      html += '    <div class="el-step-evidence"><strong>Evidence to Save:</strong> <code>' + escapeHtml(step.evidence_to_save) + '</code></div>';
      html += '  </div>';
      html += '</div>';
    });
    el.workflowContainer.innerHTML = html;
  }

  function openModal(itemId) {
    const item = allCatalog.find(function (c) { return c.id === itemId; });
    if (!item || !el.modal || !el.modalBody) return;

    let directListHtml = '';
    if (item.direct_entries && item.direct_entries.length) {
      directListHtml += '<div class="el-modal-section">';
      directListHtml += '  <h4>Direct Acquisition Files (' + item.direct_entries.length + ')</h4>';
      directListHtml += '  <ul class="el-modal-dl-list">';
      item.direct_entries.forEach(function (e) {
        directListHtml += '    <li>';
        directListHtml += '      <a href="' + e.url + '" target="_blank" rel="noopener noreferrer" class="btn btn-outline btn-sm">&#x2913; Download ' + escapeHtml(e.label) + ' <span class="badge">' + e.format + '</span></a>';
        directListHtml += '      <span class="el-url-sub">' + escapeHtml(e.url) + '</span>';
        directListHtml += '    </li>';
      });
      directListHtml += '  </ul>';
      directListHtml += '</div>';
    }

    const citationText = generateCitation(item);

    let html = '';
    html += '<div class="el-modal-head-row">';
    html += '  <span class="el-badge grade-' + item.grade.toLowerCase() + '">' + item.grade + ' Official</span>';
    html += '  <span class="el-badge el-badge-prio">Priority ' + item.suggested_priority + '</span>';
    html += '  <span class="el-card-id">' + item.id + '</span>';
    html += '</div>';

    html += '<h2 class="el-modal-title">' + escapeHtml(item.title) + '</h2>';
    html += '<div class="el-modal-meta-grid">';
    html += '  <div><strong>Publisher / Owner:</strong> ' + escapeHtml(item.publisher || 'Official') + '</div>';
    html += '  <div><strong>Period / Coverage:</strong> ' + escapeHtml(item.period_coverage || 'Current') + '</div>';
    html += '  <div><strong>Topic / Category:</strong> ' + escapeHtml(item.topic || 'General') + '</div>';
    html += '  <div><strong>Geographic Level:</strong> ' + escapeHtml(item.geographic_detail || 'National') + '</div>';
    html += '  <div><strong>Formats & Access:</strong> ' + escapeHtml(item.formats_access || 'Digital') + '</div>';
    html += '  <div><strong>Status:</strong> <span class="badge">' + escapeHtml(item.acquisition_status || 'Ready') + '</span></div>';
    html += '</div>';

    if (item.landing_page) {
      html += '<div class="el-modal-link-box">';
      html += '  <strong>Official Landing Page:</strong> <a href="' + item.landing_page + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(item.landing_page) + ' &rarr;</a>';
      html += '</div>';
    }

    html += directListHtml;

    if (item.research_uses) {
      html += '<div class="el-modal-section">';
      html += '  <h4>Research Uses & Key Variables</h4>';
      html += '  <p>' + escapeHtml(item.research_uses) + '</p>';
      html += '</div>';
    }

    if (item.caveats) {
      html += '<div class="el-modal-section el-modal-alert">';
      html += '  <h4>Access, Quality & Methodological Caveats</h4>';
      html += '  <p>' + escapeHtml(item.caveats) + '</p>';
      html += '</div>';
    }

    if (item.verification_note) {
      html += '<div class="el-modal-section">';
      html += '  <h4>Verification Note</h4>';
      html += '  <p>' + escapeHtml(item.verification_note) + '</p>';
      html += '</div>';
    }

    // Citation box
    html += '<div class="el-modal-section el-citation-box">';
    html += '  <div class="el-citation-head">';
    html += '    <h4>Academic & Policy Citation</h4>';
    html += '    <button type="button" class="btn btn-sm btn-outline" id="el-copy-citation">&#x2398; Copy Citation</button>';
    html += '  </div>';
    html += '  <pre id="el-citation-text">' + escapeHtml(citationText) + '</pre>';
    html += '</div>';

    el.modalBody.innerHTML = html;
    el.modal.hidden = false;
    document.body.classList.add('modal-open');

    const copyBtn = document.getElementById('el-copy-citation');
    if (copyBtn) {
      copyBtn.addEventListener('click', function () {
        navigator.clipboard.writeText(citationText).then(function () {
          copyBtn.textContent = 'Copied to Clipboard!';
          setTimeout(function () { copyBtn.textContent = 'Copy Citation'; }, 2000);
        });
      });
    }

    history.replaceState(null, '', '#' + item.id);
  }

  function closeModal() {
    if (!el.modal) return;
    el.modal.hidden = true;
    document.body.classList.remove('modal-open');
    history.replaceState(null, '', window.location.pathname + window.location.search);
  }

  function generateCitation(item) {
    const year = (item.period_coverage && item.period_coverage.match(/\d{4}/)) ? item.period_coverage.match(/\d{4}/)[0] : '2026';
    const publisher = item.publisher || 'Government of Pakistan';
    const title = item.title;
    const url = item.landing_page || (item.direct_urls && item.direct_urls[0]) || 'https://ppripakistan.github.io/sources/';
    return publisher + ' (' + year + '). ' + title + ' [' + item.id + ']. Retrieved from ' + url + ' via PPRI Pakistan Data Resource Inventory.';
  }

  function getGradeTooltip(grade) {
    const r = credibilityRules[grade];
    return r ? r.title + ': ' + r.description : 'Official Tier';
  }

  function truncateText(str, len) {
    if (!str || str.length <= len) return str;
    return str.substring(0, len).trim() + '...';
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function resetAllFilters() {
    state.search = '';
    state.grade = 'all';
    state.priority = 'all';
    state.topic = 'all';
    state.format = 'all';
    state.sort = 'priority';

    if (el.search) el.search.value = '';
    if (el.clearSearch) el.clearSearch.hidden = true;
    if (el.topicSelect) el.topicSelect.value = 'all';
    if (el.formatSelect) el.formatSelect.value = 'all';
    if (el.sortSelect) el.sortSelect.value = 'priority';

    if (el.gradePills) {
      el.gradePills.forEach(function (p) {
        p.classList.toggle('active', p.dataset.grade === 'all');
      });
    }
    if (el.priorityPills) {
      el.priorityPills.forEach(function (p) {
        p.classList.toggle('active', p.dataset.priority === 'all');
      });
    }

    applyFilters();
  }

  function handleHashNavigation() {
    const hash = window.location.hash.replace('#', '').trim();
    if (hash && hash.startsWith('PKD-')) {
      openModal(hash);
    }
  }

  function bindEvents() {
    // View Tab Switch
    if (el.tabs) {
      el.tabs.forEach(function (btn) {
        btn.addEventListener('click', function () {
          switchView(btn.dataset.view);
        });
      });
    }

    // Search Input
    if (el.search) {
      el.search.addEventListener('input', function (e) {
        state.search = e.target.value;
        if (el.clearSearch) el.clearSearch.hidden = !state.search;
        applyFilters();
      });
    }

    if (el.clearSearch) {
      el.clearSearch.addEventListener('click', function () {
        state.search = '';
        el.search.value = '';
        el.clearSearch.hidden = true;
        applyFilters();
      });
    }

    // Grade Filter Pills
    if (el.gradePills) {
      el.gradePills.forEach(function (pill) {
        pill.addEventListener('click', function () {
          el.gradePills.forEach(function (p) { p.classList.remove('active'); });
          pill.classList.add('active');
          state.grade = pill.dataset.grade;
          applyFilters();
        });
      });
    }

    // Priority Filter Pills
    if (el.priorityPills) {
      el.priorityPills.forEach(function (pill) {
        pill.addEventListener('click', function () {
          el.priorityPills.forEach(function (p) { p.classList.remove('active'); });
          pill.classList.add('active');
          state.priority = pill.dataset.priority;
          applyFilters();
        });
      });
    }

    // Dropdowns
    if (el.topicSelect) {
      el.topicSelect.addEventListener('change', function (e) {
        state.topic = e.target.value;
        applyFilters();
      });
    }

    if (el.formatSelect) {
      el.formatSelect.addEventListener('change', function (e) {
        state.format = e.target.value;
        applyFilters();
      });
    }

    if (el.sortSelect) {
      el.sortSelect.addEventListener('change', function (e) {
        state.sort = e.target.value;
        applyFilters();
      });
    }

    if (el.resetFilters) {
      el.resetFilters.addEventListener('click', resetAllFilters);
    }

    // Modal Events
    document.addEventListener('click', function (e) {
      const openBtn = e.target.closest('.el-open-detail');
      if (openBtn) {
        e.preventDefault();
        const id = openBtn.dataset.id;
        if (id) openModal(id);
      }
    });

    if (el.modalClose) {
      el.modalClose.addEventListener('click', closeModal);
    }

    if (el.modal) {
      el.modal.addEventListener('click', function (e) {
        if (e.target === el.modal) closeModal();
      });
    }

    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && el.modal && !el.modal.hidden) {
        closeModal();
      }
    });

    window.addEventListener('hashchange', handleHashNavigation);
  }

  // Bootstrap
  document.addEventListener('DOMContentLoaded', function () {
    initElements();
    bindEvents();
    fetchCatalog();
  });
})();
