import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/downloads/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
headings = re.findall(r'<h[123][^>]*>(.*?)</h[123]>', text)
print("Headings in data/downloads/index.html:")
for h in headings:
    print("  ", h.strip())
