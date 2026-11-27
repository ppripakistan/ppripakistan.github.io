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
  const modeBanner = document.getElementById("nfcModeBanner");
  const validationError = document.getElementById("nfcValidationError");
  const resultsTitle = document.getElementById("nfcResultsTitle");
  const shareColHeader = document.getElementById("nfcShareColHeader");
  const keyFindingEl = document.getElementById("nfcKeyFinding");

  // Official 7th NFC Award (2010) horizontal shares — Finance Division Fiscal Policy Statement 2010-11
  const OFFICIAL_7TH_NFC_SHARES = {
    punjab: 51.74,
    sindh: 24.55,
    kp: 14.62,
    balochistan: 9.09
  };

  // Documented illustrative baseline metrics for reform modeling (each criterion sums to 100.00%):
  // Population: Census 2023 relative provincial shares excluding ICT (normalized to 100.00%)
  // Poverty, Revenue, Inverse Density: illustrative policy-modeling benchmarks summing to 100%
  const provincialCriteria = {
    punjab: { pop: 53.39534, pov: 25.0, rev: 35.0, den: 12.0 },
    sindh: { pop: 23.29233, pov: 23.0, rev: 55.0, den: 18.0 },
    kp: { pop: 17.08171, pov: 28.0, rev: 8.0, den: 15.0 },
    balochistan: { pop: 6.23062, pov: 24.0, rev: 2.0, den: 55.0 }
  };

  let nfcMode = "official_7th"; // "official_7th" | "illustrative"

  function clearNfcOutputs(message) {
    ["punjab", "sindh", "kp", "balochistan"].forEach(function (p) {
      const pctEl = document.getElementById("nfcShare_" + p);
      const amtEl = document.getElementById("nfcAmt_" + p);
      if (pctEl) pctEl.textContent = "—";
      if (amtEl) amtEl.textContent = "—";
    });
    if (keyFindingEl) {
      keyFindingEl.innerHTML =
        "<strong>Input Required:</strong> " +
        (message || "Enter a valid divisible pool (Rs 500 B to Rs 25,000 B) and positive criteria weights to compute provincial allocations.");
    }
  }

  function updateNfcCalculation(modeOverride) {
    if (!sliderPop || !sliderPov || !sliderRev || !sliderDen) return;
    if (modeOverride) nfcMode = modeOverride;

    const wPop = parseFloat(sliderPop.value) || 0;
    const wPov = parseFloat(sliderPov.value) || 0;
    const wRev = parseFloat(sliderRev.value) || 0;
    const wDen = parseFloat(sliderDen.value) || 0;
    const totalWeight = wPop + wPov + wRev + wDen;

    if (valPop) valPop.textContent = wPop.toFixed(1) + "%";
    if (valPov) valPov.textContent = wPov.toFixed(1) + "%";
    if (valRev) valRev.textContent = wRev.toFixed(1) + "%";
    if (valDen) valDen.textContent = wDen.toFixed(1) + "%";

    const rawPool = poolInput ? poolInput.value.trim() : "5500";
    const pool = rawPool === "" ? NaN : Number(rawPool);

    if (!Number.isFinite(pool) || pool < 500 || pool > 25000) {
      if (validationError) {
        validationError.classList.add("is-visible");
        validationError.textContent = "Enter a divisible pool size between Rs 500 B and Rs 25,000 B.";
      }
      if (poolInput) poolInput.setAttribute("aria-invalid", "true");
      clearNfcOutputs("Divisible pool must be between Rs 500 B and Rs 25,000 B.");
      return;
    }
    if (poolInput) poolInput.setAttribute("aria-invalid", "false");

    const provinces = ["punjab", "sindh", "kp", "balochistan"];

    if (totalWeight <= 0) {
      if (totalWeightBadge) {
        totalWeightBadge.textContent = "Total Weight: 0.0% (Invalid — must exceed 0%)";
        totalWeightBadge.className = "nfc-total-weight-badge warning";
      }
      if (validationError) {
        validationError.classList.add("is-visible");
        validationError.textContent = "Total criteria weight cannot be 0%. Adjust at least one slider above 0% to calculate provincial allocations.";
      }
      clearNfcOutputs("Adjust at least one criteria slider above 0% to compute provincial shares.");
      return;
    }

    if (validationError) {
      validationError.classList.remove("is-visible");
      validationError.textContent = "";
    }

    if (totalWeightBadge) {
      totalWeightBadge.textContent = "Total Weight: " + totalWeight.toFixed(1) + "%";
      if (Math.abs(totalWeight - 100) < 0.05) {
        totalWeightBadge.className = "nfc-total-weight-badge valid";
      } else {
        totalWeightBadge.className = "nfc-total-weight-badge warning";
        totalWeightBadge.textContent += " (Normalized to 100%)";
      }
    }

    let rawShares = {};
    if (nfcMode === "official_7th") {
      rawShares = Object.assign({}, OFFICIAL_7TH_NFC_SHARES);
      if (resultsTitle) resultsTitle.textContent = "Official 7th NFC Horizontal Allocation (Statutory 2010 Baseline)";
      if (shareColHeader) shareColHeader.textContent = "Official 7th NFC Share %";
      if (modeBanner) {
        modeBanner.classList.remove("is-illustrative");
        modeBanner.innerHTML =
          '<strong>Reference Mode — Official 7th NFC Award (2010):</strong> Displaying statutory horizontal shares (Punjab 51.74%, Sindh 24.55%, KP 14.62%, Balochistan 9.09%) from <a href="https://finance.gov.pk/publications/FiscalPolicyStatement_2010_11.pdf" target="_blank" rel="noopener">Finance Division (2010–11)</a>. Adjusting sliders switches to the illustrative reform model.';
      }
    } else {
      const nPop = wPop / totalWeight;
      const nPov = wPov / totalWeight;
      const nRev = wRev / totalWeight;
      const nDen = wDen / totalWeight;

      provinces.forEach(function (p) {
        const c = provincialCriteria[p];
        rawShares[p] = (c.pop * nPop) + (c.pov * nPov) + (c.rev * nRev) + (c.den * nDen);
      });

      const rawSum = provinces.reduce((acc, p) => acc + rawShares[p], 0);
      if (Math.abs(rawSum - 100) > 1e-6) {
        throw new Error("NFC allocation shares must sum to 100% before rounding; got " + rawSum);
      }

      if (resultsTitle) resultsTitle.textContent = "Illustrative Reform Model Allocation (Modelled)";
      if (shareColHeader) shareColHeader.textContent = "Modelled Share %";
      if (modeBanner) {
        modeBanner.classList.add("is-illustrative");
        modeBanner.innerHTML =
          "<strong>Illustrative Reform Model:</strong> Modelled shares computed from Census 2023 provincial population shares (53.40% / 23.29% / 17.08% / 6.23%) and PPRI illustrative poverty, revenue, and inverse-density inputs. Click <em>7th NFC (Status Quo)</em> or <em>Reset Default</em> for the official 2010 statutory award.";
      }
    }

    provinces.forEach(function (p) {
      const sharePct = rawShares[p];
      const shareAmount = (sharePct / 100) * pool;

      const pctEl = document.getElementById("nfcShare_" + p);
      const amtEl = document.getElementById("nfcAmt_" + p);
      if (pctEl) pctEl.textContent = sharePct.toFixed(2) + "%";
      if (amtEl) amtEl.textContent = "Rs " + Math.round(shareAmount).toLocaleString("en-US") + " B";
    });

    if (keyFindingEl) {
      const poolFormatted = pool.toLocaleString("en-US");
      const balAmt = Math.round((rawShares.balochistan / 100) * pool).toLocaleString("en-US");
      if (nfcMode === "official_7th") {
        // Illustrative 10-point shift benchmark: 72% Pop, 15.3% Pov, 5% Rev, 7.7% Den
        const shiftedBalShare =
          provincialCriteria.balochistan.pop * 0.72 +
          provincialCriteria.balochistan.pov * 0.153 +
          provincialCriteria.balochistan.rev * 0.05 +
          provincialCriteria.balochistan.den * 0.077;
        const deltaAmt = Math.round(((shiftedBalShare - OFFICIAL_7TH_NFC_SHARES.balochistan) / 100) * pool);
        const shiftGain = (shiftedBalShare - OFFICIAL_7TH_NFC_SHARES.balochistan).toFixed(2);
        keyFindingEl.innerHTML =
          "<strong>Baseline Reference (Official 7th NFC):</strong> At a Rs " +
          poolFormatted +
          " B divisible pool, Balochistan receives <strong>Rs " +
          balAmt +
          " B (9.09%)</strong>. In an illustrative model shifting 10 percentage points from population to inverse density (+5%) and poverty (+5%), Balochistan rises by <strong>+" +
          shiftGain +
          " pp</strong> (~Rs " +
          deltaAmt.toLocaleString("en-US") +
          " B).";
      } else {
        const deltaPct = rawShares.balochistan - OFFICIAL_7TH_NFC_SHARES.balochistan;
        const deltaAmt = Math.round((deltaPct / 100) * pool);
        const sign = deltaPct >= 0 ? "+" : "-";
        keyFindingEl.innerHTML =
          "<strong>Live Model Comparison:</strong> At Rs " +
          poolFormatted +
          " B pool, Balochistan's modelled transfer is <strong>Rs " +
          balAmt +
          " B (" +
          rawShares.balochistan.toFixed(2) +
          "%)</strong> &mdash; <strong>" +
          sign +
          Math.abs(deltaPct).toFixed(2) +
          " pp (" +
          sign +
          "Rs " +
          Math.abs(deltaAmt).toLocaleString("en-US") +
          " B)</strong> vs. the Official 7th NFC statutory baseline (9.09%).";
      }
    }
  }

  [sliderPop, sliderPov, sliderRev, sliderDen].forEach(function (slider) {
    if (slider) {
      slider.addEventListener("input", function () {
        updateNfcCalculation("illustrative");
      });
    }
  });
  if (poolInput) {
    poolInput.addEventListener("input", function () {
      updateNfcCalculation();
    });
  }

  // Preset & Reset Buttons
  const preset7th = document.getElementById("preset7th");
  const presetEqual = document.getElementById("presetEqual");
  const presetPop = document.getElementById("presetPop");
  const presetNeed = document.getElementById("presetNeed");
  const resetNfcBtn = document.getElementById("btnResetNfc");

  function resetToOfficial7th(resetPool) {
    if (!sliderPop || !sliderPov || !sliderRev || !sliderDen) return;
    sliderPop.value = "82.0";
    sliderPov.value = "10.3";
    sliderRev.value = "5.0";
    sliderDen.value = "2.7";
    if (poolInput && (resetPool || !Number.isFinite(Number(poolInput.value)) || Number(poolInput.value) < 500 || Number(poolInput.value) > 25000)) {
      poolInput.value = "5500";
    }
    updateNfcCalculation("official_7th");
  }

  if (preset7th) {
    preset7th.addEventListener("click", function () {
      resetToOfficial7th(false);
    });
  }
  if (resetNfcBtn) {
    resetNfcBtn.addEventListener("click", function () {
      resetToOfficial7th(true);
    });
  }
  if (presetEqual) {
    presetEqual.addEventListener("click", function () {
      sliderPop.value = "40.0";
      sliderPov.value = "30.0";
      sliderRev.value = "15.0";
      sliderDen.value = "15.0";
      updateNfcCalculation("illustrative");
    });
  }
  if (presetPop) {
    presetPop.addEventListener("click", function () {
      sliderPop.value = "100.0";
      sliderPov.value = "0.0";
      sliderRev.value = "0.0";
      sliderDen.value = "0.0";
      updateNfcCalculation("illustrative");
    });
  }
  if (presetNeed) {
    presetNeed.addEventListener("click", function () {
      sliderPop.value = "50.0";
      sliderPov.value = "35.0";
      sliderRev.value = "5.0";
      sliderDen.value = "10.0";
      updateNfcCalculation("illustrative");
    });
  }

  // Initialize official 7th NFC reference state on load
  updateNfcCalculation("official_7th");

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
  const districtMobileList = document.getElementById("districtMobileList");
  const districtCountEl = document.getElementById("districtCount");
  const exportCsvBtn = document.getElementById("btnExportDistrictCsv");
  const exportJsonBtn = document.getElementById("btnExportDistrictJson");
  const exportHintEl = document.getElementById("districtExportHint");

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

    const matchCount = currentFilteredDistricts.length;
    if (districtCountEl) {
      districtCountEl.textContent = `Showing ${matchCount} of ${districtData.length} sample districts (of 144 Prov+ICT / 168 national)`;
    }

    if (exportCsvBtn) {
      exportCsvBtn.disabled = matchCount === 0;
      exportCsvBtn.setAttribute("aria-disabled", String(matchCount === 0));
    }
    if (exportJsonBtn) {
      exportJsonBtn.disabled = matchCount === 0;
      exportJsonBtn.setAttribute("aria-disabled", String(matchCount === 0));
    }
    if (exportHintEl) {
      exportHintEl.textContent =
        matchCount === 0 ? "No matching rows to download. Adjust or clear filters to enable CSV export." : "";
    }

    if (matchCount === 0) {
      districtTbody.innerHTML =
        '<tr><td colspan="7" class="dc-empty-cell">No sample districts found matching your filter.</td></tr>';
      if (districtMobileList) {
        districtMobileList.innerHTML =
          '<div class="dc-search-empty"><p>No matching sample districts found. Try clearing filters.</p></div>';
      }
      return;
    }

    districtTbody.innerHTML = currentFilteredDistricts
      .map(function (d) {
        return `<tr>
          <td><strong>${d.district}</strong></td>
          <td><span class="dc-prov-badge">${d.province}</span></td>
          <td>${d.division}</td>
          <td class="dc-num-col">${d.pop.toLocaleString("en-US")}</td>
          <td class="dc-num-col">${d.area.toLocaleString("en-US")}</td>
          <td class="dc-num-col">${d.density.toFixed(1)}</td>
          <td>${d.capitalDist}</td>
        </tr>`;
      })
      .join("");

    if (districtMobileList) {
      districtMobileList.innerHTML = currentFilteredDistricts
        .map(function (d) {
          return `<details class="district-mobile-card">
            <summary>
              <span><span class="dm-name">${d.district}</span><span class="dm-prov">${d.province}</span></span>
              <span class="dm-pop">${d.pop.toLocaleString("en-US")}</span>
              <span class="dm-chevron" aria-hidden="true">&#8250;</span>
            </summary>
            <div class="district-mobile-details">
              <div><strong>Division:</strong> ${d.division}</div>
              <div><strong>Area:</strong> ${d.area.toLocaleString("en-US")} km&sup2;</div>
              <div><strong>Density:</strong> ${d.density.toFixed(1)}/km&sup2;</div>
              <div><strong>To Capital:</strong> ${d.capitalDist}</div>
            </div>
          </details>`;
        })
        .join("");
    }
  }

  if (searchInput) searchInput.addEventListener("input", renderDistricts);
  if (provinceFilter) provinceFilter.addEventListener("change", renderDistricts);
  if (popFilter) popFilter.addEventListener("change", renderDistricts);

  // CSV Export (strictly filtered rows only; never falls back to all rows)
  if (exportCsvBtn) {
    exportCsvBtn.addEventListener("click", function () {
      if (currentFilteredDistricts.length === 0) return;
      const exportList = currentFilteredDistricts;
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
      a.download = "ppri_district_filtered_sample_2023.csv";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });
  }

  // JSON Export
  if (exportJsonBtn) {
    exportJsonBtn.addEventListener("click", function () {
      if (currentFilteredDistricts.length === 0) return;
      const exportList = currentFilteredDistricts;
      const jsonContent = JSON.stringify(
        {
          dataset: "PPRI District & Administrative Filtered Sample",
          source: "PBS Census 2023 / Admin Geography 2023",
          count: exportList.length,
          data: exportList
        },
        null,
        2
      );
      const blob = new Blob([jsonContent], { type: "application/json" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "ppri_district_filtered_sample_2023.json";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    });
  }

  // --- VERIFIED INDICATOR & TOPIC SEARCH ---
  function initThematicSearch() {
    const searchForm = document.getElementById("dcSearchForm");
    const heroInput = document.getElementById("heroCommandInput");
    const clearBtn = document.getElementById("dcSearchClear");
    const resultsWrap = document.getElementById("dcSearchResults");
    const statusText = document.getElementById("dcSearchStatusText");
    const resetInlineBtn = document.getElementById("dcResetSearch");
    const resultsGrid = document.getElementById("dcIndicatorGrid");
    const emptyBox = document.getElementById("dcSearchEmpty");
    const emptyQuerySpan = document.getElementById("dcSearchEmptyQuery");
    const emptyResetBtn = document.getElementById("dcEmptyClear");
    const heroChips = document.querySelectorAll(".dc-command-chip[data-query]");
    const topicGroups = document.querySelectorAll(".dc-topic-group");

    let indicators = [];
    fetch("/assets/data/data-centre-indicators.json")
      .then((r) => (r.ok ? r.json() : []))
      .then((data) => {
        indicators = Array.isArray(data) ? data : [];
        if (heroInput && heroInput.value.trim()) executeSearch(heroInput.value);
      })
      .catch(() => {
        indicators = [];
      });

    function escapeHTML(str) {
      return String(str || "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
    }

    function executeSearch(rawQuery) {
      const query = (rawQuery || "").toLowerCase().trim();
      if (clearBtn) clearBtn.hidden = !query;

      if (!query) {
        if (resultsWrap) resultsWrap.hidden = true;
        if (resultsGrid) resultsGrid.innerHTML = "";
        if (emptyBox) emptyBox.hidden = true;
        topicGroups.forEach((g) => {
          g.hidden = false;
        });
        return;
      }

      const terms = query.split(/\s+/).filter(Boolean);
      const matchedIndicators = indicators.filter((ind) => {
        const hay = `${ind.label} ${ind.domain} ${ind.summary} ${ind.keywords} ${ind.source}`.toLowerCase();
        return terms.every((t) => hay.includes(t));
      });

      let visibleGroups = 0;
      topicGroups.forEach((group) => {
        const gText = `${group.textContent} ${group.getAttribute("data-keywords") || ""}`.toLowerCase();
        const groupMatch = terms.some((t) => gText.includes(t));
        group.hidden = !groupMatch && matchedIndicators.length > 0;
        if (!group.hidden) visibleGroups++;
      });

      if (resultsWrap) resultsWrap.hidden = false;
      if (matchedIndicators.length > 0) {
        if (statusText) {
          statusText.textContent = `${matchedIndicators.length} verified indicator${matchedIndicators.length === 1 ? "" : "s"} matched "${rawQuery.trim()}"`;
        }
        if (emptyBox) emptyBox.hidden = true;
        if (resultsGrid) {
          resultsGrid.hidden = false;
          resultsGrid.innerHTML = matchedIndicators
            .map(
              (ind) => `<a class="dc-indicator-card" href="${escapeHTML(ind.url)}"${ind.isDownload ? " download" : ""}>
                <div class="dc-indicator-top">
                  <span class="dc-indicator-title">${escapeHTML(ind.label)}</span>
                  <span class="dc-indicator-stat">${escapeHTML(ind.stat)}</span>
                </div>
                <p class="dc-indicator-desc">${escapeHTML(ind.summary)}</p>
                <div class="dc-indicator-meta">
                  <span>${escapeHTML(ind.domain)}</span>
                  <span>Source: ${escapeHTML(ind.source)}</span>
                </div>
              </a>`
            )
            .join("");
        }
      } else {
        if (statusText) statusText.textContent = `0 verified indicators matched "${rawQuery.trim()}"`;
        if (resultsGrid) {
          resultsGrid.hidden = true;
          resultsGrid.innerHTML = "";
        }
        if (emptyBox) emptyBox.hidden = false;
        if (emptyQuerySpan) emptyQuerySpan.textContent = rawQuery.trim();
        topicGroups.forEach((g) => {
          g.hidden = false;
        });
      }
    }

    function clearSearch() {
      if (heroInput) {
        heroInput.value = "";
        heroInput.focus();
      }
      executeSearch("");
    }

    if (searchForm) {
      searchForm.addEventListener("submit", function (e) {
        e.preventDefault();
        executeSearch(heroInput ? heroInput.value : "");
      });
    }
    if (heroInput) {
      heroInput.addEventListener("input", function () {
        executeSearch(this.value);
      });
    }
    if (clearBtn) clearBtn.addEventListener("click", clearSearch);
    if (resetInlineBtn) resetInlineBtn.addEventListener("click", clearSearch);
    if (emptyResetBtn) emptyResetBtn.addEventListener("click", clearSearch);

    heroChips.forEach((chip) => {
      chip.addEventListener("click", function () {
        const q = this.getAttribute("data-query");
        if (heroInput) heroInput.value = q;
        executeSearch(q);
      });
    });
  }

  renderDistricts();
  initThematicSearch();
});
