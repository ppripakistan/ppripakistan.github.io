# -*- coding: utf-8 -*-
import re

with open('assets/js/hero-map.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    # Check lines to skip
    if 'hudWrapper' in line or 'hudDock' in line or 'hudTrigger' in line or 'hudClose' in line or 'HUD_EXPAND_DELAY' in line or 'HUD_COLLAPSE_DELAY' in line or 'hudExpandTimer' in line or 'hudCollapseTimer' in line:
        continue
    if 'Jitter-Free Collapsible HUD Dock' in line:
        skip = True
        continue
    if skip and '/* ── Boot' in line:
        skip = False
    if not skip:
        new_lines.append(line)

with open('assets/js/hero-map.js', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("hero-map.js successfully cleaned of HUD code.")
