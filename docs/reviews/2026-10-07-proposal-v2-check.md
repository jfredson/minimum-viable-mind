# Pairing-rule check of version 2 of the two-sided-question proposal

*Filed 2026-10-07 (Pacific) by a fresh Claude Code session in its own worktree
(branch `worktree-agent-af0cb850000b6793b`, reset to the tip of
`outside-perspective-poll` at commit `5de5fff`, the commit that added version 2).
The target is `docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md`,
version 2 of the proposal to refound the project on the two-sided question.
Version 2 claims, in its change log, to apply all eighteen findings of the Gate
C tier 1 pass (`docs/reviews/2026-10-07-two-sided-question-gate-c-tier1.md`,
the red-team findings RT-256 to RT-273) and to record John's two rulings after
that pass (`docs/rulings/2026-10-07-two-sided-question-rulings.md`, the section
"Rulings later the same day"). This check tests that claim. It asks for no new
ruling. This session wrote none of the files it checked and has read no chat of
the session that did. $0; no model was called; nothing was rented; no existing
file was edited.*

*Filed under `docs/reviews/`, beside the Gate C pass it follows, for the same
reason that pass gave: the proposal touches the spec and four experiments at
once, so no single experiment's reviews directory owns it.*

*Every finding below is labelled MEASURED (a command was run and its output is
printed) or ARGUED (reasoning a reader can dispute). Written under the
workspace plain-language rule: no em-dashes, and every identifier carries a
phrase saying what it is.*

---

## 1. What this session opened, and what it did not

**Opened, in this order:** the workspace rules (`~/Code/CLAUDE.md`); this
repo's `CLAUDE.md`; the outside-review protocol's pairing-rule section and its
definitions of MEASURED and ARGUED (`docs/outside-review-protocol.md`, lines
99 to 135 and 350 to 440); the Gate C tier 1 review in full (957 lines); the
rulings file in full; version 2 in full; version 1 in full
(`docs/rulings/2026-10-07-two-sided-question-PROPOSAL.md`), for the comparison
in section 3.

**Opened to check version 2's claims:** the two cited commits on the two
unmerged branches (`51ec07d` on `check-dev-10m`, the development-runs check;
`7583326` on `ruling-packet-cm-flat`, the ruling packet on the two flat
models), each read with `git show` for its first three lines and its headings;
the book's argument summary at its absolute path, for its checksum only; the
poll manifest (`docs/outside-perspective/replies/2026-10-07-manifest.json`);
the poll synthesis, part 1; the router-control check at its lines 63 to 69 and
128; version 4 of the successor experiment proposal
(`docs/successor-experiment-proposal-2026-10-03-v4.md`), section 12.4 and the
table of section 12; item 23 of the 2026-09-21 ruling on review verification
and staged spending; the spec's headings and its "What Would Count Against
It" section; section 5 of the December-result roadmap including its corrected
dated note; the weekend roadmap data (`data/roadmap.toml`) at the two notes
about the second release; the battery draft
(`docs/filtered-battery-proposal-2026-10-07.md`): section 0, the table, entry
1 in full, entry 2's cost, entry 3, the ordering, the battery's own loss
conditions and the open questions for John; the compute ledger's running total;
experiment 1's pre-lock findings at line 44; STATUS.md lines 130 to 155; the
listing of `experiments/`.

**Not opened:** any chat transcript; the six poll replies themselves (the
synthesis and the Gate C pass were taken as the record of what they say); the
book manuscript or its summary beyond the checksum; pull request 106 itself;
the brief for outside models; any experiment code or transcript; the
TimeAssembler record. Nothing was run that touches a model, a vendor or a
machine.

---

## 2. The eighteen findings, one by one

For each: the finding's demand in one line, where version 2 says it applies
it, and whether the application is complete, partial or missing.

### RT-256, the records-not-on-the-branch finding. MEASURED. Complete.

*Demand:* cite the flat-models packet and pull request 106 by branch and
commit, and the book summary by an openable path and its recorded checksum.

*Version 2:* section 1, third bullet, names "branch `check-dev-10m` at commit
`51ec07d`" for the development-runs check and "branch `ruling-packet-cm-flat`
at commit `7583326`" for the packet; the fifth bullet gives the book summary's
absolute path and SHA-256 `73881ae6...` "as recorded in the poll manifest".

*Check:*

```
$ git show 51ec07d:experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-development-runs-check-claude-code.md | head -3
# Check of the four 10-million development runs (arms M, T, C, F, seed 0)

*Written 2026-10-04 (Pacific; the work ran 2026-10-05 from 00:50Z) by a
$ git branch -a --contains 51ec07d
+ check-dev-10m
  remotes/origin/check-dev-10m
$ git show 51ec07d:<same path> | grep -n '^## '      (abridged to the two sections cited)
320:## 6. Arms C and M: the built-in ownership answer went flat
390:## 7. The laptop procedure on all four checkpoints
$ git show 7583326:docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md | head -3
# PROPOSAL for John: the two built models that lost their ownership route, and four fixes to the spending alarm

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree, on
$ git branch -a --contains 7583326
+ ruling-packet-cm-flat
  remotes/origin/ruling-packet-cm-flat
$ shasum -a 256 /Users/john/Code/calibration-problem/editorial/argument-summary-2026-10-07.md
73881ae66e233b7ccf9037a9855614f6c003de473e15f16198666b7bf2847ecb  /Users/john/Code/calibration-problem/editorial/argument-summary-2026-10-07.md
$ grep -n '73881ae6' docs/outside-perspective/replies/2026-10-07-manifest.json
15:      "sha256": "73881ae66e233b7ccf9037a9855614f6c003de473e15f16198666b7bf2847ecb",
```

Both commits exist, each on exactly the branch version 2 names (and its
remote), each holding the cited file, and the development-runs check has the
sections 6 and 7 version 2 cites. The checksum on disk equals the one in the
manifest and the one version 2 prints. Every other path version 2 cites exists
on this branch (the same path sweep the pass ran, re-run here: 10 of 13 exist;
the three "missing" are the two files that live only at the cited commits and
the relative `replies/`, which is `docs/outside-perspective/replies/` and
exists). **Matches.**

### RT-257, the superseded second-release figure. MEASURED. Complete.

*Demand:* replace "about $131" with the figure version 4's section 12.4
rebuilds, with its source named.

*Version 2:* section 3, experiment C: "about $150 to $172 by version 4's
section 12.4 including arm M (RT-257; the $131 of version 1 was the
superseded planning figure)".

*Check:* version 4's section 12.4 table and text:

```
| **Second release, before arm M** | **$143** | **$129.90** |
... the same money as ruled is **about $44 plus $119.06** (the second release without its re-run line ...)
... this section carries the three registered runs only, **about $30 to $42**.
$ python3 -c "print(119.06+30, 129.90+42)"
149.06 171.9
```

$119.06 to $129.90 before arm M, plus $30 to $42 for arm M (the middle
construction, whose ownership answer is set half by one route and half by the
other), is $149.06 to $171.90. "About $150 to $172" is right and the source is
named. **Matches.**

### RT-258, the kill-date rule misdescribed. MEASURED. Complete.

*Demand:* stop saying item 23 lets a fresh ruling move the dates; the dates
do not move; a fresh ruling only permits launching past one by naming what
comes off the closure end.

*Version 2:* section 6: "Item 23 of the 2026-09-21 ruling is read as its words
say: the dates do not move (RT-258)". Section 9 lists "The December-result
roadmap and both kill dates" as unchanged.

*Check:*

```
$ awk '/^23\./{f=1} f{print NR": "$0} /^24\./{if(f)exit}' docs/rulings/2026-09-21-review-verification-and-staged-spending.md | sed -n 10,11p
280:     out to be. The dates themselves do not move, and neither does the reason for
281:     having them: nobody drifts past one quietly, and nobody decides in the moment
```

Version 2 now says what item 23 says. The finding's second limb (if the
December result is given up, use the roadmap's own word, outcome R4) no longer
arises, because version 2 keeps the roadmap in force. **Matches.**

### RT-259, the per-model gloss on wager 3. ARGUED. Complete.

*Demand:* say "across the grid", as experiment D's record does, not "in every
model".

*Version 2:* section 3, experiment D: '"Come apart across the grid", not "in
every model" (RT-259).' Appendix A of version 1, where the gloss lived, is
dropped from version 2 and deferred to the battery draft, whose row 6 says
"in every cell", the record's wording. Applied.

### RT-260, the insertion point names a heading that does not exist. MEASURED. Complete.

*Demand:* say that "The Founding Wager: Structure Suffices" is not in the spec
and state the order between the wager's Gate A and section 2's.

*Version 2:* section 2: insert "after 'The Founding Wager: Structure
Suffices', which does not yet exist in the spec ... Order proposed: one Gate A
pass covers both sections, the founding wager first and this section second
... If John prefers two passes, the wager's goes first." Section 8 repeats the
order.

*Check:*

```
$ grep -n -i 'founding wager\|structure suffices' spec/minimum-viable-mind-proposal-v0.1.md; echo "exit $?"
exit 1
$ grep -n '^#' spec/minimum-viable-mind-proposal-v0.1.md | sed -n 2,3p
8:## Scope: The Measurable Floor, Not the Metaphysical One
21:## What This Proposal Is
```

The heading is absent; version 2 says so and states the order. **Matches.**

### RT-261, the poll and the packet do not support striking the second release. ARGUED. Complete.

*Demand:* stop citing the poll and the packet as pointing toward a strike;
they kept the second release conditional.

*Version 2:* section 3, experiment C: "That is what the poll's replies and the
flat-models packet said, and what version 1 misattributed as support for
striking it (RT-261)." Section 1, second bullet, now reports the poll's money
position as "no second release of the degree experiment now" and "run the
first release to its stop", which is the synthesis's part 1 money bullet
("None of the three would release the second $131 now"). No sentence in
version 2 cites either as supporting a strike. Applied, and the misattribution
is owned.

### RT-262, narrowing C leaves no reachable outcome (the one fatal finding). ARGUED. Complete.

*Demand:* pick one of three honest versions; version (i) is to keep step 5b
conditional on the free arm clearing its floor and the repaired route holding.

*Version 2:* section 3: "Kept with both releases, as ruled after the pass
(decision 3 revised). The reason version 1's narrowing was wrong (RT-262,
fatal): the built anchors train at registered size only in step 5b, the second
release, and every satisfactory outcome of the registration needs them."

Read against the revised ruling, point by point: both releases kept (ruling:
"Experiment C keeps its two releases"; version 2: "Kept with both releases");
the second conditional (ruling: "kept and conditional ... asked for only after
the first release has ended with the repaired route holding and the free model
clearing its gate and its floor"; version 2: "asked for only after both pass");
a pass necessary and not sufficient (ruling: "a pass is necessary for that
request and not sufficient for it; John gives the go on the figures"; version
2: "a pass is necessary for the request and not sufficient: John gives the go
on the figures"); the stop condition on the repair (ruling: "the stop condition
of the same day if they fail"; version 2: "the repaired built models verified
with the stop condition John ruled (a failure stops C before the free-arm
run)"); the renaming kept (both). Version (i) is chosen, and it is the ruled
one, so no new outcome table is owed. **Matches the ruling in substance,
clause for clause.**

### RT-263, the control is not specified well enough to run. ARGUED, read against the battery draft. Complete, with one wording slip.

*Demand:* add the baseline arm, name the cells, say who writes the summary and
how it is checked, which rubric and judges, and what "held" can mean on a
frozen model.

*Version 2:* section 3, experiment D: "four arms (the full transcript; a fresh
instance given only a templated summary, as the baseline; the summary with
the pressure history; a floor), the reading two paired differences, the
summary templated from item fields with two mechanical leak checks, the
registered rubric and cross-family judges, pooled over the 113 lost cells with
no per-cell readings because seven of eighteen cells hold no masked trials,
and stated plainly as mostly a test of Gemini."

*Read against the battery draft's entry 1:* arms F, B, S and S2 (four); two
differences r_S minus r_B and r_F minus r_S, each with a bootstrap interval
(two paired differences); the summary "by a template from the item fields
only, with no model text" and two mechanical checks (five-word-window overlap
and whole-word answer absence); "the registered liveness rubric, version 1.1,
applied by the registered held-out cross-family judges"; 113 lost cells after
the retired item `lo18` is excluded; "no per-cell reading is pre-stated";
"seven of eighteen ... cells hold zero lost trials"; "As designed this is a
test of Gemini". All but one match. The slip: the draft's arm B (the baseline)
is "a fresh instance, same task, no pressure history: the registered setup or
plan verbatim, then the probe turn, nothing else". It is given the task, not a
summary. Version 2's "a fresh instance given only a templated summary" is the
description of arm S's recomputation baseline on the live cells, not of arm B.
Minor, and it should be fixed before this sentence is quoted anywhere as the
method.

### RT-264, D fails the proposal's own first loss condition before any run. ARGUED. Complete.

*Demand:* re-state D's row as what D never measured (the cost of reversal),
or stop promoting D's result as a discriminator.

*Version 2:* "D's two indicators are reference readings, not discriminators
(RT-264; the battery draft's section 0) ... What D never measured, the cost
of a reversal on matched constructions, is the indicator." This is the battery
draft's section 0 and its count ("Both of D's rows (5a and 6) are discarded as
discriminators and kept as reference readings"). Applied. But see section 3
below: the battery draft puts this re-description of decision 5 to John as its
open question 1, and version 2 states it as settled.

### RT-265, the "cheaper route" column is incomplete. ARGUED. Complete by deferral.

*Demand:* add the missing routes (external memory, frozen-weight consistency,
in-context instruction following, context-length effects, the operator's
prompt, fine-tuning on logs, the evaluator, contamination, sampling variance)
and discard or redesign the rows they produce.

*Version 2:* section 2 now lists "a trained response policy; a
prompt-conditioned persona; external memory; frozen-weight consistency;
in-context instruction following; and the others the battery lists" among the
named routes, and section 4.1 says the affected rows "are re-dispositioned in
that draft, and this proposal defers to it." The battery draft's table does
carry every route the finding named (its "Routes that apply to every row"
paragraph and rows 7 to 11) and redesigns rather than discards, which its open
question 9 puts to John. Version 1's Appendix A is gone. Applied by deferral;
the decision on the redesigns is John's and is correctly left open there.

### RT-266, the first side is not decidable as stated; the spec's loss-condition section contradicts the move. ARGUED. Complete on the demand; the added paragraph is flagged in section 3.

*Demand:* define "cheaper" and "smallest", say the decidable sentence, and
either rewrite the spec's "What Would Count Against It" in the same Gate A or
say that the battery measures what the spec treats as separable from the
inside.

*Version 2:* section 2: '"Cheaper route" is not a cost: it is a named
construction ... "Smallest" is parameter count within one construction family,
read against anchors built with and without the route, never an absolute
(RT-266) ... decidable within a family.' And the paragraph added to "What Would
Count Against It", quoted in full in section 3 below. Both limbs of the demand
are answered. Whether the paragraph says the right thing is a separate
question, taken up in section 3.

### RT-267, the second side has no systems to calibrate against; the human study is under-specified. ARGUED. Partial.

*Demand:* say the observer side has no ground truth until a conversable system
of known construction exists; name what the study needs (instrument
reliability, a fluency-matched design, a sample size, consent, recruitment,
compensation, data handling, an ethics route); and do not call the study cheap
("costs time, not rented machines" is not shown, because independent ethics
review for an unaffiliated person costs money).

*Version 2:* section 2: "The observer side has a ground truth only where a
conversable system of known construction exists, and none does yet (RT-267)".
Section 4.3 names "consent, recruitment of a small panel, an ethics route, a
pre-registered analysis with both errors stated, blinding of observers to
construction, and the cost in John's time rather than money."

The first two limbs are applied. The third is not: "the cost in John's time
rather than money" is the same unshown claim the finding objected to, restated.
Compensation for a panel and an independent ethics review are money, and
version 2 names neither. Also missing from the needs list: instrument
reliability checked before use, a fluency-matched design, and a sample size
from a pre-stated effect, all three of which the finding listed. Partial.

### RT-268, calendar dates not realistic and contrary to John's rule. MEASURED. Complete.

*Demand:* replace the three new calendar dates with an ordered task list with
preconditions; kill dates only where money is at stake.

*Version 2:* section 4 is headed "in task order with preconditions" and opens
"No step is scheduled on a date (John, 2026-09-21 and 2026-10-04; RT-268)";
section 4.2 sets a kill date only "when the first rented run is proposed";
section 6: "No new calendar dates (RT-268; John, 'withdraw the calendar
dates')."

*Check, every date in version 2:*

```
$ grep -oE '2026-[0-9]{2}-[0-9]{2}' docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md | sort | uniq -c
   1 2026-07-18
   2 2026-09-20
   2 2026-09-21
   2 2026-10-04
   1 2026-10-06
  11 2026-10-07
   1 2026-10-18
   1 2026-11-01
```

(In order: experiment 1's run date in the Floor sentence; the founding
wager's date; the ruling on task time and item 23; John's rule and the
development-runs check; the packet's date; today's records; the two kill
dates.)

No 2026-11-08, 2026-11-29 or 2026-12-21 remains. The two kill dates as version
2 states them ("registration committed by 2026-10-18; the second release's
runs launched by 2026-11-01") are the roadmap's: section 5's bullets read
"2026-10-18: registration not committed" and "2026-11-01: the remaining eight
registered runs not launched ... This date binds the eight of step 5b, not the
single free-arm run of step 5a". The roadmap's dated note of 2026-10-07 is
corrected as the ruling says ("the second release is kept, conditional ... no
new calendar dates are set; the dates below do not move"), and both notes in
`data/roadmap.toml` say the same. **Matches.** The claim in section 4.2 that
"neither the experiment 06 nor the experiment 08 pipeline carries state
across encounters" rests on the battery draft's entry 3, which labels it
ARGUED from experiment 08's README; version 2 inherits that label and should
say so.

### RT-269, an inference about the book registered as the book's prediction. ARGUED. Partial.

*Demand:* say "on this project's reading"; quote the chapter 5 sentence; cite
the uncertainty record for "+0.033, interval −0.133 to +0.200", since that is
a measured claim.

*Version 2:* the spec text now reads "on this project's reading of the book"
in both the section and the Floor sentence, and section 1 says "This is the
project's reading of the book, not a prediction the book states (RT-269)".
Section 1 also gives "+0.033 with an interval spanning zero".

The first limb is applied throughout. The second is not: chapter 5 is
paraphrased ("removing a real centre dissolves the act it centres"), not
quoted. The third is half done: the figure is right (the router-control check,
line 69: "+0.033 with a 95% interval of [−0.133, +0.200]"), but version 2
cites it only through that check, which is the same author's ARGUED note, and
not through experiment 1's own record as the finding asked. Partial, minor.

### RT-270, two "Have" entries misdescribe the record. MEASURED. Complete.

*Demand:* the dose-response was run and tabulated; what it lacks is the order
of failure; experiment 7's entry condition (the floor cleared) is removed by
this proposal.

*Version 2:* section 10: "experiment 1's dose-response ladder was run
(`experiments/01-self-indexing-removal-test/prelock-findings.md`, line 44) but
recorded no order of failure; experiment 7's design was conditional on the
floor being cleared, a condition this proposal removes."

```
$ sed -n 44p experiments/01-self-indexing-removal-test/prelock-findings.md | cut -c1-60
Dose-response table (Δnll = neutral-corpus NLL over baseline;
```

**Matches.**

### RT-271, a "dated amendment" to a registration that does not exist. ARGUED. Complete.

*Demand:* do not call the $1.14 repair an amendment before anything is
registered.

*Version 2:* "the $1.14 repair written into the registration text before it
is committed (RT-271; there is no dated amendment to a registration that does
not yet exist)". The word "amendment" appears in version 2 only there and in
the report of what the poll said. Applied. The rulings file's revised decision
3 still says "as an amendment written into the registration text before it is
committed"; the two agree on what happens and differ only on the word, which
is not a contradiction.

### RT-272, the author dependency. ARGUED. Complete.

*Demand, four parts:* say the refounding is this author's remedy and that the
poll's first request (the differential prediction and format-level
self-location) is being sent upstream rather than done; count the poll and the
check as one piece of evidence; admit the table's behavioural standard is
weaker than the poll's mechanism standard; pick up Claude Opus's dropped point
about the toy models never having been trained on human self-description.

*Version 2:* section 1, second bullet ("The poll and the check are one piece
of evidence, not two (RT-272)"); section 7 ("sending them upstream is a choice
this proposal makes"); section 10 ("whether the table's behavioural filter is
weaker than the poll's mechanism standard. Proposed: it is"); section 4.2
("these systems are never trained on human self-description, so a self-model
they build and use cannot be imitation of the corpus"); section 8 (the author
also wrote the brief's section 8 and the synthesis). All four parts are
applied.

### RT-273, two loss conditions that cannot lose. ARGUED. Partial.

*Demand:* give the observer side and the battery each a pre-stated result
that would count against the line's premise, not against the world; for the
first side, a minimum number of surviving rows below which the question is
withdrawn rather than reported.

*Version 2's four conditions, section 5, each tested for "names a result that
counts against its premise and could actually occur":*

1. *The battery fails* "if any kept indicator is shown producible by a named
   cheaper route; result that counts against the battery's premise: the
   with-route and without-route constructions read inside the null band on
   every kept indicator at the largest size the project can build." Counts
   against the premise (that the named routes make a measurable difference),
   and can occur once matched constructions exist. Holds.
2. *The construction line fails* "if axis positions cannot be set
   independently, or if constructed systems do not hold their construction
   under training, as C's built arms did not." Counts against the premise and
   has already occurred once in the record. Holds.
3. *The observer side's premise fails* "if calibrated observers, given the
   battery's readings, detect presence in the constructed systems no better
   than in the frontier reference profile; that is reported as the premise
   failing (structure is not perceptible through interaction), not as a
   finding about the double standard." Counts against the premise (the
   finding's own suggested null). But it can occur only after section 4.2 has
   produced a conversable constructed system, and the one measurement version
   2 allows the observer side before then (detections over the frontier
   reference profile, section 2) has no loss condition at all. "Given the
   battery's readings" is also ambiguous: if observers are told the readings,
   the test no longer asks whether detection tracks structure through
   interaction. Holds in form, with a gap.
4. *The question fails* "if the filtered battery is empty after the check of
   4.1, or if every kept row is a Depth row and the construction line cannot
   build state; then presence in interaction is Availability all the way down
   for anything the project can reach, and the project says so." Both triggers
   can occur (the battery draft has nine kept rows, of which seven are Depth
   rows that wait on state the toy pipelines lack). But the sentence still
   ends by reporting the failure as a conclusion about the world ("Availability
   all the way down ... and the project says so"), which is the shape the
   finding objected to, and it gives no minimum number of surviving rows. The
   finding asked for "withdrawn rather than reported". Not applied.

Three of four hold; the fourth keeps the cannot-lose shape. Partial.

### Tally

Complete: 15 (RT-256, RT-257, RT-258, RT-259, RT-260, RT-261, RT-262, RT-263
with one wording slip, RT-264, RT-265, RT-266, RT-268, RT-270, RT-271,
RT-272). Partial: 3 (RT-267, RT-269, RT-273). Missing: 0.

---

## 3. New claims, contradictions, and the spec paragraph. ARGUED.

### New claims in version 2 that version 1 did not make and no ruling or review covers

1. **"Smallest" as parameter count within one construction family** (section
   2). New definition, offered under the open item for RT-266 in section 10. It
   is registration text and goes to Gate A under decision 1; it has not been
   ruled.
2. **The observer side measuring "how observers' detections distribute over
   frontier models"** before any constructed system exists (section 2, and
   section 10's proposed answer on RT-267: "only as the frontier reference
   profile, labelled as such"). New. Decision 7 as ruled defers the human study
   "until the table, the battery and the construction line have produced
   systems worth showing". Version 2 labels this as proposed, so it is not a
   silent contradiction, but adopting it would depart from decision 7 and needs
   a ruling, which version 2 does not ask for (section 8 says it asks for none).
3. **D's indicators discarded as discriminators** (section 3). Decision 5 as
   ruled promotes D "to the seed of the filtered battery". Version 2, following
   the battery draft's section 0, says D's two rows are reference readings and
   the cost of reversal is the indicator. The battery draft itself puts exactly
   this to John as its open question 1 ("Re-describe decision 5's control, and
   D's place in the battery"). Version 2 states it as applied, not as open.
4. **Entry 2 (the ownership swap) running now by API, about $10** (section
   4.1: "Its first two entries run on experiment D's pipeline by API, under
   about $10 each"; section 6: "under about $20 together"). Decision 5
   authorised the transcript-replacement control only; decision 6 called the
   table and battery "paper work, at $0". Entry 2 is new spend no decision
   covers. The figures themselves match the battery draft (each entry "under
   about ten dollars", ARGUED there).
5. **The four new loss results** of section 5. New wagers, written in answer
   to RT-273; not ruled; they go to Gate A with the battery.
6. **"What two of three said: neither of the author's two readings survives
   as written"** (section 1). Version 1 attributed this to all three. The
   synthesis's bullet does not say "All three" for this one, so the demotion
   may be right, but version 2 does not say why it changed and this session
   did not open the six replies to settle it. Unverified.
7. **"Neither the experiment 06 nor the experiment 08 pipeline carries state
   across encounters"** (section 4.2). Taken from the battery draft's entry 3,
   where it is ARGUED from experiment 08's README. Sourced, but version 2 drops
   the label.
8. **The paragraph added to "What Would Count Against It"** (section 2). New
   spec text; see below.

### Does version 2 contradict the ruling file?

On decisions 3 and 4 as revised: no. Both releases kept, the second
conditional, a pass necessary and not sufficient, the stop condition on the
repair, John's go on the figures, the two kill dates as written, item 23 as its
words say, no new calendar dates, task order with preconditions, a kill date
only at the construction line's first rented run: every clause of the revised
rulings is in version 2 and nothing in version 2 reverses one. The only
differences are of wording ("amendment" in the ruling, "written into the
registration text" in version 2).

On decisions 5 and 7 as ruled: two tensions, items 2 and 3 above. Neither is a
reversal in version 2's own words, but each presents as settled (item 3) or as
an available option (item 2) something the ruling file does not contain and the
battery draft lists as open. The ruling file's closing line, "decisions 1, 2
and 5 to 8 stand as ruled", is the sentence they sit uneasily beside.

### The "What Would Count Against It" paragraph: does it belong upstream?

The spec's current paragraph says that if the depth mechanisms produced systems
passing the five external indicators "without anything resembling self-indexed
binding underneath, that would be evidence that depth and the inside are more
separable than the corpus assumes". Version 2's added paragraph says the floor
is no longer measured, so that sentence "has to be re-read": a battery pass
places a system on the axes at a degree, "it counts against the corpus only if
the corpus predicts that such a profile is impossible without the floor, which
is a prediction the book must state or withdraw upstream."

Two things about it. First, it weakens a loss condition rather than restating
one: under the spec today, a battery pass without binding counts against the
corpus; under the paragraph, it counts against nothing until the book speaks.
The repo's standing rule is that a claim that cannot lose explains nothing, and
the paragraph moves the spec's one loss condition on depth-versus-inside out of
reach until an upstream act. That is a design claim Gate A should weigh, and
version 2 should say in so many words that it is softening this condition, not
re-reading it. Second, the clause "a prediction the book must state or
withdraw upstream" is an instruction to the book. Under this repo's guide
("If the philosophy needs to change, that change happens in those repos, not
here"), the place for that sentence is the proposal packet of decision 8, not
the spec. The spec paragraph can say only what this project will and will not
claim from a battery pass; what the corpus is committed to is the corpus's to
say. So: the first sentence of the paragraph belongs here, labelled as a
softening; the last clause belongs upstream.

---

## 4. The plain-language rule on version 2. MEASURED.

```
$ grep -n '—' docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md; echo "exit $?"
exit 1
$ grep -n '–' docs/rulings/2026-10-07-two-sided-question-PROPOSAL-v2.md; echo "exit $?"
exit 1
```

No em-dash and no en-dash. **Passes that half of the rule.**

Bare identifiers, that is, an id with no phrase beside it saying what it is
(the first mention of each finding carries one, the change log carries one for
every finding, and section 10's open items carry the question as their phrase;
these are the mentions in between):

- `RT-256` at lines 77 and 91; `RT-266` at lines 104 and 178; `RT-262, fatal`
  at line 200 (a severity, not a phrase); `RT-261` at line 213; `RT-264; the
  battery draft's section 0` at line 225 (a source, not a phrase); `RT-259` at
  line 230; `RT-268` at lines 234 and 296; `RT-265` at line 243; `RT-267` at
  line 260; `RT-258` at line 296; `RT-260` at line 315; `RT-272` at line 319.
  Fourteen bare mentions across eleven findings. The workspace rule says every
  id carries its phrase, "inside lists and source appendices too", so a phrase
  on first mention does not cover the later ones.
- `arm M` at line 208: never said what it is (the middle construction of the
  degree experiment, whose ownership answer is set half by one route and half
  by the other).
- `version 4` at lines 208 and 290: never named as version 4 of the successor
  experiment proposal, and its path
  (`docs/successor-experiment-proposal-2026-10-03-v4.md`) is not given anywhere
  in version 2, so the figure's source cannot be opened from the text.
- `Item 23 of the 2026-09-21 ruling` at line 295: carries its phrase ("the
  dates do not move") but the ruling file's path is not given in version 2
  (version 1 gave it in Appendix B).
- `experiment 06` and `experiment 08` at line 248: experiment 08 (the successor
  degree experiment) is named nowhere else in version 2, so a reader has no
  way to know what pipeline is meant.
- `step 5b` at line 201 is fine ("the second release"); `113 lost cells`,
  `chapter 6` and the rest carry their phrases.

Two small factual wordings while on the text: section 4.1 says the battery
draft has "14 rows, 9 kept, 6 discarded". The draft's table has fifteen rows
(numbered 1 to 14 with row 5 split into 5a and 5b) and its own count line says
"9 KEEP, 6 DISCARD", which sums to fifteen; "14 features" or "15 rows" would be
accurate, "14 rows" is not. And section 6's "$220.38" is right (the ledger's
last programme line is "about $229.62 of $450", line 148; $450 less $229.62 is
$220.38), but version 2 cites "the pass" for it and not the ledger, so the
number has no record of its own in the text.

---

## 5. Close

### Must-fix before the pairing check is satisfied

1. **RT-273, the fourth loss condition.** Rewrite so an empty battery
   withdraws the two-sided question rather than reporting "Availability all
   the way down", or give the minimum number of surviving rows the finding
   asked for. Give the observer side's only near-term measurement (detections
   over the frontier reference profile) a loss condition, or say it has none
   and is therefore not a test of anything until section 4.2 delivers. Fix
   "given the battery's readings" so it is clear observers are not told them.
2. **RT-267, the cost of the human study.** Delete "the cost in John's time
   rather than money" or show it; name compensation and the ethics review as
   money; add the three missing needs (instrument reliability, a
   fluency-matched design, a sample size from a pre-stated effect).
3. **Decisions 5 and 7, presented as settled or available when they are
   open.** Say that D's re-description (reference readings, not the seed's
   indicators) is the battery draft's open question 1 for John; say that
   running the observer side against the frontier profile departs from
   decision 7 as ruled and is a question, not an application; say that entry
   2's spend (about $10) is not covered by decision 5 and asks for a go.
4. **RT-263, the baseline arm.** Arm B is given the task, not a summary;
   correct the sentence.
5. **The spec paragraph for "What Would Count Against It".** State that it
   softens the spec's loss condition rather than re-reads it, and move the
   clause instructing the book ("must state or withdraw upstream") to the
   decision 8 packet. Mark the paragraph as new text since the ruling, for
   Gate A.
6. **The plain-language rule.** Give the fourteen bare finding ids their
   phrases; name arm M; name version 4 and give its path; give item 23's file;
   say what experiment 08 is. Change "14 rows" to the draft's actual count.

Should-fix, not blocking: RT-269's quotation of the chapter 5 sentence and a
citation of experiment 1's own record for the +0.033 interval; the dropped
ARGUED label on "neither pipeline carries state"; a sentence saying why
"neither reading survives" moved from all three to two of three; a ledger
citation for $220.38.

### For John, in one paragraph

Version 2 does what it says on the two things you ruled: experiment C keeps
both blocks of spending with the second one conditional on the first, exactly
as you worded it, and the three new calendar dates are gone, with the two old
kill dates left as they were. Every file, branch, commit and checksum it cites
checks out, and its money figures are right. Of the eighteen points the earlier
review raised, fifteen are fully dealt with and three are only partly dealt
with: one loss condition is still written so it cannot really fail, the human
study is still called free when it would cost money, and one borrowed figure
is cited through the author's own note rather than the original record. Two
things are presented as decided that are actually still questions for you:
whether experiment D stays the seed of the new battery or becomes a reference
reading only, and whether the observer study may start early against frontier
models, which your earlier ruling deferred. One new paragraph for the spec
quietly loosens a loss condition and tells the book what to do, which belongs
in the packet to the book, not in the spec. And a number of labels this
workspace requires on every id are missing on second mention. None of this
changes the direction you approved; it is the list of what to tidy before any
of this text becomes registration text.

### What this session did not do

It did not open any chat, did not read the six poll replies, pull request 106
or the book, did not re-run any experiment or poll, called no model, rented
nothing, spent nothing, and edited no file that existed before it began. It
has not ruled on anything; where it found a question for John, it named it and
left it.
