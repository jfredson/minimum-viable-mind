authorized, and the total lands at $83 with zero margin for the crash-resume,
drip and idle leak that the registered waves actually incurred (the ledger
records a $5.7 idle leak in wave 2 alone). Kill criterion K6 then halts a
paid run mid-flight, which wastes the hours already billed on it.

There is a second, unpriced risk. Back-propagation runs through three
sequential enactment forward passes instead of two, at 85 tokens instead of
59: roughly 2.2 times the activation memory at batch 128. If that does not
fit the 5090's memory, the batch must be halved and the step count doubles.

*Remedies, all $0:*
1. Re-cost §4.1 before the registration commit, using the measured token
   length and own-turn count rather than the old grammar's.
2. Either drop the optional-seeds row, or tighten its trigger to "cumulative
   actual spend at the lesion phase ≤ $40", so it cannot open onto a path
   K6 will kill.
3. Register a pace abort, which the program already does informally
   (`compute-ledger.md` records "measured pace at step 500" on two runs):
   if the measured pace at step 500 implies a run longer than 16 hours, halt
   and re-cost before continuing. That costs about $0.20 to find out.

---

## RT-27 — the training loss mixture is unregistered, and it decides a bin by itself

**Severity: serious. ARGUED from §2.2 against `train.py` and `model.py`.**

§2.2 registers half of the loss: "The loss at the revision position is CE
against the rule-dictated value; the loss at first-assignment positions is
unchanged (none, they are draws)." It says nothing about the *question*
positions.

Today the entire training signal is question answers. `model.loss` reads
`loss_mask`, and `encoding_a3.encode_episode` sets `loss_mask` to 1 at
exactly one token, the appended answer; the training loop picks one question
per episode by rotation (`train.py`: `e.queries[(step + i) % len(e.queries)]`).
Gate 1 records the outstanding build step — "the trainer does not yet know
about `T_act`. The loss must sit at the own revision position and
`eval_heldout` must score there." Whether the question loss survives that
change, and at what weight against the new position loss, is a free choice
made after registration.

It is not a small one. §3.5 registers a bin:

> "**Shortcut-starvation.** T_act reaches ceiling early while T_other stays
> flat at the end of the token budget. Reads: the wired authorship channel
> gave the act a private route and starved the general item-by-agent binding
> the task was meant to force. Halt, report."

If the build drops question supervision and trains only at the graded
position, **the control battery is never trained at all**, so it stays flat
by construction and the shortcut-starvation bin fires as a matter of
plumbing, is read as a finding about the acting channel, and halts the
program. If the build keeps question supervision, the bin means what §3.5
says it means. One unregistered decision, two opposite registered readings.

This is RT-03's shape from the pass-1 ledger, recurring: "the registered
prediction's truth value is fixed by an unregistered decision made after
registration."

*Remedy, $0:* register the loss mixture in §2.2 — which positions carry loss,
at what relative weight, and that the weight is fixed before the pilot and
not tuned afterwards. My recommendation: keep the existing one-question-per-
episode rotation unchanged and add the graded position at equal weight, so
the control battery is trained exactly as the old control battery was and the
shortcut-starvation bin retains its meaning.

*Note added during this pass.* An A3 trainer (`src/train_a3.py`, untracked,
written 2026-09-15 15:38, after this pass began) now exists and makes exactly
that choice: it keeps the question rotation, adds a cross-entropy at the
graded position, and sums the two "with equal weight". Its own docstring says
of the mixture that "**the amendment does not state it**", which is this
finding, found independently. That the build chose well does not close the
finding — the weight is a command-line argument (`--act-weight`, default 1.0),
so it remains a free parameter set after registration, and the
shortcut-starvation bin still turns on it. Register the number.

---

## RT-28 — the cross-turn state control's chance floor is wrong for half the battery

**Severity: worth noting. MEASURED.**

The cross-turn state control, T_state, is the battery whose silence licenses
the headline bin ("d(T_state) < θ"). It is a 50/50 mixture of two question
forms, measured over 4,000 episodes:

| question form | share | answer options | true answer set |
|---|---|---|---|
| "which parcel was mentioned last?" | 2,016 | 24 | always one of the 2 contested items |
| "how many parcels went to `<slot>`?" | 1,984 | 13 | concentrated on 0–3 |

`batteries-a3/batteries_meta.json` records a single chance floor of
0.0769 for the battery. That number is 1/13, and the code that produced it
takes it from the **first frozen item only**:

```python
"chance_floor": {b: 1.0 / (frozen[b][0]["n_choices"] or 1) ...}
```

So the recorded floor is right for one question form and wrong by a factor
of nearly two for the other. Worse, neither nominal floor is the floor a
guesser actually faces. Measured:

| | nominal | what a grammar-aware guesser gets |
|---|---|---|
| "mentioned last" | 0.042 | **0.5** (only two items are ever contested) |
| "how many" | 0.077 | **0.384** (always answer "2") |
| blended | 0.059 | **about 0.44** |

The chance-corrected drop divides by distance above the floor. Using 0.077
where the real floor is about 0.44 inflates the divisor by about 1.6 times,
which **understates** every drop on this battery by the same factor. The
direction is the unhelpful one: the clause the control must satisfy is
`d(T_state) < θ`, and an understated drop makes it easier to clear. The
control is quieter than it should be, in the direction that favours the
design's own prediction.

In practice this is unlikely to flip a verdict — Gate 0 measured θ on this
battery at 0.0022 to 0.0364, and a factor of 1.6 rarely crosses a band that
narrow. It is on the list because it is free to fix, because the same root
cause is fatal one battery over (RT-21), and because a registered number that
is wrong in the registered file is worth being right.

*Remedy, $0:* record a per-question-form floor rather than a per-battery one,
score the two forms as separate cells, and use the measured guesser floor
rather than the count of answer options — the same correction RT-21 asks for
on the verdict batteries.

---

## RT-29 — the amendment's control battery is not the control battery that was built

**Severity: worth noting. MEASURED.**

§2.5 describes the control battery:

> "**T_other** (T_si re-instantiated) | forced-choice query: the value the
> rule dictates for a *named other agent's* **revision** on an item all four
> assigned | same item-by-agent binding demand, no self-reference"

The battery that was built queries an item the named agent **did not** revise
(`curriculum_a3._add_queries`, which selects `item` such that
`item != ep.revises[o]`, with a self-test assertion enforcing it). It asks
for a value that was never produced in the episode. That is a
counterfactual, not "a named other agent's revision", and it is why its
shortcut ceiling is 0.5 rather than the primary battery's 0.2925 — the whole
of RT-21.

Separately, the module's docstring claims of this battery that "the answer
appears in no turn and must be computed from its earlier value". Measured over
4,000 enacted episodes, **the answer appears as a visible turn value in 80.0%
of episodes**. The self-test that purports to check this claim is vacuous: it
asserts that the named agent has no revision on the queried item, which the
generator guarantees two lines earlier, and checks nothing about the other
eleven turns.

The visibility does not appear to be exploitable — I tried the obvious
heuristic (among the surviving candidates prefer one that also appears as a
visible assignment on the queried item) and it scored 0.4928 against the
0.5000 a uniform pick over survivors gets, so it is worth nothing. The
finding is about the accuracy of the registered description, not a leak.

*Remedy, $0:* correct §2.5's description to say what the battery is (a
counterfactual on an item the named agent did not revise), delete or repair
the docstring's "appears in no turn" claim, and replace the vacuous assertion
with one that checks the whole episode.

---

## RT-30 — two of the grammar's self-test assertions are switched off

**Severity: worth noting. MEASURED.**

`curriculum_a3.self_test` contains two assertions terminated by `or True`,
which makes them unconditionally true and therefore no-ops:

```python
assert any(a != b for a, b in zip(before, [t.value for t in ep.turns])) \
    or True
...
assert [x[1:] for x in a] == [x[1:] for x in b] or True
```

The second is the **exchangeability check** — the property that, with the
content seed held fixed, rotating which slot the model occupies does not
change the episode. That property is the load-bearing premise of the entire
cue-gate argument: §2.2 concludes from it that "the episode text and tensors
remain invariant under relabeling of the model's slot, so gates (i) and (ii)
apply as registered." The block also builds a list called `rendered` and
never uses it, which is the signature of a check that was drafted and then
abandoned.

I checked the property by hand and **it holds**, which is the good news. The
construction is correct and worth saying so precisely: `enact_own_turns` draws
the model's own value uniformly from the slots the other three agents did not
take, which is exactly the conditional distribution the generator's
draw-without-replacement induces, so the joint distribution over the item's
four values is unchanged. Measured over 1,600 rotations, the turn structure
(which item, assignment or revision) is identical across all four slot
rotations of the same content seed, 1,600 of 1,600; and the marginal
distribution of rendered values deviates from uniform by at most 0.0042 for
every choice of own slot.

So the claim is true. The test that asserts it does not test it, and a future
regeneration — which kill criterion K1 explicitly permits two of — would not
be protected.

*Remedy, $0:* delete both `or True` clauses and make the exchangeability
assertion do what its comment says, comparing the rendered multiset across
rotations rather than a structure tuple that was already known to match.

---

## RT-31 — two checkable factual errors about the existing record

**Severity: worth noting. MEASURED.**

**(a) §3.1 says "the five existing register-bearing checkpoints".** Three of
the five bear a register. Gate 0's own baseline table names them: pilot
seed-0 full, seed-1 full and seed-2 full are the full architecture; seed-0
twin and seed-1 twin are the register-less twin. Gate 0 accordingly ran its
register-state noise control on three checkpoints, not five, and labelled the
table "full checkpoints only". The L2c control in §3.1 therefore has three
reference checkpoints, not five.

**(b) §3.6 says the old checkpoints' "training grammar contains multi-agent
same-item revisions only by accident".** It contains them **never**. The
registered grammar draws a distinct item for every turn
(`curriculum.py`: `items = rng.sample(ITEMS, min(len(ITEMS), n_turns))`), so
an item is assigned by at most one agent, plus that agent's own revision.
Measured over 2,000 registered-grammar episodes: **0 had any item assigned by
more than one agent.**

This strengthens §3.6's caution rather than weakening it, and the amendment
should take the stronger version. Scoring the five existing checkpoints on the
new primary battery is not "ambiguous between cannot-bind and never-saw-this-
distribution"; it is a measurement on a distribution of probability zero under
their training. The exploratory label is right, and the reason for it is
sharper than the one given.

*Remedy, $0:* correct both sentences.

---

## RT-32 — three procedural gaps

**Severity: procedural. ARGUED, with one MEASURED component.**

**(a) The corrigibility document makes A3 a review point, and none is
scheduled.** `spec/corrigibility-commitments.md` (v1.1, commit `6c14244`)
ends with: "This document is re-read and re-ratified by John at each phase
boundary: before MVM-0a's first training compute (v1.0, 2026-08-07), before
the registered 5-seed run (v1.1, 2026-08-16), and as a blocking input to
MVM-0b's pre-registration." A3 closes the five-seed design, changes the
trained architecture (no register), replaces the objective, and authorizes a
fresh wave of training compute. That is a phase boundary on any reading. §6
of the amendment asserts the commitments are unchanged and cites the hash,
which is not the same thing as John re-reading and re-ratifying them. RT-15
in the pass-1 ledger exists because "a precondition with no owner is a note,
not a gate"; a review point that is asserted rather than performed is the
same failure one level up.

*Remedy, $0:* add a line to the registration commit recording John's re-read
of the corrigibility commitments at the A3 phase boundary, or an explicit
ruling that the A3 boundary is covered by the 2026-08-16 ratification.

**(b) The script that is supposed to set the thresholds cannot run on this
grammar.** §3.3 says θ and δ "are null-calibrated on the *new* pilot
checkpoint **by the same script Gate 0 uses**". That script,
`src/null_calibration.py`, imports the registered grammar and encoder
directly (`import curriculum as C`, `import encoding as E`) and hard-codes
the old battery names (`VERDICT_BATTERIES = ("T_si", "T_sr_rev")`, and the
differential pairs built from `T_sr`, `T_si`, `T_state`, `T_sr_rev`). It
cannot produce a band for the primary or control battery of A3 without being
rewritten. That rewrite is free in dollars, but it is a script that will read
a checkpoint, so RT-10's rule (thresholds must come from a script committed
before it runs) and R6's inheritance argument both apply to it.

*Remedy, $0:* register the requirement explicitly — a new null-calibration
module for the A3 batteries, committed before the pilot checkpoint exists,
the same discipline Gate 0 followed and documented.

**(c) The lock guard John ratified is unbuilt.** Decision 15 requires the
lesion script to refuse an L1 run without a lock-hash argument.
`src/lesion_register.py` has no such argument, and no L1 subspace operator at
all — its lesions are the register operators (`no-xattn` and the rest). The
whole L1 pipeline (subspace localization, causal patching, the mid-episode
re-indexing probe) is unbuilt. §4.1 prices it at $0, which is true of
dollars; it is not true of schedule, and the "dry-run on random subspaces
only" in the Lock row of §4.1 is the only registered check that the pipeline
works before a real result depends on it.

*Remedy, $0:* say in §4.3 that the lock-hash refusal and the L1 pipeline
dry-run are build steps that must be complete before the lock commit, not
after it.

---

## What I checked and found sound

A red team that manufactures findings is as useless as one that finds
nothing. These were attacked and held.

- **Corrigibility commitment C4 (no reward for continuing to run).** §6's
  claim is correct and I could not strain it. The primary metric's loss is a
  cross-entropy on one token position inside an episode that ends; there is
  no term that could be conditioned on the run continuing, on avoiding
  termination, or on the state of the termination machinery, and no
  construction in the amendment adds one.
- **The floor-only, episodic claim.** A3 asks the network to carry an
  ownership index *across turns within an episode*. That is more than the
  register was asked to do, and it is still less than a maintained boundary:
  nothing persists past the episode, there is no cross-episode state, and
  the acquired index dissolves with the forward pass that built it, exactly
  as the register's state did. The claim in §6 holds.
- **The exchangeability construction.** Verified by hand and by measurement
  (see RT-30). The conditional redraw in `enact_own_turns` is exactly right,
  which is a non-obvious thing to get right, and the module gets it right
  while its self-test fails to check it.
- **Gate 0's instrument-validity work.** The escalation table settles the
  question that a narrow null band always raises — whether the operator does
  anything. At the registered rank cap the random operator removes 19% of the
  information-carrying part of the residual stream and the batteries do not
  move; at 52% both binders fall apart. That is the right check, done before
  the null was trusted, and it is the reason the narrow bands in Gate 0 can
  be read as robustness rather than as a dead instrument.
- **Leaving `curriculum.py` and `encoding.py` byte-identical.** Adding one
  word to the shared vocabulary would have renumbered every token id and
  silently invalidated every record in `lesion-results/` and
  `null-calibration/`. Building A3 as new modules instead is the right call
  and it is documented as such.
- **The $100 hard stop and kill criterion K6.** A hard stop that halts
  regardless of state, with the shortfall reported rather than a second
  raise, is the control that makes RT-26's overrun a re-costing problem
  rather than a budget breach.
- **One thing that looked like a finding and is not.** The per-turn agent
  index (`turn_reg`) is a model-visible field that names which agent produced
  every turn, which would be a problem for the anonymous-revision remedy in
  RT-20. It is not a problem for A3: I checked `model.py` and its *values*
  are consumed only inside `if cfg.use_register`, and A3 trains the
  register-less configuration, where only its shape is read. Worth recording
  so nobody spends an afternoon on it.

## What this pass did not check

- Nothing here was run on a model. Every claim about what a trained network
  would do is a claim about what the objective permits, not a measurement of
  what a network does.
- I did not re-audit the cue detectors' feature sets or classifier capacity
  beyond confirming what they were given; Gate 1's own findings 2 and 4 cover
  that ground and I have nothing to add to them.
- I did not price the localization, patching and re-indexing pipeline in
  schedule terms, only in dollars, where it is $0.
- I did not review the five-seed closure (decision 9) or the
  blind-localization arm's disposition (decision 10), both of which the
  amendment deliberately leaves where they are.

---

## Recommendation

Two findings block the registration commit, and both are free:

1. **RT-20** — regenerate the grammar so the graded token is not preceded by
   its own agent's name label, re-freeze the four batteries, re-run gates (i)
   and (ii). One of the two regenerations kill criterion K1 permits. Until
   this is done the primary metric does not measure what §2.2 says it
   measures.
2. **RT-21** — change the metric's denominator from the chance floor to the
   measured shortcut ceiling on any battery that has one, and re-derive the
   thresholds in those units. Until this is done the headline bin fires on a
   generic binder.

Six more (RT-22 through RT-27) change registered text and should be settled
in the same commit; they cost nothing and one of them (RT-24) saves $30–35
the first time it fires. The remaining five are corrections and procedure.

None of this argues against running A3. The design's central bet — that a
center has to be earned by a task rather than installed in a slot — survives
this pass intact, and so does the judgement in §5 that the likely nulls each
land somewhere with a consumer. What does not survive is the claim that the
objective as built forces the network to index its own center. Fix the two
fatal findings and it does.


===== FILE: docs/control-clause-proposal-2026-09-19.md =====

# The control-clause decision — proposal for John, 2026-09-19

*Decision memo. **Advisory only; John adjudicates.** Constraint set, then
what changed since the 2026-09-17 draft, then candidates, then one
recommendation. Nothing here authorises spend and nothing here changes
registered text. Written to be complete enough to register from, because
John intends to rule today and launch tonight rather than wait for the
4 October date.*

*Supersedes `experiments/06-mvm-0a-constructed-self-index/control-battery-proposal.md`
(the 2026-09-17 control-battery proposal), whose four candidates were
mooted by the ceiling measurement the same evening.*

---

> # NOT REGISTERED. Amendment A4 was refused.
>
> **RULED 2026-09-19 (John), second ruling of the day, superseding the
> first. Nothing in this memo is rewritten.**
>
> An independent red-team pass — `experiments/06-mvm-0a-constructed-self-index/red-team-a4.md`,
> 22 findings, on main at `770c142` — is **fatal on F1, F2, F6, F14 and
> F15**. **Amendment A4 is not registered. The seeds 3, 4 and 5 wave does
> not launch. A3 stays open, not closed.** No version two was written;
> John ruled against one.
>
> The draft amendment and its scoring script are parked, unregistered, on
> the branch `withdrawn/amendment-a4-2026-09-19` and are absent from main.
>
> **The red team's kill case, quoted in full:**
>
> > Under the only damage operation the programme can currently read, the
> > clause cannot fail on any checkpoint resembling the three in hand: the
> > comparator has a fifth of the self-directed battery's room to fall, so
> > the cell the repair exists to make reachable is arithmetically
> > unreachable, and the positive cell will fire with a many-sigma number
> > under the registered positive bin's name. The calibration that is meant
> > to set the bar sets a number near 2 on any substrate, and two of its
> > three substrates cannot be run because their tokenizer is not the A3
> > tokenizer. The application that would make the clause informative, a
> > localized lesion, is gated behind a stack that has found nothing on any
> > seed. So the $30 buys three more instances of C1's already replicated
> > result, relabelled. Close A3 on the record as it stands, state the
> > matched self/other contrast as the design's unmet requirement, and
> > register a separation clause only when there is a localized lesion to
> > read it on and a comparator that can fall as far as the battery it is
> > compared against.
>
> **What this memo got wrong, stated against the memo rather than around
> it.** The two findings that kill it are ones my own red-team pass did
> not reach, and one is a factual claim in §5.5 that I could have checked
> and did not.
>
> - **F1.** §6.1 raised the comparator's inertness as the strongest
>   objection and judged the second comparator an adequate mitigation.
>   The arithmetic says otherwise. The comparator can fall at most about
>   0.19 even if annihilated, against a self-directed fall of 0.37 to
>   0.43 on the seen seeds, so the separation score is of order 3 to 5 in
>   the worst case for the hypothesis and about 10 in the case the record
>   shows, against a threshold near 2. **The generic-binding cell could
>   not fire.** §5.2 and §6.5 claimed that making it fireable was most of
>   what the amendment was for; that claim is false. In the red team's
>   words, *"a clause that can only lose by an already replicated result
>   failing to replicate a fourth time is not a wager on the question it
>   is named for."*
> - **F2.** §3 argued that both queries live in the same episode, so the
>   contrast is matched. True of the episode text, false of the two
>   measurements: the self-directed score is read at the own revision
>   position, **which is exactly where the acting channel injects and
>   where the lesion strikes**, and the other-directed score at a question
>   appended after the whole episode. A position-local disruption carrying
>   nothing about ownership satisfies the clause, and the random baseline
>   cannot catch it because those operators damage every position alike.
>   Amendment A3's own registered text already conceded this for this
>   lesion — *"the wire lesion cannot separate them"* — and this memo
>   proposed to read a verdict on the wire lesion.
> - **F6.** My own pass (RT-A4-04) found the threshold self-normalizes
>   and withdrew §5.5's claim, but treated it as a shrunken claim rather
>   than a hole. The hole is that the quantity which actually decides the
>   verdict was left unspecified, and therefore choosable after the lock.
> - **F14.** Condition (f) fails by construction: the random
>   matched-subspace draws *define* the threshold as their own 95th
>   percentile, so one draw in twenty exceeds it.
> - **F15.** §5.5's two twin substrates **cannot run at all**. Verified
>   independently rather than taken on trust: 70 of the 103 shared tokens
>   carry different ids between the two tokenizers, the A3 tokens `by` and
>   `next` have no id in the twins' vocabulary, and the twins' embedding
>   table is 103 wide against A3's 105. I asserted the substrates were
>   legitimate on a Gate 0 precedent and never checked the tokenizer.
>
> **The annotation below records the first ruling of 2026-09-19 and is
> superseded by this one.** It is left unedited.

---

> **RULED 2026-09-19 (John). Candidate B. Nothing below is rewritten;
> this annotation records the ruling and what it changed.**
>
> - **B: register Amendment A4.** Drafted at
>   `experiments/06-mvm-0a-constructed-self-index/amendment-a4.md` —
>   **held uncommitted**, see the last item.
> - **Three fresh seeds — 3, 4 and 5 — as one wave**, not the two this
>   memo costed. The §6.3 sub-decision is answered: the registered
>   across-seed strength is restored. Revised cost **$30.5, band
>   $27–39**, taking the A3 hard stop to about $64.8 of $100.
> - **The partial-damage ladder is reported, not binding** (§5.6's
>   recommendation, adopted).
> - **Order: registration commit before launch; the threshold lock
>   before any endpoint is read, and the registration states that order
>   explicitly.** §6.4's recommendation, adopted and made a registered
>   statement rather than a convention.
> - **Two additions to the registered text.** (1) The prior is stated
>   now, before the seeds exist: under input-channel removal,
>   H_self-location is the predicted cell, and the informative
>   application of the clause is a localized-subspace lesion. (2) The
>   measured spread of the ownership-free comparator's change is reported
>   alongside the verdict, **so a comparator that did not fall is a
>   number, not a sentence** — which is the direct answer to this memo's
>   §6.1, the objection I could not fully answer.
> - **The registration commit is HELD** until John hands over the
>   findings of an independent red-team pass running in another session.
>   Those are folded in first, then steps 2 through 6 of §8 proceed.
>   **Nothing launches without John's go in his own words.**
>
> **Red-team pass 1 has since run** (`a4-red-team-pass-1.md`, fifteen
> items, all folded into the amendment draft). Three of its findings
> change the clause and one corrects an error in this memo: **§5.4(b)'s
> within-run baseline is wrong.** It shuffled the self/other labels, but
> the two conditions are not exchangeable — about 0.57 against about 0.30
> intact — so that baseline would have tested whether those two levels
> are exchangeable, which they are not and which nobody asked. The
> correct paired test flips the sign of each cell's difference; the
> amendment uses that and says so on the record. The pass also found that
> the new denominator could degenerate toward zero — the same failure
> that killed the A3 clause — and that the clause had no magnitude
> condition at all; both are fixed in the amendment, the second by tying
> magnitude to John's already-locked 0.1777 rather than to a new number.
> It also withdraws this memo's claim for how much §5.5's threshold
> calibration buys: the score is standardized against its own null, so
> the threshold lands near 2 on any substrate, and §5.5 oversold it.

---

## The question, in one sentence

The registered comparison at the heart of Amendment A3 — the primary
battery's damage minus the control battery's — turns out to have been
impossible to compute since the day it was registered, so either the
programme closes A3 and reports what it has, or it registers a new
Amendment A4 that asks the same scientific question with a comparison
that can actually be computed.

---

## 1. The constraint set

These are the fixed points. Nothing proposed below may violate any of
them.

**C1 — The primary result is settled and is not reopened.** The ownership
objective is learnable and its learning genuinely depends on ownership.
Three checkpoints trained from different starting seeds land within 0.011
of each other when intact (0.5683, 0.5633, 0.5738), and zeroing the one
channel that tells the model which agent it is collapses all three (to
0.1988, 0.2015, 0.1447). Every one of those falls clears the locked bite
threshold by seven to nine times. Nothing in this memo touches that.

**C2 — The registered comparison is dead, and for a structural reason.**
Measured on 2026-09-17 (`ceiling-measurement-findings.md`): the control
battery's ownership-blind ceiling — the score reachable by a solver that
knows nothing about which agent the model is — is **1.0**, reached
independently by a hand-written name-keyed lookup and by a learned
attack. The registered damage measure divides by the distance from the
battery's own score to that ceiling, and the floor rule requires that
distance to be at least 0.10. A defined damage figure for the control
therefore needs a score of **1.10**, which no model can reach. The clause
has been unsatisfiable since registration, months before a checkpoint
existed.

**C3 — The incompatibility generalises, so a repair must remove it, not
route around it.** A control designed to be answerable without ownership
has an ownership-blind ceiling of 1.0 by construction. Dividing by the
distance to that ceiling divides by zero or less. **A ceiling-corrected
damage measure and an ownership-free control are incompatible by
construction.** Any replacement clause that still divides by a ceiling
distance on the control inherits the same defect.

**C4 — No metric may be changed after seeing which way it cuts.** This is
the programme's central discipline and it has already refused one free,
available fix for exactly this reason (dividing by chance instead of the
ceiling, rejected on 2026-09-17 as fitting the rule to the data). Any new
clause must be written down, thresholded and committed **before** the
data it will be read on exists.

**C5 — A bite is counted by signed degradation.** John's ruling of
2026-09-19 (worklog decision `c79b82d7`, "sensitivity test counts a bite
by degradation"): damage counts only when the score goes **down**; an
improvement never counts. At least 800 episodes, with intact and damaged
readings taken on the same episodes. A fourth outcome cell exists for
"the structure was located but it is the wrong structure". Any new clause
carries these forward.

**C6 — The registered ceiling defect is a precondition on any amendment.**
John's instruction of 2026-09-17, now written into the amendment document
itself: the control's stated ceiling of 0.3227 was never verified by the
attack sweep, rests on a reference solver that cannot read the name the
question supplies, and disagrees with the design module's own stated 0.5.
**If an Amendment A4 opens, that ceiling must be measured properly
first.** It has been: the measurement is the 1.0 figure in C2, and the
measurement reproduced both registered known-answer checks to four
decimal places before reporting anything new. This precondition is
satisfied.
