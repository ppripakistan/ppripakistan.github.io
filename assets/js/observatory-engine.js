/**
 * assets/js/observatory-engine.js
 * PPRI Pakistan Data Observatory - Zero-Dependency Interactive Visualization & UX Engine
 * Ultra-lightweight (~10KB), pure SVG rendering, accessible tables, instant citations & exports.
 */

(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.PPRIObservatory = factory();
  }
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var engine = {};

  // Helper: Number formatting with commas
  engine.formatNumber = function (num) {
    if (num === null || num === undefined || isNaN(num)) return '—';
    var parts = num.toString().split('.');
    parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    return parts.join('.');
  };

  // Helper: Format large Pakistani numbers into Lakhs / Crores / Millions
  engine.formatPakistaniUnits = function (num, unitType) {
    if (!num || isNaN(num)) return '—';
    var n = parseFloat(num);
    if (unitType === 'crore') {
      return (n / 10000000).toFixed(2) + ' Crore';
    }
    if (n >= 1000000) {
      return (n / 1000000).toFixed(2) + ' Million';
    }
    if (n >= 100000) {
      return (n / 100000).toFixed(2) + ' Lakh';
    }
    return engine.formatNumber(n);
  };

  // Helper: Tooltip management
  var tooltipEl = null;
  function getTooltip() {
    if (!tooltipEl) {
      tooltipEl = document.createElement('div');
      tooltipEl.className = 'obs-chart-tooltip';
      tooltipEl.style.opacity = '0';
      document.body.appendChild(tooltipEl);
    }
    return tooltipEl;
  }

  function showTooltip(e, html) {
    var tip = getTooltip();
    tip.innerHTML = html;
    tip.style.opacity = '1';
    var x = e.pageX + 12;
    var y = e.pageY - 28;
    if (x + tip.offsetWidth > window.innerWidth - 20) {
      x = e.pageX - tip.offsetWidth - 12;
    }
    tip.style.left = x + 'px';
    tip.style.top = y + 'px';
  }

  function hideTooltip() {
    if (tooltipEl) {
      tooltipEl.style.opacity = '0';
    }
  }

  /**
   * Render Vertical Bar Chart (Pure SVG)
   * container: HTMLElement or selector string
   * data: array of { label: string, value: number, formattedValue?: string, subtext?: string, color?: string }
   */
  engine.renderBarChart = function (container, data, options) {
    var el = typeof container === 'string' ? document.querySelector(container) : container;
    if (!el || !data || !data.length) return;

    options = options || {};
    var height = options.height || 320;
    var width = options.width || 700;
    var padding = { top: 30, right: 20, bottom: 50, left: 60 };
    var chartW = width - padding.left - padding.right;
    var chartH = height - padding.top - padding.bottom;

    var maxVal = Math.max.apply(null, data.map(function (d) { return d.value; }));
    if (maxVal <= 0) maxVal = 1;
    maxVal = maxVal * 1.15; // 15% headroom for top labels

    var barWidth = Math.min(54, (chartW / data.length) * 0.65);
    var barStep = chartW / data.length;

    var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', '0 0 ' + width + ' ' + height);
    svg.setAttribute('class', 'obs-svg-chart');
    svg.setAttribute('role', 'img');
    svg.setAttribute('aria-label', options.title || 'Data Chart');

    // Grid lines & Y Axis ticks (4 horizontal steps)
    for (var i = 0; i <= 4; i++) {
      var yRatio = i / 4;
      var yPos = padding.top + chartH - (yRatio * chartH);
      var tickVal = (maxVal * yRatio);

      var line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      line.setAttribute('x1', padding.left);
      line.setAttribute('y1', yPos);
      line.setAttribute('x2', width - padding.right);
      line.setAttribute('y2', yPos);
      line.setAttribute('stroke', '#e2e8f0');
      line.setAttribute('stroke-dasharray', i === 0 ? 'none' : '3,3');
      svg.appendChild(line);

      var tickLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      tickLabel.setAttribute('x', padding.left - 8);
      tickLabel.setAttribute('y', yPos + 4);
      tickLabel.setAttribute('text-anchor', 'end');
      tickLabel.setAttribute('font-size', '11');
      tickLabel.setAttribute('fill', '#94a3b8');
      tickLabel.textContent = options.yFormat ? options.yFormat(tickVal) : engine.formatNumber(Math.round(tickVal));
      svg.appendChild(tickLabel);
    }

    // Render Bars
    data.forEach(function (d, idx) {
      var barH = (d.value / maxVal) * chartH;
      var x = padding.left + (idx * barStep) + (barStep - barWidth) / 2;
      var y = padding.top + chartH - barH;
      var barColor = d.color || options.barColor || '#073c3a';

      // Bar rect
      var rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rect.setAttribute('x', x);
      rect.setAttribute('y', y);
      rect.setAttribute('width', barWidth);
      rect.setAttribute('height', barH);
      rect.setAttribute('rx', '4');
      rect.setAttribute('fill', barColor);
      rect.style.transition = 'opacity 0.15s, fill 0.15s';
      rect.style.cursor = 'pointer';

      // Hover events
      rect.addEventListener('mouseenter', function (e) {
        rect.setAttribute('fill', '#0d5c59');
        var tipText = '<strong>' + d.label + '</strong><br>' +
                      (d.formattedValue || engine.formatNumber(d.value)) +
                      (d.subtext ? '<br><small style="color:#94a3b8">' + d.subtext + '</small>' : '');
        showTooltip(e, tipText);
      });
      rect.addEventListener('mousemove', function (e) {
        var tipText = '<strong>' + d.label + '</strong><br>' +
                      (d.formattedValue || engine.formatNumber(d.value)) +
                      (d.subtext ? '<br><small style="color:#94a3b8">' + d.subtext + '</small>' : '');
        showTooltip(e, tipText);
      });
      rect.addEventListener('mouseleave', function () {
        rect.setAttribute('fill', barColor);
        hideTooltip();
      });

      svg.appendChild(rect);

      // Top Value Label
      var topLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      topLabel.setAttribute('x', x + barWidth / 2);
      topLabel.setAttribute('y', y - 8);
      topLabel.setAttribute('text-anchor', 'middle');
      topLabel.setAttribute('font-size', '12');
      topLabel.setAttribute('font-weight', '700');
      topLabel.setAttribute('fill', '#1e293b');
      topLabel.textContent = d.formattedValue || engine.formatNumber(d.value);
      svg.appendChild(topLabel);

      // Bottom Category Label
      var catLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      catLabel.setAttribute('x', x + barWidth / 2);
      catLabel.setAttribute('y', padding.top + chartH + 20);
      catLabel.setAttribute('text-anchor', 'middle');
      catLabel.setAttribute('font-size', '12');
      catLabel.setAttribute('font-weight', '600');
      catLabel.setAttribute('fill', '#475569');
      catLabel.textContent = d.label;
      svg.appendChild(catLabel);
    });

    el.innerHTML = '';
    el.appendChild(svg);
  };

  /**
   * Render Horizontal Ranked Bar Chart (Ideal for Cities or Categorical Shares)
   * container: HTMLElement or selector string
   * data: array of { label: string, value: number, formattedValue?: string, subtext?: string, color?: string }
   */
  engine.renderHorizontalBarChart = function (container, data, options) {
    var el = typeof container === 'string' ? document.querySelector(container) : container;
    if (!el || !data || !data.length) return;

    options = options || {};
    var itemHeight = 36;
    var padding = { top: 20, right: 80, bottom: 20, left: 140 };
    var height = padding.top + padding.bottom + (data.length * itemHeight);
    var width = options.width || 700;
    var chartW = width - padding.left - padding.right;

    var maxVal = Math.max.apply(null, data.map(function (d) { return d.value; }));
    if (maxVal <= 0) maxVal = 1;

    var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('viewBox', '0 0 ' + width + ' ' + height);
    svg.setAttribute('class', 'obs-svg-chart');
    svg.setAttribute('role', 'img');

    data.forEach(function (d, idx) {
      var y = padding.top + (idx * itemHeight);
      var barW = (d.value / maxVal) * chartW;
      var barColor = d.color || options.barColor || '#073c3a';

      // Left Label
      var label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      label.setAttribute('x', padding.left - 12);
      label.setAttribute('y', y + 16);
      label.setAttribute('text-anchor', 'end');
      label.setAttribute('font-size', '12');
      label.setAttribute('font-weight', '600');
      label.setAttribute('fill', '#334155');
      label.textContent = d.label;
      svg.appendChild(label);

      // Background Track
      var track = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      track.setAttribute('x', padding.left);
      track.setAttribute('y', y + 2);
      track.setAttribute('width', chartW);
      track.setAttribute('height', 20);
      track.setAttribute('rx', '4');
      track.setAttribute('fill', '#f1f5f9');
      svg.appendChild(track);

      // Filled Bar
      var rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rect.setAttribute('x', padding.left);
      rect.setAttribute('y', y + 2);
      rect.setAttribute('width', Math.max(4, barW));
      rect.setAttribute('height', 20);
      rect.setAttribute('rx', '4');
      rect.setAttribute('fill', barColor);
      rect.style.cursor = 'pointer';

      rect.addEventListener('mouseenter', function (e) {
        rect.setAttribute('fill', '#0d5c59');
        var tipText = '<strong>' + d.label + '</strong><br>' +
                      (d.formattedValue || engine.formatNumber(d.value)) +
                      (d.subtext ? '<br><small style="color:#94a3b8">' + d.subtext + '</small>' : '');
        showTooltip(e, tipText);
      });
      rect.addEventListener('mousemove', function (e) {
        var tipText = '<strong>' + d.label + '</strong><br>' +
                      (d.formattedValue || engine.formatNumber(d.value)) +
                      (d.subtext ? '<br><small style="color:#94a3b8">' + d.subtext + '</small>' : '');
        showTooltip(e, tipText);
      });
      rect.addEventListener('mouseleave', function () {
        rect.setAttribute('fill', barColor);
        hideTooltip();
      });

      svg.appendChild(rect);

      // Right Value Label
      var valLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      valLabel.setAttribute('x', padding.left + barW + 8);
      valLabel.setAttribute('y', y + 16);
      valLabel.setAttribute('font-size', '12');
      valLabel.setAttribute('font-weight', '700');
      valLabel.setAttribute('fill', '#1e293b');
      valLabel.textContent = d.formattedValue || engine.formatNumber(d.value);
      svg.appendChild(valLabel);
    });

    el.innerHTML = '';
    el.appendChild(svg);
  };

  /**
   * Sortable Data Table Setup
   * tableId: HTML table element id
   */
  engine.setupTableSort = function (tableId) {
    var table = document.getElementById(tableId);
    if (!table) return;

    var headers = table.querySelectorAll('th.sortable');
    headers.forEach(function (th, colIdx) {
      th.addEventListener('click', function () {
        var tbody = table.querySelector('tbody');
        var rows = Array.prototype.slice.call(tbody.querySelectorAll('tr'));
        var isAsc = th.getAttribute('data-order') === 'asc';
        var nextOrder = isAsc ? 'desc' : 'asc';

        headers.forEach(function (h) {
          h.removeAttribute('data-order');
          var arrow = h.querySelector('.sort-arrow');
          if (arrow) arrow.textContent = '⇅';
        });

        th.setAttribute('data-order', nextOrder);
        var curArrow = th.querySelector('.sort-arrow');
        if (curArrow) curArrow.textContent = nextOrder === 'asc' ? '▲' : '▼';

        rows.sort(function (rowA, rowB) {
          var cellA = rowA.children[colIdx].innerText.trim().replace(/[%,]/g, '');
          var cellB = rowB.children[colIdx].innerText.trim().replace(/[%,]/g, '');
          var numA = parseFloat(cellA);
          var numB = parseFloat(cellB);

          if (!isNaN(numA) && !isNaN(numB)) {
            return nextOrder === 'asc' ? numA - numB : numB - numA;
          }
          return nextOrder === 'asc' ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA);
        });

        rows.forEach(function (r) { tbody.appendChild(r); });
      });
    });
  };

  /**
   * Instant Client-side Table Search/Filter
   */
  engine.setupTableSearch = function (inputId, tableId) {
    var input = document.getElementById(inputId);
    var table = document.getElementById(tableId);
    if (!input || !table) return;

    input.addEventListener('input', function () {
      var query = input.value.toLowerCase().trim();
      var rows = table.querySelectorAll('tbody tr');
      rows.forEach(function (row) {
        var text = row.textContent.toLowerCase();
        row.style.display = text.indexOf(query) !== -1 ? '' : 'none';
      });
    });
  };

  /**
   * One-click Copy Citation to Clipboard
   */
  engine.copyCitation = function (citationText, btn) {
    navigator.clipboard.writeText(citationText).then(function () {
      var origText = btn.innerHTML;
      btn.innerHTML = '✓ Copied Citation!';
      btn.classList.add('obs-btn-primary');
      setTimeout(function () {
        btn.innerHTML = origText;
        btn.classList.remove('obs-btn-primary');
      }, 2500);
    }).catch(function () {
      prompt('Copy citation manually:', citationText);
    });
  };

  /**
   * Export Table to CSV
   */
  engine.exportTableToCSV = function (tableId, filename) {
    var table = document.getElementById(tableId);
    if (!table) return;

    var csv = [];
    var rows = table.querySelectorAll('tr');
    rows.forEach(function (row) {
      if (row.style.display === 'none') return; // skip filtered rows
      var cols = row.querySelectorAll('th, td');
      var rowData = [];
      cols.forEach(function (col) {
        var text = col.innerText.replace(/"/g, '""').replace(/⇅|▲|▼/g, '').trim();
        rowData.push('"' + text + '"');
      });
      csv.push(rowData.join(','));
    });

    var blob = new Blob([csv.join('\n')], { type: 'text/csv;charset=utf-8;' });
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.setAttribute('download', filename || 'ppri_data_export.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return engine;
});
