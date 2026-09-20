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

## Keeping the site current

`site/` is the project's internal visualizer (built 2026-09-20; how it works in
`site/README.md`, decisions in `docs/site-plan-2026-09-20.md`). It renders
`data/project.toml`, the structured twin of `STATUS.md`: goals, the stage
ladder, the questions, the ideas on the table, findings, next steps, spend,
and a timeline. **Any session that adds a "WHERE THINGS STAND" entry to
STATUS.md also updates `data/project.toml` in the same commit**: bump
`project.updated_on` and rewrite the two "where" paragraphs, add a
`[[timeline]]` row at the top, add any `[[findings]]`, refresh `[[next_steps]]`
and idea statuses, adjust stage progress and `[spend]`. Write it in plain
language with every code name explained on first use, the same rule as the
scheduled reviews. Then validate:

    cd ~/Code/minimum-viable-mind && .venv/bin/python scripts/export_site.py --check

STATUS.md stays the record of record; where the two disagree, fix the data
file. Deploying the site is a launch and stays behind John's gate.
