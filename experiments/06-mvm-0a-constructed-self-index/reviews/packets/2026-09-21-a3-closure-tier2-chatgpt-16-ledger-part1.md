# Review packet - the closure text of Amendment A3 (Minimum Viable Mind) - file 16 of 22: The red team ledger, part 1 of 3

*This is file 16 of 22 of one review packet, pasted into a single
conversation. It contains the red team ledger - every row and range the text
under review cites (part 1 of 3). Reply with one short line saying you have
it, and wait for the rest: the brief you are answering is in file 1, and your
review comes only after file 22 arrives. If this file looks cut short, say so
now.*

---

===== RECORD 20 of 23, part 1 of 3 - the red team ledger - every row and range the text under review cites - EXCERPT: experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md =====

*Source note: excerpted from `experiments/06-mvm-0a-constructed-self-
index/red_team_ledger.md` (122,361 characters in full), which records every
adversarial pass the program has run since 2026-08-04 and the ruling on every
finding. Reproduced here: two review sections whole and three individual rows
from two others - that is, every row and every range the text under review
cites. The rows in between, and the four earlier reviews, are left out.
Nothing is edited, softened or reordered.*

*This part is the reviews of the fitted linear read and of the step 4
proposal. The other parts of this record are in file 17 and file 18.*

**This is an excerpt, not a whole file.** The source is
`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`, about 123,000
characters, which records every adversarial pass the programme has run since
2026-08-04 and John's ruling on every finding. It is too long to paste. What
follows is every part of it the text under review cites, quoted unedited and in
the ledger's own order:

- the review of the fitted linear read of 2026-09-20, with the row on the
  deferred marker-word read (`RT-89`), which the text cites twice — for the
  price of about seventy processor-hours and for the fact that the run was
  dropped before it happened rather than because of anything it found;
- the review of the step 4 proposal of 2026-09-20, with the row ruling that
  causal patching is new code rather than existing machinery (`RT-96`) and the
  row on the count of registered discriminators that have fired (`RT-114`),
  which the text cites for the mid-episode re-indexing probe never having run;
- the whole review of the two follow-up localization runs of 2026-09-21, which
  is the range the text cites as "ledger RT-120 to RT-142" and which contains
  the row on the margin of 1.94 episodes in four thousand (`RT-128`);
- the whole tier 1 review of this closure text of 2026-09-21, which is the
  range the text's preamble cites as "ledger RT-143 to RT-171" and which
  contains the row on the citation pointing at an uncommitted ruling
  (`RT-145`), the finding that stopped the previous version.

Rows in between, and the four earlier reviews, are not reproduced. Nothing has
been edited, softened or reordered. Where a row refers to another row by number
and that row is not here, the number is left as the ledger has it.

*Excerpt 1 of 4 — the review of the fitted linear read (2026-09-20). The section as the ledger has it, then the one row the closure text cites, the deferred marker-word read. Rows RT-70 to RT-88 and RT-90 to RT-93 are not reproduced.*

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
| RT-89 | "No linear read finds own-agent identity at the nine testable positions" is **not supportable**. The registered target is the model's own marker word (Amendment A3 §3.2; `RT-48`). This run did not read it — the marker-word target was priced at about 70 processor-hours against 11 and dropped before the run, openly. So at the nine positions the registered target has only ever been read by the difference-of-averages read, which this very run measures as recovering 5.5 to 18.7 times less lift than a fitted classifier at position 6 | fatal to that sentence | ACCEPT | The same error the previous review called fatal (`RT-33`, `RT-44`), moved from one target to another. What **is** supportable: a fitted classifier does not find the **register index** at those positions, and a difference of averages finds neither target. Decision 2 of the 2026-09-19 rulings is satisfied exactly as worded — a necessary condition for retiring the line, not a sufficient one — and the findings never claim otherwise. |

*Excerpt 2 of 4 — the review of the step 4 proposal (2026-09-20). The section as the ledger has it, then the two rows the closure text cites: causal patching as new code, and the count of registered discriminators that have fired. The other rows of that review are not reproduced.*

# Gate C review of the step 4 proposal (2026-09-20) — RT-94 to RT-117, RULED 2026-09-20

*The third review filed under `docs/outside-review-protocol.md`, and the first
under Gate C: a proposal asking for a John-level ruling gets a tier 1 pass
before it reaches him, so he rules on text that has already been attacked.
Target: `docs/step4-control-battery-proposal-2026-09-20.md` in full, whose
recommendation is to close Amendment A3 with partial discriminators, run causal
patching on the existing checkpoints before closure, and defer the grammar
redesign to a successor experiment after public release. Reviewer: a fresh
Claude Code session in its own worktree, given only the packet
(`reviews/2026-09-20-step4-proposal-packet.md`), reading at commit `1f9d2af`.
Findings filed verbatim in
`reviews/2026-09-20-step4-proposal-claude-worktree.md` and not edited
afterwards.*

***Status: RULED. John ruled on 2026-09-20 (Pacific), on Cowork's five
recommendations, "agreed on all": every disposition below is accepted as the
reviewer drafted it. Version 1 of the proposal stays on disk unedited; version
2 (`docs/step4-control-battery-proposal-2026-09-20-v2.md`) carries the
corrections and is the proposal ruled on. The five rulings: (1) close
Amendment A3 (option A); the grammar redesign (option D) is a successor
experiment after public release. (2) Localization order: the registered
blind-localization arm (roadmap step 3, 2026-09-27) first, then the
other-agent index control and the standardised refit, then causal patching
designed as new code with its target and null written before it runs, each
through Gate B. (3) The pre-registered loss condition ("no non-self cross-turn
control can be built that is state-requiring at ceiling") HAS FIRED; the
registered word for the outcome is *not testable*, and the closure text uses
it. (4) Claim scope: "a structural signature of ownership-specific learning"
is struck for A3; what A3 supports is that the ownership input is
load-bearing for the primary battery on three seeds and the matched contrast
could not be run; roadmap step 8's "structural signature of self-indexing"
holds only if a localized result exists before the paper draft. (5)
Housekeeping: the pilot's training log and trajectory are committed (the
"before the proposal is filed" deadline on RT-56, the missing-log finding, was
missed and is recorded here as missed); the two open $0 checks (RT-58, the
fixed batch-split bias check; RT-59, the one-scored-token self-test) run;
"partial discriminators" is not used; the closure text goes through Gate A.***

**The three things a ruling has to settle.** (1) Option A or option D — the
review supports A and does not dent the case for it. (2) Whether the operative
instruction stays "run causal patching before closure", which the review finds
unsupported on three counts: no patching code exists for this design
(`RT-96`), there is no localized subspace for it to transplant (`RT-103`), and
it can reach neither of the two outcomes the proposal promises (`RT-102`). (3)
What the paper is allowed to claim after a close, given that "a structural
signature of ownership-specific learning" is the reserved claim the
input-channel lesion cannot support (`RT-113`) — which also puts the approved
roadmap's step 8 claim scope back in front of him.

**Verdict of the review in one line.** The proposal reads the record accurately
and reaches the right destination by a route that does not exist: every number
reproduces, every ruling aimed at it was carried, the case for closing
Amendment A3 is sound, and the one action it asks to be authorised has no code,
no target, and no reachable outcome.

**Two fatal findings, one fatal to a sentence.** `RT-96` (patching is not free,
local and already built), `RT-102` (neither promised outcome is reachable), and
`RT-113` (the paper claim the registration reserves).

| ID | Finding | Severity | Ruling (accepted as drafted, 2026-09-20) | Reason / closure |
|---|---|---|---|---|
| RT-96 | Causal patching is **not** "local and $0 with existing code". This experiment's source folder holds no patching script; the only patching code in the repository is Experiment 1's, written for a different model, vocabulary and grammar, which section 3.2 says is reused only "where it transfers" — and whether it transfers has never been asked. The warrant the proposal offers, "the lesion machinery exists", is removal machinery for a transplant operation | **fatal** | ACCEPT | Checked by listing file names only, disclosed in the review. Writing the patching path is ordinary work, perhaps a day; it is still new code on a registered instrument, and it was put to John as a free item already built. The standing substrate rule applies: nothing is named in a clause before a dry run shows it loads and scores on this design's batteries. |
| RT-114 | "Partial discriminators" reads as "some discriminators fired". None has: the matched other-agent lesion has never run, the swap probe is patching and has never run, the mid-episode re-indexing probe has never run, the random matched subspaces are a null rather than a discriminator, and the register lesions are registered as a free reference. The count of registered discriminators bearing on the A3 claim is zero | serious | ACCEPT | The body of option A describes the three things that did survive accurately. It is the label that over-claims, and the label is what survives into a summary table — `F9` arriving again under a different name. |


===== END OF RECORD 20, part 1 =====
