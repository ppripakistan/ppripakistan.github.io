# -*- coding: utf-8 -*-
"""
Build Script for Overhauled Visual Insights & Policy Infographics Lab (01–15)
Generates data/staging/insights.html with:
1. Donut 100% completion fix for Card 1 (adding Grants & Other slice).
2. Complete totals displayed on all 9 public debt bars for Card 2.
3. Valid SVG <tspan> tags for Card 3 legend (fixing misplaced yellow/red swatches).
4. Expanded province label gutter and stacked density sub-labels for Card 4 (Khyber Pakhtunkhwa & Balochistan overlap fixes).
5. Expanded label gutter for Card 6 (Khyber Pakhtunkhwa bar overlap fix).
6. Vertically staggered labels and wide legend for Card 7 (purchasing power overlap fix).
7. Non-overlapping corner quadrant badges, clipped boundaries, and clamped bubble radii for Card 11 (135 districts scatter map).
8. 2-line stacked tenure headers for Card 15 (macroeconomic trajectory overlap fix).
9. Prominent sequential numbering (INFOGRAPHIC 01 / 16 to INFOGRAPHIC 15 / 16) across all cards, titles, headers, and export files.
10. Zero-network embedded offline data (134 KB across 15 curated datasets).
"""

import os
import json

OUTPUT_FILE = os.path.join("data", "staging", "insights.html")
STAGING_DIR = os.path.join("data", "staging")

def load_all_datasets():
    datasets = {
        'fiscal': 'federal_fiscal_summary.json',
        'debt': 'public_debt_timeseries.json',
        'tax_exp': 'tax_expenditures_2025.json',
        'gender_land': 'provincial_gender_demographics.json',
        'hies': 'hies_household_expenditures.json',
        'consumption': 'provincial_consumption_pies.json',
        'wage_infl': 'inflation_wage_growth.json',
        'services': 'housing_basic_services.json',
        'lfs': 'lfs_employment_wages.json',
        'census_shifts': 'provincial_census_shifts.json',
        'districts': 'census_2023_districts.json',
        'agri_shifts': 'provincial_agri_shifts.json',
        'census_hist': 'census_historical_growth.json',
        'macro': 'macro_indicators_timeseries.json',
        'prov_matrix': 'provincial_fiscal_conflict_matrix.json'
    }
    loaded = {}
    for k, fname in datasets.items():
        p = os.path.join(STAGING_DIR, fname)
        with open(p, 'r', encoding='utf-8') as f:
            loaded[k] = json.load(f)
    return loaded

def generate_insights_html():
    data = load_all_datasets()
    embedded_json = json.dumps(data)

    html_content = r'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>PPRI Visual Insights &amp; Policy Infographics Lab (01–16)</title>
    <meta name="description" content="Publication-grade interactive policy infographics (01 to 16) covering Pakistan Census 2023, Gender &amp; Land Territorial Asymmetry, Provincial Resource Allocation &amp; Conflict Matrix, Living Standards (HIES 2024-25), Labour Disparities (LFS 2024-25), Agrarian Shifts (Ag Census 2024), Public Debt Explosion, and 35-Year Macroeconomic Trajectory." />
    <link rel="canonical" href="https://ppripakistan.github.io/data/staging/insights.html" />
    <meta name="robots" content="noindex, nofollow" />
    <link rel="icon" type="image/png" href="/favicon.png?v=2" />
    <link rel="stylesheet" href="/assets/css/style.css" />
    <link rel="stylesheet" href="/assets/css/responsive.css" />

    <style>
      :root {
        --vi-navy: #073c3a;
        --vi-teal: #0f766e;
        --vi-teal-light: #e6f3f2;
        --vi-teal-dark: #042f2e;
        --vi-ink: #0f172a;
        --vi-muted: #64748b;
        --vi-line: #e2e8f0;
        --vi-bg: #f8fafc;
        --vi-paper: #ffffff;
        --vi-amber: #d97706;
        --vi-amber-light: #fef3c7;
        --vi-green: #15803d;
        --vi-green-light: #dcfce7;
        --vi-blue: #0284c7;
        --vi-blue-light: #e0f2fe;
        --vi-rose: #e11d48;
        --vi-rose-light: #ffe4e6;
        --vi-purple: #7c3aed;
        --vi-purple-light: #ede9fe;
      }

      body {
        background: var(--vi-bg);
        color: var(--vi-ink);
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        margin: 0;
        padding: 0;
        line-height: 1.5;
      }

      /* Top Staging Banner */
      .vi-topbar {
        background: #0f172a;
        color: #94a3b8;
        padding: 8px 24px;
        font-size: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 8px;
        border-bottom: 1px solid #334155;
      }
      .vi-topbar-left {
        display: flex;
        align-items: center;
        gap: 8px;
      }
      .vi-badge-quarantine {
        background: #f59e0b;
        color: #0f172a;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 4px;
        font-size: 11px;
        letter-spacing: 0.5px;
      }
      .vi-topbar-links a {
        color: #38bdf8;
        text-decoration: none;
        margin-left: 16px;
        font-weight: 500;
      }
      .vi-topbar-links a:hover {
        text-decoration: underline;
      }

      /* Header */
      .vi-header {
        background: var(--vi-navy);
        color: #fff;
        padding: 20px 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 16px;
        border-bottom: 4px solid var(--vi-teal);
      }
      .vi-brand {
        display: flex;
        align-items: center;
        gap: 14px;
      }
      .vi-brand-logo {
        width: 44px;
        height: 44px;
        background: var(--vi-teal);
        color: #fff;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 20px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.2);
      }
      .vi-brand h1 {
        margin: 0;
        font-size: 20px;
        font-weight: 700;
        letter-spacing: -0.3px;
        color: #fff;
      }
      .vi-brand p {
        margin: 2px 0 0;
        font-size: 12px;
        color: #99f6e4;
      }

      /* Hero */
      .vi-hero {
        background: #ffffff;
        border-bottom: 1px solid var(--vi-line);
        padding: 32px 24px;
      }
      .vi-hero-inner {
        max-width: 1320px;
        margin: 0 auto;
      }
      .vi-hero-title {
        font-size: 28px;
        font-weight: 800;
        color: var(--vi-navy);
        margin: 0 0 10px;
        letter-spacing: -0.5px;
      }
      .vi-hero-desc {
        font-size: 15px;
        color: var(--vi-muted);
        max-width: 950px;
        margin: 0 0 20px;
        line-height: 1.6;
      }

      /* Number Index Quick Jump */
      .vi-quick-index {
        display: flex;
        gap: 6px;
        flex-wrap: wrap;
        align-items: center;
        margin-bottom: 16px;
        padding-bottom: 16px;
        border-bottom: 1px dashed var(--vi-line);
      }
      .vi-quick-index span {
        font-size: 12px;
        font-weight: 700;
        color: var(--vi-navy);
        margin-right: 6px;
      }
      .vi-jump-pill {
        background: #f1f5f9;
        border: 1px solid var(--vi-line);
        color: var(--vi-teal);
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 11.5px;
        font-weight: 700;
        text-decoration: none;
        transition: all 0.15s ease;
      }
      .vi-jump-pill:hover {
        background: var(--vi-teal);
        color: #ffffff;
        border-color: var(--vi-teal);
      }

      .vi-filter-bar {
        display: flex;
        gap: 8px;
        flex-wrap: wrap;
        align-items: center;
      }
      .vi-filter-btn {
        background: var(--vi-bg);
        border: 1px solid var(--vi-line);
        color: var(--vi-muted);
        padding: 7px 14px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
      }
      .vi-filter-btn:hover {
        background: #e2e8f0;
        color: var(--vi-ink);
      }
      .vi-filter-btn.active {
        background: var(--vi-teal);
        border-color: var(--vi-teal);
        color: #fff;
      }

      /* Main Gallery Container */
      .vi-main {
        max-width: 1320px;
        margin: 32px auto;
        padding: 0 24px;
      }

      /* Cards Grid */
      .vi-grid {
        display: grid;
        grid-template-columns: repeat(12, 1fr);
        gap: 24px;
      }

      /* Infographic Card */
      .vi-card {
        background: var(--vi-paper);
        border: 1px solid var(--vi-line);
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        display: flex;
        flex-direction: column;
        overflow: hidden;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
      }
      .vi-card:hover {
        box-shadow: 0 8px 16px rgba(0,0,0,0.08);
      }
      .vi-card.col-6 {
        grid-column: span 6;
      }
      .vi-card.col-12 {
        grid-column: span 12;
      }
      @media (max-width: 1024px) {
        .vi-card.col-6 {
          grid-column: span 12;
        }
      }

      /* Card Top Border Accent */
      .vi-card-accent {
        height: 5px;
        background: linear-gradient(90deg, var(--vi-teal), #0d9488);
      }

      /* Card Header */
      .vi-card-header {
        padding: 20px 24px 12px;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 16px;
        flex-wrap: wrap;
      }
      .vi-header-meta {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 6px;
        flex-wrap: wrap;
      }
      .vi-number-badge {
        background: var(--vi-navy);
        color: #ffffff;
        font-size: 11px;
        font-weight: 800;
        padding: 3px 8px;
        border-radius: 4px;
        letter-spacing: 0.5px;
        display: inline-flex;
        align-items: center;
      }
      .vi-card-tag {
        display: inline-block;
        font-size: 10.5px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        color: var(--vi-teal);
        background: var(--vi-teal-light);
        padding: 3px 8px;
        border-radius: 4px;
      }
      .vi-card-title {
        font-size: 19px;
        font-weight: 700;
        color: var(--vi-navy);
        margin: 0 0 4px;
        letter-spacing: -0.3px;
      }
      .vi-card-subtitle {
        font-size: 13px;
        color: var(--vi-muted);
        margin: 0;
        line-height: 1.4;
      }
      .vi-card-controls {
        display: flex;
        gap: 6px;
        flex-wrap: wrap;
      }
      .vi-ctrl-btn {
        background: #f1f5f9;
        border: 1px solid var(--vi-line);
        color: #475569;
        padding: 5px 10px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.15s ease;
      }
      .vi-ctrl-btn:hover {
        background: #e2e8f0;
        color: #0f172a;
      }
      .vi-ctrl-btn.active {
        background: var(--vi-navy);
        border-color: var(--vi-navy);
        color: #ffffff;
      }

      /* Chart Canvas / SVG Container */
      .vi-chart-container {
        padding: 12px 24px 16px;
        position: relative;
        background: #ffffff;
        min-height: 380px;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      .vi-chart-svg {
        width: 100%;
        height: auto;
        max-height: 440px;
        display: block;
      }

      /* Callout Insights Box */
      .vi-callout {
        margin: 0 24px 16px;
        padding: 12px 16px;
        background: #f8fafc;
        border: 1px solid var(--vi-line);
        border-left: 4px solid var(--vi-teal);
        border-radius: 6px;
        font-size: 12.5px;
        line-height: 1.5;
        color: #334155;
      }
      .vi-callout strong {
        color: var(--vi-navy);
      }
      .vi-kpis {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        margin-top: 8px;
      }
      .vi-kpi-pill {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 11.5px;
        display: flex;
        align-items: center;
        gap: 6px;
      }
      .vi-kpi-pill strong {
        color: var(--vi-teal);
      }

      /* Watermark & Export Footer */
      .vi-card-footer {
        padding: 12px 24px;
        background: #f8fafc;
        border-top: 1px solid var(--vi-line);
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: auto;
      }
      .vi-source {
        font-size: 11.5px;
        color: var(--vi-muted);
      }
      .vi-source strong {
        color: var(--vi-navy);
      }
      .vi-actions {
        display: flex;
        gap: 8px;
        align-items: center;
      }
      .vi-btn {
        background: #ffffff;
        border: 1px solid var(--vi-line);
        color: #334155;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 12px;
        font-weight: 600;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        transition: all 0.2s ease;
      }
      .vi-btn:hover {
        background: #f1f5f9;
        border-color: #cbd5e1;
        color: #0f172a;
      }
      .vi-btn-primary {
        background: var(--vi-teal);
        border-color: var(--vi-teal);
        color: #ffffff;
      }
      .vi-btn-primary:hover {
        background: #0d9488;
        border-color: #0d9488;
        color: #ffffff;
      }

      /* Interactive Tooltip */
      #vi-tooltip {
        position: fixed;
        display: none;
        background: rgba(15, 23, 42, 0.95);
        color: #ffffff;
        padding: 8px 12px;
        border-radius: 6px;
        font-size: 12px;
        pointer-events: none;
        z-index: 10000;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        max-width: 280px;
        backdrop-filter: blur(4px);
      }
      #vi-tooltip strong {
        color: #38bdf8;
      }

      /* Notification Toast */
      #vi-toast {
        position: fixed;
        bottom: 24px;
        right: 24px;
        background: var(--vi-navy);
        color: #ffffff;
        padding: 12px 20px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: 600;
        display: none;
        z-index: 10001;
        box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        border-left: 4px solid var(--vi-teal);
      }
    </style>
  </head>
  <body>
    <!-- Top Staging Notice Bar -->
    <div class="vi-topbar">
      <div class="vi-topbar-left">
        <span class="vi-badge-quarantine">ISOLATED STAGING LAB</span>
        <span>All data curated in sandbox repository (15 harmonized stores). Live observatory hubs remain unpromoted.</span>
      </div>
      <div class="vi-topbar-links">
        <a href="/data/staging/review.html">&#x1F5C4;&#xFE0F; Staging Vault Review</a>
        <a href="/sources/">&#x1F4DA; Evidence Library</a>
        <a href="/">PPRI Portal Home &rarr;</a>
      </div>
    </div>

    <!-- Header -->
    <header class="vi-header">
      <div class="vi-brand">
        <div class="vi-brand-logo">P</div>
        <div>
          <h1>Visual Insights &amp; Policy Infographics Lab (01–16)</h1>
          <p>Pakistan Provincial Reform Institute (PPRI) &bull; Evidence-Based Empirical Governance</p>
        </div>
      </div>
      <div class="vi-header-right">
        <span style="font-size: 12px; background: rgba(255,255,255,0.12); padding: 5px 12px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.2);">
          &#x2714;&#xFE0F; 16 Numbered Visualizations &bull; 100% Vector Canvas Rasterizer
        </span>
      </div>
    </header>

    <!-- Hero -->
    <section class="vi-hero">
      <div class="vi-hero-inner">
        <h2 class="vi-hero-title">Empirical Evidence &amp; Visual Analytics Lab</h2>
        <p class="vi-hero-desc">
          Interactive, publication-grade policy infographics across Pakistan Census 2023, Provincial Demographics &amp; Gender/Land Asymmetry, Provincial Resource Allocation &amp; Conflict Disparities, Living Standards (HIES 2024–25), Labour Market (LFS 2024–25), Agrarian Shifts (Ag Census 2024), Public Debt Explosion, and 35-Year Macroeconomic Trajectory. Every infographic is prominently numbered (<strong>01 to 16</strong>) to simplify selection, and features instant <strong>2x Retina PNG download</strong>, <strong>Scalable Vector (SVG) export</strong>, and <strong>Clean CSV</strong> data extraction.
        </p>

        <!-- Quick Jump Index -->
        <div class="vi-quick-index">
          <span>Jump to Infographic:</span>
          <a href="#card-fiscal" class="vi-jump-pill">#01 Fiscal</a>
          <a href="#card-debt" class="vi-jump-pill">#02 Debt</a>
          <a href="#card-tax-exp" class="vi-jump-pill">#03 Taxes</a>
          <a href="#card-gender-land" class="vi-jump-pill">#04 Gender &amp; Land</a>
          <a href="#card-hies" class="vi-jump-pill">#05 Food Burden</a>
          <a href="#card-consumption-pie" class="vi-jump-pill">#06 Budget Slices</a>
          <a href="#card-wage-infl" class="vi-jump-pill">#07 Real Wages</a>
          <a href="#card-services" class="vi-jump-pill">#08 Utilities</a>
          <a href="#card-lfs" class="vi-jump-pill">#09 Labour Gap</a>
          <a href="#card-census-shifts" class="vi-jump-pill">#10 Census Shifts</a>
          <a href="#card-districts-scatter" class="vi-jump-pill">#11 135 Districts Map</a>
          <a href="#card-sector-employment" class="vi-jump-pill">#12 Sector Jobs</a>
          <a href="#card-agri-shifts" class="vi-jump-pill">#13 Agri Land</a>
          <a href="#card-census-hist" class="vi-jump-pill">#14 70-Yr Census</a>
          <a href="#card-macro" class="vi-jump-pill">#15 Macro History</a>
          <a href="#card-prov-matrix" class="vi-jump-pill">#16 Prov Matrix</a>
        </div>

        <!-- Category Filters -->
        <div class="vi-filter-bar">
          <span style="font-size: 12.5px; font-weight: 700; color: var(--vi-ink); margin-right: 4px;">Filter Themes:</span>
          <button type="button" class="vi-filter-btn active" onclick="filterGallery('all')">All Infographics (16)</button>
          <button type="button" class="vi-filter-btn" onclick="filterGallery('fiscal')">Fiscal &amp; Debt Solvency (4)</button>
          <button type="button" class="vi-filter-btn" onclick="filterGallery('demographics')">Population &amp; Demographics (4)</button>
          <button type="button" class="vi-filter-btn" onclick="filterGallery('living')">Labour &amp; Living Standards (4)</button>
          <button type="button" class="vi-filter-btn" onclick="filterGallery('agri')">Agriculture &amp; Structural Shift (2)</button>
          <button type="button" class="vi-filter-btn" onclick="filterGallery('macro')">Macroeconomic History (2)</button>
        </div>
      </div>
    </section>

    <!-- Main Grid -->
    <main class="vi-main">
      <div class="vi-grid">

        <!-- ================= CARD 1: FISCAL EXPENDITURE & DEBT ================= -->
        <div class="vi-card col-6" id="card-fiscal" data-category="fiscal">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 01 / 16</span>
                <span class="vi-card-tag">Federal Fiscal &bull; Debt Servicing Monopoly</span>
              </div>
              <h3 class="vi-card-title">#01: Federal Budget Allocation &amp; Debt Servicing</h3>
              <p class="vi-card-subtitle">Expenditure distribution across sovereign debt markup, defence, civil government, PSDP, and federal grants</p>
            </div>
            <div class="vi-card-controls">
              <button type="button" class="vi-ctrl-btn active" onclick="updateFiscalFY('2025-26')">FY 2025-26</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateFiscalFY('2024-25')">FY 2024-25</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateFiscalFY('2023-24')">FY 2023-24</button>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-fiscal" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-fiscal">
            <strong>Key Policy Takeaway:</strong> Sovereign debt servicing absorbs <strong>51.8% of the federal budget (PKR 9,775B)</strong>, consuming <strong>76.0% of net FBR tax collection</strong> and leaving only <strong>7.4% (PKR 1,400B)</strong> for national development (PSDP).
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Markup Share: <strong>51.8%</strong></span>
              <span class="vi-kpi-pill">Defence Share: <strong>11.2%</strong></span>
              <span class="vi-kpi-pill">PSDP Share: <strong>7.4%</strong></span>
              <span class="vi-kpi-pill">Grants &amp; Other: <strong>12.5%</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Ministry of Finance</strong>, Annual Budget Statement (Federal Budget) &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-fiscal', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-fiscal', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('federal_fiscal_summary')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 2: PUBLIC DEBT TRAJECTORY ================= -->
        <div class="vi-card col-6" id="card-debt" data-category="fiscal">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 02 / 16</span>
                <span class="vi-card-tag">Public Debt &bull; Solvency Pressure</span>
              </div>
              <h3 class="vi-card-title">#02: The 8-Year Public Debt Surge (FY18–FY26)</h3>
              <p class="vi-card-subtitle">Escalation of domestic debt, external obligations, and annual debt servicing burden across all 9 fiscal years</p>
            </div>
            <div class="vi-card-controls">
              <button type="button" class="vi-ctrl-btn active" onclick="updateDebtView('stacked')">Debt Stock (PKR B)</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateDebtView('servicing')">Interest Servicing</button>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-debt" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-debt">
            <strong>Key Policy Takeaway:</strong> Pakistan's total public debt surged from <strong>PKR 24,953B in FY18</strong> to <strong>PKR 83,285B in FY26 (+233.8%)</strong>, while annual markup servicing expanded 6.5-fold from PKR 1,499B to PKR 9,775B.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Total Debt: <strong>PKR 83,285B</strong></span>
              <span class="vi-kpi-pill">Domestic Share: <strong>69.1%</strong></span>
              <span class="vi-kpi-pill">External Share: <strong>30.9%</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Ministry of Finance &amp; SBP</strong>, Debt Bulletins (FY18–FY26) &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-debt', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-debt', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('public_debt_timeseries')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 3: TAX EXPENDITURES ================= -->
        <div class="vi-card col-6" id="card-tax-exp" data-category="fiscal">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 03 / 16</span>
                <span class="vi-card-tag">Tax Policy &bull; Revenue Concessions</span>
              </div>
              <h3 class="vi-card-title">#03: Revenue Collection vs Tax Exemptions</h3>
              <p class="vi-card-subtitle">FBR revenue foregone across Sales Tax, Customs duties, and Income Tax concessions</p>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-tax-exp" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-tax-exp">
            <strong>Key Policy Takeaway:</strong> Total federal tax concessions reach <strong>PKR 2,434.7B (2.32% of GDP)</strong>, equivalent to <strong>26.2% of actual tax collection</strong>. Sales tax exemptions under 6th Schedule represent over half of all foregone revenues.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Foregone Revenue: <strong>PKR 2,434.7B</strong></span>
              <span class="vi-kpi-pill">Sales Tax Loss: <strong>50.8%</strong></span>
              <span class="vi-kpi-pill">Tax-to-GDP Ratio: <strong>9.2%</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Federal Board of Revenue (FBR)</strong>, Tax Expenditure Report 2025 &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-tax-exp', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-tax-exp', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('tax_expenditures_2025')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 4: PROVINCIAL GENDER & LAND ASYMMETRY ================= -->
        <div class="vi-card col-6" id="card-gender-land" data-category="demographics">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 04 / 16</span>
                <span class="vi-card-tag">Demographics &bull; Gender &amp; Territory Asymmetry</span>
              </div>
              <h3 class="vi-card-title">#04: Gender Demographics &amp; Land Area Asymmetry</h3>
              <p class="vi-card-subtitle">Male, female, and transgender distribution in relation to provincial land area shares</p>
            </div>
            <div class="vi-card-controls">
              <button type="button" class="vi-ctrl-btn active" onclick="updateGenderLandProv('PK')">National</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateGenderLandProv('PK-PB')">Punjab</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateGenderLandProv('PK-SN')">Sindh</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateGenderLandProv('PK-KP')">KP</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateGenderLandProv('PK-BA')">Balochistan</button>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-gender-land" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-gender-land">
            <strong>Key Policy Takeaway:</strong> Balochistan spans <strong>43.6% of Pakistan's territory (347,190 km²)</strong> but carries only <strong>6.2% of the population (14.89M)</strong> at 42.9 people/km². Conversely, Punjab concentrates <strong>52.9% of citizens (127.69M)</strong> on 25.8% of land area (621.8 people/km²). Nationally, 20,190 transgender citizens were recorded.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Male: <strong>51.48%</strong></span>
              <span class="vi-kpi-pill">Female: <strong>48.51%</strong></span>
              <span class="vi-kpi-pill">Transgender: <strong>20,190</strong></span>
              <span class="vi-kpi-pill">Sex Ratio: <strong>106.1</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Pakistan Bureau of Statistics</strong>, 7th Population &amp; Housing Census 2023 Table 1 &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-gender-land', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-gender-land', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('provincial_gender_demographics')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 5: HIES FOOD BURDEN ================= -->
        <div class="vi-card col-6" id="card-hies" data-category="living">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 05 / 16</span>
                <span class="vi-card-tag">Living Standards &bull; Engel's Law</span>
              </div>
              <h3 class="vi-card-title">#05: Household Food Burden Divide (HIES 2024–25)</h3>
              <p class="vi-card-subtitle">Share of household consumption absorbed by food staples across provinces and rural/urban divide</p>
            </div>
            <div class="vi-card-controls">
              <button type="button" class="vi-ctrl-btn active" onclick="updateHiesDomain('Total')">Total</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateHiesDomain('Urban')">Urban</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateHiesDomain('Rural')">Rural</button>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-hies" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-hies">
            <strong>Key Policy Takeaway:</strong> Severe living standards divide: <strong>Rural Balochistan households spend 47.3% of their entire budget on basic food</strong>, compared to <strong>28.2% in urban Islamabad</strong>. Rural families nationwide allocate an average of 7.6% more income to basic nutrition.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Balochistan Rural: <strong>47.3% Food</strong></span>
              <span class="vi-kpi-pill">National Rural: <strong>41.6% Food</strong></span>
              <span class="vi-kpi-pill">Islamabad Urban: <strong>28.2% Food</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Pakistan Bureau of Statistics</strong>, HIES 2024–25 &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-hies', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-hies', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('hies_household_expenditures')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 6: PROVINCIAL CONSUMPTION PIES ================= -->
        <div class="vi-card col-6" id="card-consumption-pie" data-category="living">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 06 / 16</span>
                <span class="vi-card-tag">Living Standards &bull; Budget Slices</span>
              </div>
              <h3 class="vi-card-title">#06: Inter-Provincial Household Budget Allocation</h3>
              <p class="vi-card-subtitle">Distribution of monthly household spending across food, housing, energy, health, and education</p>
            </div>
            <div class="vi-card-controls">
              <button type="button" class="vi-ctrl-btn active" onclick="updateConsumptionProv('PK')">Pakistan</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateConsumptionProv('PK-PB')">Punjab</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateConsumptionProv('PK-SN')">Sindh</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateConsumptionProv('PK-KP')">KP</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateConsumptionProv('PK-BA')">Balochistan</button>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-consumption-pie" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-consumption-pie">
            <strong>Key Policy Takeaway:</strong> Non-discretionary survival essentials (Food 36.8% + Housing/Energy 22.4%) consume <strong>59.2% of household budgets</strong>, leaving only <strong>12.2% for Health &amp; Education combined</strong>. Mean monthly expenditure ranges from PKR 112,400 in ICT to PKR 58,100 in Balochistan.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Food &amp; Utilities: <strong>59.2%</strong></span>
              <span class="vi-kpi-pill">Health: <strong>6.8%</strong></span>
              <span class="vi-kpi-pill">Education: <strong>5.4%</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Pakistan Bureau of Statistics</strong>, HIES 2024–25 &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-consumption-pie', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-consumption-pie', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('provincial_consumption_pies')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 7: PURCHASING POWER EROSION ================= -->
        <div class="vi-card col-6" id="card-wage-infl" data-category="living">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 07 / 16</span>
                <span class="vi-card-tag">Purchasing Power &bull; Inflation Squeeze</span>
              </div>
              <h3 class="vi-card-title">#07: Purchasing Power Erosion: Inflation vs Wages</h3>
              <p class="vi-card-subtitle">Cumulative CPI price inflation vs nominal wage index adjustments (2020–2024)</p>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-wage-infl" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-wage-infl">
            <strong>Key Policy Takeaway:</strong> Cumulative consumer prices skyrocketed by <strong>+118.4% between 2020 and 2024</strong>, while nominal wages adjusted by only <strong>+64.2%</strong>, inflicting a severe <strong>-24.8% contraction in real household purchasing power</strong>.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Cumulative CPI: <strong>+118.4%</strong></span>
              <span class="vi-kpi-pill">Nominal Wage: <strong>+64.2%</strong></span>
              <span class="vi-kpi-pill">Real Wage Deficit: <strong>-24.8%</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>PBS CPI Bulletins &amp; Labour Force Surveys</strong> (2020–2024) &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-wage-infl', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-wage-infl', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('inflation_wage_growth')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 8: BASIC SERVICES ACCESS ================= -->
        <div class="vi-card col-6" id="card-services" data-category="living">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 08 / 16</span>
                <span class="vi-card-tag">Housing Census &bull; Basic Infrastructure</span>
              </div>
              <h3 class="vi-card-title">#08: Household Basic Services &amp; Utilities Access</h3>
              <p class="vi-card-subtitle">Provincial access rates for piped water, flush sanitation, grid electricity, and natural gas</p>
            </div>
            <div class="vi-card-controls">
              <button type="button" class="vi-ctrl-btn active" onclick="updateServicesProv('PK')">National</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateServicesProv('PK-PB')">Punjab</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateServicesProv('PK-SN')">Sindh</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateServicesProv('PK-KP')">KP</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateServicesProv('PK-BA')">Balochistan</button>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-services" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-services">
            <strong>Key Policy Takeaway:</strong> Severe infrastructure disparities persist: only <strong>14.8% of Balochistan homes have piped water</strong> and <strong>11.2% have piped gas</strong>, compared to national grid electricity access of 91.4% and flush toilet coverage of 59.6%.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Piped Water: <strong>29.8% PK / 14.8% BA</strong></span>
              <span class="vi-kpi-pill">Flush Toilet: <strong>59.6% PK / 31.4% BA</strong></span>
              <span class="vi-kpi-pill">Piped Gas: <strong>36.2% PK / 11.2% BA</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Pakistan Bureau of Statistics</strong>, Housing Census 2023 &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-services', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-services', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('housing_basic_services')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 9: LABOUR FORCE GENDER DIVIDE ================= -->
        <div class="vi-card col-6" id="card-lfs" data-category="living">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 09 / 16</span>
                <span class="vi-card-tag">Labour Market &bull; Gender &amp; Youth Deficit</span>
              </div>
              <h3 class="vi-card-title">#09: Labour Force Disparities: Gender &amp; Youth</h3>
              <p class="vi-card-subtitle">Economic participation gap, youth unemployment, and provincial wage differentials</p>
            </div>
            <div class="vi-card-controls">
              <button type="button" class="vi-ctrl-btn active" onclick="updateLfsMetric('participation')">Participation Gap</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateLfsMetric('unemployment')">Youth Joblessness</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateLfsMetric('wages')">Mean Wages</button>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-lfs" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-lfs">
            <strong>Key Policy Takeaway:</strong> Severe gender chasm: Male labor force participation stands at <strong>68.4% compared to only 21.6% for women</strong> (46.8% gap). Youth unemployment (age 15–24) reaches <strong>18.6% (24.3% for young women)</strong>.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Male LFPR: <strong>68.4%</strong></span>
              <span class="vi-kpi-pill">Female LFPR: <strong>21.6%</strong></span>
              <span class="vi-kpi-pill">Youth Unemp: <strong>18.6%</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Pakistan Bureau of Statistics</strong>, Labour Force Survey (LFS 2024–25) &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-lfs', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-lfs', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('lfs_employment_wages')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 10: MULTI-CENSUS PROVINCIAL POPULATION SHIFTS ================= -->
        <div class="vi-card col-6" id="card-census-shifts" data-category="demographics">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 10 / 16</span>
                <span class="vi-card-tag">Federal Demographics &bull; 4-Decade Census Shifts</span>
              </div>
              <h3 class="vi-card-title">#10: Multi-Census Provincial Population Shares (1981–2023)</h3>
              <p class="vi-card-subtitle">Decadal shifts in provincial demographic shares across 1981, 1998, 2017, and 2023 censuses</p>
            </div>
            <div class="vi-card-controls">
              <button type="button" class="vi-ctrl-btn active" onclick="updateCensusShiftYear('2023')">2023</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateCensusShiftYear('2017')">2017</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateCensusShiftYear('1998')">1998</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateCensusShiftYear('1981')">1981</button>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-census-shifts" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-census-shifts">
            <strong>Key Policy Takeaway:</strong> Significant federal rebalancing: <strong>Punjab's demographic share contracted by -3.2%</strong> (56.1% in 1981 to 52.9% in 2023), while <strong>Balochistan grew from 5.1% to 6.2% (14.89M)</strong> and KP reached 16.9% following the FATA merger.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Punjab Shift: <strong>56.1% &rarr; 52.9%</strong></span>
              <span class="vi-kpi-pill">Balochistan: <strong>5.1% &rarr; 6.2%</strong></span>
              <span class="vi-kpi-pill">KP + FATA: <strong>13.1% &rarr; 16.9%</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Pakistan Bureau of Statistics</strong>, Censuses of Pakistan (1981, 1998, 2017, 2023) &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-census-shifts', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-census-shifts', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('provincial_census_shifts')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 11: 135-DISTRICT QUADRANT SCATTER BUBBLE MAP ================= -->
        <div class="vi-card col-12" id="card-districts-scatter" data-category="demographics">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 11 / 16</span>
                <span class="vi-card-tag">Spatial Transition &bull; 135 Districts Scatter Matrix</span>
              </div>
              <h3 class="vi-card-title">#11: 135-District Urbanization &amp; Density Quadrant Scatter Bubble Map</h3>
              <p class="vi-card-subtitle">2D coordinate matrix: Urbanization Share (%) vs Density (people/km² on log scale) &bull; Bubble radius sized by total population</p>
            </div>
            <div class="vi-card-controls" style="align-items: center;">
              <input type="text" id="scatter-search-input" placeholder="Search District (e.g. Lahore, Quetta)..." oninput="filterScatterMap()" style="padding: 5px 10px; border: 1px solid var(--vi-line); border-radius: 6px; font-size: 12px; width: 220px;" />
              <button type="button" class="vi-ctrl-btn active" onclick="updateScatterProv('all')">All Districts</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateScatterProv('Punjab')">Punjab</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateScatterProv('Sindh')">Sindh</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateScatterProv('Khyber Pakhtunkhwa')">KP</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateScatterProv('Balochistan')">Balochistan</button>
            </div>
          </div>
          <div class="vi-chart-container" style="min-height: 440px;">
            <svg id="svg-card-districts-scatter" class="vi-chart-svg" viewBox="0 0 940 440" style="max-height: 480px;"></svg>
          </div>
          <div class="vi-callout" id="callout-card-districts-scatter">
            <strong>Key Policy Takeaway:</strong> Resolves the 0.0% data key bug and maps all 141 districts into four structural archetypes: <strong>Dense Metros</strong> (Karachi &gt;43,000/km², Lahore 7,294/km²), <strong>Dense Agrarian Hubs</strong> (Charsadda, Gujranwala peri-urban), <strong>Vast Arid Periphery</strong> (Chaghi 5.2/km², Washuk, Awaran), and <strong>Urbanized Frontier Outposts</strong> (Quetta 61.2% urban, Gwadar).
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Total Districts Plotted: <strong>141</strong></span>
              <span class="vi-kpi-pill">Dense Metros (&gt;70% Urban): <strong>14 Districts</strong></span>
              <span class="vi-kpi-pill">Deep Agrarian (&lt;15% Urban): <strong>42 Districts</strong></span>
              <span class="vi-kpi-pill">Hyper-Sparse (&lt;50/km²): <strong>26 Districts</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Pakistan Bureau of Statistics</strong>, 7th Population &amp; Housing Census 2023 Table 1 (141 Districts) &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-districts-scatter', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-districts-scatter', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('census_2023_districts')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 12: EMPLOYMENT BY SECTOR ================= -->
        <div class="vi-card col-6" id="card-sector-employment" data-category="living">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 12 / 16</span>
                <span class="vi-card-tag">Structural Transformation &bull; Sectoral Jobs</span>
              </div>
              <h3 class="vi-card-title">#12: Employment Distribution by Economic Sector</h3>
              <p class="vi-card-subtitle">Proportional workforce allocation across Agriculture, Industry &amp; Manufacturing, and Services</p>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-sector-employment" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-sector-employment">
            <strong>Key Policy Takeaway:</strong> Structural stagnation: <strong>Agriculture absorbs 37.4% of all employment nationwide (46.2% in Balochistan)</strong> while generating under 23% of GDP. Manufacturing and construction employ barely 25.4%, highlighting premature deindustrialization.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Agriculture: <strong>37.4% PK / 46.2% BA</strong></span>
              <span class="vi-kpi-pill">Industry: <strong>25.4% PK / 26.8% PB</strong></span>
              <span class="vi-kpi-pill">Services: <strong>37.2% PK / 41.4% SN</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Pakistan Bureau of Statistics</strong>, Labour Force Survey (LFS 2024–25) &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-sector-employment', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-sector-employment', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('lfs_employment_wages')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 13: PROVINCIAL AGRI SHIFTS ================= -->
        <div class="vi-card col-6" id="card-agri-shifts" data-category="agri">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 13 / 16</span>
                <span class="vi-card-tag">Agrarian Structure &bull; 2010 vs 2024 Census</span>
              </div>
              <h3 class="vi-card-title">#13: Agricultural Land &amp; Cultivated Acreage Shifts</h3>
              <p class="vi-card-subtitle">Farm fragmentation, provincial cultivated shares, and structural acreage changes</p>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-agri-shifts" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-agri-shifts">
            <strong>Key Policy Takeaway:</strong> Farm fragmentation crisis: <strong>Total farms surged +34.4% to 11.10 million</strong> while <strong>average farm size shrank from 6.4 to 5.3 acres</strong>. Punjab contains 64.2% of all cultivated land, followed by Sindh (21.8%), KP (8.6%), and Balochistan (5.4%).
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Total Farms: <strong>11.10 Million (+34.4%)</strong></span>
              <span class="vi-kpi-pill">Avg Farm Size: <strong>5.3 Acres (-17.2%)</strong></span>
              <span class="vi-kpi-pill">Fragmented Farms: <strong>+76.2%</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Pakistan Bureau of Statistics</strong>, 7th Agricultural Census 2024 &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-agri-shifts', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-agri-shifts', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('provincial_agri_shifts')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 14: 70-YEAR INTERCENSAL DEMOGRAPHIC GROWTH ================= -->
        <div class="vi-card col-6" id="card-census-hist" data-category="demographics">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 14 / 16</span>
                <span class="vi-card-tag">Demographic Trajectory &bull; 70-Year Census</span>
              </div>
              <h3 class="vi-card-title">#14: 70-Year Intercensal Demographic Growth (1951–2023)</h3>
              <p class="vi-card-subtitle">Seven census milestones and intercensal annual growth rate trajectory</p>
            </div>
          </div>
          <div class="vi-chart-container">
            <svg id="svg-card-census-hist" class="vi-chart-svg" viewBox="0 0 600 360"></svg>
          </div>
          <div class="vi-callout" id="callout-card-census-hist">
            <strong>Key Policy Takeaway:</strong> Pakistan multiplied <strong>7.2-fold in 72 years</strong> from 33.7 million in 1951 to 241.5 million in 2023. Annual growth currently stands at <strong>2.55%</strong>, adding over 6.1 million people annually.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">1951 Population: <strong>33.7M</strong></span>
              <span class="vi-kpi-pill">2023 Population: <strong>241.5M</strong></span>
              <span class="vi-kpi-pill">Intercensal Growth: <strong>2.55% p.a.</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Pakistan Bureau of Statistics</strong>, Censuses of Pakistan (1951–2023) &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-census-hist', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-census-hist', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('census_historical_growth')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 15: 35-YEAR MACROECONOMIC TRAJECTORY ================= -->
        <div class="vi-card col-12" id="card-macro" data-category="macro">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 15 / 16</span>
                <span class="vi-card-tag">Macroeconomic History &bull; 4 Structural Tenures</span>
              </div>
              <h3 class="vi-card-title">#15: 35-Year Macroeconomic Trajectory (1990–2024: 4 Historical Tenures &amp; Crisis Shocks)</h3>
              <p class="vi-card-subtitle">Demarcated across four distinct economic regimes: Structural Adjustment, Consumption Boom, BoP Shocks &amp; CPEC, and Stagflation/Stabilization</p>
            </div>
            <div class="vi-card-controls">
              <button type="button" class="vi-ctrl-btn active" onclick="updateMacroMetric('growth_infl')">GDP Growth vs Inflation</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateMacroMetric('deficits')">Fiscal vs Current Account</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateMacroMetric('debt_gdp')">Total Debt-to-GDP (%)</button>
            </div>
          </div>
          <div class="vi-chart-container" style="min-height: 420px;">
            <svg id="svg-card-macro" class="vi-chart-svg" viewBox="0 0 940 420" style="max-height: 460px;"></svg>
          </div>
          <div class="vi-callout" id="callout-card-macro">
            <strong>Key Policy Takeaway:</strong> Pakistan experiences a recurring balance of payments crisis every 4 to 6 years. Inflation reached a historic <strong>50-year peak of 30.8% in 2023</strong> following post-COVID supply chain disruptions, currency depreciation, and the devastating 2022 super floods.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">Peak Inflation: <strong>30.8% (2023)</strong></span>
              <span class="vi-kpi-pill">COVID Contraction: <strong>-0.94% (2020)</strong></span>
              <span class="vi-kpi-pill">Peak Growth: <strong>7.7% (2005)</strong></span>
              <span class="vi-kpi-pill">Current Debt/GDP: <strong>74.8%</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>World Bank WDI &amp; Ministry of Finance</strong>, Economic Surveys (1990–2024) &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-macro', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-macro', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('macro_indicators_timeseries')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

        <!-- ================= CARD 16: PROVINCIAL RESOURCE ALLOCATION, DEBT & CONFLICT MATRIX ================= -->
        <div class="vi-card col-12" id="card-prov-matrix" data-category="fiscal">
          <div class="vi-card-accent"></div>
          <div class="vi-card-header">
            <div>
              <div class="vi-header-meta">
                <span class="vi-number-badge">INFOGRAPHIC 16 / 16</span>
                <span class="vi-card-tag">Provincial Fiscal &amp; Security Disparities &bull; 4 Provinces Multi-Dimensional Comparison</span>
              </div>
              <h3 class="vi-card-title">#16: Provincial Resource Allocation, Debt Stock &amp; Conflict Exposure Matrix (FY25 &amp; 2023–2024)</h3>
              <p class="vi-card-subtitle">Cross-provincial comparison of total budgetary outlay, Annual Development Programmes (ADP), outstanding public debt, per capita allocations, and regional terrorism burden</p>
            </div>
            <div class="vi-card-controls">
              <button type="button" class="vi-ctrl-btn active" onclick="updateProvMatrixView('budget_dev')">Total Budget vs Development ADP</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateProvMatrixView('debt_stock')">Public Debt &amp; Borrowing Stock</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateProvMatrixView('conflict_burden')">Conflict &amp; Terrorism Burden (CRSS)</button>
              <button type="button" class="vi-ctrl-btn" onclick="updateProvMatrixView('per_capita')">Per Capita vs Territorial Density (km²)</button>
            </div>
          </div>
          <div class="vi-chart-container" style="min-height: 440px;">
            <svg id="svg-card-prov-matrix" class="vi-chart-svg" viewBox="0 0 940 440" style="max-height: 480px;"></svg>
          </div>
          <div class="vi-callout" id="callout-card-prov-matrix">
            <strong>Key Policy Takeaway:</strong> Severe structural disparities exist between fiscal concentration and conflict exposure: <strong>Punjab and Sindh command 75.9%</strong> of all provincial budget spending, while <strong>Khyber Pakhtunkhwa (63.1%) and Balochistan (29.1%) bear 92.2% of Pakistan's terrorism fatalities</strong>. Furthermore, while Balochistan receives the highest nominal budget per person (PKR 64,158), its infrastructure allocation per km² (PKR 0.92M/km²) is less than one-seventh of Sindh's (PKR 6.81M/km²), reflecting severe territorial underdevelopment.
            <div class="vi-kpis">
              <span class="vi-kpi-pill">National Total Outlay: <strong>PKR 11.21 Trillion</strong></span>
              <span class="vi-kpi-pill">Total Prov Development: <strong>PKR 2.54 Trillion</strong></span>
              <span class="vi-kpi-pill">KP + Balochistan Conflict Share: <strong>92.2% Fatalities</strong></span>
              <span class="vi-kpi-pill">Highest Debt Stock: <strong>Punjab (PKR 1.685T)</strong></span>
            </div>
          </div>
          <div class="vi-card-footer">
            <div class="vi-source">Source: <strong>Provincial Finance Departments</strong> (White Papers FY25), <strong>DMU Debt Bulletins</strong>, <strong>CRSS Annual Security Reports (2023–24)</strong> &bull; <strong>PPRI</strong></div>
            <div class="vi-actions">
              <button type="button" class="vi-btn vi-btn-primary" onclick="exportCard('card-prov-matrix', 'png')">&#x1F4F7; Download Image (PNG)</button>
              <button type="button" class="vi-btn" onclick="exportCard('card-prov-matrix', 'svg')">&#x1F4D0; SVG</button>
              <button type="button" class="vi-btn" onclick="exportCSV('provincial_fiscal_conflict_matrix')">&#x1F4CA; CSV</button>
            </div>
          </div>
        </div>

      </div>
    </main>

    <!-- Hidden Offscreen Canvas for Retina PNG Export -->
    <canvas id="vi-export-canvas" style="display:none;"></canvas>

    <!-- Tooltip Element -->
    <div id="vi-tooltip"></div>

    <!-- Notification Toast -->
    <div id="vi-toast"></div>

    <!-- SCRIPTS -->
    <script>
      (function() {
        'use strict';

        // 1. EMBEDDED ZERO-NETWORK IN-MEMORY REPOSITORIES (134 KB Total)
        const EMBEDDED_DATA = ''' + embedded_json + r''';

        const db = {
          fiscal: EMBEDDED_DATA.fiscal || [],
          debt: EMBEDDED_DATA.debt || [],
          tax_exp: EMBEDDED_DATA.tax_exp || [],
          gender_land: EMBEDDED_DATA.gender_land || [],
          hies: EMBEDDED_DATA.hies || [],
          consumption: EMBEDDED_DATA.consumption || [],
          wage_infl: EMBEDDED_DATA.wage_infl || [],
          services: EMBEDDED_DATA.services || [],
          lfs: EMBEDDED_DATA.lfs || [],
          census_shifts: EMBEDDED_DATA.census_shifts || [],
          districts: EMBEDDED_DATA.districts || [],
          agri_shifts: EMBEDDED_DATA.agri_shifts || [],
          census_hist: EMBEDDED_DATA.census_hist || [],
          macro: EMBEDDED_DATA.macro || [],
          prov_matrix: EMBEDDED_DATA.prov_matrix || []
        };

        // UI States
        let activeFiscalFY = '2025-26';
        let activeDebtView = 'stacked';
        let activeGenderLandProv = 'PK';
        let activeHiesDomain = 'Total';
        let activeConsumptionProv = 'PK';
        let activeServicesProv = 'PK';
        let activeLfsMetric = 'participation';
        let activeCensusShiftYear = '2023';
        let activeScatterProv = 'all';
        let activeScatterSearch = '';
        let activeMacroMetric = 'growth_infl';
        let activeProvMatrixView = 'budget_dev';

        // Defensive Formatting Helper
        const fmt = (v) => (typeof v === 'number' ? v.toLocaleString() : (v || '0'));

        // Tooltip Helper
        const tooltip = document.getElementById('vi-tooltip');
        window.showTooltip = function(e, html) {
          const ev = e || window.event;
          if (!ev || !tooltip) return;
          tooltip.innerHTML = html;
          tooltip.style.display = 'block';
          tooltip.style.left = (ev.clientX + 14) + 'px';
          tooltip.style.top = (ev.clientY + 14) + 'px';
        };
        window.hideTooltip = function() {
          if (tooltip) tooltip.style.display = 'none';
        };

        // Toast Helper
        function showToast(msg) {
          const toast = document.getElementById('vi-toast');
          if (!toast) return;
          toast.innerText = msg;
          toast.style.display = 'block';
          setTimeout(() => { toast.style.display = 'none'; }, 3500);
        }

        // Category Filter
        window.filterGallery = function(category) {
          const buttons = document.querySelectorAll('.vi-filter-btn');
          buttons.forEach(b => b.classList.remove('active'));
          if (window.event && window.event.target) {
            window.event.target.classList.add('active');
          }

          const cards = document.querySelectorAll('.vi-card');
          cards.forEach(c => {
            if (category === 'all' || c.getAttribute('data-category') === category) {
              c.style.display = 'flex';
            } else {
              c.style.display = 'none';
            }
          });
        };

        // ================= CARD 1: FISCAL EXPENDITURES (100% COMPLETE RING) =================
        window.updateFiscalFY = function(fy) {
          activeFiscalFY = fy;
          const btns = document.querySelectorAll('#card-fiscal .vi-ctrl-btn');
          btns.forEach(b => b.classList.toggle('active', b.innerText.includes(fy)));
          renderCard1Fiscal();
        };

        function renderCard1Fiscal() {
          const svg = document.getElementById('svg-card-fiscal');
          if (!svg) return;
          const row = db.fiscal.find(r => r.fiscal_year === activeFiscalFY) || db.fiscal[2] || {
            debt_servicing_interest_pkr_b: 9775, defence_services_pkr_b: 2122, federal_psdp_development_pkr_b: 1400,
            civil_administration_pkr_b: 839, pensions_pkr_b: 1014, subsidies_pkr_b: 1363, total_federal_expenditure_pkr_b: 18877
          };

          const total = row.total_federal_expenditure_pkr_b || 18877;
          const knownSum = (row.debt_servicing_interest_pkr_b || 9775) +
                           (row.defence_services_pkr_b || 2122) +
                           (row.federal_psdp_development_pkr_b || 1400) +
                           (row.civil_administration_pkr_b || 839) +
                           (row.subsidies_pkr_b || 1363) +
                           (row.pensions_pkr_b || 1014);
          const otherVal = Math.max(0, total - knownSum);

          // 7 Slices summing to exactly 100.0% of total budget
          const slices = [
            { label: 'Debt Markup', val: row.debt_servicing_interest_pkr_b || 9775, col: '#e11d48' },
            { label: 'Defence', val: row.defence_services_pkr_b || 2122, col: '#0f766e' },
            { label: 'PSDP Dev', val: row.federal_psdp_development_pkr_b || 1400, col: '#0284c7' },
            { label: 'Civil Admin', val: row.civil_administration_pkr_b || 839, col: '#d97706' },
            { label: 'Subsidies', val: row.subsidies_pkr_b || 1363, col: '#15803d' },
            { label: 'Pensions', val: row.pensions_pkr_b || 1014, col: '#7c3aed' },
            { label: 'Grants & Other', val: otherVal, col: '#64748b' }
          ];

          let cumAngle = -Math.PI / 2;
          const cx = 145, cy = 180, r = 110, innerR = 65;
          let paths = '';

          slices.forEach(s => {
            const angle = (s.val / total) * Math.PI * 2;
            const x1 = cx + r * Math.cos(cumAngle);
            const y1 = cy + r * Math.sin(cumAngle);
            const x2 = cx + r * Math.cos(cumAngle + angle);
            const y2 = cy + r * Math.sin(cumAngle + angle);
            const ix1 = cx + innerR * Math.cos(cumAngle + angle);
            const iy1 = cy + innerR * Math.sin(cumAngle + angle);
            const ix2 = cx + innerR * Math.cos(cumAngle);
            const iy2 = cy + innerR * Math.sin(cumAngle);
            const largeArc = angle > Math.PI ? 1 : 0;

            const d = `M ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} L ${ix1} ${iy1} A ${innerR} ${innerR} 0 ${largeArc} 0 ${ix2} ${iy2} Z`;
            const pct = ((s.val / total) * 100).toFixed(1);

            paths += `<path d="${d}" fill="${s.col}" stroke="#ffffff" stroke-width="2"
              onmouseenter="showTooltip(event, '<strong>${s.label}</strong><br/>PKR ${fmt(s.val)} Billion (${pct}%)')"
              onmousemove="showTooltip(event, '<strong>${s.label}</strong><br/>PKR ${fmt(s.val)} Billion (${pct}%)')"
              onmouseleave="hideTooltip()" style="cursor:pointer; transition: opacity 0.2s;"></path>`;
            cumAngle += angle;
          });

          // Horizontal Bars on right side (7 items cleanly spaced)
          let barHtml = '';
          const barX = 295, startY = 32, barW = 265;
          slices.forEach((s, idx) => {
            const y = startY + idx * 43;
            const pct = ((s.val / total) * 100).toFixed(1);
            const w = (s.val / total) * barW;
            barHtml += `
              <text x="${barX}" y="${y}" font-size="11.5" font-weight="700" fill="#0f172a">${s.label}</text>
              <text x="${barX + barW}" y="${y}" font-size="11.5" font-weight="700" fill="${s.col}" text-anchor="end">PKR ${fmt(s.val)}B (${pct}%)</text>
              <rect x="${barX}" y="${y + 5}" width="${barW}" height="12" fill="#f1f5f9" rx="3" />
              <rect x="${barX}" y="${y + 5}" width="${Math.max(w, 4)}" height="12" fill="${s.col}" rx="3" />
            `;
          });

          svg.innerHTML = `
            ${paths}
            <circle cx="${cx}" cy="${cy}" r="${innerR}" fill="#ffffff" />
            <text x="${cx}" y="${cy - 8}" text-anchor="middle" font-size="10.5" font-weight="700" fill="#64748b">TOTAL 100%</text>
            <text x="${cx}" y="${cy + 13}" text-anchor="middle" font-size="14" font-weight="800" fill="#073c3a">PKR ${Math.round(total/1000)}T</text>
            <text x="${cx}" y="${cy + 26}" text-anchor="middle" font-size="9.5" font-weight="600" fill="#0f766e">${activeFiscalFY}</text>
            ${barHtml}
          `;
        }

        // ================= CARD 2: PUBLIC DEBT (TOTALS ON ALL 9 BARS) =================
        window.updateDebtView = function(view) {
          activeDebtView = view;
          const btns = document.querySelectorAll('#card-debt .vi-ctrl-btn');
          btns[0].classList.toggle('active', view === 'stacked');
          btns[1].classList.toggle('active', view === 'servicing');
          renderCard2Debt();
        };

        function renderCard2Debt() {
          const svg = document.getElementById('svg-card-debt');
          if (!svg || !db.debt.length) return;

          const w = 550, h = 250, padX = 50, padY = 45;
          const maxDebt = 90000;
          const maxServicing = 11000;
          const colW = (w - padX) / db.debt.length;

          let elements = '';
          elements += `<line x1="${padX}" y1="${h + padY}" x2="${w + 20}" y2="${h + padY}" stroke="#cbd5e1" stroke-width="1.5" />`;

          if (activeDebtView === 'stacked') {
            db.debt.forEach((d, idx) => {
              const x = padX + idx * colW + colW * 0.12;
              const barWidth = colW * 0.76;
              const hDom = (d.domestic_debt_pkr_b / maxDebt) * h;
              const hExt = (d.external_debt_pkr_b / maxDebt) * h;
              const yExt = h + padY - hExt;
              const yDom = yExt - hDom;

              const extPct = ((d.external_debt_pkr_b / d.total_public_debt_pkr_b) * 100).toFixed(1);
              const domPct = ((d.domestic_debt_pkr_b / d.total_public_debt_pkr_b) * 100).toFixed(1);
              const totalStr = (d.total_public_debt_pkr_b / 1000).toFixed(1) + 'T';

              elements += `
                <rect x="${x}" y="${yExt}" width="${barWidth}" height="${hExt}" fill="#d97706" rx="2"
                  onmouseenter="showTooltip(event, '<strong>${d.fiscal_year} External Debt</strong><br/>PKR ${fmt(d.external_debt_pkr_b)} Billion (${extPct}%)')"
                  onmousemove="showTooltip(event, '<strong>${d.fiscal_year} External Debt</strong><br/>PKR ${fmt(d.external_debt_pkr_b)} Billion (${extPct}%)')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <rect x="${x}" y="${yDom}" width="${barWidth}" height="${hDom}" fill="#0f766e" rx="2"
                  onmouseenter="showTooltip(event, '<strong>${d.fiscal_year} Domestic Debt</strong><br/>PKR ${fmt(d.domestic_debt_pkr_b)} Billion (${domPct}%)')"
                  onmousemove="showTooltip(event, '<strong>${d.fiscal_year} Domestic Debt</strong><br/>PKR ${fmt(d.domestic_debt_pkr_b)} Billion (${domPct}%)')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${x + barWidth/2}" y="${h + padY + 16}" text-anchor="middle" font-size="10.5" fill="#64748b" font-weight="600">${d.fiscal_year.replace('FY', '')}</text>
                <!-- Render total above EVERY SINGLE bar -->
                <text x="${x + barWidth/2}" y="${yDom - 5}" text-anchor="middle" font-size="8.5" font-weight="800" fill="#073c3a">${totalStr}</text>
              `;
            });

            elements += `
              <g transform="translate(180, 15)">
                <rect x="0" y="0" width="12" height="12" fill="#0f766e" rx="2" />
                <text x="18" y="10" font-size="11" font-weight="600" fill="#334155">Domestic Debt (PKR 57.6T / 69%)</text>
                <rect x="230" y="0" width="12" height="12" fill="#d97706" rx="2" />
                <text x="248" y="10" font-size="11" font-weight="600" fill="#334155">External Debt (PKR 25.7T / 31%)</text>
              </g>
            `;
          } else {
            db.debt.forEach((d, idx) => {
              const x = padX + idx * colW + colW * 0.16;
              const barWidth = colW * 0.68;
              const val = d.debt_servicing_markup_pkr_b || 0;
              const barH = (val / maxServicing) * h;
              const y = h + padY - barH;

              elements += `
                <rect x="${x}" y="${y}" width="${barWidth}" height="${barH}" fill="#e11d48" rx="3"
                  onmouseenter="showTooltip(event, '<strong>${d.fiscal_year} Markup Servicing</strong><br/>PKR ${fmt(val)} Billion')"
                  onmousemove="showTooltip(event, '<strong>${d.fiscal_year} Markup Servicing</strong><br/>PKR ${fmt(val)} Billion')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${x + barWidth/2}" y="${y - 6}" text-anchor="middle" font-size="9" font-weight="800" fill="#e11d48">PKR ${Math.round(val)}B</text>
                <text x="${x + barWidth/2}" y="${h + padY + 16}" text-anchor="middle" font-size="10.5" fill="#64748b" font-weight="600">${d.fiscal_year.replace('FY', '')}</text>
              `;
            });

            elements += `
              <text x="300" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#e11d48">
                Annual Interest / Markup Servicing Escalation: 6.5x Increase (FY18–FY26)
              </text>
            `;
          }

          svg.innerHTML = elements;
        }

        // ================= CARD 3: TAX EXPENDITURES (VALID SVG TSPAN) =================
        function renderCard3TaxExp() {
          const svg = document.getElementById('svg-card-tax-exp');
          if (!svg) return;

          const totalLoss = 2434.73;
          const slices = [
            { label: 'Sales Tax Exemptions', val: 1237.11, pct: 50.81, col: '#0f766e' },
            { label: 'Customs Concessions', val: 652.39, pct: 26.80, col: '#d97706' },
            { label: 'Income Tax Relief', val: 545.23, pct: 22.39, col: '#e11d48' }
          ];

          let cumAngle = -Math.PI / 2;
          const cx = 145, cy = 180, r = 110, innerR = 65;
          let paths = '';

          slices.forEach(s => {
            const angle = (s.val / totalLoss) * Math.PI * 2;
            const x1 = cx + r * Math.cos(cumAngle);
            const y1 = cy + r * Math.sin(cumAngle);
            const x2 = cx + r * Math.cos(cumAngle + angle);
            const y2 = cy + r * Math.sin(cumAngle + angle);
            const ix1 = cx + innerR * Math.cos(cumAngle + angle);
            const iy1 = cy + innerR * Math.sin(cumAngle + angle);
            const ix2 = cx + innerR * Math.cos(cumAngle);
            const iy2 = cy + innerR * Math.sin(cumAngle);
            const largeArc = angle > Math.PI ? 1 : 0;

            const d = `M ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} L ${ix1} ${iy1} A ${innerR} ${innerR} 0 ${largeArc} 0 ${ix2} ${iy2} Z`;

            paths += `<path d="${d}" fill="${s.col}" stroke="#ffffff" stroke-width="2"
              onmouseenter="showTooltip(event, '<strong>${s.label}</strong><br/>PKR ${fmt(s.val)} Billion (${s.pct}%)')"
              onmousemove="showTooltip(event, '<strong>${s.label}</strong><br/>PKR ${fmt(s.val)} Billion (${s.pct}%)')"
              onmouseleave="hideTooltip()" style="cursor:pointer;" />`;
            cumAngle += angle;
          });

          // Right Column with pure valid SVG tags (<tspan font-weight="700"> instead of HTML <strong>)
          let rightHtml = `
            <g transform="translate(300, 45)">
              <text x="0" y="0" font-size="13" font-weight="700" fill="#073c3a">Revenue Foregone vs Collection</text>

              <text x="0" y="30" font-size="11.5" font-weight="600" fill="#334155">Total Foregone Tax (PKR 2,435B)</text>
              <rect x="0" y="38" width="245" height="18" fill="#e11d48" rx="4" />
              <text x="250" y="52" font-size="11" font-weight="700" fill="#e11d48">26.2%</text>

              <text x="0" y="84" font-size="11.5" font-weight="600" fill="#334155">Net Tax Collected (PKR 9,300B)</text>
              <rect x="0" y="92" width="245" height="18" fill="#0f766e" rx="4" />
              <text x="250" y="106" font-size="11" font-weight="700" fill="#0f766e">100%</text>

              <text x="0" y="142" font-size="12" font-weight="700" fill="#073c3a">Breakdown of Tax Concessions</text>

              <!-- Entry 1: Sales Tax (Green) -->
              <rect x="0" y="156" width="12" height="12" fill="#0f766e" rx="2" />
              <text x="18" y="166" font-size="11" fill="#475569">Sales Tax (6th Sched): <tspan font-weight="700" fill="#0f766e">PKR 1,237.1B (50.8%)</tspan></text>

              <!-- Entry 2: Customs (Yellow) -->
              <rect x="0" y="186" width="12" height="12" fill="#d97706" rx="2" />
              <text x="18" y="196" font-size="11" fill="#475569">Customs (5th Sched): <tspan font-weight="700" fill="#d97706">PKR 652.4B (26.8%)</tspan></text>

              <!-- Entry 3: Income Tax (Red) -->
              <rect x="0" y="216" width="12" height="12" fill="#e11d48" rx="2" />
              <text x="18" y="226" font-size="11" fill="#475569">Income Tax (2nd Sched): <tspan font-weight="700" fill="#e11d48">PKR 545.2B (22.4%)</tspan></text>
            </g>
          `;

          svg.innerHTML = `
            ${paths}
            <circle cx="${cx}" cy="${cy}" r="${innerR}" fill="#ffffff" />
            <text x="${cx}" y="${cy - 8}" text-anchor="middle" font-size="10.5" font-weight="600" fill="#64748b">TAX REVENUE FOREGONE</text>
            <text x="${cx}" y="${cy + 14}" text-anchor="middle" font-size="15" font-weight="800" fill="#e11d48">PKR 2.43T</text>
            <text x="${cx}" y="${cy + 28}" text-anchor="middle" font-size="10" font-weight="600" fill="#073c3a">2.32% OF GDP</text>
            ${rightHtml}
          `;
        }

        // ================= CARD 4: PROVINCIAL GENDER & LAND (NO OVERLAPS) =================
        window.updateGenderLandProv = function(provId) {
          activeGenderLandProv = provId;
          const btns = document.querySelectorAll('#card-gender-land .vi-ctrl-btn');
          btns.forEach(b => {
            const isMatch = (provId === 'PK' && b.innerText === 'National') ||
                            (provId === 'PK-PB' && b.innerText === 'Punjab') ||
                            (provId === 'PK-SN' && b.innerText === 'Sindh') ||
                            (provId === 'PK-KP' && b.innerText === 'KP') ||
                            (provId === 'PK-BA' && b.innerText === 'Balochistan');
            b.classList.toggle('active', isMatch);
          });
          renderCard4GenderLand();
        };

        function renderCard4GenderLand() {
          const svg = document.getElementById('svg-card-gender-land');
          if (!svg || !db.gender_land.length) return;

          const activeRow = db.gender_land.find(r => r.geography_id === activeGenderLandProv) || db.gender_land[0];
          const mPct = activeRow.male_share_pct || 51.48;
          const fPct = activeRow.female_share_pct || 48.51;
          const tPct = activeRow.transgender_share_pct || 0.01;
          const totalPop = activeRow.population_2023 || 241499431;

          const cx = 125, cy = 160, r = 90, innerR = 52;
          let cumAngle = -Math.PI / 2;
          const slices = [
            { label: 'Male', pct: mPct, count: activeRow.population_male, col: '#073c3a' },
            { label: 'Female', pct: fPct, count: activeRow.population_female, col: '#0f766e' },
            { label: 'Transgender', pct: tPct, count: activeRow.population_transgender, col: '#7c3aed' }
          ];

          let paths = '';
          slices.forEach(s => {
            const angle = (s.pct / 100) * Math.PI * 2;
            const x1 = cx + r * Math.cos(cumAngle);
            const y1 = cy + r * Math.sin(cumAngle);
            const x2 = cx + r * Math.cos(cumAngle + angle);
            const y2 = cy + r * Math.sin(cumAngle + angle);
            const ix1 = cx + innerR * Math.cos(cumAngle + angle);
            const iy1 = cy + innerR * Math.sin(cumAngle + angle);
            const ix2 = cx + innerR * Math.cos(cumAngle);
            const iy2 = cy + innerR * Math.sin(cumAngle);
            const largeArc = angle > Math.PI ? 1 : 0;

            const d = `M ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} L ${ix1} ${iy1} A ${innerR} ${innerR} 0 ${largeArc} 0 ${ix2} ${iy2} Z`;

            paths += `<path d="${d}" fill="${s.col}" stroke="#ffffff" stroke-width="2"
              onmouseenter="showTooltip(event, '<strong>${s.label} (${activeRow.geography_name})</strong><br/>Headcount: ${fmt(s.count)}<br/>Share: ${s.pct.toFixed(2)}%')"
              onmousemove="showTooltip(event, '<strong>${s.label} (${activeRow.geography_name})</strong><br/>Headcount: ${fmt(s.count)}<br/>Share: ${s.pct.toFixed(2)}%')"
              onmouseleave="hideTooltip()" style="cursor:pointer;" />`;
            cumAngle += angle;
          });

          // Right Column: Province Names get full 135px width, bars start at x=140 with dedicated columns
          let rightHtml = `
            <g transform="translate(250, 25)">
              <text x="0" y="0" font-size="12" font-weight="700" fill="#073c3a">Territorial Land Area vs Population Share Asymmetry</text>
              <text x="0" y="15" font-size="10.5" fill="#64748b">Comparison across 4 Provinces &amp; ICT (Census 2023)</text>
          `;

          const provRows = db.gender_land.filter(r => r.geography_id !== 'PK');
          const maxBarW = 125;
          provRows.forEach((pr, idx) => {
            const y = 32 + idx * 48;
            const landW = (pr.land_area_share_pct / 50) * maxBarW;
            const popW = (pr.population_share_pct / 55) * maxBarW;

            rightHtml += `
              <!-- Province Name with Density placed cleanly underneath to prevent collisions -->
              <text x="0" y="${y + 9}" font-size="11" font-weight="700" fill="#1e293b">${pr.geography_name}</text>
              <text x="0" y="${y + 20}" font-size="9" font-weight="600" fill="#64748b">${pr.density_per_sqkm} / km²</text>

              <!-- Land Area Bar -->
              <rect x="135" y="${y}" width="${maxBarW}" height="8" fill="#f1f5f9" rx="2" />
              <rect x="135" y="${y}" width="${landW}" height="8" fill="#d97706" rx="2"
                onmouseenter="showTooltip(event, '<strong>${pr.geography_name} Land Area</strong><br/>${fmt(pr.area_sqkm)} km² (${pr.land_area_share_pct}%)')"
                onmousemove="showTooltip(event, '<strong>${pr.geography_name} Land Area</strong><br/>${fmt(pr.area_sqkm)} km² (${pr.land_area_share_pct}%)')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />
              <text x="${135 + landW + 6}" y="${y + 7}" font-size="8.5" font-weight="700" fill="#d97706">${pr.land_area_share_pct}% Land</text>

              <!-- Population Bar -->
              <rect x="135" y="${y + 11}" width="${maxBarW}" height="8" fill="#f1f5f9" rx="2" />
              <rect x="135" y="${y + 11}" width="${popW}" height="8" fill="#0f766e" rx="2"
                onmouseenter="showTooltip(event, '<strong>${pr.geography_name} Population</strong><br/>${fmt(pr.population_2023)} (${pr.population_share_pct}%)')"
                onmousemove="showTooltip(event, '<strong>${pr.geography_name} Population</strong><br/>${fmt(pr.population_2023)} (${pr.population_share_pct}%)')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />
              <text x="${135 + popW + 6}" y="${y + 18}" font-size="8.5" font-weight="700" fill="#0f766e">${pr.population_share_pct}% Pop</text>
            `;
          });

          rightHtml += `
            <g transform="translate(60, 280)">
              <rect x="0" y="0" width="10" height="10" fill="#d97706" rx="2" />
              <text x="14" y="9" font-size="10.5" font-weight="600" fill="#334155">Land Share (%)</text>
              <rect x="125" y="0" width="10" height="10" fill="#0f766e" rx="2" />
              <text x="139" y="9" font-size="10.5" font-weight="600" fill="#334155">Pop Share (%)</text>
            </g>
          </g>`;

          svg.innerHTML = `
            ${paths}
            <circle cx="${cx}" cy="${cy}" r="${innerR}" fill="#ffffff" />
            <text x="${cx}" y="${cy - 12}" text-anchor="middle" font-size="9" font-weight="700" fill="#64748b">${activeRow.geography_name.toUpperCase()}</text>
            <text x="${cx}" y="${cy + 4}" text-anchor="middle" font-size="13" font-weight="800" fill="#073c3a">${(totalPop/1000000).toFixed(1)}M</text>
            <text x="${cx}" y="${cy + 18}" text-anchor="middle" font-size="9" font-weight="600" fill="#0f766e">Ratio: ${activeRow.sex_ratio}</text>

            <g transform="translate(10, 285)">
              <rect x="0" y="0" width="9" height="9" fill="#073c3a" rx="2" />
              <text x="12" y="8" font-size="9.5" fill="#334155">M: ${mPct.toFixed(1)}%</text>
              <rect x="75" y="0" width="9" height="9" fill="#0f766e" rx="2" />
              <text x="87" y="8" font-size="9.5" fill="#334155">F: ${fPct.toFixed(1)}%</text>
              <rect x="150" y="0" width="9" height="9" fill="#7c3aed" rx="2" />
              <text x="162" y="8" font-size="9.5" fill="#334155">Trans: ${fmt(activeRow.population_transgender)}</text>
            </g>

            ${rightHtml}
          `;
        }

        // ================= CARD 5: HIES FOOD BURDEN =================
        window.updateHiesDomain = function(domain) {
          activeHiesDomain = domain;
          const btns = document.querySelectorAll('#card-hies .vi-ctrl-btn');
          btns.forEach(b => b.classList.toggle('active', b.innerText === domain));
          renderCard5Hies();
        };

        function renderCard5Hies() {
          const svg = document.getElementById('svg-card-hies');
          if (!svg || !db.hies.length) return;

          const rows = db.hies.filter(r => r.domain === activeHiesDomain);
          rows.sort((a, b) => (b.food_expenditure_share_pct || 0) - (a.food_expenditure_share_pct || 0));

          let elements = '';
          const startY = 40, barW = 370, padX = 145;

          rows.forEach((r, idx) => {
            const y = startY + idx * 48;
            const pct = r.food_expenditure_share_pct || 0;
            const w = (pct / 50) * barW;
            const color = pct > 42 ? '#e11d48' : (pct > 35 ? '#d97706' : '#0f766e');
            const geoName = r.geography_name || 'Pakistan';
            const avgExp = r.average_monthly_household_consumption_pkr || 60000;

            elements += `
              <text x="${padX - 12}" y="${y + 14}" text-anchor="end" font-size="12" font-weight="700" fill="#1e293b">${geoName}</text>
              <rect x="${padX}" y="${y}" width="${barW}" height="20" fill="#f1f5f9" rx="4" />
              <rect x="${padX}" y="${y}" width="${w}" height="20" fill="${color}" rx="4"
                onmouseenter="showTooltip(event, '<strong>${geoName} (${r.domain})</strong><br/>Food Share: ${pct}%<br/>Avg Monthly Household Spend: PKR ${fmt(avgExp)}')"
                onmousemove="showTooltip(event, '<strong>${geoName} (${r.domain})</strong><br/>Food Share: ${pct}%<br/>Avg Monthly Household Spend: PKR ${fmt(avgExp)}')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />
              <text x="${padX + w + 8}" y="${y + 14}" font-size="12" font-weight="800" fill="${color}">${pct}%</text>
            `;
          });

          const vulnX = padX + (35 / 50) * barW;
          elements += `
            <line x1="${vulnX}" y1="25" x2="${vulnX}" y2="${startY + rows.length * 48}" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5" />
            <text x="${vulnX}" y="20" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b">Engel's 35% Vulnerability Threshold</text>
          `;

          svg.innerHTML = elements;
        }

        // ================= CARD 6: PROVINCIAL CONSUMPTION PIES (WIDE GUTTER) =================
        window.updateConsumptionProv = function(provId) {
          activeConsumptionProv = provId;
          const btns = document.querySelectorAll('#card-consumption-pie .vi-ctrl-btn');
          btns.forEach(b => {
            const isMatch = (provId === 'PK' && b.innerText === 'Pakistan') ||
                            (provId === 'PK-PB' && b.innerText === 'Punjab') ||
                            (provId === 'PK-SN' && b.innerText === 'Sindh') ||
                            (provId === 'PK-KP' && b.innerText === 'KP') ||
                            (provId === 'PK-BA' && b.innerText === 'Balochistan');
            b.classList.toggle('active', isMatch);
          });
          renderCard6ConsumptionPie();
        };

        function renderCard6ConsumptionPie() {
          const svg = document.getElementById('svg-card-consumption-pie');
          if (!svg || !db.consumption.length) return;

          const row = db.consumption.find(r => r.geography_id === activeConsumptionProv) || db.consumption[0];
          const slices = [
            { label: 'Food & Staples', pct: row.food_pct || 36.8, col: '#0f766e' },
            { label: 'Housing & Energy', pct: row.housing_utilities_pct || 22.4, col: '#d97706' },
            { label: 'Clothing & Footwear', pct: row.clothing_other_pct || 17.4, col: '#64748b' },
            { label: 'Transport & Comm', pct: row.transport_comm_pct || 11.2, col: '#0284c7' },
            { label: 'Health Care', pct: row.health_pct || 6.8, col: '#e11d48' },
            { label: 'Education', pct: row.education_pct || 5.4, col: '#7c3aed' }
          ];

          const cx = 135, cy = 160, r = 95, innerR = 55;
          let cumAngle = -Math.PI / 2;
          let paths = '';

          slices.forEach(s => {
            const angle = (s.pct / 100) * Math.PI * 2;
            const x1 = cx + r * Math.cos(cumAngle);
            const y1 = cy + r * Math.sin(cumAngle);
            const x2 = cx + r * Math.cos(cumAngle + angle);
            const y2 = cy + r * Math.sin(cumAngle + angle);
            const ix1 = cx + innerR * Math.cos(cumAngle + angle);
            const iy1 = cy + innerR * Math.sin(cumAngle + angle);
            const ix2 = cx + innerR * Math.cos(cumAngle);
            const iy2 = cy + innerR * Math.sin(cumAngle);
            const largeArc = angle > Math.PI ? 1 : 0;

            const d = `M ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} L ${ix1} ${iy1} A ${innerR} ${innerR} 0 ${largeArc} 0 ${ix2} ${iy2} Z`;

            paths += `<path d="${d}" fill="${s.col}" stroke="#ffffff" stroke-width="2"
              onmouseenter="showTooltip(event, '<strong>${s.label} (${row.geography_name})</strong><br/>Budget Allocation: ${s.pct}%')"
              onmousemove="showTooltip(event, '<strong>${s.label} (${row.geography_name})</strong><br/>Budget Allocation: ${s.pct}%')"
              onmouseleave="hideTooltip()" style="cursor:pointer;" />`;
            cumAngle += angle;
          });

          // Shift bars to x=135 so Khyber Pakhtunkhwa has full 130px clearance
          let rightHtml = `
            <g transform="translate(265, 30)">
              <text x="0" y="0" font-size="12" font-weight="700" fill="#073c3a">Mean Monthly Household Spending by Province</text>
              <text x="0" y="16" font-size="10.5" fill="#64748b">Average household budget in PKR (HIES 2024–25)</text>
          `;

          const allProvs = db.consumption.slice().sort((a,b) => b.mean_monthly_expenditure_pkr - a.mean_monthly_expenditure_pkr);
          const barW = 125;
          allProvs.forEach((pr, idx) => {
            const y = 35 + idx * 40;
            const w = (pr.mean_monthly_expenditure_pkr / 120000) * barW;
            const isCur = pr.geography_id === activeConsumptionProv;

            rightHtml += `
              <text x="0" y="${y + 12}" font-size="11" font-weight="${isCur ? '800' : '600'}" fill="${isCur ? '#0f766e' : '#334155'}">${pr.geography_name}</text>
              <rect x="135" y="${y}" width="${barW}" height="16" fill="#f1f5f9" rx="3" />
              <rect x="135" y="${y}" width="${w}" height="16" fill="${isCur ? '#0f766e' : '#94a3b8'}" rx="3" />
              <text x="${135 + w + 6}" y="${y + 12}" font-size="10" font-weight="700" fill="#1e293b">PKR ${fmt(Math.round(pr.mean_monthly_expenditure_pkr))}</text>
            `;
          });

          rightHtml += `
            <g transform="translate(0, 225)">
              <rect x="0" y="0" width="9" height="9" fill="#0f766e" rx="2" />
              <text x="12" y="8" font-size="10" fill="#334155">Food (${row.food_pct}%)</text>
              <rect x="110" y="0" width="9" height="9" fill="#d97706" rx="2" />
              <text x="122" y="8" font-size="10" fill="#334155">Housing (${row.housing_utilities_pct}%)</text>
              <rect x="220" y="0" width="9" height="9" fill="#0284c7" rx="2" />
              <text x="232" y="8" font-size="10" fill="#334155">Transport (${row.transport_comm_pct}%)</text>

              <rect x="0" y="16" width="9" height="9" fill="#e11d48" rx="2" />
              <text x="12" y="24" font-size="10" fill="#334155">Health (${row.health_pct}%)</text>
              <rect x="110" y="16" width="9" height="9" fill="#7c3aed" rx="2" />
              <text x="122" y="24" font-size="10" fill="#334155">Education (${row.education_pct}%)</text>
              <rect x="220" y="16" width="9" height="9" fill="#64748b" rx="2" />
              <text x="232" y="24" font-size="10" fill="#334155">Other (${row.clothing_other_pct}%)</text>
            </g>
          </g>`;

          svg.innerHTML = `
            ${paths}
            <circle cx="${cx}" cy="${cy}" r="${innerR}" fill="#ffffff" />
            <text x="${cx}" y="${cy - 8}" text-anchor="middle" font-size="9.5" font-weight="700" fill="#64748b">${row.geography_name.toUpperCase()}</text>
            <text x="${cx}" y="${cy + 8}" text-anchor="middle" font-size="13" font-weight="800" fill="#073c3a">PKR ${Math.round((row.mean_monthly_expenditure_pkr||70000)/1000)}k</text>
            <text x="${cx}" y="${cy + 22}" text-anchor="middle" font-size="9" font-weight="600" fill="#0f766e">Monthly Spend</text>
            ${rightHtml}
          `;
        }

        // ================= CARD 7: PURCHASING POWER (STAGGERED LABELS) =================
        function renderCard7WageInfl() {
          const svg = document.getElementById('svg-card-wage-infl');
          if (!svg || !db.wage_infl.length) return;

          const padX = 60, padY = 40, w = 480, h = 240;
          const colW = w / db.wage_infl.length;

          let elements = '';
          elements += `<line x1="${padX}" y1="${h + padY}" x2="${padX + w + 10}" y2="${h + padY}" stroke="#cbd5e1" stroke-width="1.5" />`;

          [50, 100, 150, 200, 250].forEach(val => {
            const y = h + padY - (val / 250) * h;
            elements += `
              <line x1="${padX}" y1="${y}" x2="${padX + w}" y2="${y}" stroke="#f1f5f9" stroke-width="1" />
              <text x="${padX - 8}" y="${y + 4}" text-anchor="end" font-size="9.5" fill="#94a3b8">${val}</text>
            `;
          });

          db.wage_infl.forEach((d, idx) => {
            const x = padX + idx * colW + 15;
            const barW = 30;
            const cpiVal = d.cpi_index_base2016 || 100;
            const wageVal = Math.round(100 + (d.cumulative_wage_growth_pct || 0));
            const cpiH = (cpiVal / 250) * h;
            const wageH = (wageVal / 250) * h;
            const yCpi = h + padY - cpiH;
            const yWage = h + padY - wageH;

            elements += `
              <rect x="${x}" y="${yCpi}" width="${barW}" height="${cpiH}" fill="#e11d48" rx="2"
                onmouseenter="showTooltip(event, '<strong>${d.year} Consumer Price Index</strong><br/>CPI Index (Base 2016): ${cpiVal}<br/>Annual Inflation: ${d.cpi_inflation_annual_pct}%<br/>Cumulative Inflation: +${d.cumulative_inflation_pct}%')"
                onmousemove="showTooltip(event, '<strong>${d.year} Consumer Price Index</strong><br/>CPI Index (Base 2016): ${cpiVal}<br/>Annual Inflation: ${d.cpi_inflation_annual_pct}%<br/>Cumulative Inflation: +${d.cumulative_inflation_pct}%')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />

              <rect x="${x + barW + 4}" y="${yWage}" width="${barW}" height="${wageH}" fill="#0f766e" rx="2"
                onmouseenter="showTooltip(event, '<strong>${d.year} Nominal Wage Index</strong><br/>Wage Index: ${wageVal}<br/>Monthly Mean Wage: PKR ${fmt(d.avg_monthly_wage_pkr)}<br/>Real Wage Index: ${d.real_wage_index}')"
                onmousemove="showTooltip(event, '<strong>${d.year} Nominal Wage Index</strong><br/>Wage Index: ${wageVal}<br/>Monthly Mean Wage: PKR ${fmt(d.avg_monthly_wage_pkr)}<br/>Real Wage Index: ${d.real_wage_index}')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />

              <text x="${x + barW + 2}" y="${h + padY + 16}" text-anchor="middle" font-size="11" font-weight="700" fill="#334155">${d.year}</text>
            `;

            // Vertically separated: CPI label at yCpi-7, Wage label at yWage-7 (over 50px vertical separation)
            if (idx === db.wage_infl.length - 1) {
              elements += `
                <text x="${x + barW/2}" y="${yCpi - 7}" text-anchor="middle" font-size="9.5" font-weight="800" fill="#e11d48">+${d.cumulative_inflation_pct}%</text>
                <text x="${x + barW*1.5 + 4}" y="${yWage - 7}" text-anchor="middle" font-size="9.5" font-weight="800" fill="#0f766e">+${d.cumulative_wage_growth_pct}%</text>
              `;
            }
          });

          // Legend with wide spacing (190px gap) to prevent touching
          elements += `
            <g transform="translate(110, 15)">
              <rect x="0" y="0" width="12" height="12" fill="#e11d48" rx="2" />
              <text x="16" y="10" font-size="11" font-weight="600" fill="#334155">CPI Prices (+118.4%)</text>
              <rect x="200" y="0" width="12" height="12" fill="#0f766e" rx="2" />
              <text x="216" y="10" font-size="11" font-weight="600" fill="#334155">Nominal Wages (+64.2%)</text>
            </g>
          `;

          svg.innerHTML = elements;
        }

        // ================= CARD 8: BASIC SERVICES ACCESS =================
        window.updateServicesProv = function(provId) {
          activeServicesProv = provId;
          const btns = document.querySelectorAll('#card-services .vi-ctrl-btn');
          btns.forEach(b => {
            const isMatch = (provId === 'PK' && b.innerText === 'National') ||
                            (provId === 'PK-PB' && b.innerText === 'Punjab') ||
                            (provId === 'PK-SN' && b.innerText === 'Sindh') ||
                            (provId === 'PK-KP' && b.innerText === 'KP') ||
                            (provId === 'PK-BA' && b.innerText === 'Balochistan');
            b.classList.toggle('active', isMatch);
          });
          renderCard8Services();
        };

        function renderCard8Services() {
          const svg = document.getElementById('svg-card-services');
          if (!svg || !db.services.length) return;

          const row = db.services.find(r => r.geography_id === activeServicesProv) || db.services[0];
          const indicators = [
            { label: 'Electricity Grid Access', pct: row.electricity_access_pct || 91.4, col: '#15803d' },
            { label: 'Underground Sewerage Flush', pct: row.underground_sewerage_toilet_pct || 59.6, col: '#0284c7' },
            { label: 'Piped Water Inside Dwelling', pct: row.piped_water_inside_pct || 29.8, col: '#0f766e' },
            { label: 'Clean Cooking Fuel Access', pct: row.clean_cooking_fuel_pct || 36.2, col: '#d97706' }
          ];

          let elements = '';
          const startY = 50, barW = 340, padX = 180;

          indicators.forEach((ind, idx) => {
            const y = startY + idx * 60;
            const w = (ind.pct / 100) * barW;

            elements += `
              <text x="${padX - 14}" y="${y + 16}" text-anchor="end" font-size="12" font-weight="700" fill="#1e293b">${ind.label}</text>
              <rect x="${padX}" y="${y}" width="${barW}" height="24" fill="#f1f5f9" rx="4" />
              <rect x="${padX}" y="${y}" width="${w}" height="24" fill="${ind.col}" rx="4"
                onmouseenter="showTooltip(event, '<strong>${ind.label} (${row.geography_name})</strong><br/>Household Access: ${ind.pct}%')"
                onmousemove="showTooltip(event, '<strong>${ind.label} (${row.geography_name})</strong><br/>Household Access: ${ind.pct}%')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />
              <text x="${padX + w + 10}" y="${y + 17}" font-size="13" font-weight="800" fill="${ind.col}">${ind.pct}%</text>
            `;
          });

          elements += `
            <text x="300" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#073c3a">
              Household Infrastructure Access Profile: ${row.geography_name}
            </text>
          `;

          svg.innerHTML = elements;
        }

        // ================= CARD 9: LABOUR FORCE DISPARITIES =================
        window.updateLfsMetric = function(metric) {
          activeLfsMetric = metric;
          const btns = document.querySelectorAll('#card-lfs .vi-ctrl-btn');
          btns[0].classList.toggle('active', metric === 'participation');
          btns[1].classList.toggle('active', metric === 'unemployment');
          btns[2].classList.toggle('active', metric === 'wages');
          renderCard9Lfs();
        };

        function renderCard9Lfs() {
          const svg = document.getElementById('svg-card-lfs');
          if (!svg || !db.lfs.length) return;

          let elements = '';
          const startY = 50, barW = 300, padX = 150;

          if (activeLfsMetric === 'participation') {
            db.lfs.forEach((r, idx) => {
              const y = startY + idx * 52;
              const mRate = r.labour_force_participation_rate_male || 68.4;
              const fRate = r.labour_force_participation_rate_female || 21.6;
              const mW = (mRate / 80) * barW;
              const fW = (fRate / 80) * barW;
              const geoName = r.geography_name || 'Pakistan';

              elements += `
                <text x="${padX - 12}" y="${y + 15}" text-anchor="end" font-size="11.5" font-weight="700" fill="#1e293b">${geoName}</text>
                <rect x="${padX}" y="${y}" width="${barW}" height="10" fill="#f1f5f9" rx="2" />
                <rect x="${padX}" y="${y}" width="${mW}" height="10" fill="#073c3a" rx="2"
                  onmouseenter="showTooltip(event, '<strong>${geoName} Male LFPR</strong><br/>${mRate}%')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${padX + mW + 6}" y="${y + 9}" font-size="9" font-weight="700" fill="#073c3a">${mRate}% M</text>

                <rect x="${padX}" y="${y + 13}" width="${barW}" height="10" fill="#f1f5f9" rx="2" />
                <rect x="${padX}" y="${y + 13}" width="${fW}" height="10" fill="#0f766e" rx="2"
                  onmouseenter="showTooltip(event, '<strong>${geoName} Female LFPR</strong><br/>${fRate}%')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${padX + fW + 6}" y="${y + 22}" font-size="9" font-weight="700" fill="#0f766e">${fRate}% F</text>
              `;
            });

            elements += `
              <g transform="translate(180, 15)">
                <rect x="0" y="0" width="10" height="10" fill="#073c3a" rx="2" />
                <text x="14" y="9" font-size="11" font-weight="600" fill="#334155">Male LFPR (68.4% National)</text>
                <rect x="180" y="0" width="10" height="10" fill="#0f766e" rx="2" />
                <text x="194" y="9" font-size="11" font-weight="600" fill="#334155">Female LFPR (21.6% National)</text>
              </g>
            `;
          } else if (activeLfsMetric === 'unemployment') {
            db.lfs.forEach((r, idx) => {
              const y = startY + idx * 52;
              const youthRate = r.youth_unemployment_rate_15_24 || 18.6;
              const w = (youthRate / 25) * barW;
              const geoName = r.geography_name || 'Pakistan';

              elements += `
                <text x="${padX - 12}" y="${y + 16}" text-anchor="end" font-size="12" font-weight="700" fill="#1e293b">${geoName}</text>
                <rect x="${padX}" y="${y}" width="${barW}" height="22" fill="#f1f5f9" rx="4" />
                <rect x="${padX}" y="${y}" width="${w}" height="22" fill="#e11d48" rx="4"
                  onmouseenter="showTooltip(event, '<strong>${geoName} Youth Joblessness</strong><br/>Youth (15-24) Rate: ${youthRate}%<br/>Overall Unemp: ${r.unemployment_rate_total}%')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${padX + w + 8}" y="${y + 16}" font-size="12" font-weight="800" fill="#e11d48">${youthRate}%</text>
              `;
            });
            elements += `<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#e11d48">Youth Unemployment Rate (Age 15–24)</text>`;
          } else {
            db.lfs.forEach((r, idx) => {
              const y = startY + idx * 52;
              const wage = r.average_monthly_wage_pkr || 35000;
              const w = (wage / 45000) * barW;
              const geoName = r.geography_name || 'Pakistan';

              elements += `
                <text x="${padX - 12}" y="${y + 16}" text-anchor="end" font-size="12" font-weight="700" fill="#1e293b">${geoName}</text>
                <rect x="${padX}" y="${y}" width="${barW}" height="22" fill="#f1f5f9" rx="4" />
                <rect x="${padX}" y="${y}" width="${w}" height="22" fill="#0284c7" rx="4"
                  onmouseenter="showTooltip(event, '<strong>${geoName} Wages</strong><br/>Mean Monthly Wage: PKR ${fmt(wage)}')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${padX + w + 8}" y="${y + 16}" font-size="11.5" font-weight="800" fill="#0284c7">PKR ${fmt(wage)}</text>
              `;
            });
            elements += `<text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#0284c7">Provincial Mean Monthly Wage</text>`;
          }

          svg.innerHTML = elements;
        }

        // ================= CARD 10: MULTI-CENSUS PROVINCIAL POPULATION SHIFTS =================
        window.updateCensusShiftYear = function(yr) {
          activeCensusShiftYear = yr;
          const btns = document.querySelectorAll('#card-census-shifts .vi-ctrl-btn');
          btns.forEach(b => b.classList.toggle('active', b.innerText === yr));
          renderCard10CensusShifts();
        };

        function renderCard10CensusShifts() {
          const svg = document.getElementById('svg-card-census-shifts');
          if (!svg || !db.census_shifts.length) return;

          const row = db.census_shifts.find(r => r.census_year.toString() === activeCensusShiftYear.toString()) || db.census_shifts[3];
          const slices = [
            { label: 'Punjab', pct: row.punjab_share_pct || 52.9, col: '#15803d', pop: row.punjab_pop_m },
            { label: 'Sindh', pct: row.sindh_share_pct || 23.1, col: '#0284c7', pop: row.sindh_pop_m },
            { label: 'KP', pct: row.kp_share_pct || 16.9, col: '#d97706', pop: row.kp_pop_m },
            { label: 'Balochistan', pct: row.balochistan_share_pct || 6.2, col: '#e11d48', pop: row.balochistan_pop_m },
            { label: 'ICT', pct: row.ict_share_pct || 1.0, col: '#7c3aed', pop: row.ict_pop_m }
          ];

          const cx = 135, cy = 160, r = 100, innerR = 60;
          let cumAngle = -Math.PI / 2;
          let paths = '';

          slices.forEach(s => {
            const angle = (s.pct / 100) * Math.PI * 2;
            const x1 = cx + r * Math.cos(cumAngle);
            const y1 = cy + r * Math.sin(cumAngle);
            const x2 = cx + r * Math.cos(cumAngle + angle);
            const y2 = cy + r * Math.sin(cumAngle + angle);
            const ix1 = cx + innerR * Math.cos(cumAngle + angle);
            const iy1 = cy + innerR * Math.sin(cumAngle + angle);
            const ix2 = cx + innerR * Math.cos(cumAngle);
            const iy2 = cy + innerR * Math.sin(cumAngle);
            const largeArc = angle > Math.PI ? 1 : 0;

            const d = `M ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} L ${ix1} ${iy1} A ${innerR} ${innerR} 0 ${largeArc} 0 ${ix2} ${iy2} Z`;

            paths += `<path d="${d}" fill="${s.col}" stroke="#ffffff" stroke-width="2"
              onmouseenter="showTooltip(event, '<strong>${s.label} (${row.census_year})</strong><br/>Population: ${s.pop} Million<br/>National Share: ${s.pct}%')"
              onmousemove="showTooltip(event, '<strong>${s.label} (${row.census_year})</strong><br/>Population: ${s.pop} Million<br/>National Share: ${s.pct}%')"
              onmouseleave="hideTooltip()" style="cursor:pointer;" />`;
            cumAngle += angle;
          });

          let rightHtml = `
            <g transform="translate(290, 25)">
              <text x="0" y="0" font-size="12" font-weight="700" fill="#073c3a">4-Decade Demographic Share Trajectory (1981–2023)</text>
              <text x="0" y="16" font-size="10.5" fill="#64748b">Comparison across 1981, 1998, 2017, and 2023 Censuses</text>
          `;

          const barW = 200;
          slices.forEach((s, idx) => {
            const y = 35 + idx * 44;
            const curW = (s.pct / 60) * barW;

            rightHtml += `
              <text x="0" y="${y + 11}" font-size="11.5" font-weight="700" fill="#1e293b">${s.label}</text>
              <rect x="80" y="${y}" width="${barW}" height="14" fill="#f1f5f9" rx="3" />
              <rect x="80" y="${y}" width="${curW}" height="14" fill="${s.col}" rx="3" />
              <text x="${80 + curW + 8}" y="${y + 11}" font-size="11" font-weight="800" fill="${s.col}">${s.pct}% (${s.pop}M)</text>
            `;
          });

          rightHtml += `
            <g transform="translate(0, 260)">
              <text x="0" y="0" font-size="10.5" font-weight="700" fill="#073c3a">Historical Trends Summary:</text>
              <text x="0" y="15" font-size="10" fill="#475569">• Punjab contracted -3.2% (56.1% in 1981 → 52.9% in 2023)</text>
              <text x="0" y="28" font-size="10" fill="#475569">• Balochistan expanded +1.1% (5.1% in 1981 → 6.2% in 2023)</text>
              <text x="0" y="41" font-size="10" fill="#475569">• KP gained +3.8% (13.1% in 1981 → 16.9% in 2023 with FATA merger)</text>
            </g>
          </g>`;

          svg.innerHTML = `
            ${paths}
            <circle cx="${cx}" cy="${cy}" r="${innerR}" fill="#ffffff" />
            <text x="${cx}" y="${cy - 8}" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b">CENSUS YEAR</text>
            <text x="${cx}" y="${cy + 10}" text-anchor="middle" font-size="16" font-weight="800" fill="#073c3a">${row.census_year}</text>
            <text x="${cx}" y="${cy + 24}" text-anchor="middle" font-size="10" font-weight="600" fill="#0f766e">${row.total_pakistan_pop_m}M Pop</text>
            ${rightHtml}
          `;
        }

        // ================= CARD 11: 135-DISTRICT QUADRANT SCATTER (CLIPPED & NON-OVERLAPPING) =================
        window.updateScatterProv = function(prov) {
          activeScatterProv = prov;
          const btns = document.querySelectorAll('#card-districts-scatter .vi-ctrl-btn');
          btns.forEach(b => {
            const isMatch = (prov === 'all' && b.innerText === 'All Districts') ||
                            (b.innerText.includes(prov));
            b.classList.toggle('active', isMatch);
          });
          renderCard11DistrictsScatter();
        };

        window.filterScatterMap = function() {
          const input = document.getElementById('scatter-search-input');
          activeScatterSearch = input.value.trim().toLowerCase();
          renderCard11DistrictsScatter();
        };

        function renderCard11DistrictsScatter() {
          const svg = document.getElementById('svg-card-districts-scatter');
          if (!svg || !db.districts.length) return;

          const padL = 70, padR = 40, padT = 50, padB = 60;
          const w = 940 - padL - padR;
          const h = 440 - padT - padB;

          const minDensity = 4, maxDensity = 50000;
          const logMin = Math.log10(minDensity);
          const logMax = Math.log10(maxDensity);

          function getX(urbanPct) {
            return padL + (urbanPct / 100) * w;
          }
          function getY(density) {
            const safeD = Math.max(minDensity, Math.min(density, maxDensity));
            const logVal = Math.log10(safeD);
            const ratio = (logVal - logMin) / (logMax - logMin);
            return padT + h - ratio * h;
          }

          let elements = '';

          // Add SVG clipPath to ensure no bubble or line ever spills outside the plot
          elements += `
            <defs>
              <clipPath id="scatter-plot-clip">
                <rect x="${padL}" y="${padT}" width="${w}" height="${h}" rx="2" />
              </clipPath>
            </defs>
          `;

          const nationalUrbanAvg = 38.8;
          const nationalDensityAvg = 303.4;
          const splitX = getX(nationalUrbanAvg);
          const splitY = getY(nationalDensityAvg);

          // Quadrant Background Shading
          elements += `<rect x="${splitX}" y="${padT}" width="${padL + w - splitX}" height="${splitY - padT}" fill="#f0fdf4" opacity="0.6" />`;
          elements += `<rect x="${padL}" y="${padT}" width="${splitX - padL}" height="${splitY - padT}" fill="#fefce8" opacity="0.6" />`;
          elements += `<rect x="${padL}" y="${splitY}" width="${splitX - padL}" height="${padT + h - splitY}" fill="#fff1f2" opacity="0.6" />`;
          elements += `<rect x="${splitX}" y="${splitY}" width="${padL + w - splitX}" height="${padT + h - splitY}" fill="#f0f9ff" opacity="0.6" />`;

          // Center Dividing Reference Lines
          elements += `
            <line x1="${splitX}" y1="${padT}" x2="${splitX}" y2="${padT + h}" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5" />
            <line x1="${padL}" y1="${splitY}" x2="${padL + w}" y2="${splitY}" stroke="#94a3b8" stroke-dasharray="4,4" stroke-width="1.5" />
          `;

          // NON-OVERLAPPING CORNER BADGES (220px wide with ample margins)
          // Top-Left (Q2): Agrarian Dense
          elements += `
            <g transform="translate(${padL + 12}, ${padT + 8})">
              <rect x="0" y="0" width="220" height="34" fill="#ffffff" fill-opacity="0.88" rx="4" stroke="#cbd5e1" stroke-width="1" />
              <text x="8" y="14" font-size="10.5" font-weight="700" fill="#b45309">Q2: AGRARIAN DENSE HUBS</text>
              <text x="8" y="27" font-size="8.5" font-weight="600" fill="#64748b">Low Urban (&lt;39%) • High Density</text>
            </g>
          `;

          // Top-Right (Q1): Dense Metros
          elements += `
            <g transform="translate(${splitX + 16}, ${padT + 8})">
              <rect x="0" y="0" width="220" height="34" fill="#ffffff" fill-opacity="0.88" rx="4" stroke="#cbd5e1" stroke-width="1" />
              <text x="8" y="14" font-size="10.5" font-weight="700" fill="#15803d">Q1: DENSE METROS</text>
              <text x="8" y="27" font-size="8.5" font-weight="600" fill="#64748b">High Urban (≥39%) • High Density</text>
            </g>
          `;

          // Bottom-Left (Q3): Vast Arid Periphery
          elements += `
            <g transform="translate(${padL + 12}, ${padT + h - 42})">
              <rect x="0" y="0" width="220" height="34" fill="#ffffff" fill-opacity="0.88" rx="4" stroke="#cbd5e1" stroke-width="1" />
              <text x="8" y="14" font-size="10.5" font-weight="700" fill="#be123c">Q3: VAST ARID PERIPHERY</text>
              <text x="8" y="27" font-size="8.5" font-weight="600" fill="#64748b">Low Urban (&lt;39%) • Low Density</text>
            </g>
          `;

          // Bottom-Right (Q4): Urban Outposts
          elements += `
            <g transform="translate(${splitX + 16}, ${padT + h - 42})">
              <rect x="0" y="0" width="220" height="34" fill="#ffffff" fill-opacity="0.88" rx="4" stroke="#cbd5e1" stroke-width="1" />
              <text x="8" y="14" font-size="10.5" font-weight="700" fill="#0369a1">Q4: URBAN OUTPOSTS</text>
              <text x="8" y="27" font-size="8.5" font-weight="600" fill="#64748b">High Urban (≥39%) • Lower Density</text>
            </g>
          `;

          // Grid Lines & Axis Ticks
          [0, 20, 40, 60, 80, 100].forEach(pct => {
            const x = getX(pct);
            elements += `
              <line x1="${x}" y1="${padT}" x2="${x}" y2="${padT + h}" stroke="#e2e8f0" stroke-width="1" />
              <line x1="${x}" y1="${padT + h}" x2="${x}" y2="${padT + h + 5}" stroke="#64748b" stroke-width="1.5" />
              <text x="${x}" y="${padT + h + 18}" text-anchor="middle" font-size="10.5" font-weight="600" fill="#475569">${pct}%</text>
            `;
          });

          [10, 100, 1000, 10000, 40000].forEach(dVal => {
            const y = getY(dVal);
            elements += `
              <line x1="${padL}" y1="${y}" x2="${padL + w}" y2="${y}" stroke="#e2e8f0" stroke-width="1" />
              <line x1="${padL - 5}" y1="${y}" x2="${padL}" y2="${y}" stroke="#64748b" stroke-width="1.5" />
              <text x="${padL - 8}" y="${y + 4}" text-anchor="end" font-size="10" font-weight="600" fill="#475569">${dVal.toLocaleString()}</text>
            `;
          });

          elements += `
            <text x="${padL + w/2}" y="${padT + h + 42}" text-anchor="middle" font-size="12" font-weight="700" fill="#073c3a">
              URBANIZATION PROPORTION (%) • PBS Census 2023 Table 1
            </text>
            <text x="18" y="${padT + h/2}" text-anchor="middle" font-size="12" font-weight="700" fill="#073c3a" transform="rotate(-90 18 ${padT + h/2})">
              POPULATION DENSITY (Persons / km² on Log Scale)
            </text>
          `;

          const provColors = {
            'Punjab': '#15803d',
            'Sindh': '#0284c7',
            'Khyber Pakhtunkhwa': '#d97706',
            'Balochistan': '#e11d48',
            'Islamabad': '#7c3aed'
          };

          let filtered = db.districts;
          if (activeScatterProv !== 'all') {
            filtered = filtered.filter(d => d.province_name === activeScatterProv);
          }
          if (activeScatterSearch) {
            filtered = filtered.filter(d => (d.district_name || '').toLowerCase().includes(activeScatterSearch));
          }

          // BUBBLES RENDERED WITH STRICT CLAMPING AND CLIPPING
          elements += `<g clip-path="url(#scatter-plot-clip)">`;

          filtered.forEach(d => {
            const urbanPct = typeof d.urban_proportion_pct === 'number' ? d.urban_proportion_pct : ((d.population_urban / (d.population_2023 || 1)) * 100);
            const density = d.density_per_sqkm || (d.population_2023 / (d.area_sqkm || 1));
            const rawX = getX(urbanPct);
            const rawY = getY(density);

            // Radius tuned cleanly between 3.5px and 14px (prevents clutter)
            const r = Math.max(3.5, Math.min(14, Math.sqrt((d.population_2023 || 500000) / 45000)));

            // Clamp bubble centers inside plot margins
            const x = Math.max(padL + r + 2, Math.min(padL + w - r - 2, rawX));
            const y = Math.max(padT + r + 2, Math.min(padT + h - r - 2, rawY));
            const col = provColors[d.province_name] || '#0f766e';

            elements += `
              <circle cx="${x}" cy="${y}" r="${r}" fill="${col}" fill-opacity="0.55" stroke="#ffffff" stroke-width="1.2"
                onmouseenter="showTooltip(event, '<strong>${d.district_name} (${d.province_name})</strong><br/>Population: ${fmt(d.population_2023)}<br/>Urban Share: <strong>${urbanPct.toFixed(1)}%</strong><br/>Density: <strong>${density.toFixed(1)} / km²</strong><br/>Area: ${fmt(d.area_sqkm)} km²')"
                onmousemove="showTooltip(event, '<strong>${d.district_name} (${d.province_name})</strong><br/>Population: ${fmt(d.population_2023)}<br/>Urban Share: <strong>${urbanPct.toFixed(1)}%</strong><br/>Density: <strong>${density.toFixed(1)} / km²</strong><br/>Area: ${fmt(d.area_sqkm)} km²')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />
            `;

            // Notable District Labels (safely oriented above or below bubble)
            const notable = ['Lahore', 'Karachi Central', 'Islamabad', 'Quetta', 'Peshawar', 'Rawalpindi', 'Chaghi', 'Gwadar', 'Faisalabad'];
            if (notable.includes(d.district_name)) {
              const labelY = y < padT + 25 ? (y + r + 11) : (y - r - 4);
              elements += `<text x="${x}" y="${labelY}" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0f172a">${d.district_name}</text>`;
            }
          });

          elements += `</g>`;

          // Top Legend Bar
          elements += `
            <g transform="translate(${padL + 20}, 16)">
              <rect x="0" y="0" width="10" height="10" fill="#15803d" rx="2" />
              <text x="14" y="9" font-size="10.5" font-weight="600" fill="#334155">Punjab</text>
              <rect x="85" y="0" width="10" height="10" fill="#0284c7" rx="2" />
              <text x="99" y="9" font-size="10.5" font-weight="600" fill="#334155">Sindh</text>
              <rect x="160" y="0" width="10" height="10" fill="#d97706" rx="2" />
              <text x="174" y="9" font-size="10.5" font-weight="600" fill="#334155">KP</text>
              <rect x="225" y="0" width="10" height="10" fill="#e11d48" rx="2" />
              <text x="239" y="9" font-size="10.5" font-weight="600" fill="#334155">Balochistan</text>
              <rect x="330" y="0" width="10" height="10" fill="#7c3aed" rx="2" />
              <text x="344" y="9" font-size="10.5" font-weight="600" fill="#334155">ICT</text>
              <text x="400" y="9" font-size="10" fill="#64748b">• Bubble size ~ √Population • Showing ${filtered.length} Districts</text>
            </g>
          `;

          svg.innerHTML = elements;
        }

        // ================= CARD 12: EMPLOYMENT BY SECTOR =================
        function renderCard12SectorEmployment() {
          const svg = document.getElementById('svg-card-sector-employment');
          if (!svg || !db.lfs.length) return;

          let elements = '';
          const startY = 50, barW = 340, padX = 140;

          db.lfs.forEach((r, idx) => {
            const y = startY + idx * 52;
            const agShare = r.employment_share_agriculture || 37.4;
            const indShare = r.employment_share_industry || 25.4;
            const serShare = r.employment_share_services || 37.2;
            const geoName = r.geography_name || 'Pakistan';

            const agW = (agShare / 100) * barW;
            const indW = (indShare / 100) * barW;
            const serW = (serShare / 100) * barW;

            elements += `
              <text x="${padX - 12}" y="${y + 16}" text-anchor="end" font-size="12" font-weight="700" fill="#1e293b">${geoName}</text>
              <rect x="${padX}" y="${y}" width="${agW}" height="22" fill="#0f766e" rx="2"
                onmouseenter="showTooltip(event, '<strong>${geoName} Agriculture</strong><br/>Employment Share: ${agShare}%')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />
              <rect x="${padX + agW}" y="${y}" width="${indW}" height="22" fill="#d97706" rx="0"
                onmouseenter="showTooltip(event, '<strong>${geoName} Industry</strong><br/>Employment Share: ${indShare}%')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />
              <rect x="${padX + agW + indW}" y="${y}" width="${serW}" height="22" fill="#0284c7" rx="2"
                onmouseenter="showTooltip(event, '<strong>${geoName} Services</strong><br/>Employment Share: ${serShare}%')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />

              <text x="${padX + agW/2}" y="${y + 15}" text-anchor="middle" font-size="10" font-weight="700" fill="#ffffff">${agShare}%</text>
              <text x="${padX + agW + indW/2}" y="${y + 15}" text-anchor="middle" font-size="10" font-weight="700" fill="#ffffff">${indShare}%</text>
              <text x="${padX + agW + indW + serW/2}" y="${y + 15}" text-anchor="middle" font-size="10" font-weight="700" fill="#ffffff">${serShare}%</text>
            `;
          });

          elements += `
            <g transform="translate(140, 16)">
              <rect x="0" y="0" width="12" height="12" fill="#0f766e" rx="2" />
              <text x="16" y="10" font-size="11" font-weight="600" fill="#334155">Agriculture (37.4% PK)</text>
              <rect x="170" y="0" width="12" height="12" fill="#d97706" rx="2" />
              <text x="186" y="10" font-size="11" font-weight="600" fill="#334155">Industry &amp; Const (25.4%)</text>
              <rect x="340" y="0" width="12" height="12" fill="#0284c7" rx="2" />
              <text x="356" y="10" font-size="11" font-weight="600" fill="#334155">Services &amp; Trade (37.2%)</text>
            </g>
          `;

          svg.innerHTML = elements;
        }

        // ================= CARD 13: PROVINCIAL AGRI SHIFTS =================
        function renderCard13AgriShifts() {
          const svg = document.getElementById('svg-card-agri-shifts');
          if (!svg || !db.agri_shifts.length) return;

          let elements = '';
          const startY = 40, barW = 160, padX = 110;

          elements += `
            <text x="160" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#073c3a">Farms Count Surge (+34.4% Nationwide)</text>
          `;

          db.agri_shifts.forEach((r, idx) => {
            const y = startY + idx * 56;
            const w10 = (r.farms_2010 / 6000000) * barW;
            const w24 = (r.farms_2024 / 6000000) * barW;

            elements += `
              <text x="${padX - 10}" y="${y + 14}" text-anchor="end" font-size="11" font-weight="700" fill="#1e293b">${r.province_name}</text>
              <rect x="${padX}" y="${y}" width="${w10}" height="10" fill="#94a3b8" rx="2" />
              <text x="${padX + w10 + 6}" y="${y + 9}" font-size="9" fill="#64748b">${(r.farms_2010/1000000).toFixed(2)}M (2010)</text>

              <rect x="${padX}" y="${y + 13}" width="${w24}" height="10" fill="#0f766e" rx="2"
                onmouseenter="showTooltip(event, '<strong>${r.province_name} Farm Fragmentation</strong><br/>2010: ${fmt(r.farms_2010)} farms<br/>2024: ${fmt(r.farms_2024)} farms<br/>Growth: +${r.farms_change_pct}%<br/>Avg Farm Size: ${r.avg_farm_size_2024} Acres')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />
              <text x="${padX + w24 + 6}" y="${y + 22}" font-size="9" font-weight="800" fill="#0f766e">${(r.farms_2024/1000000).toFixed(2)}M (+${r.farms_change_pct}%)</text>
            `;
          });

          const cx = 450, cy = 160, r = 90, innerR = 50;
          let cumAngle = -Math.PI / 2;
          const slices = [
            { label: 'Punjab', acres: 38.07, pct: 64.2, col: '#15803d' },
            { label: 'Sindh', acres: 12.93, pct: 21.8, col: '#0284c7' },
            { label: 'KP', acres: 5.10, pct: 8.6, col: '#d97706' },
            { label: 'Balochistan', acres: 3.20, pct: 5.4, col: '#e11d48' }
          ];

          slices.forEach(s => {
            const angle = (s.pct / 100) * Math.PI * 2;
            const x1 = cx + r * Math.cos(cumAngle);
            const y1 = cy + r * Math.sin(cumAngle);
            const x2 = cx + r * Math.cos(cumAngle + angle);
            const y2 = cy + r * Math.sin(cumAngle + angle);
            const ix1 = cx + innerR * Math.cos(cumAngle + angle);
            const iy1 = cy + innerR * Math.sin(cumAngle + angle);
            const ix2 = cx + innerR * Math.cos(cumAngle);
            const iy2 = cy + innerR * Math.sin(cumAngle);
            const largeArc = angle > Math.PI ? 1 : 0;

            const d = `M ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} L ${ix1} ${iy1} A ${innerR} ${innerR} 0 ${largeArc} 0 ${ix2} ${iy2} Z`;

            elements += `<path d="${d}" fill="${s.col}" stroke="#ffffff" stroke-width="2"
              onmouseenter="showTooltip(event, '<strong>${s.label} Cultivated Acreage</strong><br/>${s.acres} Million Acres (${s.pct}%)')"
              onmouseleave="hideTooltip()" style="cursor:pointer;" />`;
            cumAngle += angle;
          });

          elements += `
            <circle cx="${cx}" cy="${cy}" r="${innerR}" fill="#ffffff" />
            <text x="${cx}" y="${cy - 6}" text-anchor="middle" font-size="9" font-weight="700" fill="#64748b">CULTIVATED LAND</text>
            <text x="${cx}" y="${cy + 10}" text-anchor="middle" font-size="13" font-weight="800" fill="#073c3a">59.3M Acres</text>

            <g transform="translate(350, 275)">
              <rect x="0" y="0" width="8" height="8" fill="#15803d" rx="2" />
              <text x="12" y="8" font-size="9.5" fill="#334155">Punjab 64%</text>
              <rect x="85" y="0" width="8" height="8" fill="#0284c7" rx="2" />
              <text x="97" y="8" font-size="9.5" fill="#334155">Sindh 22%</text>
              <rect x="165" y="0" width="8" height="8" fill="#d97706" rx="2" />
              <text x="177" y="8" font-size="9.5" fill="#334155">KP 9%</text>
              <rect x="230" y="0" width="8" height="8" fill="#e11d48" rx="2" />
              <text x="242" y="8" font-size="9.5" fill="#334155">BA 5%</text>
            </g>
          `;

          svg.innerHTML = elements;
        }

        // ================= CARD 14: 70-YEAR DEMOGRAPHIC GROWTH =================
        function renderCard14CensusHist() {
          const svg = document.getElementById('svg-card-census-hist');
          if (!svg || !db.census_hist.length) return;

          const padX = 50, padY = 40, w = 500, h = 240;
          const colW = w / db.census_hist.length;
          const maxPop = 260;

          let elements = '';
          elements += `<line x1="${padX}" y1="${h + padY}" x2="${padX + w + 10}" y2="${h + padY}" stroke="#cbd5e1" stroke-width="1.5" />`;

          db.census_hist.forEach((d, idx) => {
            const x = padX + idx * colW + colW * 0.15;
            const barW = colW * 0.7;
            const popM = d.population_millions || d.total_population_millions || 33.7;
            const barH = (popM / maxPop) * h;
            const y = h + padY - barH;

            elements += `
              <rect x="${x}" y="${y}" width="${barW}" height="${barH}" fill="#0f766e" rx="3"
                onmouseenter="showTooltip(event, '<strong>${d.census_year} Census of Pakistan</strong><br/>Population: ${popM} Million<br/>Intercensal Growth: ${d.annual_growth_rate_pct}% p.a.')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />
              <text x="${x + barW/2}" y="${y - 6}" text-anchor="middle" font-size="10.5" font-weight="800" fill="#073c3a">${popM}M</text>
              <text x="${x + barW/2}" y="${h + padY + 16}" text-anchor="middle" font-size="11" font-weight="700" fill="#475569">${d.census_year}</text>
            `;

            if (d.annual_growth_rate_pct > 0) {
              elements += `<text x="${x + barW/2}" y="${y + 16}" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">${d.annual_growth_rate_pct}%</text>`;
            }
          });

          elements += `
            <text x="300" y="25" text-anchor="middle" font-size="12" font-weight="700" fill="#073c3a">
              7.2-Fold Expansion in 72 Years (33.7M in 1951 → 241.5M in 2023)
            </text>
          `;

          svg.innerHTML = elements;
        }

        // ================= CARD 15: 35-YEAR MACROECONOMIC TRAJECTORY (STACKED TENURE BADGES) =================
        window.updateMacroMetric = function(metric) {
          activeMacroMetric = metric;
          const btns = document.querySelectorAll('#card-macro .vi-ctrl-btn');
          btns[0].classList.toggle('active', metric === 'growth_infl');
          btns[1].classList.toggle('active', metric === 'deficits');
          btns[2].classList.toggle('active', metric === 'debt_gdp');
          renderCard15Macro();
        };

        function renderCard15Macro() {
          const svg = document.getElementById('svg-card-macro');
          if (!svg || !db.macro.length) return;

          // Ensure chronological ascending sequence (1990 -> 2025) so timeline flows left-to-right
          const chronData = db.macro.slice().sort((a, b) => parseInt(a.year) - parseInt(b.year));

          const padL = 60, padR = 40, padT = 62, padB = 60;
          const w = 940 - padL - padR;
          const h = 420 - padT - padB;

          const totalYears = chronData.length;
          function getX(idx) { return padL + (idx / (totalYears - 1)) * w; }

          let elements = '';

          const idx1990 = 0;
          const idx1999 = chronData.findIndex(r => parseInt(r.year) === 1999);
          const idx2008 = chronData.findIndex(r => parseInt(r.year) === 2008);
          const idx2018 = chronData.findIndex(r => parseInt(r.year) === 2018);
          const idxEnd = totalYears - 1;

          const x0 = getX(idx1990);
          const x99 = getX(idx1999 !== -1 ? idx1999 : 9);
          const x08 = getX(idx2008 !== -1 ? idx2008 : 18);
          const x18 = getX(idx2018 !== -1 ? idx2018 : 28);
          const xEnd = getX(idxEnd);

          // 1. Soft Ambient Tint Bands (fill-opacity 0.08) - Never obscures curves or labels
          elements += `
            <rect x="${x0}" y="${padT}" width="${x99 - x0}" height="${h}" fill="#0284c7" fill-opacity="0.08" />
            <rect x="${x99}" y="${padT}" width="${x08 - x99}" height="${h}" fill="#15803d" fill-opacity="0.08" />
            <rect x="${x08}" y="${padT}" width="${x18 - x08}" height="${h}" fill="#d97706" fill-opacity="0.08" />
            <rect x="${x18}" y="${padT}" width="${xEnd - x18}" height="${h}" fill="#e11d48" fill-opacity="0.08" />

            <!-- Vertical Dividing Boundaries between Tenures -->
            <line x1="${x99}" y1="${padT}" x2="${x99}" y2="${padT + h}" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="2,2" />
            <line x1="${x08}" y1="${padT}" x2="${x08}" y2="${padT + h}" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="2,2" />
            <line x1="${x18}" y1="${padT}" x2="${x18}" y2="${padT + h}" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="2,2" />
          `;

          // 2. Dedicated Top Header Pill Rack (y=12 to 44) completely above the plot
          elements += `
            <!-- Tenure I (1990–99) -->
            <g transform="translate(${(x0 + x99)/2 - 75}, 12)">
              <rect x="0" y="0" width="150" height="32" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1" />
              <text x="75" y="14" text-anchor="middle" font-size="9.5" font-weight="700" fill="#334155">TENURE I (1990–99)</text>
              <text x="75" y="26" text-anchor="middle" font-size="8" font-weight="600" fill="#64748b">Democracy &amp; Sanctions</text>
            </g>

            <!-- Tenure II (1999–08) -->
            <g transform="translate(${(x99 + x08)/2 - 75}, 12)">
              <rect x="0" y="0" width="150" height="32" rx="4" fill="#ffffff" stroke="#15803d" stroke-width="1" />
              <text x="75" y="14" text-anchor="middle" font-size="9.5" font-weight="700" fill="#15803d">TENURE II (1999–08)</text>
              <text x="75" y="26" text-anchor="middle" font-size="8" font-weight="600" fill="#166534">Consumption Boom</text>
            </g>

            <!-- Tenure III (2008–18) -->
            <g transform="translate(${(x08 + x18)/2 - 80}, 12)">
              <rect x="0" y="0" width="160" height="32" rx="4" fill="#ffffff" stroke="#d97706" stroke-width="1" />
              <text x="80" y="14" text-anchor="middle" font-size="9.5" font-weight="700" fill="#b45309">TENURE III (2008–18)</text>
              <text x="80" y="26" text-anchor="middle" font-size="8" font-weight="600" fill="#92400e">Energy &amp; CPEC Inflows</text>
            </g>

            <!-- Tenure IV (2018–25) -->
            <g transform="translate(${(x18 + xEnd)/2 - 75}, 12)">
              <rect x="0" y="0" width="150" height="32" rx="4" fill="#ffffff" stroke="#e11d48" stroke-width="1" />
              <text x="75" y="14" text-anchor="middle" font-size="9.5" font-weight="700" fill="#be123c">TENURE IV (2018–25)</text>
              <text x="75" y="26" text-anchor="middle" font-size="8" font-weight="600" fill="#9f1239">Stagflation &amp; Reform</text>
            </g>
          `;

          // 3. Left Y-Axis Scale & Dashed Horizontal Reference Gridlines
          let minY = -5, maxY = 35;
          let yTicks = [-10, 0, 10, 20, 30, 40];
          if (activeMacroMetric === 'deficits') { minY = -12; maxY = 5; yTicks = [-12, -8, -4, 0, 4]; }
          if (activeMacroMetric === 'debt_gdp') { minY = 50; maxY = 90; yTicks = [50, 60, 70, 80, 90]; }

          function getY(val) {
            const ratio = (val - minY) / (maxY - minY);
            return padT + h - ratio * h;
          }

          yTicks.forEach(val => {
            const y = getY(val);
            const isZero = val === 0;
            elements += `
              <line x1="${padL}" y1="${y}" x2="${padL + w}" y2="${y}" stroke="${isZero ? '#64748b' : '#e2e8f0'}" stroke-width="${isZero ? '1.5' : '1'}" stroke-dasharray="${isZero ? 'none' : '3,3'}" />
              <text x="${padL - 10}" y="${y + 4}" text-anchor="end" font-size="10" font-weight="600" fill="${isZero ? '#0f172a' : '#64748b'}">${val > 0 ? '+' : ''}${val}%</text>
            `;
          });

          let p1 = '', p2 = '';

          chronData.forEach((d, idx) => {
            const x = getX(idx);
            let val1 = 0, val2 = 0;
            if (activeMacroMetric === 'growth_infl') {
              val1 = d.gdp_growth_pct !== undefined ? d.gdp_growth_pct : 4.0;
              val2 = d.inflation_cpi_pct !== undefined ? d.inflation_cpi_pct : 8.0;
            } else if (activeMacroMetric === 'deficits') {
              val1 = d.fiscal_deficit_pct_gdp !== undefined ? d.fiscal_deficit_pct_gdp : -6.2;
              val2 = d.current_account_pct_gdp !== undefined ? d.current_account_pct_gdp : -3.1;
            } else {
              val1 = d.total_debt_to_gdp_pct !== undefined ? d.total_debt_to_gdp_pct : 72.5;
            }

            const y1 = getY(val1);
            p1 += (idx === 0 ? `M ${x} ${y1}` : ` L ${x} ${y1}`);

            if (activeMacroMetric !== 'debt_gdp') {
              const y2 = getY(val2);
              p2 += (idx === 0 ? `M ${x} ${y2}` : ` L ${x} ${y2}`);
            }

            if (idx % 5 === 0 || idx === totalYears - 1) {
              elements += `
                <line x1="${x}" y1="${padT + h}" x2="${x}" y2="${padT + h + 6}" stroke="#64748b" stroke-width="1" />
                <text x="${x}" y="${padT + h + 18}" text-anchor="middle" font-size="10.5" font-weight="600" fill="#475569">${d.year}</text>
              `;
            }
          });

          if (activeMacroMetric === 'growth_infl') {
            elements += `
              <path d="${p1}" fill="none" stroke="#0f766e" stroke-width="3" />
              <path d="${p2}" fill="none" stroke="#e11d48" stroke-width="3" />
            `;
          } else if (activeMacroMetric === 'deficits') {
            elements += `
              <path d="${p1}" fill="none" stroke="#d97706" stroke-width="3" />
              <path d="${p2}" fill="none" stroke="#0284c7" stroke-width="3" />
            `;
          } else {
            elements += `<path d="${p1}" fill="none" stroke="#7c3aed" stroke-width="3.5" />`;
          }

          // 4. Polar Staggered Shock Markers (2020 at bottom trough, 2023 at top peak)
          const shocks = [
            { year: 1998, text: '1998 Nuclear Sanctions', yPos: padT + 80, pillW: 135 },
            { year: 2008, text: '2008 Commodity Shock', yPos: padT + 95, pillW: 130 },
            { year: 2020, text: '2020 COVID Contraction (-0.9%)', yPos: padT + h - 18, pillW: 155 },
            { year: 2023, text: '2023 Peak Inflation (38%)', yPos: padT + 18, pillW: 140 }
          ];

          shocks.forEach(s => {
            const idx = chronData.findIndex(r => parseInt(r.year) === s.year);
            if (idx !== -1) {
              const x = getX(idx);
              elements += `
                <line x1="${x}" y1="${padT}" x2="${x}" y2="${padT + h}" stroke="#e11d48" stroke-width="1.5" stroke-dasharray="2,2" opacity="0.6" />
                <circle cx="${x}" cy="${s.yPos}" r="3.5" fill="#e11d48" />
                <g transform="translate(${x - s.pillW/2}, ${s.yPos - 11})">
                  <rect x="0" y="0" width="${s.pillW}" height="20" fill="#ffffff" fill-opacity="0.95" rx="3" stroke="#e11d48" stroke-width="1" />
                  <text x="${s.pillW/2}" y="14" text-anchor="middle" font-size="9" font-weight="700" fill="#be123c">${s.text}</text>
                </g>
              `;
            }
          });

          let legendHtml = '';
          if (activeMacroMetric === 'growth_infl') {
            legendHtml = `
              <g transform="translate(${padL + 20}, ${padT + h + 38})">
                <line x1="0" y1="8" x2="20" y2="8" stroke="#0f766e" stroke-width="3" />
                <text x="26" y="12" font-size="11" font-weight="700" fill="#0f766e">GDP Growth Rate (%)</text>
                <line x1="170" y1="8" x2="190" y2="8" stroke="#e11d48" stroke-width="3" />
                <text x="196" y="12" font-size="11" font-weight="700" fill="#e11d48">CPI Inflation Rate (%) • Peaked at 38% Monthly / 30.8% Annual (2023)</text>
              </g>
            `;
          } else if (activeMacroMetric === 'deficits') {
            legendHtml = `
              <g transform="translate(${padL + 20}, ${padT + h + 38})">
                <line x1="0" y1="8" x2="20" y2="8" stroke="#d97706" stroke-width="3" />
                <text x="26" y="12" font-size="11" font-weight="700" fill="#d97706">Fiscal Deficit (% of GDP)</text>
                <line x1="180" y1="8" x2="200" y2="8" stroke="#0284c7" stroke-width="3" />
                <text x="206" y="12" font-size="11" font-weight="700" fill="#0284c7">Current Account Balance (% of GDP)</text>
              </g>
            `;
          } else {
            legendHtml = `
              <g transform="translate(${padL + 20}, ${padT + h + 38})">
                <line x1="0" y1="8" x2="20" y2="8" stroke="#7c3aed" stroke-width="3" />
                <text x="26" y="12" font-size="11" font-weight="700" fill="#7c3aed">Total Public Debt to GDP Ratio (%)</text>
              </g>
            `;
          }

          svg.innerHTML = elements + legendHtml;
        }

        // ================= CARD 16: PROVINCIAL RESOURCE ALLOCATION, DEBT & CONFLICT MATRIX =================
        window.updateProvMatrixView = function(view) {
          activeProvMatrixView = view;
          const btns = document.querySelectorAll('#card-prov-matrix .vi-ctrl-btn');
          const views = ['budget_dev', 'debt_stock', 'conflict_burden', 'per_capita'];
          btns.forEach((b, idx) => {
            b.classList.toggle('active', views[idx] === view);
          });
          renderCard16ProvMatrix();
        };

        function renderCard16ProvMatrix() {
          const svg = document.getElementById('svg-card-prov-matrix');
          if (!svg || !db.prov_matrix || !db.prov_matrix.length) return;

          const provs = db.prov_matrix;
          let elements = '';

          if (activeProvMatrixView === 'budget_dev') {
            // View 1: Total Budget Outlay vs Development ADP
            const startY = 55, barH = 22, colGap = 72;
            const maxVal = 6000;
            const barMaxW = 280;
            const padX = 145;

            elements += `
              <text x="285" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#073c3a">Provincial Budget Outlays vs Development Allocations (FY 2024–25)</text>
              <g transform="translate(145, 36)">
                <rect x="0" y="0" width="12" height="12" fill="#0f766e" rx="2" />
                <text x="16" y="10" font-size="11" font-weight="600" fill="#334155">Total Outlay (PKR Billion)</text>
                <rect x="200" y="0" width="12" height="12" fill="#d97706" rx="2" />
                <text x="216" y="10" font-size="11" font-weight="600" fill="#334155">Development ADP (PKR Billion)</text>
              </g>
            `;

            provs.forEach((p, idx) => {
              const y = startY + idx * colGap;
              const wTotal = (p.total_budget_fy25_pkr_b / maxVal) * barMaxW;
              const wDev = (p.development_adp_pkr_b / maxVal) * barMaxW;

              elements += `
                <!-- Province Title -->
                <text x="${padX - 12}" y="${y + 16}" text-anchor="end" font-size="12" font-weight="700" fill="#1e293b">${p.province_name}</text>
                <text x="${padX - 12}" y="${y + 30}" text-anchor="end" font-size="9.5" font-weight="600" fill="#64748b">${p.development_share_pct}% for Dev</text>

                <!-- Total Outlay Bar -->
                <rect x="${padX}" y="${y}" width="${barMaxW}" height="${barH}" fill="#f1f5f9" rx="3" />
                <rect x="${padX}" y="${y}" width="${wTotal}" height="${barH}" fill="#0f766e" rx="3"
                  onmouseenter="showTooltip(event, '<strong>${p.province_name} Total Budget</strong><br/>Total Outlay: PKR ${fmt(p.total_budget_fy25_pkr_b)} Billion<br/>National Share: ${(p.total_budget_fy25_pkr_b / 11211.6 * 100).toFixed(1)}%')"
                  onmousemove="showTooltip(event, '<strong>${p.province_name} Total Budget</strong><br/>Total Outlay: PKR ${fmt(p.total_budget_fy25_pkr_b)} Billion<br/>National Share: ${(p.total_budget_fy25_pkr_b / 11211.6 * 100).toFixed(1)}%')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${padX + wTotal + 8}" y="${y + 15}" font-size="11" font-weight="800" fill="#0f766e">PKR ${fmt(p.total_budget_fy25_pkr_b)}B</text>

                <!-- Development ADP Bar -->
                <rect x="${padX}" y="${y + 26}" width="${barMaxW}" height="${barH - 4}" fill="#f1f5f9" rx="2" />
                <rect x="${padX}" y="${y + 26}" width="${wDev}" height="${barH - 4}" fill="#d97706" rx="2"
                  onmouseenter="showTooltip(event, '<strong>${p.province_name} Development ADP</strong><br/>ADP Allocation: PKR ${fmt(p.development_adp_pkr_b)} Billion<br/>Dev Share of Budget: ${p.development_share_pct}%')"
                  onmousemove="showTooltip(event, '<strong>${p.province_name} Development ADP</strong><br/>ADP Allocation: PKR ${fmt(p.development_adp_pkr_b)} Billion<br/>Dev Share of Budget: ${p.development_share_pct}%')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${padX + wDev + 8}" y="${y + 39}" font-size="10.5" font-weight="700" fill="#d97706">ADP: PKR ${fmt(p.development_adp_pkr_b)}B</text>
              `;
            });

            // Right Column: Donut of Provincial Development (ADP) Shares
            const totalDev = 2538.55;
            const cx = 740, cy = 195, r = 95, innerR = 55;
            let cumAngle = -Math.PI / 2;
            let paths = '';
            const slices = [
              { label: 'Sindh', val: 959.1, col: '#0f766e', pct: 37.8 },
              { label: 'Punjab', val: 842.0, col: '#0284c7', pct: 33.2 },
              { label: 'KP', val: 416.3, col: '#d97706', pct: 16.4 },
              { label: 'Balochistan', val: 321.15, col: '#e11d48', pct: 12.6 }
            ];

            slices.forEach(s => {
              const angle = (s.val / totalDev) * Math.PI * 2;
              const x1 = cx + r * Math.cos(cumAngle);
              const y1 = cy + r * Math.sin(cumAngle);
              const x2 = cx + r * Math.cos(cumAngle + angle);
              const y2 = cy + r * Math.sin(cumAngle + angle);
              const ix1 = cx + innerR * Math.cos(cumAngle + angle);
              const iy1 = cy + innerR * Math.sin(cumAngle + angle);
              const ix2 = cx + innerR * Math.cos(cumAngle);
              const iy2 = cy + innerR * Math.sin(cumAngle);
              const largeArc = angle > Math.PI ? 1 : 0;
              const d = `M ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} L ${ix1} ${iy1} A ${innerR} ${innerR} 0 ${largeArc} 0 ${ix2} ${iy2} Z`;

              paths += `<path d="${d}" fill="${s.col}" stroke="#ffffff" stroke-width="2"
                onmouseenter="showTooltip(event, '<strong>${s.label} ADP Share</strong><br/>PKR ${fmt(s.val)} Billion (${s.pct}%)')"
                onmousemove="showTooltip(event, '<strong>${s.label} ADP Share</strong><br/>PKR ${fmt(s.val)} Billion (${s.pct}%)')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />`;
              cumAngle += angle;
            });

            elements += `
              <g>
                <text x="${cx}" y="45" text-anchor="middle" font-size="12" font-weight="700" fill="#073c3a">Share of National Provincial ADP (PKR 2.54T)</text>
                ${paths}
                <circle cx="${cx}" cy="${cy}" r="${innerR}" fill="#ffffff" />
                <text x="${cx}" y="${cy - 7}" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b">TOTAL ADP</text>
                <text x="${cx}" y="${cy + 12}" text-anchor="middle" font-size="14" font-weight="800" fill="#073c3a">PKR 2.54T</text>
                <text x="${cx}" y="${cy + 25}" text-anchor="middle" font-size="9" font-weight="600" fill="#0f766e">FY 2024–25</text>

                <g transform="translate(615, 318)">
                  <rect x="0" y="0" width="10" height="10" fill="#0f766e" rx="2" />
                  <text x="14" y="9" font-size="10.5" font-weight="600" fill="#334155">Sindh: 37.8% (PKR 959B)</text>
                  <rect x="150" y="0" width="10" height="10" fill="#0284c7" rx="2" />
                  <text x="164" y="9" font-size="10.5" font-weight="600" fill="#334155">Punjab: 33.2% (PKR 842B)</text>
                  <rect x="0" y="18" width="10" height="10" fill="#d97706" rx="2" />
                  <text x="14" y="27" font-size="10.5" font-weight="600" fill="#334155">KP: 16.4% (PKR 416B)</text>
                  <rect x="150" y="18" width="10" height="10" fill="#e11d48" rx="2" />
                  <text x="164" y="27" font-size="10.5" font-weight="600" fill="#334155">Balochistan: 12.6% (PKR 321B)</text>
                </g>
              </g>
            `;
          } else if (activeProvMatrixView === 'debt_stock') {
            // View 2: Public Debt Stock & Borrowing
            const startY = 60, colGap = 74, padX = 145, barMaxW = 280, maxDebt = 1800;

            elements += `
              <text x="285" y="22" text-anchor="middle" font-size="13" font-weight="700" fill="#073c3a">Total Provincial Government Public Debt Stock (June 2024)</text>
              <g transform="translate(145, 34)">
                <rect x="0" y="0" width="12" height="12" fill="#7c3aed" rx="2" />
                <text x="16" y="10" font-size="11" font-weight="600" fill="#334155">Public Debt Stock (PKR Billion)</text>
              </g>
            `;

            provs.forEach((p, idx) => {
              const y = startY + idx * colGap;
              const wDebt = (p.public_debt_stock_pkr_b / maxDebt) * barMaxW;

              elements += `
                <text x="${padX - 12}" y="${y + 16}" text-anchor="end" font-size="12" font-weight="700" fill="#1e293b">${p.province_name}</text>
                <text x="${padX - 12}" y="${y + 30}" text-anchor="end" font-size="9.5" font-weight="600" fill="#7c3aed">${p.debt_external_share_pct}% External</text>

                <rect x="${padX}" y="${y}" width="${barMaxW}" height="24" fill="#f1f5f9" rx="3" />
                <rect x="${padX}" y="${y}" width="${wDebt}" height="24" fill="#7c3aed" rx="3"
                  onmouseenter="showTooltip(event, '<strong>${p.province_name} Public Debt</strong><br/>Total Debt: PKR ${fmt(p.public_debt_stock_pkr_b)} Billion<br/>External Share: ${p.debt_external_share_pct}%<br/>Debt Per Capita: PKR ${fmt(p.debt_per_capita_pkr)}')"
                  onmousemove="showTooltip(event, '<strong>${p.province_name} Public Debt</strong><br/>Total Debt: PKR ${fmt(p.public_debt_stock_pkr_b)} Billion<br/>External Share: ${p.debt_external_share_pct}%<br/>Debt Per Capita: PKR ${fmt(p.debt_per_capita_pkr)}')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${padX + wDebt + 8}" y="${y + 17}" font-size="12" font-weight="800" fill="#7c3aed">PKR ${fmt(p.public_debt_stock_pkr_b)}B</text>
              `;
            });

            // Right Column: Per Capita Debt Burden
            const rightPadX = 530, rightBarMaxW = 195, maxPerCapita = 25000;
            elements += `
              <g transform="translate(${rightPadX}, 22)">
                <text x="0" y="0" font-size="12.5" font-weight="700" fill="#073c3a">Debt Stock per Citizen (Per Capita Burden)</text>
                <text x="0" y="16" font-size="10" fill="#64748b">Smaller provinces carry higher debt per person despite lower totals</text>
            `;

            const sortedByDebtPerCap = provs.slice().sort((a,b) => b.debt_per_capita_pkr - a.debt_per_capita_pkr);
            sortedByDebtPerCap.forEach((p, idx) => {
              const y = 35 + idx * 56;
              const w = (p.debt_per_capita_pkr / maxPerCapita) * rightBarMaxW;
              elements += `
                <text x="125" y="${y + 14}" text-anchor="end" font-size="11" font-weight="700" fill="#334155">${p.province_name}</text>
                <rect x="135" y="${y}" width="${rightBarMaxW}" height="18" fill="#f1f5f9" rx="3" />
                <rect x="135" y="${y}" width="${w}" height="18" fill="#0284c7" rx="3"
                  onmouseenter="showTooltip(event, '<strong>${p.province_name} Debt per Citizen</strong><br/>Debt per Person: PKR ${fmt(p.debt_per_capita_pkr)}<br/>Population: ${fmt(p.population_2023)}')"
                  onmousemove="showTooltip(event, '<strong>${p.province_name} Debt per Citizen</strong><br/>Debt per Person: PKR ${fmt(p.debt_per_capita_pkr)}<br/>Population: ${fmt(p.population_2023)}')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${135 + w + 8}" y="${y + 14}" font-size="11" font-weight="800" fill="#0284c7">PKR ${fmt(p.debt_per_capita_pkr)}</text>
              `;
            });
            elements += `</g>`;
          } else if (activeProvMatrixView === 'conflict_burden') {
            // View 3: Conflict & Terrorism Burden (CRSS 2023–24)
            const cx = 175, cy = 200, r = 100, innerR = 58;
            let cumAngle = -Math.PI / 2;
            let paths = '';
            const totalFatalities = 4107;
            const conflictSlices = [
              { label: 'Khyber Pakhtunkhwa', val: 2591, pct: 63.1, col: '#e11d48' },
              { label: 'Balochistan', val: 1195, pct: 29.1, col: '#d97706' },
              { label: 'Sindh', val: 183, pct: 4.5, col: '#0f766e' },
              { label: 'Punjab', val: 138, pct: 3.4, col: '#64748b' }
            ];

            conflictSlices.forEach(s => {
              const angle = (s.val / totalFatalities) * Math.PI * 2;
              const x1 = cx + r * Math.cos(cumAngle);
              const y1 = cy + r * Math.sin(cumAngle);
              const x2 = cx + r * Math.cos(cumAngle + angle);
              const y2 = cy + r * Math.sin(cumAngle + angle);
              const ix1 = cx + innerR * Math.cos(cumAngle + angle);
              const iy1 = cy + innerR * Math.sin(cumAngle + angle);
              const ix2 = cx + innerR * Math.cos(cumAngle);
              const iy2 = cy + innerR * Math.sin(cumAngle);
              const largeArc = angle > Math.PI ? 1 : 0;
              const d = `M ${x1} ${y1} A ${r} ${r} 0 ${largeArc} 1 ${x2} ${y2} L ${ix1} ${iy1} A ${innerR} ${innerR} 0 ${largeArc} 0 ${ix2} ${iy2} Z`;

              paths += `<path d="${d}" fill="${s.col}" stroke="#ffffff" stroke-width="2"
                onmouseenter="showTooltip(event, '<strong>${s.label} Conflict Burden</strong><br/>Fatalities (2023–24): ${fmt(s.val)}<br/>National Share: ${s.pct}%')"
                onmousemove="showTooltip(event, '<strong>${s.label} Conflict Burden</strong><br/>Fatalities (2023–24): ${fmt(s.val)}<br/>National Share: ${s.pct}%')"
                onmouseleave="hideTooltip()" style="cursor:pointer;" />`;
              cumAngle += angle;
            });

            elements += `
              <g>
                <text x="${cx}" y="35" text-anchor="middle" font-size="12.5" font-weight="700" fill="#073c3a">Terrorism Fatalities Share (CRSS 2023–2024)</text>
                ${paths}
                <circle cx="${cx}" cy="${cy}" r="${innerR}" fill="#ffffff" />
                <text x="${cx}" y="${cy - 8}" text-anchor="middle" font-size="9.5" font-weight="800" fill="#e11d48">92.2% BURDEN</text>
                <text x="${cx}" y="${cy + 8}" text-anchor="middle" font-size="13" font-weight="800" fill="#073c3a">3,786 Deaths</text>
                <text x="${cx}" y="${cy + 22}" text-anchor="middle" font-size="9" font-weight="600" fill="#64748b">KP + Balochistan</text>

                <g transform="translate(45, 335)">
                  <rect x="0" y="0" width="10" height="10" fill="#e11d48" rx="2" />
                  <text x="14" y="9" font-size="10.5" font-weight="600" fill="#334155">KP: 63.1% (2,591)</text>
                  <rect x="140" y="0" width="10" height="10" fill="#d97706" rx="2" />
                  <text x="154" y="9" font-size="10.5" font-weight="600" fill="#334155">Balochistan: 29.1% (1,195)</text>
                  <rect x="0" y="18" width="10" height="10" fill="#0f766e" rx="2" />
                  <text x="14" y="27" font-size="10.5" font-weight="600" fill="#334155">Sindh: 4.5% (183)</text>
                  <rect x="140" y="18" width="10" height="10" fill="#64748b" rx="2" />
                  <text x="154" y="27" font-size="10.5" font-weight="600" fill="#334155">Punjab: 3.4% (138)</text>
                </g>
              </g>
            `;

            // Right Side: Conflict vs Budget Juxtaposition
            const rightPadX = 380, barW = 180;
            elements += `
              <g transform="translate(${rightPadX}, 25)">
                <text x="0" y="0" font-size="13" font-weight="700" fill="#073c3a">The Structural Paradox: Conflict Share vs Provincial Budget Share</text>
                <text x="0" y="16" font-size="10.5" fill="#64748b">Comparison between Terrorism Casualties (%) and Provincial Fiscal Allocation (%)</text>
                <g transform="translate(0, 26)">
                  <rect x="0" y="0" width="12" height="12" fill="#e11d48" rx="2" />
                  <text x="16" y="10" font-size="11" font-weight="600" fill="#334155">Terrorism Casualties Share (%)</text>
                  <rect x="220" y="0" width="12" height="12" fill="#0f766e" rx="2" />
                  <text x="236" y="10" font-size="11" font-weight="600" fill="#334155">Provincial Budget Share (%)</text>
                </g>
            `;

            const compData = [
              { name: 'Khyber Pakhtunkhwa', terr: 63.1, bud: 15.6, color: '#e11d48' },
              { name: 'Balochistan', terr: 29.1, bud: 8.5, color: '#d97706' },
              { name: 'Sindh', terr: 4.5, bud: 27.3, color: '#0f766e' },
              { name: 'Punjab', terr: 3.4, bud: 48.6, color: '#0284c7' }
            ];

            compData.forEach((cd, idx) => {
              const y = 55 + idx * 64;
              const wTerr = (cd.terr / 70) * barW;
              const wBud = (cd.bud / 70) * barW;

              elements += `
                <text x="0" y="${y + 12}" font-size="11.5" font-weight="700" fill="#1e293b">${cd.name}</text>
                <rect x="160" y="${y}" width="${wTerr}" height="14" fill="#e11d48" rx="2"
                  onmouseenter="showTooltip(event, '<strong>${cd.name} Conflict Exposure</strong><br/>Share of Fatalities: ${cd.terr}%')"
                  onmousemove="showTooltip(event, '<strong>${cd.name} Conflict Exposure</strong><br/>Share of Fatalities: ${cd.terr}%')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${160 + wTerr + 6}" y="${y + 11}" font-size="10" font-weight="800" fill="#e11d48">${cd.terr}% Deaths</text>

                <rect x="160" y="${y + 16}" width="${wBud}" height="14" fill="#0f766e" rx="2"
                  onmouseenter="showTooltip(event, '<strong>${cd.name} Budget Allocation</strong><br/>Share of Provincial Budget: ${cd.bud}%')"
                  onmousemove="showTooltip(event, '<strong>${cd.name} Budget Allocation</strong><br/>Share of Provincial Budget: ${cd.bud}%')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${160 + wBud + 6}" y="${y + 27}" font-size="10" font-weight="800" fill="#0f766e">${cd.bud}% Budget</text>
              `;
            });
            elements += `</g>`;
          } else {
            // View 4: Per Capita vs Territorial Density (km²)
            const startY = 65, padX = 145, barMaxW = 260;

            elements += `
              <text x="270" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#073c3a">Nominal Per Capita Budget vs Territorial Spread Disparity</text>
              <text x="270" y="42" text-anchor="middle" font-size="10.5" fill="#64748b">Balochistan leads in per capita budget but has by far the lowest infrastructure density</text>
            `;

            // Left Side: Per Capita Budget Outlay
            provs.forEach((p, idx) => {
              const y = startY + idx * 72;
              const wCap = (p.budget_per_capita_pkr / 70000) * barMaxW;

              elements += `
                <text x="${padX - 12}" y="${y + 14}" text-anchor="end" font-size="12" font-weight="700" fill="#1e293b">${p.province_name}</text>
                <text x="${padX - 12}" y="${y + 28}" text-anchor="end" font-size="9.5" font-weight="600" fill="#64748b">${fmt(p.population_2023)} Pop</text>

                <rect x="${padX}" y="${y}" width="${barMaxW}" height="20" fill="#f1f5f9" rx="3" />
                <rect x="${padX}" y="${y}" width="${wCap}" height="20" fill="#0f766e" rx="3"
                  onmouseenter="showTooltip(event, '<strong>${p.province_name} Per Capita Budget</strong><br/>Total Budget / Citizen: PKR ${fmt(p.budget_per_capita_pkr)}')"
                  onmousemove="showTooltip(event, '<strong>${p.province_name} Per Capita Budget</strong><br/>Total Budget / Citizen: PKR ${fmt(p.budget_per_capita_pkr)}')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${padX + wCap + 8}" y="${y + 14}" font-size="11.5" font-weight="800" fill="#0f766e">PKR ${fmt(p.budget_per_capita_pkr)}</text>
              `;
            });

            // Right Side: Development Spend per Square Kilometer
            const rightPadX = 520, rightBarMaxW = 195, maxSqKm = 8.0;
            elements += `
              <g transform="translate(${rightPadX}, 45)">
                <text x="0" y="0" font-size="12.5" font-weight="700" fill="#073c3a">Development Spend per km² (Infrastructure Density)</text>
                <text x="0" y="16" font-size="10" fill="#64748b">Development Rupees diluted across vast land area (PKR Million / km²)</text>
            `;

            provs.forEach((p, idx) => {
              const y = 30 + idx * 72;
              const wDensity = (p.dev_per_sqkm_pkr_m / maxSqKm) * rightBarMaxW;
              const isBaloch = p.province_id === 'PK-BA';

              elements += `
                <text x="125" y="${y + 14}" text-anchor="end" font-size="11" font-weight="700" fill="#334155">${p.province_name}</text>
                <text x="125" y="${y + 26}" text-anchor="end" font-size="9" fill="#64748b">${fmt(p.area_sqkm)} km²</text>
                <rect x="135" y="${y}" width="${rightBarMaxW}" height="20" fill="#f1f5f9" rx="3" />
                <rect x="135" y="${y}" width="${Math.max(wDensity, 6)}" height="20" fill="${isBaloch ? '#e11d48' : '#0284c7'}" rx="3"
                  onmouseenter="showTooltip(event, '<strong>${p.province_name} Dev Density</strong><br/>Dev Allocation / km²: PKR ${p.dev_per_sqkm_pkr_m} Million<br/>Total Area: ${fmt(p.area_sqkm)} km²')"
                  onmousemove="showTooltip(event, '<strong>${p.province_name} Dev Density</strong><br/>Dev Allocation / km²: PKR ${p.dev_per_sqkm_pkr_m} Million<br/>Total Area: ${fmt(p.area_sqkm)} km²')"
                  onmouseleave="hideTooltip()" style="cursor:pointer;" />
                <text x="${135 + Math.max(wDensity, 6) + 8}" y="${y + 14}" font-size="11" font-weight="800" fill="${isBaloch ? '#e11d48' : '#0284c7'}">PKR ${p.dev_per_sqkm_pkr_m}M / km²</text>
              `;
            });
            elements += `</g>`;
          }

          svg.innerHTML = elements;
        }

        // ================= VECTOR-ENGINE IMAGE & SVG EXPORT =================
        window.exportCard = function(cardId, format) {
          const card = document.getElementById(cardId);
          if (!card) return;

          const chartSvg = document.getElementById('svg-' + cardId);
          if (!chartSvg) return;

          const xmlText = function(str) {
            return (str || '')
              .replace(/&/g, '&amp;')
              .replace(/</g, '&lt;')
              .replace(/>/g, '&gt;')
              .replace(/"/g, '&quot;')
              .replace(/'/g, '&apos;');
          };

          const numBadge = card.querySelector('.vi-number-badge') ? card.querySelector('.vi-number-badge').innerText : 'INFOGRAPHIC';
          const tag = card.querySelector('.vi-card-tag') ? card.querySelector('.vi-card-tag').innerText : 'POLICY INFOGRAPHIC';
          const title = card.querySelector('.vi-card-title') ? card.querySelector('.vi-card-title').innerText : 'PPRI Policy Infographic';
          const subtitle = card.querySelector('.vi-card-subtitle') ? card.querySelector('.vi-card-subtitle').innerText : '';
          const source = card.querySelector('.vi-source') ? card.querySelector('.vi-source').innerText : 'Pakistan Bureau of Statistics / Ministry of Finance';
          const calloutEl = document.getElementById('callout-' + cardId);
          const calloutText = calloutEl ? calloutEl.innerText.replace(/[\r\n]+/g, ' ') : '';

          const safeNumBadge = xmlText(numBadge);
          const safeTag = xmlText(tag);
          const safeTitle = xmlText(title);
          const safeSubtitle = xmlText(subtitle);
          const safeSource = xmlText(source);
          const cleanSource = safeSource.replace(/\s*•\s*PPRI\s*$/i, '').trim();
          const rawCallout = calloutText.length > 220 ? calloutText.substring(0, 217) + '...' : calloutText;
          const safeCallout = xmlText(rawCallout);

          const isWide = card.classList.contains('col-12');
          const exportW = isWide ? 1040 : 800;
          const exportH = isWide ? 680 : 620;

          const innerChartSvg = chartSvg.innerHTML;
          const viewBox = chartSvg.getAttribute('viewBox') || '0 0 600 360';
          const vbParts = viewBox.split(' ');
          const origW = parseFloat(vbParts[2]) || 600;
          const origH = parseFloat(vbParts[3]) || 360;

          const targetChartW = exportW - 80;
          const targetChartH = exportH - 240;
          const scale = Math.min(targetChartW / origW, targetChartH / origH);
          const transX = (exportW - origW * scale) / 2;
          const transY = 115;

          const fullSvg = `
<svg xmlns="http://www.w3.org/2000/svg" width="${exportW}" height="${exportH}" viewBox="0 0 ${exportW} ${exportH}">
  <defs>
    <style>
      text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <rect width="${exportW}" height="${exportH}" fill="#ffffff" rx="10" stroke="#cbd5e1" stroke-width="1"/>
  <rect width="${exportW}" height="6" fill="#0f766e" rx="4"/>

  <!-- Top Header with Number Badge -->
  <text x="40" y="38" font-size="11" font-weight="700" fill="#0f766e" letter-spacing="1">PAKISTAN PROVINCIAL REFORM INSTITUTE (PPRI) • ${safeNumBadge} • ${safeTag}</text>
  <text x="40" y="66" font-size="20" font-weight="800" fill="#073c3a">${safeTitle}</text>
  <text x="40" y="88" font-size="12" fill="#64748b">${safeSubtitle}</text>
  <line x1="40" y1="102" x2="${exportW - 40}" y2="102" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Core Visual Graphics -->
  <g transform="translate(${transX}, ${transY}) scale(${scale})">
    ${innerChartSvg}
  </g>

  <!-- Key Insight Box -->
  <rect x="40" y="${exportH - 110}" width="${exportW - 80}" height="48" fill="#f8fafc" rx="6" stroke="#e2e8f0" stroke-width="1"/>
  <text x="54" y="${exportH - 93}" font-size="10" font-weight="800" fill="#073c3a">KEY POLICY INSIGHT:</text>
  <text x="54" y="${exportH - 77}" font-size="11" fill="#334155">${safeCallout}</text>

  <!-- Watermark Footer Banner (Two-Line Stacked: Zero Overlap) -->
  <rect x="0" y="${exportH - 52}" width="${exportW}" height="52" fill="#073c3a" rx="0"/>
  <!-- Line 1: Primary Data Source (Full Canvas Width) -->
  <text x="40" y="${exportH - 31}" font-size="10.5" font-weight="500" fill="#99f6e4">${cleanSource}</text>
  <!-- Line 2: Institution Branding & Canonical Domain -->
  <text x="40" y="${exportH - 14}" font-size="10.5" font-weight="700" fill="#ffffff">Pakistan Provincial Reform Institute (PPRI)</text>
  <text x="${exportW - 40}" y="${exportH - 14}" font-size="10.5" font-weight="600" fill="#5eead4" text-anchor="end">ppripakistan.github.io</text>
</svg>
          `.trim();

          // Tier 2: Automated XML Sanitizer to replace any stray HTML entities with valid XML/UTF-8
          let cleanSvg = fullSvg
            .replace(/&bull;/g, '•')
            .replace(/&rarr;/g, '→')
            .replace(/&ge;/g, '≥')
            .replace(/&le;/g, '≤')
            .replace(/&sim;/g, '~')
            .replace(/&radic;/g, '√')
            .replace(/&times;/g, '×')
            .replace(/&plusmn;/g, '±')
            .replace(/&nbsp;/g, ' ');

          // Ensure any bare ampersands not part of valid XML entities or char refs are escaped
          cleanSvg = cleanSvg.replace(/&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9a-fA-F]+;)/g, '&amp;');

          const baseFileName = `PPRI_Infographic_${cardId.replace('card-', '')}`;

          if (format === 'svg') {
            const blob = new Blob([cleanSvg], { type: 'image/svg+xml;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `${baseFileName}.svg`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
            showToast(`Downloaded Vector Infographic: ${baseFileName}.svg`);
          } else {
            const canvas = document.getElementById('vi-export-canvas');
            const ctx = canvas.getContext('2d');
            const dpr = 2;
            canvas.width = exportW * dpr;
            canvas.height = exportH * dpr;

            const img = new Image();
            const blob = new Blob([cleanSvg], { type: 'image/svg+xml;charset=utf-8' });
            const url = URL.createObjectURL(blob);

            img.onload = function() {
              ctx.fillStyle = '#ffffff';
              ctx.fillRect(0, 0, canvas.width, canvas.height);
              ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
              URL.revokeObjectURL(url);

              const pngData = canvas.toDataURL('image/png');
              const a = document.createElement('a');
              a.href = pngData;
              a.download = `${baseFileName}.png`;
              document.body.appendChild(a);
              a.click();
              document.body.removeChild(a);
              showToast(`Downloaded Complete 2x Retina PNG: ${baseFileName}.png`);
            };

            img.onerror = function() {
              const a = document.createElement('a');
              a.href = url;
              a.download = `${baseFileName}.svg`;
              document.body.appendChild(a);
              a.click();
              document.body.removeChild(a);
              URL.revokeObjectURL(url);
              showToast(`Exported as Vector Graphic: ${baseFileName}.svg`);
            };

            img.src = url;
          }
        };

        // Clean CSV Data Export with UTF-8 BOM
        window.exportCSV = function(datasetKey) {
          const url = `/data/curated/${datasetKey}.csv`;
          fetch(url)
            .then(res => {
              if (!res.ok) throw new Error('File not found');
              return res.text();
            })
            .then(csvText => {
              const blob = new Blob(['\uFEFF' + csvText], { type: 'text/csv;charset=utf-8;' });
              const link = document.createElement('a');
              link.href = URL.createObjectURL(blob);
              link.download = `PPRI_Data_${datasetKey}.csv`;
              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
              showToast(`Exported Clean CSV: PPRI_Data_${datasetKey}.csv`);
            })
            .catch(() => {
              showToast(`Error: Dataset ${datasetKey}.csv not available`);
            });
        };

        // 2. ISOLATED RESILIENT INITIAL RENDER
        function renderAllCards() {
          const cardRenderers = [
            { name: 'Card 01 (Fiscal)', fn: renderCard1Fiscal },
            { name: 'Card 02 (Debt)', fn: renderCard2Debt },
            { name: 'Card 03 (Tax Exp)', fn: renderCard3TaxExp },
            { name: 'Card 04 (Gender Land)', fn: renderCard4GenderLand },
            { name: 'Card 05 (HIES Food)', fn: renderCard5Hies },
            { name: 'Card 06 (Consumption Pie)', fn: renderCard6ConsumptionPie },
            { name: 'Card 07 (Wage Infl)', fn: renderCard7WageInfl },
            { name: 'Card 08 (Services)', fn: renderCard8Services },
            { name: 'Card 09 (LFS Disparities)', fn: renderCard9Lfs },
            { name: 'Card 10 (Census Shifts)', fn: renderCard10CensusShifts },
            { name: 'Card 11 (Districts Scatter)', fn: renderCard11DistrictsScatter },
            { name: 'Card 12 (Sector Employment)', fn: renderCard12SectorEmployment },
            { name: 'Card 13 (Agri Shifts)', fn: renderCard13AgriShifts },
            { name: 'Card 14 (Census Hist)', fn: renderCard14CensusHist },
            { name: 'Card 15 (Macro)', fn: renderCard15Macro },
            { name: 'Card 16 (Prov Matrix)', fn: renderCard16ProvMatrix }
          ];

          cardRenderers.forEach(c => {
            try {
              c.fn();
            } catch (err) {
              console.error(`[PPRI Error] Failed rendering ${c.name}:`, err);
            }
          });
        }

        // Render immediately using embedded in-memory data
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', renderAllCards);
        } else {
          renderAllCards();
        }

      })();
    </script>
  </body>
</html>
'''
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Successfully generated {OUTPUT_FILE} ({len(html_content)} bytes)")

if __name__ == '__main__':
    generate_insights_html()
