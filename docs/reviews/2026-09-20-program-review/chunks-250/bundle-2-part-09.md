
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
