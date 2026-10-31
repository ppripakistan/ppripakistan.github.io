import os

with open('insights/index.html', 'r', encoding='utf-8') as f:
    insights_html = f.read()

def get_card(cid):
    start = insights_html.find(f'id="{cid}"')
    if start == -1:
        raise ValueError(f"Card {cid} not found in insights/index.html")
    div_start = insights_html.rfind('<div class="vi-card', 0, start)
    footer_pos = insights_html.find('class="vi-card-footer"', div_start)
    actions_pos = insights_html.find('class="vi-actions"', footer_pos)
    end_div = insights_html.find('</div>\n        </div>', actions_pos)
    if end_div == -1:
        end_div = insights_html.find('</div>\r\n        </div>', actions_pos)
    return insights_html[div_start:end_div + len('</div>\n        </div>')].strip()

# Target observatory configurations
configs = [
    {
        'path': 'data/public-finance/index.html',
        'title': 'Empirical Infographics &amp; Fiscal Solvency Analytics',
        'desc': 'Interactive vector charts analyzing federal budgetary outlays, sovereign debt servicing burdens, tax concession losses, and cross-provincial resource allocations.',
        'cards': ['card-fiscal', 'card-debt', 'card-tax-exp', 'card-prov-matrix']
    },
    {
        'path': 'data/economy/index.html',
        'title': 'Economic Dynamics &amp; Structural Trajectory Visual Analytics',
        'desc': 'Interactive vector visualizations exploring purchasing power erosion, sectoral employment shifts, agricultural landholding fragmentation, and 35 years of macroeconomic regime cycles.',
        'cards': ['card-wage-infl', 'card-sector-employment', 'card-agri-shifts', 'card-macro']
    },
    {
        'path': 'data/population/index.html',
        'title': 'Demographic Architecture &amp; Urbanization Visual Analytics',
        'desc': 'Interactive vector visualizations tracking female landholding ratios, 4-decade census growth shifts, 135-district urbanization quadrants, and 70-year intercensal growth trajectories.',
        'cards': ['card-gender-land', 'card-census-shifts', 'card-districts-scatter', 'card-census-hist']
    },
    {
        'path': 'data/living-standards/index.html',
        'title': 'Living Standards, Household Budgets &amp; Labour Disparity Analytics',
        'desc': 'Interactive vector analytics illustrating household Engel food ratios, provincial food vs non-food consumption baskets, housing infrastructure deficits, and gender wage disparities.',
        'cards': ['card-hies', 'card-consumption-pie', 'card-services', 'card-lfs']
    }
]

for cfg in configs:
    p = cfg['path']
    with open(p, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add CSS in head
    if 'visual-insights.css' not in html:
        head_end = html.find('</head>')
        css_tag = '  <link rel="stylesheet" href="/assets/css/visual-insights.css" />\n  '
        html = html[:head_end] + css_tag + html[head_end:]

    # 2. Build section
    card_htmls = '\n\n'.join(get_card(cid) for cid in cfg['cards'])
    section_html = f"""
        <!-- ================= EMPIRICAL INFOGRAPHICS & VISUAL ANALYTICS ================= -->
        <section class="obs-section" id="observatory-infographics">
          <div class="obs-section-header">
            <div>
              <span class="obs-badge obs-badge-official">&check; Interactive Visual Analytics</span>
              <h2 class="obs-section-title" style="margin-top:6px;">{cfg['title']}</h2>
              <p class="obs-lead" style="font-size:0.95rem;color:var(--obs-text-muted);margin-top:4px;">
                {cfg['desc']}
              </p>
            </div>
            <div style="display:flex;align-items:center;">
              <a href="/insights/" class="obs-badge" style="background:#0f766e;color:#fff;text-decoration:none;padding:6px 12px;font-weight:600;display:inline-flex;align-items:center;gap:4px;">
                <span>View Full 16-Infographic Lab &rarr;</span>
              </a>
            </div>
          </div>

          <div class="vi-grid">
{card_htmls}
          </div>
        </section>
"""

    # Insert section before Comprehensive Indicator Catalog
    if 'id="observatory-infographics"' not in html:
        target = 'Comprehensive Indicator Catalog'
        pos = html.find(target)
        if pos != -1:
            sec_start = html.rfind('<section class="obs-section"', 0, pos)
            html = html[:sec_start] + section_html + '\n        ' + html[sec_start:]
        else:
            print(f"Target not found in {p}")

    # 3. Add scripts & canvas before </body>
    if 'visual-insights.js' not in html:
        body_end = html.rfind('</body>')
        runtime_scripts = """    <!-- Visual Analytics Runtime & Offscreen Canvas -->
    <div id="vi-tooltip" class="vi-tooltip" role="tooltip" aria-hidden="true" style="display:none;"></div>
    <div id="vi-toast" role="status" aria-live="polite"></div>
    <canvas id="vi-export-canvas" width="2080" height="1360" style="display:none;"></canvas>
    <script src="/assets/js/modules/visual-insights.js" defer></script>
"""
        html = html[:body_end] + runtime_scripts + html[body_end:]

    with open(p, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully integrated {p}")

print("All 4 thematic observatories integrated!")
