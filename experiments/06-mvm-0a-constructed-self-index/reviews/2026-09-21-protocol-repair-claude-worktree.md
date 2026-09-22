# Check of the repair to the pairing rule and the known-failure list

*Filed 2026-09-21 (Pacific) by a Claude Code session in its own worktree
(the branch `worktree-agent-a39b12c0e16c03067`). This is the check the repair says
it is owed. The repairing session's own closing words are: "This repair has not been
checked by another session. Under the rule it is being made under, it is owed one,
and that session is not this one." I am that session. I did not write the repair, I
did not write the text it repairs, and I have not read either session's chat.*

*Filed under this experiment's reviews directory, and not in a commit message,
because the target is the outside-review protocol and the failure list beside it,
which belong to no experiment. That is what the repaired filing rule says to do, and
the opening line saying why it is filed here is this one.*

---

## What I opened

The workspace plain-language rule (`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30).
The two files under check at the branch tip, `docs/outside-review-protocol.md` and
`docs/known-failure-modes.md`. The two commits that make up the repair and their full
messages: `b4e3e84`, the commit titled "Land the widening of reviewer-owned
verification, which never reached the file", and `dceeafa`, the commit titled "Repair
three of the four failure tests, and mark the list as not yet proven". The
specification for the repair, which is the earlier check filed at `0768b84`, the
commit titled "Check the pairing rule and the known-failure list: the numbers hold,
three tests do not", read in full — all nine of its findings, the ones numbered
`RT-189` through `RT-197`. The text that was repaired, at `9393b92`, the commit titled
"Pair every session that writes binding text with one that checks it". The ruling the
repair lands, at `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`,
item 3 and the section at its foot that says where each item was landed. The episode
generator for the A3 task grammar and the one it extends
(`experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py` and
`src/curriculum.py`). The method document committed before the position sweep and the
one committed before the powered target test, and the seven other method documents in
this experiment. The findings from the position sweep of 2026-09-19. The three
endpoint records under `a3-gates/`. The attack sweep source file. The messages of the
six other commits the two documents name.

## What I did not open

The chat or working context of either the writing session, the checking session or
the repairing session. The successor experiment proposal's design — I looked only at
where it is committed, as the earlier check did. STATUS.md, `data/project.toml` and
the site. The other two rulings of 2026-09-21. Pull request 13 itself: I checked what
is in the file, which is what matters, and took the earlier check's reading of the
pull request description as given.

## What I did not do

I fixed nothing. I edited neither file under check, and I did not touch the ruling
file or the earlier check. I launched no compute and spent no money. Failure 2's
second part needs a probe pipeline run twice against model checkpoints; that costs
compute, so I did not run it, and I say below what follows from not running it. I
pushed nothing to the main line, merged nothing into it and opened no pull request.
I brought the repair branch into this worktree's own branch by fast-forward so that I
could run its commands, and everything below is committed only to this branch.

*Lookup: none. No web search. Every command below was run from the root of this
worktree on 2026-09-21, against files committed in this repository.*

## The two labels

**MEASURED** means I ran a command and its output is printed below. **ARGUED** means
no single command settles it and the judgement rests on reading committed texts
against each other. Every finding carries one.

## On finding numbers

The red-team ledger on the main line ends at `RT-171`, its last row. The range
`RT-172` to `RT-188` is taken by the Gate C pass on the successor proposal, now on the
main line. `RT-189` to `RT-197` are the earlier check's. I number from `RT-198`.

---

## Verdict in one table

| what I checked | verdict |
|---|---|
| All ten printed outputs in the failure list reproduce under `diff` | **HOLDS** — ten of ten, byte for byte, no drift of any kind including whitespace |
| The first check's fatal finding (`RT-189`), that ruling item 3 never landed, is now landed | **HOLDS** — in all three places, and the three agree |
| Failure 2's repaired test detects an unrecoverable probe target | **PART ONE PARTLY, PART TWO SOUND BUT NEVER RUN** — the new middle limb is right and the history contains the numbers that fire it; the route-sentence search is a proxy (`RT-198`) |
| The failure list's claim that every repaired test is printed with an output showing it failing | **DOES NOT HOLD** for failure 2's second part (`RT-199`, serious) |
| Failure 3's first test runs and returns zero in the first pre-stated cell | **HOLDS** — and a control shows it is not vacuously zero |
| Failure 1's first part is honestly labelled | **HOLDS** — it is a display, the document says so in bold, and the criterion is about provenance |
| Failure 4's widened word list catches five of six, with the number sweep for the sixth | **HOLDS** — and I confirmed it on the real document, not only on the copies |
| The filing rule's replacement precedent carries commands and outputs | **HOLDS** — measured: zero for the four removed, three and two for the two named |
| Is the filing rule followable as written? | **YES** — concrete enough that this file was written from it (`RT-201` on its durability and on one count that does not reproduce) |
| The ruling file, left saying item 3 landed via pull request 13 | **NEEDS AN ANNOTATION** (`RT-200`, serious) — the wrong line is session bookkeeping, not John's ruling |
| Internal consistency across the four sections and the failure list | **NO CONTRADICTION FOUND** |
| The workspace plain-language rule | **LARGELY KEPT** — the breaches the earlier check named are closed; two new small ones introduced by the repair (`RT-202`, `RT-203`) |

**No fatal finding.** Two serious (`RT-199`, `RT-200`) and four worth-noting (`RT-198`,
`RT-201`, `RT-202`, `RT-203`). The fatal finding of the earlier check is closed, and
closed properly. Of the earlier check's nine findings, all nine are addressed and seven
are fully closed; the two that are not — the route-sentence test and the plain-language
rule — are closed in substance with the residue filed above.

---

## Was each of the earlier check's findings actually closed?

The repair's specification was the check filed at `0768b84`, whose nine findings are
numbered `RT-189` to `RT-197`. I went through them one at a time.

| the earlier check's finding | closed? | where I say so |
|---|---|---|
| `RT-189`, fatal — ruling item 3, reviewer-owned verification at every registration gate, was recorded as landed and had not landed | **CLOSED** — landed in three places that agree with the ruling and with each other. The ruling file's own wrong line is left, which is `RT-200` | section 2, section 4 |
| `RT-190`, serious — failure 2's criterion looked only at the probe pipeline, so it passed on the design that produced the failure | **CLOSED IN SUBSTANCE** — the new middle limb is the right pattern, and the numbers that fire it are in the record the entry was written from. It has never been executed, and the file does not say so (`RT-199`) | section 3.1 |
| `RT-191`, serious — failure 3's first test did not execute at all | **CLOSED** — it runs, returns zero in the first pre-stated cell, and a control shows it returns 137 there when the design permits it | section 3.3 |
| `RT-192`, serious — the filing rule named four commits as carrying commands and outputs, and none did | **CLOSED** — the four are removed, measured at zero apiece, and two that do carry them are named by commit | section 5 |
| `RT-193`, serious — failure 4's word list missed the document's own headline claim of measurement | **CLOSED** — the widened list catches it, which I confirmed in the file itself and not only on a typed copy | section 3.5 |
| `RT-194`, worth-noting — failure 1's first part is a display, not a detector | **CLOSED** — labelled a display in bold, the failure passing its own test is printed beside it, and the criterion is now about where the numbers came from | section 3.4 |
| `RT-195`, worth-noting — citations to off-main work anchored to a branch name, which a merge deletes | **CLOSED** — both are now cited by commit with the commit's title attached, and both have since reached the main line | section 5 |
| `RT-196`, worth-noting — three seams: the unfollowable filing fallback, "registration text" narrower than the gate, and the two labels used before being defined | **CLOSED**, all three | section 6 |
| `RT-197`, worth-noting — three small breaches of the plain-language rule | **CLOSED** — the invented count and the uncounted rates are gone, every finding number carries its phrase. Two new small breaches introduced (`RT-202`, `RT-203`) and one unwrapped line | section 6 |

**Plainly: nine of nine addressed, seven fully closed, two closed in substance with a
residue I have filed.** Nothing in the earlier check was ignored, and nothing was closed
by assertion — each closure above is either a command I ran or a passage I read against
the specification.

---

## 1. Every printed output reproduces — MEASURED

The file claims, at its line 34: "Every output printed below was produced by running
the command printed above it, in this repository, on 2026-09-21." The repair adds a
second claim, in its commit message: "Ten printed blocks, each captured live and
compared with diff rather than by eye. diff printed nothing for all ten. Two blocks
are templates with placeholders and no printed output, and are skipped."

That is a claim of measurement about a document whose subject is claims of
measurement, and the programme has twice this week been bitten by one that did not
reproduce. So I checked the count first and then every block.

**The count is right.** The file holds twelve fenced blocks, of which two are
templates carrying placeholders and no output — failure 2's second part, whose command
names `<probe_script>` and `<the pre-stated quantity>`, and failure 4's first part,
which sweeps `<the text>.md`. Ten blocks print an output.

```
$ grep -n '^```' docs/known-failure-modes.md | awk 'NR%2==1{s=$0} NR%2==0{print s" -> "$0}'
117:``` -> 125:```
133:``` -> 141:```
154:``` -> 164:```
209:``` -> 223:```
236:``` -> 239:```
308:``` -> 335:```
359:``` -> 382:```
405:``` -> 414:```
454:``` -> 457:```
475:``` -> 502:```
520:``` -> 523:```
533:``` -> 543:```
```

**All ten reproduce.** I did not judge this by eye either. For each block I cut the
printed output lines out of the document into one file, ran the command above them
and captured the live output into another, and compared the two byte for byte. `diff`
printed nothing in every case, which is what `diff` does when two files are the same.
I then repeated the comparison with `cmp`, which reports the first differing byte, as
a second opinion on the first:

```
$ for f in doc1 doc2 doc3 doc4 doc6 doc7 doc8 doc10 doc11 doc12; do n=${f#doc}; if cmp -s /tmp/kfc/$f.txt /tmp/kfc/live$n.txt; then echo "block $n: byte-identical"; else echo "block $n: DIFFERS"; fi; done
block 1: byte-identical
block 2: byte-identical
block 3: byte-identical
block 4: byte-identical
block 6: byte-identical
block 7: byte-identical
block 8: byte-identical
block 10: byte-identical
block 11: byte-identical
block 12: byte-identical
```

The ten commands and what they returned live:

**Failure 1, first part, the denominator at the measured ceiling** (document lines
117–125) — `primary battery: denominator 1 - ceiling = 0.7079` and `control battery:
denominator 1 - ceiling = 0.0000`.

**Failure 1, first part, the same command fed the ceilings as they were actually
registered** (lines 133–141, new in this repair) — `0.7079` and `0.6773`.

**Failure 1, second part, the top of the scale** (lines 154–164) — `0.861`, `0.792`,
`0.643`.

**Failure 2, first part, the search for a sentence naming the route** (lines 209–223,
new in this repair):

```
$ python3 -c "
import re
pattern = r'route to the states|carried by the token|forced by the loss|is the input token'
base = 'experiments/06-mvm-0a-constructed-self-index/'
for f in ('position-sweep-method.md', 'powered-target-test-method.md'):
    lines = [l.strip() for l in open(base + f) if re.search(pattern, l, re.I)]
    print(f'{f}: {len(lines)} route sentence(s)')
    for l in lines:
        print('   ' + l)
"
position-sweep-method.md: 0 route sentence(s)
powered-target-test-method.md: 1 route sentence(s)
   the marker position**, where it is the input token. It must clear three
```

**Failure 3, first part, the count in each pre-stated cell** (lines 308–335, rewritten
in this repair):

```
donor dictates the same answer: 0 trials
donor dictates a different answer: 1200 trials
```

**Failure 3, second part, the widened read of the generator** (lines 359–382, widened
in this repair) — twenty-one lines across the two generator files, reproduced exactly,
line numbers and source indentation included.

**Failure 3, third part, the threshold at both ends of its range** (lines 405–414) —
`0.0071`, `0.0286`, `0.0571`, `0.1071`, including the two spaces the padding puts
after `0.95`.

**Failure 4, first part, the three sweeps compared on six claims** (lines 475–502, new
in this repair) — the six-row table, reproduced exactly including the column padding
and the truncation of each sentence at forty-eight characters.

**Failure 4, second part, the attack sweep read for the control battery** (lines
520–523) — `0`. This is the one that exits with status 1 while printing the right
answer, which the repair now warns about beside it.

**Failure 4, second part, the key counts in the endpoint records** (lines 533–543) —
`15`, `15`, `7`.

**Plainly: the file's claim about its own outputs is true, and true to the byte.**
There is no third unreproducible measurement. The column padding, the source
indentation and the trailing spaces are all covered, because a byte comparison covers
them, and those are exactly where a hand-copied output drifts. **MEASURED.**

One thing the claim does not cover, and does not pretend to: two of the twelve blocks
print nothing, so nothing about them was checked by anyone. One of those two is the
subject of `RT-199` below.

---

## 2. `RT-189` is closed: ruling item 3 has landed, in three places that agree — MEASURED and ARGUED

The earlier check's one fatal finding was that item 3 of the 2026-09-21 ruling —
reviewer-owned verification at every registration gate, whether or not a fatal finding
exists — was recorded as landed and had not landed. It is now in the file.

```
$ grep -n -i "whether or not a fatal finding\|whether or not anything fatal" docs/outside-review-protocol.md
80:measured check, whether or not anything fatal was found. No Gate A pass opens until the measurement
358:owns it at every Gate A, whether or not a fatal finding exists. Where fatal
```

**Against what the ruling actually says.** The ruling's item 3 reads: "**Reviewer-owned
verification runs at every Gate A**, whether or not a fatal finding exists — not only
on the closure of a fatal finding. **This extends item 6 of the 2026-09-20 ruling**,
which named fatal closures only."

The three landing points, in the file:

1. *The registration gate's own entry* (lines 79–80): "Every Gate A also carries the tier 1
   reviewer's own measured check, whether or not anything fatal was found."
2. *The paragraph describing the first tier* (lines 357–362): the reviewer "owns it at
   every Gate A, whether or not a fatal finding exists. Where fatal findings exist,
   that verification covers their closures... Where none exists, the verification is
   still owed, as at least one decisive measured check on the text being registered."
3. *A new bullet in the closure rule* (lines 417–427): "**A Gate A with nothing fatal in
   it still owes that check.** The reviewer-owned verification runs at every Gate A,
   whether or not a fatal finding exists... A pass that found nothing fatal is still a
   pass that has to have run something."

**Plainly: the wording matches the ruling and the three places agree with each other.**
Two of the three carry the ruling's own phrase verbatim; the third says the same thing
in plainer words ("whether or not anything fatal was found"), which is a paraphrase in
the direction the workspace rule asks for and not a drift. All three say the check is
the first-tier reviewer's, all three say it is owed when nothing fatal was found, and
the two that give detail agree on what it is — at least one decisive measured check on
the text being registered, filed with the command, the output and a plain sentence.

I looked for the seam a landing in three places usually opens, which is one place
being stricter than another. There is none. The gate entry states the requirement
flatly with no escape hatch; the closure-rule bullet adds one ("If the reviewer cannot
run any such check, the reason goes on the record and the gate does not open on the
strength of reading alone"), and that escape hatch does not weaken the flat statement,
because its consequence is that the gate stays shut. The first-tier paragraph's
version matches both. **ARGUED**, by reading the three passages against the ruling and
against each other.

The repair also records what happened in the protocol's own amendments section: that
the ruling exists, that the record said it had landed, that it had not, and what is
now in force. That entry is accurate against everything I checked.

---

## 3. Does each repaired test now fail on the design it was written from?

The standard is the document's own, on its last page: "A test that has never been seen
to fail has not been shown to detect anything."

### 3.1 Failure 2, the unrecoverable probe target — the one that mattered

**The new middle limb is right, and the record contains the numbers that fire it.
MEASURED.**

The old criterion was "it fails if the second run does not clear the bar", where the
second run is on a quantity the input guarantees. The earlier check's objection was
that this looks only at the instrument, and the instrument was fine, so the test passed
on the design that produced the failure. The repair adds a middle limb: **"The second
run clears the bar and the first does not."**

I went to the record the entry is written from and asked whether that pattern is
actually there. It is, in the diagnosis table of the position sweep's findings:

```
$ grep -nE "own_slot.*what the stack asks for|marker_token.*the input token itself" experiments/06-mvm-0a-constructed-self-index/position-sweep-findings.md
120:| `own_slot` — what the stack asks for | 0.293 (+1.60) | 0.273 (+0.88) | 0.243 (−0.24) | 0.283 (+1.33) | 0.275 (+0.91) |
122:| `marker_token` — the input token itself | **0.550 (+51.6)** | 0.513 (+43.1) | 0.510 (+41.3) | 0.498 (+41.9) | 0.490 (+40.8) |
```

**Plainly: that is the middle limb, in the numbers, at the same position, on the same
instrument.** The pre-stated target — the generator's index for whichever agent the
model is playing — clears nothing at any layer. The quantity the input guarantees, the
model's own marker word, decodes at fifty-one and a half standard deviations at the
same place. First run empty, second run clearing enormously. The findings file draws
exactly the conclusion the new limb draws: "The read works... The sweep's machinery was
never the problem" and "The target is unreadable." So the middle limb is not a guess
about what would have shown the failure; it is the shape the failure actually had. The
repair's central judgement is sound, and the old limb is correctly demoted to third and
correctly scoped to a broken pipeline.

**But the limb itself has never been run, and the document does not say so.** See
`RT-199` below. Running it needs a probe pipeline executed twice against model
checkpoints, which costs compute; I did not run it and I am not asking for it to be
run.

**`RT-198` — the first part's route-sentence search is a proxy for a detector, and the
entry does not say so — MEASURED and ARGUED — worth-noting.**

The first part is repaired from paper and pencil into a command, and on its face it
works: run against the method document committed before the sweep that spent weeks on
an unrecoverable target, it returns zero route sentences; run against the method for
the target that turned out to be recoverable, it returns one, and the sentence it
returns names the token. That is a real result and it does fail on the design that
produced the failure.

The trouble is what a count of zero means. I ran the same fixed pattern across every
method document in this experiment:

```
$ python3 -c "
import re, glob, os
pattern = r'route to the states|carried by the token|forced by the loss|is the input token'
for f in sorted(glob.glob('experiments/06-mvm-0a-constructed-self-index/*method*.md')):
    lines=[l.strip() for l in open(f) if re.search(pattern,l,re.I)]
    print(f'{os.path.basename(f):45s} {len(lines)}')
"
ceiling-measurement-method.md                 0
denoised-direction-method.md                  0
fitted-position-sweep-method.md               0
other-index-position-sweep-method.md          2
position-sweep-method.md                      0
powered-position-sweep-method.md              0
powered-target-test-method.md                 1
reap-shutdown-order-method.md                 0
standardised-refit-method.md                  0
```

Seven of nine return zero. One of those seven is the method for the powered
eleven-position sweep, and that document does exactly what the test asks for — it names
the route in its own words, at length:

> **Position 6 is the positive control.** The model's own marker word sits there as an
> input token... **Position 1 is a negative control, and this is new.** At the value
> token of the model's *first* own turn, the model's own marker **has not yet appeared
> anywhere in the episode**... So the target is not determinable from anything the model
> has seen.

That is a route sentence and a no-route sentence, stated in advance, for two positions.
The fixed pattern scores it zero.

**Plainly: run with the wording it is printed with, this test flags documents that
satisfy it.** The entry anticipates this and says "Run this on a new design's method
document with that design's own wording in the pattern" — but that instruction is what
makes it a proxy rather than a detector. A session that writes the pattern out of the
wording it has just read will match by construction, and a session that does not will
get a zero whether or not a route was named. What the command measures is not whether
a route exists; it is whether the checking session found a sentence it was willing to
call one, and it records that session's reading with a command attached. That is worth
having — it forces a specific sentence to exist and be quoted into the filed output,
which is more than paper and pencil gave — but it is not what the surrounding text
implies when it says "a count of zero is the finding".

The concrete gap is that the entry does not say any of this. The other two repaired
tests each carry a plainly headed paragraph saying what they cannot see — failure 3's
second part has "**What this part cannot see, plainly**", failure 4's first part has
"**What part one still cannot catch, plainly**". Failure 2 has neither, and it is the
entry whose test most needs one.

```
$ grep -niE "cannot see|cannot catch|still cannot" docs/known-failure-modes.md
389:**What this part cannot see, plainly.** It is a text search, so it finds only
508:**What part one still cannot catch, plainly.** A claim of measurement written in
```

### 3.2 `RT-199` — the list says every repaired test is printed with an output showing it failing; failure 2's second part is neither printed nor run — MEASURED — **serious**

The block the repair adds at the top of the file says, at lines 52–54:

> Those three were repaired on 2026-09-21 by a third session, which is the session that
> wrote this paragraph, and every repaired test is printed below with the command and
> the output showing it failing on the design it was written from.

Failure 2's second part is a repaired test. Its criterion was rewritten from one limb
into three, and the repairing session's own commit message calls the new middle limb
"the important one" and "the pattern this entry exists to catch". It is printed as a
template with placeholders and no output:

```
$ python3 src/<probe_script>.py --target <the pre-stated quantity> --report margins
$ python3 src/<probe_script>.py --target <a quantity the input guarantees> --report margins
```

No command was run for it and no output is printed. It has never been seen to fail. And
the document nowhere admits this:

```
$ grep -niE "placeholder|has not been run|never been run|not yet been run|cannot be run|needs compute|requires compute|not been seen to fail" docs/known-failure-modes.md
(no output; exit status 1, which is what grep does when nothing matches)
```

**Plainly: a sentence in this document claims something about this document that this
document does not support.** That is failure 4 on its own list, in the block whose
whole purpose is to state honestly what the list has and has not been shown to be. The
commit message does say, obliquely, that "two blocks are templates with placeholders
and no printed output, and are skipped" — but that is in the commit message, about the
reproduction check, and a reader of the file will not see it.

I want to be exact about how far this goes, because the repair's substance is good and
I do not want to inflate this. The middle limb is right (section 3.1). The gap is the
blanket sentence, which covers more than was done. The honest version is available at
no cost: the numbers that fire the middle limb are in the position sweep's findings
file and I printed them above, so the entry could show the limb failing on the design
it was written from without launching anything.

A narrower reading rescues the sentence — that "every repaired test" means the one part
of each repaired entry that carries the detection, and for failure 2 that is the first
part, which is printed. But the document itself says of failure 2 "the first one is the
one that catches this failure" while the commit message says the middle limb of the
second part is the point of the repair, so the two do not settle on which part is the
test. Under either reading, a reader is owed the sentence that says the middle limb has
never been executed.

### 3.3 Failure 3, the empty cell — runs, returns zero, and is not vacuously zero — MEASURED

The earlier check's `RT-191` was that this test did not execute at all: it imported a
module that does not exist, called a function that does not exist, and used two names
that were never defined. **It runs now**, and it returns zero in the first pre-stated
cell, which is the finding:

```
donor dictates the same answer: 0 trials
donor dictates a different answer: 1200 trials
```

A zero from a test that has just been rewritten deserves one more question: is the zero
the design, or is it the harness quietly counting nothing? So I ran a control. The
distinctness rule that empties the cell binds *within* a contested item — four distinct
values, one per agent. It does not bind across items. So I ran the same harness
unchanged except for comparing the donor's value against the recipient's value on a
*different* item. If the harness can ever put a trial in the first cell, it must do so
there:

```
$ python3 -c "
import sys; sys.path.insert(0, 'experiments/06-mvm-0a-constructed-self-index/src')
import curriculum_a3 as design
eps = design.generate_balanced(200, seed=0)
same = diff = 0
for ep in eps:
    items = list(ep.contested)
    for i, item in enumerate(items):
        other = items[(i + 1) % len(items)]
        v, w = ep.values[item], ep.values[other]
        for donor in range(design.N_AGENTS):
            if donor != ep.own_slot:
                if v[donor] == w[ep.own_slot]: same += 1
                else: diff += 1
print('CONTROL, donor vs recipient on a different item:')
print('  donor dictates the same answer:', same, 'trials')
print('  donor dictates a different answer:', diff, 'trials')
"
CONTROL, donor vs recipient on a different item:
  donor dictates the same answer: 137 trials
  donor dictates a different answer: 1063 trials
```

**Plainly: the harness puts trials in the first cell when the design allows it, and
none when the design forbids it.** One hundred and thirty-seven against zero, on the
same twelve hundred pairs, changing nothing but which item the recipient's value is
read from. So the zero is a property of the registered grammar and not an artifact of
a freshly written test. This is the strongest of the three repairs: it runs, it fails
on the design that produced the finding, and it has now been shown to be capable of
passing. `RT-191` is closed.

Two small things, neither a finding against the substance. The document says "**Three
lines** belong to the design being checked and are meant to be replaced" and then lists
four things — the module imported, the list of cells, and *two* small functions —
spanning fourteen lines of the block, not three. And the second part's widened read is
what the repair says it is: twenty-one lines across both generator files where the old
pattern returned five from one file, with an honest paragraph naming what a text search
still cannot see. `RT-203` below covers the count.

### 3.4 Failure 1, the zero denominator — the "display" label is honest — ARGUED

The earlier check's `RT-194` was that the first part passes on the design as registered
and so is a display rather than a detector. The repair agrees in the document's own
words, in bold: "**Part one is a display and not a detector; part two below is what
does the detecting.**" It then prints the failure passing its own test — the same
command fed the ceilings as they were actually registered on 2026-09-15, returning two
healthy denominators — and says so: "That is the failure passing its own test." Both
blocks reproduce.

**Plainly: yes, that is honest.** A test that cannot detect is not made into a detector
by being relabelled, and the repair does not pretend otherwise; it moves the claim of
detection onto the second part, which the earlier check called the best test in the
document and which I confirmed reproduces. The new criterion — "it fails if any ceiling
typed into it cannot be traced to a committed measurement record", named by file — is a
real criterion and it is the right one, because the original failure was a ceiling
nobody had measured being typed in as though it had been.

One limit, worth saying and not a finding: that criterion is applied by the reader to
the inputs, not by the command to anything. The command's output cannot show it being
met or missed. So under the failure-mode pass's rule that "every disposition shows its
work: the command that was run and the output it returned", failure 1's first part
produces the thinnest disposition on the list — two printed numbers plus a prose claim
about where they came from. The entry is clear that the detection lives in the second
part, so nothing is being smuggled; it is simply the one place where the pass's
evidence is a sentence rather than an output.

### 3.5 Failure 4, the uncited measurement — the widened list does what is claimed — MEASURED

The repair claims the widened word list catches five of six claims where the old list
caught none, with a separate number sweep for the sixth. The printed comparison
reproduces byte for byte (section 1). But that block tests six sentences typed into the
command, so I checked the thing the earlier check's `RT-193` was actually about: whether
the widened list now catches this document's own headline claim of measurement, in the
document, where the old list missed it.

```
$ grep -n -E "verified|measured|calibrated|attacked|reproduc|confirmed|ran" docs/known-failure-modes.md | grep -c "^34:"
0

$ grep -n -iE "verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result" docs/known-failure-modes.md | grep "^34:"
34:Every output printed below was produced by running the command printed above it,
```

**Plainly: the old seven-word list does not find line 34 and the widened list does.**
That is the defect `RT-193` named, fixed and demonstrated on the real file rather than
on a copy of the sentence. The entry also adds the number sweep for a bare figure
offered as a result with no verb, which the printed block shows is the only one of the
three that finds "Control battery ceiling: 0.3227." And it carries an honest paragraph
naming what neither sweep can do, including that they cannot tell a claim from a
quotation of one. `RT-193` is closed.

### 3.6 Where the four tests now stand

| failure | does its test fail on the design it was written from? | shown, or argued? |
|---|---|---|
| 1. Zero denominator | Second part yes, as before. First part no, and the document now says so in bold and gives it a provenance criterion instead | Shown for the second part; the first part's criterion is a reading rule with no output |
| 2. Unrecoverable probe target | First part yes, with a command and an output — but the count it returns depends on the wording chosen (`RT-198`). Second part's middle limb is the right pattern and the record contains the numbers that fire it, but it has never been executed and the file does not say so (`RT-199`) | First part shown; middle limb argued from the record, not run |
| 3. Cell empty by construction | Yes. It runs, returns zero in the first pre-stated cell, and a control returns 137 in that cell when the design allows it | Shown, and shown to be capable of passing |
| 4. Claim of measurement with no record | Yes, and now on the newest form — the document's own headline claim, which I confirmed in the file itself | Shown |

---

## 4. `RT-200` — the ruling file still says item 3 landed via pull request 13, and the line that says it is not John's ruling — ARGUED — **serious**

This is the question of whether the repair was right to leave the ruling file alone.

**What the repair says.** "The ruling file is not edited. It is a record of what John
ruled, and what is wrong in it is a claim about where the text landed, which the
amendments entry answers." The same reasoning is in the protocol's amendments entry.

**The principle is right.** A session does not rewrite what John ruled, and a session
that discovers the ruling's text never reached the file fixes the file, not the ruling.
The repair did that, correctly, and recorded it.

**But it is applied to the wrong part of the file.** I opened the ruling and looked at
where the wrong sentence actually sits. It is not among the twenty ruled items. It is
the third bullet of a closing section headed "## Recorded elsewhere":

```
$ grep -n "pull request 13\|landed via" docs/rulings/2026-09-21-review-verification-and-staged-spending.md
222:- `docs/outside-review-protocol.md`: items 3 to 8, landed via pull request 13.
```

That section is a list of pointers written by the session that recorded the ruling,
saying where each item was landed — the worklog entry, the protocol file, the successor
proposal's section 12, the project configuration file. It is bookkeeping. John ruled
the twenty items; he did not rule that they landed in pull request 13, and the file
itself says the wording throughout is the session's, recorded as mixed authorship
because he approved a recommendation the session put to him.

**And nothing in the ruling file points at the correction:**

```
$ grep -niE "b4e3e84|did not land|amendments entry|corrected" docs/rulings/2026-09-21-review-verification-and-staged-spending.md
84:16. **The stale spend figures are corrected to the compute ledger**, which is the
```

The only hit is an unrelated ruled item about spend figures. So a reader who opens the
ruling — which is the document a future session opens to find out what is in force —
is still told that item 3 is live in the protocol by way of pull request 13, with no
signpost to the amendments entry that says otherwise. The correction lives only in the
document that was wrong, and not in the document that makes the false claim.

**My answer: a ruling that is wrong about where its own text landed needs an
annotation, and adding one is not editing the ruling.** Three reasons.

First, the sentence is precisely what this programme's fourth known failure is about —
a claim about a committed record that the record does not support — and the protocol's
own closure rule requires a sentence claiming something is somewhere to point at a
record that contains it. The ruling file has been failing that test since it was
written, and after this repair it still fails it. The protocol now polices this in every
registration text while a governing ruling carries an instance of it.

Second, the harm is live and one-directional. The repair's own finding is that "for as
long as the ruling has existed, every session reading this file has applied the narrow
rule while the ruling file said the wide one was in force." Landing the text fixes what
sessions reading the *protocol* will do. It does nothing for a session reading the
*ruling*, which will now be told the text landed somewhere it did not, and which — if
it goes looking in pull request 13 to check — will find the narrow wording and conclude
the widening was reverted.

Third, the remedy does not touch a ruled item. A dated note appended under "Recorded
elsewhere", marked as a later session's correction and not as part of the ruling,
saying that item 3 did not land in pull request 13 and naming the commit that landed
it, changes no ruling and removes the false pointer. That is the same act as the
amendments entry the repair already wrote, performed in the file where the error is.

**What I would not do, and why this is a finding and not a demand.** Whether a session
may annotate a ruling file at all is John's call, not mine and not the repairing
session's, and the repairing session was right to stop rather than guess. So the finding
is not "the repair should have edited the ruling". It is that leaving the file with no
pointer is not a resting place, and the open question should be put to John rather than
closed by silence. As it stands the record contains a correction that only a reader who
already knows about it can find.

---

## 5. `RT-201` — is the filing rule followable as written? — MEASURED and ARGUED — worth-noting

The earlier check's `RT-192` was that the filing rule named four commits as already
carrying commands and outputs, and none carried one. The repair removes them and names
two that do. I counted, in the same way, over all seven commits involved:

```
$ grep -cE '^\s*\$ |^\s*(git|python3?|grep|wc|sed|awk|diff|md5|shasum) ' /tmp/kfc/m1.txt ... /tmp/kfc/m7.txt
/tmp/kfc/m1.txt:0      e8dad42  the outside-reviewer packet rebuild
/tmp/kfc/m2.txt:0      9653275  the roadmap conversion
/tmp/kfc/m3.txt:0      49c1002  the launch-step split
/tmp/kfc/m4.txt:0      184a42f  the second packet rebuild
/tmp/kfc/m5.txt:3      9393b92  the commit that wrote the pairing rule
/tmp/kfc/m6.txt:2      b4e3e84  the commit that landed the widened verification
/tmp/kfc/m7.txt:6      dceeafa  the commit that repaired the tests
```

*(`grep` prints these rows in whatever order it finishes the files in; I have put them
back in the order of the file list and added the right-hand column saying which commit
each file holds. The counts are untouched. Each file holds the full message of one
commit, saved with `git log -1 --format=%B`.)*

**Plainly: the four removed precedents carry no command line between them, and the two
named in their place carry three and two.** The repair's claim is true and the
correction is complete. The document also says out loud that both replacements are off
the main line rather than leaving a reader to discover it.

I also checked the thin spot the repair names honestly. Its commit message says: "No
commit in the last sixty on the main line carries a command line in its message, which
is why the replacement names none." That claim is in prose and was never printed with a
command, so I ran one.

A complication first, recorded because it changes which sixty commits are meant. **The
main line moved under me while I worked**: another session pushed during this check, so
`origin/main` advanced from `73aa7e3` — the commit titled "Merge pull request #22 from
jfredson/worktree-agent-a023ba493bc2e40c5", which was the tip when the repair was
written — to `2ad356a`. Twenty commits arrived in between, so the last sixty from the
later tip are a third different from the repair's last sixty. I ran the count both ways.

```
$ git rev-list --count 73aa7e3..2ad356a
20

$ git log -60 --format=%B origin/main > /tmp/kfc/main60msgs.txt        # the later tip
$ grep -cE '^\s*\$ |^\s*(git|python3?|grep|wc|sed|awk|diff|md5|shasum) ' /tmp/kfc/main60msgs.txt
0

$ git log -60 --format=%B 73aa7e3 > /tmp/kfc/main60at-repair.txt       # the tip when the repair was written
$ grep -cE '^\s*\$ |^\s*(git|python3?|grep|wc|sed|awk|diff|md5|shasum) ' /tmp/kfc/main60at-repair.txt
1
```

**Plainly: the claim is true in substance, and the count as stated does not reproduce.**
Against the sixty commits the repair was actually talking about, the same counting
pattern the repair used on the four discarded precedents returns one, not zero. I opened
the hit rather than reporting the number:

```
$ grep -nE '^\s*\$ |^\s*(git|python3?|grep|wc|sed|awk|diff|md5|shasum) ' /tmp/kfc/main60at-repair.txt
1063:                                    md5 359fabbb4815e8df3cba8e38fd530248
```

```
  a3ctl_30m_seed0_train.log         the run's own console log, 116 lines,
                                    md5 359fabbb4815e8df3cba8e38fd530248
  a3ctl_30m_seed0_trajectory.jsonl  111 evaluation records, step 500 to
                                    55,116, md5 2b149ecdf1c789edfa042d31f2cd66a4
```

That is not a command. It is the wrapped second column of a two-column table listing two
files and their checksums, and the pattern matched it only because the continuation line
happens to begin with the word `md5`. So no main-line commit in that sixty carries a
command line, which is what the repair says, and the number it would have printed had it
printed one is 1 rather than 0.

**Why I am filing this rather than waving it through.** In itself it is nothing: a
counting pattern picked up a checksum. But the repair discarded four named precedents on
the strength of this same pattern returning zero for each, and it asserted the
sixty-commit result in prose without running it where a reader could see. The document
beside it requires every claim of measurement to point at a record, and this is a claim
of measurement — "it scanned sixty commits and found none" — whose stated result is off
by one when reproduced. The substance is safe and the discarding of the four precedents
is unaffected; I confirmed those separately and directly above. **MEASURED.**

**Is the rule followable as written? Yes.** This is the judgement I was asked for, and
I want to separate two things the thin spot runs together. A rule is followable when it
says what to produce, not when someone has already produced it. The rule says: file the
check under the reviews directory of the experiment the document most affects, with an
opening line saying why it is filed there; then the commit that acts on the check
carries the commands and their outputs in its message, and names the commit it checked.
Every part of that is a concrete instruction I was able to carry out without asking
anyone what it meant — this file is the evidence, and it was written from the rule and
not from the examples. The absence of a main-line model makes the rule *unillustrated*,
not unfollowable.

Two real limits, which is why this is filed rather than waved through.

*The examples are perishable.* Both named records sit on session branches. The repair
applied the earlier check's `RT-195` lesson and cited them by commit rather than by
branch, which is the durable anchor and is the right fix — a branch is deleted after
merge and takes the signpost with it, whereas a commit identifier survives the merge.
But a commit on a branch that is *abandoned* rather than merged becomes unreachable and
is eventually collected. If this repair branch never lands, the filing rule's only two
examples evaporate and the rule is back to being unillustrated. Nothing in the text
says so.

*"Both are on the repair branch"* is true in the sense that both are ancestors of its
tip, which I confirmed, though the commit that wrote the pairing rule was made on a
different session's branch and merged in. Not wrong; slightly compressed.

For completeness on `RT-195` itself: the failure list now names the review at `3bbfece`
and the proposal it reviews at `d8ceba9`, both by commit with the commit's title
attached, and hedges that neither had reached the shared main line when it was written.
That hedge was correct when written — neither was an ancestor of the main line as it
then stood — and has since been overtaken: both are now on the main line. The sentence
is dated by its own words, so it has not become false, only stale. `RT-195` is closed.

---

## 6. Internal consistency and the plain-language rule

**No contradiction found across the four sections and the failure list. ARGUED.** I read
the pairing rule, the section refusing to trade isolation for speed, the failure-mode
pass and the rebuild rule against the gates, the two tiers, the rehearsal, the closure
rule and the filing section, looking for two rules that disagree about who owns what or
about what must be filed. The three seams the earlier check named are all closed and
none opened in their place:

- *The filing fallback that could not be followed.* Now replaced. The rule says where
  such a check goes and the paragraph beside it explains, in plain words, why the
  original rule was impossible: text is not binding until committed, and by then the
  message that was supposed to hold the check is written. Closed.
- *"Registration text" narrower than the registration gate.* Now stated: "**'Registration
  text' below means every kind of text Gate A covers**", with the gate's own four kinds
  listed and the reason a session in a hurry would take the narrow reading. Closed.
- *The two labels used before they were defined.* MEASURED and ARGUED are now given their
  plain meanings at line 118, where a reader meets them first, with a sentence saying
  they are defined again where the first tier is described. Closed.

One seam I checked and cleared on my own account: the failure-mode pass now requires
every failure on the list to be run against every registration text, and failure 2's
second part needs a probe pipeline run twice, which costs compute. That could have made
the pass unaffordable. It does not, for two reasons the text gives: that part is
explicitly "run in the rehearsal", which is a run the protocol already requires before
a gate opens, and the pass carries an escape hatch — "A failure that genuinely cannot be
tested on this design gets the reason on the record and stays open." Consistent.

**The plain-language rule is largely kept, and the repair closed the breaches the
earlier check named.** "The eleven edits that got it there" is now "every edit that got
it there", and the amendments entry gives the reason plainly: nothing produced the
eleven, and a made-up number in the argument for requiring that numbers come from
somewhere is not an argument. The cost paragraph no longer rests on two uncounted rates;
it now separates what is evidenced (the same defect twice, six days apart, the second in
a design written by a session holding the first) from what is not (that catching has got
faster), and says of the second that "nothing in this repository would settle" it. Every
finding number in both files carries a plain phrase saying what it is.

Two small breaches the repair introduced, both of the kind it was fixing.

**`RT-202` — four bare commit identifiers in a list — MEASURED — worth-noting.** The
protocol's amendments entry reads: "Counting lines that look like a command in the
messages of `e8dad42`, `9653275`, `49c1002` and `184a42f` returns zero for each." Four
identifiers, no phrase on any of them. The workspace rule is explicit that this applies
"inside lists and source appendices too, which is exactly where bare ids are most
tempting and least useful", and that John cannot hold identifiers in his head. The
sentence two lines above does describe them collectively as "four commits said to carry
commands and outputs", and the pairing-rule section names them in words elsewhere ("the
two outside-reviewer packet rebuilds, the roadmap conversion and the launch-step
split"), so a determined reader can reconstruct which is which — but not from the list.
Every other identifier in both files carries its phrase, which is why this one stands
out.

**`RT-203` — a count that does not match what it counts — MEASURED — worth-noting.**
Failure 3's first part says "**Three lines** belong to the design being checked and are
meant to be replaced", then names four things — the module imported, the list of
pre-stated cells, and two functions — which together span fourteen lines of the block,
because one of the two functions is seven lines on its own. "Three things" would be
right. Trivial in itself, and in any other document I would not file it; in this one the
neighbouring argument is that an invented count in a document about counts is not an
argument, and this is a count that does not survive being counted.

**One cosmetic defect the repair introduced, which matters only because of where this
file goes.** The sentence landing ruling item 3 in the registration gate's entry was
inserted without re-wrapping the paragraph:

```
$ awk 'length>84 {print NR": len="length}' docs/outside-review-protocol.md
80: len=99
523: len=133
564: len=85
699: len=106
729: len=85
```

Line 80 is ninety-nine characters in a paragraph otherwise wrapped at about seventy-eight,
and the change that made it is in this repair. The other four are a long heading, two
file paths and one line five characters over. The earlier check filed a ragged line
break under `RT-197` on the ground that this file goes to outside reviewers verbatim; the
repair fixed that one and left a new one of the same kind. Not a finding — I am recording
it so the session that fixes the two findings above can reflow the line in the same pass.

---

## Are the protocol and the failure list now fit to be adopted?

**The protocol: yes, and more so than before the repair.** The four rules were already
judged adoptable by the earlier check and none of them was changed. What the repair
added is the ruling that should have been in the file since the day it was made, landed
in three places that agree with each other and with the ruling, plus the removal of a
precedent that did not exist, a filing rule that can actually be carried out, and a cost
argument that no longer claims a rate nobody counted. I found no contradiction with the
gates, the tiers, the brief, the rehearsal or the closure rule. The two small
plain-language breaches and the unwrapped line are worth fixing and are not reasons to
wait.

**The failure list: closer, and not yet.** What the list claims for itself is now nearly
right, and that is the important change — it says on its face that it is "a reliable
account of the past and an unproven instrument for the future", that the repairs are
owed a check, and that a clean pass from it is not evidence a design is clean. Every one
of its ten printed outputs reproduces to the byte. Failure 3's first test is now a real
detector and I have shown it both failing and capable of passing. Failure 4's word list
now catches the claim it used to miss, demonstrated in the file itself. Failure 1's first
part is honestly demoted to a display.

What stops me saying yes is failure 2, which is the entry that cost this programme the
most. Its repaired criterion is right — I found the pattern it names sitting in the
record it was written from, at fifty-one standard deviations against nothing — but the
limb carrying that judgement has never been executed, and the block at the top of the
file says every repaired test is printed with an output showing it failing. That is one
sentence overclaiming in the one document whose subject is sentences that overclaim, and
it is cheap to fix: the numbers are in the position sweep's findings file, and printing
them would turn the claim into the measurement it says it already is. The first part
needs, at minimum, the paragraph the other repaired tests have, saying that a count of
zero depends on the wording chosen and that seven of nine method documents in this
experiment return zero to the pattern as printed.

**So: adopt the protocol. Hold the failure list one more round — for `RT-199` and
`RT-198`, which are a paragraph and a printed block, not a redesign.** And put `RT-200`
to John, because whether a ruling file may carry a correcting annotation is his call and
not a session's, and until it is answered the ruling on the main line goes on telling
every reader that item 3 landed somewhere it did not.

**Nothing here is a fix.** I edited neither file under check, neither the ruling nor the
earlier check. Nothing was pushed to the main line, nothing merged into it, no pull
request opened, no compute launched and no money spent.

---

*Filed under the outside-review protocol's filing rule
(`experiments/<experiment>/reviews/YYYY-MM-DD-<target>-<reviewer>.md`), verbatim, not to
be edited after filing. The fixes belong to a different session, and the check on those
fixes to a fourth.*
