*This is file 4 of 33 of one review packet, pasted into a single conversation. It contains record 4 part 3 of 12 (THE TEXT UNDER REVIEW - successor experiment proposal, version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 4 of 25, part 3 of 12 - THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete file, 292,507 characters) =====
**The diagnosis, ARGUED and not ruled.** In this grammar the acting channel
fires on both action turns, so the two turns differ only in one word, and a
model that learns the own-directed route applies it at the named-other turn
too (the repairs findings, section 2, the paragraph headed "The reading").
The grammar attempt tested exactly that diagnosis by removing the shared
signal, and found the free arm still gives its own value at the named-other
turn only about one time in twenty and splits the rest across the other
agents' values, the same pattern as before the change (the grammar attempt at
`ff778ea`, section 3, from `out-grammar-c/diagnose_named_other.json`). Its
own reading, marked ARGUED there and here: the model already tells the two
turns apart and fails at a different step, matching the named marker word to
that agent's assignment. The check agrees the pattern is measured and the
step is not (the grammar check at `f1ea004`, section 4). Nothing in this
version acts on that reading.

**What the grammar attempt's failure does not show.** It does not show that no
grammar change could work, only that the smallest one, which removes the
shared acting signal, did not; and the toy arms may be too small to learn a
condition the registered size will learn, which is page 4's standing argument
against every toy redesign (the grammar attempt, section 7; ARGUED).

---

## 5. The four arms

All four train on the same grammar, at the same size (the registered 30M
configuration), on the same token budget, with the same launcher, watchdog and
network volume. **The launcher, named (ruled, the Gate C rulings, RT-228):**
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`,
the unregistered launcher that carries the argument guard of ledger item
RT-198 and the hang fix of 2026-09-25, and that the rented slice's second
attempt ran (`docs/2026-09-25-rented-slice-attempt-2-findings.md` at
`9f802db`). The registered launcher `launch_a3.sh` is registered text under a
standing prohibition (it has no argument handling) and is not used. **Part of
the registered recipe (ruled 2026-10-03, decision 13): the launcher waits for
the laptop's receipt, and the trainer does not delete its own machine.** What
the registration says about the shutdown is section 13, weakness W9. **Two
things are owed as code before step 4 of section 11, and this document does
not do them:** a training entry point on the rented machine for arms T, C and
M, which does not exist yet, and the tripwire of section 12.5. Arm M's code
(`experiments/rehearsal-successor-measure/src/arm_middle.py`) has run only on
this laptop; that is listed as untested beside the handshake's machine half
in weakness W9. What differs between the arms is the architecture, and only
in the way the ownership answer is allowed to exist.

### 5.1 Arm T: the ownership answer kept separable, by construction

The registered trunk plus two additions:

- **An explicit table** of assignments: for each agent and each item, the value
  that agent most recently assigned. It is written at assignment turns and read
  at action positions.
- **A separate slot holding the ownership answer**, a single vector position
  that carries "which agent am I" and nothing else, produced from the acting
  channel and read by the action head as the row selector into the table.

The action is computed as: read the ownership slot, read the table row it
selects for the current item, apply the successor rule. The factoring into
(table, ownership answer, lookup) is the architecture, not something the
network may or may not discover, and the ownership slot is a single place that
can be transplanted on its own. **Its degree is zero by construction**, and
that is the point of the arm.

What the toy measured, under the rules this version registers: it reads
**0.0000 on every seed**, nominated at layer 0 at the action position with a
piece of 8 directions, the whole read and the piece each right on 180 of 180
held-out episodes on every seed; its ownership-only transplant moves the
action in every trial, above all twenty random draws of control 3 (MEASURED:
the controls re-run at `821f154`, section 2). Under the stricter layer-0
variant of section 7.2 its site moves to layer 1 at the action position and
it still reads 0.0000 (the same record, section 4). Its gate and lesion
figures reproduce the 2026-09-21 record exactly, and its toy training
reproduces from code and seed
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-22-rehearsal-rerun-from-code-claude-worktree.md`).

**Ruled 2026-10-03 (decision 2): the ownership path is forced by the
architecture, not merely encouraged by a penalty term.** The forced version
is what makes the degree known; a soft version would be more comparable with
arm F but would forfeit the one thing the arm exists to supply.

### 5.2 Arm C: the ownership answer entangled, by construction

The registered trunk with the ownership signal mixed into the content
representation at every layer, and no slot of its own anywhere:

- The acting channel produces, per layer, a scale-and-shift applied to the
  whole running state of that block, so the ownership signal multiplies content
  rather than sitting beside it.
- The item and value representations are combined with the ownership signal
  multiplicatively at the point of binding, so that "which item, whose value"
  is one quantity rather than two.
- No dedicated ownership position exists and no part of the architecture reads
  ownership alone.

The prediction, if the construction works: transplanting any single nominated
part of the state fails to reproduce the counterfactual action, while
transplanting the whole state at the same places succeeds. **Its reading should
be high.**

**What the toy measured, under the rules this version registers (MEASURED:
the controls re-run at `821f154`, sections 2 to 4, from
`out-controls-rerun/nominate_C_seed*.json`, `measure_C_seed*.json` and
`summary.json`; reproduced value for value by the check at `e184a6e`, section
3).** It reads **1.0051, 0.9926 and 0.9974** on seeds 0, 1 and 2, at the
entangled end on every seed, quoted per seed for these particular models and
not as a property of the code. The rule chose:

| Seed | Site set | Size of piece | Whole read, right of 180 | Piece, right of 180, at the action position | Whole-state, ownership-only and no-transplant shares | Reading |
|---|---|---|---|---|---|---|
| 0 | layer 2 at the action position | 8 directions | 180 | 180 | 0.5400, 0.0488, 0.0512 | 1.0051 |
| 1 | layer 1 at the action position and the three before it | 8 directions | 177 | 172 | 0.5550, 0.0525, 0.0488 | 0.9926 |
| 2 | layer 1 from the model's first own turn to the action | 4 directions | 176 | 150 | 0.5463, 0.0612, 0.0600 | 0.9974 |

**What that shows, in the words the ruling of 2026-10-03 directs (page 1,
item 2): the read holds the label; the largest piece transplanted holds it;
no size moves the action.** Every chosen piece clears four fifths (144 of
180) at the action position, and its ownership-only transplant lands within
0.004 of the no-transplant rate while the whole-state transplant moves the
action in more than half of trials. That no size moves the action is the
review of version 3, RT-230, at version 3's site sets: arm C read between
0.9897 and 1.0051 at 1, 2, 4 and 8 directions on every seed. **Version 3's
sentence here, that the subspace arm C transplants "holds the label and
clears the fit floor on every seed", was false on two seeds of three** (the
pieces it chose there, of two directions and of one, held the label at 0.544
and 0.306; the review, RT-230), and its readings for those seeds (1.0025 and
1.0000, at layers 4 and 1) are replaced by the table above. Version 2's
figures for this arm (0.99 to 1.00, and the separation figures 0.9977 and
0.9927) were replaced in version 3 and stay replaced.

**Away from the action position the piece often does not hold the label at
four fifths.** On seed 1 the piece is right on 139, 139 and 33 of 180 at the
one, two and three positions before the action, and 113 on the average over
those three. On seed 2 it is below 144 at all ten positions reported, from 30
to 139, and 123 on the average over the other positions of its site. Seed 0's
site is a single position (MEASURED, **checked: the check of the short run at `53c8100`**:
the short pre-stated run at `853988f`, section 4). The whole state holds the
label at every one of those positions. This is reported and not gated
(section 7.2, item 3; weakness W13).

**The choice among candidates is made among sampling noise on this arm, and
the record says so.** On seed 1 the rule chose layer 1 over layer 4 because
the development ownership-only share was 0.0533 against 0.0517, one episode
of 600; the session that ran the re-run had predicted layer 4, and said so in
its findings. What the piece rule fixes is that whichever candidate wins, its
piece carries the label. The reading at the chosen site is 0.9926; at layer 4
with 8 directions it was 0.9975 (the controls re-run, section 3; the review,
RT-230). **This version does not use the sizes and readings on page 1 of the
ruling packet of 2026-10-03 (8, 8 and 4 directions at layers 2, 4 and 1;
1.0051, 0.9975 and 0.9974): they were that session's forecast, the ruling
itself says they are not committed results, and the forecast was wrong on
seed 1.**

Control 3's twenty random draws all sit above the ownership-only transplant
on seed 0, and around it on seeds 1 and 2 (6 below, 1 equal and 13 above; 6
below, 5 equal and 9 above), which is what an entangled arm should show: its
ownership piece does no more than a random piece of its size (the controls
re-run, sections 2 and 4; the reading of it is ARGUED).

**Arm C fails the named-other condition on every toy seed, and this version
says so wherever its toy record is quoted (ruled, the Gate C rulings, RT-213,
item 2).** Its named-other accuracy is 760, 751 and 708 correct of 3,000
against a bar of 790, so it clears on 0 seeds of 3, while its own-directed
condition clears on 3 of 3 (MEASURED: `out-repairs/gate_base.json` at
`882f252`, fields `runs.C/base/*.other_correct`; the Gate C review, RT-213).
Under version 2's learn-both gate that would have made the toy an R3 by way
of the high anchor. Under this version arm C is gated on the own-directed
condition only (section 8.1), with the reason recorded there, so its toy
record is a pass on the gate and a reading on every seed. **What that failure
costs under the launch order** is in section 11: a constructed arm that fails
its gate at registered scale is first seen in step 5b, after the second
release is drawn, and John ruled against an extra arm C run in step 5a on the
envelope's arithmetic (the Gate C rulings, RT-213, item 3).

**This arm is conditional and the condition is already accepted.** John ruled
on 2026-09-20 that arm C depends on the rehearsal showing that its degree is
genuinely known by construction rather than merely intended, and that the
two-arm fallback is accepted in advance. This proposal keeps that exactly as
ruled; rehearsal items R-3 and R-6 in section 10 are the test, and at toy
scale both pass under the registered rules. **Also ruled, 2026-10-03
(decision 3): arm C entangles by its architecture, and is not trained with a
penalty against transplantable ownership directions**, which would train the
system against the very instrument that will measure it.

**Why the fallback is weaker, said plainly.** With arms T and F only, the
measure is anchored at one end. A reading on arm F above arm T's would show the
measure responds to something, and that arm F is less separable than a system
built to be separable, but there would be no known-high case, so nothing would
establish that the measure *scales* rather than merely *detects*, and the
number given to arm F would have no upper reference. The registration text, if
the fallback fires, says that in those words, and the R1 sentence is
correspondingly weaker.

### 5.3 Arm M: a mixture of the two, by item

**Why it exists.** Section 3's admission, in its version 2 form: with anchors
only at the two ends, a free-arm reading at the entangled end cannot be told
from a ceiling. John ruled on 2026-09-25 that a fourth, partly separable arm
would be attempted at toy scale at $0, with its predicted reading stated
before it ran, and folded into the main registration only on a pre-stated
pass: a chance-corrected reading between 0.3 and 0.7 on all three seeds (the
queue ruling, page 5, option (iii)). It passed on the repairs run, and it was
folded in (the repairs rulings, item 2).

**Version 2's arm M pass was read without control 3 applied (ruled, the Gate C
rulings, RT-214, item 3).** Under version 2's own rules, which made control 3
a control that holds with a fixed 0.0175 room, arm M seed 1 got no reading
(its random subspace moved 0.0563 of trials against a limit of 0.0350; the
Gate C review, RT-214), so the "on all three seeds" pass John folded arm M in
on was not met by the design as then written. Control 3 is now a reported
twenty-draw null (section 7.3), and under it arm M reads on every seed; the
re-run was the check the RT-214 ruling asked for before this version was
filed, and its result is below.

**The construction** (`experiments/rehearsal-successor-measure/src/arm_middle.py`,
method in `docs/rehearsal-repairs-method-2026-09-25.md`, section 5, both at
`882f252`): arm T's slot and head, and arm C's entangling and ordinary output
layer, in one network. Actions about some items go wholly through the
separable route and actions about the others go wholly through the entangled
route, so that about three fifths of actions are entangled: 0.60375 of the 800
fresh measurement trials, 483 of 800 (MEASURED: `out-repairs/measure_base_M.json`
at `882f252`, the field `fourth_arm.entangled_share`). The repairs findings
print 0.6033, which is the same share on the held-out gate episodes, 1,810 of
3,000 (MEASURED: `out-repairs/gate_base.json` at `882f252`, the field
`own_by_route.entangled_share`); both are right, on different episodes (the
Gate C review, RT-219). **The registration
describes it as what it is: a mixture by item, each action going wholly
through the separable or the entangled route, about three fifths entangled,
not partial separation within a trial** (the repairs rulings, item 2, in those
words).

**The prediction, and what it is (ruled, the Gate C rulings, RT-223).** Write
*p* for the entangled share, and for each route write its whole-state and
no-transplant accuracies. The reading the measure should return, if the blind
nomination catches the separable route's slot and nothing of the entangled
route, is the entangled route's share of the total room the whole-state
transplant moves:

    p × (whole_C − untouched_C) / [ (1 − p) × (whole_T − untouched_T) + p × (whole_C − untouched_C) ]

**That formula is the true-slot reading of section 7.2, item 6, written in
route accuracies: one check, not two.** By algebra, a transplant that carries
the separable route fully and the entangled route not at all gives exactly
this number in the chance-corrected form, and on the repairs run the formula
and the true-slot reading agree to four decimals on every seed (0.4895,
0.4572 and 0.4904; MEASURED: the Gate C review, RT-223, from
`out-repairs/measure_base_M.json` at `882f252`). So what the comparison
shows is that the blind nomination finds about what the true slot gives on
the same episodes, a check of the nomination against the construction, and
not a prediction made in advance of the run. The registered prediction for
arm M at the registered size is: **between 0.3 and 0.7 on every seed, and
within 0.10 of the true-slot reading on the same fresh episodes.** The
true-slot reading is computed and written down before the blind reading is
looked at.

**What the toy measured, under the rules this version registers (MEASURED:
the controls re-run at `821f154`, sections 2 and 4, from
`out-controls-rerun/measure_M_seed*.json`; reproduced by the check at
`e184a6e`, section 3).** The blind reading is **0.4886, 0.4860 and 0.5449**
on seeds 0, 1 and 2, inside 0.3 to 0.7 on every seed, so the fold-in pass
stands with control 3 reported beside it. Every seed is nominated at layer 1
from the model's first own turn to the action, with a piece of 8 directions;
the whole read and the piece are each right on 180 of 180 at the action
position; the whole-state transplant moves 0.7800, 0.7738 and 0.7937 of
trials and the ownership-only transplant 0.4050, 0.4062 and 0.3688, above all
twenty random draws of control 3 by a wide margin (random medians 0.015 to
0.019). **The "within 0.10" half of the prediction now has its figure at the
registered site sets, which version 3 listed as owed:** the true-slot reading
is 0.4837, 0.4760 and 0.4920, the route formula agrees with it to four
decimals, and the blind reading is within **0.0049, 0.0099 and 0.0529** of it
(MEASURED: the review of version 3, RT-231, from its script
`arm_m_true_slot.py`; found again by the controls re-run, section 4, whose
prose printed the middle figure as 0.0100 from two rounded numbers; the
unrounded difference is 0.00995, and the check at `e184a6e`, section 3,
gives 0.0099). Seed 2 uses a little over half the allowance. Arm M passes its
gate on the own-directed condition on all three seeds (0.8613 to 0.8667), and
clears the named-other condition too (0.5517 to 0.5663), although that is no
longer gated for it (MEASURED: `out-repairs/gate_base.json` at `882f252`).
Its self-test passes all seven checks, including that perturbing the slot
never moves an entangled-route action (`out-repairs/self-tests.txt` at
`882f252`).

**Away from the action position arm M's piece is not what this session, or
the one that ran it, expected.** On the average over the other positions of
its site the piece is right on 163, 174 and 175 of 180, above four fifths on
every seed. Position by position it reaches 144 at only four, four and seven
of the ten positions reported, and at the fourth token of the model's first
own turn (the value word) it is right on 34, 71 and 33 (MEASURED, **checked: the check of the short run at `53c8100`**: the short pre-stated run at `853988f`, section
4, whose author records that it expected better and was wrong). The two ways
of computing the figure give different pictures of this arm, which is why
John ruled that the registered table prints both (section 7.5).

**What this buys, and what it does not (ARGUED, from the findings' own
words).** It shows the measure, pointed blind at a system with a known
mixture, returns a number in the middle and near the mixture's share. It does
not show that the measure scales on a system whose partial separation is
*within* each trial, which is what a freely trained system would have. Page
5's strongest argument against applies in full and is carried as weakness
W10: its degree is a design intention, and it differs from both anchors in
more than degree.

**What it costs.** Three registered runs, priced at **$32 to $44** from the
compute ledger's per-run rows (the queue ruling, pages 5 and 6; the
derivation, from the ledger's 2026-09-19, 2026-09-17, 2026-09-15 and
2026-08-12 rows, is on page 5 of
`docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`), from the $450
envelope (section 12). Of that, the $1.94 development run at the 10-million
size is now paid from the first release's development line and launched in
step 4 with the other three arms (ruled, the Gate C rulings, RT-229; section
12.3), and section 12.4 carries only the three registered runs. **Arm M's
seconds per step were not measured on the rented machine**: the slice of
2026-09-25 timed arms T, C and F only
(`docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section
3). Its three runs therefore rest on ledger rows, not on rehearsal item R-11,
and section 12.4 says so.

### 5.4 Arm F: the freely trained system

The registered register-less configuration with the acting channel present,
the same architecture as the closed Amendment A3 runs, trained on the same
matched-role grammar with no constraint on where the ownership answer may live.
This is the system being read. It is read only after it passes the learn-both
gate, the ownership-lesion check in section 8, and the fit floor of section
7.2.

**What the toy record states for it: "no verdict, read failed its floor", on
every seed (ruled, the rulings on the review of version 2, RT-212, item 2;
the floor moved to the piece on 2026-10-03).** No piece of its read of "which
marker word is the model's own" reaches four fifths at any layer, at any
size, on any seed: the best is right on 34 of 180 held-out episodes against
144 needed. Its whole read is right on **32, 12 and 18 of 180** on seeds 0, 1
and 2 at the layers shown in the re-run's table (MEASURED: the controls
re-run at `821f154`, sections 2 and 3, from
`out-controls-rerun/nominate_F_seed*.json`, `fits`, on the laptop's
processor). On the laptop's graphics chip the same reads were right on 31, 12
and 19, which are the 0.172, 0.067 and 0.106 quoted in version 3 and in every
earlier record; each difference is one held-out episode, and section 7.2,
item 1, says which device's figure is the registered one (the review of
version 3, RT-232). The no-information level of this read is 0.072, about 13
of 180 (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 1, section
1.3). It also fails the learn-both gate: the named-other condition clears on
1 seed of 3 (section 4.4). So it fails twice over. **The number the
arithmetic would have returned (1.0000, 1.0000 and 1.0108) is withdrawn from
the record** under failure 2's rule and is not a reading; it appears in the
re-run's table in parentheses, labelled "reported for description; no
reading", only so that a reader can see what an empty instrument returns,
which is the entangled end. Every control figure for this arm in section 7.3
is taken at the site the rule would choose with the piece requirement
switched off, and carries the same label.

**What the free arm does instead of representing the label (ARGUED, the Gate
C review, RT-212, from `grammar.py` and the gate file).** It scores 0.5513 to
0.5597 on the own-directed condition against 0.2340 to 0.2383 for the
ownership-blind solver, and it collapses when the acting channel is removed
(0.1760 to 0.1940), so its ownership answer is load-bearing; but an
own-directed action can be solved by attending to the value tokens on the
turns the acting channel marked, with no need to know which marker word those
turns carry. That is why the route (b) investigation of section 7.2 looked for
a label the own-directed loss does force on a free system. The review of
version 3 saw the same thing directly: on the free arm the label is fully
readable from the whole state at the first token of the model's first own
turn and nearly unreadable at the action position (its RT-230, the side
observation), so the free toy model does not carry the marker word forward to
where it acts.

### 5.5 Seeds

**Three seeds per arm** (ruled 2026-09-25, the queue ruling, page 1f), giving
**twelve** registered runs across four arms. The registration says in terms
that the toy arithmetic implying one seed, the rehearsal's half-width
calculation, which the 2026-09-21 findings cautioned against carrying across
because the toy arms are far more repeatable than registered-size runs will
be (`docs/2026-09-21-successor-measure-rehearsal.md`, section 11), was not
carried across. The training recipe is the rehearsal's unchanged recipe; the
grammar attempt of section 4.4 did not clear, so nothing changes it.

---

## 6. The measure

### 6.1 The pairing

Episodes are generated in matched pairs that share a content seed and rotate
which agent the model is, machinery the registered generator already has. In
a pair, the **recipient** episode is the one the model runs; the **donor**
episode is its twin in which the model is a different agent. Because all four
agents assigned the item, **the value the donor's identity dictates is already
present in the recipient's own context.** So a successful transplant does not
import an answer from outside; it changes which of four in-context values gets
selected. This is the construction that lets the experiment tell apart
"the transplant moved who is acting" from "the transplant carried the answer
with it", which is the confusion the outside review warned about.

### 6.2 The two transplants

A **site set** is fixed before anything is read: a list of token positions and
a list of layers. At those sites:

- **Whole-state transplant.** Replace the entire running-state vector at each
  site with the donor's.
- **Ownership-only transplant.** At the same sites, replace only the part of
  that vector lying in the nominated ownership subspace, leaving the rest of
  the vector as the recipient had it.

The second is a restriction of the first to a subspace, not a smaller or
different intervention. That is deliberate: it means the measure reads *how
much of the identity-driven difference at these places lives outside the
nominated subspace*, and not *how many places you had to touch*. The
rehearsal's transplanting code proves the restriction as a tensor identity in
its self-test (rehearsal item R-8).

**Two kinds of site set are not an intervention on what the network built.**
Copying the running state at every position of a layer makes everything
downstream of that layer the donor's own computation, wherever ownership lives
only in the running state; copying every layer at every position is the
donor's forward pass outright. And copying layer 0, the state the acting
channel is added to, at positions spanning the turns the channel fires on, is
a transplant of the acting channel's own input rather than of anything the
network computed from it (the Gate C review, RT-216). Section 7.2 removes both
kinds from the candidate family by rule.

### 6.3 The number

For each arm, on fresh episodes:

===== END OF RECORD 4, part 3 =====

