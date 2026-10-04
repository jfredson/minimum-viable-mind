# Check of the short pre-stated run of 2026-10-03, and of the record of John's evening ruling

*Written 2026-10-03 (Pacific) by a Claude Code checking session, in its own
working folder, on branch `check/short-prestated-run-2026-10-03`, cut from the
main line at `f32ba0c`. Laptop, processor only. Nothing rented, nothing
trained beyond the small straight-line reads the run itself fits, nothing
spent: $0.*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (this session ran something or read it off a committed file or
off GitHub's own record, and says which) or **ARGUED** (a judgement, with its
reasons). This is a check of a rehearsal record on twelve toy models. It is
not a result about the scientific question.*

**What this session opened and what it did not.** Committed files only, plus
GitHub's own record of pull requests 80 and 81 (their commits, and the times
the branches were pushed). It did not open any chat or transcript of the
session that wrote the work. It wrote none of the work it checks. Where a
claim can only be checked against a transcript (for example, what John's
exact words were), this document says it could not be checked.

**What was checked.**

- The short run: its method (`docs/2026-10-03-short-prestated-run-method.md`),
  its findings (`docs/2026-10-03-short-prestated-run.md`), its code
  (`experiments/rehearsal-successor-measure/src/short_prestated_run.py`) and
  its outputs (`experiments/rehearsal-successor-measure/out-short-prestated-run/`),
  against the ruling that asked for it
  (`docs/rulings/2026-10-03-controls-rerun-rulings.md`).
- The record of John's evening ruling
  (`docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`)
  against his words as the record quotes them, and its dated note in
  `docs/december-result-roadmap-2026-09-20.md`.

This session's own scripts and what they printed are beside this file, in
`2026-10-03-short-prestated-run-check-scripts/`.

## 1. The short version

- **The run holds.** Method and code were committed and pushed before any
  output, the script has not changed since, and run again from the committed
  code it gives the same output files byte for byte. Every figure in the
  findings matches the output files. The code does what the method says and
  what the ruling asked.
- **Two small things for version 4 of the proposal**, neither of which
  changes a figure or a reading: say that the "outputs" compared in the
  too-early-position control are the model's scores at its two action
  positions (finding 7); and say that the figure taken on the average over a
  site is good to an episode or two, or fix how the average is added up
  (finding 11). A third is wording only (finding 15).
- **One limit on what "pre-stated" can be shown to mean here** (finding 3):
  the record shows the order of the commits and pushes. It cannot show that
  the script was never run before the method was committed, and the two
  pushes are 2 minutes 39 seconds apart. The harm this could do is small, for
  reasons given there.
- **The record of the evening ruling says what John's words say, with one
  narrow exception** (finding 19): it records *how* the two figures are
  computed as part of what was ruled. His words, "print both figures", accept
  that by implication only. One sentence from John, or the registration
  review, settles it.
- **The roadmap note is right** (finding 21).

## 2. Was the method committed before the output, and is the script unchanged?

1. **MEASURED. The method and code were committed with no output, and the
   output came in a later commit.** Pull request 80 has two commits. The
   first, `eb13dba`, adds two files only: the method and the script. No file
   under `out-short-prestated-run/` exists at that commit. The second,
   `29a2f47`, adds the findings and the five output files and touches neither
   the method nor the script. GitHub's own record of pushes shows the branch
   created at 01:22:12 UTC on 2026-10-04 holding the first commit, and the
   second commit pushed at 01:24:51 UTC. On both commits the time the commit
   was written and the time it was last rewritten are the same, so neither
   was altered after it was first made. (Source: `gh pr view 80`, the
   repository's activity record, `git show --stat`.)
2. **MEASURED. The script is unchanged since.** The pull request was merged
   by replaying its two commits onto the main line, so they have new ids
   there (`9e978d9` and `853988f`). The script's content fingerprint is the
   same, `26d9322c`, at both original commits, both main-line commits, and
   the head of the main line today. The method file's is likewise unchanged
   (`0268fbcc`). Only one commit in the history touches the script.
3. **ARGUED. What the record cannot show.** Commit order proves the output
   files were *committed* after the method. It does not prove the script was
   first *run* after the method was committed; no committed file could. The
   two pushes are 2 minutes 39 seconds apart, and the run itself takes 71 to
   75 seconds, which leaves about a minute and a half to read the output and
   write a 241-line findings document. That is possible for a session writing
   quickly. It is also what it would look like if the findings had been
   drafted before the method commit. This session cannot tell the two apart
   and does not claim either. Three things limit what turns on it: part (a)
   cannot fail on a correctly built pair, whenever it is run; part (b) has no
   pass line, and the findings record the session's own expectation for the
   mixed model as wrong, which is not what a prediction written after the
   fact looks like; part (c) is not a result. The findings' sentence "it ran
   as committed, first time" is the writing session's word and is recorded
   here as not checkable.

## 3. The re-run

4. **MEASURED. Run again from the committed code, the outputs are identical
   byte for byte.** The five committed output files were copied aside. The
   script was run from this branch with the project's Python (torch 2.12.1,
   scikit-learn 1.9.0, numpy 2.5.0, the versions the findings name), in 73
   seconds. `part_a.json`, `part_b.json`, `part_c_NOT_A_RESULT.json` and
   `table.md` are byte-identical to the committed copies; git reports no
   change. What the run printed is identical to the committed `stdout.txt`
   except the last line, the timing (71 seconds then, 73 now). This session's
   copy of what it printed is `rerun_stdout.txt` in the scripts folder.
5. **MEASURED. Every figure in the findings' tables is in the output files.**
   The findings' part (a) table (twelve rows) and part (b) table (86 cells,
   each a whole-state count and a piece count) were compared by script
   against `part_a.json` and `part_b.json`: all match. The figures in the
   findings' running text were checked by hand against the same files and all
   match: the mixed model's piece reaches 144 of 180 at 4, 4 and 7 of its ten
   named positions on seeds 0, 1 and 2 (so it misses at 6, 6 and 3, "three to
   six"); the entangled model's seed 2 is below 144 at all ten, from 30 to
   139; the free model's piece is between 11 and 36 away from the two
   first-token figures; the whole state is right on 149 to 180 at every other
   position of every multi-position site on the built models; part (c)'s site
   set, 92 and 95 of 180, and the shares 0.0012, 0.0063 and 0.0962.

## 4. Part (a), the too-early-position control: the code against the method and the ruling

6. **MEASURED. The code does what section 3 of the method says, step for
   step.** The model file's fingerprint is checked first (`check_sha`); the
   800 pairs are the re-run's (seed 777); the layers come from each model's
   `primary` site set in the re-run's summary; the positions are those before
   the earlier of the two twins' first own turns; the transplant goes through
   the project's own function (`repairs.run`); the pass line is
   `torch.equal` on the outputs; the donor-value share, the no-transplant
   share, the number of changed actions and the largest difference are
   reported beside it; the null transplant and the identity of the twins'
   states are reported as supporting figures. This is what ruling 2 asked for
   in its items 1, 2 and 5: positions before both first own turns, the
   outputs themselves compared as the null transplant compares them, the two
   shares side by side, run method first.
7. **MEASURED, with an ARGUED note. "The model's outputs" means its scores at
   its two action positions.** The model returns, for each of the 800 pairs,
   its scores over the 46 words at two positions only (the output's shape is
   800 by 2 by 46). That is what "bit-identical" compares, and it is also
   what the null transplant has always compared, so the code matches the
   ruling's "as the null transplant does". **ARGUED:** version 4 of the
   proposal should say "outputs at the two action positions" rather than
   "outputs", so a reader does not take it to cover every position.
8. **MEASURED. The same thing by separately written code.** This session's
   own script (`independent_check.py`, which does not use the run's script or
   the project's transplant function) found, on all twelve models: the twins'
   words are identical at every position, and their "this turn is yours"
   signal is identical at every position before both first own turns; their
   internal states there are identical at all five layers, not only at the
   layer the re-run nominated; a transplant written from scratch leaves the
   outputs bit-identical; and the donor-value shares equal the committed
   ones. The positions per pair are 1 at fewest, 5.2 on average and 21 at
   most, as the findings say, and the donor's first own turn comes first in
   0.5088 of pairs, as the ruling quotes. (One share prints as 0.0487 here
   and 0.0488 in the run. It is the same number, 39 of 800, rounded two
   ways.)
9. **MEASURED. The test is not empty.** A control that "changes nothing"
   would also pass if the transplant quietly wrote nothing. So this session
   repeated the transplant at the same positions with random noise added to
   the donor's state. The outputs then change on all twelve models (the
   largest change in any output number is between 0.6 and 4.6), and on seven
   of the twelve one or more chosen actions change. The transplant does write
   at those positions; it changes nothing in the real control because what it
   writes is what was already there.
10. **ARGUED. Agreed with the findings on what this control is.** It is a
    known-answer test of the pairing and the code. It would fail if the pairs
    were built wrong or the transplant code wrote in the wrong place, and it
    says nothing about any model. The findings say so plainly, and version 4
    should describe it that way.

## 5. Part (b), the piece's accuracy at the other positions: the code against the method and the ruling

11. **MEASURED. The per-position figures reproduce by separate code; the
    figure on the average moves by one episode depending on how the same
    average is added up.** This session recomputed all 86 cells with its own
    indexing. Every per-position cell and every action-position cell equals
    the committed figure. Of the eight figures taken on the average over the
    other positions, five are equal and three differ by one episode in 180:
    the free model's seed 0 whole state (90 here, 91 committed), its seed 2
    whole state (74 here, 73 committed), and the mixed model's seed 0 piece
    (164 here, 163 committed). The two computations take the same average of
    the same numbers in a different order of addition; the tiny differences
    in the last decimal places are enough to move one borderline episode.
    Adding up in double precision gives 92 and 24 for the free model's seed
    0. **ARGUED:** nothing turns on it today: there is no pass line and none
    of these is near 144. But the registered table will print this figure, so
    version 4 should either say it is good to an episode or two, or fix the
    arithmetic (for example, average in double precision). The script's own
    figure is exactly reproducible, as finding 4 shows; the looseness is
    between two honest ways of computing it, not between two runs.
12. **MEASURED. The code does what section 4 of the method says.** The piece
    is built by the project's function from the committed read at the site's
    layer, at the size the re-run chose; the count is the re-run's own
    `correct_count` (a fresh read fitted on the first 420 development
    episodes, scored on the last 180) with only the position changed; the
    whole state's count is printed beside the piece's; the average excludes
    the action position; the action-position figure is compared with the
    re-run's and matches on all twelve (stop S3). This is what ruling 3
    asked for: the column filled for the twelve toy models, in the same run
    as the control, with no pass line.
13. **MEASURED. The ten named positions are what the method says they are.**
    On all 600 development episodes: the first token of the model's first own
    turn is its own marker word; the fourth is a value word; the second and
    fifth are fixed words. The five positions before the action are the
    action turn's own tokens (four fixed words and one that varies). The
    model's "this turn is yours" signal is on at all ten. The shortest span
    from first own turn to action is 16 positions, so the two groups of five
    never overlap. The findings' reading of the low figures at the fourth
    token ("the value word") is therefore right about what that token is.
14. **MEASURED. How much of a span the ten positions cover.** A span runs 16
    to 53 positions, 39.2 on average, so the ten named positions are about a
    quarter of the other positions. The rest is seen only through the
    average. The method and the findings both say this; the proportion is
    added here because the evening ruling registers it (finding 19).

    *A slip the findings already own:* the method predicted "about 71" for
    the free model's seed 1 at the first token of its first own turn. That
    model's site is the action position and the three before it, so it has no
    such figure. The findings say so. Checked against `part_b.json`: correct.

## 6. Part (c), the other-agent control's code path: the code against the method and the ruling

15. **MEASURED, with an ARGUED note.** The code calls the re-run's own
    function for the control with the same arguments the re-run gave it
    (compared line against line: `rerun_controls.py` line 333 and the short
    run's `part_c`), sets the piece's accuracy floor to zero for that one
    call and restores it afterwards whatever happens. Nothing else is
    switched off. In the re-run itself the same function returned no verdict
    on this model for exactly one reason, that no piece reached four fifths;
    with the floor off it ran to the end and returned the site set and the
    three shares. The pass-or-fail label is removed from the output file, as
    the method said. The output file and the findings both carry "NOT A
    RESULT" at the top. This is what ruling 1, item 4 asked for.
    **ARGUED:** the findings say "every line of the other-agent control's
    code has been executed once". That is true only when the re-run is
    counted with this run. The function has three early exits, and this call
    took none of them. All three were taken in the re-run (MEASURED, from its
    summary file: "not applicable" on the six separable and mixed models,
    "has not learned the other-agent condition" on five, and the floor on the
    free model's seed 0). What this run adds is the part after the floor,
    which had never run. Version 4 should say it that way: the part of the
    code after the floor has now run once.
16. **ARGUED. Dropping the label was right.** Had it been kept it would have
    read "pass" (0.0012 against 0.0063 plus the withdrawn tolerance), on a
    piece that is right about the named agent on 92 of 180. A reader skimming
    the file would have taken that for a result.

## 7. Against the ruling as a whole

17. **MEASURED.** The ruling asked for three things in one short run before
    the registration review: the redefined control as a pre-stated quantity,
    the new column for the twelve toy models, and the other-agent control's
    code path once on the free model's seed 0 with the floor off, labelled as
    a test of the code. All three are in the run and the outputs, and nothing
    else is. The run edits no proposal, ruling or registered text (the two
    commits touch only the method, the script, the findings and the output
    folder).
18. **ARGUED. One condition this session cannot check from committed files:**
    the ruling says the run is made "by a session that did not write the
    diagnostic". The method and findings say so of themselves, and the run
    sits on its own branch and pull request, separate from the pull request
    that carried the diagnostic. That is consistent with the claim and is not
    proof of it.

## 8. The record of John's evening ruling

The record (`docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`)
quotes John as ruling in the words **"Yes, satisfactory and weaker than R1;
print both figures"**, and says the choices are his and none of the wording
is. This session cannot check the quotation itself; it has no source for his
words but the record. What follows checks the record against those words.

19. **ARGUED. No less, and no more except in one narrow place.**

    | What the record says was ruled | Against his words |
    |---|---|
    | 1.1 The fifth outcome is satisfactory | His words |
    | 1.2 It is stated as weaker than R1 | His words |
    | 1.3 This confirms the morning's record "on its merits", and it no longer rests on the general agreement | The record's own description, and a fair one: the check had asked him to confirm or overturn exactly this, and he answered it by name |
    | 1.4 The roadmap's first note stands and gains a second | A consequence, not a ruling; done (finding 21) |
    | 2.1 The registered table prints both figures | His words |
    | 2.2 Neither has a pass line | Not in his words, and not new: it repeats item 2 of ruling 3 of that afternoon, which already said the column has no pass line |
    | 2.3 How each is computed is as the short run's method states it: a fresh read fitted at each position; for a span, the five tokens of the first own turn and the five before the action one by one, the rest through the average | **More than his words, by implication only** |

    On 2.3: the method said of its own way of computing the figure,
    "everything in this section about how is this session's reading, and
    John's to overturn", and listed three other readings it had not taken.
    The findings then put one question to John: per position, the average, or
    both. "Print both figures" answers that question. It is fair to read it
    as accepting the two figures as they were computed, since those were the
    only two figures in front of him. But the record sets down the fresh read,
    the ten positions and the uncovered middle as ruled, without saying that
    this part rests on implication, and those were the choices the method had
    marked as his to overturn. Findings 11 and 14 bear on it: the average is
    good to an episode or two, and the ten positions are about a quarter of a
    span. **Recommendation:** nothing is wrong enough to reopen. Either John
    says in a sentence that the computation in section 4 of the method is
    what he means, or version 4 of the proposal sets the computation out in
    full so that the registration review and his ruling on the registration
    cover it. Until one of those, item 2.3 should be read as "the session's
    reading, not objected to". This session has not edited the record.

    *Dated note, 2026-10-03, late evening, after this document was filed:
    John was asked and answered in the words "Yes, section 4 of the method is
    what I meant". Item 2.3 now rests on his own words. This session added a
    dated note saying so beside item 3 of the record and changed nothing else
    in it. The finding above is left as written.*
20. **MEASURED. The record's cautions are accurate.** It says neither source
    document had been checked by a second session, or merged, when John
    ruled. The record was committed at 01:28:13 UTC; the three pull requests
    were merged between 01:29:13 and 01:29:32 UTC; this document is the first
    check of the short run. The record also says it does not edit the
    proposal, registered text, protocol text or any earlier ruling file: the
    commit that carries it changes five files, none of them one of those.
    One more fact from the same record, stated without a judgement on it: the
    findings were pushed at 01:24:51 UTC and the record of the ruling was
    committed at 01:28:13 UTC, a little over three minutes later.

## 9. The dated note in the December-result roadmap

21. **MEASURED. The note is right and nothing else in the roadmap moved.**
    The commit adds six lines to `docs/december-result-roadmap-2026-09-20.md`
    (the note at lines 94 to 98 and a blank line) and removes none. The outcome table and the first dated
    note above are left as written. The second note says that "satisfactory"
    was first recorded from a general "Agreed on all" to a question the
    packet had put as open, and that John confirmed it that evening in his
    own words, "Yes, satisfactory and weaker than R1", and points to the
    ruling file. The quotation is the first half of the words the record
    gives, exact; the file it points to exists at that path. It leaves out
    "print both figures", correctly: that half is about a reporting table and
    not about the roadmap's outcomes. The caveat that the check of the ruling
    packets found missing from the first note (that the "satisfactory" half
    had been swept in by a general agreement) is now on the page beside it.

## 10. What should happen next

1. **For John, optional, one sentence:** that the way the two figures are
   computed (section 4 of the short run's method) is what "print both
   figures" means. If he would rather leave it to the registration review,
   that works too (finding 19).
2. **For whoever writes version 4 of the proposal:**
   - describe the redefined too-early-position control as a known-answer test
     of the pairing and the code, comparing the outputs at the two action
     positions (findings 7 and 10);
   - set out in full how the new column's two figures are computed, and
     either say the figure on the average is good to an episode or two or fix
     the arithmetic so it does not depend on the order of addition
     (findings 11 and 19);
   - say that the part of the other-agent control's code after the floor has
     now run once, which is what this run added (finding 15);
   - say that the piece's four fifths is established at the action position
     only, as the findings already recommend.
3. **Nothing here blocks version 4.** No figure is wrong, no stop was missed,
   and no reading changes.

## 11. What this check does not do

It does not re-run the controls re-run, train any model, or edit the
proposal, any ruling, the method, the findings or the outputs. It was written
by one session and is itself open to check. Its branch is not merged by this
session.

## 12. Files

- `2026-10-03-short-prestated-run-check-scripts/independent_check.py`: this
  session's separately written check of parts (a), (b) and (c).
- `2026-10-03-short-prestated-run-check-scripts/independent_check_output.txt`:
  what it printed.
- `2026-10-03-short-prestated-run-check-scripts/rerun_stdout.txt`: what the
  run's own script printed when run again by this session.
