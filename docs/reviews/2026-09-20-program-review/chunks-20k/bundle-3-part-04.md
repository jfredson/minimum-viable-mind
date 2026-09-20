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
