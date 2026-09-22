# MVM December-result roadmap (2026-09-20, Pacific)

*Status: APPROVED by John 2026-09-20 (Pacific), "Agreed on all" on the seven
items of section 7; ruling recorded in `docs/rulings/2026-09-20-december-result-roadmap.md`,
together with a standing rule that recommendations for spending above a cap are
proposed to him with the number, never worked around as impossible. Drafted in
the Cowork session of 2026-09-20 at John's request ("build a roadmap that has a
genuine result as its goal by the December deadline"). Where it changes
registered or protocol text, the text lands through Gate A of
`docs/outside-review-protocol.md`. Companion to
`docs/program-roadmap-2026-09-20.md` (which it refines, not replaces),
`docs/rulings/2026-09-20-center-as-degree.md`, `docs/competing-mechanisms-2026-09-20.md`
and `docs/a3-closure-text-draft-2026-09-20.md`.*

*Amended 2026-09-21: John ruled that work is measured in task time, not calendar
time — "We are not working on a delayed calendar. We are working on a finish
every task as quickly as possible mode." Section 4's week-by-week table is now
an ordered chain of what must finish before what, and the dates that were pacing
choices elsewhere in this document are stated the same way. No work item, owner,
cost, outcome or kill date changed; only how timing is expressed. The dates that
are commitments rather than pacing — the two kill dates, the book text lock, the
wrap-up start and the hibernation condition — are unchanged and are called out
where they bite.*

## 1. The question, restated so it can be answered by 2026-12-21

After the 2026-09-20 rulings the program's open question is one of degree: a
causally load-bearing self-index (a pointer to "which agent am I" that the act
depends on) is a center at the bottom of the project's gradient, and what
separates it from a center in the fuller sense is how much of the act is
organized around it. That axis is Stage 2 of `ROADMAP.md` ("global mutual
constraint versus modular shortcuts"), and its metric does not yet exist.

So the question this roadmap aims to answer by 2026-12-21 is:

> Can a decomposability metric, validated on systems whose degree is known by
> construction, read the degree of a freely trained 30-million-parameter
> transformer that acquired a load-bearing ownership pointer under task pressure?
> If so, what does it read?

Two things this question is not. It is not "is anyone home" (the founding wager
carries that step and no experiment settles it). And it is not "tracker or
center" as kinds (ruled one axis on 2026-09-20).

## 2. What counts as a result (to be registered, not just stated here)

The result has three registered outcomes. Each is a genuine result under the
program's own rules; only the fourth row is a failure of this roadmap.

| Outcome | Registered term | What it means | Satisfactory? |
|---|---|---|---|
| R1 | **metric validated, degree read** | The metric separates the by-construction contrast arms at the pre-stated bar, and the free-trained model gets a reading with paired uncertainty across seeds. The A3 closure sentence "degree unmeasured" is replaced by a number. | Yes |
| R2 | **metric does not separate** | The contrast arms are learned (eligibility gate passed) but the candidate metric cannot tell them apart at the bar. The metric is not used; the result is that this candidate does not read degree on this substrate, and the registered successor design for resumption says what to try next. | Yes |
| R3 | **substrate not a testbed** | One or more arms fail the learn-both eligibility gate after the one permitted re-run. Astra's reading: this recipe and size are not yet a mechanism testbed. Registered as such; resumption starts from a size or recipe change. | Yes, if the gate was reached |
| R4 | (none) | Registration not committed, or runs not launched, by the kill dates in section 5. The program hibernates with a registered design and a rehearsal only. | No. Recorded as a schedule failure, not a scientific one |

The separation bar for R1 versus R2, the eligibility threshold for R3, the
seed count and the paired-uncertainty method are set by the rehearsal (section
4, step 2 of the chain) and fixed in the registration text. This document does not invent
the numbers; it fixes that they are fixed before any run.

## 3. The experiment, in one paragraph

Astra's matched-role causal-interchange design (`response-chatgpt-astra.md` §5;
the requirements document's first-ranked redesign, H2 option 1), extended from
two arms to three so that the metric has known cases on both ends:

- **Arm T (tracker by construction).** Same task, same size, but the
  architecture keeps an explicit agent-item-value table and a separable pointer
  slot for "which agent am I"; the pointer is patchable on its own by design.
  Its metric reading should be at or near zero.
- **Arm C (entangled by construction).** Same task, same size, but the ownership
  signal is mixed into the content representation at every layer (for example
  multiplicative conditioning of every block's residual stream) so that no
  single patchable pointer site exists. Pointer-only patching should fail to
  reproduce the counterfactual; joint patching should succeed. Its reading
  should be high.
- **Arm F (free).** The ordinary transformer, trained without either constraint
  on the same matched-role task: own-directed and named-other-directed revisions
  at comparable action positions, comparable supervision, matched difficulty.
  This is the system being read. It must pass the learn-both eligibility gate
  and the ownership-lesion check (its pointer is load-bearing) before it is read.

The metric, as drafted in `docs/competing-mechanisms-2026-09-20.md`: accuracy
lost when the counterfactual action is produced by patching the nominated actor
representation alone versus patching the joint state, normalized by joint-patch
accuracy. Zero is fully separable; it rises as the act resists decomposition.
The candidate actor representation is nominated on development data; the
selection procedure, patching operation, controls (content swaps, other-agent
representation, position- and norm-matched interventions, fresh marker/content
combinations) and predictions are frozen before fresh episodes and confirmation
seeds are evaluated.

Arm C is the addition this roadmap makes to Astra's design. Whether an
entangled-by-construction arm can be built so that its degree is actually known
(rather than assumed) is the first thing the rehearsal has to show, and if it
cannot, the registration falls back to two arms (T and F) with the metric's
validation resting on T alone, which is weaker and is said to be weaker.

## 4. The order of work: what must finish before what

This section used to be a week-by-week calendar. John ruled on 2026-09-21 that
work is measured in task time, not calendar time — in his words, "We are not
working on a delayed calendar. We are working on a finish every task as quickly
as possible mode." So each step below starts as soon as the things it depends on
are finished and it is ready to run, and nothing waits for a date.

Five dates survive the change, because each is a commitment or a fact about the
world rather than a pacing choice: the two kill dates of section 5
(registration committed by 2026-10-18, registered runs launched by 2026-11-01),
the book text lock of 2026-09-30, the wrap-up start of 2026-12-21 (ruled;
nothing new launches after it) and the hibernation condition complete by
2027-01-04, when the SERE pipeline starts. Dates are Pacific. "CC" is a Claude
Code session; "Cowork" is this assistant; "John" is a ruling, a reviewer session
he runs by hand, or an edit in another repo.

| Step | What must finish first | Critical path | In parallel | John's items |
|---|---|---|---|---|
| 1. Rulings and the successor draft | Nothing. This is the head of the chain. | Rule the section 7 changes (successor registers now; patching code folds into the successor). Draft successor proposal v1 (CC): task grammar, three arms, metric spec, rehearsal plan, spend estimate. | Two authorised $0 runs finish (other-agent index control, standardised refit). Blind-arm status reconciled (Astra A10). A3 closure text: tier 1 review. | Book lock edits (ch05 degree reading) in calibration-problem. Rule A10. Site secrets. |
| 2. Proposal review and the measurement rehearsal | Successor proposal v1 drafted (step 1). | Gate C tier 1 on proposal v1. **Measurement rehearsal** (CC, ~$0 to $10): tiny models, show the three arms are constructible, the pointer in T is patchable, the joint patch in C works, the metric returns positive, negative and invalid values on toy cases, throughput of the new grammar measured. | A3 closure text: tier 2 sessions, John rules, lands (Gate A) — after its tier 1 review in step 1. | **Book text lock 2026-09-30** — a fixed date, not pacing. Run two tier 2 sessions for A3 closure. Rule on it. |
| 3. Registration text and Gate A | Rehearsal findings in, and Gate C tier 1 answered (step 2). | Rehearsal findings fix the bars. Registration text final (v2). Gate A: tier 1, then tier 2. **The registration is committed as soon as both tiers are answered and John rules** — there is no target date; the only date is the kill date in this row's last column. | Generator, T and C architectures, patching code implemented against the rehearsal (CC). | Run two tier 2 sessions on the registration. Rule. **Kill date 1 bites here: registration committed by 2026-10-18** or the roadmap drops to its fourth outcome (R4, a schedule failure rather than a scientific one) and says so. |
| 4. Freeze and development runs | Registration committed, and the implementation written (step 3). | Implementation frozen; unit tests; the RT-58 even-split rule and the one-scored-token self-test carried over. Development runs at 10M (~$10). | Compute ledger rows opened with estimates. | None. |
| 5. Registered training launched | Implementation frozen and tested, development runs clean (step 4), and John's launch approval. | **Registered training launched**: three arms × three seeds at 30M, ~$110 at the ledger's $12 per run (the 3.5× RunPod anomaly of 2026-08-08 is the risk; if it recurs, seeds drop to two on T and C, three on F). Eligibility gate evaluated as runs land. | Actor-representation nomination on development episodes begins as F checkpoints arrive. | Approve launch (spend gate). **Kill date 2 bites here: registered runs launched by 2026-11-01** or the same drop to the fourth outcome (R4). |
| 6. Nomination, patching, and the validation result | Registered runs landed and the eligibility gate evaluated (step 5). | Nomination frozen and committed. Patching on fresh episodes, all arms. Metric computed on T and C: the validation result. | One permitted re-run if an arm failed eligibility (~$12). | None unless a re-run needs a go. |
| 7. Validation findings and Gate B | The validation result computed (step 6). | Validation findings written. **Gate B** (tier 1, tier 2). John rules: R1 path (read F), or R2/R3 closure. | Site and `data/project.toml` updated with the validation state. | Run two tier 2 sessions. Rule. |
| 8. The reading, or the closure draft | John's Gate B ruling (step 7). | R1: read arm F on the frozen procedure, confirmation seeds. R2/R3: draft closure text and the resumption design. | Patching-code defects found at Gate B are fixed here. | None. |
| 9. Findings document and Gate B tier 1 | The reading, or the null, complete (step 8). | Findings document for the reading (or the null). Gate B tier 1. | — | Start tier 2 sessions if tier 1 is clean. |
| 10. Gate B tier 2 and the closure draft | Gate B tier 1 clean (step 9). | Gate B tier 2, ruling. Closure text drafted (registered text). | If this step lands over the Thanksgiving holiday, expect John's time to be short. | Rule. |
| 11. Gate A on the closure text | Closure text drafted (step 10). | **Gate A on the closure text** (tier 1, tier 2). Ruling. Closure lands in the successor's registration file. | State-of-the-program write-up drafted (Cowork). | Run two tier 2 sessions. Rule. |
| 12. Records closed and the write-up sent | The closure text landed (step 11). | STATUS.md, `data/project.toml`, site, ledger closed with actual-after rows. Write-up to the outside human reader (shortlist doc). | `RESUME.md` drafted. | Choose and contact the outside reader. |
| 13. Explainer refresh | The records are closed (step 12), and the book text lock of 2026-09-30 has passed. | `explainer.md` refresh, if the chain reaches it before wrap-up starts (this was the "if time" item of the old slack week, and it stays conditional). | — | None. |
| 14. Wrap-up | Everything above, or a kill date having fired. **Starts 2026-12-21** (ruled); nothing new is launched after that date. | **Wrap-up** (ruled): hibernation condition per the program roadmap, **complete by 2027-01-04**. | — | Final ruling that the hibernation condition is met. |

Gate count on the critical path: four (A3 closure Gate A, registration Gate A,
validation Gate B, closure Gate A), plus one Gate B on the reading if R1. Each
costs one tier 1 worktree session and two tier 2 sessions John runs by hand,
then a ruling. At the observed pace (the 2026-09-20 reviews turned around
inside a day when John was available) a gate costs two to four days; over a
holiday it costs a week.

**What used to be slack, restated.** The calendar version of this section kept
one empty week at the end whose job was to absorb a single slipped gate, and it
noted that a holiday week would cost more than an ordinary one. Running in task
time there is no week set aside: the chain moves as fast as the work finishes.
What stands in its place is the room the two kill dates leave. From 2026-09-21
that is about four weeks before the registration must be committed (2026-10-18)
and about six before the runs must be launched (2026-11-01). The first of those
has to hold the measurement rehearsal, the Gate C pass on the proposal and the
registration's full Gate A, with the A3 closure Gate A running alongside; the
second adds the freeze, the development runs and John's launch approval. A gate that stalls, or a holiday that turns a three-day gate into a
week-long one, now eats that room directly rather than a week reserved for it —
which is why the kill dates, and not a calendar, are what the plan is held to.
After the launch the only fixed point is the 2026-12-21 wrap-up start;
everything between the launch and wrap-up runs as fast as it finishes, and a
slip there costs the closure gate or the quality of the result, not a kill date.

## 5. Kill dates and what they trigger

These are the dates the plan is held to. They are backstops, not pacing: each
piece of work starts when its prerequisites are done, and the kill date is the
point past which it is declared failed.

- **2026-10-18: registration not committed.** The roadmap drops to R4. What
  still happens: the rehearsal findings and the registration draft are
  committed as the resumption design; nothing trains. Said plainly in
  STATUS.md as a schedule failure.
- **2026-11-01: registered runs not launched.** Same drop (anything later
  leaves no room for the two remaining gates). The implementation is committed
  and tested; the compute is not spent.
- **A gate takes more than seven days.** Cowork raises it in the next session
  and the steps behind it shift. There is no slack week to absorb the shift any
  more, so what absorbs it is the room left before the next kill date, and a
  stalled gate is raised as a threat to that date.

## 6. Caps and cuts

**Spend.** The program envelope is $400 (raised 2026-08-16; $215.70 spent per data/project.toml), with about $184
unspent as of 2026-09-20; A3's own $100 stop has about $56 left and A3 closes,
so its remainder returns to the program pool. Proposed cap for the successor:
**$130**, covering rehearsal (up to $10), development runs (up to $10), nine
registered 30M runs (about $110) and one re-run (about $12) with the balance as
the anomaly margin. Anything above $130 is a new ruling. If the 3.5× billing
anomaly recurs on the first pod, the seed plan drops as stated at the
registered-training step of section 4 (step 5) before the second pod launches.

**Time.** John's items above sum to roughly ten tier 2 reviewer sessions (about
an hour each), six rulings, the book edits and the launch approvals: three to
four hours a week for as long as the chain takes to reach the closure Gate A
(step 11), with the rehearsal-and-A3-closure step (step 2) and the validation
Gate B step (step 7) the heaviest. If that is not available, the tier 2 sessions
are the item to batch (two gates' packets in one sitting), never to skip, since
the protocol says both tiers run at Gate A.

**Cut or deferred to resumption (May 2027 or a pipeline break), so that nothing
competes with the critical path:**

- The ~70-hour marker-word fitted read (Gemini Q5). Deferred; not on the path to
  the metric.
- Blind-localization re-run with a new target. Deferred unless the A10
  reconciliation says the 2026-09-16 run did not discharge it, in which case it
  runs as a $0 side item and does not block the closure text.
- Causal patching on the A3 checkpoints. Folded: the patching code is written
  once, for the successor's grammar, and the A3 checkpoints are not patched
  (their grammar has no matched-role comparator and the target was never
  localized). The A3 closure text already says patching was never run.
- Option D (scaffolded name-keyed query). Deferred.
- The deliberative-gap-width pilot on frontier models, Stage 3's retained-
  independence benchmark, the explainer-derived tests and the construction
  project. Deferred, unchanged.
- The three protocol amendments (rehearsal before Gate A, reviewer-owned
  verification, strike "unlikely" from the fixed brief). Rule them at the head
  of the chain (step 1) so the successor's Gate A runs under the amended
  protocol; the rehearsal amendment is on the critical path anyway.

## 7. What this roadmap needs John to change (rulings, in order of urgency)

1. **Amend item 5 of `docs/rulings/2026-09-20-center-as-degree.md`**: the
   successor is registered now, through Gate A with both tiers, rather than
   "after the hibernation condition". Without this the roadmap cannot exist.
2. **Amend item 4 of the step 4 ruling** (localization order before the closure
   text): causal patching is not built for the A3 design; it is built once for
   the successor. The A3 closure text goes to Gate A after the two authorised $0
   runs and the A10 reconciliation, without waiting for patching.
3. **Rule Astra A10** (blind-arm status) so the closure text's preconditions are
   met at the head of the chain (step 1).
4. **Approve the $130 successor cap** within the $400 ceiling, with the seed
   fallback at the registered-training step (step 5).
5. **Accept the result definition in section 2 and the three-arm design in
   section 3 as the basis of the successor proposal** (it then goes through Gate
   C and Gate A as text; this is a go to draft, not a registration).
6. **Rule the three protocol amendments** before the successor's Gate A.
7. **Accept the two kill dates** and what they trigger.

## 8. What this roadmap does not change

The founding wager, the claim rule (never "a conscious machine"), the outside-
review protocol's gates and closure rule, the book lock, the 2026-12-21 wrap-up
start, the 2027-01-04 hibernation condition, and the public log. The public
sentence at the end of this roadmap, if R1, is: a 30-million-parameter
transformer with a causally load-bearing ownership pointer reads at degree d on
this project's integration axis, on a metric that separates a tracker built to
be separable from a system built to be entangled; if R2 or R3, the sentence is
the corresponding registered term and the degree stays unmeasured, on the record.
