# The loop removal test: a design on paper

*Version 0.16, written 2026-11-23 on John's instruction ("Yes, write 0.16"). It answers the closure check of
version 0.15 (`docs/reviews/2026-11-23-loop-removal-test-design-v0.15-closure-check-claude-code.md`). That
check confirmed on resampled real data that scoring by margin gives the test its power. It also found that
version 0.15's conversion constant K, which divided a precise margin loss by a noisy count of right answers,
was too uncertain to carry the thresholds. Version 0.16:
- **replaces K** with the prompt-rule cell's one-pass cost in margin, measured directly. On step 4b's data that
  cost was 4.19 nats, with a 95% range of 3.6 to 4.8, against K's range of about 15 to 51 (RT-506);
- **puts the thresholds to John as choice 9.** δ and the target gap become shares of that one-pass cost. They
  are no longer numbers carried over from the accuracy scale (RT-506, RT-507);
- **drops "accuracy-equivalent"** and rewords sections 1 and 7, so that the outcomes say what they measure: a
  loss of the model's confidence in the right answer, which can happen without any answer turning wrong
  (RT-507, RT-508);
- **fixes the definitions and stale text** the check listed (RT-509, RT-511, RT-512). The simulation's double
  division (RT-510) is the code's to fix.

The fourteenth change log at the end says how. **The changes are owed a closure check, after John's ruling on
choice 9.***

*Version 0.15 (commit 7b1fdf3) was written 2026-11-23 on John's ruling ("Yes, write 0.15";
`docs/rulings/2026-11-23-loop-removal-test-margin-scoring-ruling.md`). **The outcome measure changes from
right-or-wrong to the margin.** The margin is the log-probability of the right candidate minus that of the
best wrong one. A free check on step 4b's data (`experiments/10-loop-removal-test/margin-power-check-2026-11-23.md`)
found that, under right-or-wrong scoring, the test could not reach its power. Outcome A would be read in only
11 to 64% of runs at the test half's sizes, and outcome F almost never. Under the margin, A reached 94 to
100% from 80 pairs, and F became reachable. Version 0.15 restates the measure, its scale and every threshold
that rests on it (section 5). It does not change the confidence check or the interference checks, which stay
on accuracy as John ruled. How the thresholds are carried to margin units is the author's design, and it is
marked as such. The thirteenth change log at the end says what changed.*

*Version 0.14 (commit c9cfa08) was written 2026-11-23 on John's instruction ("Yes, write 0.14"). It answers the closure check of
version 0.13 (`docs/reviews/2026-11-23-loop-removal-test-design-v0.13-closure-check-claude-code.md`), which
found version 0.13 ready for the rebuild, with points for a short version 0.14. The main changes:
- **a pairing needs at least three confident pilot pairs** to stay in the pairing table (RT-485);
- **the reply rendering is defined exactly.** Everything before the prose is one fixed opening, so the swap
  and the average both change only the prose. A second average, built in the reply, is measured beside the
  first, with a return to John if the two differ by more than a factor of two (RT-486, RT-487);
- **the bites set's kinds are chosen by the committed simulation,** not by a 0.15 cut. The rerun pilot carries
  enough unit items to read either branch, and sections 6 and 7 name the kinds actually in the set (RT-488
  to RT-490);
- **the likeliest way the test ends unread is stated now.** That is the normal-range check and the in-loop
  comparison, from step 4b's figures. It goes to John when the rerun is priced (RT-491).

**The author's additions** are now listed as the author's in a closing note to section 11 (RT-494). The
twelfth change log at the end says how each finding is answered. The dose finding (RT-345) waits for the
rerun.*

*Version 0.13 (commit 795cba2) was written 2026-11-23 on John's instruction ("Yes, write 0.13"). It writes in his three rulings
after step 4b (`docs/rulings/2026-11-23-loop-removal-test-after-step4b-ruling.md`), which answer the step-4b
findings (`experiments/10-loop-removal-test/step4b-findings-2026-11-23.md`):
- **interference is judged by accuracy,** in place of a limit of 1.0 in margin. The new rule is counted over
  the pairs whose answer is right without the other half of the context. Counted over confident pairs, as
  the old rule was, it would be empty (section 5);
- **damage and perplexity are measured on prose placed as the model's own reply,** where its predictions are
  trained. A check that those predictions are good comes before any is used (sections 4 and 5);
- **the operator kind is simplified to a single step,** with a rule fixed now for the case where it no
  longer gains enough from the extra passes to serve in the bites set (section 5).

Step 4b also answered the dose question (RT-345) on the model, before any filter: the two cells' swap sizes
differ by under 1%. The formal closure still reads them after the filters, at the rerun. The eleventh change
log, "from version 0.12", says what changed.*

*Version 0.12 (commit 4fb7e73) was written 2026-11-21 on John's instruction ("Yes, write 0.12"). It answers the closure check
of version 0.11 (`docs/reviews/2026-11-21-loop-removal-test-design-v0.11-closure-check-claude-code.md`), which
found outcome F the right kind of answer but not yet safe to read. Version 0.12:
- **requires the swap's own loss to be small for F,** not only its loss beyond random damage (RT-457);
- **narrows the "disagree" rename.** It no longer applies to B, and for A and C it applies only when the
  operator and unit pairs themselves lose (RT-458);
- **defines the swap-size ratio exactly,** and has step 4b report it, with a return to John if F cannot be
  reached (RT-459);
- **matches the halves item by item,** with fixed tolerances and a model-free seed rule (RT-460).

It also answers RT-461 to RT-465 and the two owed definitions. The eleventh change log at the end says how.*

*Version 0.11 (commit b211fa7) was written 2026-11-21 on John's instruction ("Yes, write 0.11"). It answers the closure check
of version 0.10 (`docs/reviews/2026-11-21-loop-removal-test-design-v0.10-closure-check-claude-code.md`), which
found three serious problems. Version 0.11:
- **adds a readable negative,** outcome F, "The replacement does not bite". It covers the case where the
  extra passes help but a message built from other inputs serves as well. The prediction can then fail in
  the plainest way, not only through general or routine loss (RT-449);
- **revises choice 8** to drop the letter-code kind and share the pairs equally among the three remaining
  kinds. As version 0.10 wrote it, it would have capped the test half at about 144 pairs (RT-450);
- **replaces the bands of five** with a split that gives each half the same mix of last digits (RT-451).

It also answers RT-452 to RT-456 and the small fixes under the earlier findings. The tenth change log at the
end says how.*

*Version 0.10 (commit 600d0bb) was written 2026-11-21 on John's instruction ("Yes, write 0.10"). It answers the closure check
of version 0.9 (`docs/reviews/2026-11-21-loop-removal-test-design-v0.9-closure-check-claude-code.md`), which
judged the operator and unit bites problems the right call but found four serious problems. Version 0.10:
- **takes away outcome D's reading** while the bites problems share kinds with the prompt-rule cell (RT-437);
- **states the measured risk** that the operator kind, not only the letter code, fails the confidence filter,
  and adds choice 8, to drop the letter-code kind (RT-438);
- **meant to make the two halves equally hard** by splitting answers into interleaved bands of five, in
  place of the split by size (RT-439). The bands in fact split the last digit, and version 0.11 replaces
  them (RT-451);
- **narrows the keep-apart rule** for bites problems, so that the pilot can be built (RT-440).

It also corrects the trial figures (RT-441) and answers RT-442 to RT-448. The ninth change log at the end
says how.*

*Version 0.9 (commit 4dbc4a3) was written 2026-11-21 on John's choice ("Invented-rule problems"). It answers three runs on a
rented machine rather than a review. Step 4a found the hooks exact, but forced answers near chance. The
scoring trial found that an instruction to answer with the single word or number makes the paired questions
work. The lookup calibration trial found that the model cannot follow even two linked lookups when it must
answer at once, so chained lookup cannot serve as the bites check. Version 0.9 adopts the answer-only
instruction, and replaces chained lookup in the bites check with held-out problems of the operator and unit
rule kinds, the two kinds measured to gain from the extra passes. It also says what that replacement costs
the reading of outcome D, and asks two new questions of John. The eighth change log at the end says how.*

*Version 0.8 (commit 38148b1) was written 2026-11-21 on John's instruction ("Yes, write 0.8"). It answers the closure check of
version 0.7 (`docs/reviews/2026-11-21-loop-removal-test-design-v0.7-closure-check-claude-code.md`). That
check found version 0.7 ready for the battery specification once one rule was added, and version 0.8 adds
it: donor-only pairs may reuse routine questions and sit outside the no-reuse rule, the pool budget and the
cap (RT-403). It also makes the smaller fixes the check listed: RT-404 to RT-408, two gaps on RT-402, the
region map for RT-396, and the cost sentence. The seventh change log at the end says how.*

*Version 0.7 (commit 8a5aabb) was written 2026-11-21 on John's instruction ("Yes, write 0.7"). It answered the closure check of
version 0.6 (`docs/reviews/2026-11-21-loop-removal-test-design-v0.6-closure-check-claude-code.md`). That
check found version 0.6 one short revision from the battery specification. It asked for two fixes: the
lookup kind's donors and size classes (RT-398), and the count of single-token capitals and what that rule
does to the capitals cell (RT-399). Version 0.7 makes both. It also settles RT-400 to RT-402, the
conditions on RT-390, RT-394 to RT-396, and the section 11 note, whose quotation the check rightly
questioned (RT-401). The sixth change log at the end says how. **RT-345 stays open until step 4b.** The
fixes are owed a closure check.*

*Version 0.6 (commit 5bc172a) was written 2026-11-21 on John's instruction ("Yes, write 0.6"). It answered the closure check of
version 0.5 (`docs/reviews/2026-11-21-loop-removal-test-design-v0.5-closure-check-claude-code.md`). That
check confirmed with the real tokeniser that the shared-context construction gives both cells the same
stand-in dose (0.998 to 1.019), and judged version 0.5 nearly ready for the battery specification. It asked
for two fixes first: the lookup size-class rule at the pilot size (RT-392), and the baseline check's
comparison item with a mirror check on the prompt-rule side (RT-393). It also asked for the alignment
sentences and the context order to be fixed in the same pass (RT-390, RT-394). Version 0.6 does those, and
also settles RT-391 and RT-395 to RT-397 here rather than in the specification. The fifth change log at the
end says how.*

*Version 0.5 (commit b8579de) was written 2026-11-21 on John's instruction ("Yes, write 0.5"). It answered the closure check of
version 0.4 (`docs/reviews/2026-11-20-loop-removal-test-design-v0.4-closure-check-claude-code.md`), four serious
findings (RT-380 to RT-383) and six worth noting (RT-384 to RT-389). It is the first version written with the
research model's real tokeniser in hand (`docs/2026-11-21-loop-removal-tokeniser-download.md`). The main
change is to how the twin pairs are built: **both twins now carry one shared context word for word, and
they differ only in a final question of fixed wording** (section 5). John's rulings of 2026-11-21 on the
section 10 choices (section 11) stand, and the change keeps to them: the routine questions are still twins
of the rule questions. The fourth change log at the end says how each finding is answered. **RT-345, the
finding that the swap's dose differed between the two task groups, stays open.** Its closure remains a
measurement on the model at step 4b. The fixes are the author's and are owed a closure check, by a reviewer
working in its own empty scratch folder.*

*Version 0.4 (commit ddc5031) was written 2026-11-20 on John's instruction ("Write 0.4 first"). It answered the closure check
of version 0.3 (`docs/reviews/2026-11-20-loop-removal-test-design-v0.3-closure-check-claude-code.md`).
That check closed RT-335, the finding that the averaging method could not be computed, with its rerun on
the real template owed at step 3. It judged version 0.3 fit to go to John for his section 10 rulings, with
RT-345 carried open. It raised four serious findings, RT-370 to RT-373, and six worth noting, RT-374 to
RT-379, and it asked for five clarifications of RT-345's closure rule. The third change log at the end
says how each was answered.*

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

**What the routine cell measures** (RT-365). Each pair's two items share one context: an invented rule
with its own facts, and a fact for the routine question, such as "The country is France." The prompt-rule
item then asks a fixed question that needs the rule. The routine twin asks a fixed question that does
not, such as "What is the capital of the country?" (section 5). So the routine cell measures **a practised
answer about a thing named in the context, given while an irrelevant rule sits in the prompt**. That is not the same as practised
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
- **What the outcomes measure** (version 0.16, RT-508). Since version 0.15 every loss is a loss of **margin**:
  how far the model's confidence in the right answer falls, among five fixed choices. An outcome can be
  reached with no change in which answers are right. "Cost more on prompt-rule problems" therefore means
  "lowered the model's confidence in the right answer more", not "made it answer wrongly more often". The
  share of right answers is reported beside every outcome.
- **If the predicted pattern appears,** that is a fact about this loop in this model. It does not show
  that the model has experience, or that its workspace was found.
- **H1's prediction fails for this placement in this model** (section 7) in two kinds of case:
  - the cells show the opposite pattern or a general loss beyond matched comparisons (outcomes B and C).
    These need no result from the bites check, except that a C is set aside when the bites check and the
    cell's operator and unit pairs contradict each other (section 6, RT-458);
  - the extra passes are shown to help on the held-out rule problems, the message is shown to have been
    changed by at least half its size on average, and a message built from other inputs costs those
    problems little, in each of the two kinds (outcome F, version 0.11, RT-449; tightened in version 0.12,
    RT-457, RT-461).

  A failure in either kind of case is a result against the placement, not against H1 itself, because the
  model may do H1's job where the loop does not reach.
- **A replacement that bites but costs neither cell** (outcome D) gives no reading, because the bites problems
  share two kinds with the prompt-rule cell (section 5, RT-437).
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

- **(a) Swap, with donors drawn by pair** (RT-345, RT-358, RT-370, RT-380). Every task is one of a twin
  pair: a prompt-rule item and its routine twin. The two share one context word for word and differ only
  in a final question of fixed wording (section 5). Donors are drawn **as whole pairs**. For a recipient
  pair, a donor pair is drawn whose rule is of the same rule kind and whose routine question is of the
  same routine kind, so that its two final questions are the same fixed strings as the recipient's
  (RT-389). The prompt-rule item then gets the donor pair's prompt-rule item's block sums, and the routine
  twin gets the donor pair's routine twin's block sums, at the same position and on the same pass. All
  sums are taken from the donors' unaltered runs. Within a pair the contexts are identical, and so are the
  donor pair's. So donor and recipient diverge at the same place in both cells. Both cells' donors also
  ask the same final question as their recipients. But a donor is usually longer, so its final question
  usually starts a few positions later than the recipient's, and its tokens do not line up with the
  recipient's one for one (RT-390). That happens in the same way in both cells.
  - **Its own answer.** Each donor's run uses its own prompt and its own right answer, so that its sums
    exist at the positions of the recipient's candidates (RT-336).
  - **Length.** A donor pair is eligible only if each of its twins is at least as long as the matching
    recipient's prompt plus its longest candidate. Within a pair, the two final questions have the same
    token count, and every candidate of both twins is a single token (section 5). So the swap changes the
    same span in both twins (RT-390).
  - **One table size for the lookup kind** (RT-388, RT-392, RT-398). Every lookup table, at the pilot and
    at the test, has six entries. The size classes of versions 0.4 to 0.6 are withdrawn. The sixth check
    found that three classes made donors scarcer, not more plentiful: about 17 of 75 lookup test pairs had
    none. It also found that the classes could not be filled below 288 test pairs, and that the pilot's
    tables did not match the test's. With one size, the pilot rehearses exactly the test's lookup items.
  - **Donor-only pairs** (RT-398). Some groups have too few eligible donors, because a donor's right answer
    may not be among the recipient's candidates. Lookup, whose answers come from about eleven colours, has
    the fewest: about 6 of 30 lookup pilot pairs had none. So the generator also makes **donor-only
    pairs**. These are built exactly like scored pairs, but they are never scored: only their unaltered
    runs are kept, to serve as donors. They are added to any group of rule kind and routine kind until
    every scored pair in it has at least five eligible donors, or until the group holds three times as
    many donor-only pairs as scored ones, whichever comes first. They are drawn from the same half as the
    scored pairs they serve. The rule against intruding answers (below) is kept unchanged.
    - **They may reuse content** (RT-403). A donor-only pair may reuse any routine question, rule content
      or invented word from its own half, including those already used by scored pairs or other donor-only
      pairs. **Donor-only pairs sit outside the rule that no routine question is used twice, outside the
      pool budget, and outside the 25% cap.** Reuse is harmless. A donor-only pair that repeats a
      recipient's routine question has the recipient's right answer, so the rule against intruding answers
      already bars it as that recipient's donor. And donor-only pairs are never scored, so reuse adds no
      repeated item to either cell. Without this rule the pools run out before any donor-only pair can be
      built where it is needed, and lookup's fix fails at the pilot, as the seventh check measured.
    - **They are aimed at the pairs short of donors** (RT-404). A candidate donor-only pair is kept only if
      it is eligible to serve at least one scored pair in its group that still has fewer than five donors.
      Otherwise it is discarded and another is drawn, up to the threefold cap. Without this, random
      additions rarely reach the longest scored pair of a group, and the pairs left without donors were
      almost always the longest. Any scored pair still left with no donor is dropped, and its content is
      reported, so that a systematic loss of long items can be seen.
    - **Their cost** (corrected, RT-404 to RT-408 pass). Each donor-only pair needs two unaltered runs, one
      per twin, and its block sums must be stored. The seventh check's stand-in build added about 2.1 to 2.8
      donor-only pairs per scored pair, so about five extra unaltered runs per scored pair. That is about 5%
      beside the roughly hundred runs each scored pair needs for its own conditions. The stored block sums
      come to about 1.7 MB per run at 16 bits, or about 2.5 GB at 300 pairs.
    - **The overlap script includes them** (RT-403). Donor-only pairs count as part of the set they serve,
      pilot or test, in every check the script makes.
  - **Reporting.** For every group, step 3 reports the number of eligible donors per scored pair, from the
    stand-in build, and the number of donor-only pairs added. Scored pairs still left with no donor are
    dropped and counted, at both sizes.
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
loop supplies is not assumed: it is checked on a task measured to need the extra passes (the "bites"
check, section 5). If the replacement does not bite there, that is read as outcome F, the prediction failing, only when the
swap is shown to have changed the message, its own loss on those problems is shown to be small, and the
cells show no excess either. Otherwise it is too weak to read (section 6).

**Other conditions, which do not decide the pattern.** Fewer passes are used in two places (RT-511): the one-pass
run sets the unit C (section 5), and it gates every outcome through the bites check's one-pass condition.

- **Fewer passes: two, and one.** These remove the message and the extra passes together. They are
  reported with the same statistics as the main removal, measured against the unaltered run, and labelled
  as fewer passes.
- **The noise floor** (RT-342). Two unaltered runs of the same items are compared first. Mixture-of-experts
  routing or the order of arithmetic on the card may make them differ slightly. At step 4a, at 16-bit, they
  did not differ at all (a largest difference of 0.0 over 280 items). The **tolerance** for the next two checks is
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
| **Fewer passes** | Reported with the same statistics, against the unaltered run. Not used for the pattern; the one-pass run sets the unit C and gates every outcome through the bites check (section 5). |

**Why the random comparison is scaled to each item** (RT-345). Version 0.1 added one noise size to every
item. But the swap changes more of a long item than of a short one, so a single size let a longer cell
take a bigger dose from the swap than from the comparison. Scaling the noise to each item's own swap size
gives each item the same dose under the swap and under its comparison. The cells are also built to the
same length and layout (section 5), so the dose is matched twice over.

**Damage** is how far the model's next-word predictions move on the neutral set, measured as the average
divergence between its predictions before and after the removal, as in the split removal test.
- **Where it is measured** (version 0.13, John's ruling after step 4b). Damage and perplexity are measured on
  the neutral prose **placed as the model's own reply**. The user's message is one fixed short request, the
  same for every passage and written in the specification, and the passage follows the reply opening. Step 4b
  found that, in the chat format, the model predicts the user's own text almost at random: 8.7 nats per token,
  against 2.3 for the same prose as plain text. So damage measured there tracked changes in noise. In the
  model's reply, its predictions are the ones it was trained to make.
- **The same prose still builds the average** in the user's turn, where the items' text sits (section 3). The
  two renderings of a passage carry the same prose. Only its place in the chat format differs.
- **The reply rendering, exactly** (version 0.14, RT-486; the author's reading). Everything before the first
  prose token is **one fixed opening**: the template's opening, the fixed request, the end of the user's
  message, and the model's reply opening. Every passage has the same opening, so its positions are template
  slots, counted from the start. The prose follows, and the reply's end-of-message token closes it. That
  token is rendered, and it is the only closing slot. So the swap and the average both change only the
  prose, plus the slots. The slots get the reply rendering's own slot averages under the average method, and
  the donor's own sums under the swap; those are identical, because the opening is shared. **Plain text**,
  for the check below, is the prose's tokens alone, with no chat format.
- **The replacements on the reply rendering.**
  - Under the swap, a passage gets the sums of other passages in the same reply rendering, under the donor
    rule for neutral passages (section 3).
  - Under the average, the prose positions get the pooled text average built from the user-turn passages,
    the one the items get. **This is the author's reading of John's ruling** (RT-487, RT-494). It means the
    average's damage on the reply rendering includes a mismatch of role that the items never meet.
  - **So a second average is measured beside it**: the pooled text average built from the reply renderings of
    the "build" passages. If the two averages' damages on the measure passages differ by more than a factor of
    two, the design returns to John before registration. Otherwise the first, built in the user's turn, is the
    one used, because it is the one the items get.
  - The comparisons and the normal-range bound use the same rendering.
- **A check before it is used** (worded more modestly in version 0.14, RT-496). Before any damage is used,
  step 4b measures the unaltered model's mean loss per token on the measure passages in three renderings:
  the reply rendering, the user's turn, and plain text. If the reply rendering's loss is more than 1 nat per
  token above the plain text's, the design returns to John before any matching is done. This only shows that
  the model predicts the prose in the reply rendering. It does not show that damage measured there tracks
  what a removal does to the items.

**The likeliest way the test ends unread** (version 0.14, RT-491). At step 4b, in-loop noise of the swap's
own size did little damage. Matching the swap's damage took a factor of 987, at the top of the search's
range, and it still fell 18% short. The swap's damage is far beyond what random change of the same size does.
That is the pattern on which the split removal test failed, where the ratio was 9.4, and here it is larger.
Measured properly on the reply rendering, two things are likely:
- the main removal fails the normal-range check, whose bound comes from same-size noise;
- the in-loop comparison for the swap cannot be matched within 20%.

Either one makes every outcome "not testable" at stage one. This is stated now so that John weighs it when
the rerun is priced, and so that no different bound or comparison is chosen after seeing more results. The
factor search runs from 0.001 to 100,000 (the author's choice). A best factor at either end of the range
counts as unmatched unless its damage lies within 20%.

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
- **Ties** (RT-446). If the right candidate ties exactly with one or more wrong ones for the highest
  probability, the item counts as right in the share 1/k, where k is the number of tied candidates. Its
  margin is 0, so it fails the confidence filter. Ties are counted and reported at every step. The scores
  come out of the model at 16-bit, so exact ties happen: 8 in 640 scores in the lookup calibration trial.
  The same coarseness means the smallest non-zero margin seen was 0.047, larger than the 0.01 tolerance of
  section 3. So the identity and bypass checks will usually fail on any real difference between the runs, although a
  difference smaller than the tolerance is possible, because the tolerance applies to each candidate's
  log-probability and not to a margin. They matched exactly at step
  4a.
- **The outcome measure is the margin** (version 0.15, John's ruling). An item's **margin** is the
  log-probability of the right candidate minus the highest log-probability among the four wrong ones, in
  nats. It is the same among the five whether taken from the whole vocabulary or from the softmax over the
  five, so choice 1 is unchanged. A tie for the top gives a margin of 0.
  - **An item's loss under a condition** is its margin in the unaltered run minus its margin under the
    condition.
    - Under the swap, the condition's margin is the average of the item's margins over its five donors.
    - Under a comparison, it is the average over the comparison's draws.
    - Under fewer passes, it is the margin of the one- or two-pass run.
  - **Why** (the margin check). Scored right or wrong, an item loses nothing or everything, so the per-item
    spread of a removal's loss was 0.45 to 0.58 on step 4b's data. In the margin, converted as below, it was
    0.13 to 0.17. At the test half's size, that is the difference between an outcome the test can read and
    one it cannot.
- **The scale: shares of what one pass costs, in margin** (version 0.16, RT-506, RT-507; the author's design,
  with the thresholds put to John as choice 9). Version 0.15 divided margin losses by K, the ratio of a margin
  loss to a right-or-wrong loss. Its denominator was a noisy count of right answers, so K could lie anywhere
  from about 15 to 51 nats on step 4b's data. Version 0.16 uses one unit that is measured in margin alone:
  - **The unit, C.** On the pilot at the step-4b rerun, take the prompt-rule items that pass the baseline
    checks and the confidence check, before margin and swap-size matching (RT-509). C is their mean one-pass
    loss in margin: the unaltered margin minus the one-pass margin. On step 4b's data it was 4.19 nats, with a
    95% range of 3.6 to 4.8. C is fixed on the pilot, written into the registration and never recomputed on
    the test half. Every loss in the cells is divided by C. A loss of 1 then means "as much margin as dropping
    to one pass costs these items".
  - **The anchor's own check.** If C's 95% interval on the pilot is wider than half of C on either side, the
    unit cannot be fixed well enough, and the design returns to John. On step 4b's data it was about ±14%.
  - **The thresholds,** in units of C, are choice 9 (section 10). As written here, until John rules, they are
    the recommended option: **δ = 0.5** (an excess below half of what one pass costs counts as no excess) and
    **a target gap of 1.0** (a gap as large as what one pass costs). These round the values the accuracy scale
    implied on step 4b's data, 0.57 and 1.15.
  - **The bites items need no conversion.** Their conditions are ratios of their own one-pass cost in margin:
    "half", "three quarters" and "a quarter". Version 0.15's K_b is withdrawn, and with it the circle in which
    the branch choice needed K_b and K_b needed the branch (RT-509). The bites check's **one-pass condition**
    becomes: the bites items' one-pass cost in margin has an interval whose lower end is at least **a quarter
    of C**. That is the author's choice. On step 4b's data, the operator bites items cost 1.81 nats (range 1.02
    to 2.69) and the unit items 5.93 (5.17 to 6.71), against a quarter of C, about 1.05.
  - **What the units are not.** They are not right-or-wrong losses, and nothing in this design calls them
    "accuracy-equivalent" any more (RT-507). On step 4b's data, the swap cost the prompt-rule items about 10.8
    nats of margin, which is about 2.6 units of C, while the share of right answers they lost was 0.93 on the
    normalised accuracy scale. The two scales measure different things.
- **What the margin scale does not have.** It has no ceiling. A removal that turns an item's margin of 10
  into −10 costs it 20 nats, about five units of C. It also has long tails. The analysis resamples, so the
  tails widen the intervals honestly. The analysis resamples, so the tails widen the intervals honestly. The
  report gives the losses' quantiles beside every cell.
- **Accuracy is still reported.** Normalised accuracy is reported beside every margin figure, as a
  description, so that a reader can see what the losses mean as right and wrong answers.
- **The confidence and interference checks are unchanged.** The confidence check still asks for a margin of at
  least 2.2. The interference checks still ask whether an answer is right (John's ruling after step 4b).
- **Each condition's margin, defined** (RT-509).
  - **The swap.** The mean of the item's margins over its donors: up to five, as section 3 sets out.
  - **The average and its fallback.** The margin of the one run with the average, or with the binned average,
    in place.
  - **A comparison.** The mean over its 20 draws.
  - **Fewer passes.** The margin of the one- or two-pass run.
- **Starting margins** (RT-512). Margin matching brings the two cells' mean unaltered margins within 0.5 nats
  of each other. Under the average method, a difference in starting margins can pass into the gap. The closure
  check of version 0.15 put it at up to about a fifth of δ. So the two cells' mean starting margins are
  reported beside every outcome.

**The answer-only instruction** (version 0.9). Every scored item, donor and bites item carries one fixed
sentence: "Answer with the single word or number only." Step 4a found that, without it, the model's forced
first answer was near chance on most kinds: it always chooses to begin its reply with written reasoning,
even at the reasoning setting "none". In the scoring trial on the pilot, the sentence lifted the routine
twins from 51% to 83% or 84% at three passes, and the share of pair items passing the confidence filter from 28%
to 63% or 65% (of 240 pair items; the trial's own report also counted 40 chained items, which all failed) (`experiments/10-loop-removal-test/scoring-trial-findings-2026-11-21.md`). It does not change
choice 2: the answer is still the first token, with no written reasoning. Both twins of a pair carry it word
for word, so their lengths stay equal. Where it sits, at the start or the end of the message, is choice 6
(section 10).

**Recognising, not producing** (RT-349). Choosing among five is recognising an answer, not producing it.
A disturbed model may still recognise "Paris" among five capitals after it could no longer produce it.
That is likelier for routine questions, and it would hold routine losses down for a reason unrelated to
practice. Two things answer it. The wrong answers for routine questions are built to be close, so that
recognition needs the fact. And the report states plainly that the cells measure recognition among close
options.

**How the wrong answers are built, kind by kind** (RT-368). "Close" must not break the equal-length rule,
so every wrong answer is a real answer of the same type:
- **numbers:** within a few units of the right answer and with the same number of digits;
- **capitals:** capitals of neighbouring countries, drawn only from half B's countries, and one token each.
  Where too few neighbours qualify, capitals of countries in the same region are used, and then of the
  nearest neighbouring region. An item for which four still cannot be found is dropped. Step 3 reports
  how often each happens (RT-396). How often depends almost entirely on how "region" is drawn: the sixth
  check found about half of half B's capitals short of four, the seventh about one in ten. So **the battery
  specification writes out the region map and each region's nearest neighbouring region before any item
  exists**, and step 3 reports the counts under that map;
- **opposites:** the opposites of other adjectives from the same pool;
- **everyday colours** (the routine kind that replaces plurals, below): other common colours;
- **the lookup table's colours:** the other colours in the same table, which has six entries, each with a
  different colour, so that four wrong colours always exist (RT-377, RT-398, RT-406);
- **the letter code:** other common three-letter words, built as described under `p_code` below.

**No candidate may be found by copying** (RT-373, RT-385). The plural kind is dropped, because the right
plural always begins with the noun asked about. The rule that replaces it:
- **What it compares.** It works on the content words of the item's routine fact and final question
  ("France", "happy", "banana"). It works on whole words, not on digits or single letters, and it ignores
  the rule's text, whose single letters and invented words would otherwise bar almost everything.
- **What it bars.** No candidate may contain one of those words, or be contained in one. That bars
  "unhappy" for "happy", and "Tunis" for "Tunisia", which the version 0.4 wording, which barred only
  repeating or beginning with a word, let through.
- **What it does not apply to.** Numbers are exempt, because their wrong answers are built to share
  leading digits, and a digit-by-digit reading would drop about half the products.
- **It covers both cells** (RT-395). Under the shared context the routine fact sits in the prompt-rule item
  too, so the rule also applies to prompt-rule candidates. No letter-code candidate may contain, or be
  contained in, a content word of the routine fact (for example "nut" beside "walnut"). The fifth check
  found about 1% of letter-code items affected.
- **And the reverse rule** (RT-395). Section 5 already keeps the value the rule would give out of the
  routine twin's candidates. In the same way, the routine twin's right answer is never one of the
  prompt-rule item's candidates. A colour such as "red" can never be a letter-code candidate behind an
  everyday-colours twin. And the prompt-rule item's right answer is never one of the routine twin's
  candidates, so a letter-code answer such as "red" or "tan" never appears among a colour twin's options
  (RT-395, the residual case the sixth check found).

Candidates for test items are drawn only from half B's pools (RT-341). Step 3 reports, for every kind, how
many items the equal-length rule drops and how the right answers are spread before and after, so that the
rule's effect on which answer values are kept can be seen (RT-336, RT-368).

**No written reasoning.** The answer is scored directly after the prompt, with no reasoning text before
it, because H1 is about what happens inside one moment. If the model writes its working out, it can route
around a lost loop through the text. How to suppress written reasoning, and what the chat template needs
for that, is settled in step 4a of the rehearsal.

**The two cells that decide the outcome are built in matched pairs** (RT-345). Each prompt-rule item has a
routine twin that carries **the same context, word for word**, followed by a fixed routine question that
does not use the rule. So every pair has the same layout and the same context, and the two items differ
only in their final questions, which have the same token count (see "One shared context" below). The swap therefore changes the same span in both. A loop
that only helps long contexts helps both cells alike. This replaces version 0.1's short routine items and
the "long routine control" the review proposed.

- **P, prompt-rule problems:** the rule stated in the prompt is needed for the answer.
- **R, routine questions behind the same rule:** the rule is present but irrelevant, and the question is
  one familiar step.

**The kinds, rebuilt for no written reasoning** (RT-344). On the bench model, three of the four
prompt-rule kinds failed even with free generation. With no written reasoning they would be harder still.
The prompt-rule kinds are replaced by one-step rules:

- `p_operator`: an invented operator applied once. **Since version 0.13 it is a single arithmetic step on the
  two operands with a written constant**, for example "a ⊛ b means a plus b plus 3" (John's ruling after step
  4b). The two-step shapes used up to version 0.12, such as "3 times a, minus b", are withdrawn. At step 4b
  only 9 of 40 operator pairs were confident, and the operator's prompt-rule margins sat near 0. The battery
  specification fixes the shapes, keeping every right answer at two digits;
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

  - **Extra letters chosen to fit** (RT-372, condition 1). The five extra rows are not drawn at random.
    They are chosen so that four common three-letter words can be spelled from the table's plain letters,
    which lets nearly every item be built and leaves no cue.
  - **Three different letters in every candidate** (RT-372, condition 2). Every wrong answer, like the
    right one, uses three different letters, so that a word such as "egg" cannot be ruled out without
    decoding.

  An item for which four such wrong answers of equal token length cannot be found is dropped at
  generation. The overlap script also checks, for every letter-code item, that each wrong answer is
  spelled only with the table's plain letters.

The wrong answers are of the same type as the right one, as listed above. That way, guessing without the
rule lands at chance.

**The routine kinds, enlarged** (RT-340, RT-341, RT-361):
- sums of two numbers from 2 to 49, with the halves split by answer value as section 5 sets out below;
- products of two numbers from 2 to 12, split the same way;
- capitals, from a list of at least 150 countries;
- opposites, from a list of at least 160 common adjectives (80 opposite pairs);
- everyday colours (RT-373, RT-384), from a list of at least 120 common objects with one typical colour
  ("The object is a ripe banana. What colour is the object usually?"), where the colour word never
  appears in the item. This kind replaces plurals. The list is written out in the battery specification
  before any item exists. Each entry names the object's typical colour and every other colour the object
  is commonly seen in (a green apple, a brown egg). Those other colours are never offered as wrong answers.
  An object whose typical colour differs by country, such as a fire engine, is left out. The spread of
  right answers across colours is reported.

**No routine question is used twice.** Under the 25% cap below, a cell of 300 pairs allows 75 questions
of each routine kind. **A multiplication counts once** (RT-407): "5 × 8" and "8 × 5" are the same question,
so only one order is used, and likewise for sums. Half B then holds about 75 or more sums, about 23 to 27
two-digit products (55 in all, split by answer value), 36 capitals usable as right answers (counted with
the generator and the real tokeniser, RT-399, RT-450), about 75 opposite questions and 61 everyday colours.
**How many pairs that allows depends on choice 8** (RT-450). With four rule kinds it is about 236. With the
letter-code kind dropped and the pairs shared equally among the other three, it is about 196 to 220,
depending on the products pool. With choice 8 as version 0.10 wrote it (operator 2 : unit 1 : lookup 1) it
was about 144. The arithmetic is in the tenth change log. The sample-size
simulation is expected to ask for about 120 to 200 pairs. If the filters leave fewer
pairs than the sample-size simulation needs, the design returns to John (RT-361). The closure check of
version 0.3 found that the simulation needs about 120 to 200 pairs.

The next-weekday kind is dropped, because seven days cannot be split into a practice half and a test half.
**No single routine kind may make up more than 25% of the routine cell**, so "routine" is not mostly
arithmetic. The cap applies to routine kinds only (RT-362). The prompt-rule kinds are kept as nearly equal
in number as the filters allow, whichever kinds John's ruling on choice 8 leaves, and their counts are
reported.

**Which rule goes with which routine question** (RT-365). A rule is never paired with a routine question
of the same type:
- the arithmetic rules (`p_operator`, `p_unit`) are never paired with sums or products;
- the word rule (`p_code`) is never paired with opposites;
- the colour table (`p_lookup`) is never paired with everyday colours.

The generator first applies the 25% cap and the pool sizes. Within those limits, it spreads the routine
kinds as evenly as it can across the rule kinds (RT-374). The value the rule would give if wrongly
applied to the routine question is never one of that question's candidates.

**One shared context, and two fixed final questions** (RT-370, RT-380, RT-381, RT-382). Two earlier
constructions failed. In version 0.3, routine questions ran longer than rule questions. In version 0.4,
the questions were the same length, but a rule question carried several tokens unique to its item
(operands, a symbol, invented unit names), while a routine question carried one. So its donor differed
from it at more places, and the routine cell took less swap. The cause in both cases was item-specific
content sitting in the final question, where the two twins differ. Version 0.5 moves all of it out:

- **The shared context.** Every pair's two items carry the same context, word for word. It holds three
  things:
  - the invented rule;
  - the rule's facts for this item ("Here a is 14 and b is 17.", "You have 4 zibvams.", "The coded word
    is qxv.", "The name to look up is tovjot.");
  - the routine fact ("The country is France.", "The word is happy.", "The object is a ripe banana.",
    "The two numbers are 23 and 31.").
- **The order of the three parts is balanced** (RT-394). In half of each group of pairs, the rule's facts
  come last, just before the final question. In the other half, the routine fact does. The rule itself
  always comes first. The order is assigned with a fixed seed, and results are reported for each order.
  **The by-order results are a report only and rename nothing** (RT-394). In a group with an odd number of
  pairs, the extra pair's order is set by the same seed. Donors are not required to share the order, which
  would roughly halve the eligible donors without changing the dose.
  The aim is that neither cell's needed fact always sits nearer the question than the other's. With the
  routine fact always last, the prompt-rule item's own fact ended 6 to 8 tokens further from the question,
  and a table 16 to 18 tokens further, as the fifth check measured.
- **Two fixed final questions.** The prompt-rule item ends with a fixed question that needs the rule, such
  as "What does the rule give for them?". The routine twin ends with a fixed question that does not, such
  as "What is the capital of the country?". **Neither question contains anything specific to the item.**
- **One wording for each pairing.** For each pairing of a rule kind with a routine kind, exactly one
  wording of each question is used for every pair, chosen once so that the two have the same token count
  under the model's tokeniser. Nothing is picked item by item, so there is no phrasing difference that
  varies between items (RT-382). The wordings are fixed in the battery specification.
  A routine kind can be worded differently behind different rule kinds (for instance "the capital of the
  country" against "the capital city of the country"), so results for each routine kind are also reported
  by wording (RT-397).

**Why this equalises the dose, and where it cannot.** Within a pair, the two items are the same text up
to the final question. Within a cell, every donor has the same final question as its recipient, because
donor pairs share the rule kind and the routine kind (section 3). So in both cells the donor and recipient
diverge at the same place, which is the first item-specific token of the shared context.
- **Inside the shared context, the doses are equal.** The model reads left to right, so at every position
  inside the shared context, both the true block sums and the replacement sums are the same in the two
  twins. Step 4a confirms that the model reads left to right.
- **After it, the doses may differ.** The real dose can differ between the cells only after the shared
  context: in the final question, the template's closing tokens and the candidate. The fifth check
  measured that this tail is 16% to 34% of the changed span, depending on the rule kind. There the two
  twins' block sums differ because their questions are different words, and no token count can say by
  how much.
- **On the stand-in measure,** the two cells came out at 0.998 to 1.019 in the fifth check. They are not
  exactly equal, because a donor's final question usually starts later than the recipient's (RT-390).

That remaining difference is RT-345, closed only by measurement at step 4b (RT-391).

**Every candidate is a single token** (RT-390). In version 0.5 a routine twin's right answer could run to
several tokens ("Buenos Aires", "Port-au-Prince"), while every prompt-rule answer was one token. So the
scored span was longer in the routine cell. Now every candidate of both twins must be one token, measured
at the answer position. Capitals, opposites and everyday colours that do not meet this are left out of the
pools.

**What the rule leaves, and what it costs** (RT-399). The sixth check counted with the real tokeniser:
- **Capitals.** Only about 90 of the world's capitals are one token at the answer position, and about 84
  after the copying rule. So half B can hold about 42 capitals, not the 55 version 0.6 said. *(The generator
  with the real tokeniser later found 36 usable in half B and 44 in half A, RT-450.)* Version 0.6's
  "82 of 105" came from a short list of famous countries, which is exactly the problem.
- **Opposites.** About 12% of adjectives are lost.
- **What is untouched.** Colours, three-letter words and numbers up to 999 all pass.

The cost falls on the capitals cell. The capitals that survive are mostly famous ones, mainly European and
Middle Eastern, and so are their close wrong answers. A famous capital among famous neighbours may be easier
to recognise than to produce, which is the worry RT-349 raised about choosing among five.

**Which way the cost points** (RT-408). If famous capitals stay recognisable after the removal, routine
losses are held down. That widens the gap the test reads, toward outcome A, the predicted pattern. So the
cost favours the prediction, and it is stated as such.

Capitals are kept on those terms, with these safeguards:
- **any outcome A is reported beside the reading with the capitals pairs left out, whatever that reading
  lands in**, including E. Section 6's renaming rule still renames only on a different definite outcome,
  but the capitals-out reading is always shown next to an A;
- step 3 reports the spread of right answers by region.

Margin matching is not a safeguard here. It acts on baseline margins, not on recognition after the
removal, and the earlier text that listed it as one is withdrawn.

The alternative the fifth check offered was to keep multi-token capitals and report results by candidate
length. It is not taken, because it would bring back the unequal scored span that RT-390 removed.

**The space before the answer** (RT-400). All of this assumes that no space comes before the answer, as in
the stand-in reply opening `<|message_model|><|content_text|>`. With a space, only about 23 capitals and no
numbers at all are one token. Step 4a settles the tokens before the answer. If they differ from what step 3
assumed, the pools and the pilot are rebuilt and the single-token counts redone before any pilot item is
scored.

**The operator's answers have two digits** (RT-399; narrowed in version 0.12, RT-465; version 0.13). Both
halves share one range of operands, set by the specification for the single-step shapes, so that every right
answer has two digits. Its candidates lie within five of the right answer, with the same number of digits.

**The wordings, checked with the real tokeniser** (2026-11-21, before this version was written). The
counts are of the fixed questions alone, with a leading space, from `tokenizer.json` at revision 657b53ba:

| Pairing | Prompt-rule question | Routine question | Tokens each |
|---|---|---|---|
| operator, capitals | "What does the rule give for them?" | "What is the capital of the country?" | 8 |
| operator, opposites | "What does the rule give for them?" | "What is the opposite of the word?" | 8 |
| operator, everyday colours | "What does the rule give for them?" | "What colour is the object most often?" | 8 |
| unit, capitals | "How many of the second unit is that?" | "What is the capital city of the country?" | 9 |
| unit, opposites | "How many of the second unit?" | "Give the opposite of the word." | 7 |
| unit, everyday colours | "How many of the second unit is that?" | "Usually, what colour is the object?" | 9 |
| letter code, sums | "What word is the coded word here?" | "What is the sum of the two numbers?" | 9 |
| letter code, products | "What word is the coded word?" | "What do the two numbers multiply to?" | 8 |
| letter code, capitals | "What word is the coded word?" | "What is the capital of the country?" | 8 |
| letter code, everyday colours | "What word is the coded word?" | "What colour is the object most often?" | 8 |
| lookup, sums | "What colour does the table give the name?" | "What is the sum of the two numbers?" | 9 |
| lookup, products | "What colour does the table give the name?" | "What is the product of the two numbers?" | 9 |
| lookup, capitals | "What colour does the table give the name?" | "What is the capital city of the country?" | 9 |
| lookup, opposites | "What colour does the table give the name?" | "What is the opposite of the given word?" | 9 |

Every pairing the exclusions allow has a matching pair of wordings. The invented-unit facts now sit in the
shared context, where both twins carry them, so their length no longer has to be matched by anything
(RT-381). The table may be revised in the battery specification, as long as each pairing keeps one
wording on each side with equal counts.

**What the shared context costs.** The routine twin now has to find a fact named earlier in the context
("the country") rather than read it in the question. That is a small step of reference, which section 1
states.

**Pilot and test are kept apart, and a script checks it** (RT-341). Every content pool, including the
operands and rule shapes of each prompt-rule kind, is split into two disjoint halves: half A for pilot
items with seed 1, half B for test items with a seed written in the registration. For the operator and unit
kinds, and for sums and products, the two halves draw from **the same operand ranges** and are split **by
the right answer's value, decade by decade, with each half given the same mix of last digits** (version 0.11,
RT-439, RT-451). Within each decade (10 to 19, 20 to 29, and so on), five of the ten values go to each half,
so that each half gets one of the two values ending in 0 or 5, two of the other even endings and two of the
other odd endings.
- **The round values alternate** (version 0.12, RT-460). Which half gets the value ending in 0 alternates from
  decade to decade, starting with a half drawn by the seed, so neither half collects the round numbers. The
  other four values of each half are drawn by the seed within the rule above.
- **The halves are matched on items, not only on values** (RT-460). For each kind, both halves are built and
  these figures computed over their items, before any item is scored. The split is accepted only if, within
  each kind:
  - the shares of items whose answer ends in 0, and in 5, differ between the halves by at most 0.05;
  - the mean answers differ by at most 2;
  - the shares of even operands differ by at most 0.05;
  - for the unit kind and products, the number of distinct facts in the smaller half is at least 80% of
    the larger.
- **The seed rule** (RT-460). Seeds are tried in order from 1, and the first whose split meets every tolerance
  for a kind is used for that kind. All of this is computed from the lists, without the model, and the
  chosen seeds are committed with step 3. If no seed up to 1,000 meets them, the design returns to John.
  Version 0.11's draw matched the halves only on the grid of values; the closure check of version 0.11 found
  that in about one seed in ten one half then had more than a quarter more of its products or unit items on
  round numbers.
- **Why not bands of five.** Version 0.10 gave half A every answer whose value divided by five was even.
  That gave half A every answer ending in 0 to 4 and half B every answer ending in 5 to 9. Half A then held
  every product ending in 0, the easiest case, and a right answer ending in 0 was the only round number
  among its candidates. The pilot could not see answers ending in 5 to 9 at all.
- **Why not by size.** Until version 0.9 the halves were split by size: test-half operator answers ran from
  100 to 999 against 10 to 45 in the pilot, so the pilot could not forecast the bites check's one-pass
  condition, which decides whether any outcome is readable.
- **The ranges.** Every right answer has two digits. The operator kind's operands and constants are set in the
  specification for the single-step shapes (version 0.13; RT-493, RT-497). The
  unit kind uses a factor of 2 to 9 and a count of 2 to 12. **That is harder than the trial measured**
  (RT-464): the trial's unit items used a factor of 2 to 5 and a count of 2 to 9, and 55 of the new range's
  81 facts lie outside that, with a mean answer of 40 against 22. So every unit figure this design quotes
  from the trial, and the survivor estimates of choice 8, were measured on easier problems. The rebuilt
  pilot measures the real figures. The narrower range would leave too few facts per half (about 13).
- **What step 3 reports.** The figures behind each tolerance above, by kind and half, and the seed chosen.

A committed check script fails if any pilot prompt or table appears in the test set, or if any answer value
of one kind appears in both halves of that same kind (RT-452). **For the operator kind, the split key is
the shape and its operands together, which fixes the answer**, not the operand pair alone, because the
same operands give different answers under different shapes. **Numeric wrong answers are exempt** from the
half check, including the check on half-A candidates below, because a wrong answer within five of the right
one usually lies in the other half's values; only right answers are split. The script, `src/check_overlap.py`, is rewritten for this split before step
3, which lists it. Answer values are compared within each kind, because a
number can rightly be both a unit answer and a sum (RT-341). **Colours are exempt from the answer-value
check** (RT-383). The lookup kind and the everyday-colours kind answer from a small closed set of colour
names, too few to split into two halves. For those two kinds the check applies instead to what varies:
the invented words and tables of the lookup kind, and the objects of the everyday-colours kind. No object
or invented word may appear in both halves. The script also fails if any test item's
non-numeric candidate comes from a half-A pool. **The colour names are one shared pool**, used by both halves and
exempt from that rule as well, because they cannot be split (RT-396). It runs before the test set is used.

**Baseline checks** (at three passes, nothing removed):
- **The rule is needed:** with the rule sentence removed, accuracy on that prompt-rule kind is no better
  than chance plus 0.10. A kind that fails is dropped whole.
- **The rule is learned, and the item is confident** (RT-347): the margin, meaning the right candidate's
  log-probability minus that of the best wrong candidate, is at least 2.2 (about 90% when only those two
  are compared).
- **The rule does not get in the way of the routine question** (RT-365, RT-374, RT-393, RT-402; judged by
  accuracy since version 0.13). A routine twin is **interfered with** if it is answered right when given
  **only the routine fact and its final question**, with the rule and the rule's facts left out, and wrong
  with the full shared context. "Right" means the right candidate alone has the highest probability. A tie
  counts as not right here, because the tie rule's shares are for scoring, not for this check. Version 0.12's
  limit of 1.0 in margin struck every pairing at step 4b, because this model's margins run near 10: a routine
  answer whose margin falls from 12 to 9 is still right every time. ("The same question with no preamble", as
  version 0.5 put it, cannot be answered under the shared context.)
  - **A whole kind.** A routine kind is not paired with a rule kind if more than a fifth of that pairing's
    routine twins are interfered with. **The fifth is counted from the pairs whose routine twin is right
    without the rule**, not from the confident pairs as before (RT-402). A confident item is always right,
    so a count over confident pairs could never find an item that turned wrong, and the rule would be empty.
  - **Single items.** An interfered item is wrong in the full context, so it already fails the confidence
    check and its pair is dropped.
  - **On the step-4b pilot** (descriptive, version 0.12's operator kind). Under this rule, every lookup and
    unit pairing survives. The interfered shares are 0 for lookup with sums and with products, 0 for unit
    with capitals and with opposites, and 0.15 for unit with colours. All three operator pairings are struck.
    The routine side is worst for everyday colours behind the operator rule: 6 of 13 interfered.
  - **When it is fixed.** The resulting table of which routine kinds go with which rule kinds is fixed on
    the pilot items, at step 4b, and written into the registration before the test set is generated.
  - **What it can show.** The check works at baseline only. It cannot show that the removal leaves the
    ability to ignore the rule intact, as section 1 says.
- **The routine fact does not get in the way of the rule** (RT-393, RT-402; judged by accuracy since version
  0.13). This is the mirror check. A prompt-rule item is **interfered with** if it is right when given only
  the rule, the rule's facts and its final question, with the routine fact left out, and wrong with the full
  shared context. Under the shared context the prompt-rule item also has to ignore an irrelevant sentence, so
  it gets the same check. Its rules, written out:
  - **A whole pairing.** If more than a fifth of a pairing's prompt-rule items are interfered with, that rule
    kind is not paired with that routine kind. The fifth is counted from the pairs whose prompt-rule item is
    right without the routine fact.
  - **Single pairs.** An interfered item already fails the confidence check, so its pair is dropped.
  - **When it is fixed.** It feeds the same pairing table, fixed on the pilot and written into the
    registration.
- **Strike counts reported first** (RT-402). Before the pairing table is fixed, step 4b reports, for each
  pairing and each of the two checks, how many pilot pairs were right without the other half and how many of
  those were interfered with. Beside them it reports the margins with and without the other half, as a
  description. It also reports, for each pairing, the items that stayed right but fell below the confidence
  bar when the other half was added (RT-495). The accuracy rule does not count them, and the reader should
  see them. A pilot pairing has about 13 to 20 pairs at the pilot's allocation. If the two checks together
  would leave fewer than three rule kinds, or would leave any rule kind with one routine kind or none, the
  design returns to John before the table is fixed (RT-402).
- **A pairing needs pairs to count** (version 0.14, RT-485; the number is the author's choice). A pairing
  with **fewer than three pilot pairs that pass the confidence check** is struck, whatever the interference
  checks find. So is a pairing whose counting base is empty. Without this rule, a pairing whose items are
  almost all unconfident could pass both checks with no item to fail. It would then count as a surviving
  routine kind with no pair to score, and the "one routine kind or none" return to John would be bypassed.

**All matching acts on whole pairs, within each rule kind** (RT-359, RT-360). Nothing in the matching
removes a single item and leaves its twin behind, because the analysis resamples by pair.
- **Margin.** A pair is kept only if both twins pass the confidence check. Then, within each rule kind,
  whole pairs are dropped until the mean margins of the two cells are within 0.5 of each other. The pairs
  dropped are those whose difference between the routine twin's margin and the prompt-rule item's runs
  **in the direction of the imbalance**, largest first (RT-375). The rule is mechanical and has a fixed
  seed for ties. The margin distributions of the two cells, before and after, are reported.
  - **No margin fallback** (RT-386). Version 0.4's fallback always removed more pairs than plain
    matching, so it could never rescue a kind, and it is withdrawn. If matching the means would remove
    more than a third of a rule kind's pairs, on the pilot or on the test pairs, the design returns to
    John. The third is counted from the pairs that pass the confidence check.
- **Swap size** (RT-345). Then, within each rule kind and **for each method**, whole pairs are dropped until
  the two cells' mean swap sizes are within 10% of each other. "Within 10%" means that the routine cell's
  mean divided by the prompt-rule cell's lies between 0.90 and 1.10, the same form as the step-3
  threshold (RT-389). The pairs dropped are those whose
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

**The bites check, not in the outcome** (RT-354; task replaced in version 0.9):
- **K, held-out rule problems.** Problems of the operator and unit rule kinds, built exactly as the
  prompt-rule side of a pair is built (the rule sentence, the shared context with its routine content, the
  final question, the instruction), but scored on their own. Their routine twin is not built and nothing
  from them enters the outcome. They are drawn from the same half as the set they serve (the split by answer
  value above), from their own random stream.
- **What is kept apart** (RT-440, narrowed in version 0.10). No bites item repeats a scored pair's or a
  donor's whole content, that is its rule, its facts and its routine content all together. Numbers and
  answers may repeat. Each item is scored in its own run with nothing carried between items, so a shared
  number leaks nothing. What must stay apart is the two halves, and the half split ensures that. Version 0.9
  kept numbers apart too, which half A's unit kind could not supply under version 0.9's ranges: it had 32
  combinations of factor and count, and the pilot's scored pairs already used 19.
- **Repeated facts** (RT-455). With a factor of 2 to 9 and a count of 2 to 12, each half holds about 26 to
  29 distinct facts for the unit kind (the build report's count; RT-497). Those serve the unit bites items and the test half's unit
  pairs, so each fact is used several times. Items that share a fact are not independent. So, within the
  unit kind, intervals are resampled **by fact**, not by item or pair, by the scheme set out in section 6,
  and the number of distinct facts per kind is reported. Widening the range to repeat facts less would make the unit problems harder than the
  trial measured, which is the trade the range above accepts.
- **Donors** (RT-443). Each bites item gets five donors among bites items of the same rule kind and routine
  kind, with donor-only bites items added on the terms of section 3. The pair donor rule's conditions apply
  to the single item: the donor must be at least one token longer, and its right answer must not be among
  the item's candidates.
- **No filters** (RT-443). Bites items do not pass through the confidence filter or the two baseline checks.
  Every bites item is kept and scored. Filtering on confidence at three passes would inflate the one-pass
  cost measured on them, because it selects items the full model gets right. The reading on the bites items
  that pass the confidence filter is reported beside it, as a description.
- **If the simplified operator kind no longer gains enough from the passes** (version 0.13). John's ruling
  simplifies the operator kind to a single step. A simpler rule may gain less from the extra passes, and the
  bites check relies on that gain. The rule, fixed now:
  - At the step-4b rerun, the operator and unit bites items' one-pass costs are measured on the pilot. **The
    rerun pilot carries 40 operator and 80 unit bites items** (version 0.14, RT-490), so that either branch
    below can be read from one rental.
  - **The committed simulation chooses the branch** (version 0.14, RT-489; the author's choice, replacing
    version 0.13's cut at 0.15). Using each kind's measured one-pass cost and spread, it computes whether the
    three bites targets of "The size" are reached at 100 items a kind with both kinds, and at 200 unit items
    with the unit kind alone. Both kinds are used if they reach the targets. Otherwise the unit kind alone is
    used, if it reaches them. If neither branch reaches them, the design returns to John before registration.
    A cut at 0.15 would have been a near coin flip on 40 pilot items. Keeping a kind just above it would also
    have made outcome F unreachable, because the kind's own-loss interval would then need an upper end below
    about 0.04.
  - **The unit-only branch is expected to need John.** With 200 items resting on about 29 facts, the closure
    check's rough sketch reached the one-pass condition in about 47% of simulated sets, short of the 80%
    target.
  - Whichever branch is taken, the per-kind conditions of "does not bite" apply to the kinds in the bites
    set. The operator kind stays in the cells as a prompt-rule kind either way.
  - With unit items only, the bites set's effective size is bounded by half B's unit facts, about 29, because
    the unit kind is resampled by fact. The simulation must still reach its 80% targets for the bites
    conditions (section 5, "The size"). If it cannot, the design returns to John before registration.
- **Why these two kinds.** In the scoring trial, with the instruction, counting items (RT-441):
  - the operator kind was right on 11 of 30 at one pass and 22 of 30 at three with the instruction at the
    start (37% and 73%), and 13 and 22 of 30 at the end (43% and 73%);
  - the unit kind was right on 17 and 25 of 30 at the start (57% and 83%), and 15 and 28 of 30 at the end
    (50% and 93%);
  - the letter-code kind was at chance at every number of passes (2 to 6 of 30);
  - the lookup kind was right on every item from one pass, so it cannot show a cost from fewer passes.

  These are pilot figures, used to choose the task. Version 0.9 quoted plain averages of the routine-kind
  groups, which weight a 7-item group like a 12-item one; the figures above count items. The check itself is
  made on half B, which version 0.12 splits from half A so that the two match item by item within fixed
  tolerances (RT-439, RT-451, RT-460).
- **Why not chained lookup.** Version 0.8 used the task Thinking Machines describe, following a chain of
  two to six lookups through invented tables. On the pilot it was at chance at every number of passes. A
  trial of four easier versions, down to eleven rows with familiar one-word names, found even two-step
  chains at chance, while a one-step lookup is right every time
  (`experiments/10-loop-removal-test/chain-calibration-findings-2026-11-21.md`). Answering at once, this
  model does not compose two lookups at all, so chained lookup cannot show whether a removal takes away what
  the passes supply.
- **How many.** 100 bites items of each of the two kinds in the test half, 200 in all, and 40 of each in
  the pilot. The simulation set out below may raise this (RT-442, RT-453).
- **The one-pass run must cost it.** Fewer passes must cost the bites items margin, compared with three
  passes, **with the interval's lower end at or above a quarter of C** (version 0.16, section 5; the interval
  was added in version 0.11, RT-453, and version 0.10 used the point estimate alone). **Gate decisions use 100,000 resamples**, and where the
  decision lies within 0.005 of its threshold, the spread of the interval's end over 20 resampling seeds is
  reported beside it (version 0.14, RT-492). At step 4b the pooled lower end passed by 0.0003 on one seed,
  and on 9 of 20 seeds. Otherwise the setup is wrong, and the result is not testable. The
  0.15 is this design's own choice (RT-355). On the pilot, with the instruction, the two kinds together
  rose by about 0.3 in raw accuracy from one pass to three, about 0.4 on the normalised scale, so the
  threshold is expected to be met but is not assumed. **This condition gates every outcome** (RT-444): if it
  fails, the result is not testable (section 6, stage one).
- **The main removal must bite, beyond generic damage** (RT-367). Under each method, the main removal's
  loss on the bites items **minus the random comparison's loss** on the same items
  must be at least half of what the one-pass run costs it, with that excess's interval above zero. This
  is **"the removal bites"**. Measuring against the random comparison stops generic damage of the same size
  from passing the check.
- **The removal does not bite** (version 0.11, RT-449; rewritten in version 0.12, RT-457, RT-459, RT-461).
  All of the following, under each method:
  1. **Its own loss is small.** The main removal's loss on the bites items, measured against the unaltered
     three-pass run, has an interval whose **upper end is below a quarter of the one-pass cost**. Here the
     one-pass cost is the point estimate on the same bites items (RT-453). Version 0.11 asked only that the
     loss beyond the random comparison be small. A swap that cost the problems as much as the passes supply
     could then pass whenever matched random noise cost as much too, and F would have said the opposite of
     what happened (RT-457). With this condition, the excess is small as well.
  2. **In each of the two kinds** (RT-461). Condition 1 holds for the operator bites items and for the unit
     bites items separately, each against its own one-pass cost. If it holds pooled but not in one kind, the
     outcome is **Depends on one kind**, with the kind named.
  3. **The message was changed** (defined in version 0.12, RT-459). For each bites item, take every position
     from the first position where the item and its donor differ, through the answer position. Version 0.11
     counted every position, and about 41% of them, the template, the instruction and the rule's opening
     words, are identical between item and donor at the recommended placement, so the threshold was almost
     out of reach. At each position, for each of the two block sums the readers read, and on passes 2 and 3,
     scale the true sum and the given sum each to a root-mean-square of 1, as the readers' normalisation does
     before its learned weights. Take the distance between them divided by the true sum's length, which is
     about the square root of the width. The item's **change ratio** is the mean of that over its positions,
     both block sums and both passes. Under the average method the given sum is the average. **F needs the
     mean change ratio over the bites items to be at least 0.5 under each method.** That is a message about
     half its own size away from the true one, on average. The 0.5 is this design's own choice, fixed now.
     Without it, a swap between very similar inputs could change little and read as "the content does not
     matter". The spread over items is reported beside the mean.
- **Whether F can be reached is known before any test data** (RT-459). Step 4b reports the pilot's change
  ratio under each method, with its spread. If the pilot's mean is below 0.5 under either method, the design
  returns to John before registration. The threshold is not changed after seeing it.
- **Between "bites" and "does not bite"**, the removal is **too weak to read**.
- **Which outcomes each condition gates** (RT-444, RT-453). The one-pass condition gates every outcome. "Bites"
  and "does not bite" decide D, F and the disagreement rule (section 6).
- **The size** (rewritten in version 0.11, RT-453; version 0.12). The committed simulation finds the smallest
  number of bites items giving at least an 80% chance of each of these, fixed now:
  - "bites", when the true excess is three quarters of the one-pass cost;
  - "does not bite", with all three of its conditions, when the removal's true own loss is zero in both
    kinds and the change ratio is the one step 4b measures;
  - the one-pass condition, when the true one-pass cost is the one step 4b measures.

  200 bites items are expected to be enough; the closure check of version 0.9's simulation found "bites" at
  three quarters reached at 80 items.
- **What this replacement costs** (version 0.9; rewritten in version 0.10, RT-437). The bites task is no longer a different kind of task from
  the cells. It is the same two kinds of problem as half of the prompt-rule cell, asked in the same form.
  So the bites check and the prompt-rule cell's loss are no longer independent. A removal that bites the
  bites items would be expected to cost the operator and unit pairs of the prompt-rule cell too. Two things
  follow:
  - **Outcome D loses its reading.** When the bites check passes, the removal has been shown to cost
    operator and unit problems. D would then say it cost neither cell of the pairs more than the comparisons
    did. That cannot mean "the model does not need this input's feedback", which version 0.9's section 7
    still said, because the bites check has just shown that it does. D can be reached in three ways, none of
    which bears on H1:
    - the bites items and the pairs' operator and unit items differ by chance;
    - the lookup pairs, which are right from one pass and have little to lose, dilute the prompt-rule cell.
      On the trial's figures they would be about half of the filtered cell (RT-438), so a removal that cost
      only operator and unit items would show about half its effect in the pooled cell;
    - the scored pairs pass the confidence filter and the bites items do not, so the cell holds the items
      hardest to knock over.

    The "depends on one kind" rule does not apply to D, so none of these is caught. So, from version 0.10,
    **D is reported under the name "No excess in the cells", with no reading**, while the bites items share
    kinds with the prompt-rule cell (sections 6 and 7). The prediction can still fail through B or C, and
    since version 0.11 through F, which reads the plainest failure: the passes help, the message was changed,
    and a message from other inputs serves as well. What D's loss of reading costs is the case where the
    removal bites the held-out problems but the pairs show no excess, which cannot be read either way.
  - **Outcome A is not helped by it.** A and B are read from the cells as before. A large loss on the bites
    items does not count toward A.

  A different task, of another kind and measured to need the passes, would avoid this cost. None is known
  for this model: the trials so far found a pass gain only on the operator and unit kinds. The closure check
  of version 0.9 weighed the cost against stopping the test and judged it worth keeping.
- **The pass gain runs in opposite directions by kind** (RT-445). From one pass to three, in the scoring trial
  with the instruction at the start (at the end in brackets): operator prompt-rule items gained 0.37 (0.30) and
  their routine twins 0.00 (0.10); unit items 0.27 (0.43) and their twins 0.00 (0.03); lookup items 0.00
  (0.00) and their twins 0.27 (0.37). If what the passes supply is what the removal takes away, the operator
  and unit pairs lean toward A and the lookup pairs toward B. A pooled result may then land in C, E or
  "Depends on one kind" for a reason the trials already show. This does not favour A.
  - **Where the routine gain sits** (RT-445). Behind the lookup rule, the capitals twins were right on every
    item from one pass and the opposites twins on 75% to 100%. The routine gain came from sums (from 14% to
    29% at one pass to 100% at three) and products (from 57% to 100%). So the gain belongs to two routine
    kinds, not to a rule kind.
  - **The simulation** draws its effects by rule kind and by routine kind, not as one shared gap.
- **A risk to the three-kind rule** (rewritten in version 0.10, RT-438). A pair stays only if both twins pass
  the confidence filter. In the scoring trial, at three passes, these prompt-rule items passed it (with the
  instruction at the start, then at the end, of 30 each):
  - operator: 8, then 12;
  - unit: 23, then 24;
  - letter code: 1, then 1;
  - lookup: 30, then 30.

  The closure check of version 0.9 derived from these about 7 (start) or 9 (end) whole operator pairs, about
  22 unit pairs, 1 letter-code pair and 29 lookup pairs. So **the operator kind is at risk as well as the
  letter code.** Its pairings hold 7, 12 and 11 pilot pairs, so two of them may keep one or two pairs each,
  and a single baseline-check failure then strikes the pairing. The strike-count rule above then leaves the
  operator kind with one routine kind or none, and the design returns to John. With four kinds, about half of
  the test half's pairs would pass the filter, at the bottom of the 120 to 200 the sample-size simulation
  is expected to ask for (choice 8 gives the figures). The surviving prompt-rule cell would be about half lookup, a third unit, a tenth
  operator and almost no letter code (with four kinds as now).
  - **What is done about it now:** choice 8 (section 10, revised in version 0.11) asks John whether to drop
    the letter-code kind and share its pairs equally among the other three. Choice 6 shows the operator's
    cost of each placement.
  - **Where the operator's survivors sit.** Whole operator pairs pass the filter at 71% with capitals, 13%
    with opposites and 5% with everyday colours at the start placement (71%, 7% and 29% at the end). So the
    operator kind survives mainly on its capitals pairing, and its colours pairing is often empty. Losing two
    pairings leaves it with one routine kind, which returns the design to John.
  - **What is done if the rebuilt pilot confirms it:** the rule stands. If step 4b leaves fewer than three
    rule kinds, or any rule kind with one routine kind or none, the design returns to John before the
    pairing table is fixed. No threshold is loosened to keep a kind.

**Sample size** (RT-340). The analysis is paired: the same items are scored under every condition, and
differences are resampled by the scheme of section 6 (by pair, and by fact within the unit kind; RT-462). The number of pairs is fixed in the rehearsal by a committed
simulation. It uses the measured spread, the measured loss of the random comparison and the five-donor
averaging, and finds the smallest number giving at least an 80% chance of classifying a true normalised gap
equal to the target of choice 9 (in units of C; version 0.16, RT-511) as outcome A **after every check in
section 6 that can rename an A**, including the readings with
one kind left out, with both methods (RT-363). The first review's simulation found that about 120 items per
cell is enough for a bare A when the comparison's own loss is about 0.10 or less, and that about 200 are
needed when it is 0.20. The closure check of version 0.2, with the leave-one-kind-out rule as version 0.2
wrote it, found the chance of a clean A falling to 0.45 to 0.76 at those sizes. The closure check of
version 0.3, under that version's narrower rule, found 80% reached at about 120 pairs (comparison loss
0.10) and about 200 pairs (0.20). Version 0.4 changes the rule again (section 6) and adds routine kinds to
it. So the committed simulation must be run under the rule as written here, with both rule kinds and
routine kinds left out in turn. If a rule kind is dropped, the simulation is re-run with the kinds that
remain. Half B can supply at
most about 196 to 236 pairs before filtering, depending on choice 8 (above, RT-450), of which about 130 to
150 are expected to pass the confidence filter under the revised choice 8. That is inside the expected 120
to 200, but near its lower end. **If the simulation asks for more pairs than
survive the filters, the design returns to John.**

**The simulation's conditions** (RT-340). The committed simulation uses the spread and the comparison loss
measured at step 4b, in the margin units of section 5 (version 0.15). On step 4b's data, a true gap of 0.20
spread evenly was read as A in 94 to 96% of runs at 80 pairs, and 98 to 100% from 140 pairs. The scenario
with the gap on the operator and unit pairs only could not be judged on that data, because no operator
pairing survived there. It is run on the pairs that survive every filter, after the confidence, margin and
swap-size steps and the pairs dropped for want of a donor. If a rule kind is dropped, it is run again with
the kinds that remain.

**The pilot's size** (RT-389). The pilot set has 120 pairs, 30 for each rule kind (40 for each of three if
John rules for choice 8), generated from half A
with seed 1, plus 80 bites items (40 of the operator kind, 40 of the unit kind; version 0.9) and the 200
neutral passages of half A. Every limit in this
section that is applied to pilot pairs is applied to these: a fifth of a kind in the "answered as well
behind its rule" check, a third in margin matching, and a tenth in swap-size matching. The fifth of the
interference checks is counted from the pairs right without the other half of the context (version 0.13; the
wording here was stale until version 0.14, RT-497). The third and the tenth are counted as their own
paragraphs above say (RT-465).

**The neutral passages carry no instruction** (RT-447). They are prose, not questions, and they serve as
the source of the average and as the reference for damage. The instruction is part of the items, not of
what the swap or the average replaces. In the reply rendering, the fixed request before the prose is part of
the fixed opening (section 4, version 0.14), not of the prose. It is not the items' instruction.

**Neutral set** (RT-335, RT-376). The new neutral set has 400 passages of ordinary prose, 200 in each half.
In the half in use, 100 build the average and 100 measure damage (section 3). For the average they are
rendered in the user's turn with every template token the items use (section 3). For damage and perplexity
they are rendered as the model's reply (section 4, version 0.13). Their lengths are spread across the items'
range up to the longest item, and they are drawn from two disjoint halves like everything else. It replaces the split test's
17-to-23-word passages for every use in this design: the average method, the damage matching and the
normal-range bound. **At step 3, once the model's own chat template and tokeniser are in hand, the check
that every position of every pilot item, candidates included, has a defined average is run again and
committed** (RT-335, condition 3).

## 6. The outcomes: every case lands in exactly one

These rules are the split design's (its section 5), with its template checks removed. That design's
template checks asked whether its result came from the chat format's role headers. Nothing here turns on
who is speaking, so they have no counterpart, although the chat template is still used to present the items
(RT-352). **δ is choice 9's value**, in units of C (section 5; version 0.16). Intervals are 95%, from paired resampling (10,000
resamples, seed fixed in the registration). **The resampling scheme** (RT-462): resampling is done within
each rule kind. In the unit kind the unit of resampling is a multiplication fact, taking together every
pair and every bites item that uses it. In the other kinds it is a pair, and each bites item alone. The
sample-size simulation uses the same scheme, and it **models the bites items and the cells together**: the
bites items share two kinds and many facts with the prompt-rule cell, so their results are drawn with that
correlation, both for the chance of an A surviving every rename and for the chance of F.

For each method, on the R and P cells:
- **R**, the excess loss on routine questions: the main removal's loss minus the random comparison's;
- **P**, the excess loss on prompt-rule problems, computed the same way;
- **G = P − R**, the gap.

**Stage one: is the result readable?** It is **not testable** if:
- the identity check or the bypass check fails (section 3); or
- the one-pass run does not cost the bites items (section 5); or
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
4. **D or F, no excess in the cells.** R and P both have intervals whose upper ends are below δ. Then:
   - if the removal **bites** (section 5), the outcome is **D**, reported as **No excess in the cells**, with
     no reading while the bites items share kinds with the prompt-rule cell (RT-437);
   - if the removal **does not bite** (section 5), the outcome is **F. The replacement does not bite**
     (version 0.11, RT-449);
   - otherwise it is **Too weak to read** (RT-354).
5. **E. Unresolved.** Anything else.

**The cells and the bites check disagree** (version 0.11; narrowed in version 0.12, RT-458). If the pattern
is A or C, the removal **does not bite** on the held-out problems, and **the pairs of the prompt-rule cell
whose rule kinds are in the bites set (operator and unit, or unit alone; version 0.14, RT-488), read on their
own, have an excess whose interval lies above zero**, the outcome is renamed
**Cells and bites check disagree**, with no reading. Those pairs are the same two kinds, in the same form, as
the held-out problems, so a loss on them with none on the held-out problems points to something other than
the message, such as chance or the filters. This rename is applied before the checks below.
- **Not B.** A B has no excess on the prompt-rule problems, so a removal that does not bite the held-out
  problems agrees with it. Version 0.11 renamed exactly that coherent B and kept the B where the two pulled
  against each other.
- **Not when the loss sits elsewhere.** An A or C whose prompt-rule loss sits on the lookup pairs, about half
  of the surviving cell, does not contradict the held-out operator and unit problems. "Depends on one kind"
  is the rule built for that case.

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

  - **A smaller leak that remains, reported beside any A** (RT-371). If one kind carries most of the effect
    and the others a little, the reading with that kind left out can land in E, which does not rename. The
    closure check of version 0.4 measured this at about a fifth of such A results at 120 pairs, falling to
    2% at 300. It is a trade made on purpose in version 0.3. Any A at the smaller sizes is reported with
    this sentence beside it.

  This rule is fixed here, before any data.

C, D, E and F are never renamed by the checks that apply only to A or B (RT-465). The readings with one kind
left out ignore the bites check, so F cannot arise in them; "no excess" counts as D there, as above.

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

Every sentence below is about margin, the model's confidence in the right answer among five fixed choices,
and is reported with the share of right answers beside it (version 0.16, RT-508).

| Outcome | The sentence it is reported in | What it means for H1's prediction |
|---|---|---|
| **A** | "In [model], at 16-bit, replacing the loop's message with one built from other inputs lowered the model's confidence in the right answer (its margin among five fixed choices) more on problems solved from a rule in the prompt than on routine questions behind the same rule, beyond matched comparisons, with both methods agreeing." | **The prediction held for this placement** in this model. It does not show experience or a workspace. |
| **B** | "...cost more on the routine questions than on the prompt-rule problems..." | **The prediction failed for this placement** in this model. |
| **C** | "...cost both alike, beyond matched comparisons..." | **The prediction failed for this placement.** The feedback behaves like an essential part, which shows nothing selective. |
| **D**, reported as "No excess in the cells" | "...cost the held-out [operator and unit / unit] problems beyond matched comparisons, but cost neither the routine questions nor the prompt-rule problems of the pairs more than matched comparisons. The held-out problems share [two kinds / one kind] with the prompt-rule cell, so this gives no reading." (The bracketed words name the kinds actually in the bites set; version 0.14, RT-488.) | **No reading** (RT-437). Never reported as the prediction failing or holding, and never as "the model does not need this input". |
| **F** | "...the extra passes helped the held-out [operator and unit / unit] problems, but replacing the loop's message with one built from other inputs, which differed from the true message on average by at least half its size, cost them little[, in each kind], and cost neither cell of the pairs more than δ beyond matched comparisons." (The bracketed words name the kinds in the bites set; version 0.14, RT-488, and the specification's reading of RT-471.) | **The prediction failed for this placement** in this model (RT-449): what the extra passes supply on these problems does not depend on this input's own message. It is not reported as "the model has no workspace". |
| **E**, methods disagree, not testable, too weak to read, cells and bites check disagree, not specific, specificity not checked, depends on one kind | Reported under its name, with the reason. | **No reading.** Never reported as the prediction failing or holding. |

**The precision is named in every outcome sentence** (RT-446, choice 7). The sentences above are written
for the main model run at 16-bit, as "[model], at 16-bit". If John rules otherwise on choice 7, the words
change to match.

**How the fewer-passes runs are read beside the main result** (RT-353). They are descriptive. One sentence
is allowed in advance. It belongs to outcome F (RT-449): with F, the
report may say "what the extra passes supply on these problems survived a message built from other inputs
of the same kind, which differed from the true one on average by at least half its size".
It is not used with D, where the removal has been shown to bite. Nothing about "computing" is allowed, because in this model passes without a message add nothing.

**What would count against H1 itself.** Not this test alone. It would need independent evidence that the
loop is this model's shared workspace, and then outcome B, C or F. No such evidence exists, and this design
does not claim any.

## 8. The models, and what it would cost

- **Main model:** TML-d24-varloop-research. Every condition runs on it, and only its result has an outcome.
- **Second model, descriptive only** (RT-351): Inkling 2 Mini, which always runs three passes. It has no
  one-pass setting, so it cannot pass the bypass check or the one-pass half of the bites check. It runs at
  whatever precision it can be loaded in, which is stated beside its result (RT-446). Its result
  is therefore reported with the same statistics, labelled descriptive, with no outcome. It still gets its
  own noise floor, identity check, baseline checks, matching, normal-range bound and damage matching.
  Both models come from one maker and share pretraining, so a result on both is close to one result twice
  (RT-357).
- **The machine.** This Mac has 16 GB of memory and cannot run the model, so every step from 4a onwards
  needs a rented machine. The card names cards of at least 32 GB from NVIDIA's newest generation (the RTX
  5090 and the RTX PRO 6000 Blackwell). The model's 4-bit format could not be loaded, so at step 4a it ran with its
  weights unpacked to 16-bit, using 49.2 GB with a peak of 50.9 GB, on a 96 GB RTX PRO 6000 (RT-337, RT-448).
  A 32 GB card cannot hold it. Under the standing rule, heavy runs go to RunPod.
- **What the work amounts to** (RT-343). Counted on the main model, the conditions on task items are:
  - the unaltered run, twice, for the noise floor;
  - the main removal under two methods, with five donors each under the swap;
  - 20 random draws and 20 outside-the-loop draws for each method, so 80 runs;
  - the one- and two-pass runs, the identity check and the bypass check;
  - the baseline runs without the rule sentence;
  - the bites check under every condition that needs it.

  That is about 100 runs of the item set, plus the search over noise size for damage matching, done on
  the neutral set. Each run scores a prompt with each of its five candidates, with no long generation. On
  roughly 800 items (300 pairs and 200 bites items), plus one unaltered run of each donor-only item, that is
  about 85,000 forward runs for the main model (RT-448). Step 4a settled that all five candidates are single
  tokens scored from one run of the prompt, so the count is per item, not per candidate (RT-369). At step
  4a's speed, about 65 seconds per 280 items, that is roughly five to six hours of card time before damage
  matching. Two caveats: the 65 seconds was timed on unaltered runs, and the swap's runs also record and
  inject block sums, which were not timed; and the count assumes each donor's block sums are recorded once
  and kept, without which the swap's runs double. The count rests on 300 pairs; under choice 8 as revised it
  is nearer 200 pairs, which lowers it. The second model adds about half that again. **No price has been looked up.** The count is made again from the committed code
  before any estimate goes to John.
- **Reused code:** the paired-resampling analysis from the split design. The battery generators are
  rewritten (section 5). New code covers the loop hooks, the candidate scoring, the per-item swap size and
  noise scaling, the bites-set generator, the neutral set and the overlap check.

## 9. Order of work

1. **The closure check** of this version by a session that did not write it, working in its own empty
   scratch folder with the real tokeniser and the committed results of the three rented runs. It checks
   version 0.15's change of the outcome measure to the margin, and the scale and thresholds that carry it. It cannot close RT-345, whose decisive check
   needs the model (step 4b). $0. *(The closure check of version 0.8 found it ready for the battery
   specification. The closure checks of versions 0.9, 0.10 and 0.11 did not. The closure checks of
   versions 0.12, 0.13 and 0.14 did. Version 0.15 changes the outcome measure to the margin, on John's
   ruling.)*
2. **John's rulings.** Choices 1 to 5 were ruled on 2026-11-21, choices 6 to 8 later the same day, and the
   three questions after step 4b on 2026-11-23 (section 11). Further rulings are asked for where a return-to-John rule in sections 4 to 6 fires. $0.
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
   - **What this threshold now is** (RT-390, RT-391). Under the shared-context construction, this estimate
     and the next can only check that **the generator builds what section 5 describes**. A correct build
     gives about 0.99 to 1.03, not exactly 1, because donors' final questions start later (the sixth
     check measured 0.996 to 1.001). These estimates
     cannot forecast RT-345, because the remaining risk lies where the stand-in measure sees no difference.
   - **The tail shares, reported** (RT-391). For each rule kind and cell, step 3 reports the share of the
     changed span that lies after the shared context: the final question, the template's closing tokens
     and the candidate. From it, step 3 also reports how large a difference in real distance per position
     the 10% limit of step 4b can absorb. With six-entry lookup tables, the sixth check estimated about 30%
     for the unit kind, 32% for the operator kind, 49% for the letter-code kind and 54% for the lookup kind.
   - **What John is told when step 4 is priced** (RT-391). That the free checks passed by construction and
     settled nothing about the real dose, and that the dose question is first answered at step 4b, after
     the first rental.
   - **A free estimate for the average method too** (RT-387). The average method's dose is spread over the
     whole text span. Under the shared-context construction the two twins' text spans are the same except
     for the final question, so the dose should differ only there. Step 3 reports, for each rule kind, the
     share of each cell's text span that lies in the final question, and the share of tokens that are
     pieces of invented words or symbols. Both should be equal between the cells to within one token per
     item. If they are not, the construction is revised, as above.
4. **The rehearsal, on a rented machine, pilot items only, on John's go with a ceiling.** It runs in two
   parts, priced separately. *(Step 4b ran on 2026-11-23 for about $1.93. It answered the dose question
   before any filter, and found the two problems version 0.13 answers. After the specification and the pilot
   are rebuilt for version 0.13, step 4b is run again in full on the rebuilt pilot, priced for John's go.
   That rerun closes RT-345 formally, after the filters. Under version 0.16 it also fixes C (section 5).
   The pilot itself does not change. Only the analysis and the simulation read the margin in place of right
   or wrong. Step 4a ran on 2026-11-21, with a scoring trial and a
   lookup calibration trial after it, for about $4.45 in all. Their findings are in `experiments/10-loop-removal-test/`, and
   version 0.9 answers them. The battery specification and the pilot set are rebuilt for the version that is closed, before
   step 4b.)*
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
3. *(As put to John on version 0.4. In version 0.5 and later the twins share a whole context, section 5.)*
   **Routine twins carrying the prompt-rule item's rule as a preamble** (section 5), in place of short
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

6. **Where the answer-only instruction sits** (version 0.9; both sides added in version 0.10, RT-447). At the
   start of the message, before the rule, or at the end, after the final question.
   - **For the start:** it leaves the part of each item after the shared context unchanged, which is where
     the swap's dose differs between the cells. With it, the tail shares, the dose ratios and the donors are
     exactly the pilot's. At the end, the tail shares rise from between 0.17 and 0.34 to between 0.26 and 0.47, by rule kind, and
     the difference per position that the 10% swap-size limit can absorb falls by about a third.
   - **For the end:** it costs the operator kind less. At three passes, 12 of 30 operator prompt-rule items
     passed the confidence filter against 8 at the start, and all prompt-rule items were right on 72%
     against 66%. The bites gain was 0.37 against 0.32.
   - **Otherwise alike:** routine twins 84% and 83% at three passes; confidence filter 63% and 65% of the 240 pair items.
     Every figure comes from 30-item cells.

   - **What the placement does to the pilot under choice 8** (RT-463). The closure check of version 0.11
     simulated the strike-count rule at 40 operator, 40 unit and 40 lookup pairs. With a combined chance f of
     a surviving pair failing a baseline check, the design returns to John in 9%, 15% and 29% of runs at f of
     0, 5% and 10% at the start, against 0.2%, 7% and 22% at the end. The reason is the operator's colours
     pairing, whose pairs pass the filter at 5% at the start and 29% at the end. These are lower bounds,
     because margin matching and donor losses were left out.

   Recommended, narrowly: the start, because the dose risk (RT-345) is the one the test was built around,
   and a return to John at step 4b costs a short rental, while a dose imbalance found at the registered run
   would cost the result. The end is a fair choice if the operator's survival is weighed higher.
7. **The working precision** (version 0.9). The model's own 4-bit format cannot be loaded by the software
   that has the model's code, so steps 4a and the two trials ran with the weights unpacked to 16-bit. The
   weights are the stored 4-bit values unpacked, the same to within 16-bit rounding (RT-446; the stored scales
   are divided out, which is not exact in general), and the arithmetic is not the 4-bit arithmetic the model
   was trained to run in. No accuracy was compared with the native path. Accept 16-bit for this test, saying so in every report, or wait for, or build, support for the native
   format. Recommended: accept 16-bit, because the test compares conditions on the same model at the same
   precision, and the native path would need an inference engine where the hooks are far harder to build.

8. **Drop the letter-code kind, and share its pairs equally among the other three** (version 0.10; revised
   in version 0.11, RT-438, RT-450, RT-454). With the instruction, the letter-code kind was at chance at every
   number of passes, and 1 of its 30 prompt-rule items passed the confidence filter. The closure check of
   version 0.10 simulated the strike-count rule: with the letter code kept, the design returns to John in
   essentially every run.
   - **The allocation.** The pilot would have 40 operator, 40 unit and 40 lookup pairs, and the test half the
     same shares. Version 0.10 gave the operator kind 60 and the others 30. That helps the operator in the
     pilot, but in the test half the operator and unit pairs can pair only with capitals, opposites and
     everyday colours, and half B has only 36 usable capitals. Under the 25% cap that limits the test half to
     about 144 pairs, of which about 88 would pass the filter, below the 120 to 200 needed (RT-450).
   - **What each share allows** (recomputed by the closure check of version 0.11, RT-463). Test half, under
     the 25% cap and half B's pools, with products at the split's usual 22 to 28; survivors are with the
     generator's even spread over pairings, at the trial's whole-pair pass rates at the start placement. The
     pilot column is the chance of a return to John at f = 0 (above):

     | Allocation | Test-half pairs at most | Expected to pass the filter | Pilot: return to John, start / end |
     |---|---|---|---|
     | Letter code kept, four equal kinds | about 216 to 236 | about 114, almost none letter code | 100% / 100% |
     | Three equal kinds (recommended) | about 216 to 220 | about 140 to 145 | 9% / 0.2% |
     | Operator 2 : unit 1 : lookup 1 | about 145 | about 86 | 2% / 0% |
     | Operator 1 : unit 1 : lookup 2 | about 216 to 236 | about 154 to 168 | not simulated |

     The unit survivor figures were measured on the trial's easier unit range (RT-464), so all of these are
     likely high.
   - **The 1 : 1 : 2 share** gives the most survivors. Version 0.11 rejected it because "almost no operator
     pairs survive", which was wrong: it keeps about 10 to 12, against about 17 to 18 for three equal kinds.
     It is not recommended for two other reasons: the operator kind, already the weakest, is then the
     smallest, so the pilot's strike-count rule is likelier to return the design; and half of all pairs then
     sit behind the lookup rule with sums and products, which makes the arithmetic tie below worse.

   - **What dropping it costs.** No spare kind: all three remaining kinds must survive. The prompt-rule cell
     is then all arithmetic or table lookup. And sums and products, which may not sit behind an arithmetic
     rule, pair only with the lookup rule (RT-454). Those are the routine twins that needed the extra passes
     in the trial, so the routine cell's sensitivity to the passes sits wholly behind one rule kind. The
     surviving routine cell would be roughly 46% to 51% arithmetic, and sums alone 35% to 38%, against the
     cap's purpose that "routine" is not mostly arithmetic. **The 25% cap applies to the built cell** (RT-463),
     which it meets (sums and products together about a third). After the filter the mix is reported, not
     capped, because cutting pairs after the filter would cost about 20 survivors and select on how the model
     did. And leaving out the lookup rule removes every sum and product twin, so the
     one-kind-left-out readings cannot separate a lookup-rule effect from a routine-arithmetic effect. None of
     this favours A; it makes C likelier.
   - **The operator's risk in the pilot remains.** At 40 pairs, spread over its three pairings, the operator
     kind keeps about 12 pairs at the start (14 at the end), mainly with capitals (section 5). The simulated
     returns to John are under choice 6.

   Recommended: drop the letter code, with three equal kinds. The alternative is to keep it, and expect a
   return to John at step 4b.

9. **The thresholds in margin** (version 0.16, RT-506). Every loss is in units of C, what one pass costs the
   prompt-rule items in margin (section 5). Two numbers decide the outcomes: δ, below which an excess counts as
   none, and the target gap, which sizes the test. The options:
   - **(a) Shares of one pass's cost** (recommended): δ = 0.5 and a target gap of 1.0 in units of C. They round
     the values the accuracy scale implied on step 4b's data (0.57 and 1.15). They mean "no excess" is below
     half of what the extra passes supply, and the test is sized to find a gap as large as what they supply.
     They are anchored on a measure steady to about ±14% on the pilot.
   - **(b) Fixed nats, set now:** δ = 2.4 nats and a target gap of 4.8 nats, from step 4b's figures, never
     re-measured. This is the simplest and is fixed before any further data. But it does not follow the rebuilt
     pilot, whose items and margins differ.
   - **(c) Shares of the per-item spread:** δ and the gap as fractions of the spread of the removal's loss. This
     is not recommended, because a threshold would then move with the noise rather than with what the passes
     supply.

Version 0.1's fourth choice, keeping the pass-counting coordinates at their true values, is withdrawn
(RT-348).

## 11. John's rulings (2026-11-21)

John ruled on the questions in section 10 on 2026-11-21. He picked the recommended option each time,
from a question form in the session. Authorship is mixed: this design recommended, and John chose. The
ruling is recorded in `docs/rulings/2026-11-21-loop-removal-test-choices-ruling.md`.

- **Whether it goes ahead:** "Yes, paper work now". Design work continues at no cost before the pause
  from 2027-01-04. Every rented step still comes to him with a price first.
- **Choice 1:** five fixed options, scored by probability.
- **Choice 2:** no written reasoning.
- **Choice 3:** routine twins, with the dose question settled by the free real-tokeniser check at step 3.
- **Choice 4:** Inkling 2 Mini added as a descriptive second model.
- **Choice 5:** if both versions of the average differ from the swap by more than a factor of two, the
  test stops.

These rulings were made on version 0.4. RT-345, the finding that the swap's dose differed between the
two task groups, is open, and so are the findings of the fourth check, RT-380 to RT-389. They are to be
answered in a version 0.5, written against the model's real tokeniser where the findings turn on token
counts.

**Choices 6, 7 and 8** (ruled 2026-11-21, on version 0.12, after its closure check found the design ready
for step 3). John picked the recommended option each time, from a question form in the session. Authorship is
mixed. The ruling, with the wording he was shown, is recorded in
`docs/rulings/2026-11-21-loop-removal-test-choices-6-to-8-ruling.md`.
- **Choice 6:** "Start (Recommended)". The instruction goes before the rule.
- **Choice 7:** "Accept 16-bit (Recommended)". Every outcome sentence names the precision.
- **Choice 8:** "Drop, three equal (Recommended)". The letter-code kind is dropped, with 40 operator, 40 unit
  and 40 lookup pairs in the pilot and the same shares in the test half.

**After step 4b** (ruled 2026-11-23). The step-4b findings
(`experiments/10-loop-removal-test/step4b-findings-2026-11-23.md`) put three questions to John. He picked the
recommended option each time, from a question form in the session. Authorship is mixed. The rulings, with the
wording he was shown, are in `docs/rulings/2026-11-23-loop-removal-test-after-step4b-ruling.md`. They are to
be written into a version 0.13:
- **Interference:** "By accuracy (Recommended)". An item counts as interfered with only if it is wrong in the
  full context and right without the other half. This replaces the limit of 1.0 in margin.
- **Damage and perplexity:** "As the model's reply (Recommended)". They are measured on the prose placed as
  the model's own reply. The prose stays in the user's turn for building the average.
- **The operator kind:** "Simplify it (Recommended)". Single-step operator rules, three rule kinds kept, and
  the kind checked on the pilot before any test set. The ruling file records a consequence the question did
  not name: the bites check relies on the operator kind's gain from extra passes.

**Scoring by margin** (ruled 2026-11-23). After the free margin check, John was asked "Switch the test to
margin scoring in a version 0.15?" and answered "Yes, write 0.15". The ruling is recorded in
`docs/rulings/2026-11-23-loop-removal-test-margin-scoring-ruling.md`. The scale K, its anchor and its return
to John are the author's design (section 5).

**What is the author's, not John's, in versions 0.15 and 0.16** (RT-511). John ruled scoring by margin. These
are the author's:
- the margin's definition for each condition;
- version 0.15's constant K and its anchor rule, withdrawn in version 0.16;
- the unit C, its fixing on the pilot, and its ±50% check;
- the one-pass condition at a quarter of C;
- the reporting of starting margins.

The thresholds' values are John's to choose (choice 9).

**What is the author's, not John's, in versions 0.13 and 0.14** (RT-494). John ruled three things after step
4b: interference by accuracy, damage on the model's reply, and the operator simplified. The following were
added by the author in writing those rulings in. They are marked here so that no reader takes them for John's:
- the tie rule for the accuracy check;
- the counting base, items right without the other half;
- the minimum of three confident pairs a pairing;
- the fixed request and the fixed opening of the reply rendering;
- the reading that the average built in the user's turn is applied on the reply rendering, and the second,
  reply-built average beside it;
- the 1-nat check and its return to John;
- "with a written constant" for the operator's shapes;
- version 0.13's cut at 0.15 for the bites set, replaced in version 0.14 by the simulation's choice;
- the factor search's range.

**A premise of choice 3 that no longer holds** (dated 2026-11-21, after the fifth check; RT-391; quotation
corrected in version 0.7, RT-401). John ruled from a question form in the session.
- **What he picked.** The option he picked for choice 3 was labelled "Twins (Recommended)". It read: "Keep
  the twin design and settle the dose question with the free real-word-splitter check before any rental."
  **Where this is recorded** (RT-405). The wording comes from the session's question form, which the author
  wrote and whose answers the session recorded. The session transcript is the primary record, and it is
  not in the repository. The question text for choice 3 also differed from section 10: it added that the
  latest check found the twins still did not get an equal swap.
- **What section 10 said.** Section 10 of version 0.4 put it differently: "Whether it now passes is first
  estimated for free at step 3 and then measured on the model at step 4b."
- **What changed.** Under version 0.5's shared context, the free check passes by construction. So the
  first half of each sentence no longer holds: the free check settles nothing about the real dose. The dose
  question can now be answered only at step 4b, on the rented machine.
- **What stands.** The substance of the ruling, routine twins, is kept.
- **When John was told, and when he will be told again.** He was told in the session's closing message
  after the fifth check, on 2026-11-21, in the same session. The worklog entry "Loop removal test: the
  fifth check confirms the shared-context fix with the real tokeniser, but finds the free check can no
  longer settle the dose question" records the finding, and it names the contradiction with the ruling's
  premise. It does not itself record the telling (RT-405). He will be told again in plain words when step
  4 is priced.

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
- *donors "from the same kind and cell" became donor pairs of the same rule kind (version 0.3), and then of
  the same rule kind and routine kind (version 0.4);*
- *a reading with one kind left out "that differs from the full reading" renaming the outcome became
  renaming only on a different definite outcome (version 0.3), read on the R and P intervals alone and
  covering routine kinds (version 0.4);*
- *the bites check's "at least half of what one pass costs" now has the random comparison's loss
  subtracted first (version 0.3);*
- *plurals as a routine kind were dropped (version 0.4).*

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

*This change log records version 0.3 as it was written. Several rules in it were later replaced, and the body governs (RT-379, RT-389): the "more than a third" limit on swap-size matching became "more than a tenth" (version 0.4); plurals were dropped as a routine kind (version 0.4); donor pairs "of the same rule kind" now also share the routine kind (version 0.4); the leave-one-kind-out rule of RT-363 now covers routine kinds and ignores the bites check (version 0.4); and the routine questions "behind" a rule now share the whole context with their twin (version 0.5).*

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

## Change log from version 0.4, by finding of the fourth closure check

*This change log records version 0.4's replacements as of version 0.5. Two rules in the third change log
were later replaced, and the body governs: the equal-length phrasings chosen item by item became one fixed
wording per pairing, with all item-specific content in a shared context; and the margin fallback was
withdrawn.*

**RT-345, the swap's dose differed between the cells, kept open.** Its five clarifications were closed by
the fourth check. The construction behind it is changed (RT-380 below). On the stand-in measure, the dose
is now equal by construction. Its closure is still the step-4b measurement on the model.

**Serious findings:**
- **RT-380, equal length did not give equal dose:** all item-specific content moves into a context that
  both twins carry word for word, and each item ends with a fixed question containing nothing specific to
  it. Donor and recipient then diverge at the same place in both cells, and the final questions match their
  donors' in both (section 5).
- **RT-381, the unit kind could not be length-matched:** the unit facts move into the shared context, so
  only the fixed final questions need matching. The real tokeniser finds matching wordings for every
  allowed pairing, including the unit kind with capitals, opposites and everyday colours (section 5's
  table).
- **RT-382, the two cells got different phrasings, chosen item by item:** one wording of each question is
  fixed for each pairing of a rule kind and a routine kind. The prompt-rule and routine wordings of a
  pairing still differ, as they must, but the difference no longer varies between items. The stale sentence
  in section 3 about donors sharing "its question template" is replaced (section 3).
- **RT-383, colours could not meet the overlap check:** colour answers are exempt from the answer-value
  check, which applies instead to the lookup kind's invented words and tables and to the everyday-colours
  kind's objects (section 5).

**Worth-noting findings:**
- **RT-384, the everyday-colours pool:** the list is cut to at least 120 objects and written out before any
  item. Each entry lists the colours the object is commonly seen in, which are never offered as wrong
  answers, and objects whose colour differs by country are left out. The pool arithmetic is recounted at
  about 345 routine questions (section 5).
- **RT-385, the copying rule's wording:** it works on whole content words of the routine fact and final
  question, ignores the rule's text, bars any candidate that contains or is contained in such a word, and
  exempts numbers (section 5).
- **RT-386, the margin fallback never rescued a kind:** withdrawn. Matching the means beyond a third returns
  the design to John, on pilot or test pairs, counted from the pairs that pass the confidence check
  (section 5).
- **RT-387, step 3 saw the swap only:** step 3 also reports, for the average method, each cell's share of the
  text span in the final question and its share of invented-word or symbol tokens, to be equal within one
  token per item (section 9).
- **RT-388, donors of the same routine kind left the largest tables without donors:** lookup tables come in
  three size classes, donors are drawn within a class, and every group of rule kind, routine kind and size
  class is generated with at least six pairs (section 3).
- **RT-389, text gaps:**
  - the pilot's size is stated (120 pairs, 30 per rule kind);
  - "within 10%" is defined as a ratio between 0.90 and 1.10;
  - the two stale sentences are replaced;
  - both earlier change logs now list the rules later replaced.

**Conditions the fourth check set on findings it closed:**
- **RT-340:** the simulation is run on the pairs that survive every filter, with the measured spread and
  comparison loss, and again if a rule kind is dropped (section 5).
- **RT-371:** the smaller leak that remains at small sizes is reported beside any outcome A (section 6).
- **RT-372:** the letter code's extra letters are chosen to fit four wrong words, and every candidate has
  three different letters (section 5).
- **RT-373:** see RT-385.

## Change log from version 0.5, by finding of the fifth closure check

*This change log records version 0.6. One rule in the fourth change log was later replaced, and the body
governs: the lookup kind's six-pair floor per group now applies at the test size only, and the pilot uses
one table size (version 0.6).*

**RT-345, the swap's dose differed between the cells, kept open.** The fifth check confirmed the
shared-context construction on the stand-in measure (0.998 to 1.019). It showed that the remaining risk
lies only in the last 11 to 13 positions of each item, which no token count can see. Its closure is still
the step-4b measurement.

**Serious findings:**
- **RT-391, the free checks now pass by construction:** step 3's estimates are restated as checks that the
  generator builds what section 5 describes. Step 3 also reports the tail shares and the difference per
  position that the 10% limit can absorb. Section 11 records, with a date, that a premise of John's choice
  3 no longer holds. John is to be told plainly when step 4 is priced (sections 9 and 11).
- **RT-392, the lookup size-class floor could not be met at the pilot:** the floor of six pairs per group
  applies at the test size only. At the pilot, lookup's 30 pairs are spread across its four routine kinds,
  and every table has six entries, so that the pairing table and the baseline checks cover all four of
  lookup's pairings (section 3).
- **RT-393, the baseline check compared against an unanswerable item:** the routine side now compares the
  full shared context against the routine fact and its final question alone. A mirror check is added on
  the prompt-rule side, comparing the full context against the rule, its facts and its final question
  alone (section 5).

**Worth-noting findings:**
- **RT-390, false alignment sentences:**
  - the sentences in sections 3 and 5 now say that donors' final questions usually start later;
  - "exactly 1" is replaced by the range a correct build gives;
  - every candidate of both twins must now be a single token at the answer position, so the scored span is
    the same in both twins. The real tokeniser finds 82 of 105 common capitals to be one token, and the
    pool arithmetic is recounted at about 325 (sections 3 and 5).
- **RT-394, context order and ambiguous wordings:**
  - the order of the rule's facts and the routine fact is balanced across pairs, and results are reported
    by order;
  - "the word to look up" becomes "the name to look up";
  - the lookup question becomes "What colour does the table give the name?". The four lookup rows of the
    wording table are rewritten and recounted at 9 tokens each with the real tokeniser (section 5).
- **RT-395, the copying rule's scope:** it covers prompt-rule candidates too. The routine twin's right
  answer is never a prompt-rule candidate (section 5).
- **RT-396, the colour pool and the half-A rule:** colour names are one shared pool, exempt from the
  half-A candidate rule. Capitals' wrong answers come from half B only, with same-region capitals where
  neighbours run short (section 5).
- **RT-397, stale or conflicting text:**
  - the pair count reads about 325 in both places;
  - section 9's step 1 now describes this version's check;
  - results for each routine kind are reported by wording;
  - section 10's choice 3 is marked as describing version 0.4.


## Change log from version 0.6, by finding of the sixth closure check

*This change log records version 0.7. Two rules in the fifth change log were later replaced, and the body
governs:*
- *the lookup kind's six-pair floor per size class at the test size became one table size throughout,
  with donor-only pairs (version 0.7);*
- *"about 325" routine questions became about 307 (version 0.7).*

**RT-345, the swap's dose differed between the cells, kept open.** The sixth check found the stand-in dose
ratio at 0.996 to 1.001 in every rule kind, and the tail after the shared context at 18% to 34% of the
changed span. The closure is still the step-4b measurement.

**Serious findings:**
- **RT-398, lookup's donors and size classes:** every lookup table has six entries, at the pilot and at the
  test, and the size classes are withdrawn. Donor-only pairs, built like scored pairs but never scored, are
  added to any group until every scored pair has at least five eligible donors, up to three times the
  scored count. The rule against intruding donor answers is kept. Step 3 reports eligible donors per
  scored pair and the donor-only pairs added (section 3).
- **RT-399, single-token capitals:** the counts are corrected to about 42 capitals in half B and about 307
  routine questions. The skew toward famous capitals is stated as a cost of the single-token rule.
  Capitals are kept, with results also reported without them and the spread of right answers reported by
  region. Multi-token capitals are not brought back, because they would undo RT-390. The operator kind's
  answers are kept at or below 999 (section 5).

**Worth-noting findings:**
- **RT-400, the space before the answer:** if step 4a finds that a space or other tokens precede the answer,
  the pools, the pilot and the single-token counts are rebuilt before any pilot item is scored (section 5).
- **RT-401, the section 11 note:**
  - it now quotes exactly the option John picked and section 10's sentence;
  - it cites the worklog entry recording that he was told;
  - a dated note in the ruling file corrects its own wording without changing John's answers (section 11,
    `docs/rulings/2026-11-21-loop-removal-test-choices-ruling.md`).
- **RT-402, the baseline checks' calibration:**
  - both checks are one-sided, failing only when the full context lowers the margin by more than 1.0;
  - the mirror check's rules are written out;
  - strike counts per pairing are reported before the pairing table is fixed, and the design returns to
    John if fewer than three rule kinds, or a rule kind with one routine kind, would remain (section 5).

**Conditions the sixth check set on findings it closed:**
- **RT-390:** a correct build is described as about 0.99 to 1.03 (section 9).
- **RT-394:** results by order are a report only and rename nothing. An odd pair's order is set by the seed,
  and donors need not share the order (section 5).
- **RT-395:** the prompt-rule item's right answer is never a routine twin candidate (section 5).
- **RT-396:** capitals without four same-region wrong answers draw from the nearest neighbouring region,
  and are otherwise dropped, with both counted (section 5).

## Change log from version 0.7, by finding of the seventh closure check

*This change log records version 0.8. Some rules in earlier change logs were later replaced, and the body
governs (RT-406):*
- *the lookup size classes of the version 0.5 change log (RT-388) and the lookup tables of "five to seven
  entries" in the version 0.4 change log (RT-377) became one six-entry size (version 0.7);*
- *"about 307" routine questions in the sixth change log became about 270 to 300 pairs, with each
  multiplication counted once (version 0.8);*
- *margin matching, listed as a capitals safeguard in version 0.7, is withdrawn as one (version 0.8).*

**RT-345, the swap's dose differed between the cells, kept open.** The seventh check found the stand-in dose
ratio at 0.997 to 1.001, with or without donor-only pairs. The closure is still the step-4b measurement.

**Serious finding:**
- **RT-403, donor-only pairs and the no-reuse rule.** Donor-only pairs may reuse any routine question, rule
  content or invented word from their own half. They sit outside the rule that no routine question is used
  twice, outside the pool budget and outside the 25% cap. The overlap script counts them with the set they
  serve (section 3).

**Worth-noting findings:**
- **RT-404, the longest pairs left without donors.** A candidate donor-only pair is kept only if it can serve
  a scored pair in its group that still has fewer than five donors. Any scored pair still left with no
  donor is dropped, and its content is reported (section 3).
- **RT-405, the ruling note's wording and its source.**
  - The ruling file's dated note is corrected: the questions in the form were the author's summaries of
    section 10, and the question for choice 3 added a sentence.
  - The note and section 11 now name the session transcript as the primary record of the option wording,
    and say that the cited worklog entry records the finding, not the telling.
  - John's answers are unchanged.
- **RT-406, stale text.**
  - The lookup table is "six entries" in section 5.
  - Section 9's steps 1 to 3 now describe this check, record that John's rulings were made, and give the
    sixth check's tail figures for six-entry tables.
  - This change log's header marks the earlier rules that were replaced.
- **RT-407, the pool arithmetic.** A multiplication counts once, and so does a sum. The ceiling is given as
  about 270 to 300 pairs, depending on the split. The expected 120 to 200 is unaffected (section 5).
- **RT-408, which way the capitals cost points.** The text now says the cost favours outcome A. Any A is
  reported beside its capitals-out reading, whatever that reading lands in. Margin matching is withdrawn as
  a safeguard for this worry (section 5).

**Conditions the seventh check set:**
- **RT-402, two gaps.** "A fifth" is counted from the pairs that pass the confidence check, in both baseline
  checks. A rule kind left with one routine kind or none returns the design to John (section 5).
- **RT-396, the region map.** The battery specification writes out the region map and each region's nearest
  neighbouring region before any item exists (section 5).
- **The cost sentence.** It now counts two unaltered runs per donor-only pair, about 5% extra machine time,
  and about 2.5 GB of stored block sums at 300 pairs (section 3).

## Change log from version 0.8, by finding of the rented runs

*This change log records version 0.9. It answers three runs on a rented machine on 2026-11-21, not a review:
step 4a, the scoring trial and the lookup calibration trial. Their findings are in
`experiments/10-loop-removal-test/`: `step4a-findings-2026-11-21.md`, `scoring-trial-findings-2026-11-21.md`
and `chain-calibration-findings-2026-11-21.md`. Each is owed an independent check.*

**What the runs found, and what changed:**
- **Forced answers were near chance** (step 4a). The model always begins its reply with written reasoning.
  John chose to try an answer-only instruction ("Answer-only instruction"). It worked for the paired
  questions, and John then chose to keep it and change the bites task ("Redesign the lookups"). Version 0.9
  adds the instruction to every item (section 5). Where it sits is choice 6 (section 10).
- **Chained lookup could not be answered at once** (the scoring trial and the lookup calibration trial).
  Even two-step chains were at chance in every version tried. John chose held-out invented-rule problems
  for the bites check ("Invented-rule problems"). Version 0.9 replaces task L with task K: held-out problems
  of the operator and unit kinds, 200 in the test half and 80 in the pilot (section 5). Sections 3, 6, 7 and
  8 are updated to match.
- **The cost of that replacement is stated** (section 5). The bites task now shares two kinds with the
  prompt-rule cell, so outcome D is harder to reach and narrower, and its report must say so. The closure
  check is asked to weigh this.
- **The letter-code kind stayed at chance** with the instruction. The risk that only three prompt-rule kinds
  survive is stated (section 5).
- **The native 4-bit format could not be used** (step 4a). The working precision is choice 7 (section 10).

**Not changed:** the outcomes and their thresholds, choices 1 to 5 and John's rulings on them, the two
removal methods, and the comparisons. RT-345 stays open until step 4b.

## Change log from version 0.9, by finding of the ninth closure check

*This change log records version 0.10. The ninth check judged version 0.9 not ready for step 3, and found the
operator and unit bites problems the right call rather than stopping the test.*

**RT-345, the swap's dose differed between the cells, kept open.** The closure is still the step-4b measurement.

**Serious findings:**
- **RT-437, outcome D after the change.** D is reported as "No excess in the cells", with no reading, while
  the bites items share kinds with the prompt-rule cell. Section 5 names the three ways to reach it, and says
  the "depends on one kind" rule does not cover D. Sections 1, 6 and 7 are changed to match, and the loss to
  what the test can show is stated as a loss.
- **RT-438, the operator kind is at risk.** Section 5 gives the measured confidence-filter counts and the
  whole-pair estimates, says what follows for the test half, and says what is done now (choice 8) and if the
  rebuilt pilot confirms it (a return to John, with no threshold loosened).
- **RT-439, the halves differed in difficulty.** The operator, unit, sum and product pools are split by
  interleaved bands of five on the right answer, with the same operand ranges in both halves (section 5).
- **RT-440, the keep-apart rule could not be met.** Bites items may share numbers and answers. They may not
  repeat a scored pair's or donor's whole content, and they obey the half split (section 5).

**Worth-noting findings:**
- **RT-441, the trial figures.** The rule-kind figures now count items. Version 0.9 averaged unequal groups.
- **RT-442, the size target.** The simulation now aims at both parts of the bites check's second condition
  passing when the true excess is three quarters of the one-pass cost.
- **RT-443, filters and donors.** Bites items pass no filter and are all scored, with the filtered reading
  beside it. The donor rule's conditions apply to the single item.
- **RT-444, what the bites check gates.** The one-pass condition gates every outcome; the excess condition
  gates D only. Both are said where they are set.
- **RT-445, the gain runs in opposite directions by kind.** Stated in section 5; the simulation draws effects
  by rule kind.
- **RT-446, 16-bit.** "The same numbers" becomes "the same to within 16-bit rounding". A tie rule is added,
  and the coarseness of the scores is stated. Every outcome sentence names the precision, and the second
  model's precision is stated beside its result.
- **RT-447, choice 6.** It now gives both sides, including the operator's cost of the start placement. The
  neutral passages carry no instruction, and section 5 says why.
- **RT-448, stale text.** The noise-floor reason, the memory figure and the run count are brought up to date.
  The count now uses step 4a's finding that one run scores all five candidates: about 85,000 runs.

## Change log from version 0.10, by finding of the tenth closure check

*This change log records version 0.11. The tenth check found version 0.10 not ready for step 3, and every
trial figure it recomputed right.*

**RT-345, the swap's dose differed between the cells, kept open.** The closure is still the step-4b measurement.

**Serious findings:**
- **RT-449, the plainest failure had no reading.** New outcome F, "The replacement does not bite": the
  one-pass condition holds, the excess over the random comparison on the bites items has an interval whose
  upper end is below a quarter of the one-pass cost under each method, the swap changed the message by at
  least half its size, and the cells show no excess. F is read as the prediction failing for this placement.
  A pattern of A, B or C with a removal that does not bite is renamed "Cells and bites check disagree", with
  no reading. Section 7's allowed sentence about the fewer-passes runs moves from D to F. Sections 1, 3, 5, 6
  and 7 are changed to match, and section 1's drifting "That" is fixed.
- **RT-450, choice 8 capped the test half.** Choice 8 now shares the pairs equally among the three remaining
  kinds. The ceilings were worked with a maximum-flow fit of rule kinds to routine pools under the 25% cap,
  using half B's pools (36 capitals, 75 opposite questions, 61 objects, sums ample, products 13 or 23), and
  expected survivors from the scoring trial's whole-pair pass rates at the start placement (each pairing's
  prompt-rule pass rate times its routine pass rate):
  - four equal kinds: 196 pairs (products 13) or 236 (products 23), about 108 or 126 surviving;
  - three equal kinds: 196 or 220, about 133 or 149;
  - operator 2 : unit 1 : lookup 1: 144 either way, about 88;
  - lookup given the letter code's share (1 : 1 : 2): 196 or 236, about 133 or 161, but almost no operator
    pairs survive, so it is not offered.
  These are estimates from 7- to 12-item cells, made by the author; the closure check is asked to recheck
  them.
- **RT-451, the bands split the last digit.** Replaced by a per-decade draw that gives each half one value
  ending in 0 or 5, two other even endings and two other odd endings. Step 3 reports each half's last-digit
  mix and operand parity, and the halves are not called equally hard until it does.

**Worth-noting findings:**
- **RT-452, the overlap rules.** The operator's split key is the shape with its operands. Numeric wrong
  answers are exempt from the half check. `src/check_overlap.py` is to be rewritten for the new split. The
  "about 2.5 higher" figure is dropped.
- **RT-453, the excess condition's job.** It now decides between D, F and the disagreement rule. The
  one-pass condition gets an interval: its lower end must be at or above 0.15. The simulation sizes the
  bites set for "bites", "does not bite" and the one-pass condition together.
- **RT-454, routine arithmetic behind the lookup rule.** Stated under choice 8.
- **RT-455, repeated facts.** The unit kind uses a factor of 2 to 9 and a count of 2 to 12, and is resampled
  by multiplication fact. The number of distinct facts per kind is reported.
- **RT-456, stale text.** The sums and products splits, the pool counts, the pair ceiling, the "kept as
  nearly equal" sentence and the pilot's size are made conditional on choice 8. The step-4 note names the
  version that is closed.

**Small fixes under earlier findings:**
- the confidence share is given over the 240 pair items (28%, then 63% and 65%; RT-441);
- the identity sentence says the checks "will usually fail on any real difference" (RT-446);
- the time estimate carries its two caveats (RT-448);
- the routine gain is placed on sums and products, and the simulation draws effects by routine kind too
  (RT-445).

## Change log from version 0.11, by finding of the eleventh closure check

*This change log records version 0.12. The eleventh check found version 0.11 not ready for step 3. It
confirmed the choice 8 ceilings within a few pairs, and found outcome F the right kind of answer but not yet
safe to read.*

**RT-345, the swap's dose differed between the cells, kept open.** The closure is still the step-4b measurement.

**Serious findings:**
- **RT-457, F did not require the swap to leave the problems intact.** "Does not bite" now requires the main
  removal's own loss on the bites items, against the unaltered run, to have an interval below a quarter of
  the one-pass cost, under each method. F's sentence says "cost them little".
- **RT-458, the disagreement rename.** It no longer applies to B. For A and C it applies only when the
  operator and unit pairs of the prompt-rule cell have an excess above zero while the removal does not bite.
  Section 1 says what section 6 requires of B and C.
- **RT-459, the change ratio.** It is defined exactly: positions from the first difference between item and
  donor through the answer, both block sums, passes 2 and 3, each sum scaled to a root-mean-square of 1, the
  distance over the true sum's length, averaged. Step 4b reports it on the pilot, and a pilot mean below 0.5
  under either method returns the design to John. F's sentences say "on average".
- **RT-460, items, not values.** The round values alternate between halves decade by decade. The halves must
  match on five item-level figures within fixed tolerances, and the seed is the first from 1 that meets them,
  computed without the model, with a return to John if none up to 1,000 does.

**Worth-noting findings:**
- **RT-461, one kind carrying F.** "Does not bite" must hold in each bites kind; otherwise "Depends on one kind".
- **RT-462, resampling.** Section 6 sets the scheme: within each rule kind, by multiplication fact in the unit
  kind and by pair elsewhere. The simulation uses it and models the bites items and the cells together.
- **RT-463, choice 8.** The recomputed table, the pilot's simulated returns at both placements (now under
  choice 6), a corrected reason for not recommending 1 : 1 : 2, the survivors under the generator's even
  spread, and the cap's base (the built cell).
- **RT-464, the unit range.** "Close to the trial's difficulty" is dropped and the gap stated. The operator
  kind's shared range is stated (operands 2 to 15, answers 10 to 49).
- **RT-465, stale text.** The operator's "0 to 999", the numeric exemption from the half-A candidate check, the
  "270 to 300" remnant, the resampling wording, the "tenth" count, the rule on F in the one-kind readings,
  "never renamed by these checks", and section 9's steps 1 and 2 (choices 6 to 8 unruled). The tenth change
  log's "products 13 or 23" stands as written then; the split gives 22 to 28 (5th to 95th percentile 22 up,
  median 28), as choice 8 now says.

**The two definitions owed under RT-453:** "a quarter of the one-pass cost" is the point estimate on the same
items; the size rule's target for "does not bite" includes all three of its conditions.

## Change log from version 0.12, by John's rulings after step 4b

*This change log records version 0.13. It answers step 4b's findings
(`experiments/10-loop-removal-test/step4b-findings-2026-11-23.md`) through John's three rulings of
2026-11-23 (`docs/rulings/2026-11-23-loop-removal-test-after-step4b-ruling.md`), not through a review.*

**RT-345, the swap's dose, answered before the filters.** At step 4b, across all pilot pairs, the routine
cell's swap size over the prompt-rule cell's was 1.004 to 1.007 under the swap and 0.999 to 1.000 under the
average. The design's formal closure reads the sizes after the filters, so it waits for the rerun.

**The interference checks, judged by accuracy** ("By accuracy", John). Both checks now ask whether an item
right without the other half of the context turns wrong with it. The fifth is counted over the items right
without the other half. Counted over confident pairs, as the old wording had it, the rule would be empty,
because a confident item is always right. The step-4b pilot's figures under the new rule are given in
section 5.

**Damage and perplexity on the model's reply** ("As the model's reply", John). The neutral prose is
rendered as the model's reply for damage, perplexity, damage matching and the normal-range bound. It stays in
the user's turn for building the average. A check that the reply rendering's predictions are within 1 nat
per token of plain text's comes first, with a return to John if it fails. Section 5 says how the
replacements act on the reply rendering.

**The operator kind, simplified to a single step** ("Simplify it", John). One arithmetic step on the two
operands with a written constant. A rule is fixed now for the case the ruling's question did not name: if
the simplified kind's one-pass cost on the pilot bites items is below 0.15, the bites set holds unit items
only, with a return to John if the simulation then cannot reach its targets.

**Order of work.** After the closure check, the specification and the pilot are rebuilt. Step 4b is then
run again in full, priced for John's go.

## Change log from version 0.13, by finding of the thirteenth closure check

*This change log records version 0.14. The thirteenth check found version 0.13 ready for the specification and
pilot to be rebuilt. It owed a short version 0.14 before the step-4b rerun is priced.*

**Serious findings:**
- **RT-485, empty pairings.** A pairing with fewer than three confident pilot pairs, or an empty counting
  base, is struck (section 5).
- **RT-486, the reply rendering.** Everything before the prose is one fixed opening of template slots, and
  the closing end-of-message token is the only closing slot. "Plain text" is the prose alone (section 4).
- **RT-487, the role mismatch.** The reading is marked as the author's. A reply-built average is measured
  beside the user-built one, with a return to John if their damages differ by more than a factor of two
  (section 4).
- **RT-488, the unit-only branch.** The disagreement rename and the D and F sentences name the kinds actually
  in the bites set (sections 6 and 7).
- **RT-491, the likeliest way the test ends unread.** The normal-range and in-loop comparison risk is stated
  in section 4, to go to John when the rerun is priced. The factor search's range and its rule for an edge
  factor are fixed (section 4).

**Worth-noting findings:**
- **RT-489, the cut at 0.15.** Replaced: the committed simulation chooses between both kinds and unit alone,
  with a return to John if neither reaches the targets (section 5).
- **RT-490, the unit-only branch's power and pilot.** The rerun pilot carries 80 unit bites items, and the
  branch is said to be expected to need John (section 5).
- **RT-492, the seed.** Gate decisions use 100,000 resamples, and the seed spread is reported for close
  decisions (section 5).
- **RT-493, the single-step operator.** Its two-digit answers, crowded answers, the practised sum as a
  candidate, and the stale two-step figures go to the specification. "With a written constant" is marked as
  the author's (section 11).
- **RT-494, the author's additions.** Listed in section 11.
- **RT-495, items pushed below the bar.** Reported per pairing (section 5).
- **RT-496, the 1-nat check.** It now reports three renderings and says what it does not show (section 4).
- **RT-497, stale text.** The pilot's-size paragraph's counting base, the operator's range, the unit facts and
  the neutral passages' wording are corrected. Version 0.13's change log says "Section 5 says how the
  replacements act"; that is section 4, and the change log stands as written then. The step-4b findings'
  "about 2,600" for the baseline perplexity should read 1,869 (`collect-summary.json`); it is corrected
  there.

## Change log from version 0.14, by John's ruling on scoring by margin

*This change log records version 0.15. It answers John's ruling of 2026-11-23 ("Yes, write 0.15"), made after
the free margin check (`experiments/10-loop-removal-test/margin-power-check-2026-11-23.md`). It does not
answer a review.*

- **The outcome measure** is the margin, in place of right or wrong (section 5).
- **The scale** is accuracy-equivalent margin units. K and K_b are fixed on the pilot at the step-4b rerun,
  with a return to John if the anchor's interval reaches 0. They are the author's design (section 5).
- **The thresholds** keep their numbers in those units: δ, the gap, the one-pass condition, and the bites
  conditions, which are ratios (sections 5 and 6).
- **What the margin scale does not have.** It has no ceiling at 1 and it has long tails. Both are stated, and
  the losses' quantiles are reported (section 5).
- **Unchanged:** the confidence check, the interference checks by accuracy, the outcomes and their order, and
  every other ruling.
- **The order of work.** A closure check, then the analysis and simulation code for the margin, then the
  step-4b rerun priced. The pilot does not change (section 9).

## Change log from version 0.15, by finding of the fifteenth closure check

*This change log records version 0.16. The fifteenth check confirmed that scoring by margin gives the test its
power. On resampled real per-pair losses, outcome A came out at 99.5 to 100% from 80 pairs. The check found
the conversion to the old thresholds too uncertain.*

**Serious findings:**
- **RT-506, the anchor.** K is replaced by C, the prompt-rule cell's one-pass cost in margin, measured
  directly and steady to about ±14% on step 4b's data. The thresholds become shares of C, and their values go
  to John as choice 9. A check on C's interval returns the design to John if C cannot be fixed well enough.
- **RT-507, the units.** "Accuracy-equivalent" is dropped. The bites conditions are ratios of the bites items'
  own one-pass cost in margin. The one-pass condition's floor is a quarter of C.

**Worth-noting findings:**
- **RT-508, what the outcomes measure.** Sections 1 and 7 now say the outcomes are losses of margin, which can
  happen without any answer turning wrong, and report the share of right answers beside them.
- **RT-509, definitions.** Each condition's margin is defined, and so is the donor count. C is computed after
  the baseline and confidence checks, before matching. K_b's circle is gone.
- **RT-510, the simulation's double division.** It is to be fixed in `src/step4b_simulate.py` before the code
  is used again.
- **RT-511, stale text and marking.** The sample-size paragraph's "true normalised gap", the role of fewer
  passes, and the author's choices of versions 0.15 and 0.16 are listed in section 11.
- **RT-512, starting margins.** The cells' mean starting margins are reported beside every outcome.

