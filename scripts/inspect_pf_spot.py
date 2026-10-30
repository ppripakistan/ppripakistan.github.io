with open('data/public-finance/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Comprehensive Indicator Catalog')
print("Snippet around Comprehensive Indicator Catalog:\n", text[idx-250:idx+350])
