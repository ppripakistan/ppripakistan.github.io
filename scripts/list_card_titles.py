import re

with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

titles = re.findall(r'<h3 class="vi-card-title">(.*?)</h3>', text)
print(f"Total card titles in insights/index.html: {len(titles)}")
for i, t in enumerate(titles):
    print(f"  {i+1}: {t}")
