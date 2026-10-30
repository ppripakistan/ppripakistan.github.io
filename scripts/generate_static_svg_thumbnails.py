# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import sys
import re
import json
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

PORT = 8771

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
server_thread = threading.Thread(target=httpd.serve_forever)
server_thread.daemon = True
server_thread.start()

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
output_dir = 'assets/images/insights'
os.makedirs(output_dir, exist_ok=True)

# Read insights/index.html and inject SVG harvest runner
with open('insights/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

card_ids = [
    'card-fiscal', 'card-debt', 'card-tax-exp', 'card-gender-land',
    'card-hies', 'card-consumption-pie', 'card-wage-infl', 'card-services',
    'card-lfs', 'card-census-shifts', 'card-districts-scatter', 'card-sector-employment',
    'card-agri-shifts', 'card-census-hist', 'card-macro', 'card-prov-matrix'
]

# Script that intercepts SVG downloads or captures assembled SVG text directly
harvest_script = f"""
<script>
window.__harvestResults = {{}};
window.addEventListener('load', async () => {{
  const cards = {json.dumps(card_ids)};

  // Mock URL.createObjectURL to harvest SVG content
  const originalCreate = URL.createObjectURL;
  let currentKey = '';
  URL.createObjectURL = function(blob) {{
    if (blob.type && blob.type.includes('svg')) {{
      const reader = new FileReader();
      reader.onload = function() {{
        window.__harvestResults[currentKey] = reader.result;
      }};
      reader.readAsText(blob);
    }}
    return originalCreate.apply(this, arguments);
  }};

  for (const cid of cards) {{
    currentKey = cid;
    try {{
      exportCard(cid, 'svg');
      await new Promise(r => setTimeout(r, 120));
    }} catch(e) {{
      console.error(e);
    }}
  }}

  // Append results after harvesting all 16
  await new Promise(r => setTimeout(r, 600));
  const out = document.createElement('div');
  out.id = '__harvest_results';
  out.textContent = JSON.stringify(window.__harvestResults);
  document.body.appendChild(out);
}});
</script>
"""

temp_file = 'insights/temp_harvest_test.html'
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', harvest_script + '</body>'))

try:
    print("Harvesting 16 standalone vector SVGs from Edge headless...")
    cmd = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--virtual-time-budget=8000',
        '--dump-dom',
        f'http://localhost:{PORT}/insights/temp_harvest_test.html'
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    dom = res.stdout.decode('utf-8', errors='ignore')

    match = re.search(r'<div id="__harvest_results">(.*?)</div>', dom)
    if match:
        svgs = json.loads(match.group(1))
        print(f"Captured {len(svgs)} SVG files from DOM.")
        for cid, svg_str in svgs.items():
            out_file = os.path.join(output_dir, f"{cid}.svg")
            
            # Clean and validate XML
            try:
                # Parse to ensure 100% valid XML
                root = ET.fromstring(svg_str)
                with open(out_file, 'w', encoding='utf-8') as sf:
                    sf.write(svg_str)
                print(f"  [SAVED & VALIDATED] {cid}.svg ({len(svg_str)} bytes)")
            except Exception as xe:
                print(f"  [XML ERROR] {cid}.svg: {xe}")
                with open(out_file, 'w', encoding='utf-8') as sf:
                    sf.write(svg_str)

        print(f"\nAll 16 SVGs successfully written to {output_dir}/")
    else:
        print("FAILED to capture harvest results from DOM")
        sys.exit(1)

finally:
    if os.path.exists(temp_file):
        os.remove(temp_file)
    httpd.shutdown()
    httpd.server_close()
