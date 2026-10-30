with open('insights/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'vi-nav-pills' in l or 'id="card-fiscal"' in l or 'id="card-debt"' in l or 'id="card-tax-exp"' in l:
        print(f"Line {i+1}: {l.strip()[:60]}")
