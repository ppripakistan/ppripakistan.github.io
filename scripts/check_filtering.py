with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_script = text.find('<script>', 52000)
idx_end_script = text.find('</script>', idx_script)
inline_script = text[idx_script:idx_end_script]

# Check for filterCategory in inline script vs visual-insights.js
print("filterCategory in inline_script?", 'filterCategory' in inline_script)

with open('assets/js/modules/visual-insights.js', 'r', encoding='utf-8') as f:
    mod_script = f.read()
print("filterCategory in visual-insights.js?", 'filterCategory' in mod_script)
