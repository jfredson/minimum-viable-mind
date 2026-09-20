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
