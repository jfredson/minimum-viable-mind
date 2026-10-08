# Gate A tier 1 review of the successor experiment's registration text (proposal version 4 and the changes ruled into it) — RT-237 to RT-246

*Written 2026-10-04 (Pacific) by a Claude Code session on branch
`gate-a-tier1-successor-v4`, cut from the main line at `d19f914` (the merge of
pull request 91, John's ruling on the competing-solver run and the
twenty-piece control). Filed under this experiment's reviews directory because
the successor experiment has no directory of its own yet, and this is the
experiment its text most affects (`docs/outside-review-protocol.md`, "The
pairing rule", the filing fallback).*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (a command was run, and the command and its output are below or
in the scripts folder beside this file) or **ARGUED** (reasoning a reader can
dispute), and carries a severity: **fatal**, **serious** or **worth-noting**.
Findings continue the red-team ledger's numbering. The last number used
anywhere in the repository at `d19f914` is RT-236 (the review of version 3);
`git grep -nE "RT-2(3[7-9]|[4-9][0-9])" d19f914` returns nothing. No ledger row
is written here: rows are written when John rules.*

**Nothing was rented, created or spent: $0.** Laptop only, on its processor.
No registered text, ruling file, protocol text, known-failure list, ledger,
earlier review or proposal text was edited. The scripts beside this file read
committed output files, load committed toy models, fit small straight-line
reads and time forward passes; they train no model. One of them ran the
controls re-run's committed code again, from a copy whose output folder points
into this session's scratch space, so nothing committed was overwritten.

**How isolated this session was, said plainly.** It is a fresh session in its
own git worktree. It has no chat history: it has not seen the chat of any
session that wrote version 4, the rulings, the runs or their checks, and it
worked only from committed files. It wrote none of what it reviews.

---

## Verdict in one paragraph

**One fatal finding, four serious, five worth-noting.** The fatal one is small
to fix and large if left: the gate that decides whether the freely trained
model may be read at all includes the clause "the ownership-free state and
syntax batteries must hold" (version 4, line 2223, frozen by line 2064 and the
section 9 row at line 2270). The successor's task has no such batteries, the
clause names no line for "hold", and no rehearsal record ever exercised it; the
design's own stop condition S8 (lines 2599 to 2602) says a gate that cannot be
evaluated counts as failed and its consequence fires. Registered as written,
the freely trained model could never be read, so the first outcome, "metric
validated, degree read", could never be reached (RT-237). The serious ones: the
whole-state floor as printed admits a zero or negative divisor for a model at
chance, which only an unwritten clause in the code prevents (RT-238); the task
grammar is described as an extension of the closed design's grammar, which
puts the model's own name in front of it at the moment it acts, and the two
deliberate departures that remove that cue are written nowhere in the
registration text (RT-239); the ruled episode counts were rehearsed only at the
toy's width, and a stand-in at the registered width drops the entangled
model's read below the four-fifths floor on two of three seeds (RT-240); and
the outcome map has holes, with no registered term for a no verdict on the
separable model or for the two-model fallback (RT-241). **What held, and it is
the most important thing this review measured:** the nomination rule written
from version 4's text alone, by code that imports none of the checked code,
picks exactly the site set, size and verdict the committed code picked on all
twenty-four toy rows (twelve primary, twelve stricter), reproduces every toy
reading, and lands the toy on the fifth outcome term with a separation of
0.9926; and the committed code, run again from clean on this laptop today,
reproduces its committed outputs value for value (26,722 values in 25 files,
none different; the table identical). The registration text
describes the instrument that ran. It is not ready to register until RT-237 is
closed and the serious findings are closed or carried as named open items with
John's reasons.

---

## What this review opened, and what it did not

**Opened and read in full, in this order.** `CLAUDE.md` at the repository root;
the workspace plain-language rule in `~/Code/CLAUDE.md` (as loaded into this
session); `docs/outside-review-protocol.md`; the measurement rehearsal record
`docs/2026-09-21-successor-measure-rehearsal.md` (the first thing read after
the protocol, as the protocol requires); the target,
`docs/successor-experiment-proposal-2026-10-03-v4.md` at `d19f914`, all 4,219
lines; the rulings `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`
(record A of the seven-question ruling), `docs/rulings/2026-10-03-version-4-questions-rulings.md`
(record B), `docs/rulings/2026-10-03-seven-questions-reconciliation.md`,
`docs/rulings/2026-10-03-version-4-check-questions-rulings.md` and
`docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`; the check
of version 4, `reviews/2026-10-03-proposal-v4-check-claude-code.md`; the check
of the competing-solver run and the twenty-piece control,
`reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md`; the
findings of those two runs, `docs/2026-10-03-competing-solver-run.md` and
`docs/2026-10-03-control-2-twenty-draws.md`; `docs/known-failure-modes.md`.

**Opened in part, to look up a sentence, a figure or a function.** The morning
rulings of 2026-10-03 (page 11, what a no verdict maps to); the Weekend 1 queue
ruling (page 1h, the channel-removal check) and its packet (the 1h page); the
December-result roadmap's outcome table; `docs/2026-09-26-free-arm-label-search.md`
(its verdicts table); the label-search output folder; version 1 of the proposal
(one line, where the batteries clause first appears); versions 2 and 3 (by
search, for that clause and for the label-search sentence); Amendment A3
(`amendment-a3.md`, by search for its batteries); the closed design's grammar
`experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py` (its
header); the rehearsal grammar `experiments/rehearsal-successor-measure/src/grammar.py`
(its header and constants); the toy code the runs use (`rerun_controls.py` in
full; in `repairs.py` the floor, the reading and the masks; in `rerun_v3.py`
the paths and the model loader; `rehearse.basis_for`; `transplant.py`'s
signatures; `arms.Config`; `bench_arms.py`'s header); the two launcher checks
and the launcher's dry-run path (read before running, to be sure they create
nothing); the grammar attempt's check (one line); every committed output file
the scripts below name; the reviews directory's file list and the red-team
ledger's last lines (for numbering).

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

**What was measured.** `registered_shape_timing.py` times, on this laptop's
processor (Apple M4), the forward passes the rule makes over the 600
development pairs, at the toy shape and at the registered shape:

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-scripts/registered_shape_timing.py
torch 2.12.1, threads 4, sequence 56, pairs 600
toy shape (160 wide, 4 blocks): 1,265,191 parameters; capture 0.52 s; one transplant pass over 600 pairs 0.506 s (median of 6); one read fit 0.02 s
   nomination grid: 45 site sets -> 227 passes, 25 fits -> about 1.9 minutes per model and seed (control 2's own grid, where it runs, about doubles it)
registered shape (448 wide, 12 blocks): 29,049,735 parameters; capture 6.55 s; one transplant pass over 600 pairs 4.590 s (median of 6); one read fit 0.09 s
   nomination grid: 325 site sets -> 1627 passes, 65 fits -> about 124.6 minutes per model and seed (control 2's own grid, where it runs, about doubles it)
registered against toy, per model and seed: 65 times
twelve registered models, nomination grids only: about 24.9 hours on this processor
```

**What it shows.** The arithmetic is honest at the toy end: it predicts
about 1.9 minutes per toy model, and the controls re-run this session ran took
1,485 seconds for twelve models with every control, about 2 minutes each. At
the registered shape one model's nomination is about two hours on this
processor; the twelve registered models about a day, more where control 2 runs
its own grid, and more again if the registered episodes are longer than the
toy's 56 tokens (no text fixes that length). So the text's argument holds:
the work fits on the laptop, at a day or two of processor time and $0, and
step 5a's single free-model run is about two hours. It is now a measurement
rather than an argument. One limit: the read was timed on random labels and
may take longer on real ones; it is a small share of the total either way.

**The second half (ARGUED).** Ruling 3 of record B names the device for "the
registered accuracy", the fit. The nomination also chooses among candidate
site sets by their development ownership-only shares, and on the entangled
model seed 1 that choice was decided by one episode in 600 (version 4, lines
776 to 782). A transplant pass on a different device or number format can move
a share by an episode just as a fit can (RT-232 was exactly that for fits). If
the registration names the device for the fit and not for the transplant
passes, the stop at step 5a and every nomination can turn on an unregistered
choice. *Suggestion:* name the device and number format for the whole
nomination and reading, not only for the fit, and carry the timing above (or
the step-4 development runs' own timing) as the measurement behind "it fits on
the laptop".

---

## 2. Satisfied by the wrong thing

| Way the text could be satisfied by a model with none of the structure it claims to detect | Severity | Finding |
|---|---|---|
| A free model reads its own name off the text near the action, if the registered grammar keeps the closed design's rendering, and clears the fit floor through a name cue rather than a carried answer | serious | RT-239 |
| The high anchor reads near 1 through any piece that holds the label and does nothing, which is what "entangled" means operationally; the reading cannot tell entangled from "the answer lives where the read did not look" | (stated by version 4 as weakness W12; not re-filed) | — |
| The whole-state transplant on the entangled and mixed models moves the action even when the donor's identity dictates the same value (control 6), so it carries more than identity | (stated as W11; not re-filed) | — |
| A model at chance passes the printed whole-state floor at every site set | serious | RT-238 |
| The competing-solver test covers a model that fails the task; the toy's free model is a model that does the task by another route, and the weakness ruled on 2026-10-04 does not say so | worth-noting | RT-246 |

### RT-239 (serious; MEASURED that the texts say what is quoted, ARGUED for the consequence). The registration does not state the grammar that removes the model's own name from the act

**What version 4 says.** Section 4.1 (lines 498 to 504): "The grammar extends
the registered Amendment A3 grammar (`curriculum_a3.py`, the episode generator
committed 2026-09-15), which already has the pieces: four agents, a closed
vocabulary, ten turns, eight value slots, every revised item assigned by all
four agents before anyone revises it ... The rehearsal's shrunken version of
it is `experiments/rehearsal-successor-measure/src/grammar.py`." Line 522:
"The grammar is as version 2 had it." Section 1 (lines 133 to 141): the acting
channel "is the only honest source of ownership in this design, because ...
nothing in the text itself can carry it". Section 7.3, item 4 (lines 1890 to
1896): "The twins are the same text. They differ only in which turns carry the
acting channel."

**What the two grammars say about themselves.** The closed design's grammar,
`experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py`, header:
"Twelve turns, four agents, two *contested* items: ... Eight assignment turns
... Four revision turns"; and, under "An honest limit on the design's central
claim": "The revision turn renders as "<marker> assign <item> to <value>", so
at the moment the model acts, its own marker is in the context three tokens
back. A model could learn "the marker at a position where I am acting is
mine" ... reading a name badge at act time rather than carrying a binding."
The rehearsal grammar, `grammar.py`, header, "Two departures from the
registered A3 grammar, both deliberate": "1. **The action turn carries no
marker word.** ... Here the only route to the ownership answer is the acting
channel. 2. **The answer token is never shown.** ... Together these make a
matched pair of episodes ... come out **token-for-token identical**, differing
only in which positions the acting channel fires on."

```
$ grep -n -i "mask\b\|<mask>\|name badge\|no marker word\|carries no marker\|departure\|token-for-token\|answer token\|same text" docs/successor-experiment-proposal-2026-10-03-v4.md
1534:   the running state at the mask token of the own-directed action (the
3271:    at the mask token, scored on held-out development episodes; the label
```

So: version 4 says the closed design's grammar has ten turns; it has twelve.
And the two departures that make the act free of the model's own name, and
make the twins the same text, appear in version 4 only as two passing
mentions of "the mask token".

**Why this matters (ARGUED).** The registered generator is still to be written
(section 11, step 3, "the built generator"), and it is written from the
registration text. Read as written, the text points at the closed design's
generator as the base and at the rehearsal's as its shrunken copy, and only
the shrunken copy says the departures exist. A generator built by extending
`curriculum_a3.py` as the text says would show the model its own marker word
three tokens before it acts. Then: the registered read's label, "which marker
word is the model's own", is in the text near the action, so a free model can
clear the fit floor by copying a name rather than by carrying an answer; the
twins are no longer the same text, so the known-answer reasoning of control 4
and of section 6.1 no longer holds as stated; and the ownership signal the
whole design is built to isolate (ledger item RT-17, the finding that any
learnable ownership cue in the tokens is a fingerprint) is back. That is a
reading satisfied by the wrong thing, on the one model the experiment exists
to read.

**What would fix it.** Register the episode format itself, as the rehearsal
grammar's header gives it: the turns and their order, the action-turn
rendering with no marker word, the masked answer, and the property that twins
are token-for-token identical, with the self-test that asserts it named as
part of the registered generator's tests. Correct "ten turns" as a statement
about the closed design's grammar. Say whether the closed design's
end-of-episode question sets are carried (this decides RT-237's doubt).

### RT-246 (worth-noting, ARGUED). The ruled weakness about the competing solver can be stated more exactly

John ruled (2026-10-04, ruling 7) that section 13 gains: "the toy's ordinary
competing solver fails the task, so its 'no verdict' shows only that the
measure returns nothing on a model that has not learned the task. It does not
show what the measure does on a model that does the task by another route."

The toy has such a model: the free model. Version 4, section 5.4 (lines 986 to
999): it scores 0.5513 to 0.5597 on the own-directed condition against 0.2340
to 0.2383 for the ownership-blind solver, and solves it "by attending to the
value tokens on the turns the acting channel marked, with no need to know
which marker word those turns carry", and "the free toy model does not carry
the marker word forward to where it acts". The measure returns no verdict on
it ("read failed its floor"). So the toy does show what the measure does on
one model that does the task by a route other than carrying the registered
label: it returns nothing, and says why. What the toy does not show is a model
that does the task by a route that *also* leaves the label readable where the
model acts, and the obvious such route is the name cue of RT-239. *Suggestion:*
write the weakness with both halves, so a reader learns which "other route"
has been seen and which has not.

---

## 3. No verdict

| Way the registration text could fail to return a verdict on the runs it is written for | Severity | Finding |
|---|---|---|
| The free model's gate cannot be evaluated, so it fails by S8 and the free model is never read | fatal | RT-237 |
| A no verdict on the separable model, or the two-model fallback, has no registered outcome term | serious | RT-241 |
| The entangled model's read misses the floor at the registered width | serious | RT-240 |
| A model at chance reaches the arithmetic with a divisor of zero under the printed floor | serious | RT-238 |
| The processor proves impractical at full size (record B: a fresh question for John) | worth-noting | RT-245 |

### RT-241 (serious, ARGUED). The outcome map has holes

**What version 4 says.** The outcome table (lines 307 to 313); "What a no
verdict maps to" (lines 456 to 467): arm C fires the two-model fallback, arm M
is dropped, arm F after T and C separate is the fifth term; section 7.4 freezes
"the five registered outcome terms of section 3, and what a no verdict on each
arm maps to" (lines 2061 to 2062). Section 8.1 (lines 2188 to 2189): "An arm
that fails, after the one permitted re-run, gives outcome R3 for that arm".
Line 305: "nothing in this document may report an outcome in other words."

**The holes, each a state the registered runs can reach.**

1. **No verdict on arm T, the separable model.** Not in the list of three.
   It can happen: arm T's reading is withheld if control 1 fails on it (a
   control that holds on arm T only), if its no-transplant rate misses, or if
   its floor is missed on fresh episodes. With arm T reading on fewer than two
   seeds, "metric validated" cannot be met (lines 481 to 483), R2 is not met (the
   measure did not fail to separate; it was not computed), R3 is not met (no
   gate failed), and no other term applies. Section 7.4 says the frozen list
   covers "each arm"; it covers three.
2. **The two-model fallback has no term.** A no verdict on arm C "fires the
   two-arm fallback" (line 462). Then R1 and R2 both require separating arms
   T and C, which cannot be done. Lines 820 to 827 say "the R1 sentence is
   correspondingly weaker" and that the registration "says that in those
   words", but no words are registered, and line 305 forbids reporting in
   other words.
3. **"R3 for that arm" against R3 as the experiment's outcome.** R3 in the
   table is the whole experiment's outcome ("this recipe and this size are not
   yet a place to study mechanism"). Line 2188 makes a gate failure "R3 for
   that arm". A gate failure on arm M, a model whose no verdict merely drops
   it, would then be read either as the whole experiment's R3 or as an
   arm-level R3 that the table does not define.
4. **The free model fails its channel-removal check** (fewer than two seeds
   collapse; or RT-237's clause). Section 5.4 says it is then not read. Which
   term follows is not said: R3 if this check is a "gate" (section 8 calls it
   one), the fifth term if it counts as a no verdict.
5. **A built model that fails its gate in step 5b.** R3 is "after the one
   permitted re-run". On the ruled split the re-run is funded only in the first
   release (section 12.3; section 12.4 removes it from the second), and step
   5a's text gives it to the free model. Whether a separable, entangled or
   mixed model that fails at step 5b gets a re-run before R3 is declared, and
   from what money, is not stated.

**What would fix it.** One table in section 3, frozen in section 7.4, with a
row for every arm-level state (reads; no verdict; fails its gate after a
re-run; fails the channel-removal check, for arm F) and the registered term
each combination gives, including the fallback's own term. The ruling that
created the fifth term (2026-10-03, page 11) is the precedent: it closed the
same kind of hole (RT-182, the no-verdict finding on version 1) for three arms
and not the fourth.

---

## 4. Over-reading

| What a result could be read as claiming beyond what it measures | Severity | Finding |
|---|---|---|
| "The label search's three candidates reach 0.733, 0.383 and 0.478" read as three candidates' figures | worth-noting | RT-242 |
| "The two forms of the floor never disagree on the toy" read as a property of the toy, when it holds only where the models have learned the task | worth-noting | RT-243 |
| The ruled sentence about the competing solver's misses | worth-noting | RT-244 |
| "Metric validated" read as validation of a measure of degree in general; it is validation at the sites the procedure nominates, on built models that differ in more than degree, with a middle anchor that is a mixture by item | (stated by version 4 as W1, W2, W10; ARGUED here that the outcome term's own words invite the reading, and the registered report should carry W1's hedge in the same sentence as the term) | — |

### RT-242 (worth-noting, MEASURED). The label-search sentence quotes one candidate's three seeds as three candidates

Version 4, lines 1384 to 1389: "The best is 0.789, from candidate 1 ... and
that from position spans that start at one of the model's own turns ...;
anchored at the action position the three candidates reach 0.733, 0.383 and
0.478." The findings table it cites (`docs/2026-09-26-free-arm-label-search.md`,
section 4) has, for candidate 1 on the free model, "0.733 / 0.483 / 0.789 |
0.733 / 0.383 / 0.478", where the two cells are the best over all 60 site sets
and over the 45 fixed-extent ones, each given as seeds 0 / 1 / 2. From the
committed verdict files (`older_figures.py`):

```
  own-turn-pair    best over all 60 site sets 0.789; best over the fixed-extent 45 0.733; per seed [0.733, 0.483, 0.789]; clears: False
  own-source-turn  best over all 60 site sets 0.456; best over the fixed-extent 45 0.417; per seed [0.45, 0.45, 0.456]; clears: False
  own-value        best over all 60 site sets 0.633; best over the fixed-extent 45 0.633; per seed [0.611, 0.611, 0.633]; clears: False
```

So 0.733, 0.383 and 0.478 are candidate 1 on seeds 0, 1 and 2; the three
candidates' best over those site sets are 0.733, 0.417 and 0.633. The sentence
was carried from version 3 (line 1105). Nothing ruled rests on it and every
figure stays under 0.80. *Fix:* "anchored at the action position, candidate 1
reaches 0.733, 0.383 and 0.478 on seeds 0, 1 and 2, and candidates 2 and 3 at
most 0.417 and 0.633."

### RT-243 (worth-noting, MEASURED). The two forms of the whole-state floor do disagree on the toy, on models near chance

Version 4, lines 1118 to 1125: the plain form "is printed beside it everywhere,
so a reader can see whether the two readings of the ruled sentence ever
disagree; on the toy they never did (MEASURED: 0 disagreements across all site
sets, arms and seeds, the repairs findings at `882f252`, section 3 ...)".
`floor_forms.py` counts every committed floor record that carries both forms:

```
out-repairs/nominate_base_*.json              floor records   4254; the two forms disagree on 576
out-v3-rules/nominate_*.json                  floor records   3672; the two forms disagree on 0
out-controls-rerun/nominate_*.json            floor records   2160; the two forms disagree on 0
out-grammar-c/nominate_base_F_T_C.json        floor records   3188; the two forms disagree on 892
out-competing-solver-run/nominate_*.json      floor records   1080; the two forms disagree on 1080
```

(and 0 in every measurement file). All 576 of the repairs run's disagreements
are in the other-agent control's grids on arms C and F (the named-other
condition, near chance on those models); none is in the own-directed grids
the repairs findings counted. On the competing solver the plain form passes
every row and the registered form none. Each disagreement is the plain form
passing a model near chance. So the sentence is right about the own-directed
grids of the twelve base models, wrong about "the toy", and the record it
misses is the best evidence for the choice the design made: the plain form
would let a model at chance through. *Fix:* narrow the sentence and cite the
disagreements as the reason the corrected form is registered.

### RT-244 (worth-noting, MEASURED). The ruled sentence about the competing solver gets one of its own figures wrong

The sentence ruled into the registration text on 2026-10-04 (ruling 2):
"... its best piece missed the piece rule by 119 or more of 180 and its
untouched rate missed the no-transplant rule by 0.11 or more ...".
`solver_sentence.py` against the committed outputs:

```
piece rule missed by: 119 to 124 of 180  -> '119 or more': True
untouched rate against the formula: 0.1091 to 0.1393  -> '0.11 or more': False
untouched rate beyond the rule's room: 0.0911 to 0.1213  -> '0.11 or more': False
```

The run's own findings had already corrected the same slip in one place
(commit `3d55865`, which the check of pull requests 88 and 89 confirms: "outside
the allowance it is 0.09 to 0.12"); the check's suggested sentence, which John
adopted, reintroduced it. And its first clause, "no site set cleared the floor
at nomination", is true under the code's floor and false under the floor as
version 4 prints it (RT-238). *Fix:* "its untouched rate was 0.109 or more
above the formula, and 0.09 or more outside the rule's allowance", and close
RT-238 so the first clause is true of the text.

---

## The failure-mode pass

One section per entry of `docs/known-failure-modes.md`, in order. Each shows
the command run by this session and what it returned. The author's own pass
(version 4, section 17) was read after this pass was run; nothing below is
copied from it.

### Failure 1. A comparison whose denominator was zero — **fires on the printed floor for a model at chance (RT-238); does not fire on any model that learned the task**

*Part one, where every no-transplant rate comes from.* `failure_mode_pass.py`
prints each of the twelve, with the file and field it was read from
(`out-controls-rerun/measure_{arm}_seed{seed}.json`, `primary.reading`): T 0.0000
on every seed; C 0.0512, 0.0488, 0.0600; F 0.0587, 0.0563, 0.0688; M 0.0125,
0.0175, 0.0138. None is typed in; each is measured.

*Part two, the divisor and the top of the scale at the chosen site set:*

```
  T/0: denominator 1.0000; top of scale 1.0000; reads        (and T/1, T/2 the same)
  C/0: denominator 0.4888; top of scale 1.0000; reads
  C/1: denominator 0.5063; top of scale 1.0000; reads
  C/2: denominator 0.4863; top of scale 1.0000; reads
  F/0: denominator 0.4263; top of scale 1.0000; described only
  F/1: denominator 0.5112; top of scale 1.0000; described only
  F/2: denominator 0.4613; top of scale 1.0000; described only
  M/0: denominator 0.7675; top of scale 1.0000; reads
  M/1: denominator 0.7563; top of scale 1.0000; reads
  M/2: denominator 0.7800; top of scale 1.0000; reads
  smallest denominator among those that read: (0.48625, 'C/2')
```

*The case the printed floor admits:*

```
  solver seed 0 channel_removed : floor asks -0.0053; rows the printed formula admits 180 of 180; denominators among them +0.0000 to +0.0000
  solver seed 0 channel_left_on : floor asks -0.0027; rows the printed formula admits 180 of 180; denominators among them -0.0017 to +0.0017
  solver seed 1 channel_removed : floor asks -0.0160; rows the printed formula admits 180 of 180; denominators among them +0.0000 to +0.0000
  solver seed 1 channel_left_on : floor asks -0.0160; rows the printed formula admits 180 of 180; denominators among them +0.0000 to +0.0033
  solver seed 2 channel_removed : floor asks +0.0027; rows the printed formula admits 0 of 180
  solver seed 2 channel_left_on : floor asks +0.0053; rows the printed formula admits 0 of 180
```

**Disposition.** The top of the scale is the same, 1, on every arm, and the
smallest divisor among the models that read is 0.4863: the per-arm-ceiling
repair (ledger item RT-172) holds. The entry fires on the floor's printed
formula, which admits a divisor of zero or below on a model whose own-directed
accuracy is at or under its no-transplant rate: RT-238.

### Failure 2. A probe target that cannot be recovered in principle — **fires on the free model, and a registered rule catches it**

*Part one, a route sentence, in this design's own words, sections 0 to 16:*

```
  1277: own**. *The route by which that quantity reaches the model's states, in one
  1278: sentence:* the marker word is the input token at every turn the model's own
  1279: assignments are spoken on, so it is carried by the token into the running
  1283: claim, that which marker word is the model's own is forced by the loss at
```

(Line numbers are those of `git show d19f914:...`, which counts from the same
file; the fourth match is the sentence striking version 2's loss claim, not a
route.) A route sentence exists, and it names the token. It names a route to
the state at the model's own assignment turns; it does not name one to the
action position, where the registered read is fitted.

*Part two, the same read and the same bar at the position where the marker
word is the input token, and at the registered action position* (from the
short pre-stated run's committed `part_b.json`; the toy has no separate run of
the first kind, so this is the nearest committed pair of runs):

```
  C/2: whole state at the marker's own token 180; whole read at the action position 176 -> both clear
  F/0: whole state at the marker's own token 180; whole read at the action position 32 -> second clears, first does not
  F/2: whole state at the marker's own token 180; whole read at the action position 18 -> second clears, first does not
  M/0: whole state at the marker's own token 180; whole read at the action position 180 -> both clear
  (T, C/0, C/1 and F/1 have a single-position site and the first own turn is not reported for them;
   their action-position counts are 180, 180, 177 and 12)
  the named agent's read (control 2) on arm F seed 0, per running state (whole, best piece):
    {'0': (16, 20), '1': (95, 92), '2': (137, 139), '3': (127, 115), '4': (102, 102)} -> best 139 of 144 needed
```

**Disposition.** The middle limb, "the second run clears the bar and the first
does not", is the free model's state: the label is fully in the state where it
is spoken and absent where the model acts. This is the fatal finding of the
review of version 2 (RT-212, the empty read on the free model), still firing.
The design catches it, not repairs it: the fit floor on the piece turns it
into a registered "no verdict, read failed its floor", the number the
arithmetic would have returned is withdrawn, and the route (b) search found no
other label at the floor. The same limb fires on control 2's named-agent read
(139 against 144), which carries no line by ruling. Nothing new fires here;
what is new is that the route sentence would change if RT-239 were left open
(the marker word could then also be "the input token" three tokens before the
action).

### Failure 3. A cell that is empty by construction — **fires on one gate clause (RT-237); not on any reported cell**

*Part one, every pre-stated cell, counted:*

```
  control 6, T/0: same-value 81, different-value 719        (C/0, F/0, M/0 the same; every seed the same, per section 17's own block)
  control 4 as redefined, positions per pair: {'max': 21, 'mean': 5.212500095367432, 'min': 1}
  control 2: toy models on which it returned a figure: 0 of 12
  the two-of-three rule: arms whose three seeds disagree on the toy: 0 of 4
  the lesion clause 'the ownership-free state and syntax batteries must hold': fields the gate file records: ['lesion_collapses_own', 'lesioned_other', 'lesioned_own', 'n', 'other', 'other_clears', 'other_correct', 'own', 'own_by_route', 'own_clears', 'own_correct']
  grep of the rehearsal code for a state or syntax battery: (no file)
```

*Part two, the generator property that empties a cell.* Distinct values per
item, drawn without replacement (`grammar.py`, `_content`, `replace=False`),
which is why control 6 runs on the separately generated relaxed set; its 0 of
4,000 on the distinct grammar recomputes from `out/denominator_control6.json`
(`older_figures.out.txt`).

*Part three, every threshold at both ends:*

```
  gate bar 790 of 3,000; a model at one in four clears it with probability 0.0485
  no-transplant rule at own-directed 1.0: formula 0.0000; a broken pairing (0.125) flagged: True
  no-transplant rule at own-directed 0.8712: formula 0.0184; a broken pairing (0.125) flagged: True
  no-transplant rule at own-directed 0.56: formula 0.0629; a broken pairing (0.125) flagged: True
  no-transplant rule at own-directed 0.2633: formula 0.1052; a broken pairing (0.125) flagged: True
  piece floor at 144 of 180: the competing solver's best piece 20 to 25, arm F's 34, the built arms' chosen pieces 150 to 180
  whole-state floor, printed formula, at the broken end (solver seeds 0 and 1): admits every site set (above)
```

**Disposition.** Control 6's two cells have trials on every arm and seed (the
empty-cell repair, ledger item RT-173, holds). Control 4 transplants at one
position or more in every pair. Control 2's cell is empty on the toy and the
text says so; it carries no line, by ruling. The two-of-three rule has never
been exercised and the text says so. **The channel-removal gate's battery
clause has no cell at all, in any record: RT-237.** At both ends: the gate,
the no-transplant rule and the piece floor pass the working end and refuse
the broken end; **the whole-state floor as printed passes the broken end
(RT-238).** Control 4's pass line has no working end to test, which version 4
already says.

### Failure 4. A claim of measurement with no record, or a record that does not reproduce — **fires twice, on two worth-noting sentences (RT-242, RT-243)**

*Part one, the two sweeps* (on sections 0 to 16 at `d19f914`, cut at
section 17's heading):

```
$ git show d19f914:docs/successor-experiment-proposal-2026-10-03-v4.md | awk '/^## 17\. /{exit} {print}' > v4-through16.md
$ grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' v4-through16.md
761
$ grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' v4-through16.md
235
$ wc -l < v4-through16.md
3449
```

(Section 17 prints 759, 233 and 3,406, from before the late-evening rulings
were written in; the check of version 4 found the same 761 and 235. The
hits were read through the closure rule's own narrower question, next.)

and the closure rule's own check, every paragraph using verified, measured,
calibrated or attacked, and whether it names a record (`closure_sentences.py`):

```
paragraphs in sections 0 to 16: 274; using one of the four words: 99; of those, naming no file, commit, ledger item, section, page, ruling or item: 13
```

The thirteen were read one by one (`closure_sentences.out.txt` prints them in
full). Four are headings. Five use "measure" as the name of the instrument, or
sit in the opening summary, the quoted question or a sentence about what a
check is for, and claim nothing the body does not cite. Two are tables whose
source is named in the sentence above them (section 12.4). One is the
statement that the tripwire's ratios are measured against the posted rate,
which is a rule, not a claim. One says the transplanting code "proves the
restriction as a tensor identity in its self-test (rehearsal item R-8)", which
names the rehearsal record's item; that record (section 2a, R-8) says "The
restriction property is proved as a tensor identity at full rank". **No claim
of measurement lacks a record.**

*Part two, the records hold what the sentences say.* The check of version 4
compared 89 figures of 2026-10-03 against their files and did not re-derive
the older ones (its section 5). This review did the older ones
(`older_figures.py`, full output in `older_figures.out.txt`):

```
strong transplant, version 1 form / chance-corrected form      v4: 0.4323 / 0.5018     file: 0.4323 / 0.5018
weak transplant, version 1 form / chance-corrected form        v4: 0.3222 / 0.5013     file: 0.3222 / 0.5013
largest |measured - formula|, and where                        v4: 0.017536, free arm  file: 0.017536 at F/2
same-value trials, distinct grammar                            v4: 0 of 4,000          file: 0 of 4000
blind solver, strict set to relaxed set                        v4: 0.2467 to 0.3095    file: 0.24675 to 0.3095
arm T own-directed on unseen marker words, seeds 0/1/2         v4: 0.7612, 0.6512, 0.6512   file: 0.76125, 0.65125, 0.65125
negative readings on that pool (rehearsal R-4)                 v4: -0.1706 and -0.2755 file: -0.1706 and -0.2755 (version 1 form)
arm T seed 0 on the grammar attempt's unseen pool              v4: -0.1870             file: -0.1870
curriculum: named-other seeds clearing, counts                 v4: 0 of 3              file: 0 of 3, [232, 580, 429]
reweight: named-other seeds clearing, counts                   v4: 0 of 3              file: 0 of 3, [695, 619, 713]
grammar attempt: named-other counts; own-directed mean; level  v4: 774, 730, 759; 0.5654; 0.5513   file: [774, 730, 759]; 0.5654; 0.5513
the grammar check's own re-run                                 v4: 750, 809, 739       file: 750, 809 and 739 found
fourth_arm.entangled_share, seeds 0/1/2                        v4: 0.60375 (483 of 800) file: 0.60375, 0.60375, 0.60375
ms per step T / C / F                                          v4: 13.08 / 13.52 / 12.53   file: 13.08 / 13.52 / 12.53
arm C slowest step over its median                             v4: 2.9%                file: 2.8%
out-v3-rules/models_sha256_check.json all_agree                v4: true                file: True
```

Every figure matches its file. Two small notes: the negative readings
−0.1706 and −0.2755 are in the version 1 form of the reading (the
chance-corrected form gives −0.1917 and −0.3303 on the same rows), which
version 4 quotes only as "negative" except in this one place (line 2387 quotes
−0.1870, which is the chance-corrected form, from a different run); and arm
C's slowest step is 2.85 percent over its median from the unrounded fields
(2.9 from the rounded milliseconds), inside the "within 3%" the text claims.
Neither is a finding. **Where the entry fires:** the label-search sentence,
whose record says something else (RT-242), and the floor-forms sentence,
whose cited record is right and whose "on the toy" is wider than any record
(RT-243).

The repository's two checkers were not run again here: the check of version 4
ran both on this same file (its section 2.5) and this review changed nothing
they look at.

### Failure 5. A command that creates something while documented as creating nothing — **does not fire**

Version 4 runs nothing against a vendor. The list's own test, run by this
session after reading the launchers' dry-run paths (each stops before its first
vendor command):

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
...
negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

(exit status 0; full output in `failure5_launcher_guard.out.txt`, every line
`[ ok ]`, with the standing prohibition on the registered launcher printed as
expected). The launcher version 4 names (`launch_a3_fetch_first.sh`) carries
the guard. The gap version 4 itself states stays open: the training entry
point for the built models on the rented machine does not exist.

### Failure 6. A remote step tested only against stand-ins — **does not fire on the launcher; four steps of the design are untested at the far end, and the text says so for each**

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
launch_a3_fetch_first.sh
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)
negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.0s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang
all checks pass. Nothing was rented and nothing was spent.
```

**What stood in for the far end, step by step.** The shutdown handshake's
machine half: local stand-ins only (stated, weakness W9). The mixed model's
code on the rented machine: never run (W9; step 4 is the first time). The
tripwire: no code (section 12.5). The registered measurement code itself, run
on a full-size model on the laptop's processor: never run; the toy code at
the toy shape stood in for it, and this review's timing is the first
measurement at the registered shape (RT-245). Each is said in the text; none
is counted as tested.

### The drafted seventh entry (not yet on the list)

Version 4 ran it; this review notes only where it fires on the text that
results once the ruled changes are written in: on the battery clause (RT-237:
a gate line the design cannot produce on any path) and on the fallback's
outcome (RT-241: an outcome the design can reach and cannot name).

---

## The decisive measured checks

The protocol asks for at least one check on the text being registered that
would come out wrong if the text were wrong. Two were run.

### Check 1. The rule as the text states it, run on the committed development grids

`rule_from_text.py` implements, from version 4's sentences alone and without
importing any of the checked code, the site-set family and its two exclusions
(section 7.2, item 2), the whole-state floor as printed (section 6.4, item 1),
the smallest clearing layer set per position set with ties to the earliest
(item 4), the piece rule at 144 of 180 applied after the layers (item 3), and
the choice by the highest development ownership-only share with ties to the
smaller size and then the earlier position set (item 5). It runs that rule on
the committed development grids of the twelve toy models and compares its
choice with the committed code's, for the primary and the stricter row; then
computes the reading, the no-transplant rule, the three controls that hold,
the two-of-three rule, the separation and the outcome term, all as the text
states them.

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-scripts/rule_from_text.py
=== 1. Nomination: the text's rule against the committed code's choice, twelve toy models
primary  T/0: text -> nominated, ((0,), 'action', 8); code -> nominated, ((0,), 'action', 8); same: True
...
primary  C/1: text -> nominated, ((1,), 'action+3', 8); code -> nominated, ((1,), 'action+3', 8); same: True
primary  C/2: text -> nominated, ((1,), 'post-identity', 4); code -> nominated, ((1,), 'post-identity', 4); same: True
primary  F/0: text -> read failed its floor: no size's piece reaches four fifths, None; code -> read failed its floor: ...; same: True
...
stricter T/0: text -> nominated, ((1,), 'action', 8); code -> nominated, ((1,), 'action', 8); same: True
...
agree on 24 of 24 (twelve primary, twelve stricter)

=== 2. The reading on fresh episodes, from the text, against the committed degree
T/0: text degree 0.0000; committed 0.0000; no-transplant miss +0.0000; controls 7/1/4 True/True/True; gate True -> reads
C/0: text degree 1.0051; committed 1.0051; no-transplant miss -0.0132; controls 7/1/4 True/True/True; gate True -> reads
C/1: text degree 0.9926; committed 0.9926; no-transplant miss -0.0111; controls 7/1/4 True/True/True; gate True -> reads
C/2: text degree 0.9974; committed 0.9974; no-transplant miss -0.0039; controls 7/1/4 True/True/True; gate True -> reads
F/0: text degree 1.0000; committed 1.0000; ... gate False -> no verdict: read failed its floor (described only), fails its gate
M/0: text degree 0.4886; committed 0.4886; no-transplant miss -0.0059; controls 7/1/4 True/True/True; gate True -> reads
...
=== 3. Two seeds of three, the separation, and the outcome term (section 3)
arm T: reads on 3 of 3 seeds: [0.0, 0.0, 0.0]
arm C: reads on 3 of 3 seeds: [1.0051, 0.9926, 0.9974]
arm F: reads on 0 of 3 seeds: []
arm M: reads on 3 of 3 seeds: [0.4886, 0.486, 0.5449]
separation, lowest of arm C minus highest of arm T: 0.9926; clears 0.5: True
outcome by the text's rules: the fifth term, metric validated, degree not read
```

(full output, every row, in `rule_from_text.out.txt`).

**Does it match what the text claims?** Yes. The rule the text states picks
the same site set, the same size and the same verdict as the code that ran, on
all twenty-four rows, including the entangled model's seed 1, where the choice
was decided by one episode in 600, and the free model's three "read failed its
floor". Every reading equals the committed one to four places; the separation
under the reconciled rule is 0.9926; and the text's own outcome rules put the
toy where version 4 says it is, on the fifth term. Had the text described a
different order of rules, a different tie-break or a different floor from the
one that ran, this would have come out different on at least the entangled
model's seeds 1 and 2. The one place the text and the code differ (the floor's
clause for a requirement at or below zero) does not bite on these twelve
models, and section 4 of the same output shows where it does (RT-238).

### Check 2. The committed code, run again from clean, against its committed outputs

`rerun_controls.py`, unchanged, run from a copy of `src/` whose output folder
points into this session's scratch space (the committed models, reads and gate
file linked in read-only, the models first checked against `SHA256SUMS` by the
script itself), then compared value by value with `compare_rerun.py`:

```
$ cd <scratch copy>/src && .venv/bin/python rerun_controls.py        # the committed code, unchanged; "done in 1485s"
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-scripts/compare_rerun.py <scratch copy>/out-controls-rerun
measure_C_seed0.json     values compared    110; differ 0
measure_C_seed1.json     values compared    110; differ 0
measure_C_seed2.json     values compared    110; differ 0
...
nominate_T_seed2.json    values compared   1980; differ 0
summary.json             values compared   1497; differ 0
table.md identical: True
TOTAL: 25 JSON files, 26722 values, 0 differ
fresh run: separation field {'0': 1.0051, '1': 0.9926, '2': 0.9974} | device cpu | torch 2.12.1 | seconds 1485
```

(every file's line in `compare_rerun.out.txt`).

**Does it match?** Yes. Every value the committed code wrote on 2026-10-03,
26,722 of them in 25 files, came back identical on this laptop today, and the
table is byte-identical; only the running time differs (1,485 seconds against
the committed 967, because this session ran other scripts alongside it). The
per-seed separation field is 1.0051, 0.9926 and 0.9974, whose lowest minus
arm T's highest is the 0.9926 of check 1. This repeats what the check of the
controls re-run (at `e184a6e`) found; it is repeated because the registration
leans on these files and the protocol makes their verification the tier 1
reviewer's.

### What these two checks do not cover

They cover the procedure on the toy. They do not cover the registered width
(RT-240), the registered generator (RT-239), the battery clause (RT-237) or the
outcome states the toy never reached (RT-241); those are the findings.

---

## The kill case

The case for not registering this text, as strongly as it can be put. The
registration's purpose is to fix in advance what would count as a result; as
written it fixes one thing that would make its best outcome impossible and
leaves several reachable outcomes without a name. The free model's gate
carries a clause about batteries that the task does not contain and that no
run has ever evaluated, and the design's own rule turns an unevaluable gate
into a failure, so "degree read" cannot be reached as written. The episode
counts it freezes were chosen because they were the only ones rehearsed, but
they were rehearsed at a third of the registered width, and a stand-in at the
registered width puts the high anchor under its own floor on two seeds of
three; if that happens the experiment falls into a two-model fallback that has
no registered outcome term, after both releases of money are drawn. The grammar
it registers is described by reference to a generator that shows the model its
own name as it acts, which is the one cue the whole design exists to keep out,
and the two lines that keep it out are not in the text. And the floor that is
meant to keep the divisor off zero "by construction" does so only through a
clause in code the text does not carry. None of this is expensive to fix: one
ruling on a clause, one sentence on the floor, one page on the episode format,
one table of outcomes, and either more fitting episodes or a rehearsal at
width 448 on the laptop. But every one of them is the kind of thing this
programme has already paid for once in a registered sentence nobody could
satisfy, and the registration commit is the one commit that cannot be taken
back.

---

## For the outside reviewers

Not a ruling; for the session that builds the tier 2 packet.

**(a) The files an outside reader who cannot run code most needs.**

1. `docs/successor-experiment-proposal-2026-10-03-v4.md`, with the list of
   ruled changes in this review's section "The registration text as
   reviewed".
2. `docs/rulings/2026-10-03-version-4-questions-rulings.md` (record B), the
   reconciliation `docs/rulings/2026-10-03-seven-questions-reconciliation.md`,
   `docs/rulings/2026-10-03-version-4-check-questions-rulings.md` and
   `docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`.
3. `docs/2026-09-21-successor-measure-rehearsal.md` (sections 0, 3, 5, 6, 7,
   8): what the instrument does on built models and where it first failed.
4. `docs/2026-10-03-controls-rerun.md` and `docs/2026-10-03-competing-solver-run.md`:
   the toy figures under the rules as registered, and the ordinary competing
   solver.
5. `docs/known-failure-modes.md` and `docs/outside-review-protocol.md` (the
   brief and the closure rule).
6. This review, and the two checks it builds on:
   `reviews/2026-10-03-proposal-v4-check-claude-code.md` and
   `reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md`.
7. The two grammar headers, which say in prose what RT-239 is about:
   `experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py` (lines
   1 to 115) and `experiments/rehearsal-successor-measure/src/grammar.py`
   (lines 1 to 65).

**(b) Questions this review could not settle, for a reader from another lab.**

1. **Does a reading near 1 on the entangled model say anything the
   construction did not already guarantee?** Any piece that holds the label at
   the action position and moves nothing reads near 1. Is there a design
   change that would let the high anchor fail in an informative way, rather
   than only by its whole-state transplant missing the floor?
2. **What fit floor and fitting-sample size would you register for a
   twelve-way straight-line read on a 448-wide state?** RT-240 shows the
   ruled 420 fitting episodes are fragile under a crude stand-in; what would a
   lab that does this routinely use, and would it fix the regularisation in
   advance?
3. **Is the separation rule's asymmetry right?** It sets aside a seed that
   returns no verdict and counts a seed that returns an odd reading
   (the check-questions ruling, ruling 2). For a claim of "metric validated",
   is that the conservative direction, or does it make the result hostage to
   which failures happen to trip a floor?
4. **Is a mixture by item a fair middle anchor for a measure meant to read
   partial separation within each act?** The design says it is not, and keeps
   the mixed model anyway (W10). What middle anchor would you build at this
   size?
5. **Should the name cue at the moment of acting be closed by the grammar, or
   tested for by a control?** RT-239 asks the text to register the grammar
   that removes it. An outside reader may know a cleaner discriminator than
   removing it, one that would let a free model's reading be checked for
   reliance on a name.

---

## Scripts and outputs beside this file

In `reviews/2026-10-04-successor-v4-gate-a-scripts/`, each run from the root
of the checkout with the project's own Python (torch 2.12.1, scikit-learn
1.9.0, numpy 2.5.0, scipy 1.18.0), on the processor:

| Script | What it does | Output |
|---|---|---|
| `rule_from_text.py` | the decisive check: the rule from the text, on the committed grids; the reading, the controls that hold, the seeds rule, the separation and the outcome; the floor on the competing solver | `rule_from_text.out.txt` |
| `compare_rerun.py` | compares a fresh run of `rerun_controls.py` with its committed outputs | `compare_rerun.out.txt` |
| `failure_mode_pass.py` | the known-failure list's tests 1 to 3 on the committed outputs | `failure_mode_pass.out.txt` |
| `older_figures.py` | figures version 4 quotes from records older than 2026-10-03, against their files | `older_figures.out.txt` |
| `closure_sentences.py` | every paragraph using verified, measured, calibrated or attacked, and whether it names a record | `closure_sentences.out.txt` |
| `floor_forms.py` | where the two forms of the whole-state floor disagree, across every committed grid | `floor_forms.out.txt` |
| `solver_sentence.py` | the ruled sentence about the competing solver, against its outputs | `solver_sentence.out.txt` |
| `width_vs_count.py` | the width stand-in (NOT A RESULT) | `width_vs_count.out.txt` |
| `registered_shape_timing.py` | forward-pass timing at the toy and registered shapes on the processor | `registered_shape_timing.out.txt` |
| (the repository's) `check_launcher_argument_guard.sh`, `check_remote_forms.py` | failures 5 and 6 | `failure5_launcher_guard.out.txt`, `failure6_remote_forms.out.txt` |
