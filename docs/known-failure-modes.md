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

Five things have gone wrong in this programme badly enough to cost weeks of work,
to put an unsatisfiable sentence into text that had already been registered, or to
create a rented machine with a command documented as creating nothing.
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

**What this list has been shown to be, and what it has not.** As a description of
what has gone wrong here, it is accurate.

**Which blocks below have been run, and which have not.** Fifteen blocks are
printed below. Twelve carry a command and the output that running it produced.
A thirteenth, the first block under failure 5, is different in kind and is
flagged again where it appears: it is the **recorded** output of the command
that created a rented machine on 2026-09-21, and it must never be re-run,
because re-running it is the failure. The block beneath it is failure 5's
actual test, which was run, and which creates nothing.
Ten of those eleven have been re-run by a session other than the one that wrote
them and compared against the printed text with `cmp`, which names the first byte
at which two files differ; nothing differed. The eight the list carried before
the repair described below had already been checked the same way once, with
`diff`. The eleventh is newer than that check: it is the block under failure 2
that prints the two rows illustrating that failure's middle limb, and the session
that added it ran it, but no other session has yet re-run it. The remaining two
blocks carry placeholders in angle brackets and no output. One of them is failure
4's first part, written as a template because it is pointed at whatever document
is under review; the word lists inside it are exercised on six worked claims in
the block below it, and that block was run and its output printed. **The other is
failure 2's second part, and it has never been run at all.** Running it means
running a whole probe pipeline twice against model checkpoints, which costs
compute that nobody has authorised. Its middle limb — the second run clears the
bar and the first does not — is now illustrated, by a printed block under failure
2 showing the two rows in the position sweep's findings file where exactly that
pattern appears. Illustrated is not executed: those rows come from the history
this entry was written from, so the limb still has not been seen to fire on
anything it had not already been fitted to.

As a set of tests a new design can be run against, this list is not yet
established. The first check found that three of the four tests fell short of the
standard this document sets on its own last page — that a test never seen to fail
has not been shown to detect anything. One passed on the very design that
produced the failure it describes, one did not execute at all, and one looked
only for words that the newest form of its own failure does not use. Those three
were repaired on 2026-09-21 by a third session. Failure 3's empty cell and
failure 4's widened word list are each printed below with the command and the
output showing the test failing on the design it was written from. Failure 2 is
printed that way for its first part only, and that part is a proxy rather than a
detector, for the reasons set out under it.

**Where that leaves the list.** The repairs have been checked once, by the
session that wrote
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-protocol-repair-claude-worktree.md`
at commit `fbfecb5`, the commit titled "Check the repair: the ten outputs hold,
two tests still owe a sentence". That check found the two gaps the paragraphs
above and the paragraph under failure 2's first part now fill. Those two
corrections were written by a fourth session and have not themselves been checked
by anyone. Under the pairing rule in the protocol beside this file, they are owed
a check by a session that did not make them. Until that check exists, treat this
list as a reliable account of the past and an unproven instrument for the future:
run it on a registration text and file what it returns, but do not read a clean
pass from it as evidence that a design is clean.

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
at commit `3bbfece`, the commit titled "Gate C tier 1 review of the successor
experiment proposal: RT-172 to RT-188". The commit is named and not only the
branch it was written on, because a session branch is deleted once it is merged
and a citation anchored to one loses its signpost without anyone editing the
sentence. The design being criticised is the successor experiment proposal
(`docs/successor-experiment-proposal-2026-09-21.md`) at commit `d8ceba9`, the
commit titled "Successor proposal: the rehearsal buys a rented slice, and the
second release is bound to what it measures", which was written on a different
branch again. Both commits have since reached the main line in the working
checkout, though neither had been pushed to the shared copy of the main line when
this was written.

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

**Part one is a display and not a detector; part two below is what does the
detecting.** The arithmetic only shows what it is handed. Hand it the ceilings as
they were actually registered on 2026-09-15 — 0.2921 for the primary battery and
0.3227 for the control (`amendment-a3.md` line 415) — and it prints two healthy
denominators, with nothing to see:

```
$ python3 -c "
ceilings = {'primary battery': 0.2921, 'control battery': 0.3227}
for name, c in ceilings.items():
    print(f'{name}: denominator 1 - ceiling = {1 - c:.4f}')
"
primary battery: denominator 1 - ceiling = 0.7079
control battery: denominator 1 - ceiling = 0.6773
```

That is the failure passing its own test. The zero only appears once somebody has
measured the ceiling, and measuring it is the rehearsal's job, not this test's. So
part one's failure criterion is about where its numbers came from rather than
about the arithmetic: **it fails if any ceiling typed into it cannot be traced to
a committed measurement record**, named by file. Type in an assumed ceiling and
this command reproduces the original failure while producing a filed output that
looks like a disposition — which is what 0.3227 was.

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

**The test.** Two parts. **Part two is the one that catches this failure; part
one is a prompt to look.** Part one asks for a written sentence and checks that
it exists, which forces the question to be faced but settles nothing on its own.
Part two runs the probe twice and compares the two results, and its middle limb —
the second run clears the bar and the first does not — is what actually
distinguishes an unrecoverable target from a working one. Part two has never been
run; see the paragraph under it.

*Part one, before anything is registered:* the method document states, in one
sentence and in a fixed form of words, the route by which the quantity reaches
the model's states — which token carries it, or which part of the loss forces the
model to compute it. "The episode generator knows it" is not a route. Writing the
sentence is paper and pencil; **checking that it is there is a command**, so that
this part produces a disposition with its work shown like every other:

```
$ python3 -c "
import re
pattern = r'route to the states|carried by the token|forced by the loss|is the input token'
base = 'experiments/06-mvm-0a-constructed-self-index/'
for f in ('position-sweep-method.md', 'powered-target-test-method.md'):
    lines = [l.strip() for l in open(base + f) if re.search(pattern, l, re.I)]
    print(f'{f}: {len(lines)} route sentence(s)')
    for l in lines:
        print('   ' + l)
"
position-sweep-method.md: 0 route sentence(s)
powered-target-test-method.md: 1 route sentence(s)
   the marker position**, where it is the input token. It must clear three
```

That is this failure caught, on the design that produced it, with a command and
an output. The method committed before the sweep that spent weeks on `own_slot`
contains no sentence naming a route, because none could be written. The method
for the target that turned out to be recoverable contains one, and it names the
token. Run this on a new design's method document with that design's own wording
in the pattern; a count of zero is the finding.

**What this search cannot see, plainly.** It counts sentences that match a fixed
set of words, so it cannot see a route named in any other words. Run exactly as
printed above across all nine method documents in this experiment, seven come
back at zero, and one of the seven is the method for the powered eleven-position
sweep
(`experiments/06-mvm-0a-constructed-self-index/powered-position-sweep-method.md`),
which does what this part asks for and does it at length: it names in advance the
token that carries the target at one position, and says that nothing carries it
at another. It scores zero because it writes "as an input token" where the
pattern says "is the input token". That run is printed in the check of this
repair
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-protocol-repair-claude-worktree.md`
at commit `fbfecb5`, the commit titled "Check the repair: the ten outputs hold,
two tests still owe a sentence"). The other direction is no better: a count above
zero says only that some sentence matched the words typed into the pattern, and
the instruction to run it with the new design's own wording means a session that
writes the pattern out of the document it has just read will match by
construction. What this command records is whether the checking session found a
sentence it was willing to call a route — worth recording, because it forces one
specific sentence to exist and be quoted into the filed output where it can be
argued with by name, but not a measurement of whether a route exists.

**So part one is a prompt to look and not a verdict**, and the sentence above
calling a count of zero the finding should be read that way: a zero is a reason
to go and read the method document and settle in writing whether a route is named
there, and a sentence that matched is not on its own a pass.

*Part two, run in the rehearsal:* run the whole probe pipeline twice — once on
the pre-stated target, once on a quantity the design guarantees is present, read
at a position where it must be present — with the same bar and the same null.

```
$ python3 src/<probe_script>.py --target <the pre-stated quantity> --report margins
$ python3 src/<probe_script>.py --target <a quantity the input guarantees> --report margins
```

**It fails if** any of three things is true, and they are read together:

- **Part one returned no route sentence.** Fatal on its own, whatever the two
  runs do. A target whose route nobody can name is the target that has cost this
  programme weeks.
- **The second run clears the bar and the first does not.** *This is the failure
  this entry exists for.* A working instrument that returns nothing on the
  pre-stated target is evidence that the target is not there to be recovered —
  not evidence about the system being probed. The pre-stated target changes
  before registration, and the null already collected is withdrawn rather than
  reported.
- **The second run does not clear the bar.** Then the pipeline is broken and
  nothing has been measured at all; the first run says nothing either way,
  whether it cleared or not.

File both runs. A pre-stated probe target whose positive control was never run is
a fatal finding on its own, on the same reasoning as a pre-stated quantity the
rehearsal never exercised.

**Why the criterion is written this way.** Until 2026-09-21 this entry said only
"it fails if the second run does not clear the bar", and on the history the entry
is written from that test passes. The second run is the one on the quantity the
input guarantees, and in the position sweep of 2026-09-19 it cleared by an
enormous margin — 0.5877 against a no-information value of 0.04, about 159
standard deviations — which is the same evidence the entry itself cites for "the
instrument was never the problem". A criterion that looks only at the pipeline
detects a broken pipeline. It cannot detect an unrecoverable target, which is
what this entry is about, and the pattern that reveals one — the first run empty
while the second clears — was not named as a failure anywhere in the entry. It is
now the second bullet above.

**What that middle limb looks like in the record, with the test itself still
unrun.** The two runs part two asks for were never made. But a diagnostic filed
with the position sweep of 2026-09-19 read both quantities at the same position,
through the same instrument, each against its own fifty-draw permutation null,
and the sweep's bar throughout is three standard deviations of that null. Those
two rows are in its findings file, and this is them:

```
$ grep -nE "own_slot.*what the stack asks for|marker_token.*the input token itself" experiments/06-mvm-0a-constructed-self-index/position-sweep-findings.md
120:| `own_slot` — what the stack asks for | 0.293 (+1.60) | 0.273 (+0.88) | 0.243 (−0.24) | 0.283 (+1.33) | 0.275 (+0.91) |
122:| `marker_token` — the input token itself | **0.550 (+51.6)** | 0.513 (+43.1) | 0.510 (+41.3) | 0.498 (+41.9) | 0.490 (+40.8) |
```

First number column is the third layer, and each cell is the accuracy with its
margin in standard deviations of that cell's own null. The pre-stated quantity
tops out at 0.293, about 1.60 standard deviations, and clears three nowhere. The
quantity the input guarantees reaches 0.550, about 51.6. Second run clears, first
does not: that is the middle limb, in numbers that already exist.

**This illustrates the limb; it does not execute the test.** These are two rows
lifted from a record, not the two runs part two asks for. They come from the very
history this entry was written from, so the limb has still never been seen to
fire on a design nobody had already diagnosed. And the findings file labels the
diagnostic these rows sit in as **not pre-stated** — it was written after the
sweep had already failed, which the file says makes it worth less than a
measurement designed in advance. Part two stays unrun, because running it means
running a whole probe pipeline twice against model checkpoints and nobody has
authorised that compute. The paragraph near the top of this file that says so
still stands.

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
that proposal (`RT-173`, the empty-cell finding), in the same review file and at
the same commit named under failure 1 above (`3bbfece`), against the same
proposal commit (`d8ceba9`).

**The same defect one step further.** That control carries a pre-stated check: an
untouched condition "should be near the one-in-eight guessing rate; if it is not,
the pairing is broken and nothing is read." With distinct values, a model that has
learned the task lands on the donor's answer only by erring onto exactly that
slot. The rule as written passes a model that has learned nothing and fails one
that has learned the task. It is pointed the wrong way round, and it sits inside
the list of things the design proposes to freeze.

**The test.** Two parts, and a third for any threshold attached to a cell.

*Part one: count what the generator actually puts in each pre-stated cell, at
rehearsal scale.* This is the part that generalises to a design other than the A3
grammar, and it is the part that catches an empty cell. Four things in the block
below belong to the design being checked and are meant to be replaced: the module
that is imported, the list of pre-stated cells, and the two small functions that
say what a trial is and which cell it lands in. Between them they are most of the
block; everything else stands.

```
$ python3 -c "
import sys; sys.path.insert(0, 'experiments/06-mvm-0a-constructed-self-index/src')
from collections import Counter
import curriculum_a3 as design          # the registered generator, not a stand-in

PRE_STATED_CELLS = ['donor dictates the same answer',
                    'donor dictates a different answer']

def trials(episodes):                   # one trial per (episode, item, donor)
    for ep in episodes:
        for item in ep.contested:
            v = ep.values[item]
            for donor in range(design.N_AGENTS):
                if donor != ep.own_slot:
                    yield v[donor], v[ep.own_slot]

def cell_of(trial):
    donor, recipient = trial
    return PRE_STATED_CELLS[0] if donor == recipient else PRE_STATED_CELLS[1]

counts = Counter(cell_of(t) for t in trials(design.generate_balanced(200, seed=0)))
for cell in PRE_STATED_CELLS:
    print(f'{cell}: {counts.get(cell, 0)} trials')
"
donor dictates the same answer: 0 trials
donor dictates a different answer: 1200 trials
```

**Zero is the finding.** Two hundred episodes of the registered grammar produce
twelve hundred donor-and-recipient pairs and not one of them lands in the first
pre-stated cell, because the grammar draws a distinct value per agent for each
contested item. The comparison that cell is half of can never be made. That is
failure 3, caught by a command, on the design that produced it.

*Until 2026-09-21 this command did not execute.* It imported `src.curriculum`,
and there is no `src` package — the generator modules sit in
`experiments/06-mvm-0a-constructed-self-index/src/` and import each other by bare
name, so the directory goes on the path rather than being treated as a package.
It called a function named `generate`, and the module has `generate_episode` and
`generate_balanced` and no `generate`. And it used `cell_of` and
`PRE_STATED_CELLS` without ever defining them, so a session holding a different
design could not have told what they were supposed to return. It raised
`ModuleNotFoundError` on the first line that did any work, and so had never been
seen to fail on anything.

*Part two: read the generator for the property that would empty a cell —
drawing without replacement, a shuffle that permutes rather than resamples, a
distinctness assertion, a deterministic rule that makes two conditions the same
condition.* Every file the generator is spread across, not one of them:

```
$ grep -rnE "\.sample\(|\.shuffle\(|\.permutation|permutations\(|set\(|distinct|unique|without replacement" experiments/06-mvm-0a-constructed-self-index/src/curriculum.py experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:51:# Marker pool: per-episode speaker labels drawn without replacement, so no
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:109:    markers = rng.sample(MARKERS, n_agents)
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:113:    items = rng.sample(ITEMS, min(len(ITEMS), n_turns))
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:118:        rng.shuffle(r)
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:218:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:311:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:17:  pairs. Within an item the four values are **distinct**, so an item's
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:59:At its own revision turn the model sees four distinct earlier values for
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:209:    markers = rng.sample(MARKERS, N_AGENTS)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:210:    contested = rng.sample(ITEMS, N_CONTESTED)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:212:    # distinct values per contested item, one per agent
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:215:        vs = rng.sample(SLOTS, N_AGENTS)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:219:    rng.shuffle(pairs)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:233:    revisers = rng.sample(range(N_AGENTS), K_REVISERS)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:236:    rng.shuffle(rev_turns)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:329:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:371:       agent revised, this alone identified the model uniquely in a
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:420:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:468:        # every contested item assigned by all agents, distinct values,
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:530:    # distinctness constraint still holds
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:539:            assert len(set(vs)) == N_AGENTS, "distinctness broken by enactment"
```

Line 215 of the A3 grammar is the one that empties the cell — four distinct
values drawn for four agents, without replacement — and line 539 asserts the
property survives rendering. Lines 17, 59, 212, 468 and 530 are the comments that
say so in English, which is often where this is easiest to see.

**What this part cannot see, plainly.** It is a text search, so it finds only
idioms somebody thought to put in the pattern. Until 2026-09-21 the pattern held
two of them, `rng.sample` and `assert len(set`, and looked in one file; it would
have missed a shuffle, a `set()`, a `numpy` permutation, sampling without
replacement written a third way, a constraint enforced by rejecting and redrawing
inside a loop, a distinctness rule that lives in the encoder rather than the
generator, or a generator in a file nobody listed. The pattern above is wider and
covers two files instead of one, and it still misses all of those things if a
design spells them differently. **Part one is the detector; part two only says
where to look once part one has found a cell at zero.** A clean part two is not
evidence that no cell is empty.

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
none is checked by accident and none is missed.* Two sweeps, because one of them
is a word list and a claim of measurement does not have to use a word:

```
$ grep -n -iE "verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result" <the text>.md
$ grep -n -E "[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}" <the text>.md
```

The second sweep catches a bare number offered as a result with no verb attached
to it, which no word list will ever find. Both sweeps are deliberately noisy —
`run` matches "running" and also "run" inside other words, `result` matches
"resulting", and the number sweep matches every figure in the document including
the ones that are not claims. Noise is the safe direction here: a session reads
the list and crosses off what is not a claim, which costs minutes, where a miss
costs whatever the unchecked claim costs.

**Why the word list is this wide.** Until 2026-09-21 it held seven words —
`verified`, `measured`, `calibrated`, `attacked`, `reproduc`, `confirmed`, `ran` —
and missed this document's own headline claim of measurement, the sentence near
the top reading "Every output printed below was produced by running the command
printed above it", because "running" contains none of them. It missed several
other ordinary ways of saying the same thing too. Six claims, the old list, the
widened list, and the number sweep:

```
$ python3 -c "
import re
OLD = r'verified|measured|calibrated|attacked|reproduc|confirmed|ran'
NEW = (r'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|'
       r'shows|showed|found|observed|recorded|returns|returned|yield|result')
NUM = r'[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}'
claims = [
    'Every output printed below was produced by running the command printed above it.',
    'We verify both ceilings against the attack sweep.',
    'Verification of the clause is filed with the run.',
    'The endpoint records were checked before the gate opened.',
    'The sweep shows no ownership signal at that position.',
    'Control battery ceiling: 0.3227.',
]
print('old   new   number   sentence')
for c in claims:
    print(f'{bool(re.search(OLD,c,re.I)):<5} {bool(re.search(NEW,c,re.I)):<5} '
          f'{bool(re.search(NUM,c)):<8} {c[:48]}')
"
old   new   number   sentence
0     1     0        Every output printed below was produced by runni
0     1     0        We verify both ceilings against the attack sweep
0     1     0        Verification of the clause is filed with the run
0     1     0        The endpoint records were checked before the gat
0     1     0        The sweep shows no ownership signal at that posi
0     0     1        Control battery ceiling: 0.3227.
```

The old list catches none of the six. The widened list catches five. The sixth is
a bare number with no verb anywhere near it, and only the number sweep finds it —
which is why part one is two commands and not one.

**What part one still cannot catch, plainly.** A claim of measurement written in
words nobody put in the pattern: "the two batteries came out the same", "this
held on all three checkpoints", "the gate opened". A claim carried by a table
with no sentence around it. A claim in a figure caption or a file name. And the
sweeps cannot tell a claim from a quotation of one, or from a sentence that says
a measurement was *not* made — every hit still has to be read. Part one narrows
the reading; it does not replace it.

*Part two: for each sentence the first part returns, name the file it cites and
run the one command that regenerates the number. Two worked examples, both from
the failures above:*

```
$ grep -c control experiments/06-mvm-0a-constructed-self-index/src/shortcut_sweep.py
0
```

*A practical warning about that one.* `grep -c` exits with status 1 when the
count is zero, because "nothing matched" is grep's failure status whether or not
you asked it to count. A session running this pass inside a script that stops on
the first failing command will stop right here, on the example whose answer is
the point. Run these by hand, or make the script tolerate it — appending
`|| true` to the line is enough — and never read a stopped script as a passed
test.

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

## 5. A command that creates something while documented as creating nothing

**What it was.** The staged plan for the rehearsal's one rented slice opened
with a step headed "prove the plan with no machine and no money". Its first
line ran a launcher with `--help`. The launcher had no `--help`. It had no
handling for command-line arguments at all — no `case "$1"`, no `getopts`,
nothing anywhere in the file. So the flag was not rejected and not reported.
It was **silently ignored**, and the script carried on exactly as it does when
run with no arguments, which is the real launch at its built-in defaults: the
30-million-parameter seed-0 recipe, 585,544,960 tokens, about ten hours and
about ten dollars, writing into the directory on the network volume where the
registered seed-0 artifacts already live.

**How it showed up.** By creating a rented machine, on 2026-09-21, in a
session whose authorisation was for a different and much smaller run. The
machine (`f1vtz2adz4dj8v`) was deleted about a minute later and cost about two
cents. The full account is the 2026-09-21 row of the compute ledger
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`) and the
annotation beneath it. It is filed in the red-team ledger as `RT-198`, the
silent-argument finding.

**The two cents are not the finding, and this is the part worth keeping.** The
command was run with its output piped through `head`, which closed the pipe
and killed the script before it reached the remote steps. That pipe is the
only reason anybody saw a machine being created. Run exactly as the plan wrote
it — with the output sent to `/dev/null`, which is what the plan said — there
is no early death and there is nothing on screen. The script runs to
completion in silence. **The difference between a two-cent finding and a
ten-dollar one with registered data underneath it was an incidental `head` in
a pipeline**, and John's ruling of 2026-09-22 draws the general lesson: a
mitigation that depends on the operator noticing is not a mitigation.

**Where the bad line came from**, because it will be written again. The plan
was generated by `stage_rented_slice.sh`, and that script **does** implement
`--help`, at its line 68. The session writing the plan generalised from the
script in its hands, which supports `--help`, to a script that does not. The
person writing the instructions is exactly the person who does not know, which
is why the guard has to live in the thing being invoked.

**What was recorded when it happened.** This block is the output of the
command as it behaved before the fix. **Do not run it.** It is printed because
a failure mode with no record of the failure is a citation, and because the
guard below cannot be shown to catch anything unless what it catches is
written down. The launcher no longer behaves this way; the registered launcher
`launch_a3.sh` still does, which is why the standing prohibition exists.

```
$ ./launch_a3_fetch_first.sh --help          # DO NOT RUN — this creates a machine
local pre-flight: module self-tests
  ok: curriculum_a3
  ok: encoding_a3
  ok: train_a3
  ok: frozen batteries present
creating SECURE pod (NVIDIA GeForce RTX 5090) for 30M/585544960 tok (out: a3_30m_seed0)
  run dir: /workspace/mvm-out (network volume — survives pod death)
{
  "costPerHr": 0.99,
  "desiredStatus": "RUNNING",
  "id": "f1vtz2adz4dj8v",
  ...
}
```

**The fix.** A guard at the top of each launcher, before any other work, which
refuses any argument, says what it got, names `DRYRUN=1` as the way to preview
a launch, and **exits explicitly** rather than relying on the shell to stop —
these files run under `set -uo pipefail` and deliberately not `set -e`, so a
guard that only complained would complain and launch anyway. The reasoning is
in `experiments/06-mvm-0a-constructed-self-index/argument-guard-method.md`,
committed before the code.

It is on the three unregistered launchers now. `launch_a3.sh` is registered
text and goes to Gate A as an amendment; until that clears, **no session
invokes a registered launcher with any argument**, and the test below asserts
it.

**The test.** One command. It creates nothing, spends nothing, and never runs
the registered launcher — running that with an argument is the very thing
being forbidden, so it is checked by reading its text instead.

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
```

```
RT-198 — launchers must refuse arguments rather than launch

unregistered launchers: an argument is refused
  [ ok ] launch_a3_fetch_first.sh refuses an argument (exit 2)
  [ ok ] launch_a3_fetch_first.sh says why it refused
  [ ok ] launch_a3_fetch_first.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_a3_fetch_first.sh guard (line 104) precedes any vendor command (line 227)
  [ ok ] launch_ctl_pilot.sh refuses an argument (exit 2)
  [ ok ] launch_ctl_pilot.sh says why it refused
  [ ok ] launch_ctl_pilot.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_ctl_pilot.sh guard (line 87) precedes any vendor command (line 201)
  [ ok ] launch_pilot_a1.sh refuses an argument (exit 2)
  [ ok ] launch_pilot_a1.sh says why it refused
  [ ok ] launch_pilot_a1.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_pilot_a1.sh guard (line 42) precedes any vendor command (line 99)

unregistered launchers: the guard did not break the real path
  [ ok ] launch_a3_fetch_first.sh dry run still exits 0
  [ ok ] launch_a3_fetch_first.sh dry run still creates nothing
  [ ok ] launch_ctl_pilot.sh dry run still exits 0
  [ ok ] launch_ctl_pilot.sh dry run still creates nothing
  [ ok ] launch_pilot_a1.sh dry run still exits 0
  [ ok ] launch_pilot_a1.sh dry run still creates nothing

registered launcher: read, never run
  [ ok ] launch_a3.sh does NOT carry the guard, which is expected before Gate A

  ***********************************************************************
  STANDING PROHIBITION, in force until the Gate A amendment clears:
  launch_a3.sh is REGISTERED TEXT and still has NO argument handling.
  An argument passed to it is SILENTLY IGNORED and it proceeds to a REAL
  LAUNCH at its defaults -- about ten hours and about ten dollars,
  writing into the registered seed-0 directory on the network volume.

      NO SESSION INVOKES A REGISTERED LAUNCHER WITH ANY ARGUMENT.

  To preview it without creating anything:  DRYRUN=1 ./launch_a3.sh
  Ruled by John 2026-09-22. Method: ../argument-guard-method.md [RT-198]
  ***********************************************************************


negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

**What the output has to show**, for any design this is pointed at: every
launcher that can create a rented machine refuses an argument with exit status
2; each guard sits before that file's first vendor command; every dry run
still exits 0 and still reports creating nothing; and the negative control
rejects an unguarded stand-in. **That last one is what makes the rest worth
reading.** A test that can only pass proves nothing, so the check builds a
stand-in with the pre-2026-09-22 shape — a script that ignores its arguments
and carries on — and requires the checks to reject it. If the control ever
reports the unguarded stand-in passing, the harness has stopped measuring what
it claims to.

**The line that is expected to change.** While `launch_a3.sh` remains
registered and unguarded, the check prints the standing prohibition and still
exits 0, because an unguarded registered launcher is the expected state before
Gate A rather than a failure. When the amendment lands, that file moves into
the list whose refusal is exercised, and the prohibition block goes away. A
session reading this entry after that point should expect the output above to
differ in exactly that respect and in no other.

---

## 6. A remote step tested only against stand-ins

*Added 2026-09-25 (Pacific). John ruled the addition on 2026-09-25 ("agreed
on all", on section 7 of `docs/2026-09-25-rented-slice-findings.md`, whose
item 3 proposed it). The session that wrote this entry also wrote the fix it
describes; under the pairing rule a different session checks both. The
opening section of this file still counts five failures and fifteen printed
blocks: it predates this entry and is left as written.*

**What it was.** A command sent to a rented machine over `ssh` whose every
test replaced `ssh` with a stand-in. The command was the one that starts the
machine's own shutdown watcher, line 467 of
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`
at commit `4d98cfc`, in the form `cd /root/mvm/src && nohup sh reap_agent.sh
… >> …/reaper.log 2>&1 < /dev/null &`. In that form the `&` sends the whole
`cd && nohup` chain to the background as one subshell. The redirections
apply to `nohup` only, so the subshell keeps the connection's output open
until the watcher exits, and `ssh` waits for it. The watcher runs until its
+24-hour deadline. Every test of the launcher used a stand-in `ssh` that
exits at once (`reap_handshake_selftest.sh` sets `SSH="$BIN/fakessh"`), and a
stand-in that exits at once returns at once **whatever the remote command
does**. So no test could have seen the hang. The same file had already met
the same hang, on the training start, in August 2026: its comment says "this
ssh can HANG after the remote nohup succeeds", and that call had been capped
at 60 seconds ever since. The watcher start, added on 2026-09-21, was not.

**How it showed up.** On the first real `ssh` that line ever met, on
2026-09-25, during the rented slice. The launcher hung for about 30 minutes
after the watcher had started, never reaching the timing step, the training
or the laptop watchdog. A session watching the log stopped it and deleted
the machine; it cost $0.4974, and neither measurement was taken (the
2026-09-25 row of `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`,
and `docs/2026-09-25-rented-slice-findings.md` sections 4 and 5).
**Unattended, nothing on the laptop would have deleted the machine** — the
laptop watchdog is spawned after training starts — so it would have billed
until its own +24-hour deadline, about $24 against a hard cap of $2.00
(findings section 5, ARGUED there from the watcher's code).

**Why this is a species and not an instance of failure 5.** Failure 5 is a
command that does something its documentation says it does not. This one
does exactly what it says; what was wrong was the evidence that it worked.
A stand-in is built to answer the way the far end is *expected* to answer,
so a test against it can only confirm the expectation. The more a remote
step's behaviour depends on the far end — how a shell backgrounds a job,
what a vendor's tool accepts, what a machine carries — the less a stand-in
test says about it. The shutdown handshake itself was, until 2026-09-25,
"verified against local stand-ins only" in its own author's words
(`experiments/rehearsal-successor-measure/src/stage_rented_slice.sh`,
header), and the slice existed to close exactly that gap.

**The fix.** Ruled by John 2026-09-25. The watcher start now runs only
`nohup` in the background, with all its output redirected (`cd … || exit 1;
nohup … &`), so nothing holds the connection; and the `ssh` that sends it is
cut off at 60 seconds whatever happens, the same cap the training start
has. The laptop's machine deadline (`src/machine_deadline.sh`) bounds the
money if some other remote step hangs.

**The reproduction, with nothing rented.** The findings reproduced the hang
on the laptop by putting `| cat` where `ssh` would be: like `ssh`, `cat`
waits until everything on the far side has closed its output. Re-run on
2026-09-25 (Pacific) by the session that wrote this entry, first the
findings' own two commands, then the launcher's real old and new watcher
forms with the watcher replaced by `sleep 8`:

```
== the findings' reproduction, rerun 2026-09-26T00:49:55Z (2026-09-25 Pacific)
form as launched (cd && nohup ... &): returned after 8s
control (cd ; nohup ... &): returned after 0s
== the launcher's watcher-start form, old (line 467 at 4d98cfc) and new, with the watcher replaced by sleep 8
OLD  cd … && nohup … &        : returned after 8s
NEW  cd … || exit 1; nohup … & : returned after 0s
(a background sleep 8 is still running after the new form returned: it was started, not skipped)
```

The script that printed this is filed as
`experiments/rehearsal-successor-measure/out/launcher-fix-2026-09-25/hang-reproduction.sh`,
beside its output.

**The test.** One command. It rents nothing and contacts no vendor. For each
command a launcher sends over `ssh` that starts something in the background
(it contains `nohup`), it rewrites the command to run on this laptop, with
the backgrounded program replaced by a stand-in that leaves a marker file and
holds for 8 seconds, runs it through `bash -c '…' | cat`, and times it. A
start that returns in under 2 seconds passes. One that holds the connection
passes only if the launcher cuts that `ssh` off with a time cap. One that
holds and is not capped fails. A start whose stand-in never ran fails too,
because a command that returns at once by doing nothing has not been shown
to return at once. Then a negative control, the pre-fix form, must be
rejected.

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
```

```
remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds 8s)

launch_a3_fetch_first.sh
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)

negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang

all checks pass. Nothing was rented and nothing was spent.
```

**It fails on the design that produced the finding.** Pointed at the
launcher as it was at `4d98cfc`, the commit the slice ran:

```
$ git show 4d98cfc:experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh > "$TMPDIR/launcher-4d98cfc.sh"
$ LAUNCHER="$TMPDIR/launcher-4d98cfc.sh" experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
```

```
remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds 8s)

launcher-4d98cfc.sh
  [FAIL] launcher-4d98cfc.sh line 467: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] launcher-4d98cfc.sh line 547: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 552)

negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.2s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang

1 problem(s). Nothing was rented and nothing was spent.
```

Both outputs were produced on 2026-09-25 (Pacific) by the session that wrote
this entry, and no other session has re-run them. **The timings are wall
clock**, so a re-run will differ from the text above by a tenth of a second
here and there; compare the verdicts and the whole seconds, not the bytes.
The line numbers are those of the file at the commit this entry landed in,
and move when the launcher is edited.

**What the output has to show**, for any design this is pointed at: every
background start a launcher sends over `ssh` either returns at once or is
cut off by a time cap in the launcher; no start is reported as never having
run; and the negative control is rejected. **The control is what makes the
rest worth reading.** If it is ever accepted, the check has stopped
measuring what it claims to.

**What this test does not cover, stated so it is not read as covering it
(ARGUED).** It catches one way a remote step can differ from its stand-in:
a background job holding the connection. The species is wider. A vendor
tool on the machine that takes different arguments from the laptop's (the
2026-09-17 finding recorded at the verb-first check in the launcher), a
credential the machine does not carry (2026-09-16), a path that exists only
on the laptop — none of these is exercised here, and none can be by any
check that does not reach the real far end or a faithful copy of it. The
general discipline, for which no single command exists: **before a remote
step is counted as tested, say what stood in for the far end, and what that
stand-in cannot do that the far end can.** A test run only against a
stand-in is evidence about the stand-in.

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
