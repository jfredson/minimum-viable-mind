import { defineConfig } from 'astro/config';

// Same generator and settings as the Belt Equation site: a fully static build in
// dist/, served from Cloudflare Workers static assets. Public from its first deploy.
// `site` is the canonical URL (the custom domain in wrangler.jsonc); it feeds canonical
// links and sitemap URLs, so it must match the domain the Worker is attached to.
export default defineConfig({
  site: 'https://minimumviablemind.sentient-horizons.com',
  trailingSlash: 'always',
});
