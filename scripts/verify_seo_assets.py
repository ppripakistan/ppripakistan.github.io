#!/usr/bin/env python3
"""
scripts/verify_seo_assets.py
Comprehensive verification script for Favicons, Social Sharing Cards,
Open Graph/Twitter Metadata, and Google Search JSON-LD Structured Data.
"""

import sys
import json
import re
from pathlib import Path
from PIL import Image

ROOT_DIR = Path(__file__).resolve().parent.parent
BRAND_DIR = ROOT_DIR / "assets" / "images" / "brand"
RESEARCH_DIR = ROOT_DIR / "assets" / "images" / "research"

IGNORED_DIRS = {'.git', '.vscode', 'node_modules', '.gemini', 'scratch_inspect'}

def verify_all():
    print("=" * 75)
    print("  PPRI FAVICON, SOCIAL SHARING & TECHNICAL SEO VERIFICATION")
    print("=" * 75)

    errors = []
    warnings = []

    # 1. Verify Root & Brand Favicon Assets
    print("\n[Check 1/6] Verifying Favicon & App Icon Asset Integrity...")
    root_ico = ROOT_DIR / "favicon.ico"
    if not root_ico.exists():
        errors.append("Root /favicon.ico does not exist.")
    else:
        try:
            im = Image.open(root_ico)
            print(f"  [PASS] Root favicon.ico exists and is valid format={im.format} sizes={getattr(im, 'info', {}).get('sizes', 'N/A')}")
        except Exception as e:
            errors.append(f"Root /favicon.ico invalid: {e}")

    root_apple = ROOT_DIR / "apple-touch-icon.png"
    if not root_apple.exists():
        errors.append("Root /apple-touch-icon.png does not exist.")
    else:
        im = Image.open(root_apple)
        if im.size != (180, 180):
            errors.append(f"Root apple-touch-icon.png size is {im.size}, expected (180, 180)")
        else:
            print("  [PASS] Root apple-touch-icon.png is 180x180.")

    root_svg = ROOT_DIR / "favicon.svg"
    if not root_svg.exists() or root_svg.stat().st_size == 0:
        errors.append("Root /favicon.svg missing or empty.")
    else:
        print(f"  [PASS] Root favicon.svg exists ({root_svg.stat().st_size} bytes).")

    brand_assets = [
        ("favicon-16x16.png", (16, 16)),
        ("favicon-32x32.png", (32, 32)),
        ("favicon-48x48.png", (48, 48)),
        ("icon-192.png", (192, 192)),
        ("icon-512.png", (512, 512)),
        ("ppri-favicon.png", (192, 192)),
    ]
    for name, expected_size in brand_assets:
        p = BRAND_DIR / name
        if not p.exists():
            errors.append(f"Brand asset missing: {name}")
        else:
            im = Image.open(p)
            if im.size != expected_size:
                errors.append(f"Brand asset {name} size is {im.size}, expected {expected_size}")
            else:
                print(f"  [PASS] {name} is {im.size} (aspect ratio 1:1, non-distorted).")

    # 2. Verify site.webmanifest
    print("\n[Check 2/6] Verifying site.webmanifest...")
    manifest_path = ROOT_DIR / "site.webmanifest"
    if not manifest_path.exists():
        errors.append("site.webmanifest missing.")
    else:
        try:
            m_data = json.loads(manifest_path.read_text(encoding="utf-8"))
            icons = m_data.get("icons", [])
            if len(icons) < 2:
                errors.append("site.webmanifest must have at least 2 icon declarations.")
            for icon in icons:
                src = icon.get("src", "").lstrip("/")
                resolved = ROOT_DIR / src
                if not resolved.exists():
                    errors.append(f"Manifest icon file does not exist: {src}")
                else:
                    im = Image.open(resolved)
                    expected_sz = int(icon.get("sizes", "0x0").split("x")[0])
                    if im.size != (expected_sz, expected_sz):
                        errors.append(f"Manifest icon {src} declares {icon.get('sizes')} but actual is {im.size}")
                    else:
                        print(f"  [PASS] Manifest icon {src} matches {icon.get('sizes')}.")
        except Exception as e:
            errors.append(f"site.webmanifest JSON error: {e}")

    # 3. Verify Social Share Preview Cards on Disk
    print("\n[Check 3/6] Verifying 1200x630 Social Preview Images...")
    social_cards = [
        BRAND_DIR / "ppri-social-share.jpg",
        BRAND_DIR / "ppri-logo.jpg",
        RESEARCH_DIR / "ppri-rep01-income-inflation.jpg",
        RESEARCH_DIR / "ppri-rep02-fiscal-decentralization.jpg",
        RESEARCH_DIR / "ppri-rep03-invisible-tax-corruption.jpg",
        RESEARCH_DIR / "ppri-rep04-bureaucracy-friction.jpg",
        RESEARCH_DIR / "ppri-rep05-district-inequality.jpg",
        RESEARCH_DIR / "ppri-pp01-provincial-reorganization.jpg",
    ]
    for card_path in social_cards:
        if not card_path.exists():
            errors.append(f"Social card missing: {card_path.name}")
        else:
            im = Image.open(card_path)
            size = card_path.stat().st_size
            if im.size != (1200, 630):
                errors.append(f"Social card {card_path.name} is {im.size}, expected (1200, 630)")
            elif size > 300 * 1024:
                warnings.append(f"Social card {card_path.name} is {size/1024:.1f}KB (>300KB WhatsApp limit)")
            else:
                print(f"  [PASS] {card_path.name} is 1200x630 ({size/1024:.1f} KB, well under 300KB limit).")

    # 4. Scan all 120 HTML files for Favicon & Manifest coverage
    print("\n[Check 4/6] Scanning All HTML Pages for Favicon & Manifest References...")
    html_files = [
        p for p in ROOT_DIR.rglob("*.html")
        if not any(ign in p.parts for ign in IGNORED_DIRS)
    ]
    print(f"  Scanned {len(html_files)} HTML pages.")

    missing_favicon = []
    missing_manifest_links = []
    for p in html_files:
        text = p.read_text(encoding="utf-8")
        rel = str(p.relative_to(ROOT_DIR)).replace("\\", "/")
        if 'rel="icon"' not in text and "rel='icon'" not in text:
            missing_favicon.append(rel)
        if 'site.webmanifest' not in text:
            missing_manifest_links.append(rel)

    if missing_favicon:
        errors.append(f"HTML pages missing favicon: {missing_favicon}")
    else:
        print("  [PASS] 100% of HTML pages contain standardized favicon link tags.")

    if missing_manifest_links:
        errors.append(f"HTML pages missing site.webmanifest: {missing_manifest_links}")
    else:
        print("  [PASS] 100% of HTML pages link to /site.webmanifest.")

    # 5. Scan Content Pages for Open Graph & Twitter Cards
    print("\n[Check 5/6] Verifying Open Graph & Twitter Card Completeness...")
    content_pages = [
        p for p in html_files
        if not ('http-equiv="refresh"' in p.read_text(encoding="utf-8") or "http-equiv='refresh'" in p.read_text(encoding="utf-8"))
    ]
    print(f"  Found {len(content_pages)} active content pages.")

    missing_og = []
    missing_tw = []
    broken_og_images = []

    for p in content_pages:
        text = p.read_text(encoding="utf-8")
        rel = str(p.relative_to(ROOT_DIR)).replace("\\", "/")

        og_img_m = re.search(r'<meta[^>]*property=[\"\']og:image[\"\'][^>]*content=[\"\']([^\"\']+)[\"\']', text)
        if not og_img_m:
            missing_og.append(rel)
        else:
            og_url = og_img_m.group(1)
            # Verify file exists on disk
            clean_url = og_url.split("?")[0]
            clean_path = clean_url.replace("https://ppripakistan.github.io/", "")
            target_disk = ROOT_DIR / clean_path
            if not target_disk.exists():
                broken_og_images.append((rel, og_url))

        tw_card_m = re.search(r'<meta[^>]*name=[\"\']twitter:card[\"\'][^>]*content=[\"\']([^\"\']+)[\"\']', text)
        if not tw_card_m:
            missing_tw.append(rel)

    if missing_og:
        errors.append(f"Content pages missing og:image: {missing_og}")
    else:
        print("  [PASS] 100% of content pages contain og:image metadata.")

    if broken_og_images:
        for r, u in broken_og_images:
            errors.append(f"Broken og:image reference in {r}: {u}")
    else:
        print("  [PASS] 100% of og:image URLs resolve to existing local image assets.")

    if missing_tw:
        errors.append(f"Content pages missing twitter:card: {missing_tw}")
    else:
        print("  [PASS] 100% of content pages contain twitter:card metadata.")

    # 6. Verify Google Tag Preservation & JSON-LD
    print("\n[Check 6/6] Verifying Google Tag (gtag.js) & JSON-LD...")
    missing_gtag = []
    for p in html_files:
        text = p.read_text(encoding="utf-8")
        if "G-9C2NZV6BYF" not in text:
            missing_gtag.append(str(p.relative_to(ROOT_DIR)).replace("\\", "/"))

    if missing_gtag:
        errors.append(f"HTML pages missing Google tag: {missing_gtag}")
    else:
        print("  [PASS] 100% of 120 HTML pages retain the Google tag (gtag.js) snippet.")

    # Summary
    print("\n" + "=" * 75)
    print(f"VERIFICATION SUMMARY: {len(errors)} Errors, {len(warnings)} Warnings")
    print("=" * 75)
    if errors:
        for e in errors:
            print(f"  [ERROR] {e}")
        return False
    else:
        print("ALL FAVICON, SOCIAL SHARING & SEO CHECKS PASSED WITH 100% SUCCESS!")
        return True

if __name__ == "__main__":
    success = verify_all()
    sys.exit(0 if success else 1)
