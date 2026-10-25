#!/usr/bin/env python3
"""
scripts/build_brand_assets_v2.py
Processes New Logo/NewLogo.webp and generates:
1. Header & footer logos: ppri-logo-header.jpg, ppri-logo-header.png
2. Schema & master logo: ppri-logo.jpg, ppri-logo.png (512x512 1:1 square)
3. Complete favicon suite:
   - root & brand favicon.ico (multi-res 16, 32, 48)
   - root & brand favicon.png (512x512)
   - root & brand apple-touch-icon.png (180x180)
   - brand favicon-16x16.png, favicon-32x32.png, favicon-48x48.png, icon-192.png, icon-512.png, ppri-favicon.png
4. Master social share card: ppri-social-share.jpg (1200x630)
5. Section social cards:
   - ppri-social-data-observatory.jpg
   - ppri-social-maps.jpg
   - ppri-social-scenarios.jpg
   - ppri-social-articles.jpg
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT_DIR = Path(__file__).resolve().parent.parent
BRAND_DIR = ROOT_DIR / "assets" / "images" / "brand"
RESEARCH_DIR = ROOT_DIR / "assets" / "images" / "research"
NEW_LOGO_PATH = BRAND_DIR / "ppri-logo-master.webp"

BRAND_DIR.mkdir(parents=True, exist_ok=True)
RESEARCH_DIR.mkdir(parents=True, exist_ok=True)

# Color palette
COLOR_DARK_TEAL = (7, 60, 58)      # #073c3a
COLOR_DEEP_BG   = (5, 42, 41)      # #052a29
COLOR_GOLD      = (212, 175, 55)   # #d4af37
COLOR_BORDER    = (12, 43, 38)     # #0c2b26
COLOR_WHITE     = (255, 255, 255)
COLOR_MUTED     = (203, 213, 225)  # #cbd5e1
COLOR_MUTED_URL = (148, 163, 184)  # #94a3b8

# Windows system fonts
FONT_SEGOE_BOLD = "C:/Windows/Fonts/segoeuib.ttf"
FONT_SEGOE_REG  = "C:/Windows/Fonts/segoeui.ttf"
FONT_GEORGIA_BOLD = "C:/Windows/Fonts/georgiab.ttf"
FONT_GEORGIA_REG  = "C:/Windows/Fonts/georgia.ttf"

def load_master_logo():
    if not NEW_LOGO_PATH.exists():
        raise FileNotFoundError(f"Master logo not found at {NEW_LOGO_PATH}")
    return Image.open(NEW_LOGO_PATH).convert('RGB')

def get_cropped_composite_square(im):
    """
    Crops the composite logo (emblem + PPRI + subtitle) tightly and places it on a clean square canvas.
    Composite bbox: X: 336..1678, Y: 368..1639.
    Center is ~(1007, 1003). Height is 1271, width is 1342.
    """
    w, h = im.size
    cx, cy = 1007, 1003
    half_size = int(max(1342, 1271) * 0.55) # ~738
    box = (max(0, cx - half_size), max(0, cy - half_size), min(w, cx + half_size), min(h, cy + half_size))
    cropped = im.crop(box)
    square = Image.new('RGB', (half_size * 2, half_size * 2), (255, 255, 255))
    square.paste(cropped, (0, 0))
    return square

def get_emblem_square(im):
    """
    Extracts the circular emblem alone (Y: 368..1044).
    Emblem center is ~(1007, 706). Diameter is ~676.
    """
    cx, cy = 1007, 706
    r = int(338 * 1.08) # ~365
    box = (cx - r, cy - r, cx + r, cy + r)
    cropped = im.crop(box)
    square = Image.new('RGB', (r * 2, r * 2), (255, 255, 255))
    square.paste(cropped, (0, 0))
    return square

def generate_logo_and_favicons():
    print("Loading NewLogo.webp...")
    master = load_master_logo()
    composite_square = get_cropped_composite_square(master)
    emblem_square = get_emblem_square(master)

    # 1. ppri-logo.jpg & ppri-logo.png (512x512 1:1 square for schema and master branding)
    print("Generating ppri-logo.png and ppri-logo.jpg (512x512)...")
    logo_512 = composite_square.resize((512, 512), Image.Resampling.LANCZOS)
    logo_512.save(BRAND_DIR / "ppri-logo.png", format="PNG", optimize=True)
    logo_512.save(BRAND_DIR / "ppri-logo.jpg", format="JPEG", quality=95, optimize=True)

    # 2. ppri-logo-header.png & ppri-logo-header.jpg (240x240 for header badge and footer)
    print("Generating ppri-logo-header.png and ppri-logo-header.jpg (240x240)...")
    logo_240 = composite_square.resize((240, 240), Image.Resampling.LANCZOS)
    logo_240.save(BRAND_DIR / "ppri-logo-header.png", format="PNG", optimize=True)
    logo_240.save(BRAND_DIR / "ppri-logo-header.jpg", format="JPEG", quality=95, optimize=True)

    # 3. Favicon suite
    print("Generating Favicon suite...")
    # Root & Brand favicon.png (512x512)
    fav_512 = emblem_square.resize((512, 512), Image.Resampling.LANCZOS)
    fav_512.save(ROOT_DIR / "favicon.png", format="PNG", optimize=True)
    fav_512.save(BRAND_DIR / "favicon.png", format="PNG", optimize=True)

    # Root & Brand apple-touch-icon.png (180x180)
    apple_180 = emblem_square.resize((180, 180), Image.Resampling.LANCZOS)
    apple_180.save(ROOT_DIR / "apple-touch-icon.png", format="PNG", optimize=True)
    apple_180.save(BRAND_DIR / "apple-touch-icon.png", format="PNG", optimize=True)

    # Standard favicon PNG sizes
    for sz, name in [(16, "favicon-16x16.png"), (32, "favicon-32x32.png"), (48, "favicon-48x48.png"), (192, "icon-192.png"), (512, "icon-512.png"), (192, "ppri-favicon.png")]:
        resized = emblem_square.resize((sz, sz), Image.Resampling.LANCZOS)
        resized.save(BRAND_DIR / name, format="PNG", optimize=True)

    # Multi-resolution favicon.ico (16, 32, 48)
    fav_ico_master = emblem_square.resize((48, 48), Image.Resampling.LANCZOS)
    fav_ico_master.save(ROOT_DIR / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    fav_ico_master.save(BRAND_DIR / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])

    return emblem_square, composite_square

def draw_social_card(emblem, badge_text, title, desc, meta_text, output_path):
    W, H = 1200, 630
    card = Image.new('RGB', (W, H), COLOR_DARK_TEAL)
    draw = ImageDraw.Draw(card)

    # Decorative Borders
    draw.rectangle([(20, 20), (W-21, H-21)], outline=COLOR_GOLD, width=2)
    draw.rectangle([(26, 26), (W-27, H-27)], outline=COLOR_BORDER, width=1)

    # Top Header Bar: Emblem + Institute Name
    emb_resized = emblem.resize((84, 84), Image.Resampling.LANCZOS)
    card.paste(emb_resized, (50, 46))

    f_header = ImageFont.truetype(FONT_SEGOE_BOLD, 26)
    f_sub_header = ImageFont.truetype(FONT_SEGOE_BOLD, 16)
    f_badge = ImageFont.truetype(FONT_SEGOE_BOLD, 16)
    f_title = ImageFont.truetype(FONT_GEORGIA_BOLD, 42)
    f_desc = ImageFont.truetype(FONT_SEGOE_REG, 21)
    f_meta = ImageFont.truetype(FONT_SEGOE_REG, 18)
    f_url = ImageFont.truetype(FONT_SEGOE_BOLD, 18)

    draw.text((148, 56), "PAKISTAN PROVINCIAL REFORM INSTITUTE", font=f_header, fill=COLOR_WHITE)
    draw.text((148, 92), "RESEARCH, DATA & PUBLIC POLICY OBSERVATORY", font=f_sub_header, fill=COLOR_GOLD)
    draw.line([(50, 145), (W-50, 145)], fill=COLOR_GOLD, width=2)

    # Category / Badge
    badge_box = draw.textbbox((0, 0), badge_text, font=f_badge)
    badge_w = badge_box[2] - badge_box[0] + 28
    draw.rectangle([(50, 175), (50 + badge_w, 210)], fill=COLOR_GOLD)
    draw.text((64, 182), badge_text, font=f_badge, fill=COLOR_DARK_TEAL)

    # Title
    draw.text((50, 235), title, font=f_title, fill=COLOR_WHITE, spacing=10)

    # Description
    draw.text((50, 385), desc, font=f_desc, fill=COLOR_MUTED, spacing=8)

    # Bottom Footer Bar
    draw.line([(50, 520), (W-50, 520)], fill=(20, 80, 75), width=1)
    draw.text((50, 545), meta_text, font=f_meta, fill=COLOR_GOLD)
    draw.text((W-340, 545), "https://ppripakistan.github.io", font=f_url, fill=COLOR_MUTED_URL)

    card.save(output_path, format="JPEG", quality=94, optimize=True)
    print(f"  Generated {output_path.name} (1200x630)")

def generate_social_cards(emblem):
    print("Generating Master & Section Social Preview Cards (1200x630)...")

    # 1. Master Social Share
    draw_social_card(
        emblem,
        badge_text="OFFICIAL POLICY OBSERVATORY",
        title="Pakistan Provincial Reform Institute\nData, Research & Constitutional Analysis",
        desc="Empirical research, cartographic modeling, and public-policy analysis on provincial\nrestructuring, NFC award fiscal federalism, and municipal devolution in Pakistan.",
        meta_text="Non-Partisan Policy Research Institute - Islamabad & Subnational Hubs",
        output_path=BRAND_DIR / "ppri-social-share.jpg"
    )

    # 2. Data Observatory
    draw_social_card(
        emblem,
        badge_text="PPRI DATA OBSERVATORY",
        title="Interactive Subnational Data Atlas\nCensus 2023 & Socio-Economic Indicators",
        desc="Explore Pakistan's verified public data: population, fiscal distribution, health,\neducation, digital access, and NFC divisible pool simulation across all provinces.",
        meta_text="Pakistan Bureau of Statistics & State Bank of Pakistan Verified Records",
        output_path=BRAND_DIR / "ppri-social-data-observatory.jpg"
    )

    # 3. Maps & GIS Hub
    draw_social_card(
        emblem,
        badge_text="CARTOGRAPHY & GIS OBSERVATORY",
        title="Maps & Territorial Analysis:\nAdministrative Units & Reorganization Scenarios",
        desc="High-resolution cartographic data distinguishing constitutional administrative units,\n38 divisions, 164 districts, and illustrative boundary reorganization scenarios.",
        meta_text="PPRI Geo-Spatial Data Hub - Cartographic Boundary Modeling",
        output_path=BRAND_DIR / "ppri-social-maps.jpg"
    )

    # 4. Scenarios Lab
    draw_social_card(
        emblem,
        badge_text="POLICY SCENARIOS LAB",
        title="Provincial Reorganization Scenarios:\nComparative Federalism & Governance Models",
        desc="Quantitative models evaluating administrative scale, local government empowerment,\nsenate representation parity, and fiscal viability across 4 to 12 provincial units.",
        meta_text="Constitutional Law & Subnational Governance Evaluation",
        output_path=BRAND_DIR / "ppri-social-scenarios.jpg"
    )

    # 5. Articles & Policy Analysis
    draw_social_card(
        emblem,
        badge_text="PPRI POLICY ANALYSIS",
        title="Devolution, Federalism & Governance:\nIndependent Policy Insights on Pakistan",
        desc="Evidence-based policy briefs and analytical articles examining the 18th Amendment,\nlocal government sustainability, secondary city development, and subnational reform.",
        meta_text="Pakistan Provincial Reform Institute Policy Series",
        output_path=BRAND_DIR / "ppri-social-articles.jpg"
    )

if __name__ == '__main__':
    emblem, composite = generate_logo_and_favicons()
    generate_social_cards(emblem)
    print("All logo, favicon, and social card assets successfully generated!")
