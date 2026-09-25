# Check of the draft dispositions for the two outside reviews of the A3 closure text

*Filed 2026-09-25 (Pacific) by a Claude Code session in its own worktree
(`worktree-check-pr37-dispositions`), reading the head of the branch under
check, `worktree-a3-tier2-dispositions` at commit `06a5636` (draft pull
request 37, "A3 closure: file the two outside reviews and draft dispositions
(not ruled)"). The file under check is
`docs/rulings/2026-09-25-a3-closure-tier2-dispositions-PROPOSAL.md`, called
"the proposal" below. This session did not write the proposal, version 4 of
the closure text, or either outside review.*

*This is the check the proposal says it is owed under the pairing rule
(`docs/outside-review-protocol.md`, "The pairing rule"): a different session
checking text on its way to John. John asked for three things: re-run the
proposal's nineteen checks, C1 to C19, from a clean checkout and say whether
each reproduces; confirm the two filed reviewer files are byte-identical to
the ones in the main checkout; and check the proposal's item 19(e) against
`standardised-refit-findings.md`, which the proposal's writer did not.*

*What this session did not do: **it did not rule on anything**, and nothing
here is a recommendation about how John should rule on the proposal's lines.
It did not edit the proposal, the closure text, the red team ledger, any
ruling file or any protocol text. It ran no compute beyond `grep`, `sed`,
`cmp`, `shasum` and a four-line Python hash, and spent nothing. No web
lookup.*

`E/` is short for `experiments/06-mvm-0a-constructed-self-index/`.

---

## The answer in three lines

1. **All nineteen checks reproduce.** Eighteen give the same output the
   proposal prints. One, C19 (the highest red-team finding number in use),
   now prints `RT-204` instead of `RT-203`, and the only reason is that the
   proposal itself mentions RT-204. With the proposal left out, it prints
   `RT-203`, as stated. A few line citations are off by a line or two, and
   none changes what a check shows.
2. **Both reviewer files are byte-identical** on the branch and in the main
   checkout. But they are **not part of pull request 37**: they are on main
   already, in John's own commit `c89a3ef`, which the branch starts from.
   The proposal says they were "committed unedited in the same pull request
   as this proposal", and that is not so.
3. **Item 19(e): the findings file does not settle it, and taken alone it
   reads the other way. The committed code and the run's own output files
   show ChatGPT's point is right.** The standardised refit's 135 main tests
   used different fold splits and different shuffled-label draws from the
   unscaled run's. The findings file's statement that the run differs "by
   the scaling and by nothing else" is true of its anchor check only.

---

## 1. The nineteen checks, re-run

**How.** A fresh worktree was made, detached at `origin/worktree-a3-tier2-dispositions`
(`06a5636`) after `git fetch`, with a clean `git status`. Each command was
run from the repository root exactly as the proposal gives it, abridged
commands filled out in the obvious way. The locked worktree the proposal was
written in was not touched.

| # | Reproduces? | What this session got | Notes |
|---|---|---|---|
| C1 | **Yes** | `0` for version 4, `0` for version 3 | |
| C2 | **Yes** | line 756, RT-164: "… ACCEPT (drafted) … Done in version 3." | Both quoted fragments are on that line. |
| C3 | **Yes** | no output, exit status 1 (nothing found) in either of the two version 4 check files | |
| C4 | **Yes** | line 265: "**K5.** Probe-patching convergence fails on all three seeds: *not testable (localization)*, reported as such; no further seeds." | Word for word. |
| C5 | **Yes** | line 150: "machinery, ledger RT-96). Because the two instruments never converged on" | The line also carries the end of the previous sentence; the proposal quotes only the part that matters. |
| C6 | **Yes** | line 137: "…were never applied to the input-channel lesion on any seed…" | `grep` also hits lines 630 and 791 (the F17 heading and a later mention). The proposal cites only line 137, which is the one that matters. |
| C7 | **Yes** | line 13 "**270 testable tests**"; line 31 "### Arm 1 — the model's own marker word"; line 47 "### Arm 2 — the register index" | Also hits lines 16, 85 and 98, all mentions of 270; nothing contrary. |
| C8 | **Yes** | compute ledger line 293: "A3 cumulative is ~$44.3 -> ~$46.2 of $100, leaving ~$53.8, and the programme running total is ~$227.6 / $400" | Also hits line 74 (the rented-slice row). Version 4's money paragraph gives ~$44.3 on **line 232** and ~$225.7 on **line 233**; the proposal says line 232 for both, which is where the paragraph starts. |
| C9 | **Yes** | line 17 "Registration commit target 2026-10-11; kill date 2026-10-18."; line 95 "registration commit target of 2026-10-11 in item 1 was pacing, so it goes with" | The sentence finishes on line 96: "the calendar; the kill dates in items 1 and 7 are commitments and are unchanged." |
| C10 | **Yes** | line 85 carries "Any control that is fully determined by the visible episode and does not require ownership has an ownership-blind ceiling of 1.0 by construction" (it runs on to line 86); line 110 "The state battery's ceiling is 0.0676"; line 112 "…specific to a control designed to be ownership-free" | |
| C11 | **Yes** | line 652, RT-125, containing both "would produce the own-index pattern and this exact null together" and "ACCEPT, CARRIED OPEN" | |
| C12 | **Yes** | in lines 28–48 of the follow-up-runs ruling: "was discharged on 2026-09-16 and is not re-run" (line 41), and "requirement the arm serves … is carried into the successor's rehearsal" (lines 44–46) | Quotes match, allowing for line wrapping. |
| C13 | **Yes** | December-result ruling lines 18–23, including line 20 "patching is not built for the Amendment A3 design"; follow-up ruling line 19 "No further work on that position is authorised." | The follow-up ruling also hits line 43 ("is authorised. The A3 closure text does not wait on the arm"), which is about the blind arm, not the position; it does not change the check. |
| C14 | **Yes** | pre-registration line 84 "…result here closes that gap, and every write-up must say so"; line 529 "the same-act clause of the floor"; version 4 count `0` | Also hits lines 82, 95 and 527 of the pre-registration, all on the same limits. |
| C15 | **Yes** | lines 42–44: +0.0018, +0.0002, **+0.0769** | |
| C16 | **Yes** | lines 13–14: "**its per-row** / gradient weight quadrupled" | Also line 69, "quadrupling the control's per-row". |
| C17 | **Yes** | "The control battery's / ceiling has never been attacked" | The phrase is split across **lines 15 and 16**; the proposal cites line 16. |
| C18 | **Yes** | no packet file contains the heading, exit status 1 | Made stronger: the section's first sentence ("Twice a registration has gone in before anyone had run…") is also in no packet file, and the ChatGPT brief says at lines 152–156 that "Only the closure rule is reproduced" from the protocol. So this is not a heading-wording miss; the section really was not sent. |
| C19 | **Yes, with a note** | `RT-204` and `\| RT-171` | The only file containing "RT-204" is the proposal itself (its item 21 says to number from RT-204). Run against main at `c89a3ef`, the commit before the proposal, the highest is `RT-203`, found in `E/reviews/2026-09-21-protocol-repair-claude-worktree.md`. The check as written now counts its own proposal. The finding it supports (numbers above RT-171 are already in use outside the ledger) holds either way. |

**Line-number slips, all harmless:** C8 (version 4 money figures span lines
232–233), C9 (quote runs on to line 96), C17 (quote spans lines 15–16). The
proposal's headline count of serious findings, four from Gemini (G3 to G6)
and eleven from ChatGPT (A2, A3, A4, A6, A7, A8, A10 to A14), was also
recounted from the two files' severity columns and is right.

## 2. Are the two reviewer files byte-identical to the main checkout?

**Yes, both.**

| File | `cmp` branch vs main checkout | SHA-256 (both copies) |
|---|---|---|
| `E/reviews/2026-09-21-a3-closure-gemini.md` | no output (identical) | `8e0172213caacdcde524ce0718bb723bdd1709bffa93eabae3c19dc610b1e801` |
| `E/reviews/2026-09-21-a3-closure-chatgpt.md` | no output (identical) | `1195540909ecc1dc451b81f9c6aaf2369d5d55835966bff132f528a71f9f9936` |

The main checkout's working copies also match main's committed copies
(`git diff --quiet origin/main` passed for both), so there are no unsaved
edits in the main checkout either.

**But the proposal says something about them that is not true.** It says
the two responses were "committed unedited in the same pull request as this
proposal". They were not:

- `git diff --stat origin/main...origin/worktree-a3-tier2-dispositions`
  lists **one** file, the proposal. GitHub's file list for pull request 37
  said the same.
- Both reviewer files were added to main in commit `c89a3ef` ("File the two
  A3 closure tier 2 reviewer responses (Gemini 3.1 Pro, ChatGPT 6 Astra
  Medium), 2026-09-25", author John, 14:55:55 Pacific). That commit is the
  point the branch starts from, which is why the branch has them and the
  pull request's diff does not.

This matters only for the record: the files were filed by John on main, not
by the proposal's session in its pull request. The proposal's sentence
should say so before it lands. It does not affect the byte-identity result.

## 3. Item 19(e), checked

**What is at issue.** ChatGPT's A15 suggests replacing version 4's sentence
that the standardised refit "found the same thing everywhere but one cell"
(version 4, lines 117–119) with: *"The second estimator produced one nominal
crossing; its folds and permutation draws also differed, so the change
cannot be attributed to scaling alone."* The proposal holds this item back,
saying this session's writer did not check it and that the refit findings'
mention of folds (lines 100–104) "does not by itself show different folds".

**What `E/standardised-refit-findings.md` says.** Read in full (312 lines).
It never says the folds or the shuffled draws were different. It says the
opposite twice, in words a reader will take as covering the whole run:

- Lines 62–65: "The unscaled fit returned all fifteen recorded numbers with
  a largest difference of **0.0**, which proves this run differs from the
  recorded one by the scaling and by nothing else."
- Lines 84–85: "The two code paths are the same path, so the scaling really
  is the only thing that changed."

Both sentences sit under "The anchor, in three parts". Part A is a re-run of
the *unscaled* fit on the separate 400-episode anchor configuration, and
Part C is a self-test. Neither is the 135-test sweep at 4,000 episodes where
the one crossing happened. **So on the findings file alone, 19(e) cannot be
adopted, and a writer relying only on that file would reject it.**

**What the committed code and output say.** This goes one step past what
was asked, because the findings file does not decide the question.

- The per-test seed that fixes both the fold split and the shuffled-label
  draws is a hash of checkpoint, *target name*, position and layer
  (`E/src/fitted_position_sweep_a3.py`, `test_seed`, lines 125–130, which
  the refit imports).
- The unscaled run's target name is `"register_index"`
  (`fitted_position_sweep_a3.py`, line 95); the refit's is
  `"register_index_standardised"` (`E/src/standardised_position_sweep_a3.py`,
  line 128).
- Recomputed with the same hash for the cell that crossed (seed 2
  checkpoint, the other agent's revision value, layer 3): `1893158273`
  unscaled, `940077601` standardised. Different seeds, so different folds
  and different shuffled draws.
- The run's three committed output files say so in plain words
  (`E/a3-gates/standardised_position_sweep_a3_a3_30m_seed{0,1,2}.json`,
  field `seeding`): "The target name carries the standardised tag, so no
  test shares a split with the unscaled run's". The same sentence is in the
  code at lines 535–539.
- The anchor, by contrast, seeds its folds by layer alone
  (`standardised_position_sweep_a3.py`, line 300), so for the anchor the
  findings file's "nothing else" is true.

**Result.** ChatGPT's 19(e) is correct as a statement about the 135 main
tests: folds and shuffled draws both differed, so the one crossing cannot be
put down to the scaling alone. What is MEASURED here is the seed difference
and the output files' own wording. That the crossing *would* have moved
under the old folds is not measured by anyone; the point is only that the
comparison does not isolate the scaling.

**A side effect worth recording, not ruled.** The findings file's "by the
scaling and by nothing else" overstates what the anchor check proves when it
is read as a statement about the whole run. That is a wording problem in a
committed findings file, separate from the closure text. It is noted here
for whoever writes version 5 and for the ledger, and this session made no
change to it.

## Sources

- The proposal, at `06a5636`:
  `docs/rulings/2026-09-25-a3-closure-tier2-dispositions-PROPOSAL.md`
- Version 4 of the closure text: `docs/a3-closure-text-draft-2026-09-21-v4.md`
- The two reviewer files: `E/reviews/2026-09-21-a3-closure-gemini.md` and
  `E/reviews/2026-09-21-a3-closure-chatgpt.md` (ChatGPT's A15 table, and its
  line 266 summary row)
- The refit: `E/standardised-refit-findings.md`,
  `E/standardised-refit-method.md` (lines 58–63 and 118–137),
  `E/src/standardised_position_sweep_a3.py`,
  `E/src/fitted_position_sweep_a3.py`, and the three committed output files
  under `E/a3-gates/`
- The commit that filed the reviewer files on main: `c89a3ef`
