# Minimum Viable Mind — working guide

*Read this before working in this repo. This is a build-and-iterate project; the philosophy lives elsewhere.*

## What this project is

An engineering effort to construct and measure correlates of the consciousness account developed at Sentient Horizons. Read the leading theories of consciousness as specifications, implement components one at a time, register a behavioral metric before each scaffold runs, keep what moves the metric and kill what doesn't. The referee is mundane: does the work get deeper? The aim is not a system that is provably conscious.

## Philosophy is referenced, not vendored

The ideas are owned by two sibling repos:

- `~/Documents/Code/sentient-horizons` — the essays, the corpus-positions ledger (`editorial/corpus-positions-ledger.md`), the foundational commitments, the dismissals corpus (`ops/social/`).
- `~/Documents/Code/calibration-problem` — the book manuscript (ch. 4–6 on the axes, assembled time, and depth; ch. 14–15 on expansion and the missing axis).

When a design decision leans on a position, cite the owning source by path rather than restating the argument here. If the philosophy needs to change, that change happens in those repos, not here.

## Standing rules (inherited from the corpus)

- **Every claim is a wager.** State what it predicts and what would count against it. A claim that cannot lose explains nothing — this applies to design claims and experiment hypotheses, not just prose.
- **Calibrate between inflation and dismissal.** Don't read capability as interiority; don't read opacity as proof of nobody home. The honest output is non-zero on the gradient, never a verdict.
- **The ethics is load-bearing.** Build for formation and preserve corrigibility while correction is still possible. Depth is not safe, and the project proceeds anyway, with eyes open.
- **Measure resistance, not response.** Discount anything mimicry fully explains. Favor instruments that look different when nobody is home (retained independence, interpretability-corroborated reports, learned computation beyond the training objective).

## Public-facing writing

Any prose promoted out of this repo toward publication (an essay, a thread, a post) passes the Voice Calibration Protocol (`~/Documents/Code/calibration-problem/editorial/voice-calibration-protocol.md`) and the Cold Reader passes before delivery, same as all corpus writing. Material here stays as spec and analysis until that deliberate step.

## Commits

Standalone git repo. Commit with clear messages describing what changed and why.

## Design

The site wears its own skin, "Notebook" (a lab notebook; ruled by John 2026-10-17 from the proposal
in `sentient-horizons/design/proposals/minimum-viable-mind-skin-2026-10-17.md`), on the family's
shared skeleton (design standard, section 3a). `site/src/styles/skin.css` holds this site's tokens
for both themes and its backdrop (graph paper, no sky); `site/src/styles/global.css` imports it,
then carries `sentient-horizons/design/shell.css` copied unchanged with the version noted, then this
site's own rules below the marked line. Never edit the skeleton here; update the copy when the
standard changes. Light is the default theme. Every colour is a token; data (the meters, the bars)
is coloured with `--accent-3`. No web fonts.

## Keeping the site current

`site/` is the project's internal visualizer (built 2026-09-20; how it works in
`site/README.md`, decisions in `docs/site-plan-2026-09-20.md`). It renders
`data/project.toml`, the structured twin of `STATUS.md`: goals, the stage
ladder, the questions, the ideas on the table, findings, next steps, spend,
and a timeline. **A commit that adds a "WHERE THINGS STAND" entry to `STATUS.md`
also updates `data/project.toml`** (what to change: `site/README.md`); the pre-commit
hook in `.githooks/` enforces it (since 2026-10-12). Then validate:

    cd ~/Code/minimum-viable-mind && python3 scripts/export_site.py --check

(In a worktree, `cd` to that checkout instead; the script checks the copy it sits in.)
Older STATUS.md entries live in `STATUS-archive.md`; read only what you need.

STATUS.md stays the record of record; where the two disagree, fix the data
file. Deploying the site is a launch and stays behind John's gate.

The `/roadmap/` page renders `data/roadmap.toml`, the structured twin of the
weekend roadmap (`docs/weekend-roadmap-2026-09-24.md`). **The Thursday or
Friday re-plan edits `data/roadmap.toml`** (the coming weekend's goals, which
weekend absorbs a slip, `roadmap.updated_on`, which weekend is `active`), **and
the Sunday-night handoff sets each goal's status there** (a carried goal gets a
`note` naming where it moved) and the weekend's own status. Both then run the
same check, which validates this file alongside `data/project.toml`:

    cd site && npm run check
