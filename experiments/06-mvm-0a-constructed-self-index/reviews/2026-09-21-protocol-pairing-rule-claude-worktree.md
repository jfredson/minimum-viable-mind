# Check of the pairing rule, the failure-mode pass, and the known-failure list

*Filed 2026-09-21 (Pacific) by a Claude Code session in its own worktree
(`worktree-agent-a3a2bd18a22610614`). This is the check that the text under review
creates and says it is owed: the commit's own closing sentence reads "This text had
not been checked by another session when it was committed; under the pairing rule it
is owed one, and the session that writes that check is not this one." This session
did not write that text, did not propose the four changes, and has not read the
writing session's chat.*

*What I checked.* The commit `9393b92` ("Pair every session that writes binding text
with one that checks it") on the branch `worktree-agent-a15f7586cfb5553b3`. Two files:
`docs/outside-review-protocol.md` modified, adding four sections — the pairing rule,
"Isolation is not traded for speed", the failure-mode pass and the rebuild rule — and
`docs/known-failure-modes.md`, new. The commit's parent is `73aa7e3`, which is the tip
of the main line, so the before-text and the main-line text are the same text.

*What I opened.* The workspace plain-language rule (`~/Documents/Code/CLAUDE.md`).
`docs/outside-review-protocol.md` as it stands on main, before the change. The ruling
of 2026-09-21 on review verification and staged spending
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`), all twenty
items. The diff of pull request 13 and its description. The registered Amendment A3
text and the ceiling defect note, to check the numbers the new list quotes. The
episode generator (`src/curriculum_a3.py`, `src/curriculum.py`), the ownership-blind
attack sweep (`src/shortcut_sweep.py`) and the three endpoint records under
`a3-gates/`. The red-team ledger, for the finding numbers the new text cites. The
commit messages the new filing rule names as precedent. The review file carrying the
per-arm-ceiling and empty-cell findings, on the branch it sits on.

*What I did not open.* The writing session's chat or context. The successor experiment
proposal itself — I looked only at where it is committed, not at its design, because
nothing I was asked to check depends on its contents. STATUS.md, `data/project.toml`,
and the site. The two other ruling files of 2026-09-21 beyond the one named above.

*What I did not do.* I fixed nothing. I edited neither file under check. I ran no
compute, launched nothing and spent no money. I pushed nothing, merged nothing and
opened no pull request. Everything below is committed only to this worktree's own
branch.

*Lookup: none. No web search. Every command below was run against files committed in
this repository, from the repository root, on 2026-09-21.*

*The two labels.* **MEASURED** means I ran a command and its output is printed below.
**ARGUED** means no single command settles it and the judgement rests on reading
committed texts against each other. I have marked every finding.

*On finding numbers.* The ledger on the main line ends at `RT-171` (the last row of
`red_team_ledger.md`). The range `RT-172` to `RT-188` is taken by the Gate C pass on
the successor proposal, which sits unmerged on another branch. I therefore number
from `RT-189` so as not to collide with it, and note that if that branch is abandoned
these numbers leave a gap rather than a clash.

---

## Verdict in one table

| what I checked | verdict |
|---|---|
| Every printed output in `docs/known-failure-modes.md` reproduces | **HOLDS** — all eight reproduce exactly, character for character |
| Ruling item 3 (reviewer-owned verification at every Gate A) landed via pull request 13 | **DOES NOT HOLD** — it did not land; the ruling record is wrong (`RT-189`, fatal) |
| The four tests detect the failures they are written from | **TWO OF FOUR** — failure 2's test cannot fail on its own failure (`RT-190`); failure 3's first test does not run (`RT-191`) |
| The new filing rule's named precedent contains commands and outputs | **DOES NOT HOLD** — none of the four commit messages carries one (`RT-192`) |
| Failure 4's word-list catches a measurement claim | **PARTLY** — it misses this document's own headline claim (`RT-193`) |
| The citations to findings that sit off the main line | **TOLERABLE, WITH A DEFECT** — named by branch rather than by commit (`RT-195`) |
| Internal consistency across the four new sections and the old ones | **NO CONTRADICTION FOUND**, three seams worth naming (`RT-196`) |
| The workspace plain-language rule | **LARGELY KEPT** — identifiers are labelled throughout; three small breaches (`RT-197`) |

**One fatal finding, and it is not against the text under check.** The fatal item is a
defect in the ruling record that the writing session flagged and that I confirm
independently. Nothing in the two files under check is fatal. Four findings are
serious and four are worth-noting.

---

## 1. Every printed output reproduces — MEASURED

`docs/known-failure-modes.md` states, at line 34: "Every output printed below was
produced by running the command printed above it, in this repository, on 2026-09-21."
Today is 2026-09-21. I ran all eight commands that print an output. Every one
reproduces exactly.

I did not judge this by eye. I captured each command's live output to a file, cut the
corresponding printed lines out of the document, and compared the two byte for byte:

```
$ diff /tmp/d1.txt /tmp/o1.txt && echo "block 1 (ceiling arithmetic): IDENTICAL"
$ diff /tmp/d2.txt /tmp/o2.txt && echo "block 2 (scale tops): IDENTICAL"
$ diff /tmp/d3.txt /tmp/o3.txt && echo "block 3 (threshold range): IDENTICAL"
$ diff /tmp/d4.txt /tmp/o4.txt && echo "block 4 (key counts): IDENTICAL"
block 1 (ceiling arithmetic): IDENTICAL
block 2 (scale tops): IDENTICAL
block 3 (threshold range): IDENTICAL
block 4 (key counts): IDENTICAL
```

```
$ diff /tmp/doc_grep.txt /tmp/real_grep.txt && echo "IDENTICAL"
IDENTICAL
```

where the `d` files hold lines 88-89, 102-104, 228-231 and 291-293 of
`docs/known-failure-modes.md`, the `o` files hold the live output of the four python
commands, and the last pair compares the document's five printed grep lines (lines
212-216) against the live grep. `diff` printed nothing in every case, which is what it
does when two files are the same. That covers the column padding and the source
indentation, which are where a hand-copied output usually drifts.

The commands and their outputs, in full:

**Failure 1, part one — the ceiling arithmetic.**

```
$ python3 -c "
ceilings = {'primary battery': 0.2921, 'control battery': 1.0000}
for name, c in ceilings.items():
    print(f'{name}: denominator 1 - ceiling = {1 - c:.4f}')
"
primary battery: denominator 1 - ceiling = 0.7079
control battery: denominator 1 - ceiling = 0.0000
```

Matches the document. The two ceilings it is fed are also right: 0.2921 is the
registered primary-battery ceiling (`amendment-a3.md` line 415) and 1.0 is the
measured control-battery ceiling, which is the title of
`ceiling-measurement-findings.md` — "The control battery's ceiling is 1.0, and the
clause was never computable", with 1.0000 in its table for the name-keyed lookup, the
learned attack and the best of the family.

**Failure 1, part two — the scale-top figures.**

```
$ python3 -c "
def reading(whole, ownership_only): return (whole - ownership_only) / whole
floor = 0.125
for whole in (0.90, 0.60, 0.35):
    print(f'best score {whole}: top of scale = {reading(whole, floor):.3f}')
"
best score 0.9: top of scale = 0.861
best score 0.6: top of scale = 0.792
best score 0.35: top of scale = 0.643
```

Matches. The floor of 0.125 is the one-in-eight guessing rate, and there are in fact
eight answer slots: `len(curriculum.SLOTS)` is 8, checked by importing the module.

**Failure 3, part two — the generator grep.**

```
$ grep -n "rng.sample\|assert len(set" experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py
209:    markers = rng.sample(MARKERS, N_AGENTS)
210:    contested = rng.sample(ITEMS, N_CONTESTED)
215:        vs = rng.sample(SLOTS, N_AGENTS)
233:    revisers = rng.sample(range(N_AGENTS), K_REVISERS)
539:    assert len(set(vs)) == N_AGENTS, "distinctness broken by enactment"
```

Matches, line numbers and source indentation included, by the byte comparison above.
The substance the grep is quoted for also holds: `N_AGENTS` is 4, so line 215 draws four distinct values
without replacement and line 539 asserts they stay distinct — which is exactly the
property the document says empties the pre-stated cell.

**Failure 3, part three — the threshold range.**

```
$ python3 -c "
for p in (0.95, 0.80, 0.60, 0.25):
    print(f'own-directed accuracy {p:<5} -> untouched rate {(1 - p) / 7:.4f}')
"
own-directed accuracy 0.95  -> untouched rate 0.0071
own-directed accuracy 0.8   -> untouched rate 0.0286
own-directed accuracy 0.6   -> untouched rate 0.0571
own-directed accuracy 0.25  -> untouched rate 0.1071
```

Matches, including the two spaces after 0.95 that the padding produces.

**Failure 4, part two — the two worked examples.**

```
$ grep -c control experiments/06-mvm-0a-constructed-self-index/src/shortcut_sweep.py
0
```

```
$ python3 -c "
import json
base = 'experiments/06-mvm-0a-constructed-self-index/a3-gates/'
for p in ('endpoint_a3_30m_seed1.json', 'endpoint_a3_30m_seed2.json', 'pilot_endpoint.json'):
    print(p, len(json.load(open(base + p))))
"
endpoint_a3_30m_seed1.json 15
endpoint_a3_30m_seed2.json 15
pilot_endpoint.json 7
```

Both match. The key counts of 15, 15 and 7 are the ones the twentieth item of the
2026-09-21 ruling records, and they confirm that the count of 110 in the seventeenth
finding of the independent Amendment A4 pass is not any of them.

**This is the strongest thing in the check.** The programme has been bitten twice this
week by a claim of measurement that did not reproduce — the registered sentence
crediting the attack sweep with verifying a battery it never touches, and a finding
labelled MEASURED reporting a count of 110 keys where there are 15. A third would have
been serious. There is no third. Every number in this document came from running the
command above it.

One command exits non-zero even when it works: `grep -c` returns 1 when the count is
zero, so the first worked example of failure 4 exits 1 while printing the right
answer. A session that runs the failure-mode pass inside a script that stops on the
first error will stop there. Worth knowing; not a finding against the text.

---

## 2. `RT-189` — ruling item 3 is recorded as landed and did not land — MEASURED — **fatal**, against the ruling record

The writing session flagged this and asked for it to be confirmed or refuted
independently. I confirm it.

Item 3 of the 2026-09-21 ruling says: "**Reviewer-owned verification runs at every
Gate A**, whether or not a fatal finding exists — not only on the closure of a fatal
finding. **This extends item 6 of the 2026-09-20 ruling**, which named fatal closures
only." The last line of that ruling file says: "`docs/outside-review-protocol.md`:
items 3 to 8, landed via pull request 13."

It is not there.

```
$ git grep -c -i "whether or not a fatal finding" origin/main -- docs/outside-review-protocol.md
(no output; exit status 1, meaning no match)
```

```
$ git grep -n "owns the verification\|belongs to the reviewer" origin/main -- docs/outside-review-protocol.md
origin/main:docs/outside-review-protocol.md:171:Gate A it also owns the verification the closure rule requires below: the
origin/main:docs/outside-review-protocol.md:219:- **That check belongs to the reviewer, not to the author.** The tier 1
```

Both sentences on main are fatal-scoped. Line 171 continues "the decisive check on a
**fatal finding's** fix is the reviewer's to run". Line 219 sits inside the closure
rule, whose opening bullet is "Every **fatal finding** from either tier has a closure
line", so "That check" refers to the measured check on a fatal finding and nothing
else. The widened reading — that the verification runs whether or not a fatal finding
exists — appears nowhere in the file.

I then read what pull request 13 actually changed, and the gap is visible in the pull
request itself. Its description announces the widening in so many words: "Ruled
2026-09-21, extending the original: reviewer-owned verification runs at every Gate A,
whether or not a fatal finding exists — not only on fatal closures." Its diff adds
only the narrow wording. The description carries the ruling; the file does not.

**So the writing session's report is right and the ruling record is wrong.** This is
the same class as the uncommitted-citation defect (`RT-145`, the finding that a
registration commit was resting on a ruling file committed nowhere): a record states
that something is in place which a reader who opens the file will not find. It is
arguably worse, because `RT-145` was a citation pointing at nothing, and this is a
governing rule that every session reading the protocol will apply in its narrow form
while the ruling file says the wide form is live.

**What holds.** I checked the other items the same line claims. Item 4 (the rehearsal
sits after the gates rather than inside the closure rule) is in place — the rehearsal
section is its own section between the gates and the two tiers, and nothing about it
appears in the closure rule. Item 5 (a pre-stated quantity the rehearsal never
exercised is a fatal finding on its own) is in place, in the rehearsal section's
filing paragraph. Item 6 (the replacement for the struck "unlikely" sentence, with its
prohibition on manufacturing severity) is in place, at the end of the fixed brief.
Items 7 and 8 rule that things stand as written and needed no edit. Item 3 is the sole
gap. (ARGUED, by reading the main-line text item by item.)

**Not a finding against the text under check.** The commit I am checking did not cause
this and did not hide it; a different session reported it. It is filed here because
the brief asked for an independent answer and because the record needs one.

---

## 3. Do the four tests detect what they claim?

The document sets its own standard, in its closing section: "A test that has never
been seen to fail has not been shown to detect anything." I judged each test against
that sentence. Two meet it. Two do not.

### 3.1 `RT-190` — failure 2's test cannot fail on the failure it is written from — ARGUED — **serious**

Failure 2 is the probe target that cannot be recovered in principle: weeks spent
predicting the episode generator's index for whichever agent the model is playing,
from a model that was never required to compute it.

Its test has two parts. Part one is paper and pencil — write one sentence naming the
route by which the quantity reaches the model's states. Part two runs the probe
pipeline twice, once on the pre-stated target and once on a quantity the design
guarantees is present. Then:

> **It fails if** the second run does not clear the bar.

The second run is the one on the guaranteed quantity. In the history this test is
written from, that run cleared, and cleared enormously: the document itself says the
powered target test of 2026-09-19 "returns 0.5877 against a no-information value of
0.04, about 159 standard deviations of its own null", and concludes "The instrument
was never the problem."

So on the very design that produced failure 2, this test passes. The pipeline was
sound; the target was unrecoverable; and the stated failure criterion looks only at
the pipeline. The case the entry exists to catch — the first run returns nothing and
the second run clears — is not named as a failure anywhere in the entry.

This is the shape my brief asked me to look for: a test written so loosely that a
design can pass it while carrying the defect. A successor design could run both
probes, watch the guaranteed quantity clear, file the disposition with its command and
output, and register a pre-stated target that is as unrecoverable as `own_slot` was.

The part that would actually catch it is part one, the sentence naming the route. But
part one produces no command and no output, and the protocol's failure-mode pass
requires that "every disposition shows its work: the command that was run and the
output it returned". Failure 2 therefore cannot produce a disposition with work shown
for the case it was written to catch.

I am not proposing the repair; that belongs to a different session. I am stating what
the test does not do.

### 3.2 `RT-191` — the first part of failure 3's test does not run — MEASURED — **serious**

Failure 3 is the cell that is empty by construction. Its first test is the one that
would catch an empty cell in a new design: count what the generator actually puts in
each pre-stated cell. I ran it exactly as printed.

```
$ python3 -c "
from collections import Counter
from src.curriculum import generate          # the registered generator, not a stand-in
counts = Counter(cell_of(trial) for trial in generate(n_episodes=200, seed=0))
for cell in PRE_STATED_CELLS:
    print(f'{cell}: {counts.get(cell, 0)} trials')
"
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    from src.curriculum import generate          # the registered generator, not a stand-in
ModuleNotFoundError: No module named 'src.curriculum'
```

Three things are wrong with it, and they compound.

The import path does not exist. There is no `src` package; the generator modules sit
in `experiments/06-mvm-0a-constructed-self-index/src/` and import each other by bare
name (`curriculum_a3.py` line 128 reads `from curriculum import MARKERS, ITEMS,
SLOTS, Query, Episode`), which means the directory is put on the path, not treated as
a package.

There is no function called `generate`. I checked by importing the module directly:

```
$ python3 -c "
import sys; sys.path.insert(0,'experiments/06-mvm-0a-constructed-self-index/src')
import curriculum
print('has generate?', hasattr(curriculum,'generate'))
print('generate-like names:', [n for n in dir(curriculum) if n.startswith('generate')])
"
has generate? False
generate-like names: ['generate_balanced', 'generate_episode']
```

And `cell_of` and `PRE_STATED_CELLS` are used but never defined or explained. The
document's own instruction for writing tests, two pages later, is: "Write the test so
that a session holding a different design can run it without asking anyone what it
means." A session holding a different design cannot run this one, and cannot tell from
the text what `cell_of` is supposed to return.

**Why this matters more than it looks.** No output is printed under this command, so
the document's honesty claim at line 34 is untouched — it never said this one had been
run, and it had not. But the closing section says an entry on this list gets checked by
another session for two things: "that the test runs, and that it fails on the design
that produced the finding." I am that session. It does not run. It has therefore never
been seen to fail, and by the document's own sentence it has not been shown to detect
anything. It is the entry's primary detector and the only part of it that generalises
to a design other than the A3 grammar.

### 3.3 `RT-194` — failure 1's first test is a display, not a detector — ARGUED — worth-noting

Failure 1's part one prints `1 - ceiling` for ceilings typed into the command by hand.
It cannot fail unless the number typed in is already the number that reveals the
failure.

Run it on what was actually registered on 2026-09-15 and it passes. The registered
control-battery ceiling was 0.3227 (`amendment-a3.md` line 415), not 1.0; substitute
it and the command prints a denominator of 0.6773 and nothing looks wrong. The
zero appears only once somebody has measured the ceiling properly, and measuring it is
what the rehearsal rule requires — a rule that was already in the protocol before this
commit.

The entry says as much, honestly: "Both halves need numbers from the rehearsal: a
ceiling that was assumed rather than measured is what produced this failure in the
first place." So the entry knows. But the consequence is worth stating plainly,
because a session running the failure-mode pass under time pressure will read a printed
command as a check: all of this test's detection power is borrowed from a different
rule, and running the command against assumed ceilings reproduces the original failure
while producing a filed output that looks like a disposition.

**Part two is the best test in the document.** It runs, it is the only printed command
that would have failed on the design it was written from — 0.861, 0.792 and 0.643 are
three different tops of scale where a single pre-stated threshold has to travel — and
its failure criterion is sharp and stated ("if the top of the scale differs between
the conditions a single pre-stated threshold is compared across"). Two reservations,
both small: the criterion carries no tolerance, so a session reading 0.861 against
0.859 must decide for itself; and the formula is this measure's algebra typed in by
hand, so applying it to a different measure means rewriting the command, at which
point it is a worked example rather than a test.

### 3.4 `RT-193` — failure 4's word-list misses this document's own headline claim — MEASURED — **serious**

Failure 4's part one is the most portable thing in the document: a grep for the words
that mark a claim of measurement, so that none is checked by accident and none is
missed. I ran it on the document that ships it.

```
$ grep -n -E "verified|measured|calibrated|attacked|reproduc|confirmed|ran" docs/known-failure-modes.md
22:easy to reproduce while naming it. A proposal reviewed on 2026-09-21 quoted the
24:measure, and the measure two sections earlier reproduced it.
53:adopted. The fix depended on a ceiling nobody had measured. The measurement, when
73:— which at the time of writing sits on the reviewing session's own branch
79:will be applied to, using ceilings measured in the rehearsal rather than
108:the measured ceiling moves the reading a lot; or if the top of the scale differs
112:ceiling that was assumed rather than measured is what produced this failure in
151:the pre-stated target, once on a quantity the design guarantees is present, read
156:$ python3 src/<probe_script>.py --target <a quantity the input guarantees> --report margins
160:recover a quantity known to be there has not measured the target; it has measured
170:the seven pre-stated controls — the one that separates "the transplant moved who
171:is acting" from "the transplant smuggled a value across", and so the one the
181:under failure 1 above and with the same caution about which branch it is on.
215:233:    revisers = rng.sample(range(N_AGENTS), K_REVISERS)
219:*Part three: compute every pre-stated threshold at both ends of the range it will
235:fires on the healthy end of the range and passes on the broken end. Both are
241:## 4. A claim of measurement with no record, or with a record that does not reproduce
244:ceilings were "verified by the attack sweep, whose best ownership-blind attack
256:does not reproduce. The seventeenth finding of the independent pass on the
272:$ grep -n -E "verified|measured|calibrated|attacked|reproduc|confirmed|ran" <the text>.md
```

**Line 34 is not in that list.** Line 34 is the sentence "Every output printed below
was produced by running the command printed above it, in this repository, on
2026-09-21" — the single most load-bearing claim of measurement in the whole document,
the one this check spent most of its time on, and the one the programme has twice been
burned by getting wrong. The word list misses it because the sentence says "produced by
running", and none of `verified`, `measured`, `calibrated`, `attacked`, `reproduc`,
`confirmed` or `ran` is a substring of "running".

The same list misses other ordinary phrasings a registration text will use: "we
verify", "verification", "checked", "shows", "the sweep found", and any bare number
presented as a result with no verb at all.

In the other direction it is noisy, because `ran` is matched as a bare substring. Six
of the twenty hits above are that: "transplant" at lines 170 and 171, "range" at 219
and 235, "range(N_AGENTS)" at 215. Noise is the safe direction for this test and I do
not count it as a defect; the misses are the defect.

**The rest of failure 4 is sound.** Its two worked examples both reproduce (section 1
above). Its failure criterion is the sharpest in the document — a sentence that names
no file, or names a file that does not contain the number, or names a file that exists
at no commit — and it is the one criterion here that a session could apply to a design
it has never seen.

### 3.5 Summary on the four tests

| failure | does its test detect the failure it was written from? | would it catch the failure's newest form? |
|---|---|---|
| 1. Zero denominator | **Part two yes** — it fails on the successor design, which is where the newest form was found. **Part one no** — it passes on the design as registered, and only fails once the rehearsal has already found the problem | Part two yes, for a measure with this algebra; a different measure needs the command rewritten |
| 2. Unrecoverable probe target | **No.** The stated failure criterion is about the pipeline, and the pipeline was sound. The test passes on the design that produced the failure | No — and the case it should catch is not named as a failure anywhere in the entry |
| 3. Cell empty by construction | **Part three yes** — it shows the pre-stated check firing on a model that learned the task and passing one that learned nothing. **Part two partly** — it reproduces, but greps one hard-coded file for two hard-coded idioms. **Part one: does not run** | Part one is the part that would generalise, and it does not run. Part two would miss `shuffle`, `set()`, sampling without replacement written another way, or a generator in a different file |
| 4. Claim of measurement with no record | **Yes**, on both historical forms; both worked examples reproduce | **Partly** — its word list misses the newest form, which is this document's own line 34 |

---

## 4. `RT-192` — the new filing rule names a precedent that does not contain what it claims — MEASURED — **serious**

The pairing rule says where a check is filed. Second paragraph:

> Otherwise the check goes in the message of the commit that lands the checked text,
> **commands and outputs included**, which is where the packet rebuilds and the roadmap
> conversion of 2026-09-21 already put theirs.

I read the commit messages this points at and counted lines that look like a command:

```
$ grep -cE '^\s*\$ |^\s*(git|python3?|grep|wc|sed|awk|diff|md5|shasum) ' /tmp/m1.txt /tmp/m2.txt /tmp/m3.txt
/tmp/m3.txt:0
/tmp/m1.txt:0
/tmp/m2.txt:0
```

where the three files hold the full messages of `e8dad42` ("Tier 2 packets sized for
the apps that have to read them", the packet rebuild), `9653275` ("Say when work
happens by what it waits on, not by a week", the roadmap conversion) and `49c1002`
("Split the launch step so the chain shows the staggered launch"). I read the fourth,
`184a42f` ("Tier 2 packet: hand the reviewer every record the closure text cites"), by
hand; it has none either.

What those messages contain is careful prose describing checks that were run, with
some of their numbers — `e8dad42` says "the material in the two packets has the same
fingerprint - 386,244 characters, the same order, no difference", and `184a42f` says
"The packet gave the outside reviewer the closure text and five records. The closure
text cites twenty." Good records. But not commands and not outputs, which is what the
new rule says they already are.

This matters twice over. It is a claim about a committed record that the record does
not support, which is failure 4 on the list this same commit adds. And it is the rule
that tells a future session what a filed check has to look like when the target
belongs to no experiment — that is, the rule governing every check on this protocol
itself. A session pointed at those four commits as the model will write prose, because
that is what the model does.

**What does hold:** the rebuild rule's second bullet, which says rebuilding the
outside-reviewer packet "showed that the reviewer was being handed five records against
the twenty that text cites", reproduces exactly against `184a42f`'s own message,
quoted above. (MEASURED.)

---

## 5. `RT-195` — the citations that sit off the main line — ARGUED — worth-noting

My brief asked whether naming the branch is adequate under the closure rule, or whether
a protocol document may cite something off the main line at all.

**What is actually there.** The known-failure list gives the full path —
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md`
— and then adds that it "sits on the reviewing session's own branch
(`worktree-agent-a5e89aa434ea3f396`) and is not yet on the main line". So the path is
cited plainly and the caveat is explicit. It is also a real file at a real commit:

```
$ git ls-tree -r --name-only worktree-agent-a5e89aa434ea3f396 experiments/06-mvm-0a-constructed-self-index/reviews/ | grep successor
experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md
```

and the commit that carries it, `3bbfece`, is titled "Gate C tier 1 review of the
successor experiment proposal: RT-172 to RT-188", with the per-arm-ceiling finding
described in its message in the terms the new list uses.

**My judgement, in four parts.**

*Against the closure rule: no violation.* The closure rule asks a sentence claiming
verification to "cite the committed record by file name". The file name is cited and
the record is committed.

*Against the list's own failure-4 criterion: passes the letter, misses the reason.*
That criterion fails a sentence that "names a file that exists at no commit". This file
exists at a commit. But the reason given for the criterion is that "a registration
commit is the one commit that may not rest on a record its reader cannot open", and a
reader working from the main line cannot open this one.

*May a protocol document cite off the main line at all?* Yes, in my judgement, on three
conditions, and this text meets two of them. It must say so, which it does, twice and
prominently. The citing sentence must not be load-bearing for an obligation — here it
is load-bearing only for an argument, the cost paragraph's case that the rate of
catching defects has risen, which is an argument a reader can weigh without the file.
And it must name something durable. That is the condition it misses.

*The real defect is the anchor.* A branch name is not durable. Worktree branches in
this repository are created per session and deleted after merge; that is what they are
for. When `worktree-agent-a5e89aa434ea3f396` is merged and removed, the citation's only
signpost goes with it, and the commit `3bbfece` becomes unreachable and eventually
collectable — without anyone editing the citing sentence, and with nothing to warn the
next reader. The repository's own habit elsewhere is to cite the commit: `e8dad42`'s
message names "the closure text at `a4c754e`" and "the record selection from the
rebuilt packet at `184a42f`". The commit identifier is what should have been given,
with the branch as a convenience.

*One more layer, which the text does not mention.* The proposal that review reviews,
`docs/successor-experiment-proposal-2026-09-21.md`, is on neither the main line nor
that review branch — it is on a third branch, `worktree-agent-a94b8938df2edd88b`, at
`d8ceba9`. So the citation is two branches deep. A reader who follows it to the review
file and then wants to see the design being criticised has a second hunt ahead, and
nothing tells them where to look.

---

## 6. `RT-196` — internal consistency: no contradiction, three seams — ARGUED — worth-noting

I read the four new sections against the closure rule, the rehearsal section, the two
tiers, the gates and the filing section, looking for two rules that disagree about who
owns what. **I found no outright contradiction.** The division is coherent: the
rehearsal says when a gate may open, the failure-mode pass and the closure check say
what must be filed before a registration commit, the pairing rule says that every piece
of binding text gets a second session regardless of gates, and the rebuild rule says
when a cited document must be regenerated rather than re-read. The rehearsal and the
failure-mode pass in particular fit together rather than overlapping: the rehearsal
produces the measured ceilings that failure 1's test needs, and the pass consumes them.

Three seams are worth naming.

**(a) The filing fallback cannot be followed for this very text.** The pairing rule
defines binding text as text that has been committed — "A working draft does not, until
it is committed as one of those" — and then says a check on a document belonging to no
experiment "goes in the message of the commit that lands the checked text". Those two
cannot both hold. The text is not binding, and so does not need a check, until it is
committed; but by then the commit that lands it already exists and its message cannot
be written. The protocol document lives at `docs/`, belongs to no experiment, and is
the first thing the rule is applied to — and this check is being filed under an
experiment's reviews directory precisely because the fallback does not work. The rule's
own first application contradicts it.

**(b) "Registration text" is narrower than Gate A.** Gate A covers "Every registration,
amendment, threshold lock, or pre-statement that will be read as binding". The
failure-mode pass says "Every **registration text** goes through a pass", and closes
with "A **registration text** with no filed failure-mode pass does not reach its
registration commit." Whether an amendment, a threshold lock or a standalone
pre-statement is a "registration text" is left to the reader. The clause added to Gate A
itself is broader ("The registration commit waits on the closure rule and on the filed
failure-mode pass"), so the two readings pull apart. A session wanting to move fast will
take the narrow one.

**(c) MEASURED and ARGUED are used before they are defined.** The pairing rule is
inserted after the gates, and says "Every finding is labelled MEASURED or ARGUED, the
convention the passes already use." The definition of those two words — "MEASURED (a
check was run and the output is reported) or ARGUED (reasoning a reader can dispute)" —
is in the tier 1 section, which now sits three sections further down. A reader meeting
the words for the first time is told they are a convention and not what they mean.

**One thing I checked and cleared.** Item 7 of the 2026-09-21 ruling says "The protocol
amendment text does not need its own Gate A pass." The new commit says this text is owed
a check under the pairing rule. Those do not conflict: a pairing check is not a Gate A
pass, and the pairing rule is a new obligation ruled later. But nothing in the new text
draws that distinction, and a reader holding both documents could reasonably think the
commit is asking for something a ruling excused. Worth a sentence somewhere; not a
defect.

---

## 7. `RT-197` — the workspace plain-language rule — ARGUED — worth-noting

**Largely kept, and deliberately so.** The rule against bare identifiers is followed
carefully throughout both files. Every finding number carries a plain phrase: "the
unequal-ceilings finding (`RT-21` in the red-team ledger)", "(`RT-172`, the
per-arm-ceiling finding)", "(`RT-173`, the empty-cell finding)", "(`RT-145` in the
red-team ledger, the finding that a registration commit was resting on a ruling file
that had not been committed)", "(`F17`, on whether one condition's validity gates were
ever applied)". The one piece of jargon that could have gone unexplained — `own_slot` —
is glossed on first use as "the episode generator's index for whichever agent the model
is playing". The control battery is explained as "the comparison battery of questions,
built so that answering it does not require knowing whose value is whose". An arm is
explained as "every version of the system being compared". This is better than the rule
usually gets.

Three breaches, all small.

**The branch name is an identifier a reader cannot hold.**
`worktree-agent-a5e89aa434ea3f396` carries only the phrase "the reviewing session's own
branch", which is a label, so it meets the letter of the rule. But the rule exists
because John has said he cannot hold identifiers in his head, and a thirty-character
hexadecimal branch name is the purest example of one. Section 5 above argues it should
be a commit identifier for a different reason; either way, what a reader needs is the
sentence that says what is in the file and why it is not on the main line, which the
text does give.

**"The eleven edits that got it there."** In the pairing rule's closing paragraph: "the
gate catches the document and misses the eleven edits that got it there." It reads as
rhetoric, but it is a specific count in a document whose whole argument is that specific
counts must come from somewhere. Nothing produced the eleven. In a text that is about to
require every number to carry the command that produced it, a made-up number in the
argument for the requirement is a bad look — and the sentence loses nothing if the count
goes.

**One ragged line break.** In the cost paragraph of "Isolation is not traded for speed",
the sentence "What has improved is the finding, not the writing" is broken across three
lines, one of which is twelve characters long. Cosmetic, except that this file goes to
outside reviewers verbatim. The same paragraph's phrase "What has improved is the
finding, not the writing" is also the least plain sentence in the new text: "the
finding" is being used to mean the catching of defects, which a reader outside this
system will not get on the first pass.

**A judgement call I am recording rather than filing as a breach.** The new text coins
four labels — "binding text", "the pairing rule", "the failure-mode pass", "the rebuild
rule". The workspace rule says "Don't invent shorthand. If a phrase needs explaining,
replace it rather than explain it." Each of these is defined at its first use, and
"binding text" is then used as a bare noun afterwards ("That addition is binding text,
so it is checked under the pairing rule like any other"). I think they are defensible:
they are the names of rules in a document of rules, which is closer to "training load"
than to jargon, and a protocol that cannot name its own rules is unusable. But
"binding text" is the one doing the most work on the least explanation, and it is the
one a reader will meet again in some other document with no definition nearby.

---

## 8. One claim I could not check — ARGUED

The cost paragraph rests its whole case on one observation: "the rate at which this
programme produces defects has not fallen, while the rate at which it catches them has
risen." No record is cited and no count is given, and I know of none that exists. It is
a rate claim about the programme's own history, and it is the argument for paying the
cost of all four new rules.

I am not calling this a finding, because the sentence does not claim to be a
measurement and the paragraph is explicit that it is the session's own addition that
"nobody asked for". But a document that requires every "verified" and "measured"
sentence to point at a committed record is, in its own justification, asking to be taken
at its word about two rates. The evidence it does give — that the zero-denominator
failure and the per-arm-ceiling failure are "the same failure six days apart" (2026-09-15
to 2026-09-21, which is six days) and that "the design that produced the second was
written by a session that had the first in front of it" — supports the first half of the
claim. The second half, that catching has got faster, has nothing behind it here.

---

## Is this text fit to be the protocol?

**The four new rules: yes.** The pairing rule, the refusal to trade isolation for speed,
the failure-mode pass and the rebuild rule are each written from a real failure in this
repository, each names the failure, and each says who owns the work and what has to be
filed. The reasoning in "Isolation is not traded for speed" — that this is the cheapest
step to skip and the one that has caught the most — is the right thing to write down in
the place a session under pressure will read it. I found no contradiction with the
gates, the tiers, the brief, the rehearsal or the closure rule. The document is honest
about what is approved and what is the session's judgement, and honest that no ruling
file records the approval yet.

**The list of known failures: not yet, as a test suite.** As a description of what has
gone wrong here it is accurate and every number in it reproduces, which is the harder
half and the half the programme has been failing. As the thing a registration text is
run against, it does not yet meet the standard its own last page sets. Of the four
entries, one has a test that cannot fail on the failure it was written from (failure 2),
one has its primary test in a state that does not execute (failure 3, part one), one
has a first part that passes on the design that produced it (failure 1, part one), and
one has a word list that misses the newest form of the thing it looks for (failure 4,
demonstrated on this document's own line 34). Two tests — failure 1's second part and
failure 3's third part — are genuinely good, run, and have been seen to fail.

**So my answer is: adopt the protocol sections, and mark the list as not yet meeting its
own closing standard.** The list should say on its face that three of its tests have not
been shown to detect anything, until a different session repairs them and a third checks
that repair — which is the sequence this text itself creates, and which I am the first
half of.

**And the fatal item is outside both files.** Item 3 of the 2026-09-21 ruling — reviewer-owned
verification at every Gate A, whether or not a fatal finding exists — is recorded as
landed and did not land. Until that is fixed, the protocol in force is narrower than the
ruling that governs it, and every session that reads the file will apply the narrow one.

---

*Filed under the outside-review protocol's filing rule
(`experiments/<experiment>/reviews/YYYY-MM-DD-<target>-<reviewer>.md`), verbatim, not
to be edited after filing. Nothing here is a fix. The repairs belong to a different
session, and the check on those repairs to a third.*
