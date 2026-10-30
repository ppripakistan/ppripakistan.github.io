# -*- coding: utf-8 -*-
import os

# 1. Restore /ur/consultation/survey.html in ur/ pages
for root, dirs, files in os.walk('ur'):
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            if '/ur/surveys/' in c:
                new_c = c.replace('/ur/surveys/', '/ur/consultation/survey.html')
                with open(p, 'w', encoding='utf-8') as fp:
                    fp.write(new_c)
                print(f"Fixed Urdu survey link in {p}")

# Also check other files where /ur/surveys/ might have been created
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'archive' in root: continue
    for f in files:
        if f.endswith('.html'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
            if '/ur/surveys/' in c:
                new_c = c.replace('/ur/surveys/', '/ur/consultation/survey.html')
                with open(p, 'w', encoding='utf-8') as fp:
                    fp.write(new_c)
                print(f"Fixed /ur/surveys/ in {p}")

# 2. Fix archive/index.html
archive_index = 'archive/index.html'
if os.path.exists(archive_index):
    with open(archive_index, 'r', encoding='utf-8', errors='ignore') as fp:
        c = fp.read()
    if '/consultation/survey.html' in c:
        c = c.replace('/consultation/survey.html', '/surveys/')
        with open(archive_index, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print("Fixed archive/index.html")

print("Link restoration complete.")
