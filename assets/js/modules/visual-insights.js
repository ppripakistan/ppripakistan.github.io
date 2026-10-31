(function() {
        'use strict';

        // 1. EMBEDDED ZERO-NETWORK IN-MEMORY REPOSITORIES (134 KB Total)
        const EMBEDDED_DATA = {"fiscal": [{"fiscal_year": "2023-24", "reference_period": "FY2023\u201324 (Actual)", "gdp_current_market_prices_pkr_b": 106045, "federal_gross_revenue_pkr_b": 12163, "fbr_tax_collection_pkr_b": 9311, "fbr_direct_taxes_pkr_b": 4528, "fbr_sales_tax_pkr_b": 3097, "fbr_customs_duty_pkr_b": 1104, "fbr_federal_excise_pkr_b": 582, "non_tax_revenue_pkr_b": 2852, "provincial_transfers_nfc_pkr_b": 5169, "federal_net_revenue_pkr_b": 6994, "total_federal_expenditure_pkr_b": 14460, "debt_servicing_interest_pkr_b": 7302, "defence_services_pkr_b": 1804, "federal_psdp_development_pkr_b": 950, "civil_administration_pkr_b": 634, "subsidies_pkr_b": 1071, "pensions_pkr_b": 801, "fiscal_deficit_share_of_gdp_pct": -6.8, "total_public_debt_pkr_b": 71244, "domestic_debt_pkr_b": 47160, "external_debt_pkr_b": 24084, "source_citation": "PES 2025\u201326 / Budget in Brief / MoF Debt Bulletin"}, {"fiscal_year": "2024-25", "reference_period": "FY2024\u201325 (Revised)", "gdp_current_market_prices_pkr_b": 118430, "federal_gross_revenue_pkr_b": 14280, "fbr_tax_collection_pkr_b": 11520, "fbr_direct_taxes_pkr_b": 5010, "fbr_sales_tax_pkr_b": 4120, "fbr_customs_duty_pkr_b": 1480, "fbr_federal_excise_pkr_b": 910, "non_tax_revenue_pkr_b": 2760, "provincial_transfers_nfc_pkr_b": 6240, "federal_net_revenue_pkr_b": 8040, "total_federal_expenditure_pkr_b": 16580, "debt_servicing_interest_pkr_b": 8750, "defence_services_pkr_b": 1980, "federal_psdp_development_pkr_b": 1150, "civil_administration_pkr_b": 745, "subsidies_pkr_b": 1180, "pensions_pkr_b": 920, "fiscal_deficit_share_of_gdp_pct": -5.9, "total_public_debt_pkr_b": 78150, "domestic_debt_pkr_b": 53210, "external_debt_pkr_b": 24940, "source_citation": "PES 2025\u201326 / Budget in Brief / MoF Debt Bulletin"}, {"fiscal_year": "2025-26", "reference_period": "FY2025\u201326 (Provisional)", "gdp_current_market_prices_pkr_b": 126870, "federal_gross_revenue_pkr_b": 17815, "fbr_tax_collection_pkr_b": 12970, "fbr_direct_taxes_pkr_b": 5512, "fbr_sales_tax_pkr_b": 4938, "fbr_customs_duty_pkr_b": 1590, "fbr_federal_excise_pkr_b": 930, "non_tax_revenue_pkr_b": 4845, "provincial_transfers_nfc_pkr_b": 7438, "federal_net_revenue_pkr_b": 10377, "total_federal_expenditure_pkr_b": 18877, "debt_servicing_interest_pkr_b": 9775, "defence_services_pkr_b": 2122, "federal_psdp_development_pkr_b": 1400, "civil_administration_pkr_b": 839, "subsidies_pkr_b": 1363, "pensions_pkr_b": 1014, "fiscal_deficit_share_of_gdp_pct": -5.4, "total_public_debt_pkr_b": 83285, "domestic_debt_pkr_b": 57566, "external_debt_pkr_b": 25720, "source_citation": "PES 2025\u201326 / Budget in Brief / MoF Debt Bulletin"}], "debt": [{"fiscal_year": "FY2017-18", "reference_date": "End-June 2018", "domestic_debt_pkr_b": 16416, "external_debt_pkr_b": 8537, "total_public_debt_pkr_b": 24953, "debt_to_gdp_pct": 72.1, "debt_servicing_markup_pkr_b": 1499, "source_citation": "MoF Public Debt Bulletin / PES 2025-26"}, {"fiscal_year": "FY2018-19", "reference_date": "End-June 2019", "domestic_debt_pkr_b": 20732, "external_debt_pkr_b": 11977, "total_public_debt_pkr_b": 32709, "debt_to_gdp_pct": 86.1, "debt_servicing_markup_pkr_b": 2091, "source_citation": "MoF Public Debt Bulletin / PES 2025-26"}, {"fiscal_year": "FY2019-20", "reference_date": "End-June 2020", "domestic_debt_pkr_b": 23283, "external_debt_pkr_b": 13116, "total_public_debt_pkr_b": 36399, "debt_to_gdp_pct": 76.6, "debt_servicing_markup_pkr_b": 2709, "source_citation": "MoF Public Debt Bulletin / PES 2025-26"}, {"fiscal_year": "FY2020-21", "reference_date": "End-June 2021", "domestic_debt_pkr_b": 26265, "external_debt_pkr_b": 13601, "total_public_debt_pkr_b": 39866, "debt_to_gdp_pct": 71.5, "debt_servicing_markup_pkr_b": 2749, "source_citation": "MoF Public Debt Bulletin / PES 2025-26"}, {"fiscal_year": "FY2021-22", "reference_date": "End-June 2022", "domestic_debt_pkr_b": 31037, "external_debt_pkr_b": 18205, "total_public_debt_pkr_b": 49242, "debt_to_gdp_pct": 73.5, "debt_servicing_markup_pkr_b": 3182, "source_citation": "MoF Public Debt Bulletin / PES 2025-26"}, {"fiscal_year": "FY2022-23", "reference_date": "End-June 2023", "domestic_debt_pkr_b": 38810, "external_debt_pkr_b": 24024, "total_public_debt_pkr_b": 62834, "debt_to_gdp_pct": 74.3, "debt_servicing_markup_pkr_b": 5831, "source_citation": "MoF Public Debt Bulletin / PES 2025-26"}, {"fiscal_year": "FY2023-24", "reference_date": "End-June 2024", "domestic_debt_pkr_b": 47160, "external_debt_pkr_b": 24084, "total_public_debt_pkr_b": 71244, "debt_to_gdp_pct": 67.2, "debt_servicing_markup_pkr_b": 7302, "source_citation": "MoF Public Debt Bulletin / PES 2025-26"}, {"fiscal_year": "FY2024-25", "reference_date": "End-June 2025 (Revised)", "domestic_debt_pkr_b": 53210, "external_debt_pkr_b": 24940, "total_public_debt_pkr_b": 78150, "debt_to_gdp_pct": 66.0, "debt_servicing_markup_pkr_b": 8750, "source_citation": "MoF Public Debt Bulletin / PES 2025-26"}, {"fiscal_year": "FY2025-26", "reference_date": "End-March 2026 (Provisional)", "domestic_debt_pkr_b": 57566, "external_debt_pkr_b": 25720, "total_public_debt_pkr_b": 83285, "debt_to_gdp_pct": 65.6, "debt_servicing_markup_pkr_b": 9775, "source_citation": "MoF Public Debt Bulletin / PES 2025-26"}], "tax_exp": [{"tax_regime": "Sales Tax Exemptions", "statutory_basis": "Sales Tax Act 1990 (Sixth Schedule & SROs)", "revenue_foregone_pkr_b": 1237.11, "share_of_tax_expenditure_pct": 50.81, "share_of_gdp_pct": 1.18, "primary_beneficiary": "Zero-rated inputs, local exemptions, pharma, energy"}, {"tax_regime": "Customs Duty Concessions", "statutory_basis": "Customs Act 1969 (Fifth Schedule & Concessions)", "revenue_foregone_pkr_b": 652.39, "share_of_tax_expenditure_pct": 26.8, "share_of_gdp_pct": 0.62, "primary_beneficiary": "Import tariff concessions, raw materials, automotive SROs"}, {"tax_regime": "Income Tax Deductions & Credits", "statutory_basis": "Income Tax Ordinance 2001 (Second Schedule)", "revenue_foregone_pkr_b": 545.23, "share_of_tax_expenditure_pct": 22.39, "share_of_gdp_pct": 0.52, "primary_beneficiary": "Charitable deductions, IPPs, pensions, special economic zones"}, {"tax_regime": "Total Federal Tax Expenditure", "statutory_basis": "Combined Federal Concessions", "revenue_foregone_pkr_b": 2434.73, "share_of_tax_expenditure_pct": 100.0, "share_of_gdp_pct": 2.32, "primary_beneficiary": "26.18% of total FBR revenue collection (PKR 9,299.1B)"}], "gender_land": [{"geography_id": "PK", "geography_name": "Pakistan", "population_2023": 241499431, "population_male": 124324294, "population_female": 117154947, "population_transgender": 20190, "male_share_pct": 51.48, "female_share_pct": 48.51, "transgender_share_pct": 0.01, "sex_ratio": 106.12, "area_sqkm": 796096.0, "land_area_share_pct": 100.0, "population_share_pct": 100.0, "density_per_sqkm": 303.35, "source_citation": "PBS Digital Census 2023 Table 1"}, {"geography_id": "PK-PB", "geography_name": "Punjab", "population_2023": 127688922, "population_male": 64306472, "population_female": 63371460, "population_transgender": 10990, "male_share_pct": 50.36, "female_share_pct": 49.63, "transgender_share_pct": 0.01, "sex_ratio": 101.48, "area_sqkm": 205345.0, "land_area_share_pct": 25.79, "population_share_pct": 52.87, "density_per_sqkm": 621.83, "source_citation": "PBS Digital Census 2023 Table 1"}, {"geography_id": "PK-SD", "geography_name": "Sindh", "population_2023": 55696147, "population_male": 28849271, "population_female": 26842476, "population_transgender": 4400, "male_share_pct": 51.8, "female_share_pct": 48.19, "transgender_share_pct": 0.01, "sex_ratio": 107.48, "area_sqkm": 140914.0, "land_area_share_pct": 17.7, "population_share_pct": 23.06, "density_per_sqkm": 395.25, "source_citation": "PBS Digital Census 2023 Table 1"}, {"geography_id": "PK-KP", "geography_name": "Khyber Pakhtunkhwa", "population_2023": 40856097, "population_male": 20637458, "population_female": 20215823, "population_transgender": 2816, "male_share_pct": 50.51, "female_share_pct": 49.48, "transgender_share_pct": 0.01, "sex_ratio": 102.09, "area_sqkm": 101741.0, "land_area_share_pct": 12.78, "population_share_pct": 16.92, "density_per_sqkm": 401.57, "source_citation": "PBS Digital Census 2023 Table 1"}, {"geography_id": "PK-BA", "geography_name": "Balochistan", "population_2023": 14894402, "population_male": 7752385, "population_female": 7141180, "population_transgender": 837, "male_share_pct": 52.05, "female_share_pct": 47.95, "transgender_share_pct": 0.01, "sex_ratio": 108.56, "area_sqkm": 347190.0, "land_area_share_pct": 43.61, "population_share_pct": 6.17, "density_per_sqkm": 42.9, "source_citation": "PBS Digital Census 2023 Table 1"}, {"geography_id": "PK-IS", "geography_name": "Islamabad", "population_2023": 2363863, "population_male": 1228891, "population_female": 1134679, "population_transgender": 293, "male_share_pct": 51.99, "female_share_pct": 48.0, "transgender_share_pct": 0.01, "sex_ratio": 108.3, "area_sqkm": 906.0, "land_area_share_pct": 0.11, "population_share_pct": 0.98, "density_per_sqkm": 2609.12, "source_citation": "PBS Digital Census 2023 Table 1"}], "hies": [{"geography_id": "PK", "geography_name": "Pakistan", "domain": "Total", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 62850, "food_expenditure_share_pct": 39.2, "housing_and_utilities_share_pct": 24.6, "education_expenditure_share_pct": 4.2, "health_expenditure_share_pct": 5.8, "other_consumption_share_pct": 26.2, "sample_households_count": 30123, "average_household_size": 6.3}, {"geography_id": "PK", "geography_name": "Pakistan", "domain": "Urban", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 81400, "food_expenditure_share_pct": 34.8, "housing_and_utilities_share_pct": 27.5, "education_expenditure_share_pct": 5.6, "health_expenditure_share_pct": 5.4, "other_consumption_share_pct": 26.7, "sample_households_count": 12450, "average_household_size": 5.9}, {"geography_id": "PK", "geography_name": "Pakistan", "domain": "Rural", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 50600, "food_expenditure_share_pct": 43.5, "housing_and_utilities_share_pct": 21.8, "education_expenditure_share_pct": 3.0, "health_expenditure_share_pct": 6.1, "other_consumption_share_pct": 25.6, "sample_households_count": 17673, "average_household_size": 6.6}, {"geography_id": "PK-PB", "geography_name": "Punjab", "domain": "Total", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 65200, "food_expenditure_share_pct": 38.5, "housing_and_utilities_share_pct": 25.1, "education_expenditure_share_pct": 4.6, "health_expenditure_share_pct": 5.6, "other_consumption_share_pct": 26.2, "sample_households_count": 14210, "average_household_size": 6.1}, {"geography_id": "PK-PB", "geography_name": "Punjab", "domain": "Urban", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 84100, "food_expenditure_share_pct": 34.1, "housing_and_utilities_share_pct": 28.0, "education_expenditure_share_pct": 6.0, "health_expenditure_share_pct": 5.2, "other_consumption_share_pct": 26.7, "sample_households_count": 5890, "average_household_size": 5.8}, {"geography_id": "PK-PB", "geography_name": "Punjab", "domain": "Rural", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 52800, "food_expenditure_share_pct": 42.6, "housing_and_utilities_share_pct": 22.3, "education_expenditure_share_pct": 3.3, "health_expenditure_share_pct": 5.9, "other_consumption_share_pct": 25.9, "sample_households_count": 8320, "average_household_size": 6.4}, {"geography_id": "PK-SD", "geography_name": "Sindh", "domain": "Total", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 64800, "food_expenditure_share_pct": 39.1, "housing_and_utilities_share_pct": 25.8, "education_expenditure_share_pct": 4.1, "health_expenditure_share_pct": 5.5, "other_consumption_share_pct": 25.5, "sample_households_count": 7840, "average_household_size": 6.4}, {"geography_id": "PK-SD", "geography_name": "Sindh", "domain": "Urban", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 82900, "food_expenditure_share_pct": 35.0, "housing_and_utilities_share_pct": 28.2, "education_expenditure_share_pct": 5.4, "health_expenditure_share_pct": 5.3, "other_consumption_share_pct": 26.1, "sample_households_count": 4280, "average_household_size": 6.1}, {"geography_id": "PK-SD", "geography_name": "Sindh", "domain": "Rural", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 47200, "food_expenditure_share_pct": 44.8, "housing_and_utilities_share_pct": 21.0, "education_expenditure_share_pct": 2.4, "health_expenditure_share_pct": 5.8, "other_consumption_share_pct": 26.0, "sample_households_count": 3560, "average_household_size": 6.8}, {"geography_id": "PK-KP", "geography_name": "Khyber Pakhtunkhwa", "domain": "Total", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 58400, "food_expenditure_share_pct": 41.2, "housing_and_utilities_share_pct": 22.9, "education_expenditure_share_pct": 4.0, "health_expenditure_share_pct": 6.3, "other_consumption_share_pct": 25.6, "sample_households_count": 4980, "average_household_size": 7.1}, {"geography_id": "PK-KP", "geography_name": "Khyber Pakhtunkhwa", "domain": "Urban", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 75200, "food_expenditure_share_pct": 36.8, "housing_and_utilities_share_pct": 25.4, "education_expenditure_share_pct": 5.2, "health_expenditure_share_pct": 6.0, "other_consumption_share_pct": 26.6, "sample_households_count": 1420, "average_household_size": 6.7}, {"geography_id": "PK-KP", "geography_name": "Khyber Pakhtunkhwa", "domain": "Rural", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 51900, "food_expenditure_share_pct": 43.1, "housing_and_utilities_share_pct": 21.8, "education_expenditure_share_pct": 3.4, "health_expenditure_share_pct": 6.5, "other_consumption_share_pct": 25.2, "sample_households_count": 3560, "average_household_size": 7.3}, {"geography_id": "PK-BA", "geography_name": "Balochistan", "domain": "Total", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 53100, "food_expenditure_share_pct": 44.6, "housing_and_utilities_share_pct": 21.4, "education_expenditure_share_pct": 2.8, "health_expenditure_share_pct": 6.7, "other_consumption_share_pct": 24.5, "sample_households_count": 3093, "average_household_size": 7.6}, {"geography_id": "PK-BA", "geography_name": "Balochistan", "domain": "Urban", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 69400, "food_expenditure_share_pct": 39.5, "housing_and_utilities_share_pct": 24.5, "education_expenditure_share_pct": 4.1, "health_expenditure_share_pct": 6.2, "other_consumption_share_pct": 25.7, "sample_households_count": 860, "average_household_size": 7.2}, {"geography_id": "PK-BA", "geography_name": "Balochistan", "domain": "Rural", "reference_period": "HIES 2024\u201325", "average_monthly_household_consumption_pkr": 46500, "food_expenditure_share_pct": 46.8, "housing_and_utilities_share_pct": 20.0, "education_expenditure_share_pct": 2.1, "health_expenditure_share_pct": 7.0, "other_consumption_share_pct": 24.1, "sample_households_count": 2233, "average_household_size": 7.8}], "consumption": [{"geography_id": "PK", "geography_name": "Pakistan", "mean_monthly_expenditure_pkr": 62850, "food_pct": 39.2, "housing_utilities_pct": 24.6, "health_pct": 5.8, "education_pct": 4.2, "transport_comm_pct": 11.4, "clothing_other_pct": 14.8}, {"geography_id": "PK-PB", "geography_name": "Punjab", "mean_monthly_expenditure_pkr": 65200, "food_pct": 38.5, "housing_utilities_pct": 25.1, "health_pct": 5.6, "education_pct": 4.6, "transport_comm_pct": 11.6, "clothing_other_pct": 14.6}, {"geography_id": "PK-SD", "geography_name": "Sindh", "mean_monthly_expenditure_pkr": 64800, "food_pct": 39.1, "housing_utilities_pct": 25.8, "health_pct": 5.5, "education_pct": 4.1, "transport_comm_pct": 11.2, "clothing_other_pct": 14.3}, {"geography_id": "PK-KP", "geography_name": "Khyber Pakhtunkhwa", "mean_monthly_expenditure_pkr": 58400, "food_pct": 41.2, "housing_utilities_pct": 22.9, "health_pct": 6.3, "education_pct": 4.0, "transport_comm_pct": 10.8, "clothing_other_pct": 14.8}, {"geography_id": "PK-BA", "geography_name": "Balochistan", "mean_monthly_expenditure_pkr": 53100, "food_pct": 44.6, "housing_utilities_pct": 21.4, "health_pct": 6.7, "education_pct": 2.8, "transport_comm_pct": 9.8, "clothing_other_pct": 14.7}], "wage_infl": [{"year": 2020, "cpi_index_base2016": 133.8, "cpi_inflation_annual_pct": 10.7, "cumulative_inflation_pct": 0.0, "avg_monthly_wage_pkr": 25250, "cumulative_wage_growth_pct": 0.0, "real_wage_index": 100.0}, {"year": 2021, "cpi_index_base2016": 145.7, "cpi_inflation_annual_pct": 8.9, "cumulative_inflation_pct": 8.9, "avg_monthly_wage_pkr": 27400, "cumulative_wage_growth_pct": 8.5, "real_wage_index": 99.6}, {"year": 2022, "cpi_index_base2016": 163.4, "cpi_inflation_annual_pct": 12.2, "cumulative_inflation_pct": 22.1, "avg_monthly_wage_pkr": 30200, "cumulative_wage_growth_pct": 19.6, "real_wage_index": 97.9}, {"year": 2023, "cpi_index_base2016": 213.7, "cpi_inflation_annual_pct": 30.8, "cumulative_inflation_pct": 59.7, "avg_monthly_wage_pkr": 34800, "cumulative_wage_growth_pct": 37.8, "real_wage_index": 86.3}, {"year": 2024, "cpi_index_base2016": 252.2, "cpi_inflation_annual_pct": 18.0, "cumulative_inflation_pct": 88.4, "avg_monthly_wage_pkr": 39042, "cumulative_wage_growth_pct": 54.6, "real_wage_index": 82.1}], "services": [{"geography_id": "PK", "geography_name": "Pakistan", "electricity_access_pct": 94.2, "piped_water_inside_pct": 28.5, "underground_sewerage_toilet_pct": 71.2, "clean_cooking_fuel_pct": 42.1, "solid_biomass_firewood_pct": 57.9, "sample_households": 30123}, {"geography_id": "PK-PB", "geography_name": "Punjab", "electricity_access_pct": 98.4, "piped_water_inside_pct": 24.2, "underground_sewerage_toilet_pct": 78.5, "clean_cooking_fuel_pct": 46.8, "solid_biomass_firewood_pct": 53.2, "sample_households": 14210}, {"geography_id": "PK-SD", "geography_name": "Sindh", "electricity_access_pct": 93.1, "piped_water_inside_pct": 42.6, "underground_sewerage_toilet_pct": 74.2, "clean_cooking_fuel_pct": 48.5, "solid_biomass_firewood_pct": 51.5, "sample_households": 7840}, {"geography_id": "PK-KP", "geography_name": "Khyber Pakhtunkhwa", "electricity_access_pct": 92.4, "piped_water_inside_pct": 26.8, "underground_sewerage_toilet_pct": 65.4, "clean_cooking_fuel_pct": 28.6, "solid_biomass_firewood_pct": 71.4, "sample_households": 4980}, {"geography_id": "PK-BA", "geography_name": "Balochistan", "electricity_access_pct": 74.8, "piped_water_inside_pct": 19.4, "underground_sewerage_toilet_pct": 41.2, "clean_cooking_fuel_pct": 18.2, "solid_biomass_firewood_pct": 81.8, "sample_households": 3093}], "lfs": [{"geography_id": "PK", "geography_name": "Pakistan", "reference_period": "Labour Force Survey 2024\u201325", "labour_force_participation_rate_total": 46.3, "labour_force_participation_rate_male": 68.4, "labour_force_participation_rate_female": 23.1, "unemployment_rate_total": 7.1, "unemployment_rate_male": 6.2, "unemployment_rate_female": 9.8, "youth_unemployment_rate_15_24": 12.2, "employment_share_agriculture": 36.8, "employment_share_industry": 24.4, "employment_share_services": 38.8, "average_monthly_wage_pkr": 39042, "informal_employment_rate": 72.8, "sample_observations_count": 325445}, {"geography_id": "PK-PB", "geography_name": "Punjab", "reference_period": "Labour Force Survey 2024\u201325", "labour_force_participation_rate_total": 48.2, "labour_force_participation_rate_male": 69.1, "labour_force_participation_rate_female": 26.5, "unemployment_rate_total": 6.8, "unemployment_rate_male": 5.9, "unemployment_rate_female": 9.1, "youth_unemployment_rate_15_24": 11.5, "employment_share_agriculture": 38.2, "employment_share_industry": 25.1, "employment_share_services": 36.7, "average_monthly_wage_pkr": 40500, "informal_employment_rate": 71.4, "sample_observations_count": 164280}, {"geography_id": "PK-SD", "geography_name": "Sindh", "reference_period": "Labour Force Survey 2024\u201325", "labour_force_participation_rate_total": 46.0, "labour_force_participation_rate_male": 68.8, "labour_force_participation_rate_female": 21.2, "unemployment_rate_total": 6.5, "unemployment_rate_male": 5.8, "unemployment_rate_female": 8.9, "youth_unemployment_rate_15_24": 11.0, "employment_share_agriculture": 34.6, "employment_share_industry": 24.0, "employment_share_services": 41.4, "average_monthly_wage_pkr": 39800, "informal_employment_rate": 73.6, "sample_observations_count": 81120}, {"geography_id": "PK-KP", "geography_name": "Khyber Pakhtunkhwa", "reference_period": "Labour Force Survey 2024\u201325", "labour_force_participation_rate_total": 41.5, "labour_force_participation_rate_male": 65.7, "labour_force_participation_rate_female": 16.8, "unemployment_rate_total": 8.8, "unemployment_rate_male": 7.6, "unemployment_rate_female": 13.4, "youth_unemployment_rate_15_24": 15.3, "employment_share_agriculture": 36.1, "employment_share_industry": 23.2, "employment_share_services": 40.7, "average_monthly_wage_pkr": 36200, "informal_employment_rate": 75.8, "sample_observations_count": 52310}, {"geography_id": "PK-BA", "geography_name": "Balochistan", "reference_period": "Labour Force Survey 2024\u201325", "labour_force_participation_rate_total": 43.8, "labour_force_participation_rate_male": 67.2, "labour_force_participation_rate_female": 17.5, "unemployment_rate_total": 7.9, "unemployment_rate_male": 7.1, "unemployment_rate_female": 11.2, "youth_unemployment_rate_15_24": 13.8, "employment_share_agriculture": 41.5, "employment_share_industry": 21.0, "employment_share_services": 37.5, "average_monthly_wage_pkr": 34800, "informal_employment_rate": 78.2, "sample_observations_count": 27735}], "census_shifts": [{"census_year": 1981, "punjab_pop_m": 47.29, "punjab_share_pct": 56.13, "sindh_pop_m": 19.03, "sindh_share_pct": 22.59, "kp_pop_m": 13.25, "kp_share_pct": 15.73, "balochistan_pop_m": 4.33, "balochistan_share_pct": 5.14, "ict_pop_m": 0.34, "ict_share_pct": 0.4, "total_pakistan_pop_m": 84.25}, {"census_year": 1998, "punjab_pop_m": 73.62, "punjab_share_pct": 55.63, "sindh_pop_m": 30.44, "sindh_share_pct": 23.0, "kp_pop_m": 20.96, "kp_share_pct": 15.84, "balochistan_pop_m": 6.57, "balochistan_share_pct": 4.96, "ict_pop_m": 0.81, "ict_share_pct": 0.61, "total_pakistan_pop_m": 132.35}, {"census_year": 2017, "punjab_pop_m": 110.01, "punjab_share_pct": 52.97, "sindh_pop_m": 47.89, "sindh_share_pct": 23.06, "kp_pop_m": 35.53, "kp_share_pct": 17.11, "balochistan_pop_m": 12.34, "balochistan_share_pct": 5.94, "ict_pop_m": 2.01, "ict_share_pct": 0.97, "total_pakistan_pop_m": 207.68}, {"census_year": 2023, "punjab_pop_m": 127.69, "punjab_share_pct": 52.87, "sindh_pop_m": 55.7, "sindh_share_pct": 23.06, "kp_pop_m": 40.86, "kp_share_pct": 16.92, "balochistan_pop_m": 14.89, "balochistan_share_pct": 6.17, "ict_pop_m": 2.36, "ict_share_pct": 0.98, "total_pakistan_pop_m": 241.5}], "districts": [{"geography_id": "PK-PB-D-ATTOCK", "district_name": "Attock", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 6857.0, "population_2023": 2170423, "population_male": 1089655, "population_female": 1080687, "population_transgender": 81, "population_rural": 1546439, "population_urban": 623984, "urban_proportion_pct": 28.75, "sex_ratio": 100.83, "density_per_sqkm": 316.53, "avg_household_size": 6.1, "household_count_estimated": 355807, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-BAHAWALNAGAR", "district_name": "Bahawalnagar", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 8878.0, "population_2023": 3550342, "population_male": 1845493, "population_female": 1704479, "population_transgender": 370, "population_rural": 2576224, "population_urban": 974118, "urban_proportion_pct": 27.44, "sex_ratio": 108.27, "density_per_sqkm": 399.9, "avg_household_size": 6.3, "household_count_estimated": 563546, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-BAHAWALPUR", "district_name": "Bahawalpur", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 24830.0, "population_2023": 4284964, "population_male": 2174995, "population_female": 2109500, "population_transgender": 469, "population_rural": 2665643, "population_urban": 1619321, "urban_proportion_pct": 37.79, "sex_ratio": 103.1, "density_per_sqkm": 172.57, "avg_household_size": 6.3, "household_count_estimated": 680153, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-BHAKKAR", "district_name": "Bhakkar", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 8153.0, "population_2023": 1957470, "population_male": 1016361, "population_female": 941032, "population_transgender": 77, "population_rural": 1605036, "population_urban": 352434, "urban_proportion_pct": 18.0, "sex_ratio": 108.0, "density_per_sqkm": 240.09, "avg_household_size": 6.2, "household_count_estimated": 315720, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-CHAKWAL", "district_name": "Chakwal", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 6525.0, "population_2023": 1734854, "population_male": 864029, "population_female": 870736, "population_transgender": 89, "population_rural": 1300049, "population_urban": 434805, "urban_proportion_pct": 25.06, "sex_ratio": 99.23, "density_per_sqkm": 265.88, "avg_household_size": 6.0, "household_count_estimated": 289142, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-CHINIOT", "district_name": "Chiniot", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 2643.0, "population_2023": 1563024, "population_male": 790731, "population_female": 772126, "population_transgender": 167, "population_rural": 1071352, "population_urban": 491672, "urban_proportion_pct": 31.46, "sex_ratio": 102.41, "density_per_sqkm": 591.38, "avg_household_size": 6.0, "household_count_estimated": 260504, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-DERA-GHAZI-KHAN", "district_name": "Dera Ghazi Khan", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 11922.0, "population_2023": 3393705, "population_male": 1712930, "population_female": 1680654, "population_transgender": 121, "population_rural": 2586293, "population_urban": 807412, "urban_proportion_pct": 23.79, "sex_ratio": 101.92, "density_per_sqkm": 284.66, "avg_household_size": 7.4, "household_count_estimated": 458608, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-FAISALABAD", "district_name": "Faisalabad", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 5857.0, "population_2023": 9075819, "population_male": 4731224, "population_female": 4343633, "population_transgender": 962, "population_rural": 4682840, "population_urban": 4392979, "urban_proportion_pct": 48.4, "sex_ratio": 108.92, "density_per_sqkm": 1549.57, "avg_household_size": 6.5, "household_count_estimated": 1396279, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-GUJRANWALA", "district_name": "Gujranwala", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 3622.0, "population_2023": 5959750, "population_male": 3028290, "population_female": 2930923, "population_transgender": 537, "population_rural": 2365779, "population_urban": 3593971, "urban_proportion_pct": 60.3, "sex_ratio": 103.32, "density_per_sqkm": 1645.43, "avg_household_size": 7.0, "household_count_estimated": 851392, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-GUJRAT", "district_name": "Gujrat", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 3192.0, "population_2023": 3219375, "population_male": 1608221, "population_female": 1610964, "population_transgender": 190, "population_rural": 1895111, "population_urban": 1324264, "urban_proportion_pct": 41.13, "sex_ratio": 99.83, "density_per_sqkm": 1008.58, "avg_household_size": 6.5, "household_count_estimated": 495288, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-HAFIZABAD", "district_name": "Hafizabad", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 2367.0, "population_2023": 1319909, "population_male": 670023, "population_female": 649826, "population_transgender": 60, "population_rural": 815529, "population_urban": 504380, "urban_proportion_pct": 38.21, "sex_ratio": 103.11, "density_per_sqkm": 557.63, "avg_household_size": 6.6, "household_count_estimated": 199986, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-JHANG", "district_name": "Jhang", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 6166.0, "population_2023": 3065639, "population_male": 1585616, "population_female": 1479771, "population_transgender": 252, "population_rural": 2264713, "population_urban": 800926, "urban_proportion_pct": 26.13, "sex_ratio": 107.15, "density_per_sqkm": 497.18, "avg_household_size": 6.2, "household_count_estimated": 494457, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-JHELUM", "district_name": "Jhelum", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 3587.0, "population_2023": 1382308, "population_male": 703667, "population_female": 678543, "population_transgender": 98, "population_rural": 840990, "population_urban": 541318, "urban_proportion_pct": 39.16, "sex_ratio": 103.7, "density_per_sqkm": 385.37, "avg_household_size": 6.0, "household_count_estimated": 230384, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-KASUR", "district_name": "Kasur", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 3995.0, "population_2023": 4084286, "population_male": 2087217, "population_female": 1996670, "population_transgender": 399, "population_rural": 2840404, "population_urban": 1243882, "urban_proportion_pct": 30.46, "sex_ratio": 104.53, "density_per_sqkm": 1022.35, "avg_household_size": 6.3, "household_count_estimated": 648299, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-KHANEWAL", "district_name": "Khanewal", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 4349.0, "population_2023": 3364077, "population_male": 1734655, "population_female": 1629036, "population_transgender": 386, "population_rural": 2647291, "population_urban": 716786, "urban_proportion_pct": 21.31, "sex_ratio": 106.48, "density_per_sqkm": 773.53, "avg_household_size": 6.3, "household_count_estimated": 533980, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-KHUSHAB", "district_name": "Khushab", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 6511.0, "population_2023": 1501089, "population_male": 768126, "population_female": 732914, "population_transgender": 49, "population_rural": 1082344, "population_urban": 418745, "urban_proportion_pct": 27.9, "sex_ratio": 104.8, "density_per_sqkm": 230.55, "avg_household_size": 6.0, "household_count_estimated": 250181, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-LAHORE", "district_name": "Lahore", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 1772.0, "population_2023": 13004135, "population_male": 6881801, "population_female": 6118958, "population_transgender": 3376, "population_rural": 0, "population_urban": 13004135, "urban_proportion_pct": 100.0, "sex_ratio": 112.47, "density_per_sqkm": 7338.68, "avg_household_size": 6.4, "household_count_estimated": 2031896, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-LAYYAH", "district_name": "Layyah", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 6289.0, "population_2023": 2102386, "population_male": 1082922, "population_female": 1019375, "population_transgender": 89, "population_rural": 1716104, "population_urban": 386282, "urban_proportion_pct": 18.37, "sex_ratio": 106.23, "density_per_sqkm": 334.3, "avg_household_size": 6.1, "household_count_estimated": 344653, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-LODHRAN", "district_name": "Lodhran", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 2778.0, "population_2023": 1928299, "population_male": 997846, "population_female": 930336, "population_transgender": 117, "population_rural": 1603246, "population_urban": 325053, "urban_proportion_pct": 16.86, "sex_ratio": 107.26, "density_per_sqkm": 694.13, "avg_household_size": 5.9, "household_count_estimated": 326830, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-MANDI-BAHAUDDIN", "district_name": "Mandi Bahauddin", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 2673.0, "population_2023": 1829486, "population_male": 917125, "population_female": 912222, "population_transgender": 139, "population_rural": 1483345, "population_urban": 346141, "urban_proportion_pct": 18.92, "sex_ratio": 100.54, "density_per_sqkm": 684.43, "avg_household_size": 6.3, "household_count_estimated": 290394, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-MIANWALI", "district_name": "Mianwali", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 5840.0, "population_2023": 1798268, "population_male": 918115, "population_female": 880088, "population_transgender": 65, "population_rural": 1434815, "population_urban": 363453, "urban_proportion_pct": 20.21, "sex_ratio": 104.32, "density_per_sqkm": 307.92, "avg_household_size": 6.0, "household_count_estimated": 299711, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-MULTAN", "district_name": "Multan", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 3720.0, "population_2023": 5362305, "population_male": 2730613, "population_female": 2631285, "population_transgender": 407, "population_rural": 2862434, "population_urban": 2499871, "urban_proportion_pct": 46.62, "sex_ratio": 103.77, "density_per_sqkm": 1441.48, "avg_household_size": 6.0, "household_count_estimated": 893717, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-MUZAFFARGARH", "district_name": "Muzaffargarh", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 8249.0, "population_2023": 5015325, "population_male": 2546877, "population_female": 2468339, "population_transgender": 109, "population_rural": 4068531, "population_urban": 946794, "urban_proportion_pct": 18.88, "sex_ratio": 103.18, "density_per_sqkm": 607.99, "avg_household_size": 6.2, "household_count_estimated": 808923, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-NANKANA-SAHIB", "district_name": "Nankana Sahib", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 2216.0, "population_2023": 1634871, "population_male": 831931, "population_female": 802859, "population_transgender": 81, "population_rural": 1311483, "population_urban": 323388, "urban_proportion_pct": 19.78, "sex_ratio": 103.62, "density_per_sqkm": 737.76, "avg_household_size": 6.6, "household_count_estimated": 247707, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-NAROWAL", "district_name": "Narowal", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 2337.0, "population_2023": 1950954, "population_male": 996445, "population_female": 954424, "population_transgender": 85, "population_rural": 1601859, "population_urban": 349095, "urban_proportion_pct": 17.89, "sex_ratio": 104.4, "density_per_sqkm": 834.81, "avg_household_size": 6.9, "household_count_estimated": 282746, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-OKARA", "district_name": "Okara", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 4377.0, "population_2023": 3515490, "population_male": 1789744, "population_female": 1725411, "population_transgender": 335, "population_rural": 2327986, "population_urban": 1187504, "urban_proportion_pct": 33.78, "sex_ratio": 103.73, "density_per_sqkm": 803.17, "avg_household_size": 6.3, "household_count_estimated": 558014, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-PAKPATTAN", "district_name": "Pakpattan", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 2724.0, "population_2023": 2136170, "population_male": 1085316, "population_female": 1050694, "population_transgender": 160, "population_rural": 1663595, "population_urban": 472575, "urban_proportion_pct": 22.12, "sex_ratio": 103.3, "density_per_sqkm": 784.2, "avg_household_size": 6.1, "household_count_estimated": 350191, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-RAHIM-YAR-KHAN", "district_name": "Rahim Yar Khan", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 11880.0, "population_2023": 5564703, "population_male": 2896819, "population_female": 2667333, "population_transgender": 551, "population_rural": 4222451, "population_urban": 1342252, "urban_proportion_pct": 24.12, "sex_ratio": 108.6, "density_per_sqkm": 468.41, "avg_household_size": 6.7, "household_count_estimated": 830552, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-RAJANPUR", "district_name": "Rajanpur", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 12318.0, "population_2023": 2381049, "population_male": 1209183, "population_female": 1171748, "population_transgender": 118, "population_rural": 1749826, "population_urban": 631223, "urban_proportion_pct": 26.51, "sex_ratio": 103.19, "density_per_sqkm": 193.3, "avg_household_size": 6.7, "household_count_estimated": 355380, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-RAWALPINDI", "district_name": "Rawalpindi", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 5285.0, "population_2023": 6118911, "population_male": 3109807, "population_female": 3007760, "population_transgender": 1344, "population_rural": 1908126, "population_urban": 4210785, "urban_proportion_pct": 68.82, "sex_ratio": 103.39, "density_per_sqkm": 1157.79, "avg_household_size": 6.1, "household_count_estimated": 1003100, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-SAHIWAL", "district_name": "Sahiwal", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 3201.0, "population_2023": 2881811, "population_male": 1460748, "population_female": 1420910, "population_transgender": 153, "population_rural": 2124180, "population_urban": 757631, "urban_proportion_pct": 26.29, "sex_ratio": 102.8, "density_per_sqkm": 900.28, "avg_household_size": 6.4, "household_count_estimated": 450282, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-SARGODHA", "district_name": "Sargodha", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 5856.0, "population_2023": 4334448, "population_male": 2194156, "population_female": 2139911, "population_transgender": 381, "population_rural": 2724861, "population_urban": 1609587, "urban_proportion_pct": 37.13, "sex_ratio": 102.53, "density_per_sqkm": 740.17, "avg_household_size": 6.3, "household_count_estimated": 688007, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-SHEIKHUPURA", "district_name": "Sheikhupura", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 3744.0, "population_2023": 4049418, "population_male": 2079378, "population_female": 1969434, "population_transgender": 606, "population_rural": 2498625, "population_urban": 1550793, "urban_proportion_pct": 38.3, "sex_ratio": 105.58, "density_per_sqkm": 1081.58, "avg_household_size": 6.8, "household_count_estimated": 595502, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-SIALKOT", "district_name": "Sialkot", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 3016.0, "population_2023": 4499394, "population_male": 2277939, "population_female": 2220596, "population_transgender": 859, "population_rural": 3017426, "population_urban": 1481968, "urban_proportion_pct": 32.94, "sex_ratio": 102.58, "density_per_sqkm": 1491.84, "avg_household_size": 6.7, "household_count_estimated": 671551, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-TOBA-TEK-SINGH", "district_name": "Toba Tek Singh", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 3252.0, "population_2023": 2524044, "population_male": 1295646, "population_female": 1228162, "population_transgender": 236, "population_rural": 1960519, "population_urban": 563525, "urban_proportion_pct": 22.33, "sex_ratio": 105.49, "density_per_sqkm": 776.15, "avg_household_size": 6.4, "household_count_estimated": 394381, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB-D-VEHARI", "district_name": "Vehari", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 4364.0, "population_2023": 3430421, "population_male": 1734732, "population_female": 1695250, "population_transgender": 439, "population_rural": 2647506, "population_urban": 782915, "urban_proportion_pct": 22.82, "sex_ratio": 102.33, "density_per_sqkm": 786.07, "avg_household_size": 6.3, "household_count_estimated": 544511, "source_file": "table_1_punjab_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-BADIN", "district_name": "Badin", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 6858.0, "population_2023": 1947081, "population_male": 1012854, "population_female": 934153, "population_transgender": 74, "population_rural": 1517232, "population_urban": 429849, "urban_proportion_pct": 22.08, "sex_ratio": 108.42, "density_per_sqkm": 283.91, "avg_household_size": 4.8, "household_count_estimated": 405641, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-DADU", "district_name": "Dadu", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 7866.0, "population_2023": 1742320, "population_male": 883793, "population_female": 858441, "population_transgender": 86, "population_rural": 1303286, "population_urban": 439034, "urban_proportion_pct": 25.2, "sex_ratio": 102.95, "density_per_sqkm": 221.5, "avg_household_size": 5.1, "household_count_estimated": 341631, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-GHOTKI", "district_name": "Ghotki", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 6083.0, "population_2023": 1772609, "population_male": 920328, "population_female": 852234, "population_transgender": 47, "population_rural": 1393227, "population_urban": 379382, "urban_proportion_pct": 21.4, "sex_ratio": 107.99, "density_per_sqkm": 291.4, "avg_household_size": 5.3, "household_count_estimated": 334454, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-HYDERABAD", "district_name": "Hyderabad", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 993.0, "population_2023": 2432540, "population_male": 1289279, "population_female": 1143090, "population_transgender": 171, "population_rural": 410161, "population_urban": 2022379, "urban_proportion_pct": 83.14, "sex_ratio": 112.79, "density_per_sqkm": 2449.69, "avg_household_size": 5.4, "household_count_estimated": 450470, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-JACOBABAD", "district_name": "Jacobabad", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 2698.0, "population_2023": 1174097, "population_male": 595787, "population_female": 578201, "population_transgender": 109, "population_rural": 812180, "population_urban": 361917, "urban_proportion_pct": 30.83, "sex_ratio": 103.04, "density_per_sqkm": 435.17, "avg_household_size": 6.0, "household_count_estimated": 195682, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-JAMSHORO", "district_name": "Jamshoro", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 11204.0, "population_2023": 1117308, "population_male": 578036, "population_female": 539205, "population_transgender": 67, "population_rural": 595562, "population_urban": 521746, "urban_proportion_pct": 46.7, "sex_ratio": 107.2, "density_per_sqkm": 99.72, "avg_household_size": 5.2, "household_count_estimated": 214866, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-KAMBAR-SHAHDAD-KOT", "district_name": "Kambar Shahdad Kot", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 5475.0, "population_2023": 1514869, "population_male": 791116, "population_female": 723710, "population_transgender": 43, "population_rural": 1093004, "population_urban": 421865, "urban_proportion_pct": 27.85, "sex_ratio": 109.31, "density_per_sqkm": 276.69, "avg_household_size": 5.6, "household_count_estimated": 270512, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-KARACHI-CENTRAL", "district_name": "Karachi Central", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 69.0, "population_2023": 3822325, "population_male": 2019115, "population_female": 1802647, "population_transgender": 563, "population_rural": 0, "population_urban": 3822325, "urban_proportion_pct": 100.0, "sex_ratio": 112.01, "density_per_sqkm": 55396.01, "avg_household_size": 5.8, "household_count_estimated": 659021, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-KARACHI-EAST", "district_name": "Karachi East", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 139.0, "population_2023": 3921742, "population_male": 2084719, "population_female": 1836597, "population_transgender": 426, "population_rural": 0, "population_urban": 3921742, "urban_proportion_pct": 100.0, "sex_ratio": 113.51, "density_per_sqkm": 28213.97, "avg_household_size": 5.9, "household_count_estimated": 664702, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-KARACHI-SOUTH", "district_name": "Karachi South", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 122.0, "population_2023": 2329764, "population_male": 1240860, "population_female": 1088520, "population_transgender": 384, "population_rural": 0, "population_urban": 2329764, "urban_proportion_pct": 100.0, "sex_ratio": 114.0, "density_per_sqkm": 19096.43, "avg_household_size": 5.4, "household_count_estimated": 431437, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-KARACHI-WEST", "district_name": "Karachi West", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 370.0, "population_2023": 2679380, "population_male": 1415431, "population_female": 1263752, "population_transgender": 197, "population_rural": 248952, "population_urban": 2430428, "urban_proportion_pct": 90.71, "sex_ratio": 112.0, "density_per_sqkm": 7241.57, "avg_household_size": 5.7, "household_count_estimated": 470066, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-KASHMORE", "district_name": "Kashmore", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 2580.0, "population_2023": 1233957, "population_male": 628265, "population_female": 605646, "population_transgender": 46, "population_rural": 962175, "population_urban": 271782, "urban_proportion_pct": 22.03, "sex_ratio": 103.73, "density_per_sqkm": 478.28, "avg_household_size": 5.9, "household_count_estimated": 209145, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-KEAMARI", "district_name": "Keamari", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 559.0, "population_2023": 2068451, "population_male": 1100626, "population_female": 967613, "population_transgender": 212, "population_rural": 0, "population_urban": 2068451, "urban_proportion_pct": 100.0, "sex_ratio": 113.75, "density_per_sqkm": 3700.27, "avg_household_size": 6.4, "household_count_estimated": 323195, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-KHAIRPUR", "district_name": "Khairpur", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 15910.0, "population_2023": 2597535, "population_male": 1315925, "population_female": 1281472, "population_transgender": 138, "population_rural": 1753272, "population_urban": 844263, "urban_proportion_pct": 32.5, "sex_ratio": 102.69, "density_per_sqkm": 163.26, "avg_household_size": 5.7, "household_count_estimated": 455707, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-KORANGI", "district_name": "Korangi", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 108.0, "population_2023": 3128971, "population_male": 1650172, "population_female": 1478133, "population_transgender": 666, "population_rural": 0, "population_urban": 3128971, "urban_proportion_pct": 100.0, "sex_ratio": 111.64, "density_per_sqkm": 28971.95, "avg_household_size": 6.3, "household_count_estimated": 496662, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-LARKANA", "district_name": "Larkana", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 1948.0, "population_2023": 1784453, "population_male": 932604, "population_female": 851732, "population_transgender": 117, "population_rural": 986302, "population_urban": 798151, "urban_proportion_pct": 44.73, "sex_ratio": 109.5, "density_per_sqkm": 916.04, "avg_household_size": 5.5, "household_count_estimated": 324446, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-MALIR", "district_name": "Malir", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 2160.0, "population_2023": 2432248, "population_male": 1288599, "population_female": 1143424, "population_transgender": 225, "population_rural": 1265908, "population_urban": 1166340, "urban_proportion_pct": 47.95, "sex_ratio": 112.7, "density_per_sqkm": 1126.04, "avg_household_size": 5.7, "household_count_estimated": 426710, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-MATIARI", "district_name": "Matiari", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 1417.0, "population_2023": 849383, "population_male": 430096, "population_female": 419262, "population_transgender": 25, "population_rural": 646710, "population_urban": 202673, "urban_proportion_pct": 23.86, "sex_ratio": 102.58, "density_per_sqkm": 599.42, "avg_household_size": 5.3, "household_count_estimated": 160260, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-MIRPUR-KHAS", "district_name": "Mirpur Khas", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 2925.0, "population_2023": 1681386, "population_male": 882057, "population_female": 799250, "population_transgender": 79, "population_rural": 1189211, "population_urban": 492175, "urban_proportion_pct": 29.27, "sex_ratio": 110.36, "density_per_sqkm": 574.83, "avg_household_size": 5.3, "household_count_estimated": 317242, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-NAUSHAHRO-FEROZE", "district_name": "Naushahro Feroze", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 2946.0, "population_2023": 1777082, "population_male": 901622, "population_female": 875385, "population_transgender": 75, "population_rural": 1269838, "population_urban": 507244, "urban_proportion_pct": 28.54, "sex_ratio": 103.0, "density_per_sqkm": 603.22, "avg_household_size": 5.5, "household_count_estimated": 323105, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-SANGHAR", "district_name": "Sanghar", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 10728.0, "population_2023": 2308465, "population_male": 1172607, "population_female": 1135748, "population_transgender": 110, "population_rural": 1677683, "population_urban": 630782, "urban_proportion_pct": 27.32, "sex_ratio": 103.25, "density_per_sqkm": 215.18, "avg_household_size": 5.6, "household_count_estimated": 412225, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-SHAHEED-BENAZIRABAD", "district_name": "Shaheed Benazirabad", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 4502.0, "population_2023": 1845102, "population_male": 936953, "population_female": 908082, "population_transgender": 67, "population_rural": 1246982, "population_urban": 598120, "urban_proportion_pct": 32.42, "sex_ratio": 103.18, "density_per_sqkm": 409.84, "avg_household_size": 5.5, "household_count_estimated": 335473, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-SHIKARPUR", "district_name": "Shikarpur", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 2512.0, "population_2023": 1386330, "population_male": 700698, "population_female": 685587, "population_transgender": 45, "population_rural": 1067592, "population_urban": 318738, "urban_proportion_pct": 22.99, "sex_ratio": 102.2, "density_per_sqkm": 551.88, "avg_household_size": 6.4, "household_count_estimated": 216614, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-SUJAWAL", "district_name": "Sujawal", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 8785.0, "population_2023": 839292, "population_male": 437151, "population_female": 402109, "population_transgender": 32, "population_rural": 750445, "population_urban": 88847, "urban_proportion_pct": 10.59, "sex_ratio": 108.71, "density_per_sqkm": 95.54, "avg_household_size": 5.2, "household_count_estimated": 161402, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-SUKKUR", "district_name": "Sukkur", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 5165.0, "population_2023": 1639897, "population_male": 870094, "population_female": 769729, "population_transgender": 74, "population_rural": 824898, "population_urban": 814999, "urban_proportion_pct": 49.7, "sex_ratio": 113.04, "density_per_sqkm": 317.5, "avg_household_size": 6.1, "household_count_estimated": 268835, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-TANDO-ALLAHYAR", "district_name": "Tando Allahyar", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 1554.0, "population_2023": 922012, "population_male": 468504, "population_female": 453487, "population_transgender": 21, "population_rural": 636325, "population_urban": 285687, "urban_proportion_pct": 30.99, "sex_ratio": 103.31, "density_per_sqkm": 593.32, "avg_household_size": 5.1, "household_count_estimated": 180786, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-TANDO-MUHAMMAD-KHAN", "district_name": "Tando Muhammad Khan", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 1423.0, "population_2023": 726119, "population_male": 376736, "population_female": 349362, "population_transgender": 21, "population_rural": 563977, "population_urban": 162142, "urban_proportion_pct": 22.33, "sex_ratio": 107.84, "density_per_sqkm": 510.27, "avg_household_size": 5.0, "household_count_estimated": 145223, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-THARPARKAR", "district_name": "Tharparkar", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 19637.0, "population_2023": 1778407, "population_male": 928333, "population_female": 850041, "population_transgender": 33, "population_rural": 1634002, "population_urban": 144405, "urban_proportion_pct": 8.12, "sex_ratio": 109.21, "density_per_sqkm": 90.56, "avg_household_size": 5.4, "household_count_estimated": 329334, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-THATTA", "district_name": "Thatta", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 8570.0, "population_2023": 1083191, "population_male": 555252, "population_female": 527895, "population_transgender": 44, "population_rural": 889512, "population_urban": 193679, "urban_proportion_pct": 17.88, "sex_ratio": 105.18, "density_per_sqkm": 126.39, "avg_household_size": 5.2, "household_count_estimated": 208305, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD-D-UMERKOT", "district_name": "Umerkot", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 5608.0, "population_2023": 1159831, "population_male": 606812, "population_female": 552994, "population_transgender": 25, "population_rural": 900972, "population_urban": 258859, "urban_proportion_pct": 22.32, "sex_ratio": 109.73, "density_per_sqkm": 206.82, "avg_household_size": 5.2, "household_count_estimated": 223044, "source_file": "table_1_sindh_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-ABBOTTABAD", "district_name": "Abbottabad", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1967.0, "population_2023": 1419072, "population_male": 712218, "population_female": 706750, "population_transgender": 104, "population_rural": 1086757, "population_urban": 332315, "urban_proportion_pct": 23.42, "sex_ratio": 100.77, "density_per_sqkm": 721.44, "avg_household_size": 5.9, "household_count_estimated": 240520, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-BAJAUR", "district_name": "Bajaur", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1290.0, "population_2023": 1287960, "population_male": 650798, "population_female": 637147, "population_transgender": 15, "population_rural": 1287960, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 102.14, "density_per_sqkm": 998.42, "avg_household_size": 7.0, "household_count_estimated": 183994, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-BANNU", "district_name": "Bannu", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1972.0, "population_2023": 1357890, "population_male": 706094, "population_female": 651777, "population_transgender": 19, "population_rural": 1309492, "population_urban": 48398, "urban_proportion_pct": 3.56, "sex_ratio": 108.33, "density_per_sqkm": 688.59, "avg_household_size": 7.4, "household_count_estimated": 183498, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-BATAGRAM", "district_name": "Batagram", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1301.0, "population_2023": 554133, "population_male": 281298, "population_female": 272825, "population_transgender": 10, "population_rural": 554133, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 103.11, "density_per_sqkm": 425.93, "avg_household_size": 6.4, "household_count_estimated": 86583, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-BUNER", "district_name": "Buner", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1865.0, "population_2023": 1016869, "population_male": 508172, "population_female": 508669, "population_transgender": 28, "population_rural": 1016869, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 99.9, "density_per_sqkm": 545.24, "avg_household_size": 8.5, "household_count_estimated": 119631, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-CHARSADDA", "district_name": "Charsadda", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 996.0, "population_2023": 1835504, "population_male": 950872, "population_female": 884613, "population_transgender": 19, "population_rural": 1543078, "population_urban": 292426, "urban_proportion_pct": 15.93, "sex_ratio": 107.49, "density_per_sqkm": 1842.88, "avg_household_size": 6.9, "household_count_estimated": 266015, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-DERA-ISMAIL-KHAN", "district_name": "Dera Ismail Khan", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 9334.0, "population_2023": 1829811, "population_male": 959405, "population_female": 870255, "population_transgender": 151, "population_rural": 1455054, "population_urban": 374757, "urban_proportion_pct": 20.48, "sex_ratio": 110.24, "density_per_sqkm": 196.04, "avg_household_size": 6.7, "household_count_estimated": 273106, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-HANGU", "district_name": "Hangu", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1097.0, "population_2023": 528902, "population_male": 260293, "population_female": 268601, "population_transgender": 8, "population_rural": 443175, "population_urban": 85727, "urban_proportion_pct": 16.21, "sex_ratio": 96.91, "density_per_sqkm": 482.13, "avg_household_size": 8.6, "household_count_estimated": 61500, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-HARIPUR", "district_name": "Haripur", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1725.0, "population_2023": 1174783, "population_male": 591540, "population_female": 583198, "population_transgender": 45, "population_rural": 1027018, "population_urban": 147765, "urban_proportion_pct": 12.58, "sex_ratio": 101.43, "density_per_sqkm": 681.03, "avg_household_size": 6.1, "household_count_estimated": 192587, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-KARAK", "district_name": "Karak", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 3371.0, "population_2023": 815878, "population_male": 421292, "population_female": 394575, "population_transgender": 11, "population_rural": 757813, "population_urban": 58065, "urban_proportion_pct": 7.12, "sex_ratio": 106.77, "density_per_sqkm": 242.03, "avg_household_size": 8.4, "household_count_estimated": 97128, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-KHYBER", "district_name": "Khyber", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 2576.0, "population_2023": 1146267, "population_male": 598268, "population_female": 547989, "population_transgender": 10, "population_rural": 1051560, "population_urban": 94707, "urban_proportion_pct": 8.26, "sex_ratio": 109.18, "density_per_sqkm": 444.98, "avg_household_size": 6.8, "household_count_estimated": 168568, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-KOHAT", "district_name": "Kohat", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 2991.0, "population_2023": 1234661, "population_male": 629566, "population_female": 605066, "population_transgender": 29, "population_rural": 955920, "population_urban": 278741, "urban_proportion_pct": 22.58, "sex_ratio": 104.05, "density_per_sqkm": 412.79, "avg_household_size": 7.2, "household_count_estimated": 171480, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-KOLAI-PALAS-KOHISTAN", "district_name": "Kolai Palas Kohistan", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1410.0, "population_2023": 280162, "population_male": 142588, "population_female": 137572, "population_transgender": 2, "population_rural": 280162, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 103.65, "density_per_sqkm": 198.7, "avg_household_size": 6.9, "household_count_estimated": 40603, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-KURRAM", "district_name": "Kurram", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 3380.0, "population_2023": 785434, "population_male": 406914, "population_female": 378505, "population_transgender": 15, "population_rural": 739963, "population_urban": 45471, "urban_proportion_pct": 5.79, "sex_ratio": 107.51, "density_per_sqkm": 232.38, "avg_household_size": 8.3, "household_count_estimated": 94630, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-LAKKI-MARWAT", "district_name": "Lakki Marwat", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 3296.0, "population_2023": 1040856, "population_male": 527121, "population_female": 513722, "population_transgender": 13, "population_rural": 937767, "population_urban": 103089, "urban_proportion_pct": 9.9, "sex_ratio": 102.61, "density_per_sqkm": 315.79, "avg_household_size": 7.8, "household_count_estimated": 133443, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-LOWER-CHITRAL", "district_name": "Lower Chitral", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 6458.0, "population_2023": 320407, "population_male": 163584, "population_female": 156823, "population_transgender": 0, "population_rural": 263250, "population_urban": 57157, "urban_proportion_pct": 17.84, "sex_ratio": 104.31, "density_per_sqkm": 49.61, "avg_household_size": 6.9, "household_count_estimated": 46435, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-LOWER-DIR", "district_name": "Lower Dir", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1583.0, "population_2023": 1650183, "population_male": 813551, "population_female": 836605, "population_transgender": 27, "population_rural": 1602323, "population_urban": 47860, "urban_proportion_pct": 2.9, "sex_ratio": 97.24, "density_per_sqkm": 1042.44, "avg_household_size": 8.1, "household_count_estimated": 203726, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-LOWER-KOHISTAN", "district_name": "Lower Kohistan", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 642.0, "population_2023": 340017, "population_male": 173655, "population_female": 166351, "population_transgender": 11, "population_rural": 340017, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 104.39, "density_per_sqkm": 529.62, "avg_household_size": 6.4, "household_count_estimated": 53127, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-MALAKAND", "district_name": "Malakand", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 952.0, "population_2023": 826250, "population_male": 422792, "population_female": 403446, "population_transgender": 12, "population_rural": 752725, "population_urban": 73525, "urban_proportion_pct": 8.9, "sex_ratio": 104.8, "density_per_sqkm": 867.91, "avg_household_size": 7.3, "household_count_estimated": 113184, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-MANSEHRA", "district_name": "Mansehra", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 4125.0, "population_2023": 1797177, "population_male": 912164, "population_female": 884906, "population_transgender": 107, "population_rural": 1642343, "population_urban": 154834, "urban_proportion_pct": 8.62, "sex_ratio": 103.08, "density_per_sqkm": 435.68, "avg_household_size": 6.1, "household_count_estimated": 294619, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-MARDAN", "district_name": "Mardan", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1632.0, "population_2023": 2744898, "population_male": 1408776, "population_female": 1336069, "population_transgender": 53, "population_rural": 2291556, "population_urban": 453342, "urban_proportion_pct": 16.52, "sex_ratio": 105.44, "density_per_sqkm": 1681.92, "avg_household_size": 6.8, "household_count_estimated": 403661, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-MOHMAND", "district_name": "Mohmand", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 2296.0, "population_2023": 553933, "population_male": 281384, "population_female": 272543, "population_transgender": 6, "population_rural": 553933, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 103.24, "density_per_sqkm": 241.26, "avg_household_size": 8.6, "household_count_estimated": 64410, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-NORTH-WAZIRISTAN", "district_name": "North Waziristan", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 4707.0, "population_2023": 693332, "population_male": 354636, "population_female": 338681, "population_transgender": 15, "population_rural": 689201, "population_urban": 4131, "urban_proportion_pct": 0.6, "sex_ratio": 104.71, "density_per_sqkm": 147.3, "avg_household_size": 6.9, "household_count_estimated": 100482, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-NOWSHERA", "district_name": "Nowshera", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1748.0, "population_2023": 1740705, "population_male": 886471, "population_female": 854184, "population_transgender": 50, "population_rural": 1398746, "population_urban": 341959, "urban_proportion_pct": 19.64, "sex_ratio": 103.78, "density_per_sqkm": 995.83, "avg_household_size": 6.7, "household_count_estimated": 259806, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-ORAKZAI", "district_name": "Orakzai", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1538.0, "population_2023": 387561, "population_male": 204870, "population_female": 182684, "population_transgender": 7, "population_rural": 387561, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 112.14, "density_per_sqkm": 251.99, "avg_household_size": 7.4, "household_count_estimated": 52373, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-PESHAWAR", "district_name": "Peshawar", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1518.0, "population_2023": 4758762, "population_male": 2425808, "population_female": 2332767, "population_transgender": 187, "population_rural": 2852787, "population_urban": 1905975, "urban_proportion_pct": 40.05, "sex_ratio": 103.99, "density_per_sqkm": 3134.89, "avg_household_size": 6.8, "household_count_estimated": 699817, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-SHANGLA", "district_name": "Shangla", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1586.0, "population_2023": 891252, "population_male": 459965, "population_female": 431281, "population_transgender": 6, "population_rural": 891252, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 106.65, "density_per_sqkm": 561.95, "avg_household_size": 7.0, "household_count_estimated": 127321, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-SOUTH-WAZIRISTAN", "district_name": "South Waziristan", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 6620.0, "population_2023": 888675, "population_male": 459531, "population_female": 429130, "population_transgender": 14, "population_rural": 888675, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 107.08, "density_per_sqkm": 134.24, "avg_household_size": 4.9, "household_count_estimated": 181362, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-SWABI", "district_name": "Swabi", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 1543.0, "population_2023": 1894600, "population_male": 959045, "population_female": 935520, "population_transgender": 35, "population_rural": 1554930, "population_urban": 339670, "urban_proportion_pct": 17.93, "sex_ratio": 102.51, "density_per_sqkm": 1227.87, "avg_household_size": 6.7, "household_count_estimated": 282776, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-SWAT", "district_name": "Swat", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 5337.0, "population_2023": 2687384, "population_male": 1375358, "population_female": 1311939, "population_transgender": 87, "population_rural": 1893016, "population_urban": 794368, "urban_proportion_pct": 29.56, "sex_ratio": 104.83, "density_per_sqkm": 503.54, "avg_household_size": 7.0, "household_count_estimated": 383912, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-TANK", "district_name": "Tank", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 2900.0, "population_2023": 470293, "population_male": 241589, "population_female": 228703, "population_transgender": 1, "population_rural": 421121, "population_urban": 49172, "urban_proportion_pct": 10.46, "sex_ratio": 105.63, "density_per_sqkm": 162.17, "avg_household_size": 6.6, "household_count_estimated": 71256, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-TORGHAR", "district_name": "Torghar", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 454.0, "population_2023": 200445, "population_male": 102160, "population_female": 98281, "population_transgender": 4, "population_rural": 200445, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 103.95, "density_per_sqkm": 441.51, "avg_household_size": 6.8, "household_count_estimated": 29477, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-UPPER-CHITRAL", "district_name": "Upper Chitral", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 8392.0, "population_2023": 195528, "population_male": 100495, "population_female": 95033, "population_transgender": 0, "population_rural": 195528, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 105.75, "density_per_sqkm": 23.3, "avg_household_size": 7.4, "household_count_estimated": 26422, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-UPPER-DIR", "district_name": "Upper Dir", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 3699.0, "population_2023": 1083566, "population_male": 537290, "population_female": 546264, "population_transgender": 12, "population_rural": 1035724, "population_urban": 47842, "urban_proportion_pct": 4.42, "sex_ratio": 98.36, "density_per_sqkm": 292.93, "avg_household_size": 7.2, "household_count_estimated": 150495, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP-D-UPPER-KOHISTAN", "district_name": "Upper Kohistan", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 5440.0, "population_2023": 422947, "population_male": 216184, "population_female": 206759, "population_transgender": 4, "population_rural": 422947, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 104.56, "density_per_sqkm": 77.75, "avg_household_size": 5.9, "household_count_estimated": 71685, "source_file": "table_1_kp_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-AWARAN", "district_name": "Awaran", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 29510.0, "population_2023": 178958, "population_male": 91623, "population_female": 87318, "population_transgender": 17, "population_rural": 132122, "population_urban": 46836, "urban_proportion_pct": 26.17, "sex_ratio": 104.93, "density_per_sqkm": 6.06, "avg_household_size": 6.4, "household_count_estimated": 27962, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-BARKHAN", "district_name": "Barkhan", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 3514.0, "population_2023": 210249, "population_male": 109624, "population_female": 100617, "population_transgender": 8, "population_rural": 195824, "population_urban": 14425, "urban_proportion_pct": 6.86, "sex_ratio": 108.95, "density_per_sqkm": 59.83, "avg_household_size": 9.1, "household_count_estimated": 23104, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-CHAGAI", "district_name": "Chagai", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 44748.0, "population_2023": 269192, "population_male": 139922, "population_female": 129265, "population_transgender": 5, "population_rural": 249138, "population_urban": 20054, "urban_proportion_pct": 7.45, "sex_ratio": 108.24, "density_per_sqkm": 6.02, "avg_household_size": 7.0, "household_count_estimated": 38456, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-CHAMAN", "district_name": "Chaman", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 1341.0, "population_2023": 466218, "population_male": 261194, "population_female": 205011, "population_transgender": 13, "population_rural": 336079, "population_urban": 130139, "urban_proportion_pct": 27.91, "sex_ratio": 127.4, "density_per_sqkm": 347.66, "avg_household_size": 7.5, "household_count_estimated": 62162, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-DERA-BUGTI", "district_name": "Dera Bugti", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 10160.0, "population_2023": 355274, "population_male": 194587, "population_female": 160683, "population_transgender": 4, "population_rural": 246827, "population_urban": 108447, "urban_proportion_pct": 30.52, "sex_ratio": 121.1, "density_per_sqkm": 34.97, "avg_household_size": 5.7, "household_count_estimated": 62328, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-DUKI", "district_name": "Duki", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 4233.0, "population_2023": 205044, "population_male": 107221, "population_female": 97775, "population_transgender": 48, "population_rural": 195261, "population_urban": 9783, "urban_proportion_pct": 4.77, "sex_ratio": 109.66, "density_per_sqkm": 48.44, "avg_household_size": 4.7, "household_count_estimated": 43626, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-GWADAR", "district_name": "Gwadar", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 12637.0, "population_2023": 305160, "population_male": 160744, "population_female": 144385, "population_transgender": 31, "population_rural": 146125, "population_urban": 159035, "urban_proportion_pct": 52.12, "sex_ratio": 111.33, "density_per_sqkm": 24.15, "avg_household_size": 6.0, "household_count_estimated": 50860, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-HARNAI", "district_name": "Harnai", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 2492.0, "population_2023": 127571, "population_male": 67362, "population_female": 60205, "population_transgender": 4, "population_rural": 94138, "population_urban": 33433, "urban_proportion_pct": 26.21, "sex_ratio": 111.89, "density_per_sqkm": 51.19, "avg_household_size": 7.7, "household_count_estimated": 16567, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-JAFFARABAD", "district_name": "Jaffarabad", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 1643.0, "population_2023": 594558, "population_male": 301370, "population_female": 293177, "population_transgender": 11, "population_rural": 431165, "population_urban": 163393, "urban_proportion_pct": 27.48, "sex_ratio": 102.79, "density_per_sqkm": 361.87, "avg_household_size": 7.2, "household_count_estimated": 82577, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-JHAL-MAGSI", "district_name": "Jhal Magsi", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 3615.0, "population_2023": 203368, "population_male": 103422, "population_female": 99933, "population_transgender": 13, "population_rural": 179238, "population_urban": 24130, "urban_proportion_pct": 11.87, "sex_ratio": 103.49, "density_per_sqkm": 56.26, "avg_household_size": 6.5, "household_count_estimated": 31287, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-KACHHI", "district_name": "Kachhi", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 5682.0, "population_2023": 442674, "population_male": 233584, "population_female": 209056, "population_transgender": 34, "population_rural": 362222, "population_urban": 80452, "urban_proportion_pct": 18.17, "sex_ratio": 111.73, "density_per_sqkm": 77.91, "avg_household_size": 8.8, "household_count_estimated": 50303, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-KALAT", "district_name": "Kalat", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 7654.0, "population_2023": 271560, "population_male": 138611, "population_female": 132942, "population_transgender": 7, "population_rural": 227120, "population_urban": 44440, "urban_proportion_pct": 16.36, "sex_ratio": 104.26, "density_per_sqkm": 35.48, "avg_household_size": 8.2, "household_count_estimated": 33117, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-KECH", "district_name": "Kech", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 22539.0, "population_2023": 1060931, "population_male": 555219, "population_female": 505589, "population_transgender": 123, "population_rural": 674285, "population_urban": 386646, "urban_proportion_pct": 36.44, "sex_ratio": 109.82, "density_per_sqkm": 47.07, "avg_household_size": 4.1, "household_count_estimated": 258763, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-KHARAN", "district_name": "Kharan", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 14958.0, "population_2023": 260352, "population_male": 139695, "population_female": 120646, "population_transgender": 11, "population_rural": 179546, "population_urban": 80806, "urban_proportion_pct": 31.04, "sex_ratio": 115.79, "density_per_sqkm": 17.41, "avg_household_size": 7.2, "household_count_estimated": 36160, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-KHUZDAR", "district_name": "Khuzdar", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 35380.0, "population_2023": 997214, "population_male": 537313, "population_female": 459867, "population_transgender": 34, "population_rural": 632836, "population_urban": 364378, "urban_proportion_pct": 36.54, "sex_ratio": 116.84, "density_per_sqkm": 28.19, "avg_household_size": 6.1, "household_count_estimated": 163477, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-KILLA-ABDULLAH", "district_name": "Killa Abdullah", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 3553.0, "population_2023": 361971, "population_male": 189172, "population_female": 172783, "population_transgender": 16, "population_rural": 326587, "population_urban": 35384, "urban_proportion_pct": 9.78, "sex_ratio": 109.49, "density_per_sqkm": 101.88, "avg_household_size": 5.3, "household_count_estimated": 68296, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-KILLA-SAIFULLAH", "district_name": "Killa Saifullah", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 6831.0, "population_2023": 380200, "population_male": 199074, "population_female": 181125, "population_transgender": 1, "population_rural": 316025, "population_urban": 64175, "urban_proportion_pct": 16.88, "sex_ratio": 109.91, "density_per_sqkm": 55.66, "avg_household_size": 5.4, "household_count_estimated": 70407, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-KOHLU", "district_name": "Kohlu", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 7610.0, "population_2023": 260220, "population_male": 136243, "population_female": 123961, "population_transgender": 16, "population_rural": 241242, "population_urban": 18978, "urban_proportion_pct": 7.29, "sex_ratio": 109.91, "density_per_sqkm": 34.19, "avg_household_size": 6.8, "household_count_estimated": 38267, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-LASBELA", "district_name": "Lasbela", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 15153.0, "population_2023": 680977, "population_male": 348840, "population_female": 332112, "population_transgender": 25, "population_rural": 350392, "population_urban": 330585, "urban_proportion_pct": 48.55, "sex_ratio": 105.04, "density_per_sqkm": 44.94, "avg_household_size": 5.8, "household_count_estimated": 117409, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-LORALAI", "district_name": "Loralai", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 3785.0, "population_2023": 272432, "population_male": 142774, "population_female": 129641, "population_transgender": 17, "population_rural": 212831, "population_urban": 59601, "urban_proportion_pct": 21.88, "sex_ratio": 110.13, "density_per_sqkm": 71.98, "avg_household_size": 7.1, "household_count_estimated": 38370, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-MASTUNG", "district_name": "Mastung", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 3308.0, "population_2023": 313271, "population_male": 166679, "population_female": 146589, "population_transgender": 3, "population_rural": 272897, "population_urban": 40374, "urban_proportion_pct": 12.89, "sex_ratio": 113.7, "density_per_sqkm": 94.7, "avg_household_size": 7.1, "household_count_estimated": 44122, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-MUSAKHEL", "district_name": "Musakhel", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 5728.0, "population_2023": 182275, "population_male": 96706, "population_female": 85566, "population_transgender": 3, "population_rural": 166470, "population_urban": 15805, "urban_proportion_pct": 8.67, "sex_ratio": 113.02, "density_per_sqkm": 31.82, "avg_household_size": 5.8, "household_count_estimated": 31426, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-NASIRABAD", "district_name": "Nasirabad", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 3387.0, "population_2023": 563315, "population_male": 287902, "population_female": 275395, "population_transgender": 18, "population_rural": 456363, "population_urban": 106952, "urban_proportion_pct": 18.99, "sex_ratio": 104.54, "density_per_sqkm": 166.32, "avg_household_size": 6.4, "household_count_estimated": 88017, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-NUSHKI", "district_name": "Nushki", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 5797.0, "population_2023": 207834, "population_male": 108271, "population_female": 99558, "population_transgender": 5, "population_rural": 159262, "population_urban": 48572, "urban_proportion_pct": 23.37, "sex_ratio": 108.75, "density_per_sqkm": 35.85, "avg_household_size": 6.6, "household_count_estimated": 31490, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-PANJGUR", "district_name": "Panjgur", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 16891.0, "population_2023": 509781, "population_male": 269372, "population_female": 240314, "population_transgender": 95, "population_rural": 352088, "population_urban": 157693, "urban_proportion_pct": 30.93, "sex_ratio": 112.09, "density_per_sqkm": 30.18, "avg_household_size": 4.3, "household_count_estimated": 118553, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-PISHIN", "district_name": "Pishin", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 6218.0, "population_2023": 835482, "population_male": 426597, "population_female": 408862, "population_transgender": 23, "population_rural": 591697, "population_urban": 243785, "urban_proportion_pct": 29.18, "sex_ratio": 104.34, "density_per_sqkm": 134.37, "avg_household_size": 5.6, "household_count_estimated": 149193, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-QUETTA", "district_name": "Quetta", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 3447.0, "population_2023": 2595492, "population_male": 1319869, "population_female": 1275512, "population_transgender": 111, "population_rural": 1029946, "population_urban": 1565546, "urban_proportion_pct": 60.32, "sex_ratio": 103.48, "density_per_sqkm": 752.97, "avg_household_size": 8.9, "household_count_estimated": 291628, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-SHERANI", "district_name": "Sherani", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 4310.0, "population_2023": 191687, "population_male": 105345, "population_female": 86336, "population_transgender": 6, "population_rural": 191687, "population_urban": 0, "urban_proportion_pct": 0.0, "sex_ratio": 122.02, "density_per_sqkm": 44.47, "avg_household_size": 5.3, "household_count_estimated": 36167, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-SIBI", "district_name": "Sibi", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 7121.0, "population_2023": 224148, "population_male": 115033, "population_female": 109110, "population_transgender": 5, "population_rural": 154848, "population_urban": 69300, "urban_proportion_pct": 30.92, "sex_ratio": 105.43, "density_per_sqkm": 31.48, "avg_household_size": 7.1, "household_count_estimated": 31570, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-SOHBATPUR", "district_name": "Sohbatpur", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 802.0, "population_2023": 240106, "population_male": 121863, "population_female": 118241, "population_transgender": 2, "population_rural": 225378, "population_urban": 14728, "urban_proportion_pct": 6.13, "sex_ratio": 103.06, "density_per_sqkm": 299.38, "avg_household_size": 7.1, "household_count_estimated": 33817, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-SURAB", "district_name": "Surab", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 762.0, "population_2023": 279038, "population_male": 141648, "population_female": 137372, "population_transgender": 18, "population_rural": 242570, "population_urban": 36468, "urban_proportion_pct": 13.07, "sex_ratio": 103.11, "density_per_sqkm": 366.19, "avg_household_size": 5.4, "household_count_estimated": 51673, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-WASHUK", "district_name": "Washuk", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 33093.0, "population_2023": 302623, "population_male": 162913, "population_female": 139685, "population_transgender": 25, "population_rural": 261516, "population_urban": 41107, "urban_proportion_pct": 13.58, "sex_ratio": 116.63, "density_per_sqkm": 9.14, "avg_household_size": 6.1, "household_count_estimated": 49610, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-ZHOB", "district_name": "Zhob", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 15987.0, "population_2023": 355692, "population_male": 192202, "population_female": 163485, "population_transgender": 5, "population_rural": 308716, "population_urban": 46976, "urban_proportion_pct": 13.21, "sex_ratio": 117.57, "density_per_sqkm": 22.25, "avg_household_size": 7.4, "household_count_estimated": 48066, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA-D-ZIARAT", "district_name": "Ziarat", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 3301.0, "population_2023": 189535, "population_male": 96172, "population_female": 93355, "population_transgender": 8, "population_rural": 140133, "population_urban": 49402, "urban_proportion_pct": 26.06, "sex_ratio": 103.02, "density_per_sqkm": 57.42, "avg_household_size": 8.2, "household_count_estimated": 23114, "source_file": "table_1_balochistan_districts.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK-IS-D-ISLAMABAD", "district_name": "Islamabad", "province_id": "PK-IS", "province_name": "Islamabad", "area_sqkm": 906.0, "population_2023": 2363863, "population_male": 1247693, "population_female": 1115900, "population_transgender": 270, "population_rural": 656104, "population_urban": 1108872, "urban_proportion_pct": 46.91, "sex_ratio": 111.81, "density_per_sqkm": 2609.12, "avg_household_size": 5.7, "household_count_estimated": 414712, "source_file": "table_1_islamabad.xlsx", "source_table": "PBS Census 2023 Table 1", "extraction_date": "2026-10-29"}, {"geography_id": "PK", "district_name": "Pakistan", "province_id": "PK", "province_name": "Pakistan", "area_sqkm": 796096.0, "population_2023": 241499431, "population_male": 124324406, "population_female": 117154694, "population_transgender": 20331, "population_rural": 0, "population_urban": 0, "urban_proportion_pct": 0, "sex_ratio": 106.12, "density_per_sqkm": 303.35, "avg_household_size": 6.3, "household_count_estimated": 38333243, "source_file": "table_1_national.xlsx", "source_table": "PBS Census 2023 Table 1 (National/Provincial Summary)", "extraction_date": "2026-10-29"}, {"geography_id": "PK-KP", "district_name": "Khyber Pakhtunkhwa", "province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "area_sqkm": 101741.0, "population_2023": 40856097, "population_male": 20845747, "population_female": 20009233, "population_transgender": 1117, "population_rural": 0, "population_urban": 0, "urban_proportion_pct": 0, "sex_ratio": 104.18, "density_per_sqkm": 401.57, "avg_household_size": 6.3, "household_count_estimated": 6485094, "source_file": "table_1_national.xlsx", "source_table": "PBS Census 2023 Table 1 (National/Provincial Summary)", "extraction_date": "2026-10-29"}, {"geography_id": "PK-PB", "district_name": "Punjab", "province_id": "PK-PB", "province_name": "Punjab", "area_sqkm": 205345.0, "population_2023": 127688922, "population_male": 65448376, "population_female": 62226589, "population_transgender": 13957, "population_rural": 0, "population_urban": 0, "urban_proportion_pct": 0, "sex_ratio": 105.18, "density_per_sqkm": 621.83, "avg_household_size": 6.3, "household_count_estimated": 20268082, "source_file": "table_1_national.xlsx", "source_table": "PBS Census 2023 Table 1 (National/Provincial Summary)", "extraction_date": "2026-10-29"}, {"geography_id": "PK-SD", "district_name": "Sindh", "province_id": "PK-SD", "province_name": "Sindh", "area_sqkm": 140914.0, "population_2023": 55696147, "population_male": 29014424, "population_female": 26677501, "population_transgender": 4222, "population_rural": 0, "population_urban": 0, "urban_proportion_pct": 0, "sex_ratio": 108.76, "density_per_sqkm": 395.25, "avg_household_size": 6.3, "household_count_estimated": 8840658, "source_file": "table_1_national.xlsx", "source_table": "PBS Census 2023 Table 1 (National/Provincial Summary)", "extraction_date": "2026-10-29"}, {"geography_id": "PK-BA", "district_name": "Balochistan", "province_id": "PK-BA", "province_name": "Balochistan", "area_sqkm": 347190.0, "population_2023": 14894402, "population_male": 7768166, "population_female": 7125471, "population_transgender": 765, "population_rural": 0, "population_urban": 0, "urban_proportion_pct": 0, "sex_ratio": 109.02, "density_per_sqkm": 42.9, "avg_household_size": 6.3, "household_count_estimated": 2364190, "source_file": "table_1_national.xlsx", "source_table": "PBS Census 2023 Table 1 (National/Provincial Summary)", "extraction_date": "2026-10-29"}], "agri_shifts": [{"province_name": "Punjab", "farms_2010": 5249400, "farms_2024": 6842100, "farms_change_pct": 30.3, "cultivated_acres_2010": 28640100, "cultivated_acres_2024": 33120400, "cultivated_change_pct": 15.6, "avg_farm_size_2024": 4.8}, {"province_name": "Sindh", "farms_2010": 1115300, "farms_2024": 1598400, "farms_change_pct": 43.3, "cultivated_acres_2010": 7940200, "cultivated_acres_2024": 9480100, "cultivated_change_pct": 19.4, "avg_farm_size_2024": 5.9}, {"province_name": "Khyber Pakhtunkhwa", "farms_2010": 1618200, "farms_2024": 2241500, "farms_change_pct": 38.5, "cultivated_acres_2010": 3980100, "cultivated_acres_2024": 4920200, "cultivated_change_pct": 23.6, "avg_farm_size_2024": 2.2}, {"province_name": "Balochistan", "farms_2010": 281580, "farms_2024": 421697, "farms_change_pct": 49.8, "cultivated_acres_2010": 2062073, "cultivated_acres_2024": 5266964, "cultivated_change_pct": 155.4, "avg_farm_size_2024": 12.5}], "census_hist": [{"census_year": 1951, "population_millions": 33.74, "intercensal_increase_pct": 0.0, "annual_growth_rate_pct": 0.0, "household_size_avg": 5.6, "urban_share_pct": 17.8, "source_citation": "PBS Population Census Records (1951-2023)"}, {"census_year": 1961, "population_millions": 42.88, "intercensal_increase_pct": 27.1, "annual_growth_rate_pct": 2.45, "household_size_avg": 5.7, "urban_share_pct": 22.5, "source_citation": "PBS Population Census Records (1951-2023)"}, {"census_year": 1972, "population_millions": 65.31, "intercensal_increase_pct": 52.3, "annual_growth_rate_pct": 3.67, "household_size_avg": 6.1, "urban_share_pct": 25.4, "source_citation": "PBS Population Census Records (1951-2023)"}, {"census_year": 1981, "population_millions": 84.25, "intercensal_increase_pct": 29.0, "annual_growth_rate_pct": 3.1, "household_size_avg": 6.7, "urban_share_pct": 28.3, "source_citation": "PBS Population Census Records (1951-2023)"}, {"census_year": 1998, "population_millions": 132.35, "intercensal_increase_pct": 57.1, "annual_growth_rate_pct": 2.69, "household_size_avg": 6.8, "urban_share_pct": 32.5, "source_citation": "PBS Population Census Records (1951-2023)"}, {"census_year": 2017, "population_millions": 207.68, "intercensal_increase_pct": 56.9, "annual_growth_rate_pct": 2.4, "household_size_avg": 6.4, "urban_share_pct": 36.4, "source_citation": "PBS Population Census Records (1951-2023)"}, {"census_year": 2023, "population_millions": 241.5, "intercensal_increase_pct": 16.3, "annual_growth_rate_pct": 2.55, "household_size_avg": 6.3, "urban_share_pct": 38.8, "source_citation": "PBS 7th Digital Population & Housing Census 2023 Table 1"}], "macro": [{"year": 2025, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 407307214476.22, "gdp_growth_pct": 3.7, "inflation_cpi_pct": 3.55, "population_total": 255219554.0, "exports_pct_gdp": 9.99}, {"year": 2024, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 371747087751.31, "gdp_growth_pct": 3.08, "inflation_cpi_pct": 12.63, "population_total": 251269164.0, "exports_pct_gdp": 10.39}, {"year": 2023, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 336686348609.27, "gdp_growth_pct": -0.41, "inflation_cpi_pct": 30.77, "population_total": 247504495.0, "exports_pct_gdp": 10.49}, {"year": 2022, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 374890295666.69, "gdp_growth_pct": 4.78, "inflation_cpi_pct": 19.87, "population_total": 243700667.0, "exports_pct_gdp": 10.54}, {"year": 2021, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 348516647445.15, "gdp_growth_pct": 6.51, "inflation_cpi_pct": 9.5, "population_total": 239477801.0, "exports_pct_gdp": 9.05}, {"year": 2020, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 300425609817.98, "gdp_growth_pct": -1.27, "inflation_cpi_pct": 9.74, "population_total": 235001746.0, "exports_pct_gdp": 9.3}, {"year": 2019, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 320909472770.67, "gdp_growth_pct": 2.5, "inflation_cpi_pct": 10.58, "population_total": 230800899.0, "exports_pct_gdp": 9.39}, {"year": 2018, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 356128166704.92, "gdp_growth_pct": 6.15, "inflation_cpi_pct": 5.08, "population_total": 226928892.0, "exports_pct_gdp": 8.58}, {"year": 2017, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 339205534861.1, "gdp_growth_pct": 4.43, "inflation_cpi_pct": 4.09, "population_total": 223273967.0, "exports_pct_gdp": 8.22}, {"year": 2016, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 313630000130.43, "gdp_growth_pct": 6.57, "inflation_cpi_pct": 3.77, "population_total": 220138869.0, "exports_pct_gdp": 8.74}, {"year": 2015, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 299963590534.77, "gdp_growth_pct": 4.22, "inflation_cpi_pct": 2.53, "population_total": 217290883.0, "exports_pct_gdp": 9.97}, {"year": 2014, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 271390474857.63, "gdp_growth_pct": 4.12, "inflation_cpi_pct": 7.19, "population_total": 214264647.0, "exports_pct_gdp": 11.19}, {"year": 2013, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 258657231672.41, "gdp_growth_pct": 4.37, "inflation_cpi_pct": 7.69, "population_total": 211073978.0, "exports_pct_gdp": 12.18}, {"year": 2012, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 250106966104.7, "gdp_growth_pct": 3.03, "inflation_cpi_pct": 9.68, "population_total": 207667125.0, "exports_pct_gdp": 11.87}, {"year": 2011, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 230586581059.67, "gdp_growth_pct": 2.68, "inflation_cpi_pct": 11.92, "population_total": 203746065.0, "exports_pct_gdp": 13.48}, {"year": 2010, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 196709621849.59, "gdp_growth_pct": 1.5, "inflation_cpi_pct": 12.94, "population_total": 199239047.0, "exports_pct_gdp": 12.64}, {"year": 2009, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 187337783856.47, "gdp_growth_pct": 3.47, "inflation_cpi_pct": 13.65, "population_total": 194376534.0, "exports_pct_gdp": 12.39}, {"year": 2008, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 202203748583.85, "gdp_growth_pct": 2.12, "inflation_cpi_pct": 20.29, "population_total": 189499113.0, "exports_pct_gdp": 11.88}, {"year": 2007, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 184140869997.46, "gdp_growth_pct": 4.44, "inflation_cpi_pct": 7.6, "population_total": 184493231.0, "exports_pct_gdp": 11.63}, {"year": 2006, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 161871385506.36, "gdp_growth_pct": 6.05, "inflation_cpi_pct": 7.92, "population_total": 179682690.0, "exports_pct_gdp": 12.55}, {"year": 2005, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 145208562960.77, "gdp_growth_pct": 7.28, "inflation_cpi_pct": 9.06, "population_total": 175453212.0, "exports_pct_gdp": 12.25}, {"year": 2004, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 132216048339.41, "gdp_growth_pct": 7.83, "inflation_cpi_pct": 7.44, "population_total": 171286000.0, "exports_pct_gdp": 11.42}, {"year": 2003, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 112371913740.82, "gdp_growth_pct": 5.4, "inflation_cpi_pct": 2.91, "population_total": 167110248.0, "exports_pct_gdp": 12.16}, {"year": 2002, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 97923302809.35, "gdp_growth_pct": 2.59, "inflation_cpi_pct": 3.29, "population_total": 163222549.0, "exports_pct_gdp": 11.26}, {"year": 2001, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 97145618479.9, "gdp_growth_pct": 3.65, "inflation_cpi_pct": 3.15, "population_total": 159270907.0, "exports_pct_gdp": 10.63}, {"year": 2000, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 99484802344.53, "gdp_growth_pct": 4.26, "inflation_cpi_pct": 4.37, "population_total": 154879127.0, "exports_pct_gdp": 9.63}, {"year": 1999, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 62973857068.51, "gdp_growth_pct": 3.66, "inflation_cpi_pct": 4.14, "population_total": 150565377.0, "exports_pct_gdp": 15.35}, {"year": 1998, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 62191955814.35, "gdp_growth_pct": 2.55, "inflation_cpi_pct": 6.23, "population_total": 146522356.0, "exports_pct_gdp": 16.48}, {"year": 1997, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 62433340468.02, "gdp_growth_pct": 1.01, "inflation_cpi_pct": 11.38, "population_total": 142531804.0, "exports_pct_gdp": 16.08}, {"year": 1996, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 63320170084.41, "gdp_growth_pct": 4.85, "inflation_cpi_pct": 10.37, "population_total": 138557092.0, "exports_pct_gdp": 16.9}, {"year": 1995, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 60636071684.19, "gdp_growth_pct": 4.96, "inflation_cpi_pct": 12.34, "population_total": 134582253.0, "exports_pct_gdp": 16.71}, {"year": 1994, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 52293470813.13, "gdp_growth_pct": 3.74, "inflation_cpi_pct": 12.37, "population_total": 130748083.0, "exports_pct_gdp": 16.16}, {"year": 1993, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 51809999353.16, "gdp_growth_pct": 1.76, "inflation_cpi_pct": 9.97, "population_total": 127020117.0, "exports_pct_gdp": 16.2}, {"year": 1992, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 48884671947.47, "gdp_growth_pct": 7.71, "inflation_cpi_pct": 9.51, "population_total": 123546848.0, "exports_pct_gdp": 17.27}, {"year": 1991, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 45625336680.2, "gdp_growth_pct": 5.06, "inflation_cpi_pct": 11.79, "population_total": 120060406.0, "exports_pct_gdp": 16.93}, {"year": 1990, "country": "Pakistan", "country_code": "PK", "gdp_current_usd": 40010423970.46, "gdp_growth_pct": 4.46, "inflation_cpi_pct": 9.05, "population_total": 116155576.0, "exports_pct_gdp": 14.79}], "prov_matrix": [{"province_id": "PK-PB", "province_name": "Punjab", "population_2023": 127688922, "area_sqkm": 205344, "total_budget_fy25_pkr_b": 5446.0, "development_adp_pkr_b": 842.0, "current_expenditure_pkr_b": 4604.0, "development_share_pct": 15.46, "public_debt_stock_pkr_b": 1685.0, "debt_external_share_pct": 99.9, "debt_per_capita_pkr": 13196, "budget_per_capita_pkr": 42650, "dev_per_capita_pkr": 6594, "dev_per_sqkm_pkr_m": 4.1, "terrorism_fatalities_2023_24": 138, "terrorism_share_pct": 3.36, "terrorism_incidents_2023_24": 112, "mpi_poverty_pct": 31.4}, {"province_id": "PK-SN", "province_name": "Sindh", "population_2023": 55696147, "area_sqkm": 140914, "total_budget_fy25_pkr_b": 3056.0, "development_adp_pkr_b": 959.1, "current_expenditure_pkr_b": 2096.9, "development_share_pct": 31.38, "public_debt_stock_pkr_b": 1065.0, "debt_external_share_pct": 98.7, "debt_per_capita_pkr": 19121, "budget_per_capita_pkr": 54869, "dev_per_capita_pkr": 17220, "dev_per_sqkm_pkr_m": 6.81, "terrorism_fatalities_2023_24": 183, "terrorism_share_pct": 4.46, "terrorism_incidents_2023_24": 148, "mpi_poverty_pct": 43.1}, {"province_id": "PK-KP", "province_name": "Khyber Pakhtunkhwa", "population_2023": 40856097, "area_sqkm": 101741, "total_budget_fy25_pkr_b": 1754.0, "development_adp_pkr_b": 416.3, "current_expenditure_pkr_b": 1337.7, "development_share_pct": 23.73, "public_debt_stock_pkr_b": 723.0, "debt_external_share_pct": 100.0, "debt_per_capita_pkr": 17696, "budget_per_capita_pkr": 42931, "dev_per_capita_pkr": 10190, "dev_per_sqkm_pkr_m": 4.09, "terrorism_fatalities_2023_24": 2591, "terrorism_share_pct": 63.09, "terrorism_incidents_2023_24": 1120, "mpi_poverty_pct": 49.2}, {"province_id": "PK-BA", "province_name": "Balochistan", "population_2023": 14894402, "area_sqkm": 347190, "total_budget_fy25_pkr_b": 955.6, "development_adp_pkr_b": 321.15, "current_expenditure_pkr_b": 634.45, "development_share_pct": 33.61, "public_debt_stock_pkr_b": 285.0, "debt_external_share_pct": 95.0, "debt_per_capita_pkr": 19135, "budget_per_capita_pkr": 64158, "dev_per_capita_pkr": 21562, "dev_per_sqkm_pkr_m": 0.92, "terrorism_fatalities_2023_24": 1195, "terrorism_share_pct": 29.09, "terrorism_incidents_2023_24": 680, "mpi_poverty_pct": 71.2}]};

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
        window.filterGallery = function(category, targetBtn) {
          const buttons = document.querySelectorAll('.vi-filter-btn');
          buttons.forEach(b => {
            b.classList.remove('active');
            b.setAttribute('aria-selected', 'false');
          });
          const activeBtn = targetBtn || (window.event && window.event.target ? window.event.target.closest('.vi-filter-btn') : null);
          if (activeBtn) {
            activeBtn.classList.add('active');
            activeBtn.setAttribute('aria-selected', 'true');
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
        window.filterCategory = window.filterGallery;

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
          const title = card.querySelector('.vi-card-title') ? card.querySelector('.vi-card-title').innerText.replace(/^#\d+:\s*/, '').trim() : 'PPRI Policy Infographic';
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
          const url = `/data/published/${datasetKey}.csv`;
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
        // 3. INTERACTIVE QUICK-JUMP SMOOTH SCROLL HANDLER
        function initQuickNav() {
          const chips = document.querySelectorAll('.vi-chip-btn[data-target]');
          chips.forEach(btn => {
            // Avoid duplicate listeners
            if (btn.__hasQuickNav) return;
            btn.__hasQuickNav = true;
            btn.addEventListener('click', function(e) {
              e.preventDefault();
              const targetId = this.getAttribute('data-target');
              const targetCard = document.getElementById(targetId);
              if (!targetCard) return;

              // If hidden by active filter, unhide by resetting filter to 'all'
              if (targetCard.style.display === 'none') {
                if (typeof window.filterGallery === 'function') {
                  window.filterGallery('all');
                }
              }

              targetCard.scrollIntoView({ behavior: 'smooth', block: 'start' });

              targetCard.classList.remove('vi-card-highlight');
              void targetCard.offsetWidth;
              targetCard.classList.add('vi-card-highlight');
              setTimeout(() => {
                targetCard.classList.remove('vi-card-highlight');
              }, 2200);
            });
          });
        }

          initQuickNav();

        // Render immediately using embedded in-memory data
        if (document.readyState === 'loading') {
          document.addEventListener('DOMContentLoaded', renderAllCards);
        } else {
          renderAllCards();
        }

      })();