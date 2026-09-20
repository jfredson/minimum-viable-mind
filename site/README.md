# The project site

The program log: where the project is, where it is going, what is on the table, and what has been learned. Built 2026-09-20 on the Belt Equation site's stack and design system so the sites read as one family. Public from its first deploy (docs/program-roadmap-2026-09-20.md) at https://minimumviablemind.sentient-horizons.com (custom domain set in `wrangler.jsonc`, chosen 2026-09-20).

## How it fits together

    data/project.toml  ──►  scripts/export_site.py  ──►  site/src/data/project.json  ──►  astro build  ──►  dist/  ──►  wrangler deploy

- **Python owns the data.** `scripts/export_site.py` validates `data/project.toml` (status vocabularies, dates, stage references, spend under cap, timeline newest-first) and writes `site/src/data/project.json`. The JSON is generated, not committed; `npm run build` and `npm run dev` run the export first.
- **Astro owns the pages.** Astro 5, fully static. `src/lib/project.ts` is the typed view of the JSON and holds the human labels for every status code; every page reads from it.
- **Styles are copied** from the Belt Equation site (`global.css`), with the MVM additions at the bottom of the file.

## Pages

| Path | What it shows |
|---|---|
| `/` | Where we are and where we are going, in two paragraphs; at-a-glance numbers (days to hibernation and to wrap-up, decisions waiting, A3 spend); the founding wager; the next most valuable steps and what each teaches; decisions waiting on John; the three nested goals; the ladder strip; ideas on the table. |
| `/ladder/` | The eight stages: status, progress, delivered, remaining, and which account of consciousness each adjudicates. |
| `/questions/` | The questions that matter (current answer, what answers it, what would count against it) and every idea on the table grouped by status. |
| `/learned/` | Findings on record, newest first: what was found, so what, source path. |
| `/story/` | One row per STATUS.md entry, by month. |
| `/spend/` | Caps and spend against each, account balance, idle-billing losses. |

## Keeping it current

`data/project.toml` is the structured twin of `STATUS.md`. Any session that adds a "WHERE THINGS STAND" entry also updates the file: `project.updated_on` and the two "where" paragraphs, a `[[timeline]]` row (newest first), any new `[[findings]]`, the `[[next_steps]]` list, idea statuses, stage progress, and `[spend]`. Then `python3 scripts/export_site.py --check`. The rule is in `CLAUDE.md`.

## Commands

Run from `site/`. Needs Node and Python 3.11 or later.

    cd ~/Code/minimum-viable-mind/site && npm install       once
    cd ~/Code/minimum-viable-mind/site && npm run check     validate the data file only
    cd ~/Code/minimum-viable-mind/site && npm run dev       local preview with live reload
    cd ~/Code/minimum-viable-mind/site && npm run build     static build to dist/
    cd ~/Code/minimum-viable-mind/site && npm run deploy    build, then wrangler deploy (needs `npx wrangler login`)

The Worker is named `mvm`. Its address is https://minimumviablemind.sentient-horizons.com: `wrangler.jsonc` declares it as a custom domain, so the first deploy creates the DNS record and certificate in the sentient-horizons.com zone automatically (the zone is on the same Cloudflare account). https://mvm.jfredson.workers.dev also works as a fallback address. `.github/workflows/deploy-site.yml` deploys on push to main once the two Cloudflare secrets exist on the repo (same names as belt-equation's).
