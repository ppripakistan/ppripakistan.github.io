const PPRI_NAV = [
  {
    label: "Constitution",
    href: "/constitution/",
    prefixes: ["/constitution/", "/resources/constitution.html"],
    items: [
      ["Constitution overview", "/constitution/"],
      ["Article reader", "/constitution/reader/"],
      ["Amendments", "/constitution/amendments/"],
    ],
  },
  {
    label: "Research",
    href: "/research/",
    prefixes: ["/research/", "/publications/", "/articles/", "/archive/"],
    items: [
      ["Research programme", "/research/"],
      ["Publications", "/publications/"],
      ["Reports", "/research/reports/"],
      ["Articles", "/articles/"],
      ["Research agenda", "/research/agenda.html"],
    ],
  },
  {
    label: "Reform & scenarios",
    href: "/provinces/",
    prefixes: ["/provinces/", "/scenarios/", "/maps/", "/resources/"],
    items: [
      ["Provincial reform", "/provinces/"],
      ["Reform models", "/provinces/proposed-models.html"],
      ["Constitutional basis", "/resources/constitution.html"],
      ["Governance scenarios", "/scenarios/"],
      ["Interactive map lab", "/maps/scenarios/"],
    ],
  },
  {
    label: "Data & tools",
    href: "/data/centre.html",
    prefixes: ["/data/", "/insights/", "/knowledge-library/", "/sources/", "/reform/"],
    items: [
      ["Data Centre", "/data/centre.html"],
      ["Compare provinces", "/data/compare/"],
      ["Download datasets", "/data/downloads/"],
      ["Charts & infographics", "/insights/"],
      ["Knowledge Library", "/knowledge-library/"],
      ["Fast facts", "/data/css-fast-facts-pakistan/"],
    ],
  },
  {
    label: "Participate",
    href: "/surveys/",
    prefixes: ["/surveys/", "/consultation/"],
    items: [
      ["Community surveys", "/surveys/"],
      ["Public consultation", "/consultation/"],
      ["Submit a policy proposal", "/consultation/submissions.html"],
    ],
  },
  {
    label: "About",
    href: "/about.html",
    prefixes: ["/about.html", "/mission.html", "/researchers/", "/methodology/", "/transparency.html", "/contact.html", "/media/", "/directory.html"],
    items: [
      ["About PPRI", "/about.html"],
      ["Researchers", "/researchers/"],
      ["Methods & standards", "/methodology/"],
      ["Transparency", "/transparency.html"],
      ["Contact", "/contact.html"],
    ],
  },
];

const PPRI_NAV_UR = [
  {
    label: "دستورِ پاکستان",
    href: "/constitution/",
    prefixes: ["/constitution/", "/resources/constitution.html"],
    items: [
      ["دستور کا جائزہ (انگریزی)", "/constitution/"],
      ["آرٹیکل ریڈر (انگریزی)", "/constitution/reader/"],
      ["آئینی ترامیم (انگریزی)", "/constitution/amendments/"],
    ],
  },
  {
    label: "تحقیق",
    href: "/ur/research/",
    prefixes: ["/ur/research/", "/ur/articles/", "/publications/", "/research/", "/articles/"],
    items: [
      ["تحقیقاتی مرکز", "/ur/research/"],
      ["مطبوعات (انگریزی)", "/publications/"],
      ["تحقیقی رپورٹس", "/ur/research/reports/"],
      ["تحقیقی مضامین", "/ur/articles/"],
      ["تحقیقی ایجنڈا (انگریزی)", "/research/agenda.html"],
    ],
  },
  {
    label: "اصلاحات و منظرنامے",
    href: "/ur/provinces/",
    prefixes: ["/ur/provinces/", "/provinces/", "/scenarios/", "/maps/", "/resources/"],
    items: [
      ["صوبائی اصلاحات", "/ur/provinces/"],
      ["مجوزہ ماڈلز (انگریزی)", "/provinces/proposed-models.html"],
      ["اصلاحات کی آئینی بنیاد (انگریزی)", "/resources/constitution.html"],
      ["حکمرانی منظرنامے (انگریزی)", "/scenarios/"],
      ["انٹرایکٹو نقشہ لیب (انگریزی)", "/maps/scenarios/"],
    ],
  },
  {
    label: "اعداد و شمار",
    href: "/ur/data/centre.html",
    prefixes: ["/ur/data/", "/data/", "/insights/", "/knowledge-library/"],
    items: [
      ["مرکزی ڈیٹا آبزرویٹری", "/ur/data/centre.html"],
      ["صوبائی موازنہ (انگریزی)", "/data/compare/"],
      ["اوپن ڈیٹا ڈاؤنلوڈز (انگریزی)", "/data/downloads/"],
      ["چارٹس و انفوگرافکس (انگریزی)", "/insights/"],
      ["نالج لائبریری (انگریزی)", "/knowledge-library/"],
      ["تیز حقائق (انگریزی)", "/data/css-fast-facts-pakistan/"],
    ],
  },
  {
    label: "عوامی شرکت",
    href: "/ur/consultation/",
    prefixes: ["/ur/consultation/", "/surveys/", "/consultation/"],
    items: [
      ["قومی حکمرانی سروے", "/ur/consultation/survey.html"],
      ["عوامی مشاورت", "/ur/consultation/"],
      ["پالیسی تجاویز جمع کرائیں (انگریزی)", "/consultation/submissions.html"],
    ],
  },
  {
    label: "ادارہ",
    href: "/ur/about.html",
    prefixes: ["/ur/about.html", "/about.html", "/researchers/", "/methodology/", "/transparency.html", "/contact.html"],
    items: [
      ["ادارے کا تعارف", "/ur/about.html"],
      ["محققین اور فیکلٹی (انگریزی)", "/researchers/"],
      ["طریقہ کار و معیارات (انگریزی)", "/methodology/"],
      ["شفافیت اور اخلاقیات (انگریزی)", "/transparency.html"],
      ["رابطہ کریں (انگریزی)", "/contact.html"],
    ],
  },
];

function normalizePath(path) {
  const value = path.replace(/index\.html$/, "").replace(/\/$/, "");
  return value || "/";
}

function normalizeUrlParts(href) {
  const url = new URL(href, window.location.origin);
  return {
    pathname: normalizePath(url.pathname),
    search: url.search || "",
    hash: url.hash || "",
  };
}

function linkIsCurrent(href) {
  const target = normalizeUrlParts(href);
  const current = normalizeUrlParts(window.location.href);
  return (
    target.pathname === current.pathname &&
    target.search === current.search &&
    target.hash === current.hash
  );
}

function groupMatchesCurrentSection(group) {
  const curPath = normalizePath(window.location.pathname);
  const prefixes = group.prefixes || [group.href];
  return prefixes.some((pref) => {
    const normPref = normalizePath(pref);
    if (normPref === "/" || normPref === "/ur") return curPath === normPref;
    return curPath === normPref || curPath.startsWith(normPref + "/");
  });
}

function getLanguageCounterpartUrl() {
  const currentPath = window.location.pathname;
  const isUrdu = document.documentElement.lang === "ur" || currentPath.startsWith("/ur/");

  if (isUrdu) {
    const exactEnglishMatches = {
      "/ur/consultation/survey.html": "/surveys/",
      "/ur/data/literacy-rate-pakistan": "/data/literacy-rate-pakistan/",
      "/ur/data/literacy-rate-pakistan/": "/data/literacy-rate-pakistan/",
      "/ur/data/literacy-rate-pakistan/index.html": "/data/literacy-rate-pakistan/",
      "/ur/articles": "/articles/",
      "/ur/articles/": "/articles/",
      "/ur/articles/index.html": "/articles/",
    };
    const norm = currentPath.replace(/\/$/, "") || "/ur";
    if (exactEnglishMatches[currentPath] || exactEnglishMatches[norm]) {
      return {
        targetUrl: exactEnglishMatches[currentPath] || exactEnglishMatches[norm],
        targetLabel: "English",
        targetLang: "en",
      };
    }
    let enPath = currentPath.replace(/^\/ur(\/|$)/, "/") || "/";
    if (enPath !== "/" && !enPath.endsWith(".html") && !enPath.endsWith("/")) {
      enPath += "/";
    }
    return { targetUrl: enPath, targetLabel: "English", targetLang: "en" };
  } else {
    const exactUrduMatches = {
      "/": "/ur/index.html",
      "/index.html": "/ur/index.html",
      "/about.html": "/ur/about.html",
      "/articles": "/ur/articles/index.html",
      "/articles/": "/ur/articles/index.html",
      "/articles/index.html": "/ur/articles/index.html",
      "/articles/provinces-of-pakistan-names-capitals-population.html": "/ur/articles/provinces-of-pakistan-names-capitals-population.html",
      "/articles/new-administrative-units-pakistan-2026.html": "/ur/articles/new-administrative-units-pakistan-2026.html",
      "/articles/karachi-urban-sindh-representation-revenue-administration.html": "/ur/articles/karachi-urban-sindh-representation-revenue-administration.html",
      "/articles/bahawalpur-province-restoration-2026.html": "/ur/articles/bahawalpur-province-restoration-2026.html",
      "/articles/is-gilgit-baltistan-a-province-of-pakistan.html": "/ur/articles/is-gilgit-baltistan-a-province-of-pakistan.html",
      "/consultation/": "/ur/consultation/index.html",
      "/consultation/index.html": "/ur/consultation/index.html",
      "/surveys": "/ur/consultation/survey.html",
      "/surveys/": "/ur/consultation/survey.html",
      "/surveys/index.html": "/ur/consultation/survey.html",
      "/provinces/": "/ur/provinces/index.html",
      "/provinces/index.html": "/ur/provinces/index.html",
      "/data/centre.html": "/ur/data/centre.html",
      "/data/literacy-rate-pakistan": "/ur/data/literacy-rate-pakistan/index.html",
      "/data/literacy-rate-pakistan/": "/ur/data/literacy-rate-pakistan/index.html",
      "/data/literacy-rate-pakistan/index.html": "/ur/data/literacy-rate-pakistan/index.html",
      "/research/": "/ur/research/index.html",
      "/research/index.html": "/ur/research/index.html",
      "/research/reports/": "/ur/research/reports/index.html",
      "/research/reports/index.html": "/ur/research/reports/index.html",
      "/research/reports/income-went-up-why-does-life-feel-harder.html": "/ur/research/reports/income-went-up-why-does-life-feel-harder.html",
      "/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html": "/ur/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html",
      "/research/reports/same-country-different-life-district-access.html": "/ur/research/reports/same-country-different-life-district-access.html",
      "/research/reports/bribe-you-cant-see-corruption-private-tax.html": "/ur/research/reports/bribe-you-cant-see-corruption-private-tax.html",
      "/research/reports/does-money-work-better-spent-closer-to-people.html": "/ur/research/reports/does-money-work-better-spent-closer-to-people.html",
    };
    const norm = currentPath.replace(/\/$/, "") || "/";
    const targetUrl = exactUrduMatches[currentPath] || exactUrduMatches[norm];
    if (!targetUrl) return null;
    return { targetUrl, targetLabel: "اردو", targetLang: "ur" };
  }
}

const isDesktopNav = () => window.matchMedia("(min-width: 1101px)").matches;

function syncCurrentNavState(nav) {
  if (!nav) return;
  let assignedCurrent = false;
  nav.querySelectorAll("a[href]").forEach((link) => {
    const isMatch = !assignedCurrent && linkIsCurrent(link.getAttribute("href"));
    if (isMatch) {
      link.setAttribute("aria-current", "page");
      link.classList.add("is-current");
      assignedCurrent = true;
    } else {
      link.removeAttribute("aria-current");
      link.classList.remove("is-current");
    }
  });
  const isUrdu = document.documentElement.lang === "ur" || window.location.pathname.startsWith("/ur/");
  const activeNavData = isUrdu ? PPRI_NAV_UR : PPRI_NAV;
  nav.querySelectorAll(".nav-group").forEach((wrapper, idx) => {
    const group = activeNavData[idx];
    const hasExactChild = Boolean(wrapper.querySelector(".nav-menu a[aria-current='page']"));
    const matchesSection = hasExactChild || (group ? groupMatchesCurrentSection(group) : false);
    wrapper.classList.toggle("is-parent-current", matchesSection);
    wrapper.classList.remove("is-current");
  });
}

function buildEnhancedNavigation(nav) {
  if (!nav || nav.dataset.enhanced === "true") return;

  const isUrdu = document.documentElement.lang === "ur" || window.location.pathname.startsWith("/ur/");
  const activeNavData = isUrdu ? PPRI_NAV_UR : PPRI_NAV;

  const currentLinks = [...nav.querySelectorAll("a")];
  const home = currentLinks.find((link) => {
    const p = normalizePath(new URL(link.href, window.location.origin).pathname);
    return p === "/" || p === "/ur";
  });
  const search = currentLinks.find((link) => link.classList.contains("nav-search"));

  let navCloseTimer = null;
  const closeGroup = (groupEl) => {
    if (!groupEl) return;
    groupEl.classList.remove("is-open");
    groupEl.dataset.openSource = "";
    groupEl.querySelector(".nav-trigger")?.setAttribute("aria-expanded", "false");
  };
  const closeAllNavGroups = (sourceFilter) => {
    if (navCloseTimer) {
      clearTimeout(navCloseTimer);
      navCloseTimer = null;
    }
    nav.querySelectorAll(".nav-group.is-open").forEach((other) => {
      if (!sourceFilter || other.dataset.openSource === sourceFilter) {
        closeGroup(other);
      }
    });
  };

  const fragment = document.createDocumentFragment();
  if (home) {
    if (isUrdu) {
      home.textContent = "مرکزی صفحہ";
      home.href = "/ur/index.html";
    } else {
      home.textContent = "Home";
      home.href = "/";
    }
    home.addEventListener("click", () => {
      closeAllNavGroups();
      nav.classList.remove("is-open");
      const mb = document.querySelector(".menu-toggle");
      if (mb) mb.setAttribute("aria-expanded", "false");
    });
    home.addEventListener("mouseenter", () => {
      if (isDesktopNav()) closeAllNavGroups();
    });
    fragment.appendChild(home);
  }

  activeNavData.forEach((group, groupIndex) => {
    const wrapper = document.createElement("div");
    wrapper.className = "nav-group";
    wrapper.dataset.openSource = "";

    const trigger = document.createElement("button");
    trigger.type = "button";
    trigger.className = "nav-trigger";
    trigger.setAttribute("aria-expanded", "false");
    trigger.setAttribute("aria-controls", `nav-menu-${groupIndex}`);
    trigger.textContent = group.label;

    const menu = document.createElement("div");
    menu.id = `nav-menu-${groupIndex}`;
    menu.className = "nav-menu";

    group.items.forEach(([label, href]) => {
      const item = document.createElement("a");
      item.href = href;
      item.textContent = label;
      if (isUrdu && label.includes("(انگریزی)")) {
        item.dataset.langHandoff = "en";
      }
      menu.appendChild(item);
    });

    wrapper.addEventListener("mouseenter", () => {
      if (isDesktopNav()) {
        if (navCloseTimer) {
          clearTimeout(navCloseTimer);
          navCloseTimer = null;
        }
        nav.querySelectorAll(".nav-group.is-open").forEach((other) => {
          if (other !== wrapper) closeGroup(other);
        });
        if (!wrapper.classList.contains("is-open")) {
          wrapper.dataset.openSource = "hover";
          wrapper.classList.add("is-open");
          trigger.setAttribute("aria-expanded", "true");
        }
      }
    });

    wrapper.addEventListener("mouseleave", () => {
      if (isDesktopNav() && wrapper.dataset.openSource !== "click") {
        if (navCloseTimer) clearTimeout(navCloseTimer);
        navCloseTimer = setTimeout(() => {
          if (wrapper.dataset.openSource !== "click") closeGroup(wrapper);
          navCloseTimer = null;
        }, 180);
      }
    });

    trigger.addEventListener("click", (event) => {
      event.stopPropagation();
      if (navCloseTimer) {
        clearTimeout(navCloseTimer);
        navCloseTimer = null;
      }
      const isOpen = wrapper.classList.contains("is-open");
      const src = wrapper.dataset.openSource;
      if (isOpen && src === "hover" && isDesktopNav()) {
        wrapper.dataset.openSource = "click";
        trigger.setAttribute("aria-expanded", "true");
        return;
      }
      const willOpen = !isOpen;
      nav.querySelectorAll(".nav-group.is-open").forEach((other) => {
        if (other !== wrapper) closeGroup(other);
      });
      if (willOpen) {
        wrapper.dataset.openSource = "click";
        wrapper.classList.add("is-open");
        trigger.setAttribute("aria-expanded", "true");
      } else {
        closeGroup(wrapper);
      }
    });

    menu.querySelectorAll("a").forEach((item) => {
      item.addEventListener("click", () => {
        closeAllNavGroups();
        nav.classList.remove("is-open");
        const mb = document.querySelector(".menu-toggle");
        if (mb) mb.setAttribute("aria-expanded", "false");
      });
    });

    wrapper.append(trigger, menu);
    fragment.appendChild(wrapper);
  });

  if (search) {
    if (isUrdu) {
      search.innerHTML = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg> تلاش';
    } else if (!search.querySelector("svg")) {
      const searchSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      searchSvg.setAttribute("width", "13");
      searchSvg.setAttribute("height", "13");
      searchSvg.setAttribute("viewBox", "0 0 24 24");
      searchSvg.setAttribute("fill", "none");
      searchSvg.setAttribute("stroke", "currentColor");
      searchSvg.setAttribute("stroke-width", "2.5");
      searchSvg.setAttribute("stroke-linecap", "round");
      searchSvg.setAttribute("stroke-linejoin", "round");
      searchSvg.setAttribute("aria-hidden", "true");
      searchSvg.innerHTML = '<circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>';
      search.prepend(searchSvg);
    }
    search.addEventListener("click", () => {
      closeAllNavGroups();
      nav.classList.remove("is-open");
      const mb = document.querySelector(".menu-toggle");
      if (mb) mb.setAttribute("aria-expanded", "false");
    });
    search.addEventListener("mouseenter", () => {
      if (isDesktopNav()) closeAllNavGroups();
    });
    fragment.appendChild(search);
  }

  // Language Switcher Button (only shown when a direct translation exists)
  const counterpart = getLanguageCounterpartUrl();
  if (counterpart && counterpart.targetUrl) {
    const langSwitch = document.createElement("a");
    langSwitch.href = counterpart.targetUrl;
    langSwitch.className = "lang-switch-btn";
    langSwitch.setAttribute("hreflang", counterpart.targetLang);
    langSwitch.setAttribute("lang", counterpart.targetLang);
    langSwitch.textContent = counterpart.targetLabel;
    fragment.appendChild(langSwitch);
  }

  nav.addEventListener("mouseleave", () => {
    if (isDesktopNav()) {
      if (navCloseTimer) clearTimeout(navCloseTimer);
      navCloseTimer = setTimeout(() => closeAllNavGroups("hover"), 180);
    }
  });

  nav.replaceChildren(fragment);
  nav.dataset.enhanced = "true";
  syncCurrentNavState(nav);

  window.addEventListener("hashchange", () => syncCurrentNavState(nav));
  window.addEventListener("popstate", () => syncCurrentNavState(nav));

  const mqDesktop = window.matchMedia("(min-width: 1101px)");
  if (mqDesktop.addEventListener) {
    mqDesktop.addEventListener("change", () => {
      closeAllNavGroups();
      nav.classList.remove("is-open");
      const mb = document.querySelector(".menu-toggle");
      if (mb) mb.setAttribute("aria-expanded", "false");
    });
  }

  document.addEventListener("click", (event) => {
    if (!nav.contains(event.target)) {
      closeAllNavGroups();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      const openGroup = nav.querySelector(".nav-group.is-open");
      const activeInsideMenu = openGroup && openGroup.contains(document.activeElement);
      closeAllNavGroups();
      if (activeInsideMenu) {
        openGroup.querySelector(".nav-trigger")?.focus();
      }
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const menuButton = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav-links");
  const isUrdu = document.documentElement.lang === "ur" || window.location.pathname.startsWith("/ur/");

  if (menuButton && nav) {
    const menuLabel = isUrdu ? "مینو" : "Menu";
    if (!menuButton.querySelector("svg")) {
      menuButton.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg> <span>${menuLabel}</span>`;
    }
    menuButton.addEventListener("click", () => {
      const isOpen = nav.classList.toggle("is-open");
      menuButton.setAttribute("aria-expanded", String(isOpen));
    });
    buildEnhancedNavigation(nav);

    // Close mobile drawer on outside click or escape
    document.addEventListener("click", (event) => {
      if (nav.classList.contains("is-open") && !nav.contains(event.target) && !menuButton.contains(event.target)) {
        nav.classList.remove("is-open");
        menuButton.setAttribute("aria-expanded", "false");
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && nav.classList.contains("is-open")) {
        const wasInsideNav = nav.contains(document.activeElement);
        nav.classList.remove("is-open");
        menuButton.setAttribute("aria-expanded", "false");
        if (wasInsideNav) menuButton.focus();
      }
    });
  }

  // Defensive table containment: avoid double-wrapping and make every scroll region keyboard-accessible
  const existingTableContainerSelector = ".table-wrap, .table-container, .table-responsive, .data-table-wrap, .comparison-table-wrap, .ppri-table-wrap, .district-table-container, .obs-table-container, .el-table-wrap";
  const deriveTableLabel = (table, wrap) => {
    const caption = table.querySelector("caption");
    if (caption && caption.textContent.trim()) return caption.textContent.trim();
    let prev = wrap.previousElementSibling;
    while (prev && !/^H[1-6]$/.test(prev.tagName)) {
      const innerH = prev.querySelector("h2, h3, h4");
      if (innerH && innerH.textContent.trim()) return innerH.textContent.trim();
      prev = prev.previousElementSibling;
    }
    if (prev && prev.textContent.trim()) return prev.textContent.trim();
    const firstHeader = table.querySelector("thead th");
    return firstHeader ? `Data table (${firstHeader.textContent.trim()})` : "Scrollable data table";
  };

  document.querySelectorAll("table").forEach((table) => {
    let wrap = table.closest(existingTableContainerSelector);
    if (!wrap) {
      wrap = document.createElement("div");
      wrap.className = "table-wrap";
      table.parentNode.insertBefore(wrap, table);
      wrap.appendChild(table);
    }
    if (!wrap.hasAttribute("tabindex")) wrap.setAttribute("tabindex", "0");
    if (!wrap.hasAttribute("role")) wrap.setAttribute("role", "region");
    if (!wrap.hasAttribute("aria-label") && !wrap.hasAttribute("aria-labelledby")) {
      wrap.setAttribute("aria-label", deriveTableLabel(table, wrap));
    }
  });

  // Ensure horizontal scroll flow strips on homepage are keyboard-focusable and named
  document.querySelectorAll(".research-flow, .scenario-path").forEach((flow) => {
    if (!flow.hasAttribute("tabindex")) flow.setAttribute("tabindex", "0");
    if (!flow.hasAttribute("role")) flow.setAttribute("role", "region");
  });

  document.querySelectorAll("[data-current-year]").forEach((element) => {
    element.textContent = new Date().getFullYear();
  });

  const input = document.querySelector("[data-publication-search]");
  const cards = [...document.querySelectorAll("[data-publication-card]")];
  if (input && cards.length) {
    input.addEventListener("input", () => {
      const query = input.value.toLowerCase().trim();
      cards.forEach((card) => {
        card.hidden = !!query && !card.textContent.toLowerCase().includes(query);
      });
    });
  }
});


// Global One-Click Article Citation Copy Function
window.copyArticleCitation = function (artCode, artTitle, pubYear) {
  var url = window.location.href.split('#')[0];
  var year = pubYear || '2026';
  var citationText = 'Pakistan Provincial Reform Institute (PPRI). (' + year + '). ' + artTitle + ' (PPRI Policy Article No. ' + artCode + '). ' + url;
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(citationText).then(function () {
      showCitationToast('Citation copied to clipboard!');
    }).catch(function () {
      fallbackCopyText(citationText);
    });
  } else {
    fallbackCopyText(citationText);
  }
};

// Global One-Click Report Citation Copy Function
window.copyReportCitation = function (repCode, repTitle, pubYear) {
  var url = window.location.href.split('#')[0];
  var year = pubYear || '2026';
  var citationText = 'Pakistan Provincial Reform Institute (PPRI). (' + year + '). ' + repTitle + ' (PPRI Research Report No. ' + repCode + '). ' + url;
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(citationText).then(function () {
      showCitationToast('Report citation copied to clipboard!');
    }).catch(function () {
      fallbackCopyText(citationText);
    });
  } else {
    fallbackCopyText(citationText);
  }
};

function fallbackCopyText(text) {
  var textarea = document.createElement('textarea');
  textarea.value = text;
  textarea.style.position = 'fixed';
  textarea.style.opacity = '0';
  document.body.appendChild(textarea);
  textarea.select();
  try {
    document.execCommand('copy');
    showCitationToast('Citation copied to clipboard!');
  } catch (err) {
    prompt('Copy citation manually:', text);
  }
  document.body.removeChild(textarea);
}

function showCitationToast(msg) {
  var toast = document.getElementById('citation-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'citation-toast';
    toast.style.position = 'fixed';
    toast.style.bottom = '24px';
    toast.style.right = '24px';
    toast.style.background = '#073c3a';
    toast.style.color = '#ffffff';
    toast.style.padding = '10px 18px';
    toast.style.borderRadius = '6px';
    toast.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
    toast.style.fontSize = '0.85rem';
    toast.style.fontWeight = '600';
    toast.style.zIndex = '99999';
    toast.style.transition = 'opacity 0.25s ease, transform 0.25s ease';
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.style.opacity = '1';
  toast.style.transform = 'translateY(0)';
  setTimeout(function () {
    toast.style.opacity = '0';
    toast.style.transform = 'translateY(10px)';
  }, 2500);
}
