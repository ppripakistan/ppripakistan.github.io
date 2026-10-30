with open('scripts/build_insights_html.py', 'r', encoding='utf-8') as f:
    text = f.read()

with open('scripts/build_insights_html.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="card-macro"')
print(text[idx+2500:idx+3300])
