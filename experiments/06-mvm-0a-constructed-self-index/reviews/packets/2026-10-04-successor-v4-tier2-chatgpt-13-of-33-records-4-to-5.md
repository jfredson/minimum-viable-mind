*This is file 13 of 33 of one review packet, pasted into a single conversation. It contains record 4 part 12 of 12 (THE TEXT UNDER REVIEW - successor experiment proposal, version 4); record 5 part 1 of 4 (the inside reviewer's findings on version 4 (Gate A, tier 1)). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 4 of 25, part 12 of 12 - THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete file, 292,507 characters) =====
Seven places where this session did not think the answer was its to give.
**John ruled on all seven on 2026-10-03, late evening, in the words "Agreed
on all", taking the suggestion in each** (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`).
The questions are left below as they were put, so that a reader can see what
was chosen against what; "written as run" and "this version says" in them
describe the first filing of this version, and the body now carries each
ruling where it bears. None of them changes a toy figure. **Two things to
hold on to.** Question 6 was the one this session said deserved more of
John's attention than the others, and a general agreement settled it; the
record of the ruling says so. And question 7 leaves a run owed before the
registration review.

1. **Does the whole read still have to reach four fifths, now that the piece
   does?** The ruling of 2026-09-26 (RT-212) put the fit floor on the whole
   read, at the worst layer of the nominated site set. The ruling of
   2026-10-03 (page 1) says only sizes whose own accuracy clears may be
   chosen, printed "beside the whole read's", and does not say whether the
   earlier floor remains a second condition. The controls re-run applied the
   floor to the piece only. On the toy both readings give the same twelve
   verdicts, but a piece can score an episode or two above its whole read.
   *Written as run: the floor is on the piece (sections 6.4, item 2, and
   7.2, item 1).* **Suggestion: the piece only, with the whole read's count
   printed.** Confidence moderate. It is the piece that is transplanted, and
   a second floor is a second way to return no verdict on the arm being read,
   for no gain the first does not give. Strongest alternative: require both,
   which costs nothing on the toy and keeps the 2026-09-26 ruling to its
   letter.

2. **The piece rule is applied after the layers are chosen.** So it decides
   which sizes may be chosen and never changes which layers are used. That
   was the re-run method's own reading, marked as John's to overturn; the
   check noted it has not been put to him in terms. *Written as run (section
   7.2, item 3).* **Suggestion: confirm it.** Confidence moderate. The
   alternative, letting the piece's accuracy also decide between layer sets,
   has not been run, and would need the toy re-run again before the
   registration review.

3. **Which device, and which number format, is the registered fit computed
   on?** The ruling (page 3, RT-232) says the registration names them and
   that the figure on the named device is the registered one. It does not
   say which. *This draft writes in the laptop's processor, the model's
   states in 32-bit, the read fitted by scikit-learn in 64-bit, the library
   versions recorded (section 7.2, item 1).* **Suggestion: confirm that.**
   Confidence high on the processor, because every toy figure in this version
   was computed on it and it is the one device every later reader will also
   have; moderate on whether the registration should also pin the library
   versions exactly or only record them. Strongest alternative: the graphics
   chip, which is faster on a 30-million-parameter model and is what the
   earlier committed fits used.

4. **The numbers of episodes at the registered size.** The brief for this
   version asks for every frozen number to be stated. Every bar is stated,
   but each is a share or a rule, and no ruling sets how many development,
   held-out and fresh episodes the registered measurement uses, how many are
   on the relaxed set, how many held-out episodes the gates are scored on, or
   how many shuffles the permutation null uses. *The registration must print
   them; this version lists them as not set (section 9, the last row).*
   **Suggestion: the toy's counts, unchanged: 600 development episodes with
   the last 180 held out, 800 fresh matched pairs, 800 on the relaxed set,
   3,000 for the gates, 200 shuffles.** Confidence moderate. They are the
   only counts the procedure has been rehearsed at, the floor is then 144 of
   180 as on the toy, and section 11 already argues the registered model's
   states fit on the laptop at that scale. Strongest alternative: more
   held-out episodes, so that the floor is not decided by a handful: at 180,
   one episode is 0.0056, and the toy has already shown fits moving by one
   episode between devices.

5. **Control 2's comparison: one random piece or twenty?** The ruling keeps
   control 2 as a description: how often the own-directed action moves under
   the named agent's piece, beside how often it moves under "a random piece".
   The code draws one, with its own seed; control 3 draws twenty. *Written
   as the code runs, one draw (section 7.3, item 2).* **Suggestion: twenty,
   reported as control 3 reports them.** Confidence moderate. With no pass
   line a single draw is a weak thing to print beside a figure. It is a small
   code change, and it would mean the code path that ran once on 2026-10-03
   is not quite the one registered. Strongest alternative: leave it at one,
   since the control is expected to return no verdict anyway.

6. **What is an arm's outcome when its seeds disagree?** The floors and the
   controls that hold apply per arm and seed, so an arm can read on two seeds
   and return no verdict on the third. The ruling on what a no verdict maps
   to (page 11) speaks of "no verdict on arm C", "on arm M" and "on arm F"
   and does not say how many seeds make that so. The separation bar is
   written "per seed" in the same way, without saying what follows if it is
   cleared on two seeds of three. On the toy every arm behaves alike on all
   three seeds, so this has never bitten. *Not written into the body beyond
   section 3 saying the case is open.* **Suggestion: the rule the design
   already uses for its gates, at least two seeds of three, with the third
   reported.** Confidence low to moderate; this is a new pre-stated rule and
   deserves his attention more than the others. Strongest alternative: all
   three seeds, which is stricter and makes the fifth outcome and the
   two-arm fallback more likely.

7. **The ordinary competing solver under the piece rule.** The protocol's
   rehearsal asks that a system with none of the structure the measure
   claims to detect be put through the same measurement. The ownership-blind
   solver and the name-only solver were scored on both conditions before the
   piece rule existed, and the controls re-run did not load them. *This
   version says so in three places and quotes no figure for them as if it
   were under the new rule (sections 7.3, 8.1 and 10).* **Suggestion: run
   the ownership-blind solver's three committed toy models through the
   nomination and reading as now registered, on the laptop at $0, method
   committed before output, before the registration review opens.**
   Confidence moderate to high. The expected result is a no verdict (a
   solver with no acting channel should have no read of its own marker that
   reaches four fifths), it is an afternoon, and without it the registration
   review's first question on "satisfied by the wrong thing" has an argument
   behind it and not a number. Strongest alternative: state in the
   registration that it was not measured under the rule, and let the
   reviewer decide whether that is a finding.

**Two things that are not questions, said so they are not found later.**
John's ruling on decision 23 (which read is the registered one) still has no
ruling file of its own; it is carried from his revision instruction for
version 3. And the three rulings of 2026-10-03 were each given as agreement
to a packet or a suggestion, with the wording the recording session's; the
records say so themselves, and this version quotes the records.

---

## 20. Change log from version 3, keyed to the ruling or finding behind each change

"The morning rulings" are
`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` (main line at
`56a5a86`). "The re-run rulings" are
`docs/rulings/2026-10-03-controls-rerun-rulings.md` (`fe5df65`). "The evening
ruling" is `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`
(`f32ba0c`). "The review" is the first independent review of version 3,
findings RT-230 to RT-236 (`4cb7f8e`). "The check of the re-run" is at
`e184a6e`, and "the check of the packets" at `f32ba0c`.

- **RT-230 (serious: the floor certified the read, not the piece
  transplanted). The morning rulings, page 1.** The fit floor moved to the
  piece: only sizes whose own held-out accuracy reaches four fifths may be
  chosen, the piece's count printed beside the whole read's (sections 1, 6.4
  item 2, 7.2 items 1, 3 and 5, 7.4, 7.5, 9). Sections 3 and 5.2 reworded to
  what was measured: the read holds the label, the largest piece transplanted
  holds it, no size moves the action. Version 3's sentence that arm C's
  transplanted subspace "holds the label and clears the fit floor on every
  seed" struck. **Arm C's toy readings changed from 1.0051, 1.0025 and
  1.0000 to 1.0051, 0.9926 and 0.9974, with the sites and sizes the re-run
  chose** (sections 3, 5.2, 9, 10). The forecast on page 1 of the ruling
  packet (8, 8 and 4 directions; 0.9975 on seed 1) is not used: the re-run
  showed it wrong on seed 1, and the check of the packets says to quote the
  re-run (its section 7, row 6).
- **RT-233 (serious: four controls had no figure under the registered
  rules). The morning rulings, page 2.** The controls re-run is done and
  checked. Every figure for controls 1, 3, 4, 6 and 7, the true-slot
  reference, the rider and the stricter row is quoted from it (sections 5,
  7.2, 7.3, 10, W11). Version 3's sentences saying those figures were owed
  are gone.
- **RT-231 (minor: arm M's true-slot check, run by the review).** Arm M's
  blind reading is within 0.0049, 0.0099 and 0.0529 of its true-slot reading
  at the registered site sets (sections 5.3, 9, 10 R-3). **0.0099, not the
  0.0100 the re-run's prose printed** (the check of the re-run, section 7,
  item 3).
- **RT-232 (minor: fits move by one episode between devices). The morning
  rulings, page 3.** Fits stated as counts of held-out episodes; the
  registration names the device and number format, and the figure on that
  device is the registered one (sections 1, 5.4, 7.2 item 1, 7.5, 9). Taken
  from the review's own wording, which also names the number format, and not
  from the packet's shortening (the check of the packets, section 7, row 9).
  The device, the laptop's processor, was ruled late that evening.
- **RT-234 (minor: the whole-state floor is applied twice). Page 3.** Said in
  sections 6.4 item 1, 7.4, 7.5 and 9: on development episodes at nomination,
  again on fresh episodes at the reading, and a site set that clears the
  first and misses the second returns no verdict.
- **RT-235 (minor: the stop reads its fit at a layer the noise may pick).
  Page 3.** The report for the first full-size free-model run prints the
  read's count at every layer, the chosen piece's count and the candidates
  (sections 7.5 and 11, step 5a). Section 7.2, item 5, and section 5.2 now
  say that on an arm where nothing moves the action the choice is made among
  sampling noise.
- **RT-236 (minor: depths, and two citations by branch). Page 3.** Four
  blocks and five running states against twelve and thirteen, stated the
  same way (section 7.2, item 1). The label search and its check cited by
  their main-line commits, `a97c12b` and `ecd2b6c`, throughout.
- **Decisions 2, 3, 4, 8, 9, 10, 13, 17, 18 and 19. The morning rulings,
  pages 4 to 10, 14, 15 and 16.** Each marked ruled in section 15 and where
  it bears: sections 4.2, 5, 5.1, 5.2, 7.2 item 2, 8.2, 9, 10 R-11, 11 step
  5a, 12.2, 12.4, W8, W9. The handshake is described as ruled, option (b),
  with the caution carried (W9). **Not carried: the packet's sentence about a
  $97.04 loss, on its page for decision 13.** Version 3 left that sentence
  out on purpose, and the check of the packets found it is not what the
  ledger shows (its section 7, row 3).
- **Decision 14, what a no verdict maps to. The morning rulings, page 11; the
  evening ruling, ruling 1.** The fifth registered term, "metric validated,
  degree not read", added to the outcome table as satisfactory and stated as
  weaker than R1; the mapping for arms C and M written in; the paragraph on
  the open reporting gap replaced; the toy outcome restated as the fifth term
  (sections 1, 3, 7.4, 9, 11 steps 7 and 8, 15).
- **Decision 15, control 2's tolerance. Agreed in the morning rulings (page
  12); withdrawn by the re-run rulings, ruling 1.** Control 2 is a reported
  description with no pass line; the registration says in terms that it
  never ran at toy scale, why, and that a no verdict is expected; its one
  end-to-end run is quoted labelled NOT A RESULT (sections 7.3 item 2, 7.4,
  7.5, 9, 10, 11 S8, W7, W14).
- **Decision 16, control 4's standing. Agreed in the morning rulings (page
  13); reversed by the re-run rulings, ruling 2.** Control 4 redefined on the
  positions before both twins' first own turns, and made a control that
  holds, with the pass line that the outputs are bit-identical. Described as
  a known-answer test of the pairing and the code, which cannot fail on a
  correctly built model and whose pass says nothing about any model (the
  check of the re-run, section 5). The sentence that arms C and F "receive
  the ownership signal by other routes" withdrawn (sections 1, 6.4 item 5,
  7.3 item 4, 7.4, 7.5, 9, 10, W14). **Not carried: the re-run's sentence
  tying the six models with a large excess to their sites' position set as a
  cause**; the control uses only the site's layers (the check of the re-run,
  section 7, item 3).
- **The re-run rulings, ruling 3, and the evening ruling, ruling 2: the
  piece's accuracy at the other positions.** A reported figure, printed both
  ways, with how each is computed, and the toy's figures (sections 3, 5.2,
  5.3, 7.2 item 3, 7.4, 7.5, 9). The plain statement that the piece's four
  fifths is established at the action position only, with the figures for
  arms C and M, and a new weakness W13.
- **From the check of the re-run, section 7 (not a ruling).** The null
  transplant counted as tested at fifteen different places (sections 7.3
  item 7, 10 R-8). Two requirements on the registered code written in: the
  controls that hold withhold the reading in code (sections 6.4 item 5, 7.3,
  7.4); and the ordinary competing solver is said, in three places, not to
  have been measured under the piece rule (sections 7.3, 8.1, 10 R-5), with
  its run now owed by ruling.
- **The short pre-stated run.** Quoted for control 4 as redefined, for the
  new column, and for the one run of the part of control 2's code after the
  floor, labelled NOT A RESULT.
- **From the check of the short pre-stated run (main line at `53c8100`, pull
  request 82), section 10 (not a ruling).** Filed while this version was
  being written; the first commit of this version had marked the short run's
  figures as unchecked. All four of its notes are followed: control 4 is
  said to compare the outputs at the two action positions (section 7.3, item
  4); the new column's computation is set out in full, the figure on the
  average is said to be good to an episode or two on the toy, and the
  registered code averages in 64-bit (section 7.2, item 3); what the short
  run added for control 2 is said to be the part of its code after the floor
  (section 7.3, item 2; section 10); and the piece's four fifths is said to
  be established at the action position only (sections 3, 5.2, 5.3, W13).
  Also carried from it: the test is not empty (noise changes the outputs),
  the ten named positions are about a quarter of a span, the limit on what
  "pre-stated" can be shown to mean, and John's confirmation that section 4
  of the short run's method is what "print both figures" means.
- **John's late-evening ruling on this version's seven questions
  (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, filed with
  this version).** Each written in where it bears: the floor on the piece
  only (sections 6.4 item 2, 7.2 item 1, 9); the piece rule applied after
  the layers are chosen (section 7.2, item 3); the registered fit on the
  laptop's processor, library versions recorded (and, by the reconciliation
  ruling of the same night, pinned) (sections 7.2
  item 1, 7.4, 9); the toy's episode counts at the full size (sections 7.4,
  8.1, 9); twenty random pieces for control 2, with the code change that
  implies (sections 7.3 item 2, 7.4, 7.5, 9); two seeds of three when an
  arm's seeds disagree (sections 3, 7.4, 9); and the competing solver's run
  under the piece rule owed before the registration review (sections 7.3,
  8.1, 10, 11). Section 19 keeps the questions as put and says they are
  ruled.
- **The header, the source table, section 16 and section 17.** Rewritten for
  this version: sources by main-line commit, the eight new ones first; the
  author's failure-mode pass run again with this session's commands on the
  controls re-run's outputs. Section 18, the printed site list, is new.
  Section 19, the questions for John, is new. Version 3's change log from
  version 2 is not repeated; it is section 18 of version 3.
- **Left alone.** Sections 2, 4.1, 4.3, 4.4, 5.5, 6.1, 6.2, 7.1, 8.2 (but for
  one clause), 12.3, 12.5 to 12.8 and 14 carry version 3's text. Sections
  4.2, 6.3, 8.1, 12.1, 12.2 and 12.4 change by a sentence or a citation each.
  Wherever version 3's text says "this version" of a change it made from
  version 2, that change is carried here unchanged.

---

## What this version does not do

It edits nothing: not version 3, not any ruling, registered text or protocol
text, and not the findings of any run. It issues no go, releases no money,
launches nothing, trains nothing and rents nothing. It does not open the
registration review, and it is not ready for it: the competing solver's run
under the piece rule is owed, and this version and the record of the
late-evening ruling are owed a check under the pairing rule of
`docs/outside-review-protocol.md`. The seven questions of section 19 were
John's, and he ruled them; this version resolved none of them itself.
===== END OF RECORD 4, part 12 =====

===== RECORD 5 of 25, part 1 of 4 - the inside reviewer's findings on version 4 (Gate A, tier 1) - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md` (complete file, 80,950 characters) =====
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

===== END OF RECORD 5, part 1 =====

