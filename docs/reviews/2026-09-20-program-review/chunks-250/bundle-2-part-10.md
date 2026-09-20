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
excluded, and a null from a linear probe is weak evidence about a
non-linear representation.

It also does not touch red-team objection R1, and it **changes no
registered result**: the blind arm's not-flagged outcome, the 2026-09-16
not-testable verdict and the signed sensitivity rule all stand exactly as
recorded.

**What it is not evidence for.** It is not evidence that these models
have no self-index, and it should not be written up as though it were.
The honest statement is narrower and duller: a linear difference of
averages, at the positions and layers we chose, does not find one.

## Where this leaves the line of work

This was the last run in this line, and it ends on a clean negative with
working controls, which is a better place to stop than the three
uninformative nulls that preceded it.

What the sequence established, in order: the target every earlier probe
used could not be recovered in principle; with a well-posed target and
real power the registered probe position is empty; and now, the rest of
the episode is empty too under the same read. Each of those is a fact
about the instrument and the position rather than about the models, and
the write-up should say so in those terms.

The open questions that a future session would have to take up — a
non-linear read, a distributed read across positions, and the unexplained
gap in how legible the marker token is between checkpoints — each need
their own committed method file. None of them is started here.

## Record

- Outputs: `a3-gates/powered_position_sweep_a3_a3_30m_seed{0,1,2}.json`
  and `a3-gates/powered_position_sweep_a3_summary.json`. Fresh files,
  nothing overwritten.
- Method committed before output: `powered-position-sweep-method.md`
  (`68f7708`).
- Implementation: `src/powered_position_sweep_a3.py`.
- The vectorised scorer was verified against the original before each
  run reported: differences exactly 0.0 on accuracy and separation, on
  both the noise and planted-signal cases, on all three checkpoints.
- 4,000 episodes, 1,000 draws, four folds, layers 3/4/5/7/8, three
  checkpoints run as parallel processes. No spend.
- Gated on the known-answer test, which passes. Not gated on the
  threshold lock, and the method file says why.


===== FILE: experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings.md =====

# The fitted linear read at all eleven positions — findings

*2026-09-20 (Pacific). **UNREGISTERED**, diagnostic only. No verdict is
read and no cell here feeds one. Local, inference only, no training, no
network, $0 [C1/C2]. Method committed in
`fitted-position-sweep-method.md` at commit `f84db43`, together with
`src/fitted_position_sweep_a3.py`, **before either produced any output**.
The cells, the bar and the instrument check were fixed while nobody knew
