
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
