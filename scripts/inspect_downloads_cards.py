import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/downloads/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Available Datasets (CSV Format)')
print("Snippet around Available Datasets:\n", text[idx-50:idx+900])
