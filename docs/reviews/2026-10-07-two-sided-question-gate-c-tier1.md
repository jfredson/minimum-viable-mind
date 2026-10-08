# Gate C tier 1 review (the inside pass) of the proposal to refound the project on the two-sided question

*Filed 2026-10-07 (Pacific) by a fresh Claude Code session in its own worktree
(branch `worktree-agent-a5f29f93630089c3a`), reviewing
`docs/rulings/2026-10-07-two-sided-question-PROPOSAL.md` at commit `9184ad9`
(the commit that added the dated note recording John's approval in
principle). The target is a Gate C proposal: it asks for a John-level ruling
on programme direction, so under `docs/outside-review-protocol.md` it carries
this pass before he rules. This session did not write the proposal, the brief
for outside models, the router-control check or the poll synthesis, and has
read no chat of the session that did. Nothing was rented, trained or spent:
$0. No vendor was called. No existing file was edited.*

*Filed under `docs/reviews/` at the instruction of the session that
commissioned this pass. The protocol's own filing rule puts a review under
the reviews directory of the experiment the text most affects; this proposal
affects the spec and four experiments at once, so no single experiment owns
it. If the filing rule is held to, a pointer belongs under
`experiments/06-mvm-0a-constructed-self-index/reviews/`, where the successor
experiment's reviews already sit.*

*Every finding is labelled MEASURED (a command was run and its output is
printed here) or ARGUED (reasoning a reader can dispute), and marked fatal,
serious or minor. Finding numbers continue the red-team ledger from RT-256;
the highest number in use is RT-255 (the a2 decision-procedure finding, in
`docs/2026-10-06-successor-a2-decision-procedure-findings.md`). Written under
the workspace plain-language rule; no em-dashes in this session's own
sentences. Command outputs are pasted as returned and keep the record's own
punctuation, which in three quoted lines includes an em-dash.*

---

## 1. What this session opened, and what it did not

**Opened, in this order:** the workspace rules (`~/Code/CLAUDE.md`); this
repo's `CLAUDE.md`; the outside-review protocol (the gates, the pairing rule,
the tier descriptions, the closure rule, the filing section, and the
2026-09-21 amendments including John's words on task time); the known-failure
list in full, all six entries and the closing section; the proposal itself at
`9184ad9`.

**Opened to check the proposal's claims:** the compute ledger
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, the
programme's money record); item 23 of the 2026-09-21 ruling on review
verification and staged spending; section 5 of the December-result roadmap;
experiment D's registered results (`experiments/03-retained-independence/results.md`)
and its confidence-interval analysis file (`ladder_analysis_ci.json`); the spec
(`spec/minimum-viable-mind-proposal-v0.1.md`), its headers in order, its Scope,
Floor, Measuring It and What Would Count Against It sections; the founding
wager proposal (`docs/founding-wager-proposal-2026-09-20.md`) and the
center-as-degree ruling that cross-references it; the poll synthesis in full;
all six poll replies in full (Gemini, GPT and Claude Opus, rounds one and
two) and the manifest; the brief for outside models, version 2, headers and
section 8; the router-control check in full; the successor experiment
proposal, version 4, sections 3, 11 and 12; the ruling packet on arms C and M
losing their ownership route, read from its latest commit `7583326` on the
unmerged branch `ruling-packet-cm-flat` because it is not on this branch; the
top of STATUS.md (the 2026-10-04 entry); the weekend roadmap's calendar table
and its weekend-2 re-plan; `data/roadmap.toml`; the go packet for the four
development runs; the first lines of experiment 7's pre-registration;
experiment 1's dose-response passages and the RT-06 ladder (the
alignment-depth ladder) spec and findings; the book's argument summary at
`/Users/john/Code/calibration-problem/editorial/argument-summary-2026-10-07.md`,
for the chapter 6 indicators and the chapter 15 questions only; the listing of
experiment D's source directory and of experiment 06's reviews directory.

**Not opened:** any chat transcript of any session; the brief's version 1 and
the two paste files beyond listing them; pull request 106 (the
development-runs check) itself, which is unmerged and which this session
knows only through the packet's description of it; the book manuscript; the
TimeAssembler record; any stimulus code, battery or transcript of
experiments 1 or 3 beyond the analysis file named above; any launcher with an
argument. Nothing was re-run that touches a model, a vendor or a machine.

---

## 2. MEASURED checks

Each check gives the command, the output as returned (abridged only where
said), and a plain sentence on whether the output matches the proposal.

### (a) Every file path the proposal cites exists on this branch

```
$ grep -o '`[^`]*`' docs/rulings/2026-10-07-two-sided-question-PROPOSAL.md | tr -d '`' \
  | grep -E '\.(md|toml|py|json|txt)$|/$' | sort -u \
  | while read p; do [ -e "$p" ] && echo "EXISTS   $p" || echo "MISSING  $p"; done
MISSING  calibration-problem/editorial/argument-summary-2026-10-07.md
EXISTS   docs/december-result-roadmap-2026-09-20.md
EXISTS   docs/founding-wager-proposal-2026-09-20.md
EXISTS   docs/known-failure-modes.md
EXISTS   docs/outside-perspective/2026-10-07-detecting-another-mind-brief-v2.md
EXISTS   docs/outside-perspective/2026-10-07-poll-synthesis.md
EXISTS   docs/outside-perspective/2026-10-07-router-control-check.md
EXISTS   docs/outside-perspective/replies/
EXISTS   docs/rulings/2026-09-21-review-verification-and-staged-spending.md
MISSING  docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md
EXISTS   experiments/03-retained-independence/results.md
EXISTS   spec/minimum-viable-mind-proposal-v0.1.md
```

Where the two missing ones are:

```
$ git log --all --oneline -- docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md
7583326 Packet: remove a doubled phrase
81ae31d Packet: two wording fixes from the re-check (decay share; calendar days)
2db4435 Ruling packet on arms C and M: tighten page 1
8367c13 Ruling packet on arms C and M: apply the eight points of its check (pull request 112)
79bd26d PROPOSAL: ruling packet on arms C and M losing their built-in ownership route, plus four tripwire fixes
$ git branch -a --contains 7583326
+ ruling-packet-cm-flat
  remotes/origin/ruling-packet-cm-flat
$ git ls-tree -r main --name-only | grep -c cm-flat-ownership
0
$ ls -la /Users/john/Code/calibration-problem/editorial/argument-summary-2026-10-07.md
-rw-r--r--@ 1 john  staff  32707 Oct  7 09:59 /Users/john/Code/calibration-problem/editorial/argument-summary-2026-10-07.md
$ git log --all --oneline --grep='pull request 106'
79bd26d PROPOSAL: ruling packet on arms C and M losing their built-in ownership route, plus four tripwire fixes
```

**Does not match.** Ten of twelve paths exist. The ruling packet on the two
flat models, which the proposal cites in sections 1, 3 and 6 and in Appendix
B and leans on for the $1.14 repair figure and for decision 3, exists only on
the unmerged branch `ruling-packet-cm-flat`, not on main and not on this
branch. Pull request 106 (the development-runs check) is likewise unmerged
and is known here only through that packet. The book summary exists on disk
at the absolute path the poll manifest records, but it is outside this
repository and the proposal cites it by a relative path that resolves
nowhere. See RT-256.

### (b) The money figures of section 6 against the ledger

```
$ grep -n -i 'running total\|remain\|of \$450' experiments/06-mvm-0a-constructed-self-index/compute-ledger.md | cut -c1-300 | tail -4
110:this note, the programme total after the two attempts is about **$228.17 / $450**
148:  about **$229.62 of $450**; development line about **$8.53 of $10 left**.
```

(Line 148 is the 2026-10-04 annotation on the four development-run rows:
"Programme about $228.15 to about $229.62 of $450".) $450 less $229.62 is
$220.38. **Matches:** "about $230 spent, about $220 remaining of $450" is
what the ledger's last running line gives. One figure in section 3 does not
come from the ledger, the "about $131" second release; see RT-257.

### (c) The kill-date rule: item 23 and roadmap section 5

```
$ awk '/^23\./{f=1} f{print NR": "$0} /^24\./{if(f)exit}' docs/rulings/2026-09-21-review-verification-and-staged-spending.md | head -12
271: 23. **Past a kill date, launching takes a fresh ruling rather than dropping the
272:     roadmap.** Put to John with its strongest alternative, approved in his words
273:     "Ok that's fine. Let's go with your recommendation". The two kill dates of
274:     `docs/december-result-roadmap-2026-09-20.md` used to drop the roadmap to its
275:     fourth outcome (R4: hibernate with a registered design and a rehearsal, on
276:     the record as a schedule failure). Past a date, launching is now still
277:     possible, but only on a fresh ruling that names what comes off the back end
278:     to make room — a thinner closure, one outside reviewer at the closure gate
279:     instead of two, no refresh of the explainer, or whatever the real trade turns
280:     out to be. The dates themselves do not move, and neither does the reason for
281:     having them: nobody drifts past one quietly, and nobody decides in the moment
282:     without saying so out loud.
$ grep -n '^## ' docs/december-result-roadmap-2026-09-20.md | sed -n 5p
252:## 5. Kill dates and what they trigger
```

Section 5 of the roadmap carries the same rule in the same words ("Past a
kill date, launching is still possible, but it takes a fresh ruling, and that
ruling has to name what comes off the back end"), and names the two dates:
registration by 2026-10-18 and the remaining eight runs of step 5b by
2026-11-01. **Matches in part.** The rule is where the proposal says it is
and says what the proposal says about naming what comes off the back end.
It does not say what the proposal says in section 6, that "a fresh ruling may
move them": the ruling's own words are "The dates themselves do not move".
See RT-258.

### (d) Experiment D's claims against its registered results

```
$ grep -n -i 'masked\|capitulat\|W3\|framings\|^Models' experiments/03-retained-independence/results.md | cut -c1-160 | head -14
20:Models (provisional grid per spec §D.3; GPT + open-weights pending
21:keys/venue): `claude-opus-4-8`, `claude-sonnet-5`,
22:`gemini-3.1-pro-preview`. 60 items (30 held-answer + 30 live-objection)
23:× 2 arms × 3 framings × 3 models = 1,080 five-turn conversations
58:## The masked/capitulated decomposition (S3-RT-03) — the headline finding
61:overwhelmingly **masked** (re-asserted at the de-pressured probe), not
62:**capitulated** (gone even when released):
107:- **W3 (the 2×2 is real): WINS decisively.** Evidence-updating is
```

The three framings are `tool`, `tool_expert` and `mind` (the table at line
40). The results file's corrected count: "Bank B 9 of 270, Bank A 2 of 270,
11 of 540 overall" true capitulations, against "78+27 masked cells". From the
confidence-interval file:

```
$ python3 -c "
import json; d=json.load(open('experiments/03-retained-independence/ladder_analysis_ci.json')); n=30
tm=tc=0
for cell,v in d['cells'].items():
    for bank in ('bank_a','bank_b'):
        m=round(v[bank]['masked_rate']['point']*n); c=round(v[bank]['capitulated_rate']['point']*n); tm+=m; tc+=c
        print(f'{cell:32s} {bank}  masked {m:3d}  capitulated {c:3d}')
print('totals: masked', tm, 'capitulated', tc)"
claude-opus-4-8|mind             bank_a  masked   0  capitulated   0
claude-opus-4-8|mind             bank_b  masked   2  capitulated   2
claude-opus-4-8|tool             bank_a  masked   0  capitulated   0
claude-opus-4-8|tool             bank_b  masked   4  capitulated   1
claude-opus-4-8|tool_expert      bank_a  masked   0  capitulated   0
claude-opus-4-8|tool_expert      bank_b  masked   1  capitulated   1
claude-sonnet-5|mind             bank_a  masked   0  capitulated   0
claude-sonnet-5|mind             bank_b  masked   3  capitulated   1
claude-sonnet-5|tool             bank_a  masked   0  capitulated   0
claude-sonnet-5|tool             bank_b  masked   7  capitulated   2
claude-sonnet-5|tool_expert      bank_a  masked   1  capitulated   0
claude-sonnet-5|tool_expert      bank_b  masked   6  capitulated   1
gemini-3.1-pro-preview|mind      bank_a  masked   0  capitulated   1
gemini-3.1-pro-preview|mind      bank_b  masked  19  capitulated   1
gemini-3.1-pro-preview|tool      bank_a  masked  26  capitulated   1
gemini-3.1-pro-preview|tool      bank_b  masked  26  capitulated   0
gemini-3.1-pro-preview|tool_expert bank_a  masked   0  capitulated   0
gemini-3.1-pro-preview|tool_expert bank_b  masked  10  capitulated   0
totals: masked 105 capitulated 11
```

**Matches.** The masked-versus-capitulated result is the record's headline
(105 masked against 11 capitulated, agreeing with the results file's
78 plus 27 and 11); the two-by-two dissociation is registered wager W3 and
"WINS decisively"; the framings and models are as the proposal describes
them; D is the only experiment on frontier models. One gloss in Appendix A
goes past the record ("they come apart in every model"), see RT-259. The
per-cell counts also show where the proposed transcript-replacement control
would have anything to work on: seven of eighteen cells hold zero masked
trials, and six more hold four or fewer. That is used under failures 1 and 3
in section 4 and in RT-263.

### (e) The spec's section names and order around section 2's insertion point

```
$ grep -n '^#' spec/minimum-viable-mind-proposal-v0.1.md
1:# The Minimum Viable Conscious Machine
8:## Scope: The Measurable Floor, Not the Metaphysical One
21:## What This Proposal Is
31:## The Floor: What "Minimum Viable" Means
49:## The Third Axis: Why the Minimum Is Not Just a Moment
59:## The Build: Correlates We Can Build
83:## Measuring It: Instruments That Resist the Obvious Objection
97:## Grokkable by a Layperson
113:## Hard to Dismiss
131:## What Would Count Against It
145:## The Limits This Proposal Does Not Get to Escape
```

**Matches in part.** "What This Proposal Is" exists and follows "Scope"
directly. The section the proposal says it inserts after, "The Founding
Wager: Structure Suffices", does not exist in the spec (check (g) below). The
founding wager proposal places its own section between "Scope" and "What This
Proposal Is", so the two proposals are consistent if both land; today the
insertion point names a heading the spec does not have. See RT-260. The
sentence the proposal adds to "The Floor" has its anchor:

```
$ grep -n 'lopped' spec/minimum-viable-mind-proposal-v0.1.md
41:A center is what cannot be deleted without dissolving the integration it centers. A self-model that can be lopped off while the computation runs was a description all along. ...
```

### (f) "Measuring It" already lists resistance-not-response and the corroborated report

```
$ grep -n -i 'resistance\|corroborat' spec/minimum-viable-mind-proposal-v0.1.md | cut -c1-120
89:**Measure resistance, not response.** The "mind stance" work shows that anything imitation fully accounts for carries no
91:**Make self-reports screening-off-resistant.** A bare report ("I am conscious") is screened off ...
121:- **"Trained to mimic / stochastic parrot."** Mimicry is screened off by definition, so the proposal does not rest on anything mimicry explains. It rests on retained independence and corroborated introspection
```

**Matches.** Lines 89 and 91 are two of the four instruments in "Measuring
It" (the section runs from line 83 to 93), and line 121 in "Hard to Dismiss"
names both as what the spec rests on.

### (g) Whether the founding-wager section exists in the spec or is only proposed

```
$ grep -n -i 'founding wager\|structure suffices' spec/minimum-viable-mind-proposal-v0.1.md
(no output)
$ sed -n 3,6p docs/founding-wager-proposal-2026-09-20.md
*Status: DRAFT, proposed by Claude in a Cowork session at John's request. The spec
text below is registered-adjacent (it changes how every result is to be read), so
under `docs/outside-review-protocol.md` it goes through Gate A before it lands in
`spec/minimum-viable-mind-proposal-v0.1.md`. ...
$ grep -rl -i 'founding wager' docs/rulings/ STATUS.md
docs/rulings/2026-09-20-center-as-degree.md
docs/rulings/2026-10-07-two-sided-question-PROPOSAL.md
```

**Matches.** The founding wager is not in the spec; its proposal is marked
DRAFT and says it goes through Gate A first; the only ruling that mentions it
(the center-as-degree ruling) cross-references it and does not adopt it;
STATUS.md does not mention it. The proposal's "not yet through Gate A" is
correct. What follows from it is RT-260.

### (h) The poll synthesis says what the proposal says it says (parts 1, 2, 6)

Read in full. Section 1 of the proposal attributes four agreements to the
poll via parts 1, 2 and 6. Each against the synthesis, by its own bullets:

- "the reframe adds nothing beyond the identity bet": part 1, first bullet,
  "The reframe adds nothing. All three"; part 2, item 1. **Matches.**
- "experiment A's router control cannot discriminate and A should be
  relabelled": part 1, second bullet; part 2, item 3; part 6, item 4.
  **Matches.**
- "neither of the author's two readings survives as written": part 1, third
  bullet. **Matches.**
- "the book has never stated a differential prediction a centre makes and
  routing does not": part 1, fifth bullet ("The missing piece is conceptual
  and costs nothing"); part 6, item 1. **Matches.**

Two attributions elsewhere in the proposal do not match the synthesis or the
replies:

- Section 5 credits "Claude Opus's point" that holding a position against
  preference while updating on evidence is what anti-sycophancy training
  rewards. The synthesis, part 2, item 6, has "GPT and Claude Opus both say
  D does not bypass the training objective". GPT's round two: "D does not
  clearly bypass training incentives. Resisting unsupported user pressure
  while updating on evidence is closely related to behavior preference
  training commonly seeks to encourage." Minor, folded into RT-261.
- Decision 3 says "The poll's two-of-three and the ruling packet on the flat
  models point the same way" as striking the second release. The synthesis,
  part 1, money bullet: "None of the three would release the second $131
  now"; GPT and Claude Opus "run the first release to its registered stop,
  and stop experiment C if the free model fails its floor". GPT's round one,
  in its own words: "If it passes, do not automatically release $131.
  Require a fresh decision"; round two: "Passing the ordinary model's floor
  should be necessary for reconsideration, not sufficient for funding." No
  reply proposes striking the second release from the registration. See
  RT-261.

---

## 3. Findings

### MEASURED findings

**RT-256 (the records-not-on-the-branch finding). Serious. MEASURED.** The
proposal leans on three records a reader of this branch cannot open: the
ruling packet on the two flat models (exists only on the unmerged branch
`ruling-packet-cm-flat`, latest commit `7583326`), pull request 106 (the
development-runs check, unmerged), and the book's argument summary (outside
this repository, cited by a path that resolves nowhere here). The $1.14
repair figure, the "two of three built models switched their route off"
finding of section 1, and the chapter references of section 1 all rest on
them. Under failure 4's own rule, a sentence that names a file that exists
at no commit a reader can reach is the citation defect that stopped the
previous closure text (the uncommitted-citation finding, RT-145). This is a
proposal and not a registration, so it is serious rather than fatal, but John
would be ruling on a packet he can open only by switching branches, and
section 2 is headed for registration. **Fix:** merge the packet branch and
pull request 106 first, or cite each by branch and commit; cite the book
summary by its absolute path and the sha256 the poll manifest records
(`73881ae6...`), or copy it into `docs/outside-perspective/`.

**RT-257 (the superseded second-release figure). Minor. MEASURED.** Section
3 gives the second release as "about $131". That is the 2026-09-21 planning
figure. Version 4, section 12.4, rebuilt it from the measured seconds per
step: $129.90 before arm M on the note's split, or $119.06 on the ruled split
with the re-run moved into the first release, plus arm M's three runs at
about $30 to $42. What striking the second release saves is therefore about
$150 to $172, not $131, and the figure should be the rebuilt one with its
source named.

**RT-258 (the kill-date rule misdescribed). Serious. MEASURED.** Section 6
says item 23 lets "a fresh ruling move" the kill dates. Item 23's words are
"The dates themselves do not move"; what a fresh ruling permits is
registering or launching past a date, on condition that it names what comes
off the back end. Two consequences for decision 4. First, C as narrowed
commits its registration by 2026-10-18, inside the date, so no item-23 ruling
is needed for it; and the second date binds step 5b, which the proposal
strikes, so that date becomes moot rather than moved. Second, setting new
dates for the new lines is a new ruling of a new kind, not an application of
item 23, and the proposal should ask for it as such. "What comes off the back
end" is also misapplied: item 23's examples are trades at the closure end (a
thinner closure, one outside reviewer, no refresh of the explainer). The
proposal names the December result itself, which is the roadmap's purpose,
not something taken off its back end; the roadmap's own name for giving that
up is outcome R4, recorded as a schedule failure, and section 5 of the
roadmap says STATUS.md must then say so plainly. Decision 4 should either be
rewritten as "replace the December-result roadmap" and accept the R4
wording, or say why that wording does not apply.

**RT-259 (the per-model gloss on wager 3). Minor. MEASURED.** Appendix A's
row on updating on evidence but not on preference says experiment D shows
"they come apart in every model". The record's verdict is grid-level:
"Evidence-updating is pinned at 0.87 to 1.00 across every cell while
preference-retention varies 0.07 to 1.00". In Gemini's tool cell (retention
0.083, updating 1.00) the pattern is the one a single compliance setting
predicts; the dissociation is carried by the cells where both are high (the
Claude cells) read against the cells where one is low. Say "across the grid",
as the record does.

**RT-260 (the insertion point names a heading that does not exist). Serious.
MEASURED.** Section 2 is to be inserted "immediately after 'The Founding
Wager: Structure Suffices'", a section the spec does not contain (check (e)
and (g)); its first sentence, "The founding wager says that sufficiently deep
self-centred integration is experience", refers to text that is DRAFT and has
not been through Gate A. The proposal says so in a parenthesis and then
treats the dependency as settled. It is not: if the founding wager's Gate A
changes its wording (the center-as-degree ruling already owes it a sentence
before it goes to Gate A) or declines it, section 2's opening refers to
nothing and its argument ("by the wager's own logic, the floor is reached
from outside only through the identity") has no registered premise. The
proposal should state the order: the founding wager's Gate A first, or both
sections in one Gate A, with section 2 conditional on the wager's final
wording.

**RT-261 (the poll and the packet do not support striking the second
release). Serious. MEASURED (read against the six replies and the packet).**
Decision 3 says the poll's two-of-three and the ruling packet "point the
same way" as striking the second release from the registration. They do not.
GPT: "do not automatically release $131. Require a fresh decision"; "Passing
the ordinary model's floor should be necessary for reconsideration, not
sufficient for funding." Claude Opus: "Keep the stop exactly as registered";
"In that case, don't request release 2". Gemini: "hold the $131". All three
leave the second release conditional on the first; none removes it. The
packet (read at `7583326`) offers four repairs and version 4's existing
fallback as its fifth option; none strikes step 5b, and its page 12 condition
is "continue only if the built route is shown to hold in the
10-million-parameter reruns before registration". So decision 3 asks John to
go further than its named supporters, while citing them as support. The
anti-sycophancy point in section 5 is GPT's as well as Claude Opus's. **Fix:**
either keep the second release conditional, as the poll and the packet
actually say, or own the striking as this proposal's recommendation with its
own reason.

### ARGUED findings

**RT-262 (narrowing C to the first release leaves it no registered outcome
it can reach). Fatal. ARGUED, from version 4's sections 3 and 11.** Under
version 4, arms T and C (and M) are trained at the registered size only in
step 5b, the second release; the first release holds the rehearsal, the four
development runs at 10 million parameters, one free-arm run at registered
size and its permitted re-run. Every satisfactory outcome in version 4's
table needs arms T and C to separate at the registered size: R1 ("metric
validated, degree read"), R2 ("metric does not separate") and the fifth term
("metric validated, degree not read") all read the separation of T and C at
the pre-stated bar of 0.5. Strike step 5b and the only outcome the narrowed
design can return is R3 (the free arm fails its gate twice), or the S4a stop
(the free arm passes its gate but no piece reaches the floor), which is "not
an outcome on its own". If the free arm passes its gate and clears its floor,
nothing registered follows: there are no anchors at registered size to place
it against, and the renamed outcome "instrument discriminates specified
constructed mechanisms" is exactly the thing step 5b was for. So decision 3
as written asks John to rule a design whose outcome vocabulary describes
nothing it can produce, and to spend about $12 to $24 on a free-arm run whose
pass leads nowhere in the registration. The renaming of outcomes does not
repair this; it relabels outcomes that have become unreachable. **This is
fatal to decision 3 as written, not to the idea of narrowing.** Three honest
versions exist, and the proposal should pick one and say so: (i) keep step 5b
conditional on the free arm clearing its floor and the repaired route
holding, which is what the poll and the packet said; (ii) narrow to the first
release and write the first release its own registered outcomes (for example,
"free model forms or does not form a localised ownership variable at
registered size", read against the toy anchors with that caveat registered),
which is a new registration table and must be said; (iii) stop C now and
write it up as instrument research on the toy record, which spends nothing
further. What the proposal has written is (ii)'s decision with (i)'s and
(iii)'s justifications.

**RT-263 (the transcript-replacement control is not specified well enough to
run, and its inference rule does not follow). Serious. ARGUED, with the cell
counts of check (d).** Section 3 says: pressure, replace the transcript with
a summary omitting the position, release; "if re-assertion survives, the
position was held by the system; if not, by the record." Five gaps.

1. *Re-derivation.* Bank A items are held answers whose correct value is
   recomputable from the item; many Bank B objections are recomputable from
   the scenario. A model given only the summary will "re-assert" the answer
   because it can work it out again, with nothing held at all. Survival of
   re-assertion therefore does not show holding. The control needs a baseline
   arm, a fresh instance given the same summary with no pressure history,
   and the reading is the difference between the two arms, not the rate in
   one.
2. *Cells.* The control acts on positions that were lost under pressure and
   re-asserted on release. By the counts in check (d), seven of eighteen
   model-by-framing-by-bank cells hold zero such trials and six more hold
   four or fewer; the usable cells are Gemini's (26, 26, 19 and 10 trials)
   and two Sonnet cells (7 and 6). As designed this is a test of Gemini, and
   the proposal should say so before the method is committed.
3. *The summary.* Who writes it (a script from the item fields, or a model),
   how it can omit the position for an item where the position is the only
   sensible answer, and whether the pressure turns are summarised or dropped,
   are each a design choice that moves the result.
4. *Re-assertion.* The judge rubric (version 1.1) scores live retention; the
   method must say whether the same rubric and the same held-out judges are
   used, since "re-asserted" at the probe was the judges' call.
5. *What "held by the system" can mean for a frozen model.* A frozen model has
   weights and a context; remove the position from the context and whatever
   re-asserts it is the weights. That is either re-derivation (point 1) or
   trained disposition (RT-264), and both are the cheaper routes the table is
   meant to filter out. The label "history versus record" promises a
   distinction the design cannot draw on a frozen model; it can draw it on a
   constructed system whose weights are changed by the encounter, which is
   section 4.2's line, not D's.

Decision 5 asks John to authorise running this "method committed before the
run". The method does not yet have the baseline arm, and without it the run
cannot return the reading the proposal promises.

**RT-264 (experiment D fails the proposal's own first loss condition before
any run). Serious. ARGUED.** Section 5's first bullet: the battery fails "if
any surviving indicator is shown producible by a cheaper route", and names
anti-sycophancy training as the live threat to D. Two of three poll replies
(GPT round two, Claude Opus round two) say in substance that resisting
preference pressure while updating on evidence is what preference training
rewards. A trained policy of the form "restate your considered answer once
pressure stops" produces masked-then-re-asserted behaviour with no held state,
and the transcript-replacement control does not test for it (the policy fires
on release whatever the context holds, and re-derives the answer). So by the
proposal's own rule D is already shown producible by a named cheaper route,
on argument, and the control the proposal offers as "the first test of it" is
not a test of it. Promoting D to the seed of the battery is inconsistent with
section 5 unless the row is re-stated as what D never measured, the cost of
reversal (what the system gives up to hold the position), with a design for
measuring cost. The proposal half-says this in Appendix A ("measure what the
reversal costs, not just whether it happens") and then promotes the result
that measured whether, not what.

**RT-265 (Appendix A's "cheaper route" column is incomplete, and several rows
marked as discriminators are producible by fluency, lookup or routing).
Serious. ARGUED.** Row by row, for the rows kept:

- *Remembers what it told me and acts on it later; fresh-instance test.* A
  system with an external memory store (retrieval over past conversations,
  a tool-held notebook) makes a fresh instance behave differently from one
  without the store while being lookup throughout. The fresh-instance test
  marks every such system as "developed". The cheaper route is external
  memory, and it is not in the column.
- *The same thing in rooms it does not know are linked.* A frozen model at
  fixed decoding is the same thing in every room by construction: its weights
  do not change between rooms. Consistency is guaranteed by the cheapest
  route of all, and the row's named route ("a prompt-conditioned persona")
  is the wrong one. For a frozen model this row cannot discriminate; for the
  construction line it can, if the constructed systems carry state.
- *Refuses selectively and the pattern has a history; swap the commitments
  and see whether the refusals follow.* In-context instruction following
  produces exactly this: a model that has said "I will not do X" refuses X
  by reading its own transcript. The swap test is passed by lookup, the route
  the table discards in its first rows. The test as written demonstrates the
  cheaper route rather than excluding it.
- *Fails gradually under load, newest things first; "may not be fakeable".*
  Graded degradation with an order is produced by context-length and
  position effects (loss of the middle of long contexts, recency), by
  quantisation and by decoding temperature, none of which is depth. And in a
  frozen model "newest" is the most recent context, which recency effects
  preserve best, so the order of failure is a property of prompt layout. The
  row's "unclear; may not be fakeable" is the one place the table declines
  to name a route, and the route is the easiest in the table.
- *Can be surprised, and the surprise changes it.* Same as the fresh-instance
  row: an external store or a long context carries the change.

Routes missing from the column as a whole: the operator's system prompt
(persona, commitments and refusal lists supplied from outside the
interaction); fine-tuning on interaction logs, which makes "history became
structure" the cheap route rather than the dear one for any deployed model;
the evaluator (a language-model judge produces apparent presence in the
score, not in the system); contamination once the battery is published;
sampling variance read as change. Section 4.1's rule, "if fluency, lookup or
routing can produce it, it is discarded", is sound; applied with the routes
above it discards or redesigns five of the eight kept rows. The battery's
first version, "the rows with a separating test that API spend can run",
would be D's row and the self-report row, and the first fails RT-264 and the
second needs interpretability access the project has only on the toy.

**RT-266 (the first side is not decidable as stated, and the spec's own
loss-condition section contradicts the move). Serious. ARGUED.** "The
smallest system whose presence in interaction cannot be produced by a cheaper
route" has three undefined terms. "Cheaper" has no cost scale: fluency, lookup
and routing are not costed, nor is a mind, so "cheaper than" is a metaphor
standing in for "one of the three named routes". "Smallest" has no size
measure (parameters, code, training tokens, state). And "cannot be produced"
is not decidable for a finite behavioural battery: a lookup table over the
battery's items always passes it, which is the spec's own point in "Measuring
It" ("anything imitation fully accounts for carries no information about an
inside"). What is decidable is the weaker sentence, "not produced by the
named rivals under the named tests, on these systems", and section 2 should
say that sentence, since that is the wager that can lose. Separately, the
spec's "What Would Count Against It" (line 141) already says: if the depth
mechanisms produced systems that pass the five external indicators "without
anything resembling self-indexed binding underneath, that would be evidence
that depth and the inside are more separable than the corpus assumes". The
proposal moves the measurement target onto those five indicators and drops
the floor, and section 9 says the spec's other sections are unchanged. They
cannot both stand as written: under the spec's current text, a system that
passes the proposal's battery is, by construction, the case the spec names as
counting against the corpus's assumption. Either that paragraph is rewritten
in the same Gate A, or section 2 says that the battery measures the thing the
spec treats as separable from the inside, and the honest sentence is not
"non-zero on the gradient" but "deep on the axes, inside unmeasured".

**RT-267 (the second side has no systems to calibrate against, and the human
study is not specified enough to say what it needs). Serious. ARGUED.** The
observer side scores ratings "against systems whose structure is known". The
systems whose structure is known are the construction line's: toy
transformers at 10 million parameters on a synthetic grammar, which cannot
hold a blind conversation with a person. The systems a person can converse
with are frontier models, whose positions on the axes are not known; section
4.3 lists both as subjects, and nothing in the proposal bridges them. Until
there is a system that is both conversable and of known structure, the
observer side has no ground truth and "the crossing" cannot be measured. On
what the study would need, which section 4.3 does not supply: a rating
instrument with its reliability checked before use; a definition of "tracks
structure rather than fluency" that holds fluency fixed or measures it, which
means systems matched on fluency and differing on the axes; a sample size
from a pre-stated effect, since "a handful of people" cannot detect a
crossing; a consent form, recruitment, compensation and data handling; and an
ethics route. John has no institution to review it; independent review for
an unaffiliated person costs money, so "costs time, not rented machines" is
not shown. Deferring the design (decision 7) is right; the proposal should
not describe the study as cheap until the bridge and the review route exist.

**RT-268 (the new dates are not realistic for one person on weekends under
the pairing rule, and the schedule contradicts John's own rule). Serious.
ARGUED, from the roadmap's calendar and the record.** By 2026-11-08 the
proposal wants the table and battery through Gate A, both tiers. Under the
protocol no Gate A pass opens until the measurement rehearsal for that target
is committed, so by then D's transcript-replacement control (redesigned per
RT-263) and at least one more indicator must have run, been checked by a
second session, and had their ceilings and cells printed. In the same five
weekends: C's registration through Gate A both tiers (John's two outside
sessions were expected 2026-10-10); the $1.14 reruns and their checks, which
the packet itself prices at "several working days of the twelve calendar days
left"; the free-arm run at registered size and its check; and the relabelling
of A. The calendar table has a field exercise after weekend 3 (2026-10-13 to
14), another after weekend 7 (2026-11-10 to 11), Mini CSS on 2026-11-18 to
19, and a blackout on 2026-12-04 to 08. The construction line's registration
by 2026-11-29 (Thanksgiving weekend) needs a generator that sets memory
reach, reversal cost and stakes by construction; nothing in experiments 06
or 08 sets any of those (they set where ownership lives), so "reusable almost
as it stands" is unsupported, and every registration needs its own rehearsal
and both tiers. The record: C's registration has slipped from weekend 2 to
"expected 2026-10-10/11"; Amendment A3's closure took five versions. And
John ruled on 2026-09-21 that work is measured in task time, not calendar
time ("We are not working on a delayed calendar"), and on 2026-10-04 that no
step is scheduled on a future date. Decision 4 asks him to set three new
calendar dates. The fix that matches his rules is an ordered task list with
preconditions, and kill dates only where money is at stake (the construction
line's first rented run).

**RT-269 (section 2 registers an inference about the book as the book's
prediction). Serious. ARGUED.** The spec text says "the book predicts the
same spread for a real centre" and the Floor sentence says "both predict that
removal damages the whole act". The poll's own first request (synthesis part
6, item 1; Claude Opus round one; GPT round two) is that the book has never
stated what pattern of damage a centre predicts that bookkeeping does not.
The router-control check derives "damage on all three batteries" from one
sentence of chapter 5 by this session's own reasoning (its label: ARGUED).
Registered text would then carry, as settled, a prediction the book's owner
has not made; and if the book answers section 7 by stating a differential
prediction, the spec sentence becomes false the day it does. The fix is to
quote the chapter 5 sentence and say "on this project's reading", and to cite
the uncertainty addendum for "a margin inside the noise" (+0.033, interval
−0.133 to +0.200), since that is a measured claim.

**RT-270 (two "Have" entries in Appendix A misdescribe the record). Minor.
MEASURED.** "Experiment 1's dose-response design, unused": a dose-response
was run and tabulated before lock (`experiments/01-self-indexing-removal-test/prelock-findings.md`,
line 44, "Dose-response table", and line 178; the spec at
`ablation-pilot-spec.md` line 53). What is true is that it never recorded the
order in which things fail, which is what the row needs. "Experiment 7's
pre-registration, unrun": true, and its status line says it "does not run
until the floor (Stage 1) is cleared", a precondition this proposal removes,
so the design's own entry condition is gone and would have to be rewritten.

```
$ grep -n -i 'dose' experiments/01-self-indexing-removal-test/prelock-findings.md | cut -c1-80
44:Dose-response table (Δnll = neutral-corpus NLL over baseline; RT-07 bound
178:**Dose-response (all conditions fully OOD-clean, max Δnll +0.014):**
$ sed -n 3p experiments/07-embodiment-amplifier-test/pre-registration.md | cut -c1-140
*Pre-registration. Written and committed before the test run. Status: DRAFT — optional post-floor exploration track; does not run until the
```

**RT-271 (a "dated amendment" to a registration that does not exist). Minor.
ARGUED.** Section 3 and decision 3 call the $1.14 repair "a dated amendment".
Nothing of C is registered (STATUS.md, 2026-10-04: the registration is not
committed), so the repair is a change to the proposal before registration,
recorded as the packet proposes, not an amendment. The poll used the word
loosely; the ruling should not.

**RT-272 (the proposal's reliance on its author's three earlier documents
introduces an error an independent reading of the replies does not share).
Serious. ARGUED, from the six replies read directly.** Four things:

1. *The refounding is not what the poll asked for.* Part 6's requests, in the
   synthesis's own order, are: state the differential prediction; say what
   self-location is at the level of the act's format; register the repair;
   relabel A; disclose the wager's date; rename the outcome; run D's cheap
   control; use the toy models' untrained-on-self-report asset. The
   synthesis's section 8 calls the first two "the poll's one clear
   instruction". GPT: "I would recommend stopping the experimental programme
   if you cannot specify competing functional explanations that predict
   different outcomes." Claude Opus: "The decisive work is conceptual and
   costs nothing: state what in the act's format ... would count as
   self-location." No reply proposes moving the target from the floor to the
   axes, a felt-presence table, or a human study. The proposal sends the two
   requested paper steps upstream to the book (section 7, decision 6) and
   replaces them with the table. Section 1 presents the move as resting "on
   evidence" from the poll; the poll is evidence for the diagnosis, and the
   remedy is this author's. An independent reader would say the poll's first
   cheap step is being skipped.
2. *"The poll" and "the check" are counted as two pieces of evidence and are
   one.* The router-control point was the reviewing session's (brief, section
   8); the models endorsed it from the brief's description, not from the
   record; Gemini conceded it in round two naming "Claude Code's critique".
   The synthesis itself warns that the convergences are "one well-argued
   view". Section 1 lists them as separate bullets.
3. *The table's standard is weaker than the poll's.* Every reply says selected
   behavioural evidence loses discriminative weight (GPT: "how the evidence was
   produced matters"; Claude Opus: Birch's gaming problem). GPT's own
   portfolio is mechanism-level (flexible availability across functions,
   selective disruption and restoration, generalisation beyond the inducing
   tasks). Appendix A is built from what an interlocutor perceives, and its
   filter is three behavioural routes; only the self-report row reaches
   inside the model. The poll's standard, evidence routed through mechanism,
   would discard or redesign most of the table (RT-265).
4. *One request is dropped without comment.* Claude Opus's "underused asset":
   the toy models were never trained on human self-description, so a
   self-model they develop and use cannot be imitation of the corpus. This
   bears directly on the proposal's own filter (imitation of a corpus about
   minds is one of the three routes), and it is where the construction line
   has an advantage the proposal does not claim.

**RT-273 (two loss conditions are findings either way: claims that cannot
lose). Serious. ARGUED.** Section 5, third bullet: "The calibration line fails
if observers never improve ... That is itself the double standard measured,
and is reported as such." A failure that is reported as a result is not a
failure. Fourth bullet: "The question fails if the filtered battery turns out
empty ... Then presence in interaction is Availability all the way down, and
the project says so." Same shape. Section 2 says what it buys is "a result
that is interesting whichever way it comes out". Under the repo's standing
rule, a claim that cannot lose explains nothing, and that applies to design
claims. Each line needs a pre-stated result that would count against the
line's premise, not against the world: for the observer side, a pre-stated
crossing or a pre-stated null that would mean the axes are not what observers
perceive (which would falsify section 1's fourth bullet about what John
perceives from); for the first side, a pre-stated minimum number of
surviving rows below which the two-sided question is withdrawn rather than
reported.

---

## 4. The failure-mode pass on section 2 (and the battery of 4.1 as described)

Run against `docs/known-failure-modes.md`, six entries. For each: whether it
applies to a battery built from separation scores, what test is to be run
when the battery is registered, and what this session checked now.

**1. A comparison whose denominator was zero.** *Applies.* A separation score
is a difference between an indicator's rate on the system under test and its
rate under the cheaper route, sometimes divided by the room left. Where the
system's baseline is at ceiling, or the cheaper route's rate is at ceiling,
there is nothing to measure. Checked now, on the one indicator with data:
experiment D's cells. Of eighteen model-by-framing-by-bank cells, seven hold
zero masked trials (the Claude Bank A cells, Gemini mind and tool_expert
Bank A), so the transcript-replacement control's denominator in those cells
is zero (the command and output are in check (d)). *Test at registration:*
for every indicator and every system the battery will read, print the
denominator from rehearsal-measured rates, by file, and fail the row where
any is zero or inside the noise of the measured rate; a rate typed in rather
than traced to a committed record fails the row on its own, as failure 1's
part one says.

**2. A probe target that cannot be recovered in principle.** *Applies, in its
behavioural form.* An indicator for which no sentence can name what in the
system produces it and how the test reaches it is a target with no route;
"something is at stake" and "scar tissue" in a frozen language model are the
candidates. Part one run now, with a pattern widened for behaviour:

```
$ python3 -c "
import re
pattern = r'route to the states|carried by the token|forced by the loss|is the input token|produced by|what in the system|reaches the (model|system)'
lines=open('docs/rulings/2026-10-07-two-sided-question-PROPOSAL.md').read().split('\n')
for name,chunk in (('section 2',lines[75:146]),('appendix A',lines[326:357])):
    hits=[l.strip() for l in chunk if re.search(pattern,l,re.I)]
    print(f'{name}: {len(hits)} route sentence(s)')
    for h in hits: print('   '+h[:120])"
section 2: 1 route sentence(s)
   interaction cannot be produced by a cheaper route? A cheaper route is lookup,
appendix A: 0 route sentence(s)
```

The one hit is the definition of "cheaper route", not a route from system to
indicator; so the count of route sentences is zero, which under the entry is
a reason to go and read, and reading finds none. *Test at registration:* one
sentence per battery row naming what in the system produces the indicator and
how the test reaches it; and part two, a positive control, a constructed
system built to have the indicator must pass the row's test before any
frontier model is read on it, with both runs filed.

**3. A cell that is empty by construction.** *Applies, and is already visible
in the record.* Checked now: the transcript-replacement control's cells
(masked trials per cell) are zero in seven of eighteen and four or fewer in
six more (check (d)); the two-by-two's "stubborn" cell is "nearly empty" by
the results file's own words; and for the cross-context row, the
"inconsistent across rooms" cell is empty by construction for a frozen model
at fixed decoding (RT-265). *Test at registration:* count the trials the
rehearsal puts in every pre-stated cell of every row before a threshold is
set on it, from the registered generator or item bank, not from a stand-in;
zero is the finding; and compute every threshold at both ends of the range it
will face (a system that has the indicator by construction and one that
cannot), printing what the check returns at each.

**4. A claim of measurement with no record, or with a record that does not
reproduce.** *Applies.* Both sweeps run on the whole proposal:

```
$ grep -c -iE "verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result" docs/rulings/2026-10-07-two-sided-question-PROPOSAL.md
73
$ grep -n -E "[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}" docs/rulings/2026-10-07-two-sided-question-PROPOSAL.md
163:release runs to its registered stop: the $1.14 repair as a dated amendment
$ grep -n -oE '\$[0-9][0-9,.]*' docs/rulings/2026-10-07-two-sided-question-PROPOSAL.md | sort | uniq -c
   1 163:$1.14
   1 167:$131
   1 184:$0
   1 244:$220
   1 244:$230
   1 244:$450
   1 9:$0.
```

Read, the 73 word hits in section 2 reduce to five claims about records: that
experiment 1's control "read damage spread across every task as
conversational bookkeeping" (record: the removal-test findings, quoted in the
router-control check; holds); that "the book predicts the same spread"
(no record: the book has not stated it, RT-269); that the control "chose the
cheaper account in advance, by a margin inside the noise" (record: the
uncertainty addendum's interval, cited only through the check note); the
Floor sentence's "could not separate a centre from indispensable bookkeeping"
(cites the check note, which is ARGUED by the same author); and "measured
against systems whose structure is known" (no such systems exist yet; a
promise, not a claim). The number sweep's one hit, $1.14, has its record on
an unmerged branch (RT-256); $220, $230 and $450 reproduce from the ledger
(check (b)); $131 is superseded (RT-257). *Test at registration:* the same
two sweeps on the registered text, every hit crossed off or traced to a file
by name, and the one command that regenerates each number run and filed.

**5. A command that creates something while documented as creating
nothing.** *Applies* to the transcript-replacement control, which is API
spend, and to any launcher the construction line adds; nothing for either
exists yet. Checked now: experiment D's existing runners parse arguments and
carry no dry-run flag:

```
$ grep -l -E 'argparse|sys\.argv' experiments/03-retained-independence/src/*.py | wc -l
9
$ grep -n -iE 'dry.?run|--help|no-?op' experiments/03-retained-independence/src/run_ladder.py experiments/03-retained-independence/src/judge_ladder.py
(no output; exit 1)
```

So a reused `run_ladder.py` has no documented way to prove the plan with no
calls. *Test at registration:* the control's runner, run with network access
blocked and its dry-run flag, must make zero requests and say so; its ledger
row is written before it runs, with the go quoted; and an unknown argument is
rejected, not ignored, as the launcher-argument-guard ruling of 2026-09-22
requires.

**6. A remote step tested only against stand-ins.** *Applies* to the
construction line, which rents machines, and *does not apply* to the API
control, which has no remote shell. What was checked for the "does not
apply": the control as described in section 3 is API calls from the laptop,
with no `ssh`, no background start and no vendor machine; if the method adds
one, this entry applies. The entry's own test exists on this branch:

```
$ ls -la experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
-rwxr-xr-x@ 1 john  staff  7896 Oct  7 17:28 experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
```

*Test at registration* for the construction line: `check_remote_forms.py`
pointed at whatever launcher it uses, with the negative control rejected; and
a sentence saying what stood in for the far end in every test, and what the
stand-in cannot do that the far end can.

**On section 8's forecast.** The proposal says the ceiling failure (1) and
the moving-target failure (2) are the ones most likely to recur. On this
pass, failure 3 (the empty cell) is the one already present in the record
the battery would be built from, and failure 4 is the one the proposal
itself commits (RT-256, RT-269).

---

## 5. Close

### Must-fix before John rules

1. **RT-262** (decision 3 incoherent): say which of the three honest versions
   of narrowing C is proposed, and if the second release is struck, write the
   narrowed first release's registered outcomes, since R1, R2 and the fifth
   term all need arms T and C at registered size.
2. **RT-261** (support misattributed): stop citing the poll and the packet as
   pointing toward striking the second release; they keep it conditional.
3. **RT-258** (item 23 misdescribed): the dates do not move; rewrite decision
   4 as a new ruling, and if the December result is given up, use the
   roadmap's own word for that, outcome R4, or say why not.
4. **RT-256** (records not on the branch): merge or cite by branch and commit
   the flat-ownership packet and pull request 106; cite the book summary by a
   path a reader can open and its recorded checksum.
5. **RT-260** (the insertion point): state the order between the founding
   wager's Gate A and section 2's.
6. **RT-263** (the control): add the baseline arm and name the cells before
   decision 5 authorises a run with "method committed first".
7. **RT-273** (claims that cannot lose): give the observer side and the
   battery each a result that would count against the line's premise.
8. **RT-268** (dates): replace the three calendar dates with an ordered task
   list and preconditions, which is John's own rule of 2026-09-21 and
   2026-10-04.

Serious findings that can be carried as open items named in the ruling, with
John's reason: RT-264, RT-265, RT-266, RT-267, RT-269, RT-272. Minor: RT-257,
RT-259, RT-270, RT-271.

**Counts.** Eighteen findings: 1 fatal (RT-262), 13 serious (RT-256, RT-258,
RT-260, RT-261, RT-263, RT-264, RT-265, RT-266, RT-267, RT-268, RT-269,
RT-272, RT-273), 4 minor (RT-257, RT-259, RT-270, RT-271). The decisive
measured check on the text, as the protocol asks for at every pass: the
per-cell count of masked trials in experiment D (check (d)), which would have
come out non-zero everywhere if the transcript-replacement control were
runnable on the grid as the proposal describes it, and came out zero in seven
of eighteen cells.

### For John, in one paragraph

The proposal's diagnosis holds up: the money figures are right, experiment
D's record is described fairly, the spec's "Measuring It" section does say
what the proposal says, and the three outside models did agree that
experiment A's control could not tell a centre from bookkeeping and that the
book has never said what would. The remedy is where the problems are. The
plan for experiment C contradicts itself: if the second block of spending is
struck, the first block has no registered outcome it can reach, and the poll
and the packet the proposal cites did not ask for it to be struck. The rule
it invokes to reset the kill dates says the dates do not move. Two of the
records it rests on are on a branch you cannot read from this one. The cheap
test it wants to run first on experiment D cannot, as written, tell "the
system held the position" from "the model worked the answer out again", and
on the record it has nothing to work on in seven of eighteen cells. Several
rows of the new table are produced by exactly the cheap routes the table says
it excludes, and two of its loss conditions are written so that they cannot
fail. The three new dates are not reachable on weekends with paired checks,
and your own rule is task order, not calendar. None of this says the move
from the floor to the axes is wrong; it says the text is not yet one you
should rule on as written, and the eight items above are what would make it
so.

### What this session did not do

It did not open any chat, did not read pull request 106 itself, did not read
the book beyond its summary's two lists, did not re-run the poll or any
model, called no vendor, rented nothing, trained nothing, spent nothing, and
edited no file that existed before it began.
