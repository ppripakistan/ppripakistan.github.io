/**
 * assets/js/research-papers.js
 * Enhanced interactivity for PPRI Research Reports:
 * - Connected bullet stepper rail with active scroll-spy
 * - Reading progress percentage & back-to-top quick jump
 * - Mobile floating action button & slide-up chapters drawer
 * - Citation copy button feedback
 * - Expandable source cards
 */

document.addEventListener("DOMContentLoaded", () => {
  // 1. Reading Progress & Percentage
  const progressBar = document.getElementById("reading-progress");
  const progressPills = document.querySelectorAll(".toc-progress-pill, .mobile-toc-fab .toc-pct");

  const updateProgress = () => {
    const scrollable = document.documentElement.scrollHeight - window.innerHeight;
    const progress = scrollable > 0 ? Math.min(100, Math.max(0, Math.round((window.scrollY / scrollable) * 100))) : 0;
    if (progressBar) progressBar.style.width = `${progress}%`;
    progressPills.forEach((pill) => {
      pill.textContent = `${progress}%`;
    });
  };

  window.addEventListener("scroll", updateProgress, { passive: true });
  window.addEventListener("resize", updateProgress, { passive: true });
  updateProgress();

  // 2. Back-to-Top Button
  const topButtons = document.querySelectorAll(".toc-top-btn");
  topButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });

  // 3. Active Chapter Scroll-Spy
  const headings = Array.from(document.querySelectorAll("article.prose-wide h2[id], article.prose-wide h3[id]"));
  const tocItems = Array.from(document.querySelectorAll(".toc-stepper-list .toc-item"));
  const tocLinks = Array.from(document.querySelectorAll(".toc-link, .mobile-toc-sheet .toc-link"));
  const tocContainer = document.querySelector(".toc");

  if (headings.length && (tocItems.length || tocLinks.length)) {
    let activeId = "";

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            activeId = entry.target.id;
          }
        });

        if (activeId) {
          tocItems.forEach((item) => {
            const link = item.querySelector("a");
            const isActive = link && link.getAttribute("href") === `#${activeId}`;
            item.classList.toggle("is-active", isActive);
            if (isActive && tocContainer) {
              // Ensure active item stays in visible region of the sticky sidebar without affecting window scroll
              const itemTop = item.offsetTop - tocContainer.offsetTop;
              const viewTop = tocContainer.scrollTop;
              const viewBottom = viewTop + tocContainer.clientHeight;
              if (itemTop < viewTop || itemTop > viewBottom - 40) {
                tocContainer.scrollTop = Math.max(0, itemTop - 60);
              }
            }
          });

          // Also highlight mobile drawer links if open
          document.querySelectorAll(".mobile-toc-sheet .toc-item").forEach((item) => {
            const link = item.querySelector("a");
            item.classList.toggle("is-active", Boolean(link && link.getAttribute("href") === `#${activeId}`));
          });
        }
      },
      {
        rootMargin: "-12% 0px -65% 0px",
        threshold: 0,
      }
    );

    headings.forEach((h) => observer.observe(h));
  }

  // 4. Mobile Drawer Controller
  const fab = document.querySelector(".mobile-toc-fab");
  const drawer = document.querySelector(".mobile-toc-drawer");
  const closeBtn = document.querySelector(".mobile-sheet-close");
  const backdrop = document.querySelector(".mobile-toc-backdrop");
  const mobileLinks = document.querySelectorAll(".mobile-toc-sheet .toc-link");

  const openDrawer = () => {
    if (!drawer) return;
    drawer.classList.add("is-open");
    drawer.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  };

  const closeDrawer = () => {
    if (!drawer) return;
    drawer.classList.remove("is-open");
    drawer.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  };

  if (fab) fab.addEventListener("click", openDrawer);
  if (closeBtn) closeBtn.addEventListener("click", closeDrawer);
  if (backdrop) backdrop.addEventListener("click", closeDrawer);

  mobileLinks.forEach((link) => {
    link.addEventListener("click", () => {
      closeDrawer();
    });
  });

  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && drawer && drawer.classList.contains("is-open")) {
      closeDrawer();
    }
  });

  // 5. Citation Copy with Visual Confirmation
  const copyBtn = document.querySelector(".citation-copy-btn");
  if (copyBtn) {
    copyBtn.addEventListener("click", () => {
      const citationTextEl = document.querySelector(".citation-text");
      if (!citationTextEl) return;
      const text = citationTextEl.innerText.replace("Copy Citation", "").trim();
      navigator.clipboard.writeText(text).then(() => {
        const originalText = copyBtn.innerText;
        copyBtn.innerText = "✓ Copied!";
        copyBtn.classList.add("copied");
        setTimeout(() => {
          copyBtn.innerText = originalText;
          copyBtn.classList.remove("copied");
        }, 2500);
      });
    });
  }

  // 6. Source Card Accordion Toggles
  document.querySelectorAll(".source-card-toggle").forEach((btn) => {
    btn.addEventListener("click", function () {
      const card = this.closest(".source-card");
      if (!card) return;
      const body = card.querySelector(".source-card-body");
      if (!body) return;
      const isExpanded = this.getAttribute("aria-expanded") === "true";
      this.setAttribute("aria-expanded", String(!isExpanded));
      card.classList.toggle("open", !isExpanded);
      body.style.display = isExpanded ? "none" : "block";
    });
  });
});
