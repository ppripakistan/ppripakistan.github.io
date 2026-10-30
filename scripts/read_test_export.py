with open('scripts/test_export_svg_xml.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("Length of test_export_svg_xml.py:", len(text))
print("First 35 lines:\n", '\n'.join(text.splitlines()[:35]))
