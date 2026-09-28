(function () {
  "use strict";

  const ADM0_URL =
    "https://cdn.jsdelivr.net/gh/PakData/GISData@master/PAK-GeoJSON/PAK_adm0.json";
  const ADM1_URL =
    "https://cdn.jsdelivr.net/gh/PakData/GISData@master/PAK-GeoJSON/PAK_adm1.json";
  const ADM3_URL =
    "https://cdn.jsdelivr.net/gh/PakData/GISData@master/PAK-GeoJSON/PAK_adm3.json";
  const SCENARIO_URL = "/data/scenarios/ppri-01.json";

  const COLORS = [
    "#0f766e",
    "#2563eb",
    "#b45309",
    "#7c3aed",
    "#be123c",
    "#0369a1",
    "#15803d",
    "#9333ea",
    "#c2410c",
    "#475569",
    "#4338ca",
    "#a16207",
    "#be185d",
    "#047857",
    "#7e22ce",
    "#1d4ed8",
    "#9f1239",
    "#0e7490",
  ];

  const normalize = (value) =>
    String(value || "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .replace(/&/g, "and")
      .replace(/[’']/g, "")
      .replace(/[^a-z0-9]+/g, " ")
      .trim();

  const canonical = (value) => {
    let n = normalize(value);
    const aliases = {
      baluchistan: "balochistan",
      "north west frontier province": "khyber pakhtunkhwa",
      "northwest frontier province": "khyber pakhtunkhwa",
      "north west frontier": "khyber pakhtunkhwa",
      nwfp: "khyber pakhtunkhwa",
      "n w f p": "khyber pakhtunkhwa",
      kpk: "khyber pakhtunkhwa",
      "k p k": "khyber pakhtunkhwa",
      fata: "khyber pakhtunkhwa",
      "f a t a": "khyber pakhtunkhwa",
      "f a t a area": "khyber pakhtunkhwa",
      "federally administered tribal areas": "khyber pakhtunkhwa",
      "khyber pakhtunkhwa province": "khyber pakhtunkhwa",
      "khyber pakhtunkhwa (n w f p)": "khyber pakhtunkhwa",
      "azad jammu and kashmir": "azad jammu kashmir",
      ajk: "azad jammu kashmir",
      "azad kashmir": "azad jammu kashmir",
      "gilgit baltistan territory": "gilgit baltistan",
      "gilgit baltistan": "gilgit baltistan",
      "gilgit baltistan province": "gilgit baltistan",
      "gilgit baltistan administrative territory": "gilgit baltistan",
      "northern areas": "gilgit baltistan",
      "northern area": "gilgit baltistan",
      gilgit: "gilgit baltistan",
      "islamabad capital territory": "islamabad",
      "islamabad territory": "islamabad",
      "federal capital territory": "islamabad",
      "federal capital": "islamabad",
      "islamabad capital": "islamabad",
      fct: "islamabad",
      "f c t": "islamabad",
      sind: "sindh",
      "kambar shahdadkot": "qambar shahdadkot",
      kemari: "keamari",
      mekhran: "makran",
      mekran: "makran",
      nawabshah: "shaheed benazirabad",
      "d i khan": "dera ismail khan",
      "d g khan": "dera ghazi khan",
      "kolai palas": "kolai palas kohistan",
      "kolai palas kohistan": "kolai palas kohistan",
      "upper kohistan": "upper kohistan",
      "lower kohistan": "lower kohistan",
      "kolai pallas": "kolai palas kohistan",
      "south waziristan district": "south waziristan",
      "khyber pakhtunkhwa": "khyber pakhtunkhwa",
    };
    n = aliases[n] || n;
    return n.replace(/\s+(division|district|province|territory)$/g, "").trim();
  };

  const CURRENT_EXCLUDED_DISTRICTS = new Set([
    "kargil",
    "kupwara gilgit wazarat",
    "ladakh leh",
    "rann of kutch",
  ]);

  function isExcludedHistoricalDistrict(feature) {
    return CURRENT_EXCLUDED_DISTRICTS.has(district(feature));
  }

  const CURRENT_PROVINCE_METADATA = {
    punjab: {
      name: "Punjab",
      type: "Constitutional Province",
      legal: true,
      color: "#1e3a8a",
      fill: "#3b82f6",
    },
    sindh: {
      name: "Sindh",
      type: "Constitutional Province",
      legal: true,
      color: "#92400e",
      fill: "#f59e0b",
    },
    "khyber pakhtunkhwa": {
      name: "Khyber Pakhtunkhwa",
      type: "Constitutional Province",
      legal: true,
      color: "#065f46",
      fill: "#10b981",
    },
    balochistan: {
      name: "Balochistan",
      type: "Constitutional Province",
      legal: true,
      color: "#581c87",
      fill: "#a855f7",
    },
    islamabad: {
      name: "Islamabad Capital Territory",
      type: "Federal Capital Territory",
      legal: false,
      color: "#0369a1",
      fill: "#0ea5e9",
    },
    "gilgit baltistan": {
      name: "Gilgit-Baltistan",
      type: "Administrative Territory",
      legal: false,
      color: "#166534",
      fill: "#22c55e",
    },
    "azad jammu kashmir": {
      name: "Azad Jammu & Kashmir",
      type: "Administrative Territory",
      legal: false,
      color: "#c2410c",
      fill: "#f97316",
    },
  };

  function currentProvinceKey(feature) {
    const p = province(feature);
    if (
      p === "nwfp" ||
      p === "n w f p" ||
      p === "fata" ||
      p === "f a t a" ||
      p === "khyber pakhtunkhwa"
    )
      return "khyber pakhtunkhwa";
    if (p === "northern areas" || p === "gilgit baltistan")
      return "gilgit baltistan";
    if (p === "fct" || p === "f c t" || p === "islamabad") return "islamabad";
    if (p === "azad kashmir" || p === "azad jammu kashmir")
      return "azad jammu kashmir";
    if (p === "punjab") return "punjab";
    if (p === "sind" || p === "sindh") return "sindh";
    if (p === "balochistan" || p === "baluchistan") return "balochistan";
    return p;
  }

  let cachedCurrentProvinceFeatures = null;

  function buildCurrentProvinceFeatures(districtFeatures) {
    if (cachedCurrentProvinceFeatures && cachedCurrentProvinceFeatures.length) {
      return cachedCurrentProvinceFeatures;
    }
    const groups = new Map();
    (districtFeatures || []).forEach((feature) => {
      if (!feature?.geometry || isExcludedHistoricalDistrict(feature)) return;
      const key = currentProvinceKey(feature);
      if (!key) return;
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(feature);
    });

    const output = [];
    groups.forEach((items, key) => {
      let geometry;
      try {
        const fc = turf.featureCollection(items);
        geometry = items.length === 1 ? items[0] : turf.union(fc);
      } catch (error) {
        console.warn("Current province dissolve failed for", key, error);
        geometry = items.length === 1 ? items[0] : null;
      }
      if (!geometry) return;
      const meta = CURRENT_PROVINCE_METADATA[key] || {
        name: key,
        type: "Administrative unit",
        legal: false,
        color: "#111827",
        fill: "#64748b",
      };
      const feature =
        geometry.type === "Feature" ? geometry : turf.feature(geometry);
      feature.properties = {
        ...(feature.properties || {}),
        __currentProvinceKey: key,
        __currentProvinceName: meta.name,
        __currentProvinceType: meta.type,
        __currentProvinceLegal: meta.legal,
        __currentProvinceColor: meta.color,
        __currentProvinceFill: meta.fill,
        __districtCount: items.length,
      };
      output.push(feature);
    });
    cachedCurrentProvinceFeatures = output;
    return output;
  }

  const props = (feature) => feature?.properties || {};
  const firstProp = (p, keys) => {
    for (const key of keys)
      if (p[key] != null && String(p[key]).trim()) return p[key];
    return "";
  };
  const province = (feature) =>
    canonical(
      firstProp(props(feature), [
        "NAME_1",
        "VARNAME_1",
        "NL_NAME_1",
        "PROVINCE",
        "province",
      ]),
    );
  const country = (feature) =>
    canonical(
      firstProp(props(feature), [
        "NAME_0",
        "VARNAME_0",
        "NL_NAME_0",
        "COUNTRY",
        "country",
      ]),
    );
  const division = (feature) =>
    canonical(
      firstProp(props(feature), [
        "NAME_2",
        "VARNAME_2",
        "NL_NAME_2",
        "DIVISION",
        "division",
      ]),
    );
  const district = (feature) =>
    canonical(
      firstProp(props(feature), [
        "NAME_3",
        "VARNAME_3",
        "NL_NAME_3",
        "DISTRICT",
        "district",
      ]),
    );
  const displayDistrict = (feature) =>
    props(feature).NAME_3 || props(feature).DISTRICT || "District";
  const displayDivision = (feature) =>
    props(feature).NAME_2 || props(feature).DIVISION || "Division";
  const displayProvince = (feature) =>
    props(feature).NAME_1 ||
    props(feature).PROVINCE ||
    props(feature).NAME_0 ||
    "Administrative unit";

  function sameName(a, b) {
    return canonical(a) === canonical(b);
  }

  function fetchJSON(url, label = url, timeoutMs = 12000) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    return fetch(url, { signal: controller.signal, cache: "no-store" })
      .then((r) => {
        if (!r.ok) throw new Error(`${label}: HTTP ${r.status}`);
        return r.json();
      })
      .finally(() => clearTimeout(timer));
  }

  function baseMap(map) {
    const street = L.tileLayer(
      "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
      {
        maxZoom: 19,
        keepBuffer: 3,
        updateWhenIdle: false,
        updateWhenZooming: false,
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      },
    );
    const light = L.tileLayer(
      "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
      {
        maxZoom: 19,
        attribution: "&copy; OpenStreetMap contributors &copy; CARTO",
      },
    );
    street.addTo(map);
    // light.addTo(map);

    return { street, light };
  }

  function stabilizeMapSize(map, el) {
    const refresh = () =>
      requestAnimationFrame(() => map.invalidateSize({ pan: false }));
    refresh();
    window.addEventListener("load", refresh, { once: true });
    window.addEventListener("resize", refresh, { passive: true });
    if (window.ResizeObserver && el) {
      const observer = new ResizeObserver(refresh);
      observer.observe(el);
      map.once("unload", () => observer.disconnect());
    }
    [50, 250, 750].forEach((ms) => setTimeout(refresh, ms));
  }

  function pakistanMask(national) {
    const feature = national?.features?.[0];
    if (!feature?.geometry) return null;
    const holes = [];
    if (feature.geometry.type === "Polygon") {
      holes.push(feature.geometry.coordinates[0]);
    } else if (feature.geometry.type === "MultiPolygon") {
      feature.geometry.coordinates.forEach((poly) => {
        if (poly?.[0]) holes.push(poly[0]);
      });
    }
    if (!holes.length) return null;
    const world = [
      [-89, -179],
      [-89, 179],
      [89, 179],
      [89, -179],
      [-89, -179],
    ];
    const rings = [world].concat(
      holes.map((ring) => ring.map(([lng, lat]) => [lat, lng])),
    );
    return L.polygon(rings, {
      stroke: false,
      fillColor: "#f8fafc",
      fillOpacity: 0.94,
      interactive: false,
      pane: "ppri-mask",
    });
  }

  function configurePakistanView(map, national, el) {
    const layer = L.geoJSON(national);
    const bounds = layer.getBounds();
    if (!bounds.isValid()) return;
    map.setMaxBounds(bounds.pad(0.1));
    map.fitBounds(bounds, { padding: [24, 24], maxZoom: 6 });
    stabilizeMapSize(map, el);
  }

  function addPakistanMaskPane(map, national) {
    map.createPane("ppri-mask");
    map.getPane("ppri-mask").style.zIndex = 350;
    const mask = pakistanMask(national);
    if (mask) mask.addTo(map);
  }

  function initCurrentMap() {
    const el = document.getElementById("p6CurrentMap");
    if (!el || typeof L === "undefined") return;
    const map = L.map(el, {
      scrollWheelZoom: true,
      minZoom: 4,
      maxZoom: 12,
      worldCopyJump: false,
      zoomSnap: 0.25,
    }).setView([30.4, 69.3], 5);
    stabilizeMapSize(map, el);
    const bases = baseMap(map);
    const provinceLayer = L.layerGroup().addTo(map);
    const districtLayer = L.layerGroup().addTo(map);
    const status = document.getElementById("p6MapStatus");
    const provinceToggle = document.getElementById("p6ShowProvinces");
    const districtToggle = document.getElementById("p6ShowDistricts");

    Promise.all([
      fetchJSON(ADM0_URL, "Pakistan outline"),
      fetchJSON(ADM1_URL, "Current provinces"),
      fetchJSON(ADM3_URL, "District geography"),
    ])
      .then(([national, provinces, districts]) => {
        configurePakistanView(map, national, el);
        addPakistanMaskPane(map, national);
        const currentFeatures = buildCurrentProvinceFeatures(
          districts.features || [],
        );
        currentFeatures.forEach((feature) => {
          const meta = feature.properties || {};
          L.geoJSON(feature, {
            style: {
              color: meta.__currentProvinceColor || "#111827",
              weight: 2.4,
              fillColor: meta.__currentProvinceFill || "#ffffff",
              fillOpacity: 0.24,
            },
            onEachFeature: (f, layer) => {
              const badge = meta.__currentProvinceLegal
                ? "Constitutional Legal Province"
                : meta.__currentProvinceType;
              layer.bindPopup(
                `<strong>${meta.__currentProvinceName}</strong><br><span>${badge}</span><br><small>${meta.__districtCount || ""} districts</small>`,
              );
            },
          }).addTo(provinceLayer);
        });
        L.geoJSON(
          { type: "FeatureCollection", features: districts.features || [] },
          {
            style: { color: "#475569", weight: 0.65, fillOpacity: 0 },
            onEachFeature: (feature, layer) =>
              layer.bindPopup(
                `<strong>${displayDistrict(feature)}</strong><br>${displayDivision(feature)} Division<br><span>Current ADM3 reference boundary</span>`,
              ),
          },
        ).addTo(districtLayer);
        if (status)
          status.textContent =
            "Pakistan boundary and current administrative layers loaded.";
      })
      .catch(() => {
        if (status)
          status.textContent =
            "The administrative boundary source could not be loaded. Check the network connection.";
      });

    provinceToggle?.addEventListener("change", () =>
      provinceToggle.checked
        ? map.addLayer(provinceLayer)
        : map.removeLayer(provinceLayer),
    );
    districtToggle?.addEventListener("change", () =>
      districtToggle.checked
        ? map.addLayer(districtLayer)
        : map.removeLayer(districtLayer),
    );
    L.control
      .layers(
        { OpenStreetMap: bases.street, "Light map": bases.light },
        {
          "Provincial boundaries": provinceLayer,
          "District boundaries": districtLayer,
        },
        { collapsed: false },
      )
      .addTo(map);
  }

  // Legacy GADM/PakData has several historical labels and, for some
  // territories, a different administrative hierarchy. These fallbacks are
  // deliberately data-specific: they map the source geography to the PPRI
  // scenario without changing the scenario JSON itself.
  const SOURCE_DISTRICT_ALIASES = {
    Islamabad: ["Islamabad", "Islamabad Capital Territory", "ICT"],
    "Gilgit-Baltistan": [
      "Gilgit",
      "Gilgit Agency",
      "Baltistan",
      "Diamer",
      "Ghizer",
      "Hunza",
      "Nagar",
      "Skardu",
      "Ghanche",
      "Astore",
    ],
    "Rural Sindh": [
      "Hyderabad",
      "Dadu",
      "Thatta",
      "Badin",
      "Jamshoro",
      "Matiari",
      "Tando Allahyar",
      "Tando Muhammad Khan",
      "Mirpur Khas",
      "Tharparkar",
      "Umerkot",
      "Sanghar",
      "Shaheed Benazirabad",
      "Nawabshah",
    ],
    Mehran: [
      "Sukkur",
      "Khairpur",
      "Ghotki",
      "Larkana",
      "Kambar Shahdadkot",
      "Qambar Shahdadkot",
      "Shikarpur",
      "Jacobabad",
      "Kashmore",
      "Kandhkot",
    ],
    Khyber: [
      "Peshawar",
      "Charsadda",
      "Nowshera",
      "Mardan",
      "Swabi",
      "Malakand",
      "Lower Dir",
      "Upper Dir",
      "Swat",
      "Buner",
      "Chitral",
      "Khyber",
      "Mohmand",
      "Bajaur",
      "Kurram",
      "Orakzai",
      "North Waziristan",
    ],
    "South KPK": [
      "Kohat",
      "Hangu",
      "Karak",
      "Bannu",
      "Lakki Marwat",
      "Dera Ismail Khan",
      "Tank",
      "South Waziristan",
    ],
    Hazara: ["Abbottabad", "Haripur", "Mansehra", "Battagram", "Torghar"],
    Kohistan: [
      "Kohistan",
      "Lower Kohistan",
      "Upper Kohistan",
      "Kolai Palas",
      "Kolai Pallas",
    ],
  };

  const SOURCE_DIVISION_ALIASES = {
    "Rural Sindh": [
      "Hyderabad",
      "Mirpur Khas",
      "Nawabshah",
      "Shaheed Benazirabad",
    ],
    Mehran: ["Larkana", "Sukkur"],
    Khyber: ["Peshawar", "Mardan", "Malakand"],
    "South KPK": ["Kohat", "Bannu", "Dera Ismail Khan"],
    Hazara: ["Hazara"],
  };

  const FALLBACK_UNIT_IDS = new Map(
    Object.entries(SOURCE_DISTRICT_ALIASES).map(([name, aliases]) => [
      name,
      aliases.map(canonical),
    ]),
  );
  const FALLBACK_DIVISIONS = new Map(
    Object.entries(SOURCE_DIVISION_ALIASES).map(([name, aliases]) => [
      name,
      aliases.map(canonical),
    ]),
  );

  function fallbackMatches(feature, unitName) {
    const aliases = FALLBACK_UNIT_IDS.get(unitName) || [];
    const divAliases = FALLBACK_DIVISIONS.get(unitName) || [];
    const d = district(feature);
    const div = division(feature);
    const raw = props(feature);
    const values = [
      d,
      division(feature),
      province(feature),
      raw.NAME_3,
      raw.VARNAME_3,
      raw.NL_NAME_3,
      raw.NAME_2,
      raw.VARNAME_2,
      raw.NL_NAME_2,
      raw.NAME_1,
      raw.VARNAME_1,
      raw.NL_NAME_1,
    ]
      .filter(Boolean)
      .map(canonical);
    if (divAliases.includes(div)) return true;
    return aliases.some((alias) => values.includes(alias));
  }

  function ruleMatches(feature, rule) {
    const p = province(feature),
      d = district(feature),
      div = division(feature),
      c = country(feature);
    const raw = props(feature);
    const adminNames = [
      raw.NAME_1,
      raw.PROVINCE,
      raw.province,
      raw.NAME_2,
      raw.DIVISION,
      raw.division,
      raw.NAME_3,
      raw.DISTRICT,
      raw.district,
      raw.NAME,
      raw.name,
    ]
      .filter(Boolean)
      .map(canonical);
    const hasName = (name) => adminNames.includes(canonical(name));
    if (rule.level === "province")
      return (
        hasName(rule.province) ||
        sameName(p, rule.province) ||
        sameName(c, rule.province)
      );
    if (rule.level === "district") {
      const list = rule.districts || (rule.district ? [rule.district] : []);
      return list.some((name) => sameName(d, name));
    }
    if (rule.level === "district-prefix") {
      const prefix = canonical(rule.prefix);
      return d === prefix || d.startsWith(`${prefix} `);
    }
    if (rule.level === "division") {
      const sameProvince = !rule.province || sameName(p, rule.province);
      const divisions = rule.divisions || [];
      const excluded = rule.excludeDistricts || [];
      return (
        sameProvince &&
        divisions.some((name) => sameName(div, name) || hasName(name)) &&
        !excluded.some((name) => sameName(d, name))
      );
    }
    return false;
  }

  function matchesAnyRule(feature, rules) {
    return (rules || []).some((rule) => ruleMatches(feature, rule));
  }

  function unitHasGeometry(unit, adm1, adm3) {
    if (unit.type === "federal-territory") {
      const direct = adm1.filter((f) => matchesAnyRule(f, unit.rules));
      if (direct.length) return direct;
      // Some legacy ADM1 files use historical territory names. Try the
      // district source as a last-resort geometry source for single-unit
      // territories so coverage never depends on a perfect ADM1 label.
      return adm3.filter((f) => fallbackMatches(f, unit.name));
    }
    const direct = adm3.filter((f) => matchesAnyRule(f, unit.rules));
    if (direct.length) return direct;
    return adm3.filter((f) => fallbackMatches(f, unit.name));
  }

  function getUnitFeatures(unit, adm1Features, districtFeatures) {
    return unitHasGeometry(unit, adm1Features || [], districtFeatures || []);
  }

  function makeDistrictAssignments(adm1Features, features, scenario) {
    const assignments = new Map();
    // scenario.units
    //   .filter(
    //     (u) => u.type !== "federal-territory" && u.type !== "federal-overlay",
    //   )
    //   .forEach((unit) => {
    scenario.units
      .filter((u) => u.type !== "federal-overlay")
      .forEach((unit) => {
        getUnitFeatures(unit, adm1Features, features).forEach((feature) => {
          if (!assignments.has(feature)) assignments.set(feature, unit.id);
        });
      });
    // The legacy PakData dataset can represent Kohistan as one district rather than
    // the later Upper/Lower/Kolai Pallas split. Preserve that geography in PPRI-01.
    const kohistan = scenario.units.find((u) => u.id === "K-KOHISTAN");
    if (kohistan)
      features.forEach((f) => {
        if (canonical(displayDistrict(f)) === "kohistan")
          assignments.set(f, kohistan.id);
      });
    return assignments;
  }

  function initScenarioMap() {
    const el = document.getElementById("p6ScenarioMap");
    if (!el || typeof L === "undefined") return;
    const map = L.map(el, {
      scrollWheelZoom: true,
      minZoom: 4,
      maxZoom: 12,
      worldCopyJump: false,
      zoomSnap: 0.25,
    }).setView([30.4, 69.3], 5);
    stabilizeMapSize(map, el);
    const bases = baseMap(map);
    map.createPane("ppri-scenario");
    map.getPane("ppri-scenario").style.zIndex = 410;
    map.createPane("ppri-current");
    map.getPane("ppri-current").style.zIndex = 400;

    const scenarioLayer = L.layerGroup().addTo(map);
    const currentLayer = L.layerGroup();
    const districtLayer = L.layerGroup();
    const overlayLayer = L.layerGroup();
    const selectedLayer = L.layerGroup().addTo(map);
    const status = document.getElementById("p6ScenarioStatus");
    const unitSelect = document.getElementById("p6ScenarioUnit");
    const editToggle = document.getElementById("p6ScenarioEdit");
    const resetBtn = document.getElementById("p6ScenarioReset");
    const saveBtn = document.getElementById("p6ScenarioSave");
    const exportBtn = document.getElementById("p6ScenarioExport");
    const shareBtn = document.getElementById("p6ScenarioShare");
    const undoBtn = document.getElementById("p6ScenarioUndo");
    const redoBtn = document.getElementById("p6ScenarioRedo");
    const districtList = document.getElementById("p6ScenarioDistrictList");
    const selectedName = document.getElementById("p6SelectedDistrict");
    const stats = document.getElementById("p6ScenarioStats");
    const search = document.getElementById("p6DistrictSearch");
    const currentToggle = document.getElementById("p6ShowCurrentBoundaries");
    const scenarioToggle = document.getElementById("p6ShowScenarioBoundaries");
    const overlayToggle = document.getElementById("p6ShowFederalOverlays");
    const districtToggle = document.getElementById("p6ShowDistrictBoundaries");
    const quickCards = [...document.querySelectorAll("[data-p6-view]")];
    const changeStrip = document.getElementById("p6ScenarioChange");

    let scenario = null,
      features = [],
      adm1 = [],
      assignments = new Map(),
      originalAssignments = new Map();
    let selectedDistrict = null,
      editing = false,
      viewMode = "ppri",
      showDistricts = true;
    let undoStack = [],
      redoStack = [];

    const primaryUnits = () =>
      scenario.units.filter((u) => u.type !== "federal-overlay");
    const unitById = (id) => scenario.units.find((u) => u.id === id);
    const unitName = (id) => unitById(id)?.name || "Unassigned";

    function renderUnitSelect() {
      if (!unitSelect) return;
      unitSelect.innerHTML = primaryUnits()
        .map(
          (u) =>
            `<option value="${u.id}">${u.name}${u.type === "federal-territory" ? " — federal territory" : ""}</option>`,
        )
        .join("");
    }

    function snapshot() {
      return new Map(assignments);
    }
    function changed() {
      undoBtn && (undoBtn.disabled = undoStack.length === 0);
      redoBtn && (redoBtn.disabled = redoStack.length === 0);
    }
    function pushChange() {
      undoStack.push(snapshot());
      if (undoStack.length > 30) undoStack.shift();
      redoStack = [];
      changed();
    }
    function applyAssignments(next, label) {
      assignments = new Map(next);
      renderScenarioBoundaries();
      renderDistrictLayer();
      renderDistrictList();
      changed();
      if (changeStrip)
        changeStrip.innerHTML = `<strong>Scenario updated</strong><span>${label || "District assignments changed."}</span>`;
    }

    function renderCurrentLayer() {
      currentLayer.clearLayers();
      const currentFeatures = buildCurrentProvinceFeatures(features);
      currentFeatures.forEach((f) => {
        const meta = f.properties || {};
        const layer = L.geoJSON(f, {
          pane: "ppri-current",
          style: {
            color: meta.__currentProvinceColor || "#1e293b",
            weight: 2.2,
            fillColor: meta.__currentProvinceFill || "#3b82f6",
            fillOpacity: 0.3,
          },
        });
        const badge = meta.__currentProvinceLegal
          ? `<span style="display:inline-block;padding:2px 6px;border-radius:4px;font-size:11px;font-weight:700;background:#dbeafe;color:#1e40af;margin-top:4px;">Legal Province</span>`
          : `<span style="display:inline-block;padding:2px 6px;border-radius:4px;font-size:11px;font-weight:600;background:#f1f5f9;color:#475569;margin-top:4px;">${meta.__currentProvinceType || "Territory"}</span>`;
        layer.bindTooltip(
          `<strong>${meta.__currentProvinceName}</strong><br>${badge}<br><small>${meta.__districtCount || ""} districts</small>`,
          { sticky: true },
        );
        layer.addTo(currentLayer);
      });
      if (currentToggle?.checked || viewMode === "current")
        map.addLayer(currentLayer);
      else map.removeLayer(currentLayer);
    }

    function renderScenarioBoundaries() {
      scenarioLayer.clearLayers();
      overlayLayer.clearLayers();
      const primary = primaryUnits();

      primary.forEach((unit, index) => {
        let unitFeatures = [];
        if (unit.type === "federal-territory") {
          unitFeatures = getUnitFeatures(unit, adm1, features);
        } else if (viewMode === "ppri") {
          // PPRI-01 is constructed from district geometry. This is the
          // authoritative building block for hypothetical boundaries.
          unitFeatures = getUnitFeatures(unit, adm1, features);
        } else {
          unitFeatures = features.filter((f) => assignments.get(f) === unit.id);
        }

        if (!unitFeatures.length) return;

        let geometry = null;
        try {
          geometry =
            unitFeatures.length === 1
              ? unitFeatures[0]
              : turf.union(turf.featureCollection(unitFeatures));
        } catch (error) {
          console.warn("Scenario geometry union failed for", unit.name, error);
          geometry = unitFeatures[0];
        }
        if (!geometry) return;

        const layer = L.geoJSON(geometry, {
          pane: "ppri-scenario",
          style: {
            color: COLORS[index % COLORS.length],
            weight: 2.1,
            fillColor: COLORS[index % COLORS.length],
            fillOpacity: 0.34,
          },
        }).bindTooltip(unit.name, { sticky: true });

        layer.on("click", () => {
          if (unitSelect) unitSelect.value = unit.id;
          if (layer.getBounds().isValid()) {
            map.fitBounds(layer.getBounds(), { padding: [30, 30], maxZoom: 7 });
          }
        });
        layer.addTo(scenarioLayer);
      });

      scenario.units
        .filter((u) => u.type === "federal-overlay")
        .forEach((unit) => {
          const unitFeatures = getUnitFeatures(unit, adm1, features);
          if (!unitFeatures.length) return;
          let geometry = null;
          try {
            geometry =
              unitFeatures.length === 1
                ? unitFeatures[0]
                : turf.union(turf.featureCollection(unitFeatures));
          } catch (error) {
            geometry = unitFeatures[0];
          }
          if (!geometry) return;

          L.geoJSON(geometry, {
            pane: "ppri-scenario",
            style: {
              color: "#111827",
              weight: 2.4,
              dashArray: "7 6",
              fillOpacity: 0.04,
            },
          })
            .bindTooltip(`${unit.name} — federal overlay`, { sticky: true })
            .addTo(overlayLayer);
        });

      if (scenarioToggle?.checked !== false && viewMode !== "current")
        map.addLayer(scenarioLayer);
      else map.removeLayer(scenarioLayer);
      if (overlayToggle?.checked && viewMode !== "current")
        map.addLayer(overlayLayer);
      else map.removeLayer(overlayLayer);

      renderStats();
      renderCoverage();
    }

    function renderStats() {
      if (!stats) return;
      if (viewMode === "current") {
        const provFeatures = buildCurrentProvinceFeatures(features);
        stats.innerHTML = `<div class="p6-scenario-stat-grid">${provFeatures
          .map((f) => {
            const meta = f.properties || {};
            let area = 0;
            try {
              area = turf.area(f) / 1e6;
            } catch (e) {}
            return `<div class="p6-scenario-stat" style="border-top: 3px solid ${meta.__currentProvinceColor || "#cbd5e1"}">
            <strong>${meta.__currentProvinceName}</strong>
            <span>${meta.__currentProvinceLegal ? "Constitutional Legal Province" : meta.__currentProvinceType} · ${meta.__districtCount || 0} districts</span>
            <span>${Math.round(area).toLocaleString()} km² geometry</span>
          </div>`;
          })
          .join("")}</div>`;
        return;
      }
      stats.innerHTML = `<div class="p6-scenario-stat-grid">${primaryUnits()
        .map((u) => {
          const assigned = features.filter((f) => assignments.get(f) === u.id);
          let area = 0;
          const geometryFeatures =
            u.type === "federal-territory"
              ? adm1.filter((f) => matchesAnyRule(f, u.rules))
              : viewMode === "ppri"
                ? features.filter((f) => matchesAnyRule(f, u.rules))
                : assigned;
          geometryFeatures.forEach((f) => {
            try {
              area += turf.area(f) / 1e6;
            } catch (e) {}
          });
          return `<div class="p6-scenario-stat"><strong>${u.name}</strong><span>${u.type === "federal-territory" ? "Federal territory" : `${assigned.length} editable district${assigned.length === 1 ? "" : "s"}`}</span><span>${Math.round(area).toLocaleString()} km² geometry</span></div>`;
        })
        .join("")}</div>`;
    }

    function renderCoverage() {
      const el = document.getElementById("p6ScenarioCoverage");
      if (!el || !scenario) return;
      const primary = primaryUnits();
      const mapped = primary.filter((u) => {
        const fs = unitHasGeometry(u, adm1, features);
        return fs && fs.length;
      });
      const missing = primary.filter((u) => !mapped.includes(u));
      el.className = `p6-coverage p6-coverage-${missing.length ? "warning" : "complete"}`;
      const details = primary
        .map((u) => {
          const fs = unitHasGeometry(u, adm1, features);
          return `${fs && fs.length ? "✓" : "!"} ${u.name} (${fs ? fs.length : 0})`;
        })
        .join(" · ");
      el.innerHTML = `<strong>${mapped.length}/${primary.length} primary units mapped</strong><span>${features.length} editable source districts loaded</span>${missing.length ? `<span class="p6-coverage-missing">Missing geometry: ${missing.map((u) => u.name).join(", ")}</span>` : `<span>All ${primary.length} primary PPRI-01 units have source geometry.</span>`}<details class="p6-coverage-details"><summary>Geographic assignment audit</summary><p>${details}</p></details>`;
    }

    function renderDistrictLayer() {
      districtLayer.clearLayers();
      features.forEach((feature) => {
        const layer = L.geoJSON(feature, {
          style: {
            color: "#475569",
            weight: 0.75,
            fillColor: "#ffffff",
            fillOpacity: 0.01,
          },
        });
        layer.on("click", () => selectDistrict(feature, editing));
        layer.on("mouseover", (e) => {
          e.target.setStyle({ weight: 2, color: "#0f172a" });
        });
        layer.on("mouseout", (e) => {
          e.target.setStyle({ weight: 0.75, color: "#475569" });
        });

        const dName = displayDistrict(feature);
        const divName = displayDivision(feature);
        if (viewMode === "current") {
          const provKey = currentProvinceKey(feature);
          const provMeta = CURRENT_PROVINCE_METADATA[provKey];
          const provName = provMeta?.name || displayProvince(feature);
          layer.bindTooltip(
            `<strong>${dName}</strong><br>${divName ? `${divName} Division · ` : ""}${provName}`,
            { sticky: true },
          );
        } else {
          layer.bindTooltip(
            `<strong>${dName}</strong><br>${divName ? `${divName} Division · ` : ""}${unitName(assignments.get(feature))}`,
            { sticky: true },
          );
        }
        layer.addTo(districtLayer);
      });

      if (showDistricts) {
        map.addLayer(districtLayer);
      } else {
        map.removeLayer(districtLayer);
      }
    }

    function selectDistrict(feature, reassign) {
      selectedDistrict = feature;
      const dName = displayDistrict(feature);
      const divName = displayDivision(feature);
      if (viewMode === "current") {
        const provKey = currentProvinceKey(feature);
        const provMeta = CURRENT_PROVINCE_METADATA[provKey];
        const provName = provMeta?.name || displayProvince(feature);
        if (selectedName)
          selectedName.textContent = `${dName} — ${divName} Division · ${provName}`;
      } else {
        if (selectedName)
          selectedName.textContent = `${dName} — ${divName} Division · ${unitName(assignments.get(feature))}`;
      }
      selectedLayer.clearLayers();
      L.geoJSON(feature, {
        style: { color: "#111827", weight: 3, fillOpacity: 0.14 },
      }).addTo(selectedLayer);
      if (reassign && editing && unitSelect?.value) {
        const target = unitSelect.value;
        const before = unitName(assignments.get(feature));
        if (before !== unitName(target)) {
          pushChange();
          assignments.set(feature, target);
          applyAssignments(
            assignments,
            `${dName} moved from ${before} to ${unitName(target)}.`,
          );
        }
      }
    }

    function renderDistrictList() {
      if (!districtList) return;
      const q = normalize(search?.value || "");
      const rows = features
        .filter(
          (f) =>
            !q ||
            normalize(displayDistrict(f)).includes(q) ||
            normalize(displayDivision(f)).includes(q),
        )
        .slice(0, 300);
      districtList.innerHTML = rows
        .map(
          (f) =>
            `<button type="button" class="p6-district-row${selectedDistrict === f ? " active" : ""}" data-id="${f.properties.__ppriDistrictId}"><span>${displayDistrict(f)}</span><small>${unitName(assignments.get(f))}</small></button>`,
        )
        .join("");
      districtList.querySelectorAll("button").forEach((b) =>
        b.addEventListener("click", () => {
          const f = features.find(
            (x) => x.properties.__ppriDistrictId === b.dataset.id,
          );
          if (f) selectDistrict(f, true);
          renderDistrictList();
        }),
      );
    }

    function setView(mode) {
      viewMode = mode;
      quickCards.forEach((card) =>
        card.classList.toggle("active", card.dataset.p6View === mode),
      );
      if (mode === "current") {
        editing = false;
        if (editToggle) editToggle.checked = false;
        if (currentToggle) currentToggle.checked = true;
        if (scenarioToggle) scenarioToggle.checked = false;
        if (overlayToggle) overlayToggle.checked = false;
        renderCurrentLayer();
        map.addLayer(currentLayer);
        map.removeLayer(scenarioLayer);
        map.removeLayer(overlayLayer);
        status.textContent =
          "Current mode: showing Pakistan's 4 legal provinces and federal/administrative territories with official district boundaries.";
      } else {
        if (scenarioToggle) scenarioToggle.checked = true;
        if (currentToggle) currentToggle.checked = false;
        if (overlayToggle) overlayToggle.checked = mode === "ppri";
        map.removeLayer(currentLayer);
        map.addLayer(scenarioLayer);
        if (overlayToggle?.checked) map.addLayer(overlayLayer);
        else map.removeLayer(overlayLayer);
        editing = mode === "custom";
        if (editToggle) editToggle.checked = editing;
        status.textContent =
          mode === "custom"
            ? "My Scenario: edit mode is on. Select a target unit and click districts to experiment."
            : "PPRI-01: illustrative boundaries loaded from the documented scenario rules.";
      }
      renderDistrictLayer();
      renderScenarioBoundaries();
    }

    function resetScenario() {
      assignments = new Map(originalAssignments);
      undoStack = [];
      redoStack = [];
      localStorage.removeItem("ppri-scenario-ppri-01");
      setView("ppri");
      if (changeStrip)
        changeStrip.innerHTML =
          "<strong>Scenario reset</strong><span>PPRI-01 restored.</span>";
    }

    function saveScenario() {
      const saved = {};
      features.forEach((f) => {
        saved[f.properties.__ppriDistrictId] = assignments.get(f);
      });
      localStorage.setItem("ppri-scenario-ppri-01", JSON.stringify(saved));
      status.textContent = "Your scenario is saved in this browser only.";
    }

    function exportScenario() {
      const payload = {
        scenario: scenario.scenario_id,
        title: scenario.title,
        generated_at: new Date().toISOString(),
        methodology: scenario.note,
        assignments: features.map((f) => ({
          district: displayDistrict(f),
          division: displayDivision(f),
          source_province: displayProvince(f),
          unit: unitName(assignments.get(f)),
        })),
      };
      const a = document.createElement("a");
      a.href = URL.createObjectURL(
        new Blob([JSON.stringify(payload, null, 2)], {
          type: "application/json",
        }),
      );
      a.download = "ppri-scenario.json";
      a.click();
      URL.revokeObjectURL(a.href);
    }

    function shareScenario() {
      const ids = features
        .map(
          (f) => `${f.properties.__ppriDistrictId}=${assignments.get(f) || ""}`,
        )
        .join("~");
      const url = `${location.origin}${location.pathname}?scenario=${encodeURIComponent(btoa(unescape(encodeURIComponent(ids))))}`;
      navigator.clipboard
        ?.writeText(url)
        .then(() => {
          status.textContent =
            "Share link copied. It encodes the district assignments and requires no database.";
        })
        .catch(() => {
          status.textContent = url;
        });
    }

    undoBtn?.addEventListener("click", () => {
      if (!undoStack.length) return;
      redoStack.push(snapshot());
      assignments = undoStack.pop();
      applyAssignments(assignments, "Last change undone.");
    });
    redoBtn?.addEventListener("click", () => {
      if (!redoStack.length) return;
      undoStack.push(snapshot());
      assignments = redoStack.pop();
      applyAssignments(assignments, "Change restored.");
    });
    quickCards.forEach((card) =>
      card.addEventListener("click", () => setView(card.dataset.p6View)),
    );
    currentToggle?.addEventListener("change", () =>
      setView(currentToggle.checked ? "current" : "ppri"),
    );
    scenarioToggle?.addEventListener("change", () => {
      if (scenarioToggle.checked) map.addLayer(scenarioLayer);
      else map.removeLayer(scenarioLayer);
    });
    districtToggle?.addEventListener("change", () => {
      showDistricts = districtToggle.checked;
      if (showDistricts) map.addLayer(districtLayer);
      else map.removeLayer(districtLayer);
    });
    overlayToggle?.addEventListener("change", () =>
      overlayToggle.checked
        ? map.addLayer(overlayLayer)
        : map.removeLayer(overlayLayer),
    );
    editToggle?.addEventListener("change", () => {
      editing = editToggle.checked;
      if (editing) viewMode = "custom";
      quickCards.forEach((card) =>
        card.classList.toggle(
          "active",
          card.dataset.p6View === (editing ? "custom" : "ppri"),
        ),
      );
      renderDistrictLayer();
    });
    resetBtn?.addEventListener("click", resetScenario);
    saveBtn?.addEventListener("click", saveScenario);
    exportBtn?.addEventListener("click", exportScenario);
    shareBtn?.addEventListener("click", shareScenario);
    search?.addEventListener("input", renderDistrictList);

    const setLoading = (message) => {
      if (status) status.textContent = message;
      const coverage = document.getElementById("p6ScenarioCoverage");
      if (coverage) {
        coverage.className = "p6-coverage p6-coverage-loading";
        coverage.innerHTML = `<strong>${message}</strong><span>Loading Pakistan administrative geography…</span>`;
      }
    };
    setLoading("Loading Pakistan administrative geography…");

    // Do not make the whole Scenario Lab depend on one optional geography request.
    // ADM1 + ADM3 + scenario are the required inputs; ADM0 is optional because
    // it is used only for the national mask/initial outline.
    Promise.allSettled([
      fetchJSON(ADM0_URL, "Pakistan outline"),
      fetchJSON(ADM1_URL, "Current provincial boundaries"),
      fetchJSON(ADM3_URL, "District boundaries"),
      fetchJSON(SCENARIO_URL, "PPRI-01 scenario"),
    ])
      .then((results) => {
        const [nationalResult, adm1Result, districtResult, scenarioResult] =
          results;
        const failure = (result) =>
          result.status === "rejected" ? result.reason : null;

        if (scenarioResult.status !== "fulfilled")
          throw failure(scenarioResult);
        if (districtResult.status !== "fulfilled")
          throw failure(districtResult);

        scenario = scenarioResult.value;
        adm1 =
          adm1Result.status === "fulfilled"
            ? adm1Result.value.features || []
            : [];
        features = (districtResult.value.features || []).map((f, i) => {
          f.properties = Object.assign({}, f.properties, {
            __ppriDistrictId: `${i}-${displayDistrict(f)}`,
          });
          return f;
        });
        const national =
          nationalResult.status === "fulfilled"
            ? nationalResult.value
            : { type: "FeatureCollection", features: adm1 };
        assignments = makeDistrictAssignments(adm1, features, scenario);
        originalAssignments = new Map(assignments);

        configurePakistanView(map, national, el);
        addPakistanMaskPane(map, national);
        renderUnitSelect();
        renderCurrentLayer();
        renderScenarioBoundaries();
        renderDistrictLayer();
        renderDistrictList();
        setView("ppri");
        changed();
        status.textContent =
          nationalResult.status === "fulfilled"
            ? "PPRI-01 loaded. Scenario geometry and current administrative boundaries are ready."
            : "PPRI-01 loaded. The optional national outline source was unavailable; administrative geometry is still available.";

        const overlayControls = {
          "PPRI scenario": scenarioLayer,
          "Current provinces": currentLayer,
          "District boundaries": districtLayer,
          "Federal overlays": overlayLayer,
        };
        L.control
          .layers(
            { OpenStreetMap: bases.street, "Light map": bases.light },
            overlayControls,
            { collapsed: false },
          )
          .addTo(map);

        map.on("overlayadd", (e) => {
          if (e.layer === districtLayer && districtToggle)
            districtToggle.checked = true;
          if (e.layer === scenarioLayer && scenarioToggle)
            scenarioToggle.checked = true;
          if (e.layer === currentLayer && currentToggle)
            currentToggle.checked = true;
          if (e.layer === overlayLayer && overlayToggle)
            overlayToggle.checked = true;
        });
        map.on("overlayremove", (e) => {
          if (e.layer === districtLayer && districtToggle)
            districtToggle.checked = false;
          if (e.layer === scenarioLayer && scenarioToggle)
            scenarioToggle.checked = false;
          if (e.layer === currentLayer && currentToggle)
            currentToggle.checked = false;
          if (e.layer === overlayLayer && overlayToggle)
            overlayToggle.checked = false;
        });
      })
      .catch((error) => {
        console.error("PPRI scenario map load failed:", error);
        if (status)
          status.textContent = `Map data could not be loaded: ${error.message || "unknown error"}.`;
        const coverage = document.getElementById("p6ScenarioCoverage");
        if (coverage) {
          coverage.className = "p6-coverage p6-coverage-error";
          coverage.innerHTML = `<strong>Map data failed to load</strong><span>${error.message || "Unknown loading error."}</span><span>Open the browser console for the failed source.</span>`;
        }
      });
  }

  document.addEventListener("DOMContentLoaded", () => {
    initCurrentMap();
    initScenarioMap();
  });
})();
