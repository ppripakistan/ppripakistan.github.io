document.addEventListener("DOMContentLoaded", () => {
  const b = document.querySelector(".menu-toggle"),
    n = document.querySelector(".nav-links");
  if (b && n) {
    b.addEventListener("click", () => {
      const o = n.classList.toggle("is-open");
      b.setAttribute("aria-expanded", String(o));
    });
    n.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => {
        n.classList.remove("is-open");
        b.setAttribute("aria-expanded", "false");
      }),
    );
  }
  document
    .querySelectorAll("[data-current-year]")
    .forEach((e) => (e.textContent = new Date().getFullYear()));
});
