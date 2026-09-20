# Outside-review protocol for Minimum Viable Mind

*Drafted 2026-09-19 (Pacific) in a Cowork session from the mobile-session
proposal of the same day ("a standing outside-review gate for MVM").
Status: IN FORCE. John ruled on the seven decisions at the end on
2026-09-19 (Pacific), all accepted as proposed, in his words: "agreed on
all". No compute or spend is implied.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30).*

---

## What already exists, so this is continuity and not a new practice

MVM has run adversarial review five times, all recorded in
`experiments/06-mvm-0a-constructed-self-index/`:

- Pass 1, 2026-08-04, on the pre-registration draft: 15 findings, 3 fatal
  (`red_team_ledger.md`, RT-01 to RT-15).
- Pass 2, 2026-08-09, on the gate-(iii) fix (same ledger, RT-16 to RT-19).
- Pass 3, 2026-09-15, on Amendment A3 before its registration commit: 13
  findings, 2 fatal (`red-team-pass-3.md`, RT-20 to RT-32).
- A4 pass 1, 2026-09-19, Claude on its own A4 proposal: 15 items
  (`a4-red-team-pass-1.md`).
- Independent A4 pass, 2026-09-19, a separate Claude Code session in its own
  worktree (`worktree-red-team-a4`), which by its own discipline did not open
  the amendment draft, the first pass, or the scoring script: 22 findings,
  labelled F1 to F22 (`red-team-a4.md`). This is the pass that stopped the
  three-seed wave.

So the proposal's premise that review "has run once" is wrong on the record.
What is true is that review has been ad hoc (fired when someone thought of
it), same-model (every pass was Claude), and has no closure rule. The third
of those is the one that has cost the most.

## What actually went wrong, read from the repo

The proposal lists two failures caught late: the registered comparison clause
was unsatisfiable from the day it was registered, and the localization probes
targeted a generator index that cannot be recovered in principle.

The first was not a detection failure. Pass 3 (2026-09-15, four days before
the registration commit) said it in so many words in RT-21: "under the unfixed
grammar the ownership-blind ceiling is 1.000, so the corrected metric has a
zero denominator, which is the arithmetic saying, correctly, that the metric
has nothing to measure." RT-21 was marked fatal and its metric fix was marked
adopted. But the fix depended on the control battery's ceiling having been
measured and attacked, and it never was: the registered text of A3 §4 said
both ceilings were "verified by the attack sweep" when only the primary's had
been (`ceiling-defect-2026-09-17.md`). The 2026-09-17 defect registration and
the 2026-09-19 "never computable" finding are the same fact landing twice.

So the missing piece is not more review before registration. It is a rule
that a fatal finding is not closed by a sentence saying it is fixed; it is
closed by a committed record that a second reader can check, and any
"verified" or "measured" claim in registered text has to point at one.

The second failure (the unrecoverable probe target) is the feasibility
question no pass was asked to ask: can the quantity the pre-statement names
be recovered at all with the stated instrument. That question goes into the
brief.

## The gates

Review fires, with a written record in the repo, at three points.

**Gate A — registration.** Every registration, amendment, threshold lock, or
pre-statement that will be read as binding, before the registration commit.
Both tiers below run. The registration commit waits on the closure rule.

**Gate B — interpretation.** An interpretation of a result before it enters
STATUS.md's current-state section or the paper draft, when it either changes
program direction or is a claim the paper will carry. Routine null entries and
ledger rows are not gated. Tier 1 runs; tier 2 runs only when the
interpretation is paper-bound.

**Gate C — rulings.** A ruling on program direction is John's call by design,
and a review of the ruling after the fact would make the reviewer a veto over
him. So the review attaches to the proposal before it reaches him: any
proposal that asks for a John-level ruling carries a tier 1 pass, filed and
linked, so he rules on text that has already been attacked. Tier 2 only if he
asks. First application: public path step 4, the 2026-10-04 control-battery
decision (repair the clause under a new amendment, or close A3 with partial
discriminators).

## Two tiers, because outside models cannot run the code

**Tier 1, the inside pass.** A fresh Claude Code session in its own worktree.
Context isolation is the non-negotiable part, and is what made the
independent A4 pass useful despite being the same model: the session gets the
packet (the target text, the registered text it must be read against, the
committed code and records) and nothing else. No chat history, no uncommitted
files from the shared checkout, no ruling annotations, and it says at the top
what it did and did not open. Every finding is labelled MEASURED (a check was
run and the output is reported) or ARGUED (reasoning a reader can dispute),
the convention the existing passes already use. This tier can run code and
compute bounds; it is the only one that can produce MEASURED findings.

**Tier 2, the outside pass.** At least two models from labs other than
Anthropic, run by John through their apps, exactly as the Belt Equation's
step-27 protocol does it (`belt-equation/docs/reviews/protocol.md`). Same
packet as tier 1 plus the tier 1 findings, so the outside reader can go
looking elsewhere. All findings are ARGUED, since these models see documents
and not a running checkout. Model, version, date and mode recorded at the top
of every filed response; responses filed verbatim and never edited.

The tier 1 pass runs first. The tier 2 packet includes its findings. Neither
tier's author writes the fix for its own finding's closure check (below).

## The brief, fixed, sent unchanged with every packet

Four parts, in this order, a table first in each, severity marked fatal,
serious, or worth-noting, and a one-paragraph kill case at the end whether or
not the reviewer thinks the target should ship.

1. **Feasibility.** For every quantity the target pre-states or thresholds:
   can it be measured at all with the stated instrument, and can the control
   or comparison condition actually reach the stated threshold? Cite the
   committed record that shows so, or say that none exists. A "verified" or
   "measured" claim in the text with no record behind it is a fatal finding
   on its own.
2. **Satisfied by the wrong thing.** Every way the clause, its baselines, or
   its threshold calibration could be satisfied by a model with none of the
   structure it claims to detect, or fitted to data the text says is excluded.
3. **No verdict.** Every way the target could fail to return any verdict on
   the runs it is written for.
4. **Over-reading.** What the result will be read as claiming beyond what it
   measures, in the paper, in STATUS.md, and in public.

Plain language throughout. Lookup allowed and flagged. Do not soften findings
to be polite; a target with nothing fatal is a possible finding, but an
unlikely one.

## The closure rule, which is the new part

Before a registration commit at Gate A:

- Every fatal finding from either tier has a closure line in the ledger, in
  the form: finding, the commit that lands the fix, and a MEASURED check by a
  session other than the one that wrote the fix, showing the fix does what
  the closure says. "Adopted" is a disposition, not a closure.
- Every sentence in the registered text that says verified, measured,
  calibrated, or attacked cites the committed record by file name, and the
  closure check confirms the record contains what the sentence says it does.
- Serious findings are closed the same way or carried as an open item named
  in the registered text, with John's ruling and reason.
- A declined finding keeps its reason on the record so the next pass can see
  it was considered.

Had this rule been in force on 2026-09-15, RT-21's closure check would have
gone looking for the control battery's attack record and found none.

## Filing

- Findings: `experiments/<experiment>/reviews/YYYY-MM-DD-<target>-<reviewer>.md`,
  verbatim, never edited after filing. Tier 1 findings continue the ledger's
  RT numbering; tier 2 findings are labelled by reviewer (for example G1 to
  Gn for Gemini) and take RT numbers only when John's ruling adopts them, so
  the two passes cannot collide.
- Rulings: one line per item in `red_team_ledger.md`, in the form used since
  2026-08-04: item, reviewer(s), John's ruling (accept, accept with change,
  decline, carry open), reason, and for fatal items the closure line.
- Packets: hand-assembled for now, with the file list at the top of the
  findings file. A packet script like the Belt Equation's
  `scripts/review_packets.py` is worth writing once the third packet exists.

## What changes from the Belt Equation's step-27 protocol

Kept as is: reviewers see everything; lookup allowed and flagged; a fixed
brief sent unchanged; John runs the outside sessions and Claude prepares and
files; verbatim filing; John rules on every item and a ruling to keep the
text over an objection is a valid outcome with its reason on record.

Changed for an empirical program:

- The unit of review is a document (a registration, an amendment, a
  pre-statement, an interpretation), not a factor packet of nodes.
- The brief asks about feasibility, wrong-thing satisfaction, no-verdict, and
  over-reading, in place of missing nodes, criteria, and numbers.
- No 0.15 threshold for what counts as a disagreement; severity (fatal,
  serious, worth-noting) does that job, as the ledger already does.
- Two tiers instead of one, because the review needs code access to produce
  MEASURED findings and outside models cannot have it.
- The closure rule, which the Belt Equation does not need because a
  probability change lands in one data file and a re-run.

## Retroactivity

The proposal asked whether Gate A applies to the control-learnability pilot.
It is moot: the pilot launched 2026-09-19 at about 20:14Z on John's verbatim
go (compute ledger row of that date), and it is unregistered by design. Its
pre-statement (`control-learnability-pilot.md`) is the kind of document Gate A
would cover in future, and its pre-stated cells were committed before the
code existed, which is the discipline the gate is meant to enforce.

## Decisions (ruled 2026-09-19, all accepted as proposed; each with confidence, whether it is standard practice, and the alternative)

1. **Adopt the three gates as scoped here** (A: every registration, both
   tiers; B: direction-changing or paper-bound interpretations only; C: review
   attached to proposals, advisory, not a gate on rulings). Confidence high on
   A, moderate on the scoping of B and C. Standard practice for A (a
   registration is a pre-print of the method). Alternative: the proposal's
   original wording, every interpretation and every ruling; costs a pass on
   routine null entries and puts a reviewer between John and his own calls.
2. **Context isolation is mandatory for tier 1; other-lab models are
   mandatory for tier 2.** Confidence high. The independent A4 pass shows
   isolation is what does the work; other labs add a different set of blind
   spots. Alternative: tier 1 only. Cheaper; every pass so far has been
   Claude, and a same-model reviewer shares the proposer's priors about what
   is measurable.
3. **The closure rule.** Confidence high; this is the finding of this draft.
   Standard in engineering review (a fix is closed by a test, not by a note).
   Alternative: keep "adopted" as the terminal state. That is the state RT-21
   was in when the unsatisfiable clause was registered.
4. **The four-part brief.** Confidence moderate on the exact wording, high on
   feasibility being part 1. Alternative: reuse the A4 brief (a to d) as
   written; it lacks the feasibility question, which is the one both late
   failures needed.
5. **Tier 2 reviewers: the same pair as the Belt Equation** (GPT-6 Astra via
   the ChatGPT app, Gemini via its app), a third on disagreement. Confidence
   moderate. Alternative: one outside model; halves John's session time,
   loses the disagreement signal.
6. **Filing under `experiments/<experiment>/reviews/` with the ledger as the
   rulings file**, this protocol at `docs/outside-review-protocol.md`,
   mirrored as a TimeAssembler project document once ruled. Confidence high;
   it is where the five existing passes already live.
7. **First application is public path step 4**: a tier 1 pass on whatever
   proposal carries the 2026-10-04 control-battery decision, then Gate A in
   full on any amendment text that comes out of it. Confidence high.
   Alternative: start with the paper draft at step 7; later, and step 7's
   outside human reader is a different check (see
   `docs/outside-reader-shortlist-2026-09-19.md`), not a substitute.
