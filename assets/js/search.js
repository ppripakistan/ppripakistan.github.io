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

  // Load primary search index, and merge with Urdu index if available
  Promise.all([
    fetch("/search-index.json").then((r) => r.json()).catch(() => []),
    fetch("/search-index-ur.json").then((r) => r.json()).catch(() => [])
  ])
    .then(([mainIndex, urduIndex]) => {
      idx = [...urduIndex, ...mainIndex];
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
    const normalizedQ = hasUrdu ? normalizeUrdu(rawQ) : rawQ.toLowerCase();

    const rows = rawQ
      ? idx.filter((x) => {
          const searchable = [
            x.title || "",
            x.type || "",
            x.description || "",
            x.text || "",
            (x.tags || []).join(" ")
          ].join(" ");

          const target = hasUrdu ? normalizeUrdu(searchable) : searchable.toLowerCase();
          return target.includes(normalizedQ);
        })
      : (isUrdu ? idx.filter(x => (x.url || "").startsWith("/ur/")).slice(0, 12) : idx.slice(0, 12));

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
