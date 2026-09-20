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
