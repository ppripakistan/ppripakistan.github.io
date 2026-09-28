(function () {
  "use strict";
  const DATA_URL = "/data/provinces/provinces-2023.json";
  const fmt = (n) => Number(n).toLocaleString("en-US");
  const pct = (n) => Number(n).toFixed(2) + "%";
  async function getData() {
    const r = await fetch(DATA_URL);
    if (!r.ok) throw new Error("Dataset unavailable");
    return (await r.json()).records;
  }
  function optionList(select, rows) {
    select.innerHTML = rows
      .map(
        (r, i) =>
          `<option value="${r.code}" ${i === 0 ? "selected" : ""}>${r.name}</option>`,
      )
      .join("");
  }
  function barChart(canvas, rows, key, label) {
    const ctx = canvas.getContext("2d"),
      d = window.devicePixelRatio || 1,
      w = canvas.clientWidth * d,
      h = canvas.clientHeight * d;
    canvas.width = w;
    canvas.height = h;
    ctx.clearRect(0, 0, w, h);
    const max = Math.max(...rows.map((r) => Number(r[key]))),
      pad = 55 * d,
      gap = 16 * d,
      bw = Math.max(
        24 * d,
        (w - pad * 2 - gap * (rows.length - 1)) / rows.length,
      );
    ctx.strokeStyle = "#dce3e8";
    ctx.fillStyle = "#17232d";
    ctx.font = `12px system-ui`;
    [0, 0.25, 0.5, 0.75, 1].forEach((t) => {
      const y = h - pad - t * (h - pad * 1.5);
      ctx.beginPath();
      ctx.moveTo(pad, y);
      ctx.lineTo(w - pad, y);
      ctx.stroke();
      ctx.fillText(((max * t) / 1e6).toFixed(0) + "m", 8 * d, y + 4 * d);
    });
    rows.forEach((r, i) => {
      const v = Number(r[key]),
        bh = (v / max) * (h - pad * 1.5),
        x = pad + i * (bw + gap),
        y = h - pad - bh;
      ctx.fillStyle = "#b08a49";
      ctx.fillRect(x, y, bw, bh);
      ctx.fillStyle = "#17232d";
      ctx.save();
      ctx.translate(x + bw / 2, h - pad + 19 * d);
      ctx.rotate(-Math.PI / 8);
      ctx.textAlign = "right";
      ctx.fillText(r.name, 0, 0);
      ctx.restore();
    });
    ctx.fillStyle = "#17232d";
    ctx.font = "700 14px system-ui";
    ctx.fillText(label, pad, 22 * d);
  }
  function initCentre(rows) {
    const tbody = document.querySelector("#p6ProvinceTable tbody");
    if (tbody) {
      tbody.innerHTML = rows
        .map(
          (r) =>
            `<tr><td>${r.name}</td><td class="number">${fmt(r.population_2023)}</td><td>${pct(r.share_percent)}</td><td>${fmt(r.area_sq_km)}</td><td>${Number(r.density_per_sq_km).toFixed(1)}</td><td>${Number(r.urban_proportion_pct).toFixed(1)}%</td><td>${Number(r.annual_growth_2017_2023_pct).toFixed(2)}%</td><td>${r.districts}</td></tr>`,
        )
        .join("");
    }
    const c = document.querySelector("#p6PopulationChart");
    if (c)
      barChart(
        c,
        rows,
        "population_2023",
        "Population by administrative unit — Census 2023",
      );
  }
  function initCompare(rows) {
    const a = document.querySelector("#p6CompareA"),
      b = document.querySelector("#p6CompareB"),
      metric = document.querySelector("#p6Metric"),
      out = document.querySelector("#p6ComparisonOutput");
    if (!a || !b) return;
    optionList(a, rows);
    optionList(b, rows);
    if (rows[1]) b.value = rows[1].code;
    function render() {
      const x = rows.find((r) => r.code === a.value),
        y = rows.find((r) => r.code === b.value),
        k = metric.value,
        labels = {
          population_2023: "Population",
          area_sq_km: "Area (sq km)",
          density_per_sq_km: "Density",
          urban_proportion_pct: "Urban proportion",
          annual_growth_2017_2023_pct: "2017–2023 annual growth",
          districts: "Districts",
        };
      out.innerHTML = `<div class="grid grid-2"><div class="card"><span class="card-meta">${x.name}</span><h3>${fmt(x[k])}${k.includes("pct") ? "%" : ""}</h3><p>${labels[k]}</p></div><div class="card"><span class="card-meta">${y.name}</span><h3>${fmt(y[k])}${k.includes("pct") ? "%" : ""}</h3><p>${labels[k]}</p></div></div><div class="p6-callout">This comparison is descriptive. It does not rank administrative units or establish that one structure is preferable to another.</div>`;
    }
    [a, b, metric].forEach((el) => el.addEventListener("change", render));
    render();
  }
  function initScenario(rows) {
    const p = document.querySelector("#p6ScenarioProvince"),
      n = document.querySelector("#p6ScenarioUnits"),
      o = document.querySelector("#p6ScenarioOutput");
    if (!p || !n) return;
    optionList(p, rows);
    function render() {
      const r = rows.find((x) => x.code === p.value),
        units = Math.max(2, Math.min(12, Number(n.value) || 2)),
        target = r.population_2023 / units,
        range = target * 0.1;
      o.innerHTML = `<p><span class="p6-badge">Illustrative analytical scenario</span></p><strong>${fmt(Math.round(target))}</strong><p>Illustrative target population per unit if ${r.name} were divided into ${units} equal-population units.</p><p class="muted">A ±10% planning band would be approximately ${fmt(Math.round(target - range))} to ${fmt(Math.round(target + range))} people. This is a mathematical thought experiment, not a proposed boundary or PPRI recommendation.</p>`;
    }
    [p, n].forEach((el) => el.addEventListener("input", render));
    render();
  }
  function initMap() {
    const el = document.getElementById("p6Map");
    if (!el || typeof L === "undefined") return;
    const map = L.map(el, { scrollWheelZoom: false }).setView([30.4, 69.3], 5);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "&copy; OpenStreetMap contributors",
    }).addTo(map);
    const adm1 =
      "https://services2.arcgis.com/xsh7pVZv42relbEf/ArcGIS/rest/services/Pakistan_Administrative_Boundaries/FeatureServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=geojson";
    const adm3 =
      "https://services2.arcgis.com/xsh7pVZv42relbEf/ArcGIS/rest/services/Pakistan_Administrative_Boundaries/FeatureServer/3/query?where=1%3D1&outFields=*&outSR=4326&f=geojson";
    fetch(adm1)
      .then((r) => r.json())
      .then((g) => {
        L.geoJSON(g, {
          style: { color: "#b08a49", weight: 2, fillOpacity: 0.12 },
          onEachFeature: (f, l) =>
            l.bindPopup(
              `<strong>${f.properties.NAME_1 || "Province"}</strong><br>Boundary layer: ADM1`,
            ),
        }).addTo(map);
      })
      .catch(() => {});
    fetch(adm3)
      .then((r) => r.json())
      .then((g) => {
        L.geoJSON(g, {
          style: { color: "#748493", weight: 0.55, fillOpacity: 0 },
          onEachFeature: (f, l) =>
            l.bindPopup(
              `<strong>${f.properties.NAME_3 || "District"}</strong><br>District boundary layer`,
            ),
        }).addTo(map);
      })
      .catch(() => {});
  }
  document.addEventListener("DOMContentLoaded", () => {
    getData()
      .then((rows) => {
        initCentre(rows);
        initCompare(rows);
        initScenario(rows);
      })
      .catch((e) => console.warn("PPRI Observatory:", e));
    initMap();
  });
})();
