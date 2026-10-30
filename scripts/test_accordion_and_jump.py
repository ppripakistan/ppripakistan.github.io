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

PORT = 8770

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
server_thread = threading.Thread(target=httpd.serve_forever)
server_thread.daemon = True
server_thread.start()

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Read insights/index.html and inject comprehensive UI verification runner
with open('insights/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

test_runner = """
<script>
window.__uiTestResults = {};
window.addEventListener('load', async () => {
  const res = {};

  // 1. Check badge removed
  res.badgeExists = !!document.querySelector('.vi-badge-top');

  // 2. Check export footer note removed
  res.footerNoteExists = !!document.querySelector('.vi-seo-footer-note');

  // 3. Check filter pills removed
  res.filterPillsExists = !!document.querySelector('.vi-filter-pills');

  // 4. Check breadcrumb spacing and current page color
  const bcNav = document.querySelector('.breadcrumb-nav');
  const bcCurrent = document.querySelector('.breadcrumb-inner [aria-current="page"]');
  res.breadcrumb = {
    exists: !!bcNav,
    paddingTop: bcNav ? window.getComputedStyle(bcNav).paddingTop : null,
    currentTagColor: bcCurrent ? window.getComputedStyle(bcCurrent).color : null,
    currentTagBg: bcCurrent ? window.getComputedStyle(bcCurrent).backgroundColor : null
  };

  // 5. Check 4 accordions
  const accordions = document.querySelectorAll('.vi-seo-accordion');
  res.accordionCount = accordions.length;
  res.accordionsClosedByDefault = Array.from(accordions).every(a => !a.open);
  
  // Test click toggle on first accordion
  if (accordions.length > 0) {
    const summary = accordions[0].querySelector('summary');
    if (summary) {
      summary.click();
      await new Promise(r => setTimeout(r, 60));
      res.accordionOpensOnClick = accordions[0].open;
    }
  }

  // 6. Check 4 separated domain jump cards
  const domainCards = document.querySelectorAll('.vi-jump-domain-card');
  res.domainCardCount = domainCards.length;

  const chips = document.querySelectorAll('.vi-chip-btn[data-target]');
  res.totalChipCount = chips.length;

  // Test chip click smooth scroll and scrollMarginTop
  const firstChip = chips[0];
  if (firstChip) {
    const targetId = firstChip.getAttribute('data-target');
    const targetEl = document.getElementById(targetId);
    firstChip.click();
    await new Promise(r => setTimeout(r, 60));
    res.targetChip = {
      targetId: targetId,
      scrollMarginTop: targetEl ? window.getComputedStyle(targetEl).scrollMarginTop : null,
      highlighted: targetEl ? targetEl.classList.contains('vi-card-highlight') : false
    };
  }

  window.__uiTestResults = res;

  const out = document.createElement('div');
  out.id = '__ui_test_results';
  out.textContent = JSON.stringify(res);
  document.body.appendChild(out);
});
</script>
"""

temp_file = 'insights/temp_ui_verify.html'
with open(temp_file, 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', test_runner + '</body>'))

try:
    cmd = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--virtual-time-budget=6000',
        '--dump-dom',
        f'http://localhost:{PORT}/insights/temp_ui_verify.html'
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=25)
    dom = res.stdout.decode('utf-8', errors='ignore')

    match = re.search(r'<div id="__ui_test_results">(.*?)</div>', dom)
    if match:
        data = json.loads(match.group(1))
        print("=== UI VERIFICATION TEST RESULTS ===")
        print(f"  Top Badge Removed: {not data['badgeExists']}")
        print(f"  Footer Note Removed: {not data['footerNoteExists']}")
        print(f"  Filter Pills Removed: {not data['filterPillsExists']}")
        print(f"  Breadcrumb Padding Top: {data['breadcrumb']['paddingTop']}")
        print(f"  Breadcrumb Active Color: {data['breadcrumb']['currentTagColor']}")
        print(f"  Breadcrumb Active Background: {data['breadcrumb']['currentTagBg']}")
        print(f"  Accordions Count: {data['accordionCount']} (Closed by default: {data['accordionsClosedByDefault']}, Opens on click: {data.get('accordionOpensOnClick')})")
        print(f"  Separated Domain Jump Cards: {data['domainCardCount']}")
        print(f"  Total Quick-Jump Chips: {data['totalChipCount']}")
        print(f"  Chip Navigation Test: {data.get('targetChip')}")

        all_ok = (
            not data['badgeExists'] and
            not data['footerNoteExists'] and
            not data['filterPillsExists'] and
            data['accordionCount'] == 4 and
            data['accordionsClosedByDefault'] and
            data.get('accordionOpensOnClick') and
            data['domainCardCount'] == 4 and
            data['totalChipCount'] == 16 and
            data.get('targetChip', {}).get('scrollMarginTop') == '100px'
        )
        if all_ok:
            print("\n=======================================================")
            print("ALL REFINEMENT CRITERIA PASSED 100% IN HEADLESS BROWSER!")
            print("=======================================================")
        else:
            print("\nCRITERIA FAILED!")
            sys.exit(1)
    else:
        print("FAILED to find test results in DOM")
        sys.exit(1)

finally:
    if os.path.exists(temp_file):
        os.remove(temp_file)
    httpd.shutdown()
    httpd.server_close()
