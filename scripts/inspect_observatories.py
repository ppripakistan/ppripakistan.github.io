obs_files = [
    'data/public-finance/index.html',
    'data/economy/index.html',
    'data/population/index.html',
    'data/living-standards/index.html'
]

for p in obs_files:
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"=== {p} ===")
    print(f"Length: {len(text)}")
    # Find all section tags
    import re
    sections = re.findall(r'<section[^>]*id="([^"]+)"[^>]*>', text)
    print("Section IDs:", sections)
    main_pos = text.find('<main')
    end_main_pos = text.find('</main>')
    print(f"Main tag from {main_pos} to {end_main_pos}")
