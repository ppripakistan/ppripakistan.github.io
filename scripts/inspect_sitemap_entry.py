with open('sitemap.xml', 'r', encoding='utf-8') as f:
    text = f.read()

import re
urls = re.findall(r'<url>.*?</url>', text, re.DOTALL)
print(f"Total URLs in sitemap: {len(urls)}")
print("First URL entry:\n", urls[0])
