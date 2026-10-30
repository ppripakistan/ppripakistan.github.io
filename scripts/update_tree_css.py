# -*- coding: utf-8 -*-

css_code = '''/* ==========================================================================
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
  margin-bottom: 3.5rem;
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
  flex-wrap: wrap;
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

.vi-tree-btn-group {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  background: #f1f5f9;
  padding: 0.3rem;
  border-radius: 10px;
  border: 1px solid #cbd5e1;
}

.vi-tree-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.45rem 0.95rem;
  border: 1px solid transparent;
  border-radius: 7px;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.18s ease;
}

.vi-tree-expand-all {
  background: #0f172a;
  color: #ffffff;
  border-color: #0f172a;
  box-shadow: 0 2px 4px rgba(15, 23, 42, 0.12);
}

.vi-tree-expand-all:hover {
  background: #1e293b;
  transform: translateY(-1px);
}

.vi-tree-collapse-all {
  background: #ffffff;
  color: #334155;
  border-color: #cbd5e1;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.vi-tree-collapse-all:hover {
  background: #f8fafc;
  color: #0f172a;
  border-color: #94a3b8;
  transform: translateY(-1px);
}

/* ── Level 0: Grand Octagonal Root Node ─────────────────────────────────── */
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
  border-radius: 16px;
  padding: 1.1rem 2.2rem;
  text-align: center;
  box-shadow: 0 0 0 4px #ccfbf1, 0 8px 24px rgba(15, 118, 110, 0.16);
  max-width: 560px;
  position: relative;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.vi-tree-root-node:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 0 6px #ccfbf1, 0 12px 30px rgba(15, 118, 110, 0.22);
}

.root-badge {
  display: inline-block;
  font-size: 0.72rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #0f766e;
  background: #ccfbf1;
  padding: 0.2rem 0.75rem;
  border-radius: 9999px;
  margin-bottom: 0.5rem;
}

.root-title {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.85rem;
}

.root-icon {
  font-size: 2rem;
}

.root-text h3 {
  font-size: 1.25rem;
  font-weight: 800;
  color: #0f172a;
  margin: 0;
  line-height: 1.25;
}

.root-text span {
  font-size: 0.9rem;
  font-weight: 600;
  color: #64748b;
}

.root-port-bottom {
  position: absolute;
  bottom: -6px;
  left: 50%;
  transform: translateX(-50%);
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #0f766e;
  border: 2px solid #ffffff;
  box-shadow: 0 0 0 2px #0f766e;
}

.vi-tree-root-stem {
  width: 3px;
  height: 28px;
  background: #0f766e;
  margin: 0 auto;
}

/* ── Level 1: Mathematical CSS Tree Busbar & Pillar Network ────────────── */
.vi-tree-busbar-container {
  display: none; /* Managed directly via .vi-tree-pillars-row::before */
}

.vi-tree-pillars-row {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 0.85rem;
  align-items: start;
  position: relative;
  margin-top: 0;
}

/* Mathematical Tree Busbar: Exactly spans from center of Col 1 to center of Col 6 */
.vi-tree-pillars-row::before {
  content: '';
  position: absolute;
  top: 0;
  /* (100% - 5 * gap) / 12 is the exact center of column 1 */
  left: calc((100% - 5 * 0.85rem) / 12);
  right: calc((100% - 5 * 0.85rem) / 12);
  height: 3px;
  background: #94a3b8;
  z-index: 2;
}

/* Center junction node where root stem meets busbar */
.vi-tree-pillars-row::after {
  content: '';
  position: absolute;
  top: -3.5px;
  left: 50%;
  transform: translateX(-50%);
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #0f766e;
  border: 2px solid #ffffff;
  box-shadow: 0 0 0 2px #0f766e;
  z-index: 3;
}

.vi-tree-branch {
  display: flex;
  flex-direction: column;
  position: relative;
  transition: all 0.25s ease;
}

/* Vertical connector stem dropping from busbar into pillar */
.vi-tree-branch-stem-in {
  width: 3px;
  height: 20px;
  background: #94a3b8;
  margin: 0 auto;
  position: relative;
  z-index: 2;
}

/* Port socket dot on top of stem where it meets the busbar */
.vi-tree-branch-stem-in::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #94a3b8;
  border: 2px solid #ffffff;
  box-shadow: 0 0 0 1.5px #94a3b8;
}

.vi-tree-branch.is-open .vi-tree-branch-stem-in {
  background: var(--pillar-accent);
}
.vi-tree-branch.is-open .vi-tree-branch-stem-in::before {
  background: var(--pillar-accent);
  box-shadow: 0 0 0 1.5px var(--pillar-accent);
}

/* Pillar Card Node */
.vi-tree-node-card {
  width: 100%;
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 12px;
  padding: 0.95rem 0.8rem;
  text-align: left;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04);
  transition: all 0.2s ease;
  position: relative;
  border-top: 4px solid var(--pillar-accent);
}

.vi-tree-node-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(15, 23, 42, 0.09);
  border-color: #94a3b8;
}

.vi-tree-branch.is-open .vi-tree-node-card {
  box-shadow: 0 8px 20px rgba(15, 23, 42, 0.12);
  border-color: var(--pillar-border);
}

.node-port-top {
  position: absolute;
  top: -5px;
  left: 50%;
  transform: translateX(-50%);
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--pillar-accent);
  border: 1.5px solid #ffffff;
  z-index: 4;
}

.node-port-bottom {
  position: absolute;
  bottom: -5px;
  left: 50%;
  transform: translateX(-50%);
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--pillar-accent);
  border: 1.5px solid #ffffff;
  opacity: 0;
  transition: opacity 0.2s ease;
  z-index: 4;
}

.vi-tree-branch.is-open .node-port-bottom {
  opacity: 1;
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
  width: 34px;
  height: 34px;
  border-radius: 8px;
  font-size: 1.2rem;
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

/* ── CRITICAL FIX: SPECIFICITY RULES FOR EXPAND / COLLAPSE ────────────── */
.vi-tree-children-container {
  display: flex;
  flex-direction: column;
  animation: treeFadeIn 0.25s ease-out;
}

.vi-tree-children-container[hidden],
.vi-tree-branch:not(.is-open) .vi-tree-children-container {
  display: none !important;
}

.vi-tree-branch.is-open .vi-tree-children-container {
  display: flex !important;
}

@keyframes treeFadeIn {
  from { opacity: 0; transform: translateY(-4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ── Level 2 & 3: Continuous CSS Vector Connector Lines ────────────────── */
.vi-tree-substem {
  width: 3px;
  height: 18px;
  background: var(--pillar-accent);
  margin: 0 auto;
}

.vi-tree-subbranches-list {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 0.85rem 0.75rem;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}

.vi-tree-subbranch-node {
  border-bottom: 1px dashed #e2e8f0;
  padding-bottom: 0.75rem;
}

.vi-tree-subbranch-node:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.subbranch-header {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin-bottom: 0.5rem;
}

.subbranch-joint {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--pillar-accent);
  color: transparent;
  flex-shrink: 0;
  box-shadow: 0 0 0 2px var(--pillar-badge-bg);
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

/* Continuous Tree Spine for Leaf Nodes */
.vi-tree-leaves-grid {
  display: flex;
  flex-direction: column;
  gap: 0.35rem;
  padding-left: 0.75rem;
  margin-left: 0.35rem;
  border-left: 2px solid var(--pillar-badge-bg);
  position: relative;
}

.vi-tree-leaf {
  position: relative;
  display: flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.38rem 0.6rem;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  font-size: 0.78rem;
  color: #1e293b;
  text-decoration: none;
  line-height: 1.3;
  transition: all 0.18s ease;
}

.vi-tree-leaf:hover {
  background: #ffffff;
  border-color: var(--pillar-accent);
  color: var(--pillar-accent);
  transform: translateX(2px);
  box-shadow: 0 2px 6px rgba(0,0,0,0.06);
}

.leaf-joint {
  position: absolute;
  left: -0.75rem;
  top: 50%;
  width: 0.55rem;
  height: 2px;
  background: var(--pillar-badge-bg);
}

.leaf-metric, .leaf-badge {
  display: inline-block;
  padding: 0.12rem 0.38rem;
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
  .vi-tree-pillars-row::before,
  .vi-tree-pillars-row::after {
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

  .vi-tree-branch-stem-in::before {
    display: none;
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

import re
# Strip existing tree CSS block
existing_clean = re.sub(r'/\* =+ \s* PPRI TOP-DOWN HIERARCHICAL KNOWLEDGE.*?(\Z)', '', existing, flags=re.DOTALL)

with open('assets/css/visual-insights.css', 'w', encoding='utf-8') as f:
    f.write(existing_clean.strip() + '\n\n' + css_code.strip() + '\n')

print("Updated assets/css/visual-insights.css with Busbar, Sockets, and Specificity Fix.")
