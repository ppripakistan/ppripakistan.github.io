with open('data/downloads/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of data/downloads/index.html:", len(text))
nav_start = text.find('id="site-navigation"')
print("Nav snippet:\n", text[nav_start:nav_start+300])
