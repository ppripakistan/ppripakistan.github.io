import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Check visual-insights.js is NOT in index.html
has_js = 'visual-insights.js' in html
print(f"visual-insights.js in index.html? {has_js} (Must be False!)")

# 2. Count mosaic cards
cards = re.findall(r'<a href="(/insights/#card-[^"]+)" class="vi-mosaic-card"', html)
print(f"Total mosaic cards on index.html: {len(cards)}")
for c in cards:
    print(f"  Target: {c}")

# 3. Check all images have explicit width, height, loading=lazy, decoding=async
imgs = re.findall(r'<img\s+src="([^"]+)"\s+alt="([^"]+)"\s+width="([^"]+)"\s+height="([^"]+)"\s+loading="lazy"\s+decoding="async"', html)
print(f"Total compliant lazy-loaded SVGs: {len(imgs)}")

# 4. Check all 16 image files exist on disk
all_files_exist = True
for src, alt, w, h in imgs:
    local_path = src.lstrip('/')
    exists = os.path.exists(local_path)
    size = os.path.getsize(local_path) if exists else 0
    if not exists or size == 0:
        print(f"  FAILED: {src} -> exists={exists}, size={size}")
        all_files_exist = False
    else:
        print(f"  PASS: {src:<38} -> {size:>6} bytes (w={w}, h={h})")

all_ok = (not has_js) and len(cards) == 16 and len(imgs) == 16 and all_files_exist
if all_ok:
    print("\n=======================================================")
    print("HOMEPAGE 16-CARD MOSAIC GRID IS 100% VALID & COMPLIANT!")
    print("=======================================================")
else:
    print("\nVERIFICATION FAILED!")
    exit(1)
