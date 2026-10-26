#!/usr/bin/env python3
"""
IndexNow URL Submission Script
==============================
Automatically extracts URLs from sitemap.xml and submits them to the IndexNow API.

Usage:
    # Run URL submission:
    python scripts/submit_indexnow.py

    # Optional dry-run (validates sitemap and previews payload without sending):
    python scripts/submit_indexnow.py --dry-run
"""

import sys
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path

# Configuration
ENDPOINT = "https://indexnow.org"
SITE_HOST = "ppripakistan.github.io"
INDEXNOW_KEY = "1041249209c94dfd929a97ff432b4437"
KEY_LOCATION = "https://ppripakistan.github.io/1041249209c94dfd929a97ff432b4437.txt"

ROOT_DIR = Path(__file__).resolve().parent.parent
SITEMAP_FILE = ROOT_DIR / "sitemap.xml"
BATCH_SIZE = 10000  # IndexNow protocol limit per request


def extract_urls_from_sitemap(sitemap_path: Path) -> list:
    """Reads sitemap.xml and extracts all canonical URLs."""
    if not sitemap_path.is_file():
        raise FileNotFoundError(f"Sitemap file not found at: {sitemap_path}")

    tree = ET.parse(sitemap_path)
    root = tree.getroot()

    # Match all <loc> tags regardless of XML namespace
    raw_urls = [elem.text.strip() for elem in root.findall(".//{*}loc") if elem.text]

    # Deduplicate while preserving original order
    seen = set()
    unique_urls = []
    for url in raw_urls:
        if url and url not in seen:
            seen.add(url)
            unique_urls.append(url)

    return unique_urls


def submit_batch(urls: list, dry_run: bool = False) -> bool:
    """Constructs the IndexNow JSON payload and sends an HTTP POST request."""
    payload = {
        "host": SITE_HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }

    if dry_run:
        print(f"[DRY-RUN] Ready to submit {len(urls)} URLs to {ENDPOINT}")
        print(f"[DRY-RUN] Sample payload (first 3 URLs):\n{json.dumps({**payload, 'urlList': urls[:3]}, indent=2)}")
        return True

    json_data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url=ENDPOINT,
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
                print(f"[SUCCESS] HTTP 200 OK: Successfully submitted {len(urls)} URLs to IndexNow.")
                return True
            elif status == 202:
                print(f"[SUCCESS] HTTP 202 Accepted: {len(urls)} URLs accepted for processing (key pending validation).")
                return True
            else:
                print(f"[INFO] HTTP {status}: IndexNow responded with unexpected status code.")
                return True

    except urllib.error.HTTPError as error:
        status = error.code
        if status == 400:
            print(f"[ERROR] HTTP 400 Bad Request: Invalid format, missing parameters, or invalid host.", file=sys.stderr)
        elif status == 403:
            print(f"[ERROR] HTTP 403 Forbidden: Key is invalid or not found at keyLocation URL.", file=sys.stderr)
        elif status == 422:
            print(f"[ERROR] HTTP 422 Unprocessable Entity: URLs do not belong to host or key does not match schema.", file=sys.stderr)
        elif status == 429:
            print(f"[ERROR] HTTP 429 Too Many Requests: Rate limit exceeded (request marked as spam).", file=sys.stderr)
        else:
            print(f"[ERROR] HTTP {status} {error.reason}: Failed to submit URLs.", file=sys.stderr)
        return False

    except urllib.error.URLError as error:
        print(f"[ERROR] Network error connecting to {ENDPOINT}: {error.reason}", file=sys.stderr)
        return False


def main():
    dry_run = "--dry-run" in sys.argv

    print(f"Reading sitemap from: {SITEMAP_FILE}")
    try:
        urls = extract_urls_from_sitemap(SITEMAP_FILE)
    except Exception as exc:
        print(f"[ERROR] Could not parse sitemap: {exc}", file=sys.stderr)
        sys.exit(1)

    if not urls:
        print("[WARNING] No URLs found in sitemap.xml. Nothing to submit.")
        sys.exit(0)

    print(f"Discovered {len(urls)} URLs in sitemap.xml")

    # Split into batches within IndexNow's 10,000 URL limit
    success = True
    for i in range(0, len(urls), BATCH_SIZE):
        batch = urls[i : i + BATCH_SIZE]
        print(f"Submitting batch {i // BATCH_SIZE + 1} ({len(batch)} URLs)...")
        if not submit_batch(batch, dry_run=dry_run):
            success = False

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
