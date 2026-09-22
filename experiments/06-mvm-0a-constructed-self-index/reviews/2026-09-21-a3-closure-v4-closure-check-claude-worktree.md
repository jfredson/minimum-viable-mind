# Gate A closure check — the Amendment A3 closure text, version 4

*Filed 2026-09-21 (Pacific) by a Claude Code session in its own worktree
(`worktree-agent-aaccf55dd43fe5aab`), reading at commit `8ebf9f3` on the
main line. This is the reviewer-owned verification the closure rule of
`docs/outside-review-protocol.md` requires: a measured check, by a session
other than the one that wrote the fix, on each of the six fatal findings
the Gate A tier 1 review raised against this text. This session did not
write any part of version 3 or version 4 and did not write the findings it
is checking. Filed verbatim and not edited after filing.*

*What this session did not do: it did not edit the closure text, the
findings ledger, or any registered file; it ran no compute and spent no
money; it pushed nothing and merged nothing.*

*Lookup: none. No web search. Every check below is run against files
committed in this repository.*

*How to read the two words in the verdicts. **Checked** means a command was
run against the committed record and its output is printed here.
**Accepted** means no decisive command exists and the judgement rests on
reading two committed texts against each other, which is stated where it
happens. A disposition in the ledger ("accepted as drafted", "done in
version 3") is neither, and was treated throughout as a claim to test.*

---

## Verdict in one table

| finding, in plain words | where the fix lands | verdict |
|---|---|---|
| `RT-143`, nine measured scores stated with no file named | version 3, commit `8229674` | **CLOSED** (checked) |
| `RT-144`, the "causal patching was never run" claim with no record named | version 3, commit `8229674` | **CLOSED** (checked) |
| `RT-145`, a citation to a ruling file that was in no commit | ruling committed at `acd8305`; sentence written in version 4, commit `b5aabab` | **NOT CLOSED** (checked) — the file is committed, but the sentence names the wrong item inside it |
| `RT-153`, "center" used in two incompatible senses | version 3, commit `8229674` | **CLOSED** (checked) |
| `RT-155`, the registered other-agent control described as having run | version 3, commit `8229674` | **CLOSED** (checked) |
| `RT-161`, the registered instrument-failure reading dropped | version 3, commit `8229674` | **CLOSED** (checked) |
| `RT-165` (serious), the deferred marker-word read | version 3, commit `8229674` | **CARRIED**, and the carry is thinner than the rule asks |

Four further problems that nobody has raised are in the last section. One
of them, the missing record behind "the validity gates were clean", is the
same kind of gap as `RT-143` and `RT-144` and was not caught by the tier 1
pass.

---

## `RT-143` — the nine measured scores now name their file

**What the closure claims.** The paragraph headed "What A3 measured" gains
the citation `seeds-endpoint-findings.md`, and that file contains all nine
figures: three intact scores, three lesioned scores, the state battery's
movement on one seed, its locked threshold, and the syntax battery's
non-movement.

**Check run.**

    grep -n -E "0\.5683|0\.5633|0\.5738|0\.1988|0\.2015|0\.1447|0\.0769|0\.1172" \
      experiments/06-mvm-0a-constructed-self-index/seeds-endpoint-findings.md

**Output.**

    25:| pilot (seed 0) | 0.5683 (sd 0.0076) | 0.1988 (sd 0.0173) | 1.337 (sd 0.057) | 7.5x |
    26:| seed 1 | 0.5633 (sd 0.0316) | 0.2015 (sd 0.0215) | 1.342 (sd 0.103) | 7.6x |
    27:| seed 2 | 0.5738 (sd 0.0284) | 0.1447 (sd 0.0127) | 1.528 (sd 0.068) | 8.6x |
    44:| seed 2 | **+0.0769** | 0.0000 |
    47:battery is untouched on two and moves 0.0769 on seed 2, which is forty
    51:0.1172 and 0.0769 is well inside it -- but it is reported rather than

**Second check, for the two claims in that paragraph that are not single
numbers.**

    grep -n -i "paired\|syntax battery does not move\|six evaluation seeds" \
      experiments/06-mvm-0a-constructed-self-index/seeds-endpoint-findings.md

**Output.**

    20:Across six independent evaluation seeds at n=800, reported as a spread
    46:The syntax battery does not move at all on any checkpoint. The
    137:- Every figure is a mean across six evaluation seeds with its spread, not
    138:  a single draw. Intact and lesioned are paired within each seed, so the

**Does the output match the claim?** Yes, for every figure and both
supporting claims. Each intact score sits in the same table row as its own
lesioned score, so the pairing the sentence asserts is visible in the
record and not only asserted in it. The state battery's 0.0769 on seed 2
and its locked threshold of 0.1172 are on the same line of the file, with
the file drawing the same conclusion the closure text draws: inside the
threshold, reported rather than rounded away. The syntax battery's
non-movement is stated in the file in the same words the closure text uses.

**Verdict: CLOSED, checked.** Nothing in the paragraph is stated beyond
what the cited file carries. One thing worth recording in the text's
favour rather than against it: the file itself flags that the pilot's
published 0.506 was a lucky single-seed draw and 0.5683 is the honest
figure, and 0.5683 is the number the closure text uses.

---

## `RT-144` — the "never run" claim about causal patching now names its ruling

**What the closure claims.** The sentence cites, in words and by number,
the ruling of 2026-09-20 that causal patching is new code rather than
existing machinery.

**The sentence, as it stands in version 4** (lines 100 to 104):

> Causal patching, which the section on how the ablation is localized
> (§3.2) requires alongside the probe before anything counts as localized
> or as absent, was never run and has no code for this design (the ruling
> of 2026-09-20 that patching is new code rather than existing machinery,
> ledger RT-96).

**Check 1, that the ruling says what the sentence says.**

    grep -n "^| RT-96 " experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md

**Output** (abridged to the load-bearing clauses; the row is one long line):

    531:| RT-96 | Causal patching is **not** "local and $0 with existing code".
    This experiment's source folder holds no patching script; the only patching
    code in the repository is Experiment 1's, written for a different model,
    vocabulary and grammar ... | **fatal** | ACCEPT | ... it is still new code
    on a registered instrument ...

**Check 2, independent of the ruling: is there patching code for this
design?** This is the check the closure rule exists for — the ruling is
itself a claim, and `RT-96` records that it was made "by listing file names
only". So I opened the one module that would hold such code.

    grep -n "^def \|^class " \
      experiments/06-mvm-0a-constructed-self-index/src/localize_a3.py

**Output.**

    74:def paired_episodes(n: int, seed: int):
    97:def residuals_at(model, eps, device, positions="revision"):
    142:def fit_probe(X, y, seed=0):
    163:def own_direction(X, y, rank=RANK_CAP):
    176:def run_l1(ckpt: str, lock: str | None, device: str = "cpu",
    212:def self_test() -> None:
    264:def main() -> None:

    grep -rn "patch" experiments/06-mvm-0a-constructed-self-index/src/*.py \
      | grep -iv dispatch

**Output** (the only hits in this design's own localization module):

    src/localize_a3.py:27:3. **Causal patching** takes the subspace from an episode where the model
    src/localize_a3.py:29:   action. If the action follows the patched identity, the subspace

Both hits are inside the module's opening description, which describes
patching as part of the method and never implements it. The remaining hits
across the folder are a local function named `patched` inside three
unrelated scripts that swap a transformer block's forward pass for a
lesion, and the word "patch" in two comments about curriculum fixes.

**Check 3, that the section named requires both instruments.**

    sed -n '/### 3.2/,/### 3.3/p' \
      experiments/06-mvm-0a-constructed-self-index/amendment-a3.md

**Output** (item 4 of that section):

    4. **Convergence requirement**, inherited: L1 counts as localized only
    when probe and patching agree on a confound-controlled design; otherwise
    the outcome is *not testable (localization)*, as Experiment 1 registered.

**Does the output match the claim?** Yes on all three counts. The module
that would run patching describes it and does not implement it; the
registered section requires it alongside the probe; the ruling cited says
it is new code.

**Verdict: CLOSED, checked.** Note for the record that the citation is to
a ledger row rather than to a file name, and the rule asks for a file name.
The ledger is a committed file (`red_team_ledger.md`) and the row is
findable, so this is a wording point and not an open finding. It is listed
again in the new-problems section because the same shortcut appears twice
more in this document without even a row number.

---

## `RT-145` — the ruling file is committed, but the sentence points at the wrong item

This is the one that does not close.

**What the closure requires.** Two things: commit the ruling, then a
measured check by another session that its successor item says what the
closure text's sentence says.

**Check 1, is the ruling committed?**

    git log --oneline -- docs/rulings/2026-09-20-december-result-roadmap.md

**Output.**

    acd8305 December-result roadmap and its ruling (2026-09-20), project data
    and center-as-degree amendment; left uncommitted by the session that wrote them

    git cat-file -e acd8305:docs/rulings/2026-09-20-december-result-roadmap.md && echo YES

**Output.**

    YES

The first half passes. The file the tier 1 pass could not find is in the
record, at a commit that lands before the one carrying version 4
(`b5aabab`).

**Check 2, does the item the sentence names say what the sentence says?**

The sentence, as it stands in version 4 (lines 148 to 151):

> It registers in 2026 through Gate A with both tiers, registration commit
> target 2026-10-11 and kill date 2026-10-18
> (`docs/rulings/2026-09-20-december-result-roadmap.md`, item 7, which
> amends item 5 of `docs/rulings/2026-09-20-center-as-degree.md`).

    sed -n '13,17p;44,46p' docs/rulings/2026-09-20-december-result-roadmap.md

**Output.**

    1. **The successor registers now.** Item 5 of
       `docs/rulings/2026-09-20-center-as-degree.md` ("registered after the
       hibernation condition") is amended: the matched-role causal-interchange
       experiment is registered in 2026, through Gate A with both tiers.
       Registration commit target 2026-10-11; kill date 2026-10-18.
    ...
    7. **The two kill dates are accepted**: registration committed by
       2026-10-18; registered runs launched by 2026-11-01. Missing either drops
       the roadmap to R4 (a schedule failure, named as such in STATUS.md).

**Does the output match the claim? No.** Every fact in the sentence is in
the ruling, and every one of them is in **item 1** — which is also the item
that amends item 5 of the center-as-degree ruling, exactly as the sentence
says its cited item does. **Item 7 is a different item.** It amends
nothing, and its two dates (registration committed by 2026-10-18, runs
launched by 2026-11-01) are not the two dates the sentence quotes. A reader
who does what the closure rule is designed to make possible — open the
named file and check the named item — lands on a paragraph that gives a
different registration date and does not contain the amendment claim.

**Cross-check that item 1 is the operative one**, from the other side:

    tail -7 docs/rulings/2026-09-20-center-as-degree.md

**Output.**

    ## Amendment 2026-09-20 (later the same day)

    Item 5 is amended by `docs/rulings/2026-09-20-december-result-roadmap.md`:
    the successor experiment is registered in 2026, through Gate A with both
    tiers, not after the hibernation condition. Registration commit target
    2026-10-11. Its three-arm form and result definition are in
    `docs/december-result-roadmap-2026-09-20.md`.

The amended ruling's own note confirms the substance, and again does not
point at item 7.

**Verdict: NOT CLOSED, checked.** The finding was that a registration
commit rested on a file the record did not contain. Half of it is fixed:
the file is in the record. The other half is not: the pointer into it is
wrong, so a checker who follows it is told something different from what
the sentence claims. This is a small error with a one-word fix, and it is
precisely the error the finding was about — a citation that cannot be
followed to what it promises. Because a registration commit is the one
commit that has to survive a hostile reader opening every citation, it
should not be made with this pointer in it.

**What would close it.** Change "item 7" to "item 1" in the successor
paragraph, and have a session other than the one that makes that change
confirm, by opening the file, that item 1 carries the 2026-10-11 target,
the 2026-10-18 kill date, the both-tiers requirement and the amendment to
item 5. Nothing else in the sentence needs to move. If the intention was
to cite both items — item 1 for the registration dates, item 7 for the kill
dates that grade the roadmap — then both numbers belong in the citation
with a few words saying which does what.

---

## `RT-153` — the two senses of "center" are now named

**What the closure claims.** The text names both senses, and does not
deliver the substance of a claim it has just refused.

**The text as it stands.** The first sense, in the paragraph headed "What
A3 did not measure" (lines 59 to 62):

> Whether the network built an internal structure around the ownership
> input — a center in the sense of something the network acquired — is not
> testable with these instruments.

The second, in the paragraph headed "Where this sits on the project's
gradient" (lines 129 to 136):

> Under the ruling of 2026-09-20 that a load-bearing self-index is a center
> (`docs/rulings/2026-09-20-center-as-degree.md`), "center" has a second and
> weaker sense than the one used above: a pointer that is causally
> load-bearing for the act is a center at the bottom of the gradient, with
> no requirement that the network built a structure to hold it. In that
> weaker sense — and only in it — what the lesion measured puts these
> checkpoints above zero.

**Check 1, against the ruling the sentence cites.**

    sed -n '36,42p;52,57p;79,84p' docs/rulings/2026-09-20-center-as-degree.md

**Output** (abridged to the three ruled items that bear on the wording):

    2. **The corpus holds one position: a load-bearing self-index is a
       center, at the bottom of the gradient.** A pointer that is causally
       load-bearing for the act is the floor at its thinnest ...
    4. **Consequence for the Amendment A3 closure text** ... the ownership
       input is load-bearing on three seeds; whether the network built an
       internal center around it is not testable with these instruments; its
       degree on the integration axis is unmeasured because the metric does
       not yet exist. No "structural", no "self-indexing".
    7. **The public sentence this commits the project to**: a 30-million-
       parameter transformer with a causally load-bearing ownership pointer
       sits above zero on this project's gradient, at a degree the project
       cannot yet measure.

**Check 2, on the sentence the finding said was the dangerous one.** The
finding's sharpest point was that "these checkpoints have one" is not in
item 4 and is the sentence the paper would quote.

    grep -n "these checkpoints have one" docs/a3-closure-text-draft-2026-09-21-v4.md

**Output.**

    (no output — the phrase is absent)

**Does the output match the claim?** Yes. Each sense is attached to the
ruling that licenses it, and the weaker sense is fenced by "and only in it".
The replacement wording, "puts these checkpoints above zero", is item 7's
own, and item 7's conditional tail ("at a degree the project cannot yet
measure") is carried in the next sentence. The public sentence at lines 139
to 143 reproduces item 4 clause for clause, with "for the primary battery"
added, which is the separate finding `RT-168` and which makes the sentence
narrower than the ruling rather than wider.

**Verdict: CLOSED, checked.**

---

## `RT-155` — the other-agent control is now described as half-run

**What the closure claims.** The text says the probe half ran, in the
phrasing the two rulings license, and says the lesion half is unavailable.

**The text as it stands** (lines 81 to 90):

> The registered matched control (§L2(a), the other-agent index) had its
> **probe half** run for the first time, with rank matched by design and
> accuracy matched as observed; it excluded the exclusion confound that had
> been proposed for that pattern, while a purely relational encoding remains
> open as a route that would produce both the pattern and this null
> (`other-index-position-sweep-findings.md`). The control's **lesion half**
> — a localized other-agent subspace whose ablation leaves the self-directed
> condition intact — remains unavailable, because no such subspace was found
> and there is nothing to ablate; running the probe half does not discharge
> the registered requirement.

**Check 1, against the ruling that forbids the elision.**

    grep -n "^| RT-142 " experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md

**Output** (the clause at issue):

    One point that must not be elided: the other-agent run is the first
    execution of the **probe** half of the registered other-index control;
    Part 3 item 2 asks for the **lesion** half, a localized other-index
    subspace whose ablation leaves the self-directed condition intact. The run
    found no such subspace at any testable position, so there is nothing to
    ablate and that control remains unavailable. Running the probe half does
    not discharge the requirement.

The closure text reproduces this almost word for word, including the final
sentence, which is the one the earlier draft contradicted.

**Check 2, against the ruling on how the match is to be recorded.**

    grep -n "^| RT-121 " experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md

**Output** (the clause at issue):

    Record it as "rank matched by design, accuracy matched as observed", not
    as the registered control run to specification.

The closure text uses that phrase exactly.

**Check 3, that the cited findings file carries the match and the null it
describes.**

    grep -n "class shares\|0.5390\|0.5670\|0.5310\|0.5665\|FOUND NOWHERE" \
      experiments/06-mvm-0a-constructed-self-index/other-index-position-sweep-findings.md

**Output.**

    19:**FOUND NOWHERE.** Sub-pattern: **nothing was found on any checkpoint.**
    110:**Matched in rank.** On the 4,000 episodes actually scored, the
    111:other-agent index has the same class shares as the own register index to
    122:| pilot | 0.5548 - 0.5670 | 0.5428 - 0.5665 |
    124:| seed 2 | 0.5390 - 0.5485 | 0.5310 - 0.5530 |

**Does the output match the claim?** Yes. The rank match is in the record
as a design property fixed before the run; the accuracy match is in the
record as two observed ranges; the file's own headline is the "nothing
found" that makes the lesion half unavailable. The one clause not in that
file is the relational-encoding route, which the ruling on it (`RT-125`)
says the findings file does not name; the closure text covers it with the
sentence at lines 91 to 92 attributing the paragraph's rulings to the Gate B
block `RT-120` to `RT-142`, and `RT-125` sits inside that range.

**Verdict: CLOSED, checked.**

---

## `RT-161` — the registered instrument-failure reading is back, in its own clause

**What the closure claims.** The registered reading is stated in its own
clause, and the inference pointing the other way is dropped or conditioned.

**The text as it stands** (lines 109 to 119):

> **The registered term for the line is therefore *not testable
> (localization)*, and the registered reading of this null is instrument
> failure, not absence.** The registration reads "ownership is known to be
> load-bearing and the instruments cannot find it" as a failure of the
> instruments until causal patching has run, and that reading stands. What
> can be said descriptively, and separately from it: these probes did not
> localize this target at these positions, at a heuristic reach of roughly
> one legible episode in eleven. What may not be said is that the structure
> is absent, or that these nulls make it less likely ...

**Check 1, against the three rulings that establish the registered
reading.**

    grep -n "^| RT-50 \|^| RT-92 \|^| RT-102 " \
      experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md

**Output** (the clauses at issue):

    363:| RT-50 | ... Under the registered text it is instrument failure until
    patching has run. |
    464:| RT-92 | ... The pre-registration reads a probe-only null against a
    centre known to be load-bearing as instrument failure. The registered term
    for where the line stands is *not testable (localization)* ... Repeated
    because the packet asks for it and because it is the clause most likely to
    be dropped when the paragraph is shortened. |
    537:| RT-102 | ... a null against a centre known to be load-bearing is
    registered as instrument failure, not absence ...

The closure text now carries both halves the rulings ask for — the term and
the reading — in a bolded sentence at the head of its own paragraph, which
is the position in the document least likely to be lost the next time the
paragraph is shortened. That is the failure mode `RT-92` names.

**Check 2, that the opposing inference is gone.**

    grep -n -i "less plausible\|readily recoverable" docs/a3-closure-text-draft-2026-09-21-v4.md

**Output.**

    (no output — the sentence is absent)

**Check 3, that the descriptive replacement's number is in the record it
belongs to.**

    grep -n -i "one episode in eleven\|heuristic" \
      experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings-CORRECTION-2026-09-20.md

**Output.**

    13:legible in about **one episode in eleven**. The same correction applies to
    19:step 4 proposal, the paper draft), it reads one in eleven and cites this

**Does the output match the claim?** Yes. The registered reading is stated
as the standing one rather than listed as one possibility among several,
the inference in the opposite direction is gone, and the descriptive
sentence that replaced it carries the record's own figure with the word
"heuristic" attached, which is what the separate finding on that number
(`RT-169`) asked for. The correction note is cited by name two paragraphs
earlier in the same document.

**Verdict: CLOSED, checked.**

---

## `RT-165` (serious) — the deferred marker-word read is carried, thinly

**What the rule allows.** A serious finding is closed like a fatal one, or
carried as an open item named in the registered text, with John's ruling and
reason.

**The text as it stands.** Named twice: in the body at lines 94 to 99 ("the
model's own marker word, has been read at these positions only by the weaker
difference-of-averages method ... Reading the registered target with a
sensitive instrument is one unrun job of about seventy processor-hours at no
money cost, and until it runs, only the narrower sentence above is
available"), and in the open-items list at lines 163 to 165.

**Check 1, that John's ruling to carry it exists and is committed.**

    grep -n "^| RT-165 " experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md

The row records the disposition of 2026-09-21 — accept as drafted — with
its reason, inside the block headed "rulings on RT-143 to RT-171". So the
ruling exists in a committed file.

**Check 2, on the state of the underlying question.**

    sed -n '86,99p' docs/rulings/2026-09-20-center-as-degree.md

**Output** (the relevant line of the list headed "What this ruling does not
decide"):

    - Gemini's Q5: whether the ~70-hour marker-word fitted read runs before
      the paper draft. $0 compute, Mac time.

**Verdict: CARRIED — the carry is real, and thinner than the rule asks.**
The item is named in the registered text, which is the substance of what
the rule requires, and the ruling to carry it is on the committed record.
Two things are missing from the registered text itself. It gives no reason
for the deferral, and the last committed ruling on the underlying question
says that question is undecided. A reader who notices that the job costs no
money and about seventy hours of a Mac's time will ask why a closure was
written instead of running it, and the text does not answer. This is not a
reason to hold the registration commit. It is one sentence that would make
the open item legible to a reader in six months: say that whether this read
runs before the paper is an open question for John, and point at the ruling
where it is parked.

---

## The second clause, swept across the whole document

The rule: every sentence saying verified, measured, calibrated or attacked
cites the committed record by file name, and the record contains what the
sentence says.

**Sweep run.**

    grep -n -i -E "verif|measur|calibrat|attack" docs/a3-closure-text-draft-2026-09-21-v4.md

Fourteen lines came back. Each was read in its sentence and dispositioned:

| line | the claim | record named | checked? |
|---|---|---|---|
| 26 | "was measured on three seeds", in the outcome headline | none in the headline; the same claim is cited twenty lines below | fair, see note |
| 28 | "the validity gates were clean and no instrument breached them" | **none, and none found** | **open, see new problems** |
| 35 | the control battery's ceiling "was measured at 1.0" | `ceiling-measurement-findings.md` | checked, matches |
| 38 | "the same measurement shows why this is structural" | same file | checked, matches |
| 41 | the ceiling number "was itself never attacked" | `ceiling-defect-2026-09-17.md` | checked, matches |
| 49-55 | the nine scores | `seeds-endpoint-findings.md` | checked, matches |
| 59 | "What A3 did not measure" | no measurement asserted | not applicable |
| 81 | "a sub-bar pattern measured twice, not a clearance" | `standardised-refit-findings.md` | **partly, see new problems** |
| 120 | the blind arm is "the measurement that would establish it" | `docs/rulings/2026-09-21-followup-runs-and-blind-arm.md` | checked, matches |
| 135 | "what the lesion measured" | the seeds paragraph above | fair |
| 138, 141 | the degree is "unmeasured" | `docs/rulings/2026-09-20-center-as-degree.md` | checked, matches |
| 152 | "measuring the control's ceiling properly is a precondition" | `ceiling-defect-2026-09-17.md` | checked, matches |
| 156-157 | the rehearsal requirement, "a full measurement procedure be demonstrated" | **none** | **open, see new problems** |

**The checks behind the rows marked "checked, matches".**

    grep -n -i "ceiling" \
      experiments/06-mvm-0a-constructed-self-index/ceiling-measurement-findings.md

    1:# The control battery's ceiling is 1.0, and the clause was never computable
    48:With a ceiling of 1.0, a defined drop needs a baseline of **1.10**.
    89:**So the ceiling-corrected metric and the concept of an ownership-free
       control are incompatible by construction.

    grep -n -i "attack\|precondition" \
      experiments/06-mvm-0a-constructed-self-index/ceiling-defect-2026-09-17.md

    1:# REGISTERED DEFECT -- the control battery's ceiling was never verified
    15:attack sweep**. Only the primary battery's was. The control battery's
    16:ceiling has never been attacked, and the single solver that produced it
    98:**If A4 opens, measuring the control's ceiling properly is a precondition
       of the amendment.

One small widening, noted without objecting to it: the defect file's
sentence is conditional on an Amendment A4 opening, and the closure text
generalises it to "any successor amendment". That is what the ruling on the
point (`RT-163`) asked for, so the text follows the ruling rather than the
file, and the ruling is the higher authority.

**The other cited records, checked the same way.**

    grep -n "0.3125\|0.60\|before the code existed" \
      experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot-findings.md

    4:written and committed **before the code existed** (`control-learnability-pilot.md`,
    15:about a third to about two thirds.** It scored **0.3125**.
    40:| LEARNED, at or above **0.60** | -0.2875 | **-11.98** |

    grep -n "270\|both arms" \
      experiments/06-mvm-0a-constructed-self-index/powered-position-sweep-findings.md

    10:**CARRIED NOWHERE, on both arms.**
    13:checkpoints -- **270 testable tests** -- **not one reached even three
    16:mean across all 270 was **-0.085**. Zero marginal clearances. Zero robust

    grep -n -i "eleven position\|five layer" \
      experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings.md

    1:# The fitted linear read at all eleven positions -- findings
    232:They may say that at these eleven positions, five layers and three

    sed -n '454,474p' experiments/06-mvm-0a-constructed-self-index/pre-registration.md

The loss condition the closure text quotes is reproduced in that section
word for word, including the phrase "the honest report is 'not testable'".

**The money figures.**

    grep -n -E "\$[0-9]" docs/a3-closure-text-draft-2026-09-21-v4.md

    125: a re-run is a $0 side item
    170: ~$44.3 of its $100 hard stop
    171: ~$225.7 of its $400 ceiling (`compute-ledger.md`, the running totals
         on the rows dated 2026-09-19 and 2026-09-20)

    grep -n "225.7\|44.3" experiments/06-mvm-0a-constructed-self-index/compute-ledger.md

**Output** (the 2026-09-20 row's final cell):

    71: A3 cumulative ~$44.2 / $100 before this -> **~$44.3 / $100** with the
    $0.07 recovery; **programme running total ~$225.6 + $0.07 = ~$225.7 / $400**
    (added 2026-09-21 so the A3 closure text can cite a figure the ledger
    contains).

The row before it, dated 2026-09-19, now carries its own programme total
(~$225.6 of $400), which is what the money finding (`RT-147`) asked for:
two consecutive rows without one is the failure the ledger's own 2026-09-17
correction named. Both figures the closure text quotes are in the ledger, in
the rows it points at. The `$0` at line 125 is quoted from the ruling cited
in the same sentence, and nothing was spent, so it needs no ledger row.
**Money: clean.**

**One claim about the document itself, which a reviewer should not take on
trust**, since everything the tier 1 pass checked in version 3 carries over
only if it is true. Version 4's preamble says the difference from version 3
is confined to the successor's registration date, the blind-arm sentences
and the money paragraph.

    diff -u docs/a3-closure-text-draft-2026-09-21-v3.md \
            docs/a3-closure-text-draft-2026-09-21-v4.md

The body changes are exactly four: the blind-arm sentences at the end of the
localization paragraph, the successor paragraph's date and citation, the
blind-arm entry in the open-items list, and the money paragraph. The rest of
the diff is the preamble. **The claim is true as stated**, and the tier 1
pass's twenty-nine checks on version 3's body carry over.

---

## New problems, not raised by anyone

**1. The wrong item number in the successor citation.** Covered above, as
the reason `RT-145` does not close.

**2. The one localization number that is not in the file cited with it.**
The closure text says, at lines 77 to 82, that the standardised refit
"crossed the family bar by 1.94 episodes in four thousand", and names
`standardised-refit-findings.md`.

    grep -n "1\.94" \
      experiments/06-mvm-0a-constructed-self-index/standardised-refit-findings.md

**Output.**

    (no output)

    grep -rn "1\.94 episodes" experiments/06-mvm-0a-constructed-self-index/

**Output.**

    red_team_ledger.md:640: clears by 1.94 episodes in 4,000, it is inside the
    estimation noise of its own
    red_team_ledger.md:655:| RT-128 | The one clearing cell clears the bar by
    0.000484 in accuracy, which is 1.94 episodes in 4,000 ... | fatal to
    reporting it as a clearance | ACCEPT | ... The findings say "suggestive and
    not settled" ... but never give these two numbers. The number and its
    fragility must travel together or neither travels.

The figure is right — the tier 1 pass checked its arithmetic and credited it
(`RT-148`) — and it is in the committed record. But it is in the ledger row
`RT-128`, and that row says in so many words that the findings file does not
contain it. So the closure text attaches a number to the one file its own
record says does not carry it. A checker doing what the closure rule asks
will open `standardised-refit-findings.md`, fail to find 1.94, and be unable
to tell whether the number is wrong or merely misfiled. The same sentence's
other half, "a sub-bar pattern measured twice, not a clearance", is John's
ruled wording and lives in
`docs/rulings/2026-09-21-followup-runs-and-blind-arm.md`, not in the file
cited either. Both are covered loosely by the sentence at lines 91 to 92
attributing the paragraph's rulings to the ledger block `RT-120` to
`RT-142`, which is why this is serious rather than fatal. The fix is a few
words: name the ruling row or the ruling file for the number, alongside the
findings file. `RT-128`'s own closing sentence — the number and its
fragility travel together or neither travels — argues for going further and
saying that moving the null spread by one standard error puts the cell on
either side of the bar.

**3. "The validity gates were clean" has no record, and I could not find
one.** At lines 27 to 29 the closure text separates its two senses of "not
testable" by asserting that "the validity gates were clean and no instrument
breached them". That is a measured claim about the instruments, in the
second sentence of the registered block, and it names no file.

    grep -rln -i "validity gate" \
      experiments/06-mvm-0a-constructed-self-index/*.md

**Output.**

    amendment-a3.md
    red-team-a4.md
    pre-registration.md
    separation-clause-requirements.md
    red_team_ledger.md

Every hit is a document that defines or discusses the gates. None is a
findings file reporting an outcome.

    grep -rln -i "rep-4\|degeneracy\|neutral-episode" \
      experiments/06-mvm-0a-constructed-self-index/*.md

The same shape: the gate metrics appear in the registration and in method
and review documents, and in no record of a gate having been run and passed
on the three A3 checkpoints. There may be a fair defence — the gates in §3.3
attach to ablations that read an L1 result, no L1 ablation was ever run, and
so nothing could have breached them — but that defence is the opposite of
what the sentence says. "Were clean" asserts that they were evaluated and
passed. If the truth is that they never had an occasion to fire, the
sentence should say so, because "clean gates" in a closure block will be
read by the paper as a positive validity result. This is the same class of
defect as `RT-143` and `RT-144`, in a sentence neither of them covered, and
of the four new problems it is the one I would rank second after the item
number.

**4. Two further "never run" claims with no record, where the third one has
one.** The fix to `RT-144` attached a ruling to the patching claim. Two
claims of the same form in the same document did not get the same treatment.

    grep -n -i "has never run\|unrun" docs/a3-closure-text-draft-2026-09-21-v4.md

**Output.**

    69:question, the mid-episode re-indexing probe, has never run.
    98:a sensitive instrument is one unrun job of about seventy processor-hours at
    165:positions. Causal patching, unwritten and unrun. The mid-episode re-indexing

The re-indexing probe's never-run status is on the record — the ledger row
`RT-114` states it, and the registration names that probe as the registered
discriminator for the tag bin, in its pre-stated signatures section and in
decision 11 — and neither is cited. The seventy-processor-hour figure is
likewise on the record, in the ledger row `RT-89` and in the center-as-degree
ruling's list of what it does not decide, and is cited nowhere.
Worth-noting rather than serious, because both claims are true and
checkable, and the patching sentence already shows the form the fix takes:
three or four words each.

**5. Smaller things, recorded so the next pass can see they were
considered.** The reference at lines 65 to 68 to "registration revision 8,
'The central claim is narrowed'" names no file; the text is section 8 of
`amendment-a3.md`, which is also the file this closure block will land in,
so a later reader could take it for a section of the pre-registration
instead. The rehearsal requirement at lines 156 to 158 cites nothing: it is
item 6 of the December-result ruling, and that ruling records the protocol
amendment carrying it as owed rather than written, so at the commit I read
the closure text asserts a requirement whose protocol text did not yet
exist. And one mislabel in the compute ledger rather than in the closure
text: the 2026-09-19 row credits its correction to "Gate A finding RT-143's
companion, the money citation", when the money finding is `RT-147`.

---

## Is version 4 fit for a registration commit?

**Not as it stands, and it is close.** One fatal finding does not close:
the successor paragraph's citation points at item 7 of the December-result
ruling when the facts it states are item 1's, which is the same failure of
checkable citation that `RT-145` was raised about. Three further claims —
the validity gates, the 1.94-in-four-thousand figure, and the re-indexing
probe's never-run status — carry no record a reader can open, and two of the
six original fatal findings were exactly that. Every one of these is a few
words. None requires a run, a ruling or a rewrite.

Five of the six fatal findings close on measurement, and they close well:
the nine scores reproduce in the file named; the patching claim survives an
independent look at the source folder rather than resting on the ruling that
asserts it; both senses of "center" are fenced by the rulings that license
them, and the sentence the paper would have quoted is gone; the other-agent
control is described in the exact words two rulings require, including the
sentence saying the probe half does not discharge it; and the registered
instrument-failure reading is back in a bolded clause at the head of its own
paragraph, which is the hardest place in the document to lose it. The money
figures are in the ledger. The preamble's claim about what changed between
version 3 and version 4 is true, so the tier 1 pass's work carries.

**Recommendation.** Fix the item number, attach records to the three
uncited claims, and have the closure check on the item number run by a
session other than the one that makes the change, as the rule requires.
Then this text is fit to register, with its date placeholder filled by the
commit that files it.
