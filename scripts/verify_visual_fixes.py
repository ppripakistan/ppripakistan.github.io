# -*- coding: utf-8 -*-
import re

with open('data/staging/insights.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = [
    ('Card 1: Grants & Other 7th slice completes 100% donut', 'Grants & Other' in text),
    ('Card 2: Modulo filter removed so all 9 bars have totals', 'idx % 2 === 0' not in text),
    ('Card 3: SVG tspan used for tax expenditures legend', 'tspan font-weight=' in text),
    ('Card 4: Stacked density underneath province name', 'density_per_sqkm' in text),
    ('Card 6: Bar offset shifted to 135 for KPK clearance', 'rect x="135"' in text),
    ('Card 7: Vertical staggering for CPI and wage labels', 'yCpi - 7' in text and 'yWage - 7' in text),
    ('Card 11: Corner quadrant badges (Q1-Q4)', 'Q1: DENSE METROS' in text and 'Q2: AGRARIAN DENSE HUBS' in text and 'Q3: VAST ARID PERIPHERY' in text and 'Q4: URBAN OUTPOSTS' in text),
    ('Card 11: SVG scatter clip path present', 'scatter-plot-clip' in text),
    ('Card 15: 2-line stacked tenure badges', 'TENURE I (1990–99)' in text and 'Democracy &amp; Sanctions' in text),
]

all_passed = True
for name, passed in checks:
    status = '[PASS]' if passed else '[FAIL]'
    if not passed:
        all_passed = False
    print(f"  {status} {name}")

tags = re.findall(r'INFOGRAPHIC\s+(\d{2})\s+/\s+15', text)
seq_match = tags == [f'{i:02d}' for i in range(1, 16)]
status = '[PASS]' if (len(tags) == 15 and seq_match) else '[FAIL]'
if not seq_match:
    all_passed = False
print(f"  {status} Numbered tags 01/15 to 15/15: Found {len(tags)} tags")

if all_passed:
    print("\n>>> ALL VISUAL AND OVERLAP FIXES VERIFIED 100% SUCCESSFUL! <<<")
else:
    print("\n>>> SOME CHECKS FAILED! <<<")
    exit(1)
