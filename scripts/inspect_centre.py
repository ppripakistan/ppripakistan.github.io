with open('data/centre.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
headings = re.findall(r'<h[123][^>]*>(.*?)</h[123]>', text)
print("Headings in data/centre.html:")
for h in headings[:15]:
    print("  ", h.strip())
