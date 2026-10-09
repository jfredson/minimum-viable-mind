# Re-check of pull request 158 (ready for the registration commit), after the reviewer's failure-mode pass

*2026-10-08 (late night, Pacific). Claude Code, as the checker, in its own
worktree cut from the main line at `93f4e90` (the merge of pull request 156,
the check of the decoy test), filed on top of branch `check-registration-ready`
(pull request 159, the first check of pull request 158). I wrote none of what I
check: not the two new commits on branch `registration-ready-2026-10-08`
(`eb6696e`, the commit of the nine retrained toy models, and `b2371a8`, the
commit that writes the night's two checks and the reviewer's pass into the
record), not the Gate A tier 1 reviewer's failure-mode pass (pull request 161,
branch `gate-a-fmp-v5`), not the end-to-end re-run (pull request 157) or its
check (pull request 160). Laptop only, $0. I fixed nothing, merged nothing,
and edited nothing on any branch under check.*

## Verdict: not ready to merge as it stands; ready once two small wording fixes land

The substance is right. The nine model files are in the commit, match the
folder's committed list of file fingerprints nine of nine, load with the
frozen code with the sharpness fixed at 4.0, and reproduce the committed
in-use figures exactly on the two models I re-ran. So the reviewer's one
serious finding (the nine retrained toy models not committed, RT-276) is
closed as its ledger row says, and this file is the check that row names. The
eight new ledger rows say what the reviewer found, with closure words the
ledger has used before. Version 5's edits cite the right files, and no
figure, bar, outcome term or stopping rule changed. The site check passes.

Two things stop the merge, both one-line wording fixes:

1. The new words in version 5's section 6.4, item 5 say the per-seed row
   files mark a withheld seed's figure as withheld. They do not: they mark it
   "valid". This re-makes the reviewer's finding about that sentence (RT-277,
   the sentence claiming a withheld figure appears nowhere) in a new form, in
   the text being registered, and the ledger row for it says the wording now
   matches the code.
2. The newest STATUS.md entry still says pull request 157's check is
   "running" and that pull request 157 is "owed its check". That check is
   filed (pull request 160), and the same paragraph says so a few lines
   earlier.

## Must-fix

**M1. Section 6.4, item 5: the row files are not marked as withheld.** The
new text (version 5 on the branch, lines 1839 to 1841) reads: "the figure the
arithmetic would have given appears nowhere in the summary file or the table
(the per-seed row files keep it, marked as the arithmetic of a seed that was
withheld; the reviewer's RT-277; ...)". The row files the registered code
writes carry the figure under `primary.reading` with `status: "valid"` and no
word of withholding; the withholding is recorded only in the summary file.

```
$ python3 -c "import json;r=json.load(open('experiments/08-successor-degree/out-ruled-code-changes/passB-limit10000/row_C_seed0.json'));p=r['primary']['reading'];print({k:p[k] for k in p if k in ('degree','status','reason','note')})"
{'degree': 1.0025575447570334, 'status': 'valid'}
$ grep -o -i '"[a-z_]*withh[a-z_]*"' experiments/08-successor-degree/out-ruled-code-changes/passB-limit10000/row_C_seed0.json
(no output)
```

That is arm C seed 0 of the registered code's toy pass, a seed its summary
withholds; the reviewer's script found the same on all nine withheld toy seeds
(`failure_mode_pass_v5.out.txt` on pull request 161, part two (d): every one
"status 'valid'"). The ledger row for the reviewer's finding (RT-277) closes
it "Noted only. The wording now matches the code", which is not yet so.
**Fix:** use the reviewer's own suggested words, or the like: "the per-seed
row files keep the arithmetic, marked 'valid', as a record of the computation;
it is never the reported figure". No code change.

**M2. STATUS.md, newest entry: two stale sentences about pull request 157's
check.** Line 39: "all 31 made-up cases on their terms (pull request 157, its
check running)". Lines 75 and 76: "This branch is owed its check before it
merges, and pull request 157 its check." The check of pull request 157 is
filed as pull request 160 (`docs/reviews/2026-10-08-end-to-end-final-code-check-claude-code.md`,
"ready to merge"), which the same entry says at lines 66 and 67. STATUS.md is
the record the site is built from and the one where the two disagree is
fixed against. **Fix:** "(pull request 157, checked in 160)"; and replace the
last sentence with "This branch's re-check is pull request 159
(`docs/reviews/2026-10-08-registration-ready-recheck-claude-code.md`)", or
drop it.

After both fixes, a reading of those lines by any session that did not write
them is enough; nothing else needs re-checking.

## Should-fix

**S1. Section 10's heading still says thirty.** "**The models every toy
result rests on: thirty, all committed.**" (line 3180) heads the paragraph
whose new note ends "rest on thirty-nine committed models". Make the heading
say thirty-nine, or "thirty, and since 2026-10-08 thirty-nine".

**S2. "Seeds counted two of three" reads as if version 5 dropped the
two-of-three rule.** The closing change note, and the ledger row on the stale
code comments (RT-281), say the docstrings describe rules the code no longer
applies, "the no-transplant rate withholding; seeds counted two of three".
Version 5 still registers two seeds of three (line 2846, "two seeds of
three"; line 3116). What the docstring lacks is the 2026-10-06 rule that the
same seeds must pass every condition (page 7 of that ruling). Say "seeds
counted two of three without the page 7 rule that the same seeds pass every
condition".

**S3. STATUS.md's ledger tally predates the reviewer's eight rows.** "The
ledger has no open row that bears on the registration (checked 21, accepted
18, carried by name 1, open 5 ...)". Four of the new rows are carried open
and do bear on the registered design: the reading's denominator margin
(RT-275), the in-use judge accepting a missing route (RT-278), the stale code
comments (RT-281) and the evaluation sets' fingerprint seen only on the laptop
(RT-282). None blocks the commit. Add "plus the reviewer's eight: one closed
by a check, four carried open, three noted".

**S4. The note heading section 17 says no cited file is off the main line.**
"the count of files off the main line, now none that this text cites". On the
branch today the repository's own citation checker finds the version citing
files that exist only on pull requests 157, 159, 160 and 161 (commands
below). It becomes true at the merge order below. Say "none once pull
requests 157, 159, 160 and 161 are merged", or leave as is and keep the merge
order.

**S5. The ledger row on the denominator margin (RT-275) quotes the smallest
denominator without saying whose.** "smallest denominator 0.4263" is arm F
seed 0, which is described and not read; among rows that read the smallest is
0.4863 (arm C seed 2), and at 10 million parameters 0.4600
(`failure_mode_pass_v5.out.txt`, failure 1). The reviewer's own glance table
and body differ the same way. Name which.

**S6. The reviewer's suggested clause for section 7.4 is not written.** The
reviewer's last worth-noting finding (RT-282) suggested that section 7.4 say
the re-pinned fingerprint of the evaluation sets has met only the laptop. It
is carried open in the ledger and not said in the registered text. Optional;
the closure rule only requires a carried item named in the text for a serious
finding.

**S7. The eight dispositions are a session's, and the reviewer's pass says
they are John's.** The ledger section header marks them "decided by: agent,
for John to overturn", which is honest. The closure rule asks for John's
ruling only for a serious finding carried open, and the one serious finding
is closed, not carried, so nothing blocks. But the reviewer's pass ends "the
dispositions of RT-275 to RT-282 are John's". Put them to him in one line
before or with the registration commit, so his commit is not read as having
ruled them.

## What was checked, with commands and output

### 1. The nine models

In a checkout of the branch at its head, `b2371a8`:

```
$ git show --stat eb6696e        # 9 files, all ckpt_{C,M,T}_fixed_seed{0,1,2}.pt, nothing else
$ git log --oneline -1 -- experiments/08-successor-degree/out-sharpness-fix/models/SHA256SUMS
644238e Toy retrain with the sharpness fixed: nine models, ...
$ cd experiments/08-successor-degree/out-sharpness-fix/models && shasum -a 256 -c SHA256SUMS
ckpt_C_fixed_seed0.pt: OK
ckpt_C_fixed_seed1.pt: OK
ckpt_C_fixed_seed2.pt: OK
ckpt_M_fixed_seed0.pt: OK
ckpt_M_fixed_seed1.pt: OK
ckpt_M_fixed_seed2.pt: OK
ckpt_T_fixed_seed0.pt: OK
ckpt_T_fixed_seed1.pt: OK
ckpt_T_fixed_seed2.pt: OK
exit=0
```

The fingerprint list was committed with the sharpness branch (`644238e`),
before the models, and `eb6696e` does not touch it, so the files were
checked against a list written before they were added.

Loaded with the frozen code's own loader (`procedure.load_model` in
`experiments/08-successor-degree/src/`, unchanged since `6c47c56`:
`git diff --stat 6c47c56 HEAD -- experiments/08-successor-degree/src` is
empty), by a scratch script that is not committed:

```
$ .venv/bin/python -I load_nine.py <worktree> C/0
T/0: arm=T own_sharpness=4.0 buffer=True learned=False fixed_at_4=True
T/1: arm=T own_sharpness=4.0 buffer=True learned=False fixed_at_4=True
T/2: arm=T own_sharpness=4.0 buffer=True learned=False fixed_at_4=True
C/0: arm=C own_sharpness=4.0 buffer=True learned=False fixed_at_4=True
C/1: arm=C own_sharpness=4.0 buffer=True learned=False fixed_at_4=True
C/2: arm=C own_sharpness=4.0 buffer=True learned=False fixed_at_4=True
M/0: arm=M own_sharpness=4.0 buffer=True learned=False fixed_at_4=True
M/1: arm=M own_sharpness=4.0 buffer=True learned=False fixed_at_4=True
M/2: arm=M own_sharpness=4.0 buffer=True learned=False fixed_at_4=True
```

Every model is the arm its name says, and its sharpness is a stored fixed
value of exactly 4.0, not a learned number, which is where the sharpness
findings (`docs/2026-10-06-sharpness-fix-inuse-check-findings.md`, section 4)
and `models.py` (`OWN_SHARPNESS = 4.0`, `_fix_sharpness`) say it is.

**The in-use figures recompute from the committed files.** The script repeats
what `tests/retrained_toy_inuse.py` does for one model (the gate's 3,000
held-out episodes, `procedure._accuracy` and `procedure.route_in_use`) and
compares with `out-sharpness-fix/retrained_inuse.json`:

```
C/0 own_correct: recomputed=1731 file=1731 match=True
C/0 other_correct: recomputed=768 file=768 match=True
C/0 sharpness: recomputed=4.0 file=4.0 match=True
C/0 weight: recomputed=0.9989947080612183 file=0.9989947080612183 match=True
C/0 state: recomputed=failed file=failed match=True
C/0 route_use: recomputed={'entangled': 0.2848064702484113} file={'entangled': 0.2848064702484113} match=True
M/1 own_correct: recomputed=2563 file=2563 match=True
M/1 other_correct: recomputed=1676 file=1676 match=True
M/1 sharpness: recomputed=4.0 file=4.0 match=True
M/1 weight: recomputed=0.9989947080612183 file=0.9989947080612183 match=True
M/1 state: recomputed=failed file=failed match=True
M/1 route_use: recomputed={'entangled_items': 0.1056081573197378, 'separable': 1.0} file={'entangled_items': 0.1056081573197378, 'separable': 1.0} match=True
```

Arm C seed 0's route use 0.285 and arm M seed 1's 0.106 are figures version 5
quotes in section 5.6 (part B after the fix). Both match to every digit on
the processor, though the models were trained on the laptop's graphics chip.

**Verdict on item 1:** matches. The ledger row for the serious finding
(RT-276) says "The nine files match ... SHA256SUMS, nine of nine, confirmed
by the check of this commit"; that is what this check found.

### 2. The ledger rows for the reviewer's eight findings

Read against the pass (`git show origin/gate-a-fmp-v5:experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-08-successor-v5-gate-a-failure-mode-pass-claude-code.md`),
its glance table and each finding's body.

| Row | Matches the finding? | Severity | Closure word fits? |
|---|---|---|---|
| RT-275, the denominator margin | Yes (11 of 800 pairs, band about ±0.29) | worth-noting, as filed | "Carried open": the ledger's own precedent for a worth-noting row ("ACCEPTED, CARRIED OPEN", RT-39 and RT-40). See S5 on 0.4263 |
| RT-276, the nine models | Yes | serious, as filed | "Closed: the claim was checked" fits the method note's rule (a committed check by a session that did not write the fix, whose output confirms it, named in the row): confirmed above |
| RT-277, the withheld figure | Yes, including "marked 'valid'" | worth-noting | "Noted only" is a precedent word (RT-43), but its sentence "The wording now matches the code" is not yet true: M1 |
| RT-278, the in-use judge | Yes | worth-noting | "Carried open", with what it waits on (step 4b's reruns) |
| RT-279, section 17's stale records | Yes, all five places | worth-noting | "Noted only", with the dated note written in |
| RT-280, best pieces | Yes; recomputed below | worth-noting | "Noted only. Corrected" |
| RT-281, the stale code comments | Yes; see S2 on "two of three" | worth-noting | "Carried open", with what closes it |
| RT-282, the fingerprint seen only on the laptop | Yes | worth-noting | "Carried open. Seen at step 4b"; see S6 |

Every disposition carries "(agent)", and the section header says the
dispositions are the drafting session's, "decided by: agent", for John to
overturn. The rows sit after RT-274 with no gap, under their own section
heading naming the source file and the commit reviewed (`d674807`); no row
above it is edited (`git show b2371a8 -- <ledger>` adds 19 lines and removes
none).

Best pieces, recomputed from the rows the reviewer named:

```
$ python3 - (reads out-dev-10m-check/row_{C,M}_seed0.json, "fits")
C best whole 41 best piece 45
M best whole 45 best piece 43
```

### 3. Version 5

`git show b2371a8 -- docs/successor-experiment-proposal-2026-10-07-v5.md`:
56 lines, eight places. Each against the pass and the end-to-end check:

| Edit | Says what the record says? |
|---|---|
| Header (line 35), section 10's "What happens next" (line 3449), section 17's "leaves open" (line 5309), closing note (line 5920): "still owed" replaced by the two filed checks, with paths and pull request numbers | Yes. Both files exist at those paths on their branches (pull requests 160 and 161) |
| Section 7.4: the end-to-end check cited | Yes. The check says every output re-ran byte-identical, "ready to merge" |
| Section 10: thirty-nine committed models | Yes (item 1); heading still thirty, S1 |
| A dated note heading section 17 | Yes: names the reviewer's pass, the verdict (nothing fatal, one serious, seven worth-noting) and the five stale places of RT-279. See S4 |
| Section 6.4, item 5 | **No**: M1 |
| Best-piece figures, sections 5.6 and 17 | Yes (recomputed above) |
| Closing note on the stale code comments | Yes in substance, a session's call labelled as such; see S2 |

**No figure, bar, term or stopping rule changed.** Every removed line in the
diff is one of the "what remains" sentences, the RT-277 sentence, the two
best-piece sentences or the end of section 7.4's paragraph that the check's
citation extends; nothing in sections 3, 6.3, 8, 11 or 12's numbers is
touched, and the frozen code is unchanged.

**Nothing in version 5 still says a check is owed, or that nothing waits,
wrongly.**

```
$ grep -n -i "still owed\|is owed\|are owed\|owed before\|check running\|still running\|nothing waits" v5.md
27:  (1) This version is owed a check ...           (the original list, each item marked done in the next sentence)
632, 1564: the other eleven re-reads are owed     (true: work for after the registration, stated as such)
5141, 5142, 5154, 5710, 5749:                     (section 17 and older change notes, covered by the dated note)
5903, 5927:                                       (history of earlier change notes)
```

What the text says remains is John's registration commit, which is so once
the merge order below is followed.

### 4. STATUS.md and the site data

```
$ python3 scripts/export_site.py --check        # on the branch at b2371a8
export_site: data/project.toml is valid (8 stages, 9 questions, 13 ideas, 25 findings, 43 next steps, 49 timeline rows)
export_site: data/roadmap.toml is valid (13 weekends, 45 goals, 4 milestones, 5 extensions)
exit=0
$ grep -n -i -E "check running|is owed its check|its check\." STATUS.md
39:terms (pull request 157, its check running). ...
75:... This branch is owed its check before it
76:merges, and pull request 157 its check.
(112 on: older entries)
```

`data/project.toml` is accurate: `where_we_are`, next step N41 and the
timeline row each say both checks are filed and what remains is John's
commit; nothing claims a check still owed. STATUS.md has M2 and S3.

### 5. The merge order

The five pull requests touch disjoint files except pull request 158
(`git diff --stat main...origin/<branch>` for each), so no order conflicts.
I merged them locally on a throwaway detached checkout of main, in the order
below, and ran the repository's citation checker on each pull request's new
files at the moment it landed:

```
after 157: check_citations --only the two end-to-end files          -> 0 files named that are not in the repository
after 160: --only the end-to-end check                              -> 0
after 161: --only the reviewer's pass                               -> 2: failure_pass_v5.py, scan_ids.py
                                                                       (the author's two scratch scripts; RT-279's note says they were never committed)
after 159: --only the first check of 158                            -> docs/rulings/2026-10-08-decoy-w18-ruling.md (arrives with 158),
                                                                       plus SCRATCH/ and count.py names of its own scratch folder
after 158: --only version 5, the ledger, STATUS.md, the check of 158 -> version 5: only the two scratch scripts above;
                                                                       ledger: docs/reviews/2026-10-08-registration-ready-recheck-claude-code.md
                                                                       (this file, which joins pull request 159 with this commit, so it is present
                                                                       once 159 is merged with it)
```

On the branch alone, before any merge, version 5 names five files that are
on no main-line commit: the end-to-end findings and its code fingerprints
(pull request 157), the end-to-end check (pull request 160), the reviewer's
pass (pull request 161) and the first check of 158 (pull request 159).

**Order: 157, then 160, then 161, then 159 (with this file), then 158 last.**
158 must be last because version 5 and the ledger cite files on all four
others. 159 and 158 cite each other (159's first check names the decoy
ruling that arrives with 158), so one of the two points briefly at a file not
yet merged; with 159 first that is a review file pointing at the change it
reviews, and the registration text never points at a missing file. 160 after
157 because the check cites the files it checked. 161 may go anywhere before
158. Pull request 158 should take M1 and M2 before it merges.

## What this does not do

It edits none of the files under check, writes no ledger row, rules on
nothing, and merges nothing. The scratch script `load_nine.py` stayed in the
session's scratch folder; its whole content is the loader call, the sharpness
print and the comparison shown above.
