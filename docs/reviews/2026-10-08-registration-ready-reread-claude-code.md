# Re-read of pull request 158 (ready for the registration commit), after the re-check's fixes

*2026-10-08 (late night, Pacific). Claude Code, as the checker, in its own
worktree, filed on top of branch `check-registration-ready` (pull request 159,
the checks of pull request 158). I wrote none of what I check: not the commit
that applies the re-check, `9b755c0` on branch `registration-ready-2026-10-08`,
and not the re-check it answers
(`docs/reviews/2026-10-08-registration-ready-recheck-claude-code.md`, the
second file on pull request 159). Laptop only, $0. I fixed nothing, merged
nothing, and edited nothing on the branch under check.*

## Verdict: ready to merge

Both must-fix items are fixed and say what the files say. All seven
should-fix items are applied, and applied correctly. The ledger tally that
STATUS.md now gives for rows RT-230 to RT-282 recounts exactly. The three
edited ledger rows keep their five columns, no figure, bar, outcome term or
stopping rule changed, and the site check passes. Merge in the order the
re-check gave and STATUS.md now repeats: pull requests 157, 160, 161, 159
(with this file), then 158 last.

Two small things are left, neither blocking; see "Left over" at the end.

## What was checked, with commands and output

All in a detached checkout of `9b755c0`, the head of the branch
(`git rev-parse origin/registration-ready-2026-10-08` gives `9b755c0…`).
`git show --stat 9b755c0`: three files, STATUS.md (+13 −3), version 5 of the
registration text (+16 −7), the red-team ledger (+3 −3).

### Must-fix 1: section 6.4, item 5 against a withheld seed's row file

The new words in version 5 (from line 1839): "the per-seed row files keep
the arithmetic as a record of the computation, under `primary.reading.degree`
with `status: "valid"`, and it is never the reported figure".

Arm C seed 0 of the registered code's toy pass, a seed the summary withholds,
opened with a scratch script (not committed) that prints the row's
`primary.reading` and searches every file in the folder for the letters
"withh":

```
$ python3 -I rows.py <checkout>        # folder out-ruled-code-changes/passB-limit10000/
primary keys ['bootstrap_raw_difference', 'controls', 'described_only', 'dev_floor_clears', 'fit_floor',
              'no_transplant', 'null_at_worst_state', 'piece_elsewhere', 'reading', 'site_set', 'whole_read_at_worst_state']
primary.reading {'accuracy_ownership_only': 0.05, 'accuracy_untouched': 0.05125, 'accuracy_whole': 0.54,
                 'arm_own_accuracy': 0.54875, 'degree': 1.0025575447570334, 'floor': 'dict',
                 'raw_difference': 0.49000000000000005, 'status': 'valid', 'version1_form': 0.9074074074074074}
row_C_seed0.json mentions "withh": False      (and the same for all twelve row files)
```

Every one of the twelve row files has `primary.reading.status` "valid", the
withheld seeds included (C 0 to 2, M 0 to 2 and the rest). The figure itself
stays out of the reported files, as the sentence before says:

```
$ grep -c "1.00255" summary.json table.md
summary.json:0
table.md:0
$ grep -n "| C/0 " table.md
6:| C/0 | no verdict: the built ownership route has gone flat (construction did not hold): ... | withheld | withheld | ...
```

The field is where the text says, under the name it gives, with the status
it gives. **Fixed.** The ledger row for the reviewer's finding on this
sentence (RT-277) now says the wording was corrected again after the
re-check, and why; its "The wording now matches the code" is now true.

### Must-fix 2: STATUS.md no longer calls the end-to-end check running or owed

```
$ grep -n "^## WHERE THINGS STAND" STATUS.md | head -2
17:## WHERE THINGS STAND 2026-10-08 (late night) — the registration text is ready for John's commit
88:## WHERE THINGS STAND 2026-10-08 (night) — ...
$ grep -n -i -E "check running|owed its check|pull request 157 its check" STATUS.md
131:commit of the registered code. This branch itself is owed its check before it
347:pipeline does. It is owed its check. ...
```

Both hits are in older entries (line 88 onward), which are history. In the
newest entry, line 39 now reads "(pull request 157, checked in pull request
160)", and the sentence "This branch is owed its check before it merges, and
pull request 157 its check" is replaced by the merge order. **Fixed.**

### The should-fix items

| Item | Applied? | What I read |
|---|---|---|
| S1, section 10's heading still said thirty | Yes | Line 3185: "thirty, all committed (thirty-nine since 2026-10-08; see the note below)", one of the two wordings the re-check offered |
| S2, "seeds counted two of three" read as if the two-of-three rule were dropped | Yes, in both places | Closing change note: "seeds counted two of three without the newer rule that the same seeds pass every condition". The ledger row on the stale code comments (RT-281) says the same in its own words. Matches the code: `procedure.py` line 30's docstring still says only "two of three", while `summarise` (line 937) judges each seed on its own gate conditions and every withholding check |
| S3, STATUS.md's tally predated the reviewer's eight rows | Yes | New paragraph "Before the commit, one line for John" gives the tally with them; recounted below |
| S4, section 17's note said no cited file is off the main line | Yes | Note now ends "holds once pull requests 157, 160, 161, 159 and 158 have merged, in that order", the re-check's order |
| S5, the denominator-margin row (RT-275) did not say whose 0.4263 | Yes | "smallest denominator on a model that read 0.4863; 0.4263 on arm F seed 0, which is described and not read". Both figures are in the reviewer's script output (below) |
| S6, section 7.4 did not say the re-pinned fingerprint has met only the laptop | Yes | An italic note at lines 2775 to 2779, inside section 7.4 (heading at line 2770): built and checked on the laptop only, first met by the rented machine at step 4b, a mismatch deletes the machine before training, cost cents; cites RT-282 |
| S7, the eight dispositions are a session's, not John's | Yes | STATUS.md: "were disposed by this session, not by John ... His registration commit is not a ruling on them unless he says so" |

The denominators, from the reviewer's committed output on pull request 161:

```
$ git show origin/gate-a-fmp-v5:experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-08-successor-v5-gate-a-failure-mode-pass-scripts/failure_mode_pass_v5.out.txt | grep -n -E "0\.4263|0\.4863"
17:C/2       0.0600    0.5463  0.5525 | 0.4863  0.3940  True   | ... | reads
18:F/0       0.0587    0.4850  0.5587 | 0.4263  0.4000  True   | ... | described only
24:smallest fresh denominator among the rows that read: 0.4863 (C/2)
```

### The ledger tally, recounted

STATUS.md claims, for rows RT-230 to RT-282: checked 22, accepted 18, carried
by name 1, carried open 4, noted only 3, open 5. A scratch script (not
committed) reads every ledger row from RT-230 to RT-282, including the two
whose first cell carries a label in brackets (RT-256, the decision-procedure
finding; RT-274, the records-not-on-the-branch finding), and sorts them by
the bold closure word at the start of the last column:

```
$ python3 -I ledger.py experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md
rows found 53 missing []
{'checked': 22, 'accepted': 18, 'carried by name': 1, 'open': 5, 'carried open': 4, 'noted only': 3} total 53
```

**Right**, every number. Checked 22 is the 21 STATUS.md already gave for
RT-230 to RT-274 plus the nine-models row (RT-276). Open 5 are RT-263, RT-266, RT-267, RT-269 and
RT-273, all on the refounding proposal. Carried by name is the decoy row
(RT-247). The four carried open are RT-275, RT-278, RT-281 and RT-282; the
three noted only are RT-277, RT-279 and RT-280.

### Columns, figures and the site check

The same script prints each row's cell count: all 53 rows, the three edited
ones (RT-275, RT-277, RT-281) among them, have five cells, as the table's
header has.

Every number added or removed by the commit:

```
$ git diff -U0 9b755c0~1 9b755c0 | grep -E "^[-+][^-+]" | grep -o -E "[0-9]+(\.[0-9]+)?" | sort | uniq -c | sort -rn
```

gives only pull request numbers (157 to 161), ledger row numbers, dates,
section numbers, the tally above, the existing 11 of 800 pairs, ±0.29 and
0.4263, and the one new figure 0.4863, quoted from the reviewer's output. No
bar, outcome term, stopping rule or registered number is touched, and no file
under `experiments/08-successor-degree/src/` is in the commit.

```
$ python3 scripts/export_site.py --check
export_site: data/project.toml is valid (8 stages, 9 questions, 13 ideas, 25 findings, 43 next steps, 49 timeline rows)
export_site: data/roadmap.toml is valid (13 weekends, 45 goals, 4 milestones, 5 extensions)
exit=0
```

## Left over (neither blocks the merge)

1. **Two tallies in one STATUS.md entry.** The "Where things stand"
   paragraph still says "The ledger has no open row that bears on the
   registration (checked 21, accepted 18, carried by name 1, open 5 ...)", and
   the new paragraph below gives the count with the reviewer's eight. Both
   are true for the rows they cover, and "With them" signals the second; but
   four of the eight are carried open and bear on the registered design, so a
   reader of the first sentence alone is told less than the whole. A later
   edit could fold the two into one.
2. **The section 7.4 note sits mid-sentence.** It is inserted between the
   bold lead-in and "the frozen code in ...", so the sentence resumes in
   lower case after the italic aside. It reads, and says the right thing;
   moving it to the end of the paragraph would read more cleanly.

`data/project.toml` was not touched by the commit. That is within the repo's
rule, which asks for it when a session adds a "WHERE THINGS STAND" entry;
this commit edited an existing one, and nothing in the data file contradicts
the new lines.

## What this does not do

It edits none of the files under check, writes no ledger row, rules on
nothing and merges nothing. The two scratch scripts (`rows.py`, `ledger.py`)
stayed in the session's scratch folder; their whole job is shown by the
output above.
