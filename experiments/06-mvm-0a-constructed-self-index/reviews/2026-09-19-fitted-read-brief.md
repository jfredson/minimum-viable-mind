# Brief — the fitted linear read at all eleven positions

*Ruled 2026-09-19 (Pacific) as decision 2 on the Gate B review of the
linear-read closure (ledger RT-33, RT-44, RT-47). Local, $0, existing
checkpoints. Under the execution-gates ruling of 2026-09-19 this needs its
method committed before any output, not a fresh go. Nothing registered is
touched; no registered verdict is read from it.*

## The question

Does a fitted linear classifier find own-agent identity at any of the
eleven positions where the difference-of-averages read found none?

## What to run

The same eleven positions, five layers and three 30M checkpoints as the
powered eleven-position sweep (`powered-position-sweep-method.md`), read
with the logistic-regression classifier already implemented in
`src/probe_target_diagnostic_a3.py`, on the **four-answer register-index
target**, which is the one that classifier has already been run on at the
marker position (`probe_target_diagnostic_a3_*.json`). The marker-word
target (more than eight answers) was skipped there as too slow; run it too
if it fits in the session, and say so either way.

## What the method file must state before the run

1. The classifier, its regularisation, and the fold scheme, with folds and
   shuffle draws seeded **per test**, not per layer (RT-39).
2. The null: shuffled-label draws, how many, and the family-adjusted bar
   for the number of tests actually run, stated as a number.
3. The positive control for the register index, or the statement that
   there is none and what that costs the reading (RT-35). The marker-word
   control at the input position is not a register-index control.
4. The pre-stated cells: what "found" and "not found" mean per test, and
   the degeneracy precondition (accuracy equal to the majority-class rate).
5. The anchor reproduction: the marker-position register-index numbers
   already on the record (0.48–0.535 on seed 1) must reproduce, or the run
   is a failed instrument and says nothing.
6. If cheap: the state-space geometry (share of variation in the top ten
   directions) at each position, not just the anchor (RT-40).

Commit the method file and the code, then run, then commit the findings.
The findings report every cell, the detectable-signal size (RT-37), and
the degeneracy hits (RT-38), and quote the pilot-versus-seeds legibility
gap as a caveat rather than resolving it (RT-36).

## What the findings may and may not say

They may say where a fitted linear read finds own-agent identity and where
it does not, on these checkpoints, at these positions. They may not say
the linear-read line is closed, or that the models carry no self-index;
under Amendment A3 §3.2 nothing counts as localized or as absent until
causal patching has also run (RT-49, RT-50). The findings go through a
Gate B review before any of this enters STATUS.md.
