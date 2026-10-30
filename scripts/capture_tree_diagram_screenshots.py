# -*- coding: utf-8 -*-
import http.server
import socketserver
import threading
import subprocess
import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

PORT = 8790

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
temp_shot = os.path.join(brain_dir, 'screenshot_tree_temp.png')

# Inject test file with measuring script
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Test 1: Collapsed View
measure_script = '<script>window.addEventListener("load", function() { var r = document.getElementById("section-site-treemap").getBoundingClientRect(); document.title = "RECT:" + Math.round(r.top) + ":" + Math.round(r.bottom) + ":" + Math.round(r.height); });</script>'
with open('test_tree_view.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', measure_script + '</body>'))

# Test 2: Expanded View
measure_script_exp = '<script>window.addEventListener("load", function() { document.querySelectorAll(".vi-tree-branch").forEach(b => { b.classList.add("is-open"); b.querySelector(".vi-tree-children-container").hidden = false; }); var r = document.getElementById("section-site-treemap").getBoundingClientRect(); document.title = "RECT:" + Math.round(r.top) + ":" + Math.round(r.bottom) + ":" + Math.round(r.height); });</script>'
with open('test_tree_view_exp.html', 'w', encoding='utf-8') as f:
    f.write(html.replace('</body>', measure_script_exp + '</body>'))

try:
    # ── 1. Collapsed View Capture ───────────────────────────────────────────
    print("Measuring collapsed tree rect...")
    cmd_dom = [
        edge, '--headless=new', '--disable-gpu', '--window-size=1400,25000',
        '--virtual-time-budget=3000', '--dump-dom', f'http://localhost:{PORT}/test_tree_view.html'
    ]
    res = subprocess.run(cmd_dom, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    import re
    m = re.search(r'<title>RECT:(\d+):(\d+):(\d+)</title>', res.stdout.decode('utf-8', errors='replace'))
    if m:
        top, bottom, height = int(m.group(1)), int(m.group(2)), int(m.group(3))
        print(f"Collapsed Tree rect: top={top}, bottom={bottom}, height={height}")
        cmd_shot = [
            edge, '--headless=new', '--disable-gpu', '--window-size=1400,25000',
            '--virtual-time-budget=3000', f'--screenshot={temp_shot}', f'http://localhost:{PORT}/test_tree_view.html'
        ]
        subprocess.run(cmd_shot, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=35)
        if os.path.exists(temp_shot):
            with Image.open(temp_shot) as im:
                print(f"Loaded image size: {im.size}")
                crop_top = max(0, top - 20)
                crop_bottom = min(im.size[1], bottom + 30)
                print(f"Cropping from y={crop_top} to y={crop_bottom}")
                cropped = im.crop((0, crop_top, im.size[0], crop_bottom))
                cropped.save(collapsed_shot)
                print(f"Saved: {collapsed_shot} ({cropped.size}, {os.path.getsize(collapsed_shot)} bytes)")
            try: os.remove(temp_shot)
            except: pass

    # ── 2. Expanded View Capture ────────────────────────────────────────────
    print("Measuring expanded tree rect...")
    cmd_dom_exp = [
        edge, '--headless=new', '--disable-gpu', '--window-size=1400,32000',
        '--virtual-time-budget=3500', '--dump-dom', f'http://localhost:{PORT}/test_tree_view_exp.html'
    ]
    res_exp = subprocess.run(cmd_dom_exp, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=35)
    m_exp = re.search(r'<title>RECT:(\d+):(\d+):(\d+)</title>', res_exp.stdout.decode('utf-8', errors='replace'))
    if m_exp:
        top_e, bottom_e, height_e = int(m_exp.group(1)), int(m_exp.group(2)), int(m_exp.group(3))
        print(f"Expanded Tree rect: top={top_e}, bottom={bottom_e}, height={height_e}")
        cmd_shot_exp = [
            edge, '--headless=new', '--disable-gpu', '--window-size=1400,32000',
            '--virtual-time-budget=3500', f'--screenshot={temp_shot}', f'http://localhost:{PORT}/test_tree_view_exp.html'
        ]
        subprocess.run(cmd_shot_exp, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=40)
        if os.path.exists(temp_shot):
            with Image.open(temp_shot) as im:
                print(f"Loaded expanded image size: {im.size}")
                crop_top_e = max(0, top_e - 20)
                crop_bottom_e = min(im.size[1], bottom_e + 30)
                print(f"Cropping from y={crop_top_e} to y={crop_bottom_e}")
                cropped_e = im.crop((0, crop_top_e, im.size[0], crop_bottom_e))
                cropped_e.save(expanded_shot)
                print(f"Saved: {expanded_shot} ({cropped_e.size}, {os.path.getsize(expanded_shot)} bytes)")
            try: os.remove(temp_shot)
            except: pass

finally:
    httpd.shutdown()
    httpd.server_close()
    if os.path.exists('test_tree_view.html'):
        try: os.remove('test_tree_view.html')
        except: pass
    if os.path.exists('test_tree_view_exp.html'):
        try: os.remove('test_tree_view_exp.html')
        except: pass

print("Tree capture process complete.")
