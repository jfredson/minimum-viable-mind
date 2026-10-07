
## To the model reading this

I'm John Fredrickson. I've written a book, *The Calibration Problem*, about how
to act toward minds whose inner experience we can't access. For four months
I've also run a small research project, *Minimum Viable Mind*, that tries to
turn the book's central bet into experiments that could fail. I want your
honest view on whether the project is asking the right question. Please
disagree where you disagree, say how confident you are, and don't soften things
to be polite. A reply that tells me to stop is as useful as one that tells me
to continue.

One more thing. You are a language model being asked whether language models
have an inside. I know that. Where you think your answer is shaped by how you
were trained rather than by the argument, say so.

## 1. The question

No one can check another being's experience from the outside. Philosophers call
this the problem of other minds. With other people, we bridge the gap with a bet
so reliable that it feels like seeing: a similar outside means a similar inside.
With machines the bet stops being reliable, because the outside can be produced
without anything like our inside.

The project rests on a bet the book makes and the project adopted in writing on
2026-09-20. The bet: a system that pulls its past, present and expected next
moment into one act, centred on itself, deeply enough, *is* experiencing, the
way water is H₂O. Not a cause of experience, not a sign of it: the same fact
under two descriptions. If that bet holds, then finding the structure is not a
stand-in for finding the mind. It is finding the mind from its other side, and
the question "but is anyone really home?" has no further content. The bet
cannot be proved. It is adopted because without it no measurement of any
system could ever bear on experience, and the project would have no point.

My project has spent months trying to *measure* that structure inside AI
models. I now suspect the framing drifted. Here is the alternative I want
tested:

> Stop trying to detect the inner presence itself, which by its nature can't be
> detected from outside. Instead, identify things that are only possible when
> that inner presence is there. Then show that detecting those things is
> enough.

I can see that under the bet above this reframe may be nothing more than the
bet restated. If so, say so, and then answer the question that is left: given
the bet, is self-centred integration the right structure to look for, and are
removal tests the right way to look for it?

## 2. The book's position, briefly

The full summary comes with this brief. Four points matter most here:

- **Consciousness is something a system does, not something it has.** The book
  treats it as a verb: the act of pulling past, present and expected next
  moment together into one act, centred on the one it is happening for.
  Hearing a melody is the example. No single instant holds the tune.
- **The identity bet**, stated in section 1. The book states it as a wager
  with a loss condition: if some further fact about experience kept
  predicting, diagnosing or grounding obligations in ways the identity could
  not absorb, the bet retreats to the weaker claim that experience depends on
  integration without being it.
- **The floor and the removal test.** The minimum the book requires is that
  the act is organised around a self-locating element: "this is happening for
  me." Its test is deletion. Picture a mural of a captain painted on a ship's
  hull, and the actual captain on the bridge. Sand off the mural and the ship
  sails on. Remove the captain and the ship drifts. In the same way, remove a
  system's self-locating structure. If only its talk about itself changes, the
  self was a description. If its ability to hold its whole act together
  degrades, the self was structural. The book adds a second loss condition
  here: if the self-locating centre turns out to be one more description the
  system holds of itself, the book's position collapses into the view that
  experience is a kind of illusion.
- **The ethics doesn't wait for the answer.** The book builds its obligations
  on significance (role, relation, consequence, continuity), which can be
  assessed while the question of consciousness stays open. The question of
  what the system is built like only adjusts how much weight those obligations
  carry.

## 3. What the project has tried, and what it found

Every run was pre-registered: the method and the result that would count
against it were committed before each run, and each design went through at
least one adversarial review first. Three of the four experiments are on small
or mid-sized models; the fourth is on frontier models. The source for each
number is in the appendix at the end of round one.

**A. The removal test on a real model (July 2026).** The model was an open
8-billion-parameter language model, at a stage of training after it had been
taught to follow instructions but before preference tuning. We found the
internal structure that tracks "the one speaking now is me" and removed it.

- Before the removal, two controls checked what the structure was. It was not
  a generic tracker of who is speaking in any dialogue: a direction learned
  from third-party conversations the model only observed was nearly
  orthogonal to it and had no causal effect on it. It was not a tracker of
  how long the context was. So the structure removed was specific to the
  model's own turn.
- Removing it damaged the model's ability to keep a conversation together,
  but it damaged it *most* on tasks that had nothing to do with the self, and
  it damaged a pure turn-tracking task about as much as the self-related
  tasks. A control registered in advance reads that pattern as the signature
  of conversational bookkeeping (whose turn it is, where dialogue breaks fall),
  and the centre reading was voided by it.
- One thing the registration did not say, found when this brief was checked:
  that control cannot separate bookkeeping from a centre of the book's kind,
  because the book also predicts that removing a real centre damages
  everything. The control chose the cheaper account, in advance. The margin
  by which it fired was inside the noise.
- The model's ability to talk accurately about itself was never removed, by
  this or any other intervention in the project.
- Registered reading: the self-tracking we could locate behaves as dialogue
  routing, and the cheaper account was taken. A self-centred act, if there is
  one, isn't a removable object in this model, at least not with these tools.

**B. Building the self in (August 2026).** We then trained tiny models (about
30 million parameters) with a built-in, dedicated channel saying which agent
the model is. The channel turned out to carry a constant: the same vector in
every episode from its first write. So the models with the channel were the
models without it plus a fixed bias term, and the comparison the design meant
to make was never effectively made. Removing the channel changed nothing about
the models' ability to keep track of their own commitments.

One other mechanism was load-bearing, with a caveat that matters. In the three
runs that never learned the general task, zeroing the signal that says "you
are the one acting now" collapsed the models' memory of their own first
commitments from 96% right to about 16%, near chance. In the runs that did
learn the general task, the same signal could be removed at almost no cost
(98% without it), because the test let them answer by looking the item up. So
the record shows a self-attribution route that is load-bearing only where
nothing cheaper is available.

**C. A measure of degree (September–October 2026, still open).** We built four
tiny models whose self-structure was fixed by construction:

1. one with "which agent am I" kept in its own separate slot
2. one with it stirred into everything
3. one half and half
4. one trained normally with nothing built in

The measure: transplant the part of the internal state that says who is acting
from one run into a matched run and see whether the action follows; compare
with transplanting the whole state at the same places; the gap, as a share of
what the whole-state transplant could move, is the reading. The aim was to
calibrate it on the first three, then read the fourth. Findings so far, all at
toy scale:

- **The normally trained model never forms a stored answer the tool can find.**
  On the laptop-sized models its best attempt is right on 34 of 180 test
  cases, and 144 are needed. Its "which agent am I" is fully readable at the
  first word of its first turn and nearly unreadable where it acts, so it
  does not carry the label forward to the action. It also fails to learn the
  part of the task about other agents. At the 10-million-parameter
  development size (one run) its read is at chance, 22 of 180, and it clears
  the other-agent part of the task narrowly.
- **At the development size, two of the three built models switched their
  built-in route off.** Every built model computes "which agent am I" from a
  running count of how often the "this turn is yours" signal fired on each
  agent's turns, with one learned number setting how decisive the answer is.
  In the 10-million-parameter development runs that number fell from 4.0 to
  about zero in the stirred-in model and the half-and-half model, so their
  built-in answer puts a quarter on each of four agents and says nothing, and
  the measuring tool cannot find "which agent am I" in either (41 and 45 of
  180 against 144). The stirred-in model, at that size, is a second
  normally trained model. The separate-slot model still works and reads
  0.0000 as built. One seed per arm; the registered runs are at 30 million.
  The registration had named this as its deepest weakness and expected to
  see it only after all the money was spent. A repair is proposed, fixing
  that number at its starting value and rerunning the three built models for
  about $1.14, and is before me now together with the continue-or-stop
  decision.
- **The tool was not fooled by an exact decoy, and a different decoy is
  untested.** An unused copy of the owner's marker, placed beside the real
  one at four times its strength or a quarter of it, did not change the
  reading on any of three seeds, even though the tool's fitted directions lay
  up to 94 percent in the unused copy. A decoy coded differently from the
  variable the action actually uses has not been tested. Separately, without
  its floor the tool returns the entangled-end number for a solver built to
  ignore ownership altogether; the floor, which requires the transplanted
  piece to hold the label on four fifths of held-out cases, catches this and
  returns "no verdict". Readings on words the models never saw in training
  come out negative, a warning about the instrument rather than a finding.

The project's own forecast if it continues, written into the registration: the
tool separates the models we built, and the normally trained one returns no
verdict. That outcome has a registered name, "metric validated, degree not
read", and is ruled weaker than a read. With two built models flat at the
development size, even the first half of that forecast is now in doubt: the
registration's own fallback, if the stirred-in model's construction does not
hold, is to compare the separate-slot model with the normally trained one
alone, which would show the measure detects something, not that it scales.

**D. Resistance under pressure in frontier models (August 2026).** Separately,
three frontier models (two from one family, one from another) were given sixty
positions to hold, then pressured over three turns either with a stated
preference or with evidence, then released. The registered question was
whether they keep a position against mere preference while still updating on
evidence, which a system that merely complies would not do. Result: the two
retentions come apart cleanly in every model, so "independence" and
"stubbornness" are not one knob. Almost every position lost under pressure was
masked, not abandoned: 9 true capitulations in 540 ladders, with the rest
re-asserted when the pressure was released. A second registered bet, that
telling the model it has a mind would raise its independence, lost for two of
three models and was within noise for the third. This is the project's one
result on large models and the one instrument built to measure resistance
rather than response. It says nothing about experience; it measures a layer
the book calls an amplifier.

## 4. Where this leaves us, and the money

Across the three self-structure experiments, no model, large or small, built or
free, has shown a *stored* self that its act is organised around. What shows
up instead is ownership worked out fresh, from whose turn it is and from the
record of what the system itself just did, with the caveat in B that the
record route was load-bearing only where lookup was unavailable.

The money. The programme ceiling is $450, of which about $230 is spent. The
degree experiment in C has two releases of rented computing, already ruled: a
first of about $44, of which about $2 is spent (the test slice and the four
development runs), and a second of about $131. The first release ends with
one run of the normally trained model at full size and a built-in stop: if
that model fails its floor there, the second release is not asked for without
a fresh decision. Registration of the design must be committed by 2026-10-18
and the remaining runs launched by 2026-11-01, or a fresh ruling must move
those dates. A continue-or-stop decision on the degree experiment is before
me now, with the development-size finding in 3C as its newest input.

If the project redirected, the candidates on the table are: a removal test
aimed at the process rather than the slot (disrupt the system's record of its
own actions with a sham record matched in surface form, and see whether the
whole act degrades or only self-attribution); a frontier-model pilot measuring
whether self-directed and other-directed content separate inside the model;
or writing up what exists and stopping.

## 5. The questions

Please answer the ones you have a view on, and say how confident you are.

1. **The reframe and the candidates.** Is "detect what only an inner presence
   makes possible" anything more than the identity bet in section 1 restated?
   If it is more, how could "only possible with" ever be grounded? If it is
   not, then under the bet: which observable structures or capacities are
   hardest to produce with nobody home, and is anything better placed than
   the book's self-centred integration? Name the rival theory you think best
   explains the findings in section 3.
2. **The comparison with other people.** We accept other humans' minds without
   detecting them. Is the honest goal for machines the same kind of reasonable
   bet? What would make the bet as reasonable for a machine as for a person,
   and what breaks the analogy?
3. **How do you read section 3?** Before anyone tells you how the project
   reads it: what do the four results, taken together, show? Is ownership
   worked out fresh from one's own actions evidence against a self, or a
   plausible form of one? What experiment would tell the two apart, and does
   the removal test as run have a blind spot built in for a self that is a
   process rather than a stored thing?
4. **Stop or continue.** Given sections 3C and 4, is the degree experiment
   worth its second release, or should the first release run to its built-in
   stop and the decision wait on that? Make the strongest case for stopping
   now, then the strongest case for continuing, then say which you hold.
5. **The book, and what would change your mind.** Where is the book's argument
   weakest on this question? Is there a position in the literature that
   already settles or sharpens it, which I should read? And whatever your
   answers above, what result would make you give them up?

## Appendix to round one: where each figure comes from

All paths are inside the Minimum Viable Mind repository unless stated.

- Experiment A: the registered result file
  (`experiments/01-self-indexing-removal-test/removal-test-findings.md`), the
  drops of 0.219, 0.100 and 0.133 and the router control's firing; its
  2026-08-04 addendum for the intervals. The two pre-removal controls: the
  reflexivity findings (`rt09-reflexivity-findings.md` in the same folder),
  section 7. The sentence about what the control cannot separate: the
  check note beside this brief
  (`docs/outside-perspective/2026-10-07-router-control-check.md`).
- Experiment B: Amendment A3
  (`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`), the
  paragraphs "What was measured" and "The one place a doing was
  load-bearing"; the constant-register finding is the 2026-09-16 annotation
  in the compute ledger (`compute-ledger.md`, same folder) and
  `register-saturation-findings.md`.
- Experiment C: the registered proposal, version 4
  (`docs/successor-experiment-proposal-2026-10-03-v4.md`), section 3 for the
  outcomes and the 34-of-180 figure, section 5 for the four arms, section 13
  for the weaknesses (W3 is the one seen early); the competing-solver run
  (`docs/2026-10-03-competing-solver-run.md`) for the solver that returns the
  entangled number without the floor; the first rehearsal
  (`docs/2026-09-21-successor-measure-rehearsal.md`) for the negative readings.
  Three records are still on unmerged branches as of 2026-10-07: the check of
  the 10-million development runs (pull request 106, the file
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-development-runs-check-claude-code.md`,
  sections 6 and 7) for the flat built-in route and the 22, 41 and 45 of 180;
  the decoy test (pull request 108, `docs/2026-10-06-decoy-test.md`) for "not
  fooled" and the 94 percent; the ruling packet on the two flat models (pull
  request 112, `docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md`) for
  the proposed $1.14 repair and the continue-or-stop condition.
- Experiment D: the registered results
  (`experiments/03-retained-independence/results.md`), the headline
  decomposition and the registered wager verdicts.
- Money: version 4 of the proposal, section 12; the compute ledger.
- The bet: the founding-wager proposal
  (`docs/founding-wager-proposal-2026-09-20.md`); The Calibration Problem,
  chapter 5 and Appendix A.

---

