# Red-team pass 3 — on Amendment A3, before the registration commit

*2026-09-15. Target: `amendment-a3.md`, ratified 2026-09-15 and awaiting
registration, read against the two completed gates and against the grammar
those gates actually built (`src/curriculum_a3.py`, `src/encoding_a3.py`,
`src/cue_detector_a3.py`, all at commit `7ab8018`). Thirteen findings,
numbered **RT-20** to **RT-32**, continuing the numbering in
`red_team_ledger.md`, which ends at RT-19. Two are fatal against the
amendment as written; both are fixable for $0 before the registration
commit, and both must be fixed before it, because both change registered
text.*

*Every finding below is marked **MEASURED** (I ran the code and report what
it returned) or **ARGUED** (I am reasoning from the documents and the
source, and a reader can disagree). Nothing in this pass ran a model,
created a pod or spent a dollar; the arithmetic is local. The commands I
used are reproducible against the modules named.*

*House rule this document is written under: the workspace plain-language
rule (`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30). Short labels like
RT-01 and K2 are kept because they are what make a claim checkable, and
every one of them carries a phrase saying what it is.*

---

## What was already known, and is not restated here

Five problems were found by the two gates before this pass and are on the
record: the verdict cell size at 400 episodes (`gate0-null-calibration-findings.md`,
reading 2); kill criterion K2, the halt for an unlearnable objective, adding
a raw accuracy to a chance-corrected band (same file, reading 3); kill
criterion K0, the halt for a null band too wide to read a verdict through,
not saying which checkpoints its band is read on (same file, reading 1); the
measured shortcut ceilings of 0.2925 and 0.5 rather than the 0.25 the
amendment pre-states (`gate1-curriculum-findings.md`, finding 3); and the
input-tensor cue gate's single-sample interval understating how far its
result wanders between samples (same file, finding 4). This pass takes all
five as found, endorses all five remedies, and spends its effort elsewhere.
Two of them recur below only because a new finding changes what the right
remedy is: RT-21 supersedes the ceiling remedy offered in Gate 1, and RT-24
extends the K2 units fix to the rest of the amendment's thresholds.

---

## Summary

| ID | Finding | Severity | Cost to fix |
|---|---|---|---|
| RT-20 | The primary metric does not require a self-index: the acting agent's own name label sits in the prompt of the supervised position, and a solver with no ownership at all scores 1.000 | **fatal** (against the design as written) | $0, one grammar regeneration |
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

> **ANNOTATION, 2026-09-21. The figure quoted above was right when this pass
> was filed. The battery record was rebuilt nine and a half minutes later and
> now reads 0.0909.
> Nothing in the finding is edited, and its substance is untouched.**
>
> The record of frozen batteries this finding cites
> (`experiments/06-mvm-0a-constructed-self-index/batteries-a3/batteries_meta.json`)
> today gives the cross-turn state control a chance floor of 0.0909, not the
> 0.0769 quoted above. The pass did not misread it. As first committed — by the
> commit titled "Gate 1 complete: the grammar passes both cue gates at $0; K1
> does not fire" (`7995382`, 2026-09-15, 09:58 Pacific) — the file recorded
> 0.07692307692307693 for that battery, which is one thirteenth, exactly as the
> finding says it is. The battery was rebuilt the same afternoon by the commit
> titled "Shortcut sweep finds a second fatal leak; three drafts map the real
> trade-off; revision proposal drafted" (`e76d0d4`, 2026-09-15, 16:00 Pacific),
> which cut the turns per episode from twelve to ten and moved the floor to
> 0.09090909090909091. The file was regenerated under the reviewer.
>
> The finding still stands against the record as it is today. What it objects to
> is that a single floor is recorded for a battery that mixes two question
> forms, and is taken from the first frozen item only. The record as it stands
> still carries one floor per battery, so that objection survives the rebuild
> untouched — only the digit moved. A reader who opens the cited file, fails to
> find 0.0769 and stops there would drop a live finding over a stale digit.
>
> Added 2026-09-21 by a later session, not by the reviewer. It follows this
> repository's practice of annotating a filed record rather than editing it, so
> the reviewer's own wording survives — the form used by the two stacked ruling
> annotations at the top of the control-clause proposal of 2026-09-19
> (`docs/control-clause-proposal-2026-09-19.md`), the second of which says of
> the first, "Nothing in this memo is rewritten" and "It is left unedited". The
> nearest ruling on a wrong figure in a filed review, item 20 of the ruling of
> 2026-09-21 on review verification and staged spending
> (`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`),
> likewise leaves the review's sentence standing and carries the correction as a
> separate task.

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
