# The loop removal test: a design on paper

*Version 0.2, written 2026-11-20 on John's instruction ("Yes, write 0.2"). It answers the inside
review pass of version 0.1 (`docs/reviews/2026-11-20-loop-removal-test-design-gate-c-tier1-claude-code.md`,
red-team findings RT-335 to RT-357). That pass found two fatal problems, fourteen serious ones and
seven worth noting, and its verdict was not to register version 0.1 as drafted. The change log at the
end says how each finding is answered. The fixes are the author's. Under the review protocol they are
owed a closure check by a session that did not write them, and the two fatal findings (RT-335 and
RT-345) must be closed by that check before John rules on anything that rests on them. Version 0.1 is
commit 4f68df5.*

*This is a design, not a registration. Nothing has been run, downloaded or spent, and no choice in it
is ruled. The proposed experiment number is 10; no folder exists yet. It grew from the design note of
the same date (`docs/2026-11-20-loop-removal-design-note.md`).*

## 1. The question, and what one run can say

The three-hypotheses proposal of 2026-11-20 (`docs/2026-11-20-three-hypotheses-and-refocus-proposal.md`)
states hypothesis H1: experience needs contents held together in one shared workspace and updated as
input arrives. It predicts what removing that workspace does: **routine, practised output keeps running,
while flexible handling of anything new collapses.**

Thinking Machines Lab's variable-loop research model,
[TML-d24-varloop-research](https://thinkingmachines.ai/model-card/tml-d24-varloop-research/), runs its
middle layers several times for each word. On every pass after the first, those layers read a "message"
built from their own results on the pass before. The message is the one place in the model where the
processing of a single word feeds back on itself before the model commits to that word.

This test keeps the model's three passes and **replaces the message with one built from other inputs**.
It then measures whether the loss falls more on problems the model must solve from a rule given in the
prompt than on routine questions of the same length and layout, beyond matched comparison removals.

**What a result here can and cannot say.**

- **The loop is not a candidate for experience.** The Sentient Horizons positions say that looping back
  is one way evolved brains reach deep integration, not what experience is (positions ledger entry 45, as
  quoted in the three-hypotheses proposal). The loop is a candidate for **one part of the mechanism that
  does H1's job in this model**.
- **The loop is narrower than a shared workspace** (RT-356). It works on one word at a time. The
  integration across words, done by ordinary attention, is untouched by this removal. So the most a result
  can show is whether the feedback within each word is part of how this model does H1's job.
- **If the predicted pattern appears,** that is a fact about this loop in this model. It does not show
  that the model has experience, or that its workspace was found.
- **If the message is replaced, the replacement is shown to bite, and the predicted pattern does not
  appear,** H1's prediction failed **for this placement in this model** (section 7). That is a result
  against the placement, not against H1 itself, because the model may do H1's job where the loop does not
  reach.
- **This test cannot separate feedback from computing** (RT-353). Section 3 shows that a pass without the
  message repeats the pass before, so in this model extra passes add nothing without a message. What the
  test compares is a message about this input against a message about other inputs.
- **H1's second clause, that no self-model is needed, is not tested here.**

## 2. The model, and what is known about the loop

All of this comes from the makers' pages and from
[Goodfire's interpretability write-up](https://www.goodfire.com/research/interpreting-inkling-2-mini/)
(Goodfire is an interpretability lab that had early access to the weights), read 2026-11-20 and not yet
checked by this project.

**Which model Goodfire describes** (RT-355). Goodfire studied Inkling 2 Mini, not the research model. The
research model's card calls it "a variable-looped counterpart to Inkling 2 Mini" that shares its
pretraining and the first stage of its middle training, and says their later training differs. No page
says the two are built the same way in every detail. Every architectural fact below is therefore checked
on the research model's own code in the first step of the rehearsal (section 9, step 4a), before anything
rests on it.

- **Layout.** 24 layers in four blocks of six. Block 1 runs once; blocks 2 and 3 (layers 7 to 18) run a
  chosen number of passes; block 4 runs once and produces the output. There is no single running record
  through the network. Each block keeps a running sum of its own layers' outputs, and each layer reads a
  learned mix of the block sums available to it.
- **The message.** On passes 2 and onwards, every looped layer has four readers, one each for the three
  inputs of attention and one for the expert sublayer, so 48 in all. Each reader builds its own message as
  a learned mix of **the two block sums from the previous pass**, those of block 2 and block 3. Goodfire
  says the model "almost always reads from block 3" on later passes, without giving a figure.
- **How the message is mixed in.** The message does two things. The current input and the message,
  each normalised, are passed together through two linear maps and a tanh, which gives a "keep" setting
  between 0 and 2 that scales the current pass's own input and a "gain" setting between −1 and 1 that
  scales the message before it is added. So the message both adds content and controls how much of the
  current input is kept. Goodfire describes this step only for passes 2 and onwards. Whether pass 1 skips
  it entirely is confirmed in the code (step 4a).
- **A pass-counting signal.** Goodfire found a few coordinates in block 3's normalised sum that take very
  large values at the end of every pass except the last. The largest, coordinate 2027 of 2304, averages
  about 32 times the size a coordinate would have if every coordinate were equal, and carries about 46% of
  the sum's squared size. Goodfire found that the readers of the first block-3 layer on pass 2 lean on it
  to decide which block to read, and reads it as the model signalling "another pass follows".
- **Training.** The research model was trained at one to five passes in the ratio 1:2:6:2:1 for the later
  part of its middle training, then at three passes only in its final stage. The card warns it "may behave
  unpredictably at pass counts other than 3".
- **Size and machine.** One checkpoint of about 20 GB, which the card says is the precision the model was
  trained in. It needs at least 32 GB of graphics or shared memory. The Hugging Face page lists the Hugging
  Face software among the supported frameworks. Its sample code, though, uses a loading class for a
  different kind of model, so nothing shows yet that the model's insides can be read and changed while it
  runs (RT-337). This Mac has 16 GB and cannot run it.

## 3. What is removed

The removals act on **the two previous-pass block sums that the message readers read**, on passes 2 and 3,
at every position the item uses, including the positions of the candidate answers (section 5). Acting
there, rather than on each reader's message, changes all 48 readers consistently. It changes both what the
message adds and the keep and gain settings the message controls.

**The main removal, in two methods.** The run keeps three passes, the number the model was trained on
last.

- **(a) Swap.** The two block sums are replaced by those that a different item of **the same kind and the
  same cell** produced, at the same position and on the same pass, taken from the donor's unaltered run
  (RT-352). The donor's run uses its own prompt and its own right answer, so that its sums exist at the
  positions of the recipient's candidates (RT-336). Donors are at least as long as the recipient's prompt
  plus its longest candidate. **Each item gets five donors**, drawn at random with a seed fixed in the
  registration, and the item's score under the swap is the average over the five, so that the luck of the
  donor draw is inside the intervals (RT-352). A donor's right answer is never one of the recipient's
  candidates (RT-346).
- **(b) Average.** The two block sums are replaced by their average over **a new neutral set**, taken
  separately for each pass and each layer source but **not for each position** (RT-335). Positions inside
  the fixed chat template are averaged separately by template token, so that template positions get a
  template average. The new neutral set is ordinary prose, given in the same chat template as the items,
  with passages as long as the longest items (section 5). Averaging over positions rather than at each
  position is what experiment 01's mean-ablation did in effect, and it makes the method computable at any
  length.

**Nothing is kept at its true value** (RT-348). Version 0.1 kept the pass-counting coordinates at their
true values. The review showed that this keeps close to half of the message's normalised size, and with
it much of the choice of block and the keep and gain settings. It is not needed. A donor also ran three
passes, so its sums carry the same "another pass follows" signal on the same pass. The average is taken
for each pass, so it carries the average signal for that pass. Both methods therefore keep the model's
count of passes without leaking anything from the recipient. The rehearsal reports, for description:
- how much the pass-counting coordinates vary from item to item;
- what share of the message's normalised size the swap changes;
- how far it moves the keep and gain settings.

**The swap's size is measured for every item** (RT-345). For each item and method, the **swap size** is the
total distance, over all changed positions and both passes, between the true normalised block sums and the
replacement ones. Section 4 uses it to scale the comparisons item by item, and section 5 uses it to check
that the two cells received the same dose.

**What "removed" means here.** The replacement is exact by construction: the readers receive sums computed
only from other inputs, or from an average. The model can still recompute on passes 2 and 3 what pass 1
found, because every pass starts again from block 1's output. Whether the replacement takes away what the
loop supplies is not assumed: it is checked on the one task known to need the loop (the "bites" check,
section 5). If the replacement does not bite there, no null result is read (section 6).

**Other conditions, which do not decide the outcome.**

- **Fewer passes: two, and one.** These remove the message and the extra passes together. They are
  reported with the same statistics as the main removal, measured against the unaltered run, and labelled
  as fewer passes.
- **The noise floor** (RT-342). Two unaltered runs of the same items are compared first. Mixture-of-experts
  routing and 4-bit arithmetic may make them differ slightly. The **tolerance** for the next two checks is
  the larger of 0.01 and three times the largest difference between those two runs in any answer's
  log-probability.
- **The identity check.** The swap code is run with each item as its own donor. The outputs must match the
  unaltered run within the tolerance. If they do not, the hooks are wrong, and the design returns to John.
- **The bypass check** (RT-342). On passes 2 and 3 the code does exactly what it does on pass 1, whatever
  that turns out to be in the research model's code. Three facts make the arithmetic say every pass then
  repeats pass 1, and they are confirmed in the code first:
  1. pass 1 has no mixing step;
  2. each pass's own block sums start from zero;
  3. each pass has its own attention keys and values, not a store shared across passes.
  The result must match the one-pass run within the tolerance. If any of the three facts is false, or the
  result does not match, the design returns to John.

## 4. The comparison removals

| Removal | What it stands for |
|---|---|
| **The message, replaced** (section 3, methods a and b) | The candidate: the loop's feedback about this input |
| **Random, scaled to each item** | Random noise added to the same two block sums on passes 2 and 3, at the positions the swap changes. Its length at each item equals that item's swap size, times one factor shared by all items. The factor is chosen so that the average damage on the neutral set lands within 20% of the main removal's. Twenty draws; their average is the comparison. |
| **Damage outside the loop, scaled the same way** | The same, but added to block 1's output, which runs once and is not part of the loop. Twenty draws. It is used only for the "not specific" check (section 6). |
| **Fewer passes** | Reported with the same statistics, against the unaltered run. Not used for any outcome. |

**Why the random comparison is scaled to each item** (RT-345). Version 0.1 added one noise size to every
item. But the swap changes more of a long item than of a short one, so a single size let a longer cell
take a bigger dose from the swap than from the comparison. Scaling the noise to each item's own swap size
gives each item the same dose under the swap and under its comparison. The cells are also built to the
same length and layout (section 5), so the dose is matched twice over.

**Damage** is how far the model's next-word predictions move on the neutral set, measured as the average
divergence between its predictions before and after the removal, as in the split removal test.

**How the noise is added** (RT-339). The noise is added to the block sums before the readers normalise
them. It touches every coordinate, as the main removal now does. The readers normalise what they read, so
past some size more noise stops adding damage. If the largest damage the noise can reach is less than the
main removal's, the comparison cannot be matched, and the design returns to John before any registration.

**The normal-range check.** It applies to the main removal and to every comparison. The neutral set's
perplexity (how surprised the model is by ordinary text) may rise by no more than the 95th percentile of
the rise across 20 random removals **of the same size**. Here "same size" means noise scaled to each
passage's own swap size with a factor of one, not matched on damage, so that the bound is not circular
(the split design's RT-329). The bound is derived in the rehearsal and fixed before any task is scored.

**Room under the bound** (RT-338). The rehearsal reports how much room the main removal leaves under the
bound, and the ratio of the main removal's damage to that of the same-size noise. The split test's
structured removal on the bench model did about 9.4 times the damage of random noise of the same size,
which is why the split test failed. **If the main removal fails the normal-range check, or leaves too
little room for the comparisons to be matched inside the bound, the design returns to John before any
registration.**

## 5. The tasks

**Scoring by five candidates** (RT-336, RT-349). Every item has a fixed set of five candidate answers: the
right one and four wrong ones built by a rule for that kind, committed before any item exists.

- **All five candidates of an item have the same number of tokens** under the model's own tokeniser.
  Items where this cannot be met are dropped at generation, before any scoring. Each candidate is scored by
  the sum of its tokens' log-probabilities after the prompt, so equal length makes the sums comparable.
- **The probability among the five** is the softmax of those five sums.
- **The model's answer** is the candidate with the highest probability.
- **Chance is 0.20**, so results are reported on a **normalised scale**: normalised accuracy =
  (accuracy − 0.20) / 0.80. On it, 0 is chance and 1 is every item right. A removal that destroys an item
  completely costs at most 1 on this scale, whatever the cell. All thresholds in section 6 apply to this
  scale. Raw accuracy is reported beside it.
- **Why the thresholds still fit.** The δ of 0.10 and the target gap of 0.20 were set for generated answers
  scored from zero. On the normalised scale they mean the same share of the room between chance and perfect.

**Recognising, not producing** (RT-349). Choosing among five is recognising an answer, not producing it.
A disturbed model may still recognise "Paris" among five capitals after it could no longer produce it.
That is likelier for routine questions, and it would hold routine losses down for a reason unrelated to
practice. Two things answer it. The wrong answers for routine questions are built to be close (capitals of
neighbouring countries, sums off by one or two), so that recognition needs the fact. And the report states
plainly that the cells measure recognition among close options.

**No written reasoning.** The answer is scored directly after the prompt, with no reasoning text before
it, because H1 is about what happens inside one moment. If the model writes its working out, it can route
around a lost loop through the text. How to suppress written reasoning, and what the chat template needs
for that, is settled in step 4a of the rehearsal.

**The two cells that decide the outcome are built in matched pairs** (RT-345). Each prompt-rule item has a
routine twin that carries **the same invented rule, word for word, as a preamble**, followed by a routine
question that does not use the rule. So every pair has the same layout and the same preamble, and the two
items differ in length by a few tokens at most. The swap therefore changes the same span in both. A loop
that only helps long contexts helps both cells alike. This replaces version 0.1's short routine items and
the "long routine control" the review proposed.

- **P, prompt-rule problems:** the rule stated in the prompt is needed for the answer.
- **R, routine questions behind the same rule:** the rule is present but irrelevant, and the question is
  one familiar step.

**The kinds, rebuilt for no written reasoning** (RT-344). On the bench model, three of the four
prompt-rule kinds failed even with free generation. With no written reasoning they would be harder still.
The prompt-rule kinds are replaced by one-step rules:

- `p_operator`: an invented operator applied once ("a ◇ b means 2a + b − 1"), kept from the split test;
- `p_unit`: an invented unit conversion applied once ("1 blick is 3 florps; how many florps are 4
  blicks?");
- `p_lookup`: one lookup in an invented table given in the prompt ("a zibvam is red, a tovjot is green...;
  what colour is a tovjot?");
- `p_code`: a one-letter shift applied to a three-letter word, with the shift table given.

The wrong answers are of the same type as the right one: numbers near the right number, colours from the
same table, and real three-letter words. That way, guessing without the rule lands at chance.

**The routine kinds, enlarged** (RT-340, RT-341):
- sums of two numbers from 2 to 49;
- products of two numbers from 2 to 12;
- capitals, from a list of at least 60 countries;
- plurals, from a list of at least 120 common regular nouns;
- opposites, from a list of at least 80 common adjectives.

The next-weekday kind is dropped, because seven days cannot be split into a practice half and a test half.
No single kind may make up more than 25% of a cell, so "routine" is not mostly arithmetic.

**Pilot and test are kept apart, and a script checks it** (RT-341). Every content pool, including the
operands and rule shapes of each prompt-rule kind, is split into two disjoint halves: half A for pilot
items with seed 1, half B for test items with a seed written in the registration. For the operator and unit
kinds, the two halves draw from operand ranges whose answers cannot coincide. A committed check script
fails if any pilot prompt, table, operand pair or answer value appears in the test set, and it runs before
the test set is used.

**Baseline checks** (at three passes, nothing removed):
- **The rule is needed:** with the rule sentence removed, accuracy on that prompt-rule kind is no better
  than chance plus 0.10. A kind that fails is dropped whole.
- **The rule is learned, and the item is confident** (RT-347): the margin, meaning the right candidate's
  log-probability minus that of the best wrong candidate, is at least 2.2 (about 90% when only those two
  are compared).
- **Matching on margin** (RT-347): pairs are kept only if both twins pass, and the R and P cells are then
  matched on margin in bins 0.5 wide, with a fixed seed. Matching on the margin rather than on a coarse
  probability band stops thin-margin P items from simply failing first under any disturbance.
- **Matching on swap size** (RT-345): after margin matching, the two cells' mean swap sizes must be within
  10% of each other for each method. If they are not, items are dropped from the larger cell, from the
  top of the swap-size order, until they are. The number dropped is reported.

**At least three prompt-rule kinds must survive.** If fewer do, the design returns to John before any
registration, rather than running to "not testable".

**The bites check, not in the outcome** (RT-354):
- **L, chained lookup:** the task Thinking Machines describe. Several lookup tables of invented entries are
  given, and the model must follow a chain of two to six lookups in its head, with five answer options.
- **The one-pass run must cost it.** Fewer passes must cost at least 0.15 on the normalised scale on chains
  of four or more lookups, compared with three passes. Otherwise the setup is wrong, and the result is not
  testable. The 0.15 is this design's own choice (RT-355). No page gives a per-pass figure for this task.
  The card's GraphWalks task, a different multi-step task, falls from 64.3% at three passes to 23.5% at one.
- **The main removal must bite.** Under each method, the main removal must cost chained lookup (chains of
  four or more) at least half of what the one-pass run costs it. If it does not, the removal is too weak to
  read a null, and outcome D cannot be read (section 6).

**Sample size** (RT-340). The analysis is paired: the same items are scored under every condition, and
differences are resampled by item. The number of pairs is fixed in the rehearsal by a committed
simulation. It uses the measured spread, the measured loss of the random comparison and the five-donor
averaging, and finds the smallest number giving at least an 80% chance of classifying a true normalised gap
of 0.20 as outcome A, with both methods. The review's simulation found that about 120 items per cell is
enough when the comparison's own loss is about 0.10 or less, and that about 200 are needed when it is 0.20.
The enlarged pools are sized so that half B can supply at least 300 candidate pairs before filtering. **If
the simulation asks for more pairs than survive the filters, the design returns to John.**

**Neutral set** (RT-335). The new neutral set has 200 passages of ordinary prose. They are given in the
same chat template as the items, with lengths spread across the items' range up to the longest item, and
drawn from two disjoint halves like everything else. It replaces the split test's 17-to-23-word passages
for every use in this design: the average method, the damage matching and the normal-range bound.

## 6. The outcomes: every case lands in exactly one

These rules are the split design's (its section 5), with its template checks removed. That design's
template checks asked whether its result came from the chat format's role headers. Nothing here turns on
who is speaking, so they have no counterpart, although the chat template is still used to present the items
(RT-352). **δ = 0.10**, on the normalised scale. Intervals are 95%, from paired resampling of pairs (10,000
resamples, seed fixed in the registration).

For each method, on the R and P cells:
- **R**, the excess loss on routine questions: the main removal's loss minus the random comparison's;
- **P**, the excess loss on prompt-rule problems, computed the same way;
- **G = P − R**, the gap.

**Stage one: is the result readable?** It is **not testable** if:
- the identity check or the bypass check fails (section 3); or
- the one-pass run does not cost chained lookup (section 5); or
- the normal-range check fails for the main removal or for the random comparison; or
- fewer than 10 of the 20 random draws can be matched on damage; or
- fewer than three prompt-rule kinds survive the baseline checks; or
- the two cells' swap sizes cannot be matched within 10%.

Several of these return the design to John during the rehearsal, before any registration, so they should
be met there and not in the run. The report says which applied.

**Stage two: the pattern.** Apply these in order; the first that applies decides.

1. **A. Selective loss on prompt-rule problems.** G is at least δ and its interval lies above zero; P's
   interval lies above zero; and R's interval has its upper end below δ.
2. **B. Selective loss on routine questions.** G is at most −δ and its interval lies below zero; R's
   interval lies above zero; and P's interval has its upper end below δ.
3. **C. General loss.** R and P both have intervals above zero.
4. **D. No excess loss.** R and P both have intervals whose upper ends are below δ, **and the main removal
   passed the bites check** (section 5). If it did not, the outcome is **Too weak to read** (RT-354).
5. **E. Unresolved.** Anything else.

**Checks that apply only to A or B.**
- **Not specific:** if the damage-outside-the-loop comparison's gap, computed like G against the random
  comparison, meets the same test, the outcome is renamed **Not specific**. A loss of this shape would then
  follow from damage of this size anywhere, not from losing this input's feedback.
- **Specificity not checked** (RT-339): if the outside-the-loop comparison could not be matched on damage
  or left the normal range, an A or B is renamed **Specificity not checked**. It is reported with that
  name, never as the prediction holding or failing.
- **Depends on one kind** (RT-352): each prompt-rule kind is reported separately. The outcome is also read
  with each kind left out in turn, and with its routine twins left out with it. If any of those readings
  lands outside A (for an A) or outside B (for a B), the outcome is renamed **Depends on one kind**, with
  the kind named.

C, D and E are never renamed by these checks.

**Combining the two methods** (RT-350). The outcome holds if the swap and the average land in the same one.
If they differ, the result is "methods disagree", reported with both and read as "could not decide". The
two methods differ in kind: one gives a real message about other inputs, the other a blurred average that
no real input produces. So the rehearsal reports each method's damage and swap size side by side. **If
their damage on the neutral set differs by more than a factor of two, the design returns to John before
registration**, so that he can judge in advance whether agreement is plausible.

## 7. What each outcome means, and the words it may be reported in

Every summary, in `STATUS.md`, on the site and in public, uses the sentence below and keeps both
conditions: "both methods agree" and "beyond matched comparisons". No summary may say that the model's
workspace was found, or call the prompt-rule problems "anything new" (RT-356). Every summary names the
model and says the second model shares its pretraining (RT-357).

| Outcome | The sentence it is reported in | What it means for H1's prediction |
|---|---|---|
| **A** | "In [model], replacing the loop's message with one built from other inputs cost more on problems solved from a rule in the prompt than on routine questions behind the same rule, beyond matched comparisons, with both methods agreeing." | **The prediction held for this placement** in this model. It does not show experience or a workspace. |
| **B** | "...cost more on the routine questions than on the prompt-rule problems..." | **The prediction failed for this placement** in this model. |
| **C** | "...cost both alike, beyond matched comparisons..." | **The prediction failed for this placement.** The feedback behaves like an essential part, which shows nothing selective. |
| **D** | "...bit on chained lookup but cost neither routine questions nor prompt-rule problems more than matched comparisons..." | **The prediction failed for this placement.** The model does not need this input's feedback for either kind of task. It is not reported as "the model has no workspace". |
| **E**, methods disagree, not testable, too weak to read, not specific, specificity not checked, depends on one kind | Reported under its name, with the reason. | **No reading.** Never reported as the prediction failing or holding. |

**How the fewer-passes runs are read beside the main result** (RT-353). They are descriptive. One sentence
is allowed in advance. If the one-pass run shows a large loss and the main removal shows outcome D, the
report may say: "what the extra passes supply survives a message built from other inputs of the same
kind". Nothing about "computing" is allowed, because in this model passes without a message add nothing.

**What would count against H1 itself.** Not this test alone. It would need independent evidence that the
loop is this model's shared workspace, and then outcome B, C or D. No such evidence exists, and this design
does not claim any.

## 8. The models, and what it would cost

- **Main model:** TML-d24-varloop-research. Every condition runs on it, and only its result has an outcome.
- **Second model, descriptive only** (RT-351): Inkling 2 Mini, which always runs three passes. It has no
  one-pass setting, so it cannot pass the bypass check or the one-pass half of the bites check. Its result
  is therefore reported with the same statistics, labelled descriptive, with no outcome. It still gets its
  own noise floor, identity check, baseline checks, matching, normal-range bound and damage matching.
  Both models come from one maker and share pretraining, so a result on both is close to one result twice
  (RT-357).
- **The machine.** This Mac has 16 GB of memory and cannot run the model, so every step from 4a onwards
  needs a rented machine. The card names cards of at least 32 GB from NVIDIA's newest generation (the RTX
  5090 and the RTX PRO 6000 Blackwell). If reading and changing the block sums needs the 4-bit weights
  unpacked to ordinary 16-bit numbers, the model needs about 53 GB, and an 80 GB card would be needed
  (RT-337). Under the standing rule, heavy runs go to RunPod.
- **What the work amounts to** (RT-343). Counted on the main model, the conditions on task items are:
  - the unaltered run, twice, for the noise floor;
  - the main removal under two methods, with five donors each under the swap;
  - 20 random draws and 20 outside-the-loop draws for each method, so 80 runs;
  - the one- and two-pass runs, the identity check and the bypass check;
  - the baseline runs without the rule sentence;
  - the bites check under every condition that needs it.

  That is about 100 runs of the item set, plus the search over noise size for damage matching, done on
  the neutral set. Each run is a forward pass over a prompt and its five candidates, with no long
  generation. On roughly 700 items (300 pairs, 100 chained lookups) and 200 neutral passages, that is on
  the order of 100,000 to 200,000 short forward passes for the main model, and about half that again for
  the second model. **No price has been looked up.** The count is made again from the committed code
  before any estimate goes to John.
- **Reused code:** the paired-resampling analysis from the split design. The battery generators are
  rewritten (section 5). New code covers the loop hooks, the candidate scoring, the per-item swap size and
  noise scaling, the chained-lookup generator, the neutral set and the overlap check.

## 9. Order of work

1. **The closure check** of this version by a session that did not write it. It checks that the fixes for
   the two fatal findings (RT-335 and RT-345) close them, and the others as it sees fit. $0.
2. **John rules** on the choices in section 10, and on whether this test goes ahead at all, given the
   tracker of theories ruled on 2026-11-20 and the hibernation from 2027-01-04. $0.
3. **The battery specification, committed before any item:** the rebuilt kinds, the candidate rules, the
   twin construction, the enlarged and split pools, the neutral set, the overlap check script, and the
   pilot set generated with seed 1. The tokeniser is needed for the equal-length rule. It is a small
   download, which comes to John as a file action first. Otherwise $0, on this Mac.
4. **The rehearsal, on a rented machine, pilot items only, on John's go with a ceiling.** It runs in two
   parts, priced separately.
   - **4a. Feasibility**, the first and smallest spend (RT-337). Load the model. Confirm that the block
     sums can be read and replaced, and how much memory that takes. Confirm in the code the facts section 2
     takes from Goodfire and the three facts the bypass check needs. Settle how to suppress written
     reasoning. Measure the noise floor, and run the identity and bypass checks. **If the hooks cannot be
     built, any of the three facts is false, or either check fails, the design returns to John.**
   - **4b. The measurement rehearsal.** The baseline checks and matching; the bites check; the swap sizes;
     the normal-range bound and the room under it; damage matching for both comparisons; the two methods'
     damage side by side; and the committed sample-size simulation. **Each return-to-John condition in
     sections 4 to 6 applies here.**
5. **Registration text**, through the inside and outside review passes (Gate A), then the registration
   commit.
6. **The registered run**, on John's go, with a ceiling.
7. **The findings**, through the interpretation review (Gate B).

Steps 1 to 3 cost nothing and can be done before the hibernation. When steps 4 onwards happen is John's
call.

## 10. Choices for John

1. **Score by the five candidates' probabilities, not by a generated answer** (section 5). The swap needs
   the donor's sums at every position the recipient uses, which is only possible when the answer's
   positions are fixed in advance. Recommended.
2. **Score with no written reasoning only** (section 5). Recommended, because H1 is about one moment, and
   written reasoning lets the model route around the loop.
3. **Routine twins carrying the prompt-rule item's rule as a preamble** (section 5), in place of short
   routine items. Recommended, because it is the main answer to the fatal finding that length and dose
   could produce the predicted pattern on their own.
4. **Inkling 2 Mini as a second, descriptive model** (section 8). Recommended as optional. It costs a
   second download and about half as much machine time again, and it gives no outcome.

Version 0.1's fourth choice, keeping the pass-counting coordinates at their true values, is withdrawn
(RT-348).

## Sources read for this design (all on 2026-11-20)

- Thinking Machines Lab,
  [Introducing Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/).
- Thinking Machines Lab,
  [TML-d24-varloop-research model card](https://thinkingmachines.ai/model-card/tml-d24-varloop-research/),
  and its [Hugging Face page](https://huggingface.co/thinkingmachines/TML-d24-varloop-research).
- Goodfire,
  [Interpreting Inkling 2 Mini](https://www.goodfire.com/research/interpreting-inkling-2-mini/), including
  its appendix on the architecture.
- This project: `docs/2026-11-20-loop-removal-design-note.md`,
  `docs/2026-11-20-three-hypotheses-and-refocus-proposal.md`,
  `docs/split-removal-test-design-2026-10-24.md` (sections 2 to 6),
  `experiments/09-split-removal-test/battery-authoring-spec.md`, `experiments/09-split-removal-test/src/batteries.py`,
  `experiments/09-split-removal-test/rehearsal/phase1-findings-2026-10-24.md`, and the inside review of
  version 0.1.

## Change log from version 0.1, by finding

**Fatal findings:**
- **RT-335 (fatal), the average method cannot be computed:** the average is now taken over positions, by
  pass and by layer source, with template positions averaged by template token. It uses a new neutral set
  in the chat template, with passages as long as the longest items (sections 3 and 5).
- **RT-345 (fatal), the swap's dose and the item lengths differ between the cells:** three changes.
  - The routine items are now twins of the prompt-rule items, carrying the same rule as a preamble, so the
    two cells have the same length, layout and changed span (section 5).
  - The swap size is measured for every item, and the cells must match on it within 10%, with a stated
    rule for dropping items (sections 3 and 5).
  - The random comparison is scaled to each item's swap size (section 4).

**Serious findings:**
- **RT-336, five-candidate scoring undefined:** candidates of equal token length, scored by summed
  log-probability, normalised by a softmax over the five. The donor runs on its own prompt and right
  answer, so its sums exist at the candidates' positions (sections 3 and 5).
- **RT-337, hooking unproven:** feasibility is the first, separately priced step (4a). The 80 GB case is
  stated, and a failure returns the design to John (sections 8 and 9).
- **RT-338, normal-range check and the dropped room rule:** the room-under-the-bound rule is restored, with
  the damage ratio reported. A failed or tight bound returns the design to John (section 4).
- **RT-340, sample size and the pool cap:** the routine pools are enlarged so that half B can supply at least
  300 candidate pairs. The simulation uses the measured comparison loss, and a shortfall returns the design
  to John (section 5).
- **RT-341, pilot and test overlap:** next weekday dropped; operator and unit operands drawn from ranges
  whose answers cannot coincide; a committed overlap check; no kind above 25% of a cell (section 5).
- **RT-344, three prompt-rule kinds may not survive:** the kinds are rebuilt as one-step rules suited to no
  written reasoning, with wrong answers of the same type. Fewer than three surviving returns the design to
  John (section 5).
- **RT-346, the donor's answer can intrude:** donors' right answers are excluded from the recipient's
  candidates (section 3).
- **RT-347, coarse confidence bins:** matching on the margin between the right and the best wrong candidate,
  in bins 0.5 wide, with pairs kept only when both twins pass (section 5).
- **RT-348, the kept coordinates keep half the message:** nothing is kept at its true value. A three-pass
  donor and a per-pass average already carry the pass-counting signal (section 3). The fourth choice of
  version 0.1 is withdrawn.
- **RT-349, five-candidate scoring changes what a loss means:** results are on a normalised scale from chance
  to perfect, raw accuracy is reported beside it, routine wrong answers are built to be close, and
  recognition among close options is stated in every report (section 5).
- **RT-350, the two methods differ in kind:** their damage is reported side by side in the rehearsal, and a
  difference of more than a factor of two returns the design to John (section 6).
- **RT-351, the second model cannot pass stage one:** it is descriptive only, with no outcome, and keeps its
  own baseline and range checks (section 8).
- **RT-353, the "extra computing" sentence:** deleted. Section 1 states that the test cannot separate
  feedback from computing, and the one allowed sentence speaks only of what survives the swap (section 7).
- **RT-354, outcome D with no check behind it:** chained lookup is now scored under each method. D needs the
  main removal to cost it at least half of what one pass costs. Otherwise the outcome is "too weak to read"
  (sections 5 and 6).

**Worth-noting findings:**
- **RT-339, damage matching and the noise:** the noise is added before normalisation and touches every
  coordinate. Too low a damage ceiling returns the design to John. An unmatched outside-the-loop comparison
  renames an A or B "specificity not checked" (sections 4 and 6).
- **RT-342, the bypass check:** it is defined from the code as doing on passes 2 and 3 what pass 1 does.
  The three facts it needs are confirmed in the code first, and the tolerance comes from a measured noise
  floor (section 3).
- **RT-343, the work undercounted:** recounted, and to be counted again from the committed code before an
  estimate goes to John (section 8).
- **RT-352, rules left undefined:** donors are drawn from the same kind and cell; donors on the neutral set
  are other neutral passages of similar length; every replaced sum comes from the donor's unaltered run;
  there are five donors per item; and a reading with one kind left out that differs from the full reading
  renames the outcome "depends on one kind". The "typical coordinate" threshold is no longer used. Section
  6 now says why the template checks have no counterpart, even though the chat template is used.
- **RT-355, claims about the external pages:** "same architecture" withdrawn; every fact taken from
  Goodfire is checked on the research model's code in step 4a. "Almost all of it from block 3" is now
  Goodfire's own "almost always". The pass-counting finding is narrowed to the readers Goodfire studied.
  "No message on pass 1" is now a fact to confirm. The mixing is described as Goodfire gives it, with its
  ranges. The 0.15 threshold is stated as this design's own choice. The review's two corrections that did
  not hold (the card's pass-count figures, and the training precision) are recorded in the filer's check
  below the review.
- **RT-356, a per-word loop is not the shared workspace:** section 1 says so, and section 7 bars "the
  workspace was found" and "anything new" from every summary.
- **RT-357, one maker, one pretraining run:** every summary says the second model shares pretraining.
