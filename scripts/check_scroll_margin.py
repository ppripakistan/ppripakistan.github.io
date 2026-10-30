with open('assets/css/visual-insights.css', 'r', encoding='utf-8') as f:
    css = f.read()

print("scroll-margin in visual-insights.css?", 'scroll-margin' in css)
print("scroll-padding in visual-insights.css?", 'scroll-padding' in css)
print("scroll-behavior in visual-insights.css?", 'scroll-behavior' in css)
