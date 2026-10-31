# -*- coding: utf-8 -*-
import re

tree_html = '''    <!-- ================= PPRI HIERARCHICAL KNOWLEDGE & EVIDENCE TREE ATLAS ================= -->
    <section class="vi-tree-section" id="section-site-treemap" aria-labelledby="tree-atlas-title">
      <div class="container">
        <!-- Section Header -->
        <div class="vi-tree-header">
          <div class="vi-tree-header-text">
            <span class="home-section-label">Topological Site Atlas</span>
            <h2 id="tree-atlas-title">Hierarchical Knowledge &amp; Evidence Tree</h2>
            <p>
              An authentic multi-tier tree architecture mapping the Pakistan Provincial Reform Institute from its central evidence core down to verified data observatories, analytical models, and community surveys.
            </p>
          </div>
          <div class="vi-tree-controls">
            <span class="vi-tree-stat-pill">6 Major Pillars • 24 Sub-Branches • 70+ Verified Nodes</span>
            <button type="button" class="vi-tree-toggle-all-btn" id="viTreeToggleAll" aria-expanded="false">
              <span class="toggle-icon" aria-hidden="true">⊞</span>
              <span class="toggle-text">Expand All Branches</span>
            </button>
          </div>
        </div>

        <!-- The Interactive Tree Canvas -->
        <div class="vi-tree-canvas">
          <!-- Level 0: The Central Root Node -->
          <div class="vi-tree-root-container">
            <div class="vi-tree-root-node">
              <div class="root-badge">Core Repository · Root Node</div>
              <div class="root-title">
                <span class="root-icon" aria-hidden="true">🌲</span>
                <div class="root-text">
                  <h3>Pakistan Provincial Reform Institute</h3>
                  <span>Public Knowledge &amp; Evidence Tree</span>
                </div>
              </div>
            </div>
            <!-- Central Trunk Stem dropping down from root -->
            <div class="vi-tree-root-stem" aria-hidden="true"></div>
          </div>

          <!-- SVG Trunk Branching Network (Desktop/Tablet) -->
          <div class="vi-tree-trunk-network" aria-hidden="true">
            <svg class="vi-tree-trunk-svg" viewBox="0 0 1200 48" preserveAspectRatio="none">
              <!-- Stepped orthogonal horizontal distributor line connecting 6 pillars -->
              <path class="trunk-path-base" d="M 600,0 V 24 M 100,24 H 1100 M 100,24 V 48 M 300,24 V 48 M 500,24 V 48 M 700,24 V 48 M 900,24 V 48 M 1100,24 V 48" />
            </svg>
          </div>

          <!-- Level 1: The 6 Pillar Branch Nodes -->
          <div class="vi-tree-pillars-row">

            <!-- Pillar 1: Visual Analytics (Teal Theme) -->
            <div class="vi-tree-branch theme-teal" data-pillar="insights">
              <div class="vi-tree-branch-stem-in" aria-hidden="true"></div>
              <button type="button" class="vi-tree-node-card" aria-expanded="false" aria-controls="branch-content-insights">
                <div class="node-header">
                  <span class="node-icon" aria-hidden="true">📊</span>
                  <div class="node-titles">
                    <span class="node-tier">Pillar 1 · Empirical Lab</span>
                    <h4 class="node-name">Visual Analytics</h4>
                  </div>
                </div>
                <div class="node-meta">
                  <span class="node-count">16 Infographics</span>
                  <span class="node-toggle-state" aria-hidden="true">+</span>
                </div>
              </button>
              
              <!-- Downward connector to sub-branches -->
              <div class="vi-tree-children-container" id="branch-content-insights" hidden>
                <div class="vi-tree-substem" aria-hidden="true"></div>
                
                <div class="vi-tree-subbranches-list">
                  <!-- Sub-branch 1.1 -->
                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">├─</span>
                      <h5>Fiscal &amp; Sovereign Debt</h5>
                      <span class="subbranch-badge">4 Models</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/insights/#card-fiscal" class="vi-tree-leaf">
                        <span class="leaf-metric">51.8%</span>
                        <span class="leaf-name">Federal Budget &amp; Markup</span>
                      </a>
                      <a href="/insights/#card-debt" class="vi-tree-leaf">
                        <span class="leaf-metric">PKR 86.4T</span>
                        <span class="leaf-name">Public Debt Surge (FY18–26)</span>
                      </a>
                      <a href="/insights/#card-tax-exp" class="vi-tree-leaf">
                        <span class="leaf-metric">PKR 3.88T</span>
                        <span class="leaf-name">Federal Tax Concessions</span>
                      </a>
                      <a href="/insights/#card-prov-matrix" class="vi-tree-leaf">
                        <span class="leaf-metric">4 Provinces</span>
                        <span class="leaf-name">NFC, Debt &amp; Conflict Matrix</span>
                      </a>
                    </div>
                  </div>

                  <!-- Sub-branch 1.2 -->
                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">├─</span>
                      <h5>Economy &amp; Sectoral Shifts</h5>
                      <span class="subbranch-badge">4 Models</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/insights/#card-wage-infl" class="vi-tree-leaf">
                        <span class="leaf-metric">-11.6%</span>
                        <span class="leaf-name">Real Purchasing Power</span>
                      </a>
                      <a href="/insights/#card-sector-employment" class="vi-tree-leaf">
                        <span class="leaf-metric">40.7%</span>
                        <span class="leaf-name">Services vs Agriculture</span>
                      </a>
                      <a href="/insights/#card-agri-shifts" class="vi-tree-leaf">
                        <span class="leaf-metric">64.5% Small</span>
                        <span class="leaf-name">Farmland Fragmentation</span>
                      </a>
                      <a href="/insights/#card-macro" class="vi-tree-leaf">
                        <span class="leaf-metric">35 Years</span>
                        <span class="leaf-name">Macro Trajectory Overlay</span>
                      </a>
                    </div>
                  </div>

                  <!-- Sub-branch 1.3 -->
                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">├─</span>
                      <h5>Demographics &amp; Spatial Governance</h5>
                      <span class="subbranch-badge">4 Models</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/insights/#card-gender-land" class="vi-tree-leaf">
                        <span class="leaf-metric">1.8% Female</span>
                        <span class="leaf-name">Land Ownership Ratio</span>
                      </a>
                      <a href="/insights/#card-census-shifts" class="vi-tree-leaf">
                        <span class="leaf-metric">38.8% Urban</span>
                        <span class="leaf-name">Census Growth Shifts</span>
                      </a>
                      <a href="/insights/#card-districts-scatter" class="vi-tree-leaf">
                        <span class="leaf-metric">135 Districts</span>
                        <span class="leaf-name">Poverty vs Literacy</span>
                      </a>
                      <a href="/insights/#card-census-hist" class="vi-tree-leaf">
                        <span class="leaf-metric">1951–2023</span>
                        <span class="leaf-name">70-Year Census Trajectory</span>
                      </a>
                    </div>
                  </div>

                  <!-- Sub-branch 1.4 -->
                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">└─</span>
                      <h5>Living Standards &amp; Budgets</h5>
                      <span class="subbranch-badge">4 Models</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/insights/#card-hies" class="vi-tree-leaf">
                        <span class="leaf-metric">42.4% Food</span>
                        <span class="leaf-name">Food Engel Burden</span>
                      </a>
                      <a href="/insights/#card-consumption-pie" class="vi-tree-leaf">
                        <span class="leaf-metric">63.7% Basic</span>
                        <span class="leaf-name">Consumption Basket</span>
                      </a>
                      <a href="/insights/#card-services" class="vi-tree-leaf">
                        <span class="leaf-metric">6.2x Gap</span>
                        <span class="leaf-name">Basic Utilities Inequality</span>
                      </a>
                      <a href="/insights/#card-lfs" class="vi-tree-leaf">
                        <span class="leaf-metric">-34% Rural</span>
                        <span class="leaf-name">Labor &amp; Wage Gap</span>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="vi-tree-leaf-hub-link">
                  <a href="/insights/">Launch Visual Analytics Lab &rarr;</a>
                </div>
              </div>
            </div>

            <!-- Pillar 2: Data Observatories (Blue Theme) -->
            <div class="vi-tree-branch theme-blue" data-pillar="data">
              <div class="vi-tree-branch-stem-in" aria-hidden="true"></div>
              <button type="button" class="vi-tree-node-card" aria-expanded="false" aria-controls="branch-content-data">
                <div class="node-header">
                  <span class="node-icon" aria-hidden="true">🏛️</span>
                  <div class="node-titles">
                    <span class="node-tier">Pillar 2 · Evidence Centre</span>
                    <h4 class="node-name">Data Observatories</h4>
                  </div>
                </div>
                <div class="node-meta">
                  <span class="node-count">8 Observatories</span>
                  <span class="node-toggle-state" aria-hidden="true">+</span>
                </div>
              </button>

              <div class="vi-tree-children-container" id="branch-content-data" hidden>
                <div class="vi-tree-substem" aria-hidden="true"></div>
                <div class="vi-tree-subbranches-list">
                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">├─</span>
                      <h5>Thematic Observatories</h5>
                      <span class="subbranch-badge">5 Domains</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/data/centre.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Hub</span>
                        <span class="leaf-name">Central Data Observatory</span>
                      </a>
                      <a href="/data/public-finance/" class="vi-tree-leaf">
                        <span class="leaf-badge">Finance</span>
                        <span class="leaf-name">Public Finance &amp; 7th NFC</span>
                      </a>
                      <a href="/data/economy/" class="vi-tree-leaf">
                        <span class="leaf-badge">Economy</span>
                        <span class="leaf-name">Economy &amp; Real Wages</span>
                      </a>
                      <a href="/data/population/" class="vi-tree-leaf">
                        <span class="leaf-badge">Demographics</span>
                        <span class="leaf-name">Population &amp; Census 2023</span>
                      </a>
                      <a href="/data/living-standards/" class="vi-tree-leaf">
                        <span class="leaf-badge">Welfare</span>
                        <span class="leaf-name">Living Standards &amp; HIES</span>
                      </a>
                    </div>
                  </div>

                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">└─</span>
                      <h5>Tools &amp; Open Data</h5>
                      <span class="subbranch-badge">4 Repositories</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/data/compare/" class="vi-tree-leaf">
                        <span class="leaf-badge">Tool</span>
                        <span class="leaf-name">Indicator Comparator</span>
                      </a>
                      <a href="/data/downloads/" class="vi-tree-leaf">
                        <span class="leaf-badge">Downloads</span>
                        <span class="leaf-name">Open Data (16 Datasets)</span>
                      </a>
                      <a href="/knowledge-library/" class="vi-tree-leaf">
                        <span class="leaf-badge">Reference</span>
                        <span class="leaf-name">Knowledge Library</span>
                      </a>
                      <a href="/sources/" class="vi-tree-leaf">
                        <span class="leaf-badge">Citations</span>
                        <span class="leaf-name">Statistical Sources</span>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="vi-tree-leaf-hub-link">
                  <a href="/data/centre.html">Explore Central Data Observatory &rarr;</a>
                </div>
              </div>
            </div>

            <!-- Pillar 3: Scenarios & Maps (Emerald Theme) -->
            <div class="vi-tree-branch theme-emerald" data-pillar="maps">
              <div class="vi-tree-branch-stem-in" aria-hidden="true"></div>
              <button type="button" class="vi-tree-node-card" aria-expanded="false" aria-controls="branch-content-maps">
                <div class="node-header">
                  <span class="node-icon" aria-hidden="true">🗺️</span>
                  <div class="node-titles">
                    <span class="node-tier">Pillar 3 · Spatial Models</span>
                    <h4 class="node-name">Scenarios &amp; Maps</h4>
                  </div>
                </div>
                <div class="node-meta">
                  <span class="node-count">Cartography Lab</span>
                  <span class="node-toggle-state" aria-hidden="true">+</span>
                </div>
              </button>

              <div class="vi-tree-children-container" id="branch-content-maps" hidden>
                <div class="vi-tree-substem" aria-hidden="true"></div>
                <div class="vi-tree-subbranches-list">
                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">├─</span>
                      <h5>Interactive Scenario Lab</h5>
                      <span class="subbranch-badge">Spatial Engine</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/maps/scenarios/" class="vi-tree-leaf">
                        <span class="leaf-badge">PPRI-01</span>
                        <span class="leaf-name">13-Unit Administrative Model</span>
                      </a>
                      <a href="/scenarios/" class="vi-tree-leaf">
                        <span class="leaf-badge">Framework</span>
                        <span class="leaf-name">Subnational Governance Scenarios</span>
                      </a>
                    </div>
                  </div>

                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">└─</span>
                      <h5>Cartographic Reference</h5>
                      <span class="subbranch-badge">Boundaries</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/maps/current/administrative.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Reference</span>
                        <span class="leaf-name">Current Geography (4 Provinces)</span>
                      </a>
                      <a href="/maps/" class="vi-tree-leaf">
                        <span class="leaf-badge">Gallery</span>
                        <span class="leaf-name">Cartographic Map Gallery</span>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="vi-tree-leaf-hub-link">
                  <a href="/maps/scenarios/">Launch Interactive Scenario Lab &rarr;</a>
                </div>
              </div>
            </div>

            <!-- Pillar 4: Policy Research & Reports (Indigo Theme) -->
            <div class="vi-tree-branch theme-indigo" data-pillar="research">
              <div class="vi-tree-branch-stem-in" aria-hidden="true"></div>
              <button type="button" class="vi-tree-node-card" aria-expanded="false" aria-controls="branch-content-research">
                <div class="node-header">
                  <span class="node-icon" aria-hidden="true">📑</span>
                  <div class="node-titles">
                    <span class="node-tier">Pillar 4 · Evidence Base</span>
                    <h4 class="node-name">Policy Research</h4>
                  </div>
                </div>
                <div class="node-meta">
                  <span class="node-count">8 Major Studies</span>
                  <span class="node-toggle-state" aria-hidden="true">+</span>
                </div>
              </button>

              <div class="vi-tree-children-container" id="branch-content-research" hidden>
                <div class="vi-tree-substem" aria-hidden="true"></div>
                <div class="vi-tree-subbranches-list">
                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">├─</span>
                      <h5>Flagship &amp; Empirical Reports</h5>
                      <span class="subbranch-badge">6 Publications</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/research/policy-papers/provincial-reorganization-of-pakistan.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Flagship</span>
                        <span class="leaf-name">Provincial Reorganization</span>
                      </a>
                      <a href="/research/reports/income-went-up-why-does-life-feel-harder.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Report 1</span>
                        <span class="leaf-name">Household Income vs Inflation</span>
                      </a>
                      <a href="/research/reports/bribe-you-cant-see-corruption-private-tax.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Report 2</span>
                        <span class="leaf-name">NCPS 2025 Corruption Tax</span>
                      </a>
                      <a href="/research/reports/price-of-a-simple-task-pakistan-bureaucracy-cost.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Report 3</span>
                        <span class="leaf-name">Bureaucracy Cost Index</span>
                      </a>
                      <a href="/research/reports/same-country-different-life-district-access.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Report 4</span>
                        <span class="leaf-name">District Inequality: Basic Services</span>
                      </a>
                      <a href="/research/reports/does-money-work-better-spent-closer-to-people.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Report 5</span>
                        <span class="leaf-name">Fiscal Decentralization vs ADP</span>
                      </a>
                    </div>
                  </div>

                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">└─</span>
                      <h5>Working Papers &amp; Legal Frameworks</h5>
                      <span class="subbranch-badge">3 Studies</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/research/working-papers/provinces-local-government.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Paper</span>
                        <span class="leaf-name">Provinces &amp; Local Government</span>
                      </a>
                      <a href="/research/briefs/administrative-scale.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Brief</span>
                        <span class="leaf-name">Administrative Scale &amp; Ratios</span>
                      </a>
                      <a href="/research/legal-library.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Legal</span>
                        <span class="leaf-name">Constitutional Legal Library</span>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="vi-tree-leaf-hub-link">
                  <a href="/research/">Explore PPRI Research Hub &rarr;</a>
                </div>
              </div>
            </div>

            <!-- Pillar 5: 25 Analytical Articles (Purple Theme) -->
            <div class="vi-tree-branch theme-purple" data-pillar="articles">
              <div class="vi-tree-branch-stem-in" aria-hidden="true"></div>
              <button type="button" class="vi-tree-node-card" aria-expanded="false" aria-controls="branch-content-articles">
                <div class="node-header">
                  <span class="node-icon" aria-hidden="true">📰</span>
                  <div class="node-titles">
                    <span class="node-tier">Pillar 5 · Policy Discourse</span>
                    <h4 class="node-name">Analytical Articles</h4>
                  </div>
                </div>
                <div class="node-meta">
                  <span class="node-count">25 Articles</span>
                  <span class="node-toggle-state" aria-hidden="true">+</span>
                </div>
              </button>

              <div class="vi-tree-children-container" id="branch-content-articles" hidden>
                <div class="vi-tree-substem" aria-hidden="true"></div>
                <div class="vi-tree-subbranches-list">
                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">├─</span>
                      <h5>Provincial Demands &amp; Scale</h5>
                      <span class="subbranch-badge">8 Analyses</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/articles/four-provinces-241-million-people-administrative-scale.html" class="vi-tree-leaf">
                        <span class="leaf-name">4 Provinces vs 241.5M Scale</span>
                      </a>
                      <a href="/articles/provinces-of-pakistan-names-capitals-population.html" class="vi-tree-leaf">
                        <span class="leaf-name">Provinces of Pakistan (2026)</span>
                      </a>
                      <a href="/articles/south-punjab-why-does-the-province-demand-keep-returning.html" class="vi-tree-leaf">
                        <span class="leaf-name">South Punjab: 11 Districts Map</span>
                      </a>
                      <a href="/articles/hazara-province-why-has-the-demand-survived.html" class="vi-tree-leaf">
                        <span class="leaf-name">Hazara Province &amp; KP Share</span>
                      </a>
                      <a href="/articles/karachi-urban-sindh-representation-revenue-administration.html" class="vi-tree-leaf">
                        <span class="leaf-name">Karachi: 7 Districts &amp; 25 Towns</span>
                      </a>
                      <a href="/articles/south-punjab-saraiki-bahawalpur-difference.html" class="vi-tree-leaf">
                        <span class="leaf-name">South Punjab vs Bahawalpur</span>
                      </a>
                      <a href="/articles/bahawalpur-province-restoration-2026.html" class="vi-tree-leaf">
                        <span class="leaf-name">Bahawalpur Restoration (1955)</span>
                      </a>
                      <a href="/articles/is-gilgit-baltistan-a-province-of-pakistan.html" class="vi-tree-leaf">
                        <span class="leaf-name">Is Gilgit-Baltistan a Province?</span>
                      </a>
                    </div>
                  </div>

                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">└─</span>
                      <h5>Fiscal Federalism &amp; Devolution</h5>
                      <span class="subbranch-badge">6 Analyses</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/articles/where-does-pakistans-development-money-go.html" class="vi-tree-leaf">
                        <span class="leaf-name">Where Does Development Money Go?</span>
                      </a>
                      <a href="/articles/18th-amendment-did-devolution-stop-at-provincial-capital.html" class="vi-tree-leaf">
                        <span class="leaf-name">18th Amendment vs Article 140A</span>
                      </a>
                      <a href="/articles/more-provinces-or-stronger-local-governments.html" class="vi-tree-leaf">
                        <span class="leaf-name">More Provinces vs Local Governments</span>
                      </a>
                      <a href="/articles/did-2001-devolution-improve-services-evidence.html" class="vi-tree-leaf">
                        <span class="leaf-name">Did 2001 Devolution Improve Services?</span>
                      </a>
                      <a href="/articles/how-far-is-government-administrative-distance.html" class="vi-tree-leaf">
                        <span class="leaf-name">Administrative Travel Times</span>
                      </a>
                      <a href="/articles/how-should-pakistan-evaluate-a-new-province.html" class="vi-tree-leaf">
                        <span class="leaf-name">12-Point Evaluation Rubric</span>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="vi-tree-leaf-hub-link">
                  <a href="/articles/">Browse All 25 Policy Articles &rarr;</a>
                </div>
              </div>
            </div>

            <!-- Pillar 6: Reform Frameworks & Surveys (Amber Theme) -->
            <div class="vi-tree-branch theme-amber" data-pillar="reform">
              <div class="vi-tree-branch-stem-in" aria-hidden="true"></div>
              <button type="button" class="vi-tree-node-card" aria-expanded="false" aria-controls="branch-content-reform">
                <div class="node-header">
                  <span class="node-icon" aria-hidden="true">🗳️</span>
                  <div class="node-titles">
                    <span class="node-tier">Pillar 6 · Public Action</span>
                    <h4 class="node-name">Reform &amp; Surveys</h4>
                  </div>
                </div>
                <div class="node-meta">
                  <span class="node-count">6 Surveys + Models</span>
                  <span class="node-toggle-state" aria-hidden="true">+</span>
                </div>
              </button>

              <div class="vi-tree-children-container" id="branch-content-reform" hidden>
                <div class="vi-tree-substem" aria-hidden="true"></div>
                <div class="vi-tree-subbranches-list">
                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">├─</span>
                      <h5>Constitutional &amp; Administrative Models</h5>
                      <span class="subbranch-badge">4 Frameworks</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/provinces/proposed-models.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Model</span>
                        <span class="leaf-name">13-Unit Restructuring Model</span>
                      </a>
                      <a href="/provinces/constitutional-framework.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Law</span>
                        <span class="leaf-name">Article 239(4) Bill Procedure</span>
                      </a>
                      <a href="/provinces/transition-framework.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Execution</span>
                        <span class="leaf-name">3-Year Civil Service Transition</span>
                      </a>
                      <a href="/provinces/why-provinces.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Case</span>
                        <span class="leaf-name">Why Subnational Reform?</span>
                      </a>
                    </div>
                  </div>

                  <div class="vi-tree-subbranch-node">
                    <div class="subbranch-header">
                      <span class="subbranch-connector" aria-hidden="true">└─</span>
                      <h5>Pakistan Community Surveys Hub</h5>
                      <span class="subbranch-badge">6 Surveys</span>
                    </div>
                    <div class="vi-tree-leaves-grid">
                      <a href="/surveys/" class="vi-tree-leaf">
                        <span class="leaf-badge">Hub</span>
                        <span class="leaf-name">Community Surveys Portal</span>
                      </a>
                      <a href="/surveys/new-provinces/" class="vi-tree-leaf">
                        <span class="leaf-badge">Survey 1</span>
                        <span class="leaf-name">New Provinces &amp; Representation</span>
                      </a>
                      <a href="/surveys/local-government/" class="vi-tree-leaf">
                        <span class="leaf-badge">Survey 2</span>
                        <span class="leaf-name">Stronger Local Government</span>
                      </a>
                      <a href="/surveys/household-costs-inflation/" class="vi-tree-leaf">
                        <span class="leaf-badge">Survey 3</span>
                        <span class="leaf-name">Household Costs &amp; Inflation</span>
                      </a>
                      <a href="/surveys/youth-jobs/" class="vi-tree-leaf">
                        <span class="leaf-badge">Survey 4</span>
                        <span class="leaf-name">Youth Jobs &amp; Careers</span>
                      </a>
                      <a href="/surveys/jobs-abroad/" class="vi-tree-leaf">
                        <span class="leaf-badge">Survey 5</span>
                        <span class="leaf-name">Jobs Abroad &amp; Work Migration</span>
                      </a>
                      <a href="/surveys/government-delays/" class="vi-tree-leaf">
                        <span class="leaf-badge">Survey 6</span>
                        <span class="leaf-name">Government Delays &amp; Paperwork</span>
                      </a>
                      <a href="/consultation/submissions.html" class="vi-tree-leaf">
                        <span class="leaf-badge">Submit</span>
                        <span class="leaf-name">Submit Policy Memoranda</span>
                      </a>
                    </div>
                  </div>
                </div>

                <div class="vi-tree-leaf-hub-link">
                  <a href="/surveys/">Take a Pakistan Community Survey &rarr;</a>
                </div>
              </div>
            </div>

          </div>
          <!-- /.vi-tree-pillars-row -->
        </div>
        <!-- /.vi-tree-canvas -->
      </div>
    </section>
'''

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace existing #section-site-treemap
sec_start = html.find('id="section-site-treemap"')
if sec_start != -1:
    tag_start = html.rfind('<section', 0, sec_start)
    tag_end = html.find('</section>', sec_start) + len('</section>')
    html = html[:tag_start] + tree_html + html[tag_end:]
    print("Replaced tree section in index.html")
else:
    print("Error: #section-site-treemap not found")

# Replace or add tree interaction script before </body>
tree_script = '''    <script>
      (function() {
        var toggleAllBtn = document.getElementById('viTreeToggleAll');
        var branchCards = document.querySelectorAll('.vi-tree-node-card');

        function setBranchState(branch, open) {
          var btn = branch.querySelector('.vi-tree-node-card');
          var container = branch.querySelector('.vi-tree-children-container');
          var indicator = branch.querySelector('.node-toggle-state');
          if (!btn || !container) return;

          btn.setAttribute('aria-expanded', open ? 'true' : 'false');
          container.hidden = !open;
          if (open) {
            branch.classList.add('is-open');
            if (indicator) indicator.textContent = '−';
          } else {
            branch.classList.remove('is-open');
            if (indicator) indicator.textContent = '+';
          }
        }

        branchCards.forEach(function(card) {
          card.addEventListener('click', function(e) {
            e.preventDefault();
            var branch = card.closest('.vi-tree-branch');
            if (!branch) return;
            var isExpanded = card.getAttribute('aria-expanded') === 'true';
            setBranchState(branch, !isExpanded);
            updateGlobalButton();
          });
        });

        function updateGlobalButton() {
          if (!toggleAllBtn) return;
          var total = branchCards.length;
          var openCount = document.querySelectorAll('.vi-tree-branch.is-open').length;
          var allOpen = openCount === total;
          toggleAllBtn.setAttribute('aria-expanded', allOpen ? 'true' : 'false');
          toggleAllBtn.querySelector('.toggle-text').textContent = allOpen ? 'Collapse All Branches' : 'Expand All Branches';
          toggleAllBtn.querySelector('.toggle-icon').textContent = allOpen ? '⊟' : '⊞';
        }

        if (toggleAllBtn) {
          toggleAllBtn.addEventListener('click', function() {
            var isAllOpen = toggleAllBtn.getAttribute('aria-expanded') === 'true';
            document.querySelectorAll('.vi-tree-branch').forEach(function(b) {
              setBranchState(b, !isAllOpen);
            });
            updateGlobalButton();
          });
        }
      })();
    </script>
'''

# Remove previous toggle script if present
html = re.sub(r'<script>\s*\(function\(\)\s*\{\s*var btn = document\.getElementById\(\'viTreemapToggleAll\'\);.*?</script>\s*', '', html, flags=re.DOTALL)

# Add new tree_script before </body>
html = html.replace('  </body>', tree_script + '  </body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated with Hierarchical Tree Architecture & interaction script.")
