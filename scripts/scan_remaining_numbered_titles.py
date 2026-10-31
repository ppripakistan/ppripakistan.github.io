import os
import re

files = [os.path.join(r, f) for r, _, fs in os.walk('.') for f in fs if f.endswith('.html') and not any(x in r for x in ['.git', 'node_modules', 'archive'])]

matches = []
for p in files:
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    found = re.findall(r'<h3 class="vi-card-title">\s*#\d+.*?</h3', text)
    if found:
        matches.append((p, found))

print("Scan for remaining numbered card titles (<h3 class=\"vi-card-title\">#...):")
if matches:
    for p, f in matches:
        print(f"  FOUND in {p}: {f}")
else:
    print("  ZERO NUMBERED CARD TITLES FOUND ACROSS THE ENTIRE REPOSITORY! 100% CLEAN!")
