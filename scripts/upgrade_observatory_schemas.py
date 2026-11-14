#!/usr/bin/env python3
import json
import re
from pathlib import Path

BASE_URL = "https://ppripakistan.github.io"

OBSERVATORIES = {
    "population": {
        "name": "Pakistan Population, Demographics & Urbanization Dataset (7th Census 2023)",
        "alternateName": "PBS Census 2023 Provincial & City Population Data — PPRI Data Observatory",
        "description": "Verified Pakistan Bureau of Statistics (PBS) 7th Population and Housing Census 2023 dataset covering national population (241,499,431), provincial distributions (Punjab, Sindh, Khyber Pakhtunkhwa, Balochistan, Islamabad), urban-rural shares, household size, and top 22 major urban localities.",
        "keywords": [
            "Pakistan population 2023 census",
            "Pakistan provinces population 2026",
            "Punjab Sindh KP Balochistan population",
            "Karachi Lahore population census 2023",
            "Pakistan demographics urbanization"
        ],
        "citation": "Pakistan Bureau of Statistics (PBS), 7th Population and Housing Census 2023, Tables 1, 2, 4 & Major Localities.",
        "temporalCoverage": "2017/2026",
        "csv_path": "/data/downloads/pakistan-population-census-2023.csv",
        "variables": [
            {"@type": "PropertyValue", "name": "Total Population", "unitText": "persons"},
            {"@type": "PropertyValue", "name": "Annual Population Growth Rate (2017-2023)", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Urbanization Share", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Average Household Size", "unitText": "persons per household"}
        ],
        "title": "Pakistan Population by Province & City (Census 2023 Data)",
        "meta_desc": "Official PBS 7th Census 2023 dataset: Pakistan population (241.5M), Punjab, Sindh, KP & Balochistan shares, growth rates, and top 22 cities. Download CSV."
    },
    "economy": {
        "name": "Pakistan Macroeconomic Benchmarks, Inflation & Public Debt Dataset (2026)",
        "alternateName": "Pakistan Macroeconomic Indicators & Fiscal Baseline — PPRI Data Observatory",
        "description": "Official Ministry of Finance, State Bank of Pakistan (SBP), and PBS macroeconomic dataset tracking GDP growth, CPI and SPI inflation indices, debt-to-GDP ratios, external debt service burdens, and tax revenue performance.",
        "keywords": [
            "Pakistan macroeconomic data 2026",
            "Pakistan inflation rate CPI SPI",
            "Pakistan GDP growth benchmarks",
            "Pakistan debt to GDP ratio",
            "Pakistan economic indicators"
        ],
        "citation": "Ministry of Finance, State Bank of Pakistan & Pakistan Bureau of Statistics (PBS) Macroeconomic Statistics 2024-2026.",
        "temporalCoverage": "2018/2026",
        "csv_path": "/data/downloads/pakistan-economic-benchmarks-2026.csv",
        "variables": [
            {"@type": "PropertyValue", "name": "GDP Growth Rate", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Consumer Price Index (CPI) Inflation", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Public Debt to GDP", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Tax-to-GDP Ratio", "unitText": "percent"}
        ],
        "title": "Pakistan Economic Benchmarks & Inflation Data (2026) | PPRI",
        "meta_desc": "Verified macroeconomic benchmarks: GDP growth, CPI/SPI inflation trends, public debt trajectory, tax-to-GDP ratio, and monetary policy indicators. Download CSV."
    },
    "education": {
        "name": "Pakistan Education, Literacy & Human Capital Dataset (HIES 2024–25)",
        "alternateName": "PBS HIES & PSLM Education & Literacy Benchmarks — PPRI Data Observatory",
        "description": "Comprehensive subnational education dataset covering adult and youth literacy rates, provincial gender parity gaps, school participation by wealth quintile, and out-of-school children distributions.",
        "keywords": [
            "Pakistan literacy rate 2025 2026",
            "province wise literacy rate pakistan",
            "out of school children pakistan",
            "gender parity education pakistan",
            "HIES education statistics"
        ],
        "citation": "Pakistan Bureau of Statistics, Household Integrated Economic Survey (HIES) 2024-25 & PSLM Education Modules.",
        "temporalCoverage": "2020/2026",
        "csv_path": "/data/downloads/pakistan-education-literacy-hies-2024-25.csv",
        "variables": [
            {"@type": "PropertyValue", "name": "Literacy Rate (10 Years and Above)", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Primary School Net Attendance Rate", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Out of School Children (OOSC)", "unitText": "persons"},
            {"@type": "PropertyValue", "name": "Gender Parity Index in Primary Education", "unitText": "ratio"}
        ],
        "title": "Pakistan Education & Literacy Rate by Province (2025–26 Data) | PPRI",
        "meta_desc": "Official PBS HIES 2024–25 education data: Pakistan literacy rates, provincial comparisons (Punjab, Sindh, KP, Balochistan), gender parity, and school access. Download CSV."
    },
    "health": {
        "name": "Pakistan Public Health & Demographic Indicators Dataset (2026)",
        "alternateName": "Pakistan Demographic and Health Indicators — PPRI Data Observatory",
        "description": "Verified health indicators covering child immunization rates (73%), total fertility rate (3.6 births/woman), prenatal healthcare consultations (88%), contraceptive prevalence, and reproductive health autonomy.",
        "keywords": [
            "Pakistan health indicators 2026",
            "child immunization rate pakistan",
            "total fertility rate pakistan",
            "prenatal healthcare access pakistan",
            "PDHS health survey data"
        ],
        "citation": "National Institute of Population Studies (NIPS) & Pakistan Bureau of Statistics, PDHS & PSLM Health Bulletins.",
        "temporalCoverage": "2020/2026",
        "csv_path": "/data/downloads/pakistan-health-indicators-2026.csv",
        "variables": [
            {"@type": "PropertyValue", "name": "Fully Immunized Children (12-23 Months)", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Total Fertility Rate", "unitText": "births per woman"},
            {"@type": "PropertyValue", "name": "Prenatal Care Consultation Rate", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Contraceptive Prevalence Rate", "unitText": "percent"}
        ],
        "title": "Pakistan Public Health Indicators & Immunization Data (2026) | PPRI",
        "meta_desc": "Official health benchmarks: 73% immunization, 3.6 TFR, maternal health consultations, and urban-rural healthcare delivery metrics across provinces. Download CSV."
    },
    "living-standards": {
        "name": "Pakistan Household Income, Poverty & Food Insecurity Dataset (HIES 2024–25)",
        "alternateName": "PBS HIES 2024–25 Household Income & Living Standards — PPRI Data Observatory",
        "description": "Official PBS HIES 2024–25 living standards dataset detailing average monthly household income (Rs 82,179 national average), income quintile distributions, moderate/severe food insecurity rates (24.35%), and household consumption baskets.",
        "keywords": [
            "average household income pakistan",
            "pakistan poverty rate 2026",
            "food insecurity pakistan HIES",
            "household income quintiles pakistan",
            "PBS HIES 2024 25 data"
        ],
        "citation": "Pakistan Bureau of Statistics, Household Integrated Economic Survey (HIES) 2024-25, Living Standards & Consumption Tables.",
        "temporalCoverage": "2024/2026",
        "csv_path": "/data/downloads/pakistan-household-income-consumption-hies-2024-25.csv",
        "variables": [
            {"@type": "PropertyValue", "name": "Average Monthly Household Income", "unitText": "PKR"},
            {"@type": "PropertyValue", "name": "Food Insecurity (FIES Moderate or Severe)", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "National Poverty Headcount Rate", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Average Household Consumption Expenditure", "unitText": "PKR"}
        ],
        "title": "Pakistan Household Income, Poverty & Living Standards (HIES 2024–25) | PPRI",
        "meta_desc": "PBS HIES 2024–25 dataset: Average household income (Rs 82,179/mo), poverty headcount (28.9%), food insecurity (24.35%), and quintile distributions. Download CSV."
    },
    "digital-access": {
        "name": "Pakistan Digital Access, Mobile & Technology Connectivity Dataset (HIES 2024–25)",
        "alternateName": "Pakistan Digital Divide & Telecommunications Data — PPRI Data Observatory",
        "description": "Empirical survey data on broadband connectivity, mobile telephone ownership (96.2% national penetration), smartphone adoption, and urban-rural digital divide metrics across Pakistani households.",
        "keywords": [
            "pakistan digital access data",
            "mobile phone penetration pakistan",
            "internet access by province pakistan",
            "digital divide pakistan HIES",
            "broadband connectivity pakistan"
        ],
        "citation": "Pakistan Bureau of Statistics, HIES 2024-25 Technology Access Module & PTA Telecommunications Indicators.",
        "temporalCoverage": "2024/2026",
        "csv_path": "/data/downloads/pakistan-digital-access-hies-2024-25.csv",
        "variables": [
            {"@type": "PropertyValue", "name": "Household Mobile Telephone Ownership", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Household Internet Access Rate", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Computer/Laptop Ownership Rate", "unitText": "percent"}
        ],
        "title": "Pakistan Digital Access & Mobile Connectivity Data (2025–26) | PPRI",
        "meta_desc": "Official PBS HIES 2024–25 technology dataset: 96.2% mobile ownership, internet adoption rates, urban-rural digital divide, and provincial tech metrics. Download CSV."
    },
    "public-finance": {
        "name": "Pakistan Public Finance, Federal Budgets & NFC Award Allocations Dataset",
        "alternateName": "Pakistan Fiscal Federalism & Provincial Finance Baseline — PPRI Data Observatory",
        "description": "Comprehensive subnational public finance dataset documenting 7th NFC Award formula distributions (Punjab 51.74%, Sindh 24.55%, KP 14.62%, Balochistan 9.09%), provincial revenue generation vs. federal transfers, and ADP expenditures.",
        "keywords": [
            "nfc award formula pakistan",
            "7th nfc award provincial shares",
            "provincial finance commission pakistan",
            "pakistan public finance budget data",
            "federal transfers to provinces"
        ],
        "citation": "Federal Ministry of Finance, Provincial Finance Departments & National Finance Commission Secretariat.",
        "temporalCoverage": "2020/2026",
        "csv_path": "/data/downloads/province_baseline_2023.csv",
        "variables": [
            {"@type": "PropertyValue", "name": "NFC Divisible Pool Share", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Annual Federal Transfer Allocation", "unitText": "PKR billion"},
            {"@type": "PropertyValue", "name": "Provincial Own-Source Revenue Share", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Annual Development Programme (ADP) Budget", "unitText": "PKR billion"}
        ],
        "title": "Pakistan Public Finance & 7th NFC Award Allocations Data | PPRI",
        "meta_desc": "Verified fiscal federalism dataset: 7th NFC Award provincial shares (Punjab, Sindh, KP, Balochistan), federal divisible pool transfers, and own-source tax data. Download CSV."
    },
    "compare": {
        "name": "Pakistan Provinces & Subnational Administrative Units Comparative Dataset",
        "alternateName": "Pakistan Subnational Comparative Governance Matrix — PPRI Data Observatory",
        "description": "Unified comparative matrix synthesizing Census 2023 populations, geographic land areas, literacy rates, poverty headcounts, NFC shares, and National Assembly seats across Punjab, Sindh, KP, Balochistan, ICT, GB, and AJK.",
        "keywords": [
            "pakistan provinces comparison data",
            "punjab vs sindh vs kp vs balochistan",
            "provinces of pakistan facts and figures",
            "subnational administrative matrix pakistan",
            "pakistan territory metrics"
        ],
        "citation": "Pakistan Bureau of Statistics (PBS), Election Commission of Pakistan (ECP) & PPRI Subnational Matrix.",
        "temporalCoverage": "2023/2026",
        "csv_path": "/data/downloads/pakistan-provinces-census-2023.csv",
        "variables": [
            {"@type": "PropertyValue", "name": "Census Population (2023)", "unitText": "persons"},
            {"@type": "PropertyValue", "name": "Total Land Area", "unitText": "square kilometers"},
            {"@type": "PropertyValue", "name": "Population Density", "unitText": "persons per sq km"},
            {"@type": "PropertyValue", "name": "National Assembly General Seats", "unitText": "seats"}
        ],
        "title": "Pakistan Provinces Comparator: Population, Area & Fiscal Metrics | PPRI",
        "meta_desc": "Side-by-side comparative data for Pakistan's provinces and territories: Census 2023 population, area, literacy, poverty, NA seats, and NFC shares. Download CSV."
    },
    "downloads": {
        "name": "Pakistan Provincial Reform Institute Open Data Catalog & Master Manifest",
        "alternateName": "PPRI Open Data Repository & Primary Source CSV Downloads",
        "description": "Complete public catalog of all open-access datasets published by PPRI, including 2023 Census demographics, HIES 2024-25 socio-economic surveys, NFC fiscal models, and administrative boundary geospatial matrices.",
        "keywords": [
            "pakistan open data catalog",
            "pakistan census csv download",
            "HIES survey datasets download",
            "pakistan public policy research data",
            "PPRI data repository"
        ],
        "citation": "Pakistan Provincial Reform Institute Open Data Repository (CC-BY-4.0).",
        "temporalCoverage": "2017/2026",
        "csv_path": "/data/downloads/ppri-open-data-catalog-manifest.csv",
        "variables": [
            {"@type": "PropertyValue", "name": "Published Open Datasets Count", "unitText": "datasets"},
            {"@type": "PropertyValue", "name": "Data Encoding Standard", "unitText": "CSV, JSON"}
        ],
        "title": "PPRI Open Data Catalog: Download Pakistan Datasets (CSV & JSON)",
        "meta_desc": "Download verified Pakistan policy datasets: 2023 Census population, HIES 2024–25 income & poverty, NFC public finance, literacy rates, and GIS matrices. 100% Free CSV."
    },
    "methodology": {
        "name": "Pakistan Provincial Reform Institute Data Architecture & Methodology Specification",
        "alternateName": "PPRI Data Science Standards, Sources & Verification Framework",
        "description": "Technical specification and data integrity protocols governing PPRI datasets: statistical sampling bounds, PBS Census 2023 reconciliation methods, HIES 2024-25 microdata processing, and GIS boundary standards.",
        "keywords": [
            "PPRI data methodology",
            "pakistan data verification standards",
            "census 2023 reconciliation method",
            "hies survey microdata methodology",
            "spatial modeling methodology pakistan"
        ],
        "citation": "Pakistan Provincial Reform Institute Data Architecture & Standards Board.",
        "temporalCoverage": "2023/2026",
        "csv_path": "/data/downloads/ppri-open-data-catalog-manifest.csv",
        "variables": [
            {"@type": "PropertyValue", "name": "Data Confidence Level", "unitText": "percent"},
            {"@type": "PropertyValue", "name": "Administrative Districts Cataloged", "unitText": "districts"}
        ],
        "title": "PPRI Data Architecture & Research Methodology | PPRI",
        "meta_desc": "Learn how PPRI collects, cleans, verifies, and analyzes Pakistan public-policy data: PBS Census 2023 standards, HIES microdata protocols, and GIS modeling."
    }
}

CANONICAL_NAV = """        <nav id="site-navigation" class="nav-links" aria-label="Primary navigation">
          <a href="/">Home</a>
          <a href="/constitution/">Constitution</a>
          <a href="/research/">Research</a>
          <a href="/provinces/">Reform</a>
          <a href="/scenarios/">Scenarios</a>
          <a href="/insights/">Insights</a>
          <a href="/data/centre.html" aria-current="page">Data</a>
          <a href="/publications/">Publications</a>
          <a href="/consultation/">Engage</a>
          <a href="/about.html">About</a>
          <a class="nav-search" href="/search.html">Search</a>
        </nav>"""

def build_dataset_jsonld(slug, meta):
    dataset_url = f"{BASE_URL}/data/{slug}/"
    csv_url = f"{BASE_URL}{meta['csv_path']}"
    
    schema = {
        "@context": "https://schema.org",
        "@type": "Dataset",
        "@id": f"{dataset_url}#dataset",
        "name": meta["name"],
        "alternateName": meta["alternateName"],
        "description": meta["description"],
        "url": dataset_url,
        "keywords": meta["keywords"],
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "isAccessibleForFree": True,
        "creator": {
            "@type": "Organization",
            "@id": f"{BASE_URL}/#organization",
            "name": "Pakistan Provincial Reform Institute (PPRI)",
            "url": BASE_URL
        },
        "publisher": {
            "@type": "Organization",
            "@id": f"{BASE_URL}/#organization",
            "name": "Pakistan Provincial Reform Institute (PPRI)"
        },
        "citation": meta["citation"],
        "temporalCoverage": meta["temporalCoverage"],
        "spatialCoverage": {
            "@type": "Place",
            "name": "Pakistan",
            "geo": {
                "@type": "GeoShape",
                "box": "23.6345 60.8729 37.0841 77.8375"
            }
        },
        "variableMeasured": meta["variables"],
        "distribution": [
            {
                "@type": "DataDownload",
                "encodingFormat": "text/csv",
                "contentUrl": csv_url
            }
        ],
        "datePublished": "2026-09-15",
        "dateModified": "2026-11-14"
    }
    return json.dumps(schema, indent=2, ensure_ascii=False)

def build_breadcrumb_jsonld(slug, meta):
    page_url = f"{BASE_URL}/data/{slug}/"
    name = meta["name"].split(" Dataset")[0]
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": f"{BASE_URL}/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Data Observatory",
                "item": f"{BASE_URL}/data/centre.html"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": name,
                "item": page_url
            }
        ]
    }
    return json.dumps(schema, indent=2, ensure_ascii=False)

for slug, meta in OBSERVATORIES.items():
    file_path = Path(f"data/{slug}/index.html")
    if not file_path.exists():
        print(f"Skipping missing: {file_path}")
        continue
    
    html = file_path.read_text(encoding="utf-8")
    
    # 1. Update Title and Meta Description
    html = re.sub(r'<title>.*?</title>', f'<title>{meta["title"]}</title>', html, count=1, flags=re.DOTALL)
    html = re.sub(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'][^"\']*["\'][^>]*>', 
                  f'<meta name="description" content="{meta["meta_desc"]}" />', html, count=1)

    # 2. Update og:title and og:description
    html = re.sub(r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\'][^"\']*["\'][^>]*>', 
                  f'<meta property="og:title" content="{meta["title"]}" />', html, count=1)
    html = re.sub(r'<meta[^>]*property=["\']og:description["\'][^>]*content=["\'][^"\']*["\'][^>]*>', 
                  f'<meta property="og:description" content="{meta["meta_desc"]}" />', html, count=1)

    # 3. Update twitter:title and twitter:description
    html = re.sub(r'<meta[^>]*name=["\']twitter:title["\'][^>]*content=["\'][^"\']*["\'][^>]*>', 
                  f'<meta name="twitter:title" content="{meta["title"]}" />', html, count=1)
    html = re.sub(r'<meta[^>]*name=["\']twitter:description["\'][^>]*content=["\'][^"\']*["\'][^>]*>', 
                  f'<meta name="twitter:description" content="{meta["meta_desc"]}" />', html, count=1)

    # 4. Replace existing Dataset and Breadcrumb JSON-LD scripts
    dataset_json = build_dataset_jsonld(slug, meta)
    breadcrumb_json = build_breadcrumb_jsonld(slug, meta)
    
    # Remove existing application/ld+json blocks
    html = re.sub(r'<script\s+type=["\']application/ld\+json["\']>.*?</script>\s*', '', html, flags=re.DOTALL)
    
    # Inject new clean structured data right before </head>
    new_jsonld = f"""    <script type="application/ld+json">
{dataset_json}
    </script>
    <script type="application/ld+json">
{breadcrumb_json}
    </script>
  </head>"""
    html = html.replace("</head>", new_jsonld, 1)

    # 5. Standardize Primary Navigation
    html = re.sub(r'<nav\s+id=["\']site-navigation["\'][^>]*>.*?</nav>', CANONICAL_NAV, html, count=1, flags=re.DOTALL)
    
    # 6. Ensure direct static CSV download link points to actual CSV
    csv_url = meta["csv_path"]
    if slug == "health":
        html = html.replace("/data/downloads/pakistan-economic-benchmarks-2026.csv", csv_url)

    file_path.write_text(html, encoding="utf-8")
    print(f"[UPGRADED] {file_path} -> Title, Meta, Dataset & Breadcrumbs JSON-LD")

print("Done upgrading all 10 observatories.")
