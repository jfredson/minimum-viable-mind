2026-09-19 (Pacific), "agreed on all". The three decisions the rulings rest
on: (1) STATUS.md carries the reviewer's replacement paragraph, with the
addendum's causal-patching clause, in place of any claim that the linear
read is closed; (2) the line is not retired until a fitted linear classifier
has been run on the four-answer register-index target at all eleven
positions, $0, local, method committed before output; (3) PR 5 merged as a
merge commit.*

| ID | Finding | Severity | Ruling | Reason / closure |
|---|---|---|---|---|
| RT-33 | The difference-of-averages read is about half as sensitive as a fitted linear classifier, measured on these checkpoints in `probe_target_diagnostic_a3_*.json` and reported in no findings file | fatal | ACCEPTED | Reproduced independently from the seed 1 record (classifier 0.48–0.535 against the read's 0.25–0.2675 at the marker position). **Closure:** decision 1 lands the corrected wording in STATUS.md citing the record; decision 2 runs the fitted read at all eleven positions. Closure is checked by the tier 1 pass on that run's findings, not by the session that writes them. |
| RT-34 | The read cannot see a linear signal in a quiet direction, at the stack's own measured geometry (ten of 448 directions carry ~99% of variation) | serious | ACCEPTED | This is the mechanism behind RT-33 and the reason the fitted run is needed. Carried into that run's method. |
| RT-35 | The register-index arm has no positive control of its own; "demonstrably carries it somewhere" rests on the marker-word control | serious | ACCEPTED WITH CHANGE | The "demonstrably carries" sentence does not enter STATUS.md. The fitted run's method must state what its positive control for the register index is, or say it has none. |
| RT-36 | The positive control recovers the input token on only about one episode in eight on seeds 1 and 2, and that caveat drifted to "holds without qualification" across four findings files | serious | ACCEPTED | STATUS.md reinstates the caveat: the null is strong on the pilot and weaker on seeds 1 and 2. The gap stays an open item. |
| RT-37 | The smallest detectable signal is nowhere on the record (computed: identity legible in 1.3% of episodes for the marker word, 3.9% for the register index) | worth-noting | ACCEPTED | A point in the result's favour and it goes into STATUS.md. |
| RT-38 | Two pre-stated degeneracy preconditions fired on the pilot and the findings do not say so (family 268, bar ~3.55) | worth-noting | ACCEPTED | Nothing material changes. Recorded here so that pre-stated preconditions are seen to be honoured. |
| RT-39 | All 270 tests share five fold splits and five shuffle sets (seeded by layer alone) | worth-noting | ACCEPTED, CARRIED OPEN | Moot for this result. The fitted run seeds folds and shuffles per test. |
| RT-40 | The state-space geometry is measured at one position of eleven | worth-noting | ACCEPTED, CARRIED OPEN | Measured at the other positions in the fitted run if cheap; otherwise stated as unknown. |
| RT-41 | The two cells are exhaustive, so a partial pattern lands in CARRIED NOWHERE | none | NO ACTION | The reviewer checked and found the method names the risk and reports the sub-pattern. |
| RT-42 | The negative control at position 1 is read as licensing the other 270 numbers; the inference only runs one way, and position 1 is the weakest place to look for a leak | worth-noting | ACCEPTED | STATUS.md says the negative control showed no leak at position 1 and no more than that. |
| RT-43 | The sweep's method and findings files are headed 2026-09-20 but were committed 2026-09-19 Pacific | worth-noting | ACCEPTED, NOTED ONLY | Committed method files are not edited after the run. This line is the correction: the dates are UTC; the commit order is what matters and is correct. |
| RT-44 | "Closing the linear-read line" is not supported: one linear read found nothing, the fitted read was never tried at nine of eleven positions | fatal | ACCEPTED | Same closure as RT-33. The claim does not enter STATUS.md or the paper. |
| RT-45 | "The instrument demonstrably works" claims general linear-probe sensitivity; the control only shows the read recovers a token that is present | serious | ACCEPTED | Wording handled by decision 1. |
| RT-46 | "The rest of the episode is empty too" over-reads eleven positions of a seventy-one-token episode under one read | serious | ACCEPTED | Wording handled by decision 1. |
| RT-47 | "This was the last run in this line" — the cheapest follow-up (fitted classifier, four-answer target, all positions) has not been run and was listed as open item 5 in the first sweep's own findings | serious | ACCEPTED | Closed by decision 2: the line is retired, if at all, after that run. |
| RT-48 | The powered runs are the first to use the registered probe target (the marker word); every earlier probe was off-spec against the registration | worth-noting (credit) | ACCEPTED | Recorded as credit. STATUS.md says the registered target was used. |
| RT-49 | The registration (Amendment A3 §3.2) requires probe AND causal patching with a convergence rule; patching has never been run, so a probe-only null is "not testable (localization)" under the registered text | serious | ACCEPTED, CARRIED OPEN | The patching clause goes into STATUS.md. Whether patching runs before A3 closes is a direction question and is added to the 2026-10-04 control-battery decision (public path step 4) as a second item. |
| RT-50 | The registration reads "known load-bearing, instruments cannot find it" as instrument failure; the interpretation reads the same pattern as absence without saying so | serious | ACCEPTED | STATUS.md must not read the null as absence. Under the registered text it is instrument failure until patching has run. |
| RT-51 | The reviewer skipped two listed sources, disclosed it, and filed an addendum rather than editing the filed review | worth-noting | ACCEPTED | The first exercise of the immutable-filing rule, and the right behaviour under it. |

# Gate B review of the control-learnability pilot (2026-09-20) — rulings on RT-52 to RT-69

*The second review filed under `docs/outside-review-protocol.md` (the fitted-read
review below filed four minutes later and is numbered after it). Target: the
interpretation "the control battery does not learn when properly supervised;
supervision is not the binding constraint", from
`control-learnability-pilot-findings.md` (commit `062636e`). Reviewer: a fresh
Claude Code session in its own worktree, given only the packet
(`reviews/2026-09-20-control-learnability-packet.md`). Findings filed verbatim
in `reviews/2026-09-20-control-learnability-claude-worktree.md` (PR 7).
Rulings drafted by Cowork, ruled by John 2026-09-20 (Pacific), "agreed on all".
Settled: STATUS.md carries the reviewer's part 4 paragraph; the sentence
"supervision is not the binding constraint" does not enter STATUS.md, the
step 4 proposal, or the paper; the verdict DID NOT LEARN stands with its scope
cut to what was run, reweighting the rows the battery already had.*

| ID | Finding | Severity | Ruling | Reason / closure |
|---|---|---|---|---|
| RT-52 | 0.3227 is a name-blind solver's score, not an attacked ceiling (the 2026-09-17 defect), but it is still the right number for the pre-stated cell | serious | ACCEPTED | The cell was pre-stated against it and is scored against it. The ceiling precondition of 2026-09-17 still binds any option that keeps this battery (RT-69). |
| RT-53 | The endpoint record states the floor rule the programme corrected on 2026-09-16 (control needs baseline minus ceiling of at least 0.10, so 0.4227, not 0.3227) | serious | ACCEPTED | The endpoint script's text is corrected in the next commit that touches it; the 0.4227 bar is the stated reason in the step 4 proposal. |
| RT-54 | The 0.60 boundary is reachable in principle; the battery's true limit is near 1.0 | worth-noting | ACCEPTED | Recorded. |
| RT-55 | The supervision was delivered exactly as claimed (four times per-row weight, one third to two thirds of the query gradient), verified from the code and the step-500 loss check; the findings cite nothing for it | serious | ACCEPTED | STATUS.md cites the code (`ee7fc91`) and the ledger's loss check. |
| RT-56 | The training log and trajectory record are not in the repository | serious | ACCEPTED | **Closure:** commit both beside the endpoint record before the step 4 proposal is filed. |
| RT-57 | The intervention did three things: raised the control's share, tripled the whole query loss against the action term, and changed what the gradient clip does | serious | ACCEPTED | STATUS.md describes the intervention as what it was. Any future reweighting run holds the total query weight fixed or says why not. |
| RT-58 | The control rows are the first half of every batch, a fixed positional split never checked for bias | serious | ACCEPTED, CARRIED OPEN | **Closure:** a $0 local check of episode order against the split, filed as a findings note. |
| RT-59 | "Exactly one scored token per row" is asserted in a comment and never tested | worth-noting | ACCEPTED, CARRIED OPEN | **Closure:** one-line self-test, $0. |
| RT-60 | The evaluation can see what was learned | clean | NO ACTION | Checked clean by the reviewer. |
| RT-61 | The battery converged on the name-blind solver (95% of the way from chance 0.125 to 0.3227) and learned none of the name-keyed lookup | serious | ACCEPTED | This is the sentence STATUS.md leads with after the number. |
| RT-62 | The matched-seed comparison the design was built around is missing; against it the control moved +0.0248 (SE 0.0157), so "bought nothing" is false | **fatal** | ACCEPTED | **Closure:** STATUS.md quotes the matched comparison (0.3125 against 0.2877) and does not say "bought nothing". Checked by the tier 1 pass on the step 4 proposal. |
| RT-63 | "0.42 sd" is one draw's spread, not the uncertainty of the scored mean; a PARTIAL rerun is less likely than stated | worth-noting | ACCEPTED | And moot: below 0.4227 PARTIAL changes nothing for A3 (RT-53). |
| RT-64 | One training seed; the design only had power against a large effect | serious | ACCEPTED | STATUS.md says one seed, one dose. |
| RT-65 | The control is flat at the end and the budget was not short-changed | clean | NO ACTION | Checked clean. |
| RT-66 | The one trajectory reading in the review set also runs the intervention's way | worth-noting | ACCEPTED | Recorded. |
| RT-67 | "Supervision is not the binding constraint" will be read as ruling out supervision; one dose of one form was tested | serious | ACCEPTED | The sentence is withdrawn. STATUS.md says "reweighting the rows it already had is not what this battery is missing". |
| RT-68 | Step 4 should narrow to option D or close A3, but for the 0.4227 reason, and option D is itself a new training signal, so the findings' stated reason argues against the option it points to | serious | ACCEPTED | The step 4 proposal states the 0.4227 reason and frames option D as a different, easier question, not more supervision. |
| RT-69 | Any step 4 option that keeps this battery inherits the 2026-09-17 ceiling precondition | worth-noting | ACCEPTED | Carried explicitly in the step 4 proposal. |

# Gate B review of the fitted linear read (2026-09-20) — rulings on RT-70 to RT-93 (filed as RT-52 to RT-75 in the review file)

*The second review under `docs/outside-review-protocol.md`. Target: the
interpretation of the fitted eleven-position sweep (FOUND NOWHERE, nothing on
any checkpoint), which was decision 2 of the 2026-09-19 review of the
linear-read closure. Reviewer: a fresh Claude Code session in its own worktree,
given only the packet (`reviews/2026-09-20-fitted-read-packet.md`), reading at
the merge commit `a846b0c`. Findings filed verbatim in
`reviews/2026-09-20-fitted-read-claude-worktree.md`. The two 2026-09-20 reviews ran in parallel and both
numbered from RT-52. The control-learnability review filed first (09:44 Pacific
against 09:48) and keeps RT-52 to RT-69; this block's findings are ledger
numbers RT-70 to RT-93, which are the review file's RT-52 to RT-75 plus 18. The
review file is not edited, per the filing rule.*

**Rulings below were drafted by the reviewer and RULED by John on 2026-09-20
(Pacific), all accepted as drafted, on Cowork's recommendation ("agreed on
all").** Settled: (1) STATUS.md carries the part 4 paragraph; (2) the
sensitivity figure is corrected by a dated note beside the findings; (3) the
other-agent index (RT-82, review RT-64) and the standardised refit (RT-76,
review RT-58) are authorised, the marker-word fitted read (RT-89, review RT-71)
is deferred, and the line is parked under the registered term *not testable
(localization)* pending causal patching. The three things a ruling has to settle: (1)
whether the replacement paragraph in part 4 of the review is what STATUS.md
carries; (2) whether the sensitivity figure is corrected from one episode in
twenty-seven to one in eleven wherever it has been written; (3) which of the
three cheap follow-up runs, if any, are authorised — the other-agent index
(`RT-82`), the marker-word target under the fitted read (`RT-89`), and the
standardised refit (`RT-76`).

**Verdict of the review in one line.** The cell is right, every published number
reproduces from the machine records, and all nineteen rulings from the previous
review were honoured. Two things are wrong with the interpretation: the run is
about two and a half times less sensitive than the findings claim, and the
sentence "no linear read finds own-agent identity at the nine testable
positions" cannot be said because the registered target was never read by this
instrument at any of those nine positions.

| ID | Finding | Severity | Ruling | Reason / closure |
|---|---|---|---|---|
| RT-70 | All six of the brief's requirements are met and each has a record behind it; the instrument check is locked at both ends, so neither the code's pre-stated table nor the committed record can be edited to fit the other, and a mismatch stops the run rather than being reported afterwards | worth-noting (credit) | ACCEPT AS CREDIT | The brief said a requirement claimed met with no record is fatal. There are none. Verified from the machine records and from the code, not from the method file's description of itself. |
| RT-71 | The findings' "below 1e-15" for the instrument check is not on the record: the code rounds the largest difference to six decimal places, so the record's finest statement is "below five parts in ten million". Two checkpoints reproduced bit-exactly and the pilot did not, which the findings' table flattens | worth-noting | ACCEPT | Nothing turns on it — the pre-stated tolerance was one episode in 400 and none was used. Corrected because a figure stated as measured was inferred. |
| RT-72 | Both corrections the findings make to their own committed method file are accurate: the pilot converges on all twenty anchor folds (158–933 passes) while seeds 1 and 2 cap on 9 of 20 and 17 of 20; and the run's three elapsed times sum to 10.76 hours against an estimate of six and a half | worth-noting (credit) | ACCEPT AS CREDIT | Verified against the records. Correcting a committed method file in the findings rather than editing it is what the ruling on committed files (`RT-43`) asks for, and this is its first exercise. |
| RT-73 | The run used 200 shuffled-label draws where the previous review's first recommendation was 1,000. Disclosed in advance with the cost arithmetic, but it is why the bar rests on a normal approximation rather than on counting: zero of 200 establishes only 2.578 standard deviations against a bar of 3.38 | worth-noting | ACCEPT, CARRIED OPEN | Not a departure from the brief, which did not restate the 1,000. Raise the draws on any single cell that ever needs to be believed. |
| RT-74 | The run's reach is a signal legible in about one episode in eleven, not one in twenty-seven. The detectable-share measure assumes a perfectly legible episode scores 1.0; the only ceiling this run measures is 0.539–0.567, at position 6. Recalibrated: 8.6–9.4 per cent, not 3.65 | serious | ACCEPT | The figure the findings lead with overstates the run's reach by about two and a half times. It must not enter STATUS.md in the one-in-twenty-seven form. The measure came from the previous review (`RT-37`), so the correction applies to both runs. |
| RT-75 | "It is consistently lowest at position 6" is false on seed 1, where the control position is the fourth most concentrated of eleven (0.9791–0.9820 against a testable low of 0.9430), and a photo-finish on seed 2 (0.8774 against 0.8781). It holds only on the pilot. "About 99 per cent holds at the other positions" is also wrong: seed 2's testable median is 0.942 | serious | ACCEPT | The geometry is the mechanism behind the quiet-direction problem (`RT-34`) and the only evidence about whether the control tests the read in the same regime as the tested positions. The records carry a real per-checkpoint distinction that the findings replace with one claim true of one checkpoint in three. |
| RT-76 | Leaving the 448 directions unscaled under a squared penalty at strength 1.0 charges a quiet direction the square of how quiet it is, so the instrument is by construction worst-placed against the hypothesis under test — a self-index that is real, linear and quiet | serious | ACCEPT, CARRIED OPEN | The method names the cost and declines to fix it, reasonably, because the run's credibility rested on reproducing fifteen recorded numbers. It should not be declined twice. A standardised refit at the nine positions costs the same eleven processor-hours and needs its own anchor. |
| RT-77 | The family bar treats 135 tests as independent. All three checkpoints read the same 4,000 episodes at content seed 20260917, and five layers read one residual stream. The correction stays valid but buys less power than its arithmetic implies: at 45 effective tests the bar is 3.06, at 9 it is 2.54, and the run's one MARGINAL at +3.34 clears both | serious | ACCEPT | Not an argument that the bar should have been lower — it was pre-stated and conservative, which is the right instinct. It is an argument that 3.38 is the strict end of a defensible range, not a neutral technical choice, and that for a run asking "is anything there" over-correcting is the direction that manufactures a null. |
| RT-78 | Fold size and classifier capacity are cleared. At 4,000 episodes, four folds, 448 directions and a smallest answer class of 964, the fit is in a comfortable regime and the records show no sign of capacity failure. The 400-episode anchor is the overparameterized configuration, and no sweep cell rests on it | worth-noting | ACCEPT | Two of the four mechanisms the packet names are eliminated. Regularisation (`RT-76`) is not, and the two untested positions are the two controls, which is correct design and leaves the episode's other sixty tokens unexamined (`RT-46`, unchanged). |
| RT-79 | The majority-class requirement, announced as a deliberate tightening, never binds: the rate is 0.2582 on every checkpoint and the accuracy needed at the family bar is 0.2774–0.2778 on all 135 tests | worth-noting | ACCEPT | Harmless and would bind under a looser bar. A pre-stated safeguard that cannot fire should be reported as inert, the way the degeneracy rule correctly was. |
