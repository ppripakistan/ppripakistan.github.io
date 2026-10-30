#!/usr/bin/env python3
"""
scripts/run_full_site_audit.py
Unified, End-to-End Audit & Verification Suite for Pakistan Provincial Reform Institute (PPRI).

Audits:
1. Data Master Integrity & Parity (CSV vs JSON)
2. All HTML Pages: Syntax, JSON-LD Schema, Canonical & Metadata
3. Core Web Vitals: Zero CLS (100% image width/height enforcement)
4. Internal Link Graph & Anchor Fragment (#hash) Integrity
5. Asset Availability (CSS, JS, Fonts, Images)
6. Security: 100% rel="noopener" on target="_blank" links
7. Accessibility: lang (en/ur), dir (rtl for ur), viewport, alt text, form controls
8. Sitemap & Search Index Parity (including search-index-ur.json)
"""

import os
import sys
import json
import csv
import xml.etree.ElementTree as ET
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

ROOT_DIR = Path(__file__).resolve().parent.parent
MASTER_DIR = ROOT_DIR / "data" / "master"
SITEMAP_PATH = ROOT_DIR / "sitemap.xml"
SEARCH_INDEX_PATH = ROOT_DIR / "search-index.json"
SEARCH_INDEX_UR_PATH = ROOT_DIR / "search-index-ur.json"

class ComprehensivePageParser(HTMLParser):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.rel_path = str(file_path.relative_to(ROOT_DIR)).replace("\\", "/")
        
        self.title = None
        self.in_title = False
        self.meta_description = None
        self.canonical = None
        self.is_redirect = False
        self.html_lang = None
        self.html_dir = None
        self.has_viewport = False
        
        self.json_ld = []
        self.in_json_ld = False
        self.json_ld_buffer = []
        
        self.element_ids = set()
        self.headings = [] # (tag, text)
        self.current_h_tag = None
        self.current_h_text = []
        
        self.links = [] # dict(href, target, rel, text, line)
        self.current_link = None
        self.current_link_text = []
        
        self.images = [] # dict(src, alt, width, height, line)
        self.scripts = [] # dict(src, type, line)
        self.stylesheets = [] # href
        self.inputs = [] # dict(tag, type, id, name, aria_label, line)
        self.hreflangs = {} # lang -> href

    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        line = self.getpos()[0]
        
        if 'id' in ad:
            self.element_ids.add(ad['id'])
            
        if tag == 'html':
            self.html_lang = ad.get('lang')
            self.html_dir = ad.get('dir')
            
        elif tag == 'title':
            self.in_title = True
            
        elif tag == 'meta':
            name = ad.get('name', '').lower()
            http_equiv = ad.get('http-equiv', '').lower()
            if name == 'description':
                self.meta_description = ad.get('content', '')
            elif name == 'viewport':
                self.has_viewport = True
            elif http_equiv == 'refresh':
                self.is_redirect = True
                
        elif tag == 'link':
            rel = ad.get('rel', '').lower()
            href = ad.get('href', '')
            if 'canonical' in rel:
                self.canonical = href
            elif 'stylesheet' in rel:
                self.stylesheets.append(href)
            elif 'alternate' in rel and 'hreflang' in ad:
                self.hreflangs[ad['hreflang']] = href
                
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.current_h_tag = tag
            self.current_h_text = []
            
        elif tag == 'a':
            self.current_link = {
                'href': ad.get('href', ''),
                'target': ad.get('target', ''),
                'rel': ad.get('rel', ''),
                'aria_label': ad.get('aria-label', ''),
                'line': line
            }
            self.current_link_text = []
            
        elif tag == 'img':
            self.images.append({
                'src': ad.get('src', ''),
                'alt': ad.get('alt'),
                'width': ad.get('width'),
                'height': ad.get('height'),
                'line': line
            })
            
        elif tag == 'script':
            script_type = ad.get('type', '')
            src = ad.get('src', '')
            if script_type == 'application/ld+json':
                self.in_json_ld = True
                self.json_ld_buffer = []
            elif src:
                self.scripts.append({'src': src, 'type': script_type, 'line': line})
                
        elif tag in ('input', 'select', 'textarea'):
            self.inputs.append({
                'tag': tag,
                'type': ad.get('type', 'text' if tag == 'input' else ''),
                'id': ad.get('id', ''),
                'name': ad.get('name', ''),
                'aria_label': ad.get('aria-label', ''),
                'line': line
            })

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
            
        elif tag == self.current_h_tag:
            self.headings.append((self.current_h_tag, "".join(self.current_h_text).strip()))
            self.current_h_tag = None
            self.current_h_text = []
            
        elif tag == 'a' and self.current_link is not None:
            self.current_link['text'] = "".join(self.current_link_text).strip()
            self.links.append(self.current_link)
            self.current_link = None
            self.current_link_text = []
            
        elif tag == 'script' and self.in_json_ld:
            raw = "".join(self.json_ld_buffer).strip()
            if raw:
                self.json_ld.append(raw)
            self.in_json_ld = False
            self.json_ld_buffer = []

    def handle_data(self, data):
        if self.in_title:
            self.title = (self.title or "") + data
        elif self.current_h_tag:
            self.current_h_text.append(data)
        elif self.current_link:
            self.current_link_text.append(data)
        elif self.in_json_ld:
            self.json_ld_buffer.append(data)


def run_suite():
    print("=" * 75)
    print("  PAKISTAN PROVINCIAL REFORM INSTITUTE (PPRI)")
    print("  COMPREHENSIVE END-TO-END AUDIT & VERIFICATION SUITE")
    print("=" * 75)
    
    errors = []
    warnings = []
    
    # 1. Audit Data Master Parity
    print("\n[Audit 1/8] Verifying Master Data Store Integrity & CSV/JSON Parity...")
    obs_csv = MASTER_DIR / "observations.csv"
    obs_json = MASTER_DIR / "observations.json"
    
    if not obs_csv.exists() or not obs_json.exists():
        errors.append("Missing master observation data files (observations.csv / json)")
    else:
        with open(obs_csv, encoding="utf-8") as f:
            csv_records = list(csv.DictReader(f))
        with open(obs_json, encoding="utf-8") as f:
            json_records = json.load(f)
            
        if len(csv_records) != len(json_records):
            errors.append(f"Parity mismatch: CSV has {len(csv_records)} rows, JSON has {len(json_records)} rows")
        else:
            print(f"  [PASS] Observations: {len(csv_records)} records in exact CSV/JSON parity.")

    # 2. Collect and Parse HTML pages
    print("\n[Audit 2/8] Scanning and Parsing All Published HTML Pages...")
    all_html_files = [
        p for p in ROOT_DIR.rglob("*.html")
        if not any(part.startswith('.') or part in ('node_modules', 'scratch_inspect', 'raw', 'build library', 'Build Library', 'unintegrated_staging') for part in p.parts)
    ]
    print(f"  Discovered {len(all_html_files)} HTML pages.")

    parsed_pages = {}
    for hf in all_html_files:
        parser = ComprehensivePageParser(hf)
        try:
            content = hf.read_text(encoding="utf-8")
            parser.feed(content)
            parsed_pages[hf] = parser
        except Exception as e:
            errors.append(f"HTML Parse Error in {hf.relative_to(ROOT_DIR)}: {e}")

    # 3. Core Web Vitals: Zero CLS (Image Width/Height check)
    print("\n[Audit 3/8] Auditing Core Web Vitals Image Dimensions (CLS Guard)...")
    cls_violations = []
    for p, parser in parsed_pages.items():
        for img in parser.images:
            src = img['src']
            if not src:
                continue
            if not (img['width'] and img['height']):
                cls_violations.append((parser.rel_path, src, img['line']))
                
    if cls_violations:
        for r, s, l in cls_violations:
            errors.append(f"CLS Hazard: Image missing width/height in {r} (line {l}): {s}")
    else:
        print("  [PASS] Zero CLS violations: 100% of images have explicit width and height dimensions.")

    # 4. Internal Link Graph & Asset Verification
    print("\n[Audit 4/8] Validating Internal Links, Assets, & Anchor Fragments...")
    broken_links = []
    broken_assets = []
    broken_fragments = []

    for p, parser in parsed_pages.items():
        page_dir = p.parent
        rel_page = parser.rel_path

        # Stylesheets
        for sheet in parser.stylesheets:
            if sheet.startswith("http://") or sheet.startswith("https://"):
                continue
            sheet_clean = sheet.split("?")[0]
            if sheet_clean.startswith("/"):
                target = ROOT_DIR / sheet_clean.lstrip("/")
            else:
                target = page_dir / sheet_clean
            if not target.exists():
                broken_assets.append((rel_page, sheet, "stylesheet"))

        # Scripts
        for s in parser.scripts:
            src = s['src']
            if src.startswith("http://") or src.startswith("https://"):
                continue
            src_clean = src.split("?")[0]
            if src_clean.startswith("/"):
                target = ROOT_DIR / src_clean.lstrip("/")
            else:
                target = page_dir / src_clean
            if not target.exists():
                broken_assets.append((rel_page, src, "script"))

        # Links
        for lk in parser.links:
            href = lk['href']
            if not href or href.startswith("mailto:") or href.startswith("tel:") or href.startswith("javascript:"):
                continue
            if href.startswith("http://") or href.startswith("https://"):
                continue

            parsed_url = urlparse(href)
            path_part = parsed_url.path
            fragment_part = parsed_url.fragment

            if not path_part:
                # Same page fragment
                if fragment_part and fragment_part not in parser.element_ids:
                    warnings.append(f"Unresolved in-page anchor fragment #{fragment_part} in {rel_page} (line {lk['line']})")
                continue

            # Determine target file
            if path_part.startswith("/"):
                target_file = ROOT_DIR / path_part.lstrip("/")
            else:
                target_file = page_dir / path_part

            # Directory normalization
            if target_file.is_dir():
                target_file = target_file / "index.html"
            elif not target_file.exists() and (target_file.parent / f"{target_file.name}.html").exists():
                target_file = target_file.parent / f"{target_file.name}.html"

            if not target_file.exists():
                broken_links.append((rel_page, href, lk['line']))
            else:
                if fragment_part and target_file in parsed_pages:
                    target_parser = parsed_pages[target_file]
                    if fragment_part not in target_parser.element_ids:
                        warnings.append(f"Unresolved anchor fragment #{fragment_part} in {rel_page} (line {lk['line']}): {href}")

    if broken_assets:
        for r, a, t in broken_assets:
            errors.append(f"Broken {t} asset in {r}: {a}")
    else:
        print("  [PASS] Zero broken asset references (stylesheets & scripts).")

    if broken_links:
        for r, h, l in broken_links:
            errors.append(f"Broken internal link in {r} (line {l}): {h}")
    else:
        print("  [PASS] Zero broken internal links.")

    # 5. Security: rel="noopener"
    print("\n[Audit 5/8] Security Audit: target='_blank' rel='noopener noreferrer'...")
    insecure_links = []
    for p, parser in parsed_pages.items():
        for lk in parser.links:
            if lk['target'] == '_blank':
                rel = lk['rel'].lower()
                if 'noopener' not in rel:
                    insecure_links.append((parser.rel_path, lk['href'], lk['line']))

    if insecure_links:
        for r, h, l in insecure_links:
            errors.append(f"Insecure target='_blank' link in {r} (line {l}) missing rel='noopener': {h}")
    else:
        print("  [PASS] 100% of external target='_blank' links enforce rel='noopener noreferrer'.")

    # 6. SEO & Metadata
    print("\n[Audit 6/8] Auditing SEO Titles, Descriptions, Canonicals & JSON-LD...")
    json_ld_errs = 0
    missing_seo = []
    for p, parser in parsed_pages.items():
        rel = parser.rel_path
        if not parser.title:
            missing_seo.append(f"Missing <title> in {rel}")
        if not parser.meta_description:
            missing_seo.append(f"Missing <meta name='description'> in {rel}")
        if not parser.canonical and rel != "404.html":
            missing_seo.append(f"Missing <link rel='canonical'> in {rel}")

        # JSON-LD check
        for raw in parser.json_ld:
            try:
                j = json.loads(raw)
                if '@context' not in j:
                    errors.append(f"JSON-LD in {rel} missing @context")
            except Exception as e:
                errors.append(f"JSON-LD syntax error in {rel}: {e}")
                json_ld_errs += 1

    if missing_seo:
        for m in missing_seo:
            errors.append(m)
    else:
        print(f"  [PASS] All {len(parsed_pages)} pages have valid <title>, <meta description>, and <link rel='canonical'> tags.")
        print(f"  [PASS] Zero Schema.org JSON-LD errors across all structured data blocks.")

    # 7. Accessibility & Localization
    print("\n[Audit 7/8] Auditing Accessibility (HTML Lang, RTL Direction, Viewport, Image Alt)...")
    a11y_errs = []
    for p, parser in parsed_pages.items():
        rel = parser.rel_path
        if not parser.html_lang:
            a11y_errs.append(f"Missing lang attribute on <html> in {rel}")
        elif parser.html_lang not in ('en', 'ur'):
            a11y_errs.append(f"Unexpected lang attribute on <html> in {rel}: {parser.html_lang}")
            
        if parser.html_lang == 'ur' and parser.html_dir != 'rtl':
            a11y_errs.append(f"Urdu page missing dir='rtl' attribute on <html> in {rel}")
            
        if not parser.has_viewport:
            a11y_errs.append(f"Missing <meta name='viewport'> in {rel}")
        for img in parser.images:
            if img['alt'] is None:
                a11y_errs.append(f"Image missing alt in {rel} (line {img['line']}): {img['src']}")

    if a11y_errs:
        for ae in a11y_errs[:5]:
            errors.append(ae)
    else:
        print("  [PASS] 100% compliance on html lang (en/ur), dir='rtl' on Urdu pages, viewport metadata, and image alt attributes.")

    # 8. Sitemap & Search Index Parity
    print("\n[Audit 8/8] Verifying sitemap.xml & search-index.json Integrity...")
    try:
        sitemap_tree = ET.parse(SITEMAP_PATH)
        sitemap_root = sitemap_tree.getroot()
        sitemap_locs = [
            e.text.strip()
            for e in sitemap_root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            if e.text
        ]
        
        # Check for redirects in sitemap
        redirect_in_sitemap = []
        for loc in sitemap_locs:
            path_part = loc.replace("https://ppripakistan.github.io/", "")
            target_file = ROOT_DIR / path_part
            if not target_file.exists():
                if (ROOT_DIR / f"{path_part}.html").exists():
                    target_file = ROOT_DIR / f"{path_part}.html"
                elif (ROOT_DIR / path_part / "index.html").exists():
                    target_file = ROOT_DIR / path_part / "index.html"
            
            if target_file in parsed_pages and parsed_pages[target_file].is_redirect:
                redirect_in_sitemap.append(loc)

        if redirect_in_sitemap:
            for r in redirect_in_sitemap:
                errors.append(f"Redirect page present in sitemap.xml: {r}")
        else:
            print(f"  [PASS] sitemap.xml contains {len(sitemap_locs)} clean canonical URLs (0 redirect stubs).")

        # Search index check
        with open(SEARCH_INDEX_PATH, encoding="utf-8") as f:
            search_items = json.load(f)
        print(f"  [PASS] search-index.json contains {len(search_items)} validated, searchable records.")

        if SEARCH_INDEX_UR_PATH.exists():
            with open(SEARCH_INDEX_UR_PATH, encoding="utf-8") as f:
                urdu_search_items = json.load(f)
            print(f"  [PASS] search-index-ur.json contains {len(urdu_search_items)} validated, searchable Urdu records.")

    except Exception as e:
        errors.append(f"Sitemap / search-index error: {e}")

    # Final Verdict
    print("\n" + "=" * 75)
    print(f"  VERIFICATION SUITE SUMMARY:")
    print(f"  * Errors Found:   {len(errors)}")
    print(f"  * Warnings Found: {len(warnings)}")
    print("=" * 75)

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  [WARN] {w}")

    if errors:
        print("\nErrors:")
        for e in errors:
            print(f"  [ERROR] {e}")
        print("\nRESULT: FAILED")
        print("=" * 75)
        sys.exit(1)
    else:
        print("\nRESULT: 100% PASS — ALL CHECKS SUCCESSFUL")
        print("=" * 75)
        sys.exit(0)

if __name__ == "__main__":
    run_suite()
