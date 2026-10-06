# Method: bringing the successor's decision code to the 2026-10-06 rulings, and running it on made-up failure cases (outside finding A2)

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree,
on branch `a2-decision-procedure`, cut from `origin/main` at `53ae82c`.
**Committed before any changed code has run and before any case output
exists.** Every expected outcome below was written from the ruling text, not
from the code. A case that lands elsewhere is a finding and is reported as
one; the expectation is not edited afterwards. Laptop only, no model trained
or loaded, nothing rented: $0.*

*Plain language. "Arm" is one of the four model designs (T: the separable
model built to be easy to read; C: the entangled model, the high anchor; M:
the middle model; F: the free model whose degree the experiment exists to
read). A "seed" is one of an arm's three training runs. "Withheld" means the
reading is replaced by "no verdict" with its reasons, and the figure itself is
not written anywhere.*

## What this answers

The fatal outside finding A2 (the ChatGPT review of version 4): the procedure
that turns per-seed records into one registered outcome must follow the
rulings and be run end to end on made-up failure cases before registration.
The rules are John's rulings of 2026-10-06
(`docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`, with its same-day
addendum, pull request 103, branch `rulings-2026-10-06-gate-a-v4`) and the
drafted texts they adopt: the A2 list of what must be added to `procedure.py`
and `measure.py` (outside dispositions, lines 247 to 281), the outcome table
(inside dispositions, RT-241, lines 441 to 493, as changed by A10, lines 592
to 665), the seed rule (A10, lines 592 to 639), the no-transplant change (A9,
lines 515 to 552), and the ownership-free line (RT-237, lines 140 to 196).

## The changes to the frozen code (`experiments/08-successor-degree/src/`)

1. **The outcome table** (`measure.outcome`), applied in this order:
   1. If arm F's step 5a run failed its learning gate (after its re-run),
      the outcome is **R3, "substrate not a testbed"**, and nothing else is
      needed: stop S4, unchanged.
   2. If arm T or arm C fails its learning gate, **R3**, naming the arm,
      whatever else happened. If arm F fails its learning gate and there is
      no record that it passed at step 5a, **R3** (see reading 2 below).
      Arm M failing its gate drops arm M and changes no term.
   3. Arm T no verdict: **"metric not validated"**, reason after a colon.
   4. Arm C no verdict (the two-model fallback): arm F reads gives **"metric
      checked against the separable model only, degree read"**; otherwise
      **"metric checked against the separable model only, degree not
      read"**, reason after a colon.
   5. Arms T and C both read: if they do not separate (arm C's lowest
      reading minus arm T's highest under 0.5), **R2, "metric does not
      separate"**. If they separate: arm F reads gives **R1, "metric
      validated, degree read"**; arm F no verdict, failing its
      channel-removal check, or (having passed at step 5a) failing its
      learning gate at step 5b gives the fifth term, **"metric validated,
      degree not read"**, with the reason after a colon. A step 5b gate
      failure's reason is exactly "failed its gate on learning".
   6. Arm M reading outside 0.3 to 0.7 on any seed that reads, or more than
      0.10 from its true-slot reading, changes no term; the outcome sentence
      says "arm M missed its predicted reading" with the figures, and that
      arm F's figure is placed against arms T and C only.
   7. The outcome sentence carries the scope phrases of page 11 and the
      addendum: "on these constructed systems, for this intervention
      procedure" after every term containing "metric validated" and after
      the three new terms; "as a ratio of two transplants at the sites this
      procedure chose" after "degree read". The bare registered term is kept
      in its own field so it can be matched exactly.
2. **The seed rule (page 7), in one place** (`procedure.summarise` with
   `measure.withhold`): each seed is judged on its own gate, not the arm's.
   A seed counts only if it passes every condition of its arm's learning
   gate (own-directed; on arm F also named-other), on arm F the
   channel-removal check (the collapse below the gate bar and the
   ownership-free line), and every check that withholds a reading, and
   returns a reading. An arm passes its learning gate if two seeds each pass
   every learning condition; an arm reads if two seeds count. The separate
   two-of-three count for the collapse is removed.
3. **The ownership-free line (page 1)**: `procedure.gate` writes, for every
   arm and seed, the lesioned own-directed count and the **lesioned candidate
   count** (with the acting channel zeroed, own-directed answers that are the
   successor of one of the four agents' earlier values on the item named),
   and the line, **1,546 of 3,000**, computed from the exact binomial tail
   (above one half at the 0.05 level, one-sided), not typed. The arm F
   channel-removal check requires it per seed.
4. **The no-transplant check (page 8)** no longer withholds. Its rate, the
   formula's value, their difference, the share of errors on the donor's
   answer, and the chance the formula would flag a broken pairing on 800
   pairs at the learning bar (about 0.56) are reported. Control 4 stays the
   pairing check that withholds.
5. **Every reason listed; nothing withheld left in the output** (A2 item 7):
   `withhold` evaluates every check whether or not a reading was computed
   and lists every one that did not pass. A check that never ran (its field
   is absent) is listed as "not run", not as "failed"; under stop S8 it
   still counts against the seed (it withholds, or fails the gate). A check
   whose field is present but empty is listed as "could not be evaluated",
   and also counts against. `arithmetic_withheld` is removed from
   `summary.json`, and the table prints nothing computed from a withheld
   seed's reading in the reading column.
6. **The freeze's self-tests updated**: the "toy lands on the fifth term"
   test now uses the toy's real gate pattern, and the new rules each get a
   unit test.
7. **The generator self-test on unseen combinations (RT-255, adopted by John
   later on 2026-10-06, recorded on the rulings branch at `abb7e0a`)**: one
   check added to `grammar.py --self-test`, asserting that no fresh or
   relaxed episode's combination occurs in the training stream: the default
   training stream's exclusion list holds every fresh and relaxed content, and
   over the sampled training steps none of their contents appears. "Combination"
   is read as the episode's whole content (every random draw except which
   agent the model is), which is what the generator's fingerprint covers.

## Readings of the ruling text this code had to make

1. **"Not run" versus "failed".** Item 7 asks for every withholding reason;
   the coordinator's brief asks that a never-run check be listed as not run.
   Stop S8 (version 4) says a check that cannot be evaluated counts as
   failed and its consequence fires. Both are honoured: the label says "not
   run", the consequence is the same as failing.
2. **Step 5a in the records.** The ruling makes arm F's gate failure R3 at
   step 5a and the fifth term at step 5b. The records do not say which seed
   was the step 5a run, so the procedure reads a small step record,
   `steps.json`, beside the rows (`{"arm_F_step_5a_seed": s}`). Where none
   exists (the toy) and arm F fails its learning gate, the outcome is **R3**,
   because nothing shows arm F passed at step 5a, and the fifth-term
   exception exists only for a free model that did. The toy is run three
   ways: no record, seed 0 as step 5a, and seed 1 as step 5a, as the ruling's
   toy sentence asks.
3. **Which conditions are "the gate" for R3.** R3 follows the learning gate
   (section 8.1). The channel-removal check (section 8.2: collapse and the
   ownership-free line) is a seed condition (page 7) and its failure leaves
   arm F with no verdict, which the table maps to the fifth term or the
   fallback's "degree not read", not to R3.
4. **The scope phrase on R2.** "Metric does not separate" is neither "metric
   validated" nor one of the three new terms, so it carries no scope phrase.
5. **R4** is a schedule outcome (a missed date), not a result of the
   records; the procedure cannot reach it and no case tries to.

## The made-up failure cases, and the outcome each must land on

Each case is the toy's committed records
(`experiments/08-successor-degree/out-freeze-tests/t3a-committed-reads/row_*.json`,
confirmed by SHA-256 before use) with the named fields changed. The exact
changes and expectations are code in
`experiments/08-successor-degree/tests/a2_cases.py`, **committed with this
note**. Where a case needs arm F to read, it is given passing learning counts,
nomination, floors and controls, and the ownership-free counts from the
committed rehearsal check (2,100, 2,238 and 2,324 of 3,000 on arm F;
`experiments/rehearsal-successor-measure/out-lesion-content-check/lesion_content_check.json`
on the rulings branch). "Step 5a" names the step record.

| # | Case | What is changed | Expected outcome (written before running) |
|---|---|---|---|
| 1 | **The toy as it actually is** | nothing; no step record; no ownership-free field | **R3**, naming arm F; arm F's seeds list "the ownership-free line was not run", seeds 1 and 2 also "failed its gate on learning"; arm M's prediction met |
| 2 | Toy, seed 0 as step 5a | step record only | **fifth term**: "metric validated, degree not read: failed its gate on learning" |
| 3 | Toy, seed 1 as step 5a | step record only | **R3**, arm F at step 5a |
| 4 | Every arm reads | arm F made to read (0.62, 0.66, 0.71) | **R1**, sentence with both scope phrases |
| 5 | Anchors do not separate | as 4, arm C read 0.40, 0.45, 0.50 | **R2** |
| 6 | Arm C no verdict, F reads | as 4, control 7 fails on C seeds 0 and 1 | **"metric checked against the separable model only, degree read"** |
| 7 | Arm C no verdict, F not read | arm F learns but fails nomination on every seed; control 7 fails on C seeds 0 and 1 | **"metric checked against the separable model only, degree not read"**, reason naming the piece floor |
| 8 | **Arm T no verdict** | as 4, control 1 fails on T seeds 0 and 1 | **"metric not validated"**, reason naming control 1 |
| 9 | Arm T and arm C both no verdict | 8 and 6 together | **"metric not validated"** |
| 10 | **Split seeds: the review's A10 table** on arm F | seed 0 fails named-other; seed 1 fails the collapse; seed 2 fails own-directed and the piece; step 5a on seed 1 | **fifth term: failed its gate on learning** |
| 11 | Split seeds, learning passes | every F seed learns; seed 0 fails nomination, seed 1 the collapse, seed 2 the ownership-free line (1,500) | **fifth term**, reasons naming all three (the frozen code would give R1) |
| 12 | Split seeds, exactly one seed passes everything | seed 1 fails named-other, seed 2 fails the collapse | **fifth term** (the frozen code would give R1) |
| 13 | **Overlapping failures on one seed** | T seed 2: no site set clears, development floor missed, controls 7 and 4 fail | **R1**; all four reasons listed on T seed 2 |
| 14 | **Arm M outside its band** | as 4, M read 0.80, 0.85, 0.90 | **R1**, sentence says arm M missed its predicted reading, F placed against T and C only |
| 15 | Arm M fails its gate | as 4, M own-directed 700 on seeds 0 and 1 | **R1**, arm M dropped and said so |
| 16 | **A withheld seed** | as 4, F seed 2 computes 0.123456 but control 4 fails | **R1**; 0.123456 (and 0.1235) appears in neither `summary.json` nor `table.md` |
| 17 | **A never-run check** | as 4, the ownership-free field removed from every F seed | **fifth term**, reason "the ownership-free line was not run" |
| 18 | A never-run control | as 4, control 4 absent on C seeds 0 and 1 | **"metric checked against the separable model only, degree read"**; C seeds list control 4 as not run |
| 19 | No-transplant rate far off | as 4, T's rate 0.05 off the formula on every seed | **R1** (page 8: reported, not a veto) |
| 20 | Arm F fails its channel removal | as 4, no collapse on F seeds 0 and 1 | **fifth term**, reason naming the collapse |
| 21 | Arm T fails its gate | as 4, T own-directed 700 on seeds 0 and 1; C no verdict too | **R3**, naming arm T |
| 22 | Arm F fails at step 5a | only arm F's records; step 5a on seed 1 (fails named-other) | **R3**, arm F at step 5a |

Every term the procedure can reach is covered: R1 (4), R2 (5), R3 (1, 3, 21,
22), the fifth term (2, 10, 11, 12, 17, 20), both fallback terms (6, 7, 18),
"metric not validated" (8, 9).

## How it runs, and what is recorded

`experiments/08-successor-degree/tests/a2_run_cases.py` (written after this
note) checks the SHA-256 of the toy rows, builds each case directory under
`experiments/08-successor-degree/out-a2-cases/`, runs `procedure.summarise` on
it, and writes `results.json` and `results.md`: per case the expected and
actual outcome code, the term and sentence, whether each expected text piece
was found, and a search of both output files for every withheld seed's
figure (full precision and four places) and for the field name
`arithmetic_withheld`. Then `run_self_tests.sh` is run. Light on the laptop:
no model is loaded.

## What is owed afterwards (not done here)

The independent check listed under A2 (outside dispositions, lines 303 to
323), by a session that wrote neither the code nor this run: recompute every
outcome with independent code from the ruling text; show withheld readings
appear nowhere; turn each veto off in turn and see an outcome change; every
registered term reached and no unregistered one; inputs confirmed by SHA-256.
