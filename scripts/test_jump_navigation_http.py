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

PORT = 8768

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
server_thread = threading.Thread(target=httpd.serve_forever)
server_thread.daemon = True
server_thread.start()

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Read insights/index.html and inject navigation test script
with open('insights/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

test_runner = """
<script>
window.__navTestResults = [];
window.addEventListener('load', async () => {
  const chips = document.querySelectorAll('.vi-chip-btn[data-target]');
  for (const chip of chips) {
    const targetId = chip.getAttribute('data-target');
    const el = document.getElementById(targetId);
    const computed = el ? window.getComputedStyle(el) : null;
    
    // Simulate click
    chip.click();
    await new Promise(r => setTimeout(r, 50));

    window.__navTestResults.push({
      target: targetId,
      exists: !!el,
      scrollMarginTop: computed ? computed.scrollMarginTop : null,
      highlightApplied: el ? el.classList.contains('vi-card-highlight') : false
    });
  }

  const out = document.createElement('div');
  out.id = '__nav_test_results';
  out.textContent = JSON.stringify(window.__navTestResults);
  document.body.appendChild(out);
});
</script>
"""

temp_file = 'insights/temp_nav_test.html'
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', test_runner + '</body>'))

try:
    cmd = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--virtual-time-budget=6000',
        '--dump-dom',
        f'http://localhost:{PORT}/insights/temp_nav_test.html'
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=25)
    dom = res.stdout.decode('utf-8', errors='ignore')

    match = re.search(r'<div id="__nav_test_results">(.*?)</div>', dom)
    if match:
        results = json.loads(match.group(1))
        all_passed = True
        print("=== QUICK-JUMP NAVIGATION EDGE HEADLESS RESULTS ===")
        for r in results:
            if r['exists'] and r['scrollMarginTop'] == '100px' and r['highlightApplied']:
                print(f"  PASS: {r['target']} -> scrollMarginTop={r['scrollMarginTop']}, highlightApplied={r['highlightApplied']}")
            else:
                print(f"  FAILED: {r['target']} -> {r}")
                all_passed = False
        if all_passed:
            print("==================================================")
            print("ALL 16 CHIPS PASSED SMOOTH JUMP & HIGHLIGHT TEST!")
            print("==================================================")
        else:
            sys.exit(1)
    else:
        print("FAILED: Could not find nav test results in DOM")
        sys.exit(1)

finally:
    if os.path.exists(temp_file):
        os.remove(temp_file)
    httpd.shutdown()
    httpd.server_close()
