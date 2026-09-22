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
4, week 40) and fixed in the registration text. This document does not invent
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

## 4. Week-by-week critical path

Thirteen weeks from 2026-09-21 to 2026-12-20. Wrap-up starts 2026-12-21 (ruled);
nothing launches after that. Dates are Pacific. "CC" is a Claude Code session;
"Cowork" is this assistant; "John" is a ruling, a reviewer session he runs by
hand, or an edit in another repo.

| Week | Dates | Critical path | In parallel | John's items |
|---|---|---|---|---|
| 39 | 09-21 to 09-27 | Rule the section 7 changes (successor registers now; patching code folds into the successor). Draft successor proposal v1 (CC): task grammar, three arms, metric spec, rehearsal plan, spend estimate. | Two authorised $0 runs finish (other-agent index control, standardised refit). Blind-arm status reconciled (Astra A10). A3 closure text: tier 1 review. | Book lock edits (ch05 degree reading) in calibration-problem. Rule A10. Site secrets. |
| 40 | 09-28 to 10-04 | Gate C tier 1 on proposal v1. **Measurement rehearsal** (CC, ~$0 to $10): tiny models, show the three arms are constructible, the pointer in T is patchable, the joint patch in C works, the metric returns positive, negative and invalid values on toy cases, throughput of the new grammar measured. | A3 closure text: tier 2 sessions, John rules, lands (Gate A). | **Book lock 09-30.** Run two tier 2 sessions for A3 closure. Rule on it. |
| 41 | 10-05 to 10-11 | Rehearsal findings fix the bars. Registration text final (v2). Gate A: tier 1, then tier 2. **Registration commit target: 2026-10-11.** | Generator, T and C architectures, patching code implemented against the rehearsal (CC). | Run two tier 2 sessions on the registration. Rule. |
| 42 | 10-12 to 10-18 | Implementation frozen; unit tests; the RT-58 even-split rule and the one-scored-token self-test carried over. Development runs at 10M (~$10). | Compute ledger rows opened with estimates. | **Kill date 1: registration committed by 10-18** or the roadmap drops to R4 and says so. |
| 43 | 10-19 to 10-25 | **Registered training launched**: three arms × three seeds at 30M, ~$110 at the ledger's $12 per run (the 3.5× RunPod anomaly of 2026-08-08 is the risk; if it recurs, seeds drop to two on T and C, three on F). Eligibility gate evaluated as runs land. | Actor-representation nomination on development episodes begins as F checkpoints arrive. | Approve launch (spend gate). |
| 44 | 10-26 to 11-01 | Nomination frozen and committed. Patching on fresh episodes, all arms. Metric computed on T and C: the validation result. | One permitted re-run if an arm failed eligibility (~$12). | None unless a re-run needs a go. **Kill date 2: registered runs launched by 11-01** or R4. |
| 45 | 11-02 to 11-08 | Validation findings written. **Gate B** (tier 1, tier 2). John rules: R1 path (read F), or R2/R3 closure. | Site and `data/project.toml` updated with the validation state. | Run two tier 2 sessions. Rule.   |
| 46 | 11-09 to 11-15 | R1: read arm F on the frozen procedure, confirmation seeds. R2/R3: draft closure text and the resumption design. | Buffer for patching-code defects found at Gate B. | None. |
| 47 | 11-16 to 11-22 | Findings document for the reading (or the null). Gate B tier 1. | Buffer. | Start tier 2 sessions if tier 1 is clean. |
| 48 | 11-23 to 11-29 | Gate B tier 2, ruling. Closure text drafted (registered text). | Thanksgiving week; expect John's time to be short. | Rule. |
| 49 | 11-30 to 12-06 | **Gate A on the closure text** (tier 1, tier 2). Ruling. Closure lands in the successor's registration file. | State-of-the-program write-up drafted (Cowork). | Run two tier 2 sessions. Rule. |
| 50 | 12-07 to 12-13 | STATUS.md, `data/project.toml`, site, ledger closed with actual-after rows. Write-up to the outside human reader (shortlist doc). | `RESUME.md` drafted. | Choose and contact the outside reader. |
| 51 | 12-14 to 12-20 | Slack week. Absorbs one slipped gate. | Explainer refresh if time. | None. |
| 52+ | 12-21 to 01-03 | **Wrap-up** (ruled): hibernation condition per the program roadmap. | | Final ruling that the hibernation condition is met. |

Gate count on the critical path: four (A3 closure Gate A, registration Gate A,
validation Gate B, closure Gate A), plus one Gate B on the reading if R1. Each
costs one tier 1 worktree session and two tier 2 sessions John runs by hand,
then a ruling. At the observed pace (the 2026-09-20 reviews turned around
inside a day when John was available) a gate costs two to four days; at
Thanksgiving pace it costs a week. The plan assumes three days and has week 51
as the only slack, which is why the two kill dates exist.

## 5. Kill dates and what they trigger

- **2026-10-18: registration not committed.** The roadmap drops to R4. What
  still happens: the rehearsal findings and the registration draft are
  committed as the resumption design; nothing trains. Said plainly in
  STATUS.md as a schedule failure.
- **2026-11-01: registered runs not launched.** Same drop (a week after the planned launch; anything later leaves no room for the two remaining gates). The implementation
  is committed and tested; the compute is not spent.
- **A gate takes more than seven days.** Cowork raises it in the next session
  and the next-week items shift, eating week 51 first.

## 6. Caps and cuts

**Spend.** The program envelope is $400 (raised 2026-08-16; $215.70 spent per data/project.toml), with about $184
unspent as of 2026-09-20; A3's own $100 stop has about $56 left and A3 closes,
so its remainder returns to the program pool. Proposed cap for the successor:
**$130**, covering rehearsal (up to $10), development runs (up to $10), nine
registered 30M runs (about $110) and one re-run (about $12) with the balance as
the anomaly margin. Anything above $130 is a new ruling. If the 3.5× billing
anomaly recurs on the first pod, the seed plan drops as stated in week 43
before the second pod launches.

**Time.** John's items above sum to roughly ten tier 2 reviewer sessions (about
an hour each), six rulings, the book edits and the launch approvals: three to
four hours a week through week 49, with weeks 40 and 45 heavier. If that is not
available, the tier 2 sessions are the item to batch (two gates' packets in one
sitting), never to skip, since the protocol says both tiers run at Gate A.

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
  verification, strike "unlikely" from the fixed brief). Rule them in week 39
  so the successor's Gate A runs under the amended protocol; the rehearsal
  amendment is on the critical path anyway.

## 7. What this roadmap needs John to change (rulings, in order of urgency)

1. **Amend item 5 of `docs/rulings/2026-09-20-center-as-degree.md`**: the
   successor is registered now, through Gate A with both tiers, rather than
   "after the hibernation condition". Without this the roadmap cannot exist.
2. **Amend item 4 of the step 4 ruling** (localization order before the closure
   text): causal patching is not built for the A3 design; it is built once for
   the successor. The A3 closure text goes to Gate A after the two authorised $0
   runs and the A10 reconciliation, without waiting for patching.
3. **Rule Astra A10** (blind-arm status) so the closure text's preconditions are
   met in week 39.
4. **Approve the $130 successor cap** within the $400 ceiling, with the seed
   fallback in week 43.
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
