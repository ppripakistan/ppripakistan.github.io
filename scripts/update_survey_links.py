# -*- coding: utf-8 -*-
import os
import re
import json

# 1. Update search-index.json
with open('search-index.json', 'r', encoding='utf-8') as f:
    s_data = json.load(f)

s_data_filtered = [item for item in s_data if item.get('url') != '/consultation/survey.html']
with open('search-index.json', 'w', encoding='utf-8') as f:
    json.dump(s_data_filtered, f, indent=2, ensure_ascii=False)
print("Updated search-index.json (removed /consultation/survey.html)")

# 2. Update sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

# Match <url> ... https://ppripakistan.github.io/consultation/survey.html ... </url>
sitemap_updated = re.sub(
    r'\s*<url>\s*<loc>https://ppripakistan\.github\.io/consultation/survey\.html</loc>.*?</url>',
    '',
    sitemap_content,
    flags=re.DOTALL
)
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_updated)
print("Updated sitemap.xml (removed consultation/survey.html)")

# 3. Update all html files
updated_count = 0
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'archive' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            if 'consultation/survey.html' in content:
                new_c = content.replace('href="/consultation/survey.html"', 'href="/surveys/"')
                new_c = new_c.replace('href="https://ppripakistan.github.io/consultation/survey.html"', 'href="https://ppripakistan.github.io/surveys/"')
                new_c = new_c.replace('href="/consultation/survey.html#', 'href="/surveys/#')
                new_c = new_c.replace('href="survey.html"', 'href="/surveys/"')
                new_c = new_c.replace('<link rel="alternate" hreflang="en" href="https://ppripakistan.github.io/consultation/survey.html" />', '<link rel="alternate" hreflang="en" href="https://ppripakistan.github.io/surveys/" />')
                new_c = new_c.replace('<link rel="alternate" hreflang="x-default" href="https://ppripakistan.github.io/consultation/survey.html" />', '<link rel="alternate" hreflang="x-default" href="https://ppripakistan.github.io/surveys/" />')
                new_c = new_c.replace('https://ppripakistan.github.io/consultation/survey.html', 'https://ppripakistan.github.io/surveys/')
                new_c = new_c.replace('/consultation/survey.html', '/surveys/')
                
                if new_c != content:
                    with open(p, 'w', encoding='utf-8') as fp:
                        fp.write(new_c)
                    updated_count += 1

print(f"Updated {updated_count} HTML files to link to /surveys/")
