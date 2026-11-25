#!/usr/bin/env node
// Makes the social preview image, site/public/social-preview.png (1200 by 630): what link previews
// on iMessage, Slack, X, Reddit and the rest show when the site is shared. Added 2026-11-14 on the
// pattern of the sibling sites (quiet-galaxy/scripts/social-image.mjs, belt-equation's and
// upgrade-tree's): the site's name in the accent's capitals, one line in the large sans, a smaller
// line under it, the address in the monospace; no stock picture. Drawn in the "Notebook" skin's own
// light-theme tokens (site/src/styles/skin.css): the cool off-white page, ink, the mulberry accent (the
// ink violet until the re-inking of 2026-11-21), and
// the graph paper of 24-pixel squares fading out down the picture, as it does behind the first screen.
// Since 2026-11-21 the words are the tracker's: the big lines are the home page's title, the smaller
// one the footer line, ruled by John on 2026-11-21.
//
// Run from the repository root after changing the skin or these words:
//   node scripts/social-image.mjs
// It needs `sharp`, which Astro already installs in site/node_modules (run `npm ci` in site/ first).
// The picture is the same every time it is made; the only inputs are the values written below. The
// fonts are this machine's, so the picture is made here and committed, never at deploy.
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import { readFileSync } from 'node:fs';

const sharp = createRequire(new URL('../site/', import.meta.url))('sharp');

const W = 1200;
const H = 630;
const SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif";
const MONO = "Menlo, 'SF Mono', Consolas, monospace";

// The Notebook skin, light theme (site/src/styles/skin.css).
const bg = '#f4f4f1';
const ink = '#1b1b1a';
const muted = '#6a6a66';
const accent = '#8e2f63';
const line = 'rgba(27, 27, 26, 0.12)';

const NAME = 'Minimum Viable Mind';
const BIG = ['How the theories of', 'consciousness are holding up'];
// The small line's count comes from the records, as the line above the home page's title does
// (John, 2026-11-21: "Ten theories of consciousness, held to the same rules"). Run the export
// first so site/src/data/tracker.json exists.
const WORDS = ['No', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve'];
const tracker = JSON.parse(readFileSync(new URL('../site/src/data/tracker.json', import.meta.url), 'utf8'));
const SMALL = [`${WORDS[tracker.listed_count] ?? tracker.listed_count} theories of consciousness, held to the same rules`];
const DOMAIN = 'minimumviablemind.sentient-horizons.com';

// The graph paper: 24-pixel squares at 24 * 1.25 = 30 pixels on the card, so the grid reads at
// preview size, fading out towards the bottom.
const step = 30;
let grid = '';
for (let x = 0; x <= W; x += step) grid += `<line x1="${x}" y1="0" x2="${x}" y2="${H}" stroke="${line}" stroke-width="1"/>`;
for (let y = 0; y <= H; y += step) grid += `<line x1="0" y1="${y}" x2="${W}" y2="${y}" stroke="${line}" stroke-width="1"/>`;

const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
<defs>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#fff" stop-opacity="1"/>
    <stop offset="0.5" stop-color="#fff" stop-opacity="1"/>
    <stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
  <mask id="m"><rect width="${W}" height="${H}" fill="url(#fade)"/></mask>
</defs>
<rect width="${W}" height="${H}" fill="${bg}"/>
<g mask="url(#m)" opacity="0.8">${grid}</g>
<text x="72" y="96" font-family="${SANS}" font-size="28" font-weight="600" letter-spacing="5" fill="${accent}">${NAME.toUpperCase()}</text>
${BIG.map((t, i) => `<text x="72" y="${232 + i * 84}" font-family="${SANS}" font-size="72" font-weight="600" letter-spacing="-2" fill="${ink}">${t.replace(/'/g, '&#8217;')}</text>`).join('\n')}
${SMALL.map((t, i) => `<text x="72" y="${408 + i * 42}" font-family="${SANS}" font-size="30" fill="${muted}">${t}</text>`).join('\n')}
<text x="72" y="560" font-family="${MONO}" font-size="26" fill="${muted}">${DOMAIN}</text>
</svg>
`;

const out = fileURLToPath(new URL('../site/public/social-preview.png', import.meta.url));
await sharp(Buffer.from(svg)).png({ compressionLevel: 9 }).toFile(out);
console.log('wrote', out);
