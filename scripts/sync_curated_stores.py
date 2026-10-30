#!/usr/bin/env python3
"""
scripts/sync_curated_stores.py
Phase 5 Complete Overhaul: Synchronizes verified staging tables and multi-year analytical series
into domain-specific modular curated data stores under data/curated/ and mirrors to data/staging/.

Maintains clean, human-readable CSV (with UTF-8 BOM for Excel) and JSON files for:
1. census_2023_districts.csv & .json (141 records: all 135 districts + ICT + 4 provinces + Pakistan)
2. lfs_employment_wages.csv & .json (National & provincial LFPR, employment shares, wages)
3. hies_household_expenditures.csv & .json (Monthly consumption, food/housing share by province and urban/rural)
4. federal_fiscal_summary.csv & .json (Multi-year FBR taxes, debt servicing, and debt stocks)
5. macro_indicators_timeseries.csv & .json (35 years of annual macroeconomic indicators 1990–2024)
6. public_debt_timeseries.csv & .json (8-year public debt accumulation FY2018–FY2026)
7. census_historical_growth.csv & .json (70-year intercensal growth 1951–2023)
8. agri_census_2024_summary.csv & .json (2010 vs 2024 farm counts, acreage, fragmentation, crops)
9. tax_expenditures_2025.csv & .json (FBR tax concessions & revenue foregone by regime)
10. housing_basic_services.csv & .json (Household access to piped water, sanitation, electricity, clean fuel)
11. inflation_wage_growth.csv & .json (2020–2024 cumulative inflation vs nominal wage index)
12. provincial_gender_demographics.csv & .json (Census 2023 Male, Female, Transgender, Sex Ratio, Area sq km, Pop & Land shares)
13. provincial_census_shifts.csv & .json (1981, 1998, 2017, 2023 provincial population & percentage shares)
14. provincial_consumption_pies.csv & .json (HIES 2024–25 budget distribution: Food, Housing, Health, Education, Other)
15. provincial_agri_shifts.csv & .json (Ag Census 2010 vs 2024 provincial cultivated, uncultivated, and farm variations)

Zero external dependencies: uses pure standard Python (csv, json, shutil, pathlib).
"""

import sys
import shutil
import csv
import json
from pathlib import Path
from datetime import datetime, timezone

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = Path(__file__).resolve().parent.parent
STAGING_DIR = ROOT_DIR / "data" / "staging"
CURATED_DIR = ROOT_DIR / "data" / "curated"

def save_curated_pair(filename_base, records):
    """Saves records as CSV (with UTF-8 BOM) and JSON in data/curated/ and mirrors to data/staging/."""
    csv_path = CURATED_DIR / f"{filename_base}.csv"
    json_path = CURATED_DIR / f"{filename_base}.json"
    stg_csv_path = STAGING_DIR / f"{filename_base}.csv"
    stg_json_path = STAGING_DIR / f"{filename_base}.json"
    
    if not records:
        return
        
    fieldnames = list(records[0].keys())
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
        
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)

    shutil.copy2(csv_path, stg_csv_path)
    shutil.copy2(json_path, stg_json_path)
        
    print(f"  [CURATED & STAGED] {csv_path.name} ({len(records)} rows)")

def generate_overhaul_datasets():
    """Generates the new analytical series for gender demographics, multi-census shifts, and provincial pies."""
    
    # 1. Provincial Gender Demographics & Land Area Asymmetry (Census 2023)
    gender_demo = [
        {
            "geography_id": "PK",
            "geography_name": "Pakistan",
            "population_2023": 241499431,
            "population_male": 124324294,
            "population_female": 117154947,
            "population_transgender": 20190,
            "male_share_pct": 51.48,
            "female_share_pct": 48.51,
            "transgender_share_pct": 0.01,
            "sex_ratio": 106.12,
            "area_sqkm": 796096.0,
            "land_area_share_pct": 100.0,
            "population_share_pct": 100.0,
            "density_per_sqkm": 303.35,
            "source_citation": "PBS Digital Census 2023 Table 1"
        },
        {
            "geography_id": "PK-PB",
            "geography_name": "Punjab",
            "population_2023": 127688922,
            "population_male": 64306472,
            "population_female": 63371460,
            "population_transgender": 10990,
            "male_share_pct": 50.36,
            "female_share_pct": 49.63,
            "transgender_share_pct": 0.01,
            "sex_ratio": 101.48,
            "area_sqkm": 205345.0,
            "land_area_share_pct": 25.79,
            "population_share_pct": 52.87,
            "density_per_sqkm": 621.83,
            "source_citation": "PBS Digital Census 2023 Table 1"
        },
        {
            "geography_id": "PK-SD",
            "geography_name": "Sindh",
            "population_2023": 55696147,
            "population_male": 28849271,
            "population_female": 26842476,
            "population_transgender": 4400,
            "male_share_pct": 51.80,
            "female_share_pct": 48.19,
            "transgender_share_pct": 0.01,
            "sex_ratio": 107.48,
            "area_sqkm": 140914.0,
            "land_area_share_pct": 17.70,
            "population_share_pct": 23.06,
            "density_per_sqkm": 395.25,
            "source_citation": "PBS Digital Census 2023 Table 1"
        },
        {
            "geography_id": "PK-KP",
            "geography_name": "Khyber Pakhtunkhwa",
            "population_2023": 40856097,
            "population_male": 20637458,
            "population_female": 20215823,
            "population_transgender": 2816,
            "male_share_pct": 50.51,
            "female_share_pct": 49.48,
            "transgender_share_pct": 0.01,
            "sex_ratio": 102.09,
            "area_sqkm": 101741.0,
            "land_area_share_pct": 12.78,
            "population_share_pct": 16.92,
            "density_per_sqkm": 401.57,
            "source_citation": "PBS Digital Census 2023 Table 1"
        },
        {
            "geography_id": "PK-BA",
            "geography_name": "Balochistan",
            "population_2023": 14894402,
            "population_male": 7752385,
            "population_female": 7141180,
            "population_transgender": 837,
            "male_share_pct": 52.05,
            "female_share_pct": 47.95,
            "transgender_share_pct": 0.01,
            "sex_ratio": 108.56,
            "area_sqkm": 347190.0,
            "land_area_share_pct": 43.61,
            "population_share_pct": 6.17,
            "density_per_sqkm": 42.90,
            "source_citation": "PBS Digital Census 2023 Table 1"
        },
        {
            "geography_id": "PK-IS",
            "geography_name": "Islamabad",
            "population_2023": 2363863,
            "population_male": 1228891,
            "population_female": 1134679,
            "population_transgender": 293,
            "male_share_pct": 51.99,
            "female_share_pct": 48.00,
            "transgender_share_pct": 0.01,
            "sex_ratio": 108.30,
            "area_sqkm": 906.0,
            "land_area_share_pct": 0.11,
            "population_share_pct": 0.98,
            "density_per_sqkm": 2609.12,
            "source_citation": "PBS Digital Census 2023 Table 1"
        }
    ]
    save_curated_pair("provincial_gender_demographics", gender_demo)

    # 2. Multi-Census Provincial Population Shifts (1981, 1998, 2017, 2023)
    census_shifts = [
        {
            "census_year": 1981,
            "punjab_pop_m": 47.29,
            "punjab_share_pct": 56.13,
            "sindh_pop_m": 19.03,
            "sindh_share_pct": 22.59,
            "kp_pop_m": 13.25,
            "kp_share_pct": 15.73,
            "balochistan_pop_m": 4.33,
            "balochistan_share_pct": 5.14,
            "ict_pop_m": 0.34,
            "ict_share_pct": 0.40,
            "total_pakistan_pop_m": 84.25
        },
        {
            "census_year": 1998,
            "punjab_pop_m": 73.62,
            "punjab_share_pct": 55.63,
            "sindh_pop_m": 30.44,
            "sindh_share_pct": 23.00,
            "kp_pop_m": 20.96,
            "kp_share_pct": 15.84,
            "balochistan_pop_m": 6.57,
            "balochistan_share_pct": 4.96,
            "ict_pop_m": 0.81,
            "ict_share_pct": 0.61,
            "total_pakistan_pop_m": 132.35
        },
        {
            "census_year": 2017,
            "punjab_pop_m": 110.01,
            "punjab_share_pct": 52.97,
            "sindh_pop_m": 47.89,
            "sindh_share_pct": 23.06,
            "kp_pop_m": 35.53,
            "kp_share_pct": 17.11,
            "balochistan_pop_m": 12.34,
            "balochistan_share_pct": 5.94,
            "ict_pop_m": 2.01,
            "ict_share_pct": 0.97,
            "total_pakistan_pop_m": 207.68
        },
        {
            "census_year": 2023,
            "punjab_pop_m": 127.69,
            "punjab_share_pct": 52.87,
            "sindh_pop_m": 55.70,
            "sindh_share_pct": 23.06,
            "kp_pop_m": 40.86,
            "kp_share_pct": 16.92,
            "balochistan_pop_m": 14.89,
            "balochistan_share_pct": 6.17,
            "ict_pop_m": 2.36,
            "ict_share_pct": 0.98,
            "total_pakistan_pop_m": 241.50
        }
    ]
    save_curated_pair("provincial_census_shifts", census_shifts)

    # 3. Provincial Living Standards & Food Spend Pie Breakdown (HIES 2024-25)
    prov_pies = [
        {
            "geography_id": "PK",
            "geography_name": "Pakistan",
            "mean_monthly_expenditure_pkr": 62850,
            "food_pct": 39.2,
            "housing_utilities_pct": 24.6,
            "health_pct": 5.8,
            "education_pct": 4.2,
            "transport_comm_pct": 11.4,
            "clothing_other_pct": 14.8
        },
        {
            "geography_id": "PK-PB",
            "geography_name": "Punjab",
            "mean_monthly_expenditure_pkr": 65200,
            "food_pct": 38.5,
            "housing_utilities_pct": 25.1,
            "health_pct": 5.6,
            "education_pct": 4.6,
            "transport_comm_pct": 11.6,
            "clothing_other_pct": 14.6
        },
        {
            "geography_id": "PK-SD",
            "geography_name": "Sindh",
            "mean_monthly_expenditure_pkr": 64800,
            "food_pct": 39.1,
            "housing_utilities_pct": 25.8,
            "health_pct": 5.5,
            "education_pct": 4.1,
            "transport_comm_pct": 11.2,
            "clothing_other_pct": 14.3
        },
        {
            "geography_id": "PK-KP",
            "geography_name": "Khyber Pakhtunkhwa",
            "mean_monthly_expenditure_pkr": 58400,
            "food_pct": 41.2,
            "housing_utilities_pct": 22.9,
            "health_pct": 6.3,
            "education_pct": 4.0,
            "transport_comm_pct": 10.8,
            "clothing_other_pct": 14.8
        },
        {
            "geography_id": "PK-BA",
            "geography_name": "Balochistan",
            "mean_monthly_expenditure_pkr": 53100,
            "food_pct": 44.6,
            "housing_utilities_pct": 21.4,
            "health_pct": 6.7,
            "education_pct": 2.8,
            "transport_comm_pct": 9.8,
            "clothing_other_pct": 14.7
        }
    ]
    save_curated_pair("provincial_consumption_pies", prov_pies)

    # 4. Provincial Agricultural Shift (Ag Census 2010 vs 2024)
    prov_agri = [
        {
            "province_name": "Punjab",
            "farms_2010": 5249400,
            "farms_2024": 6842100,
            "farms_change_pct": 30.3,
            "cultivated_acres_2010": 28640100,
            "cultivated_acres_2024": 33120400,
            "cultivated_change_pct": 15.6,
            "avg_farm_size_2024": 4.8
        },
        {
            "province_name": "Sindh",
            "farms_2010": 1115300,
            "farms_2024": 1598400,
            "farms_change_pct": 43.3,
            "cultivated_acres_2010": 7940200,
            "cultivated_acres_2024": 9480100,
            "cultivated_change_pct": 19.4,
            "avg_farm_size_2024": 5.9
        },
        {
            "province_name": "Khyber Pakhtunkhwa",
            "farms_2010": 1618200,
            "farms_2024": 2241500,
            "farms_change_pct": 38.5,
            "cultivated_acres_2010": 3980100,
            "cultivated_acres_2024": 4920200,
            "cultivated_change_pct": 23.6,
            "avg_farm_size_2024": 2.2
        },
        {
            "province_name": "Balochistan",
            "farms_2010": 281580,
            "farms_2024": 421697,
            "farms_change_pct": 49.8,
            "cultivated_acres_2010": 2062073,
            "cultivated_acres_2024": 5266964,
            "cultivated_change_pct": 155.4,
            "avg_farm_size_2024": 12.5
        }
    ]
    save_curated_pair("provincial_agri_shifts", prov_agri)

def main():
    print("=" * 75)
    print("  PPRI: SYNCHRONIZING OVERHAULED CURATED DATA STORES")
    print("=" * 75)
    
    CURATED_DIR.mkdir(parents=True, exist_ok=True)
    STAGING_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Base stores from staging
    base_mappings = [
        ("census_2023_districts_baseline", "census_2023_districts"),
        ("lfs_employment_indicators", "lfs_employment_wages"),
        ("hies_household_expenditures", "hies_household_expenditures"),
        ("federal_fiscal_summary", "federal_fiscal_summary"),
        ("macro_indicators_timeseries", "macro_indicators_timeseries"),
        ("public_debt_timeseries", "public_debt_timeseries"),
        ("census_historical_growth", "census_historical_growth"),
        ("agri_census_2024_summary", "agri_census_2024_summary"),
        ("tax_expenditures_2025", "tax_expenditures_2025"),
        ("housing_basic_services", "housing_basic_services"),
        ("inflation_wage_growth", "inflation_wage_growth")
    ]
    
    for s_base, t_base in base_mappings:
        src_csv = STAGING_DIR / f"{s_base}.csv"
        src_json = STAGING_DIR / f"{s_base}.json"
        dst_csv = CURATED_DIR / f"{t_base}.csv"
        dst_json = CURATED_DIR / f"{t_base}.json"
        
        if src_csv.exists():
            with open(src_csv, "r", encoding="utf-8-sig") as f_in:
                content = f_in.read()
            with open(dst_csv, "w", encoding="utf-8-sig", newline="") as f_out:
                f_out.write(content)
            with open(dst_csv, "r", encoding="utf-8-sig") as f:
                row_count = sum(1 for _ in csv.DictReader(f))
            print(f"  [SYNCED] {dst_csv.name} ({row_count} rows)")
            
        if src_json.exists():
            shutil.copy2(src_json, dst_json)
            
    # 2. Overhaul multi-year and provincial series
    print("\n[Generating] Overhauled provincial and multi-year series...")
    generate_overhaul_datasets()
    
    print("\n" + "=" * 75)
    print("  OVERHAULED CURATED STORES SYNCHRONIZATION COMPLETE (15 DATASETS)")
    print("=" * 75)

if __name__ == "__main__":
    main()
