# The loop removal test: a design on paper

*Version 0.4, written 2026-11-20 on John's instruction ("Write 0.4 first"). It answers the closure check
of version 0.3 (`docs/reviews/2026-11-20-loop-removal-test-design-v0.3-closure-check-claude-code.md`).
That check closed RT-335, the finding that the averaging method could not be computed, with its rerun on
the real template owed at step 3. It judged version 0.3 fit to go to John for his section 10 rulings, with
RT-345 carried open. It raised four serious findings, RT-370 to RT-373, and six worth noting, RT-374 to
RT-379, and it asked for five clarifications of RT-345's closure rule. The third change log at the end
says how each is answered. **RT-345, the finding that the swap's dose differed between the two task
groups, stays open.** Its closure remains a measurement on the model at step 4b. The fixes are the
author's and are owed a closure check.*

*Version 0.3 (commit 8bd34cd) was written on John's instruction ("Yes, write 0.3"). It answered the closure check
of version 0.2 (`docs/reviews/2026-11-20-loop-removal-test-design-v0.2-closure-check-claude-code.md`).
That check closed fatal finding RT-335 (the averaging method could not be computed) with three
conditions. It kept fatal finding RT-345 (the swap's dose differed between the two task groups) open,
and judged that its decisive check needs the model. It also raised RT-358 to RT-369. The second change
log at the end says how each was answered.*

*Version 0.2 (commit 7760fda) answered the inside review pass of version 0.1
(`docs/reviews/2026-11-20-loop-removal-test-design-gate-c-tier1-claude-code.md`, red-team findings
RT-335 to RT-357). That pass found two fatal problems, fourteen serious ones and seven worth noting.
The first change log at the end says how each was answered. Version 0.1 is commit 4f68df5.*

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

**What the routine cell measures** (RT-365). Each routine question sits behind an invented rule that it
does not use, so that the two cells have the same length and layout. So the routine cell measures **a
practised answer given while an irrelevant rule sits in the prompt**. That is not the same as practised
output on its own, because ignoring a rule just read is itself a small act of control. Section 5 limits
this: no rule is paired with a routine question of the same type, and a routine twin must be answered as
well behind its rule as with no rule at all. The rest of the gap is stated in every report: a routine loss
could come from a lost ability to ignore the rule, which is flexible control rather than practice.

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

- **(a) Swap, with donors drawn by pair** (RT-345, RT-358, RT-370). Every task is one of a twin pair: a
  prompt-rule item and its routine twin, which carries the same rule as a preamble (section 5). Donors are
  drawn **as whole pairs**. For a recipient pair, a donor pair is drawn whose rule is of the same rule
  kind **and whose routine twin asks the same routine kind**. That way each routine twin's donor shares
  its question template, just as each prompt-rule item's donor does. The prompt-rule item then gets the donor pair's prompt-rule item's block sums, and the routine twin
  gets the donor pair's routine twin's block sums, at the same position and on the same pass. All sums are
  taken from the donors' unaltered runs. Because the two preambles of a pair are word for word the same,
  and the two donor preambles are too, donor and recipient diverge at the same place in both cells. Only
  the question parts differ.
  - **Its own answer.** Each donor's run uses its own prompt and its own right answer, so that its sums
    exist at the positions of the recipient's candidates (RT-336).
  - **Length.** A donor pair is eligible only if each of its twins is at least as long as the matching
    recipient's prompt plus its longest candidate. Within a pair, the two question parts also have the
    same token count by construction (section 5), so the swap changes the same span in both twins.
  - **Five donor pairs.** Each pair gets five donor pairs, drawn at random with a seed fixed in the
    registration. Each item's score under the swap is the average over its five donors, so that the luck of
    the draw is inside the intervals (RT-352). If fewer than five are eligible, all eligible ones are used.
    If none is, the pair is dropped. Both counts are reported (RT-369).
  - **No intruding answers.** A donor's right answer is never one of the recipient's candidates (RT-346).
    The rehearsal reports how often the chosen candidate shares its first token with a donor's answer.
- **(b) Average.** The two block sums are replaced by their average over **a new neutral set**, taken
  separately for each pass and each layer source, but **not for each position** of ordinary text
  (RT-335). Positions inside the fixed chat template are averaged **by template slot**: by their place in
  the template, counted from the start of the template's opening part and from the end of its closing
  part. That way a token that fills several slots, such as a newline, gets a separate average for each
  (RT-335, condition 2). The neutral set is rendered with **every template token the items use**,
  including the generation prompt and any block used to suppress written reasoning, once step 4a has fixed
  them (RT-335, condition 1). Pooling over text positions makes the method computable at any length. (The
  earlier sentence comparing this with experiment 01's mean-ablation is withdrawn, because experiment 01's
  records do not say how it treated positions.)
  - **Built on one part of the neutral set, measured on another** (RT-376). The neutral set has 200
    passages in each half. In the half in use, 100 build the average and the other 100 measure its
    damage, so that the average is not judged on the passages it came from.
  - **The fallback, fixed now** (RT-364, RT-376). Pooling gives the same message at every text position.
    It may therefore turn out much harsher or much milder than the swap, and trip the factor-of-two rule in
    section 6. If it does, method (b) is replaced by **one named fallback**: the average taken in ten bins
    of relative position. In full:
    - **The text span.** For an item, this is every position that is not a template slot, from the first
      word of the user text through the last token of the candidate being scored. For a neutral passage,
      it is every position of its prose.
    - **The bin.** A position's bin is ten times its place in the span (counting from 0) divided by the
      span's length, rounded down.
    - **Template slots** keep their slot averages.

    Nothing else may be chosen after seeing results. If the fallback also trips the rule, the average method ends. The
    outcome would then rest on the swap alone, which changes the "both methods agree" rule, so it needs
    John's ruling (section 10, choice 5).

**Nothing is kept at its true value** (RT-348). Version 0.1 kept the pass-counting coordinates at their
true values. The review showed that this keeps close to half of the message's normalised size, and with
it much of the choice of block and the keep and gain settings. It is not needed. A donor also ran three
passes, so its sums carry the same "another pass follows" signal on the same pass. The average is taken
for each pass, so it carries the average signal for that pass. Both methods therefore keep the model's
count of passes without leaking anything from the recipient. The rehearsal reports, for description:
- how much the pass-counting coordinates vary from item to item and from position to position (RT-379);
- what share of the message's normalised size the swap changes;
- how far it moves the keep and gain settings.

**The swap's size is measured for every item** (RT-345). For each item and method, the **swap size** is the
total distance, over all changed positions and both passes, between the true normalised block sums and the
replacement ones. Section 4 uses it to scale the comparisons item by item, and section 5 uses it to check
that the two cells received the same dose.

**Donors on the neutral set** (RT-352, RT-366). The swap's damage on the neutral set is needed for damage
matching and for the normal-range bound. Each neutral passage gets five donors, which are other neutral
passages of the same half at least as long as it, drawn with a seed fixed in the registration. Its damage
is the average over the five, the same dose rule as the items. As with items, if fewer than five donors
are eligible, all eligible ones are used, and a passage with none is left out of the swap's damage. Both
counts are reported (RT-378).

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
| **Random, scaled to each item** | Random noise added to the same two block sums on passes 2 and 3, at the positions the swap changes. At each position its length is proportional to that position's own swap distance (RT-366), so that its total over the item equals the item's swap size, times one factor shared by all items. The factor is chosen once, so that the average damage of the twenty draws on the neutral set lands within 20% of the main removal's. Twenty draws; their average is the comparison. |
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
past some size more noise stops adding damage. **If no shared factor brings the average damage within 20%
of the main removal's** (RT-366), the comparison cannot be matched, and the design returns to John before
any registration.

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
practice. Two things answer it. The wrong answers for routine questions are built to be close, so that
recognition needs the fact. And the report states plainly that the cells measure recognition among close
options.

**How the wrong answers are built, kind by kind** (RT-368). "Close" must not break the equal-length rule,
so every wrong answer is a real answer of the same type:
- **numbers:** within a few units of the right answer and with the same number of digits;
- **capitals:** capitals of neighbouring countries;
- **opposites:** the opposites of other adjectives from the same pool;
- **everyday colours** (the routine kind that replaces plurals, below): other common colours;
- **the lookup table's colours:** the other colours in the same table, which has five to seven entries,
  each with a different colour, so that four wrong colours always exist (RT-377);
- **the letter code:** other common three-letter words, built as described under `p_code` below.

**No candidate may be found by copying** (RT-373). For every routine kind, no candidate may repeat a word
of the question, or begin with one. The plural kind is dropped for this reason, because the right plural
always begins with the noun asked about.

Candidates for test items are drawn only from half B's pools (RT-341). Step 3 reports, for every kind, how
many items the equal-length rule drops and how the right answers are spread before and after, so that the
rule's effect on which answer values are kept can be seen (RT-336, RT-368).

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
- `p_code` (RT-368, RT-372): **decoding** a three-letter string with an invented letter-substitution table
  given in the prompt. The right answer is a common real word, and the table is invented for each item
  and is not a shift, because a uniform shift is practised knowledge. So that the answer cannot be found by
  spotting letters:
  - **Extra rows.** The table has eight rows, not three. The coded word uses three of them, and the other
    five map further letters.
  - **Wrong answers from the same letters.** Every wrong answer is a common three-letter word from the
    same pool, spelled only with the table's plain letters. Every candidate is then "spelled with the
    table's letters", and only decoding tells them apart.
  - **Shuffled rows.** The rows are listed in shuffled order, not in the order of the coded word.
  - **No coded string.** The coded string itself is never a candidate.

  An item for which four such wrong answers of equal token length cannot be found is dropped at
  generation. The overlap script also checks, for every letter-code item, that each wrong answer is
  spelled only with the table's plain letters.

The wrong answers are of the same type as the right one, as listed above. That way, guessing without the
rule lands at chance.

**The routine kinds, enlarged** (RT-340, RT-341, RT-361):
- sums of two numbers from 2 to 49, with the halves split at an answer of 50;
- products of two numbers from 2 to 12, with the halves split at an answer of 40;
- capitals, from a list of at least 150 countries;
- opposites, from a list of at least 160 common adjectives (80 opposite pairs);
- everyday colours (RT-373), from a list of at least 150 common objects with one typical colour ("What
  colour is a ripe banana?"), where the colour word never appears in the question. This kind replaces
  plurals.

**No routine question is used twice.** Under the 25% cap below, a cell of 300 pairs allows 75 questions
of each routine kind. Half B then holds about 75 sums, 60 products, 75 capitals, 80 opposites and 75
everyday colours, so about 360 distinct routine questions before any filter. If the filters leave fewer
pairs than the sample-size simulation needs, the design returns to John (RT-361). The closure check of
version 0.3 found that the simulation needs about 120 to 200 pairs.

The next-weekday kind is dropped, because seven days cannot be split into a practice half and a test half.
**No single routine kind may make up more than 25% of the routine cell**, so "routine" is not mostly
arithmetic. The cap applies to routine kinds only (RT-362). The prompt-rule kinds are kept as nearly equal
in number as the filters allow, and their counts are reported.

**Which rule goes with which routine question** (RT-365). A rule is never paired with a routine question
of the same type:
- the arithmetic rules (`p_operator`, `p_unit`) are never paired with sums or products;
- the word rule (`p_code`) is never paired with opposites;
- the colour table (`p_lookup`) is never paired with everyday colours.

The generator first applies the 25% cap and the pool sizes. Within those limits, it spreads the routine
kinds as evenly as it can across the rule kinds (RT-374). The value the rule would give if wrongly
applied to the routine question is never one of that question's candidates.

**The two question parts of a pair have the same token count** (RT-370). The closure check of version 0.3
found that, with the preambles matched, the swap still changed more of the routine twin. That was because
routine questions ran a few tokens longer than rule questions, in every pair of the operator and
letter-code kinds. So each routine kind and each rule kind is written in several phrasings of different
lengths. For instance, "What is the capital city of X?", "Name the capital of X." and "X's capital
is?". The generator picks, for each pair, the phrasings that give the two question parts the same token
count under the model's tokeniser. A pair for which no phrasings match is dropped at generation, and the
drops are counted by kind.

**Pilot and test are kept apart, and a script checks it** (RT-341). Every content pool, including the
operands and rule shapes of each prompt-rule kind, is split into two disjoint halves: half A for pilot
items with seed 1, half B for test items with a seed written in the registration. For the operator and unit
kinds, the two halves draw from operand ranges whose answers cannot coincide. A committed check script
fails if any pilot prompt, table or operand pair appears in the test set, or if any answer value of one
kind appears in both halves of that same kind. Answer values are compared within each kind, because a
number can rightly be both a unit answer and a sum (RT-341). The script also fails if any test item's
candidate comes from a half-A pool. It runs before the test set is used.

**Baseline checks** (at three passes, nothing removed):
- **The rule is needed:** with the rule sentence removed, accuracy on that prompt-rule kind is no better
  than chance plus 0.10. A kind that fails is dropped whole.
- **The rule is learned, and the item is confident** (RT-347): the margin, meaning the right candidate's
  log-probability minus that of the best wrong candidate, is at least 2.2 (about 90% when only those two
  are compared).
- **The rule does not get in the way of the routine question** (RT-365, RT-374): each routine twin's
  margin behind its rule must be within 1.0 of the same question's margin with no preamble.
  - **A whole kind.** A routine kind that fails this check for more than a fifth of its items, behind a
    given rule kind, is not paired with that rule kind.
  - **Single items.** Within a kind that passes, a pair whose routine twin fails is dropped whole.
  - **When it is fixed.** The resulting table of which routine kinds go with which rule kinds is fixed on
    the pilot items, at step 4b, and written into the registration before the test set is generated.
  - **What it can show.** The check works at baseline only. It cannot show that the removal leaves the
    ability to ignore the rule intact, as section 1 says.

**All matching acts on whole pairs, within each rule kind** (RT-359, RT-360). Nothing in the matching
removes a single item and leaves its twin behind, because the analysis resamples by pair.
- **Margin.** A pair is kept only if both twins pass the confidence check. Then, within each rule kind,
  whole pairs are dropped until the mean margins of the two cells are within 0.5 of each other. The pairs
  dropped are those whose difference between the routine twin's margin and the prompt-rule item's runs
  **in the direction of the imbalance**, largest first (RT-375). The rule is mechanical and has a fixed
  seed for ties. The margin distributions of the two cells, before and after, are reported.
  - **The margin fallback, fixed now** (RT-375). Practised facts are likely to sit at higher margins than
    one-step rules. If matching the means would remove more than a third of a rule kind's pairs, the
    fallback is used instead: keep only pairs whose two margins both lie between 2.2 and the 90th
    percentile of the prompt-rule items' margins in that kind, and then match as above. If that also
    removes more than a third, the design returns to John.
- **Swap size** (RT-345). Then, within each rule kind and **for each method**, whole pairs are dropped until
  the two cells' mean swap sizes are within 10% of each other. The pairs dropped are those whose
  difference runs in the direction of the imbalance, largest first. For the average method, the changed
  span is the whole text span of the item, so its swap size is measured over every position that is not
  a template slot.
- **Limits** (RT-345, clarifications 2 to 5).
  - **Margin matching.** It may remove at most a third of any rule kind's pairs, as above.
  - **Swap-size matching.** It may remove **at most a tenth** of any rule kind's pairs, under either
    method. The tenth is counted from the pairs left just before swap-size matching, after the confidence
    check, margin matching and donor eligibility.
  - **On the pilot pairs** (step 4b), exceeding the tenth returns the design to John before any
    registration.
  - **On the test pairs** (the registered run), the same rule is applied unchanged. If it would need more
    than a tenth in any kind, the result is not testable for that reason (section 6).
  - **Reporting.** The mix of rule kinds and routine kinds before and after each step is reported, and so
    is the routine-kind mix of the pairs dropped.

**At least three prompt-rule kinds must survive.** If fewer do, the design returns to John before any
registration, rather than running to "not testable".

**The bites check, not in the outcome** (RT-354):
- **L, chained lookup:** the task Thinking Machines describe. Several lookup tables of invented entries are
  given, and the model must follow a chain of two to six lookups in its head, with five answer options.
- **The one-pass run must cost it.** Fewer passes must cost at least 0.15 on the normalised scale on chains
  of four or more lookups, compared with three passes. Otherwise the setup is wrong, and the result is not
  testable. The 0.15 is this design's own choice (RT-355). No page gives a per-pass figure for this task.
  The card's GraphWalks task, a different multi-step task, falls from 64.3% at three passes to 23.5% at one.
- **The main removal must bite, beyond generic damage** (RT-367). Under each method, the main removal's
  loss on chained lookup (chains of four or more) **minus the random comparison's loss** on the same items
  must be at least half of what the one-pass run costs it, with that excess's interval above zero. If not,
  the removal is too weak to read a null, and outcome D cannot be read (section 6). Measuring against the
  random comparison stops generic damage of the same size from passing the check.

**Sample size** (RT-340). The analysis is paired: the same items are scored under every condition, and
differences are resampled by item. The number of pairs is fixed in the rehearsal by a committed
simulation. It uses the measured spread, the measured loss of the random comparison and the five-donor
averaging, and finds the smallest number giving at least an 80% chance of classifying a true normalised gap
of 0.20 as outcome A **after every check in section 6 that can rename an A**, including the readings with
one kind left out, with both methods (RT-363). The first review's simulation found that about 120 items per
cell is enough for a bare A when the comparison's own loss is about 0.10 or less, and that about 200 are
needed when it is 0.20. The closure check of version 0.2, with the leave-one-kind-out rule as version 0.2
wrote it, found the chance of a clean A falling to 0.45 to 0.76 at those sizes. The closure check of
version 0.3, under that version's narrower rule, found 80% reached at about 120 pairs (comparison loss
0.10) and about 200 pairs (0.20). Version 0.4 changes the rule again (section 6) and adds routine kinds to
it. So the committed simulation must be run under the rule as written here, with both rule kinds and
routine kinds left out in turn. If a rule kind is dropped, the simulation is re-run with the kinds that
remain. Half B can supply at
most about 360 distinct pairs before filtering (above). **If the simulation asks for more pairs than
survive the filters, the design returns to John.**

**Neutral set** (RT-335, RT-376). The new neutral set has 400 passages of ordinary prose, 200 in each half.
In the half in use, 100 build the average and 100 measure damage (section 3). They are rendered with
every template token the items use (section 3), with lengths spread across the items' range up to the
longest item, and drawn from two disjoint halves like everything else. It replaces the split test's
17-to-23-word passages for every use in this design: the average method, the damage matching and the
normal-range bound. **At step 3, once the model's own chat template and tokeniser are in hand, the check
that every position of every pilot item, candidates included, has a defined average is run again and
committed** (RT-335, condition 3).

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
- no shared factor brings the random comparison's average damage within 20% of the main removal's
  (RT-366); or
- fewer than three prompt-rule kinds survive the baseline checks; or
- the two cells' swap sizes cannot be matched within 10%, under either method, without removing more than
  a tenth of a rule kind's pairs (section 5).

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
- **Depends on one kind** (RT-352, RT-363, RT-371, RT-373). Each prompt-rule kind and each routine kind is
  reported separately. The outcome is also read with each kind left out in turn:
  - leaving out a **rule kind** removes every pair with that rule;
  - leaving out a **routine kind** removes every pair whose routine twin asks it.

  If any of those readings lands in a **different definite outcome** (B, C or D for an A; A, C or D for a
  B), the outcome is renamed **Depends on one kind**, with the kind named. A reading that lands in E is
  reported but does not rename.
  - **The bites check does not apply here.** These readings are made on their R and P intervals alone.
    "No excess loss" counts as D in them whether or not the main removal passed the bites check. Without
    this, a failed bites check turned the D that exposes a one-kind effect into "too weak to read", which
    renames nothing. The closure check of version 0.3 measured that leak at 81% to 96% when one kind
    carried the whole effect.
  - **Why E does not rename.** Leaving out a quarter of the pairs widens every interval, so in version
    0.2's form the rule turned true effects into "no reading" about half the time.
  - **Why routine kinds are included.** A routine kind that held routine losses down by itself would
    otherwise go unseen.

  This rule is fixed here, before any data.

C, D and E are never renamed by these checks.

**Combining the two methods** (RT-350). The outcome holds if the swap and the average land in the same one.
If they differ, the result is "methods disagree", reported with both and read as "could not decide". The
two methods differ in kind: one gives a real message about other inputs, the other a blurred average that
no real input produces. So the rehearsal reports each method's damage and swap size side by side. **If
their damage on the neutral set differs by more than a factor of two, the average is replaced by its one
named fallback** (section 3). If the fallback also differs by more than a factor of two, the design returns
to John before registration (RT-364).

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
  the neutral set. Each run scores a prompt with each of its five candidates, with no long generation. On
  roughly 700 items (300 pairs, 100 chained lookups), that is about 330,000 short continuations for the
  main model if each candidate is run separately (RT-369). The count is lower if the five candidates share
  the prompt's computation, which step 4a settles. The second model adds about half that again. **No price has been looked up.** The count is made again from the committed code
  before any estimate goes to John.
- **Reused code:** the paired-resampling analysis from the split design. The battery generators are
  rewritten (section 5). New code covers the loop hooks, the candidate scoring, the per-item swap size and
  noise scaling, the chained-lookup generator, the neutral set and the overlap check.

## 9. Order of work

1. **The closure check** of this version by a session that did not write it. It checks the fixes for the
   third closure check's findings (RT-370 to RT-379) and the five clarifications of RT-345's closure rule.
   It cannot close RT-345, whose decisive check needs the model (step 4b), although it can rerun the
   stand-in estimate under the equal-length construction. $0.
2. **John rules** on the choices in section 10, and on whether this test goes ahead at all, given the
   tracker of theories ruled on 2026-11-20 and the hibernation from 2027-01-04. $0.
3. **The battery specification, committed before any item:** the rebuilt kinds, the candidate rules, the
   twin construction, the enlarged and split pools, the neutral set, the overlap check script, and the
   pilot set generated with seed 1. The tokeniser is needed for the equal-length rule. It is a small
   download, which comes to John as a file action first. Otherwise $0, on this Mac. With the real
   tokeniser and template, step 3 also commits:
   - the check that every position has a defined average (RT-335, condition 3);
   - the equal-length rule's drop rates by kind (RT-368);
   - the twins' lengths;
   - a stand-in estimate of the swap's dose in each cell under the pair donor rule, using the real
     tokeniser. This is the measure the closure checks used: the changed span, and a proxy swap size with
     same-token positions weighted 0, 0.3 and 0.6. It runs before the model is rented, so that a large
     imbalance shows up without spending anything (RT-345).
   - **A threshold on that estimate** (RT-370, RT-345 clarification 5). In every rule kind, the ratio of
     the routine cell's proxy swap size to the prompt-rule cell's must lie between 0.95 and 1.05 at weight
     0.3, and between 0.90 and 1.10 at weights 0 and 0.6. If it does not, the construction is revised and
     the estimate run again before anything is rented. Each revision and its reason is committed. If no
     revision brings every kind inside, the design returns to John.
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
   - **The closure of RT-345.** A session that did not write the pair donor rule or the equal-length
     construction reads the committed swap sizes from 4b. It checks that, in every rule kind **and under
     both methods**, the two cells' mean swap sizes are within 10%. That must hold either before any pairs
     are dropped, or with at most a tenth of the kind's pairs dropped, counted as section 5 says. It also
     reports the routine-kind mix of any pairs dropped. If all of this holds, RT-345 is closed. If not, it
     stays open, and the design returns to John before any registration. The same rule is applied
     unchanged to the test pairs at the registered run (section 5).
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
   could produce the predicted pattern on their own. The cost is stated in section 1: the routine cell
   then measures a practised answer given while ignoring a rule, not practised output on its own (RT-365).
   This choice bears most on what the test means. In version 0.4 the twins also have question parts of
   equal token count, written in several phrasings so that lengths can be matched, and their donors share
   the routine kind (RT-370). The closure check of version 0.3 forecast that, without this, the swap-dose
   check would fail in two of the four rule kinds. Whether it now passes is first estimated for free at
   step 3 and then measured on the model at step 4b.
4. **Inkling 2 Mini as a second, descriptive model** (section 8). Recommended as optional. It costs a
   second download and about half as much machine time again, and it gives no outcome.
5. **If the average and its fallback both differ from the swap by more than a factor of two** (sections 3
   and 6), should the outcome rest on the swap alone, or should the test stop there? Asked now, before any
   data, so that the choice cannot be made from results. Recommended: stop. One method gives no check that
   a result is not a quirk of how the message was replaced.

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

*This change log records version 0.2 as it was written. Several rules in it were later replaced, and
the body governs (RT-379):*
- *"averaged by template token" became averaging by template slot (version 0.3);*
- *"no kind above 25% of a cell" became a cap on routine kinds only (version 0.3);*
- *margin matching "in bins 0.5 wide" became matching of mean margins on whole pairs within each rule
  kind (version 0.3);*
- *a factor-of-two difference between the methods now leads first to a named fallback (version 0.3);*
- *neutral donors "of similar length" became donors at least as long, from the same half (version 0.3);*

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

## Change log from version 0.2, by finding of the closure check

*This change log records version 0.3 as it was written. Two rules in it were later replaced, and the body governs (RT-379): the "more than a third" limit on swap-size matching became "more than a tenth" (version 0.4); and plurals were dropped as a routine kind (version 0.4).*

**The fatal findings:**
- **RT-335, the averaging method, closed with three conditions.** All three are now in the design:
  - the neutral set is rendered with every template token the items use (section 3);
  - template positions are averaged by template slot, not by token identity (section 3);
  - the check is run again with the real template and tokeniser at step 3, and committed (sections 5
    and 9).

  The unchecked sentence about experiment 01's mean-ablation is withdrawn.
- **RT-345, the swap's dose, kept open.** The length half was closed by the routine twins. For the dose
  half, donors are now drawn as whole pairs of the same rule kind, so that the preambles diverge at the same
  place in both cells (section 3). All matching acts on whole pairs within each rule kind (section 5). A
  stand-in estimate of the changed span is committed at step 3, before anything is rented. The closure is
  the measured swap sizes at step 4b, read by a session that did not write the fix (section 9).

**Findings the closure check left open:**
- **RT-340, sample size.** The simulation now targets a clean A after every renaming check, including the
  leave-one-kind-out readings. The pools are sized under the cap (RT-361), and a shortfall returns the
  design to John (section 5).
- **RT-352, a rule written only in the change log.** The rule for donors on the neutral set is now in
  section 3.

**Conditions the closure check set on findings it closed:**
- **RT-336:** drop rates of the equal-length rule by kind are reported at step 3.
- **RT-339:** see RT-366.
- **RT-341:** answer values are compared within each kind, and test candidates may come only from half B
  (section 5).
- **RT-346:** the rehearsal reports how often the chosen candidate shares a first token with a donor's
  answer (section 3).
- **RT-348:** the report of how much the pass-counting coordinates vary by item and position stays in
  section 3.
- **RT-349:** see RT-368.

**New findings:**
- **RT-358, the donor rule for routine twins was ambiguous:** donors are drawn by pair. The prompt-rule
  item gets the donor pair's prompt-rule item, and the routine twin gets the donor pair's routine twin
  (section 3).
- **RT-359, matching by dropping single items:** matching drops whole pairs, within each rule kind, choosing
  the pairs whose twins differ most. Removing more than a third of a kind returns the design to John
  (section 5).
- **RT-360, margin matching broke pairs:** margin matching now acts on whole pairs within each rule kind,
  matching the two cells' mean margins within 0.5, and both margin distributions are reported (section 5).
- **RT-361, 300 pairs not available under the cap:** the pools are enlarged to at least 150 countries, 240
  nouns and 160 adjectives. No routine question is used twice. The arithmetic of about 360 distinct
  questions in half B is shown (section 5).
- **RT-362, the cap and the prompt-rule cell:** the 25% cap applies to routine kinds only (section 5).
- **RT-363, the leave-one-kind-out rule halves the chance of a clean A:** the rule now renames an outcome
  only when a reading with one kind left out lands in a different definite outcome, not when it lands in E.
  The sample-size simulation must include the rule as written (sections 5 and 6).
- **RT-364, no fallback for the average:** one fallback is named now, the average in ten bins of relative
  position. If that also trips the factor-of-two rule, the average method ends, and John is asked in
  advance whether the outcome then rests on the swap alone or the test stops (sections 3, 6 and 10).
- **RT-365, a routine question behind an irrelevant rule also tests ignoring the rule:**
  - section 1 says what the routine cell now measures;
  - no rule is paired with a routine question of its own type;
  - the value the misapplied rule would give is never a candidate;
  - a new baseline check requires each routine twin to be answered as well behind its rule as without it
    (section 5);
  - the choice to use twins says what it costs (section 10).
- **RT-366, rules missing from the body:** the rules for neutral donors and five donors on the neutral set
  are in section 3. The noise is spread across positions in proportion to each position's swap distance
  (section 4). The stage-one rule on matched draws is restated for a single shared factor (section 6).
- **RT-367, the bites check could be passed by generic damage:** the check is now made on the main
  removal's loss on chained lookup minus the random comparison's loss, with its interval above zero
  (section 5).
- **RT-368, building the candidates:** wrong answers are real answers of the same type, kind by kind, with
  numbers of the same digit count. The letter code is now decoding with an invented substitution table, so
  the right answer is a real word and the table is not practised. Drop rates are reported (section 5).
- **RT-369, donors for the longest items and the pass count:** if fewer than five donor pairs are eligible,
  all eligible ones are used, and a pair with none is dropped, both counted. The pass count is restated at
  about 330,000 continuations if candidates are run separately (sections 3 and 8).

## Change log from version 0.3, by finding of the third closure check

**RT-345, the swap's dose differed between the cells, kept open.** Its closure rule (section 9, step 4b)
now takes the five clarifications the check asked for:
1. it covers both methods, with the average method's changed span defined as the whole text span
   (section 5);
2. the tenth is counted from the pairs left just before swap-size matching (section 5);
3. the tenth is now section 5's limit for swap-size matching, in place of a third, and section 6's
   stage one says so;
4. the same rule is applied unchanged to the test pairs, and exceeding it there makes the result not
   testable (section 5);
5. the routine-kind mix of the pairs dropped is reported. The free step-3 estimate now has a threshold,
   which triggers a revision of the construction before anything is rented (section 9, step 3).

**Serious findings:**
- **RT-370, the routine cell still took more swap in two rule kinds:** each pair's two question parts
  now have the same token count, chosen from several phrasings of each kind, with pairs that cannot match
  dropped and counted. Donor pairs must also share the routine kind (sections 3 and 5). A threshold on the
  step-3 estimate, at 0.95 to 1.05 at the middle weight, catches any remaining gap before money is spent
  (section 9).
- **RT-371, the narrower "depends on one kind" rule leaked when the bites check failed:** the
  leave-one-kind-out readings are now made on their R and P intervals alone, so that "no excess loss"
  counts as D in them whatever the bites check gave (section 6).
- **RT-372, the letter code could be answered by spotting letters:** the table now has eight rows in
  shuffled order. Every wrong answer is a common word spelled only from the table's plain letters, and
  the coded string is never a candidate. The overlap script checks the spelling rule (section 5).
- **RT-373, plurals could be answered by copying the noun:** plurals are dropped. They are replaced by
  everyday colours ("What colour is a ripe banana?"), whose answer word never appears in the question. A
  general rule now bars any candidate that repeats or begins with a word of the question. Routine kinds
  are now left out in turn in the "depends on one kind" readings, as rule kinds are (sections 5 and 6).

**Worth-noting findings:**
- **RT-374, the "answered as well behind its rule" check:** failing pairs within a passing kind are
  dropped whole. The pairing table is fixed on the pilot items and written into the registration, and
  the generator spreads kinds only after the cap and pool sizes are applied (section 5).
- **RT-375, the direction of dropping, and margin matching:** both matching steps now drop pairs whose
  difference runs in the direction of the imbalance. A margin fallback is fixed in advance: a common band
  from 2.2 to the 90th percentile of the prompt-rule margins in that kind (section 5).
- **RT-376, the relative-position fallback:** the text span, the bin and the treatment of template slots
  are defined. The neutral set is enlarged to 400 passages, so that in the half in use the average is
  built on 100 passages and its damage measured on the other 100 (sections 3 and 5).
- **RT-377, the lookup table's size:** five to seven entries, each with a different colour (section 5).
- **RT-378, donors for the longest neutral passages:** the items' rule now applies to them too: use all
  eligible donors, leave out a passage with none, and count both (section 3).
- **RT-379, change logs out of step with the body:** section 3 now reports the pass-counting coordinates'
  variation by item and by position. Each earlier change log opens with a note listing its rules that
  were later replaced.
