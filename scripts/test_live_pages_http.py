# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

PORT = 8772

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
server_thread = threading.Thread(target=httpd.serve_forever)
server_thread.daemon = True
server_thread.start()

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

test_pages = [
    {
        'url': f'http://localhost:{PORT}/insights/',
        'name': '/insights/ (Dynamic Interactive Lab)',
        'type': 'svg_elements',
        'expected': [
            'svg-card-fiscal', 'svg-card-debt', 'svg-card-tax-exp', 'svg-card-gender-land',
            'svg-card-hies', 'svg-card-consumption-pie', 'svg-card-wage-infl', 'svg-card-services',
            'svg-card-lfs', 'svg-card-census-shifts', 'svg-card-districts-scatter', 'svg-card-sector-employment',
            'svg-card-agri-shifts', 'svg-card-census-hist', 'svg-card-macro', 'svg-card-prov-matrix'
        ]
    },
    {
        'url': f'http://localhost:{PORT}/',
        'name': 'Homepage (/) (16-Card Visual Mosaic Grid)',
        'type': 'mosaic_images',
        'expected': [
            'card-fiscal', 'card-debt', 'card-tax-exp', 'card-prov-matrix',
            'card-wage-infl', 'card-sector-employment', 'card-agri-shifts', 'card-macro',
            'card-gender-land', 'card-census-shifts', 'card-districts-scatter', 'card-census-hist',
            'card-hies', 'card-consumption-pie', 'card-services', 'card-lfs'
        ]
    },
    {
        'url': f'http://localhost:{PORT}/data/public-finance/',
        'name': 'Public Finance (/data/public-finance/)',
        'type': 'svg_elements',
        'expected': [
            'svg-card-fiscal', 'svg-card-debt', 'svg-card-tax-exp', 'svg-card-prov-matrix'
        ]
    },
    {
        'url': f'http://localhost:{PORT}/data/economy/',
        'name': 'Economy (/data/economy/)',
        'type': 'svg_elements',
        'expected': [
            'svg-card-wage-infl', 'svg-card-sector-employment', 'svg-card-agri-shifts', 'svg-card-macro'
        ]
    },
    {
        'url': f'http://localhost:{PORT}/data/population/',
        'name': 'Population (/data/population/)',
        'type': 'svg_elements',
        'expected': [
            'svg-card-gender-land', 'svg-card-census-shifts', 'svg-card-districts-scatter', 'svg-card-census-hist'
        ]
    },
    {
        'url': f'http://localhost:{PORT}/data/living-standards/',
        'name': 'Living Standards (/data/living-standards/)',
        'type': 'svg_elements',
        'expected': [
            'svg-card-hies', 'svg-card-consumption-pie', 'svg-card-services', 'svg-card-lfs'
        ]
    }
]

try:
    all_passed = True
    for page in test_pages:
        url = page['url']
        name = page['name']
        expected = page['expected']
        p_type = page['type']
        print(f"\n--- Testing {name} ({len(expected)} items expected) ---")

        cmd = [
            edge,
            '--headless=new',
            '--disable-gpu',
            '--virtual-time-budget=4000',
            '--dump-dom',
            url
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
        dom = res.stdout.decode('utf-8', errors='ignore')

        page_ok = True
        if p_type == 'svg_elements':
            for svg_id in expected:
                pattern = re.compile(r'<svg[^>]*id=["\']' + svg_id + r'["\'][^>]*>(.*?)</svg>', re.DOTALL)
                match = pattern.search(dom)
                if not match:
                    print(f"  FAILED: {svg_id} not found in DOM")
                    page_ok = False
                    all_passed = False
                else:
                    inner = match.group(1).strip()
                    tag_count = len(re.findall(r'<(?:path|rect|text|circle|g|line)', inner))
                    print(f"  PASS: {svg_id} (rendered {tag_count} graphic tags, {len(inner)} bytes)")
        elif p_type == 'mosaic_images':
            for card_id in expected:
                # Check for image and link
                img_found = f'/assets/images/insights/{card_id}.svg' in dom
                link_found = f'/insights/#{card_id}' in dom
                if img_found and link_found:
                    print(f"  PASS: {card_id} -> Static Vector SVG & Deep Link verified in DOM")
                else:
                    print(f"  FAILED: {card_id} -> img={img_found}, link={link_found}")
                    page_ok = False
                    all_passed = False

        if page_ok:
            print(f"--> ALL {len(expected)} ITEMS VERIFIED IN {name}")

    if all_passed:
        print("\n=======================================================")
        print("ALL 6 PRODUCTION PAGES PASSED FULL HTTP VERIFICATION!")
        print("=======================================================")
    else:
        print("\nSOME TESTS FAILED!")
        sys.exit(1)

finally:
    httpd.shutdown()
    httpd.server_close()
