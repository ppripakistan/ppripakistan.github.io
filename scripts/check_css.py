with open('assets/css/visual-insights.css', 'r', encoding='utf-8') as f:
    text = f.read()

print("CSS lines:", len(text.splitlines()))
print("First 300 chars:\n", text[:300])
