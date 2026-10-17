# The project site

The program log: where the project is, where it is going, what is on the table, and what has been learned. Built 2026-09-20 on the Belt Equation site's stack and the family's shared skeleton so the sites read as one family; since 2026-10-17 it wears its own skin, "Notebook" (ruled by John that day, pull request 176). Public from its first deploy (docs/program-roadmap-2026-09-20.md), which John ran on 2026-10-08, at https://minimumviablemind.sentient-horizons.com (custom domain set in `wrangler.jsonc`, chosen 2026-09-20).

## How it fits together

    data/project.toml  ──►  scripts/export_site.py  ──►  site/src/data/project.json     ──►  astro build  ──►  dist/  ──►  wrangler deploy
    data/roadmap.toml  ──┘                         ├──►  site/src/data/roadmap.json     ──┘
                                                   ├──►  data/headline.json              (committed)
                                                   └──►  site/public/data/headline.json  (served at /data/headline.json)

- **Python owns the data.** `scripts/export_site.py` validates `data/project.toml` (status vocabularies, dates, stage references, spend under cap, timeline newest-first) and `data/roadmap.toml` (the vocabularies in its header, real dates, weekends in order with start on or before end, goal ids unique, at most one active weekend, a note on every carried goal), and writes `site/src/data/project.json` and `site/src/data/roadmap.json`. The JSON is generated, not committed; `npm run build` and `npm run dev` run the export first.
- **The headline file.** The same script writes `data/headline.json` (committed) and a public copy at `site/public/data/headline.json` (generated, ignored by git, served by the build at `/data/headline.json`): the stages delivered with their names, the ladder's mean progress, the spend against the programme's ceiling (the spend line with the largest cap), the day the log was last updated, the programme's state in one sentence (the first sentence of `where_we_are`), the latest log entry, and a status line. Every value is read from `data/project.toml`; nothing is computed from anything else. Added 2026-10-17 as this site's first adoption from the Sentient Horizons design review of the same day, which also asked that each site serve its headline at that path. `npm run check` warns when the committed copy lags the data file.
- **Astro owns the pages.** Astro 5, fully static. `src/lib/project.ts` is the typed view of the project JSON and holds the human labels for every status code; `src/lib/roadmap.ts` is the typed view of the roadmap JSON. Every page reads from one of them.
- **The styles are the family's skeleton with this site's own skin.** `src/styles/skin.css` is the "Notebook" skin (a lab notebook: a cool off-white with a faint grid behind the first screen, the ink violet, a slate for the meters; light by default; ruled by John 2026-10-17 from `sentient-horizons/design/proposals/minimum-viable-mind-skin-2026-10-17.md`), every token for both themes plus the backdrop. `src/styles/global.css` imports it, then carries `sentient-horizons/design/shell.css` copied unchanged (version noted at the marked line), then this site's own rules: the Belt Equation's components copied on 2026-09-20 and the MVM additions, with the notebook's register (the monospace on the labels, the squared at-a-glance card) at the top of them.

## Pages

| Path | What it shows |
|---|---|
| `/` | One number first (how many of the eight stages are delivered, with their names), then where we are and where we are going, in two paragraphs at the reading size; at-a-glance numbers (days to hibernation and to wrap-up, decisions waiting, A3 spend); the founding wager; the next most valuable steps and what each teaches; decisions waiting on John; the three nested goals; the ladder strip; ideas on the table. |
| `/eli5/` | The whole project in plain words. Internal working prose: it has not passed Voice Calibration or the Cold Reader. |
| `/ladder/` | The eight stages: status, progress, delivered, remaining, and which account of consciousness each adjudicates. |
| `/data/headline.json` | Not a page: the headline file, a copy of `data/headline.json` made by the build (above). |
| *(none)* | The weekend roadmap (`data/roadmap.toml`) is not published: it is a working plan for John and the sessions (John, 2026-10-08). The export still writes `roadmap.json` and validates the TOML; no page reads it. |
| `/questions/` | The questions that matter (current answer, what answers it, what would count against it) and every idea on the table grouped by status. |
| `/learned/` | Findings on record, newest first: what was found, so what, source path. |
| `/story/` | One row per STATUS.md entry, by month. |
| `/spend/` | Caps and spend against each, account balance, idle-billing losses. |

## Keeping it current

`data/project.toml` is the structured twin of `STATUS.md`. Any session that adds a "WHERE THINGS STAND" entry also updates the file: `project.updated_on` and the two "where" paragraphs, a `[[timeline]]` row (newest first), any new `[[findings]]`, the `[[next_steps]]` list, idea statuses, stage progress, and `[spend]`. Then `python3 scripts/export_site.py --check`, and `python3 scripts/export_site.py` to rewrite `data/headline.json`, which is committed with the change. The rule is in `CLAUDE.md`.

`data/roadmap.toml` is the structured twin of the weekend roadmap (`docs/weekend-roadmap-2026-09-24.md`). The Thursday or Friday evening re-plan edits it (the coming weekend's goals, which weekend absorbs a slip, `roadmap.updated_on`, which weekend is `active`), and the Sunday-night handoff sets each goal's status there (a carried goal gets a `note` naming the weekend it moved to) and the weekend's own status; both then run `npm run check`, which validates this file alongside `data/project.toml`.

## Commands

Run from `site/`. Needs Node and Python 3.11 or later.

    cd ~/Code/minimum-viable-mind/site && npm install       once
    cd ~/Code/minimum-viable-mind/site && npm run check     validate the data files only (warns if data/headline.json lags)
    cd ~/Code/minimum-viable-mind/site && npm run export    write the JSON the pages read, data/headline.json and its public copy
    cd ~/Code/minimum-viable-mind/site && npm run dev       local preview with live reload
    cd ~/Code/minimum-viable-mind/site && npm run build     static build to dist/
    cd ~/Code/minimum-viable-mind/site && npm run deploy    build, then wrangler deploy by hand (needs `npx wrangler login`); John's gate

The Worker is named `mvm`. Its address is https://minimumviablemind.sentient-horizons.com: `wrangler.jsonc` declares it as a custom domain, so the first deploy created the DNS record and certificate in the sentient-horizons.com zone (the zone is on the same Cloudflare account). https://mvm.jfredson.workers.dev also works as a fallback address.

**The deploy gate, as it stands on 2026-10-17.** John ran the first deploy from his machine on 2026-10-08 and set the two Cloudflare secrets the same afternoon, so since then `.github/workflows/deploy-site.yml` deploys on every push to `main` that touches `data/`, `scripts/export_site.py`, `site/` or the workflow itself. Merging such a pull request is therefore a deploy. Deploying is a launch and stays behind John's gate (`CLAUDE.md`, "Keeping the site current"): sessions do not push those paths to `main`; they open a pull request whose description says it deploys the site, and John merges it. (Until 2026-10-08 this paragraph read that the workflow would deploy "once the two Cloudflare secrets exist on the repo"; they have existed since that day.)

**robots.txt and sitemap, checked 2026-10-17.** The repository has no `robots.txt` and builds no sitemap. The host serves its own `robots.txt` at the site's address (Cloudflare's managed file of content signals), which names no sitemap, so nothing promises one; `/sitemap-index.xml` is the site's 404 page. The comment in `astro.config.mjs` that said `site` fed "sitemap URLs" was corrected the same day.

## Changes to the site

Newest first, with absolute dates. The project's record of record is `STATUS.md`; this list is only for the site itself.

- 2026-10-17: the headline file. `scripts/export_site.py` now also writes `data/headline.json` and its public copy, served at `/data/headline.json`, so another site (the Sentient Horizons Projects page, which read the stages delivered and the record's date from `data/project.toml` on the raw main branch) can take the project's few numbers from the site itself. This README's deploy-gate paragraph and the repository README's status paragraph were brought up to the day. The first adoption from the Sentient Horizons design review of 2026-10-17 (`design/reviews/2026-10-17-lessons-review.md` in that repository, sections 8 and 9), on John's ruling of the same day that each project takes its first adoption and serves its headline from its site.
- 2026-10-17: the site wears its own skin, Notebook, ruled by John from the proposal of the same day and merged as pull request 176 (the deploy ran on the merge): a cool off-white page with a faint grid behind the first screen, the ink violet, a slate for the meters, the monospace on the labels, light by default; the stylesheet split into `skin.css`, the shared `shell.css` 2.0.1 copied unchanged, and the site's own rules.

- 2026-10-16: the home page opens on one number a stranger can hold, the count of delivered stages on the ladder (3 of 8) in the monospace with aligned figures, with the stage names as its claim in the sans; the "where we are" and "where we are going" paragraphs moved under it at the reading size instead of the large sans. Asked for by John on 2026-10-16 after the Sentient Horizons design review of the same day found this the one home page in the family that gave a stranger nothing to hold. Pictures at 1280 pixels before and after: `docs/home-page-2026-10-16-before.png` and `docs/home-page-2026-10-16-after.png`. Not deployed: the site's deploy stays behind John's gate. Checked the same day: the light-theme button bug the rest of the family had (the standard's light-theme link colour outranking the button's text colour, found on theupgradetree.com on 2026-10-16) does not affect this site, whose stylesheet has carried its own override since 2026-09-20.
