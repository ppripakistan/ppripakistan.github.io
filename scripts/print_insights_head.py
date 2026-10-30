import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('insights/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(''.join(lines[95:215]))
