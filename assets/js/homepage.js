document.addEventListener("DOMContentLoaded", () => {
  const setRevealObserver = () => {
    const nodes = document.querySelectorAll("[data-reveal]");
    if (!nodes.length) return;

    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches || !("IntersectionObserver" in window)) {
      nodes.forEach((node) => node.classList.add("is-visible"));
      return;
    }

    const observer = new IntersectionObserver(
      (entries, instance) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          instance.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
    );

    nodes.forEach((node) => observer.observe(node));
  };


  const setupHeroMessages = () => {
    const shell = document.querySelector("[data-hero-message]");
    const lineOne = document.querySelector("[data-hero-line-one]");
    const lineTwo = document.querySelector("[data-hero-line-two]");
    if (!shell || !lineOne || !lineTwo) return;

    const messages = [
      ["Study the structure.", "Test the alternatives."],
      ["Rethink the map.", "Understand the consequences."],
      ["Explore new provinces.", "Examine what changes."],
      ["Evidence first.", "Scenarios second."],
      ["Bring government closer.", "Examine institutional design."],
    ];

    let index = 0;
    let timer = null;
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

    const show = (nextIndex) => {
      index = nextIndex % messages.length;
      const [first, second] = messages[index];
      shell.classList.remove("is-changing");
      void shell.offsetWidth;
      lineOne.textContent = first;
      lineTwo.textContent = second;
      if (!reduceMotion.matches) shell.classList.add("is-changing");
    };

    const start = () => {
      if (reduceMotion.matches || timer) return;
      timer = window.setInterval(() => show(index + 1), 6200);
    };
    const stop = () => {
      if (!timer) return;
      window.clearInterval(timer);
      timer = null;
    };

    shell.addEventListener("mouseenter", stop);
    shell.addEventListener("mouseleave", start);
    shell.addEventListener("focusin", stop);
    shell.addEventListener("focusout", start);
    show(0);
    start();
  };

  const setupPakistanCanvas = () => {
    const mapBg = document.querySelector("[data-pak-map]");
    if (!mapBg) return;

    const pakSvg = mapBg.querySelector(".pak-map-svg");
    if (!pakSvg) return;

    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

    // Calibrate the border-draw animation using actual path length
    const outline = pakSvg.querySelector(".pak-outline");
    if (outline) {
      try {
        const len = Math.ceil(outline.getTotalLength()) + 20;
        outline.style.strokeDasharray = len;
        outline.style.strokeDashoffset = len;
      } catch (_) { /* SVG not in DOM yet — CSS fallback value of 2600 applies */ }
    }

    if (reduceMotion.matches) {
      pakSvg.classList.add("is-animated");
      return;
    }

    // Start animation sequence when the research desk enters the viewport
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (!entry.isIntersecting) return;
        pakSvg.classList.add("is-animated");
        observer.unobserve(entry.target);
      },
      { threshold: 0.25 }
    );
    observer.observe(mapBg);

    // Province hover interactions
    const zones = [...mapBg.querySelectorAll(".prov-zone")];
    const fills = [...mapBg.querySelectorAll("[data-prov-fill]")];
    const badges = [...mapBg.querySelectorAll("[data-badge]")];

    zones.forEach((zone) => {
      zone.addEventListener("mouseenter", () => {
        const prov = zone.dataset.prov;
        fills.forEach((f) => {
          f.classList.toggle("pf-highlight", f.dataset.provFill === prov);
          f.classList.toggle("pf-dim", f.dataset.provFill !== prov);
        });
        badges.forEach((badge) => badge.classList.toggle("is-active", badge.dataset.badge === prov));
      });
      zone.addEventListener("mouseleave", () => {
        fills.forEach((f) => { f.classList.remove("pf-highlight", "pf-dim"); });
        badges.forEach((badge) => badge.classList.remove("is-active"));
      });
      // Mobile tap
      zone.addEventListener("focus", () => {
        const prov = zone.dataset.prov;
        badges.forEach((badge) => badge.classList.toggle("is-active", badge.dataset.badge === prov));
      });
      zone.addEventListener("blur", () => {
        badges.forEach((badge) => badge.classList.remove("is-active"));
      });
    });
  };

  const setupScrollDepthNav = () => {
    const nav = document.getElementById("scrollDepthNav");
    if (!nav) return;

    const sectionData = [
      { id: "section-hero",          label: "Hero" },
      { id: "section-treatises",     label: "Treatises" },
      { id: "section-latest",        label: "Latest Work" },
      { id: "section-scenario",      label: "Scenario Lab" },
      { id: "section-questions",     label: "Questions" },
      { id: "section-research",      label: "Research" },
      { id: "section-platform",      label: "Platform" },
      { id: "section-evidence",      label: "Evidence" },
      { id: "section-participation", label: "Participation" },
    ];

    const sections = sectionData
      .map((s) => ({ el: document.getElementById(s.id), label: s.label }))
      .filter((s) => s.el);

    if (sections.length < 2) return;

    // Build dots
    const dots = sections.map(({ el, label }) => {
      const btn = document.createElement("button");
      btn.className = "sdnav-dot";
      btn.setAttribute("data-label", label);
      btn.setAttribute("aria-label", `Jump to ${label}`);
      btn.addEventListener("click", () => el.scrollIntoView({ behavior: "smooth" }));
      nav.appendChild(btn);
      return btn;
    });

    // Update nav visibility: Hidden on hero, appears when user scrolls below hero
    const hero = document.getElementById("section-hero");
    const updateNavVisibility = () => {
      if (!hero) {
        nav.classList.add("is-visible");
        return;
      }
      const heroRect = hero.getBoundingClientRect();
      const isBelowHero = heroRect.bottom <= window.innerHeight * 0.35;
      nav.classList.toggle("is-visible", isBelowHero);
    };
    window.addEventListener("scroll", updateNavVisibility, { passive: true });
    window.addEventListener("resize", updateNavVisibility, { passive: true });
    updateNavVisibility();

    // Track active section
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const idx = sections.findIndex((s) => s.el === entry.target);
          if (idx === -1) return;
          dots.forEach((dot, i) => dot.classList.toggle("is-active", i === idx));
        });
      },
      { threshold: 0.45, rootMargin: "-10% 0px -10% 0px" }
    );

    sections.forEach((s) => observer.observe(s.el));
  };

  const setupScrollCueFade = () => {
    const cue = document.querySelector(".hero-map-scroll-cue, .hero-scroll-cue");
    if (!cue) return;
    const hero = document.getElementById("section-hero");
    if (!hero) return;
    window.addEventListener(
      "scroll",
      () => {
        const heroBottom = hero.getBoundingClientRect().bottom;
        const fade = Math.max(0, Math.min(1, (heroBottom - window.innerHeight * 0.15) / (window.innerHeight * 0.85)));
        cue.style.opacity = fade;
      },
      { passive: true }
    );
  };

  const setupPageProgress = () => {
    const bar = document.querySelector("[data-page-progress] span");
    if (!bar) return;
    let frame = null;
    const update = () => {
      if (frame) return;
      frame = requestAnimationFrame(() => {
        const scrollable = document.documentElement.scrollHeight - window.innerHeight;
        const progress = scrollable > 0 ? Math.min(1, Math.max(0, window.scrollY / scrollable)) : 0;
        bar.style.width = `${progress * 100}%`;
        frame = null;
      });
    };
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
  };

  const setupScenarioPreview = () => {
    const frame = document.getElementById("homeMapPreview");
    const buttons = [...document.querySelectorAll("[data-preview-mode]")];
    if (!frame || !buttons.length) return;

    const title = document.querySelector("[data-preview-title]");
    const badge = document.querySelector("[data-preview-badge]");
    const copy = document.querySelector("[data-preview-copy]");

    const models = {
      ppri: {
        src: "/maps/scenarios/index.html?embed=1",
        title: "PPRI-01 · illustrative scenario",
        badge: "PPRI-01 model",
        copy: "The live PPRI-01 preview uses the same scenario map that powers the full Scenario Lab. It is illustrative, editable and separate from enacted administrative boundaries.",
      },
      current: {
        src: "/maps/current/administrative.html?embed=1",
        title: "Current · geographic reference",
        badge: "Current reference map",
        copy: "The current view is the reference geography used to orient the research. Switch back to PPRI-01 to see the illustrative scenario layer.",
      },
    };

    let loadedMode = "ppri";

    const applyMode = (mode) => {
      const model = models[mode];
      if (!model) return;

      buttons.forEach((button) => button.classList.toggle("is-active", button.dataset.previewMode === mode));
      if (title) title.textContent = model.title;
      if (badge) badge.textContent = model.badge;
      if (copy) copy.textContent = model.copy;

      if (loadedMode !== mode) {
        frame.src = model.src;
        loadedMode = mode;
      }
    };

    buttons.forEach((button) => {
      button.addEventListener("click", () => applyMode(button.dataset.previewMode));
    });
  };

  const setupQuestionWorkbench = () => {
    const tabs = [...document.querySelectorAll("[data-question]")];
    if (!tabs.length) return;

    const title = document.querySelector("[data-question-title]");
    const copy = document.querySelector("[data-question-copy]");
    const link = document.querySelector("[data-question-link]");
    const kicker = document.querySelector("[data-question-kicker]");
    const route = document.querySelector("[data-question-route]");

    const questions = [
      {
        title: "Why are new provinces being discussed?",
        copy: "Explore arguments about representation, administrative reach, geographic scale, public services, reservations and alternative reform pathways.",
        href: "/provinces/why-provinces.html",
        route: "Question → evidence → reform options",
      },
      {
        title: "Could stronger local government address some of the same issues?",
        copy: "Examine provincial restructuring alongside constitutional local-government devolution and the question of where authority should sit.",
        href: "/provinces/local-government.html",
        route: "Question → devolution → institutional design",
      },
      {
        title: "What would reform need to finance?",
        copy: "Follow the fiscal side of reform: revenue, transfers, expenditure, assets, liabilities and transition arrangements.",
        href: "/provinces/fiscal-framework.html",
        route: "Question → fiscal framework → transition",
      },
      {
        title: "What would the constitutional process involve?",
        copy: "Start with the governing constitutional provisions and the documented legal procedure before drawing conclusions about any proposal.",
        href: "/provinces/constitutional-framework.html",
        route: "Question → law → constitutional process",
      },
      {
        title: "What does the evidence show?",
        copy: "Use the Data Observatory to explore population, geography, administrative scale and the sources behind the numbers.",
        href: "/data/centre.html",
        route: "Question → data → interpretation",
      },
      {
        title: "What could a different map look like?",
        copy: "Move from a conceptual reform question to a visible model: compare the reference geography, PPRI-01 and your own scenario.",
        href: "/maps/scenarios/index.html",
        route: "Question → map → scenario testing",
      },
    ];

    const activate = (index) => {
      const item = questions[index];
      if (!item) return;
      tabs.forEach((tab) => {
        const active = Number(tab.dataset.question) === index;
        tab.classList.toggle("is-active", active);
        tab.setAttribute("aria-selected", String(active));
      });
      if (kicker) kicker.textContent = `Research question ${String(index + 1).padStart(2, "0")}`;
      if (title) title.textContent = item.title;
      if (copy) copy.textContent = item.copy;
      if (link) link.href = item.href;
      if (route) route.textContent = item.route;
    };

    tabs.forEach((tab) => {
      tab.addEventListener("mouseenter", () => activate(Number(tab.dataset.question)));
      tab.addEventListener("focus", () => activate(Number(tab.dataset.question)));
      tab.addEventListener("click", () => activate(Number(tab.dataset.question)));
      tab.addEventListener("keydown", (event) => {
        if (event.key !== "ArrowDown" && event.key !== "ArrowUp") return;
        event.preventDefault();
        const current = tabs.indexOf(tab);
        const next = event.key === "ArrowDown" ? (current + 1) % tabs.length : (current - 1 + tabs.length) % tabs.length;
        tabs[next].focus();
        activate(next);
      });
    });
  };

  const setupHomepageFeed = () => {
    const feed = document.querySelector("[data-homefeed]");
    if (!feed) return;

    const escapeHtml = (value) =>
      String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");

    const formatCard = (item) => `
      <a class="latest-card" href="${escapeHtml(item.url)}">
        <span class="card-meta">${escapeHtml(item.type)}</span>
        <h3>${escapeHtml(item.title)}</h3>
        <p>${escapeHtml(item.summary)}</p>
        <span class="home-card-link">Open publication <span aria-hidden="true">→</span></span>
      </a>`;

    fetch("/content/homepage.json", { cache: "no-cache" })
      .then((response) => {
        if (!response.ok) throw new Error(`Homepage feed HTTP ${response.status}`);
        return response.json();
      })
      .then((data) => {
        const latest = Array.isArray(data.latest) ? data.latest.slice(0, 3) : [];
        if (latest.length) feed.innerHTML = latest.map(formatCard).join("");

        const featured = data.featured;
        if (!featured) return;
        const feature = document.querySelector("[data-featured-publication]");
        if (!feature) return;
        feature.querySelector("[data-feature-type]").textContent = `${featured.type} · ${featured.id} · ${featured.date}`;
        feature.querySelector("[data-feature-title]").textContent = featured.title;
        feature.querySelector("[data-feature-summary]").textContent = featured.summary;
        feature.querySelector("[data-feature-link]").href = featured.url;
        feature.querySelector("[data-feature-download]").href = featured.download;
      })
      .catch(() => {
        // Static semantic fallback in index.html remains visible.
      });
  };

  const setupSearchShortcut = () => {
    window.addEventListener("keydown", (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        window.location.href = "/search.html";
      }
    });
  };

  setRevealObserver();
  setupHeroMessages();
  setupPakistanCanvas();
  setupPageProgress();
  setupScenarioPreview();
  setupQuestionWorkbench();
  setupHomepageFeed();
  setupScrollDepthNav();
  setupScrollCueFade();
  setupSearchShortcut();
});
