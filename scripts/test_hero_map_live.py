# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

PORT = 8788

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

httpd = socketserver.TCPServer(("", PORT), QuietHandler)
t = threading.Thread(target=httpd.serve_forever, daemon=True)
t.start()

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
brain_dir = r'C:\Users\HP\.gemini\antigravity\brain\145e2ba0-a7d5-4939-bfd4-974ac46ce013'
hero_shot = os.path.join(brain_dir, 'screenshot_live_hero_map_restored.png')

print("=======================================================")
print("  TESTING HERO MAP RESTORATION IN MS EDGE HEADLESS")
print("=======================================================")

try:
    # 1. Dump DOM after 3.5s virtual time
    cmd_dom = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--window-size=1400,900',
        '--virtual-time-budget=4000',
        '--dump-dom',
        f'http://localhost:{PORT}/'
    ]
    res = subprocess.run(cmd_dom, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=25)
    dom = res.stdout.decode('utf-8', errors='replace')

    # Assertions
    leaflet_present = 'leaflet-container' in dom
    paths_count = dom.count('leaflet-interactive')
    loader_hidden = 'is-loaded' in dom

    print(f"  Leaflet Container initialized: {leaflet_present}")
    print(f"  Leaflet Interactive Vector Paths rendered: {paths_count}")
    print(f"  Hero Map Loader hidden (.is-loaded): {loader_hidden}")

    if leaflet_present and paths_count > 0 and loader_hidden:
        print("  [PASS] Pakistan map vectors successfully loaded, rendered, and loader dismissed!")
    else:
        print("  [FAIL] Map vectors not found or loader not dismissed!")

    # 2. Capture screenshot of the hero
    cmd_shot = [
        edge,
        '--headless=new',
        '--disable-gpu',
        '--window-size=1400,900',
        '--virtual-time-budget=4000',
        f'--screenshot={hero_shot}',
        f'http://localhost:{PORT}/'
    ]
    subprocess.run(cmd_shot, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=25)
    if os.path.exists(hero_shot):
        print(f"  [PASS] Captured live screenshot: {hero_shot} ({os.path.getsize(hero_shot)} bytes)")
    else:
        print(f"  [FAIL] Screenshot not generated")

finally:
    httpd.shutdown()
    httpd.server_close()

print("=======================================================")
