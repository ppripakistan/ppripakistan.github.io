with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<section\n        class="home-section home-platform-section"'
pos = text.find(target)
if pos == -1:
    target = '<section class="home-section home-platform-section"'
    pos = text.find(target)

print("Found home-platform-section at pos:", pos)
print("Snippet around target:\n", text[pos-200:pos+100])
