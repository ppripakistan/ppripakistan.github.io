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

  // 3. Active Chapter Scroll-Spy & Smart Auto-Centering TOC Engine
  const headings = Array.from(document.querySelectorAll("article.prose-wide h2[id], article.prose-wide h3[id]"));
  const desktopItems = Array.from(document.querySelectorAll(".toc .toc-stepper-list .toc-item"));
  const mobileItems = Array.from(document.querySelectorAll(".mobile-toc-sheet .toc-item"));
  const tocContainer = document.querySelector(".toc");
  const mobileSheetBody = document.querySelector(".mobile-sheet-body");

  if (headings.length && (desktopItems.length || mobileItems.length)) {
    let activeId = "";
    let isUserManualScrolling = false;
    let manualScrollTimer = null;





    // User manual mouse-wheel or touch detection with 2.5s grace period
    const registerManualInteraction = () => {
      isUserManualScrolling = true;
      clearTimeout(manualScrollTimer);
      manualScrollTimer = setTimeout(() => {
        isUserManualScrolling = false;
      }, 2500);
    };

    if (tocContainer) {
      tocContainer.addEventListener("wheel", registerManualInteraction, { passive: true });
      tocContainer.addEventListener("touchstart", registerManualInteraction, { passive: true });
    }

    // Robust Bounding-Box Auto-Centering inside scrollable TOC
    const autoCenterActiveItem = (item, container, force = false) => {
      if (!item || !container) return;
      if (isUserManualScrolling && !force) return;

      const itemRect = item.getBoundingClientRect();
      const containerRect = container.getBoundingClientRect();
      const headerEl = container.querySelector(".toc-stepper-header, .mobile-sheet-head");
      const headerHeight = headerEl ? headerEl.offsetHeight : 44;

      const visibleTop = containerRect.top + headerHeight + 10;
      const visibleBottom = containerRect.bottom - 14;

      // Only scroll when item is outside or approaching the boundary edges
      if (force || itemRect.top < visibleTop || itemRect.bottom > visibleBottom) {
        const relativeItemTop = itemRect.top - containerRect.top + container.scrollTop;
        const targetScrollTop = Math.max(0, relativeItemTop - (container.clientHeight / 2) + (itemRect.height / 2));

        container.scrollTo({
          top: targetScrollTop,
          behavior: "smooth"
        });
      }
    };

    const setActiveHeading = (id, forceScroll = false) => {
      if (!id) return;
      const hasChanged = id !== activeId;
      activeId = id;

      let activeDesktopItem = null;
      let activeIndex = -1;

      // Update Desktop TOC items
      desktopItems.forEach((item, idx) => {
        const link = item.querySelector("a");
        const isActive = link && link.getAttribute("href") === `#${activeId}`;
        item.classList.toggle("is-active", isActive);
        if (isActive) {
          activeDesktopItem = item;
          activeIndex = idx;
        }
      });



      // Smoothly auto-center active chapter inside desktop TOC
      if (activeDesktopItem && tocContainer) {
        autoCenterActiveItem(activeDesktopItem, tocContainer, forceScroll || hasChanged);
      }

      // Update Mobile Drawer items
      let activeMobileItem = null;
      mobileItems.forEach((item) => {
        const link = item.querySelector("a");
        const isActive = link && link.getAttribute("href") === `#${activeId}`;
        item.classList.toggle("is-active", isActive);
        if (isActive) activeMobileItem = item;
      });

      // Auto-center in mobile sheet if drawer is open
      if (activeMobileItem && mobileSheetBody) {
        autoCenterActiveItem(activeMobileItem, mobileSheetBody, forceScroll);
      }
    };

    // Continuous scroll detection: ensures current section is always highlighted accurately
    const updateActiveScrollSpy = () => {
      const topOffset = 160;
      let currentId = "";
      for (let i = 0; i < headings.length; i++) {
        const top = headings[i].getBoundingClientRect().top;
        if (top <= topOffset) {
          currentId = headings[i].id;
        } else {
          break;
        }
      }
      if (currentId) {
        setActiveHeading(currentId);
      }
    };

    window.addEventListener("scroll", updateActiveScrollSpy, { passive: true });
    updateActiveScrollSpy();

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setActiveHeading(entry.target.id);
          }
        });
      },
      {
        rootMargin: "-10% 0px -60% 0px",
        threshold: 0,
      }
    );

    headings.forEach((h) => observer.observe(h));

    // Smooth click handling: clicking a chapter link centers it immediately in the TOC
    document.querySelectorAll(".toc-link").forEach((link) => {
      link.addEventListener("click", () => {
        const href = link.getAttribute("href");
        if (href && href.startsWith("#")) {
          const targetId = href.slice(1);
          setTimeout(() => {
            setActiveHeading(targetId, true);
          }, 80);
        }
      });
    });
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
    setTimeout(() => {
      const activeMobile = document.querySelector(".mobile-toc-sheet .toc-item.is-active");
      const sheetBody = document.querySelector(".mobile-sheet-body");
      if (activeMobile && sheetBody) {
        const itemRect = activeMobile.getBoundingClientRect();
        const sheetRect = sheetBody.getBoundingClientRect();
        const relTop = itemRect.top - sheetRect.top + sheetBody.scrollTop;
        sheetBody.scrollTo({
          top: Math.max(0, relTop - (sheetBody.clientHeight / 2) + (itemRect.height / 2)),
          behavior: "smooth"
        });
      }
    }, 120);
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

  // 7. Dynamic TOC Visibility: Disappear when crossing conclusion into full-width post content
  const postFullwidth = document.querySelector(".paper-post-fullwidth");
  const tocElement = document.querySelector(".paper-layout > .toc");
  const mobileFab = document.querySelector(".mobile-toc-fab");

  if (postFullwidth && (tocElement || mobileFab)) {
    const checkTocVisibility = () => {
      const postRect = postFullwidth.getBoundingClientRect();
      // When the top of post-conclusion content reaches within 140px of viewport top, hide TOC
      const shouldHide = postRect.top <= 140;
      if (tocElement) tocElement.classList.toggle("toc-hidden", shouldHide);
      if (mobileFab) mobileFab.classList.toggle("fab-hidden", shouldHide);
    };

    window.addEventListener("scroll", checkTocVisibility, { passive: true });
    window.addEventListener("resize", checkTocVisibility, { passive: true });
    checkTocVisibility();
  }
});
