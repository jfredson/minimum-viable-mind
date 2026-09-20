| A3 hard stop | $34.31 | **$65.69** |

Three retrained seeds cost **$27 to $39** at measured rates. That fits
inside both, comfortably. Money is not the binding constraint on this
decision, and I should not have implied it was.

## Candidates

**A. Close A3 with partial discriminators.** Report the primary result,
the instrument audit, and the undefined comparison. *Cost $0.* Honest, and
weaker than it sounds: the discriminators that do not need the control are
the matched other-agent lesion, the random matched subspaces and the swap
probe — all of which run through a localization stack that has so far
found nothing, with probes below their own nulls and an ablation that
improved the battery it was meant to damage.

**B. Eval-side A4: divide by chance instead of the ceiling.** *Cost $0.*
At chance all three checkpoints would clear the floor and the comparison
would become computable. **Reject.** The ceiling denominator was itself a
registered revision made because dividing by chance manufactured a
spurious differential. Changing it back after seeing that it blocks the
result is fitting the rule to the data, which is the thing this programme
exists to not do. It would be the third time in two days that a rule of
mine was found wanting by the data, and the first two were reported rather
than repaired for exactly this reason.

**C. Retrain with the control properly supervised.** *Cost $27–39, three
seeds.* One change: give the control its own loss term or oversample it,
instead of a third of a shared one. No grammar change, so the frozen
batteries, the cue gates and the attack sweep are all unaffected.

**D. Retrain with a scaffolded intermediate query.** *Cost $27–39 plus
re-freezing batteries.* Teach plain name-keyed retrieval before layering
the rule on top.

**E. Train longer or bigger.** **Fenced by the registration**, which says
the finding is "unlearnable at this scale under this curriculum" and never
a silent scale bump.

## Recommendation

> **ANNOTATION, 2026-09-17, later the same day. The candidates below are
> MOOTED and the recommendation is superseded, though its one operative
> instruction was right.**
>
> The ceiling measurement John made a precondition has now run. The
> control battery's ownership-blind ceiling is **1.0**, reached by two
> independent solvers, with both known-answer checks reproducing their
> registered values exactly first.
>
> A defined drop needs a baseline of 1.10, so **the control's drop is
> undefined for every possible model** and the registered differential
> clause was never computable, at any budget, on any architecture. It has
> been unsatisfiable since registration.
>
> **So options C and D below are moot.** Both aimed at making the control
> learn, and a perfectly learning control would change nothing. I was
> proposing to spend $27 to $39 repairing the wrong component. What caught
> it was John's instruction to measure the ceiling before opening an
> amendment, and the recommendation below to run the free thing first.
>
> The October question is no longer whether to make the control learn. It
> is whether the clause can be repaired at all, and whether that repair is
> a metric change rather than a training change. See
> `ceiling-measurement-findings.md`.

**Do the free diagnostic first, then decide between A and C. Do not spend
yet.**

The audit produced a hypothesis with a sharp, free test. The control fails
for one of three reasons: the model cannot do name-keyed retrieval at all,
it can retrieve but not apply the successor rule, or the reversed
rendering defeats the retrieval specifically. **These are distinguishable
on the checkpoints already in hand, locally and for nothing**, by asking
the trained models plain lookup questions without the rule step and
comparing against the control's own score.

That matters because option C is a bet that supervision is the binding
constraint. If the diagnostic shows the models cannot retrieve by name at
all, more supervision on the same rendering is likely to buy little and
option D becomes the honest candidate. If they retrieve well and fail only
at the rule step, C is well targeted and cheap.

**Whichever way the decision goes, register the ceiling defect.** The
control's 0.3227 was never attack-verified, is set by a solver blind to
the name the question supplies, and disagrees with the module's own stated
0.5. That is a defect in the registered instrument, independent of whether
A3 continues, and it belongs on the record either way. If A3 closes, it
belongs in the write-up as a limitation of the comparison that was never
available. If A4 opens, the ceiling must be measured properly first,
because an amendment built on an unverified denominator would inherit the
same problem.

**What I am not recommending.** I am not recommending the eval-side change
that would make the numbers work. It is available, it is free, and it is
the wrong thing to do.

## What this decision does not settle

Where ownership lives. Every result here comes from removing an input
channel, which shows the action depends on ownership without showing the
network built an internal structure carrying it. The localization work
that was meant to answer that is unvalidated at this scale, and no
control-battery decision changes it.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-control-learnability-packet.md =====

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


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-control-learnability-claude-worktree.md =====

# Findings — the control-learnability pilot (Gate B, tier 1)

*Filed 2026-09-20 under the outside-review protocol, against the review
packet for the control-learnability pilot
(`reviews/2026-09-20-control-learnability-packet.md`). Verbatim once
filed. Rulings are John's and go in the red-team ledger
(`red_team_ledger.md`); nothing here is a ruling.*

## What was opened, and nothing else

Everything below was read at the commit the packet names — the ledger
commit that closed both spend rows (`a569a35`). I first checked that none
of the listed files changed between that commit and the current tip of the
main branch; none did, so the working copies are the right versions.

Opened, all inside `experiments/06-mvm-0a-constructed-self-index/`:

- the pre-statement (`control-learnability-pilot.md`)
- the findings under review (`control-learnability-pilot-findings.md`)
- the full-budget endpoint record (`a3-gates/endpoint_a3ctl_30m_seed0.json`)
- the partial-checkpoint endpoint record
  (`a3-gates/endpoint_a3ctl_30m_seed0_PARTIAL_step51500.json`)
- the trainer (`src/train_a3.py`) and the pilot launcher
  (`src/launch_ctl_pilot.sh`)
- the compute ledger (`compute-ledger.md`), the two rows dated 2026-09-19
  (the pilot) and 2026-09-20 (the checkpoint recovery)
- the two comparison write-ups (`gate2-pilot-findings.md` and
  `seeds-endpoint-findings.md`)
- the registered text the interpretation is read against: Amendment A3
  (`amendment-a3.md`) — the battery table in §2.5, the lesion protocol in
  §3.1 and §3.2, the pre-stated signatures in §3.5, and registration
  revisions 3 and 4, which carry the metric and the ceilings — and the
  registered ceiling defect (`ceiling-defect-2026-09-17.md`)
- the red-team ledger, to read its last entry number only, so this file
  continues the numbering correctly

**The training log and the trajectory record were not opened, because they
are not in the repository.** The findings file never says where they are,
which is the first thing to record. They do exist on the laptop, in the
run's artifacts folder alongside the checkpoint; I established that by
listing the folder and reading no file in it, because the packet forbids
opening uncommitted files and everything under `artifacts/` is excluded
from the repository by `.gitignore`. See finding RT-56.

**Not opened, as instructed:** the current-state document (`STATUS.md`),
the `docs/` folder, anything to do with the A4 clause, any chat
transcript, any uncommitted file. Two modules I wanted and did not take
because the packet does not list them: the episode generator
(`curriculum_a3.py`) and the encoder (`encoding_a3.py`). Two findings
below (RT-58 and RT-59) are limited by exactly that, and say so.

**Lookup: none.** No web search, no external source. Every number here is
computed from the files listed above, and every computation is shown.

**Severity across this review: eighteen findings — one fatal, ten
serious, five worth-noting, and two checks that came back clean and are
recorded as clean.** Numbering continues from the ledger's last entry
(`RT-51`), so this file runs from `RT-52` to `RT-69`.

---

## 1. Feasibility

*For every quantity the pre-statement names: is the boundary the right
number, is the higher boundary reachable at all, and did the intervention
deliver the supervision it claims.*

| id | finding | label | severity |
|---|---|---|---|
| RT-52 | 0.3227 is not a ceiling, and the registered text naming it is already recorded as defective — but it is still the right number for the cell it was used in | MEASURED | serious |
| RT-53 | The endpoint record states a floor rule the programme corrected three days before the run | MEASURED | serious |
| RT-54 | The 0.60 boundary is reachable in principle; the battery's real limit is near 1.0 | MEASURED | worth-noting |
| RT-55 | The supervision was delivered, exactly as claimed — the findings file cites nothing for it, and the endpoint record does not carry the run's settings | MEASURED | serious |
| RT-56 | The training log and the trajectory record are not in the repository, though the previous run's equivalent is | MEASURED | serious |

### RT-52 — the boundary is the right number wearing the wrong label

**MEASURED. Serious.**

The pre-statement, the findings file and the endpoint record all call
0.3227 the control battery's "ownership-blind ceiling". The programme's
own registered defect of 2026-09-17 says that is false, and says so in
the registered text itself: the attack sweep that Amendment A3 credits
with verifying both ceilings contains no control-battery code at all, so
the claim "verified by the attack sweep" covers the primary battery only.
The 0.3227 comes from one reference solver that never reads the marker
the control question supplies. The question names an agent; the solver
enumerates all four agents' successors on the item, strikes the ones
already visible as revisions, and guesses among the rest.

So 0.3227 is the score of a solver that cannot read names, and the
battery's real ownership-blind ceiling is near 1.0 and unmeasured.

**And yet the number is fit for the cell that used it.** "The control did
not learn name-keyed lookup" means precisely "it scores no better than a
solver that cannot read the name", and 0.3227 is that solver's score. The
pre-statement's own gloss is correct — "a battery at or below it has not
learned the task, whatever else is true." Nothing about the verdict turns
on the mislabel.

What does turn on it: a Gate B interpretation rests on a boundary the
programme formally registered as defective three days before the run, and
**the findings file never mentions the defect.** Anyone reading the
findings alone would take 0.3227 for a checked quantity. It is not one,
and John has already ruled that measuring this ceiling properly is a
precondition of any Amendment A4.

**Fix:** the findings file should cite the ceiling defect
(`ceiling-defect-2026-09-17.md`) and call 0.3227 what it is — the score
of a name-blind reference solver — everywhere it appears.

### RT-53 — the endpoint record carries a superseded rule

**MEASURED. Serious.**

The full-budget endpoint record describes the metric this way:

> floor rule leaves a battery undefined when its baseline is below its own
> ownership-blind ceiling

That is the rule as it was stated before 2026-09-17. The correction of
that date, recorded in the three-seed write-up
(`seeds-endpoint-findings.md`), says the floor rule is not "baseline
below ceiling" but **baseline minus ceiling below 0.10** — so the control
needs **0.4227**, not 0.3227, for its drop to be a defined quantity at
all.

No number moves: the control reads 0.3125, which is below both. But the
artifact that carries the reading encodes a rule the programme corrected
before the run was launched, and the same superseded sentence sits in the
partial-checkpoint record too. The consequence is not arithmetic, it is
that 0.4227 — the number that actually decides whether this battery is any
use to Amendment A3 — appears nowhere in the pilot's pre-statement,
findings or endpoint records. That omission does real work in part 4
below.

### RT-54 — the higher boundary is reachable, on an argument nobody has attacked

**MEASURED. Worth-noting.**

Checked and clear. Amendment A3's battery table puts chance on this
battery at 0.125 — a forced choice among eight. The ceiling defect
establishes that every turn renders the speaker's marker in plain text,
so a solver doing ordinary name-keyed lookup "answers correctly every
time". The battery's attainable score is therefore about 1.0, and the
0.60 boundary sits comfortably inside it. **The LEARNED cell was not set
at an unreachable number.**

The caveat is that "near 1.0" is analytic and explicitly unmeasured — the
defect memo says so in as many words — and the attack sweep has still
never been pointed at this battery. So "reachable in principle" rests on
an argument that has not been adversarially tested, which is the same
weakness RT-52 records at the other end of the scale.

### RT-55 — the supervision was delivered; the findings file cites nothing for it

**MEASURED. Serious, and explicitly not fatal — I found the record.**

The findings file's load-bearing claim is that "its per-row gradient
weight quadrupled and its share of the query gradient went from about a
third to about two thirds." It carries no citation whatsoever. The
packet's rule is that a measured claim with no record behind it is fatal
on its own. **It is not fatal here, because the record exists and I found
it — in the compute ledger's pilot row, dated 2026-09-19. But the findings
file does not point at it, and the endpoint record does not carry the
run's settings either.**

The claim itself is exactly right. I checked it two ways.

**From the code.** With the flag off, the query loss is the total loss on
the answer tokens divided by their count, so each of the 128 rows carries
one one-hundred-and-twenty-eighth of the term, and the round-robin gives
the control battery about one row in three — a share of about a third.
With the flag on at the settings used, half the batch (64 rows) carries
the control question, the control's own term is the average over those 64
rows, and that term is multiplied by 2. So each control row carries two
sixty-fourths, which is one thirty-second: **exactly four times**
one-one-hundred-and-twenty-eighth. By the same arithmetic the control's
total weight is 2.0 against the other batteries' 1.0, so its share of the
query gradient is **exactly two thirds**, up from a third. Both figures in
the findings are right to the digit.

**From the run.** The ledger records the query loss at step 500 as 3.433
for this run against 1.075 for the matched earlier pilot, and notes that
"other-term + 2 × control-term" predicts about 1.1 + 2 × 1.15 = 3.40.
That is direct evidence the split fired on the rented machine and fired at
the right scale, not merely that the flag was typed. The ledger also
quotes John's go verbatim with the two settings in it, records that the
trainer's self-test ran on the pod before any training step, and records
the measured pace at 0.6508 seconds per step against the earlier pilot's
0.6501 — so the flag cost nothing and the run was not short-changed.

**Fix, and it is cheap.** The trainer already saves the run's full
settings into the checkpoint. The endpoint record should echo the two that
matter — the control weight and the control fraction — so the artifact
that carries the reading is self-contained. As it stands, the only thing
tying that record to a run with the flag on is the output name.

### RT-56 — the log and the trajectory are not in the repository

**MEASURED. Serious.**

The packet asked for "the training log and trajectory record for the run,
wherever the findings file says they are." The findings file does not say.
Its only reference to the log is a claim sourced to it — "the trainer's
own log records both acts on consecutive lines" — with no path.

They exist. The run's artifacts folder holds the trainer's log, the
trajectory file and a complete copy of it, alongside both checkpoints.
Everything under `artifacts/` is excluded from the repository by
`.gitignore`, so **none of it can be cited at a commit**, and the packet's
own rule against uncommitted files put all of it outside this review.

Two things make this worse than a filing quibble.

1. **The previous run's equivalent is committed.** The A3 pilot's
   trajectory sits in the gates folder (`a3-gates/pilot_trajectory.jsonl`)
   at about 20 kilobytes. This run's is the same size and is not
   committed. The precedent exists and was not followed.
2. **The trajectory is the only record that could answer several
   questions this review had to leave open** — most of all whether the
   control battery was flat throughout or moved and came back, and what
   the loss did after step 1,000. The ledger preserves two points; the
   file has 109 evaluations.

The claim about the two log lines is itself fine, because the ledger
quotes them verbatim. The fix is one command, and it should be done before
this finding is quoted anywhere.

---

## 2. Satisfied by the wrong thing

*Every way DID NOT LEARN could be returned by a control battery that would
learn under supervision.*

| id | finding | label | severity |
|---|---|---|---|
| RT-57 | The intervention tripled the whole query loss against the action term, and nothing held that fixed | MEASURED / ARGUED | serious |
| RT-58 | The control rows are the first half of every batch, not a random half, for all 55,116 steps | ARGUED | serious |
| RT-59 | The split's correctness rests on "exactly one scored token per row", asserted in a comment and never tested | ARGUED | worth-noting |
| RT-60 | The evaluation can see what was learned — checked, clean | MEASURED | clean |
| RT-61 | The battery did not fail to learn; it converged on the name-blind solver | MEASURED | serious |

### RT-57 — a loss term on the wrong scale, and it is the whole query side

**MEASURED for the arithmetic, ARGUED for the consequence. Serious. This
is the most plausible route by which a battery that would learn returns
this number.**

With the flag off, the query part of the loss has total weight 1.0 and the
action term sits beside it at weight 1.0. With the flag on, the query part
becomes "other-term at 1.0, plus control-term at 2.0" — **total weight
3.0** — while the action term stays at 1.0. The ledger's own reading note
says this in passing, to stop anyone misreading the two loss curves side
by side, and it is right: the query loss went from about 1.08 to about
3.43 by construction.

But the pre-statement describes the action term as "unchanged". **Its
coefficient is unchanged. Its share of the gradient fell by about three
times.** Nobody wrote that down, and it is not a presentational point:

- Every parameter the four batteries share now receives a query signal
  three times larger relative to the action signal than on the checkpoint
  this run is compared against.
- The trainer clips the combined gradient to a fixed norm of 1.0 on every
  step. A query term three times larger means the clip bites at different
  moments and in different proportions, so the effective step size on
  shared parameters is not the same run to run.

There is no setting of this flag that raises the control's share while
holding the query side's total fixed. Even at a control weight of 1.0 the
query loss doubles, because the split replaces one average over all rows
with two averages added together. **The only neutral setting is off.** So
the dose and the rescaling arrived bundled, and the pre-statement's "one
coupling, stated rather than buried" — the state and syntax batteries
losing rows — names a different and smaller coupling than the one that
actually exists.

The state and syntax batteries finishing at 0.9960 and 1.0000 does not
clear this. Both were already at the top of their range and have room to
absorb a disturbance that the control battery, sitting near the floor, does
not.

**What would settle it:** a single arm at the same control weight and
fraction with the two terms renormalised so the query side still sums to
1.0. Same cost as the run already bought.

### RT-58 — the control trains on a fixed half of every batch

**ARGUED, and I could not settle it. Serious.**

The registered path assigns each row a question by rotating on both the
step number and the row's position in the batch, so over steps every batch
position carries every battery. The pilot flag replaces that with a fixed
positional rule: rows numbered below the halfway point carry the control
question and are marked as control rows; everything else round-robins over
the remaining two.

Whether that is harmless turns entirely on whether the episode generator
returns a batch in randomised order or in a systematic one. If episodes
come back ordered or blocked by any property — and the function is named
for balancing, which is what you do when you are allocating counts across
conditions — then **for all 55,116 steps the control battery trained on a
systematically biased half of the episode space and the state and syntax
batteries on the complement.** That is a mechanism by which the control
fails to learn for a reason that has nothing to do with how much
supervision it got, and it is introduced by the very change that was meant
to isolate supervision.

I could not check it: the episode generator is not in the review set.

The self-test does not close it either. It checks that half the rows are
control rows, that a control row carries the control question, and that a
non-control row never does. It never checks that the control rows are a
*representative* half. That check is one line, and the run is over.

**What would settle it:** generate one batch, group the first half and the
second half by whatever properties the generator balances, and compare the
two. Free, local, and it either clears the run or explains it.

### RT-59 — an untested assumption under the split

**ARGUED. Worth-noting.**

The split computes each row's loss by summing across positions and then
averaging across rows; the unsplit path averages across tokens. The two
agree only if every row carries exactly one scored token. The code says so
in a comment — "exactly one masked token per row, so summing over
positions gives that row's answer CE" — and nothing tests it.

The self-test's strongest claim is that with the flag off the query term
equals the pre-flag pooled term, to within a millionth. That is true and
it is also nearly vacuous: with the flag off, the code takes the same
branch it always took. The test that matters is the one on the split path,
and it was not written. If any row ever carries two scored tokens, the
control's term silently becomes a sum where the comparison is a mean.

A one-line assertion that every row's scored-token count is exactly one
would close it, and should be added before this flag is used again.

### RT-60 — the evaluation can see what was learned

**MEASURED. Clean, and recorded as clean.**

The control battery is scored by ranking the candidate answers within the
question's own choice set. That is an easier readout than the training
objective, which scores the answer token against the whole vocabulary. An
evaluation easier than the training signal cannot hide learning that the
signal produced. The endpoint used 800 episodes per draw, and every
question of every episode is scored, so the sample is the full 800 rather
than a third of it.

The spread across six draws (0.0240) is larger than the spread you would
get from sampling alone at that size (0.0164), which is what you expect
when each draw is a fresh set of items rather than a fresh subsample of
one set. That is the honest behaviour, and it means the quoted spread is
not an underestimate.

**No finding.** This route is closed.

### RT-61 — the battery learned the structure and none of the name

**MEASURED. Serious, as a misdescription rather than an error.**

Chance on this battery is 0.125. The name-blind reference solver reaches
0.3227. The control reads **0.3125** — which is **about 95% of the way
from chance to the name-blind solver**.

That is a far more specific result than "did not learn", and the findings
file does not state it. The model learned the entire procedure the
name-blind solver uses — form the candidate successors on the queried
item, strike the ones already visible as revisions, choose among what is
left — and learned **none** of the name-keyed lookup that would take it
past that solver. It is not near the floor. It is sitting exactly on the
name-blind solver's shoulder, and has been on all four checkpoints.

This matters because "DID NOT LEARN" is a cell label and will be read as
"learned nothing". The run measured something sharper and more useful:
**four times the supervision moved a battery that had already saturated
the name-blind procedure, and did not start it on the name.** Say that,
and the case for the remaining explanations — the reversed rendering, the
missing private route, an answer that appears in no turn — gets stronger,
not weaker, because all three are about reading the name.

---

## 3. No verdict

*Every way the run could have failed to answer the supervision question
