import re

with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

chip_targets = re.findall(r'class="vi-chip-btn[^"]*"\s+data-target="([^"]+)"', text)
print(f"Total chip buttons found: {len(chip_targets)}")
for target in chip_targets:
    exists = f'id="{target}"' in text
    print(f"  Target: {target} -> Card Exists? {exists}")
