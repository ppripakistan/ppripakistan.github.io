with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

head_start = text.find('<head>')
head_end = text.find('</head>')
print(text[head_start:head_end+7])
