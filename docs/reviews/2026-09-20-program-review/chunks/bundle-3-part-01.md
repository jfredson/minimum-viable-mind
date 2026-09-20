| RT-21 | The two batteries have different shortcut ceilings, which biases the headline bin's differential by up to 0.24 against a band of about 0.01 — a purely generic binder reads as self-location, and the generic-binding bin cannot fire | **fatal** (false positive on the headline) | $0 for the metric fix; $12–15 for the grammar fix |
| RT-22 | The outcome bins are neither exhaustive nor mutually exclusive on this grammar: a flat null satisfies two bins at once, the positive bin and the ownership-tag bin overlap, and there is no bin at all for the validity check failing | serious | $0 |
| RT-23 | The lesion target is not well-posed where it matters: the own revision turn *is* an acting position, so the amendment's own localization rule contradicts itself on the built grammar, and objection R1 has a sharper form the mitigations do not touch | serious | $0 to re-specify; the sharp form may not be answerable at this scale |
| RT-24 | The thresholds are written as single numbers but Gate 0 measured them per battery across a 25-fold range, and no readability floor on the primary metric is registered before the two paid seeds are authorized | serious | $0; saves $30–35 when it fires |
| RT-25 | "Uncertifiable" is a third outcome for the ownership-cue gate that the procedure routes nowhere: it is not a kill, not a pass, and there is no branch for it | serious | $0 |
| RT-26 | The budget ladder is costed on the old 8-turn grammar; the built 12-turn grammar costs about 1.3 to 1.4 times as much per run at the same token budget | serious | $0 to re-cost; the optional extra seeds no longer fit |
| RT-27 | The training loss mixture is unregistered, and it alone decides whether the shortcut-starvation bin fires by construction | serious | $0 |
| RT-28 | The cross-turn state control's recorded chance floor is taken from one item and is wrong for half the battery; its real floor is about 0.44, not 0.077 | worth noting | $0 |
| RT-29 | The amendment's description of the control battery does not match the battery that was built, and the module's claim that its answer appears in no turn is false 80% of the time | worth noting | $0 |
| RT-30 | Two assertions in the grammar's self-test are disabled by a trailing `or True`, one of them the exchangeability check the whole cue-gate argument rests on | worth noting | $0 |
| RT-31 | Two checkable factual errors about the existing record: three of the five checkpoints carry a register, not five; and same-item multi-agent assignment happens in the old grammar zero times, not "by accident" | worth noting | $0 |
| RT-32 | Three procedural gaps: the corrigibility document's own re-reading rule makes A3 a review point and none is scheduled; the null-calibration script the amendment says will set the thresholds cannot run on this grammar; and the lock guard John ratified is unbuilt | procedural | $0 |

**The single most serious finding is RT-20.** On the grammar Gate 1 built and
certified, the primary metric can be scored at 1.000 by a solver that has no
representation of ownership whatsoever, because the model's own name label is
sitting in the context three tokens before the token it is graded on. The
pre-stated shortcut ceiling — 0.25 in the amendment, 0.2925 as Gate 1
measured it — is not a bound on ownership-blind solvers at all. It is the
score of a solver that has been forbidden, by the person computing it, from
reading a name that is in plain sight.

---

## RT-20 — the supervised position hands the model its own name label

**Severity: fatal against the design as written. MEASURED.**

### The problem

Amendment A3 §2.2 states the design's central claim:

> "A solver that does item lookup without ownership sees four candidate
> earlier values and can do no better than 1/4; this is the pre-stated
> **lookup ceiling of 0.25**. ... The only route from 0.25 to 1.0 is to have
> bound the act event to the item at the time of acting and carried that
> binding forward to the revision turn."

Every turn in the grammar, the model's own turns included, is rendered
through one fixed template (`curriculum.py`, `TEMPLATE`):

```
{marker} assign {item} to {value}
```

The name label comes first and the graded value comes last. The supervised
position for the primary metric is the value token of the model's own
revision turn (`encoding_a3.py`, `encode_episode`: `act_pos = span[-2]`).
So at the moment the model is graded, its own name label is three tokens
back in its own context window, attached to the very turn it is producing.

The task at that position is therefore: *given `<name> assign <item> to`,
emit the successor of the value that `<name>` assigned to `<item>` earlier
in this episode.* That is ordinary name-keyed retrieval composed with a
successor map. It is the same function for every agent in the episode. It
needs no self-index, no acting channel, and nothing carried forward from
the act.

### The evidence

Printing the tokens around the supervised position of an enacted episode
(`encoding_a3.encode_episode`, episode seed 7, enactment seed 3):

```
context around the graded token: ['bay_B', '<nl>', '<verdant>', 'assign',
                                  'parcel_18', 'to', 'bay_H', '<nl>']
graded token: bay_H     the metric's target: bay_H
own slot: 2             own name label: <verdant>
```

I then scored a solver that is given the rule and the episode text and does
exactly one thing — find the earlier assignment turn whose name label and
item match *this turn's* name label and item, and emit that value's
successor. It has no acting-channel input, no ownership variable, and no
access to `own_slot`. Over 3,000 enacted episodes:

```
ownership-free name-keyed solver on the primary metric: 1.0000
pre-stated shortcut ceiling (amendment):                0.25
measured shortcut ceiling (Gate 1):                     0.2925
```

The measured ceiling of 0.2925 is computed in `curriculum_a3.measured_ceilings`
by counting the candidate successors of the item's four earlier values and
taking one over that count. That calculation assumes the solver cannot tell
which of the four assignments was its own. The name label at the graded
position tells it.

### Why the certified cue gates did not catch this

They were not asked to. Gates (i) and (ii) — the text detector and the
input-tensor detector — ask whether a classifier can predict *which turns
are the model's own* from surface form. Both passed, at 0.5097 and 0.5259
against a chance value of 0.5 (`a3-gates/cue_detector_gate_a3.json`), and
those results stand. But passing them is a necessary condition, not a
sufficient one. There is no cue predicting ownership *across* turns, and
there does not need to be: the solver never has to know which agent it is.
It only has to copy the label off the turn in front of it. The amendment
reads the cue gates as though they certify the shortcut ceiling. They
certify something narrower.

### What follows if this is registered unfixed

- The pre-stated shortcut ceiling is not a bound, so kill criterion K2 (the
  halt for an unlearnable objective) tests nothing.
- The acting channel is redundant at the graded position, so the L0 lesion —
  zeroing the acting projection, which §3.1 registers as "a *validity check*
  ... it should collapse T_act to the lookup ceiling" — is predicted *not*
  to collapse it. That is a detectable failure, but it is detected only
  after the pilot run is paid for, and RT-22 shows there is no bin to put
  it in.
- The primary and control batteries then demand the *same* computation
  (name-keyed retrieval plus a successor map), differing only in whether it
  is read at an in-episode position or at an appended question. So the
  ground truth of the experiment is generic who-did-what binding — which
  RT-21 shows the metric will nonetheless report as self-location.

### Remedy

The graded token must not be preceded, in its own turn, by the name of the
agent producing it. Two ways, both $0 in compute:

**(a) Preferred — reorder the rendering template so the name label comes
last**, for every turn: `assign {item} to {value} by {marker}`. Turn length
goes from six tokens to seven; the segment boundaries in `model.py` are
derived from `turn_ids` rather than a fixed width, so nothing downstream
breaks. The A3 vocabulary gains one more word ("by"), which costs nothing
because no existing checkpoint depends on the A3 vocabulary. Every earlier
turn keeps its label, so the control battery and the co-reviser inference
are untouched. At the graded position the model now has: this is a revision
of item X, and two earlier positions in this episode carried acting-channel
injections. To emit the right value it must find which of the four
assignments on X was at one of those injected positions. That is the
computation the design was written to force.

**(b) Alternative — render revision turns without a name label at all**, with
a distinct verb so they remain parseable. This works for the graded position
for the same reason. It has a wrinkle worth stating, because it is the
obvious objection: an already-emitted anonymous revision is trivially
de-anonymized, since its value implies its predecessor, which is visible with
its owner's label. That does not undo the fix — at its *own* revision the
model has emitted nothing to invert — but it does mean the anonymity is
cosmetic everywhere else, so (a) is cleaner.

Under either fix the measured shortcut ceiling stays near 0.2925, because a
co-reviser who went first still strikes one candidate; the difference is that
it becomes a real ceiling rather than a stipulated one.

**Cost.** $0 in compute. One grammar regeneration, a re-freeze of the four
batteries, and a re-run of gates (i) and (ii), which took about 1.5 hours of
local wall clock and $0 the first time. Kill criterion K1 permits two
regenerations and none has been used. **This must happen before the
registration commit**, because §2.2's ceiling is registered text.

**One thing the fix does not do.** It does not make objection R1 (the
acquired index is just the wire, passed forward) go away — see RT-23. It
makes R1 the live question instead of a foregone conclusion, which is what
the amendment wants.

---

## RT-21 — unequal shortcut ceilings bias the headline bin toward a false positive

**Severity: fatal (produces the program's headline claim from a generic
binder). MEASURED inputs, ARGUED consequence.**

### The problem

The registered metric is the chance-corrected drop: how far a battery fell
under a lesion, divided by how far it stood above guessing.

```
d(B) = (baseline − ablated) / (baseline − chance)
```

Chance is 0.125 for both verdict batteries. But the two batteries do not
fall to chance when ownership is removed — they fall to their *shortcut
ceilings*, which Gate 1 measured and which are not equal:

| battery | what it is | chance | shortcut ceiling |
|---|---|---|---|
| T_act (primary) | the value the rule dictates at the model's own revision | 0.125 | **0.2925** |
| T_other (control) | the same rule's verdict for a named other agent | 0.125 | **0.5** |

(`batteries-a3/batteries_meta.json`, `lookup_ceiling_measured`; the asymmetry
arises because two agents revise each contested item, so on the queried item
both revisions strike a candidate, while on the model's own item only a
co-reviser who went first does.)

So the largest drop each battery can show, on a lesion that removes the
binding completely from a model at ceiling, is:

```
max d(T_act)   = (1.000 − 0.2925) / (1.000 − 0.125) = 0.809
max d(T_other) = (1.000 − 0.5000) / (1.000 − 0.125) = 0.571
difference                                            0.237
```

The headline bin, H_self-location, requires `d(T_act) − d(T_other) ≥ δ`,
where δ is the differential band. Gate 0 measured that band on the two
checkpoints that bound: **0.0061 and 0.0096**
(`gate0-null-calibration-findings.md`, δ table, the self-battery-against-
state-control column). Call it 0.01.

**A lesion of a purely generic who-did-what binder — a structure that binds
items to agents for everyone, with no self-index anywhere — produces a
differential of 0.237 against a band of 0.01.** The positive bin fires. The
bin that is actually true, H_generic-binding, requires
`d(T_other) ≥ d(T_act) − δ`, which on the same numbers reads 0.571 ≥ 0.799.
It cannot fire.

This is not confined to a total lesion. If a lesion removes a fraction *f*
of the binding capacity, both drops scale with *f* and the differential is
about 0.237 × *f*. It exceeds the band of 0.01 whenever *f* ≥ 0.042. So the
generic-binding bin can only fire when the lesion removes less than about
four percent of the capacity, which is to say when almost nothing happened.

The bias gets worse, not better, if the model does not reach ceiling. At a
baseline of 0.9 on both batteries the same arithmetic gives 0.784 against
0.516, a differential of 0.268.

### Why this is worse than the ceiling item Gate 1 already raised

Gate 1's finding 3 raised the ceilings as a pre-registration accuracy
problem and offered John a choice: adopt the measured numbers, or buy 0.25
back by adding a third contested item. Adopting the measured numbers *does
not fix this*. The numbers being right in the text does not change what the
metric does with them, because the metric never uses the ceiling — it divides
by distance above chance. This is the same defect Gate 0 identified in kill
criterion K2 (a raw accuracy added to a chance-corrected band), one level up:
the amendment compares two chance-corrected drops whose attainable ranges
differ by 42%.

### Remedy

**Primary, $0: correct against the measured shortcut ceiling, not against
chance, for any battery that has one.**

```
d'(B) = (baseline − ablated) / (baseline − ceiling_B)
```

Both batteries then top out at 1.0 and the differential is unbiased. The
thresholds θ and δ must be re-derived in those units, which is the same
script on the same draws and costs nothing. The chance-corrected form stays
as the reported quantity for continuity with the five existing checkpoints,
where it is the registered metric and where no shortcut ceiling was ever
measured. Note the pleasing consequence: under the *unfixed* grammar of
RT-20 the ownership-blind ceiling is 1.000, so `d'` has a zero denominator —
which is the arithmetic saying, correctly, that the metric has nothing to
measure.

**Alternative, priced: equalize the ceilings in the grammar** by adding a
third contested item that nobody revises, restoring a four-candidate set for
both batteries. Gate 1 priced this at "roughly a third more compute per run".
Against the re-costed run price in RT-26 ($13–15), that is about $4–5 per
run, or **$12–15 across the pilot and two seeds**, and it pushes episode
length from 85 tokens to about 109, which compounds RT-26's overrun. The
metric fix is free, exact, and does not touch the certified grammar. I
recommend it, and record the grammar fix as the option if John prefers the
correction to live in the data rather than in the arithmetic.

---

## RT-22 — the bins are neither exhaustive nor mutually exclusive

**Severity: serious. ARGUED from the text of §3.5.**

Three separate defects, all in the bin list. The amendment was written
before the grammar existed and its bins were never re-read against it.

**(a) There is no bin for the validity check failing.** §3.1 makes L0 — the
lesion that zeroes the acting projection — "a *validity check* and an upper
bound": it "should collapse T_act to the lookup ceiling", showing the task is
ownership-dependent as designed. Every bin in §3.5 that reads a lesion
verdict presupposes that it did. H_diffuse says so explicitly ("L0 collapses
T_act ... but no L1 subspace"). **Nothing in §3.5 catches "L0 clean, the
primary metric at ceiling" — the task turned out not to be
ownership-dependent.** RT-20 predicts exactly that outcome on the current
grammar, so this is not a hypothetical.

The registered design had this guard and A3 dropped it. RT-09 in the pass-1
ledger created a bin called **construction failure (register unused)** for
precisely this shape — an instrument that was never live — with the rule
that "nothing goes upstream", because a construction failure reported as
evidence about selves is a training bug propagating into the philosophy
repos. A3 removed the register and removed the guard with it, without
replacing it.

*Remedy, $0:* register a bin **construction failure (task not
ownership-dependent)**: L0 leaves the primary metric within the null band
while the metric is above its shortcut ceiling. Nothing goes upstream; the
grammar is rebuilt; the finding is a methods note. Place it, as the
registration places its gates, as a *precondition* — no other bin may be
read until L0 has collapsed the primary metric.

**(b) A flat null satisfies two bins at once.** H_generic-binding is stated
as a bare inequality: `d(T_other) ≥ d(T_act) − δ`. It carries no requirement
that anything moved. If an L1 lesion moves nothing — both drops about zero —
the inequality is true, so H_generic-binding fires; and H_self-reference-only
("its ablation leaves T_act within the null band") fires too, whenever the
probe decodes identity. Two bins, opposite readings, same data. Nothing in
§3.5 or in the registration's bin list gives a precedence rule.

*Remedy, $0:* add the missing clause — H_generic-binding requires
`d(T_act) ≥ θ(T_act)` as well as the inequality — and state a precedence
order for the case where clauses still overlap.

**(c) The positive bin and the ownership-tag bin overlap by construction.**
H_self-location requires, among other clauses, that "the swap probe moves the
action with the patched identity". H_tag requires that the re-indexing probe
"shows the action following the tag". Those are close to the same experiment:
one patches the subspace carrying identity into a matched episode and reads
the action; the other switches which slot the acting channel is injected for
and reads the action. A subspace that satisfies the first will, in most
mechanisms one can write down, satisfy the second. And nothing in
H_self-location excludes a high address-probe reading. So a genuinely
positive result lands in both bins, and §3.5 does not say which is reported.

This matters more than a tidiness complaint, because the two bins say
opposite things upstream: H_self-location says a center acquired under task
pressure passed the removal test; H_tag says ch05's program-counter reply
applies and this is not the floor. The amendment is candid that the removal
test cannot separate them (R4). What it does not do is say what gets written
when both fire.

*Remedy, $0:* state the precedence explicitly — the amendment's own R4
reasoning implies the tag bin wins, since an address that survives
re-indexing is not a center however much the swap probe moves. Write that
down as a registered rule rather than leaving it to the write-up.

---

## RT-23 — the lesion target is not localizable where it matters, and objection R1 has a sharper form

**Severity: serious. MEASURED geometry, ARGUED consequence.**

### The self-contradiction

§3.1 defines the registered lesion target:

> "**L1, the acquired index (the lesion target).** A low-rank subspace of the
> residual stream ... that carries 'which marker is mine' at positions *away
> from* act positions (revision turns and query positions)."

On the grammar Gate 1 built, **the model's own revision turn contains an
acting position.** The acting channel injects a copy of the model's own
preceding state at the value token of *every* own turn, the revision
included (`train.py`, `compute_act_inject`: `ps.append(int(span[-1]) - 1)`,
looping over `own_idx`, which is every turn where `t.agent == e.own_slot`).
That is the same token index the encoder calls `act_pos`. So "revision
turns" are not away from act positions; the own revision turn is one. The
parenthetical contradicts the rule it is attached to.

### The geometry, measured

Over 2,000 enacted episodes:

| quantity | measured |
|---|---|
| episode length | 73 tokens (12 turns × 6, plus the start token) |
| own turns per episode | 3 (two assignments, one revision) |
| acting positions per episode | 3 |
| tokens more than one turn from every acting position | 38 of 73 (52%) |
| distance from the graded read position to the nearest earlier acting position | median 24 tokens, minimum 6, maximum 60 |
| episodes where the previous own turn is the immediately preceding turn | 6.6% |
| own revision turn index | uniform over turns 8, 9, 10, 11 |

So there is no shortage of positions away from acting positions — 52% of the
episode qualifies. The problem is that they are the wrong positions. They are
other agents' turns, where "which marker is mine" has no demonstrated role,
so a subspace localized there is not shown to be the one the model uses when
it acts, and ablating it has no predicted effect on the primary metric. The
one position where the index demonstrably matters is the graded read
position, and that sits a median of 24 tokens — and as little as 6 — from an
acting position.

### The sharper form of R1

The amendment states objection R1 as: whatever probes find at revision
positions may be the acting-channel input propagated through attention, an
echo of the sense organ rather than a structure the network built. Its
mitigations are to localize far from acting positions, to require the
other-agent control to stay clean, to require the swap probe to move the
action, and to report the L0-to-L1 gap honestly.

The sharper form the amendment does not state is this. **The acting channel
is not a signal that has to be carried; it is a pointer into the context that
can be re-read.** The three injections sit at fixed, attendable positions in
the model's own context. A model that, at the graded position, attends back to
"positions carrying an acting injection whose item matches this one" and reads
that turn's value needs no carried index at all. It needs one attention
pattern and the injections themselves. Under that solution:

- a probe at the revision position decodes own identity at high accuracy,
  because attention has just fetched it;
- patching the subspace moves the action, because the fetched value is what
  the action is computed from;
- the other-agent control stays clean, because other agents have no
  injections to fetch;
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
