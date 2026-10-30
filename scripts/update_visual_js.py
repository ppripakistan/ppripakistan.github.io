with open('assets/js/modules/visual-insights.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update title extraction in exportCard
target_title = "const title = card.querySelector('.vi-card-title') ? card.querySelector('.vi-card-title').innerText : 'PPRI Policy Infographic';"
replace_title = "const title = card.querySelector('.vi-card-title') ? card.querySelector('.vi-card-title').innerText.replace(/^#\\d+:\\s*/, '').trim() : 'PPRI Policy Infographic';"

if target_title in text:
    text = text.replace(target_title, replace_title, 1)
    print("SUCCESS: Updated title extraction in exportCard")
else:
    print("WARNING: target_title not found in exportCard")

# 2. Add initQuickNav and call in renderAllCards
quick_nav_fn = """
        // 3. INTERACTIVE QUICK-JUMP SMOOTH SCROLL HANDLER
        function initQuickNav() {
          const chips = document.querySelectorAll('.vi-chip-btn[data-target]');
          chips.forEach(btn => {
            // Avoid duplicate listeners
            if (btn.__hasQuickNav) return;
            btn.__hasQuickNav = true;
            btn.addEventListener('click', function(e) {
              e.preventDefault();
              const targetId = this.getAttribute('data-target');
              const targetCard = document.getElementById(targetId);
              if (!targetCard) return;

              // If hidden by active filter, unhide by resetting filter to 'all'
              if (targetCard.style.display === 'none') {
                if (typeof window.filterGallery === 'function') {
                  window.filterGallery('all');
                }
              }

              targetCard.scrollIntoView({ behavior: 'smooth', block: 'start' });

              targetCard.classList.remove('vi-card-highlight');
              void targetCard.offsetWidth;
              targetCard.classList.add('vi-card-highlight');
              setTimeout(() => {
                targetCard.classList.remove('vi-card-highlight');
              }, 2200);
            });
          });
        }
"""

target_render_end = "cardRenderers.forEach(c => {\n            try {\n              c.fn();\n            } catch (err) {\n              console.error(`[PPRI Error] Failed rendering ${c.name}:`, err);\n            }\n          });\n        }"

replace_render_end = target_render_end + quick_nav_fn + "\n          initQuickNav();"

if target_render_end in text:
    text = text.replace(target_render_end, replace_render_end, 1)
    print("SUCCESS: Added initQuickNav to visual-insights.js")
else:
    # Try normalized
    target_norm = target_render_end.replace('\r\n', '\n')
    text_norm = text.replace('\r\n', '\n')
    if target_norm in text_norm:
        text = text_norm.replace(target_norm, replace_render_end.replace('\r\n', '\n'), 1)
        print("SUCCESS: Added initQuickNav to visual-insights.js (normalized)")
    else:
        print("WARNING: target_render_end not found")

with open('assets/js/modules/visual-insights.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated assets/js/modules/visual-insights.js")
