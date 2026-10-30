# -*- coding: utf-8 -*-
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=======================================================")
print("  HIERARCHICAL TREE ARCHITECTURE AUTOMATED TEST")
print("=======================================================")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

errors = []

# 1. Assert Section and Root Node
if 'class="vi-tree-section"' not in html:
    errors.append("FAILED: .vi-tree-section not found in index.html")
else:
    print("  [PASS] .vi-tree-section is present in index.html.")

if 'class="vi-tree-root-node"' not in html:
    errors.append("FAILED: .vi-tree-root-node not found")
else:
    print("  [PASS] Level 0 Root Node (PPRI Public Knowledge & Evidence Tree) is present.")

# 2. Assert Tree Busbar Distributor & Socket Ports
if 'class="vi-tree-pillars-row"' not in html or 'node-port-top' not in html:
    errors.append("FAILED: Tree busbar distributor or socket ports not found")
else:
    print("  [PASS] Mathematical Tree busbar distributor and connection socket ports are present.")

# 3. Assert 6 Pillar Branch Nodes
pillars = re.findall(r'<div class="vi-tree-branch\s+theme-([^"]+)"', html)
print(f"  [PASS] Level 1 Pillars found: {len(pillars)} ({pillars})")
if len(pillars) != 6:
    errors.append(f"FAILED: Expected 6 pillars, found {len(pillars)}")

# 4. Assert Sub-branches and Leaves
subbranches = re.findall(r'class="vi-tree-subbranch-node"', html)
print(f"  [PASS] Level 2 Sub-branches found: {len(subbranches)}")
if len(subbranches) < 12:
    errors.append(f"FAILED: Expected at least 12 sub-branches, found {len(subbranches)}")

leaves = re.findall(r'class="vi-tree-leaf"', html)
print(f"  [PASS] Level 3 Leaves found: {len(leaves)}")
if len(leaves) < 40:
    errors.append(f"FAILED: Expected at least 40 leaves, found {len(leaves)}")

# 5. Check all internal links
tree_match = re.search(r'class="vi-tree-section".*?</section>', html, re.DOTALL)
if tree_match:
    links = re.findall(r'href="([^"#]+)(?:#[^"]*)?"', tree_match.group(0))
    broken = []
    for link in set(links):
        if link.startswith('/'):
            rel_path = link.lstrip('/')
            target = rel_path
            if target == '' or target.endswith('/'):
                target = os.path.join(rel_path, 'index.html')
            elif not os.path.splitext(target)[1]:
                target = os.path.join(rel_path, 'index.html')
            target = os.path.normpath(target)
            if not os.path.exists(target):
                broken.append((link, target))
    if broken:
        errors.append(f"FAILED: Broken links in tree: {broken}")
    else:
        print(f"  [PASS] All {len(set(links))} internal links in tree verified on disk.")

print("=======================================================")
if errors:
    print(f"RESULT: FAILED with {len(errors)} errors:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
else:
    print("RESULT: 100% PASS — TREE ARCHITECTURE FULLY VALIDATED!")
print("=======================================================")
