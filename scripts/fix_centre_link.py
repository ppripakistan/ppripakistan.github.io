with open('data/centre.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '<a href="/data/curated/agri_census_2024_summary.csv"'
replacement = '<a href="/data/published/agri_census_2024_summary.csv"'

if target in text:
    text = text.replace(target, replacement)
    with open('data/centre.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated data/centre.html to /data/published/agri_census_2024_summary.csv")
else:
    print("FAILED to find target in data/centre.html")
