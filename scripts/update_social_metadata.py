#!/usr/bin/env python3
import glob
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

def update_social_images(file_path, new_image_url):
    p = Path(file_path)
    if not p.is_absolute():
        p = ROOT_DIR / p
    if not p.exists():
        print(f"Skipping non-existent: {p}")
        return

    content = p.read_text(encoding='utf-8')

    # Replace og:image
    content = re.sub(
        r'<meta\s+property=[\'"]og:image[\'"]\s+content=[\'"][^\'"]+[\'"]\s*/?>',
        f'<meta property="og:image" content="{new_image_url}" />',
        content
    )
    # Replace og:image:secure_url
    content = re.sub(
        r'<meta\s+property=[\'"]og:image:secure_url[\'"]\s+content=[\'"][^\'"]+[\'"]\s*/?>',
        f'<meta property="og:image:secure_url" content="{new_image_url}" />',
        content
    )
    # Replace twitter:image
    content = re.sub(
        r'<meta\s+name=[\'"]twitter:image[\'"]\s+content=[\'"][^\'"]+[\'"]\s*/?>',
        f'<meta name="twitter:image" content="{new_image_url}" />',
        content
    )
    p.write_text(content, encoding='utf-8')
    print(f"Updated social image in {p.relative_to(ROOT_DIR)}")

def main():
    # 1. Bespoke Research Reports
    bespoke_reports = {
        'research/reports/income-went-up-why-does-life-feel-harder.html': 'https://ppripakistan.github.io/assets/images/research/ppri-rep01-income-inflation.jpg',
        'research/reports/does-money-work-better-spent-closer-to-people.html': 'https://ppripakistan.github.io/assets/images/research/ppri-rep02-fiscal-decentralization.jpg',
        'research/reports/bribe-you-cant-see-corruption-private-tax.html': 'https://ppripakistan.github.io/assets/images/research/ppri-rep03-invisible-tax-corruption.jpg',
        'research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html': 'https://ppripakistan.github.io/assets/images/research/ppri-rep04-bureaucracy-friction.jpg',
        'research/reports/same-country-different-life-district-access.html': 'https://ppripakistan.github.io/assets/images/research/ppri-rep05-district-inequality.jpg',
        'research/policy-papers/provincial-reorganization-of-pakistan.html': 'https://ppripakistan.github.io/assets/images/research/ppri-pp01-provincial-reorganization.jpg'
    }

    for path, img_url in bespoke_reports.items():
        update_social_images(path, img_url)

    # 2. Data Observatory
    obs_img = 'https://ppripakistan.github.io/assets/images/brand/ppri-social-data-observatory.jpg'
    update_social_images('data/centre.html', obs_img)
    for p in glob.glob(str(ROOT_DIR / 'data' / '*' / 'index.html')):
        update_social_images(p, obs_img)

    # 3. Maps
    maps_img = 'https://ppripakistan.github.io/assets/images/brand/ppri-social-maps.jpg'
    for p in glob.glob(str(ROOT_DIR / 'maps' / '**' / '*.html'), recursive=True):
        if 'scenarios' not in p:
            update_social_images(p, maps_img)

    # 4. Scenarios
    scen_img = 'https://ppripakistan.github.io/assets/images/brand/ppri-social-scenarios.jpg'
    for p in glob.glob(str(ROOT_DIR / 'scenarios' / '**' / '*.html'), recursive=True):
        update_social_images(p, scen_img)
    update_social_images('maps/scenarios/index.html', scen_img)

    # 5. Articles
    articles_img = 'https://ppripakistan.github.io/assets/images/brand/ppri-social-articles.jpg'
    for p in glob.glob(str(ROOT_DIR / 'articles' / '*.html')):
        update_social_images(p, articles_img)

    print("All social preview images updated successfully!")

if __name__ == '__main__':
    main()
