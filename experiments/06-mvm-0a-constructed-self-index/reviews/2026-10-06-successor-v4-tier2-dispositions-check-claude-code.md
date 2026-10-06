# Check of the proposed dispositions for the outside reviews of successor proposal version 4 (pull request 101), and of the measurements behind them

*Written 2026-10-06 (Pacific) by a Claude Code checking session, in its own git
worktree, on branch `check-tier2-dispositions`, cut from
`origin/gate-a-v4-tier2-dispositions` at `cbf2f03` (pull request 101,
"PROPOSAL: dispositions for the outside reviews of successor version 4, and a
six-page addendum for John"). This is a paired check under "The pairing rule"
of `docs/outside-review-protocol.md`. It wrote none of version 4, either outside
review, the inside dispositions, the frozen successor code, the method, the
measurements or the two PROPOSAL documents, and has no chat history. Laptop
only, on the processor. Nothing was trained, rented or spent: $0. Version 4,
the reviews, the rulings, the ledger and the author's files were not edited.*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (a command was run; the script and its output are in the folder
beside this file) or **ARGUED** (reasoning a reader can dispute).*

## What this session opened

**Read in full:** the method and the output of the measurements
(`docs/2026-10-06-gate-a-v4-tier2-dispositions-measurements-method.md`,
`docs/2026-10-06-gate-a-v4-tier2-dispositions-measurements.md`); both PROPOSAL
documents (`docs/rulings/2026-10-04-successor-v4-gate-a-tier2-dispositions-PROPOSAL.md`,
the detail; `docs/rulings/2026-10-04-successor-v4-gate-a-tier2-questions-PROPOSAL.md`,
pages 7 to 12 for John); both outside reviews as filed
(`reviews/2026-10-04-successor-v4-chatgpt.md`, `reviews/2026-10-04-successor-v4-gemini.md`);
the author's script `tier2_dispositions_check.py` (read and run as a program,
never imported); the frozen successor code's `measure.py` and the `gate` and
`summarise` functions of `procedure.py`, from `origin/main` at `53ae82c`.

**Read in part:** version 4 (sections 3, 6.1, 6.4, 7.3 item 6, 9, 11 step 5a
and stop S4, W5, W11, W12, and every passage a proposed change replaces); page
5 of John's earlier packet and the RT-241 table of the inside dispositions;
the freeze report `docs/2026-10-04-successor-code-freeze.md` (section 4.1, on
main); the frozen `grammar.py` (how matched pairs and the relaxed set are
built); the rehearsal's `rerun_controls.py` (controls 6 and 7); freeze test
T3a and T6 summaries (on main); the 2026-10-04 dispositions check, for its form.

**Not opened:** the outside packets, `STATUS.md`, the site, any chat.

**Scripts and outputs** are in
`reviews/2026-10-06-successor-v4-tier2-dispositions-check-scripts/`. None
imports the author's script. `a9_recompute.py` and `a9_joint_sampling.py`
import no project code at all. `frozen_procedure_probe.py` imports the
**frozen successor code** (written by the freeze session, not by this pull
request's author), from a fresh copy of `origin/main` in a temporary folder,
because checks 2 and 3 are about what that code does.

---

## The answer in seven lines

1. **A9's arithmetic: holds exactly.** Every figure recomputes in exact
   fractions from the twelve committed records and from first principles, and
   it still holds when *p* is measured on the same 800 pairs rather than taken
   as known (0.5562 against 0.5589; 0.9961 against 0.9904).
2. **A2's account of the frozen code: right, with two gaps in the "must be
   added" list.** The code does what the corrected account says, including
   arm T's no verdict going to R2 and the toy landing on R3; its self-test
   passes, 40 of 40. But the code writes a withheld reading into its output
   file (`arithmetic_withheld`), which the proposed R-13 text and the
   closure check's step 2 forbid, and the list does not say to remove it.
3. **The A7 counterexample: exact against the code** (rehearsal and frozen).
   The proposed text leaves two sentences that still claim what A7 says the
   cell cannot show.
4. **Numbers trace; one proposed change is incomplete in a way that matters.**
   Page 9 is shown to John as a change to page 5, plainly. But it does not
   say, or change, that version 4's step 5a and stop S4 already make a free
   model's gate failure R3 with "nothing else launches". That is the most
   likely way the free model fails.
5. **Method before output: holds.** The method (`da505d4`) is the parent of the
   output (`025ce90`); the script never changed; rerun, its output is
   byte-identical. The dated correction only adds lines.
6. **The two checker scripts: clean** once main's files are laid over the
   branch (0 confident findings). On the branch alone, all 12 confident
   findings are paths that exist only on main.
7. **Mapping: right.** A1, A3, A4, A5 and G1 to G9 land on the right RT
   numbers; Gemini's second answer found nothing. Three remarks inside
   ChatGPT's feasibility table are not mentioned anywhere (small).

**Verdict.** Fit to go to John after the text fixes below. Defect 1 (page 9
against step 5a) changes what John is being asked and should be fixed first.
Defect 8 (the pull request description still says the code does not exist)
should be fixed before John opens the pull request page.

---

## 1. Check 1, the A9 arithmetic (MEASURED): holds exactly

`a9_recompute.py` reads only the twelve records
`out-controls-rerun/measure_<arm>_seed<s>.json`. It counts erring trials and
donor-answer hits as whole numbers (800 × the rates) and does every
probability as an exact sum of fractions, so nothing depends on rounding at
the 0.018 edge.

| Claim in the PROPOSAL | This check |
|---|---|
| The formula `(1 − p)/7` recomputes on all twelve records | **Yes**, all twelve equal the committed `formula` field |
| At p = 0.8: 0.0667 against 0.0286, a gap of 0.0381 over 0.018 | **Yes**: 0.0667, 0.0286, 0.0381 (over the allowance by 0.0201) |
| The gap exceeds the allowance below p ≈ 0.9055 | **Yes**: exactly below 1811/2000 = 0.9055 |
| Withholds a healthy model in the review's case 0.9904 of the time at p = 0.8, 1.0000 at 0.56 | **Yes**: 0.9904, 1.0000 |
| Flags a broken pairing at the learning bar 0.5589 of the time | **Yes**: 0.5589 at 0.2633 and at the exact bar 790/3,000 |
| Withholds a healthy, evenly erring model 0.0945, 0.0347, 0.0023 | **Yes** |
| The toy models put 0.097 to 0.155 of their errors on the donor's answer | **Yes**: 10 of 103 (arm M seed 0) to 55 of 355 (arm F seed 2) |
| W11's 0.51 to 0.63 (arm C) and 0.22 to 0.32 (arm M) | **Yes**: 0.5062 to 0.6296 and 0.2222 to 0.3210 |

**One assumption the author did not state, tested (MEASURED,
`a9_joint_sampling.py`).** The author treated *p* as known. Version 4 measures
it on the same fresh episodes as the untouched rate, so both wobble together.
Building the exact joint distribution of the two counts over 800 pairs:
broken pairing flagged 0.5562 at the bar; healthy review's case withheld
0.9961 at p = 0.8 and 1.0000 at 0.56; healthy even case 0.0908, 0.0286,
0.0014. **Nothing the PROPOSAL says changes.**

## 2. Check 2, A2: what the frozen code does (MEASURED and ARGUED)

`frozen_procedure_probe.py` extracts `origin/main` (`53ae82c`) into a temporary
folder, runs `measure.py --self-test`, then runs `procedure.summarise` on the
committed T3a toy rows and on eight altered copies of them. The landing of
each was written in the script before it ran. One case (C8, arm M out of its
band) first came out "not as expected" because of this session's mistake:
the rows store the reading as computed, and the first version changed only
an accuracy. It was fixed to set the stored reading too, and then landed as
written.

| The PROPOSAL says | This check |
|---|---|
| `measure.withhold` replaces the reading with "no verdict" and lists the reasons (gate, nomination, described-only, fresh and development floors, no-transplant, controls 7, 1 on arm T, 4; an unevaluated control counts as failed) | **Right** (read; and the self-test's withholding cases pass) |
| Learning own-directed and named-other are joint per seed; the collapse is counted separately; the arm's gate is applied to every seed | **Right.** Case C2: arm C seed 2 fails the gate itself, the arm passes on seeds 0 and 1, and seed 2 still reads (0.9974) |
| R3 if T, C or F fails its gate; arm M's band never changes the term | **Right.** Case C8: arm M reads 0.95 on two seeds; the term is unchanged and nothing is said about it in the term or the notes |
| Arm T no verdict with arm C reading gives R2 | **Right** (case C1). Arms T and C both no verdict also give R2 (case C6) |
| The two-model fallback gives "R1 with a note" | **Half right.** With arm F unread it gives the fifth term with the note (case C5). The word "R1" in item 1 of the list should be "R1 or the fifth term" |
| The toy, end to end, lands on R3 | **Right**: rerun on the committed rows, R3, "arm(s) F failed the gate", every arm F seed withheld with three reasons, same as the committed `summary.json` |
| T6 untrained models land on R3 | **Right** (both summaries on main: every gate fails) |
| `measure.py --self-test` passes | **Right**: 40 PASS, 0 FAIL, "all checks passed" |
| The self-test never runs `summarise` on constructed rows | **Right**: `procedure.py`'s self-test and `tests/reproduce_toy.py` call `summarise` only on real rows |

**The six "must be added" items.** Each is right. The list is not complete:

- **Missing: the withheld reading is in the output file.** `summarise`
  writes `arithmetic_withheld` for every withheld seed. On the toy that is
  1.0, 1.0 and 1.0108 for arm F (MEASURED, part B of the probe). Version 4,
  section 6.4, item 5, says the registered code "replaces the reading with
  'no verdict'... in the output file". The proposed R-13 text says "no
  withheld reading appears in its output file or its table". The closure
  check's step 2 says the reading "must appear in neither". All three would
  fail on today's code, and none of the six items fixes it. The PROPOSAL
  mentions the field once, as a neutral fact. The table is fine: it prints
  "no verdict" and the three accuracies, not the reading.
- **Missing, smaller: not every reason is listed.** `withhold` checks the
  controls only when a reading was computed. `summarise` adds the arm F
  collapse reason only to a seed that would otherwise read. Case C7: arm F
  passes its gate, its collapse fails on two seeds, and the seeds list only
  the nomination reasons. Item 2 (the collapse folded into the per-seed
  gate) would cure the second part if John picks the joint rule. The first
  part needs its own line.

## 3. Check 3, the A7 counterexample (MEASURED from the code, ARGUED as logic): exact

In both the rehearsal (`rerun_controls.py`, line 204) and the frozen code
(`procedure.py`, lines 488 to 499), control 6 has three parts:

- **same-value** means the recipient's correct answer equals the donor's
  (`targets == ct`, with `ct` the donor episode's target);
- **moved** means the transplanted prediction differs from the untouched
  one;
- the twins share all content (`grammar.make_pairs`: "recipient and donor
  differ only in the acting channel").

So copying who is acting, then looking up that agent's value in the
recipient's context, gives `ct`. Copying the donor's prepared answer also
gives `ct`. The prediction is the same token trial by trial, so the two
mechanisms give identical cells. **The author's "exact" holds.** The only
qualification is the one the review itself makes: if the untouched model
was wrong on a same-value trial, both mechanisms move it.

**The text change is incomplete (ARGUED).** It replaces section 6.1's last two
sentences, item 6's "discriminating control" sentences and W11's body. It
leaves:

- item 6's "on those arms the whole-state transplant carries something
  besides identity" (version 4, lines 1975 to 1976);
- **W11's title**, "Control 6 says the whole-state transplant carries more
  than identity on the entangled arms".

Both claim what A7's second point, accepted in the same disposition, says a
moved same-value cell cannot show by itself. A7's closure search ("no
sentence claims control 6 separates the two") would not catch them, because
they make the neighbouring claim.

## 4. Check 4, numbers and text changes

### 4.1 Numbers (MEASURED)

Every figure in both PROPOSAL documents that comes from this pull request's
measurements traces to `check.json` or to the records named. That covers
0.9055, 0.0667, 0.0286, 0.0381, 0.9904, 1.0000, 0.5589, 0.097 to 0.155,
"99%", "56%", "about 0.9" and W11's ranges. The figures about the frozen code
trace to main: R3 on the toy, three reasons per arm F seed, T6 on R3, "all
checks passed". Version 4 figures the text leans on also match: 144 of 180,
0.3 to 0.7, 0.10, rank cap 8, arm T's 0.0000, the 0.0018 margin at the bar.
The tally (9 new: 1 fatal, 5 serious, 3 worth-noting; accept 3, accept with
change 6) adds up.

### 4.2 Each text change against its finding (ARGUED)

| Finding | Matches the finding? | Changes something else silently? |
|---|---|---|
| A2 (R-13, section 6.4 item 5) | Yes | R-13's "no withheld reading appears in its output file" is false of today's code (section 2 above) |
| A6 (section 3, W12) | Yes; the anchor sentence exists at version 4 lines 370 to 371 | No |
| A7 | Yes, as far as it goes | Leaves two contrary sentences (section 3 above) |
| A8 | Yes | No |
| A9 (section 6.4 item 3, item 5, section 9 row) | Yes | It deletes, without saying so, version 4's "the detection margin at the bar is printed in the reporting table" and its figures (0.0198, 0.0018, 0.0441). It also says control 7 checks "that the transplant code uses the pairs as built". Control 7 transplants a recipient into itself and never touches the donor. Control 4 is the one that checks the twins: the frozen code requires the output to be bit-identical when donor states are transplanted before both twins' own turns. See section 6 |
| A10 text change 1 (joint seeds, section 9 rows) | Yes | No |
| A10 text change 2 (page 9, rule 1 "T or C") | Yes | **Leaves four contradictions; see below** |
| A10 text change 3 (arm M's miss) | Yes | No |
| A11, A12, A13 | Yes | No |

**Page 9 and step 5a (the defect that matters most).** Version 4's step 5a
(lines 2511 to 2514) says of the first free-model run: "if that fails too,
the outcome is R3 and nothing else launches". Stop S4 says the same.
The freeze report, section 4.1, quotes it as the reason the code returns R3.
The free model's most likely gate failure (the design's own prior) is at
step 5a, before arms T and C are run at the registered size. So:

- the situation page 9 asks about ("the two built models still learn and
  separate") arises only if arm F passes at step 5a on one seed, then fails
  its gate on the other two at step 5b;
- page 9 does not tell John this, and no text change touches step 5a or S4.

Adopting page 9 as drafted would also leave version 5 contradicting itself
in three places the A10 text changes do not touch:

- section 3's R3 row ("One or more arms fail its gate");
- the R2 row ("Every arm carried passes its gate ... both conditions on arm
  F"), when arm F fails and T and C do not separate;
- the inside dispositions' text change 2 to section 8.1 ("R3 for the
  experiment (arm M excepted)").

Page 9 also says the recommendation "matches how the rehearsal code already
treats it". That is true of the rehearsal code. The frozen registered code
does the opposite: it returns R3, deliberately.

**Is page 9 shown as a change to page 5? Yes.** The index row says "Changes
page 5's table". The page heading says "(A10; changes page 5)". The body says
"Page 5's table, as drafted, would make it the first". Nothing is hidden.
Page 5 itself carries no pointer forward, so John should rule pages 5 and 9
together.

**A smaller point on page 7 and A10.** The PROPOSAL says the review's split
table "would still pass the collapse column separately" under the frozen
code. Run through the frozen code, that table **fails** arm F's gate: only
seed 1 passes both learning conditions (case C3). Over all 512 pass-or-fail
patterns of arm F's three conditions on three seeds (part D of the probe):

| Rule | Patterns where it passes the arm with no seed passing all three |
|---|---|
| Separate majorities (version 4's text, the rehearsal) | 6 |
| The frozen code | 0 |

The frozen code's remaining gap is 18 patterns where exactly one seed passes
everything. Page 7's opening, "Today each gate condition is counted across
seeds separately", describes version 4's text and the rehearsal code, not the
registered code. The recommendation is unaffected.

## 5. Check 5, method before output (MEASURED): holds

- **Order.** `da505d4` (method and script, 08:58:15) is the parent of
  `025ce90` (the output and `check.json`, 08:59:00). The script has only one
  commit touching it.
- **Rerun.** The author's script, rerun as a program in a scratch copy,
  writes a `check.json` byte-identical to the committed one
  (`author_script_rerun.out.txt`).
- **What this check cannot see.** When the method commit reached the remote:
  the 45 seconds between the two commits fit the method's "committed and
  pushed before anything described here is run", but this check cannot
  confirm it.
- **The correction.** The diff from `025ce90` to `cbf2f03` on the
  measurements file removes no line. It adds a dated note at the top and a
  "Correction to Part A" at the end, so `025ce90`'s text stands as
  committed.
- **One muddled phrase there.** "the command `ls -d ...` was true of this
  branch and false of main" means the command found no such folder on the
  branch, and the folder does exist on main.
- **Part A's commands, rerun on the branch** (`part_a_commands.out.txt`),
  return exactly what the table in Part A says. On main the first two return
  the folder and `measure.py`.

## 6. Check 6, the two checker scripts (MEASURED): clean

`check_citations.py` and `check_single_source.py`, one run per new document.

- **On the branch alone:** 12 confident citation findings. All 12 are
  `experiments/08-successor-degree/...` or
  `docs/2026-10-04-successor-code-freeze.md`, which exist only on main.
- **On a scratch copy of the branch with those main files laid over it:** 0
  confident findings. The items marked for a human eye are bare names
  (`table.md`, `src/`) and two rounded figures (0.9 and 0.99, from 0.9055
  and 0.9904), all fine.
- **Single-source (money):** 0 confident findings. The one item per document
  is its own "$0".

## 7. Check 7, the mapping (ARGUED, against both reviews as filed): right

- **The ChatGPT repeats.** A1 is RT-237 (the batteries), A3 is RT-238 (the
  floor's positivity), A4 is RT-240 (the fitting sample at width 448), A5 is
  RT-239 (the grammar departures). A10's first paragraph is RT-241's five
  holes.
- **Gemini.** G1 is RT-240, G2 RT-245, G3 RT-239, G4 RT-238, G5 RT-237, G6
  RT-241, G7 RT-242, G8 RT-244, G9 RT-246. Each Gemini finding cites the
  inside review for its evidence. Gemini's second answer says "No additional
  findings" in all four parts.
- **Lettered findings.** None is folded away. A10's two new cases and the
  precedence point are disposed as A10. The kill case is put on page 12.
- **Not mentioned anywhere: three remarks in ChatGPT's feasibility table**
  (small; none is lettered):
  - "the final committed dependency file must actually be named and
    present": already one of the thirty ruled wording fixes (the inside
    review, line 149);
  - "different random seeds alone do not prove that combinations never
    overlap" (control 5, unseen combinations): the frozen generator's
    training stream skips an excluded set of fingerprints, which may answer
    it, but this check did not verify that;
  - the single-fit-and-reload procedure "differs from the toy's historical
    two-fit provenance": already disclosed in version 4, section 7.2.

  One line in the dispositions saying each is covered, or why it needs
  nothing, would close the "nothing missed" question.

---

## Defects, in order of weight

1. **Page 9 omits step 5a and stop S4** (section 4.2). Say on page 9 that a
   free-model gate failure at step 5a is, under ruled text, R3 with nothing
   else launched, and that page 9's case arises only from a step 5b split.
   Then either:
   - propose the step 5a and S4 wording too, plus section 3's R3 and R2 rows
     and the inside section 8.1 change; or
   - narrow page 9 to failures found at step 5b.

   Also correct "matches how the rehearsal code already treats it": the
   registered code returns R3.
2. **A2's list lacks removing `arithmetic_withheld`** from the output file,
   or a ruling that it may stay, with R-13 and the closure check's step 2
   reworded to match.
3. **A7 leaves two contrary sentences**: item 6's "carries something
   besides identity", and W11's title.
4. **A9's replacement silently drops the detection-margin sentence** and
   names control 7 as a pairing check. Say that the margin line goes, and
   name control 4 (and the generator self-test) as the direct checks.
5. **A10 and page 7 describe the frozen gate as looser than it is**: the
   review's own table fails under it. Reword the sentence; the
   recommendation stands.
6. **A2's "lists every reason" is overstated** (case C7). Add a line to the
   list.
7. **Small wording.**
   - A2's status says "four pending rulings" and lists five.
   - Item 1's "in place of R1-with-a-note" should be "in place of R1 or the
     fifth term with a note".
   - The correction note's "was true of this branch and false of main".
8. **The pull request description is stale.** It still says "It does not
   exist as code. There is no `experiments/08-successor-degree`, and no code
   assigns an outcome term." Edit it to match `cbf2f03`.
9. **Three feasibility-table remarks are unmentioned** (section 7). One line
   each.

## For John

- **Rule pages 5 and 9 together, and know what step 5a says first.** Under
  ruled text, if the free model fails its gate at the first registered run
  and its re-run, the outcome is "substrate not a testbed" and nothing else
  is run. Page 9's recommendation is about a later, rarer case, and adopting
  it means rewriting step 5a, stop S4 and two rows of the outcome table too.
- **Page 8 is stronger than it says.** The registered code already has a
  direct, bit-for-bit pairing check that withholds a reading: control 4, as
  redefined, transplants the donor's states from before either twin's own
  turn and requires the output to be bit-identical, which a mismatched pair
  would break. Dropping the no-transplant veto loses little. The arithmetic
  against the veto holds even with accuracy measured on the same pairs.
- **On the decoy test (page 10), a design point for its method (ARGUED).**
  Arm T's true slot is already read perfectly (fit 1.000 at layer 0). An
  exact copy of the marker would also be read perfectly. So which one the
  nomination picks may be decided by its tie-breaking order, not by which is
  "easier to read". The method should say in advance how ties fall, or run
  the decoy both ways round.
- **The toy outcome is R3 in the registered code today**, by design and on
  the record (freeze report, section 4.1). Version 4's sentence calling it
  the fifth term is the loose one. Page 9 decides which way that goes.

## What this session did not do

It did not rule, or edit version 4, the reviews, the rulings, the ledger,
the frozen code, the author's measurement files or either PROPOSAL document.
It did not write version 5, build the decoy, or change the decision
procedure. It did not merge anything. It spent nothing and rented nothing.

---

## Re-check of the fixes at `dedd56c`, 2026-10-06 (later the same day)

*The same checking session, in a fresh worktree. It read only the diff from
`cbf2f03` to `dedd56c` (three files: the measurements file and both PROPOSAL
documents), version 4's step 5a, stop S4 and section 7.2, and the frozen
code's `measure.outcome` and `procedure.summarise` on main. Nothing was run
that is not named here; $0.*

**Nothing else changed (MEASURED).** `dedd56c` touches only those three
files. In the measurements file it removes three lines only: the muddled
sentence in the first correction note, itself added at `cbf2f03`. That
sentence is reworded in place with a dated note. `025ce90`'s text is
untouched (the removed wording does not occur in it). Every other change in
the diff answers one of the nine defects or one of the "For John" points
above.

| Defect | Fix at `dedd56c` | Verdict |
|---|---|---|
| 1. Page 9 against step 5a and stop S4 | Narrowed to a free-model gate failure at step 5b. Step 5a and S4 are left as ruled. The R3 and R2 rows, the inside section 8.1 change and the toy sentence are now listed for change. The frozen code is described as returning R3 by design. The packet tells John to rule pages 5 and 9 together | **Holds**, with one precision point below |
| 2. `arithmetic_withheld` | New "does not do" item 6, and new must-be-added item 7: remove the field, with John's alternative (keep it, and reword R-13 and the closure check's step 2) stated | **Holds**. Small slip: item 7 is printed between items 5 and 6 |
| 3. A7's two contrary sentences | Text change 2b rewrites item 6's later sentence; W11 is retitled | **Holds** |
| 4. A9's detection margin and control 7 | The margin sentence is now replaced openly, with a 0.56 chance of flagging at the learn-both bar (0.5589 measured; 0.5562 with accuracy measured on the same pairs). Control 4 is named as the pairing check; control 7 is said to check the transplant code only | **Holds**, with two small points below |
| 5. The frozen gate described as too loose | The A10 text and page 7 now give 0 (frozen code), 6 (separate counts) and 18 (exactly one seed passes everything), and say the review's table fails under the frozen code. The figures are attributed to this check | **Holds**. The counts equal this check's part D output, and the "because the collapse is counted separately" explanation is right |
| 6. "Every reason" | Reworded, and covered by the new items 6 and 7 | **Holds** |
| 7. Small wording | "five pending rulings"; "R1 or the fifth term with a note"; the correction note reworded | **Holds** |
| 8. The pull request 101 description | Rewritten: the code exists, the toy lands on R3, `arithmetic_withheld` is to be removed, page 9 is narrowed | **Holds** |
| 9. Three feasibility-table remarks | One line each. Checked: `experiments/08-successor-degree/requirements-measure.txt` exists on main; the fit-once-and-reload disclosure is in version 4 section 7.2, item 1; the control 5 point is honestly left "not yet shown", with a generator self-test line proposed | **Holds** |

**Page 9's reasoning, against version 4 and the frozen code (ARGUED, from
the text and the code).**

- **Step 5a and S4 really are left alone.** The new rule 1 makes a step 5a
  failure after its re-run R3, which is what step 5a and S4 say.
- **The 5a run is one of arm F's three seeds.** Step 5b's "eleven later
  runs" make twelve with the 5a run, so "passes at 5a, fails the gate at 5b"
  means one seed passed and two failed. That is a real, reachable case.
- **It fits the frozen code's structure.** A step 5a stop launches nothing
  else, and `summarise` computes an outcome only when arms T, C and F are
  all present, so the code never sees a step 5a failure. `measure.outcome`
  only has to stop returning R3 for an arm F gate failure, which A2's item 1
  already covers.
- **The toy sentence is right, with one condition the text does not state.**
  The toy's arm F passes both conditions on seed 0 and fails named-other on
  seeds 1 and 2.
  - If seed 0 is the step 5a run, it passes, and seeds 1 and 2 fail at step
    5b. That is the fifth term.
  - If seed 1 or 2 is the step 5a run, it fails. "R3 otherwise" then needs
    the re-run to fail too. The toy has no re-run (the freeze report says
    so). If the toy's other failing seed stands in for the re-run, the
    answer is R3. If seed 0 stood in for it, the re-run would pass and the
    case would go on.

  Version 5's toy sentence should add "the toy has no re-run" or "taking the
  re-run as failed". This does not change the recommendation.

**Smaller points left (none blocks).**

- **The section 9 row.** A9's replacement middle column for "The
  no-transplant allowance" still omits the flagging chance that item 3 now
  prints. Add it, so the row and the item agree.
- **"0.56" means two things.** In the new A9 sentence it is a probability.
  In the version 4 sentence it replaces, 0.56 is the toy free model's
  accuracy. Writing "a 56 per cent chance" would avoid misreading.
- **Item 7 needs one more clause.** It says `withhold` "evaluates every check
  whether or not a reading was computed". For a seed with no reading the
  controls may never have run. Under the code's own "unevaluated counts as
  failed" rule, item 7 would then list failures of checks that were never
  run. Add "and lists a check that was not run as not run".

**Re-check verdict.** All nine defects are fixed as asked, and nothing else
changed. Page 9 is now consistent with version 4's step 5a and stop S4 and
with the frozen code. The pull request is fit for John once the three small
points are tidied, which can wait until version 5 is written.
