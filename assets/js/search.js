(function () {
  const i = document.querySelector("[data-search]"),
    b = document.querySelector("[data-results]");
  if (!i || !b) return;
  const params = new URLSearchParams(window.location.search);
  const initialQ = params.get("q") || "";
  if (initialQ) i.value = initialQ;

  let idx = [];
  fetch("/search-index.json")
    .then((r) => r.json())
    .then((d) => {
      idx = d;
      render(i.value || "");
    })
    .catch((err) => {
      console.warn("Unable to load search index:", err);
      b.innerHTML = "<div class='callout'>Unable to load search index. Please try again.</div>";
    });

  function render(q) {
    q = q.trim().toLowerCase();
    const rows = q
      ? idx.filter((x) => {
          const searchable = [
            x.title || "",
            x.type || "",
            x.description || "",
            x.text || "",
            (x.tags || []).join(" ")
          ].join(" ").toLowerCase();
          return searchable.includes(q);
        })
      : idx.slice(0, 12);

    b.innerHTML =
      rows
        .map((x) => {
          const typeBadge = x.type ? `<span class="card-meta">${x.type}</span>` : "";
          const descText = x.description || x.text || "";
          return `<a class="card card-link" href="${x.url}">${typeBadge}<h3>${x.title}</h3>${descText ? `<p>${descText}</p>` : ""}</a>`;
        })
        .join("") ||
      "<div class='callout'>No matching PPRI material was found.</div>";
  }
  i.addEventListener("input", () => render(i.value));
})();
