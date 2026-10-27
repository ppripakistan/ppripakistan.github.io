#!/usr/bin/env python3
"""
IndexNow URL Submission Script
==============================
Automatically submits canonical URLs to search engines via the IndexNow protocol
(supported by Microsoft Bing, Yandex, Naver, Seznam, and other participating engines).

Usage:
    # Submit all URLs from sitemap.xml (sorted by latest modification date & priority first):
    python scripts/submit_indexnow.py

    # Submit only the latest updated pages and observatory hubs:
    python scripts/submit_indexnow.py --latest

    # Submit specific URLs:
    python scripts/submit_indexnow.py https://ppripakistan.github.io/knowledge-library/

    # Validate payload without sending network requests:
    python scripts/submit_indexnow.py --dry-run
    python scripts/submit_indexnow.py --latest --dry-run
"""

import sys
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path

# Configuration
PRIMARY_ENDPOINT = "https://api.indexnow.org/indexnow"
FALLBACK_ENDPOINTS = [
    "https://www.bing.com/indexnow",
    "https://indexnow.org",
]
SITE_HOST = "ppripakistan.github.io"
INDEXNOW_KEY = "1041249209c94dfd929a97ff432b4437"
KEY_LOCATION = "https://ppripakistan.github.io/1041249209c94dfd929a97ff432b4437.txt"

ROOT_DIR = Path(__file__).resolve().parent.parent
SITEMAP_FILE = ROOT_DIR / "sitemap.xml"
BATCH_SIZE = 10000  # IndexNow protocol limit per request

# High-priority latest observatory hubs & canonical assets
LATEST_CORE_URLS = [
    "https://ppripakistan.github.io/knowledge-library/",
    "https://ppripakistan.github.io/data/centre.html",
    "https://ppripakistan.github.io/data/population/",
    "https://ppripakistan.github.io/data/economy/",
    "https://ppripakistan.github.io/data/living-standards/",
    "https://ppripakistan.github.io/data/public-finance/",
    "https://ppripakistan.github.io/data/education/",
    "https://ppripakistan.github.io/data/health/",
    "https://ppripakistan.github.io/data/digital-access/",
    "https://ppripakistan.github.io/data/compare/",
    "https://ppripakistan.github.io/data/downloads/",
    "https://ppripakistan.github.io/data/methodology/",
    "https://ppripakistan.github.io/",
    "https://ppripakistan.github.io/directory.html",
    "https://ppripakistan.github.io/research/",
    "https://ppripakistan.github.io/provinces/",
    "https://ppripakistan.github.io/scenarios/",
]


def extract_urls_from_sitemap(sitemap_path: Path, latest_only: bool = False) -> list:
    """Reads sitemap.xml and returns canonical URLs sorted by lastmod & priority."""
    if not sitemap_path.is_file():
        raise FileNotFoundError(f"Sitemap file not found at: {sitemap_path}")

    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    entries = []
    seen = set()

    # Find all <url> blocks
    for url_el in root.findall(".//{*}url"):
        loc_el = url_el.find("{*}loc")
        if loc_el is None or not loc_el.text:
            continue
        loc = loc_el.text.strip()
        if not loc or loc in seen:
            continue
        seen.add(loc)

        lm_el = url_el.find("{*}lastmod")
        pr_el = url_el.find("{*}priority")

        lastmod = lm_el.text.strip() if (lm_el is not None and lm_el.text) else "1970-01-01"
        try:
            priority = float(pr_el.text.strip()) if (pr_el is not None and pr_el.text) else 0.5
        except ValueError:
            priority = 0.5

        entries.append({
            "loc": loc,
            "lastmod": lastmod,
            "priority": priority,
        })

    if not entries:
        return []

    # Sort descending by lastmod, then by priority
    entries.sort(key=lambda x: (x["lastmod"], x["priority"]), reverse=True)

    if latest_only:
        # Determine the latest date present in sitemap
        latest_date = entries[0]["lastmod"]
        print(f"[FILTER] Selecting URLs updated on latest date ({latest_date}) or in latest core hubs...")

        latest_set = set(LATEST_CORE_URLS)
        filtered = [
            e["loc"] for e in entries
            if e["lastmod"] == latest_date or e["loc"] in latest_set
        ]

        # Guarantee all LATEST_CORE_URLS are included at the top
        ordered = []
        seen_filtered = set()
        for u in LATEST_CORE_URLS:
            if u not in seen_filtered:
                seen_filtered.add(u)
                ordered.append(u)
        for u in filtered:
            if u not in seen_filtered:
                seen_filtered.add(u)
                ordered.append(u)
        return ordered

    # Default: return all URLs with newest/highest-priority first
    ordered_all = []
    seen_all = set()
    for u in LATEST_CORE_URLS:
        if u not in seen_all:
            seen_all.add(u)
            ordered_all.append(u)
    for e in entries:
        if e["loc"] not in seen_all:
            seen_all.add(e["loc"])
            ordered_all.append(e["loc"])

    return ordered_all


def submit_batch(urls: list, dry_run: bool = False) -> bool:
    """Constructs the IndexNow JSON payload and sends an HTTP POST request."""
    payload = {
        "host": SITE_HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }

    if dry_run:
        print(f"[DRY-RUN] Ready to submit {len(urls)} URLs to IndexNow API")
        sample_preview = urls[:5]
        print(f"[DRY-RUN] First {len(sample_preview)} URLs in batch:")
        for idx, u in enumerate(sample_preview, 1):
            print(f"  {idx}. {u}")
        if len(urls) > 5:
            print(f"  ... and {len(urls) - 5} more URLs.")
        print(f"[DRY-RUN] Sample payload structure:\n{json.dumps({**payload, 'urlList': sample_preview}, indent=2)}")
        return True

    json_data = json.dumps(payload).encode("utf-8")
    endpoints = [PRIMARY_ENDPOINT] + FALLBACK_ENDPOINTS

    for endpoint in endpoints:
        print(f"[HTTP POST] Submitting {len(urls)} URLs to {endpoint}...")
        request = urllib.request.Request(
            url=endpoint,
            data=json_data,
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "User-Agent": f"IndexNowSubmitter/1.0 (+https://{SITE_HOST}/)",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                status = response.status
                if status == 200:
                    print(f"[SUCCESS] HTTP 200 OK: {len(urls)} URLs successfully submitted to {endpoint}.")
                    return True
                elif status == 202:
                    print(f"[SUCCESS] HTTP 202 Accepted: {len(urls)} URLs accepted for processing by {endpoint}.")
                    return True
                else:
                    print(f"[INFO] HTTP {status}: Endpoint {endpoint} returned unexpected status code.")
                    return True

        except urllib.error.HTTPError as error:
            status = error.code
            if status == 400:
                print(f"[ERROR] HTTP 400 Bad Request at {endpoint}: Invalid format, missing parameters, or invalid host.", file=sys.stderr)
            elif status == 403:
                print(f"[ERROR] HTTP 403 Forbidden at {endpoint}: Key is invalid or not found at keyLocation URL.", file=sys.stderr)
            elif status == 422:
                print(f"[ERROR] HTTP 422 Unprocessable Entity at {endpoint}: URLs do not belong to host or key does not match schema.", file=sys.stderr)
            elif status == 429:
                print(f"[ERROR] HTTP 429 Too Many Requests at {endpoint}: Rate limit exceeded.", file=sys.stderr)
            else:
                print(f"[ERROR] HTTP {status} {error.reason} at {endpoint}: Failed to submit URLs.", file=sys.stderr)
            # Try next endpoint if available
            continue

        except urllib.error.URLError as error:
            print(f"[ERROR] Network error connecting to {endpoint}: {error.reason}", file=sys.stderr)
            continue

    return False


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    latest_only = "--latest" in args or "-l" in args

    # Extract any explicit URLs provided in CLI arguments
    explicit_urls = [
        arg for arg in args
        if arg.startswith("http://") or arg.startswith("https://")
    ]

    if explicit_urls:
        print(f"[TARGET] Submitting {len(explicit_urls)} explicitly specified URL(s)...")
        urls = explicit_urls
    else:
        print(f"Reading canonical sitemap from: {SITEMAP_FILE}")
        try:
            urls = extract_urls_from_sitemap(SITEMAP_FILE, latest_only=latest_only)
        except Exception as exc:
            print(f"[ERROR] Could not parse sitemap: {exc}", file=sys.stderr)
            sys.exit(1)

    if not urls:
        print("[WARNING] No URLs found to submit.")
        sys.exit(0)

    mode_label = "Latest priority URLs" if latest_only else ("Explicitly specified URLs" if explicit_urls else "All canonical sitemap URLs")
    print(f"[INDEXNOW] Prepared {len(urls)} URLs ({mode_label})")

    # Split into batches within IndexNow's 10,000 URL limit
    success = True
    for i in range(0, len(urls), BATCH_SIZE):
        batch = urls[i : i + BATCH_SIZE]
        print(f"\n--- Submitting Batch {i // BATCH_SIZE + 1} ({len(batch)} URLs) ---")
        if not submit_batch(batch, dry_run=dry_run):
            success = False

    if success:
        print("\n[COMPLETE] All IndexNow submissions finished successfully.")
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
