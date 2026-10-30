with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Chars 52500 to 52900:")
print(text[52500:52900])
