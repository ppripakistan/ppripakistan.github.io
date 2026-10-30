# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

PORT = 8795

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
threading.Thread(target=httpd.serve_forever, daemon=True).start()

# Create a test page that clicks the button and logs what happens
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

test_js = '''
<script>
window.addEventListener("load", function() {
  var btn = document.getElementById("viTreeToggleAll");
  console.log("TEST: btn exists?", !!btn);
  if (btn) {
    btn.click();
    var openCount = document.querySelectorAll(".vi-tree-branch.is-open").length;
    var hiddenContainers = document.querySelectorAll(".vi-tree-children-container[hidden]").length;
    console.log("TEST: After expand click, openCount =", openCount, "hiddenContainers =", hiddenContainers);
    document.title = "EXPAND_RESULT:" + openCount + ":" + hiddenContainers;
  }
});
</script>
'''

with open('test_click.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', test_js + '</body>'))

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

try:
    cmd = [edge, '--headless=new', '--disable-gpu', '--virtual-time-budget=2000', '--dump-dom', f'http://localhost:{PORT}/test_click.html']
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
    dom = res.stdout.decode('utf-8', errors='replace')
    import re
    m = re.search(r'<title>(EXPAND_RESULT:\d+:\d+)</title>', dom)
    if m:
        print("Result:", m.group(1))
    else:
        print("Could not find EXPAND_RESULT")
finally:
    httpd.shutdown()
    httpd.server_close()
    if os.path.exists('test_click.html'):
        os.remove('test_click.html')
