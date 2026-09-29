document.addEventListener("DOMContentLoaded", () => {
  const feed = document.querySelector("[data-homefeed]");
  if (!feed) return;

  const formatCard = (item) => `
    <a class="latest-card" href="${item.url}">
      <span class="card-meta">${item.type}</span>
      <h3>${item.title}</h3>
      <p>${item.summary}</p>
      <span class="home-card-link">Open publication →</span>
    </a>`;

  fetch("/content/homepage.json", { cache: "no-cache" })
    .then((response) => {
      if (!response.ok) throw new Error(`Homepage feed HTTP ${response.status}`);
      return response.json();
    })
    .then((data) => {
      const latest = Array.isArray(data.latest) ? data.latest.slice(0, 2) : [];
      if (!latest.length) return;
      feed.innerHTML = latest.map(formatCard).join("");

      const featured = data.featured;
      if (!featured) return;
      const feature = document.querySelector("[data-featured-publication]");
      if (!feature) return;
      feature.querySelector("[data-feature-type]").textContent = `${featured.type} · ${featured.id} · ${featured.date}`;
      feature.querySelector("[data-feature-title]").textContent = featured.title;
      feature.querySelector("[data-feature-summary]").textContent = featured.summary;
      feature.querySelector("[data-feature-link]").href = featured.url;
      feature.querySelector("[data-feature-download]").href = featured.download;
    })
    .catch(() => {
      // Static semantic fallback in index.html remains visible.
    });
});
