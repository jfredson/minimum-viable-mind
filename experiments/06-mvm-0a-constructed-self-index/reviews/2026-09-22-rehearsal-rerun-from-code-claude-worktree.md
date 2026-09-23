# Does the code still produce the committed record? — the measurement rehearsal, re-run from scratch

*2026-09-22 (Pacific). **INTERIM RECORD, FILED BEFORE THE LONG RUN.** This file
is committed now, empty of results, so that a re-run of roughly two hours of
laptop time cannot be lost the way the session before this one nearly lost its
own work. Results are appended to this same file when the run finishes.*

*Written under the workspace plain-language rule
(`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30).*

---

## The gap this closes

The measurement rehearsal is merged to the shared main line: the code sits at
`experiments/rehearsal-successor-measure/`, the findings at
`docs/2026-09-21-successor-measure-rehearsal.md`.

Two earlier checking sessions verified every figure in the findings **against
the committed output files**, exhaustively. Both checks ran in one direction
only. What nobody has done is the other direction: whether those committed
output files are what the code actually produces when you run it today.

That distinction is the whole point of this session. A document agreeing with a
record is not the same as the record having come out of the code. The programme
has twice this week been bitten by a number that agreed with everything except
reality.

## What is being done

1. The whole rehearsal is re-run end to end, from the committed code, in a
   scratch copy outside the repository at `~/.cache/mvm-rehearsal-verify/`.
   Nothing under `experiments/rehearsal-successor-measure/` is touched.
2. Every regenerated output file is compared against the committed one, byte
   for byte where the file is deterministic, and number by number where a file
   legitimately cannot be byte-identical (the two files that record wall-clock
   seconds).
3. Particular attention goes to the figures a registration review would be
   argued from: the separable arm reading exactly 0.0000 on three seeds; the
   entangled arm at 0.8727, 0.8848 and 0.8801; the freely trained arm at
   0.8863, 0.8366 and 0.8499; the three readings of the read's label at fits of
   0.256, 0.706 and 1.000, with their transplant readings; and the degree range
   of 0.9817 to 1.0000 that the two failing readings produce for an arm whose
   degree is 0.0000 by construction.
4. Any number that does not come back is reported, however small, with a
   judgement on whether the committed record or the fresh run is the right one.

The training is seeded, so it should come back **identical, not merely close**.
A seeded run that drifts is itself a finding and is reported as one.

## Decision on the half-finished run left behind: start clean

The brief for this session says a previous session got five of the ten toy
models retrained into `/tmp/rehearsal-check/`, and offers that directory for
re-use if its checkpoints can be shown to have come from the same code.

**That directory does not exist.** It is absent from `/tmp`, from
`/private/tmp`, from the per-user temporary folder and from a search of the
user's home directory; nothing anywhere in the repository names it. Whether the
system cleaned it out or it was never written, there is nothing to inspect and
therefore nothing whose origin could be established.

So this session **starts clean**, which is what it would have chosen anyway.
Re-using checkpoints is only safe if you can show which code wrote them, and a
half-finished set of five models out of ten could not have supplied the other
five in any case.

## Cost and limits

Laptop time only. No machine is rented, no vendor is contacted, nothing is
spent. The staged slice of rented time is **not** run and is not touched.

Nothing is fixed. Anything found is reported here and left alone.

*(Results section appended below when the run completes.)*
