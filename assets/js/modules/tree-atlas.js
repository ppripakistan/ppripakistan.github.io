/**
 * PPRI Organic Hierarchical Pyramid Tree Atlas
 * Dynamic multi-tier SVG Bézier branching (Root ➔ 6 Pillars ➔ 14 Subdivisions),
 * integrated root toggle button, and hover lineage glow.
 */

(function () {
  'use strict';

  function initPyramidTree() {
    var canvas = document.getElementById('viTreeCanvas');
    var svg = document.getElementById('viTreeSvgBranches');
    var tier1Group = document.getElementById('viTreeTier1Paths');
    var tier2Group = document.getElementById('viTreeTier2Paths');
    var rootPort = document.getElementById('rootPortBottom');
    var rootNode = document.getElementById('viTreeRootNode');
    var rootToggle = document.getElementById('viTreeRootToggle');
    var toggleIcon = document.getElementById('viTreeToggleIcon');
    var toggleText = document.getElementById('viTreeToggleText');
    var pillarCols = document.querySelectorAll('.vi-tree-pillar-col');
    var subNodes = document.querySelectorAll('.vi-tree-subdivision-node');
    var level2Container = document.getElementById('viTreeLevel2Container');
    var tooltip = document.getElementById('viTreeTooltip');
    var tooltipBadge = document.getElementById('viTooltipBadge');
    var tooltipTitle = document.getElementById('viTooltipTitle');
    var tooltipSummary = document.getElementById('viTooltipSummary');

    if (!canvas || !svg || !tier1Group || !tier2Group || !rootPort) {
      return;
    }

    var isExpanded = true;
    var tier1Paths = {};
    var tier2Paths = {};

    /* ── 1. Dynamic SVG Bézier Paths Calculation ─────────────────────── */
    function renderSvgBranches() {
      var canvasRect = canvas.getBoundingClientRect();
      var rootPortRect = rootPort.getBoundingClientRect();

      var canvasWidth = canvasRect.width;
      var canvasHeight = canvasRect.height;
      svg.setAttribute('viewBox', '0 0 ' + canvasWidth + ' ' + canvasHeight);
      svg.style.width = canvasWidth + 'px';
      svg.style.height = canvasHeight + 'px';

      // Level 0 Root Port coordinates (relative to canvas)
      var rootX = rootPortRect.left + rootPortRect.width / 2 - canvasRect.left;
      var rootY = rootPortRect.top + rootPortRect.height / 2 - canvasRect.top;

      // ── Draw Tier 1 Paths (Root ➔ 6 Pillars) ─────────────────────────
      pillarCols.forEach(function (col) {
        var pid = col.getAttribute('data-pillar');
        var portTop = document.getElementById('pillarPortTop-' + pid);
        if (!portTop) return;

        var portRect = portTop.getBoundingClientRect();
        var targetX = portRect.left + portRect.width / 2 - canvasRect.left;
        var targetY = portRect.top + portRect.height / 2 - canvasRect.top;

        var deltaY = Math.max(targetY - rootY, 20);
        var cp1X = rootX;
        var cp1Y = rootY + deltaY * 0.55;
        var cp2X = targetX;
        var cp2Y = targetY - deltaY * 0.45;

        var pathData = [
          'M', rootX, rootY,
          'C', cp1X, cp1Y, cp2X, cp2Y, targetX, targetY
        ].join(' ');

        var pathEl = tier1Paths[pid];
        if (!pathEl) {
          pathEl = document.createElementNS('http://www.w3.org/2000/svg', 'path');
          pathEl.setAttribute('id', 'tier1-path-' + pid);
          pathEl.setAttribute('class', 'vi-tree-stem-tier1 path-theme-' + pid);
          tier1Group.appendChild(pathEl);
          tier1Paths[pid] = pathEl;
        }

        pathEl.setAttribute('d', pathData);
      });

      // ── Draw Tier 2 Paths (6 Pillars ➔ 14 Subdivisions) ──────────────
      if (!isExpanded) {
        tier2Group.style.display = 'none';
        return;
      }
      tier2Group.style.display = 'block';

      subNodes.forEach(function (sub) {
        var sbid = sub.id;
        var pid = sub.getAttribute('data-pillar');
        var pillarPortBottom = document.getElementById('pillarPortBottom-' + pid);
        var subPortTop = document.getElementById('subPortTop-' + sbid);

        if (!pillarPortBottom || !subPortTop) return;

        var sourceRect = pillarPortBottom.getBoundingClientRect();
        var sourceX = sourceRect.left + sourceRect.width / 2 - canvasRect.left;
        var sourceY = sourceRect.top + sourceRect.height / 2 - canvasRect.top;

        var targetRect = subPortTop.getBoundingClientRect();
        var subTargetX = targetRect.left + targetRect.width / 2 - canvasRect.left;
        var subTargetY = targetRect.top + targetRect.height / 2 - canvasRect.top;

        var deltaSubY = Math.max(subTargetY - sourceY, 25);
        var scp1X = sourceX;
        var scp1Y = sourceY + deltaSubY * 0.55;
        var scp2X = subTargetX;
        var scp2Y = subTargetY - deltaSubY * 0.45;

        var subPathData = [
          'M', sourceX, sourceY,
          'C', scp1X, scp1Y, scp2X, scp2Y, subTargetX, subTargetY
        ].join(' ');

        var subPathEl = tier2Paths[sbid];
        if (!subPathEl) {
          subPathEl = document.createElementNS('http://www.w3.org/2000/svg', 'path');
          subPathEl.setAttribute('id', 'tier2-path-' + sbid);
          subPathEl.setAttribute('class', 'vi-tree-stem-tier2 path-theme-' + pid);
          tier2Group.appendChild(subPathEl);
          tier2Paths[sbid] = subPathEl;
        }

        subPathEl.setAttribute('d', subPathData);
      });
    }

    var resizeTimer = null;
    function scheduleRedraw() {
      if (window.requestAnimationFrame) {
        window.requestAnimationFrame(renderSvgBranches);
      } else {
        renderSvgBranches();
      }
    }

    window.addEventListener('resize', function () {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(scheduleRedraw, 50);
    });

    /* ── 2. Integrated Root Toggle Button ────────────────────────────── */
    function toggleAllBranches() {
      isExpanded = !isExpanded;

      if (isExpanded) {
        if (level2Container) level2Container.classList.remove('is-collapsed');
        if (rootToggle) rootToggle.setAttribute('aria-expanded', 'true');
        if (toggleIcon) toggleIcon.textContent = '⊟';
        if (toggleText) toggleText.textContent = 'Collapse All';
      } else {
        if (level2Container) level2Container.classList.add('is-collapsed');
        if (rootToggle) rootToggle.setAttribute('aria-expanded', 'false');
        if (toggleIcon) toggleIcon.textContent = '⊞';
        if (toggleText) toggleText.textContent = 'Expand All';
      }

      scheduleRedraw();
      setTimeout(scheduleRedraw, 50);
      setTimeout(scheduleRedraw, 200);
    }

    if (rootToggle) {
      rootToggle.addEventListener('click', function (e) {
        e.stopPropagation();
        toggleAllBranches();
      });
    }

    /* ── 3. Lineage Path Illumination ───────────────────────────────── */
    function setupLineage() {
      var leafNodes = document.querySelectorAll('.vi-tree-leaf-mini');
      leafNodes.forEach(function (leaf) {
        var pid = leaf.getAttribute('data-pillar');
        var subnode = leaf.closest('.vi-tree-subdivision-node');
        var sbid = subnode ? subnode.id : '';

        function activate() {
          leaf.classList.add('is-lineage-active');
          if (subnode) subnode.classList.add('is-lineage-active');
          var col = document.getElementById('pillarCol-' + pid);
          if (col) col.classList.add('is-lineage-active');
          if (rootNode) rootNode.classList.add('is-lineage-active');
          if (tier1Paths[pid]) tier1Paths[pid].classList.add('is-lineage-active');
          if (tier2Paths[sbid]) tier2Paths[sbid].classList.add('is-lineage-active');
        }

        function deactivate() {
          leaf.classList.remove('is-lineage-active');
          if (subnode) subnode.classList.remove('is-lineage-active');
          var col = document.getElementById('pillarCol-' + pid);
          if (col) col.classList.remove('is-lineage-active');
          if (rootNode) rootNode.classList.remove('is-lineage-active');
          if (tier1Paths[pid]) tier1Paths[pid].classList.remove('is-lineage-active');
          if (tier2Paths[sbid]) tier2Paths[sbid].classList.remove('is-lineage-active');
        }

        leaf.addEventListener('mouseenter', activate);
        leaf.addEventListener('mouseleave', deactivate);
        leaf.addEventListener('focus', activate);
        leaf.addEventListener('blur', deactivate);

        // Tooltip
        if (tooltip && tooltipBadge && tooltipTitle && tooltipSummary) {
          leaf.addEventListener('mouseenter', function () {
            var titleText = leaf.querySelector('.leaf-name') ? leaf.querySelector('.leaf-name').textContent : leaf.textContent;
            var summaryText = leaf.getAttribute('data-summary') || '';
            var categoryText = subnode ? (subnode.querySelector('.subdivision-title') ? subnode.querySelector('.subdivision-title').textContent : 'Resource') : 'Resource';

            tooltipTitle.textContent = titleText.trim();
            tooltipBadge.textContent = categoryText;
            tooltipSummary.textContent = summaryText;

            var leafRect = leaf.getBoundingClientRect();
            var canvasRect = canvas.getBoundingClientRect();
            var tooltipX = leafRect.left + leafRect.width / 2 - canvasRect.left;
            var tooltipY = leafRect.top - canvasRect.top - 12;

            tooltip.style.left = tooltipX + 'px';
            tooltip.style.top = tooltipY + 'px';
            tooltip.classList.add('is-visible');
          });

          leaf.addEventListener('mouseleave', function () {
            tooltip.classList.remove('is-visible');
          });
        }
      });
    }

    setupLineage();

    // Initial render
    setTimeout(renderSvgBranches, 100);
    setTimeout(renderSvgBranches, 350);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPyramidTree);
  } else {
    initPyramidTree();
  }
})();
