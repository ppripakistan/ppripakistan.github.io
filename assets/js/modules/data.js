(function () {
  window.PPRI = window.PPRI || {};
  PPRI.fmtNumber = (n) => Number(n).toLocaleString("en-US");
  PPRI.populateTable = (s, rows) => {
    const t = document.querySelector(s);
    if (!t) return;
    const b = t.querySelector("tbody");
    b.innerHTML = "";
    rows.forEach((r) => {
      const tr = document.createElement("tr");
      [
        r.name,
        PPRI.fmtNumber(r.population_2023),
        r.share_percent + "%",
        "PBS Census 2023",
      ].forEach((v) => {
        const td = document.createElement("td");
        td.textContent = v;
        tr.appendChild(td);
      });
      b.appendChild(tr);
    });
  };
  PPRI.barChart = (id, labels, values, title) => {
    const c = document.getElementById(id);
    if (!c) return;
    const x = c.getContext("2d"),
      d = devicePixelRatio || 1,
      w = c.clientWidth * d,
      h = 330 * d;
    c.width = w;
    c.height = h;
    const max = Math.max(...values),
      pad = 50 * d,
      gap = 18 * d,
      bw = Math.max(
        20 * d,
        (w - pad * 2 - gap * (values.length - 1)) / values.length,
      );
    x.clearRect(0, 0, w, h);
    x.font = `${12 * d}px system-ui`;
    x.fillStyle = "#17232d";
    x.strokeStyle = "#dce3e8";
    [0, 0.25, 0.5, 0.75, 1].forEach((t) => {
      let y = h - pad - t * (h - pad * 2);
      x.beginPath();
      x.moveTo(pad, y);
      x.lineTo(w - pad, y);
      x.stroke();
      x.fillText(((max * t) / 1e6).toFixed(0) + "m", 5 * d, y + 4 * d);
    });
    values.forEach((v, i) => {
      let bh = (v / max) * (h - pad * 2),
        xx = pad + i * (bw + gap),
        y = h - pad - bh;
      x.fillStyle = "#b08a49";
      x.fillRect(xx, y, bw, bh);
      x.fillStyle = "#17232d";
      x.save();
      x.translate(xx + bw / 2, h - pad + 19 * d);
      x.rotate(-Math.PI / 7);
      x.textAlign = "right";
      x.fillText(labels[i], 0, 0);
      x.restore();
    });
    x.fillStyle = "#17232d";
    x.font = `700 ${13 * d}px system-ui`;
    x.fillText(title, pad, 18 * d);
  };
})();
