# The grammar attempt (redesign (c)) — method, committed before any code or output

*Written 2026-09-25 (Pacific) by the Claude Code session "MVM W1c grammar
attempt", on branch `worktree-w1c-grammar-attempt`, branched from the main line
at `a96f873`. **UNREGISTERED.** This is a rehearsal-scale attempt on the laptop
at $0. It is not registered text, not a ruling and not a result about the
scientific question. Written under the workspace plain-language rule.*

*This file is committed on its own, before any code is written and before any
output exists. The commits that follow it are, in order: the rehearsal-repairs
driver carried in unchanged from pull request 52, the grammar change and its
driver, the outputs, and the findings
(`docs/2026-09-26-grammar-attempt.md`).*

---

## 1. Why this is being run, and what was ruled

John ruled on 2026-09-25 that redesign (c), a grammar change, is attempted at
toy scale on the laptop at $0, with its pass line stated before the run
(`docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` on branch
`rulings-2026-09-25-repairs`, commit `e03288c`, item 1). Redesign (c) is option
(c) on page 4 of the Weekend 1 queue proposal
(`docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`): "a grammar change that
makes the named-other action depend on the same mechanism as the own-directed
one". The ruling says that if the attempt clears, version 2 of the successor
proposal is amended before its registration review (Gate A) with the grammar
change, and rehearsal items R-1 to R-6 are re-run; if it does not, fallback (d)
— accepting the risk on the record — is what registers.

**The starting diagnosis, which the ruling says is a starting point and not a
ruling.** The rehearsal-repairs findings (`docs/2026-09-26-rehearsal-repairs.md`
on branch `worktree-w1c-rehearsal-repairs`, commit `e0626b2`, section 2) argue
that in the current grammar the acting channel — the input wire that tells the
model "this turn is yours" — fires on **both** action turns, so the only thing
telling the own-directed action from the named-other one is a single word, and
the two conditions compete for one route. Those findings mark that reading
ARGUED.

## 2. The grammar change

### 2.1 What the current grammar does (read from the code)

In `experiments/rehearsal-successor-measure/src/grammar.py`, function `render`,
each of the two action turns is rendered as seven tokens,
`<act> revise <who> <item> <ans> <mask> <nl>`, and the acting channel is set on
all seven of them in both conditions (`acting.extend([1] * 7)`). The `<who>`
word is the special word meaning *your own* in the own-directed condition and
the named agent's marker word in the named-other condition. On the assignment
turns the acting channel fires only on the model's own two turns.

### 2.2 The change: the acting channel is off on the named-other action turn

**On the named-other action turn, the acting channel is set to 0 on all seven
tokens instead of 1. Nothing else changes**: every token of every episode is
the same as before, the own-directed action turn still carries the acting
channel on all seven tokens, and the assignment turns are untouched.

It is implemented as one module-level setting in `grammar.py`,
`NAMED_OTHER_ACTING`, whose default is 1 (the current grammar, so every earlier
record still reproduces from the same code) and which the new driver sets to 0
before it generates anything.

### 2.3 Why this change, and not a smaller or a different one

**It is the smallest change that removes the shared signal, and removes all of
it.** The signal the diagnosis names is "the acting channel fires on both
action turns". Turning it off on the named-other turn's mask position alone
would be a one-token change, but the other six tokens of that turn would still
carry the channel, and the model reads earlier positions of its own turn
through attention; the shared signal would remain. Turning it off on all seven
tokens of that turn is the smallest change after which the named-other turn
carries no "this turn is yours" signal anywhere. ARGUED.

**It keeps the property the transplant depends on.** A matched pair of
episodes (a "recipient" and its "donor" twin) must be token-for-token identical
and differ only in which agent the acting channel marks. The acting bits on the
action turns do not depend on which agent is the model, so under this change
the twins are still token-for-token identical and still differ only on the
assignment turns. This is checked by the grammar self-test (section 4).

**The packet's example was considered and not used, for two reasons.** The
example was "placing the named agent's marker where the model's own marker sits
at the action position". (i) In this grammar the named agent's marker already
sits there: the `<who>` word is three tokens before the scored position, which
is where the Amendment A3 grammar (`curriculum_a3.py`) rendered the model's own
marker. The grammar's docstring records that the own-directed turn was made
marker-free on purpose (its "departure 1"). (ii) The other reading — putting the
**model's own** marker word at the own-directed action position, so both
conditions are read by matching a marker — puts the model's name in the text.
Section 4.2 of the successor proposal
(`docs/successor-experiment-proposal-2026-09-21.md`) rules that out in terms:
"removing it would mean putting the model's own name in the text, which would
reintroduce the very leak the acting channel was built to avoid" (ledger item
RT-17, the finding that any learnable ownership cue in the text is a
fingerprint). It would also make the twins differ in their tokens, which the
transplant cannot tolerate. ARGUED.

**A third option, not used:** a second input channel marking the named agent's
assignment turns. That hands the named-other answer to the model as an input
feature, which makes the condition trivial rather than learnable, and it is a
larger change than 2.2. ARGUED.

### 2.4 What the change costs, stated before the run

Section 4.1 of the proposal calls it "the whole point of the redesign" that
both conditions are "actions on the model's own turn". Under this change the
named-other action is still an action the model takes, supervised and scored
the same way, at the same kind of position — but it is no longer marked by the
acting channel as the model's own turn. If the attempt clears, version 2 of the
proposal has to say that in section 4.1, and that is a change in what the
experiment compares. This file records the cost; it does not weigh it. ARGUED.

### 2.5 The wager, stated before the run

**This session expects the change not to clear the pass line.** The reason is
in the repairs findings' own diagnostic table (section 2 of that file,
`out-repairs/diagnose_named_other.json` on PR 52): on the unchanged recipe the
free arm gives **its own** value at the named-other turn on only 0.05 to 0.07 of
episodes — below the one-in-four a model that could not tell the turns apart
would give — and splits the rest across the other three agents' values. That
pattern says the model already tells the two turns apart and fails at the
other step: matching the named marker word to that agent's assignment. If so,
removing the shared acting signal does not supply the missing step. What would
count against this wager: the free arm clearing the pass line below. ARGUED.

## 3. What is trained and measured

The recipe is the unchanged 2026-09-21 recipe, as carried in the repairs driver
(`repairs.py`, recipe `base`: 2,500 steps, batch 256, learning rate 0.003,
15,000 training pairs), on the new grammar. No training change of any kind.

- **Free arm (arm F), seeds 0, 1, 2** — the pass line is read on this arm.
- **Arm T** (the arm built so that its ownership answer is separable) **and
  arm C** (the arm built so that it is entangled), **seeds 0, 1, 2** — for the
  re-reading of R-1 to R-6.
- **The ownership-blind solver is not re-trained.** It trains with the acting
  channel zeroed everywhere, so the grammar change cannot reach its data. That
  is shown by a command (section 6, R-5), not assumed.

Every stage runs through the repairs driver's own functions (train, gate,
nominate, measure, summary), unchanged, with the output folder pointed at
`experiments/rehearsal-successor-measure/out-grammar-c/`. Nothing in `out/` or
`out-repairs/` is written.

## 4. The four matched properties that must still hold (proposal section 4.2)

Checked in the generated data of the new grammar by the grammar self-test, run
with `NAMED_OTHER_ACTING = 0`, on 3,000 matched pairs (6,000 episodes):

1. **Candidate count.** In both conditions the item has been assigned by all
   four agents, so four distinct earlier values are in context.
2. **Distance.** The gap in turns between the source assignment and the action
   has the same distribution in both conditions (largest difference between the
   two histograms under 0.02).
3. **Supervision.** One supervised position of each kind per episode, one
   scored token each, the scored token being the mask word.
4. **Transformation.** The same successor rule in both conditions.

Added for this change: the twins are still token-for-token identical and still
differ in the acting channel; the new grammar's tokens are identical to the old
grammar's for the same content; and the acting channel differs from the old
grammar's only on the seven positions of the named-other action turn. If any
check fails, nothing is trained and the findings say so.

## 5. The pass line, pre-stated

From the ruling (item 1) and the page 1b bar of
`docs/rulings/2026-09-26-weekend-1-queue.md`:

**The attempt clears if both of these hold on the free arm, on the 3,000
held-out development episodes the repairs gate used (1,500 pairs, pool `dev`,
seed 99):**

- **(a) Named-other.** The named-other condition has **790 or more correct of
  3,000** (above one in four at the 0.05 level under a one-sided binomial test;
  0.2630 is the ruling's figure for the boundary) on **at least two of the three
  seeds**.
- **(b) Own-directed not below its unchanged-recipe level.** The mean
  own-directed accuracy over the three seeds is **at or above 0.5513**. That is
  the lowest own-directed accuracy the free arm has on either committed record
  of the unchanged recipe on the old grammar: the six seeds in
  `experiments/rehearsal-successor-measure/out/gate.json` (2026-09-21: 0.5633,
  0.5563, 0.5890) and in `out-repairs/gate_base.json` on PR 52 (2026-09-25:
  0.5597, 0.5513, 0.5547). The mean is compared against the lowest seed because
  the free arm does not reproduce from code and seed on this laptop
  (`docs/rulings/2026-09-23-range-and-direction-only.md`), so a per-seed
  comparison would fail an unchanged model by drift alone; the line still
  catches a real loss of the kind the loss re-weighting caused (own-directed
  0.17 to 0.18). This comparison rule is this session's choice; the strongest
  alternative is to retrain the old grammar in the same session and compare
  seed by seed, which costs about 45 more minutes of laptop time and still
  meets the drift problem. ARGUED.

Anything else is **not cleared**. The findings say plainly which, and do not
recommend beyond that.

## 6. Rehearsal items R-1 to R-6, re-read against the new grammar

Each item is read against its wording in section 10 of the proposal, with the
ruled numbers where a ruling fixed one, and given one of four labels:

- **HOLDS** — it passed before and passes on the new grammar;
- **NOW PASSES** — it failed before and passes on the new grammar;
- **FAILS** — it does not pass on the new grammar (the findings say whether it
  was already failing);
- **UNCHANGED BY CONSTRUCTION** — the change cannot reach the item's inputs,
  shown by a command, so its earlier verdict carries.

"Before" means the latest committed reading: the repairs findings on PR 52
where they re-measured an item under the ruled instrument, otherwise the
2026-09-21 rehearsal findings (`docs/2026-09-21-successor-measure-rehearsal.md`,
section 2a).

- **R-1, the grammar works and both conditions are learnable.** Passes if the
  four matched properties of section 4 hold **and** each of arms T, C and F
  clears the 790-of-3,000 bar on both conditions on at least two seeds of three.
  The acting-channel lesion (page 1h) is reported beside it.
- **R-2, arm T's ownership answer is transplantable on its own.** Passes if, on
  every seed, the blind nomination (the repairs driver's one rule) returns a
  site set for arm T and the chance-corrected reading at it is within 0.1 of
  zero. The 0.1 is a rehearsal-only tolerance, not a ruled number.
- **R-3, arm C's degree is known by construction.** Passes if, on every seed,
  arm C's whole-state transplant clears the page 1c floor at its nominated site
  set and the chance-corrected reading there is 0.5 or higher (the page 1a
  separation bar, used here as the line for "high"). The repairs driver's
  sensitivity row with every "all positions" set removed — which the
  2026-09-25 ruling, item 3, has since made the ruled exclusion — is reported
  beside it and read the same way.
- **R-4, all four outcomes are reachable.** Passes if each of these lands where
  stated: near zero (arm T, as R-2); high (arm C, as R-3); no verdict (arm T at
  the failing site set the 2026-09-21 rehearsal used — the first layer, before
  the identity can be known, rank 2 — where the whole-state transplant should
  not clear the floor); negative (the ownership-only transplant beating the
  whole-state one, searched for on the unseen-vocabulary pool of 800 pairs,
  seed 780, at every arm's nominated site set and rank, seed 0, as
  `negative_case.py` did on 2026-09-21; if none of the three is negative, the
  search widens to every site set and rank cap at seed 0 on that pool, and the
  findings say it had to).
- **R-5, the competing solvers.** The name-only solver is computed from the
  episode's values alone and the ownership-blind solver trains with the acting
  channel zeroed. Both are UNCHANGED BY CONSTRUCTION if a command shows that,
  with the acting channel zeroed, the batches the two grammars produce are
  byte-identical; the name-only solver is recomputed anyway and printed.
- **R-6, the arithmetic is finite.** The measure's self-test (`measure.py
  --self-test`) and the chance-corrected reading's floor and no-verdict rules
  (`repairs.reading`) run on made-up cases chosen to break them; they are pure
  arithmetic. UNCHANGED BY CONSTRUCTION if a command shows they do not import or
  call the grammar's rendering, and they are re-run anyway.

Also reported, not items: the separation between arms C and T per seed (page
1a), and, on the free arm, what it answers at the named-other turn (the
repairs diagnostic `diagnose_named_other.py`, pre-stated here this time).

## 7. Order of commits, and what is not done

1. This file.
2. The repairs driver and its helpers, carried in byte-for-byte from commit
   `e0626b2` (pull request 52 is still open, and this branch is from the main
   line): `repairs.py`, `arm_middle.py`, `diagnose_named_other.py`, and
   `training.py`'s training options.
3. The grammar setting, its self-test additions, and the new driver
   `grammar_attempt.py` (code only, no output).
4. The outputs in `out-grammar-c/`.
5. The findings, `docs/2026-09-26-grammar-attempt.md`, in the same shape as the
   rehearsal-repairs findings, with the author's run of the known-failure list
   (`docs/known-failure-modes.md`) against this method. That run does not stand
   in for a reviewer's pass; under the pairing rule this work is owed a check by
   a different session.

No machine is rented, no vendor is contacted and nothing is spent. No
registered text, ruling file or protocol text is edited.
