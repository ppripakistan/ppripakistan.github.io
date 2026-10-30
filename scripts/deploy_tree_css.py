# -*- coding: utf-8 -*-

css_code = '''
/* ==========================================================================
   PPRI TOP-DOWN HIERARCHICAL KNOWLEDGE & EVIDENCE TREE ATLAS
   ========================================================================== */

.vi-tree-section {
  padding: 5.5rem 0 6.5rem;
  background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
  border-top: 1px solid #e2e8f0;
  border-bottom: 1px solid #cbd5e1;
  position: relative;
}

.vi-tree-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  flex-wrap: wrap;
  gap: 1.5rem;
  margin-bottom: 3rem;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid #e2e8f0;
}

.vi-tree-header-text {
  max-width: 780px;
}

.vi-tree-header-text h2 {
  font-size: clamp(1.85rem, 3.2vw, 2.5rem);
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -0.025em;
  line-height: 1.2;
  margin: 0.35rem 0 0.75rem;
}

.vi-tree-header-text p {
  font-size: 1.05rem;
  color: #475569;
  line-height: 1.6;
  margin: 0;
}

.vi-tree-controls {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.vi-tree-stat-pill {
  display: inline-flex;
  align-items: center;
  padding: 0.45rem 0.95rem;
  background: #ffffff;
  color: #0f766e;
  border: 1px solid #ccfbf1;
  border-radius: 9999px;
  font-size: 0.85rem;
  font-weight: 700;
  box-shadow: 0 1px 3px rgba(15, 118, 110, 0.08);
}

.vi-tree-toggle-all-btn {
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

.vi-tree-toggle-all-btn:hover {
  background: #1e293b;
  transform: translateY(-1px);
}

/* ── Level 0: Root Node ─────────────────────────────────────────────────── */
.vi-tree-root-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 5;
}

.vi-tree-root-node {
  background: #ffffff;
  border: 2px solid #0f766e;
  border-radius: 14px;
  padding: 0.85rem 1.75rem;
  text-align: center;
  box-shadow: 0 4px 14px rgba(15, 118, 110, 0.14);
  max-width: 520px;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.vi-tree-root-node:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(15, 118, 110, 0.2);
}

.root-badge {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #0f766e;
  background: #ccfbf1;
  padding: 0.18rem 0.65rem;
  border-radius: 9999px;
  margin-bottom: 0.45rem;
}

.root-title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
}

.root-icon {
  font-size: 1.85rem;
}

.root-text h3 {
  font-size: 1.15rem;
  font-weight: 800;
  color: #0f172a;
  margin: 0;
  line-height: 1.25;
}

.root-text span {
  font-size: 0.86rem;
  font-weight: 600;
  color: #64748b;
}

.vi-tree-root-stem {
  width: 3px;
  height: 26px;
  background: #0f766e;
  margin: 0 auto;
}

/* ── SVG Trunk Distributor (Desktop) ────────────────────────────────────── */
.vi-tree-trunk-network {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  line-height: 0;
}

.vi-tree-trunk-svg {
  width: 100%;
  height: 48px;
  display: block;
}

.trunk-path-base {
  stroke: #94a3b8;
  stroke-width: 2.5;
  fill: none;
  stroke-linecap: round;
  stroke-linejoin: round;
}

/* ── Level 1: 6 Pillar Branch Nodes ─────────────────────────────────────── */
.vi-tree-pillars-row {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 0.85rem;
  align-items: start;
}

.vi-tree-branch {
  display: flex;
  flex-direction: column;
  position: relative;
  transition: all 0.25s ease;
}

.vi-tree-branch-stem-in {
  width: 2.5px;
  height: 14px;
  background: #94a3b8;
  margin: 0 auto;
}

.vi-tree-node-card {
  width: 100%;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 10px;
  padding: 0.85rem 0.75rem;
  text-align: left;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
  transition: all 0.2s ease;
  position: relative;
}

.vi-tree-node-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 14px rgba(15, 23, 42, 0.08);
  border-color: #94a3b8;
}

.vi-tree-branch.is-open .vi-tree-node-card {
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.1);
  border-color: var(--pillar-border);
}

/* Pillar Theme Colors */
.theme-teal {
  --pillar-accent: #0f766e;
  --pillar-border: #0f766e;
  --pillar-bg-soft: #f0fdfa;
  --pillar-badge-bg: #ccfbf1;
}
.theme-blue {
  --pillar-accent: #2563eb;
  --pillar-border: #2563eb;
  --pillar-bg-soft: #eff6ff;
  --pillar-badge-bg: #dbeafe;
}
.theme-emerald {
  --pillar-accent: #059669;
  --pillar-border: #059669;
  --pillar-bg-soft: #ecfdf5;
  --pillar-badge-bg: #d1fae5;
}
.theme-indigo {
  --pillar-accent: #4f46e5;
  --pillar-border: #4f46e5;
  --pillar-bg-soft: #eef2ff;
  --pillar-badge-bg: #e0e7ff;
}
.theme-purple {
  --pillar-accent: #7c3aed;
  --pillar-border: #7c3aed;
  --pillar-bg-soft: #faf5ff;
  --pillar-badge-bg: #ede9fe;
}
.theme-amber {
  --pillar-accent: #d97706;
  --pillar-border: #d97706;
  --pillar-bg-soft: #fffbeb;
  --pillar-badge-bg: #fef3c7;
}

.vi-tree-node-card {
  border-top: 4px solid var(--pillar-accent);
}

.node-header {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.65rem;
}

.node-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 8px;
  font-size: 1.15rem;
  background: var(--pillar-bg-soft);
  flex-shrink: 0;
}

.node-titles {
  min-width: 0;
}

.node-tier {
  display: block;
  font-size: 0.68rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--pillar-accent);
  line-height: 1.2;
}

.node-name {
  font-size: 0.88rem;
  font-weight: 700;
  color: #0f172a;
  margin: 0.15rem 0 0 0;
  line-height: 1.25;
}

.node-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 0.5rem;
  border-top: 1px dashed #e2e8f0;
}

.node-count {
  font-size: 0.72rem;
  font-weight: 700;
  color: #475569;
  background: #f1f5f9;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
}

.node-toggle-state {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--pillar-badge-bg);
  color: var(--pillar-accent);
  font-size: 0.95rem;
  font-weight: 800;
  line-height: 1;
  transition: all 0.2s ease;
}

.vi-tree-branch.is-open .node-toggle-state {
  background: var(--pillar-accent);
  color: #ffffff;
}

/* ── Level 2: Sub-Branches & Level 3: Leaves ────────────────────────────── */
.vi-tree-substem {
  width: 2.5px;
  height: 18px;
  background: var(--pillar-accent);
  margin: 0 auto;
}

.vi-tree-children-container {
  display: flex;
  flex-direction: column;
  animation: treeFadeIn 0.25s ease-out;
}

@keyframes treeFadeIn {
  from { opacity: 0; transform: translateY(-4px); }
  to { opacity: 1; transform: translateY(0); }
}

.vi-tree-subbranches-list {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 0.75rem;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.vi-tree-subbranch-node {
  border-bottom: 1px dashed #e2e8f0;
  padding-bottom: 0.65rem;
}

.vi-tree-subbranch-node:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.subbranch-header {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  margin-bottom: 0.45rem;
}

.subbranch-connector {
  font-family: monospace;
  font-size: 0.85rem;
  color: #94a3b8;
}

.subbranch-header h5 {
  font-size: 0.78rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  color: #334155;
  margin: 0;
}

.subbranch-badge {
  font-size: 0.68rem;
  font-weight: 700;
  color: #64748b;
  margin-left: auto;
}

.vi-tree-leaves-grid {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
}

.vi-tree-leaf {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.35rem 0.55rem;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  font-size: 0.78rem;
  color: #1e293b;
  text-decoration: none;
  line-height: 1.3;
  transition: all 0.15s ease;
}

.vi-tree-leaf:hover {
  background: #ffffff;
  border-color: var(--pillar-accent);
  color: var(--pillar-accent);
  transform: translateX(2px);
  box-shadow: 0 2px 5px rgba(0,0,0,0.05);
}

.leaf-metric, .leaf-badge {
  display: inline-block;
  padding: 0.12rem 0.35rem;
  font-size: 0.68rem;
  font-weight: 700;
  border-radius: 4px;
  background: var(--pillar-badge-bg);
  color: var(--pillar-accent);
  white-space: nowrap;
  flex-shrink: 0;
}

.leaf-name {
  font-weight: 500;
  word-break: break-word;
}

.vi-tree-leaf-hub-link {
  margin-top: 0.65rem;
  padding-top: 0.5rem;
  text-align: center;
}

.vi-tree-leaf-hub-link a {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.76rem;
  font-weight: 700;
  color: var(--pillar-accent);
  text-decoration: none;
}

.vi-tree-leaf-hub-link a:hover {
  text-decoration: underline;
}

/* ── Mobile & Tablet Responsiveness: Vertical Indented Tree Spine ──────── */
@media (max-width: 1024px) {
  .vi-tree-trunk-network {
    display: none;
  }

  .vi-tree-pillars-row {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    margin-top: 1.5rem;
    padding-left: 1.25rem;
    border-left: 3px solid #0f766e;
    margin-left: auto;
    margin-right: auto;
    max-width: 600px;
  }

  .vi-tree-branch {
    position: relative;
  }

  .vi-tree-branch-stem-in {
    position: absolute;
    top: 1.4rem;
    left: -1.25rem;
    width: 1.25rem;
    height: 3px;
    background: #0f766e;
    margin: 0;
  }

  .vi-tree-node-card {
    padding: 1rem;
  }

  .node-name {
    font-size: 0.98rem;
  }
}
'''

with open('assets/css/visual-insights.css', 'r', encoding='utf-8') as f:
    existing = f.read()

# Replace previous treemap CSS if present
import re
existing_clean = re.sub(r'/\* =+ \s* PPRI MODULAR VISUAL TREEMAP MATRIX.*?(\Z|(?=/\* =+))', '', existing, flags=re.DOTALL)

with open('assets/css/visual-insights.css', 'w', encoding='utf-8') as f:
    f.write(existing_clean.strip() + '\n\n' + css_code.strip() + '\n')

print("Updated assets/css/visual-insights.css with Top-Down Hierarchical Tree styles.")
