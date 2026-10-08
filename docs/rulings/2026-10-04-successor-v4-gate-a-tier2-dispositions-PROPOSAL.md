# PROPOSAL — draft dispositions for the outside reviews of successor proposal version 4 (ChatGPT A1 to A13, Gemini G1 to G9)

*Dated note, 2026-10-06 (Pacific): ruled. John ruled the drafted text behind pages 7 to 12 on 2026-10-06, one page at a time, in a planning session; his words and what was adopted are recorded in `docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`. The text below is left as written and still reads PROPOSED; that file says what stands.*

*Drafted 2026-10-06 (Pacific) by a Claude Code session in its own worktree,
on branch `gate-a-v4-tier2-dispositions`, cut from `gate-a-v4-dispositions`
(the inside-review dispositions, pull requests 95 and 96) with the two filed
outside reviews merged in. Asked for by the coordination session, so that
John can rule on every finding, inside and outside, in one sitting.
**Nothing here is ruled.** Every disposition is a recommendation, marked
PROPOSED. This session did not edit version 4, either review, the inside
dispositions, the ledger, any ruling file or the protocol. Nothing was
rented or spent: $0.*

*Written under the workspace plain-language rule. MEASURED means a command
was run and its output is in a committed file named beside it; ARGUED means
reasoning a reader can dispute. Documents named once here:*

- *"version 4" is `docs/successor-experiment-proposal-2026-10-03-v4.md`;*
- *"the ChatGPT review" is
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-chatgpt.md`
  (GPT-6 Astra, pull request 100), findings A1 to A13;*
- *"the Gemini review" is
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gemini.md`
  (Gemini 3.1 Pro, pull request 99), findings G1 to G9;*
- *"the inside dispositions" is
  `docs/rulings/2026-10-04-successor-v4-gate-a-dispositions-PROPOSAL.md`, with
  John's six-question packet
  `docs/rulings/2026-10-04-successor-v4-gate-a-questions-PROPOSAL.md`;*
- *"this session's measurements" is
  `docs/2026-10-06-gate-a-v4-tier2-dispositions-measurements.md`, method
  committed first at `da505d4`, output at `025ce90`.*

*The short packet that puts the new questions to John is
`docs/rulings/2026-10-04-successor-v4-gate-a-tier2-questions-PROPOSAL.md`,
pages 7 to 12, an addendum to the six pages already with him.*

**Three things to know before relying on this.**

1. **Who wrote it.** A fresh session. It wrote none of version 4, the
   reviews, the inside dispositions or the toy runs. It did write this
   session's measurements, which A2, A9 and A10 below rest on.
2. **It is owed a check** by a session that did not write it, before John
   relies on a number in it (the pairing rule, `docs/outside-review-protocol.md`).
   That check should rerun
   `python3 experiments/rehearsal-successor-measure/src/tier2_dispositions_check.py`
   and diff it against the committed `check.json`, and confirm Part A's
   commands return what the measurements file says.
3. **Outside findings take ledger numbers only when John adopts them** (the
   protocol's Filing section). The session that records his ruling numbers
   the adopted ones from RT-247 on.

---

## Headline

**One new fatal finding, still open; five new serious ones, of which two go
to whether the experiment is worth running; three new worth-noting ones.
Every new finding is recommended for acceptance, most with a change. None is
recommended for decline.**

- **A2, fatal (the final procedure that withholds readings and assigns
  outcomes has never run end to end): not closed today.** *Corrected
  2026-10-06:* the procedure **does** exist, in the frozen successor code on
  main (`experiments/08-successor-degree`, pull request 97), and it has run
  end to end on the toy, landing on R3 rather than the fifth term. What
  remains: changing it to the rules John is about to rule (pages 5, 7, 8 and
  9, and RT-237), running constructed failure cases through the whole path,
  and another session's check. All $0, after he rules.
- **A9, serious (the no-transplant check can withhold a correctly paired,
  competent model): the review's arithmetic holds and it read the formula
  correctly** (MEASURED). Recommended: stop using that check as a veto; check
  the pairing directly instead.
- **A6 and A13, serious, and the review's kill case, go to whether the
  experiment is worth running.** A6: an idle but readable copy of the
  owner's marker could make a separable model read as fully entangled, and
  nothing outside the instrument certifies the high anchor. A13: the
  registered outcome words claim more than that. Recommended: narrow the
  words now, and run one $0 test (a "decoy" model) before deciding whether
  to register at all.

---

## Where an outside finding repeats an inside one: disposed once

These take the inside disposition already drafted and are not disposed
again. Where the outside review adds something, it is noted.

| Outside finding | Plain words | Same as | Added by the outside review |
|---|---|---|---|
| A1 | The free model's gate requires question sets ("batteries") the task does not have | RT-237 (fatal) | Agrees the gate cannot pass "not applicable": closure needs a ruled removal or a defined, rehearsed check. The inside disposition (page 1) is exactly that |
| A3 | The printed whole-state floor lacks the code's "requirement above zero" condition | RT-238 | Nothing |
| A4 | The ruled fitting sample was not shown to recover the label at the registered width | RT-240 | Agrees the noise stand-in is "a warning, not a forecast"; the inside disposition's new weakness says so |
| A5 | The episode format that keeps the model's own name out of the act is not written down | RT-239 | Nothing |
| A10, its first half | Holes in the outcome map | RT-241 (serious) | Accepts all five inside holes; its two new cases are disposed below as A10 |
| G1 | Episode counts tried only at the toy's width | RT-240 | Nothing |
| G2 | The laptop nomination argued, not timed | RT-245 | Nothing |
| G3 | The grammar's departures from the closed design not written down | RT-239 | Nothing |
| G4 | The floor admits a zero or negative divisor at chance | RT-238 | Nothing |
| G5 | The battery clause cannot be evaluated | RT-237 | Nothing |
| G6 | Holes in the outcome map | RT-241 | Nothing |
| G7 | One candidate's three seeds quoted as three candidates | RT-242 | Nothing |
| G8 | The competing solver's miss given as "0.11 or more" | RT-244 | Nothing |
| G9 | The competing-solver weakness omits the free model's other route | RT-246 | Nothing |

**The Gemini review's second answer**, asked for problems the inside review
did not raise, found none in any of the four parts. Nothing to dispose; it
is recorded as a pass that found nothing new, which the protocol counts as a
valid result. (The inside finding RT-243, that the two forms of the floor do
disagree on the toy, was not restated by either outside review.)

**Three remarks in the ChatGPT review's feasibility table, not lettered,
each covered (the check of these dispositions, pull request 102, section
7):**

- *"The final committed dependency file must actually be named and
  present."* Already covered: one of the ruled wording fixes from the inside
  review (its line 149) names the pinned file; the frozen code pins
  `experiments/08-successor-degree/requirements-measure.txt` (on main). The
  closure check confirms the file named in version 5 exists at the
  registration commit.
- *"Different random seeds alone do not prove that combinations never
  overlap"* (control 5, unseen combinations). Not yet shown: the frozen
  generator's training stream skips an excluded set of fingerprints, which
  may answer it, but neither this session nor the check verified it.
  **Proposed:** one line added to the generator self-test at section 11,
  step 3, asserting that no fresh or relaxed episode's combination occurs in
  the training stream, and its output cited in version 5. Small; no ruling
  needed beyond accepting it.
- *"The registered single-fit-and-reload procedure also differs from the
  toy's historical two-fit provenance."* Already disclosed in version 4,
  section 7.2, item 1, and the frozen code fits once and reloads; nothing
  further.

---

## The new findings, one line each (ledger form)

| Finding | Reviewer | The finding, in plain words | Severity as filed | Proposed ruling | Confidence | What closes it |
|---|---|---|---|---|---|---|
| A2 | ChatGPT | The final procedure that withholds bad readings and assigns the outcome has never been run end to end | fatal | **PROPOSED: ACCEPT.** The frozen procedure (`experiments/08-successor-degree`) already runs end to end on the toy; bring it to the ruled rules, run constructed failure cases through it, check it, before registration | high | The changed code, its method-first constructed-case run, and the check listed under A2, by another session. **Open** |
| A6 | ChatGPT | A readable but unused copy of the owner's marker could be what the read finds, so a separable model reads as entangled; nothing independent shows the high anchor is entangled | serious | **PROPOSED: ACCEPT WITH CHANGE.** Narrow what arm C is said to show; and, on John's go, a $0 decoy test before deciding to register | moderate | The text change; the decoy test's method, output and check if John orders it; otherwise carried open in the registration by name |
| A7 | ChatGPT | Copying the donor's answer gives the same pattern on control 6 as copying who is acting, so control 6 does not tell them apart | serious | **PROPOSED: ACCEPT WITH CHANGE.** Strike the claim that control 6 discriminates; keep its two cells as description; rewrite weakness W11 | high | The text change; a search showing no sentence claims control 6 separates the two |
| A8 | ChatGPT | The toy runs are development evidence, adapted after looking at outputs, not an untouched test of the final rule | worth-noting | **PROPOSED: ACCEPT.** Say so where the toy is quoted as a demonstration | high | The text change |
| A9 | ChatGPT | The no-transplant check withholds correctly paired, competent models whose errors go to other agents' values; and near the bar it barely catches a broken pairing | serious | **PROPOSED: ACCEPT WITH CHANGE.** Report the no-transplant rate against the formula, no longer as a veto; check the pairing directly in the generator's self-test | moderate | The text change; the generator self-test run on the built generator at step 3 |
| A10 | ChatGPT | Two new outcome cases: arm M reads but misses its predicted band; and different seeds can each pass different conditions, so an arm passes with no seed passing everything. Also: the toy is called the fifth outcome though arm F failed its gate | serious | **PROPOSED: ACCEPT WITH CHANGE.** A seed counts only if it passes everything; arm M's miss is reported, not a term change; arm F's gate failure at step 5b (not at step 5a, which stays R3 with stop S4) maps to the fifth term (a change to the inside table, page 5) | moderate; John rules it with page 5 | The text change (including section 3's R3 and R2 rows and the toy sentence; step 5a and stop S4 unchanged), and the A2 run's cases (e), (f) and (g) |
| A11 | ChatGPT | Many legitimate routes to "no verdict" exist; none means the structure is absent | worth-noting | **PROPOSED: ACCEPT.** One registered sentence on what a no verdict means | high | The text change |
| A12 | ChatGPT | The registered uncertainty is for the raw difference, not for the reading or the separation | worth-noting | **PROPOSED: ACCEPT WITH CHANGE.** Label the reading and the separation as descriptive, with no registered uncertainty | high | The text change |
| A13 | ChatGPT | The outcome words ("metric validated", "known high anchor") read as more than the experiment shows | serious | **PROPOSED: ACCEPT WITH CHANGE.** Keep John's terms, and require a fixed scope phrase beside every use; register the review's "defensible scope" table | moderate; low on whether to rename the terms instead | The text change; a search showing every "metric validated" in sections 0 to 16 carries the scope phrase |

---

## Each new finding: the check of its counterexample, the proposed text, and the reason

Section and line numbers are version 4's. Square brackets mark what the
writer of version 5 fills in.

### A2 (fatal): the final decision procedure has never run end to end

**Corrected 2026-10-06.** The first version of this section said the
procedure "does not exist as code". **That was wrong.** This session searched
only its own branch, which was cut before pull request 97 merged the frozen
successor code into main (`53ae82c`, 2026-10-05). On main,
`experiments/08-successor-degree/src/measure.py` and `procedure.py` hold the
procedure, frozen 2026-10-04 and reported in
`docs/2026-10-04-successor-code-freeze.md` (on main). The corrected account
follows; the correction is also recorded, dated, in this session's
measurements file.

**What the frozen code does (read from origin/main, ARGUED from the code,
with its self-test re-run, MEASURED: `measure.py --self-test`, "all checks
passed").**

- **Per-seed withholding: yes.** `measure.withhold` replaces the reading
  with "no verdict" and lists its reasons, in the output file and the
  table (not always every reason: see "what it does not do", item 6): the arm's gate failed; no site set or read failed its floor at
  nomination; described-only; the whole-state floor missed on fresh or on
  development episodes; the no-transplant rate outside 0.018; control 7
  failed; control 1 failed on arm T; control 4 failed. A control that could
  not be evaluated counts as failed. The withheld figure is kept in a
  separate field (`arithmetic_withheld`).
- **Seed aggregation: partly joint, partly separate.** In
  `procedure.gate`, a seed passes the learning gate only if it clears
  own-directed **and**, on arm F, named-other on that same seed
  (`seed_passes`), and the arm passes if two seeds do: joint for those two
  conditions. The channel-removal collapse on arm F is counted across seeds
  **separately** (`lesion_ok`, two of three on its own). And the gate is
  then applied **at arm level** to every seed (`withhold` receives the
  arm's `gate_ok`), so a seed that itself failed the gate still counts
  toward "two of three read" if the arm passed. Readings: `arm_outcome`
  reads an arm if two or more seeds survive `withhold`.
- **Outcome term: yes, one of the four version 4 terms.** `measure.outcome`
  returns R3 if arm T, C or F failed its gate; otherwise R2 if T and C do
  not separate; R1 if F reads; otherwise the fifth term with F's reasons.
  Arm M's band and true-slot check is computed (`arm_M_check`,
  `prediction_met`) and printed but never changes the term or the
  sentence.
- **It has run end to end on the toy** (freeze test T3a, on the committed
  reads: `out-freeze-tests/t3a-committed-reads/summary.json` and
  `table.md`, on main): every arm T, C and M seed reads; every arm F seed
  is withheld with three reasons; **the outcome is R3, "substrate not a
  testbed"**, because arm F fails its gate. The freeze report found and
  reported this (its section 4.1): version 4 section 3 says the toy reaches
  the fifth term. That is A10's precedence point, already found by the
  freeze. It also ran end to end on untrained 10-million and 30-million
  parameter models (test T6), each landing on R3.

**What it does not do, measured against the review and the pending
rulings.**

1. **No constructed failure cases through the whole path.** The self-test
   drives `withhold`, `arm_outcome` and `outcome` separately with made-up
   inputs and reaches R1, R2, R3, the fifth term, the fallback and "arm M
   dropped". It does not run `summarise` on constructed row files, so it
   never exercises: the arm-level gate meeting per-seed readings; split
   seeds as in A10's table; overlapping failures on one seed; arm M reading
   outside its band; arm T returning no verdict.
2. **Two mappings that the inside dispositions (RT-241) call holes are
   coded as version 4 wrote them:** arm T no verdict with arm C reading
   gives R2 (nothing was compared, so R2 is wrong; RT-241 proposes "metric
   not validated"); and the two-model fallback returns the R1 term with a
   note, not a registered fallback term.
3. **The battery replacement (RT-237) is absent**: no ownership-free line.
4. **The no-transplant check is a veto** (A9 proposes it is not).
5. **No independent check of the freeze's outcome logic against the
   registration text** has been filed that this session found; the freeze
   report is its author's.
6. **It does not always list every reason, and it keeps the withheld
   figure in its output file** (found by the check of these dispositions,
   pull request 102, section 2). `withhold` checks the controls only when a
   reading was computed, so a seed already withheld at nomination never
   shows a failed control; and `summarise` adds arm F's channel-removal
   reason only to a seed that would otherwise read. And `summarise` writes
   each withheld seed's figure into `summary.json` as `arithmetic_withheld`
   (on the toy, 1.0, 1.0 and 1.0108 for arm F), which version 4 section
   6.4, item 5, and the R-13 text below forbid. The table is clean.

**Status: still not closed at $0 today, for a different reason.** The
procedure exists and has run end to end on the toy, which is most of what
A2 asks. What remains: (i) the rules it encodes are about to change,
because five pending rulings change it (RT-237's line, RT-241's table, A9,
A10, and page 9's precedence); a closure measurement on today's code would
certify rules John is about to replace; (ii) the constructed cases have
not been run through the whole path; (iii) another session's check. All
three are $0 and can follow straight after John rules.

**What must be added to `procedure.py` and `measure.py` (draft, replacing
the earlier "what must be built").**

1. **The ruled outcome table** in `measure.outcome`: R3 for arm T or C
   failing its gate (or T, C or F, if John keeps page 5's draft); "metric
   not validated" for arm T no verdict; the two fallback terms in place of
   R1 or the fifth term with a note; arm M's missed prediction stated in the outcome's
   sentence (page 9).
2. **The seed rule John picks on page 7**, in one place: if joint, the
   per-seed gate (every condition, the channel-removal collapse and the
   ownership-free line included) is passed into `withhold` per seed, not
   the arm's `gate_ok`; `lesion_ok` stops being a separate count.
3. **The ownership-free line** (RT-237) as a field of `procedure.gate` and
   a condition of the arm F gate.
4. **The no-transplant check** moved from `withhold`'s reasons to the
   reported fields, if page 8 is ruled as recommended.
5. **A constructed-case run through `summarise`**: a small script that
   writes row files for the toy plus the cases (a) to (j) of this
   session's method note (each a copy of the T3a rows with named fields
   changed), runs `procedure.summarise` on each directory, and compares
   each term with the one written beside it before it ran. Method first;
   by a session other than this one; $0.
7. **Every reason listed, and nothing withheld left in the output.**
   `withhold` evaluates every check whether or not a reading was computed,
   and lists every failure; arm F's channel-removal failure is listed on
   every seed it applies to (item 2 does this if John picks the joint
   rule); and `arithmetic_withheld` is removed from `summary.json`. (The
   alternative, for John: keep it, as a record of what was not reported,
   and reword R-13 and the closure check's step 2 to say the figure may
   appear only under that one named field and never as a reading. This
   file recommends removing it: a figure in the output file is one a later
   session will quote.)
6. **The freeze's own self-test updated** so that "the toy lands on the
   fifth term" is tested with the toy's real gate (arm F failing), not with
   every gate passed.

**Text change, section 10 (the rehearsal) and section 11, before step 1, one
item added:**

> **R-13. The final decision procedure, run end to end before registration
> (the ChatGPT outside review of version 4, A2, ruled [date]).** The module
> that turns per-seed records into one registered term
> (`experiments/08-successor-degree/src/measure.py` and `procedure.py`,
> `summarise`, at [commit]) was
> run on the toy's committed records, giving [term], and on [n] constructed
> cases, each landing on the term written beside it before it ran, among
> them R1, R2, the fifth term, both fallback terms, "metric not validated"
> and R3; no withheld reading appears in its output file or its table
> (MEASURED: [findings file] at [commit]; checked at [commit]). The
> registered runs use this code unchanged.

and in section 6.4, item 5, replace "A requirement on the registered code:
it withholds the reading itself." with "**It withholds the reading itself;
the procedure that does so was rehearsed end to end before registration
(section 10, R-13).**"

**The check owed afterwards, by a session that wrote neither the module
nor its run** (the closure rule gives a fatal finding's check to the tier 1
reviewer of this Gate A). It must:

1. **Recompute every outcome independently.** Without importing `measure.py` or `procedure.py`,
   write the rules from the registration text and compute the term for the
   toy records and every constructed case. Every term must equal the
   module's. This comes out wrong if the module disagrees with the text.
2. **Confirm withholding in both outputs.** For each withheld seed, search
   the module's output file and its table for that seed's reading (its
   value printed to four places, and the field): it must appear in neither.
3. **Break each rule and see a case notice.** Turn off each veto (control
   7, control 1 on arm T, control 4, the fresh floor, the piece floor, the
   gate, the seed rule) one at a time and rerun the cases: at least one
   case's term must change for each. A rule whose removal changes no case is
   untested, and the finding stays open.
4. **Cover every term.** Each registered term, the new ones included, is
   reached by at least one case, and no output contains a term that is not
   registered.
5. **Confirm the inputs** were the committed toy records, by their SHA-256.
6. **File** the commands, outputs and a plain sentence per point.

**Reason.** The protocol requires the whole measurement to run once end to
end before Gate A, and this part never has. Every past registration failure
on this programme's list was a step nobody had run; a veto printed beside a
reading instead of replacing it is exactly the kind of gap that survives
until the result is read. It costs nothing but laptop time. **Alternative,
not recommended:** carry it open and build the module at step 3 of section
11. That is after registration, so the registered rules would be first run
on real results, which is what the rehearsal exists to prevent; and a fatal
finding cannot be carried open under the closure rule.

### A6 (serious): a readable but unused marker could make a separable model read as entangled

**Is the counterexample right? Yes, as an argument (ARGUED).** The read is
fitted to recover which marker word is the model's own; the piece floor
checks only that the label is recoverable from the chosen directions at the
action position; the reading is 1 when transplanting those directions does
nothing. A model carrying an idle, easily read copy of its marker plus a
separate ownership variable the action uses would: pass the gate; have the
idle copy nominated if it is the easiest to read; clear 144 of 180; show no
movement from the ownership-only transplant; and show full movement from
the whole-state transplant, which carries both. The reading would be near 1
on a separable model. Version 4's W12 admits that "the act's ownership
answer is carried by directions the read did not find" is not excluded. What
the review adds, and this session agrees with, is the consequence for arm C:
arm C's "high" status rests on its construction (ownership multiplied into
every layer) and on this instrument failing to find a piece that moves the
action (section 3, "That is what 'entangled at these sites' means"; W3).
Nothing independent of the instrument shows arm C's ownership answer cannot
be separated. Arm T, by contrast, has an independent reference: its true
slot, handed to the procedure, reads 0.0000. Whether the read would actually
pick an idle copy over a used one is untested.

**Text change 1, section 3, after "That is what 'entangled at these sites'
means.":**

> That is a statement about this instrument at these sites, not an
> independent certificate of arm C's degree: arm C's high status rests on
> its construction and on the instrument finding no piece that moves the
> action. A model with a readable but unused copy of its marker and a
> separate ownership variable the action uses would read the same way (the
> ChatGPT outside review of version 4, A6; weakness W12).

**Text change 2, W12, a sentence added at its end:**

> The same limit applies to the high anchor: arm C's reading near 1 is
> what this instrument returns on it, and no measurement independent of the
> instrument shows arm C's ownership answer cannot be separated. [If the
> decoy test runs: "The decoy test (section 10, R-14) [did / did not] read
> a separable model with an idle marker copy as entangled: [figures]."]

**The optional $0 test, on John's go (page 10).** A decoy model: arm T's
committed toy models, with extra coordinates appended to the state at
every layer that carry an exact, unused copy of the owner's marker (nothing
downstream reads them), as the width stand-in of RT-240 appended noise.
The registered nomination and reading then run on it unchanged. **If the
reading is near 0**, the read finds the used slot even with a cleaner decoy
beside it, and A6's counterexample does not bite in this form. **If the
reading is near 1**, the instrument calls a separable model entangled, and
the high anchor means much less than its name. Method first; $0; a few
hours on the laptop; a session other than this one; checked. It is a
constructed stand-in, not a trained model, and would be said to be one.
**Ties, stated in advance** (the check of these dispositions, pull request
102): arm T's true slot is already read perfectly, and an exact copy of the
marker would be too, so which one the read and the nomination favour may be
decided by tie-breaking (the fit's weighting between two perfect features,
then the rule's order: highest ownership-only share, smaller size, earlier
position set), not by which is "easier to read". **So the test runs both
ways round, fixed in its method before it runs:** once with the copy at
larger scale than the slot (so a fit that weights by scale favours the
copy) and once at smaller scale, at the same layers and positions as the
slot so the rule's order cannot exclude it; both readings are reported.
The counterexample bites if, in either run, the transplanted piece lies
mostly in the copy and the reading is near 1.

**Reason.** The finding goes to what a high reading means, which is half
of what the experiment validates. The wording change is cheap and true
either way. The decoy test is the one affordable measurement that could
show the counterexample is real or not before money is spent.
**Alternative:** carry it as a named weakness only, no test. Valid, and
cheaper in time; its cost is registering without knowing whether the
instrument can be fooled this simply.

### A7 (serious): control 6 cannot tell "who is acting" from "the answer" apart

**Is the counterexample right? Yes (ARGUED, checked against the code).**
Control 6 measures whether the whole-state transplant changes the model's
prediction (`rerun_controls.py`, line 204: moved = transplanted prediction
differs from the untouched one). In a same-value pair the donor's identity
and the recipient's dictate the same answer. Copying who is acting changes
nothing; copying the donor's prepared answer also changes nothing, because
it is the same answer. In a different-value pair both change the
prediction. So both mechanisms give the pattern version 4 attributes to
"moved who is acting", and version 4's sentence "a transplant that has
smuggled a value across changes the action in both" is wrong for the
donor's own answer. The review is also right that a moved same-value cell
does not by itself show non-identity content was carried: a model that errs
differently as different owners can move it. And section 6.1's argument
(the donor's value is already in the recipient's context, so nothing is
imported) does not stop a transplant at the action position from carrying
a selected value.

**Text change 1, section 6.1, replace the last two sentences** ("So a
successful transplant does not import ... warned about.") with:

> So the donor's answer is not new to the recipient. That does not show a
> successful transplant moved who is acting rather than carrying the
> donor's chosen value: a transplant at the action position can carry
> either, and nothing in this design separates the two (the ChatGPT outside
> review of version 4, A7).

**Text change 2, section 7.3, item 6: retitle "Same and different value
cells. Reported, on the relaxed set." and replace "The discriminating
control." and the sentences "A transplant that has moved who is acting
changes the action in the second group and not the first; a transplant
that has smuggled a value across changes the action in both." with:**

> A description, not a discriminator. Copying who is acting and copying
> the donor's prepared answer predict the same pattern: nothing moves in
> the same-value cell, everything in the different-value cell. A moved
> same-value cell shows the whole-state transplant changes the action where
> neither would, which can be other content carried across or an imperfect
> model erring differently for the two owners; it does not say which (the
> ChatGPT outside review of version 4, A7).

**Text change 2b, the same item 6, its later sentence** "an entangled arm
is expected to move the same-value cell too, and that is reported as the
caveat it is (weakness W11): on those arms the whole-state transplant
carries something besides identity" — replace from "on those arms" with:
"on those arms the whole-state transplant moves the action where neither
copying who is acting nor copying the answer would, which may be other
content carried across or the model erring differently by owner; the cell
does not say which."

**Text change 3, W11, retitle it "W11. On the entangled arms, the
same-value cell of control 6 moves, and control 6 cannot say why." and
replace its body with:**

> On the relaxed set the same-value cell moved on arm C in 0.51 to 0.63 of
> trials and on arm M in 0.22 to 0.32 (section 7.3, item 6). Neither
> copying who is acting nor copying the donor's answer would move it, so
> the whole-state transplant changes something else on those arms, or the
> models err differently by owner. Control 6 cannot separate copying who is
> acting from copying the answer, so no reading here is claimed as purely a
> statement about where the ownership answer lives.

**Reason.** The counterexample is exact and needs no measurement. Keeping
the cells as description costs nothing. **Not recommended now:** the
review's stronger design (recipients whose content forces an answer
different from the donor's prepared one) would need its own generator and
rehearsal; carry it as an extension.

### A8 (worth-noting): the toy is development evidence

**Text change, section 10, its opening, and W5, one sentence:**

> The toy runs are development and rehearsal evidence. Controls, gates and
> site exclusions were changed after toy outputs were seen, and some fresh
> episodes were reused to assess changed rules; committing a method before
> re-running already-inspected models does not make them untouched. No toy
> figure is an independent test of the frozen procedure; the registered
> runs, on unused episodes, are the first (the ChatGPT outside review of
> version 4, A8).

**Reason.** True, disclosed piecemeal already, and worth one plain sentence.

### A9 (serious): the no-transplant check withholds competent models

**Is the counterexample right, and did the reviewer read the formula
correctly? Yes to both (MEASURED, this session's measurements, Part B).**
Version 4 section 6.4, item 3, expects the untouched rate near `(1 − p) / 7`
"because an untransplanted model lands on the donor's answer only by erring
onto exactly that one of the seven other slots": that is an even spread of
errors over the seven wrong values. The committed formula values recompute
exactly from `p` on all twelve toy records. In the review's case (errors
only on the other three agents' values) the rate is `(1 − p) / 3`: at
`p = 0.8`, 0.0667 against 0.0286, a gap of 0.0381 over the 0.018 allowance.
The gap is over the allowance at every accuracy below 0.9055. By the exact
binomial on 800 pairs, the rule withholds such a model 0.9904 of the time at
`p = 0.8` and 1.0000 at `p = 0.56`. On the toy, every model errs roughly
evenly (0.097 to 0.155 of its errors on the donor's answer, near 1/7), which
is why it passed; nothing makes a registered-size model do the same, and a
model that has half-learned ownership is exactly one that errs onto other
owners. **The reviewer's second point holds too:** at the learn-both bar the
rule catches a fully broken pairing only 0.5589 of the time.

**The reading does not need the check.** The chance-corrected form uses the
measured untouched rate (section 6.3); the formula's only job is to catch a
broken pairing, and a broken pairing is a code fault that can be tested
directly.

**Text change, section 6.4, item 3: replace from "A measured no-transplant
rate more than 0.018 from the formula's value means the pairing is suspect,
and nothing is read for that arm." to the end of the item with:**

> **The no-transplant rate is reported against the formula, not used to
> withhold a reading (the ChatGPT outside review of version 4, A9, ruled
> [date], amending the Gate C rulings, RT-222).** The formula is right only
> if the model's errors spread evenly over the seven wrong values. A
> correctly paired model whose errors go to the other three agents' values
> lands at `(1 − p) / 3`, outside the allowance at any accuracy below about
> 0.9; on 800 pairs a rule of 0.018 would withhold such a model at `p = 0.8`
> 0.99 of the time, and would catch a broken pairing at the learn-both bar
> only 0.56 of the time (MEASURED:
> `docs/2026-10-06-gate-a-v4-tier2-dispositions-measurements.md`, Part B).
> On the toy every model erred roughly evenly. **The pairing is checked
> directly instead:** the registered generator's self-test asserts, on every
> matched pair, that the donor's dictated answer is computed from the
> donor's own identity and value on the named item, and differs from the
> recipient's except in the relaxed set's same-value trials; and **control
> 4**, which already withholds a reading, transplants the donor's states
> from before either twin's own turn and requires the output to be
> bit-identical, which a mismatched pair would break. (Control 7, the null
> transplant, checks the transplant code, not the pairing.) **Version 4's
> detection-margin sentence is replaced, not dropped silently:** "the
> detection margin at the bar is printed in the reporting table ... 0.0198,
> a margin of only 0.0018 over the allowance; at 0.56 ... 0.0441" becomes
> "the chance the formula would flag a broken pairing on 800 pairs is
> printed beside the rate: 0.56 at the learn-both bar (the ChatGPT outside
> review, A9: the 0.0018 margin was not a demonstration of detection)". The
> rate, the formula's value, their difference and the share of
> errors landing on the donor's answer are printed in the reporting table.

and in section 6.4, item 5, delete "a no-transplant miss outside its
allowance," from the list of things that withhold a reading; and in section
9, the row "The no-transplant allowance", replace its middle column with
"**reported, not a veto**: the rate beside `(1 − p) / 7`, their difference,
and the share of errors on the donor's answer; the pairing checked by the
generator's self-test".

**Reason.** As written, the check selects models by how they err, and the
errors most likely in a model learning ownership are the ones it rejects,
while it catches what it is for about as often as a coin. A direct test of
the pairing is stronger and cannot reject a good model. **Strongest
alternative:** keep the veto as an explicit restriction on which models the
instrument accepts, with the counterexample written beside it, as the
review allows; its cost is a new and likely route to "no verdict" on the
free model.

### A10 (serious): split seeds, arm M's missed band, and which outcome wins

Extends RT-241; the inside table (page 5 of the packet) is assumed.

**Is the counterexample right? Yes (ARGUED, and MEASURED that the code does
what the review describes).** The rehearsal's `repairs.py` (lines 157 to
160) counts each gate condition across seeds separately. *Corrected
2026-10-06:* the frozen successor code on main is partly joint:
`procedure.gate` requires own-directed and (on arm F) named-other on the
same seed, but counts the channel-removal collapse separately, and applies
the arm's gate to every seed, so a seed that failed the gate can still be
one of the two that read (see A2). **Run through the frozen code, the
review's own table fails arm F's gate** (only seed 1 passes both learning
conditions), and over all 512 pass-or-fail patterns of arm F's three
conditions on three seeds the frozen code never passes an arm where no
seed passes everything; separate majorities do so on 6 patterns. The
frozen code's remaining gap is the **18 patterns where exactly one seed
passes everything** and the arm still passes (MEASURED by the check of
these dispositions, pull request 102, section 4.2). The toy has no such split: under either rule every toy
gate verdict is the same (this session's measurements, Part C). The
precedence conflict is real too: version 4 section 3 calls the toy the fifth
term although arm F fails its gate (named-other on seeds 1 and 2), while R3
says an arm failing its gate gives R3; and the inside table's rule 1, as
drafted, would make the toy R3. The frozen code already does: its
end-to-end toy run lands on R3, which the freeze report found and reported
(`docs/2026-10-04-successor-code-freeze.md` on main, section 4.1).

**Proposed rules (each John's; page 7 and page 9).**

1. **A seed counts only if it passes everything.** An arm passes its gate
   if two or more seeds each pass every gate condition that arm is gated on;
   an arm reads if two or more seeds each pass the gate and every
   withholding check and return a reading. No toy verdict changes
   (MEASURED, Part C).
2. **Arm M reading outside its prediction** changes no term. The report
   says, in the sentence carrying the term, "arm M missed its predicted
   reading" with the figures, and arm F's figure is then placed against
   arms T and C only. The prediction holds if every seed of arm M that reads
   is inside 0.3 to 0.7 and within 0.10 of its true-slot reading.
3. **Arm F failing its gate: narrowed to step 5b** (revised after the check
   of these dispositions, pull request 102, defect 1). Under ruled text,
   arm F's first registered run is trained alone at step 5a, and if it and
   its one re-run fail the learn-both gate, "the outcome is R3 and nothing
   else launches" (version 4, section 11, step 5a, and stop S4). That is
   the design's most likely failure, and this proposal **does not change
   it**: S4 is a ruled stop that keeps the loss to the first release. The
   case this rule covers is narrower: arm F passes at step 5a, then its
   other seeds, trained at step 5b alongside arms T and C, fail the gate so
   that the arm fails it. Then arm F is a "no verdict" with the reason
   "failed its gate on learning", mapping to the fifth term when arms T and
   C separate (or R2 when they do not). R3 is for arm T or arm C failing
   its gate, or arm F failing at step 5a; arm M failing is dropped (as the
   inside table already says).
   **The frozen code returns R3 for any arm F gate failure, by design**,
   following step 5a and S4 (the freeze report,
   `docs/2026-10-04-successor-code-freeze.md` on main, section 4.1), and
   **the toy is "substrate not a testbed" in that code today**. Under this
   rule the toy's pattern (arm F passes both conditions on seed 0, fails
   named-other on seeds 1 and 2) would be the fifth term if seed 0 is taken
   as the step 5a run, and R3 if seed 1 or 2 is; version 5's toy sentence
   in section 3 says exactly that instead of "the toy reaches the fifth
   term".

**Text change 1, section 3, the paragraph "When an arm's three seeds
disagree", replace "an arm is read if at least two of its three seeds
return a reading" with:**

> a seed counts only if it passes every condition of its arm's gate and
> every check that withholds a reading, and returns a reading; an arm passes
> its gate if two or more seeds each pass every gate condition, and is read
> if two or more seeds count (the ChatGPT outside review of version 4, A10,
> ruled [date]); separate two-of-three counts per condition are not used.

and in section 9, the rows "Gate on learning (R3)", "Ownership-lesion
collapse threshold" and "An arm whose three seeds disagree", replace "on at
least two seeds of three" with "on at least two seeds of three, **the same
seeds passing every condition**".

**Text change 2, the inside table (RT-241), rule 1:** replace "If arm T, C
or F fails its gate" with "If arm T or arm C fails its gate, or arm F fails
its gate at step 5a after its re-run (section 11, stop S4)", and add to the
table's arm F column, in the two rows that read "no verdict, or fails the
channel-removal check", "or, having passed at step 5a, fails its gate on
learning at step 5b". **Four other places then change to match:**

- **Section 3, the R3 row**, "One or more arms fail its gate after the one
  permitted re-run" becomes "Arm T or arm C fails its gate after the one
  permitted re-run, or arm F fails it at step 5a after its re-run".
- **Section 3, the R2 row**, "Every arm carried passes its gate (... both
  conditions on arm F)" becomes "Arms T and C pass their gates and do not
  separate at the bar; arm F is not read, whether or not it passed its gate
  at step 5b".
- **The inside dispositions' text change 2 to section 8.1**, "R3 for the
  experiment (arm M excepted: it is dropped)" becomes "R3 for the
  experiment (arm M excepted: it is dropped; arm F excepted after step 5a:
  section 3, rule 1)".
- **Section 3's toy sentence**, as rule 3 above says. Step 5a and stop S4
  are **not** changed.

**Text change 3, the inside table, below "Arm M never changes the term",
add:** "If arm M reads and misses its prediction (section 9), the report
says so in the sentence that carries the term, with the figures, and arm
F's figure is placed against arms T and C only."

**Reason.** Separate majorities let an arm through on models none of which
met all the conditions the claim rests on; the joint rule costs nothing on
the toy. For arm F, R3's meaning ("this recipe and size are not a place to
study mechanism") is wrong once the two built anchors have learned and
separated: the free model's failure to learn is then a fact about the free
model, which is what the fifth term with its reason says. At step 5a the
anchors have not been trained yet, so nothing has been validated and R3
with the stop is right; that is why step 5a and S4 stay. The rehearsal code
treats a gate failure as a reason for no verdict; **the frozen registered
code does the opposite, R3, deliberately**, so adopting this rule means
changing `measure.outcome` (A2, item 1). **Alternatives:** (a) R3 for any
gate failure of T, C or F, as page 5 drafted and the frozen code does:
simplest, no change to code, and the toy is R3. (b) Extend the fifth term
to a step 5a failure too, rewriting step 5a and S4: not recommended, since
S4's stop exists to avoid spending the second release on a free model that
did not learn. **John should rule page 5 and page 9 together.**

### A11 (worth-noting): no verdict is not absence

**Text change, section 3, after "What a no verdict maps to", one paragraph:**

> **What a no verdict does not mean (the ChatGPT outside review of version
> 4, A11).** It means this registered procedure did not return a reading,
> for the stated reason. It does not show that the arm has no ownership
> representation, that its representation cannot be separated, or that
> another instrument could not read it. The registered search has limits
> that can produce it on a model with a recoverable representation: the
> nomination order, the rank cap of 8, the fitting sample, the fresh-episode
> floor, the gates and the seed rule.

### A12 (worth-noting): the uncertainty belongs to the raw difference only

**Text change, section 9, the row "Uncertainty across seeds", add:**

> This is the spread of the raw difference, not of the reading
> `(W − S)/(W − U)`, whose denominator moves too, and not of the separation
> between arms T and C, which is a decision rule on point figures. Neither
> the reading nor the separation has a registered uncertainty; both are
> reported as descriptions. The sampling band printed beside a piece's count
> does not account for that piece having been chosen on the same held-out
> episodes (the ChatGPT outside review of version 4, A12).

**Reason.** True and cheap. Adding an uncertainty for the ratio (for
example, a bootstrap over pairs) would need its own rehearsal; carried as
an extension.

### A13 (serious): the outcome words claim more than the experiment shows

**Text change 1, section 3, under the outcome table, a rule added:**

> **Scope, fixed with the terms (the ChatGPT outside review of version 4,
> A13, ruled [date]).** Wherever "metric validated" appears, in this text,
> STATUS.md, the paper or in public, it is followed in the same sentence by
> "**on these constructed systems, for this intervention procedure**".
> "Degree read" is followed by "**as a ratio of two transplants at the sites
> this procedure chose**". No result here establishes a scale of
> integration, consciousness, selfhood or general agency.

**Text change 2, section 13, the review's table registered as written, as
"How results may be summarised":** the seven rows from "The metric measures
degree of integration" to "Seven controls validated the mechanism", each
with its defensible scope, with "control 6" added to the last row's
description-only controls (A7).

**Reason.** The weaknesses are already honest but sit far from the
headline; a fixed phrase travels with the term. **The choice that is
John's:** rename the terms (for example, "metric separates the built
anchors") instead. Renaming is the cleaner fix, but the terms were ruled in
his words on 2026-10-03, and changing them reopens that ruling.

---

## The kill case, and what this file proposes about it

The ChatGPT review ends: the full spend could separate T from C, place M in
the middle, and still show only that the probe finds arm T's deliberately
exposed slot and misses the representation that matters elsewhere; "if
that limited result is not worth the cost on its own, the registration
should stop here." This is John's question (page 11). This file's view
(ARGUED): A7, A9 and A13 can be fixed in text, and A2 at $0 once John has
ruled the rules it encodes. A6 cannot be
fixed in text, and it decides how limited the limited result is. The $0
decoy test answers the sharpest version of it before any money moves.

## Tally

New findings: 9 (one fatal, five serious, three worth-noting). Proposed:
accept 3 (A2, with its text items, A8, A11); accept with change 6 (A6, A7,
A9, A10, A12, A13); decline 0; carry open 0, unless John declines the
decoy test, when A6 is carried open by name. Repeats of inside findings: 4
from ChatGPT, 9 from Gemini, disposed once with RT-237 to RT-246. Four of
the proposals change something John ruled: A9 (the Gate C rulings, RT-222),
A10 (the two-of-three rule of 2026-10-03, ruling 6, and the inside table's
rule 1), A13 (the outcome terms' use) and A6 (only if the decoy test runs).

## What this session did not do

It did not rule, edit version 4 or any ruling, write version 5, build
the decoy, or change the frozen successor code. It did not check its own work.
**Its first version wrongly said the decision procedure did not exist as code,
having searched only its own branch; corrected 2026-10-06 under A2.**
