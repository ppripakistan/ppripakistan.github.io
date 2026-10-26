#!/usr/bin/env python3
from pathlib import Path
import re

ROOT_DIR = Path(__file__).resolve().parent.parent

def update_index_schema():
    index_path = ROOT_DIR / 'index.html'
    content = index_path.read_text(encoding='utf-8')

    # Update organization logo to 512x512
    old_logo_pat = r'"logo":\s*\{\s*"@type":\s*"ImageObject",\s*"url":\s*"https://ppripakistan\.github\.io/assets/images/brand/ppri-logo\.jpg",\s*"width":\s*1200,\s*"height":\s*630\s*\}'
    new_logo = '''"logo": {
          "@type": "ImageObject",
          "url": "https://ppripakistan.github.io/assets/images/brand/ppri-logo.png",
          "width": 512,
          "height": 512
        }'''
    content = re.sub(old_logo_pat, new_logo, content)

    # Update WebSite alternateName to array
    old_website_name = r'"@type":\s*"WebSite",\s*"@id":\s*"https://ppripakistan\.github\.io/#website",\s*"url":\s*"https://ppripakistan\.github\.io/",\s*"name":\s*"Pakistan Provincial Reform Institute",\s*"alternateName":\s*"PPRI"'
    new_website_name = '''"@type": "WebSite",
        "@id": "https://ppripakistan.github.io/#website",
        "url": "https://ppripakistan.github.io/",
        "name": "Pakistan Provincial Reform Institute",
        "alternateName": ["PPRI", "Pakistan Provincial Reform Institute"]'''
    content = re.sub(old_website_name, new_website_name, content)

    index_path.write_text(content, encoding='utf-8')
    print("Updated index.html structured data.")

def update_about_schema():
    about_path = ROOT_DIR / 'about.html'
    content = about_path.read_text(encoding='utf-8')
    content = re.sub(
        r'"url":\s*"https://ppripakistan\.github\.io/assets/images/brand/ppri-logo\.jpg",\s*"width":\s*1200,\s*"height":\s*630',
        r'"url": "https://ppripakistan.github.io/assets/images/brand/ppri-logo.png",\n                "width": 512,\n                "height": 512',
        content
    )
    about_path.write_text(content, encoding='utf-8')
    print("Updated about.html structured data.")

def update_manifest_and_feed():
    # feed.xml
    feed_path = ROOT_DIR / 'feed.xml'
    feed_txt = feed_path.read_text(encoding='utf-8')
    feed_txt = feed_txt.replace('ppri-logo.jpg', 'ppri-logo.png')
    feed_path.write_text(feed_txt, encoding='utf-8')
    print("Updated feed.xml.")

    # release-manifest.json
    rel_path = ROOT_DIR / 'release-manifest.json'
    rel_txt = rel_path.read_text(encoding='utf-8')
    rel_txt = rel_txt.replace('ppri-logo.jpg', 'ppri-logo.png')
    rel_path.write_text(rel_txt, encoding='utf-8')
    print("Updated release-manifest.json.")

    # robots.txt
    robots_path = ROOT_DIR / 'robots.txt'
    robots_content = "User-agent: *\nAllow: /\n\nUser-agent: Bingbot\nAllow: /\n\nSitemap: https://ppripakistan.github.io/sitemap.xml\n"
    robots_path.write_text(robots_content, encoding='utf-8')
    print("Updated robots.txt with explicit Bingbot directive.")

if __name__ == '__main__':
    update_index_schema()
    update_about_schema()
    update_manifest_and_feed()
