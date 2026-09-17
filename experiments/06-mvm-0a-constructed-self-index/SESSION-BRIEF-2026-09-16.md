# Session brief — Amendment A3, 2026-09-15 to 16

*A handoff for another session. Written to be read cold: it assumes you
know nothing about this project. Every claim is traceable to a file named
here. Branch `gate0-null-calibration`, pushed. Total spend this session:
**$13.92**, all of it one training run.*

---

## What the project is trying to do

Minimum Viable Mind builds small systems and measures whether a structural
correlate of self-location is present, treating theories of consciousness
as engineering specifications rather than as philosophy to defend. The
governing distinction comes from the book the programme is built on:
**self-reference** is a report a system carries about itself, and
**self-location** is a structural feature of the processing itself. The
test that separates them is removal. Take away self-location and the
integrated act degrades; take away a description and the processing
carries on intact.

Experiment 6 trains a small transformer on synthetic multi-agent dialogue
and asks whether a self-index can be *constructed* to be load-bearing.

## Where things stood before this session

Badly, and honestly so. The original design installed a designated
"register" meant to hold the model's self-index, trained five
30-million-parameter checkpoints, and then measured that the register was
**numerically active and informationally inert** — removing it entirely
changed no battery score at all. Worse, a control model built *without*
the register passed the same batteries at ceiling. So the thing the design
installed was not doing the work, and the batteries could be solved
without it.

The five-seed programme was halted at four of nine launches. Amendment A3
was the redesign: stop installing a self-index and instead build a task
that cannot be done without one, then make the acquired structure the
lesion target. John ratified it, and this session was meant to execute it.

## What this session actually did

### Four gates, three of which found something wrong

**Gate 0, the null calibration** (`gate0-null-calibration-findings.md`).
Established the noise floor of the measuring instrument before spending
anything. The band came out near 0.01 where a real effect is around 0.73,
so the kill criterion did not fire. It also found that the
revision-conditioned battery yields only 19 scoring cells from 400
episodes, and that a kill criterion added a raw accuracy to a
chance-corrected quantity, which is meaningless.

**Gate 1, the grammar** (`gate1-curriculum-findings.md`). Built the new
task and ran the cue detectors on it. **The grammar took three drafts and
each one traded one flaw for another.** Making the model revise in every
episode gives a scoring cell every time but makes how much an agent speaks
a perfect giveaway. Making every agent revise removes that cue but means
anyone who has already revised can be crossed off, which lifted the true
shortcut ceiling from 0.29 to 0.52. Two revisers drawn uniformly fixes
both. The underlying constraint, which nobody had named: you cannot have
all three of a scoring cell every episode, revising not marking the model
out, and agents that have acted not being eliminable.

**Red-team pass 3** (`red-team-pass-3.md`), run as an independent
adversarial review. Thirteen findings, two fatal. The one that mattered:
**the grammar Gate 1 had just certified did not test self-indexing at
all.** Each turn rendered with the speaker's name first, and the graded
token is the value, so the model's own name sat three tokens back in its
own context at the moment it was scored. A solver using no ownership
information whatsoever scored **1.000 over 3,000 episodes**. The cue gates
could not have caught it because they ask a different question. Fixed for
free by moving the name after the value.

**An ownership-blind attack sweep** (`src/shortcut_sweep.py`), built
because a regression test for the shortcut you already found is worth very
little. It caught the second fatal flaw and is now a registered gate whose
job is to make the stated ceiling honest.

### An instrument was amended, carefully

The cue detector failed the corrected grammar. Investigation showed its
two comparison arms were **drawn by different rules**: the model's turn
agent-first, the comparison turn pooled across three agents, which
over-represents agents who speak more. Since the detector's null is
exchangeability, both arms have to be drawn the same way, which makes this
a bug fix rather than a preference.

John ruled the change through with three conditions, all met: a dated
amendment that **names openly that the change was prompted by a grammar
failing the old detector** (`cue-detector-sampler-amendment.md`), both
numbers reported side by side on every verdict, and a regression check
against every grammar the old detector had passed. That check matters
most for the registered grammar the five existing checkpoints were trained
on: it reads 0.4969 under the old sampler and 0.4984 under the new one, so
nothing earlier is disturbed.

### Fourteen decisions and a registration commit

All fourteen ruled by John, folded into the amendment with the ratified
text left standing and the revisions appended so each names what it
replaces. The most consequential: **the metric now divides each drop by
the measured shortcut ceiling rather than by chance**, because a lesion
cannot push a battery below its ceiling, and the old denominator made a
purely generic result look like a positive.

### The pilot ran, and it answered its question

`gate2-pilot-findings.md`. One register-less 30M model, full registered
budget, 55,116 steps and 585.5 million tokens, $13.92.

| battery | intact | authorship channel zeroed | its shortcut ceiling |
|---|---|---|---|
| **primary (the action)** | **0.506** | **0.182** | 0.2921 |
| control | 0.299 | 0.234 | 0.3227 |
| ownership-free state | 1.000 | 0.999 | — |
| syntax floor | 1.000 | 1.000 | — |

**The objective is learnable**: the primary battery is 0.214 above what
any ownership-blind solver can reach. **And what was learned genuinely
depends on ownership**: zeroing the only authorship signal collapses it to
0.182 while the ownership-free batteries do not move at all. Across 120
random ablations not one pushed it below its ceiling, the worst reaching
0.2758, against 1.515 for the authorship lesion. So the effect is five and
a half times the worst random damage and qualitatively unlike it.

**The control battery never learned**, finishing below its own shortcut
ceiling. This repeats the programme's history, where the comparable
ability was a lottery only two of five earlier runs won.

**Gate 3, the fingerprint detector, passes both arms** (0.483 and 0.4975
clean, controls at 0.9895 and 0.8724), so the training data carries no
ownership fingerprint.

## The three open questions

**1. The headline hypothesis has a term that does not exist.** It requires
the drop on the primary battery to exceed the drop on the control by a
margin. The control never learned, so its baseline sits below its ceiling
and its drop is undefined. The positive bin cannot be satisfied on this
checkpoint — not because the result is negative, but because one of its
terms is missing. Either amend the bin, or get a checkpoint where the
control learned.

**2. The outcome bins do not cover what happened.** The starvation
criterion wants the primary at ceiling with the control flat. The control
is flat; the primary is at 0.506, well above its shortcut floor and
nowhere near 1.0. Half fired. The bins were written before the grammar
existed.

**3. The real prize is now reachable and has not been taken.** A
localization arm was registered unconditionally and never run, and the
argument against it was that its premise had evaporated: with no known
center, failing to find one would prove nothing. **The pilot restored that
premise.** Ownership is now measured to be load-bearing in a specific
checkpoint. So the interpretability toolkit can finally be scored against
a ground truth, and if it cannot carve a center known to be there, the
honest reading of the earlier experiment's null shifts toward instrument
failure. The amendment's own red team called this the finding that might
outweigh the headline. It costs nothing and is the next build.

## Things this session got wrong, and corrected

Recorded because the corrections matter as much as the findings.

- **A reported "truncated checkpoint" was a misreading.** I described the
  fetched checkpoint as silently corrupt and called it a serious process
  failure. It was a file observed part-way through extraction. Corrected
  in the findings note, the status document, the ledger and the worklog
  rather than edited out, because a fabricated defect in the tooling's
  permanent record would send the next session hunting a bug that does not
  exist.
- **Gate 3's first "uncertifiable" was my bad control.** I gave the
  likelihood arm a constant-value filler, which is the classifier arm's
  control and which a likelihood attack is structurally blind to. With the
  registered greedy control it fires at 0.8724.
- **A smoke-scale validity check gave false reassurance** early on,
  appearing to show the task was ownership-dependent when it only showed
  that a tiny network had not yet found a shortcut that was there.

## What is real, and what it cost

Idle billing recurred for the third time: the run finished at 09:54 and
the pod was reaped at 13:47, costing about $3.80 of the $13.92, because
the sleep blocker stops idle sleep but not a closed lid. Now addressed by
having the pod terminate itself on completion, with the laptop as backstop
rather than the only mechanism. Checkpoint pulls also now verify a
checksum before promoting anything.

## State and next steps

Spend $13.92 of a $100 hard stop, inside a $400 all-vendor ceiling.
Nothing running. Gates 0, 1 and 3 complete, registration committed,
calibration done and thresholds measured.

Waiting on John: the threshold lock commit, which is reserved to him; the
go for seeds 1 and 2, about $22 as one wave; and rulings on the two bin
questions above.

Next build, free and highest value: the lesion and localization pipeline
on the checkpoint already in hand.
