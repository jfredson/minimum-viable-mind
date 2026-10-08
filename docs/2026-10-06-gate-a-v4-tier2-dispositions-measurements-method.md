# The end-to-end run of the final decision procedure, and two $0 checks behind the outside-review dispositions: method, committed before any output

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree,
on branch `gate-a-v4-tier2-dispositions`, cut from `gate-a-v4-dispositions`
(the inside-review dispositions, pull requests 95 and 96) with the two filed
outside reviews merged in (the ChatGPT review, pull request 100; the Gemini
review, pull request 99). **Committed and pushed before anything described
here is run.** The commit that carries this file and its script carries no
output; the output, with the commands and what they printed, is a later
commit. Laptop only, on the processor. Nothing is trained, rented or spent:
$0. No model is loaded: every figure below is computed from records already
committed.*

*Written under the workspace plain-language rule. MEASURED means a command
was run and its output is in a committed file named beside it; ARGUED means
reasoning a reader can dispute. These are rehearsal records on the toy, made
to inform proposed dispositions. They are not results about the scientific
question, and no number here is a bar for anything until John rules it into
the registration text.*

**What this session opened before writing this.** Both outside reviews in
full; the inside-review dispositions and John's six-question packet in full;
`docs/outside-review-protocol.md` (the gates, the pairing rule, the
measurement rehearsal, the two tiers, the closure rule, filing); version 4
(`docs/successor-experiment-proposal-2026-10-03-v4.md`) sections 3, 6, 7.3
item 6, 9 and 13, and the spend tables of section 12; the rehearsal code
`rerun_v3.verdicts`, `rerun_controls.py` (its control 6 and table code),
`repairs.py` lines 150 to 165 (the gate stage); and the **field names** (not
the values) of `out-controls-rerun/measure_F_seed0.json`,
`out-controls-rerun/summary.json`, `out-repairs/gate_base.json` and
`out-lesion-content-check/lesion_content_check.json`. One file was read with
values: `out-controls-rerun/measure_F_seed0.json` (arm F seed 0), while
learning the field layout; its own-directed accuracy (0.55875) and
no-transplant rate (0.05875) were therefore seen before this note was
written. All other values the script prints are unseen by this session,
though most are quoted in version 4.

---

## Part A. The end-to-end run of the final decision procedure (for the fatal finding A2)

**The finding.** The ChatGPT review's A2: the procedure that turns per-seed
measurements into a reported outcome has never been run as one thing. Its
parts are: the controls that withhold a reading (control 7, the null
transplant; control 1 on arm T; control 4); the no-transplant check; the
whole-state floor applied again on fresh episodes; the fit floor on the
piece; the gates on learning and, for arm F, the channel-removal check; then
two-of-three across seeds; then the separation of arms T and C; then the
outcome term. The protocol's measurement rehearsal, item 5, asks for made-up
cases driven to every outcome. The review says this can close at $0, on the
saved toy measurements plus deliberately constructed failure cases.

**The run this would be, stated in full before any of it is attempted.**

1. **One procedure, one entry point.** A single function takes, for each arm
   (T, C, M, F) and each seed, the record of that seed (gate fields, lesion
   fields, the nominated site set and piece counts, the three accuracies,
   the no-transplant rate and formula, the fresh-episode floor, controls 1,
   4 and 7) and returns: for each seed, a reading or "no verdict" with every
   reason; for each arm, read or not read under two of three; the separation
   (lowest reading of arm C among seeds that read, minus highest of arm T);
   and exactly one registered outcome term with its reason. It writes the
   readings it keeps to a machine-readable file and to a table, and a
   withheld reading appears in **neither**, only its reason.
2. **On the saved toy records.** Input: the twelve arm-and-seed records of
   the controls re-run (`out-controls-rerun/`) and the gate and lesion files.
   Expected: the outcome version 4 section 3 states for the toy, or, if the
   order of rules John adopts makes arm F's gate failure decide first, R3;
   which of the two is the point of finding A10's precedence question, and
   the run reports which one the procedure returns under each order.
3. **On constructed failure cases**, each a copy of the toy records with
   named fields changed, each with its expected outcome written beside it
   before it runs:
   - (a) control 7 fails on arm C seed 0 only: that seed's reading vanishes
     from both outputs; arm C still reads on two seeds; outcome unchanged.
   - (b) control 7 fails on arm C seeds 0 and 1: arm C returns no verdict;
     the two-model fallback term.
   - (c) control 1 fails on arm T seed 2 and the no-transplant check fails
     on arm T seed 1: arm T returns no verdict; "metric not validated" (the
     proposed new term, inside-review dispositions, RT-241).
   - (d) overlapping failures on one seed (control 4 fails, the fresh floor
     is missed and the no-transplant check fails, all on arm C seed 1): one
     seed withheld with all three reasons listed, not three withheld seeds.
   - (e) split seeds, as in the ChatGPT review's A10 table, on arm F's
     gate: seed 0 passes own-directed, fails named-other, passes the
     channel-removal collapse; seed 1 passes, passes, fails; seed 2 fails,
     passes, passes. Under separate majorities arm F passes its gate; under
     the joint rule (a seed counts only if it passes every condition) it
     fails. Both results printed; the outcome under each.
   - (f) arm M reads on all seeds but outside 0.3 to 0.7 on two of them:
     the outcome term and the line said about arm M, under each of the
     rules put to John.
   - (g) arm M reads in band but more than 0.10 from its true-slot reading
     on one seed.
   - (h) arm C's readings drop so that arm C minus arm T is below 0.5: R2.
   - (i) arm F reads on one seed only: "metric validated, degree not read",
     with that seed printed as a description.
   - (j) a negative reading on arm T kept, not clipped.
4. **What it would show, and what it would not.** That the written rules,
   as code, return exactly one registered term on every case, withhold what
   they should in both outputs, and that every case's result matches the
   expectation written before it ran. Not that the rules are the right
   ones: that is John's.
5. **The check owed afterwards** (the closure rule gives it to a session
   other than the one that writes the fix): written out in the dispositions
   file under A2.

**The step before the run: does this procedure exist as code?** The run
above needs one runnable procedure. This session will establish, by the
commands below, whether it exists in the rehearsal
(`experiments/rehearsal-successor-measure/src/`) or in
`experiments/08-successor-degree/`, and print what each returns:

    ls -d experiments/08-successor-degree
    grep -rln "metric validated\|degree not read\|substrate not a testbed" --include='*.py' experiments
    grep -n "def verdicts" -A 25 experiments/rehearsal-successor-measure/src/rerun_v3.py
    grep -n "seeds_clearing\|learn_both" experiments/rehearsal-successor-measure/src/repairs.py
    grep -n "described_only\|inside_allowance\|bit_identical" experiments/rehearsal-successor-measure/src/rerun_controls.py

**Pre-stated rule for what happens next.** If one procedure exists that
takes per-seed records to an outcome term, it is run on the toy records and
on cases (a) to (j), with this note as its method. **If it does not, the run
is not attempted with pieces stitched together for the occasion**, because a
procedure written by this session to pass its own cases would be the fix's
author running the fix's check; and because three of its rules (the gate
precedence and joint seeds of A10, arm M's missed band, and whether the
no-transplant check withholds at all, A9) are not yet ruled, so any code
written today would have to guess them. The output then says plainly that
A2 is not closed, and the dispositions file drafts what must be built.

## Part B. The no-transplant check's assumption about errors, on the toy (for A9)

**The finding.** The ChatGPT review's A9: the no-transplant rule (version 4,
section 6.4, item 3) expects the untouched model to land on the donor's
answer at `(1 − p) / 7`, with `p` the arm's own-directed accuracy, and
withholds the reading if the measured rate is more than 0.018 away. That
expectation assumes the model's errors are spread evenly over the seven
wrong value slots. A model whose errors all go to the other three agents'
values lands on the donor's answer at `(1 − p) / 3`; at `p = 0.8` that is
0.0667 against 0.0286, a gap of 0.0381, and the rule would withhold a
correctly paired model.

**The quantities (pre-stated), for each of the twelve toy arm-and-seed
records** in `out-controls-rerun/measure_<arm>_seed<s>.json`, field
`primary`:

- `p` = `reading.arm_own_accuracy`; `U` = `no_transplant.rate`; the
  formula's value `no_transplant.formula`, recomputed as `(1 − p) / 7` and
  checked equal;
- **the share of the untouched model's errors that land on the donor's
  answer**, `U / (1 − p)`: 1/7 (0.1429) if errors are spread evenly over the
  seven wrong slots, 1/3 (0.3333) if they all go to the other three agents'
  values (the review's case). Where `1 − p` is small the share rests on few
  errors; the script prints the number of erring trials, `800 × (1 − p)`,
  beside it;
- at the record's own `p`, the gap the review's case would give,
  `(1 − p) / 3 − (1 − p) / 7`, and whether it exceeds 0.018.

**And the rule's power, by the exact binomial distribution on 800 fresh
pairs** (no models; arithmetic only):

- the chance the rule flags a **broken** pairing (the donor's answer
  unrelated, so the untouched model hits it one time in eight) at
  `p = 0.2633` (the learn-both bar) and `p = 0.56`;
- the chance it withholds a **healthy** model whose errors are spread evenly,
  at `p = 0.2633`, `0.56` and `0.8`;
- the chance it withholds a healthy model in the review's case (errors only
  on the other three agents), at `p = 0.56` and `0.8`.

**What this session expects, said now.** The formula's values recompute
exactly. On arms T and C, where `p` is near 1, there are few errors and the
share is not informative. On arm F seed 0 the share is about 0.133 (from the
values seen above), close to 1/7: the toy's free model errs roughly evenly,
which is why it passed. In the review's case the gap is `(1 − p) × (1/3 − 1/7)`,
which exceeds 0.018 at every `p` below about 0.905; so the review's case
withholds a correctly paired model at any accuracy a free model is likely
to reach. The rule flags a broken
pairing at the learn-both bar barely more often than not.

**What would count against the review's finding.** A share near 1/7 on every
toy model would not: it would show only that the toy's models err evenly,
not that a registered-size model must. A recomputed formula value that
differs from the committed one would show the review misread the formula.

## Part C. Separate majorities against one seed passing everything, on the toy gates (for A10)

**The question.** Version 4 and the code (`repairs.py`, the gate stage) apply
two-of-three to each gate condition separately. The ChatGPT review's A10
asks whether an arm needs two seeds that each pass every condition. Would
the joint rule change any toy verdict?

**The quantities (pre-stated).** From `out-repairs/gate_base.json`, `runs`,
for each arm and seed: `own_clears`, `other_clears`,
`lesion_collapses_own`. From
`out-lesion-content-check/lesion_content_check.json`, `models`:
`holds_own` (the proposed replacement for the battery clause, RT-237). The
conditions each arm is gated on: arms T, C and M, own-directed only; arm F,
own-directed, named-other, the collapse, and the proposed ownership-free
line. For each arm: the gate verdict under separate majorities and under
the joint rule; and from `out-controls-rerun/summary.json`, which seeds
returned a reading, so that the overlap between seeds that pass the gate
and seeds that read is printed.

**Expected.** No toy verdict changes: arms T, C and M pass own-directed on
every seed; arm F fails named-other on two seeds under either rule. So the
toy cannot tell the two rules apart, which is the review's point: the rule
has never been exercised on a split.

## The script

`experiments/rehearsal-successor-measure/src/tier2_dispositions_check.py`,
committed with this note. It loads no model and imports no project code; it
reads the four committed files above and writes
`experiments/rehearsal-successor-measure/out-tier2-dispositions-check/check.json`
and prints a report. Part A's commands are run by hand and their output
pasted into the findings file.
