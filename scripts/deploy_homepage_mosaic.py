import re

# 1. Append Mosaic CSS to assets/css/visual-insights.css
mosaic_css = """
/* ==========================================================================
   HOMEPAGE 16-INFOGRAPHIC VISUAL POLICY MOSAIC GRID
   ========================================================================== */
.vi-mosaic-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-top: 24px;
}
@media (max-width: 1200px) {
  .vi-mosaic-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
@media (max-width: 820px) {
  .vi-mosaic-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 520px) {
  .vi-mosaic-grid {
    grid-template-columns: 1fr;
  }
}

.vi-mosaic-card {
  display: flex;
  flex-direction: column;
  background: #ffffff;
  border: 1px solid var(--vi-line, #e2e8f0);
  border-radius: 8px;
  overflow: hidden;
  text-decoration: none;
  color: inherit;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.2s ease, border-color 0.2s ease;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.vi-mosaic-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(15, 118, 110, 0.12);
  border-color: #5eead4;
}

.vi-mosaic-media {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 10;
  background: #073c3a;
  overflow: hidden;
}
.vi-mosaic-media img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.3s ease;
}
.vi-mosaic-card:hover .vi-mosaic-media img {
  transform: scale(1.03);
}

.vi-mosaic-hover-pill {
  position: absolute;
  bottom: 8px;
  right: 8px;
  background: rgba(15, 23, 42, 0.85);
  color: #5eead4;
  font-size: 0.72rem;
  font-weight: 700;
  padding: 3px 8px;
  border-radius: 4px;
  backdrop-filter: blur(4px);
  opacity: 0;
  transform: translateY(4px);
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.vi-mosaic-card:hover .vi-mosaic-hover-pill {
  opacity: 1;
  transform: translateY(0);
}

.vi-mosaic-body {
  padding: 12px 14px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}
.vi-mosaic-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 6px;
  gap: 6px;
}
.vi-mosaic-domain {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 2px 6px;
  border-radius: 3px;
}
.vi-domain-fiscal { background: #f0fdfa; color: #0f766e; }
.vi-domain-economy { background: #eff6ff; color: #2563eb; }
.vi-domain-demographics { background: #faf5ff; color: #7c3aed; }
.vi-domain-living { background: #fffbeb; color: #d97706; }

.vi-mosaic-metric {
  font-size: 0.72rem;
  font-weight: 700;
  color: #073c3a;
  background: #f1f5f9;
  padding: 2px 6px;
  border-radius: 3px;
}

.vi-mosaic-title {
  font-size: 0.88rem;
  font-weight: 700;
  color: #0f172a;
  margin: 0 0 6px 0;
  line-height: 1.35;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.vi-mosaic-snippet {
  font-size: 0.78rem;
  color: #64748b;
  line-height: 1.45;
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
"""

with open('assets/css/visual-insights.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'HOMEPAGE 16-INFOGRAPHIC VISUAL POLICY MOSAIC GRID' not in css_content:
    with open('assets/css/visual-insights.css', 'w', encoding='utf-8') as f:
        f.write(css_content.rstrip() + '\n' + mosaic_css)
    print("SUCCESS: Appended mosaic grid CSS to visual-insights.css")
else:
    print("Mosaic CSS already present in visual-insights.css")

# 2. Metadata for the 16 Policy Micro-Cards
mosaic_cards = [
    # Fiscal & Sovereign Debt
    {
        'id': 'card-fiscal',
        'domain_class': 'vi-domain-fiscal',
        'domain': 'Fiscal Solvency',
        'metric': '51.8% Markup',
        'title': 'Federal Budget Allocation &amp; Sovereign Debt Servicing',
        'snippet': 'Sovereign debt markup absorbs PKR 9,775B, leaving only 7.4% for national development (PSDP).',
        'w': 800, 'h': 620
    },
    {
        'id': 'card-debt',
        'domain_class': 'vi-domain-fiscal',
        'domain': 'Public Debt',
        'metric': 'PKR 86.4T Debt',
        'title': 'The 8-Year Sovereign Public Debt Trajectory (FY18–FY26)',
        'snippet': 'Total public debt expanded from PKR 25.0T to PKR 86.4T, compounding sovereign markup velocity.',
        'w': 800, 'h': 620
    },
    {
        'id': 'card-tax-exp',
        'domain_class': 'vi-domain-fiscal',
        'domain': 'Tax Policy',
        'metric': 'PKR 3.98T Exempt',
        'title': 'Federal Tax Concessions &amp; Revenue Foregone',
        'snippet': 'Corporate exemptions and zero-rating concessions equal 43% of total FBR tax revenue.',
        'w': 800, 'h': 620
    },
    {
        'id': 'card-prov-matrix',
        'domain_class': 'vi-domain-fiscal',
        'domain': 'Provincial Matrix',
        'metric': '4 Provinces',
        'title': 'Provincial Resource Allocation, Debt Stock &amp; Conflict Matrix',
        'snippet': 'Comparing budgetary outlay, ADP allocations, debt stock, per capita spend, and regional conflict incidents.',
        'w': 1040, 'h': 680
    },

    # Economy & Jobs
    {
        'id': 'card-wage-infl',
        'domain_class': 'vi-domain-economy',
        'domain': 'Purchasing Power',
        'metric': '-42% Real Wage',
        'title': 'Purchasing Power Erosion: Real Wages vs Inflation',
        'snippet': 'Cumulative CPI inflation (+205%) heavily outpaced statutory minimum wage adjustments since FY10.',
        'w': 800, 'h': 620
    },
    {
        'id': 'card-sector-employment',
        'domain_class': 'vi-domain-economy',
        'domain': 'Labour Markets',
        'metric': '37.4% Agri Share',
        'title': 'Sectoral Labour Force Absorption Dynamics',
        'snippet': 'Agriculture absorbs 37.4% of total labour force despite contributing only 24% to gross value added.',
        'w': 800, 'h': 620
    },
    {
        'id': 'card-agri-shifts',
        'domain_class': 'vi-domain-economy',
        'domain': 'Agrarian Economy',
        'metric': '64% Farms &lt;5 Acres',
        'title': 'Smallholder Landholding &amp; Acreage Fragmentation',
        'snippet': 'Rapid subdivision into sub-subsistence holdings constrains agricultural mechanization and yield.',
        'w': 800, 'h': 620
    },
    {
        'id': 'card-macro',
        'domain_class': 'vi-domain-economy',
        'domain': 'Macro History',
        'metric': '35-Year Trajectory',
        'title': '35-Year Macroeconomic Trajectory (4 Regimes &amp; Crisis Shocks)',
        'snippet': 'Tracking real GDP growth, CPI inflation, current account deficits, and debt over 35 years.',
        'w': 1040, 'h': 680
    },

    # Demographics & Spatial Governance
    {
        'id': 'card-gender-land',
        'domain_class': 'vi-domain-demographics',
        'domain': 'Gender &amp; Property',
        'metric': '2.9% Female Owners',
        'title': 'Female Gender Ratios &amp; Agrarian Landholding Asymmetry',
        'snippet': 'Stark divide between female demographic population share and formal land ownership.',
        'w': 800, 'h': 620
    },
    {
        'id': 'card-census-shifts',
        'domain_class': 'vi-domain-demographics',
        'domain': 'Demographics',
        'metric': '+2.55% Annual Growth',
        'title': 'Multi-Census Provincial Demographic Shifts (1981–2023)',
        'snippet': 'Differential compound annual growth rates reshaping provincial demographic weights across 4 decades.',
        'w': 800, 'h': 620
    },
    {
        'id': 'card-districts-scatter',
        'domain_class': 'vi-domain-demographics',
        'domain': 'Spatial Atlas',
        'metric': '135 Districts',
        'title': '135-District Urbanization &amp; Density Quadrant Matrix',
        'snippet': 'Spatial clustering across mega-urban hubs, dense agrarian belts, and sparse peripheries.',
        'w': 1040, 'h': 680
    },
    {
        'id': 'card-census-hist',
        'domain_class': 'vi-domain-demographics',
        'domain': 'Demographic History',
        'metric': '33.7M &rarr; 241.5M',
        'title': '70-Year Intercensal Demographic Growth Trajectory',
        'snippet': 'Seven-fold population expansion over seven decades of statehood since the 1951 baseline.',
        'w': 800, 'h': 620
    },

    # Living Standards & Household Budgets
    {
        'id': 'card-hies',
        'domain_class': 'vi-domain-living',
        'domain': 'Living Standards',
        'metric': '52.4% Food Engel',
        'title': 'Household Food Engel Burden Divide (HIES 2024–25)',
        'snippet': 'Lowest-income quintiles commit over half of total consumption exclusively to basic food.',
        'w': 800, 'h': 620
    },
    {
        'id': 'card-consumption-pie',
        'domain_class': 'vi-domain-living',
        'domain': 'Household Baskets',
        'metric': 'Food vs Non-Food',
        'title': 'Provincial Food vs Non-Food Household Consumption Baskets',
        'snippet': 'Disparities between provincial spending on basic food vs housing, utilities, and healthcare.',
        'w': 800, 'h': 620
    },
    {
        'id': 'card-services',
        'domain_class': 'vi-domain-living',
        'domain': 'Basic Amenities',
        'metric': '38% Piped Water',
        'title': 'Household Basic Housing Characteristics &amp; Utilities Deficit',
        'snippet': 'Critical deficits in piped drinking water, flush sanitation, and clean cooking fuel access.',
        'w': 800, 'h': 620
    },
    {
        'id': 'card-lfs',
        'domain_class': 'vi-domain-living',
        'domain': 'Labour &amp; Wages',
        'metric': '-34% Rural Wage',
        'title': 'Labour Force Participation &amp; Gender/Rural Wage Disparities',
        'snippet': 'Significant female wage discounts and rural-urban earnings gap across provinces.',
        'w': 800, 'h': 620
    }
]

# Generate micro-cards HTML
cards_markup = []
for c in mosaic_cards:
    markup = f"""            <!-- Micro-Card: {c['id']} -->
            <a href="/insights/#{c['id']}" class="vi-mosaic-card" aria-label="Explore {c['title']}">
              <div class="vi-mosaic-media">
                <img
                  src="/assets/images/insights/{c['id']}.svg"
                  alt="{c['title']}"
                  width="{c['w']}"
                  height="{c['h']}"
                  loading="lazy"
                  decoding="async"
                />
                <span class="vi-mosaic-hover-pill">Launch Interactive Visual &rarr;</span>
              </div>
              <div class="vi-mosaic-body">
                <div class="vi-mosaic-meta">
                  <span class="vi-mosaic-domain {c['domain_class']}">{c['domain']}</span>
                  <span class="vi-mosaic-metric">{c['metric']}</span>
                </div>
                <h3 class="vi-mosaic-title">{c['title']}</h3>
                <p class="vi-mosaic-snippet">{c['snippet']}</p>
              </div>
            </a>"""
    cards_markup.append(markup)

all_cards_html = '\n'.join(cards_markup)

new_section_html = f"""      <!-- ================= VISUAL POLICY ANALYTICS & INFOGRAPHICS SHOWCASE ================= -->
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
              High-efficiency vector visualizations translating sovereign debt trajectories, provincial budgetary allocations, district disparities, and household living standards into actionable policy evidence.
            </p>
          </div>

          <!-- 16-Infographic Visual Policy Mosaic Grid -->
          <div class="vi-mosaic-grid">
{all_cards_html}
          </div>

          <div class="center" style="margin-top: 2.75rem; text-align: center;" data-reveal>
            <a href="/insights/" class="btn btn-primary" style="display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.85rem 1.85rem; font-size: 1.05rem; font-weight: 600; text-decoration: none; border-radius: 6px;">
              <span>Explore All 16 Interactive Policy Infographics in Insights Lab</span>
              <span aria-hidden="true">&rarr;</span>
            </a>
          </div>
        </div>
      </section>"""

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    home_html = f.read()

# Replace existing showcase section
section_pattern = r'<!-- =+ VISUAL POLICY ANALYTICS.*?-->\s*<section[^>]*id="section-visual-analytics".*?</section>'
if re.search(section_pattern, home_html, flags=re.DOTALL):
    home_html = re.sub(section_pattern, new_section_html, home_html, flags=re.DOTALL)
    print("SUCCESS: Replaced showcase section with 16-card mosaic grid in index.html")
else:
    print("WARNING: Could not match existing section-visual-analytics pattern")

# Remove visual-insights.js and canvas/tooltip from index.html
old_scripts = r'<!-- Visual Analytics Runtime & Offscreen Canvas -->\s*<div id="vi-tooltip".*?</canvas>\s*<script src="/assets/js/modules/visual-insights.js"[^>]*></script>'
if re.search(old_scripts, home_html, flags=re.DOTALL):
    home_html = re.sub(old_scripts, '', home_html, flags=re.DOTALL)
    print("SUCCESS: Removed visual-insights.js runtime and offscreen canvas from index.html (Saved 232 KB JS!)")
else:
    # Try individual script removal
    home_html = re.sub(r'<script src="/assets/js/modules/visual-insights.js"[^>]*></script>\s*', '', home_html)
    home_html = re.sub(r'<canvas id="vi-export-canvas"[^>]*></canvas>\s*', '', home_html)
    home_html = re.sub(r'<div id="vi-tooltip"[^>]*></div>\s*', '', home_html)
    home_html = re.sub(r'<div id="vi-toast"[^>]*></div>\s*', '', home_html)
    print("SUCCESS: Cleaned up script and canvas tags from index.html")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(home_html)

print("Updated index.html with 16-card mosaic grid!")
