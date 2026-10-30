# -*- coding: utf-8 -*-
"""
Test 1: XML Validation of Exported SVGs for all 16 Infographics.
Dumps DOM from data/staging/insights.html using Microsoft Edge headless,
assembles the exported SVG exactly as exportCard() does (including xmlText escaping,
cleanSource suffix stripping, stacked footer, and automated regex entity sanitization),
and verifies that xml.etree.ElementTree parses every single card's SVG with ZERO XML errors.
"""

import subprocess
import os
import re
import xml.etree.ElementTree as ET

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
html_path = os.path.abspath('data/staging/insights.html')
file_url = 'file:///' + html_path.replace('\\', '/')

print("Dumping rendered DOM from Edge headless...")
cmd = [edge, '--headless=new', '--dump-dom', '--virtual-time-budget=2000', file_url]
p = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', timeout=30)
dom = p.stdout
assert len(dom) > 100000, "DOM output too short"

card_ids = [
    'card-fiscal', 'card-debt', 'card-tax-exp', 'card-gender-land',
    'card-hies', 'card-consumption-pie', 'card-wage-infl', 'card-services',
    'card-lfs', 'card-census-shifts', 'card-districts-scatter', 'card-sector-employment',
    'card-agri-shifts', 'card-census-hist', 'card-macro', 'card-prov-matrix'
]

def xml_escape(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&apos;')

print(f"\n=======================================================")
print(f"  TEST 1: XML VALIDATION ACROSS ALL {len(card_ids)} EXPORTED SVGS")
print(f"=======================================================")

xml_errors = 0

for idx, cid in enumerate(card_ids, 1):
    svg_id = f'id="svg-{cid}"'
    start_svg = dom.find(svg_id)
    if start_svg == -1:
        print(f"[{idx:02d}/16] FAIL: svg-{cid} not found in DOM")
        xml_errors += 1
        continue
    
    end_svg = dom.find('</svg>', start_svg)
    chart_svg_tag = dom[start_svg:end_svg]
    tag_close = chart_svg_tag.find('>')
    inner_chart = chart_svg_tag[tag_close+1:].strip()
    
    # Extract card headers from DOM
    card_marker = f'id="{cid}"'
    c_idx = dom.find(card_marker)
    c_end = dom.find('</div>\n        </div>', c_idx)
    card_chunk = dom[c_idx:c_end] if c_idx != -1 else ""
    
    num_badge_m = re.search(r'class="vi-number-badge">([^<]+)<', card_chunk)
    num_badge = num_badge_m.group(1).strip() if num_badge_m else f"INFOGRAPHIC {idx:02d} / 16"
    
    tag_m = re.search(r'class="vi-card-tag">([^<]+)<', card_chunk)
    tag = tag_m.group(1).strip() if tag_m else "POLICY INFOGRAPHIC"
    
    title_m = re.search(r'class="vi-card-title">([^<]+)<', card_chunk)
    title = title_m.group(1).strip() if title_m else "PPRI Policy Infographic"
    
    subtitle_m = re.search(r'class="vi-card-subtitle">([^<]+)<', card_chunk)
    subtitle = subtitle_m.group(1).strip() if subtitle_m else ""
    
    source = "Pakistan Bureau of Statistics / Ministry of Finance"
    source_m = re.search(r'class="vi-source">([^<]+(?:<strong>[^<]+</strong>)*[^<]*)</div>', card_chunk)
    if source_m:
        raw_src = re.sub(r'<[^>]+>', '', source_m.group(1)).strip()
        source = raw_src
    
    clean_source = re.sub(r'\s*•\s*PPRI\s*$', '', source).strip()

    callout_id = f'id="callout-{cid}"'
    callout_idx = dom.find(callout_id)
    safe_callout = "Empirical Evidence & Policy Analysis"
    if callout_idx != -1:
        callout_close = dom.find('</div>', callout_idx)
        raw_text = re.sub(r'<[^>]+>', '', dom[callout_idx:callout_close]).strip()
        safe_callout = raw_text[:217] + '...' if len(raw_text) > 220 else raw_text

    safe_num_badge = xml_escape(num_badge)
    safe_tag = xml_escape(tag)
    safe_title = xml_escape(title)
    safe_subtitle = xml_escape(subtitle)
    safe_clean_source = xml_escape(clean_source)
    safe_callout = xml_escape(safe_callout)

    is_wide = 'col-12' in card_chunk
    export_w = 1040 if is_wide else 800
    export_h = 680 if is_wide else 620
    trans_x = 20
    trans_y = 115
    scale = 1.0

    full_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{export_w}" height="{export_h}" viewBox="0 0 {export_w} {export_h}">
  <defs>
    <style>
      text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }}
    </style>
  </defs>

  <rect width="{export_w}" height="{export_h}" fill="#ffffff" rx="10" stroke="#cbd5e1" stroke-width="1"/>
  <rect width="{export_w}" height="6" fill="#0f766e" rx="4"/>

  <!-- Top Header with Number Badge -->
  <text x="40" y="38" font-size="11" font-weight="700" fill="#0f766e" letter-spacing="1">PAKISTAN PROVINCIAL REFORM INSTITUTE (PPRI) • {safe_num_badge} • {safe_tag}</text>
  <text x="40" y="66" font-size="20" font-weight="800" fill="#073c3a">{safe_title}</text>
  <text x="40" y="88" font-size="12" fill="#64748b">{safe_subtitle}</text>
  <line x1="40" y1="102" x2="{export_w - 40}" y2="102" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Core Visual Graphics -->
  <g transform="translate({trans_x}, {trans_y}) scale({scale})">
    {inner_chart}
  </g>

  <!-- Key Insight Box -->
  <rect x="40" y="{export_h - 110}" width="{export_w - 80}" height="48" fill="#f8fafc" rx="6" stroke="#e2e8f0" stroke-width="1"/>
  <text x="54" y="{export_h - 93}" font-size="10" font-weight="800" fill="#073c3a">KEY POLICY INSIGHT:</text>
  <text x="54" y="{export_h - 77}" font-size="11" fill="#334155">{safe_callout}</text>

  <!-- Watermark Footer Banner (Two-Line Stacked: Zero Overlap) -->
  <rect x="0" y="{export_h - 52}" width="{export_w}" height="52" fill="#073c3a" rx="0"/>
  <!-- Line 1: Primary Data Source (Full Canvas Width) -->
  <text x="40" y="{export_h - 31}" font-size="10.5" font-weight="500" fill="#99f6e4">{safe_clean_source}</text>
  <!-- Line 2: Institution Branding & Canonical Domain -->
  <text x="40" y="{export_h - 14}" font-size="10.5" font-weight="700" fill="#ffffff">Pakistan Provincial Reform Institute (PPRI)</text>
  <text x="{export_w - 40}" y="{export_h - 14}" font-size="10.5" font-weight="600" fill="#5eead4" text-anchor="end">ppripakistan.github.io</text>
</svg>"""

    # Apply Tier 2 Automated XML Sanitizer
    clean_svg = full_svg
    for ent, char in [('&bull;', '•'), ('&rarr;', '→'), ('&ge;', '≥'), ('&le;', '≤'), ('&sim;', '~'), ('&radic;', '√'), ('&times;', '×'), ('&plusmn;', '±'), ('&nbsp;', ' ')]:
        clean_svg = clean_svg.replace(ent, char)
    clean_svg = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;|#\d+;|#x[0-9a-fA-F]+;)', '&amp;', clean_svg)

    try:
        ET.fromstring(clean_svg)
        print(f"  [PASS] Card {idx:02d}: {cid:24} -> 100% Valid XML 1.0 ({len(clean_svg):6} chars)")
    except ET.ParseError as err:
        print(f"  [FAIL] Card {idx:02d}: {cid:24} -> XML ParseError: {err}")
        xml_errors += 1

print(f"=======================================================")
print(f"  XML VALIDATION RESULT: {len(card_ids) - xml_errors}/{len(card_ids)} PASSED")
print(f"=======================================================")

assert xml_errors == 0, f"{xml_errors} cards failed XML validation!"
print(">>> ALL 16 EXPORTED SVGS ARE 100% VALID XML 1.0 WITH STACKED FOOTER! <<<")
