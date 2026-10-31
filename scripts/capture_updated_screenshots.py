# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

PORT = 8769

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
server_thread = threading.Thread(target=httpd.serve_forever)
server_thread.daemon = True
server_thread.start()

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
brain_dir = r'C:\Users\HP\.gemini\antigravity\brain\145e2ba0-a7d5-4939-bfd4-974ac46ce013'

shots = [
    {
        'url': f'http://localhost:{PORT}/insights/',
        'out': os.path.join(brain_dir, 'screenshot_live_insights_denumbered_hero.png'),
        'w': 1400, 'h': 1100
    }
]

try:
    for s in shots:
        print(f"Capturing {s['url']} -> {os.path.basename(s['out'])}...")
        cmd = [
            edge,
            '--headless=new',
            '--disable-gpu',
            f"--window-size={s['w']},{s['h']}",
            '--virtual-time-budget=4000',
            f"--screenshot={s['out']}",
            s['url']
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=25)
        if os.path.exists(s['out']):
            print(f"  Captured: {os.path.basename(s['out'])} ({os.path.getsize(s['out'])} bytes)")
        else:
            print(f"  FAILED to capture {os.path.basename(s['out'])}")

finally:
    httpd.shutdown()
    httpd.server_close()

print("Screenshot capture complete.")
