# -*- coding: utf-8 -*-
import subprocess
import os
import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(edge):
    print("Edge not found at:", edge)
    sys.exit(1)

test_pages = [
    {
        'path': 'insights/index.html',
        'expected_svgs': [
            'svg-card-fiscal', 'svg-card-debt', 'svg-card-tax-exp', 'svg-card-gender-land',
            'svg-card-hies', 'svg-card-consumption-pie', 'svg-card-wage-infl', 'svg-card-services',
            'svg-card-lfs', 'svg-card-census-shifts', 'svg-card-districts-scatter', 'svg-card-sector-employment',
            'svg-card-agri-shifts', 'svg-card-census-hist', 'svg-card-macro', 'svg-card-prov-matrix'
        ]
    },
    {
        'path': 'index.html',
        'expected_svgs': [
            'svg-card-fiscal', 'svg-card-prov-matrix', 'svg-card-districts-scatter'
        ]
    },
    {
        'path': 'data/public-finance/index.html',
        'expected_svgs': [
            'svg-card-fiscal', 'svg-card-debt', 'svg-card-tax-exp', 'svg-card-prov-matrix'
        ]
    },
    {
        'path': 'data/economy/index.html',
        'expected_svgs': [
            'svg-card-wage-infl', 'svg-card-sector-employment', 'svg-card-agri-shifts', 'svg-card-macro'
        ]
    },
    {
        'path': 'data/population/index.html',
        'expected_svgs': [
            'svg-card-gender-land', 'svg-card-census-shifts', 'svg-card-districts-scatter', 'svg-card-census-hist'
        ]
    },
    {
        'path': 'data/living-standards/index.html',
        'expected_svgs': [
            'svg-card-hies', 'svg-card-consumption-pie', 'svg-card-services', 'svg-card-lfs'
        ]
    }
]

print("=== RUNNING LIVE PAGE EMBED TESTS VIA HEADLESS EDGE ===")
all_passed = True

for page in test_pages:
    p = page['path']
    expected = page['expected_svgs']
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    expected_json = json.dumps(expected)

    # Create temporary instrumented test file
    harness = f"""
    <script>
    window.addEventListener('load', () => {{
      const results = {{}};
      const expected = {expected_json};
      expected.forEach(id => {{
        const el = document.getElementById(id);
        results[id] = {{
          exists: !!el,
          childCount: el ? el.childNodes.length : 0,
          innerHTML_len: el ? el.innerHTML.length : 0
        }};
      }});
      const outDiv = document.createElement('div');
      outDiv.id = '__test_results';
      outDiv.textContent = JSON.stringify(results);
      document.body.appendChild(outDiv);
    }});
    </script>
    """
    test_html = html.replace('</body>', harness + '</body>')
    temp_file = os.path.abspath(f"temp_test_{os.path.basename(os.path.dirname(p))}_{os.path.basename(p)}")
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(test_html)

    try:
        cmd = [
            edge,
            '--headless=new',
            '--disable-gpu',
            '--virtual-time-budget=5000',
            '--dump-dom',
            f'file:///{temp_file.replace(os.sep, "/")}'
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=25)
        dom = res.stdout.decode('utf-8', errors='ignore')

        match = re.search(r'<div id="__test_results">(.*?)</div>', dom)
        if match:
            data = json.loads(match.group(1))
            page_ok = True
            print(f"\n--- Testing {p} ({len(expected)} cards expected) ---")
            for svg_id, stats in data.items():
                if not stats['exists'] or stats['innerHTML_len'] == 0:
                    print(f"  FAILED: {svg_id} -> exists={stats['exists']}, len={stats['innerHTML_len']}")
                    page_ok = False
                    all_passed = False
                else:
                    print(f"  PASS: {svg_id} (rendered {stats['childCount']} SVG elements, {stats['innerHTML_len']} bytes)")
            if page_ok:
                print(f"--> ALL {len(expected)} SVGs RENDERED SUCCESSFULLY IN {p}")
        else:
            print(f"\nFAILED to capture test results from {p}")
            all_passed = False

    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

if all_passed:
    print("\n==========================================")
    print("ALL 6 LIVE PAGES PASSED HEADLESS RENDERING!")
    print("==========================================")
else:
    print("\nSOME TESTS FAILED! Review details above.")
    sys.exit(1)
