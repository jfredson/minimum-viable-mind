# Review packet — the fitted linear read at all eleven positions (Gate B, tier 1)

*Prepared 2026-09-20 (Pacific) under `docs/outside-review-protocol.md`.
Gate B: this run was decision 2 of the 2026-09-19 review of the
linear-read closure, and whether the line is retired on it is a
direction question, so its interpretation is reviewed before it enters
STATUS.md.*

## The interpretation under review

From the findings on branch `worktree-fitted-read-sweep` (commit
`9080d02`), headline: FOUND NOWHERE, nothing on any checkpoint. Across
nine testable positions, five layers and three checkpoints (135 tests) a
fitted linear classifier does not find the register index anywhere at the
family-adjusted bar of 3.38 sd; one test on one checkpoint reached
MARGINAL. The instrument check reproduced all fifteen recorded numbers
exactly; the positive control at position 6 holds on all three
checkpoints at +34 to +54 sd. The findings say explicitly that this is
not a finding of absence.

The question for this review: with both the difference-of-averages read
and the fitted read now empty at these positions, what may STATUS.md say
about the linear read, and what does the registration (probe plus causal
patching, RT-49, RT-50) still require before anything is called localized
or absent.

## What the reviewer gets, and nothing else

At commit `9080d02` on `worktree-fitted-read-sweep` (or main once merged),
in `experiments/06-mvm-0a-constructed-self-index/`:

- `reviews/2026-09-19-fitted-read-brief.md` — what the run was told to do.
- `fitted-position-sweep-method.md` — committed before output (`f84db43`).
- `fitted-position-sweep-findings.md` — the findings under review.
- `a3-gates/fitted_position_sweep_a3_*.json` — the records.
- `src/fitted_position_sweep_a3.py`.
- The prior review and its rulings, since this run answers them:
  `reviews/2026-09-19-linear-read-closure-claude-worktree.md`, its
  addendum, and the RT-33 to RT-51 block of `red_team_ledger.md`.
- `powered-position-sweep-findings.md` — the difference-of-averages
  result this pairs with.
- Registered text: `amendment-a3.md` §3.2 and `pre-registration.md`.

Do not open: STATUS.md, `docs/`, any chat transcript, any uncommitted
file. Say at the top what was opened.

## The brief (fixed text from the protocol)

Four parts, a table first in each, severities marked, a one-paragraph
kill case at the end.

1. **Feasibility.** Check the brief's six requirements against the method
   file: per-test seeding (RT-39), the bar stated as a number, a
   register-index positive control or the statement that there is none
   (RT-35), the pre-stated cells and degeneracy rule, the anchor
   reproduction, geometry at the other positions (RT-40). A requirement
   claimed met with no record is a fatal finding.
2. **Satisfied by the wrong thing.** Every way FOUND NOWHERE could be
   returned by a model that carries a linear register-index signal at
   these positions: regularisation, fold size, the two untestable
   positions, the classifier's capacity against 448 dimensions on 400
   episodes.
3. **No verdict.** Including the MARGINAL test and what the pre-stated
   cells say a marginal means.
4. **Over-reading.** Write the STATUS.md sentence. Say whether "no linear
   read finds own-agent identity at the nine testable positions" is now
   supportable, and state what the registration still requires (causal
   patching) before "not localized" or "absent" can be said.

Label every finding MEASURED or ARGUED. Continue the ledger numbering
from where the control-learnability review leaves off, or from RT-52 if
that review has not filed; say which. Plain language. Do not soften.

## Filing

Findings to `reviews/2026-09-20-fitted-read-claude-worktree.md`, verbatim,
never edited after filing. Rulings in `red_team_ledger.md`. Nothing enters
STATUS.md until John rules.
