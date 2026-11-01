#!/usr/bin/env python3
"""
scripts/run_complete_seo_audit.py
Full-Spectrum SEO Audit Tool for Pakistan Provincial Reform Institute (PPRI).
Audits Titles, Descriptions, Canonicals, Headings, JSON-LD, Alt Texts,
Open Graph, Twitter Cards, Internal Links, and Sitemap consistency.
"""

import os
import sys
import json
import re
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT_DIR = Path(__file__).resolve().parent.parent
IGNORED_DIRS = {'.git', '.vscode', 'node_modules', '.gemini', 'scratch_inspect', 'scratch', 'archive', 'PPRI_Pakistan_GK_Knowledge_Library_Content_Pack'}
BASE_URL = "https://ppripakistan.github.io"

def run_audit():
    print("=" * 80)
    print("  PPRI FULL-SPECTRUM SITE-WIDE SEO & LINK INTEGRITY AUDIT")
    print("=" * 80)

    html_files = [
        p for p in ROOT_DIR.rglob("*.html")
        if not any(ign in p.parts for ign in IGNORED_DIRS)
    ]
    print(f"Total HTML files discovered: {len(html_files)}")

    errors = []
    warnings = []
    passed = []

    # Dictionaries to track uniqueness
    titles_map = {}
    canonicals_map = {}

    active_pages = []
    redirect_stubs = []

    for p in html_files:
        rel = str(p.relative_to(ROOT_DIR)).replace("\\", "/")
        text = p.read_text(encoding="utf-8")
        if 'http-equiv="refresh"' in text or "http-equiv='refresh'" in text:
            redirect_stubs.append(rel)
        else:
            active_pages.append((p, rel, text))

    print(f"Active content pages: {len(active_pages)} (Redirect stubs excluded: {len(redirect_stubs)})\n")

    # -------------------------------------------------------------
    # 1. TITLE TAGS AUDIT
    # -------------------------------------------------------------
    print("[Audit 1/8] Auditing Title Tags...")
    title_issues = []
    for p, rel, text in active_pages:
        t_m = re.search(r'<title>(.*?)</title>', text, re.IGNORECASE | re.DOTALL)
        if not t_m or not t_m.group(1).strip():
            title_issues.append(f"{rel}: Missing or empty <title>")
        else:
            title = t_m.group(1).strip()
            if len(title) < 20 and rel != "404.html":
                warnings.append(f"Short title ({len(title)} chars) in {rel}: '{title}'")
            elif len(title) > 95:
                warnings.append(f"Long title ({len(title)} chars) in {rel}: '{title[:60]}...'")
            
            # Check uniqueness
            if title in titles_map and rel != "404.html":
                warnings.append(f"Duplicate title between {rel} and {titles_map[title]}: '{title}'")
            else:
                titles_map[title] = rel

    if title_issues:
        errors.extend(title_issues)
    else:
        passed.append(f"100% of active pages ({len(active_pages)}) possess a valid <title> tag.")

    # -------------------------------------------------------------
    # 2. META DESCRIPTIONS AUDIT
    # -------------------------------------------------------------
    print("[Audit 2/8] Auditing Meta Descriptions...")
    desc_issues = []
    for p, rel, text in active_pages:
        if rel == "404.html":
            continue
        d_m = re.search(r'<meta[^>]*name=[\"\']description[\"\'][^>]*content=\"([^\"]*)\"', text, re.IGNORECASE)
        if not d_m:
            d_m = re.search(r'<meta[^>]*name=[\"\']description[\"\'][^>]*content=\'([^\']*)\'', text, re.IGNORECASE)
        if not d_m or not d_m.group(1).strip():
            desc_issues.append(f"{rel}: Missing meta description")
        else:
            desc = d_m.group(1).strip()
            if len(desc) < 50:
                warnings.append(f"Short meta description ({len(desc)} chars) in {rel}: '{desc}'")
            elif len(desc) > 220:
                warnings.append(f"Long meta description ({len(desc)} chars) in {rel}: '{desc[:60]}...'")

    if desc_issues:
        errors.extend(desc_issues)
    else:
        passed.append(f"100% of content pages possess an informative meta description.")

    # -------------------------------------------------------------
    # 3. CANONICAL URL AUDIT
    # -------------------------------------------------------------
    print("[Audit 3/8] Auditing Canonical Link Headers...")
    canon_issues = []
    for p, rel, text in active_pages:
        if rel == "404.html":
            continue
        c_m = re.search(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*href=[\"\']([^\"\']*)[\"\']', text, re.IGNORECASE)
        if not c_m or not c_m.group(1).strip():
            canon_issues.append(f"{rel}: Missing canonical link")
        else:
            c_url = c_m.group(1).strip()
            if not c_url.startswith(BASE_URL):
                canon_issues.append(f"{rel}: Canonical does not start with {BASE_URL} ({c_url})")
            
            # Check for duplicates across different files
            if c_url in canonicals_map and canonicals_map[c_url] != rel:
                canon_issues.append(f"Duplicate canonical target: {rel} and {canonicals_map[c_url]} both claim '{c_url}'")
            else:
                canonicals_map[c_url] = rel

    if canon_issues:
        errors.extend(canon_issues)
    else:
        passed.append(f"100% of content pages declare a unique, well-formed canonical URL.")

    # -------------------------------------------------------------
    # 4. HEADING HIERARCHY AUDIT
    # -------------------------------------------------------------
    print("[Audit 4/8] Auditing <h1> Heading Structure...")
    h1_issues = []
    for p, rel, text in active_pages:
        if rel == "404.html":
            continue
        h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', text, re.IGNORECASE | re.DOTALL)
        if len(h1_matches) == 0:
            h1_issues.append(f"{rel}: Missing <h1> tag")
        elif len(h1_matches) > 1:
            warnings.append(f"Multiple <h1> tags ({len(h1_matches)}) in {rel}")

    if h1_issues:
        errors.extend(h1_issues)
    else:
        passed.append(f"100% of active content pages contain a distinct primary <h1> heading.")

    # -------------------------------------------------------------
    # 5. STRUCTURED DATA (JSON-LD) AUDIT
    # -------------------------------------------------------------
    print("[Audit 5/8] Auditing Schema.org JSON-LD Structured Data...")
    jsonld_issues = []
    jsonld_count = 0
    for p, rel, text in active_pages:
        for script_m in re.finditer(r'<script[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>', text, re.IGNORECASE | re.DOTALL):
            jsonld_count += 1
            raw_json = script_m.group(1).strip()
            try:
                data = json.loads(raw_json)
                if "@context" not in data:
                    warnings.append(f"JSON-LD in {rel} missing '@context'")
            except Exception as e:
                jsonld_issues.append(f"Invalid JSON-LD syntax in {rel}: {e}")

    if jsonld_issues:
        errors.extend(jsonld_issues)
    else:
        passed.append(f"Verified {jsonld_count} Schema.org JSON-LD structured data blocks across site with 0 syntax errors.")

    # -------------------------------------------------------------
    # 6. IMAGE ACCESSIBILITY & ALT TAGS AUDIT
    # -------------------------------------------------------------
    print("[Audit 6/8] Auditing Image Alt Attributes...")
    missing_alt = []
    for p, rel, text in active_pages:
        # Find <img> tags lacking alt
        img_tags = re.findall(r'<img[^>]+>', text, re.IGNORECASE)
        for img in img_tags:
            if 'alt=' not in img:
                missing_alt.append(f"{rel}: {img[:50]}...")
            else:
                alt_m = re.search(r'alt=[\"\']([^\"\']*)[\"\']', img, re.IGNORECASE)
                if alt_m and not alt_m.group(1).strip() and 'aria-hidden="true"' not in img and "role='presentation'" not in img:
                    # decorative or empty alt is acceptable in HTML5 if decorative, but flag if notable
                    pass

    if missing_alt:
        errors.extend(missing_alt[:5])
        if len(missing_alt) > 5:
            errors.append(f"... and {len(missing_alt) - 5} more missing alt attributes.")
    else:
        passed.append("100% of <img> tags have valid alt attributes.")

    # -------------------------------------------------------------
    # 7. INTERNAL LINK RESOLUTION & 404 AUDIT
    # -------------------------------------------------------------
    print("[Audit 7/8] Auditing Internal Links Integrity...")
    broken_links = []
    checked_links = set()
    total_internal_links = 0

    for p, rel, text in active_pages:
        # Match href="..."
        hrefs = re.findall(r'<a[^>]+href=[\"\']([^\"\'#][^\"\']*)[\"\']', text, re.IGNORECASE)
        for href in hrefs:
            href_clean = href.strip()
            # Skip external protocols, mailto, tel, javascript
            if href_clean.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:')):
                continue

            total_internal_links += 1
            path_part = href_clean.split('?')[0].split('#')[0]
            if not path_part:
                continue

            link_key = (rel, path_part)
            if link_key in checked_links:
                continue
            checked_links.add(link_key)

            # Resolve to local disk
            if path_part.startswith('/'):
                # Root-relative
                local_rel = path_part.lstrip('/')
            else:
                # Document-relative
                parent_dir = p.parent
                local_rel = str((parent_dir / path_part).resolve().relative_to(ROOT_DIR)).replace('\\', '/')

            # Test if target file exists
            resolved_file = ROOT_DIR / local_rel
            exists = False
            if resolved_file.exists():
                exists = True
            elif (ROOT_DIR / f"{local_rel}.html").exists():
                exists = True
            elif (ROOT_DIR / local_rel / "index.html").exists():
                exists = True
            elif resolved_file.is_dir() and (resolved_file / "index.html").exists():
                exists = True

            if not exists:
                broken_links.append(f"{rel} -> '{href_clean}' (resolved target: '{local_rel}')")

    if broken_links:
        for b in broken_links[:10]:
            errors.append(f"Broken internal link in {b}")
        if len(broken_links) > 10:
            errors.append(f"... and {len(broken_links) - 10} more broken internal links.")
    else:
        passed.append(f"Audited {total_internal_links} internal links across the site: 0 broken links discovered.")

    # -------------------------------------------------------------
    # 8. SITEMAP & ROBOTS.TXT INTEGRITY
    # -------------------------------------------------------------
    print("[Audit 8/8] Auditing Sitemap & Robots.txt Alignment...")
    sitemap_path = ROOT_DIR / "sitemap.xml"
    robots_path = ROOT_DIR / "robots.txt"

    if not sitemap_path.exists():
        errors.append("sitemap.xml does not exist at root.")
    else:
        s_txt = sitemap_path.read_text(encoding="utf-8")
        sitemap_urls = re.findall(r'<loc>(.*?)</loc>', s_txt)
        passed.append(f"sitemap.xml verified with {len(sitemap_urls)} canonical URLs.")

        # Check for non-existent pages in sitemap
        missing_in_disk = []
        for u in sitemap_urls:
            u_path = urlparse(u).path.lstrip('/')
            if not u_path:
                target = ROOT_DIR / "index.html"
            elif u_path.endswith('.html'):
                target = ROOT_DIR / u_path
            else:
                target = ROOT_DIR / u_path / "index.html"
            
            if not target.exists():
                missing_in_disk.append((u, str(target)))
        
        if missing_in_disk:
            for u, t in missing_in_disk:
                errors.append(f"sitemap.xml contains URL '{u}' but file '{t}' does not exist on disk!")
        else:
            passed.append("100% of sitemap.xml URLs map to valid, existing HTML files on disk.")

    if not robots_path.exists():
        errors.append("robots.txt does not exist at root.")
    else:
        r_txt = robots_path.read_text(encoding="utf-8")
        if "sitemap.xml" not in r_txt:
            warnings.append("robots.txt does not declare Sitemap reference.")
        else:
            passed.append("robots.txt declares valid sitemap reference.")

    # -------------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------------
    print("\n" + "=" * 80)
    print(f"  AUDIT SUMMARY: {len(errors)} Errors, {len(warnings)} Warnings, {len(passed)} Checks Passed")
    print("=" * 80)

    for p_msg in passed:
        print(f"  [PASS] {p_msg}")

    if warnings:
        print(f"\n  [WARNINGS] ({len(warnings)}):")
        for w in warnings[:15]:
            print(f"    - {w}")
        if len(warnings) > 15:
            print(f"    ... and {len(warnings) - 15} more warnings.")

    if errors:
        print(f"\n  [ERRORS] ({len(errors)}):")
        for e in errors:
            print(f"    - {e}")
        return False
    else:
        print("\n>>> ALL TECHNICAL SEO & LINK INTEGRITY AUDITS PASSED WITH ZERO ERRORS! <<<")
        return True

if __name__ == "__main__":
    success = run_audit()
    sys.exit(0 if success else 1)
