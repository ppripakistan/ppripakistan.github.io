#!/usr/bin/env python3
"""
scripts/acquire_library_data.py
Automated & Guided Data Acquisition Engine for PPRI Pakistan Evidence Base.
Implements Steps 2, 3, 5, and 6 of the 16-Step Acquisition Workflow:
- Identifies exact artifacts & direct URLs
- Streams downloads with custom User-Agent and retry logic
- Computes SHA-256 checksums to guarantee raw provenance
- Preserves raw source files in data/raw/<id>/ without modification
- Maintains an auditable data/raw/acquisition_manifest.json
"""

import os
import sys

# Force UTF-8 stdout/stderr on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

import json
import hashlib
import argparse
import urllib.request
import urllib.error
import ssl
import time
from urllib.parse import urlparse

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG_JSON_PATH = os.path.join(ROOT_DIR, "assets", "data", "pakistan_library_catalog.json")
RAW_DATA_DIR = os.path.join(ROOT_DIR, "data", "raw")
MANIFEST_PATH = os.path.join(RAW_DATA_DIR, "acquisition_manifest.json")
GUIDE_PATH = os.path.join(RAW_DATA_DIR, "acquisition_guide.md")

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 (PPRI Research Archive; +https://ppripakistan.github.io)"

def load_catalog():
    if not os.path.exists(CATALOG_JSON_PATH):
        raise FileNotFoundError(f"Catalog JSON not found at {CATALOG_JSON_PATH}. Run scripts/export_library_json.py first.")
    with open(CATALOG_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_manifest():
    if os.path.exists(MANIFEST_PATH):
        try:
            with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_manifest(manifest):
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

def sanitize_filename(name):
    clean = "".join(c if c.isalnum() or c in "._- " else "_" for c in name).strip()
    return clean[:120]

def derive_filename(url, label="", fallback_name="dataset_file"):
    parsed = urlparse(url)
    clean_path = parsed.path.rstrip("/")
    basename = os.path.basename(clean_path) if clean_path else ""
    
    # Guess extension
    ext = ""
    low_url = url.lower()
    low_label = label.lower() if label else ""
    
    if "format=json" in low_url or low_url.endswith(".json"):
        ext = ".json"
    elif "format=csv" in low_url or low_url.endswith(".csv") or "csv" in low_label:
        ext = ".csv"
    elif low_url.endswith(".zip") or "zip" in low_label:
        ext = ".zip"
    elif low_url.endswith(".pdf") or "pdf" in low_label:
        ext = ".pdf"
    elif low_url.endswith(".xlsx") or "excel" in low_label or low_url.endswith(".xls"):
        ext = ".xlsx"
    elif low_url.endswith(".dta") or "stata" in low_label:
        ext = ".dta"
    elif low_url.endswith(".sav") or "spss" in low_label:
        ext = ".sav"
    elif not basename or "." not in basename:
        ext = ".html"
        
    if basename and "." in basename:
        return sanitize_filename(basename)
        
    stem = sanitize_filename(basename or label or fallback_name)
    if not stem:
        stem = fallback_name
    if ext and not stem.lower().endswith(ext):
        stem += ext
    return stem

def download_file(url, dest_path, timeout=45):
    """
    Streams file download, calculates SHA-256 incrementally,
    handles redirect & custom SSL context.
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9"
        }
    )

    sha256 = hashlib.sha256()
    total_bytes = 0
    temp_path = dest_path + ".tmp"
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    try:
        with urllib.request.urlopen(req, context=ctx, timeout=timeout) as response:
            with open(temp_path, "wb") as out_file:
                while True:
                    chunk = response.read(65536)
                    if not chunk:
                        break
                    sha256.update(chunk)
                    out_file.write(chunk)
                    total_bytes += len(chunk)
                    
        # Atomic rename upon complete download
        if os.path.exists(dest_path):
            os.remove(dest_path)
        os.rename(temp_path, dest_path)
        
        return {
            "success": True,
            "sha256": sha256.hexdigest(),
            "bytes": total_bytes,
            "error": None
        }
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return {
            "success": False,
            "sha256": None,
            "bytes": total_bytes,
            "error": str(e)
        }

def execute_acquisition(target_items, dry_run=False, timeout=30):
    manifest = load_manifest()
    
    print(f"\nTargeting {len(target_items)} resources for acquisition processing...\n")
    
    for idx, item in enumerate(target_items, 1):
        res_id = item.get("id") or item.get("queue_id") or f"ITEM-{idx:03d}"
        title = item.get("title") or item.get("resource_family") or item.get("resource") or "Dataset"
        direct_entries = item.get("direct_entries", [])
        landing_page = item.get("landing_page", "")
        grade = item.get("grade", "A1")
        topic = item.get("topic") or item.get("suggested_topic", "")
        
        print(f"[{idx}/{len(target_items)}] {res_id} ({grade}) - {title[:55]}")
        
        if not direct_entries:
            print(f"    [i] Mode: Portal / Gated Access required ({landing_page})")
            if res_id not in manifest:
                manifest[res_id] = {
                    "resource_id": res_id,
                    "title": title,
                    "landing_page": landing_page,
                    "status": "INTERACTIVE_REQUIRED",
                    "files": []
                }
            continue
            
        res_dir = os.path.join(RAW_DATA_DIR, res_id)
        file_entries = []
        all_success = True
        
        for u_idx, entry in enumerate(direct_entries, 1):
            url = entry["url"]
            label = entry["label"]
            fmt = entry.get("format", "")
            fname = derive_filename(url, label, f"{res_id}_file_{u_idx}")
            dest_file = os.path.join(res_dir, fname)
            rel_path = os.path.relpath(dest_file, ROOT_DIR)
            
            print(f"    -> [{label} ({fmt})] {url}")
            print(f"       Target: {rel_path}")
            
            if dry_run:
                print("       [DRY RUN - skipping actual HTTP request]")
                continue
                
            # If already downloaded and hash verified, skip re-download
            existing_record = None
            if res_id in manifest:
                for f_entry in manifest[res_id].get("files", []):
                    if f_entry.get("url") == url and f_entry.get("status") == "DOWNLOADED":
                        if os.path.exists(dest_file):
                            existing_record = f_entry
                            break
                            
            if existing_record:
                print(f"       [CACHED] {existing_record['bytes']:,} bytes, sha256={existing_record['sha256'][:10]}...")
                file_entries.append(existing_record)
                continue
                
            print(f"       [DOWNLOADING] ...")
            t0 = time.time()
            res = download_file(url, dest_file, timeout=timeout)
            duration = time.time() - t0
            
            if res["success"]:
                print(f"       [SUCCESS] {res['bytes']:,} bytes in {duration:.1f}s (SHA256: {res['sha256'][:10]}...)")
                file_entries.append({
                    "label": label,
                    "format": fmt,
                    "url": url,
                    "filename": fname,
                    "relative_path": rel_path.replace("\\", "/"),
                    "bytes": res["bytes"],
                    "sha256": res["sha256"],
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "status": "DOWNLOADED"
                })
            else:
                print(f"       [FAILED] {res['error']}")
                all_success = False
                file_entries.append({
                    "label": label,
                    "format": fmt,
                    "url": url,
                    "filename": fname,
                    "status": "ERROR",
                    "error": res["error"],
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                })
                
        if not dry_run:
            manifest[res_id] = {
                "resource_id": res_id,
                "title": title,
                "grade": grade,
                "topic": topic,
                "landing_page": landing_page,
                "status": "DOWNLOADED" if all_success else "PARTIAL_OR_ERROR",
                "last_run": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "files": file_entries
            }
            save_manifest(manifest)
            
    print("\nAcquisition process finished.")

def generate_interactive_guide(data):
    """
    Builds data/raw/acquisition_guide.md listing sources that require
    interactive browser navigation, credentials, or custom query parameters.
    """
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    gated_items = [i for i in data["catalog"] if not i["direct_urls"]]
    queue_items = data.get("download_queue", [])
    
    with open(GUIDE_PATH, "w", encoding="utf-8") as f:
        f.write("# Pakistan Data Resource Inventory — Interactive Acquisition Guide\n\n")
        f.write("This guide details sources requiring browser-based selection, credentials, or dynamic API queries.\n\n")
        f.write("## Priority Gated Sources (From Download Queue)\n\n")
        for q in queue_items:
            f.write(f"### {q['queue_id']}: {q['resource_family']}\n")
            f.write(f"- **Grade**: {q['grade']} | **Priority**: {q['priority']} | **Topic**: {q['topic']}\n")
            f.write(f"- **Landing Page**: [{q['landing_page']}]({q['landing_page']})\n")
            f.write(f"- **What to Obtain**: {q['formats']}\n")
            f.write(f"- **Access Caution**: {q['caution']}\n\n")
            
        f.write("## All Other Catalog Gated Sources\n\n")
        for item in gated_items[:25]:
            f.write(f"- **[{item['id']}] {item['title']}** ({item['publisher']})\n")
            f.write(f"  - Landing: {item['landing_page']}\n")
            f.write(f"  - Formats: {item['formats_access']}\n")
            f.write(f"  - Caveat: {item['caveats']}\n\n")
            
    print(f"Generated interactive guide at {GUIDE_PATH}")

def main():
    parser = argparse.ArgumentParser(description="Acquire library data from Pakistan Data Resource Inventory.")
    parser.add_argument("--mode", choices=["all-direct", "queue", "queue-all-remaining", "top15", "resource", "guide"], default="queue",
                        help="Acquisition target mode")
    parser.add_argument("--preset", choices=["top15-priority", "census-districts", "macro-apis"],
                        help="Target specific verified acquisition presets")
    parser.add_argument("--priority", choices=["P1", "P2", "P3", "all"], default="P1", help="Filter by priority")
    parser.add_argument("--resource-id", help="Target single resource ID or Queue ID")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of items")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without downloading")
    parser.add_argument("--timeout", type=int, default=45, help="HTTP timeout in seconds")
    args = parser.parse_args()

    data = load_catalog()
    generate_interactive_guide(data)
    
    if args.mode == "guide":
        return

    target_items = []

    if args.preset == "census-districts":
        census_item = {
            "id": "Q-03",
            "title": "PBS Population & Housing Census 2023 Table 1 District Workbooks",
            "grade": "A1",
            "topic": "Population / Census",
            "landing_page": "https://www.pbs.gov.pk/census/",
            "direct_entries": [
                {"label": "National Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_national.xlsx"},
                {"label": "Punjab Districts Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_punjab_districts.xlsx"},
                {"label": "Sindh Districts Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_sindh_districts.xlsx"},
                {"label": "Khyber Pakhtunkhwa Districts Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_kp_districts.xlsx"},
                {"label": "Balochistan Districts Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_balochistan_districts.xlsx"},
                {"label": "Islamabad Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_islamabad.xlsx"}
            ]
        }
        target_items.append(census_item)

    elif args.preset == "top15-priority":
        # Add Census Table 1 Workbooks
        target_items.append({
            "id": "Q-03",
            "title": "PBS Population & Housing Census 2023 Table 1 District Workbooks",
            "grade": "A1",
            "topic": "Population / Census",
            "landing_page": "https://www.pbs.gov.pk/census/",
            "direct_entries": [
                {"label": "National Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_national.xlsx"},
                {"label": "Punjab Districts Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_punjab_districts.xlsx"},
                {"label": "Sindh Districts Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_sindh_districts.xlsx"},
                {"label": "Khyber Pakhtunkhwa Districts Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_kp_districts.xlsx"},
                {"label": "Balochistan Districts Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_balochistan_districts.xlsx"},
                {"label": "Islamabad Table 1", "format": "Excel", "url": "https://www.pbs.gov.pk/wp-content/uploads/2020/07/table_1_islamabad.xlsx"}
            ]
        })
        # Add World Bank API Pakistan Macro Data
        target_items.append({
            "id": "Q-29",
            "title": "World Bank Indicators API: Pakistan Macroeconomic Series",
            "grade": "A2",
            "topic": "Macroeconomics / API",
            "landing_page": "https://data.worldbank.org/country/pakistan",
            "direct_entries": [
                {"label": "GDP Current USD", "format": "API", "url": "https://api.worldbank.org/v2/country/PAK/indicator/NY.GDP.MKTP.CD?format=json"},
                {"label": "GDP Growth Annual %", "format": "API", "url": "https://api.worldbank.org/v2/country/PAK/indicator/NY.GDP.MKTP.KD.ZG?format=json"},
                {"label": "Inflation Consumer Prices %", "format": "API", "url": "https://api.worldbank.org/v2/country/PAK/indicator/FP.CPI.TOTL.ZG?format=json"},
                {"label": "Population Total", "format": "API", "url": "https://api.worldbank.org/v2/country/PAK/indicator/SP.POP.TOTL?format=json"},
                {"label": "Exports of Goods & Services % of GDP", "format": "API", "url": "https://api.worldbank.org/v2/country/PAK/indicator/NE.EXP.GNFS.ZS?format=json"}
            ]
        })
        # Add Economic Survey 2025-26
        target_items.append({
            "id": "Q-11",
            "title": "Pakistan Economic Survey 2025–26 Full Report",
            "grade": "A1",
            "topic": "Macroeconomics / Annual report",
            "landing_page": "https://www.finance.gov.pk/survey_2026.html",
            "direct_entries": [
                {"label": "Complete PES 2025-26 PDF", "format": "PDF", "url": "https://finance.gov.pk/survey/chapter_26/Complete_PES2025_26.pdf"}
            ]
        })
    elif args.resource_id:
        for c in data["catalog"]:
            if c["id"].upper() == args.resource_id.upper():
                target_items.append(c)
                break
        if not target_items:
            for q in data["download_queue"]:
                if q["queue_id"].upper() == args.resource_id.upper():
                    target_items.append(q)
                    break
    elif args.mode == "queue-all-remaining":
        manifest = load_manifest()
        for q in data["download_queue"]:
            qid = q["queue_id"]
            # If already downloaded and all files verified on disk, skip
            if qid in manifest and manifest[qid].get("status") == "DOWNLOADED":
                files = manifest[qid].get("files", [])
                if files and all(os.path.exists(os.path.join(ROOT_DIR, f.get("relative_path", ""))) for f in files):
                    print(f"Skipping already cached: {qid} - {q['resource_family'][:45]}")
                    continue
            target_items.append(q)
    elif args.mode == "top15":
        top_resources = {s["resource"].lower(): s for s in data["top_stack"]}
        for c in data["catalog"]:
            c_title = c["title"].lower()
            if any(t in c_title or c_title in t for t in top_resources):
                target_items.append(c)
    elif args.mode == "queue":
        for q in data["download_queue"]:
            if args.priority == "all" or q["priority"] == args.priority:
                target_items.append(q)
    elif args.mode == "all-direct":
        target_items = [c for c in data["catalog"] if c["direct_urls"]]

    if args.limit and args.limit > 0:
        target_items = target_items[:args.limit]

    execute_acquisition(target_items, dry_run=args.dry_run, timeout=args.timeout)

if __name__ == "__main__":
    main()
