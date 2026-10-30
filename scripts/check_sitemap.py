with open('sitemap.xml', 'r', encoding='utf-8') as f:
    text = f.read()

print("sitemap.xml length:", len(text))
print("Has /insights/?", '/insights/' in text)
