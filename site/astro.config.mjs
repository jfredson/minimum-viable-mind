import { defineConfig } from 'astro/config';

// Same generator and settings as the Belt Equation site: a fully static build in
// dist/, served from Cloudflare Workers static assets. Public from its first deploy.
// `site` is the canonical URL (the custom domain in wrangler.jsonc); it feeds the pages'
// canonical links and the sitemap's addresses, so it must match the domain the Worker is
// attached to. The sitemap is src/pages/sitemap.xml.ts and robots.txt is in public/, both
// added 2026-10-31; before that the repository had neither, and the host's own robots.txt
// (Cloudflare's block of content signals, still put in front of ours) named no sitemap.
export default defineConfig({
  site: 'https://minimumviablemind.sentient-horizons.com',
  trailingSlash: 'always',
});
