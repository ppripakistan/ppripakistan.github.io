with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_end = text.find('</script>', 165000)
print("Script tag ends at:", idx_end)
print(text[idx_end:idx_end+500])
