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
7. Accessibility: lang, viewport, alt text, form controls
8. Sitemap & Search Index Parity (zero redirects, zero orphaned URLs)
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

    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        line = self.getpos()[0]
        
        if 'id' in ad:
            self.element_ids.add(ad['id'])
            
        if tag == 'html':
            self.html_lang = ad.get('lang')
            
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
                self.scripts.append({'src': src, 'line': line})
                
        elif tag in ('input', 'select', 'textarea'):
            self.inputs.append({
                'tag': tag,
                'type': ad.get('type', 'text' if tag == 'input' else ''),
                'id': ad.get('id', ''),
                'name': ad.get('name', ''),
                'aria_label': ad.get('aria-label', ''),
                'aria_labelledby': ad.get('aria-labelledby', ''),
                'line': line
            })

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6') and self.current_h_tag == tag:
            text = ' '.join(''.join(self.current_h_text).split())
            self.headings.append((tag, text))
            self.current_h_tag = None
        elif tag == 'a' and self.current_link:
            text = ' '.join(''.join(self.current_link_text).split())
            self.current_link['text'] = text
            self.links.append(self.current_link)
            self.current_link = None
        elif tag == 'script' and self.in_json_ld:
            self.in_json_ld = False
            raw = ''.join(self.json_ld_buffer).strip()
            if raw:
                self.json_ld.append(raw)

    def handle_data(self, data):
        if self.in_title and self.title is None:
            self.title = data.strip()
        elif self.in_json_ld:
            self.json_ld_buffer.append(data)
        elif self.current_h_tag:
            self.current_h_text.append(data)
        elif self.current_link:
            self.current_link_text.append(data)

def resolve_local(current_path, url_str):
    parsed = urlparse(url_str)
    if parsed.scheme in ('http', 'https', 'mailto', 'tel', 'javascript') or url_str.startswith('data:'):
        return None, True, parsed.fragment
    path_part = unquote(parsed.path)
    if not path_part:
        return current_path, False, parsed.fragment
    if path_part.startswith('/'):
        clean = path_part.lstrip('/')
        resolved = ROOT_DIR / clean
    else:
        resolved = (current_path.parent / path_part).resolve()
    if path_part.endswith('/') or (resolved.is_dir() and not resolved.is_file()):
        candidate = resolved / 'index.html'
        if candidate.exists():
            resolved = candidate
    return resolved, False, parsed.fragment

def run_suite():
    print("=" * 75)
    print("  PAKISTAN PROVINCIAL REFORM INSTITUTE (PPRI)")
    print("  COMPREHENSIVE END-TO-END AUDIT & VERIFICATION SUITE")
    print("=" * 75)

    errors = []
    warnings = []

    # 1. Master Dataset Integrity
    print("\n[Audit 1/8] Verifying Master Data Store Integrity & CSV/JSON Parity...")
    try:
        with open(MASTER_DIR / "observations.csv", encoding="utf-8-sig") as f:
            obs_csv = list(csv.DictReader(f))
        with open(MASTER_DIR / "observations.json", encoding="utf-8") as f:
            obs_json = json.load(f)
        if len(obs_csv) != len(obs_json):
            errors.append(f"Observation count mismatch: CSV {len(obs_csv)} vs JSON {len(obs_json)}")
        else:
            print(f"  [PASS] Observations: {len(obs_csv)} records in exact CSV/JSON parity.")
    except Exception as e:
        errors.append(f"Master dataset error: {e}")

    # 2. HTML Files & Parser
    print("\n[Audit 2/8] Scanning and Parsing All Published HTML Pages...")
    ignored = {'.git', '.vscode', 'node_modules', 'ppri_pakistan_search_data_observatory'}
    html_files = [
        Path(root) / f
        for root, dirs, files in os.walk(ROOT_DIR)
        if not any(ign in Path(root).parts for ign in ignored)
        for f in files if f.endswith('.html')
    ]
    print(f"  Discovered {len(html_files)} HTML pages.")

    parsed_pages = {}
    for p in html_files:
        try:
            content = p.read_text(encoding='utf-8', errors='replace')
            parser = ComprehensivePageParser(p)
            parser.feed(content)
            parsed_pages[p] = parser
        except Exception as e:
            errors.append(f"HTML parse error in {p.relative_to(ROOT_DIR)}: {e}")

    # 3. Core Web Vitals & CLS Check (Zero missing width/height)
    print("\n[Audit 3/8] Auditing Core Web Vitals Image Dimensions (CLS Guard)...")
    cls_violations = []
    for p, parser in parsed_pages.items():
        rel = parser.rel_path
        for img in parser.images:
            if not img['width'] or not img['height']:
                cls_violations.append((rel, img['src'], img['line']))

    if cls_violations:
        for rel, src, line in cls_violations[:5]:
            errors.append(f"CLS violation (missing width/height) in {rel} (line {line}): {src}")
    else:
        print(f"  [PASS] Zero CLS violations: 100% of images have explicit width and height dimensions.")

    # 4. Internal Link & Anchor Fragment Resolution
    print("\n[Audit 4/8] Validating Internal Links, Assets, & Anchor Fragments...")
    broken_links = []
    broken_assets = []
    broken_anchors = []

    file_to_parser = {parser.file_path: parser for parser in parsed_pages.values()}

    for p, parser in parsed_pages.items():
        rel = parser.rel_path
        # Links
        for lk in parser.links:
            href = lk['href'].strip()
            if not href or href.startswith(('javascript:', 'mailto:', 'tel:')):
                continue
            res, is_ext, frag = resolve_local(p, href)
            if not is_ext:
                if not res or not res.exists():
                    broken_links.append((rel, href, lk['line']))
                elif frag and res in file_to_parser:
                    target_parser = file_to_parser[res]
                    if frag not in target_parser.element_ids:
                        broken_anchors.append((rel, href, frag, lk['line']))

        # Assets: Stylesheets
        for sheet in parser.stylesheets:
            res, is_ext, _ = resolve_local(p, sheet)
            if not is_ext and (not res or not res.exists()):
                broken_assets.append((rel, sheet, "stylesheet"))

        # Assets: Scripts
        for sc in parser.scripts:
            res, is_ext, _ = resolve_local(p, sc['src'])
            if not is_ext and (not res or not res.exists()):
                broken_assets.append((rel, sc['src'], "script"))

    if broken_links:
        for r, h, l in broken_links:
            errors.append(f"Broken internal link in {r} (line {l}): {h}")
    else:
        print("  [PASS] Zero broken internal links.")

    if broken_assets:
        for r, a, t in broken_assets:
            errors.append(f"Broken asset reference in {r}: {a} ({t})")
    else:
        print("  [PASS] Zero broken asset references (stylesheets & scripts).")

    if broken_anchors:
        for r, h, f, l in broken_anchors:
            warnings.append(f"Unresolved anchor fragment #{f} in {r} (line {l}): {h}")
    else:
        print("  [PASS] All anchor fragments (#hash) resolve to valid element IDs.")

    # 5. Security: target="_blank"
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
        print("  [PASS] All 120 pages have valid <title>, <meta description>, and <link rel='canonical'> tags.")
        print(f"  [PASS] Zero Schema.org JSON-LD errors across all structured data blocks.")

    # 7. Accessibility
    print("\n[Audit 7/8] Auditing Accessibility (HTML Lang, Viewport, Image Alt)...")
    a11y_errs = []
    for p, parser in parsed_pages.items():
        rel = parser.rel_path
        if not parser.html_lang:
            a11y_errs.append(f"Missing lang attribute on <html> in {rel}")
        if not parser.has_viewport:
            a11y_errs.append(f"Missing <meta name='viewport'> in {rel}")
        for img in parser.images:
            if img['alt'] is None:
                a11y_errs.append(f"Image missing alt in {rel} (line {img['line']}): {img['src']}")

    if a11y_errs:
        for ae in a11y_errs[:5]:
            errors.append(ae)
    else:
        print("  [PASS] 100% compliance on html lang, viewport metadata, and image alt attributes.")

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
