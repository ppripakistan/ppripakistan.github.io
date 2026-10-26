#!/usr/bin/env python3
"""
scripts/build_observatory_hubs.py
Builds the 8 authoritative thematic hubs for the PPRI Pakistan Data Observatory,
complete with zero-dependency interactive SVG charts, sortable data tables,
official CSV download actions, and rich "Context & Policy Analysis" cross-links.
"""

import os
import json
import csv
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
MASTER_DIR = os.path.join(DATA_DIR, "master")

def get_common_header(active_nav="data"):
    return """    <a class="skip-link" href="#main-content">Skip to content</a>
    <header class="site-header">
      <div class="container navbar">
        <a class="brand" href="/index.html">
          <img src="/assets/images/brand/ppri-logo-header.jpg" alt="PPRI logo" width="38" height="38" loading="eager" decoding="async" />
          <span class="brand-text"><strong>PPRI</strong><span>Pakistan Provincial Reform Institute</span></span>
        </a>
        <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-navigation">Menu</button>
        <nav id="site-navigation" class="nav-links" aria-label="Primary navigation">
          <a href="/index.html">Home</a>
          <a href="/research/index.html">Research</a>
          <a href="/provinces/index.html">Reform</a>
          <a href="/data/centre.html" aria-current="page">Data</a>
          <a href="/publications/index.html">Publications</a>
          <a href="/consultation/index.html">Engage</a>
          <a href="/about.html">About</a>
          <a class="nav-search" href="/search.html">Search</a>
        </nav>
      </div>
    </header>"""

def get_common_footer():
    return """    <footer class="site-footer">
      <div class="container footer-grid">
        <div>
          <img src="/assets/images/brand/ppri-logo-header.jpg" alt="PPRI — Pakistan Provincial Reform Institute" class="footer-logo" width="38" height="38" loading="lazy" decoding="async" />
          <p>Pakistan Provincial Reform Institute</p>
          <p>Non-partisan research, empirical data observatories, and cartographic analysis on governance, provincial reform, and decentralization in Pakistan.</p>
        </div>
        <div>
          <h3>Data Observatory</h3>
          <ul class="footer-links">
            <li><a href="/data/centre.html">Observatory Hub &amp; Map</a></li>
            <li><a href="/data/population/">Population &amp; Cities</a></li>
            <li><a href="/data/economy/">Economy &amp; Inflation</a></li>
            <li><a href="/data/living-standards/">Living Standards &amp; Income</a></li>
            <li><a href="/data/public-finance/">Public Finance &amp; NFC</a></li>
            <li><a href="/data/education/">Education &amp; Literacy</a></li>
            <li><a href="/data/health/">Public Health</a></li>
            <li><a href="/data/digital-access/">Digital Access</a></li>
            <li><a href="/data/compare/">Provinces Comparator</a></li>
            <li><a href="/knowledge-library/">Knowledge Library</a></li>
            <li><a href="/data/downloads/">Open Data Downloads</a></li>
          </ul>
        </div>
        <div>
          <h3>Research &amp; Policy</h3>
          <ul class="footer-links">
            <li><a href="/research/policy-papers/provincial-reorganization-of-pakistan.html">Flagship Reorganization</a></li>
            <li><a href="/research/reports/income-went-up-why-does-life-feel-harder.html">Income &amp; Inflation Report</a></li>
            <li><a href="/research/reports/does-money-work-better-spent-closer-to-people.html">Fiscal Decentralization</a></li>
            <li><a href="/research/reports/same-country-different-life-district-access.html">Spatial Inequality</a></li>
            <li><a href="/articles/four-provinces-241-million-people-administrative-scale.html">Administrative Scale</a></li>
            <li><a href="/articles/index.html">All Policy Articles</a></li>
          </ul>
        </div>
        <div>
          <h3>Connect</h3>
          <ul class="footer-links">
            <li><a href="https://x.com/PPRI_Pakistan" rel="me">X / @PPRI_Pakistan</a></li>
            <li><a href="/consultation/index.html">Public Consultation</a></li>
            <li><a href="/contact.html">Contact Us</a></li>
          </ul>
        </div>
      </div>
      <div class="container footer-bottom">
        <span>&copy; <span data-current-year>2026</span> Pakistan Provincial Reform Institute</span>
        <span><a href="/privacy.html">Privacy</a> &middot; <a href="/terms.html">Terms</a> &middot; <a href="/sitemap.xml">Sitemap</a></span>
      </div>
    </footer>"""

def get_observatory_nav_rail(active_slug):
    rail_items = [
        ("centre", "/data/centre.html", "🌐 Overview &amp; Map"),
        ("population", "/data/population/", "👥 Population &amp; Cities"),
        ("economy", "/data/economy/", "📈 Economy &amp; Inflation"),
        ("living-standards", "/data/living-standards/", "🏠 Living Standards"),
        ("public-finance", "/data/public-finance/", "⚖️ Public Finance &amp; NFC"),
        ("education", "/data/education/", "🎓 Education"),
        ("health", "/data/health/", "🏥 Health"),
        ("digital-access", "/data/digital-access/", "🌐 Digital Access"),
        ("compare", "/data/compare/", "📊 Compare"),
        ("knowledge-library", "/knowledge-library/", "★ Knowledge Library")
    ]
    pills = []
    for slug, url, label in rail_items:
        active_class = ' active" style="background:var(--obs-primary);color:#fff;border-color:var(--obs-primary);' if slug == active_slug else '"'
        pills.append(f'<a href="{url}" class="obs-query-chip{active_class}>{label}</a>')
    
    return f"""        <div style="background:#ffffff;border:1px solid var(--obs-border);border-radius:var(--obs-radius-md);padding:14px 18px;margin-bottom:28px;box-shadow:var(--obs-shadow);">
          <div style="font-size:0.8rem;font-weight:700;color:var(--obs-text-muted);text-transform:uppercase;letter-spacing:0.05em;margin-bottom:8px;">Observatory Thematic Hubs</div>
          <div style="display:flex;flex-wrap:wrap;gap:8px;">
            {''.join(pills)}
          </div>
        </div>"""

def get_related_research_section(papers):
    cards_html = []
    for p in papers:
        badge_color = "#e0f2fe;color:#0369a1;" if p.get('type') == 'Report' else "#fef3c7;color:#92400e;" if p.get('type') == 'Policy Paper' else "#dcfce7;color:#166534;"
        cards_html.append(f"""          <div class="obs-stat-card" style="padding:22px;">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
              <span class="obs-badge" style="background:{badge_color}font-weight:700;">{p['type']}</span>
              <span style="font-size:0.8rem;color:var(--obs-text-muted);font-weight:600;">{p['read_time']}</span>
            </div>
            <h3 style="margin:0 0 10px 0;font-size:1.15rem;line-height:1.4;">
              <a href="{p['url']}" style="color:var(--obs-dark);text-decoration:none;">{p['title']}</a>
            </h3>
            <p style="font-size:0.9rem;color:var(--obs-text);line-height:1.55;margin:0 0 16px 0;">{p['summary']}</p>
            <div style="margin-top:auto;">
              <a href="{p['url']}" class="obs-source-link" style="font-weight:700;">Read Policy Analysis &rarr;</a>
            </div>
          </div>""")
    
    return f"""        <section class="obs-section" style="margin-top:36px;border-top:3px solid var(--obs-accent);">
          <div class="obs-section-header" style="margin-bottom:18px;">
            <div>
              <span class="obs-badge obs-badge-survey">&bull; Context &amp; Governance Implications</span>
              <h2 class="obs-section-title" style="margin-top:6px;">What Does This Data Mean for Pakistan? Related Policy Research</h2>
              <p style="margin:4px 0 0 0;font-size:0.95rem;color:var(--obs-text-muted);">
                Empirical evidence is the foundation of institutional reform. Explore peer-reviewed PPRI policy papers, working papers, and empirical analyses addressing these findings.
              </p>
            </div>
            <a href="/research/index.html" class="obs-btn obs-btn-outline">All Research Papers &rarr;</a>
          </div>
          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:20px;">
            {''.join(cards_html)}
          </div>
        </section>"""

HUBS_CONFIG = {
    "population": {
        "slug": "population",
        "title": "Pakistan Population, Demographics & Urbanization Data",
        "h1": "Pakistan Population, Demographics &amp; Urbanization",
        "description": "Verified Pakistan Bureau of Statistics 7th Census 2023 results: 241.49M national population, provincial breakdowns, urban-rural distributions, sex ratios, and top 22 city populations.",
        "canonical": "https://ppripakistan.github.io/data/population/",
        "csv_download": "/data/downloads/pakistan-population-census-2023.csv",
        "stats": [
            ("241.49M", "National Population", "PBS Census 2023 (+2.55%/yr)", "PBS Census Table 1"),
            ("38.8%", "Urbanization Share", "93.75M in urban localities", "Census Urban/Rural"),
            ("6.30", "Avg Household Size", "Persons per household", "PBS Census Table 4"),
            ("20.38M", "Karachi Locality Pop.", "Pakistan's largest urban center", "PBS Major Localities")
        ],
        "chart_title": "Census 2023 Provincial Population Distribution (Millions)",
        "chart_data": [
            {"label": "Punjab", "value": 127.69, "formattedValue": "127.7M (52.9%)", "color": "#073c3a"},
            {"label": "Sindh", "value": 55.70, "formattedValue": "55.7M (23.1%)", "color": "#0f766e"},
            {"label": "KP", "value": 40.86, "formattedValue": "40.9M (16.9%)", "color": "#0284c7"},
            {"label": "Balochistan", "value": 14.89, "formattedValue": "14.9M (6.2%)", "color": "#d97706"},
            {"label": "Islamabad", "value": 2.36, "formattedValue": "2.4M (1.0%)", "color": "#64748b"}
        ],
        "table_headers": ["Indicator / Geographic Unit", "2023 Census Figure", "National Share", "Growth Rate (2017–23)", "Source"],
        "table_rows": [
            ["Pakistan (National Total)", "241,499,431", "100.0%", "2.55% / yr", "PBS Census 2023 Table 1"],
            ["Punjab (PK-PB)", "127,688,922", "52.87%", "2.53% / yr", "PBS Census 2023 Table 1"],
            ["Sindh (PK-SD)", "55,696,147", "23.06%", "2.57% / yr", "PBS Census 2023 Table 1"],
            ["Khyber Pakhtunkhwa (PK-KP)", "40,856,097", "16.92%", "2.38% / yr", "PBS Census 2023 Table 1"],
            ["Balochistan (PK-BA)", "14,894,402", "6.17%", "3.20% / yr", "PBS Census 2023 Table 1"],
            ["Islamabad Capital Territory (PK-ICT)", "2,363,863", "0.98%", "2.80% / yr", "PBS Census 2023 Table 1"],
            ["Male Population", "124,324,591", "51.48%", "—", "PBS Census Table 2"],
            ["Female Population", "117,153,066", "48.51%", "—", "PBS Census Table 2"],
            ["Transgender Population", "21,774", "0.01%", "—", "PBS Census Table 2"],
            ["Karachi Urban Locality", "20,382,881", "8.44%", "2.41% / yr", "PBS Major Localities"],
            ["Lahore Urban Locality", "13,004,135", "5.38%", "2.71% / yr", "PBS Major Localities"],
            ["Faisalabad Urban Locality", "3,691,999", "1.53%", "2.10% / yr", "PBS Major Localities"],
            ["Rawalpindi Urban Locality", "3,357,612", "1.39%", "2.35% / yr", "PBS Major Localities"],
            ["Gujranwala Urban Locality", "2,511,118", "1.04%", "2.22% / yr", "PBS Major Localities"],
            ["Multan Urban Locality", "2,215,381", "0.92%", "2.15% / yr", "PBS Major Localities"],
            ["Hyderabad Urban Locality", "2,199,463", "0.91%", "2.28% / yr", "PBS Major Localities"],
            ["Peshawar Urban Locality", "2,112,500", "0.87%", "2.45% / yr", "PBS Major Localities"],
            ["Quetta Urban Locality", "1,565,000", "0.65%", "3.41% / yr", "PBS Major Localities"]
        ],
        "citation": "Pakistan Bureau of Statistics. (2023). 7th Population & Housing Census 2023: Key Findings and Provincial Tables. Government of Pakistan.",
        "related_research": [
            {
                "type": "Article",
                "title": "Four Provinces, 241.5 Million People: Has Pakistan Outgrown Its Administrative Structure?",
                "url": "/articles/four-provinces-241-million-people-administrative-scale.html",
                "read_time": "9 min read",
                "summary": "Pakistan's four provinces average over 60 million citizens each, creating an extreme administrative burden unmatched among democratic federations globally."
            },
            {
                "type": "Article",
                "title": "Can Pakistan Grow Beyond Its Provincial Capitals? Secondary Cities and Urban Growth",
                "url": "/articles/can-pakistan-grow-beyond-provincial-capitals-secondary-cities.html",
                "read_time": "8 min read",
                "summary": "Census 2023 confirms rapid secondary urbanization in Faisalabad, Rawalpindi, and Gujranwala, yet infrastructure investments remain disproportionately concentrated in provincial capitals."
            },
            {
                "type": "Policy Paper",
                "title": "The Provincial Reorganization of Pakistan: Flagship Institutional Proposal",
                "url": "/research/policy-papers/provincial-reorganization-of-pakistan.html",
                "read_time": "25 min read",
                "summary": "Detailed constitutional and administrative model for establishing smaller, functionally responsive provinces aligned with Pakistan's demographic realities."
            },
            {
                "type": "Article",
                "title": "Provinces of Pakistan: Names, Capitals, Population & Administrative Units",
                "url": "/articles/provinces-of-pakistan-names-capitals-population.html",
                "read_time": "6 min read",
                "summary": "A comprehensive factual reference guide to Pakistan's 4 provinces, Islamabad territory, 164 districts, and administrative divisions."
            }
        ]
    },
    "economy": {
        "slug": "economy",
        "title": "Pakistan Economy, Inflation & Market Benchmarks Data",
        "h1": "Pakistan Macroeconomy, Inflation &amp; Markets",
        "description": "Verified economic indicators: CPI & SPI inflation indices, real GDP growth rates, sector contributions, foreign exchange rates, workers remittances, and wage rates.",
        "canonical": "https://ppripakistan.github.io/data/economy/",
        "csv_download": "/data/downloads/pakistan-economic-benchmarks-2026.csv",
        "stats": [
            ("10.26%", "National CPI Inflation", "Year-on-Year latest bulletin", "PBS Price Statistics"),
            ("3.70%", "Real GDP Growth", "Targeted growth for FY2026", "PES 2025–26"),
            ("$1,680", "GDP Per Capita", "Current USD per person", "National Accounts"),
            ("Rs 39,042", "Mean Monthly Wage", "PBS Labour Force Survey", "LFS Official Benchmark")
        ],
        "chart_title": "Sectoral Contribution & Economic Growth Rates (%)",
        "chart_data": [
            {"label": "Services", "value": 4.09, "formattedValue": "4.09%", "color": "#073c3a"},
            {"label": "Industry", "value": 3.51, "formattedValue": "3.51%", "color": "#0f766e"},
            {"label": "Agriculture", "value": 2.89, "formattedValue": "2.89%", "color": "#0284c7"},
            {"label": "Overall GDP", "value": 3.70, "formattedValue": "3.70%", "color": "#d97706"},
            {"label": "LSM Growth", "value": 10.37, "formattedValue": "10.37%", "color": "#16a34a"}
        ],
        "table_headers": ["Economic Indicator", "Current Value", "Prior Period", "Update Period", "Primary Source"],
        "table_rows": [
            ["Consumer Price Index (CPI) YoY", "10.26%", "28.3%", "Monthly Bulletin", "PBS Monthly CPI Bulletin"],
            ["CPI Urban YoY", "10.50%", "30.1%", "Monthly Bulletin", "PBS Monthly CPI Bulletin"],
            ["CPI Rural YoY", "10.10%", "26.5%", "Monthly Bulletin", "PBS Monthly CPI Bulletin"],
            ["Sensitive Price Indicator (SPI) YoY", "8.40%", "25.2%", "Weekly Bulletin", "PBS SPI Price Monitoring"],
            ["Wholesale Price Index (WPI) YoY", "13.30%", "24.1%", "Monthly Bulletin", "PBS Wholesale Bulletins"],
            ["Real GDP Growth Rate (Annual)", "3.70%", "2.12%", "Annual FY", "Pakistan Economic Survey"],
            ["Quarterly Real GDP Growth (Q1)", "3.99%", "2.40%", "Q1 National Accounts", "PBS National Accounts"],
            ["Large Scale Manufacturing (LSM)", "10.37%", "-2.1%", "Cumulative FY", "PBS Industrial Output"],
            ["Per Capita Income (USD)", "$1,901", "$1,680", "Annual Benchmark", "PES National Accounts"],
            ["Investment Share of GDP", "14.38%", "13.6%", "Annual Benchmark", "State Bank of Pakistan"],
            ["National Savings Share of GDP", "14.13%", "13.0%", "Annual Benchmark", "State Bank of Pakistan"],
            ["Domestic Savings Share of GDP", "7.03%", "6.8%", "Annual Benchmark", "State Bank of Pakistan"],
            ["IT & Telecom Software Exports", "$3,388 Million", "$2,596M", "Annual Benchmark", "SBP Export Receipts"],
            ["Average Monthly Wage (National)", "PKR 39,042", "PKR 34,200", "Labour Survey", "PBS Labour Force Survey"],
            ["Provincial Minimum Wage (Punjab/Sindh)", "PKR 37,000", "PKR 32,000", "Gazette 2025–26", "Provincial Labor Depts"]
        ],
        "citation": "State Bank of Pakistan & Pakistan Bureau of Statistics. (2025). Monthly Inflation Monitor & Pakistan Economic Survey 2025–26. Ministry of Finance, Islamabad.",
        "related_research": [
            {
                "type": "Report",
                "title": "Income Went Up. So Why Does Life Feel Harder? Inflation & Household Purchasing Power",
                "url": "/research/reports/income-went-up-why-does-life-feel-harder.html",
                "read_time": "14 min read",
                "summary": "Analyzing how double-digit food inflation and energy tariffs eroded real wages across Pakistani households despite nominal income growth."
            },
            {
                "type": "Article",
                "title": "Where Does Pakistan's Development Money Go? Federal, Provincial and Regional Priorities",
                "url": "/articles/where-does-pakistans-development-money-go.html",
                "read_time": "11 min read",
                "summary": "An empirical audit of Public Sector Development Programme (PSDP) allocations revealing deep structural imbalances between federal mega-projects and local basic services."
            },
            {
                "type": "Report",
                "title": "The Price of a Simple Task: Bureaucratic Friction & Economic Cost in Pakistan",
                "url": "/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html",
                "read_time": "12 min read",
                "summary": "Quantifying the economic loss and citizen hours wasted in routine interactions with government departments, revenue offices, and regulatory hurdles."
            }
        ]
    },
    "living-standards": {
        "slug": "living-standards",
        "title": "Pakistan Living Standards, Poverty & Household Income Data",
        "h1": "Living Standards, Income &amp; Well-Being",
        "description": "Verified findings from PBS Household Integrated Economic Survey (HIES) 2024–25: household income quintiles, monthly consumption patterns, drinking water access, and energy infrastructure.",
        "canonical": "https://ppripakistan.github.io/data/living-standards/",
        "csv_download": "/data/downloads/pakistan-household-income-consumption-hies-2024-25.csv",
        "stats": [
            ("PKR 82,179", "Mean Monthly Income", "HIES 2024–25 Economic Report, Fig. 1", "Pakistan Bureau of Statistics"),
            ("PKR 79,150", "Monthly Consumption", "HIES 2024–25 Economic Report, §3.7", "Pakistan Bureau of Statistics"),
            ("97%", "Improved Drinking-Water Source", "Source classification; not a water-safety test", "PBS HIES 2024–25 Social Report"),
            ("96%", "Electricity / Solar Lighting", "Main lighting source is electricity or solar", "PBS HIES 2024–25 Social Report")
        ],
        "chart_title": "Average Monthly Household Income by Consumption Quintile (HIES 2024–25 PKR)",
        "chart_data": [
            {"label": "1st Quintile (Poorest)", "value": 41851, "formattedValue": "Rs 41,851", "color": "#d97706"},
            {"label": "2nd Quintile", "value": 55138, "formattedValue": "Rs 55,138", "color": "#0284c7"},
            {"label": "3rd Quintile (Middle)", "value": 65741, "formattedValue": "Rs 65,741", "color": "#0f766e"},
            {"label": "4th Quintile", "value": 80387, "formattedValue": "Rs 80,387", "color": "#073c3a"},
            {"label": "5th Quintile (Richest)", "value": 139317, "formattedValue": "Rs 139,317", "color": "#16a34a"}
        ],
        "table_headers": ["Living Standard Metric", "National Benchmark", "Urban Share", "Rural Share", "Survey Source"],
        "table_rows": [
            ["Mean Monthly Household Income", "PKR 82,179", "PKR 96,767", "PKR 72,157", "PBS HIES 2024–25, §3.5 / Table 3.5.A"],
            ["Mean Monthly Household Consumption", "PKR 79,150", "PKR 95,533", "PKR 67,894", "PBS HIES 2024–25, §3.7 / Table 3.6.A"],
            ["Average Household Size (HIES)", "5.98 Persons", "5.69 Persons", "6.18 Persons", "PBS HIES 2024–25, Table 4"],
            ["Income Share: Wages & Salaries", "42.00%", "50.27%", "34.38%", "PBS HIES 2024–25, Table 3.5.B"],
            ["Income Share: Crop Production", "6.89%", "1.64%", "11.73%", "PBS HIES 2024–25, Table 3.5.B"],
            ["Income Share: Livestock", "7.07%", "1.78%", "11.94%", "PBS HIES 2024–25, Table 3.5.B"],
            ["Income Share: Other Non-Agricultural Activities", "16.25%", "20.36%", "12.47%", "PBS HIES 2024–25, Table 3.5.B"],
            ["Income Share: Foreign Remittances", "7.77%", "5.89%", "9.50%", "PBS HIES 2024–25, Table 3.5.B"],
            ["Income Share: Domestic Remittances", "3.77%", "2.41%", "5.02%", "PBS HIES 2024–25, Table 3.5.B"],
            ["Improved drinking-water source", "97%", "99%", "95%", "PBS HIES 2024–25 Social Report, SDG indicator summary"],
            ["Improved drinking-water source within premises", "79%", "—", "—", "PBS HIES 2024–25 Social Report; within premises, not necessarily inside the dwelling"],
            ["Drinking-water source inside the dwelling", "65%", "—", "—", "PBS HIES 2024–25 Social Report, detailed WASH section; inside dwelling is narrower than within premises"],
            ["Tap water as main drinking-water source", "22%", "—", "14%", "PBS HIES 2024–25 Social Report; 14% rural; main source, not all piped access"],
            ["Improved sanitation facility not shared with another household", "74%", "—", "—", "PBS HIES 2024–25 Social Report, SDG 6.2.1a; differs from flush-toilet access"],
            ["Households using a flush toilet", "89%", "98%", "82%", "PBS HIES 2024–25 Social Report, detailed WASH section"],
            ["Handwashing facility with both soap and water", "64%", "—", "—", "PBS HIES 2024–25 Social Report"],
            ["Electricity or solar as main lighting source", "96%", "98%", "94%", "PBS HIES 2024–25 Social Report; does not mean grid-only connection"],
            ["Clean fuels/technology for cooking, lighting and heating", "38%", "74%", "13%", "PBS HIES 2024–25 Social Report, composite clean-fuel indicator"],
            ["Gas as main cooking fuel", "47%", "84%", "22%", "PBS HIES 2024–25 Social Report; differs from composite clean-fuel indicator"],
            ["Household ownership of dwelling", "82%", "74%", "88%", "PBS HIES 2024–25 Social Report"],
        ],
        "citation": "Pakistan Bureau of Statistics. (2025). Household Integrated Economic Survey (HIES) 2024–25: Key Indicators on Income, Consumption, and Living Conditions. Government of Pakistan.",
        "related_research": [
            {
                "type": "Report",
                "title": "Same Country, Different Life: District-Level Spatial Inequality Across Pakistan",
                "url": "/research/reports/same-country-different-life-district-access.html",
                "read_time": "15 min read",
                "summary": "Revealing extreme contrasts where a child in an urban center experiences 90%+ basic amenity access while peripheral districts face near-total infrastructural absence."
            },
            {
                "type": "Report",
                "title": "Income Went Up. So Why Does Life Feel Harder? Analyzing Household Vulnerability",
                "url": "/research/reports/income-went-up-why-does-life-feel-harder.html",
                "read_time": "14 min read",
                "summary": "A deep empirical examination of the bottom two income quintiles, where over 60% of monthly spending goes directly to bare subsistence nutrition and power."
            },
            {
                "type": "Report",
                "title": "The Bribe You Can't See: Corruption as an Invisible Regressive Tax on Poor Citizens",
                "url": "/research/reports/bribe-you-cant-see-corruption-private-tax.html",
                "read_time": "13 min read",
                "summary": "Documenting how informal extortion and administrative delays disproportionately penalize low-income citizens attempting to access basic services and entitlements."
            }
        ]
    },
    "public-finance": {
        "slug": "public-finance",
        "title": "Pakistan Public Finance, Budgets & NFC Award Formula Data",
        "h1": "Public Finance, Federal Budgets &amp; NFC Award",
        "description": "Verified fiscal data: National Finance Commission (NFC) formula weights, provincial divisible pool transfers, FBR tax revenue collection, public debt maturity, and education expenditure.",
        "canonical": "https://ppripakistan.github.io/data/public-finance/",
        "csv_download": "/data/downloads/province_baseline_2023.csv",
        "stats": [
            ("Rs 5,500B+", "Federal Divisible Pool", "7th NFC Award Pool Size", "Ministry of Finance"),
            ("82.0%", "NFC Population Weight", "Dominant formula distribution factor", "7th NFC Award Gazette"),
            ("Rs 83.28T", "Total Public Debt", "Domestic + External Liabilities", "State Bank Debt Bulletin"),
            ("3.86 Yrs", "Domestic Debt Maturity", "Average time to maturity", "PES Debt Chapter")
        ],
        "chart_title": "7th NFC Award Divisible Pool Formula Weights (%)",
        "chart_data": [
            {"label": "Population", "value": 82.0, "formattedValue": "82.0%", "color": "#073c3a"},
            {"label": "Poverty/Backwardness", "value": 10.3, "formattedValue": "10.3%", "color": "#0f766e"},
            {"label": "Revenue Collection", "value": 5.0, "formattedValue": "5.0%", "color": "#0284c7"},
            {"label": "Inverse Density", "value": 2.7, "formattedValue": "2.7%", "color": "#d97706"}
        ],
        "table_headers": ["Fiscal Parameter", "Formula Weight / Value", "Provincial / Sector Share", "Institutional Source"],
        "table_rows": [
            ["NFC Population Criterion Weight", "82.0%", "Favors populous units (Punjab 51.74%)", "7th NFC Award (2010)"],
            ["NFC Poverty & Backwardness Weight", "10.3%", "Multi-dimensional index (Balochistan/KP)", "7th NFC Award (2010)"],
            ["NFC Revenue Collection Weight", "5.0%", "Recognizes port/commercial revenues (Sindh)", "7th NFC Award (2010)"],
            ["NFC Inverse Density Weight", "2.7%", "Compensates vast land areas (Balochistan)", "7th NFC Award (2010)"],
            ["Simulated Punjab Divisible Pool Share", "51.74%", "~Rs 2,846 Billion (at Rs 5.5T pool)", "PPRI NFC Simulator"],
            ["Simulated Sindh Divisible Pool Share", "24.55%", "~Rs 1,350 Billion (at Rs 5.5T pool)", "PPRI NFC Simulator"],
            ["Simulated KP Divisible Pool Share", "14.62%", "~Rs 804 Billion (at Rs 5.5T pool)", "PPRI NFC Simulator"],
            ["Simulated Balochistan Divisible Pool Share", "9.09%", "~Rs 500 Billion (at Rs 5.5T pool)", "PPRI NFC Simulator"],
            ["Total Public Debt (Domestic + External)", "PKR 83,285 Billion", "Total federal sovereign liabilities", "State Bank Debt Monitor"],
            ["Domestic Public Debt", "PKR 57,566 Billion", "T-Bills, PIBs, and Sukuk", "State Bank Debt Monitor"],
            ["External Public Debt", "PKR 25,720 Billion", "Multilateral, bilateral & eurobonds", "State Bank Debt Monitor"],
            ["Domestic Debt Time to Maturity", "3.86 Years", "Refinancing risk benchmark", "PES 2025–26 Debt Report"],
            ["Federal & Provincial Education Expenditure", "PKR 962 Billion", "Combined national budgetary outlay", "PES Education Chapter"],
            ["Annual Interest Expense Shift", "-23.0%", "YoY change due to monetary easing", "PES Public Debt Analysis"]
        ],
        "citation": "Ministry of Finance & National Finance Commission. (2025). Federal Budget 2025–26 & SBP Debt Bulletins. Government of Pakistan, Islamabad.",
        "related_research": [
            {
                "type": "Report",
                "title": "Does Money Work Better When Spent Closer to the People? Fiscal Decentralization",
                "url": "/research/reports/does-money-work-better-spent-closer-to-people.html",
                "read_time": "16 min read",
                "summary": "Demonstrating that shifting funds from provincial secretariats to elected district governments dramatically accelerates local school completion and drinking water maintenance."
            },
            {
                "type": "Article",
                "title": "The 18th Amendment: Did Devolution Stop at the Provincial Capital?",
                "url": "/articles/18th-amendment-did-devolution-stop-at-provincial-capital.html",
                "read_time": "10 min read",
                "summary": "Exploring the constitutional paradox: federal power devolved to provinces in 2010, but provincial governments retained monopoly control without sub-devolving to local councils."
            },
            {
                "type": "Article",
                "title": "One Province, Many Needs: When Regions Compete for the Same Budget",
                "url": "/articles/one-province-many-needs-development-budget-priority.html",
                "read_time": "8 min read",
                "summary": "How mega-provinces create bitter regional rivalries over annual development plans (ADPs) between industrial centers and neglected agrarian peripheries."
            },
            {
                "type": "Article",
                "title": "Where Did Development Money Go When Pakistan Tried District Government?",
                "url": "/articles/where-did-development-money-go-district-government.html",
                "read_time": "9 min read",
                "summary": "Historical fiscal analysis of the 2001–2008 Local Government Ordinance era, examining how local budget discretion affected service outcomes."
            }
        ]
    },
    "education": {
        "slug": "education",
        "title": "Pakistan Education, Literacy & Human Capital Data",
        "h1": "Education, Literacy &amp; Human Capital",
        "description": "PBS HIES 2024–25 education indicators: literacy by age, sex and province, plus out-of-school rates for children aged 5–16, with definitions and downloadable data.",
        "canonical": "https://ppripakistan.github.io/data/education/",
        "csv_download": "/data/downloads/pakistan-education-literacy-hies-2024-25.csv",
        "stats": [
            ("63%", "National Literacy Rate", "Population aged 10+; HIES 2024–25", "Pakistan Bureau of Statistics"),
            ("73% / 54%", "Male vs Female Literacy", "19 percentage-point gap; age 10+", "PBS HIES 2024–25 Social Report"),
            ("28%", "Out-of-School Rate", "Children aged 5–16; boys 25%, girls 31%", "PBS HIES 2024–25 Social Report"),
            ("77%", "Youth Literacy Rate", "Population aged 15–24", "PBS HIES 2024–25 Social Report")
        ],
        "chart_title": "Provincial Literacy Rates (Age 10+, HIES 2024–25)",
        "chart_data": [
            {"label": "Punjab", "value": 68, "formattedValue": "68%", "color": "#073c3a"},
            {"label": "Sindh", "value": 58, "formattedValue": "58%", "color": "#0f766e"},
            {"label": "Khyber Pakhtunkhwa", "value": 58, "formattedValue": "58%", "color": "#0284c7"},
            {"label": "Balochistan", "value": 49, "formattedValue": "49%", "color": "#d97706"},
            {"label": "National Total", "value": 63, "formattedValue": "63%", "color": "#16a34a"}
        ],
        "table_headers": ["Indicator / Population", "National / Province", "Male / Boys / Urban", "Female / Girls / Rural", "Official Source / Notes"],
        "table_rows": [
            ["Literacy rate (age 10+)", "63%", "Male: 73%; urban: 74%", "Female: 54%; rural: 55%", "PBS HIES 2024–25 Social Report"],
            ["Provincial literacy rate (age 10+)", "Punjab: 68%", "Sindh: 58%", "KP: 58%", "Balochistan: 49%; PBS HIES 2024–25"],
            ["Adult literacy rate (age 15+)", "60%", "Male: 71%; urban: 73%", "Female: 50%; rural: 51%", "PBS HIES 2024–25; different age threshold"],
            ["Youth literacy rate (age 15–24)", "77%", "Male: 82%; urban: 85%", "Female: 71%; rural: 71%", "PBS HIES 2024–25 Social Report"],
            ["Out-of-school rate (age 5–16)", "28%", "Boys: 25%", "Girls: 31%", "PBS HIES 2024–25 Social Report"],
            ["Provincial out-of-school rate (age 5–16)", "Punjab: 21%", "Sindh: 39%", "KP: 28%", "Balochistan: 45%; PBS HIES 2024–25"]
        ],
        "citation": "Pakistan Bureau of Statistics. (2025). Household Integrated Economic Survey (HIES) 2024–25: Social Report. Government of Pakistan.",
        "related_research": [
            {
                "type": "Report",
                "title": "Same Country, Different Life: The 26 Million Out-of-School Children Crisis",
                "url": "/research/reports/same-country-different-life-district-access.html",
                "read_time": "15 min read",
                "summary": "Disaggregating education outcomes down to district level, showing female rural literacy below 15% in parts of Balochistan and southern KP."
            },
            {
                "type": "Report",
                "title": "Does Money Work Better When Spent Closer to the People? Local Education Budgets",
                "url": "/research/reports/does-money-work-better-spent-closer-to-people.html",
                "read_time": "16 min read",
                "summary": "Why centralized provincial education departments struggle with teacher absenteeism, school boundary walls, and primary school dropout rates."
            },
            {
                "type": "Policy Brief",
                "title": "Administrative Scale and Public Service Delivery in Pakistan's Mega-Provinces",
                "url": "/research/briefs/administrative-scale.html",
                "read_time": "7 min read",
                "summary": "Analyzing span-of-control bottlenecks when a single Provincial Secretary of Education attempts to administer 60,000+ public schools."
            }
        ]
    },
    "health": {
        "slug": "health",
        "title": "Pakistan Public Health & Demographic Health Indicators Data",
        "h1": "Public Health &amp; Demographics",
        "description": "Verified health indicators: child immunization coverage (73%), total fertility rate (3.6 births/woman), prenatal healthcare consultations, and maternal health access.",
        "canonical": "https://ppripakistan.github.io/data/health/",
        "csv_download": "/data/downloads/pakistan-economic-benchmarks-2026.csv",
        "stats": [
            ("73.0%", "Child Immunization Rate", "Children 12–23 months fully vaccinated", "PDHS / PBS Survey"),
            ("3.60", "Total Fertility Rate", "Births per woman nationally", "PBS Demographic Survey"),
            ("88.0%", "Prenatal Consultation", "Skilled health provider visits", "PBS Health Indicators"),
            ("38.0%", "Contraceptive Prevalence", "Family planning prevalence rate", "PBS / PDHS Benchmark")
        ],
        "chart_title": "Core Public Health Coverage Benchmarks (%)",
        "chart_data": [
            {"label": "Prenatal Consultation", "value": 88.0, "formattedValue": "88.0%", "color": "#073c3a"},
            {"label": "Child Immunization", "value": 73.0, "formattedValue": "73.0%", "color": "#0f766e"},
            {"label": "Female Health Autonomy", "value": 56.0, "formattedValue": "56.0%", "color": "#0284c7"},
            {"label": "Contraceptive Prevalence", "value": 38.0, "formattedValue": "38.0%", "color": "#d97706"}
        ],
        "table_headers": ["Health Indicator", "National Benchmark", "Urban Status", "Rural Status", "Survey Source"],
        "table_rows": [
            ["Fully Immunized Children (12–23 Months)", "73.0%", "81.0%", "68.0%", "PDHS / PBS Health Survey"],
            ["Total Fertility Rate (Births per Woman)", "3.60", "3.00", "4.00", "PBS Demographic Survey"],
            ["Prenatal Care Skilled Consultation Rate", "88.0%", "94.0%", "83.0%", "PBS PSLM / Health Bulletin"],
            ["Contraceptive Prevalence Rate (CPR)", "38.0%", "45.0%", "33.0%", "PDHS Official Benchmark"],
            ["Female Reproductive Healthcare Autonomy", "56.0%", "64.0%", "51.0%", "PBS Gender Health Tables"],
            ["Safe Water Access in Health Facilities", "86.0%", "92.0%", "81.0%", "PBS Infrastructure Survey"],
            ["Clean fuels/technology for cooking, lighting and heating", "38%", "74%", "13%", "PBS HIES 2024–25 Social Report; composite indicator"],
            ["Handwashing facility with both soap and water", "64%", "—", "—", "PBS HIES 2024–25 Social Report; urban/rural split not included without a verified table"]
        ],
        "citation": "National Institute of Population Studies & Pakistan Bureau of Statistics. (2025). Pakistan Demographic and Health Survey & PSLM Health Indicators. Ministry of National Health Services.",
        "related_research": [
            {
                "type": "Report",
                "title": "Same Country, Different Life: Public Health Gaps Across Pakistan's Districts",
                "url": "/research/reports/same-country-different-life-district-access.html",
                "read_time": "15 min read",
                "summary": "Investigating how travel times exceeding 6 hours to tertiary hospitals contribute to elevated maternal and infant mortality in peripheral divisions."
            },
            {
                "type": "Article",
                "title": "How Far Is Government? The Hidden Cost of Administrative Distance for Healthcare",
                "url": "/articles/how-far-is-government-administrative-distance.html",
                "read_time": "8 min read",
                "summary": "Mapping spatial isolation from Gwadar, Chitral, and Tharparkar to provincial teaching hospitals and medical specialist clusters."
            },
            {
                "type": "Working Paper",
                "title": "Provinces & Local Government: Primary Health Care Service Delivery",
                "url": "/research/working-papers/provinces-local-government.html",
                "read_time": "11 min read",
                "summary": "Comparing outcomes of devolved Basic Health Units (BHUs) and Rural Health Centres (RHCs) under local governance vs provincial control."
            }
        ]
    },
    "digital-access": {
        "slug": "digital-access",
        "title": "Pakistan Digital Access, Mobile & Telecom Infrastructure Data",
        "h1": "Digital Access, Mobile &amp; Technology",
        "description": "Verified digital infrastructure data: 95% household mobile access, individual mobile ownership gender gap, household broadband access, internet penetration, and $3.39B IT exports.",
        "canonical": "https://ppripakistan.github.io/data/digital-access/",
        "csv_download": "/data/downloads/pakistan-digital-access-hies-2024-25.csv",
        "stats": [
            ("95.0%", "Household Mobile Access", "Households with at least 1 phone", "PBS HIES Survey"),
            ("69% / 39%", "Individual Mobile by Sex", "30% male-female ownership gap", "PBS Individual Access"),
            ("34.0%", "Household Broadband", "70% Urban vs 24% Rural access", "PBS Digital Tables"),
            ("$3.39B", "IT & Telecom Exports", "Annual software export earnings", "State Bank of Pakistan")
        ],
        "chart_title": "Household vs Individual Mobile & Internet Access (%)",
        "chart_data": [
            {"label": "Household Mobile", "value": 95.0, "formattedValue": "95.0%", "color": "#073c3a"},
            {"label": "Internet Users (Pop)", "value": 57.0, "formattedValue": "57.0%", "color": "#0f766e"},
            {"label": "Male Mobile Owner", "value": 69.0, "formattedValue": "69.0%", "color": "#0284c7"},
            {"label": "Female Mobile Owner", "value": 39.0, "formattedValue": "39.0%", "color": "#d97706"},
            {"label": "Household Broadband", "value": 34.0, "formattedValue": "34.0%", "color": "#16a34a"},
            {"label": "Household PC/Laptop", "value": 14.0, "formattedValue": "14.0%", "color": "#64748b"}
        ],
        "table_headers": ["Digital & Telecom Indicator", "National Total", "Urban Status", "Rural Status", "Survey / Institutional Source"],
        "table_rows": [
            ["Household Mobile / Smartphone Access", "95.0%", "96.2%", "93.8%", "PBS HIES 2024–25"],
            ["Individual Mobile Phone Ownership (Overall)", "50.0%", "60.0%", "44.0%", "PBS Digital Access Tables"],
            ["Male Individual Mobile Ownership", "69.0%", "76.0%", "64.0%", "PBS Digital Access Tables"],
            ["Female Individual Mobile Ownership", "39.0%", "52.0%", "29.0%", "PBS Digital Access Tables"],
            ["Household Internet / Broadband Access", "34.0%", "70.0%", "24.0%", "PBS HIES 2024–25"],
            ["Population Using Internet", "57.0%", "72.0%", "46.0%", "PTA / PBS Official Figures"],
            ["Household Computer / Laptop Access", "14.0%", "27.0%", "6.0%", "PBS HIES 2024–25"],
            ["IT & Telecommunication Software Exports", "USD 3,388 Million", "Major Hub: Karachi/Lahore", "Islamabad Software Cluster", "State Bank of Pakistan"],
            ["Adults with Bank or Mobile Money Account", "28.0%", "39.0%", "21.0%", "SBP Financial Inclusion"]
        ],
        "citation": "Pakistan Telecommunication Authority & Pakistan Bureau of Statistics. (2025). Telecom Indicators & HIES Digital Access Module 2024–25. Ministry of Information Technology and Telecommunication.",
        "related_research": [
            {
                "type": "Report",
                "title": "The Price of a Simple Task: Bureaucratic Friction & Digital Governance",
                "url": "/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html",
                "read_time": "12 min read",
                "summary": "Assessing how paper-based procedures cost businesses and citizens billions annually, and how mobile e-governance can bridge the citizen-state divide."
            },
            {
                "type": "Article",
                "title": "Can Pakistan Grow Beyond Its Provincial Capitals? Tech Infrastructure & Secondary Cities",
                "url": "/articles/can-pakistan-grow-beyond-provincial-capitals-secondary-cities.html",
                "read_time": "8 min read",
                "summary": "Why high-speed fiber broadband and software technology parks are essential for unlocking IT export growth in secondary cities like Multan, Gujranwala, and Sukkur."
            },
            {
                "type": "Article",
                "title": "Karachi and Urban Sindh: Representation, Revenue and Digital Infrastructure",
                "url": "/articles/karachi-urban-sindh-representation-revenue-administration.html",
                "read_time": "10 min read",
                "summary": "Analyzing the tech and commercial ecosystem of Pakistan's financial capital and the institutional friction holding back municipal digitisation."
            }
        ]
    }
}

def generate_hub_html(key, hub):
    stat_cards_html = []
    for val, label, subtext, source in hub["stats"]:
        stat_cards_html.append(f"""            <div class="obs-stat-card">
              <span class="obs-stat-label">{label}</span>
              <div class="obs-stat-val">{val}</div>
              <div class="obs-stat-unit">{subtext}</div>
              <div class="obs-stat-footer" style="display:flex;justify-content:space-between;align-items:center;">
                <span>{source}</span>
                <span class="obs-badge obs-badge-official">&check; Verified</span>
              </div>
            </div>""")

    chart_json = json.dumps(hub["chart_data"])
    chart_id = f"chart_{hub['slug'].replace('-', '_')}"
    table_id = f"table_{hub['slug'].replace('-', '_')}"

    header_cols = "".join([f'<th class="sortable">{h} <span class="sort-arrow">&udhar;</span></th>' for h in hub["table_headers"]])
    rows_html = []
    num_markers = ('%', 'PKR', 'Rs', '$', '499', '688', '696', '856', '894', '363')
    for r in hub["table_rows"]:
        cells = []
        for cell in r:
            is_num = any(m in cell for m in num_markers)
            cls_attr = ' class="num"' if is_num else ''
            cells.append(f"<td{cls_attr}>{cell}</td>")
        rows_html.append(f"<tr>{''.join(cells)}</tr>")

    citation_escaped = hub['citation'].replace("'", "\\'")

    html = f"""<!doctype html>
<html lang="en">
  <head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-9C2NZV6BYF"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());

      gtag('config', 'G-9C2NZV6BYF');
    </script>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>{hub['title']} | PPRI Data Observatory</title>
    <meta name="description" content="{hub['description']}" />
    <link rel="canonical" href="{hub['canonical']}" />
    <meta property="og:site_name" content="Pakistan Provincial Reform Institute (PPRI)" />
    <meta property="og:locale" content="en_PK" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="{hub['title']} | PPRI Data Observatory" />
    <meta property="og:description" content="{hub['description']}" />
    <meta property="og:url" content="{hub['canonical']}" />
    <meta property="og:image" content="https://ppripakistan.github.io/assets/images/previews/index.jpg" />
    <meta property="og:image:secure_url" content="https://ppripakistan.github.io/assets/images/previews/index.jpg" />
    <meta property="og:image:type" content="image/jpeg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:image:alt" content="{hub['title']} | PPRI Data Observatory" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:site" content="@PPRI_Pakistan" />
    <meta name="twitter:creator" content="@PPRI_Pakistan" />
    <meta name="twitter:title" content="{hub['title']} | PPRI Data Observatory" />
    <meta name="twitter:description" content="{hub['description']}" />
    <meta name="twitter:image" content="https://ppripakistan.github.io/assets/images/previews/index.jpg" />
    <meta name="twitter:image:alt" content="{hub['title']} | PPRI Data Observatory" />
    <link rel="icon" href="/favicon.ico" sizes="48x48" />
    <link rel="icon" href="/assets/images/brand/favicon.svg" type="image/svg+xml" />
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/images/brand/favicon-32x32.png" />
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/images/brand/favicon-16x16.png" />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
    <link rel="manifest" href="/site.webmanifest" />
    <meta name="theme-color" content="#073c3a" />
    <link rel="stylesheet" href="/assets/css/style.css" />
    <link rel="stylesheet" href="/assets/css/responsive.css" />
    <link rel="stylesheet" href="/assets/css/observatory.css" />
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Dataset",
      "name": "{hub['h1']}",
      "description": "{hub['description']}",
      "url": "{hub['canonical']}",
      "license": "https://creativecommons.org/licenses/by/4.0/",
      "spatialCoverage": {{
        "@type": "Place",
        "name": "Pakistan"
      }},
      "creator": {{
        "@type": "Organization",
        "name": "Pakistan Provincial Reform Institute",
        "url": "https://ppripakistan.github.io/"
      }},
      "distribution": [
        {{
          "@type": "DataDownload",
          "encodingFormat": "text/csv",
          "contentUrl": "https://ppripakistan.github.io{hub['csv_download']}"
        }}
      ]
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://ppripakistan.github.io/"
        }},
        {{
          "@type": "ListItem",
          "position": 2,
          "name": "Data Observatory",
          "item": "https://ppripakistan.github.io/data/centre.html"
        }},
        {{
          "@type": "ListItem",
          "position": 3,
          "name": "{hub['h1']}",
          "item": "{hub['canonical']}"
        }}
      ]
    }}
    </script>
  </head>
  <body>
{get_common_header()}

    <main id="main-content">
      <div class="obs-header">
        <div class="container">
          <ul class="obs-breadcrumbs">
            <li><a href="/index.html">Home</a></li>
            <li class="separator">/</li>
            <li><a href="/data/centre.html">Data Observatory</a></li>
            <li class="separator">/</li>
            <li aria-current="page">{hub['h1']}</li>
          </ul>
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
            <span class="obs-badge obs-badge-official">&check; Verified Public Data</span>
            <span class="obs-badge obs-badge-period">Updated 2025–26</span>
          </div>
          <h1 class="obs-title">{hub['h1']}</h1>
          <p class="obs-subtitle">{hub['description']}</p>
        </div>
      </div>

      <div class="container">
{get_observatory_nav_rail(hub['slug'])}

        <!-- Executive Stat Cards -->
        <div class="obs-stat-grid">
{''.join(stat_cards_html)}
        </div>

        <!-- Interactive SVG Chart Section -->
        <section class="obs-section">
          <div class="obs-section-header">
            <div>
              <span class="obs-badge obs-badge-census">&bull; Interactive Graphic</span>
              <h2 class="obs-section-title" style="margin-top:6px;">{hub['chart_title']}</h2>
            </div>
            <a href="{hub['csv_download']}" class="obs-btn obs-btn-outline" download>&darr; Download CSV</a>
          </div>
          <div class="obs-chart-wrapper" id="{chart_id}"></div>
        </section>

        <!-- Searchable & Sortable Comprehensive Data Table -->
        <section class="obs-section">
          <div class="obs-section-header">
            <div>
              <span class="obs-badge obs-badge-official">&check; Authoritative Records</span>
              <h2 class="obs-section-title" style="margin-top:6px;">Comprehensive Indicator Catalog &amp; Provincial Breakdowns</h2>
            </div>
            <div style="display:flex;gap:10px;align-items:center;">
              <input type="text" id="filterInput" placeholder="Filter indicators..." style="padding:7px 12px;border:1px solid var(--obs-border);border-radius:var(--obs-radius-sm);font-size:0.88rem;width:200px;" />
              <button class="obs-btn obs-btn-primary" onclick="PPRIObservatory.exportTableToCSV('{table_id}', '{hub['slug']}_indicators.csv')">&darr; Export CSV</button>
            </div>
          </div>
          <div class="obs-table-container">
            <table class="obs-table" id="{table_id}">
              <thead>
                <tr>
                  {header_cols}
                </tr>
              </thead>
              <tbody>
                {''.join(rows_html)}
              </tbody>
            </table>
          </div>
        </section>

        <!-- Action Bar: Citation & Downloads -->
        <div class="obs-actions-bar">
          <div class="obs-actions-text">
            <strong>Need to cite this data in academic research, policy papers, or CSS essays?</strong>
          </div>
          <div class="obs-actions-btns">
            <button class="obs-btn obs-btn-outline" onclick="PPRIObservatory.copyCitation('{citation_escaped}')">
              &boxbox; Copy Citation (APA)
            </button>
            <a href="{hub['csv_download']}" class="obs-btn obs-btn-primary" download>
              &darr; Download Official CSV
            </a>
          </div>
        </div>

        <!-- Official Sources Citation Box -->
        <div class="obs-source-card">
          <h3 class="obs-source-title">Official Sources &amp; Verification Methodology</h3>
          <p class="obs-source-text">
            All statistics on this page are compiled directly from public official releases including the Pakistan Bureau of Statistics (PBS), Ministry of Finance, and the State Bank of Pakistan. Data points undergo rigorous verification and cross-validation against official gazettes and published survey workbooks.
          </p>
          <div style="display:flex;gap:12px;flex-wrap:wrap;align-items:center;">
            <a href="/data/methodology/" class="obs-source-link">&rarr; View Data Verification Standards</a>
            <span style="color:var(--obs-text-muted);">&middot;</span>
            <a href="/data/downloads/" class="obs-source-link">&rarr; Browse All Public Datasets</a>
          </div>
        </div>

{get_related_research_section(hub['related_research'])}

      </div>
    </main>

{get_common_footer()}

    <script src="/assets/js/main.js" defer></script>
    <script src="/assets/js/observatory-engine.js" defer></script>
    <script>
      document.addEventListener('DOMContentLoaded', function() {{
        // Render Interactive SVG Bar Chart
        if (typeof PPRIObservatory !== 'undefined') {{
          PPRIObservatory.renderBarChart('#{chart_id}', {chart_json}, {{
            title: '{hub['chart_title']}'
          }});
          PPRIObservatory.setupTableSort('{table_id}');
          PPRIObservatory.initSearchFilter('#filterInput', '#{table_id}');
        }}
      }});
    </script>
  </body>
</html>
"""
    return html

def build_all_hubs():
    print("Building 7 Thematic Hubs...")
    for key, hub in HUBS_CONFIG.items():
        hub_dir = os.path.join(DATA_DIR, hub["slug"])
        os.makedirs(hub_dir, exist_ok=True)
        hub_file = os.path.join(hub_dir, "index.html")
        content = generate_hub_html(key, hub)
        with open(hub_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated hub: {hub_file} ({len(content)} bytes)")

if __name__ == "__main__":
    build_all_hubs()
