with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer('filterCategory', text)]
print("filterCategory occurrences at:", matches)
for pos in matches:
    print(text[max(0, pos-20):min(len(text), pos+100)])
    print("---")
