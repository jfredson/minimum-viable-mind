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


===== FILE: experiments/06-mvm-0a-constructed-self-index/powered-position-sweep-findings.md =====

# Powered eleven-position sweep — result

*2026-09-20. **UNREGISTERED**, diagnostic only. No verdict is read and
nothing here reopens one. Method and code committed before any output at
`68f7708`. Local, inference only, no training, no network, $0. Three
checkpoints verified by checksum.*

## The result

**CARRIED NOWHERE, on both arms.**

Across eleven positions, five layers, two well-posed targets and three
checkpoints — **270 testable tests** — **not one reached even three
standard deviations**, let alone the family-adjusted bar of 3.56. The
largest margin anywhere was **+2.73**, the smallest **−2.59**, and the
mean across all 270 was **−0.085**. Zero marginal clearances. Zero robust
clearances.

The only things that cleared in the entire sweep were the positive
controls, which are the positions where the answer is the input token.

**Which positions clear: none.** That was the question, and that is the
answer.

## Every position, best margin across the five layers

Margins in standard deviations of each test's own 1,000-draw permutation
null. The cells turn on 3.56; three standard deviations is shown for
continuity with earlier runs.

### Arm 1 — the model's own marker word

| position | pilot | seed 1 | seed 2 | |
|---|---|---|---|---|
| `own_assign_1_value` | +0.60 | +0.03 | +0.36 | *negative control* |
| `own_assign_2_value` | +1.16 | +0.42 | +0.64 | |
| `own_revision_decision` | −0.02 | −0.26 | −0.33 | *the registered anchor* |
| `own_revision_value` | +0.55 | +1.36 | +1.78 | |
| `own_revision_by` | +0.12 | +0.06 | +1.51 | |
| `own_revision_marker` | **+159.08** | **+20.66** | **+29.45** | *positive control* |
| `before_own_revision_turn` | +0.92 | +0.97 | +0.83 | |
| `other_revision_decision` | +0.43 | −0.04 | +0.63 | |
| `other_revision_value` | −0.03 | **+2.73** | +0.04 | |
| `query_answer_decision` | +0.83 | +1.00 | +0.97 | |
| `query_answer_value` | +0.60 | +1.96 | +0.20 | |

### Arm 2 — the register index

| position | pilot | seed 1 | seed 2 | |
|---|---|---|---|---|
| `own_assign_1_value` | +0.76 | +0.74 | −0.71 | *negative control* |
| `own_assign_2_value` | −0.42 | +0.56 | +1.25 | |
| `own_revision_decision` | +0.49 | +0.34 | +0.22 | *the registered anchor* |
| `own_revision_value` | +0.46 | +1.68 | −0.08 | |
| `own_revision_by` | +0.60 | +1.67 | +0.14 | |
| `own_revision_marker` | **+7.40** | +2.72 | **+5.54** | *positive control* |
| `before_own_revision_turn` | +1.51 | +0.48 | +1.10 | |
| `other_revision_decision` | +1.06 | −0.12 | +0.22 | |
| `other_revision_value` | +0.94 | +1.17 | +1.07 | |
| `query_answer_decision` | −0.21 | −0.14 | +0.34 | |
| `query_answer_value` | +1.36 | +0.28 | +1.42 | |

## Both controls behaved, which is what lets the null be read

**The positive control holds on all three checkpoints.** The marker word
read where it *is* the input token clears at +159, +21 and +29 standard
deviations, with no shuffled draw out of 1,000 beating it. The read
works everywhere it is applied. The register index also clears at that
position on the pilot (+7.40) and seed 2 (+5.54), reaching +2.72 on seed
1; the control that governs both arms is the marker word, and it holds
without qualification.

**The negative control shows no leak.** At the value token of the model's
first own turn, where its own marker has not yet appeared anywhere in the
episode and neither target is determinable, the margins are +0.60, +0.03
and +0.36 for the marker word and +0.76, +0.74 and −0.71 for the register
index. Nothing clears.

That second result is worth its own sentence, because it was the outcome
that would have undermined everything else. The acting channel injects at
exactly that token, and had it been leaking the model's own identity
there, every other position in the sweep would have been in doubt. It is
not. **The channel does not carry the marker identity into that
position**, which is a small positive finding in its own right and the
reason the other 270 numbers can be taken at face value.

## The anchor reproduces the previous run exactly

The registered position reads −0.02, −0.26 and −0.33 in the marker-word
arm — identical to the powered anchor test of the previous run, on the
same episodes with the same seeds. The sweep widened the measurement from
two positions to eleven and did not perturb the one number that was
already known. That is the consistency check it should be expected to
pass, and it passed.

## The family bar: the right call, and moot in the event

Setting it was not a formality. With 270 discovery tests, leaving the bar
at three standard deviations would have given a **30.6 per cent** chance
of a false clearance somewhere — for a sweep whose entire question is
"does anything clear anywhere", that is the error that would have
manufactured a finding. The bar was raised to 3.56 before the run.

In the event it made no difference: nothing reached 3.0 either. The
distinction between the two bars never had to be exercised, and the
honesty note attached to it in the method file — that 1,000 draws resolve
only to p < 0.001, or about 3.09 standard deviations, and so cannot on
their own certify a family-safe clearance — never had to be called on.
Both are recorded because they were committed in advance and would have
governed a different outcome.

## What this settles, and what it does not

**Settles.** Combined with the anchor result, the linear-read line of
attack on these checkpoints is closed. Own-agent identity — in either of
the two forms the grammar makes well-posed — is not linearly recoverable
by a difference of averages at any of eleven positions across the
episode, at any of five layers, on any of three checkpoints, except at
the one position where it is present as an input token. The instrument
demonstrably works: at that position it reads the answer at 159 standard
deviations.

**Does not settle.** It reads one statistic, linearly, at eleven
positions out of an episode of seventy-one tokens. Identity could be
carried non-linearly. It could be distributed across positions rather
than resident at any one of them, which a per-position read cannot see by
construction. It could sit at a position not on the list. None of that is
