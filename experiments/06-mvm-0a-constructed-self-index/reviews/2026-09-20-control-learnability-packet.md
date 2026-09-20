# Review packet — the control-learnability pilot (Gate B, tier 1)

*Prepared 2026-09-20 (Pacific) under `docs/outside-review-protocol.md`.
Gate B: an interpretation that changes program direction, reviewed before
it enters STATUS.md's current-state section. This one also feeds public
path step 4, the 2026-10-04 control-battery decision, so under Gate C the
proposal that carries that decision will cite this review.*

## The interpretation under review

From the session that ran the pilot (commits `062636e`, `a569a35`, both
on main):

> The control battery does not learn when properly supervised. It scored
> 0.3125 (sd 0.0240) after an intervention that quadrupled its per-row
> gradient weight and took its share of the query gradient from about a
> third to about two thirds. The three existing checkpoints, with none of
> that, scored 0.2877, 0.3057 and 0.3195. Against the pre-stated cells:
> 0.42 sd below the 0.3227 boundary, 11.98 sd below 0.60. The cell is DID
> NOT LEARN. Both secondary cells pass, so this is a real answer, not a
> failed intervention. Supervision was not the binding constraint. What
> is left are the explanations that are not about supervision: the
> reversed rendering, the missing private route, and an answer that
> appears in no turn.

The session's own qualifications, which the review should test rather
than take on trust: across six evaluation seeds the control ranged
0.2850 to 0.3460, so a rerun could formally land in PARTIAL; and the
control is not inert, since it falls under the lesion from 0.3125 to
0.2613.

## What the reviewer gets, and nothing else

All in `experiments/06-mvm-0a-constructed-self-index/` at commit
`a569a35`. Read in this order.

- `control-learnability-pilot.md` — the pre-statement, committed before
  the code existed (`7eee3c5`). The cells are read against this.
- `control-learnability-pilot-findings.md` — the findings under review.
- `a3-gates/endpoint_a3ctl_30m_seed0.json` — the full-budget endpoint
  (step 55,116), the record the cells are read on.
- `a3-gates/endpoint_a3ctl_30m_seed0_PARTIAL_step51500.json` — the
  partial-checkpoint endpoint, for comparison only.
- The training log and trajectory record for the run, wherever the
  findings file says they are.
- `src/train_a3.py` and `src/launch_ctl_pilot.sh` — the loss change
  (`ee7fc91`) and the launcher; the self-test that claims the off path is
  bit-identical to the old pooled term.
- `compute-ledger.md`, the two rows dated 2026-09-19 (pilot) and
  2026-09-20 (recovery) only.
- `gate2-pilot-findings.md` and `seeds-endpoint-findings.md` — the three
  comparison checkpoints' control scores.
- Registered text the interpretation is read against: `amendment-a3.md`
  (the control battery's definition, its ceiling, and §3.2) and
  `ceiling-defect-2026-09-17.md`.

Do not open: STATUS.md, `docs/`, the A4 files, any chat transcript, any
uncommitted file. Say at the top of the findings file what was opened.

## The brief (fixed text from the protocol)

Four parts, in this order, a table first in each, severity marked fatal,
serious, or worth-noting, and a one-paragraph kill case at the end whether
or not you think the interpretation should stand.

1. **Feasibility.** For every quantity the pre-statement names: is the
   0.3227 boundary the right number (it is the control's ownership-blind
   ceiling as registered; the 2026-09-17 defect says that ceiling was
   never attacked), is the 0.60 boundary reachable by this battery in
   principle, and did the intervention actually deliver the supervision
   it claims (per-row weight, share of rows), citing the training log or
   the code. A "verified" or "measured" claim with no record behind it is
   a fatal finding on its own.
2. **Satisfied by the wrong thing.** Every way DID NOT LEARN could be
   returned by a control battery that would learn under supervision: an
   intervention that did not reach the control's rows, a loss term on
   the wrong scale, an evaluation that cannot see what was learned, a
   ceiling boundary that is itself wrong.
3. **No verdict.** Every way the run could have failed to answer the
   supervision question and been read as answering it, including the
   seed-1-only design and the six-seed spread straddling the boundary.
4. **Over-reading.** What "supervision is not the binding constraint"
   will be read as claiming in STATUS.md, in the step 4 proposal, and in
   the paper, beyond what one seed at one weight setting measured. Say
   whether the finding supports narrowing step 4 to "option D or close
   A3", or whether a cheaper supervision variant is still live. Write the
   sentence that should go in STATUS.md.

Label every finding MEASURED or ARGUED. Continue the ledger numbering
from RT-51. Plain language throughout. Lookup allowed and flagged. Do not
soften findings to be polite.

## Filing

Findings to `reviews/2026-09-20-control-learnability-claude-worktree.md`,
verbatim, never edited after filing. Rulings go in `red_team_ledger.md`.
Nothing from this enters STATUS.md or the step 4 proposal until John
rules on it.
