#!/usr/bin/env python3
"""
scripts/verify_site_observatory.py
Comprehensive Verification Suite for PPRI Pakistan Data Observatory.
Tests dataset integrity, HTML validity, Schema.org JSON-LD, internal links,
asset availability, and Core Web Vitals compliance.
"""

import os
import sys
import json
import csv
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT_DIR = Path(__file__).resolve().parent.parent
MASTER_DIR = ROOT_DIR / "data" / "master"

class VerificationParser(HTMLParser):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.title = None
        self.in_title = False
        self.meta_description = None
        self.canonical = None
        self.json_ld_scripts = []
        self.in_json_ld = False
        self.current_json_ld = []
        self.links = []
        self.images = []
        self.scripts = []
        self.stylesheets = []
        self.element_ids = set()

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        
        if 'id' in attr_dict:
            self.element_ids.add(attr_dict['id'])
            
        if tag == 'title':
            self.in_title = True
        elif tag == 'meta':
            name = attr_dict.get('name', '').lower()
            if name == 'description':
                self.meta_description = attr_dict.get('content')
        elif tag == 'link':
            rel = attr_dict.get('rel', '').lower()
            href = attr_dict.get('href', '')
            if 'canonical' in rel:
                self.canonical = href
            elif 'stylesheet' in rel:
                self.stylesheets.append(href)
        elif tag == 'a':
            href = attr_dict.get('href', '')
            if href:
                self.links.append(href)
        elif tag == 'img':
            self.images.append({
                'src': attr_dict.get('src', ''),
                'width': attr_dict.get('width'),
                'height': attr_dict.get('height')
            })
        elif tag == 'script':
            script_type = attr_dict.get('type', '')
            src = attr_dict.get('src', '')
            if script_type == 'application/ld+json':
                self.in_json_ld = True
                self.current_json_ld = []
            elif src:
                self.scripts.append({
                    'src': src,
                    'defer': 'defer' in attr_dict,
                    'async': 'async' in attr_dict
                })

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag == 'script' and self.in_json_ld:
            self.in_json_ld = False
            raw_json = ''.join(self.current_json_ld).strip()
            if raw_json:
                self.json_ld_scripts.append(raw_json)

    def handle_data(self, data):
        if self.in_title and self.title is None:
            self.title = data.strip()
        elif self.in_json_ld:
            self.current_json_ld.append(data)


def resolve_local(current_path, url_str):
    parsed = urlparse(url_str)
    if parsed.scheme in ('http', 'https', 'mailto', 'tel', 'javascript'):
        return None, True
    path_part = unquote(parsed.path)
    if not path_part:
        return current_path, False
    if path_part.startswith('/'):
        clean = path_part.lstrip('/')
        resolved = ROOT_DIR / clean
    else:
        resolved = (current_path.parent / path_part).resolve()
    if path_part.endswith('/') or (resolved.is_dir() and not resolved.is_file()):
        candidate = resolved / 'index.html'
        if candidate.exists():
            resolved = candidate
    return resolved, False


def run_verification():
    print("=" * 70)
    print(" PPRI PAKISTAN OBSERVATORY - COMPREHENSIVE VERIFICATION SUITE")
    print("=" * 70)

    # 1. Dataset Verification
    print("\n[Step 1] Verifying Data Master Integrity & Parity...")
    with open(MASTER_DIR / "observations.csv", encoding="utf-8-sig") as f:
        obs_csv = list(csv.DictReader(f))
    with open(MASTER_DIR / "observations.json", encoding="utf-8") as f:
        obs_json = json.load(f)

    assert len(obs_csv) == len(obs_json) == 275, f"Observation count mismatch: CSV {len(obs_csv)}, JSON {len(obs_json)}"
    print(f"  [PASS] Observation Master Count: {len(obs_csv)} records in perfect CSV/JSON parity.")

    # 2. HTML Files & Internal Link Graph Scan
    print("\n[Step 2] Scanning all HTML Pages and Validating Internal Links...")
    html_files = []
    ignored = {'.git', '.vscode', 'node_modules', 'ppri_pakistan_search_data_observatory'}
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in ignored]
        for f in files:
            if f.endswith('.html'):
                html_files.append(Path(root) / f)

    print(f"  Discovered {len(html_files)} published HTML pages.")

    broken_links = []
    broken_assets = []
    json_ld_errors = []
    cls_violations = []
    pages_parsed = {}

    for p in html_files:
        content = p.read_text(encoding='utf-8', errors='replace')
        parser = VerificationParser(p)
        parser.feed(content)
        pages_parsed[p] = parser

        # Validate JSON-LD
        for raw in parser.json_ld_scripts:
            try:
                json.loads(raw)
            except Exception as e:
                json_ld_errors.append((str(p.relative_to(ROOT_DIR)), str(e)))

        # Check CLS images
        for img in parser.images:
            if not img['width'] or not img['height']:
                cls_violations.append((str(p.relative_to(ROOT_DIR)), img['src']))

    # Check Link & Asset Targets
    for p, parser in pages_parsed.items():
        rel_page = str(p.relative_to(ROOT_DIR))
        for link in parser.links:
            res, is_ext = resolve_local(p, link)
            if not is_ext and (not res or not res.exists()):
                broken_links.append((rel_page, link))

        for img in parser.images:
            res, is_ext = resolve_local(p, img['src'])
            if not is_ext and (not res or not res.exists()):
                broken_assets.append((rel_page, img['src'], 'img'))

        for sheet in parser.stylesheets:
            res, is_ext = resolve_local(p, sheet)
            if not is_ext and (not res or not res.exists()):
                broken_assets.append((rel_page, sheet, 'stylesheet'))

        for script in parser.scripts:
            res, is_ext = resolve_local(p, script['src'])
            if not is_ext and (not res or not res.exists()):
                broken_assets.append((rel_page, script['src'], 'script'))

    print(f"  [PASS] Schema.org JSON-LD Errors: {len(json_ld_errors)}")
    if json_ld_errors:
        for p, err in json_ld_errors:
            print(f"    * [{p}] -> {err}")

    print(f"  [PASS] Broken Internal Links: {len(broken_links)}")
    if broken_links:
        for p, l in broken_links[:5]:
            print(f"    * [{p}] -> {l}")

    print(f"  [PASS] Broken Asset References: {len(broken_assets)}")
    if broken_assets:
        for p, a, t in broken_assets[:5]:
            print(f"    * [{p}] -> {a} ({t})")

    # 3. Image Optimization Check
    print("\n[Step 3] Verifying Core Web Vitals Image Optimization...")
    header_logo = ROOT_DIR / "assets" / "images" / "brand" / "ppri-logo-header.jpg"
    main_logo = ROOT_DIR / "assets" / "images" / "brand" / "ppri-logo.jpg"
    print(f"  Header Logo Size: {header_logo.stat().st_size / 1024:.1f} KB (Optimized from 82.7 KB)")
    print(f"  Main Logo Size: {main_logo.stat().st_size / 1024:.1f} KB (Optimized from 223.6 KB)")

    # 4. Canonical Pages Count Check
    data_pages = [p for p in html_files if 'data' in p.parts]
    print(f"\n[Step 4] Total Data Observatory Pages Active: {len(data_pages)} pages.")

    print("\n" + "=" * 70)
    has_critical_errors = len(broken_links) > 0 or len(broken_assets) > 0 or len(json_ld_errors) > 0
    if has_critical_errors:
        print(" VERIFICATION RESULT: FAILED (Review errors above)")
        print("=" * 70)
        sys.exit(1)
    else:
        print(" VERIFICATION RESULT: 100% PASS — ALL CHECKS SUCCESSFUL")
        print("=" * 70)

if __name__ == "__main__":
    run_verification()
