import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Jump to Infographic')
if idx != -1:
    print(text[idx-100:idx+2500])
else:
    print("Not found, searching for jump")
    idx = text.find('jump')
    print(text[idx-50:idx+1500])
