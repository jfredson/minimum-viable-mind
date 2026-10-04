*This is file 14 of 33 of one review packet, pasted into a single conversation. It contains record 5 part 2 of 4 (the inside reviewer's findings on version 4 (Gate A, tier 1)). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 5 of 25, part 2 of 4 - the inside reviewer's findings on version 4 (Gate A, tier 1) - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md` (complete file, 80,950 characters) =====
**Not opened.** `STATUS.md`, `data/project.toml`, the `site/` directory, any
pull request description, TimeAssembler, any chat or transcript, any
uncommitted file of another checkout, anything outside this repository except
`~/Code/CLAUDE.md`. The project's Python interpreter lives in the main
checkout's `.venv` and was run by its full path; no file there was opened. The
earlier Gate C reviews of versions 1 and 2, the ruling packets other than the
1h page, the controls re-run's and short run's findings and checks as
documents (their output files were read directly), and the compute ledger were
not opened: the check of version 4 had already compared every dollar figure
and the 2026-10-03 toy figures against them, and this review spent its time on
what that check says it did not do.

---

## Findings at a glance

| Number | Severity | Label | Brief part | Version 4 lines | The finding in one line |
|---|---|---|---|---|---|
| RT-237 | **fatal** | MEASURED | 1, 3 | 2223, 2270, 2064; S8 at 2599 to 2609 | The free model's gate requires "the ownership-free state and syntax batteries" to hold. The successor's task has no such batteries, the clause sets no line, and nothing rehearsed it; by the design's own stop condition S8 an unevaluable gate fails, so the free model could never be read |
| RT-238 | **serious** | MEASURED | 1, 3 | 1113 to 1132; 2261 | The whole-state floor as printed admits every site set, with a divisor of exactly zero or below, when a model's own-directed accuracy is at or under its no-transplant rate. The code refuses those cases by a clause the text does not carry. On the competing solver the printed rule admits 45 of 45 site sets on four runs of six; the code admits none |
| RT-239 | **serious** | MEASURED (the texts), ARGUED (the consequence) | 2, 1 | 496 to 525; 1890 to 1896; 133 to 141 | The grammar is registered as an extension of the closed design's grammar, which has twelve turns (not the ten stated) and shows the model its own name three tokens before it acts. The two deliberate departures that remove that cue and make the twins the same text are written nowhere in version 4 |
| RT-240 | **serious** | MEASURED (a stand-in, NOT A RESULT) | 1, 3 | 2067 to 2071; 2276; 1320 to 1355 | The ruled counts (a read fitted on 420 episodes) were rehearsed only at the toy's width of 160. At the registered width of 448 there are more coordinates than fitting episodes. Padding the committed toy states to 448 with noise drops the entangled model's read from 177 to about 90 and from 176 to about 130 of 180, below the floor of 144 |
| RT-241 | **serious** | ARGUED | 3 | 295 to 313; 456 to 467; 2061 to 2062; 2188 to 2189; 820 to 827 | The outcome map has holes: a no verdict on the separable model maps to nothing; the two-model fallback has no registered outcome term; "R3 for that arm" against R3 as the whole experiment's outcome; a failed channel-removal check on the free model; and whether a built model that fails its gate after the first release gets the one permitted re-run |
| RT-242 | worth-noting | MEASURED | 4 | 1384 to 1389 | "Anchored at the action position the three candidates reach 0.733, 0.383 and 0.478": those are one candidate's three seeds. The three candidates' best on the free model over those site sets are 0.733, 0.417 and 0.633. Carried from version 3 |
| RT-243 | worth-noting | MEASURED | 4 | 1118 to 1125 | "On the toy they never did [disagree]": true of the twelve own-directed nomination grids, not of the toy. The two forms of the floor disagree on 576 rows of the repairs run's other-agent grids, 892 of the grammar attempt's and 1,080 of 1,080 of the competing solver's, each time with the plain form passing a model near chance |
| RT-244 | worth-noting | MEASURED | 4 | (the ruled sentence of 2026-10-04, ruling 2; v4 1996 to 2017) | The ruled sentence about the competing solver says its untouched rate "missed the no-transplant rule by 0.11 or more". It missed the formula by 0.109 to 0.139 and the rule's allowance by 0.091 to 0.121; "0.11 or more" holds on neither reading. Its first clause holds only under the code's floor (RT-238) |
| RT-245 | worth-noting | MEASURED | 1 | 2520 to 2524; 1332 to 1355 | The registered nomination on the laptop's processor is argued, not measured, to be practical. Timed here at the registered shape: one transplant pass over the 600 development pairs takes 4.6 seconds, so one model's nomination takes about two hours and the twelve registered models about 25 hours, which holds the argument up. The device ruling names the device for the read's fit; it does not name one for the transplant passes that choose the site set, which on the entangled model was decided by one episode in 600 |
| RT-246 | worth-noting | ARGUED | 2 | (the weakness ruled 2026-10-04, ruling 7) | The ruled new weakness says the toy has no model that does the task by another route. It has one: the free model itself solves the own-directed condition without carrying its marker word (version 4, section 5.4), and the measure returns no verdict on it. The weakness can be stated more exactly, and the other-route case that would read is the name-cue route of RT-239 |

---

## The registration text as reviewed

The registration text is version 4 plus changes that have been ruled and not
yet written in. This review collected those changes from the committed record,
read version 4 against each, and asked whether each can be written in as
described.

| Ruled change, and where it is ruled | Version 4 now | Can it be written in as described? |
|---|---|---|
| The thirty wording fixes of the check of version 4 (its section 4), ruled into the text by `docs/rulings/2026-10-03-version-4-check-questions-rulings.md` ("What this changes") | Not yet written: the stale per-seed separation sentences (lines 412 to 414, 2256, 2418 to 2420, 3814), the stale citations to record A, the processor clause at lines 2520 to 2524, and the rest | **Yes**, all thirty. This review confirmed the ones it could check by a command: the stale separation sentences are at lines 413, 2419 and 3814; the processor clause is at lines 2520 to 2524; section 17's sweeps now return 761 and 235, not 759 and 233; and the lock file given as the model for pinning is not committed (`git check-ignore` names `.gitignore` line 35) |
| The other-agent control's code changed to twenty random pieces and its code test run again before the registration review (the check-questions ruling, ruling 1; record B, ruling 5) | Lines 1831 to 1837 still say "owed with the registered measurement" | **Yes**; done in `src/control2_twenty_draws.py`, run as a test of the code (`out-control-2-twenty-draws/`, NOT A RESULT), and checked |
| The separation rule stays as ruled, said in one sentence (the check-questions ruling, ruling 2) | Not yet written | **Yes** |
| The solver's main reading has the acting channel removed; the other reading stated beside it; the main reading's no verdict comes from the pairing (2026-10-04, ruling 1) | Lines 1996 to 2017 still say the run is owed | **Yes** |
| The sentence on what stopped the solver, in the check's words (2026-10-04, ruling 2) | Not yet written | **Not as worded.** Its first clause, "no site set cleared the floor at nomination", is true only under a clause of the code the text does not carry (RT-238), and "0.11 or more" is true on no reading of the figures (RT-244) |
| The no-transplant formula reported, not described as true of every model (2026-10-04, ruling 3) | Lines 1178 to 1183 give the formula's reason as if general | **Yes** |
| The registered control 2 is `control2_twenty_draws.control2`; `rerun_controls.control2` named as the earlier version (2026-10-04, ruling 4) | Not yet written | **Yes**; the new function's early exits are copied from the old one and its random pieces are control 3's twenty (the check of pull requests 88 and 89, section 5.1) |
| Ninety-fifth percentile of twenty as the summary, all twenty printed (2026-10-04, ruling 5) | Not yet written | **Yes** |
| "Would fail the gate if it were gated as the free model is", not "the gate stopped it" (2026-10-04, ruling 6) | Not quoted in version 4 yet | **Yes** |
| A new two-sentence weakness: the toy's competing solver fails the task (2026-10-04, ruling 7) | Not yet written | **Yes**, and it can be stated more exactly (RT-246) |
| The changes in section 7 of the check of pull requests 88 and 89, including the sampling band named as a 95 percent Wilson interval (2026-10-04, "What this changes") | Lines 2105 to 2108, 2072 to 2076 and 2276 name a band and no method | **Yes**; the competing-solver run computed it that way (`nominate_blind_*.json`, `best_piece_sampling_band`) |
| Record B's fuller points: the processor proving impractical is a fresh question for John, not a switch; the method states what "the model's own turn" means for a solver with no channel; a miss at the first full-size run goes to John with the band (record B rulings 3, 4 and 7; the check-questions ruling, "For John to know") | Lines 2520 to 2524 say the opposite of the first; S4a at lines 2578 to 2583 omits the band | **Yes** |

**Where version 4 as it stands conflicts with a ruling in a way the ruled
changes above do not already fix:** nowhere this review found, beyond the
places the two checks already list. The findings below are about the text that
results once all of the above is written in.

---

## 1. Feasibility

| Pre-stated quantity or rule | Can it be measured with the stated instrument, and can the comparison reach its line? | Record | Holds? |
|---|---|---|---|
| The nomination rule (sections 6.4 item 1, 7.2 items 2 to 5) | Yes: the rule written from the text alone reproduces the committed code's choice on 24 of 24 toy rows | this review, `rule_from_text.out.txt` | **holds** |
| The reading (section 6.3) and its top of scale | Yes; top of scale 1.0000 on every arm and seed; smallest divisor among the models that read 0.4863 | `failure_mode_pass.out.txt`, failure 1 | **holds** |
| The whole-state floor (section 6.4 item 1) | On a model that has learned the task, yes. On a model at chance, the printed formula is met by any site set, with a divisor of zero or below | `rule_from_text.out.txt` section 4; `failure_mode_pass.out.txt` | **RT-238** |
| The fit floor, 144 of 180, on the piece (sections 6.4 item 2, 7.2 item 3) | Rehearsed at width 160 only. At width 448 the same counts give more coordinates than fitting episodes; a stand-in drops the entangled model below the floor | `width_vs_count.out.txt` | **RT-240** |
| The sampling band at the floor | Computable; ruled as a 95 percent Wilson interval by adoption of the check's section 7 | `out-competing-solver-run/nominate_blind_*.json` | holds once written in |
| The no-transplant rule, 0.018 room | Exercised at both ends (`failure_mode_pass.out.txt`, failure 3 part three); its largest measured miss 0.017536 recomputes | `older_figures.out.txt` | **holds** |
| The gate on learning, 790 of 3,000 | Exercised; recomputes | the check of version 4; `failure_mode_pass.out.txt` | **holds** |
| The channel-removal collapse line (section 8.2) | Exercised on all twelve toy models | `out-repairs/gate_base.json` | **holds** |
| **"The ownership-free state and syntax batteries must hold"** (section 8.2) | **Cannot be measured: no such battery exists in the successor's task, no line is set, no rehearsal record exists** | `failure_mode_pass.out.txt`, failure 3 part one | **RT-237, fatal** |
| Separation 0.5, lowest of arm C minus highest of arm T | Exercised: 0.9926 | `rule_from_text.out.txt` section 3 | **holds** |
| Arm M: 0.3 to 0.7 and within 0.10 of its true-slot reading | Exercised; recomputes (the check of version 4) | | **holds** |
| The controls that hold (7, 1 on arm T, 4 as redefined) | Exercised on all twelve | `rule_from_text.out.txt` section 2 | **holds** |
| Control 2, twenty random pieces | No figure possible at toy scale; carries no line, by ruling | | as ruled |
| The two-of-three rule for seeds that disagree | Never produced on the toy (no arm's seeds disagree); the code does not exist | `failure_mode_pass.out.txt`, failure 3 part one | stated in the text; open |
| The registered nomination on the laptop's processor | Argued in the text; timed here | `registered_shape_timing.out.txt` | **RT-245** |

### RT-237 (fatal, MEASURED). The free model's gate names batteries the successor's task does not have

**What version 4 says.** Section 8.2, the channel-removal check that gates
whether the free model is read (lines 2201 to 2223), ends: "the ownership-free
state and syntax batteries **must hold**." The section 9 row (line 2270)
carries the same words, and section 7.4 freezes "the ownership-lesion rule"
among the gates (lines 2063 to 2065). Section 5.4 (lines 957 to 959) says the
free model "is read only after it passes the learn-both gate, the
ownership-lesion check in section 8, and the fit floor". Stop condition S8
(lines 2599 to 2602): "A rehearsal item, a gate or a stop condition **cannot
be evaluated**: missing data, code that will not run on the artifact, a
measurement never taken. It counts as failed and its consequence fires; it is
never recorded as not applicable and stepped over."

**What was measured.**

```
$ grep -rlE '\bT_(state|syntax)\b|([Ss]tate|[Ss]yntax) batter' experiments/rehearsal-successor-measure/src || true
(no file)
$ grep -rlE '\bT_(state|syntax)\b|([Ss]tate|[Ss]yntax) batter' experiments/06-mvm-0a-constructed-self-index/src/
experiments/06-mvm-0a-constructed-self-index/src/summarize_null.py
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py
experiments/06-mvm-0a-constructed-self-index/src/lock_guard.py
experiments/06-mvm-0a-constructed-self-index/src/ctl_split_check.py
experiments/06-mvm-0a-constructed-self-index/src/null_calibration_a3.py
experiments/06-mvm-0a-constructed-self-index/src/run_post_pilot.sh
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py
```

and, from `failure_mode_pass.py` (output in `failure_mode_pass.out.txt`):

```
  the lesion clause 'the ownership-free state and syntax batteries must hold': fields the gate file records: ['lesion_collapses_own', 'lesioned_other', 'lesioned_own', 'n', 'other', 'other_clears', 'other_correct', 'own', 'own_by_route', 'own_clears', 'own_correct']
  grep of the rehearsal code for a state or syntax battery: (no file)
```

The batteries are the closed design's end-of-episode question sets (`T_state`
and `T_syntax` in `curriculum_a3.py`, line 163: `BATTERIES = ("T_act",
"T_other", "T_state", "T_syntax")`). The successor's task, as the rehearsal
built it (`grammar.py`), has eight assignment turns and two action turns and
no end-of-episode questions at all. The gate file every toy channel-removal
figure comes from records no battery field. By search, the clause entered at
version 1 (`docs/successor-experiment-proposal-2026-09-21.md`, line 568: "the
ownership-free state and syntax batteries hold"), was ruled into the queue
ruling's page 1h with the rest of option (i), and has been carried word for
word through versions 2, 3 and 4. No review of versions 1 to 3 and neither
check of version 4 mentions it (`grep -n -i batter` over those files returns
nothing on this clause).

**Why it is fatal.** Two rules the design itself carries make it so. Item 5 of
the 2026-09-21 ruling, which version 4 quotes at line 2352: "A pre-stated
quantity the rehearsal never exercised is a fatal finding on its own." And S8:
at the registered run the clause cannot be evaluated (there is no battery, no
data, no line), so the channel-removal gate counts as failed for the free
model, and the free model is not read. Then the first registered outcome,
"metric validated, degree read", cannot be reached by any result whatever.
That is the shape of the closed design's unsatisfiable clause: a registered
sentence nobody can satisfy, carried in plain sight.

**One honest doubt, stated.** Version 4's grammar section says the successor
grammar "extends" the closed design's grammar (line 498), which does have
these batteries. If the registered generator kept them, the clause could be
evaluated. But nothing in version 4 says the batteries are kept, the rehearsal
grammar dropped them, the clause still sets no line for "hold", and no record
exercised it on any model of this design, so the finding stands either way
(and RT-239 is about the same unstated grammar).

**What would fix it (a suggestion).** Either John rules the clause out, with
its reason on the record (it was written for a grammar this design no longer
uses), or the registration defines the batteries in the successor's grammar,
sets the line for "hold", and a rehearsal run on the committed toy models
exercises it. The closure check is then a search showing the clause gone, or
the rehearsal record with the figure.

**On the known-failure list.** This is a pre-stated gate the design cannot
evaluate on the path it expects. It is closest to the drafted seventh entry,
"an outcome line a plan states in advance that the design cannot produce on
the path it expects" (version 4, section 17), which John has not yet ruled
onto the list, and to failure 3, part three. The protocol asks the pass that
finds a fatal finding of a new kind to add it to the list; this session was
told not to edit the list, so the test is written here for whoever does:
*for every clause of every gate, name the field of a committed rehearsal
output file that evaluates it, and print that field; a clause with no field
is the finding.*

### RT-238 (serious, MEASURED). The whole-state floor as printed admits a zero or negative divisor

**What version 4 says.** Section 6.4, item 1 (lines 1113 to 1132): "A site set
is usable only if the whole-state transplant clears four fifths of the arm's
own own-directed accuracy ... written on the chance-corrected scale:
`accuracy_whole − accuracy_untouched ≥ 0.8 × (own_directed_accuracy −
accuracy_untouched)` ... The floor keeps the denominator away from zero by
construction: on an arm that has learned the task, `own_directed_accuracy −
accuracy_untouched` is large, and the denominator is at least four fifths of
it." The section 9 row (line 2261) states the floor the same way.

**What the code does.** `experiments/rehearsal-successor-measure/src/repairs.py`,
`floor_check` (line 276): `clears=bool(whole - untouched >= need and need >
0)`. The second clause, that the requirement itself is above zero, is in no
sentence of version 4.

**What was measured.** `rule_from_text.py`, section 4, applies the floor as
printed and the floor as coded to the committed development grids of the
ordinary competing solver (the ownership-blind model, which version 4 now puts
through the measure):

```
seed 0, channel_removed: own-directed 0.2333, untouched 0.2400, floor asks for -0.0053; whole - untouched over the family: +0.0000 to +0.0000
    text's floor: 45 of 45 site sets clear -> read failed its floor: no size's piece reaches four fifths
    code's floor: 0 of 45 site sets clear -> no site set clears the whole-state floor   (committed: no site set clears the whole-state floor)
seed 0, channel_left_on: own-directed 0.2383, untouched 0.2417, floor asks for -0.0027; whole - untouched over the family: -0.0017 to +0.0017
    text's floor: 45 of 45 site sets clear -> read failed its floor: no size's piece reaches four fifths
    code's floor: 0 of 45 site sets clear -> no site set clears the whole-state floor   (committed: no site set clears the whole-state floor)
seed 1, channel_removed: ... floor asks for -0.0160; whole - untouched over the family: +0.0000 to +0.0000
    text's floor: 45 of 45 site sets clear -> read failed its floor ...
seed 1, channel_left_on: ... floor asks for -0.0160; whole - untouched over the family: +0.0000 to +0.0033
    text's floor: 45 of 45 site sets clear -> read failed its floor ...
seed 2, both readings: floor asks for +0.0027 and +0.0053 -> text and code agree: 0 of 45
```

(full output in `rule_from_text.out.txt`). On four of the six runs the printed
rule admits every site set with a divisor of exactly zero, or as low as
−0.0017. What then refuses the solver is the piece rule (best piece 20 to 25
of 180). Had a model at chance held a readable label, the printed rule would
have gone on to divide by zero.

**Does it change any toy verdict?** No: the solver's verdict is no verdict
under both, and on all twelve arm models the requirement is well above zero.
It changes the stated reason, and with it the sentence John ruled into the
text on 2026-10-04 ("no site set cleared the floor at nomination"), which is
true under the code and false under the text.

**Why serious and not worth-noting.** The registered code is still to be
written (section 11, step 3), and it is written from the registration text.
The text's floor is the place the design says keeps the divisor off zero
"by construction", which is the claim failure 1 of the known-failure list
exists to test; it holds only on models that have learned the task, and the
competing solver, which the rehearsal requires the measure to face, has not.
The check of pull requests 88 and 89 (its section 5.4) found the same
dependence from the other side: on a real arm the divisor is kept large by
the floor *together with* the gate and the no-transplant rule.

**What would fix it.** Write the code's clause into section 6.4, item 1, and
the section 9 row: a site set is usable only if the requirement is above
zero (equivalently, the model's own-directed accuracy is above its
no-transplant rate on those episodes), and say that otherwise the arm
returns "no verdict: floor not defined". Then the ruled sentence about the
solver is true as written.

### RT-240 (serious, MEASURED on a stand-in; NOT A RESULT). The ruled episode counts were rehearsed only at the toy's width

**What version 4 says.** Ruled 2026-10-03, late evening (record A ruling 4,
record B ruling 4): the registered measurement uses the toy's counts, 600
development episodes with the last 180 held out, so every read is fitted on
420 (lines 2067 to 2071; section 9, line 2276). The read is scikit-learn's
logistic regression on the running state (line 1335). The caution carried with
the ruling is about sampling at 180 held-out episodes. Nothing is said about
width.

**Why width matters (ARGUED).** The toy's running state is 160 wide
(`arms.Config`, `d_model: int = 160`); the registered model's is 448
(`bench_arms.py`, `REGISTERED_SHAPE`). The read has twelve answers. At 160
there are fewer coordinates than the 420 fitting episodes; at 448 there are
more, and a twelve-way read on 448 coordinates from 420 episodes is in the
regime where a straight-line read can fit its training episodes by chance and
generalise worse. The floor is a hard line on the held-out count.

**What was measured, on a stand-in.** `width_vs_count.py` loads committed toy
models, takes the state at the chosen layer at the action position on the 600
development episodes, and appends 288 coordinates of independent noise (scaled
to the state's own median coordinate spread) to make it 448 wide, then fits the
registered read the registered way. Five noise draws per model:

```
arm/seed layer | width 160: whole read, piece of 8 | width 448 (288 noise coords), five noise draws: whole read; piece of 8
C/0 layer 2 | 180, 180 | [147, 156, 159, 156, 162]; [163, 157, 166, 157, 158]  (noise scale 7.941)
C/1 layer 1 | 177, 172 | [91, 94, 89, 90, 92]; [80, 88, 79, 76, 85]  (noise scale 2.250)
C/2 layer 1 | 176, 178 | [123, 134, 132, 126, 130]; [128, 132, 134, 126, 138]  (noise scale 2.929)
M/0 layer 1 | 180, 180 | [180, 180, 180, 179, 180]; [180, 180, 180, 180, 180]  (noise scale 2.048)
T/0 layer 1 | 180, 180 | [180, 180, 180, 180, 180]; [180, 180, 180, 180, 180]  (noise scale 0.648)
floor: 144 of 180. NOT A RESULT: a stand-in for width, with independent noise in place of a wider model's own coordinates.
```

**What it shows, and what it does not.** On the two built models whose label
sits in a clean slot (T and M), width costs nothing. On the entangled model,
whose label is spread through the state, two seeds of three fall well under
144 and the third keeps a margin of 3 to 18 episodes. A wider model's extra
coordinates are not independent noise; they carry structured content, which
could hurt more or less than this. So this is not a forecast. It is a measured
reason to think the ruled counts, which were chosen because they are "the only
counts the procedure has been rehearsed at", have not been rehearsed at the
size where they will be used, and that the arm most at risk is the high anchor
(and, behind it, the free model the floor exists for).

**The consequence (ARGUED).** An entangled model whose read misses the floor
returns "no verdict, read failed its floor", which fires the two-model
fallback, which has no registered outcome term (RT-241), and which is first
seen after both releases of money are drawn (section 11, step 5b).

**What would fix it.** Any one of: (a) the alternative John was offered and did
not take, more development episodes, sized against the registered width (for
instance several times 448 fitting episodes); (b) the read's regularisation
fixed in advance for the registered width, with the toy re-fitted under it;
(c) a rehearsal of the read at width 448, on a stand-in model trained at the
registered shape on the laptop or on the development runs of step 4, before
registration. At the least, a weakness in section 13 saying the counts were
rehearsed at width 160 only.

### RT-245 (worth-noting, MEASURED). The registered nomination on the laptop's processor is argued, not timed; the device ruling covers the fit, not the choice

**What version 4 says.** Section 11, step 5a (lines 2520 to 2524): "The fit is
computed on the laptop from the fetched checkpoint ... (ARGUED: a
30-million-parameter model's activations on development episodes fit on the
laptop ...)". Section 7.2, item 1 (lines 1332 to 1355): the registered fit is
computed on the processor.

===== END OF RECORD 5, part 2 =====

