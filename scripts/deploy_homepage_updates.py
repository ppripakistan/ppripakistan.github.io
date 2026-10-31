# -*- coding: utf-8 -*-
import re

# ================= 1. UPDATE index.html =================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove #hudWrapper
hud_pattern = r'<!-- Research Desk HUD —.*?<!-- /#hudWrapper -->\s*'
html_new = re.sub(hud_pattern, '', html, flags=re.DOTALL)
if html_new != html:
    print("Successfully removed #hudWrapper")
    html = html_new
else:
    print("Warning: #hudWrapper pattern did not match directly, checking fallback...")
    # fallback line search
    start = html.find('<!-- Research Desk HUD')
    end = html.find('<!-- /#hudWrapper -->')
    if start != -1 and end != -1:
        end_idx = end + len('<!-- /#hudWrapper -->')
        html = html[:start] + html[end_idx:]
        print("Fallback removed #hudWrapper successfully")

# Remove post-mosaic CTA button:
# <div class="center" style="margin-top: 2.75rem; text-align: center;" data-reveal> ... Explore All 16 Interactive Policy Infographics in Insights Lab ... </div>
cta_pattern = r'<div class="center"[^>]*data-reveal>\s*<a href="/insights/" class="btn btn-primary"[^>]*>\s*<span>Explore All 16 Interactive Policy Infographics in Insights Lab</span>\s*<span aria-hidden="true">&rarr;</span>\s*</a>\s*</div>'
html_new = re.sub(cta_pattern, '', html)
if html_new != html:
    print("Successfully removed post-mosaic CTA button")
    html = html_new
else:
    print("Warning: post-mosaic CTA pattern did not match directly, attempting string replacement")
    start = html.find('Explore All 16 Interactive Policy Infographics in Insights Lab')
    if start != -1:
        div_start = html.rfind('<div class="center"', 0, start)
        div_end = html.find('</div>', start) + len('</div>')
        html = html[:div_start] + html[div_end:]
        print("Fallback removed post-mosaic CTA button successfully")

# Remove #section-platform
plat_start = html.find('id="section-platform"')
if plat_start != -1:
    sec_start = html.rfind('<section', 0, plat_start)
    sec_end = html.find('</section>', plat_start) + len('</section>')
    html = html[:sec_start] + html[sec_end:]
    print("Successfully removed #section-platform")

# Remove #section-evidence
evi_start = html.find('id="section-evidence"')
if evi_start != -1:
    sec_start = html.rfind('<section', 0, evi_start)
    sec_end = html.find('</section>', evi_start) + len('</section>')
    html = html[:sec_start] + html[sec_end:]
    print("Successfully removed #section-evidence")

# Remove .home-follow-section
fol_start = html.find('home-follow-section')
if fol_start != -1:
    sec_start = html.rfind('<section', 0, fol_start)
    sec_end = html.find('</section>', fol_start) + len('</section>')
    html = html[:sec_start] + html[sec_end:]
    print("Successfully removed home-follow-section")

# Replace .site-directory with .vi-treemap-section
treemap_html = '''
    <!-- ================= PPRI VISUAL SITE TREEMAP MATRIX ================= -->
    <section class="vi-treemap-section" id="section-site-treemap" aria-labelledby="treemap-section-title">
      <div class="container">
        <div class="vi-treemap-header-row">
          <div class="vi-treemap-title-group">
            <span class="home-section-label">Interactive Platform Atlas</span>
            <h2 id="treemap-section-title">Visual Site Architecture &amp; Knowledge Matrix</h2>
            <p class="vi-treemap-subtitle">
              Explore the entire Pakistan Provincial Reform Institute research ecosystem across 6 thematic pillars, 16 empirical infographics, and 70+ policy repositories.
            </p>
          </div>
          <div class="vi-treemap-controls">
            <span class="vi-treemap-stats-pill">6 Pillars • 70+ Verified Nodes</span>
            <button type="button" class="vi-treemap-toggle-btn" id="viTreemapToggleAll" aria-expanded="false">
              <span class="toggle-icon" aria-hidden="true">⊞</span>
              <span class="toggle-text">Expand All</span>
            </button>
          </div>
        </div>

        <div class="vi-treemap-grid">
          <!-- Pillar 1: Visual Policy Analytics & Infographics Lab (Teal Theme) -->
          <details class="vi-treemap-tile theme-teal" data-pillar="insights">
            <summary class="vi-treemap-summary">
              <div class="vi-treemap-sum-left">
                <span class="vi-treemap-icon" aria-hidden="true">📊</span>
                <div class="vi-treemap-sum-text">
                  <h3>Visual Policy Analytics &amp; Infographics Lab</h3>
                  <p>16 interactive empirical vector models &amp; econometric charts</p>
                </div>
              </div>
              <div class="vi-treemap-sum-right">
                <span class="vi-treemap-pill">16 Infographics</span>
                <svg class="vi-treemap-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
            </summary>
            <div class="vi-treemap-content">
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Fiscal &amp; Sovereign Debt</span>
                <div class="vi-treemap-chips">
                  <a href="/insights/#card-fiscal" class="vi-treemap-chip">
                    <span class="chip-metric">51.8%</span>
                    <span class="chip-title">Federal Budget &amp; Markup</span>
                  </a>
                  <a href="/insights/#card-debt" class="vi-treemap-chip">
                    <span class="chip-metric">PKR 86.4T</span>
                    <span class="chip-title">Public Debt Surge (FY18–26)</span>
                  </a>
                  <a href="/insights/#card-tax-exp" class="vi-treemap-chip">
                    <span class="chip-metric">PKR 3.88T</span>
                    <span class="chip-title">Federal Tax Concessions</span>
                  </a>
                  <a href="/insights/#card-prov-matrix" class="vi-treemap-chip">
                    <span class="chip-metric">4 Provinces</span>
                    <span class="chip-title">NFC, Debt &amp; Conflict Matrix</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Economy &amp; Sectoral Shifts</span>
                <div class="vi-treemap-chips">
                  <a href="/insights/#card-wage-infl" class="vi-treemap-chip">
                    <span class="chip-metric">-11.6%</span>
                    <span class="chip-title">Real Purchasing Power Squeeze</span>
                  </a>
                  <a href="/insights/#card-sector-employment" class="vi-treemap-chip">
                    <span class="chip-metric">40.7%</span>
                    <span class="chip-title">Agriculture to Services Shift</span>
                  </a>
                  <a href="/insights/#card-agri-shifts" class="vi-treemap-chip">
                    <span class="chip-metric">64.5% Small</span>
                    <span class="chip-title">Farmland Fragmentation (1960–2020)</span>
                  </a>
                  <a href="/insights/#card-macro" class="vi-treemap-chip">
                    <span class="chip-metric">35 Years</span>
                    <span class="chip-title">Macro Trajectory Overlay</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Demographics &amp; Spatial Governance</span>
                <div class="vi-treemap-chips">
                  <a href="/insights/#card-gender-land" class="vi-treemap-chip">
                    <span class="chip-metric">1.8% Female</span>
                    <span class="chip-title">Agricultural Land Ownership</span>
                  </a>
                  <a href="/insights/#card-census-shifts" class="vi-treemap-chip">
                    <span class="chip-metric">38.8% Urban</span>
                    <span class="chip-title">Census Growth &amp; Urbanization</span>
                  </a>
                  <a href="/insights/#card-districts-scatter" class="vi-treemap-chip">
                    <span class="chip-metric">135 Districts</span>
                    <span class="chip-title">Poverty vs Literacy Disparities</span>
                  </a>
                  <a href="/insights/#card-census-hist" class="vi-treemap-chip">
                    <span class="chip-metric">1951–2023</span>
                    <span class="chip-title">70-Year Census Trajectory</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Living Standards &amp; Household Budgets</span>
                <div class="vi-treemap-chips">
                  <a href="/insights/#card-hies" class="vi-treemap-chip">
                    <span class="chip-metric">42.4% Food</span>
                    <span class="chip-title">Food Engel Burden by Quintile</span>
                  </a>
                  <a href="/insights/#card-consumption-pie" class="vi-treemap-chip">
                    <span class="chip-metric">63.7% Basic</span>
                    <span class="chip-title">Household Consumption Basket</span>
                  </a>
                  <a href="/insights/#card-services" class="vi-treemap-chip">
                    <span class="chip-metric">6.2x Gap</span>
                    <span class="chip-title">Basic Utilities &amp; Infrastructure</span>
                  </a>
                  <a href="/insights/#card-lfs" class="vi-treemap-chip">
                    <span class="chip-metric">-34% Rural</span>
                    <span class="chip-title">Labor Participation &amp; Wage Gap</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-footer-link">
                <a href="/insights/">Launch Visual Analytics Lab Hub &rarr;</a>
              </div>
            </div>
          </details>

          <!-- Pillar 2: Data Observatories & Evidence Centre (Blue Theme) -->
          <details class="vi-treemap-tile theme-blue" data-pillar="data">
            <summary class="vi-treemap-summary">
              <div class="vi-treemap-sum-left">
                <span class="vi-treemap-icon" aria-hidden="true">🏛️</span>
                <div class="vi-treemap-sum-text">
                  <h3>Data Observatories &amp; Evidence Centre</h3>
                  <p>Harmonized indicators, macroeconomic benchmarks &amp; open downloads</p>
                </div>
              </div>
              <div class="vi-treemap-sum-right">
                <span class="vi-treemap-pill">8 Observatories</span>
                <svg class="vi-treemap-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
            </summary>
            <div class="vi-treemap-content">
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Thematic Data Observatories</span>
                <div class="vi-treemap-chips">
                  <a href="/data/centre.html" class="vi-treemap-chip">
                    <span class="chip-badge">Central Hub</span>
                    <span class="chip-title">Central Data Observatory &amp; Knowledge Map</span>
                  </a>
                  <a href="/data/public-finance/" class="vi-treemap-chip">
                    <span class="chip-badge">Finance</span>
                    <span class="chip-title">Public Finance &amp; NFC Divisible Pool</span>
                  </a>
                  <a href="/data/economy/" class="vi-treemap-chip">
                    <span class="chip-badge">Economy</span>
                    <span class="chip-title">Economy, Real Wages &amp; Inflation Benchmarks</span>
                  </a>
                  <a href="/data/population/" class="vi-treemap-chip">
                    <span class="chip-badge">Demographics</span>
                    <span class="chip-title">Population, Demographics &amp; Census 2023</span>
                  </a>
                  <a href="/data/living-standards/" class="vi-treemap-chip">
                    <span class="chip-badge">Welfare</span>
                    <span class="chip-title">Living Standards, Utilities &amp; HIES 2024–25</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Analytical Tools &amp; Data Access</span>
                <div class="vi-treemap-chips">
                  <a href="/data/compare/" class="vi-treemap-chip">
                    <span class="chip-badge">Interactive</span>
                    <span class="chip-title">Cross-Provincial Indicator Comparator</span>
                  </a>
                  <a href="/data/downloads/" class="vi-treemap-chip">
                    <span class="chip-badge">Open Data</span>
                    <span class="chip-title">Open Data Downloads (16 CSV &amp; JSON Datasets)</span>
                  </a>
                  <a href="/knowledge-library/" class="vi-treemap-chip">
                    <span class="chip-badge">Reference</span>
                    <span class="chip-title">Public Policy Knowledge Library</span>
                  </a>
                  <a href="/sources/" class="vi-treemap-chip">
                    <span class="chip-badge">Citations</span>
                    <span class="chip-title">Official Statistical Sources &amp; Citations</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-footer-link">
                <a href="/data/centre.html">Explore Central Data Observatory &rarr;</a>
              </div>
            </div>
          </details>

          <!-- Pillar 3: Scenario Lab & Cartographic Maps (Emerald Theme) -->
          <details class="vi-treemap-tile theme-emerald" data-pillar="maps">
            <summary class="vi-treemap-summary">
              <div class="vi-treemap-sum-left">
                <span class="vi-treemap-icon" aria-hidden="true">🗺️</span>
                <div class="vi-treemap-sum-text">
                  <h3>Scenario Lab &amp; Cartographic Maps</h3>
                  <p>Interactive spatial boundaries, administrative models &amp; district maps</p>
                </div>
              </div>
              <div class="vi-treemap-sum-right">
                <span class="vi-treemap-pill">Interactive Maps</span>
                <svg class="vi-treemap-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
            </summary>
            <div class="vi-treemap-content">
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Interactive Cartography</span>
                <div class="vi-treemap-chips">
                  <a href="/maps/scenarios/" class="vi-treemap-chip">
                    <span class="chip-badge">Interactive</span>
                    <span class="chip-title">PPRI-01 Administrative Scenario Lab (13-Unit Model)</span>
                  </a>
                  <a href="/maps/current/administrative.html" class="vi-treemap-chip">
                    <span class="chip-badge">Reference</span>
                    <span class="chip-title">Current Administrative Geography (4 Provinces &amp; ICT)</span>
                  </a>
                  <a href="/maps/" class="vi-treemap-chip">
                    <span class="chip-badge">Gallery</span>
                    <span class="chip-title">Cartographic Map Gallery &amp; District Topologies</span>
                  </a>
                  <a href="/scenarios/" class="vi-treemap-chip">
                    <span class="chip-badge">Governance</span>
                    <span class="chip-title">Subnational Governance Scenarios Suite</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-footer-link">
                <a href="/maps/scenarios/">Launch Interactive Scenario Lab &rarr;</a>
              </div>
            </div>
          </details>

          <!-- Pillar 4: Policy Research, Papers & Briefs (Indigo Theme) -->
          <details class="vi-treemap-tile theme-indigo" data-pillar="research">
            <summary class="vi-treemap-summary">
              <div class="vi-treemap-sum-left">
                <span class="vi-treemap-icon" aria-hidden="true">📑</span>
                <div class="vi-treemap-sum-text">
                  <h3>Policy Research, Papers &amp; Briefs</h3>
                  <p>Peer-reviewed reports, empirical field studies &amp; constitutional analysis</p>
                </div>
              </div>
              <div class="vi-treemap-sum-right">
                <span class="vi-treemap-pill">8 Major Studies</span>
                <svg class="vi-treemap-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
            </summary>
            <div class="vi-treemap-content">
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Flagship &amp; Empirical Reports</span>
                <div class="vi-treemap-chips">
                  <a href="/research/policy-papers/provincial-reorganization-of-pakistan.html" class="vi-treemap-chip">
                    <span class="chip-badge">Flagship</span>
                    <span class="chip-title">Provincial Reorganization of Pakistan</span>
                  </a>
                  <a href="/research/reports/income-went-up-why-does-life-feel-harder.html" class="vi-treemap-chip">
                    <span class="chip-badge">Report 1</span>
                    <span class="chip-title">Household Income vs Inflation (HIES 2024–25)</span>
                  </a>
                  <a href="/research/reports/bribe-you-cant-see-corruption-private-tax.html" class="vi-treemap-chip">
                    <span class="chip-badge">Report 2</span>
                    <span class="chip-title">NCPS 2025 Corruption: Bribes as Private Tax</span>
                  </a>
                  <a href="/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html" class="vi-treemap-chip">
                    <span class="chip-badge">Report 3</span>
                    <span class="chip-title">Price of a Simple Task: Bureaucracy Cost Index</span>
                  </a>
                  <a href="/research/reports/same-country-different-life-district-access.html" class="vi-treemap-chip">
                    <span class="chip-badge">Report 4</span>
                    <span class="chip-title">District Inequality: Disparities in Basic Services</span>
                  </a>
                  <a href="/research/reports/does-money-work-better-spent-closer-to-people.html" class="vi-treemap-chip">
                    <span class="chip-badge">Report 5</span>
                    <span class="chip-title">Fiscal Decentralization: Local Government vs ADP</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Working Papers &amp; Legal Frameworks</span>
                <div class="vi-treemap-chips">
                  <a href="/research/working-papers/provinces-local-government.html" class="vi-treemap-chip">
                    <span class="chip-badge">Working Paper</span>
                    <span class="chip-title">Provinces and Local Governments Interplay</span>
                  </a>
                  <a href="/research/briefs/administrative-scale.html" class="vi-treemap-chip">
                    <span class="chip-badge">Brief</span>
                    <span class="chip-title">Administrative Scale &amp; Governance Ratios</span>
                  </a>
                  <a href="/research/comparative-governance.html" class="vi-treemap-chip">
                    <span class="chip-badge">Comparative</span>
                    <span class="chip-title">Global Subnational Federations</span>
                  </a>
                  <a href="/research/legal-library.html" class="vi-treemap-chip">
                    <span class="chip-badge">Legal</span>
                    <span class="chip-title">Constitutional Legal Library (Articles 239 &amp; 140A)</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-footer-link">
                <a href="/research/">Explore PPRI Research Hub &rarr;</a>
              </div>
            </div>
          </details>

          <!-- Pillar 5: 25 Analytical Policy Articles (Purple Theme) -->
          <details class="vi-treemap-tile theme-purple" data-pillar="articles">
            <summary class="vi-treemap-summary">
              <div class="vi-treemap-sum-left">
                <span class="vi-treemap-icon" aria-hidden="true">📰</span>
                <div class="vi-treemap-sum-text">
                  <h3>Analytical Policy Articles &amp; Insights</h3>
                  <p>In-depth policy essays on provincial restructuring, fiscal federalism &amp; devolution</p>
                </div>
              </div>
              <div class="vi-treemap-sum-right">
                <span class="vi-treemap-pill">25 Articles</span>
                <svg class="vi-treemap-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
            </summary>
            <div class="vi-treemap-content">
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Provincial Restructuring &amp; Regional Demands</span>
                <div class="vi-treemap-chips">
                  <a href="/articles/four-provinces-241-million-people-administrative-scale.html" class="vi-treemap-chip">
                    <span class="chip-title">4 Provinces vs 241.5M Scale</span>
                  </a>
                  <a href="/articles/provinces-of-pakistan-names-capitals-population.html" class="vi-treemap-chip">
                    <span class="chip-title">Provinces of Pakistan (2026): Names &amp; Capitals</span>
                  </a>
                  <a href="/articles/south-punjab-why-does-the-province-demand-keep-returning.html" class="vi-treemap-chip">
                    <span class="chip-title">South Punjab: 11 Districts Map &amp; Budget</span>
                  </a>
                  <a href="/articles/hazara-province-why-has-the-demand-survived.html" class="vi-treemap-chip">
                    <span class="chip-title">Hazara Province Movement &amp; KP Fiscal Share</span>
                  </a>
                  <a href="/articles/karachi-urban-sindh-representation-revenue-administration.html" class="vi-treemap-chip">
                    <span class="chip-title">Karachi Structure: 7 Districts &amp; 25 Towns</span>
                  </a>
                  <a href="/articles/south-punjab-saraiki-bahawalpur-difference.html" class="vi-treemap-chip">
                    <span class="chip-title">South Punjab vs Saraiki vs Bahawalpur</span>
                  </a>
                  <a href="/articles/bahawalpur-province-restoration-2026.html" class="vi-treemap-chip">
                    <span class="chip-title">Bahawalpur Province Restoration &amp; 1955 Merger</span>
                  </a>
                  <a href="/articles/is-gilgit-baltistan-a-province-of-pakistan.html" class="vi-treemap-chip">
                    <span class="chip-title">Is Gilgit-Baltistan a Province? Legal Status</span>
                  </a>
                  <a href="/articles/new-administrative-units-pakistan-2026.html" class="vi-treemap-chip">
                    <span class="chip-title">New Provinces Debate: 13-Units Model</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Fiscal Federalism, NFC &amp; Local Devolution</span>
                <div class="vi-treemap-chips">
                  <a href="/articles/where-does-pakistans-development-money-go.html" class="vi-treemap-chip">
                    <span class="chip-title">Where Does Development Money Go? NFC &amp; ADP</span>
                  </a>
                  <a href="/articles/18th-amendment-did-devolution-stop-at-provincial-capital.html" class="vi-treemap-chip">
                    <span class="chip-title">18th Amendment: Devolution vs Article 140A</span>
                  </a>
                  <a href="/articles/more-provinces-or-stronger-local-governments.html" class="vi-treemap-chip">
                    <span class="chip-title">More Provinces vs Local Governments Dilemma</span>
                  </a>
                  <a href="/articles/did-2001-devolution-improve-services-evidence.html" class="vi-treemap-chip">
                    <span class="chip-title">Did 2001 Devolution Improve Services?</span>
                  </a>
                  <a href="/articles/how-far-is-government-administrative-distance.html" class="vi-treemap-chip">
                    <span class="chip-title">Administrative Distance &amp; Secretariat Travel Times</span>
                  </a>
                  <a href="/articles/how-should-pakistan-evaluate-a-new-province.html" class="vi-treemap-chip">
                    <span class="chip-title">PPRI 12-Point Empirical Evaluation Rubric</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-footer-link">
                <a href="/articles/">Browse All 25 Policy Articles &rarr;</a>
              </div>
            </div>
          </details>

          <!-- Pillar 6: Reform Frameworks, Consultations & Surveys (Amber Theme) -->
          <details class="vi-treemap-tile theme-amber" data-pillar="reform">
            <summary class="vi-treemap-summary">
              <div class="vi-treemap-sum-left">
                <span class="vi-treemap-icon" aria-hidden="true">🗳️</span>
                <div class="vi-treemap-sum-text">
                  <h3>Reform Frameworks, Consultations &amp; Surveys</h3>
                  <p>Constitutional mechanisms, 6 community surveys &amp; public participation</p>
                </div>
              </div>
              <div class="vi-treemap-sum-right">
                <span class="vi-treemap-pill">6 Community Surveys</span>
                <svg class="vi-treemap-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 9 12 15 18 9"></polyline></svg>
              </div>
            </summary>
            <div class="vi-treemap-content">
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Constitutional &amp; Administrative Models</span>
                <div class="vi-treemap-chips">
                  <a href="/provinces/proposed-models.html" class="vi-treemap-chip">
                    <span class="chip-badge">Model</span>
                    <span class="chip-title">13-Unit Administrative Restructuring Model</span>
                  </a>
                  <a href="/provinces/constitutional-framework.html" class="vi-treemap-chip">
                    <span class="chip-badge">Law</span>
                    <span class="chip-title">Article 239(4) Amendment Bill Procedure</span>
                  </a>
                  <a href="/provinces/transition-framework.html" class="vi-treemap-chip">
                    <span class="chip-badge">Execution</span>
                    <span class="chip-title">3-Year Civil Service &amp; Asset Transition</span>
                  </a>
                  <a href="/provinces/why-provinces.html" class="vi-treemap-chip">
                    <span class="chip-badge">Case</span>
                    <span class="chip-title">Why Subnational Reform? Core Case Studies</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-cluster">
                <span class="vi-treemap-cluster-label">Pakistan Community Surveys Hub</span>
                <div class="vi-treemap-chips">
                  <a href="/surveys/" class="vi-treemap-chip">
                    <span class="chip-badge">Hub</span>
                    <span class="chip-title">Pakistan Community Surveys Central Portal</span>
                  </a>
                  <a href="/surveys/new-provinces/" class="vi-treemap-chip">
                    <span class="chip-badge">Survey 1</span>
                    <span class="chip-title">New Provinces &amp; Regional Representation</span>
                  </a>
                  <a href="/surveys/local-government/" class="vi-treemap-chip">
                    <span class="chip-badge">Survey 2</span>
                    <span class="chip-title">Stronger Local Government &amp; Powers</span>
                  </a>
                  <a href="/surveys/household-costs-inflation/" class="vi-treemap-chip">
                    <span class="chip-badge">Survey 3</span>
                    <span class="chip-title">Household Costs &amp; Inflation Burden</span>
                  </a>
                  <a href="/surveys/youth-jobs/" class="vi-treemap-chip">
                    <span class="chip-badge">Survey 4</span>
                    <span class="chip-title">Youth Jobs &amp; Career Opportunities</span>
                  </a>
                  <a href="/surveys/jobs-abroad/" class="vi-treemap-chip">
                    <span class="chip-badge">Survey 5</span>
                    <span class="chip-title">Jobs Abroad &amp; Moving for Work</span>
                  </a>
                  <a href="/surveys/government-delays/" class="vi-treemap-chip">
                    <span class="chip-badge">Survey 6</span>
                    <span class="chip-title">Government Delays &amp; Paperwork Cost</span>
                  </a>
                  <a href="/consultation/submissions.html" class="vi-treemap-chip">
                    <span class="chip-badge">Feedback</span>
                    <span class="chip-title">Submit Policy Memoranda &amp; Research Ideas</span>
                  </a>
                </div>
              </div>
              <div class="vi-treemap-footer-link">
                <a href="/surveys/">Take a Pakistan Community Survey &rarr;</a>
              </div>
            </div>
          </details>
        </div>
      </div>
    </section>
'''

dir_start = html.find('<section class="site-directory"')
if dir_start != -1:
    dir_end = html.find('</section>', dir_start) + len('</section>')
    html = html[:dir_start] + treemap_html + html[dir_end:]
    print("Successfully replaced site-directory with .vi-treemap-section")
else:
    print("Warning: site-directory section not found")

# Add small script before </body> to support Expand All / Collapse All button
script_tag = '''
  <script>
    (function() {
      var btn = document.getElementById('viTreemapToggleAll');
      if (!btn) return;
      btn.addEventListener('click', function() {
        var tiles = document.querySelectorAll('.vi-treemap-tile');
        var isExpanded = btn.getAttribute('aria-expanded') === 'true';
        tiles.forEach(function(t) {
          t.open = !isExpanded;
        });
        btn.setAttribute('aria-expanded', !isExpanded ? 'true' : 'false');
        btn.querySelector('.toggle-text').textContent = !isExpanded ? 'Collapse All' : 'Expand All';
        btn.querySelector('.toggle-icon').textContent = !isExpanded ? '⊟' : '⊞';
      });
    })();
  </script>
'''

if 'viTreemapToggleAll' not in html:
    html = html.replace('</body>', script_tag + '\n</body>')
    print("Added toggle controller script before </body>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html fully updated!")
