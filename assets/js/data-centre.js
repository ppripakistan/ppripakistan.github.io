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

  // --- INTERACTIVE DATA OBSERVATORY ATLAS ---
  function initDataAtlas() {
    const atlasMenu = document.getElementById("atlasMenu");
    const atlasStage = document.getElementById("atlasStage");
    if (!atlasMenu || !atlasStage) return;

    const domains = [
      {
        id: "population",
        title: "Population & Cities",
        icon: "👥",
        badge: "Census 2023",
        metric: "241.49M",
        metricSub: "National Population (+2.55%/yr)",
        url: "/data/population/",
        csvUrl: "/data/downloads/pakistan-population-census-2023.csv",
        chartTitle: "Provincial Population Breakdown (Census 2023 Millions)",
        chartData: [
          { label: "Punjab", value: 127.69, formattedValue: "127.7M (52.9%)", color: "#073c3a" },
          { label: "Sindh", value: 55.70, formattedValue: "55.7M (23.1%)", color: "#0f766e" },
          { label: "KP", value: 40.86, formattedValue: "40.9M (16.9%)", color: "#0284c7" },
          { label: "Balochistan", value: 14.89, formattedValue: "14.9M (6.2%)", color: "#d97706" },
          { label: "ICT", value: 2.36, formattedValue: "2.4M (1.0%)", color: "#64748b" }
        ],
        topics: ["National Census Population (241.5M)", "Intercensal Growth (+2.55%/yr)", "Urban vs Rural Distribution (38.8%)", "Household Size (6.30)", "Sex Ratio (106M:100F)", "Top 22 Urban Centers (Karachi 20.4M, Lahore 13.0M)"],
        researchTitle: "Four Provinces, 241M People: Has Pakistan Outgrown Its Administrative Structure?",
        researchUrl: "/articles/four-provinces-241-million-people-administrative-scale.html",
        keywords: ["population", "census", "karachi", "lahore", "faisalabad", "demographics", "urban", "rural", "gender", "growth", "cities", "household", "languages"]
      },
      {
        id: "economy",
        title: "Economy & Inflation",
        icon: "📈",
        badge: "PBS / SBP / PES",
        metric: "10.26%",
        metricSub: "National CPI YoY Inflation Benchmark",
        url: "/data/economy/",
        csvUrl: "/data/downloads/pakistan-economic-benchmarks-2026.csv",
        chartTitle: "Sectoral GDP Contributions & Economic Growth Rates (%)",
        chartData: [
          { label: "Services", value: 4.09, formattedValue: "4.09%", color: "#073c3a" },
          { label: "Industry", value: 3.51, formattedValue: "3.51%", color: "#0f766e" },
          { label: "Agriculture", value: 2.89, formattedValue: "2.89%", color: "#0284c7" },
          { label: "Overall GDP", value: 3.70, formattedValue: "3.70%", color: "#d97706" },
          { label: "LSM Growth", value: 10.37, formattedValue: "10.37%", color: "#16a34a" }
        ],
        topics: ["CPI Inflation (10.26%)", "SPI Weekly Food Index (8.4%)", "Real GDP Growth (3.70%)", "GDP Per Capita ($1,680)", "LSM Industrial Output (+10.37%)", "Software & IT Exports ($3.39B)", "Mean Monthly Wage (Rs 39,042)"],
        researchTitle: "Income Went Up. So Why Does Life Feel Harder? Analyzing Inflation & Real Wages",
        researchUrl: "/research/reports/income-went-up-why-does-life-feel-harder.html",
        keywords: ["economy", "inflation", "cpi", "spi", "food prices", "gdp", "growth", "prices", "remittances", "trade", "wages", "lsm", "dollar", "rupee", "petrol"]
      },
      {
        id: "living-standards",
        title: "Living Standards & Income",
        icon: "🏠",
        badge: "HIES 2024–25",
        metric: "PKR 82,179",
        metricSub: "Mean Monthly Household Income (PBS)",
        url: "/data/living-standards/",
        csvUrl: "/data/downloads/pakistan-household-income-consumption-hies-2024-25.csv",
        chartTitle: "Average Monthly Household Income by Consumption Quintile (HIES 2024–25 PKR)",
        chartData: [
          { label: "Q1 (Lowest consumption)", value: 41851, formattedValue: "Rs 41,851", color: "#d97706" },
          { label: "Q2", value: 55138, formattedValue: "Rs 55,138", color: "#0284c7" },
          { label: "Q3", value: 65741, formattedValue: "Rs 65,741", color: "#0f766e" },
          { label: "Q4", value: 80387, formattedValue: "Rs 80,387", color: "#073c3a" },
          { label: "Q5 (Highest consumption)", value: 139317, formattedValue: "Rs 139,317", color: "#16a34a" }
        ],
        topics: ["Monthly Household Income (Rs 82,179)", "Monthly Consumption Spending (Rs 79,150)", "Income Quintile Disparities", "Improved drinking-water source (97%; not a water-safety test)", "Flush toilet use (89%; 98% urban / 82% rural)", "Electricity or solar lighting (96%)", "Clean fuels for cooking, lighting and heating (38%)"],
        researchTitle: "Same Country, Different Life: Spatial Inequality Across Pakistan's Districts",
        researchUrl: "/research/reports/same-country-different-life-district-access.html",
        keywords: ["living standards", "income", "household", "hies", "consumption", "poverty", "water", "sanitation", "electricity", "energy", "welfare", "wages"]
      },
      {
        id: "public-finance",
        title: "Public Finance & NFC",
        icon: "⚖️",
        badge: "Finance Division",
        metric: "Rs 5.5T+",
        metricSub: "Federal Divisible Pool Baseline",
        url: "/data/public-finance/",
        csvUrl: "/data/downloads/province_baseline_2023.csv",
        chartTitle: "7th NFC Award Divisible Pool Formula Weights (%)",
        chartData: [
          { label: "Population", value: 82.0, formattedValue: "82.0%", color: "#073c3a" },
          { label: "Poverty", value: 10.3, formattedValue: "10.3%", color: "#0f766e" },
          { label: "Revenue Collection", value: 5.0, formattedValue: "5.0%", color: "#0284c7" },
          { label: "Inverse Density", value: 2.7, formattedValue: "2.7%", color: "#d97706" }
        ],
        topics: ["7th NFC Formula Distribution Weights", "Provincial Divisible Pool Shares", "Total Public Debt (Rs 83.3T)", "Domestic Debt Time to Maturity (3.86 Yrs)", "Public Education & Health Outlays (Rs 962B)"],
        researchTitle: "Does Money Work Better When Spent Closer to the People? Fiscal Decentralization",
        researchUrl: "/research/reports/does-money-work-better-spent-closer-to-people.html",
        keywords: ["public finance", "nfc", "divisible pool", "budget", "debt", "tax", "fbr", "revenue", "transfers", "fiscal", "spending", "provinces"]
      },
      {
        id: "education",
        title: "Education & Literacy",
        icon: "🎓",
        badge: "PBS HIES 2024–25",
        metric: "63%",
        metricSub: "Literacy rate, population age 10+",
        url: "/data/education/",
        csvUrl: "/data/downloads/pakistan-education-literacy-hies-2024-25.csv",
        chartTitle: "Provincial Literacy Rates (Age 10+, HIES 2024–25)",
        chartData: [
          { label: "Punjab", value: 68, formattedValue: "68%", color: "#073c3a" },
          { label: "Sindh", value: 58, formattedValue: "58%", color: "#0f766e" },
          { label: "KP", value: 58, formattedValue: "58%", color: "#0284c7" },
          { label: "Balochistan", value: 49, formattedValue: "49%", color: "#d97706" },
          { label: "National Total", value: 63, formattedValue: "63%", color: "#16a34a" }
        ],
        topics: ["Literacy rate age 10+ (63%)", "Literacy gap (73% male / 54% female)", "Out-of-school rate ages 5–16 (28%)", "Youth literacy ages 15–24 (77%)", "Out-of-school rate in Balochistan (45%)"],
        researchTitle: "Out-of-School Children in Pakistan: Spatial District Analysis",
        researchUrl: "/research/reports/same-country-different-life-district-access.html",
        keywords: ["education", "literacy", "schools", "out of school", "completion", "gender gap", "parity", "children", "attendance", "teachers"]
      },
      {
        id: "health",
        title: "Public Health",
        icon: "🏥",
        badge: "PDHS / PBS",
        metric: "73.0%",
        metricSub: "Child Immunization Coverage Rate",
        url: "/data/health/",
        csvUrl: "/data/downloads/pakistan-economic-benchmarks-2026.csv",
        chartTitle: "Core Public Health Coverage Benchmarks (%)",
        chartData: [
          { label: "Prenatal Care", value: 88.0, formattedValue: "88.0%", color: "#073c3a" },
          { label: "Child Vaccines", value: 73.0, formattedValue: "73.0%", color: "#0f766e" },
          { label: "Female Autonomy", value: 56.0, formattedValue: "56.0%", color: "#0284c7" },
          { label: "Contraceptive Use", value: 38.0, formattedValue: "38.0%", color: "#d97706" }
        ],
        topics: ["Child Immunization Coverage (73%)", "Total Fertility Rate (3.6 Births/Woman)", "Skilled Prenatal Consultation (88%)", "Contraceptive Prevalence (38%)", "Female Health Autonomy (56%)"],
        researchTitle: "How Far Is Government? The Hidden Cost of Administrative Distance for Healthcare",
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
        csvUrl: "/data/downloads/pakistan-digital-access-hies-2024-25.csv",
        chartTitle: "Household & Individual Mobile / Internet Access (%)",
        chartData: [
          { label: "HH Mobile", value: 95.0, formattedValue: "95.0%", color: "#073c3a" },
          { label: "Internet Users", value: 57.0, formattedValue: "57.0%", color: "#0f766e" },
          { label: "Male Mobile", value: 69.0, formattedValue: "69.0%", color: "#0284c7" },
          { label: "Female Mobile", value: 39.0, formattedValue: "39.0%", color: "#d97706" },
          { label: "Broadband", value: 34.0, formattedValue: "34.0%", color: "#16a34a" }
        ],
        topics: ["Household Mobile Ownership (95%)", "Individual Gender Gap (69% Male / 39% Female)", "Household Broadband Access (34%)", "Internet Penetration (57%)", "Software & IT Exports ($3.39B)"],
        researchTitle: "The Price of a Simple Task: Bureaucratic Friction & Digital Governance",
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
        csvUrl: "/data/downloads/pakistan-provinces-census-2023.csv",
        chartTitle: "Territorial Land Area (Thousand km²)",
        chartData: [
          { label: "Balochistan", value: 347.19, formattedValue: "347K km² (43.6%)", color: "#d97706" },
          { label: "Punjab", value: 205.34, formattedValue: "205K km² (25.8%)", color: "#073c3a" },
          { label: "Sindh", value: 140.91, formattedValue: "141K km² (17.7%)", color: "#0f766e" },
          { label: "KP", value: 101.74, formattedValue: "102K km² (12.8%)", color: "#0284c7" },
          { label: "Islamabad", value: 0.91, formattedValue: "0.9K km² (0.1%)", color: "#64748b" }
        ],
        topics: ["Census 2023 Population Distribution", "Territorial Land Area Shares", "Population Density per km²", "Urbanization Rates", "Mean Household Incomes", "7th NFC Divisible Pool Shares"],
        researchTitle: "The Provincial Reorganization of Pakistan: Flagship Institutional Proposal",
        researchUrl: "/research/policy-papers/provincial-reorganization-of-pakistan.html",
        keywords: ["compare", "provinces", "punjab", "sindh", "kp", "balochistan", "ict", "islamabad", "subnational", "regions", "density", "area"]
      }
    ];

    // Render Atlas Menu Items
    atlasMenu.innerHTML = domains.map(d => `
      <div class="atlas-item${d.id === 'population' ? ' active' : ''}" data-domain="${d.id}" role="button" tabindex="0">
        <div class="atlas-item-left">
          <div class="atlas-item-icon">${d.icon}</div>
          <div class="atlas-item-info">
            <h4 class="atlas-item-title">${d.title}</h4>
            <div class="atlas-item-sub">${d.metricSub}</div>
          </div>
        </div>
        <span class="atlas-item-badge">${d.metric}</span>
      </div>
    `).join("");

    function selectAtlasDomain(domainId) {
      const d = domains.find(item => item.id === domainId);
      if (!d) return;

      document.querySelectorAll(".atlas-item").forEach(item => {
        item.classList.toggle("active", item.getAttribute("data-domain") === domainId);
      });

      const topicPills = d.topics.map(t => `<div class="atlas-topic-pill">${t}</div>`).join("");

      atlasStage.innerHTML = `
        <div class="atlas-stage-header">
          <div class="atlas-stage-title-wrap">
            <div class="atlas-stage-icon">${d.icon}</div>
            <div>
              <h3 class="atlas-stage-title">${d.title}</h3>
              <span class="obs-badge obs-badge-official">&check; ${d.badge} Verified</span>
            </div>
          </div>
          <div class="atlas-headline-box">
            <div class="atlas-headline-val">${d.metric}</div>
            <div class="atlas-headline-sub">${d.metricSub}</div>
          </div>
        </div>

        <div class="atlas-chart-card">
          <div class="atlas-chart-header">
            <h4 class="atlas-chart-title">${d.chartTitle}</h4>
            <span class="obs-badge obs-badge-census">&bull; Interactive Preview</span>
          </div>
          <div class="obs-chart-wrapper" id="atlasMiniChart"></div>
        </div>

        <div class="atlas-topics-wrap">
          <div class="atlas-topics-label">Verified Topics &amp; Indicators Tracked:</div>
          <div class="atlas-topics-grid">
            ${topicPills}
          </div>
        </div>

        <div class="atlas-policy-card">
          <div class="atlas-policy-left">
            <strong>Context &amp; Policy Analysis:</strong>
            <a href="${d.researchUrl}">${d.researchTitle} &rarr;</a>
          </div>
          <a href="${d.researchUrl}" class="obs-btn obs-btn-outline" style="font-size:0.82rem;padding:6px 14px;">Read Analysis &rarr;</a>
        </div>

        <div class="atlas-actions-bar">
          <a href="${d.url}" class="obs-btn obs-btn-primary" style="padding:10px 22px; font-size:0.95rem;">
            Explore Full ${d.title} Hub &rarr;
          </a>
          <a href="${d.csvUrl}" class="obs-btn obs-btn-outline" download>
            &darr; Download Domain CSV
          </a>
          <a href="/data/quick-facts/" class="obs-btn obs-btn-outline">
            ★ CSS Fast Facts
          </a>
        </div>
      `;

      // Render interactive chart into the mini chart container
      if (typeof PPRIObservatory !== "undefined" && PPRIObservatory.renderBarChart) {
        PPRIObservatory.renderBarChart("#atlasMiniChart", d.chartData, {
          title: d.chartTitle,
          height: 260
        });
      }
    }

    // Attach click listeners to menu items
    document.querySelectorAll(".atlas-item").forEach(item => {
      item.addEventListener("click", function () {
        selectAtlasDomain(this.getAttribute("data-domain"));
      });
      item.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          selectAtlasDomain(this.getAttribute("data-domain"));
        }
      });
    });

    // Initial render with first domain
    selectAtlasDomain("population");

    // Command Search in Hero
    const heroInput = document.getElementById("heroCommandInput");
    const heroChips = document.querySelectorAll(".dc-command-chip");

    function executeSearch(query) {
      query = (query || "").toLowerCase().trim();
      let firstMatch = null;

      domains.forEach(d => {
        const item = document.querySelector(`.atlas-item[data-domain="${d.id}"]`);
        if (!item) return;

        const isMatch = !query ||
          d.title.toLowerCase().includes(query) ||
          d.metric.toLowerCase().includes(query) ||
          d.topics.some(t => t.toLowerCase().includes(query)) ||
          d.keywords.some(k => k.toLowerCase().includes(query));

        if (isMatch) {
          item.style.display = "flex";
          if (query) {
            item.classList.add("highlight");
            if (!firstMatch) firstMatch = d.id;
          } else {
            item.classList.remove("highlight");
          }
        } else {
          item.style.display = "none";
          item.classList.remove("highlight");
        }
      });

      if (firstMatch) {
        selectAtlasDomain(firstMatch);
      } else if (!query) {
        selectAtlasDomain("population");
      }
    }

    if (heroInput) {
      heroInput.addEventListener("input", function () {
        executeSearch(this.value);
      });
    }

    heroChips.forEach(chip => {
      chip.addEventListener("click", function () {
        const q = this.getAttribute("data-query");
        if (heroInput) heroInput.value = q;
        executeSearch(q);
        const atlasSection = document.getElementById("atlas-section");
        if (atlasSection) {
          atlasSection.scrollIntoView({ behavior: "smooth" });
        }
      });
    });
  }

  renderDistricts();
  initDataAtlas();
});
