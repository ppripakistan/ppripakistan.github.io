#!/usr/bin/env python3
"""
scripts/sync_preview_metadata.py
Synchronizes Open Graph and X (Twitter) Card preview metadata across all
publication pages, observatory hubs, maps, scenarios, Urdu translations, and articles.

Ensures every page points to its bespoke 1200x630 preview card in
assets/images/previews/ with standardized tags for Threads, X, Facebook, and LinkedIn.
"""

import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PREVIEWS_DIR = ROOT_DIR / "assets" / "images" / "previews"
BASE_URL = "https://ppripakistan.github.io"

def get_page_slug(file_path):
    rel = file_path.relative_to(ROOT_DIR).as_posix()
    slug = rel.replace('/', '-').replace('.html', '')
    if slug.endswith('-index'):
        slug = slug[:-6]
    return slug

def sync_page(file_path):
    rel = file_path.relative_to(ROOT_DIR).as_posix()
    content = file_path.read_text(encoding='utf-8')

    # Skip redirect stubs
    if 'http-equiv="refresh"' in content or "http-equiv='refresh'" in content:
        return False

    slug = get_page_slug(file_path)
    preview_filename = f"{slug}.jpg"
    preview_disk_path = PREVIEWS_DIR / preview_filename

    # Fallback to English counterpart card or master card if bespoke image not generated
    if preview_disk_path.exists():
        img_url = f"{BASE_URL}/assets/images/previews/{preview_filename}"
    elif slug.startswith("ur-"):
        en_slug = slug[3:]
        en_preview = PREVIEWS_DIR / f"{en_slug}.jpg"
        if en_preview.exists():
            img_url = f"{BASE_URL}/assets/images/previews/{en_slug}.jpg"
        else:
            img_url = f"{BASE_URL}/assets/images/previews/index.jpg"
    else:
        img_url = f"{BASE_URL}/assets/images/previews/index.jpg"

    # Extract title & description for alt tags
    title_m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    raw_title = title_m.group(1).strip() if title_m else "Pakistan Provincial Reform Institute"
    clean_title = re.sub(r'<[^>]+>', '', raw_title)
    for suffix in [' | PPRI Pakistan', ' | PPRI', ' - PPRI', ' | Pakistan Provincial Reform Institute']:
        if clean_title.endswith(suffix):
            clean_title = clean_title[:-len(suffix)]

    alt_text = f"{clean_title} | Pakistan Provincial Reform Institute"

    # 1. Update og:image
    if 'property="og:image"' in content or "property='og:image'" in content:
        content = re.sub(
            r'<meta\s+property=[\'"]og:image[\'"]\s+content=[\'"][^\'"]+[\'"]\s*/?>',
            f'<meta property="og:image" content="{img_url}" />',
            content
        )
    else:
        content = content.replace('</head>', f'    <meta property="og:image" content="{img_url}" />\n  </head>')

    # 2. Update og:image:secure_url
    if 'property="og:image:secure_url"' in content or "property='og:image:secure_url'" in content:
        content = re.sub(
            r'<meta\s+property=[\'"]og:image:secure_url[\'"]\s+content=[\'"][^\'"]+[\'"]\s*/?>',
            f'<meta property="og:image:secure_url" content="{img_url}" />',
            content
        )
    else:
        content = re.sub(
            r'(<meta property="og:image" content="[^"]+" />)',
            r'\1\n    <meta property="og:image:secure_url" content="' + img_url + '" />',
            content
        )

    # 3. Update og:image:alt
    if 'property="og:image:alt"' in content or "property='og:image:alt'" in content:
        content = re.sub(
            r'<meta\s+property=[\'"]og:image:alt[\'"]\s+content=[\'"][^\'"]+[\'"]\s*/?>',
            f'<meta property="og:image:alt" content="{alt_text}" />',
            content
        )

    # 4. Update twitter:card if missing
    if 'name="twitter:card"' not in content and "name='twitter:card'" not in content:
        tw_block = (
            '    <meta name="twitter:card" content="summary_large_image" />\n'
            '    <meta name="twitter:site" content="@PPRI_Pakistan" />\n'
            '    <meta name="twitter:creator" content="@PPRI_Pakistan" />'
        )
        if 'property="og:image:alt"' in content:
            content = re.sub(
                r'(<meta property="og:image:alt" content="[^"]*" />)',
                r'\1\n' + tw_block,
                content
            )
        elif 'property="og:image"' in content:
            content = re.sub(
                r'(<meta property="og:image" content="[^"]*" />)',
                r'\1\n' + tw_block,
                content
            )

    # 5. Update twitter:image
    if 'name="twitter:image"' in content or "name='twitter:image'" in content:
        content = re.sub(
            r'<meta\s+name=[\'"]twitter:image[\'"]\s+content=[\'"][^\'"]+[\'"]\s*/?>',
            f'<meta name="twitter:image" content="{img_url}" />',
            content
        )
    else:
        content = content.replace('</head>', f'    <meta name="twitter:image" content="{img_url}" />\n  </head>')

    # 6. Update twitter:image:alt
    if 'name="twitter:image:alt"' in content or "name='twitter:image:alt'" in content:
        content = re.sub(
            r'<meta\s+name=[\'"]twitter:image:alt[\'"]\s+content=[\'"][^\'"]+[\'"]\s*/?>',
            f'<meta name="twitter:image:alt" content="{alt_text}" />',
            content
        )

    file_path.write_text(content, encoding='utf-8')
    return True

def sync_all():
    print("=" * 70)
    print("  SYNCHRONIZING SOCIAL PREVIEW METADATA")
    print("=" * 70)

    target_patterns = [
        '*.html',
        'articles/*.html',
        'research/**/*.html',
        'data/centre.html',
        'data/*/index.html',
        'maps/**/*.html',
        'scenarios/**/*.html',
        'consultation/**/*.html',
        'provinces/**/*.html',
        'media/**/*.html',
        'ur/**/*.html',
        'insights/*.html',
        'surveys/**/*.html',
        'knowledge-library/**/*.html',
    ]

    all_files = []
    for pat in target_patterns:
        for p in ROOT_DIR.glob(pat):
            rel = p.relative_to(ROOT_DIR).as_posix()
            if any(ign in rel for ign in ['archive/', 'node_modules/', 'scratch', '.git']):
                continue
            all_files.append(p)

    seen = set()
    pages = []
    for p in all_files:
        if p not in seen:
            seen.add(p)
            pages.append(p)

    updated = 0
    for p in pages:
        if sync_page(p):
            updated += 1

    print(f"Successfully synchronized Open Graph & X metadata across {updated} pages.")
    print("=" * 70)
    return True

if __name__ == '__main__':
    success = sync_all()
    sys.exit(0 if success else 1)
