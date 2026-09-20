fraction improves") winnable with GWT landing in MVM-0b — it does not need
it in MVM-0a. Record the deferral in v0.4 so the fork adjudication's
paper trail stays unbroken.

## Decision 6 — blind-localization arm [RT-12]: alongside or follow-on

**Recommendation: alongside — registered now, in this pre-registration, as
an unconditional arm.** The decisive argument is selection-proofing: if the
arm is a follow-on, the decision to run it is made *after* the headline is
known, and "we ran the instrument-audit because the headline disappointed"
is a story a skeptical reader gets to tell. Registering it unconditionally
now — it runs on the same trained seeds regardless of bin — removes that
degree of freedom for ~$5 of analysis compute (probes, patching, and SAEs
are minutes-scale at d ≤ 448). Sequencing firewall inside the arm: the
headline verdict is computed and committed **before** the localization
pipeline runs, and the pipeline (Experiment 1's, mechanically re-run)
receives a config with the register location withheld. State the honest
limit in the registration: with one researcher, blindness is **procedural,
not epistemic** — the analyst knows the architecture; what is blind is the
pipeline's inputs, and every threshold it uses is inherited from Experiment
1, not tuned here. The red team's judgement stands in the draft and this
memo endorses it: if the instruments cannot recover a center known-by-
construction to be there and load-bearing, **Experiment 1's null was
instrument failure** — a result worth more than the headline either way it
goes.

---

## Adjudication checklist (for the v0.4 commit)

| # | decision | proposed value |
|---|---|---|
| 1 | scale + budget | ladder 10M→30M→100M, pre-committed smallest-that-learns rule; 20 tok/param; cap $200; unlearnable-at-scale loss condition verbatim |
| 2a | registers | N (one per agent), marker-keyed, symmetric machinery |
| 2b | register width | 32 |
| 2c | injection | cross-attention, every layer |
| 2d | attention span | full-episode causal |
| 3 | N agents / turns | keep 4 / 8 (gate-certified values) |
| 4 | corrigibility doc | John, 2026-08-21, blocks first training run |
| 5 | GWT metric | defer to MVM-0b, recorded in v0.4 |
| 6 | blind-localization | alongside, unconditional, verdict-first firewall |

After adjudication: write values into pre-registration.md v0.4, John's
review, then the registration commit makes it binding (house procedure,
step 2). The cue-detector gate run (ii) on input tensors becomes buildable
the moment 2a–2d are fixed, since the tensor layout (register keying,
marker embeddings, loss masks) is what it inspects.


===== FILE: experiments/06-mvm-0a-constructed-self-index/red-team-pass-3.md =====

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
