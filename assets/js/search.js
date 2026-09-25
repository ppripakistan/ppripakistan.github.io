(function () {
  const i = document.querySelector("[data-search]"),
    b = document.querySelector("[data-results]");
  if (!i || !b) return;
  let idx = [];
  fetch("/search-index.json")
    .then((r) => r.json())
    .then((d) => {
      idx = d;
      render("");
    });
  function render(q) {
    q = q.trim().toLowerCase();
    const rows = q
      ? idx.filter((x) =>
          (x.title + " " + x.description + " " + (x.tags || []).join(" "))
            .toLowerCase()
            .includes(q),
        )
      : idx.slice(0, 12);
    b.innerHTML =
      rows
        .map(
          (x) =>
            `<a class="card card-link" href="${x.url}"><span class="card-meta">${x.type}</span><h3>${x.title}</h3><p>${x.description}</p></a>`,
        )
        .join("") ||
      "<div class='callout'>No matching PPRI material was found.</div>";
  }
  i.addEventListener("input", () => render(i.value));
})();
