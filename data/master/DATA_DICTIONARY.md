# Data dictionary v0.2.0

**Canonical numeric facts:** `facts/observations.csv` is the single source of truth. `facts/observations.json` is the same records in JSON for static-site build consumption, not an additional set of facts. Identity: `indicator_id + geography_id + reference_period + dimension`.

**Search architecture:** `search/google_year_in_search_rankings.csv` preserves category ranks. `search/google_year_in_search_terms.csv` deduplicates the query phrase within each year and combines its categories/ranks. `search/query_variants.csv` contains candidates with blank volume until measured. `search/query_clusters.csv` maps related variants to a single canonical page.

**Geographies:** District registry follows the PBS Census 2023 listed-district vintage. City/urban locality population is not the same as surrounding district population. District numeric rows remain pending workbook extraction.

**Statuses:** `reported_in_official_report` / `reported_in_official_dashboard` indicate source-reported values located in official outputs, not independent microdata computation. `source identified / values not extracted` means the value is intentionally absent, not zero. Every caveat should travel with its value.
