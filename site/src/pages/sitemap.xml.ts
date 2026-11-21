// The sitemap at /sitemap.xml, in the shape the sister sites use (upgrade-tree and quiet-galaxy,
// site/src/pages/sitemap.xml.ts). This site has no generated pages: every page is a file in
// src/pages, so the list is written here and must change when a page is added or removed. The
// not-found page is left out. Added 2026-10-31, when a search for the family's sites by name found
// four of them, this one among them, serving no sitemap.
import type { APIRoute } from 'astro';

const PAGES = ['/', '/eli5/', '/ladder/', '/questions/', '/learned/', '/story/', '/spend/'];

export const GET: APIRoute = ({ site }) => {
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${PAGES.map((p) => `<url><loc>${new URL(p, site).href}</loc></url>`).join('\n')}
</urlset>
`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
