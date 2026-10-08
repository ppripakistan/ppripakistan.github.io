document.addEventListener("DOMContentLoaded", () => {
  const bar = document.getElementById("reading-progress");
  const pill = document.getElementById("articleProgressPill");
  const pctSpan = pill ? pill.querySelector(".article-pct") : null;
  if (!bar && !pill) return;

  const update = () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const progress = scrollable > 0 ? Math.min(100, Math.max(0, Math.round((window.scrollY / scrollable) * 100))) : 0;
    if (bar) bar.style.width = `${progress}%`;
    if (pctSpan) pctSpan.textContent = `${progress}%`;
    if (pill) {
      pill.classList.toggle("is-visible", window.scrollY > 150);
    }
  };

  window.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update, { passive: true });
  update();
});
