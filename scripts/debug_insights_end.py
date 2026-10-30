with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

print("Text after Card 16 (chars 52544 to 54000):")
print(text[52544:54000])
print("Total file length:", len(text))
