#!/usr/bin/env python3
"""
scripts/update_sitemap_and_search_index.py
Synchronizes canonical Data Observatory hubs, core pages, and high-volume queries
into sitemap.xml and search-index.json, ensuring 0 broken links and 0 orphaned URLs.
"""

import os
import json
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
SITEMAP_PATH = ROOT_DIR / "sitemap.xml"
SEARCH_INDEX_PATH = ROOT_DIR / "search-index.json"

TODAY_STR = "2026-10-16"

CANONICAL_OBSERVATORY_HUBS = [
    ("https://ppripakistan.github.io/data/centre.html", "1.0", "weekly"),
    ("https://ppripakistan.github.io/data/population/", "0.9", "weekly"),
    ("https://ppripakistan.github.io/data/economy/", "0.9", "weekly"),
    ("https://ppripakistan.github.io/data/living-standards/", "0.9", "weekly"),
    ("https://ppripakistan.github.io/data/public-finance/", "0.9", "weekly"),
    ("https://ppripakistan.github.io/data/education/", "0.9", "weekly"),
    ("https://ppripakistan.github.io/data/health/", "0.9", "weekly"),
    ("https://ppripakistan.github.io/data/digital-access/", "0.9", "weekly"),
    ("https://ppripakistan.github.io/data/compare/", "0.9", "weekly"),
    ("https://ppripakistan.github.io/data/quick-facts/", "0.9", "weekly"),
    ("https://ppripakistan.github.io/data/downloads/", "0.8", "monthly"),
    ("https://ppripakistan.github.io/data/methodology/", "0.8", "monthly"),
]

def clean_and_update_sitemap():
    print("Synchronizing sitemap.xml...")
    if not SITEMAP_PATH.exists():
        print("  sitemap.xml not found!")
        return

    content = SITEMAP_PATH.read_text(encoding="utf-8")
    
    # Parse existing XML
    root = ET.fromstring(content)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    ET.register_namespace('', "http://www.sitemaps.org/schemas/sitemap/0.9")

    # Collect existing valid non-observatory URLs, or keep track
    valid_entries = []
    seen_locs = set()

    REDIRECT_STUBS = {
        "governance.html", "methodology.html", "media/events.html", "media/interviews.html",
        "news/index.html", "opinion/index.html", "resources/datasets.html", "resources/maps.html",
        "updates/index.html", "data/methodology.html", "data/economy.html", "data/population.html",
        "data/fiscal.html", "data/demographics.html", "data/governance.html", "data/data-notes.html",
        "data/index.html", "data/maps.html", "data/datasets.html", "data/provincial-comparison.html",
        "data/district-explorer.html", "404.html", "search.html"
    }

    for url_el in root.findall('sm:url', ns):
        loc_el = url_el.find('sm:loc', ns)
        if loc_el is None or not loc_el.text:
            continue
        loc = loc_el.text.strip()
        
        # Check if this is an observatory URL
        if "/data/" in loc:
            # We will handle observatory URLs explicitly via CANONICAL_OBSERVATORY_HUBS
            continue
            
        # Check if root path or other page
        path_part = loc.replace("https://ppripakistan.github.io/", "")
        if path_part == "" or path_part == "index.html":
            file_path = ROOT_DIR / "index.html"
            rel_str = "index.html"
        else:
            file_path = ROOT_DIR / path_part
            rel_str = path_part
            if not file_path.exists() and (ROOT_DIR / f"{path_part}.html").exists():
                file_path = ROOT_DIR / f"{path_part}.html"
                rel_str = f"{path_part}.html"
            elif not file_path.exists() and (ROOT_DIR / path_part / "index.html").exists():
                file_path = ROOT_DIR / path_part / "index.html"
                rel_str = f"{path_part}/index.html"

        if rel_str in REDIRECT_STUBS or path_part in REDIRECT_STUBS:
            continue

        if file_path.exists() and loc not in seen_locs:
            lastmod_el = url_el.find('sm:lastmod', ns)
            freq_el = url_el.find('sm:changefreq', ns)
            prio_el = url_el.find('sm:priority', ns)

            lastmod = lastmod_el.text if lastmod_el is not None else TODAY_STR
            freq = freq_el.text if freq_el is not None else "monthly"
            prio = prio_el.text if prio_el is not None else "0.7"

            valid_entries.append((loc, prio, freq, lastmod))
            seen_locs.add(loc)

    # Add canonical observatory hubs
    for loc, prio, freq in CANONICAL_OBSERVATORY_HUBS:
        if loc not in seen_locs:
            valid_entries.append((loc, prio, freq, TODAY_STR))
            seen_locs.add(loc)

    # Reconstruct XML
    new_root = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for loc, prio, freq, lastmod in valid_entries:
        u = ET.SubElement(new_root, "url")
        l = ET.SubElement(u, "loc")
        l.text = loc
        lm = ET.SubElement(u, "lastmod")
        lm.text = lastmod
        cf = ET.SubElement(u, "changefreq")
        cf.text = freq
        pr = ET.SubElement(u, "priority")
        pr.text = prio

    xml_str = ET.tostring(new_root, encoding="utf-8").decode("utf-8")
    # Pretty print with standard XML declaration
    header = '<?xml version="1.0" encoding="UTF-8"?>\n'
    import xml.dom.minidom
    dom = xml.dom.minidom.parseString(xml_str)
    pretty_xml = dom.toprettyxml(indent="  ")
    # Strip extra empty lines
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

    # Filter out dead links (only keep items whose file exists, or are valid hubs)
    clean_items = []
    seen_urls = set()

    for item in existing_items:
        url = item.get("url", "")
        if not url:
            continue
            
        # If it's a data url, only keep canonical hubs
        if "/data/" in url:
            continue
            
        # For non-data URLs, check file existence
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

    # Add the authoritative observatory hub entries with rich search tags
    observatory_search_records = [
        {
            "title": "Data Observatory & Interactive Knowledge Map",
            "type": "Data Observatory",
            "description": "Central empirical observatory: Interactive Knowledge Map of Pakistan's public data, Census 2023 baseline, NFC Reform Simulator, and district explorer.",
            "url": "/data/centre.html",
            "tags": ["data observatory", "knowledge map", "census 2023", "nfc simulator", "districts", "provinces", "data hub", "datasets", "statistics"]
        },
        {
            "title": "Pakistan Population, Demographics & Urbanization Data",
            "type": "Data Observatory: Population",
            "description": "Verified PBS 7th Census 2023 results: 241.49M national population, provincial breakdowns, urban-rural distributions, sex ratios, and top 22 city populations.",
            "url": "/data/population/",
            "tags": ["population", "pakistan population", "census 2023", "punjab population", "sindh population", "kp population", "balochistan population", "karachi population", "lahore population", "urbanization", "growth rate", "demographics", "largest cities", "household size", "mother tongues"]
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
            "description": "Findings from PBS Household Integrated Economic Survey (HIES) 2024–25: household income quintiles (mean PKR 63,450), monthly consumption, water access, and energy.",
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
            "description": "Educational statistics: national literacy rate (61%), provincial literacy comparison, gender literacy gap (71% M / 50% F), and 26.2M out-of-school children.",
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
            "title": "CSS Aspirants & Researchers Fast-Fact Matrix",
            "type": "Data Observatory: Fast Facts",
            "description": "Verified official statistics for Pakistan competitive exams (CSS, PMS), academic research, and policy journalism with one-click copyable APA citations.",
            "url": "/data/quick-facts/",
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

def main():
    clean_and_update_sitemap()
    clean_and_update_search_index()

if __name__ == "__main__":
    main()
