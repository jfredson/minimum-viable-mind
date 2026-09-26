# Tier 1 check of the Amendment A3 closure text, version 5: the closure rule's reviewer-owned check

*Filed 2026-09-25 (Pacific) by a Claude Code session in its own worktree
(`worktree-a3-closure-v5-tier1-check`, branched from the main line at commit
`4d98cfc`). The target is version 5 of the closure text for Amendment A3, the
third registered design change to the first constructed self-index experiment:
`docs/a3-closure-text-draft-2026-09-25-v5.md` as it stands at commit `432e966`
on branch `worktree-a3-closure-v5` (pull request 43), together with the two
proposed annotations that commit adds (`docs/proposed-annotation-rt164-2026-09-25.md`
and `docs/proposed-annotation-chatgpt-review-2026-09-25.md`). The three files
were read with `git show 432e966:<path>`; that commit adds exactly those three
files and changes nothing else (`git show --stat 432e966`: 3 files changed, 405
insertions).*

*This is the check that item 22 of John's ruling of 2026-09-25
(`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`) and the closure
rule (`docs/outside-review-protocol.md`, "The closure rule, which is the new
part") require before version 5 is appended to `amendment-a3.md` as the
registration commit. This session did not write version 5, the ruling, the
dispositions proposal, either outside review, or the check of the dispositions.
It has not seen the writing session's chat.*

*What was opened: the files named in "Sources" at the end, and nothing else.
What was not opened: the worktree folder of the version 5 branch, the tier 2
packets, versions 1 to 3 of the closure text, and any session chat. No machine
was launched, nothing was rented, nothing was spent, and no web lookup was made.
Nothing was edited: version 5, the ruling, the ledgers, the reviews, the
protocol and the known-failure list are untouched. A copy of version 5 was
placed in this worktree for the two repository scripts that only read files
inside the repository, and deleted straight after (the `ls` that follows each
run in section 4 confirms it is gone).*

*Written under the workspace plain-language rule. Every finding is labelled
MEASURED (a command was run and its output is reported) or ARGUED (reasoning a
reader can dispute). Severity is fatal, serious or minor. Finding numbers
continue from RT-204, as item 21 of the ruling instructs; see the note on
numbering in section 6. `E/` is short for
`experiments/06-mvm-0a-constructed-self-index/`.*

---

## The answer in five lines

1. **Every ruled item (1, 2, 5 to 9, 11, 12, 14 to 19) is applied as the ruling
   states it and nowhere wider.** A sentence-level diff of the version 4 block
   against the version 5 block gives nine changed hunks, and every sentence in
   them is either a ruled change or a plain-language gloss the version 5
   change table declares (with one undeclared gloss, RT-208, minor). Where the
   ruling adopts a reviewer's wording, version 5 carries it word for word; the
   only differences are line wrapping and straight quotation marks where the
   reviewer typed curly ones.
2. **Every number and quotation in the closure block is in the file it cites**,
   checked one by one (section 4, 82 lookups), with one exception: the count of
   135 tests per arm (RT-205, minor) is the cited file's 270 divided by its two
   arms, and is written out only in the sweep's method file and in the
   follow-up ruling. The money figures match the compute ledger as it reads
   today, whose last row is still dated 2026-09-21; the $450 ceiling matches
   page 6 of the Weekend 1 queue ruling, but the ledger itself still reads $400
   everywhere (RT-206, minor, an action on the ledger rather than on the text).
3. **Hard kill K5 is named, read as "not reached" in the ruling's words, and
   the reading is attributed to John.** The same-act limit the pre-registration
   requires of every write-up is present, in the reviewer's adopted sentence.
4. **All five known failure modes were run against version 5** (section 5).
   None fires on it; the one the text reports (the zero denominator) is
   reported as a failure that already happened, with its record cited, not
   reproduced.
5. **One serious finding, RT-204, and it is the gap the writer flagged.** The
   adopted schedule sentence cites the December-result ruling "including its
   2026-09-21 annotation" for what a missed kill date means, and that
   annotation does not carry item 23 of the ruling of 2026-09-21, under which a
   missed date no longer moves the roadmap to outcome R4 by itself and
   launching past one takes a fresh ruling. Registered text would point a
   reader at a superseded consequence. It is closable by one clause or by
   carrying it open, either on John's word. **Nothing fatal was found.**

**Closing line.** Version 5 at `432e966` may be appended to `amendment-a3.md`
as the registration commit under the closure rule **once John has ruled on
RT-204** (one clause added, or the item carried open in the text, with his
reason on record). Nothing else found stands in the way. Not as it stands;
yes with that one ruling.

---

## 1. Check (1): each ruled item, applied as ruled and nowhere wider

**Method.** The closure block of version 4 (`docs/a3-closure-text-draft-2026-09-21-v4.md`,
lines 53 to 234) and of version 5 (lines 43 to 280 of the file at `432e966`)
were split into sentences and diffed (`sentdiff.py`, a 25-line script; its
full output is reproduced in the appendix). Then every reviewer sentence the
ruling adopts was searched for in version 5, both byte for byte and after
collapsing whitespace and mapping curly quotes to straight ones (`verbatim.py`;
output in the appendix).

**Result of the diff, MEASURED.** 46 sentences in version 4's block, 79 in
version 5's, nine changed hunks. Each hunk, and the ruling item that
authorises every sentence in it:

| Hunk | What changed | Ruling item(s) | Anything wider? |
|---|---|---|---|
| 1 | Headline replaced; "That bin did not fire…" replaced; "any lesion" narrowed to "the input-channel lesion, the only lesion A3 ran" | 16, 19(a), 5 | No |
| 2 | Structural sentence carries the restriction "any control fully determined by the visible episode and not requiring ownership"; "was itself never attacked" becomes "had not been attacked before registration"; "at quadrupled weight" becomes "per-row gradient weight quadrupled" | 11 (main point), 19(b), 6 | No. ChatGPT's main A6 replacement paragraph ("John applied the registered loss condition…") is correctly **absent**, since the ruling adopted only the restriction and the successor sentence (`verbatim.py`: "A6 main replacement NOT adopted (should be absent)": False) |
| 3 | Successor sentence added; state drops given for all three seeds; "All six scores" becomes "The six primary-battery scores" | 11 (successor sentence), 19(c) | No |
| 4 | Refit sentence replaced with ChatGPT's 19(e) sentence, cited to the dispositions check, with glosses for "folds" and "permutation draws"; margin given as 0.000484 with the ledger cited; confound sentence bounded in the ruling's words; relational-route sentence now cites RT-125 | 19(e), 19(d), 12 | No. ChatGPT's full A8 replacement ("did not support the proposed explanation…") is correctly absent, as item 12 declined it in favour of the narrower form |
| 5 | 270-test sentence replaced with ChatGPT's two sentences plus a gloss; "never converged" replaced; new K5 paragraph | 7, 2, 1 | One undeclared gloss on "causal patching" (RT-208, minor); otherwise no |
| 6 | One-in-eleven sentence replaced and scoped to the fitted register-index read; "a center that is known to be there" replaced; 19(f) sentence added; blind-arm sentences replaced | 18, 19(f), 14 | The "$0 side item" clause of version 4 goes with the replaced sentences (RT-209, minor, authorised by item 14) |
| 7 | ChatGPT's two gradient sentences and public sentence added; pre-registration's "every write-up" requirement cited by section; the attribution sentence | 17 | No |
| 8 | 2026-10-11 dropped; ChatGPT's schedule sentences | 9 | No wider than ruled, but see RT-204 |
| 9 | ChatGPT's open-decisions paragraph with both rulings cited by item; money paragraph rewritten | 15, 8 | No |

Version 4's wording that the ruling replaces survives only in version 5's
change table (lines 294, 296, 299 and 308 of the version 5 file, which quote
the old phrases to say what became of them), and nowhere in the block:

```
$ grep -n "2026-10-11\|never converged\|invalidated\|at quadrupled weight" <v5>
294:| 2 | Gemini G4, G6 | "Because the two instruments never converged on any seed" replaced …
296:| 6 | ChatGPT A1 | "at quadrupled weight" becomes "per-row gradient weight quadrupled". |
299:| 9 | ChatGPT A4 | The 2026-10-11 target is dropped. …
308:| 19(b) | ChatGPT A15 | "was itself never attacked" becomes "had not been attacked before registration", with no claim about what the later measurement invalidated. |
```

Items the ruling gives no text change (3, 4, 10, 13, 20, 21, 22) make no
change in the block, as the version 5 table says at lines 314 to 320. The one
ChatGPT suggestion the ruling did not adopt (the two reasons the crossing is
sub-bar, under A15) is absent from the block, as it should be.

**Result of the word-for-word check, MEASURED.** Of the 37 adopted reviewer
sentences and ruled phrases searched (`verbatim.py` output in the appendix),
every one is present after whitespace and quote normalisation. Fourteen are
also present byte for byte; the other 23 differ only because version 5 wraps
lines at about 80 characters and writes straight quotation marks where the
ChatGPT file has curly ones (for example the headline, item 16, and "Above
zero", item 17). Four of ChatGPT's A15 sentences were searched a second time
with the quotation marks their table wraps them in, which of course do not
appear in the block; 19(d) was confirmed without them, and 19(c), 19(e) and
19(f) were confirmed in the sentence diff, where each appears whole (appendix,
hunks 3, 4 and 6).

One item deserves a sentence. **Item 2** says "never converged" is "replaced by
Gemini's wording" and then gives that wording as "patching was never run, so
agreement could not be tested and no L1 subspace was ever localized". Gemini's
own G6 sentence reads "probe-patching convergence could not be tested … therefore,
the registered uncarvable signature H_diffuse…" (`E/reviews/2026-09-21-a3-closure-gemini.md`,
line 49). Version 5 carries the ruling's form, "agreement between probe and
patching could not be tested" (line 159), which is also the form the
dispositions proposal wrote as "near-verbatim" (`docs/rulings/2026-09-25-a3-closure-tier2-dispositions-PROPOSAL.md`,
item 2), and its change table says so ("in the ruling's words", line 294).
That is the ruled wording, applied as ruled. Not a finding.

## 2. Check (3): K5, and check (4): the same-act limit

**K5, MEASURED.** The paragraph at lines 165 to 176 of version 5 opens "**Hard
kill K5 is not reached.**" The ruling's item 1 phrases were each searched for
(`verbatim.py`): "K5 is not reached" (present), "tests whether two instruments
agree" (present), "Causal patching was never built for this design (ruling of
2026-09-20, ledger RT-96), so the test was never run" (present), "rests
instead on §3.2's convergence requirement" (present), "closes under the
pre-registration's loss condition above, with no further A3 seeds" (present),
and "This reading of the registered kill list is John's, ruled on 2026-09-25"
(present, followed by the ruling file and item number). The registered K5
wording the paragraph quotes matches `E/amendment-a3.md` line 265 exactly, and
it sits under "### 4.2 Hard kill criteria" (line 258), as the paragraph says.
The paragraph also says "this closure does not report a measured K5 failure",
which is the distinction ChatGPT's A7 asked for and the ruling adopted in
substance. Check (3) passes.

**The same-act limit, MEASURED.** Version 5 line 211 to 213: "A3 does not
establish that binding specifies its center in the same act, and it provides
no licensed verdict about consciousness or experience." The pre-registration
requires it: `E/pre-registration.md` line 84, "No result here closes that gap,
and every write-up must say so", and lines 529 to 530 name the clause, "the
same-act clause of the floor claim (binding that in the same act specifies its
own center)". Version 5's parenthesis at lines 213 to 215 cites the section by
its heading, which is line 47 of the pre-registration, "## Scope: this is Q5,
not the removal test". Check (4) passes.

## 3. Findings

### RT-204 — serious, ARGUED (with the record MEASURED): the schedule sentence cites a superseded consequence and omits the fresh-ruling requirement

This is the gap the writer flagged, and it is a finding.

**What version 5 says** (lines 234 to 237, ChatGPT's A4 wording adopted by item
9): "The operative deadlines remain registration by 2026-10-18 and launch of
the registered runs by 2026-11-01; missing either is recorded as a schedule
failure (`docs/rulings/2026-09-20-december-result-roadmap.md`, including its
2026-09-21 annotation)."

**What the cited file says, MEASURED.** Item 7 of that ruling (lines 44 to 46):
"Missing either drops the roadmap to R4 (a schedule failure, named as such in
STATUS.md)." Its 2026-09-21 annotation (lines 67 to 96) says the kill dates
"are commitments and are unchanged" and mentions neither item 23 nor a fresh
ruling:

```
$ grep -n "fresh ruling\|item 23" docs/rulings/2026-09-20-december-result-roadmap.md
(no output)
```

**What the later ruling says, MEASURED.** Item 23 of
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md` (lines 271
to 300): "Past a kill date, launching takes a fresh ruling rather than dropping
the roadmap … Past a date, launching is now still possible, but only on a fresh
ruling that names what comes off the back end … a missed date no longer puts
the roadmap there [R4] by itself." The same item settles that the second date
binds "the launch of the remaining eight runs … not the single free-arm run
before it". The record of record says the same (`STATUS.md` line 133, in the
entry of 2026-09-24 that begins at line 79: "passing one takes a fresh ruling
naming what comes off the back end, rather than dropping the roadmap to outcome
R4").

**Why it is a finding, ARGUED.** "Recorded as a schedule failure" is not false.
But the sentence sends a reader of the registered closure block to a file
whose stated consequence for a miss (drop to R4) was withdrawn four days later
by a ruling the sentence does not cite, and the annotation the sentence leans
on does not carry that withdrawal. A reader in 2027 following the citation
would conclude that a missed date means hibernation, which is no longer the
rule. The same sentence's "launch of the registered runs" is wider than the
step item 23 says the second date binds. This is the same shape as the
citation defect that stopped version 2 (`RT-145`: a pointer at something that
does not say what the current rule is), in a milder form, since here the file
exists and the sentence's own words remain true.

**Why serious and not fatal, ARGUED.** It sits in the successor paragraph and
alters no claim about what A3 measured or what it may be read as showing. It
is a currency defect in registered text, which the closure rule says is closed
by wording or carried as an open item with John's ruling and reason; it does
not need a run, money, or a second outside round.

**Why serious and not minor, ARGUED.** The ruling's item 9 authorised exactly
the sentence version 5 carries, so the writer could not add to it under item
22 without going wider than ruled; that is why it was flagged rather than fixed.
But a closure block is read as settled, and this is a live rule about spending
past a date. That is worth John's word before the text is registered rather
than an annotation afterwards.

**What would close it.** A proposal, not a ruling: after "(…including its
2026-09-21 annotation)", add one clause in John's name or the appending
session's, such as: "Since item 23 of
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, a missed
date no longer moves the roadmap to outcome R4 by itself, and launching past one
takes a fresh ruling naming what comes off the back end; the second date binds
the launch of the remaining eight registered runs, not the single free-arm run
before them." The alternative the closure rule allows is to carry it as an open
item named in the text. Whichever John chooses, the clause is binding text and
the pairing rule applies to it: whoever writes it does not check it.

### RT-205 — minor, MEASURED: "135 tests … and 135" is derived from the cited file, not stated in it

Version 5 line 144 (ChatGPT's A2 wording, adopted by item 7): "135 tests read
the registered marker-word target and 135 read the register index", cited to
`E/powered-position-sweep-findings.md`. That file states 270 and the two arms,
but never 135:

```
$ grep -n "135" E/powered-position-sweep-findings.md
(no output)
$ sed -n 12,13p E/powered-position-sweep-findings.md
Across eleven positions, five layers, two well-posed targets and three
checkpoints — **270 testable tests** — **not one reached even three
```

The arithmetic is written out in the method file the findings rest on,
`E/powered-position-sweep-method.md` line 107: "Two arms × nine testable
positions × five layers × three checkpoints =". Nine times five times three is
135 per arm. The figure also appears in `docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`
line 14 ("the one cell of 135") and in the ledger's RT-120 row (`E/red_team_ledger.md`
line 647, "3.3740 at 135 tests"), both cited elsewhere in the block. So the
number is right and traceable, and the citation checker (section 4) does not
flag it because it treats small whole numbers as section and item numbers by
default. Under the rule that a figure is in the file its sentence cites, it is
a gap of one file name. Closable by adding the method file to that citation, or
by John accepting the arithmetic as it stands; it changes no claim either way.

### RT-206 — minor, MEASURED: the $450 ceiling has no home in the compute ledger yet

Version 5 lines 277 to 279: "The programme ceiling those figures count against
was raised from $400 to $450 on 2026-09-25 (`docs/rulings/2026-09-26-weekend-1-queue.md`,
page 6)." That is what item 8 of the ruling instructs, and the citation is
right: page 6 of that file (line 134) reads "The programme envelope is raised
from $400 to **$450**", and its header (line 3) records the ruling on
2026-09-25. But the compute ledger, which is the programme's single home for
money, does not yet carry the change:

```
$ grep -c '\$450' E/compute-ledger.md
0
$ git log --oneline d9f4729..main -- E/compute-ledger.md
(no output: the ledger has not changed since the ruling commit)
```

The repository's own money checker says the same (full output in the appendix):

```
$ python3 scripts/check_single_source.py --only docs/a3-closure-text-draft-2026-09-25-v5.md
[CONFIDENT] Group 1: a dollar figure the ledger does not contain
  docs/a3-closure-text-draft-2026-09-25-v5.md:273   $450
      names instead: docs/rulings/2026-09-26-weekend-1-queue.md
[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source
  docs/a3-closure-text-draft-2026-09-25-v5.md:273   $400
      names instead: docs/rulings/2026-09-26-weekend-1-queue.md
Confident findings: 3.
```

This is not a defect in version 5, which does what the ruling says. It is a
note for the ledger: a dated line recording the ceiling change, before the
registration commit, so that the re-read of the ledger on landing day (which
version 5's own preamble at lines 37 to 39 requires) finds the ceiling there
and the closure text's money paragraph has one source rather than two.

### RT-207 — minor, MEASURED: the gloss on "L1 subspace" names the wrong section

Version 5 lines 159 to 161: "no L1 subspace (§3.2's name for the located region
of the network's internal activity that carries which marker is its own)". The
name is section 3.1's, not 3.2's:

```
$ sed -n 193,196p E/amendment-a3.md   (trimmed)
### 3.1 What is ablated: three levels
- **L0, the wire.** …
- **L1, the acquired index (the lesion target).** A low-rank subspace of the residual stream, localized as in §3.2, that carries "which marker is mine" …
```

Section 3.2 says how L1 is localized (lines 199 to 207) and uses the name;
section 3.1 defines it. The gloss's plain-language content is right; its
pointer is off by one section. This is a drafting choice, declared in the
change table (item 2, "Gloss added for 'L1 subspace'"), and it alters no
claim. Closable by writing "§3.1's name" or "the amendment's name".

### RT-208 — minor, MEASURED: one gloss is not declared in the change table

The version 5 preamble (lines 17 to 20) says every place where a gloss was
added beside adopted wording "is listed, item by item, in the section after
the block". The sentence diff (appendix, hunk 5) shows a gloss the table does
not list: "Causal patching — copying internal activity from one run into
another to test whether it causes the behaviour —" (version 5 lines 153 to
154), inserted into a version 4 sentence that item 2 did not replace. The
table's item 2 row declares only the "L1 subspace" gloss. The gloss itself is a
fair plain-language reading of `E/amendment-a3.md` line 204 ("patch the L1
subspace from an episode in which the model is agent A into the matched
episode in which it is agent B and read the revision action. If the action
follows the patched identity, the subspace carries ownership causally"). It
alters no claim. Closable by adding it to the table's item 2 row.

### RT-209 — minor, ARGUED: the "$0 side item" clause leaves the block with the replaced blind-arm sentences

Version 4's blind-arm passage ended "and a re-run is a $0 side item if a later
session finds the 2026-09-16 run did not meet the arm's registered target"
(version 4, lines 175 to 177). Item 14 replaces "the blind-arm sentence" with
ChatGPT's three sentences, which do not carry that clause, and version 5
follows the ruling (sentence diff, hunk 6). The fact survives in two files the
block cites: `docs/rulings/2026-09-20-december-result-roadmap.md` item 3 (lines
27 to 29) and `docs/rulings/2026-09-21-followup-runs-and-blind-arm.md` lines 34
to 36. Nothing is wrong with version 5 here; the ruling authorises the
replacement and the closure rule does not require every ruled fact to be in
the block. Recorded so that the drop is seen to be deliberate rather than
found later and read as a loss. No change is proposed.

### RT-210 — minor, MEASURED: a descriptive phrase inherited from version 4 is not in the file it cites

Version 5 lines 227 to 230, unchanged from version 4 lines 195 to 198: "A
matched-role causal-interchange experiment with a learn-both eligibility gate
… (`docs/competing-mechanisms-2026-09-20.md`)".

```
$ grep -n -i "learn.both\|interchange\|eligib" docs/competing-mechanisms-2026-09-20.md
(no output)
$ grep -n -i "matched-role" docs/competing-mechanisms-2026-09-20.md
67:same matched-role task, and the metric must separate them before it is
```

"Matched-role causal-interchange" is the name item 5 of
`docs/rulings/2026-09-20-center-as-degree.md` (line 63) gives the successor,
and "learn-both" is the name the ruling of 2026-09-23 on ranges and directions
uses for the check (`docs/rulings/2026-09-23-range-and-direction-only.md`, line
96). The description is right; the one file cited beside it does not contain
two of its three terms. This sentence is outside the 2026-09-25 ruling's
scope, passed the two earlier checks of version 4 unremarked, and is not a
number or a quotation. Recorded for the record; no change under this ruling.

### Checked and held (not findings)

- **Neither outside review filed a fatal finding**, as version 5's preamble
  says (line 17). MEASURED: `grep -n -i fatal` on both review files hits only
  prose about version 2's earlier fatal items (Gemini line 53; ChatGPT lines
  9, 184, 195), never a severity cell.
- **The reviewer names in the preamble** match the filed headers: "Model:
  Gemini 3.1 Pro" and "Model: ChatGPT 6 Astra Medium" (line 1 of each file).
- **The ledger claims in the money paragraph** hold as the ledger reads today
  (section 4, table rows for the ledger): about $46.2 of $100 and about
  $227.6 on the 2026-09-21 row (`E/compute-ledger.md` line 74); $1.904 on the
  two follow-up machines, "refused by the instrument check and deleted" (lines
  72, 73 and 215); the last table row is dated 2026-09-21 (line 74) and no row
  follows it. Version 5's "the instrument's own reproducibility check" is a
  plain-language rendering of what the ledger calls the instrument check,
  which "re-runs a recorded classifier accuracy and demands it come back to
  within one episode in 400" (lines 229 to 231). ARGUED: a fair rendering.
- **"Third checkpoint"** for the refit's crossing cell: the findings file says
  "Seed 2, the other agent's revision value, layer 3"
  (`E/standardised-refit-findings.md` line 28); the follow-up ruling calls the
  same cell "third checkpoint" (`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`
  line 14). Consistent.
- **"Calculated using its positive-control accuracy"** (item 18, ChatGPT's
  wording): the correction note derives one in eleven from "the only ceiling
  the run measures … at the position where the answer is the input token"
  (`E/fitted-position-sweep-findings-CORRECTION-2026-09-20.md` lines 10 to 12),
  which version 5 itself glosses as the positive control (lines 147 to 149),
  consistent with `E/powered-position-sweep-findings.md` lines 19 to 20.
- **The other glosses** all match their sources: "discovery positions" and
  "positive controls" (`E/powered-position-sweep-findings.md` lines 19 to 20);
  "folds" and "permutation draws" (`E/standardised-refit-method.md` lines 58 to
  69: training rows against held-out rows per fold, "the 200-draw
  shuffled-label null", "the bar of 3.38 standard deviations"); the blind arm
  "meant to show the instruments can find something known to be there"
  (`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md` lines 44 to 45);
  "A hard kill is a registered stop condition with a named consequence"
  (`E/amendment-a3.md` line 258, "each halts spend and sends the finding to
  John"; `E/red_team_ledger.md` line 756, "a registered event with
  consequences attached"). The lead-in "limited to each read above and its
  own target" (line 184) is the writer's, and states ChatGPT's A14 point
  without adding to it. ARGUED: none of these alters a claim. This is check
  (6): nothing in the change table's drafting choices alters a claim; RT-207
  and RT-208 are the only defects in them, and both are pointers, not claims.

## 4. Check (2): every number and quotation, against its cited file

**The two sweeps of failure mode 4, part one** (`docs/known-failure-modes.md`,
section 4), run over the closure block (lines 43 to 280 of version 5): the word
sweep returns 61 lines and the number sweep 10 lines (both reproduced in the
appendix). Every line was read. The 10 number lines carry 21 figures: 0.3125,
0.60, 0.5683, 0.5633, 0.5738, 0.1988, 0.2015, 0.1447, 0.0769, 0.0018, 0.0002,
0.1172, 0.000484, 1.94, 4,000, $46.2, $100, $227.6, $1.904, $400, $450. The
word-sweep lines add the counts and names that carry no decimal: 1.0, 135 and
135, eleven positions, five layers, seventy and eleven processor-hours, one in
eleven, the dates, the item numbers and section names, the ledger finding
numbers, and the quoted registered sentences.

**The lookups, MEASURED.** A script (`numbers_in_files.py`, appendix) searched
each figure and quotation in the file its sentence cites: 82 lookups. Result:

```
not found where expected: ['six evaluation seeds, paired', '135 per arm (NOT in findings file)']
```

The first of those two is a false miss of the script's own pattern, which
asked for two phrases within three lines; `E/seeds-endpoint-findings.md` has
them at lines 137 to 138 ("Every figure is a mean across six evaluation seeds
with its spread … Intact and lesioned are paired within each seed"), which a
plain `grep -n "six evaluation seeds\|paired"` returns. The second is RT-205.
Everything else was found, including: the nine endpoint numbers and the
0.1172 threshold (`E/seeds-endpoint-findings.md` lines 25 to 27, 42 to 44,
51); the control ceiling 1.0000 (`E/ceiling-measurement-findings.md` lines 30
to 33) and the restriction sentence (lines 85 to 86); 0.3125, the 0.60 bar,
"per-row gradient weight quadrupled" and "before the code existed"
(`E/control-learnability-pilot-findings.md` lines 4, 13 to 15, 40); the
registered ceiling 0.2921 (`E/amendment-a3.md` line 415); 0.000484 and 1.94 of
4,000 (`E/red_team_ledger.md` line 655, RT-128); RT-125 "ACCEPT, CARRIED OPEN"
(line 652); RT-89's "about 70 processor-hours against 11 and dropped before
the run" (line 461); RT-96 and RT-114 (lines 531, 549); RT-120 and RT-142
(lines 647, 669); F17's exact wording (`E/red-team-a4.md` line 137); the K5
line (`E/amendment-a3.md` line 265); the loss-condition quotation
(`E/pre-registration.md` lines 566 to 568); every ruling item cited (December
result items 1, 2, 7 and its annotation; follow-up ruling item 3 and the
reconciliation; center-as-degree item 5 and "What this ruling does not
decide", where "whether the ~70-hour marker-word fitted read runs before the
paper draft" is listed at line 92); the dispositions check's section 3 and its
sentence that the difference is shown "from the refit code and the run's three
output files"; the protocol sections named; and the two review headers.

**The repository's citation checker, MEASURED**, reproduces the writer's
commit-message claim exactly:

```
$ python3 scripts/check_citations.py --only docs/a3-closure-text-draft-2026-09-25-v5.md
[CONFIDENT] 0 reference(s) name a file that is not in the repository
[LOOK AT IT] 4 bare name(s) match more than one file
  …:61  pre-registration.md     …:108  red_team_ledger.md
  …:203 pre-registration.md     …:310  red_team_ledger.md
[CONFIDENT] 0 exact figure(s) absent from the one file their sentence cites
Confident findings: 0. Things for a human to look at: 4.
$ rm docs/a3-closure-text-draft-2026-09-25-v5.md; ls docs/a3-closure-text-draft-2026-09-25-v5.md
ls: docs/a3-closure-text-draft-2026-09-25-v5.md: No such file or directory
```

The four bare names are resolved by the block's own first sentence, which
names the experiment folder (version 5 lines 3 to 5), and by the text's
standing convention that bare names are files in that folder; each was looked
up there above.

**The $450 ceiling against page 6, MEASURED**: `docs/rulings/2026-09-26-weekend-1-queue.md`
line 126 "### Page 6 — spend", line 134 "The programme envelope is raised from
$400 to **$450**", line 3 "Recorded 2026-09-25 (Pacific)". The file's name
carries the planned date and its header says the ruling was made a day early,
so version 5's "on 2026-09-25" is right and its file name is right.

**The money figures against the ledger as it reads today, MEASURED**:
`E/compute-ledger.md` line 74 (the 2026-09-21 row) "A3 cumulative about
**$46.2 / $100**, programme about **$227.6 / $400**"; line 215 "Total measured
spend $1.904"; no table row after line 74; no commit to the ledger since the
ruling commit `d9f4729` (`git log --oneline d9f4729..main -- E/compute-ledger.md`
prints nothing).

**The decisive measured check the closure rule asks for.** Of everything run,
the single measurement that would have come out wrong had version 5 been wrong
is the pair of lookups above on the money paragraph: the ledger's last row
(dated 2026-09-21, carrying $46.2 and $227.6) and the queue ruling's page 6
($400 to $450 on 2026-09-25). Both match the text. The sentence-level diff and
the 82-row lookup table are the wider check behind it.

## 5. The failure-mode pass (check (5)): each of the five known failures, tested against version 5

Filed as the protocol requires, headed by the list's entries in order, each
with the command run and what it returned. The list is `docs/known-failure-modes.md`.

### 1. A comparison whose denominator was zero

Part one, with ceilings traced to committed records rather than assumed:

```
$ python3 -c "
ceilings = {'primary battery (registered, amendment-a3.md line 415)': 0.2921, 'control battery (measured, ceiling-measurement-findings.md line 33)': 1.0000}
for name, c in ceilings.items():
    print(f'{name}: denominator 1 - ceiling = {1 - c:.4f}')
"
primary battery (registered, amendment-a3.md line 415): denominator 1 - ceiling = 0.7079
control battery (measured, ceiling-measurement-findings.md line 33): denominator 1 - ceiling = 0.0000
```

**Disposition.** The control denominator is zero, which is failure 1 firing.
Version 5 does not reproduce it: it registers no comparison and no denominator,
and the zero is the thing it reports, as the loss condition, with the record
cited (lines 64 to 68, `E/ceiling-measurement-findings.md`). Part two (the top
of the scale per condition) has nothing to run on, because the text pre-states
no reading. Passes, in the only sense a closure text can: the failure is
named, its record is cited, and no new denominator is written.

### 2. A probe target that cannot be recovered in principle

Part one, the route-sentence search, run on version 5 with the list's pattern:

```
$ python3 -c "  (the list's part-one command, pointed at version 5)
v5: 1 route sentence(s)
   the positions where the answer is the input token, which any working read should
$ grep -n -i "pre-state\|will be read\|will decode\|is to be read\|registers the\|hereby\|we register" <v5>
76:usable — 0.3125 against a bar of 0.60 that was pre-stated before the code
```

**Disposition.** Version 5 pre-states no probe target (the only "pre-stated"
in the block is the pilot's 0.60 bar, already applied). The one sentence the
pattern matched is the gloss naming the positive control, where the answer is
the input token, which is the route sentence for the quantity the input
guarantees, consistent with `E/powered-position-sweep-findings.md` lines 19
to 20. Part two (running the probe pipeline twice) is not applicable to a text
that registers no probe, and was not run; running it costs compute nobody has
authorised, as the list itself says. Does not apply, shown by the search
rather than asserted.

### 3. A cell that is empty by construction

Every threshold, bar and cell the block mentions, and the trials behind each:

```
$ grep -n -i "threshold\|bar of\|the bar\|family bar\|cell\|locked\|≥\|>=" <v5>   (block lines only)
76:usable — 0.3125 against a bar of 0.60 that was pre-stated before the code
86:0.0018 and 0.0002 on the other seeds; all were below the locked 0.1172
87:threshold. The six primary-battery scores are means across six evaluation
119:the bar is built from. That both differed is shown from the refit's code and its
$ grep -n "0\.0018\|0\.0002\|0\.0769\|0\.1172" E/seeds-endpoint-findings.md
42:| pilot (seed 0) | +0.0018 | 0.0000 |
43:| seed 1 | +0.0002 | 0.0000 |
44:| seed 2 | **+0.0769** | 0.0000 |
51:0.1172 and 0.0769 is well inside it — but it is reported rather than
$ grep -n "0\.3125\|\*\*0\.60\*\*" E/control-learnability-pilot-findings.md
15:about a third to about two thirds.** It scored **0.3125**.
30:| **control (T_other)** | **0.3125** (sd 0.0240) | 0.2613 (sd 0.0258) |
40:| LEARNED, at or above **0.60** | −0.2875 | **−11.98** |
```

**Disposition.** Version 5 pre-states no cell and no new threshold. The three
thresholds it mentions were all applied to recorded trials: the 0.60 bar to
one pilot score of 0.3125; the locked 0.1172 threshold to three state drops;
the family bar to 135 refit tests with one crossing cell
(`E/standardised-refit-findings.md` lines 28 and 34). No cell comes back with
zero trials. Part one's generator count and part three's two-ended threshold
check have no design to run on here. Passes.

### 4. A claim of measurement with no record, or with a record that does not reproduce

Both sweeps were run and every hit read (section 4 and the appendix); 82
figures and quotations were then looked up in their cited files, and the
repository's citation checker was run. One derived count is not written in the
file cited (RT-205, minor); every other figure and quotation is present in its
file. No sentence claims a measurement and names no file; no cited file is
absent from the repository (`check_citations.py`: 0 confident findings); every
cited file is on the main line at `4d98cfc`, which is the checkout these
lookups ran in. Passes, with RT-205 recorded.

### 5. A command that creates something while documented as creating nothing

Version 5 contains no command and names no script:

```
$ grep -c -E '^\s*\$ |\.sh\b|python3? |launch_|--help|DRYRUN|runpodctl|ssh |curl ' <v5>
0
$ grep -o -E '`[^`]*\.(sh|py)`' <v5>
(no output)
```

The list's own test was also run, after reading the three launchers to confirm
that each exits inside its dry-run block before its first real vendor command
(`launch_a3_fetch_first.sh` lines 284 and 315; `launch_ctl_pilot.sh` 216 and
236; `launch_pilot_a1.sh` 114 and 127) and refuses an argument earlier still:

```
$ E/src/check_launcher_argument_guard.sh
RT-198 — launchers must refuse arguments rather than launch
  [ ok ] launch_a3_fetch_first.sh refuses an argument (exit 2)
  … (12 refusal checks, 6 dry-run checks, all ok)
  [ ok ] launch_a3.sh does NOT carry the guard, which is expected before Gate A
negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing
all checks pass. nothing was created and nothing was spent.
```

Exit status 0; the full output is in the appendix and matches the list's
printed output line for line apart from the three guard line numbers, which
the list printed as 104, 87 and 42 and which now read 119, 93 and 48 (the
launchers gained lines when the sleep guard landed as pull request 30). The
registered launcher's standing prohibition still prints, as expected before
the amendment lands. Passes.

## 6. Check (8): the two proposed annotations

### The annotation beside RT-164 (`docs/proposed-annotation-rt164-2026-09-25.md`)

Item 1 asks for: "A dated annotation goes beside RT-164's line in the red team
ledger saying 'Done in version 3' was not so; the line itself is not edited."

MEASURED: the proposal is dated 2026-09-25; it goes beside the row (a new row
directly under it, line 756 at `d9f4729`, which is where the row is:
`git show d9f4729:E/red_team_ledger.md | grep -n "^| RT-164"` prints 756, and
the ledger has not changed since); it says "'Done in version 3', was not so";
and it leaves the RT-164 row unedited, twice in so many words. The K5 wording
it quotes matches `E/amendment-a3.md` line 265. Every fact it adds is sourced:
the two `grep -c "K5"` zeros to the proposal's C1 and the dispositions check's
table (line 63 of that file), the two checks' silence to C3 (line 65), and the
disposition to item 1 of the ruling.

ARGUED, minor: the row carries more than the one sentence item 1 asks for. It
restates item 1's whole disposition, names both reviewer findings, and gives
the annotation a severity cell ("serious"). None of it is unsourced and none of
it rules anything, so it says what item 1 asks and nothing that contradicts
it; but "nothing more" is not quite met. John can land it whole or trim the
Finding cell to its first sentence. Either is within his ruling.

### The annotation beside the ChatGPT review (`docs/proposed-annotation-chatgpt-review-2026-09-25.md`)

Item 20 asks for: "A dated annotation beside the ChatGPT review file (not in
it): run in the Codex app; model as the app reported it, 'ChatGPT 6 Astra
Medium'; the body's self-description 'Codex' is the app's name; documents
pasted in 22 parts in one conversation; no lookup verified."

MEASURED: the proposal is dated 2026-09-25, is a separate file beside the
review (not in it), and carries each of the five facts: Codex app; "ChatGPT 6
Astra Medium" as the app reported it; "Codex" is the app's name; pasted in 22
parts in one conversation; lookup not verified. The two review lines it quotes
are exact (`E/reviews/2026-09-21-a3-closure-chatgpt.md` line 1 "Model: ChatGPT
6 Astra Medium"; line 7 "**Reviewer:** Codex; exact model version and app mode
were not exposed in the supplied context"). It says the facts are John's
account as the ruling records them and that the drafting session adds nothing.

ARGUED, minor: under "Lookup" the proposal reads item 20's "no lookup
verified" as "not verified either way", and adds an observation of its own that
the review's header says "lookup allowed" (line 3) while its body says "No
external lookup … was used" (line 7). Both quoted lines are right. But the
ruling's phrase also bears the other reading, that it was verified no lookup
took place. The annotation should carry whichever John meant, so this is a
question for him rather than a defect: one word settles it. Otherwise the file
says what item 20 asks and nothing more.

### A note on numbering

Item 21 says "Adopted findings are numbered from RT-204", meaning the tier 2
findings John adopted, when they are copied into the ledger. No file on the
main line uses RT-204 or above as a finding label today
(`grep -rn "RT-20[4-9]\|RT-21[0-9]" --include='*.md' .` hits only the
proposal, the dispositions check and the ruling, each quoting item 21). This
file numbers its own findings RT-204 to RT-210 because its brief said to
continue from RT-204. If the session that copies the adopted tier 2 items into
the ledger also starts at RT-204, one of the two ranges must move, and the
ledger's rows should win; the reconciliation item 21 already assigns to a later
session can absorb this.

## 7. What this check did not do

It did not re-run any model, probe, sweep or training step, and had no reason
to: version 5 pre-states nothing and reports only what committed records
already hold. It did not check the ledger's own arithmetic (the ledger is taken
as true, as the money checker says of itself). It did not open the tier 2
packets, so it cannot say what the outside reviewers saw beyond what their
filed responses say. It did not edit any file under review. It did not rule on
anything: RT-204's two closing routes, RT-206's ledger line, the trim of the
RT-164 annotation, and the reading of "no lookup verified" are all John's.

## Sources

Opened in the worktree at `4d98cfc` (the main line), unless a commit is named:

- The target, at `432e966`: `docs/a3-closure-text-draft-2026-09-25-v5.md`,
  `docs/proposed-annotation-rt164-2026-09-25.md`,
  `docs/proposed-annotation-chatgpt-review-2026-09-25.md`
- `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md` (the ruling) and
  `docs/rulings/2026-09-25-a3-closure-tier2-dispositions-PROPOSAL.md`
- `docs/a3-closure-text-draft-2026-09-21-v4.md`
- `E/reviews/2026-09-21-a3-closure-gemini.md`, `E/reviews/2026-09-21-a3-closure-chatgpt.md`,
  `E/reviews/2026-09-25-a3-dispositions-check-claude-worktree.md`
- `CLAUDE.md`, `STATUS.md` (top entry), `docs/outside-review-protocol.md`,
  `docs/known-failure-modes.md`
- `E/amendment-a3.md`, `E/pre-registration.md`, `E/red_team_ledger.md`,
  `E/red-team-a4.md`, `E/compute-ledger.md`
- `E/seeds-endpoint-findings.md`, `E/ceiling-measurement-findings.md`,
  `E/ceiling-defect-2026-09-17.md`, `E/control-learnability-pilot-findings.md`,
  `E/fitted-position-sweep-findings.md`,
  `E/fitted-position-sweep-findings-CORRECTION-2026-09-20.md`,
  `E/standardised-refit-findings.md`, `E/standardised-refit-method.md`,
  `E/other-index-position-sweep-findings.md`,
  `E/powered-position-sweep-findings.md`, `E/powered-position-sweep-method.md`
- `docs/rulings/2026-09-20-december-result-roadmap.md`,
  `docs/rulings/2026-09-20-center-as-degree.md`,
  `docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`,
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md` (item 23),
  `docs/rulings/2026-09-26-weekend-1-queue.md` (page 6),
  `docs/rulings/2026-09-23-range-and-direction-only.md` (the "learn-both" name),
  `docs/competing-mechanisms-2026-09-20.md`
- `E/src/check_launcher_argument_guard.sh`, and (read, run only under the
  guard check) `E/src/launch_a3_fetch_first.sh`, `E/src/launch_ctl_pilot.sh`,
  `E/src/launch_pilot_a1.sh`
- `scripts/check_citations.py`, `scripts/check_single_source.py`

## Appendix: the commands and their full outputs

### A. The sentence-level diff, version 4 block against version 5 block

`sentdiff.py` splits each block (version 4 lines 53 to 234; version 5 lines 43
to 280) into sentences and prints only the sentences removed (-) or added (+).

```
$ python3 sentdiff.py <v5>
v4 block: 46 sentences; v5 block: 79 sentences

=== hunk 1: replace v4[1:3] -> v5[1:5] ===
- It cannot be written before that commit exists, so it is still open here.* **Outcome: not testable — the registered comparison could never be computed, and what the experiment could measure without it was measured on three seeds.** This is the loss condition's sense of the phrase, not the validity-gate bin of the same name — the bin for an ablation that damages the model so broadly that no reading of it can be trusted.
- That bin did not fire, and it was also never tested: those gates have no code written for this design and were never applied to any lesion on any seed (the independent review of 2026-09-19 searched the source and the three endpoint records and found neither — `red-team-a4.md`, its seventeenth finding, labelled there F17).
+ It cannot be written before that commit exists, so it is still open here.* **Outcome: not testable — the registered comparison was undefined for every possible model.
+ Separately, removing the ownership-input channel reduced primary-battery accuracy on all three trained seeds.** This is the loss condition's sense of the phrase, not the validity-gate bin of the same name — the bin for an ablation that damages the model so broadly that no reading of it can be trusted.
+ The validity-gate bin was not evaluated: its gates were unimplemented and unapplied.
+ No code for them was written for this design, and they were never applied to the input-channel lesion, the only lesion A3 ran, on any seed (the independent review of 2026-09-19 searched the source and the three endpoint records and found neither — `red-team-a4.md`, its seventeenth finding, labelled there F17).

=== hunk 2: replace v4[4:7] -> v5[6:10] ===
- The control battery's ownership-blind ceiling was measured at 1.0 (`ceiling-measurement-findings.md`, 2026-09-17), so the registered differential clause had no computable value for any model from the day it was registered; the same measurement shows why this is structural rather than a defect of this control, in that the ceiling-corrected metric and the idea of an ownership-free control are incompatible by construction.
- The number the registration recorded as that ceiling was itself never attacked, which is registered separately as a defect in the instrument (`ceiling-defect-2026-09-17.md`).
- An unregistered pilot giving the control its own loss term at quadrupled weight did not make it usable — 0.3125 against a bar of 0.60 that was pre-stated before the code existed (`control-learnability-pilot-findings.md`).
+ The control battery's ownership-blind ceiling was measured at 1.0 (`ceiling-measurement-findings.md`, 2026-09-17), so the registered differential clause had no computable value for any model from the day it was registered.
+ The same measurement shows why this is structural rather than a defect of this control alone: the ceiling-corrected metric is incompatible by construction with any control fully determined by the visible episode and not requiring ownership, because every such control has an ownership-blind ceiling of 1.0.
+ The number the registration recorded as that ceiling had not been attacked before registration, which is registered separately as a defect in the instrument (`ceiling-defect-2026-09-17.md`).
+ An unregistered pilot giving the control its own loss term, per-row gradient weight quadrupled, did not make it usable — 0.3125 against a bar of 0.60 that was pre-stated before the code existed (`control-learnability-pilot-findings.md`).

=== hunk 3: replace v4[8:10] -> v5[11:15] ===
- **What A3 measured.** On three seeds trained from scratch, the primary battery learned (intact 0.5683, 0.5633, 0.5738) and collapsed when the ownership input channel was zeroed (0.1988, 0.2015, 0.1447), while the syntax battery was unchanged and the state battery moved on one seed (0.0769 on seed 2, below its locked threshold of 0.1172).
- All six scores are means across six evaluation seeds, paired within seed, and every figure in this paragraph is recorded at `seeds-endpoint-findings.md`.
+ A successor must demonstrate both its control ceiling and a usable comparison metric; measuring the ceiling alone does not resolve this defect.
+ **What A3 measured.** On three seeds trained from scratch, the primary battery learned (intact 0.5683, 0.5633, 0.5738) and collapsed when the ownership input channel was zeroed (0.1988, 0.2015, 0.1447), while the syntax battery was unchanged.
+ The state drop was 0.0769 on seed 2, versus 0.0018 and 0.0002 on the other seeds; all were below the locked 0.1172 threshold.
+ The six primary-battery scores are means across six evaluation seeds, paired within seed, and every figure in this paragraph is recorded at `seeds-endpoint-findings.md`.

=== hunk 4: replace v4[18:20] -> v5[23:30] ===
- A standardised refit, a different estimator on the same states, found the same thing everywhere but one cell (`standardised-refit-findings.md`): at the third checkpoint, at the **other** agent's revision value, at layer 3, it crossed the family bar by 1.94 episodes in four thousand — a margin computed in the review of that run and not stated in its findings file (the red team ledger's finding `RT-128`, which ruled that the number and its fragility travel together or neither travels) — and is recorded as a sub-bar pattern measured twice, not a clearance.
- The registered matched control (§L2(a), the other-agent index) had its **probe half** run for the first time, with rank matched by design and accuracy matched as observed; it excluded the exclusion confound that had been proposed for that pattern, while a purely relational encoding remains open as a route that would produce both the pattern and this null (`other-index-position-sweep-findings.md`).
+ A standardised refit, a different estimator on the same states, was run next (`standardised-refit-findings.md`).
+ The second estimator produced one nominal crossing; its folds and permutation draws also differed, so the change cannot be attributed to scaling alone.
+ (The folds are the way the episodes were split between fitting and testing; the permutation draws are the shuffled-label runs the bar is built from.
+ That both differed is shown from the refit's code and its three committed output files, not from its findings file, in the check of 2026-09-25, `reviews/2026-09-25-a3-dispositions-check-claude-worktree.md`, section 3.) The crossing sits at the third checkpoint, at the **other** agent's revision value, at layer 3.
+ It is an accuracy margin of 0.000484, equivalent to 1.94 of 4,000 episodes — a margin computed in the review of that run and not stated in its findings file (`red_team_ledger.md`, finding `RT-128`, which ruled that the number and its fragility travel together or neither travels) — and is recorded as a sub-bar pattern measured twice, not a clearance.
+ The registered matched control (§L2(a), the other-agent index) had its **probe half** run for the first time, with rank matched by design and accuracy matched as observed; it excluded the exclusion confound in the form proposed, a four-way rank of the other agent that this probe could decode (`other-index-position-sweep-findings.md`).
+ A purely relational encoding remains open as a route that would produce both the pattern and this null (the red team ledger's finding `RT-125`, carried open).

=== hunk 5: replace v4[22:26] -> v5[32:43] ===
- The registered probe target, the model's own marker word, has been read at these positions only by the weaker difference-of-averages method, which found it nowhere on either of its two arms across 270 tests (`powered-position-sweep-findings.md`).
- Reading the registered target with a sensitive instrument is one unrun job of about seventy processor-hours at no money cost (both the price and the fact that the job was dropped before that run rather than after it are recorded in the red team ledger's finding `RT-89`), and until it runs, only the narrower sentence above is available.
- Causal patching, which the section on how the ablation is localized (§3.2) requires alongside the probe before anything counts as localized or as absent, was never run and has no code for this design (the ruling of 2026-09-20 that patching is new code rather than existing machinery, ledger RT-96).
- Because the two instruments never converged on any seed, no L1 subspace was ever localized, and so the registered uncarvable signature H_diffuse was never reachable either: it requires a carved subspace to compare against the matched controls, and none was carved.
+ The registered probe target, the model's own marker word, has been read at these positions only by the weaker difference-of-averages method.
+ The difference-of-averages sweep found no discovery-position clearance for either target: 135 tests read the registered marker-word target and 135 read the register index.
+ Positive-control detections occurred where the answer was supplied by the input token (`powered-position-sweep-findings.md`).
+ (The discovery positions are the positions under test; the positive controls are the positions where the answer is the input token, which any working read should find.) Reading the registered target with a sensitive instrument is one unrun job of about seventy processor-hours at no money cost (both the price and the fact that the job was dropped before that run rather than after it are recorded in the red team ledger's finding `RT-89`), and until it runs, only the narrower sentence above is available.
+ Causal patching — copying internal activity from one run into another to test whether it causes the behaviour — which the section on how the ablation is localized (§3.2) requires alongside the probe before anything counts as localized or as absent, was never run and has no code for this design (the ruling of 2026-09-20 that patching is new code rather than existing machinery, ledger RT-96).
+ Because causal patching was never run, agreement between probe and patching could not be tested and no L1 subspace (§3.2's name for the located region of the network's internal activity that carries which marker is its own) was ever localized; so the registered uncarvable signature H_diffuse was never reachable either: it requires a carved subspace to compare against the matched controls, and none was carved.
+ **Hard kill K5 is not reached.** A hard kill is a registered stop condition with a named consequence.
+ K5 (`amendment-a3.md`, §4.2, its list of hard kill criteria: "Probe-patching convergence fails on all three seeds: *not testable (localization)*, reported as such; no further seeds") tests whether two instruments agree.
+ Causal patching was never built for this design (ruling of 2026-09-20, ledger RT-96), so the test was never run, and this closure does not report a measured K5 failure.
+ The term *not testable (localization)* rests instead on §3.2's convergence requirement, that nothing counts as localized until probe and patching agree, and A3 closes under the pre-registration's loss condition above, with no further A3 seeds.
+ This reading of the registered kill list is John's, ruled on 2026-09-25 (`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`, item 1).

=== hunk 6: replace v4[27:31] -> v5[44:52] ===
- What can be said descriptively, and separately from it: these probes did not localize this target at these positions, at a heuristic reach of roughly one legible episode in eleven (`fitted-position-sweep-findings-CORRECTION-2026-09-20.md`, which John ruled on 2026-09-20 must be cited wherever that figure is used; it is a rough reach and not measured detection power).
- What may not be said is that the structure is absent, or that these nulls make it less likely, because every number in these runs is conditional on this stack being able to recover a center that is known to be there, and that has never been established on this design.
- The registered blind-localization arm is the measurement that would establish it.
- Its status is ruled: the 2026-09-16 blind run discharged the registered arm and no re-run is scheduled (`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`, reconciling the December-result ruling's item 3 with the step 4 ruling); the requirement it serves is carried into the successor's rehearsal, and a re-run is a $0 side item if a later session finds the 2026-09-16 run did not meet the arm's registered target.
+ What can be said descriptively, and separately from it, is limited to each read above and its own target.
+ The fitted register-index read had a heuristic reach of approximately one episode in eleven, calculated using its positive-control accuracy.
+ This is not measured detection power at the discovery positions and does not establish the sensitivity of the unrun fitted marker-word read (`fitted-position-sweep-findings-CORRECTION-2026-09-20.md`, which John ruled on 2026-09-20 must be cited wherever that figure is used).
+ What may not be said is that the structure is absent, or that these nulls make it less likely, because every number in these runs is conditional on this stack being able to recover such a structure.
+ Ownership-channel dependence was established; recovery of an acquired internal representation by this stack was not.
+ John ruled the 2026-09-16 blind arm (the registered blind-localization run, meant to show the instruments can find something known to be there) discharged, so it does not block this closure.
+ That disposition does not establish successful recovery of an acquired ownership representation on the A3 design.
+ The unmet sensitivity requirement carries into the successor's rehearsal (`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`, reconciling the December-result ruling's item 3 with the step 4 ruling).

=== hunk 7: replace v4[33:35] -> v5[54:60] ===
- Their degree on the integration axis, how much of the act is organized around the ownership signal rather than consulting it, is unmeasured, because the metric for that axis (Stage 2) does not yet exist.
- The sentence this experiment supports in public is: the ownership input is load-bearing for the primary battery on three seeds; whether an internal center formed around it is not testable here; its degree is unmeasured.
+ "Above zero" is the project's classification under its 2026-09-20 definition of a load-bearing input, not a measured integration score.
+ A3 does not establish that binding specifies its center in the same act, and it provides no licensed verdict about consciousness or experience.
+ (The first of those two limits is the one `pre-registration.md` requires every write-up to state, under "Scope: this is Q5, not the removal test".) Their degree on the integration axis, how much of the act is organized around the ownership signal rather than consulting it, is unmeasured, because the metric for that axis (Stage 2) does not yet exist.
+ The sentence this experiment supports in public is: Removing the ownership-input channel reduced primary-battery accuracy on three trained seeds.
+ The matched comparison was unavailable; whether an acquired internal ownership structure exists was not established, and integration degree was not measured.
+ The above-zero classification may follow it only when expressly attributed to the ruling of 2026-09-20.

=== hunk 8: replace v4[37:38] -> v5[62:65] ===
- It registers in 2026 through Gate A with both tiers, registration commit target 2026-10-11 and kill date 2026-10-18 (`docs/rulings/2026-09-20-december-result-roadmap.md`, item 1, which carries all four of those facts and is what amends item 5 of `docs/rulings/2026-09-20-center-as-degree.md`; item 7 of the same ruling restates the 2026-10-18 date and adds a second one, that the registered runs launch by 2026-11-01, with either date missed recorded as a schedule failure).
+ It registers in 2026 (`docs/rulings/2026-09-20-december-result-roadmap.md`, item 1, which amends item 5 of `docs/rulings/2026-09-20-center-as-degree.md`).
+ The successor proceeds through Gate A with both tiers as soon as its prerequisites are complete.
+ The operative deadlines remain registration by 2026-10-18 and launch of the registered runs by 2026-11-01; missing either is recorded as a schedule failure (`docs/rulings/2026-09-20-december-result-roadmap.md`, including its 2026-09-21 annotation).

=== hunk 9: replace v4[45:46] -> v5[72:79] ===
- **Money.** Amendment A3 closed at ~$44.3 of its $100 hard stop, and the programme at ~$225.7 of its $400 ceiling (`compute-ledger.md`, the running totals on the rows dated 2026-09-19 and 2026-09-20).
+ Patching is not scheduled for A3; the December-result ruling assigns its construction to the successor (`docs/rulings/2026-09-20-december-result-roadmap.md`, item 2).
+ No further investigation of the other-agent revision-value position is authorised under the follow-up ruling (`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`, item 3).
+ The marker-word fitted read remains deferred, and whether it runs before the paper remains undecided.
+ These limitations do not imply that the missing measurements have been satisfied.
+ **Money.** As of the compute ledger's 2026-09-21 row (the measurement rehearsal's rented slice), about $46.2 was counted against Amendment A3's $100 stop and about $227.6 had been spent across the programme, including $1.904 spent on the two follow-up machines of 2026-09-20 that the instrument's own reproducibility check refused (`compute-ledger.md`).
+ The programme ceiling those figures count against was raised from $400 to $450 on 2026-09-25 (`docs/rulings/2026-09-26-weekend-1-queue.md`, page 6).
+ The ledger was re-read on 2026-09-25 and carries no row after 2026-09-21.

9 hunks
```

### B. The word-for-word check of adopted wording

`verbatim.py` searches version 5 for each string. "exact" is a byte-for-byte
substring match; "normalised" collapses whitespace and maps curly quotes to
straight ones before matching. Rows marked "(should be absent)" test that
replaced or declined wording is gone from the file; the four that read True
are in the change table only (section 1).

```
item                                                         exact  normalised
7 A2 s1                                                      False  True
7 A2 s2                                                      False  True
9 A4 s1                                                      False  True
9 A4 s2                                                      False  True
11 A6 successor                                              False  True
11 restriction (ruling words)                                True   True
12 ruling phrase                                             True   True
14 A10 s1 head                                               True   True
14 A10 s1 tail                                               True   True
14 A10 s2                                                    False  True
14 A10 s3                                                    False  True
15 A11 s1 head                                               False  True
15 A11 s2 head                                               False  True
15 A11 s3                                                    False  True
15 A11 s4                                                    False  True
16 A12 headline                                              False  True
17 A13 s1                                                    False  True
17 A13 s2                                                    False  True
17 A13 public                                                False  True
18 A14 s1                                                    False  True
18 A14 s2 head                                               False  True
19a A15                                                      False  True
19b ruling                                                   True   True
19c A15 (with the table's surrounding quote marks)           False  False   — confirmed whole in hunk 3
19d A15 (with the table's surrounding quote marks)           False  False   — see next row
19d as used                                                  True   True
19e A15 (with the table's surrounding quote marks)           False  False   — confirmed whole in hunk 4
19f A15 (with the table's surrounding quote marks)           False  False   — confirmed whole in hunk 6
5 ruling                                                     True   True
6 ruling                                                     True   True
2 Gemini G6 verbatim                                         False  False   — the ruling's own form is used; section 1
2 ruling/proposal words                                      False  True
1 ruling: tests whether two instruments agree                True   True
1 ruling: never built                                        False  True
1 ruling: rests on 3.2                                       False  True
1 ruling: closes under loss condition                        False  True
1 ruling: John                                               False  True
1 ruling: K5 is not reached                                  True   True
8 ruling: 46.2                                               True   True
8 ruling: 227.6                                              True   True
8 ruling: 450                                                True   True
8 ruling: page 6                                             True   True
A6 main replacement NOT adopted (should be absent)           False  False
A8 full replacement NOT adopted (should be absent)           False  False
A7 replacement NOT adopted verbatim (ruling words used instead) False  False
v4 2026-10-11 (should be absent)                             True   True    — change table line 299 only
v4 never converged (should be absent)                        True   True    — change table line 294 only
v4 270 tests (should be absent)                              False  False
v4 $44.3 (should be absent)                                  False  False
v4 $225.7 (should be absent)                                 False  False
A15b invalidated (should be absent)                          True   True    — change table line 308 only
v4 quadrupled weight (should be absent)                      True   True    — change table line 296 only
```

### C. The failure-mode-4 word sweep over the block (61 lines)

```
$ grep -n -iE "verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result" <v5> | awk -F: '$1>=43 && $1<=280'
56:they were never applied to the input-channel lesion, the only lesion A3 ran, on
58:three endpoint records and found neither — `red-team-a4.md`, its seventeenth
65:ownership-blind ceiling was measured at 1.0
66:(`ceiling-measurement-findings.md`, 2026-09-17), so the registered
68:was registered. The same measurement shows why this is structural rather than a
72:of 1.0. The number the registration recorded as that ceiling had not been
73:attacked before registration, which is registered separately as a defect in the
79:control ceiling and a usable comparison metric; measuring the ceiling alone does
82:**What A3 measured.** On three seeds trained from scratch, the primary
88:seeds, paired within seed, and every figure in this paragraph is recorded at
91:run.
93:**What A3 did not measure.** Whether the network built an internal
104:question, the mid-episode re-indexing probe, has never run (the red team
108:Four localization runs bear on where ownership sits, and none of them
110:layers found the register index — the four-way rank of the marker, not the
114:refit, a different estimator on the same states, was run next
118:between fitting and testing; the permutation draws are the shuffled-label runs
120:three committed output files, not from its findings file, in the check of
121:2026-09-25, `reviews/2026-09-25-a3-dispositions-check-claude-worktree.md`,
122:section 3.) The crossing sits at the third checkpoint, at the **other** agent's
124:1.94 of 4,000 episodes — a margin computed in the review of that run and not
127:recorded as a sub-bar pattern measured twice, not a clearance. The registered
128:matched control (§L2(a), the other-agent index) had its **probe half** run for
129:the first time, with rank matched by design and accuracy matched as observed;
130:it excluded the exclusion confound in the form proposed, a four-way rank of the
136:because no such subspace was found and there is nothing to ablate; running
139:follow-up runs (ledger RT-120 to RT-142).
143:difference-of-averages sweep found no discovery-position clearance for either
151:fact that the job was dropped before that run rather than after it are recorded
152:in the red team ledger's finding `RT-89`), and until it runs, only the narrower
154:one run into another to test whether it causes the behaviour — which the
156:before anything counts as localized or as absent, was never run and has no code
158:existing machinery, ledger RT-96). Because causal patching was never run,
170:so the test was never run, and this closure does not report a measured K5
182:instruments until causal patching has run, and that reading stands. What
186:positive-control accuracy. This is not measured detection power at the
192:likely, because every number in these runs is conditional on this stack being
195:John ruled the 2026-09-16 blind arm (the registered blind-localization run,
200:rehearsal (`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`,
201:reconciling the December-result ruling's item 3 with the step 4 ruling).
209:sense — and only in it — what the lesion measured puts these checkpoints
211:definition of a load-bearing input, not a measured integration score. A3 does
217:signal rather than consulting it, is unmeasured, because the metric for that
222:and integration degree was not measured. The above-zero classification may
224:result of A3 is described as "a structural signature of self-indexing" or
231:(`docs/rulings/2026-09-20-december-result-roadmap.md`, item 1, which amends
235:launch of the registered runs by 2026-11-01; missing either is recorded as a
236:schedule failure (`docs/rulings/2026-09-20-december-result-roadmap.md`,
238:things the successor inherits and must carry: measuring the control's
242:successor's whole purpose is a measurement that does not yet exist, so the
243:rehearsal requirement — that a full measurement procedure be demonstrated
245:the measurement rehearsal required before any Gate A) — applies to it even
254:place, and dropped before that run rather than because of anything the run
255:found (the red team ledger's finding `RT-89`); whether it runs before the
264:Patching is not scheduled for A3; the December-result ruling assigns its
265:construction to the successor (`docs/rulings/2026-09-20-december-result-roadmap.md`,
268:(`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`, item 3). The
269:marker-word fitted read remains deferred, and whether it runs before the paper
270:remains undecided. These limitations do not imply that the missing measurements
273:**Money.** As of the compute ledger's 2026-09-21 row (the measurement
277:reproducibility check refused (`compute-ledger.md`). The programme ceiling
```

### D. The failure-mode-4 number sweep over the block (10 lines)

```
$ grep -n -E "[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}|\$[0-9]+" <v5> | awk -F: '$1>=43 && $1<=280'
76:usable — 0.3125 against a bar of 0.60 that was pre-stated before the code
83:battery learned (intact 0.5683, 0.5633, 0.5738) and collapsed when the
84:ownership input channel was zeroed (0.1988, 0.2015, 0.1447), while the
85:syntax battery was unchanged. The state drop was 0.0769 on seed 2, versus
86:0.0018 and 0.0002 on the other seeds; all were below the locked 0.1172
123:revision value, at layer 3. It is an accuracy margin of 0.000484, equivalent to
124:1.94 of 4,000 episodes — a margin computed in the review of that run and not
274:rehearsal's rented slice), about $46.2 was counted against Amendment A3's $100
275:stop and about $227.6 had been spent across the programme, including $1.904
278:those figures count against was raised from $400 to $450 on 2026-09-25
```

### E. The 82 lookups of figures and quotations in their cited files

`numbers_in_files.py` holds one row per figure or quotation, the file its
sentence cites, and a search pattern. Rows marked "(expect NO)" test for an
absence the text asserts or that a finding rests on.

```
$ python3 numbers_in_files.py
check                                                              file                                                       found
K5 registered wording                                              amendment-a3.md                                            yes
K5 is in section 4.2                                               amendment-a3.md                                            yes
§3.2 convergence requirement                                       amendment-a3.md                                            yes
§3.1 heading                                                       amendment-a3.md                                            yes
L2 (a) other-index                                                 amendment-a3.md                                            yes
registration revision 8 heading                                    amendment-a3.md                                            yes
H_diffuse                                                          amendment-a3.md                                            yes
loss condition quote                                               pre-registration.md                                        yes
Loss conditions heading                                            pre-registration.md                                        yes
Scope heading                                                      pre-registration.md                                        yes
every write-up must say so                                         pre-registration.md                                        yes
same-act clause wording                                            pre-registration.md                                        yes
ceiling 1.0                                                        ceiling-measurement-findings.md                            yes
restriction sentence                                               ceiling-measurement-findings.md                            yes
never attacked (defect file)                                       ceiling-defect-2026-09-17.md                               yes
precondition of successor                                          ceiling-defect-2026-09-17.md                               yes
pilot 0.3125                                                       control-learnability-pilot-findings.md                     yes
pilot bar 0.60                                                     control-learnability-pilot-findings.md                     yes
pilot per-row quadrupled                                           control-learnability-pilot-findings.md                     yes
pilot pre-stated before code                                       control-learnability-pilot-findings.md                     yes
0.5683                                                             seeds-endpoint-findings.md                                 yes
0.5633                                                             seeds-endpoint-findings.md                                 yes
0.5738                                                             seeds-endpoint-findings.md                                 yes
0.1988                                                             seeds-endpoint-findings.md                                 yes
0.2015                                                             seeds-endpoint-findings.md                                 yes
0.1447                                                             seeds-endpoint-findings.md                                 yes
0.0769 seed 2                                                      seeds-endpoint-findings.md                                 yes
0.0018 pilot                                                       seeds-endpoint-findings.md                                 yes
0.0002 seed 1                                                      seeds-endpoint-findings.md                                 yes
0.1172 threshold                                                   seeds-endpoint-findings.md                                 yes
six evaluation seeds, paired                                       seeds-endpoint-findings.md                                 NO   (pattern too narrow; lines 137–138 carry it, see section 4)
syntax unchanged (0.0000 on all three)                             seeds-endpoint-findings.md                                 yes
RT-114 lists re-indexing probe as never run                        red_team_ledger.md                                         yes
eleven positions                                                   fitted-position-sweep-findings.md                          yes
five layers                                                        fitted-position-sweep-findings.md                          yes
one in eleven (correction)                                         fitted-position-sweep-findings-CORRECTION-2026-09-20.md    yes
correction: input-token ceiling used                               fitted-position-sweep-findings-CORRECTION-2026-09-20.md    yes
correction: ruled by John 2026-09-20, cited wherever used          fitted-position-sweep-findings-CORRECTION-2026-09-20.md    yes
refit cell: seed 2, other agent revision value, layer 3            standardised-refit-findings.md                             yes
RT-128: 0.000484 and 1.94 of 4,000                                 red_team_ledger.md                                         yes
RT-128: number and fragility travel together                       red_team_ledger.md                                         yes
RT-125 carried open                                                red_team_ledger.md                                         yes
RT-125 relational encoding                                         red_team_ledger.md                                         yes
RT-120 to RT-142 exist                                             red_team_ledger.md                                         yes
RT-89: ~70 hours vs 11, dropped before the run                     red_team_ledger.md                                         yes
RT-96: patching is new code                                        red_team_ledger.md                                         yes
RT-164 row exists                                                  red_team_ledger.md                                         yes
rank matched, measured                                             other-index-position-sweep-findings.md                     yes
accuracy matched, measured                                         other-index-position-sweep-findings.md                     yes
exclusion reading not supported                                    other-index-position-sweep-findings.md                     yes
F17 wording                                                        red-team-a4.md                                             yes
270 testable tests, two arms                                       powered-position-sweep-findings.md                         yes
135 per arm (NOT in findings file)                                 powered-position-sweep-findings.md                         NO   (RT-205)
135 per arm arithmetic (method file, not cited)                    powered-position-sweep-method.md                           yes
135 per family (follow-up ruling, cited elsewhere)                 2026-09-21-followup-runs-and-blind-arm.md                  yes
positive controls = input-token positions                          powered-position-sweep-findings.md                         yes
Dec ruling item 1: registers in 2026, amends item 5                2026-09-20-december-result-roadmap.md                      yes
Dec ruling item 2: patching not built for A3                       2026-09-20-december-result-roadmap.md                      yes
Dec ruling item 7: 2026-10-18 and 2026-11-01, schedule failure     2026-09-20-december-result-roadmap.md                      yes
Dec ruling 2026-09-21 annotation exists                            2026-09-20-december-result-roadmap.md                      yes
Dec ruling annotation: 2026-10-11 was pacing                       2026-09-20-december-result-roadmap.md                      yes
Dec ruling annotation mentions item 23 / fresh ruling? (expect NO) 2026-09-20-december-result-roadmap.md                      NO   (RT-204)
follow-up ruling item 3: no further work authorised                2026-09-21-followup-runs-and-blind-arm.md                  yes
follow-up ruling: arm discharged, carried into rehearsal           2026-09-21-followup-runs-and-blind-arm.md                  yes
follow-up ruling: reconciles Dec item 3 with step 4 ruling         2026-09-21-followup-runs-and-blind-arm.md                  yes
center-as-degree: What this ruling does not decide                 2026-09-20-center-as-degree.md                             yes
center-as-degree: marker-word read before paper undecided          2026-09-20-center-as-degree.md                             yes
center-as-degree item 5 amended by Dec item 1                      2026-09-20-center-as-degree.md                             yes
competing-mechanisms: matched-role                                 competing-mechanisms-2026-09-20.md                         yes
competing-mechanisms: learn-both eligibility gate (expect NO)      competing-mechanisms-2026-09-20.md                         NO   (RT-210)
ledger 2026-09-21 row: $46.2 / $100, $227.6 / $400                 compute-ledger.md                                          yes
ledger: $1.904 on the two follow-up pods, refused, deleted         compute-ledger.md                                          yes
ledger: any row dated after 2026-09-21 (expect NO)                 compute-ledger.md                                          NO
ledger mentions $450 (expect NO)                                   compute-ledger.md                                          NO   (RT-206)
queue ruling page 6: $400 to $450                                  2026-09-26-weekend-1-queue.md                              yes
queue ruling dated 2026-09-25                                      2026-09-26-weekend-1-queue.md                              yes
dispositions check §3: shown from code and three output files      2026-09-25-a3-dispositions-check-claude-worktree.md        yes
dispositions ruling item 1 (John's interpretation)                 2026-09-25-a3-closure-tier2-dispositions.md                yes
protocol: measurement rehearsal section                            outside-review-protocol.md                                 yes
protocol: closure rule section                                     outside-review-protocol.md                                 yes
Gemini review header                                               2026-09-21-a3-closure-gemini.md                            yes
ChatGPT review header                                              2026-09-21-a3-closure-chatgpt.md                           yes

not found where expected: ['six evaluation seeds, paired', '135 per arm (NOT in findings file)']
```

### F. The money checker's full output on version 5

```
$ python3 scripts/check_single_source.py --only docs/a3-closure-text-draft-2026-09-25-v5.md
System of record: experiments/06-mvm-0a-constructed-self-index/compute-ledger.md
Documents read: 1   scope: live   figures below $0 ignored
Figures that are in the ledger and point at it: 8
Set aside as forecasts (a proposal pricing something, not a record of spend): 0
Set aside as neither, by the wording around them: 1
[CONFIDENT] Group 1: a dollar figure the ledger does not contain
2 found. Either the document is stale or the ledger is missing
a number it should state. A total summed across ledger rows lands here too.
  docs/a3-closure-text-draft-2026-09-25-v5.md:273   $450
      names instead: docs/rulings/2026-09-26-weekend-1-queue.md
      in: The programme ceiling those figures count against was raised from $400 to $450 on 2026-09-25 (`docs/rulings/2026-09-26-weekend-1-queue.md`, page 6).
  docs/a3-closure-text-draft-2026-09-25-v5.md:298   $450
      in: Money paragraph rewritten to the ruling's figures: about $46.2 of $100 and about $227.6, as of the ledger's 2026-09-21 row, against a ceiling raised from $400 to $450 on 2026-09-25.
[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source
1 found. This is a second home being built for a number
that already has one.
  docs/a3-closure-text-draft-2026-09-25-v5.md:273   $400
      names instead: docs/rulings/2026-09-26-weekend-1-queue.md
[LOOK AT IT] Group 3: in the ledger, and no source named
0 found.
Confident findings: 3. Things for a human to look at: 0 unsourced figures and 0 widely repeated ones.
```

### G. The failure-mode-5 guard check, full output

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
RT-198 — launchers must refuse arguments rather than launch

unregistered launchers: an argument is refused
  [ ok ] launch_a3_fetch_first.sh refuses an argument (exit 2)
  [ ok ] launch_a3_fetch_first.sh says why it refused
  [ ok ] launch_a3_fetch_first.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_a3_fetch_first.sh guard (line 119) precedes any vendor command (line 287)
  [ ok ] launch_ctl_pilot.sh refuses an argument (exit 2)
  [ ok ] launch_ctl_pilot.sh says why it refused
  [ ok ] launch_ctl_pilot.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_ctl_pilot.sh guard (line 93) precedes any vendor command (line 219)
  [ ok ] launch_pilot_a1.sh refuses an argument (exit 2)
  [ ok ] launch_pilot_a1.sh says why it refused
  [ ok ] launch_pilot_a1.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_pilot_a1.sh guard (line 48) precedes any vendor command (line 117)

unregistered launchers: the guard did not break the real path
  [ ok ] launch_a3_fetch_first.sh dry run still exits 0
  [ ok ] launch_a3_fetch_first.sh dry run still creates nothing
  [ ok ] launch_ctl_pilot.sh dry run still exits 0
  [ ok ] launch_ctl_pilot.sh dry run still creates nothing
  [ ok ] launch_pilot_a1.sh dry run still exits 0
  [ ok ] launch_pilot_a1.sh dry run still creates nothing

registered launcher: read, never run
  [ ok ] launch_a3.sh does NOT carry the guard, which is expected before Gate A

  ***********************************************************************
  STANDING PROHIBITION, in force until the Gate A amendment clears:
  launch_a3.sh is REGISTERED TEXT and still has NO argument handling.
  An argument passed to it is SILENTLY IGNORED and it proceeds to a REAL
  LAUNCH at its defaults -- about ten hours and about ten dollars,
  writing into the registered seed-0 directory on the network volume.

      NO SESSION INVOKES A REGISTERED LAUNCHER WITH ANY ARGUMENT.

  To preview it without creating anything:  DRYRUN=1 ./launch_a3.sh
  Ruled by John 2026-09-22. Method: ../argument-guard-method.md [RT-198]
  ***********************************************************************


negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
(exit status 0)
```

### H. The three helper scripts

The three scripts run above are committed beside this file, in
`E/reviews/2026-09-25-a3-closure-v5-tier1-check-scripts/`: `sentdiff.py` (27
lines), `verbatim.py` (71 lines) and `numbers_in_files.py` (100 lines), all
Python standard library, none writing anything. To re-run them from the
repository root, first extract version 5 to a file outside the repository
(`git show 432e966:docs/a3-closure-text-draft-2026-09-25-v5.md > /tmp/v5.md`,
or wherever), then:

```
$ python3 E/reviews/2026-09-25-a3-closure-v5-tier1-check-scripts/sentdiff.py /tmp/v5.md
$ python3 E/reviews/2026-09-25-a3-closure-v5-tier1-check-scripts/verbatim.py /tmp/v5.md
$ python3 E/reviews/2026-09-25-a3-closure-v5-tier1-check-scripts/numbers_in_files.py
```

The first reads version 4 from its committed path; the third reads only
committed files. The row labels in `numbers_in_files.py` are the ones printed in
appendix E, and its search patterns are the quoted phrases.

---

## Re-check, 2026-09-25: version 5 at commit `3393f7d`, after John's rulings on the findings above

*Appended 2026-09-25 (Pacific) by the same session that filed the check above,
now on a branch cut from the main line at `0e9cd4a` (the commit that merged the
check, pull request 45). John ruled on the findings above on 2026-09-25, in the
session that asked for the revisions, and passed the rulings to this session in
his message: RT-204 accepted and closed by the clause the check proposes;
RT-205, RT-207, RT-208 and RT-210 accepted as wording changes; RT-209 stays as
recorded; RT-206 is a ledger note for the registration commit, not a text
defect; the RT-164 annotation stays as written; the "not verified either way"
reading in the ChatGPT annotation stands. The writer applied them as commit
`3393f7d` on branch `worktree-a3-closure-v5` (pull request 43). This session
did not write that commit. It re-read the file with `git show 3393f7d:docs/a3-closure-text-draft-2026-09-25-v5.md`
(362 lines; SHA-256 `4b46347dcf1c60fb42b506de9174437b5130cf1b2c85c56194fab74faa347596`).
Nothing was edited, launched or spent.*

### The answer

**Version 5 at `3393f7d` may be appended to `amendment-a3.md` as the
registration commit under the closure rule.** The RT-204 clause is the proposed
clause word for word, with one gloss on "R4" taken from item 23's own words,
and it cites item 23 correctly. Every accepted minor fix is applied as ruled.
Nothing else in the closure block changed: a sentence-level diff of the two
blocks gives exactly four hunks, one per accepted text change. Outside the
block, the preamble records the check and the change table gains one amended
row and six new rows, each citing the check. The citation checker now resolves
this file. Two things are owed to the red team ledger with or before the
registration commit, neither a defect in the text (below), and one minor
citation slip outside the block is recorded as RT-211.

### RT-204, closed: the clause as landed, MEASURED

The clause in the block (`3393f7d` lines 250 to 255) was compared with the
proposal in section 3 above, both with whitespace collapsed:

```
PROPOSAL: Since item 23 of `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, a missed date no longer moves the roadmap to outcome R4 by itself, and launching past one takes a fresh ruling naming what comes off the back end; the second date binds the launch of the remaining eight registered runs, not the single free-arm run before them.
LANDED  : Since item 23 of `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, a missed date no longer moves the roadmap to outcome R4 (hibernating with a registered design and a rehearsal) by itself, and launching past one takes a fresh ruling naming what comes off the back end; the second date binds the launch of the remaining eight registered runs, not the single free-arm run before them.
landed == proposal byte for byte: False
landed minus the R4 gloss == proposal: True
gloss present exactly once: True
```

The one difference is the parenthesis glossing R4. Its words are item 23's
own: `docs/rulings/2026-09-21-review-verification-and-staged-spending.md` line
275, "(R4: hibernate with a registered design and a rehearsal, on the record as
a schedule failure)". The clause cites item 23 by file, and item 23 (lines 271
to 300 of that file) says each thing the clause says: "a missed date no longer
puts the roadmap there by itself", "launching is now still possible, but only
on a fresh ruling that names what comes off the back end", and "the launch of
the remaining eight runs … not the single free-arm run before it". The clause
sits directly after the citation of the December-result ruling's annotation
(line 250), where the proposal put it. **Closed**: this is the MEASURED check
by a session other than the fix's writer that the closure rule asks for. The
ledger line is owed (see "Owed to the ledger").

### The minor fixes, each against its ruling, MEASURED

The sentence-level diff of the closure block at `432e966` (lines 43 to 283,
79 sentences) against the block at `3393f7d` (lines 49 to 301, 81 sentences)
gives four hunks and no others:

```
=== hunk 1: replace ===   (RT-205)
- (The discovery positions are the positions under test; …)  Reading the registered target …
+ (That file states 270 tests across the two targets; the 135 per target is derived from it, as nine testable positions × five layers × three checkpoints, the arithmetic `powered-position-sweep-method.md` sets out.) (The discovery positions are the positions under test; …)  Reading the registered target …

=== hunk 2: replace ===   (RT-207)
- … no L1 subspace (§3.2's name for the located region of the network's internal activity that carries which marker is its own) was ever localized; …
+ … no L1 subspace (§3.1's name for the located region of the network's internal activity that carries which marker is its own) was ever localized; …

=== hunk 3: replace ===   (RT-210)
- **Successor.** A matched-role causal-interchange experiment with a learn-both eligibility gate, whose purpose is to develop and validate the Stage 2 degree metric on contrast cases known by construction (`docs/competing-mechanisms-2026-09-20.md`).
+ **Successor.** A matched-role causal-interchange experiment with a learn-both eligibility gate, whose purpose is to develop and validate the Stage 2 degree metric on contrast cases known by construction.
+ The name "matched-role causal-interchange" is the one item 5 of `docs/rulings/2026-09-20-center-as-degree.md` gives the successor; "learn-both" is the name `docs/rulings/2026-09-23-range-and-direction-only.md` uses for the eligibility check; the contrast cases are set out in `docs/competing-mechanisms-2026-09-20.md`.

=== hunk 4: insert ===   (RT-204)
+ Since item 23 of … not the single free-arm run before them.

4 hunks in the block
```

- **RT-205 (135 per target), applied as ruled.** ChatGPT's two adopted
  sentences are untouched (`verbatim.py` re-run on `3393f7d`: every row
  identical to its run on `432e966`, save that "270 tests" is now present,
  which is this parenthesis). The arithmetic matches
  `E/powered-position-sweep-method.md` line 107, "Two arms × nine testable
  positions × five layers × three checkpoints =", and that file is now cited.
- **RT-207 (the L1 gloss), applied as ruled.** "§3.1's name", matching
  `E/amendment-a3.md` line 195, where L1 is defined under "### 3.1 What is
  ablated: three levels" (line 193).
- **RT-208 (the undeclared gloss), applied as ruled.** No block change. The
  change table's item 2 row now declares the causal-patching gloss and quotes
  it (diff hunk 5, below).
- **RT-209 (the "$0 side item" clause), stays as recorded.** No block change
  at that place (no hunk touches the blind-arm sentences). The table's RT-209
  row says so and names the two rulings that still carry the fact.
- **RT-210 (the inherited phrase), applied as ruled.** The sentence now cites
  item 5 of `docs/rulings/2026-09-20-center-as-degree.md` for the name (line
  63 of that file: "The successor experiment is Astra's matched-role
  causal-interchange design"), `docs/rulings/2026-09-23-range-and-direction-only.md`
  for "learn-both" (line 96: "On the learn-both check, each of the two arms
  clears its …"), and keeps `docs/competing-mechanisms-2026-09-20.md` for the
  contrast cases (line 67 of that file, "same matched-role task").
- **RT-206, not a text change, as ruled.** The table's paragraph after the new
  rows (line 351) says it is a note for the ledger and that nothing in the text
  changes for it. Correct as ruled; owed to the ledger (below).

### Nothing else changed: the whole diff, MEASURED

The diff of `432e966` against `3393f7d` touches one file, 51 insertions and 9
deletions, in six hunks. Four are the block changes above (the RT-210 and
RT-204 changes share one hunk). The other two are outside the block: the
preamble paragraph that records that the check ran and the revisions await a
re-check, and the change table (item 2 row amended; a new section "Revisions
after the tier 1 check (2026-09-25)" with six rows and the RT-206 paragraph).
The full diff, pasted:

```
diff --git a/docs/a3-closure-text-draft-2026-09-25-v5.md b/docs/a3-closure-text-draft-2026-09-25-v5.md
index a4b0916..0d731fc 100644
--- a/docs/a3-closure-text-draft-2026-09-25-v5.md
+++ b/docs/a3-closure-text-draft-2026-09-25-v5.md
@@ -32,9 +32,15 @@ where it was, beside version 4.*
 
 *This is registered text once it lands in
 `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md` as a dated
-closure block. It has not landed. Nothing is appended until the tier 1
-reviewer-owned check on this version has been run and filed (item 22 of the
-ruling). The session that appends it re-reads the compute ledger that day, as
+closure block. It has not landed. The tier 1 reviewer-owned check that item 22
+of the ruling requires has been run and filed
+(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-a3-closure-v5-tier1-check-claude-worktree.md`,
+commit `99b8b64`, pull request 45). It found one serious finding (RT-204) and
+six minor ones (RT-205 to RT-210). John ruled on them on 2026-09-25, and this
+version was revised the same day to apply those rulings; the revisions are the
+last rows of the change table after the block. Those revisions are binding text
+written by this version's writer, so they wait on a re-check by a different
+session. Nothing is appended until that re-check is filed. The session that appends it re-reads the compute ledger that day, as
 item 8 of the ruling asks, and changes the money paragraph only if a row has
 been added since.*
 
@@ -143,7 +149,10 @@ these positions only by the weaker difference-of-averages method. The
 difference-of-averages sweep found no discovery-position clearance for either
 target: 135 tests read the registered marker-word target and 135 read the
 register index. Positive-control detections occurred where the answer was
-supplied by the input token (`powered-position-sweep-findings.md`). (The
+supplied by the input token (`powered-position-sweep-findings.md`). (That file
+states 270 tests across the two targets; the 135 per target is derived from it,
+as nine testable positions × five layers × three checkpoints, the arithmetic
+`powered-position-sweep-method.md` sets out.) (The
 discovery positions are the positions under test; the positive controls are
 the positions where the answer is the input token, which any working read should
 find.) Reading the registered target with a sensitive instrument is one unrun
@@ -157,7 +166,7 @@ before anything counts as localized or as absent, was never run and has no code
 for this design (the ruling of 2026-09-20 that patching is new code rather than
 existing machinery, ledger RT-96). Because causal patching was never run,
 agreement between probe and patching could not be tested and no L1 subspace
-(§3.2's name for the located region of the network's internal activity that
+(§3.1's name for the located region of the network's internal activity that
 carries which marker is its own) was ever localized; so the registered
 uncarvable signature H_diffuse was never reachable either: it requires a carved
 subspace to compare against the matched controls, and none was carved.
@@ -226,15 +235,24 @@ result of A3 is described as "a structural signature of self-indexing" or
 
 **Successor.** A matched-role causal-interchange experiment with a
 learn-both eligibility gate, whose purpose is to develop and validate the
-Stage 2 degree metric on contrast cases known by construction
-(`docs/competing-mechanisms-2026-09-20.md`). It registers in 2026
+Stage 2 degree metric on contrast cases known by construction. The name
+"matched-role causal-interchange" is the one item 5 of
+`docs/rulings/2026-09-20-center-as-degree.md` gives the successor; "learn-both"
+is the name `docs/rulings/2026-09-23-range-and-direction-only.md` uses for the
+eligibility check; the contrast cases are set out in
+`docs/competing-mechanisms-2026-09-20.md`. It registers in 2026
 (`docs/rulings/2026-09-20-december-result-roadmap.md`, item 1, which amends
 item 5 of `docs/rulings/2026-09-20-center-as-degree.md`). The successor
 proceeds through Gate A with both tiers as soon as its prerequisites are
 complete. The operative deadlines remain registration by 2026-10-18 and
 launch of the registered runs by 2026-11-01; missing either is recorded as a
 schedule failure (`docs/rulings/2026-09-20-december-result-roadmap.md`,
-including its 2026-09-21 annotation). Three
+including its 2026-09-21 annotation). Since item 23 of
+`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, a missed
+date no longer moves the roadmap to outcome R4 (hibernating with a registered
+design and a rehearsal) by itself, and launching past one takes a fresh ruling
+naming what comes off the back end; the second date binds the launch of the
+remaining eight registered runs, not the single free-arm run before them. Three
 things the successor inherits and must carry: measuring the control's
 ceiling properly is a precondition of any successor amendment (John,
 2026-09-17, `ceiling-defect-2026-09-17.md`); nothing counts as localized or
@@ -291,7 +309,7 @@ beside it is named.
 | Ruling item | Reviewer finding | What changed |
 |---|---|---|
 | 1 | Gemini G5, ChatGPT A7 | New paragraph "Hard kill K5 is not reached", in the ruling's words: K5 tests whether two instruments agree; patching was never built (RT-96), so the test was never run; *not testable (localization)* rests on §3.2's convergence requirement; A3 closes under the loss condition with no further A3 seeds; stated as John's interpretation. The annotation beside RT-164 in the red team ledger is drafted separately, not made here. |
-| 2 | Gemini G4, G6 | "Because the two instruments never converged on any seed" replaced with Gemini's G6 rewrite, in the ruling's words ("agreement between probe and patching could not be tested"). Gloss added for "L1 subspace". |
+| 2 | Gemini G4, G6 | "Because the two instruments never converged on any seed" replaced with Gemini's G6 rewrite, in the ruling's words ("agreement between probe and patching could not be tested"). Gloss added for "L1 subspace". Gloss also added for "causal patching" ("copying internal activity from one run into another to test whether it causes the behaviour") in the version 4 sentence before it, which item 2 did not replace (declared after the tier 1 check; see the RT-208 row below). |
 | 5 | Gemini G3 | "never applied to any lesion" becomes "never applied to the input-channel lesion, the only lesion A3 ran, on any seed". |
 | 6 | ChatGPT A1 | "at quadrupled weight" becomes "per-row gradient weight quadrupled". |
 | 7 | ChatGPT A2 | The 270-test sentence replaced with ChatGPT's replacement, verbatim. Gloss added for "discovery positions" and "positive controls". |
@@ -311,6 +329,30 @@ beside it is named.
 | 19(e) | ChatGPT A15 | "found the same thing everywhere but one cell" replaced with ChatGPT's sentence, verbatim. Cited to the dispositions check of 2026-09-25, section 3, not to `standardised-refit-findings.md`, as the ruling requires. Glosses added for "folds" and "permutation draws". |
 | 19(f) | ChatGPT A15 | "a center that is known to be there" replaced; ChatGPT's sentence added, verbatim. |
 
+### Revisions after the tier 1 check (2026-09-25)
+
+These rows apply John's rulings of 2026-09-25 on the tier 1 reviewer-owned check
+of this version at commit `432e966`
+(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-a3-closure-v5-tier1-check-claude-worktree.md`,
+commit `99b8b64`, pull request 45; "section 3" below is that file's findings
+section). The rulings were given in the session that asked for these revisions
+and are not yet in a committed ruling file. They were written by this version's
+writer and are owed a re-check by a different session.
+
+| Check finding | Severity as filed | John's ruling, 2026-09-25 | What changed |
+|---|---|---|---|
+| RT-204 (section 3) | serious | Accepted; closed by the clause the check proposes | In the successor paragraph, after the citation of the December-result ruling's 2026-09-21 annotation, the check's proposed clause is added: since item 23 of `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, a missed date no longer moves the roadmap to outcome R4 by itself, and launching past one takes a fresh ruling naming what comes off the back end; the second date binds the launch of the remaining eight registered runs, not the single free-arm run before them. Gloss added for R4 ("hibernating with a registered design and a rehearsal"), from item 23's own words. |
+| RT-205 (section 3) | minor | Accepted: state 135 as derived from the cited 270 | ChatGPT's two sentences are unchanged. A parenthesis after the citation says the findings file states 270 across the two targets and that 135 per target is derived, as nine testable positions × five layers × three checkpoints, citing `powered-position-sweep-method.md`. |
+| RT-207 (section 3) | minor | Accepted: fix the gloss's section | "§3.2's name" becomes "§3.1's name" in the gloss on "L1 subspace". Section 3.1 of `amendment-a3.md` defines L1; section 3.2 says how it is localized. |
+| RT-208 (section 3) | minor | Accepted: declare the undeclared gloss | No change to the block. The "causal patching" gloss is now declared in the item 2 row above. |
+| RT-209 (section 3) | minor | Accepted: the removal of the "$0 side item" clause stays as recorded | No change. Version 4's clause that a blind-arm re-run would be a $0 side item stays out of the block, as item 14's replacement left it. The fact is still in the December-result ruling's item 3 and in `docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`, both cited in the block. |
+| RT-210 (section 3) | minor | Accepted: correct the inherited phrase's citation | The successor's description, unchanged from version 4, cited only `docs/competing-mechanisms-2026-09-20.md`, which does not contain "causal-interchange" or "learn-both". It now cites item 5 of `docs/rulings/2026-09-20-center-as-degree.md` for the name, `docs/rulings/2026-09-23-range-and-direction-only.md` for "learn-both", and keeps the competing-mechanisms document for the contrast cases. |
+
+RT-206 (minor, section 3: the $450 ceiling is not yet in the compute ledger) was
+not part of the rulings passed to this session, and the check says itself that
+it is not a defect in this text. It is a note for the ledger, and nothing here
+changes for it.
+
 Not applied here, because the ruling gives them no text change: items 3, 4,
 10 and 13 (credit or records), item 20 (an annotation beside the ChatGPT
 review file, drafted separately), item 21 (finding numbers from RT-204, which
```

### The change table cites the check, MEASURED

```
$ grep -c "2026-09-25-a3-closure-v5-tier1-check-claude-worktree.md" <v5 at 3393f7d>
2
$ grep -c "^| RT-2.. (section 3)" <v5 at 3393f7d>
6
```

The file is named in the preamble (line 37) and in the new section's header
(line 336); each of the six new rows names its finding and "(section 3)", the
findings section of this file. The rows' "John's ruling" column matches the
rulings John passed to this session, item for item.

### The citation checker now resolves this file, MEASURED

Run on a copy of the `3393f7d` file placed at its own path in a worktree at
`0e9cd4a`, then removed:

```
$ python3 scripts/check_citations.py --only docs/a3-closure-text-draft-2026-09-25-v5.md
[CONFIDENT] 0 reference(s) name a file that is not in the repository
[LOOK AT IT] 4 bare name(s) match more than one file
  …:67  pre-registration.md   …:114 red_team_ledger.md   …:212 pre-registration.md   …:328 red_team_ledger.md
[CONFIDENT] 0 exact figure(s) absent from the one file their sentence cites
Confident findings: 0. Things for a human to look at: 4.
$ rm docs/a3-closure-text-draft-2026-09-25-v5.md; ls docs/a3-closure-text-draft-2026-09-25-v5.md
ls: docs/a3-closure-text-draft-2026-09-25-v5.md: No such file or directory
```

The writer's commit message reported two confident findings, both this check
file, because pull request 45 had not merged when the writer ran it. It has
now (`0e9cd4a`), and the two are gone. The four bare names are the same four as
before, resolved the same way.

### RT-211 — minor, MEASURED: the file cites this check by a commit that is not on the main line

The preamble (line 38) and the new section's header (line 337) cite this check
as "commit `99b8b64`, pull request 45". Pull request 45 was squash-merged, so
that commit is not an ancestor of the main line (the ancestor test returns
status 1; the merge commit `0e9cd4a` has the single parent `4d98cfc`):

```
$ git merge-base --is-ancestor 99b8b64 origin/main; echo $?
1
$ git show --format='%h parents:%p %s' -s 0e9cd4a
0e9cd4a parents:4d98cfc Tier 1 check of the A3 closure text, version 5 at 432e966: one serious finding, nothing fatal (#45)
```

`99b8b64` exists only on the review branch, which will be deleted, and the
known-failure list itself warns that a citation anchored to a session branch
"loses its signpost without anyone editing the sentence"
(`docs/known-failure-modes.md`, section 1). The check is on the main line at
`0e9cd4a`. Both citations are outside the closure block (the preamble and the
change table are not appended to `amendment-a3.md`), so this does not bear on
the registration commit; it is a one-token fix for whoever next touches the
file, and the file path and pull request number already locate the check
without the hash.

### Owed to the red team ledger, with or before the registration commit

Neither is a defect in the text, and neither was in John's rulings on the
text; both are what the closure rule and the ruling's item 21 already require:

1. **A closure line for RT-204** in `E/red_team_ledger.md`, in the ledger's
   form: the finding, the commit that lands the fix (`3393f7d`), and the
   MEASURED check by a session other than the fix's writer, which is the
   section "RT-204, closed" above. Rows for RT-205 to RT-211 with John's
   rulings as passed. None exists yet:
   ```
   $ grep -n "RT-20[4-9]\|RT-210\|RT-211" E/red_team_ledger.md
   (no output)
   ```
   The numbering question in section 6 above still stands: item 21 reserves
   RT-204 onward for the adopted tier 2 findings when they reach the ledger,
   and the reconciliation it assigns to a later session should settle both
   ranges at once.
2. **A dated line in the compute ledger for the $450 ceiling** (RT-206), so
   the re-read of the ledger on landing day, which the version 5 preamble
   requires, finds the ceiling where money lives.

### Closing line

**Version 5 at `3393f7d` may be appended to `amendment-a3.md` as the
registration commit under the closure rule.** RT-204 is closed by a clause that
matches the proposal word for word plus a gloss in item 23's own words; the
minor fixes are applied as ruled and nothing else in the block changed; the
change table cites the check; the citation checker is clean. The appending
session fills the date placeholder, re-reads the compute ledger that day as
the preamble requires, and the two ledger items above go in with or before
that commit. RT-211 is a one-token fix outside the block and does not wait on
anything.
