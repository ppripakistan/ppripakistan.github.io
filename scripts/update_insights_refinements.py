import re

with open('insights/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Top Badge
badge_pattern = r'<div class="vi-badge-top">.*?</div>\s*'
html = re.sub(badge_pattern, '', html)

# 2. Replace vi-seo-highlights and vi-seo-footer-note with 4 Collapsible Accordion Cards
old_narrative_block = r'<ul class="vi-seo-highlights">.*?<p class="vi-seo-footer-note">.*?</p>'

new_accordion_grid = """<div class="vi-seo-accordion-grid">
              <!-- Domain 1: Public Finance -->
              <details class="vi-seo-accordion">
                <summary class="vi-seo-summary">
                  <span class="vi-seo-summary-left">
                    <span class="vi-seo-icon" style="color:#0f766e;">🏛️</span>
                    <span class="vi-seo-title">Public Finance &amp; Sovereign Debt</span>
                  </span>
                  <span class="vi-seo-summary-right">
                    <span class="vi-seo-badge">4 Infographics</span>
                    <span class="vi-seo-chevron" aria-hidden="true">▾</span>
                  </span>
                </summary>
                <div class="vi-seo-body">
                  <p>Visualizing how sovereign debt interest servicing (PKR 9,775B) absorbs over 51% of total federal budget outlays and 76% of net FBR tax collection, the 8-year trajectory of public debt stock escalation (FY18–FY26), the distribution of PKR 3.98T in federal tax concessions and exemptions, and a 4-province comparative matrix examining provincial budgetary outlays, Annual Development Programmes (ADP), outstanding sub-national debt, per capita allocations, and regional conflict exposure.</p>
                </div>
              </details>

              <!-- Domain 2: Economic Transitions -->
              <details class="vi-seo-accordion">
                <summary class="vi-seo-summary">
                  <span class="vi-seo-summary-left">
                    <span class="vi-seo-icon" style="color:#2563eb;">📈</span>
                    <span class="vi-seo-title">Economic Transitions &amp; Purchasing Power</span>
                  </span>
                  <span class="vi-seo-summary-right">
                    <span class="vi-seo-badge">4 Infographics</span>
                    <span class="vi-seo-chevron" aria-hidden="true">▾</span>
                  </span>
                </summary>
                <div class="vi-seo-body">
                  <p>Tracking real wage erosion where cumulative inflation of +205% since FY10 dramatically outpaced statutory minimum wage adjustments (-42% real purchasing power loss), sectoral labour force absorption dynamics, smallholder agricultural land fragmentation (<5 acres to >50 acres), and 35 years of macroeconomic trajectory across four distinct political and reform regimes (FY90–FY24).</p>
                </div>
              </details>

              <!-- Domain 3: Demographics & Spatial Governance -->
              <details class="vi-seo-accordion">
                <summary class="vi-seo-summary">
                  <span class="vi-seo-summary-left">
                    <span class="vi-seo-icon" style="color:#7c3aed;">👥</span>
                    <span class="vi-seo-title">Demographics &amp; Spatial Governance</span>
                  </span>
                  <span class="vi-seo-summary-right">
                    <span class="vi-seo-badge">4 Infographics</span>
                    <span class="vi-seo-chevron" aria-hidden="true">▾</span>
                  </span>
                </summary>
                <div class="vi-seo-body">
                  <p>Charting female sex ratios versus agrarian landownership disparities, 4-decade provincial demographic growth trajectories across the 1981, 1998, 2017, and 2023 censuses, a 135-district urbanization versus population density quadrant scale, and national demographic acceleration milestones across 70 years of census history.</p>
                </div>
              </details>

              <!-- Domain 4: Living Standards & Household Budgets -->
              <details class="vi-seo-accordion">
                <summary class="vi-seo-summary">
                  <span class="vi-seo-summary-left">
                    <span class="vi-seo-icon" style="color:#d97706;">🏠</span>
                    <span class="vi-seo-title">Living Standards &amp; Household Budgets</span>
                  </span>
                  <span class="vi-seo-summary-right">
                    <span class="vi-seo-badge">4 Infographics</span>
                    <span class="vi-seo-chevron" aria-hidden="true">▾</span>
                  </span>
                </summary>
                <div class="vi-seo-body">
                  <p>Analyzing regressive food Engel ratios where lowest-quintile households dedicate 52.4% of total consumption to food (HIES 2024–25), provincial food versus non-food consumption basket variations, basic housing characteristics and clean water access deficits, and Labour Force Survey (LFS) gender employment and rural-urban wage disparities.</p>
                </div>
              </details>
            </div>"""

html = re.sub(old_narrative_block, new_accordion_grid, html, flags=re.DOTALL)

# 3. Replace Quick-Jump with 4 Clearly Separated Thematic Cards
old_quick_nav = r'<!-- Grouped Thematic Quick-Jump Toolbar -->\s*<div class="vi-quick-nav".*?</div>\s*</div>\s*</div>'

new_quick_nav = """<!-- Grouped Thematic Quick-Jump Toolbar -->
          <div class="vi-quick-nav" aria-label="Quick Jump to Policy Infographics">
            <div class="vi-quick-nav-header">
              <span class="vi-quick-nav-title">Quick-Jump to Infographic:</span>
              <span class="vi-quick-nav-hint">Click any sub-category chip to smoothly glide directly to its interactive visual</span>
            </div>
            <div class="vi-quick-clusters-grid">
              <!-- Domain 1 Card: Public Finance -->
              <div class="vi-jump-domain-card vi-jump-card-fiscal">
                <div class="vi-jump-domain-header">
                  <span class="vi-domain-tag">
                    <span style="font-size:1rem;">🏛️</span> Public Finance &amp; Debt
                  </span>
                </div>
                <div class="vi-group-chips">
                  <button type="button" class="vi-chip-btn" data-target="card-fiscal">Federal Outlays</button>
                  <button type="button" class="vi-chip-btn" data-target="card-debt">Public Debt Surge</button>
                  <button type="button" class="vi-chip-btn" data-target="card-tax-exp">Tax Concessions</button>
                  <button type="button" class="vi-chip-btn vi-chip-highlight" data-target="card-prov-matrix">Provincial Matrix</button>
                </div>
              </div>

              <!-- Domain 2 Card: Economy & Jobs -->
              <div class="vi-jump-domain-card vi-jump-card-economy">
                <div class="vi-jump-domain-header">
                  <span class="vi-domain-tag">
                    <span style="font-size:1rem;">📈</span> Economy &amp; Jobs
                  </span>
                </div>
                <div class="vi-group-chips">
                  <button type="button" class="vi-chip-btn" data-target="card-wage-infl">Real Wage Squeeze</button>
                  <button type="button" class="vi-chip-btn" data-target="card-sector-employment">Sectoral Jobs</button>
                  <button type="button" class="vi-chip-btn" data-target="card-agri-shifts">Farm Landholding</button>
                  <button type="button" class="vi-chip-btn" data-target="card-macro">35-Yr Macro History</button>
                </div>
              </div>

              <!-- Domain 3 Card: Demographics & Districts -->
              <div class="vi-jump-domain-card vi-jump-card-demographics">
                <div class="vi-jump-domain-header">
                  <span class="vi-domain-tag">
                    <span style="font-size:1rem;">👥</span> Demographics &amp; Districts
                  </span>
                </div>
                <div class="vi-group-chips">
                  <button type="button" class="vi-chip-btn" data-target="card-gender-land">Gender &amp; Land</button>
                  <button type="button" class="vi-chip-btn" data-target="card-census-shifts">Census Shifts</button>
                  <button type="button" class="vi-chip-btn" data-target="card-districts-scatter">135 Districts Map</button>
                  <button type="button" class="vi-chip-btn" data-target="card-census-hist">70-Yr Population</button>
                </div>
              </div>

              <!-- Domain 4 Card: Living Standards & Baskets -->
              <div class="vi-jump-domain-card vi-jump-card-living">
                <div class="vi-jump-domain-header">
                  <span class="vi-domain-tag">
                    <span style="font-size:1rem;">🏠</span> Living Standards &amp; Baskets
                  </span>
                </div>
                <div class="vi-group-chips">
                  <button type="button" class="vi-chip-btn" data-target="card-hies">Food Engel Burden</button>
                  <button type="button" class="vi-chip-btn" data-target="card-consumption-pie">Consumption Baskets</button>
                  <button type="button" class="vi-chip-btn" data-target="card-services">Basic Utilities</button>
                  <button type="button" class="vi-chip-btn" data-target="card-lfs">Wage Disparity</button>
                </div>
              </div>
            </div>
          </div>"""

html = re.sub(old_quick_nav, new_quick_nav, html, flags=re.DOTALL)

# 4. Remove Filter Theme Pills completely
filter_pattern = r'<!-- Theme Filter Pills -->\s*<div class="vi-filter-pills".*?</div>\s*</div>\s*</header>'
replace_header_end = '</div>\n      </header>'
html = re.sub(filter_pattern, replace_header_end, html, flags=re.DOTALL)

with open('insights/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Updated insights/index.html with accordions, separated jump cards, removed top badge and filter pills!")
