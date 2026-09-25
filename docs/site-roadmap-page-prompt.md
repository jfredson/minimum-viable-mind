# Session prompt: the /roadmap/ page on the project site

*Written 2026-09-24 (Pacific) by the Cowork planning session. Model: Opus 5.5
(it is site code against an existing design system). Independent of the three
weekend-1 sessions already running; it can start now. Checker prompt at the
end. Deploying the site stays behind John's gate (CLAUDE.md); this session
builds and previews only.*

---

## Writer prompt

```
You are working in ~/Code/minimum-viable-mind. Read CLAUDE.md, site/README.md,
docs/site-plan-2026-09-20.md, docs/weekend-roadmap-2026-09-24.md, and
data/roadmap.toml (the new data file this page renders; read its header
comment for the vocabularies) before anything else. Work in your own git
worktree under .claude/worktrees/, branched from main, and open a pull request
at the end; never commit to main directly. Write in plain language, every code
name explained on first use. Do not deploy the site; do not launch or spend
anything. Dates are Pacific and absolute (YYYY-MM-DD). When you finish, append
one worklog entry to TimeAssembler (project Minimum Viable Mind) and put your
PR number and a three-line summary at the end of your last message.

Task: add a /roadmap/ page to the Astro site that renders data/roadmap.toml,
in the site's existing design system (the Belt Equation stack; use the same
components, spacing and status labelling as /ladder/ and /learned/), and
shows both the plan and the progress against it on one page.

1. Data. Extend scripts/export_site.py to validate data/roadmap.toml (the
   vocabularies in its header; every weekend's start <= end; weekends in
   order; every goal id unique; every milestone date a real date) and write
   site/src/data/roadmap.json beside project.json. Extend src/lib/project.ts
   (or add src/lib/roadmap.ts) with the typed view and the human labels for
   every status code. Keep `npm run check` covering both files.

2. Page. /roadmap/ with, top to bottom:
   - The title, the one_line, the question, and the two rules (weekday and
     re-plan), from [roadmap].
   - A progress strip: goals done / goals that count (planned + done +
     carried + dropped, excluding not_needed; "carried" counts as not yet
     done, "dropped" counts against), weekends done / working weekends
     (blackout excluded), and days to each milestone (kill date 1, kill date
     2, wrap-up, hibernation) computed at build time from the build date,
     the way the index page computes days to hibernation. Use the site's
     Meter component for the bar.
   - A timeline strip of the thirteen weekends as segments, coloured by
     weekend.status (planned, active, done, partial, blackout, slack), with
     the four milestones marked as ticks on the same axis with their dates.
   - One card per weekend, in order: number, dates, days, title, status
     label; the outcome paragraph; the goals as a checklist where each goal
     shows its status (planned, done, carried, dropped, not needed) and its
     owner (John, agents, both) as a small label; John's items as a short
     list with the hours estimate; the "beside" line in muted text. The
     active weekend is visually distinguished. A goal with a `note` shows it
     inline (carried goals must say where they moved).
   - The extensions table: id, title, when, cost, teaches, status.
   - A footer line: "Plan: docs/weekend-roadmap-2026-09-24.md. Data:
     data/roadmap.toml. Updated <updated_on>."
   No JavaScript needed beyond what the site already uses; fully static.

3. Navigation. Add Roadmap to Nav.astro between the existing entries where it
   reads best (probably after the ladder), and add the row to the Pages table
   in site/README.md. Add a "Keeping it current" sentence to site/README.md
   and to CLAUDE.md's "Keeping the site current" section: the Thursday/Friday
   re-plan edits data/roadmap.toml and the Sunday handoff sets goal statuses
   there, then runs the check.

4. Build. `cd site && npm run check && npm run build` must pass; paste the
   output in the PR. Do not run deploy.
```

## Checker prompt (fresh session, either model)

```
[same header as above]

Check branch <writer's branch>: run `cd site && npm run check && npm run
build` and paste the output; open dist/roadmap/index.html and confirm with
grep that all thirteen weekend ids (W1 to W13), all four milestone ids and
all five extension ids appear (paste); break data/roadmap.toml on purpose in
a scratch copy (a goal status outside the vocabulary, a weekend out of order)
and confirm the check fails with a plain message (paste, then restore); confirm
`git diff --stat main..HEAD` touches only site/, scripts/export_site.py,
CLAUDE.md, site/README.md and nothing registered (paste). File at
experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-2X-site-roadmap-
page-check-claude-worktree.md with the real date.
```
