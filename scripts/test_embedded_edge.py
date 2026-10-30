import subprocess
import os

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_path = os.path.abspath('data/staging/insights.html')
file_url = 'file:///' + html_path.replace('\\', '/')

cmd = [
    edge,
    '--headless=new',
    '--dump-dom',
    '--virtual-time-budget=2000',
    file_url
]

p = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', timeout=30)
dom = p.stdout
print('Dumped DOM length of real insights.html:', len(dom))

svg_ids = [
    ('Card 01 (Fiscal)', 'svg-card-fiscal'),
    ('Card 02 (Debt)', 'svg-card-debt'),
    ('Card 03 (Tax Exp)', 'svg-card-tax-exp'),
    ('Card 04 (Gender Land)', 'svg-card-gender-land'),
    ('Card 05 (HIES Food)', 'svg-card-hies'),
    ('Card 06 (Consumption Pie)', 'svg-card-consumption-pie'),
    ('Card 07 (Wage Infl)', 'svg-card-wage-infl'),
    ('Card 08 (Services)', 'svg-card-services'),
    ('Card 09 (LFS Disparities)', 'svg-card-lfs'),
    ('Card 10 (Census Shifts)', 'svg-card-census-shifts'),
    ('Card 11 (Districts Scatter)', 'svg-card-districts-scatter'),
    ('Card 12 (Sector Employment)', 'svg-card-sector-employment'),
    ('Card 13 (Agri Shifts)', 'svg-card-agri-shifts'),
    ('Card 14 (Census Hist)', 'svg-card-census-hist'),
    ('Card 15 (Macro)', 'svg-card-macro'),
    ('Card 16 (Prov Matrix)', 'svg-card-prov-matrix')
]

empty_count = 0
print('\nAuditing rendered SVG content across all 16 cards:')
for label, sid in svg_ids:
    idx = dom.find(sid)
    if idx == -1:
        print(f'  [MISSING] {label:28} : {sid}')
        empty_count += 1
    else:
        end_idx = dom.find('</svg>', idx)
        inner_content = dom[idx+len(sid)+2:end_idx].strip()
        tag_close = inner_content.find('>')
        inner_svg = inner_content[tag_close+1:].strip()
        if len(inner_svg) == 0:
            print(f'  [EMPTY]   {label:28} : {sid}')
            empty_count += 1
        else:
            print(f'  [OK]      {label:28} : {sid:28} -> {len(inner_svg):5} chars rendered')

print(f'\n======================================================')
print(f'  RESULT: {16 - empty_count}/16 INFOGRAPHICS RENDERED SUCCESSFULLY')
print(f'======================================================')

assert empty_count == 0, f'{empty_count} cards are still empty!'
