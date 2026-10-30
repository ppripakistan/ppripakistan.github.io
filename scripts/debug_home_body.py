with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

body_close = text.rfind('</body>')
print("Snippet before </body>:\n", text[body_close-300:body_close])
