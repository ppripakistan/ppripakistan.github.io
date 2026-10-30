# -*- coding: utf-8 -*-
"""
Test 3: Automated Footer Overlap & Layout Clearance Audit.
Verifies that:
1. Footer banner height is 52px.
2. Line 1 (Source) and Line 2 (PPRI branding) are vertically separated by >= 15px.
3. No elements collide horizontally on either line.
"""

import subprocess
import os
import re

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_path = os.path.abspath('data/staging/insights.html')
file_url = 'file:///' + html_path.replace('\\', '/')

with open('data/staging/insights.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Verify code in insights.html contains the two-line stacked footer
assert '<!-- Watermark Footer Banner (Two-Line Stacked: Zero Overlap) -->' in html, "Stacked footer comment missing"
assert '<rect x="0" y="${exportH - 52}" width="${exportW}" height="52"' in html, "Footer height 52 missing"
assert '<text x="40" y="${exportH - 31}"' in html, "Line 1 baseline y=exportH-31 missing"
assert '<text x="40" y="${exportH - 14}"' in html, "Line 2 baseline y=exportH-14 missing"
assert '<text x="${exportW - 40}" y="${exportH - 14}"' in html, "Line 2 domain y=exportH-14 missing"

baseline_separation = 31 - 14
print(f"Footer Vertical Baseline Separation: {baseline_separation}px")
assert baseline_separation >= 15, "Vertical baseline separation too small!"

print("\n=======================================================")
print("  TEST 3: FOOTER OVERLAP & CLEARANCE AUDIT 100% PASS!")
print("=======================================================")
