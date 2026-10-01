const PPRI_NAV = [
  {
    label: "Research",
    href: "/research/index.html",
    items: [
      ["Research programme", "/research/index.html"],
      ["Research agenda", "/research/agenda.html"],
      ["Articles & Analysis", "/articles/index.html"],
      ["Faculty & Working Groups", "/researchers/index.html"],
      ["Policy Papers", "/research/policy-papers/index.html"],
      ["Policy Briefs", "/research/briefs/index.html"],
      ["Working Papers", "/research/working-papers/index.html"],
      ["Reports", "/research/reports/index.html"],
      ["Research FAQ", "/research/faq.html"],
    ],
  },
  {
    label: "Reform",
    href: "/provinces/index.html",
    items: [
      ["Provincial reform", "/provinces/index.html"],
      ["Why provinces?", "/provinces/why-provinces.html"],
      ["Proposed models", "/provinces/proposed-models.html"],
      ["Administrative model", "/provinces/administrative-model.html"],
      ["Local government", "/provinces/local-government.html"],
      ["Fiscal framework", "/provinces/fiscal-framework.html"],
      ["Constitutional framework", "/provinces/constitutional-framework.html"],
      ["Transition framework", "/provinces/transition-framework.html"],
      ["Constitution Reader", "/resources/constitution.html"],
      ["Local Govt Legislation", "/resources/legislation.html"],
    ],
  },
  {
    label: "Explore",
    href: "/maps/index.html",
    items: [
      ["Scenario Lab", "/maps/scenarios/index.html"],
      ["Current administrative map", "/maps/current/administrative.html"],
      ["Data Observatory", "/data/centre.html"],
      ["Provincial comparison", "/data/provincial-comparison.html"],
      ["District explorer", "/data/district-explorer.html"],
      ["Open Datasets", "/data/datasets.html"],
      ["Sources", "/sources/index.html"],
      ["Methodology", "/methodology/index.html"],
    ],
  },
  {
    label: "Engage",
    href: "/consultation/index.html",
    items: [
      ["Public consultation", "/consultation/index.html"],
      ["Survey", "/consultation/survey.html"],
      ["Submit an idea", "/consultation/submissions.html"],
      ["Frequently asked questions", "/consultation/frequently-asked-questions.html"],
    ],
  },
  {
    label: "About",
    href: "/about.html",
    items: [
      ["About PPRI", "/about.html"],
      ["Mission & Charter", "/mission.html"],
      ["Research Faculty", "/researchers/index.html"],
      ["Press Room", "/media/press.html"],
      ["Transparency & Ethics", "/transparency.html"],
      ["Contact & Inquiries", "/contact.html"],
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

  const fragment = document.createDocumentFragment();
  if (home) {
    home.removeAttribute("aria-current");
    home.classList.toggle("is-current", linkIsCurrent(home.href));
    if (linkIsCurrent(home.href)) home.setAttribute("aria-current", "page");
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

    let closeTimer = null;
    wrapper.addEventListener("mouseenter", () => {
      if (window.innerWidth > 900) {
        if (closeTimer) { clearTimeout(closeTimer); closeTimer = null; }
        document.querySelectorAll(".nav-group.is-open").forEach((other) => {
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
        closeTimer = setTimeout(() => {
          wrapper.classList.remove("is-open");
          trigger.setAttribute("aria-expanded", "false");
        }, 220);
      }
    });

    trigger.addEventListener("click", () => {
      if (closeTimer) { clearTimeout(closeTimer); closeTimer = null; }
      const willOpen = !wrapper.classList.contains("is-open");
      document.querySelectorAll(".nav-group.is-open").forEach((other) => {
        other.classList.remove("is-open");
        other.querySelector(".nav-trigger")?.setAttribute("aria-expanded", "false");
      });
      wrapper.classList.toggle("is-open", willOpen);
      trigger.setAttribute("aria-expanded", String(willOpen));
    });

    menu.querySelectorAll("a").forEach((item) => {
      item.addEventListener("click", () => {
        if (closeTimer) { clearTimeout(closeTimer); closeTimer = null; }
        wrapper.classList.remove("is-open");
        trigger.setAttribute("aria-expanded", "false");
        nav.classList.remove("is-open");
      });
    });

    wrapper.append(trigger, menu);
    fragment.appendChild(wrapper);
  });

  if (search) {
    fragment.appendChild(search);
  }

  nav.replaceChildren(fragment);
  nav.dataset.enhanced = "true";

  document.addEventListener("click", (event) => {
    if (!nav.contains(event.target)) {
      nav.querySelectorAll(".nav-group.is-open").forEach((group) => {
        group.classList.remove("is-open");
        group.querySelector(".nav-trigger")?.setAttribute("aria-expanded", "false");
      });
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      nav.querySelectorAll(".nav-group.is-open").forEach((group) => {
        group.classList.remove("is-open");
        group.querySelector(".nav-trigger")?.setAttribute("aria-expanded", "false");
      });
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
  }

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
