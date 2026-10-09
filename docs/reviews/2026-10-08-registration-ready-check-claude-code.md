# Check of pull request 158 (ready for the registration commit)

*2026-10-08 (night, Pacific). Claude Code, as the checker, on branch
`check-registration-ready`, cut from the main line at `93f4e90` (the merge of
pull request 156, the check of the decoy test). I wrote none of what I check:
not the branch under check (`registration-ready-2026-10-08`, one commit,
`c27b174`, base main), not the decoy test or its check, not pull request 157.
I cannot see the chat in which John ruled; I take his words ("Option 1") as
the ruling file gives them. Laptop only, $0. I fixed nothing, merged nothing,
and edited nothing on the branch under check.*

*Read as a registration reviewer would: this is meant to be the last change
before John's registration commit, so every claim that something is done, and
every claim that nothing else remains, was checked against the record.*

## Verdict: not ready to merge

The substance is right. The ruling file is true to the decoy findings, their
check and version 5's section 7.3; the figures written into weakness W18 (the
named weak point about a differently coded decoy) all match the findings and
the check, and the check's three corrections S1 to S3 are carried; the
registered code is correctly named and is unchanged on the main line since;
the ledger's closure of the decoy row fits the protocol's rule for a serious
finding, and its count is right; the site data validates. Two things stop the
merge, both small to fix:

1. W18's new paragraph says the opposite of what happened in one word (control
   1 "held", where the findings say it failed).
2. The branch says, in its STATUS heading, in the site data and in version 5's
   change note, that nothing waits on any session and only John's commit
   remains. On the record two things still do: the check of the end-to-end
   re-run that ruling 3 asks for (pull request 157's check), and the
   failure-mode pass that version 5's own section 17 says is "still owed" by
   the reviewer.

## Must-fix

**M1. W18 says control 1 "held"; it failed.** Version 5 on the branch, line
4276: "At four times the block's size every seed returned no verdict, because
control 1 held: transplanting everything but the chosen piece moved 0.1313,
0.1638 and 0.1038 of actions against the allowance of 0.018." The findings'
table gives "no verdict (control 1 failed)" on all three seeds
(`docs/2026-10-08-decoy-w18-findings.md`, section 3), and version 5 itself
uses "hold" to mean "passed" (line 1016, "controls 1, 4 and 7 holding"; line
1562, "controls 1, 4 and 7 hold"). In the registered text a reader takes
"control 1 held" as "the control passed", which inverts the result. Replace
with "because control 1 failed" or "because control 1 withheld the reading".
The figures in the sentence are right.

**M2. "Nothing waits on any session" is not yet true, and the branch says it
in four places.** The STATUS heading ("nothing waits on any session") and its
"The one thing left is John's registration commit"; `data/project.toml`
(`where_we_are`, "What remains is John's registration commit"; next step N41,
"every piece of work they asked for done and checked the same night"; the new
timeline row, "every piece of work ... was done and checked by a second
session, and merged at his word ... the decision code was re-run end to end");
version 5's header ("What remains is John's registration commit") and its new
closing change note ("Nothing waits on any session now"). Against the record:

- **The end-to-end re-run is not yet checked or merged.** Ruling 3 of
  `docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md` asks to
  "re-run it on the final registered code ..., have the run checked, and name
  it in the registration". Pull request 157 is open, its own findings say the
  check "is owed", and STATUS's last sentence on this branch says so too
  ("pull request 157 its check"), which contradicts its own heading. Section
  7.4 cites the run as if ruling 3 were met, and the source table lists the
  run's findings under "main line" though the file is not on the main line.
- **The reviewer's failure-mode pass on version 5 is called owed by version
  5.** Section 17's "What this pass leaves open, in one place" ends "the
  reviewer's own pass, which is still owed, as the protocol says". The
  protocol (`docs/outside-review-protocol.md`, "The failure-mode pass") says
  the pass belongs to the Gate A tier 1 reviewer, "an author's run never
  stands in for the reviewer's", and a registration text "with no filed
  failure-mode pass does not reach its registration commit". The check of
  version 5 (`docs/reviews/2026-10-08-successor-v5-check-claude-code.md`,
  pull request 130, section 2.4) re-ran the author's section 17 commands; it
  does not describe itself as the tier 1 reviewer's own pass, and I found no
  other filed pass on version 5 and no ruling that the check's re-run counts.

Fix: either say, in those four places, what still stands (the check of pull
request 157 and its merge; the reviewer's failure-mode pass, or John's ruling
that the check of version 5 discharged it), or wait to write "nothing
remains" until they are done. Section 7.4 should cite the check of the
end-to-end run once it exists.

## Should-fix

**S1. W18 keeps the sentences the test has now overtaken.** The first
paragraph of W18 still says "So a separable model carrying such a decoy could
read part way to entangled, and a high reading on arm C could in principle be
of that kind. Nothing in the design excludes it." The new paragraph below it
says the design does exclude it on arm T (control 1 withholds the reading)
and that a decoy of this kind does not explain a reading near 1 at the chosen
site. The decoy findings (section 5, the wording suggestion) proposed
replacing exactly that sentence. Either rewrite the two sentences or mark the
first paragraph "as written before the test".

**S2. The reason for the ruling is not in the registered text.** The
protocol's rule for a serious finding carried rather than closed asks for
"John's ruling and reason". W18 gives the ruling; section 15, entry 39, gives
only "the alternative not taken". The reason is in the ruling file's options
(a guard for the other arms would be a new kind of control, with its own
design, code, re-run and checks before 2026-10-18, changing the registered
procedure; option 1 costs nothing and changes neither the procedure nor the
schedule). One clause in W18 or entry 39 would meet the rule as written.

**S3. Leftover "owed" and "remain" wording in version 5 that this branch
makes stale.** Each now contradicts the branch's own change note:

- line 6, the status line: "DRAFT, not yet checked" (it has been checked;
  "not yet committed as registered" is right until the commit);
- line 3353, rehearsal item R-12: "the differently coded decoy is untested as
  a ruled test", followed two lines later by "Run 2026-10-08 and checked";
- lines 3435 to 3437, section 10's "What happens next": "The closure check of
  RT-237 (the fatal finding about the free model's gate), the work the rulings
  ask for, and John's commit remain";
- lines 3491 and 3494, section 11, step 3: "(this batch)" for pull request
  153, and "that commit is named after those code changes land", now named in
  section 7.4;
- line 4703, end of section 15: "follows the check owed on this version";
- line 5271, section 17: "item 8's test with a differently coded decoy is
  still owed".

**S4. Next step N26 in `data/project.toml` was not refreshed.** It is still
"pending" with "version 5 drafted 2026-10-07 with 39 ruled changes written in
and twelve open items; owed a check". It covers the same registration as N41.
Bring it current or mark it as folded into N41.

**S5. Merge order.** The source table row and section 7.4 cite
`docs/2026-10-08-end-to-end-final-code-findings.md` and
`experiments/08-successor-degree/out-e2e-final-code/code-identity.txt`, which
exist only on pull request 157's branch. If this branch merges first, the main
line cites files it does not have, the defect header item (4) of version 5
forbids at the commit. Merge pull request 157 (after its check) first, or say
so in this pull request's description.

**S6. Two small accuracy points in W18.** "At a quarter of the size and at
equal size it was not fooled" and "at sixteen times it was withheld" join the
two ruled variants with the supplementary ones: the equal-size and
sixteen-times variants (V4 and V3) were placed "beside" and reported beside
the verdict, not part of it (findings section 4). And "the procedure's own
search reaches 0.94 to 0.997 at sites it did not choose" is on development
pairs, at sites and sizes it did not choose (the check's S1). Neither changes
a figure.

## Worth noting, not items

- The ledger's open five now include RT-266 (the first side of the refounding
  question not decidable as stated), which ruling 5 did not list among the
  refounding rows that may stand open, because it was reopened after that
  ruling. It belongs to the refounding proposal, which registers nothing, so
  the note's "no open row bears on the registration commit" holds.
- STATUS calls pull request 153 "a one-number fix to the reporting table";
  that pull request also wrote the code changes into version 5 and closed
  three ledger rows. Harmless.
- Gate A, both tiers, ran on version 4; version 5's section 11 treats that,
  with the check of version 5 and the closure check on version 5, as the
  registration review. I found no separate ruling saying a second outside
  pass is not needed on version 5. The record has always read it this way and
  John has ruled around it, so I do not raise it as an item; I note it because
  a registration reviewer would ask.

## The seven parts, one by one

**1. The ruling file** (`docs/rulings/2026-10-08-decoy-w18-ruling.md`). True to
the record. The withheld readings (0.1488, 0.2137, 0.1162), the chosen piece
"about 94 per cent" in the unused code (0.935, 0.939, 0.935), control 1
withholding every seed, and the eighth term rather than a false "entangled"
all match the findings, section 3, and the check's re-run, section 3. Its
paraphrase of version 5's section 7.3, item 1 ("on an entangled model the rest
of the state carries ownership by construction") matches the text: "the
complement carries the ownership signal by construction, since in a system
where ownership multiplies content at every layer there is no ownership-free
complement". The two options match what the findings left to John (section 5:
"whether a guard like control 1 is wanted for the other arms, is John's
call"). Authorship mixed, John's words quoted. Its account of the three
corrections matches the check's S1 to S3.

**2. W18 and R-12.** Every figure matches: control 1 at 0.1313, 0.1638,
0.1038 against 0.018; withheld 0.1488, 0.2137, 0.1162; 0.0000 on every seed
of V2 and V4; V3 withheld at 0.2788 to 0.4100 ("0.28 to 0.41"); the search's
highest 0.943 to 0.997 ("0.94 to 0.997", the check's S1); the unaltered model
"about 0.86 at 1 direction and 0.57 to 0.67 at 2" (the check's S2 gives 0.85
to 0.86 and 0.57 to 0.67); arm F's 0.1 to 0.4 marked "argued from arm T and
not measured" (the check's S3). S1, S2 and S3 are all carried. The one wrong
word is M1; the overtaken sentences are S1 above.

**3. The registered code (section 7.4).**

    $ git log -1 --format=%h -- experiments/08-successor-degree/src    # on main, 93f4e90
    6c47c56
    $ git merge-base --is-ancestor 6c47c56 origin/main && echo ancestor
    ancestor
    $ git diff --stat 6c47c56 origin/main -- experiments/08-successor-degree/src
    (nothing)
    $ git diff --stat 6c47c56 origin/registration-ready-2026-10-08 -- experiments/08-successor-degree/src
    (nothing)
    $ git diff --stat 6c47c56 origin/e2e-final-code -- experiments/08-successor-degree/src
    (nothing)

`6c47c56` is pull request 153's commit, merged at `133bbc2`. The SHA-256 of
all nine files of `experiments/08-successor-degree/src/` on the main line
(`shasum -a 256 *` in this checkout) equal the nine in pull request 157's
`code-identity.txt`, line for line. Pull request 157's findings
(`gh pr view 157`: branch `e2e-final-code`) support every claim section 7.4
makes of it: "31 cases; 0 differ from expectation or leak"; the toy summary R3
("substrate not a testbed: arm F failed its gate on learning (named-other
condition, on seeds 1 and 2)"), its `summary.json` byte for byte the committed
one; "14 checks; differ from expectation: []"; the whole-pipeline test "ran to
the end at: 10M 30M", exit 0. What section 7.4 leaves out is that ruling 3
also asks for the run to be checked (M2).

**4. Section 15, the source table, the leftovers.** Entries 38 and 39 match
the ruling files (five rulings, "As recommended"; "Option 1", authorship
mixed). The source-table row is right except that it calls pull request 157's
file "main line" (S5). All five leftovers of
`docs/reviews/2026-10-08-final-batch-recheck-claude-code.md` are fixed:
section 5.1's arm T paragraph now says the figures were fitted on 420 and are
the same at 1,800; section 9's arm M row cites the check (pull request 152);
sections 6.3 and 10 (R-4) give 1.0026 at 1,800 beside 1.0051; section 5.6
says the sharpness work was checked, citing
`docs/reviews/2026-10-08-sharpness-fix-check-claude-code.md`, which exists on
main; the 5.2 and 5.3 headings name the earlier iteration limit of 3,000.

**5. The dated note in the decoy findings.** It states S1 to S3 as the check
did, and names who added it. Right.

**6. The ledger's decoy row (RT-247) and the count.** The protocol's closure
rule: "Serious findings are closed the same way or carried as an open item
named in the registered text, with John's ruling and reason." RT-247 is
serious; it is now named in the registered text (W18, R-12, section 15 entry
39) with John's ruling. The rule fits, with S2's caveat about the reason. My
recount of the closure words of the 45 rows RT-230 to RT-274, from the
branch's ledger:

| Closure | Count | Rows |
|---|---|---|
| the claim was checked | 21 | 230, 231, 233, 234, 237, 238, 239, 240, 241, 248, 249, 250, 251, 255, 256 (the decision-procedure finding), 257, 258, 260, 268, 270, 274 |
| the argument was accepted | 18 | 232, 235, 236, 242 to 246, 252, 253, 254, 259, 261, 262, 264, 265, 271, 272 |
| carried by name in the registered text | 1 | 247 (the decoy) |
| open | 5 | 263 (the control's specification), 266 (the first side not decidable as stated), 267 (the observer side), 269 (the book's prediction), 273 (the loss conditions that cannot lose) |

So checked 21, accepted 18, carried 1, open 5, as the note says. All five open
rows belong to the refounding proposal; none is about the degree
experiment's registration. RT-237 (the fatal finding about the free model's
gate) is closed as checked with one condition carried to step 4b, as the
earlier note says.

**7. STATUS.md and `data/project.toml`.** Against the record, the pull
request numbers and what each did are right (141 and 145 the ledger rows,
checked in 143 and 148; 142 and 152 the closure check and its fired
condition; 146 the three serious findings; 151 and 152 the code changes; 153
and 154; 155 and 156; 157 with its check running; 140 and 149 with 143 and
150). John's quoted words match the ruling files. The decoy figures in STATUS
and in new finding F25 match the findings (F25 rounds the withheld readings to
0.15, 0.21, 0.12). The overclaims are M2; N26 is S4. The validator passes:

    $ git checkout --detach origin/registration-ready-2026-10-08
    $ python3 scripts/export_site.py --check
    export_site: data/project.toml is valid (8 stages, 9 questions, 13 ideas, 25 findings, 43 next steps, 49 timeline rows)
    export_site: data/roadmap.toml is valid (13 weekends, 45 goals, 4 milestones, 5 extensions)
    (exit 0)

## The question: after this and pull request 157 merge, what is left before John's commit?

Plainly: **two things beyond the commit itself, on the record as it stands.**

1. **The check of the end-to-end re-run** (pull request 157), which ruling 3
   asks for in so many words. Merging 157 is not enough; the run must be
   checked by a session that did not do it, and section 7.4 should cite that
   check. The STATUS entry says it is running.
2. **The reviewer's failure-mode pass on version 5**, which version 5's
   section 17 calls "still owed, as the protocol says", and without which the
   protocol says a registration text does not reach its commit. Either a
   session acting as the tier 1 reviewer files its own pass on version 5, or
   John rules that the check of version 5's re-run of section 17 (pull
   request 130, section 2.4) discharges it, and section 17 says so.

Then, as part of the commit itself: the status line at the head of version 5
changes from "DRAFT" to registered, and the commit records the hash `6c47c56`
as section 7.4 says.

Nothing else. The grep:

    $ git show origin/registration-ready-2026-10-08:docs/successor-experiment-proposal-2026-10-07-v5.md > v5.md
    $ grep -n -i "owed\|not yet\|before the registration commit\|OPEN ITEM" v5.md

Every hit, sorted:

- **Must happen before the commit:** line 5277 (the reviewer's own pass;
  item 2 above).
- **Stale, now done (S3):** lines 6, 3353, 3437, 3494, 4703, 5271.
- **Declared limits that the registration carries, not preconditions:**
  lines 633, 1564 and 3399 (eleven of the twelve re-reads of the toy models
  with the sharpness fixed; the text registers that the toy anchors are the
  learned-sharpness models' readings); line 5195 (the in-use check not yet run
  on a repaired checkpoint, which is step 4b, after the commit); line 2337 (no
  toy nomination has more than one layer).
- **History, done, or not about owed work:** lines 27 to 38 (the header's
  list, each marked done), 85, 86, 89, 98, 99, 101, 110, 111, 124 (source
  table), 390, 398, 409, 411, 415, 955, 961, 968, 1009, 1029, 1255, 1412,
  1414, 1432, 1472, 1525, 1671, 2617, 2655, 2772, 3134, 3135, 3261, 3432,
  3435, 3481, 3486, 3523, 3637, 3681, 3857, 3923, 4434, 4465, 4656, 4675,
  4717 (section 16: merged), 5059, 5072, 5109, 5110, 5118, 5122, 5123, 5221,
  5507, 5576, 5579, 5590 and 5639 to 5794 (section 21, kept as it stood
  before the rulings, and the ruled-in note), 5816 to 5881 (change notes).
- **"OPEN ITEM" markers:** every one in the body is ruled (line 63 and the
  note at line 5787 say so; none is left unruled).

In the ledger, no open row bears on the registration (part 6). In STATUS and
the site data, only STATUS's last sentence names anything still owed (pull
request 157's check); I found the failure-mode pass called owed nowhere but
version 5's section 17 (searched: `docs/reviews`, `docs/rulings`, STATUS).

## Commands, in order

    git fetch origin
    gh pr view 158 --json baseRefName,headRefName,title,state      # base main
    gh pr view 157 --json baseRefName,headRefName,title,state      # base main, branch e2e-final-code
    git diff --stat origin/main...origin/registration-ready-2026-10-08
    git log --oneline origin/main..origin/registration-ready-2026-10-08
    git diff origin/main...origin/registration-ready-2026-10-08 -- <each file>
    git show origin/main:docs/2026-10-08-decoy-w18-findings.md
    git show origin/main:docs/reviews/2026-10-08-decoy-w18-check-claude-code.md
    git show origin/registration-ready-2026-10-08:docs/successor-experiment-proposal-2026-10-07-v5.md > $SCRATCH/v5.md
    sed -n 2418,2470p, 3325,3360p, 4250,4300p, 3390,3500p, 4700,4725p, 5262,5282p $SCRATCH/v5.md
    git log -3 --format='%h %p %s' origin/main -- experiments/08-successor-degree/src
    git diff --stat 6c47c56 origin/main -- experiments/08-successor-degree/src
    git diff --stat 6c47c56 origin/registration-ready-2026-10-08 -- experiments/08-successor-degree/src
    git diff --stat 6c47c56 origin/e2e-final-code -- experiments/08-successor-degree/src
    git merge-base --is-ancestor 6c47c56 origin/main
    git show origin/e2e-final-code:docs/2026-10-08-end-to-end-final-code-findings.md
    (cd experiments/08-successor-degree/src && shasum -a 256 *)    # on main; compared with code-identity.txt
    cat docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md
    sed -n 292,345p and 400,440p docs/outside-review-protocol.md
    git show origin/registration-ready-2026-10-08:experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md > $SCRATCH/ledger.md
    python3 -I $SCRATCH/count.py $SCRATCH/ledger.md     # the closure-word count of part 6
    cat docs/reviews/2026-10-08-final-batch-recheck-claude-code.md
    grep -n -i "owed\|not yet\|before the registration commit\|OPEN ITEM" $SCRATCH/v5.md
    git grep -n -i "failure-mode pass\|reviewer's own" -- docs/reviews docs/rulings STATUS.md
    gh pr list --state all --limit 25
    git checkout --detach origin/registration-ready-2026-10-08
    python3 scripts/export_site.py --check
    python3 -I -c '<list next steps not done in data/project.toml>'

`$SCRATCH` is this session's scratch folder; nothing there is committed.
`count.py` reads each ledger row from RT-230 to RT-274 and tallies the bold
word at the head of its closure cell.

## What this does not do

It fixes nothing, merges nothing and spends nothing. It edits neither version
5, the ledger, STATUS, the site data nor pull request 158's or 157's branch.
