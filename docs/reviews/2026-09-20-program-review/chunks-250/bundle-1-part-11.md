a default. The reading confirmed: §2.1's "not a query asking it to
describe who did what" is satisfied because **no query anywhere asks about
the model's own commitments** — the self-report battery is gone — while
the ownership-free and other-agent queries stay supervised. Read at its
strictest the clause would remove query supervision entirely, and then the
control batteries would never be trained and the differential the
generic-binding bin turns on would be meaningless.

## 10. Money (decision 11)

**Registered, from measurement rather than estimate:** the token budget is
fixed at twenty tokens per parameter, so the longer episodes mean **fewer
steps** (0.71×), which offsets most of the higher per-step cost (1.26×
enactment passes, 1.41× sequence length). A run is **9.1 to 12.8 hours,
$9 to $13**; three seeds **$27 to $39**. The optional extra seeds remain
available inside the $100 hard stop but need a separate go. The $400
ceiling, the $100 stop and the corrigibility commitments are unchanged and
were not reopened.

**Note for the launch:** the RunPod account carries a spend limit of $80,
below the $100 stop. It should not bind at these costs, but it exists.

## What is registered, and what runs next

Registered: the grammar at `src/curriculum_a3.py`, its tokenizer at
`src/encoding_a3.py`, the trainer at `src/train_a3.py`, the batteries
frozen at `batteries-a3/`, the gates at `src/cue_detector_a3.py` and
`src/shortcut_sweep.py`, the calibration at
`src/null_calibration_a3.py`, the lock guard at `src/lock_guard.py`, and
the launcher at `src/launch_a3.sh`.

Next is Gate 2, the pilot: one register-less 30M run at seed 0, on John's
authorization in his own words, quoted verbatim in the ledger row. Nothing
has been spent on A3 to this point.


===== FILE: experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot.md =====

# Control-learnability pilot — pre-statement

**UNREGISTERED. Written and committed BEFORE the code change and before
any run, at John's instruction of 2026-09-19.** One 30M register-less
seed, run exactly the way the A3 pilot was run on 2026-09-15. Nothing
here is registered text, no registered verdict is read from this run, and
**nothing launches without John's go in his own words, quoted in the
ledger row.**

*TimeAssembler task: the control-learnability pilot (`90763b8f`).*

---

## The question

**Does the control battery learn when it carries its own loss term,
instead of a third of a shared one?**

The control battery has not learned on any checkpoint. Its intact scores
are 0.2877, 0.3057 and 0.3195 across the pilot and seeds 1 and 2 — all
below 0.3227, the score reached by a reference solver that cannot read
the name the control question supplies. Three seeds, one outcome, so it
is not a seed lottery.

Two explanations have been live since the 2026-09-17 audit and have never
been separated. Either **the control is under-supervised** — it receives
roughly one training row in three, sharing a single pooled term with two
much easier questions, while the primary battery has a dedicated
full-weight term of its own — or **supervision is not the binding
constraint**, and something else in the design defeats it: the reversed
rendering it must attend backwards through, the absence of the private
route the acting channel gives the primary battery, or the fact that its
answer appears in no turn and must be retrieved and then transformed.

This pilot separates them, once, for about ten dollars.

**What it does not do.** It does not repair Amendment A3's registered
comparison, which was refused on 2026-09-19 and stays refused. A control
that learns would make a comparison *designable*; it would not make the
A4 clause registerable, whose fatal findings were about what the clause
measures and where it is read, not about the control's score. **A3 stays
open, not closed**, and this pilot informs that decision rather than
making it.

---

## The change to the training objective

**One paragraph, and no grammar change.** The grammar, the tokenizer, the
frozen batteries, the episode structure, the rendering, the ceilings and
the attack sweep are all untouched; the only thing that moves is how the
loss is apportioned across the queries each episode already carries.
Today every training row carries exactly one query, chosen round-robin
from the three an episode holds, and the cross-entropy on that one answer
token is averaged into a single pooled term shared by the control
battery, the state battery and the syntax battery — so the control gets
about a third of the rows and a third of one term. Under the flag, the
batch is split: **half the rows carry the control query and its
cross-entropy becomes a term of its own with its own weight**, while the
remaining rows carry the state and syntax queries round-robin in a
separate term, and the primary battery's dedicated action term at the
model's own revision position is unchanged. At the flag's default weight
of 2.0 the control's share of the query gradient rises from about a third
to about two thirds, and **its per-row weight quadruples** — from
one-one-hundred-and-twenty-eighth of the pooled term to two
sixty-fourths of its own. With the flag off, the trainer computes exactly
what it computes today.

**Two design calls in that paragraph, both mine, both flagged, and
neither registered so John can move either before the go.**

- **Why the batch is split rather than a second forward pass added.** A
  truly per-episode control term — the control query on *every* episode,
  not half of them — needs a second forward pass and would roughly
  double the step time, taking the run from about ten hours and ten
  dollars to about twenty and twenty. Splitting the batch buys a
  dedicated, separately weighted term **at no extra compute**, which is
  what keeps the estimate on the pilot's measured 0.645 seconds per step.
  *Confidence: high that this is the right trade for a ten-dollar
  question. The strongest alternative is the second forward pass, which
  is the cleaner intervention and tests a stronger dose; it was rejected
  on cost, not on merit.*
- **Why the weight is 2.0.** It is a judgment, not a derivation. The
  arithmetic above is the whole justification: it is the dose at which
  the control's per-row gradient weight quadruples, which is large enough
  that a null result is informative about supervision rather than about
  the dose being timid. *Confidence: moderate. A larger dose would make a
  null more decisive and risks destabilising the other batteries; a
  smaller one makes a null uninterpretable.*

**One coupling, stated rather than buried.** The flag changes two things
at once — the control gets a term of its own *and* it gets more rows —
so a positive result will not say which of the two did the work. That is
deliberate and matches the question as John framed it, which contrasts
"its own loss term" against "a third of a shared one". The two halves are
not separated here and a follow-up would be needed to separate them.

**A consequence worth naming:** the state and syntax batteries drop from
about a third of the rows each to about a quarter. Both sit at 0.999 and
1.000 intact, so there is room, but the secondary cells below watch for
it.

---

## Pre-stated outcome cells

**Primary, read on the control battery's intact score at the registered
endpoint evaluation.** These boundaries are John's, set on 2026-09-19
before the code existed.

| control intact score | cell | what it reads |
|---|---|---|
| **at or above 0.60** | **LEARNED** | the control learns when properly supervised. Name-keyed lookup is available to it, and it is using it. Supervision was the binding constraint. |
| **above 0.3227 and below 0.60** | **PARTIAL** | supervision moves it but does not carry it. Something else in the design is also binding. |
| **at or below 0.3227** | **DID NOT LEARN** | supervision is **not** the binding constraint. Option D (a scaffolded intermediate query, which teaches plain name-keyed retrieval before layering the rule on top) or closing A3 is what is left. |

The 0.3227 boundary is the score of the reference solver that cannot read
the name the control question supplies. A battery at or below it has not
learned the task, whatever else is true.

**Secondary cells, reported with the primary and never in place of it.**

| reading | expected | what a miss would mean |
|---|---|---|
| **primary battery still learns** | intact **≥ 0.50** | below 0.50, the reallocation damaged the objective that works, and the pilot answers nothing: the run is reported as a failed intervention, not as evidence about the control. |
| **the input-channel lesion still collapses the primary battery** | collapse, as on all three existing checkpoints (0.57 → 0.14–0.20) | if the primary battery survives its own lesion, ownership has stopped being load-bearing under the new weighting and no reading about the control is available from this run either. |

**No threshold is crossed and no registered verdict is read.** The cells
above are raw intact scores. John's committed threshold lock governs
registered readings on registered checkpoints; this run is unregistered,
reads no registered verdict, and does not touch the lock.

---

## What is run, exactly

Identical to the A3 pilot of 2026-09-15 in every respect but the flag:
one 30M **register-less** run — the launcher has no flag that could train
a register — at **seed 0**, chosen so the comparison against the existing
pilot is matched on initialization and data order and **the loss is the
only thing that differs**. Registered recipe values, unchanged:
585,544,960 tokens, 55,116 steps, batch 128, action weight 1.0,
evaluation every 500 steps at n=100 for the trajectory only. Artifacts go
to a distinct output name so nothing can overwrite the existing pilot's
checkpoint.

**Cost, from the pilot's measured 0.645 seconds per step:** 55,116 × 0.645
= 9.87 hours of training, about 10.2 hours of pod life at $0.99/hour on
the registered venue, so **about $10.2, band $9–13**. That takes the A3
cumulative from $34.31 to about $44.5 against the $100 hard stop. Step
count and token budget are unchanged because the grammar is unchanged;
the one thing that could move the measured pace is that control questions
render at a slightly different length from state and syntax ones, so
padded batches may differ by a few percent. **The ledger records the
measured pace at step 500**, as it did for the pilot, and the estimate is
revised in flight if it has moved.

---

## Order, and the gates

1. This pre-statement, committed **before** the code change. *(Done: this
   file.)*
2. The loss change behind a flag, self-tested, committed.
3. One run staged through the registered launcher with the flag, dry-run
   clean, and a ledger row carrying the estimate **before** any spend.
4. **Stop for John's go, in his own words.** Nothing launches without it.

**Nothing in this document is registered.** It is a pre-statement for an
unregistered diagnostic, and its value is entirely that it was written
down before the code existed and before the number came back.


===== FILE: docs/public-path-roadmap-2026-09-16.md =====

# MVM public path roadmap (drafted 2026-09-16, Pacific)

*Status: APPROVED by John 2026-09-16 (Pacific), verbatim: "Approved on all". Proposed by Claude (Cowork session); steps and dates stand as written.
Companion to `ROADMAP.md` (stage gates), `ROADMAP-post-removal-test.md` (the fork and the paper shape)
and `STATUS.md` (this week). This file covers only one thing: getting from the current experimental
state to something usable in public discourse. It builds on the 2026-08-02 adjudication that the
writeup is one flagship registered-report-style paper (`drafts/paper-removal-test-nature-draft.md`).*

## Why this path matters

1. The Calibration Problem's chapter 1 thesis contract says the wager (self-indexed temporal
   integration as the floor of an inside) and the Part III ethics fail separately. MVM is where the
   wager is exposed to evidence.
2. Public AI-consciousness discourse runs mostly on assertion. Pre-registered instruments that can
   lose, an open ledger and published nulls are the differentiator for Sentient Horizons.
3. The essays, Appendix B ("Running the Instrument") and a possible video series need a concrete
   story. The registered results, including the nulls, are that story.

## Already handled (verified in the repo 2026-09-16, branch gate0-null-calibration)

- Threshold lock committed by John: `6ad4362` (2026-09-16 20:08 PDT).
- John's verbatim go for the A3 seeds 1 and 2 wave: `45fd652` (20:11 PDT). Two pods in flight.
- Pod-side reaping ruled and implemented for future launches: `5dedc18` (20:24 PDT).
- Both process fixes, Gate 3 (passes both arms), L1 localization pipeline built and smoke-tested.
- Ruled 2026-09-16: seed 0 is not-testable on the differential clause, so Amendment A3 as registered
  can no longer return a full registered positive. Seeds 1 and 2 test whether primary-battery
  learnability replicates and whether the control battery is a seed lottery.

## Steps from here

| # | Step | Owner | Proposed date |
|---|---|---|---|
| 1 | Seeds 1 and 2 report, checkpoints fetched and checksummed, pods reaped, ledger actual-after rows | Claude Code session | 2026-09-18 |
| 2 | DECIDE: optional extra seeds (bounded by the $100 A3 stop and the $80 RunPod limit) | John | 2026-09-20 |
| 3 | Blind-localization arm (registered, unconditional): run blind on one of the five A2 register-bearing 30M checkpoints, local, $0. The A3 L1 pipeline does not discharge it | Claude Code session, John schedules | 2026-09-27 |
| 4 | DECIDE the control-battery question: a registered Amendment A4 that makes the control learn reliably, or close A3 with partial discriminators and say so. Without this no future run can return a full verdict | John, on a proposal | 2026-10-04 | **RULED EARLY 2026-09-20: Amendment A3 closes as *not testable* (the pre-registered loss condition on a non-self control at ceiling has fired). Proposal v2 in `docs/step4-control-battery-proposal-2026-09-20-v2.md`; Gate C review RT-94 to RT-117. Grammar redesign deferred to a successor experiment after release. Closure text still to be drafted, after step 3 and the two authorised localization runs, through Gate A.**
| 5 | Refresh `explainer.md` (last touched 2026-07-01, predates the registered removal-test result, MVM-0 and A3). After the 2026-09-30 book text lock | Cowork session | 2026-10-11 |
