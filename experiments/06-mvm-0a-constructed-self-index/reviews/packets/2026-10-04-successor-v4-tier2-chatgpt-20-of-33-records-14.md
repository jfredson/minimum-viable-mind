*This is file 20 of 33 of one review packet, pasted into a single conversation. It contains record 14 part 2 of 3 (the check of version 4 by a session that did not write it (holds the wording fixes the registration text must carry)). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 14 of 25, part 2 of 3 - the check of version 4 by a session that did not write it (holds the wording fixes the registration text must carry) - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-claude-code.md` (complete file, 62,740 characters) =====
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

===== END OF RECORD 14, part 2 =====

