# -*- coding: utf-8 -*-

css_code = '''
/* ==========================================================================
   PPRI MODULAR VISUAL TREEMAP MATRIX SITE EXPLORER
   ========================================================================== */

.vi-treemap-section {
  padding: 5.5rem 0 6rem;
  background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
  border-top: 1px solid #e2e8f0;
  border-bottom: 1px solid #cbd5e1;
}

.vi-treemap-header-row {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-bottom: 2.75rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
}

.vi-treemap-title-group {
  max-width: 780px;
}

.vi-treemap-title-group h2 {
  font-size: clamp(1.85rem, 3.2vw, 2.5rem);
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -0.025em;
  line-height: 1.2;
  margin: 0.35rem 0 0.75rem;
}

.vi-treemap-subtitle {
  font-size: 1.05rem;
  color: #475569;
  line-height: 1.6;
  margin: 0;
}

.vi-treemap-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.vi-treemap-stats-pill {
  display: inline-flex;
  align-items: center;
  padding: 0.45rem 0.95rem;
  background: #ffffff;
  color: #0f766e;
  border: 1px solid #ccfbf1;
  border-radius: 9999px;
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  box-shadow: 0 1px 3px rgba(15, 118, 110, 0.08);
}

.vi-treemap-toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.55rem 1.15rem;
  background: #0f172a;
  color: #ffffff;
  border: 1px solid #0f172a;
  border-radius: 8px;
  font-size: 0.88rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 4px rgba(15, 23, 42, 0.12);
}

.vi-treemap-toggle-btn:hover {
  background: #1e293b;
  transform: translateY(-1px);
}

.vi-treemap-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

@media (max-width: 900px) {
  .vi-treemap-grid {
    grid-template-columns: 1fr;
  }
}

.vi-treemap-tile {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}

.vi-treemap-tile:hover {
  box-shadow: 0 6px 16px rgba(15, 23, 42, 0.08);
  border-color: #cbd5e1;
}

.vi-treemap-tile[open] {
  box-shadow: 0 8px 24px rgba(15, 23, 42, 0.09);
}

/* Pillar Theme Left Accents */
.vi-treemap-tile.theme-teal { border-left: 5px solid #0f766e; }
.vi-treemap-tile.theme-blue { border-left: 5px solid #2563eb; }
.vi-treemap-tile.theme-emerald { border-left: 5px solid #059669; }
.vi-treemap-tile.theme-indigo { border-left: 5px solid #4f46e5; }
.vi-treemap-tile.theme-purple { border-left: 5px solid #7c3aed; }
.vi-treemap-tile.theme-amber { border-left: 5px solid #d97706; }

.vi-treemap-summary {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.35rem 1.5rem;
  cursor: pointer;
  list-style: none;
  user-select: none;
  background: #ffffff;
  transition: background 0.2s ease;
}

.vi-treemap-summary::-webkit-details-marker {
  display: none;
}

.vi-treemap-summary:hover {
  background: #f8fafc;
}

.vi-treemap-sum-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.vi-treemap-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 10px;
  font-size: 1.4rem;
  background: #f1f5f9;
  flex-shrink: 0;
}

.theme-teal .vi-treemap-icon { background: #f0fdfa; }
.theme-blue .vi-treemap-icon { background: #eff6ff; }
.theme-emerald .vi-treemap-icon { background: #ecfdf5; }
.theme-indigo .vi-treemap-icon { background: #eef2ff; }
.theme-purple .vi-treemap-icon { background: #faf5ff; }
.theme-amber .vi-treemap-icon { background: #fffbeb; }

.vi-treemap-sum-text h3 {
  font-size: 1.15rem;
  font-weight: 700;
  color: #0f172a;
  margin: 0 0 0.25rem 0;
  line-height: 1.3;
}

.vi-treemap-sum-text p {
  font-size: 0.88rem;
  color: #64748b;
  margin: 0;
  line-height: 1.4;
}

.vi-treemap-sum-right {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-shrink: 0;
}

.vi-treemap-pill {
  display: inline-block;
  padding: 0.28rem 0.75rem;
  font-size: 0.78rem;
  font-weight: 700;
  border-radius: 9999px;
  background: #f1f5f9;
  color: #475569;
}

.theme-teal .vi-treemap-pill { background: #e6f7f5; color: #0f766e; }
.theme-blue .vi-treemap-pill { background: #dbeafe; color: #1d4ed8; }
.theme-emerald .vi-treemap-pill { background: #d1fae5; color: #047857; }
.theme-indigo .vi-treemap-pill { background: #e0e7ff; color: #4338ca; }
.theme-purple .vi-treemap-pill { background: #ede9fe; color: #6d28d9; }
.theme-amber .vi-treemap-pill { background: #fef3c7; color: #b45309; }

.vi-treemap-chevron {
  color: #94a3b8;
  transition: transform 0.25s ease;
}

.vi-treemap-tile[open] .vi-treemap-chevron {
  transform: rotate(180deg);
  color: #0f172a;
}

.vi-treemap-content {
  padding: 1.25rem 1.5rem 1.5rem;
  border-top: 1px solid #f1f5f9;
  background: #fafbfc;
}

.vi-treemap-cluster {
  margin-bottom: 1.25rem;
}

.vi-treemap-cluster:last-of-type {
  margin-bottom: 1rem;
}

.vi-treemap-cluster-label {
  display: block;
  font-size: 0.74rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #64748b;
  margin-bottom: 0.65rem;
}

.vi-treemap-chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.vi-treemap-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.42rem 0.75rem;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  font-size: 0.84rem;
  color: #1e293b;
  text-decoration: none;
  line-height: 1.35;
  transition: all 0.18s ease;
  box-shadow: 0 1px 2px rgba(0,0,0,0.02);
}

.vi-treemap-chip:hover {
  background: #ffffff;
  border-color: #0f766e;
  color: #0f766e;
  transform: translateY(-1px);
  box-shadow: 0 3px 6px rgba(15, 118, 110, 0.08);
}

.theme-blue .vi-treemap-chip:hover { border-color: #2563eb; color: #2563eb; }
.theme-emerald .vi-treemap-chip:hover { border-color: #059669; color: #059669; }
.theme-indigo .vi-treemap-chip:hover { border-color: #4f46e5; color: #4f46e5; }
.theme-purple .vi-treemap-chip:hover { border-color: #7c3aed; color: #7c3aed; }
.theme-amber .vi-treemap-chip:hover { border-color: #d97706; color: #d97706; }

.chip-metric, .chip-badge {
  display: inline-block;
  padding: 0.15rem 0.45rem;
  font-size: 0.72rem;
  font-weight: 700;
  border-radius: 4px;
  background: #f1f5f9;
  color: #334155;
  white-space: nowrap;
}

.theme-teal .chip-metric, .theme-teal .chip-badge { background: #ccfbf1; color: #0f766e; }
.theme-blue .chip-metric, .theme-blue .chip-badge { background: #dbeafe; color: #1e40af; }
.theme-emerald .chip-metric, .theme-emerald .chip-badge { background: #d1fae5; color: #065f46; }
.theme-indigo .chip-metric, .theme-indigo .chip-badge { background: #e0e7ff; color: #3730a3; }
.theme-purple .chip-metric, .theme-purple .chip-badge { background: #ede9fe; color: #5b21b6; }
.theme-amber .chip-metric, .theme-amber .chip-badge { background: #fef3c7; color: #92400e; }

.chip-title {
  font-weight: 500;
}

.vi-treemap-footer-link {
  margin-top: 1.15rem;
  padding-top: 0.95rem;
  border-top: 1px dashed #e2e8f0;
  text-align: right;
}

.vi-treemap-footer-link a {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.86rem;
  font-weight: 700;
  color: #0f766e;
  text-decoration: none;
  transition: color 0.15s ease;
}

.theme-blue .vi-treemap-footer-link a { color: #2563eb; }
.theme-emerald .vi-treemap-footer-link a { color: #059669; }
.theme-indigo .vi-treemap-footer-link a { color: #4f46e5; }
.theme-purple .vi-treemap-footer-link a { color: #7c3aed; }
.theme-amber .vi-treemap-footer-link a { color: #d97706; }

.vi-treemap-footer-link a:hover {
  text-decoration: underline;
}
'''

with open('assets/css/visual-insights.css', 'r', encoding='utf-8') as f:
    existing = f.read()

if 'vi-treemap-section' not in existing:
    with open('assets/css/visual-insights.css', 'a', encoding='utf-8') as f:
        f.write('\n' + css_code)
    print("Appended treemap CSS to assets/css/visual-insights.css")
else:
    print("Treemap CSS already present in visual-insights.css")
