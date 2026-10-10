const fs = require('fs');
const path = require('path');
const assert = require('assert');

console.log('=====================================================');
console.log('PPRI RESPONSIVENESS & RELATED SHOWCASE VERIFICATION');
console.log('=====================================================\n');

let totalTests = 0;
let passedTests = 0;

function test(description, fn) {
  totalTests++;
  try {
    fn();
    passedTests++;
    console.log(`  ✓ ${description}`);
  } catch (err) {
    console.error(`  ✗ FAIL: ${description}`);
    console.error(`    ${err.message}`);
  }
}

// ----------------------------------------------------------------------------
// AUDIT 1: CSS RULES & UNIVERSAL DEFENSES
// ----------------------------------------------------------------------------
console.log('=== AUDIT 1: CSS DEFENSES IN style.css & responsive.css ===');

const styleCss = fs.readFileSync('assets/css/style.css', 'utf8');
const responsiveCss = fs.readFileSync('assets/css/responsive.css', 'utf8');

test('style.css defines centered article-related-content with max-width 960px', () => {
  assert(styleCss.includes('.article-related-content {'));
  assert(styleCss.includes('width: min(calc(100% - 40px), 960px);'));
  assert(styleCss.includes('margin: 64px auto 32px;'));
  assert(styleCss.includes('box-sizing: border-box;'));
});

test('style.css has mobile gutter padding for article-related-content at max-width 800px', () => {
  assert(styleCss.includes('width: min(calc(100% - 32px), 960px);'));
  assert(styleCss.includes('margin: 48px auto 24px;'));
});

test('style.css defines paper-layout blowout defense with min-width: 0 on children', () => {
  assert(styleCss.includes('.paper-layout > article,'));
  assert(styleCss.includes('.paper-layout > .prose-wide {'));
  assert(styleCss.includes('min-width: 0;'));
});

test('style.css enforces min-width: 0 !important on paper-layout children at max-width 900px', () => {
  assert(styleCss.includes('grid-template-columns: minmax(0, 1fr) !important;'));
  assert(styleCss.includes('min-width: 0 !important;'));
  assert(styleCss.includes('width: 100% !important;'));
});

test('responsive.css defines universal CSS grid & flex child blowout defenses', () => {
  assert(responsiveCss.includes('.paper-layout > *,'));
  assert(responsiveCss.includes('.prose-wide > *,'));
  assert(responsiveCss.includes('.article-body > *,'));
  assert(responsiveCss.includes('min-width: 0;'));
});

test('responsive.css defines 900px breakpoint blowout defense for paper-layout', () => {
  assert(responsiveCss.includes('.paper-layout {'));
  assert(responsiveCss.includes('grid-template-columns: minmax(0, 1fr) !important;'));
  assert(responsiveCss.includes('min-width: 0 !important;'));
});

// ----------------------------------------------------------------------------
// AUDIT 2: ALL 25 ARTICLES CONTAINER ENCLOSURE AUDIT
// ----------------------------------------------------------------------------
console.log('\n=== AUDIT 2: ALL 25 ARTICLES CONTAINER ENCLOSURE AUDIT ===');

const articlesDir = './articles';
const articleFiles = fs.readdirSync(articlesDir).filter(f => f.endsWith('.html') && f !== 'index.html').sort();

test('Exactly 25 active analytical articles exist', () => {
  assert.strictEqual(articleFiles.length, 25);
});

articleFiles.forEach(f => {
  test(`Article ${f} has properly enclosed and centered related content`, () => {
    const content = fs.readFileSync(path.join(articlesDir, f), 'utf8');
    const relIdx = content.indexOf('article-related-content');
    assert(relIdx !== -1, 'Must contain article-related-content section');

    // Check ancestry: trace open container divs before relIdx
    const before = content.substring(0, relIdx);
    const openTags = [];
    const regex = /<(\/?)([a-zA-Z0-9]+)([^>]*)>/g;
    let m;
    while ((m = regex.exec(before)) !== null) {
      const isClose = m[1] === '/';
      const tag = m[2].toLowerCase();
      const attr = m[3];
      if (['main', 'article', 'section', 'div'].includes(tag)) {
        if (!isClose) {
          const classMatch = attr.match(/class=["']([^"']*)["']/i);
          openTags.push({ tag, class: classMatch ? classMatch[1] : '' });
        } else {
          for (let i = openTags.length - 1; i >= 0; i--) {
            if (openTags[i].tag === tag) {
              openTags.splice(i, 1);
              break;
            }
          }
        }
      }
    }

    const isEnclosed = openTags.some(t => t.class.includes('container') || t.class.includes('prose-wide') || t.class.includes('article-body'));
    assert(isEnclosed, `Must be enclosed within a container/prose-wide element. Stack was: ${openTags.map(t => t.tag + '.' + t.class).join(' > ')}`);
  });
});

// ----------------------------------------------------------------------------
// AUDIT 3: PROVINCIAL REORGANIZATION POLICY PAPER MOBILE AUDIT
// ----------------------------------------------------------------------------
console.log('\n=== AUDIT 3: POLICY PAPER 001 MOBILE RESPONSIVENESS AUDIT ===');

const paperPath = 'research/policy-papers/provincial-reorganization-of-pakistan.html';
const paperHtml = fs.readFileSync(paperPath, 'utf8');

test('Policy paper 001 contains responsive style block in head', () => {
  assert(paperHtml.includes('<style>'));
  assert(paperHtml.includes('.paper-layout > article.prose-wide {'));
  assert(paperHtml.includes('min-width: 0 !important;'));
});

test('Policy paper 001 has table-wrap around both data tables', () => {
  const tableMatches = paperHtml.match(/<table[\s\S]*?<\/table>/gi) || [];
  assert.strictEqual(tableMatches.length, 2, 'Should have exactly 2 data tables');
  
  tableMatches.forEach(t => {
    const idx = paperHtml.indexOf(t);
    const before = paperHtml.substring(Math.max(0, idx - 150), idx);
    assert(before.includes('class="table-wrap"'), 'Each table must be wrapped in table-wrap');
  });
});

test('Policy paper 001 has paper-kpi-ribbon with responsive minmax', () => {
  assert(paperHtml.includes('class="paper-kpi-ribbon"'));
  assert(paperHtml.includes('minmax(min(100%, 200px), 1fr)'));
});

test('Policy paper 001 has flowchart-wrap and flowchart-step with flex-start alignment', () => {
  assert(paperHtml.includes('class="flowchart-wrap"'));
  assert(paperHtml.includes('class="flowchart-step"'));
  assert(paperHtml.includes('align-items: flex-start;'));
});

test('Policy paper 001 has matrix-wrap and matrix-grid with fluid columns', () => {
  assert(paperHtml.includes('class="matrix-wrap"'));
  assert(paperHtml.includes('class="matrix-grid"'));
  assert(paperHtml.includes('minmax(min(100%, 240px), 1fr)'));
});

test('Policy paper 001 has models-grid with fluid columns', () => {
  assert(paperHtml.includes('class="grid grid-2 models-grid"'));
  assert(paperHtml.includes('minmax(min(100%, 260px), 1fr)'));
});

test('Policy paper 001 TOC targets all valid heading anchors', () => {
  const tocTargets = [
    '#problem',
    '#baseline',
    '#demography',
    '#arguments',
    '#reservations',
    '#local',
    '#fiscal',
    '#administration',
    '#models',
    '#framework',
    '#process',
    '#conclusion'
  ];

  tocTargets.forEach(target => {
    const id = target.substring(1);
    assert(paperHtml.includes(`id="${id}"`), `Anchor target ${target} must exist as id in the page`);
  });
});

test('Policy paper 001 TOC is ordered before content on mobile screens', () => {
  assert(paperHtml.includes('@media (max-width: 900px)'));
  assert(paperHtml.includes('order: -1;'));
});

// ----------------------------------------------------------------------------
// AUDIT 4: LINK INTEGRITY ON MODIFIED ARTICLES
// ----------------------------------------------------------------------------
console.log('\n=== AUDIT 4: LINK INTEGRITY ON MODIFIED ARTICLES ===');

const modifiedFiles = [
  'articles/why-is-pakistan-debating-new-provinces-again.html',
  'articles/four-provinces-241-million-people-administrative-scale.html',
  'articles/what-would-a-new-province-actually-change.html',
  paperPath
];

modifiedFiles.forEach(f => {
  test(`All internal links in ${f} resolve to existing files`, () => {
    const html = fs.readFileSync(f, 'utf8');
    const hrefs = html.match(/href=["'](\/[^"']+)["']/g) || [];
    hrefs.forEach(h => {
      let target = h.replace(/href=["']/, '').replace(/["']$/, '');
      const hashIdx = target.indexOf('#');
      if (hashIdx !== -1) target = target.substring(0, hashIdx);
      if (target && !target.startsWith('//') && !target.endsWith('.pdf')) {
        const localPath = target === '/' ? 'index.html' : target.substring(1);
        assert(fs.existsSync(localPath), `File does not exist: ${localPath} referenced from ${f}`);
      }
    });
  });
});

// ----------------------------------------------------------------------------
// SUMMARY
// ----------------------------------------------------------------------------
console.log('\n=============================================');
console.log(`AUDIT RESULTS: ${passedTests} passed, ${totalTests - passedTests} failed`);
if (totalTests === passedTests) {
  console.log('🎉 ALL RESPONSIVENESS AND LAYOUT AUDITS PASSED WITH ZERO ERRORS!\n');
} else {
  console.log('⚠️ SOME AUDITS FAILED. Review output above.\n');
  process.exit(1);
}
