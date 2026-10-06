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

  renderDistricts();
});
