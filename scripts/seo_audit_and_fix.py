#!/usr/bin/env python3
import os
import re
from pathlib import Path

SITE_ROOT = Path(".")
BASE_URL = "https://ppripakistan.github.io"

def get_canonical_url(rel_path: Path) -> str:
    posix = rel_path.as_posix()
    if posix == "index.html":
        return f"{BASE_URL}/"
    if posix.endswith("/index.html"):
        return f"{BASE_URL}/{posix[:-10]}"
    return f"{BASE_URL}/{posix}"

def fix_links_single(m):
    quote = m.group(1)
    url = m.group(2)
    frag = ""
    if "#" in url:
        url, frag = url.split("#", 1)
        frag = "#" + frag
    
    # Don't touch external URLs that are not BASE_URL
    if url.startswith("http://") or (url.startswith("https://") and not url.startswith(BASE_URL)):
        return m.group(0)

    if url.endswith("/index.html"):
        norm = url[:-10]
        return f'href={quote}{norm}{frag}{quote}'
    return m.group(0)

def fix_html_file(file_path: Path):
    rel_path = file_path.relative_to(SITE_ROOT)
    # Skip archive, Google Search Console, scratch directories
    if any(p in rel_path.parts for p in [".git", "archive", "Google Search Console", ".gemini", "scratch", "scratch_inspect"]):
        return

    content = file_path.read_text(encoding="utf-8")
    original = content
    canonical_url = get_canonical_url(rel_path)

    # 1. Canonical tag check & normalization
    is_redirect_or_alias = ('http-equiv="refresh"' in content or 'http-equiv=\'refresh\'' in content) and 'noindex' in content.lower()

    if not is_redirect_or_alias:
        canon_match = re.search(r'<link[^>]*rel=["\']canonical["\'][^>]*href=["\']([^"\']+)["\'][^>]*>', content)
        if not canon_match:
            canon_match = re.search(r'<link[^>]*href=["\']([^"\']+)["\'][^>]*rel=["\']canonical["\'][^>]*>', content)

        if canon_match:
            curr_href = canon_match.group(1)
            if curr_href != canonical_url:
                old_tag = canon_match.group(0)
                new_tag = f'<link rel="canonical" href="{canonical_url}" />'
                content = content.replace(old_tag, new_tag)
        else:
            if "</head>" in content:
                content = content.replace("</head>", f'    <link rel="canonical" href="{canonical_url}" />\n  </head>')

    # 2. Normalize internal <a href> links ending in /index.html -> /
    content = re.sub(r'href=(["\'])([^"\']*index\.html[^"\']*)\1', fix_links_single, content)

    # 3. Audit Title & Meta Description lengths
    title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    title_text = title_match.group(1).strip() if title_match else ""
    
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=(["\'])(.*?)\1', content, re.DOTALL | re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'<meta\s+content=(["\'])(.*?)\1\s+name=["\']description["\']', content, re.DOTALL | re.IGNORECASE)
    desc_text = desc_match.group(2).strip() if desc_match else ""

    if len(title_text) > 65 or (len(title_text) < 20 and len(title_text) > 0):
        print(f"[TITLE WARN] {rel_path}: ({len(title_text)} chars) -> {title_text}")
    if len(desc_text) > 165 or (len(desc_text) < 50 and len(desc_text) > 0):
        print(f"[DESC WARN]  {rel_path}: ({len(desc_text)} chars) -> {desc_text[:80]}...")

    # 4. Check JSON-LD presence
    if not re.search(r'<script\s+type=["\']application/ld\+json["\']>', content):
        if not is_redirect_or_alias:
            print(f"[SCHEMA MISSING] {rel_path}: No JSON-LD found!")

    if content != original:
        file_path.write_text(content, encoding="utf-8")
        print(f"[FIXED] {rel_path}")

def rebuild_sitemap():
    urls = []
    for html_file in sorted(SITE_ROOT.rglob("*.html")):
        rel = html_file.relative_to(SITE_ROOT)
        if any(part in {".git", "archive", "Google Search Console", ".gemini", "scratch", "scratch_inspect", "scripts", "templates", "components"} for part in rel.parts):
            continue
        try:
            html = html_file.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
            
        # Exclude noindex / redirect stubs
        if 'content="noindex' in html.lower() or "content='noindex" in html.lower():
            continue
        if 'http-equiv="refresh"' in html.lower() or "http-equiv='refresh'" in html.lower():
            continue
        if html_file.name == "404.html":
            continue

        canon = get_canonical_url(rel)
        urls.append(canon)

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    unique_urls = sorted(set(urls))
    for u in unique_urls:
        if u == f"{BASE_URL}/" or u == f"{BASE_URL}/ur/":
            priority = "1.0"
        elif "/data/" in u or "/articles/" in u or "/research/" in u or "/scenarios/" in u or "/reform/" in u or "/provinces/" in u:
            priority = "0.9"
        else:
            priority = "0.8"
        xml_lines.append(f"  <url>\n    <loc>{u}</loc>\n    <lastmod>2026-11-14</lastmod>\n    <priority>{priority}</priority>\n  </url>")
    xml_lines.append("</urlset>\n")
    
    (SITE_ROOT / "sitemap.xml").write_text("\n".join(xml_lines), encoding="utf-8")
    print(f"[SITEMAP] Rebuilt sitemap.xml with {len(unique_urls)} canonical URLs with lastmod 2026-11-14.")

if __name__ == "__main__":
    for html_file in sorted(SITE_ROOT.rglob("*.html")):
        fix_html_file(html_file)
    rebuild_sitemap()
