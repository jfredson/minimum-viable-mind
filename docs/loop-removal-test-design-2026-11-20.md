# The loop removal test: a design on paper

*Version 0.1, written 2026-11-20 by a working session, on John's instruction of the same day ("Go
ahead with the version 0.1 design"). It turns the design note of the same date
(`docs/2026-11-20-loop-removal-design-note.md`) into a design in the form the split removal test
used (`docs/split-removal-test-design-2026-10-24.md`), and it borrows that design's outcome rules
wherever they fit. This is a design, not a registration. Nothing has been run, downloaded or
spent, and no choice in it is ruled. It has not yet had the inside review pass that every design
gets from a session that did not write it. The proposed experiment number is 10; no folder exists
yet.*

## 1. The question, and what one run can say

The three-hypotheses proposal of 2026-11-20 (`docs/2026-11-20-three-hypotheses-and-refocus-proposal.md`)
states hypothesis H1: experience needs contents held together in one shared workspace and updated
as input arrives. It predicts what removing that workspace does: **routine, practised output keeps
running, while flexible handling of anything new collapses.**

Thinking Machines Lab's variable-loop research model,
[TML-d24-varloop-research](https://thinkingmachines.ai/model-card/tml-d24-varloop-research/), runs
its middle layers several times for each word. On every pass after the first, those layers read a
"message" carrying their own result from the pass before. The message is the one place in the
model where the processing of a single word feeds back on itself before the model commits to that
word. This test asks whether that feedback does H1's job in this model.

It does so by keeping the model's full amount of computing and **replacing the message with one
that is not about the input in front of it**. It then measures whether the loss falls more on
problems the model must solve from rules given in the prompt than on practised routines, beyond
matched comparison removals.

**What a result here can and cannot say.**

- **The loop is not a candidate for experience.** The Sentient Horizons positions say that looping
  back is one way evolved brains reach deep integration, not what experience is (positions ledger
  entry 45, as quoted in the three-hypotheses proposal). The loop is a candidate for **the
  mechanism that does H1's job in this model**.
- **If the predicted pattern appears,** that is a fact about this loop in this model. It does not
  show that the model has experience.
- **If the message is replaced and the predicted pattern does not appear,** H1's prediction failed
  **for this placement in this model**, and that is reported as a result against the placement,
  not as a neutral "nothing" (section 7). It is not a result against H1 itself, because the model
  may do H1's job somewhere the loop does not reach, such as its ordinary attention across earlier
  words.
- **H1's second clause, that no self-model is needed, is not tested here.**

## 2. The model, and what is known about the loop

All of this comes from the makers' pages and from
[Goodfire's interpretability write-up](https://www.goodfire.com/research/interpreting-inkling-2-mini/)
(Goodfire is an interpretability lab that had early access to the weights), read 2026-11-20 and not
yet checked by this project. Goodfire describes Inkling 2 Mini, which has the same architecture as
the research model.

- **Layout.** 24 layers in four blocks of six. Block 1 runs once; blocks 2 and 3 (layers 7 to 18)
  run a chosen number of passes; block 4 runs once and produces the output. There is no single
  running record through the network: each block keeps a running sum of its own layers' outputs,
  and each layer reads a learned mix of the block sums available to it.
- **The message.** On passes 2 and onwards, every looped layer has four readers (for the three
  parts of attention and for the expert sublayer). Each reader builds its own message as a learned
  mix of the **two block sums from the previous pass**, those of block 2 and block 3. In Goodfire's
  measurements the readers take almost all of it from block 3.
- **How the message is mixed in.** The message does two things, not one. A small learned network
  looks at the current input and the message together and computes two settings from them: a
  "keep" setting that scales the current pass's own input, and a "gain" setting that scales the
  message before it is added. So the message both adds content and controls how much of the
  current input is kept. On the first pass there is no message.
- **A control signal.** Goodfire found a few coordinates in block 3's sum that take very large
  values at the end of every pass except the last (the largest is coordinate 2027 of 2304, at
  about 32 times the typical size). The next pass's readers use them to decide which block to read.
  Goodfire reads them as the model signalling "another pass follows".
- **Training.** The research model was trained at one to five passes in the ratio 1:2:6:2:1 for
  the later part of its middle stage of training, then at three passes only in its final stage.
  The model card warns it "may behave unpredictably at pass counts other than 3".
- **Size and machine.** One checkpoint of about 20 GB in the low-precision formats it was trained
  in. It needs at least 32 GB of graphics or shared memory. The Hugging Face page lists the
  Hugging Face software among the supported frameworks, which is the usual route for reading and
  changing activity inside a model while it runs. This Mac has 16 GB and cannot run it.

## 3. What is removed

The removals act on the **two previous-pass block sums that the message readers read**, on passes
2 and 3, at every position in the input. Acting there, rather than on each reader's message,
changes all 48 readers consistently, and it changes both what the message adds and the keep and
gain settings it controls.

**The main removal, in two methods.** The run keeps three passes, the number the model was trained
on last, so the amount of computing is unchanged.

- **(a) Swap.** The two block sums are replaced by those that a different item of the same kind
  produced, at the same position and on the same pass. The donor item is drawn at random from the
  same cell (section 5) among items at least as long as the recipient, with a seed fixed in the
  registration. The model gets a message of the right size and kind, but not about this input.
- **(b) Average.** The two block sums are replaced by their average over the neutral text, taken
  separately for each pass and each position up to the longest item. This follows experiment 01's
  mean-ablation, the method with the longest record in this project.

**The control coordinates are kept.** Before any removal, the rehearsal identifies the control
coordinates as those whose average size in block 3's sum, measured on neutral text at the end of
each pass, exceeds 10 times the typical coordinate. Coordinate 2027 is expected among them. In both
methods these coordinates keep their true values, so that the removal changes the message's content
and not the model's bookkeeping of how many passes are left. A secondary run swaps them too and is
reported, not used for any outcome.

**What "removed" means here, and why there is no separate check that it was.** The split removal
test needed a check that its target was really gone, because the model could rebuild who said what
from the role headers still in its input. Here the replacement is exact by construction: the
message the readers receive is computed only from another input, or from an average. The model can
still recompute on passes 2 and 3 what pass 1 found, because every pass starts again from block 1's
output. But recomputing from scratch is exactly what having no feedback means. If the model loses
nothing because it recomputes, the honest reading is that it did not need the feedback, which is a
result (outcome D), not a failed removal. The rehearsal reports, for description, how close the
final pass's block sums come to the unaltered run's under each method.

**Other conditions, which do not decide the outcome.**

- **Fewer passes: two, and one.** These remove the feedback and the computing together. They are
  reported with the same statistics as the main removal, measured against the unaltered run, and
  labelled as fewer passes.
- **Identity check.** The swap code is run with each item as its own donor. The outputs must match
  the unaltered run to within numerical rounding (largest difference in an answer's log-probability
  at most 0.01). If they do not, the hooks are wrong and nothing else is read.
- **Mixing bypassed.** On passes 2 and 3 the mixing step is skipped entirely, so each layer gets its
  input as it would on pass 1. Because each pass's own block sums start from zero and block 1's
  output is unchanged, the arithmetic says every pass then repeats pass 1, and the result must match
  the one-pass run to within the same rounding. If it does not, something other than the message
  differs between passes, and the design returns to John before anything else is read. Cutting only
  the gain, as the design note proposed, is dropped: the message would still steer the keep setting,
  so it would not be a clean cut.

## 4. The comparison removals

Every comparison is matched on **measured damage**, as in the split removal test: how far the
model's next-word predictions move on neutral text, measured as the average divergence between its
predictions before and after the removal. Each comparison must land within 20% of the main removal's
figure for the same method. Comparisons are selected by that rule alone, before any task is scored.

| Removal | What it stands for |
|---|---|
| **The message, replaced** (section 3, methods a and b) | The candidate: the loop's feedback |
| **Random, matched damage** | Random noise added to the same two block sums on passes 2 and 3, scaled until its damage matches. Twenty draws; their average is the comparison. |
| **Damage outside the loop, matched** | Random noise added to block 1's output, which runs once and is not part of the loop, scaled until its damage matches. Twenty draws. It is used only for the "not specific" check (section 6). |
| **Fewer passes** | Reported with the same statistics, against the unaltered run. Not used for any outcome (section 3). |

**The normal-range check.** It applies to the main removal and to every comparison. The neutral-text
perplexity (how surprised the model is by ordinary text) may rise by no more than the 95th percentile
of the rise across 20 random removals **of the same size**. Here, "same size" means random noise added
to the same two block sums with the same average length as the difference between the true sums and
the replacement ones. That draws on experiment 01's rule as the split design re-stated it (finding
RT-329 of its review): the bound is matched on size, not on damage, so that it is not circular. The
bound is derived in the rehearsal and fixed before any task is scored. A comparison that leaves the
range cannot serve as a comparison.

## 5. The tasks

**Scoring changes from the split design.** The split design scored a generated answer by exact
match. Here every item has a **fixed set of five candidate answers**, the right one and four wrong
ones built by a rule for that kind, and the model's answer is the candidate it gives the highest
probability to after the prompt. Chance is 0.20. The reason is mechanical: the swap needs a donor's
block sums at every position the recipient uses, and that is only possible when every position is
known in advance. It is also how Thinking Machines scored their chained-lookup task.

**No written reasoning.** The answer is scored directly after the prompt, with no reasoning text
before it, because H1 is about what happens inside one moment. If the model can write its working
out, it can route around a lost loop through the text. How to stop this model from writing
reasoning first, and what the chat template needs for that, is settled in the rehearsal (section 9).

**The cells that decide the outcome**, both single-turn and not about the model, built by the split
test's generators (`experiments/09-split-removal-test/src/batteries.py`) with the candidate sets
added:

- **R, routine:** one familiar step. The six kinds from the split test: sums, products, capitals,
  plurals, the next weekday, opposites.
- **P, prompt-rule problems:** a rule or symbol system invented for the item and stated in the
  prompt. The four kinds from the split test: an invented operator, a letter code, two rules applied
  to a list, and the next token on a ring. On the 2-billion-parameter bench model only the invented
  operator was answered reliably. This model is much larger, so the rehearsal checks again whether
  at least three kinds survive.

Each P item must pass two checks at baseline, as in the split design:
- **The rule is needed:** with the rule sentence removed, accuracy on that kind is no better than
  chance plus 0.10.
- **The rule is learned:** with the rule given, the item is answered right.

**Matched on confidence.** At baseline (three passes, nothing removed), an item is kept only if the
right candidate is chosen and given a probability of at least 0.9 among the five. R and P are then
matched on that probability in bins (0.90 to 0.95, and above 0.95), with a fixed seed, so that the
P items are not simply the harder ones.

**A positive check, not in the outcome:**
- **L, chained lookup:** the task Thinking Machines describe. Several lookup tables of invented
  entries are given, and the model must follow a chain of two to six lookups in its head, with five
  answer options. It is known to depend on the loop. **If the one-pass run does not lose at least
  0.15 on chains of four or more lookups compared with the three-pass run, the setup is wrong and the
  result is not testable.**

**Pilot and test are kept apart** as in the split test's authoring specification: content pools are
split in two halves, pilot items come from half A with seed 1, and test items come from half B with
a seed written in the registration and generated only after it. The split test used half A on the
bench model and never generated half B, so half B is unused.

**Sample size.** The analysis is paired: the same items are scored under every condition, and
differences are resampled by item. The number of items per cell is fixed in the rehearsal by a
committed simulation, as in the split design: the smallest number giving at least an 80% chance of
classifying a true gap of 0.20 as outcome A, with both methods. The provisional figure, carried over
from the split design, is about 120 items per cell.

## 6. The outcomes: every case lands in exactly one

These rules are the split design's (its section 5), with the template checks removed, because no
chat template is in play here. **δ = 0.10**, on the scale of the fraction of items lost. Intervals are
95%, from paired resampling of items (10,000 resamples, seed fixed in the registration).

For each method, on the R and P cells:
- **R**, the excess loss on routines: the main removal's loss minus the random comparison's;
- **P**, the excess loss on prompt-rule problems, computed the same way;
- **G = P − R**, the gap.

**Stage one: is the result readable?** It is **not testable** if:
- the identity check or the mixing-bypassed check fails (section 3); or
- the positive check on chained lookup fails (section 5); or
- the normal-range check fails for the main removal or for a needed comparison; or
- fewer than 10 of the 20 random draws can be matched on damage; or
- fewer than three P kinds survive the baseline checks.

The report says which.

**Stage two: the pattern.** Apply these in order; the first that applies decides.

1. **A. Selective loss on prompt-rule problems.** G is at least δ and its interval lies above zero;
   P's interval lies above zero; and R's interval has its upper end below δ.
2. **B. Selective loss on routines.** G is at most −δ and its interval lies below zero; R's interval
   lies above zero; and P's interval has its upper end below δ.
3. **C. General loss.** R and P both have intervals above zero.
4. **D. No excess loss.** R and P both have intervals whose upper ends are below δ.
5. **E. Unresolved.** Anything else.

**One check that applies only to A or B. Not specific:** if the damage-outside-the-loop comparison's
gap, computed like G against the random comparison, meets the same test, the outcome is renamed
**Not specific**. That would mean a loss of this shape follows from damage of this size anywhere,
not from losing the feedback. C, D and E are never renamed.

**Each P kind is reported separately, and the outcome is also read with each kind left out in
turn**, so that a loss in one kind is not read as a loss across the board.

**Combining the two methods.** The outcome holds if the swap and the average land in the same one.
If they differ, the result is "methods disagree", reported with both and read as "could not decide".

**Combining the two models** (section 8). Each model is reported on its own; no pooled outcome.

## 7. What each outcome means, and the words it may be reported in

Every summary, in `STATUS.md`, on the site and in public, uses the sentence below and keeps both
conditions: "both methods agree" and "beyond matched comparisons".

| Outcome | The sentence it is reported in | What it means for H1's prediction |
|---|---|---|
| **A** | "In [model], replacing the loop's message with one not about the input cost more on problems solved from rules in the prompt than on routines, beyond matched comparisons, with both methods agreeing." | **The prediction held for this placement** in this model. It does not show experience. |
| **B** | "...cost more on routines than on prompt-rule problems..." | **The prediction failed for this placement** in this model. |
| **C** | "...cost both alike, beyond matched comparisons..." | **The prediction failed for this placement.** The feedback behaves like an essential part, which shows nothing selective. |
| **D** | "...cost neither routines nor prompt-rule problems more than matched comparisons..." | **The prediction failed for this placement.** The model does not need the feedback to do either kind of task. It is not reported as "the model has no workspace". |
| **E**, methods disagree, not testable, not specific | Reported under its name, with the reason. | **No reading.** Never reported as the prediction failing. |

**How the fewer-passes runs are read beside the main result.** They are descriptive, but one
contrast is worth stating in advance. If the one-pass run shows a large loss and the main removal
shows outcome D, then the loop's value in this model is the extra computing, not the feedback. That
sentence is allowed in the report; nothing stronger is.

**What would count against H1 itself.** Not this test alone. It would need independent evidence
that the loop is this model's shared workspace, and then outcome B, C or D. No such evidence exists
yet, and this design does not claim any.

## 8. The models, and what it would cost

- **Main model:** TML-d24-varloop-research. Every condition runs on it.
- **Second model, proposed:** Inkling 2 Mini, which always runs three passes. Only the main removal,
  its comparisons and the identity check run on it, since it has no one- or two-pass setting. The
  makers caution against comparing the two models directly, because their later training differs,
  so each is reported on its own. Both come from one maker and one family, so a result on both is
  not the "two models of different families" the split design required before reporting a candidate
  as failing. The design says so in every report.
- **No bench model on this Mac.** There is no small looped model in this project's hands, and this
  Mac has 16 GB of memory. The rehearsal and the run both need a rented machine with an NVIDIA card
  of at least 32 GB from the newest generation, which handles the model's native number formats
  (the model card names the RTX 5090 and the RTX PRO 6000 Blackwell). Under the standing rule, heavy
  runs go to RunPod.
- **What the work amounts to.** Every condition is a forward pass over a prompt and its five
  candidates, with no long generation. With about 360 items across the three cells, 200 neutral
  passages and roughly 60 conditions (including the 20 random draws, the 20 normal-range draws and
  the damage matching), that is on the order of 100,000 short forward passes per model. That is
  likely a few hours on one card. **No price has been looked up.** An estimate and a ceiling go to
  John before anything is rented, as with every spend.
- **Reused code:** the split test's battery generators, and the paired-resampling analysis from the
  split design. New code covers the loop hooks, the candidate sets, the chained-lookup generator and
  the damage matching on block sums.

## 9. Order of work

1. **The inside review pass** of this design by a session that did not write it, as the split design
   had. $0.
2. **John rules** on the choices in section 10, and on whether this test goes ahead at all, given
   the tracker of theories ruled on 2026-11-20 and the hibernation from 2027-01-04. $0.
3. **The battery specification, committed before any item:** candidate sets for every kind, the
   chained-lookup generator, and the pilot set generated with seed 1. $0, on this Mac.
4. **The rehearsal, on a rented machine, pilot items only, on John's go with a ceiling.** In order:
   load the model and confirm the hooks can read and replace the block sums; settle how to suppress
   written reasoning; the identity check; the mixing-bypassed check; the positive check on chained
   lookup; locate the control coordinates; the baseline checks and matching; derive the normal-range
   bound; match the comparisons on damage; commit the sample-size simulation. **If the identity
   check, the mixing-bypassed check or the positive check fails, the design returns to John before
   any registration.**
5. **Registration text**, through the inside and outside review passes (Gate A), then the
   registration commit.
6. **The registered run**, on John's go, with a ceiling.
7. **The findings**, through the interpretation review (Gate B).

Steps 1 to 3 cost nothing and can be done before the hibernation. When steps 4 onwards happen is
John's call.

## 10. Choices for John

1. **Score by the five candidates' probabilities, not by a generated answer** (section 5). The swap
   needs every position known in advance. Recommended, since otherwise the main removal cannot be
   run.
2. **Score with no written reasoning only** (section 5). Recommended, because H1 is about one moment
   and written reasoning lets the model route around the loop. A run that allows reasoning could be
   added later as a separate, descriptive condition.
3. **Inkling 2 Mini as a second model, main removal only** (section 8). Recommended, at the cost of a
   second download and roughly a third more machine time.
4. **Keep the control coordinates at their true values in the main removal** (section 3), with a
   secondary run swapping them. Recommended, so that the test reads the message's content and not
   the model's count of passes.

## Sources read for this design (all on 2026-11-20)

- Thinking Machines Lab,
  [Introducing Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/).
- Thinking Machines Lab,
  [TML-d24-varloop-research model card](https://thinkingmachines.ai/model-card/tml-d24-varloop-research/),
  and its [Hugging Face page](https://huggingface.co/thinkingmachines/TML-d24-varloop-research).
- Goodfire,
  [Interpreting Inkling 2 Mini](https://www.goodfire.com/research/interpreting-inkling-2-mini/),
  including its appendix on the architecture.
- This project: `docs/2026-11-20-loop-removal-design-note.md`,
  `docs/2026-11-20-three-hypotheses-and-refocus-proposal.md`,
  `docs/split-removal-test-design-2026-10-24.md` (sections 2 to 6),
  `experiments/09-split-removal-test/battery-authoring-spec.md`, and
  `experiments/09-split-removal-test/rehearsal/phase1-findings-2026-10-24.md` (the baseline checks
  on prompt-rule kinds).
