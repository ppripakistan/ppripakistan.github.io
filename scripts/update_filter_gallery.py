with open('assets/js/modules/visual-insights.js', 'r', encoding='utf-8') as f:
    text = f.read()

target = """        window.filterGallery = function(category) {
          const buttons = document.querySelectorAll('.vi-filter-btn');
          buttons.forEach(b => b.classList.remove('active'));
          if (window.event && window.event.target) {
            window.event.target.classList.add('active');
          }

          const cards = document.querySelectorAll('.vi-card');
          cards.forEach(c => {
            if (category === 'all' || c.getAttribute('data-category') === category) {
              c.style.display = 'flex';
            } else {
              c.style.display = 'none';
            }
          });
        };"""

replacement = """        window.filterGallery = function(category, targetBtn) {
          const buttons = document.querySelectorAll('.vi-filter-btn');
          buttons.forEach(b => {
            b.classList.remove('active');
            b.setAttribute('aria-selected', 'false');
          });
          const activeBtn = targetBtn || (window.event && window.event.target ? window.event.target.closest('.vi-filter-btn') : null);
          if (activeBtn) {
            activeBtn.classList.add('active');
            activeBtn.setAttribute('aria-selected', 'true');
          }

          const cards = document.querySelectorAll('.vi-card');
          cards.forEach(c => {
            if (category === 'all' || c.getAttribute('data-category') === category) {
              c.style.display = 'flex';
            } else {
              c.style.display = 'none';
            }
          });
        };
        window.filterCategory = window.filterGallery;"""

if target in text:
    new_text = text.replace(target, replacement, 1)
    with open('assets/js/modules/visual-insights.js', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("SUCCESS: filterGallery and filterCategory updated")
else:
    print("FAILED")
