# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

toggle_script = '''    <script>
      (function() {
        var btn = document.getElementById('viTreemapToggleAll');
        if (!btn) return;
        btn.addEventListener('click', function() {
          var tiles = document.querySelectorAll('.vi-treemap-tile');
          var isExpanded = btn.getAttribute('aria-expanded') === 'true';
          tiles.forEach(function(t) { t.open = !isExpanded; });
          btn.setAttribute('aria-expanded', !isExpanded ? 'true' : 'false');
          btn.querySelector('.toggle-text').textContent = !isExpanded ? 'Collapse All' : 'Expand All';
          btn.querySelector('.toggle-icon').textContent = !isExpanded ? '⊟' : '⊞';
        });
      })();
    </script>
'''

target = '  </body>'
if 'viTreemapToggleAll' in content and 'btn.querySelector' not in content:
    content = content.replace(target, toggle_script + target)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added treemap toggle script successfully")
else:
    print("Script already present or not needed")
