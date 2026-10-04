*This is file 23 of 33 of one review packet, pasted into a single conversation. It contains record 15 part 3 of 3 (the check of the competing-solver run and the twenty-piece control); record 16 part 1 of 3 (the measurement rehearsal on small stand-in models). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 15 of 25, part 3 of 3 - the check of the competing-solver run and the twenty-piece control - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md` (complete file, 42,479 characters) =====
| Where | Lines | What changes | Why |
|---|---|---|---|
| Header, item 2 | 21 to 25 | The run is done and checked; say what came back in one sentence, or remove the item | Pull request 88 and this check |
| Section 6.4, item 3 | 1178 to 1183 | After "because an untransplanted model lands on the donor's answer only by erring onto exactly that one of the seven other slots", add that this assumes wrong answers spread evenly; a model that confuses owners lands on the donor's value more often (on the toy's competing solver about twice the formula), and the rule then withholds the reading, which is the intended outcome | The solver's question 3; table 3.3 of its findings |
| Section 7.3, item 2, "has run once" bullet | 1810 to 1829 | Name the second code test (pull request 89, `out-control-2-twenty-draws/`, NOT A RESULT) beside the first, with its figures: real figure 0.0012; twenty pieces middle 0.0037, 95th percentile 0.0052; 0 below, 1 equal, 19 above. Keep "not a pass or a fail of anything" | Ruling 5; pull request 89 |
| Section 7.3, item 2, "Twenty random pieces, not one" | 1830 to 1837 | Replace "owed with the registered measurement, so the code path that ran once ... is not quite the one registered" with: the change is made, in `src/control2_twenty_draws.py`, and its code test was run before the registration review. Cite the check-questions ruling 1 | That ruling names these lines |
| Section 7.3, the last paragraph | 1996 to 2017 | Replace "has not yet been measured ... This version quotes no figure for it ... until then this text does not go to the registration review" with the result: no verdict on every seed, under both readings of the solver; the reason (no site set cleared the floor at nomination); the read's best piece 20 to 25 of 180; the no-transplant rule failed on every seed; and that with the channel removed this follows from the pairing alone, so the reading with the channel left on is the informative one. Cite the findings and this check | Pull request 88 |
| Section 7.5, item 4, and the matching lines in 7.4 and section 9 | 2105 to 2108; 2072 to 2076; 2276 | Name how the band is computed: the Wilson interval at 95 percent, as the competing-solver run computes it. Ruling 4 says "the band that sampling alone would put around it" and names no method | Section 4.2 above |
| Section 8.1, reference points | 2178 to 2187 | Replace "to be put through the nomination under it before the registration review" with the result, and keep the solvers as references: **say that the gate does not apply to them** | Section 5.3 above |
| Section 9, control 2 row | 2265 | Cite record B, ruling 5, and the check-questions ruling 1 beside record A | Both records stand; the second ruling set the timing |
| Section 10, R-4 | 2386 to 2389 | Add the competing solver to the no-verdict cases | Pull request 88 |
| Section 10, R-5 | 2391 to 2396 | "Exercised under the piece rule, 2026-10-03, and checked" with a pointer | Pull request 88 and this check |
| Section 10, R-6 | 2397 to 2399 | "kept off zero by the whole-state floor" becomes "kept off zero by the whole-state floor together with the gate and the no-transplant rule", with one sentence: on the toy's competing solver, which fails the gate, the floor was cleared on fresh episodes with a divisor of one or two episodes in 800 | Section 5.4 above |
| Section 10, the paragraph on the seven controls | 2445 to 2453 | As for lines 1810 to 1829 | Pull request 89 |
| Section 10, "What happens next"; section 11, step 1 | 2455 to 2458; 2475 to 2478 | Move the competing solver's run and its check from "owed" to done | Pull request 88 and this check |
| Section 13, weaknesses | (new) | One weakness, if John agrees (question 7 in section 9 below): the toy's ordinary competing solver fails the task, so its no verdict shows the measure returns nothing on a model that has not learned the task, not on one that solves it by a different route | Section 9, question 7 |
| Section 15, item 29; section 17; section 19, items 5 and 7; section 20; closing | 3318 to 3324; 3735 to 3737; 3864 to 3869; 4009 to 4018; 4035 to 4053; 4161 to 4162; 4190 to 4193; 4215 to 4217 | Each says the run, the control's code change, or both are owed; each becomes done, with a pointer | Pull requests 88 and 89 |

**Not to change:** nothing in either pull request touches a registered
number. No floor, bar, count or site list moves.

---

## 8. What this session did not do

- It did not edit pull request 88 or 89, version 4, any ruling file,
  `STATUS.md` or `data/project.toml`.
- It did not read version 4 through end to end; the passages in section 6
  were found by search and read with their sections.
- It did not run either piece of code on any model the runs did not use, did
  not run the `--smoke` paths, and did not re-run the earlier code test (it
  compared against that test's committed output).
- It did not compute, at the 33 site sets that cleared the floor on fresh
  episodes, what the reading would have been at each one; the run does not
  save the fresh-episode grid, and section 5.4 relies on the summary the run
  does save.
- It did not check the controls re-run, the short pre-stated run or the
  repairs, beyond reading the functions these two runs import.
- It put no question to John in chat and read no transcript of another
  session.

---

## 9. The questions for John

Not asked in chat; for the coordination session that routes rulings, one
session at a time.

### 9.1 The five the two findings put

**The solver's question 1: which reading of the solver the registration
cites.** *Their suggestion:* the channel removed as the primary, because
that is how the solver was trained and scored; the channel left on stated
beside it, because with the channel removed the no verdict follows from the
pairing alone. **Follows from the evidence.** With the channel removed the
twins' states were identical to the last bit on every seed (section 4.1), so
every transplant is a null transplant and that reading cannot return
anything but no verdict. *Addition:* the registration should say in so many
words that the primary reading's no verdict is a property of the pairing,
not evidence about the measure, and that the channel-left-on reading is the
one that tests the measure.

**The solver's question 2: whether the registration says what actually
stops this solver.** *Their suggestion:* one sentence, that the solver's no
verdict comes from the gate on learning, the piece rule and the
no-transplant rule, each with room to spare, and that the floor is close to
zero for a model near chance. **Follows in part; the gate needs rewording.**
The piece rule (best 20 to 25 of 180 against 144) and the no-transplant rule
(missed by 0.11 to 0.14 against 0.018) are right. The gate is not applied to
competing solvers in version 4 (section 5.3). *Suggested sentence instead:*
"On the toy, the ordinary competing solver returned no verdict because no
site set cleared the floor at nomination; behind that, its best piece missed
the piece rule by 119 or more of 180 and its untouched rate missed the
no-transplant rule by 0.11 or more, and it would have failed the gate on
learning had it been gated as the free model is. For a model near chance the
floor itself is close to zero and is decided by one or two episodes."

**The solver's question 3: the no-transplant formula on a solver that cannot
tell owners apart.** *Their suggestion:* report only; the rule withholds a
reading here, which is the right outcome, but the registration should not
describe the formula as a property of every model. **Follows.** The untouched
rate (0.22 to 0.25) sits close to the solver's own accuracy (0.22 to 0.24),
which is what a solver choosing among the four agents' values would show;
the donor's value is one of those four. The wording change is in section 7
above, at lines 1178 to 1183.

**The control's question 1: which file is the registered control 2.**
*Their suggestion:* the registration names `control2_twenty_draws.control2`
as control 2's code and says `rerun_controls.control2` is the earlier
version, kept as the record of what the re-run did. **Follows.** The new
function is the old one with only the ruled change (section 5.1), and the old
one still carries the pass line John withdrew. *Addition:* the registered
code for the full-size run is still to be written (section 11, step 3 of
version 4); it should take control 2 from the new function, so that there is
one control 2 at registration and not two.

**The control's question 2: whether the 95th percentile of twenty is the
right summary.** *Their suggestion:* leave it as ruled, and print the twenty
as well. **Follows.** With twenty draws the 95th percentile is a mix of the
two largest (here 0.0052, between 4 and 7 episodes of 800, which no single
draw can equal); control 3 has the same property and was ruled that way.
Printing the twenty, as the code does, lets a reader see the spread.

### 9.2 Two that this check raises

**6. The solver run's explanation, before it is quoted.** Section 4 of the
solver's findings, its question 2 and pull request 88's description say the
gate on learning is the first thing holding the solver back, on the ground
that "a model that fails the gate is not read at all". Version 4 does not
gate the competing solvers (section 5.3). *Suggestion:* the running session,
or the session that writes the registration text, corrects those three
places to "would fail the gate if it were gated as the free model is" before
any of it is quoted; no re-run, and no change to any rule. This is a wording
question, and it goes to John only because pull request 88 is his to merge.

**7. What the competing-solver run can and cannot show.** The toy's ordinary
competing solver fails the task: it is right about one time in four, the
rate of a solver that cannot tell whose value it needs. So its no verdict
shows that the measure returns nothing on a model that has not learned the
task. It does not show what the measure does on a model that *does* the task
by a route other than tracking whose turn it is, which is the harder test of
"satisfied by the wrong thing". The toy has no such model: the name-only
solver is computed from the episodes and has no states to transplant
(`training.name_only_solver`). *Suggestion:* no new run before the
registration review. Add one weakness to section 13 of the registration text
saying this in two sentences, so a reviewer finds it stated rather than
finding it. *Strongest alternative:* build a competing solver that learns
the task from another cue (for example, a model fed the name token at every
turn) and put it through the measure before the review; that is a training
run, not $0 work on committed files, and would move the timeline.
===== END OF RECORD 15, part 3 =====

===== RECORD 16 of 25, part 1 of 3 - the measurement rehearsal on small stand-in models - `docs/2026-09-21-successor-measure-rehearsal.md` (complete file, 56,203 characters) =====
# The successor experiment's measurement rehearsal — findings

*2026-09-21 (Pacific). **UNREGISTERED.** Nothing here is a result about the
scientific question, nothing here is a bar, and nothing here registers
anything. It is a demonstration that the instrument exists and gives back
numbers — and, where it does not, an account of why.*

*Ran locally on the laptop, on models of about one to one and a third million
parameters. **No machine was rented, no vendor was contacted and nothing was
spent.** The one short slice of rented time is staged and has not been run; it
needs John's spoken go naming it, and that has not been given.*

*Filed at the path the protocol names for a rehearsal whose experiment
directory does not exist yet. Code and every output file:
`experiments/rehearsal-successor-measure/`.*

*Written under the workspace plain-language rule.*

---

## 0. What to read if you read nothing else

The measure works, and the procedure for pointing it at a system does not.

- **The measure separates the two constructed arms by the whole width of its
  scale.** The arm built so that the ownership answer sits in a slot of its
  own reads **exactly 0.0000** on all three seeds. The arm built so the
  ownership answer is stirred through everything reads **0.873, 0.885 and
  0.880**. That is rehearsal item R-2 and R-3 both passing, and it is the
  thing the successor experiment most needed to know.
- **The nomination procedure as the proposal writes it fails completely**, on
  the one arm whose answer is in a known place. It returns 0.0000 to 0.0117
  where the truth is 1.0000 — that is, it reads the separable arm as
  maximally entangled. The cause is that the proposal names the quantity the
  straight-line read is fitted to and never says what the **label** is, and in
  a grammar whose marker words are drawn afresh each episode that phrase has
  three meanings, two of which find nothing.
- **The two findings the proposal review marked fatal are both confirmed**, by
  measurement rather than by argument, and one of them is confirmed to four
  decimal places.
- **The freely trained arm reads at the entangled end**, not between the two
  anchors. That is either the honest answer or the instrument's ceiling, and
  the rehearsal cannot tell which.
- **Two of the seven controls do not mean what they say they mean**, and one
  of them would veto exactly the arm it exists to validate.
- **Throughput**: the two constructed architectures cost 0.98 and 1.05 times
  what the free one costs per step, not the 1.55 the money estimate inherited
  from a different experiment. Only the *ratio* is measured; the absolute
  figure the second release of money rests on still needs the rented slice.
- **The proposal's first stop condition is adjudicated here and does not
  fire.** It is keyed to the learn-both item failing, and that item does fail on
  half of itself. But the condition's own words are "not learnable even in
  principle" and "nothing trains", and the separable arm reaches 1.0000 on both
  conditions on all three seeds. The reasoning is in section 8, and it is the
  rehearsal's reading rather than a ruling.

---

## 1. What was committed when

The programme's discipline is method before output, and the worst failure in
its history came from a fix marked adopted with nobody having run anything.
The commit order on this branch:

| order | commit | what |
|---|---|---|
| 1 | `9a91c06` | the method: what would be built, and passing, failing and no-verdict for every check, written down while nobody knew which would fire |
| 2 | `518bf0e` | the method addendum: four further checks, after the review returned two findings marked fatal — again committed before their code |
| 3 | `5fa85e2` | the code: the grammar, the three architectures, the transplanting code, the measure |
| 4 | `8bc5fbe` | the rented slice, staged and not run |
| 5 | `9673bf1`, `4e89c69`, `623ef23` | the denominator checks, the frozen reads, the across-seed method, the self-test record |
| 6 | `6e8cc08` | the results |
| 7 | this file | the findings |

Section 9 records every place where building it differed from planning it,
which is the only honest way to keep a method file that was committed first.

---

## 2. The six checks the protocol requires

Each with the command that was run and the output it produced. The full output
of every one is in `experiments/rehearsal-successor-measure/out/`.

### P-1. The target can be found — **PASS, but only after a repair**

    cd experiments/rehearsal-successor-measure/src
    ../../../.venv/bin/python rehearse.py --stage nominate

The instrument is the proposal's own two-step nomination: fit a straight-line
read for "which agent is acting" at every candidate site, take its leading
directions up to a rank cap, then nominate by **causal effect** — the subspace
whose transplant best reproduces the counterfactual on development episodes.
It runs blind on every arm; the separable arm's known ownership block is never
handed to it.

On the separable arm, where the answer is in a known place by construction:

| seed | the procedure **as pre-stated** | the procedure **repaired** | the truth (its real ownership block) |
|---|---|---|---|
| 0 | 0.0117 | **1.0000** | 1.0000 |
| 1 | 0.0000 | **1.0000** | 1.0000 |
| 2 | 0.0000 | **1.0000** | 1.0000 |

The repair is section 3. **As written the procedure fails**; repaired, it
finds the answer exactly, and the reading it produces matches what the
procedure gets when it is simply handed the true block.

### P-2. The comparison has room to move — **PASS**

    ../../../.venv/bin/python rehearse.py --stage gate

Both ordinary competing solvers were built and scored on both conditions, and
all seven controls were run on every arm and seed. Nothing was assumed.

| solver | own-directed | named-other-directed |
|---|---|---|
| ownership-blind (trained, acting channel removed) | 0.2237 | 0.2253 |
| name-only (computed) | 0.2380 | 1.0000 |
| references: guessing over eight slots / a solver that cannot tell whose value it needs | 0.1250 / 0.2500 | 0.1250 / 0.2500 |

The comparison is not saturated: the separable arm reaches 1.0000 on both
conditions against an ownership-blind competitor at 0.2237.

### P-3. The arithmetic is finite — **PASS**

    ../../../.venv/bin/python measure.py --self-test

Sixteen made-up cases chosen to break the formula, including a zero
denominator, a denominator just under and just over the floor, an
ownership-only accuracy above the whole-state one, both accuracies equal and
both zero. Every one returns a finite number or the explicit no-verdict
outcome with its reason. All 10,201 share pairs from zero to one were swept:
none returns a non-finite value. A floor of zero is refused outright, because
a floor of zero is the closed design's unsatisfiable-denominator defect
re-entering through the front door.

### P-4. The interventions run end to end — **PASS**

    ../../../.venv/bin/python transplant.py --self-test
    ../../../.venv/bin/python rehearse.py --stage transplant

Every arm is trained, **saved to a checkpoint file and read back from it**
before any intervention runs, so what is exercised is the path the registered
experiment would use. Eight interventions run to completion on every arm and
seed: the whole-state transplant, the ownership-only transplant, the null
transplant, the content-complement transplant, the matched random-subspace
transplant, an unmatched donor's transplant, a transplant at a position where
the identity cannot yet be known, and the acting-channel lesion.

They move what they are supposed to move: on the separable arm the whole-state
transplant takes the donor-dictated action from 0.0000 to 1.0000.

### P-5. All three outcomes are reachable — **PASS**

    ../../../.venv/bin/python rehearse.py --stage outcomes
    ../../../.venv/bin/python negative_case.py

| made-up case | expected | measured |
|---|---|---|
| the separable arm at its nominated site set | near zero, valid | **0.0000, 0.0000, 0.0000** |
| the entangled arm at its nominated site set | high, valid | **0.8727, 0.8848, 0.8801** |
| the separable arm at a deliberately failing site set (earliest layer, before the identity can be known) | no verdict | **no verdict**, whole-state accuracy 0.0000 |
| a negative reading | reachable | **−0.1706 and −0.2755** |

The negative reading deserves its own sentence, because finding it took
finding out what causes it. Searched over every architecture, every one of the
nine layer sets, every one of the five position sets, all three readings of
the read's label and all six rank caps on fresh episodes, **no configuration
produced a negative reading at all**. It appears immediately on episodes whose
marker words the arms have never seen. The condition is therefore not
mysterious and it is worth registering: **a negative reading appears when the
subspace was chosen on data whose vocabulary the reading is then taken on.**
The nominated directions live in the well-trained part of the space; the
whole-state transplant is capped by the arm's own degraded accuracy on strange
words; so the subspace beats the superspace and the reading goes below zero.
That is exactly what the proposal says a negative reading is for — a warning
about the instrument, reported as observed and never clipped to zero.

### P-6. An ordinary competing solver is built and scored — **PASS**

    ../../../.venv/bin/python rehearse.py --stage gate

Two were built, because "satisfied by the wrong thing" has two shapes here. An
**ownership-blind solver** — the same architecture with the acting channel
removed entirely, so it has none of the structure the measure claims to detect
— scores 0.2237 on the own-directed condition and 0.2253 on the named-other
one, which is the one-in-four level and nothing more. A **name-only solver**,
computed rather than trained, gets the named-other condition exactly right and
the own-directed condition at 0.2380.

The measure does not read near-zero degree off the blind solver, because the
blind solver cannot be read at all: its own-directed action does not depend on
an ownership answer it does not have, so there is nothing for a transplant to
move. **That is the right answer** — a system with none of the structure
returns no reading rather than a flattering one.

---

## 2a. The proposal's eleven rehearsal items, and where each one stands

===== END OF RECORD 16, part 1 =====

