(function () {
  const i = document.querySelector("[data-search]"),
    b = document.querySelector("[data-results]");
  if (!i || !b) return;
  const params = new URLSearchParams(window.location.search);
  const initialQ = params.get("q") || "";
  if (initialQ) i.value = initialQ;

  const isUrdu = document.documentElement.lang === "ur" || window.location.pathname.startsWith("/ur/");

  let idx = [];

  function normalizeUrdu(str) {
    if (!str) return "";
    return String(str)
      .toLowerCase()
      .replace(/[يى]/g, "ی")
      .replace(/[ك]/g, "ک")
      .replace(/[ة]/g, "ہ")
      .replace(/[ؤ]/g, "و")
      .replace(/[\u064B-\u065F]/g, "") // strip harakat
      .trim();
  }

  // Load primary search index, and merge with Urdu index
  Promise.all([
    fetch("/search-index.json").then((r) => r.json()).catch(() => []),
    fetch("/search-index-ur.json").then((r) => r.json()).catch(() => [])
  ])
    .then(([mainIndex, urduIndex]) => {
      // Put language-relevant index first
      idx = isUrdu ? [...urduIndex, ...mainIndex] : [...mainIndex, ...urduIndex];
      render(i.value || "");
    })
    .catch((err) => {
      console.warn("Unable to load search indices:", err);
      b.innerHTML = isUrdu
        ? "<div class='callout'>تلاش کا ڈیٹا لوڈ نہیں ہو سکا۔ برائے مہربانی صفحہ ریفریش کریں۔</div>"
        : "<div class='callout'>Unable to load search index. Please try again.</div>";
    });

  function escapeHTML(str) {
    if (!str) return "";
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function render(q) {
    const rawQ = q.trim();
    const hasUrdu = /[\u0600-\u06FF]/.test(rawQ);

    let rows = [];

    if (!rawQ) {
      // Default initial display (empty query)
      rows = isUrdu
        ? idx.filter((x) => (x.url || "").startsWith("/ur/")).slice(0, 12)
        : idx.filter((x) => !(x.url || "").startsWith("/ur/")).slice(0, 12);
    } else {
      // Tokenize search terms for multi-word matching
      const normalizedQuery = hasUrdu ? normalizeUrdu(rawQ) : rawQ.toLowerCase();
      const terms = normalizedQuery.split(/\s+/).filter(Boolean);

      // On English pages without Urdu query, exclude /ur/ cards to keep results clean
      const candidateList = (!isUrdu && !hasUrdu)
        ? idx.filter((x) => !(x.url || "").startsWith("/ur/"))
        : (isUrdu && hasUrdu ? idx.filter((x) => (x.url || "").startsWith("/ur/")) : idx);

      const scored = [];

      for (const item of candidateList) {
        const title = hasUrdu ? normalizeUrdu(item.title || "") : (item.title || "").toLowerCase();
        const type = hasUrdu ? normalizeUrdu(item.type || "") : (item.type || "").toLowerCase();
        const tags = hasUrdu ? normalizeUrdu((item.tags || []).join(" ")) : (item.tags || []).join(" ").toLowerCase();
        const desc = hasUrdu ? normalizeUrdu(item.description || item.text || "") : (item.description || item.text || "").toLowerCase();
        const fullHaystack = `${title} ${type} ${tags} ${desc}`;

        // Every search term must match somewhere in the entry
        const allTermsMatch = terms.every((t) => fullHaystack.includes(t));
        if (!allTermsMatch) continue;

        // Calculate relevance score
        let score = 0;

        // Exact phrase match in title
        if (title.includes(normalizedQuery)) score += 100;
        // Exact phrase match in tags or type
        if (tags.includes(normalizedQuery)) score += 40;
        if (type.includes(normalizedQuery)) score += 30;
        if (desc.includes(normalizedQuery)) score += 20;

        // Individual term occurrences
        for (const t of terms) {
          if (title.includes(t)) score += 25;
          if (tags.includes(t)) score += 15;
          if (type.includes(t)) score += 10;
          if (desc.includes(t)) score += 5;
        }

        // Title begins with first query term boost
        if (terms.length > 0 && title.startsWith(terms[0])) score += 15;

        scored.push({ item, score });
      }

      // Sort descending by score
      scored.sort((a, b) => b.score - a.score);
      rows = scored.map((s) => s.item);
    }

    const noResultsMsg = isUrdu
      ? "<div class='callout'>اس تلاش سے مطابقت رکھنے والا کوئی مواد دستیاب نہیں ہے۔</div>"
      : "<div class='callout'>No matching PPRI material was found.</div>";

    b.innerHTML =
      rows
        .map((x) => {
          const typeBadge = x.type ? `<span class="card-meta">${escapeHTML(x.type)}</span>` : "";
          const descText = x.description || x.text || "";
          return `<a class="card card-link" href="${escapeHTML(x.url)}">${typeBadge}<h3>${escapeHTML(x.title)}</h3>${descText ? `<p>${escapeHTML(descText)}</p>` : ""}</a>`;
        })
        .join("") || noResultsMsg;
  }

  i.addEventListener("input", () => render(i.value));
})();
