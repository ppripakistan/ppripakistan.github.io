with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_footer = text.find('<footer class="site-footer">')
print("Footer position:", idx_footer)
idx_script = text.find('<script>', 52000)
print("Inline script position:", idx_script)
print("Is footer before or after inline script?")
print("Footer index:", idx_footer, "Inline script index:", idx_script)
