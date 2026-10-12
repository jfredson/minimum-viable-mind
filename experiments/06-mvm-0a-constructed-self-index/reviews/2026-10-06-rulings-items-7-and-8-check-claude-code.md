# Check of the two rulings added to the 2026-10-06 rulings record (items 7 and 8)

Checked 2026-10-06 (Pacific) by a Claude Code session that wrote neither
addition. Read-only apart from this note.

**What was checked.** Two commits on pull request 103 (branch
`rulings-2026-10-06-gate-a-v4`):

- `5a4b45b`, item 7: the two refinements, "yes, stricter, go with the
  recommendation";
- `9fd76f4`, item 8: the training exclusion, "(a), go with the
  recommendation", plus edits to `STATUS.md` and `data/project.toml`.

They were compared word for word against John's rulings as stored in the
TimeAssembler worklog: the refinements decision (entry `f4aa2083`) and the
training-exclusion decision (entry `9fbca0db`).

## Verdict: accurate, with one small gap in the site data file

### John's words

- Item 7 quotes "yes, stricter, go with the recommendation". This matches the
  worklog exactly. The same quote appears in `STATUS.md`.
- Item 8 quotes "(a), go with the recommendation". This matches the worklog
  exactly. The same quote appears in `STATUS.md`.
- The only other quoted wording is the scope phrase "on these constructed
  systems, for this intervention procedure", option (c)'s "in a sample of 200
  steps" and the registered claim's "occurs in the training stream". All three
  match the worklog exactly.

### Nothing added that he did not rule

- Item 7: the first refinement (the "metric does not separate" outcome carries
  the scope phrase) and the second (the self-test checks the specific pairing
  that makes an episode fresh or relaxed) are both as ruled. The reason, that
  an overlap on that pairing alone would have passed the self-test as built,
  is the worklog's own reason. "Raised by the independent check of the
  decision-code work (pull request 107, checking pull request 105)" is also
  from the worklog. The record adds a cross-reference ("as 'metric validated'
  and the three new terms do"; item 2 of the follow-up). That is a correct
  pointer to earlier rulings, not a new claim. The phrase "asserts that no
  such pairing occurs in the training stream" restates the self-test John
  adopted earlier that day (item 4) with the stricter reading applied. It does
  not appear word for word in the refinements decision. It is fair, and item 8
  now says what limits it.
- Item 8: the three options are close paraphrases of the worklog. "Leave
  those pairings out outright" stands in for "exclude those pairings
  outright", a plain-language change that keeps the meaning. Only (a) is
  recorded as chosen. The owed work (change the exclusion from whole episode
  content to the marker-item-value pairing, add a self-test, commit the method
  first, re-run the self-tests, then an independent check, all before
  registration) is as ruled. "That work is being done separately, on branch
  `training-exclusion-pairing`" is a statement of fact about the work, not a
  ruling, and the record does not credit it to John.
- Both additions are stated as mixed authorship ("John was offered", "John
  chose") and are not upgraded to John's sole ruling. The worklog has
  `decidedBy: mixed` for both.

### Nothing he ruled is missing

- Refinements decision, point 1: the "metric does not separate" outcome
  (called R2 in the decision code) carries the scope phrase. Present, with the
  phrase in full.
- Refinements decision, point 2: the stricter self-test. Present.
- The worklog's "still to do, no ruling needed" items are not rulings. The
  record addition is this pull request. The new made-up case, the naming of
  the failed condition in outcome R3's sentence, and putting both refinements
  into the code are done in the re-check's head commit `d776c70`, whose
  message says "Implements John's two follow-ups".
- Training-exclusion decision: the choice, the owed work, and the note that
  the four 10-million-step development runs need no re-run are all present.

### Facts

- **The re-check at `d776c70`:** correct. The re-check commit on the check
  branch of pull request 107 (`1f519cc`) is titled "Re-check of the A2 work at
  d776c70". `d776c70` is the decision-code fix it re-checked.
- **200 sampled steps:** correct. The re-check says "A 200-step" sample and
  offers rewording to "in a sample of 200 steps". The findings note on that
  branch reports "200 sampled steps (9,600 training contents)".
- Item 7's ledger cross-references are correct. RT-250 is the outside finding
  on outcome words, page 11. RT-255 is the self-test on unseen combinations,
  item 4.
- Timing is consistent. `5a4b45b` was committed at 10:23 Pacific, the same
  minute as the refinements decision (17:23 UTC).

### Site export check

`python3 scripts/export_site.py --check` passes at `9fd76f4`. Both data files
are valid (8 stages, 31 next steps, 44 timeline rows). `data/project.toml`
parses.

### The gap: next step N30 in `data/project.toml` was not updated

`9fd76f4` adds the training-exclusion work to item 4 of the owed list in
`STATUS.md` ("Alongside it, the frozen training code changed to leave fresh
and relaxed pairings out of training outright…"). The site's structured copy
of that same step is next step N30 ("Bring the frozen decision code to the
ruled rules…"), and it was left unchanged. Its `teaches` line still covers
only the decision code. The new work appears only in the timeline row's
`teaches` text, not as owed work. `CLAUDE.md` says the data file follows
`STATUS.md` and that `[[next_steps]]` are refreshed in the same commit. The
check script cannot catch this, because the file is still valid.

**Fix:** in `data/project.toml`, next step N30, add the training work to its
`teaches` line. For example, append: "Alongside it, the frozen training code
leaves fresh and relaxed pairings out of training outright, with a self-test
asserting it, method first, then the self-tests re-run and an independent
check (branch training-exclusion-pairing)." Optionally widen the title to
"…and the training exclusion…". Then re-run the export check.

### Plain language

Both additions read plainly. Every worklog id and commit carries a label
("TimeAssembler decision entry", "the re-check … at commit"). One small point,
not an error: item 7's "(refines page 11, RT-250, and item 2 above)" uses a
ledger number with no label in that sentence. The label is in the table
further up. "The outside finding on outcome words (RT-250)" would follow the
workspace rule more closely. This is optional.

### A pre-existing check failure, not caused by these commits

`scripts/check_single_source.py` exits non-zero at `9fd76f4`. It does the same
at `380612a`, before either addition, so these commits did not cause it. It
was not part of this check.
