# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

PORT = 8781

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
t = threading.Thread(target=httpd.serve_forever, daemon=True)
t.start()

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
brain_dir = r'C:\Users\HP\.gemini\antigravity\brain\145e2ba0-a7d5-4939-bfd4-974ac46ce013'

treemap_expanded_shot = os.path.join(brain_dir, 'screenshot_live_treemap_expanded.png')
temp_expanded = os.path.join(brain_dir, 'screenshot_expanded_temp.png')

# Inject script to open all details tiles for the screenshot
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

injected = html.replace('</body>', '<script>window.addEventListener("load", function() { document.querySelectorAll(".vi-treemap-tile").forEach(t => t.open = true); });</script></body>')
with open('test_expanded.html', 'w', encoding='utf-8') as f:
    f.write(injected)

try:
    print("Capturing expanded treemap...")
    cmd_expanded = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--window-size=1400,16000',
        '--virtual-time-budget=4000',
        f'--screenshot={temp_expanded}',
        f'http://localhost:{PORT}/test_expanded.html'
    ]
    subprocess.run(cmd_expanded, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)

    if os.path.exists(temp_expanded):
        with Image.open(temp_expanded) as im:
            h = im.size[1]
            crop_top = max(0, h - 5200)
            crop_bottom = min(h, h - 350)
            cropped = im.crop((0, crop_top, im.size[0], crop_bottom))
            cropped.save(treemap_expanded_shot)
            print(f"Cropped expanded treemap to {treemap_expanded_shot} (size: {cropped.size}, bytes: {os.path.getsize(treemap_expanded_shot)})")

finally:
    httpd.shutdown()
    httpd.server_close()
    if os.path.exists('test_expanded.html'):
        try: os.remove('test_expanded.html')
        except: pass
    if os.path.exists(temp_expanded):
        try: os.remove(temp_expanded)
        except: pass

print("Expanded treemap capture complete.")
