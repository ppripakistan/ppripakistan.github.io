with open('scripts/test_png_rasterization.py', 'r', encoding='utf-8') as f:
    text = f.read()

print("test_png_rasterization.py length:", len(text))
print("First 30 lines:\n", '\n'.join(text.splitlines()[:30]))
