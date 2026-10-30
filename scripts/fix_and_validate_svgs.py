import os
import html
import xml.etree.ElementTree as ET

output_dir = 'assets/images/insights'
files = [f for f in os.listdir(output_dir) if f.endswith('.svg')]

all_valid = True
print(f"Validating and unescaping {len(files)} SVGs in {output_dir}/...")

for f in sorted(files):
    filepath = os.path.join(output_dir, f)
    with open(filepath, 'r', encoding='utf-8') as sf:
        raw = sf.read()
    
    # Unescape HTML entities from DOM serialization if present
    if raw.startswith('&lt;svg') or '&lt;' in raw[:100]:
        cleaned = html.unescape(raw)
    else:
        cleaned = raw

    # Validate strict XML 1.0
    try:
        root = ET.fromstring(cleaned)
        with open(filepath, 'w', encoding='utf-8') as sf:
            sf.write(cleaned)
        w = root.attrib.get('width', 'auto')
        h = root.attrib.get('height', 'auto')
        vb = root.attrib.get('viewBox', 'none')
        print(f"  [PASS] {f:<26} -> Valid XML 1.0 ({len(cleaned):>6} bytes, w={w}, h={h}, viewBox={vb})")
    except Exception as e:
        print(f"  [FAIL] {f:<26} -> XML Error: {e}")
        all_valid = False

if all_valid:
    print(f"\nALL {len(files)} SVGS ARE 100% VALID XML 1.0 VECTOR FILES!")
else:
    print("\nSOME SVGS FAILED VALIDATION!")
    exit(1)
