import os
import re

hub_files = [
    'index.html',
    'data/centre.html',
    'data/public-finance/index.html',
    'data/economy/index.html',
    'data/population/index.html',
    'data/living-standards/index.html',
    'data/downloads/index.html',
    'research/index.html',
    'provinces/index.html',
    'scenarios/index.html'
]

insights_link = '<a href="/insights/">Insights</a>\n          '

for path in hub_files:
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already added
    if '<a href="/insights/">Insights</a>' in content or '<a href="/insights/"' in content:
        print(f"Already has insights link: {path}")
        continue
    
    # We want to insert before <a href="/data/centre.html"
    target = '<a href="/data/centre.html"'
    if target in content:
        # Find indent before target if possible
        pos = content.find(target)
        # Check line indentation
        line_start = content.rfind('\n', 0, pos) + 1
        indent = content[line_start:pos]
        insertion = f'<a href="/insights/">Insights</a>\n{indent}'
        new_content = content[:pos] + insertion + content[pos:]
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated nav in: {path}")
    else:
        print(f"Target <a href=\"/data/centre.html\" not found in: {path}")

print("Nav update completed.")
