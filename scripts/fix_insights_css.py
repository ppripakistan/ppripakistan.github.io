with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

bad_css = """    <!-- Core Stylesheets -->
    <link rel="stylesheet" href="/assets/css/variables.css" />
    <link rel="stylesheet" href="/assets/css/base.css" />
    <link rel="stylesheet" href="/assets/css/components.css" />
    <link rel="stylesheet" href="/assets/css/layout.css" />
    <link rel="stylesheet" href="/assets/css/utilities.css" />
    <link rel="stylesheet" href="/assets/css/visual-insights.css" />"""

good_head = """    <link rel="icon" type="image/png" href="/favicon.png?v=2" />
    <link rel="icon" href="/favicon.ico" sizes="48x48" />
    <link rel="icon" href="/assets/images/brand/favicon.svg" type="image/svg+xml" />
    <link rel="icon" type="image/png" sizes="32x32" href="/assets/images/brand/favicon-32x32.png" />
    <link rel="icon" type="image/png" sizes="16x16" href="/assets/images/brand/favicon-16x16.png" />
    <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
    <link rel="manifest" href="/site.webmanifest" />
    <meta name="theme-color" content="#073c3a" />

    <!-- Core Stylesheets -->
    <link rel="stylesheet" href="/assets/css/style.css" />
    <link rel="stylesheet" href="/assets/css/responsive.css" />
    <link rel="stylesheet" href="/assets/css/visual-insights.css" />"""

if bad_css in text:
    text = text.replace(bad_css, good_head)
    with open('insights/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("SUCCESS: Updated stylesheets in insights/index.html")
else:
    # Try normalized newlines
    bad_css_norm = bad_css.replace('\r\n', '\n')
    text_norm = text.replace('\r\n', '\n')
    if bad_css_norm in text_norm:
        text_norm = text_norm.replace(bad_css_norm, good_head.replace('\r\n', '\n'))
        with open('insights/index.html', 'w', encoding='utf-8') as f:
            f.write(text_norm)
        print("SUCCESS: Updated stylesheets in insights/index.html (normalized)")
    else:
        print("FAILED: Could not find bad_css block")
