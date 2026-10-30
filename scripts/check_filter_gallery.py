with open('assets/js/modules/visual-insights.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('window.filterGallery')
print(text[idx:idx+500])
