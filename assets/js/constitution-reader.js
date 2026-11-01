/**
 * PPRI Constitution Explorer — Modernized Interactive Reader Engine (assets/js/constitution-reader.js)
 * High-performance, accessible client-side reader for all 280 Articles + Schedules.
 */

(function () {
  'use strict';

  let articlesCache = [];
  let filteredArticles = [];
  let currentIndex = 0;
  let activeViewMode = 'salient'; // 'salient' | 'text' | 'both'
  let toastTimer = null;

  const el = {
    partFilter: document.getElementById('reader-part-filter'),
    searchInput: document.getElementById('reader-search-input'),
    searchClear: document.getElementById('reader-search-clear'),
    searchHint: document.getElementById('reader-search-hint'),
    resultsCount: document.getElementById('reader-results-count'),
    tocPane: document.getElementById('reader-toc-pane'),
    tocList: document.getElementById('reader-toc-list'),
    mobileTocToggle: document.getElementById('mobile-toc-toggle'),
    mobileCurrentArt: document.getElementById('mobile-current-art'),
    drawerOverlay: document.getElementById('reader-drawer-overlay'),
    drawerCloseBtn: document.getElementById('reader-drawer-close-btn'),
    articlePane: document.getElementById('reader-article-pane'),
    breadcrumb: document.getElementById('reader-breadcrumb'),
    artTitle: document.getElementById('reader-art-title'),
    statusBadge: document.getElementById('reader-status-badge'),
    salientSection: document.getElementById('section-salient'),
    salientText: document.getElementById('reader-salient-text'),
    textSection: document.getElementById('section-text'),
    clausesBox: document.getElementById('reader-clauses-box'),
    tabSalient: document.getElementById('tab-btn-salient'),
    tabText: document.getElementById('tab-btn-text'),
    tabBoth: document.getElementById('tab-btn-both'),
    fontSm: document.getElementById('font-btn-sm'),
    fontMd: document.getElementById('font-btn-md'),
    fontLg: document.getElementById('font-btn-lg'),
    citationBtn: document.getElementById('reader-citation-btn'),
    toast: document.getElementById('reader-toast'),
    toastMsg: document.getElementById('reader-toast-msg'),
    prevBtn: document.getElementById('reader-prev-btn'),
    nextBtn: document.getElementById('reader-next-btn'),
    navIndicator: document.getElementById('reader-nav-indicator'),
    copyLinkBtn: document.getElementById('reader-copy-link-btn'),
    amendedNotice: document.getElementById('reader-amended-notice')
  };

  // URL parameters
  const urlParams = new URLSearchParams(window.location.search);
  const paramArt = urlParams.get('article');
  const paramPart = urlParams.get('part');

  // Load articles dataset
  fetch('/data/constitution/articles.json')
    .then(r => {
      if (!r.ok) throw new Error('HTTP ' + r.status);
      return r.json();
    })
    .then(data => {
      articlesCache = data;
      filteredArticles = [...articlesCache];

      // Handle initial part filter from URL
      if (paramPart && el.partFilter) {
        const option = Array.from(el.partFilter.options).find(o => o.value.toLowerCase() === paramPart.toLowerCase());
        if (option) {
          el.partFilter.value = option.value;
          applyFilters();
        }
      }

      // Handle initial article from URL
      if (paramArt) {
        const idx = articlesCache.findIndex(a => a.article_number.toLowerCase() === paramArt.trim().toLowerCase());
        if (idx !== -1) {
          currentIndex = idx;
        }
      } else {
        const defaultIdx = articlesCache.findIndex(a => a.article_number === '1');
        currentIndex = defaultIdx !== -1 ? defaultIdx : 0;
      }

      renderTOC();
      displayArticle(currentIndex);
      setupEvents();
    })
    .catch(err => {
      console.error('Failed to load articles:', err);
      if (el.tocList) {
        el.tocList.innerHTML = '<div style="padding:16px;color:#c53030;">Failed to load Constitution database. Please check connection.</div>';
      }
    });

  function showToast(message) {
    if (!el.toast) return;
    if (el.toastMsg) el.toastMsg.textContent = message;
    el.toast.classList.add('is-visible');
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      el.toast.classList.remove('is-visible');
    }, 2500);
  }

  function setFontSize(size) {
    if (!el.articlePane) return;
    el.articlePane.classList.remove('reader-font-sm', 'reader-font-md', 'reader-font-lg');
    el.articlePane.classList.add(`reader-font-${size}`);

    if (el.fontSm) el.fontSm.classList.toggle('is-active', size === 'sm');
    if (el.fontMd) el.fontMd.classList.toggle('is-active', size === 'md');
    if (el.fontLg) el.fontLg.classList.toggle('is-active', size === 'lg');

    try {
      localStorage.setItem('ppri_reader_font_size', size);
    } catch (_) {}
  }

  function openMobileDrawer() {
    if (el.tocPane) el.tocPane.classList.add('drawer-open');
    if (el.drawerOverlay) el.drawerOverlay.classList.add('is-visible');
  }

  function closeMobileDrawer() {
    if (el.tocPane) el.tocPane.classList.remove('drawer-open');
    if (el.drawerOverlay) el.drawerOverlay.classList.remove('is-visible');
  }

  function applyFilters() {
    const selectedPart = el.partFilter ? el.partFilter.value : 'ALL';
    const query = el.searchInput ? el.searchInput.value.trim().toLowerCase() : '';

    filteredArticles = articlesCache.filter(a => {
      // Part match
      if (selectedPart !== 'ALL') {
        if (selectedPart === 'Schedules') {
          if (!a.part.toLowerCase().includes('schedule')) return false;
        } else if (a.part.toLowerCase() !== selectedPart.toLowerCase()) {
          return false;
        }
      }

      // Query match
      if (query) {
        const numMatch = a.article_number.toLowerCase().includes(query);
        const titleMatch = a.title.toLowerCase().includes(query);
        const tagMatch = a.tags && a.tags.some(t => t.toLowerCase().includes(query));
        const salientMatch = a.salient_points && a.salient_points.toLowerCase().includes(query);
        return numMatch || titleMatch || tagMatch || salientMatch;
      }

      return true;
    });

    if (el.resultsCount) {
      el.resultsCount.textContent = `Showing ${filteredArticles.length} of ${articlesCache.length} entries`;
    }

    renderTOC();

    if (filteredArticles.length > 0) {
      const currentArt = articlesCache[currentIndex];
      const newIdx = filteredArticles.findIndex(a => a.article_number === (currentArt ? currentArt.article_number : ''));
      if (newIdx === -1) {
        displayArticleByArtNumber(filteredArticles[0].article_number);
      } else {
        highlightActiveTOC(currentArt.article_number);
      }
    }
  }

  function renderTOC() {
    if (!el.tocList) return;
    el.tocList.innerHTML = '';

    if (filteredArticles.length === 0) {
      el.tocList.innerHTML = '<div style="padding: 16px; color: #64748b; text-align: center;">No matching articles found.</div>';
      return;
    }

    const fragment = document.createDocumentFragment();
    filteredArticles.forEach(art => {
      const item = document.createElement('a');
      item.href = `?article=${encodeURIComponent(art.article_number)}`;
      item.className = 'reader-toc-item';
      item.dataset.artNum = art.article_number;

      const prefix = art.article_number.toLowerCase().includes('schedule') || art.article_number.toLowerCase().includes('preamble')
        ? art.article_number
        : `Art. ${art.article_number}`;

      item.innerHTML = `<div style="display:flex; justify-content:space-between; align-items:center;">
        <strong>${escapeHTML(prefix)}</strong>
        ${art.status === 'omitted' ? '<span style="font-size:0.7rem; color:#dc2626;">Omitted</span>' : ''}
      </div>
      <div style="font-size:0.82rem; color:#475569; margin-top:2px; line-height:1.35;">${escapeHTML(art.title)}</div>`;

      item.addEventListener('click', (e) => {
        e.preventDefault();
        displayArticleByArtNumber(art.article_number);
        history.pushState(null, '', `?article=${encodeURIComponent(art.article_number)}`);
        closeMobileDrawer();
      });

      fragment.appendChild(item);
    });

    el.tocList.appendChild(fragment);

    const currentArt = articlesCache[currentIndex];
    if (currentArt) {
      highlightActiveTOC(currentArt.article_number);
    }
  }

  function highlightActiveTOC(artNumber) {
    if (!el.tocList) return;
    const items = el.tocList.querySelectorAll('.reader-toc-item');
    items.forEach(item => {
      const isMatch = item.dataset.artNum === artNumber;
      item.classList.toggle('is-active', isMatch);
      if (isMatch) {
        item.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      }
    });
  }

  function displayArticleByArtNumber(artNumber) {
    const idx = articlesCache.findIndex(a => a.article_number === artNumber);
    if (idx !== -1) {
      currentIndex = idx;
      displayArticle(currentIndex);
    }
  }

  function displayArticle(index) {
    const art = articlesCache[index];
    if (!art) return;

    // Mobile Current Art Indicator
    if (el.mobileCurrentArt) {
      const prefix = art.article_number.toLowerCase().includes('schedule') || art.article_number.toLowerCase().includes('preamble')
        ? art.article_number
        : `Art. ${art.article_number}`;
      el.mobileCurrentArt.textContent = prefix;
    }

    // Breadcrumb
    if (el.breadcrumb) {
      const breadcrumbParts = [art.part];
      if (art.part_title && art.part_title !== art.part) breadcrumbParts.push(art.part_title);
      if (art.chapter) breadcrumbParts.push(art.chapter + (art.chapter_title ? `: ${art.chapter_title}` : ''));
      el.breadcrumb.textContent = breadcrumbParts.join(' • ');
    }

    // Title
    if (el.artTitle) {
      const prefix = art.article_number.toLowerCase().includes('schedule') || art.article_number.toLowerCase().includes('preamble')
        ? ''
        : `Article ${art.article_number}: `;
      el.artTitle.textContent = `${prefix}${art.title}`;
    }

    // Status Badge
    if (el.statusBadge) {
      if (art.status === 'omitted') {
        el.statusBadge.innerHTML = '<span class="const-badge const-badge-gold"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/></svg>Omitted / Repealed</span>';
      } else {
        el.statusBadge.innerHTML = '<span class="const-badge const-badge-primary"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>In Force</span>';
      }
    }

    // Amendment Reference Banner
    if (el.amendedNotice) {
      const amendmentsMap = {
        "9A": { num: 26, title: "26th Amendment (2024)" },
        "10A": { num: 18, title: "18th Amendment (2010)" },
        "19A": { num: 18, title: "18th Amendment (2010)" },
        "25A": { num: 18, title: "18th Amendment (2010)" },
        "63A": { num: 14, title: "14th & 18th Amendments" },
        "140A": { num: 18, title: "18th Amendment (2010)" },
        "160": { num: 18, title: "18th Amendment (Clause 3A)" },
        "172": { num: 18, title: "18th Amendment (Clause 3)" },
        "175A": { num: 18, title: "18th, 19th, 26th & 27th Amendments" },
        "191A": { num: 26, title: "26th & 27th Amendments (Constitutional Benches)" },
        "246": { num: 25, title: "25th Amendment (FATA Merger)" },
        "247": { num: 25, title: "25th Amendment (Omitted)" }
      };

      const amendedInfo = amendmentsMap[art.article_number];
      if (amendedInfo) {
        el.amendedNotice.style.display = 'block';
        el.amendedNotice.innerHTML = `<span style="font-size:0.85rem; color:#854d0e; display:inline-flex; align-items:center; gap:6px;">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
          <strong>Constitutional Amendment Context:</strong> Inserted / Amended by 
          <a href="/constitution/amendments/#amendment-${amendedInfo.num}" style="color:#073c3a; text-decoration:underline; font-weight:700;">${amendedInfo.title}</a>
        </span>`;
      } else {
        el.amendedNotice.style.display = 'none';
      }
    }

    // Salient Points
    if (el.salientText) {
      el.salientText.textContent = art.salient_points || 'Salient points summary for this article is being updated.';
    }

    // Clauses / Constitutional Text
    if (el.clausesBox) {
      el.clausesBox.innerHTML = '';
      if (art.clauses && art.clauses.length > 0) {
        art.clauses.forEach((clause, i) => {
          const div = document.createElement('div');
          div.className = 'reader-clause-item';
          div.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:4px;">
              <span style="font-size:0.75rem; font-weight:700; color:#b08a49; text-transform:uppercase;">Clause ${i + 1}</span>
              <button class="clause-copy-btn" title="Copy this clause" style="background:none; border:none; cursor:pointer; color:#64748b; padding:2px;" type="button">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              </button>
            </div>
            <p style="margin:0; font-family:Georgia, serif; line-height:1.75; color:#1e293b;">${escapeHTML(clause)}</p>
          `;

          const copyBtn = div.querySelector('.clause-copy-btn');
          if (copyBtn) {
            copyBtn.addEventListener('click', () => {
              navigator.clipboard.writeText(clause).then(() => {
                copyBtn.innerHTML = '<span style="font-size:0.72rem; color:#15803d; font-weight:bold;">Copied!</span>';
                setTimeout(() => {
                  copyBtn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>';
                }, 1800);
              });
            });
          }

          el.clausesBox.appendChild(div);
        });
      } else {
        el.clausesBox.textContent = 'Constitutional text pending official verification against Gazette records.';
      }
    }

    // Active TOC item
    highlightActiveTOC(art.article_number);

    // Nav indicator & Pagination
    if (el.navIndicator) {
      const artDisplay = art.article_number.toLowerCase().includes('schedule') || art.article_number.toLowerCase().includes('preamble')
        ? art.article_number
        : `Article ${art.article_number}`;
      el.navIndicator.textContent = `${artDisplay} (${index + 1} of ${articlesCache.length})`;
    }

    if (el.prevBtn) el.prevBtn.disabled = (index <= 0);
    if (el.nextBtn) el.nextBtn.disabled = (index >= articlesCache.length - 1);

    updateViewMode();
  }

  function updateViewMode() {
    if (!el.salientSection || !el.textSection) return;

    if (activeViewMode === 'salient') {
      el.salientSection.style.display = 'block';
      el.textSection.style.display = 'none';
      if (el.tabSalient) el.tabSalient.classList.add('is-active');
      if (el.tabText) el.tabText.classList.remove('is-active');
      if (el.tabBoth) el.tabBoth.classList.remove('is-active');
    } else if (activeViewMode === 'text') {
      el.salientSection.style.display = 'none';
      el.textSection.style.display = 'block';
      if (el.tabSalient) el.tabSalient.classList.remove('is-active');
      if (el.tabText) el.tabText.classList.add('is-active');
      if (el.tabBoth) el.tabBoth.classList.remove('is-active');
    } else { // 'both'
      el.salientSection.style.display = 'block';
      el.textSection.style.display = 'block';
      if (el.tabSalient) el.tabSalient.classList.remove('is-active');
      if (el.tabText) el.tabText.classList.remove('is-active');
      if (el.tabBoth) el.tabBoth.classList.add('is-active');
    }
  }

  function setupEvents() {
    if (el.partFilter) el.partFilter.addEventListener('change', applyFilters);

    if (el.searchInput) {
      el.searchInput.addEventListener('input', () => {
        applyFilters();
        const hasVal = el.searchInput.value.trim().length > 0;
        if (el.searchClear) el.searchClear.style.display = hasVal ? 'block' : 'none';
        if (el.searchHint) el.searchHint.style.display = hasVal ? 'none' : 'block';
      });
    }

    if (el.searchClear) {
      el.searchClear.addEventListener('click', () => {
        if (el.searchInput) {
          el.searchInput.value = '';
          applyFilters();
          el.searchClear.style.display = 'none';
          if (el.searchHint) el.searchHint.style.display = 'block';
          el.searchInput.focus();
        }
      });
    }

    // Mobile Drawer events
    if (el.mobileTocToggle) el.mobileTocToggle.addEventListener('click', openMobileDrawer);
    if (el.drawerCloseBtn) el.drawerCloseBtn.addEventListener('click', closeMobileDrawer);
    if (el.drawerOverlay) el.drawerOverlay.addEventListener('click', closeMobileDrawer);

    // Font size adjustments
    if (el.fontSm) el.fontSm.addEventListener('click', () => setFontSize('sm'));
    if (el.fontMd) el.fontMd.addEventListener('click', () => setFontSize('md'));
    if (el.fontLg) el.fontLg.addEventListener('click', () => setFontSize('lg'));

    try {
      const savedFont = localStorage.getItem('ppri_reader_font_size');
      if (savedFont && ['sm', 'md', 'lg'].includes(savedFont)) {
        setFontSize(savedFont);
      }
    } catch (_) {}

    // View switcher tabs
    if (el.tabSalient) {
      el.tabSalient.addEventListener('click', () => {
        activeViewMode = 'salient';
        updateViewMode();
      });
    }
    if (el.tabText) {
      el.tabText.addEventListener('click', () => {
        activeViewMode = 'text';
        updateViewMode();
      });
    }
    if (el.tabBoth) {
      el.tabBoth.addEventListener('click', () => {
        activeViewMode = 'both';
        updateViewMode();
      });
    }

    // Previous / Next Buttons
    if (el.prevBtn) {
      el.prevBtn.addEventListener('click', () => {
        if (currentIndex > 0) {
          currentIndex--;
          displayArticle(currentIndex);
          history.pushState(null, '', `?article=${encodeURIComponent(articlesCache[currentIndex].article_number)}`);
        }
      });
    }
    if (el.nextBtn) {
      el.nextBtn.addEventListener('click', () => {
        if (currentIndex < articlesCache.length - 1) {
          currentIndex++;
          displayArticle(currentIndex);
          history.pushState(null, '', `?article=${encodeURIComponent(articlesCache[currentIndex].article_number)}`);
        }
      });
    }

    // Keyboard navigation & search shortcut '/'
    window.addEventListener('keydown', (e) => {
      if (e.key === '/' && document.activeElement !== el.searchInput && !['INPUT', 'SELECT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
        e.preventDefault();
        if (el.searchInput) {
          el.searchInput.focus();
          el.searchInput.select();
        }
        return;
      }

      if (['INPUT', 'SELECT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

      if (e.key === 'ArrowLeft' && currentIndex > 0) {
        currentIndex--;
        displayArticle(currentIndex);
        history.pushState(null, '', `?article=${encodeURIComponent(articlesCache[currentIndex].article_number)}`);
      } else if (e.key === 'ArrowRight' && currentIndex < articlesCache.length - 1) {
        currentIndex++;
        displayArticle(currentIndex);
        history.pushState(null, '', `?article=${encodeURIComponent(articlesCache[currentIndex].article_number)}`);
      }
    });

    // Copy Provision Link button
    if (el.copyLinkBtn) {
      el.copyLinkBtn.addEventListener('click', () => {
        const art = articlesCache[currentIndex];
        if (!art) return;
        const url = `${window.location.origin}/constitution/reader/?article=${encodeURIComponent(art.article_number)}`;
        navigator.clipboard.writeText(url).then(() => {
          showToast('Provision URL copied to clipboard!');
        }).catch(() => {
          prompt('Copy article URL:', url);
        });
      });
    }

    // Standardized Legal Citation button
    if (el.citationBtn) {
      el.citationBtn.addEventListener('click', () => {
        const art = articlesCache[currentIndex];
        if (!art) return;
        const prefix = art.article_number.toLowerCase().includes('schedule') || art.article_number.toLowerCase().includes('preamble')
          ? art.article_number
          : `Art. ${art.article_number}`;
        const citation = `Constitution of the Islamic Republic of Pakistan, 1973, ${prefix}: ${art.title} (Fourteenth Edition, amended up to 21 November 2025). Pakistan Provincial Reform Institute (PPRI). https://ppripakistan.github.io/constitution/reader/?article=${encodeURIComponent(art.article_number)}`;

        navigator.clipboard.writeText(citation).then(() => {
          showToast('Legal citation copied to clipboard!');
        }).catch(() => {
          prompt('Copy citation:', citation);
        });
      });
    }
  }

  function escapeHTML(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }
})();
