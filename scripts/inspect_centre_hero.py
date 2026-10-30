import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/centre.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('THEMATIC DOMAIN ATLAS')
print("Before THEMATIC DOMAIN ATLAS:\n", text[idx-600:idx])
