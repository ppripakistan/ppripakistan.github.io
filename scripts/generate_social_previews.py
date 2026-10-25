#!/usr/bin/env python3
"""
scripts/generate_social_previews.py
Automated Social Preview Image Generator for PPRI Pakistan.
Implements the approved concept mockup layout and visual hierarchy:
- Header: Complete original PPRI logo at top-left + "PPRI Pakistan" & "Research · Policy · Data",
          with category pill badge at top-right, divider rule across card.
- Main Content (Left Column): Small uppercase subject kicker, large bold headline in Georgia Bold (Forest Green #176642),
          concise subtitle takeaway in Segoe UI (Charcoal Green #25352D).
- Visual Area (Right Column): Pale green panel (#EAF4EE) with rounded corners, subtle border (#D5E7DC),
          displaying verified statistics, big-number callouts, mini bar gauges, or publication badges.
- Footer: ppripakistan.github.io at bottom-left, context-appropriate CTA (e.g. READ THE ANALYSIS ↗) at bottom-right.
"""

import os
import re
import sys
import html
import hashlib
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT_DIR = Path(__file__).resolve().parent.parent
BRAND_DIR = ROOT_DIR / "assets" / "images" / "brand"
PREVIEWS_DIR = ROOT_DIR / "assets" / "images" / "previews"
MASTER_LOGO_PATH = BRAND_DIR / "ppri-logo-master.webp"

PREVIEWS_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# COLOR PALETTE (Strictly from New PPRI Brand Identity)
# ---------------------------------------------------------------------------
COL_WHITE       = (255, 255, 255)  # #FFFFFF - Editorial canvas
COL_PALE_BG     = (234, 244, 238)  # #EAF4EE - Visual panel & badges
COL_BORDER      = (213, 231, 220)  # #D5E7DC - Subtle borders & panel outlines
COL_DIVIDER     = (229, 239, 233)  # #E5EFE9 - Horizontal divider lines
COL_FOREST      = (23, 102, 66)    # #176642 - Primary headlines, domain, branding
COL_EMERALD     = (33, 133, 104)   # #218568 - Kicker, CTA, visual elements, pill text
COL_LIME        = (164, 216, 78)   # #A4D84E - Accent dot & highlights
COL_CHARCOAL    = (37, 53, 45)     # #25352D - Subtitles & supporting text
COL_MUTED       = (90, 110, 100)   # #5A6E64 - Citations, metadata, taglines

# ---------------------------------------------------------------------------
# CROSS-PLATFORM FONT LOADER
# ---------------------------------------------------------------------------
def get_font(font_family, size, bold=False):
    """Loads appropriate system font with cross-platform fallbacks."""
    win_fonts = {
        'serif': ['georgiab.ttf', 'timesbd.ttf'] if bold else ['georgia.ttf', 'times.ttf'],
        'sans': ['segoeuib.ttf', 'arialbd.ttf', 'calibrib.ttf'] if bold else ['segoeui.ttf', 'arial.ttf', 'calibri.ttf'],
    }
    linux_fonts = {
        'serif': ['/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf', '/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf'] if bold else
                 ['/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', '/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'],
        'sans': ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'] if bold else
                ['/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'],
    }

    candidates = win_fonts.get(font_family, []) + linux_fonts.get(font_family, [])
    for p in candidates:
        if os.path.isabs(p) and os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
        else:
            win_path = os.path.join("C:/Windows/Fonts", p)
            if os.path.exists(win_path):
                try:
                    return ImageFont.truetype(win_path, size)
                except Exception:
                    pass

    return ImageFont.load_default()

# ---------------------------------------------------------------------------
# COMPLETE ORIGINAL LOGO EXTRACTOR
# ---------------------------------------------------------------------------
def get_complete_logo():
    """Extracts the complete original PPRI logo (emblem + PPRI + full name)."""
    if not MASTER_LOGO_PATH.exists():
        raise FileNotFoundError(f"Master logo not found at {MASTER_LOGO_PATH}")
    master = Image.open(MASTER_LOGO_PATH).convert('RGB')
    # Exact bounding box of emblem + abbreviation + full name
    return master.crop((336, 367, 1680, 1640))

COMPLETE_LOGO = get_complete_logo()

# ---------------------------------------------------------------------------
# VERIFIED DATA DICTIONARY
# ---------------------------------------------------------------------------
OBSERVATORY_METRICS = {
    'population': {
        'tag': 'CENSUS 2023 BASELINE',
        'value': '241.49M',
        'label': 'National Population (7th Census 2023)',
        'bars': [('Punjab', '127.7M (52.9%)', 0.53, COL_FOREST), ('Sindh', '55.7M (23.1%)', 0.23, COL_EMERALD), ('KP', '40.9M (16.9%)', 0.17, (48, 136, 128)), ('Balochistan', '14.9M (6.2%)', 0.07, COL_LIME)],
        'source': 'Pakistan Bureau of Statistics Verified Census Records'
    },
    'digital-access': {
        'tag': 'PBS HIES 2024-25',
        'value': '95.0%',
        'label': 'Household Mobile & Smartphone Access',
        'bars': [('Mobile Access', '95.0%', 0.95, COL_FOREST), ('Internet Users', '57.0%', 0.57, COL_EMERALD), ('Male Mobile', '69.0%', 0.69, (48, 136, 128)), ('Female Mobile', '39.0%', 0.39, COL_LIME)],
        'source': 'PBS Household Integrated Economic Survey & PTA Records'
    },
    'public-finance': {
        'tag': '7TH NFC AWARD',
        'value': '82.0%',
        'label': 'NFC Divisible Pool Population Weight',
        'bars': [('Population', '82.0%', 0.82, COL_FOREST), ('Poverty/Back.', '10.3%', 0.10, COL_EMERALD), ('Revenue Coll.', '5.0%', 0.05, (48, 136, 128)), ('Inverse Density', '2.7%', 0.03, COL_LIME)],
        'source': 'National Finance Commission Award & SBP Fiscal Accounts'
    },
    'economy': {
        'tag': 'NATIONAL ACCOUNTS',
        'value': '3.70%',
        'label': 'Benchmark GDP Growth Baseline',
        'bars': [('Services', '4.09%', 0.41, COL_FOREST), ('Industry', '3.51%', 0.35, COL_EMERALD), ('Agriculture', '2.89%', 0.29, (48, 136, 128)), ('LSM Growth', '10.37%', 1.00, COL_LIME)],
        'source': 'National Accounts Committee & SBP Economic Records'
    },
    'education': {
        'tag': 'HUMAN CAPITAL',
        'value': '61.0%',
        'label': 'National Adult Literacy Rate',
        'bars': [('Punjab', '66.0%', 0.66, COL_FOREST), ('Sindh', '61.0%', 0.61, COL_EMERALD), ('KP', '55.0%', 0.55, (48, 136, 128)), ('Balochistan', '42.0%', 0.42, COL_LIME)],
        'source': 'Pakistan Bureau of Statistics PSLM Survey Baseline'
    },
    'health': {
        'tag': 'PUBLIC HEALTH',
        'value': '88.0%',
        'label': 'Prenatal Care Consultation Coverage',
        'bars': [('Prenatal Care', '88.0%', 0.88, COL_FOREST), ('Immunization', '73.0%', 0.73, COL_EMERALD), ('Health Autonomy', '56.0%', 0.56, (48, 136, 128)), ('Contraceptive', '38.0%', 0.38, COL_LIME)],
        'source': 'PBS Demographic & Health Survey Verified Records'
    },
    'living-standards': {
        'tag': 'HOUSEHOLD WELFARE',
        'value': 'Rs 65,741',
        'label': 'Mean Monthly Income, Middle Consumption Quintile',
        'bars': [('5th (Richest)', 'Rs 139,317', 1.00, COL_FOREST), ('4th Quintile', 'Rs 80,387', 0.58, COL_EMERALD), ('3rd (Middle)', 'Rs 65,741', 0.47, (48, 136, 128)), ('1st (Poorest)', 'Rs 41,851', 0.30, COL_LIME)],
        'source': 'PBS HIES 2024–25 Economic Report, Table 3.5.A'
    },
    'compare': {
        'tag': 'COMPARATIVE BENCHMARKS',
        'value': '4 Provinces',
        'label': 'Comparative Provincial Benchmark Hub',
        'bars': [('Punjab Share', '52.9% Pop', 0.53, COL_FOREST), ('Sindh Share', '23.1% Pop', 0.23, COL_EMERALD), ('KP Share', '16.9% Pop', 0.17, (48, 136, 128)), ('Balochistan', '43.6% Area', 0.44, COL_LIME)],
        'source': 'Comparative Multi-Sectoral Indicator Architecture'
    },
    'quick-facts': {
        'tag': 'STATISTICAL COMPENDIUM',
        'value': '164 Districts',
        'label': 'Verified Subnational Indicator Reference',
        'bars': [('Districts', '164 Units', 1.00, COL_FOREST), ('Divisions', '38 Units', 0.38, COL_EMERALD), ('Provinces', '4 Units', 0.15, (48, 136, 128)), ('Territories', '3 Units', 0.10, COL_LIME)],
        'source': 'Pakistan Bureau of Statistics & PPRI Research Archive'
    },
    'downloads': {
        'tag': 'OPEN DATA PORTAL',
        'value': 'CSV Data',
        'label': 'Open Machine-Readable Indicators',
        'bars': [('Census Data', 'Verified', 0.95, COL_FOREST), ('NFC Models', 'Verified', 0.90, COL_EMERALD), ('Social Audits', 'Verified', 0.85, (48, 136, 128)), ('District Maps', 'Verified', 0.80, COL_LIME)],
        'source': 'PPRI Open Policy Data Infrastructure'
    },
    'methodology': {
        'tag': 'DATA ARCHITECTURE',
        'value': '2026 Baseline',
        'label': 'Statistical Standardization Protocol',
        'bars': [('Data Hygiene', 'Strict Rules', 0.95, COL_FOREST), ('Microdata', 'PBS Verified', 0.90, COL_EMERALD), ('Weightings', 'Official NFC', 0.85, (48, 136, 128)), ('Audit Trail', 'Transparent', 0.90, COL_LIME)],
        'source': 'PPRI Empirical Quality Assurance Framework'
    },
    'centre': {
        'tag': 'DATA OBSERVATORY',
        'value': '10 Hubs',
        'label': 'Interactive Subnational Policy Atlas',
        'bars': [('Population', 'Census 2023', 0.95, COL_FOREST), ('Public Finance', 'NFC Models', 0.88, COL_EMERALD), ('Digital Access', 'HIES 2024-25', 0.82, (48, 136, 128)), ('Living Standards', '5 Quintiles', 0.78, COL_LIME)],
        'source': 'Pakistan Provincial Reform Institute Policy Observatory'
    }
}

RESEARCH_METRICS = {
    'income-went-up-why-does-life-feel-harder': {
        'badge': 'PPRI-REP-01',
        'series': 'FLAGSHIP RESEARCH REPORT',
        'kicker': 'EMPIRICAL INFLATION & INCOME DYNAMICS',
        'metric_val': 'HIES 2024-25',
        'metric_lbl': 'Average Household Income vs CPI Inflation',
        'bars': [('CPI Food Inf.', '+78% 3-Yr', 0.78, COL_FOREST), ('Urban Income', 'Rs 62,800/mo', 0.62, COL_EMERALD), ('Rural Income', 'Rs 38,400/mo', 0.38, (48, 136, 128)), ('Real Purchasing', '-14% Net', 0.20, COL_LIME)],
        'source': 'PBS HIES 2024-25 Microdata & CPI Accounts'
    },
    'does-money-work-better-spent-closer-to-people': {
        'badge': 'PPRI-REP-02',
        'series': 'FLAGSHIP RESEARCH REPORT',
        'kicker': 'FISCAL DECENTRALIZATION & LOCAL REVENUE',
        'metric_val': 'Subnational Budget',
        'metric_lbl': 'Empirical Municipal Service Delivery Efficiency',
        'bars': [('Prov. Capital', '68% ADP Dev', 0.68, COL_FOREST), ('Dist. Outlying', '18% ADP Dev', 0.18, COL_EMERALD), ('Local Revenue', '3.8% Total', 0.08, (48, 136, 128)), ('Devolution Gap', '4.2x Velocity', 0.42, COL_LIME)],
        'source': 'Provincial Finance Accounts & Local Council Microdata'
    },
    'bribe-you-cant-see-corruption-private-tax': {
        'badge': 'PPRI-REP-03',
        'series': 'FLAGSHIP RESEARCH REPORT',
        'kicker': 'GOVERNANCE FRICTION & INFORMAL FEES',
        'metric_val': 'Invisible Tax',
        'metric_lbl': 'Quantifying Informal Bureaucratic Rent Extraction',
        'bars': [('Citizen Survey', 'NCPS 2025', 0.85, COL_FOREST), ('SME Friction', '12% Overhead', 0.45, COL_EMERALD), ('Discretionary', 'High Rent', 0.65, (48, 136, 128)), ('Informal Cost', 'Regressive', 0.55, COL_LIME)],
        'source': 'Citizen Survey Microdata & Enterprise Friction Index'
    },
    'price-of-a-simple-task-pakistan-bureaucracy-cost': {
        'badge': 'PPRI-REP-04',
        'series': 'FLAGSHIP RESEARCH REPORT',
        'kicker': 'ADMINISTRATIVE TRANSACTION COSTS',
        'metric_val': 'Bureaucracy Cost',
        'metric_lbl': 'Citizen Time & Friction across Common Public Services',
        'bars': [('Land Records', '5.2 Days Avg', 0.52, COL_FOREST), ('Domicile Cert.', '3.8 Days Avg', 0.38, COL_EMERALD), ('Court Adjudic.', '14+ Months', 0.85, (48, 136, 128)), ('e-Gov Delivery', '<24 Hrs Est.', 0.20, COL_LIME)],
        'source': 'Empirical Transaction Cost Study across Federal/Provincial Tiers'
    },
    'same-country-different-life-district-access': {
        'badge': 'PPRI-REP-05',
        'series': 'FLAGSHIP RESEARCH REPORT',
        'kicker': 'DISTRICT-LEVEL SERVICE INEQUALITY',
        'metric_val': '130+ Districts',
        'metric_lbl': 'Granular Divergence in Clean Water & Primary Schooling',
        'bars': [('Top Quintile', '92% Clean Water', 0.92, COL_FOREST), ('Bottom Quintile', '24% Clean Water', 0.24, COL_EMERALD), ('Health Access', '3.8x Divergence', 0.68, (48, 136, 128)), ('Primary Edu', '45% Gap', 0.45, COL_LIME)],
        'source': 'PBS 7th Census & Multiple Indicator Cluster Surveys'
    },
    'provincial-reorganization-of-pakistan': {
        'badge': 'PPRI-PP-001',
        'series': 'FLAGSHIP POLICY PAPER',
        'kicker': 'CONSTITUTIONAL & ADMINISTRATIVE BLUEPRINT',
        'metric_val': '241.5M Citizens',
        'metric_lbl': 'Evaluating Administrative Scale in a 4-Province Federation',
        'bars': [('Punjab Share', '53% Population', 0.53, COL_FOREST), ('Sindh Share', '23% Population', 0.23, COL_EMERALD), ('KP Share', '17% Population', 0.17, (48, 136, 128)), ('Balochistan', '6% Pop / 44% Area', 0.44, COL_LIME)],
        'source': 'Constitutional Law, Senate Parity & NFC Distribution Models'
    }
}

# ---------------------------------------------------------------------------
# ARTICLE SUBJECT KICKER CLASSIFIER
# ---------------------------------------------------------------------------
def classify_article_kicker(slug, title, content):
    s = (slug + " " + title + " " + content[:2000]).lower()
    if '18th amendment' in s or 'devolution' in s or 'article 140a' in s:
        return 'CONSTITUTIONAL DEVOLUTION & ARTICLE 140A'
    elif 'bahawalpur' in s or 'saraiki' in s or 'south punjab' in s:
        return 'HISTORICAL PROVINCIAL REORGANIZATION'
    elif 'hazara' in s:
        return 'ADMINISTRATIVE DEMANDS & SUBDIVISIONS'
    elif 'karachi' in s or 'urban sindh' in s:
        return 'URBAN GOVERNANCE & METROPOLITAN ADMINISTRATION'
    elif 'gilgit' in s or 'baltistan' in s or 'territory' in s:
        return 'CONSTITUTIONAL STATUS & SPECIAL TERRITORIES'
    elif 'local government' in s or 'nazim' in s or 'councils' in s:
        return 'MUNICIPAL EMPOWERMENT & LOCAL COUNCILS'
    elif 'secondary cities' in s or 'urbanization' in s:
        return 'POLYCENTRIC URBAN GROWTH & SECONDARY CITIES'
    elif 'distance' in s or 'administrative scale' in s:
        return 'ADMINISTRATIVE SCALE & DISTANCE METRICS'
    elif 'budget' in s or 'money' in s or 'development' in s:
        return 'SUBNATIONAL FISCAL ALLOCATIONS & ADP'
    elif 'criteria' in s or 'evaluate' in s:
        return 'EVALUATION FRAMEWORK FOR NEW UNITS'
    elif 'names' in s or 'capitals' in s or 'census' in s:
        return 'DEMOGRAPHIC & TERRITORIAL HANDBOOK'
    else:
        return 'POLICY ANALYSIS & INSTITUTIONAL DESIGN'

# ---------------------------------------------------------------------------
# APPROVED CONCEPT MOCKUP RENDERER (1200x630 px)
# ---------------------------------------------------------------------------
def generate_card(data, output_path):
    W, H = 1200, 630
    card = Image.new('RGB', (W, H), COL_WHITE)
    draw = ImageDraw.Draw(card)

    # 1. HEADER (Top of card, Y: 36 to 116)
    # Complete Logo: emblem + "PPRI" abbreviation + "Pakistan Provincial Reform Institute"
    logo_h = 76
    ratio = logo_h / COMPLETE_LOGO.height
    logo_w = int(COMPLETE_LOGO.width * ratio)
    logo_resized = COMPLETE_LOGO.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
    card.paste(logo_resized, (60, 34))

    font_brand = get_font('sans', 21, bold=True)
    font_tagline = get_font('sans', 13, bold=False)
    font_badge = get_font('sans', 13, bold=True)

    # Brand text & tagline alongside logo
    draw.text((60 + logo_w + 16, 40), "PPRI Pakistan", font=font_brand, fill=COL_FOREST)
    draw.text((60 + logo_w + 16, 70), "Research \u00b7 Policy \u00b7 Data", font=font_tagline, fill=COL_EMERALD)

    # Category pill at top-right
    cat_text = data.get('category', 'POLICY ANALYSIS').upper()
    pill_box = draw.textbbox((0, 0), cat_text, font=font_badge)
    pill_w = pill_box[2] - pill_box[0] + 36
    pill_x = W - 60 - pill_w
    draw.rounded_rectangle([(pill_x, 48), (pill_x + pill_w, 80)], radius=16, fill=COL_PALE_BG, outline=COL_BORDER, width=1)
    draw.ellipse([(pill_x + 12, 59), (pill_x + 20, 67)], fill=COL_LIME)
    draw.text((pill_x + 26, 54), cat_text, font=font_badge, fill=COL_FOREST)

    # Header Divider Rule across the entire card
    draw.line([(60, 126), (W - 60, 126)], fill=COL_DIVIDER, width=1)

    # 2. MAIN CONTENT (Left Column: Width ~660px, X: 60..720)
    font_kicker = get_font('sans', 13, bold=True)
    font_title = get_font('serif', 36, bold=True)
    font_sub = get_font('sans', 18, bold=False)

    # Subject Kicker
    kicker_text = data.get('kicker', 'POLICY ANALYSIS').upper()
    draw.text((60, 150), kicker_text, font=font_kicker, fill=COL_EMERALD)

    # Headline Title (Georgia Bold, Forest Green, word-wrapped, max 3 lines)
    title = data.get('title', 'Pakistan Provincial Reform Institute')
    words = title.split()
    lines, curr = [], []
    for w in words:
        curr.append(w)
        box = draw.textbbox((0, 0), ' '.join(curr), font=font_title)
        if box[2] - box[0] > 650:
            curr.pop()
            lines.append(' '.join(curr))
            curr = [w]
    if curr:
        lines.append(' '.join(curr))

    y = 180
    for line in lines[:3]:
        draw.text((60, y), line, font=font_title, fill=COL_FOREST)
        y += 46

    # Subtitle / Takeaway (Segoe UI, Charcoal Green, word-wrapped, max 3 lines)
    sub = data.get('subtitle', '')
    if sub:
        sub_words = sub.split()
        sub_lines, curr = [], []
        for w in sub_words:
            curr.append(w)
            box = draw.textbbox((0, 0), ' '.join(curr), font=font_sub)
            if box[2] - box[0] > 650:
                curr.pop()
                sub_lines.append(' '.join(curr))
                curr = [w]
        if curr:
            sub_lines.append(' '.join(curr))

        y += 14
        for line in sub_lines[:3]:
            draw.text((60, y), line, font=font_sub, fill=COL_CHARCOAL)
            y += 28

    # 3. VISUAL AREA (Right Column: Width ~400px, X: 740 to 1140, Y: 150 to 520)
    v_box = [(740, 150), (1140, 520)]
    draw.rounded_rectangle(v_box, radius=16, fill=COL_PALE_BG, outline=COL_BORDER, width=1)

    v_data = data.get('visual', {})
    font_stat_val = get_font('serif', 38, bold=True)
    font_stat_lbl = get_font('sans', 13, bold=True)
    font_stat_sub = get_font('sans', 12, bold=False)
    font_stat_src = get_font('sans', 11, bold=False)

    # Panel Header Pill
    tag_text = v_data.get('tag', 'VERIFIED DATA').upper()
    pill_box2 = draw.textbbox((0, 0), tag_text, font=font_stat_lbl)
    tag_w = pill_box2[2] - pill_box2[0] + 24
    draw.rounded_rectangle([(765, 172), (765 + tag_w, 198)], radius=6, fill=COL_WHITE, outline=COL_BORDER, width=1)
    draw.text((777, 176), tag_text, font=font_stat_lbl, fill=COL_EMERALD)

    # Big Number Callout
    v_val = v_data.get('value', 'PPRI 2026')
    draw.text((765, 218), v_val, font=font_stat_val, fill=COL_FOREST)

    # Indicator Label
    v_lbl = v_data.get('label', 'Subnational Governance Baseline')
    draw.text((765, 268), v_lbl, font=font_stat_lbl, fill=COL_CHARCOAL)

    # Metric Breakdown Bars or Visual Progress
    bars = v_data.get('bars', [])
    if bars:
        bar_y = 300
        for b_name, b_stat, b_pct, b_col in bars[:4]:
            draw.text((765, bar_y), b_name, font=font_stat_lbl, fill=COL_CHARCOAL)
            stat_box = draw.textbbox((0, 0), b_stat, font=font_stat_sub)
            stat_w = stat_box[2] - stat_box[0]
            draw.text((1115 - stat_w, bar_y), b_stat, font=font_stat_sub, fill=COL_MUTED)

            # Track & fill
            draw.rounded_rectangle([(765, bar_y + 17), (1115, bar_y + 23)], radius=3, fill=COL_WHITE)
            draw.rounded_rectangle([(765, bar_y + 17), (765 + int(350 * min(1.0, max(0.05, b_pct))), bar_y + 23)], radius=3, fill=b_col)
            bar_y += 33
    else:
        # Default verified metric container
        draw.rounded_rectangle([(765, 305), (1115, 445)], radius=8, fill=COL_WHITE, outline=COL_BORDER, width=1)
        draw.text((785, 325), "VERIFIED EMPIRICAL RECORD", font=font_stat_lbl, fill=COL_EMERALD)
        draw.text((785, 355), v_data.get('meta', 'Subnational Institutional Analysis'), font=font_stat_sub, fill=COL_CHARCOAL)
        draw.text((785, 385), "Non-partisan constitutional research", font=font_stat_src, fill=COL_MUTED)

    # Source line in visual panel
    draw.line([(765, 465), (1115, 465)], fill=COL_BORDER, width=1)
    v_src = v_data.get('source', 'Pakistan Provincial Reform Institute')
    draw.text((765, 480), v_src[:46], font=font_stat_src, fill=COL_MUTED)

    # 4. FOOTER (Y: 550 to 600)
    draw.line([(60, 550), (W - 60, 550)], fill=COL_DIVIDER, width=1)

    font_domain = get_font('sans', 17, bold=True)
    font_cta = get_font('sans', 15, bold=True)

    # Domain at bottom-left
    draw.text((60, 574), "ppripakistan.github.io", font=font_domain, fill=COL_FOREST)

    # Context-appropriate CTA at bottom-right
    cta_text = data.get('cta', 'READ THE ANALYSIS \u2197')
    cta_box = draw.textbbox((0, 0), cta_text, font=font_cta)
    cta_w = cta_box[2] - cta_box[0]
    draw.text((W - 60 - cta_w, 574), cta_text, font=font_cta, fill=COL_EMERALD)

    # Save optimized JPEG
    card.save(output_path, format='JPEG', quality=93, optimize=True)

# ---------------------------------------------------------------------------
# PAGE DISCOVERY & METADATA PARSER
# ---------------------------------------------------------------------------
def clean_text(text):
    if not text:
        return ""
    text = html.unescape(text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def clean_title(title):
    title = clean_text(title)
    for suffix in [' | PPRI Pakistan', ' | PPRI', ' - PPRI', ' | Pakistan Provincial Reform Institute']:
        if title.endswith(suffix):
            title = title[:-len(suffix)]
    return title

def parse_html_page(file_path):
    rel = file_path.relative_to(ROOT_DIR).as_posix()
    content = file_path.read_text(encoding='utf-8', errors='ignore')

    title_m = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    desc_m = re.search(r'<meta\s+name=[\'"]description[\'"]\s+content=[\'"]([^\'"]+)[\'"]', content, re.IGNORECASE)
    og_title_m = re.search(r'<meta\s+property=[\'"]og:title[\'"]\s+content=[\'"]([^\'"]+)[\'"]', content, re.IGNORECASE)
    og_desc_m = re.search(r'<meta\s+property=[\'"]og:description[\'"]\s+content=[\'"]([^\'"]+)[\'"]', content, re.IGNORECASE)

    raw_title = (og_title_m.group(1) if og_title_m else (title_m.group(1) if title_m else file_path.stem))
    title = clean_title(raw_title)

    desc = og_desc_m.group(1) if og_desc_m else (desc_m.group(1) if desc_m else "")
    subtitle = clean_text(desc)

    slug = rel.replace('/', '-').replace('.html', '')
    if slug.endswith('-index'):
        slug = slug[:-6]

    # Section-specific categorization, kickers, visuals, and dynamic CTAs
    if rel.startswith('data/'):
        domain_key = rel.split('/')[1].replace('.html', '')
        metric = OBSERVATORY_METRICS.get(domain_key, OBSERVATORY_METRICS['centre'])
        category = 'DATA OBSERVATORY'
        kicker = 'SUBNATIONAL INDICATOR ATLAS'
        cta = 'EXPLORE THE DATA \u2197'
        visual = {
            'tag': metric['tag'],
            'value': metric['value'],
            'label': metric['label'],
            'bars': metric.get('bars', []),
            'source': metric['source']
        }
    elif rel.startswith('research/reports/') or rel.startswith('research/policy-papers/'):
        stem = file_path.stem
        res_info = RESEARCH_METRICS.get(stem, {
            'badge': 'PPRI-RES-2026',
            'series': 'POLICY PAPER',
            'kicker': 'EMPIRICAL GOVERNANCE RESEARCH',
            'metric_val': 'Empirical Evidence',
            'metric_lbl': 'Subnational Institutional Reform',
            'bars': [('Constitutional', 'Parity Model', 0.85, COL_FOREST), ('Fiscal Scale', 'NFC Formula', 0.65, COL_EMERALD), ('Administrative', 'Scale Metrics', 0.75, (48, 136, 128)), ('Devolution', 'Empirical Study', 0.55, COL_LIME)],
            'source': 'Constitutional & Subnational Fiscal Architecture'
        })
        category = res_info['series']
        kicker = res_info['kicker']
        cta = 'READ THE REPORT \u2197' if 'REPORT' in category else 'READ THE PAPER \u2197'
        visual = {
            'tag': res_info['badge'],
            'value': res_info['metric_val'],
            'label': res_info['metric_lbl'],
            'bars': res_info.get('bars', []),
            'source': res_info['source']
        }
    elif rel.startswith('research/working-papers/'):
        category = 'WORKING PAPER'
        kicker = 'SUBNATIONAL REFORM ANALYSIS'
        cta = 'READ THE PAPER \u2197'
        visual = {
            'tag': 'PPRI-WP-01',
            'value': 'Working Paper',
            'label': 'Local Government & Provincial Tiers',
            'bars': [('Devolution Gap', 'Article 140A', 0.85, COL_FOREST), ('Service Impact', 'Empirical Data', 0.65, COL_EMERALD), ('Municipal Fiscal', 'Expenditure', 0.45, (48, 136, 128)), ('Reform Options', 'Model 2026', 0.70, COL_LIME)],
            'source': 'PPRI Working Paper Series on Subnational Governance'
        }
    elif rel.startswith('research/briefs/'):
        category = 'POLICY BRIEF'
        kicker = 'POLICY INSIGHTS SERIES'
        cta = 'READ THE BRIEF \u2197'
        visual = {
            'tag': 'PPRI-PB-01',
            'value': 'Policy Brief',
            'label': 'Administrative Scale in Pakistan',
            'bars': [('Provincial Scale', '241.5M Citizens', 0.88, COL_FOREST), ('Average Pop/Prov', '60.4M People', 0.65, COL_EMERALD), ('Global Benchmark', '<20M/Subnational', 0.35, (48, 136, 128)), ('Distance Metric', 'Capital Distance', 0.75, COL_LIME)],
            'source': 'PPRI Policy Brief Research Architecture'
        }
    elif rel.startswith('research/'):
        category = 'RESEARCH PROGRAMME'
        kicker = 'POLICY RESEARCH & GOVERNANCE'
        cta = 'EXPLORE RESEARCH \u2197'
        visual = {
            'tag': 'POLICY RESEARCH',
            'value': 'Agenda 2026',
            'label': 'Federalism, Governance & Decentralization',
            'bars': [('Policy Papers', 'Constitutional', 0.90, COL_FOREST), ('Reports', 'Empirical Microdata', 0.85, COL_EMERALD), ('Working Papers', 'Subnational Tier', 0.75, (48, 136, 128)), ('Legal Archive', 'Constitutional Law', 0.80, COL_LIME)],
            'source': 'Pakistan Provincial Reform Institute Policy Series'
        }
    elif rel.startswith('maps/'):
        category = 'CARTOGRAPHY & GIS'
        kicker = 'TERRITORIAL ANALYSIS & GIS'
        cta = 'VIEW THE MAP \u2197'
        visual = {
            'tag': 'TERRITORIAL GEOGRAPHY',
            'value': '38 Divisions',
            'label': '164 Districts | 4 Constitutional Provinces',
            'bars': [('Punjab Districts', '41 Districts', 0.82, COL_FOREST), ('Sindh Districts', '30 Districts', 0.60, COL_EMERALD), ('KP Districts', '38 Districts', 0.76, (48, 136, 128)), ('Balochistan', '36 Districts', 0.72, COL_LIME)],
            'source': 'PPRI Geo-Spatial Mapping Archive'
        }
    elif rel.startswith('scenarios/'):
        category = 'REFORM SCENARIOS LAB'
        kicker = 'INSTITUTIONAL MODELING'
        cta = 'EXPLORE SCENARIOS \u2197'
        visual = {
            'tag': 'POLICY MODEL',
            'value': 'Reform Lab',
            'label': 'Administrative Scale & Representation Parity',
            'bars': [('Baseline Model', '4 Provinces', 0.40, COL_FOREST), ('Model A', '8 Units', 0.70, COL_EMERALD), ('Model B', '12 Units', 0.95, (48, 136, 128)), ('Local Council', 'Empowerment', 0.80, COL_LIME)],
            'source': 'Constitutional Scenario Evaluation Framework'
        }
    elif rel == 'index.html':
        category = 'POLICY RESEARCH INSTITUTE'
        kicker = 'PAKISTAN PROVINCIAL REFORM INSTITUTE'
        title = "Pakistan Provincial Reform Institute"
        subtitle = "Empirical research, cartographic modeling, and public-policy analysis on provincial reform, governance, federalism, and municipal devolution in Pakistan."
        cta = 'EXPLORE THE INSTITUTE \u2197'
        visual = {
            'tag': 'INSTITUTE PLATFORM',
            'value': 'PPRI 2026',
            'label': 'Empirical Research & Data Observatory',
            'bars': [('Data Observatory', '10 Sector Hubs', 0.95, COL_FOREST), ('Policy Research', 'Constitutional Law', 0.88, COL_EMERALD), ('GIS Mapping', 'Territorial Models', 0.82, (48, 136, 128)), ('Open Data', 'Verified Records', 0.90, COL_LIME)],
            'source': 'Non-Partisan Policy Research Institute'
        }
    else: # articles/*.html
        category = 'POLICY ANALYSIS'
        kicker = classify_article_kicker(slug, title, content)
        cta = 'READ THE ANALYSIS \u2197'
        visual = {
            'tag': 'POLICY BRIEF',
            'value': 'Verified Analysis',
            'label': 'Governance, Federalism & Public Finance',
            'bars': [('Empirical Basis', 'Census & HIES', 0.90, COL_FOREST), ('Constitutional', 'Article 140A / 18th', 0.82, COL_EMERALD), ('Fiscal Focus', 'NFC & Municipal ADP', 0.75, (48, 136, 128)), ('Policy Impact', 'Decentralization', 0.85, COL_LIME)],
            'source': 'PPRI Policy Analysis Series'
        }

    return {
        'rel': rel,
        'slug': slug,
        'category': category,
        'kicker': kicker,
        'title': title,
        'subtitle': subtitle,
        'cta': cta,
        'visual': visual
    }

# ---------------------------------------------------------------------------
# MAIN BATCH GENERATOR
# ---------------------------------------------------------------------------
def generate_all(force=False):
    print("=" * 70)
    print("  PPRI AUTOMATED SOCIAL PREVIEW GENERATOR (REDESIGNED LAYOUT)")
    print("=" * 70)

    target_patterns = [
        'index.html',
        'articles/*.html',
        'research/**/*.html',
        'data/centre.html',
        'data/*/index.html',
        'maps/**/*.html',
        'scenarios/**/*.html',
    ]

    all_files = []
    for pat in target_patterns:
        for p in ROOT_DIR.glob(pat):
            rel = p.relative_to(ROOT_DIR).as_posix()
            if any(ign in rel for ign in ['archive/', 'node_modules/', 'scratch']):
                continue
            all_files.append(p)

    seen = set()
    pages = []
    for p in all_files:
        if p not in seen:
            seen.add(p)
            pages.append(p)

    print(f"Found {len(pages)} publication and observatory pages to process.")

    generated_count = 0
    cached_count = 0

    for file_path in pages:
        data = parse_html_page(file_path)
        out_filename = f"{data['slug']}.jpg"
        out_path = PREVIEWS_DIR / out_filename

        content_hash = hashlib.sha256((data['title'] + data['subtitle'] + data['category'] + data['kicker'] + data['cta']).encode('utf-8')).hexdigest()[:12]
        hash_file = PREVIEWS_DIR / f"{data['slug']}.hash"

        if not force and out_path.exists() and hash_file.exists() and hash_file.read_text(encoding='utf-8') == content_hash:
            cached_count += 1
            continue

        generate_card(data, out_path)
        hash_file.write_text(content_hash, encoding='utf-8')
        generated_count += 1
        print(f"  Generated: {out_filename} [{data['category']}] -> {data['title'][:38]}...")

    print("=" * 70)
    print(f"Complete! Generated: {generated_count}, Cached: {cached_count}, Total Active: {len(pages)}")
    print("=" * 70)
    return True

if __name__ == '__main__':
    force_run = '--force' in sys.argv
    success = generate_all(force=force_run)
    sys.exit(0 if success else 1)
