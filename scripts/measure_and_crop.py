# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import re
from PIL import Image

PORT = 8775

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

injected = html.replace('</body>', '<script>window.addEventListener("load", function() { var r = document.getElementById("section-visual-analytics").getBoundingClientRect(); document.title = "RECT:" + Math.round(r.top) + ":" + Math.round(r.bottom) + ":" + Math.round(r.height); });</script></body>')

with open('test_measure.html', 'w', encoding='utf-8') as f:
    f.write(injected)

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
t = threading.Thread(target=httpd.serve_forever, daemon=True)
t.start()

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
brain_dir = r'C:\Users\HP\.gemini\antigravity\brain\145e2ba0-a7d5-4939-bfd4-974ac46ce013'
temp_shot = os.path.join(brain_dir, 'screenshot_full_temp.png')
final_shot = os.path.join(brain_dir, 'screenshot_live_homepage_mosaic.png')

try:
    cmd_dom = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--window-size=1400,6000',
        '--virtual-time-budget=4000',
        '--dump-dom',
        f'http://localhost:{PORT}/test_measure.html'
    ]
    res = subprocess.run(cmd_dom, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
    stdout_text = res.stdout.decode('utf-8', errors='replace')
    m = re.search(r'<title>(RECT:(\d+):(\d+):(\d+))</title>', stdout_text)
    top, bottom, height = 0, 0, 0
    if m:
        parts = m.group(1).split(':')
        top = int(parts[1])
        bottom = int(parts[2])
        height = int(parts[3])
        print(f"Found rect: top={top}, bottom={bottom}, height={height}")
    else:
        print("Could not find RECT in title")

    # Now take screenshot of the full height
    cmd_shot = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--window-size=1400,13500',
        '--virtual-time-budget=5000',
        f'--screenshot={temp_shot}',
        f'http://localhost:{PORT}/'
    ]
    subprocess.run(cmd_shot, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)

    if os.path.exists(temp_shot) and top > 0:
        with Image.open(temp_shot) as im:
            print(f"Loaded full page image: {im.size}")
            crop_top = max(0, top - 30)
            crop_bottom = min(im.size[1], bottom + 40)
            print(f"Cropping from y={crop_top} to y={crop_bottom}...")
            cropped = im.crop((0, crop_top, im.size[0], crop_bottom))
            cropped.save(final_shot)
            print(f"Successfully cropped mosaic grid to {final_shot} (size: {cropped.size}, bytes: {os.path.getsize(final_shot)})")
    else:
        print("Failed to crop or take screenshot")

finally:
    httpd.shutdown()
    httpd.server_close()
    if os.path.exists('test_measure.html'):
        os.remove('test_measure.html')
    if os.path.exists(temp_shot):
        os.remove(temp_shot)
