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

  setRevealObserver();
  setupScenarioPreview();
  setupQuestionWorkbench();
  setupHomepageFeed();
});
