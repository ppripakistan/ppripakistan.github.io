import json
import os
import re

base_dir = os.path.join("data", "staging")

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
    'macro': 'macro_indicators_timeseries.json'
}

schema = {}
for k, fname in datasets.items():
    p = os.path.join(base_dir, fname)
    with open(p, 'r', encoding='utf-8') as f:
        data = json.load(f)
        schema[k] = list(data[0].keys())
        print(f"[{k}] ({len(data)} rows):")
        print("  ", schema[k])

with open("data/staging/insights.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's inspect each renderCard function
funcs = [
    ("Card 1 (Fiscal)", "renderCard1Fiscal", "fiscal"),
    ("Card 2 (Debt)", "renderCard2Debt", "debt"),
    ("Card 3 (Tax Exp)", "renderCard3TaxExp", "tax_exp"),
    ("Card 4 (Gender Land)", "renderCard4GenderLand", "gender_land"),
    ("Card 5 (HIES)", "renderCard5Hies", "hies"),
    ("Card 6 (Consumption Pie)", "renderCard6ConsumptionPie", "consumption"),
    ("Card 7 (Wage Inflation)", "renderCard7WageInfl", "wage_infl"),
    ("Card 8 (Services)", "renderCard8Services", "services"),
    ("Card 9 (LFS)", "renderCard9Lfs", "lfs"),
    ("Card 10 (Census Shifts)", "renderCard10CensusShifts", "census_shifts"),
    ("Card 11 (Districts Scatter)", "renderCard11DistrictsScatter", "districts"),
    ("Card 12 (Sector Employment)", "renderCard12SectorEmployment", "lfs"),
    ("Card 13 (Agri Shifts)", "renderCard13AgriShifts", "agri_shifts"),
    ("Card 14 (Census Hist)", "renderCard14CensusHist", "census_hist"),
    ("Card 15 (Macro)", "renderCard15Macro", "macro"),
]

print("\n" + "="*60)
print("  AUDITING EACH CARD'S PROPERTY ACCESSORS AGAINST JSON SCHEMA")
print("="*60)

for card_label, fn_name, db_key in funcs:
    start = html.find(f"function {fn_name}()")
    next_fn = html.find("function ", start + 10)
    fn_body = html[start:next_fn] if next_fn != -1 else html[start:start+2500]
    
    # Find all property accesses like r.foo, d.foo, s.val, etc.
    accesses = set(re.findall(r'(?:r|d|pr|activeRow)\.([a-zA-Z0-9_]+)', fn_body))
    valid_keys = set(schema[db_key])
    
    invalid = [acc for acc in accesses if acc not in valid_keys]
    print(f"\n{card_label} -> accesses on db.{db_key}:")
    print(f"  Valid: {len(accesses - set(invalid))}")
    if invalid:
        print(f"  [MISMATCH DETECTED]: {invalid}")
    else:
        print(f"  [ALL KEYS VALID]")
