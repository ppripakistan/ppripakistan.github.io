with open('data/centre.html', 'r', encoding='utf-8') as f:
    html = f.read()

spotlight_html = """
      <!-- ================= SPOTLIGHT: VISUAL POLICY ANALYTICS LAB ================= -->
      <section class="dc-section" style="background: linear-gradient(135deg, #073c3a 0%, #042f2e 100%); color: #ffffff; padding: 2.75rem 0; border-bottom: 1px solid rgba(255,255,255,0.1);">
        <div class="container">
          <div style="display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1.5rem;">
            <div style="max-width: 680px;">
              <span class="dc-eyebrow" style="color: #5eead4; background: rgba(94,234,212,0.15); border: 1px solid rgba(94,234,212,0.3); padding: 4px 10px; border-radius: 999px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; display: inline-block; margin-bottom: 0.75rem;">NEW // EMPIRICAL VISUAL LAB</span>
              <h2 style="font-size: 1.85rem; font-weight: 800; color: #ffffff; margin-bottom: 0.5rem; letter-spacing: -0.02em;">Visual Policy Analytics &amp; Infographics Lab</h2>
              <p style="font-size: 1rem; color: #cbd5e1; line-height: 1.6; margin: 0;">
                Access 16 publication-grade interactive vector infographics covering sovereign debt servicing, provincial budget allocations, tax concession losses, 135-district urbanization quadrants, and 35-year macroeconomic regime trajectories.
              </p>
            </div>
            <div>
              <a href="/insights/" class="btn" style="background: #0f766e; color: #ffffff; padding: 0.9rem 1.85rem; border-radius: 6px; font-weight: 700; font-size: 1.05rem; text-decoration: none; display: inline-flex; align-items: center; gap: 0.5rem; box-shadow: 0 4px 14px rgba(0,0,0,0.25);">
                <span>Launch Visual Insights Lab (16 Infographics)</span>
                <span aria-hidden="true">&rarr;</span>
              </a>
            </div>
          </div>
        </div>
      </section>
"""

if 'Visual Policy Analytics &amp; Infographics Lab' not in html:
    target = '<!-- 02: THEMATIC DOMAIN ATLAS'
    if target not in html:
        target = 'THEMATIC DOMAIN ATLAS'
        pos = html.find(target)
        sec_pos = html.rfind('<section', 0, pos)
        html = html[:sec_pos] + spotlight_html + '\n\n      ' + html[sec_pos:]
    else:
        html = html.replace(target, spotlight_html + '\n\n      ' + target)

    with open('data/centre.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("data/centre.html updated with Visual Insights Lab spotlight!")
else:
    print("Spotlight already present in data/centre.html")
