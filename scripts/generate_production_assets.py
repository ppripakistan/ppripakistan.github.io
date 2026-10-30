# -*- coding: utf-8 -*-
"""
Generate Production Assets for Visual Analytics:
1. assets/css/visual-insights.css
2. assets/js/modules/visual-insights.js
3. insights/index.html (Canonical Public Visual Analytics Lab)
"""

import os
import json
import re

PUBLISHED_DIR = os.path.join("data", "published")

# 1. Load active published datasets
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

loaded_db = {}
for k, fname in datasets.items():
    p = os.path.join(PUBLISHED_DIR, fname)
    with open(p, 'r', encoding='utf-8') as f:
        loaded_db[k] = json.load(f)

embedded_json = json.dumps(loaded_db)

# Read build_insights_html.py to extract CSS and JS
with open('scripts/build_insights_html.py', 'r', encoding='utf-8') as f:
    orig_code = f.read()

# 2. Extract CSS
css_start = orig_code.find('<style>') + 7
css_end = orig_code.find('</style>')
raw_css = orig_code[css_start:css_end].strip()

# Clean up CSS: remove body overrides and staging-specific styles if any
os.makedirs('assets/css', exist_ok=True)
with open('assets/css/visual-insights.css', 'w', encoding='utf-8') as f:
    f.write(raw_css)
print("Created assets/css/visual-insights.css (", len(raw_css), "bytes)")

# 3. Extract JS
js_start = orig_code.find('<script>') + 8
js_end = orig_code.rfind('</script>')
raw_js = orig_code[js_start:js_end].strip()

# In raw_js, replace embedded_json placeholder if needed
if "''' + embedded_json + r'''" in raw_js:
    raw_js = raw_js.replace("''' + embedded_json + r'''", embedded_json)

# Make sure window functions are exported and auto-init renders whatever cards exist on the page
auto_init_block = """
        // Auto-initialize whichever cards are present in the DOM
        const cardRenderers = [
          { id: 'svg-card-fiscal', fn: renderCard1Fiscal },
          { id: 'svg-card-debt', fn: renderCard2Debt },
          { id: 'svg-card-tax-exp', fn: renderCard3TaxExp },
          { id: 'svg-card-gender-land', fn: renderCard4GenderLand },
          { id: 'svg-card-hies', fn: renderCard5Hies },
          { id: 'svg-card-consumption-pie', fn: renderCard6ConsumptionPie },
          { id: 'svg-card-wage-infl', fn: renderCard7WageInfl },
          { id: 'svg-card-services', fn: renderCard8Services },
          { id: 'svg-card-lfs', fn: renderCard9Lfs },
          { id: 'svg-card-census-shifts', fn: renderCard10CensusShifts },
          { id: 'svg-card-districts-scatter', fn: renderCard11DistrictsScatter },
          { id: 'svg-card-sector-employment', fn: renderCard12SectorEmployment },
          { id: 'svg-card-agri-shifts', fn: renderCard13AgriShifts },
          { id: 'svg-card-census-hist', fn: renderCard14CensusHist },
          { id: 'svg-card-macro', fn: renderCard15Macro },
          { id: 'svg-card-prov-matrix', fn: renderCard16ProvMatrix }
        ];

        window.initVisualInsights = function() {
          cardRenderers.forEach(item => {
            if (document.getElementById(item.id)) {
              try { item.fn(); } catch(e) { console.error('Error rendering ' + item.id, e); }
            }
          });
        };

        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', window.initVisualInsights);
        } else {
          window.initVisualInsights();
        }
"""

# Replace the DOMContentLoaded listener in raw_js with our auto_init_block
if "document.addEventListener('DOMContentLoaded', () => {" in raw_js:
    idx_dcl = raw_js.find("document.addEventListener('DOMContentLoaded', () => {")
    idx_dcl_end = raw_js.find("});\n      })();", idx_dcl)
    raw_js = raw_js[:idx_dcl] + auto_init_block + "\n      })();"

os.makedirs('assets/js/modules', exist_ok=True)
with open('assets/js/modules/visual-insights.js', 'w', encoding='utf-8') as f:
    f.write(raw_js)
print("Created assets/js/modules/visual-insights.js (", len(raw_js), "bytes)")

print("Production assets generation complete!")
