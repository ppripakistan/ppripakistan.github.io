# PPRI Pakistan Search-Driven Data Observatory — Dataset v0.2.0

**Build date:** 2026-10-15  
**Market:** Pakistan  
**Objective:** make a connected research foundation that maps search demand/evidence to one canonical page per user intent, then maps the page to source-cited public-data observations.

## What v0.2 adds

This is not a replay of v0.1's same file layout. It consolidates existing numeric records into a normalized fact master and adds additional official-source records: major urban-locality populations and census sex counts; HIES 2018–19 vs 2024–25 household income, consumption, income-source shares, consumption quintiles, household size, internet/computer/mobile/electricity access; selected HIES SDG metrics; and a public-debt snapshot from Pakistan Economic Survey 2025–26. It expands source coverage and proposes one canonical URL per search-intent page, with multilingual candidate queries mapped to it.

## File map

- `facts/observations.csv`: **one canonical fact store** with value, unit, period, geography, source/table, definition, status and caveat.
- `facts/observations.json`: same records serialized for static site builds; it is a format mirror, not additional data.
- `facts/indicator_catalog.csv`: unique indicator definitions and availability status; future/source-mapped indicators have no invented values.
- `geography/geographies.csv`: Pakistan, provinces, ICT, 135 Census 2023 province-district records and 22 major urban locality records. District numeric values are explicitly pending source-workbook extraction.
- `search/google_year_in_search_rankings.csv`: Google Year in Search category ranks for Pakistan in 2024 and 2025.
- `search/google_year_in_search_terms.csv`: deduplicated terms by year, with category ranks consolidated.
- `search/query_variants.csv`: candidate English/Urdu/Roman Urdu phrase set mapped to a cluster. Search-volume columns are blank until measured.
- `search/query_clusters.csv`: canonical intent clusters; one search need maps to one page.
- `pages/page_catalog.csv`: SEO paths, titles, data readiness and UX guidance.
- `relations/query_fact_map.csv`: links cluster IDs to indicator IDs without repeating numeric values in every topic page.
- `sources/source_registry.csv`: official/secondary source metadata; primary government reports take precedence.
- `sources/source_dataset_index.csv`: source files/links with acquisition status and next action.
- `sources/next_extraction_queue.csv`: prioritized tables still needing full extraction.
- `quality/data_quality_report.csv`: methodological conflicts and known limitations.
- `schemas/`: JSON schema examples.
- `scripts/validate_dataset.py`: offline consistency checks.

## Search evidence: what the numbers mean

Google Year in Search lists queries whose search interest rose/trended during the year, ranked inside categories. It is **not** absolute all-time popularity or monthly search volume. See [Google's methodology](https://trends.withgoogle.com/year-in-search/data-methodology/). Candidate phrases in `query_variants.csv` are research ideas, not observed searches. No search volume is fabricated. To get demand measured properly, export Pakistan-targeted Google Trends and Google Ads Keyword Planner reports with extraction date, market, language, query mode, network and time range; after launch add Google Search Console's impressions/clicks for the PPRI property. These are different measures and should stay separate.

## Data authority and caveats

The package prioritizes PBS, Finance Division and other Pakistani official sources; World Bank data is included for cross-checking and Wikipedia only for orientation/secondary references. Each observation carries a source URL, period, unit and caveat. Survey vs census, household vs individual measures, salary vs household income, CPI vs SPI/WPI, budget vs actual spending, and NFC formula shares vs cash transfers must remain distinct.

The HIES 2024–25 income/consumption records are nominal means per household, not median income. Consumption quintiles are not poverty thresholds. Some compact HIES SDG dashboard headlines need exact denominator/definition confirmation against the full social report before page-specific prose is published. The reported social indicators are preserved separately rather than combined into a vague “access” number.

## Known gaps (do not cover up)

1. **District population and density:** PBS Census 2023 district Table 1 workbook links are provided in `sources/source_dataset_index.csv` (from the original v0.1 manifest), but XLSX binaries were not retrievable in this build. District names exist in `geography/geographies.csv`; district numeric rows are not fabricated. Import the workbook files before enabling district population maps/comparators.
2. **Current boundary crosswalk:** Census 2023 district list is a historic source vintage, not a verified October 2026 current administrative list. The target number of website pages must not be mistaken for an official district count.
3. **Full source extraction:** Not every chapter/table in the HIES reports, Economic Survey, budget, monthly trade/price series, SBP remittances/FX or PTA telecom data has been transcribed into the observation store yet. See `sources/next_extraction_queue.csv`.
4. **Search-volume data:** This build has YIS trend ranks and candidate phrase research, not Keyword Planner/Trends numerical exports. Add measured evidence before declaring “top search queries”.
5. **Live service/price pages:** Petroleum rates, exchange rates, electricity tariff, gold quotes, public programmes, board results and e-challan process need timestamped official/source checks before publication. A gold-market quote is not a government-set price.

## Census urban/rural source difference

PBS Census Table 1 reports 93,750,724 urban and 147,748,707 rural for 2023; the Key Findings table reports 93,884,702 urban and 147,614,729 rural. Both pairs sum to 241,499,431. v0.2 retains the inherited Table 1 split as the canonical urban/rural population record and logs the discrepancy in `quality/data_quality_report.csv`; it does not average the figures.

## Use in the website

1. Use `pages/page_catalog.csv` as the routing/content plan, not as automatic permission to publish every page.
2. Use `search/query_variants.csv` as synonyms/search needs on the mapped canonical page, not as a separate list of pages to index.
3. Join `relations/query_fact_map.csv` to the indicator catalog and observations by IDs; do not manually recopy the same numeric data into many files.
4. Carry the `source_url`, table/section, reference period and caveat into chart captions, CSV exports and copy-citation features.
5. Only enable district numeric filters when district-level values are actually present.

## Validation

Run:

```bash
python scripts/validate_dataset.py
```

This checks IDs, references, canonical URL uniqueness, search-volume evidence policy, observation-key uniqueness and CSV/JSON parity. Structural checks cannot independently prove every figure's factual correctness.
