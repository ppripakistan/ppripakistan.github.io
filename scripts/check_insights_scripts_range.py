with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx_scripts = text.find('<!-- SCRIPTS -->')
idx_footer = text.find('<footer class="site-footer">')

print(f"Scripts start: {idx_scripts}, Footer start: {idx_footer}")
print("Content right before footer (last 300 chars before footer):")
print(text[idx_footer-300:idx_footer])
