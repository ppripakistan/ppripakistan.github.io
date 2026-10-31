import re

with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

card_ids = [
    'card-fiscal',
    'card-debt',
    'card-tax-exp',
    'card-gender-land',
    'card-hies',
    'card-consumption-pie',
    'card-wage-infl',
    'card-services',
    'card-lfs',
    'card-census-shifts',
    'card-districts-scatter',
    'card-sector-employment',
    'card-agri-shifts',
    'card-census-hist',
    'card-macro',
    'card-prov-matrix'
]

# Find positions of all cards
card_blocks = {}
for i, cid in enumerate(card_ids):
    start = text.find(f'id="{cid}"')
    if start == -1:
        print(f"NOT FOUND: {cid}")
        continue
    # Find preceding card start tag '<div class="vi-card'
    div_start = text.rfind('<div class="vi-card', 0, start)
    # The end is right before the next card or before the end of vi-grid
    if i < len(card_ids) - 1:
        next_cid = card_ids[i+1]
        next_start = text.find(f'id="{next_cid}"')
        next_div = text.rfind('<div class="vi-card', 0, next_start)
        block = text[div_start:next_div].rstrip()
    else:
        # last card: prov-matrix, ends before </div>\n    </div>\n  </main>
        end_grid = text.find('</div>\n    </div>\n  </main>', div_start)
        if end_grid == -1:
            end_grid = text.find('</div>\r\n    </div>\r\n  </main>', div_start)
        if end_grid == -1:
            end_grid = text.find('<!-- FOOTER', div_start)
        block = text[div_start:end_grid].rstrip()
    card_blocks[cid] = block
    print(f"{cid}: block length = {len(block)}")

print(f"Total extracted: {len(card_blocks)}")
