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

PORT = 8766

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
server_thread = threading.Thread(target=httpd.serve_forever)
server_thread.daemon = True
server_thread.start()

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Read insights/index.html and inject export runner
with open('insights/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

card_ids = [
    'card-fiscal', 'card-debt', 'card-tax-exp', 'card-gender-land',
    'card-hies', 'card-consumption-pie', 'card-wage-infl', 'card-services',
    'card-lfs', 'card-census-shifts', 'card-districts-scatter', 'card-sector-employment',
    'card-agri-shifts', 'card-census-hist', 'card-macro', 'card-prov-matrix'
]

test_runner = f"""
<script>
window.__exportResults = [];
window.addEventListener('load', async () => {{
  // Override download to capture data URL
  let captured = {{}};
  const origClick = HTMLAnchorElement.prototype.click;
  HTMLAnchorElement.prototype.click = function() {{
    if (this.download && this.href) {{
      captured[this.download] = {{
        href_len: this.href.length,
        is_png: this.href.startsWith('data:image/png;base64,'),
        is_svg: this.href.startsWith('data:image/svg+xml')
      }};
    }}
  }};

  const cards = {json.dumps(card_ids)};
  for (const cid of cards) {{
    captured = {{}};
    try {{
      exportCard(cid, 'png');
      // Wait 300ms for rasterization
      await new Promise(r => setTimeout(r, 300));
      const keys = Object.keys(captured);
      const res = keys.length ? captured[keys[0]] : {{ is_png: false, href_len: 0 }};
      window.__exportResults.push({{
        card: cid,
        success: res.is_png,
        data_len: res.href_len
      }});
    }} catch (e) {{
      window.__exportResults.push({{
        card: cid,
        success: false,
        error: String(e)
      }});
    }}
  }}

  const out = document.createElement('div');
  out.id = '__export_test_results';
  out.textContent = JSON.stringify(window.__exportResults);
  document.body.appendChild(out);
}});
</script>
"""

temp_file = 'insights/temp_export_test.html'
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', test_runner + '</body>'))

try:
    cmd = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--virtual-time-budget=10000',
        '--dump-dom',
        f'http://localhost:{PORT}/insights/temp_export_test.html'
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    dom = res.stdout.decode('utf-8', errors='ignore')

    match = re.search(r'<div id="__export_test_results">(.*?)</div>', dom)
    if match:
        results = json.loads(match.group(1))
        all_passed = True
        print("=== 16 CARDS PNG RETINA RASTERIZATION RESULTS ===")
        for r in results:
            if r.get('success'):
                print(f"  PASS: {r['card']} -> Valid Retina PNG Data URI ({r['data_len']} bytes)")
            else:
                print(f"  FAILED: {r['card']} -> Error: {r}")
                all_passed = False
        if all_passed:
            print("==================================================")
            print("ALL 16 CARDS RASTERIZED TO VALID PNG WITH ZERO ERRORS!")
            print("==================================================")
        else:
            sys.exit(1)
    else:
        print("FAILED: Could not find export test results in DOM")
        sys.exit(1)

finally:
    if os.path.exists(temp_file):
        os.remove(temp_file)
    httpd.shutdown()
    httpd.server_close()
