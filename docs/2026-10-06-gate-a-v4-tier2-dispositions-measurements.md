# The end-to-end run of the final decision procedure, and two $0 checks behind the outside-review dispositions: what was found

*Written 2026-10-06 (Pacific) by the Claude Code session that wrote the
method, on branch `gate-a-v4-tier2-dispositions`. **The method was committed
and pushed first, at `da505d4`**
(`docs/2026-10-06-gate-a-v4-tier2-dispositions-measurements-method.md`);
nothing below was run before that commit. No model was loaded; nothing was
trained, rented or spent: $0. These are rehearsal records on the toy, not
results about the scientific question, and **they are owed a check by a
session that did not write them** (the pairing rule of
`docs/outside-review-protocol.md`).*

*Plain language throughout. MEASURED means a command was run and its output
is given here or in the committed file named; ARGUED means reasoning a
reader can dispute.*

> **Correction, 2026-10-06 (later the same day; the text below is left as
> committed at `025ce90`).** Part A's conclusion, that the decision
> procedure "does not exist as code", is **wrong**. Its commands ran on this
> branch, cut from `gate-a-v4-dispositions` before pull request 97 merged the
> frozen successor code into main (`53ae82c`, 2026-10-05); the command
> `ls -d experiments/08-successor-degree` was true of this branch and false
> of main. See "Correction to Part A" at the end of this file. Parts B and C
> are unaffected, except Part C's description of the gate code, corrected
> there too.

## Part A. The final decision procedure does not exist as one runnable thing, so A2 is not closed

**The commands, as the method pre-stated them, and what they returned
(MEASURED, run from the worktree root):**

| Command | Output | What it shows |
|---|---|---|
| `ls -d experiments/08-successor-degree` | `No such file or directory` | There is no registered-code folder yet |
| `grep -rln "metric validated\|degree not read\|substrate not a testbed" --include='*.py' experiments` | one file: the inside review's `rule_from_text.py` (a reviewer's script, not the procedure) | No code anywhere assigns a registered outcome term |
| `grep -n "def verdicts" -A 25 .../src/rerun_v3.py` | a per-seed function listing reasons (gate failed, no site set clears the floor, layer 0, read failed its floor, fresh floor missed, control 3) | Per-seed withholding exists in one older script, for **version 3's** rules (it still treats control 3 as a veto, which version 4 made a description, and does not include controls 1, 4 or 7 or the no-transplant check) |
| `grep -n "seeds_clearing\|learn_both" .../src/repairs.py` | lines 157 to 160: each gate condition counted across seeds separately, then `>= 2` on each | The gate code applies two-of-three **condition by condition**, the case the ChatGPT review's A10 table attacks |
| `grep -n "described_only\|inside_allowance\|bit_identical" .../src/rerun_controls.py` | the no-transplant check (line 177) and control 7 (line 210) are recorded as true-or-false fields; the only reading suppressed is the one marked `described_only` (arm F) | In the version 4 rehearsal code, a failed control or no-transplant miss is **printed beside** the reading, not withheld, as version 4 section 6.4, item 5, itself says |

**So, plainly: the procedure that takes per-seed records to one registered
outcome does not exist as code.** Its parts are spread over three scripts
written for different versions of the rules; nothing aggregates seeds into
arm verdicts under two-of-three for readings; nothing computes an outcome
term. Following the method's pre-stated rule, the end-to-end run and its
constructed cases (a) to (j) were **not** attempted, and no stitched-together
substitute was written. **A2 stays open.** What must be built, and the check
owed after it, are drafted in the dispositions file
(`docs/rulings/2026-10-04-successor-v4-gate-a-tier2-dispositions-PROPOSAL.md`,
under A2). Three of its rules wait on John (pages 7, 8 and 9 of the
addendum packet).

## Part B. The no-transplant check's assumption about errors (A9): the review's arithmetic holds

`python3 experiments/rehearsal-successor-measure/src/tier2_dispositions_check.py`,
output in `experiments/rehearsal-successor-measure/out-tier2-dispositions-check/check.json`
(MEASURED, from the committed controls re-run records):

| Arm / seed | Own-directed accuracy *p* | Untouched rate *U* | Formula (1 − p)/7 | Share of errors landing on the donor's answer, U/(1 − p) | Gap in the review's case |
|---|---|---|---|---|---|
| T / 0, 1, 2 | 1.00000 | 0.00000 | 0.00000 | no errors | 0 |
| C / 0, 1, 2 | 0.54875, 0.58125, 0.55250 | 0.05125, 0.04875, 0.06000 | 0.06446, 0.05982, 0.06393 | 0.1136, 0.1164, 0.1341 | 0.0860, 0.0798, 0.0852 |
| M / 0, 1, 2 | 0.87125, 0.88000, 0.87125 | 0.01250, 0.01750, 0.01375 | 0.01839, 0.01714, 0.01839 | 0.0971, 0.1458, 0.1068 | 0.0245, 0.0229, 0.0245 |
| F / 0, 1, 2 | 0.55875, 0.56625, 0.55625 | 0.05875, 0.05625, 0.06875 | 0.06304, 0.06196, 0.06339 | 0.1331, 0.1297, 0.1549 | 0.0840, 0.0826, 0.0845 |

- **The formula recomputes exactly** from *p* on all twelve records, so the
  review read version 4's formula correctly: it is `(1 − p) / 7`, which is
  right only if the errors spread evenly over the seven wrong value slots
  (an even spread puts 1/7, 0.1429, of errors on the donor's answer).
- **The review's arithmetic holds.** In its case (all errors on the other
  three agents' values) the untouched rate is `(1 − p) / 3`; at `p = 0.8`,
  0.0667 against 0.0286, a gap of 0.0381, over the 0.018 allowance. The gap
  exceeds 0.018 at **every accuracy below 0.9055**, so it is not a corner case.
- **On the toy every model errs roughly evenly**, with 0.097 to 0.155 of its
  errors on the donor's answer, near 1/7 and far from 1/3. That is why the
  toy passed the rule, and it is a fact about these toy models, not a
  property the registered models must share.
- **How well the rule does its job, on 800 pairs, by the exact binomial
  distribution:** it flags a **broken** pairing at the learn-both bar
  (`p = 0.2633`) only **0.5589** of the time; it withholds a **healthy** model
  whose errors spread evenly 0.0945 of the time at that bar, 0.0347 at
  `p = 0.56`, 0.0023 at `p = 0.8`; and it withholds a healthy model in the
  review's case **1.0000** of the time at `p = 0.56` and **0.9904** at `p = 0.8`.

So near the bar the rule is about a coin toss at catching what it is for,
and nearly certain to withhold a correctly paired model that confuses
owners. (ARGUED, from these figures.)

## Part C. Separate majorities against joint seeds (A10): the toy cannot tell them apart

Same command and output file (MEASURED, from `out-repairs/gate_base.json`,
`out-lesion-content-check/lesion_content_check.json` and
`out-controls-rerun/summary.json`):

| Arm | Per seed (P pass, F fail) | Separate majorities | Joint (two seeds pass everything) | Seeds that pass the gate and read |
|---|---|---|---|---|
| T | own P, P, P | pass | pass | 0, 1, 2 |
| C | own P, P, P | pass | pass | 0, 1, 2 |
| M | own P, P, P | pass | pass | 0, 1, 2 |
| F | own P, P, P; named-other P, F, F; collapse P, P, P; ownership-free line P, P, P | fail | fail | none |

No toy verdict changes under either rule, as expected: the toy has no split,
which is the review's point. The rule John picks is exercised only by the
constructed cases of Part A, which wait on the code.

## What this does not show

It does not close A2: nothing was run end to end. Part B does not show what
a registered-size model's errors will look like. Part C does not exercise
either rule. Nothing here was checked by another session yet.

## Correction to Part A, 2026-10-06

**What was wrong.** The search ran only on this branch. On main,
`experiments/08-successor-degree/src/` (frozen 2026-10-04, merged by pull
request 97) holds the procedure. Read from `origin/main` for this
correction:

| Command | Output |
|---|---|
| `git ls-tree -r --name-only origin/main experiments/08-successor-degree` | `src/` with `measure.py` and `procedure.py`, among others; `out-freeze-tests/` with test T3a's `summary.json` and `table.md` on the toy |
| `git show origin/main:.../src/measure.py > measure.py; python measure.py --self-test` (project Python, run from a scratch copy) | every check PASS, "all checks passed", among them withholding on control 7, 4 and 1 (arm T), the no-transplant rate, the fresh floor and the gate; two of three; the separation; outcomes R1, R2, R3, fifth, the fallback note, and arm M dropped |
| `git show origin/main:.../out-freeze-tests/t3a-committed-reads/summary.json` | gates T, C, M pass and F fails; every T, C and M seed reads; every F seed is withheld with three reasons; outcome `substrate not a testbed` (R3), reason "arm(s) F failed the gate" |

**What the frozen code does.**

- **Withholds per seed**, in the output file and the table, with every
  reason (`measure.withhold`).
- **Aggregates seeds partly jointly.** `procedure.gate` needs own-directed
  and, on arm F, named-other to pass on the same seed. Arm F's
  channel-removal collapse is counted separately, two of three on its own.
  The arm's gate verdict is then applied to every seed, so a seed that
  failed the gate itself can still be one of the two that read.
- **Assigns one of version 4's four terms** (`measure.outcome`). Any gate
  failure on T, C or F gives R3. If arm T returns no verdict while arm C
  reads, the result is R2. The two-model fallback gives R1 with a note.
  Arm M's band is computed and printed but changes nothing.
- **Has run end to end on the toy** (freeze test T3a, landing on R3) and on
  untrained 10-million and 30-million parameter models (test T6).

**What it does not do.**

- It has no ownership-free line (RT-237).
- It has no "metric not validated" term and no fallback terms (RT-241).
- No constructed failure case has been run through `summarise`: no split
  seeds, no overlapping failures on one seed, no arm M outside its band.
- The self-test's "the toy lands on the fifth term" case passes every gate.
  That is not the toy's real state.

**What this changes.** A2 is still not closed. That is no longer because
the procedure is missing. It is because:

1. its rules are about to change under the pending rulings (RT-237, RT-241,
   A9, A10 and page 9);
2. the constructed cases have not been run through the whole path;
3. another session has not checked it.

**Correction to Part C.** Its sentence that "the gate code applies two of
three condition by condition" is true of the rehearsal's `repairs.py` and
only partly true of the frozen code, as described above. Part C's
measurement, from the rehearsal's gate file, is unchanged.
