
**No ceiling is measured in this note.** Measuring it is the precondition
above, and John's instruction was to register the defect before further
analysis. Nothing here authorises spend, and nothing here changes
registered text.

## How this was found

Not by review of the registration, which had passed three red-team passes
with the mismatch sitting in the module's own docstring the whole time. It
surfaced from asking a narrower question, why the control battery failed
to learn, and reading the code that defines it. The original comment
predicted the exact failure mode and named the review that should have
caught it. The lesson worth keeping is that a warning written into the
code is not a warning anyone has read.


===== FILE: experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot-findings.md =====

# The control battery does not learn when it is properly supervised

*2026-09-20. Unregistered diagnostic. Question and outcome cells were
written and committed **before the code existed** (`control-learnability-pilot.md`,
commit `7eee3c5`); the boundaries below are John's, set before any number
came back. No registered verdict is read here and John's threshold lock is
not touched. Cost: **$9.9** for the run plus **$0.067** to recover the
checkpoint.*

## Verdict: DID NOT LEARN — supervision is not the binding constraint

The control battery was given a loss term of its own, at double weight,
on half the training rows instead of about a third — **its per-row
gradient weight quadrupled and its share of the query gradient went from
about a third to about two thirds.** It scored **0.3125**.

The three existing checkpoints, trained without any of that, scored
0.2877, 0.3057 and 0.3195.

**The intervention moved nothing distinguishable from seed variation.**

## The numbers

Full registered budget — 55,116 steps, 585,552,384 tokens, identical to
the A3 pilot and seeds 1 and 2. Six independent evaluation seeds at
n=800, intact and lesioned paired within each seed.

| battery | intact | under the input-channel lesion |
|---|---|---|
| **control (T_other)** | **0.3125** (sd 0.0240) | 0.2613 (sd 0.0258) |
| primary (T_act) | 0.5727 (sd 0.0212) | 0.1663 (sd 0.0135) |
| state | 0.9960 (sd 0.0022) | 0.9787 (sd 0.0094) |
| syntax | 1.0000 | 1.0000 |

**Against John's pre-stated cells:**

| boundary | distance | in standard deviations |
|---|---|---|
| DID NOT LEARN, at or below **0.3227** | −0.0102 | **−0.42** |
| LEARNED, at or above **0.60** | −0.2875 | **−11.98** |

**Both secondary cells pass**, so the intervention did not break what
works and the run answers the question it was bought for. The primary
battery still learns, at 0.5727 against the 0.50 the cell asks. The
input-channel lesion still collapses it, to 0.1663, a ceiling-corrected
drop of 1.448 — in the same band as the three existing checkpoints.

## Where the verdict is thin, and where it is not

**Thin, and stated rather than glossed.** The control sits 0.42 standard
deviations below the 0.3227 boundary, and across the six evaluation seeds
it ranged 0.2850 to 0.3460 — so **individual draws land on both sides of
that boundary.** The cell is scored on the mean, and the mean is below
it, but a rerun could formally land in PARTIAL. Anyone quoting "DID NOT
LEARN" as a crisp result is quoting it harder than the data supports.

**Not thin at all.** The boundary that carries the reading is 0.60, and
that is **twelve standard deviations away**. Whether the control formally
landed in DID NOT LEARN or scraped the bottom of PARTIAL changes nothing:
on either reading it is indistinguishable from three checkpoints that
received none of this supervision, and it is nowhere near the level that
would show it had learned name-keyed lookup. **The distinction the cells
draw at 0.3227 is not the distinction that matters here.**

## What this settles

**Supervision was not the binding constraint.** That reading has been
live since the 2026-09-17 audit and was never separated from the
alternative. It is separated now: quadrupling the control's per-row
gradient weight bought nothing.

So the remaining explanations are the ones the audit named that are *not*
about supervision — the reversed rendering the control must attend
backwards through, the absence of the private route the acting channel
gives the primary battery, and the fact that its answer appears in no
turn and must be retrieved and then transformed.

**By John's own pre-statement, what is left is option D — teaching plain
name-keyed retrieval before layering the rule on top — or closing A3.**
That is what the pre-statement says, recorded here because it was written
before the number. **It is not a recommendation and nothing is proposed
here.** A3 stays open on John's ruling of 2026-09-19, and the choice is
his.

## Two things worth recording that were not the question

**The coupling cost nothing.** The pre-statement flagged that the state
and syntax batteries would drop from about a third of the training rows
to about a quarter, and watched for damage. The state battery finished at
0.9960 and syntax at 1.0000. It recovered fully; the reallocation was
free.

**The control does fall under the lesion**, from 0.3125 to 0.2613. It is
not inert. That bears on the independent red team's observation that
under this lesion *everything* falls to some degree, and it is reported
here rather than left for someone to find.

## Process, recorded because it will recur

The run completed its full budget and **the final checkpoint was nearly
lost to a race between two safety mechanisms.** The trainer self-terminates
its pod on completion — added after idle billing cost about $9.50 across
three occurrences — and the laptop watchdog performs the final
fetch-and-delete on its roughly ten-minute poll. The trainer finished
between polls, wrote everything, and deleted its own pod before the
watchdog came back. The trainer's own log records both acts on
consecutive lines.

Nothing was lost: checkpoints are written to the network volume, and the
file was recovered intact and checksum-verified for $0.067. But the
locally held copy stopped at step 51,500 until it was, and **this will
happen on every future run that finishes normally.** Full record in
`compute-ledger.md`. No fix is proposed here.

*For the record: the run also billed **zero idle time**, the first in the
programme's history, because self-termination worked exactly as designed.
The same mechanism caused both outcomes.*


===== FILE: experiments/06-mvm-0a-constructed-self-index/blind-arm-findings.md =====

# Blind-localization arm — result

*2026-09-16. Local, $0, no compute rented. Read strictly against the
criteria committed in `401a54d` and `da0427f` **before the run produced
any output**. No bin was added after the fact.*

## Verdict

**NOT FLAGGED**, and within that, the sub-bin **instrument failure to
locate**.

The stack did not find own-agent identity at all. Criterion (a) — the
best probe clearing its label-permutation null by three standard
deviations — failed at every layer, and failed by a wide margin. The best
layer reached **1.3 standard deviations**, less than half the bar.

Because (a) failed, criterion (b) is moot: the subspace that was ablated
is one the probe never validly located, so the small drops below are
ablations of a direction that decodes at chance. They are reported for
completeness, not as evidence.

> **ANNOTATION, 2026-09-16 (John's ruling).** *Superseded in
> interpretation by the unblinded register probe: no valid target.*
>
> The verdict above and its pre-stated sub-bin name stand exactly as
> committed. John ruled the name is **not retired**: "The committed
> verdict and its pre-stated name stand as written. Add a dated
> annotation beside it ... Annotate, never rewrite."
>
> What the annotation records is that the *interpretation* has been
> superseded, not the verdict. The unblinded probe of the register at its
> known location found no own-agent identity at any turn, so there was
> nothing at this location for the blind stack to locate. "Failure to
> locate" remains the correct name of the bin the result fell into under
> the criteria as committed. It is no longer the correct description of
> what happened. See `register-direct-probe-findings.md`.

## The numbers

Four agents, so chance is 0.25. Every probe sits on it.

| layer | probe accuracy | null mean | null sd | margin |
|---|---|---|---|---|
| 3 | 0.2575 | 0.2473 | 0.0249 | 0.41 sd |
| 4 | 0.2675 | 0.2482 | 0.0243 | 0.80 sd |
| 5 | 0.2625 | 0.2435 | 0.0224 | 0.85 sd |
| **7** | **0.2750** | 0.2441 | 0.0237 | **1.30 sd** |
| 8 | 0.2450 | 0.2417 | 0.0227 | 0.15 sd |

Ablating the best-layer subspace at the inherited rank moved nothing. The
largest chance-corrected drop was **0.0739**, against the ruled Gate 0
band of 0.25, and it was **negative** — the battery it touched went *up*,
from 0.842 to 0.895, which is what noise looks like.

| battery | baseline | lesioned | drop |
|---|---|---|---|
| T_sr | 0.993 | 0.985 | 0.0092 |
| T_si | 0.960 | 0.955 | 0.0060 |
| T_state | 0.993 | 0.990 | 0.0033 |
| T_syntax | 1.000 | 1.000 | 0.0000 |
| T_sr_rev | 0.842 | 0.895 | −0.0739 |

## What this does and does not support

*Amended 2026-09-16 on John's ruling. The original wording of this
section claimed more than the numbers carry, in two places. Both are
corrected here rather than quietly rewritten, and what was originally
written is stated so the correction is checkable.*

**The specificity reading is weak, and weaker than first written.** The
criteria committed before the run said this result would support
specificity only and never sensitivity. That still holds and is still the
ceiling. But John ruled that even the specificity half is thin:

  "'not flagged' from probes at chance on every layer is weak evidence of
  specificity, since an instrument that locates nothing cannot cry wolf."

That is right, and the original draft of this section said the stack "did
not manufacture a false positive. It did not cry wolf." **That sentence is
withdrawn.** Crying wolf requires having found something to raise an alarm
about. An instrument returning chance at every layer never reached the
point where it could have flagged wrongly, so declining to flag is not
restraint and is barely evidence of anything. The honest statement is
narrower: **no false positive was produced, by an instrument that produced
no positive of any kind.**

What the result cannot show is whether the stack could find a structure
that *does* matter, because this checkpoint contains none to find. That
limit was committed before the number was seen and is unchanged.

**The sub-bin name stands.** The criteria split "not flagged" in two
before the run, and this landed on the worse half: **instrument failure to
locate**. "Recovers and correctly dismisses" would have meant the stack
located a decodable direction and correctly declined to call it
load-bearing. What happened instead is that the stack could not decode
own-agent identity **at all**, at any probed layer, in a model built with
a designated slot for exactly that. Chance is 0.25 and the best probe
returned 0.275.

## What this says about Experiment 1, correctly scoped

*Also amended 2026-09-16 on John's ruling.* The original draft said this
result "weakens any reading of Experiment 1's null that assumes the
instruments would have found a self-index had one been there", and that it
"moves in that direction rather than away from it". **That inference was
too broad and is withdrawn.** John's ruling:

  "that stack located a real structure (the router) on 2B and 8B models.
  This result says the stack is unvalidated at 30M; it does not by itself
  show Experiment 1's null was instrument blindness."
