
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
