*This is file 19 of 33 of one review packet, pasted into a single conversation. It contains record 13 (John's ruling of 2026-10-04 on seven questions from the competing-solver run and the twenty-piece control); record 14 part 1 of 3 (the check of version 4 by a session that did not write it (holds the wording fixes the registration text must carry)). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 13 of 25 - John's ruling of 2026-10-04 on seven questions from the competing-solver run and the twenty-piece control - `docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md` (complete file, 4,173 characters) =====
# Ruling 2026-10-04: seven questions from the competing-solver run, the twenty-piece control and their check

*Recorded 2026-10-04 (UTC; the evening of 2026-10-03, Pacific) by the
Claude Code coordination session. **Authorship: mixed.** Each question and
its suggestion come from the findings of pull request 88
(`docs/2026-10-03-competing-solver-run.md`, section 8), pull request 89
(`docs/2026-10-03-control-2-twenty-draws.md`, section 7) and their check,
pull request 90
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md`,
section 9). The coordination session put all seven to John once, with the
check's version of each suggestion, and he ruled in the words **"Agreed on
all seven"**. No compute was launched and no money was spent.*

*Written under the workspace plain-language rule.*

## What was ruled

1. **Which reading of the solver the registration cites.** The main reading
   has the acting channel removed, as the solver was trained and scored. The
   reading with the channel left on is stated beside it. The registration
   says plainly that the main reading's "no verdict" comes from how the
   twins are paired: their states are identical, so every transplant is a
   null transplant. It is not evidence about the measure. The reading with
   the channel left on is the one that tests the measure.
2. **The registration says what stopped this solver**, in the check's
   sentence: "On the toy, the ordinary competing solver returned no verdict
   because no site set cleared the floor at nomination; behind that, its
   best piece missed the piece rule by 119 or more of 180 and its untouched
   rate missed the no-transplant rule by 0.11 or more, and it would have
   failed the gate on learning had it been gated as the free model is. For
   a model near chance the floor itself is close to zero and is decided by
   one or two episodes."
3. **The no-transplant formula is reported, not generalised.** It withholds
   a reading here, which is the right outcome. But it assumes wrong answers
   spread evenly over the other values, and this solver's do not, so the
   registration does not describe the formula as true of every model
   (version 4, lines 1178 to 1183).
4. **The registered other-agent control is `control2_twenty_draws.control2`.**
   `rerun_controls.control2` is named as the earlier version, kept as the
   record of the re-run. The full-size registered code takes control 2 from
   the new function, so there is one control 2 at registration.
5. **The 95th percentile of the twenty random pieces stays as the summary**,
   as ruled, and all twenty are printed beside it.
6. **The solver run's explanation is corrected before it is quoted.** The
   solver's findings (section 4 and question 2) and the description of pull
   request 88 say the gate on learning stopped the solver. Version 4 does not
   gate competing solvers. The session that writes the registration text
   uses "would fail the gate if it were gated as the free model is". No
   re-run, and no rule change. Pull request 88 was merged as written.
7. **No new run before the registration review.** The registration's
   section 13 gains a two-sentence weakness: the toy's ordinary competing
   solver fails the task, so its "no verdict" shows only that the measure
   returns nothing on a model that has not learned the task. It does not
   show what the measure does on a model that does the task by another
   route. The alternative, training a solver that learns from another cue
   before the review, was not taken.

## Also merged on John's instruction

Pull requests 88 (the competing-solver run), 89 (the other-agent control
against twenty random pieces, NOT A RESULT) and 90 (their check). All three
are on the main line at `ecf3820`.

## What this changes

All seven rulings go into the registration text, together with version 4,
the thirty wording fixes from the check of version 4, the ruling of
2026-10-03 on that check's two questions, and the changes in section 7 of
the check in pull request 90. Nothing here edits version 4, an earlier
ruling file, STATUS.md or `data/project.toml`.
===== END OF RECORD 13 =====

===== RECORD 14 of 25, part 1 of 3 - the check of version 4 by a session that did not write it (holds the wording fixes the registration text must carry) - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-claude-code.md` (complete file, 62,740 characters) =====
# Check of version 4 of the successor experiment proposal, of the two ruling packets behind it, and of the ruling that reconciled them

*Written 2026-10-03 (Pacific), night, by the Claude Code session "MVM W2c check
of proposal version 4", in its own worktree (branch `w2c-proposal-v4-check`,
cut from the main line at `41b0bd3`, the commit that put version 4 and the
three ruling records on the main line as pull request 85). This is a paired
check under the pairing rule of `docs/outside-review-protocol.md`. It is not
the registration review. Laptop only, on the processor. Nothing was rented,
trained or spent: $0. Nothing was edited but this file and the scripts beside
it.*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (the command and its output are in this file or in the folder
beside it) or **ARGUED** (reasoning a reader can dispute).*

## What this session opened, and what it did not

**It wrote none of what it checks.** It did not write version 4, any ruling
record, either packet, the controls re-run or the short pre-stated run.

**Opened and read in full:** version 4
(`docs/successor-experiment-proposal-2026-10-03-v4.md`, all 4,219 lines); the
six ruling files of 2026-10-03 and the packet
`docs/rulings/2026-10-03-version-4-questions-PROPOSAL.md`.

**Opened in part, to look up a figure or a sentence:** version 3 (one row of
its section 9); the findings of the controls re-run and of the short
pre-stated run; the checks of both; the two earlier ruling files that gained
dated notes; the December-result roadmap's outcome table; the compute ledger;
the toy code's constants; and the committed output files under
`experiments/rehearsal-successor-measure/`.

**Not opened:** any chat or transcript of another session; the first two
packets of 2026-10-03 (they were checked earlier, and version 4 quotes the
rulings and not the packets); the worktree of the session running the
competing solver.

**One thing found by accident and used:** a file outside the committed
record, `.venv-lock-2026-08-28.txt`, in the main checkout. Three documents
cite it, so this session looked at whether it is committed. It is not
(finding 9).

**Names used below.** The four trained systems are called what version 4
calls them, with the plain meaning first: the separable model (arm T), the
entangled model (arm C), the mixed model (arm M) and the freely trained model
(arm F). "The piece" is the part of the internal state that is actually
transplanted. "Record A" is the ruling record written by the session that
drafted version 4
(`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`). "Record B"
is the one written by the session that wrote the packet
(`docs/rulings/2026-10-03-version-4-questions-rulings.md`). "The
reconciliation" is John's ruling that record B stands on the four points
where they differ (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`).
Line numbers are version 4's at `41b0bd3`.

---

## The result in one page

**What held.**

- **Every number checked matches the record it cites.** 89 comparisons of
  toy figures against the committed output files, all equal. The site list in
  section 18 is the rule's output, set for set (325 and 45). Every dollar
  figure is in the ledger line or the note it names, and the arithmetic of
  section 12 comes out as printed.
- **The first three sets of rulings (the morning's sixteen pages, the three
  after the controls re-run, and the evening's two) are carried correctly.**
  36 rows checked, all "yes".
- **The passages marked "reconciled" say what the reconciliation says.**
- **The packet's numbers are right**, including the 0.9926 on its page 6, and
  the reasoning of page 6 holds.

**What did not hold.**

1. **Four sentences still give the separation between the two built models
   the old way**, seed by seed: lines 412 to 414, the second half of the cell
   at line 2256, lines 2418 to 2420 and line 3814. One of them sits in the
   same table cell as the reconciled wording.
2. **Version 4 carries record A's wording wherever the reconciliation's
   table did not list a difference, and record B says more in five such
   places.** The reconciliation says the two records "say the same thing" on
   everything outside its four rows. They do not quite. One of the five is a
   difference of substance: when the changed code for the other-agent control
   is written and tested (finding 4).
3. **Version 4 contradicts itself in one place that matters.** Section 7.2
   fixes the laptop's processor as the device for the registered accuracy;
   section 11, step 5a, still says that if the laptop cannot do it the work
   moves to rented time and "is said". Record B says that case is a fresh
   question for John.
4. **Two citations in the "pinned versions" passage do not check out.** The
   output file version 4 names records one library version of three. And the
   file given as the model for pinning is not committed: the repository's own
   ignore list keeps it out.
5. **The bookkeeping around the edges is stale**: the header still says three
   sets of rulings and pull request 83; section 19's heading still says each
   question was ruled "as suggested"; the printed output of section 17's text
   sweeps no longer matches the file.

**Is version 4 ready to become the registration text?** Yes, once the list in
section 4 below is made and the competing solver's run is written in. Nothing
found changes a number, a rule or a design choice. Every item is wording, a
citation or a carried-over sentence, and all of it can be done in one pass.
One item needs John first (question 1 at the end).

---

## 1. Job 1: does version 4 say what the rulings say?

One row per ruling. "Where" is the place in version 4 that carries it.

### 1.1 The morning rulings (`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`)

| Ruling | Where version 4 carries it | Carried correctly? |
|---|---|---|
| Page 1, item 1: only sizes of piece that themselves reach four fifths may be chosen; the count printed beside the whole read's; no size clearing returns "no verdict, read failed its floor" | section 6.4, item 2 (lines 1145 to 1154); section 7.2, items 1 and 3 (lines 1299 to 1307, 1544 to 1553); section 9, the fit-floor row | yes; it quotes the ruling's own words |
| Page 1, item 2: sections 3 and 5.2 reworded to "the read holds the label; the largest piece transplanted holds it; no size moves the action" | section 3 (lines 360 to 375); section 5.2 (lines 750 to 757) | yes |
| Page 1, item 3: the packet's forecast readings are not committed results; version 4 quotes the re-run | section 5.2 (lines 783 to 787); section 20 (lines 4083 to 4086) | yes; it says the forecast was wrong on one seed |
| Page 2: the controls re-run comes before the registration review; the mixed model's true-slot check cited to the review and re-confirmed | section 7.3 (lines 1739 to 1751); section 5.3 (lines 902 to 910); section 15, entry 25 | yes |
| Page 3, the read's accuracy as a count, on a named device (finding RT-232) | section 7.2, item 1 (lines 1320 to 1332) | yes |
| Page 3, the whole-state floor applied twice (RT-234) | section 6.4, item 1 (lines 1134 to 1144) | yes |
| Page 3, the fuller report for the first full-size run (RT-235) | section 7.5 (lines 2137 to 2144); section 11, step 5a | yes |
| Page 3, depths stated alike; two citations by main-line commit; a dated note in the earlier rulings file (RT-236) | section 7.2, item 1 (lines 1407 to 1414); the note exists (section 3.4 below) | yes |
| Decision 2: the separable model's ownership path is forced by its architecture | section 5.1 (lines 712 to 715); section 15, entry 2 | yes |
| Decision 3: the entangled model entangles by architecture, no penalty | section 5.2 (lines 815 to 818); entry 3 | yes |
| Decision 4: the two transplants are a subspace and its containing space at the same sites | section 6.2; entry 4 | yes |
| Decision 8: a new experiment directory; the ledger stays where it is | section 12.2 (lines 2673 to 2676); entry 8 | yes |
| Decision 9: the own-versus-named asymmetry recorded as a known limitation | section 4.2 (lines 557 to 558); weakness W6; entry 9 | yes |
| Decision 10: the channel-removal check is a precondition and never evidence of a centre | section 8.2 (lines 2225 to 2230); entry 10 | yes |
| Decision 13: the launcher waits for the receipt; the trainer does not delete its own machine | section 5 (lines 670 to 672); entry 13 | yes |
| Decision 15: the other-agent control's 0.05 tolerance (later withdrawn) | section 7.3, item 2; entry 15 | yes, as withdrawn |
| Decision 16: the too-early-position control reported only (later reversed) | section 7.3, item 4; entry 16 | yes, as reversed |
| Decision 17: fifty timed steps accepted; the five-hundred-step figure from the first full-size run | section 9 (line 2274); section 11, step 5a; weakness W8; entry 17 | yes |
| Decision 19: the position sets are the rehearsal's four | section 7.2, item 2 (lines 1451 to 1452); entry 19 | yes |
| Page 11, items 1 and 2: no verdict on the entangled model fires the two-model fallback; on the mixed model drops it | section 3 (lines 462 to 465); section 11, step 7 | yes |
| Page 11, item 3: the fifth registered term, "metric validated, degree not read", with its reason after a colon | section 3, the outcome table (line 313) and lines 340 to 342 | yes |
| Page 11, item 4: the roadmap's outcome list gains a dated note | section 3 (lines 301 to 304); the note exists | yes |
| Page 11, item 5: the fifth outcome is satisfactory and weaker than the first | the outcome table (line 313) | yes |
| Page 11, item 6: the stop after the first full-size run is unchanged | section 3 (lines 346 to 350); section 11, step 5a | yes |
| Page 15: the registration says what is true of the shutdown today; the repair comes off the Weekend 2 list; the caution is carried | weakness W9 (lines 2973 to 2982); entry 18 | yes |

### 1.2 The three rulings after the controls re-run (`docs/rulings/2026-10-03-controls-rerun-rulings.md`)

| Ruling | Where | Carried correctly? |
|---|---|---|
| 1, items 1 and 2: the other-agent control kept as a reported description; its pass line withdrawn | section 7.3, item 2 (lines 1775 to 1791); section 9 (line 2265) | yes |
| 1, item 3: the registration says it never ran at toy scale, why, and that no verdict is expected | lines 1792 to 1809 | yes |
| 1, item 4: its code run once with the floor off, labelled a test of the code | lines 1810 to 1830 | yes |
| 2, item 1: the too-early-position control's positions are those before both twins' first own turns | section 7.3, item 4 (lines 1871 to 1878) | yes |
| 2, item 2: it holds; its pass line is that nothing changes; the outputs themselves are compared; two shares reported | lines 1879 to 1889 | yes |
| 2, item 3: the "other routes" sentence withdrawn | lines 1902 to 1912 | yes |
| 2, items 4 and 5: reverses the morning's decision 16; run as a pre-stated quantity by another session; the diagnostic's figures not quoted as that run | lines 1913 to 1948; entry 16 | yes |
| 3: the piece's accuracy at the other positions of its site is a reported column, with no pass line, filled for the twelve toy models | section 7.2, item 3 (lines 1573 to 1644); section 7.5, column 3 | yes |

### 1.3 The evening ruling (`docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`)

| Ruling | Where | Carried correctly? |
|---|---|---|
| 1: the fifth outcome is satisfactory and stated as weaker than the first, in John's own words | the outcome table (line 313); entry 28 | yes |
| 2, items 1 and 2: the new figure printed both ways, neither with a pass line | section 7.2, item 3 (lines 1580 to 1583); section 7.5, column 3 | yes |
| 2, item 3, with its dated note: computed as section 4 of the short run's method states | lines 1585 to 1625 | yes; version 4 adds that the average is taken in 64-bit arithmetic and says that choice is its own |

### 1.4 The seven questions, as they stand after the reconciliation

"Record B only" marks something record B says and record A does not, outside
the four rows of the reconciliation's table. The reconciliation says both
records stand on everything else, so these are ruled too.

| Ruling | Where | Carried correctly? |
|---|---|---|
| 1: the floor is on the piece only; the whole read's count printed, not a second condition | section 6.4, item 2 (lines 1155 to 1168); section 7.2, item 1 (line 1317) | yes |
| 2: the piece rule is applied after the layers are chosen | section 7.2, item 3 (lines 1555 to 1562) | yes |
| 2, reconciled: the registration says in a sentence what that order can miss | lines 1562 to 1571 | yes there. **Partly** overall: the same order is stated without the sentence at line 2258 (section 9), line 3316 (section 15, entry 29) and line 4186 (section 20); section 7.4's list of what is frozen does not name it; section 9 has no row for it |
| 3: the laptop's processor; 32-bit states; the read fitted in 64-bit | section 7.2, item 1 (lines 1332 to 1336); section 9 (line 2260) | yes |
| 3, reconciled: the library versions pinned in a committed file named in the registration | lines 1338 to 1344; section 7.4 (line 2074); section 9 (line 2260); section 20 (lines 4187 to 4188) | **partly**: the ruling is stated correctly, but the two things cited beside it do not check out (findings 8 and 9) |
| 3, record B only: if the processor proves impractical at full size, that is a fresh question for John, not a switch | nowhere | **no**; and section 11, step 5a (lines 2520 to 2524) says the opposite (finding 5) |
| 4: the toy's episode counts at full size | section 7.4 (lines 2067 to 2071); section 8.1 (lines 2175 to 2176); section 9 (line 2276) | yes; the counts are the toy code's (finding 12) |
| 4, reconciled: the band that sampling alone puts around each count against the four-fifths floor is printed beside it | section 7.4 (lines 2072 to 2073); section 7.5, column 4; section 9 (line 2276) | yes |
| 4, record B only: a miss at the first full-size run goes to John with that band beside it | not in section 11, step 5a, nor in stop condition S4a (lines 2578 to 2583) | **partly**: the band is in the table row that run prints, but the two passages that say what goes to John do not name it |
| 5: the other-agent control is compared with twenty random pieces, reported as the neighbouring control reports them | section 7.3, item 2 (lines 1781 to 1785, 1831 to 1838); section 7.5, column 14 | yes |
| 5, record B only: the code is changed and the code test of 2026-10-03 is run once more on the changed code, before the registration review | lines 1834 to 1836 say the change is "owed with the registered measurement"; section 17 (lines 3866 to 3868) lists it with the code owed before step 4 | **no**: version 4 follows record A's timing (finding 4) |
| 6, part 1: a model is read if at least two of its three seeds read; the third reported | section 3 (lines 469 to 477); section 9 (line 2277) | yes |
| 6, part 2, reconciled: the separation is the lowest reading among the entangled model's seeds that read minus the highest among the separable model's; at least 0.5; seeds not paired by number | section 3 (lines 477 to 487); section 7.4 (lines 2074 to 2075); section 9 (lines 2256, 2277) | **partly**: stated correctly in those places, and stated the old way in four others (finding 1) |
| 6, what follows: "metric validated" and "degree read" defined; the free model reading on one seed only gives the fifth outcome with that figure as a description | section 3 (lines 481 to 486) | yes |
| 7: the competing solver's three committed models are put through the measurement before the registration review, method first, by another session, and checked | section 7.3, last paragraph (lines 1996 to 2017); section 8.1; section 10, item R-5; section 11, step 1 | yes |
| 7, record B only: the method states what "the model's own turn" and its twin pairing mean for a solver with no acting channel; a reading on any seed goes to John before anything else moves | nowhere | **no** |

### 1.5 The reconciliation (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`)

| Ruling | Where | Carried correctly? |
|---|---|---|
| Record B stands on the device point (pinned) | as 1.4 | partly, as above |
| Record B stands on the order of the piece rule (what it can miss) | as 1.4 | partly, as above |
| Record B stands on the episode counts (the band) | as 1.4 | yes |
| Record B stands on seeds that disagree (the separation) | as 1.4 | partly, as above |
| Version 4 carries a notice at its head naming the ruling | lines 47 to 58 | yes |
| Version 4 is edited at its header table, sections 3, 7.2, 7.4, 7.5, 9 and 20 | the header table (line 75) and sections 3, 7.2, 7.5: all four points where they apply. Section 7.4: three of the four (not the order of the piece rule). Section 9: three of the four (the same one missing). Section 20: one of the four (pinned only) | **partly** |

### 1.6 Finding 1 (MEASURED): four sentences still state the separation seed by seed

The command is `stale_search.sh` in the folder beside this file; its full
output is `stale_search.out.txt`. The lines that matter:

```
$ sh experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/stale_search.sh
...
413:separation, arm C minus arm T, is 1.0051, 0.9926 and 0.9974 and clears 0.5 on
478:separation is not compared seed by seed.** It is the lowest reading among arm
...
--- 'clear(s|ed) ... every seed' and the three per-seed figures given as the separation
2256:| Separation bar between arms T and C (R1 against R2) | **0.5**: the minimum gap ... **Reconciled 2026
2419:  0.873 to 0.885 on 2026-09-21, and cleared at 1.0051, 0.9926 and 0.9974 under
3814:- **The separation line** (0.5 on every seed): produced (failure 2's output).
```

Each was then read in place:

| Line | Section | What it says | Verdict |
|---|---|---|---|
| 412 to 414 | 3, "The toy outcome" | "the separation, arm C minus arm T, is 1.0051, 0.9926 and 0.9974 and clears 0.5 on every seed" | **old way.** Under the ruling the toy's separation is one number, 0.9926 |
| 2256 | 9, first row | the first half of the cell is the reconciled wording and gives 0.9926; the second half says "the toy cleared it on every seed, at 1.0051, 0.9926 and 0.9974" | **old way, in the same cell as the new** |
| 2418 to 2420 | 10, item R-10 | "cleared at 1.0051, 0.9926 and 0.9974 under the registered rules" | **old way** |
| 3814 | 17, candidate 7 | "The separation line (0.5 on every seed): produced" | **old way.** The command output it points to (lines 3545 and 3561) prints the per-seed field of the output file, which is fine as output; the sentence is what is stale |
| 4024 to 4025 | 19, question 6 | the bar "is written 'per seed'" | left as put, by design. But see finding 3 on section 19's heading |

The three figures are right as the entangled model's three readings. What is
stale is calling them three separations and saying the bar clears "on every
seed". Nothing else in the document states the separation the old way: every
other line the search prints for this point either states it the new way or
uses "separation" for something else (partial separation within a trial).
Reading the whole document found no old-way sentence that the search
patterns miss.

### 1.7 Finding 2 (MEASURED by the same search, then read): the other three points

- **Library versions.** No sentence in the body states "recorded" without
  "pinned". Line 1336 says "recorded" and the next sentence adds "also
  pinned". Section 19, question 3 (lines 3984 to 3988) has "recorded" alone,
  left as it was put.
- **Episode counts without the band.** Section 7.4 (lines 2067 to 2071)
  gives the counts and the next bullet gives the band. Section 9 (line 2276)
  has both. No stale sentence. Two passages that describe what goes to John
  at the stop after the first full-size run do not mention the band: section
  11, step 5a (lines 2502 to 2507) and stop condition S4a (lines 2578 to
  2583). Section 6.4, item 2, lists what is printed beside the count and does
  not list the band either.
- **The order of the piece rule without what it can miss.** Three places
  give the order alone: line 2258 (section 9, the fit-floor row, cited to
  record A's ruling 2), lines 3316 to 3317 (section 15, entry 29) and line
  4186 (section 20). Weakness W12, where the packet said the sentence would
  also go, does not carry it; record B does not require it there.

### 1.8 Finding 3 (MEASURED by reading): places that cite record A for something record B settled, or that predate the reconciliation

===== END OF RECORD 14, part 1 =====

