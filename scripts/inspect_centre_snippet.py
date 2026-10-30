import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/centre.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Explore Pakistan by Thematic Domain')
print("Snippet:\n", text[idx-100:idx+800])
