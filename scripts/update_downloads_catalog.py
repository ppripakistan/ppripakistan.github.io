import sys
import json
import os
sys.stdout.reconfigure(encoding='utf-8')

datasets_info = [
    {
        'key': 'federal_fiscal_summary',
        'title': 'Federal Budget Outlays & Sovereign Debt Servicing Monopoly',
        'badge': 'Ministry of Finance &bull; Annual Budget Statement',
        'desc': 'Detailed expenditure breakdown of sovereign debt markup, defence, federal PSDP, civil administration, pensions, and subsidies across FY24, FY25, and FY26.'
    },
    {
        'key': 'public_debt_timeseries',
        'title': '8-Year Sovereign Public Debt Surge & Markup Trajectory (FY18–FY26)',
        'badge': 'State Bank of Pakistan &bull; Debt Bulletin',
        'desc': 'Historical series of total sovereign debt stock (PKR Billion) and annual debt markup interest servicing payments.'
    },
    {
        'key': 'tax_expenditures_2025',
        'title': 'Federal Tax Concessions, Exemptions & Zero-Rating (Tax Expenditure)',
        'badge': 'Federal Board of Revenue &bull; Tax Expenditure Report',
        'desc': 'Corporate and sectoral revenue foregone across Sales Tax exemptions, Income Tax concessions, Customs exemptions, and FTR privileges.'
    },
    {
        'key': 'provincial_fiscal_conflict_matrix',
        'title': 'Provincial Resource Allocation, Debt Stock & Conflict Exposure Matrix',
        'badge': 'Provincial Finance Depts, SBP, NACTA',
        'desc': 'Comparative multi-dimensional matrix of Punjab, Sindh, KP, and Balochistan covering total budgets, ADP allocations, public debt, per capita spends, and regional conflict incidents.'
    },
    {
        'key': 'macro_indicators_timeseries',
        'title': '35-Year Macroeconomic Trajectory Across 4 Political Regimes (FY90–FY24)',
        'badge': 'PBS, SBP & World Bank',
        'desc': 'Annual timeseries of real GDP growth, CPI inflation, external current account balance (% GDP), and total public debt (% GDP).'
    },
    {
        'key': 'inflation_wage_growth',
        'title': 'Real Purchasing Power Erosion, Minimum Wage & CPI Squeeze',
        'badge': 'PBS CPI / Ministry of Labour',
        'desc': 'Tracking headline consumer price inflation against statutory minimum wage adjustments and cumulative purchasing power degradation.'
    },
    {
        'key': 'provincial_gender_demographics',
        'title': 'Female Gender Ratios & Agrarian Landholding Asymmetry',
        'badge': 'PBS Census 2023 & Agricultural Census',
        'desc': 'Cross-provincial metrics comparing female sex ratios (females per 1,000 males) against female agricultural landownership percentages.'
    },
    {
        'key': 'hies_household_expenditures',
        'title': 'Household Income & Regressive Food Engel Ratios (HIES 2024–25)',
        'badge': 'PBS HIES 2024–25',
        'desc': 'Average monthly household income, consumption outlays, and food spending shares across income quintiles Q1 through Q5.'
    },
    {
        'key': 'provincial_consumption_pies',
        'title': 'Provincial Food vs Non-Food Household Consumption Baskets',
        'badge': 'PBS HIES 2024–25',
        'desc': 'Provincial food expenditure budget percentages versus essential non-food requirements (housing, health, utilities, transport).'
    },
    {
        'key': 'housing_basic_services',
        'title': 'Basic Housing Characteristics & Clean Water Access Deficits',
        'badge': 'PBS 7th Housing Census 2023',
        'desc': 'Provincial coverage rates for piped drinking water, grid electricity access, flush sanitation, and clean cooking fuel.'
    },
    {
        'key': 'lfs_employment_wages',
        'title': 'Labour Force Gender Employment & Urban/Rural Wage Disparities',
        'badge': 'PBS Labour Force Survey (LFS)',
        'desc': 'Cross-provincial comparison of female labour force participation, male vs female average wages, and rural wage discounts.'
    },
    {
        'key': 'provincial_census_shifts',
        'title': '4-Decade Provincial Demographic Growth Trajectories (1981–2023)',
        'badge': 'PBS Historical Censuses',
        'desc': 'Provincial population headcounts and annual intercensal compound annual growth rates across the 1981, 1998, 2017, and 2023 censuses.'
    },
    {
        'key': 'census_2023_districts',
        'title': '135 Districts Urbanization vs Density Quadrant Scale',
        'badge': 'PBS 7th Population Census 2023',
        'desc': 'Complete microdata of 135 districts across Pakistan with population headcount, urbanization share (%), density (persons/sq km), and province tagging.'
    },
    {
        'key': 'provincial_agri_shifts',
        'title': 'Smallholder Landholding Fragmentation Dynamics',
        'badge': 'PBS Agriculture Census',
        'desc': 'Farms and cultivated acreage distributions across subsistence (<5 acres), small (5–12.5 acres), medium (12.5–50 acres), and large (>50 acres) landholdings.'
    },
    {
        'key': 'census_historical_growth',
        'title': '70-Year Intercensal Demographic Trajectory (1951–2023)',
        'badge': 'PBS Historical Censuses (1951–2023)',
        'desc': 'National headcount growth milestones, intercensal growth rates, and urbanization expansion over seven decades of statehood.'
    }
]

# Generate HTML cards
cards_html = []
for d in datasets_info:
    csv_path = f"data/published/{d['key']}.csv"
    json_path = f"data/published/{d['key']}.json"
    
    # Calculate row count
    row_count = "Published Store"
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as f:
            lines = [l for l in f if l.strip()]
            row_count = f"{max(0, len(lines)-1)} records"

    card = f"""          <div class="obs-stat-card" style="margin-bottom:16px;">
            <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px;">
              <div style="max-width:760px;">
                <span class="obs-badge obs-badge-official">{d['badge']}</span>
                <span class="obs-badge obs-badge-period">{row_count}</span>
                <h3 style="margin:8px 0 4px 0;font-size:1.12rem;color:var(--obs-dark);">{d['title']}</h3>
                <p style="font-size:0.9rem;color:var(--obs-text);margin:0 0 8px 0;line-height:1.5;">{d['desc']}</p>
              </div>
              <div style="display:flex;gap:8px;align-items:center;flex-shrink:0;">
                <a href="/data/published/{d['key']}.csv" download="PPRI_{d['key']}.csv" class="obs-btn obs-btn-primary" style="padding:6px 14px;font-size:0.85rem;text-decoration:none;">Download CSV</a>
                <a href="/data/published/{d['key']}.json" download="PPRI_{d['key']}.json" class="obs-btn" style="padding:6px 12px;font-size:0.85rem;text-decoration:none;">JSON</a>
              </div>
            </div>
          </div>"""
    cards_html.append(card)

section_content = f"""
        <!-- ================= PUBLISHED VISUAL ANALYTICS DATASETS ================= -->
        <section class="obs-section" id="visual-analytics-datasets" style="margin-top:32px;">
          <div class="obs-section-header">
            <div>
              <span class="obs-badge obs-badge-official">&check; Production Data Stores</span>
              <h2 class="obs-section-title" style="margin-top:6px;">PPRI Visual Analytics &amp; Empirical Baseline Stores (2024–2026)</h2>
              <p class="obs-lead" style="font-size:0.95rem;color:var(--obs-text-muted);margin-top:4px;">
                The 15 curated, machine-readable datasets powering PPRI's 16 interactive policy infographics. Formatted with Excel UTF-8 BOM encoding and validated JSON schemas.
              </p>
            </div>
          </div>

          <div style="margin-top:16px;">
{chr(10).join(cards_html)}
          </div>
        </section>
"""

with open('data/downloads/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

if 'id="visual-analytics-datasets"' not in text:
    # Insert before Citation & Open Data License
    target = 'Citation &amp; Open Data License'
    pos = text.find(target)
    if pos != -1:
        sec_start = text.rfind('<section class="obs-section"', 0, pos)
        text = text[:sec_start] + section_content + '\n\n        ' + text[sec_start:]
    else:
        # Fallback before footer
        pos = text.find('<footer class="site-footer">')
        text = text[:pos] + section_content + '\n\n        ' + text[pos:]

    with open('data/downloads/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("data/downloads/index.html updated with 15 published datasets!")
else:
    print("visual-analytics-datasets already present in data/downloads/index.html")
