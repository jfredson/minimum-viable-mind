// The News posts (tracker pattern rules 4.10 to 4.16), dated Markdown files in
// src/content/news/YYYY-MM-DD-slug.md. None yet (2026-11-21): rule 3.3 part 4 holds every post
// while any tracker record carries an open verify entry.
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
const news = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/news' }),
  schema: z.object({
    title: z.string(),
    date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    kind: z.enum(['a prediction tested', 'a score moved', 'a theory added', 'the headline moved', 'the method changed', 'a ruling', 'start here']),
    summary: z.string(),
    records: z.array(z.string()).default([]),
    sources: z.array(z.object({ label: z.string(), url: z.string().url() })).default([]),
  }).transform((d) => {
    const [y, m, day] = d.date.split('-').map(Number);
    return { ...d, date_long: `${day} ${MONTHS[m - 1]} ${y}` };
  }),
});
export const collections = { news };
