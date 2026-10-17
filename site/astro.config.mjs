import { defineConfig } from 'astro/config';

// Same generator and settings as the Belt Equation site: a fully static build in
// dist/, served from Cloudflare Workers static assets. Public from its first deploy.
// `site` is the canonical URL (the custom domain in wrangler.jsonc); it feeds the pages'
// canonical links, so it must match the domain the Worker is attached to. There is no
// sitemap and no robots.txt in this repository (checked 2026-10-17): the host serves its
// own robots.txt, which names no sitemap, and nothing here promises one.
export default defineConfig({
  site: 'https://minimumviablemind.sentient-horizons.com',
  trailingSlash: 'always',
});
