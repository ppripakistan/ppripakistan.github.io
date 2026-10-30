import glob

files = [
    'index.html',
    'data/centre.html',
    'data/public-finance/index.html',
    'data/economy/index.html',
    'data/population/index.html',
    'data/living-standards/index.html',
    'data/datasets.html',
    'data/downloads/index.html',
    'research/index.html',
    'provinces/index.html',
    'scenarios/index.html'
]

for p in files:
    try:
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()
        nav_start = content.find('id="site-navigation"')
        if nav_start != -1:
            nav_end = content.find('</nav>', nav_start)
            nav_snippet = content[nav_start:nav_end+6]
            has_insights = '/insights/' in nav_snippet
            print(f"{p}: has_insights={has_insights}")
        else:
            print(f"{p}: NO site-navigation FOUND")
    except Exception as e:
        print(f"{p}: error {e}")
