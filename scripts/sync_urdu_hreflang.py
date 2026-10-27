#!/usr/bin/env python3
"""
scripts/sync_urdu_hreflang.py
Injects reciprocal hreflang tags into English counterpart pages.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAIRS = [
    ('index.html', 'https://ppripakistan.github.io/', 'https://ppripakistan.github.io/ur/'),
    ('about.html', 'https://ppripakistan.github.io/about.html', 'https://ppripakistan.github.io/ur/about.html'),
    ('consultation/index.html', 'https://ppripakistan.github.io/consultation/', 'https://ppripakistan.github.io/ur/consultation/index.html'),
    ('consultation/survey.html', 'https://ppripakistan.github.io/consultation/survey.html', 'https://ppripakistan.github.io/ur/consultation/survey.html'),
    ('provinces/index.html', 'https://ppripakistan.github.io/provinces/', 'https://ppripakistan.github.io/ur/provinces/index.html'),
    ('data/centre.html', 'https://ppripakistan.github.io/data/centre.html', 'https://ppripakistan.github.io/ur/data/centre.html'),
    ('research/index.html', 'https://ppripakistan.github.io/research/', 'https://ppripakistan.github.io/ur/research/index.html'),
    ('research/reports/index.html', 'https://ppripakistan.github.io/research/reports/', 'https://ppripakistan.github.io/ur/research/reports/index.html'),
    ('research/reports/income-went-up-why-does-life-feel-harder.html', 'https://ppripakistan.github.io/research/reports/income-went-up-why-does-life-feel-harder.html', 'https://ppripakistan.github.io/ur/research/reports/income-went-up-why-does-life-feel-harder.html'),
    ('research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html', 'https://ppripakistan.github.io/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html', 'https://ppripakistan.github.io/ur/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html'),
    ('research/reports/same-country-different-life-district-access.html', 'https://ppripakistan.github.io/research/reports/same-country-different-life-district-access.html', 'https://ppripakistan.github.io/ur/research/reports/same-country-different-life-district-access.html'),
    ('research/reports/bribe-you-cant-see-corruption-private-tax.html', 'https://ppripakistan.github.io/research/reports/bribe-you-cant-see-corruption-private-tax.html', 'https://ppripakistan.github.io/ur/research/reports/bribe-you-cant-see-corruption-private-tax.html'),
    ('research/reports/does-money-work-better-spent-closer-to-people.html', 'https://ppripakistan.github.io/research/reports/does-money-work-better-spent-closer-to-people.html', 'https://ppripakistan.github.io/ur/research/reports/does-money-work-better-spent-closer-to-people.html'),
]

def main():
    for rel_path, en_url, ur_url in PAIRS:
        file_path = ROOT / rel_path
        if not file_path.exists():
            print(f"Missing: {rel_path}")
            continue
        content = file_path.read_text(encoding="utf-8")
        if 'hreflang="ur"' in content:
            print(f"Already has hreflang ur: {rel_path}")
            continue
        
        hreflang_block = f"""    <link rel="alternate" hreflang="en" href="{en_url}" />
    <link rel="alternate" hreflang="ur" href="{ur_url}" />
    <link rel="alternate" hreflang="x-default" href="{en_url}" />"""
        
        # Look for canonical link
        import re
        can_match = re.search(r'(<link\s+rel=["\']canonical["\'][^>]*>)', content, re.IGNORECASE)
        if can_match:
            matched_tag = can_match.group(1)
            new_content = content.replace(matched_tag, matched_tag + "\n" + hreflang_block, 1)
            file_path.write_text(new_content, encoding="utf-8")
            print(f"Injected hreflang after canonical in: {rel_path}")
        else:
            new_content = content.replace("</head>", hreflang_block + "\n  </head>", 1)
            file_path.write_text(new_content, encoding="utf-8")
            print(f"Injected hreflang before </head> in: {rel_path}")

if __name__ == "__main__":
    main()
