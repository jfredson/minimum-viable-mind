# Check: John's ruling packet for Saturday 2026-09-26 (nine decisions, one page each)

*Filed by a Claude Code session in its own worktree
(`.claude/worktrees/weekend-1-packet-check`, branched from `main` at
`45875ee`). Written on 2026-09-24 (Pacific), 18:00 onward. The file name carries
2026-09-25 because that is the path the brief for this check gave; the brief in
`docs/weekend-1-session-prompts.md`, section (a), names a different path
(`…/2026-09-26-weekend-1-queue-check-claude-worktree.md`). The target is
`docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md` on branch
`worktree-weekend-1-queue-packet`, commit `555f215` (draft pull request 34).
This session did not write the packet and has not seen the session that did.
Nothing in the packet, in any registered text, ruling file or protocol text was
edited. Nothing was rented or spent.*

*Every finding is labelled **MEASURED** (a command was run and its output is
reported here) or **ARGUED** (reasoning a reader can dispute).*

---

## The answer first

**Every figure John will rule from traces to the file the packet cites for it,
with the exceptions listed under "What must change" below.** Two of those
exceptions affect a number John would put into the registration text (item 2 in
the list below: a family count of 180 that should be 176) or the file named as
the source of a dollar figure (item 3: the ledger's "$12 planning figure" is
for ten runs, not one). The rest are wrong section or row citations, quotes that
are not quite word for word, and one piece of arithmetic whose basis is misstated.
None of them reverses a recommendation (ARGUED).

**The money, added up independently from the ledger rows (MEASURED, check M-6
below):** spent about **$227.63 of $400**, leaving about **$172.37**; Amendment
A3, the first constructed self-index experiment, about **$46.18 of its $100
stop**, leaving about **$53.82**. The packet says about $227.6, $172.4, $46.2
and $53.8. Those agree.

**Page 8b's claim that John already chose "dated note" on 2026-09-21 is true**,
and the note says so itself. It is pasted in full below (MEASURED).

**Every recommendation carries a confidence level and a strongest argument
against it:** 18 recommendations and 18 "strongest argument against" paragraphs
(MEASURED).

---

## What must change in the packet (the writer's session or a fixer makes these, not this one)

1. **Disagreement 4 and page 1b cite the wrong section of the proposal.**
   MEASURED. The packet says the proposal sets the learn-both bar "against the
   measured accuracy of an ordinary competing solver" in section 8.1. Section 8.1
   (lines 547–552 of `docs/successor-experiment-proposal-2026-09-21.md`) says the
   opposite: the competing solver is among the "Reference points reported
   alongside, and they are references and not thresholds". The threshold wording
   is in the section 9 table (line 594): "Learn-both threshold, per condition |
   R3 | Rehearsal items R-1 and R-5, against the measured competing solver".
   Also, the quote in the packet is not word for word; the words "against" and
   "the measured accuracy" are not next to each other in the source. The
   disagreement is real, but it is *inside the proposal* (section 8.1 against the
   section 9 table), and section 8.1 already says what page 1b recommends, for all
   three reference points and not only "the one in eight and one in four".
   Option (ii) on page 1b ("as section 8.1 of the proposal words it") should say
   section 9.
2. **Page 1e, option (i): the count is 176, not 180.** MEASURED. The 45 site
   sets are 9 layer sets × 5 position sets
   (`experiments/rehearsal-successor-measure/src/rehearse.py`, lines 53–55), and
   one of them is layers (0, 1, 2, 3, 4) at positions "all", which is the
   every-layer, every-position set that the rehearsal (section 7, item 5) says
   "has to be excluded in writing". Removing it leaves 44 site sets, and 44 × 4
   rank caps × 1 label = **176**. The packet writes "45 site sets × 4 rank caps ×
   1 label = 180 comparisons per arm and seed, with the degenerate all-sites set
   excluded". Both cannot be true. The rehearsal's own "180 as computed" was 45 ×
   4 with the all-sites set still inside it. This count sets the size of the
   correction for making many comparisons, so it matters if John rules option (i).
3. **The "$12 planning figure" is cited to a ledger line that does not say
   $12 a run.** MEASURED. The packet (pages 4, 5 and 6) calls $12 "the ledger's
   planning figure at this size" per run, citing the compute ledger's "Phase
   budget guide". That line reads "Registered training, 5 seeds × full+twin |
   ~$2 (10M) / ~$12 (30M) / ~$120 (100M)", which is the price of ten runs, not
   one, and the ledger's own 2026-08-12 reconciliation calls the guide "now
   known-stale: it prices the 5-seed 30M at ~$12, but the measured 30M pilot
   alone cost ~$97" (ledger line 360). The proposal (section 12.4) and the weekend
   roadmap use $12 a run with the same citation, so the packet inherits the
   error; it is not the packet's alone. The dollar effect is small, because
   measured clean runs are about $9.9 to $10.1 and $12 sits just above them
   (ARGUED), but the packet should call $12 the proposal's per-run planning figure,
   not the ledger's, and could list it as a tenth source disagreement.
4. **"About $10.30 across four occurrences" is cited to the wrong ledger row.**
   MEASURED. Page 6's table and page 9 give the 2026-09-21 row. That row (ledger
   line 74) never mentions $10.30. The phrase is in the 2026-09-19 row (line 70)
   and the first 2026-09-20 follow-up row (line 72).
5. **Page 9: "the same figures in the staging document, section 7" is not so.**
   MEASURED. The staging document (`docs/successor-rented-slice-staging-2026-09-21.md`,
   line 179) says the rehearsal line "is up to $10 and of which nothing has been
   spent". It holds no $0.02 or $9.98; it predates the two-cent spend. The ledger
   row is the only source for those figures and is enough.
6. **Page 9: the plan file was regenerated twice, not three times.** MEASURED.
   `git log -- …/out/rented-slice-plan.txt` lists `8bc5fbe` (staged), `c4165b3`
   and `60d1496`. Commit `e95d127` changed the staging *script*
   (`stage_rented_slice.sh`) and not the plan file. The conclusion (a check of
   the plan as it now stands is owed) is unchanged.
7. **Page 3: "still owed" is cited to section 3 of the nomination-label ruling.**
   MEASURED. It is in that file's "What was NOT ruled here" section (line 147).
   Section 3 says the problem "is not closed by this ruling" but not "still owed".
8. **Disagreement 5 cites rehearsal section 8 for "the rehearsal's reading rather
   than a ruling".** MEASURED. That phrase is at line 55, in section 0. Section 8
   (line 714) says "the rehearsal's adjudication and not a ruling". The meaning is
   the same; the citation is off.
9. **Three quotes are not word for word.** MEASURED. (a) Page 5 quotes weakness
   W3 as a network "can still learn to concentrate it in a low-rank direction";
   the proposal (line 1203–1204) says a network "can be built with ownership
   multiplied into every layer and still learn to concentrate it …". (b) Page 1g
   quotes "not ruled out for later"; the ruling (line 119) says "Neither is ruled
   out for later." (c) Page 4 quotes stop condition S1 as "not learnable at tiny
   scale even in principle … Nothing trains"; the ellipsis drops the fact that S1
   also fires on item R-8 ("the transplanting code does not pass its known-answer
   tests"). None of these changes a meaning John relies on (ARGUED), but a packet
   that puts words in quotation marks should match them.
10. **Page 6: "$92 to $108 on the measured ratio" misstates its basis.**
    MEASURED for the arithmetic, ARGUED for the reading. On the spending
    proposal's own $10.20 base, the measured ratios 0.981 and 1.049 give nine runs
    at about $90.6 to $94.8 (the proposal itself gives $91.80 at a ratio of 1.0).
    $108 is nine runs at $12, a different basis (and see item 3). The sentence
    should say "about $91 to $95 on the measured ratio, or $108 at $12 a run".
11. **The commit message says the two scripts' outputs are in Appendix A; they
    are not, and its count is off by one.** MEASURED. `grep -c
    'check_citations\|check_single_source'` on the packet returns 0. The commit
    message says "5 dollar figures not in the ledger"; the script reports 6 at the
    packet's own commit ($130 three times, $450 twice, $175 once). The outputs are
    pasted below; the packet should carry them.
12. **Two small staleness points.** MEASURED. The packet's preamble (lines 22–27)
    says `docs/weekend-1-session-prompts.md` is uncommitted; it reached `main` in
    `b5cfc23` after the packet's base (`97ee3c9`). Appendix B counts "six open
    `awaiting-john` tasks"; TimeAssembler lists six to-do and one in progress
    (the A3 closure task), seven not done.

---

## What was opened, and what was not

**Opened and read against the packet:** `CLAUDE.md`; the top entry of
`STATUS.md`; `docs/outside-review-protocol.md` (the pairing rule, isolation,
Filing); `docs/known-failure-modes.md` (opening and headings); the packet in full;
`docs/weekend-1-session-prompts.md` section (a); the sections the packet cites in
`docs/2026-09-21-successor-measure-rehearsal.md` (sections 0, 2a, 3, 4, 5, 7, 8,
9, 10, 11, 12), `docs/successor-experiment-proposal-2026-09-21.md` (sections 3,
6.3, 6.4, 7.2, 8.1, 8.2, 9, 12.4, 13, decision 5), both rulings of 2026-09-23,
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md` (section 4,
items 5, 10–16, 20, the 2026-09-22 correction note), `docs/rulings/2026-09-20-december-result-roadmap.md`
(item 4, the standing rule, the 2026-09-21 annotation), the Gate C review at RT-172,
RT-176 and RT-179, `docs/preauthorised-spending-proposal-2026-09-21.md` (sections
0, 1.1, 3.2, 3.5, 5.3, 7 and the second afterwards note), `docs/weekend-roadmap-2026-09-24.md`
(sections 1–4), the compute ledger in full (every row, the reconciliation notes,
the phase budget guide), `red-team-a4.md` at F17 and its notes,
`pre-registration.md` lines 205–312, `cue_detector_gate.json`, the three A3
endpoint records under `a3-gates/`, the citation triage and pointer-fix check
reviews of 2026-09-21 at the cue-detector item, the staging document (sections
4, 6, 7, 8), `docs/rulings/2026-09-22-launcher-argument-guard.md` section 4,
`spec/corrigibility-commitments.md` at C2, the rehearsal code at its site, label and
nomination lines, the derived launcher at its sleep guard, the plan file,
`argument-guard-method.md` (searched), the two sleep-guard checks of 2026-09-24
(searched), the TimeAssembler note "Wittgenstein criteria for the Stage 2 metric"
(document `d08c23ae-7dca-4e55-9ac3-bb785ebed652`, read through the TimeAssembler
tool), and the `awaiting-john` task list on the Minimum Viable Mind project.

**Not opened:** the rehearsal's output files under
`experiments/rehearsal-successor-measure/out/` other than the plan file (every
rehearsal figure was checked against the findings file, not against the outputs
it was computed from); the method file and its addendum; the red-team ledger; the
A3 tier 2 packet files beyond the index lines the packet quotes; the bodies of the
TimeAssembler tasks (so the packet's quote from the registered-text task's body,
"what is NOT yet known … whether the value is wrong, or merely uncited", was
**not checked**); `data/project.toml`. No rehearsal stage was run.

---

## How the checks were run

Most checks used one small search tool kept outside the repository
(`$CLAUDE_JOB_DIR/tmp/findq.py`): for each quote or figure the packet gives, it
looks for it in the file the packet cites, ignoring line wraps, bold marks and
backticks, and prints the line and the heading it sits under, so a figure cited
to the wrong section shows up. It does not strip the `>` that starts a
blockquote line, so quotes from blockquotes were checked by reading the lines,
shown below. The checklists were written from the packet, one line per claim:
53 lines for page 1, 30 for page 2, 7 for page 3, 32 for pages 4 and 5, 35 for
page 6, and 40 for pages 7 to 9. Output is given below for each page, cut to the
lines that carry the result; every line not shown was FOUND in the cited file and
section.

The copy of the packet checked is byte-identical to the one on the branch:

```
$ shasum docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md …/weekend-1-queue-packet/docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md
98ded3f22371ed323646edb76663fd3587d24c43  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md
98ded3f22371ed323646edb76663fd3587d24c43  …/weekend-1-queue-packet/docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md
$ git merge-base main worktree-weekend-1-queue-packet
97ee3c9a6d079db04f10ee37e80b20ac068f24dd
$ git diff --stat 97ee3c9 main
 data/roadmap.toml                 | 380 ++++
 docs/site-roadmap-page-prompt.md  |  88 ++
 docs/weekend-1-session-prompts.md | 397 ++++
```

No file the packet cites changed between its base and `main` today, so the
checks below hold for the text John will rule from. (MEASURED)

---

## The two scripts, run on the packet (from this worktree, on `main` at `45875ee`)

```
$ .venv/bin/python scripts/check_citations.py --only docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md
PART (a): does every file a document names exist?
[CONFIDENT] 1 reference(s) name a file that is not in the repository
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:47
      names: docs/rulings/2026-09-26-weekend-1-queue.md
[LOOK AT IT] 0 bare name(s) match more than one file
[LOOK AT IT] 1 name(s) of run-output files that are not in the repository
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:1216  bench_arms.json
[LOOK AT IT] 2 reference(s) written with a gap or a wildcard that matched nothing
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:35  experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-<model>.md
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:1002  experiments/<experiment>/reviews/YYYY-MM-DD-<target>-<reviewer>.md
[NOT CHECKED] 1 reference(s) to files outside this repository
     1x  ~/Documents/Code/CLAUDE.md
PART (b): is a figure given with a citation actually in the file cited?
[CONFIDENT] 0 exact figure(s) absent from the one file their sentence cites
[LOOK AT IT] 2 figure(s) worth a human eye
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:632
      figure: $10.04    cited: experiments/06-mvm-0a-constructed-self-index/compute-ledger.md    (only an approximate match found)
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:831
      figure: $92    cited: docs/2026-09-21-successor-measure-rehearsal.md, docs/preauthorised-spending-proposal-2026-09-21.md    (only an approximate match found)
Confident findings: 1. Things for a human to look at: 5.
exit 1
```

Reading: the one confident finding is the rulings file to be written on Saturday,
missing by design. `$10.04` is arithmetic on the 2026-09-17 row ($20.08 ÷ 2) and
is labelled so on the page. `$92` is item 10 above. At the packet's own branch the
same script also reports `docs/weekend-1-session-prompts.md` as missing; on `main`
it now exists. (MEASURED)

```
$ .venv/bin/python scripts/check_single_source.py --only docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md
Figures that are in the ledger and point at it: 8
Set aside as forecasts (a proposal pricing something, not a record of spend): 92
Set aside as neither, by the wording around them: 51
[CONFIDENT] Group 1: a dollar figure the ledger does not contain
6 found.
  …PROPOSAL.md:72   $130   names instead: docs/rulings/2026-09-20-december-result-roadmap.md
  …PROPOSAL.md:108  $130
  …PROPOSAL.md:824  $450
  …PROPOSAL.md:824  $175
  …PROPOSAL.md:831  $450   names instead: docs/weekend-roadmap-2026-09-24.md
  …PROPOSAL.md:933  $130
[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source
0 found.
[LOOK AT IT] Group 3: in the ledger, and no source named
12 found.
  …:709 $13.92, $3.8, $10.1, $13.92   …:754 $32, $44   …:781 $400
  …:785 $0.02, $9.98   …:819 $44, $131   …:824 $142
[LOOK AT IT] The same figure in many documents
0 figure(s) appear in four or more documents.
Confident findings: 6. Things for a human to look at: 12 unsourced figures and 0 widely repeated ones.
exit 1
```

Reading: all six group 1 figures are caps or proposed caps and envelopes, not
spend, and each has a non-ledger source by design. The group 3 figures sit in
table rows whose column names the ledger row, which the script reads one sentence
at a time and cannot see. Re-run at the packet's own branch
(`.claude/worktrees/weekend-1-queue-packet`), group 1 is the same **6**; the
packet's commit message says 5 (item 11 above). (MEASURED)

---

## Page by page

### Page 1 — the eight numbers. MEASURED.

```
$ python3 findq.py p1.txt        # 53 claims, pages 1a to 1h
1a.1  FOUND line 833 under ## 11. …   [separation of 0.873 to 0.885 against 0.0000, across-seed spread 0.019 …]
1a.3  FOUND line 379 under ## 4. The reading, on fresh episodes   [0.9818]
1a.7  FOUND line 210 under ## What follows for the registration text   [is being set between one arm whose reading is exact …]
1a.8  FOUND line 138 under ### RT-172 …   [in units whose ceiling moves between the place it is set …]
1b.3  FOUND line 629 under ## 8. …   [On 3,000 held-out episodes that bar is 0.2630]
1b.4  MISSING docs/successor-experiment-proposal-2026-09-21.md   [against the measured accuracy of an ordinary competing solver]
1c.1  FOUND line 835 under ## 11. …   [the entangled arm runs 0.0517 at the first layer, 0.3467 …]
1c.5  FOUND line 598 under ## 7. …   [0.7612, 0.6512 and 0.6512]
1d.1  FOUND line 322 under ## 3. …   [0.153 at rank 1, 0.355 at rank 2, 0.832 at rank 4 and 1.000 at rank 8]
1d.2–1d.9  FOUND lines 323–324 under ## 3.   [0.1517 … 0.8717, each per-seed figure]
1e.1  FOUND line 837 under ## 11. …   [45 site sets × 3 labels × 6 rank caps = 810 comparisons …]
1e.3  FOUND line 788 under ## 10. …   [448 wide, 12 layers]
1f.1  FOUND line 838 under ## 11. …   [three seeds gave an across-seed spread of 0.019 and 0.023 …]
1f.3  FOUND line 137 under ## 3. The sharp corollary …   [leaves out a source of variation as large as …]
1f.4  FOUND line 176 under ## 5. The arm this does not touch   [0.51]
1f.5  MISSING …proposal…   [three arms × three seeds]
1f.6  MISSING …range-and-direction-only.md   [scientifically standard]
1g.1  FOUND line 839 under ## 11. …   [across-seed spread 0.0189 and 0.0227; … 0.0198 and 0.0203 …]
1g.2–1g.4  FOUND lines 75–76 under ## The measurement the ruling rests on   [0.0156, 0.0102, one of them half what it was]
1g.5  MISSING …range-and-direction-only.md   [not ruled out for later]
1h.1  FOUND line 840 under ## 11. …   [the separable arm drops to 0.2467 to 0.2733 …]
1h.4  FOUND line 624 under ## 8.   [0.1717 / 0.1807 / 0.1860]
1h.5  FOUND line 625 under ## 8.   [0.1813 / 0.1947 / 0.1857]
1h.6  FOUND line 571 under ### 8.2 …   [removes a sense organ, not a structure the network built]
1h.7  MISSING …proposal…   [own-directed collapses, named-other holds]
```

The misses, opened by hand:

```
$ grep -n 'competing solver\|competitor' docs/successor-experiment-proposal-2026-09-21.md
551:  **measured** accuracy of an ordinary competing solver built at the rehearsal
594:| Learn-both threshold, per condition | R3 | Rehearsal items R-1 and R-5, against the measured competing solver |
$ sed -n 547,552p docs/successor-experiment-proposal-2026-09-21.md
- Reference points reported alongside, and they are references and not
  thresholds: one in eight for guessing, one in four for a solver that cannot
  tell whose value it needs, and — the addition this proposal makes — the
  **measured** accuracy of an ordinary competing solver built at the rehearsal
  (rehearsal item R-5), so the bar is set against something that was actually
  built rather than against arithmetic. The closed design's comparison battery
$ grep -n '0\.0506\|standard\|for later' docs/rulings/2026-09-23-range-and-direction-only.md
42:> 0.0506, against an uncertainty method that reports 0.019. What may the
54:| entangled, seed 2 | 0.8801 | 0.8295 | **0.0506** |
109:> then quote a mean with that spread. Scientifically standard and gives a real
119:Neither is ruled out for later. What is ruled is that the registration does not
$ grep -n 'three seeds\|× three' docs/successor-experiment-proposal-2026-09-21.md
1051:| The remaining eight registered runs | Three arms × three seeds, less the one free-arm run … (section 12.4)
$ grep -n 'collapses' docs/2026-09-21-successor-measure-rehearsal.md
726:proposal's section 8.2 pre-states the shape "own-directed collapses,
$ sed -n 53,55p experiments/rehearsal-successor-measure/src/rehearse.py
CANDIDATE_LAYER_SETS = [(0,), (1,), (2,), (3,), (4,),
                        (3, 4), (2, 3, 4), (1, 2, 3, 4), (0, 1, 2, 3, 4)]
CANDIDATE_POSITIONS = ["action", "action+ans", "action+3", "post-identity", "all"]
$ sed -n 603,607p docs/2026-09-21-successor-measure-rehearsal.md
5. **The degenerate site set is real and has to be excluded in writing.**
   Transplanting every layer at every position is not an intervention: it is
   the donor's own forward pass, proved as a tensor identity in the
   transplanting code's self-test. On the separable arm the whole-state
   accuracy is 1.0000 at *every one* of the forty-five site sets, so the
```

Reading: "three arms × three seeds" and "scientifically standard" are there with a
capital letter; "own-directed collapses, named-other holds" is the rehearsal
quoting the proposal, as the packet presents it; 0.0506 is in the table the packet
names. What does not hold is 1b.4 (item 1 above), 1g.5 (item 9b) and the 1e count
(item 2). Arithmetic on the page, checked by hand: 0.8 × 0.556 = 0.445, which the
first two layers (0.0517, 0.3467) fall below and the third (0.556) clears, as page 1c
says; 0.5 ÷ 0.0506 ≈ 9.9, "ten times" as page 1a says; the named-other readings
0.2637 (entangled seed 2) and 0.2680 (free seed 1) are the only ones above 0.2630,
"one seed each". (MEASURED)

### Page 2 — which form of the reading. MEASURED.

```
$ python3 findq.py p2.txt        # 30 claims
2.1  FOUND line 407 under ### 6.3 The number   [(accuracy_whole − accuracy_ownership_only) / accuracy_whole]
2.2  FOUND line 149 under ### RT-172 …   [accuracy_whole − accuracy_untouched]
2.6  FOUND line 413 under ### The reading divides by an uncorrected accuracy — confirmed   [strong transplant … 0.9008 … 0.4323 (spread 0.0119) … 0.5018 (spread 0.0132)]
2.7  FOUND line 414 (same)   [weak transplant … 0.3497 … 0.3222 (spread 0.0181) … 0.5013 (spread 0.0230)]
2.8  FOUND line 416 (same)   [… by 0.110 — six times its own spread.]
2.9  MISSING   [five of nine]
2.10–2.13  FOUND lines 432–451 (same)   [0.0680, 0.0710, D-2, recorded here as a fail]
2.18–2.24  FOUND lines 381–384 under ## 4.   [0.9949, 0.8863, 0.8366, 0.8499, 0.9880, 0.9267, 0.9821]
2.25–2.27  FOUND lines 506–512 under ### A control's first cell is empty by construction   [0.0175, about a third of the value being predicted, needs room for a miss of that size]
2.28 FOUND line 435 under ### 6.4 …   [No normalisation by an ownership-blind ceiling anywhere]
$ sed -n 376,384p docs/2026-09-21-successor-measure-rehearsal.md      (the section 4 table, cut to the two reading columns)
| entangled, seed 0 | 0.0600 | 0.5400 | 0.0688 | **0.8727** | 0.9818 |
| entangled, seed 1 | 0.0663 | 0.5750 | 0.0663 | **0.8848** | 1.0000 |
| entangled, seed 2 | 0.0638 | 0.5525 | 0.0663 | **0.8801** | 0.9949 |
| free, seed 0 | 0.0600 | 0.5825 | 0.0663 | **0.8863** | 0.9880 |
| free, seed 1 | 0.0550 | 0.5663 | 0.0925 | **0.8366** | 0.9267 |
| free, seed 2 | 0.0762 | 0.5663 | 0.0850 | **0.8499** | 0.9821 |
$ grep -n 'Five of the nine' docs/2026-09-21-successor-measure-rehearsal.md
441:**Five of the nine, not six.** Three are dead heats, and they are dead heats
```

Reading: every figure on page 2 is in section 4 or 5 of the rehearsal, arm by arm
as the packet assigns them. The no-transplant column (0.055 to 0.076) supports page
1c's "about 0.06". The 0.0175 miss is section 5's second finding, as cited. The
Gate C review's closures (a), (b) and (c) under RT-172 are at its lines 148–154,
and the proposal's decision 5 (line 1324) names and declines the raw difference.

### Page 3 — nomination as three instruments. MEASURED.

```
$ python3 findq.py p3.txt
3.1  FOUND line 92 under ## 3. What this does not settle …   [Across the nine arm-and-seed pairs … three instruments, not one.]
3.2  FOUND line 339 under ## 3. The finding that matters most …   [… 0.0683, 0.0650 and 0.0633 … 0.0700, 0.0683 and 0.0667 …]
3.4  FOUND line 469 under ### 7.2 …   [the ones with the highest development-set ownership-only transplant accuracy]
3.6  FOUND line 147 under ## What was NOT ruled here   [still owed]
$ grep -n READ_LABELS experiments/rehearsal-successor-measure/src/rehearse.py
69:READ_LABELS = ("agent-slot", "marker-rank", "marker-word")
79:               * len(RANK_CAPS) * len(READ_LABELS))
212:    for label in READ_LABELS:
284:                    for label in READ_LABELS:
520:                    for label in READ_LABELS:
$ sed -n 297,298p experiments/rehearsal-successor-measure/src/rehearse.py
            # nominated by causal effect, not by how well the read fits
            best = max(grid, key=lambda g: g["accuracy_ownership_only"])
$ sed -n 465,466p docs/successor-experiment-proposal-2026-09-21.md; sed -n 479,480p …
2. **Candidate directions.** At each site, fit a straight-line read for "which
   agent is acting" and take the leading directions, up to a rank cap the
5. **Arm T's known ownership slot is not handed to the procedure.** The
   nomination runs blind on every arm, so what is validated is the whole
```

Reading: the code does what page 3 says: the search ranges over all three labels
and picks the best by causal effect, labels included. The proposal quotes are there
(3.3 and 3.5 missed only on quote-mark style and a line break). "Still owed" is item
7 above.

### Page 4 — the named-other condition. MEASURED.

```
$ python3 findq.py p45.txt       # pages 4 and 5, 32 claims
4.1  FOUND line 623 under ## 8. …   [separable, 0 / 1 / 2 | 1.0000 … | 0.2467 / 0.2510 / 0.2733]
4.2  FOUND line 624 (same)   [entangled … 0.5817 / 0.5660 / 0.5767 | 0.2590 / 0.2370 / 0.2637 | 0.1717 / 0.1807 / 0.1860]
4.3  FOUND line 625 (same)   [free … 0.5633 / 0.5563 / 0.5890 | 0.2547 / 0.2680 / 0.2393 | 0.1813 / 0.1947 / 0.1857]
4.4  FOUND line 630   [The entangled and free arms clear it on one seed each.]
4.5  FOUND line 645   [The named-other condition moved from 0.2547 to 0.2657]
4.8  FOUND line 689 under ### Does the proposal's first stop condition fire? …   [reaches 1.0000 on the named-other condition (and 0.2380 …)]
4.10 FOUND line 182 under ## 3. What counts as a result   [the most likely reason is the named-other half]
4.12 FOUND line 714   [This is the rehearsal's adjudication and not a ruling, and it is John's to overturn]
4.13 FOUND line 717   [about $10 spent]
4.14 FOUND line 186 under ## 3. …   [four times the per-row weight and two thirds of the query gradient, reached 0.3125 and changed nothing]
4.15 FOUND line 15 of control-learnability-pilot-findings.md   [0.3125]
4.16 FOUND line 69 (the 2026-09-17 ledger row)   [20.28 pod-hours at $0.99 = $20.08]
4.9  MISSING   [That does not settle what happens at the registered size — …]
4.11 MISSING   [not learnable at tiny scale even in principle … Nothing trains]
$ sed -n 656,658p docs/2026-09-21-successor-measure-rehearsal.md
1.0000 at the same size on the same grammar.) That does not settle what happens
at the registered size — the ten-million rung failed to learn the earlier
design's task and the thirty-million rung did not — but it does mean the risk
$ sed -n 668,670p docs/2026-09-21-successor-measure-rehearsal.md
> **S1.** The rehearsal fails item R-1 (the grammar is not learnable at tiny
> scale even in principle) or item R-8 (the transplanting code does not pass
> its known-answer tests). Nothing trains. About $10 spent.
```

Reading: all page 4 figures hold. 4.9 and 4.11 are there (the tool missed a
blockquote and a line break); the S1 elision is item 9c. $20.08 ÷ 2 = $10.04, as the
page says. The "$12" planning figure on this page is item 3.

### Page 5 — the middle of the scale. MEASURED.

```
5.2  FOUND line 576 under ## 7. …   [What would separate the two readings is a fourth arm … cannot be told from a ceiling.]
5.3  FOUND line 70 (2026-09-19 ledger row)   [10.0h ≈ $9.9]
5.4  FOUND line 70   [ZERO idle billing]
5.5  FOUND line 67 (2026-09-15 row)   [$13.92]
5.6  FOUND line 67   [$3.8 of the total is AVOIDABLE IDLE]
5.7  FOUND line 344   [A1 10M row trues up to $1.943]
5.8  FOUND line 171 of the weekend roadmap   [about $36]
5.10 FOUND line 1188 under ## 13. …   [where arm F sits between two constructed anchors on this measure]
5.11 FOUND line 1182   [differ in more than their degree]
5.1  MISSING (quote-mark style only; lines 390–393 read by hand, match)
5.9  MISSING   [can still learn to concentrate it in a low-rank direction]
$ sed -n 1203,1204p docs/successor-experiment-proposal-2026-09-21.md
cannot be built": a network can be built with ownership multiplied into every
layer and still learn to concentrate it in a low-rank direction, in which case
```

Arithmetic checked by hand (MEASURED): 3 × $9.9 = $29.70; 3 × $10.04 = $30.12;
3 × $12 = $36; 3 × $13.92 = $41.76; plus $1.94 gives $31.64 to $43.70, "call it $32
to $44" holds. $13.92 − $3.8 = $10.12, "about $10.1 clean" holds. The free arm's
corrected readings (0.9880, 0.9267, 0.9821) and the entangled arm's (0.9818 to
1.0000) give "0.93 to 1.00" as stated. The W3 quote is item 9a.

### Page 6 — spend. MEASURED. The ledger read and added independently.

Every spend row of `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`
(lines 59–74) was read, with the 2026-08-12 reconciliation that trues up the
first and third rows. The figure used for each row was grepped from the ledger:

```
$ grep -o 'Row 1 trues up to \*\*\$6.645\*\*' $L          → Row 1 trues up to **$6.645**
$ grep -o 'A1 10M row trues up to \*\*\$1.943\*\*' $L     → A1 10M row trues up to **$1.943**
$ grep -o '\*\*~\$18.9\*\*' $L                             → **~$18.9**
$ grep -o '\*\*~\$25.29\*\*' $L                            → **~$25.29**
$ grep -o '\*\*~\$31.63\*\*' $L                            → **~$31.63**
$ grep -o '\*\*\$13.92\*\* (balance' $L                    → **$13.92** (balance
$ grep -o '\*\*\$0.29\*\* (balance' $L                     → **$0.29** (balance
$ grep -o '20.28 pod-hours at \$0.99 = \$20.08' $L         → 20.28 pod-hours at $0.99 = $20.08
$ grep -o 'about \*\*10.0h ≈ \$9.9\*\*' $L                 → about **10.0h ≈ $9.9**
$ grep -o '\*\*\$0.067\*\* (balance' $L                    → **$0.067** (balance
$ grep -o 'a measured \$1.904 combined' $L                 → a measured $1.904 combined
$ grep -o '\*\*about \$0.02\*\*' $L                        → **about $0.02**
(the 2026-08-09/10 row's actual column reads **$97.04**)

08-07/08 10M pilot, trued up        6.645  running    6.645
08-09/10 30M A1 pilot              97.040  running  103.685
08-09 A1 10M, trued up              1.943  running  105.628
08-15 30M re-run                   18.900  running  124.528
08-16 A2 wave 1                    25.290  running  149.818
08-17 A2 wave 2                    31.630  running  181.448
09-14 Gate 0                        0.000  running  181.448
09-15 Gate 1                        0.000  running  181.448
09-15 Gate 2 pilot                 13.920  running  195.368
09-16 ops test                      0.290  running  195.658
09-17 seeds 1+2                    20.080  running  215.738
09-19 control pilot                 9.900  running  225.638
09-20 recovery                      0.067  running  225.705
09-20 follow-ups 1+2                1.904  running  227.609
09-21 rented slice                  0.020  running  227.629
spent 227.63 left of 400 172.37
A3 cumulative 46.181 left of 100 53.82
with row 1 as first entered (6.02): 227.0
```

**Independent figures: spent about $227.63 of $400, about $172.37 left; A3 about
$46.18 of $100, about $53.82 left.** The ledger's own running total at each step
agrees ($105.62, ~$124.5, ~$149.8, ~$181.4, ~$195.3, ~$195.6, ~$215.7, ~$225.7,
~$227.6). A reader who adds the first row as entered ($6.02) instead of trued up
($6.645) gets $227.0; the ledger's chain uses $6.645, and so does this check. Storage
charges are not in the running total, by the ledger's own rule of reconciliation
(its "Reconciliation baseline"). The packet's figures agree. (MEASURED)

The rest of page 6:

```
$ python3 findq.py p6.txt        # 35 claims, all FOUND
6.1  line 30 of the 2026-09-20 ruling, under ## The seven items   [Successor spend cap: $130, within the MVM-0a $400 envelope]
6.2  line 52 under ## Standing rule on spend   [a gate for John's ruling]
6.8  line 396 under ## Correction added 2026-09-22 …   [about $2.60 past it]
6.9  line 401 (same)   [about $44 and about $131 still sum to about $175]
6.12 line 1055 under ### 12.4 …   [$143]
6.13 line 511 of the Gate C review   [one sentence … saying whether item 4's $130 cap is superseded …]
6.17 line 170 of the weekend roadmap, Weekend 1   [$450]
6.18 line 322 under ## 4.   [about $490]
6.27 line 246 under ### 3.2 of the spending proposal   [$125.46]
6.30 line 594 under ### 5.3 The check, specified   [1.25]
6.31 line 601 (same)   [roughly halves the chance of a false trip … about $63 across nine runs]
6.32 line 72 under ## 4. Spending (ruling of 2026-09-21)   [doubles as the billing-anomaly check]
$ grep -n 'Registered training' $L ; grep -n 'known-stale' $L
388:| Registered training, 5 seeds × full+twin | ~$2 (10M) / ~$12 (30M) / ~$120 (100M) |
360:the phase-budget guide below is now known-stale:** it prices the
$ awk 'NR==74' $L | grep -c '10\.3'      → 0
$ grep -n 'about \$10.30 across four' $L | cut -c1-12
70:| 2026-09
72:| 2026-09
```

Arithmetic (MEASURED): $175 + $227.6 = $402.6; $450 − $402.6 − $44 = $3.4 and
$450 − $402.6 − $32 = $15.4, "between $3 and $15 left" holds; $142 − $130 = $12;
$225 − $14 = $211. The $92–$108 range is item 10; the $12 citation item 3; the
$10.30 row item 4.

### Page 7 — the Wittgenstein criteria. MEASURED.

The TimeAssembler note was read through the TimeAssembler tool
(`get_project_document d08c23ae-7dca-4e55-9ac3-bb785ebed652`, "Updated:
2026-09-23"). Every quote on page 7 is in it word for word: "Nothing here is ruled or
registered"; test 1's "an internal variable belongs to the game only if intervening
on it changes what the model does … Proposal: state this as the philosophical
rationale for the successor's causal-interchange design in the spec"; test 2's
"corrupt the ownership input mid-episode … Strongest candidate for inclusion in the
2026 successor"; test 3's "Could be deferred to resumption (post-May 2027) if it
threatens the October schedule"; question 1's "the successor's $130 cap and the
2026-10-11 registration target"; and the framing caution. In the repository:

```
7.1  FOUND line 166 of the weekend roadmap, Weekend 1   [wait for resumption unless they change the metric spec]
7.3  FOUND line 139 of the proposal   [## 2. The question, and what this experiment is for]
$ grep -n 'never exercised' docs/rulings/2026-09-21-review-verification-and-staged-spending.md
39:5. **A pre-stated quantity the rehearsal never exercised is a fatal finding on its
$ sed -n 95,96p docs/rulings/2026-09-20-december-result-roadmap.md
registration commit target of 2026-10-11 in item 1 was pacing, so it goes with
the calendar; the kill dates in items 1 and 7 are commitments and are unchanged.
```

### Page 8a — the key count in the A4 review. MEASURED.

```
$ grep -n '110 keys' experiments/06-mvm-0a-constructed-self-index/red-team-a4.md
640:records for seeds 0 to 2 carry no such field among their 110 keys. So
$ sed -n 82,83p experiments/06-mvm-0a-constructed-self-index/red-team-a4.md
> Added 2026-09-21 by a later session, not by the reviewer. It supplies a
> pointer and changes no finding; every word of the pass stands as filed.
$ sed -n 204,213p docs/rulings/2026-09-21-review-verification-and-staged-spending.md   (item 20)
20. **The key count that does not reproduce gets an owner.** The seventeenth
    … labelled MEASURED and says the endpoint records for seeds 0 to 2 carry no
    such field "among their 110 keys". That count does not reproduce in any
    committed version … each hold **15** top-level keys, and the
    earlier pilot record (`a3-gates/pilot_endpoint.json`) holds 7. The number 110
    is not any of them. The finding's substance — that the gates were never applied —
$ cd experiments/06-mvm-0a-constructed-self-index/a3-gates && python3 -c "import json; …len(json.load(open(f)))…"
endpoint_a3_30m_seed1.json 15
endpoint_a3_30m_seed2.json 15
pilot_endpoint.json 7
$ grep -n 'verbatim, never edited after filing' docs/outside-review-protocol.md
483:  verbatim, never edited after filing. Tier 1 findings continue the ledger's
```

The counts 15, 15 and 7 reproduce. The 110 is not in any of the three records.

### Page 8b — the note in registered text, and whether John already chose. MEASURED.

The registered sentence, line 208 of
`experiments/06-mvm-0a-constructed-self-index/pre-registration.md`, reads
"certified (AUC 0.5008 [0.477, 0.524]), with the frozen batteries' chance floors
(`batteries/batteries_meta.json`: …)". The record:

```
$ python3 -c "import json; d=json.load(open('…/cue_detector_gate.json')); …"
"run": "(i) curriculum text", "n_episodes": 4000, "seed": 20260804,
"clean": {"auc": 0.5008, "ci95": [0.4773, 0.5242]},
"positive_control": {"auc": 0.8627, …}, "GATE": "PASS"
$ grep -n 'The number is not wrong' …/reviews/2026-09-21-citation-and-money-check-triage-claude-worktree.md
(FOUND line 226, under "### D1. The cue-detector figure in the registered pre-registration")
$ git log --oneline -3 -- experiments/06-mvm-0a-constructed-self-index/pre-registration.md
57eb09d Pre-registration note: give the question John was shown and the option he picked, word for word
eeedb2f Pre-registration note: give the battery keys as the registration writes them, and state the permission in the house form
285903e Pre-registration: dated note naming the record that holds the cue-detector figure
```

**The note, as it stands on `main` (`sed -n 256,312p` of
`pre-registration.md`), pasted:**

> **The registered value is unchanged and is correct.** Nothing here corrects
> anything. What was missing was only the file name, which the closure rule in
> `docs/outside-review-protocol.md` asks for: every sentence in registered text
> that says verified, measured, calibrated or attacked cites the committed
> record by file name, and "certified" is a word of that family.
>
> **The authority for this note, and what that authority does not cover.** On
> 2026-09-21, in the session that ordered this note, John did not say or write a
> sentence that could be quoted. He was shown a question with three options under
> it, each option carrying the consequence of choosing it, and he selected one.
> The wording of the question and of all three options was that session's, not
> his; what is his is the selection. The house form for recording a ruling in
> this programme quotes the words John used — as at item 22 of the ruling on
> review verification and staged spending
> (`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, on the
> main line). This decision cannot take that form, because there were no words of
> his to quote. What stands in their place is the question he was shown and the
> option he picked out of it, and both are given here in full. The question, word
> for word as it was put to him:
>
> > Registered text states a measured value without naming the record that holds
> > it. The value is right and the record is committed — only the pointer is
> > missing. How should it be fixed?
>
> The option he selected, word for word, its short label and the description
> under it:
>
> > **Dated note on the registered text** — Add the missing pointer as a dated
> > annotation. Claim unchanged, nothing rewritten. Risk: 'annotation that
> > changes no claim' becomes a judgement each writer makes about their own text
> > — the shape of every drift this program has recorded.
>
> The risk in that last sentence is kept here unedited, and not paraphrased,
> because it was on the page in front of him: he took this option having been
> shown the case against it, which makes the choice a better informed one than a
> bare yes, and a reader should be able to see exactly what he was shown.
>
> What he turned down is part of what he decided, so the two options he did not
> take are set down here as well, also word for word:
>
> > **Registered amendment** — Treat any change to registered text as an
> > amendment, even one adding a pointer. Strictest, keeps registered text
> > genuinely fixed. Cost: amendments become cheap and routine, which is the one
> > thing they must not be.
>
> > **Leave it, record the defect** — Change nothing in the registered text. File
> > the defect with the correct pointer so any reader can find the record.
> > Registered text stays exactly as registered.
>
> **What he authorised is the act — a dated note naming a committed record, where
> no registered claim changes. It does not authorise restating a registered label
> in other words, describing registered content, or annotating registered text
> for any other purpose, and it does not settle any particular wording.** Not one
> word of this note is John's drafting; the wording is this session's, and his to
> overturn. One limit on the record of the ruling itself, stated plainly because
> it weakens it: the ruling is not yet carried in any filed ruling under
> `docs/rulings/`, and what is filed there is about annotating rulings, not
> registered text. Until it is filed, this paragraph is the whole record of it.

Reading: the packet's page 8b is accurate. The choice was a selection from options
a session wrote, not a sentence of John's, and the note itself says so, which is
what the packet's strongest argument against says. (MEASURED)

### Page 9 — the rented slice. MEASURED.

```
9.1  FOUND line 82 of the staging document under ## 4. Which launcher …   [is neither used nor edited]
9.2  FOUND line 174 under ## 7. What it costs   [$0.75]
9.3  FOUND line 175 (same)   [$2.00]
9.4  FOUND line 79 of the launcher-guard ruling, under ## 4.   [My go does not carry over, and I am not issuing a fresh one yet. …]
9.5  FOUND line 88 (same)   [an authorisation naming a document by date lapses when that document changes]
9.6  FOUND line 84 (same)   [What is owed before a fresh go: the amended plan, checked by a session other than the one that amended it]
9.7  FOUND line 56 of spec/corrigibility-commitments.md under ## Commitments   [in the live session, in his own words, naming the specific run(s)]
9.8  FOUND line 75 of STATUS.md   [what is owed first is the amended plan, …]
9.10 FOUND line 262 of the Gate C review under ### RT-179   [three architectures John has not ruled on, …]
9.11 FOUND line 188 of the staging document under ## 8.   [measures the handshake once]
9.13 MISSING staging document   [$9.98]
$ grep -n 'rehearsal line' docs/successor-rented-slice-staging-2026-09-21.md
179:rehearsal line is up to $10 and of which nothing has been spent: everything
$ git log --oneline -- experiments/rehearsal-successor-measure/out/rented-slice-plan.txt
60d1496 Regenerate the plan file on main, with step 0 withdrawn
c4165b3 Regenerate the staged plan file against the real checkout paths
8bc5fbe Stage the one short slice of rented time, for two answers and one rent, and do not run it
$ git show --stat --format='%h %s' e95d127
e95d127 The argument guard, and the check that asserts the standing prohibition
 .../src/check_launcher_argument_guard.sh | 160 +++
 .../src/launch_a3_fetch_first.sh         |  17 +
 .../src/launch_ctl_pilot.sh              |  17 +
 .../src/launch_pilot_a1.sh               |  17 +
 .../src/stage_rented_slice.sh            |  30 +-
$ sed -n 22,24p experiments/rehearsal-successor-measure/out/rented-slice-plan.txt
    DRYRUN=1 SCALE=10M MAXTOK=2000000 OUT=slice_handshake \
      GRACE_S=600 \
      /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh
$ grep -rl --include='*.md' -e 'rented-slice-plan' -e '60d1496' -e 'stage_rented_slice' docs experiments STATUS.md spec
docs/2026-09-21-successor-measure-rehearsal.md
docs/successor-rented-slice-staging-2026-09-21.md
docs/known-failure-modes.md
docs/rulings/2026-09-22-launcher-argument-guard.md
experiments/rehearsal-successor-measure/README.md
experiments/06-mvm-0a-constructed-self-index/argument-guard-method.md
experiments/06-mvm-0a-constructed-self-index/compute-ledger.md
experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-22-rehearsal-rerun-from-code-claude-worktree.md
experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-tier2-packet.md
experiments/06-mvm-0a-constructed-self-index/reviews/packets/2026-09-21-a3-closure-tier2-chatgpt-21-compute-ledger-part3.md
experiments/06-mvm-0a-constructed-self-index/reviews/packets/2026-09-21-a3-closure-tier2-gemini.md
$ grep -c -i plan …/reviews/2026-09-24-sleep-guard-check-claude-worktree.md …/reviews/2026-09-24-sleep-guard-fixes-check-claude-worktree.md
…sleep-guard-check…: 1        (line 301, about a hung launcher, not the plan)
…sleep-guard-fixes-check…: 0
$ grep -n SleepDisabled …/reviews/2026-09-24-sleep-guard-fixes-check-claude-worktree.md
21:end as at the start: the never-sleep override off (`SleepDisabled 0`), drawing from
$ git log --format='%h %s' -1 a0723bc^2          (pull request 30's merge)
5913bfa Tell the operator what the keep-awake cover does not reach
$ grep -n 'SLEEP_REFUSAL="the never-sleep\|SLEEP_FIX="sudo pmset\|SLEEP_FIX="plug in' …/src/launch_a3_fetch_first.sh
292:  SLEEP_REFUSAL="the never-sleep override is OFF (SleepDisabled $SLEEP_OVERRIDE) — shu…
293:  SLEEP_FIX="sudo pmset -a disablesleep 1      (put it back afterwards with: sudo pmse…
299:  SLEEP_FIX="plug in the power adapter, then re-run"
$ awk 'NR==67||NR==69||NR==70' $L | grep -o 'go[^|]\{0,20\}verbatim[^|]\{0,60\}'
go, quoted verbatim per C2(b): "Go"** (2026-09-15, in direct reply to Claude naming the run …
go, quoted verbatim per C2(b): "Go"** (in direct reply to Claude staging the wave …
go, quoted verbatim per C2(b): "Go. Launch the control-learnability pilot as staged: …
```

Reading: the wider search finds one file the packet's own search did not cover,
`argument-guard-method.md`; it is a method document, not a filed check. **This
session also finds no filed check of the plan file as it stands at `60d1496`.**
The packet's condition 1 on page 9 stands (MEASURED). Items 5 and 6 above are the
two errors on this page.

---

## The nine source disagreements, each side quoted

1. **Cap and envelope.** Holds. The 2026-09-20 ruling, line 30: "Successor spend
   cap: $130, within the MVM-0a $400 envelope". The spending proposal, section 1.1:
   "Proposed cap for the successor: **$130**, covering rehearsal (up to $10),
   development runs (up to $10), nine registered 30M runs (about $110) and one
   re-run (about $12)" … "The four items sum to $142". The two-release ruling
   mentions $130 only as money left unauthorised (`grep -n 130` → line 115 "still
   leaving about $130.30 unauthorised", line 193 "roughly $130 unauthorised"),
   never as the cap. The spending proposal, section 7: "**Successor cap $225**" and
   "**Programme envelope $400 to $460**". The weekend roadmap, lines 168–170:
   "set the successor cap at $142 … rule the programme envelope up from $400 to
   $450". (MEASURED)
2. **The registered-text pointer.** Holds. The pre-registration note (pasted
   above) against `STATUS.md` line 85, "(5) how to correct a measured value in
   registered text that its cited record does not contain", and the TimeAssembler
   task "DECIDE (John): how to correct a measured value in REGISTERED text that its
   cited record does not contain", status to-do. The task's body was not opened.
   (MEASURED)
3. **The seed count.** Holds. Rehearsal line 838: "the arithmetic for a
   half-width of 0.05 implies **one seed**". Proposal line 1051: "Three arms ×
   three seeds". Range-and-direction ruling line 137 (section 3): the spread
   "leaves out a source of variation as large as the tightness it was aiming for".
   (MEASURED)
4. **The learn-both reference points.** Real, but mis-cited: see item 1 of "What
   must change". Section 8.1 says "references and not thresholds"; the section 9
   table says "against the measured competing solver". Rehearsal line 689: the
   name-only solver "reaches **1.0000** on the named-other condition". (MEASURED)
5. **Whether S1 fired.** Holds, with the section citation off (item 8). Rehearsal
   line 204: "**R-1** … **FAIL**"; line 55: "the rehearsal's reading rather than a
   ruling"; line 714: "This is the rehearsal's adjudication and not a ruling, and
   it is John's to overturn". (MEASURED)
6. **The Wittgenstein note's premises.** Holds. The note: "the successor's $130
   cap and the 2026-10-11 registration target". The 2026-09-20 ruling, lines 95–96:
   "registration commit target of 2026-10-11 in item 1 was pacing, so it goes with
   the calendar". (MEASURED)
7. **The ledger's header.** Holds. Ledger line 3: "Cap: **$200 for the entire
   registered design**"; line 62 (the 2026-08-15 row): "cap now $400 per Amendment
   A2". (MEASURED)
8. **Two ruled tasks still open.** Holds. TimeAssembler lists "[todo] DECIDE
   (John): the entangled and free arms' numbers are one sample, not a measurement"
   and "[todo] DECIDE (John): how to correct a measured value in REGISTERED text …".
   The range-and-direction ruling's "What the question was" (line 42) is the first
   of these questions. Whether it fully answers the task is a reading (ARGUED:
   yes, it does).
9. **What is owed before the go.** Holds. Launcher-guard ruling line 84: "What is
   owed before a fresh go: the amended plan, checked by a session other than the
   one that amended it"; `STATUS.md` line 75: "what is owed first is the amended
   plan, checked by a session other than the one that amended it"; no filed check
   found (page 9 above). (MEASURED)

---

## Confidence and strongest argument against, on every recommendation

```
$ grep -n -o '^\*Recommendation[^:]*:\|^\*\*Recommendation[^*]*\*\*' $P
169 200 230 263 296 328 358 388   (pages 1a–1h: moderate ×6, moderate to high ×2)
644 (page 4, moderate)  744 (page 5, moderate)  884 (tripwire, high)
958 (page 7, moderate to high)  1016 (8a, high)  1082 (8b, high)
1203 (page 9, high on the shape and moderate on the timing)
$ grep -n -o '^\*Strongest argument against[^*]*\*\|^\*\*Strongest argument against[^*]*\*\*' $P
175 208 239 270 302 337 363 392 466 554 655 754 853 890 964 1021 1088 1210
```

Three recommendations use a different wording and the pattern above does not
catch them; each was read by hand: page 2 (line 458, "confidence high on the
arithmetic and moderate on behaviour at the registered size"), page 3 (line 547,
"confidence high that both the code and the text change are needed; moderate on (i)
over (ii)") and page 6's cap and envelope (line 831, "confidence moderate on the
envelope and high on recording the cap's status"). That makes 18 recommendations
and 18 strongest-argument paragraphs. The index table's confidence column matches
each page. (MEASURED)

---

## What this check could not settle

- Whether the packet's recommendations are *right* is John's to rule; this check
  tests the numbers and quotes they rest on, not the judgement.
- The rehearsal figures were checked against the findings file, not recomputed
  from the rehearsal's output files.
- The TimeAssembler task bodies were not read, so one quote on page 8b is
  unchecked.
- A filed check of the plan file may exist under a name neither search matched.
  The claim is that none was found, not that none exists.

---

## Re-check, 2026-09-24 (Pacific, 19:00 onward): the twelve findings against commit `614443d`

*Appended by the same checking session. It adds to this file; nothing above
this heading is changed. The target is commit `614443d` on
`worktree-weekend-1-queue-packet` (pull request 34), "Apply the twelve findings
of the packet's check (pull request 35); no recommendation changes". Before it,
`fa7aeca` merges the main line into that branch. Only the twelve findings were
re-checked, plus any new source claim the fixes introduced. The packet was not
edited.*

**Answer first.** All twelve are fixed and match their sources (MEASURED). The
fixes bring in two new small problems, neither of which changes a number John
rules on (items R-A and R-B below). Both scripts' outputs are in the packet's
Appendix A as check 8, and they are byte-identical to a fresh run on the tree
of `614443d` (MEASURED). The money figures are the same values as before. Page
6's table now gives them to the cent from this check's sum, with the ledger
row's own rounding beside them (MEASURED).

### How it was run

```
$ git fetch -q origin && git log --oneline main..origin/worktree-weekend-1-queue-packet
614443d Apply the twelve findings of the packet's check (pull request 35); no recommendation changes
fa7aeca Merge remote-tracking branch 'origin/main' into worktree-weekend-1-queue-packet
555f215 Build John's ruling packet for 2026-09-26: nine decisions, one page each
$ git diff --stat fa7aeca 614443d
 .../rulings/2026-09-26-weekend-1-queue-PROPOSAL.md | 321 +++++++++++++++++----
 1 file changed, 263 insertions(+), 58 deletions(-)
$ git show 614443d:docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md > packet2.md
$ diff packet.md packet2.md          (read in full; every change is quoted below)
```

The fix commit changes only the packet. Line numbers below are in the new
packet (1,608 lines).

### The twelve, one by one

1. **Disagreement 4 and page 1b: fixed.** MEASURED. New lines 103–112:
   "The proposal's section 9 table sets the learn-both threshold 'against the
   measured competing solver' (… section 9). Its section 8.1 says the opposite of
   the same solver: the reference points are 'reported alongside, and they are
   references and not thresholds'". Page 1b, lines 220–231: option (ii) now
   reads "as the section 9 table of the proposal words it ('against the measured
   competing solver')", and "which is what proposal section 8.1 already says of
   all three reference points". Source: proposal line 594, "…against the
   measured competing solver |"; lines 547–548, "Reference points reported
   alongside, and they are references and not thresholds". Both quotes are word
   for word.
2. **Page 1e count: fixed.** MEASURED. Lines 311–318: "with the degenerate
   all-sites set excluded: 44 site sets × 4 rank caps (1, 2, 4, 8) × 1 label =
   **176** comparisons per arm and seed. The 45 site sets are 9 layer sets × 5
   position sets (… `rehearse.py`, the candidate layer sets and positions near
   line 53) … 'has to be excluded in writing'". Source: `rehearse.py` lines
   53–55 (9 layer sets, 5 positions, including (0, 1, 2, 3, 4) and "all");
   rehearsal line 603, "has to be excluded in writing". 44 × 4 × 1 = 176.
3. **"$12 a run": fixed on every page.** MEASURED. New disagreement 10 (lines
   139–151) quotes the proposal's "the ledger's $12 planning figure" (proposal
   line 1051, section 12.4, word for word), the guide line "Registered
   training, 5 seeds × full+twin" at "~$12 (30M)" (ledger line 388), and "now
   known-stale" (ledger line 360). Page 4 (lines 673–680) now uses the
   2026-09-19 row ("about 10.0h ≈ $9.9", ledger line 70) and the 2026-09-15
   row ($13.92, "$3.8 of the total is AVOIDABLE IDLE", line 67), and calls $12
   "The proposal's own per-run planning figure". Page 5 drops the ledger-guide
   row from its table and says "$36 at the proposal's planning figure" (line
   758). Page 6's table row (line 835): "the proposal's planning figure, not a
   ledger row". A search for leftover wording:
   `grep -c -i "ledger's planning\|ledger's own planning" packet2.md` → **0**.
   One new placement error in disagreement 10 is item R-A below.
4. **The $10.30 row: fixed.** MEASURED. Line 837 (page 6 table): "about $10.30
   across four occurrences | the 2026-09-19 row and the first 2026-09-20
   follow-up row"; line 1224 (page 9): "(ledger, the 2026-09-19 row and the
   first 2026-09-20 follow-up row)". Source: `grep -n 'about \$10.30 across
   four' compute-ledger.md` → lines 70 and 72, which are those two rows.
5. **Page 9 staging-document claim: fixed.** MEASURED. Lines 1175–1178:
   "The staging document carries the estimate and the cap, and says of the
   rehearsal line only that it 'is up to $10 and of which nothing has been
   spent' — it predates the two cents (… staging …, section 7)". Source: staging
   document line 179, "rehearsal line is up to $10 and of which nothing has been
   spent", under "## 7. What it costs".
6. **Plan regenerations: fixed.** MEASURED. Lines 1202–1204: "twice since the
   staging document was written (commits `c4165b3` and `60d1496`; a third commit,
   `e95d127`, changed the staging script that generates it and not the plan
   file)". Appendix A check 5 now also prints the plan file's own log (lines
   1383–1386). Source: `git log --oneline -- …/out/rented-slice-plan.txt` →
   `60d1496`, `c4165b3`, `8bc5fbe`; `git show --stat e95d127` lists
   `stage_rented_slice.sh` and not the plan file.
7. **"Still owed": fixed.** MEASURED. Lines 598–601: "The ruling file says this
   work is 'still owed' in its 'What was NOT ruled here' section (its section 3
   says the problem 'is not closed by this ruling')". Source: nomination-label
   ruling line 147 under "## What was NOT ruled here"; line 92 under "## 3.",
   "**The nomination problem is not closed by this ruling.**"
8. **Disagreement 5: fixed.** MEASURED. Lines 115–117: "rehearsal's
   adjudication and not a ruling" (… section 8; its section 0 says 'the
   rehearsal's reading rather than a ruling')". Source: rehearsal line 714,
   under the section 8 subheading "Does the proposal's first stop condition
   fire?"; line 55, under "## 0.".
9. **Three quotes: fixed.** MEASURED. (a) Line 774: "a network can be built
   with ownership multiplied into every layer and still learn to concentrate it
   in a low-rank direction", word for word from proposal lines 1203–1204. (b)
   Lines 386–387: "Neither is ruled out for later.", word for word from the
   range-and-direction ruling, line 119. (c) Lines 634–641 give S1 in full:
   "The rehearsal fails item R-1 (the grammar is not learnable at tiny scale
   even in principle) or item R-8 (the transplanting code does not pass its
   known-answer tests). Nothing trains. About $10 spent.", word for word from
   rehearsal lines 668–670. The fix adds two claims, both checked: S1 is "from
   section 11 of the proposal" (proposal line 818, under "## 11. Order of work,
   and where it stops"), and "Item R-8 passed (rehearsal section 2a)" (rehearsal
   line 211, status column "**PASS.**").
10. **The $91 to $95 range: fixed.** MEASURED. Lines 895–901: "On the spending
    proposal's own base of $10.20 a run, its nine-run line of $125.46 falls to
    about $91 to $95 at the measured ratios (that document itself gives $91.80 at
    a ratio of exactly one …). Nine runs at the proposal's $12 planning figure
    would be $108, a different basis." Source: spending proposal section 3.2,
    "$10.20 base", "Total $125.46", "nine runs cost $91.80". Arithmetic, as in
    the first pass: $90.6 to $94.8.
11. **Script outputs in the appendix: fixed.** MEASURED. Check 8 (from line
    1432) carries both outputs. Details and the comparison with a fresh run are
    below.
12. **Staleness: fixed.** MEASURED. Lines 25–27: "That file was uncommitted when
    this packet was first written and reached the main line afterwards, in
    commit `b5cfc23`." (`git log --oneline 97ee3c9..main` lists `b5cfc23` "Add
    the weekend roadmap, its structured twin for the site, and the weekend 1
    session prompts".) Lines 1597–1599: "the seven `awaiting-john` tasks not yet
    done … (six to do and one in progress, the Amendment A3 closure sessions)",
    which matches the TimeAssembler list read in the first pass.

### Two new things the fixes introduced

- **R-A. Disagreement 10 puts the ledger's reconciliation note "above the
  ledger table"; it is below it.** MEASURED. Packet lines 146–148: "the
  2026-08-12 reconciliation note above the ledger table". The ledger's table
  runs from line 55 ("## Ledger") to line 74. The note starts at line 325
  ("**⚠ 2026-08-12 reconciliation: FAIL …"), and the guide at line 383.
  `grep -n '^## Ledger\|^## Phase budget\|2026-08-12 reconciliation'
  compute-ledger.md` → `55`, `325`, `383`. One word to change: "above" becomes
  "below". The quoted words are correct.
- **R-B. Page 6's headline money figure is now cited to this check file, which
  is on pull request 35 and not on the main line.** MEASURED that the citation
  is there (line 827) and that `check_citations.py` reports the path missing on
  the packet's tree (below). ARGUED that it matters. The packet's own rule
  (line 14) is that "The only source for money is the compute ledger". The
  cell still quotes the ledger row, so the ledger is still named. But the
  to-the-cent figures ($227.63, $172.37, $46.18, $53.82) now rest on a review
  that only lands if pull request 35 merges. Either merge pull request 35
  first, or cite the ledger rows as the source and name this check only as
  where the sum was done. A smaller point, also ARGUED: page 4's sentence "The
  ledger's measured actual-after rows for single 30-million-parameter runs are
  about $9.9 … and $13.92" leaves out one more single 30M row, the 2026-08-15
  re-run at about $18.9 over about 19 hours, which was a different, earlier
  design. The sentence reads as the full list, but the point it makes (about
  $10 to $14 a run on the current design) is unaffected.

### The scripts: pasted outputs against a fresh run on the same tree

The fresh run used an exact copy of the `614443d` tree, not this worktree,
because this worktree sits on an older main line and holds this check file,
which would change one result. The main line has since moved to `a741eee`,
which `614443d` does not contain (`git merge-base --is-ancestor origin/main
614443d` → exit 1). The packet's run is of its own tree, and so is this one.

```
$ git archive 614443d | tar -x -C tree614
$ cd tree614
$ .venv/bin/python scripts/check_citations.py --only docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md > fresh_cit.txt      (exit 1)
$ .venv/bin/python scripts/check_single_source.py --only docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md > fresh_ss.txt    (exit 1)
$ (the two pasted blocks cut out of the packet's check 8 into pasted_cit.txt and pasted_ss.txt)
$ diff pasted_cit.txt fresh_cit.txt && echo "check_citations: IDENTICAL"
check_citations: IDENTICAL
$ diff pasted_ss.txt fresh_ss.txt && echo "check_single_source: IDENTICAL"
check_single_source: IDENTICAL
$ wc -l pasted_cit.txt fresh_cit.txt pasted_ss.txt fresh_ss.txt
      57 pasted_cit.txt
      57 fresh_cit.txt
      69 pasted_ss.txt
      69 fresh_ss.txt
```

The fresh run, pasted (the same text as the packet's check 8):

```
$ .venv/bin/python scripts/check_citations.py --only docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md
==============================================================================
check_citations.py - do the pointers land, and are the cited numbers there?
==============================================================================
Documents read: 1   scope: live

------------------------------------------------------------------------------
PART (a): does every file a document names exist?
------------------------------------------------------------------------------

[CONFIDENT] 3 reference(s) name a file that is not in the repository
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:22
      names: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-weekend-1-queue-packet-check-claude-worktree.md
      in:    The check of this packet is filed at `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-weekend-1-queue-packet-check-claude-worktree.md` on pull r
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:52
      names: docs/rulings/2026-09-26-weekend-1-queue.md
      in:    The plan for the weekend (`docs/weekend-roadmap-2026-09-24.md`, section 7) says the rulings are written up as a new file, `docs/rulings/2026-09-26-weekend-1-que
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:827
      names: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-weekend-1-queue-packet-check-claude-worktree.md
      in:    every spend row added independently by the check of this packet (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-weekend-1-queue-packet-check-c

[LOOK AT IT] 0 bare name(s) match more than one file

[LOOK AT IT] 1 name(s) of run-output files that are not in the repository
             (this repo does not commit `artifacts/`, so most of these point at
              uncommitted output rather than at a broken citation)
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:1271  bench_arms.json
      in: **What the ruling changes, and where.** Nothing in any document until the go is spoken; then a ledger row written before the machine exists, quoting the go; the

[LOOK AT IT] 2 reference(s) written with a gap or a wildcard that matched nothing
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:40  experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-<model>.md
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:1052  experiments/<experiment>/reviews/YYYY-MM-DD-<target>-<reviewer>.md

[NOT CHECKED] 1 reference(s) to files outside this repository
     1x  ~/Documents/Code/CLAUDE.md

[NOT CHECKED] 0 reference(s) to paths .gitignore keeps out of the repository (run outputs and caches, deliberately not committed)

------------------------------------------------------------------------------
PART (b): is a figure given with a citation actually in the file cited?
------------------------------------------------------------------------------

[CONFIDENT] 0 exact figure(s) absent from the one file their sentence cites

[LOOK AT IT] 2 figure(s) worth a human eye
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:878
      figure: $91    cited: docs/preauthorised-spending-proposal-2026-09-21.md    (only an approximate match found)
      in:     On the spending proposal's own base of $10.20 a run, its nine-run line of $125.46 falls to about $91 to $95 at the measured ratios (that document itself gives $91.80 at a ratio of exactly one; `docs/p
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:878
      figure: $95    cited: docs/preauthorised-spending-proposal-2026-09-21.md    (only an approximate match found)
      in:     On the spending proposal's own base of $10.20 a run, its nine-run line of $125.46 falls to about $91 to $95 at the measured ratios (that document itself gives $91.80 at a ratio of exactly one; `docs/p

==============================================================================
Confident findings: 3. Things for a human to look at: 5.
A confident finding is not a verdict. Read the sentence before acting on it,
and read the 'what this cannot check' note at the top of this file before
reading a clean run as reassurance.
==============================================================================

$ .venv/bin/python scripts/check_single_source.py --only docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md
==============================================================================
check_single_source.py - does every money figure trace back to the compute ledger?
==============================================================================
System of record: experiments/06-mvm-0a-constructed-self-index/compute-ledger.md
Documents read: 1   scope: live   figures below $0 ignored
Figures that are in the ledger and point at it: 11
Set aside as forecasts (a proposal pricing something, not a record of spend): 107
Set aside as neither, by the wording around them: 52

------------------------------------------------------------------------------
[CONFIDENT] Group 1: a dollar figure the ledger does not contain
------------------------------------------------------------------------------
6 found. Either the document is stale or the ledger is missing
a number it should state. A total summed across ledger rows lands here too.
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:77   $130
      names instead: docs/rulings/2026-09-20-december-result-roadmap.md
      in: **The successor's cap and the programme envelope.** The ruling of 2026-09-20 sets a flat cap of $130 (`docs/rulings/2026-09-20-december-result-roadmap.md`, item 4).
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:118   $130
      in: **The Wittgenstein note's premises.** The note asks whether its second test fits "the successor's $130 cap and the 2026-10-11 registration target" (TimeAssembler note, "Questions for the session").
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:871   $450
      in: (ii) The weekend roadmap's pair: a successor cap of $142 and an envelope of $450.
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:871   $175
      in: (iv) RT-176's: raise the cap to $175 and leave the envelope until the slice reports.
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:878   $450
      names instead: docs/weekend-roadmap-2026-09-24.md
      in: Second, **rule the envelope up now, with the number and what it buys, as that standing rule requires; the number this packet puts forward is the weekend roadmap's, an envelope of $450** (`docs/weekend
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:983   $130
      in: The note's questions ask whether test 2 fits "the successor's $130 cap and the 2026-10-11 registration target"; both premises have moved (disagreement 6 in the index).

------------------------------------------------------------------------------
[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source
------------------------------------------------------------------------------
0 found. This is a second home being built for a number
that already has one.

------------------------------------------------------------------------------
[LOOK AT IT] Group 3: in the ledger, and no source named
------------------------------------------------------------------------------
13 found. Right today, and with nothing pointing at the record that
would correct it tomorrow. This is the state the stale $215.70 copies were in.
By document:
    13  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md

The first 13 in full (use --only <path> for one document's own):
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:634   $10   in: About $10 spent." Item R-8 passed (rehearsal section 2a).
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:747   $13.92   in: $13.92, "$3.8 of the total is AVOIDABLE IDLE"
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:747   $3.8   in: $13.92, "$3.8 of the total is AVOIDABLE IDLE"
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:747   $10.1   in: about $10.1 clean, $13.92 as billed
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:747   $13.92   in: about $10.1 clean, $13.92 as billed
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:800   $32   in: And it costs $32 to $44 the envelope does not hold, so ruling (i) or (iii) is also ruling page 6.
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:800   $44   in: And it costs $32 to $44 the envelope does not hold, so ruling (i) or (iii) is also ruling page 6.
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:827   $400   in: Programme spent, of the $400 ceiling ruled with Amendment A2
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:831   $0.02   in: about $0.02 spent, about $9.98 left
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:831   $9.98   in: about $0.02 spent, about $9.98 left
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:866   $44   in: no cap named; about $44 + about $131
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:866   $131   in: no cap named; about $44 + about $131
  docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md:871   $142   in: (ii) The weekend roadmap's pair: a successor cap of $142 and an envelope of $450.

------------------------------------------------------------------------------
[LOOK AT IT] The same figure in many documents
------------------------------------------------------------------------------
0 figure(s) appear in four or more documents. A figure with many homes
is a figure a correction has to find many times.

==============================================================================
Confident findings: 6. Things for a human to look at: 13 unsourced figures and 0 widely repeated ones.
The ledger is taken as true here. Read the 'what this cannot check' note at the
top of this file before reading a clean run as reassurance.
==============================================================================
```

Reading (MEASURED): three files are reported missing. Two are this check file,
on pull request 35 and not yet on the main line; the third is Saturday's
rulings file, by design. No cited figure is missing from the file its sentence
cites. The six dollar figures the ledger does not contain are the same six
caps and proposals as in the first pass. The spending check now counts 11
figures in the ledger that point at it (8 before) and 13 unsourced ones for a
human to look at (12 before). The new one is "$10" at line 634, inside the S1
quote, where the dollar figure is the proposal's own wording.

### The money figures

```
$ grep -n -o -e '\$227\.6[0-9]*' -e '\$172\.[0-9]*' -e '\$46\.[0-9]*' -e '\$53\.[0-9]*' -e '\$402\.6[0-9]*' -e '\$2\.6[0-9]*' packet2.md
764:$172.40 827:$227.63 827:$227.6 829:$172.37 829:$227.63 830:$46.18 830:$53.82 830:$172.37
830:$46.2 851:$172.40 851:$2.60 866:$2.60 872:$2.60 888:$227.63 888:$402.63 889:$2.63
1290:$227.6 1291:$227.6 1292:$46.2 1293:$46.2
$ git diff 555f215 614443d -- experiments/06-mvm-0a-constructed-self-index/compute-ledger.md | wc -l
       0
```

MEASURED: the values have not changed. Page 6's table (lines 827–830) and its
"what it buys" sentence (lines 888–889) now carry this check's independent sums
to the cent: $227.63 spent and $172.37 left of $400; $46.18 and $53.82 of
Amendment A3's $100; $402.63 once the base plan is added, $2.63 over. The ledger
row's own rounding ($227.6, $46.2) is quoted beside them. The other places
(lines 764, 851, 866, 872 and Appendix A's check 1 at lines 1290–1293) keep the
figures the documents they quote use ($172.40, $2.60, $227.6, $46.2). These are
the same amounts at a different rounding, not a different number. The compute
ledger is unchanged between the packet's two commits (zero changed lines,
above), so nothing has been spent since the first pass.

### What must still change

1. R-A: in disagreement 10, "above the ledger table" becomes "below the ledger
   table". MEASURED.
2. R-B: merge pull request 35 before or with pull request 34, or source page
   6's to-the-cent money figures to the ledger rows and name this check only as
   where the sum was done. ARGUED.

Neither changes a number or a recommendation John rules on Saturday.
