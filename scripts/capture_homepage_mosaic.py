# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import sys

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
brain_dir = r'C:\Users\HP\.gemini\antigravity\brain\145e2ba0-a7d5-4939-bfd4-974ac46ce013'
out_path = os.path.join(brain_dir, 'screenshot_live_homepage_mosaic.png')

try:
    print(f"Capturing homepage mosaic to {out_path}...")
    cmd = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--window-size=1400,1200',
        '--virtual-time-budget=4000',
        f"--screenshot={out_path}",
        f"http://localhost:{PORT}/#section-visual-analytics"
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=25)
    if os.path.exists(out_path):
        print(f"Captured: {out_path} ({os.path.getsize(out_path)} bytes)")
    else:
        print(f"Failed to capture screenshot")
finally:
    httpd.shutdown()
    httpd.server_close()
