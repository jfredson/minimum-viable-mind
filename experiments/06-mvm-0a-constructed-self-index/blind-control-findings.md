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
> DIAGNOSTIC ONLY. No rule is rewritten after the data.**
>
> That settles it, and it is the right call for a reason worth recording.
> I found the absolute-value hole *because* of what the data did, and a
> rule changed at that moment is not a pre-stated rule any more, however
> sound the correction looks. The discipline only works if the criteria
> that were committed are the criteria that are read. Anything else lets
> the result choose its own test.
>
> So: **the verdict of this run is NOT TESTABLE.** The signed reading is
> recorded, is not a verdict, and does not become one later. What the
> absolute-value form should be for any FUTURE run of this pipeline is a
> separate question, to be settled before that run rather than after it.

## The lesion behaves like a non-specific one

Whatever the blind search carved, its removal **improved** the battery
that depends on ownership and **damaged** a battery that does not, past
that battery's own locked threshold of 0.1172. The syntax control did not
move.

That is close to the inverse of a self-location signature. A structure
that indexes the act to its own center should degrade the primary battery
and leave the state battery alone. This did the opposite on both counts.

## What this says, given that ownership *is* load-bearing here

This is the point of the control. On this exact checkpoint, ownership is
measured to matter: zeroing the acting channel takes the primary battery
from 0.506 to 0.182, while the ownership-free batteries hold at 0.999 and
1.000, and across 120 content-blind ablations the worst reached 0.2758
against 1.515 for the authorship lesion.

So there is something here to find, and the localization stack did not
find it. It returned five probes below their nulls and a subspace whose
removal helps the action it was supposed to be carrying.

**Taken with the registered arm, the stack has now come up empty on both
checkpoints it has been pointed at**: once where there was nothing to find,
which was uninformative, and once where something is known to be there.
Only the second is evidence, and it is evidence of insensitivity at this
scale.

> **WITHDRAWN 2026-09-16 on John's ruling. The paragraph above stays as
> written; its last clause is the one withdrawn.** John: *"Withdraw
> 'evidence of insensitivity at small scale' for now... The result cannot
> yet distinguish an insensitive stack from a broken pipeline."*
>
> He is right that I claimed more than the run could carry, and he was
> right before the known-answer test existed to settle it. Two facts were
> ruled to sit beside the withdrawal, and both were measured.
>
> **FACT ONE: the five probes falling below their nulls is systematic,
> not chance scatter.** All five margins are negative: −0.75, −0.54,
> −0.96, −0.24 and −1.01 standard deviations. If the five were
> independent, all falling below their own null means would happen about
> **1 time in 32**. They are not independent: they read the same episodes
> at different depths, so they are positively correlated and the true
> probability is **higher** than 1 in 32. That figure is a floor on how
> surprising this is, not a p-value, and it is reported as one.
>
> **FACT TWO: the +0.052 movement is inside evaluation noise.** Measured
> rather than argued, twelve independent draws of the same evaluation on
> the same checkpoint at each sample size:
>
> | episodes | scored denominator | mean | sd | min | max | range |
> |---|---|---|---|---|---|---|
> | 400 | ~200 | 0.5621 | 0.0284 | 0.520 | 0.599 | **0.079** |
> | 800 | ~397 | 0.5663 | 0.0169 | 0.542 | 0.593 | **0.051** |
>
> The control ran at 400 episodes, where one standard deviation of pure
> evaluation noise is 0.0284. The movement under test is 0.052, which is
> **1.8 standard deviations** and sits well inside the observed range of
> 0.079. So the ablation's apparent effect on the ownership battery
> carries no information. The scored denominator is about half the episode
> count because the action is scored only where the model revises, which
> is why the noise is larger than the nominal sample size suggests.
>
> **A CORRECTION TO THE RULING'S PREMISE, at John's instruction, with his
> original wording kept.** The ruling as issued read: *"the ownership
> battery's baseline has read 0.506, 0.483, 0.4975 and 0.440 across
> evaluations, so +0.052 is inside evaluation noise."* John then wrote:
> *"Ruling 2's premise contained an error from the Cowork session: 0.483
> and 0.4975 are Gate 3 detector scores, not ownership-battery baselines.
> Note the correction beside the ruling, original wording kept. Your
> twelve-draw measurement supersedes the argument."* Those two numbers are
> areas under the curve from the Gate 3 fingerprint detector's two arms,
> where chance is 0.5 and the equivalence bound was [0.45, 0.55]. The
> conclusion is unaffected, because it now rests on the measurement rather
> than on the comparison.
>
> **AND A THING WORTH KNOWING, found while checking that premise.** The
> two genuine on-record readings, 0.506 and 0.440, are **not two
> independent draws**. Both come from the single default evaluation seed,
> 987654321, which reproduces them exactly at 800 and 400 episodes. Both
> also sit below all twelve fresh draws at their own sample size. So the
> programme's headline ownership number rests on one unlucky evaluation
> seed, and the checkpoint's typical score is nearer **0.566** than 0.506.
> That does not change any verdict — every drop is measured against its
> own baseline in the same run — but any write-up quoting 0.506 as the
> pilot's ownership score should quote the spread with it.
>
> **WHAT THE WITHDRAWAL LEAVES STANDING.** The probe result is the only
> signal this run carries, and it is "found nothing". The ablation result
> is noise. Whether "found nothing" means an insensitive stack or a broken
> pipeline was exactly John's open question, and the known-answer test he
> ordered in the same breath now answers the pipeline half: it passes at
> ceiling, accuracy 1.0 against a null of 0.1306, a margin of 32.9
> standard deviations (`known-answer-test-findings.md`). That test
> validates residual capture, position indexing, probe fitting and null
> construction. It does not exercise the ablation path, and it probes a
> different layer and position than the blind runs did. So the pipeline's
> shared machinery is sound and the claim stays withdrawn until something
> tests the rest.

## What a pass would and would not have shown, per John's ruling

John ruled that when this reported, the record must say what a pass does
and does not show. It did not pass, so this is written as the scoping that
*would* have applied, and it matters more now rather than less, because it
shows how generous the test was that the stack still failed.

**A pass would have shown:** sensitivity to an **input-side** signal whose
removal produces a measured drop of about **0.32** in raw battery points,
from 0.506 to 0.182. That is a large, deliberately constructed, single
channel.

**A pass would NOT have shown:**

- Sensitivity to **weaker** structure. Nothing here speaks to whether the
  stack could find something whose removal costs a tenth of that. The
  ground truth was chosen because it is the strongest signal the programme
  has, which is exactly what makes it a weak basis for generalising
  downward.
- Sensitivity to **purely internal** structure. The ground truth is the
  removal of an input channel, not of a structure the network built. A
  pass would show the stack can find something whose removal hurts the
  act; it would not establish that the thing found is a carried
  self-index rather than the input trace passed forward. That is red-team
  objection R1 and this control never addressed it.
- Anything registered. The control is **unregistered** and was proposed
  after the pilot result was known. A pass would have carried less weight
  than a registered result, and any write-up would have had to say so.

Since it failed rather than passed, the honest summary is narrower still:
the stack did not find the strongest, most deliberately constructed,
input-side ownership signal available to it, at 30M.

## Honest notes

- The baseline primary score here is **0.440**, against **0.506** at the
  pilot endpoint. The endpoint used 800 episodes and this used 400, so
  this is sampling variation on a different draw, not a discrepancy in the
  checkpoint. The checksum matches the ledger exactly.
- The probes read residual states at revision positions, which is the A3
  pipeline's registered choice. A different position choice might read
  differently, and nothing here tests that.
- The lock was honoured throughout. It supplied θ = 0.1777 on the primary
  battery and carries no threshold at all for the control battery, so the
  control battery is reported and never read for a verdict.
- This is one checkpoint and one seed. Seeds 1 and 2 are still training.
