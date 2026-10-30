# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

PORT = 8792

# Extract the tree section from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
tree_match = re.search(r'(<section class="vi-tree-section".*?</section>)', html, re.DOTALL)
if not tree_match:
    print("Could not find vi-tree-section")
    sys.exit(1)

tree_html = tree_match.group(1)

# Template with same stylesheets as index.html
template = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" href="/assets/css/style.css" />
  <link rel="stylesheet" href="/assets/css/homepage.css" />
  <link rel="stylesheet" href="/assets/css/visual-insights.css" />
  <style>
    body {{ margin: 0; padding: 2rem 0; background: #f8fafc; font-family: system-ui, -apple-system, sans-serif; }}
  </style>
</head>
<body>
  {tree_html}
  <script>
    (function() {{
      var toggleAllBtn = document.getElementById('viTreeToggleAll');
      var branchCards = document.querySelectorAll('.vi-tree-node-card');

      function setBranchState(branch, open) {{
        var btn = branch.querySelector('.vi-tree-node-card');
        var container = branch.querySelector('.vi-tree-children-container');
        var indicator = branch.querySelector('.node-toggle-state');
        if (!btn || !container) return;

        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
        container.hidden = !open;
        if (open) {{
          branch.classList.add('is-open');
          if (indicator) indicator.textContent = '−';
        }} else {{
          branch.classList.remove('is-open');
          if (indicator) indicator.textContent = '+';
        }}
      }}

      branchCards.forEach(function(card) {{
        card.addEventListener('click', function(e) {{
          e.preventDefault();
          var branch = card.closest('.vi-tree-branch');
          if (!branch) return;
          var isExpanded = card.getAttribute('aria-expanded') === 'true';
          setBranchState(branch, !isExpanded);
        }});
      }});
    }})();
  </script>
</body>
</html>'''

with open('test_tree_standalone.html', 'w', encoding='utf-8') as f:
    f.write(template)

# Also create expanded version
template_exp = template.replace('</body>', '<script>document.querySelectorAll(".vi-tree-branch").forEach(b => { b.classList.add("is-open"); b.querySelector(".vi-tree-children-container").hidden = false; b.querySelector(".node-toggle-state").textContent = "−"; });</script></body>')
with open('test_tree_standalone_exp.html', 'w', encoding='utf-8') as f:
    f.write(template_exp)

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
t = threading.Thread(target=httpd.serve_forever, daemon=True)
t.start()

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
brain_dir = r'C:\Users\HP\.gemini\antigravity\brain\145e2ba0-a7d5-4939-bfd4-974ac46ce013'

collapsed_shot = os.path.join(brain_dir, 'screenshot_live_tree_diagram_collapsed.png')
expanded_shot = os.path.join(brain_dir, 'screenshot_live_tree_diagram_expanded.png')

try:
    print("Capturing collapsed standalone tree...")
    cmd_col = [
        edge, '--headless=new', '--disable-gpu', '--window-size=1400,900',
        '--virtual-time-budget=2000', f'--screenshot={collapsed_shot}',
        f'http://localhost:{PORT}/test_tree_standalone.html'
    ]
    subprocess.run(cmd_col, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
    if os.path.exists(collapsed_shot):
        print(f"Captured collapsed tree: {collapsed_shot} ({os.path.getsize(collapsed_shot)} bytes)")

    print("Capturing expanded standalone tree...")
    cmd_exp = [
        edge, '--headless=new', '--disable-gpu', '--window-size=1400,1650',
        '--virtual-time-budget=2000', f'--screenshot={expanded_shot}',
        f'http://localhost:{PORT}/test_tree_standalone_exp.html'
    ]
    subprocess.run(cmd_exp, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
    if os.path.exists(expanded_shot):
        print(f"Captured expanded tree: {expanded_shot} ({os.path.getsize(expanded_shot)} bytes)")

finally:
    httpd.shutdown()
    httpd.server_close()
    if os.path.exists('test_tree_standalone.html'):
        try: os.remove('test_tree_standalone.html')
        except: pass
    if os.path.exists('test_tree_standalone_exp.html'):
        try: os.remove('test_tree_standalone_exp.html')
        except: pass

print("Direct tree capture complete.")
