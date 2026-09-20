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
and been read as answering it.*

| id | finding | label | severity |
|---|---|---|---|
| RT-62 | The matched comparison the design was built around is missing, and "bought nothing" is false | MEASURED | **fatal** |
| RT-63 | "0.42 standard deviations" is the spread of one draw, not the uncertainty of the mean being scored | MEASURED | worth-noting |
| RT-64 | One training seed; the design only ever had power against a large effect | ARGUED | serious |
| RT-65 | The control is flat at the end and the budget was not short-changed — checked, clean | MEASURED | clean |
| RT-66 | The one trajectory reading in the review set also runs the intervention's way | MEASURED | worth-noting |

### RT-62 — the comparison the pre-statement designed is not in the findings

**MEASURED. Fatal — one sentence in the interpretation is false as
written, and the number that makes it false is absent.**

The pre-statement is explicit about why this run used seed 0:

> chosen so the comparison against the existing pilot is matched on
> initialization and data order and **the loss is the only thing that
> differs**

Its counterpart therefore exists and is in the review set. The A3 pilot at
seed 0, with none of this supervision, reads the control battery at
**0.2877** (spread 0.0302). This run, same seed, same initialization, same
data order, reads **0.3125** (spread 0.0240).

**The matched move is +0.0248.** Treating the two six-draw means as
independent, the standard error of that difference — the amount it would
wobble if you re-measured — is 0.0157, so the move is about **1.6 standard
errors**: it does not reach conventional significance, and it is not
nothing either.

The findings file does not report this comparison at all. It sets 0.3125
beside all three checkpoints — 0.2877, 0.3057, 0.3195 — which are three
*different training seeds*, and so re-imports exactly the between-seed
variation the matched design existed to remove. Against the mean of those
three (0.3043) the move is +0.0082, about half a training-seed standard
deviation, and that is where the sentence "the intervention moved nothing
distinguishable from seed variation" comes from.

That sentence is defensible. **The next one is not:**

> quadrupling the control's per-row gradient weight bought nothing

It bought about **+0.025, give or take 0.016**, on the comparison the
pre-statement was written around. "Not distinguishable from nothing" and
"nothing" are different claims, and only the first is true. A four-times
dose that moves a saturated battery a quarter of the way to its next
boundary, on one seed, is a weak positive that failed to reach
significance — not a zero.

**Both comparisons are legitimate. Only one was designed in advance, and
it is the one that is missing.**

There is also a sharper version available for nothing. Both checkpoints
were read on six evaluation draws. If they are the same six draws — this
run's are numbered 771000 through 771185, and the three-seed write-up says
its six are the first six of the twelve from the noise measurement — then
the difference can be taken **within each draw**, on the same held-out
items, which removes the item-set variation from both sides and would
tighten the estimate considerably. I could not do it: the earlier pilot's
per-draw control scores are not in the review set, only its summary. It
costs nothing and should be done before the step 4 proposal cites this
run.

**What survives:** the DID NOT LEARN verdict. 0.3125 is below 0.3227 on
the mean, it is nowhere near 0.60, and RT-61 shows the battery has
saturated the name-blind procedure. **What must not survive:** the words
"bought nothing", and the presentation of an unmatched three-seed
comparison in place of the matched one the pre-statement promised.

### RT-63 — the wrong spread against the boundary

**MEASURED. Worth-noting, and it cuts in the findings' own disfavour.**

The distance table reports the control as "0.42 standard deviations" below
0.3227 and "11.98" below 0.60, using 0.0240 — the spread of a *single*
evaluation draw. But the cell is scored on the **mean of six**, and the
uncertainty of a mean of six is the spread divided by the square root of
six: 0.0098. On that footing the control sits **1.04 standard errors**
below 0.3227, not 0.42.

The table's heading, "in standard deviations", is literally accurate. It
is simply not the uncertainty of the quantity the cell is read on.

The consequence runs against the findings' own hedge. They warn that "a
rerun could formally land in PARTIAL". How likely depends on what a rerun
means:

- a fresh single evaluation draw lands above 0.3227 about **34%** of the
  time;
- a fresh six-draw estimate, which is what the cell is actually read on,
  does so about **15%** of the time.

So the finding is better supported than its own caveat says. The caveat
should stay — it is the right instinct — but with the right number
attached.

### RT-64 — one training seed, and only a large effect was ever detectable

**ARGUED. Serious.**

The six seeds are **evaluation** seeds. They redraw the held-out set from
one checkpoint. They say nothing whatever about what a second *training*
seed would have done, and the three flag-off checkpoints put training-seed
spread at about 0.016 — comparable to the evaluation spread, and larger
than the matched move in RT-62.

A single training seed at that spread cannot separate "supervision does
nothing" from "supervision buys +0.02 to +0.03", which is roughly what the
matched comparison shows. The pre-statement implicitly accepted this by
setting LEARNED at 0.60: only a large effect was ever going to be
detectable, and a large effect is genuinely excluded.

The problem is that the conclusion now being drawn — "supervision is not
the binding constraint" — is a claim about small and moderate effects too,
and the run has no power against those. The design answers "does
supervision carry this battery?" It does not answer "does supervision do
anything?", and the findings file's own framing slides between the two.

### RT-65 — the run did answer the question it was bought for

**MEASURED. Clean, and recorded as clean, because it closes two escapes.**

Both secondary cells pass, as the findings say: the primary battery still
learns (0.5727 against the 0.50 the cell asks) and still collapses under
its own lesion (to 0.1663, a corrected drop of 1.448, in the same band as
the three earlier checkpoints). So this is not a failed intervention.

Two further checks, which the findings do not make and which matter more
than they look:

- **The control is flat at the end.** The partial checkpoint at step
  51,500 reads 0.3158; the full checkpoint at 55,116 reads 0.3125. That is
  a move of **−0.0033 over the last 3,616 steps**. This is not a battery
  still climbing when the budget ran out, which is the most obvious way a
  null could be an artefact of stopping early.
- **The budget was not short-changed by the flag.** The ledger records
  0.6508 seconds per step against the earlier pilot's 0.6501 — within
  about 0.7% — and the run finished on the identical 55,116 steps and
  585,552,384 tokens, confirmed by the completion sentinel and matching
  the earlier pilot and seeds 1 and 2. The padding worry the pre-statement
  flagged was real and negligible.

Minor, and recorded because the packet asks about every quantity the
pre-statement names: the pre-statement and the launcher both state the
budget as 585,544,960 tokens; the run stopped at 585,552,384, the first
step-multiple at or above it. The findings file quotes the second. Both are
right; they are different quantities and nobody says so.

### RT-66 — the early trajectory also runs the intervention's way

**MEASURED. Worth-noting.**

The one trajectory reading inside the review set is in the ledger, at steps
500 and 1,000: this run reads 0.28 and 0.27 on the control battery against
the earlier pilot's 0.24 and 0.18 at the same steps on the same seed.

Nothing should be read from 1.8% of training at 100 episodes, and the
ledger says so at length and correctly. It is recorded here only because it
is the second place where the matched comparison favours the intervention
slightly, and the findings file quotes neither. Two weak indications in the
same direction are still weak — but a findings file that reports neither,
and then says the intervention "bought nothing", has selected against its
own result.

---

## 4. Over-reading

*What "supervision is not the binding constraint" will be read as
claiming, beyond what one seed at one weight setting measured.*

| id | finding | label | severity |
|---|---|---|---|
| RT-67 | The sentence will be read as ruling out supervision; the run tested one dose of one form of it | ARGUED | serious |
| RT-68 | Step 4 should narrow — but for a reason the findings do not give, and the stated reason undercuts the option it points to | ARGUED | serious |
| RT-69 | Any step 4 option that keeps this battery inherits the ceiling precondition John already set | MEASURED | worth-noting |

### RT-67 — what the sentence will be taken to mean

**ARGUED. Serious.**

What was measured: on one training seed, at four times the per-row weight
and two thirds of the query gradient, with the whole query side
simultaneously tripled against the action term, the control battery moved
+0.0248 against its matched counterpart and stayed on the shoulder of a
name-blind solver.

What "supervision is not the binding constraint" will be taken to mean, in
the current-state document, in the 4 October control-battery proposal and
in the paper: **supervision has been ruled out.** That is a claim about
every dose and every form of supervision, and three things sit outside what
the run touched:

1. **Other doses.** One point on a dose curve. The pre-statement said as
   much — a larger dose "would make a null more decisive" — and the larger
   dose was not run.
2. **Other forms.** The pre-statement's own rejected alternative, a second
   forward pass putting the control question on *every* episode rather
   than half of them, is a different and stronger intervention that was
   rejected on cost, not on merit. It remains untested.
3. **The confound.** RT-57: the dose did not arrive alone. Until an arm
   renormalises the query side, "the control's share was raised" and "the
   whole query side was tripled" are not separated — and the pre-statement
   already warns that the flag changes two things at once, while naming a
   *different* pair than the ones that actually moved.

The honest scope is narrower and still useful: **reweighting the rows the
control battery already had does not teach it to read the name.**

### RT-68 — narrow step 4, but say why properly

**ARGUED. Serious. This is the recommendation the packet asks for.**

**Yes, this supports narrowing step 4 to option D or closing A3. No, a
cheaper supervision variant is not live as a route to 0.60. But the
findings file gives the weaker of the two available reasons, and the one it
gives argues against the option it points to.**

**The practical case, which does not depend on anything contested above.**
The control is 95% of the way from chance to a name-blind solver (RT-61)
and flat over the last 3,600 steps (RT-65). Four times the per-row weight
bought about +0.025 (RT-62). The distance remaining to 0.60 is 0.29 —
**more than ten times what the intervention bought.** Extrapolating from a
single dose is not evidence and I am not offering it as evidence; but
nothing in this run suggests any reweighting of existing rows clears 0.60,
and the money would be better spent elsewhere.

**The stronger case, which is in the review set and which the findings miss
entirely.** Even a rerun landing in PARTIAL would change nothing for
Amendment A3. The operative bar for this battery to be *useful* is not
0.3227 but **0.4227** — the corrected floor rule of ceiling plus 0.10
(RT-53). Below that the control's drop stays undefined and the registered
differential clause stays uncomputable, exactly as it is on all three
existing checkpoints. **So the whole band from 0.3227 to 0.4227 is a band
in which the control "learns" by the pre-stated cell and Amendment A3 is no
better off than it is today.** The findings file's anxiety about a rerun
formally landing in PARTIAL is therefore misplaced twice over: it is less
likely than stated (RT-63), and it would not matter if it happened.

That argument narrows step 4 far more firmly than "supervision is not the
binding constraint" does, and it survives every objection in this review.

**The case against, which the step 4 proposal must handle.** Option D — a
scaffolded intermediate query that teaches plain name-keyed retrieval
before layering the rule on top — **is itself a supervision change.** It
adds a training signal the control battery does not currently receive. So
"supervision is not the binding constraint" and "therefore do option D" sit
badly together, and a proposal that cites this review for the first claim
will be citing it against its own recommendation. What the run actually
rules out is **reweighting rows the battery already had**. What option D
proposes is **giving it a different and easier question first**. Those are
different interventions, and the run says nothing against the second. Write
it that way, or the contradiction will be found by someone else.

### RT-69 — the ceiling precondition still binds

**MEASURED. Worth-noting.**

John ruled on 2026-09-17 that if an Amendment A4 opens, measuring the
control battery's ceiling properly is a precondition of it. That ruling is
in the registered text. Any step 4 option that keeps this battery — option
D certainly does — inherits it, and the true ceiling near 1.0 is still
unmeasured. The 4 October proposal should carry the precondition
explicitly rather than leave it to be rediscovered.

### The sentence for the current-state document

The packet asks for the sentence that should go in `STATUS.md`. Proposed,
and deliberately avoiding both "supervision" as a bare word and the cell
label as a summary:

> **Giving the control battery its own loss term — four times the per-row
> weight, two thirds of the query gradient instead of one third — left it
> at 0.3125, against 0.2877 on the matched checkpoint that received none of
> it: still on the shoulder of a solver that cannot read the name the
> question supplies, and nowhere near the 0.60 that would show it had
> learned to read it. Reweighting the rows it already had is not what this
> battery is missing.**

Three choices in that sentence, each deliberate. It quotes the **matched**
comparison, because that is the one the pre-statement designed and the one
the findings file omits (RT-62). It says **"reweighting the rows it already
had"** rather than "supervision", because that is what was tested and the
broader word would be over-read (RT-67). It does not say "bought nothing",
because that is false (RT-62).

If a second sentence is wanted, it should be the one the findings file
should have led with: **the battery has learned the whole name-blind
procedure and none of the name-keyed lookup, which is what the three
remaining explanations are all about.**

---

## Kill case

The strongest case for throwing this interpretation out is RT-57 joined to
RT-58: the intervention did not do one thing, it did three. It raised the
control battery's share of the query gradient, it tripled the size of the
entire query loss against an action term that was never meant to move —
changing what the gradient clip does to every shared parameter on every
step — and it replaced a rotating assignment of questions to batch
positions with a fixed one whose representativeness nobody checked and
which then ran unchanged for 55,116 steps. On top of that it is one
training seed, and the matched comparison the design was built around moved
**+0.0248 with a standard error of 0.0157** — in the direction the
intervention predicted, at about 1.6 standard errors — and was reported as
"nothing". If the fixed positional split fed the control a biased half of
the episode space, or if tripling the query side degraded the shared trunk,
then a control battery that *would* learn under a clean reweighting returns
exactly this number, and the run has measured its own confound rather than
the question it was bought for. Nothing in the committed record excludes
either, because the two one-line checks that would have — episode order,
and one scored token per row — are not in the self-test, and the log and
trajectory that would show the run's behaviour over time are excluded from
the repository. **I do not think that kills the finding.** The battery sits
95% of the way from chance to the name-blind solver and is flat over the
last 3,600 steps, so whatever the confounds did, they did not hide a
battery on its way up; and the distance to the 0.60 boundary is more than
ten times what four times the supervision bought. The verdict should stand
with its scope cut to what was actually run — **reweighting the rows the
control battery already had does not teach it to read the name** — and the
sentence "supervision is not the binding constraint" should not enter the
current-state document, the 4 October proposal or the paper in that form.
