/**
 * PPRI Data Centre Interactive Module
 * - NFC Divisible Pool Reform Simulator
 * - District & Regional Explorer with Search/Filters/Export
 * - Spatial Access & Distance Observatory
 */
document.addEventListener("DOMContentLoaded", function () {
  "use strict";

  // --- TAB NAVIGATION ---
  const tabBtns = document.querySelectorAll(".dc-tab-btn");
  const tabPanes = document.querySelectorAll(".dc-tab-pane");

  tabBtns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      const targetId = this.getAttribute("data-tab");
      tabBtns.forEach((b) => b.classList.remove("active"));
      tabPanes.forEach((p) => p.classList.remove("active"));
      this.classList.add("active");
      const targetPane = document.getElementById(targetId);
      if (targetPane) targetPane.classList.add("active");
    });
  });

  // --- NFC SIMULATOR ---
  const sliderPop = document.getElementById("nfcWeightPop");
  const sliderPov = document.getElementById("nfcWeightPov");
  const sliderRev = document.getElementById("nfcWeightRev");
  const sliderDen = document.getElementById("nfcWeightDen");
  const poolInput = document.getElementById("nfcPoolAmount");

  const valPop = document.getElementById("valPop");
  const valPov = document.getElementById("valPov");
  const valRev = document.getElementById("valRev");
  const valDen = document.getElementById("valDen");
  const totalWeightBadge = document.getElementById("nfcTotalWeight");

  // Provincial baseline metrics for NFC criteria (Standardized benchmarks)
  // Population (Census 2023 relative provincial shares excluding ICT):
  // Punjab: 53.39%, Sindh: 23.29%, KP: 17.08%, Balochistan: 6.23%
  const provincialCriteria = {
    punjab: { pop: 53.39, pov: 25.0, rev: 35.0, den: 12.0 },
    sindh: { pop: 23.29, pov: 23.0, rev: 55.0, den: 18.0 },
    kp: { pop: 17.08, pov: 28.0, rev: 8.0, den: 15.0 },
    balochistan: { pop: 6.23, pov: 24.0, rev: 2.0, den: 55.0 }
  };

  function updateNfcCalculation() {
    if (!sliderPop || !sliderPov || !sliderRev || !sliderDen) return;

    const wPop = parseFloat(sliderPop.value) || 0;
    const wPov = parseFloat(sliderPov.value) || 0;
    const wRev = parseFloat(sliderRev.value) || 0;
    const wDen = parseFloat(sliderDen.value) || 0;
    const pool = parseFloat(poolInput ? poolInput.value : 5500) || 5500;

    if (valPop) valPop.textContent = wPop.toFixed(1) + "%";
    if (valPov) valPov.textContent = wPov.toFixed(1) + "%";
    if (valRev) valRev.textContent = wRev.toFixed(1) + "%";
    if (valDen) valDen.textContent = wDen.toFixed(1) + "%";

    const totalWeight = wPop + wPov + wRev + wDen;
    if (totalWeightBadge) {
      totalWeightBadge.textContent = "Total Weight: " + totalWeight.toFixed(1) + "%";
      if (Math.abs(totalWeight - 100) < 0.2) {
        totalWeightBadge.className = "nfc-total-weight-badge valid";
      } else {
        totalWeightBadge.className = "nfc-total-weight-badge warning";
        totalWeightBadge.textContent += " (Auto-normalized to 100%)";
      }
    }

    // Normalized weights
    const normFactor = totalWeight > 0 ? 100 / totalWeight : 1;
    const nPop = (wPop * normFactor) / 100;
    const nPov = (wPov * normFactor) / 100;
    const nRev = (wRev * normFactor) / 100;
    const nDen = (wDen * normFactor) / 100;

    // Calculate provincial shares
    const provinces = ["punjab", "sindh", "kp", "balochistan"];
    provinces.forEach(function (p) {
      const c = provincialCriteria[p];
      const sharePct = (c.pop * nPop) + (c.pov * nPov) + (c.rev * nRev) + (c.den * nDen);
      const shareAmount = (sharePct / 100) * pool;

      const pctEl = document.getElementById("nfcShare_" + p);
      const amtEl = document.getElementById("nfcAmt_" + p);
      if (pctEl) pctEl.textContent = sharePct.toFixed(2) + "%";
      if (amtEl) amtEl.textContent = "Rs " + Math.round(shareAmount).toLocaleString("en-US") + " B";
    });
  }

  [sliderPop, sliderPov, sliderRev, sliderDen].forEach(function (slider) {
    if (slider) slider.addEventListener("input", updateNfcCalculation);
  });
  if (poolInput) poolInput.addEventListener("input", updateNfcCalculation);

  // Preset Buttons
  const preset7th = document.getElementById("preset7th");
  const presetEqual = document.getElementById("presetEqual");
  const presetPop = document.getElementById("presetPop");
  const presetNeed = document.getElementById("presetNeed");

  if (preset7th) {
    preset7th.addEventListener("click", function () {
      sliderPop.value = 82.0;
      sliderPov.value = 10.3;
      sliderRev.value = 5.0;
      sliderDen.value = 2.7;
      updateNfcCalculation();
    });
  }
  if (presetEqual) {
    presetEqual.addEventListener("click", function () {
      sliderPop.value = 40.0;
      sliderPov.value = 30.0;
      sliderRev.value = 15.0;
      sliderDen.value = 15.0;
      updateNfcCalculation();
    });
  }
  if (presetPop) {
    presetPop.addEventListener("click", function () {
      sliderPop.value = 100.0;
      sliderPov.value = 0.0;
      sliderRev.value = 0.0;
      sliderDen.value = 0.0;
      updateNfcCalculation();
    });
  }
  if (presetNeed) {
    presetNeed.addEventListener("click", function () {
      sliderPop.value = 50.0;
      sliderPov.value = 35.0;
      sliderRev.value = 5.0;
      sliderDen.value = 10.0;
      updateNfcCalculation();
    });
  }

  // Run initial calculation
  updateNfcCalculation();

  // --- DISTRICT EXPLORER ---
  const districtData = [
    { district: "Lahore", province: "Punjab", division: "Lahore", pop: 13004135, area: 1772, density: 7338.7, capitalDist: "0 km (Provincial Seat)" },
    { district: "Faisalabad", province: "Punjab", division: "Faisalabad", pop: 8838842, area: 5856, density: 1509.4, capitalDist: "135 km (2.5 hrs)" },
    { district: "Rawalpindi", province: "Punjab", division: "Rawalpindi", pop: 5405633, area: 5286, density: 1022.6, capitalDist: "375 km (4.5 hrs)" },
    { district: "Multan", province: "Punjab", division: "Multan", pop: 5362305, area: 3720, density: 1441.5, capitalDist: "340 km (4.0 hrs)" },
    { district: "Bahawalpur", province: "Punjab", division: "Bahawalpur", pop: 4284964, area: 24830, density: 172.6, capitalDist: "430 km (5.5 hrs)" },
    { district: "Dera Ghazi Khan", province: "Punjab", division: "Dera Ghazi Khan", pop: 3393414, area: 11922, density: 284.6, capitalDist: "475 km (6.5 hrs)" },
    { district: "Rajanpur", province: "Punjab", division: "Dera Ghazi Khan", pop: 2381049, area: 12318, density: 193.3, capitalDist: "610 km (8.5 hrs)" },
    { district: "Karachi Central", province: "Sindh", division: "Karachi", pop: 3822325, area: 69, density: 55396.0, capitalDist: "0 km (Provincial Seat)" },
    { district: "Karachi East", province: "Sindh", division: "Karachi", pop: 3950031, area: 165, density: 23939.6, capitalDist: "0 km (Provincial Seat)" },
    { district: "Hyderabad", province: "Sindh", division: "Hyderabad", pop: 2432540, area: 993, density: 2449.7, capitalDist: "160 km (2.5 hrs)" },
    { district: "Sukkur", province: "Sindh", division: "Sukkur", pop: 1639897, area: 5165, density: 317.5, capitalDist: "485 km (6.0 hrs)" },
    { district: "Larkana", province: "Sindh", division: "Larkana", pop: 1784453, area: 1948, density: 916.0, capitalDist: "450 km (5.5 hrs)" },
    { district: "Tharparkar", province: "Sindh", division: "Mirpur Khas", pop: 1778407, area: 19638, density: 90.6, capitalDist: "410 km (6.5 hrs)" },
    { district: "Peshawar", province: "Khyber Pakhtunkhwa", division: "Peshawar", pop: 4758762, area: 1257, density: 3785.8, capitalDist: "0 km (Provincial Seat)" },
    { district: "Mardan", province: "Khyber Pakhtunkhwa", division: "Mardan", pop: 2743890, area: 1632, density: 1681.3, capitalDist: "65 km (1.0 hr)" },
    { district: "Swat", province: "Khyber Pakhtunkhwa", division: "Malakand", pop: 2687384, area: 5337, density: 503.5, capitalDist: "160 km (2.8 hrs)" },
    { district: "Abbottabad", province: "Khyber Pakhtunkhwa", division: "Hazara", pop: 1419072, area: 1967, density: 721.4, capitalDist: "205 km (3.2 hrs)" },
    { district: "Dera Ismail Khan", province: "Khyber Pakhtunkhwa", division: "Dera Ismail Khan", pop: 1829098, area: 7326, density: 249.7, capitalDist: "320 km (4.5 hrs)" },
    { district: "Quetta", province: "Balochistan", division: "Quetta", pop: 2595491, area: 2653, density: 978.3, capitalDist: "0 km (Provincial Seat)" },
    { district: "Kech (Turbat)", province: "Balochistan", division: "Makran", pop: 1060931, area: 22539, density: 47.1, capitalDist: "760 km (11.0 hrs)" },
    { district: "Gwadar", province: "Balochistan", division: "Makran", pop: 305160, area: 12637, density: 24.1, capitalDist: "910 km (13.5 hrs)" },
    { district: "Khuzdar", province: "Balochistan", division: "Kalat", pop: 996328, area: 35380, density: 28.2, capitalDist: "300 km (4.5 hrs)" },
    { district: "Zhob", province: "Balochistan", division: "Zhob", pop: 355694, area: 20297, density: 17.5, capitalDist: "330 km (5.0 hrs)" },
    { district: "Islamabad", province: "ICT", division: "Federal Capital", pop: 2363863, area: 906, density: 2609.1, capitalDist: "Federal Seat" }
  ];

  const searchInput = document.getElementById("districtSearchInput");
  const provinceFilter = document.getElementById("districtProvinceFilter");
  const popFilter = document.getElementById("districtPopFilter");
  const districtTbody = document.getElementById("districtTbody");
  const districtCountEl = document.getElementById("districtCount");
  const exportCsvBtn = document.getElementById("btnExportDistrictCsv");
  const exportJsonBtn = document.getElementById("btnExportDistrictJson");

  let currentFilteredDistricts = districtData;

  function renderDistricts() {
    if (!districtTbody) return;
    const query = (searchInput ? searchInput.value : "").trim().toLowerCase();
    const prov = provinceFilter ? provinceFilter.value : "all";
    const popTier = popFilter ? popFilter.value : "all";

    currentFilteredDistricts = districtData.filter(function (d) {
      const matchesSearch =
        d.district.toLowerCase().includes(query) ||
        d.division.toLowerCase().includes(query) ||
        d.province.toLowerCase().includes(query);
      const matchesProv = prov === "all" || d.province === prov;
      const matchesPop =
        popTier === "all" ||
        (popTier === "small" && d.pop < 1000000) ||
        (popTier === "medium" && d.pop >= 1000000 && d.pop <= 3000000) ||
        (popTier === "large" && d.pop > 3000000);
      return matchesSearch && matchesProv && matchesPop;
    });

    if (districtCountEl) {
      districtCountEl.textContent = `Showing ${currentFilteredDistricts.length} of ${districtData.length} baseline units`;
    }

    if (currentFilteredDistricts.length === 0) {
      districtTbody.innerHTML = `<tr><td colspan="7" style="text-align:center; padding: 24px; color: #64748b;">No administrative units found matching your search.</td></tr>`;
      return;
    }

    districtTbody.innerHTML = currentFilteredDistricts
      .map(function (d) {
        return `<tr>
          <td style="font-weight: 700; color: #073c3a;">${d.district}</td>
          <td><span class="badge" style="background: #e2e8f0; font-size: 0.78rem; padding: 3px 8px; border-radius: 4px;">${d.province}</span></td>
          <td>${d.division}</td>
          <td style="text-align: right; font-variant-numeric: tabular-nums;">${d.pop.toLocaleString("en-US")}</td>
          <td style="text-align: right; font-variant-numeric: tabular-nums;">${d.area.toLocaleString("en-US")}</td>
          <td style="text-align: right; font-variant-numeric: tabular-nums;">${d.density.toFixed(1)}</td>
          <td style="color: #64748b; font-size: 0.82rem;">${d.capitalDist}</td>
        </tr>`;
      })
      .join("");
  }

  if (searchInput) searchInput.addEventListener("input", renderDistricts);
  if (provinceFilter) provinceFilter.addEventListener("change", renderDistricts);
  if (popFilter) popFilter.addEventListener("change", renderDistricts);

  // CSV Export
  if (exportCsvBtn) {
    exportCsvBtn.addEventListener("click", function () {
      const exportList = currentFilteredDistricts.length > 0 ? currentFilteredDistricts : districtData;
      const headers = ["District", "Province", "Division", "Population_2023", "Area_km2", "Density_per_km2", "Distance_to_Capital"];
      const rows = exportList.map((d) => [
        `"${d.district}"`,
        `"${d.province}"`,
        `"${d.division}"`,
        d.pop,
        d.area,
        d.density,
        `"${d.capitalDist}"`
      ]);
      const csvContent = [headers.join(","), ...rows.map((r) => r.join(","))].join("\n");
      const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "ppri_district_baseline_2023.csv";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });
  }

  // JSON Export
  if (exportJsonBtn) {
    exportJsonBtn.addEventListener("click", function () {
      const exportList = currentFilteredDistricts.length > 0 ? currentFilteredDistricts : districtData;
      const jsonContent = JSON.stringify({ dataset: "PPRI District & Administrative Baseline", source: "PBS Census 2023", count: exportList.length, data: exportList }, null, 2);
      const blob = new Blob([jsonContent], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "ppri_district_baseline_2023.json";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });
  }

  // --- INTERACTIVE DATA OBSERVATORY KNOWLEDGE MAP ---
  function initKnowledgeMap() {
    const kmapContainer = document.getElementById("kmapInteractiveNodes");
    if (!kmapContainer) return;

    const domains = [
      {
        id: "population",
        title: "Population & Cities",
        icon: "👥",
        badge: "Census 2023",
        metric: "241.49M",
        metricSub: "National Population (+2.55%/yr)",
        url: "/data/population/",
        topics: ["National Population (241.5M)", "Provincial Breakdown", "Urban vs Rural (38.8%)", "Sex Ratio (106M:100F)", "Household Size (6.3)", "Top 22 Cities (Karachi, Lahore)"],
        researchTitle: "Four Provinces, 241M People: Administrative Scale",
        researchUrl: "/articles/four-provinces-241-million-people-administrative-scale.html",
        keywords: ["population", "census", "karachi", "lahore", "faisalabad", "demographics", "urban", "rural", "gender", "growth", "cities", "household", "languages"]
      },
      {
        id: "economy",
        title: "Economy & Inflation",
        icon: "📈",
        badge: "PBS / SBP / PES",
        metric: "10.26%",
        metricSub: "National CPI YoY Inflation",
        url: "/data/economy/",
        topics: ["CPI Inflation (10.26%)", "SPI Weekly (8.4%)", "Real GDP Growth (3.7%)", "GDP Per Capita ($1,680)", "LSM Output (+10.37%)", "IT Exports ($3.39B)"],
        researchTitle: "Income Went Up. So Why Does Life Feel Harder?",
        researchUrl: "/research/reports/income-went-up-why-does-life-feel-harder.html",
        keywords: ["economy", "inflation", "cpi", "spi", "food prices", "gdp", "growth", "prices", "remittances", "trade", "wages", "lsm", "dollar", "rupee", "petrol"]
      },
      {
        id: "living-standards",
        title: "Living Standards & Income",
        icon: "🏠",
        badge: "HIES 2024–25",
        metric: "PKR 63,450",
        metricSub: "Mean Monthly Household Income",
        url: "/data/living-standards/",
        topics: ["Monthly Income Quintiles", "Household Consumption", "Drinking Water (97%)", "Sanitation (74%)", "Electricity (95%)", "Clean Fuel (38%)"],
        researchTitle: "Same Country, Different Life: Spatial Inequality",
        researchUrl: "/research/reports/same-country-different-life-district-access.html",
        keywords: ["living standards", "income", "household", "hies", "consumption", "poverty", "water", "sanitation", "electricity", "energy", "welfare", "wages"]
      },
      {
        id: "public-finance",
        title: "Public Finance & NFC",
        icon: "⚖️",
        badge: "Finance Division",
        metric: "Rs 5.5T+",
        metricSub: "Federal Divisible Pool Size",
        url: "/data/public-finance/",
        topics: ["7th NFC Formula Weights", "Provincial Divisible Shares", "Total Public Debt (Rs 83.3T)", "Debt Maturity (3.86 Yrs)", "Education Outlay (Rs 962B)"],
        researchTitle: "Does Money Work Better Spent Closer to the People?",
        researchUrl: "/research/reports/does-money-work-better-spent-closer-to-people.html",
        keywords: ["public finance", "nfc", "divisible pool", "budget", "debt", "tax", "fbr", "revenue", "transfers", "fiscal", "spending", "provinces"]
      },
      {
        id: "education",
        title: "Education & Literacy",
        icon: "🎓",
        badge: "PBS / AEPAM",
        metric: "61.0%",
        metricSub: "National Literacy Rate (10+ Yrs)",
        url: "/data/education/",
        topics: ["Literacy Rate (61%)", "Gender Gap (71% M / 50% F)", "Out-of-School Children (26.2M)", "Primary Completion (70%)", "Secondary Completion (30%)"],
        researchTitle: "The 26 Million Out-of-School Children Crisis",
        researchUrl: "/research/reports/same-country-different-life-district-access.html",
        keywords: ["education", "literacy", "schools", "out of school", "completion", "gender gap", "parity", "children", "attendance", "teachers"]
      },
      {
        id: "health",
        title: "Public Health",
        icon: "🏥",
        badge: "PDHS / PBS",
        metric: "73.0%",
        metricSub: "Child Immunization Coverage",
        url: "/data/health/",
        topics: ["Child Immunization (73%)", "Fertility Rate (3.6 Births)", "Prenatal Consultation (88%)", "Contraceptive Use (38%)", "Health Decision Autonomy (56%)"],
        researchTitle: "How Far Is Government? Health Administrative Distance",
        researchUrl: "/articles/how-far-is-government-administrative-distance.html",
        keywords: ["health", "immunization", "vaccine", "fertility", "prenatal", "maternal", "hospital", "contraceptive", "doctors", "clinics"]
      },
      {
        id: "digital-access",
        title: "Digital Access & Tech",
        icon: "🌐",
        badge: "HIES / PTA",
        metric: "95.0%",
        metricSub: "Household Mobile Ownership",
        url: "/data/digital-access/",
        topics: ["Mobile Access (95%)", "Individual Gender Gap (69% M / 39% F)", "Broadband Access (34%)", "Internet Users (57%)", "Computer Access (14%)"],
        researchTitle: "The Price of a Simple Task: Digital Governance",
        researchUrl: "/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html",
        keywords: ["digital", "internet", "broadband", "mobile", "smartphone", "telecom", "gender gap", "technology", "it exports", "computer"]
      },
      {
        id: "compare",
        title: "Provinces Comparator",
        icon: "📊",
        badge: "Multi-Domain",
        metric: "5 Units",
        metricSub: "Punjab, Sindh, KP, Balochistan, ICT",
        url: "/data/compare/",
        topics: ["Population Shares", "Territorial Land Area", "Population Density", "Urbanization Rates", "Provincial Income Levels", "NFC Divisible Shares"],
        researchTitle: "The Provincial Reorganization of Pakistan",
        researchUrl: "/research/policy-papers/provincial-reorganization-of-pakistan.html",
        keywords: ["compare", "provinces", "punjab", "sindh", "kp", "balochistan", "ict", "islamabad", "subnational", "regions", "density", "area"]
      }
    ];

    const container = kmapContainer;
    const svgCanvas = document.getElementById("kmapSvgCanvas");
    const inspectorEl = document.getElementById("kmapInspector");
    const searchInput = document.getElementById("kmapSearchInput");
    const quickChips = document.querySelectorAll(".kmap-quick-chip");
    const viewGraphBtn = document.getElementById("btnViewGraph");
    const viewGridBtn = document.getElementById("btnViewGrid");
    const graphStage = document.getElementById("kmapStage");
    const gridStage = document.getElementById("kmapGridStage");

    function positionNodes() {
      const rect = container.getBoundingClientRect();
      const cx = rect.width / 2;
      const cy = rect.height / 2;
      const rx = Math.min(cx - 95, 230);
      const ry = Math.min(cy - 50, 180);

      let svgLines = "";

      domains.forEach((d, i) => {
        const angle = (i * 2 * Math.PI / domains.length) - (Math.PI / 2);
        const x = cx + rx * Math.cos(angle);
        const y = cy + ry * Math.sin(angle);

        let node = document.getElementById("kmap-node-" + d.id);
        if (!node) {
          node = document.createElement("a");
          node.id = "kmap-node-" + d.id;
          node.href = d.url;
          node.className = "kmap-node";
          node.setAttribute("data-domain", d.id);
          node.innerHTML = `
            <span class="kmap-node-icon">${d.icon}</span>
            <div class="kmap-node-text">
              <strong>${d.title}</strong>
              <span>${d.metric}</span>
            </div>
          `;
          container.appendChild(node);

          node.addEventListener("click", function (e) {
            e.preventDefault();
            selectDomain(d.id);
          });

          node.addEventListener("mouseenter", function () {
            selectDomain(d.id, false);
          });
        }

        node.style.left = x + "px";
        node.style.top = y + "px";

        svgLines += `<line x1="${cx}" y1="${cy}" x2="${x}" y2="${y}" stroke="rgba(94, 234, 212, 0.35)" stroke-width="1.5" stroke-dasharray="4,4" />`;
      });

      if (svgCanvas) {
        svgCanvas.innerHTML = svgLines;
      }
    }

    function selectDomain(domainId, scrollToInspector) {
      const d = domains.find(item => item.id === domainId);
      if (!d || !inspectorEl) return;

      document.querySelectorAll(".kmap-node").forEach(n => {
        n.classList.toggle("active", n.getAttribute("data-domain") === domainId);
      });

      const topicChips = d.topics.map(t => `<span class="kmap-insp-chip">${t}</span>`).join("");

      inspectorEl.innerHTML = `
        <div class="kmap-insp-header">
          <div class="kmap-insp-icon">${d.icon}</div>
          <div>
            <h3 class="kmap-insp-title">${d.title}</h3>
            <span class="kmap-insp-badge">&check; ${d.badge} Verified</span>
          </div>
        </div>

        <div class="kmap-insp-stat-box">
          <div class="kmap-insp-stat-val">${d.metric}</div>
          <div class="kmap-insp-stat-sub">${d.metricSub}</div>
        </div>

        <div class="kmap-insp-topics">
          <div class="kmap-insp-topics-label">Verified Topics &amp; Indicators:</div>
          <div class="kmap-insp-chips">
            ${topicChips}
          </div>
        </div>

        <div class="kmap-insp-research">
          <strong>Related Policy Analysis:</strong>
          <a href="${d.researchUrl}">${d.researchTitle} &rarr;</a>
        </div>

        <div class="kmap-insp-actions">
          <a href="${d.url}" class="obs-btn obs-btn-primary" style="justify-content:center; text-align:center;">
            Open ${d.title} Hub &rarr;
          </a>
          <a href="/data/downloads/" class="obs-btn obs-btn-outline" style="justify-content:center; text-align:center; font-size:0.82rem;">
            &darr; Download Domain CSV
          </a>
        </div>
      `;
    }

    function filterNodes(q) {
      q = q.toLowerCase().trim();
      let firstMatch = null;

      domains.forEach(d => {
        const node = document.getElementById("kmap-node-" + d.id);
        if (!node) return;

        const isMatch = !q ||
          d.title.toLowerCase().includes(q) ||
          d.metric.toLowerCase().includes(q) ||
          d.topics.some(t => t.toLowerCase().includes(q)) ||
          d.keywords.some(k => k.toLowerCase().includes(q));

        if (isMatch) {
          node.classList.remove("dimmed");
          if (q) {
            node.classList.add("highlight");
            if (!firstMatch) firstMatch = d.id;
          } else {
            node.classList.remove("highlight");
          }
        } else {
          node.classList.add("dimmed");
          node.classList.remove("highlight");
        }
      });

      if (firstMatch) {
        selectDomain(firstMatch, false);
      } else if (!q) {
        selectDomain("population", false);
      }
    }

    if (searchInput) {
      searchInput.addEventListener("input", function () {
        filterNodes(this.value);
      });
    }

    quickChips.forEach(chip => {
      chip.addEventListener("click", function () {
        const query = this.getAttribute("data-query");
        if (searchInput) {
          searchInput.value = query;
          filterNodes(query);
        }
      });
    });

    if (viewGraphBtn && viewGridBtn && graphStage && gridStage) {
      viewGraphBtn.addEventListener("click", function () {
        viewGraphBtn.classList.add("active");
        viewGridBtn.classList.remove("active");
        graphStage.style.display = "grid";
        gridStage.style.display = "none";
        positionNodes();
      });

      viewGridBtn.addEventListener("click", function () {
        viewGridBtn.classList.add("active");
        viewGraphBtn.classList.remove("active");
        graphStage.style.display = "none";
        gridStage.style.display = "grid";
      });
    }

    positionNodes();
    selectDomain("population", false);
    window.addEventListener("resize", positionNodes);
  }

  renderDistricts();
  initKnowledgeMap();
});
