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
