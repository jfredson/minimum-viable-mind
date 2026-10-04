# Proposal for John, 2026-10-03: the seven questions version 4 of the proposal asks, one page each

*Written 2026-10-03 (Pacific), late evening, by a Claude Code session, at
John's request. **This is a proposal, not a ruling. Nothing in it is decided
or registered, and no registered text, ruling file, protocol text or proposal
text is changed by it.** Nothing was rented or spent to write it.*

*Written under the workspace plain-language rule. Findings are labelled
**MEASURED** (in a committed file named beside them) or **ARGUED** (reasoning
a reader can dispute).*

**The questions come from** section 19 of version 4 of the successor
experiment proposal, `docs/successor-experiment-proposal-2026-10-03-v4.md`,
read at commit `a64aa82` on pull request 83, which was open and unmerged when
this was written. Each page gives version 4's own suggestion and then this
session's recommendation, and says where the two differ.

**Three things to know before relying on this packet.**

1. **This session did not write version 4, but it wrote much of what version
   4 is built from:** the review of version 3, the first two ruling packets,
   their records and the controls re-run. Questions 1, 2 and 3 are about gaps
   in rulings this session drafted, and question 2 is about a reading this
   session chose. Where that is so the page says it.
2. **It is owed a check** by a session that did not write it, like the
   packets before it. Version 4 is itself still owed its check.
3. **Pages 6 and 7 are the ones that most deserve reading in full.** Page 6
   sets a new rule for how a result is named. Page 7 is the only one that adds
   a run.

**What the answers add to the work before the registration review:** page 7
adds one short run at $0. Page 5 adds a small code change and a repeat of a
code test. If page 2 or page 4 is ruled the other way from the
recommendation, each adds a toy re-run and its check. The rest are wording.

---

## The one-page index

"Agreed on all", or exceptions by page number, is enough.

| Page | Question | Version 4 suggests | This packet recommends | Confidence |
|---|---|---|---|---|
| 1 | Must the whole read still reach four fifths, now that the piece must? | The piece only | The same | moderate to high |
| 2 | Is the piece rule applied after the layers are chosen? | Confirm it | Confirm it, and say in the registration what it can miss | moderate |
| 3 | Which device and number format is the registered accuracy computed on? | The laptop's processor | The same, with the library versions pinned in a committed file | high |
| 4 | How many episodes at full size? | The toy's counts | The same, with the size of the sampling noise at the floor printed beside the count | moderate |
| 5 | The other-agent control: one random piece or twenty? | Twenty | The same | moderate |
| 6 | What is a model's outcome when its three seeds disagree? | Two seeds of three | Two of three, **and the separation is no longer paired by seed number** | moderate; the second half is this packet's own |
| 7 | Is the ordinary competing solver run under the new rule? | Run it, $0 | The same | high |

---

## Page 1 — must the whole read still reach four fifths, now that the piece must?

**The question.** On 2026-09-26 John ruled a four-fifths floor on the whole
straight-line read (the finding RT-212). On 2026-10-03 he ruled that only
pieces which themselves reach four fifths may be chosen. Is the first still a
second condition?

**Why it is open.** This session drafted the 2026-10-03 ruling and did not
say. The controls re-run applied the floor to the piece only.

**What is on the record** (MEASURED:
`experiments/rehearsal-successor-measure/out-controls-rerun/`). On the twelve
toy models both readings give the same verdicts. A piece can score an episode
or two above its whole read: on the one model where the named agent's read
was tried, the 8-direction piece was right on 139 of 180 and the whole read
on 137. So a model sitting at the line could pass on the piece and miss on
the whole read.

**Recommendation: the piece only, with the whole read's count printed beside
it.** *Confidence: moderate to high.* The piece is what gets transplanted, so
it is the thing whose label-carrying needs certifying. A second floor is a
second way for the model being read to return no verdict, and it certifies
nothing the first does not. Version 4 suggests the same.

**Strongest alternative:** require both. It costs nothing on the toy and
keeps the 2026-09-26 ruling to its letter.

*Amends:* the ruling of 2026-09-26 on RT-212, item 1, which gains a dated
note. *Changes:* nothing in version 4, which is written this way.

---

## Page 2 — is the piece rule applied after the layers are chosen?

**The question.** The rule first picks, for each group of positions, the
fewest layers at which the whole-state transplant works. Only then does it
ask which sizes of piece carry the label. So the piece rule can exclude
sizes; it can never send the choice to a different layer.

**Why it is open.** This was this session's reading when it wrote the
controls re-run's method, marked as John's to overturn. It has never been put
to him directly.

**What it can miss** (ARGUED, with one toy instance). The earliest layer at
which the transplant works need not be a layer at which the label can be read
where the model acts. If it is not, the model returns "no verdict, read failed
its floor" even though a later layer might have passed. The toy shows the
shape once: on the free model's seed 0, for the named agent's read, the
candidates were layers 1 and 3 (best pieces 92 and 115 of 180) while layer 2,
not a candidate, had the best piece of all (139). None reached 144, so
nothing turned on it there (MEASURED:
`out-controls-rerun/measure_F_seed0.json`, `control2`).

**The options.**

- **(a) Confirm it as run.** It is the only order that has been rehearsed.
- **(b) Let the piece rule take part in choosing the layers:** per group of
  positions, the fewest layers at which the transplant works *and* some size
  carries the label. It gives the free model its best chance of a reading. It
  has not been run; it needs the toy re-run again and a check, about half a
  day, before the registration review. It also lets the read's accuracy steer
  the choice of site, which the design has so far kept apart on purpose.

**Recommendation: (a), and the registration says in a sentence what it can
miss.** *Confidence: moderate.* The cost of (a) lands in one place, the stop
after the first full-size free-model run, and John already ruled that the
report for that run prints the accuracy at every layer and the candidates the
rule chose among. So if this is what causes a miss, he will see it in the
figures and can rule with them in hand. Version 4 suggests confirming it.

**Strongest alternative: (b)**, if John would rather not spend about $44 to
learn that the order of two steps cost him the reading.

*Changes:* one sentence in version 4, section 7.2 and weakness W12.

---

## Page 3 — which device and number format is the registered accuracy computed on?

**The question.** John ruled on 2026-10-03 (the finding RT-232) that the
registration names the device and that the figure on that device is the
registered one. He was not asked which.

**What is on the record** (MEASURED: the review of version 3, RT-232). The
free model's toy accuracies differ by one held-out episode between the
laptop's processor and its graphics chip. Every toy figure since the controls
re-run was computed on the processor.

**Version 4 writes:** the laptop's processor; the model's states in 32-bit
numbers; the read fitted by scikit-learn in 64-bit; the library versions
recorded.

**Recommendation: confirm that, and pin the library versions in a committed
file named in the registration**, in the way `.venv-lock-2026-08-28.txt`
already does for the project's environment. *Confidence: high on the
processor; moderate on pinning.* A hard line read to one episode should not
move because a library was upgraded between the registration and the reading.

**Strongest alternative:** the graphics chip, which is faster on a
30-million-parameter model and is what the earlier committed figures used.
Nobody has measured how long the processor takes at full size; if it turns
out to be impractical, that is a fresh question for John then, not a quiet
switch.

*Changes:* version 4, section 7.2, item 1, one clause on the pinned file.

---

## Page 4 — how many episodes at full size?

**The question.** Every bar in the design is a share or a rule. No ruling
says how many episodes each is measured on at full size.

**Version 4 suggests the toy's counts:** 600 development episodes with the
last 180 held out; 800 fresh matched pairs; 800 on the relaxed set; 3,000 for
the gates; 200 shuffles for the permutation baseline.

**What the count means at the floor** (ARGUED, ordinary sampling arithmetic).
With 180 held-out episodes the floor is 144. One episode is 0.0056. A piece
whose true accuracy is exactly four fifths would land within about three
points either way (roughly 139 to 149) on most draws, and would pass about
half the time. So at 180 the floor cannot tell 0.78 from 0.82.

**The options.**

- **(a) The toy's counts, unchanged.** The only counts the procedure has been
  rehearsed at.
- **(b) More held-out episodes for the read only** (for example three times
  as many), leaving the transplant counts alone. It narrows that band to
  under two points. It changes a rehearsed quantity, so the toy fits would
  need running once at the new count, with a check.

**Recommendation: (a), and the registration prints, beside every count
against the floor, the band that sampling alone would put around it.**
*Confidence: moderate.* The one place this matters, the stop after the first
full-size free-model run, is not automatic: a miss goes to John with the
figure, and with the band printed he can tell a miss by two episodes from a
miss by forty. Version 4 suggests the same counts.

**Strongest alternative: (b).** It is cheap, and it is the better instrument.
What it costs is a small re-run and a check inside the two weeks before the
registration deadline.

*Changes:* version 4, section 9 (the last row, filled) and section 7.5 (the
band printed).

---

## Page 5 — the other-agent control: one random piece or twenty?

**The question.** John ruled on 2026-10-03 that this control is reported as
two figures: how often the model's own-marker action moves under the other
agent's piece, and how often under "a random piece". The code draws one
random piece. The neighbouring control draws twenty.

**Recommendation: twenty, reported the way the neighbouring control reports
them** (the middle value, the 95th percentile, and where the real figure sits
among them). *Confidence: moderate.* With no pass line, one random draw is a
weak thing to print beside a figure a reader has to judge. Version 4 suggests
the same.

**What it adds.** A small code change, and the code test of 2026-10-03 run
once more on the changed code, labelled as before as a test of the code and
not a result. A few minutes.

**Strongest alternative:** leave it at one, since the control is expected to
return no verdict anyway.

*Changes:* version 4, section 7.3, item 2; the rehearsal code.

---

## Page 6 — what is a model's outcome when its three seeds disagree?

**The question.** Every floor and every control that holds is applied per
model and per seed. So a model can return a reading on two seeds and no
verdict on the third. The rulings speak of "no verdict on arm C", "on arm F"
and so on, and do not say how many seeds make that so. On the toy every model
behaves alike on all three seeds, so this has never come up.

**Why it deserves attention.** It decides which registered words the result
is reported in, and it is a new pre-stated rule that nothing has rehearsed.

**Part 1: how many seeds.**

- **(a) At least two of three, with the third reported.** A model "reads" if
  two of its seeds return a reading. This is the rule the design already uses
  for whether a model learned the task and for the channel-removal check.
- **(b) All three.** Stricter. It makes the two-model fallback and the fifth
  outcome more likely.

**Recommendation for part 1: (a).** *Confidence: moderate.* One rule for
"how many seeds" across the design is easier to hold to than two. Version 4
suggests the same.

**Part 2, which is this packet's own and not version 4's: the separation is
paired by seed number, and that pairing means nothing.** The bar is written
as the entangled model's reading minus the separable model's, "per seed".
Seed 0 of one model has no relation to seed 0 of another; they are separate
trainings that happen to share a number. With two seeds reading on one model
and three on the other, the pairing is not even defined.

**Recommendation for part 2:** the separation is **the lowest reading among
the entangled model's seeds that read, minus the highest among the separable
model's seeds that read**, and it must clear 0.5. *Confidence: moderate.* It
needs no pairing, it is defined whenever each model reads on at least two
seeds, and it is the stricter of the two ways. On the toy it gives 0.9926
(MEASURED: `out-controls-rerun/summary.json`: the entangled model reads
1.0051, 0.9926 and 0.9974; the separable model 0.0000 on every seed).

**Strongest alternative for part 2:** keep the per-seed wording and require
two of three pairs to clear, accepting that the pairing is arbitrary.

**What follows from both parts.** "Metric validated" means both built anchors
read on at least two seeds and the separation as defined clears 0.5. "Degree
read" means the free model reads on at least two seeds; with one seed reading,
the result is "metric validated, degree not read", and the one figure is
printed as a description.

*Amends:* the ruling of 2026-09-25 that set the separation bar "per seed"
(`docs/rulings/2026-09-26-weekend-1-queue.md`, page 1a), which gains a dated
note. *Changes:* version 4, sections 3 and 9.

---

## Page 7 — is the ordinary competing solver run under the new rule?

**The question.** The protocol's rehearsal asks that a system with none of
the structure the measure claims to detect be put through the same
measurement, so that "could this be satisfied by the wrong thing" has a
number behind it. The toy has such a system: a solver trained with no acting
channel at all. It was scored on the task before the piece rule existed. It
has never been put through the nomination and the reading as now ruled.

**What exists** (MEASURED: the three files are committed with fingerprints at
`experiments/rehearsal-successor-measure/out-repairs/models/ckpt_blind_base_seed{0,1,2}.pt`).

**The options.**

- **(a) Run it:** the three committed models through the nomination and
  reading as registered, on the laptop, $0, method committed before output,
  checked by a second session.
- **(b) Say in the registration that it was not measured under the rule,**
  and let the registration review decide whether that is a finding.

**Recommendation: (a).** *Confidence: high.* It is an afternoon. The expected
result is a no verdict on every seed, because a solver that is never told
which turns are its own should have no read of its own marker that reaches
four fifths. If that is what comes back, the registration review's first
question has a number. If it is not, something is wrong with the measure and
it is far better to learn it now. Version 4 suggests the same.

**One thing the method must settle before it runs** (ARGUED): the solver has
no acting channel, so "the model's own turn" and its twin pairing need a
stated meaning for it. That choice belongs in the method file, marked as the
running session's reading.

**Strongest alternative: (b).** Under item 5 of the ruling of 2026-09-21 an
unexercised rehearsal item is likely to be found fatal at that review, so (b)
mostly moves the same work later.

*Changes:* one more short run before the registration review; version 4,
sections 7.3, 8.1 and 10, which then quote its figures.

---

## Appendix — where each fact comes from

- The seven questions and version 4's suggestions: version 4, section 19, at
  `a64aa82` (pull request 83).
- Page 1: the named read's counts, `out-controls-rerun/measure_F_seed0.json`,
  field `control2`.
- Page 2: the same field (candidates at layers 1 and 3; the fits at every
  layer); the ruling on the fuller report for the first full-size run,
  `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 3, RT-235.
- Page 3: the review of version 3, finding RT-232.
- Page 4: the band is the ordinary spread of a count of 180 at a true share
  of 0.8 (about three points either side, two standard deviations being about
  six points); it is arithmetic, not a measurement.
- Page 6: `out-controls-rerun/summary.json`; the separation bar,
  `docs/rulings/2026-09-26-weekend-1-queue.md`, page 1a.
- Page 7: `out-repairs/models/SHA256SUMS`; item 5 of
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`.
