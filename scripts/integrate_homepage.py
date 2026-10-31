import re

# Load extracted card blocks
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

card_01 = get_card('card-fiscal')
card_16 = get_card('card-prov-matrix')
card_11 = get_card('card-districts-scatter')

showcase_html = f"""
      <!-- ================= VISUAL POLICY ANALYTICS & INFOGRAPHICS SHOWCASE ================= -->
      <section
        class="home-section home-visual-insights-section"
        id="section-visual-analytics"
        aria-labelledby="visual-analytics-title"
      >
        <div class="container">
          <div class="home-section-head" data-reveal>
            <div>
              <span class="home-section-label">Empirical Evidence Lab</span>
              <h2 id="visual-analytics-title">
                Visual Policy Analytics &amp; Empirical Infographics
              </h2>
            </div>
            <p>
              Interactive vector visualizations translating sovereign debt trajectories, provincial budgetary allocations, district disparities, and household living standards into actionable policy evidence.
            </p>
          </div>

          <div class="vi-grid">
            {card_01}

            {card_16}

            {card_11}
          </div>

          <div class="center" style="margin-top: 2.5rem; text-align: center;" data-reveal>
            <a href="/insights/" class="btn btn-primary" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.85rem 1.85rem; font-size: 1.05rem; font-weight: 600; text-decoration: none; border-radius: 6px;">
              <span>Explore All 16 Interactive Policy Infographics in Insights Lab</span>
              <span aria-hidden="true">&rarr;</span>
            </a>
          </div>
        </div>
      </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    home_html = f.read()

# 1. Add visual-insights.css if not present
if 'visual-insights.css' not in home_html:
    css_target = '<link rel="stylesheet" href="/assets/css/homepage.css" />'
    home_html = home_html.replace(css_target, f'{css_target}\n    <link rel="stylesheet" href="/assets/css/visual-insights.css" />')

# 2. Add section before platform section
if 'id="section-visual-analytics"' not in home_html:
    plat_target = '<section\n        class="home-section home-platform-section"'
    if plat_target in home_html:
        home_html = home_html.replace(plat_target, showcase_html + '\n      ' + plat_target)
    else:
        print("WARNING: plat_target not found with exact newlines, checking normalized")
        plat_target_norm = '<section class="home-section home-platform-section"'
        plat_idx = home_html.find('home-platform-section')
        sec_idx = home_html.rfind('<section', 0, plat_idx)
        home_html = home_html[:sec_idx] + showcase_html + '\n      ' + home_html[sec_idx:]

# 3. Add scripts & canvas before </body>
if 'visual-insights.js' not in home_html:
    body_target = '</body>'
    home_scripts = """    <!-- Visual Analytics Runtime & Offscreen Canvas -->
    <div id="vi-tooltip" class="vi-tooltip" role="tooltip" aria-hidden="true" style="display:none;"></div>
    <div id="vi-toast" role="status" aria-live="polite"></div>
    <canvas id="vi-export-canvas" width="2080" height="1360" style="display:none;"></canvas>
    <script src="/assets/js/modules/visual-insights.js" defer></script>
  </body>"""
    home_html = home_html.replace(body_target, home_scripts)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(home_html)

print("Homepage successfully integrated!")
