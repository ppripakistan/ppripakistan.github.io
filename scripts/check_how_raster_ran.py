with open('scripts/test_png_rasterization.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('msedge')
print(text[idx-200:idx+400])
