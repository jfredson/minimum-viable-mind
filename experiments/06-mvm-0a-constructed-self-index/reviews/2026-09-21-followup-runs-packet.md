# Review packet — the two follow-up localization runs (Gate B, tier 1)

*Prepared 2026-09-21 (Pacific) under `docs/outside-review-protocol.md`.
Gate B: an interpretation that bears on program direction, reviewed
before it enters STATUS.md. Both runs were authorised 2026-09-20 as
decision 3 on the fitted-read review (ledger RT-76, RT-82) and briefed in
`reviews/2026-09-20-followup-runs-brief.md`. They are reviewed together
because the interpretation under review joins them.*

## The interpretation under review

From the session that ran both (PR 11, branch
`worktree-followup-runs-l2a-standardised`, commits `7745d4a` method and
code, `f75accd` run 1 findings, `d038f07` run 2 findings):

> Run 1, the other agent's index (registered matched control L2(a)):
> FOUND NOWHERE. The exclusion confound proposed in RT-82 is not
> supported. Pointed at agent B's index, the position in question gives
> +1.00, +1.40, +1.73 against a 3.38 bar, while the instrument finds that
> target at +52.81 where agent B's marker is the input token, and finds
> the exclusion effect itself at the model's own marker token. So the
> own-index pattern is now unexplained, not explained away.
>
> Run 2, the standardised refit: FOUND NOWHERE, sub-pattern "found on
> seeds but not the pilot", but one testable cell cleared the bar: seed
> 2, the other agent's revision value, layer 3, +3.43 with 0 of 200 draws
> beating it. First time anything in this line has crossed a
> family-adjusted bar at a position where the answer is not in the
> current token. Standardising did not broadly raise sensitivity (mean
> margins unchanged to two decimals) but made every fit converge (0% hit
> the pass cap against 13.5 / 22.3 / 73.6% unscaled).
>
> Three independent lines now point at that one position, and none is
> strong enough alone: one cell in 135 is what a 5% family bar permits by
> chance about one time in twenty; 200 draws certify only about 2.58 sd
> against the 3.38 needed; the layer moved (4 to 3); the pilot does not
> show it.

The question for this review: what may STATUS.md say about the other
agent's revision value, and what does the registration require before it
is anything more than an open item.

## What the reviewer gets, and nothing else

On branch `worktree-followup-runs-l2a-standardised` at `d038f07` (or main
once PR 11 is merged), in `experiments/06-mvm-0a-constructed-self-index/`:

- `reviews/2026-09-20-followup-runs-brief.md` — what the runs were told
  to do.
- `other-index-position-sweep-method.md`, `standardised-refit-method.md`
  — committed before output (`7745d4a`).
- `other-index-position-sweep-findings.md`,
  `standardised-refit-findings.md` — the findings under review.
- `a3-gates/other_index_position_sweep_a3_*.json`,
  `a3-gates/standardised_position_sweep_a3_*.json` — the records.
- `src/other_index_position_sweep_a3.py`,
  `src/standardised_position_sweep_a3.py`, and the parent
  `src/fitted_position_sweep_a3.py`.
- The prior review and rulings these runs answer:
  `reviews/2026-09-20-fitted-read-claude-worktree.md`, the ledger block
  RT-70 to RT-93, and `fitted-position-sweep-findings.md` with its
  correction note.
- Registered text: `amendment-a3.md` §3.2 and §L2 (matched controls),
  `pre-registration.md` (the two-method requirement and the
  instrument-failure reading).
- `separation-clause-requirements.md` Part 3 (what still needs a
  localized lesion).

Do not open: STATUS.md, `docs/`, any chat transcript, any uncommitted
file. Say at the top what was opened.

## The brief (fixed text from the protocol)

Four parts, a table first in each, severities fatal / serious /
worth-noting, a one-paragraph kill case at the end.

1. **Feasibility.** Check each method file against the brief's
   requirements (per-test seeding, bar as a number, positive control for
   the register index or the statement that there is none, pre-stated
   cells and degeneracy rule, anchor reproduction, standardisation per
   fold from training statistics only, regularisation chosen without
   looking at sweep results, geometry). Check the detectable-signal size
   is calibrated against the read's measured ceiling, not 1.0. Check the
   L2(a) run is the registered matched control as §L2 defines it
   (matched in rank and probe accuracy) or say how it departs. A
   requirement claimed met with no record is fatal.
2. **Satisfied by the wrong thing.** For run 1: every way FOUND NOWHERE
   on the other agent's index could be returned while the exclusion
   confound is still live. For run 2: every way the one clearing cell
   could be an artefact (the family bar at 135 tests when three
   checkpoints read the same episodes; 200 draws; the layer shift; the
   pilot's absence; standardisation itself).
3. **No verdict.** Every way "three independent lines point at one
   position" could be read as a result when the pre-stated cells say it
   is not one, and every way the two runs could have failed to answer
   RT-82 and RT-76 and been read as answering them.
4. **Over-reading.** Write the STATUS.md paragraph. Say whether "the
   own-index pattern is now unexplained, not explained away" is
   supportable. State what the registration requires before the other
   agent's revision value becomes a localization target (Part 3 of the
   requirements; probe plus patching), and whether the registered blind
   arm (public path step 3) should run before or after any follow-up on
   this position. If a further $0 run would settle the one cell (more
   draws, a held-out replication), name it and its cost in
   processor-hours; do not recommend spend.

Label every finding MEASURED or ARGUED. Continue the ledger numbering from
RT-117. Plain language throughout. Lookup allowed and flagged. Do not
soften findings to be polite.

## Filing

Findings to `reviews/2026-09-21-followup-runs-claude-worktree.md`,
verbatim, never edited after filing. Rulings in `red_team_ledger.md`.
Nothing enters STATUS.md until John rules.
