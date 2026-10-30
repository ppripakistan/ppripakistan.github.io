with open('data/datasets.html', 'r', encoding='utf-8') as f:
    text = f.read()

hdr_idx = text.find('<header')
print("Header in data/datasets.html:")
print(text[hdr_idx:hdr_idx+600])
