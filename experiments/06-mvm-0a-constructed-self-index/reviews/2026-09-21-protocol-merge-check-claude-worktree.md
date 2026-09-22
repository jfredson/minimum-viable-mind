# Final check before merge — the ruling annotation, the thirteenth printed block, and the small corrections

*2026-09-21 (Pacific). A checking session that did not write the work under
check. Target: the branch `worktree-agent-a35a6f89b244b4e29` at the commit
`df76394`, titled "Correct the ruling's bookkeeping, illustrate failure 2's
middle limb, and close the small items", sitting on top of the commit `f3ba2f2`,
titled "Say which tests have been run, and what failure 2's route search cannot
see". Three files changed. Read only: nothing was fixed, no compute was launched,
no money was spent, nothing was pushed to the shared main line, and no pull
request was opened.*

*Written under the workspace plain-language rule
(`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30).*

**Verdict: merge. No must-fix finding.** Six things are worth noting and can all
follow afterwards. This is the fifth round of write-and-check on this work; it
found no defect that should hold the merge, and this file says so rather than
manufacturing one.

This check also discharges a debt the failure list names about itself: it says
the two newest corrections in it "were written by a fourth session and have not
themselves been checked by anyone", and that under the pairing rule they are owed
a check by a session that did not make them. This is that check.

---

## 1. The ruling annotation — the judgement asked for

John authorised a later session, on 2026-09-21, to annotate a ruling file to
correct its **bookkeeping** — claims about where text landed, cross-references
and the like — while the twenty ruled items themselves stay untouchable. He was
told the risk that the line between bookkeeping and substance is drawn by
whoever is writing. This annotation is the first use of that permission.

**Judgement: it stayed on the right side of the line. No overreach.** Every test
I could put to it, it passes.

**It is additions only, and it touches no ruled item.** The change to the ruling
file is a single hunk appended after the last line, adding forty lines and
removing none.

```
$ git diff --numstat f3ba2f2 df76394
63	21	docs/known-failure-modes.md
26	7	docs/outside-review-protocol.md
40	0	docs/rulings/2026-09-21-review-verification-and-staged-spending.md
```

The zero in the third row is the whole answer on this point: nothing in that file
was removed or rewritten, so items 1 to 20 stand exactly as they stood. The diff
header for the one hunk is `@@ -223,3 +223,43 @@`, which is an append at the end
of a 225-line file.

**It corrects a bookkeeping claim and nothing else.** The claim it corrects is
the third entry in the closing "Recorded elsewhere" list — a list of pointers
saying where each ruled item went, which the recording session added as its own
record-keeping. That is bookkeeping in the plainest sense of the permission. The
annotation restates no ruled item, extends none, and reinterprets none.

**The claim it corrects is genuinely false, and I confirmed that without relying
on either session that reported it.** The pointer says items 3 to 8 landed in
`docs/outside-review-protocol.md` through pull request 13. Item 3 is the widening
of reviewer-owned verification to every Gate A, whether or not a fatal finding
exists.

```
$ git show b4e3e84~1:docs/outside-review-protocol.md > /tmp/proto_before.txt
$ grep -c "whether or not a fatal finding" /tmp/proto_before.txt
0
$ grep -n "owns the verification\|belongs to the reviewer" /tmp/proto_before.txt
297:Gate A it also owns the verification the closure rule requires below: the
345:- **That check belongs to the reviewer, not to the author.** The tier 1
```

Before the landing commit, the wide wording was absent from the protocol file,
and both reviewer-ownership sentences were the narrow ones. And the pull request
really did announce the widening it did not carry:

```
$ gh pr view 13 --json title,body -q '.title, .body'
Outside-review protocol: the three amendments ruled 2026-09-20
  …
  2. **Reviewer-owned verification of a fatal finding's closure**, added to the
     closure rule with a named owner and a required output.
  …
  **Ruled 2026-09-21, extending the original**: reviewer-owned verification runs
  at every Gate A, whether or not a fatal finding exists — not only on fatal
  closures.
```

The description carries the wide rule; the amendment it lists carries the narrow
one; the file got the narrow one. Exactly as the annotation says.

**Its account of where item 3 is now is accurate.** It says the widening was
landed at three points — the Gate A entry, the paragraph describing tier 1, and a
new bullet in the closure rule — by the commit `b4e3e84`, titled "Land the
widening of reviewer-owned verification, which never reached the file", and that
the protocol file's amendments section carries an entry saying why the landing
was owed.

```
$ git log -1 --format='%s' b4e3e84
Land the widening of reviewer-owned verification, which never reached the file
$ git show --stat --format='' b4e3e84
 docs/outside-review-protocol.md | 49 +++++++++++++++++++++++++++++++++++++----
 1 file changed, 45 insertions(+), 4 deletions(-)
```

That commit's change to the protocol file is three hunks, and they are the three
places named. The amendments entry is there. All four claims hold.

**Its scoping is right: item 3 is the only one of the six that did not land.** I
spot-checked the rest against the protocol file as it stands at the commit under
check. Item 4, the rehearsal requirement sitting after the gates rather than
inside the closure rule, is the section headed "The measurement rehearsal,
required before any Gate A". Item 5, a pre-stated quantity the rehearsal never
exercised being fatal on its own, is there in those terms. Item 6, the struck
word "unlikely" and its replacement's prohibition on manufacturing severity, is
there twice. So the annotation names the one entry that was wrong and does not
overstate the damage.

**It describes John's ruling in the ruling's own words, not the session's.** The
phrase it uses for item 3 — reviewer-owned verification at every Gate A, whether
or not a fatal finding exists — is item 3's wording verbatim. It does not
paraphrase him.

**It claims no authority beyond what he gave.** The closing note records the
permission as a choice among three options put to him, records that he was told
the risk and accepted it, and records that no compute was launched and no money
spent. That is the permission as granted, written down as granted, with the
session's own part in it visible rather than hidden.

The one sentence in it that leans at all is "He ruled item 3, and item 3 stands
above exactly as he ruled it." The same file's opening says the recommendations
were the session's and he approved them, recorded as mixed authorship, "never as
his own drafting". Read as "as he ruled it" rather than "as he wrote it" the
sentence is the file's own vocabulary — the file's title calls these John's
rulings — so this is a nuance and not a claim of authorship. Noted below, not
held against the merge.

---

## 2. Every printed block, re-run and compared byte for byte

Three sessions before this one re-ran the printed blocks in
`docs/known-failure-modes.md` and found them byte-identical. The pass under check
added a thirteenth block. I re-ran **all** of them, against the working tree at
this branch, which is byte-identical to the target for every file outside `docs/`
(`git diff --stat 2ad356a df76394 -- . ':!docs'` returns nothing, so nothing a
block reads has moved).

Method: a small script split each fenced block into its commands and its printed
output, ran the commands, and compared the captured output to the printed text as
whole strings. Thirteen blocks found, matching the file's own count.

```
$ python3 /tmp/runblocks.py
blocks found: 13
block  1 (line 141): IDENTICAL
block  2 (line 157): IDENTICAL
block  3 (line 178): IDENTICAL
block  4 (line 239): IDENTICAL
block  5 (line 293): PLACEHOLDER skipped (angle-bracket template)
block  6 (line 336): IDENTICAL
block  7 (line 396): IDENTICAL
block  8 (line 447): IDENTICAL
block  9 (line 493): PLACEHOLDER skipped (angle-bracket template)
block 10 (line 542): PLACEHOLDER skipped (angle-bracket template)
block 11 (line 563): IDENTICAL
block 12 (line 608): IDENTICAL
block 13 (line 621): IDENTICAL
```

Block 9 was a false alarm from my own filter, not a placeholder: it contains the
formatting instruction `{p:<5}` and an arrow `->`, which my angle-bracket test
mistook for a template. Run on its own it is identical too:

```
$ python3 -c "
for p in (0.95, 0.80, 0.60, 0.25):
    print(f'own-directed accuracy {p:<5} -> untouched rate {(1 - p) / 7:.4f}')
" > /tmp/blk9_got.txt
$ cmp /tmp/blk9_got.txt /tmp/blk9_exp.txt && echo "BLOCK 9 IDENTICAL"
BLOCK 9 IDENTICAL
```

So the two genuine placeholder blocks are block 5 — failure 2's part two, the one
that has never been run — and block 10, failure 4's part-one template. That is
two, which is what the file says.

**Result: eleven runnable blocks, eleven byte-identical, no drift.** The streak
is now four sessions. The file's own accounting — thirteen blocks, eleven with a
command and its output, two placeholders — is exactly right.

The thirteenth block is the new one, and it reproduces:

```
$ grep -nE "own_slot.*what the stack asks for|marker_token.*the input token itself" experiments/06-mvm-0a-constructed-self-index/position-sweep-findings.md
120:| `own_slot` — what the stack asks for | 0.293 (+1.60) | 0.273 (+0.88) | 0.243 (−0.24) | 0.283 (+1.33) | 0.275 (+0.91) |
122:| `marker_token` — the input token itself | **0.550 (+51.6)** | 0.513 (+43.1) | 0.510 (+41.3) | 0.498 (+41.9) | 0.490 (+40.8) |
```

### The new block's framing

**The numbers are right, at the layer and against the null the pass says.** The
findings file's table has columns layer 3, 4, 5, 7, 8, so the first number column
is the third layer, as the block says. The pre-stated quantity reads 0.293 at
about 1.60 standard deviations; the quantity the input guarantees reads 0.550 at
about 51.6. The table is introduced with "each against its own 50-draw
permutation null", which the block renders as fifty-draw. All correct.

**All three hedges are present.** (a) That it is a record and not the two runs
the test asks for: "These are two rows lifted from a record, not the two runs
part two asks for." (b) That the limb has never fired on anything it was not
fitted to: "the limb has still never been seen to fire on a design nobody had
already diagnosed." (c) That the findings file labels the diagnostic not
pre-stated and written after the sweep had already failed: the block says so, and
the findings file says "`src/probe_target_diagnostic_a3.py`, and it is **not
pre-stated** — it was written after seeing the sweep fail, which makes it worth
less than a measurement designed in advance". All three check out.

**The limb the block illustrates is supported across all three checkpoints, not
only the one the rows come from.** The findings file's own surviving claim is
"`own_slot` clears nothing in any of the thirty tests … while the input token at
the marker position clears on all three checkpoints." So the direction the block
draws from the two rows is the direction the record supports. Three things about
how it is presented are worth noting, and are in the list below.

---

## 3. The small corrections, spot-checked

**Four commit identifiers now carry plain phrases and titles.** Read off the
commits, one at a time:

```
$ git log -1 --format='%s' e8dad42
Tier 2 packets sized for the apps that have to read them
$ git log -1 --format='%s' 9653275
Say when work happens by what it waits on, not by a week
$ git log -1 --format='%s' 49c1002
Split the launch step so the chain shows the staggered launch
$ git log -1 --format='%s' 184a42f
Tier 2 packet: hand the reviewer every record the closure text cites
```

All four match the protocol file word for word. The other identifiers in the
three changed files check out too: the repair commit (`dceeafa`, "Repair three of
the four failure tests, and mark the list as not yet proven"), the pairing-rule
commit (`9393b92`, "Pair every session that writes binding text with one that
checks it"), the first check of the repair (`fbfecb5`, "Check the repair: the ten
outputs hold, two tests still owe a sentence"), the check before it (`0768b84`,
"Check the pairing rule and the known-failure list: the numbers hold, three tests
do not"), the Gate C review commit (`3bbfece`, "Gate C tier 1 review of the
successor experiment proposal: RT-172 to RT-188") and the proposal commit
(`d8ceba9`, "Successor proposal: the rehearsal buys a rented slice, and the
second release is bound to what it measures"). Every identifier in all three
files carries a plain phrase saying what it is, as the workspace rule requires.

**"Three lines" corrected to four things.** The four named are the module that is
imported, the list of pre-stated cells, and the two small functions — one, one
and two, which is four. The correction is right.

**The commit-message count correction reproduces exactly.** The claim being
corrected is that no commit in the last sixty on the main line carries a command
line in its message. Counting from the merge commit that was the main line's tip
when the repair was written (`73aa7e3`, "Merge pull request #22 from
jfredson/worktree-agent-a023ba493bc2e40c5"):

```
$ git log -60 --format='===COMMIT %H%n%B' 73aa7e3 > /tmp/chk_msgs2.txt
$ grep -c '^===COMMIT' /tmp/chk_msgs2.txt
60
$ grep -nE '^[[:space:]]*md5' /tmp/chk_msgs2.txt
1122:                                    md5 359fabbb4815e8df3cba8e38fd530248
```

One hit, and it is what the correction says it is. The surrounding lines show a
two-column table of filenames and their checksums, inside a message that files
the missing training log for the control-learnability pilot, and the hit is the
wrapped second column of one row. It is not a command. So the printed number was
wrong and the substance was right, which is what the protocol file now says. The
handling is also right: it opened the single hit rather than reporting a bare
number, and it recorded the correction in the protocol file because a commit
message cannot be edited after the fact.

**The long line was rewrapped and the words are unchanged.** The Gate A entry's
over-long line is re-broken across three lines with no word added or removed.

---

## 4. The two things left alone deliberately

**"That is this failure caught", under failure 2's part one.** Leaving it is
defensible but it is the weaker of the two choices. The new opening says "Part
two is the one that catches this failure; part one is a prompt to look", and
three paragraphs below the sentence in question the file says again "So part one
is a prompt to look and not a verdict". So the reader is told twice, once before
and once after. The sentence can also be read narrowly and truly — the search did
surface the failure on the design that produced it. But it reads against the new
opening, and a reader skimming for the disposition could take it at face value.
A wording cleanup, not a defect. It follows.

**Declining to assert a line count.** Right call, and I would not have wanted it
otherwise. The pass could not reproduce the count, so it wrote "most of the
block" instead of a number it could not stand behind. Counting the command lines
of that block myself, the four replaceable things are about thirteen of roughly
twenty-four, which is "most" and would have been a fussy number to print. A
softer true claim beats a precise unverified one, which is the standard this
whole document argues for.

---

## 5. Is the failure list fit to merge?

Yes, on the test that matters: **what it says about itself is true.** It does not
claim to be proven. It says at the top that as a set of tests a new design can be
run against it is not yet established, names which three of its four tests fell
short and why, says which blocks have been run and which have not, and says the
newest corrections in it are owed a check by a session that did not write them.
Every one of those statements I was able to check held. The protocol file is in
the same condition: it records what changed, why, and what has not been checked.

One sentence goes stale the moment this check lands: the top paragraph says of
the thirteenth block that "no other session has yet re-run it". This session has
now re-run it, byte for byte, along with the other ten.

---

## 6. Findings

### Must fix before merge

**None.**

### Can follow afterwards

1. **The new block quotes one checkpoint's row without saying which.** The two
   rows come from a table the findings file introduces with "Held-out
   nearest-average accuracy **on the pilot**". Eighteen lines further down the
   same file corrects itself: "Two things I said on the pilot alone do not
   generalise" — the first being this very read, which gives 0.49 to 0.55 on the
   pilot but only 0.06 to 0.12 on the other two checkpoints, clearing at three of
   five layers on one of them. The block's limb survives that, because the
   findings file's surviving claim covers all three checkpoints, and the block
   cites the file by path and line so the correction is one scroll away. But the
   block reads as though 0.550 at about 51.6 is the record, when it is the
   record's strongest instance. A fourth hedge naming the pilot would be more
   material than at least one of the three already there. This is the most
   substantive item on the list and it still does not warrant another round.

2. **"That null" points at the wrong null.** The block says the two quantities
   were read "each against its own fifty-draw permutation null, and the sweep's
   bar throughout is three standard deviations of that null". The sweep's own
   stated bar is three standard deviations of each test's **200-draw** null; the
   fifty-draw null belongs to the diagnostic the two rows come from. The rule —
   three standard deviations of a test's own null — is the same throughout, so
   only the pointer is loose, not the standard.

3. **The findings file asks for a companion number that the block does not
   carry.** That file corrects itself on quoting margins: they were "quoted in
   standard deviations of a 200-draw null, which cannot resolve beyond about one
   part in two hundred … Every test in this sweep reports how many shuffled draws
   met or beat the real score alongside the margin, and that convention should be
   carried backwards when those numbers are quoted." The block quotes about 1.60
   and about 51.6 without that count, from a null with fewer draws still. The
   block's "about" softens it and the grep shows the source, so this is a
   convention not followed rather than a number misstated.

4. **"That is this failure caught" reads against the new opening** under failure
   2's part one, as set out in section 4 above. A sentence's worth of work.

5. **One sentence is stale on landing.** The top paragraph's "no other session
   has yet re-run it", about the thirteenth block, stopped being true when this
   check ran it. Worth a one-line edit next time that paragraph is touched.

6. **One sentence in the ruling annotation leans slightly forward.** "Item 3
   stands above exactly as he ruled it" sits next to the same file's opening
   statement that the wording is the session's and the authorship mixed, "never
   as his own drafting". The file's own vocabulary calls these John's rulings, so
   the sentence is defensible; it is flagged because the standing rule is never
   to upgrade a session's call to John's, and the safest phrasing would have been
   "item 3 stands above exactly as it was ruled".

---

## 7. What was not done

- **Failure 2's part two is still unrun**, and this session did not run it.
  Running it means running a whole probe pipeline twice against model
  checkpoints, which costs compute nobody has authorised. It is correctly
  described as unrun in three separate places in the file. It stays unrun.
- No file was fixed, no compute was launched, no money was spent, nothing was
  pushed to the shared main line, no branch was merged and no pull request was
  opened. The only write this session made is this file, on its own worktree
  branch.
