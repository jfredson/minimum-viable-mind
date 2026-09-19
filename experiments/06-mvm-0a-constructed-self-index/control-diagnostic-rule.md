# Control-battery diagnostic — decision rule, registered before running

*2026-09-17. **Written and committed BEFORE the diagnostic runs**, on
John's instruction. Unregistered diagnostic on existing checkpoints.
Local, $0, no spend. **Not yet run. Awaiting John's go.***

John's instruction, quoted: *"Write and register the diagnostic's decision
rule before running it: for each of the three failure causes (no name
retrieval, retrieval without rule application, reversed word order
defeating retrieval), state which outcome means open A4, which means close
A3, and what result would be ambiguous. Show me the rule before you run
anything."*

## The design problem, and how the rule avoids it

The obvious diagnostic is to ask the models a simpler question, such as a
plain lookup with no rule step. **That would not work.** The models were
trained on exactly three question forms and a plain lookup is not one of
them. A failure on a new form confounds *cannot retrieve* with *has never
seen this question*, and the confound is not separable after the fact.

So the diagnostic asks **no new question**. It uses the control question
the models were trained on, unchanged, and reads their existing answer
distribution against **different targets**. The model's output is already a
distribution over the eight slots. What varies is which slot we ask
whether it chose.

## What is computed

For each scored episode, with `o` the queried agent and `x` the queried
item:

- `v` = the queried agent's own value on that item.
- `t` = `successor(v)` — **the registered correct answer.**
- `v_a`, `t_a` = the same two quantities for each *other* agent `a`.

Let `p` be the model's predicted slot. Every episode falls in exactly one
cell, tested in this order so the cells are disjoint and exhaustive:

| cell | condition | reads as |
|---|---|---|
| **CORRECT** | `p = t` | the registered score |
| **UNTRANSFORMED** | `p = v` | right agent retrieved, rule not applied |
| **WRONG-AGENT-TRANSFORMED** | `p = t_a`, some `a ≠ o` | rule applied, bound to the wrong name |
| **WRONG-AGENT-RAW** | `p = v_a`, some `a ≠ o` | wrong name, no rule either |
| **OFF-STRUCTURE** | none of the above | unrelated to the item's values |

Those five cells map onto John's three failure causes: UNTRANSFORMED is
*retrieval without rule application*, WRONG-AGENT-TRANSFORMED is the
signature of *name binding failing* which is what reversed word order
would produce, and OFF-STRUCTURE is *no name retrieval* in the strongest
form, no engagement with the item's value structure at all.

**The null.** Permute which agent is queried and recompute every cell.
That gives the rate each cell reaches by coincidence, given the item's
value structure, without any real retrieval. Same label-permutation
construction used throughout this programme, and the same stated
convention of three standard deviations.

**Precondition, carried forward from the two rule defects found this
week.** If the permutation null has zero spread, or a cell's rate exactly
equals what a constant predictor gives, **no bin is assigned** and the run
reports DEGENERATE. A vacuous comparison is not a result.

## The decision rule

**OPEN A4 BY THE SUPERVISION ROUTE.** UNTRANSFORMED clears its null by
three standard deviations **and** exceeds CORRECT.

> Reads: the models find the right agent's value and fail only to apply
> the revision rule to it. Name binding works. The missing piece is the
> transform, which is what more supervision on this battery would train.
> This is the cheap route, three retrained seeds at $27 to $39.

**OPEN A4 BY THE SCAFFOLDING ROUTE.** WRONG-AGENT-TRANSFORMED clears its
null by three standard deviations **and** exceeds UNTRANSFORMED.

> Reads: the models apply the rule correctly but to the wrong agent's
> value. The transform is learned; the **binding by name** is not. That is
> the signature the reversed word order predicts, since the marker sits
> after the value it identifies. More supervision on the same rendering
> would be training against the grammar rather than with it, so the honest
> route is the scaffolded intermediate question, not extra weight.

**CLOSE A3.** OFF-STRUCTURE dominates **and** neither UNTRANSFORMED nor
WRONG-AGENT-TRANSFORMED clears its null.

> Reads: the answers bear no relation to the item's values at all. The
> models learned nothing about the question, not a partial piece of it.
> That is the case the registration already fences as *"unlearnable at
> this scale under this curriculum"*, and an amendment would be betting
> against the fence.

**AMBIGUOUS, and it decides nothing.** Any other pattern. Explicitly
including: both UNTRANSFORMED and WRONG-AGENT-TRANSFORMED clearing their
nulls, no cell clearing its null while OFF-STRUCTURE does not dominate,
or a degenerate null.

> On this outcome the diagnostic has failed to separate the causes and
> **must not be reported as pointing anywhere.** The October decision then
> rests on the evidence already in hand, which is that the control fails
> on all three seeds and its ceiling was never verified.

No cell is added after the fact. A result fitting none of these is
reported as fitting none.

## What this diagnostic cannot do, stated in advance

**It distinguishes failure modes, not their causes.** If UNTRANSFORMED
dominates, that tells us the transform is the missing step. It does not
prove that under-supervision is why, and it does not guarantee that more
supervision fixes it. The rule above says such a result *opens* A4, not
that A4 will succeed.

**It is unregistered and post hoc.** These checkpoints have already been
read. The diagnostic was designed after seeing that the control failed, so
it carries less weight than a pre-registered test and any write-up must
say so.

**It cannot rescue the comparison.** Whatever it shows, the registered
differential clause remains uncomputable on all three checkpoints, and
this changes nothing about that.

**It does not measure the ceiling.** That is a separate precondition John
set for any amendment, and it is not attempted here.

## Cost and authorisation

Local inference on checkpoints already held. **No spend, no network, no
new runs.** Nothing here authorises an amendment; it informs a decision
John makes on 4 October.

**Status: not run.** The rule is committed first, as instructed, and the
diagnostic waits on John's go.
