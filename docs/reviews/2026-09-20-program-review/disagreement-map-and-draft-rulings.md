# Program-level outside review: disagreement map and draft rulings

*Written 2026-09-20 (Pacific) in the Cowork session, after both tier-2
responses were filed verbatim (`response-gemini.md`, Gemini 3.1 Pro;
`response-chatgpt-astra.md`, GPT-6 Astra). Status: DRAFT rulings for John.
Nothing here is ruled until he says so; the recommended disposition on
each item is Claude's, and Claude is the co-author the reviewers were asked
to check, so every "decline" below deserves more suspicion than every
"accept". Written under the plain-language rule; shorthand is expanded on
first use.*

## What the two reviewers saw, and why it differs

The two packets were not identical. Gemini read the bundles as built at
about 09:50 Pacific on 2026-09-20, from the repository at commit `1f9d2af`.
Astra's file tool truncated those bundles, so they were rebuilt as 20 KB
parts about two hours later, by which time three commits had landed
(`d72c52b`, `d0d376d`, `2e26bbc`): the Gate C tier-1 review of the step 4
proposal (ledger items RT-94 to RT-117), proposal version 2, and John's
early ruling of step 4 (Amendment A3 closes as *not testable*; claim scope
narrowed; localization order set). So Astra reviewed a record in which the
2026-10-04 decision had already been taken, and says so; Gemini reviewed
one in which it was still open. Where the two disagree about step 4, part
of the gap is that they were answering different states of the record.

Both read bundles 1 and 2 in full. Gemini opened three files of bundle 3
(the A4 proposal, `red-team-a4.md`, `red-team-pass-3.md`); Astra opened none
of bundle 3 and lists what it would have wanted from it.

## The short answer to John's question

John asked whether the program is on track to a meaningful result and
whether the process needs to change. Taking both reviews together:

The process is doing the part it was built for. Both reviewers credit it
with stopping over-claims and spend (Gemini: "functioning exactly as
intended"; Astra: "stopping claims from becoming stronger than the
evidence"). Neither found an arithmetic or record error the ledger had not
already caught. Gemini's two "fatal" findings restate corrections the record
made on 2026-09-17 and 2026-09-19.

The theory has a gap the process cannot close. Astra's A1 is the finding of
this review: even the outcome Amendment A3 hoped for, a localized acquired
own-index whose lesion degrades the task and whose swap moves the action,
is what an ordinary agent-tracking mechanism (a table of agent, item and
value plus a pointer to "which agent am I") would also produce. Amendment
A3 §5 R4 concedes this ("cannot separate an indispensable mine-bit from a
center"). No experiment inside the remaining budget fixes it, because what
is missing is a stated observable that a tracker cannot satisfy and a
center must, not compute. Gemini did not see this; it treats the registered
discriminators (re-indexing probe, swap) as sufficient if run.

So: the program can produce a meaningful result, but a narrower one than
the spec names, and the record's 2026-09-20 claim scope ("the ownership
input is load-bearing for the primary battery on three seeds") is already
that result. Both reviewers say it is publishable, to interpretability and
evaluation-methods readers, as a methods and negative-result contribution.
The change to the process is upstream of any gate: before the successor
experiment is registered, a one-page statement of two competing mechanisms
and the observation that separates them, or an explicit decision to pursue
the narrower question.

## Where the reviewers agree with each other

1. Close Amendment A3 now rather than repair it (Gemini: "neither A nor D"
   but stop repairing the control; Astra: option A, as the record ruled).
2. The original public claim scope, "a structural signature of
   self-indexing in small constructed models", is over-claimed on the
   evidence. Astra endorses the 2026-09-20 replacement wording; Gemini
   proposes a near-identical sentence ("authorship inputs are specifically
   load-bearing for perspective-dependent tasks in small constructed
   transformers").
3. "Not testable (localization)" is the correct registered status of the
   probe nulls (both), and causal patching has never run and has no code
   for this design (both; the record found this at RT-96).
4. Same-model review with blanket acceptance is a governance check, not
   independent validation (Gemini process change 2; Astra A9). Both want an
   independent party to own a small decisive verification, not just read.
5. Registered constants and comparators should be demonstrated
   computable before the threshold lock (Gemini process change 1; Astra
   process change 3 and A8). This is the closure rule extended backwards
   from fixes to designs.
6. The result is publishable as a methods contribution to interpretability
   and evaluation-design readers, with the failed controls as content.

## Where the reviewers disagree with each other

| Question | Gemini | Astra | Note |
|---|---|---|---|
| Can the A3 design distinguish a center from an agent tracker? | Yes, if the re-indexing probe and swap are run; "currently unreachable" only because no L1 target has been found | No; a tracker with a pointer produces every observation A3 measures, and A3 §5 R4 concedes it (A1, fatal) | The central disagreement. Astra cites the registered text; Gemini does not engage §5 R4. |
| What single experiment to run next | Fitted linear read on the marker word at the nine positions (~70 processor-hours), then patching if a signal appears; priced at "~$70" | A matched-role causal-interchange experiment as a successor with its own registration ($40 to $80), gated on both tasks learning; nothing inside the ceiling settles the center question | Gemini's price is wrong: the run is local and $0 in compute, about 70 hours of Mac time (fitted-read brief). Gemini's experiment is the one the 2026-09-20 ruling deferred; Astra's is the requirements document's first-ranked redesign (H2 option 1). |
| Experiment 1's verdict | "A finding about the hypothesis" | Informative against the center reading, but the +0.033 router gap with a confidence interval spanning zero does not identify a router; replace "No center was removed" with "these interventions did not demonstrate removal of a center" | Astra's is the stricter reading of the 2026-08-04 uncertainty addendum, which the record itself flagged. |
| The control-learnability pilot's reading | A capability finding at 30M | A bounded result about one reweighting on one seed; the claim that the control learned "the whole name-blind procedure and none of the name-keyed lookup" is not established by an aggregate score (A6) | Astra's A6 is a new finding; the sentence is in STATUS.md's current state. |
| Process pattern | Under-specification before launch; "treating registration as an iterative sandbox" | Same diagnosis, stated as feasibility and construct-validity failures reaching execution; amendments per se are not the problem | Agreement on substance; Astra separates the count of ledger items from the count of defects. |

## Where both reviewers disagree with the record

1. Roadmap step 8's claim scope, as approved 2026-09-16 and as conditioned
   in the 2026-09-20 ruling (holds "only if the localization line produces
   a localized result"). Both say the structural wording is unearned now;
   Astra adds that a localized result would not restore it either, because
   of A1. Recommended: amend ruling 3 of 2026-09-20 so that a localized
   result earns "a localized, causally load-bearing ownership
   representation", never "self-indexing".
2. The record's confidence that supervision and seed variance are excluded
   as causes of the control's failure ("not a seed lottery", STATUS
   2026-09-19 §2). Astra A5 says three of three seeds failing narrows, not
   excludes. Gemini's capability reading implies the same.

## Where one reviewer disagrees with the record and the other does not

Astra only: A3 (the ownership-blind optimum is not a lower bound on a
lesioned network's score, so "pushed below what a solver that knows nothing
about ownership can reach" describes a number, not an anomaly); A4 (the
ledger's prohibition on saying "not localized" collapses a registered status
with a descriptive statement); A7 (a defective decision rule's verdict is
kept as if authoritative; the signed-rule case); A10 (the blind arm is
recorded as discharged on 2026-09-19 and scheduled first on 2026-09-20);
A11 (the "one episode in eleven" sensitivity figure is not measured power);
A12 (Experiment 3's headline "pressure suppresses assertion, almost never
belief" exceeds what a release-prompt reassertion measures).

Gemini only: G3, disputing that "the linear-read line is closed". The record
withdrew that sentence on 2026-09-19 (STATUS: "what this closes is the
difference-of-averages read, not the linear read"), in a section Gemini's
packet contained. Gemini argued against a reading the record no longer
holds.

## Draft rulings, Gemini (G1 to G5 and its recommendations)

Tier-2 findings take RT numbers only when adopted (protocol, filing
section). "Credit" means the finding confirms a correction the record had
already made; it is recorded so the confirmation is on file.

| Item | Finding, in short | Recommended ruling | Reason |
|---|---|---|---|
| G1 | Control ceiling is 1.0; the differential clause is uncomputable | ACCEPT AS CREDIT, no RT number | Restates `ceiling-measurement-findings.md` Verdict A (2026-09-17) and STATUS 2026-09-19 §3. Independent confirmation from another lab is worth having; it is not new. |
| G2 | Probe null cannot be read as "absent" without patching | ACCEPT AS CREDIT | Restates RT-49 and RT-50. |
| G3 | The "linear-read line is closed" claim is invalid | DECLINE AS MOOT | The record withdrew the sentence on 2026-09-19; Gemini's packet contained the withdrawal. Record that the reviewer's own conclusion matches the record's current position. |
| G4 | Amendment A4 uncomputable (comparator has a fifth of the room to fall) | ACCEPT AS CREDIT | Restates `red-team-a4.md` F1, on which A4 was refused 2026-09-19. |
| G5 | Fixed positional batch split in the pilot risks bias | ACCEPT AS CREDIT | Is RT-58, open, with a $0 check ordered on 2026-09-20. |
| Q5 recommendation | Neither A nor D; run the marker-word fitted read, then patching if a signal appears | CARRY OPEN, FOR JOHN | Conflicts with the 2026-09-20 localization order (blind arm, then other-agent index and refit, then patching) and with RT-103 (patching has no target until a probe finds one). But it puts a real question back: the marker-word read is the only run against the registered probe target with a sensitive instrument, the ledger says closure can only make the narrower sentence until it runs (RT-89, RT-112), and it was deferred on time, not on merit. John rules whether the ~70 hours of Mac time run before the paper draft (2026-10-25). Compute cost is $0; Gemini's "$70" is an error. |
| Process 1 | Unit-test every registered constant and ceiling before the threshold lock | ACCEPT, protocol amendment (Gate A text, John's gate) | Same as Astra process change 3. Would have caught the 0.3227 ceiling on 2026-09-15. Fold into the closure rule as a pre-registration rehearsal requirement. |
| Process 2 | Decouple red team from author with a zero-context model instance | ACCEPT AS PARTLY IN FORCE | Tier 1 already requires context isolation; tier 2 requires other labs. What is not in force is the reviewer owning a verification (see Astra A9). |
| Process 3 | No localization null analysed until patching code exists and passes a known-answer test | ACCEPT THE TEST, DECLINE THE ORDER | The known-answer requirement is already RT-103's closure. Blocking all analysis on patching inverts the 2026-09-20 order (RT-105) and would have blocked the fitted read that produced the current null. |
| Before 2026-10-04 | Patching script built, merged, validated on a synthetic known-answer test | CARRY OPEN | Consistent with the ruled order only as the third item; the two authorised runs and the blind-arm reconciliation (Astra A10) come first. |

## Draft rulings, Astra (A1 to A12 and its recommendations)

| Item | Finding, in short | Recommended ruling | Reason and closure |
|---|---|---|---|
| A1 | Even a successful A3 lesion and swap would not distinguish a center from an ordinary tracker with a pointer; A3 §5 R4 concedes it | ACCEPT, takes an RT number, **fatal to the program-level claim, not to A3's closure** | The finding of this review. It does not change the A3 closure (already *not testable*). It changes what any successor may claim and what must exist before one is registered. Closure: a one-page competing-mechanisms statement (ordinary tracking; the additional structure the spec proposes; the observation that separates them) committed before any successor pre-registration, and reviewed at Gate A. If no such observation can be stated, the successor's question is stated as the narrower one (how a small trained system uses an ownership signal and whether a causally identifiable internal representation develops) and the spec's floor claim is recorded as not operationalized. This also amends 2026-09-20 ruling 3 (see "both disagree with the record", item 1). |
| A2 | The original claim scope is unearned; the 2026-09-20 wording substantially fixes it | ACCEPT AS CREDIT with one change | Already ruled at RT-113. The change: make the narrow wording unconditional in the roadmap (strike the "holds only if localized" clause per A1). |
| A3 | The ownership-blind optimum is not a lower bound on a lesioned network's score | ACCEPT, worth-noting | The record reports drops above 1.0 as "below what a solver that knows nothing about ownership can reach" and draws no anomaly from it, but the sentence invites one. Closure: add one clause where the metric is explained (STATUS current state, the paper's methods) that a lesioned network is not an optimal blind solver, so a drop above 1.0 measures damage, not a paradox. |
| A4 | Three statements must stay separate: registered status (not testable), observation (these probes did not localize this target at these positions), inference (strong readable versions are less plausible) | ACCEPT | RT-92's prohibition on "not localized" is a ruling, not registered text, and can be narrowed. Closure: amend RT-92's ruling line to forbid "not localized" only as a verdict, and permit the descriptive sentence with its qualifiers; carry the three-statement form into the closure text. |
| A5 | The nulls do not eliminate a seed lottery or exclude supervision; three of three is narrowing, not exclusion | ACCEPT WITH CHANGE | Closure: annotate STATUS 2026-09-19 §2 ("not a seed lottery") and the pilot section's "reweighting the rows it already had is not what this battery is missing" with the bounded wording Astra proposes ("this reweighting did not make the control usable"). Annotate, never rewrite. |
| A6 | "Learned the whole name-blind procedure and none of the name-keyed lookup" is not established by an aggregate score of 0.3125 | ACCEPT | New. The sentence is in STATUS.md's current state and in proposal v2 settled item 4. Closure: either an item-level check on the existing pilot endpoint (does the control's error pattern match the name-blind solver's predictions item by item; $0, existing artifacts, method committed first) or the sentence is replaced by the score alone. |
| A7 | Pre-registration is being used to preserve a defective verdict's authority, not just its audit trail (the 2026-09-16 not-testable verdict under the absolute-value rule; Experiment 3's post-hoc uncertainty) | ACCEPT AS PRINCIPLE | The record's "annotate, never rewrite" rule already keeps the audit trail. What A7 adds: the annotation must say the rule was invalid for its inference, not only that the interpretation is superseded. Closure: one sentence added to the 2026-09-16 blind-control annotation and to the Experiment 1 addendum where the uncertainty analysis weakened the verdict. |
| A8 | Registration repeatedly preceded a demonstration that the full measurement procedure existed | ACCEPT | Same as Gemini process 1. Closure: protocol amendment, "measurement rehearsal" before any Gate A pass: target identifiable, comparator has headroom, arithmetic finite, interventions run end to end on a checkpoint, all three outcome bins reachable, and an ordinary competing solver built. John's gate (protocol text). |
| A9 | Same-family review plus "agreed on all" is governance, not independent validation | ACCEPT | Closure: protocol amendment so that at Gate A the tier-1 reviewer owns one decisive verification (reproduce the denominator, build the competing solver, or run the intervention) rather than only reading; and the ruling record distinguishes "accepted the argument" from "checked the claim". |
| A10 | The blind arm is recorded discharged (STATUS 2026-09-19 §4 and §7) and scheduled first (2026-09-20 ruling 4) | ACCEPT, **JOHN TO RECONCILE** | Real contradiction, and RT-99 already noted the review set did not say where step 3 stood. Either the registered arm ran on 2026-09-16 (NOT FLAGGED, instrument failure to locate, on an A2 register-bearing checkpoint), in which case ruling 4's first item is void and the order begins with the two authorised runs; or a rerun with a different, valid target was intended, in which case that target must be named before it runs. No run until reconciled. |
| A11 | "One episode in eleven" is not measured detection power; it assumes marker-position signal geometry transfers | ACCEPT | Closure: the follow-up runs brief and any future probe method state power by planted alternatives (including weak and distributed signals) across repeated samples, and report the null distribution and control performance; the existing sensitivity figures are annotated as heuristic. |
| A12 | Experiment 3's headline "pressure suppresses assertion, almost never belief" exceeds what a release-prompt reassertion measures | ACCEPT WITH CHANGE | The masked/capitulated decomposition stands; the word "belief" does not. Closure: annotate `results.md` (registered results, annotate not rewrite) and correct the sentence wherever it is quoted (STATUS, the paper draft, the sibling repos' report of W2). |
| Q5 recommendation | Option A; the successor is a matched-role causal-interchange experiment with a learn-both eligibility gate, $40 to $80 | ACCEPT AS THE SUCCESSOR CANDIDATE, not ruled | Matches the requirements document's first-ranked redesign (H2 option 1) and RT-106. Registers after public release, after the A1 closure exists, through Gate A with both tiers. |
| Process 1 to 7 | Narrow claim; reconcile current state; rehearsal; item-level checks; a human methods reader before the successor design; power calibration; fewer duplicate findings and strike "unlikely" from the fixed brief | ACCEPT 1 to 6; 7 FOR JOHN | 1, 2, 4 and 6 are the closures of A2, A10, A6 and A11. 3 is A8. 5 moves the outside human reader (roadmap step 7) forward to before the successor is designed, which is a roadmap change. 7 changes protocol text: the fixed brief's "a target with nothing fatal is a possible finding, but an unlikely one" rewards severity production, and this program review's own brief dropped the equivalent sentence for the same reason before it went out. |
| Before 2026-10-04 | Closure statement; blind-arm reconciliation; pilot log and two checks; corrected claim inventory; competing-mechanisms page; bounded publication plan | ACCEPT as the pre-closure list | Items 1, 3 are already ruled (2026-09-20 rulings 2 and 5). Items 2, 4, 5, 6 are new and are the closures of A10, A5/A6, A1, and A2 respectively. |

## Decisions for John, in order of consequence

1. **A1.** Accept as the program-level finding, and require the
   competing-mechanisms page before any successor registration. Or decline,
   with the reason on record. Everything else about the successor waits on
   this.
2. **Ruling 3 of 2026-09-20.** Strike the conditional that a localized
   result restores "a structural signature of self-indexing". Replace with
   the wording a localized result would actually earn.
3. **A10.** State whether the blind-localization arm is discharged (ran
   2026-09-16, NOT FLAGGED) or whether a rerun with a new target was
   intended. Until then, the first item of the 2026-09-20 localization
   order does not run.
4. **Gemini's Q5.** Whether the ~70-hour marker-word fitted read runs before
   the 2026-10-25 paper draft. $0 compute; Mac time. It is the only test of
   the registered probe target with a sensitive instrument, and without it
   the closure text carries the narrower sentence (RT-112).
5. **Protocol amendments** (A8/Gemini 1, A9, Astra 7): the rehearsal
   requirement before Gate A, the reviewer-owned verification, and the
   removal of "unlikely" from the fixed brief. Protocol text is John's gate.
6. **Roadmap change** (Astra process 5): the outside human reader before the
   successor design, not only before publication.
7. **The remaining accepts** (A3 to A7, A11, A12, and the Gemini credits):
   annotation and wording work, all $0, done in a Claude Code session once
   ruled, each annotation dated and beside the original.

## What this review did not do

Neither reviewer ran code, so every finding is ARGUED. Neither read the
paper drafts. Astra did not open bundle 3, so its view of the tier-1
reviews' independence rests on the ledger's account of them. The two
reviewers saw different states of the record, described above. The brief
was written by Claude, and Astra's process change 7 shows a reviewer can
notice when a brief steers; the "what has happened" summary was
fact-checked by a separate session before it went out, but the five
questions were not, and question 4's original wording had to be de-loaded
in draft.
