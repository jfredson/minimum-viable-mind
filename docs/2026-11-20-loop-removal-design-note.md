# Removing the loop: a design note on testing the inner loop of a looped open model

*Written 2026-11-20 by a working session, at John's request of the same day ("Yes, write the
note"). It follows his question about Thinking Machines Lab's new model, Inkling 2 Mini, and
whether it bears on this project. This is a note, not a design ready for registration. Nothing
has been run, downloaded or spent, and nothing here is ruled. It sits on the branch of the
three-hypotheses proposal (`docs/2026-11-20-three-hypotheses-and-refocus-proposal.md`) because
it leans on that proposal's first hypothesis. The idea was logged first as a TimeAssembler
worklog idea entry, "use Thinking Machines' looped open models to remove the loop itself"
(`eaa37951`).*

## 1. Why this note exists

On 2026-11-20 [Thinking Machines Lab](https://thinkingmachines.ai/) released two open-weights
models that do something ordinary language models do not.

In an ordinary model, each word passes once through the stack of layers, from bottom to top, and
then the model commits to the word. Nothing inside the model loops back while that one word is
being worked out. The only way back in is through the text the model has already written.

[Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/) instead runs its middle 12
layers three times for every word. On the second and third passes those layers also read what
they themselves produced on the pass before. Thinking Machines calls that hand-off the
"message". So inside the working-out of a single word there is a real loop, in which earlier
results shape later processing of the same moment.

The second model,
[TML-d24-varloop-research](https://thinkingmachines.ai/model-card/tml-d24-varloop-research/)
(the variable-loop research model), has the same design, but the number of passes can be chosen
each time it runs. That makes the loop something a researcher can turn down or off without
cutting into the model.

There are two reasons this matters here.

- **It bears on the first of today's three hypotheses.** The three-hypotheses proposal states
  hypothesis H1 as: experience needs contents held together in one shared workspace and updated
  as input arrives, and needs no self-model. John's wording that morning was "update those
  models in real time". A loop inside the working-out of each word is the most direct form of
  that real-time updating that can be opened and edited in an available model.
- **It may avoid the problem that stopped the last removal test.** The split removal test of
  2026-10-24 (experiment 09) failed on the bench model (Gemma 2, 2 billion parameters) because the
  information it tried to remove could not be taken out without pushing the model far outside its
  normal behaviour. That was a result about the method, not about the theory. The number of
  passes in the variable-loop model is a setting it was trained across, so turning it down is
  not an edit to the model's insides. Section 5 explains why this advantage is smaller than it
  first looks.

## 2. The model, from its makers' pages

Everything in this section comes from Thinking Machines' announcement and the research model's
model card, both read on 2026-11-20, and from
[Goodfire's early interpretability write-up](https://www.goodfire.com/research/interpreting-inkling-2-mini/)
(Goodfire is an interpretability lab that had early access to the weights), read the same day.
None of it has been checked by this project.

- **Size.** 26.4 billion parameters in all, of which 3.4 billion are used per word at one pass.
  Each extra pass adds about 1 billion more, so 5.4 billion at three passes and 7.4 billion at
  five. The model is a "mixture of experts", which means each word is routed to 8 of 128
  specialist sub-networks in each layer.
- **Layout.** 24 layers in four blocks of six. The first block runs once, the middle two blocks
  run a chosen number of times, and the last block runs once.
- **How the passes talk to each other.** According to Goodfire, a layer's input on a later pass
  is the mix it would have had anyway plus a gated copy of the message, which is drawn from the
  middle blocks' output on the previous pass. In practice the later passes read almost only from
  the third block's previous output. Goodfire also found one coordinate in the model's internal
  activity (number 2027 of 2304) that takes a very large value at the end of the first two passes
  and is cleared at the end of the last. They read it as the model signalling "another pass
  follows". That matters for section 4.
- **How the research model was trained.** In the later part of its middle stage of training it
  ran one to five passes, sampled in the ratio 1:2:6:2:1. So one pass made up one-twelfth of those
  samples and three passes made up half. Its final stage of training used three passes only.
  The card warns that it "may behave unpredictably at pass counts other than 3".
- **What changes with fewer passes, by the makers' own numbers.**
  - **Multi-step coding work collapses.** On the DeepSWE coding benchmark the score falls from
    47.4% of tasks at three passes to 0.7% at one pass.
  - **Silent reasoning gets shorter.** With no written-out reasoning, the length of task the model
    handles (measured in how long it takes a person) falls from 37 seconds of work to 16 seconds.
  - **Recall of facts barely moves.** On a closed-book factual quiz (SimpleQA Verified) the score
    goes from 7.3% at three passes to 6.3% at one.
  - **Chained lookups improve with more passes.** On a test of following a chain of lookups in
    its head, accuracy keeps rising up to ten passes, twice the most it was trained with.
- **Hardware.** The model is one file of about 20 GB, stored in the low-precision number formats
  it was trained in (4-bit and 8-bit formats designed for recent NVIDIA chips). It needs at least
  32 GB of graphics or shared memory. The card lists a Mac with 32 GB or more, a single NVIDIA
  card with 32 GB or more (for example the RTX 5090), or NVIDIA's DGX Spark. It is distributed as
  weights only, with no paid service to call.

## 3. What the loop is, and is not, a candidate for

The positions are careful here, and this note follows them. Ledger entry 45 in the Sentient
Horizons positions says that broadcast and looping back (recurrence) are ways evolved brains
reach deep integration, not what experience is. So the loop in this model is not a candidate for
experience. It is a candidate for **the mechanism that does H1's job in this model**: holding the
contents of one moment together and updating them before the model commits to a word.

That gives the test the same shape as the split removal test:

- **It places one candidate in one model.** It asks whether, in this model, the loop is where
  H1's job is done.
- **It cannot speak against H1 on its own.** If removing the loop does not produce H1's pattern,
  the most direct reading is that this model does H1's job somewhere else. One likely place is the
  ordinary attention across earlier words, which looping does not touch. That is a result against
  this placement, not against H1.
- **It can count for H1 only modestly.** If removing the loop produces H1's pattern beyond the
  comparison removals, that shows a fact about this loop in this model. It does not show that
  the model has experience.

H1's prediction, from the three-hypotheses proposal: removing the shared workspace's contents
leaves routine, practised output running and collapses flexible handling of anything new.

The makers' numbers already lean that way. Recall of stored facts barely moves at one pass,
while reasoning that needs many new steps in a row collapses. But those benchmarks were not built
for this question, and there is a second explanation that fits them equally well, set out in the
next section.

## 4. The central problem: fewer passes also means less computing

Turning the loop down removes two things at once:

1. **The feedback.** The model's later processing of a word no longer reads its own earlier
   result for that word.
2. **The amount of computing.** The model simply does fewer steps of work per word.

H1 is about the first, not the second. A model that does less work will do worse on hard new
problems and keep its easy recall for that reason alone. So a test that only turns the pass count
down cannot tell the two apart, and the makers' numbers cannot either.

Three removals, taken together, could separate them.

- **Removal A: fewer passes** (three, then two, then one). It is cheap, needs no edits, and shows
  the combined effect of both losses. It is also the one the makers already measured, so it
  doubles as a check that the project's setup reproduces their numbers.
- **Removal B: cut the message, keep the passes.** The model still runs three passes, but the
  gate that lets the previous pass's message in is set to zero. The expected result needs saying
  plainly: if nothing else differs between passes, every pass now gets the same input as the
  first, does the same work, and Removal B behaves exactly like one pass. If it does, that
  confirms the message is the only route between passes, which is worth knowing, but it does not
  separate feedback from computing. If Removal B differs from Removal A, then something other
  than the message also differs between passes, and that has to be found before anything else is
  read.
- **Removal C: swap the message, keep the passes.** The model runs three passes, but on passes two
  and three it receives the message that another input produced at the same position, in place of
  its own. It keeps the full amount of computing and receives a message of the right size and
  kind, but one that is not about this input. **This is the removal that tests H1.** If the H1
  pattern appears under C beyond the comparisons, it is the feedback about this very moment that
  matters, not the extra work. If C changes little while A collapses, the loop's value in this
  model is the extra computing, and the loop is not where H1's job is done.

**Open design questions for Removal C,** all to be settled on paper before any run:

- **Where the swapped message comes from.** It could come from the same text at a different
  position, from a different text of matched length and kind, or from the average message, as in
  experiment 01's mean-ablation.
- **What to do with the control coordinate.** Goodfire's coordinate 2027 seems to say "another
  pass follows". If a swapped message carries the wrong value there, C could damage the model's
  bookkeeping rather than its content. One answer is to keep the true run's value for that
  coordinate and swap everything else.
- **The normal-range check.** The project's rule is that a removal may raise the model's surprise
  at ordinary text by no more than random removals of the same size do. Removal A has no natural
  "random removal of the same size". Removal C does: swapping in a message from a different
  position of the same text is a mild version of C and can serve as the comparison.

## 5. Why the October problem is only partly avoided

Section 1 said the pass count is a setting the model was trained across. That is true, but only
weakly for one pass. One pass made up one-twelfth of the middle-stage samples and none of the
final stage, and the card itself warns of unpredictable behaviour away from three passes. The
0.7% DeepSWE score at one pass may be a model out of its normal range, not a model that has lost
one feature.

So the normal-range check applies to Removal A as much as to any edit, and two passes (a quarter
of the samples) may be the cleanest reduced setting. Removal C runs at the trained three passes,
which is another reason it is the main removal.

## 6. Tasks

The intention is to reuse the task batteries written for experiment 09, the split removal test
(`experiments/09-split-removal-test/batteries/`), which already separate the two kinds of task H1
is about:

- **Practised routines**, and problems the model must solve from rules given in the prompt.
- **Tasks about the model**, and tasks that never mention it.

One task is added as a positive check. The chained-lookup task the makers describe is known to
depend on the loop, so if Removal A does not hurt it, the project's setup is wrong.

Whether the experiment 09 pilot items suit a different and much larger model has not been
checked. The batteries were written for chat-format conversation and for the speaker question,
not for this one.

## 7. What a result would say

| What is seen | What it means | Counts for or against |
|---|---|---|
| Removal C gives H1's pattern (routines kept, new problems collapse) beyond the comparisons | The feedback about this moment does H1's job in this model | For the placement, modestly for H1 |
| Removal C changes little and Removal A collapses | The loop's value here is extra computing, not feedback | Against the placement, not against H1 |
| Removal C damages everything evenly | The message is essential to the model working at all, which tells nothing selective | Neither: not readable |
| Removal C pushes the model out of its normal range | The method failed, as in October | Neither: a result about the method |

The outcome that would count against H1 itself is not available from this test alone. That would
need evidence that the loop really is this model's shared workspace, together with no H1 pattern
when it is removed.

## 8. How this fits the rest of the project

- **The tracker.** John ruled on 2026-11-20 that the project goes ahead in stages as a tracker of
  the theories of consciousness (`docs/2026-11-20-consciousness-tracker-kickoff-proposal.md`). If
  that goes ahead, a result here would be one prediction under the Sentient Horizons account. It
  might also bear on any listed theory that puts recurrence at its centre. Whether it does depends
  on how that theory's core claims are fixed, which this note has not checked.
- **The hibernation.** The project hibernates from 2027-01-04. Design work on paper costs nothing
  and can be done before then. Any run costs money.
- **Order of work.** The three-hypotheses proposal puts H2 (the split, by taking the speaker cue
  out of the input) first and H1 next. This note does not propose changing that order. It offers
  a candidate design for H1.

## 9. Cost and machine

- **This Mac cannot run it.** It has 16 GB of memory and the model needs at least 32 GB.
- **Removals B and C need a rented machine.** They require reading and changing activity inside
  the model while it runs. On NVIDIA hardware the card lists the Hugging Face software among the
  supported frameworks, which is the usual route for that kind of access. Whether the model's
  4-bit format can be hooked into this way has not been checked. A rented card with 32 GB or more
  of the newer NVIDIA generation would be needed (RunPod, under the standing rule that heavy runs
  go there).
- **No price has been looked up.** Before any go, the next step would price a short feasibility
  check: load the model, run one prompt at one, two and three passes, and confirm that the
  message can be read and replaced. That estimate and its ceiling go to John first, as with every
  spend.

## 10. What would come next, if John wants it

1. **John rules whether this goes on the list at all**, given the tracker and the hibernation.
   No cost.
2. **A design at version 0.1, on paper.** It would fix the three removals, the swap source for
   Removal C, the comparisons, the normal-range bound, the battery and the reading rules, and then
   go to the inside review pass, as experiment 09's design did. No cost.
3. **A priced feasibility check on a rented machine**, only on John's go.

## Sources read for this note (all on 2026-11-20)

- Thinking Machines Lab,
  [Introducing Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/).
- Thinking Machines Lab,
  [TML-d24-varloop-research model card](https://thinkingmachines.ai/model-card/tml-d24-varloop-research/).
- Goodfire,
  [Interpreting Inkling 2 Mini](https://www.goodfire.com/research/interpreting-inkling-2-mini/)
  (read up to its section on decoding the loops, where the page text was cut off).
- This project: `docs/2026-11-20-three-hypotheses-and-refocus-proposal.md`,
  `docs/split-removal-test-design-2026-10-24.md`, `STATUS.md` (the 2026-10-24 evening entry on the
  split test's failure), `spec/minimum-viable-mind-proposal-v0.1.md` (the recurrent-integration
  component) and `spec/theory-instrument-ledger.md` (item 6, recurrent and predictive processing).
