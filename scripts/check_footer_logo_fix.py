with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="footer-logo"')
print("Footer logo snippet:")
print(text[idx-70:idx+150])
