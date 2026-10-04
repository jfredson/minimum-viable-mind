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

- Line 470 (section 3) cites record A's ruling 6 for the seeds rule. Fine
  for part 1; the reconciled part cites record B at line 485.
- Line 2260 (section 9, the device row) cites record A's ruling 3 for a cell
  that now includes "pinned", which record A's ruling 3 says the opposite of.
- Line 2276 (the episode-counts row) cites record A's ruling 4 for a cell
  that now includes the band, which record A does not have.
- Line 2277 (the seeds row) cites "the same file, ruling 6", which is record
  A, for a cell whose second half is record B's.
- Lines 3314 to 3321 (section 15, entry 29) list the seven rulings as record
  A has them and cite record A only.
- Line 3940 (the heading of section 19) says "each now ruled as suggested",
  and lines 3943 to 3944 say John ruled "taking the suggestion in each". On
  four of the seven the suggestion was not what was finally ruled. Section 19
  has no notice of the reconciliation.
- Section 20's entry for the seven questions (lines 4182 to 4195) carries one
  reconciled point of four.

### 1.9 Finding 4 (MEASURED by reading the two records side by side): the records differ on when the other-agent control's code is changed and tested

- **Record A**, ruling 5 and "What this changes": the change "is not quite
  the one registered", and it is listed as "code owed with the registered
  measurement".
- **Record B**, ruling 5 and "What this changes": "the code changes
  accordingly, and the code test of 2026-10-03 is run once more on the changed
  code", listed under "Before the registration review, at $0".

The reconciliation's table does not list this, and its text says the records
agree on question 5. Version 4 follows record A (lines 1834 to 1836; section
17, lines 3866 to 3868), and its header (lines 15 to 26) names three things
that stand in front of the registration review, of which this is not one.

Doing it record B's way satisfies both records. It is still a choice between
two things John agreed to, so it is question 1 at the end.

### 1.10 Does version 4 contradict itself?

**On the four reconciled points:** yes, on the separation (finding 1). Not on
the other three, where the old wording is absent or left as put.

**Elsewhere:**

- **Finding 5 (MEASURED by reading; the consequence ARGUED).** Section 7.2,
  item 1 (lines 1332 to 1333) says the registered accuracy "is computed on
  the laptop's processor, never its graphics chip". Section 11, step 5a
  (lines 2520 to 2524) says the fit is computed on the laptop and that "if
  that turns out not to be so, the cost goes into the first release's
  rehearsal line and is said", which is a move to a rented machine by the
  session's own decision. Record B's ruling 3 says that case "is a fresh
  question for John, not a switch". The sentence in section 11 is carried
  from version 3 and predates the ruling.
- **Finding 6 (MEASURED by counting).** Line 64 says "the first ten rows are
  new since version 3"; line 4197 says "the eight new ones first". The source
  table has ten rows above the first one carried from version 3.
- **Finding 7 (MEASURED by reading).** Counts of the day's rulings are stale
  in four places. Line 8: "John's three sets of rulings of 2026-10-03" (there
  are five, and the reconciliation). Line 3342: "the three rulings of
  2026-10-03 this version is built to", in a list that names neither record B
  nor its packet nor the reconciliation. Line 4056: "the three rulings of
  2026-10-03 were each given as agreement"; the reconciliation was given in
  John's own words. Lines 62 to 64, 75, 3373 to 3375 and 4183: record A is
  "filed with this version on pull request 83" and is the one source "not on
  the main line"; both are on the main line at `41b0bd3` through pull request
  85, which superseded 83 and 84.
- **A small one, carried from version 3 (MEASURED,
  `site_sets_and_arithmetic.out.txt`).** The whole successor is "about $194
  to $206" at line 2541 and "about $192 to $204" or "about $193 to $205" at
  line 2763. All three are correct sums of different things (which split of
  the two releases, and whether the mixed model's $1.94 development run is
  counted inside its $32 to $44). A reader meets three ranges for one
  quantity.

Nothing else was found. In particular the three controls that hold are the
same three everywhere they are listed (sections 6.4, 7.3, 7.4, 7.5 and
weakness W14), and the five outcome terms are the same wherever they appear.

---

## 2. Job 2: do version 4's numbers match the records they cite?

### 2.1 The toy figures (MEASURED)

The script reads the committed output files and prints each figure beside
what version 4 prints. It loads no model.

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/toy_figures.py
...
ALL MATCH
$ grep -c '^MATCH' .../toy_figures.out.txt
89
```

The full output, 317 lines, is `toy_figures.out.txt` beside the script. What
the 89 comparisons cover, with one sentence each on whether it matches:

- **Every reading.** The separable model reads 0.0000 on every seed, the
  entangled model 1.0051, 0.9926 and 0.9974, the mixed model 0.4886, 0.4860
  and 0.5449, and the freely trained model is marked "described only": all
  match. The number the arithmetic would have returned for the free model
  (1.0000, 1.0000, 1.0108) matches.
- **The separation.** The lowest of the entangled model's readings minus the
  highest of the separable model's is 0.9926: matches. The output file's own
  `separation` field holds the three per-seed figures.
- **The entangled model's table in section 5.2**, all three rows (site, size
  of piece, the two counts of 180, the three shares): match. The largest gap
  between the ownership-only share and the no-transplant rate is 0.0037,
  inside the "within 0.004" the text states.
- **Every count against the four-fifths floor of 144 of 180.** The free
  model's best piece at any layer, size or seed is 34: matches. Its whole
  read at the first layer is 32, 12 and 18: matches. Every chosen piece on
  the three built models is at or above 144, the lowest being 150: matches.
  Every chosen piece's whole read is 176 or more: matches.
- **The whole-state floor.** 0.4433 against 0.4280 on the free model's first
  seed, 9 episodes of 600: matches. It clears on fresh episodes on all
  twelve: matches. The smallest denominators, 0.4863 and 0.4263: match.
- **The controls.** The complement shares of control 1 on all four models;
  control 3's counts below, equal and above (20 above on the entangled
  model's first seed; 6, 1, 13; 6, 5, 9) and the mixed model's random medians
  of 0.015 to 0.019; control 6's 81 and 719 trials and its shares; control 7
  bit-identical at fifteen different places: all match. The old definition of
  control 4 was above the no-transplant rate by 0.065 to 0.10 on six models
  and by 0.005 or less on six: matches to the two decimals printed (the
  largest is 0.1013).
- **The rider and the true-slot reference.** The whole-state shares at the
  separable model's site on the other three models; the mixed model's
  true-slot reading of 0.4837, 0.4760 and 0.4920; the gaps of 0.0049, 0.0099
  and 0.0529 (the middle one is 0.00992 unrounded): all match.
- **The other-agent control on the one model that learned its condition.**
  The best whole read 137 and the best piece 139 of 180; the candidates at
  layers 1 and 3: match.
- **The entangled model's second seed.** The choice between layer 1 and
  layer 4 was 0.0533 against 0.0517 on development episodes, one episode of
  600: matches.
- **The short pre-stated run.** The redefined control 4 holds on all twelve
  with identical outputs and no action changed; 1 to 21 positions per pair,
  about 5 on average; the piece's counts away from the action position on the
  entangled model (139, 139, 33 and 113 on the average; 30 to 139 and 123)
  and on the mixed model (163, 174, 175 on the average; 144 reached at four,
  four and seven positions of ten; 34, 71 and 33 at the fourth token); the
  free model's one outlier of 145; the three figures from the code test
  labelled NOT A RESULT (0.0012, 0.0063, 0.0962, with a piece right on 92):
  all match.
- **The gate file.** The bar of 790 of 3,000; the named-other counts (994,
  781, 746 and 760, 751, 708); every range quoted for the four models and the
  two competing solvers; the channel-removal figures including the separable
  model's third seed at 0.2733: all match.

Looked up by hand and matching: 407 of 800 pairs is 0.5088 (the check of the
controls re-run, line 247); "about 26,700 values" (the same check, line 118);
the three figures that moved by one episode under a different order of
addition, and 92 and 24 in 64-bit (the check of the short run, finding 11);
the method and the output of the short run committed 2 minutes 39 seconds
apart (the two commits' author times, 18:22:10 and 18:24:49); 0.9975 for the
entangled model's second seed at layer 4 (the controls re-run's findings,
line 112).

### 2.2 The site list of section 18 (MEASURED)

The script builds every site set as a pair and applies the exclusions, a
different route from the row-by-row count in section 18, then parses the list
printed in version 4 and compares set for set.

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/site_sets_and_arithmetic.py
=== 1. The site-set rule, run
states | contiguous layer sets | full family | registered | x4 | narrower | x4 | stricter | x4
     5 |                    15 |          60 |         45 |  180 |       55 |  220 |       40 |  160
    13 |                    91 |         364 |        325 | 1300 |      351 | 1404 |      312 | 1248

=== 2. The list printed in section 18, parsed and compared set for set
registered model: printed list holds 325 site sets; the rule gives 325; in the list and not the rule: 0; in the rule and not the list: 0
toy model: printed list holds 45 site sets; the rule gives 45; in the list and not the rule: 0; in the rule and not the list: 0

=== 3. What the toy code asserts
   rerun_controls.py: assert len(FAMILY) == 45 and len(FAMILY) * len(RANKS) == 180 and len(STRICT) == 40
```

All eight counts in section 7.2, item 2, and the printed list match the rule.

### 2.3 Thresholds (MEASURED, the same script)

```
=== 4. Thresholds
gate bar: smallest count with a one-sided tail at or under 0.05 at one in four, of 3,000: 790 (share 0.2633, tail 0.0485)
four fifths of 180: 144 | one episode of 180: 0.0056
no-transplant formula at own-directed 0.2633: 0.1052; a broken pairing (0.1250) misses by 0.0198; margin over 0.018: 0.0018
no-transplant formula at own-directed 0.56: 0.0629; a broken pairing (0.1250) misses by 0.0621; margin over 0.018: 0.0441
graphics-chip fits as shares of 180: 31, 12, 19 -> [0.172, 0.067, 0.106]
407 of 800 = 0.50875 | 483 of 800 = 0.60375 | 1810 of 3000 = 0.6033
```

Each matches what version 4 prints.

### 2.4 Dollars (MEASURED)

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/ledger_lookup.py
the last row of the run table is line 95 dated 2026-09-25
FOUND   | 228.15       | spent across the programme | line 95
FOUND   | 46.75        | Amendment A3 against its $100 stop | line 95
FOUND   | 9.43         | rehearsal line left, of $10 | line 95
FOUND   | 0.0525       | second attempt cost | line 95
FOUND   | 75.8645      | vendor balance on 2026-09-26T01:54Z | line 95
FOUND   | 0.4974       | first attempt cost | line 94
FOUND   | 0.02         | the 2026-09-21 slice row | line 93
FOUND   | 8.47         | 2026-08-08 anomaly, billed and existed hours | line 93
FOUND   | 2.42         | 2026-08-08 anomaly, billed and existed hours | line 93
FOUND   | 8.47         | the same, in the note | line 423
FOUND   | 2.42         | the same, in the note | line 423
FOUND   | 20.28        | two-run pod-hours and rate | line 88
FOUND   | 0.99         | two-run pod-hours and rate | line 88
FOUND   | 1.943        | 10-million run trued up | lines 393 and 400
FOUND   | 450          | ceiling raised to $450 on 2026-09-25 | the top of the file
...
nothing missing
```

Every figure section 12 cites to a ledger line is on that line. The thirteen
figures cited to the note that recomputed the second release are in its
committed output. The ledger has no row after line 95, as section 12.1 says.
The arithmetic (section 5 of `site_sets_and_arithmetic.out.txt`): $221.85 of
headroom, $0.57 spent on the rehearsal, $7.77 for four development runs,
$10.04 a run, $163.06 on the ruled split, $422.05 and $434.05 after the
successor, $14.79 and $17.03 left at the two ends the wager names: all as
printed. The eight runs come to $84.04 from the rounded per-run figures and
$84.06 in the note, which works from unrounded ratios; version 4 quotes the
note.

### 2.5 The repository's two checkers (MEASURED)

The headline lines of each; the full outputs are beside the scripts.

```
$ .venv/bin/python scripts/check_citations.py --only docs/successor-experiment-proposal-2026-10-03-v4.md
[CONFIDENT] 0 reference(s) name a file that is not in the repository
[LOOK AT IT] 8 bare name(s) match more than one file
[LOOK AT IT] 1 name(s) of run-output files that are not in the repository
  docs/successor-experiment-proposal-2026-10-03-v4.md:1320  .venv-lock-2026-08-28.txt
[LOOK AT IT] 12 reference(s) written with a gap or a wildcard that matched nothing
[NOT CHECKED] 1 reference(s) to files outside this repository
[CONFIDENT] 1 exact figure(s) absent from the one file their sentence cites
  docs/successor-experiment-proposal-2026-10-03-v4.md:850
      figure: 1,810    cited: out-repairs/gate_base.json
[LOOK AT IT] 16 figure(s) worth a human eye
Confident findings: 1. Things for a human to look at: 37.

$ .venv/bin/python scripts/check_single_source.py --only docs/successor-experiment-proposal-2026-10-03-v4.md
[CONFIDENT] Group 1: a dollar figure the ledger does not contain
0 found.
[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source
2 found.
  docs/successor-experiment-proposal-2026-10-03-v4.md:2645   $44
  docs/successor-experiment-proposal-2026-10-03-v4.md:2645   $131
[LOOK AT IT] Group 3: in the ledger, and no source named
3 found.
Confident findings: 2.
```

Both exit with status 1, which is what they do when anything confident is
found. Full outputs are beside the scripts. What each confident finding is:

- **The 1,810** (line 850 of version 4 as the checker counts paragraphs; the
  sentence is at lines 858 to 860). The file holds the share, 0.6033, in the
  field the sentence names, and 0.6033 of 3,000 is 1,810. The count is right
  and is arithmetic on the cited field. Version 4's section 17 says the same.
- **The $44 and $131** are cited to the ruling that set them, which is their
  source. Version 4's section 17 says the same.
- The 16 figures "worth a human eye" are four-decimal roundings of values
  the cited files hold at full length; this session's script compared those
  same values and they match.
- **The one new thing the checker shows is the lock file**, which leads to
  finding 9.

These results agree with what version 4's section 17 prints for the same two
commands.

### 2.6 Finding 8 (MEASURED): the output file records one library version, not three

Version 4, lines 1336 to 1338: "the versions of torch, scikit-learn and numpy
are recorded in the output file, as the controls re-run did (torch 2.12.1,
scikit-learn 1.9.0, numpy 2.5.0, `out-controls-rerun/summary.json`)".

```
=== 12. What summary.json records about the software (section 7.2 item 1)
    top-level fields of summary.json other than arms and separation: {'device': 'cpu', 'seconds': 967.1754839420319, 'torch': '2.12.1'}

$ grep -rn -i 'scikit\|sklearn\|numpy' experiments/rehearsal-successor-measure/out-controls-rerun/summary.json experiments/rehearsal-successor-measure/out-controls-rerun/table.md experiments/rehearsal-successor-measure/out-short-prestated-run/*.json experiments/rehearsal-successor-measure/out-short-prestated-run/stdout.txt
(no output)
```

The three version numbers are true: they are what the project's environment
holds today, and the findings of the controls re-run state them in prose
(`docs/2026-10-03-controls-rerun.md`, line 64). But the output file records
torch only. So "as the controls re-run did" is right for one library of
three, and the registered code has to write the other two for the sentence to
be true of the registered run.

### 2.7 Finding 9 (MEASURED): the file given as the model for pinning is not committed

Version 4 (line 1340), the packet (page 3) and record B (ruling 3) all say
the versions are pinned in a committed file "in the way
`.venv-lock-2026-08-28.txt` does for the project's environment".

```
$ git ls-files | grep -i -E 'lock|requirements'      (no line for .venv-lock-2026-08-28.txt)
$ git check-ignore -v .venv-lock-2026-08-28.txt
.gitignore:35:.venv-lock-*.txt	.venv-lock-2026-08-28.txt
$ git log --oneline --all -- .venv-lock-2026-08-28.txt
f222c94 WIP snapshot 2026-08-29: uncommitted working files (repo census)
$ git merge-base --is-ancestor f222c94 HEAD && echo "on main line" || echo "not an ancestor of the main line"
not an ancestor of the main line
```

The file exists in John's main checkout and lists the right versions
(`torch==2.12.1`, `scikit_learn==1.9.0`, `numpy==2.5.0`). It is not on the
main line: line 35 of `.gitignore` keeps every file of that name out, and
the one commit that holds it is a work-in-progress snapshot on a side branch.
So the example of "a committed file" is a file the record does not hold.

This does not touch the ruling, which is that the versions are pinned in a
committed file named in the registration. It means the registration cannot
point at that file as it stands, and a file named the same way would be
ignored again. **ARGUED, one more thing for whoever writes the pin file:**
scikit-learn's logistic regression does its fitting through scipy, so scipy's
version can move a fit as much as the three named libraries can. The lock
file lists it (`scipy==1.18.0`); the sentence in version 4 does not.

### 2.8 Finding 10 (MEASURED): section 17's printed sweep output no longer matches the file

Section 17 prints the output of text searches run on sections 0 to 16. Run
again on the file as it stands:

```
$ sh experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/section17_sweeps.sh
--- failure 2, part one (section 17 prints lines 1256, 1257, 1258, 1262)
1277: ...   1278: ...   1279: ...   1283: ...
--- failure 4, part one (section 17 prints 759, 233, 68, 14, 3406, 8)
761
235
68
14
    3449
8
```

The text grew by 43 lines after the sweeps were run (the seven rulings and
the reconciliation were written in), so four of the printed numbers and the
four line numbers are out of date. The conclusions drawn from them do not
change. Every other command block in section 17 reads the committed output
files, and this session's own script found the same values.

---

## 3. Job 3: the packet, the two records and the reconciliation

### 3.1 The packet (`docs/rulings/2026-10-03-version-4-questions-PROPOSAL.md`)

Every number, against the place it cites:

| Page | What it states | Matches? |
|---|---|---|
| 1 | On the one model where the named agent's read was tried, the 8-direction piece was right on 139 of 180 and the whole read on 137; both readings give the same twelve verdicts | yes (MEASURED: `toy_figures.out.txt`, sections 4 and 8) |
| 2 | Candidates at layers 1 and 3, best pieces 92 and 115; layer 2, not a candidate, best piece 139; none reached 144 | yes (MEASURED: the same output, section 8) |
| 2 | "about $44" for the first release | yes (section 12.3 of version 4) |
| 3 | Two reads moved by one held-out episode between the processor and the graphics chip; every toy figure since the controls re-run was computed on the processor | yes (32 against 31 and 18 against 19; `device: cpu` in both runs' output files) |
| 3 | `.venv-lock-2026-08-28.txt` "already does" this "for the project's environment" | **partly**: the file exists and lists the versions; it is not a committed file (finding 9) |
| 4 | The toy's counts: 600 development episodes, the last 180 held out; 800 fresh pairs; 800 on the relaxed set; 3,000 for the gates; 200 shuffles | yes (finding 12 below) |
| 4 | With 180 held out the floor is 144; one episode is 0.0056; a piece at exactly four fifths lands "within about three points either way (roughly 139 to 149) on most draws" and passes "about half the time"; three times as many episodes narrows the band "to under two points" | yes, as arithmetic (finding 11 below) |
| 5 | The code draws one random piece; the neighbouring control draws twenty | yes (`N_RANDOM = 20` in the toy code; the check of the controls re-run, section 4, item 4) |
| 6 | The entangled model reads 1.0051, 0.9926 and 0.9974; the separable model 0.0000 on every seed; the proposed separation is 0.9926 | **yes** (MEASURED: `toy_figures.out.txt`, section 2) |
| 6 | "Amends: the ruling of 2026-09-25 that set the separation bar 'per seed'" | **no.** Page 1a of that ruling does not say "per seed"; the words were added by the proposal (version 3, section 9, line 1628). Record B says this correctly and the packet does not |
| 7 | The three ownership-blind models are committed with fingerprints | yes (three files; three lines in `SHA256SUMS`) |

**Finding 11 (MEASURED: `site_sets_and_arithmetic.out.txt`, section 4).** The
sampling arithmetic of page 4:

```
sampling spread of a count of 180 at a true share of 0.8: one standard deviation 5.37 episodes (0.0298); two 10.7 episodes (0.060)
a piece whose true accuracy is exactly 0.8 reaches 144 of 180 with probability 0.544; lands in 139 to 149 with probability 0.695
at three times as many held-out episodes (540): one standard deviation 0.0172
   a piece whose true accuracy is 0.78 reaches 144 of 180 with probability 0.293
   a piece whose true accuracy is 0.82 reaches 144 of 180 with probability 0.789
```

"About three points either way on most draws" is one standard deviation and
holds on about seven draws in ten. "About half the time" is 0.54. "Under two
points" is 0.017. All fair. **One sentence is stronger than its arithmetic
(ARGUED):** "at 180 the floor cannot tell 0.78 from 0.82". A piece at 0.78
passes about three times in ten and a piece at 0.82 about eight times in ten.
The floor tells them apart poorly, which is the point being made; "cannot
tell" overstates it. Nothing ruled rests on that sentence.

**Finding 12 (MEASURED).** The counts are the toy code's:

```
rerun_controls.py:45:HELD_OUT, PIECE_MIN = 180, 144                   # rule 7: four fifths of 180
rerun_controls.py:269:    dev_pairs, _ = T.make_data(600, seed=4242, pool="dev", device=DEVICE)
rerun_controls.py:270:    fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=DEVICE)
rerun_controls.py:271:    coll_pairs, _ = T.make_data(800, seed=778, pool="fresh", device=DEVICE, collide=True)
repairs.py:50:GATE_EPISODES = 3000
rerun_v3.py:69:N_PERM = 200
```

**Does each page state its options fairly?** (ARGUED throughout.)

- **Pages 1, 5 and 7:** yes. Each gives the alternative its real cost and
  its real merit.
- **Page 2:** yes. It gives the case against its own recommendation in
  figures, and the toy instance it quotes is one where the order made no
  difference, which it says.
- **Page 3:** mostly. The choice version 4 had left open, pin or only
  record, is given as part of the recommendation and not as two options with
  a case for each. The case for recording only is not stated. It is a small
  point and the recommendation is the more careful of the two.
- **Page 4:** yes, and it is candid that the alternative "is the better
  instrument".
- **Page 6:** yes on part 1. On part 2 see below.

**Page 6, part 2: does the reasoning hold?** (ARGUED, with the arithmetic
MEASURED.) The proposal is that the separation be the lowest reading among
the entangled model's seeds that read, minus the highest among the separable
model's. Three claims are made for it.

1. *"Seed 0 of one model has no relation to seed 0 of another."* **Holds,
   with one qualification.** The two are separate trainings of different
   architectures; nothing about the trained models is matched by the shared
   number. The qualification: a shared seed number may mean the two trainings
   drew the same stream of training episodes, so "no relation" is slightly
   too strong. It does not rescue the pairing, because nothing in the measure
   uses that.
2. *"With two seeds reading on one model and three on the other, the pairing
   is not even defined."* **Holds.** This is the stronger argument: once
   part 1 allows a model to read on two seeds, a rule paired by number has
   nothing to say when the missing seeds differ.
3. *"It is the stricter of the two ways."* **Holds.** Whatever the pairing,
   each paired gap is at least the lowest of one minus the highest of the
   other. So if the proposed separation clears 0.5, every paired gap does.

And the 0.9926 is right.

**One consequence the packet does not state (ARGUED), which John may want to
know he has ruled.** Part 1 forgives one seed of three that returns no
verdict. Part 2 does not forgive one seed that returns a reading and reads
oddly. If one seed of the entangled model read 0.3 and the other two read
near 1, the separation would be 0.3 and the outcome would be "metric does not
separate". If that same seed had returned no verdict, it would be set aside
and the metric would be validated on the other two. So a bad seed that fails
its floor costs nothing and a bad seed that passes its floor can decide the
outcome. That is defensible: a built model that reads low is evidence against
the measure and a model that returns nothing is not. But it is a real
property of the rule, it is new, and nothing has rehearsed it. It is question
2 at the end, with the suggestion that it stand and be said.

### 3.2 Record B against the packet: no more and no less?

Ruling by ruling, record B records what the packet's page recommended, in the
packet's terms, with these exceptions:

- **One thing more.** Ruling 7 ends: "a reading on any seed goes to John
  before anything else moves". The packet's page 7 says that if the result is
  not a no verdict "something is wrong with the measure and it is far better
  to learn it now". It does not put a stop to John. The record's sentence is
  a reasonable reading of that, and it is the record's.
- **One correction.** The packet's page 6 says page 1a of the earlier ruling
  set the bar "per seed". Record B's ruling 6 says page 1a "did not say how
  the gap is taken across seeds; the proposal's 'per seed' was the
  proposal's". The record is right and the packet was wrong (the table
  above). The record says less than the packet here, correctly.
- **Nothing less** otherwise. The clause in ruling 3 about the processor
  proving impractical is in the packet, in the paragraph on the strongest
  alternative. The clause in ruling 4 about a miss going to John with the
  band is in the packet's recommendation.

Record B's caution 3 says plainly that part 2 of ruling 6 was that session's
own proposal and is in no earlier document. That is accurate.

### 3.3 The reconciliation's table of four differences

| Row | Record A, as the table gives it | Record B, as the table gives it | Matches the two records? |
|---|---|---|---|
| Question 3, the device | recorded and not pinned | pinned in a committed file named in the registration | yes (A, ruling 3, item 3; B, ruling 3) |
| Question 2, the order of the piece rule | confirmed as run | confirmed as run, and the registration says what it can miss | yes |
| Question 4, the episode counts | the toy's counts | the toy's counts, and the band printed at the floor | yes |
| Question 6, seeds that disagree | two of three; the separation "cleared if cleared on two or more seeds", compared seed by seed | two of three; the lowest minus the highest, not paired by number; what "metric validated" and "degree read" mean | yes in substance. The words the table puts in quotation marks for record A are a paraphrase: record A says the bar "is cleared if the entangled model's reading minus the separable model's is 0.5 or more on at least two of the three seeds, compared seed by seed as before" |

**Do the two records differ anywhere the table does not list? Yes, in six
places** (MEASURED by reading the two side by side). The reconciliation says
the records "agree on questions 1, 5 and 7" and that "on everything else the
two records say the same thing and both stand".

| Question | Record A | Record B | Kind of difference |
|---|---|---|---|
| 5 | the code change is "owed with the registered measurement" | the code is changed and its test run once more "before the registration review" | **substance: when** (finding 4) |
| 7 | nothing on either point | the method states what "the model's own turn" and its twin pairing mean for a solver with no acting channel; a reading on any seed goes to John before anything else moves | B says more |
| 3 | nothing on the point | if the processor proves impractical at full size, that is a fresh question for John, not a switch | B says more |
| 4 | "at 180, one episode is 0.0056" | the same, and that a piece at exactly four fifths passes about half the time, and that a miss at the first full-size run goes to John with the band beside it | B says more |
| 6 | a model "returns no verdict, as an arm, if two or more of its seeds return no verdict"; "every seed is printed" | if the free model reads on one seed only, the outcome is the fifth term and that seed's figure is printed as a description | each says something the other does not; they agree |
| 1 | "Nothing here edits ... any earlier ruling file" | the earlier ruling on the floor gains a dated note | a difference in what each record did, not in what was ruled |

None of these is a contradiction that needs undoing: where record B says
more, it stands by the reconciliation's own rule that both stand, and nothing
in record A forbids it. The one that changes what happens and when is
question 5. **The practical cost of the table's four rows being taken as the
whole list is section 1.4 above: version 4 was edited at the four listed
points and still follows record A on the unlisted ones.**

### 3.4 The dated notes

| Note | Where | Accurate? |
|---|---|---|
| Beside item 1 of the ruling on finding RT-212 (the floor was on the whole read; now on the piece, and the whole read is not a second condition) | `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`, lines 46 to 52 | yes; it cites the morning's page 1 and record B's ruling 1, and leaves item 1 as written |
| Beside the phrase "a five-layer model" (four blocks and five states against twelve and thirteen) | the same file, lines 346 to 351 | yes |
| Beside page 1a (the separation bar does not say how the gap is taken across seeds; now the lowest minus the highest, not paired) | `docs/rulings/2026-09-26-weekend-1-queue.md`, lines 37 to 42 | yes. It is right that page 1a is silent on seeds. It leaves out "among the seeds that read" for the separable model, which the ruling has for both; a reader would not be misled |
| At the head of record A (a second record exists; the four points; record B stands) | lines 15 to 26 | yes; its one-line summary of each of the four points is right |
| At the head of record B | lines 16 to 22 | yes |
| Under the roadmap's outcome table, two notes (the fifth term; then John's own words) | `docs/december-result-roadmap-2026-09-20.md`, lines 87 to 98 | yes |

Each note is dated, says the text beside it is left as written, and points
at the ruling. None rewrites the sentence it sits beside.

---

## 4. What needs changing in version 4, by section and line

For the session that writes the registration text, in document order. None
changes a number or a rule.

| # | Where (lines at `41b0bd3`) | Change | From |
|---|---|---|---|
| 1 | Header, line 8 | "John's three sets of rulings of 2026-10-03" becomes five sets and the reconciliation | finding 7 |
| 2 | Header, lines 15 to 26 | Add to what stands in front of the registration review: the other-agent control's changed code and its repeated code test, if question 1 is ruled as suggested | finding 4 |
| 3 | Lines 28 to 35, 62 to 64; source table, line 75; section 16, lines 3373 to 3375; section 20, line 4183 | Record A is on the main line at `41b0bd3` (pull request 85, which superseded 83 and 84). Give record B, its packet and the reconciliation their own rows in the source table and their own entries in section 16 | finding 7 |
| 4 | Section 3, lines 412 to 414 | The toy's separation is 0.9926, the lowest of the entangled model's readings minus the highest of the separable model's; drop "clears 0.5 on every seed" | finding 1 |
| 5 | Section 3, line 470 | Cite record B and the reconciliation beside record A for the seeds rule | finding 3 |
| 6 | Section 6.4, item 2, lines 1152 to 1154 | Add the sampling band to what is printed beside the piece's count | section 1.7 |
| 7 | Section 7.2, item 1, lines 1336 to 1338 | The output file of the controls re-run records torch only. Say the registered code writes all the pinned versions to its output file, and cite the re-run's findings for the three version numbers | finding 8 |
| 8 | Section 7.2, item 1, lines 1339 to 1341 | Drop "in the way `.venv-lock-2026-08-28.txt` does", or say that file is not committed. Name the file the registration will commit, in a place the ignore list does not catch, and include scipy | finding 9 |
| 9 | Section 7.2, item 1, after line 1347 | Add record B's clause: if the processor proves impractical at full size, that is a fresh question for John, not a switch | section 1.4 |
| 10 | Section 7.3, item 2, lines 1831 to 1838 | Per question 1: the code is changed and its code test run once more, labelled as before, before the registration review; then quote that test | finding 4 |
| 11 | Section 7.3, last paragraph, lines 1996 to 2017 | Add record B's two clauses: the method states what "the model's own turn" and its twin pairing mean for the solver; a reading on any seed goes to John before anything else moves. Then write the run's result in | section 1.4 |
| 12 | Section 7.4, lines 2072 to 2076 | Add the fourth reconciled point to the frozen list: the order of the piece rule, with the sentence on what it can miss | section 1.5 |
| 13 | Section 9, line 2256 | Remove the second half of the cell ("cleared it on every seed, at 1.0051, 0.9926 and 0.9974"), or reword it as the entangled model's three readings | finding 1 |
| 14 | Section 9, line 2258 | Cite record B's ruling 2 and add that the registration says what the order can miss | section 1.7 |
| 15 | Section 9, lines 2260, 2276 and 2277 | Cite record B and the reconciliation for "pinned", for the band and for the separation; "the same file" at line 2277 points at record A | finding 3 |
| 16 | Section 10, item R-10, lines 2418 to 2420 | "a separation of 0.9926 under the registered rules" | finding 1 |
| 17 | Section 10, "What happens next", and section 11, step 1, lines 2475 to 2478 | Add the other-agent control's code test to what is owed before step 2, per question 1 | finding 4 |
| 18 | Section 11, step 5a, lines 2502 to 2507 | Add: the count is reported with the sampling band beside it | section 1.4 |
| 19 | Section 11, step 5a, lines 2520 to 2524 | Replace "if that turns out not to be so, the cost goes into the first release's rehearsal line and is said" with record B's rule: a fresh question for John | finding 5 |
| 20 | Section 11, stop condition S4a, lines 2578 to 2583 | Add the sampling band to what is reported to John | section 1.4 |
| 21 | Section 11, line 2541, or section 12.4, line 2763 | One range for the whole successor, or a clause saying why they differ | section 1.10 |
| 22 | Section 13, weakness W12 | Optional: a sentence that the order of the piece rule can cost a reading (the packet said it would go here; record B does not require it) | section 1.7 |
| 23 | Section 15, intro and entry 29, lines 3082 to 3084, 3314 to 3321 | Entry 29 cites record A only and lists the seven as record A has them. Add record B, the reconciliation and the four points | finding 3 |
| 24 | Section 16, line 3342 | "The three rulings of 2026-10-03" becomes the full list | finding 7 |
| 25 | Section 17, lines 3522 to 3525 and 3700 to 3709 | Run the text sweeps again and print the current output | finding 10 |
| 26 | Section 17, line 3814 | "The separation line (the lowest reading of the entangled model minus the highest of the separable model, at least 0.5): produced, at 0.9926" | finding 1 |
| 27 | Section 17, lines 3866 to 3868 | Move "control 2's twenty random pieces" out of the code owed before step 4, per question 1 | finding 4 |
| 28 | Section 19, heading (line 3940) and lines 3943 to 3948 | "each now ruled as suggested" is not true of four. Say that the body follows the reconciliation where the suggestion and the final ruling differ | finding 3 |
| 29 | Section 19, line 4056 | "the three rulings of 2026-10-03 were each given as agreement" becomes the five, with the reconciliation in John's own words | finding 7 |
| 30 | Section 20, lines 4182 to 4195 | Add the three reconciled points it does not carry; correct "the eight new ones" at line 4197 to ten | section 1.5; finding 6 |

Two things outside version 4, noted and not acted on:

- **The reconciliation ruling says** the two records "agree on questions 1, 5
  and 7" and "say the same thing" on everything else. Section 3.3 shows six
  places they do not. A dated note beside that sentence would stop the next
  reader taking the table of four as the whole list. This session did not
  add one: ruling files are not its to edit.
- **`.gitignore`, line 35**, keeps any file named `.venv-lock-*.txt` out of
  the repository. Whoever commits the pin file needs a different name or a
  different place.

---

## 5. What this check did not do

- It did not run the controls re-run or the short pre-stated run again. Both
  were re-run from code by their own checks. This check compared version 4's
  figures with the committed outputs of those runs.
- It did not recompute any figure that version 4 quotes from records older
  than 2026-10-03 other than those in the gate file: the label search's fits,
  the grammar attempt's counts, the rented slice's timings and the
  permutation baseline were not re-derived. Each was checked when it was
  filed, and version 4 carries them from version 3 unchanged.
- It did not check sections that version 4 says are carried from version 3
  word for word against version 3, sentence by sentence. It read them for
  contradiction with the rulings of 2026-10-03 and found one (finding 5).
- It did not judge the design. That is the registration review's job.
- "Yes" in section 1 means the ruling is stated where it bears and stated
  correctly. It does not mean every sentence of the passage was re-derived.

---

## 6. Questions that need John's ruling, each with a suggestion

Listed here and not put to him in this session's chat, as the brief asks.

1. **When is the other-agent control's code changed to twenty random pieces
   and its code test run again: before the registration review (record B),
   or with the registered measurement (record A)?** John agreed to both, and
   the reconciliation did not list the difference. *Suggestion: before the
   registration review, as record B has it.* It is a few minutes on the
   laptop at $0, it satisfies both records, and it means the registration
   review is not looking at a control whose registered code path has never
   run. Confidence: high. The alternative: leave it with the registered
   code, and say in the registration that the path with twenty draws has not
   run.

2. **The separation rule forgives a seed that returns no verdict and does
   not forgive a seed that reads oddly (section 3.1). Is that what John
   meant?** *Suggestion: yes, leave the rule as ruled, and have the
   registration say it in a sentence.* A built model that returns a low
   reading is evidence against the measure in a way that a model returning
   nothing is not, and the rule is the stricter one, which is the safer
   direction for a claim of "metric validated". Confidence: moderate. The
   alternative: the middle reading of each model's three, which tolerates one
   odd seed on each side and is less strict.

Not a question, but for John to know: the six unlisted differences between
the two records (section 3.3). On five of them record B simply says more and
nothing is in conflict; this check treats those as ruled, by the
reconciliation's own sentence that both records stand.

---

## 7. Scripts and outputs beside this file

In `reviews/2026-10-03-proposal-v4-check-scripts/`, each run from the root of
the checkout with the project's own Python (which lives in the main checkout
and was run by its full path from this worktree):

| Script | What it does | Output |
|---|---|---|
| `toy_figures.py` | recomputes 89 toy figures from the committed output files and prints each beside version 4's | `toy_figures.out.txt` |
| `stale_search.sh` | lists every line of version 4 that touches one of the four reconciled points | `stale_search.out.txt` |
| `site_sets_and_arithmetic.py` | runs the site-set rule and compares it with section 18's printed list; redoes the threshold, sampling and money arithmetic | `site_sets_and_arithmetic.out.txt` |
| `ledger_lookup.py` | looks up each dollar figure in the ledger line version 4 names | `ledger_lookup.out.txt` |
| `section17_sweeps.sh` | runs section 17's text sweeps again on the file as it stands | `section17_sweeps.out.txt` |
| (the repository's own) `scripts/check_citations.py`, `scripts/check_single_source.py` | run on version 4 | `check_citations.out.txt`, `check_single_source.out.txt` |
