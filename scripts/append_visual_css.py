css_additions = """
/* ==========================================================================
   SMOOTH SCROLL, QUICK-JUMP CHIPS & COMPREHENSIVE SEO NARRATIVE STYLES
   ========================================================================== */

/* Smooth Scroll & Card Anchor Clearance */
html {
  scroll-behavior: smooth;
}
.vi-card {
  scroll-margin-top: 100px;
  transition: box-shadow 0.3s ease, border-color 0.3s ease;
}
.vi-card.vi-card-highlight {
  box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.4), 0 12px 32px rgba(15, 118, 110, 0.15) !important;
  border-color: var(--vi-teal) !important;
}

/* Comprehensive SEO Hero Narrative */
.vi-hero-desc-narrative {
  color: #334155;
  font-size: 0.98rem;
  line-height: 1.65;
  margin-top: 16px;
  max-width: 1080px;
}
.vi-hero-desc-narrative p {
  margin-bottom: 12px;
}
.vi-seo-highlights {
  list-style: none;
  padding: 0;
  margin: 14px 0 18px 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 12px;
}
.vi-seo-highlights li {
  background: rgba(255, 255, 255, 0.85);
  border: 1px solid var(--vi-line);
  border-left: 3px solid var(--vi-teal);
  border-radius: 6px;
  padding: 10px 14px;
  font-size: 0.88rem;
  line-height: 1.55;
  color: #475569;
}
.vi-seo-highlights li strong {
  color: var(--vi-navy);
  display: block;
  margin-bottom: 4px;
  font-size: 0.92rem;
}
.vi-seo-footer-note {
  font-size: 0.9rem;
  color: var(--vi-muted);
  border-top: 1px dashed var(--vi-line);
  padding-top: 10px;
}

/* Grouped Thematic Quick-Jump Toolbar */
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
.vi-quick-clusters {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
  gap: 16px;
}
.vi-quick-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.vi-group-label {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--vi-teal);
  text-transform: uppercase;
  letter-spacing: 0.05em;
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

with open('assets/css/visual-insights.css', 'r', encoding='utf-8') as f:
    existing_css = f.read()

if 'SMOOTH SCROLL, QUICK-JUMP CHIPS' not in existing_css:
    new_css = existing_css.rstrip() + '\n' + css_additions
    with open('assets/css/visual-insights.css', 'w', encoding='utf-8') as f:
        f.write(new_css)
    print("SUCCESS: Appended new styles to assets/css/visual-insights.css")
else:
    print("Styles already present in visual-insights.css")
