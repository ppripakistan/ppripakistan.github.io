/**
 * PPRI Constitution Explorer — Hub Interactive Controller (assets/js/constitution-hub.js)
 * Powers the Quick Article Finder live widget, Visual Atlas previews, and the Interactive
 * "Constitution at a Glance" Architecture & Citizen Rights SVG Diagram on /constitution/.
 */

(function () {
  'use strict';

  let articlesCache = [];

  const elements = {
    finderInput: document.getElementById('hub-finder-input'),
    chipsContainer: document.getElementById('hub-chips-container'),
    previewBox: document.getElementById('hub-finder-preview'),
    previewTitle: document.getElementById('hub-preview-title'),
    previewPart: document.getElementById('hub-preview-part'),
    previewText: document.getElementById('hub-preview-text'),
    previewLink: document.getElementById('hub-preview-link'),
    
    // Interactive Visual Diagram Elements
    svg: document.getElementById('constitution-interactive-svg'),
    diagCard: document.getElementById('diagram-detail-card'),
    diagBadge: document.getElementById('diag-badge'),
    diagTitle: document.getElementById('diag-title'),
    diagDesc: document.getElementById('diag-desc'),
    diagActionBtn: document.getElementById('diag-action-btn'),
    diagSubchips: document.getElementById('diag-subchips'),
    pillsRow: document.getElementById('diagram-pills-row')
  };

  const diagramData = {
    rights: {
      badge: "Inviolable Constitutional Compact",
      title: "Part II: Fundamental Rights Sanctuary (Articles 8–28)",
      desc: "Article 8 establishes that any law inconsistent with or in derogation of Fundamental Rights is void to that extent. The Constitution guarantees security of person (Art. 9), clean environment (Art. 9A), safeguards on arrest (Art. 10), fair trial and due process (Art. 10A), privacy and human dignity (Art. 14), civic freedoms (Arts 15–20), equality (Art. 25), free compulsory education (Art. 25A), and property protections (Arts 23–24).",
      link: "/constitution/reader/?part=Part+II",
      linkText: "Explore Fundamental Rights in Reader \u2192",
      chips: ["Art. 9: Life", "Art. 9A: Environment", "Art. 10A: Fair Trial", "Art. 14: Dignity", "Art. 19A: Information", "Art. 25A: Education"]
    },
    devolution: {
      badge: "PPRI Core Focus \u2022 Third Tier Governance",
      title: "Article 140A: Local Government & Devolution",
      desc: "Each province is constitutionally mandated by law to establish a local government system and devolve political, administrative, and financial responsibility and authority to elected local government representatives. Elections are constitutionally vested in the Election Commission of Pakistan (ECP).",
      link: "/constitution/reader/?article=140A",
      linkText: "Read Article 140A in Full Reader \u2192",
      chips: ["Political Devolution", "Administrative Cadres", "Financial PFC Devolution", "ECP Elections", "Article 140A(2)"]
    },
    parliament: {
      badge: "Democratic Federal Representation",
      title: "Part III: Majlis-e-Shoora (Bicameral Parliament)",
      desc: "The federal legislature consists of the President and two Houses: the National Assembly (336 seats, allocated to provinces based on population via Census 2023) and the Senate (equal provincial representation of 23 seats per province, safeguarding smaller federating units from population dominance).",
      link: "/constitution/reader/?part=Part+III",
      linkText: "Read Parliament Provisions (Arts 41–100) \u2192",
      chips: ["Art. 51: National Assembly", "Art. 59: Senate", "Art. 90: Prime Minister", "Art. 70: Bills Procedure"]
    },
    judicature: {
      badge: "Apex Rule of Law & 26th Amendment",
      title: "Part VII: The Judicature & Constitutional Benches",
      desc: "Vests judicial power in the Supreme Court of Pakistan, High Courts in each Province, and the Federal Shariat Court. Under the 26th Constitutional Amendment (2024), specialized Constitutional Benches (Art. 191A & 202A) hear constitutional interpretation petitions and suo motu / original jurisdiction matters.",
      link: "/constitution/reader/?part=Part+VII",
      linkText: "Read Judicature Articles (Arts 175–212) \u2192",
      chips: ["Art. 175: Judicial Structure", "Art. 175A: Judicial Appointments", "Art. 191A: Constitutional Benches", "Art. 199: High Court Writs"]
    },
    safeguards: {
      badge: "Federalism & Provincial Guardrails",
      title: "Fiscal Ratchet (Art. 160) & Boundary Consent (Art. 239)",
      desc: "Two insurmountable constitutional protections for provinces: Article 160(3A) mandates that provincial divisible pool shares in any National Finance Commission (NFC) Award cannot be less than the previous Award (the fiscal ratchet). Article 239(4) prohibits altering the limits of any Province without a 2/3 total membership supermajority vote in that Province's own Assembly.",
      link: "/constitution/reader/?article=239",
      linkText: "Inspect Article 239 Supermajority in Reader \u2192",
      chips: ["Art. 160(3A): Non-Regressive NFC", "Art. 172: Natural Resources", "Art. 239(4): Provincial Boundary Lock"]
    }
  };

  // Load articles database
  fetch('/data/constitution/articles.json')
    .then(r => r.json())
    .then(data => {
      articlesCache = data;
      setupFinder();
      setupDiagram();
    })
    .catch(err => {
      console.warn('Hub articles fetch error:', err);
      setupDiagram(); // Diagram runs even if fetch is pending
    });

  function setupFinder() {
    if (!elements.finderInput || !elements.previewBox) return;

    // Handle input search
    elements.finderInput.addEventListener('input', (e) => {
      const val = e.target.value.trim().toLowerCase();
      if (!val) {
        showPreview('140A'); // Default showcase
        resetChipActive();
        return;
      }

      // Find match
      const matched = articlesCache.find(a => 
        a.article_number.toLowerCase() === val ||
        a.article_number.toLowerCase() === `article ${val}` ||
        a.title.toLowerCase().includes(val) ||
        (a.tags && a.tags.some(t => t.toLowerCase().includes(val)))
      );

      if (matched) {
        renderArticlePreview(matched);
      } else {
        // Show partial search guidance
        elements.previewTitle.textContent = `Searching for "${e.target.value}"...`;
        elements.previewPart.textContent = 'Explore Reader';
        elements.previewText.textContent = 'No exact article number match found. Press Enter or click below to search across the full 280-Article text database.';
        elements.previewLink.href = `/constitution/reader/?article=${encodeURIComponent(e.target.value)}`;
        elements.previewLink.innerHTML = `Search in 280-Article Reader &rarr;`;
      }
    });

    // Handle quick topic chips
    if (elements.chipsContainer) {
      const chips = elements.chipsContainer.querySelectorAll('.const-chip');
      chips.forEach(chip => {
        chip.addEventListener('click', () => {
          chips.forEach(c => c.classList.remove('is-active'));
          chip.classList.add('is-active');
          const artNum = chip.dataset.article;
          if (elements.finderInput) {
            elements.finderInput.value = artNum;
          }
          showPreview(artNum);
        });
      });
    }

    // Initial showcase
    showPreview('140A');
  }

  function resetChipActive() {
    if (!elements.chipsContainer) return;
    const chips = elements.chipsContainer.querySelectorAll('.const-chip');
    chips.forEach(c => c.classList.remove('is-active'));
    const defaultChip = elements.chipsContainer.querySelector('[data-article="140A"]');
    if (defaultChip) defaultChip.classList.add('is-active');
  }

  function showPreview(artNumber) {
    if (!articlesCache || articlesCache.length === 0) return;
    const matched = articlesCache.find(a => a.article_number.toLowerCase() === artNumber.toLowerCase());
    if (matched) {
      renderArticlePreview(matched);
    }
  }

  function renderArticlePreview(art) {
    if (!elements.previewTitle || !elements.previewText || !elements.previewLink) return;

    const prefix = art.article_number.toLowerCase().includes('schedule') || art.article_number.toLowerCase().includes('preamble')
      ? ''
      : `Article ${art.article_number}: `;

    elements.previewTitle.textContent = `${prefix}${art.title}`;
    
    const partInfo = art.chapter 
      ? `${art.part} • ${art.chapter}: ${art.chapter_title || ''}`
      : `${art.part} • ${art.part_title || ''}`;
    elements.previewPart.textContent = partInfo;

    elements.previewText.textContent = art.salient_points || 'Salient legal summary available in the full reader.';
    elements.previewLink.href = `/constitution/reader/?article=${encodeURIComponent(art.article_number)}`;
    elements.previewLink.innerHTML = `Read Article ${escapeHTML(art.article_number)} in Full Reader &rarr;`;
  }

  /* -------------------------------------------------------------
   * Interactive "Constitution at a Glance" Visual Diagram Controller
   * ----------------------------------------------------------- */
  function setupDiagram() {
    if (!elements.svg || !elements.diagCard) return;

    const nodes = elements.svg.querySelectorAll('.diag-node');
    const pills = elements.pillsRow ? elements.pillsRow.querySelectorAll('.const-diag-pill') : [];

    function activateSector(nodeKey) {
      const data = diagramData[nodeKey];
      if (!data) return;

      // Update SVG node highlights
      nodes.forEach(n => {
        n.classList.toggle('is-active', n.dataset.node === nodeKey);
      });

      // Update pill button active states
      pills.forEach(p => {
        p.classList.toggle('is-active', p.dataset.node === nodeKey);
      });

      // Update detail card
      if (elements.diagBadge) elements.diagBadge.textContent = data.badge;
      if (elements.diagTitle) elements.diagTitle.textContent = data.title;
      if (elements.diagDesc) elements.diagDesc.textContent = data.desc;
      if (elements.diagActionBtn) {
        elements.diagActionBtn.href = data.link;
        elements.diagActionBtn.textContent = data.linkText;
      }

      // Update subchips
      if (elements.diagSubchips) {
        elements.diagSubchips.innerHTML = '';
        data.chips.forEach(chipText => {
          const span = document.createElement('span');
          span.className = 'const-badge const-badge-verified';
          span.textContent = chipText;
          elements.diagSubchips.appendChild(span);
        });
      }
    }

    // SVG Node Click / Keypress
    nodes.forEach(node => {
      node.addEventListener('click', () => {
        const key = node.dataset.node;
        if (key) activateSector(key);
      });

      node.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          const key = node.dataset.node;
          if (key) activateSector(key);
        }
      });
    });

    // Pill Row Click
    pills.forEach(pill => {
      pill.addEventListener('click', () => {
        const key = pill.dataset.node;
        if (key) activateSector(key);
      });
    });

    // Initialize with Fundamental Rights
    activateSector('rights');
  }

  function escapeHTML(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }
})();
