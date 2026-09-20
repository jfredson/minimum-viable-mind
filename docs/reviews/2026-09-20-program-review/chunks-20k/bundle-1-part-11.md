drawn uniformly over all four** then revise, one item each. The model is
therefore a reviser in half of episodes, and a scoring cell comes from
half of episodes.

**Why it took three drafts, recorded because a design that took three
tries should say so where it is registered.** Making the model revise in
every episode gives a cell every time but makes how much an agent speaks a
perfect giveaway. Making every agent revise removes that cue and creates a
worse leak: anyone who has already revised is not the one revising now, so
when the model revises last its own assignment is the only one left and
identifying it needs no self-knowledge at all, which lifted the true
ownership-blind ceiling to 0.52 while the record still said 0.29. Drawing
two revisers uniformly restores the ceiling and keeps both cues
uninformative. You cannot have all three of a cell in every episode,
revising not marking the model out, and agents that have acted not being
eliminable. Any two.

## 2. The speaker's name moves after the value (RT-20)

**Ratified text:** §2.2 assumed the registered rendering, in which a turn
opens with the speaker's name.

**Registered:** a turn renders `assign <item> to <value> by <marker>`.

**Why.** Under the old rendering the graded token is the value and the
model's own name sat three tokens back in its own context, so a solver
using no ownership information at all could read that name, find the
matching earlier assignment and apply the rule. Measured: **1.000 over
3,000 episodes**, on a grammar that had just passed both cue gates. The
cue gates could not have caught it, because they ask which turns are the
model's own, which is a different question. The attack is kept as a
permanent regression test in the grammar's own self-test.

## 3. The metric divides by the ceiling, not by chance (decision 3)

**Ratified text:** `d(B) = (B_base − B_abl) / (B_base − chance_B)`,
inherited from the registration.

**Registered:** `d(B) = (B_base − B_abl) / (B_base − ceiling_B)`, where
`ceiling_B` is the measured shortcut ceiling. **A value above 1.0 is
reported, never clipped**: it means the ablation took the battery below
what an ownership-blind solver reaches, so the lesion removed more than
ownership, and hiding that in a clamp would turn the most interesting
failure into a quiet 1.0.

**Why.** A lesion that removes ownership cannot push a battery below its
ceiling, so dividing by the distance to chance divides by a range the
battery cannot traverse — and the error differs per battery. With ceilings
of 0.2921 and 0.3227 the two verdict batteries could show at most 0.809
and 0.774, so a lesion of a purely **generic** binder, which hits both
equally in real terms, still reported a differential of 0.035 against a
band near 0.01. The bin meant to catch the boring explanation could not
fire and the bin meant to find a self-index fired on it. Under the
registered metric that differential is exactly 0.

## 4. The ceilings are measured, not asserted (decision 2)

**Ratified text:** §2.2 pre-states a lookup ceiling of 0.25.

**Registered:** **0.2921** for the primary battery and **0.3227** for the
control, measured on the registered grammar and verified by the attack
sweep, whose best ownership-blind attack reached 0.3036 on 12,000
episodes — one standard error from the analytic value. Both numbers are
stored in `batteries-a3/batteries_meta.json` with their method. Any future
grammar carries its own measured ceilings; none is ever asserted.

> **REGISTERED DEFECT, 2026-09-17 (John's instruction; decidedBy john).
> Nothing above is altered. The claim "verified by the attack sweep" is
> FALSE as applied to the control battery.**
>
> The 0.3036 attack figure quoted above is an attack on the **primary**
> battery, compared against the primary's 0.2921. `src/shortcut_sweep.py`
> contains **zero** occurrences of the control battery and attacks the
> primary only. One verification is attached to two numbers.
>
> The control's 0.3227 rests entirely on the reference solver in
> `curriculum_a3.measured_ceilings`, **which never reads the marker the
> control question supplies**. The control asks about a *named* agent;
> the solver enumerates all four agents' successors and guesses among
> those not already visible. So 0.3227 is the score of a solver that
> cannot read names, and the battery's real ownership-blind ceiling is
> **near 1.0 and unmeasured**.
>
> The module's own documentation states the control's lookup ceiling as
> **0.5**, not 0.3227, and says red-team pass 3 "should weigh" it because
> the generic-binding bin turns on the two batteries' difference. That
> pass ran and did not weigh it.
>
> **No result changes.** The control fails its floor at 0.3227, fails by
> more at 0.5, and fails by far more at a true ceiling near 1.0. Every
> reading makes it less learned. What changes is that the metric's
> denominator for this battery was never a checked quantity.
>
> **If an Amendment A4 opens, measuring this ceiling properly is a
> precondition of it** (John, 2026-09-17). Full record:
> `ceiling-defect-2026-09-17.md`.

## 5. The attack sweep becomes a gate (decision 8)

**Registered:** `src/shortcut_sweep.py` is a gate in its own right, run
before any dollar is spent. **It passes when no ownership-blind attack
beats the stated ceiling by more than sampling error** — that is, when the
stated ceiling is the true one. If it cannot be made to pass within two
regenerations, the design halts.

**Why this shape rather than a threshold on the ceiling.** The sweep's job
is to make the stated ceiling honest, not to veto a design. A ceiling that
is high but honest weakens the learnability reading and shrinks the range
a lesion can show, but both degrade smoothly and neither has a cliff; an
earlier draft of this clause proposed halting above 0.40 and that number
could not be derived. Whether an honest ceiling is too high to be worth
training is the judgment in item 1, not an automatic kill.

## 6. Thresholds, kills and bins (decisions 4, 5, 6, 12; K0's number)

- **Revision frequency** is now stated (item 1): two of four agents, drawn
  uniformly, so half of episodes carry a supervised action and a 400-cell
  verdict needs 800 episodes.
- **K2** compared "lookup ceiling plus the null band", adding a raw
  accuracy to a chance-corrected quantity. It is restated in raw accuracy,
  with the band converted explicitly. It decides the unlearnable verdict,
  so it is fixed before the pilot rather than after.
- **K0's band stays at 0.25**, the pre-stated figure, deliberately
  unchanged now that Gate 0 has measured the band at about 0.01. Moving it
  either way after seeing the data would be fitting the rule to the data,
  and the value of a pre-stated number is that you do not touch it once
  you have looked. It is read **only on batteries above the floor margin**,
  so a run that never learned a battery cannot trip it.
- **θ and δ are per battery**, not single numbers. Gate 0 measured them
  varying across a twenty-five-fold range within one checkpoint.
- **A bin is added for the validity check failing.** If zeroing the acting
  channel does not collapse the primary battery to its ceiling, ownership
  is not load-bearing and the objective has failed. The registered design
  had such a guard and it was dropped along with the register. Without a
  bin that outcome has nowhere to land, and an outcome with nowhere to
  land gets explained away.
- **An uncertifiable likelihood attack is routed.** If the act-withheld
  arm's positive controls do not fire, the arm is declared uncertifiable
  rather than passed or failed, and the procedure continues with that
  stated, instead of deadlocking.

## 7. The cue detector's sampler (decision 7 and the sampler amendment)

Both arms of the detector are now drawn the same way, and the verdict is
taken over five independent samples rather than one. Full reasoning,
including that the change was prompted by a grammar failing the old
detector, is in `cue-detector-sampler-amendment.md`. Every verdict reports
both samplers side by side. The amended detector was re-run against every
grammar the old one passed, including the registered MVM-0a grammar, which
reads 0.4969 under the old sampler and 0.4984 under the new one — so the
clean verdict the five existing checkpoints rest on is undisturbed.

## 8. The central claim is narrowed (decision 9)

**Ratified text:** §2.2, that the only route from the ceiling to full
accuracy is to bind the act to the item when acting and carry that binding
forward.

**Registered:** that claim is too strong and was false of two of the three
drafts. The acting channel marks positions, and attending back to marked
positions is a re-readable pointer rather than a carried binding. Both
routes need the channel, so the wire lesion cannot separate them. The
mid-episode re-indexing probe, already registered for the tag bin, is the
discriminator.

## 9. The loss (decision 10)

**Registered:** the loss is the action cross-entropy at the model's own
revision position plus the query-answer cross-entropy, **summed with equal
weight**, the weight passed explicitly at every launch rather than left to
a default. The reading confirmed: §2.1's "not a query asking it to
describe who did what" is satisfied because **no query anywhere asks about
the model's own commitments** — the self-report battery is gone — while
the ownership-free and other-agent queries stay supervised. Read at its
strictest the clause would remove query supervision entirely, and then the
control batteries would never be trained and the differential the
generic-binding bin turns on would be meaningless.

## 10. Money (decision 11)

**Registered, from measurement rather than estimate:** the token budget is
fixed at twenty tokens per parameter, so the longer episodes mean **fewer
steps** (0.71×), which offsets most of the higher per-step cost (1.26×
enactment passes, 1.41× sequence length). A run is **9.1 to 12.8 hours,
$9 to $13**; three seeds **$27 to $39**. The optional extra seeds remain
available inside the $100 hard stop but need a separate go. The $400
ceiling, the $100 stop and the corrigibility commitments are unchanged and
were not reopened.

**Note for the launch:** the RunPod account carries a spend limit of $80,
below the $100 stop. It should not bind at these costs, but it exists.

## What is registered, and what runs next

Registered: the grammar at `src/curriculum_a3.py`, its tokenizer at
`src/encoding_a3.py`, the trainer at `src/train_a3.py`, the batteries
frozen at `batteries-a3/`, the gates at `src/cue_detector_a3.py` and
`src/shortcut_sweep.py`, the calibration at
`src/null_calibration_a3.py`, the lock guard at `src/lock_guard.py`, and
the launcher at `src/launch_a3.sh`.

Next is Gate 2, the pilot: one register-less 30M run at seed 0, on John's
authorization in his own words, quoted verbatim in the ledger row. Nothing
has been spent on A3 to this point.


===== FILE: experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot.md =====

# Control-learnability pilot — pre-statement

**UNREGISTERED. Written and committed BEFORE the code change and before
any run, at John's instruction of 2026-09-19.** One 30M register-less
seed, run exactly the way the A3 pilot was run on 2026-09-15. Nothing
here is registered text, no registered verdict is read from this run, and
**nothing launches without John's go in his own words, quoted in the
ledger row.**

*TimeAssembler task: the control-learnability pilot (`90763b8f`).*

---

## The question

**Does the control battery learn when it carries its own loss term,
instead of a third of a shared one?**

The control battery has not learned on any checkpoint. Its intact scores
are 0.2877, 0.3057 and 0.3195 across the pilot and seeds 1 and 2 — all
below 0.3227, the score reached by a reference solver that cannot read
the name the control question supplies. Three seeds, one outcome, so it
is not a seed lottery.

Two explanations have been live since the 2026-09-17 audit and have never
been separated. Either **the control is under-supervised** — it receives
roughly one training row in three, sharing a single pooled term with two
much easier questions, while the primary battery has a dedicated
full-weight term of its own — or **supervision is not the binding
constraint**, and something else in the design defeats it: the reversed
rendering it must attend backwards through, the absence of the private
route the acting channel gives the primary battery, or the fact that its
answer appears in no turn and must be retrieved and then transformed.

This pilot separates them, once, for about ten dollars.

**What it does not do.** It does not repair Amendment A3's registered
comparison, which was refused on 2026-09-19 and stays refused. A control
that learns would make a comparison *designable*; it would not make the
A4 clause registerable, whose fatal findings were about what the clause
measures and where it is read, not about the control's score. **A3 stays
open, not closed**, and this pilot informs that decision rather than
making it.

---

## The change to the training objective

**One paragraph, and no grammar change.** The grammar, the tokenizer, the
frozen batteries, the episode structure, the rendering, the ceilings and
the attack sweep are all untouched; the only thing that moves is how the
loss is apportioned across the queries each episode already carries.
Today every training row carries exactly one query, chosen round-robin
from the three an episode holds, and the cross-entropy on that one answer
token is averaged into a single pooled term shared by the control
battery, the state battery and the syntax battery — so the control gets
about a third of the rows and a third of one term. Under the flag, the
batch is split: **half the rows carry the control query and its
cross-entropy becomes a term of its own with its own weight**, while the
remaining rows carry the state and syntax queries round-robin in a
separate term, and the primary battery's dedicated action term at the
model's own revision position is unchanged. At the flag's default weight
of 2.0 the control's share of the query gradient rises from about a third
to about two thirds, and **its per-row weight quadruples** — from
one-one-hundred-and-twenty-eighth of the pooled term to two
sixty-fourths of its own. With the flag off, the trainer computes exactly
what it computes today.

**Two design calls in that paragraph, both mine, both flagged, and
neither registered so John can move either before the go.**

- **Why the batch is split rather than a second forward pass added.** A
  truly per-episode control term — the control query on *every* episode,
  not half of them — needs a second forward pass and would roughly
  double the step time, taking the run from about ten hours and ten
  dollars to about twenty and twenty. Splitting the batch buys a
  dedicated, separately weighted term **at no extra compute**, which is
  what keeps the estimate on the pilot's measured 0.645 seconds per step.
  *Confidence: high that this is the right trade for a ten-dollar
  question. The strongest alternative is the second forward pass, which
  is the cleaner intervention and tests a stronger dose; it was rejected
  on cost, not on merit.*
- **Why the weight is 2.0.** It is a judgment, not a derivation. The
  arithmetic above is the whole justification: it is the dose at which
  the control's per-row gradient weight quadruples, which is large enough
  that a null result is informative about supervision rather than about
  the dose being timid. *Confidence: moderate. A larger dose would make a
  null more decisive and risks destabilising the other batteries; a
  smaller one makes a null uninterpretable.*

**One coupling, stated rather than buried.** The flag changes two things
at once — the control gets a term of its own *and* it gets more rows —
so a positive result will not say which of the two did the work. That is
deliberate and matches the question as John framed it, which contrasts
"its own loss term" against "a third of a shared one". The two halves are
not separated here and a follow-up would be needed to separate them.

**A consequence worth naming:** the state and syntax batteries drop from
about a third of the rows each to about a quarter. Both sit at 0.999 and
1.000 intact, so there is room, but the secondary cells below watch for
it.

---

## Pre-stated outcome cells

**Primary, read on the control battery's intact score at the registered
endpoint evaluation.** These boundaries are John's, set on 2026-09-19
before the code existed.

| control intact score | cell | what it reads |
|---|---|---|
| **at or above 0.60** | **LEARNED** | the control learns when properly supervised. Name-keyed lookup is available to it, and it is using it. Supervision was the binding constraint. |
| **above 0.3227 and below 0.60** | **PARTIAL** | supervision moves it but does not carry it. Something else in the design is also binding. |
| **at or below 0.3227** | **DID NOT LEARN** | supervision is **not** the binding constraint. Option D (a scaffolded intermediate query, which teaches plain name-keyed retrieval before layering the rule on top) or closing A3 is what is left. |

The 0.3227 boundary is the score of the reference solver that cannot read
the name the control question supplies. A battery at or below it has not
learned the task, whatever else is true.

**Secondary cells, reported with the primary and never in place of it.**

| reading | expected | what a miss would mean |
|---|---|---|
| **primary battery still learns** | intact **≥ 0.50** | below 0.50, the reallocation damaged the objective that works, and the pilot answers nothing: the run is reported as a failed intervention, not as evidence about the control. |
| **the input-channel lesion still collapses the primary battery** | collapse, as on all three existing checkpoints (0.57 → 0.14–0.20) | if the primary battery survives its own lesion, ownership has stopped being load-bearing under the new weighting and no reading about the control is available from this run either. |

**No threshold is crossed and no registered verdict is read.** The cells
above are raw intact scores. John's committed threshold lock governs
registered readings on registered checkpoints; this run is unregistered,
reads no registered verdict, and does not touch the lock.

---

## What is run, exactly

Identical to the A3 pilot of 2026-09-15 in every respect but the flag:
one 30M **register-less** run — the launcher has no flag that could train
a register — at **seed 0**, chosen so the comparison against the existing
pilot is matched on initialization and data order and **the loss is the
only thing that differs**. Registered recipe values, unchanged:
585,544,960 tokens, 55,116 steps, batch 128, action weight 1.0,
evaluation every 500 steps at n=100 for the trajectory only. Artifacts go
to a distinct output name so nothing can overwrite the existing pilot's
checkpoint.

**Cost, from the pilot's measured 0.645 seconds per step:** 55,116 × 0.645
= 9.87 hours of training, about 10.2 hours of pod life at $0.99/hour on
the registered venue, so **about $10.2, band $9–13**. That takes the A3
cumulative from $34.31 to about $44.5 against the $100 hard stop. Step
count and token budget are unchanged because the grammar is unchanged;
the one thing that could move the measured pace is that control questions
render at a slightly different length from state and syntax ones, so
padded batches may differ by a few percent. **The ledger records the
measured pace at step 500**, as it did for the pilot, and the estimate is
revised in flight if it has moved.

---

## Order, and the gates

1. This pre-statement, committed **before** the code change. *(Done: this
   file.)*
2. The loss change behind a flag, self-tested, committed.
3. One run staged through the registered launcher with the flag, dry-run
