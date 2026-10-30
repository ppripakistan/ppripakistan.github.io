# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

PORT = 8796

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
threading.Thread(target=httpd.serve_forever, daemon=True).start()

# Create a test script that exercises the interactions inside the live browser
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

test_script = '''
<script>
window.addEventListener("load", function() {
  var log = [];
  
  // Test 1: Initial state
  var initialOpen = document.querySelectorAll('.vi-tree-branch.is-open').length;
  var initialHidden = document.querySelectorAll('.vi-tree-children-container[hidden]').length;
  log.push("T1_INIT:" + initialOpen + ":" + initialHidden);

  // Test 2: Click Expand All
  var expandBtn = document.getElementById('viTreeExpandAll');
  if (expandBtn) expandBtn.click();
  var expOpen = document.querySelectorAll('.vi-tree-branch.is-open').length;
  var expHidden = document.querySelectorAll('.vi-tree-children-container[hidden]').length;
  log.push("T2_EXPAND:" + expOpen + ":" + expHidden);

  // Test 3: Click Collapse All
  var collapseBtn = document.getElementById('viTreeCollapseAll');
  if (collapseBtn) collapseBtn.click();
  var colOpen = document.querySelectorAll('.vi-tree-branch.is-open').length;
  var colHidden = document.querySelectorAll('.vi-tree-children-container[hidden]').length;
  log.push("T3_COLLAPSE:" + colOpen + ":" + colHidden);

  // Test 4: Click Pillar 2 directly
  var pillar2Card = document.querySelector('.vi-tree-branch[data-pillar="data"] .vi-tree-node-card');
  if (pillar2Card) pillar2Card.click();
  var p2Open = document.querySelectorAll('.vi-tree-branch.is-open').length;
  var p2BranchOpen = document.querySelector('.vi-tree-branch[data-pillar="data"]').classList.contains('is-open');
  log.push("T4_PILLAR2:" + p2Open + ":" + p2BranchOpen);

  // Test 5: Check alignment of Pillar 2 card center vs its incoming stem center
  var p2Branch = document.querySelector('.vi-tree-branch[data-pillar="data"]');
  var p2Stem = p2Branch.querySelector('.vi-tree-branch-stem-in');
  var rCard = p2Branch.querySelector('.vi-tree-node-card').getBoundingClientRect();
  var rStem = p2Stem.getBoundingClientRect();
  var cardCenter = rCard.left + rCard.width / 2;
  var stemCenter = rStem.left + rStem.width / 2;
  var drift = Math.abs(cardCenter - stemCenter);
  log.push("T5_DRIFT:" + drift.toFixed(2));

  document.title = "TEST_RUN|" + log.join("|");
});
</script>
'''

with open('test_tree_interaction.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', test_script + '</body>'))

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

try:
    cmd = [
        edge, '--headless=new', '--disable-gpu', '--window-size=1400,900',
        '--virtual-time-budget=3000', '--dump-dom', f'http://localhost:{PORT}/test_tree_interaction.html'
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=25)
    dom = res.stdout.decode('utf-8', errors='replace')
    import re
    m = re.search(r'<title>(TEST_RUN\|[^<]+)</title>', dom)
    if m:
        results = m.group(1).split('|')[1:]
        print("=======================================================")
        print("  LIVE BROWSER INTERACTION & ALIGNMENT TEST RESULTS")
        print("=======================================================")
        for r in results:
            print(" ", r)
        print("=======================================================")
        
        # Verify assertions
        # T1_INIT:0:6
        # T2_EXPAND:6:0
        # T3_COLLAPSE:0:6
        # T4_PILLAR2:1:true
        # T5_DRIFT:0.00
        assert "T1_INIT:0:6" in results, "Test 1 failed: initial state not 0 open, 6 hidden"
        assert "T2_EXPAND:6:0" in results, "Test 2 failed: Expand All did not open all 6"
        assert "T3_COLLAPSE:0:6" in results, "Test 3 failed: Collapse All did not close all 6"
        assert "T4_PILLAR2:1:true" in results, "Test 4 failed: Pillar 2 click did not open Pillar 2"
        drift_val = float([x.split(':')[1] for x in results if 'T5_DRIFT' in x][0])
        assert drift_val < 0.5, f"Test 5 failed: Pillar 2 stem drift is {drift_val}px (expected < 0.5px)"
        print("ALL 5 AUTOMATED INTERACTION & ALIGNMENT TESTS PASSED 100%!")
    else:
        print("Could not find TEST_RUN title. Check console logs.")
finally:
    httpd.shutdown()
    httpd.server_close()
    if os.path.exists('test_tree_interaction.html'):
        os.remove('test_tree_interaction.html')
