# Check before merge — the seven corrections to the measurement rehearsal's findings

*2026-09-21 (Pacific). A checking session that did not write the work under
check, and did not write the check that specified the corrections either.
Target: the branch `worktree-agent-ac1aafaeec7772df4` at the commit `ed22fc8`,
titled "Correct seven sentences in the rehearsal findings; no result changes".
Two files changed: the findings document
(`docs/2026-09-21-successor-measure-rehearsal.md`) and section 11, the
departures appendix, of the method document
(`docs/successor-measure-rehearsal-method-2026-09-21.md`). The check that
specified the corrections is filed on the branch
`worktree-agent-a2419cc1507df37a1` at the commit `3fcff5a`.*

*Read only. Nothing was fixed, no training was launched, no machine was rented,
no money was spent, nothing was pushed to the shared main line and no pull
request was opened. Every figure below was re-derived from the committed output
files in `experiments/rehearsal-successor-measure/out/` by this session, not
taken from the correcting session's word that it had checked them.*

*Written under the workspace plain-language rule
(`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30).*

---

## Verdict: merge. No must-fix finding.

Every one of the seven corrections is right, and each corrected figure is in
the committed record where the correcting session says it is. The withdrawn
rank curve really is absent from the record, and the curve that replaces it is
exact at the site set named. The adjudication of the first stop condition is
sound on both of its measurements and its reasoning holds; the case against it
is stated in its strongest form rather than knocked down. The one sentence
narrowed beyond the seven was narrowed because the record contradicted it as
written, not to soften it. Nothing was introduced that is not in an output
file: every one of the sixty-eight decimal figures the change adds traces to a
committed file or to the arithmetic in `measure.py`.

Three things are worth noting and can all follow afterwards. None of them
changes a measurement or a decision. This is the last round before merge and
this file does not invent a reason to run another one.

---

## 1. The rank curve — both halves confirmed

The findings used to print the transplant curve on the separable arm as 0.170
at rank 1, 0.365 at rank 2 and 0.805 at rank 4. The correcting session withdrew
those three figures and replaced them with 0.153, 0.355, 0.832 and 1.000.

**The old figures are absent.** I searched every cell of the whole nomination
record — nine trained models (three architectures at three seeds), each with
810 rows, so 7,290 rows in all. No row's transplant accuracy comes within half
a thousandth of 0.170, of 0.365 or of 0.805. I then built every rank curve the
record can produce: every architecture, every seed, all three readings of the
read's label, all forty-five site sets, and three ways of combining seeds
(seed by seed, averaged across the three seeds, and best-of across site sets).
The closest curve taken one seed at a time misses the three old figures by
**0.0550 in total**, which is the 0.055 the correcting session reported, to the
digit. The closest curve under the across-seed average misses by 0.0478. Either
way the old curve is not in the record and nothing reproduces it.

**The new figures are right at the site set named.** The nomination picks the
first layer at the position where the action is taken, on all three seeds, and
picks the which-marker-word reading of the label each time. At that site set,
with that label, on the separable arm:

| rank cap | seed 0 | seed 1 | seed 2 | average |
|---|---|---|---|---|
| 1 | 0.1517 | 0.1417 | 0.1667 | **0.1533** |
| 2 | 0.3350 | 0.3950 | 0.3350 | **0.3550** |
| 4 | 0.7783 | 0.8467 | 0.8717 | **0.8322** |
| 8 | 1.0000 | 1.0000 | 1.0000 | **1.0000** |

Every per-seed figure printed in the findings matches, and the averages round
to the 0.153, 0.355, 0.832 and 1.000 the findings print. The claim that the
reading stays at exactly 1.0000 at rank 8 and above also holds: rank 16 and
rank 24 are 1.0000 on every seed.

**The withdrawal is recorded, not painted over.** The corrected paragraph
carries an italic note naming the three withdrawn figures, saying they are in
no committed output file, and saying they are withdrawn. A reader who saw the
old draft can tell what happened to it. That is the right way round.

## 2. The two transplant rows, per seed

The label table used to print the two failing readings as a flat 0.0000. Taking
the best transplant over every site set and every rank cap, on the separable
arm, out of the nomination record:

| reading of the label | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| the agent's slot | 0.0117 | 0.0000 | 0.0000 |
| the marker's rank | 0.0050 | 0.0183 | 0.0117 |
| which marker word | 1.0000 | 1.0000 | 1.0000 |

Exactly what the corrected table prints. The accompanying claim that the
marker-rank row is not 0.0000 on any seed is true, and the claim that neither
failing row is 0.0000 on every seed is true. The fit figures beside them are
right too: the agent's slot fits at 0.2556 on all three seeds (printed 0.256),
the marker's rank at 0.7056, 0.6944 and 0.7000 (printed 0.706, 0.694, 0.700),
and which-marker-word at 1.000 throughout.

## 3. The degree range of 0.9817 to 1.0000 — reproduced through the measure itself

This is the sentence the registration turns on, so I did not take it on trust
and did not recompute it by hand. I imported the rehearsal's own measure code
(`experiments/rehearsal-successor-measure/src/measure.py`), fed it each label's
best configuration out of the nomination record, at the rehearsal's working
floor of 0.30, and printed what came back:

| seed | reading of the label | whole-state | ownership-only | registered form | floor-corrected form |
|---|---|---|---|---|---|
| 0 | the agent's slot | 1.0000 | 0.0117 | **0.9883** | 0.9883 |
| 0 | the marker's rank | 1.0000 | 0.0050 | **0.9950** | 0.9950 |
| 0 | which marker word | 1.0000 | 1.0000 | 0.0000 | 0.0000 |
| 1 | the agent's slot | 1.0000 | 0.0000 | **1.0000** | 1.0000 |
| 1 | the marker's rank | 1.0000 | 0.0183 | **0.9817** | 0.9817 |
| 1 | which marker word | 1.0000 | 1.0000 | 0.0000 | 0.0000 |
| 2 | the agent's slot | 1.0000 | 0.0000 | **1.0000** | 1.0000 |
| 2 | the marker's rank | 1.0000 | 0.0117 | **0.9883** | 0.9883 |
| 2 | which marker word | 1.0000 | 1.0000 | 0.0000 | 0.0000 |

The nine-row table in the findings is reproduced cell for cell. The range over
the two failing readings is **0.9817 to 1.0000**, which the findings round to
"0.982 to 1.000". The supporting claims hold as well: the whole-state accuracy
is 1.0000 and the no-transplant rate is 0.0000 on all three seeds for this arm,
which is why both candidate forms of the reading agree to the last digit, as
the findings say they do.

So the sentence stands as written: under the two failing readings of one
unwritten word, the instrument reports a degree of 0.982 to 1.000 for an arm
whose degree is 0.0000 by construction. It is a wrong answer of the largest
size the scale allows, on the one arm where the right answer is known in
advance.

## 4. Five of nine, the nine-row table, and the fail that was not reported

Counting the span each form of the reading covers across the four attenuations,
arm by arm and seed by seed, out of the attenuated-transplant record:

| arm and seed | the reading as registered | the floor-corrected reading | flatter |
|---|---|---|---|
| entangled, seed 0 | 0.0405 | 0.0221 | floor-corrected |
| entangled, seed 1 | 0.3424 | 0.0164 | floor-corrected |
| entangled, seed 2 | 0.0087 | 0.0023 | floor-corrected |
| free, seed 0 | 0.3291 | 0.0085 | floor-corrected |
| free, seed 1 | 0.0680 | 0.0710 | **the registered one** |
| free, seed 2 | 0.5169 | 0.0732 | floor-corrected |
| separable, seed 0 | 0.0067 | 0.0067 | dead heat |
| separable, seed 1 | 0.0631 | 0.0631 | dead heat |
| separable, seed 2 | 0.0066 | 0.0066 | dead heat |

Five favour the correction, three are dead heats, one favours the registered
form. **Five of nine, not six.** I also recomputed each span from the four
underlying rows rather than reading the stored span, and got the same figures.
The dead heats are dead heats for the reason given: on the separable arm the
no-transplant rate is exactly zero, so the two forms are the same arithmetic
and cannot disagree.

The unreported fail is real. The denominator addendum's check D-2 — the one
that asks the same question on real forward passes — has a fail line reading
exactly "the registered form is the flatter one". On the free arm at seed 1 the
registered form is the flatter one, 0.0680 against 0.0710. The findings now
report it as a fail. The two largest gaps in the table are also correctly
named: the free arm at seed 2 (a gap of 0.4437) and the entangled arm at seed 1
(0.3260), both in the correction's favour.

## 5. The floor-rule misses — settling which count is right

The review's formula against what was actually measured, out of the
floor record:

| arm and seed | measured | predicted | miss |
|---|---|---|---|
| entangled, seed 0 | 0.0600 | 0.0598 | 0.0002 |
| entangled, seed 1 | 0.0663 | 0.0620 | 0.0042 |
| entangled, seed 2 | 0.0638 | 0.0605 | 0.0033 |
| free, seed 0 | 0.0600 | 0.0624 | 0.0024 |
| free, seed 1 | 0.0550 | 0.0634 | **0.0084** |
| free, seed 2 | 0.0762 | 0.0587 | **0.0175** |
| separable, all three seeds | 0.0000 | 0.0000 | exact |

The worst miss is **0.0175**, the next is **0.0084**, and both figures in the
findings are right. The worst miss is 0.0175 against a predicted 0.0587, which
is 30 per cent of the value being predicted — the findings say "about a third",
which is fair.

**On the disagreement the brief asked me to settle: the correcting session is
right and the previous check's arithmetic is wrong.** The correcting session
wrote seven within about four thousandths and two outside. Seven is the count:
three exact zeros on the separable arm, plus 0.0002, 0.0024, 0.0033 and 0.0042.
Two are outside: 0.0084 and 0.0175. Seven plus two is nine, which is how many
there are. The previous check wrote six plus two, which is eight and leaves one
model unaccounted for. Six is reachable only by reading "four thousandths" as a
hard cut that excludes the 0.0042 — but that reading gives six plus **three**,
not six plus two, so the previous check's pairing does not work on either
reading. The findings hedge with "about four thousandths or better" and name
both outliers by value immediately afterwards, so the description is accurate
as written.

## 6. The pre-stated family — 180, and the rank cap that vanished

Confirmed in the code's history, not just in the record. The first commit of
the rehearsal code (`5fa85e2`), made before any result ran, carries the line
`RANK_CAPS = [1, 2, 3, 4, 8]` — five rank caps, and nine layer sets by five
position sets by five rank caps is the 225 the plan fixed. The final code
carries `RANK_CAPS = [1, 2, 4, 8, 16, 24]` and flags a row as pre-stated only
when the label is the agent's slot **and** the rank cap is one of one, two,
four or eight. The cap of three is gone.

Counting the flagged rows in the nomination record: **exactly 180 per model**,
on all nine of them, over rank caps 1, 2, 4 and 8 and the agent's-slot label
only. Nine by five by four is 180. So the corrected figure is right and the
departure is real.

The supporting claim holds too: across the separable arm's whole pre-stated
family, all 540 flagged rows over the three seeds, the transplant reading runs
from 0.0000 to 0.0117 — the range the findings give — so there is no mechanism
by which a cap of three alone would have found the answer. The departure is
recorded in the method document's appendix in the same form as the others,
which is the right place for it.

## 7. The two coverage tables — eleven items and nine numbers

Both corrected counts are right against the proposal on the main line: its
section 10 lists eleven rehearsal items, and its section 9 lists nine numbers.
The claim about the timing is right to the second and I checked it in the
commit history rather than accepting it. The rehearsal's method document was
committed at 20:09:55 on 2026-09-21; the proposal commit that added the
eleventh rehearsal item and the ninth number landed at 20:09:59 — **four
seconds later**, on a branch this work was not on. The added row's staged cost
matches the staging note exactly: an estimate of about $0.75 to $1.00 against a
hard cap of $2.00, inside the $3 the proposal budgets for that item.

## 8. The adjudication of the first stop condition — sound, and fairly argued

**Both measurements check out.** From the learn-both record: the separable arm
reaches 1.0000 on the own-directed condition and 1.0000 on the named-other one,
on all three seeds. From the same file's solver section: the name-only solver —
which reads nothing but the name token — reaches 1.0000 on the named-other
condition and 0.2380 on the own-directed one. Both are exactly as the findings
report them, and the findings correctly describe the name-only solver as
something the rehearsal built and scored rather than something it trained,
which is what the record says it is.

**The conclusion is right.** The first stop condition's own words are that the
grammar "is not learnable at tiny scale even in principle" and that "nothing
trains". Both are contradicted directly. Something trains, at this size and on
this grammar, and it trains to the top of the scale on both conditions. And the
named-other condition — the half that failed — is solvable at this scale by a
strategy the rehearsal scored at a perfect 1.0000. A stop condition keyed to
"nothing trains" cannot fire on a record in which a model scores perfectly on
both conditions. What actually failed is narrower and the findings say so: on
the two architectures that are not built with the ownership answer in a slot of
its own, the named-other condition does not clear its bar on a majority of
seeds, and doubling the training budget does not fix it.

**The counter-case is stated fairly, not strawmanned.** The strongest argument
for the other reading is that the stop condition's trigger, read literally, is
"the rehearsal fails item R-1", and the findings do mark that item a fail. The
adjudication states exactly that, in those terms, and adds the second prong
itself — that the eighth stop condition, which forbids stepping over anything,
can be read as pushing the same way. It does not soften either. I could not
construct a stronger version of the objection than the one written down.

The rebuttal holds. The eighth stop condition is about a check that **cannot be
evaluated** — missing data, a measurement never taken — and this one was
evaluated with every number on the record, so it is not the case that condition
describes. And the first condition's parenthesis is not decoration: it names the
state of the world the condition is about, and that state is false.

Two things make this the right way to handle it rather than a dodge. The item
itself is **left marked FAIL** — the adjudication does not quietly downgrade the
finding to escape the stop. And the adjudication says in terms that it is the
rehearsal's reading and not a ruling, that it is John's to overturn, and what
the accounting would be if he overturned it. That is the correct posture for a
session adjudicating a line that halts spend.

## 9. The sentence narrowed beyond the seven — forced, not softened

The sentence used to read "at this size, on this grammar, the
named-other-directed revision is close to unlearnable". As a claim about this
size and this grammar without qualification, it is **false on the record**: at
the same size, on the same grammar, the separable arm learns that condition to
1.0000 on all three seeds. It is not a matter of emphasis; the record
contradicts the sentence as written, and it would have contradicted the
adjudication printed three lines below it.

The narrowing is therefore forced. Two further things say it is not a
softening. Nothing the sentence was doing was removed: "more steps do not fix
it" survives, and so does the whole consequence — that the risk is real, is
reproducible on a laptop for nothing, and is worth attacking in the design
before about $110 of registered runs are committed to it. And the exception is
put in the reader's way rather than buried: the paragraph adds a parenthesis
saying the qualifier matters and naming the separable arm's 1.0000. A softening
would have dropped the consequence or hidden the exception. This does neither.

## 10. Did the corrections introduce anything new? No

I pulled every decimal figure the change adds — sixty-eight distinct values —
and traced each one. All of them land in a committed output file, in the
arithmetic of `measure.py` applied to committed values, in the staging note, or
in the code's own commit history. The three withdrawn figures (0.170, 0.365,
0.805) appear only inside the note that withdraws them. There is no figure in
the change that the record does not carry.

---

## Can follow afterwards

**a. "The eight numbers above" now sits under a table of nine.** Section 12's
first item asks for John's rulings on "the eight numbers above", and the table
immediately above it gained a ninth row in this very change. The count is
defensible — eight of the nine need a ruling from John, and the ninth needs the
rented slice, which is the next item in the same list — but a reader who counts
the table gets nine and reads the eight as stale. Worth one clause
disambiguating it ("the eight of those nine that need a ruling"), especially as
the change's own commit message says the word "eight" was corrected, which it
was in one place and not here. No figure or decision moves either way.

**b. The rehearsal code still says 225.** The documents are now right, but
`rehearse.py` still carries `PRE_STATED_FAMILY_SIZE = 9 * 5 * 5` with a comment
saying "five rank caps", and its progress line prints that number while the
file it writes contains 180 flagged rows. Nothing committed under `out/` repeats
the 225, so the record itself is clean, and correcting the documents rather than
re-running the code was the right call. But anyone who reads the code next will
meet the stale constant before they meet the appendix that explains it. A
one-line comment pointing at the departure would close it.

**c. The failing check is applied per model and seed, where the addendum wrote
it per arm.** The denominator addendum's check D-2 states its outcomes per arm;
the findings apply it per arm and per seed and report a fail on one seed of one
arm. That is the stricter reading and it errs toward disclosure, so it is not a
defect — but the findings describe the addendum's cell as "written per arm" and
then apply it per seed in the next sentence, which a careful reader will notice.
One clause saying the stricter reading was chosen deliberately would settle it.

---

## What this check did not do

It did not re-check the rehearsal as a whole — a previous check covered that,
and this one was scoped to the seven corrections, the adjudication and the one
narrowed sentence. It did not run the staged slice, rent anything, retrain
anything or spend any money; every figure above came from files already in the
repository and from about a second of arithmetic. It did not fix anything, and
it did not push, merge or open a pull request.

**Merge.**
