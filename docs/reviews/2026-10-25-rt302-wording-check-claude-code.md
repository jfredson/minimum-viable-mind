# RT-302 wording check: ruling 4 carried beyond section 2

*Saved by the session that made the change; the report is the checker's, condensed only by removing nothing of substance, and what was done about each finding is at the end.*

**Checker:** Claude Code, a session that did not make the change, working read-only.
**Commit checked:** `9216f2a` (2026-10-25), on branch `claude/rt302-ambiguous-wording-2026-10-25`.
**Checked against:** the row for RT-302 (the router argument's missing step) in `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`, ruling 4 in `docs/rulings/2026-10-12-two-sided-question-section-2-v3.md`, and the figures in `experiments/01-self-indexing-removal-test/removal-test-findings.md`.
**Site check:** `python3 scripts/export_site.py --check` passes.

## Checks

**(1) Every place the row names is brought into ruling 4's form: passes, with one gap (finding 1).** The four `STATUS.md` lines the row named on 2026-10-12 (175, 521, 3207, 3208, traced at `bfd1d5d`) are now the pull request 163 entry at `STATUS.md` line 704, the ruling entry at `STATUS-archive.md` line 281, and the 2026-07-18 dated note at `STATUS-archive.md` lines 2968–2969. Each has a dated pointer; none was edited. The rulings file of 2026-10-07 has a dated note under decision 2; version 2's section 3 has a dated note. In `data/project.toml`, goal G2, stage 1, question Q1 and finding F1 were rewritten and F21 got a dated note. `learned.astro` and `eli5.astro` were rewritten.

**(2) No remaining sentence in the site data or pages asserts the missing step: fails on one finding (finding 1).** Searched `site/` and `data/` for "cheaper account", "could not discriminate", "could never", "chose the" and "taken in advance". The only hit that matters is F21. The "could never" hits elsewhere are about other experiments.

**(3) No figure changed, and every figure matches the source: passes.** +0.033 with an interval from −0.133 to +0.200; drops of 0.219, 0.100 and 0.133; differential +0.156. `data/headline.json` changed only its regeneration date.

**(4) The new wording does not overclaim the other way: passes.** Optional: goal G2's "a centre would also have damaged every task set" is more exact as "the book predicts a centre would also have damaged…".

**(5) Plain language: passes, with small points.** The data file swaps between "battery" and "task set". In both dated notes, "finding RT-302" has no plain phrase beside it.

**(6) The dated notes are accurate about authorship and paths: passes**, except that the rulings note's "the site data and the site's pages carry the ambiguous form since 2026-10-25" is not yet fully true because of F21's title.

## Findings

1. **F21's title, shown on the public learned page, still asserts the missing step (serious; blocks closing).** "Experiment 1's router control cannot separate bookkeeping from a centre; it chose the cheaper account in advance". Its `what` keeps "On the three batteries the predictions coincide." Fix: retitle it, change that sentence to "both accounts fit the damage seen", and "cannot separate" to "did not separate" in the "so what".
2. **The router-check paragraph in `STATUS-archive.md` (lines 226–236) has no pointer (minor).** Add the same dated pointer.
3. **The pointer in `STATUS.md` is about 20 lines from the label it qualifies (minor).** Name "the experiment A label in the pull request 163 sentence above".
4. **Version 2 states the step in section 0 and section 2 too (minor; outside the closing condition).** Extend the dated note, or leave it.

## Other files still carrying the old label or the missing step

The repository is public on GitHub.

| File | For outside readers? | Inside the closing condition? |
|---|---|---|
| `README.md` line 51 | Yes | No, but it should follow; one phrase |
| `explainer.md` line 33 | Yes | No; a dated gloss on the bold label would be enough |
| `drafts/paper-removal-test-nature-draft.md` lines 23, 61, 148–149, 375 | Repo-internal draft | No; owed when the paper is next revised |
| `docs/outside-reader-approach-note-2026-10-17.md` line 114 | Outreach draft | No; check before any use |
| Version 1 of the proposal, `docs/outside-perspective/*`, `docs/reviews/*`, review packets | No (dated records) | No; leave them |

## Overall verdict

RT-302 cannot close on `9216f2a` as it stands, but it is one small edit away: once F21's title and its "predictions coincide" sentence are reworded, it can close, and a re-search of `data/` and `site/` is enough to confirm the fix.

---

## What was done (2026-10-25, by the session that made the change)

- **Finding 1:** applied as suggested. F21 is now titled "Experiment 1's router control did not separate bookkeeping from a centre (argued 2026-10-07; read as an ambiguous result under ruling 4 of 2026-10-12)"; "both accounts fit the damage seen"; "did not separate". A re-search of `data/` and `site/src/pages/` for "cheaper account", "could not discriminate", "predictions coincide" and "cannot separate" returns nothing.
- **Findings 2 and 3:** applied (a pointer after the router-check paragraph in `STATUS-archive.md`; the `STATUS.md` pointer names the pull request 163 sentence).
- **Finding 4:** the dated note in version 2 now says it covers sections 0 and 2 as well.
- **Point 4 and point 5:** goal G2 now reads "the book predicts a centre would also have damaged every battery"; both dated notes carry the plain phrase "the router argument's missing step" beside RT-302.
- **Other files:** `README.md` gets the one-phrase change and `explainer.md` a dated gloss after its bold label. The paper draft and the outreach note are left, as the table says.
- RT-302 is marked closed in the ledger, with a dated note giving the new count (closed with the claim checked 4; argument accepted 17; John's reading 1; open 0).
