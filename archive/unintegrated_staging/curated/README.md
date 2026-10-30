# PPRI Curated Modular Data Stores (`data/curated/`)

Last Synchronized: 2026-10-29 04:13:53 UTC
Status: **EXPANDED CURATED STORES (11 TOPIC DATASETS)**

This directory hosts clean, domain-specific, modular data tables extracted from primary official sources (Pakistan Bureau of Statistics, Ministry of Finance, State Bank of Pakistan, and World Bank). Rather than flattening all multidimensional tables into a monolithic master observation file, these topic-specific stores preserve natural table relations, column types, and geographic hierarchies.

---

## Complete Catalog of Curated Stores

| File Name | Topic Domain | Rows | Coverage | Primary Source |
|---|---|---|---|---|
| `census_2023_districts.csv/.json` | Demographics & Census | 141 | 135 Districts + ICT + 4 Provinces + Pakistan | PBS Digital Census 2023 Table 1 |
| `lfs_employment_wages.csv/.json` | Labour Force & Wages | 5 | Pakistan + 4 Provinces | PBS Labour Force Survey 2024–25 |
| `hies_household_expenditures.csv/.json` | Living Standards & Consumption | 15 | Pakistan + 4 Provinces (Total, Urban, Rural) | PBS HIES 2024–25 |
| `federal_fiscal_summary.csv/.json` | Fiscal Policy & Public Debt | 3 | National (Multi-Year Trends FY24–FY26) | MoF PES 2025–26 & Budget in Brief |
| `macro_indicators_timeseries.csv/.json` | Macroeconomy (1990–2024) | 36 | 35-Year Time Series | World Bank WDI API & SBP |
| `public_debt_timeseries.csv/.json` | Public Debt Stock (FY18–FY26) | 9 | 8-Year Accumulation Series | MoF Public Debt Bulletin / PES |
| `census_historical_growth.csv/.json` | Demographic Growth (1951–2023) | 7 | 70-Year Intercensal Series | PBS Population Censuses (1951–2023) |
| `agri_census_2024_summary.csv/.json` | Agriculture & Land Structure | 8 | 2010 vs 2024 Structural Shift | PBS 7th Agricultural Census 2024 |
| `tax_expenditures_2025.csv/.json` | Tax Exemptions & Foregone Revenue | 4 | FBR Tax Concession Regimes | FBR Tax Expenditure Report 2025 |
| `housing_basic_services.csv/.json` | Basic Services & Utilities | 5 | National + 4 Provinces | PBS HIES 2024–25 Modules |
| `inflation_wage_growth.csv/.json` | Cost of Living & Real Wages | 5 | 2020–2024 Wage vs CPI Index | PBS Price Statistics & LFS |

---

## Data Standards
1. **Canonical Geographies**: Every row references canonical IDs (`PK`, `PK-PB`, `PK-SD`, `PK-KP`, `PK-BA`, `PK-IS`, or district codes `PK-PB-D-ATTOCK`, etc.) aligned with `data/master/geographies.csv`.
2. **UTF-8 BOM Encoding**: All CSV files include standard UTF-8 BOM (`\uFEFF`) headers for seamless opening in Microsoft Excel without character encoding corruptions.
3. **Exact CSV / JSON Parity**: Every dataset is maintained in exact structural parity between CSV and JSON formats.
