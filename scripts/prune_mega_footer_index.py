#!/usr/bin/env python3
import os
import re
from pathlib import Path

SITE_ROOT = Path(".")

BANNER_REPLACEMENT = """      <section class="directory-banner" aria-label="PPRI Research Directory">
        <div class="container">
          <div class="directory-banner-card">
            <div class="directory-banner-content">
              <span class="directory-banner-badge">Master Catalog</span>
              <h3 class="directory-banner-title">Complete PPRI Policy, Research &amp; Data Directory</h3>
              <p class="directory-banner-text">Explore the unified catalog of 25 policy articles, 5 research reports, and 10 subnational data observatories.</p>
            </div>
            <a href="/directory.html" class="directory-banner-btn">
              <span>Browse 70+ Page Directory</span>
              <span aria-hidden="true">&rarr;</span>
            </a>
          </div>
        </div>
      </section>"""

def clean_file(path: Path):
    if path.name == "directory.html":
        return
    
    txt = path.read_text(encoding="utf-8")
    original = txt
    
    # 1. Check if wrapped in <div data-nosnippet class="global-directory-nosnippet">...</div>
    pattern_wrapped = r'<div\s+data-nosnippet\s+class="global-directory-nosnippet">\s*<section\s+class="site-directory"[^>]*>.*?</section>\s*</div>'
    # 2. Check if direct site-directory
    pattern_direct = r'<section\s+class="site-directory"[^>]*>.*?</section>'
    # 3. Check if existing directory-banner
    pattern_banner = r'\s*<section\s+class="directory-banner"[^>]*>.*?</section>'
    
    if re.search(pattern_wrapped, txt, re.DOTALL):
        txt = re.sub(pattern_wrapped, BANNER_REPLACEMENT, txt, count=1, flags=re.DOTALL)
    elif re.search(pattern_direct, txt, re.DOTALL):
        txt = re.sub(pattern_direct, BANNER_REPLACEMENT, txt, count=1, flags=re.DOTALL)
    elif re.search(pattern_banner, txt, re.DOTALL):
        txt = re.sub(pattern_banner, "\n" + BANNER_REPLACEMENT, txt, count=1, flags=re.DOTALL)
        
    if txt != original:
        path.write_text(txt, encoding="utf-8")
        print(f"[UPDATED DIRECTORY BANNER] {path}")

for root, dirs, files in os.walk("."):
    if any(p in root for p in [".git", "archive", "Google Search Console", ".gemini", "scratch", "scratch_inspect"]):
        continue
    for f in files:
        if f.endswith(".html"):
            clean_file(Path(root) / f)

print("Done pruning mega-footer index.")
