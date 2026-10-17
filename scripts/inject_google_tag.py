#!/usr/bin/env python3
"""
scripts/inject_google_tag.py
Injects the Google tag (gtag.js) snippet immediately following the <head> tag
across all HTML pages in the repository.
"""

import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

GTAG_SNIPPET = """    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-9C2NZV6BYF"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-9C2NZV6BYF');
    </script>"""

IGNORED_DIRS = {'.git', '.vscode', 'node_modules', '.gemini'}

def run_injection():
    html_files = [
        p for p in ROOT_DIR.rglob('*.html')
        if not any(ign in p.parts for ign in IGNORED_DIRS)
    ]

    print(f"Discovered {len(html_files)} HTML pages.")
    updated_count = 0
    already_present_count = 0
    missing_head_count = 0

    for path in sorted(html_files):
        content = path.read_text(encoding='utf-8')

        # Check if Google tag is already present in this file
        if 'googletagmanager.com/gtag/js?id=G-9C2NZV6BYF' in content:
            already_present_count += 1
            continue

        if '<head>' in content:
            new_content = content.replace('<head>', f'<head>\n{GTAG_SNIPPET}', 1)
            path.write_text(new_content, encoding='utf-8')
            updated_count += 1
        elif '<head ' in content:
            # In case attributes exist on head tag
            import re
            m = re.search(r'<head[^>]*>', content)
            if m:
                target = m.group(0)
                new_content = content.replace(target, f'{target}\n{GTAG_SNIPPET}', 1)
                path.write_text(new_content, encoding='utf-8')
                updated_count += 1
            else:
                missing_head_count += 1
                print(f"Warning: Could not match head in {path.relative_to(ROOT_DIR)}")
        else:
            missing_head_count += 1
            print(f"Warning: No <head> found in {path.relative_to(ROOT_DIR)}")

    print(f"\nInjection Summary:")
    print(f"  Total HTML files scanned: {len(html_files)}")
    print(f"  Files updated:            {updated_count}")
    print(f"  Files already had gtag:   {already_present_count}")
    print(f"  Files missing <head>:     {missing_head_count}")

if __name__ == '__main__':
    run_injection()
