#!/usr/bin/env python3
"""
scripts/build_brand_assets.py
Generates the complete suite of brand assets:
1. Favicon suite: favicon.ico, favicon.svg, favicon-16x16, 32x32, 48x48, apple-touch-icon, icon-192, icon-512
2. Master social share card: assets/images/brand/ppri-social-share.jpg (1200x630)
3. Flagship publication cards in assets/images/research/ (1200x630)
4. Updated ppri-logo.jpg (1200x630)
"""

import os
import io
import base64
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT_DIR = Path(__file__).resolve().parent.parent
BRAND_DIR = ROOT_DIR / "assets" / "images" / "brand"
RESEARCH_DIR = ROOT_DIR / "assets" / "images" / "research"

BRAND_DIR.mkdir(parents=True, exist_ok=True)
RESEARCH_DIR.mkdir(parents=True, exist_ok=True)

# Colors
COLOR_DARK_TEAL = (7, 60, 58)      # #073c3a
COLOR_DEEP_BG   = (5, 42, 41)      # #052a29
COLOR_GOLD      = (212, 175, 55)   # #d4af37
COLOR_BORDER    = (12, 43, 38)     # #0c2b26
COLOR_WHITE     = (255, 255, 255)
COLOR_MUTED     = (203, 213, 225)  # #cbd5e1
COLOR_MUTED_URL = (148, 163, 184)  # #94a3b8

# Fonts
FONT_SEGOE_BOLD = "C:/Windows/Fonts/segoeuib.ttf"
FONT_SEGOE_REG  = "C:/Windows/Fonts/segoeui.ttf"
FONT_GEORGIA_BOLD = "C:/Windows/Fonts/georgiab.ttf"
FONT_GEORGIA_REG  = "C:/Windows/Fonts/georgia.ttf"

def extract_master_emblem():
    """Extracts the high-resolution circular emblem from the original logo with clean transparency."""
    # Obtain original 1408x768 logo from git history (commit 0591f44)
    out = subprocess.check_output(['git', 'show', '0591f44:assets/images/brand/ppri-logo.jpg'], cwd=ROOT_DIR)
    orig_logo = Image.open(io.BytesIO(out)).convert('RGBA')

    # Bounding box of emblem in original logo: X: 492..914, Y: 8..421
    # Center is (703, 214.5). Crop a square around it.
    padded = Image.new('RGBA', (orig_logo.width, orig_logo.height + 40), (235, 236, 231, 255))
    padded.paste(orig_logo, (0, 20))
    # Emblem center is at (703, 234.5). Square size 450x450
    crop_box = (703 - 225, 235 - 225, 703 + 225, 235 + 225)
    emblem_raw = padded.crop(crop_box)

    # Flood fill exterior background with transparency
    pixels = emblem_raw.load()
    w, h = emblem_raw.size
    from collections import deque
    q = deque([(0, 0), (w-1, 0), (0, h-1), (w-1, h-1), (0, h//2), (w-1, h//2), (w//2, 0), (w//2, h-1)])
    visited = set(q)

    def is_bg(r, g, b):
        lum = 0.299 * r + 0.587 * g + 0.114 * b
        return lum > 215 and abs(r - g) < 22 and abs(g - b) < 22

    while q:
        x, y = q.popleft()
        pixels[x, y] = (0, 0, 0, 0)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                r, g, b, a = pixels[nx, ny]
                if is_bg(r, g, b):
                    visited.add((nx, ny))
                    q.append((nx, ny))

    return emblem_raw

def build_favicons(master_emblem):
    print("Building Favicon Suite...")
    # 1. Standard PNG sizes
    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "favicon-48x48.png": 48,
        "icon-192.png": 192,
        "icon-512.png": 512,
        "ppri-favicon.png": 192,
    }
    for filename, sz in sizes.items():
        resized = master_emblem.resize((sz, sz), Image.Resampling.LANCZOS)
        resized.save(BRAND_DIR / filename, format="PNG")
        print(f"  Generated {filename} ({sz}x{sz})")

    # 2. Apple Touch Icon (180x180 with subtle margin on solid/subtle institutional background)
    apple_icon = Image.new("RGBA", (180, 180), (255, 255, 255, 255))
    emb_150 = master_emblem.resize((150, 150), Image.Resampling.LANCZOS)
    apple_icon.paste(emb_150, (15, 15), emb_150)
    apple_icon.convert("RGB").save(ROOT_DIR / "apple-touch-icon.png", format="PNG")
    apple_icon.convert("RGB").save(BRAND_DIR / "apple-touch-icon.png", format="PNG")
    print("  Generated apple-touch-icon.png (180x180)")

    # 3. Multi-resolution favicon.ico (16, 32, 48)
    ico_img = master_emblem.resize((48, 48), Image.Resampling.LANCZOS)
    ico_img.save(ROOT_DIR / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    ico_img.save(BRAND_DIR / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print("  Generated favicon.ico (16/32/48 mipmaps) in root and brand/")

    # 4. Scalable SVG favicon
    emb_buf = io.BytesIO()
    master_emblem.save(emb_buf, format="PNG")
    b64_data = base64.b64encode(emb_buf.getvalue()).decode('ascii')
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 450" width="100%" height="100%">
  <image width="450" height="450" href="data:image/png;base64,{b64_data}"/>
</svg>'''
    (ROOT_DIR / "favicon.svg").write_text(svg_content, encoding="utf-8")
    (BRAND_DIR / "favicon.svg").write_text(svg_content, encoding="utf-8")
    print("  Generated favicon.svg in root and brand/")

def build_default_social_cards(master_emblem):
    print("Building Default Social Share Cards...")
    W, H = 1200, 630

    # Option A: Institutional Dark Teal Card (Primary)
    card = Image.new('RGB', (W, H), COLOR_DARK_TEAL)
    draw = ImageDraw.Draw(card)

    # Double borders: Outer gold, inner subtle
    draw.rectangle([(20, 20), (W-21, H-21)], outline=COLOR_GOLD, width=2)
    draw.rectangle([(26, 26), (W-27, H-27)], outline=COLOR_BORDER, width=1)

    # Centered Emblem
    emb = master_emblem.resize((200, 200), Image.Resampling.LANCZOS)
    card.paste(emb, ((W - 200)//2, 60), emb)

    # Typography
    f_title = ImageFont.truetype(FONT_SEGOE_BOLD, 62)
    f_sub = ImageFont.truetype(FONT_SEGOE_BOLD, 24)
    f_tag = ImageFont.truetype(FONT_GEORGIA_REG, 21)
    f_url = ImageFont.truetype(FONT_SEGOE_BOLD, 22)

    def draw_centered(y, text, font, fill):
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw)//2, y), text, font=font, fill=fill)

    draw_centered(280, "PPRI", f_title, COLOR_WHITE)
    draw_centered(362, "PAKISTAN PROVINCIAL REFORM INSTITUTE", f_sub, COLOR_GOLD)
    draw.line([((W-320)//2, 415), ((W+320)//2, 415)], fill=COLOR_GOLD, width=2)
    draw_centered(442, "Independent Public Policy Research & Subnational Governance Engineering", f_tag, COLOR_MUTED)
    draw_centered(530, "https://ppripakistan.github.io", f_url, COLOR_MUTED_URL)

    # Save as ppri-social-share.jpg (satisfies existing links) and ppri-logo.jpg (1200x630)
    card.save(BRAND_DIR / "ppri-social-share.jpg", format="JPEG", quality=94, optimize=True)
    card.save(BRAND_DIR / "ppri-logo.jpg", format="JPEG", quality=94, optimize=True)
    print(f"  Generated ppri-social-share.jpg and ppri-logo.jpg ({W}x{H})")

def build_research_publication_cards(master_emblem):
    print("Building Flagship Research Social Cards...")
    W, H = 1200, 630

    publications = [
        {
            "filename": "ppri-rep01-income-inflation.jpg",
            "badge": "FLAGSHIP RESEARCH REPORT · PPRI-REP-01",
            "title": "Income Went Up. So Why Does\nLife Feel Harder?",
            "desc": "An empirical investigation into Pakistan's household squeeze:\nnominal income nearly doubled while food insecurity, poverty, and essential living costs rose.",
            "meta": "Verified PBS Household Integrated Economic Survey (HIES) & Inflation Microdata"
        },
        {
            "filename": "ppri-rep02-fiscal-decentralization.jpg",
            "badge": "FLAGSHIP RESEARCH REPORT · PPRI-REP-02",
            "title": "Does Money Work Better When\nSpent Closer to the People?",
            "desc": "Evaluating local government public finance, allocative efficiency, and social delivery\nacross Pakistan's 134 districts under Article 140A devolution frameworks.",
            "meta": "Empirical Subnational Budget Analysis & Municipal Service Delivery Metrics"
        },
        {
            "filename": "ppri-rep03-invisible-tax-corruption.jpg",
            "badge": "FLAGSHIP RESEARCH REPORT · PPRI-REP-03",
            "title": "The Bribe You Can't See:\nCorruption as an Invisible Private Tax",
            "desc": "Quantifying informal transaction fees, bureaucratic delay costs, and administrative\nrent extraction on small businesses and ordinary households in Pakistan.",
            "meta": "Empirical Governance Friction Index & Citizen Survey Microdata"
        },
        {
            "filename": "ppri-rep04-bureaucracy-friction.jpg",
            "badge": "FLAGSHIP RESEARCH REPORT · PPRI-REP-04",
            "title": "The Price of a Simple Task:\nQuantifying Bureaucracy Cost",
            "desc": "Measuring citizen time, paperwork requirements, discretionary extortion, and\ninformal payments across common public service interfaces.",
            "meta": "Administrative Transaction Cost Analysis across Federal & Provincial Tiers"
        },
        {
            "filename": "ppri-rep05-district-inequality.jpg",
            "badge": "FLAGSHIP RESEARCH REPORT · PPRI-REP-05",
            "title": "Same Country, Different Life:\nMeasuring District Service Inequality",
            "desc": "Granular divergence metrics across clean water access, childhood nutrition, primary\neducation quality, and court adjudication velocity across 130+ districts.",
            "meta": "Pakistan Bureau of Statistics 7th Census & Multiple Indicator Cluster Surveys"
        },
        {
            "filename": "ppri-pp01-provincial-reorganization.jpg",
            "badge": "FLAGSHIP POLICY PAPER · PPRI-PP-001",
            "title": "The Provincial Reorganization\nof Pakistan: Restructuring Scale",
            "desc": "Examining whether 4 provincial administrations are structurally capable of governing\na federation of 241.5 million citizens. Quantitative models for constitutional reform.",
            "meta": "Constitutional Frameworks, Senate Parity, and NFC Fiscal Distribution Models"
        }
    ]

    # Shared assets for research cards
    emb = master_emblem.resize((84, 84), Image.Resampling.LANCZOS)
    f_header = ImageFont.truetype(FONT_SEGOE_BOLD, 26)
    f_sub_header = ImageFont.truetype(FONT_SEGOE_BOLD, 16)
    f_badge = ImageFont.truetype(FONT_SEGOE_BOLD, 16)
    f_title = ImageFont.truetype(FONT_GEORGIA_BOLD, 42)
    f_desc = ImageFont.truetype(FONT_SEGOE_REG, 21)
    f_meta = ImageFont.truetype(FONT_SEGOE_REG, 18)
    f_url = ImageFont.truetype(FONT_SEGOE_BOLD, 18)

    for pub in publications:
        card = Image.new('RGB', (W, H), COLOR_DARK_TEAL)
        draw = ImageDraw.Draw(card)

        # Borders
        draw.rectangle([(20, 20), (W-21, H-21)], outline=COLOR_GOLD, width=2)
        draw.rectangle([(26, 26), (W-27, H-27)], outline=COLOR_BORDER, width=1)

        # Top Bar: PPRI emblem + Institute title
        card.paste(emb, (50, 46), emb)
        draw.text((148, 56), "PAKISTAN PROVINCIAL REFORM INSTITUTE", font=f_header, fill=COLOR_WHITE)
        draw.text((148, 92), "RESEARCH & POLICY OBSERVATORY · PPRI.ORG.PK", font=f_sub_header, fill=COLOR_GOLD)
        draw.line([(50, 145), (W-50, 145)], fill=COLOR_GOLD, width=2)

        # Badge
        badge_box = draw.textbbox((0, 0), pub["badge"], font=f_badge)
        badge_w = badge_box[2] - badge_box[0] + 28
        draw.rectangle([(50, 175), (50 + badge_w, 210)], fill=COLOR_GOLD)
        draw.text((64, 182), pub["badge"], font=f_badge, fill=COLOR_DARK_TEAL)

        # Title
        draw.text((50, 235), pub["title"], font=f_title, fill=COLOR_WHITE, spacing=10)

        # Description
        draw.text((50, 385), pub["desc"], font=f_desc, fill=COLOR_MUTED, spacing=8)

        # Bottom Bar
        draw.line([(50, 520), (W-50, 520)], fill=(20, 80, 75), width=1)
        draw.text((50, 545), pub["meta"], font=f_meta, fill=COLOR_GOLD)
        draw.text((W-340, 545), "https://ppripakistan.github.io", font=f_url, fill=COLOR_MUTED_URL)

        target = RESEARCH_DIR / pub["filename"]
        card.save(target, format="JPEG", quality=94, optimize=True)
        print(f"  Generated {pub['filename']} ({W}x{H})")

def main():
    print("=" * 60)
    print("Building Master PPRI Brand & Social Asset Suite")
    print("=" * 60)
    emblem = extract_master_emblem()
    build_favicons(emblem)
    build_default_social_cards(emblem)
    build_research_publication_cards(emblem)
    print("=" * 60)
    print("Asset generation complete!")

if __name__ == "__main__":
    main()
