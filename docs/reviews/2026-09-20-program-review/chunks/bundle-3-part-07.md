and been read as answering it.*

| id | finding | label | severity |
|---|---|---|---|
| RT-62 | The matched comparison the design was built around is missing, and "bought nothing" is false | MEASURED | **fatal** |
| RT-63 | "0.42 standard deviations" is the spread of one draw, not the uncertainty of the mean being scored | MEASURED | worth-noting |
| RT-64 | One training seed; the design only ever had power against a large effect | ARGUED | serious |
| RT-65 | The control is flat at the end and the budget was not short-changed — checked, clean | MEASURED | clean |
| RT-66 | The one trajectory reading in the review set also runs the intervention's way | MEASURED | worth-noting |

### RT-62 — the comparison the pre-statement designed is not in the findings

**MEASURED. Fatal — one sentence in the interpretation is false as
written, and the number that makes it false is absent.**

The pre-statement is explicit about why this run used seed 0:

> chosen so the comparison against the existing pilot is matched on
> initialization and data order and **the loss is the only thing that
> differs**

Its counterpart therefore exists and is in the review set. The A3 pilot at
seed 0, with none of this supervision, reads the control battery at
**0.2877** (spread 0.0302). This run, same seed, same initialization, same
data order, reads **0.3125** (spread 0.0240).

**The matched move is +0.0248.** Treating the two six-draw means as
independent, the standard error of that difference — the amount it would
wobble if you re-measured — is 0.0157, so the move is about **1.6 standard
errors**: it does not reach conventional significance, and it is not
nothing either.

The findings file does not report this comparison at all. It sets 0.3125
beside all three checkpoints — 0.2877, 0.3057, 0.3195 — which are three
*different training seeds*, and so re-imports exactly the between-seed
variation the matched design existed to remove. Against the mean of those
three (0.3043) the move is +0.0082, about half a training-seed standard
deviation, and that is where the sentence "the intervention moved nothing
distinguishable from seed variation" comes from.

That sentence is defensible. **The next one is not:**

> quadrupling the control's per-row gradient weight bought nothing

It bought about **+0.025, give or take 0.016**, on the comparison the
pre-statement was written around. "Not distinguishable from nothing" and
"nothing" are different claims, and only the first is true. A four-times
dose that moves a saturated battery a quarter of the way to its next
boundary, on one seed, is a weak positive that failed to reach
significance — not a zero.

**Both comparisons are legitimate. Only one was designed in advance, and
it is the one that is missing.**

There is also a sharper version available for nothing. Both checkpoints
were read on six evaluation draws. If they are the same six draws — this
run's are numbered 771000 through 771185, and the three-seed write-up says
its six are the first six of the twelve from the noise measurement — then
the difference can be taken **within each draw**, on the same held-out
items, which removes the item-set variation from both sides and would
tighten the estimate considerably. I could not do it: the earlier pilot's
per-draw control scores are not in the review set, only its summary. It
costs nothing and should be done before the step 4 proposal cites this
run.

**What survives:** the DID NOT LEARN verdict. 0.3125 is below 0.3227 on
the mean, it is nowhere near 0.60, and RT-61 shows the battery has
saturated the name-blind procedure. **What must not survive:** the words
"bought nothing", and the presentation of an unmatched three-seed
comparison in place of the matched one the pre-statement promised.

### RT-63 — the wrong spread against the boundary

**MEASURED. Worth-noting, and it cuts in the findings' own disfavour.**

The distance table reports the control as "0.42 standard deviations" below
0.3227 and "11.98" below 0.60, using 0.0240 — the spread of a *single*
evaluation draw. But the cell is scored on the **mean of six**, and the
uncertainty of a mean of six is the spread divided by the square root of
six: 0.0098. On that footing the control sits **1.04 standard errors**
below 0.3227, not 0.42.

The table's heading, "in standard deviations", is literally accurate. It
is simply not the uncertainty of the quantity the cell is read on.

The consequence runs against the findings' own hedge. They warn that "a
rerun could formally land in PARTIAL". How likely depends on what a rerun
means:

- a fresh single evaluation draw lands above 0.3227 about **34%** of the
  time;
- a fresh six-draw estimate, which is what the cell is actually read on,
  does so about **15%** of the time.

So the finding is better supported than its own caveat says. The caveat
should stay — it is the right instinct — but with the right number
attached.

### RT-64 — one training seed, and only a large effect was ever detectable

**ARGUED. Serious.**

The six seeds are **evaluation** seeds. They redraw the held-out set from
one checkpoint. They say nothing whatever about what a second *training*
seed would have done, and the three flag-off checkpoints put training-seed
spread at about 0.016 — comparable to the evaluation spread, and larger
than the matched move in RT-62.

A single training seed at that spread cannot separate "supervision does
nothing" from "supervision buys +0.02 to +0.03", which is roughly what the
matched comparison shows. The pre-statement implicitly accepted this by
setting LEARNED at 0.60: only a large effect was ever going to be
detectable, and a large effect is genuinely excluded.

The problem is that the conclusion now being drawn — "supervision is not
the binding constraint" — is a claim about small and moderate effects too,
and the run has no power against those. The design answers "does
supervision carry this battery?" It does not answer "does supervision do
anything?", and the findings file's own framing slides between the two.

### RT-65 — the run did answer the question it was bought for

**MEASURED. Clean, and recorded as clean, because it closes two escapes.**

Both secondary cells pass, as the findings say: the primary battery still
learns (0.5727 against the 0.50 the cell asks) and still collapses under
its own lesion (to 0.1663, a corrected drop of 1.448, in the same band as
the three earlier checkpoints). So this is not a failed intervention.

Two further checks, which the findings do not make and which matter more
than they look:

- **The control is flat at the end.** The partial checkpoint at step
  51,500 reads 0.3158; the full checkpoint at 55,116 reads 0.3125. That is
  a move of **−0.0033 over the last 3,616 steps**. This is not a battery
  still climbing when the budget ran out, which is the most obvious way a
  null could be an artefact of stopping early.
- **The budget was not short-changed by the flag.** The ledger records
  0.6508 seconds per step against the earlier pilot's 0.6501 — within
  about 0.7% — and the run finished on the identical 55,116 steps and
  585,552,384 tokens, confirmed by the completion sentinel and matching
  the earlier pilot and seeds 1 and 2. The padding worry the pre-statement
  flagged was real and negligible.

Minor, and recorded because the packet asks about every quantity the
pre-statement names: the pre-statement and the launcher both state the
budget as 585,544,960 tokens; the run stopped at 585,552,384, the first
step-multiple at or above it. The findings file quotes the second. Both are
right; they are different quantities and nobody says so.

### RT-66 — the early trajectory also runs the intervention's way

**MEASURED. Worth-noting.**

The one trajectory reading inside the review set is in the ledger, at steps
500 and 1,000: this run reads 0.28 and 0.27 on the control battery against
the earlier pilot's 0.24 and 0.18 at the same steps on the same seed.

Nothing should be read from 1.8% of training at 100 episodes, and the
ledger says so at length and correctly. It is recorded here only because it
is the second place where the matched comparison favours the intervention
slightly, and the findings file quotes neither. Two weak indications in the
same direction are still weak — but a findings file that reports neither,
and then says the intervention "bought nothing", has selected against its
own result.

---

## 4. Over-reading

*What "supervision is not the binding constraint" will be read as
claiming, beyond what one seed at one weight setting measured.*

| id | finding | label | severity |
|---|---|---|---|
| RT-67 | The sentence will be read as ruling out supervision; the run tested one dose of one form of it | ARGUED | serious |
| RT-68 | Step 4 should narrow — but for a reason the findings do not give, and the stated reason undercuts the option it points to | ARGUED | serious |
| RT-69 | Any step 4 option that keeps this battery inherits the ceiling precondition John already set | MEASURED | worth-noting |

### RT-67 — what the sentence will be taken to mean

**ARGUED. Serious.**

What was measured: on one training seed, at four times the per-row weight
and two thirds of the query gradient, with the whole query side
simultaneously tripled against the action term, the control battery moved
+0.0248 against its matched counterpart and stayed on the shoulder of a
name-blind solver.

What "supervision is not the binding constraint" will be taken to mean, in
the current-state document, in the 4 October control-battery proposal and
in the paper: **supervision has been ruled out.** That is a claim about
every dose and every form of supervision, and three things sit outside what
the run touched:

1. **Other doses.** One point on a dose curve. The pre-statement said as
   much — a larger dose "would make a null more decisive" — and the larger
   dose was not run.
2. **Other forms.** The pre-statement's own rejected alternative, a second
   forward pass putting the control question on *every* episode rather
   than half of them, is a different and stronger intervention that was
   rejected on cost, not on merit. It remains untested.
3. **The confound.** RT-57: the dose did not arrive alone. Until an arm
   renormalises the query side, "the control's share was raised" and "the
   whole query side was tripled" are not separated — and the pre-statement
   already warns that the flag changes two things at once, while naming a
   *different* pair than the ones that actually moved.

The honest scope is narrower and still useful: **reweighting the rows the
control battery already had does not teach it to read the name.**

### RT-68 — narrow step 4, but say why properly

**ARGUED. Serious. This is the recommendation the packet asks for.**

**Yes, this supports narrowing step 4 to option D or closing A3. No, a
cheaper supervision variant is not live as a route to 0.60. But the
findings file gives the weaker of the two available reasons, and the one it
gives argues against the option it points to.**

**The practical case, which does not depend on anything contested above.**
The control is 95% of the way from chance to a name-blind solver (RT-61)
and flat over the last 3,600 steps (RT-65). Four times the per-row weight
bought about +0.025 (RT-62). The distance remaining to 0.60 is 0.29 —
**more than ten times what the intervention bought.** Extrapolating from a
single dose is not evidence and I am not offering it as evidence; but
nothing in this run suggests any reweighting of existing rows clears 0.60,
and the money would be better spent elsewhere.

**The stronger case, which is in the review set and which the findings miss
entirely.** Even a rerun landing in PARTIAL would change nothing for
Amendment A3. The operative bar for this battery to be *useful* is not
0.3227 but **0.4227** — the corrected floor rule of ceiling plus 0.10
(RT-53). Below that the control's drop stays undefined and the registered
differential clause stays uncomputable, exactly as it is on all three
existing checkpoints. **So the whole band from 0.3227 to 0.4227 is a band
in which the control "learns" by the pre-stated cell and Amendment A3 is no
better off than it is today.** The findings file's anxiety about a rerun
formally landing in PARTIAL is therefore misplaced twice over: it is less
likely than stated (RT-63), and it would not matter if it happened.

That argument narrows step 4 far more firmly than "supervision is not the
binding constraint" does, and it survives every objection in this review.

**The case against, which the step 4 proposal must handle.** Option D — a
scaffolded intermediate query that teaches plain name-keyed retrieval
before layering the rule on top — **is itself a supervision change.** It
adds a training signal the control battery does not currently receive. So
"supervision is not the binding constraint" and "therefore do option D" sit
badly together, and a proposal that cites this review for the first claim
will be citing it against its own recommendation. What the run actually
rules out is **reweighting rows the battery already had**. What option D
proposes is **giving it a different and easier question first**. Those are
different interventions, and the run says nothing against the second. Write
it that way, or the contradiction will be found by someone else.

### RT-69 — the ceiling precondition still binds

**MEASURED. Worth-noting.**

John ruled on 2026-09-17 that if an Amendment A4 opens, measuring the
control battery's ceiling properly is a precondition of it. That ruling is
in the registered text. Any step 4 option that keeps this battery — option
D certainly does — inherits it, and the true ceiling near 1.0 is still
unmeasured. The 4 October proposal should carry the precondition
explicitly rather than leave it to be rediscovered.

### The sentence for the current-state document

The packet asks for the sentence that should go in `STATUS.md`. Proposed,
and deliberately avoiding both "supervision" as a bare word and the cell
label as a summary:

> **Giving the control battery its own loss term — four times the per-row
> weight, two thirds of the query gradient instead of one third — left it
> at 0.3125, against 0.2877 on the matched checkpoint that received none of
> it: still on the shoulder of a solver that cannot read the name the
> question supplies, and nowhere near the 0.60 that would show it had
> learned to read it. Reweighting the rows it already had is not what this
> battery is missing.**

Three choices in that sentence, each deliberate. It quotes the **matched**
comparison, because that is the one the pre-statement designed and the one
the findings file omits (RT-62). It says **"reweighting the rows it already
had"** rather than "supervision", because that is what was tested and the
broader word would be over-read (RT-67). It does not say "bought nothing",
because that is false (RT-62).

If a second sentence is wanted, it should be the one the findings file
should have led with: **the battery has learned the whole name-blind
procedure and none of the name-keyed lookup, which is what the three
remaining explanations are all about.**

---

## Kill case

The strongest case for throwing this interpretation out is RT-57 joined to
RT-58: the intervention did not do one thing, it did three. It raised the
control battery's share of the query gradient, it tripled the size of the
entire query loss against an action term that was never meant to move —
changing what the gradient clip does to every shared parameter on every
step — and it replaced a rotating assignment of questions to batch
positions with a fixed one whose representativeness nobody checked and
which then ran unchanged for 55,116 steps. On top of that it is one
training seed, and the matched comparison the design was built around moved
**+0.0248 with a standard error of 0.0157** — in the direction the
intervention predicted, at about 1.6 standard errors — and was reported as
"nothing". If the fixed positional split fed the control a biased half of
the episode space, or if tripling the query side degraded the shared trunk,
then a control battery that *would* learn under a clean reweighting returns
exactly this number, and the run has measured its own confound rather than
the question it was bought for. Nothing in the committed record excludes
either, because the two one-line checks that would have — episode order,
and one scored token per row — are not in the self-test, and the log and
trajectory that would show the run's behaviour over time are excluded from
the repository. **I do not think that kills the finding.** The battery sits
95% of the way from chance to the name-blind solver and is flat over the
last 3,600 steps, so whatever the confounds did, they did not hide a
battery on its way up; and the distance to the 0.60 boundary is more than
ten times what four times the supervision bought. The verdict should stand
with its scope cut to what was actually run — **reweighting the rows the
control battery already had does not teach it to read the name** — and the
sentence "supervision is not the binding constraint" should not enter the
current-state document, the 4 October proposal or the paper in that form.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-fitted-read-packet.md =====

# Review packet — the fitted linear read at all eleven positions (Gate B, tier 1)

*Prepared 2026-09-20 (Pacific) under `docs/outside-review-protocol.md`.
Gate B: this run was decision 2 of the 2026-09-19 review of the
linear-read closure, and whether the line is retired on it is a
direction question, so its interpretation is reviewed before it enters
STATUS.md.*

## The interpretation under review

From the findings on branch `worktree-fitted-read-sweep` (commit
`9080d02`), headline: FOUND NOWHERE, nothing on any checkpoint. Across
nine testable positions, five layers and three checkpoints (135 tests) a
fitted linear classifier does not find the register index anywhere at the
family-adjusted bar of 3.38 sd; one test on one checkpoint reached
MARGINAL. The instrument check reproduced all fifteen recorded numbers
exactly; the positive control at position 6 holds on all three
checkpoints at +34 to +54 sd. The findings say explicitly that this is
not a finding of absence.

The question for this review: with both the difference-of-averages read
and the fitted read now empty at these positions, what may STATUS.md say
about the linear read, and what does the registration (probe plus causal
patching, RT-49, RT-50) still require before anything is called localized
or absent.

## What the reviewer gets, and nothing else

At commit `9080d02` on `worktree-fitted-read-sweep` (or main once merged),
in `experiments/06-mvm-0a-constructed-self-index/`:

- `reviews/2026-09-19-fitted-read-brief.md` — what the run was told to do.
- `fitted-position-sweep-method.md` — committed before output (`f84db43`).
- `fitted-position-sweep-findings.md` — the findings under review.
- `a3-gates/fitted_position_sweep_a3_*.json` — the records.
- `src/fitted_position_sweep_a3.py`.
- The prior review and its rulings, since this run answers them:
  `reviews/2026-09-19-linear-read-closure-claude-worktree.md`, its
  addendum, and the RT-33 to RT-51 block of `red_team_ledger.md`.
- `powered-position-sweep-findings.md` — the difference-of-averages
  result this pairs with.
- Registered text: `amendment-a3.md` §3.2 and `pre-registration.md`.

Do not open: STATUS.md, `docs/`, any chat transcript, any uncommitted
file. Say at the top what was opened.

## The brief (fixed text from the protocol)

Four parts, a table first in each, severities marked, a one-paragraph
kill case at the end.

1. **Feasibility.** Check the brief's six requirements against the method
   file: per-test seeding (RT-39), the bar stated as a number, a
   register-index positive control or the statement that there is none
   (RT-35), the pre-stated cells and degeneracy rule, the anchor
   reproduction, geometry at the other positions (RT-40). A requirement
   claimed met with no record is a fatal finding.
2. **Satisfied by the wrong thing.** Every way FOUND NOWHERE could be
   returned by a model that carries a linear register-index signal at
   these positions: regularisation, fold size, the two untestable
   positions, the classifier's capacity against 448 dimensions on 400
   episodes.
3. **No verdict.** Including the MARGINAL test and what the pre-stated
   cells say a marginal means.
4. **Over-reading.** Write the STATUS.md sentence. Say whether "no linear
   read finds own-agent identity at the nine testable positions" is now
   supportable, and state what the registration still requires (causal
   patching) before "not localized" or "absent" can be said.

Label every finding MEASURED or ARGUED. Continue the ledger numbering
from where the control-learnability review leaves off, or from RT-52 if
that review has not filed; say which. Plain language. Do not soften.

## Filing

Findings to `reviews/2026-09-20-fitted-read-claude-worktree.md`, verbatim,
never edited after filing. Rulings in `red_team_ledger.md`. Nothing enters
STATUS.md until John rules.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-fitted-read-claude-worktree.md =====

# Outside review — the fitted linear read at all eleven positions (Gate B, tier 1)

*Filed 2026-09-20 under the outside-review protocol, against the review
packet `2026-09-20-fitted-read-packet.md`. Verbatim on filing and not
edited afterwards. Nothing here is a ruling; rulings are John's and go in
the red-team ledger (`red_team_ledger.md`).*

## What was opened

Read in a fresh worktree off `main` at the merge commit `a846b0c`, which
merged the branch the packet names (`worktree-fitted-read-sweep`) and
contains the findings commit `9080d02`. Exactly the packet's list and
nothing else:

- The brief for the run (`reviews/2026-09-19-fitted-read-brief.md`).
- The method file (`fitted-position-sweep-method.md`).
- The findings under review (`fitted-position-sweep-findings.md`).
- The four machine records under `a3-gates/` whose names begin
  `fitted_position_sweep_a3_`: one per checkpoint and the summary.
- The code (`src/fitted_position_sweep_a3.py`), all 736 lines.
- The previous review
  (`reviews/2026-09-19-linear-read-closure-claude-worktree.md`), its
  addendum, and the block of the red-team ledger running from the
  sensitivity finding (`RT-33`) to the reviewer's own disclosed error
  (`RT-51`).
- The difference-of-averages result this pairs with
  (`powered-position-sweep-findings.md`).
- The registered text: section 3.2 of `amendment-a3.md`, and the clause
  of `pre-registration.md` the previous addendum quotes. I also read
  section 3.1 of `amendment-a3.md`, because 3.2 defines how a thing is
  located and 3.1 defines what the thing is, and one is unreadable
  without the other. If that counts as exceeding the list, it is
  disclosed here rather than left to be discovered.
- Git metadata only — commit order, messages and the files each commit
  touched — to check the "committed before output" claim.

**Not opened**, as instructed: the status file (`STATUS.md`), the `docs/`
folder including the outside-review protocol itself, any chat transcript,
any uncommitted file.

**Three gaps this list creates**, stated so they are not mistaken for
omissions on my part.

**First**, the run's code imports six helper modules — the episode
builder, the capture path, the fold helper, the position definitions and
two target definitions. None is on the list. So where a claim depends on
what an episode is, what a position is, or how a fold is cut, I have the
run's own code and the registered text and nothing else, and I say so at
each point.

**Second**, the section of the findings headed "RT-33 confirmed and now
measured directly" quotes six difference-of-averages accuracies at
position 6. Those numbers are not in `powered-position-sweep-findings.md`,
which reports margins only and no accuracies at all. They must come from
the powered sweep's machine records, which the packet does not list. I
have not checked them.

**Third**, I could not read the status file, so where I write a sentence
for it I am writing a replacement for a paragraph I have not seen.

No outside lookup was used. Every number below either comes from a
committed record in this repository or from a computation I ran myself
against those records, and each is labelled MEASURED or ARGUED.

## Ledger numbering

The packet says to continue from where the control-learnability review
leaves off, or from **RT-52** if that review has not filed. **It has not
filed.** The reviews folder holds its packet
(`2026-09-20-control-learnability-packet.md`) and no findings file
answering it. The last row in the ledger is the previous reviewer's
disclosed error (`RT-51`). So I number from **RT-52**.

## Verdict in one line

**The cell is right and the run is the best-built thing in this stack.**
I reproduced every published number from the machine records, the
instrument check is locked at both ends, and no ruling from the previous
review was ignored. The interpretation is also mostly right, and holds
itself to the registered limits without being asked twice. Two things are
wrong with it: the run is roughly **two and a half times less sensitive
than the findings claim**, and the sentence the packet asks about — that
no linear read finds own-agent identity at the nine testable positions —
**cannot be said**, because the target the registration actually names
was never read by this instrument at any of those nine positions.

---

# 1. Feasibility

*Did the method file meet the six requirements the brief set, and is each
one backed by a record?*

| # | finding | severity | label |
|---|---|---|---|
| RT-52 | all six requirements are met and every one has a record; the instrument check is locked at both ends so neither the code nor the record can be edited to fit the other | worth-noting (credit) | MEASURED |
| RT-53 | the findings' "below 1e-15" for the instrument check is not on the record, which resolves only to six decimal places, and two of the three checkpoints are exactly zero rather than nearly zero | worth-noting | MEASURED |
| RT-54 | both self-corrections in the findings are accurate, and I confirmed each against the record | worth-noting (credit) | MEASURED |
| RT-55 | the run used 200 shuffled-label draws where the previous review's first recommendation was 1,000; disclosed in advance with the arithmetic, but it is why the bar leans on a normal approximation | worth-noting | MEASURED |

### RT-52 — the six requirements, each with a record behind it

**Worth-noting, and it is credit. MEASURED.** The brief said a
requirement claimed met with no record is a fatal finding. I checked all
six against the machine records rather than against the method file's
description of itself. There are no fatal findings here.

**Seeding per test.** The method says the fold split and the shuffled
draws are seeded from a digest of checkpoint, target, position and layer
together, rather than by layer alone as the previous sweep did. The code
does this, and its own self-test asserts that all 55 tests on a
checkpoint get distinct seeds, that the seed is stable when recomputed,
and that it changes when the checkpoint changes. Verified by reading the
code, not by trusting the comment.

**The bar as a number.** Stated as 3.38, applied rounded up from an exact
3.3740. I recomputed it: spreading a 5 per cent family-wise error across
135 tests needs a one-sided margin of **3.3740** standard deviations.
Exact. The previous sweep's 3.56 for 270 tests recomputes to **3.5603**.
Also exact.

There is a small thing worth recording because it could have gone the
other way. The code rounds each margin to two decimal places *before*
comparing it to the bar, so the threshold that actually operates is
3.375, not 3.3740. That is still stricter than the arithmetic requires,
so the method file's promise — "rounded up, so the bar in force is never
looser than the bar the arithmetic asks for" — survives its own
implementation. I checked because it is exactly the kind of thing that is
usually wrong.

**A positive control for the register index, or the statement that there
is none.** The method states plainly that there is no guaranteed-present
control for this target, only a guaranteed-*derivable* one at position 6,
and spells out what that costs before the run: a null everywhere cannot
separate "the models do not carry it away from that position" from "this
read cannot find it away from that position". That is what the ruling on
the missing control (`RT-35`) asked for, and it is what the findings
repeat. The control is then used as a one-way gate — failure voids a
checkpoint, success certifies nothing elsewhere — which is the correct
shape.

**Pre-stated cells and the degeneracy rule.** Both fixed in the method
file and both implemented as written. FOUND requires three things
together: margin at or above the bar, zero of 200 draws matching or
beating the real accuracy, and accuracy above the majority-class rate.
The degeneracy rule suppresses a label if the null has no spread, a class
is missing from a training fold, or accuracy lands exactly on the
majority-class rate. The code's self-test plants a signal and confirms
FOUND, plants noise and confirms no label, raises the bar out of reach
and confirms the same planted signal is demoted to MARGINAL, and starves
a class to confirm the degeneracy rule fires and suppresses the label. I
read all of it.

**The anchor reproduction.** This is the strongest piece of engineering
in the stack and it deserves saying. The fifteen recorded numbers are
written into the code as a pre-stated claim, **and** the code refuses to
run at all unless those fifteen values match the committed record files
to nine decimal places. So the code cannot be edited to fit the record,
and the record cannot be edited to fit the code, and a mismatch stops the
run rather than being reported at the end. Then the run re-executes the
original 400-episode configuration and compares. Every one of the fifteen
reproduced.

**Geometry at every position.** Measured at all 165 tests, not just the
anchor, which is what the ruling on the one-position geometry (`RT-40`)
asked for. The numbers are in the records. What the findings *say* about
them is wrong in one place, which is a separate finding below (`RT-57`).

### RT-53 — a number in the findings that the record does not carry

**Worth-noting. MEASURED.** The findings report the instrument check as
reproducing "to floating-point round-off — the largest difference on any
cell was below 1e-15". The record does not support that figure. The code
rounds the largest difference to six decimal places before writing it, so
every record says `0.0`, and the finest statement the record can make is
"below five parts in ten million".

The record does carry one detail the findings lose. On the pilot the
field recording an exact match across every layer is **false** while the
largest difference still prints as `0.0` — which means the pilot's worst
difference is greater than zero and smaller than the rounding could show.
On seeds 1 and 2 that same field is **true**, so those two are bit-exact.
So the three checkpoints did not behave identically: two reproduced
exactly and one reproduced to within summation order. The findings' table
prints "below 1e-15" against all three, which flattens that.

Nothing turns on it. The pre-stated tolerance was one episode in 400 and
the run used none of it. But "below 1e-15" is stated as a measurement and
it is an inference, and this review is required to mark that distinction.
