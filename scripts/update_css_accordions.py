with open('assets/css/visual-insights.css', 'r', encoding='utf-8') as f:
    css = f.read()

target_marker = "/* Comprehensive SEO Hero Narrative */"
idx = css.find(target_marker)
if idx == -1:
    raise ValueError("Target marker not found in visual-insights.css")

base_css = css[:idx]

new_styles = """/* ==========================================================================
   BREADCRUMB SPACING & CURRENT-PAGE DARK GREEN STYLING
   ========================================================================== */
.breadcrumb-nav {
  padding-top: 28px !important;
  padding-bottom: 10px !important;
  background: transparent;
}
.breadcrumb-inner {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  font-size: 0.86rem;
  color: var(--vi-muted);
}
.breadcrumb-inner a {
  color: var(--vi-teal);
  text-decoration: none;
  font-weight: 500;
  transition: color 0.15s ease;
}
.breadcrumb-inner a:hover {
  color: var(--vi-teal-dark);
  text-decoration: underline;
}
.breadcrumb-separator {
  color: #cbd5e1;
  font-size: 0.8rem;
  user-select: none;
}
.breadcrumb-inner [aria-current="page"] {
  color: #042f2e !important; /* Prominent dark green */
  background: #e6f3f2 !important; /* Soft mint / dark-green tint */
  padding: 3px 12px !important;
  border-radius: 999px !important;
  font-weight: 700 !important;
  font-size: 0.84rem !important;
  border: 1px solid rgba(15, 118, 110, 0.25) !important;
  letter-spacing: -0.01em;
  display: inline-flex;
  align-items: center;
}

/* ==========================================================================
   EXECUTIVE SEO NARRATIVE & COLLAPSIBLE ACCORDION CARDS
   ========================================================================== */
.vi-hero-desc-narrative {
  color: #334155;
  font-size: 0.98rem;
  line-height: 1.65;
  margin-top: 14px;
  max-width: 1100px;
}
.vi-hero-desc-narrative p {
  margin-bottom: 12px;
}

/* 4 Collapsible Policy Accordion Cards */
.vi-seo-accordion-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 14px;
  margin: 18px 0 24px 0;
}
.vi-seo-accordion {
  background: #ffffff;
  border: 1px solid var(--vi-line);
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}
.vi-seo-accordion[open] {
  box-shadow: 0 4px 16px rgba(0,0,0,0.08);
  border-color: #cbd5e1;
}
.vi-seo-summary {
  padding: 12px 14px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  user-select: none;
  list-style: none;
  background: #f8fafc;
  font-weight: 700;
  font-size: 0.88rem;
  color: var(--vi-navy);
  transition: background 0.15s ease, color 0.15s ease;
}
.vi-seo-summary::-webkit-details-marker {
  display: none;
}
.vi-seo-summary:hover {
  background: #f0fdfa;
  color: var(--vi-teal);
}
.vi-seo-summary-left {
  display: flex;
  align-items: center;
  gap: 8px;
}
.vi-seo-icon {
  font-size: 1.05rem;
}
.vi-seo-summary-right {
  display: flex;
  align-items: center;
  gap: 8px;
}
.vi-seo-badge {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 2px 7px;
  background: #e2e8f0;
  color: #475569;
  border-radius: 4px;
}
.vi-seo-chevron {
  font-size: 0.85rem;
  color: var(--vi-muted);
  transition: transform 0.2s ease;
  display: inline-block;
}
.vi-seo-accordion[open] .vi-seo-chevron {
  transform: rotate(180deg);
}
.vi-seo-body {
  padding: 14px 16px;
  font-size: 0.88rem;
  color: #475569;
  line-height: 1.62;
  background: #ffffff;
  border-top: 1px solid #f1f5f9;
}
.vi-seo-body p {
  margin: 0;
}

/* ==========================================================================
   SEPARATED THEMATIC QUICK-JUMP TOOLBAR & DOMAIN CARDS
   ========================================================================== */
.vi-quick-nav {
  margin-top: 24px;
  margin-bottom: 24px;
  background: #ffffff;
  border: 1px solid var(--vi-line);
  border-radius: 12px;
  padding: 18px 20px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.03);
}
.vi-quick-nav-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 14px;
  padding-bottom: 10px;
  border-bottom: 1px solid #f1f5f9;
}
.vi-quick-nav-title {
  font-size: 0.85rem;
  font-weight: 800;
  color: var(--vi-navy);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}
.vi-quick-nav-hint {
  font-size: 0.8rem;
  color: var(--vi-muted);
}

/* 4 Distinct Visually Separated Thematic Domain Cards */
.vi-quick-clusters-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 16px;
  margin-top: 8px;
}
.vi-jump-domain-card {
  background: #ffffff;
  border: 1px solid var(--vi-line);
  border-radius: 8px;
  padding: 14px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  display: flex;
  flex-direction: column;
  gap: 10px;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.vi-jump-domain-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.06);
}

.vi-jump-card-fiscal {
  border-top: 3.5px solid #0f766e;
  background: linear-gradient(180deg, #f0fdfa 0%, #ffffff 40px);
}
.vi-jump-card-economy {
  border-top: 3.5px solid #2563eb;
  background: linear-gradient(180deg, #eff6ff 0%, #ffffff 40px);
}
.vi-jump-card-demographics {
  border-top: 3.5px solid #7c3aed;
  background: linear-gradient(180deg, #faf5ff 0%, #ffffff 40px);
}
.vi-jump-card-living {
  border-top: 3.5px solid #d97706;
  background: linear-gradient(180deg, #fffbeb 0%, #ffffff 40px);
}

.vi-jump-domain-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 8px;
  border-bottom: 1px solid rgba(0,0,0,0.06);
}
.vi-domain-tag {
  font-size: 0.82rem;
  font-weight: 800;
  color: var(--vi-navy);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  display: flex;
  align-items: center;
  gap: 6px;
}

.vi-group-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.vi-chip-btn {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  color: #1e293b;
  padding: 6px 11px;
  border-radius: 6px;
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
  display: inline-flex;
  align-items: center;
  gap: 4px;
  outline: none;
  user-select: none;
}
.vi-chip-btn:hover {
  background: #f0fdfa;
  border-color: #5eead4;
  color: #0f766e;
  transform: translateY(-1px);
  box-shadow: 0 2px 6px rgba(15, 118, 110, 0.08);
}
.vi-chip-btn:active {
  transform: translateY(0);
  background: #ccfbf1;
}
.vi-chip-btn.vi-chip-highlight {
  background: #f0fdfa;
  border-color: #99f6e4;
  color: #0f766e;
  font-weight: 700;
}
.vi-chip-btn.vi-chip-highlight:hover {
  background: #0f766e;
  color: #ffffff;
  border-color: #0f766e;
}
"""

with open('assets/css/visual-insights.css', 'w', encoding='utf-8') as f:
    f.write(base_css + new_styles)

print("SUCCESS: Updated assets/css/visual-insights.css with accordions, separated cards, and breadcrumb styling!")
