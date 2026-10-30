obs_files = [
    'data/economy/index.html',
    'data/population/index.html',
    'data/living-standards/index.html'
]

import re
for p in obs_files:
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"=== {p} ===")
    headings = re.findall(r'<h[123][^>]*>(.*?)</h[123]>', text)
    for h in headings[:10]:
        print("  ", h.strip())
