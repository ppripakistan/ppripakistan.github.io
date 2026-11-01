/**
 * PPRI Constitution Explorer — Amendments Controller (assets/js/constitution-amendments.js)
 * Powers filter pills and instant search for the Constitutional Amendments Register (1–27).
 */

(function () {
  'use strict';

  let amendmentsCache = [];
  let currentFilter = 'ALL';
  let searchQuery = '';

  const elements = {
    searchInput: document.getElementById('amendments-search-input'),
    pillGroup: document.getElementById('amendments-pill-group'),
    cardsContainer: document.getElementById('amendments-cards-container'),
    resultsCounter: document.getElementById('amendments-results-counter')
  };

  fetch('/data/constitution/amendment-register.json')
    .then(r => r.json())
    .then(data => {
      amendmentsCache = data;
      renderCards();
      setupEvents();
    })
    .catch(err => {
      console.error('Failed to load amendment register:', err);
      if (elements.cardsContainer) {
        elements.cardsContainer.innerHTML = '<div style="padding: 24px; color: #dc2626;">Failed to load amendments data.</div>';
      }
    });

  function renderCards() {
    if (!elements.cardsContainer) return;

    const filtered = amendmentsCache.filter(item => {
      // Pill Filter
      if (currentFilter === 'ENACTED' && item.status !== 'enacted') return false;
      if (currentFilter === 'UNENACTED' && item.status !== 'un_enacted_bill') return false;
      if (currentFilter === 'PROVINCIAL') {
        const isProvincial = [1, 5, 8, 18, 24, 25].includes(item.position);
        if (!isProvincial) return false;
      }

      // Search Query
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        const posMatch = String(item.position).includes(q);
        const titleMatch = item.official_title.toLowerCase().includes(q) || item.short_title.toLowerCase().includes(q);
        const impactMatch = item.substantive_impact.toLowerCase().includes(q);
        const articlesMatch = item.affected_articles && item.affected_articles.some(a => a.toLowerCase().includes(q));
        return posMatch || titleMatch || impactMatch || articlesMatch;
      }

      return true;
    });

    if (elements.resultsCounter) {
      elements.resultsCounter.textContent = `Showing ${filtered.length} of ${amendmentsCache.length} amendment positions`;
    }

    if (filtered.length === 0) {
      elements.cardsContainer.innerHTML = '<div style="padding: 32px; text-align: center; color: #64748b; grid-column: 1 / -1;">No matching amendments found.</div>';
      return;
    }

    elements.cardsContainer.innerHTML = '';
    const fragment = document.createDocumentFragment();

    filtered.forEach(item => {
      const card = document.createElement('article');
      card.className = 'const-amendment-card';
      card.id = `amendment-${item.position}`;

      const isEnacted = item.status === 'enacted';
      const statusPill = isEnacted
        ? `<span class="const-badge const-badge-primary"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>Enacted Act</span>`
        : `<span class="const-badge const-badge-gold"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>Un-enacted Historical Proposal</span>`;

      const dateMeta = isEnacted && item.assent_date
        ? `<span class="const-amendment-meta-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>Assent: ${escapeHTML(item.assent_date)}</span>`
        : `<span class="const-amendment-meta-item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/></svg>Lapsed / Never Assented</span>`;

      // Affected articles tags
      let tagsHTML = '';
      if (item.affected_articles && item.affected_articles.length > 0) {
        tagsHTML = item.affected_articles.map(art => 
          `<a class="const-tag-pill" href="/constitution/reader/?article=${encodeURIComponent(art)}" title="Read Article ${escapeHTML(art)} in Reader">Art. ${escapeHTML(art)}</a>`
        ).join('');
      }

      // Key changes list
      const changesList = item.key_changes.map(ch => `<li>${escapeHTML(ch)}</li>`).join('');

      card.innerHTML = `
        <div class="const-amendment-header">
          <div>
            <div style="font-size:0.8rem; font-weight:700; color:#b08a49; text-transform:uppercase; margin-bottom:2px;">Position ${item.position} of 27</div>
            <h3 class="const-amendment-title">${escapeHTML(item.short_title)}</h3>
          </div>
          ${statusPill}
        </div>

        <div class="const-amendment-meta">
          ${dateMeta}
          <span style="color:#073c3a; font-weight:600;">${escapeHTML(item.official_title)}</span>
        </div>

        <div class="const-amendment-impact">
          <strong>Substantive Governance Impact:</strong> ${escapeHTML(item.substantive_impact)}
        </div>

        <div style="font-size: 0.92rem; color: #334155; margin-bottom: 14px;">
          <strong style="color: #073c3a;">Key Provisions:</strong>
          <ul style="margin: 6px 0 0; padding-left: 18px; line-height: 1.5;">
            ${changesList}
          </ul>
        </div>

        <div class="const-tag-list">
          <span style="font-size: 0.78rem; font-weight: 700; color: #64748b; margin-right: 4px;">Affected:</span>
          ${tagsHTML}
        </div>
      `;

      fragment.appendChild(card);
    });

    elements.cardsContainer.appendChild(fragment);
  }

  function setupEvents() {
    // Search input
    if (elements.searchInput) {
      elements.searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value.trim();
        renderCards();
      });
    }

    // Filter pills
    if (elements.pillGroup) {
      const pills = elements.pillGroup.querySelectorAll('.const-filter-pill');
      pills.forEach(pill => {
        pill.addEventListener('click', () => {
          pills.forEach(p => p.classList.remove('is-active'));
          pill.classList.add('is-active');
          currentFilter = pill.dataset.filter;
          renderCards();
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
