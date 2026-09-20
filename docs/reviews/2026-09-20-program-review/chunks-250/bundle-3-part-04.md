- and localizing "far from acting positions" finds nothing, because nothing
  is carried there.

That is every clause of H_self-location satisfied by a mechanism that is
exactly the wire being re-read, which is the thing R1 says would make a
positive worthless. None of the four mitigations touches it. Distance does
not help, because the retrieval happens where the localization has to happen.

I do not think this is fatal, and I am not confident it can be made to go
away at 30 million parameters — the distinction between "carried forward" and
"re-fetched from a marked position" may not have a clean operational test in
a twelve-turn episode. But the amendment should say so rather than list four
mitigations that read as though they close it.

*Remedy, $0:* (i) delete the false parenthetical and state where L1 is
actually localized — at the graded read position, with the honest note that
this is where R1 bites hardest; (ii) register a discriminator for the
re-fetch mechanism, and the best available one is cheap: **ablate the L1
subspace only at the graded read position while leaving the acting
injections intact, and separately ablate the acting injections at the two
earlier own assignment positions while leaving the read position intact.**
If the second collapses the metric and the first does not, the structure is
a re-read pointer, not a carried index; (iii) add "re-fetched pointer" to
§3.5 as a named reading under R1, so it has somewhere to land.

---

## RT-24 — the thresholds are written as single numbers, and no readability floor is registered

**Severity: serious. MEASURED from Gate 0's tables, ARGUED consequence.
Fixing it costs $0 and saves $30–35 when it fires.**

### (a) θ and δ are per-battery quantities written as scalars

§3.5 writes every clause against a single θ and a single δ — "d(T_act) ≥ θ
... d(T_state) < θ". Gate 0 computed them per battery and they are not close
to each other. On the pilot seed-0 full checkpoint alone:

| battery | 95th-percentile null band θ |
|---|---|
| T_syntax | 0.0000 |
| T_state | 0.0022 |
| T_sr | 0.0058 |
| T_si | 0.0060 |
| T_sr_rev | 0.1464 |

A 25-fold range within one checkpoint. Which θ the clause "d(T_state) < θ"
uses changes whether the control clause is nearly automatic (against 0.1464)
or genuinely demanding (against 0.0022). The same ambiguity runs through
every clause.

*Remedy, $0:* write θ with a battery subscript throughout — θ(T_act),
θ(T_other), θ(T_state) — and δ with a battery pair — δ(T_act, T_other),
δ(T_act, T_state). Gate 0's script already produces exactly these; the
amendment simply does not name them.

### (b) Nothing stops the program paying for two seeds it cannot read

Gate 0's reading 3 measured what the chance-corrected metric does as a
battery approaches chance: on the checkpoint whose control battery sat at
0.340, the null band was 0.163; at 0.355, it was 0.379. Against 0.006 on a
checkpoint at ceiling. The band is not an artifact — it is what dividing by a
small number does, compounded by a near-chance model genuinely being noisier.

Gate 0 applied that reading to kill criterion K2 and stopped there. It
applies equally to the whole lesion phase. K2 retires the pilot only if the
primary metric is at or below its shortcut ceiling plus the band. A pilot
landing at, say, 0.40 — above the 0.2925 ceiling, far below ceiling
performance — passes K2, and then §4.3 proceeds straight to the lock and to
seeds 1 and 2. At a baseline of 0.40 the divisor is 0.275 and the null band
will be somewhere in Gate 0's near-chance regime. **The program would pay for
two more training runs and a lesion phase to read a verdict through a band
wide enough to swallow it.** At the re-costed prices in RT-26 that is $30–35
of avoidable spend, on top of the pilot.

*Remedy, $0:* register a **readability gate** between the lock and the
authorization of seeds 1 and 2. After θ is null-calibrated on the pilot
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
