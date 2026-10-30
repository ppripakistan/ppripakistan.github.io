import re

with open("data/staging/insights.html", "r", encoding="utf-8") as f:
    text = f.read()

cards = re.findall(r'id="(card-[^"]+)"', text)
print("Existing card IDs found:", len(cards), cards)

# Also check header/nav links
nav_links = re.findall(r'href="#(card-[^"]+)"', text)
print("Nav links found:", len(nav_links), nav_links)
