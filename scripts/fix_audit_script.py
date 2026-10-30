with open('scripts/run_full_site_audit.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = "if not any(part.startswith('.') or part in ('node_modules', 'scratch_inspect', 'raw', 'build library', 'Build Library') for part in p.parts)"
replacement = "if not any(part.startswith('.') or part in ('node_modules', 'scratch_inspect', 'raw', 'build library', 'Build Library', 'unintegrated_staging') for part in p.parts)"

if target in text:
    text = text.replace(target, replacement)
    with open('scripts/run_full_site_audit.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated run_full_site_audit.py exclusion list")
else:
    print("FAILED: Could not find target line")
