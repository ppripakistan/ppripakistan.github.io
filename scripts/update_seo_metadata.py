#!/usr/bin/env python3
"""
scripts/update_seo_metadata.py
Standardizes favicons, Open Graph tags, Twitter cards, and JSON-LD structured data
across all 120 HTML files in the repository.
"""

import os
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

IGNORED_DIRS = {'.git', '.vscode', 'node_modules', '.gemini', 'scratch_inspect'}

FAVICON_BLOCK = """    <link rel="icon" href="/favicon.ico" sizes="48x48" />
    <link rel="icon" href="/assets/images/brand/favicon.svg" type="image/svg+xml" />
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/images/brand/favicon-32x32.png" />
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/images/brand/favicon-16x16.png" />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
    <link rel="manifest" href="/site.webmanifest" />
    <meta name="theme-color" content="#073c3a" />"""

SPECIFIC_OG_IMAGES = {
    "research/reports/income-went-up-why-does-life-feel-harder.html": (
        "https://ppripakistan.github.io/assets/images/research/ppri-rep01-income-inflation.jpg?v=2",
        "PPRI Research Report: Income Went Up. So Why Does Life Feel Harder?"
    ),
    "research/reports/does-money-work-better-spent-closer-to-people.html": (
        "https://ppripakistan.github.io/assets/images/research/ppri-rep02-fiscal-decentralization.jpg?v=2",
        "PPRI Research Report: Does Money Work Better When Spent Closer to the People?"
    ),
    "research/reports/bribe-you-cant-see-corruption-private-tax.html": (
        "https://ppripakistan.github.io/assets/images/research/ppri-rep03-invisible-tax-corruption.jpg?v=2",
        "PPRI Research Report: The Bribe You Can't See: Corruption as an Invisible Private Tax"
    ),
    "research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html": (
        "https://ppripakistan.github.io/assets/images/research/ppri-rep04-bureaucracy-friction.jpg?v=2",
        "PPRI Research Report: The Price of a Simple Task: Quantifying Bureaucracy Cost"
    ),
    "research/reports/same-country-different-life-district-access.html": (
        "https://ppripakistan.github.io/assets/images/research/ppri-rep05-district-inequality.jpg?v=2",
        "PPRI Research Report: Same Country, Different Life: Measuring District Service Inequality"
    ),
    "research/policy-papers/provincial-reorganization-of-pakistan.html": (
        "https://ppripakistan.github.io/assets/images/research/ppri-pp01-provincial-reorganization.jpg?v=2",
        "PPRI Flagship Policy Paper: The Provincial Reorganization of Pakistan"
    )
}

DEFAULT_OG_IMAGE = "https://ppripakistan.github.io/assets/images/brand/ppri-social-share.jpg?v=2"
DEFAULT_OG_ALT = "Pakistan Provincial Reform Institute (PPRI)"

def process_html_file(file_path):
    rel_path = str(file_path.relative_to(ROOT_DIR)).replace("\\", "/")
    content = file_path.read_text(encoding="utf-8")

    # Extract title
    title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL | re.I)
    title = title_m.group(1).strip() if title_m else "Pakistan Provincial Reform Institute | PPRI"

    # Extract description
    desc_m = re.search(r'<meta[^>]*name=[\"\']description[\"\'][^>]*content=[\"\'](.*?)[\"\']', content, re.DOTALL | re.I)
    if not desc_m:
        desc_m = re.search(r'<meta[^>]*content=[\"\'](.*?)[\"\'][^>]*name=[\"\']description[\"\']', content, re.DOTALL | re.I)
    desc = desc_m.group(1).strip() if desc_m else "Pakistan Provincial Reform Institute: research, data, maps and public-policy analysis on provincial reform, governance, federalism and decentralization in Pakistan."

    # Extract canonical
    canon_m = re.search(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*href=[\"\'](.*?)[\"\']', content, re.I)
    canonical = canon_m.group(1).strip() if canon_m else f"https://ppripakistan.github.io/{rel_path}"

    # Determine OG Image & Alt
    if rel_path in SPECIFIC_OG_IMAGES:
        og_image, og_alt = SPECIFIC_OG_IMAGES[rel_path]
    else:
        og_image = DEFAULT_OG_IMAGE
        og_alt = DEFAULT_OG_ALT

    # Determine OG Type
    is_article = any(x in rel_path for x in ['articles/', 'reports/', 'policy-papers/', 'briefs/', 'working-papers/'])
    og_type = "article" if is_article else "website"

    # Check if redirect stub
    is_redirect = 'http-equiv="refresh"' in content or "http-equiv='refresh'" in content

    # Standard Social & Meta Block
    social_block = f"""    <meta property="og:site_name" content="Pakistan Provincial Reform Institute (PPRI)" />
    <meta property="og:locale" content="en_PK" />
    <meta property="og:type" content="{og_type}" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{desc}" />
    <meta property="og:url" content="{canonical}" />
    <meta property="og:image" content="{og_image}" />
    <meta property="og:image:secure_url" content="{og_image}" />
    <meta property="og:image:type" content="image/jpeg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:image:alt" content="{og_alt}" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:site" content="@PPRI_Pakistan" />
    <meta name="twitter:creator" content="@PPRI_Pakistan" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{desc}" />
    <meta name="twitter:image" content="{og_image}" />
    <meta name="twitter:image:alt" content="{og_alt}" />"""

    # 1. Clean existing favicon links and theme-color
    content = re.sub(r'[ \t]*<link[^>]*rel=[\"\'](?:shortcut )?icon[\"\'][^>]*>\r?\n?', '', content, flags=re.I)
    content = re.sub(r'[ \t]*<link[^>]*rel=[\"\']apple-touch-icon[\"\'][^>]*>\r?\n?', '', content, flags=re.I)
    content = re.sub(r'[ \t]*<link[^>]*rel=[\"\']manifest[\"\'][^>]*>\r?\n?', '', content, flags=re.I)
    content = re.sub(r'[ \t]*<meta[^>]*name=[\"\']theme-color[\"\'][^>]*>\r?\n?', '', content, flags=re.I)

    # 2. Clean existing Open Graph & Twitter meta tags (except on redirect stubs where they might be absent)
    content = re.sub(r'[ \t]*<meta[^>]*property=[\"\']og:[^\"\']+[\"\'][^>]*>\r?\n?', '', content, flags=re.I)
    content = re.sub(r'[ \t]*<meta[^>]*name=[\"\']twitter:[^\"\']+[\"\'][^>]*>\r?\n?', '', content, flags=re.I)

    # 3. For redirect stubs, just insert favicons before </head>
    if is_redirect:
        replacement = f"{FAVICON_BLOCK}\n  </head>"
        content = re.sub(r'[ \t]*</head>', replacement, content, count=1)
        file_path.write_text(content, encoding="utf-8")
        return "redirect"

    # 4. For standard pages, place Social Block and Favicon Block cleanly after canonical link
    if '<link rel="canonical"' in content or "<link rel='canonical'" in content:
        # Match the whole canonical link line
        canon_pat = r'(<link[^>]*rel=[\"\']canonical[\"\'][^>]*>)'
        m = re.search(canon_pat, content, flags=re.I)
        if m:
            orig_canon = m.group(1)
            new_chunk = f"{orig_canon}\n{social_block}\n{FAVICON_BLOCK}"
            content = content.replace(orig_canon, new_chunk, 1)
        else:
            # Fallback before </head>
            content = re.sub(r'[ \t]*</head>', f"{social_block}\n{FAVICON_BLOCK}\n  </head>", content, count=1)
    else:
        # No canonical, insert before </head>
        content = re.sub(r'[ \t]*</head>', f"{social_block}\n{FAVICON_BLOCK}\n  </head>", content, count=1)

    # Also update any JSON-LD references to ppri-social-share.jpg or ppri-logo.jpg if width/height are specified
    content = content.replace(
        '"url": "https://ppripakistan.github.io/assets/images/brand/ppri-social-share.jpg"',
        '"url": "https://ppripakistan.github.io/assets/images/brand/ppri-social-share.jpg?v=2"'
    )

    file_path.write_text(content, encoding="utf-8")
    return "updated"

def run_all():
    print("Standardizing SEO, Favicon, and Social Metadata across all pages...")
    html_files = [
        p for p in ROOT_DIR.rglob("*.html")
        if not any(ign in p.parts for ign in IGNORED_DIRS)
    ]
    print(f"Discovered {len(html_files)} HTML pages.")

    stats = {"updated": 0, "redirect": 0}
    for p in sorted(html_files):
        res = process_html_file(p)
        stats[res] = stats.get(res, 0) + 1

    print("\nProcessing complete:")
    print(f"  Content pages standardized: {stats.get('updated', 0)}")
    print(f"  Redirect stubs updated:     {stats.get('redirect', 0)}")
    print(f"  Total processed:            {len(html_files)}")

if __name__ == "__main__":
    run_all()
