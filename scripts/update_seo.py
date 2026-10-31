import json

# 1. Update sitemap.xml
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

insights_url_entry = """  <url>
    <loc>https://ppripakistan.github.io/insights/</loc>
    <lastmod>2026-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
"""

if 'https://ppripakistan.github.io/insights/' not in sitemap:
    home_url_end = sitemap.find('</url>') + len('</url>')
    sitemap = sitemap[:home_url_end] + '\n' + insights_url_entry + sitemap[home_url_end:]
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print("sitemap.xml updated with /insights/")
else:
    print("sitemap.xml already has /insights/")

# 2. Update search-index.json
with open('search-index.json', 'r', encoding='utf-8') as f:
    search_data = json.load(f)

new_entries = [
    {
        "title": "Visual Policy Analytics & Infographics Lab",
        "type": "Interactive Visual Analytics",
        "description": "16 publication-grade interactive infographics analyzing sovereign debt, provincial budget allocations, tax expenditures, district urbanization, and 35-year macroeconomic history.",
        "url": "/insights/",
        "tags": ["visual analytics", "infographics", "debt", "budget", "provinces", "macroeconomics", "demographics", "living standards"]
    },
    {
        "title": "Provincial Resource Allocation, Debt Stock & Conflict Exposure Matrix",
        "type": "Infographic #16",
        "description": "Comparative 4-view matrix of Punjab, Sindh, Khyber Pakhtunkhwa, and Balochistan analyzing total budgets, ADP, public debt, per capita allocations, and regional conflict incidents.",
        "url": "/insights/#card-prov-matrix",
        "tags": ["provincial budget", "ADP", "provincial debt", "conflict", "terrorism", "per capita spending", "Balochistan", "KPK", "Sindh", "Punjab"]
    },
    {
        "title": "Federal Budget Allocation & Sovereign Debt Servicing Monopoly",
        "type": "Infographic #01",
        "description": "Interactive vector chart visualizing how sovereign debt markup interest absorbs over 51% of Pakistan's federal budget and 76% of net tax revenues.",
        "url": "/insights/#card-fiscal",
        "tags": ["federal budget", "debt servicing", "defence", "PSDP", "fiscal policy", "subsidies"]
    },
    {
        "title": "135 Districts Urbanization vs Population Density Quadrant Scale",
        "type": "Infographic #11",
        "description": "Interactive 2D quadrant scatter matrix plotting all 135 districts across Pakistan by urbanization percentage and population density.",
        "url": "/insights/#card-districts-scatter",
        "tags": ["districts", "urbanization", "density", "census 2023", "quadrants", "spatial"]
    },
    {
        "title": "35-Year Macroeconomic Trajectory Across 4 Regimes (FY90–FY24)",
        "type": "Infographic #15",
        "description": "Longitudinal vector trajectory tracking real GDP growth, CPI inflation, current account balances, and public debt ratios across 35 years and 4 political regimes.",
        "url": "/insights/#card-macro",
        "tags": ["macroeconomics", "GDP growth", "inflation", "debt to GDP", "current account", "regimes", "history"]
    }
]

added_count = 0
for entry in new_entries:
    if not any(item.get('url') == entry['url'] for item in search_data):
        search_data.append(entry)
        added_count += 1

with open('search-index.json', 'w', encoding='utf-8') as f:
    json.dump(search_data, f, indent=2, ensure_ascii=False)

print(f"search-index.json updated with {added_count} new entries (total: {len(search_data)})")
