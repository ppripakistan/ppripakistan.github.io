with open('assets/js/modules/visual-insights.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
window_props = re.findall(r'window\.([a-zA-Z0-9_]+)\s*=', text)
print("Window properties assigned in visual-insights.js:")
for p in sorted(window_props):
    print("  window." + p)
