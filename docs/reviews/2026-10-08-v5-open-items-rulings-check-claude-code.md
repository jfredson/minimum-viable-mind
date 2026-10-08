# Check of the branch that records John's answers to version 5's open items (2026-10-08)

*Written 2026-10-08 (Thursday night, Pacific) by a Claude Code session that
wrote none of the work checked. Laptop only; $0. The work checked is the
branch `v5-open-items-rulings-2026-10-08`, pull request 137 against main, one
commit (`31c6931`) on top of main at `9e9daa3`. It records John's answers to
the open items of version 5 of the registration text
(`docs/successor-experiment-proposal-2026-10-07-v5.md`, section 21) and
writes them into that text.*

*John's words in the chat, which this session cannot see, are taken as the
caller gave them: to a packet of eleven recommendations, "Agreed on all."; to
the choice among three drafted wordings for the confirmation file, "1". The
packet was version 5's own section 21 recommendations, with item 3's eighth
term renamed "instrument returned no reading on the separable mechanism",
item 9's middle change (storing arm M's per-step copy once) declined unless
John asks, and item 10 updated to say the fifteen branches had already landed
(pull request 136) and that the registered commit is named after the code
changes of items 7 and 9.*

## Verdict

**Not ready to merge, by a small margin.** The two rulings files are faithful
to section 21 and to John's words, record authorship as mixed, and do not
present the confirmation as a ruling first made today. Every number in the
diff is unchanged except the new iteration limit of 10,000, which is the
ruling itself. The site data validates. But three things need fixing before
merge: the stop list's own definition of the early stop (stop S4b) still
names only the stirred-in and half-and-half models, so the one change of rule
this branch makes is missing from the place that defines it; section 9's
table of registered numbers still says the training recipe is "not ruled
(open item 5)" and the alarm has "no rulings file (open item 2)"; and the
confirmation file attributes to the method note a condition (continue only if
the built route holds) that the method note does not record, then says it
adds nothing the method notes did not report.

## How it was checked

```
git fetch origin
git log --oneline origin/main..origin/v5-open-items-rulings-2026-10-08
  31c6931 Record John's answers to the eleven open items of registration text version 5, and write them in
git diff --stat origin/main...origin/v5-open-items-rulings-2026-10-08
  STATUS.md                                          |  46 ++++++
  data/project.toml                                  |  30 +++-
  data/roadmap.toml                                  |   4 +-
  .../2026-10-08-flat-models-ruling-confirmed.md     |  76 ++++++++++
  docs/rulings/2026-10-08-v5-open-items-rulings.md   |  51 +++++++
  .../successor-experiment-proposal-2026-10-07-v5.md | 163 ++++++++++++++-------
  6 files changed, 314 insertions(+), 56 deletions(-)
```

Both versions of the registration text were written out
(`git show origin/main:docs/successor-experiment-proposal-2026-10-07-v5.md > v5old.md`,
the same from the branch to `v5new.md`) and every grep below runs on
`v5new.md`, the branch's copy.

## Must-fix

### M1. The early stop's own definition (stop S4b, section 11's stop list) does not carry arm T

The branch's one change of rule is that a failure of the hand-set model's
rerun (arm T) now also stops experiment C. It is written into section 5.6 and
into step 4b of section 11, but not into the definition of stop S4b in the
list of stops, which still names only the other two built models:

```
grep -n "stirred-in model or the half-and-half\|stirred-in model and the half-and-half" v5new.md
1493:ownership route (the stirred-in model and the half-and-half model) or do not
3579:  (the stirred-in model or the half-and-half model fails the in-use check at
```

Line 3576 onward reads: "**S4b** ... The verification of the repair fails:
the rerun built models at 10 million parameters do not hold their built-in
ownership route (the stirred-in model or the half-and-half model fails the
in-use check at the bar section 5.6 fixes) or do not do the task". A reader
who goes to the stop list, which is where a stop is defined, finds arm T
absent. Line 1493 is the 2026-10-07 ruling's own sentence and can stay, since
the added sentence after it (line 1500) carries the change; line 3579 is the
definition and needs arm T added, citing open item 6 as ruled 2026-10-08.
The branch's change note says "sections 5.6 and 11 (step 4b) carry arm T's
stop", which is accurate but leaves the stop list behind.

### M2. Section 9's table of registered numbers still says two items are unruled

```
grep -n -i "open item" v5new.md | grep -v "2026-10-08" | cut -c1-12
...
3084:| The t
3085:| The s
...
```

Line 3084 (section 9, "The numbers, now set"), the training recipe row, ends:
"`experiments/08-successor-degree/src/train_successor.py` at `53ae82c`;
**not ruled** (open item 5)". Line 3085, the spending alarm's cadence row,
ends: "reported ruled 2026-10-06 in `docs/2026-10-06-tripwire-fixes-method.md`,
section 1 ...; no rulings file (open item 2)". Both are now false: item 5 was
ruled 2026-10-08 and item 2 is closed by the confirmation file. Section 9 is
the table a reader uses to see what is registered, so these two rows matter
more than prose elsewhere. The branch's change note says each open-item
marker "in the body" was replaced; these were not bracketed markers, which is
likely why they were missed.

### M3. The confirmation file reports one condition the method note does not record, and then says it adds nothing

In `docs/rulings/2026-10-08-flat-models-ruling-confirmed.md`, under the
heading "On the two built models (the packet's page 1), as recorded in
`docs/2026-10-06-sharpness-fix-inuse-check-method.md`, 'What John ruled'",
the third bullet says the condition for going on, "continue if the decoy test
is not fooled", "became 'continue only if the built route is shown to hold in
those reruns' (the packet, page 1, 'Page 12')". The method note does not say
that:

```
grep -n -i "page 12\|decoy test is not fooled\|shown to hold\|continue only" \
  docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md \
  docs/2026-10-06-sharpness-fix-inuse-check-method.md \
  docs/2026-10-06-tripwire-fixes-method.md \
  docs/2026-10-06-tripwire-fixes-recheck-method.md \
  docs/2026-10-06-sharpness-fix-inuse-check-findings.md
docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md:66:**Page 12 (continue or stop).** Your words were "decide after the decoy test,
docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md:71:**changes the condition you endorsed**: continue only if the built route is
docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md:72:shown to hold in the 10-million-parameter reruns before registration (evidence
docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md:129:and the one-seed limit added (6); page 12 states your words and the decoy
```

Only the proposal packet has it, as a proposal. No method note records John
ruling it. The file then closes with "It adds nothing the method notes did
not already report", which this bullet contradicts. John's chosen sentence
confirms the rulings "as the method notes record them: option 1(b) plus
option 4 on the flat models, the four alarm fixes, and the three follow-up
alarm rulings"; the continue condition is not in that list. The condition is
in substance ruled elsewhere, as the stop condition John added on 2026-10-07
("Yes, add the stop condition to decision 3", stop S4b), so the fix is to
take it out of this bullet, or move it below as a plain note that the packet
proposed it and the 2026-10-07 ruling's stop condition is what rules it. A
rulings file should not widen what John's words confirmed.

Everything else in that file checks against its sources:

- **Option 1(b) and option 4, and the three reruns approved after the code
  change and its check:** match `docs/2026-10-06-sharpness-fix-inuse-check-method.md`
  lines 11 to 28 ("What John ruled") nearly word for word.
- **The four alarm fixes:** match `docs/2026-10-06-tripwire-fixes-method.md`
  section 1, items 1 to 4 (lines 19 to 36), with the same meaning.
- **The three follow-up alarm rulings:** match
  `docs/2026-10-06-tripwire-fixes-recheck-method.md` step 3 (lines 27 to 30):
  "bills below 0.90 of life are 'cannot be checked yet'; the 3-hour operator
  rule is written where an operator reads it; a rise in the balance restarts
  the in-flight comparison, is logged, and does not trip."
- **"John's own words of 2026-10-06 are in no rulings file on the main
  line":** holds. `grep -rln "1(b)" docs/rulings/` on main returns only the
  proposal packet.
- **Authorship and dating:** the header says "Authorship: **mixed**" and
  "This file is dated today and **confirms** decisions first made on
  2026-10-06; it is not a ruling first made today." John's chosen sentence is
  quoted exactly as given.

## Should-fix

### S1. Other stale sentences in version 5 still describe the open items or the merges as pending

```
sed -n 3376,3380p v5new.md     (section 10, "What happens next")
  session that did not write it; the open items of section 21 go to John; the
  closure check of RT-237 runs on this text; the branches of section 16 reach
  the main line; John commits the registration.
sed -n 4203,4205p v5new.md     (weakness W18, an unused differently coded representation)
  ... A ruled test
  of the differently coded decoy, about an hour on the laptop at $0, is open
  item 8.
grep -c "unmerged:" v5new.md
  10
```

- Section 10's "What happens next" still says the open items "go to John"
  and the branches "reach the main line"; both are done.
- Weakness W18 ends "is open item 8" with no note that item 8 is ruled (run
  before the registration commit, or before step 5b with W18 named).
- The source table at the top still marks ten records "**unmerged:**",
  including the row this branch edited (the flat-models packet, line 83) and
  the sharpness row, which also still says "**owed its check**" although
  pull request 135 checked it and pull request 136 merged it. The header's
  new note says item (4), the merges, is done; the table contradicts it.
  This staleness came in with pull request 136, not this branch, but this
  branch edited one of those rows and kept "unmerged".
- "What this version does not do" (line 5609 onward) still says "It does not
  rule any of the twelve open items" and "with everything ruled by
  2026-10-07 written in". Defensible as a description of the version as
  drafted, but a one-line dated note would stop a reader taking it as current.

### S2. The site's step N42 says two reporting changes "are made"; they are ruled, and one is owed code

`data/project.toml`, step N42, `teaches`: "Two of three reporting changes are
made." The two are reporting arm T's row-choice split (already in the
reporting table) and the summary saying "gate not decidable on one seed",
which is a code change still owed (the rulings file's own "What is now owed"
says so, as does step N43). "Two of three reporting changes are ruled in" or
"accepted" would be accurate.

### S3. The rulings file says two packet items were "updated against the main line", naming items 10 and 12; the caller's account names items 3, 9 and 10 as the ones that differed

`docs/rulings/2026-10-08-v5-open-items-rulings.md`, header: "with two updated
against the main line as it stood that evening (items 10 and 12 below)". As
the caller describes the packet, item 10 was updated, item 3 carried the
renamed eighth term, and item 9 declined the middle change. Item 12's text
(the ledger has no rows from entry 230 on) matches section 21's own
recommendation; it is checkable that it is still true
(`grep -o "RT-[0-9]*" experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md | sort -t- -k2 -n -u | tail -1`
gives `RT-211`), but it is not an update. Not wrong in substance; worth a
plain sentence saying which items differed from section 21's text and how,
since the body of the table already shows the item 3 and item 9 choices.

### S4. Roadmap goal W3.2 could note its partial progress

`data/roadmap.toml` goal W3.2 ("Version 5 checked ..., the fifteen branches
merged, and the registration committed") stays `planned`, although two of its
three parts are done (pull requests 130, 132 and 136). Not this branch's
doing, and leaving it planned until the commit is defensible; a `note` would
make the roadmap page match STATUS.

## What checks out

**The rulings file against section 21.** Each row of the table in
`docs/rulings/2026-10-08-v5-open-items-rulings.md` was read against section
21, items 2 to 12 (`sed -n 5515,5605p v5new.md`):

| Item | Section 21 recommended | Rulings file says | Match |
|---|---|---|---|
| 2 | a dated rulings file with John's words, authorship mixed | the confirmation file, in John's chosen wording | yes |
| 3 | adopt the drafted words; names "instrument returned no reading on the separable mechanism" as the alternative to the weakest one | adopted, eighth term renamed to that alternative | yes, as the packet put it |
| 4 | keep the scope phrases | kept, including for the eighth term | yes |
| 5 | confirm the recipe; name arm T's lookup damage | confirmed; damage stays named | yes |
| 6 | confirm arm T's failure stops C | stops C at S4b | yes |
| 7 | raise the limit (e.g. 10,000) with the 1,980 change, re-run page 4, quote figures | 10,000, re-run, checked, quoted, before commit | yes (adds "checked", consistent with the pairing rule) |
| 8 | ruled test before commit, or W18 named and run before step 5b | same | yes |
| 9 | yes to first and third; second only if John wants arm M cheaper | same | yes |
| 10 | merge, then name the main-line commit | branches merged (pull request 136); code changes of 7 and 9 land; then name | yes, as the packet updated it |
| 11 | confirm the derived launcher | confirmed | yes |
| 12 | write the ledger rows before commit | same, plus checked by another session | yes |

John's words are quoted exactly ("Agreed on all.", "1"); authorship is
"mixed" in the header of both files, in section 15 entries 33, 34 and 37 of
version 5, in STATUS and in step N42. The packet-number column (packet 1 to
11 against version 5's 2 to 12) cannot be checked from the record, since the
packet itself lives only in the chat; it is consistent with itself.

**No figure, bar or stop changed other than arm T's.** Every number on a
removed line and every number on an added line of the version 5 diff were
compared:

```
diff v5old.md v5new.md > d.txt
grep '^<' d.txt | grep -oE '[0-9][0-9.,$]*' | sort | uniq > old_nums
grep '^>' d.txt | grep -oE '[0-9][0-9.,$]*' | sort | uniq > new_nums
comm -23 old_nums new_nums   ->  1,980 11 21, 3,000 5.6. 6
comm -13 old_nums new_nums   ->  08 08, 08. 1,980, 10, 10,000 11, 12, 12.4, 12.5 12.5, 130 132 136 136. 15. 16, 17 18 20 21. 3, 3,000. 33 34 37 37. 4, 5, 5.1, 5.5, 5.6 5.6, 6, 7, 7.2, 8,
```

The only differences are punctuation, section and pull request numbers, item
numbers, and 10,000, the ruled new iteration limit, written as a change still
owed ("until then the frozen code still fits on 420 of 600 at 3,000"). The
in-use check's bars (0.9, 0.5), the money ($1.14, $1.47) and every measured
figure are untouched.

**No stale open-item marker; the eighth term's old words only as history.**

```
grep -n "OPEN ITEM" v5new.md
61:records John's answer. A passage marked **[OPEN ITEM n for John: ...]** is
5676:this text nor its checks: each **[OPEN ITEM n]** marker in the body is
grep -n "not validated" v5new.md
395:| **The eighth term** (new, page 5) | **instrument returned no reading on the separable mechanism** | metric not validated | ...
5530:   the words; "instrument not validated" for the eighth term is the weakest
5635:2. The scope rule of section 3 now names "instrument not validated" too, so
```

Line 61 explains the marking convention and line 5676 is the change note;
line 395's "metric not validated" is version 4's name in the old-name column;
lines 5530 and 5635 are section 21's original text and an earlier change
note. The scope rule (line 400) now names "returned no reading". No current
use of "instrument not validated" remains. The two non-marker leftovers are
M2 above.

**STATUS.md's new top entry.** Accurate against the record: the twelve items,
the first ruled earlier the same day (`docs/rulings/2026-10-08-verification-bar-ruling.md`,
pull request 126); John's two answers; the rename and the reason; the arm T
change; the list of what was written in (except that the stop list, M1, and
section 9, M2, were not); what is owed before the commit. "Laptop only;
nothing rented; $0" is consistent with the diff (no code, no ledger rows).
The claim that the red-team ledger has no rows from entry 230 on holds (the
last row is RT-211).

**`data/project.toml`.** The `where_we_are` paragraph's claims check: the
site live and publishing on every merge (STATUS, 2026-10-08 addendum, line
84 on main); the verification bar at 0.9 and 0.5 (pull request 126); the
restatement adopted (pull requests 127 and 128); version 5 checked and its
fixes re-checked (pull requests 130 and 132); the fifteen branches on the
main line (pull request 136); $229.62 of $450 unchanged. Step N41's new
`when` is accurate and points to N43 and to N39, the closure check of the
free model's gate, which exists. N42 is accurate apart from S2. N43 lists the
owed work correctly. The top timeline row is accurate.

**`data/roadmap.toml`.** W3.1 marked done with a note citing the rulings
file: accurate. W3.6 marked done, citing pull request 127 and
`docs/rulings/2026-10-08-december-result-restatement-rulings.md`, which
exists on main: accurate.

**The site check passes.**

```
git checkout -q origin/v5-open-items-rulings-2026-10-08
python3 scripts/export_site.py --check; echo "exit=$?"
export_site: data/project.toml is valid (8 stages, 9 questions, 13 ideas, 24 findings, 43 next steps, 48 timeline rows)
export_site: data/roadmap.toml is valid (13 weekends, 45 goals, 4 milestones, 5 extensions)
exit=0
```

**Pull request numbers cited.** `gh pr list --state all --limit 15` shows 126
(verification bar ruling), 127 (restatement proposal), 128 (restatement
rulings), 130 (check of version 5), 132 (re-check of its fixes), 135 (check
of the sharpness branch) and 136 (the fifteen branches landed) all merged
into main, and 137 open against main.

## Claimed done that is not, or cannot be checked

- **Claimed in the change note:** "each [OPEN ITEM n] marker in the body is
  replaced". True of the bracketed markers; two unbracketed references in
  section 9 were left (M2).
- **Claimed in the change note and STATUS:** arm T's stop is carried in
  "sections 5.6 and 11 (step 4b)". True, but the stop list's definition of
  S4b was not changed (M1).
- **Cannot be checked:** the packet's own text and its numbering (packet
  items 1 to 11), and the three drafted wordings John chose among. Both live
  only in the chat. The chosen wording matches the caller's account word for
  word.
- Nothing in the branch claims any code change, re-run, decoy test or ledger
  row as done; each is listed as owed in the rulings file, STATUS, N43 and
  version 5's change note.
