# The control-battery decision — proposal for John, due 2026-10-04

*2026-09-17. **Advisory only; John adjudicates.** Decision-memo pattern:
constraint set, then what the audit changed, then candidates, then one
recommendation. Nothing here authorises spend or changes registered text.
Written after the seeds reported, as the roadmap specified.*

## The question

Three trained checkpoints. The ownership objective learns on all three and
its removal lesion is enormous. The control battery never learned on any
of them, so the registered clause comparing the two cannot be evaluated
anywhere. Does the programme open a registered Amendment A4 that makes the
control learn, or close A3 with partial discriminators and say so plainly?

## What is settled

| | pilot | seed 1 | seed 2 |
|---|---|---|---|
| primary, intact | 0.5683 | 0.5633 | 0.5738 |
| primary, channel zeroed | 0.1988 | 0.2015 | 0.1447 |
| corrected drop | 1.337 | 1.342 | 1.528 |
| control, intact | 0.2877 | 0.3057 | 0.3195 |

The primary result is not in doubt and is not marginal. The control's
failure is systematic rather than a seed lottery, which is what the wave
was run to find out.

## Four things the audit changed, and they matter more than the numbers

**1. The bar is higher than I have been saying, and I was wrong about it.**
The floor rule is not "the baseline must clear the ceiling." It is
`baseline − ceiling ≥ 0.10`. So the control needs **0.4227**, not 0.3227.
All three miss by 0.103 to 0.135, so no conclusion moves, but an A4
argument that merely clears 0.3227 would still leave the drop undefined.
My findings note said "below its own ceiling" and is corrected.

**2. The control's ceiling was never attack-verified.** The registration
says the ceilings are verified by the attack sweep. **The attack sweep
contains no control-battery code at all** — zero occurrences. It attacks
the primary battery only. The 0.3227 rests entirely on one reference
solver in the curriculum module.

**3. That reference solver is blind to the thing the question hands it.**
The control question **names** the agent it asks about. The solver that
sets the ceiling never uses that name; it enumerates the four agents'
successors and guesses among those not already visible. A solver that can
do ordinary name-keyed lookup answers correctly every time.

So 0.3227 is not a ceiling on the battery. It is the score of a solver
that cannot read names, and the battery's real ceiling is near 1.0.
**This is the deeper problem, and it cuts both ways.** It means the
control at 0.32 is far worse than it looked, since it is barely above a
solver that ignores half the question. It also means the metric's
denominator for this battery was never a meaningful quantity.

**4. The design warned about this and the warning was never acted on.**
The curriculum module's own documentation says the control's lookup
ceiling is **0.5**, not 0.3227, and says in terms that *"red-team pass 3
should weigh"* it *"since the H_generic-binding bin turns on the
difference between the two batteries' drops."* Red-team pass 3 ran. It did
not weigh this. The registered number and the module's own comment have
disagreed since before the first dollar was spent.

## Why the control plausibly failed, from the code

It is **not** unsupervised. Each episode carries three queries and one is
chosen per training row, so roughly **one row in three** carries a control
target, one token each. Against that, the primary battery has a dedicated
full-weight loss term of its own on the roughly half of rows that carry an
action. The control gets perhaps a third of one shared term, with two easy
queries soaking up most of it.

Three further asymmetries, all in the code:

- **The primary battery has a private route the control does not.** The
  acting channel marks the model's own earlier value positions directly.
  The control must bind a name to a value across turns by ordinary
  attention, with no such help.
- **The rendering was reversed for the primary battery's benefit.** The
  speaker's name was moved after the value to kill a name-reading shortcut
  on the primary battery. The consequence for the control, which must now
  attend backwards from a name to a value two tokens earlier, was never
  revisited.
- **The answer appears in no turn.** It must be retrieved and then
  transformed by the revision rule. Retrieval and arithmetic both, from
  one supervised token.

## A correction on the money, in the programme's favour

I wrote in the seeds findings that an A4 needing new runs "must make that
argument explicitly" against the single-amendment ceiling rule. **That was
misleading and is withdrawn here.** The rule bars a *raise* above $400. An
A4 that fits inside the existing ceiling is not a raise and needs no cap
amendment at all.

| envelope | spent | remaining |
|---|---|---|
| A2 ceiling | $215.7 | **$184.3** |
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
