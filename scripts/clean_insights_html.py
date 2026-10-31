with open('insights/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find end of Card 16:
start_c16 = text.find('id="card-prov-matrix"')
footer_pos = text.find('class="vi-card-footer"', start_c16)
actions_pos = text.find('class="vi-actions"', footer_pos)
end_c16 = text.find('</div>\n        </div>', actions_pos)
if end_c16 == -1:
    end_c16 = text.find('</div>\r\n        </div>', actions_pos)

c16_close = end_c16 + len('</div>\n        </div>')

# Up to c16_close is all the header, hero, filter pills, jump nav, and 16 cards!
head_and_cards = text[:c16_close]

# Now assemble clean ending
clean_ending = """
      </div>
    </main>

    <!-- Hidden Offscreen Canvas for Retina PNG Export -->
    <canvas id="vi-export-canvas" width="2080" height="1360" style="display:none;"></canvas>

    <!-- High-Precision Floating Tooltip Engine -->
    <div id="vi-tooltip" class="vi-tooltip" role="tooltip" aria-hidden="true" style="display:none;"></div>

    <!-- Toast Notification Container -->
    <div id="vi-toast" role="status" aria-live="polite"></div>

    <!-- Primary Site Footer -->
    <footer class="site-footer">
      <div class="container footer-grid">
        <div class="footer-brand">
          <img
            src="/assets/images/brand/ppri-logo-footer.jpg"
            alt="PPRI Seal"
            class="footer-logo"
            width="84"
            height="84"
            loading="lazy"
            decoding="async"
          />
          <p>Pakistan Provincial Reform Institute</p>
          <p>
            Policy research on provincial reform, federalism, decentralization
            and institutional design in Pakistan.
          </p>
        </div>
        <div>
          <h3>Research</h3>
          <ul class="footer-links">
            <li>
              <a href="/publications/#policy-papers">Policy Papers</a>
            </li>
            <li><a href="/research/reports/">Reports</a></li>
            <li><a href="/publications/#briefs">Policy Briefs</a></li>
            <li>
              <a href="/publications/#working-papers">Working Papers</a>
            </li>
            <li><a href="/articles/">Articles &amp; Analysis</a></li>
          </ul>
        </div>
        <div>
          <h3>Explore</h3>
          <ul class="footer-links">
            <li><a href="/scenarios/">Governance Scenarios</a></li>
            <li><a href="/insights/" aria-current="page">Visual Insights Lab</a></li>
            <li><a href="/data/centre.html">Data Observatory</a></li>
            <li><a href="/data/population/">Population &amp; Demographics</a></li>
            <li><a href="/data/compare/">Provinces Comparator</a></li>
            <li><a href="/data/downloads/">Open Data Downloads</a></li>
            <li><a href="/provinces/">Provincial Reform</a></li>
            <li><a href="/maps/">Maps</a></li>
            <li><a href="/maps/scenarios/">Scenario Lab</a></li>
            <li><a href="/methodology/">Methodology</a></li>
            <li><a href="/sources/">Sources</a></li>
          </ul>
        </div>
        <div>
          <h3>Connect</h3>
          <ul class="footer-links">
            <li>
              <a href="https://x.com/PPRI_Pakistan" rel="me"
                >X / @PPRI_Pakistan</a
              >
            </li>
            <li><a href="/consultation/">Public Consultation</a></li>
            <li><a href="/consultation/submissions.html">Submit an idea</a></li>
            <li><a href="/contact.html"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: -2px; margin-right: 5px;" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>Contact</a></li>
          </ul>
        </div>
      </div>
      <div class="container footer-bottom">
        <span>&copy; <span data-current-year>2026</span> Pakistan Provincial Reform Institute</span>
        <span><a href="/privacy.html">Privacy</a> &middot; <a href="/terms.html">Terms</a> &middot; <a href="/directory.html">Directory</a> &middot; <a href="/sitemap.xml">Sitemap</a> &middot; <a href="/feed.xml">RSS Feed</a></span>
      </div>
    </footer>

    <!-- Modular Visual Analytics Runtime -->
    <script src="/assets/js/modules/visual-insights.js"></script>
    <script src="/assets/js/main.js"></script>
  </body>
</html>
"""

cleaned_html = head_and_cards + clean_ending
with open('insights/index.html', 'w', encoding='utf-8') as f:
    f.write(cleaned_html)

print(f"Cleaned insights/index.html: new size {len(cleaned_html)} bytes")
