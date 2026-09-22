# Review packet — the Amendment A3 closure text (Gate A, tier 1)

*Prepared 2026-09-21 (Pacific) under `docs/outside-review-protocol.md`.
Gate A: registered text before the registration commit, both tiers, with
the closure rule. This packet is the tier 1 pass; the tier 2 packet (two
other-lab models, run by John) is built from this one plus the tier 1
findings.*

*Protocol amendments adopted 2026-09-20 (December-result ruling, item 6)
and applied here ahead of the protocol text edit: "unlikely" is struck
from the brief; the reviewer, not the author of a fix, verifies the
closure of any fatal finding; the measurement-rehearsal requirement
concerns registrations that pre-state a measurement, and this closure
block pre-states none. The reviewer may contest that last reading in
part 1.*

## The target

`docs/a3-closure-text-draft-2026-09-21-v2.md`, in full: the dated closure
block to be appended to `amendment-a3.md`. Its outcome word is *not
testable*; its claim sentence is that the ownership input is load-bearing
on three seeds, that whether an internal center formed around it is not
testable here, and that its degree is unmeasured.

## What the reviewer gets, and nothing else

In `experiments/06-mvm-0a-constructed-self-index/` unless noted:

- The target, and version 1 beside it for the diff only.
- `amendment-a3.md` and `pre-registration.md` in full (the registered
  text the closure block joins; the loss conditions; §3.1, §3.2, §L2).
- `ceiling-measurement-findings.md`, `ceiling-defect-2026-09-17.md`.
- `seeds-endpoint-findings.md`, `gate2-pilot-findings.md`.
- `control-learnability-pilot.md`, `control-learnability-pilot-findings.md`.
- `separation-clause-requirements.md`.
- `fitted-position-sweep-findings.md` and its correction note,
  `other-index-position-sweep-findings.md`, `standardised-refit-findings.md`,
  `powered-position-sweep-findings.md`.
- `red_team_ledger.md`, blocks RT-33 onward (every ruling the closure text
  must honour).
- `docs/step4-control-battery-proposal-2026-09-20-v2.md`,
  `docs/rulings/2026-09-20-center-as-degree.md`,
  `docs/rulings/2026-09-20-december-result-roadmap.md`,
  `docs/competing-mechanisms-2026-09-20.md`.
- `compute-ledger.md`, running totals only.

Do not open: STATUS.md, any chat transcript, any uncommitted file. Say at
the top what was opened.

## The brief (fixed text from the protocol, as amended 2026-09-20)

Four parts, a table first in each, severities fatal / serious /
worth-noting, a one-paragraph kill case at the end.

1. **Feasibility.** Every number and every "measured", "verified" or
   "ran" claim in the block cites a committed record that contains what
   the sentence says: the ceiling of 1.0; the three seeds' intact and
   lesioned scores; the pilot's 0.3125 against 0.60; the fitted, refit,
   and other-agent reads; "never run and has no code" for patching; the
   money. Check that "not testable" is the registered word for the loss
   condition that fired, quoting the pre-registration. A claim with no
   record behind it is fatal.
2. **Satisfied by the wrong thing.** Every way this block could close A3
   while leaving something the registration requires undone or misnamed:
   a discriminator that was run and is not named; a registered bin the
   result should land in other than *not testable*; a sentence that
   reads as a finding of absence; a sentence that hands the paper a claim
   the registered text withholds (the ledger's RT-113 and RT-119).
3. **No verdict.** Every way the block could be registered and still
   leave the paper unable to say what A3 supports, or the successor
   unable to inherit what it needs (the ceiling precondition, the
   two-instrument requirement, the deferred marker-word read).
4. **Over-reading.** What each sentence will be read as claiming in the
   paper and in public. Write the closure block as it should be
   registered, if it differs.

Label every finding MEASURED or ARGUED. Continue the ledger numbering from
the last number on main at the time of filing, and say what it was. Plain
language throughout. Lookup allowed and flagged. Do not soften findings.

## Closure rule (applies before the registration commit)

Every fatal finding gets a closure line in the ledger naming the commit
that lands the fix and a MEASURED check by this reviewer, not the author
of the fix. Every "verified", "measured", "ran" or "never run" in the
registered block cites the committed record by file name.

## Filing

Findings to `reviews/2026-09-21-a3-closure-claude-worktree.md`, verbatim,
never edited. Rulings in `red_team_ledger.md`. If the review changes the
block, version 3 is written beside version 2 with the review cited. The
tier 2 packet is assembled after this review files. Nothing is appended to
`amendment-a3.md` until both tiers have filed, John has ruled, and the
closure rule is satisfied.
