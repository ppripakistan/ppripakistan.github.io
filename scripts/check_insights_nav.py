with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav_start = text.find('id="site-navigation"')
print("Nav in insights/index.html:\n", text[nav_start:nav_start+450])
