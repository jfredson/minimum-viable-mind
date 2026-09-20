the marker in the question, finds that marker's turn for the queried item,
and applies the shared revision rule. The learned one was given only
ownership-blind features and found the same structure by itself.

Neither touches the model's own slot or the acting channel. A scan of the
code, with docstrings and comments stripped, enforces that.

## Why this kills the clause

The floor rule defines a battery's drop only when
`baseline − ceiling ≥ 0.10`.

With a ceiling of 1.0, a defined drop needs a baseline of **1.10**.
Accuracy cannot exceed 1.0. So the control battery's drop is undefined for
**every possible model**, including a hypothetical one scoring a perfect
1.0, which would give a denominator of exactly zero.

The registered signature requires the primary battery's drop **minus the
control's**. One of its two terms can never exist.

## The reason is not what we thought, and the correction matters

Until today the record said A3 could not return a positive **because the
control battery never learned**. That conclusion was right and the reason
was wrong.

The control's failure to learn is **beside the point**. A perfectly
learning control would have made no difference whatever. The clause was
unsatisfiable the day it was registered, months before any checkpoint
existed.

**This also moots the proposal I wrote this morning.** Both routes I
offered, extra supervision and a scaffolded intermediate question, aimed
at making the control learn. Neither would have fixed anything. I was
proposing to spend $27 to $39 on a repair to the wrong component, and I
would have recommended it had this measurement not been run first. John's
instruction to measure the ceiling before opening an amendment is what
caught it.

## The structural point, which generalises past A3

This is not a slip in one number. It follows from two registered choices
that are individually reasonable and jointly incoherent.

1. The control battery is **designed to be answerable without ownership**.
   That is its entire purpose: same binding demand, no self-reference.
2. The metric divides by the distance from baseline to the **best score an
   ownership-blind solver reaches**.

Any control that is fully determined by the visible episode and does not
require ownership has an ownership-blind ceiling of 1.0 by construction.
Divide by the distance to 1.0 and you divide by zero or less.

**So the ceiling-corrected metric and the concept of an ownership-free
control are incompatible by construction**, not by accident. Any future
design pairing them inherits this, which is why it is worth reporting
upstream rather than filing as an A3 defect.

Worth stating fairly: the ceiling denominator was itself a registered
revision, adopted because dividing by chance manufactured a spurious
differential of 0.035 between the two batteries. That was a real problem
and the fix was a real fix. It simply traded a small artifact for an
unsatisfiable clause, and nobody noticed because the control never got
close enough to its floor for anyone to check the arithmetic.

## What this does not change

**The primary result is untouched.** Its ceiling is 0.2921, the models
score about 0.57, so its drop is well defined and enormous, between 7.5
and 8.6 times the locked threshold. Nothing here bears on it.

**No verdict is reopened.** Every finding that said the comparison was
uncomputable remains correct. Only the explanation changes.

**The other batteries are fine.** The state battery's ceiling is 0.0676
against a baseline of 1.0. The problem is specific to a control designed
to be ownership-free.

## What it means for 4 October

The question is no longer whether to make the control learn. **It is
whether the clause can be repaired at all, and if so whether repairing it
is a metric change rather than a training change.**

That is a different decision from the one the proposal framed, and it
should be re-framed before the date. I am not proposing the repair here,
because a metric change after seeing which way it cuts is exactly the move
this programme forbids, and because John decides whether the line
continues at all.

**No spend. No registered text altered.** This measurement is itself
unregistered, and says so.


===== FILE: experiments/06-mvm-0a-constructed-self-index/ceiling-defect-2026-09-17.md =====

# REGISTERED DEFECT — the control battery's ceiling was never verified

*2026-09-17. **Registered on John's instruction, before any further
analysis**, and independent of how the control-battery decision goes on
4 October. Local, $0. Nothing in the registered text is altered; §4 of the
amendment carries a dated notice pointing here.*

John's instruction, quoted: *"Register the ceiling defect now, before any
further analysis. Include the 0.5 vs 0.3227 documentation mismatch and the
fact that the solver ignores the supplied name."*

## The defect in one sentence

The registered text says both battery ceilings were **verified by the
attack sweep**. Only the primary battery's was. The control battery's
ceiling has never been attacked, and the single solver that produced it
ignores the one piece of information the control question supplies.

## What the registration claims

Amendment A3, §4 of the registration revisions, "The ceilings are measured,
not asserted":

> **Registered:** **0.2921** for the primary battery and **0.3227** for the
> control, measured on the registered grammar and **verified by the attack
> sweep, whose best ownership-blind attack reached 0.3036 on 12,000
> episodes — one standard error from the analytic value.**

The 0.3036 figure is an attack on the **primary** battery, compared against
the primary's 0.2921. It says nothing about the control. The sentence
attaches one verification to two numbers.

## Evidence, each checkable

**1. The attack sweep contains no control-battery code at all.** Searching
`src/shortcut_sweep.py` for the control battery's name returns **zero**
occurrences. The module attacks the primary battery only. So the clause
"verified by the attack sweep" is false as applied to the control, and the
0.3227 rests entirely on one reference solver in `curriculum_a3.py`.

**2. That solver ignores the name the question supplies.** The control
question names the agent it asks about, in the form *"where did
&lt;marker&gt; assign &lt;item&gt; to next?"*. The reference solver in
`measured_ceilings` never reads that marker. It forms all four agents'
successors on the queried item, strikes any already visible as a revision,
and guesses uniformly among the rest. Its score is therefore the score of
a solver that **cannot read names**, averaging 0.3227 over candidate sets
of size four, three and two.

**3. So 0.3227 is not a ceiling on this battery.** Every turn renders the
speaker's marker in plain text, so a solver that can do ordinary
name-keyed lookup retrieves the named agent's value and applies the
revision rule to it. Such a solver answers correctly every time. The
control battery's real ownership-blind ceiling is therefore **near 1.0 and
currently unmeasured**, not 0.3227.

That is coherent with the battery's purpose rather than a contradiction of
it. The control was designed to carry the same binding demand **without
self-reference**, so knowing which agent you are is irrelevant to
answering it. A solver blind to ownership should do well on it. What went
wrong is that the number recorded as its ceiling came from a solver blind
to something else entirely.

**4. The documentation mismatch, which predates the first dollar.** The
curriculum module's own description of the control battery states a
different figure:

> *"Two of the item's four values are struck by the two revisions a solver
> can invert, so its lookup ceiling is **0.5** — higher than T_act's, which
> **red-team pass 3 should weigh**, since the H_generic-binding bin turns
> on the difference between the two batteries' drops."*

So the registered number is 0.3227 and the module says 0.5. The comment
also names the exact risk and assigns it to a specific review. **Red-team
pass 3 ran and did not weigh it.** Neither figure has ever been checked
against an adversary.

## What follows, and what does not

**This does not change any result.** The control battery scored 0.2877,
0.3057 and 0.3195 on the three checkpoints. Against a floor requirement of
ceiling plus 0.10, it fails at 0.3227 and fails by more at 0.5 and fails
by far more at a true ceiling near 1.0. **Every reading makes the control
less learned, not more.** No verdict moves.

**It does change what the number means.** The metric divides the drop by
the distance from baseline to ceiling. For the control that denominator
was never a meaningful quantity, so the registered differential clause
rested on a yardstick nobody had checked. That is worth knowing whether or
not the clause was ever computable.

**It is a defect in a registered instrument, not in a result.** Recording
it is not a correction to a finding. It is a correction to the
registration's own claim about how one of its numbers was established.

## Consequences John has already set

**If A4 opens, measuring the control's ceiling properly is a precondition
of the amendment** (John, 2026-09-17). An amendment built on an unverified
denominator would inherit this defect.

**If A3 closes**, this belongs in the write-up as a limitation of a
comparison that was never actually available, alongside the fact that the
comparison could not be computed anyway.

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

The record supports him. Experiment 1 did not come back empty-handed. Its
pipeline **found** a load-bearing structure and characterised it: the
registered reading is that the locatable residual is dialogue-state
routing infrastructure rather than the floor's self-binding. The router
control fired on its own pre-registered terms, and the ablations moved the
batteries by 0.219, 0.100 and 0.133. An instrument that locates a real
structure and correctly declines to call it a center is working, not
blind.

The scales are also nowhere near each other. Experiment 1 ran on a 2
billion parameter pilot substrate and a registered 8 billion parameter
run. This arm ran at 30 million, roughly two orders of magnitude smaller
and a different architecture besides.

So the correct scope is narrow: **the localization stack is unvalidated at
30M.** That is a real and reportable limitation of the A2 and A3 work,
which is where it applies. It is not evidence that Experiment 1's null was
an artifact of blind instruments, and this record should not be cited for
that claim. RT-12 named instrument blindness as the single finding that
might outweigh the headline; this result does not deliver it, and saying
otherwise would be reading a null at one scale as a verdict on a positive
result at another.

## The checkpoint, and why it is the strongest available case

The arm read the seed-0 full-architecture checkpoint. "Full" is the
register-bearing architecture; the twins are register-less. Its baseline
matches the registered lesion table exactly (T_sr 0.99, T_si 0.96,
T_sr_rev 0.84), which confirms identity without the arm ever having been
told where the register lives.

This is also the checkpoint that *binds* — one of only two in the five
that do. So the negative result is not an artifact of probing a model
with nothing going on. It is the most favourable case the register-
bearing set offers, and the stack still found nothing.

## Firewall, as registered

- Headline verdict committed 2026-08-19, before this arm existed.
- The pipeline never names any register internal; a self-check scans its
  own source against eleven forbidden names and refuses to run on a hit.
- Thresholds inherited, not chosen after seeing output.
- Both outcomes and the specificity-only limit committed before the run
  produced anything (`da0427f`, while the process was in flight).
- The three-standard-deviation bar is a **stated convention**, not a
  threshold inherited from Experiment 1, and was labelled as such in
  advance. The 0.25 is John's ruled Gate 0 band.

Worth stating plainly: a laxer bar would not have rescued this. The best
margin was 1.3 standard deviations, so the verdict is unchanged at two
standard deviations and unchanged at one and a half.

## What is still open, and what John ruled on 2026-09-16

Sensitivity is untested and cannot be tested on this checkpoint. Two
follow-ups were ruled, both local and free, both after this verdict was
committed:

1. **An unblinded probe of the register at its known location**, on this
   same checkpoint, for the same four-agent target with the same null and
   the same 3 sd bar. This separates two readings the blind arm cannot
   separate: a register that *holds* decodable own-agent identity the
   blind stack walked past, versus a register that is simply **empty**, in
   which case the arm had no valid target and "failure to locate" is the
   wrong description of what happened. Criteria pre-stated and committed
   before output, as with the blind arm. See
   `register-direct-probe-findings.md`.
2. **The companion positive control**, ruled **YES**: the same blind
   pipeline on the A3 pilot checkpoint, where zeroing the acting channel
   is measured load-bearing at 0.506 to 0.182. It stays **unregistered**
   and labelled so, under the same firewall, with criteria committed
   before output. See `blind-arm-positive-control-proposal.md` and its
   findings.

The order matters and was John's: the unblinded probe runs first, because
if the register turns out to be empty then this arm's "failure to locate"
was never a failure of the instrument at all.


===== FILE: experiments/06-mvm-0a-constructed-self-index/blind-control-findings.md =====

# Positive control for the blind arm — result

*2026-09-16. **UNREGISTERED**, ruled by John, criteria committed before
any output at `a3c5fbf`. Local, $0, inference only, gated on John's
threshold lock. Checkpoint verified by checksum against the ledger's
recorded A3 pilot (`f751228c…`).*

## Verdict by the letter of the pre-stated cells

**NOT TESTABLE.** The probe failed and the ablation reached θ, which is
the cell I created on the morning of the run when I resolved the overlap
in my own proposal. Had I not resolved it beforehand, this result would
have fallen in the gap between two bins.

But the number driving that verdict needs flagging, and it points the
other way.

## The probe found nothing, at any layer

| layer | accuracy | null mean | null sd | margin |
|---|---|---|---|---|
| 3 | 0.2350 | 0.2532 | 0.0243 | −0.75 sd |
| 4 | 0.2400 | 0.2529 | 0.0238 | −0.54 sd |
| 5 | 0.2275 | 0.2530 | 0.0266 | −0.96 sd |
| **7** | **0.2475** | 0.2543 | 0.0283 | **−0.24 sd** |
| 8 | 0.2250 | 0.2502 | 0.0249 | −1.01 sd |

Every probe sits **below** its own permutation null. Not near the bar and
short of it: below the null, at all five depths. Own-agent identity is not
linearly decodable from the residual stream at the probed positions on
this checkpoint.

The nulls here are healthy, spread 0.024 to 0.028, so the precondition I
added in advance is satisfied and the comparison means something.

## A second defect in my own pre-stated rule

The rule said the ablation "bites" when `|d_found| >= θ`. It does:
−0.3516 against θ = 0.1777. **But the sign is negative, and negative means
the ablation made the primary battery better.**

| battery | baseline | after ablation | direction | corrected drop | threshold |
|---|---|---|---|---|---|
| T_act (primary) | 0.440 | 0.492 | **improved** | −0.3516 | 0.1777 |
| T_state | 1.000 | 0.858 | damaged | 0.1523 | 0.1172 |
| T_syntax | 1.000 | 1.000 | unchanged | 0.0000 | 0.0 |
| T_other (control) | 0.292 | 0.292 | unchanged | not read for a verdict | none in the lock |

A sensitivity test asks whether removing the located structure
**degrades** the action. Taking the absolute value lets an improvement
count as a bite. That is wrong for this question, and it is the second
hole I have found in my own pre-stated criteria in one day. The first was
the zero-spread null in the register probe.

As before, I am not repairing the rule to change its output. The literal
verdict stands above. What follows is the reading under a signed rule,
reported beside it, for John to rule on.

**Under a signed rule the result is INSENSITIVE**: the probe failed and
the ablation did not degrade the primary battery. That is the cell I
pre-stated, in those words, as *"the outcome that would shift the honest
reading of Experiment 1's null toward instrument failure."* It cuts toward
the more consequential finding, not the more comfortable one, which is
why it needs saying plainly rather than leaving buried under a
not-testable label.

> **RULED 2026-09-16 (John). The literal pre-stated result, NOT TESTABLE,
> is authoritative. The signed-rule reading stays beside it as a
