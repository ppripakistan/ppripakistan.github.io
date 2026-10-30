with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('id="section-visual-analytics"')
if idx != -1:
    end_idx = text.find('</section>', idx)
    print("Showcase section length:", end_idx - idx)
    print("Lines in showcase section:", text[idx:end_idx].count('\n'))
    print("First 300 chars:\n", text[idx:idx+300])
