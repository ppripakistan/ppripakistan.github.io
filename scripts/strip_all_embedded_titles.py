import re
import os

target_files = [
    'index.html',
    'data/public-finance/index.html',
    'data/economy/index.html',
    'data/population/index.html',
    'data/living-standards/index.html'
]

title_map = {
    'Federal Budget Allocation &amp; Debt Servicing': 'Federal Budget Allocation &amp; Sovereign Debt Servicing',
    'The 8-Year Public Debt Surge (FY18–FY26)': 'The 8-Year Sovereign Public Debt Trajectory (FY18–FY26)',
    'Revenue Collection vs Tax Exemptions': 'Federal Tax Concessions &amp; Revenue Foregone',
    'Gender Demographics &amp; Land Area Asymmetry': 'Female Gender Ratios &amp; Agrarian Landholding Asymmetry',
    'Household Food Burden Divide (HIES 2024–25)': 'Household Food Engel Burden Divide (HIES 2024–25)',
    'Inter-Provincial Household Budget Allocation': 'Provincial Food vs Non-Food Household Consumption Baskets',
    'Purchasing Power Erosion: Inflation vs Wages': 'Purchasing Power Erosion: Real Wages vs Inflation',
    'Household Basic Services &amp; Utilities Access': 'Household Basic Housing Characteristics &amp; Utilities Deficit',
    'Labour Force Disparities: Gender &amp; Youth': 'Labour Force Participation &amp; Gender/Rural Wage Disparities',
    'Multi-Census Provincial Population Shares (1981–2023)': 'Multi-Census Provincial Demographic Shifts (1981–2023)',
    '135-District Urbanization &amp; Density Quadrant Scatter Bubble Map': '135-District Urbanization &amp; Population Density Quadrant Matrix',
    'Employment Distribution by Economic Sector': 'Sectoral Labour Force Absorption Dynamics',
    'Agricultural Land &amp; Cultivated Acreage Shifts': 'Smallholder Landholding &amp; Cultivated Acreage Fragmentation',
    '70-Year Intercensal Demographic Growth (1951–2023)': '70-Year Intercensal Demographic Growth Trajectory (1951–2023)',
    '35-Year Macroeconomic Trajectory (1990–2024: 4 Historical Tenures &amp; Crisis Shocks)': '35-Year Macroeconomic Trajectory (4 Regimes &amp; Crisis Shocks)',
    'Provincial Resource Allocation, Debt Stock &amp; Conflict Exposure Matrix (FY25 &amp; 2023–2024)': 'Provincial Resource Allocation, Debt Stock &amp; Conflict Exposure Matrix'
}

for path in target_files:
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex replace any <h3 class="vi-card-title">#\d+:\s*(.*?)</h3>
    def clean_title(match):
        raw = match.group(1).strip()
        # Check if mapped
        for k, v in title_map.items():
            if k in raw or raw in k:
                return f'<h3 class="vi-card-title">{v}</h3>'
        return f'<h3 class="vi-card-title">{raw}</h3>'

    new_content = re.sub(r'<h3 class="vi-card-title">#\d+:\s*(.*?)</h3>', clean_title, content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated titles in: {path}")
    else:
        print(f"No titles needed update in: {path}")

# Also update data/centre.html spotlight button
if os.path.exists('data/centre.html'):
    with open('data/centre.html', 'r', encoding='utf-8') as f:
        c_text = f.read()
    c_updated = c_text.replace('Launch Visual Insights Lab (16 Infographics)', 'Launch Visual Policy Analytics Lab')
    if c_updated != c_text:
        with open('data/centre.html', 'w', encoding='utf-8') as f:
            f.write(c_updated)
        print("Updated spotlight in data/centre.html")

print("All embedded titles de-numbered!")
