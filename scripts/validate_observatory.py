#!/usr/bin/env python3
"""
scripts/validate_observatory.py
Offline integrity, schema, parity, and consistency check for PPRI Data Observatory.
Validates master dataset files in data/master/.
"""

import csv
import json
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
MASTER_DIR = ROOT_DIR / "data" / "master"

def read_csv(filename):
    path = MASTER_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"Missing required master file: {path}")
    with open(path, encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def validate():
    errs = []
    warn = []

    obs = read_csv('observations.csv')
    inds = read_csv('indicator_catalog.csv')
    geos = read_csv('geographies.csv')
    src = read_csv('source_registry.csv')
    qs = read_csv('query_variants.csv')
    clusters = read_csv('query_clusters.csv')
    pages = read_csv('page_catalog.csv')
    ranks = read_csv('google_year_in_search_rankings.csv')
    terms = read_csv('google_year_in_search_terms.csv')
    bridge = read_csv('query_fact_map.csv')

    def check_unique(rows, key, label):
        values = [r.get(key, '') for r in rows if r.get(key, '')]
        if len(values) != len(set(values)):
            errs.append(f"duplicate {label} {key}")

    for rows, k, l in [
        (obs, 'observation_id', 'observation'),
        (inds, 'indicator_id', 'indicator'),
        (geos, 'geography_id', 'geography'),
        (src, 'source_id', 'source'),
        (qs, 'query_id', 'query'),
        (clusters, 'cluster_id', 'cluster'),
        (pages, 'page_id', 'page')
    ]:
        check_unique(rows, k, l)

    sids = {r['source_id'] for r in src}
    gids = {r['geography_id'] for r in geos}
    iids = {r['indicator_id'] for r in inds}
    cids = {r['cluster_id'] for r in clusters}
    pids = {r['page_id'] for r in pages}

    # Foreign key references
    for o in obs:
        if o['source_id'] not in sids:
            errs.append(f"observation missing source: {o['source_id']}")
        if o['geography_id'] not in gids:
            errs.append(f"observation missing geography: {o['geography_id']}")
        if o['indicator_id'] not in iids:
            errs.append(f"observation missing indicator: {o['indicator_id']}")

    for q in qs:
        if q['cluster_id'] not in cids:
            errs.append(f"query missing cluster: {q['query_id']}")
        if q['search_evidence_status'] == 'candidate_unmeasured' and (q['monthly_search_volume'] or q['absolute_search_volume']):
            errs.append(f"candidate query contains volume: {q['query_id']}")

    for c in clusters:
        if c['page_id'] not in pids:
            errs.append(f"cluster missing page: {c['cluster_id']}")

    # Canonical observation keys uniqueness
    keys = [(o['indicator_id'], o['geography_id'], o['reference_period'], o['dimension']) for o in obs]
    if len(keys) != len(set(keys)):
        errs.append("duplicate canonical observation key (indicator/geography/period/dimension)")

    # Canonical paths uniqueness
    paths = [p['canonical_path'] for p in pages]
    if len(paths) != len(set(paths)):
        errs.append("duplicate canonical URL in page_catalog.csv")

    for r in ranks:
        if r['search_volume']:
            errs.append(f"YIS row has absolute volume: {r['query_text_raw']}")

    # JSON vs CSV parity
    with open(MASTER_DIR / 'observations.json', encoding='utf-8') as f:
        oj = json.load(f)
    if len(oj) != len(obs):
        errs.append(f"CSV ({len(obs)}) and JSON ({len(oj)}) observation counts differ")

    # Demographic arithmetic check
    lookup = {(o['indicator_id'], o['geography_id'], o['reference_period']): o for o in obs}
    try:
        total = int(float(lookup[('population_total', 'PK', 'Census 2023')]['value']))
        subtot = sum(int(float(lookup[('population_total', g, 'Census 2023')]['value'])) for g in ['PK-PB', 'PK-SD', 'PK-KP', 'PK-BA', 'PK-ICT'])
        if total != subtot:
            warn.append(f"Province/ICT population sum {subtot} != national total {total}; inspect source family.")
    except Exception as e:
        warn.append(f"Census arithmetic check unavailable: {e}")

    print("=" * 60)
    print(" PPRI Pakistan Permanent Master Dataset Validation")
    print(f" Directory: {MASTER_DIR}")
    print("=" * 60)
    print(f"Observations: {len(obs)} | Indicators: {len(inds)} | Geographies: {len(geos)} | Sources: {len(src)}")
    print(f"Queries: {len(qs)} | Canonical Clusters/Pages: {len(clusters)} | YIS Ranks: {len(ranks)} | Deduplicated YIS Terms: {len(terms)}")
    
    for w in warn:
        print("  WARNING:", w)
    for e in errs:
        print("  ERROR:", e)

    result = "PASS" if not errs else "FAIL"
    print(f"\nRESULT: {result}")
    print("=" * 60)

    if errs:
        sys.exit(1)

if __name__ == "__main__":
    validate()
