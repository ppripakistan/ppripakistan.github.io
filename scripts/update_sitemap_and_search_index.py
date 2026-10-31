#!/usr/bin/env python3
"""
scripts/update_sitemap_and_search_index.py
Synchronizes canonical Data Observatory hubs, Urdu portal pages, and core site assets
into sitemap.xml, search-index.json, and search-index-ur.json.
Strictly compliant with Google Search Central XML Sitemap guidelines:
- UTF-8 XML declaration and xhtml namespace
- Content-aware lastmod extraction
- Bidirectional hreflang alternates for English and Urdu counterparts
- Canonical trailing slash normalization for directory pages
- Elimination of ignored changefreq and priority tags
"""

import os
import json
import subprocess
import xml.etree.ElementTree as ET
import xml.dom.minidom
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
SITEMAP_PATH = ROOT_DIR / "sitemap.xml"
SEARCH_INDEX_PATH = ROOT_DIR / "search-index.json"
SEARCH_INDEX_UR_PATH = ROOT_DIR / "search-index-ur.json"

TODAY_STR = datetime.now().strftime("%Y-%m-%d")

CANONICAL_OBSERVATORY_HUBS = [
    "https://ppripakistan.github.io/data/centre.html",
    "https://ppripakistan.github.io/data/population/",
    "https://ppripakistan.github.io/data/economy/",
    "https://ppripakistan.github.io/data/living-standards/",
    "https://ppripakistan.github.io/data/public-finance/",
    "https://ppripakistan.github.io/data/education/",
    "https://ppripakistan.github.io/data/health/",
    "https://ppripakistan.github.io/data/digital-access/",
    "https://ppripakistan.github.io/data/compare/",
    "https://ppripakistan.github.io/knowledge-library/",
    "https://ppripakistan.github.io/data/downloads/",
    "https://ppripakistan.github.io/data/methodology/",
]

CANONICAL_URDU_PAGES = [
    "https://ppripakistan.github.io/ur/",
    "https://ppripakistan.github.io/ur/about.html",
    "https://ppripakistan.github.io/ur/consultation/",
    "https://ppripakistan.github.io/ur/consultation/survey.html",
    "https://ppripakistan.github.io/ur/provinces/",
    "https://ppripakistan.github.io/ur/data/centre.html",
    "https://ppripakistan.github.io/ur/research/",
    "https://ppripakistan.github.io/ur/research/reports/",
    "https://ppripakistan.github.io/ur/research/reports/income-went-up-why-does-life-feel-harder.html",
    "https://ppripakistan.github.io/ur/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html",
    "https://ppripakistan.github.io/ur/research/reports/same-country-different-life-district-access.html",
    "https://ppripakistan.github.io/ur/research/reports/bribe-you-cant-see-corruption-private-tax.html",
    "https://ppripakistan.github.io/ur/research/reports/does-money-work-better-spent-closer-to-people.html",
]

HREFLANG_PAIRS = [
    ("https://ppripakistan.github.io/", "https://ppripakistan.github.io/ur/"),
    ("https://ppripakistan.github.io/about.html", "https://ppripakistan.github.io/ur/about.html"),
    ("https://ppripakistan.github.io/consultation/", "https://ppripakistan.github.io/ur/consultation/"),
    ("https://ppripakistan.github.io/provinces/", "https://ppripakistan.github.io/ur/provinces/"),
    ("https://ppripakistan.github.io/data/centre.html", "https://ppripakistan.github.io/ur/data/centre.html"),
    ("https://ppripakistan.github.io/research/", "https://ppripakistan.github.io/ur/research/"),
    ("https://ppripakistan.github.io/research/reports/", "https://ppripakistan.github.io/ur/research/reports/"),
    ("https://ppripakistan.github.io/research/reports/income-went-up-why-does-life-feel-harder.html", "https://ppripakistan.github.io/ur/research/reports/income-went-up-why-does-life-feel-harder.html"),
    ("https://ppripakistan.github.io/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html", "https://ppripakistan.github.io/ur/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html"),
    ("https://ppripakistan.github.io/research/reports/same-country-different-life-district-access.html", "https://ppripakistan.github.io/ur/research/reports/same-country-different-life-district-access.html"),
    ("https://ppripakistan.github.io/research/reports/bribe-you-cant-see-corruption-private-tax.html", "https://ppripakistan.github.io/ur/research/reports/bribe-you-cant-see-corruption-private-tax.html"),
    ("https://ppripakistan.github.io/research/reports/does-money-work-better-spent-closer-to-people.html", "https://ppripakistan.github.io/ur/research/reports/does-money-work-better-spent-closer-to-people.html"),
    ("https://ppripakistan.github.io/surveys/", "https://ppripakistan.github.io/ur/consultation/survey.html"),
]

HREFLANG_LOOKUP = {}
for en_url, ur_url in HREFLANG_PAIRS:
    alternates = [
        {"rel": "alternate", "hreflang": "en", "href": en_url},
        {"rel": "alternate", "hreflang": "ur", "href": ur_url},
        {"rel": "alternate", "hreflang": "x-default", "href": en_url},
    ]
    HREFLANG_LOOKUP[en_url] = alternates
    HREFLANG_LOOKUP[ur_url] = alternates


def get_content_lastmod_map():
    """
    Extracts organic content lastmod dates using git numstat history,
    filtering out bulk repository-wide boilerplate sweeps (e.g. style, footer, or link sweeps).
    """
    BULK_COMMITS = {"phase-20f", "phase-20e", "Phase 18", "Phase 17", "Revert \"Phase 17\""}
    cmd = ["git", "log", "--numstat", "--date=short", "--format=COMMIT|%ad|%s"]
    try:
        proc = subprocess.run(cmd, cwd=ROOT_DIR, capture_output=True, check=True)
        raw = proc.stdout.decode("utf-8", errors="replace")
    except Exception:
        return {}

    file_dates = {}
    commits = raw.split("COMMIT|")
    for block in commits:
        if not block.strip():
            continue
        lines = [l.strip() for l in block.splitlines() if l.strip()]
        if not lines:
            continue
        header = lines[0]
        parts = header.split("|", 1)
        date_str = parts[0].strip()
        msg = parts[1].strip() if len(parts) > 1 else ""

        if msg in BULK_COMMITS or any(msg.startswith(p) for p in ["phase-20e", "phase-20f"]):
            continue

        for line in lines[1:]:
            parts = line.split("\t")
            if len(parts) != 3:
                continue
            added, deleted, fname = parts
            norm_f = fname.replace("\\", "/")
            try:
                a_cnt = int(added)
                d_cnt = int(deleted)
            except ValueError:
                a_cnt, d_cnt = 0, 0

            if a_cnt + d_cnt >= 4:
                if norm_f not in file_dates:
                    file_dates[norm_f] = date_str

    return file_dates


def resolve_file_for_loc(loc):
    path_part = loc.replace("https://ppripakistan.github.io/", "").strip("/")
    if not path_part:
        return ROOT_DIR / "index.html", "index.html"
    if (ROOT_DIR / path_part / "index.html").is_file():
        return ROOT_DIR / path_part / "index.html", f"{path_part}/index.html"
    if (ROOT_DIR / f"{path_part}.html").is_file():
        return ROOT_DIR / f"{path_part}.html", f"{path_part}.html"
    p = ROOT_DIR / path_part
    return p, path_part


def clean_and_update_sitemap():
    print("Synchronizing sitemap.xml...")
    if not SITEMAP_PATH.exists():
        print("  sitemap.xml not found!")
        return

    content_lastmod_map = get_content_lastmod_map()

    content = SITEMAP_PATH.read_text(encoding="utf-8")
    root = ET.fromstring(content)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    valid_entries = []
    seen_locs = set()

    REDIRECT_STUBS = {
        "governance.html", "methodology.html", "media/events.html", "media/interviews.html",
        "news/index.html", "opinion/index.html", "resources/datasets.html", "resources/maps.html",
        "updates/index.html", "data/methodology.html", "data/economy.html", "data/population.html",
        "data/fiscal.html", "data/demographics.html", "data/governance.html", "data/data-notes.html",
        "data/index.html", "data/maps.html", "data/datasets.html", "data/provincial-comparison.html",
        "404.html", "search.html", "data/quick-facts/index.html"
    }

    urdu_locs = set(CANONICAL_URDU_PAGES)

    for url_el in root.findall('sm:url', ns):
        loc_el = url_el.find('sm:loc', ns)
        if loc_el is None or not loc_el.text:
            continue
        loc = loc_el.text.strip()
        
        # Urdu pages or observatory hubs handled by canonical lists
        if "/data/" in loc or loc in urdu_locs or loc.startswith("https://ppripakistan.github.io/ur/"):
            continue

        file_path, rel_str = resolve_file_for_loc(loc)
        path_part = loc.replace("https://ppripakistan.github.io/", "").strip("/")

        if rel_str in REDIRECT_STUBS or path_part in REDIRECT_STUBS:
            continue

        if file_path.exists() and loc not in seen_locs:
            norm_rel = rel_str.replace("\\", "/")
            lastmod = content_lastmod_map.get(norm_rel)
            if not lastmod:
                lastmod_el = url_el.find('sm:lastmod', ns)
                lastmod = lastmod_el.text if lastmod_el is not None else "2026-10-18"

            valid_entries.append((loc, lastmod))
            seen_locs.add(loc)

    # Add canonical observatory hubs
    for loc in CANONICAL_OBSERVATORY_HUBS:
        if loc not in seen_locs:
            file_path, rel_str = resolve_file_for_loc(loc)
            norm_rel = rel_str.replace("\\", "/")
            lastmod = content_lastmod_map.get(norm_rel, "2026-10-30")
            valid_entries.append((loc, lastmod))
            seen_locs.add(loc)

    # Add canonical Urdu portal pages
    for loc in CANONICAL_URDU_PAGES:
        if loc not in seen_locs:
            file_path, rel_str = resolve_file_for_loc(loc)
            norm_rel = rel_str.replace("\\", "/")
            lastmod = content_lastmod_map.get(norm_rel, "2026-10-28")
            valid_entries.append((loc, lastmod))
            seen_locs.add(loc)

    # Reconstruct XML with strict UTF-8 header and xhtml namespace
    ET.register_namespace('', "http://www.sitemaps.org/schemas/sitemap/0.9")
    ET.register_namespace('xhtml', "http://www.w3.org/1999/xhtml")
    new_root = ET.Element("{http://www.sitemaps.org/schemas/sitemap/0.9}urlset")

    for loc, lastmod in valid_entries:
        u = ET.SubElement(new_root, "{http://www.sitemaps.org/schemas/sitemap/0.9}url")
        l = ET.SubElement(u, "{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        l.text = loc
        lm = ET.SubElement(u, "{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod")
        lm.text = lastmod

        if loc in HREFLANG_LOOKUP:
            for alt in HREFLANG_LOOKUP[loc]:
                xhtml_link = ET.SubElement(u, "{http://www.w3.org/1999/xhtml}link")
                xhtml_link.set("rel", alt["rel"])
                xhtml_link.set("hreflang", alt["hreflang"])
                xhtml_link.set("href", alt["href"])

    xml_str = ET.tostring(new_root, encoding="utf-8").decode("utf-8")
    dom = xml.dom.minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="  ", encoding="UTF-8").decode("utf-8")
    lines = [line for line in pretty_xml.splitlines() if line.strip()]
    SITEMAP_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  sitemap.xml updated with {len(valid_entries)} canonical URLs.")


def clean_and_update_search_index():
    print("\nSynchronizing search-index.json...")
    if not SEARCH_INDEX_PATH.exists():
        print("  search-index.json not found!")
        return

    with open(SEARCH_INDEX_PATH, encoding="utf-8") as f:
        existing_items = json.load(f)

    clean_items = []
    seen_urls = set()

    for item in existing_items:
        url = item.get("url", "")
        if not url:
            continue
            
        if "/data/" in url or url.startswith("/ur/"):
            continue
            
        clean_path = url.lstrip("/")
        if clean_path == "" or clean_path == "index.html":
            target = ROOT_DIR / "index.html"
        else:
            target = ROOT_DIR / clean_path
            if not target.exists() and (ROOT_DIR / f"{clean_path}.html").exists():
                target = ROOT_DIR / f"{clean_path}.html"
            elif not target.exists() and (ROOT_DIR / clean_path / "index.html").exists():
                target = ROOT_DIR / clean_path / "index.html"

        if target.exists() and url not in seen_urls:
            clean_items.append(item)
            seen_urls.add(url)

    observatory_search_records = [
        {
            "title": "Data Observatory & Interactive Knowledge Map",
            "type": "Data Observatory",
            "description": "Central empirical observatory: Interactive Knowledge Map of Pakistan's public data, Census 2023 baseline, NFC Reform Simulator, and district explorer.",
            "url": "/data/centre.html",
            "tags": ["data observatory", "knowledge map", "census 2023", "nfc simulator", "districts", "provinces", "data hub", "datasets", "statistics"]
        },
        {
            "title": "Pakistan Population 2023 Census: Total, Province-Wise & City Data",
            "type": "Data Observatory: Population",
            "description": "Pakistan had 241,499,431 people in the 2023 Census. Explore official province-wise population, urban and rural shares, major city counts, and 16 population FAQs.",
            "url": "/data/population/",
            "tags": ["population", "pakistan population", "census 2023", "punjab population", "sindh population", "kp population", "balochistan population", "karachi population", "lahore population", "urbanization", "growth rate", "demographics", "largest cities", "household size", "mother tongues", "population faqs"]
        },
        {
            "title": "Pakistan Economy, Inflation & Market Benchmarks Data",
            "type": "Data Observatory: Economy",
            "description": "Verified economic indicators: CPI & SPI inflation bulletins, real GDP growth rates (3.7%), sector growth, IT software exports ($3.39B), and wages.",
            "url": "/data/economy/",
            "tags": ["economy", "inflation", "cpi inflation", "spi inflation", "food prices", "gdp growth", "gdp per capita", "petrol price", "dollar rate", "remittances", "trade balance", "wages", "lsm growth", "it exports", "market prices"]
        },
        {
            "title": "Pakistan Living Standards, Poverty & Household Income Data",
            "type": "Data Observatory: Living Standards",
            "description": "PBS HIES 2024–25 household income and consumption: mean monthly household income PKR 82,179, mean consumption PKR 79,150, consumption-quintile comparisons, and living-standard indicators.",
            "url": "/data/living-standards/",
            "tags": ["living standards", "household income", "hies 2024", "consumption expenditure", "poverty", "income quintiles", "drinking water", "sanitation", "electricity access", "clean fuel", "wealth", "well-being"]
        },
        {
            "title": "Pakistan Public Finance, Budgets & NFC Award Formula Data",
            "type": "Data Observatory: Public Finance",
            "description": "Verified fiscal data: National Finance Commission (NFC) formula weights (82% population), provincial divisible pool transfers (Rs 5.5T+), tax revenue, and public debt.",
            "url": "/data/public-finance/",
            "tags": ["public finance", "nfc award", "divisible pool", "federal budget", "provincial budget", "fbr tax revenue", "public debt", "domestic debt", "external debt", "debt maturity", "education budget", "fiscal federalism"]
        },
        {
            "title": "Pakistan Education, Literacy & Human Capital Data",
            "type": "Data Observatory: Education",
            "description": "PBS HIES 2024–25 education indicators: 63% literacy among people aged 10+, provincial literacy rates, sex and urban-rural breakdowns, and a 28% out-of-school rate for children aged 5–16.",
            "url": "/data/education/",
            "tags": ["education", "literacy rate", "female literacy", "out of school children", "school completion", "education spending", "primary education", "secondary education", "human capital", "schools pakistan"]
        },
        {
            "title": "Pakistan Public Health & Demographic Health Indicators Data",
            "type": "Data Observatory: Health",
            "description": "Verified health indicators: child immunization coverage (73%), total fertility rate (3.6 births/woman), prenatal healthcare consultations, and maternal health access.",
            "url": "/data/health/",
            "tags": ["health", "public health", "child immunization", "vaccination", "fertility rate", "prenatal care", "contraceptive", "maternal health", "hospitals", "infant health"]
        },
        {
            "title": "Pakistan Digital Access, Mobile & Telecom Infrastructure Data",
            "type": "Data Observatory: Digital Access",
            "description": "Digital infrastructure data: 95% household mobile access, individual mobile ownership gender gap (30%), household broadband access (34%), and IT exports ($3.39B).",
            "url": "/data/digital-access/",
            "tags": ["digital access", "mobile phones", "internet access", "broadband", "telecom", "4g", "mobile ownership gender gap", "it exports", "computer access", "digital economy"]
        },
        {
            "title": "Subnational Comparator: Provinces & Administrative Units",
            "type": "Data Observatory: Comparator",
            "description": "Side-by-side empirical comparison of Punjab, Sindh, Khyber Pakhtunkhwa, Balochistan, and Islamabad across Census 2023 population, land area, urbanization, and living standards.",
            "url": "/data/compare/",
            "tags": ["compare", "provinces comparator", "punjab vs sindh", "balochistan vs punjab", "kp vs sindh", "subnational comparison", "provincial comparison", "territorial scale", "provincial density"]
        },
        {
            "title": "PPRI Pakistan Knowledge Library",
            "type": "Knowledge Library & Question Bank",
            "description": "Verified official statistics for Pakistan competitive exams (CSS, PMS), academic research, and policy journalism with one-click copyable APA citations.",
            "url": "/knowledge-library/",
            "tags": ["css", "pms", "css pakistan affairs", "fast facts", "exam facts", "pakistan facts", "css current affairs", "cheat sheet", "citations", "official numbers"]
        },
        {
            "title": "Open Public Data Downloads Hub",
            "type": "Data Observatory: Downloads",
            "description": "Download machine-readable CSV datasets: Census 2023 population, HIES 2024–25 income, inflation, and public debt under Creative Commons CC-BY 4.0.",
            "url": "/data/downloads/",
            "tags": ["downloads", "csv", "open data", "census 2023 csv", "hies download", "raw data", "pakistan datasets", "excel data"]
        },
        {
            "title": "Data Observatory Sources & Verification Methodology",
            "type": "Data Observatory: Methodology",
            "description": "Verification policies, primary official authorities (PBS, Finance Division, SBP), definition hygiene, and search intent mapping standards.",
            "url": "/data/methodology/",
            "tags": ["methodology", "data sources", "pbs", "verification", "definitions", "citations", "academic authority"]
        }
    ]

    for item in observatory_search_records:
        if item["url"] not in seen_urls:
            clean_items.append(item)
            seen_urls.add(item["url"])

    with open(SEARCH_INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(clean_items, f, indent=2, ensure_ascii=False)

    print(f"  search-index.json successfully updated with {len(clean_items)} verified entries.")

    # Generate Urdu Search Index
    print("\nGenerating search-index-ur.json...")
    urdu_search_records = [
        {
            "title": "پاکستان پروونشل ریفارم انسٹیٹیوٹ (PPRI) - مرکزی صفحہ",
            "type": "مرکزی پورٹل",
            "description": "پاکستان میں صوبائی اصلاحات، بااختیار بلدیات، 13 انتظامی یونٹس ماڈل، اور اضلاعی تفریق پر غیر جانبدارانہ تحقیق و ڈیٹا مشاہدہ گاہ۔",
            "url": "/ur/",
            "tags": ["مرکزی صفحہ", "ہوم", "پاکستان", "صوبائی اصلاحات", "بلدیات", "نئے صوبے", "پی پی آر آئی", "گورننس"]
        },
        {
            "title": "ادارے کا تعارف و فکری منشور (About PPRI)",
            "type": "ادارہ جاتی منشور",
            "description": "پاکستان پروونشل ریفارم انسٹیٹیوٹ کا تعارف، فکری منشور، غیر جانبدارانہ تحقیقی اصول، اور وفاقی و بلدیاتی اصلاحات کا ایجنڈا۔",
            "url": "/ur/about.html",
            "tags": ["تعارف", "منشور", "مشن", "تحقیقی اصول", "غیر جانبدارانہ", "ادارہ"]
        },
        {
            "title": "قومی حکمرانی سروے 2026 (National Governance Survey)",
            "type": "عوامی مشاورت",
            "description": "نئے صوبوں کی حد بندی، این ایف سی ایوارڈ، بااختیار بلدیات (آرٹیکل 140 اے)، اور بیوروکریسی کے بوجھ پر شہریوں کا تفصیلی سروے۔",
            "url": "/ur/consultation/survey.html",
            "tags": ["سروے", "عوامی مشاورت", "رائے شماری", "نئے صوبے", "این ایف سی", "آرٹیکل 140 اے", "بلدیاتی حکومتیں", "سوالنامہ"]
        },
        {
            "title": "عوامی مشاورت کا مرکز (Public Consultation Hub)",
            "type": "عوامی مشاورت",
            "description": "پاکستان میں صوبائی اصلاحات اور مقامی حکومتوں پر عوامی آراء، تجاویز اور قانونی یادداشتیں جمع کرانے کا پورٹل۔",
            "url": "/ur/consultation/",
            "tags": ["عوامی مشاورت", "مشاورتی مرکز", "تجاویز", "یادداشتیں", "سول سوسائٹی"]
        },
        {
            "title": "صوبائی تنظیمِ نو اور 13 انتظامی یونٹس ماڈل (Reform Framework)",
            "type": "صوبائی اصلاحات",
            "description": "پاکستان کے لیے 13 خود مختار صوبائی یونٹس کا مجوزہ انتظامی و آئینی ماڈل، آرٹیکل 239 ترمیم اور سینیٹ میں مساوی نمائندگی۔",
            "url": "/ur/provinces/",
            "tags": ["صوبائی اصلاحات", "13 یونٹس", "صوبائی تنظیم نو", "آرٹیکل 239", "انتظامی ڈویژن", "بہاولپور", "جنوبی پنجاب", "ہزارہ"]
        },
        {
            "title": "مرکزی ڈیٹا آبزرویٹری (Data Observatory)",
            "type": "ڈیٹا مشاہدہ گاہ",
            "description": "پاکستان کی 7ویں مردم شماری 2023، 130 اضلاع کا موازنہ، صوبائی جی ڈی پی اور این ایف سی ایوارڈ کے مستند سرکاری اعداد و شمار۔",
            "url": "/ur/data/centre.html",
            "tags": ["ڈیٹا", "اعداد و شمار", "مردم شماری 2023", "شماریات", "اضلاعی موازنہ", "اوپن ڈیٹا"]
        },
        {
            "title": "تحقیقاتی مرکز و ریسرچ رپورٹس (Research Hub)",
            "type": "تحقیقاتی مرکز",
            "description": "PPRI کا 2026 فلیگ شپ ریسرچ پروگرام: مہنگائی، بیوروکریسی، اضلاعی تفریق اور بلدیاتی فنانس پر 5 جامع رپورٹس۔",
            "url": "/ur/research/",
            "tags": ["تحقیق", "ریسرچ رپورٹس", "پالیسی پیپرز", "علمی مقالے", "شواہد"]
        },
        {
            "title": "تحقیقی رپورٹس ڈائریکٹری (Reports Index)",
            "type": "تحقیقاتی مرکز",
            "description": "تمام پانچوں فلیگ شپ پالیسی رپورٹس کے تفصیلی اردو خلاصہ جات اور اوپن ڈیٹا ڈاؤنلوڈز۔",
            "url": "/ur/research/reports/",
            "tags": ["رپورٹس", "خلاصہ جات", "پالیسی رپورٹس", "ڈائریکٹری"]
        },
        {
            "title": "آمدن بڑھی، تو زندگی مشکل کیوں ہوئی؟ (REP-01)",
            "type": "تحقیقی رپورٹ 001",
            "description": "HIES 2024-25 اور افراطِ زر کا تجزیہ: برائے نام تنخواہوں میں اضافے کے باوجود پاکستانی گھرانوں پر غذائی عدم تحفظ کا شدید دباؤ۔",
            "url": "/ur/research/reports/income-went-up-why-does-life-feel-harder.html",
            "tags": ["آمدن", "مہنگائی", "افراط زر", "خوراک", "غذائی عدم تحفظ", "HIES 2024", "قوت خرید"]
        },
        {
            "title": "ایک معمولی کام کی قیمت: بیوروکریسی کا بوجھ (REP-02)",
            "type": "تحقیقی رپورٹ 002",
            "description": "66 لاکھ شکایات کا جائزہ: شناختی کارڈ، ڈومیسائل اور زمین کے فرد کے حصول پر عام شہری کے وقت اور روزگار کے زیاں کا تخمینہ۔",
            "url": "/ur/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html",
            "tags": ["بیوروکریسی", "انتظامی بوجھ", "شکایات", "محتسب", "شناختی کارڈ", "ڈومیسائل", "سرکاری دفاتر"]
        },
        {
            "title": "ایک ہی ملک، مختلف زندگیاں: اضلاعی تفریق (REP-03)",
            "type": "تحقیقی رپورٹ 003",
            "description": "پاکستان کے 130 سے زائد اضلاع میں صاف پانی، پرائمری اسکولوں اور بنیادی صحت میں شدید علاقائی تفریق کا موازنہ۔",
            "url": "/ur/research/reports/same-country-different-life-district-access.html",
            "tags": ["اضلاعی تفریق", "صاف پانی", "تعلیم", "صحت", "پسماندگی", "بلوچستان", "جنوبی پنجاب", "تھرپارکر"]
        },
        {
            "title": "وہ رشوت جو دکھائی نہیں دیتی: نجی ٹیکس (REP-04)",
            "type": "تحقیقی رپورٹ 004",
            "description": "بدعنوانی بطور غیر علانیہ رجعت پسند نجی ٹیکس: کم آمدن والے شہریوں پر پولیس، پٹوار خانے اور بلدیاتی عملے کی رشوت کا بوجھ۔",
            "url": "/ur/research/reports/bribe-you-cant-see-corruption-private-tax.html",
            "tags": ["رشوت", "بدعنوانی", "نجی ٹیکس", "پٹوار خانہ", "پولیس", "کرپشن سروے"]
        },
        {
            "title": "کیا پیسہ عوام کے قریب خرچ ہو تو بہتر نتائج دیتا ہے؟ (REP-05)",
            "type": "تحقیقی رپورٹ 005",
            "description": "مقامی حکومتوں کی مالیات، ترقیاتی اخراجات کی صوبائی مرکزیت بمقابلہ بلدیاتی اختیارات کی تفویض پر بین الاقوامی و ملکی شواہد۔",
            "url": "/ur/research/reports/does-money-work-better-spent-closer-to-people.html",
            "tags": ["بلدیاتی فنانس", "مقامی حکومتیں", "آرٹیکل 140 اے", "ترقیاتی بجٹ", "این ایف سی", "پی ایف سی"]
        }
    ]

    with open(SEARCH_INDEX_UR_PATH, "w", encoding="utf-8") as f:
        json.dump(urdu_search_records, f, indent=2, ensure_ascii=False)

    print(f"  search-index-ur.json successfully generated with {len(urdu_search_records)} validated Urdu entries.")


def main():
    clean_and_update_sitemap()
    clean_and_update_search_index()


if __name__ == "__main__":
    main()
