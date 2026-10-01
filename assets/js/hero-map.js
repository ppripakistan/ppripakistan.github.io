/**
 * PPRI — Interactive Map Hero  |  hero-map.js  v4
 * Authentic Pakistan borders (Leaflet.js) · 16-unit dissolve ·
 * Magnetic unit hover with metadata tooltip · Jitter-free HUD dock
 */

(function () {
  "use strict";

  /* ── DOM References ────────────────────────────────────────────────────── */
  const section      = document.querySelector(".hero-map-section");
  const mapContainer = document.getElementById("hero-map-container");
  const hudWrapper   = document.getElementById("hudWrapper");
  const hudDock      = document.getElementById("hudDock");
  const hudTrigger   = document.getElementById("hudTrigger");
  const hudClose     = document.getElementById("hudClose");
  const tooltip      = document.getElementById("pak-tooltip");

  if (!section || !mapContainer) return;

  /* ── State ─────────────────────────────────────────────────────────────── */
  let mapInstance       = null;
  let currentLayerGroup = null;
  let scenarioGroup     = null;
  let scenarioLayersMap = new Map();

  let mouseX = 0, mouseY = 0;
  let tooltipVisible   = false;
  let tooltipAnimFrame = null;
  let animationTriggered = false;

  // Jitter-free HUD debounce timers
  let hudExpandTimer   = null;
  let hudCollapseTimer = null;
  const HUD_EXPAND_DELAY   = 160;
  const HUD_COLLAPSE_DELAY = 220;

  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ── Initialize Leaflet Map ────────────────────────────────────────────── */
  function initLeafletMap() {
    if (typeof L === "undefined") {
      setTimeout(initLeafletMap, 60);
      return;
    }

    // Pure vector canvas without external tile imagery or default controls
    mapInstance = L.map(mapContainer, {
      zoomControl: false,
      attributionControl: false,
      dragging: false,
      touchZoom: false,
      scrollWheelZoom: false,
      doubleClickZoom: false,
      boxZoom: false,
      keyboard: false,
      inertia: false,
    });

    const PAK_BOUNDS = L.latLngBounds([23.4, 60.6], [37.2, 77.4]);
    mapInstance.fitBounds(PAK_BOUNDS, { padding: [15, 15] });

    window.addEventListener("resize", () => {
      if (mapInstance) {
        mapInstance.invalidateSize();
        mapInstance.fitBounds(PAK_BOUNDS, { padding: [15, 15] });
      }
    }, { passive: true });

    loadGeographicData();
  }

  /* ── Load Authentic Geography & Build Layers ───────────────────────────── */
  function loadGeographicData() {
    fetch("/assets/data/hero-pakistan-geography.json")
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then(data => {
        renderMapLayers(data);
      })
      .catch(err => {
        console.warn("Hero map geography load fallback:", err);
      });
  }

  function renderMapLayers(data) {
    if (!mapInstance) return;

    currentLayerGroup = L.layerGroup().addTo(mapInstance);
    scenarioGroup     = L.layerGroup().addTo(mapInstance);

    // 1. Current 4 Constitutional Provinces (plus federal reference)
    L.geoJSON(data.currentProvinces, {
      style: () => ({
        className: "hero-prov-path",
        color: "rgba(168, 224, 106, 0.48)",
        weight: 1.8,
        fillColor: "rgba(168, 224, 106, 0.04)",
        fillOpacity: 0.04,
        lineJoin: "round",
        lineCap: "round"
      })
    }).addTo(currentLayerGroup);

    // 2. 16 Scenario Units (Dissolved illustrative model)
    L.geoJSON(data.scenarioUnits, {
      style: () => ({
        className: "hero-unit-path",
        color: "#a8e06a",
        weight: 1.5,
        fillColor: "rgba(168, 224, 106, 0.07)",
        fillOpacity: 0.07,
        lineJoin: "round",
        lineCap: "round"
      }),
      onEachFeature: (feature, layer) => {
        const u = feature.properties || {};
        scenarioLayersMap.set(u.id, layer);

        layer.on({
          mouseover: (e) => onUnitHover(e, u, layer),
          mouseout:  ()  => onUnitLeave(layer),
          mousemove: onUnitMouseMove
        });
      }
    }).addTo(scenarioGroup);

    // Start animation on reveal
    setupAnimationTrigger();
  }

  /* ── Dissolve Animation Sequence ───────────────────────────────────────── */
  function setupAnimationTrigger() {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting && !animationTriggered) {
        animationTriggered = true;
        observer.disconnect();
        startDissolveSequence();
      }
    }, { threshold: 0.25 });

    observer.observe(section);

    // Also trigger if already in view
    const rect = section.getBoundingClientRect();
    if (rect.top < window.innerHeight * 0.9 && !animationTriggered) {
      animationTriggered = true;
      startDissolveSequence();
    }
  }

  function startDissolveSequence() {
    if (prefersReducedMotion) {
      mapContainer.querySelectorAll(".hero-unit-path").forEach(p => p.classList.add("is-active"));
      return;
    }

    // Phase 1: 4 current provinces shown in crisp wireframe
    // Phase 2: After 1.2s delay, dissolve cleanly into the 16 scenario units
    setTimeout(() => {
      // Dim the current provinces outline
      mapContainer.querySelectorAll(".hero-prov-path").forEach(p => p.classList.add("is-dimmed"));

      // Fade in the 16 scenario units
      mapContainer.querySelectorAll(".hero-unit-path").forEach(p => p.classList.add("is-active"));
    }, 1200);
  }

  /* ── Interactive Magnetic Hover & Tooltip ──────────────────────────────── */
  function onUnitHover(e, unit, layer) {
    if (!unit) return;

    // Highlight active unit, dim all other units
    scenarioLayersMap.forEach((l) => {
      const path = l.getElement ? l.getElement() : null;
      if (!path) return;
      if (l === layer) {
        path.classList.add("is-hovered");
        path.classList.remove("is-dimmed");
        if (l.bringToFront) l.bringToFront();
      } else {
        path.classList.add("is-dimmed");
        path.classList.remove("is-hovered");
      }
    });

    showTooltip(unit);
  }

  function onUnitLeave(layer) {
    scenarioLayersMap.forEach((l) => {
      const path = l.getElement ? l.getElement() : null;
      if (path) {
        path.classList.remove("is-hovered", "is-dimmed");
      }
    });

    hideTooltip();
  }

  function onUnitMouseMove(e) {
    if (e.originalEvent) {
      mouseX = e.originalEvent.clientX;
      mouseY = e.originalEvent.clientY;
    }
    updateTooltipPosition();
  }

  /* ── Tooltip Management ────────────────────────────────────────────────── */
  function showTooltip(unit) {
    if (!tooltip || !unit) return;
    const ttName = tooltip.querySelector(".tt-name");
    const ttProv = tooltip.querySelector(".tt-province");
    const ttMeta = tooltip.querySelector(".tt-meta");

    if (ttName) ttName.textContent = unit.name || "";
    if (ttProv) ttProv.textContent = `Province: ${unit.province || ""}`;
    if (ttMeta) {
      ttMeta.innerHTML = `
        <div class="tt-meta-item"><strong>${unit.pop     || "—"}</strong>Population</div>
        <div class="tt-meta-item"><strong>${unit.capital || "—"}</strong>Capital</div>
        <div class="tt-meta-item" style="grid-column:1/-1"><strong>${unit.area || "—"}</strong>Area</div>
      `;
    }

    tooltip.classList.add("is-visible");
    tooltipVisible = true;
    updateTooltipPosition();
  }

  function hideTooltip() {
    if (!tooltip) return;
    tooltip.classList.remove("is-visible");
    tooltipVisible = false;
  }

  function updateTooltipPosition() {
    if (!tooltip || !tooltipVisible) return;
    if (tooltipAnimFrame) cancelAnimationFrame(tooltipAnimFrame);

    tooltipAnimFrame = requestAnimationFrame(() => {
      const tw = tooltip.offsetWidth;
      const th = tooltip.offsetHeight;
      const vw = window.innerWidth;
      const vh = window.innerHeight;
      const off = 18;

      let x = mouseX + off;
      let y = mouseY - off - th / 2;

      if (x + tw + 8 > vw) x = mouseX - tw - off;
      if (y < 8) y = 8;
      if (y + th > vh - 8) y = vh - th - 8;

      tooltip.style.left = `${x}px`;
      tooltip.style.top  = `${y}px`;
    });
  }

  document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    if (tooltipVisible) updateTooltipPosition();
  }, { passive: true });

  /* ── Jitter-Free Collapsible HUD Dock ──────────────────────────────────── */
  function cancelExpand() {
    if (hudExpandTimer) { clearTimeout(hudExpandTimer); hudExpandTimer = null; }
  }
  function cancelCollapse() {
    if (hudCollapseTimer) { clearTimeout(hudCollapseTimer); hudCollapseTimer = null; }
  }

  function expandHUD() {
    cancelCollapse();
    if (!hudDock || hudDock.classList.contains("is-expanded")) return;
    cancelExpand();
    hudExpandTimer = setTimeout(() => {
      hudDock.classList.add("is-expanded");
      hudDock.setAttribute("aria-expanded", "true");
      section.classList.add("hud-open");
      hudExpandTimer = null;
    }, HUD_EXPAND_DELAY);
  }

  function collapseHUD() {
    cancelExpand();
    if (!hudDock || !hudDock.classList.contains("is-expanded")) return;
    cancelCollapse();
    hudCollapseTimer = setTimeout(() => {
      hudDock.classList.remove("is-expanded");
      hudDock.setAttribute("aria-expanded", "false");
      section.classList.remove("hud-open");
      hudCollapseTimer = null;
    }, HUD_COLLAPSE_DELAY);
  }

  const hudTarget = hudWrapper || hudDock;
  if (hudTarget) {
    hudTarget.addEventListener("mouseenter", () => {
      cancelCollapse();
      expandHUD();
    });

    hudTarget.addEventListener("mouseleave", (e) => {
      const related = e.relatedTarget;
      if (hudTarget.contains(related) || (hudDock && hudDock.contains(related))) return;
      collapseHUD();
    });
  }

  if (hudTrigger) {
    hudTrigger.addEventListener("click", (e) => {
      e.stopPropagation();
      expandHUD();
    });
  }

  if (hudClose) {
    hudClose.addEventListener("click", (e) => {
      e.stopPropagation();
      cancelExpand();
      cancelCollapse();
      if (hudDock) {
        hudDock.classList.remove("is-expanded");
        hudDock.setAttribute("aria-expanded", "false");
      }
      section.classList.remove("hud-open");
    });
  }

  /* ── Boot ──────────────────────────────────────────────────────────────── */
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initLeafletMap);
  } else {
    initLeafletMap();
  }

})();
