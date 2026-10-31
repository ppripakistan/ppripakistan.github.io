# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

PORT = 8780

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
t = threading.Thread(target=httpd.serve_forever, daemon=True)
t.start()

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
brain_dir = r'C:\Users\HP\.gemini\antigravity\brain\145e2ba0-a7d5-4939-bfd4-974ac46ce013'

hero_shot = os.path.join(brain_dir, 'screenshot_live_hero_cleaned.png')
treemap_shot = os.path.join(brain_dir, 'screenshot_live_treemap_matrix.png')
temp_full = os.path.join(brain_dir, 'screenshot_full_page_temp.png')

try:
    print("Capturing cleaned hero...")
    cmd_hero = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--window-size=1400,900',
        '--virtual-time-budget=3000',
        f'--screenshot={hero_shot}',
        f'http://localhost:{PORT}/'
    ]
    subprocess.run(cmd_hero, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=20)
    if os.path.exists(hero_shot):
        print(f"Captured: {hero_shot} ({os.path.getsize(hero_shot)} bytes)")

    # Full page screenshot to crop treemap section
    print("Capturing full page to crop treemap section...")
    cmd_full = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--window-size=1400,12000',
        '--virtual-time-budget=4000',
        f'--screenshot={temp_full}',
        f'http://localhost:{PORT}/'
    ]
    subprocess.run(cmd_full, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)

    # Measure position of section-site-treemap
    # We can measure by querying DOM or finding footer
    # Let's inspect temp_full
    if os.path.exists(temp_full):
        with Image.open(temp_full) as im:
            print(f"Full page size: {im.size}")
            # Treemap is directly above the footer.
            # In index.html, footer starts ~1000px before bottom.
            # Let's crop the bottom 2400px excluding the last 400px (footer)
            h = im.size[1]
            crop_top = max(0, h - 2300)
            crop_bottom = min(h, h - 350)
            cropped = im.crop((0, crop_top, im.size[0], crop_bottom))
            cropped.save(treemap_shot)
            print(f"Cropped treemap section to {treemap_shot} (size: {cropped.size}, bytes: {os.path.getsize(treemap_shot)})")

finally:
    httpd.shutdown()
    httpd.server_close()
    if os.path.exists(temp_full):
        try: os.remove(temp_full)
        except: pass

print("Screenshots captured successfully.")
