import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="vi-hero"')
if idx == -1:
    idx = text.find('class="vi-header"')
if idx == -1:
    idx = text.find('<main')

print(text[idx:idx+1500])
