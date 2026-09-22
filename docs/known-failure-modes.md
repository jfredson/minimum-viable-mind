# Known failure modes, and the test that catches each one

*Written 2026-09-21 (Pacific) as the companion to the outside-review protocol
(`docs/outside-review-protocol.md`). That protocol was amended the same day to
require every registration text to be run against this list rather than to cite
it. This file is the list.*

*Approved by John as one of six recommendations put to him with its cost, in his
words "Ok, can we implement all of these?". The session proposed and he
approved; the wording here is the session's and is his to overturn.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30).*

---

## What this list is for

Four things have gone wrong in this programme badly enough to cost weeks of work
or to put an unsatisfiable sentence into text that had already been registered.
Each is easy to recognise once it has been named — and, as it turns out, just as
easy to reproduce while naming it. A proposal reviewed on 2026-09-21 quoted the
first failure below by name, in the section discussing the weaknesses of its own
measure, and the measure two sections earlier reproduced it.

So this is not a reading list. Every entry ends with a test: a command a session
can run against a new design, and what the output has to show. The protocol's
failure-mode pass requires that test to be run and its output filed, for every
failure here, on every registration text. **"Considered and does not apply" is
not a disposition.** The count that is not zero, the cell that has trials in it,
the record that exists and contains what the sentence says it contains — those
are dispositions.

Every output printed below was produced by running the command printed above it,
in this repository, on 2026-09-21.

---

## 1. A comparison whose denominator was zero

**What it was.** Amendment A3 registered a corrected measure that subtracts, from
each score, the best a solver could do while ignoring ownership — the
ownership-blind ceiling — and then divides by the distance left between that
ceiling and a perfect score. For the control battery (the comparison battery of
questions, built so that answering it does not require knowing whose value is
whose), that ceiling turned out to be 1.0. The distance left was zero. The
measure had nothing to measure, and had had nothing to measure from the day it
was registered.

**How it showed up.** The third adversarial pass said it four days before the
registration commit, in its twenty-first finding — the unequal-ceilings finding
(`RT-21` in the red-team ledger), marked fatal, whose metric fix was marked
adopted. The fix depended on a ceiling nobody had measured. The measurement, when
it was finally made, is
`experiments/06-mvm-0a-constructed-self-index/ceiling-measurement-findings.md`,
whose title is the finding: "The control battery's ceiling is 1.0, and the clause
was never computable." A battery built so that its questions do not require
ownership has an ownership-blind ceiling of 1.0 by construction; dividing by the
distance to 1.0 divides by zero.

**Its newest form, found 2026-09-21.** The successor experiment proposal
registers its reading as the difference between two accuracies divided by the
larger of them, with no floor subtracted from either. A floor that sits under
both terms does not cancel in a ratio, so the largest value the reading can
return is different for every arm — every version of the system being compared —
because the accuracy it divides by is different for every arm, and the design
expects it to be. Two systems separable to exactly the same degree then read
differently for no reason but their overall accuracy. This is the ceiling failure
with the zero replaced by a moving number, which is harder to see and no more
measurable. It is filed as the first finding of the Gate C pass on that proposal
(`RT-172`, the per-arm-ceiling finding), in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md`
— which at the time of writing sits on the reviewing session's own branch
(`worktree-agent-a5e89aa434ea3f396`) and is not yet on the main line.

**The test.** Two parts, both cheap.

*Part one: print the denominator at the ceiling, for every condition the reading
will be applied to, using ceilings measured in the rehearsal rather than
assumed.*

```
$ python3 -c "
ceilings = {'primary battery': 0.2921, 'control battery': 1.0000}
for name, c in ceilings.items():
    print(f'{name}: denominator 1 - ceiling = {1 - c:.4f}')
"
primary battery: denominator 1 - ceiling = 0.7079
control battery: denominator 1 - ceiling = 0.0000
```

*Part two: print the largest value the reading can return, per condition, when
the thing it is meant to detect is entirely absent.*

```
$ python3 -c "
def reading(whole, ownership_only): return (whole - ownership_only) / whole
floor = 0.125
for whole in (0.90, 0.60, 0.35):
    print(f'best score {whole}: top of scale = {reading(whole, floor):.3f}')
"
best score 0.9: top of scale = 0.861
best score 0.6: top of scale = 0.792
best score 0.35: top of scale = 0.643
```

**It fails if** any denominator is zero, or small enough that ordinary noise in
the measured ceiling moves the reading a lot; or if the top of the scale differs
between the conditions a single pre-stated threshold is compared across. A
threshold in units whose top of scale moves between where it was set and where it
is applied is not a threshold. Both halves need numbers from the rehearsal: a
ceiling that was assumed rather than measured is what produced this failure in
the first place.

---

## 2. A probe target that cannot be recovered in principle

**What it was.** The localization line spent weeks predicting `own_slot` — the
episode generator's index for whichever agent the model is playing — from the
model's internal states. That quantity has no consistent surface realisation: the
generator knows it, and nothing the model was shown or trained on requires the
model to compute it. It cannot be recovered from these states at any position,
with any instrument. Every null the line produced was therefore a null about an
unanswerable question, which is not evidence of the absence of anything.

**How it showed up.** In the position sweep of 2026-09-19
(`experiments/06-mvm-0a-constructed-self-index/position-sweep-findings.md`),
whose first arm came back "SWEEP INVALID on all three checkpoints" because its
positive control failed: zero of 165 tests cleared the bar. The finding names
what that cost — the blind-arm probes of 2026-09-16, the denoise-before-probing
diagnostic and the sweep itself "were all asking a question with no answer". The
contrast is the powered target test of the same day
(`powered-target-test-findings.md`): with the target re-posed as a quantity that
demonstrably reaches the states — the marker word, read at the position where it
*is* the input token — the same kind of read returns 0.5877 against a
no-information value of 0.04, about 159 standard deviations of its own null. The
instrument was never the problem. No review pass had been asked whether the named
quantity was recoverable at all.

**The test.** Two parts, one of them free.

*Part one, paper and pencil, before anything is registered:* write one sentence
naming the route by which the quantity reaches the model's states — which token
carries it, or which part of the loss forces the model to compute it. "The
episode generator knows it" is not a route. If no such sentence can be written,
the pre-statement changes before it is registered, not after the probes come back
empty.

*Part two, run in the rehearsal:* run the whole probe pipeline twice — once on
the pre-stated target, once on a quantity the design guarantees is present, read
at a position where it must be present — with the same bar and the same null.

```
$ python3 src/<probe_script>.py --target <the pre-stated quantity> --report margins
$ python3 src/<probe_script>.py --target <a quantity the input guarantees> --report margins
```

**It fails if** the second run does not clear the bar. A pipeline that cannot
recover a quantity known to be there has not measured the target; it has measured
its own noise, and a null from it says nothing. File both runs. A pre-stated probe
target whose positive control was never run is a fatal finding on its own, on the
same reasoning as a pre-stated quantity the rehearsal never exercised.

---

## 3. A cell that is empty by construction

**What it was.** Found 2026-09-21, in the successor experiment proposal. One of
the seven pre-stated controls — the one that separates "the transplant moved who
is acting" from "the transplant smuggled a value across", and so the one the
whole reading leans on — splits trials into pairs where the donor's identity
dictates the *same* answer as the recipient's and pairs where it dictates a
*different* one. Both cells are pre-stated and both are to be reported. The
grammar the design extends draws four *distinct* values for each contested item,
one per agent, without replacement, and asserts that the property survives
rendering. Two agents therefore never dictate the same answer, the first cell can
never hold a trial, and three other passages of the same proposal require the
distinctness that empties it. Filed as the second finding of the Gate C pass on
that proposal (`RT-173`, the empty-cell finding), in the same review file named
under failure 1 above and with the same caution about which branch it is on.

**The same defect one step further.** That control carries a pre-stated check: an
untouched condition "should be near the one-in-eight guessing rate; if it is not,
the pairing is broken and nothing is read." With distinct values, a model that has
learned the task lands on the donor's answer only by erring onto exactly that
slot. The rule as written passes a model that has learned nothing and fails one
that has learned the task. It is pointed the wrong way round, and it sits inside
the list of things the design proposes to freeze.

**The test.** Two parts, and a third for any threshold attached to a cell.

*Part one: count what the generator actually puts in each pre-stated cell, at
rehearsal scale.*

```
$ python3 -c "
from collections import Counter
from src.curriculum import generate          # the registered generator, not a stand-in
counts = Counter(cell_of(trial) for trial in generate(n_episodes=200, seed=0))
for cell in PRE_STATED_CELLS:
    print(f'{cell}: {counts.get(cell, 0)} trials')
"
```

*Part two: look for the property in the generator that would empty a cell —
drawing without replacement, a distinctness assertion, a deterministic rule that
makes two conditions the same condition.*

```
$ grep -n "rng.sample\|assert len(set" experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py
209:    markers = rng.sample(MARKERS, N_AGENTS)
210:    contested = rng.sample(ITEMS, N_CONTESTED)
215:        vs = rng.sample(SLOTS, N_AGENTS)
233:    revisers = rng.sample(range(N_AGENTS), K_REVISERS)
539:            assert len(set(vs)) == N_AGENTS, "distinctness broken by enactment"
```

*Part three: compute every pre-stated threshold at both ends of the range it will
face — a system that has learned the task and one that has learned nothing — and
print what the check returns at each.*

```
$ python3 -c "
for p in (0.95, 0.80, 0.60, 0.25):
    print(f'own-directed accuracy {p:<5} -> untouched rate {(1 - p) / 7:.4f}')
"
own-directed accuracy 0.95  -> untouched rate 0.0071
own-directed accuracy 0.8   -> untouched rate 0.0286
own-directed accuracy 0.6   -> untouched rate 0.0571
own-directed accuracy 0.25  -> untouched rate 0.1071
```

**It fails if** any pre-stated cell comes back with zero trials, or if a threshold
fires on the healthy end of the range and passes on the broken end. Both are
fatal: the first registers a comparison that can never be made, the second
registers an instrument check that reads a working instrument as a broken one.

---

## 4. A claim of measurement with no record, or with a record that does not reproduce

**What it was, first form.** Amendment A3's registered text said both battery
ceilings were "verified by the attack sweep, whose best ownership-blind attack
reached 0.3036 on 12,000 episodes". The 0.3036 is an attack on the primary
battery. The attack sweep contains no control-battery code at all, so the clause
is false as applied to the control, and the control's registered ceiling rests
entirely on one reference solver that ignores the one piece of information the
control question supplies. Registered on John's instruction, before any further
analysis, in
`experiments/06-mvm-0a-constructed-self-index/ceiling-defect-2026-09-17.md`. One
sentence had attached one verification to two numbers, and the number it did not
cover is the one that later turned out to be 1.0 — which is failure 1 above.

**What it was, second form.** A finding labelled MEASURED reported a count that
does not reproduce. The seventeenth finding of the independent pass on the
Amendment A4 clause (`F17`, on whether one condition's validity gates were ever
applied) says the endpoint records carry no such field "among their 110 keys".
They carry 15. John ruled on this on 2026-09-21, as the twentieth item of that
day's review-verification and staged-spending ruling
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`): the
finding's substance is undisturbed, but a MEASURED label is this programme's
promise that a number came from running something, and a committed record a
future session may cite has to be right.

**The test.** Two parts.

*Part one: list every sentence in the text that claims a measurement, so that
none is checked by accident and none is missed.*

```
$ grep -n -E "verified|measured|calibrated|attacked|reproduc|confirmed|ran" <the text>.md
```

*Part two: for each sentence the first part returns, name the file it cites and
run the one command that regenerates the number. Two worked examples, both from
the failures above:*

```
$ grep -c control experiments/06-mvm-0a-constructed-self-index/src/shortcut_sweep.py
0
```

```
$ python3 -c "
import json
base = 'experiments/06-mvm-0a-constructed-self-index/a3-gates/'
for p in ('endpoint_a3_30m_seed1.json', 'endpoint_a3_30m_seed2.json', 'pilot_endpoint.json'):
    print(p, len(json.load(open(base + p))))
"
endpoint_a3_30m_seed1.json 15
endpoint_a3_30m_seed2.json 15
pilot_endpoint.json 7
```

The first says that the module the registered sentence credits with verifying the
control battery's ceiling does not mention that battery once. The second says
where 110 came from: nowhere.

**It fails if** a sentence claiming a measurement names no file; or names a file
that does not contain the number; or names a file that exists at no commit, which
is its own recurring form — the citation defect that stopped the previous version
of the Amendment A3 closure text was exactly this (`RT-145` in the red-team
ledger, the finding that a registration commit was resting on a ruling file that
had not been committed). A registration commit is the one commit that may not
rest on a record its reader cannot open.

---

## Adding to this list

A fatal finding that is a new species — not a new instance of one of the four
above — is added here by the pass that found it, with its test written the same
way: a command, and what the output has to show. Write the test so that a session
holding a different design can run it without asking anyone what it means.

An entry here is binding text under the protocol's pairing rule, so a session
other than the one that wrote it checks the entry: that the test runs, and that
it fails on the design that produced the finding. A test that has never been seen
to fail has not been shown to detect anything.

The list is added to and not shortened. A failure that has stopped recurring is a
failure whose test is passing, which is the reason to keep running it rather than
a reason to drop it.
