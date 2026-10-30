import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

hero_idx = text.find('Visual Policy Analytics')
print(text[hero_idx-100:hero_idx+1200])
