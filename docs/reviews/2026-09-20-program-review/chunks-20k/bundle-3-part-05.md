checkpoint, require that the largest drop the primary metric could possibly
show — the distance from its baseline to its shortcut ceiling, in the same
units as θ — exceed the band by a pre-committed factor (a factor of 5 is the
natural pick, since Gate 0 measured about a hundredfold headroom on the
binders and about twofold on the near-chance runs). If it does not, the
honest outcome is *not testable (underpowered)*, reported as such, with no
further seeds. This is the same move K0 makes for the old checkpoints,
applied where the verdict is actually read.

---

## RT-25 — "uncertifiable" is an outcome the procedure routes nowhere

**Severity: serious. ARGUED from §3.4, §4.2 and §4.3.**

The amendment re-specifies arm B of the ownership-cue gate — the likelihood
attack — so that it scores every turn with the acting channel withheld from
the prefix (§3.4). Its own red-team section is candid that this is new and
untested, and adds a rule:

> "*Mitigation:* the positive controls must fire on the same withheld
> forwards or the arm is declared **uncertifiable, not failed**; K4 caps the
> retry. The known weakness stands: arm B's positive control had demonstrated
> sensitivity on exactly one of four old checkpoints ... so 'uncertifiable' is
> a live outcome and is reported as such." (R5)

Now follow that outcome through the procedure:

- Kill criterion **K4** halts on "Gate (iii) act-withheld arm B **fails with
  positive controls firing**". Uncertifiable means the controls did *not*
  fire. **K4 does not fire.**
- §3.4 requires that "Gate (iii) must pass on the pilot checkpoint before any
  second seed is launched, as A1.4 required." Uncertifiable is not a pass.
  **The precondition is not satisfied.**
- §4.3's binding order runs "Gate 3 → lock → seeds 1 and 2" with no branch.
  **There is nowhere to go.**

So the amendment names a live third outcome, tells the program to report it,
and then leaves the procedure deadlocked on it: not killed, not permitted to
continue, with $18 already spent and no rule for what happens next. This is
the kind of gap that gets resolved in the moment by whoever is at the
keyboard, which is exactly what a pre-registration exists to prevent.

*Remedy, $0:* register the branch. My recommendation, offered and not ruled:
an uncertifiable arm B is **not** a kill and **not** a pass; it permits the
program to continue to the remaining seeds with a registered caveat attached
to every result — *the absence of a statistical ownership cue in the enacted
data is asserted from gates (i) and (ii) only, and the likelihood attack could
not be certified on this checkpoint* — and it forecloses the floor claim
regardless of which bin fires, because RT-17 in the pass-2 ledger (every
learnable ownership signal in a token-only interface is the attacker's
statistic) is what the arm exists to rule out. §2.2's Candidate C (other
agents' turns sampled from the model's own policy) is already recorded as
"the hardening to reach for if Candidate A's gate (iii) comes back with a
fingerprint that the act-withheld arm cannot clear" — but Candidate C is
priced out by the budget, so the caveat route is the honest one.

---

## RT-26 — the budget ladder is costed on the wrong grammar

**Severity: serious. MEASURED inputs, ARGUED cost model.**

### The problem

§4.1's unit cost is the measured one for the *registered* grammar: "a
register-less 30M run is about 10.2 hours at $0.99/hr, about $10 to $11"
(`compute-ledger.md`, wave 1 and 2 twin rows — actual pod times 10.29 and
10.16 hours, 0.34 to 0.35 seconds per step). That grammar has 8 turns, 2 own
turns, and 59 tokens per episode. The grammar Gate 1 built has 12 turns,
3 own turns, and 85 tokens per episode.

The compute ledger records the reason this matters: "the workload is
enactment/Python-bound, not GPU-bound" (2026-08-15 row) — the 5090 at
$0.99/hr ran *faster per step* than the H100 at $3.29. So the cost scales
with the per-step Python and forward-pass work, not with floating-point
throughput.

### The arithmetic

Measured inputs:

| quantity | registered grammar | A3 grammar | ratio |
|---|---|---|---|
| tokens per episode, with question | 59 | 85 | 1.44 |
| own turns (enactment forward passes per step) | 2 | 3 | 1.50 |
| forward passes per step, including the loss pass | 3 | 4 | 1.33 |
| turn segments per forward pass (`model.py` Python loop) | 8 | 12 | 1.50 |
| segment iterations per step | 24 | 48 | 2.00 |

The registered token budget is fixed at 20 tokens per parameter — 784.08
million tokens, which at batch 128 was 102,000 steps on the old grammar
(`compute-ledger.md`, 2026-08-09 row). On 85-token episodes the same budget
is **72,066 steps**, 29% fewer. But each step costs 1.9 to 2.0 times as much
(1.44 per forward × 1.33 more forwards on the GPU side; 2.0 on the Python
segment-loop side, which is the side the ledger says binds).

```
wall-clock ratio = 0.707 steps × (1.9 to 2.0) per step = 1.34 to 1.41
per run: 10.2 h → 13.7 to 14.4 h,  $10.1 → $13.6 to $14.3
```

### What that does to the ladder

Re-costing §4.1's table at 1.35 times, with Gates 0 and 1 at their actual $0
rather than their budgeted $5:

| line | amendment | re-costed |
|---|---|---|
| Gate 0 + Gate 1 | $5 | $0 (actual) |
| Gate 2, the learnability pilot | $11–13 | **$15–18** |
| Seeds 1 and 2 | $22–26 | **$30–35** |
| Lesion phase (local) | $0–10 | $0–10 |
| Margin (one crash-resume, volume drip, one overnight idle leak) | $20 | $20 |
| **three-seed total** | **$74** | **$83** |
| Optional seeds 3 and 4 | $22 | **$30** |
| **grand total** | **$96** | **$113** |

The three-seed path still fits the $100 hard stop, with the margin intact.
**The optional two extra seeds no longer fit**, and the way they fail is the
bad way: the trigger in §4.1 is "cumulative *actual* spend at the lesion
phase is ≤ $55", and a clean run with no crash and no idle leak reaches the
lesion phase at about $53 — so the trigger opens, the two seeds are
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
