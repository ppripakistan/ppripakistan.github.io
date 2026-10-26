const PPRI_NAV = [
  {
    label: "Research",
    href: "/research/",
    items: [
      ["Research Programme", "/research/"],
      ["Policy Papers", "/publications/#policy-papers"],
      ["Research Reports", "/research/reports/"],
      ["Policy Briefs", "/publications/#briefs"],
      ["Working Papers", "/publications/#working-papers"],
      ["Articles & Analysis", "/articles/"],
      ["Faculty & Working Groups", "/researchers/"],
      ["Research Agenda", "/research/agenda.html"],
      ["Research FAQ", "/research/faq.html"],
    ],
  },
  {
    label: "Reform",
    href: "/provinces/",
    items: [
      ["Provincial Reform Overview", "/provinces/"],
      ["Proposed 13-Unit Model", "/provinces/proposed-models.html"],
      ["Article 140A Municipal Devolution", "/scenarios/#local-government"],
      ["Fiscal Framework & NFC", "/provinces/#fiscal-framework"],
      ["Constitutional Path (Art. 239)", "/provinces/constitutional-framework.html"],
      ["Administrative Model", "/provinces/#administrative-model"],
      ["Transition Framework", "/provinces/transition-framework.html"],
      ["Why Subnational Reform?", "/provinces/why-provinces.html"],
      ["Constitution Reader", "/resources/constitution.html"],
      ["Local Govt Legislation", "/resources/legislation.html"],
    ],
  },
  {
    label: "Scenarios",
    href: "/scenarios/",
    items: [
      ["Governance Scenarios Suite", "/scenarios/"],
      ["1. Four-Province Baseline", "/scenarios/#current-structure"],
      ["2. Territorial Restructuring", "/scenarios/#new-provinces"],
      ["3. Municipal Devolution (140A)", "/scenarios/#local-government"],
      ["4. Comparative Decision Matrix", "/scenarios/#comparative-analysis"],
      ["5. Global Federal Benchmarks", "/scenarios/#international-models"],
      ["6. AI & Governance Delivery", "/scenarios/#technology-ai"],
      ["Interactive GIS Scenario Lab", "/maps/scenarios/"],
    ],
  },
  {
    label: "Data",
    href: "/data/centre.html",
    items: [
      ["Central Data Observatory", "/data/centre.html"],
      ["Population & Demographics", "/data/population/"],
      ["Economy & Inflation", "/data/economy/"],
      ["Public Finance & 7th NFC", "/data/public-finance/"],
      ["Living Standards & Income", "/data/living-standards/"],
      ["Education & Literacy", "/data/education/"],
      ["Public Health Infrastructure", "/data/health/"],
      ["Digital Access & Teledensity", "/data/digital-access/"],
      ["Provinces Comparator", "/data/compare/"],
      ["Open Data Downloads", "/data/downloads/"],
      ["CSS Fast Facts Matrix", "/data/quick-facts/"],
    ],
  },
  {
    label: "Publications",
    href: "/publications/",
    items: [
      ["All Policy Publications", "/publications/"],
      ["Policy Papers Series", "/publications/#policy-papers"],
      ["Analytical Reports", "/research/reports/"],
      ["Policy Briefs", "/publications/#briefs"],
      ["Working Papers", "/publications/#working-papers"],
      ["Historical Research Archive", "/archive/"],
    ],
  },
  {
    label: "Engage",
    href: "/consultation/",
    items: [
      ["Public Consultation Hub", "/consultation/"],
      ["National Governance Survey", "/consultation/survey.html"],
      ["Submit Policy Ideas", "/consultation/submissions.html"],
      ["Consultation FAQ", "/consultation/frequently-asked-questions.html"],
    ],
  },
  {
    label: "About",
    href: "/about.html",
    items: [
      ["About PPRI", "/about.html"],
      ["Mission & Charter", "/mission.html"],
      ["Research Faculty & Fellows", "/researchers/"],
      ["Press & Media Centre", "/media/press.html"],
      ["Transparency & Ethics", "/transparency.html"],
      ["Methodology & Standards", "/methodology/"],
      ["Contact & Institutional Desk", "/contact.html"],
    ],
  },
];

function normalizePath(path) {
  const value = path.replace(/index\.html$/, "").replace(/\/$/, "");
  return value || "/";
}

function linkIsCurrent(href) {
  return normalizePath(new URL(href, window.location.origin).pathname) === normalizePath(window.location.pathname);
}

function buildEnhancedNavigation(nav) {
  if (!nav || nav.dataset.enhanced === "true") return;

  const currentLinks = [...nav.querySelectorAll("a")];
  const home = currentLinks.find((link) => normalizePath(new URL(link.href).pathname) === "/");
  const search = currentLinks.find((link) => link.classList.contains("nav-search"));

  let navCloseTimer = null;
  const closeAllNavGroups = () => {
    if (navCloseTimer) {
      clearTimeout(navCloseTimer);
      navCloseTimer = null;
    }
    nav.querySelectorAll(".nav-group.is-open").forEach((other) => {
      other.classList.remove("is-open");
      other.querySelector(".nav-trigger")?.setAttribute("aria-expanded", "false");
    });
  };

  const fragment = document.createDocumentFragment();
  if (home) {
    home.removeAttribute("aria-current");
    home.classList.toggle("is-current", linkIsCurrent(home.href));
    if (linkIsCurrent(home.href)) home.setAttribute("aria-current", "page");
    home.addEventListener("click", () => {
      nav.classList.remove("is-open");
      const mb = document.querySelector(".menu-toggle");
      if (mb) mb.setAttribute("aria-expanded", "false");
    });
    home.addEventListener("mouseenter", () => {
      if (window.innerWidth > 900) closeAllNavGroups();
    });
    fragment.appendChild(home);
  }

  PPRI_NAV.forEach((group, groupIndex) => {
    const wrapper = document.createElement("div");
    wrapper.className = "nav-group";

    const trigger = document.createElement("button");
    trigger.type = "button";
    trigger.className = "nav-trigger";
    trigger.setAttribute("aria-expanded", "false");
    trigger.setAttribute("aria-haspopup", "true");
    trigger.setAttribute("aria-controls", `nav-menu-${groupIndex}`);
    trigger.textContent = group.label;

    const menu = document.createElement("div");
    menu.id = `nav-menu-${groupIndex}`;
    menu.className = "nav-menu";
    menu.setAttribute("role", "menu");

    let groupIsCurrent = false;
    group.items.forEach(([label, href]) => {
      const item = document.createElement("a");
      item.href = href;
      item.textContent = label;
      item.setAttribute("role", "menuitem");
      if (linkIsCurrent(href)) {
        item.setAttribute("aria-current", "page");
        item.classList.add("is-current");
        groupIsCurrent = true;
      }
      menu.appendChild(item);
    });

    if (groupIsCurrent) wrapper.classList.add("is-current");

    wrapper.addEventListener("mouseenter", () => {
      if (window.innerWidth > 900) {
        if (navCloseTimer) {
          clearTimeout(navCloseTimer);
          navCloseTimer = null;
        }
        nav.querySelectorAll(".nav-group.is-open").forEach((other) => {
          if (other !== wrapper) {
            other.classList.remove("is-open");
            other.querySelector(".nav-trigger")?.setAttribute("aria-expanded", "false");
          }
        });
        wrapper.classList.add("is-open");
        trigger.setAttribute("aria-expanded", "true");
      }
    });

    wrapper.addEventListener("mouseleave", () => {
      if (window.innerWidth > 900) {
        if (navCloseTimer) clearTimeout(navCloseTimer);
        navCloseTimer = setTimeout(() => {
          wrapper.classList.remove("is-open");
          trigger.setAttribute("aria-expanded", "false");
          navCloseTimer = null;
        }, 180);
      }
    });

    trigger.addEventListener("click", () => {
      if (navCloseTimer) {
        clearTimeout(navCloseTimer);
        navCloseTimer = null;
      }
      const willOpen = !wrapper.classList.contains("is-open");
      nav.querySelectorAll(".nav-group.is-open").forEach((other) => {
        other.classList.remove("is-open");
        other.querySelector(".nav-trigger")?.setAttribute("aria-expanded", "false");
      });
      wrapper.classList.toggle("is-open", willOpen);
      trigger.setAttribute("aria-expanded", String(willOpen));
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
    search.addEventListener("click", () => {
      nav.classList.remove("is-open");
      const mb = document.querySelector(".menu-toggle");
      if (mb) mb.setAttribute("aria-expanded", "false");
    });
    search.addEventListener("mouseenter", () => {
      if (window.innerWidth > 900) closeAllNavGroups();
    });
    fragment.appendChild(search);
  }

  nav.addEventListener("mouseleave", () => {
    if (window.innerWidth > 900) {
      if (navCloseTimer) clearTimeout(navCloseTimer);
      navCloseTimer = setTimeout(closeAllNavGroups, 180);
    }
  });

  nav.replaceChildren(fragment);
  nav.dataset.enhanced = "true";

  document.addEventListener("click", (event) => {
    if (!nav.contains(event.target)) {
      closeAllNavGroups();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeAllNavGroups();
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  const menuButton = document.querySelector(".menu-toggle");
  const nav = document.querySelector(".nav-links");

  if (menuButton && nav) {
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
        nav.classList.remove("is-open");
        menuButton.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Defensive table containment: ensure every data table is wrapped in a touch-scrollable container
  document.querySelectorAll("table").forEach((table) => {
    if (!table.closest(".table-wrap")) {
      const wrap = document.createElement("div");
      wrap.className = "table-wrap";
      table.parentNode.insertBefore(wrap, table);
      wrap.appendChild(table);
    }
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

