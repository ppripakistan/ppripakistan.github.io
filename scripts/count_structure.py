with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
footers = [m.start() for m in re.finditer('<footer', text)]
mains = [m.start() for m in re.finditer('<main', text)]
end_mains = [m.start() for m in re.finditer('</main>', text)]
print(f"Footers found at: {footers}")
print(f"Mains found at: {mains}")
print(f"End mains found at: {end_mains}")
