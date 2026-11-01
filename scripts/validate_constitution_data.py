#!/usr/bin/env python3
"""
scripts/validate_constitution_data.py
Validates the minimalist PPRI Constitution Explorer data files in data/constitution/ against their JSON Schemas:
- articles.json (All 280 Articles + Schedules)
- amendment-register.json (27 positions / 24 enacted)
- constitutional-bills.json (Un-enacted proposals)
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data" / "constitution"
SCHEMAS_DIR = DATA_DIR / "schemas"

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    print("ERROR: jsonschema is required. Run 'python -m pip install jsonschema'.", file=sys.stderr)
    sys.exit(2)

errors: list[str] = []
warnings: list[str] = []

# Load schemas
schema_cache = {}
for s_path in SCHEMAS_DIR.glob("*.schema.json"):
    try:
        s_data = json.loads(s_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(s_data)
        schema_name = s_path.name.replace(".schema.json", "")
        schema_cache[schema_name] = s_data
    except Exception as exc:
        errors.append(f"Invalid schema {s_path.name}: {exc}")

if errors:
    print("Schema syntax errors encountered:")
    for err in errors:
        print(f" - {err}")
    sys.exit(1)

format_checker = FormatChecker()

def validate_item(item: dict, schema_name: str, item_id: str):
    schema = schema_cache.get(schema_name)
    if not schema:
        errors.append(f"Missing schema: {schema_name}")
        return
    validator = Draft202012Validator(schema, format_checker=format_checker)
    for err in validator.iter_errors(item):
        path_str = " -> ".join(str(p) for p in err.path)
        errors.append(f"[{schema_name}] {item_id}: {err.message} (path: {path_str})")

print("=" * 60)
print("PPRI MINIMALIST CONSTITUTION DATA VALIDATION")
print("=" * 60)

# 1. Validate articles.json
articles_path = DATA_DIR / "articles.json"
articles_count = 0
if not articles_path.exists():
    errors.append("Missing articles.json")
else:
    articles_data = json.loads(articles_path.read_text(encoding="utf-8"))
    articles_count = len(articles_data)
    if articles_count < 280:
        errors.append(f"articles.json has only {articles_count} items; expected at least 280 articles.")
    
    seen_numbers = set()
    for art in articles_data:
        art_num = art.get("article_number", "unknown")
        if art_num in seen_numbers:
            errors.append(f"Duplicate article number: {art_num}")
        seen_numbers.add(art_num)
        validate_item(art, "article", f"Article {art_num}")
    
    # Check essential landmark articles
    essential_articles = ["1", "8", "9", "9A", "10A", "19A", "25A", "140A", "160", "172", "239"]
    for ea in essential_articles:
        if ea not in seen_numbers:
            errors.append(f"Essential landmark Article {ea} missing from articles.json")
    print(f"Articles & Schedules validated: {articles_count}")

# 2. Validate amendment-register.json
amendments_path = DATA_DIR / "amendment-register.json"
amendments_count = 0
enacted_count = 0
if not amendments_path.exists():
    errors.append("Missing amendment-register.json")
else:
    amendments_data = json.loads(amendments_path.read_text(encoding="utf-8"))
    amendments_count = len(amendments_data)
    if amendments_count != 27:
        errors.append(f"Expected 27 amendment positions; found {amendments_count}")
    
    positions = set()
    for item in amendments_data:
        pos = item.get("position")
        if pos in positions:
            errors.append(f"Duplicate amendment position: {pos}")
        positions.add(pos)
        validate_item(item, "amendment", f"Amendment position {pos}")
        if item.get("status") == "enacted":
            enacted_count += 1
            if not item.get("assent_date"):
                errors.append(f"Enacted amendment position {pos} missing assent_date")
        elif item.get("status") == "un_enacted_bill":
            if pos not in (9, 11, 15):
                errors.append(f"Unexpected un-enacted amendment at position {pos}")

    if enacted_count != 24:
        errors.append(f"Expected 24 enacted amendment acts; found {enacted_count}")
    print(f"Amendments validated: {amendments_count} (Enacted: {enacted_count})")

# 3. Validate constitutional-bills.json
bills_path = DATA_DIR / "constitutional-bills.json"
bills_count = 0
if not bills_path.exists():
    errors.append("Missing constitutional-bills.json")
else:
    bills_data = json.loads(bills_path.read_text(encoding="utf-8"))
    bills_count = len(bills_data)
    for bill in bills_data:
        bill_id = bill.get("bill_id", "unknown")
        validate_item(bill, "constitutional-bill", bill_id)
        if bill.get("status") != "un_enacted_proposal":
            errors.append(f"Bill {bill_id} status must be 'un_enacted_proposal'")
    print(f"Constitutional bills validated: {bills_count}")

print("-" * 60)
if warnings:
    print(f"WARNINGS ({len(warnings)}):")
    for w in warnings:
        print(f" [WARN] {w}")

if errors:
    print(f"FAILED ({len(errors)} errors):")
    for err in errors:
        print(f" [ERROR] {err}")
    sys.exit(1)

print("PASS: All minimalist Constitution data files conform to JSON Schemas and cross-reference checks!\n")
sys.exit(0)
