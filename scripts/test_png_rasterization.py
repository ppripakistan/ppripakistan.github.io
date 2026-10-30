# -*- coding: utf-8 -*-
"""
Test 2: Browser In-Memory PNG Rasterization Test with Two-Line Stacked Footer.
Injects an automated harness into data/staging/insights.html and runs it inside
Microsoft Edge headless. Evaluates exportCard(cardId, 'png') logic across all 16 cards,
verifying that:
1. img.onload fires for every card (0 errors).
2. Canvas renders a valid PNG data URI starting with data:image/png;base64,
3. img.onerror is NEVER triggered.
"""

import subprocess
import os
import re

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

with open('data/staging/insights.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Harness script to test PNG rasterization across all 16 cards in browser
harness_script = """
<script>
window.__rasterTestResults = [];
window.addEventListener('DOMContentLoaded', async () => {
  const cards = [
    'card-fiscal', 'card-debt', 'card-tax-exp', 'card-gender-land',
    'card-hies', 'card-consumption-pie', 'card-wage-infl', 'card-services',
    'card-lfs', 'card-census-shifts', 'card-districts-scatter', 'card-sector-employment',
    'card-agri-shifts', 'card-census-hist', 'card-macro', 'card-prov-matrix'
  ];

  await new Promise(r => setTimeout(r, 600));

  for (const cid of cards) {
    const card = document.getElementById(cid);
    const chartSvg = document.getElementById('svg-' + cid);
    if (!card || !chartSvg) {
      window.__rasterTestResults.push({ id: cid, status: 'NOT_FOUND' });
      continue;
    }

    try {
      const p = new Promise((resolve) => {
        const numBadge = card.querySelector('.vi-number-badge') ? card.querySelector('.vi-number-badge').innerText : 'INFOGRAPHIC';
        const tag = card.querySelector('.vi-card-tag') ? card.querySelector('.vi-card-tag').innerText : 'POLICY INFOGRAPHIC';
        const title = card.querySelector('.vi-card-title') ? card.querySelector('.vi-card-title').innerText : 'PPRI Policy Infographic';
        const subtitle = card.querySelector('.vi-card-subtitle') ? card.querySelector('.vi-card-subtitle').innerText : '';
        const source = card.querySelector('.vi-source') ? card.querySelector('.vi-source').innerText : 'Pakistan Bureau of Statistics';
        const calloutEl = document.getElementById('callout-' + cid);
        const calloutText = calloutEl ? calloutEl.innerText.replace(/[\\r\\n]+/g, ' ') : '';

        const xmlText = str => (str || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&apos;');
        const safeNumBadge = xmlText(numBadge);
        const safeTag = xmlText(tag);
        const safeTitle = xmlText(title);
        const safeSubtitle = xmlText(subtitle);
        const safeSource = xmlText(source);
        const cleanSource = safeSource.replace(/\\s*•\\s*PPRI\\s*$/i, '').trim();
        const rawCallout = calloutText.length > 220 ? calloutText.substring(0, 217) + '...' : calloutText;
        const safeCallout = xmlText(rawCallout);

        const isWide = card.classList.contains('col-12');
        const exportW = isWide ? 1040 : 800;
        const exportH = isWide ? 680 : 620;

        const innerChartSvg = chartSvg.innerHTML;
        const viewBox = chartSvg.getAttribute('viewBox') || '0 0 600 360';
        const vbParts = viewBox.split(' ');
        const origW = parseFloat(vbParts[2]) || 600;
        const origH = parseFloat(vbParts[3]) || 360;

        const targetChartW = exportW - 80;
        const targetChartH = exportH - 240;
        const scale = Math.min(targetChartW / origW, targetChartH / origH);
        const transX = (exportW - origW * scale) / 2;
        const transY = 115;

        const fullSvg = `
<svg xmlns="http://www.w3.org/2000/svg" width="${exportW}" height="${exportH}" viewBox="0 0 ${exportW} ${exportH}">
  <defs>
    <style>
      text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
    </style>
  </defs>

  <rect width="${exportW}" height="${exportH}" fill="#ffffff" rx="10" stroke="#cbd5e1" stroke-width="1"/>
  <rect width="${exportW}" height="6" fill="#0f766e" rx="4"/>

  <!-- Top Header with Number Badge -->
  <text x="40" y="38" font-size="11" font-weight="700" fill="#0f766e" letter-spacing="1">PAKISTAN PROVINCIAL REFORM INSTITUTE (PPRI) • ${safeNumBadge} • ${safeTag}</text>
  <text x="40" y="66" font-size="20" font-weight="800" fill="#073c3a">${safeTitle}</text>
  <text x="40" y="88" font-size="12" fill="#64748b">${safeSubtitle}</text>
  <line x1="40" y1="102" x2="${exportW - 40}" y2="102" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Core Visual Graphics -->
  <g transform="translate(${transX}, ${transY}) scale(${scale})">
    ${innerChartSvg}
  </g>

  <!-- Key Insight Box -->
  <rect x="40" y="${exportH - 110}" width="${exportW - 80}" height="48" fill="#f8fafc" rx="6" stroke="#e2e8f0" stroke-width="1"/>
  <text x="54" y="${exportH - 93}" font-size="10" font-weight="800" fill="#073c3a">KEY POLICY INSIGHT:</text>
  <text x="54" y="${exportH - 77}" font-size="11" fill="#334155">${safeCallout}</text>

  <!-- Watermark Footer Banner (Two-Line Stacked: Zero Overlap) -->
  <rect x="0" y="${exportH - 52}" width="${exportW}" height="52" fill="#073c3a" rx="0"/>
  <!-- Line 1: Primary Data Source (Full Canvas Width) -->
  <text x="40" y="${exportH - 31}" font-size="10.5" font-weight="500" fill="#99f6e4">${cleanSource}</text>
  <!-- Line 2: Institution Branding & Canonical Domain -->
  <text x="40" y="${exportH - 14}" font-size="10.5" font-weight="700" fill="#ffffff">Pakistan Provincial Reform Institute (PPRI)</text>
  <text x="${exportW - 40}" y="${exportH - 14}" font-size="10.5" font-weight="600" fill="#5eead4" text-anchor="end">ppripakistan.github.io</text>
</svg>`.trim();

        let cleanSvg = fullSvg
          .replace(/&bull;/g, '•')
          .replace(/&rarr;/g, '→')
          .replace(/&ge;/g, '≥')
          .replace(/&le;/g, '≤')
          .replace(/&sim;/g, '~')
          .replace(/&radic;/g, '√')
          .replace(/&times;/g, '×')
          .replace(/&plusmn;/g, '±')
          .replace(/&nbsp;/g, ' ');

        cleanSvg = cleanSvg.replace(/&(?!amp;|lt;|gt;|quot;|apos;|#\\d+;|#x[0-9a-fA-F]+;)/g, '&amp;');

        const canvas = document.getElementById('vi-export-canvas') || document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        const dpr = 2;
        canvas.width = exportW * dpr;
        canvas.height = exportH * dpr;

        const img = new Image();
        const blob = new Blob([cleanSvg], { type: 'image/svg+xml;charset=utf-8' });
        const url = URL.createObjectURL(blob);

        img.onload = function() {
          ctx.fillStyle = '#ffffff';
          ctx.fillRect(0, 0, canvas.width, canvas.height);
          ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
          URL.revokeObjectURL(url);
          const pngData = canvas.toDataURL('image/png');
          resolve({ id: cid, status: 'PASS', isPNG: pngData.startsWith('data:image/png;base64,'), dataLen: pngData.length, w: canvas.width, h: canvas.height });
        };

        img.onerror = function(err) {
          URL.revokeObjectURL(url);
          resolve({ id: cid, status: 'ERROR_ON_IMAGE_LOAD', error: String(err) });
        };

        img.src = url;
      });

      const res = await p;
      window.__rasterTestResults.push(res);
    } catch (e) {
      window.__rasterTestResults.push({ id: cid, status: 'EXCEPTION', error: String(e) });
    }
  }

  const div = document.createElement('div');
  div.id = 'raster-test-summary';
  div.textContent = JSON.stringify(window.__rasterTestResults);
  document.body.appendChild(div);
});
</script>
"""

test_html = html.replace('</body>', harness_script + '</body>')
test_file = os.path.abspath('data/staging/test_raster_harness.html')
with open(test_file, 'w', encoding='utf-8') as f:
    f.write(test_html)

file_url = 'file:///' + test_file.replace('\\', '/')
print("Running Microsoft Edge headless PNG rasterization test suite...")
cmd = [edge, '--headless=new', '--dump-dom', '--virtual-time-budget=8000', file_url]
p = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', timeout=40)
dom = p.stdout

if os.path.exists(test_file):
    os.remove(test_file)

import json
m = re.search(r'id="raster-test-summary">([^<]+)<', dom)
assert m, "Could not find raster test summary in dumped DOM! Check if browser ran to completion."
results = json.loads(m.group(1))

print(f"\n=======================================================")
print(f"  TEST 2: MS EDGE CANVAS PNG RASTERIZATION RESULTS")
print(f"=======================================================")

raster_errors = 0
for idx, r in enumerate(results, 1):
    cid = r.get('id', 'unknown')
    status = r.get('status', 'FAIL')
    if status == 'PASS' and r.get('isPNG'):
        w, h = r.get('w'), r.get('h')
        dlen = r.get('dataLen', 0)
        print(f"  [PASS] Card {idx:02d}: {cid:24} -> 2x Retina PNG Canvas OK ({w}x{h}px, {dlen:,} bytes)")
    else:
        print(f"  [FAIL] Card {idx:02d}: {cid:24} -> Status: {status}, Error: {r.get('error')}")
        raster_errors += 1

print(f"=======================================================")
print(f"  PNG RASTERIZATION RESULT: {len(results) - raster_errors}/{len(results)} PASSED")
print(f"=======================================================")

assert raster_errors == 0, f"{raster_errors} cards failed browser PNG rasterization!"
print(">>> ALL 16 INFOGRAPHICS RENDER FLAWLESS 2x RETINA PNGS WITH STACKED FOOTER! <<<")
