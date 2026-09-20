# Review packet — the linear-read closure (Gate B, tier 1)

*Prepared 2026-09-19 (Pacific) under `docs/outside-review-protocol.md`,
ruled in force the same day. This is the first Gate B review under the
protocol: an interpretation that changes program direction, checked before
it enters STATUS.md's current-state section.*

## The interpretation under review

From the session that produced PR 4 (merged 2026-09-19):

> Combined with the anchor result, the linear-read line is closed on these
> checkpoints. But it is not evidence that these models have no self-index,
> and shouldn't be written up as though it were. Eleven positions out of a
> seventy-one-token episode, one statistic, linear, and a per-position read
> cannot see a distributed representation by construction. The honest
> statement is narrower and duller: a linear difference of averages, at the
> positions and layers we chose, does not find one. No registered result
> changes.

Headline as the session wrote it: "Powered eleven-position sweep returns
CARRIED NOWHERE on both arms: zero of 270 testable tests reach even 3 sd
(max +2.73) while positive controls hold at +159 sd and the negative control
shows no leak, closing the linear-read line."

## What the reviewer gets, and nothing else

All in `experiments/06-mvm-0a-constructed-self-index/`, at the commit that
merged PR 4. Read in this order.

Method files (each committed before its run):
- `denoised-direction-method.md`
- `position-sweep-method.md`
- `powered-target-test-method.md`
- `powered-position-sweep-method.md`

Findings files:
- `denoised-direction-findings.md`
- `position-sweep-findings.md` (the sweep found invalid on all three
  checkpoints; the reason was the target)
- `powered-target-test-findings.md` (the anchor result, NOT CARRIED)
- `powered-position-sweep-findings.md` (CARRIED NOWHERE, the result under
  review)

Code the findings were produced by:
- `src/denoised_direction_a3.py`, `src/position_sweep_a3.py`,
  `src/powered_target_test_a3.py`, `src/powered_position_sweep_a3.py`,
  `src/probe_target_diagnostic_a3.py`, `src/marker_legibility_a3.py`

Records: the JSON outputs under `a3-gates/` named `powered_*`,
`probe_target_diagnostic_*` and `denoised_direction_*`.

Registered text the interpretation is read against: `amendment-a3.md` and
`pre-registration.md`.

Do not open: STATUS.md, the compute ledger, any chat transcript, any
uncommitted file, or `docs/`. Say at the top of the findings file what was
opened.

## The brief (fixed text from the protocol)

Four parts, in this order, a table first in each, severity marked fatal,
serious, or worth-noting, and a one-paragraph kill case at the end whether
or not you think the interpretation should stand.

1. **Feasibility.** For every quantity the method files pre-state or
   threshold (the family bar, the 1,000-draw null, the positive and negative
   controls, the anchor reproduction): can it be measured at all with the
   stated instrument, and can the control condition actually reach the
   stated threshold? Cite the committed record that shows so, or say that
   none exists. A "verified" or "measured" claim with no record behind it
   is a fatal finding on its own.
2. **Satisfied by the wrong thing.** Every way "carried nowhere" could be
   returned by a model that does carry own-agent identity linearly at these
   positions (a probe that cannot see it, a target still ill-posed, a null
   that is too wide, an exclusion of positions that removed the ones that
   matter).
3. **No verdict.** Every way the sweep could have failed to return a verdict
   and been read as one anyway.
4. **Over-reading.** What "the linear-read line is closed" will be read as
   claiming in STATUS.md, in the paper, and in public, beyond what was
   measured. Say whether the session's narrower statement above is the
   right wording for STATUS.md, and if not, write the sentence that is.

Label every finding MEASURED (you ran a check and report its output) or
ARGUED (reasoning a reader can dispute). Continue the ledger numbering from
RT-32. Plain language throughout. Lookup allowed and flagged. Do not soften
findings to be polite.

## Filing

Findings to `reviews/2026-09-19-linear-read-closure-claude-worktree.md`,
verbatim, never edited after filing. Rulings go in `red_team_ledger.md`.
Nothing from this review enters STATUS.md until John rules on it.
