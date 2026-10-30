import re

with open('insights/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Footer Logo
html = html.replace('/assets/images/brand/ppri-logo-footer.jpg', '/assets/images/brand/ppri-logo-header.jpg')

# 2. De-number Title & Meta
html = re.sub(
    r'<title>Visual Policy Analytics &amp; Infographics Lab \(01[–-]16\) \| PPRI Pakistan</title>',
    r'<title>Visual Policy Analytics &amp; Infographics Lab | PPRI Pakistan</title>',
    html
)
html = re.sub(
    r'<meta property="og:title" content="Visual Policy Analytics &amp; Infographics Lab \(01[–-]16\) \| PPRI" />',
    r'<meta property="og:title" content="Visual Policy Analytics &amp; Infographics Lab | PPRI" />',
    html
)

# 3. Breadcrumb
html = re.sub(
    r'<span aria-current="page">Visual Policy Analytics \(01[–-]16\)</span>',
    r'<span aria-current="page">Visual Policy Analytics &amp; Infographics</span>',
    html
)

# 4. Top Badge
html = re.sub(
    r'<div class="vi-badge-top">.*?16 Numbered Visualizations.*?</div>',
    r'<div class="vi-badge-top">&#x2714;&#xFE0F; Empirical Policy Visualizations &bull; 100% Vector Canvas Rasterizer</div>',
    html
)

# 5. Hero Description -> Comprehensive SEO Executive Narrative
old_hero_desc_pattern = r'<p class="vi-hero-desc">.*?</p>'
new_hero_narrative = """<div class="vi-hero-desc-narrative">
            <p>
              The <strong>PPRI Visual Policy Analytics &amp; Infographics Lab</strong> translates complex macroeconomic indicators, intergovernmental fiscal transfers, provincial budget allocations, and national household microdata into interactive, publication-grade empirical visualizations. Designed for policymakers, researchers, constitutional scholars, and civil society, this repository presents verified evidence on Pakistan’s core structural dilemmas: sovereign debt servicing monopolies, corporate tax expenditure concessions, cross-provincial fiscal and security disparities across Punjab, Sindh, Khyber Pakhtunkhwa, and Balochistan, and the persistent erosion of real household purchasing power.
            </p>
            <p>
              Explore empirical visual evidence across four primary policy domains:
            </p>
            <ul class="vi-seo-highlights">
              <li>
                <strong>Public Finance &amp; Sovereign Debt:</strong> Visualizing how sovereign debt interest servicing (PKR 9,775B) absorbs over 51% of total federal budget outlays and 76% of net FBR tax collection, the 8-year trajectory of public debt stock escalation (FY18–FY26), the distribution of PKR 3.98T in federal tax concessions and exemptions, and a 4-province comparative matrix examining provincial budgetary outlays, Annual Development Programmes (ADP), outstanding sub-national debt, per capita allocations, and regional conflict exposure.
              </li>
              <li>
                <strong>Economic Transitions &amp; Purchasing Power:</strong> Tracking real wage erosion where cumulative inflation of +205% since FY10 dramatically outpaced statutory minimum wage adjustments (-42% real purchasing power loss), sectoral labour force absorption dynamics, smallholder agricultural land fragmentation (<5 acres to >50 acres), and 35 years of macroeconomic trajectory across four distinct political and reform regimes (FY90–FY24).
              </li>
              <li>
                <strong>Demographics &amp; Spatial Governance:</strong> Charting female sex ratios versus agrarian landownership disparities, 4-decade provincial demographic growth trajectories across the 1981, 1998, 2017, and 2023 censuses, a 135-district urbanization versus population density quadrant scale, and national demographic acceleration milestones across 70 years of census history.
              </li>
              <li>
                <strong>Living Standards &amp; Household Budgets:</strong> Analyzing regressive food Engel ratios where lowest-quintile households dedicate 52.4% of total consumption to food (HIES 2024–25), provincial food versus non-food consumption basket variations, basic housing characteristics and clean water access deficits, and Labour Force Survey (LFS) gender employment and rural-urban wage disparities.
              </li>
            </ul>
            <p class="vi-seo-footer-note">
              Every infographic is rendered as clean scalable vector graphics (SVG) with instant <strong>2x Retina PNG download</strong>, <strong>direct SVG export</strong>, and <strong>Excel-ready UTF-8 BOM CSV</strong> data extraction.
            </p>
          </div>"""

html = re.sub(old_hero_desc_pattern, new_hero_narrative, html, flags=re.DOTALL)

# 6. Quick-Jump Toolbar (Replace vi-nav-pills)
old_jump_pattern = r'<!-- Jump Navigation Bar \(01 to 16\) -->\s*<div class="vi-nav-pills">.*?</div>'
new_jump_toolbar = """<!-- Grouped Thematic Quick-Jump Toolbar -->
          <div class="vi-quick-nav" aria-label="Quick Jump to Policy Infographics">
            <div class="vi-quick-nav-header">
              <span class="vi-quick-nav-title">Quick-Jump to Infographic:</span>
              <span class="vi-quick-nav-hint">Click any policy topic to smoothly scroll to its interactive visual</span>
            </div>
            <div class="vi-quick-clusters">
              <!-- Cluster 1: Fiscal & Debt Solvency -->
              <div class="vi-quick-group">
                <span class="vi-group-label">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="2"></rect><line x1="2" y1="10" x2="22" y2="10"></line></svg>
                  Fiscal &amp; Debt
                </span>
                <div class="vi-group-chips">
                  <button type="button" class="vi-chip-btn" data-target="card-fiscal">Federal Outlays</button>
                  <button type="button" class="vi-chip-btn" data-target="card-debt">Public Debt Surge</button>
                  <button type="button" class="vi-chip-btn" data-target="card-tax-exp">Tax Concessions</button>
                  <button type="button" class="vi-chip-btn vi-chip-highlight" data-target="card-prov-matrix">Provincial Matrix</button>
                </div>
              </div>

              <!-- Cluster 2: Economy & Structural Shifts -->
              <div class="vi-quick-group">
                <span class="vi-group-label">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline><polyline points="17 6 23 6 23 12"></polyline></svg>
                  Economy &amp; Jobs
                </span>
                <div class="vi-group-chips">
                  <button type="button" class="vi-chip-btn" data-target="card-wage-infl">Real Wage Squeeze</button>
                  <button type="button" class="vi-chip-btn" data-target="card-sector-employment">Sectoral Jobs</button>
                  <button type="button" class="vi-chip-btn" data-target="card-agri-shifts">Farm Landholding</button>
                  <button type="button" class="vi-chip-btn" data-target="card-macro">35-Yr Macro History</button>
                </div>
              </div>

              <!-- Cluster 3: Demographics & Spatial Atlas -->
              <div class="vi-quick-group">
                <span class="vi-group-label">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                  Demographics
                </span>
                <div class="vi-group-chips">
                  <button type="button" class="vi-chip-btn" data-target="card-gender-land">Gender &amp; Land</button>
                  <button type="button" class="vi-chip-btn" data-target="card-census-shifts">Census Shifts</button>
                  <button type="button" class="vi-chip-btn" data-target="card-districts-scatter">135 Districts Map</button>
                  <button type="button" class="vi-chip-btn" data-target="card-census-hist">70-Yr Population</button>
                </div>
              </div>

              <!-- Cluster 4: Living Standards & Labour -->
              <div class="vi-quick-group">
                <span class="vi-group-label">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                  Living Standards
                </span>
                <div class="vi-group-chips">
                  <button type="button" class="vi-chip-btn" data-target="card-hies">Food Engel Burden</button>
                  <button type="button" class="vi-chip-btn" data-target="card-consumption-pie">Consumption Baskets</button>
                  <button type="button" class="vi-chip-btn" data-target="card-services">Basic Utilities</button>
                  <button type="button" class="vi-chip-btn" data-target="card-lfs">Wage Disparity</button>
                </div>
              </div>
            </div>
          </div>"""

html = re.sub(old_jump_pattern, new_jump_toolbar, html, flags=re.DOTALL)

# 7. Strip #01:, #02:, etc. from all 16 Card Titles
title_replacements = [
    ('#01: Federal Budget Allocation &amp; Debt Servicing', 'Federal Budget Allocation &amp; Sovereign Debt Servicing'),
    ('#02: The 8-Year Public Debt Surge (FY18–FY26)', 'The 8-Year Sovereign Public Debt Trajectory (FY18–FY26)'),
    ('#02: The 8-Year Public Debt Surge (FY18FY26)', 'The 8-Year Sovereign Public Debt Trajectory (FY18–FY26)'),
    ('#03: Revenue Collection vs Tax Exemptions', 'Federal Tax Concessions &amp; Revenue Foregone'),
    ('#04: Gender Demographics &amp; Land Area Asymmetry', 'Female Gender Ratios &amp; Agrarian Landholding Asymmetry'),
    ('#05: Household Food Burden Divide (HIES 2024–25)', 'Household Food Engel Burden Divide (HIES 2024–25)'),
    ('#05: Household Food Burden Divide (HIES 202425)', 'Household Food Engel Burden Divide (HIES 2024–25)'),
    ('#06: Inter-Provincial Household Budget Allocation', 'Provincial Food vs Non-Food Household Consumption Baskets'),
    ('#07: Purchasing Power Erosion: Inflation vs Wages', 'Purchasing Power Erosion: Real Wages vs Inflation'),
    ('#08: Household Basic Services &amp; Utilities Access', 'Household Basic Housing Characteristics &amp; Utilities Deficit'),
    ('#09: Labour Force Disparities: Gender &amp; Youth', 'Labour Force Participation &amp; Gender/Rural Wage Disparities'),
    ('#10: Multi-Census Provincial Population Shares (1981–2023)', 'Multi-Census Provincial Demographic Shifts (1981–2023)'),
    ('#10: Multi-Census Provincial Population Shares (19812023)', 'Multi-Census Provincial Demographic Shifts (1981–2023)'),
    ('#11: 135-District Urbanization &amp; Density Quadrant Scatter Bubble Map', '135-District Urbanization &amp; Population Density Quadrant Matrix'),
    ('#12: Employment Distribution by Economic Sector', 'Sectoral Labour Force Absorption Dynamics'),
    ('#13: Agricultural Land &amp; Cultivated Acreage Shifts', 'Smallholder Landholding &amp; Cultivated Acreage Fragmentation'),
    ('#14: 70-Year Intercensal Demographic Growth (1951–2023)', '70-Year Intercensal Demographic Growth Trajectory (1951–2023)'),
    ('#14: 70-Year Intercensal Demographic Growth (19512023)', '70-Year Intercensal Demographic Growth Trajectory (1951–2023)'),
    ('#15: 35-Year Macroeconomic Trajectory (1990–2024: 4 Historical Tenures &amp; Crisis Shocks)', '35-Year Macroeconomic Trajectory (4 Regimes &amp; Crisis Shocks)'),
    ('#15: 35-Year Macroeconomic Trajectory (19902024: 4 Historical Tenures &amp; Crisis Shocks)', '35-Year Macroeconomic Trajectory (4 Regimes &amp; Crisis Shocks)'),
    ('#16: Provincial Resource Allocation, Debt Stock &amp; Conflict Exposure Matrix (FY25 &amp; 2023–2024)', 'Provincial Resource Allocation, Debt Stock &amp; Conflict Exposure Matrix'),
    ('#16: Provincial Resource Allocation, Debt Stock &amp; Conflict Exposure Matrix (FY25 &amp; 20232024)', 'Provincial Resource Allocation, Debt Stock &amp; Conflict Exposure Matrix')
]

for old_t, new_t in title_replacements:
    html = html.replace(f'<h3 class="vi-card-title">{old_t}</h3>', f'<h3 class="vi-card-title">{new_t}</h3>')

with open('insights/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Updated insights/index.html with all de-numbering, SEO narrative, quick-jump toolbar, and logo fix!")
