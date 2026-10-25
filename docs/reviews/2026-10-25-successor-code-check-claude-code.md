# Check of the frozen successor code and the development runs' results (2026-10-25)

**Verdict: the code holds.** It does what the registered text (version 5) says. The outcome
rule is applied as registered, and the reruns' printed results follow from the code and the
saved models: re-measured on the laptop, they come out identical, value for value. Two small problems
were found in the spending alarm, and both are on paths the reruns never took. Two questions
need a ruling from John or a decision by whoever builds the next version of the built models.
Nothing found changes a result already on record, or the stop that experiment C (the
successor experiment) is at.

*This is the roadmap task "Check the frozen successor code and the development runs' results,
by a session that wrote neither" (`21a08412`), which John gave his go for on 2026-10-25. It is
filed under the pairing rule of `docs/outside-review-protocol.md` (whatever one session writes,
a different session checks). The checker is a Claude Code session that wrote none of the code,
none of the runs and none of their records, and did not read other sessions' conclusions about
the code before forming its own. It worked in its own worktree on branch
`claude/hungry-newton-85cd56`, cut from `main` at `dacc7b4`. Cost: $0. Everything ran on the
laptop's processor: forward passes and re-measurement of saved models, the self-tests, and
arithmetic on saved records. Nothing was trained, rented or sent to a paid model. Nothing under
check was edited. Written under the workspace plain-language rule.*

**What was checked against.** The registered text is
`docs/successor-experiment-proposal-2026-10-07-v5.md` (registered 2026-10-09; it names the code
in `experiments/08-successor-degree/src/` as at `6c47c56`). The freeze findings are
`docs/2026-10-04-successor-code-freeze.md`. The development runs' records are the run record
`docs/2026-10-09-reruns-10m-run-record.md`, `out-reruns-10m/` and `out-dev-10m-check/`, and
the saved models in `experiments/08-successor-degree/artifacts/` (these are not committed; they
are on the laptop only). The task notes name three things to look at first. They are findings
2 (the outcome rule), 3 (the toy scripts' port into `procedure.py`) and 9 (the spending alarm).

**Two kinds of development run.** The four 10-million-parameter development runs of
2026-10-04 (one per model) ran code from before the 2026-10-06 and 2026-10-08 changes, so
they cannot be re-measured on the registered code and give the same printout. They are checked
here only on what they are cited for: the sharpness figures (finding 7). The three reruns of
2026-10-09 (the three built models, retrained with the sharpness fixed) ran the registered code,
and those are re-measured in full (finding 8).

The scripts and outputs behind every figure here are in
`docs/reviews/2026-10-25-successor-code-check-claude-code-scripts/`.

## Findings

Each finding is marked **confirmed** (it holds as the record says), **problem** (something is
wrong, with a proposed fix), or **question** (something a person has to decide).

### 1. The registered code is the code in the folder — confirmed

`git diff 6c47c56 HEAD` over `experiments/08-successor-degree/src/` and
`requirements-measure.txt` is empty. The laptop's measuring environment has the pinned library
versions (torch 2.12.1, numpy 2.5.0, scikit-learn 1.9.0, scipy 1.18.0).

### 2. The outcome rule is applied as registered — confirmed

The first thing the task notes name is the freeze's section 4.1. It found that, applied as
written, version 4's rules put the toy on R3 ("substrate not a testbed"), not on the fifth term
that version 4's own section 3 claimed. Version 5 settles this in its section 3 ("The toy
outcome, on the anchors' terms"). There the toy's outcome depends on which free-model seed is
taken as the step 5a run: the fifth term if seed 0 is taken, R3 if seed 1 or seed 2 is. The code
was not bent to make the toy land anywhere.

I read `measure.outcome`, `measure.arm_outcome`, `measure.withhold`, `measure.seed_gate`,
`measure.separation`, `measure.arm_M_check` and `procedure.summarise` against version 5,
section 3, where its rules 1 to 3, the table, the seed rule and the scope phrases are set out.
The order of the rules is right. The gate on learning comes first: arm T or arm C failing its
gate gives R3, and so does arm F failing at step 5a. If arm F passed at step 5a and then fails
at step 5b, that is a no verdict on arm F with the reason "failed its gate on learning", and the
readings decide. Arm M never changes the outcome term. The separation is arm C's lowest reading
minus arm T's highest, and it must be at least 0.5. The built models' gate checks only the
own-directed condition. Every term that begins "instrument …" carries the scope phrase in the
same sentence.

I then wrote 15 cases of my own straight from section 3's table, without looking at the
earlier test cases in `tests/a2_cases.py`. They cover every term from R1 to the eighth, a
separation of exactly 0.5, arm F passing at step 5a and failing at 5b (with arm C reading, and
with arm C returning no verdict), arm M dropped, arm M inside its band, arm M missing its
band, and arm F reading on one seed only. A sixteenth case is an arm F seed whose
channel-removal check fails. **All sixteen land where the registered text says**
(`my_outcome_cases.py`, `my_outcome_cases.txt`).

### 3. The toy scripts' port into `procedure.py` is faithful — confirmed

This is the second thing the task notes name. I compared the parts of the procedure that decide
a reading with the rehearsal's code (`experiments/rehearsal-successor-measure/src/`):

- **Choosing the site** (`procedure.pick`) is the same as the rehearsal's `rerun_controls.pick`,
  line for line. It is also what version 5, section 7.2, items 3 to 5, registers: for each
  position set, the smallest layer set that clears the floor; then only sizes whose piece
  clears four fifths; then the highest ownership-only share, with ties going to the smaller
  size and then the earlier position set. A site set's fit is the fit of its worst layer.
- **The reading** (`measure.reading`) is the same as the rehearsal's `repairs.reading`,
  formula for formula.
- **The held-out counts** (`procedure.correct_count`, `accuracies`) are the rehearsal's,
  except for the two ruled changes: the 1,800 of 1,980 fitting split, and the iteration limit
  of 10,000 (rulings of 2026-10-08, item 7).

The test that the committed toy models load and give bit-identical outputs (test T2 of the
freeze method) was re-run and **passes, 12 of 12**. I did not re-run test T3a (about half an
hour), which reproduced 502 toy figures. On the registered code it would no longer match by
design, because the ruled fitting split changed. The earlier record of that reproduction, and
the page 4 re-run with the limit set back to 3,000, are what stand there.

### 4. Every self-test passes — confirmed

`src/run_self_tests.sh` passes, with 266 checks printed as passing across the seven files, in
1 minute 40 seconds (`selftests.txt`).

### 5. The reruns were trained on the registered recipe — confirmed

Read from the three saved models of 2026-10-09:

- **Training settings:** AdamW at a peak learning rate of 0.002, weight decay 0.01, the first
  tenth of the steps as warm-up, gradients clipped at 1.0, 96 episodes a step, and 108,919
  steps (585,548,544 tokens against the budget of 585,544,960). These are version 5's
  section 5.5, word for word.
- **Sharpness:** 4.000, held in a fixed stored value rather than a learned one, as section 5.6
  requires. (The sharpness is the number that sets how decisive the built "which agent am I"
  answer is.)
- **Training episodes skipped:** 0, because none matched an evaluation episode. This agrees
  with the earlier count over the whole stream (`out-check-training-exclusion/count_real_old_stream.txt`:
  0 of 5,228,112).

The models' SHA-256 checksums match `out-reruns-10m/checkpoints.sha256-md5.txt`.

### 6. The gate figures re-measure exactly — confirmed

On the laptop, the gate on learning gives own-directed and named-other answers of 2,959 and
2,980 of 3,000 for arm T, 3,000 and 3,000 for arm C, and 2,577 and 1,733 for arm M. These are
the committed figures.

### 7. The 2026-10-04 development runs' sharpness figures hold — confirmed

Read straight from the four saved models of 2026-10-04: arm T 1.947, arm C −0.089, arm M
−0.008, and arm F 4.000 (learned, but its route is never used). These are the figures version 5,
section 5.6, quotes.

### 8. The reruns' results follow from the code and the saved models — confirmed

I ran the registered procedure again on each of the three saved rerun models, using the run
record's own command (`procedure.py model --ckpt <model> --seed 0`). The three ran side by side
on the laptop's processor and took 1.7 to 2.0 hours each. Then I ran `procedure.py summarise`
on the output.

- **Every value in each row file is identical to the committed row**, compared field by field
  with timings and paths left out: 7,704 values for arm T, 7,860 for arm C and 7,521 for
  arm M, with 0 different (`compare_rows.py`, `compare_rows.txt`).
- **All 18 saved read arrays per model are identical**, bit for bit.
- **The summary table is identical** to `out-reruns-10m/table.md` (`table_diff.txt`).

So the printed results stand as they come out of the code. Arm T reads 0.0000 (the separable
model; the built route is in use, at 0.986). Arm C gets no verdict, because "construction did
not hold": its stirred-in route is used 0.000. Arm M gets no verdict for the same reason: route
use 0.024 on its stirred-in items and 0.000 on its separable items. Applied to these figures,
version 5's section 5.6 bar of 0.5 fails for arms C and M, which is the registered stop S4b.
The code reports exactly what the bar requires it to report.

### 9. The spending alarm met real billing on the reruns and behaved as written — confirmed

This is the third thing the task notes name: when the freeze was written, the alarm (the
spending tripwire) had met only recorded vendor readings. It has met real billing twice since
then. On 2026-10-04 it failed, as version 5's section 12.5 records. Its fixed version ran on the
reruns of 2026-10-09. I recomputed both comparisons from the alarm's own committed records
(`out-reruns-10m/tripwire-records/`):

- **The fast comparison (money drawn from the balance against what the posted rate
  predicts).** I recomputed it at all 25 readings with my own arithmetic. Once the prediction
  passed the rule's $0.25 floor, it ran from 0.62 to 1.009 and ended at 1.006. No reading was
  over the line under either in-flight rule as amended on 2026-10-06 (rule S: two readings in a
  row over 1.25 × prediction + $0.05; rule D: one reading over 1.25 × prediction + $0.02, at
  least 15 minutes after a deletion). The early readings of 9.0, 4.9 and 4.1 came before the
  floor, when a cent of drawdown dominated, and the rules correctly ignore them.
- **The authoritative comparison (billed hours against how long each machine existed).** This
  is 1.000 on each machine from the recorded lifetimes: 0.3367, 0.3345 and 0.4239 hours billed,
  against 0.3367, 0.3344 and 0.4237 hours existed.
- **Deletion times:** each deletion was recorded as it happened, not inferred afterwards.

Spending was normal, and this time the alarm could say so.

### 10. If a machine's creation record gives no rate, the alarm uses the typed rate instead of stopping — problem

`launch_successor.sh` (lines 401 to 410) registers the machine with the alarm at the hourly
rate its creation record gives. When the record gives none, it falls back to the
`RATE_PER_HOUR_USD` the operator typed. Version 5's section 12.5 says the rate is "read from the
machine's creation record, not remembered". Section 12.7 says a check that cannot be run counts
as a trip. A missing rate is a check that cannot be run. This did not happen on the reruns,
where all three records stated $1.19. **Proposed fix (not made here; the code is frozen):** if
the creation record gives no rate, write the halt file and delete the machine, as for any other
check that cannot be run.

### 11. The decision on a machine already running checks only half of the registered rule — problem

Version 5's section 12.5, item 2, says a machine already running when the alarm trips is left
to finish only if both of these hold:

- its projected total stays inside its estimate times the measured ratio, **and**
- the funded balance covers it.

`tripwire.in_flight_decision` checks only the second. It also projects the remaining cost from
the estimate, so a machine already past its estimated hours projects $0 remaining and is
always left to finish. This matters little in practice, because the separate machine deadline
(hard cap ÷ rate) still deletes it. But the code does not do what the text says. **Proposed
fix:** project from the time actually used, and delete when the projected total is above
estimate × ratio.

### 12. A price rise at the vendor reaches John only through the hard cap — question for John

The go for the reruns was "about $1.14", worked out at the $0.99 an hour on record. The vendor
charged $1.19, as each machine's creation record stated, and the wave cost $1.3032. That is
1.14 times the approved figure. This is not a fault in the code. The alarm is built to compare
against the posted rate, so a price change is invisible to it. The launcher shortens the
machine deadline when the posted rate is higher (lines 429 to 442), so the hard cap still bounds
the spend. But nothing stops a launch when the posted rate is above the rate John approved.
Under "every spend needs John's go", the question is: **should the launcher refuse to start a
machine whose posted rate is more than some margin (for example 10 per cent) above the rate
named in the go, so that a price change comes back to John before money is spent?** It costs
nothing to add, and it would be a change to frozen code, so it needs his ruling.

### 13. Fixing the sharpness closed one way for the built route to go unused, not the only one — question for whoever designs the next built models

This bears on option (d), the route version 5's section 5.6 names for real reference models
now that experiment C has stopped. In the reruns the sharpness stayed at 4.0, but arm C's
stirred-in route still went unused (route use 0.000). The saved models suggest how. The
projection that turns each agent's marker word into the built answer (`own_marker`) makes the
markers nearly alike in arms C and M, and very different in arm T. Measured as the average
distance of a marker's projection from the mean projection, across the 20 marker words, it is
0.84 in arm C, 0.46 in arm M and 9.51 in arm T (`marker_spread.txt`). The stirred-in weights
themselves are large, not zero.

So arms C and M seem to have made the built answer carry little information about who is
acting, and to have taken it from the acting signal in the trunk instead. This is
**ARGUED from weights, not tested by intervention**, and I did not check it against the
separate investigation of arm M's separable half (`docs/reviews/2026-10-18-arm-m-separable-zero-check-claude-code.md`).
If it holds, any redesign has to close this route too: for example, by removing the acting
signal from the trunk of the stirred-in model, as option (d) already suggests, or by fixing
the marker projection. Retuning the sharpness alone would not be enough.

### 14. A misnamed step 5a seed would be reported as R3 — question (small)

`procedure.summarise` reads the seed of arm F's step 5a run from `steps.json`. If that file
names a seed that has no row, the summary reports R3 with "condition not recorded". That is in
the spirit of section 12.7, but it would report a bookkeeping slip as a scientific outcome.
**Suggestion:** if the seed named has no row, refuse to summarise and say why.

## What was not done, and what would cost money

- **Not re-run, laptop time only (no money):** test T3a, the 502-figure toy reproduction,
  about half an hour (see finding 3 for why it would not match on the registered code); test T6,
  the full run of the pipeline at 30 million parameters, which takes hours; the eleven re-reads
  of the toy models retrained with the sharpness fixed, which version 5 lists as owed; and a
  re-measurement of the four 2026-10-04 development runs on the code of that date.
- **Nothing in this check needed rented machines or a paid model.** Testing the fixes proposed
  in findings 10 and 11 against the real vendor would need a rented wave. The smallest
  development-size run cost about $0.40 to $0.50 a machine on 2026-10-09 at $1.19 an hour. No
  such wave is proposed here.

## For the record

- Findings 10, 11 and 14 are proposed fixes to frozen code. The code is not changed by this
  check. Experiment C is stopped at its registered stop S4b, so none of them blocks anything
  now, and they belong with any new version of the built models.
- Finding 12 is for John to rule on.
- Finding 13 is for whoever writes option (d).
