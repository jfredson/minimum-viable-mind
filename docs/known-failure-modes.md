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

**What this list has been shown to be, and what it has not.** As a description of
what has gone wrong here, it is accurate.

**Which blocks below have been run, and which have not.** Twelve blocks are
printed below. Ten carry a command and the output that running it produced, and
all ten have been re-run by a session other than the one that wrote them and
compared against the printed text with `cmp`, which names the first byte at which
two files differ; nothing differed. The eight the list carried before the repair
described below had already been checked the same way once, with `diff`. The
remaining two blocks carry placeholders in angle brackets and no output. One of
them is failure 4's first part, written as a template because it is pointed at
whatever document is under review; the word lists inside it are exercised on six
worked claims in the block below it, and that block was run and its output
printed. **The other is failure 2's second part, and it has never been run at
all.** Running it means running a whole probe pipeline twice against model
checkpoints, which costs compute that nobody has authorised. Its middle limb —
the second run clears the bar and the first does not — is argued from numbers
already sitting in the position sweep's findings file, which failure 2 names
below, and not from running the test. It has not been seen to fail on anything.

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

**The test.** Two parts, and the first one is the one that catches this failure.

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
grammar, and it is the part that catches an empty cell. Three lines belong to the
design being checked and are meant to be replaced: the module that is imported,
the list of pre-stated cells, and the two small functions that say what a trial
is and which cell it lands in. Everything else stands.

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
