# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=======================================================")
print("  HOMEPAGE CLEANUP & VISUAL TREEMAP AUTOMATED VERIFICATION")
print("=======================================================")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

errors = []

# 1. Assert #hudWrapper is absent
if 'id="hudWrapper"' in html or 'class="hud-dock"' in html:
    errors.append("FAILED: #hudWrapper or .hud-dock still present in index.html")
else:
    print("  [PASS] Research Desk HUD (#hudWrapper) is completely absent.")

# 2. Assert post-mosaic CTA button is absent
if 'Explore All 16 Interactive Policy Infographics in Insights Lab' in html:
    errors.append("FAILED: Post-mosaic CTA button still present in index.html")
else:
    print("  [PASS] Post-mosaic CTA button is completely absent.")

# 3. Assert #section-platform is absent
if 'id="section-platform"' in html or 'Move between the evidence, the map and the argument' in html:
    errors.append("FAILED: #section-platform still present in index.html")
else:
    print("  [PASS] Section 'Explore the platform' (#section-platform) is completely absent.")

# 4. Assert #section-evidence is absent
if 'id="section-evidence"' in html or 'Evidence, interpretation and scenarios stay distinct' in html:
    errors.append("FAILED: #section-evidence still present in index.html")
else:
    print("  [PASS] Section 'How to read PPRI' (#section-evidence) is completely absent.")

# 5. Assert .home-follow-section is absent
if 'home-follow-section' in html or 'Follow @PPRI_Pakistan on X' in html:
    errors.append("FAILED: .home-follow-section still present in index.html")
else:
    print("  [PASS] Section 'Follow PPRI' (.home-follow-section) is completely absent.")

# 6. Assert #section-participation points to /surveys/
part_match = re.search(r'id="section-participation".*?</section>', html, re.DOTALL)
if part_match:
    part_html = part_match.group(0)
    if 'href="/surveys/"' in part_html and 'consultation/survey' not in part_html:
        print("  [PASS] Public Participation section correctly links to /surveys/.")
    else:
        errors.append("FAILED: #section-participation does not properly link to /surveys/")
else:
    errors.append("FAILED: #section-participation not found")

# 7. Assert consultation/survey.html is deleted
if os.path.exists('consultation/survey.html'):
    errors.append("FAILED: consultation/survey.html still exists on disk")
else:
    print("  [PASS] consultation/survey.html is permanently removed from disk.")

# 8. Assert #section-site-treemap exists with 6 tiles
if 'id="section-site-treemap"' in html:
    tiles = re.findall(r'<details class="vi-treemap-tile\s+theme-([^"]+)"', html)
    print(f"  [PASS] #section-site-treemap exists with {len(tiles)} thematic pillar tiles: {tiles}")
    if len(tiles) != 6:
        errors.append(f"FAILED: Expected 6 tiles, found {len(tiles)}")
else:
    errors.append("FAILED: #section-site-treemap not found in index.html")

# 9. Verify all links in treemap exist on disk
treemap_match = re.search(r'id="section-site-treemap".*?</section>', html, re.DOTALL)
if treemap_match:
    links = re.findall(r'href="([^"#]+)(?:#[^"]*)?"', treemap_match.group(0))
    broken = []
    for link in set(links):
        if link.startswith('/'):
            rel_path = link.lstrip('/')
            # If directory, look for index.html
            target = rel_path
            if target == '' or target.endswith('/'):
                target = os.path.join(rel_path, 'index.html')
            elif not os.path.splitext(target)[1]:
                target = os.path.join(rel_path, 'index.html')
            
            target = os.path.normpath(target)
            if not os.path.exists(target):
                broken.append((link, target))
    if broken:
        errors.append(f"FAILED: Found broken links in treemap: {broken}")
    else:
        print(f"  [PASS] All {len(set(links))} internal links in treemap verified to exist on disk.")

print("=======================================================")
if errors:
    print(f"RESULT: FAILED with {len(errors)} errors:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
else:
    print("RESULT: 100% PASS — ALL CLEANUP & TREEMAP CHECKS SUCCESSFUL!")
print("=======================================================")
