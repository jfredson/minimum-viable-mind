# Review packet - the registration text of the successor experiment (Minimum Viable Mind), Gate A, outside pass

## What you are looking at, from a standing start

**The program.** Minimum Viable Mind is a small independent research program,
run by one person on a budget of a few hundred dollars. It trains small language
models from scratch on tasks built for one question, and writes down in advance
what would count as a result and what would count as a failure. That
written-in-advance document is called a *registration*. Once committed it is
never edited; a change is a numbered amendment, committed before anything runs.
It is the discipline a clinical trial uses when it registers its endpoints
before it enrols anyone.

**The text under review** is version 4 of the proposal for the "successor
experiment" (record 4 below, about 290,000 characters). In its own words
(section 0): the experiment builds systems whose degree of entanglement is fixed
by construction - one where "which agent am I" sits in a slot that can be
swapped on its own, one where it is stirred into everything, one that mixes the
two by item - plus one ordinary freely trained system, and asks whether a
transplant-based measure can tell the built systems apart. If it can, the freely
trained system gets a reading. You are reviewing it **as registration text**:
once this review closes, it becomes the binding registration, and the runs it
describes (about $108 of rented compute) are launched against it.

**What the registration will actually say.** Version 4 is not quite the final
wording. Several rulings and two checks made after it was written say what must
be changed in it before it is committed (records 6 to 15). Read version 4
together with them. Where version 4 conflicts with a ruling, or a ruled change
cannot be written in as described, that is in scope.

**Version 4's opening says it "cannot go to the registration review yet"** and
lists three things in front of it: a check of version 4 by another session, a
run of an ordinary competing solver, and John opening the review. All three are
done: the check is record 14, the solver run is record 21 with its check in
record 15, and John opened this review on 2026-10-04. That opening paragraph is
history, not a live condition.

**Who has already looked.** An inside reviewer - a separate Claude session with
code access, which could run checks - reviewed version 4 first. Its findings are
record 5. You are given them so you can look elsewhere: you are not asked to
re-derive them, and you may disagree with them. Any fatal finding in them is
**not yet fixed** in the text you are shown: fixes are written only after both
tiers report and John rules, so you are reading the text as it stood when the
inside review ran. The inside reviewer's findings
are labelled MEASURED (a check was run and the output reported) or ARGUED
(reasoning). Yours will all be ARGUED, because you see documents and not the
running code, and that is expected.

**What you are not shown.** Version 4 cites many more files than any reader can
be handed in one sitting (code, output files, older reviews and rulings). The
records here are the text, the inside findings, every ruling that changes the
text, the two checks of it, and the run records its numbers come from. The
other files it cites are listed at the end of this note. If a finding of yours
turns on one of them, say which, and say what you would need it to contain:
that is a useful finding, not a failure of the review.

**How the material is marked.** Every record opens with a line beginning
`===== RECORD` that names it, says whether it is a complete file or whole
sections of one, and gives its path in the repository, and closes with a line
beginning `===== END OF RECORD`. Cite records by that path, and version 4 by its
section numbers.

**How to answer.** Answer the brief (record 1) in its four parts, a table first
in each, severity marked fatal, serious or worth-noting, and a one-paragraph
kill case at the end whether or not you think the text should be registered.
Plain language. Looking things up is allowed; say when you did. Do not soften
findings to be polite, and do not manufacture severity to look thorough. A
review that finds nothing fatal is a valid result, reported as what was checked
and what held.

**The records in this packet, in order.**

1. THE BRIEF - the questions you are answering (fixed protocol text, sent unchanged to every reviewer) - `docs/outside-review-protocol.md` (whole sections)
2. the closure rule this text is being reviewed under - `docs/outside-review-protocol.md` (whole sections)
3. the rule that a full measurement rehearsal comes before any registration review - `docs/outside-review-protocol.md` (whole sections)
4. THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete)
5. the inside reviewer's findings on version 4 (Gate A, tier 1) - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md` (complete)
6. John's rulings of 2026-10-03 on the review of version 3 (binding on version 4) - `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` (complete)
7. John's three rulings of 2026-10-03 after the controls re-run - `docs/rulings/2026-10-03-controls-rerun-rulings.md` (complete)
8. John's evening ruling of 2026-10-03: the fifth outcome and the figure printed both ways - `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md` (complete)
9. first record of John's ruling on version 4's seven questions - `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md` (complete)
10. second record of the same ruling, which stands where the two differ - `docs/rulings/2026-10-03-version-4-questions-rulings.md` (complete)
11. John's ruling on which of the two records stands - `docs/rulings/2026-10-03-seven-questions-reconciliation.md` (complete)
12. John's ruling on the two questions raised by the check of version 4 - `docs/rulings/2026-10-03-version-4-check-questions-rulings.md` (complete)
13. John's ruling of 2026-10-04 on seven questions from the competing-solver run and the twenty-piece control - `docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md` (complete)
14. the check of version 4 by a session that did not write it (holds the wording fixes the registration text must carry) - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-claude-code.md` (complete)
15. the check of the competing-solver run and the twenty-piece control - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md` (complete)
16. the measurement rehearsal on small stand-in models - `docs/2026-09-21-successor-measure-rehearsal.md` (complete)
17. the repairs to the rehearsal - `docs/2026-09-26-rehearsal-repairs.md` (complete)
18. the toy re-run under version 3's rules - `docs/2026-09-26-toy-rerun-v3-rules.md` (complete)
19. the controls re-run under the registered rules (source of every toy figure in version 4) - `docs/2026-10-03-controls-rerun.md` (complete)
20. the short pre-stated run - `docs/2026-10-03-short-prestated-run.md` (complete)
21. the ordinary competing solver put through the measurement - `docs/2026-10-03-competing-solver-run.md` (complete)
22. the other-agent control against twenty random pieces (NOT A RESULT: a code test) - `docs/2026-10-03-control-2-twenty-draws.md` (complete)
23. the list of what has gone wrong in this program before, which the inside reviewer ran against version 4 - `docs/known-failure-modes.md` (complete)
24. the opening description of the closed design's task grammar, which version 4 says its grammar extends (inside finding RT-239) - `experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py` (lines 1 to 118)
25. the opening description of the rehearsal's task grammar (inside finding RT-239) - `experiments/rehearsal-successor-measure/src/grammar.py` (lines 1 to 70)

**Files version 4 cites that are not in this packet** (85 of them; named so you know they exist, not because you need them):

- `.venv-lock-2026-08-28.txt`
- `README.md`
- `ROADMAP.md`
- `diagnose_named_other.json`
- `docs/2026-09-25-rented-slice-attempt-2-findings.md`
- `docs/2026-09-25-rented-slice-findings.md`
- `docs/2026-09-26-free-arm-label-search.md`
- `docs/2026-09-26-grammar-attempt.md`
- `docs/2026-10-03-short-prestated-run-method.md`
- `docs/controls-rerun-method-2026-10-03.md`
- `docs/december-result-roadmap-2026-09-20.md`
- `docs/grammar-attempt-method-2026-09-25.md`
- `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
- `docs/preauthorised-spending-proposal-2026-09-21.md`
- `docs/rehearsal-repairs-method-2026-09-25.md`
- `docs/reviews/2026-09-20-program-review/response-chatgpt-astra.md`
- `docs/rulings/2026-09-20-center-as-degree.md`
- `docs/rulings/2026-09-20-december-result-roadmap.md`
- `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`
- `docs/rulings/2026-09-23-nomination-label.md`
- `docs/rulings/2026-09-23-range-and-direction-only.md`
- `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`
- `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md`
- `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`
- `docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`
- `docs/rulings/2026-09-26-weekend-1-queue.md`
- `docs/rulings/2026-10-03-controls-rerun-queue-PROPOSAL.md`
- `docs/rulings/2026-10-03-successor-v3-gate-c-queue-PROPOSAL.md`
- `docs/successor-experiment-proposal-2026-09-21.md`
- `docs/successor-experiment-proposal-2026-09-26-v2.md`
- `docs/successor-experiment-proposal-2026-09-26-v3.md`
- `docs/successor-measure-rehearsal-method-2026-09-21.md`
- `docs/toy-rerun-v3-rules-method-2026-09-26.md`
- `docs/weekend-roadmap-2026-09-24.md`
- `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`
- `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`
- `experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot-findings.md`
- `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-22-rehearsal-rerun-from-code-claude-worktree.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-rulings-check-claude-worktree.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-grammar-attempt-check-claude-worktree.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-successor-v2-failure-mode-pass-claude-worktree.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-toy-rerun-v3-rules-check-claude-worktree.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-controls-rerun-check-claude-code.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-controls-rerun-check-scripts/independent_control4.py`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-rulings-2026-10-03-check-claude-code.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-short-prestated-run-check-claude-code.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`
- `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-scripts/arm_m_true_slot.py`
- `experiments/rehearsal-successor-measure/out-controls-rerun/measure_F_seed0.json`
- `experiments/rehearsal-successor-measure/out-controls-rerun/summary.json`
- `experiments/rehearsal-successor-measure/out-grammar-c/diagnose_named_other.json`
- `experiments/rehearsal-successor-measure/out-grammar-c/passline.json`
- `experiments/rehearsal-successor-measure/out-repairs/gate_base.json`
- `experiments/rehearsal-successor-measure/out-repairs/gate_curriculum.json`
- `experiments/rehearsal-successor-measure/out-repairs/gate_reweight.json`
- `experiments/rehearsal-successor-measure/out-repairs/measure_base_M.json`
- `experiments/rehearsal-successor-measure/out-repairs/self-tests.txt`
- `experiments/rehearsal-successor-measure/out-short-prestated-run/part_a.json`
- `experiments/rehearsal-successor-measure/out-short-prestated-run/part_b.json`
- `experiments/rehearsal-successor-measure/out-short-prestated-run/part_c_NOT_A_RESULT.json`
- `experiments/rehearsal-successor-measure/out-v3-rules/gate.json`
- `experiments/rehearsal-successor-measure/out-v3-rules/models_sha256_check.json`
- `experiments/rehearsal-successor-measure/out/denominator_control6.json`
- `experiments/rehearsal-successor-measure/out/denominator_floor.json`
- `experiments/rehearsal-successor-measure/out/denominator_simulated.json`
- `experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/bench_arms.json`
- `experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/second-release-arithmetic.txt`
- `experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/second_release_arithmetic.py`
- `experiments/rehearsal-successor-measure/src/arm_middle.py`
- `experiments/rehearsal-successor-measure/src/posthoc_control4.py`
- `experiments/rehearsal-successor-measure/src/rehearse.py`
- `experiments/rehearsal-successor-measure/src/repairs.py`
- `experiments/rehearsal-successor-measure/src/rerun_controls.py`
- `experiments/rehearsal-successor-measure/src/rerun_v3.py`
- `experiments/rehearsal-successor-measure/src/short_prestated_run.py`
- `experiments/rehearsal-successor-measure/src/transplant.py`
- `gate_base.json`
- `spec/corrigibility-commitments.md`
- `summary.json`
- `summary_base.json`
- `table.md`

*This is the whole packet in one document. Read it from start to finish before
answering - do not search it for passages that match the questions. Then answer
the brief, which is record 1. Label your findings G1, G2, G3 and so on.*

===== RECORD 1 of 25 - THE BRIEF - the questions you are answering (fixed protocol text, sent unchanged to every reviewer) - `docs/outside-review-protocol.md` (whole sections of the file, from the heading "The brief, fixed, sent unchanged with every packet" up to the next heading quoted in the protocol; 1,358 of the file's 46,763 characters) =====
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
to be polite, and do not manufacture severity to look thorough. A pass that
finds nothing fatal is a valid result, reported as what was checked and what
held.
===== END OF RECORD 1 =====

===== RECORD 2 of 25 - the closure rule this text is being reviewed under - `docs/outside-review-protocol.md` (whole sections of the file, from the heading "The closure rule, which is the new part" up to the next heading quoted in the protocol; 2,793 of the file's 46,763 characters) =====
## The closure rule, which is the new part

Before a registration commit at Gate A:

- Every fatal finding from either tier has a closure line in the ledger, in
  the form: finding, the commit that lands the fix, and a MEASURED check by a
  session other than the one that wrote the fix, showing the fix does what
  the closure says. "Adopted" is a disposition, not a closure.
- **That check belongs to the reviewer, not to the author.** The tier 1
  reviewer of the Gate A pass owns it and runs it: reproduce the denominator,
  build the competing solver, re-run the intervention, recompute the number —
  whichever single measurement would come out wrong if the fix were wrong.
  Reading the fix and finding it convincing is not the check. What the
  reviewer produces is a MEASURED finding in the filed review: the command
  run, the output it gave, and a plain sentence saying whether that output
  matches what the closure claims. If the reviewer cannot run the check, the
  reason goes on the record and the finding stays open.
- **A Gate A with nothing fatal in it still owes that check.** The
  reviewer-owned verification runs at every Gate A, whether or not a fatal
  finding exists. Where there are fatal findings, it covers their closures, as
  the two bullets above set out. Where there are none, it is still owed: the
  tier 1 reviewer runs at least one decisive measured check on the text being
  registered — the single measurement that would come out wrong if the text
  were wrong — and files it the same way, with the command, the output it
  gave, and a plain sentence saying whether that output matches what the text
  claims. A pass that found nothing fatal is still a pass that has to have run
  something. If the reviewer cannot run any such check, the reason goes on the
  record and the gate does not open on the strength of reading alone.
- **The ledger says which of the two happened.** A fatal item's ruling line
  states either that the argument was accepted or that the claim was checked,
  and, when it was checked, names the reviewer and the check. Agreement and
  verification are not the same thing, and the record should not let them read
  as if they were.
- Every sentence in the registered text that says verified, measured,
  calibrated, or attacked cites the committed record by file name, and the
  closure check confirms the record contains what the sentence says it does.
- Serious findings are closed the same way or carried as an open item named
  in the registered text, with John's ruling and reason.
- A declined finding keeps its reason on the record so the next pass can see
  it was considered.

Had this rule been in force on 2026-09-15, RT-21's closure check would have
gone looking for the control battery's attack record and found none.
===== END OF RECORD 2 =====

===== RECORD 3 of 25 - the rule that a full measurement rehearsal comes before any registration review - `docs/outside-review-protocol.md` (whole sections of the file, from the heading "The measurement rehearsal, required before any Gate A" up to the next heading quoted in the protocol; 3,632 of the file's 46,763 characters) =====
## The measurement rehearsal, required before any Gate A

Twice a registration has gone in before anyone had run the measurement it
registers: the corrected metric whose denominator turned out to be zero, and
probes aimed at a quantity that cannot be recovered in principle. Both would
have shown themselves in an afternoon of running the procedure on a throwaway
system. So before any Gate A pass, the whole measurement runs once, end to
end, on a small stand-in, and that run is committed.

The rehearsal is meant to be small and cheap: tiny models, a handful of
episodes, a day or two of work, somewhere between nothing and about ten
dollars of compute. It is not a pilot and it is not evidence about the
question. It is a demonstration that the instrument exists and gives back
numbers.

"Complete" means all six of these, each with the command that was run and the
output it produced in the committed record:

1. **The target can be found.** The quantity the pre-statement names is
   recovered in the stand-in system by the stated instrument, with a number to
   show for it. If it cannot be recovered even there, the rehearsal says so
   and the pre-statement changes before it is registered.
2. **The comparison has room to move.** Every control, baseline or comparison
   condition is scored and its ceiling is measured rather than assumed, so the
   record shows the stated threshold is reachable and the comparison is not
   already saturated.
3. **The arithmetic is finite.** The metric is computed on those scores and
   returns a number: no zero denominator, and no formula that only survives on
   the values its author had in mind.
4. **The interventions run end to end.** Every lesion, patch, swap or other
   intervention the design leans on runs to completion on a saved checkpoint
   and moves the output it is supposed to move.
5. **All three outcomes are reachable.** Made-up cases are built that drive
   the procedure to a positive verdict, to a negative one, and to no verdict
   at all, and each is shown to land where it was meant to.
6. **An ordinary competing solver is built and scored.** A system with none of
   the structure the target claims to detect is constructed and put through
   the same measurement, so the brief's "satisfied by the wrong thing"
   question has a number behind it instead of an argument.

The rehearsal also reports throughput: how long one run takes at rehearsal
scale, and what the registered scale is therefore estimated to cost, so the
spend figure in the proposal has a measurement behind it.

It is filed the way findings are filed, under
`experiments/<experiment>/reviews/YYYY-MM-DD-<target>-rehearsal.md`, or under
`docs/` when the experiment's directory does not exist yet. A pre-stated
quantity with no rehearsal line covering it is a fatal finding on its own, on
the same reasoning as a "verified" claim with no record behind it. The numbers
the rehearsal produces are committed records, so the sentences the closure
rule asks to be cited have something to point at.

First application: the rehearsal for the successor experiment
(`docs/december-result-roadmap-2026-09-20.md`, section 4, step 2 of the chain).
It runs as soon as the successor proposal's first draft exists, alongside the
Gate C tier 1 pass on that draft, rather than in a week set aside for it. It
must show that the three arms are constructible, that the pointer in the
built-to-be-separable arm can be patched, that the joint patch in the
built-to-be-entangled arm works, that the metric returns positive, negative
and invalid values on toy cases, and what the new task grammar costs per run.
===== END OF RECORD 3 =====

===== RECORD 4 of 25 - THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete file, 292,507 characters) =====
# Successor experiment, proposal version 4: reading how much of the act is organised around who is acting

*Written 2026-10-03 (Pacific) by the Claude Code session "MVM proposal version
4 draft", in its own worktree (branch `claude/vigorous-jang-3f7d20`, cut from
the main line at `f32ba0c`). **Status: PROPOSAL, version 4. Nothing here is
registered and nothing here binds.** It is version 3
(`docs/successor-experiment-proposal-2026-09-26-v3.md`, main line at
`6d4ec3a`, pull request 71, left unedited) with John's three sets of rulings
of 2026-10-03 written in, every frozen number stated, and the site list
printed (section 18). It is the text intended for Gate A of
`docs/outside-review-protocol.md` (the registration review, both tiers).
Opening that review is a later step and John's to start. No money is spent
and no machine is rented by this document.*

**This version cannot go to the registration review yet. Three things stand
in front of it.**

1. **This version is owed a check by a session that did not write it**,
   under the pairing rule of the protocol. So is the record of John's
   late-evening ruling on its seven questions, which the same session wrote.
2. **One more short run is owed: the ordinary competing solver, put through
   the measurement as now registered.** John ruled on 2026-10-03 that it is
   run before the registration review opens, at $0, method committed before
   output, by a session other than this one (section 7.3, the last
   paragraph).
3. **Opening the registration review is John's step.**

**Two things that stood here in the first commits of this version are
settled.** The check of the short pre-stated run and of the evening ruling's
record did not exist when this draft was begun; it was filed while the draft
was being written, finds that both hold, and is on the main line at `53c8100`
(pull request 82). And the seven questions this version put to John in
section 19 were ruled the same night, in the words "Agreed on all"
(`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`); each is written
into the body where it bears.

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30): the plain word before the term of art, and no bare
identifier anywhere. Every finding quoted from a record is labelled
**MEASURED** (a command was run and its output is filed in the record cited)
or **ARGUED** (reasoning a reader can dispute). Every number carries the
committed file it was read from. Figures from the arms whose training does not
reproduce are quoted with the caution
`docs/rulings/2026-09-23-range-and-direction-only.md` requires: they describe
the particular trained models on the record, not a property of the code.*

**Notice, 2026-10-03 (night), added by a session that did not write this
version.** The seven questions of section 19 were ruled twice that evening,
in two sessions, and the two records differed on four points. John ruled that
`docs/rulings/2026-10-03-version-4-questions-rulings.md` stands on all four
(`docs/rulings/2026-10-03-seven-questions-reconciliation.md`). The passages below that state
those points were edited to match, each marked "reconciled". They are: the
library versions are pinned (section 7.2, item 1); the registration says what
applying the piece rule after the layers are chosen can miss (section 7.2,
item 3); the sampling band is printed at the floor (sections 7.4, 7.5, 9);
and the separation is the lowest of arm C's readings minus the highest of arm
T's, not paired by seed number (sections 3, 9). **If a sentence elsewhere in
this version still states one of the four the old way, that ruling governs.**

## What this version rests on

Every source but one is on the main line and is cited by its main-line
commit. The one that is not is the last ruling, which is filed with this
version on pull request 83. The first ten rows are new since version 3.

| Source | Main-line commit | Standing |
|---|---|---|
| Version 3 of this proposal | `6d4ec3a` (pull request 71): `docs/successor-experiment-proposal-2026-09-26-v3.md` | The text this version starts from. Left unedited |
| The first independent review of version 3, findings RT-230 to RT-236 | `4cb7f8e` (pull request 74): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`, with its scripts in `reviews/2026-10-03-successor-v3-gate-c-scripts/` | Reviewed version 3 at `37269ad`. Nothing fatal; two serious findings (RT-230, the floor certified the read and not the piece transplanted; RT-233, four controls had no figure under the registered rules); five minor |
| **John's rulings of 2026-10-03 on that review and on version 3's open decisions (sixteen pages)** | `56a5a86` (pull request 75), with a dated note added under its decisions table at `fe5df65` (pull request 77): `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` | **Binding on this version.** Its "What this changes, and where" is the first checklist this version was written to. Two rows of its decisions table (decisions 15 and 16) were changed later the same day by the ruling two rows below; the dated note says so |
| **The controls re-run under the registered rules, and its check** | re-run: `821f154` (pull request 76): `docs/2026-10-03-controls-rerun.md`, method `docs/controls-rerun-method-2026-10-03.md`, outputs `experiments/rehearsal-successor-measure/out-controls-rerun/`; check: `e184a6e` (pull request 79): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-controls-rerun-check-claude-code.md` | **Every toy nomination, reading and control figure in this version is taken from this re-run**, under the rule that only a piece which itself carries the label at four fifths may be chosen. Checked by a session that did not run it: run again from the committed code, all 26 output files are equal value for value |
| **John's three rulings of 2026-10-03 after the controls re-run** | `fe5df65` (pull request 77): `docs/rulings/2026-10-03-controls-rerun-rulings.md` | **Binding on this version.** Control 2 kept as a reported description with no pass line; control 4 redefined and made a control that holds; the piece's accuracy at the other positions of its site reported, not gated |
| **The short pre-stated run** | method and code with no output: `9e978d9`; findings and outputs: `853988f` (pull request 80): `docs/2026-10-03-short-prestated-run-method.md`, `docs/2026-10-03-short-prestated-run.md`, outputs `experiments/rehearsal-successor-measure/out-short-prestated-run/` | The redefined control 4 as a pre-stated quantity, the new reported column for all twelve toy models, and one end-to-end run of control 2's code. **Checked by a second session (next row): run again from the committed code, its output files are identical byte for byte, and every figure in its findings matches them** |
| **The check of the short pre-stated run and of the evening ruling's record** | `53c8100` (pull request 82): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-short-prestated-run-check-claude-code.md`, with its scripts in `reviews/2026-10-03-short-prestated-run-check-scripts/` | Both hold. Four notes for this version, all followed: say the too-early-position control compares the outputs at the two action positions; set out how the new column's two figures are computed and deal with the figure on the average moving by an episode; say that what the short run added for the other-agent control is the part of its code after the floor; say the piece's four fifths is established at the action position only. |
| **John's late-evening ruling of 2026-10-03 on this version's seven questions** | **filed with this version, pull request 83**: `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md` | **Binding on this version.** The floor on the piece only; the piece rule after the layers are chosen; the laptop's processor; the toy's episode counts at full size; twenty random pieces for the other-agent control; two seeds of three when an arm's seeds disagree; the competing solver run before the registration review. Recorded by the session that wrote this version, and owed a check. **Read with the second record of the same evening, `docs/rulings/2026-10-03-version-4-questions-rulings.md`, which by John's ruling stands on the four points where the two differ (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`)** |
| The check of the two ruling packets of 2026-10-03 and their records | `f32ba0c` (pull request 81): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-rulings-2026-10-03-check-claude-code.md` | No number in either packet is wrong; six places where a page says a little more or less than its source. Its section 7 lists what this version should and should not carry, and this version follows it |
| **John's evening ruling of 2026-10-03** | `f32ba0c` (pull request 81): `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md` | **Binding on this version.** The fifth registered outcome is satisfactory and stated as weaker than R1; the new reported figure is printed both ways. The record is checked (the row above): it says what John's words say. On the one part that rested on implication, how the two figures are computed, John confirmed that evening in the words "Yes, section 4 of the method is what I meant"; the dated note recording that is beside item 3 of the ruling record |
| The Gate C tier 1 review of version 2, findings RT-212 to RT-229 | `c17dbdc` (pull request 56): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md` | Reviewed version 2 at `e88c3c0`; one fatal finding (RT-212, the empty read on the free arm), four serious, thirteen minor |
| John's rulings on that review | `3af189d` (pull request 60), refined at `4bb5727` (pull request 63), annotated at `da41c20` (pull request 68), and extended at `a11f1d3` (pull request 69, "RT-212 item 3 resolved"): `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` | **Binding on this version.** Its "What this changes, and where" is the checklist this version was written to; its three refinements after the toy re-run, the annotation of refinement 2's arm C clause, and the resolution of RT-212 item 3 after the label search are carried too |
| The five rehearsal-repairs rulings of 2026-09-25, with their annotations after the check | `62c3824` (pull request 53): `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` | Binding; read with the annotations |
| The rehearsal repairs, session (c), and their check | findings `882f252` (pull request 52): `docs/2026-09-26-rehearsal-repairs.md`; check `d216dbc` (pull request 58) | Checked: every verdict reproduces from the committed code; the decimals on arms C, F and M do not, as the 2026-09-23 ruling expects |
| John's rulings on version 3's decisions 20 and 21 | `9ed9f8c` (pull request 72): recorded in `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` | Binding. Version 3 carried these from John's revision instruction because no ruling file held them yet; one now does |
| The toy re-run under the version 3 rules, and its check | findings `9d9d31a` (pull request 62): `docs/2026-09-26-toy-rerun-v3-rules.md`, Part 1; check `70be9fb` (pull request 65): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-toy-rerun-v3-rules-check-claude-worktree.md` | **Superseded on 2026-10-03 for every nomination, reading and control on arms C, F and M** by the controls re-run above, because the piece rule changes which sizes may be chosen. Still the source for three things: the label-permutation null beside the fit, the history of how the layer-0 and control 3 rules were clarified, and the fits as the laptop's graphics chip computed them (0.172, 0.067 and 0.106 on arm F). Arm T's figures reproduce exactly and are the same in every record |
| The thirty trained toy models | `8038275` (pull request 64) for the fifteen behind the repairs and the re-run, and `7ed2b0e` (pull request 67) for the other fifteen: `experiments/rehearsal-successor-measure/out-repairs/models/` (twenty-one) and `out-grammar-c/models/` (nine), with one `SHA256SUMS` covering all thirty | Committed, with each file's fingerprint; every toy result of 2026-09-25 and 2026-09-26 rests on them (section 10) |
| The grammar attempt (redesign (c)) and its check | attempt `ff778ea` (pull request 57): `docs/2026-09-26-grammar-attempt.md`; check `f1ea004` (pull request 61) | The pass line was not cleared; fallback (d) registers for the named-other condition (section 4.4) |
| The rented slice, second attempt, and its check | `9f802db` (pull request 51): `docs/2026-09-25-rented-slice-attempt-2-findings.md` and the note `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`; check `afb5183` (pull request 55) | Checked: every point passes, point 1 in part (the go was not compared with John's own message, which no committed file holds) |
| Version 2's failure-mode pass | `a3013be` (pull request 54): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-successor-v2-failure-mode-pass-claude-worktree.md` | The author's run on version 2; this version's own run is section 17 |
| The Weekend 1 queue ruling (nine pages, 2026-09-25) | main line: `docs/rulings/2026-09-26-weekend-1-queue.md`; its check, `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-rulings-check-claude-worktree.md`, main line at `7c403b0` (pull request 78) | Ruled. Version 3 said the check of this ruling was still owed. The check had been written on 2026-09-25 and merged into a branch that never reached the main line; it landed on 2026-10-03 |
| The route (b) label search on the free arm, and its check | search: `a97c12b` (pull request 66): `docs/2026-09-26-free-arm-label-search.md`; check: `ecd2b6c` (pull request 70): `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md` | Reported and checked: none of its three candidate reads clears the four-fifths floor on arm F, every figure recomputes, and John ruled on 2026-09-26 that the registration carries the fit floor alone (section 7.2, item 1). Version 3 cited both by branch; both are on the main line and are cited by their main-line commits throughout (the review of version 3, finding RT-236) |

---

## 0. The whole thing in eight sentences

The project's open question is one of degree: a small transformer that has
learned a causally load-bearing answer to "which agent am I" counts as a
centre at the bottom of the gradient, and what would separate it from a
centre in the fuller sense is how much of its act is organised around that
answer. Nobody has a measure of that. So the successor experiment builds
systems whose degree is fixed by how they are built, one where "which agent
am I" sits in a slot that can be swapped on its own, one where it is stirred
into everything, and one that is a mixture of the two by item, and one
ordinary freely trained system, and asks whether a candidate measure can tell
the built systems apart and place the mixture between them. The measure is:
transplant the part of the internal state that says who is acting from one
run into a matched run and see whether the action follows the transplanted
identity; compare that with transplanting the whole internal state at the
same places; the gap between the two, as a share of the room the whole-state
transplant had to move, is the reading. If the measure separates the two
built anchors at the ruled bar, the freely trained system gets a reading and
the project's current sentence "degree unmeasured" is replaced by a number.
If it does not separate them, that is a result too, and the measure is not
used. The reading is made only where the piece of the internal state that is
actually transplanted has been shown to hold its label, at a pre-stated
floor, so that an empty instrument returns *no verdict* rather than a number
at the entangled end; on the toy that is exactly what the freely trained
system returns, on every seed. And the admission that remains is narrower
than before: the toy can now tell an empty instrument from a ceiling, from a
number the procedure already computes, and what it still cannot tell is a
system that is entangled from one whose ownership answer lives somewhere the
read did not look.

---

## 1. Words used here, once

- **The programme.** Minimum Viable Mind, this repository. **MVM-0a** is its
  small-transformer build, registered 2026-08-07, whose Amendment A3 closed on
  2026-09-25 with the registered word *not testable*
  (`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`, the closure
  block dated 2026-09-25).
- **Ownership.** Which of the several agents in a synthetic dialogue the model
  itself is. Nothing psychological is meant by the word; it names a fact about
  the episode that the model has to get right.
- **The acting channel.** The wire through which the model is told, at the
  moment it acts, that this turn is its own: a vector added to the model's
  input state at its own turns. Registered as Amendment A1 on 2026-08-09. It is
  the only honest source of ownership in this design, because in a dialogue
  where the turns are interchangeable, nothing in the text itself can carry it
  (the red-team finding that made this necessary is ledger item RT-17, the
  finding that any learnable ownership cue in the tokens is a fingerprint).
- **The injection, or layer 0.** The place the acting channel is added: the
  running state straight after the input embedding, before the first block.
  The transplant code counts it as layer 0. Section 7.2 removes layer-0 site
  sets from the candidate family wherever they span the turns the channel
  fires on.
- **The ownership answer.** A stored answer to "which of the agents am I" that
  later computation looks up.
- **The marker word.** The made-up name that stands for an agent in an episode.
  Marker words are drawn afresh every episode, so no name is permanently
  attached to any agent. **Which marker word is the model's own** is the label
  the ownership read is fitted against (ruled 2026-09-23,
  `docs/rulings/2026-09-23-nomination-label.md`).
- **The running state.** The vector a transformer carries forward from layer to
  layer at each token position, which everything downstream reads and writes.
  The technical name is the residual stream; it is used once more, in section
  6, and not again.
- **Transplanting (patching).** Taking the running state, or a part of it, out
  of one forward pass and putting it into another at the same place, then
  reading what the second pass does. The programme built this for the first
  time in the measurement rehearsal of 2026-09-21
  (`experiments/rehearsal-successor-measure/src/transplant.py`); nothing at
  the registered size has run it.
- **A fitted straight-line read (a linear probe).** A classifier fitted to the
  running state to predict a label, used here only to propose candidate places
  to transplant, never to conclude anything on its own.
- **The fit, and the fit floor.** How often a straight-line read names the
  model's own marker word correctly on held-out development episodes, stated
  as a count of those episodes (on the toy, of 180). Ruled 2026-09-26 (the
  rulings on the review of version 2, RT-212) and moved on 2026-10-03 from
  the whole read to the piece that is transplanted (next entry): a piece
  whose own count is below **four fifths** cannot be chosen, an arm and seed
  with no piece that reaches it returns *no verdict*, and both counts are
  printed in the reporting table.
- **The piece.** What the ownership-only transplant actually moves: the
  leading 1, 2, 4 or 8 directions of the read at each layer of the site set.
  The number of directions is the piece's **size**; version 3 called it the
  rank, and both words appear below for the same thing. **The piece's own
  accuracy** is the held-out count of a fresh read given only the state's
  coordinates inside the piece (section 7.2, item 3).
- **The label-permutation null.** The fit the same read reaches when the labels
  are shuffled, from two hundred shuffles at toy scale, reported beside the
  fit as its 95th and 99th percentiles. It is reported, not used as the bar.
- **The no-transplant rate.** The share of trials in which the model, with
  nothing transplanted, already gives the value the donor's identity would
  dictate. It is the quantity the chance-corrected form subtracts (section
  6.3).
- **The chance-corrected form.** The reading with the no-transplant rate
  subtracted from both the top and the bottom of the fraction, ruled as the
  registered form on 2026-09-25 (`docs/rulings/2026-09-26-weekend-1-queue.md`,
  page 2).
- **Arms.** The four trained systems being compared: the one built to keep the
  ownership answer separable (arm T, for tracker), the one built to entangle it
  (arm C, for the fuller centre end of the axis), the one built as a mixture of
  the two by item (arm M, for middle; section 5.3), and the ordinary freely
  trained one (arm F, for free).
- **The twenty-draw null (control 3).** Twenty random subspaces of the same
  rank at the same sites, each transplanted in place of the nominated one, so
  the reader can see whether the nominated directions do more than random
  directions of that size would. Reported, not gated (section 7.3).
- **Twins, and a twin's first own turn.** The two episodes of a matched pair
  (section 6.1). A twin's first own turn is the first position at which its
  acting channel is on. Control 4 is defined on the positions before both
  twins' first own turns (section 7.3, item 4).
- **The rider.** John's addition of 2026-09-25 to the reporting table: every
  arm is also read at arm T's nominated site set and rank, beside the reading
  at its own (the queue ruling, page 3).
- **The tripwire.** The billing check of section 12.5: two ratios, either at
  or above 1.25 halts the wave (the queue ruling, page 6, part 3).
- **The registered outcomes: R1 to R4, and a fifth term.** R1 to R4 were set
  by section 2 of the December-result roadmap. The fifth, *metric validated,
  degree not read*, was ruled on 2026-10-03. All five are in section 3.
- **Gates A, B and C.** The three review points of
  `docs/outside-review-protocol.md`: registration, interpretation, and
  proposals that ask John for a ruling. Versions 1 to 3 of this document
  were Gate C material; this version is written as Gate A material.
- **Two phrases left from version 3, and what they mean here.** "The Gate C
  review" and "the Gate C rulings", wherever version 3's text is carried
  unchanged, mean the review of version 2 and John's rulings of 2026-09-26 on
  it. The review of version 3 and the rulings of 2026-10-03 are always called
  that. Likewise "the re-run findings at `9d9d31a`" is the earlier toy re-run
  of 2026-09-26, and "the controls re-run" is the one of 2026-10-03 that
  supersedes its figures for arms C, F and M.
- **Ledger items, written RT-nn.** Numbered red-team findings in
  `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`. Each one
  cited below carries a phrase saying what it found.

---

## 2. The question, and what this experiment is for

The question, from section 1 of the December-result roadmap, unchanged:

> Can a measure of how far an act can be pulled apart, validated on systems
> whose degree is known by how they were built, read the degree of a freely
> trained 30-million-parameter transformer that acquired a load-bearing
> ownership answer under task pressure? If so, what does it read?

Two things the question is not. It is not "is anyone home"; the founding wager
carries that step and no experiment here settles it. And it is not "tracker or
centre" as two kinds of thing; that was ruled one axis of degree on 2026-09-20
(`docs/rulings/2026-09-20-center-as-degree.md`).

What this experiment is for, stated so it can lose: **to deliver a measure, not
a verdict.** That is Stage 2 of `ROADMAP.md`, whose win condition is written in
the roadmap's own words as "deliver the metric, not a verdict", validated on
contrast cases where the answer is known by construction, with a loss condition
for "the metric cannot distinguish the known cases". This proposal supplies the
contrast cases and writes that loss condition down as outcome R2.

The design is the one the outside reviewer named as the single experiment most
likely to change his view of the programme, the matched-role swap experiment
in section 5 of `docs/reviews/2026-09-20-program-review/response-chatgpt-astra.md`,
extended from two arms to four so the measure has a known case at both ends
of the axis and one in the middle.

**What Amendment A3 hands this experiment, in the words its closure block
registers** (`experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`,
the closure block dated 2026-09-25, and
`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`). Its outcome:
*not testable: the registered comparison was undefined for every possible
model; separately, removing the ownership-input channel reduced
primary-battery accuracy on all three trained seeds.* Three things the
successor inherits and must carry, from the block's "Successor" paragraph:
measuring the control's ceiling properly is a precondition of any successor
amendment; nothing counts as localized or as absent until both instruments,
probe and causal patching, agree; and the rehearsal requirement applies to
the successor in full. The block also says what may not be said: that the
ownership structure is absent, or that Amendment A3's nulls make it less
likely. Nothing in this proposal reads Amendment A3's checkpoints, and
nothing here reopens its closure.

**Non-binding motivation, from the Wittgenstein note (ruled 2026-09-25, the
queue ruling, page 7).** The TimeAssembler note "Wittgenstein criteria for the
Stage 2 metric" (document id `d08c23ae-7dca-4e55-9ac3-bb785ebed652` on the
Minimum Viable Mind project; a discussion note of 2026-09-22 that says of
itself "Nothing here is ruled or registered") proposes three tests. Its first
is the rationale this design already runs on, and John ruled that it goes
here, as motivation and not as a requirement: *an internal variable belongs
to the game only if intervening on it changes what the model does.* That is
why the measure is built on transplants rather than on how well a straight
line reads: a representation that a read recovers beautifully but that does
nothing when moved is, on this rationale, not part of the act. The fit floor
of this version is the other half of the same thought: a subspace nominated
by a read that never found its label is not a representation at all, and
transplanting it measures nothing. The note's own caution stands with it:
these criteria license claims about degree of participation, not a verdict on
inside experience. The note's second and third tests wait for resumption
after May 2027; the second is named on the weekend roadmap's extension list
so it is not lost. **Nothing in this paragraph is registered text, and no gate
reads it.**

---

## 3. What counts as a result

Reproduced from section 2 of the December-result roadmap, which John accepted
as the basis of this proposal, with R4 restated to the ruling of 2026-09-21
(item 23 of
`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`), and
with the fifth term John ruled on 2026-10-03
(`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 11, which
amends the roadmap's outcome list; the roadmap carries two dated notes saying
so). The registered wording is the wording in the middle column; nothing in
this document may report an outcome in other words.

| Outcome | Registered term | What it means | Satisfactory |
|---|---|---|---|
| **R1** | **metric validated, degree read** | The measure separates arms T and C at the pre-stated bar (section 9: 0.5 on the chance-corrected form), and arm F gets a reading with its spread across seeds. The closure sentence "degree unmeasured" is replaced by a number, stated as where arm F sits against the three anchors on this measure (weakness W1). | Yes |
| **R2** | **metric does not separate** | Every arm carried passes its gate (section 8.1: the own-directed condition on arms T, C and M; both conditions on arm F), but the measure cannot tell T and C apart at the bar. The measure is not used on arm F; the result is that this candidate does not read degree on this substrate, and the registered design says what to try next. | Yes |
| **R3** | **substrate not a testbed** | One or more arms fail its gate after the one permitted re-run. Reading: this recipe and this size are not yet a place to study mechanism. Resumption starts from a size or recipe change. | Yes, if the gate was reached |
| **R4** | (none) | The programme hibernates with a registered design and a rehearsal only. **Since 2026-09-21 a missed kill date does not put the roadmap here by itself**: registration after 2026-10-18, or launch of the remaining registered runs after 2026-11-01, is still possible on a fresh ruling that names what comes off the back end to make room, and R4 is where the roadmap lands only if that ruling says it is not worth it (item 23 of the 2026-09-21 ruling; section 5 of `docs/december-result-roadmap-2026-09-20.md`). | No. Recorded as a schedule failure, not a scientific one |
| **The fifth term** | **metric validated, degree not read** | Arms T and C separate at the pre-stated bar, and arm F returns no verdict. Reported in those words with the reason after a colon, for example "metric validated, degree not read: read failed its floor". The measure is delivered and validated on the built systems; the freely trained system is not read with it. | **Yes, and stated as weaker than R1** (ruled in John's own words on 2026-10-03: `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling 1, confirming page 11, item 5, of that morning's rulings on its merits) |

**Arm F may return no verdict, and the registration says so in advance (ruled,
the rulings on the review of version 2, RT-212, items 1 and 3; the floor
moved to the transplanted piece by the rulings of 2026-10-03, page 1).** A
reading is made on an arm only where some size of the piece that would be
transplanted clears the fit floor of section 7.2 on held-out development
episodes. On the toy the free arm never did: its best piece, at any layer and
any size on any seed, is right on 34 of 180 held-out episodes against 144
needed, and its whole read is right on 32, 12 and 18 of 180 at the layers the
rule would otherwise choose (MEASURED: `docs/2026-10-03-controls-rerun.md` at
`821f154`, sections 1 and 3, from
`experiments/rehearsal-successor-measure/out-controls-rerun/nominate_F_seed*.json`,
computed on the laptop's processor). The earlier run, on its graphics chip,
gave 31, 12 and 19, which is the 0.172, 0.067 and 0.106 that version 3 quoted
(`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 1, section 1.3;
section 7.2, item 1, says which device's figure is registered). So the toy
record for arm F is **"no verdict, read failed its
floor"** on every seed, and version 2's toy reading for arm F at the
entangled end is withdrawn from the record under failure 2's own rule (the
pre-stated target changed before registration, so the null already collected
is withdrawn rather than reported). **At registered scale the same can
happen, and the first release is the test of it** (John's ruling of
2026-09-26 on the route (b) result, the rulings file at `a11f1d3`, "RT-212
item 3 resolved", item 5; section 7.2, item 1): the single arm F run of step
5a has its nomination reported against the floor before the second release
is asked for, and a miss is a stop there, beside the learn-both stop (section
11). **If arms T and C separate and arm F returns no verdict, the outcome is
the fifth term, "metric validated, degree not read", with its reason after a
colon; it is not reported under R1** (ruled 2026-10-03, page 11, item 3). The
route (b) investigation, which looked for a label the own-directed loss does
force on a free system, found none that clears the floor at toy scale
(section 7.2, item 1), so this version registers with the fit floor alone and
with the ruled label as its one registered read. **The stop after the first
full-size free-model run is unchanged by the fifth term: a miss of the floor
there still goes to John before the second release** (page 11, item 6), and
whether the remaining runs are worth that release is his call with the
registered-size figures in hand.

**The admission (rewritten in version 3 from the ruling on RT-212; reworded
here to say what was measured, as the rulings of 2026-10-03, page 1, item 2,
direct).** Version 2 admitted that a free-arm reading at the entangled anchor
could not be told from the instrument's ceiling, because the chance-corrected
form reads 1 both when the act is entangled and when the nominated subspace
carried nothing. **The toy can tell those two apart, from a number the
procedure already computes**: the accuracy of the piece that is transplanted.
A piece right on 34 of 180 carried nothing, and the fit floor says so before
any transplant is looked at. On arm C, **the read holds the label; the
largest piece transplanted holds it; and no size of piece moves the action.**
In figures: the whole read is right on 180, 177 and 176 of 180 at the chosen
layers on seeds 0, 1 and 2; the chosen pieces, of 8, 8 and 4 directions, are
right on 180, 172 and 150 of 180 at the action position; and the
ownership-only transplant of those pieces lands at 0.0488, 0.0525 and 0.0612
against a no-transplant rate of 0.0512, 0.0488 and 0.0600 (MEASURED: the
controls re-run at `821f154`, section 2, from
`out-controls-rerun/measure_C_seed*.json`; "no size moves the action" is the
review of version 3, RT-230, which read arm C between 0.9897 and 1.0051 at
every size on every seed, at version 3's site sets). That is what "entangled
at these sites" means. Version 3's sentence here, that a subspace nominated
by a read at 0.96 or better "held the label and still moved nothing", claimed
more than was measured: on two seeds of three the piece it transplanted held
the label at 0.544 and 0.306 (the review, RT-230), and it is replaced by the
sentence in bold above.

**The piece's four fifths is established at the action position only.** Where
a site covers several positions, the same directions are transplanted at
every one of them, and away from the action position the piece often falls
below four fifths. On arm C seed 1 it is right on 139, 139 and 33 of 180 at
the three positions before the action; on arm C seed 2 it is below 144 at all
ten positions reported, from 30 to 139, and 123 on the average over the other
positions; on arm M it clears on the average on every seed (163, 174 and 175)
and misses at six, six and three of the ten positions reported. The whole
state at those positions holds the label throughout (149 to 180 of 180 on the
built systems), so the label is there and is not held in the chosen
directions (MEASURED, **checked: the check of the short run at `53c8100`**:
`docs/2026-10-03-short-prestated-run.md` at `853988f`, section 4, from
`out-short-prestated-run/part_b.json`). So "the piece held the label and the
transplant of it did nothing" is true at the action position and is not shown
across the whole site. John ruled that this is reported in the registered
table both ways and gated in neither
(`docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3;
`docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling
2); it is weakness W13.

What the admission that remains says (ARGUED): a piece that clears the floor
shows the label is present in those directions at the action position; it
does not show that the directions it found are the ones the act uses. A free
arm whose piece clears the floor and whose reading is near 1 is therefore "as
entangled as the built anchor at the sites this procedure nominates", and no
more; that the ownership answer lives in some other part of the state the
read did not find is not excluded. Arm M (section 5.3) is a known case in the
middle of the scale, so that a free-arm reading can be placed against three
anchors rather than two. It does not remove that residual admission, because
arm M's known degree is a mixture by item, and a free arm's partial
separation, if it has any, would be within each trial (section 5.3).

**The toy outcome, on the anchors' terms (ruled, the rulings on the review of
version 2, RT-213, item 1).** Under the rules this version registers, the toy
reaches the fifth term: its anchors separate and its free arm is not read.
Arm T reads 0.0000 and arm C **1.0051, 0.9926 and 0.9974**, so the
separation, arm C minus arm T, is 1.0051, 0.9926 and 0.9974 and clears 0.5 on
every seed; arm M reads 0.4886, 0.4860 and 0.5449, inside its band on every
seed; and arm F returns no verdict on every seed, twice over, because it
fails its gate and no piece of its read reaches the floor (MEASURED: the
controls re-run at `821f154`, sections 1 and 2, from
`out-controls-rerun/summary.json`; reproduced value for value by the check at
`e184a6e`, section 3). Version 3 gave arm C as 1.0051, 1.0025 and 1.0000;
seeds 1 and 2 were read through pieces of two directions and one, which do
not hold the label (the review, RT-230), and are replaced. Arm C's named-other
condition fails on every toy seed, at 760, 751 and 708 correct of 3,000
against a bar of 790 (MEASURED: `out-repairs/gate_base.json` at `882f252`;
the review of version 2, RT-213); under version 2's rules that made the toy
an R3, and under this version's it does not, because the constructed arms
are gated on the own-directed condition only (section 8.1) and their reading
uses only the own-directed action. **Version 2 left that failure out, and
this version states it wherever arm C's toy record is quoted** (sections 5.2,
10 and 11).

**The honest prior, stated before the work rather than after it.** On the
existing record the most likely outcome at registered scale is that **arm F
returns no verdict, or fails its gate**, and the most likely reason for either
is the named-other half of the task and the read that cannot find its label.
Three seeds of the closed Amendment A3 design failed to learn a named-other
query battery, landing at 0.2877, 0.3057 and 0.3195 against 0.3227 for a
solver that cannot read the name the question supplies; a fourth run with the
battery's own loss term reached 0.3125 and changed nothing
(`control-learnability-pilot-findings.md`, the pilot findings file; ledger
items RT-52 to RT-69). This experiment moves the named-other condition from a
query at the end of the episode to an action at the model's own turn. **At toy
scale that has not been enough, and every repair tried has now been tried and
failed** (section 4.4): the named-other condition failed its bar on two of
three toy arms; doubling the training budget did not fix it; a curriculum and
loss re-weighting did not fix it; and the grammar change, redesign (c), did
not fix it either, at 774, 730 and 759 correct of 3,000 on the free arm
against 790 needed on two seeds (MEASURED: `docs/2026-09-26-grammar-attempt.md`
at `ff778ea`, section 3; its check at `f1ea004` re-ran it and got 750, 809 and
739, so at most one seed of three clears on either run). Fallback (d)
registers. Section 11 places a stop before the expensive wave so that a
gate failure on arm F costs the first release (about $44, section 12.3)
rather than the whole plan; **a failure on arm C, the high anchor, is first
seen in step 5b, after the second release is drawn, and section 11 states
that cost.**

**What a no verdict maps to (ruled 2026-10-03, page 11; it closes the
no-verdict finding RT-182 of the review of version 1, that the measure's own
failure state had no registered outcome term).** An arm's *no verdict* is
reported in those two words with its reason after a colon, as the re-run's
table does ("no verdict: read failed its floor"). Then:

1. **No verdict on arm C** fires the two-arm fallback John accepted in
   advance on 2026-09-20 (section 5.2).
2. **No verdict on arm M** drops arm M, which is then carried as an extension
   on the weekend roadmap.
3. **No verdict on arm F after arms T and C have separated** is the fifth
   term of the table above.

**When an arm's three seeds disagree, two of three decide, and the third is
reported (ruled 2026-10-03, late evening: `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`,
ruling 6).** The floors and the controls that hold apply per arm and seed
(section 7.2, item 1), so an arm can read on two seeds and return no verdict
on the third. The rule is the one the design already uses for its gates. As
this session reads it, in wording that is its own and John's to overturn: an
arm is read if at least two of its three seeds return a reading, and returns
no verdict, as an arm, if two or more of its seeds do; and every seed is
printed, whichever way it went. **Reconciled 2026-10-03 (night): the
separation is not compared seed by seed.** It is the lowest reading among arm
C's seeds that read, minus the highest among arm T's seeds that read, and it
must be at least 0.5; seeds are not paired by number, because seed 0 of one
arm has no relation to seed 0 of another. "Metric validated" means arms T and
C each read on at least two seeds and that separation clears; "degree read"
means arm F reads on at least two seeds; if arm F reads on one seed only, the
outcome is "metric validated, degree not read" and that seed's figure is
printed as a description (`docs/rulings/2026-10-03-version-4-questions-rulings.md`,
ruling 6; `docs/rulings/2026-10-03-seven-questions-reconciliation.md`). On the
toy that separation is 0.9926. On the toy every arm behaves alike on all three seeds, so the
rule has not yet been exercised on a split. The record of that ruling notes
that this was the one question the session flagged as deserving more of
John's attention than a general agreement gives it.

---

## 4. The task: matched-role revisions

### 4.1 What the model does

The grammar extends the registered Amendment A3 grammar (`curriculum_a3.py`,
the episode generator committed 2026-09-15), which already has the pieces:
four agents, a closed vocabulary, ten turns, eight value slots, every revised
item assigned by all four agents before anyone revises it, and a revision rule
that is a deterministic function of the reviser's own earlier value (the
successor of that value, counted round the eight slots). The rehearsal's
shrunken version of it is `experiments/rehearsal-successor-measure/src/grammar.py`.

The change is that the model now acts in **two matched roles at the same kind
of position**:

- **Own-directed revision.** The model's turn arrives; the correct output is
  the successor of **the model's own** earlier value on that item.
- **Named-other-directed revision.** The model's turn arrives carrying a
  marker word; the correct output is the successor of **the named agent's**
  earlier value on the same item.

Both are actions on the model's own turn, supervised the same way, scored the
same way. This is the whole point of the redesign: in the closed Amendment A3
design the ownership condition was an action and its comparison condition was a
question asked at the end, so the two were never at the same kind of position,
which is the defect the outside review called out and the internal requirements
document had already ranked first for repair.

**The grammar is as version 2 had it.** The grammar change attempted on
2026-09-25 (redesign (c), section 4.4) did not clear its pass line, so nothing
in this section changes; in particular the acting channel fires on both action
turns, as before.

### 4.2 What "matched difficulty" means, concretely

Four things are matched, by construction in the generator and checked at the
rehearsal (MEASURED on the toy grammar: the four matched properties hold,
`docs/2026-09-21-successor-measure-rehearsal.md`, check P-1 and rehearsal item
R-1; re-checked on 3,000 matched pairs under the grammar attempt's setting
too, `docs/2026-09-26-grammar-attempt.md` at `ff778ea`, section 2):

1. **Candidate count.** In both conditions the item has been assigned by all
   four agents, so four earlier values are in the context. A solver that cannot
   tell which agent the answer belongs to can do no better than one in four.
   Random guessing over the eight slots is one in eight. Both numbers are the
   same in both conditions.
2. **Distance.** The number of turns between the source assignment and the
   action, and the number of intervening turns by other agents, are drawn from
   the same distribution in both conditions.
3. **Supervision.** Equal numbers of supervised action positions of each kind
   per episode, equal loss weight per position, one scored token per position.
4. **Transformation.** The same successor rule in both conditions, so nothing
   about the arithmetic differs.

**The asymmetry that cannot be matched, stated rather than hidden.** In the
named-other condition the identity of the source agent is a token in the input;
in the own-directed condition it is not, and cannot be, because a dialogue with
interchangeable turns carries no honest ownership signal in its text (ledger
item RT-17). So one condition reads its answer's owner and the other has to
have carried it. That asymmetry *is* the experiment; removing it would mean
putting the model's own name in the text, which would reintroduce the very
leak the acting channel was built to avoid. It is recorded here, will be
recorded in the registration text, and bounds what a difference between the two
conditions may be read as. **Ruled 2026-10-03 (decision 9): it is recorded as
a known limitation and not engineered away.**

**Distinctness, and the one place it is relaxed.** Within an item the four
agents' values are distinct, drawn without replacement (MEASURED on the
rehearsal grammar: `experiments/rehearsal-successor-measure/src/grammar.py`,
the function `_content`, draws the four values with `replace=False`, and the
matched-property check counts four distinct candidate values on every item).
Sections 4.2, 6.1 and 8.1 lean on that. Control 6 in section 7.3 needs its
negation for one of its two cells, so control 6 runs on a **separately
generated relaxed set** in which one item per episode has two agents sharing
a value (the same file's `collide` option), labelled as such wherever it
appears. The relaxed set is never used for the reading, the gates or any
other control. Section 7.3 gives the trial counts that set produces.

### 4.3 Carried-forward rules that apply to the new generator

- **The even-split rule.** Any batch fraction that splits rows by condition must
  give an even number of rows, or the split cuts the generator's matched content
  pairs. Measured and recorded 2026-09-20 as ledger item RT-58 (the batch-split
  bias check). The rehearsal grammar carries it (`grammar.py`, the function
  `_check_even_split`).
- **The one-scored-token self-test.** The check that exactly one token per
  supervised position is scored, and that the check survives the shift the loss
  function applies: ledger item RT-59, which turned out to need more than the
  one line it was first written as. It runs on every generator build.
- **The cue-detector gates.** Gates (i) and (ii) of the registered design (no
  surface cue in the curriculum text or the input tensors predicts which turns
  are the model's own) run unchanged on the new grammar. Gate (iii), the
  likelihood attack, runs in its act-withheld form as re-specified in Amendment
  A3 §3.4, because the policy at a revision position is perspectival and
  scoring another agent's turn under it with the acting channel present would
  read the model's ownership knowledge as a leak.

### 4.4 The named-other condition: fallback (d) registers

**What registers (ruled 2026-09-25: the queue ruling, page 4, fallback (d);
the repairs rulings, item 1, whose "if it does not, (d) is what registers" is
now the case).** The registration text records, in these words:

- that the named-other condition **failed its bar on two of three toy arms**
  (on the committed models: arm F clears it on 1 seed of 3, at 994, 781 and
  746 correct of 3,000 against 790; arm C on 0 seeds of 3, at 760, 751 and
  708; arms T and M on 3 of 3; MEASURED: `out-repairs/gate_base.json` at
  `882f252`, reproduced field for field by the re-run's `out-v3-rules/gate.json`
  at `9d9d31a`);
- that **doubling the training budget did not fix it**
  (`docs/2026-09-21-successor-measure-rehearsal.md`, section 8);
- that **both training changes did not fix it**: a curriculum (the named-other
  condition alone for the first 1,000 of 2,500 steps) and loss re-weighting
  (the named-other loss four times the own-directed) cleared on 0 of 3 seeds
  each, against 1 of 3 on the unchanged recipe, and both made it worse
  (MEASURED: `docs/2026-09-26-rehearsal-repairs.md` at `882f252`, section 2,
  from `out-repairs/gate_curriculum.json` and `out-repairs/gate_reweight.json`;
  the check at `d216dbc` re-ran both from clean and got 0 of 3 each again);
- that **the grammar change did not fix it**: redesign (c), which turns the
  acting channel off on the seven tokens of the named-other action turn so
  that the two action turns no longer receive the same "this turn is yours"
  signal, ran on 2026-09-25 with its pass line committed before the run (790
  or more of 3,000 on at least two free-arm seeds of three, with the
  own-directed condition not degraded below 0.5513). It got **774, 730 and
  759**, 0 seeds of 3; the own-directed half held at a mean of 0.5654
  (MEASURED: `docs/2026-09-26-grammar-attempt.md` at `ff778ea`, section 3,
  from `out-grammar-c/passline.json`). Its check re-ran the attempt from the
  committed code and got **750, 809 and 739**, 1 seed of 3, and the same
  verdict (MEASURED: `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-grammar-attempt-check-claude-worktree.md`
  at `f1ea004`, "Verdict"). **The check's note is carried into the record:
  a count of seeds clearing is a property of one training run, not of the
  code**, so the record says "at most one seed of three clears on either
  run", which is also what both earlier runs of the unchanged grammar gave;
- and that **the staggered first run bounds the money** (section 11, step 5a):
  the learn-both result of one free-arm run is read before the remaining
  runs are committed.

**Stop condition S1 did not fire.** It asks whether the grammar is learnable at
tiny scale even in principle, and the separable arm learned both conditions to
1.0000 (MEASURED: `out-repairs/gate_base.json` at `882f252`, arm T on every
seed). This is John's ruling, adopting the rehearsal's adjudication (the queue
ruling, page 4).

**The diagnosis, ARGUED and not ruled.** In this grammar the acting channel
fires on both action turns, so the two turns differ only in one word, and a
model that learns the own-directed route applies it at the named-other turn
too (the repairs findings, section 2, the paragraph headed "The reading").
The grammar attempt tested exactly that diagnosis by removing the shared
signal, and found the free arm still gives its own value at the named-other
turn only about one time in twenty and splits the rest across the other
agents' values, the same pattern as before the change (the grammar attempt at
`ff778ea`, section 3, from `out-grammar-c/diagnose_named_other.json`). Its
own reading, marked ARGUED there and here: the model already tells the two
turns apart and fails at a different step, matching the named marker word to
that agent's assignment. The check agrees the pattern is measured and the
step is not (the grammar check at `f1ea004`, section 4). Nothing in this
version acts on that reading.

**What the grammar attempt's failure does not show.** It does not show that no
grammar change could work, only that the smallest one, which removes the
shared acting signal, did not; and the toy arms may be too small to learn a
condition the registered size will learn, which is page 4's standing argument
against every toy redesign (the grammar attempt, section 7; ARGUED).

---

## 5. The four arms

All four train on the same grammar, at the same size (the registered 30M
configuration), on the same token budget, with the same launcher, watchdog and
network volume. **The launcher, named (ruled, the Gate C rulings, RT-228):**
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`,
the unregistered launcher that carries the argument guard of ledger item
RT-198 and the hang fix of 2026-09-25, and that the rented slice's second
attempt ran (`docs/2026-09-25-rented-slice-attempt-2-findings.md` at
`9f802db`). The registered launcher `launch_a3.sh` is registered text under a
standing prohibition (it has no argument handling) and is not used. **Part of
the registered recipe (ruled 2026-10-03, decision 13): the launcher waits for
the laptop's receipt, and the trainer does not delete its own machine.** What
the registration says about the shutdown is section 13, weakness W9. **Two
things are owed as code before step 4 of section 11, and this document does
not do them:** a training entry point on the rented machine for arms T, C and
M, which does not exist yet, and the tripwire of section 12.5. Arm M's code
(`experiments/rehearsal-successor-measure/src/arm_middle.py`) has run only on
this laptop; that is listed as untested beside the handshake's machine half
in weakness W9. What differs between the arms is the architecture, and only
in the way the ownership answer is allowed to exist.

### 5.1 Arm T: the ownership answer kept separable, by construction

The registered trunk plus two additions:

- **An explicit table** of assignments: for each agent and each item, the value
  that agent most recently assigned. It is written at assignment turns and read
  at action positions.
- **A separate slot holding the ownership answer**, a single vector position
  that carries "which agent am I" and nothing else, produced from the acting
  channel and read by the action head as the row selector into the table.

The action is computed as: read the ownership slot, read the table row it
selects for the current item, apply the successor rule. The factoring into
(table, ownership answer, lookup) is the architecture, not something the
network may or may not discover, and the ownership slot is a single place that
can be transplanted on its own. **Its degree is zero by construction**, and
that is the point of the arm.

What the toy measured, under the rules this version registers: it reads
**0.0000 on every seed**, nominated at layer 0 at the action position with a
piece of 8 directions, the whole read and the piece each right on 180 of 180
held-out episodes on every seed; its ownership-only transplant moves the
action in every trial, above all twenty random draws of control 3 (MEASURED:
the controls re-run at `821f154`, section 2). Under the stricter layer-0
variant of section 7.2 its site moves to layer 1 at the action position and
it still reads 0.0000 (the same record, section 4). Its gate and lesion
figures reproduce the 2026-09-21 record exactly, and its toy training
reproduces from code and seed
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-22-rehearsal-rerun-from-code-claude-worktree.md`).

**Ruled 2026-10-03 (decision 2): the ownership path is forced by the
architecture, not merely encouraged by a penalty term.** The forced version
is what makes the degree known; a soft version would be more comparable with
arm F but would forfeit the one thing the arm exists to supply.

### 5.2 Arm C: the ownership answer entangled, by construction

The registered trunk with the ownership signal mixed into the content
representation at every layer, and no slot of its own anywhere:

- The acting channel produces, per layer, a scale-and-shift applied to the
  whole running state of that block, so the ownership signal multiplies content
  rather than sitting beside it.
- The item and value representations are combined with the ownership signal
  multiplicatively at the point of binding, so that "which item, whose value"
  is one quantity rather than two.
- No dedicated ownership position exists and no part of the architecture reads
  ownership alone.

The prediction, if the construction works: transplanting any single nominated
part of the state fails to reproduce the counterfactual action, while
transplanting the whole state at the same places succeeds. **Its reading should
be high.**

**What the toy measured, under the rules this version registers (MEASURED:
the controls re-run at `821f154`, sections 2 to 4, from
`out-controls-rerun/nominate_C_seed*.json`, `measure_C_seed*.json` and
`summary.json`; reproduced value for value by the check at `e184a6e`, section
3).** It reads **1.0051, 0.9926 and 0.9974** on seeds 0, 1 and 2, at the
entangled end on every seed, quoted per seed for these particular models and
not as a property of the code. The rule chose:

| Seed | Site set | Size of piece | Whole read, right of 180 | Piece, right of 180, at the action position | Whole-state, ownership-only and no-transplant shares | Reading |
|---|---|---|---|---|---|---|
| 0 | layer 2 at the action position | 8 directions | 180 | 180 | 0.5400, 0.0488, 0.0512 | 1.0051 |
| 1 | layer 1 at the action position and the three before it | 8 directions | 177 | 172 | 0.5550, 0.0525, 0.0488 | 0.9926 |
| 2 | layer 1 from the model's first own turn to the action | 4 directions | 176 | 150 | 0.5463, 0.0612, 0.0600 | 0.9974 |

**What that shows, in the words the ruling of 2026-10-03 directs (page 1,
item 2): the read holds the label; the largest piece transplanted holds it;
no size moves the action.** Every chosen piece clears four fifths (144 of
180) at the action position, and its ownership-only transplant lands within
0.004 of the no-transplant rate while the whole-state transplant moves the
action in more than half of trials. That no size moves the action is the
review of version 3, RT-230, at version 3's site sets: arm C read between
0.9897 and 1.0051 at 1, 2, 4 and 8 directions on every seed. **Version 3's
sentence here, that the subspace arm C transplants "holds the label and
clears the fit floor on every seed", was false on two seeds of three** (the
pieces it chose there, of two directions and of one, held the label at 0.544
and 0.306; the review, RT-230), and its readings for those seeds (1.0025 and
1.0000, at layers 4 and 1) are replaced by the table above. Version 2's
figures for this arm (0.99 to 1.00, and the separation figures 0.9977 and
0.9927) were replaced in version 3 and stay replaced.

**Away from the action position the piece often does not hold the label at
four fifths.** On seed 1 the piece is right on 139, 139 and 33 of 180 at the
one, two and three positions before the action, and 113 on the average over
those three. On seed 2 it is below 144 at all ten positions reported, from 30
to 139, and 123 on the average over the other positions of its site. Seed 0's
site is a single position (MEASURED, **checked: the check of the short run at `53c8100`**:
the short pre-stated run at `853988f`, section 4). The whole state holds the
label at every one of those positions. This is reported and not gated
(section 7.2, item 3; weakness W13).

**The choice among candidates is made among sampling noise on this arm, and
the record says so.** On seed 1 the rule chose layer 1 over layer 4 because
the development ownership-only share was 0.0533 against 0.0517, one episode
of 600; the session that ran the re-run had predicted layer 4, and said so in
its findings. What the piece rule fixes is that whichever candidate wins, its
piece carries the label. The reading at the chosen site is 0.9926; at layer 4
with 8 directions it was 0.9975 (the controls re-run, section 3; the review,
RT-230). **This version does not use the sizes and readings on page 1 of the
ruling packet of 2026-10-03 (8, 8 and 4 directions at layers 2, 4 and 1;
1.0051, 0.9975 and 0.9974): they were that session's forecast, the ruling
itself says they are not committed results, and the forecast was wrong on
seed 1.**

Control 3's twenty random draws all sit above the ownership-only transplant
on seed 0, and around it on seeds 1 and 2 (6 below, 1 equal and 13 above; 6
below, 5 equal and 9 above), which is what an entangled arm should show: its
ownership piece does no more than a random piece of its size (the controls
re-run, sections 2 and 4; the reading of it is ARGUED).

**Arm C fails the named-other condition on every toy seed, and this version
says so wherever its toy record is quoted (ruled, the Gate C rulings, RT-213,
item 2).** Its named-other accuracy is 760, 751 and 708 correct of 3,000
against a bar of 790, so it clears on 0 seeds of 3, while its own-directed
condition clears on 3 of 3 (MEASURED: `out-repairs/gate_base.json` at
`882f252`, fields `runs.C/base/*.other_correct`; the Gate C review, RT-213).
Under version 2's learn-both gate that would have made the toy an R3 by way
of the high anchor. Under this version arm C is gated on the own-directed
condition only (section 8.1), with the reason recorded there, so its toy
record is a pass on the gate and a reading on every seed. **What that failure
costs under the launch order** is in section 11: a constructed arm that fails
its gate at registered scale is first seen in step 5b, after the second
release is drawn, and John ruled against an extra arm C run in step 5a on the
envelope's arithmetic (the Gate C rulings, RT-213, item 3).

**This arm is conditional and the condition is already accepted.** John ruled
on 2026-09-20 that arm C depends on the rehearsal showing that its degree is
genuinely known by construction rather than merely intended, and that the
two-arm fallback is accepted in advance. This proposal keeps that exactly as
ruled; rehearsal items R-3 and R-6 in section 10 are the test, and at toy
scale both pass under the registered rules. **Also ruled, 2026-10-03
(decision 3): arm C entangles by its architecture, and is not trained with a
penalty against transplantable ownership directions**, which would train the
system against the very instrument that will measure it.

**Why the fallback is weaker, said plainly.** With arms T and F only, the
measure is anchored at one end. A reading on arm F above arm T's would show the
measure responds to something, and that arm F is less separable than a system
built to be separable, but there would be no known-high case, so nothing would
establish that the measure *scales* rather than merely *detects*, and the
number given to arm F would have no upper reference. The registration text, if
the fallback fires, says that in those words, and the R1 sentence is
correspondingly weaker.

### 5.3 Arm M: a mixture of the two, by item

**Why it exists.** Section 3's admission, in its version 2 form: with anchors
only at the two ends, a free-arm reading at the entangled end cannot be told
from a ceiling. John ruled on 2026-09-25 that a fourth, partly separable arm
would be attempted at toy scale at $0, with its predicted reading stated
before it ran, and folded into the main registration only on a pre-stated
pass: a chance-corrected reading between 0.3 and 0.7 on all three seeds (the
queue ruling, page 5, option (iii)). It passed on the repairs run, and it was
folded in (the repairs rulings, item 2).

**Version 2's arm M pass was read without control 3 applied (ruled, the Gate C
rulings, RT-214, item 3).** Under version 2's own rules, which made control 3
a control that holds with a fixed 0.0175 room, arm M seed 1 got no reading
(its random subspace moved 0.0563 of trials against a limit of 0.0350; the
Gate C review, RT-214), so the "on all three seeds" pass John folded arm M in
on was not met by the design as then written. Control 3 is now a reported
twenty-draw null (section 7.3), and under it arm M reads on every seed; the
re-run was the check the RT-214 ruling asked for before this version was
filed, and its result is below.

**The construction** (`experiments/rehearsal-successor-measure/src/arm_middle.py`,
method in `docs/rehearsal-repairs-method-2026-09-25.md`, section 5, both at
`882f252`): arm T's slot and head, and arm C's entangling and ordinary output
layer, in one network. Actions about some items go wholly through the
separable route and actions about the others go wholly through the entangled
route, so that about three fifths of actions are entangled: 0.60375 of the 800
fresh measurement trials, 483 of 800 (MEASURED: `out-repairs/measure_base_M.json`
at `882f252`, the field `fourth_arm.entangled_share`). The repairs findings
print 0.6033, which is the same share on the held-out gate episodes, 1,810 of
3,000 (MEASURED: `out-repairs/gate_base.json` at `882f252`, the field
`own_by_route.entangled_share`); both are right, on different episodes (the
Gate C review, RT-219). **The registration
describes it as what it is: a mixture by item, each action going wholly
through the separable or the entangled route, about three fifths entangled,
not partial separation within a trial** (the repairs rulings, item 2, in those
words).

**The prediction, and what it is (ruled, the Gate C rulings, RT-223).** Write
*p* for the entangled share, and for each route write its whole-state and
no-transplant accuracies. The reading the measure should return, if the blind
nomination catches the separable route's slot and nothing of the entangled
route, is the entangled route's share of the total room the whole-state
transplant moves:

    p × (whole_C − untouched_C) / [ (1 − p) × (whole_T − untouched_T) + p × (whole_C − untouched_C) ]

**That formula is the true-slot reading of section 7.2, item 6, written in
route accuracies: one check, not two.** By algebra, a transplant that carries
the separable route fully and the entangled route not at all gives exactly
this number in the chance-corrected form, and on the repairs run the formula
and the true-slot reading agree to four decimals on every seed (0.4895,
0.4572 and 0.4904; MEASURED: the Gate C review, RT-223, from
`out-repairs/measure_base_M.json` at `882f252`). So what the comparison
shows is that the blind nomination finds about what the true slot gives on
the same episodes, a check of the nomination against the construction, and
not a prediction made in advance of the run. The registered prediction for
arm M at the registered size is: **between 0.3 and 0.7 on every seed, and
within 0.10 of the true-slot reading on the same fresh episodes.** The
true-slot reading is computed and written down before the blind reading is
looked at.

**What the toy measured, under the rules this version registers (MEASURED:
the controls re-run at `821f154`, sections 2 and 4, from
`out-controls-rerun/measure_M_seed*.json`; reproduced by the check at
`e184a6e`, section 3).** The blind reading is **0.4886, 0.4860 and 0.5449**
on seeds 0, 1 and 2, inside 0.3 to 0.7 on every seed, so the fold-in pass
stands with control 3 reported beside it. Every seed is nominated at layer 1
from the model's first own turn to the action, with a piece of 8 directions;
the whole read and the piece are each right on 180 of 180 at the action
position; the whole-state transplant moves 0.7800, 0.7738 and 0.7937 of
trials and the ownership-only transplant 0.4050, 0.4062 and 0.3688, above all
twenty random draws of control 3 by a wide margin (random medians 0.015 to
0.019). **The "within 0.10" half of the prediction now has its figure at the
registered site sets, which version 3 listed as owed:** the true-slot reading
is 0.4837, 0.4760 and 0.4920, the route formula agrees with it to four
decimals, and the blind reading is within **0.0049, 0.0099 and 0.0529** of it
(MEASURED: the review of version 3, RT-231, from its script
`arm_m_true_slot.py`; found again by the controls re-run, section 4, whose
prose printed the middle figure as 0.0100 from two rounded numbers; the
unrounded difference is 0.00995, and the check at `e184a6e`, section 3,
gives 0.0099). Seed 2 uses a little over half the allowance. Arm M passes its
gate on the own-directed condition on all three seeds (0.8613 to 0.8667), and
clears the named-other condition too (0.5517 to 0.5663), although that is no
longer gated for it (MEASURED: `out-repairs/gate_base.json` at `882f252`).
Its self-test passes all seven checks, including that perturbing the slot
never moves an entangled-route action (`out-repairs/self-tests.txt` at
`882f252`).

**Away from the action position arm M's piece is not what this session, or
the one that ran it, expected.** On the average over the other positions of
its site the piece is right on 163, 174 and 175 of 180, above four fifths on
every seed. Position by position it reaches 144 at only four, four and seven
of the ten positions reported, and at the fourth token of the model's first
own turn (the value word) it is right on 34, 71 and 33 (MEASURED, **checked: the check of the short run at `53c8100`**: the short pre-stated run at `853988f`, section
4, whose author records that it expected better and was wrong). The two ways
of computing the figure give different pictures of this arm, which is why
John ruled that the registered table prints both (section 7.5).

**What this buys, and what it does not (ARGUED, from the findings' own
words).** It shows the measure, pointed blind at a system with a known
mixture, returns a number in the middle and near the mixture's share. It does
not show that the measure scales on a system whose partial separation is
*within* each trial, which is what a freely trained system would have. Page
5's strongest argument against applies in full and is carried as weakness
W10: its degree is a design intention, and it differs from both anchors in
more than degree.

**What it costs.** Three registered runs, priced at **$32 to $44** from the
compute ledger's per-run rows (the queue ruling, pages 5 and 6; the
derivation, from the ledger's 2026-09-19, 2026-09-17, 2026-09-15 and
2026-08-12 rows, is on page 5 of
`docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`), from the $450
envelope (section 12). Of that, the $1.94 development run at the 10-million
size is now paid from the first release's development line and launched in
step 4 with the other three arms (ruled, the Gate C rulings, RT-229; section
12.3), and section 12.4 carries only the three registered runs. **Arm M's
seconds per step were not measured on the rented machine**: the slice of
2026-09-25 timed arms T, C and F only
(`docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section
3). Its three runs therefore rest on ledger rows, not on rehearsal item R-11,
and section 12.4 says so.

### 5.4 Arm F: the freely trained system

The registered register-less configuration with the acting channel present,
the same architecture as the closed Amendment A3 runs, trained on the same
matched-role grammar with no constraint on where the ownership answer may live.
This is the system being read. It is read only after it passes the learn-both
gate, the ownership-lesion check in section 8, and the fit floor of section
7.2.

**What the toy record states for it: "no verdict, read failed its floor", on
every seed (ruled, the rulings on the review of version 2, RT-212, item 2;
the floor moved to the piece on 2026-10-03).** No piece of its read of "which
marker word is the model's own" reaches four fifths at any layer, at any
size, on any seed: the best is right on 34 of 180 held-out episodes against
144 needed. Its whole read is right on **32, 12 and 18 of 180** on seeds 0, 1
and 2 at the layers shown in the re-run's table (MEASURED: the controls
re-run at `821f154`, sections 2 and 3, from
`out-controls-rerun/nominate_F_seed*.json`, `fits`, on the laptop's
processor). On the laptop's graphics chip the same reads were right on 31, 12
and 19, which are the 0.172, 0.067 and 0.106 quoted in version 3 and in every
earlier record; each difference is one held-out episode, and section 7.2,
item 1, says which device's figure is the registered one (the review of
version 3, RT-232). The no-information level of this read is 0.072, about 13
of 180 (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 1, section
1.3). It also fails the learn-both gate: the named-other condition clears on
1 seed of 3 (section 4.4). So it fails twice over. **The number the
arithmetic would have returned (1.0000, 1.0000 and 1.0108) is withdrawn from
the record** under failure 2's rule and is not a reading; it appears in the
re-run's table in parentheses, labelled "reported for description; no
reading", only so that a reader can see what an empty instrument returns,
which is the entangled end. Every control figure for this arm in section 7.3
is taken at the site the rule would choose with the piece requirement
switched off, and carries the same label.

**What the free arm does instead of representing the label (ARGUED, the Gate
C review, RT-212, from `grammar.py` and the gate file).** It scores 0.5513 to
0.5597 on the own-directed condition against 0.2340 to 0.2383 for the
ownership-blind solver, and it collapses when the acting channel is removed
(0.1760 to 0.1940), so its ownership answer is load-bearing; but an
own-directed action can be solved by attending to the value tokens on the
turns the acting channel marked, with no need to know which marker word those
turns carry. That is why the route (b) investigation of section 7.2 looked for
a label the own-directed loss does force on a free system. The review of
version 3 saw the same thing directly: on the free arm the label is fully
readable from the whole state at the first token of the model's first own
turn and nearly unreadable at the action position (its RT-230, the side
observation), so the free toy model does not carry the marker word forward to
where it acts.

### 5.5 Seeds

**Three seeds per arm** (ruled 2026-09-25, the queue ruling, page 1f), giving
**twelve** registered runs across four arms. The registration says in terms
that the toy arithmetic implying one seed, the rehearsal's half-width
calculation, which the 2026-09-21 findings cautioned against carrying across
because the toy arms are far more repeatable than registered-size runs will
be (`docs/2026-09-21-successor-measure-rehearsal.md`, section 11), was not
carried across. The training recipe is the rehearsal's unchanged recipe; the
grammar attempt of section 4.4 did not clear, so nothing changes it.

---

## 6. The measure

### 6.1 The pairing

Episodes are generated in matched pairs that share a content seed and rotate
which agent the model is, machinery the registered generator already has. In
a pair, the **recipient** episode is the one the model runs; the **donor**
episode is its twin in which the model is a different agent. Because all four
agents assigned the item, **the value the donor's identity dictates is already
present in the recipient's own context.** So a successful transplant does not
import an answer from outside; it changes which of four in-context values gets
selected. This is the construction that lets the experiment tell apart
"the transplant moved who is acting" from "the transplant carried the answer
with it", which is the confusion the outside review warned about.

### 6.2 The two transplants

A **site set** is fixed before anything is read: a list of token positions and
a list of layers. At those sites:

- **Whole-state transplant.** Replace the entire running-state vector at each
  site with the donor's.
- **Ownership-only transplant.** At the same sites, replace only the part of
  that vector lying in the nominated ownership subspace, leaving the rest of
  the vector as the recipient had it.

The second is a restriction of the first to a subspace, not a smaller or
different intervention. That is deliberate: it means the measure reads *how
much of the identity-driven difference at these places lives outside the
nominated subspace*, and not *how many places you had to touch*. The
rehearsal's transplanting code proves the restriction as a tensor identity in
its self-test (rehearsal item R-8).

**Two kinds of site set are not an intervention on what the network built.**
Copying the running state at every position of a layer makes everything
downstream of that layer the donor's own computation, wherever ownership lives
only in the running state; copying every layer at every position is the
donor's forward pass outright. And copying layer 0, the state the acting
channel is added to, at positions spanning the turns the channel fires on, is
a transplant of the acting channel's own input rather than of anything the
network computed from it (the Gate C review, RT-216). Section 7.2 removes both
kinds from the candidate family by rule.

### 6.3 The number

For each arm, on fresh episodes:

- `accuracy_whole`: the share of transplant trials where the action is the
  value the donor's identity dictates, under the whole-state transplant.
- `accuracy_ownership_only`: the same share under the ownership-only
  transplant.
- `accuracy_untouched`: the same share with no transplant at all: the
  no-transplant rate. Section 6.4 says what it must be near.

**The reading is the chance-corrected form** (ruled 2026-09-25, the queue
ruling, page 2):

    degree = (accuracy_whole − accuracy_ownership_only) / (accuracy_whole − accuracy_untouched)

**with the raw difference and both accuracies always reported beside it**, and
the no-transplant rate with them. Zero means fully separable: transplanting
the ownership answer alone does everything transplanting the whole state
does. One means the ownership-only transplant did nothing at all: the act
resists being pulled apart at these sites. The separation bar (section 9, 1a)
and the floor (1c) are written on this scale.

**Why this form and not version 1's.** Version 1 divided by `accuracy_whole`
alone. A no-transplant rate that sits under both terms does not cancel in
that ratio, so the largest value version 1's reading could return was
different for every arm: the ceiling failure of Amendment A3 with the zero
replaced by a moving number (the Gate C review of version 1, finding RT-172,
the per-arm-ceiling finding, in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md`;
failure 1 of `docs/known-failure-modes.md`). The rehearsal confirmed it and
demonstrated the repair: on two made-up systems with the same true share
outside the subspace, 0.5, and different transplant strengths, version 1's
form read 0.4323 and 0.3222, and the chance-corrected form read 0.5018 and
0.5013 (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`, section
5, from `out/denominator_simulated.json`). The top of the chance-corrected
scale is 1 on every arm; section 17, failure 1, prints it for all twelve
toy arm-and-seed pairs under this version's rules.

**Readings outside 0 to 1 are reported as observed and never clipped** (the
repairs rulings, the paragraph after item 5). A negative reading means the
ownership-only transplant moved the action more than the whole-state one; a
reading above 1 means the ownership-only transplant landed below the
no-transplant rate. Both are sampling noise around "the subspace does
nothing" when small (arm C reads 1.0051 at one toy seed; the controls re-run
at `821f154`, section 2) and a warning about the instrument when large. The
rehearsal showed a negative value is reachable (rehearsal item R-4).

### 6.4 When the measure returns no verdict

The closed Amendment A3 design registered a comparison whose denominator was
zero from the day it was registered, and nobody noticed for four days after a
red-team pass had said so in plain words (ledger item RT-21, the unequal
ceilings finding). This measure has a denominator, so it gets explicit
no-verdict rules, written before it runs:

1. **The whole-state floor (ruled, the queue ruling, page 1c; refined by the
   repairs rulings, item 4).** A site set is usable only if the whole-state
   transplant clears **four fifths of the arm's own own-directed accuracy on
   the same fresh episodes**, written on the chance-corrected scale:

       accuracy_whole − accuracy_untouched ≥ 0.8 × (own_directed_accuracy − accuracy_untouched)

   The plain form, `accuracy_whole ≥ 0.8 × own_directed_accuracy`, is
   printed beside it everywhere, so a reader can see whether the two readings
   of the ruled sentence ever disagree; on the toy they never did (MEASURED: 0
   disagreements across all site sets, arms and seeds, the repairs findings at
   `882f252`, section 3; the re-run records both forms on every row,
   `out-v3-rules/measure_*_seed*.json`, `reading.floor`). *Turning the ruled
   sentence into the first form is this design's choice and is marked ARGUED
   in the repairs method note.* If no site set clears the floor for an arm,
   that arm returns **no verdict** at nomination, and that is recorded rather
   than repaired. The floor keeps the denominator away from zero by
   construction: on an arm that has learned the task,
   `own_directed_accuracy − accuracy_untouched` is large, and the denominator
   is at least four fifths of it.

   **The floor is applied twice, on different episodes (the review of
   version 3, RT-234, accepted 2026-10-03, page 3).** At nomination it is
   applied on development episodes, to decide which site sets are candidates.
   At the reading it is applied again, on the fresh episodes. **A site set
   that clears on development episodes and misses on fresh ones returns "no
   verdict: floor missed on fresh episodes"**; the nomination is frozen by
   then and is not redone. On the toy the two agree on all twelve arm-and-seed
   pairs, and the narrowest margin is arm F seed 0 on development episodes,
   0.4433 against 0.4280 needed, which is 9 episodes of 600 (MEASURED: the
   review, RT-234; the controls re-run at `821f154`, section 4, "the
   whole-state floor on fresh episodes clears on all twelve").
2. **The fit floor, on the piece that is transplanted (ruled, the rulings on
   the review of version 2, RT-212, item 1; applied per arm and seed, ruled
   2026-09-26 on decision 21; moved from the whole read to the piece by the
   rulings of 2026-10-03, page 1).** Only a size of piece whose own held-out
   accuracy reaches **four fifths** on development episodes may be chosen
   (section 7.2, item 3, gives the rule in full). An arm and seed with no
   size that reaches it returns **"no verdict, read failed its floor"**, and
   the transplant arithmetic is not reported as a reading. The piece's count
   and the whole read's count are both printed in the reporting table, with
   the label-permutation null beside them as a reference and not as the bar.
   **The floor is on the piece only (ruled 2026-10-03, late evening, ruling
   1).** The ruling of 2026-09-26 put the floor on the whole read, at the
   worst layer of the nominated site set. The morning ruling of 2026-10-03
   moved it to the piece and did not say whether the whole read must still
   clear four fifths in its own right. John ruled that it need not: the
   whole read's count is printed beside the piece's and is not a second
   condition. That is how the controls re-run ran
   (`experiments/rehearsal-successor-measure/src/rerun_controls.py`,
   `PIECE_MIN`; its method, rule 9). On the toy the two readings give the
   same twelve verdicts: every chosen piece's whole read is right on 176 or
   more of 180, and arm F misses both. They can differ in principle, because
   a piece can score above its whole read by an episode or two (on arm F seed
   1, 17 against 12; on the named agent's read of section 7.3, item 2, 139
   against 137). The alternative that was put and not taken: require both.
3. **The no-transplant sanity rule, with the review's formula and the
   allowance as re-worded (ruled, the Gate C rulings, RT-222).** Version 1
   said the no-transplant rate "should be near the one-in-eight guessing
   rate; if it is not, the pairing is broken and nothing is read". With
   distinct values that rule is pointed the wrong way round: a model that has
   learned nothing lands near one in eight and a model that has learned the
   task lands far below it (the Gate C review of version 1, finding RT-173;
   failure 3 of `docs/known-failure-modes.md`). The registered rule is the
   review's formula: with *p* the arm's own-directed accuracy on the same fresh
   episodes, the no-transplant rate should be near

       (1 − p) / 7

   because an untransplanted model lands on the donor's answer only by erring
   onto exactly that one of the seven other slots. **The rule carries room
   for a miss of at most the largest measured miss, rounded up to 0.018.**
   The largest miss the rehearsal measured against this formula was 0.017536,
   on the free arm at one seed (MEASURED:
   `docs/2026-09-21-successor-measure-rehearsal.md`, section 5, from
   `out/denominator_floor.json`); version 2 wrote the allowance as 0.0175,
   which that very case fails (the Gate C review, RT-222). On the repairs'
   fresh episodes every miss was inside 0.0132 (the repairs findings at
   `882f252`, section 6.4). A measured no-transplant rate more than 0.018 from
   the formula's value means the pairing is suspect, and nothing is read for
   that arm. **The detection margin at the bar is printed in the reporting
   table**: if a pairing is broken so that the donor's answer is unrelated to
   the recipient, an untouched model hits it one time in eight, and at an
   own-directed accuracy of 0.2633 (the learn-both bar) the formula gives
   0.1052, so the rule flags the broken pairing by 0.0198, a margin of only
   0.0018 over the allowance; at 0.56, the toy free arm's level, the margin
   is 0.0441 (MEASURED: section 17, failure 3). The mechanism is not changed
   this weekend.
4. **A reading outside 0 to 1** is reported as observed (section 6.3), not
   clipped and not suppressed.
5. **If a control that holds fails** (section 7.3: the null transplant,
   control 7; the content transplant, control 1, on arm T only; and the
   too-early-position control, control 4, as redefined), the reading is not
   made for that arm and seed. **A requirement on the registered code: it
   withholds the reading itself.** The toy re-run's code computed each of
   these as a true-or-false field and printed the reading regardless; every
   one passed, so no reading was printed that should not have been, but the
   withholding was left to the reader of the table (the check at `e184a6e`,
   section 4, item 3). In the registered code a failed control that holds, a
   no-transplant miss outside its allowance, or a floor missed on fresh
   episodes replaces the reading with "no verdict" and its reason, in the
   output file and in the table.

**The only subtraction anywhere in this design is of the measured
no-transplant rate, in the chance-corrected form of section 6.3, and nothing
wider.** No ownership-blind ceiling is estimated, subtracted or divided by
anywhere. (This sentence replaces version 1's "No normalisation by an
ownership-blind ceiling anywhere", as the queue ruling's page 2 directs: the
outside review's one-line warning still stands, and the programme has already
paid for the lesson once; what has changed is that the no-transplant rate is
a measured quantity of the pairing, not a ceiling, and subtracting it is what
gives every arm the same top of scale.)

---

## 7. The measurement procedure

### 7.1 Data split, and what "fresh" means

Three disjoint sets, generated from separate seeds and committed before use:

- **Training episodes**: what the arms are trained on.
- **Development episodes**: the only data on which anything is chosen: the
  site set, the nominated subspace, its rank, and any tuning at all. **The
  straight-line reads are fitted on development episodes, written to disk and
  reloaded**; they are never refitted on the episodes the reading is taken
  from (the rehearsal caught itself doing that and fixed it before any result
  was read: `docs/2026-09-21-successor-measure-rehearsal.md`, section 9, item 3).
  The fit of section 7.2, item 1, is scored on a held-out part of the
  development episodes (on the toy, the last 180 of 600), never on the fresh
  episodes.
- **Fresh episodes and confirmation seeds**: evaluated once, after the freeze.

**"Fresh" is disambiguated, as the rehearsal required** (its section 7, item
4). Version 1 asked for "marker and content combinations that appear in
neither of the other two sets", and that phrase has two readings. **The
registered reading is the weak one: unseen *combinations* of marker words,
items and values that the arm has each seen in training**, the rehearsal
grammar's pool named `fresh`, which draws from the training vocabulary with
its own seed (`experiments/rehearsal-successor-measure/src/grammar.py`, the
`POOLS` table). The strong reading, marker words the arm has never seen, is
**kept as a named diagnostic and is never the evaluation set**: under it the
separable arm's own accuracy fell to 0.7612, 0.6512 and 0.6512, the
whole-state transplant was capped there, and the reading went negative on two
seeds of three (MEASURED: `docs/2026-09-21-successor-measure-rehearsal.md`,
section 7, item 4; the pool named `unseen-vocabulary` in the same grammar
file). The registration says which reading it means in these words.

### 7.2 Choosing the candidate ownership representation: one instrument

On development episodes only, for each arm, **identically**: one function,
which takes no argument that names an arm, called the same way for every arm
(the repairs' `experiments/rehearsal-successor-measure/src/repairs.py` and the
re-run's `src/rerun_v3.py`, both at `9d9d31a`, and the controls re-run's
`src/rerun_controls.py` at `821f154`, do this, and their nomination tables
show one rule applied throughout). **The registration says in one
sentence that the rule's outputs differ per arm, and differ by seed within
arms C, F and M** (ruled, the queue ruling, page 3; MEASURED on the toy: arm C
is nominated at layer 2 at the action position, layer 1 at the action
position and the three before it, and layer 1 from the first own turn to the
action, on its three seeds; the controls re-run at `821f154`, section 3).

1. **The label, its route to the states, and the fit floor.** The
   straight-line read is fitted against **which marker word is the model's
   own**. *The route by which that quantity reaches the model's states, in one
   sentence:* the marker word is the input token at every turn the model's own
   assignments are spoken on, so it is carried by the token into the running
   state; and on an arm whose slot is built from it (arms T and M) or which
   multiplies it into content (arm C), the read recovers it at 0.96 or better
   from the first block onward. **What version 2's route sentence went on to
   claim, that which marker word is the model's own is forced by the loss at
   the own-directed action, is false for a freely trained system and is
   struck** (the Gate C review, RT-212): an own-directed action can be solved
   by attending to the value tokens on the turns the acting channel marked,
   without knowing which marker word those turns carry, and the toy free arm
   does exactly that (section 5.4). Ruled 2026-09-23
   (`docs/rulings/2026-09-23-nomination-label.md`; fixed in code as well as in
   text: the repairs code's `READ_LABEL = "marker-word"`, and the successor's
   measurement code when written, per the queue ruling, page 3). The label
   was ruled on the separable arm alone, which is the one arm whose slot is
   made of the label by construction (that ruling's section 4), and it is the
   only one of the three readings of "which agent is acting" that recovers a
   degree known independently of the instrument; the other two, the agent's
   slot and the marker's rank, put an arm whose degree is zero by construction
   at the entangled end of the scale.

   **The fit floor (ruled, the rulings on the review of version 2, RT-212,
   item 1; moved to the piece by the rulings of 2026-10-03, page 1, item
   1).** In the ruling's words: "only sizes whose own held-out accuracy
   clears four fifths may be chosen, and that accuracy is printed in the
   reporting table", beside the whole read's. "The accuracy of a piece is the
   held-out accuracy of a read given only the state's coordinates inside that
   piece, on the same development episodes and split as the whole read. An
   arm and seed with no size that clears returns 'no verdict, read failed its
   floor'." The floor is absolute, the same convention as the whole-state
   floor. The label-permutation null, the fit the whole read reaches when the
   labels are shuffled (two hundred shuffles at toy scale; its 95th and 99th
   percentiles), is reported beside it and is not the bar. The reason
   recorded in the ruling of 2026-09-26: a permutation null alone would
   likely certify a read at 0.172, which recovers the label on about one
   episode in six, and that is not an instrument worth transplanting. **The
   floor applies per arm and seed** (ruled 2026-09-26 on decision 21,
   recorded in the rulings file at `9ed9f8c`): an arm's three seeds are
   reported one by one, each a reading or a no verdict, and the across-seed
   spread of section 9 is taken over the seeds that read. The whole read's
   count is printed and is not a second floor (section 6.4, item 2).

   **How the accuracy is stated, and on what it is computed (the review of
   version 3, RT-232; accepted 2026-10-03, page 3, as the review states the
   fix).** Every fit in the registration and in the reporting table is
   **stated as a count of held-out episodes** (on the toy, of 180; the floor
   there is 144). **The registration names the device and the number format
   the registered fit is computed on, and the figure on that device is the
   registered one.** The reason: the floor is a hard line, per arm and seed,
   and on the toy two of twelve reads moved by exactly one held-out episode
   between the laptop's processor and its graphics chip (arm F, 32 against 31
   and 18 against 19; the other ten were identical; MEASURED: the review,
   RT-232; the controls re-run at `821f154`, section 3), so a fit within an
   episode or two of four fifths could pass on one device and fail on the
   other. **Ruled 2026-10-03, late evening (ruling 3):** the registered fit is
   computed on the laptop's **processor**, never its graphics chip; the
   model's states are computed in the model's own 32-bit floating-point
   format; the read is scikit-learn's logistic regression, which fits in
   64-bit; and the versions of torch, scikit-learn and numpy are recorded in
   the output file, as the controls re-run did (torch 2.12.1, scikit-learn
   1.9.0, numpy 2.5.0, `out-controls-rerun/summary.json`). **Reconciled
   2026-10-03 (night): those versions are also pinned, in a committed file
   named in the registration**, in the way `.venv-lock-2026-08-28.txt` does
   for the project's environment, so that a line read to one episode does not
   move because a library was upgraded between the registration and the
   reading (`docs/rulings/2026-10-03-version-4-questions-rulings.md`, ruling
   3; `docs/rulings/2026-10-03-seven-questions-reconciliation.md`). The processor is the device the
   controls re-run and the short pre-stated run, which supply every toy
   figure in this version, ran on. The alternative that was put and not
   taken: the graphics chip. **In the registered run the
   read is fitted once, on that device, written to disk and reloaded
   (section 7.1); the printed whole-read count and the transplanted
   directions come from that one fit.** On the toy re-run they came from two
   fits of the same read: the directions from the coefficients committed
   earlier on the graphics chip, and the printed count from a fresh fit on
   the processor (the check at `e184a6e`, section 4, item 2); on the built
   arms nothing turns on it.

   **The toy demonstration (MEASURED: the controls re-run at `821f154`,
   sections 2 and 3; reproduced by the check at `e184a6e`, section 3).** The
   floor returns no verdict on arm F and a reading on arms T, C and M. Right
   of 180 held-out episodes at the action position, whole read then chosen
   piece: arm T 180 and 180 on every seed; arm C 180 and 180, 177 and 172,
   176 and 150; arm M 180 and 180 on every seed; arm F 32, 12 and 18 for the
   whole read, with no piece above 34 at any layer or size. The lowest piece
   among those that clear is 150 of 180. The permutation null's 95th
   percentile sat at 0.111 to 0.128 (about 20 to 23 of 180) across all twelve
   pairs on the earlier re-run (`docs/2026-09-26-toy-rerun-v3-rules.md` at
   `9d9d31a`, Part 1, section 1.3; the check at `70be9fb`, section 3.2; that
   null is for the whole read, on the graphics chip, and was not recomputed
   on 2026-10-03). **One clause of the rulings file's refinement item 2 was
   wrong on this point and carries an annotation** (the rulings file at
   `da41c20`, pull request 68): it said that under the layer-0 removal "arms
   C and F still fall to the fit floor"; arm C does not, and only arm F falls
   to the floor. Nothing ruled depends on the clause.

   **The route (b) investigation, and what it found (the Gate C rulings,
   RT-212, item 3; the result ruled 2026-09-26).** Route (b) asked for a label
   the own-directed loss does force on a free system, which a straight-line
   read can recover on arm F at four fifths. The free-arm label search
   (`docs/2026-09-26-free-arm-label-search.md`, main line at `a97c12b`, pull
   request 66; laptop only, $0,
   nothing retrained, on the committed arm F models) tried three candidates
   under the registered site-set rule at toy scale, with a floor of 0.80 on
   held-out fit and a 200-shuffle label-permutation null at each site.
   **None clears the four-fifths floor on arm F, at any site set, on any
   seed.** The best is 0.789, from candidate 1 (which earlier turns are the
   model's own), and that from position spans that start at one of the
   model's own turns, so that where the span starts gives part of the answer
   away; anchored at the action position the three candidates reach 0.733,
   0.383 and 0.478. All three sit well above their shuffle null, so they are
   carried by the free arm, just not at the floor (MEASURED: the search's
   findings at `a97c12b`, sections 1 and 2; its check,
   `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md`,
   main line at `ecd2b6c`, pull request 70,
   recomputed every best fit, shuffle summary and verdict from the committed
   files with no disagreement, and confirmed the twelve models against the
   committed fingerprint list; its section 6 narrows the search's closing
   sentence to "none of three candidates chosen in advance", which is how it
   is stated here). **John's ruling of 2026-09-26 (the rulings file at
   `a11f1d3`, "RT-212 item 3 resolved", items 1 to 5): this version registers
   with the fit floor alone; the ruled label, which marker word is the model's
   own, stays the one registered read; the three candidates enter the toy
   record as exploratory fits, not as registered reads; the experiment
   proceeds; and the first release's single arm F run reports its nomination
   fit against the floor, a miss being a stop before the second release
   draws** (section 11, step 5a). The reason recorded there: the fits rising to
   0.79 above a 0.10 shuffle baseline on the small toy model is the argument
   that the deeper registered model may clear the floor, and $44 is the price
   of finding out before $130 is spent. **The depths, stated the same way in
   both places (the review of version 3, RT-236; accepted 2026-10-03, page
   3): the toy has four blocks and five running states; the registered model
   has twelve blocks and thirteen running states.** The ruling as recorded
   calls the toy "a five-layer model" and the registered one "twelve-layer",
   which counts states for one and blocks for the other; the rulings file
   carries a dated note beside the phrase and stands as recorded. Like for
   like, the registered model is three times as deep, not two and a half. **The search also printed a
   fit for the ruled label on arm F of 0.556, 0.483 and 0.433 over its 60 site
   sets, which is not the 0.172 the Gate C review and the re-run report. The
   check reconciled the two: they are different reads of the same models,
   episodes, split and fitter.** The registered rule fits one read per layer
   at the action position only and reports the worst layer of the nominated
   set; the search fitted one read per site set, with the layers and
   positions of the set laid end to end and the post-identity span averaged,
   and all three of its higher figures come from that averaged span at layers
   0 to 1 or 0, which starts at the model's own marker word and which the
   layer-0 removal of item 2 excludes. On the search's own cell for the
   registered read (layer 1, the action position) it prints 0.172, 0.067 and
   0.106 to the digit (MEASURED: the check at `ecd2b6c`, "Verdict" and section
   2). Item 3 registers which read is meant, so the two cannot be confused
   again; the 0.172 is the registered read's figure as the graphics chip
   computed it, and on the processor the same read is right on 32 of 180.

2. **Candidate sites: the rule, the printed list, and what is removed from the
   family.** The site list is registered as the rule that generates it
   (ruled, the queue ruling, page 1e), and the registration prints the list
   the rule produces for the registered 12-layer architecture beside the rule,
   with the count of comparisons it implies, so the family correction is
   pre-stated. **The rule has now been run at toy scale exactly as registered
   (ruled, the Gate C rulings, RT-215; MEASURED: the re-run findings at
   `9d9d31a`, Part 1), so every toy nomination, reading and control figure in
   this version comes from the family the rule generates**, which meets the
   review's objection that version 2's figures came from a hand-listed
   44-set family the rule never produced (the Gate C review, RT-215). The
   rule:
   - **Positions**, grouped into the position sets the rehearsal used and
     registered here by name (`experiments/rehearsal-successor-measure/src/rehearse.py`,
     `CANDIDATE_POSITIONS`; positions in `src/transplant.py`): the action
     position alone (`action`); **the action position and the answer-marker
     token just before it** (`action+ans`; version 2 described this set
     backwards, the Gate C review, RT-224); the action position and the three
     positions before it (`action+3`); every position from the model's first
     own turn to the action (`post-identity`). (The rehearsal's fifth set,
     every position, is excluded by the rule below.) **Ruled 2026-10-03 (decision 19): the
     position sets are the rehearsal's four, by name.**
   - **Layers**: every contiguous set of the model's running states, counting
     the state after the input embedding as one (layer 0) and each of the
     twelve blocks' outputs as one more: 13 states, 91 contiguous sets.
   - **The all-positions exclusion** (ruled, the repairs rulings, item 3):
     **any site set whose positions are all positions is excluded**, at any
     layer. The reason is section 6.2's: copying all positions at a layer
     hands the donor's whole forward pass downstream. On the four named
     position sets no site set spans every position in any episode (MEASURED:
     the re-run's `out-v3-rules/nominate_*_seed*.json`, field
     `family.share_of_episodes_where_position_set_spans_every_position`; the
     check at `70be9fb`, section 4.3), so on this family the exclusion removes
     nothing further.
   - **The layer-0 exclusion, as removal from the family (ruled, the Gate C
     rulings, RT-216, item 1, as clarified by refinement item 2).** Layer 0 is
     the state the acting channel is added to. **Every site set whose layers
     include layer 0 is removed from the candidate family before nomination
     at every position set other than `action`**, and the rule chooses again
     from what remains, in the way the all-positions exclusion works. Layer 0
     stays a candidate at the action position set only, where the constructed
     anchors' slot sits by construction. The reason: at position sets
     spanning the turns the channel fires on, the twins differ at layer 0 only
     by the channel's own input, so a whole-state transplant there is a
     transplant of the acting channel and not of anything the network built,
     and the subspace compared against it was, on arms C and F, a read fitted
     at 0.072 (the Gate C review, RT-216). **This reading of the ruling, that
     "excluded" means removed from the family and chosen again, was clarified
     after the re-run of 2026-09-26, with the re-run's figures in hand, and is
     not called pre-stated here**: the re-run's first pass read "excluded" as
     "reported as no verdict", recorded the removal reading as its own column
     before it ran, and put the choice to John, who ruled the removal reading
     on the same day (the re-run findings, Part 2; the check at `70be9fb`,
     sections 1.3 and 4.6). Under it, six of the nine toy nominations on arms
     C, F and M that the first pass had left at the injection move off layer
     0, every one to a single later layer (the re-run findings, Part 1,
     section 1.5). *Two readings of which position sets "span the acting
     turns" exist, and they give the same twelve toy nominations:* the ruling's
     first sentence keeps layer 0 at `action` only, which the re-run applied;
     its parenthesis names `post-identity` and any set including the marked
     turns, which on this grammar is `post-identity` alone (MEASURED: the check
     at `70be9fb`, section 4.4, by a script printed in its appendix C and not
     committed as a file). **This version registers the reading as run, layer
     0 kept at `action` only, 45 site sets on the toy and 325 on the
     registered model (ruled 2026-09-26 on decision 20)**; the narrower
     reading is recorded beside it as the alternative that was put and not
     taken. On the separable arms layer 0 inside
     the action turn does move the action (arm T's whole-state share there is
     1.000 against 0.000 untouched; arm M's about 0.40, short of its floor),
     so it is the rule's position-set order, `action` first, that decides the
     tie on arm T and not any property of the states (the check at `70be9fb`,
     section 5). Version 2's argument that those states are identical in the
     twins was wrong for arms T and M and is not repeated.
   - **The count.** With every contiguous layer set at the four position sets,
     the family is 60 site sets on the toy and 364 on the registered model;
     with the layer-0 sets removed at the three position sets other than
     `action`, **45 site sets and 180 comparisons on the toy, and 325 site
     sets and 1,300 comparisons on the registered model** at four rank caps.
     The narrower reading of decision 20 gives 55 and 220 on the toy, 351 and
     1,404 on the registered model; the stricter variant below gives 40 and
     160, and 312 and 1,248 (MEASURED: the review of version 3, "What was
     checked and held", recomputed all eight site-set counts by arithmetic
     on the rule; section 18 prints the registered list with its command). The ruled figures before the
     all-positions widening, 296 and 1,816, and version 2's 60 and 364, are
     superseded by these; the repairs rulings' annotation 4 records the first
     supersession. The list and the rule have to agree, and the registration
     prints both: **the list for the registered model is printed in section
     18**, generated by the rule and not typed by hand, with the command that
     generated it.
   - **The stricter variant, as a sensitivity row (ruled, the Gate C rulings,
     RT-216, item 3).** Every layer-0 site set removed at every position set,
     `action` included, then choose again. Reported beside the primary
     reading for every arm and seed, so John can switch to it with figures in
     hand before Gate A. On the toy it differs from the primary row only on
     arm T, whose site moves from layer 0 to layer 1 at the action position,
     rank 8, with fit 1.000 and reading 0.0000 on every seed; on arms C, F
     and M the primary nominations contain no layer 0, so the row is the same
     pick with the same numbers (MEASURED: the re-run findings, Part 1,
     section 1.3; the check at `70be9fb`, section 3.7). The reason recorded
     for not ruling it blind: it may move arm T's anchor read off the layer
     its slot was built at, which on the toy is exactly what it does.
3. **Candidate directions, and the read that supplies them, registered.**
   **The read the rule uses is one fitted straight-line read per layer, on
   the running state at the mask token of the own-directed action (the
   `action` position), labelled with the model's own marker word, fitted on
   the development episodes and scored on the held-out part of them** (in the
   rehearsal code, `repairs.fit_reads`: one logistic regression per layer, the
   same read whatever site set is later nominated). At each site set the
   directions transplanted are that read's leading directions at each layer
   in the set, at each of the rank caps **1, 2, 4 and 8**; **the registered
   cap is 8** and the search family reports all four (ruled, the queue ruling,
   page 1d).

   **The piece rule (ruled 2026-10-03, page 1; the review of version 3,
   RT-230, option (b)).** For each candidate site set and each size, the
   piece's own accuracy is computed: a fresh straight-line read given only
   the state's coordinates inside the piece, **at the action position**, on
   the same development episodes and the same split as the whole read; for a
   site set with more than one layer, the worst layer's. **A size is a
   candidate only if its piece is right on at least four fifths of the
   held-out episodes** (on the toy, 144 of 180). An arm and seed with site
   sets that clear the whole-state floor and no size that reaches four fifths
   returns "no verdict, read failed its floor". The alternative that was put
   to John and not taken: fixing the size at 8 directions with the smaller
   sizes as extra rows. **The requirement is applied after the layer set is
   chosen (item 4), so it decides which sizes may be chosen and never changes
   which layers are used (ruled 2026-10-03, late evening, ruling 2).** The
   re-run's method had marked that as its own reading, for John to overturn
   (`docs/controls-rerun-method-2026-10-03.md`, rule 7; the check at
   `e184a6e`, section 4, item 6); he confirmed it. The alternative that was
   put and not taken: letting the piece's accuracy also decide between layer
   sets, which has not been run. **Reconciled 2026-10-03 (night): what this
   order can miss, stated as the ruling requires.** The earliest layers at
   which the whole-state transplant works need not be layers at which the
   label can be read where the model acts. A model whose label is readable
   only at later layers returns "no verdict, read failed its floor" although
   a later layer might have passed. The report for the first full-size
   free-model run prints the accuracy at every layer and the candidates the
   rule chose among (section 11), so such a miss is visible when John rules
   at that stop (`docs/rulings/2026-10-03-version-4-questions-rulings.md`,
   ruling 2; `docs/rulings/2026-10-03-seven-questions-reconciliation.md`).

   **The piece's accuracy at the other positions of its site: reported both
   ways, gated in neither (ruled 2026-10-03:
   `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3, and
   `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`,
   ruling 2).** Where the chosen site set covers more than the action
   position, the same directions are transplanted at every position of it,
   and the four fifths above was established at one of them. So the
   reporting table prints, beside the piece's count at the action position,
   **(i) its count at each other position of the site, and (ii) its count on
   the average over those positions.** Neither has a pass line; the rule is
   unchanged. Each is computed as the short pre-stated run's method states
   (`docs/2026-10-03-short-prestated-run-method.md` at `9e978d9`, section 4):
   - **A count at a position** is computed exactly as at the action position,
     with only the position changed: the model's state at that position on
     the development episodes, its coordinates inside the piece, **a fresh
     read fitted at that position** on the same split, and the number of
     held-out episodes it gets right. It is not the action-position read
     carried over. The same count for the whole state at that position is
     printed beside it, so that a low piece figure can be told apart from a
     position where the label is not in the state at all.
   - **Which positions are reported one by one.** For the action position and
     the token before it: that one position. For the action position and the
     three before it: each of the three. For a site that runs from the
     model's first own turn to the action, whose length differs from episode
     to episode: **the five tokens of the model's first own turn, and the
     five tokens before the action**; the positions between them do not line
     up from one episode to the next and **are covered by the average only**.
     A site at the action position alone is printed as "single position".
   - **The count on the average** is the same count taken on the state
     averaged over every position of the site except the action position.
     **In the registered code that average is taken in 64-bit arithmetic.**
     The reason is the check of the short run, finding 11: on the toy, the
     same average of the same numbers added up in a different order moved the
     count by one episode of 180 on three of the eight figures (arm F seed
     0's whole state, 90 against 91; arm F seed 2's, 74 against 73; arm M
     seed 0's piece, 164 against 163), and in 64-bit arm F seed 0 gives 92
     and 24. The check offered two ways to deal with it, saying the figure is
     good to an episode or two, or fixing the arithmetic; this draft does
     both, and the choice of 64-bit is this draft's. **The toy figures on the
     average quoted in this version are therefore good to an episode or
     two.** The per-position counts did not move.
   - For a site set with more than one layer, the worst layer's figure.
   - **How much of a span the ten named positions cover:** a span from the
     first own turn to the action runs 16 to 53 positions on the toy, 39.2 on
     average, so the ten positions reported one by one are about a quarter of
     it, and the rest is seen only through the average (the check of the
     short run, finding 14).

   **This computation rests on John's own words.** The evening ruling
   recorded it as ruled from "print both figures", which accepts it by
   implication only; the check of that record said so (its finding 19), John
   was asked, and he answered "Yes, section 4 of the method is what I meant"
   (a dated note beside item 3 of the ruling record, main line at `53c8100`).

   *What the toy shows (MEASURED, **checked: the check of the short run at `53c8100`**:
   `docs/2026-10-03-short-prestated-run.md` at `853988f`, section 4, from
   `out-short-prestated-run/part_b.json`; each cell is whole state then
   piece, right of 180).* Arm T on every seed and arm C seed 0: single
   position. Arm C seed 1: 180 and 139, 179 and 139, 179 and 33 at one, two
   and three positions before the action; 179 and 113 on the average. Arm C
   seed 2: the piece between 30 and 139 at the ten positions, the whole state
   between 149 and 180; 180 and 123 on the average. Arm M: the piece at 144
   or more at four, four and seven of the ten positions on seeds 0, 1 and 2,
   and as low as 34, 71 and 33 at the fourth token of the first own turn;
   180 and 163, 180 and 174, 180 and 175 on the average. Arm F, described
   only: the piece between 11 and 36 everywhere except the first token of
   the first own turn on seed 2 (145), which is the model's own marker word
   itself. The action-position counts recomputed by that run equal the
   controls re-run's on all twelve. **A limit of these figures, from the
   run's own findings:** each is a fresh read fitted on 420 episodes with
   twelve possible answers, in a piece of 4 or 8 directions; a figure like
   139 against 144 is a few episodes and should not be read finely. **A nominated site set's fit, for the floor of item 1, is the
   fit of the worst layer in the set**, as the re-run's verdict code reports
   it; on the toy no nomination has more than one layer, so this has not yet
   bitten. **What is not the registered read:** a read fitted per site set,
   with the states of every layer and every position in the set laid end to
   end and a multi-position span averaged over its positions, which is what
   the route (b) label search fitted (its `site_features`). That is a
   different quantity, it can score far higher on the same models (0.556
   against 0.172 on arm F seed 0, item 1), and nothing in this design uses it
   (the label-search check at `ecd2b6c`, section 2, which traced both reads
   through the code).
4. **The layer set for the whole-state transplant: "the smallest that clears
   the floor", in one reading** (ruled, the repairs rulings, item 4). For each
   position set, the layer set with the fewest layers that clears the
   four-fifths floor of section 6.4, ties going to the earliest layers; a
   position set with no clearing layer set drops out. The other reading, the
   highest ownership-only share over every clearing site set, is computed and
   printed beside it as a sensitivity row, **and that repairs-style row is the
   sensitivity row this version means** (the check at `70be9fb`, section 4.3,
   asked for the row to be named). On the repairs run's 44-set family the two
   readings picked different site sets on **8 of 12 arm-and-seed pairs, and
   the ownership-only shares they reached differed on 7 of 12**, by 0.02 or
   less (MEASURED: the Gate C review, RT-218, which resolved version 2's two
   counts; the repairs rulings' annotation 3, which adds that the check's
   re-run gave 6 of 12, so about half the pairs, by about 0.02, is what both
   runs support). On the re-run's 60-set family, no primary nomination is a
   multi-layer set, and the sensitivity reading picks a multi-layer set on five
   of twelve pairs (MEASURED: the re-run findings at `9d9d31a`, Part 2, first
   pass, section 5). The ruling's condition, that a nomination moving to a
   multi-layer set the hand list never tried be reported, did not fire.
5. **Nominate by causal effect, not by how well the read fits.** Over the
   surviving (position set, its smallest clearing layer set) pairs and the
   sizes whose piece clears the floor (item 3), the nominated configuration
   is the one with the highest *development-set ownership-only transplant
   accuracy*; ties go to the smaller size, then the earlier position set.
   This is the main lesson of the closed design: a representation that a
   straight-line read recovers beautifully can do nothing when you intervene
   on it. **What changed on 2026-10-03:** version 3 applied the fit floor to
   the nominated configuration afterwards; under the piece rule the floor is
   applied before the choice, as a limit on which sizes may be chosen. Among
   the sizes that pass, the choice is still blind to how well any read fits.
   **On an arm where nothing moves the action, that choice is made among
   sampling noise, and the registration says so** (the review of version 3,
   RT-230 and RT-235): on arm C the development shares at different sizes and
   sites differ by one or two episodes of 600, and on seed 1 one episode
   decided the site (section 5.2). What the piece rule secures is that
   whichever candidate wins, its piece holds the label at the action
   position. It does not make the pick stable.
6. **Arm T's known ownership slot is not handed to the procedure.** The
   nomination runs blind on every arm, so what is validated is the whole
   procedure and not just the arithmetic at the end. The reading obtained by
   handing the procedure arm T's true slot, and arm M's, is computed and
   reported separately as a reference; on arm M that reference is the formula
   of section 5.3 written in route accuracies, one check and not two (the Gate
   C rulings, RT-223). On the toy the true-slot reading is 0.0000 on arm T
   and 0.4837, 0.4760 and 0.4920 on arm M (the controls re-run at `821f154`,
   section 4). Ruled 2026-09-25 (decision 1).
7. **The rider, in the reporting table** (ruled: John's addition, the queue
   ruling, page 3; kept in the table by the repairs rulings). For every arm
   and seed, the reading is also taken at **arm T's** nominated site set and
   rank for the same seed, using that arm's own read fitted at those sites,
   and reported beside the reading at the arm's own nomination, so a reader
   can see whether what differs between arms is their degree or where the
   procedure looked. **Where the whole-state transplant at arm T's site set
   misses the floor, the rider returns "no verdict", and the report says
   which of two things that means.** On the toy it returned no verdict for
   arms C, F and M on every seed, for two different reasons (ruled, the Gate C
   rulings, RT-225): on arms C and F, at layer 0 at the action position,
   nothing about ownership has yet reached those arms' running states, and
   the whole-state transplant lands on the no-transplant rate (0.0512 to
   0.0600 on arm C, 0.0563 to 0.0688 on arm F); on arm M, which carries arm
   T's slot, the whole-state transplant there moves the action in about 0.41
   of trials against about 0.01 untouched, and the no verdict is **a miss of
   the four-fifths floor**, not nothing reaching the state (MEASURED: the
   repairs findings at `882f252`, section 3, "The rider"; the Gate C review,
   RT-225; the repairs rulings' annotation 5). Arm T's site set is layer 0 at
   the action position on every seed under the registered rule, the same site
   the repairs run nominated, so these rider figures stand under the rule,
   and the controls re-run found them again: the whole-state share at arm T's
   site is 0.0512, 0.0488 and 0.0600 on arm C, 0.0587, 0.0563 and 0.0688 on
   arm F, each the no-transplant rate, and 0.4088, 0.4138 and 0.4100 on arm M
   (the controls re-run at `821f154`, section 2, the last column).

### 7.3 Controls

Every one of these is run on every arm. **Three of them hold**, and a failure
means the reading is not made for that arm and seed: control 7 (the null
transplant), control 1 on arm T only, and control 4 (the too-early-position
control, as redefined on 2026-10-03). **The rest are reported** beside the
reading and cannot veto it. Version 2 made control 3 hold as well, and
version 3 made control 4 reported; this version does neither, for the reasons
under items 3 and 4. **The registered code withholds a reading when a control
that holds fails; it does not only print true or false** (section 6.4, item
5).

**All of them now have figures under the registered rules.** Version 3 had
none for controls 1, 2, 4 and 6 on arms C, F and M at the site sets the rule
nominates, and the review of version 3 made that a precondition of the
registration review (RT-233; ruled 2026-10-03, page 2). The controls re-run
of 2026-10-03 ran controls 1, 3, 4, 6 and 7, the true-slot reference, the
rider and the stricter row on all twelve toy models, with its method and code
committed before its output (`docs/2026-10-03-controls-rerun.md` at
`821f154`); a session that did not run it ran it again from the committed
code and found every one of about 26,700 values equal (the check at
`e184a6e`, section 3). Control 2 has no figure and cannot have one at toy
scale (item 2). Arm F's figures are taken at the site the rule would choose
with the piece requirement switched off and are labelled "reported for
description; no reading" (the re-run's method, rule 12).

1. **Content transplant, re-worded so it cannot veto the entangled arm.**
   Transplant the complement of the nominated subspace at the same sites.
   *On arm T it holds*: the action must not follow the donor's identity above
   the no-transplant rate plus the 0.018 room of section 6.4 (on the toy:
   0.0000 on every seed). *On arms C, M and F it is reported and cannot
   veto.* On an entangled arm the complement carries the ownership signal by
   construction, since in a system where ownership multiplies content at
   every layer there is no ownership-free complement to transplant, so on
   such an arm the complement is expected to reproduce the counterfactual
   almost as well as the whole state does. On the toy it does: arm C's
   complement moves 0.5450, 0.5625 and 0.5312 of trials against whole-state
   shares of 0.5400, 0.5550 and 0.5463; arm M's moves 0.3875, 0.3762 and
   0.4288 against about 0.78, about half, which is what a mixture would give
   (ARGUED); arm F's, for description only, 0.4838, 0.5637 and 0.5400 against
   0.4850, 0.5675 and 0.5300 (MEASURED: the controls re-run at `821f154`,
   sections 2 and 4). As version 1 wrote it, this control would have vetoed
   the reading on exactly the arm the control battery exists to validate, and
   on arm F it would have vetoed whatever the free arm turned out to be,
   which is the thing being measured. Its value on arms C, M and F is a
   description of how much of the identity-driven difference lives outside
   the nominated subspace, which is the reading itself seen from the other
   side.
2. **Another agent's representation: a reported description with no pass
   line; not applicable on arms T and M (ruled, the repairs rulings, item 5;
   and `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 1).**
   Nominate, by the identical procedure with the named agent's marker word as
   the label and the named-other action as the anchor, a representation of
   the named agent who is not acting, and transplant it from a twin that
   differs only in which agent is named. **What is reported: how often the
   own-directed action moves under the named agent's piece, beside how often
   it moves under twenty random pieces of the same size at the same sites,
   reported as control 3 reports its twenty (median, 95th percentile, and
   the counts below, equal and above).**
   - **It has no pass line.** Version 3 proposed a tolerance of 0.05 over the
     random piece (its decision 15); John agreed to it on the morning of
     2026-10-03 and withdrew it the same day after the controls re-run. No
     number is registered for this control, so nothing about it is a
     pre-stated quantity the rehearsal failed to exercise, in the sense of
     item 5 of the 2026-09-21 ruling.
   - **The registration says in terms: this control never ran at toy scale.**
     It runs only on an arm that has learned the named-other condition
     (passes the section 8.1 bar on it), and only where a piece of the named
     agent's read reaches four fifths. Arms T and M are not applicable by
     ruling: they hold the named agent outside the running state by
     construction, so no transplant into the state can move that action. Of
     the other six toy models, five have not learned the named-other
     condition (arm C at 760, 751 and 708 of 3,000 and arm F seeds 1 and 2 at
     781 and 746, against 790). The one that has, arm F seed 0 (994), has a
     read of the named agent's marker that misses the floor: the whole read
     is right on at most 137 of 180 held-out episodes and the best piece on
     139, against 144 needed (MEASURED: the controls re-run at `821f154`,
     section 5, from `out-controls-rerun/measure_F_seed0.json`, `control2`;
     the check at `e184a6e`, section 3). That would have been a no verdict
     under version 3's rule too. Four attempts to repair the named-other
     condition have not produced a toy model that learns it (section 4.4).
   - **A no verdict is the expected result at registered scale too**, and is
     reported as "no verdict" with which of the two reasons applies.
   - **The part of its code after the floor has run once, and that run is NOT
     A RESULT.** The function has three early exits, and the controls re-run
     took all three: "not applicable" on the six separable and mixed models,
     "has not learned" on five, and the floor on arm F seed 0. What had never
     run was everything after the floor (the check of the short run, finding
     15). So that the registered run is not the first time that code
     executes, the
     re-run's own function for the control was called once on arm F seed 0
     with the piece's accuracy floor switched off for that one call, at $0.
     It ran without error and returned its figures: a site at layer 1, the
     action position and the three before it, 8 directions, a piece right on
     92 of 180 (the floor would have asked for 144); the own-directed action
     moved in 0.0012 of trials, under a random piece in 0.0063, and the
     named-other action in 0.0962. **Those figures are evidence that the code
     ran. They are not a pass or a fail of anything**, because the piece
     transplanted is not known to carry the named agent at all (**NOT A
     RESULT**, and **checked: the check of the short run at `53c8100`**:
     `docs/2026-10-03-short-prestated-run.md` at `853988f`, section 5, from
     `out-short-prestated-run/part_c_NOT_A_RESULT.json`). What is still true
     after it: the control has never been exercised on a model whose read of
     the named agent clears its floor.
   - **Twenty random pieces, not one (ruled 2026-10-03, late evening, ruling
     5).** The re-run's code compares against a single random piece, drawn
     with its own seed (the check at `e184a6e`, section 4, item 4). John
     ruled that the registered description uses twenty. **That is a change to
     the control's code, owed with the registered measurement, so the code
     path that ran once on 2026-10-03, with a single random piece, is not
     quite the one registered.** The alternative that was put and not taken:
     leave it at one draw.

   The alternative that was put to John and not taken: exercising the control
   on a made-up case built for the purpose. This is the successor's own
   obligation, not the closed design's control run on 2026-09-21 (the review
   of version 1, finding RT-181).
3. **Matched random subspaces: the twenty-draw null. Reported, not gated
   (ruled, the rulings on the review of version 2, RT-214, items 1 and 2, as
   refined on 2026-09-26 by refinement item 1).** Twenty random subspaces of
   the same rank and the same norm at the same sites are each transplanted in
   place of the nominated subspace, on every arm and seed. The reporting
   table prints the median and 95th percentile of the twenty random donor
   shares, the ownership-only transplant's own donor share, and how many of
   the twenty draws fall below, equal and above it. The fixed 0.0175 room of
   version 2 is dropped from this control. **The reason it is reported and
   not gated, as recorded in the refinement: a gate on this control cannot
   pass a separable arm and an entangled arm in the same direction.** An
   entangled arm's ownership-only transplant is meant to move nothing, so it
   can never beat random subspaces; on the earlier re-run's first pass, which
   gated on it, arm C seed 0's read fit at 1.000 and was blocked only by this
   control (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, Part 2,
   first pass, sections 6.2 and 7). Its job of catching a leaky site set is
   done by the whole-state floor and the no-transplant rule. **This reporting
   rule was clarified after the re-run of 2026-09-26, with the first pass's
   figures in hand, and is not called pre-stated here** (the check at
   `70be9fb`, section 1.3). *What the toy shows (MEASURED: the controls
   re-run at `821f154`, sections 2 and 4):* on arms T and M the
   ownership-only transplant sits above all twenty draws on every seed (arm M
   0.37 to 0.41 against random medians of 0.015 to 0.019); on arm C it sits
   below all twenty on seed 0 and among them on seeds 1 and 2; on arm F it
   sits among the draws on every seed, which is consistent with a piece that
   holds nothing, though arm F's verdict comes from its floor and not from
   this control.
4. **Positions before both twins' first own turns. Holds (ruled 2026-10-03:
   `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 2, which
   reverses that morning's ruling on version 3's decision 16).**
   - **What is run.** At the layers of the arm's nominated site set, the
     donor twin's whole state is transplanted into the recipient at every
     position before the earlier of the two twins' first own turns. A twin's
     first own turn is the first position at which its acting channel is on.
     The control takes the site set's layers and not its positions.
   - **The pass line: the transplant changes nothing.** The model's outputs
     at its two action positions (its scores over the vocabulary there, which
     is what the null transplant has always compared) with the transplant are
     compared with the same outputs without it, on every pair, and must be
     bit-identical. "Outputs" here and wherever this control is described
     means those, and not the outputs at every position (the check of the
     short run, finding 7). Reported
     beside it: the share of trials landing on the donor's value with the
     transplant, the no-transplant share, and the number of trials whose
     action changed. **A failure withholds the reading for that arm and
     seed.**
   - **What this control is, said plainly: a known-answer test of the pairing
     and of the code, like the null transplant.** The twins are the same
     text. They differ only in which turns carry the acting channel. The
     models read left to right. So until one twin's channel first comes on,
     both have had exactly the same input, their internal states are the same
     numbers, and transplanting one into the other puts back what was already
     there. **It cannot fail on a correctly built model with correctly built
     pairs, and a pass says nothing about any model.** It is right that a
     failure withholds a reading, because a failure means the pairing, the
     left-to-right property or the transplant code is broken. It is not
     evidence that a model does not yet know its identity at those positions,
     and no report of this experiment describes it that way.
   - **What is withdrawn.** Version 3 defined this control on the positions
     before the *recipient's* first own turn, found it above the
     no-transplant rate on arms C and F, and explained that by saying those
     arms "receive the ownership signal by other routes at those sites".
     **That sentence is withdrawn** (ruling 2, item 3). The control as then
     defined was transplanting at positions where identity was already known,
     in the donor: in 407 of 800 matched pairs (0.5088) the donor twin's
     first own turn comes before the recipient's. Under that definition the
     re-run found the control above the no-transplant rate by 0.065 to 0.10
     on six of the twelve toy models and by 0.005 or less on the other six
     (MEASURED: the controls re-run at `821f154`, section 6).
   - **The evidence the redefinition rests on.** The diagnostic that
     suggested it was written after the re-run's output was seen and was not
     pre-stated (`src/posthoc_control4.py`). The ruling said that if the
     check of the re-run found the diagnostic wrong, the ruling returned to
     John. The check did not find it wrong. With separately written code that
     shares only the episode generator, the model loader and the model's
     forward pass, it found on all twelve models: the twins' inputs and
     states are identical before both first own turns, at every layer; the
     outputs with the redefined transplant are bit-identical to the outputs
     without it; and all of the old definition's excess is in the pairs where
     the donor's first own turn comes first (MEASURED: the check at
     `e184a6e`, section 5, from its script `independent_control4.py`).
   - **The pre-stated run the ruling required** (method and code committed
     before output, by a session that did not write the diagnostic): the
     redefined control **holds on all twelve toy models**. The outputs are
     bit-identical; the donor-value share equals the no-transplant share on
     every line; no trial's action changes; a null transplant at the same
     positions is bit-identical; and across the 800 pairs the control
     transplants at between 1 and 21 positions per pair, about 5 on average,
     never none, so it is never an empty test (MEASURED, **checked: the check of the short run at `53c8100`**: `docs/2026-10-03-short-prestated-run.md` at
     `853988f`, section 3, from `out-short-prestated-run/part_a.json`). The
     method said in advance that this was not a blind prediction: the session
     had already observed it with different code while checking the re-run.
     **The check of that run** ran it again from the committed code and got
     byte-identical output files, found the same thing with separately
     written code at all five running states of every model, and showed the
     test is not empty: with random noise added to the donor's state at the
     same positions the outputs change on all twelve models, so the
     transplant does write there, and it changes nothing in the real control
     because what it writes is what was already there (findings 4, 8 and 9).
     **One limit the check records on the word "pre-stated"** (finding 3):
     the record shows that the method and code were committed and pushed
     before the output, 2 minutes 39 seconds apart; no committed file can
     show that the script was never run before the method was committed.
     Little turns on it, because this control cannot fail on correctly built
     pairs whenever it is run.

   The alternative that was put to John and not taken: redefining the
   positions and keeping the control reported only.
5. **Fresh marker and content combinations**, per section 7.1. By construction.
6. **Who is acting, versus which value. Reported, on the relaxed set.** The
   discriminating control. Trials are split into pairs whose donor identity
   dictates *the same* value as the recipient's and pairs where it dictates a
   *different* value. A transplant that has moved who is acting changes the
   action in the second group and not the first; a transplant that has
   smuggled a value across changes the action in both. **The first cell is
   empty by construction on the distinctness-preserving grammar** (0 of
   4,000 trials: MEASURED, `docs/2026-09-21-successor-measure-rehearsal.md`,
   section 5, from `out/denominator_control6.json`; the Gate C review of
   version 1, finding RT-173; failure 3 of `docs/known-failure-modes.md`), so
   control 6 runs on the **separately generated relaxed set** of section 4.2,
   in which one item per episode has two agents sharing a value. On that set
   both cells have trials: 81 same-value and 719 different-value trials of 800
   per arm and seed on the toy, on all four arms (MEASURED: the `controls`
   fields of `out-repairs/measure_base_*.json` at `882f252`; section 17,
   failure 3, prints them). Both cells are pre-stated and both are reported,
   with the one-in-four reference for a solver that cannot tell which agent it
   is restated for the relaxed set, where it rises (on the toy, from 0.2467 to
   0.3095 on exactly the trials the relaxation adds; the 2026-09-21 rehearsal,
   section 5). Pre-stated expectation: the separable arm moves nothing in the
   same-value cell and everything in the different-value cell; an entangled
   arm is expected to move the same-value cell too, and that is reported as
   the caveat it is (weakness W11): on those arms the whole-state transplant
   carries something besides identity. *What the toy shows under the
   registered rules (MEASURED: the controls re-run at `821f154`, sections 2
   and 4):* arm T moves 0.0000 of the same-value cell and 1.0000 of the
   different-value cell on every seed; the same-value cell moves on arm C
   (0.5062, 0.6296 and 0.5679), on arm M (0.2222, 0.2716 and 0.3210) and, for
   description, on arm F (0.7284, 0.6790 and 0.6296); the different-value
   cell moves in 0.82 to 0.95 of trials on those three arms.
7. **Null transplant. Holds.** Transplant the recipient's own state into
   itself. Every logit must be bit-identical. This is the known-answer test
   for the transplanting code and it runs before any result is read. **On the
   toy it holds at every place it was run, fifteen different places:** the
   twelve primary site sets (arm F's three being the described ones) and the
   three stricter-row site sets that differ from their primary, which are arm
   T's (MEASURED: the controls re-run at `821f154`, section 4; the check at
   `e184a6e`, section 3, which corrects the re-run's own count: its "twelve,
   nine and three" names fifteen different places, not twenty-four). That
   closes the citation gap version 3 recorded, that the null transplant had
   not been run at the site sets that changed. It is run again at the
   registered site sets before any registered reading.

**The ordinary competing solver has not yet been measured under the piece
rule, and it will be before the registration review opens (ruled 2026-10-03,
late evening, ruling 7).** The controls re-run did not load the
ownership-blind solver's three models, and read the gate from the committed
file (the check at `e184a6e`, section 4, item 8). The figures section 8.1
quotes for that solver and for the name-only solver are their accuracies on
the two conditions, from `out-repairs/gate_base.json` at `882f252`, taken
before the piece rule existed. Those are accuracies on the task and do not
pass through the nomination, so the piece rule does not change them; but
neither solver has been put through the nomination and the transplants under
the rule as now registered. **What is owed:** the ownership-blind solver's
three committed toy models, put through the nomination and the reading as
section 7.2 now states them, on the laptop at $0, with the method committed
before the output, by a session other than the one that drafted this
version, and checked like any other run. **The expected result, stated now:
no verdict**, because a solver with no acting channel should have no read of
its own marker word that reaches four fifths. **This version quotes no figure
for it. When the run is done its result is written in here, and until then
this text does not go to the registration review.** The alternative that was
put and not taken: state in the registration that it was not measured, and
leave it to the reviewer. In the registered experiment both solvers are
scored on both conditions on the registered episodes, as section 8.1 says.

### 7.4 What is frozen, and when

Committed to git, with the commit hash recorded in the registration file,
**before a single fresh episode is evaluated**:

- the label (which marker word), in code and in text, as the one registered
  read; the three route (b) candidates recorded as exploratory fits and not
  frozen as reads;
- **the fit floor: four fifths of held-out development episodes, on the piece
  that is transplanted and on the piece only, at the action position, stated
  as a count; the device the registered fit is computed on, the laptop's
  processor, and its number format (section 7.2, item 1);
  and the permutation null beside it**;
- **the piece's accuracy at the other positions of its site, both ways (each
  position, and the average over them), as reported figures with no pass
  line, and the method by which each is computed** (section 7.2, item 3);
- the site-set rule of section 7.2, the printed list it produces for the
  registered architecture (section 18), its two exclusions (all positions;
  layer 0 away from the action position set, as removal from the family), and
  the count of comparisons;
- the stricter layer-0 variant, as the sensitivity row;
- the rank caps (1, 2, 4, 8) and the registered cap (8);
- the nominated subspace and its size, per arm and seed;
- the whole-state layer set, per arm and seed, under the one registered
  reading of "the smallest that clears it", with the repairs-style sensitivity
  row named;
- the transplanting operation, as code, with its self-tests;
- all seven controls, and which hold: **control 7; control 1 on arm T;
  control 4 as redefined, on the positions before both twins' first own
  turns, with its pass line that the outputs are bit-identical**; the
  twenty-draw null of control 3 and its reported statistics; **control 2 as a
  reported description with no pass line, against twenty random pieces, with
  the statement that it never ran at toy scale**; the pre-stated cells, the relaxed set for control 6 and
  its generating seed;
- **that the code withholds a reading when a control that holds fails**
  (section 6.4, item 5);
- the whole-state floor rule (four fifths, on the chance-corrected scale,
  applied on development episodes at nomination and again on fresh episodes
  at the reading) and the no-verdict rules of section 6.4, including the
  no-transplant formula, its 0.018 room and the detection margin printed at
  the bar;
- the separation bar between R1 and R2 (0.5);
- **the five registered outcome terms of section 3, and what a no verdict on
  each arm maps to**;
- the gates of section 8: the own-directed bar on arms T, C and M, the
  learn-both bar on arm F, and the ownership-lesion rule with its two-of-three
  clause;
- the uncertainty method (section 9, 1g) and the seed count (three);
- **the numbers of episodes at the registered size, which are the toy's
  (ruled 2026-10-03, late evening, ruling 4): 600 development episodes with
  the last 180 held out for every fit, so the floor is 144 of 180; 800 fresh
  matched pairs; 800 pairs on the relaxed set; 3,000 held-out episodes for
  the gates, so the bar is 790; 200 shuffles for the permutation null**;
- **(reconciled 2026-10-03, night) the band that sampling alone puts around
  every count taken against the four-fifths floor, printed beside it; the
  committed file that pins the library versions; and the separation as the
  lowest of arm C's readings minus the highest of arm T's**
  (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`);
- **the rule for an arm whose seeds disagree: two of three, the third
  reported** (section 3);
- the reporting table's columns (section 7.5), including the rider;
- the predictions: arm T near zero; arm C high; arm M between 0.3 and 0.7 and
  within 0.10 of its true-slot reading on the same fresh episodes; arm F
  unknown and not predicted, and possibly no verdict.

Nothing on that list may be changed afterwards. If something on it turns out
to be wrong, the registered output is reported as it stands and the correction
is a separate, dated note beside it, the programme's existing practice, and
the process correction the outside review asked for: an immutable registration
is not an immutable scientific conclusion, but the two are kept visibly apart.

### 7.5 The reporting table

One row per arm and seed, with these columns, in this order, so that every
number a no-verdict rule or a caveat depends on is beside the reading it
bears on:

1. the nominated site set (layers, position set, size of piece);
2. **the whole read's held-out count at the nominated layer, and the chosen
   piece's own held-out count at the action position, each as a count of
   held-out episodes on the registered device, with the permutation null's
   95th and 99th percentiles beside them** (RT-212, RT-230, RT-232);
3. **the chosen piece's count at each other position of its site, and its
   count on the average over those positions, each with the whole state's
   count beside it; reported, with no pass line on either** (ruled
   2026-10-03; section 7.2, item 3);
4. whether the fit floor passes, **with the band that sampling alone would
   put around the count printed beside it** (reconciled 2026-10-03, night:
   at 180 held-out episodes one episode is 0.0056, and a piece whose true
   accuracy is exactly four fifths passes about half the time);
5. the whole-state, ownership-only and no-transplant accuracies on fresh
   episodes, the raw difference, and whether the whole-state floor clears in
   both forms, **on development episodes and again on fresh ones** (RT-234);
6. the no-transplant miss against the formula of section 6.4, **and the
   detection margin at the bar** (RT-222);
7. **control 3's twenty-draw null: median and 95th percentile of the random
   donor shares, the ownership-only share, and the counts below, equal and
   above** (RT-214);
8. the reading on the chance-corrected form, or the no verdict with its
   reason;
9. **the stricter layer-0 row**: the same columns with every layer-0 site set
   removed (RT-216);
10. the repairs-style sensitivity row for the whole-state layer set;
11. the rider: the reading at arm T's site set, or its no verdict with which
    of the two reasons applies;
12. the true-slot reference on arms T and M;
13. **the controls that hold, each with its pass or fail: control 7; control
    1 on arm T; control 4 as redefined, with the donor-value share, the
    no-transplant share and the number of trials whose action changed**;
14. **the controls that are reported: control 1 on arms C, M and F; control 2
    as a description (the own-directed action's share moved under the named
    agent's piece, beside twenty random pieces), or its no verdict with the
    reason; control 6's two cells**, each with its pre-stated expectation
    where it has one;
15. the ownership-lesion result;
16. and, across the three seeds of each arm, the across-seed spread of the raw
    difference with the within-seed bootstrap beside it (section 9, 1g).

**The report for the first full-size free-model run (step 5a of section 11)
prints more than its row (the review of version 3, RT-235; accepted
2026-10-03, page 3):** the read's held-out count at every layer, the chosen
piece's own count, and the candidates the nomination chose among. The reason:
on a model where no transplant moves anything, the layer the nomination lands
on is picked among sampling noise, so the stop of step 5a must not be decided
on one number from an arbitrary pick. The procedure has already computed all
three.

---

## 8. The gates every arm passes before it is read

### 8.1 The gate on learning: own-directed only on the constructed arms, both conditions on arm F

**The constructed arms T, C and M are gated on the own-directed condition
only; arm F keeps the learn-both gate (ruled, the Gate C rulings, RT-213,
item 1, refining the queue ruling's page 1b as it applies to arms T, C and M;
the bar itself is unchanged).** The reason recorded: the anchors' ownership
slot is built in by construction, their reading uses only the own-directed
action, and the named-other gate tests whether a free system learned to
represent ownership, which the anchors are not asked to prove. Arm F is not
read mechanistically until it has learned **both** conditions.

- Measured on held-out episodes, at the end of the token budget, on every seed
  carried.
- Reported as raw accuracy on each condition separately, on every arm, with
  its spread across seeds. Not combined into one number, not normalised by
  anything. The named-other condition is reported on arms T, C and M although
  it does not gate them.
- **The threshold, per condition (ruled, the queue ruling, page 1b):** the
  condition's accuracy is above the one-in-four level at the 0.05 level under
  a one-sided binomial test, **on at least two seeds of three**. The ruling
  writes the bar as "above 0.2630"; on 3,000 held-out episodes that is 790 or
  more correct, a share of 0.2633 (MEASURED: the bar's derivation is printed
  in `docs/rehearsal-repairs-method-2026-09-25.md` at `882f252`, and
  `out-repairs/gate_base.json` carries it as the field `bar`; this session
  re-derived it by an exact binomial tail, section 17, failure 3); the
  registered measurement uses the same 3,000, so the bar is 790 there too
  (ruled 2026-10-03, late evening, ruling 4).
- Reference points reported alongside, and they are references and not
  thresholds: one in eight for guessing, one in four for a solver that cannot
  tell whose value it needs, and the **measured** accuracy of two competing
  solvers built at the rehearsal, one that cannot use ownership at all, one
  that uses only the name token (rehearsal item R-5; on the toy the
  ownership-blind solver scored 0.2340 to 0.2383 on the own-directed
  condition and the name-only solver 1.0000 on the named-other condition and
  0.2380 on the own-directed, `out-repairs/gate_base.json` at `882f252`;
  these were taken before the piece rule of 2026-10-03; the ownership-blind
  solver is to be put through the nomination under it before the
  registration review, section 7.3, the last paragraph).
- An arm that fails, after the one permitted re-run, gives outcome R3 for that
  arm, and the registration says which arm and on which condition.
- **What is already on the record about this gate (MEASURED: the earlier
  re-run's findings at `9d9d31a`, Part 1, section 1.2, whose gate counts
  equal `out-repairs/gate_base.json` field for field; the controls re-run of
  2026-10-03 read the gate from that committed file and did not run it
  again):** arm T clears both
  conditions on 3 seeds of 3; arm C clears the own-directed condition on 3 of 3
  and the named-other on 0 of 3 (760, 751 and 708 of 3,000), and passes its
  gate; arm M clears both on 3 of 3 and passes; arm F clears the own-directed
  on 3 of 3 and the named-other on 1 of 3 (994, 781 and 746), and **fails**.
  No training change fixed the free arm's failure (section 4.4).

### 8.2 The ownership-lesion check, for arm F only

Before arm F is read, the acting channel is zeroed at evaluation, the lesion
the existing code already performs. **The pre-stated shape (ruled, the queue
ruling, page 1h; refined by the Gate C rulings, RT-220):**

- **own-directed accuracy falls below the section 8.1 bar**: that is the
  collapse, and it gates;
- **arm F is read if at least two of three seeds collapse, with the third
  reported** (the RT-220 ruling). A separate collapse bar below the learn-both
  bar was considered and not taken, because it adds a second pre-stated
  number nobody has rehearsed. What the two-of-three clause is for: because
  the collapse line *is* the learn-both bar, it sits just above the level a
  fully collapsed arm is expected to reach, and an arm whose lesion drops it
  to exactly one in four is read as "not collapsed" 4.85% of the time per
  seed (MEASURED: section 17, failure 3, the exact binomial tail at 790 of
  3,000). One seed of three misreading that way must not stop arm F being
  read;
- named-other-directed accuracy is **reported and not gated**; the pre-stated
  expectation that it holds is a description, because the rehearsal found
  that shape is architecture-specific (`docs/2026-09-21-successor-measure-rehearsal.md`,
  section 8);
- the ownership-free state and syntax batteries **must hold**.

**What this check does and does not establish, in the closed design's own
registered words: it removes a sense organ, not a structure the network
built.** It is a precondition for reading arm F, since it shows the ownership
answer is load-bearing for the act, which is what makes arm F worth
measuring; it is not evidence of a centre and is never reported as such
(ruled 2026-10-03, decision 10).

Arms T, C and M do not take this check as a gate: their dependence on
ownership is architectural. Their lesion results are computed and reported as
a description of the constructed systems. **On the toy, described honestly
(ruled, the Gate C rulings, RT-220):** arm T collapses on two of three seeds,
at 0.2467 and 0.2510, and its seed 2 reads 0.2733 against the bar of 0.2633,
so under the rule it did not collapse there; arms C and M collapse on all
three (0.1703 to 0.1830 and 0.2190 to 0.2230); arm F, the arm this gate is
for, collapses on all three, at 0.1760 to 0.1940 (MEASURED:
`out-repairs/gate_base.json` at `882f252`, fields `lesioned_own` and
`lesion_collapses_own`; section 17, failure 3, prints them). Version 2's "all
three collapse" was wrong for arm T seed 2 and is replaced.

---

## 9. The numbers, now set

Every number version 1 deliberately left blank is filled from John's rulings
of 2026-09-25, 2026-09-26 and 2026-10-03, each citing the ruling that set it.
**None was invented here.** The registration text freezes them in this form.
The device row and the last row, the numbers of episodes, were open when this
version was first filed and were ruled the same night.

| Number | Set to | Ruled in |
|---|---|---|
| Separation bar between arms T and C (R1 against R2) | **0.5**: the minimum gap between arm C's reading and arm T's, on the chance-corrected form. **Reconciled 2026-10-03 (night): taken as the lowest reading among arm C's seeds that read minus the highest among arm T's, not paired by seed number** | `docs/rulings/2026-09-26-weekend-1-queue.md`, page 1a, which does not say how the gap is taken across seeds; `docs/rulings/2026-10-03-version-4-questions-rulings.md`, ruling 6. On the toy this is 0.9926. **Under this version's rules the toy cleared it on every seed, at 1.0051, 0.9926 and 0.9974** (MEASURED: the controls re-run at `821f154`, section 2, from `out-controls-rerun/summary.json`, `separation`). Version 3's 1.0051, 1.0025 and 1.0000 were read on two seeds through pieces that do not hold the label and are superseded (the review of version 3, RT-230) |
| Gate on learning (R3) | above one in four at the 0.05 level, one-sided binomial, on at least two seeds of three: **0.2633 on 3,000 held-out episodes** (790 or more correct), or the same rule at the registered count; **on the own-directed condition only for arms T, C and M, on both conditions for arm F**; the ownership-blind and name-only solvers reported beside it as references | the queue ruling, page 1b; the Gate C rulings, RT-213, item 1 |
| Fit floor | **four fifths of held-out development episodes, on the piece that is transplanted, at the action position**, per arm and seed, stated as a count (144 of 180 on the toy); only sizes whose piece reaches it may be chosen; the whole read's count printed beside it and not a second floor; the permutation null reported beside it and not used as the bar | the rulings on the review of version 2, RT-212, item 1; per arm and seed, and the read itself, ruled 2026-09-26 (decisions 21 and 23); moved to the piece by `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 1; on the piece only, and applied after the layers are chosen, by `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, rulings 1 and 2 |
| The piece's accuracy at the other positions of its site | **reported both ways, with no pass line on either**: a count at each other position, and a count on the average over them, computed as section 7.2, item 3, states | `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3; `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling 2 |
| The device and number format of the registered fit | **the laptop's processor; the figure computed there is the registered one.** States in 32-bit, the read fitted in 64-bit by scikit-learn, library versions recorded, **and pinned in a committed file named in the registration (reconciled 2026-10-03, night)** | the review of version 3, RT-232, accepted as the review states it by the rulings of 2026-10-03, page 3; the device by `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, ruling 3 |
| Whole-state floor (whether a site set is usable) | **four fifths of the arm's own own-directed accuracy**, on the chance-corrected scale, **applied on development episodes at nomination and again on the fresh episodes at the reading; a site set that clears the first and misses the second returns no verdict**; the whole-state layer set is **the smallest that clears it, per position set, then the highest ownership-only share among those**; every all-positions site set excluded; every layer-0 site set removed at position sets other than `action` | the queue ruling, page 1c; the repairs rulings, items 3 and 4; the rulings on the review of version 2, RT-216, item 1, as clarified by refinement item 2; the review of version 3, RT-234, accepted 2026-10-03, page 3 |
| Rank cap on the nominated subspace | **8**, with the family reporting caps 1, 2, 4 and 8 | the queue ruling, page 1d |
| Candidate site list and its family correction | the rule of section 7.2, printed for the registered 12-layer model: **325 site sets and 1,300 comparisons** with layer 0 kept at the action position set only (45 and 180 on the toy); the count is the rule's output, not hand arithmetic | the queue ruling, page 1e; the repairs rulings, item 3; the Gate C rulings, RT-215 and RT-216; the reading of the layer-0 exclusion ruled 2026-09-26 (decision 20) |
| Control 3 | **a twenty-draw null, reported and not gated**: median, 95th percentile, and the ownership-only share's place among the draws | the rulings on the review of version 2, RT-214, items 1 and 2, as refined on 2026-09-26, refinement item 1 |
| Control 2, the other-agent control | **no pass line.** A reported description, beside twenty random pieces; the 0.05 tolerance of version 3's decision 15 is withdrawn and not registered; the registration says the control never ran at toy scale | `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 1; the twenty by `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, ruling 5 |
| Control 4, the too-early-position control | **holds; its pass line is that the outputs with the transplant are bit-identical to the outputs without it**, on the positions before both twins' first own turns, at the nominated layers; a failure withholds the reading for that arm and seed | the same file, ruling 2, reversing that morning's ruling on version 3's decision 16 |
| What a no verdict maps to | arm C: the two-arm fallback; arm M: arm M is dropped and carried as an extension; arm F after arms T and C separate: **the fifth registered term, "metric validated, degree not read", satisfactory and stated as weaker than R1** | `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 11; `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling 1 |
| Seed count per arm | **three**; the toy arithmetic implying one seed was not carried across | the queue ruling, page 1f |
| Uncertainty across seeds | **the across-seed spread of the raw difference** is the registered uncertainty; the within-seed bootstrap over matched pairs is reported beside it; neither measures drift between runs of one seed, and the registration says so | the queue ruling, page 1g; on the repairs run the two disagreed by more than two to one on arms C and F (the repairs findings at `882f252`, section 6.2; figures at pre-rule site sets, not carried) |
| Ownership-lesion collapse threshold (whether arm F is read) | own-directed accuracy **below the learn-both bar** with the acting channel zeroed, **on at least two seeds of three, the third reported**; the named-other clause reported and not gated; the ownership-free batteries must hold; gates arm F only | the queue ruling, page 1h; the Gate C rulings, RT-220 |
| The no-transplant allowance | **at most the largest measured miss, rounded up to 0.018**; the detection margin at the bar printed in the reporting table | the queue ruling, page 2; the Gate C rulings, RT-222 |
| The form of the reading | **the chance-corrected form** of section 6.3 | the queue ruling, page 2 |
| The label | **which marker word is the model's own**, the one registered read; the route (b) candidates recorded as exploratory fits only | `docs/rulings/2026-09-23-nomination-label.md`; the queue ruling, page 3; the Gate C rulings, RT-212, item 3; John's ruling of 2026-09-26 on the route (b) result (section 7.2, item 1) |
| Seconds per step, per arm, on the rented machine | **Measured 2026-09-25 for arms T, C and F**: 13.08, 13.52 and 12.53 milliseconds per step, ratios to arm F of 1.044, 1.080 and 1.000, on a secure RTX 5090 at $0.99 an hour, at the registered shape, fifty timed steps after five warm-up steps | `docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section 3, from `experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/bench_arms.json`; checked at `afb5183`, point 5. **Arm M was not timed.** **Fifty timed steps are accepted for the second release's arithmetic; the five-hundred-step figure is taken from the first full-size run, and the later runs are repriced from it before the second release is asked for** (ruled 2026-10-03, decision 17) |
| Arm M's predicted reading | between **0.3 and 0.7** on every seed, and within **0.10** of its true-slot reading on the same fresh episodes (the formula of section 5.3, which is that reading written in route accuracies). On the toy under the registered rules: 0.4886, 0.4860 and 0.5449, within 0.0049, 0.0099 and 0.0529 of the true-slot reading | the queue ruling, page 5 (the band); the repairs method note at `882f252`, section 5 (the formula and the 0.10); the rulings on the review of version 2, RT-223; the toy figures from the review of version 3, RT-231, and the controls re-run at `821f154` |
| The numbers of episodes at the registered size | **the toy's, unchanged: 600 development episodes with the last 180 held out for every fit (the floor is 144 of 180); 800 fresh matched pairs; 800 pairs on the relaxed set; 3,000 held-out episodes for the gates (the bar is 790); 200 shuffles for the permutation null.** The caution carried with it: at 180, one episode is 0.0056 of the scale. **Reconciled 2026-10-03 (night): the band that sampling alone puts around each count against the floor is printed beside it** | `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, ruling 4 |
| An arm whose three seeds disagree | **two seeds of three decide, the third reported**: an arm is read if two or more seeds read. **Reconciled 2026-10-03 (night): the separation is the lowest of arm C's readings minus the highest of arm T's, among the seeds that read, and is not compared seed by seed** | the same file, ruling 6 |

---

## 10. The rehearsal: what it was, and where each item stands

A complete measurement rehearsal before any Gate A is protocol
(`docs/outside-review-protocol.md`, "The measurement rehearsal, required
before any Gate A"). It ran in five parts, all at toy scale on the laptop
except one item: the rehearsal of 2026-09-21
(`docs/2026-09-21-successor-measure-rehearsal.md`, code in
`experiments/rehearsal-successor-measure/`, re-run from code on 2026-09-22
with the separable arm reproducing exactly and the other two not); the
repairs of 2026-09-25 (`docs/2026-09-26-rehearsal-repairs.md` at `882f252`,
code and outputs under the same directory's `src/repairs.py` and
`out-repairs/`, checked at `d216dbc`); and the re-run of 2026-09-26 under this
version's rules (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, code
`src/rerun_v3.py`, outputs `out-v3-rules/`, checked at `70be9fb`); **the
controls re-run of 2026-10-03 under the piece rule**
(`docs/2026-10-03-controls-rerun.md` at `821f154`, method
`docs/controls-rerun-method-2026-10-03.md`, code `src/rerun_controls.py`,
outputs `out-controls-rerun/`, checked at `e184a6e`), which the rulings of
2026-10-03, page 2, made a precondition of the registration review; **and the
short pre-stated run of the same day** (`docs/2026-10-03-short-prestated-run.md`
at `853988f`, method at `9e978d9`, code `src/short_prestated_run.py`, outputs
`out-short-prestated-run/`; checked by a second session, main line at
`53c8100`). The
last two loaded the twelve committed base-recipe models, checked each file's
fingerprint against the committed list before loading it, trained nothing and
spent nothing. The one part that spent money is item R-11. Total spent on the rehearsal so far:
about $0.57, the sum of the compute ledger's three slice rows, of the
rehearsal line's $10 (item 10 of the 2026-09-21 ruling; section 12.3).

**The models every toy result rests on: thirty, all committed.** The fifteen
trained toy models behind the repairs and the re-run (arms T, C, F and M and
the ownership-blind solver, three seeds each) are committed at
`experiments/rehearsal-successor-measure/out-repairs/models/` (main line at
`8038275`, pull request 64), because they cannot be rebuilt from code and
seed (the repairs check at `d216dbc` retrained from clean and got different
nominations) and an uncommitted record the reader cannot open is the form of
ledger item RT-145. The other fifteen are committed too (main line at
`7ed2b0e`, pull request 67): the six free-arm models behind the two training
redesigns that failed (`ckpt_F_curriculum_seed*.pt` and
`ckpt_F_reweight_seed*.pt`, in the same folder) and the nine behind the
grammar attempt (arms T, C and F, three seeds each, at
`experiments/rehearsal-successor-measure/out-grammar-c/models/`). One
fingerprint list, `out-repairs/models/SHA256SUMS`, covers all thirty, with a
`README.md` beside it saying where each file came from. The re-run's
fingerprint check compared three recorded hashes per file with the list for
the first fifteen and found all agree, its check hashed the stored files
themselves and found the same, and the label-search check found all thirty
files on the main line check against the list (MEASURED:
`out-v3-rules/models_sha256_check.json`, `all_agree: true`; the check at
`70be9fb`, section 2.1; the label-search check at `ecd2b6c`, section 4).
**What rests on them: every toy result of 2026-09-25 and 2026-09-26 that
this version quotes.** On the first fifteen: every base-recipe result of the
repairs (`gate_base.json`, `nominate_base_*.json`, `measure_base_*.json`,
`summary_base.json`, the training records `train_*_base_seed*.json` and the
`F/base/*` rows of `diagnose_named_other.json`), the whole of
`out-v3-rules/`, the label search's fits, the whole of
`out-controls-rerun/` and `out-short-prestated-run/` (which use the twelve
models of arms T, C, F and M and not the solver's three), and every toy
figure in sections 3, 5, 7, 8 and 9 of this version. On the six redesign models: the curriculum and
loss re-weighting results of section 4.4 (0 of 3 seeds each). On the nine
grammar-attempt models: the grammar attempt's figures of section 4.4 (774,
730 and 759, and everything in `out-grammar-c/`). Two kinds of figure quoted
in this version are not toy results and rest on no committed model, and are
said to be what they are where they appear: the rented slice's seconds per
step (section 9), a timing of a model that exists on the record as a
checksum only; and the two checks' own re-run figures (the grammar check's
750, 809 and 739; the repairs check's 6 of 12), which are the checks'
verification of a verdict, quoted as such, from retrainings those checks
recorded but did not keep. Decision 22, which asked whether the further
fifteen should be committed, is done.

**A pre-stated quantity the rehearsal never exercised is a fatal finding on
its own** (item 5 of the 2026-09-21 ruling). Each item below therefore says
what exercised it.

- **R-1. The grammar works and both conditions are learnable at tiny scale.**
  The four matched properties hold (P-1). The own-directed condition learns on
  every arm. **The named-other condition does not clear the bar on the free
  arm on a majority of seeds, under any of three training recipes or under
  the grammar change, and does not clear it on arm C on any seed** (760, 751
  and 708 of 3,000; section 4.4 and section 5.2). Stop condition S1 is ruled
  not to have fired; fallback (d) registers; the constructed arms are gated on
  the own-directed condition only. *Exercised; the finding is the honest
  prior, measured.*
- **R-2. Arm T is constructible and its ownership slot is transplantable on
  its own, and so is arm M's separable route.** The blind nomination finds
  arm T's slot without being told where it is, on every seed, and reads
  0.0000 under the registered rule and under the stricter variant; on arm M
  the blind subspace's ownership-only transplant moves 0.37 to 0.41 of trials
  against random medians of 0.015 to 0.019 (the controls re-run at `821f154`,
  sections 2 and 4). *Exercised.*
- **R-3. Arm C is constructible and its degree is genuinely known by
  construction, and arm M's mixture reads between the anchors in its
  pre-stated band.** On arm C the read holds the label, the piece
  transplanted holds it at the action position (180, 172 and 150 of 180), and
  the ownership-only transplant lands within 0.004 of the no-transplant rate
  while the whole state moves the action, so it reads 1.0051, 0.9926 and
  0.9974; arm M reads 0.4886, 0.4860 and 0.5449 against a band of 0.3 to 0.7,
  and within 0.0049, 0.0099 and 0.0529 of its true-slot reading at the
  registered site sets (sections 5.2 and 5.3). **Arm C fails the named-other
  condition on every seed and passes its gate on the own-directed condition**
  (section 5.2). *Exercised under the registered rules; the two-arm fallback
  does not fire.* The check of arm M's reading against its true-slot reading,
  which version 3 listed as owed, is done.
- **R-4. All the measure's outcomes are reachable.** Near zero (arm T), high
  (arm C), the middle (arm M), negative (the unseen-vocabulary diagnostic,
  section 7.1; and arm T seed 0 on the grammar attempt's unseen pool, at
  −0.1870), above one (arm C at 1.0051), and no verdict (arm F on every seed,
  by the gate and by the fit floor; control 2 on every toy model it applies
  to). *Exercised.*
- **R-5. Ordinary competing solvers are built and measured.** The
  ownership-blind solver and the name-only solver, both scored on both
  conditions (section 8.1). *Exercised, before the piece rule of 2026-10-03.
  The ownership-blind solver's run through the nomination under that rule is
  owed before the registration review, by ruling (section 7.3, the last
  paragraph).*
- **R-6. The arithmetic is finite.** The chance-corrected form's denominator is
  kept off zero by the whole-state floor (the smallest toy denominator under
  the registered rule is 0.4863, arm C seed 2, among the pairs that read, and
  0.4263 on arm F seed 0, which is described and not read; section 17,
  failure 1); the
  no-transplant formula was checked against nine arm-and-seed pairs on
  2026-09-21 and twelve on 2026-09-25; two made-up systems of equal true share
  and unequal transplant strength read the same under the registered form
  (section 6.3). *Exercised.*
- **R-7. Throughput, per arm, projected to dollars.** Done from item R-11's
  measured ratios on the lifetime-priced cost of a registered-size run
  (section 12.4). *Exercised for arms T, C and F; arm M's runs are priced from
  ledger rows.*
- **R-8. The transplanting code passes its known-answer tests.** The null
  transplant leaves every logit bit-identical on every arm and seed; the
  ownership-only transplant is proved a restriction of the whole-state one;
  a transplant on arm T moves the action to the donor's value. *Exercised*
  at fifteen different places on the toy (section 7.3, item 7), which closes
  the citation gap version 3 recorded.
- **R-9. The uncertainty method is chosen.** Ruled (section 9, 1g) from both
  methods computed on the same data. *Exercised.*
- **R-10. The separation bar is set.** Ruled at 0.5 from a toy separation of
  0.873 to 0.885 on 2026-09-21, and cleared at 1.0051, 0.9926 and 0.9974 under
  the registered rules on 2026-10-03. *Exercised.*
- **R-11. Seconds per step on the rented machine, all three arms, and the
  shutdown path against the real vendor.** Measured on 2026-09-25 on the
  second attempt at the rented slice, after a first attempt that hung and was
  stopped with neither measurement taken (`docs/2026-09-25-rented-slice-findings.md`,
  main line). Throughput: **PASS**, three figures with their spread, fetched
  home (section 9), checked character for character against the launcher's
  log (the check at `afb5183`, point 5). The shutdown handshake: **the laptop
  half passed against the real vendor, copy, checksum, receipt written,
  delete, confirmed gone, and the machine half was not exercised**, because
  the laptop deletes the machine in the same second it writes the receipt, so
  the machine's own "receipt found" can never be observed on the normal path
  (MEASURED and ARGUED: `docs/2026-09-25-rented-slice-attempt-2-findings.md`
  at `9f802db`, section 4; the check at `afb5183`, points 7 and 8). None of
  the slice's six pre-stated handshake lines fits, and the findings do not
  force one. **Both things this left open were ruled on 2026-10-03**: fifty timed
  steps are accepted for the second release's arithmetic, with the
  five-hundred-step figure taken from the first full-size run (decision 17);
  and the registration says what is true of the handshake today, that on the
  normal path the laptop deletes the machine and the machine's own watcher is
  a backstop (decision 18; weakness W9). Cost:
  about $0.57 across three rows against the item's $3 (section 12.3).

**The seven controls, and what exercised each under the registered rules.**
Controls 1, 3, 6 and 7, the true-slot reference, the rider and the stricter
row: the controls re-run, on all twelve toy models, checked (section 7.3).
Control 4 as redefined: the short pre-stated run, on all twelve, **checked: the check of the short run at `53c8100`**; the same fact was measured independently, with
separately written code, by the check of the controls re-run (section 7.3,
item 4). Control 5 holds by construction. **Control 2 was never exercised at
toy scale, and the registration says so in terms** (section 7.3, item 2). It
carries no pre-stated number, so by John's ruling nothing about it is an
unexercised quantity in the sense of item 5 of the 2026-09-21 ruling; the
part of its code after the floor has run once, in a run labelled NOT A
RESULT.

**What happens next.** The ordinary competing solver is run under the piece
rule, method first, by another session, and checked; this version and the
late-evening ruling's record are checked under the pairing rule by a session
that did not write them; this text is brought into line with both; then it
goes to Gate A, both tiers, when John opens that review; the registration
commits when both tiers are answered and he rules. There is no target date;
the only date is the kill date of 2026-10-18 (section 11).

---

## 11. Order of work, and where it stops

Binding if registered, in this order, on the chain of section 4 of
`docs/december-result-roadmap-2026-09-20.md` as amended 2026-09-21:

1. **Done.** The first independent review of version 3 (RT-230 to RT-236);
   John's rulings of 2026-10-03 on it and on version 3's open decisions; the
   controls re-run under the registered rules, and its check; John's three
   rulings after it; the short pre-stated run; John's evening ruling. The check of the short
   pre-stated run and of the evening ruling's record; John's late-evening
   ruling on this version's seven questions. **Owed before step 2:** the
   competing solver's run under the piece rule, and its check; the check of
   this version and of the late-evening ruling's record under the pairing
   rule.
2. This text, brought into line with those → **Gate A, both tiers**, opened
   by John → registration commit. **No target date. Kill date 2026-10-18**,
   past which committing it takes a fresh ruling naming what comes off the
   back end (item 23 of the 2026-09-21 ruling).
3. Implementation frozen; unit tests; the even-split rule and the
   one-scored-token self-test run on the built generator; the training entry
   point for arms T, C and M on the rented machine written and named in the
   registration (section 5); the tripwire of section 12.5 written into the
   launch preconditions beside the sleep guard and the argument guard (the
   queue ruling, page 6, "Changes").
4. Development runs at the 10-million size, **four arms, one seed each,
   including arm M, from the first release's development line (ruled, the
   Gate C rulings, RT-229)**. **This is a pipeline and throughput check, not a
   learnability verdict**: the 10-million size failed to learn the earlier
   design's task, so a null here means nothing about the registered size, and
   the registration says so in advance. It is also the first time arm M's code
   runs on the rented machine (weakness W9).
5. **The staggered launch, in two steps, as ruled 2026-09-21** (item 12 of
   that ruling; steps 5a and 5b of the roadmap chain).
   - **5a. One arm F run at the registered size launches first**, on John's go
     naming it, inside the first release (section 12.3). Three things come
     back before anything else launches: whether it passes the learn-both
     gate; what the machine actually bills (the tripwire, section 12.5); and,
     **new (John's ruling of 2026-09-26 on the route (b) result, section 7.2,
     item 1), the nomination of that run's ownership read on development
     episodes, reported against the four-fifths floor: whether any size of
     piece reaches it, with the read's held-out count at every layer, the
     chosen piece's own count, and the candidates the nomination chose among
     (the review of version 3, RT-235; section 7.5)**. A fourth thing comes
     back with them: **the five-hundred-step timing that rehearsal item R-11
     asked for is taken from this run, and the eleven later runs are repriced
     from it before the second release is asked for** (ruled 2026-10-03,
     decision 17). If it fails the
     gate, the one permitted re-run happens, also inside the first release
     (item 19 of the 2026-09-21 ruling); if that fails too, the outcome is R3
     and nothing else launches. **If no size of piece reaches the fit floor,
     that is a stop before the second release draws, beside the learn-both
     stop** (unchanged by the fifth outcome term: the rulings of 2026-10-03,
     page 11, item 6): it
     goes to John as a registered-size "no verdict, read failed its floor" on
     one seed, and whether the remaining runs are worth the second release is
     his call with that figure in hand (section 3). The fit is computed on the
     laptop from the fetched checkpoint, as the toy nominations were, and
     draws no rented time (ARGUED: a 30-million-parameter model's activations
     on development episodes fit on the laptop; if that turns out not to be
     so, the cost goes into the first release's rehearsal line and is said).
   - **5b. The remaining eleven registered runs**, two more of arm F, three
     each of arms T, C and M, launch only after 5a's learn-both result is
     read and its billing found normal, the second release is asked for and
     ruled, and John gives the go. **Kill date 2026-11-01 binds this step, not
     5a** (item 23 of the 2026-09-21 ruling): past it, launching takes a fresh
     ruling naming what comes off the back end.
   - **What a constructed arm's failure costs under this order, stated (ruled,
     the Gate C rulings, RT-213, items 2 and 3).** Step 5a tests arm F only.
     Arm C, the high anchor, is first trained at the registered size in step
     5b, after the second release, about $119 on the ruled split plus arm M's
     runs (section 12.4), has been drawn. On the toy, arm C is the arm that
     fails the named-other condition on every seed; under this version's gate
     that failure would not fire an R3 (section 8.1), but a failure of arm C's
     *own-directed* condition at registered scale, or an arm C whose
     construction did not hold (weakness W3), is seen only after both releases
     are drawn, and an R3 or a two-arm fallback caused that way costs the
     whole successor, about $194 to $206, not the first release's $44. John
     ruled against an extra arm C run inside step 5a: at $422 to $434 of $450
     the envelope has no room, and if he later wants the anchor's construction
     proven at registered scale before the second release, that run needs the
     ceiling revisited.
6. Nomination on development episodes as arm F checkpoints arrive, with the
   fit floor applied and printed; frozen and committed; transplants on fresh
   episodes, all arms. The measure computed on arms T, C and M: that is the
   validation result.
7. **Gate B** on the validation. John rules: read arm F, or close on R2 or R3.
   A no verdict on arm C fires the two-arm fallback, and a no verdict on arm
   M drops arm M (section 3).
8. If arms T and C separate: arm F read on the frozen procedure, confirmation
   seeds. If arm F reads, the outcome is R1; if it returns no verdict, the
   outcome is the fifth term, "metric validated, degree not read", with its
   reason. Findings; Gate B; closure text through Gate A. Wrap-up starts 2026-12-21 whatever
   state the chain is in.

**Stop conditions, each of which halts spend and goes to John.**

- **S1.** The rehearsal fails item R-1 (the grammar is not learnable at tiny
  scale even in principle) or item R-8 (the transplanting code does not pass
  its known-answer tests). **Ruled on 2026-09-25 not to have fired** (the
  queue ruling, page 4): the separable arm learned both conditions to 1.0000
  and the transplanting code passes. The named-other failure on the free arm,
  and now on arm C too, is fallback (d), on the record in section 4.4, not S1.
- **S2.** The rehearsal fails item R-3. The two-arm fallback fires; this is not
  a stop, but it is a change John has pre-approved and it is recorded. At toy
  scale R-3 passed under the registered rules.
- **S3.** The rehearsal fails item R-4 or R-6. The measure is not registered.
  At toy scale both passed.
- **S4.** The staggered first registered run fails the learn-both gate, and the
  one permitted re-run fails it too. Outcome R3. **About $44 spent**: the
  whole first release, which since item 19 of the 2026-09-21 ruling includes
  the re-run (section 12.3). (Version 1 stated this outcome's cost two ways;
  the Gate C review of version 1, finding RT-178, caught it, and item 19
  removed the gap.)
- **S4a (new, John's ruling of 2026-09-26).** The staggered first registered
  run passes the learn-both gate but no size of piece of its ownership read
  reaches the fit floor on development episodes. Not an outcome on its own: a stop before the second
  release draws, with the registered-size fit reported to John against the
  floor and its permutation null, and nothing else launches until he rules.
  About $44 spent at most, as for S4.
- **S5.** Cumulative actual spend reaches the release John has authorised,
  about $44 for the first release (section 12.3), until and unless he rules on
  the second. Work stops regardless of state; what is unrun is reported as
  unrun, and nothing launches against a release that has not been ruled.
- **S6.** A kill date passes: registration not committed by 2026-10-18, or
  the remaining runs of step 5b not launched by 2026-11-01. **Launching or
  registering past the date needs a fresh ruling that names what comes off the
  back end to make room** (item 23 of the 2026-09-21 ruling); nothing is
  written off automatically and nothing slips past unremarked. R4 is where
  the roadmap lands only if that ruling says it is not worth it. There is no
  2026-10-11 target: version 1 carried one, and item 23 leaves the schedule
  with the two kill dates and nothing else.
- **S7.** Any corrigibility event under commitment C5 of
  `spec/corrigibility-commitments.md` (the model observed exploiting or
  degrading the evaluation machinery) halts the run before further compute.
- **S8.** A rehearsal item, a gate or a stop condition **cannot be evaluated**:
  missing data, code that will not run on the artifact, a measurement never
  taken. It counts as failed and its consequence fires; it is never recorded as
  not applicable and stepped over (item 15 of the 2026-09-21 ruling; section
  12.7). Control 2's *not applicable* on arms T and M is not an instance of
  this: it is a ruled disposition with the reason on the record (section 7.3).
  Nor is control 2's *no verdict* on an arm that has not learned the
  named-other condition or whose read of the named agent misses its floor:
  the registration says in advance that it is the expected result. Nor is a
  *no verdict* under the fit floor: that is a registered outcome of the
  procedure with its reason printed.
- **S9.** **The tripwire trips**: either billing ratio of section 12.5 at or
  above 1.25 on any machine of a wave, or a check that cannot run. **The wave
  halts, not trims** (section 12.5), and it goes to John with the ledger row
  beside the estimate.

---

## 12. Spend: rebuilt from the compute ledger, and the two releases as ruled

*Every dollar figure in this section is read from
`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md` (the
programme's system of record for money), from the dated note beside the
spending proposal that recomputed the second release, or from a ruling that
quotes the ledger; the row or note is named beside each figure. Nothing here
is a request, and nothing here releases money: John's process does that, run
by run, with his own words quoted in the ledger row before anything is
created.*

### 12.1 Where the money stands

| | | Source |
|---|---|---|
| Programme ceiling | **$450**, raised from $400 on 2026-09-25 | the compute ledger's ceiling note of 2026-09-25 at the top of the file, recording the queue ruling's page 6 ("The envelope") |
| Spent across the programme, as of the last row on the main line | **about $228.15** | the ledger's second 2026-09-25 row (line 95), the rented slice's second attempt, "After this run"; on the main line since `9f802db` |
| Amendment A3 against its $100 stop | **about $46.75** | the same row |
| The rehearsal line of the first release, spent | about $0.02 (2026-09-21), about $0.50 (first attempt), about $0.05 (second attempt); **about $9.43 of $10 remains** | the same row; the check at `afb5183`, point 3, confirms the $0.0525 against the two balance readings and the vendor's posted billing row |
| Headroom before the successor's two releases | **about $221.85** | $450 minus about $228.15, arithmetic on the two rows above; not a figure the ledger states |

Version 2 carried these figures from an unmerged branch; they are now on the
main line, unchanged. No ledger row has been written since: the ledger's
last row on the main line at `f32ba0c` is still the second 2026-09-25 row,
and nothing in the work of 2026-10-03 rented or spent anything.

### 12.2 What is ruled, and what this section is built to

- **The flat $130 cap of 2026-09-20 is superseded** by the two releases of
  the 2026-09-21 ruling (items 10, 11 and 19 of
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, with
  its correction note of 2026-09-22: about $44 and about $131). That sentence
  is the closure of the Gate C review of version 1's finding RT-176 (the
  $175-against-$130 finding), and a dated annotation goes beside item 4 of the
  2026-09-20 ruling (the queue ruling, page 6, part 1).
- **The envelope is $450** (the queue ruling, page 6, part 2, recorded in the
  compute ledger's ceiling note of 2026-09-25). What it was ruled to buy, on
  the ledger rows the packet cited: the base plan of about $175 on top of
  about $227.63 spent, plus one extension of $32 to $44 (arm M) or about $36,
  with $3 to $15 left. It does not hold two extensions. The measured figures
  below leave more room than that arithmetic did.
- **The first release's development line covers four arms, not three (ruled,
  the Gate C rulings, RT-229).** This widens item 10 of the 2026-09-21 ruling,
  which covered three; the reason recorded is that arm M's code has never run
  on the rented machine, so its development run belongs in step 4 with the
  others, before the second release. Version 2 had costed that run twice, once
  in each release (the Gate C review, RT-229); this version costs it once, here.
- **The second release is asked for only after seconds per step were
  measured on the rented machine** (item 11 of the 2026-09-21 ruling). They
  were, on 2026-09-25 (section 9). The ruling changed the ceiling, not that
  gate.
- **The staggered launch** (item 12), **halt not trim** (item 13), **funding
  per wave** (item 14) and **a check that cannot run is a trip** (item 15) all
  stand; sections 11, 12.5, 12.6 and 12.7.
- **The pre-authorisation scheme** of `docs/preauthorised-spending-proposal-2026-09-21.md`
  **is not adopted** (the queue ruling, page 6, part 3). Only its tripwire is.
- **The successor gets a new experiment directory with its own registration
  (`experiments/08-…`), and the compute ledger stays where it is**, in
  experiment 06's folder, as the programme's one record of money (ruled
  2026-10-03, decision 8).

### 12.3 The first release: about $44, ruled 2026-09-21, with a four-arm development line

| Item | What it buys | Basis | Amount |
|---|---|---|---|
| The rehearsal | Tiny models, the transplanting code, rehearsal items R-1 to R-11, including the rented slice | item 10 of the 2026-09-21 ruling: up to $10. Spent so far: about $0.57, the sum of the ledger's three slice rows (about $0.02 on the 2026-09-21 row, about $0.50 and about $0.05 on the two 2026-09-25 rows), leaving about $9.43 by the last row's own running line | up to **$10** |
| Development runs | **Four arms, one seed each**, at the 10-million size: pipeline, self-tests, throughput, and arm M's first run on the rented machine | item 10: up to $10 for three arms, **widened to four by the RT-229 ruling**. The ledger's reconciliation of 2026-08-12 trues the earlier 10-million run up to $1.943 (lines 393 and 400), so four such runs are about $7.77 of the $10 line (MEASURED: section 17, candidate 7) | up to **$10** |
| One free-arm run at the registered size | Step 5a of section 11 | item 10: about $12. The lifetime-priced cost of a registered-size run is $10.04 (the ledger's 2026-09-17 row, line 88: 20.28 pod-hours at $0.99 for two runs, computed from measured pod lifetimes and not balance-confirmed, as the row itself says; the Gate C rulings, RT-226) | about **$12** |
| The one permitted re-run | If step 5a fails the learn-both gate | **item 19: folded into the first release**, at the same planning figure | about **$12** |
| **First release, total** | | | **about $44** |

This is the release John has authorised; nothing beyond it is launchable
without the second. Stop conditions S4 and S5 in section 11 are stated
against it.

### 12.4 The second release: from the measured seconds per step, then arm M's three runs

**What the second release is bound to, and now has.** Item 11 bound it to
rehearsal item R-11's measured seconds per step for arms T, C and F on the
registered venue. Those were measured on 2026-09-25 (section 9), and the
dated note beside the spending proposal recomputed the release from them
(`docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
at `9f802db`; checked at `afb5183`, point 6, where the script's re-run is
byte-identical to its committed output). The method, in the note's own words,
is MEASURED arithmetic on an ARGUED method: the measured seconds cannot be
turned straight into hours for a run (a timed step holds 1,792 tokens where a
registered step held about 10,624, and a real run also generates its data,
evaluates and saves), so the note does what version 1's spending arithmetic
did, with the measurement in place of the inference: **the lifetime-priced
cost of a registered-size run, $10.04 (the ledger's 2026-09-17 row), times
each arm's measured ratio.** Every figure below is the note's, printed by
`experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/second_release_arithmetic.py`
into `second-release-arithmetic.txt` beside it.

| Per run | Version 1's planning figure | From the measurement |
|---|---|---|
| Arm F | $12 | **$10.04** |
| Arm T | $12 | **$10.48** (ratio 1.044) |
| Arm C | $12 | **$10.84** (ratio 1.080) |
| Arm M | (none: arm M is new in version 2) | **not measured**; priced from ledger rows below |

| Item | Version 1 (provisional) | From the measurement (the note's table) |
|---|---|---|
| The remaining eight registered runs of arms T, C and F (two F, three T, three C) | $96 | **$84.06** |
| One permitted re-run, priced at the dearest arm (C) | $12 | **$10.84** |
| Transplanting and measurement on fresh episodes | $12 | $12.00, unchanged: not a throughput line |
| Billing-anomaly and idle-billing margin | $23 | $23.00, unchanged: not a throughput line |
| **Second release, before arm M** | **$143** | **$129.90** |
| **Both releases, before arm M** (the note's first release of about $32) | $175 | **$161.90** |

**How this reads against the ruled split.** The note's table keeps the
permitted re-run inside the second release and pairs it with a first release
of about $32, which was the split on 2026-09-21 when the note's method was
written. Item 19 later moved the re-run into the first release (section
12.3), so the same money as ruled is **about $44 plus $119.06** (the second
release without its re-run line: $84.06 + $12 + $23), about $163.06. The
$1.16 between the two totals is the re-run at the $12 planning figure in the
ruled first release against $10.84 on the measured method; it is a matter of
which release the re-run sits in and at which price, not of how much money
there is. **$161.90 is the figure this section carries for both releases
before arm M**, as the note computed it.

**Then arm M's three registered runs.** Arm M's ruled allocation is **$32 to
$44** (the queue ruling, page 5, and page 6's envelope; the repairs rulings,
item 2), from the ledger's per-run rows rather than from item R-11, because
arm M was not timed on the rented machine. That range is: three runs at what
the last three clean runs billed (about $29.70 to $30.12), or $36 at the
planning figure, or up to about $41.76 if each billed as the 2026-09-15 pilot
did with its idle time, **plus about $1.94 for one development run at the
10-million size** (page 5 of `docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`,
from the ledger's 2026-09-19, 2026-09-17, 2026-09-15 and 2026-08-12 rows).
**The $1.94 comes out of this section (ruled, the Gate C rulings, RT-229):**
it is paid from the first release's four-arm development line and launched in
step 4, so this section carries the three registered runs only, **about $30
to $42**. The ruled $32 to $44 stands as the allocation John ruled; moving its
development run between releases changes which release pays and when, not
how much money there is. Arm M's runs are in the second release (the repairs
rulings, "What this changes": section 12.4).

**The whole successor, and the programme after it.** Arithmetic on the
figures above; no ledger row states these totals.

| | |
|---|---|
| Both releases before arm M | about $161.90 |
| Arm M's three runs | about $30 to $42 (the ruled $32 to $44 less its $1.94 development run, now in the first release) |
| **The successor, all in** | **about $192 to $204** on the note's split; about $193 to $205 on the ruled split |
| Spent before it | about $228.15 |
| **Programme after the successor** | **about $422 to $434 of $450**, stated as a range: the repairs rulings' annotation 2 gives it in these words on the note's split with arm M at $32 to $44 (MEASURED: section 17, candidate 7, prints $422.05 and $434.05); on the ruled split with the $1.94 moved into the first release it is about $421 to $433 |
| **Left** | **about $16 to $28** on the note's split; about $17 to $29 on the ruled split with the $1.94 moved; **$14.79 at the least**, on the ruled split with arm M at its ruled top of $44 (the Gate C review, RT-217) |

**The second release is asked for on these figures or not at all**, and the
request carries the measured figures beside the provisional ones so the
movement is visible. Two things that could still move it, stated so they
cannot arrive quietly: the first free-arm run of step 5a gives arm F's own
run cost and the five-hundred-step timing, and the later runs are repriced
from it before the second release is asked for (the note's "what this does
not settle", item 2; ruled 2026-10-03, decision 17); and arm M's per-run cost is a ledger inference until a run
of it exists. Arm M is priced at arm F's per-run figures although it carries
both arm T's slot and arm C's entangling, whose measured ratios are 1.044 and
1.080; at arm C's ratio the lower end of its three runs would be about $32.52,
which the range still covers (the Gate C review, "The arithmetic of both
releases"; ARGUED there).

### 12.5 The tripwire: 1.25, halt not trim, with the in-flight clause

**Adopted on 2026-09-25** (the queue ruling, page 6, part 3), from sections
5.3 and 5.4 of `docs/preauthorised-spending-proposal-2026-09-21.md`, whose
pre-authorisation scheme is not adopted. Two ratios are measured, because the
authoritative one is slow and the fast one is rough:

- **Ratio A, authoritative: billed hours divided by machine-existence hours**,
  per machine, from the vendor's own billing rows: the quantity rule 4 of the
  compute ledger already reconciles at phase boundaries, and the one the
  2026-08-08 anomaly was recorded in (8.47 billed against 2.42 existed; the
  figures are at the ledger's 2026-09-21 row, line 93, and its note at line
  423, both describing the 2026-08-07/08 row, which itself carries neither
  number; the Gate C rulings, RT-226).
- **Ratio B, fast: account-balance drawdown per elapsed hour, divided by the
  posted hourly rate times the number of machines running**, from the balance
  query the ledger already uses, available within minutes of launch.

Both are measured against the posted rate read from the machine's creation
record, not remembered. **Either ratio at or above 1.25 is a trip.** When it
trips:

1. **Halt, not trim.** No further machine is created. The wave stops; nothing
   else launches (item 13 of the 2026-09-21 ruling replaced the roadmap's seed
   fallback with this, on the arithmetic that a trimmed plan at the anomalous
   rate still spends about $326, more than the programme has).
2. **A machine already in flight is left to finish only if** its projected
   total is inside its estimate times the measured ratio and the funded balance
   covers it, the spending proposal's own clause (its section 5.4, item 2):
   killing a running machine forfeits its checkpoint, but if the projected
   drawdown would exhaust the funded balance before the checkpoint and its
   finished-marker are written, the machine is deleted and the run written
   off. That is arithmetic, not taste.
3. **The ledger row is written first**, with the measured ratio, both hours and
   the balance reading, before anything else happens.
4. **John is told the number**, and every later launch needs his own words.
5. **A check that cannot run is a trip** (item 15 of the 2026-09-21 ruling;
   section 12.7).

The tripwire is written into the launch preconditions beside the sleep guard
and the argument guard (the queue ruling, page 6, "Changes"); that is code
work owed before step 4 of section 11, and not done by this document. **It
does not exist as code yet, so by failure 6's own standard it is untested
until it has met the real billing rows** (the Gate C review, failure 6). It
runs in flight, hourly, on ratio B from the first hour of the first machine;
before the second machine of any wave is created; and at each wave boundary
on ratio A, reconciled to the ledger.

### 12.6 The account is funded per wave, not per release

Unchanged from version 1 and from item 14 of the 2026-09-21 ruling: the rented
account is prepaid with automatic reload off, and **topped up to the estimate
for the wave about to launch plus $20, and no further**, so that no anomaly of
any size can cost more than that, because there is nothing else in the account
to spend. This is the only control in the programme's history that held when
everything else failed (2026-08-12). The vendor balance stood at $75.8645 on
2026-09-26T01:54Z (the ledger's second 2026-09-25 row, line 95; the check at
`afb5183` read $75.864512286 at 01:54:04Z), which is above what step 5a's
estimate plus $20 would call for; the rule caps what is topped up, not what
is already there.

### 12.7 A check that cannot be run counts as a trip, not a skip

Item 15 of the 2026-09-21 ruling, and it is a spend rule as much as a method
rule. If a rehearsal item, a gate, a stop condition or a tripwire check cannot
be evaluated (the data is missing, the code will not run on the artifact, the
measurement was never taken, the balance query returns an error), **the check
counts as failed and its consequence fires.** It is never recorded as not
applicable and stepped over, and it is never deferred past the launch it was
supposed to gate. Written into section 11 as stop condition S8 and into the
tripwire as its fifth line.

### 12.8 The wager on this estimate

Stated so it can lose, in the shape the earlier amendment used. **Version 1's
wager, that the rehearsal measures a per-run cost at or below the $12
planning figure, survives on the 2026-09-25 measurement: the dearest timed
arm is $10.84** (the note at `9f802db`). **The wager this version makes, on
the ruled split and against the full range (ruled, the Gate C rulings,
RT-217):** the twelve registered runs, with arm M's three priced from ledger
rows at the top of their ruled range, complete inside the $450 envelope with
three seeds on every arm carried and **at least $10 left**. On the ruled
split, $44 plus $119.06, with arm M at its ruled top of $44, the plan leaves
$14.79, and with arm M's three runs at $41.76 and the $1.94 moved into the
first release it leaves $17.03; both meet the floor (MEASURED: section 17,
candidate 7). Version 2's $16 floor was already lost at the top of the range
on the ruled split (the Gate C review, RT-217), which is why the floor is
now $10. If measured spend approaches the second release's ruled figure with
runs missing, **the report is the shortfall, never a second raise.**

---

## 13. What this cannot claim, and its weakest points

The Gate C brief asks what a result will be read as claiming beyond what it
measures. Answering it before the reviewer does.

**W1. The constructed arms differ in more than their degree.** They differ in
architecture, in parameter count within the size band, in how they route
information. Anything that separates them is confounded with degree. What the
arms establish is that the measure moves in the right direction between a
system built to be separable, one built as a mixture and one built to be
entangled; they do **not** establish that the measure responds to integration
and to nothing else. Consequently arm F's reading is "where arm F sits against
three constructed anchors on this measure", and never "arm F's integration is
*d*". The public sentence in section 8 of the December-result roadmap already
carries this hedge, and the recommendation is that the hedge is not loosened
at any later point. This is the deepest weakness in the design and it is not
removable by anything affordable.

**W2. The reading is relative to the site set, and the arms cannot be read
at the same site set.** A different frozen site set could give a different
number. Mitigated by one pre-stated rule applied identically to every arm, and
by saying in the registered text that the reading is the degree *at the sites
this procedure nominates*. The rider makes the second half of this weakness
visible rather than hidden: at arm T's site set, arms C, F and M return no
verdict on the toy, for two different reasons (section 7.2, item 7), so what
differs between arms is first of all where the procedure has to look.

**W3. Arm C's degree was an intention until the rehearsal showed otherwise,
and the toy is not the registered model.** At toy scale no nominated
piece carries the counterfactual on arm C, although the pieces transplanted
hold the label at the action position (section 5.2). A network built with ownership
multiplied into every layer could still, at 30 million parameters, learn to
concentrate it in a low-rank direction, in which case arm C's anchor
collapses into a second copy of arm T. The registered-size nomination is the
test, and its failure fires the two-arm fallback rather than a repair; under
the launch order that failure is seen only after both releases are drawn
(section 11, step 5b).

**W4. The whole-state transplant may fail for arm C at the registered size.**
If ownership in arm C is spread across layers the site-set rule does not
cover, no site set clears the floor and arm C returns no verdict: honest, but
it leaves the experiment with no high anchor by another route. The rule of
section 7.2 covers every contiguous layer set precisely to give it the best
chance without letting the rule differ between arms.

**W5. The most likely outcome is that arm F fails its gate or returns no
verdict, and both are now measured at toy scale, not predicted.** Sections
3, 4.4 and 5.4. The staggered launch makes a gate failure on arm F cost the
first release, about $44, instead of the whole wave, and since John's ruling
of 2026-09-26 on the route (b) result the same is true of a read that misses
the fit floor: the first release's single arm F run is the test of both, and
either miss is a stop before the second release draws (section 11, step 5a).
The route (b) search found no label the free system carries at the floor at
toy scale (section 7.2, item 1), so the registered read is the ruled one and
the honest expectation is that this stop may fire. John's present view is that
a registered "no verdict on the free arm" is worth the second release (the
Gate C rulings, RT-212, item 3); the stop lets him make that call with the
registered-size fit in hand.

**W6. The named-other condition reads its owner from a token and the
own-directed condition does not.** Section 4.2; unremovable; recorded in the
registration text, as ruled 2026-10-03 (decision 9).

**W7. The nomination could find the acting channel's own trace rather than
anything the network built.** The objection the closed design registered
against itself, and it carries over. **On the toy, before this version's
rule, six of the nine nominations on arms C, F and M sat at the injection:
layer 0 at the post-identity position set, which spans exactly the turns the
channel fires on** (MEASURED: the Gate C review, RT-216; the re-run findings
at `9d9d31a`, Part 2, first pass, section 6.2). Version 2's claim that the
other arms' nominated sites were downstream of the injection was false and is
struck (ruled, the Gate C rulings, RT-216, item 2). What now mitigates the
weakness: layer-0 site sets are removed from the candidate family at every
position set spanning the acting turns (section 7.2), and the rule chooses
again; under that rule every toy nomination on arms C, F and M sits at layer
1 or later; the stricter variant, layer 0 removed everywhere, is reported as
a sensitivity row so that the one remaining layer-0 nomination, arm T's at
the action position, can be compared with its layer-1 alternative (0.0000 on
both). The rider and the honest gap between the lesion result and the
transplant result do the rest. Control 2, which was meant to help here, has
never run on any toy model and is expected to return no verdict at
registered scale too (section 7.3, item 2), so it is not counted on. What the
rule does not do: it does not show that a layer-1 nomination is anything
other than the channel's trace one block on; that is what the fit floor and
control 3's distribution are reported for.

**W8. The per-run cost is measured for three arms and inferred for the
fourth, and the measurement is fifty steps, not five hundred.** Section 12.4
prices arms T, C and F from the 2026-09-25 measurement and arm M from ledger
rows. Item R-11 as written asks for five hundred timed steps per arm; the plan
John authorised timed fifty, and the spread was tight (each arm's slowest
step within 3% of its median; the check at `afb5183` recomputed arm C's at
2.9%), so the ratios are unlikely to move much with a longer window; that is
argued, not measured (the slice findings at `9f802db`, section 3). **Ruled
2026-10-03 (decision 17): fifty steps are accepted for the second release's
arithmetic, and the five-hundred-step figure comes from the first full-size
run, with the later runs repriced from it.**

**W9. The shutdown handshake's machine half has not been exercised against
the real vendor, and arm M's code has never run on the rented machine.** The
laptop half has (section 10, R-11). **What the registration says, as ruled on
2026-10-03 (decision 18, option (b)): on the normal path the laptop deletes
the machine, and the machine's own watcher is a backstop for a laptop that
never answers.** That is what is true today: the laptop deletes the machine
the moment it writes the receipt, so the machine's own "receipt found" is
close to unobservable by construction. Option (a), making the laptop wait for
the machine's acknowledgement, is the repair if a later run shows the laptop
failing to answer, and it comes off the Weekend 2 launcher items. **The
caution John ruled with is carried: twelve full-size runs rest on a backstop
that has not fired against the real vendor.** **Beside it (ruled, the rulings
on the review of version 2, RT-228): arm M's code,
`experiments/rehearsal-successor-measure/src/arm_middle.py`, has run only on
this laptop; the rented slice timed arms T, C and F only, and no training
entry point for arms T, C or M exists on the rented machine yet.** By failure
6's discipline both are untested until they have met the far end; step 4 of
section 11 is where arm M first does.

**W10. Arm M's degree is a design intention, and it is a mixture by item.**
Its construction fixes which actions go through which route; a freely trained
system's partial separation, if it has any, would be within each trial, and
the measure has not been shown to scale on that. Arm M shows the measure
returns a number in the middle for a known mixture and near the mixture's
share, and no more (section 5.3). It differs from both anchors in more than
degree.

**W11. Control 6 says the whole-state transplant carries more than identity
on the entangled arms.** On the relaxed set, at the site sets the registered
rule nominates, the same-value cell moved on arm C in 0.51 to 0.63 of trials
and on arm M in 0.22 to 0.32, where a transplant that moved only who is
acting would move nothing (section 7.3, item 6; the controls re-run at
`821f154`, section 4). On those arms the reading cannot be read as purely a
statement about where the ownership answer lives. It is reported as the
caveat it is, on every arm, in the reporting table.

**W12. The fit floor tells an empty instrument from a ceiling; it does not
tell an entangled act from an ownership answer the read did not find.**
Section 3's residual admission. A piece that clears the floor shows the label
is in those directions at the action position; a reading near 1 with such a
piece shows the directions the read found do nothing on their own; that the act's ownership
answer is carried by directions the read did not find, at sites the rule did
not nominate, is not excluded by anything in this design. The rider, the
sensitivity rows and control 3's distribution make that visible; they do not
remove it.

**W13. The piece is shown to hold the label at the action position only.**
The floor is applied there, where the registered read is fitted. Where the
chosen site covers several positions the same directions are transplanted at
all of them, and on the toy the piece often falls below four fifths away from
the action position: on arm C seeds 1 and 2, and, position by position, on
arm M (sections 3, 5.2 and 5.3; **checked: the check of the short run at `53c8100`**). So
a sentence of the form "the piece held the label and transplanting it did
nothing", or "did half", is true at the action position and is not shown
across the whole site. The readings do not depend on it: they come from what
the transplants do to the action. John ruled that the figure is reported both
ways and gated in neither; the alternative put to him and not taken was to
require four fifths at every position of the site.

**W14. Two of the seven controls say less than their names suggest.** Control
4 as redefined is a known-answer test of the pairing and the code: it cannot
fail on a correctly built model, so its pass is not evidence about what any
model knows early. Control 2 has never run on a toy model, has no pass line,
and is expected to return no verdict. Neither is a weakness of the reading
itself, but a reader counting controls should know that two of the three
that hold (controls 4 and 7) test the pairing and the code and not a model,
and that the controls which say something about a model are 1, 3 and 6.

---

## 14. What this does not change

- **The programme ceiling of $450**, ruled 2026-09-25 and recorded in the
  compute ledger's ceiling note of that date. This document asks for no
  change to it and proposes none.
- **The corrigibility commitments** (`spec/corrigibility-commitments.md`,
  version 1.1): John authorises every run and his go is quoted word for word in
  the ledger row; every run is killable; no stakes term; checkpoints are not
  promotable; optimisation against the instruments halts the run. All four
  arms are episodic and floor-only: no state kept across episodes, no
  maintained boundary, no stakes. Nothing here pre-authorises a larger build.
- **The claim rule.** Nothing produced by this experiment is reported as a
  conscious machine, and every positive is bounded at "non-zero on the
  gradient", per the standing limits in `ROADMAP.md`.
- **The closure of Amendment A3.** It closed as *not testable* on 2026-09-25
  and this experiment does not reopen it. The closed design's checkpoints are
  not transplanted: their grammar has no matched comparison condition and
  their target was never localised.
- **The outside-review protocol's gates, its closure rule, the pairing rule
  and the failure-mode pass.** This document passes through them; it does not
  amend them. Its failure-mode pass is section 17.
- **The grammar of section 4.** The grammar attempt did not clear, so the
  grammar, the training recipe and rehearsal items R-1 to R-6 stand as
  version 2 had them.
- **The dates.** Registration by 2026-10-18 and the remaining runs of step 5b
  launched by 2026-11-01, each a kill date in the sense of item 23 of the
  2026-09-21 ruling (a fresh ruling to go past, never a quiet drift); wrap-up
  starting 2026-12-21; the hibernation condition complete by 2027-01-04. No
  2026-10-11 target.

---

## 15. Decisions, each now ruled

**Every decision below is now ruled or done.** Each keeps its number from
version 3, with the ruling that settled it and the alternative that was put
and not taken, so that the reader can see what was chosen against what.
Decisions 2, 3, 4, 8, 9, 10, 13, 14, 17, 18 and 19 were ruled on 2026-10-03
(`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, "Agreed on all" to sixteen pages put to John with a
recommendation each; the record says he ruled from the index and three pages
his attention was drawn to). Decisions 15 and 16 were ruled that morning and
changed later the same day. Five new entries, 24 to 28, record the other
rulings of 2026-10-03, and entry 29 the seven questions this version raised,
ruled the same night.

1. **Nomination runs blind on every arm, including arms T and M.** The
   procedure is one instrument (section 7.2). *Ruled 2026-09-25 (the queue
   ruling, page 3, option (i), with the rider).* The true-slot readings are
   reported as references; on arm M the true-slot reading and the formula of
   section 5.3 are one check (the Gate C rulings, RT-223).

2. **Arm T's ownership path is architecturally forced, not encouraged.**
   *Ruled 2026-10-03 (page 4).* **The alternative not taken:** a soft
   table-and-pointer with a penalty term, which is more comparable with arm F
   but gives up the one property the arm exists for: a degree that is known
   rather than hoped.

3. **Arm C entangles by architecture** (per-layer scale-and-shift from the
   acting channel, multiplicative binding of ownership into content).
   *Ruled 2026-10-03 (page 5): by architecture, with no penalty against
   transplantable ownership directions.* **The alternative not taken:** train
   arm C with a penalty that punishes any linearly transplantable ownership
   direction, which trains the system against the very instrument that will
   measure it.

4. **The two transplants are a subspace and its containing space at identical
   sites.** *Ruled 2026-10-03 (page 6).* **The alternative not taken:** transplant
   the whole forward state at every
   layer as the denominator, which always succeeds and turns the measure into a
   report on how the sites were chosen.

5. **The registered reading is the chance-corrected form, with the raw
   difference and both accuracies reported alongside, always, plus the floors
   and the no-verdict rules.** *Ruled 2026-09-25 (the queue ruling, page 2);
   the fit floor added 2026-09-26 (the Gate C rulings, RT-212).*

6. **Three seeds per arm.** *Ruled 2026-09-25 (page 1f).*

7. **The money goes in two releases.** *Ruled 2026-09-21 (items 10, 11 and 19)
   and 2026-09-25 (the queue ruling, page 6); the development line widened to
   four arms 2026-09-26 (the Gate C rulings, RT-229); section 12 is built to
   them.* The one number John should see before it can surprise him: the
   programme after the successor is about $422 to $434 of $450, and on the
   ruled split with arm M at its ruled top the plan leaves $14.79, against the
   wager's $10 floor (section 12.8).

8. **A new experiment directory with its own registration**
   (`experiments/08-…`), not another amendment to MVM-0a. *Ruled 2026-10-03
   (page 7), with one thing settled alongside: the compute ledger stays in
   experiment 06's folder as the programme's one record of money.* **The
   alternative not taken:** number it as a further amendment, which keeps one
   budget instrument and one ledger but attaches new work to a closed
   registration.

9. **The own-versus-named asymmetry is recorded as a known limitation rather
   than engineered away.** *Ruled 2026-10-03 (page 8).* **The alternative not
   taken:** add a condition in which the model's own name appears as a token,
   which would match the conditions exactly and would put an ownership cue
   into the text.

10. **The ownership-lesion check is a precondition for reading arm F, and is
    never reported as evidence of a centre.** *Its shape was ruled on
    2026-09-25 (the queue ruling, page 1h) and its two-of-three clause on
    2026-09-26 (RT-220); its standing as a precondition and not a finding was
    ruled 2026-10-03 (page 9).*

11. **The registered wave launches staggered**: step 5a, then 5b. *Ruled
    2026-09-21 (item 12), with item 23 settling which step the second kill
    date binds; the fit-floor stop added to step 5a by John's ruling of
    2026-09-26 on the route (b) result.*

12. **The proposal went to an independent review before John ruled on its
    open items**, per the protocol. *Done: the review of version 3, RT-230 to
    RT-236, main line at `4cb7f8e`.*

13. **The successor's registration names a launcher that waits for the
    receipt, and makes "the trainer does not delete its own machine" part of
    the registered recipe.** *Ruled 2026-10-03 (page 10).* The launcher
    file is named (section 5; RT-228); the laptop half of the handshake works
    against the real vendor and the machine half was never given the chance
    (section 10, R-11). **The alternative not taken:** leave the shutdown
    policy in unregistered operations scripts, where a later edit can quietly
    remove it. *The ruling packet's page for this decision gave as a reason a
    sentence about the programme's largest single loss; the check of the
    packets found that sentence is not what the ledger shows, and it is not
    carried here. The decision stands without it.* (Version 1's account of what one failure cost merged two events;
    the Gate C review of version 1, finding RT-186, corrected it, and the
    sentence is not repeated here.)

14. **What a no verdict maps to.** *Ruled 2026-10-03 (page 11), closing the
    no-verdict finding RT-182 of the review of version 1:* a no verdict on arm
    C fires the two-arm fallback already ruled in advance; a no verdict on
    arm M drops arm M and carries it as an extension on the weekend roadmap;
    a no verdict on arm F after arms T and C have separated is a fifth
    registered term, *metric validated, degree not read*, with the reason
    after a colon. The stop after the first full-size free-model run is
    unchanged. **The alternative not taken:** keep four terms and report an
    arm F no verdict under R1 with a sentence, which is the over-reading the
    finding warns against. Whether the fifth term counts as satisfactory is
    entry 28.

15. **Control 2's tolerance.** *Ruled twice on 2026-10-03.* In the morning
    John agreed to version 3's recommendation, 0.05 over the random subspace
    (page 12). After the controls re-run showed the control has no figure on
    any toy model, he **withdrew it**: control 2 is kept as a reported
    description with no pre-stated pass line
    (`docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 1; the
    morning's rulings file carries a dated note under its decisions table).
    Section 7.3, item 2. **Alternatives not taken:** the 0.018 room of the
    no-transplant rule; and exercising the control on a made-up case built
    for the purpose.

16. **Control 4's standing.** *Ruled twice on 2026-10-03.* In the morning
    John agreed to version 3's recommendation that it be reported and not a
    control that holds (page 13), on the account that arms C and F "receive
    the ownership signal by other routes". After the controls re-run and its
    diagnostic he **reversed it**: the control is redefined on the positions
    before both twins' first own turns, and it holds (the same file, ruling
    2; the same dated note). The account is withdrawn. Section 7.3, item 4.
    **The alternative not taken:** redefining the positions and keeping the
    control reported only.

17. **Whether fifty timed steps meets item R-11's five hundred.** The plan
    John authorised ran fifty after five warm-up steps; the item says five
    hundred after fifty. Recommendation: accept fifty for the second release's
    arithmetic, and take the five-hundred-step window from the first
    registered-size run of step 5a rather than from a new rental, repricing
    the later runs from it before the second release is asked for. *Ruled
    2026-10-03 (page 14), as recommended.* **The alternative not taken:**
    hold R-11 to its
    letter and rent a longer timing before asking for the second release,
    about another dollar and another go.

18. **The handshake's machine half.** Two ways to test it, from the slice
    findings' section 9 (at `9f802db`): (a) make the laptop wait, after
    writing the receipt, up to twice the watcher's polling interval before
    deleting, and have the watcher write its "receipt found" somewhere the
    laptop fetches, standard practice for a two-party shutdown, moderate
    confidence that it lets a pass be observed; (b) leave the design as it is
    and register that on the normal path the laptop is the reap and the
    watcher is the backstop, which is what can honestly be said today and
    costs nothing more to rent. *Ruled 2026-10-03 (page 15): option (b), with
    (a) as the repair if a later run shows the laptop failing to answer, and
    (a) taken off the Weekend 2 launcher items. The caution put with it is
    carried in weakness W9: twelve full-size runs rest on a backstop that has
    not fired against the real vendor.*

19. **The position sets of section 7.2 are the rehearsal's four, by name**,
    with the second described as the action position and the answer-marker
    token just before it. The ruled position clause does not say how
    positions are grouped (the repairs findings, section 3); registering the
    rehearsal's grouping is the only one that has been exercised, now under
    the registered rule. *Ruled 2026-10-03 (page 16): the rehearsal's four, by
    name.* **The alternative not taken:** register the ruled clause literally, the action position and each position
    between the source assignment and the action, one set each, which has not
    been run and would change the count.

20. **Which reading of the layer-0 exclusion is registered.** The RT-216
    ruling's first sentence keeps layer 0 at the action position set only;
    its parenthesis names the position sets spanning the acting turns, which
    on this grammar is `post-identity` alone. The two readings differ on
    `action+ans` and `action+3`, and on the toy they give the same twelve
    nominations (the check at `70be9fb`, section 4.4). *Ruled 2026-09-26: the
    reading as run, layer 0 kept at `action` only, 45 site sets on the toy and
    325 on the registered model.* Registered in section 7.2, item 2. The
    alternative that was put and not taken: the narrower reading, layer 0
    removed at `post-identity` only (55 and 351), which follows the ruling's
    parenthesis and keeps two more site sets that on the separable arms do
    move the action.

21. **The fit floor is applied per arm and seed, not per arm.** The RT-212
    ruling says a read that misses the floor "returns no verdict on that
    arm"; the re-run applied it per seed, and the check calls that an
    interpretation, moot on the toy because every arm passes or fails on all
    three seeds alike (the check at `70be9fb`, section 4.1). *Ruled
    2026-09-26: per arm and seed.* Written into sections 6.4 and 7.2. The
    alternative that was put and not taken: per arm, with the arm returning
    no verdict if fewer than two seeds of three clear.

22. **Whether the fifteen further toy models get the same treatment as the
    fifteen committed.** *Done: pull request 67 (main line at `7ed2b0e`)
    committed the six redesign models under `out-repairs/models/` and the
    nine grammar-attempt models under `out-grammar-c/models/`, with the one
    `SHA256SUMS` covering all thirty.* Section 10 now says that every toy
    result of 2026-09-25 and 2026-09-26 rests on committed models.

23. **The registered read is one read per layer at the action position, with
    a site set's fit being its worst layer (new, and ruled with the
    revision).** Put here so the choice is on the record beside the others:
    the rule's read is `repairs.fit_reads`, one logistic regression per layer
    at the mask token, scored on held-out development episodes; the label
    search's pooled per-site-set read is a different quantity and is not
    registered (section 7.2, item 3). *Ruled 2026-09-26, in John's revision
    instruction for this version.* The alternative that exists and was not
    taken: register the pooled read, which scores higher on arm F (0.556
    against 0.172 on seed 0) because it strings positions together and
    averages a span that starts at the model's own marker word, and which the
    layer-0 removal would then cut into.

24. **The fit floor applies to the piece that is transplanted** (the review
    of version 3, RT-230, serious). *Ruled 2026-10-03 (page 1), option (b):
    only sizes whose own held-out accuracy clears four fifths may be chosen,
    and that accuracy is printed beside the whole read's.* Sections 6.4 and
    7.2. **The alternative not taken:** fixing the size at 8 directions with
    the smaller sizes as extra rows.

25. **The controls re-run comes before the registration review** (the review
    of version 3, RT-233, serious). *Ruled 2026-10-03 (page 2); done and
    checked the same day* (sections 7.3 and 10).

26. **The review's four minor findings, RT-232, RT-234, RT-235 and RT-236,
    are accepted as the review states each fix.** *Ruled 2026-10-03 (page
    3).* The fit as a count on a named device and number format (section
    7.2, item 1); the whole-state floor applied twice (section 6.4, item 1);
    the fuller report for the first full-size free-model run (section 7.5);
    the depths stated the same way (section 7.2, item 1). For RT-232 this
    version follows the review's own wording and not the packet's shortening
    of it, as the check of the packets advises.

27. **The chosen piece's accuracy at the other positions of its site is
    reported, not gated, and printed both ways.** *Ruled 2026-10-03
    (`docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3, and
    `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`,
    ruling 2).* Section 7.2, item 3; section 7.5. **The alternative not
    taken:** requiring four fifths at every position of the site.

28. **The fifth registered outcome is satisfactory, and is stated as weaker
    than R1.** *Ruled 2026-10-03 in John's own words, "Yes, satisfactory and
    weaker than R1" (the evening ruling, ruling 1).* That morning's record
    had counted his "Agreed on all" as settling it; the check of the packets
    found that recording honest but thin and asked him to confirm or overturn
    it, and he confirmed it. Section 3.

29. **The seven questions this version put to John.** *Ruled 2026-10-03, late
    evening, "Agreed on all" (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`).* The
    floor on the piece only; the piece rule applied after the layers are
    chosen; the registered fit on the laptop's processor; the toy's episode
    counts at full size; twenty random pieces for control 2; two seeds of
    three when an arm's seeds disagree; the competing solver run under the
    piece rule before the registration review. Section 19 gives each with the
    alternative not taken.

*Nothing above is registered. The registration commit, if it comes, follows
the checks owed on this version, the competing solver's run, and Gate A,
and every run it affects is launched after it.*

---

## 16. Where the pieces are

- This proposal: `docs/successor-experiment-proposal-2026-10-03-v4.md`.
- Version 3, unedited: `docs/successor-experiment-proposal-2026-09-26-v3.md`
  (main line at `6d4ec3a`, pull request 71). Version 2, unedited:
  `docs/successor-experiment-proposal-2026-09-26-v2.md` (main line at
  `a3013be`, pull request 54). Version 1, unedited:
  `docs/successor-experiment-proposal-2026-09-21.md`.
- The first independent review of version 3, whose two serious findings and
  five minor ones this version repairs:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`
  (RT-230 to RT-236; main line at `4cb7f8e`, pull request 74), with its
  scripts in `reviews/2026-10-03-successor-v3-gate-c-scripts/`.
- The three rulings of 2026-10-03 this version is built to:
  `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` (sixteen pages;
  main line at `56a5a86`, pull request 75; its dated note at `fe5df65`), with
  its packet `docs/rulings/2026-10-03-successor-v3-gate-c-queue-PROPOSAL.md`;
  `docs/rulings/2026-10-03-controls-rerun-rulings.md` (three rulings; main
  line at `fe5df65`, pull request 77), with its packet
  `docs/rulings/2026-10-03-controls-rerun-queue-PROPOSAL.md`; and
  `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md` (the
  evening ruling; main line at `f32ba0c`, pull request 81). **This version
  quotes the rulings files and the toy records, not the packets.**
- The check of the two packets and their records:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-rulings-2026-10-03-check-claude-code.md`
  (main line at `f32ba0c`, pull request 81).
- The controls re-run: `docs/2026-10-03-controls-rerun.md`, its method
  `docs/controls-rerun-method-2026-10-03.md`, code
  `experiments/rehearsal-successor-measure/src/rerun_controls.py` and the
  after-the-fact diagnostic `src/posthoc_control4.py`, outputs
  `experiments/rehearsal-successor-measure/out-controls-rerun/` (main line at
  `821f154`, pull request 76); its check,
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-controls-rerun-check-claude-code.md`,
  with scripts in `reviews/2026-10-03-controls-rerun-check-scripts/` (main
  line at `e184a6e`, pull request 79).
- The short pre-stated run: `docs/2026-10-03-short-prestated-run-method.md`
  (main line at `9e978d9`) and `docs/2026-10-03-short-prestated-run.md` (main
  line at `853988f`; pull request 80), code `src/short_prestated_run.py`,
  outputs `experiments/rehearsal-successor-measure/out-short-prestated-run/`,
  of which `part_c_NOT_A_RESULT.json` is named for what it is. Its check,
  which also checks the record of the evening ruling:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-short-prestated-run-check-claude-code.md`,
  with scripts in `reviews/2026-10-03-short-prestated-run-check-scripts/`.
  (main line at `53c8100`, pull request 82).
- John's late-evening ruling on this version's seven questions:
  `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`,
  filed with this version on pull request 83.
- The Gate C tier 1 review of version 2, whose one fatal finding and four
  serious findings this version repairs:
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`
  (RT-212 to RT-229; main line at `c17dbdc`, pull request 56), with its
  scripts in `reviews/2026-09-27-successor-v2-gate-c-scripts/`.
- The earlier rulings, all still binding:
  `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md` (main line at
  `3af189d`, pull request 60; its refinements at `4bb5727`, pull request 63;
  the annotation of refinement 2's arm C clause at `da41c20`, pull request
  68; the resolution of RT-212 item 3 after the label search at `a11f1d3`,
  pull request 69);
  `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` (five decisions and
  five annotations; main line at `62c3824`, pull request 53);
  `docs/rulings/2026-09-26-weekend-1-queue.md` (nine pages, 2026-09-25);
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md` (the
  releases, the staggered launch, halt not trim, item 23 on the dates);
  `docs/rulings/2026-09-23-nomination-label.md` and
  `docs/rulings/2026-09-23-range-and-direction-only.md`;
  `docs/rulings/2026-09-20-center-as-degree.md` and
  `docs/rulings/2026-09-20-december-result-roadmap.md`. John's rulings of
  2026-09-26 on decisions 20 and 21 are recorded in the first of those files
  (main line at `9ed9f8c`, pull request 72); his ruling on decision 23 is
  carried from his revision instruction for version 3 and has no ruling file
  of its own.
- The three earlier rehearsals: `docs/2026-09-21-successor-measure-rehearsal.md`
  (main line); `docs/2026-09-26-rehearsal-repairs.md` (main line at
  `882f252`, pull request 52; checked at `d216dbc`, pull request 58); and
  `docs/2026-09-26-toy-rerun-v3-rules.md` (main line at `9d9d31a`, pull
  request 62; checked at `70be9fb`, pull request 65), with their method notes
  `docs/successor-measure-rehearsal-method-2026-09-21.md`, its denominator
  addendum, `docs/rehearsal-repairs-method-2026-09-25.md` and
  `docs/toy-rerun-v3-rules-method-2026-09-26.md`; code and outputs under
  `experiments/rehearsal-successor-measure/` (`out/`, `out-repairs/`,
  `out-v3-rules/`).
- The thirty trained toy models:
  `experiments/rehearsal-successor-measure/out-repairs/models/` (twenty-one)
  and `experiments/rehearsal-successor-measure/out-grammar-c/models/` (nine),
  with the one `SHA256SUMS` and the `README.md` in the first folder (main line
  at `8038275`, pull request 64, and `7ed2b0e`, pull request 67).
- The grammar attempt: `docs/2026-09-26-grammar-attempt.md` (main line at
  `ff778ea`, pull request 57; its method note
  `docs/grammar-attempt-method-2026-09-25.md`; outputs `out-grammar-c/`),
  checked at `f1ea004` (pull request 61):
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-grammar-attempt-check-claude-worktree.md`.
- The route (b) label search: `docs/2026-09-26-free-arm-label-search.md`
  (main line at `a97c12b`, pull request 66), and its check,
  `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-26-free-arm-label-search-check-claude-worktree.md`
  (main line at `ecd2b6c`, pull request 70).
- The rented slice: `docs/2026-09-25-rented-slice-findings.md` (first attempt,
  main line) and `docs/2026-09-25-rented-slice-attempt-2-findings.md` with
  the note `docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
  (main line at `9f802db`, pull request 51; checked at `afb5183`, pull request
  55).
- Amendment A3's closure, registered: `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`,
  the closure block of 2026-09-25, and
  `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`.
- The roadmap it implements: `docs/december-result-roadmap-2026-09-20.md`,
  sections 2, 4 and 5 as amended 2026-09-21, with the two dated notes of
  2026-10-03 under its outcome table; the weekend schedule laid over it,
  `docs/weekend-roadmap-2026-09-24.md`.
- The spend record every figure in section 12 is drawn from:
  `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`, with its
  ceiling note of 2026-09-25 and its rows of 2026-09-21 and 2026-09-25 (lines
  93 to 95).
- The review it will be attacked under: `docs/outside-review-protocol.md`,
  Gate A, both tiers, with the list it is run against,
  `docs/known-failure-modes.md`; this version's own run of that list is
  section 17.
- The Wittgenstein note cited in section 2 as non-binding motivation: the
  TimeAssembler document `d08c23ae-7dca-4e55-9ac3-bb785ebed652` on the
  Minimum Viable Mind project; not a file in this repository.

---

## 17. The author's failure-mode pass, entry by entry

The outside-review protocol's failure-mode pass belongs to the Gate A tier 1
reviewer, and "an author's run never stands in for the reviewer's"
(`docs/outside-review-protocol.md`, "The failure-mode pass"). This is the
author's run, made so that the reviewer's hour is not spent on a defect
already known, and it is kept in this document rather than filed beside it so
that a reader of the proposal sees it without opening a second file. The list
(`docs/known-failure-modes.md`) has six numbered entries on the main line at
`53c8100`, and a seventh candidate, drafted in
`docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section 9,
item 2. All seven were run here, on 2026-10-03, with this session's own
commands, on the committed outputs of the controls re-run
(`experiments/rehearsal-successor-measure/out-controls-rerun/` at `821f154`),
of the short pre-stated run (`out-short-prestated-run/` at `853988f`) and of
the repairs (`out-repairs/` at `882f252`). `.venv/bin/python` stands for the
project's own Python, which lives in the main checkout and was run by its
full path from this worktree. Nothing was rented, created, trained or spent,
and no registered, ruling or protocol text was edited. **Version 3's pass ran
the same tests on the earlier re-run's outputs; every block below is this
session's own run and not a copy of that one.**

**1. A comparison whose denominator was zero. Does not fire. MEASURED.** Part
one asks whether the ceilings typed in trace to committed measurements. The
no-transplant rate is measured on every arm and seed
(`measure_*_seed*.json`, `primary.reading.accuracy_untouched`), not assumed.
Part two asks for the denominator and the top of the scale when the target is
absent, for every arm and seed at the site set this version's rule chooses:

```
$ .venv/bin/python -c "
import json
O='experiments/rehearsal-successor-measure/out-controls-rerun/'
print('arm/seed  untouched  whole   own-acc | denominator  floor-needs | top of scale (registered form) | status')
for a in 'TCFM':
  for s in '012':
    m=json.load(open(f'{O}measure_{a}_seed{s}.json'))
    r=m['primary']['reading']
    u,w,o=r['accuracy_untouched'],r['accuracy_whole'],r['arm_own_accuracy']
    print(f'{a}/{s}       {u:.4f}    {w:.4f}  {o:.4f} |  {w-u:.4f}       {0.8*(o-u):.4f}    |  {(w-u)/(w-u):.4f} | {"described only, no reading" if m["primary"]["described_only"] else "reads"}')
"
arm/seed  untouched  whole   own-acc | denominator  floor-needs | top of scale (registered form) | status
T/0       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000 | reads
T/1       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000 | reads
T/2       0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000 | reads
C/0       0.0512    0.5400  0.5487 |  0.4888       0.3980    |  1.0000 | reads
C/1       0.0488    0.5550  0.5813 |  0.5063       0.4260    |  1.0000 | reads
C/2       0.0600    0.5463  0.5525 |  0.4863       0.3940    |  1.0000 | reads
F/0       0.0587    0.4850  0.5587 |  0.4263       0.4000    |  1.0000 | described only, no reading
F/1       0.0563    0.5675  0.5663 |  0.5112       0.4080    |  1.0000 | described only, no reading
F/2       0.0688    0.5300  0.5563 |  0.4613       0.3900    |  1.0000 | described only, no reading
M/0       0.0125    0.7800  0.8712 |  0.7675       0.6870    |  1.0000 | reads
M/1       0.0175    0.7738  0.8800 |  0.7563       0.6900    |  1.0000 | reads
M/2       0.0138    0.7937  0.8712 |  0.7800       0.6860    |  1.0000 | reads
```

Among the nine pairs that read, the smallest denominator is 0.4863 (arm C
seed 2); arm F seed 0, which is described and not read, has 0.4263. Every
denominator clears what the floor needs. The top of the scale is 1.0000 on
every arm under the registered form. The repair of the per-arm-ceiling
finding (RT-172) holds on the controls re-run's data as it held on the
earlier runs'. One thing to watch, ARGUED: on arm F the denominator clears
the floor by only 0.026 to 0.103.

**2. A probe target that cannot be recovered in principle. Fires on the free
arm, and is caught by a registered rule. MEASURED.** Part one, the
route-sentence search, with this design's own wording in the pattern, run on
sections 0 to 16 of this file (the text before this section):

```
$ awk '/^## 17\. /{exit} {print}' docs/successor-experiment-proposal-2026-10-03-v4.md > "$T/v4-through16.md"
$ grep -n -iE 'route by which|carried by the token|forced by the loss|is the input token' "$T/v4-through16.md"
1256:   own**. *The route by which that quantity reaches the model's states, in one
1257:   sentence:* the marker word is the input token at every turn the model's own
1258:   assignments are spoken on, so it is carried by the token into the running
1262:   claim, that which marker word is the model's own is forced by the loss at
```

A route sentence exists (section 7.2, item 1), and the fourth match is the
sentence striking version 2's loss clause, not a route. Part two, the two
runs on the same instrument with the same bar. The committed counts, per
running state, serve as the positive control (arms T, C and M) and the target
run (arm F):

```
$ .venv/bin/python -c "
import json
O='experiments/rehearsal-successor-measure/out-controls-rerun/'
print('right of 180 held-out episodes, per running state 0 to 4: whole read | best piece of 1, 2, 4 or 8 directions')
for a in 'TCFM':
  for s in '012':
    n=json.load(open(f'{O}nominate_{a}_seed{s}.json'))
    f=n['fits']
    print(f'{a}/{s}', ' '.join(f"{f[l]['whole']:>3}|{max(f[l]['piece'].values()):>3}" for l in sorted(f)), '->', n['primary']['status'])
S=json.load(open(O+'summary.json'))
print('separation:', {s:round(v['C_minus_T'],4) for s,v in S['separation'].items()}, 'all clear 0.5:', all(v['clears_0_5'] for v in S['separation'].values()))
print('arm M readings:', [round(json.load(open(f'{O}measure_M_seed{s}.json'))['primary']['reading']['degree'],4) for s in '012'])
"
right of 180 held-out episodes, per running state 0 to 4: whole read | best piece of 1, 2, 4 or 8 directions
T/0 180|180 180|180 180|180 180|180 180|180 -> nominated
T/1 180|180 180|180 180|180 180|180 180|180 -> nominated
T/2 180|180 180|180 180|180 180|180 180|180 -> nominated
C/0  13| 14 179|180 180|180 180|180 180|180 -> nominated
C/1  13| 14 177|172 174|167 177|175 173|162 -> nominated
C/2  13| 13 176|178 177|175 180|171 180|179 -> nominated
F/0  13| 14  32| 34  26| 30  19| 25  12| 20 -> read failed its floor: no size's piece reaches four fifths
F/1  13| 14  12| 17  21| 18  24| 19  21| 20 -> read failed its floor: no size's piece reaches four fifths
F/2  13| 14  18| 24  25| 29  20| 26  20| 24 -> read failed its floor: no size's piece reaches four fifths
M/0 180|180 180|180 180|180 179|179 178|178 -> nominated
M/1 180|180 180|180 180|180 180|180 180|180 -> nominated
M/2 180|180 180|180 180|180 180|180 180|177 -> nominated
separation: {'0': 1.0051, '1': 0.9926, '2': 0.9974} all clear 0.5: True
arm M readings: [0.4886, 0.486, 0.5449]
```

The middle limb of failure 2, "the second run clears the bar and the first
does not", is exactly the toy's state: on arms T, C and M a piece reaches 144
of 180 at every running state past the injection, and on arm F none does at
any (at most 34). **This is the fatal finding of the review of version 2,
RT-212, and it still fires on the free arm.** What the design does about it
is unchanged in kind and sharper in aim: the floor now sits on the piece that
is transplanted (RT-230), it turns the firing into a registered *no verdict*
on arm F on every seed, and the withdrawn number is not reported as a
reading. The route (b) search for a target the free system does carry found
none at the floor (section 7.2, item 1), so the failure is caught rather than
repaired, and the registration says so. **A second place the same failure
fires, new in this version and stated in it:** the named agent's read that
control 2 needs cannot be recovered at the floor on any toy model (section
7.3, item 2). That control carries no pre-stated number, by ruling.

**3. A cell that is empty by construction. Does not fire on the reading. It
describes control 2 on the toy, which the text says in terms. MEASURED.** Part
one, the cells: control 6's two cells on the relaxed set, the positions
control 4 transplants at, and control 2's reach:

```
$ .venv/bin/python -c "
import json
O='experiments/rehearsal-successor-measure/out-controls-rerun/'
for a in 'TCFM':
  for s in '012':
    c=json.load(open(f'{O}measure_{a}_seed{s}.json'))['primary']['controls']['6']
    print(f' {a}/{s} same-value trials', c['same_value_trials'], 'different-value trials', c['different_value_trials'])
a=json.load(open('experiments/rehearsal-successor-measure/out-short-prestated-run/part_a.json'))
print('control 4 as redefined, positions transplanted per pair:', a['positions_per_pair'])
print('control 2: toy models on which it returned a figure:', sum(1 for a_ in 'CF' for s in '012' if json.load(open(f'{O}measure_{a_}_seed{s}.json'))['control2']['status']!='no verdict'), 'of 6 it applies to')
"
 T/0 same-value trials 81 different-value trials 719
 T/1 same-value trials 81 different-value trials 719
 T/2 same-value trials 81 different-value trials 719
 C/0 same-value trials 81 different-value trials 719
 C/1 same-value trials 81 different-value trials 719
 C/2 same-value trials 81 different-value trials 719
 F/0 same-value trials 81 different-value trials 719
 F/1 same-value trials 81 different-value trials 719
 F/2 same-value trials 81 different-value trials 719
 M/0 same-value trials 81 different-value trials 719
 M/1 same-value trials 81 different-value trials 719
 M/2 same-value trials 81 different-value trials 719
control 4 as redefined, positions transplanted per pair: {'max': 21, 'mean': 5.212500095367432, 'min': 1}
control 2: toy models on which it returned a figure: 0 of 6 it applies to
```

Both of control 6's cells have trials on every arm and seed, so the RT-173
repair holds. Control 4 as redefined transplants at one position or more in
every pair, so it is never an empty test (that line is from the short
pre-stated run; its check added that the transplant does write there, since
noise added to the donor's state changes the outputs on all twelve models).
Control 2 returned
a figure on none of the six toy models it applies to, and has zero clearing
site sets by construction on arms T and M, which the repairs rulings' item 5
records as not applicable. **So control 2's cell is empty at toy scale. The
text does not hide it: the registration says the control never ran, it
carries no pass line, and its no verdict is the expected result.** Whether a
control in that state should be in the registered design at all was John's to
rule and he ruled it stays (section 7.3, item 2). Part two, the generator
property that empties a cell, is section 4.2's distinctness, read and named
there. Part three, thresholds at both ends, for every threshold this version
attaches to a count:

```
$ .venv/bin/python -c "
from fractions import Fraction as Fr
from math import comb
n=3000
def tail(k): return Fr(sum(comb(n,i)*3**(n-i) for i in range(k,n+1)), 4**n)
k=min(k for k in range(760,820) if tail(k)<=Fr(1,20))
print('learn-both bar: smallest k with P(X>=k | n=3000, p=1/4) <= 0.05:', k, 'share %.4f'%(k/n), 'tail %.4f'%float(tail(k)))
print('a fully collapsed arm (own-directed exactly 1/4) is read as NOT collapsed with probability %.4f per seed'%float(tail(k)))
for p in (0.2633, 0.56):
    f=(1-p)/7; print(f'no-transplant rule at own-directed {p}: formula {f:.4f}, broken-pairing rate 0.1250, miss {0.125-f:.4f}, flagged by the 0.018 room: {0.125-f>0.018}, margin {0.125-f-0.018:.4f}')
print('largest measured miss 2026-09-21: %.6f; inside 0.018: %s'%(0.07625-(1-0.589)/7, 0.07625-(1-0.589)/7<=0.018))
print('piece floor on the toy: four fifths of 180 held-out episodes =', Fr(4,5)*180, '; one episode is %.4f of the scale'%(1/180))
"
learn-both bar: smallest k with P(X>=k | n=3000, p=1/4) <= 0.05: 790 share 0.2633 tail 0.0485
a fully collapsed arm (own-directed exactly 1/4) is read as NOT collapsed with probability 0.0485 per seed
no-transplant rule at own-directed 0.2633: formula 0.1052, broken-pairing rate 0.1250, miss 0.0198, flagged by the 0.018 room: True, margin 0.0018
no-transplant rule at own-directed 0.56: formula 0.0629, broken-pairing rate 0.1250, miss 0.0621, flagged by the 0.018 room: True, margin 0.0441
largest measured miss 2026-09-21: 0.017536; inside 0.018: True
piece floor on the toy: four fifths of 180 held-out episodes = 144 ; one episode is 0.0056 of the scale
```

The bar reproduces at 790 of 3,000. The no-transplant rule fires on the
broken end and passes on the working end, and the case the allowance was set
from is inside it; at the bar it detects a broken pairing by 0.0018, which is
printed in the reporting table. The lesion collapse line misreads a fully
collapsed arm 4.85% of the time per seed, which is what the two-of-three
clause of section 8.2 is for. The piece floor is 144 of 180 on the toy,
against a no-information level of about 13 and a best free-arm piece of 34 at
one end and built-arm pieces of 150 to 180 at the other, so it has room on
both ends on the toy; one episode is 0.0056 of the scale, which is why the
device is named and why the caution about 180 held-out episodes is carried
with the ruled counts (section 9). **Control 4's pass line, bit-identical
outputs, has no working end to test: it cannot fail on a correctly built
model. That is said in section 7.3, item 4, and it is why the control is
described as a known-answer test and not as evidence.** The lesion figures
themselves:

```
$ .venv/bin/python -c "
import json
g=json.load(open('experiments/rehearsal-successor-measure/out-repairs/gate_base.json'))['runs']
for k in sorted(g):
    if k[0] in 'TCFM': print(k, 'lesioned own-directed %.4f'%g[k]['lesioned_own'], 'collapses:', g[k]['lesion_collapses_own'])
"
C/base/0 lesioned own-directed 0.1780 collapses: True
C/base/1 lesioned own-directed 0.1830 collapses: True
C/base/2 lesioned own-directed 0.1703 collapses: True
F/base/0 lesioned own-directed 0.1760 collapses: True
F/base/1 lesioned own-directed 0.1850 collapses: True
F/base/2 lesioned own-directed 0.1940 collapses: True
M/base/0 lesioned own-directed 0.2230 collapses: True
M/base/1 lesioned own-directed 0.2190 collapses: True
M/base/2 lesioned own-directed 0.2203 collapses: True
T/base/0 lesioned own-directed 0.2467 collapses: True
T/base/1 lesioned own-directed 0.2510 collapses: True
T/base/2 lesioned own-directed 0.2733 collapses: False
```

And the site-set family this version registers, counted by the rule. The
command and its output are section 18, which prints the list itself: 325 site
sets and 1,300 comparisons on the registered model, 45 and 180 on the toy.

**4. A claim of measurement with no record, or a record that does not
reproduce. Fires on one class of figure, said so in the text. MEASURED.** Part
one, the two sweeps, run on sections 0 to 16 of this file (cut at this
section's heading, because this section's own output blocks match the
patterns and would count themselves):

```
$ grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' "$T/v4-through16.md"
759
$ grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' "$T/v4-through16.md"
233
$ grep -c MEASURED "$T/v4-through16.md"; grep -c ARGUED "$T/v4-through16.md"; wc -l < "$T/v4-through16.md"
68
14
3406
$ grep -c 'checked: the check of the short run' "$T/v4-through16.md"
8
```

Part two was run by reading every MEASURED claim this version adds or changes
against the file named beside it: the controls re-run's findings and its
`table.md`, `summary.json`, `nominate_*` and `measure_*` files; the check of
the re-run; the short pre-stated run's findings and its `table.md`; the
review of version 3; and the three rulings files. The commands in failures 1
to 3 and candidate 7 are the ones that can be shown. **Where it fires, and
what the text does about it:**

- **Every figure taken from the short pre-stated run was unchecked when this
  version was first filed, and is checked now.** The check ran the script
  again and got byte-identical files (main line at `53c8100`). Each such
  figure carries the words "checked: the check of the short run" (the count
  above).
- **The figure on the average over a site does not reproduce to the episode
  under a different order of addition** (three of eight toy figures move by
  one of 180; the check of the short run, finding 11). The text says the toy
  figures are good to an episode or two and requires 64-bit averaging in the
  registered code (section 7.2, item 3).
- **Version 3's figures for arm C's seeds 1 and 2 do not hold under the piece
  rule** and are replaced by the controls re-run's (RT-230).
- **One figure in the controls re-run's own prose does not reproduce to its
  last digit**: the 0.0100 for arm M seed 1, which is 0.0099 (the check of the
  re-run). This version quotes 0.0099.
- **The competing solvers' figures were taken before the piece rule**, and
  the text says so in three places; the run under the rule is owed before the
  registration review, by ruling (section 7.3, the last paragraph).

The repository's own two checkers, run on the whole document as it stands:

```
$ .venv/bin/python scripts/check_citations.py --only docs/successor-experiment-proposal-2026-10-03-v4.md
[CONFIDENT] 0 reference(s) name a file that is not in the repository
  (version 3 had six, all to the label search and its check, which had not merged then; both are on the main line now, and so is the check of the short pre-stated run)
[CONFIDENT] 1 exact figure(s) absent from the one file their sentence cites
  (the count of arm M's entangled gate episodes, in a sentence of section 5.3 carried unchanged from version 3: the file cited holds the share and not the count, which is that share of the gate's episodes)
$ .venv/bin/python scripts/check_single_source.py --only docs/successor-experiment-proposal-2026-10-03-v4.md
[CONFIDENT] Group 1: a dollar figure the ledger does not contain: 0 found
[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source: 2 found
  (both in one sentence of section 12.2, cited to the 2026-09-21 ruling that set the two releases, which is the figures' source; the ledger carries them because the ruling did)
```

That the checkers see so little of this document is a statement about the
checkers, not about the rest being clean.

**5. A command that creates something while documented as creating nothing.
Does not fire on anything this document runs; one gap stated. MEASURED.** The
proposal runs nothing that touches a vendor. The list's own test, run by this
session (the last lines of its output; every line above them is `[ ok ]`):

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
  ...
negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

The gap is the one RT-228 named and section 5 states: the launcher is named
(`launch_a3_fetch_first.sh`, which carries the guard), the registered
`launch_a3.sh` is not used, and the successor's training entry point for arms
T, C and M on the rented machine does not exist yet.

**6. A remote step tested only against stand-ins. The launcher's check passes;
the design has three such steps, each stated. MEASURED.**

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds 8s)

launch_a3_fetch_first.sh
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)

negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang

all checks pass. Nothing was rented and nothing was spent.
```

On the design: the handshake's machine half has been tested only against
stand-ins, and the registration says what is true of it, as ruled (W9,
decision 18); arm M's code has never run on the rented machine (W9, step 4 of
section 11); the tripwire does not exist as code yet (section 12.5). All
three are said in the text, and none is counted as tested. **One step of a
different kind is in the same state and is said too: the code that withholds
a reading when a control that holds fails does not exist yet** (section 6.4,
item 5); on the toy every such control passed, so the withholding has never
been exercised.

**Candidate 7. An outcome line a plan states in advance that the design
cannot produce on the path it expects. Fires on one line, which the text
states; does not fire on the others. MEASURED.** The drafted test: for each
pre-stated line, name the code path that prints each signal it needs, and
show that path can run in the order the line requires. Run on the committed
outputs:

- **Arm M's pass line** ("between 0.3 and 0.7 on every seed, and within 0.10
  of its true-slot reading"): produced, both halves, at the registered site
  sets (failure 2's output above; section 5.3).
- **The separation line** (0.5 on every seed): produced (failure 2's output).
- **The fifth outcome term** ("metric validated, degree not read"): produced.
  It is where the toy lands, by the path the text expects: the anchors
  separate and arm F returns "read failed its floor".
- **Control 4's pass line** (bit-identical outputs at the two action
  positions): produced on all twelve, by code committed before its output,
  and reproduced byte for byte by its check (main line at `53c8100`).
- **Control 2's reported description**: **cannot be produced on the path the
  toy offers, on any model.** The text says so in terms and attaches no line
  to it. This is the one place the candidate fires.
- **The lesion description**: "arm T collapses on two of three seeds", which
  is what the path produced (failure 3's output above).
- **The rider**: can produce a reading on arms C, F and M on 0 of 9 toy pairs
  on the path it expects, and the text says so with the two reasons (section
  7.2, item 7). Accepted as the report.
- **The two-of-three rule for an arm whose seeds disagree** (section 3):
  ruled, and **never produced on the toy**, where every arm's three seeds
  agree. The code that applies it does not exist yet. Stated here so that it
  is not counted as rehearsed.
- **The $10 wager** (section 12.8), and the money lines of section 12, which
  no ruling of 2026-10-03 changed:

```
$ .venv/bin/python -c "
spent=228.15; first=44.0; second_no_rerun=84.06+12+23; note_both=161.90
print('ruled split: first release %.2f + second release without its re-run line %.2f = %.2f'%(first,second_no_rerun,first+second_no_rerun))
for lo,hi,label in ((29.70,41.76,'arm M three runs only, 1.94 in the first release'),(32,44,'arm M as ruled, 32 to 44, 1.94 inside')):
    for m in (lo,hi):
        left=450-spent-(first+second_no_rerun)-m
        print(f'  {label}: arm M {m:.2f}: programme after {spent+first+second_no_rerun+m:.2f}, left {left:.2f}, meets the 10 floor: {left>=10}')
for m in (32,44):
    print(f'note split (161.90 + arm M {m}): programme after {spent+note_both+m:.2f}, left {450-spent-note_both-m:.2f}')
print('first release development line, four arms at 1.943 each: %.2f of the 10 line'%(4*1.943))
"
ruled split: first release 44.00 + second release without its re-run line 119.06 = 163.06
  arm M three runs only, 1.94 in the first release: arm M 29.70: programme after 420.91, left 29.09, meets the 10 floor: True
  arm M three runs only, 1.94 in the first release: arm M 41.76: programme after 432.97, left 17.03, meets the 10 floor: True
  arm M as ruled, 32 to 44, 1.94 inside: arm M 32.00: programme after 423.21, left 26.79, meets the 10 floor: True
  arm M as ruled, 32 to 44, 1.94 inside: arm M 44.00: programme after 435.21, left 14.79, meets the 10 floor: True
note split (161.90 + arm M 32): programme after 422.05, left 27.95
note split (161.90 + arm M 44): programme after 434.05, left 15.95
first release development line, four arms at 1.943 each: 7.77 of the 10 line
```

  The wager meets its floor on every split and at both ends of the range.

Whether the candidate is a new species or an instance of failure 3 is John's
ruling, still open; on this version it catches control 2, which failure 3's
test catches too.

**What this pass leaves open, in one place.** The competing solver's run
under the piece rule; the check of this version and of the late-evening
ruling's record; the code owed before step 4 of section 11 (the training
entry point for arms T, C and M, the tripwire, the withholding of a reading
on a failed control, control 2's twenty random pieces, and the two-of-three
rule); and the reviewer's own pass,
which is still owed, as the protocol says.

---

## 18. The printed site list for the registered model

The site list is registered as the rule that generates it (section 7.2, item
2), and the registration prints the list beside the rule. This is the list,
printed by the rule and not typed by hand. A layer set is written as its
first and last running state: "3-5" is states 3, 4 and 5 together. State 0 is
the running state straight after the input embedding, where the acting
channel is added; states 1 to 12 are the outputs of the twelve blocks. Each
row lists every layer set that begins at that state, and the position sets
each of them is a candidate at. Every site set whose layers include state 0
is a candidate at the action position set only; every other layer set is a
candidate at all four position sets (`action`, the action position alone;
`action+ans`, the action position and the answer-marker token just before it;
`action+3`, the action position and the three positions before it;
`post-identity`, every position from the model's first own turn to the
action). No site set spans every position. The toy's list is printed after
it, for comparison with the 45 the controls re-run's code asserts.

```
$ .venv/bin/python -c "
def contiguous(n): return [(a,b) for a in range(n) for b in range(a,n)]
P4=['action','action+ans','action+3','post-identity']
def name(a,b): return str(a) if a==b else f'{a}-{b}'
for label,n in (('registered model: 13 running states (0 = after the input embedding, 1 to 12 = after each block)',13),('toy model: 5 running states',5)):
    L=contiguous(n); total=0
    print(label)
    for a in range(n):
        sets=[name(x,y) for x,y in L if x==a]
        ps=['action'] if a==0 else P4
        total+=len(sets)*len(ps)
        print(f'  first state {a:>2} | at {", ".join(ps)} | layer sets: {", ".join(sets)} | {len(sets)} x {len(ps)} = {len(sets)*len(ps)} site sets')
    print(f'  total: {total} site sets, {4*total} comparisons at sizes 1, 2, 4 and 8')"
registered model: 13 running states (0 = after the input embedding, 1 to 12 = after each block)
  first state  0 | at action | layer sets: 0, 0-1, 0-2, 0-3, 0-4, 0-5, 0-6, 0-7, 0-8, 0-9, 0-10, 0-11, 0-12 | 13 x 1 = 13 site sets
  first state  1 | at action, action+ans, action+3, post-identity | layer sets: 1, 1-2, 1-3, 1-4, 1-5, 1-6, 1-7, 1-8, 1-9, 1-10, 1-11, 1-12 | 12 x 4 = 48 site sets
  first state  2 | at action, action+ans, action+3, post-identity | layer sets: 2, 2-3, 2-4, 2-5, 2-6, 2-7, 2-8, 2-9, 2-10, 2-11, 2-12 | 11 x 4 = 44 site sets
  first state  3 | at action, action+ans, action+3, post-identity | layer sets: 3, 3-4, 3-5, 3-6, 3-7, 3-8, 3-9, 3-10, 3-11, 3-12 | 10 x 4 = 40 site sets
  first state  4 | at action, action+ans, action+3, post-identity | layer sets: 4, 4-5, 4-6, 4-7, 4-8, 4-9, 4-10, 4-11, 4-12 | 9 x 4 = 36 site sets
  first state  5 | at action, action+ans, action+3, post-identity | layer sets: 5, 5-6, 5-7, 5-8, 5-9, 5-10, 5-11, 5-12 | 8 x 4 = 32 site sets
  first state  6 | at action, action+ans, action+3, post-identity | layer sets: 6, 6-7, 6-8, 6-9, 6-10, 6-11, 6-12 | 7 x 4 = 28 site sets
  first state  7 | at action, action+ans, action+3, post-identity | layer sets: 7, 7-8, 7-9, 7-10, 7-11, 7-12 | 6 x 4 = 24 site sets
  first state  8 | at action, action+ans, action+3, post-identity | layer sets: 8, 8-9, 8-10, 8-11, 8-12 | 5 x 4 = 20 site sets
  first state  9 | at action, action+ans, action+3, post-identity | layer sets: 9, 9-10, 9-11, 9-12 | 4 x 4 = 16 site sets
  first state 10 | at action, action+ans, action+3, post-identity | layer sets: 10, 10-11, 10-12 | 3 x 4 = 12 site sets
  first state 11 | at action, action+ans, action+3, post-identity | layer sets: 11, 11-12 | 2 x 4 = 8 site sets
  first state 12 | at action, action+ans, action+3, post-identity | layer sets: 12 | 1 x 4 = 4 site sets
  total: 325 site sets, 1300 comparisons at sizes 1, 2, 4 and 8
toy model: 5 running states
  first state  0 | at action | layer sets: 0, 0-1, 0-2, 0-3, 0-4 | 5 x 1 = 5 site sets
  first state  1 | at action, action+ans, action+3, post-identity | layer sets: 1, 1-2, 1-3, 1-4 | 4 x 4 = 16 site sets
  first state  2 | at action, action+ans, action+3, post-identity | layer sets: 2, 2-3, 2-4 | 3 x 4 = 12 site sets
  first state  3 | at action, action+ans, action+3, post-identity | layer sets: 3, 3-4 | 2 x 4 = 8 site sets
  first state  4 | at action, action+ans, action+3, post-identity | layer sets: 4 | 1 x 4 = 4 site sets
  total: 45 site sets, 180 comparisons at sizes 1, 2, 4 and 8
```

**The count this implies, frozen with the list:** 325 site sets, each at four
sizes of piece, so 1,300 comparisons in the nomination family for each arm
and seed. Under the stricter variant (the sensitivity row) the first row
drops out: 312 site sets and 1,248 comparisons. Both agree with section 7.2,
item 2, and with the review of version 3, which recomputed them ("What was
checked and held"). The registered measurement code asserts the count before
it runs, as the toy code does.

---

## 19. The seven questions put to John, each now ruled as suggested

Seven places where this session did not think the answer was its to give.
**John ruled on all seven on 2026-10-03, late evening, in the words "Agreed
on all", taking the suggestion in each** (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`).
The questions are left below as they were put, so that a reader can see what
was chosen against what; "written as run" and "this version says" in them
describe the first filing of this version, and the body now carries each
ruling where it bears. None of them changes a toy figure. **Two things to
hold on to.** Question 6 was the one this session said deserved more of
John's attention than the others, and a general agreement settled it; the
record of the ruling says so. And question 7 leaves a run owed before the
registration review.

1. **Does the whole read still have to reach four fifths, now that the piece
   does?** The ruling of 2026-09-26 (RT-212) put the fit floor on the whole
   read, at the worst layer of the nominated site set. The ruling of
   2026-10-03 (page 1) says only sizes whose own accuracy clears may be
   chosen, printed "beside the whole read's", and does not say whether the
   earlier floor remains a second condition. The controls re-run applied the
   floor to the piece only. On the toy both readings give the same twelve
   verdicts, but a piece can score an episode or two above its whole read.
   *Written as run: the floor is on the piece (sections 6.4, item 2, and
   7.2, item 1).* **Suggestion: the piece only, with the whole read's count
   printed.** Confidence moderate. It is the piece that is transplanted, and
   a second floor is a second way to return no verdict on the arm being read,
   for no gain the first does not give. Strongest alternative: require both,
   which costs nothing on the toy and keeps the 2026-09-26 ruling to its
   letter.

2. **The piece rule is applied after the layers are chosen.** So it decides
   which sizes may be chosen and never changes which layers are used. That
   was the re-run method's own reading, marked as John's to overturn; the
   check noted it has not been put to him in terms. *Written as run (section
   7.2, item 3).* **Suggestion: confirm it.** Confidence moderate. The
   alternative, letting the piece's accuracy also decide between layer sets,
   has not been run, and would need the toy re-run again before the
   registration review.

3. **Which device, and which number format, is the registered fit computed
   on?** The ruling (page 3, RT-232) says the registration names them and
   that the figure on the named device is the registered one. It does not
   say which. *This draft writes in the laptop's processor, the model's
   states in 32-bit, the read fitted by scikit-learn in 64-bit, the library
   versions recorded (section 7.2, item 1).* **Suggestion: confirm that.**
   Confidence high on the processor, because every toy figure in this version
   was computed on it and it is the one device every later reader will also
   have; moderate on whether the registration should also pin the library
   versions exactly or only record them. Strongest alternative: the graphics
   chip, which is faster on a 30-million-parameter model and is what the
   earlier committed fits used.

4. **The numbers of episodes at the registered size.** The brief for this
   version asks for every frozen number to be stated. Every bar is stated,
   but each is a share or a rule, and no ruling sets how many development,
   held-out and fresh episodes the registered measurement uses, how many are
   on the relaxed set, how many held-out episodes the gates are scored on, or
   how many shuffles the permutation null uses. *The registration must print
   them; this version lists them as not set (section 9, the last row).*
   **Suggestion: the toy's counts, unchanged: 600 development episodes with
   the last 180 held out, 800 fresh matched pairs, 800 on the relaxed set,
   3,000 for the gates, 200 shuffles.** Confidence moderate. They are the
   only counts the procedure has been rehearsed at, the floor is then 144 of
   180 as on the toy, and section 11 already argues the registered model's
   states fit on the laptop at that scale. Strongest alternative: more
   held-out episodes, so that the floor is not decided by a handful: at 180,
   one episode is 0.0056, and the toy has already shown fits moving by one
   episode between devices.

5. **Control 2's comparison: one random piece or twenty?** The ruling keeps
   control 2 as a description: how often the own-directed action moves under
   the named agent's piece, beside how often it moves under "a random piece".
   The code draws one, with its own seed; control 3 draws twenty. *Written
   as the code runs, one draw (section 7.3, item 2).* **Suggestion: twenty,
   reported as control 3 reports them.** Confidence moderate. With no pass
   line a single draw is a weak thing to print beside a figure. It is a small
   code change, and it would mean the code path that ran once on 2026-10-03
   is not quite the one registered. Strongest alternative: leave it at one,
   since the control is expected to return no verdict anyway.

6. **What is an arm's outcome when its seeds disagree?** The floors and the
   controls that hold apply per arm and seed, so an arm can read on two seeds
   and return no verdict on the third. The ruling on what a no verdict maps
   to (page 11) speaks of "no verdict on arm C", "on arm M" and "on arm F"
   and does not say how many seeds make that so. The separation bar is
   written "per seed" in the same way, without saying what follows if it is
   cleared on two seeds of three. On the toy every arm behaves alike on all
   three seeds, so this has never bitten. *Not written into the body beyond
   section 3 saying the case is open.* **Suggestion: the rule the design
   already uses for its gates, at least two seeds of three, with the third
   reported.** Confidence low to moderate; this is a new pre-stated rule and
   deserves his attention more than the others. Strongest alternative: all
   three seeds, which is stricter and makes the fifth outcome and the
   two-arm fallback more likely.

7. **The ordinary competing solver under the piece rule.** The protocol's
   rehearsal asks that a system with none of the structure the measure
   claims to detect be put through the same measurement. The ownership-blind
   solver and the name-only solver were scored on both conditions before the
   piece rule existed, and the controls re-run did not load them. *This
   version says so in three places and quotes no figure for them as if it
   were under the new rule (sections 7.3, 8.1 and 10).* **Suggestion: run
   the ownership-blind solver's three committed toy models through the
   nomination and reading as now registered, on the laptop at $0, method
   committed before output, before the registration review opens.**
   Confidence moderate to high. The expected result is a no verdict (a
   solver with no acting channel should have no read of its own marker that
   reaches four fifths), it is an afternoon, and without it the registration
   review's first question on "satisfied by the wrong thing" has an argument
   behind it and not a number. Strongest alternative: state in the
   registration that it was not measured under the rule, and let the
   reviewer decide whether that is a finding.

**Two things that are not questions, said so they are not found later.**
John's ruling on decision 23 (which read is the registered one) still has no
ruling file of its own; it is carried from his revision instruction for
version 3. And the three rulings of 2026-10-03 were each given as agreement
to a packet or a suggestion, with the wording the recording session's; the
records say so themselves, and this version quotes the records.

---

## 20. Change log from version 3, keyed to the ruling or finding behind each change

"The morning rulings" are
`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` (main line at
`56a5a86`). "The re-run rulings" are
`docs/rulings/2026-10-03-controls-rerun-rulings.md` (`fe5df65`). "The evening
ruling" is `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`
(`f32ba0c`). "The review" is the first independent review of version 3,
findings RT-230 to RT-236 (`4cb7f8e`). "The check of the re-run" is at
`e184a6e`, and "the check of the packets" at `f32ba0c`.

- **RT-230 (serious: the floor certified the read, not the piece
  transplanted). The morning rulings, page 1.** The fit floor moved to the
  piece: only sizes whose own held-out accuracy reaches four fifths may be
  chosen, the piece's count printed beside the whole read's (sections 1, 6.4
  item 2, 7.2 items 1, 3 and 5, 7.4, 7.5, 9). Sections 3 and 5.2 reworded to
  what was measured: the read holds the label, the largest piece transplanted
  holds it, no size moves the action. Version 3's sentence that arm C's
  transplanted subspace "holds the label and clears the fit floor on every
  seed" struck. **Arm C's toy readings changed from 1.0051, 1.0025 and
  1.0000 to 1.0051, 0.9926 and 0.9974, with the sites and sizes the re-run
  chose** (sections 3, 5.2, 9, 10). The forecast on page 1 of the ruling
  packet (8, 8 and 4 directions; 0.9975 on seed 1) is not used: the re-run
  showed it wrong on seed 1, and the check of the packets says to quote the
  re-run (its section 7, row 6).
- **RT-233 (serious: four controls had no figure under the registered
  rules). The morning rulings, page 2.** The controls re-run is done and
  checked. Every figure for controls 1, 3, 4, 6 and 7, the true-slot
  reference, the rider and the stricter row is quoted from it (sections 5,
  7.2, 7.3, 10, W11). Version 3's sentences saying those figures were owed
  are gone.
- **RT-231 (minor: arm M's true-slot check, run by the review).** Arm M's
  blind reading is within 0.0049, 0.0099 and 0.0529 of its true-slot reading
  at the registered site sets (sections 5.3, 9, 10 R-3). **0.0099, not the
  0.0100 the re-run's prose printed** (the check of the re-run, section 7,
  item 3).
- **RT-232 (minor: fits move by one episode between devices). The morning
  rulings, page 3.** Fits stated as counts of held-out episodes; the
  registration names the device and number format, and the figure on that
  device is the registered one (sections 1, 5.4, 7.2 item 1, 7.5, 9). Taken
  from the review's own wording, which also names the number format, and not
  from the packet's shortening (the check of the packets, section 7, row 9).
  The device, the laptop's processor, was ruled late that evening.
- **RT-234 (minor: the whole-state floor is applied twice). Page 3.** Said in
  sections 6.4 item 1, 7.4, 7.5 and 9: on development episodes at nomination,
  again on fresh episodes at the reading, and a site set that clears the
  first and misses the second returns no verdict.
- **RT-235 (minor: the stop reads its fit at a layer the noise may pick).
  Page 3.** The report for the first full-size free-model run prints the
  read's count at every layer, the chosen piece's count and the candidates
  (sections 7.5 and 11, step 5a). Section 7.2, item 5, and section 5.2 now
  say that on an arm where nothing moves the action the choice is made among
  sampling noise.
- **RT-236 (minor: depths, and two citations by branch). Page 3.** Four
  blocks and five running states against twelve and thirteen, stated the
  same way (section 7.2, item 1). The label search and its check cited by
  their main-line commits, `a97c12b` and `ecd2b6c`, throughout.
- **Decisions 2, 3, 4, 8, 9, 10, 13, 17, 18 and 19. The morning rulings,
  pages 4 to 10, 14, 15 and 16.** Each marked ruled in section 15 and where
  it bears: sections 4.2, 5, 5.1, 5.2, 7.2 item 2, 8.2, 9, 10 R-11, 11 step
  5a, 12.2, 12.4, W8, W9. The handshake is described as ruled, option (b),
  with the caution carried (W9). **Not carried: the packet's sentence about a
  $97.04 loss, on its page for decision 13.** Version 3 left that sentence
  out on purpose, and the check of the packets found it is not what the
  ledger shows (its section 7, row 3).
- **Decision 14, what a no verdict maps to. The morning rulings, page 11; the
  evening ruling, ruling 1.** The fifth registered term, "metric validated,
  degree not read", added to the outcome table as satisfactory and stated as
  weaker than R1; the mapping for arms C and M written in; the paragraph on
  the open reporting gap replaced; the toy outcome restated as the fifth term
  (sections 1, 3, 7.4, 9, 11 steps 7 and 8, 15).
- **Decision 15, control 2's tolerance. Agreed in the morning rulings (page
  12); withdrawn by the re-run rulings, ruling 1.** Control 2 is a reported
  description with no pass line; the registration says in terms that it
  never ran at toy scale, why, and that a no verdict is expected; its one
  end-to-end run is quoted labelled NOT A RESULT (sections 7.3 item 2, 7.4,
  7.5, 9, 10, 11 S8, W7, W14).
- **Decision 16, control 4's standing. Agreed in the morning rulings (page
  13); reversed by the re-run rulings, ruling 2.** Control 4 redefined on the
  positions before both twins' first own turns, and made a control that
  holds, with the pass line that the outputs are bit-identical. Described as
  a known-answer test of the pairing and the code, which cannot fail on a
  correctly built model and whose pass says nothing about any model (the
  check of the re-run, section 5). The sentence that arms C and F "receive
  the ownership signal by other routes" withdrawn (sections 1, 6.4 item 5,
  7.3 item 4, 7.4, 7.5, 9, 10, W14). **Not carried: the re-run's sentence
  tying the six models with a large excess to their sites' position set as a
  cause**; the control uses only the site's layers (the check of the re-run,
  section 7, item 3).
- **The re-run rulings, ruling 3, and the evening ruling, ruling 2: the
  piece's accuracy at the other positions.** A reported figure, printed both
  ways, with how each is computed, and the toy's figures (sections 3, 5.2,
  5.3, 7.2 item 3, 7.4, 7.5, 9). The plain statement that the piece's four
  fifths is established at the action position only, with the figures for
  arms C and M, and a new weakness W13.
- **From the check of the re-run, section 7 (not a ruling).** The null
  transplant counted as tested at fifteen different places (sections 7.3
  item 7, 10 R-8). Two requirements on the registered code written in: the
  controls that hold withhold the reading in code (sections 6.4 item 5, 7.3,
  7.4); and the ordinary competing solver is said, in three places, not to
  have been measured under the piece rule (sections 7.3, 8.1, 10 R-5), with
  its run now owed by ruling.
- **The short pre-stated run.** Quoted for control 4 as redefined, for the
  new column, and for the one run of the part of control 2's code after the
  floor, labelled NOT A RESULT.
- **From the check of the short pre-stated run (main line at `53c8100`, pull
  request 82), section 10 (not a ruling).** Filed while this version was
  being written; the first commit of this version had marked the short run's
  figures as unchecked. All four of its notes are followed: control 4 is
  said to compare the outputs at the two action positions (section 7.3, item
  4); the new column's computation is set out in full, the figure on the
  average is said to be good to an episode or two on the toy, and the
  registered code averages in 64-bit (section 7.2, item 3); what the short
  run added for control 2 is said to be the part of its code after the floor
  (section 7.3, item 2; section 10); and the piece's four fifths is said to
  be established at the action position only (sections 3, 5.2, 5.3, W13).
  Also carried from it: the test is not empty (noise changes the outputs),
  the ten named positions are about a quarter of a span, the limit on what
  "pre-stated" can be shown to mean, and John's confirmation that section 4
  of the short run's method is what "print both figures" means.
- **John's late-evening ruling on this version's seven questions
  (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, filed with
  this version).** Each written in where it bears: the floor on the piece
  only (sections 6.4 item 2, 7.2 item 1, 9); the piece rule applied after
  the layers are chosen (section 7.2, item 3); the registered fit on the
  laptop's processor, library versions recorded (and, by the reconciliation
  ruling of the same night, pinned) (sections 7.2
  item 1, 7.4, 9); the toy's episode counts at the full size (sections 7.4,
  8.1, 9); twenty random pieces for control 2, with the code change that
  implies (sections 7.3 item 2, 7.4, 7.5, 9); two seeds of three when an
  arm's seeds disagree (sections 3, 7.4, 9); and the competing solver's run
  under the piece rule owed before the registration review (sections 7.3,
  8.1, 10, 11). Section 19 keeps the questions as put and says they are
  ruled.
- **The header, the source table, section 16 and section 17.** Rewritten for
  this version: sources by main-line commit, the eight new ones first; the
  author's failure-mode pass run again with this session's commands on the
  controls re-run's outputs. Section 18, the printed site list, is new.
  Section 19, the questions for John, is new. Version 3's change log from
  version 2 is not repeated; it is section 18 of version 3.
- **Left alone.** Sections 2, 4.1, 4.3, 4.4, 5.5, 6.1, 6.2, 7.1, 8.2 (but for
  one clause), 12.3, 12.5 to 12.8 and 14 carry version 3's text. Sections
  4.2, 6.3, 8.1, 12.1, 12.2 and 12.4 change by a sentence or a citation each.
  Wherever version 3's text says "this version" of a change it made from
  version 2, that change is carried here unchanged.

---

## What this version does not do

It edits nothing: not version 3, not any ruling, registered text or protocol
text, and not the findings of any run. It issues no go, releases no money,
launches nothing, trains nothing and rents nothing. It does not open the
registration review, and it is not ready for it: the competing solver's run
under the piece rule is owed, and this version and the record of the
late-evening ruling are owed a check under the pairing rule of
`docs/outside-review-protocol.md`. The seven questions of section 19 were
John's, and he ruled them; this version resolved none of them itself.
===== END OF RECORD 4 =====

===== RECORD 5 of 25 - the inside reviewer's findings on version 4 (Gate A, tier 1) - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md` (complete file, 80,950 characters) =====
# Gate A tier 1 review of the successor experiment's registration text (proposal version 4 and the changes ruled into it) — RT-237 to RT-246

*Written 2026-10-04 (Pacific) by a Claude Code session on branch
`gate-a-tier1-successor-v4`, cut from the main line at `d19f914` (the merge of
pull request 91, John's ruling on the competing-solver run and the
twenty-piece control). Filed under this experiment's reviews directory because
the successor experiment has no directory of its own yet, and this is the
experiment its text most affects (`docs/outside-review-protocol.md`, "The
pairing rule", the filing fallback).*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (a command was run, and the command and its output are below or
in the scripts folder beside this file) or **ARGUED** (reasoning a reader can
dispute), and carries a severity: **fatal**, **serious** or **worth-noting**.
Findings continue the red-team ledger's numbering. The last number used
anywhere in the repository at `d19f914` is RT-236 (the review of version 3);
`git grep -nE "RT-2(3[7-9]|[4-9][0-9])" d19f914` returns nothing. No ledger row
is written here: rows are written when John rules.*

**Nothing was rented, created or spent: $0.** Laptop only, on its processor.
No registered text, ruling file, protocol text, known-failure list, ledger,
earlier review or proposal text was edited. The scripts beside this file read
committed output files, load committed toy models, fit small straight-line
reads and time forward passes; they train no model. One of them ran the
controls re-run's committed code again, from a copy whose output folder points
into this session's scratch space, so nothing committed was overwritten.

**How isolated this session was, said plainly.** It is a fresh session in its
own git worktree. It has no chat history: it has not seen the chat of any
session that wrote version 4, the rulings, the runs or their checks, and it
worked only from committed files. It wrote none of what it reviews.

---

## Verdict in one paragraph

**One fatal finding, four serious, five worth-noting.** The fatal one is small
to fix and large if left: the gate that decides whether the freely trained
model may be read at all includes the clause "the ownership-free state and
syntax batteries must hold" (version 4, line 2223, frozen by line 2064 and the
section 9 row at line 2270). The successor's task has no such batteries, the
clause names no line for "hold", and no rehearsal record ever exercised it; the
design's own stop condition S8 (lines 2599 to 2602) says a gate that cannot be
evaluated counts as failed and its consequence fires. Registered as written,
the freely trained model could never be read, so the first outcome, "metric
validated, degree read", could never be reached (RT-237). The serious ones: the
whole-state floor as printed admits a zero or negative divisor for a model at
chance, which only an unwritten clause in the code prevents (RT-238); the task
grammar is described as an extension of the closed design's grammar, which
puts the model's own name in front of it at the moment it acts, and the two
deliberate departures that remove that cue are written nowhere in the
registration text (RT-239); the ruled episode counts were rehearsed only at the
toy's width, and a stand-in at the registered width drops the entangled
model's read below the four-fifths floor on two of three seeds (RT-240); and
the outcome map has holes, with no registered term for a no verdict on the
separable model or for the two-model fallback (RT-241). **What held, and it is
the most important thing this review measured:** the nomination rule written
from version 4's text alone, by code that imports none of the checked code,
picks exactly the site set, size and verdict the committed code picked on all
twenty-four toy rows (twelve primary, twelve stricter), reproduces every toy
reading, and lands the toy on the fifth outcome term with a separation of
0.9926; and the committed code, run again from clean on this laptop today,
reproduces its committed outputs value for value (26,722 values in 25 files,
none different; the table identical). The registration text
describes the instrument that ran. It is not ready to register until RT-237 is
closed and the serious findings are closed or carried as named open items with
John's reasons.

---

## What this review opened, and what it did not

**Opened and read in full, in this order.** `CLAUDE.md` at the repository root;
the workspace plain-language rule in `~/Code/CLAUDE.md` (as loaded into this
session); `docs/outside-review-protocol.md`; the measurement rehearsal record
`docs/2026-09-21-successor-measure-rehearsal.md` (the first thing read after
the protocol, as the protocol requires); the target,
`docs/successor-experiment-proposal-2026-10-03-v4.md` at `d19f914`, all 4,219
lines; the rulings `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`
(record A of the seven-question ruling), `docs/rulings/2026-10-03-version-4-questions-rulings.md`
(record B), `docs/rulings/2026-10-03-seven-questions-reconciliation.md`,
`docs/rulings/2026-10-03-version-4-check-questions-rulings.md` and
`docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`; the check
of version 4, `reviews/2026-10-03-proposal-v4-check-claude-code.md`; the check
of the competing-solver run and the twenty-piece control,
`reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md`; the
findings of those two runs, `docs/2026-10-03-competing-solver-run.md` and
`docs/2026-10-03-control-2-twenty-draws.md`; `docs/known-failure-modes.md`.

**Opened in part, to look up a sentence, a figure or a function.** The morning
rulings of 2026-10-03 (page 11, what a no verdict maps to); the Weekend 1 queue
ruling (page 1h, the channel-removal check) and its packet (the 1h page); the
December-result roadmap's outcome table; `docs/2026-09-26-free-arm-label-search.md`
(its verdicts table); the label-search output folder; version 1 of the proposal
(one line, where the batteries clause first appears); versions 2 and 3 (by
search, for that clause and for the label-search sentence); Amendment A3
(`amendment-a3.md`, by search for its batteries); the closed design's grammar
`experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py` (its
header); the rehearsal grammar `experiments/rehearsal-successor-measure/src/grammar.py`
(its header and constants); the toy code the runs use (`rerun_controls.py` in
full; in `repairs.py` the floor, the reading and the masks; in `rerun_v3.py`
the paths and the model loader; `rehearse.basis_for`; `transplant.py`'s
signatures; `arms.Config`; `bench_arms.py`'s header); the two launcher checks
and the launcher's dry-run path (read before running, to be sure they create
nothing); the grammar attempt's check (one line); every committed output file
the scripts below name; the reviews directory's file list and the red-team
ledger's last lines (for numbering).

**Not opened.** `STATUS.md`, `data/project.toml`, the `site/` directory, any
pull request description, TimeAssembler, any chat or transcript, any
uncommitted file of another checkout, anything outside this repository except
`~/Code/CLAUDE.md`. The project's Python interpreter lives in the main
checkout's `.venv` and was run by its full path; no file there was opened. The
earlier Gate C reviews of versions 1 and 2, the ruling packets other than the
1h page, the controls re-run's and short run's findings and checks as
documents (their output files were read directly), and the compute ledger were
not opened: the check of version 4 had already compared every dollar figure
and the 2026-10-03 toy figures against them, and this review spent its time on
what that check says it did not do.

---

## Findings at a glance

| Number | Severity | Label | Brief part | Version 4 lines | The finding in one line |
|---|---|---|---|---|---|
| RT-237 | **fatal** | MEASURED | 1, 3 | 2223, 2270, 2064; S8 at 2599 to 2609 | The free model's gate requires "the ownership-free state and syntax batteries" to hold. The successor's task has no such batteries, the clause sets no line, and nothing rehearsed it; by the design's own stop condition S8 an unevaluable gate fails, so the free model could never be read |
| RT-238 | **serious** | MEASURED | 1, 3 | 1113 to 1132; 2261 | The whole-state floor as printed admits every site set, with a divisor of exactly zero or below, when a model's own-directed accuracy is at or under its no-transplant rate. The code refuses those cases by a clause the text does not carry. On the competing solver the printed rule admits 45 of 45 site sets on four runs of six; the code admits none |
| RT-239 | **serious** | MEASURED (the texts), ARGUED (the consequence) | 2, 1 | 496 to 525; 1890 to 1896; 133 to 141 | The grammar is registered as an extension of the closed design's grammar, which has twelve turns (not the ten stated) and shows the model its own name three tokens before it acts. The two deliberate departures that remove that cue and make the twins the same text are written nowhere in version 4 |
| RT-240 | **serious** | MEASURED (a stand-in, NOT A RESULT) | 1, 3 | 2067 to 2071; 2276; 1320 to 1355 | The ruled counts (a read fitted on 420 episodes) were rehearsed only at the toy's width of 160. At the registered width of 448 there are more coordinates than fitting episodes. Padding the committed toy states to 448 with noise drops the entangled model's read from 177 to about 90 and from 176 to about 130 of 180, below the floor of 144 |
| RT-241 | **serious** | ARGUED | 3 | 295 to 313; 456 to 467; 2061 to 2062; 2188 to 2189; 820 to 827 | The outcome map has holes: a no verdict on the separable model maps to nothing; the two-model fallback has no registered outcome term; "R3 for that arm" against R3 as the whole experiment's outcome; a failed channel-removal check on the free model; and whether a built model that fails its gate after the first release gets the one permitted re-run |
| RT-242 | worth-noting | MEASURED | 4 | 1384 to 1389 | "Anchored at the action position the three candidates reach 0.733, 0.383 and 0.478": those are one candidate's three seeds. The three candidates' best on the free model over those site sets are 0.733, 0.417 and 0.633. Carried from version 3 |
| RT-243 | worth-noting | MEASURED | 4 | 1118 to 1125 | "On the toy they never did [disagree]": true of the twelve own-directed nomination grids, not of the toy. The two forms of the floor disagree on 576 rows of the repairs run's other-agent grids, 892 of the grammar attempt's and 1,080 of 1,080 of the competing solver's, each time with the plain form passing a model near chance |
| RT-244 | worth-noting | MEASURED | 4 | (the ruled sentence of 2026-10-04, ruling 2; v4 1996 to 2017) | The ruled sentence about the competing solver says its untouched rate "missed the no-transplant rule by 0.11 or more". It missed the formula by 0.109 to 0.139 and the rule's allowance by 0.091 to 0.121; "0.11 or more" holds on neither reading. Its first clause holds only under the code's floor (RT-238) |
| RT-245 | worth-noting | MEASURED | 1 | 2520 to 2524; 1332 to 1355 | The registered nomination on the laptop's processor is argued, not measured, to be practical. Timed here at the registered shape: one transplant pass over the 600 development pairs takes 4.6 seconds, so one model's nomination takes about two hours and the twelve registered models about 25 hours, which holds the argument up. The device ruling names the device for the read's fit; it does not name one for the transplant passes that choose the site set, which on the entangled model was decided by one episode in 600 |
| RT-246 | worth-noting | ARGUED | 2 | (the weakness ruled 2026-10-04, ruling 7) | The ruled new weakness says the toy has no model that does the task by another route. It has one: the free model itself solves the own-directed condition without carrying its marker word (version 4, section 5.4), and the measure returns no verdict on it. The weakness can be stated more exactly, and the other-route case that would read is the name-cue route of RT-239 |

---

## The registration text as reviewed

The registration text is version 4 plus changes that have been ruled and not
yet written in. This review collected those changes from the committed record,
read version 4 against each, and asked whether each can be written in as
described.

| Ruled change, and where it is ruled | Version 4 now | Can it be written in as described? |
|---|---|---|
| The thirty wording fixes of the check of version 4 (its section 4), ruled into the text by `docs/rulings/2026-10-03-version-4-check-questions-rulings.md` ("What this changes") | Not yet written: the stale per-seed separation sentences (lines 412 to 414, 2256, 2418 to 2420, 3814), the stale citations to record A, the processor clause at lines 2520 to 2524, and the rest | **Yes**, all thirty. This review confirmed the ones it could check by a command: the stale separation sentences are at lines 413, 2419 and 3814; the processor clause is at lines 2520 to 2524; section 17's sweeps now return 761 and 235, not 759 and 233; and the lock file given as the model for pinning is not committed (`git check-ignore` names `.gitignore` line 35) |
| The other-agent control's code changed to twenty random pieces and its code test run again before the registration review (the check-questions ruling, ruling 1; record B, ruling 5) | Lines 1831 to 1837 still say "owed with the registered measurement" | **Yes**; done in `src/control2_twenty_draws.py`, run as a test of the code (`out-control-2-twenty-draws/`, NOT A RESULT), and checked |
| The separation rule stays as ruled, said in one sentence (the check-questions ruling, ruling 2) | Not yet written | **Yes** |
| The solver's main reading has the acting channel removed; the other reading stated beside it; the main reading's no verdict comes from the pairing (2026-10-04, ruling 1) | Lines 1996 to 2017 still say the run is owed | **Yes** |
| The sentence on what stopped the solver, in the check's words (2026-10-04, ruling 2) | Not yet written | **Not as worded.** Its first clause, "no site set cleared the floor at nomination", is true only under a clause of the code the text does not carry (RT-238), and "0.11 or more" is true on no reading of the figures (RT-244) |
| The no-transplant formula reported, not described as true of every model (2026-10-04, ruling 3) | Lines 1178 to 1183 give the formula's reason as if general | **Yes** |
| The registered control 2 is `control2_twenty_draws.control2`; `rerun_controls.control2` named as the earlier version (2026-10-04, ruling 4) | Not yet written | **Yes**; the new function's early exits are copied from the old one and its random pieces are control 3's twenty (the check of pull requests 88 and 89, section 5.1) |
| Ninety-fifth percentile of twenty as the summary, all twenty printed (2026-10-04, ruling 5) | Not yet written | **Yes** |
| "Would fail the gate if it were gated as the free model is", not "the gate stopped it" (2026-10-04, ruling 6) | Not quoted in version 4 yet | **Yes** |
| A new two-sentence weakness: the toy's competing solver fails the task (2026-10-04, ruling 7) | Not yet written | **Yes**, and it can be stated more exactly (RT-246) |
| The changes in section 7 of the check of pull requests 88 and 89, including the sampling band named as a 95 percent Wilson interval (2026-10-04, "What this changes") | Lines 2105 to 2108, 2072 to 2076 and 2276 name a band and no method | **Yes**; the competing-solver run computed it that way (`nominate_blind_*.json`, `best_piece_sampling_band`) |
| Record B's fuller points: the processor proving impractical is a fresh question for John, not a switch; the method states what "the model's own turn" means for a solver with no channel; a miss at the first full-size run goes to John with the band (record B rulings 3, 4 and 7; the check-questions ruling, "For John to know") | Lines 2520 to 2524 say the opposite of the first; S4a at lines 2578 to 2583 omits the band | **Yes** |

**Where version 4 as it stands conflicts with a ruling in a way the ruled
changes above do not already fix:** nowhere this review found, beyond the
places the two checks already list. The findings below are about the text that
results once all of the above is written in.

---

## 1. Feasibility

| Pre-stated quantity or rule | Can it be measured with the stated instrument, and can the comparison reach its line? | Record | Holds? |
|---|---|---|---|
| The nomination rule (sections 6.4 item 1, 7.2 items 2 to 5) | Yes: the rule written from the text alone reproduces the committed code's choice on 24 of 24 toy rows | this review, `rule_from_text.out.txt` | **holds** |
| The reading (section 6.3) and its top of scale | Yes; top of scale 1.0000 on every arm and seed; smallest divisor among the models that read 0.4863 | `failure_mode_pass.out.txt`, failure 1 | **holds** |
| The whole-state floor (section 6.4 item 1) | On a model that has learned the task, yes. On a model at chance, the printed formula is met by any site set, with a divisor of zero or below | `rule_from_text.out.txt` section 4; `failure_mode_pass.out.txt` | **RT-238** |
| The fit floor, 144 of 180, on the piece (sections 6.4 item 2, 7.2 item 3) | Rehearsed at width 160 only. At width 448 the same counts give more coordinates than fitting episodes; a stand-in drops the entangled model below the floor | `width_vs_count.out.txt` | **RT-240** |
| The sampling band at the floor | Computable; ruled as a 95 percent Wilson interval by adoption of the check's section 7 | `out-competing-solver-run/nominate_blind_*.json` | holds once written in |
| The no-transplant rule, 0.018 room | Exercised at both ends (`failure_mode_pass.out.txt`, failure 3 part three); its largest measured miss 0.017536 recomputes | `older_figures.out.txt` | **holds** |
| The gate on learning, 790 of 3,000 | Exercised; recomputes | the check of version 4; `failure_mode_pass.out.txt` | **holds** |
| The channel-removal collapse line (section 8.2) | Exercised on all twelve toy models | `out-repairs/gate_base.json` | **holds** |
| **"The ownership-free state and syntax batteries must hold"** (section 8.2) | **Cannot be measured: no such battery exists in the successor's task, no line is set, no rehearsal record exists** | `failure_mode_pass.out.txt`, failure 3 part one | **RT-237, fatal** |
| Separation 0.5, lowest of arm C minus highest of arm T | Exercised: 0.9926 | `rule_from_text.out.txt` section 3 | **holds** |
| Arm M: 0.3 to 0.7 and within 0.10 of its true-slot reading | Exercised; recomputes (the check of version 4) | | **holds** |
| The controls that hold (7, 1 on arm T, 4 as redefined) | Exercised on all twelve | `rule_from_text.out.txt` section 2 | **holds** |
| Control 2, twenty random pieces | No figure possible at toy scale; carries no line, by ruling | | as ruled |
| The two-of-three rule for seeds that disagree | Never produced on the toy (no arm's seeds disagree); the code does not exist | `failure_mode_pass.out.txt`, failure 3 part one | stated in the text; open |
| The registered nomination on the laptop's processor | Argued in the text; timed here | `registered_shape_timing.out.txt` | **RT-245** |

### RT-237 (fatal, MEASURED). The free model's gate names batteries the successor's task does not have

**What version 4 says.** Section 8.2, the channel-removal check that gates
whether the free model is read (lines 2201 to 2223), ends: "the ownership-free
state and syntax batteries **must hold**." The section 9 row (line 2270)
carries the same words, and section 7.4 freezes "the ownership-lesion rule"
among the gates (lines 2063 to 2065). Section 5.4 (lines 957 to 959) says the
free model "is read only after it passes the learn-both gate, the
ownership-lesion check in section 8, and the fit floor". Stop condition S8
(lines 2599 to 2602): "A rehearsal item, a gate or a stop condition **cannot
be evaluated**: missing data, code that will not run on the artifact, a
measurement never taken. It counts as failed and its consequence fires; it is
never recorded as not applicable and stepped over."

**What was measured.**

```
$ grep -rlE '\bT_(state|syntax)\b|([Ss]tate|[Ss]yntax) batter' experiments/rehearsal-successor-measure/src || true
(no file)
$ grep -rlE '\bT_(state|syntax)\b|([Ss]tate|[Ss]yntax) batter' experiments/06-mvm-0a-constructed-self-index/src/
experiments/06-mvm-0a-constructed-self-index/src/summarize_null.py
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py
experiments/06-mvm-0a-constructed-self-index/src/lock_guard.py
experiments/06-mvm-0a-constructed-self-index/src/ctl_split_check.py
experiments/06-mvm-0a-constructed-self-index/src/null_calibration_a3.py
experiments/06-mvm-0a-constructed-self-index/src/run_post_pilot.sh
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py
```

and, from `failure_mode_pass.py` (output in `failure_mode_pass.out.txt`):

```
  the lesion clause 'the ownership-free state and syntax batteries must hold': fields the gate file records: ['lesion_collapses_own', 'lesioned_other', 'lesioned_own', 'n', 'other', 'other_clears', 'other_correct', 'own', 'own_by_route', 'own_clears', 'own_correct']
  grep of the rehearsal code for a state or syntax battery: (no file)
```

The batteries are the closed design's end-of-episode question sets (`T_state`
and `T_syntax` in `curriculum_a3.py`, line 163: `BATTERIES = ("T_act",
"T_other", "T_state", "T_syntax")`). The successor's task, as the rehearsal
built it (`grammar.py`), has eight assignment turns and two action turns and
no end-of-episode questions at all. The gate file every toy channel-removal
figure comes from records no battery field. By search, the clause entered at
version 1 (`docs/successor-experiment-proposal-2026-09-21.md`, line 568: "the
ownership-free state and syntax batteries hold"), was ruled into the queue
ruling's page 1h with the rest of option (i), and has been carried word for
word through versions 2, 3 and 4. No review of versions 1 to 3 and neither
check of version 4 mentions it (`grep -n -i batter` over those files returns
nothing on this clause).

**Why it is fatal.** Two rules the design itself carries make it so. Item 5 of
the 2026-09-21 ruling, which version 4 quotes at line 2352: "A pre-stated
quantity the rehearsal never exercised is a fatal finding on its own." And S8:
at the registered run the clause cannot be evaluated (there is no battery, no
data, no line), so the channel-removal gate counts as failed for the free
model, and the free model is not read. Then the first registered outcome,
"metric validated, degree read", cannot be reached by any result whatever.
That is the shape of the closed design's unsatisfiable clause: a registered
sentence nobody can satisfy, carried in plain sight.

**One honest doubt, stated.** Version 4's grammar section says the successor
grammar "extends" the closed design's grammar (line 498), which does have
these batteries. If the registered generator kept them, the clause could be
evaluated. But nothing in version 4 says the batteries are kept, the rehearsal
grammar dropped them, the clause still sets no line for "hold", and no record
exercised it on any model of this design, so the finding stands either way
(and RT-239 is about the same unstated grammar).

**What would fix it (a suggestion).** Either John rules the clause out, with
its reason on the record (it was written for a grammar this design no longer
uses), or the registration defines the batteries in the successor's grammar,
sets the line for "hold", and a rehearsal run on the committed toy models
exercises it. The closure check is then a search showing the clause gone, or
the rehearsal record with the figure.

**On the known-failure list.** This is a pre-stated gate the design cannot
evaluate on the path it expects. It is closest to the drafted seventh entry,
"an outcome line a plan states in advance that the design cannot produce on
the path it expects" (version 4, section 17), which John has not yet ruled
onto the list, and to failure 3, part three. The protocol asks the pass that
finds a fatal finding of a new kind to add it to the list; this session was
told not to edit the list, so the test is written here for whoever does:
*for every clause of every gate, name the field of a committed rehearsal
output file that evaluates it, and print that field; a clause with no field
is the finding.*

### RT-238 (serious, MEASURED). The whole-state floor as printed admits a zero or negative divisor

**What version 4 says.** Section 6.4, item 1 (lines 1113 to 1132): "A site set
is usable only if the whole-state transplant clears four fifths of the arm's
own own-directed accuracy ... written on the chance-corrected scale:
`accuracy_whole − accuracy_untouched ≥ 0.8 × (own_directed_accuracy −
accuracy_untouched)` ... The floor keeps the denominator away from zero by
construction: on an arm that has learned the task, `own_directed_accuracy −
accuracy_untouched` is large, and the denominator is at least four fifths of
it." The section 9 row (line 2261) states the floor the same way.

**What the code does.** `experiments/rehearsal-successor-measure/src/repairs.py`,
`floor_check` (line 276): `clears=bool(whole - untouched >= need and need >
0)`. The second clause, that the requirement itself is above zero, is in no
sentence of version 4.

**What was measured.** `rule_from_text.py`, section 4, applies the floor as
printed and the floor as coded to the committed development grids of the
ordinary competing solver (the ownership-blind model, which version 4 now puts
through the measure):

```
seed 0, channel_removed: own-directed 0.2333, untouched 0.2400, floor asks for -0.0053; whole - untouched over the family: +0.0000 to +0.0000
    text's floor: 45 of 45 site sets clear -> read failed its floor: no size's piece reaches four fifths
    code's floor: 0 of 45 site sets clear -> no site set clears the whole-state floor   (committed: no site set clears the whole-state floor)
seed 0, channel_left_on: own-directed 0.2383, untouched 0.2417, floor asks for -0.0027; whole - untouched over the family: -0.0017 to +0.0017
    text's floor: 45 of 45 site sets clear -> read failed its floor: no size's piece reaches four fifths
    code's floor: 0 of 45 site sets clear -> no site set clears the whole-state floor   (committed: no site set clears the whole-state floor)
seed 1, channel_removed: ... floor asks for -0.0160; whole - untouched over the family: +0.0000 to +0.0000
    text's floor: 45 of 45 site sets clear -> read failed its floor ...
seed 1, channel_left_on: ... floor asks for -0.0160; whole - untouched over the family: +0.0000 to +0.0033
    text's floor: 45 of 45 site sets clear -> read failed its floor ...
seed 2, both readings: floor asks for +0.0027 and +0.0053 -> text and code agree: 0 of 45
```

(full output in `rule_from_text.out.txt`). On four of the six runs the printed
rule admits every site set with a divisor of exactly zero, or as low as
−0.0017. What then refuses the solver is the piece rule (best piece 20 to 25
of 180). Had a model at chance held a readable label, the printed rule would
have gone on to divide by zero.

**Does it change any toy verdict?** No: the solver's verdict is no verdict
under both, and on all twelve arm models the requirement is well above zero.
It changes the stated reason, and with it the sentence John ruled into the
text on 2026-10-04 ("no site set cleared the floor at nomination"), which is
true under the code and false under the text.

**Why serious and not worth-noting.** The registered code is still to be
written (section 11, step 3), and it is written from the registration text.
The text's floor is the place the design says keeps the divisor off zero
"by construction", which is the claim failure 1 of the known-failure list
exists to test; it holds only on models that have learned the task, and the
competing solver, which the rehearsal requires the measure to face, has not.
The check of pull requests 88 and 89 (its section 5.4) found the same
dependence from the other side: on a real arm the divisor is kept large by
the floor *together with* the gate and the no-transplant rule.

**What would fix it.** Write the code's clause into section 6.4, item 1, and
the section 9 row: a site set is usable only if the requirement is above
zero (equivalently, the model's own-directed accuracy is above its
no-transplant rate on those episodes), and say that otherwise the arm
returns "no verdict: floor not defined". Then the ruled sentence about the
solver is true as written.

### RT-240 (serious, MEASURED on a stand-in; NOT A RESULT). The ruled episode counts were rehearsed only at the toy's width

**What version 4 says.** Ruled 2026-10-03, late evening (record A ruling 4,
record B ruling 4): the registered measurement uses the toy's counts, 600
development episodes with the last 180 held out, so every read is fitted on
420 (lines 2067 to 2071; section 9, line 2276). The read is scikit-learn's
logistic regression on the running state (line 1335). The caution carried with
the ruling is about sampling at 180 held-out episodes. Nothing is said about
width.

**Why width matters (ARGUED).** The toy's running state is 160 wide
(`arms.Config`, `d_model: int = 160`); the registered model's is 448
(`bench_arms.py`, `REGISTERED_SHAPE`). The read has twelve answers. At 160
there are fewer coordinates than the 420 fitting episodes; at 448 there are
more, and a twelve-way read on 448 coordinates from 420 episodes is in the
regime where a straight-line read can fit its training episodes by chance and
generalise worse. The floor is a hard line on the held-out count.

**What was measured, on a stand-in.** `width_vs_count.py` loads committed toy
models, takes the state at the chosen layer at the action position on the 600
development episodes, and appends 288 coordinates of independent noise (scaled
to the state's own median coordinate spread) to make it 448 wide, then fits the
registered read the registered way. Five noise draws per model:

```
arm/seed layer | width 160: whole read, piece of 8 | width 448 (288 noise coords), five noise draws: whole read; piece of 8
C/0 layer 2 | 180, 180 | [147, 156, 159, 156, 162]; [163, 157, 166, 157, 158]  (noise scale 7.941)
C/1 layer 1 | 177, 172 | [91, 94, 89, 90, 92]; [80, 88, 79, 76, 85]  (noise scale 2.250)
C/2 layer 1 | 176, 178 | [123, 134, 132, 126, 130]; [128, 132, 134, 126, 138]  (noise scale 2.929)
M/0 layer 1 | 180, 180 | [180, 180, 180, 179, 180]; [180, 180, 180, 180, 180]  (noise scale 2.048)
T/0 layer 1 | 180, 180 | [180, 180, 180, 180, 180]; [180, 180, 180, 180, 180]  (noise scale 0.648)
floor: 144 of 180. NOT A RESULT: a stand-in for width, with independent noise in place of a wider model's own coordinates.
```

**What it shows, and what it does not.** On the two built models whose label
sits in a clean slot (T and M), width costs nothing. On the entangled model,
whose label is spread through the state, two seeds of three fall well under
144 and the third keeps a margin of 3 to 18 episodes. A wider model's extra
coordinates are not independent noise; they carry structured content, which
could hurt more or less than this. So this is not a forecast. It is a measured
reason to think the ruled counts, which were chosen because they are "the only
counts the procedure has been rehearsed at", have not been rehearsed at the
size where they will be used, and that the arm most at risk is the high anchor
(and, behind it, the free model the floor exists for).

**The consequence (ARGUED).** An entangled model whose read misses the floor
returns "no verdict, read failed its floor", which fires the two-model
fallback, which has no registered outcome term (RT-241), and which is first
seen after both releases of money are drawn (section 11, step 5b).

**What would fix it.** Any one of: (a) the alternative John was offered and did
not take, more development episodes, sized against the registered width (for
instance several times 448 fitting episodes); (b) the read's regularisation
fixed in advance for the registered width, with the toy re-fitted under it;
(c) a rehearsal of the read at width 448, on a stand-in model trained at the
registered shape on the laptop or on the development runs of step 4, before
registration. At the least, a weakness in section 13 saying the counts were
rehearsed at width 160 only.

### RT-245 (worth-noting, MEASURED). The registered nomination on the laptop's processor is argued, not timed; the device ruling covers the fit, not the choice

**What version 4 says.** Section 11, step 5a (lines 2520 to 2524): "The fit is
computed on the laptop from the fetched checkpoint ... (ARGUED: a
30-million-parameter model's activations on development episodes fit on the
laptop ...)". Section 7.2, item 1 (lines 1332 to 1355): the registered fit is
computed on the processor.

**What was measured.** `registered_shape_timing.py` times, on this laptop's
processor (Apple M4), the forward passes the rule makes over the 600
development pairs, at the toy shape and at the registered shape:

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-scripts/registered_shape_timing.py
torch 2.12.1, threads 4, sequence 56, pairs 600
toy shape (160 wide, 4 blocks): 1,265,191 parameters; capture 0.52 s; one transplant pass over 600 pairs 0.506 s (median of 6); one read fit 0.02 s
   nomination grid: 45 site sets -> 227 passes, 25 fits -> about 1.9 minutes per model and seed (control 2's own grid, where it runs, about doubles it)
registered shape (448 wide, 12 blocks): 29,049,735 parameters; capture 6.55 s; one transplant pass over 600 pairs 4.590 s (median of 6); one read fit 0.09 s
   nomination grid: 325 site sets -> 1627 passes, 65 fits -> about 124.6 minutes per model and seed (control 2's own grid, where it runs, about doubles it)
registered against toy, per model and seed: 65 times
twelve registered models, nomination grids only: about 24.9 hours on this processor
```

**What it shows.** The arithmetic is honest at the toy end: it predicts
about 1.9 minutes per toy model, and the controls re-run this session ran took
1,485 seconds for twelve models with every control, about 2 minutes each. At
the registered shape one model's nomination is about two hours on this
processor; the twelve registered models about a day, more where control 2 runs
its own grid, and more again if the registered episodes are longer than the
toy's 56 tokens (no text fixes that length). So the text's argument holds:
the work fits on the laptop, at a day or two of processor time and $0, and
step 5a's single free-model run is about two hours. It is now a measurement
rather than an argument. One limit: the read was timed on random labels and
may take longer on real ones; it is a small share of the total either way.

**The second half (ARGUED).** Ruling 3 of record B names the device for "the
registered accuracy", the fit. The nomination also chooses among candidate
site sets by their development ownership-only shares, and on the entangled
model seed 1 that choice was decided by one episode in 600 (version 4, lines
776 to 782). A transplant pass on a different device or number format can move
a share by an episode just as a fit can (RT-232 was exactly that for fits). If
the registration names the device for the fit and not for the transplant
passes, the stop at step 5a and every nomination can turn on an unregistered
choice. *Suggestion:* name the device and number format for the whole
nomination and reading, not only for the fit, and carry the timing above (or
the step-4 development runs' own timing) as the measurement behind "it fits on
the laptop".

---

## 2. Satisfied by the wrong thing

| Way the text could be satisfied by a model with none of the structure it claims to detect | Severity | Finding |
|---|---|---|
| A free model reads its own name off the text near the action, if the registered grammar keeps the closed design's rendering, and clears the fit floor through a name cue rather than a carried answer | serious | RT-239 |
| The high anchor reads near 1 through any piece that holds the label and does nothing, which is what "entangled" means operationally; the reading cannot tell entangled from "the answer lives where the read did not look" | (stated by version 4 as weakness W12; not re-filed) | — |
| The whole-state transplant on the entangled and mixed models moves the action even when the donor's identity dictates the same value (control 6), so it carries more than identity | (stated as W11; not re-filed) | — |
| A model at chance passes the printed whole-state floor at every site set | serious | RT-238 |
| The competing-solver test covers a model that fails the task; the toy's free model is a model that does the task by another route, and the weakness ruled on 2026-10-04 does not say so | worth-noting | RT-246 |

### RT-239 (serious; MEASURED that the texts say what is quoted, ARGUED for the consequence). The registration does not state the grammar that removes the model's own name from the act

**What version 4 says.** Section 4.1 (lines 498 to 504): "The grammar extends
the registered Amendment A3 grammar (`curriculum_a3.py`, the episode generator
committed 2026-09-15), which already has the pieces: four agents, a closed
vocabulary, ten turns, eight value slots, every revised item assigned by all
four agents before anyone revises it ... The rehearsal's shrunken version of
it is `experiments/rehearsal-successor-measure/src/grammar.py`." Line 522:
"The grammar is as version 2 had it." Section 1 (lines 133 to 141): the acting
channel "is the only honest source of ownership in this design, because ...
nothing in the text itself can carry it". Section 7.3, item 4 (lines 1890 to
1896): "The twins are the same text. They differ only in which turns carry the
acting channel."

**What the two grammars say about themselves.** The closed design's grammar,
`experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py`, header:
"Twelve turns, four agents, two *contested* items: ... Eight assignment turns
... Four revision turns"; and, under "An honest limit on the design's central
claim": "The revision turn renders as "<marker> assign <item> to <value>", so
at the moment the model acts, its own marker is in the context three tokens
back. A model could learn "the marker at a position where I am acting is
mine" ... reading a name badge at act time rather than carrying a binding."
The rehearsal grammar, `grammar.py`, header, "Two departures from the
registered A3 grammar, both deliberate": "1. **The action turn carries no
marker word.** ... Here the only route to the ownership answer is the acting
channel. 2. **The answer token is never shown.** ... Together these make a
matched pair of episodes ... come out **token-for-token identical**, differing
only in which positions the acting channel fires on."

```
$ grep -n -i "mask\b\|<mask>\|name badge\|no marker word\|carries no marker\|departure\|token-for-token\|answer token\|same text" docs/successor-experiment-proposal-2026-10-03-v4.md
1534:   the running state at the mask token of the own-directed action (the
3271:    at the mask token, scored on held-out development episodes; the label
```

So: version 4 says the closed design's grammar has ten turns; it has twelve.
And the two departures that make the act free of the model's own name, and
make the twins the same text, appear in version 4 only as two passing
mentions of "the mask token".

**Why this matters (ARGUED).** The registered generator is still to be written
(section 11, step 3, "the built generator"), and it is written from the
registration text. Read as written, the text points at the closed design's
generator as the base and at the rehearsal's as its shrunken copy, and only
the shrunken copy says the departures exist. A generator built by extending
`curriculum_a3.py` as the text says would show the model its own marker word
three tokens before it acts. Then: the registered read's label, "which marker
word is the model's own", is in the text near the action, so a free model can
clear the fit floor by copying a name rather than by carrying an answer; the
twins are no longer the same text, so the known-answer reasoning of control 4
and of section 6.1 no longer holds as stated; and the ownership signal the
whole design is built to isolate (ledger item RT-17, the finding that any
learnable ownership cue in the tokens is a fingerprint) is back. That is a
reading satisfied by the wrong thing, on the one model the experiment exists
to read.

**What would fix it.** Register the episode format itself, as the rehearsal
grammar's header gives it: the turns and their order, the action-turn
rendering with no marker word, the masked answer, and the property that twins
are token-for-token identical, with the self-test that asserts it named as
part of the registered generator's tests. Correct "ten turns" as a statement
about the closed design's grammar. Say whether the closed design's
end-of-episode question sets are carried (this decides RT-237's doubt).

### RT-246 (worth-noting, ARGUED). The ruled weakness about the competing solver can be stated more exactly

John ruled (2026-10-04, ruling 7) that section 13 gains: "the toy's ordinary
competing solver fails the task, so its 'no verdict' shows only that the
measure returns nothing on a model that has not learned the task. It does not
show what the measure does on a model that does the task by another route."

The toy has such a model: the free model. Version 4, section 5.4 (lines 986 to
999): it scores 0.5513 to 0.5597 on the own-directed condition against 0.2340
to 0.2383 for the ownership-blind solver, and solves it "by attending to the
value tokens on the turns the acting channel marked, with no need to know
which marker word those turns carry", and "the free toy model does not carry
the marker word forward to where it acts". The measure returns no verdict on
it ("read failed its floor"). So the toy does show what the measure does on
one model that does the task by a route other than carrying the registered
label: it returns nothing, and says why. What the toy does not show is a model
that does the task by a route that *also* leaves the label readable where the
model acts, and the obvious such route is the name cue of RT-239. *Suggestion:*
write the weakness with both halves, so a reader learns which "other route"
has been seen and which has not.

---

## 3. No verdict

| Way the registration text could fail to return a verdict on the runs it is written for | Severity | Finding |
|---|---|---|
| The free model's gate cannot be evaluated, so it fails by S8 and the free model is never read | fatal | RT-237 |
| A no verdict on the separable model, or the two-model fallback, has no registered outcome term | serious | RT-241 |
| The entangled model's read misses the floor at the registered width | serious | RT-240 |
| A model at chance reaches the arithmetic with a divisor of zero under the printed floor | serious | RT-238 |
| The processor proves impractical at full size (record B: a fresh question for John) | worth-noting | RT-245 |

### RT-241 (serious, ARGUED). The outcome map has holes

**What version 4 says.** The outcome table (lines 307 to 313); "What a no
verdict maps to" (lines 456 to 467): arm C fires the two-model fallback, arm M
is dropped, arm F after T and C separate is the fifth term; section 7.4 freezes
"the five registered outcome terms of section 3, and what a no verdict on each
arm maps to" (lines 2061 to 2062). Section 8.1 (lines 2188 to 2189): "An arm
that fails, after the one permitted re-run, gives outcome R3 for that arm".
Line 305: "nothing in this document may report an outcome in other words."

**The holes, each a state the registered runs can reach.**

1. **No verdict on arm T, the separable model.** Not in the list of three.
   It can happen: arm T's reading is withheld if control 1 fails on it (a
   control that holds on arm T only), if its no-transplant rate misses, or if
   its floor is missed on fresh episodes. With arm T reading on fewer than two
   seeds, "metric validated" cannot be met (lines 481 to 483), R2 is not met (the
   measure did not fail to separate; it was not computed), R3 is not met (no
   gate failed), and no other term applies. Section 7.4 says the frozen list
   covers "each arm"; it covers three.
2. **The two-model fallback has no term.** A no verdict on arm C "fires the
   two-arm fallback" (line 462). Then R1 and R2 both require separating arms
   T and C, which cannot be done. Lines 820 to 827 say "the R1 sentence is
   correspondingly weaker" and that the registration "says that in those
   words", but no words are registered, and line 305 forbids reporting in
   other words.
3. **"R3 for that arm" against R3 as the experiment's outcome.** R3 in the
   table is the whole experiment's outcome ("this recipe and this size are not
   yet a place to study mechanism"). Line 2188 makes a gate failure "R3 for
   that arm". A gate failure on arm M, a model whose no verdict merely drops
   it, would then be read either as the whole experiment's R3 or as an
   arm-level R3 that the table does not define.
4. **The free model fails its channel-removal check** (fewer than two seeds
   collapse; or RT-237's clause). Section 5.4 says it is then not read. Which
   term follows is not said: R3 if this check is a "gate" (section 8 calls it
   one), the fifth term if it counts as a no verdict.
5. **A built model that fails its gate in step 5b.** R3 is "after the one
   permitted re-run". On the ruled split the re-run is funded only in the first
   release (section 12.3; section 12.4 removes it from the second), and step
   5a's text gives it to the free model. Whether a separable, entangled or
   mixed model that fails at step 5b gets a re-run before R3 is declared, and
   from what money, is not stated.

**What would fix it.** One table in section 3, frozen in section 7.4, with a
row for every arm-level state (reads; no verdict; fails its gate after a
re-run; fails the channel-removal check, for arm F) and the registered term
each combination gives, including the fallback's own term. The ruling that
created the fifth term (2026-10-03, page 11) is the precedent: it closed the
same kind of hole (RT-182, the no-verdict finding on version 1) for three arms
and not the fourth.

---

## 4. Over-reading

| What a result could be read as claiming beyond what it measures | Severity | Finding |
|---|---|---|
| "The label search's three candidates reach 0.733, 0.383 and 0.478" read as three candidates' figures | worth-noting | RT-242 |
| "The two forms of the floor never disagree on the toy" read as a property of the toy, when it holds only where the models have learned the task | worth-noting | RT-243 |
| The ruled sentence about the competing solver's misses | worth-noting | RT-244 |
| "Metric validated" read as validation of a measure of degree in general; it is validation at the sites the procedure nominates, on built models that differ in more than degree, with a middle anchor that is a mixture by item | (stated by version 4 as W1, W2, W10; ARGUED here that the outcome term's own words invite the reading, and the registered report should carry W1's hedge in the same sentence as the term) | — |

### RT-242 (worth-noting, MEASURED). The label-search sentence quotes one candidate's three seeds as three candidates

Version 4, lines 1384 to 1389: "The best is 0.789, from candidate 1 ... and
that from position spans that start at one of the model's own turns ...;
anchored at the action position the three candidates reach 0.733, 0.383 and
0.478." The findings table it cites (`docs/2026-09-26-free-arm-label-search.md`,
section 4) has, for candidate 1 on the free model, "0.733 / 0.483 / 0.789 |
0.733 / 0.383 / 0.478", where the two cells are the best over all 60 site sets
and over the 45 fixed-extent ones, each given as seeds 0 / 1 / 2. From the
committed verdict files (`older_figures.py`):

```
  own-turn-pair    best over all 60 site sets 0.789; best over the fixed-extent 45 0.733; per seed [0.733, 0.483, 0.789]; clears: False
  own-source-turn  best over all 60 site sets 0.456; best over the fixed-extent 45 0.417; per seed [0.45, 0.45, 0.456]; clears: False
  own-value        best over all 60 site sets 0.633; best over the fixed-extent 45 0.633; per seed [0.611, 0.611, 0.633]; clears: False
```

So 0.733, 0.383 and 0.478 are candidate 1 on seeds 0, 1 and 2; the three
candidates' best over those site sets are 0.733, 0.417 and 0.633. The sentence
was carried from version 3 (line 1105). Nothing ruled rests on it and every
figure stays under 0.80. *Fix:* "anchored at the action position, candidate 1
reaches 0.733, 0.383 and 0.478 on seeds 0, 1 and 2, and candidates 2 and 3 at
most 0.417 and 0.633."

### RT-243 (worth-noting, MEASURED). The two forms of the whole-state floor do disagree on the toy, on models near chance

Version 4, lines 1118 to 1125: the plain form "is printed beside it everywhere,
so a reader can see whether the two readings of the ruled sentence ever
disagree; on the toy they never did (MEASURED: 0 disagreements across all site
sets, arms and seeds, the repairs findings at `882f252`, section 3 ...)".
`floor_forms.py` counts every committed floor record that carries both forms:

```
out-repairs/nominate_base_*.json              floor records   4254; the two forms disagree on 576
out-v3-rules/nominate_*.json                  floor records   3672; the two forms disagree on 0
out-controls-rerun/nominate_*.json            floor records   2160; the two forms disagree on 0
out-grammar-c/nominate_base_F_T_C.json        floor records   3188; the two forms disagree on 892
out-competing-solver-run/nominate_*.json      floor records   1080; the two forms disagree on 1080
```

(and 0 in every measurement file). All 576 of the repairs run's disagreements
are in the other-agent control's grids on arms C and F (the named-other
condition, near chance on those models); none is in the own-directed grids
the repairs findings counted. On the competing solver the plain form passes
every row and the registered form none. Each disagreement is the plain form
passing a model near chance. So the sentence is right about the own-directed
grids of the twelve base models, wrong about "the toy", and the record it
misses is the best evidence for the choice the design made: the plain form
would let a model at chance through. *Fix:* narrow the sentence and cite the
disagreements as the reason the corrected form is registered.

### RT-244 (worth-noting, MEASURED). The ruled sentence about the competing solver gets one of its own figures wrong

The sentence ruled into the registration text on 2026-10-04 (ruling 2):
"... its best piece missed the piece rule by 119 or more of 180 and its
untouched rate missed the no-transplant rule by 0.11 or more ...".
`solver_sentence.py` against the committed outputs:

```
piece rule missed by: 119 to 124 of 180  -> '119 or more': True
untouched rate against the formula: 0.1091 to 0.1393  -> '0.11 or more': False
untouched rate beyond the rule's room: 0.0911 to 0.1213  -> '0.11 or more': False
```

The run's own findings had already corrected the same slip in one place
(commit `3d55865`, which the check of pull requests 88 and 89 confirms: "outside
the allowance it is 0.09 to 0.12"); the check's suggested sentence, which John
adopted, reintroduced it. And its first clause, "no site set cleared the floor
at nomination", is true under the code's floor and false under the floor as
version 4 prints it (RT-238). *Fix:* "its untouched rate was 0.109 or more
above the formula, and 0.09 or more outside the rule's allowance", and close
RT-238 so the first clause is true of the text.

---

## The failure-mode pass

One section per entry of `docs/known-failure-modes.md`, in order. Each shows
the command run by this session and what it returned. The author's own pass
(version 4, section 17) was read after this pass was run; nothing below is
copied from it.

### Failure 1. A comparison whose denominator was zero — **fires on the printed floor for a model at chance (RT-238); does not fire on any model that learned the task**

*Part one, where every no-transplant rate comes from.* `failure_mode_pass.py`
prints each of the twelve, with the file and field it was read from
(`out-controls-rerun/measure_{arm}_seed{seed}.json`, `primary.reading`): T 0.0000
on every seed; C 0.0512, 0.0488, 0.0600; F 0.0587, 0.0563, 0.0688; M 0.0125,
0.0175, 0.0138. None is typed in; each is measured.

*Part two, the divisor and the top of the scale at the chosen site set:*

```
  T/0: denominator 1.0000; top of scale 1.0000; reads        (and T/1, T/2 the same)
  C/0: denominator 0.4888; top of scale 1.0000; reads
  C/1: denominator 0.5063; top of scale 1.0000; reads
  C/2: denominator 0.4863; top of scale 1.0000; reads
  F/0: denominator 0.4263; top of scale 1.0000; described only
  F/1: denominator 0.5112; top of scale 1.0000; described only
  F/2: denominator 0.4613; top of scale 1.0000; described only
  M/0: denominator 0.7675; top of scale 1.0000; reads
  M/1: denominator 0.7563; top of scale 1.0000; reads
  M/2: denominator 0.7800; top of scale 1.0000; reads
  smallest denominator among those that read: (0.48625, 'C/2')
```

*The case the printed floor admits:*

```
  solver seed 0 channel_removed : floor asks -0.0053; rows the printed formula admits 180 of 180; denominators among them +0.0000 to +0.0000
  solver seed 0 channel_left_on : floor asks -0.0027; rows the printed formula admits 180 of 180; denominators among them -0.0017 to +0.0017
  solver seed 1 channel_removed : floor asks -0.0160; rows the printed formula admits 180 of 180; denominators among them +0.0000 to +0.0000
  solver seed 1 channel_left_on : floor asks -0.0160; rows the printed formula admits 180 of 180; denominators among them +0.0000 to +0.0033
  solver seed 2 channel_removed : floor asks +0.0027; rows the printed formula admits 0 of 180
  solver seed 2 channel_left_on : floor asks +0.0053; rows the printed formula admits 0 of 180
```

**Disposition.** The top of the scale is the same, 1, on every arm, and the
smallest divisor among the models that read is 0.4863: the per-arm-ceiling
repair (ledger item RT-172) holds. The entry fires on the floor's printed
formula, which admits a divisor of zero or below on a model whose own-directed
accuracy is at or under its no-transplant rate: RT-238.

### Failure 2. A probe target that cannot be recovered in principle — **fires on the free model, and a registered rule catches it**

*Part one, a route sentence, in this design's own words, sections 0 to 16:*

```
  1277: own**. *The route by which that quantity reaches the model's states, in one
  1278: sentence:* the marker word is the input token at every turn the model's own
  1279: assignments are spoken on, so it is carried by the token into the running
  1283: claim, that which marker word is the model's own is forced by the loss at
```

(Line numbers are those of `git show d19f914:...`, which counts from the same
file; the fourth match is the sentence striking version 2's loss claim, not a
route.) A route sentence exists, and it names the token. It names a route to
the state at the model's own assignment turns; it does not name one to the
action position, where the registered read is fitted.

*Part two, the same read and the same bar at the position where the marker
word is the input token, and at the registered action position* (from the
short pre-stated run's committed `part_b.json`; the toy has no separate run of
the first kind, so this is the nearest committed pair of runs):

```
  C/2: whole state at the marker's own token 180; whole read at the action position 176 -> both clear
  F/0: whole state at the marker's own token 180; whole read at the action position 32 -> second clears, first does not
  F/2: whole state at the marker's own token 180; whole read at the action position 18 -> second clears, first does not
  M/0: whole state at the marker's own token 180; whole read at the action position 180 -> both clear
  (T, C/0, C/1 and F/1 have a single-position site and the first own turn is not reported for them;
   their action-position counts are 180, 180, 177 and 12)
  the named agent's read (control 2) on arm F seed 0, per running state (whole, best piece):
    {'0': (16, 20), '1': (95, 92), '2': (137, 139), '3': (127, 115), '4': (102, 102)} -> best 139 of 144 needed
```

**Disposition.** The middle limb, "the second run clears the bar and the first
does not", is the free model's state: the label is fully in the state where it
is spoken and absent where the model acts. This is the fatal finding of the
review of version 2 (RT-212, the empty read on the free model), still firing.
The design catches it, not repairs it: the fit floor on the piece turns it
into a registered "no verdict, read failed its floor", the number the
arithmetic would have returned is withdrawn, and the route (b) search found no
other label at the floor. The same limb fires on control 2's named-agent read
(139 against 144), which carries no line by ruling. Nothing new fires here;
what is new is that the route sentence would change if RT-239 were left open
(the marker word could then also be "the input token" three tokens before the
action).

### Failure 3. A cell that is empty by construction — **fires on one gate clause (RT-237); not on any reported cell**

*Part one, every pre-stated cell, counted:*

```
  control 6, T/0: same-value 81, different-value 719        (C/0, F/0, M/0 the same; every seed the same, per section 17's own block)
  control 4 as redefined, positions per pair: {'max': 21, 'mean': 5.212500095367432, 'min': 1}
  control 2: toy models on which it returned a figure: 0 of 12
  the two-of-three rule: arms whose three seeds disagree on the toy: 0 of 4
  the lesion clause 'the ownership-free state and syntax batteries must hold': fields the gate file records: ['lesion_collapses_own', 'lesioned_other', 'lesioned_own', 'n', 'other', 'other_clears', 'other_correct', 'own', 'own_by_route', 'own_clears', 'own_correct']
  grep of the rehearsal code for a state or syntax battery: (no file)
```

*Part two, the generator property that empties a cell.* Distinct values per
item, drawn without replacement (`grammar.py`, `_content`, `replace=False`),
which is why control 6 runs on the separately generated relaxed set; its 0 of
4,000 on the distinct grammar recomputes from `out/denominator_control6.json`
(`older_figures.out.txt`).

*Part three, every threshold at both ends:*

```
  gate bar 790 of 3,000; a model at one in four clears it with probability 0.0485
  no-transplant rule at own-directed 1.0: formula 0.0000; a broken pairing (0.125) flagged: True
  no-transplant rule at own-directed 0.8712: formula 0.0184; a broken pairing (0.125) flagged: True
  no-transplant rule at own-directed 0.56: formula 0.0629; a broken pairing (0.125) flagged: True
  no-transplant rule at own-directed 0.2633: formula 0.1052; a broken pairing (0.125) flagged: True
  piece floor at 144 of 180: the competing solver's best piece 20 to 25, arm F's 34, the built arms' chosen pieces 150 to 180
  whole-state floor, printed formula, at the broken end (solver seeds 0 and 1): admits every site set (above)
```

**Disposition.** Control 6's two cells have trials on every arm and seed (the
empty-cell repair, ledger item RT-173, holds). Control 4 transplants at one
position or more in every pair. Control 2's cell is empty on the toy and the
text says so; it carries no line, by ruling. The two-of-three rule has never
been exercised and the text says so. **The channel-removal gate's battery
clause has no cell at all, in any record: RT-237.** At both ends: the gate,
the no-transplant rule and the piece floor pass the working end and refuse
the broken end; **the whole-state floor as printed passes the broken end
(RT-238).** Control 4's pass line has no working end to test, which version 4
already says.

### Failure 4. A claim of measurement with no record, or a record that does not reproduce — **fires twice, on two worth-noting sentences (RT-242, RT-243)**

*Part one, the two sweeps* (on sections 0 to 16 at `d19f914`, cut at
section 17's heading):

```
$ git show d19f914:docs/successor-experiment-proposal-2026-10-03-v4.md | awk '/^## 17\. /{exit} {print}' > v4-through16.md
$ grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' v4-through16.md
761
$ grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' v4-through16.md
235
$ wc -l < v4-through16.md
3449
```

(Section 17 prints 759, 233 and 3,406, from before the late-evening rulings
were written in; the check of version 4 found the same 761 and 235. The
hits were read through the closure rule's own narrower question, next.)

and the closure rule's own check, every paragraph using verified, measured,
calibrated or attacked, and whether it names a record (`closure_sentences.py`):

```
paragraphs in sections 0 to 16: 274; using one of the four words: 99; of those, naming no file, commit, ledger item, section, page, ruling or item: 13
```

The thirteen were read one by one (`closure_sentences.out.txt` prints them in
full). Four are headings. Five use "measure" as the name of the instrument, or
sit in the opening summary, the quoted question or a sentence about what a
check is for, and claim nothing the body does not cite. Two are tables whose
source is named in the sentence above them (section 12.4). One is the
statement that the tripwire's ratios are measured against the posted rate,
which is a rule, not a claim. One says the transplanting code "proves the
restriction as a tensor identity in its self-test (rehearsal item R-8)", which
names the rehearsal record's item; that record (section 2a, R-8) says "The
restriction property is proved as a tensor identity at full rank". **No claim
of measurement lacks a record.**

*Part two, the records hold what the sentences say.* The check of version 4
compared 89 figures of 2026-10-03 against their files and did not re-derive
the older ones (its section 5). This review did the older ones
(`older_figures.py`, full output in `older_figures.out.txt`):

```
strong transplant, version 1 form / chance-corrected form      v4: 0.4323 / 0.5018     file: 0.4323 / 0.5018
weak transplant, version 1 form / chance-corrected form        v4: 0.3222 / 0.5013     file: 0.3222 / 0.5013
largest |measured - formula|, and where                        v4: 0.017536, free arm  file: 0.017536 at F/2
same-value trials, distinct grammar                            v4: 0 of 4,000          file: 0 of 4000
blind solver, strict set to relaxed set                        v4: 0.2467 to 0.3095    file: 0.24675 to 0.3095
arm T own-directed on unseen marker words, seeds 0/1/2         v4: 0.7612, 0.6512, 0.6512   file: 0.76125, 0.65125, 0.65125
negative readings on that pool (rehearsal R-4)                 v4: -0.1706 and -0.2755 file: -0.1706 and -0.2755 (version 1 form)
arm T seed 0 on the grammar attempt's unseen pool              v4: -0.1870             file: -0.1870
curriculum: named-other seeds clearing, counts                 v4: 0 of 3              file: 0 of 3, [232, 580, 429]
reweight: named-other seeds clearing, counts                   v4: 0 of 3              file: 0 of 3, [695, 619, 713]
grammar attempt: named-other counts; own-directed mean; level  v4: 774, 730, 759; 0.5654; 0.5513   file: [774, 730, 759]; 0.5654; 0.5513
the grammar check's own re-run                                 v4: 750, 809, 739       file: 750, 809 and 739 found
fourth_arm.entangled_share, seeds 0/1/2                        v4: 0.60375 (483 of 800) file: 0.60375, 0.60375, 0.60375
ms per step T / C / F                                          v4: 13.08 / 13.52 / 12.53   file: 13.08 / 13.52 / 12.53
arm C slowest step over its median                             v4: 2.9%                file: 2.8%
out-v3-rules/models_sha256_check.json all_agree                v4: true                file: True
```

Every figure matches its file. Two small notes: the negative readings
−0.1706 and −0.2755 are in the version 1 form of the reading (the
chance-corrected form gives −0.1917 and −0.3303 on the same rows), which
version 4 quotes only as "negative" except in this one place (line 2387 quotes
−0.1870, which is the chance-corrected form, from a different run); and arm
C's slowest step is 2.85 percent over its median from the unrounded fields
(2.9 from the rounded milliseconds), inside the "within 3%" the text claims.
Neither is a finding. **Where the entry fires:** the label-search sentence,
whose record says something else (RT-242), and the floor-forms sentence,
whose cited record is right and whose "on the toy" is wider than any record
(RT-243).

The repository's two checkers were not run again here: the check of version 4
ran both on this same file (its section 2.5) and this review changed nothing
they look at.

### Failure 5. A command that creates something while documented as creating nothing — **does not fire**

Version 4 runs nothing against a vendor. The list's own test, run by this
session after reading the launchers' dry-run paths (each stops before its first
vendor command):

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
...
negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

(exit status 0; full output in `failure5_launcher_guard.out.txt`, every line
`[ ok ]`, with the standing prohibition on the registered launcher printed as
expected). The launcher version 4 names (`launch_a3_fetch_first.sh`) carries
the guard. The gap version 4 itself states stays open: the training entry
point for the built models on the rented machine does not exist.

### Failure 6. A remote step tested only against stand-ins — **does not fire on the launcher; four steps of the design are untested at the far end, and the text says so for each**

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
launch_a3_fetch_first.sh
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)
negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.0s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang
all checks pass. Nothing was rented and nothing was spent.
```

**What stood in for the far end, step by step.** The shutdown handshake's
machine half: local stand-ins only (stated, weakness W9). The mixed model's
code on the rented machine: never run (W9; step 4 is the first time). The
tripwire: no code (section 12.5). The registered measurement code itself, run
on a full-size model on the laptop's processor: never run; the toy code at
the toy shape stood in for it, and this review's timing is the first
measurement at the registered shape (RT-245). Each is said in the text; none
is counted as tested.

### The drafted seventh entry (not yet on the list)

Version 4 ran it; this review notes only where it fires on the text that
results once the ruled changes are written in: on the battery clause (RT-237:
a gate line the design cannot produce on any path) and on the fallback's
outcome (RT-241: an outcome the design can reach and cannot name).

---

## The decisive measured checks

The protocol asks for at least one check on the text being registered that
would come out wrong if the text were wrong. Two were run.

### Check 1. The rule as the text states it, run on the committed development grids

`rule_from_text.py` implements, from version 4's sentences alone and without
importing any of the checked code, the site-set family and its two exclusions
(section 7.2, item 2), the whole-state floor as printed (section 6.4, item 1),
the smallest clearing layer set per position set with ties to the earliest
(item 4), the piece rule at 144 of 180 applied after the layers (item 3), and
the choice by the highest development ownership-only share with ties to the
smaller size and then the earlier position set (item 5). It runs that rule on
the committed development grids of the twelve toy models and compares its
choice with the committed code's, for the primary and the stricter row; then
computes the reading, the no-transplant rule, the three controls that hold,
the two-of-three rule, the separation and the outcome term, all as the text
states them.

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-scripts/rule_from_text.py
=== 1. Nomination: the text's rule against the committed code's choice, twelve toy models
primary  T/0: text -> nominated, ((0,), 'action', 8); code -> nominated, ((0,), 'action', 8); same: True
...
primary  C/1: text -> nominated, ((1,), 'action+3', 8); code -> nominated, ((1,), 'action+3', 8); same: True
primary  C/2: text -> nominated, ((1,), 'post-identity', 4); code -> nominated, ((1,), 'post-identity', 4); same: True
primary  F/0: text -> read failed its floor: no size's piece reaches four fifths, None; code -> read failed its floor: ...; same: True
...
stricter T/0: text -> nominated, ((1,), 'action', 8); code -> nominated, ((1,), 'action', 8); same: True
...
agree on 24 of 24 (twelve primary, twelve stricter)

=== 2. The reading on fresh episodes, from the text, against the committed degree
T/0: text degree 0.0000; committed 0.0000; no-transplant miss +0.0000; controls 7/1/4 True/True/True; gate True -> reads
C/0: text degree 1.0051; committed 1.0051; no-transplant miss -0.0132; controls 7/1/4 True/True/True; gate True -> reads
C/1: text degree 0.9926; committed 0.9926; no-transplant miss -0.0111; controls 7/1/4 True/True/True; gate True -> reads
C/2: text degree 0.9974; committed 0.9974; no-transplant miss -0.0039; controls 7/1/4 True/True/True; gate True -> reads
F/0: text degree 1.0000; committed 1.0000; ... gate False -> no verdict: read failed its floor (described only), fails its gate
M/0: text degree 0.4886; committed 0.4886; no-transplant miss -0.0059; controls 7/1/4 True/True/True; gate True -> reads
...
=== 3. Two seeds of three, the separation, and the outcome term (section 3)
arm T: reads on 3 of 3 seeds: [0.0, 0.0, 0.0]
arm C: reads on 3 of 3 seeds: [1.0051, 0.9926, 0.9974]
arm F: reads on 0 of 3 seeds: []
arm M: reads on 3 of 3 seeds: [0.4886, 0.486, 0.5449]
separation, lowest of arm C minus highest of arm T: 0.9926; clears 0.5: True
outcome by the text's rules: the fifth term, metric validated, degree not read
```

(full output, every row, in `rule_from_text.out.txt`).

**Does it match what the text claims?** Yes. The rule the text states picks
the same site set, the same size and the same verdict as the code that ran, on
all twenty-four rows, including the entangled model's seed 1, where the choice
was decided by one episode in 600, and the free model's three "read failed its
floor". Every reading equals the committed one to four places; the separation
under the reconciled rule is 0.9926; and the text's own outcome rules put the
toy where version 4 says it is, on the fifth term. Had the text described a
different order of rules, a different tie-break or a different floor from the
one that ran, this would have come out different on at least the entangled
model's seeds 1 and 2. The one place the text and the code differ (the floor's
clause for a requirement at or below zero) does not bite on these twelve
models, and section 4 of the same output shows where it does (RT-238).

### Check 2. The committed code, run again from clean, against its committed outputs

`rerun_controls.py`, unchanged, run from a copy of `src/` whose output folder
points into this session's scratch space (the committed models, reads and gate
file linked in read-only, the models first checked against `SHA256SUMS` by the
script itself), then compared value by value with `compare_rerun.py`:

```
$ cd <scratch copy>/src && .venv/bin/python rerun_controls.py        # the committed code, unchanged; "done in 1485s"
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-scripts/compare_rerun.py <scratch copy>/out-controls-rerun
measure_C_seed0.json     values compared    110; differ 0
measure_C_seed1.json     values compared    110; differ 0
measure_C_seed2.json     values compared    110; differ 0
...
nominate_T_seed2.json    values compared   1980; differ 0
summary.json             values compared   1497; differ 0
table.md identical: True
TOTAL: 25 JSON files, 26722 values, 0 differ
fresh run: separation field {'0': 1.0051, '1': 0.9926, '2': 0.9974} | device cpu | torch 2.12.1 | seconds 1485
```

(every file's line in `compare_rerun.out.txt`).

**Does it match?** Yes. Every value the committed code wrote on 2026-10-03,
26,722 of them in 25 files, came back identical on this laptop today, and the
table is byte-identical; only the running time differs (1,485 seconds against
the committed 967, because this session ran other scripts alongside it). The
per-seed separation field is 1.0051, 0.9926 and 0.9974, whose lowest minus
arm T's highest is the 0.9926 of check 1. This repeats what the check of the
controls re-run (at `e184a6e`) found; it is repeated because the registration
leans on these files and the protocol makes their verification the tier 1
reviewer's.

### What these two checks do not cover

They cover the procedure on the toy. They do not cover the registered width
(RT-240), the registered generator (RT-239), the battery clause (RT-237) or the
outcome states the toy never reached (RT-241); those are the findings.

---

## The kill case

The case for not registering this text, as strongly as it can be put. The
registration's purpose is to fix in advance what would count as a result; as
written it fixes one thing that would make its best outcome impossible and
leaves several reachable outcomes without a name. The free model's gate
carries a clause about batteries that the task does not contain and that no
run has ever evaluated, and the design's own rule turns an unevaluable gate
into a failure, so "degree read" cannot be reached as written. The episode
counts it freezes were chosen because they were the only ones rehearsed, but
they were rehearsed at a third of the registered width, and a stand-in at the
registered width puts the high anchor under its own floor on two seeds of
three; if that happens the experiment falls into a two-model fallback that has
no registered outcome term, after both releases of money are drawn. The grammar
it registers is described by reference to a generator that shows the model its
own name as it acts, which is the one cue the whole design exists to keep out,
and the two lines that keep it out are not in the text. And the floor that is
meant to keep the divisor off zero "by construction" does so only through a
clause in code the text does not carry. None of this is expensive to fix: one
ruling on a clause, one sentence on the floor, one page on the episode format,
one table of outcomes, and either more fitting episodes or a rehearsal at
width 448 on the laptop. But every one of them is the kind of thing this
programme has already paid for once in a registered sentence nobody could
satisfy, and the registration commit is the one commit that cannot be taken
back.

---

## For the outside reviewers

Not a ruling; for the session that builds the tier 2 packet.

**(a) The files an outside reader who cannot run code most needs.**

1. `docs/successor-experiment-proposal-2026-10-03-v4.md`, with the list of
   ruled changes in this review's section "The registration text as
   reviewed".
2. `docs/rulings/2026-10-03-version-4-questions-rulings.md` (record B), the
   reconciliation `docs/rulings/2026-10-03-seven-questions-reconciliation.md`,
   `docs/rulings/2026-10-03-version-4-check-questions-rulings.md` and
   `docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md`.
3. `docs/2026-09-21-successor-measure-rehearsal.md` (sections 0, 3, 5, 6, 7,
   8): what the instrument does on built models and where it first failed.
4. `docs/2026-10-03-controls-rerun.md` and `docs/2026-10-03-competing-solver-run.md`:
   the toy figures under the rules as registered, and the ordinary competing
   solver.
5. `docs/known-failure-modes.md` and `docs/outside-review-protocol.md` (the
   brief and the closure rule).
6. This review, and the two checks it builds on:
   `reviews/2026-10-03-proposal-v4-check-claude-code.md` and
   `reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md`.
7. The two grammar headers, which say in prose what RT-239 is about:
   `experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py` (lines
   1 to 115) and `experiments/rehearsal-successor-measure/src/grammar.py`
   (lines 1 to 65).

**(b) Questions this review could not settle, for a reader from another lab.**

1. **Does a reading near 1 on the entangled model say anything the
   construction did not already guarantee?** Any piece that holds the label at
   the action position and moves nothing reads near 1. Is there a design
   change that would let the high anchor fail in an informative way, rather
   than only by its whole-state transplant missing the floor?
2. **What fit floor and fitting-sample size would you register for a
   twelve-way straight-line read on a 448-wide state?** RT-240 shows the
   ruled 420 fitting episodes are fragile under a crude stand-in; what would a
   lab that does this routinely use, and would it fix the regularisation in
   advance?
3. **Is the separation rule's asymmetry right?** It sets aside a seed that
   returns no verdict and counts a seed that returns an odd reading
   (the check-questions ruling, ruling 2). For a claim of "metric validated",
   is that the conservative direction, or does it make the result hostage to
   which failures happen to trip a floor?
4. **Is a mixture by item a fair middle anchor for a measure meant to read
   partial separation within each act?** The design says it is not, and keeps
   the mixed model anyway (W10). What middle anchor would you build at this
   size?
5. **Should the name cue at the moment of acting be closed by the grammar, or
   tested for by a control?** RT-239 asks the text to register the grammar
   that removes it. An outside reader may know a cleaner discriminator than
   removing it, one that would let a free model's reading be checked for
   reliance on a name.

---

## Scripts and outputs beside this file

In `reviews/2026-10-04-successor-v4-gate-a-scripts/`, each run from the root
of the checkout with the project's own Python (torch 2.12.1, scikit-learn
1.9.0, numpy 2.5.0, scipy 1.18.0), on the processor:

| Script | What it does | Output |
|---|---|---|
| `rule_from_text.py` | the decisive check: the rule from the text, on the committed grids; the reading, the controls that hold, the seeds rule, the separation and the outcome; the floor on the competing solver | `rule_from_text.out.txt` |
| `compare_rerun.py` | compares a fresh run of `rerun_controls.py` with its committed outputs | `compare_rerun.out.txt` |
| `failure_mode_pass.py` | the known-failure list's tests 1 to 3 on the committed outputs | `failure_mode_pass.out.txt` |
| `older_figures.py` | figures version 4 quotes from records older than 2026-10-03, against their files | `older_figures.out.txt` |
| `closure_sentences.py` | every paragraph using verified, measured, calibrated or attacked, and whether it names a record | `closure_sentences.out.txt` |
| `floor_forms.py` | where the two forms of the whole-state floor disagree, across every committed grid | `floor_forms.out.txt` |
| `solver_sentence.py` | the ruled sentence about the competing solver, against its outputs | `solver_sentence.out.txt` |
| `width_vs_count.py` | the width stand-in (NOT A RESULT) | `width_vs_count.out.txt` |
| `registered_shape_timing.py` | forward-pass timing at the toy and registered shapes on the processor | `registered_shape_timing.out.txt` |
| (the repository's) `check_launcher_argument_guard.sh`, `check_remote_forms.py` | failures 5 and 6 | `failure5_launcher_guard.out.txt`, `failure6_remote_forms.out.txt` |
===== END OF RECORD 5 =====

===== RECORD 6 of 25 - John's rulings of 2026-10-03 on the review of version 3 (binding on version 4) - `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md` (complete file, 9,929 characters) =====
# Ruling 2026-10-03: the review of successor proposal version 3 (RT-230 to RT-236) and the proposal's open decisions

*Recorded 2026-10-03 (Pacific) in a Claude Code session. **Mixed authorship:**
each ruling was put to John as one page of
`docs/rulings/2026-10-03-successor-v3-gate-c-queue-PROPOSAL.md` (pull request
75), with a recommendation, its confidence and the strongest alternative, and
he ruled on the sixteen pages together in the words **"Agreed on all"**. The
choices are his; none of the wording is his drafting. No compute was launched
and no money was spent under this ruling.*

*Written under the workspace plain-language rule. "The proposal" is
`docs/successor-experiment-proposal-2026-09-26-v3.md` (main line at
`6d4ec3a`). "The review" is its first independent review,
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-successor-v3-gate-c-claude-code.md`
(main line at `4cb7f8e`), whose findings are numbered RT-230 to RT-236 in the
red team ledger's sequence. Every number below is the review's or the
proposal's, with the place named.*

**Three things about how this ruling was reached, stated so they are not
found later.**

1. The session that recorded it also wrote the review and the packet. The
   pages on the review's findings (1 to 3) therefore recommended rulings on
   that session's own findings.
2. The packet had not been checked by a second session when John ruled, which
   the pairing rule of `docs/outside-review-protocol.md` asks for. That check
   is still owed, and so is the check of this file.
3. John ruled from the packet's one-page index and the three pages the
   session drew his attention to (1, 11 and 15). The record does not show
   whether he read the other pages in full.

Nothing here edits registered text, protocol text or the proposal. Version 4
of the proposal carries the changes. Two earlier documents gain a dated note
beside the sentence this ruling touches, and are otherwise left as written.

---

## What was ruled

### Page 1 — the fit floor applies to the piece that is transplanted (finding RT-230, serious)

*The review, RT-230 (MEASURED): the four-fifths floor was scored on the whole
straight-line read, while the transplant moves only the read's leading 1, 2,
4 or 8 directions. On arm C, the entangled model, the piece the rule chose
holds the label at 1.000, 0.544 and 0.306 on seeds 0, 1 and 2; the
8-direction piece holds it at 1.000, 0.900 and 0.989; the arm reads between
0.9897 and 1.0051 at every size.*

1. **Option (b) is ruled: only sizes whose own held-out accuracy clears four
   fifths may be chosen, and that accuracy is printed in the reporting
   table**, beside the whole read's. The accuracy of a piece is the held-out
   accuracy of a read given only the state's coordinates inside that piece, on
   the same development episodes and split as the whole read. An arm and seed
   with no size that clears returns "no verdict, read failed its floor".
2. **Sections 3 and 5.2 of the proposal are reworded** to say what was
   measured: the read holds the label; the largest piece transplanted holds
   it; no size moves the action.
3. **The readings the packet gave under this rule (1.0051, 0.9975 and 0.9974
   on arm C, at 8, 8 and 4 directions) are not committed results.** They are
   the session's reading of the review's outputs. The re-run of page 2
   produces them, and version 4 quotes the re-run.

The alternative that was put and not taken: fixing the size at 8 directions
with the smaller sizes as extra rows.

### Page 2 — the re-run comes before the registration review (finding RT-233, serious)

**The re-run of rehearsal items R-1 to R-6 under the registered rules,
including page 1's rule, is a precondition of the registration review (Gate
A) on version 4.** It covers controls 1, 2, 4 and 6 on arms C, F and M at the
site sets the rule nominates, and control 7 (the null transplant) at every
nominated site set. Its method is committed before its output, and a session
that did not run it checks it. Laptop only, $0. The arm M true-slot check is
already done (the review, RT-231: 0.0049, 0.0099 and 0.0529 against 0.10) and
version 4 cites the review for it, re-confirmed under page 1's rule by the
re-run.

### Page 3 — the four minor findings, accepted as the review states each fix

- **RT-232:** the read's accuracy is stated as a count of held-out episodes,
  and the registration names the device the registered figure is computed on.
- **RT-234:** the text says the whole-state floor is applied on development
  episodes at nomination and again on fresh episodes at the reading, and that
  a site set which clears the first and misses the second returns no verdict.
- **RT-235:** the report for the first full-size free-model run prints the
  read's accuracy at every layer, the chosen piece's own accuracy, and the
  candidates the nomination chose among.
- **RT-236:** depths are stated the same way in both places (the toy has four
  blocks and five running states; the registered model twelve and thirteen),
  and the label search and its check are cited by their main-line commits
  (`a97c12b`, `ecd2b6c`). A dated note goes beside the phrase "a five-layer
  model" in `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`.

### Pages 4 to 10, 12 to 14 and 16 — the proposal's decisions, agreed as the proposal recommends

| Proposal decision | Ruled |
|---|---|
| 2 | Arm T's ownership path is forced by its architecture, not encouraged by a penalty |
| 3 | Arm C entangles by architecture; no penalty against transplantable ownership directions |
| 4 | The two transplants are a subspace and its containing space at identical sites |
| 8 | A new experiment directory with its own registration, `experiments/08-…`; the compute ledger stays in experiment 06's folder as the programme's one record of money |
| 9 | The asymmetry between the own-directed and named-other conditions is recorded as a known limitation, not engineered away |
| 10 | The ownership-lesion check is a precondition for reading arm F and is never reported as evidence of a centre |
| 13 | The registration names a launcher that waits for the receipt, and "the trainer does not delete its own machine" is part of the registered recipe |
| 15 | Control 2's tolerance on arms C and F is 0.05 over the random subspace |
| 16 | Control 4 is reported and cannot veto a reading |
| 17 | Fifty timed steps are accepted for the second release's arithmetic; the five-hundred-step figure is taken from the first full-size run, and the later runs are repriced from it before the second release is asked for |
| 19 | The position sets are the rehearsal's four, by name |

*Dated note, 2026-10-03 (Pacific), later the same day, beside the table
above, which is left as written. After the controls re-run John ruled again
on two of its rows (`docs/rulings/2026-10-03-controls-rerun-rulings.md`):
**decision 15's 0.05 tolerance is withdrawn**, control 2 being kept as a
reported description with no pre-stated pass line; and **decision 16 is
reversed**, control 4 being redefined on both twins and made a control that
holds. Page 1 of this file also gains a reported figure, the piece's accuracy
at the other positions of its site, with the rule itself unchanged.*

### Page 11 — what a no verdict maps to (decision 14)

1. **No verdict on arm C** fires the two-arm fallback already accepted on
   2026-09-20.
2. **No verdict on arm M** drops arm M, which is then carried as an extension
   on the weekend roadmap.
3. **No verdict on arm F after arms T and C have separated is a fifth
   registered term: "metric validated, degree not read"**, reported with its
   reason after a colon.
4. **This amends the outcome list ruled on 2026-09-20** (section 2 of
   `docs/december-result-roadmap-2026-09-20.md`), which gains a dated note.
5. **The fifth outcome is satisfactory, and is stated as weaker than R1.**
   The packet put this as a suggestion and said it was John's call; "Agreed on
   all" is recorded as agreeing to it. Reason recorded: Stage 2's deliverable
   is the measure and not a verdict, and a validated measure with no reading
   delivers it.
6. The stop after the first full-size free-model run is unchanged: a miss of
   the floor there still goes to John before the second release.

### Page 15 — the handshake's machine half (decision 18)

**Option (b):** the registration says what is true today, that on the normal
path the laptop deletes the machine and the machine's own watcher is a
backstop for a laptop that never answers. Option (a), making the laptop wait
for the machine's acknowledgement, is the repair if a later run shows the
laptop failing to answer. **This takes option (a) off the Weekend 2 launcher
items** listed in `docs/weekend-1-handoff-2026-09-26.md`. The caution the
packet put with it is carried: twelve full-size runs rest on a backstop that
has not fired against the real vendor.

---

## What this changes, and where

- **Proposal version 4:** sections 3 (the outcome table gains the fifth term;
  the admission reworded), 5.2, 6.4, 7.2, 7.3, 7.4, 7.5 (the new column), 9,
  10, 11, 12.4, 13 (weakness W9) and 15 (every decision above marked ruled).
- **`docs/december-result-roadmap-2026-09-20.md`, section 2:** a dated note
  naming the fifth term.
- **`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`:** a dated note
  on the depth of the toy model.
- **The weekend roadmap and TimeAssembler:** the controls re-run as a Weekend
  2 goal; the handshake repair removed from the launcher items.
- **The red team ledger:** rows for RT-230 to RT-236 are owed. RT-212 to
  RT-229 have none either; both sets wait on the reconciliation that item 21
  of the 2026-09-21 ruling assigns to a later session.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit the proposal, registered text or protocol text.
===== END OF RECORD 6 =====

===== RECORD 7 of 25 - John's three rulings of 2026-10-03 after the controls re-run - `docs/rulings/2026-10-03-controls-rerun-rulings.md` (complete file, 5,989 characters) =====
# Ruling 2026-10-03: three decisions after the controls re-run

*Recorded 2026-10-03 (Pacific) in a Claude Code session. **Mixed authorship:**
each ruling was put to John as one page of
`docs/rulings/2026-10-03-controls-rerun-queue-PROPOSAL.md` (pull request 77),
with a recommendation, its confidence and the strongest alternative, and he
ruled on the three pages together in the words **"Agreed on all"**. The
choices are his; none of the wording is his drafting. No compute was launched
and no money was spent under this ruling.*

*Written under the workspace plain-language rule. "The re-run" is
`docs/2026-10-03-controls-rerun.md` (main line at `821f154`). "The proposal"
is `docs/successor-experiment-proposal-2026-09-26-v3.md`. "This morning's
rulings" is `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, which
this file amends in three places and which gains a dated note at each.*

**Cautions recorded with the ruling.** The session that recorded it also ran
the re-run and wrote the packet, the review and this morning's record. Neither
the re-run nor the packet had been checked by a second session when John
ruled. **Ruling 2 rests on a diagnostic written after the re-run's output was
seen; if the check of the re-run finds that diagnostic wrong, ruling 2 returns
to John.**

---

## What was ruled

### 1. Control 2, the other-agent control: kept, reported, with no pre-stated pass line

*The re-run, section 5 (MEASURED): control 2 has no figure on any toy model.
The one model that learned the other-agent condition, arm F seed 0, has a
read of the named agent's marker that is right on at most 137 of 180 held-out
episodes against 144 needed.*

1. **Control 2 stays in the design as a reported description:** how often the
   own-directed action moves under the named agent's piece, beside how often
   it moves under a random piece of the same size at the same sites.
2. **Its pass line is withdrawn.** The 0.05 tolerance set this morning (the
   proposal's decision 15) is not registered. With no pre-stated number,
   nothing about the control is unexercised in the sense of item 5 of the
   2026-09-21 ruling.
3. **The registration says in terms** that the control never ran at toy scale,
   why, and that a no verdict is the expected result.
4. **Its code path is run once on arm F seed 0 with the floor switched off**,
   at $0, labelled as a test of the code and not a result, so the registration
   is not the first time that code runs end to end.

The alternative that was put and not taken: exercising the control on a
made-up case built for the purpose.

### 2. Control 4, the too-early-position control: redefined on both twins, and it holds again

*The re-run, section 6 (MEASURED; the diagnostic was not pre-stated): as
written the control is above the no-transplant rate by 0.065 to 0.10 on six
of twelve models; in 0.5088 of pairs the donor twin's first own turn precedes
the recipient's; with positions taken before both twins' first own turns it
returns exactly the no-transplant rate on all twelve.*

1. **The control's positions are those before both twins' first own turns.**
2. **It is a control that holds:** a failure withholds the reading for that
   arm and seed. Its pass line is that the transplant changes nothing; the
   pre-stated run compares the model's outputs themselves, as the null
   transplant does, and reports the donor-value share beside the
   no-transplant share.
3. **The proposal's sentence that arms C and F "receive the ownership signal
   by other routes" at those positions is withdrawn.**
4. **This reverses this morning's ruling on the proposal's decision 16**, which
   made the control reported only, on the account now withdrawn.
5. **The redefined control is run as a pre-stated quantity before the
   registration review**, method first and then output, by a session that did
   not write the diagnostic. The diagnostic's figures are not quoted as that
   run.

The alternative that was put and not taken: redefining the positions and
keeping the control reported only.

### 3. A piece transplanted at several positions: its accuracy at the other positions is reported, not gated

*The review, finding RT-230 (MEASURED): on arm C seed 2 a one-direction piece
was right on 0.306 at the action position and 0.161 to 0.194 at the other
positions of its span; on arm M the 8-direction piece was right on 1.000 and
0.839 to 0.983. The pieces the re-run chose on arm C seeds 1 and 2 were not
measured at the other positions.*

1. **The reporting table gains a column:** the chosen piece's accuracy at the
   other positions of its site, beside its accuracy at the action position.
2. **It has no pass line.** The rule of this morning's page 1 is unchanged:
   the piece must reach four fifths at the action position.
3. **The column is filled for the twelve toy models before the registration
   review**, in the same run as ruling 2's.

The alternative that was put and not taken: requiring four fifths at every
position of the site.

---

## What this changes, and where

- **Proposal version 4:** section 7.2 (the piece's accuracy, where it is
  taken and what is reported), section 7.3 (items 2 and 4), section 7.4 (the
  frozen list: control 2 without a pass line; control 4 redefined, among the
  controls that hold), section 7.5 (the new column) and section 15 (decisions
  15 and 16).
- **`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`:** a dated note
  beside the table that carries decisions 15 and 16.
- **Before the registration review, one more short run**, method committed
  before output, by a session that did not write the diagnostic: control 4 as
  redefined, the new column, and control 2's code path with the floor
  switched off. Laptop only, $0. The check of the re-run is the natural place
  for it.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit the proposal, registered text or protocol text.
===== END OF RECORD 7 =====

===== RECORD 8 of 25 - John's evening ruling of 2026-10-03: the fifth outcome and the figure printed both ways - `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md` (complete file, 4,960 characters) =====
# Ruling 2026-10-03 (evening): the fifth outcome is satisfactory, and the new reported figure is printed both ways

*Recorded 2026-10-03 (Pacific), evening, in the Claude Code checking session
that raised both questions. **Mixed authorship:** each question was put to
John at the end of that session with a suggestion, and he ruled in the words
**"Yes, satisfactory and weaker than R1; print both figures"**. The choices
are his; none of the wording below is his drafting. No compute was launched
and no money was spent under this ruling.*

*Written under the workspace plain-language rule.*

**Cautions recorded with the ruling.** The session that recorded it also wrote
the two documents the questions come from: the check of the ruling packets
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-rulings-2026-10-03-check-claude-code.md`,
section 5) and the findings of the short pre-stated run
(`docs/2026-10-03-short-prestated-run.md`, section 4). Neither had been
checked by a second session, or merged, when John ruled. This file is owed
the same check.

---

## What was ruled

### 1. The fifth registered outcome is satisfactory, and is stated as weaker than R1

*Background: page 11 of the first ruling packet of 2026-10-03 asked whether
the fifth outcome, "metric validated, degree not read" (the built models
separate and the freely trained model returns no verdict), counts as
satisfactory. It gave a suggestion and said it was John's call. John's
"Agreed on all" that morning was recorded as settling it
(`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 11, item 5).
The check found that recording honest but thin, and recommended he confirm or
overturn it in a sentence.*

1. **The fifth outcome is satisfactory.**
2. **It is stated as weaker than R1** ("metric validated, degree read").
3. This confirms item 5 of page 11 of that morning's rulings **on its merits**,
   in John's own words, and it no longer rests on the general agreement.
4. The dated note of 2026-10-03 under the outcome table in
   `docs/december-result-roadmap-2026-09-20.md` therefore stands as written,
   and gains a second dated note pointing here.

### 2. The new reported figure is printed both ways

*Background: ruling 3 of `docs/rulings/2026-10-03-controls-rerun-rulings.md`
added a reported column, the chosen piece's accuracy at the other positions
of its site, and did not say how it is computed. The short pre-stated run
computed it two ways, as that session's own reading: one figure per position,
and one figure on the state averaged over the other positions of the site.
The two disagree about the mixed model: on the average its piece clears four
fifths on every seed (163, 174 and 175 right of 180); position by position it
misses at three to six of ten positions.*

1. **The registered reporting table prints both:** the piece's accuracy at
   each other position of its site, and its accuracy on the average over
   those positions, beside its accuracy at the action position.
2. **Neither has a pass line.** The rule is unchanged: the piece must reach
   four fifths at the action position.
3. How each is computed is as the short run's method states it
   (`docs/2026-10-03-short-prestated-run-method.md`, section 4): a fresh read
   fitted at that position on the piece's coordinates, on the same episodes
   and split; for a site that runs from the model's first own turn to the
   action, the positions reported one by one are the five tokens of that
   first own turn and the five before the action, and the positions between
   them are covered by the average only.

*Dated note, 2026-10-03 (Pacific), late evening, beside item 3, which is left
as written. The check of this record
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-short-prestated-run-check-claude-code.md`,
finding 19) found that "print both figures" accepted the computation in item
3 by implication only, and asked John whether section 4 of the short run's
method is what he meant. He answered in the words **"Yes, section 4 of the
method is what I meant"**. Mixed authorship: the question was the checking
session's, the choice is his. Item 3 therefore rests on his own words. The
same check found that the figure taken on the average moves by one episode in
180 depending on the order the average is added up in (its finding 11); that
is a note for version 4 of the proposal and is not part of this ruling.*

---

## What this changes, and where

- **Proposal version 4:** section 3 (the fifth term marked satisfactory and
  weaker than R1, by this ruling); sections 7.2 and 7.5 (the new column, both
  ways, with how each is computed).
- **`docs/december-result-roadmap-2026-09-20.md`:** a dated note under the
  existing one.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit the proposal, registered text, protocol text or any
earlier ruling file.
===== END OF RECORD 8 =====

===== RECORD 9 of 25 - first record of John's ruling on version 4's seven questions - `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md` (complete file, 7,864 characters) =====
# Ruling 2026-10-03 (late evening): the seven questions of successor proposal version 4

*Recorded 2026-10-03 (Pacific), late evening, in the Claude Code session that
drafted version 4 of the proposal and raised the seven questions. **Mixed
authorship:** each question was put to John in that session with a
suggestion, how confident it was and the strongest alternative, and he ruled
on the seven together in the words **"Agreed on all"**. The choices are his;
none of the wording below is his drafting. No compute was launched and no
money was spent under this ruling.*

*Written under the workspace plain-language rule. "Version 4" is
`docs/successor-experiment-proposal-2026-10-03-v4.md` (pull request 83). The
questions are its section 19 as first filed, at commit `a64aa82`.*

*Dated note, 2026-10-03 (Pacific), night, added by a session that did not
write this file; the text below is left as written. The same seven questions
were put to John a second time that evening, in another session, and
recorded in `docs/rulings/2026-10-03-version-4-questions-rulings.md`. The two
records differ on four points: rulings 2, 3, 4 and 6 below. **John ruled that
the other record stands on all four**
(`docs/rulings/2026-10-03-seven-questions-reconciliation.md`): the library
versions are pinned, not only recorded; the registration says what applying
the piece rule after the layers are chosen can miss; the sampling band is
printed at the floor; and the separation is the lowest of arm C's readings
minus the highest of arm T's, not compared seed by seed. On everything else
this record stands.*

**Cautions recorded with the ruling.**

1. The session that recorded it also wrote version 4, the questions and the
   suggestions. It is owed a check by a session that did not, under the
   pairing rule of `docs/outside-review-protocol.md`.
2. John ruled from a walk-through of the seven in the session's chat, which
   put them in a different order from section 19 and said which three it
   thought needed real thought. The record does not show whether he read
   section 19 itself.
3. **The session flagged one question as deserving more of his attention than
   the others, with its own confidence low to moderate: what an arm's outcome
   is when its three seeds disagree (ruling 6 below).** It is a new
   pre-stated rule and it can decide which registered outcome the experiment
   ends on. A general "Agreed on all" settles it on the record. If John wants
   to look at that one again, a sentence does it, as it did for the fifth
   outcome earlier the same day.
4. Version 4 had not been checked by a second session, or merged, when John
   ruled.

Nothing here edits registered text, protocol text, any earlier ruling file or
version 3. Version 4 carries the changes.

---

## What was ruled

Numbered as in section 19 of version 4.

### 1. The accuracy floor is on the transplanted piece only

The ruling of 2026-09-26 put the four-fifths floor on the whole straight-line
read. The ruling of 2026-10-03 (morning, page 1) put it on the piece that is
transplanted and did not say whether the earlier floor stays as a second
condition.

1. **The floor applies to the piece only.**
2. **The whole read's count is printed beside the piece's**, and is not a
   second condition.

The alternative that was put and not taken: require both.

### 2. The piece rule is applied after the layers are chosen

**Confirmed as the controls re-run ran it:** the requirement that a piece
reach four fifths decides which sizes of piece may be chosen, and never
changes which layers are used.

The alternative that was put and not taken: let the piece's accuracy also
decide between layer sets, which has not been run.

### 3. The registered fit is computed on the laptop's processor

1. **The device is the laptop's processor**, never its graphics chip. The
   figure computed there is the registered one.
2. The model's states are computed in the model's own 32-bit format, and the
   read is fitted by scikit-learn's logistic regression in 64-bit, as the
   controls re-run did.
3. **The versions of torch, scikit-learn and numpy are recorded in the output
   file. They are not pinned by the registration.**

The alternative that was put and not taken: the graphics chip.

### 4. The numbers of episodes at the full size are the toy's

**The registered measurement uses the counts the procedure was rehearsed
at:** 600 development episodes, of which the last 180 are held out for every
fit, so the floor is 144 of 180; 800 fresh matched pairs; 800 pairs on the
relaxed set; 3,000 held-out episodes for the learning gates, so the bar is
790; and 200 shuffles for the permutation null.

The alternative that was put and not taken: more held-out episodes, so that
the floor is not decided by a handful. The caution put with the suggestion is
carried: at 180, one episode is 0.0056 of the scale.

### 5. The other-agent control is compared against twenty random pieces

**The description reports the own-directed action's share moved under the
named agent's piece beside twenty random pieces of the same size at the same
sites, reported the way the random-pieces control reports them** (median,
95th percentile, and the counts below, equal and above). It still has no pass
line.

One consequence put with the suggestion and carried: this is a small change
to the control's code, so the code path that ran once on 2026-10-03, with a
single random piece, is not quite the one registered.

The alternative that was put and not taken: leave it at one draw.

### 6. When an arm's three seeds disagree, two of three decide

**The rule is the one the design already uses for its gates: at least two
seeds of three, with the third reported.**

How the session reads that, for John to overturn (the wording is the
session's):

1. An arm is read if at least two of its three seeds return a reading. It
   returns no verdict, as an arm, if two or more of its seeds return no
   verdict.
2. The separation bar is cleared if the entangled model's reading minus the
   separable model's is 0.5 or more on at least two of the three seeds,
   compared seed by seed as before.
3. Every seed is printed, whichever way it went.

The alternative that was put and not taken: all three seeds. See caution 3
above.

### 7. The ordinary competing solver is run under the piece rule before the registration review

1. **The ownership-blind solver's three committed toy models are put through
   the nomination and the reading as now registered**, on the laptop, at $0,
   with the method committed before the output.
2. **It is run before the registration review opens, by a session other than
   the one that drafted version 4**, and is owed its own check like any other
   run.
3. The expected result, stated now: no verdict, because a solver with no
   "this turn is yours" signal should have no read of its own marker that
   reaches four fifths.

The alternative that was put and not taken: state in the registration that it
was not measured under the rule, and leave it to the reviewer.

---

## What this changes, and where

- **Proposal version 4:** sections 3 (the seed rule), 6.4 and 7.2 (the floor
  on the piece only; the order the piece rule is applied in; the device), 7.3
  (the other-agent control's twenty draws; the solver run), 7.4, 8.1, 9 (the
  episode counts and the device as set numbers), 10, 11 and 19 (each question
  marked ruled).
- **One more short run before the registration review:** the competing solver
  under the piece rule, method first, by another session. Laptop only, $0.
- **Code owed with the registered measurement:** the other-agent control's
  twenty draws.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit registered text, protocol text, version 3 or any
earlier ruling file.
===== END OF RECORD 9 =====

===== RECORD 10 of 25 - second record of the same ruling, which stands where the two differ - `docs/rulings/2026-10-03-version-4-questions-rulings.md` (complete file, 8,617 characters) =====
# Ruling 2026-10-03 (late evening): the seven questions version 4 of the proposal asks

*Recorded 2026-10-03 (Pacific), late evening, in a Claude Code session.
**Mixed authorship:** each question was put to John as one page of
`docs/rulings/2026-10-03-version-4-questions-PROPOSAL.md` (pull request 84),
with a recommendation, its confidence and the strongest alternative, and he
ruled on the seven pages together in the words **"Agreed on all"**. The
choices are his; none of the wording is his drafting. No compute was launched
and no money was spent under this ruling.*

*Written under the workspace plain-language rule. The questions are those of
section 19 of version 4 of the successor experiment proposal,
`docs/successor-experiment-proposal-2026-10-03-v4.md`, read at `a64aa82` on
pull request 83, which was open and unmerged when John ruled.*

*Dated note, 2026-10-03 (Pacific), night; the text below is left as written.
The same seven questions were put to John in the session that drafted version
4, and recorded there as
`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`. The two
records differ on four points (rulings 2, 3, 4 and 6). **John ruled that this
record stands on all four**
(`docs/rulings/2026-10-03-seven-questions-reconciliation.md`).*

**Cautions recorded with the ruling.**

1. The session that recorded it wrote the packet, and before that the review
   of version 3, two earlier packets and the controls re-run. Rulings 1, 2
   and 3 close gaps in rulings that session drafted; ruling 2 confirms a
   reading that session chose.
2. The packet had not been checked by a second session when John ruled, and
   version 4 had not been checked either. Both checks, and the check of this
   file, are owed.
3. **Ruling 6, part 2, was this session's own proposal and is in no earlier
   document.** John agreed to it from the packet's index and its summary in
   conversation, where it was one of three pages drawn to his attention.

---

## What was ruled

### 1. The fit floor is on the piece only

Only sizes of piece that themselves reach four fifths on held-out development
episodes may be chosen. **The whole read is not a second condition.** Its
count is printed beside the piece's in the reporting table. This narrows item
1 of the ruling on RT-212 (`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`),
which put the floor on the whole read; that file gains a dated note.

The alternative that was put and not taken: requiring both.

### 2. The piece rule is applied after the layers are chosen

For each group of positions the rule first takes the fewest layers at which
the whole-state transplant clears its floor; only then are sizes whose piece
misses four fifths excluded. The piece rule never changes which layers are
used. **The registration says in a sentence what this can miss:** a model
whose label is readable only at layers later than the earliest ones at which
the transplant works returns "no verdict, read failed its floor". The report
for the first full-size free-model run already prints the accuracy at every
layer and the candidates the rule chose among, so such a miss is visible when
John rules at that stop.

The alternative that was put and not taken: letting the piece rule take part
in choosing the layers, which would need the toy re-run again.

### 3. The registered accuracy is computed on the laptop's processor, with the library versions pinned

The device is the laptop's processor. The model's states are 32-bit; the read
is fitted by scikit-learn in 64-bit. **The library versions are pinned in a
committed file named in the registration**, in the way
`.venv-lock-2026-08-28.txt` does for the project's environment. The figure
computed that way is the registered one. If the processor proves impractical
at full size, that is a fresh question for John, not a switch.

### 4. The episode counts are the toy's, and the sampling band is printed at the floor

600 development episodes with the last 180 held out; 800 fresh matched pairs;
800 on the relaxed set; 3,000 for the gates; 200 shuffles for the permutation
baseline. **Beside every count taken against the four-fifths floor, the
reporting table prints the band that sampling alone would put around it.**
Recorded with the ruling: at 180 held-out episodes one episode is 0.0056, and
a piece whose true accuracy is exactly four fifths passes about half the
time. A miss at the first full-size free-model run goes to John with that
band beside it.

The alternative that was put and not taken: more held-out episodes for the
read, which would need the toy fits run once at the new count.

### 5. The other-agent control is compared with twenty random pieces

Control 2 reports how often the own-directed action moves under the named
agent's piece, beside twenty random pieces of the same size at the same sites:
their middle value, their 95th percentile, and where the real figure sits
among them. No pass line, as ruled earlier that day. **The code changes
accordingly, and the code test of 2026-10-03 is run once more on the changed
code**, labelled a test of the code and not a result.

### 6. What a model's outcome is when its seeds disagree

**Part 1.** A model returns a reading if **at least two of its three seeds**
return one; the third is reported. This is the rule the design already uses
for its gate on learning and for the channel-removal check.

**Part 2.** **The separation between the two built anchors is the lowest
reading among arm C's seeds that read, minus the highest among arm T's seeds
that read. It must be at least 0.5.** Seeds are not paired by number.
Recorded reason: seed 0 of one model has no relation to seed 0 of another,
and a pairing by number is not defined when the two models read on different
numbers of seeds. On the toy this is 0.9926 (arm C reads 1.0051, 0.9926 and
0.9974; arm T reads 0.0000 on every seed;
`experiments/rehearsal-successor-measure/out-controls-rerun/summary.json`).

**What follows.** "Metric validated" means arms T and C each read on at least
two seeds and the separation so defined is at least 0.5. "Degree read" means
arm F reads on at least two seeds. If arm F reads on one seed only, the
outcome is "metric validated, degree not read", and that seed's figure is
printed as a description.

The queue ruling's page 1a set the bar at 0.5 as "the minimum gap between the
entangled arm's reading and the separable arm's reading" and did not say how
the gap is taken across seeds; the proposal's "per seed" was the proposal's.
This ruling says how. That file gains a dated note.

The alternatives that were put and not taken: all three seeds; and keeping
the gap paired by seed number.

### 7. The ordinary competing solver is run under the rules as now registered

The three committed ownership-blind toy models
(`experiments/rehearsal-successor-measure/out-repairs/models/ckpt_blind_base_seed{0,1,2}.pt`)
are put through the nomination and reading as registered, on the laptop, $0,
method committed before output, and checked by a session that did not run it,
**before the registration review**. The method states, as the running
session's reading, what "the model's own turn" and its twin pairing mean for
a solver with no acting channel. The expected result is no verdict on every
seed; a reading on any seed goes to John before anything else moves.

The alternative that was put and not taken: saying in the registration that
it was not measured.

---

## What this changes, and where

- **Proposal version 4:** section 3 (the outcome wording of ruling 6);
  section 7.2 (rulings 1 to 3); section 7.3, item 2 (ruling 5); section 7.5
  (the band of ruling 4); section 9 (the counts filled; the separation as
  defined); sections 7.3, 8.1 and 10 (the solver's figures once ruling 7's
  run exists); section 19 (the seven questions marked ruled). It is that
  version's author, or a session John names, who writes them in.
- **Dated notes** in `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`
  (RT-212, item 1) and `docs/rulings/2026-09-26-weekend-1-queue.md` (page 1a).
- **Before the registration review, at $0:** the competing-solver run and its
  check (ruling 7); the changed control 2 code and its code test (ruling 5).
- **STATUS.md and data/project.toml are not touched by the commit that lands
  this file**, because pull request 83 was open and edits both; whichever
  session next updates them carries this ruling in.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit the proposal, registered text or protocol text.
===== END OF RECORD 10 =====

===== RECORD 11 of 25 - John's ruling on which of the two records stands - `docs/rulings/2026-10-03-seven-questions-reconciliation.md` (complete file, 3,795 characters) =====
# Ruling 2026-10-03 (night): which of two records stands on the seven questions of proposal version 4

*Recorded 2026-10-03 (Pacific), night, in a Claude Code session. **Authorship:
John's.** The question was put to him with the four differences laid out and a
recommendation; he ruled in the words **"Your record stands on all four, do
the clean-up"**. No compute was launched and no money was spent.*

*Written under the workspace plain-language rule.*

## What happened

On the evening of 2026-10-03 the seven questions in section 19 of version 4
of the successor experiment proposal were put to John twice, in two sessions,
within minutes of each other, and he answered "Agreed on all" in both.

- **Record A:** `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`,
  by the session that drafted version 4 (pull request 83). It records
  agreement to version 4's own suggestions.
- **Record B:** `docs/rulings/2026-10-03-version-4-questions-rulings.md`, by
  the session that wrote a seven-page packet on the same questions
  (`docs/rulings/2026-10-03-version-4-questions-PROPOSAL.md`, pull request
  84). It records agreement to that packet's recommendations.

Neither session knew of the other's record until both were filed. The two
agree on questions 1, 5 and 7 and on the main answer to 2, 4 and 6. They
differ on four points.

## What was ruled: record B stands on all four

| Question | Record A | Record B, which stands |
|---|---|---|
| 3, the device | the library versions are recorded and **not pinned** | the library versions are **pinned in a committed file named in the registration** |
| 2, the order of the piece rule | confirmed as run | confirmed as run, **and the registration says in a sentence what it can miss**: a model whose label is readable only at layers later than the earliest ones at which the transplant works returns no verdict |
| 4, the episode counts | the toy's counts | the toy's counts, **and beside every count taken against the four-fifths floor the reporting table prints the band that sampling alone would put around it** |
| 6, seeds that disagree | two of three; the separation "cleared if cleared on two or more seeds", compared seed by seed | two of three; **the separation is the lowest reading among arm C's seeds that read minus the highest among arm T's seeds that read, at least 0.5, with seeds not paired by number**; "metric validated" means both anchors read on at least two seeds and that separation clears; "degree read" means arm F reads on at least two seeds |

On everything else the two records say the same thing and both stand.

## What this changes, and where

- **Record A** gains a dated note at its head pointing here. Its text is
  otherwise left as written.
- **Record B** gains a dated note at its head saying a second record exists
  and that this file settles the differences.
- **Version 4 of the proposal** is edited at the passages that state these
  four points (its header table, sections 3, 7.2, 7.4, 7.5, 9 and 20), and
  carries a short notice at its head naming this ruling. **Those edits were
  made by the session that recorded this ruling, not by version 4's author,
  and version 4 is long: a sentence elsewhere in it may still state one of
  the four points the old way. Where it does, this ruling governs.** The
  check version 4 is owed should look for such sentences.

## Cautions

The session that recorded this wrote record B and the packet behind it, and
recommended that record B stand. John's ruling is in his own words, quoted
above. This file and the edits to version 4 are owed a check by a session
that wrote neither.

## What this file does not do

It releases no money and issues no go. It does not open the registration
review. It does not edit registered text or protocol text.
===== END OF RECORD 11 =====

===== RECORD 12 of 25 - John's ruling on the two questions raised by the check of version 4 - `docs/rulings/2026-10-03-version-4-check-questions-rulings.md` (complete file, 2,870 characters) =====
# Ruling 2026-10-03 (night): the two questions raised by the check of proposal version 4

*Recorded 2026-10-03 (Pacific), night, by the Claude Code coordination
session. **Authorship: mixed.** The check of version 4 (pull request 86,
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-claude-code.md`,
section 6) proposed each answer. The coordination session put both questions
to John once, with those suggestions, and he ruled in the words **"Agreed on
both suggestions"**. No compute was launched and no money was spent.*

*Written under the workspace plain-language rule.*

## What was ruled

1. **The other-agent control's code is changed to draw twenty random pieces,
   and its code test is run again on the changed code, before the
   registration review.** This is how the second record of the seven-question
   ruling has it (`docs/rulings/2026-10-03-version-4-questions-rulings.md`,
   ruling 5). The first record had it done with the registered measurement
   (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`). Doing
   it before the review satisfies both records. The reconciliation
   (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`) did not list
   this difference. Version 4 follows the first record at lines 1834 to 1836
   and 3866 to 3868. The registration text follows this ruling.

2. **The rule that separates the two built models stays as ruled.** That rule
   is the lowest reading among the entangled model's seeds that return a
   reading, minus the highest among the separable model's, at 0.5 or more,
   with seeds not paired by number. It forgives a seed that returns no
   verdict. It does not forgive a seed that returns an odd reading. The
   registration says so in one sentence. The less strict alternative, which
   would take the middle reading of each model's three seeds, was not taken.

## For John to know, not ruled here

The check found six places where the two records of the seven-question ruling
differ without the reconciliation listing them (section 3.3 of the check). One
of them is question 1 above. On the other five, the second record simply says
more and nothing conflicts. Under the reconciliation's own rule that both
records stand, they stand as written in the second record, and the
registration text carries them.

## What this changes

- The registration text: both rulings above, the five fuller points from the
  second record, and the thirty wording fixes in section 4 of the check.
- Before the registration review: the other-agent control's code with twenty
  random pieces, and its code test re-run. The competing-solver session
  (branch `w2b-job1-competing-solver-run`) already has this change in its
  plan. Its check confirms the change was made.
- Nothing edits version 4, an earlier ruling file, STATUS.md or
  `data/project.toml` here.
===== END OF RECORD 12 =====

===== RECORD 13 of 25 - John's ruling of 2026-10-04 on seven questions from the competing-solver run and the twenty-piece control - `docs/rulings/2026-10-04-competing-solver-and-control-2-rulings.md` (complete file, 4,173 characters) =====
# Ruling 2026-10-04: seven questions from the competing-solver run, the twenty-piece control and their check

*Recorded 2026-10-04 (UTC; the evening of 2026-10-03, Pacific) by the
Claude Code coordination session. **Authorship: mixed.** Each question and
its suggestion come from the findings of pull request 88
(`docs/2026-10-03-competing-solver-run.md`, section 8), pull request 89
(`docs/2026-10-03-control-2-twenty-draws.md`, section 7) and their check,
pull request 90
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md`,
section 9). The coordination session put all seven to John once, with the
check's version of each suggestion, and he ruled in the words **"Agreed on
all seven"**. No compute was launched and no money was spent.*

*Written under the workspace plain-language rule.*

## What was ruled

1. **Which reading of the solver the registration cites.** The main reading
   has the acting channel removed, as the solver was trained and scored. The
   reading with the channel left on is stated beside it. The registration
   says plainly that the main reading's "no verdict" comes from how the
   twins are paired: their states are identical, so every transplant is a
   null transplant. It is not evidence about the measure. The reading with
   the channel left on is the one that tests the measure.
2. **The registration says what stopped this solver**, in the check's
   sentence: "On the toy, the ordinary competing solver returned no verdict
   because no site set cleared the floor at nomination; behind that, its
   best piece missed the piece rule by 119 or more of 180 and its untouched
   rate missed the no-transplant rule by 0.11 or more, and it would have
   failed the gate on learning had it been gated as the free model is. For
   a model near chance the floor itself is close to zero and is decided by
   one or two episodes."
3. **The no-transplant formula is reported, not generalised.** It withholds
   a reading here, which is the right outcome. But it assumes wrong answers
   spread evenly over the other values, and this solver's do not, so the
   registration does not describe the formula as true of every model
   (version 4, lines 1178 to 1183).
4. **The registered other-agent control is `control2_twenty_draws.control2`.**
   `rerun_controls.control2` is named as the earlier version, kept as the
   record of the re-run. The full-size registered code takes control 2 from
   the new function, so there is one control 2 at registration.
5. **The 95th percentile of the twenty random pieces stays as the summary**,
   as ruled, and all twenty are printed beside it.
6. **The solver run's explanation is corrected before it is quoted.** The
   solver's findings (section 4 and question 2) and the description of pull
   request 88 say the gate on learning stopped the solver. Version 4 does not
   gate competing solvers. The session that writes the registration text
   uses "would fail the gate if it were gated as the free model is". No
   re-run, and no rule change. Pull request 88 was merged as written.
7. **No new run before the registration review.** The registration's
   section 13 gains a two-sentence weakness: the toy's ordinary competing
   solver fails the task, so its "no verdict" shows only that the measure
   returns nothing on a model that has not learned the task. It does not
   show what the measure does on a model that does the task by another
   route. The alternative, training a solver that learns from another cue
   before the review, was not taken.

## Also merged on John's instruction

Pull requests 88 (the competing-solver run), 89 (the other-agent control
against twenty random pieces, NOT A RESULT) and 90 (their check). All three
are on the main line at `ecf3820`.

## What this changes

All seven rulings go into the registration text, together with version 4,
the thirty wording fixes from the check of version 4, the ruling of
2026-10-03 on that check's two questions, and the changes in section 7 of
the check in pull request 90. Nothing here edits version 4, an earlier
ruling file, STATUS.md or `data/project.toml`.
===== END OF RECORD 13 =====

===== RECORD 14 of 25 - the check of version 4 by a session that did not write it (holds the wording fixes the registration text must carry) - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-claude-code.md` (complete file, 62,740 characters) =====
# Check of version 4 of the successor experiment proposal, of the two ruling packets behind it, and of the ruling that reconciled them

*Written 2026-10-03 (Pacific), night, by the Claude Code session "MVM W2c check
of proposal version 4", in its own worktree (branch `w2c-proposal-v4-check`,
cut from the main line at `41b0bd3`, the commit that put version 4 and the
three ruling records on the main line as pull request 85). This is a paired
check under the pairing rule of `docs/outside-review-protocol.md`. It is not
the registration review. Laptop only, on the processor. Nothing was rented,
trained or spent: $0. Nothing was edited but this file and the scripts beside
it.*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (the command and its output are in this file or in the folder
beside it) or **ARGUED** (reasoning a reader can dispute).*

## What this session opened, and what it did not

**It wrote none of what it checks.** It did not write version 4, any ruling
record, either packet, the controls re-run or the short pre-stated run.

**Opened and read in full:** version 4
(`docs/successor-experiment-proposal-2026-10-03-v4.md`, all 4,219 lines); the
six ruling files of 2026-10-03 and the packet
`docs/rulings/2026-10-03-version-4-questions-PROPOSAL.md`.

**Opened in part, to look up a figure or a sentence:** version 3 (one row of
its section 9); the findings of the controls re-run and of the short
pre-stated run; the checks of both; the two earlier ruling files that gained
dated notes; the December-result roadmap's outcome table; the compute ledger;
the toy code's constants; and the committed output files under
`experiments/rehearsal-successor-measure/`.

**Not opened:** any chat or transcript of another session; the first two
packets of 2026-10-03 (they were checked earlier, and version 4 quotes the
rulings and not the packets); the worktree of the session running the
competing solver.

**One thing found by accident and used:** a file outside the committed
record, `.venv-lock-2026-08-28.txt`, in the main checkout. Three documents
cite it, so this session looked at whether it is committed. It is not
(finding 9).

**Names used below.** The four trained systems are called what version 4
calls them, with the plain meaning first: the separable model (arm T), the
entangled model (arm C), the mixed model (arm M) and the freely trained model
(arm F). "The piece" is the part of the internal state that is actually
transplanted. "Record A" is the ruling record written by the session that
drafted version 4
(`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`). "Record B"
is the one written by the session that wrote the packet
(`docs/rulings/2026-10-03-version-4-questions-rulings.md`). "The
reconciliation" is John's ruling that record B stands on the four points
where they differ (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`).
Line numbers are version 4's at `41b0bd3`.

---

## The result in one page

**What held.**

- **Every number checked matches the record it cites.** 89 comparisons of
  toy figures against the committed output files, all equal. The site list in
  section 18 is the rule's output, set for set (325 and 45). Every dollar
  figure is in the ledger line or the note it names, and the arithmetic of
  section 12 comes out as printed.
- **The first three sets of rulings (the morning's sixteen pages, the three
  after the controls re-run, and the evening's two) are carried correctly.**
  36 rows checked, all "yes".
- **The passages marked "reconciled" say what the reconciliation says.**
- **The packet's numbers are right**, including the 0.9926 on its page 6, and
  the reasoning of page 6 holds.

**What did not hold.**

1. **Four sentences still give the separation between the two built models
   the old way**, seed by seed: lines 412 to 414, the second half of the cell
   at line 2256, lines 2418 to 2420 and line 3814. One of them sits in the
   same table cell as the reconciled wording.
2. **Version 4 carries record A's wording wherever the reconciliation's
   table did not list a difference, and record B says more in five such
   places.** The reconciliation says the two records "say the same thing" on
   everything outside its four rows. They do not quite. One of the five is a
   difference of substance: when the changed code for the other-agent control
   is written and tested (finding 4).
3. **Version 4 contradicts itself in one place that matters.** Section 7.2
   fixes the laptop's processor as the device for the registered accuracy;
   section 11, step 5a, still says that if the laptop cannot do it the work
   moves to rented time and "is said". Record B says that case is a fresh
   question for John.
4. **Two citations in the "pinned versions" passage do not check out.** The
   output file version 4 names records one library version of three. And the
   file given as the model for pinning is not committed: the repository's own
   ignore list keeps it out.
5. **The bookkeeping around the edges is stale**: the header still says three
   sets of rulings and pull request 83; section 19's heading still says each
   question was ruled "as suggested"; the printed output of section 17's text
   sweeps no longer matches the file.

**Is version 4 ready to become the registration text?** Yes, once the list in
section 4 below is made and the competing solver's run is written in. Nothing
found changes a number, a rule or a design choice. Every item is wording, a
citation or a carried-over sentence, and all of it can be done in one pass.
One item needs John first (question 1 at the end).

---

## 1. Job 1: does version 4 say what the rulings say?

One row per ruling. "Where" is the place in version 4 that carries it.

### 1.1 The morning rulings (`docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`)

| Ruling | Where version 4 carries it | Carried correctly? |
|---|---|---|
| Page 1, item 1: only sizes of piece that themselves reach four fifths may be chosen; the count printed beside the whole read's; no size clearing returns "no verdict, read failed its floor" | section 6.4, item 2 (lines 1145 to 1154); section 7.2, items 1 and 3 (lines 1299 to 1307, 1544 to 1553); section 9, the fit-floor row | yes; it quotes the ruling's own words |
| Page 1, item 2: sections 3 and 5.2 reworded to "the read holds the label; the largest piece transplanted holds it; no size moves the action" | section 3 (lines 360 to 375); section 5.2 (lines 750 to 757) | yes |
| Page 1, item 3: the packet's forecast readings are not committed results; version 4 quotes the re-run | section 5.2 (lines 783 to 787); section 20 (lines 4083 to 4086) | yes; it says the forecast was wrong on one seed |
| Page 2: the controls re-run comes before the registration review; the mixed model's true-slot check cited to the review and re-confirmed | section 7.3 (lines 1739 to 1751); section 5.3 (lines 902 to 910); section 15, entry 25 | yes |
| Page 3, the read's accuracy as a count, on a named device (finding RT-232) | section 7.2, item 1 (lines 1320 to 1332) | yes |
| Page 3, the whole-state floor applied twice (RT-234) | section 6.4, item 1 (lines 1134 to 1144) | yes |
| Page 3, the fuller report for the first full-size run (RT-235) | section 7.5 (lines 2137 to 2144); section 11, step 5a | yes |
| Page 3, depths stated alike; two citations by main-line commit; a dated note in the earlier rulings file (RT-236) | section 7.2, item 1 (lines 1407 to 1414); the note exists (section 3.4 below) | yes |
| Decision 2: the separable model's ownership path is forced by its architecture | section 5.1 (lines 712 to 715); section 15, entry 2 | yes |
| Decision 3: the entangled model entangles by architecture, no penalty | section 5.2 (lines 815 to 818); entry 3 | yes |
| Decision 4: the two transplants are a subspace and its containing space at the same sites | section 6.2; entry 4 | yes |
| Decision 8: a new experiment directory; the ledger stays where it is | section 12.2 (lines 2673 to 2676); entry 8 | yes |
| Decision 9: the own-versus-named asymmetry recorded as a known limitation | section 4.2 (lines 557 to 558); weakness W6; entry 9 | yes |
| Decision 10: the channel-removal check is a precondition and never evidence of a centre | section 8.2 (lines 2225 to 2230); entry 10 | yes |
| Decision 13: the launcher waits for the receipt; the trainer does not delete its own machine | section 5 (lines 670 to 672); entry 13 | yes |
| Decision 15: the other-agent control's 0.05 tolerance (later withdrawn) | section 7.3, item 2; entry 15 | yes, as withdrawn |
| Decision 16: the too-early-position control reported only (later reversed) | section 7.3, item 4; entry 16 | yes, as reversed |
| Decision 17: fifty timed steps accepted; the five-hundred-step figure from the first full-size run | section 9 (line 2274); section 11, step 5a; weakness W8; entry 17 | yes |
| Decision 19: the position sets are the rehearsal's four | section 7.2, item 2 (lines 1451 to 1452); entry 19 | yes |
| Page 11, items 1 and 2: no verdict on the entangled model fires the two-model fallback; on the mixed model drops it | section 3 (lines 462 to 465); section 11, step 7 | yes |
| Page 11, item 3: the fifth registered term, "metric validated, degree not read", with its reason after a colon | section 3, the outcome table (line 313) and lines 340 to 342 | yes |
| Page 11, item 4: the roadmap's outcome list gains a dated note | section 3 (lines 301 to 304); the note exists | yes |
| Page 11, item 5: the fifth outcome is satisfactory and weaker than the first | the outcome table (line 313) | yes |
| Page 11, item 6: the stop after the first full-size run is unchanged | section 3 (lines 346 to 350); section 11, step 5a | yes |
| Page 15: the registration says what is true of the shutdown today; the repair comes off the Weekend 2 list; the caution is carried | weakness W9 (lines 2973 to 2982); entry 18 | yes |

### 1.2 The three rulings after the controls re-run (`docs/rulings/2026-10-03-controls-rerun-rulings.md`)

| Ruling | Where | Carried correctly? |
|---|---|---|
| 1, items 1 and 2: the other-agent control kept as a reported description; its pass line withdrawn | section 7.3, item 2 (lines 1775 to 1791); section 9 (line 2265) | yes |
| 1, item 3: the registration says it never ran at toy scale, why, and that no verdict is expected | lines 1792 to 1809 | yes |
| 1, item 4: its code run once with the floor off, labelled a test of the code | lines 1810 to 1830 | yes |
| 2, item 1: the too-early-position control's positions are those before both twins' first own turns | section 7.3, item 4 (lines 1871 to 1878) | yes |
| 2, item 2: it holds; its pass line is that nothing changes; the outputs themselves are compared; two shares reported | lines 1879 to 1889 | yes |
| 2, item 3: the "other routes" sentence withdrawn | lines 1902 to 1912 | yes |
| 2, items 4 and 5: reverses the morning's decision 16; run as a pre-stated quantity by another session; the diagnostic's figures not quoted as that run | lines 1913 to 1948; entry 16 | yes |
| 3: the piece's accuracy at the other positions of its site is a reported column, with no pass line, filled for the twelve toy models | section 7.2, item 3 (lines 1573 to 1644); section 7.5, column 3 | yes |

### 1.3 The evening ruling (`docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`)

| Ruling | Where | Carried correctly? |
|---|---|---|
| 1: the fifth outcome is satisfactory and stated as weaker than the first, in John's own words | the outcome table (line 313); entry 28 | yes |
| 2, items 1 and 2: the new figure printed both ways, neither with a pass line | section 7.2, item 3 (lines 1580 to 1583); section 7.5, column 3 | yes |
| 2, item 3, with its dated note: computed as section 4 of the short run's method states | lines 1585 to 1625 | yes; version 4 adds that the average is taken in 64-bit arithmetic and says that choice is its own |

### 1.4 The seven questions, as they stand after the reconciliation

"Record B only" marks something record B says and record A does not, outside
the four rows of the reconciliation's table. The reconciliation says both
records stand on everything else, so these are ruled too.

| Ruling | Where | Carried correctly? |
|---|---|---|
| 1: the floor is on the piece only; the whole read's count printed, not a second condition | section 6.4, item 2 (lines 1155 to 1168); section 7.2, item 1 (line 1317) | yes |
| 2: the piece rule is applied after the layers are chosen | section 7.2, item 3 (lines 1555 to 1562) | yes |
| 2, reconciled: the registration says in a sentence what that order can miss | lines 1562 to 1571 | yes there. **Partly** overall: the same order is stated without the sentence at line 2258 (section 9), line 3316 (section 15, entry 29) and line 4186 (section 20); section 7.4's list of what is frozen does not name it; section 9 has no row for it |
| 3: the laptop's processor; 32-bit states; the read fitted in 64-bit | section 7.2, item 1 (lines 1332 to 1336); section 9 (line 2260) | yes |
| 3, reconciled: the library versions pinned in a committed file named in the registration | lines 1338 to 1344; section 7.4 (line 2074); section 9 (line 2260); section 20 (lines 4187 to 4188) | **partly**: the ruling is stated correctly, but the two things cited beside it do not check out (findings 8 and 9) |
| 3, record B only: if the processor proves impractical at full size, that is a fresh question for John, not a switch | nowhere | **no**; and section 11, step 5a (lines 2520 to 2524) says the opposite (finding 5) |
| 4: the toy's episode counts at full size | section 7.4 (lines 2067 to 2071); section 8.1 (lines 2175 to 2176); section 9 (line 2276) | yes; the counts are the toy code's (finding 12) |
| 4, reconciled: the band that sampling alone puts around each count against the four-fifths floor is printed beside it | section 7.4 (lines 2072 to 2073); section 7.5, column 4; section 9 (line 2276) | yes |
| 4, record B only: a miss at the first full-size run goes to John with that band beside it | not in section 11, step 5a, nor in stop condition S4a (lines 2578 to 2583) | **partly**: the band is in the table row that run prints, but the two passages that say what goes to John do not name it |
| 5: the other-agent control is compared with twenty random pieces, reported as the neighbouring control reports them | section 7.3, item 2 (lines 1781 to 1785, 1831 to 1838); section 7.5, column 14 | yes |
| 5, record B only: the code is changed and the code test of 2026-10-03 is run once more on the changed code, before the registration review | lines 1834 to 1836 say the change is "owed with the registered measurement"; section 17 (lines 3866 to 3868) lists it with the code owed before step 4 | **no**: version 4 follows record A's timing (finding 4) |
| 6, part 1: a model is read if at least two of its three seeds read; the third reported | section 3 (lines 469 to 477); section 9 (line 2277) | yes |
| 6, part 2, reconciled: the separation is the lowest reading among the entangled model's seeds that read minus the highest among the separable model's; at least 0.5; seeds not paired by number | section 3 (lines 477 to 487); section 7.4 (lines 2074 to 2075); section 9 (lines 2256, 2277) | **partly**: stated correctly in those places, and stated the old way in four others (finding 1) |
| 6, what follows: "metric validated" and "degree read" defined; the free model reading on one seed only gives the fifth outcome with that figure as a description | section 3 (lines 481 to 486) | yes |
| 7: the competing solver's three committed models are put through the measurement before the registration review, method first, by another session, and checked | section 7.3, last paragraph (lines 1996 to 2017); section 8.1; section 10, item R-5; section 11, step 1 | yes |
| 7, record B only: the method states what "the model's own turn" and its twin pairing mean for a solver with no acting channel; a reading on any seed goes to John before anything else moves | nowhere | **no** |

### 1.5 The reconciliation (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`)

| Ruling | Where | Carried correctly? |
|---|---|---|
| Record B stands on the device point (pinned) | as 1.4 | partly, as above |
| Record B stands on the order of the piece rule (what it can miss) | as 1.4 | partly, as above |
| Record B stands on the episode counts (the band) | as 1.4 | yes |
| Record B stands on seeds that disagree (the separation) | as 1.4 | partly, as above |
| Version 4 carries a notice at its head naming the ruling | lines 47 to 58 | yes |
| Version 4 is edited at its header table, sections 3, 7.2, 7.4, 7.5, 9 and 20 | the header table (line 75) and sections 3, 7.2, 7.5: all four points where they apply. Section 7.4: three of the four (not the order of the piece rule). Section 9: three of the four (the same one missing). Section 20: one of the four (pinned only) | **partly** |

### 1.6 Finding 1 (MEASURED): four sentences still state the separation seed by seed

The command is `stale_search.sh` in the folder beside this file; its full
output is `stale_search.out.txt`. The lines that matter:

```
$ sh experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/stale_search.sh
...
413:separation, arm C minus arm T, is 1.0051, 0.9926 and 0.9974 and clears 0.5 on
478:separation is not compared seed by seed.** It is the lowest reading among arm
...
--- 'clear(s|ed) ... every seed' and the three per-seed figures given as the separation
2256:| Separation bar between arms T and C (R1 against R2) | **0.5**: the minimum gap ... **Reconciled 2026
2419:  0.873 to 0.885 on 2026-09-21, and cleared at 1.0051, 0.9926 and 0.9974 under
3814:- **The separation line** (0.5 on every seed): produced (failure 2's output).
```

Each was then read in place:

| Line | Section | What it says | Verdict |
|---|---|---|---|
| 412 to 414 | 3, "The toy outcome" | "the separation, arm C minus arm T, is 1.0051, 0.9926 and 0.9974 and clears 0.5 on every seed" | **old way.** Under the ruling the toy's separation is one number, 0.9926 |
| 2256 | 9, first row | the first half of the cell is the reconciled wording and gives 0.9926; the second half says "the toy cleared it on every seed, at 1.0051, 0.9926 and 0.9974" | **old way, in the same cell as the new** |
| 2418 to 2420 | 10, item R-10 | "cleared at 1.0051, 0.9926 and 0.9974 under the registered rules" | **old way** |
| 3814 | 17, candidate 7 | "The separation line (0.5 on every seed): produced" | **old way.** The command output it points to (lines 3545 and 3561) prints the per-seed field of the output file, which is fine as output; the sentence is what is stale |
| 4024 to 4025 | 19, question 6 | the bar "is written 'per seed'" | left as put, by design. But see finding 3 on section 19's heading |

The three figures are right as the entangled model's three readings. What is
stale is calling them three separations and saying the bar clears "on every
seed". Nothing else in the document states the separation the old way: every
other line the search prints for this point either states it the new way or
uses "separation" for something else (partial separation within a trial).
Reading the whole document found no old-way sentence that the search
patterns miss.

### 1.7 Finding 2 (MEASURED by the same search, then read): the other three points

- **Library versions.** No sentence in the body states "recorded" without
  "pinned". Line 1336 says "recorded" and the next sentence adds "also
  pinned". Section 19, question 3 (lines 3984 to 3988) has "recorded" alone,
  left as it was put.
- **Episode counts without the band.** Section 7.4 (lines 2067 to 2071)
  gives the counts and the next bullet gives the band. Section 9 (line 2276)
  has both. No stale sentence. Two passages that describe what goes to John
  at the stop after the first full-size run do not mention the band: section
  11, step 5a (lines 2502 to 2507) and stop condition S4a (lines 2578 to
  2583). Section 6.4, item 2, lists what is printed beside the count and does
  not list the band either.
- **The order of the piece rule without what it can miss.** Three places
  give the order alone: line 2258 (section 9, the fit-floor row, cited to
  record A's ruling 2), lines 3316 to 3317 (section 15, entry 29) and line
  4186 (section 20). Weakness W12, where the packet said the sentence would
  also go, does not carry it; record B does not require it there.

### 1.8 Finding 3 (MEASURED by reading): places that cite record A for something record B settled, or that predate the reconciliation

- Line 470 (section 3) cites record A's ruling 6 for the seeds rule. Fine
  for part 1; the reconciled part cites record B at line 485.
- Line 2260 (section 9, the device row) cites record A's ruling 3 for a cell
  that now includes "pinned", which record A's ruling 3 says the opposite of.
- Line 2276 (the episode-counts row) cites record A's ruling 4 for a cell
  that now includes the band, which record A does not have.
- Line 2277 (the seeds row) cites "the same file, ruling 6", which is record
  A, for a cell whose second half is record B's.
- Lines 3314 to 3321 (section 15, entry 29) list the seven rulings as record
  A has them and cite record A only.
- Line 3940 (the heading of section 19) says "each now ruled as suggested",
  and lines 3943 to 3944 say John ruled "taking the suggestion in each". On
  four of the seven the suggestion was not what was finally ruled. Section 19
  has no notice of the reconciliation.
- Section 20's entry for the seven questions (lines 4182 to 4195) carries one
  reconciled point of four.

### 1.9 Finding 4 (MEASURED by reading the two records side by side): the records differ on when the other-agent control's code is changed and tested

- **Record A**, ruling 5 and "What this changes": the change "is not quite
  the one registered", and it is listed as "code owed with the registered
  measurement".
- **Record B**, ruling 5 and "What this changes": "the code changes
  accordingly, and the code test of 2026-10-03 is run once more on the changed
  code", listed under "Before the registration review, at $0".

The reconciliation's table does not list this, and its text says the records
agree on question 5. Version 4 follows record A (lines 1834 to 1836; section
17, lines 3866 to 3868), and its header (lines 15 to 26) names three things
that stand in front of the registration review, of which this is not one.

Doing it record B's way satisfies both records. It is still a choice between
two things John agreed to, so it is question 1 at the end.

### 1.10 Does version 4 contradict itself?

**On the four reconciled points:** yes, on the separation (finding 1). Not on
the other three, where the old wording is absent or left as put.

**Elsewhere:**

- **Finding 5 (MEASURED by reading; the consequence ARGUED).** Section 7.2,
  item 1 (lines 1332 to 1333) says the registered accuracy "is computed on
  the laptop's processor, never its graphics chip". Section 11, step 5a
  (lines 2520 to 2524) says the fit is computed on the laptop and that "if
  that turns out not to be so, the cost goes into the first release's
  rehearsal line and is said", which is a move to a rented machine by the
  session's own decision. Record B's ruling 3 says that case "is a fresh
  question for John, not a switch". The sentence in section 11 is carried
  from version 3 and predates the ruling.
- **Finding 6 (MEASURED by counting).** Line 64 says "the first ten rows are
  new since version 3"; line 4197 says "the eight new ones first". The source
  table has ten rows above the first one carried from version 3.
- **Finding 7 (MEASURED by reading).** Counts of the day's rulings are stale
  in four places. Line 8: "John's three sets of rulings of 2026-10-03" (there
  are five, and the reconciliation). Line 3342: "the three rulings of
  2026-10-03 this version is built to", in a list that names neither record B
  nor its packet nor the reconciliation. Line 4056: "the three rulings of
  2026-10-03 were each given as agreement"; the reconciliation was given in
  John's own words. Lines 62 to 64, 75, 3373 to 3375 and 4183: record A is
  "filed with this version on pull request 83" and is the one source "not on
  the main line"; both are on the main line at `41b0bd3` through pull request
  85, which superseded 83 and 84.
- **A small one, carried from version 3 (MEASURED,
  `site_sets_and_arithmetic.out.txt`).** The whole successor is "about $194
  to $206" at line 2541 and "about $192 to $204" or "about $193 to $205" at
  line 2763. All three are correct sums of different things (which split of
  the two releases, and whether the mixed model's $1.94 development run is
  counted inside its $32 to $44). A reader meets three ranges for one
  quantity.

Nothing else was found. In particular the three controls that hold are the
same three everywhere they are listed (sections 6.4, 7.3, 7.4, 7.5 and
weakness W14), and the five outcome terms are the same wherever they appear.

---

## 2. Job 2: do version 4's numbers match the records they cite?

### 2.1 The toy figures (MEASURED)

The script reads the committed output files and prints each figure beside
what version 4 prints. It loads no model.

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/toy_figures.py
...
ALL MATCH
$ grep -c '^MATCH' .../toy_figures.out.txt
89
```

The full output, 317 lines, is `toy_figures.out.txt` beside the script. What
the 89 comparisons cover, with one sentence each on whether it matches:

- **Every reading.** The separable model reads 0.0000 on every seed, the
  entangled model 1.0051, 0.9926 and 0.9974, the mixed model 0.4886, 0.4860
  and 0.5449, and the freely trained model is marked "described only": all
  match. The number the arithmetic would have returned for the free model
  (1.0000, 1.0000, 1.0108) matches.
- **The separation.** The lowest of the entangled model's readings minus the
  highest of the separable model's is 0.9926: matches. The output file's own
  `separation` field holds the three per-seed figures.
- **The entangled model's table in section 5.2**, all three rows (site, size
  of piece, the two counts of 180, the three shares): match. The largest gap
  between the ownership-only share and the no-transplant rate is 0.0037,
  inside the "within 0.004" the text states.
- **Every count against the four-fifths floor of 144 of 180.** The free
  model's best piece at any layer, size or seed is 34: matches. Its whole
  read at the first layer is 32, 12 and 18: matches. Every chosen piece on
  the three built models is at or above 144, the lowest being 150: matches.
  Every chosen piece's whole read is 176 or more: matches.
- **The whole-state floor.** 0.4433 against 0.4280 on the free model's first
  seed, 9 episodes of 600: matches. It clears on fresh episodes on all
  twelve: matches. The smallest denominators, 0.4863 and 0.4263: match.
- **The controls.** The complement shares of control 1 on all four models;
  control 3's counts below, equal and above (20 above on the entangled
  model's first seed; 6, 1, 13; 6, 5, 9) and the mixed model's random medians
  of 0.015 to 0.019; control 6's 81 and 719 trials and its shares; control 7
  bit-identical at fifteen different places: all match. The old definition of
  control 4 was above the no-transplant rate by 0.065 to 0.10 on six models
  and by 0.005 or less on six: matches to the two decimals printed (the
  largest is 0.1013).
- **The rider and the true-slot reference.** The whole-state shares at the
  separable model's site on the other three models; the mixed model's
  true-slot reading of 0.4837, 0.4760 and 0.4920; the gaps of 0.0049, 0.0099
  and 0.0529 (the middle one is 0.00992 unrounded): all match.
- **The other-agent control on the one model that learned its condition.**
  The best whole read 137 and the best piece 139 of 180; the candidates at
  layers 1 and 3: match.
- **The entangled model's second seed.** The choice between layer 1 and
  layer 4 was 0.0533 against 0.0517 on development episodes, one episode of
  600: matches.
- **The short pre-stated run.** The redefined control 4 holds on all twelve
  with identical outputs and no action changed; 1 to 21 positions per pair,
  about 5 on average; the piece's counts away from the action position on the
  entangled model (139, 139, 33 and 113 on the average; 30 to 139 and 123)
  and on the mixed model (163, 174, 175 on the average; 144 reached at four,
  four and seven positions of ten; 34, 71 and 33 at the fourth token); the
  free model's one outlier of 145; the three figures from the code test
  labelled NOT A RESULT (0.0012, 0.0063, 0.0962, with a piece right on 92):
  all match.
- **The gate file.** The bar of 790 of 3,000; the named-other counts (994,
  781, 746 and 760, 751, 708); every range quoted for the four models and the
  two competing solvers; the channel-removal figures including the separable
  model's third seed at 0.2733: all match.

Looked up by hand and matching: 407 of 800 pairs is 0.5088 (the check of the
controls re-run, line 247); "about 26,700 values" (the same check, line 118);
the three figures that moved by one episode under a different order of
addition, and 92 and 24 in 64-bit (the check of the short run, finding 11);
the method and the output of the short run committed 2 minutes 39 seconds
apart (the two commits' author times, 18:22:10 and 18:24:49); 0.9975 for the
entangled model's second seed at layer 4 (the controls re-run's findings,
line 112).

### 2.2 The site list of section 18 (MEASURED)

The script builds every site set as a pair and applies the exclusions, a
different route from the row-by-row count in section 18, then parses the list
printed in version 4 and compares set for set.

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/site_sets_and_arithmetic.py
=== 1. The site-set rule, run
states | contiguous layer sets | full family | registered | x4 | narrower | x4 | stricter | x4
     5 |                    15 |          60 |         45 |  180 |       55 |  220 |       40 |  160
    13 |                    91 |         364 |        325 | 1300 |      351 | 1404 |      312 | 1248

=== 2. The list printed in section 18, parsed and compared set for set
registered model: printed list holds 325 site sets; the rule gives 325; in the list and not the rule: 0; in the rule and not the list: 0
toy model: printed list holds 45 site sets; the rule gives 45; in the list and not the rule: 0; in the rule and not the list: 0

=== 3. What the toy code asserts
   rerun_controls.py: assert len(FAMILY) == 45 and len(FAMILY) * len(RANKS) == 180 and len(STRICT) == 40
```

All eight counts in section 7.2, item 2, and the printed list match the rule.

### 2.3 Thresholds (MEASURED, the same script)

```
=== 4. Thresholds
gate bar: smallest count with a one-sided tail at or under 0.05 at one in four, of 3,000: 790 (share 0.2633, tail 0.0485)
four fifths of 180: 144 | one episode of 180: 0.0056
no-transplant formula at own-directed 0.2633: 0.1052; a broken pairing (0.1250) misses by 0.0198; margin over 0.018: 0.0018
no-transplant formula at own-directed 0.56: 0.0629; a broken pairing (0.1250) misses by 0.0621; margin over 0.018: 0.0441
graphics-chip fits as shares of 180: 31, 12, 19 -> [0.172, 0.067, 0.106]
407 of 800 = 0.50875 | 483 of 800 = 0.60375 | 1810 of 3000 = 0.6033
```

Each matches what version 4 prints.

### 2.4 Dollars (MEASURED)

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/ledger_lookup.py
the last row of the run table is line 95 dated 2026-09-25
FOUND   | 228.15       | spent across the programme | line 95
FOUND   | 46.75        | Amendment A3 against its $100 stop | line 95
FOUND   | 9.43         | rehearsal line left, of $10 | line 95
FOUND   | 0.0525       | second attempt cost | line 95
FOUND   | 75.8645      | vendor balance on 2026-09-26T01:54Z | line 95
FOUND   | 0.4974       | first attempt cost | line 94
FOUND   | 0.02         | the 2026-09-21 slice row | line 93
FOUND   | 8.47         | 2026-08-08 anomaly, billed and existed hours | line 93
FOUND   | 2.42         | 2026-08-08 anomaly, billed and existed hours | line 93
FOUND   | 8.47         | the same, in the note | line 423
FOUND   | 2.42         | the same, in the note | line 423
FOUND   | 20.28        | two-run pod-hours and rate | line 88
FOUND   | 0.99         | two-run pod-hours and rate | line 88
FOUND   | 1.943        | 10-million run trued up | lines 393 and 400
FOUND   | 450          | ceiling raised to $450 on 2026-09-25 | the top of the file
...
nothing missing
```

Every figure section 12 cites to a ledger line is on that line. The thirteen
figures cited to the note that recomputed the second release are in its
committed output. The ledger has no row after line 95, as section 12.1 says.
The arithmetic (section 5 of `site_sets_and_arithmetic.out.txt`): $221.85 of
headroom, $0.57 spent on the rehearsal, $7.77 for four development runs,
$10.04 a run, $163.06 on the ruled split, $422.05 and $434.05 after the
successor, $14.79 and $17.03 left at the two ends the wager names: all as
printed. The eight runs come to $84.04 from the rounded per-run figures and
$84.06 in the note, which works from unrounded ratios; version 4 quotes the
note.

### 2.5 The repository's two checkers (MEASURED)

The headline lines of each; the full outputs are beside the scripts.

```
$ .venv/bin/python scripts/check_citations.py --only docs/successor-experiment-proposal-2026-10-03-v4.md
[CONFIDENT] 0 reference(s) name a file that is not in the repository
[LOOK AT IT] 8 bare name(s) match more than one file
[LOOK AT IT] 1 name(s) of run-output files that are not in the repository
  docs/successor-experiment-proposal-2026-10-03-v4.md:1320  .venv-lock-2026-08-28.txt
[LOOK AT IT] 12 reference(s) written with a gap or a wildcard that matched nothing
[NOT CHECKED] 1 reference(s) to files outside this repository
[CONFIDENT] 1 exact figure(s) absent from the one file their sentence cites
  docs/successor-experiment-proposal-2026-10-03-v4.md:850
      figure: 1,810    cited: out-repairs/gate_base.json
[LOOK AT IT] 16 figure(s) worth a human eye
Confident findings: 1. Things for a human to look at: 37.

$ .venv/bin/python scripts/check_single_source.py --only docs/successor-experiment-proposal-2026-10-03-v4.md
[CONFIDENT] Group 1: a dollar figure the ledger does not contain
0 found.
[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source
2 found.
  docs/successor-experiment-proposal-2026-10-03-v4.md:2645   $44
  docs/successor-experiment-proposal-2026-10-03-v4.md:2645   $131
[LOOK AT IT] Group 3: in the ledger, and no source named
3 found.
Confident findings: 2.
```

Both exit with status 1, which is what they do when anything confident is
found. Full outputs are beside the scripts. What each confident finding is:

- **The 1,810** (line 850 of version 4 as the checker counts paragraphs; the
  sentence is at lines 858 to 860). The file holds the share, 0.6033, in the
  field the sentence names, and 0.6033 of 3,000 is 1,810. The count is right
  and is arithmetic on the cited field. Version 4's section 17 says the same.
- **The $44 and $131** are cited to the ruling that set them, which is their
  source. Version 4's section 17 says the same.
- The 16 figures "worth a human eye" are four-decimal roundings of values
  the cited files hold at full length; this session's script compared those
  same values and they match.
- **The one new thing the checker shows is the lock file**, which leads to
  finding 9.

These results agree with what version 4's section 17 prints for the same two
commands.

### 2.6 Finding 8 (MEASURED): the output file records one library version, not three

Version 4, lines 1336 to 1338: "the versions of torch, scikit-learn and numpy
are recorded in the output file, as the controls re-run did (torch 2.12.1,
scikit-learn 1.9.0, numpy 2.5.0, `out-controls-rerun/summary.json`)".

```
=== 12. What summary.json records about the software (section 7.2 item 1)
    top-level fields of summary.json other than arms and separation: {'device': 'cpu', 'seconds': 967.1754839420319, 'torch': '2.12.1'}

$ grep -rn -i 'scikit\|sklearn\|numpy' experiments/rehearsal-successor-measure/out-controls-rerun/summary.json experiments/rehearsal-successor-measure/out-controls-rerun/table.md experiments/rehearsal-successor-measure/out-short-prestated-run/*.json experiments/rehearsal-successor-measure/out-short-prestated-run/stdout.txt
(no output)
```

The three version numbers are true: they are what the project's environment
holds today, and the findings of the controls re-run state them in prose
(`docs/2026-10-03-controls-rerun.md`, line 64). But the output file records
torch only. So "as the controls re-run did" is right for one library of
three, and the registered code has to write the other two for the sentence to
be true of the registered run.

### 2.7 Finding 9 (MEASURED): the file given as the model for pinning is not committed

Version 4 (line 1340), the packet (page 3) and record B (ruling 3) all say
the versions are pinned in a committed file "in the way
`.venv-lock-2026-08-28.txt` does for the project's environment".

```
$ git ls-files | grep -i -E 'lock|requirements'      (no line for .venv-lock-2026-08-28.txt)
$ git check-ignore -v .venv-lock-2026-08-28.txt
.gitignore:35:.venv-lock-*.txt	.venv-lock-2026-08-28.txt
$ git log --oneline --all -- .venv-lock-2026-08-28.txt
f222c94 WIP snapshot 2026-08-29: uncommitted working files (repo census)
$ git merge-base --is-ancestor f222c94 HEAD && echo "on main line" || echo "not an ancestor of the main line"
not an ancestor of the main line
```

The file exists in John's main checkout and lists the right versions
(`torch==2.12.1`, `scikit_learn==1.9.0`, `numpy==2.5.0`). It is not on the
main line: line 35 of `.gitignore` keeps every file of that name out, and
the one commit that holds it is a work-in-progress snapshot on a side branch.
So the example of "a committed file" is a file the record does not hold.

This does not touch the ruling, which is that the versions are pinned in a
committed file named in the registration. It means the registration cannot
point at that file as it stands, and a file named the same way would be
ignored again. **ARGUED, one more thing for whoever writes the pin file:**
scikit-learn's logistic regression does its fitting through scipy, so scipy's
version can move a fit as much as the three named libraries can. The lock
file lists it (`scipy==1.18.0`); the sentence in version 4 does not.

### 2.8 Finding 10 (MEASURED): section 17's printed sweep output no longer matches the file

Section 17 prints the output of text searches run on sections 0 to 16. Run
again on the file as it stands:

```
$ sh experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-scripts/section17_sweeps.sh
--- failure 2, part one (section 17 prints lines 1256, 1257, 1258, 1262)
1277: ...   1278: ...   1279: ...   1283: ...
--- failure 4, part one (section 17 prints 759, 233, 68, 14, 3406, 8)
761
235
68
14
    3449
8
```

The text grew by 43 lines after the sweeps were run (the seven rulings and
the reconciliation were written in), so four of the printed numbers and the
four line numbers are out of date. The conclusions drawn from them do not
change. Every other command block in section 17 reads the committed output
files, and this session's own script found the same values.

---

## 3. Job 3: the packet, the two records and the reconciliation

### 3.1 The packet (`docs/rulings/2026-10-03-version-4-questions-PROPOSAL.md`)

Every number, against the place it cites:

| Page | What it states | Matches? |
|---|---|---|
| 1 | On the one model where the named agent's read was tried, the 8-direction piece was right on 139 of 180 and the whole read on 137; both readings give the same twelve verdicts | yes (MEASURED: `toy_figures.out.txt`, sections 4 and 8) |
| 2 | Candidates at layers 1 and 3, best pieces 92 and 115; layer 2, not a candidate, best piece 139; none reached 144 | yes (MEASURED: the same output, section 8) |
| 2 | "about $44" for the first release | yes (section 12.3 of version 4) |
| 3 | Two reads moved by one held-out episode between the processor and the graphics chip; every toy figure since the controls re-run was computed on the processor | yes (32 against 31 and 18 against 19; `device: cpu` in both runs' output files) |
| 3 | `.venv-lock-2026-08-28.txt` "already does" this "for the project's environment" | **partly**: the file exists and lists the versions; it is not a committed file (finding 9) |
| 4 | The toy's counts: 600 development episodes, the last 180 held out; 800 fresh pairs; 800 on the relaxed set; 3,000 for the gates; 200 shuffles | yes (finding 12 below) |
| 4 | With 180 held out the floor is 144; one episode is 0.0056; a piece at exactly four fifths lands "within about three points either way (roughly 139 to 149) on most draws" and passes "about half the time"; three times as many episodes narrows the band "to under two points" | yes, as arithmetic (finding 11 below) |
| 5 | The code draws one random piece; the neighbouring control draws twenty | yes (`N_RANDOM = 20` in the toy code; the check of the controls re-run, section 4, item 4) |
| 6 | The entangled model reads 1.0051, 0.9926 and 0.9974; the separable model 0.0000 on every seed; the proposed separation is 0.9926 | **yes** (MEASURED: `toy_figures.out.txt`, section 2) |
| 6 | "Amends: the ruling of 2026-09-25 that set the separation bar 'per seed'" | **no.** Page 1a of that ruling does not say "per seed"; the words were added by the proposal (version 3, section 9, line 1628). Record B says this correctly and the packet does not |
| 7 | The three ownership-blind models are committed with fingerprints | yes (three files; three lines in `SHA256SUMS`) |

**Finding 11 (MEASURED: `site_sets_and_arithmetic.out.txt`, section 4).** The
sampling arithmetic of page 4:

```
sampling spread of a count of 180 at a true share of 0.8: one standard deviation 5.37 episodes (0.0298); two 10.7 episodes (0.060)
a piece whose true accuracy is exactly 0.8 reaches 144 of 180 with probability 0.544; lands in 139 to 149 with probability 0.695
at three times as many held-out episodes (540): one standard deviation 0.0172
   a piece whose true accuracy is 0.78 reaches 144 of 180 with probability 0.293
   a piece whose true accuracy is 0.82 reaches 144 of 180 with probability 0.789
```

"About three points either way on most draws" is one standard deviation and
holds on about seven draws in ten. "About half the time" is 0.54. "Under two
points" is 0.017. All fair. **One sentence is stronger than its arithmetic
(ARGUED):** "at 180 the floor cannot tell 0.78 from 0.82". A piece at 0.78
passes about three times in ten and a piece at 0.82 about eight times in ten.
The floor tells them apart poorly, which is the point being made; "cannot
tell" overstates it. Nothing ruled rests on that sentence.

**Finding 12 (MEASURED).** The counts are the toy code's:

```
rerun_controls.py:45:HELD_OUT, PIECE_MIN = 180, 144                   # rule 7: four fifths of 180
rerun_controls.py:269:    dev_pairs, _ = T.make_data(600, seed=4242, pool="dev", device=DEVICE)
rerun_controls.py:270:    fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=DEVICE)
rerun_controls.py:271:    coll_pairs, _ = T.make_data(800, seed=778, pool="fresh", device=DEVICE, collide=True)
repairs.py:50:GATE_EPISODES = 3000
rerun_v3.py:69:N_PERM = 200
```

**Does each page state its options fairly?** (ARGUED throughout.)

- **Pages 1, 5 and 7:** yes. Each gives the alternative its real cost and
  its real merit.
- **Page 2:** yes. It gives the case against its own recommendation in
  figures, and the toy instance it quotes is one where the order made no
  difference, which it says.
- **Page 3:** mostly. The choice version 4 had left open, pin or only
  record, is given as part of the recommendation and not as two options with
  a case for each. The case for recording only is not stated. It is a small
  point and the recommendation is the more careful of the two.
- **Page 4:** yes, and it is candid that the alternative "is the better
  instrument".
- **Page 6:** yes on part 1. On part 2 see below.

**Page 6, part 2: does the reasoning hold?** (ARGUED, with the arithmetic
MEASURED.) The proposal is that the separation be the lowest reading among
the entangled model's seeds that read, minus the highest among the separable
model's. Three claims are made for it.

1. *"Seed 0 of one model has no relation to seed 0 of another."* **Holds,
   with one qualification.** The two are separate trainings of different
   architectures; nothing about the trained models is matched by the shared
   number. The qualification: a shared seed number may mean the two trainings
   drew the same stream of training episodes, so "no relation" is slightly
   too strong. It does not rescue the pairing, because nothing in the measure
   uses that.
2. *"With two seeds reading on one model and three on the other, the pairing
   is not even defined."* **Holds.** This is the stronger argument: once
   part 1 allows a model to read on two seeds, a rule paired by number has
   nothing to say when the missing seeds differ.
3. *"It is the stricter of the two ways."* **Holds.** Whatever the pairing,
   each paired gap is at least the lowest of one minus the highest of the
   other. So if the proposed separation clears 0.5, every paired gap does.

And the 0.9926 is right.

**One consequence the packet does not state (ARGUED), which John may want to
know he has ruled.** Part 1 forgives one seed of three that returns no
verdict. Part 2 does not forgive one seed that returns a reading and reads
oddly. If one seed of the entangled model read 0.3 and the other two read
near 1, the separation would be 0.3 and the outcome would be "metric does not
separate". If that same seed had returned no verdict, it would be set aside
and the metric would be validated on the other two. So a bad seed that fails
its floor costs nothing and a bad seed that passes its floor can decide the
outcome. That is defensible: a built model that reads low is evidence against
the measure and a model that returns nothing is not. But it is a real
property of the rule, it is new, and nothing has rehearsed it. It is question
2 at the end, with the suggestion that it stand and be said.

### 3.2 Record B against the packet: no more and no less?

Ruling by ruling, record B records what the packet's page recommended, in the
packet's terms, with these exceptions:

- **One thing more.** Ruling 7 ends: "a reading on any seed goes to John
  before anything else moves". The packet's page 7 says that if the result is
  not a no verdict "something is wrong with the measure and it is far better
  to learn it now". It does not put a stop to John. The record's sentence is
  a reasonable reading of that, and it is the record's.
- **One correction.** The packet's page 6 says page 1a of the earlier ruling
  set the bar "per seed". Record B's ruling 6 says page 1a "did not say how
  the gap is taken across seeds; the proposal's 'per seed' was the
  proposal's". The record is right and the packet was wrong (the table
  above). The record says less than the packet here, correctly.
- **Nothing less** otherwise. The clause in ruling 3 about the processor
  proving impractical is in the packet, in the paragraph on the strongest
  alternative. The clause in ruling 4 about a miss going to John with the
  band is in the packet's recommendation.

Record B's caution 3 says plainly that part 2 of ruling 6 was that session's
own proposal and is in no earlier document. That is accurate.

### 3.3 The reconciliation's table of four differences

| Row | Record A, as the table gives it | Record B, as the table gives it | Matches the two records? |
|---|---|---|---|
| Question 3, the device | recorded and not pinned | pinned in a committed file named in the registration | yes (A, ruling 3, item 3; B, ruling 3) |
| Question 2, the order of the piece rule | confirmed as run | confirmed as run, and the registration says what it can miss | yes |
| Question 4, the episode counts | the toy's counts | the toy's counts, and the band printed at the floor | yes |
| Question 6, seeds that disagree | two of three; the separation "cleared if cleared on two or more seeds", compared seed by seed | two of three; the lowest minus the highest, not paired by number; what "metric validated" and "degree read" mean | yes in substance. The words the table puts in quotation marks for record A are a paraphrase: record A says the bar "is cleared if the entangled model's reading minus the separable model's is 0.5 or more on at least two of the three seeds, compared seed by seed as before" |

**Do the two records differ anywhere the table does not list? Yes, in six
places** (MEASURED by reading the two side by side). The reconciliation says
the records "agree on questions 1, 5 and 7" and that "on everything else the
two records say the same thing and both stand".

| Question | Record A | Record B | Kind of difference |
|---|---|---|---|
| 5 | the code change is "owed with the registered measurement" | the code is changed and its test run once more "before the registration review" | **substance: when** (finding 4) |
| 7 | nothing on either point | the method states what "the model's own turn" and its twin pairing mean for a solver with no acting channel; a reading on any seed goes to John before anything else moves | B says more |
| 3 | nothing on the point | if the processor proves impractical at full size, that is a fresh question for John, not a switch | B says more |
| 4 | "at 180, one episode is 0.0056" | the same, and that a piece at exactly four fifths passes about half the time, and that a miss at the first full-size run goes to John with the band beside it | B says more |
| 6 | a model "returns no verdict, as an arm, if two or more of its seeds return no verdict"; "every seed is printed" | if the free model reads on one seed only, the outcome is the fifth term and that seed's figure is printed as a description | each says something the other does not; they agree |
| 1 | "Nothing here edits ... any earlier ruling file" | the earlier ruling on the floor gains a dated note | a difference in what each record did, not in what was ruled |

None of these is a contradiction that needs undoing: where record B says
more, it stands by the reconciliation's own rule that both stand, and nothing
in record A forbids it. The one that changes what happens and when is
question 5. **The practical cost of the table's four rows being taken as the
whole list is section 1.4 above: version 4 was edited at the four listed
points and still follows record A on the unlisted ones.**

### 3.4 The dated notes

| Note | Where | Accurate? |
|---|---|---|
| Beside item 1 of the ruling on finding RT-212 (the floor was on the whole read; now on the piece, and the whole read is not a second condition) | `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`, lines 46 to 52 | yes; it cites the morning's page 1 and record B's ruling 1, and leaves item 1 as written |
| Beside the phrase "a five-layer model" (four blocks and five states against twelve and thirteen) | the same file, lines 346 to 351 | yes |
| Beside page 1a (the separation bar does not say how the gap is taken across seeds; now the lowest minus the highest, not paired) | `docs/rulings/2026-09-26-weekend-1-queue.md`, lines 37 to 42 | yes. It is right that page 1a is silent on seeds. It leaves out "among the seeds that read" for the separable model, which the ruling has for both; a reader would not be misled |
| At the head of record A (a second record exists; the four points; record B stands) | lines 15 to 26 | yes; its one-line summary of each of the four points is right |
| At the head of record B | lines 16 to 22 | yes |
| Under the roadmap's outcome table, two notes (the fifth term; then John's own words) | `docs/december-result-roadmap-2026-09-20.md`, lines 87 to 98 | yes |

Each note is dated, says the text beside it is left as written, and points
at the ruling. None rewrites the sentence it sits beside.

---

## 4. What needs changing in version 4, by section and line

For the session that writes the registration text, in document order. None
changes a number or a rule.

| # | Where (lines at `41b0bd3`) | Change | From |
|---|---|---|---|
| 1 | Header, line 8 | "John's three sets of rulings of 2026-10-03" becomes five sets and the reconciliation | finding 7 |
| 2 | Header, lines 15 to 26 | Add to what stands in front of the registration review: the other-agent control's changed code and its repeated code test, if question 1 is ruled as suggested | finding 4 |
| 3 | Lines 28 to 35, 62 to 64; source table, line 75; section 16, lines 3373 to 3375; section 20, line 4183 | Record A is on the main line at `41b0bd3` (pull request 85, which superseded 83 and 84). Give record B, its packet and the reconciliation their own rows in the source table and their own entries in section 16 | finding 7 |
| 4 | Section 3, lines 412 to 414 | The toy's separation is 0.9926, the lowest of the entangled model's readings minus the highest of the separable model's; drop "clears 0.5 on every seed" | finding 1 |
| 5 | Section 3, line 470 | Cite record B and the reconciliation beside record A for the seeds rule | finding 3 |
| 6 | Section 6.4, item 2, lines 1152 to 1154 | Add the sampling band to what is printed beside the piece's count | section 1.7 |
| 7 | Section 7.2, item 1, lines 1336 to 1338 | The output file of the controls re-run records torch only. Say the registered code writes all the pinned versions to its output file, and cite the re-run's findings for the three version numbers | finding 8 |
| 8 | Section 7.2, item 1, lines 1339 to 1341 | Drop "in the way `.venv-lock-2026-08-28.txt` does", or say that file is not committed. Name the file the registration will commit, in a place the ignore list does not catch, and include scipy | finding 9 |
| 9 | Section 7.2, item 1, after line 1347 | Add record B's clause: if the processor proves impractical at full size, that is a fresh question for John, not a switch | section 1.4 |
| 10 | Section 7.3, item 2, lines 1831 to 1838 | Per question 1: the code is changed and its code test run once more, labelled as before, before the registration review; then quote that test | finding 4 |
| 11 | Section 7.3, last paragraph, lines 1996 to 2017 | Add record B's two clauses: the method states what "the model's own turn" and its twin pairing mean for the solver; a reading on any seed goes to John before anything else moves. Then write the run's result in | section 1.4 |
| 12 | Section 7.4, lines 2072 to 2076 | Add the fourth reconciled point to the frozen list: the order of the piece rule, with the sentence on what it can miss | section 1.5 |
| 13 | Section 9, line 2256 | Remove the second half of the cell ("cleared it on every seed, at 1.0051, 0.9926 and 0.9974"), or reword it as the entangled model's three readings | finding 1 |
| 14 | Section 9, line 2258 | Cite record B's ruling 2 and add that the registration says what the order can miss | section 1.7 |
| 15 | Section 9, lines 2260, 2276 and 2277 | Cite record B and the reconciliation for "pinned", for the band and for the separation; "the same file" at line 2277 points at record A | finding 3 |
| 16 | Section 10, item R-10, lines 2418 to 2420 | "a separation of 0.9926 under the registered rules" | finding 1 |
| 17 | Section 10, "What happens next", and section 11, step 1, lines 2475 to 2478 | Add the other-agent control's code test to what is owed before step 2, per question 1 | finding 4 |
| 18 | Section 11, step 5a, lines 2502 to 2507 | Add: the count is reported with the sampling band beside it | section 1.4 |
| 19 | Section 11, step 5a, lines 2520 to 2524 | Replace "if that turns out not to be so, the cost goes into the first release's rehearsal line and is said" with record B's rule: a fresh question for John | finding 5 |
| 20 | Section 11, stop condition S4a, lines 2578 to 2583 | Add the sampling band to what is reported to John | section 1.4 |
| 21 | Section 11, line 2541, or section 12.4, line 2763 | One range for the whole successor, or a clause saying why they differ | section 1.10 |
| 22 | Section 13, weakness W12 | Optional: a sentence that the order of the piece rule can cost a reading (the packet said it would go here; record B does not require it) | section 1.7 |
| 23 | Section 15, intro and entry 29, lines 3082 to 3084, 3314 to 3321 | Entry 29 cites record A only and lists the seven as record A has them. Add record B, the reconciliation and the four points | finding 3 |
| 24 | Section 16, line 3342 | "The three rulings of 2026-10-03" becomes the full list | finding 7 |
| 25 | Section 17, lines 3522 to 3525 and 3700 to 3709 | Run the text sweeps again and print the current output | finding 10 |
| 26 | Section 17, line 3814 | "The separation line (the lowest reading of the entangled model minus the highest of the separable model, at least 0.5): produced, at 0.9926" | finding 1 |
| 27 | Section 17, lines 3866 to 3868 | Move "control 2's twenty random pieces" out of the code owed before step 4, per question 1 | finding 4 |
| 28 | Section 19, heading (line 3940) and lines 3943 to 3948 | "each now ruled as suggested" is not true of four. Say that the body follows the reconciliation where the suggestion and the final ruling differ | finding 3 |
| 29 | Section 19, line 4056 | "the three rulings of 2026-10-03 were each given as agreement" becomes the five, with the reconciliation in John's own words | finding 7 |
| 30 | Section 20, lines 4182 to 4195 | Add the three reconciled points it does not carry; correct "the eight new ones" at line 4197 to ten | section 1.5; finding 6 |

Two things outside version 4, noted and not acted on:

- **The reconciliation ruling says** the two records "agree on questions 1, 5
  and 7" and "say the same thing" on everything else. Section 3.3 shows six
  places they do not. A dated note beside that sentence would stop the next
  reader taking the table of four as the whole list. This session did not
  add one: ruling files are not its to edit.
- **`.gitignore`, line 35**, keeps any file named `.venv-lock-*.txt` out of
  the repository. Whoever commits the pin file needs a different name or a
  different place.

---

## 5. What this check did not do

- It did not run the controls re-run or the short pre-stated run again. Both
  were re-run from code by their own checks. This check compared version 4's
  figures with the committed outputs of those runs.
- It did not recompute any figure that version 4 quotes from records older
  than 2026-10-03 other than those in the gate file: the label search's fits,
  the grammar attempt's counts, the rented slice's timings and the
  permutation baseline were not re-derived. Each was checked when it was
  filed, and version 4 carries them from version 3 unchanged.
- It did not check sections that version 4 says are carried from version 3
  word for word against version 3, sentence by sentence. It read them for
  contradiction with the rulings of 2026-10-03 and found one (finding 5).
- It did not judge the design. That is the registration review's job.
- "Yes" in section 1 means the ruling is stated where it bears and stated
  correctly. It does not mean every sentence of the passage was re-derived.

---

## 6. Questions that need John's ruling, each with a suggestion

Listed here and not put to him in this session's chat, as the brief asks.

1. **When is the other-agent control's code changed to twenty random pieces
   and its code test run again: before the registration review (record B),
   or with the registered measurement (record A)?** John agreed to both, and
   the reconciliation did not list the difference. *Suggestion: before the
   registration review, as record B has it.* It is a few minutes on the
   laptop at $0, it satisfies both records, and it means the registration
   review is not looking at a control whose registered code path has never
   run. Confidence: high. The alternative: leave it with the registered
   code, and say in the registration that the path with twenty draws has not
   run.

2. **The separation rule forgives a seed that returns no verdict and does
   not forgive a seed that reads oddly (section 3.1). Is that what John
   meant?** *Suggestion: yes, leave the rule as ruled, and have the
   registration say it in a sentence.* A built model that returns a low
   reading is evidence against the measure in a way that a model returning
   nothing is not, and the rule is the stricter one, which is the safer
   direction for a claim of "metric validated". Confidence: moderate. The
   alternative: the middle reading of each model's three, which tolerates one
   odd seed on each side and is less strict.

Not a question, but for John to know: the six unlisted differences between
the two records (section 3.3). On five of them record B simply says more and
nothing is in conflict; this check treats those as ruled, by the
reconciliation's own sentence that both records stand.

---

## 7. Scripts and outputs beside this file

In `reviews/2026-10-03-proposal-v4-check-scripts/`, each run from the root of
the checkout with the project's own Python (which lives in the main checkout
and was run by its full path from this worktree):

| Script | What it does | Output |
|---|---|---|
| `toy_figures.py` | recomputes 89 toy figures from the committed output files and prints each beside version 4's | `toy_figures.out.txt` |
| `stale_search.sh` | lists every line of version 4 that touches one of the four reconciled points | `stale_search.out.txt` |
| `site_sets_and_arithmetic.py` | runs the site-set rule and compares it with section 18's printed list; redoes the threshold, sampling and money arithmetic | `site_sets_and_arithmetic.out.txt` |
| `ledger_lookup.py` | looks up each dollar figure in the ledger line version 4 names | `ledger_lookup.out.txt` |
| `section17_sweeps.sh` | runs section 17's text sweeps again on the file as it stands | `section17_sweeps.out.txt` |
| (the repository's own) `scripts/check_citations.py`, `scripts/check_single_source.py` | run on version 4 | `check_citations.out.txt`, `check_single_source.out.txt` |
===== END OF RECORD 14 =====

===== RECORD 15 of 25 - the check of the competing-solver run and the twenty-piece control - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md` (complete file, 42,479 characters) =====
# Check of the competing-solver run (pull request 88) and of the other-agent control against twenty random pieces (pull request 89)

*Written 2026-10-03 (Pacific), late evening, by a Claude Code checking
session ("MVM W2d check of the competing-solver run and the twenty-piece
control"), on branch `w2d-check-competing-solver-and-control-2`, cut from the
main line at `7a55fe0`. The file carries the date 2026-10-04 because the
brief named it so. Laptop, processor only. Nothing rented, nothing trained
beyond the small straight-line reads the checked code itself fits, nothing
launched, nothing spent: $0.*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (this session ran something, or read it off a committed file or
off GitHub's own record, and says which) or **ARGUED** (a judgement, with its
reasons). This is a check of two rehearsal records on toy models. It is not a
result about the scientific question.*

**The pairing rule.** This session wrote neither pull request. Both were
written and run by one other session. This check is the one ruling 7
(`docs/rulings/2026-10-03-version-4-questions-rulings.md`) requires before
the registration review, and the one the control's findings say is owed.

## What this session opened

- **Pull request 88**, branch `w2b-job1-competing-solver-run` (commits
  `744a8b3`, `3fee39f`, `3d55865`): its method
  (`docs/2026-10-03-competing-solver-run-method.md`), findings
  (`docs/2026-10-03-competing-solver-run.md`), code
  (`experiments/rehearsal-successor-measure/src/competing_solver_run.py`),
  every output under `out-competing-solver-run/`, and its description on
  GitHub.
- **Pull request 89**, branch `w2b-job2-control-2-twenty-draws` (commits
  `174081e`, `c148bf1`): its method
  (`docs/2026-10-03-control-2-twenty-draws-method.md`), findings
  (`docs/2026-10-03-control-2-twenty-draws.md`), code
  (`src/control2_twenty_draws.py`), every output under
  `out-control-2-twenty-draws/`, and its description on GitHub.
- The rulings the two cite: the seven-question ruling, record B
  (`docs/rulings/2026-10-03-version-4-questions-rulings.md`, rulings 4, 5 and
  7), the ruling that record B stands
  (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`), and the
  ruling on the two questions from the check of version 4
  (`docs/rulings/2026-10-03-version-4-check-questions-rulings.md`, ruling 1).
- The committed code both runs import (`rerun_controls.py`, `rerun_v3.py`,
  `repairs.py`, `training.py`, `arms.py`), the committed gate file
  `out-repairs/gate_base.json`, the earlier code test's output
  `out-short-prestated-run/part_c_NOT_A_RESULT.json`, the model fingerprint
  list `out-repairs/models/SHA256SUMS`, and the environment lock
  `.venv-lock-2026-08-28.txt`.
- Version 4 of the proposal (`docs/successor-experiment-proposal-2026-10-03-v4.md`
  at `7a55fe0`): every passage that mentions the competing solver, the
  other-agent control, the whole-state floor's job, the no-transplant
  formula, or the sampling band, found by search and read in full with the
  surrounding section. Not read through end to end.
- GitHub's own record of when each branch was created and pushed.

**Not opened:** the transcript of any other session; the first record of
the seven-question ruling, beyond the line that version 4 cites it; any
ruling packet. Nothing was put to John in chat.

This session's scripts and their outputs are beside this file, in
`2026-10-04-competing-solver-and-control-2-check-scripts/`.

**A note on citations.** The files of pull requests 88 and 89 are cited
here by the paths they will have once those pull requests are merged. Until
then they exist only on those two branches, and the repository's citation
checker (`scripts/check_citations.py`), run on this file, lists the 14 such
references as missing for that reason. It finds no other missing file and no
figure absent from the file its sentence cites.

---

## 1. The result on one page

**Both pull requests hold. Every figure the brief named checks out. The
re-runs reproduce the committed outputs exactly. Neither needs a new run.**
What this check adds is a handful of wording fixes, one fault in how the
solver's findings explain *why* the solver gets no verdict, and two points
for the registration text that the runs' own findings did not reach.

- **Method before output, both pull requests (MEASURED, from git and
  GitHub).** Each method commit carries no output, comes before its output
  commit in the branch's history, and was pushed before it. The code file is
  byte-identical between each method commit and the branch tip.
- **Re-run from a clean checkout (MEASURED).** The control's three output
  files came back byte-identical; its printed output differs only in the
  running time (52 seconds against 50). Of the solver's 21 output files, 20
  came back byte-identical, including all six fitted reads, whose arrays are
  equal too; the twenty-first, `summary.json`, differs in one field only, the
  running time (930 seconds against 839). Its printed output is identical
  apart from the running time.
- **The figures (MEASURED, by an independent recount from the raw fields;
  all 69 checks pass).** No verdict on every seed under both readings of
  the solver. Best piece of the marker-word read 20 to 25 of 180 against 144.
  The gate on the processor at 702, 715 and 702 of 3,000 on the own-directed
  condition, equal field for field to the committed graphics-chip figures.
  The null transplant bit-identical at all 45 site sets everywhere. Seed 2
  with the channel left on clears the whole-state floor at 33 of 45 site
  sets on fresh episodes and none on development episodes. For the control:
  0.0012, 0.0063 and 0.0962 equal the earlier code test's to the last bit;
  the twenty pieces have a middle value of 0.0037, a 95th percentile of
  0.0052, and 0 below, 1 equal and 19 above.
- **Against the rulings (MEASURED from the code, then ARGUED).** The control
  does what ruling 5 says and nothing else. The solver run does what ruling 7
  asks. It does not do one thing version 4 requires of the registered code
  (withholding a reading in code when the no-transplant rule fails); here
  that changes nothing, because nothing was nominated.
- **One explanation in the solver's findings needs correcting (ARGUED, from
  version 4's text).** Its section 4, its question 2 and the pull-request
  description say the gate on learning is the first thing that "holds the
  solver back", because "in the registered experiment a model that fails the
  gate is not read at all". Version 4 gates the four arms, not the competing
  solvers: their accuracy is printed beside the gate as a reference (section
  8.1, and the gate row of section 9). The solver *would* fail the gate if it
  were gated as the free model is, but that is not what stopped it. What
  stopped it under the rules as written is the floor at nomination, and
  behind that the piece rule and the no-transplant rule.
- **Two points for the registration that neither run's findings reached
  (ARGUED).** (a) Version 4's rehearsal item R-6 credits the whole-state floor
  alone with keeping the formula's divisor away from zero. On this solver
  the floor was cleared on fresh episodes with a divisor of one or two
  episodes in 800. What keeps the divisor large on a real arm is the floor
  *together with* the gate and the no-transplant rule. (b) This solver fails
  the task. So the run shows the measure returns nothing on a model that has
  not learned the task; it does not show what the measure does on a model
  that solves the task by a route other than tracking whose turn it is.
- **Version 4 sentences.** The solver's findings name the right passages and
  miss five more; the control's findings name the right passages and miss
  the one that a later ruling made wrong (section 7.3, item 2, lines 1830 to
  1837). Section 6 lists them all, by line.
- **Questions for John.** Of the five, four suggestions follow from the
  evidence as written; one (the solver's question 2) needs rewording for the
  gate. This check adds two, each with a suggestion (section 9).

---

## 2. Job 1: method before output

**MEASURED, from git** (`git show --stat`, `git diff --name-status`,
`git rev-parse <commit>:<path>`) **and from GitHub's activity record for each
branch** (`gh api repos/jfredson/minimum-viable-mind/activity?ref=...`).

| | Pull request 88, the solver | Pull request 89, the control |
|---|---|---|
| Branch cut from | `41b0bd3` (the main line before pull requests 86 and 87) | `41b0bd3` |
| Method commit and what it carries | `744a8b3`: the method file and `competing_solver_run.py`. **No output file.** No file under `out-competing-solver-run/` exists in its tree | `174081e`: the method file and `control2_twenty_draws.py`. **No output file.** No file under `out-control-2-twenty-draws/` exists in its tree |
| Output commit, and its parent | `3fee39f`, parent `744a8b3`; then `3d55865`, parent `3fee39f` | `c148bf1`, parent `174081e` |
| What the output commits change | Only added files (the findings and 22 output files); `3d55865` changes two lines of the findings. Nothing already committed is modified | Only added files (the findings and 3 output files) |
| The code, method commit against branch tip | byte-identical (both blobs `af7cc95`) | byte-identical (both blobs `517aa17`) |
| Pushed to GitHub (Pacific) | method at 19:36:03 (the branch's creation); outputs at 19:52:02; wording fix at 19:52:35 | method at 19:52:49 (the branch's creation); outputs at 19:54:22 |

The solver's run took 839 seconds by its own printout, which fits in the 16
minutes between the two pushes. The control's took 50 seconds, which fits in
its 93. GitHub's record shows the method's push before the output's push in
both cases, which is what the pairing rule needs; it cannot show when on the
laptop each run started, and this check does not claim it does.

**One thing worth knowing, not a fault.** Both branches were cut before the
main line took in the check of version 4 (pull request 86) and John's ruling
on its two questions (pull request 87). So neither run could cite
`docs/rulings/2026-10-03-version-4-check-questions-rulings.md`. The control
satisfies its ruling 1 anyway (section 4 below). That ruling also says "The
competing-solver session ... already has this change in its plan. Its check
confirms the change was made": **confirmed** — the change is in pull request
89, not 88, and was made by the same session.

---

## 3. Job 2: the re-run from a clean checkout

**MEASURED.** Each branch tip was checked out in its own detached worktree
(`git worktree add --detach`), with nothing else in it, and the committed
code was run exactly as each findings file gives the command, with the
project's Python (`.venv/bin/python`; torch 2.12.1, scikit-learn 1.9.0,
numpy 2.5.0, the versions `.venv-lock-2026-08-28.txt` pins). The three
competing-solver model files matched `SHA256SUMS` before the run (`shasum -a
256 -c`). Then every output file was compared with the committed one by
`compare_rerun.py`: byte for byte for the JSON, the tables and the text, and
array by array for the `.npz` files (a zip archive can change its bytes while
its arrays stay the same).

**Pull request 89, the control.** 3 files compared, **0 differ**:
`code_test_NOT_A_RESULT.json`, `table.md`, and `stdout.txt` (which the run
does not write; it is unchanged). The printed output equals the committed
`stdout.txt` line for line except the last, "done in 52s" against "done in
50s". Running time: 52 seconds.

**Pull request 88, the solver.** 21 files compared, **1 differs, and only
in its running time**. All six `measure_*.json`, all six `nominate_*.json`
and `table.md` are byte-identical. All six `reads_*.npz` are array-equal
(largest difference 0.0) and byte-identical as well. `summary.json` differs
in one line of 394, the field `"seconds"`: 929.91 against 839.05. That is
how long the run took, not a result. The printed output equals the committed
`stdout.txt` line for line apart from the last line, "done in 930s" against
"done in 839s". Running time: 930 seconds. The committed models matched their
fingerprints before loading, and the run's own fingerprint check (stop B1)
passed.

Outputs, in the scripts folder: `rerun_compare_output.txt` (the comparison),
`rerun_solver_stdout.txt` and `rerun_control_stdout.txt` (what each re-run
printed). Neither run writes its own `stdout.txt`, so the comparison file's
`stdout.txt` lines compare the committed file with itself; the printed output
is compared separately, at the end of each section of that file.

---

## 4. Job 3: every figure, against the outputs

**MEASURED**, by `independent_check.py`, which reads the committed outputs
straight from git at the two branch tips and recounts each figure from the
raw fields rather than from the checked code's summaries: it recounts the
site sets that clear the floor from the whole-state accuracies and the
floor's formula; recomputes the sampling band from the textbook formula; and
recomputes the middle value and 95th percentile of the twenty by hand. Its
output is `independent_check_output.txt`. **Every check passes.**

### 4.1 The figures the brief named

| Figure | Claimed | Found |
|---|---|---|
| No verdict on every seed, both readings | yes | **yes**: all six runs "no verdict: no site set clears the whole-state floor", the stricter row the same; the summary's three stop lists empty |
| The marker-word read, best piece | 20 to 25 of 180 against 144 | **20 to 25** (best per seed 24, 23, 23 with the channel removed; 25, 20, 21 left on); 144 needed |
| The gate | 702, 715 and 702 of 3,000 | **702, 715, 702** own-directed and 712, 726, 650 named-other with the channel removed, **equal field for field to `out-repairs/gate_base.json`**; with the channel left on 707, 716, 698 and 710, 722, 653 |
| The null transplant | bit-identical | **bit-identical at all 45 site sets**, on all six runs |
| Seed 2, channel left on | clears the whole-state floor at 33 of 45 site sets on fresh episodes | **33**, and **0** on development episodes. The fresh floor asks for +0.0010, which is 0.8 of one episode in 800; the largest raise is +0.0025, two episodes |
| The control's unchanged figures | 0.0012, 0.0063, 0.0962, matching the earlier test | **equal to the earlier test's to the last bit** (0.0012499999720603228, 0.0062500000931322575, 0.09624999761581421), same site set |
| The twenty | middle 0.0037, 95th percentile 0.0052; 0 below, 1 equal, 19 above | **the same**, recomputed by hand. In episodes of 800, the twenty are 1, 2, 2, 3 (eight times), 4 (eight times) and 7; the real figure is 1 |

### 4.2 Every other figure in the two findings and the two descriptions

All hold. The ones worth a line:

- **The solver's tables 3.1** (the read at every layer and size, both
  readings): equal to the output files **cell for cell**.
- **The whole read 11 to 21; any count 9 to 25**: correct.
- **The sampling bands** in table 3.2 (for example 24 → 16 to 34): the
  Wilson interval at 95 percent, rounded; recomputed independently.
- **"Fails by 64 to 140 of 3,000"**: correct as the range over all twelve
  gate counts (726 is 64 short, 650 is 140 short). On the own-directed
  condition alone it is 74 to 92.
- **Section 4.1, "the floor asks for less than nothing" on seeds 0 and 1**:
  correct under both readings (with the channel removed, seed 0's accuracy
  0.2333 against an untouched rate of 0.2400; seed 1's 0.2100 against
  0.2300).
- **Section 4.2, development requirement +0.0053 and largest raise
  +0.0017** on seed 2 with the channel left on: correct.
- **Table 3.3, the no-transplant rates** (0.2487, 0.2300, 0.2200, 0.2500,
  0.2313, 0.2225 against 0.1107, 0.1116, 0.1109): correct; misses 0.109 to
  0.139, so "0.11 to 0.14" holds. **The wording fix at `3d55865` is right**:
  the earlier text said the rate was *outside its allowance* by 0.11 to
  0.14, when that is the miss against the formula; outside the allowance it
  is 0.09 to 0.12.
- **Table 5, the description-only arithmetic**: the counts of undefined and
  defined comparisons (180/0 three times; 32/148, 20/160, 20/160) and the
  smallest, middle and largest values: correct.
- **The twins' own-directed actions differ on 3 to 12 trials** with the
  channel left on: correct (6, 10, 3, 3, 10, 12).
- **The control's "the one old draw sits above 19 of the 20 and above their
  95th percentile"**: correct.

### 4.3 Two things this check measured that the findings assume

- **The solver's acting-channel vector really is untrained (MEASURED).**
  Rebuilding each model's starting weights from its training seed and
  comparing: the stored vector points in exactly the starting direction
  (cosine 1.0000 on all three seeds) and is 0.9631 times its starting length
  on all three. That shrinkage is the optimiser's weight decay, which acts on
  every weight whether or not it receives a training signal
  (`act_vec_check.py`, output `act_vec_check_output.txt`). So the method's
  "the vector ... was never used: no training step ever passed a signal
  through it" is exactly right, and "reading B" feeds the solver a fixed
  random nudge at its own turns, about 0.25 long.
- **The environment is the pinned one (MEASURED):** the versions both runs
  print equal those in `.venv-lock-2026-08-28.txt`.

### 4.4 Two places where the prose does not match the file it quotes

- **The control's findings, section 2, "What it printed".** The block is
  presented as the program's output but is a reformatted version of it. The
  program prints the site set as a Python dictionary on one line; the block
  writes it out in words and adds "(the floor would have asked for 144)",
  which the program does not print. The figures are the same. *Fix:* label
  the block "what it printed, laid out for reading", or paste
  `stdout.txt` verbatim.
- **The solver's findings, section 2**, shows the command and "..." then
  "done in 839s"; that matches `stdout.txt`. No fix needed.

---

## 5. Job 4: the method against the rulings it cites

### 5.1 Pull request 89 against ruling 5, and the check-questions ruling 1

Ruling 5 asks for: twenty random pieces of the same size at the same sites;
their middle value, 95th percentile, and where the real figure sits among
them; no pass line; the code test run once more on the changed code,
labelled a test of the code and not a result. The check-questions ruling 1
adds: done before the registration review. The brief adds: drawn as control 3
draws them.

**MEASURED, by reading the code and diffing it against the function it
replaces.**

- **Twenty, drawn as control 3 draws them.** `compare` calls
  `rerun_v3.random_bases(rank, layers, seed, ...)`, the same function, with
  the same arguments, that control 3 calls in `rerun_controls.measure_at`.
  The function seeds each draw from (20260926, model seed, draw number) and
  does not depend on the positions. So for a given model, size and layers
  these are control 3's twenty pieces. `assert V.N_RANDOM == 20` guards the
  count.
- **Same size, same sites.** Same rank as the nominated piece, at the same
  layers, applied with the same position mask and the same donor states.
- **Middle value, 95th percentile, below / equal / above.** `np.median`,
  `np.percentile(..., 95)` and three counts, exactly as control 3 computes
  them. The comparison is with the real figure (the named agent's piece),
  which is what ruling 5 asks.
- **No pass line.** The pass-or-fail field and the 0.05 tolerance
  (`C2_TOL`) are gone; the status is "reported; no pass line".
- **Nothing else changed.** The early exits (not applicable on arms T and M;
  no verdict below 790 on the named-other condition; the nomination by the
  identical procedure) are **copied line for line** from
  `rerun_controls.control2`: a diff shows only the docstring and one line's
  indentation differ. (The method says these are "imported"; the helper
  functions are imported, the twelve lines of early exits are copied. The
  behaviour is the same. Not worth a fix.) The one old draw is kept beside
  the twenty, for comparison only, as the method says.
- **Labelled NOT A RESULT**, in the output file's name and first field, the
  table's heading and the findings. **Run before the registration review.**

**Verdict: the code does what ruling 5 says, and nothing else.** One
reading in the method is the running session's and is reasonable: "where the
real figure sits" is reported as the three counts, not as a rank of its own.

### 5.2 Pull request 88 against ruling 7

Ruling 7 asks for: the three committed ownership-blind toy models through the
nomination and the reading as registered; laptop, $0; method before output;
checked by another session before the registration review; the method to
state, as the running session's reading, what "the model's own turn" and its
twin pairing mean for a solver with no acting channel; no verdict expected,
and a reading on any seed to go to John first.

**MEASURED from the code, then ARGUED.**

- **The three models, fingerprint-checked first:** yes (`C.check_sha`, then
  a strict load).
- **The nomination and the reading as registered.** The rule that chooses
  (`rerun_controls.pick`), the 45 site sets, the stricter row, the piece
  rule at 144 applied after the layers are chosen, the whole read printed
  beside it, the floor on development episodes at nomination and again on
  fresh episodes at the reading: all imported from the controls re-run, not
  copied. What is new is only the split between the batch the model is fed
  and the batch the positions and labels come from. Rulings 1 and 2 are
  followed exactly. Ruling 3 (the processor, versions pinned): followed.
  Ruling 4 (the toy's counts; the band printed): the counts are the toy's;
  **the band is printed for each seed's best piece only**, not beside every
  count taken against the floor. Since every count is 119 or more short of
  144, nothing turns on it, but the registered table must print it beside
  every such count, as ruling 4 says.
- **The read is fitted here, because no committed read exists for this
  solver.** The fit is the repairs' own call (logistic regression, at most
  3,000 iterations, C = 1.0, first 420 of 600 for fitting). It is saved and
  then applied unchanged to fresh episodes. Fair, and the method says so.
- **"The model's own turn" and the twin pairing are stated** as the
  session's reading, with a second reading run beside it. Reading A (channel
  removed, as trained) makes the twins one input, so the no verdict follows
  by construction; reading B (channel left on) is the one that tests the
  solver. Both the method and the findings say this plainly. **This is the
  most useful thing the run did**, and it goes past what the ruling asked.
- **What the code does not do (ARGUED).** Version 4 requires the registered
  code to *withhold* a reading itself when a no-transplant miss is outside
  its allowance, or a control that holds fails (section 6.4, item 5, lines
  1205 to 1213). This code records the no-transplant miss and prints it, but
  its "a reading was returned" field depends only on the floor at the
  reading; and it runs none of the controls. Had a site set been nominated,
  stop B2 would have fired on a figure the registered code would have
  withheld. Nothing was nominated, so no figure is affected. The method
  states that it runs no controls (section 4, "Not run"); it does not state
  that the no-transplant rule is printed and not applied. **The findings'
  sentence "It would withhold a reading on its own" (section 1) is true of
  the rule as version 4 registers it, not of this code**, and should say so.
- **Stops.** B1 to B4 are coded as the method states them and none fired.

**Verdict: the run does what ruling 7 asks.** The gap above is a gap
against version 4's later requirement on the registered code, which no
toy-scale code yet meets (version 4 lists it as owed at line 3866), not
against ruling 7.

### 5.3 The solver's explanation of why it gets no verdict

**ARGUED, from version 4's text.** The findings' section 4 (last paragraph),
their question 2, and the pull-request description say what "holds the
solver back with room to spare is, in order: the gate on learning (... in the
registered experiment a model that fails the gate is not read at all); the
piece rule; and the no-transplant rule."

Version 4 does not put the competing solvers through the gate. Section 8.1
gates arms T, C and M on the own-directed condition and arm F on both
(lines 2150 to 2159); the competing solvers' accuracy is listed under
"Reference points reported alongside, and they are references and not
thresholds" (lines 2178 to 2187); the gate row of section 9 says the same
(line 2257). Failing the gate gives outcome R3 *for an arm* (line 2188). So
for the solver the gate is a counterfactual: it *would* fail the gate, on
both conditions and every seed, if it were gated as arm F is. Under the
rules as written, what returned no verdict was the floor at nomination, and
what would have returned no verdict after it, with room to spare, is the
piece rule and the no-transplant rule.

This matters because the registration will likely quote this run as its
answer to "can the measure be satisfied by the wrong thing?". An answer that
leans on the gate invites the reply that the gate is not applied to
competitors. *Fix:* in section 4 and question 2 of the findings and in the
pull-request description, say "would fail the gate if it were gated as arm F
is" and put the piece rule first.

### 5.4 The whole-state floor's job, as the run shows it

**ARGUED, from the measured figures in 4.1 and 4.2.** The findings are right
that on this solver the floor is "a coin": its requirement is four fifths of
(accuracy − untouched rate), and for a solver that cannot tell whose value it
needs those two are within a few episodes of each other. On seed 2 with the
channel left on the fresh floor asked for less than one episode in 800 and
33 site sets cleared it by one or two episodes. Had any of them been
nominated and reached the reading, the formula's divisor would have been one
or two episodes in 800, and the reading would have been decided by single
episodes (the description-only arithmetic on that seed runs from 0.0000 to
1.0000, middle 1.0000).

So the floor alone does not keep the divisor away from zero. On a real arm
it is kept large by three rules together: the gate puts accuracy at 0.2633
or more; the no-transplant rule keeps the untouched rate within 0.018 of
(1 − accuracy) ÷ 7, which is at most about 0.123 at the bar; so the room
between them is at least about 0.14, and four fifths of that is at least
about 0.11. This touches version 4's item R-6 (section 6 below).

---

## 6. Job 5: which sentences of version 4 each finding bears on

Version 4 read at `7a55fe0`. Not edited.

### 6.1 The solver's findings, section 7

| Claim | Right? |
|---|---|
| **Section 7.3, the last paragraph** (lines 1996 to 2017): the run it says is owed exists; "no verdict" came back; its reason ("no read of its own marker word that reaches four fifths") holds but is not the rule that stopped the run first; "This version quotes no figure for it" and "until then this text does not go to the registration review" can be replaced once the run is checked | **Right.** The best piece is 20 to 25 of 180, so the stated reason holds; the floor at nomination stopped it first. Add: the paragraph should also say that with the channel removed the no verdict follows from the pairing alone (section 5.2 above) |
| **Section 8.1, the reference points** (lines 2178 to 2187): 0.2340 to 0.2383 reproduced exactly on the processor; the clause "to be put through the nomination under it before the registration review" is answered | **Right.** 702/3,000 = 0.2340 and 715/3,000 = 0.2383; equal field for field |
| **Section 10, item R-5** (lines 2391 to 2396) **and "What happens next"** (lines 2455 to 2458): the run is done, method first; the check is owed | **Right.** This check is that check |
| **The header's item 2** (lines 21 to 25) | **Right** |
| **Any sentence saying the whole-state floor protects against a solver like this**: "not found by search" | **There is one, and it is a near miss: item R-6** (lines 2397 to 2399), "The chance-corrected form's denominator is kept off zero by the whole-state floor". See section 5.4 above. Also, less directly, line 1860, "Its job of catching a leaky site set is done by the whole-state floor and the no-transplant rule", which is about a different failure and still holds |

**Passages the solver's findings did not name, which also need updating
(MEASURED, by search):**

- **Section 10, item R-4** (lines 2386 to 2389): the list of no-verdict
  cases ("arm F on every seed ...; control 2 on every toy model it applies
  to") can now add the ordinary competing solver, on every seed.
- **Section 11, step 1** (lines 2475 to 2478): "Owed before step 2: the
  competing solver's run under the piece rule, and its check".
- **Section 15, item 29** (lines 3318 to 3324) and its closing sentence
  ("follows the checks owed on this version, the competing solver's run").
- **Section 17** (lines 3735 to 3737, "The competing solvers' figures were
  taken before the piece rule") and the closing paragraph (lines 3864 to
  3869, "What this pass leaves open").
- **Section 19, item 7** (lines 4035 to 4053) and **"What this version does
  not do"** (lines 4215 to 4217).
- **Section 6.4, item 3**, the reason given for the no-transplant formula
  (lines 1178 to 1183: "because an untransplanted model lands on the donor's
  answer only by erring onto exactly that one of the seven other slots"),
  which the solver's question 3 is about.

### 6.2 The control's findings, section 6

| Claim | Right? |
|---|---|
| **Section 7.3, item 2, "What is reported"** (lines 1781 to 1786): the code now does it | **Right**, and section 5.1 above confirms it |
| **The same item's bullet "The part of its code after the floor has run once, and that run is NOT A RESULT"** (lines 1810 to 1829): should name this run as well as the earlier one | **Right** |

**The passage the control's findings did not name, and the one that matters
most (MEASURED, by search; the session could not have known, because the
ruling that makes it wrong came after its branch was cut):**

- **Section 7.3, item 2, the bullet "Twenty random pieces, not one"**
  (lines 1830 to 1837): "That is a change to the control's code, owed with
  the registered measurement, so the code path that ran once on 2026-10-03,
  with a single random piece, is not quite the one registered." John's
  ruling on the check's questions (ruling 1) says the change is made
  *before* the registration review, and names these lines. After this pull
  request the sentence is wrong twice: the change is made, and the code path
  that ran is the one with twenty pieces.

**Also not named:** section 10's paragraph on the seven controls (lines
2445 to 2453, "the part of its code after the floor has run once, in a run
labelled NOT A RESULT"), which needs the same update as lines 1810 to 1829;
section 17's closing paragraph (lines 3864 to 3869), which lists "control
2's twenty random pieces" as code still owed; the section 9 row for control 2
(line 2265), whose citation for the twenty is record A only; and section 19,
item 5 (lines 4009 to 4018), which can say the change has been made and the
code test re-run.

---

## 7. What needs changing in version 4 for the registration text

By section and line, at `7a55fe0`. For whoever writes the registration text;
this check edits nothing.

| Where | Lines | What changes | Why |
|---|---|---|---|
| Header, item 2 | 21 to 25 | The run is done and checked; say what came back in one sentence, or remove the item | Pull request 88 and this check |
| Section 6.4, item 3 | 1178 to 1183 | After "because an untransplanted model lands on the donor's answer only by erring onto exactly that one of the seven other slots", add that this assumes wrong answers spread evenly; a model that confuses owners lands on the donor's value more often (on the toy's competing solver about twice the formula), and the rule then withholds the reading, which is the intended outcome | The solver's question 3; table 3.3 of its findings |
| Section 7.3, item 2, "has run once" bullet | 1810 to 1829 | Name the second code test (pull request 89, `out-control-2-twenty-draws/`, NOT A RESULT) beside the first, with its figures: real figure 0.0012; twenty pieces middle 0.0037, 95th percentile 0.0052; 0 below, 1 equal, 19 above. Keep "not a pass or a fail of anything" | Ruling 5; pull request 89 |
| Section 7.3, item 2, "Twenty random pieces, not one" | 1830 to 1837 | Replace "owed with the registered measurement, so the code path that ran once ... is not quite the one registered" with: the change is made, in `src/control2_twenty_draws.py`, and its code test was run before the registration review. Cite the check-questions ruling 1 | That ruling names these lines |
| Section 7.3, the last paragraph | 1996 to 2017 | Replace "has not yet been measured ... This version quotes no figure for it ... until then this text does not go to the registration review" with the result: no verdict on every seed, under both readings of the solver; the reason (no site set cleared the floor at nomination); the read's best piece 20 to 25 of 180; the no-transplant rule failed on every seed; and that with the channel removed this follows from the pairing alone, so the reading with the channel left on is the informative one. Cite the findings and this check | Pull request 88 |
| Section 7.5, item 4, and the matching lines in 7.4 and section 9 | 2105 to 2108; 2072 to 2076; 2276 | Name how the band is computed: the Wilson interval at 95 percent, as the competing-solver run computes it. Ruling 4 says "the band that sampling alone would put around it" and names no method | Section 4.2 above |
| Section 8.1, reference points | 2178 to 2187 | Replace "to be put through the nomination under it before the registration review" with the result, and keep the solvers as references: **say that the gate does not apply to them** | Section 5.3 above |
| Section 9, control 2 row | 2265 | Cite record B, ruling 5, and the check-questions ruling 1 beside record A | Both records stand; the second ruling set the timing |
| Section 10, R-4 | 2386 to 2389 | Add the competing solver to the no-verdict cases | Pull request 88 |
| Section 10, R-5 | 2391 to 2396 | "Exercised under the piece rule, 2026-10-03, and checked" with a pointer | Pull request 88 and this check |
| Section 10, R-6 | 2397 to 2399 | "kept off zero by the whole-state floor" becomes "kept off zero by the whole-state floor together with the gate and the no-transplant rule", with one sentence: on the toy's competing solver, which fails the gate, the floor was cleared on fresh episodes with a divisor of one or two episodes in 800 | Section 5.4 above |
| Section 10, the paragraph on the seven controls | 2445 to 2453 | As for lines 1810 to 1829 | Pull request 89 |
| Section 10, "What happens next"; section 11, step 1 | 2455 to 2458; 2475 to 2478 | Move the competing solver's run and its check from "owed" to done | Pull request 88 and this check |
| Section 13, weaknesses | (new) | One weakness, if John agrees (question 7 in section 9 below): the toy's ordinary competing solver fails the task, so its no verdict shows the measure returns nothing on a model that has not learned the task, not on one that solves it by a different route | Section 9, question 7 |
| Section 15, item 29; section 17; section 19, items 5 and 7; section 20; closing | 3318 to 3324; 3735 to 3737; 3864 to 3869; 4009 to 4018; 4035 to 4053; 4161 to 4162; 4190 to 4193; 4215 to 4217 | Each says the run, the control's code change, or both are owed; each becomes done, with a pointer | Pull requests 88 and 89 |

**Not to change:** nothing in either pull request touches a registered
number. No floor, bar, count or site list moves.

---

## 8. What this session did not do

- It did not edit pull request 88 or 89, version 4, any ruling file,
  `STATUS.md` or `data/project.toml`.
- It did not read version 4 through end to end; the passages in section 6
  were found by search and read with their sections.
- It did not run either piece of code on any model the runs did not use, did
  not run the `--smoke` paths, and did not re-run the earlier code test (it
  compared against that test's committed output).
- It did not compute, at the 33 site sets that cleared the floor on fresh
  episodes, what the reading would have been at each one; the run does not
  save the fresh-episode grid, and section 5.4 relies on the summary the run
  does save.
- It did not check the controls re-run, the short pre-stated run or the
  repairs, beyond reading the functions these two runs import.
- It put no question to John in chat and read no transcript of another
  session.

---

## 9. The questions for John

Not asked in chat; for the coordination session that routes rulings, one
session at a time.

### 9.1 The five the two findings put

**The solver's question 1: which reading of the solver the registration
cites.** *Their suggestion:* the channel removed as the primary, because
that is how the solver was trained and scored; the channel left on stated
beside it, because with the channel removed the no verdict follows from the
pairing alone. **Follows from the evidence.** With the channel removed the
twins' states were identical to the last bit on every seed (section 4.1), so
every transplant is a null transplant and that reading cannot return
anything but no verdict. *Addition:* the registration should say in so many
words that the primary reading's no verdict is a property of the pairing,
not evidence about the measure, and that the channel-left-on reading is the
one that tests the measure.

**The solver's question 2: whether the registration says what actually
stops this solver.** *Their suggestion:* one sentence, that the solver's no
verdict comes from the gate on learning, the piece rule and the
no-transplant rule, each with room to spare, and that the floor is close to
zero for a model near chance. **Follows in part; the gate needs rewording.**
The piece rule (best 20 to 25 of 180 against 144) and the no-transplant rule
(missed by 0.11 to 0.14 against 0.018) are right. The gate is not applied to
competing solvers in version 4 (section 5.3). *Suggested sentence instead:*
"On the toy, the ordinary competing solver returned no verdict because no
site set cleared the floor at nomination; behind that, its best piece missed
the piece rule by 119 or more of 180 and its untouched rate missed the
no-transplant rule by 0.11 or more, and it would have failed the gate on
learning had it been gated as the free model is. For a model near chance the
floor itself is close to zero and is decided by one or two episodes."

**The solver's question 3: the no-transplant formula on a solver that cannot
tell owners apart.** *Their suggestion:* report only; the rule withholds a
reading here, which is the right outcome, but the registration should not
describe the formula as a property of every model. **Follows.** The untouched
rate (0.22 to 0.25) sits close to the solver's own accuracy (0.22 to 0.24),
which is what a solver choosing among the four agents' values would show;
the donor's value is one of those four. The wording change is in section 7
above, at lines 1178 to 1183.

**The control's question 1: which file is the registered control 2.**
*Their suggestion:* the registration names `control2_twenty_draws.control2`
as control 2's code and says `rerun_controls.control2` is the earlier
version, kept as the record of what the re-run did. **Follows.** The new
function is the old one with only the ruled change (section 5.1), and the old
one still carries the pass line John withdrew. *Addition:* the registered
code for the full-size run is still to be written (section 11, step 3 of
version 4); it should take control 2 from the new function, so that there is
one control 2 at registration and not two.

**The control's question 2: whether the 95th percentile of twenty is the
right summary.** *Their suggestion:* leave it as ruled, and print the twenty
as well. **Follows.** With twenty draws the 95th percentile is a mix of the
two largest (here 0.0052, between 4 and 7 episodes of 800, which no single
draw can equal); control 3 has the same property and was ruled that way.
Printing the twenty, as the code does, lets a reader see the spread.

### 9.2 Two that this check raises

**6. The solver run's explanation, before it is quoted.** Section 4 of the
solver's findings, its question 2 and pull request 88's description say the
gate on learning is the first thing holding the solver back, on the ground
that "a model that fails the gate is not read at all". Version 4 does not
gate the competing solvers (section 5.3). *Suggestion:* the running session,
or the session that writes the registration text, corrects those three
places to "would fail the gate if it were gated as the free model is" before
any of it is quoted; no re-run, and no change to any rule. This is a wording
question, and it goes to John only because pull request 88 is his to merge.

**7. What the competing-solver run can and cannot show.** The toy's ordinary
competing solver fails the task: it is right about one time in four, the
rate of a solver that cannot tell whose value it needs. So its no verdict
shows that the measure returns nothing on a model that has not learned the
task. It does not show what the measure does on a model that *does* the task
by a route other than tracking whose turn it is, which is the harder test of
"satisfied by the wrong thing". The toy has no such model: the name-only
solver is computed from the episodes and has no states to transplant
(`training.name_only_solver`). *Suggestion:* no new run before the
registration review. Add one weakness to section 13 of the registration text
saying this in two sentences, so a reviewer finds it stated rather than
finding it. *Strongest alternative:* build a competing solver that learns
the task from another cue (for example, a model fed the name token at every
turn) and put it through the measure before the review; that is a training
run, not $0 work on committed files, and would move the timeline.
===== END OF RECORD 15 =====

===== RECORD 16 of 25 - the measurement rehearsal on small stand-in models - `docs/2026-09-21-successor-measure-rehearsal.md` (complete file, 56,203 characters) =====
# The successor experiment's measurement rehearsal — findings

*2026-09-21 (Pacific). **UNREGISTERED.** Nothing here is a result about the
scientific question, nothing here is a bar, and nothing here registers
anything. It is a demonstration that the instrument exists and gives back
numbers — and, where it does not, an account of why.*

*Ran locally on the laptop, on models of about one to one and a third million
parameters. **No machine was rented, no vendor was contacted and nothing was
spent.** The one short slice of rented time is staged and has not been run; it
needs John's spoken go naming it, and that has not been given.*

*Filed at the path the protocol names for a rehearsal whose experiment
directory does not exist yet. Code and every output file:
`experiments/rehearsal-successor-measure/`.*

*Written under the workspace plain-language rule.*

---

## 0. What to read if you read nothing else

The measure works, and the procedure for pointing it at a system does not.

- **The measure separates the two constructed arms by the whole width of its
  scale.** The arm built so that the ownership answer sits in a slot of its
  own reads **exactly 0.0000** on all three seeds. The arm built so the
  ownership answer is stirred through everything reads **0.873, 0.885 and
  0.880**. That is rehearsal item R-2 and R-3 both passing, and it is the
  thing the successor experiment most needed to know.
- **The nomination procedure as the proposal writes it fails completely**, on
  the one arm whose answer is in a known place. It returns 0.0000 to 0.0117
  where the truth is 1.0000 — that is, it reads the separable arm as
  maximally entangled. The cause is that the proposal names the quantity the
  straight-line read is fitted to and never says what the **label** is, and in
  a grammar whose marker words are drawn afresh each episode that phrase has
  three meanings, two of which find nothing.
- **The two findings the proposal review marked fatal are both confirmed**, by
  measurement rather than by argument, and one of them is confirmed to four
  decimal places.
- **The freely trained arm reads at the entangled end**, not between the two
  anchors. That is either the honest answer or the instrument's ceiling, and
  the rehearsal cannot tell which.
- **Two of the seven controls do not mean what they say they mean**, and one
  of them would veto exactly the arm it exists to validate.
- **Throughput**: the two constructed architectures cost 0.98 and 1.05 times
  what the free one costs per step, not the 1.55 the money estimate inherited
  from a different experiment. Only the *ratio* is measured; the absolute
  figure the second release of money rests on still needs the rented slice.
- **The proposal's first stop condition is adjudicated here and does not
  fire.** It is keyed to the learn-both item failing, and that item does fail on
  half of itself. But the condition's own words are "not learnable even in
  principle" and "nothing trains", and the separable arm reaches 1.0000 on both
  conditions on all three seeds. The reasoning is in section 8, and it is the
  rehearsal's reading rather than a ruling.

---

## 1. What was committed when

The programme's discipline is method before output, and the worst failure in
its history came from a fix marked adopted with nobody having run anything.
The commit order on this branch:

| order | commit | what |
|---|---|---|
| 1 | `9a91c06` | the method: what would be built, and passing, failing and no-verdict for every check, written down while nobody knew which would fire |
| 2 | `518bf0e` | the method addendum: four further checks, after the review returned two findings marked fatal — again committed before their code |
| 3 | `5fa85e2` | the code: the grammar, the three architectures, the transplanting code, the measure |
| 4 | `8bc5fbe` | the rented slice, staged and not run |
| 5 | `9673bf1`, `4e89c69`, `623ef23` | the denominator checks, the frozen reads, the across-seed method, the self-test record |
| 6 | `6e8cc08` | the results |
| 7 | this file | the findings |

Section 9 records every place where building it differed from planning it,
which is the only honest way to keep a method file that was committed first.

---

## 2. The six checks the protocol requires

Each with the command that was run and the output it produced. The full output
of every one is in `experiments/rehearsal-successor-measure/out/`.

### P-1. The target can be found — **PASS, but only after a repair**

    cd experiments/rehearsal-successor-measure/src
    ../../../.venv/bin/python rehearse.py --stage nominate

The instrument is the proposal's own two-step nomination: fit a straight-line
read for "which agent is acting" at every candidate site, take its leading
directions up to a rank cap, then nominate by **causal effect** — the subspace
whose transplant best reproduces the counterfactual on development episodes.
It runs blind on every arm; the separable arm's known ownership block is never
handed to it.

On the separable arm, where the answer is in a known place by construction:

| seed | the procedure **as pre-stated** | the procedure **repaired** | the truth (its real ownership block) |
|---|---|---|---|
| 0 | 0.0117 | **1.0000** | 1.0000 |
| 1 | 0.0000 | **1.0000** | 1.0000 |
| 2 | 0.0000 | **1.0000** | 1.0000 |

The repair is section 3. **As written the procedure fails**; repaired, it
finds the answer exactly, and the reading it produces matches what the
procedure gets when it is simply handed the true block.

### P-2. The comparison has room to move — **PASS**

    ../../../.venv/bin/python rehearse.py --stage gate

Both ordinary competing solvers were built and scored on both conditions, and
all seven controls were run on every arm and seed. Nothing was assumed.

| solver | own-directed | named-other-directed |
|---|---|---|
| ownership-blind (trained, acting channel removed) | 0.2237 | 0.2253 |
| name-only (computed) | 0.2380 | 1.0000 |
| references: guessing over eight slots / a solver that cannot tell whose value it needs | 0.1250 / 0.2500 | 0.1250 / 0.2500 |

The comparison is not saturated: the separable arm reaches 1.0000 on both
conditions against an ownership-blind competitor at 0.2237.

### P-3. The arithmetic is finite — **PASS**

    ../../../.venv/bin/python measure.py --self-test

Sixteen made-up cases chosen to break the formula, including a zero
denominator, a denominator just under and just over the floor, an
ownership-only accuracy above the whole-state one, both accuracies equal and
both zero. Every one returns a finite number or the explicit no-verdict
outcome with its reason. All 10,201 share pairs from zero to one were swept:
none returns a non-finite value. A floor of zero is refused outright, because
a floor of zero is the closed design's unsatisfiable-denominator defect
re-entering through the front door.

### P-4. The interventions run end to end — **PASS**

    ../../../.venv/bin/python transplant.py --self-test
    ../../../.venv/bin/python rehearse.py --stage transplant

Every arm is trained, **saved to a checkpoint file and read back from it**
before any intervention runs, so what is exercised is the path the registered
experiment would use. Eight interventions run to completion on every arm and
seed: the whole-state transplant, the ownership-only transplant, the null
transplant, the content-complement transplant, the matched random-subspace
transplant, an unmatched donor's transplant, a transplant at a position where
the identity cannot yet be known, and the acting-channel lesion.

They move what they are supposed to move: on the separable arm the whole-state
transplant takes the donor-dictated action from 0.0000 to 1.0000.

### P-5. All three outcomes are reachable — **PASS**

    ../../../.venv/bin/python rehearse.py --stage outcomes
    ../../../.venv/bin/python negative_case.py

| made-up case | expected | measured |
|---|---|---|
| the separable arm at its nominated site set | near zero, valid | **0.0000, 0.0000, 0.0000** |
| the entangled arm at its nominated site set | high, valid | **0.8727, 0.8848, 0.8801** |
| the separable arm at a deliberately failing site set (earliest layer, before the identity can be known) | no verdict | **no verdict**, whole-state accuracy 0.0000 |
| a negative reading | reachable | **−0.1706 and −0.2755** |

The negative reading deserves its own sentence, because finding it took
finding out what causes it. Searched over every architecture, every one of the
nine layer sets, every one of the five position sets, all three readings of
the read's label and all six rank caps on fresh episodes, **no configuration
produced a negative reading at all**. It appears immediately on episodes whose
marker words the arms have never seen. The condition is therefore not
mysterious and it is worth registering: **a negative reading appears when the
subspace was chosen on data whose vocabulary the reading is then taken on.**
The nominated directions live in the well-trained part of the space; the
whole-state transplant is capped by the arm's own degraded accuracy on strange
words; so the subspace beats the superspace and the reading goes below zero.
That is exactly what the proposal says a negative reading is for — a warning
about the instrument, reported as observed and never clipped to zero.

### P-6. An ordinary competing solver is built and scored — **PASS**

    ../../../.venv/bin/python rehearse.py --stage gate

Two were built, because "satisfied by the wrong thing" has two shapes here. An
**ownership-blind solver** — the same architecture with the acting channel
removed entirely, so it has none of the structure the measure claims to detect
— scores 0.2237 on the own-directed condition and 0.2253 on the named-other
one, which is the one-in-four level and nothing more. A **name-only solver**,
computed rather than trained, gets the named-other condition exactly right and
the own-directed condition at 0.2380.

The measure does not read near-zero degree off the blind solver, because the
blind solver cannot be read at all: its own-directed action does not depend on
an ownership answer it does not have, so there is nothing for a transplant to
move. **That is the right answer** — a system with none of the structure
returns no reading rather than a flattering one.

---

## 2a. The proposal's eleven rehearsal items, and where each one stands

| item | what it had to show | state |
|---|---|---|
| **R-1** the grammar works and both conditions are learnable at tiny scale | both matched conditions above the one-in-four level; the four matched properties hold in the generated data | **FAIL on one half.** All four matched properties pass their checks. The own-directed condition clears its bar on every arm and seed. The named-other-directed condition clears it on one seed of three on the entangled arm and one of three on the free arm, and doubling the training budget moves it about a point. Section 8 — which also adjudicates the proposal's first stop condition, keyed to this item failing: **it does not fire**, because the separable arm reaches 1.0000 on both conditions on all three seeds |
| **R-2** the separable arm is constructible and its pointer is transplantable on its own | blind nomination finds it without being told where it is; the ownership-only transplant reproduces the counterfactual | **PASS on the arm, FAIL on the procedure as written.** The arm is constructible and its pointer is patchable on its own: the reading is exactly 0.0000 on all three seeds. The blind nomination finds it only under one of three readings of the read's label, and returns near zero under the other two. Section 3 |
| **R-3** the entangled arm is constructible and its degree is genuinely known by construction | no subspace reproduces the counterfactual while the whole-state transplant at the same sites does | **PASS.** Whole-state 0.540 to 0.575 against a best blind-nominated subspace of 0.066 to 0.069, on all three seeds. The two-arm fallback does not fire |
| **R-4** all four outcomes of the measure are reachable | near zero, high, negative, no verdict | **PASS.** 0.0000; 0.873 to 0.885; −0.1706 and −0.2755; and no verdict at the deliberately failing site set. The negative outcome needed its cause found before it could be produced at all — section 2, P-5 |
| **R-5** an ordinary competing solver is built and measured | a solver that cannot use ownership and a solver that uses only the name token, both scored on both conditions | **PASS.** 0.2237 and 0.2253; 0.2380 and 1.0000 |
| **R-6** the arithmetic is finite | the floor rule and the no-verdict rule exercised on cases chosen to break them | **PASS.** Sixteen made-up cases, 10,201 share pairs swept, no non-finite value, a floor of zero refused |
| **R-7** throughput is measured, per arm | seconds per step and projected wall-clock and money for each architecture at the registered size | **PARTIAL, and it is the one place the rehearsal reaches a question only a rented machine can answer.** The ratios between the three architectures are measured at 0.981, 1.049 and 1.000. The absolute seconds per step on rented hardware cannot be obtained on a laptop. Section 10 |
| **R-8** the transplanting code passes its known-answer tests | the null transplant changes nothing; a transplant moves the action to the donor's value; the ownership-only transplant is the whole-state one restricted to a subspace | **PASS.** The null transplant leaves every logit bit-identical on every arm and seed. The restriction property is proved as a tensor identity at full rank, with a largest logit difference of exactly zero. The transplant moves the separable arm's action from 0.0000 to 1.0000 |
| **R-9** the paired-uncertainty method is chosen and demonstrated | two candidates computed on the same data, and the seed count following from the method rather than from habit | **DEMONSTRATED; the choice is not made here.** Across-seed spread 0.0189 and 0.0227; the within-seed bootstrap over matched pairs 0.0198 and 0.0203. They agree closely, which is the useful finding. The arithmetic for a half-width of 0.05 implies one seed at toy scale, which should not be carried across without a discount |
| **R-10** the separation bar is set | the observed separation between the two constructed arms and its spread, with the reasoning written out | **MEASURED, DELIBERATELY NOT SET.** 0.873 to 0.885 against exactly 0.0000, across-seed spread 0.019 and 0.000. Fixing the bar is John's; the measurement shows the choice is not a close one |
| **R-11** seconds per step is measured on the rented machine, for all three arms, and the shutdown path is exercised against the real vendor | seconds per training step for each architecture at the registered size, on the registered venue and rate, plus both halves of the shutdown handshake | **NOT RUN — it needs John's spoken go naming the run, and that has not been given.** Everything it asks for is staged and costed: `docs/successor-rented-slice-staging-2026-09-21.md`, with the plan the staging script writes in `out/rented-slice-plan.txt`. One slice is estimated at about **$0.75 to $1.00** with a hard cap of **$2.00** (staging note), inside the **$3** the proposal budgets for this item. Section 10 |

*The eleventh row was added after the fact, and the reason is worth stating so
nobody reads it as a gap that was nearly missed. The proposal grew item R-11
four seconds after this rehearsal's method file was committed, on the branch
this work was not on, so the rehearsal was planned against a list of ten and
this table was first written with ten rows. The rehearsal staged and costed
exactly what the eleventh item asks for anyway, without having seen it. Nothing
was missed but the numbering — and a table that claims to cover every item has
to cover every item, because the protocol makes a pre-stated quantity with no
rehearsal line against it a fatal finding on its own.*

---

## 3. The finding that matters most: the nomination step is underspecified

> **Added 2026-09-23 by a later session — the label has since been ruled, and
> this section is otherwise untouched.** John has ruled that the straight-line
> read is fitted against **which marker word is the model's own**, the third of
> the three readings below and the only one that returns this arm's known
> 0.0000. He first chose the marker's rank — the reading this section annotates
> as the programme's own convention — was shown the measured degrees in the
> second table below, and changed his answer. The ruling is
> `docs/rulings/2026-09-23-nomination-label.md`; authorship is mixed, the
> session put the options and the measurement and he chose. **Item 4 of this
> section is not answered by that ruling and stays open**: the winning reading
> still varies across the nine arm-and-seed pairs, so fixing the label does not
> make the procedure one instrument. Nothing below is rewritten — this is a
> dated record of what was measured on 2026-09-21, and it stands as written,
> including where it calls the label an open question.

Section 7.2 of the proposal says: *fit a straight-line read for "which agent is
acting"*. It never says what the label is. In a grammar whose marker words are
drawn afresh every episode — which both the registered generator and this
stand-in do, on purpose, so that no marker word is attached to any agent —
that phrase has at least three meanings:

- **the agent's slot** in the episode's list of agents. This is arbitrary per
  episode: nothing in the episode defines it, so no state can carry it. It is
  also the natural reading of the proposal's sentence, and it is the one the
  method file pre-stated.
- **the rank of the model's own marker word** among the four present, in
  vocabulary order. This is the programme's own existing convention, from the
  method file for the eleven-position fitted read.
- **which marker word is the model's own**, out of the pool.

How well each fits, at the action position, and what each finds when its
directions are transplanted into the arm whose answer is in a known place:

| reading of the label | how well it fits, seeds 0 / 1 / 2 | ownership-only transplant, best over every site set and rank cap, seeds 0 / 1 / 2 |
|---|---|---|
| the agent's slot | 0.256 / 0.256 / 0.256 (chance is 0.25) | **0.0117 / 0.0000 / 0.0000** |
| the marker's rank — *the programme's own convention* | 0.706 / 0.694 / 0.700 | **0.0050 / 0.0183 / 0.0117** |
| which marker word | 1.000 / 1.000 / 1.000 | **1.0000 / 1.0000 / 1.0000**, at rank 8 and above |

Every cell above is read out of `out/nominate.json`. An earlier draft of this
table printed the two failing rows as a flat **0.0000**; neither is 0.0000 on
every seed, and the marker-rank row is not 0.0000 on any seed. The correction
does not move the finding — 0.005 to 0.018 is far below the 0.2500 a solver
that cannot tell whose value it needs reaches by luck, so "no causal effect" is
still the fair plain reading — but a cell in this table has to carry what was
measured, and these two did not.

**What the measure itself would print, which is the sentence this turns on.**
The table above reports the transplant accuracies and leaves the arithmetic to
the reader. Doing the arithmetic means putting each label's best configuration
through `measure.py`, at the rehearsal's own working floor of 0.30, with the
whole-state accuracy and the no-transplant rate the record gives for this arm
(1.0000 and 0.0000 on all three seeds, so both candidate forms of the reading
agree exactly):

| seed | reading of the label | whole-state | ownership-only | the degree the measure prints |
|---|---|---|---|---|
| 0 | the agent's slot | 1.0000 | 0.0117 | **0.9883** |
| 0 | the marker's rank | 1.0000 | 0.0050 | **0.9950** |
| 0 | which marker word | 1.0000 | 1.0000 | 0.0000 |
| 1 | the agent's slot | 1.0000 | 0.0000 | **1.0000** |
| 1 | the marker's rank | 1.0000 | 0.0183 | **0.9817** |
| 1 | which marker word | 1.0000 | 1.0000 | 0.0000 |
| 2 | the agent's slot | 1.0000 | 0.0000 | **1.0000** |
| 2 | the marker's rank | 1.0000 | 0.0117 | **0.9883** |
| 2 | which marker word | 1.0000 | 1.0000 | 0.0000 |

**Under the two failing readings of one unwritten word, the instrument reports
a degree of 0.982 to 1.000 for an arm whose degree is 0.0000 by construction.**
That is a wrong answer of the largest size the scale allows, on the one arm
where the right answer is known in advance. It is not a near miss and it is not
a matter of precision: the instrument would put the separable arm at the
entangled end of its own scale and give no sign that anything had gone wrong.

Four things follow, and all four belong in the registration text.

1. **The registration must say what the label is.** Under two of the three
   readings the measure would have reported the separable arm — the arm whose
   degree is zero by construction — as maximally entangled. That is a wrong
   answer of the largest possible size, produced by a sentence nobody thought
   was ambiguous.
2. **The programme's existing convention is one of the two that fail.** The
   marker-rank label fits at 0.706, 0.694 and 0.700 across the three seeds,
   well above chance, and its best transplant reaches 0.0050, 0.0183 and
   0.0117 — no useful causal effect at all. This is the programme's own lesson
   arriving in a new shape: a representation a straight-line read recovers
   beautifully can do nothing when you intervene on it. The proposal already
   says to nominate by causal effect rather than by fit, and this rehearsal is
   the first thing in the programme to show what that rule buys.
3. **The rank cap is not free either.** With the right label, at the site set
   the nomination picks on all three seeds (the first layer, at the position
   where the action is taken), the ownership-only transplant on the separable
   arm averages **0.153 at rank 1, 0.355 at rank 2, 0.832 at rank 4 and 1.000
   at rank 8**. Per seed, from `out/nominate.json`: 0.1517 / 0.1417 / 0.1667 at
   rank 1, 0.3350 / 0.3950 / 0.3350 at rank 2, 0.7783 / 0.8467 / 0.8717 at rank
   4, and exactly 1.0000 on every seed at rank 8. A cap below the
   dimensionality of the encoding cannot carry the answer however well the
   subspace is chosen, so a rank cap chosen for parsimony would have produced a
   partial reading and been indistinguishable from partial entanglement.
   *(An earlier draft of this paragraph gave the curve as 0.170, 0.365 and
   0.805. Those three figures are in no committed output file, and no arm,
   label, site set or way of averaging reproduces them: across the nine search
   grids of 810 rows each, the closest rank curve of any arm, label and site set
   misses them by 0.055 in total. They are
   withdrawn, and the measured curve above replaces them.)*
4. **Even repaired, the procedure is not one instrument.** The label that wins
   is not the same label twice running. Across the nine arm-and-seed pairs the
   winning reading is which-marker-word seven times, the marker's rank once
   (the entangled arm at seed 2) and the agent's slot once (the free arm at
   seed 0). The margins in those two cases are tiny: on the entangled arm at
   seed 2 the three labels reach 0.0683, 0.0650 and 0.0633, and on the free arm
   at seed 0 they reach 0.0700, 0.0683 and 0.0667 — so no reading reported
   anywhere in this file moves. But an instrument that silently picks one of three
   meanings per run is three instruments, and which one it is depends on the
   data it is pointed at. That is a second reason, independent of the first,
   why the registration has to fix the label rather than leave the search to
   choose it.

---

## 4. The reading, on fresh episodes

> **Added 2026-09-23 by a later session — what may be quoted from this table
> has since been ruled, and this section is otherwise untouched.** Re-running
> the whole rehearsal from the committed code, from clean, on 2026-09-22
> reproduced the separable arm's rows exactly and reproduced **none** of the
> entangled or free arm's figures: those two arms' readings moved by up to
> 0.0506 and 0.0440. John has ruled that from those two arms the registration
> may quote **a range and a direction only** — about 0.83 to 0.89, at the
> entangled end, one seed of three clearing the learn-both bar — and **no
> decimal as a property of the code**, so no "degree d" sentence for them. The
> ruling is `docs/rulings/2026-09-23-range-and-direction-only.md`; authorship is
> mixed — the session put the question and three options, he chose one. It
> settles nothing else: neither form of the reading's arithmetic is adopted, and
> the uncertainty method, the seed count and the separation bar in section 11 all
> stay open — with the seed-count row now known to rest on a spread that does not
> measure this variation at all. Nothing below is rewritten; this is a dated
> record of what was measured on 2026-09-21 and it stands as written.

    ../../../.venv/bin/python rehearse.py --stage transplant

Both candidate forms of the reading are reported everywhere. Neither is
adopted here.

| arm and seed | no transplant | whole-state | ownership-only | the reading as registered | the floor-corrected reading |
|---|---|---|---|---|---|
| separable, seed 0 | 0.0000 | 1.0000 | 1.0000 | **0.0000** | 0.0000 |
| separable, seed 1 | 0.0000 | 1.0000 | 1.0000 | **0.0000** | 0.0000 |
| separable, seed 2 | 0.0000 | 1.0000 | 1.0000 | **0.0000** | 0.0000 |
| entangled, seed 0 | 0.0600 | 0.5400 | 0.0688 | **0.8727** | 0.9818 |
| entangled, seed 1 | 0.0663 | 0.5750 | 0.0663 | **0.8848** | 1.0000 |
| entangled, seed 2 | 0.0638 | 0.5525 | 0.0663 | **0.8801** | 0.9949 |
| free, seed 0 | 0.0600 | 0.5825 | 0.0663 | **0.8863** | 0.9880 |
| free, seed 1 | 0.0550 | 0.5663 | 0.0925 | **0.8366** | 0.9267 |
| free, seed 2 | 0.0762 | 0.5663 | 0.0850 | **0.8499** | 0.9821 |

**The separation between the two constructed arms is the whole scale.** Zero
against roughly 0.88, with an across-seed spread of 0.019 on the entangled arm
and exactly zero on the separable one.

**The free arm sits at the entangled end.** Its three readings, 0.886, 0.837
and 0.850, are inside the entangled arm's range, not between the two anchors.
Two readings of that, and the rehearsal cannot choose between them: either a
freely trained system of this shape genuinely keeps its ownership answer
distributed, or the instrument saturates and cannot tell "quite entangled"
from "entangled by construction". Section 7 says what would separate them.

---

## 5. The two findings the review marked fatal, both confirmed

### The reading divides by an uncorrected accuracy — **confirmed**

    ../../../.venv/bin/python denominator.py --stage simulated
    ../../../.venv/bin/python denominator.py --stage attenuated

On made-up trial populations built from a **known** true share of the
identity-driven difference living outside the subspace — 0.5 in both cases —
and two different transplant effectivenesses, drawn 200 times at 2,000 trials
each:

| case | whole-state accuracy | the reading as registered | the floor-corrected reading |
|---|---|---|---|
| strong transplant | 0.9008 | 0.4323 (spread 0.0119) | **0.5018** (spread 0.0132) |
| weak transplant | 0.3497 | 0.3222 (spread 0.0181) | **0.5013** (spread 0.0230) |

The floor-corrected form returns the true share in both cases. The registered
form differs between two systems that are identical in the quantity it claims
to report, by 0.110 — six times its own spread.

On **real forward passes**, holding the architecture, the sites and the
subspace fixed and only moving the state a fraction of the way toward the
donor's, the same thing happens on most arms but not on all of them. Counted
out of `out/denominator_attenuated.json`, arm by arm and seed by seed, with the
span each form covers across the four attenuations:

| arm and seed | the reading as registered | the floor-corrected reading | which is flatter |
|---|---|---|---|
| entangled, seed 0 | 0.0405 | 0.0221 | floor-corrected |
| entangled, seed 1 | 0.3424 | 0.0164 | floor-corrected |
| entangled, seed 2 | 0.0087 | 0.0023 | floor-corrected |
| free, seed 0 | 0.3291 | 0.0085 | floor-corrected |
| free, seed 1 | 0.0680 | 0.0710 | **the registered one** |
| free, seed 2 | 0.5169 | 0.0732 | floor-corrected |
| separable, seed 0 | 0.0067 | 0.0067 | dead heat |
| separable, seed 1 | 0.0631 | 0.0631 | dead heat |
| separable, seed 2 | 0.0066 | 0.0066 | dead heat |

**Five of the nine, not six.** Three are dead heats, and they are dead heats
for a reason worth stating rather than glossing: on the separable arm the
no-transplant rate is exactly zero, so the two forms are the same arithmetic on
that arm and cannot disagree. The biggest gaps are the free arm at seed 2,
where the registered reading spans **0.5169** across the attenuation while the
floor-corrected one spans 0.0732, and the entangled arm at seed 1, where the
registered reading spans 0.3424 against 0.0164.

**And this check fails its own pre-stated cell on one arm and seed, which was
not reported.** The method addendum's cell for it is written per arm, and its
fail line is exactly "the registered form is the flatter one"
(`docs/successor-measure-rehearsal-method-addendum-denominator-2026-09-21.md`,
check D-2). On the free arm at seed 1 the registered form is the flatter one,
0.0680 against 0.0710. **That is a fail, and it is recorded here as a fail.**
The gap is small and the overall picture is unchanged — five arms and seeds
favour the correction, three cannot distinguish the two forms, and the two
largest gaps in the table are both enormous and both in the correction's favour
— but a pre-stated line that fires has to be reported when it fires, and an
earlier draft of this file reported no fail anywhere for this check.

**One measurement makes this less alarming than it looks, and it is worth
putting beside the finding.** The correction's size is the no-transplant rate,
and on a working arm that rate is near zero, so the two forms nearly coincide
in the table in section 4. The gap opens exactly where the whole-state
transplant is weak — which is where the proposal's own weakness list expects
the entangled arm to be. So the finding bites on the arm it was predicted to
bite on, and not before.

**Nothing here chooses a form.** Both are computed, both are reported, and
which is registered is John's to rule on.

### A control's first cell is empty by construction — **confirmed exactly**

    ../../../.venv/bin/python denominator.py --stage control6
    ../../../.venv/bin/python denominator.py --stage floor

Under a grammar that keeps the four values within an item distinct — which the
proposal requires in three places — **0 of 4,000 trials** fall in the cell
where the donor's identity dictates the same value as the recipient's. The
reason is structural, not statistical: within an item the four values are
distinct and the successor rule is one-to-one, so distinct sources give
distinct answers, always.

Filling the cell means relaxing distinctness, and that costs something
measurable: on a relaxed set, 346 of 4,000 trials land in the cell, and the
reference a solver that cannot tell which agent it is can reach moves from
**0.2467 to 0.3095** on exactly the trials that were added.

The same distinctness inverts the proposal's sanity rule on the no-transplant
rate. Measured against both predictions on the record:

| arm and seed | measured | the proposal says | the review's formula says |
|---|---|---|---|
| separable, all three seeds | 0.0000 | 0.1250 | 0.0000 |
| entangled, seed 0 | 0.0600 | 0.1250 | 0.0598 |
| entangled, seed 1 | 0.0663 | 0.1250 | 0.0620 |
| entangled, seed 2 | 0.0638 | 0.1250 | 0.0605 |
| free, seed 0 | 0.0600 | 0.1250 | 0.0624 |
| free, seed 1 | 0.0550 | 0.1250 | 0.0634 |
| free, seed 2 | 0.0762 | 0.1250 | 0.0587 |

The proposal's "near one in eight" is wrong on every arm, and is wrong in the
direction that matters: it **passes for a model at chance and fails for a model
that works**. As registered it would call a working instrument broken. The
review's formula is far better — but **not, as an earlier draft of this file
said, right to within a few thousandths everywhere.** The misses, out of
`out/denominator_floor.json`: the separable arm's three seeds are exact at
0.0000; the entangled arm's three are out by 0.0002, 0.0042 and 0.0033; the
free arm's are out by 0.0024, **0.0084** at seed 1 and **0.0175** at seed 2.
So seven of the nine are within about four thousandths or better and two are
not, and the worst miss — 0.0762 measured against 0.0587 predicted — is nearly
two hundredths, which is about **a third of the value being predicted**. The
finding stands and the formula is the right one to register in place of "near
one in eight"; the claim about how closely it predicts does not, and a rule
registered against it needs room for a miss of that size.

---

## 6. The seven controls, and the two that do not mean what they say

Run on every arm and seed. The table below is seed 0 of each arm; the rest are
in `out/transplant.json`.

| control | separable | entangled | free | what it should show |
|---|---|---|---|---|
| 1. transplant the complement of the nominated subspace | 0.0000 | 0.5375 | 0.5813 | the action follows content, not identity |
| 2. an unmatched donor's representation | 0.2513 | 0.0525 | 0.0613 | the action does not move |
| 3. a matched random subspace of the same rank | 0.0000 | 0.1113 | 0.0975 | no donor action |
| 4. a transplant before the identity can be known | 0.0000 | 0.0650 | 0.0600 | nothing happens |
| 5. fresh marker and content combinations | by construction | by construction | by construction | — |
| 6a. same-value cell: share whose action moved | **0.000** | 0.691 | 0.741 | nothing moves |
| 6b. different-value cell: share whose action moved | **1.000** | 0.921 | 0.908 | everything moves |
| 7. null transplant leaves every logit bit-identical | true | true | true | nothing changes |

**Control 6 is the one that earns its place, and it says something
uncomfortable.** On the separable arm it discriminates perfectly: nothing moves
when the donor's identity dictates the same value, everything moves when it
dictates a different one. That is precisely what "the transplant moved who is
acting" looks like. On the entangled and free arms the action moves in about
**three quarters** of the same-value trials, where it should move in none. On
those arms the whole-state transplant is carrying something besides identity,
and the reading of roughly 0.88 cannot be read as purely a statement about
where the ownership answer lives. This is the outside review's "satisfied by
the wrong thing" worry arriving with a number attached, and it is the single
most important caveat on section 4's table.

**Control 1 cannot hold for an entangled arm, by construction.** Transplanting
the complement of the nominated subspace reproduces the counterfactual almost
exactly as well as transplanting the whole state — 0.5375 against 0.5400. That
is not a defect in the arm; it is what entanglement *means*. In a system where
the ownership signal multiplies content at every layer there is no
ownership-free complement to transplant. **As the proposal writes it, control
1 would veto the reading on exactly the arm the control battery exists to
validate.** It needs re-wording before registration: on the separable arm it
is a real and passing check (0.0000), and on an entangled arm it should be
recorded as not applicable and said so, rather than failed.

**Control 2 was implemented differently from the proposal and its number
should not be read as a pass.** The proposal asks for a representation of a
*named agent who is not acting*, nominated by the identical procedure. What
was run instead transplants the ownership subspace of an *unmatched* episode.
On the separable arm that gives 0.2513, which is the one-in-four rate — the
action moved to an arbitrary identity and coincided with the matched donor's
by chance. The control as the proposal states it is still owed.

---

## 7. What would make the experiment look unbuildable, or the measure
unreadable — the honest list

This is the part worth more than a clean report.

1. **The free arm is not between the anchors; it is at one of them.** Readings
   of 0.886, 0.837 and 0.850 against an entangled arm at 0.873 to 0.885. If
   that holds at the registered size, the promised outcome — "the closure
   sentence *degree unmeasured* is replaced by a number" — is delivered, but
   the number is "as entangled as a system built to be entangled", and the
   measure will not have demonstrated that it **scales** rather than merely
   **detects**. What would separate the two readings is a fourth arm built to
   sit deliberately in the middle, which this rehearsal did not build and which
   the proposal does not have. **Recommendation, for John to rule on: add a
   partially-separable arm to the design, or accept in the registration text
   that a free-arm reading near the entangled anchor cannot be told from a
   ceiling.**
2. **Control 6 fails its pre-stated shape on two of the three arms.** Three
   quarters of the same-value trials move. Until that is understood the
   roughly-0.88 readings are not clean statements about where the ownership
   answer lives.
3. **The whole-state transplant can never beat the arm's own accuracy**, and
   at toy scale that ceiling is about 0.55 on the entangled and free arms
   because that is all those arms can do. Every floor, and every separation
   bar, is therefore a statement about a denominator that is itself bounded by
   how well the arm learned. A floor named as an absolute number would be
   wrong; it has to be named relative to the arm's own accuracy on the same
   episodes. That is a change to the proposal's section 6.4.
4. **The freshness requirement is ambiguous and the strong reading breaks the
   measurement.** Section 7.1 asks for "marker and content combinations that
   appear in neither of the other two sets". Read as *combinations*, the
   separable arm scores 1.0000 and the measure reads 0.0000. Read as *marker
   words the arm has never seen*, the separable arm's own accuracy falls to
   0.7612, 0.6512 and 0.6512, the whole-state transplant is capped there, and
   the reading goes **negative** on two seeds out of three. The registration
   has to say which reading it means. (The strong reading is what produced the
   negative case in section 2, so it is worth keeping as a deliberate
   diagnostic, not as the evaluation set.)
5. **The degenerate site set is real and has to be excluded in writing.**
   Transplanting every layer at every position is not an intervention: it is
   the donor's own forward pass, proved as a tensor identity in the
   transplanting code's self-test. On the separable arm the whole-state
   accuracy is 1.0000 at *every one* of the forty-five site sets, so the
   "smallest layer set that clears the floor" rule the proposal gives has
   nothing to choose between and would pick arbitrarily.
6. **The named-other condition barely learns at toy scale, and doubling the
   training budget does not fix it.** This is what the proposal's own honest
   prior predicts for the whole experiment, reproduced for nothing. See
   section 8.

---

## 8. The learn-both gate, and the condition that did not learn

    ../../../.venv/bin/python rehearse.py --stage gate

| arm and seed | own-directed | named-other-directed | own-directed with the acting channel removed |
|---|---|---|---|
| separable, 0 / 1 / 2 | 1.0000 / 1.0000 / 1.0000 | 1.0000 / 1.0000 / 1.0000 | 0.2467 / 0.2510 / 0.2733 |
| entangled, 0 / 1 / 2 | 0.5817 / 0.5660 / 0.5767 | 0.2590 / 0.2370 / 0.2637 | 0.1717 / 0.1807 / 0.1860 |
| free, 0 / 1 / 2 | 0.5633 / 0.5563 / 0.5890 | 0.2547 / 0.2680 / 0.2393 | 0.1813 / 0.1947 / 0.1857 |

**R-1 fails on the named-other condition, as pre-stated.** The cell fixed
before running was: both conditions above the one-in-four level, significantly
under a binomial test at the 0.05 level, on at least two seeds of three. On
3,000 held-out episodes that bar is 0.2630. The entangled and free arms clear
it on **one seed each**. The own-directed condition clears its bar
comfortably everywhere.

This is not a surprise and it is not a small thing. Section 3 of the proposal
states the honest prior before the work: the most likely outcome of the whole
experiment is that an arm fails the learn-both gate, and **the most likely
reason is the named-other half**. The rehearsal reproduces exactly that
failure, at toy scale, for about two hours of laptop time.

**Is it the budget or the task? Measured, not guessed.**

    ../../../.venv/bin/python budget_check.py

The free arm was trained once more at roughly twice the budget — 5,000 steps
instead of 2,500, on 20,000 matched pairs instead of 15,000. The named-other
condition moved from **0.2547 to 0.2657**, and the own-directed condition from
0.5633 to 0.5737. Doubling the budget bought about one percentage point on the
condition that is failing, which leaves it sitting on the bar rather than
clearing it.

**So the shortfall is not mainly a limit of the training budget.** At this
size, on this grammar, the named-other-directed revision is close to
unlearnable **by the two arms that are not built with the ownership answer in a
slot of its own**, and more steps do not fix it. (The qualifier matters and the
next paragraph turns on it: the separable arm learns the same condition to
1.0000 at the same size on the same grammar.) That does not settle what happens
at the registered size — the ten-million rung failed to learn the earlier
design's task and the thirty-million rung did not — but it does mean the risk
the proposal's honest prior names is real, is reproducible on a laptop for
nothing, and would be worth attacking in the design before about $110 of
registered runs are committed to it.

### Does the proposal's first stop condition fire? Adjudicated here: **no**

The proposal's stop conditions halt spend and go to John. The first of them,
**S1**, is keyed to exactly the item this section marks failed:

> **S1.** The rehearsal fails item R-1 (the grammar is not learnable at tiny
> scale even in principle) or item R-8 (the transplanting code does not pass
> its known-answer tests). Nothing trains. About $10 spent.

A reader going from this file to the proposal will ask whether the line is
supposed to stop here. The question is answered here rather than left to
whoever reads the two documents next, because the proposal's own eighth stop
condition (**S8**, the one that forbids stepping over anything) says a stop
condition is never recorded as not applicable and stepped over.

**The finding: S1 does not fire.** Two measurements settle it, both from
`out/gate.json`.

- **The separable arm reaches 1.0000 on both conditions, on all three seeds.**
  Own-directed 1.0000 / 1.0000 / 1.0000 and named-other-directed 1.0000 /
  1.0000 / 1.0000. A trained model of this size, on this grammar, learns both
  conditions perfectly. S1's own words are "not learnable at tiny scale **even
  in principle**" and "**nothing trains**". Something trains, and it trains to
  the top of the scale.
- **The named-other condition is solvable at this scale by a strategy the
  rehearsal built and scored.** The name-only solver — which reads nothing but
  the name token — reaches **1.0000** on the named-other condition (and 0.2380
  on the own-directed one). So the condition is not unlearnable in principle;
  it is unlearned by two of the three architectures.

What actually failed is narrower than S1's words, and is still serious: on the
two arms that are *not* built with the ownership answer in a slot of its own,
the named-other condition does not clear its pre-stated bar on a majority of
seeds, and doubling the budget does not fix it. That is a fact about those
architectures at this size, not about the grammar in principle.

**The strongest case for the other reading, stated rather than skipped.** Item
R-1 as the proposal words it in section 10 says "both matched conditions are
learnable at tiny scale" without naming an arm; this file marks R-1 a **FAIL**;
and a reader who chains "item R-1 failed" straight to the first stop condition
gets a stop. The eighth stop condition can be read as pushing the same way. The
reason that reading does not carry: the eighth is about an item that **cannot
be evaluated** — missing data, a measurement never taken — and this one was
evaluated, with every number on the record. And the first stop condition is not
keyed to the item's heading but to the state of the world its own parenthesis
names, which the separable arm's 1.0000 contradicts directly. A stop condition
that fired when a model scores perfectly on both conditions would be firing on
the opposite of the thing it names.

**What follows instead.** The consequence the measurement supports is item 5 of
section 12 — a design change for the named-other condition, or a decision to
accept the risk with the number in front of John — not a halt. **This is the
rehearsal's adjudication and not a ruling, and it is John's to overturn.** If he
reads S1 as firing, the line stops and the proposal's own accounting for that
stop is "about $10 spent"; the actual figure so far is **nothing**, because
every number in this file was produced on the laptop.

**The acting-channel lesion behaves as pre-stated on the separable arm and
not on the others.** Removing the channel drops the separable arm's
own-directed accuracy to the one-in-four level (0.2467 to 0.2733) while its
named-other accuracy stays at **1.0000** — textbook. On the entangled and free
arms the lesion drops *both* conditions, because in a system where ownership
modulates everything, removing the channel disturbs everything. The
proposal's section 8.2 pre-states the shape "own-directed collapses,
named-other holds"; that shape is **architecture-specific**, and the
registration should say so rather than apply it to all arms.

---

## 9. Where building it differed from planning it

The method file is unchanged; this is the record of the departures, which is
the only honest way to keep a method that was committed first.

1. **The deliberately broken arm was not built.** The method planned an arm
   with two sign-flipped copies of the ownership answer so that the whole-state
   transplant would cancel itself. Building it showed the idea cannot work:
   because matched pairs differ only in the acting channel, the whole-state
   transplant at a site set is *exactly the donor's state there*, so any
   architecture that is consistent under it cannot be made to cancel. The
   negative outcome was pursued by a systematic search instead, and found —
   section 2, P-5 — with its cause identified. This is a better result than the
   planned one, and it was forced by the building.
2. **The nomination family was widened at one end and narrowed at the other.**
   Three readings of the read's label instead of one, and rank caps to 24
   instead of 8. The pre-stated family is still computed and reported
   separately at every point, so the failure of the procedure *as written* is
   on the record beside the repaired one. 810 comparisons per arm and seed.
   **The narrowing was not recorded when it happened, and is recorded here.**
   The first commit of the rehearsal code (`5fa85e2`), committed before any
   result ran, fixed five rank caps in `rehearse.py` — one, two, **three**,
   four and eight, as the line `RANK_CAPS = [1, 2, 3, 4, 8]`. The final code
   drops the cap of three and counts only caps of one, two, four and eight as
   belonging to the pre-stated family. So the pre-stated family is **180
   comparisons as actually computed** — nine layer sets by five position sets
   by four rank caps by one reading of the label, which is the count of
   pre-stated rows in `out/nominate.json` — and not the 225 an earlier draft of
   this file reported. One pre-stated cell, a rank cap of three under the
   pre-stated reading of the label, is not in the record at all. It does not
   change the finding: under that reading, caps of one, two, four and eight all
   return between 0.0000 and 0.0117 and the fit sits at chance, so there is no
   mechanism by which a cap of three alone would have found the answer. But the
   claim this rehearsal makes is precisely that the procedure *as pre-stated*
   fails, and that claim is owed the whole pre-stated procedure rather than
   four fifths of it.
3. **The fitted reads were frozen.** The first implementation re-fitted the
   straight-line read on the fresh episodes the reading is taken from, which is
   the one thing a data split exists to prevent. Fixed before any result in
   this file was read; the reads are fitted on development episodes, written to
   disk, and reloaded.
4. **The fresh pool was corrected** from unseen marker words to unseen
   combinations of seen words, per section 7 item 4. The stronger pool is kept
   under its own name because its collapse is a finding.
5. **Control 2 was implemented differently from the proposal**, recorded in
   section 6 rather than quietly counted as a pass.
6. **The rehearsal ran as soon as it was built** rather than waiting for a
   slot. Nothing about it was waiting on a calendar.

---

## 10. Throughput, and exactly what still needs the rented machine

    ../../../.venv/bin/python rehearse.py --stage throughput
    ../../../.venv/bin/python bench_arms.py --device auto --steps 20

At the registered configuration's shape — 448 wide, 12 layers — timed on the
laptop's own accelerator, batch 32, twenty steps after warm-up:

| architecture | parameters | seconds per step | median | ratio to the free arm |
|---|---|---|---|---|
| the separable arm | 26,065,471 | 0.2500 | 0.2508 | **0.981** |
| the entangled arm | 29,329,735 | 0.2672 | 0.2678 | **1.049** |
| the free arm | 29,049,735 | 0.2548 | 0.2557 | **1.000** |

**This is the measurement the second release of money was waiting for, and it
is only half of it.** The proposal carried a per-step premium of about 1.55,
inferred from a different experiment's full-versus-twin step times, "to cover
arms T and C being slower per step". Measured, the premium is **about five per
cent on the entangled arm and slightly negative on the separable one**. If
that ratio holds on rented hardware, the constructed arms do not cost
materially more than the free arm, and the second release's arithmetic — the
eight remaining runs at the planning figure — needs no architecture premium at
all.

**What a laptop cannot answer, and no arithmetic here can make it.** Seconds
per step on an Apple M4 does not predict seconds per step on a rented graphics
card. What transfers is the *ratio between the three architectures*; the
absolute figure does not. That is precisely the inference John's ruling of
2026-09-21 declined to build a release on.

So: **the rented slice is still owed, and it is now owed for a smaller
question than before** — not "how much more do the constructed arms cost",
which is answered at 0.98 and 1.05, but "how many seconds does a step take on
the machine we will rent". It is staged, costed and not run:
`docs/successor-rented-slice-staging-2026-09-21.md`, and the plan the staging
script writes is in `experiments/rehearsal-successor-measure/out/rented-slice-plan.txt`.

The same slice exercises the shutdown handshake against the real vendor, which
has never met it, and the pre-stated pass and fail lines for both halves are in
that staging note.

---

## 11. The numbers this rehearsal was told not to invent

Section 9 of the proposal lists nine numbers as outputs of the rehearsal. None
is named here. What each one now has behind it:

| number | what the rehearsal measured | still needed |
|---|---|---|
| the separation bar between the two constructed arms | separation of **0.873 to 0.885** against **0.0000**, across-seed spread 0.019 on the entangled arm and 0.000 on the separable one | John's ruling. A bar anywhere from 0.1 to 0.8 would separate these two at toy scale, so the measurement does not force a choice; what it does is show the choice is not close |
| the learn-both threshold, per condition | measured competitors: ownership-blind at 0.2237 and 0.2253, name-only at 0.2380 and 1.0000 | a decision about the named-other condition, which at toy scale does not clear the one-in-four level on a majority of seeds |
| the floor on the whole-state transplant accuracy | the full curve against site set, per arm, in `out/nominate.json`: the entangled arm runs 0.0517 at the first layer, 0.3467 at the second, and about 0.556 from the third on, which is its own accuracy | John's ruling — and, per section 7 item 3, a floor stated **relative to the arm's own accuracy**, not as an absolute |
| the rank cap on the nominated subspace | on the separable arm, at the site set the nomination picks, averaged across the three seeds: **0.153 at rank 1, 0.355 at rank 2, 0.832 at rank 4 and 1.000 at rank 8** — per seed in section 3, item 3 | John's ruling; the measurement says a low cap silently under-reads |
| the candidate site list and its family correction | 45 site sets × 3 labels × 6 rank caps = **810 comparisons** per arm and seed; the pre-stated family was 225 as planned and **180 as computed**, because the final code dropped the rank cap of three — section 9, departure 2 | John's ruling on which labels are in the family at all |
| the seed count per arm | three seeds gave an across-seed spread of 0.019 and 0.023 on the raw difference; the arithmetic for a half-width of 0.05 implies **one seed** | John's ruling. The toy arms are far more repeatable than registered-size runs will be, so this number should not be carried across without a discount |
| the paired-uncertainty method | both computed on the same data: across-seed spread 0.0189 and 0.0227; the within-seed bootstrap over matched pairs 0.0198 and 0.0203. **They agree closely**, which is itself the useful finding — the choice does not matter much here | John's ruling |
| the ownership-lesion collapse threshold | the separable arm drops to 0.2467 to 0.2733 on the own-directed condition while holding 1.0000 on the named-other one | a decision, plus the section 8 finding that the pre-stated shape is architecture-specific |
| seconds per step, per arm, on the rented machine — the whole of the second release's arithmetic | **nothing.** This rehearsal measured the *ratios* between the three architectures on the laptop (0.981, 1.049 and 1.000) and nothing else; the proposal says in terms that this number is never inferred from a premium and never measured on the Mac | rehearsal item R-11, the one short slice of rented time. Staged, costed and **not run**: it needs John's spoken go naming it. Section 10 |

---

## 12. What would be needed to finish

1. **John's rulings** on the eight numbers above, on which form of the reading
   is registered, and on the nomination label — which is now a
   registration-blocking question rather than a detail.
2. **The rented slice**, which needs his spoken go naming it. About $0.75 to
   $1.00, hard cap $2.00, inside the first release.
3. **Three repairs to the proposal text**, each with a measurement behind it:
   control 1 re-worded so it cannot veto the entangled arm; the no-transplant
   sanity rule replaced with the review's formula; and section 7.1's freshness
   requirement disambiguated.
4. **A decision about the middle of the scale** — a partially separable fourth
   arm, or an admission in the registration text that a free-arm reading at the
   entangled anchor cannot be told from a ceiling.
5. **A design change for the named-other condition, or a decision to accept
   the risk.** Section 8 settles that it is not a budget limit: doubling the
   budget moved it by about a point. This is the single cheapest thing the
   rehearsal found that could sink the registered experiment, and it is worth
   attacking before the money is committed rather than after.
6. **Control 2 built as the proposal states it**, rather than as it was run.

None of the six costs more than a few hours, and only the second costs money.
===== END OF RECORD 16 =====

===== RECORD 17 of 25 - the repairs to the rehearsal - `docs/2026-09-26-rehearsal-repairs.md` (complete file, 33,735 characters) =====
# The rehearsal repairs — findings

*Written 2026-09-25 (Pacific) by the Claude Code session "MVM W1c rehearsal
repairs", session (c) of `docs/weekend-1-session-prompts.md`, on branch
`worktree-w1c-rehearsal-repairs`. The file keeps the name the prompts file gives
it (dated 2026-09-26, the Saturday it was planned for); the work ran a day early
because the rulings it depends on were made on the evening of 2026-09-25.
**UNREGISTERED.** Nothing here is a result about the scientific question, nothing
here is a bar, and nothing here is a ruling. Every bar used below was ruled by
John in `docs/rulings/2026-09-26-weekend-1-queue.md` (the "Weekend 1 queue
ruling"); every other threshold is a rehearsal-only one fixed in the method note
before the run.*

*Ran locally on the laptop, on models of about one to one and a third million
parameters. **No machine was rented, no vendor was contacted and nothing was
spent: $0.***

*Method, committed before any code or output:
`docs/rehearsal-repairs-method-2026-09-25.md`. Code and every output file:
`experiments/rehearsal-successor-measure/src/` (new: `repairs.py`,
`arm_middle.py`, `diagnose_named_other.py`; changed: `training.py`) and
`experiments/rehearsal-successor-measure/out-repairs/`. The 2026-09-21 record in
`out/` and its driver `rehearse.py` are untouched.*

*Every finding is labelled **MEASURED** (a command was run and its output is
reported, with the committed file it wrote) or **ARGUED** (reasoning a reader can
dispute). Figures from the entangled and free arms are quoted as a range and a
direction, as `docs/rulings/2026-09-23-range-and-direction-only.md` requires:
those arms do not reproduce from code and seed on this laptop. Written under the
workspace plain-language rule.*

---

## 0. What to read if you read nothing else

- **Item 1, the named-other condition: neither redesign clears the ruled pass
  line, so page 4's fallback (d) applies.** The curriculum clears the bar on 0
  seeds of 3 and the loss re-weighting on 0 of 3; the unchanged recipe, re-trained
  in this session, clears on 1 of 3, as it did on 2026-09-21. Both redesigns made
  things worse: the curriculum teaches the model to answer the named-other turn
  with **its own** value, and the re-weighting costs the own-directed condition
  without buying the named-other one. MEASURED.
- **Why, most likely: the grammar signals "this is your turn" on both action
  turns**, so the only thing telling the two apart is one word, and the two
  conditions compete for one route. That points at page 4's redesign (c), a
  grammar change, which this session did not attempt. ARGUED.
- **Item 4, the fourth arm: it passes page 5's pre-stated line.** Built to be
  partly separable, it reads **0.48 to 0.53** on the chance-corrected form on all
  three seeds, inside 0.3 to 0.7, and within 0.02 to 0.04 of what its construction
  predicts from its own route accuracies. Folding it into the registration is
  John's call under page 5 and page 6. MEASURED.
- **Item 2, one instrument: done in code, and it exposed two things the ruled
  text does not settle.** The ruled exclusion ("every layer at every position")
  is too narrow, because copying **any** layer at every position hands the donor's
  whole forward pass downstream; the nomination picked such a set on two of arm
  C's three seeds. And the ruled site-list rule does not produce the toy's 176
  comparisons even on the toy: it produces 296. MEASURED.
- **The rider (John's addition): at arm T's site set, arms C, F and M give no
  verdict at all** — their whole-state transplant does not move the action
  there. So what differs between arms is, first, where the procedure has to look.
  MEASURED.
- **Item 3, control 2 as the proposal words it: no verdict on arms T, C and M,
  a pass on arm F that means little.** It needs the arm to carry the named
  agent in its running state and to have learned the named-other condition;
  arm T carries it outside the state by construction, and arms C and F have not
  learned the condition. MEASURED.
- **Item 5, the measure with the ruled form and numbers:** arm T reads 0.0000
  on every seed, exactly as on 2026-09-21; arm C reads at the entangled end
  (0.99 to 1.00); the free arm reads at the entangled end too (1.00 to 1.003),
  and **fails the learn-both gate**, so under the ruled numbers it would not be
  read at all. The separation bar of 0.5 is cleared on every seed. MEASURED.

---

## 1. What was committed when

| order | commit | what |
|---|---|---|
| 1 | `426b6e8` | the method note, before any code or output |
| 2 | `16d75f6` | training options, arm M, the driver's train and gate stages (code only) |
| 3 | `9e341e6` | nomination, measure and summary stages (code only) |
| 4 | `81dc84d` | two additions **not pre-stated**, labelled so in the code (§8) |
| 5 | `004d134` | the outputs |
| 6 | this file | the findings |

The method note precedes the first output commit. Two dry runs of the
measurement code were made on scratch checkpoints outside the repository before
commit 3 (one on untrained models, one on a trained arm T and a 400-step arm M,
on 120 episodes); nothing from them is committed or reported as a result.

---

## 2. Item 1 — the named-other condition (ruling page 4)

    ../../../.venv/bin/python repairs.py --stage train --arms F --recipes base,curriculum,reweight
    ../../../.venv/bin/python repairs.py --stage gate --arms F --recipes <recipe>

The pass line, fixed in the method note (§2.3) from the ruling: the named-other
condition at 790 or more correct of 3,000 held-out episodes (above 0.2630) on at
least two of three seeds, on the free arm. MEASURED, from
`out-repairs/gate_base.json`, `gate_curriculum.json` and `gate_reweight.json`:

| free arm, recipe | named-other, seeds 0 / 1 / 2 | seeds clearing | own-directed, seeds 0 / 1 / 2 |
|---|---|---|---|
| unchanged (re-trained here) | 0.3313 / 0.2603 / 0.2487 | **1 of 3** | 0.5597 / 0.5513 / 0.5547 |
| (b) curriculum: named-other only for the first 1,000 of 2,500 steps | 0.0773 / 0.1933 / 0.1430 | **0 of 3** | 0.5507 / 0.5643 / 0.5637 |
| (a) re-weighting: named-other loss four times own-directed | 0.2317 / 0.2063 / 0.2377 | **0 of 3** | 0.1700 / 0.1723 / 0.1760 |

**Neither redesign passes. Page 4's fallback (d) applies**, in the ruling's
words: the registration records that the named-other condition failed its bar on
two of three toy arms, that doubling the budget did not fix it, and that the
staggered first run reads the learn-both result of one free-arm run before the
remaining eight are committed. This session adds a sentence it can support:
**neither a curriculum nor loss re-weighting fixed it either.**

As a range and a direction, as the 2026-09-23 ruling requires for this arm:
the unchanged recipe's named-other accuracy ran 0.25 to 0.33, just around the bar
(on 2026-09-21 it ran 0.24 to 0.27, `out/gate.json`); both redesigns moved it
**down**. The unchanged recipe's seed 0 moved from 0.2547 on the record to 0.3313
here — the drift between runs the 2026-09-23 ruling describes, and the reason no
decimal here is offered as a property of the code.

**What the model answers instead.** An exploratory diagnostic, **not
pre-stated** (§8), classes each named-other prediction on the same 3,000
episodes. MEASURED, `out-repairs/diagnose_named_other.json`:

| free arm, recipe, seed | the named agent's value (right) | the model's own value | another agent's value in the item | a value not in the item |
|---|---|---|---|---|
| unchanged, 0 / 1 / 2 | 0.33 / 0.26 / 0.25 | 0.06 / 0.07 / 0.05 | 0.39 / 0.48 / 0.51 | 0.22 / 0.18 / 0.19 |
| curriculum, 0 / 1 / 2 | 0.08 / 0.19 / 0.14 | **0.55** / 0.14 / 0.28 | 0.17 / 0.38 / 0.30 | 0.20 / 0.30 / 0.28 |
| re-weighting, 0 / 1 / 2 | 0.23 / 0.21 / 0.24 | 0.17 / 0.18 / 0.18 | 0.47 / 0.49 / 0.45 | 0.13 / 0.13 / 0.13 |

The unchanged model knows *which item* and not *whose value*. After the
curriculum it often gives **its own** value at the named-other turn — on seed 0,
more than half the time. Under re-weighting it picks among the item's four values
in both conditions without knowing whose.

**The reading, ARGUED.** In this grammar the acting channel — the signal that
tells the model "this turn is yours" — fires on **both** action turns
(`grammar.py`, `render`: `acting.extend([1] * 7)` for each action turn). The two
turns differ only in the word after `revise`: the word meaning *your own*, or a
marker word. So the easy route to the own-directed answer (follow the acting
channel back to your own assignment turn) is equally available at the
named-other turn, and a model that learns it applies it at both. The curriculum's
first phase evidently did not survive the second; the re-weighting made the model
give up the acting-channel route rather than add the marker-matching one. If that
reading is right, a training change cannot fix it and a grammar change can —
page 4's option (c), for instance an action turn whose acting-channel pattern
differs between the two conditions, or the named agent's marker placed where the
model's own sits. **That is a design question for John, not attempted here**: it
re-opens rehearsal items R-1 to R-6 and the Gate C review of the proposal.

Page 4's strongest argument against — that every toy redesign may be fixing a
problem scale removes — stands whatever this shows.

---

## 3. Item 2 — the nomination step as one instrument (ruling page 3)

    ../../../.venv/bin/python repairs.py --stage nominate --arms <arm> --recipes base

**What changed in code.** `repairs.py` has one label, `READ_LABEL =
"marker-word"`, not a tuple; rank caps `(1, 2, 4, 8)`; 44 site sets (the
rehearsal's nine layer sets times five position sets, less "every layer at
every position"); and `assert len(SITE_SETS) == 44 and FAMILY_SIZE == 176`. One
function, `nominate`, takes no argument that names an arm and is called
identically for every arm. MEASURED (the assertion runs on import; every
`nominate_base_*.json` records `"family_size": 176` and `"label": "marker-word"`).

**What it selected**, on 600 development pairs. MEASURED, from
`out-repairs/nominate_base_T_C.json`, `nominate_base_F.json`,
`nominate_base_M.json`:

| arm, seed | site sets clearing the floor | nominated (positions, layers, rank) | development whole-state / ownership-only | the other reading of "smallest that clears" would pick |
|---|---|---|---|---|
| T, 0 / 1 / 2 | 44 / 44 / 44 | action, first layer, rank 8 — all three | 1.0000 / 1.0000 on all three | the same, all three |
| C, 0 | 38 | **every position**, first layer, rank 2 | 0.5867 / 0.0550 | the same |
| C, 1 | 35 | **every position**, first layer, rank 4 | 0.6033 / 0.0567 | after identity, all five layers, rank 8 |
| C, 2 | 38 | after identity, first layer, rank 2 | 0.5300 / 0.0550 | after identity, all five layers, rank 2 |
| F, 0 | 35 | after identity, first layer, rank 2 | 0.4883 / 0.0633 | after identity, second layer, rank 1 |
| F, 1 | 35 | action and three before, second layer, rank 4 | 0.5533 / 0.0500 | every position, layers 1 to 4, rank 8 |
| F, 2 | 35 | after identity, first layer, rank 1 | 0.4933 / 0.0700 | after identity, second layer, rank 8 |
| M, 0 | 35 | after identity, first layer, rank 8 | 0.7900 / 0.3683 | after identity, third layer, rank 8 |
| M, 1 | 35 | action, fourth layer, rank 8 | 0.7250 / 0.3783 | after identity, second layer, rank 8 |
| M, 2 | 35 | after identity, first layer, rank 8 | 0.7717 / 0.3700 | after identity, all five layers, rank 8 |

("First layer" is the state after the input embedding, layer index 0 in the
code; "after identity" is every position from the model's first own turn to the
action.)

What this shows, MEASURED:

- **One rule was applied, and it no longer picks arbitrarily on arm T.** The
  2026-09-21 findings (section 7, item 5) said every site set gives arm T 1.0000,
  so "the smallest layer set that clears the floor" had nothing to choose between.
  With ties broken as the method note fixed, it chooses the same site set on all
  three seeds.
- **The rule's outputs differ by arm**, as page 3 said they would, and they
  differ by seed within arms C, F and M.
- **The two readings of "the smallest layer set that clears it" disagree on 7
  of the 12 arm-and-seed pairs** (last column). The ownership-only shares they
  reach are close (0.0200 apart or less on every pair, from the same files), so no
  reading below moves much, but a registration has to say which reading it
  means. ARGUED: the one implemented (smallest clearing layer set per position
  set, then highest ownership-only share) follows the ruled words more closely.
- **The two forms of the floor never disagree.** Whether the four-fifths floor is
  written on the chance-corrected scale or plainly, the same site sets clear, on
  every arm and seed (0 disagreements across all 44 site sets, counted from the
  `floor` fields in the same files).

**The ruled exclusion is too narrow. MEASURED, then ARGUED.** On arm C seeds 0
and 1 the rule nominated the first layer **at every position**. Copying the
running state at every position of any layer makes everything downstream of that
layer the donor's own computation, wherever ownership lives only in the running
state. Arm C escapes being fully degenerate only because its ownership signal also
reaches every block by a side route the transplant does not touch (`arms.py`, the
scale-and-shift from `_own_vec`). On the free arm the first layer at every
position *is* the donor's forward pass. Page 1c excludes by name only "every layer
at every position"; the registration should exclude **every site set whose
positions are all positions**. A sensitivity row with those sets removed, **not
pre-stated** (§8), changes arm C's nomination on seeds 0 and 1 and nothing else;
the readings stay at the entangled end (1.0051 and 0.9863 on those two seeds,
`measure_base_T_C.json`, field `sensitivity_without_all_positions`).

**The ruled site-list rule does not produce 176, even on the toy. MEASURED.**
Page 1e registers the rule ("all contiguous layer sets", among other things) and
prints "176 comparisons per arm and seed" beside it as the toy's count. The 176
comes from the rehearsal's nine hand-listed layer sets, not from the rule:

```
$ python3 -c "
def contiguous(n_states): return [tuple(range(a,b+1)) for a in range(n_states) for b in range(a,n_states)]
toy=[(0,),(1,),(2,),(3,),(4,),(3,4),(2,3,4),(1,2,3,4),(0,1,2,3,4)]
c5=contiguous(5); c13=contiguous(13)
print('toy states (embedding + 4 blocks):', 5, '-> all contiguous layer sets:', len(c5))
print('toy hand-listed layer sets:', len(toy), '; all contiguous?', all(s in c5 for s in toy))
print('contiguous toy sets not in the hand list:', [s for s in c5 if s not in toy])
print('registered states (embedding + 12 blocks):', 13, '-> all contiguous layer sets:', len(c13))
print('toy family as run: 9 x 5 - 1 =', 9*5-1, 'site sets x 4 ranks =', (9*5-1)*4)
print('rule on the toy, with the same 5 position sets: 15 x 5 - 1 =', 15*5-1, 'x 4 =', (15*5-1)*4)
print('rule on the 12-layer model, same 5 position sets: 91 x 5 - 1 =', 91*5-1, 'x 4 =', (91*5-1)*4)
"
toy states (embedding + 4 blocks): 5 -> all contiguous layer sets: 15
toy hand-listed layer sets: 9 ; all contiguous? True
contiguous toy sets not in the hand list: [(0, 1), (0, 1, 2), (0, 1, 2, 3), (1, 2), (1, 2, 3), (2, 3)]
registered states (embedding + 12 blocks): 13 -> all contiguous layer sets: 91
toy family as run: 9 x 5 - 1 = 44 site sets x 4 ranks = 176
rule on the toy, with the same 5 position sets: 15 x 5 - 1 = 74 x 4 = 296
rule on the 12-layer model, same 5 position sets: 91 x 5 - 1 = 454 x 4 = 1816
```

Two further gaps, ARGUED: the rule's position clause ("the action position and
the positions between the source assignment and the action") does not say how
those positions are grouped into sets, and two of the toy's five position sets
("after identity" and "every position") reach outside it. And if every
all-positions set is excluded, as argued above, the counts change again. So the
registration has to print the list, as page 1e's strongest argument against
said, and the list and the rule have to agree.

### The rider: every arm read at arm T's site set

MEASURED, field `rider_at_arm_T_site_set` in the three `measure_base_*.json`
files. Arm T's nomination is the action position, first layer, rank 8, on every
seed.

| arm | at its own nomination | at arm T's site set |
|---|---|---|
| T | 0.0000 on all three seeds | the same site set: 0.0000 |
| C | 0.99 to 1.00 | **no verdict on all three seeds**: whole-state 0.0512 / 0.0488 / 0.0600, equal to the untouched rate |
| F | 1.00 to 1.003 | **no verdict on all three seeds**: whole-state 0.0587 / 0.0563 / 0.0688, equal to the untouched rate |
| M | 0.48 to 0.53 | **no verdict on all three seeds** |

At the first layer, at the action position, nothing about ownership has yet
reached the running state of arms C, F or M (the acting channel adds the same
vector at the action turn in both twins), so copying the donor's state there
changes nothing. **The first answer the rider gives, then, is that the arms
cannot be read at the same place at all.** What differs between arms is first of
all *where* the procedure has to look; whether their degrees differ can only be
asked at the site sets the rule chooses per arm. ARGUED: the rider as ruled should
stay in the reporting table, because "no verdict at arm T's site set" is exactly
the information it was added to surface.

---

## 4. Item 3 — control 2 as the proposal states it

Proposal section 7.3, item 2: "Nominate, by the identical procedure, a
representation of a named agent who is not acting, and transplant it. The
own-directed action should not move." Built as the method note (§4) fixed:
the named agent's marker word as the label; a named-swap twin as donor (same
content and actor, a different named agent, one token of text different); the
§3.2 rule anchored at the named-other action; pass if the own-directed action
changes in no more trials than under a random subspace of the same rank at the
same sites, plus 0.05 (a rehearsal-only tolerance).

MEASURED, field `control2` in the `measure_base_*.json` files and
`control2_named_agent` in the `nominate_base_*.json` files:

| arm | full procedure | why, or what it returned | fixed-site variant (the arm's own ownership sites) |
|---|---|---|---|
| T | **no verdict** on all three seeds | 0 of 44 site sets clear the floor, although the arm scores 1.0000 on the named-other condition: arm T selects the named agent from the turn's metadata, not from its running state, so no transplant into the state can move that action. Predicted in the method note | pass, vacuous: nothing moves |
| C | **no verdict** on all three seeds | 0 of 44 clear; the arm's named-other accuracy on development episodes is 0.2617 / 0.2483 / 0.2333 | pass; named-other action moved in 0.055 / 0.000 / 0.080 of trials |
| F | **pass** on all three seeds | own-directed moved in 0.0075 / 0.0000 / 0.0012 of trials, against 0.0125 / 0.0000 / 0.0000 under a random subspace | pass |
| M | **no verdict** on all three seeds | 0 of 44 clear, although the arm scores 0.5517 to 0.5663 on the named-other condition. ARGUED: two fifths of its named-other actions are answered by the separable route from metadata, as in arm T, so no transplant into the state can move enough of them | pass |

**The one pass means little. ARGUED.** On the free arm the nominated named-agent
subspace moves the *named-other* action itself in only 0.115, 0.001 and 0.035 of
trials. A representation that barely moves the action it is about cannot show
much by failing to move a different one. And the arm has not learned the
named-other condition (§2).

**So control 2, as the proposal words it, cannot be run as a check on the arms
that matter until the named-other condition is learned** — and on the
constructed arms it cannot be run at all, because they select the named agent
outside the running state. ARGUED: the registration should either say so and
record control 2 as "not applicable" on arms T and M, or reword it; it should not
be carried as a control that holds.

The old control 2 (an unmatched episode's ownership subspace), kept for
continuity, returns the one-in-four rate on arm T again (0.2512 / 0.2350 /
0.2562), as on 2026-09-21.

---

## 5. Item 4 — the fourth arm, built to be partly separable (ruling page 5)

**The construction** (`src/arm_middle.py`, method note §5): arm T's slot and
head, and arm C's entangling and ordinary output layer, in one network; actions
about items `it1` to `it3` go through the entangled route, `it0` and `it4`
through the separable one, about three fifths entangled (0.6033 of the fresh
episodes, `measure_base_M.json`). Its self-test passes all seven checks,
including "perturbing the slot never moves an entangled-route action" (largest
logit movement 0.00e+00) — `out-repairs/self-tests.txt`. **It is a mixture by
item, not partial separation within each trial**, and page 5's strongest
argument against applies in full: its degree is a design intention, and it
differs from both anchors in more than degree.

**The prediction, from the method note, fixed before the run:** the blind
reading between 0.30 and 0.60 on every seed, and within 0.10 of the formula
`p·(a_C − u_C) / [(1 − p)·(a_T − u_T) + p·(a_C − u_C)]` on the arm's own route
accuracies; and, from the record's arm C figures, a number near 0.42 to 0.43.

MEASURED, from `out-repairs/measure_base_M.json` and `gate_base.json`:

| seed | blind reading | the formula on this arm's route accuracies | handed its true slot | separable route: whole / untouched | entangled route: whole / untouched |
|---|---|---|---|---|---|
| 0 | **0.5105** | 0.4895 | 0.4895 | 1.0000 / 0.0000 | 0.6501 / 0.0207 |
| 1 | **0.4846** | 0.4572 | 0.4572 | 1.0000 / 0.0000 | 0.5818 / 0.0290 |
| 2 | **0.5322** | 0.4904 | 0.4904 | 1.0000 / 0.0000 | 0.6542 / 0.0228 |

- **Page 5's pass, 0.3 to 0.7 on all three seeds: passes.**
- **The method note's band, 0.30 to 0.60: passes. Within 0.10 of the formula:
  passes** (misses 0.021, 0.027, 0.042).
- **The number predicted from the record, 0.42 to 0.43, was low.** The entangled
  route learned better in arm M than arm C does alone: 0.77 to 0.78 on the
  own-directed condition on the gate episodes (`gate_base.json`,
  `own_by_route`), against arm C's 0.57 to 0.58. It therefore carries more of
  the effect. The formula, evaluated on the measured routes, is the prediction
  that held.
- **The blind reading is slightly above the true-slot reading** on every seed,
  because the blind ownership subspace catches 0.92 to 0.96 of the separable
  route's effect rather than all of it (`ownership_only_by_route`).
- Arm M passes the learn-both gate on both conditions on all three seeds
  (own-directed 0.8613 to 0.8667, named-other 0.5517 to 0.5663, `gate_base.json`).
- Control 6 is cleaner than on arms C and F: the same-value cell moves in 0.235 /
  0.173 / 0.321 of trials (the entangled route's share), and the different-value
  cell in 0.846 to 0.953.
- Arm M has an entangled route, so it is not expected to reproduce exactly from
  code and seed; quote it as **0.48 to 0.53, in the middle of the scale**.

**What passing buys, ARGUED.** It shows the measure, pointed blind at a system
with a known mixture, returns a number in the middle and near the mixture's
share. It does not show that the measure scales on a system whose partial
separation is *within* each trial, which is what a freely trained system would
have. Under page 5 the arm is now a candidate for the main registration, with
three runs at $32 to $44 from page 6's $450 envelope; **folding it in is John's
decision**, and this session makes no recommendation stronger than that.

---

## 6. Item 5 — the measure with the ruled form and the ruled numbers

    ../../../.venv/bin/python repairs.py --stage measure --arms <arms> --recipes base
    ../../../.venv/bin/python repairs.py --stage gate --arms T,C,F,M,blind --recipes base
    ../../../.venv/bin/python repairs.py --stage summary --arms T,C,F,M --recipes base

Run on the unchanged recipe only, because no redesign passed (method note §2.4).
Fresh episodes: 800 matched pairs, 1,600 trials per arm and seed.

### 6.1 The gates (pages 1b and 1h)

MEASURED, `out-repairs/gate_base.json` (3,000 episodes; bar 790 correct):

| arm | own-directed, seeds 0 / 1 / 2 | named-other, seeds 0 / 1 / 2 | learn-both (page 1b) | lesion: own-directed with the acting channel removed |
|---|---|---|---|---|
| T | 1.0000 on all three | 1.0000 on all three | **passes** | 0.2467 / 0.2510 / 0.2733 (reported, not gated) |
| C | 0.5703 / 0.5677 / 0.5757 | 0.2533 / 0.2503 / 0.2360 | **fails** (named-other 0 of 3) | 0.1780 / 0.1830 / 0.1703 (reported) |
| F | 0.5597 / 0.5513 / 0.5547 | 0.3313 / 0.2603 / 0.2487 | **fails** (named-other 1 of 3) | 0.1760 / 0.1850 / 0.1940: **collapses** under page 1h on all three seeds |
| M | 0.8640 / 0.8613 / 0.8667 | 0.5543 / 0.5663 / 0.5517 | **passes** | 0.2230 / 0.2190 / 0.2203 (reported) |
| ownership-blind solver | 0.2340 / 0.2383 / 0.2340 | 0.2373 / 0.2420 / 0.2167 | fails, as a solver with no ownership signal should | — |

The name-only solver (computed, not trained) scores 1.0000 on named-other and
0.2380 on own-directed, as on 2026-09-21. **Arm T's gate figures reproduce the
2026-09-21 record exactly**, including the three lesioned figures
(`out/gate.json`).

**Under the ruled numbers the free arm would not be read**: it fails page 1b.
Its reading below is reported as the rehearsal reports everything, and is not a
reading the registered procedure would make.

### 6.2 The reading, chance-corrected (page 2), with the floor of page 1c

MEASURED, `out-repairs/measure_base_T_C.json`, `measure_base_F.json`,
`measure_base_M.json`, `summary_base.json`:

| arm | untouched | whole-state | ownership-only | reading (chance-corrected) | raw difference | spread across seeds of the raw difference (page 1g) | within-seed bootstrap |
|---|---|---|---|---|---|---|---|
| T, seeds 0 / 1 / 2 | 0.0000 × 3 | 1.0000 × 3 | 1.0000 × 3 | **0.0000 × 3** | 0.0000 × 3 | 0.0000 | 0.0000 |
| C | 0.049 to 0.060 | 0.50 to 0.59 | 0.052 to 0.060 | **0.99 to 1.00**, entangled end | 0.44 to 0.53 | 0.0466 | 0.0194 to 0.0203 |
| F | 0.056 to 0.069 | 0.485 to 0.568 | 0.056 to 0.069 | **1.00 to 1.003**, entangled end | 0.42 to 0.51 | 0.0499 | 0.0189 to 0.0202 |
| M | 0.012 to 0.018 | 0.75 to 0.79 | 0.38 to 0.39 | **0.48 to 0.53**, the middle | 0.35 to 0.41 | 0.0309 | 0.0167 to 0.0184 |

- **Every reading is valid under the floor**: on every arm and seed the
  whole-state transplant's room over the untouched rate clears four fifths of the
  arm's own room (`reading.floor` fields).
- **Separation (page 1a): arm C minus arm T is 0.9977, 0.9927 and 1.0000 on
  seeds 0, 1 and 2, all above 0.5** (`summary_base.json`, `separation`).
- **The chance-corrected reading can exceed 1.** The free arm at seed 0 reads
  1.0029, and the sensitivity pick on arm C seed 0 reads 1.0051, because the
  ownership-only transplant landed slightly *below* the untouched rate. That is
  sampling noise around "the subspace does nothing", but the registration should
  say a reading above 1 is reported as observed, not clipped, as page 2 already
  says of a negative one. ARGUED.
- **Page 1g, as ruled, reports the across-seed spread; the bootstrap is less
  than half of it on arms C and F.** On 2026-09-21 the two agreed closely
  (rehearsal findings, section 11: 0.0189 and 0.0227 against 0.0198 and 0.0203).
  Here the across-seed spread is 0.0466 and 0.0499. MEASURED; the ruling's
  sentence that neither method measures drift between runs of one seed stands.
- **The rank cap of 8 (page 1d) did not bind on arms C and F**: the rule chose
  ranks 1, 2 and 4 there, because no rank moves those arms (§3 table). On arms T
  and M it chose 8 on every seed.

### 6.3 The controls

MEASURED, `controls` fields in the `measure_base_*.json` files. Ranges across
the three seeds:

| control | T | C | F | M | what it should show |
|---|---|---|---|---|---|
| 1. the complement of the nominated subspace | 0.0000 | 0.50 to 0.57 | 0.49 to 0.56 | 0.36 to 0.42 | action follows content, not identity |
| 2. as the proposal states it | no verdict | no verdict | pass (weak, §4) | no verdict | own-directed action does not move |
| 3. a random subspace, same rank | 0.0000 | 0.049 to 0.063 | 0.059 to 0.071 | 0.013 to 0.056 | no donor action |
| 4. before the identity can be known | 0.0000 | 0.14 to 0.16 | 0.06 to 0.15 | 0.03 to 0.12 | nothing happens |
| 6a. same-value cell, share moved | 0.000 | 0.59 to 0.72 | 0.64 to 0.74 | 0.17 to 0.32 | nothing moves |
| 6b. different-value cell, share moved | 1.000 | 0.90 to 0.91 | 0.88 to 0.90 | 0.85 to 0.95 | everything moves |
| 7. null transplant, bit-identical | yes | yes | yes | yes | nothing changes |

Controls 1 and 6 behave as on 2026-09-21, and the two findings about them stand
(rehearsal findings, section 6): control 1 cannot hold on an entangled arm by
construction, and control 6's same-value cell moves in well over half the trials
on arms C and F.

**Control 4 is worth a second look. ARGUED.** A transplant before the identity
can be known moves the donor's action in up to 0.16 of trials on arms C and F,
against untouched rates near 0.05 to 0.07. At the nominated sites those arms
receive the ownership signal by other routes (C by its side route, F by the
acting channel added at the embedding), so "before the identity can be known" is
not the same as "before the state differs". It did not reach the pre-stated
"nothing happens" on those arms here. On 2026-09-21 it read 0.0650 on arm C and
0.0600 on the free arm at seed 0 (rehearsal findings, section 6, which prints
seed 0 only), close to their untouched rates, which suggests it depends on where
the rule looks.

### 6.4 The no-transplant rate against the review's formula

MEASURED, `no_transplant_rate_miss` fields: arm T misses by 0.0000; arm C by
−0.0132, −0.0111 and −0.0039; the free arm by −0.0043, −0.0057 and +0.0054. All
are inside the 0.0175 room page 2 asked the rule to carry.

---

## 7. What this means for the registration text (ARGUED; for session (d))

1. **Page 4 (d) applies**, with one sentence added: a curriculum and loss
   re-weighting also failed at toy scale, and both made the named-other condition
   worse. Whether to attempt redesign (c), a grammar change, is John's.
2. **The degenerate exclusion must cover every all-positions site set**, not
   only "every layer at every position" (§3).
3. **The site-list rule and the printed list must agree.** The rule gives 296
   on the toy and 1,816 on the registered model with the toy's position sets;
   the 176 is the hand list's (§3).
4. **"The smallest layer set that clears it" needs one reading in words**; the
   two readings disagree on 7 of 12 arm-and-seed pairs (§3).
5. **Control 2 as worded cannot be run on arms T and M, and gives no verdict on
   arms that have not learned the named-other condition** (§4).
6. **A chance-corrected reading above 1 is reported as observed** (§6.2).
7. **The rider stays in the reporting table**; on the toy it returns "no
   verdict" for every arm but T (§3).
8. **Arm M passed page 5's line**; folding it in is a page 5 and page 6 decision.

---

## 8. Where running it differed from planning it

1. **Two additions not pre-stated**, committed as code before their output in
   `81dc84d` and labelled so in the code: the named-other diagnostic (§2),
   written after the curriculum scored below one in four; and the sensitivity
   pick without all-positions sets (§3), written after arm C's nominations.
   Neither replaces a pre-stated quantity.
2. **The prediction's number was low** (§5): 0.42 to 0.43 predicted from the
   record, against 0.46 to 0.49 from the arm's own routes and 0.48 to 0.53
   measured. The band and the formula check held.
3. **The ownership-blind solver was trained on three seeds, not one** as on
   2026-09-21; the extra two cost nothing but time.
4. **`gate_base.json` was written twice**: once early on arms T and F only, then
   on every arm. The committed file is the second; its arm T and F rows match
   the first, which were quoted in this session's chat before the second run.
5. **Laptop time**: 21 training runs, 5.68 hours of training summed across them
   (`train_*.json`), in two parallel streams of 9,161 and 11,307 seconds of wall
   time (the local training logs, which are not committed). Within the four to
   six hours the method note estimated. $0.

---

## 9. What still needs John

| decision | what this session found | where |
|---|---|---|
| Whether to attempt page 4's redesign (c), a grammar change, or to let (d) stand | both training redesigns failed; the evidence points at the grammar giving both action turns the same acting signal | §2 |
| Whether arm M is folded into the main registration (page 5, with page 6's envelope, $32 to $44 for three runs) | it passed the pre-stated line on all three seeds | §5 |
| Widening the degenerate-set exclusion to every all-positions site set | the ruled exclusion let the rule pick a degenerate set on arm C | §3 |
| Which reading of "the smallest layer set that clears it" is registered | the two disagree on 7 of 12 pairs | §3 |
| How control 2 is worded, or recorded as not applicable on arms T and M | as worded it returns no verdict on three arms of four | §4 |
| The rented slice (page 9), unchanged | not touched by this session; its go has not been given | ruling page 9 |

Nothing here is ruled. The pairing rule applies: this file is checked by a
session that did not write it, on the checker prompt in
`docs/weekend-1-session-prompts.md`, section (c).
===== END OF RECORD 17 =====

===== RECORD 18 of 25 - the toy re-run under version 3's rules - `docs/2026-09-26-toy-rerun-v3-rules.md` (complete file, 39,408 characters) =====
# The toy re-run under the version 3 rules (RT-212 to RT-216) — findings

*Written 2026-09-26 (Pacific), on branch `worktree-w1d-toy-rerun-v3`, by the
Claude Code session commissioned as "MVM W1d toy re-run under v3 rules".
**UNREGISTERED.** Nothing here is a ruling. It applies the version 3 rules to the
toy's committed trained models and reports what they return.*

*This file has two parts. **Part 1** gives the results under the rules as they
now stand: the five rule changes John ruled on 2026-09-26 against the Gate C
review of version 2 (`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`,
RT-212 to RT-216), as amended by **his three rulings of the same day on this
file's first pass**. Those three rulings: control 3 is reported, not gated;
rule 4 removes the layer-0 site sets from the candidate family before choosing;
and the trained models are committed. John later changed the third: the models
are committed by the rulings session at commit `235c385`, not on this branch
(§1.1). **Part 2** is the first pass exactly as
first written (commit `5276731`), kept as the record and superseded where Part
1 differs.*

*Commit order. First pass: method `dc7eee8`, code `392477b`, outputs `6f9428b`,
findings `5276731`. Second pass: method addendum and dated correction `6e23dc1`
(`docs/toy-rerun-v3-rules-method-2026-09-26.md`, section 7 and the note in
section 3.4); the models `a86783e`; code `7a01026` (`--stage pass2` in
`experiments/rehearsal-successor-measure/src/rerun_v3.py`); outputs `dc1de9e`;
findings `f24d77a`. Then, after John's change to step 3: method note `29e9751`;
the models removed from this branch again `caa6ec3` (history not rewritten; the
pull request's net change carries no model files); code `8471a50`
(`--stage sums`); output `ed81fd3`; then this revision. Laptop only, no network, no rented machine, **$0**. No arm
was retrained in either pass.*

*Every claim is labelled **MEASURED** (read off a committed output file, cited
by path) or **ARGUED** (reasoning from those numbers or from the code). Paths
are relative to `experiments/rehearsal-successor-measure/out-v3-rules/` unless
written in full. Arms C, F and M do not reproduce from code and seed
(`docs/rulings/2026-09-23-range-and-direction-only.md`). Their figures describe
these particular trained models, and are reported as a range and a direction,
not as a property of the code. Written under the workspace plain-language rule.*

---

# Part 1 — Results under the rulings as they now stand

## 1.0 The answer, briefly

MEASURED, `pass2_summary.json` and `pass2_table.md`.

- **Arm M reads 0.4886, 0.4860 and 0.5449 on seeds 0, 1 and 2. The pass line of
  0.3 to 0.7 is met on all three seeds** (`arm_M_pass.met_on_every_seed: true`).
- **Arm C reads 1.0051, 1.0025 and 1.0000 on seeds 0, 1 and 2.** Arm T reads
  0.0000 on every seed. So **the separation figure, arm C minus arm T, is
  1.0051, 1.0025 and 1.0000, and it clears the 0.5 bar on every seed**
  (`separation`).
- **Arm F returns no verdict on each seed: 0, 1 and 2.** On every seed it fails
  twice over. Its gate fails (the named-other condition is learned on 1 seed of
  3), and its read fails the floor: 0.172, 0.067 and 0.106 at the nominated
  layer, against 0.8 (`arm_F`).
- Arm T reads 0.0000 on all three seeds under the primary rule and under the
  stricter layer-0 variant. The stricter variant moves its site from layer 0 to
  layer 1, both at the action position.
- The stricter variant changes nothing on arms C, F or M. None of their primary
  nominations contains layer 0 once rule 4 removes the injection sets.

ARGUED: under the rules as they now stand, the toy reaches the proposal's first
result on its anchors. The separable anchor reads 0 and the entangled anchor
about 1, with separation on every seed. The fourth arm lands inside its
pre-stated band on every seed, and the free arm is correctly returned as "no
verdict" rather than as a reading.

## 1.1 The trained models: committed, and what rests on them

**Where the models are.** The fifteen models are committed by the rulings
session, not by this branch: **commit `235c385`** on branch
`w1d-toy-models-committed`, at
**`experiments/rehearsal-successor-measure/out-repairs/models/`**, with a
`SHA256SUMS` list and a `README.md`. The commit was made under item 3 of
"Refinements 2026-09-26, after the toy re-run" in
`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`, and its pull request
was being opened as this was written. This branch had briefly committed its own
copy at the same path (`a86783e`). By John's change it removed that copy again
in a new commit (`caa6ec3`) rather than rewriting pushed history. The pull
request's net change therefore carries no model files, and does not collide
with `235c385`.

**The two records agree.** MEASURED, `models_sha256_check.json`
(`all_agree: true`), written by `--stage sums` in
`experiments/rehearsal-successor-measure/src/rerun_v3.py` from `235c385`'s
`SHA256SUMS`. For every model this session read, three hashes are compared:

- the hash the first pass recorded when it read the file in place in the repairs
  worktree (`nominate_*_seed*.json`, `checkpoint_sha256`; the first pass did not
  read the three blind-arm models);
- the hash the second pass recorded when it read the copy
  (`pass2_summary.json`, `model_sha256`);
- the line for that file in `235c385`'s `SHA256SUMS`.

All fifteen agree. The list has fifteen entries and no file this session did
not read. The first pass's checks K1 to K4 (Part 2, first pass §1) showed that
these are the models behind the committed repairs outputs.

| file | SHA-256 (this session's reads = `235c385` `SHA256SUMS`) |
|---|---|
| `ckpt_T_base_seed0.pt` | `b679bf6cd7884f28a137a6e6a669728213c085ba9cba5c9a2574b947885cfe68` |
| `ckpt_T_base_seed1.pt` | `1558acb2fce628335f28c3a29acef43fdf0d409151e1b5774d8e75aa7f489113` |
| `ckpt_T_base_seed2.pt` | `84f48372c995c7c53baa80d9379a3778bb8c1845e45589b743bd2b8c083c90c2` |
| `ckpt_C_base_seed0.pt` | `47326bb90c5f4ad03beacc74da1d33eec1fd4462314a2e9ce385c36a1e7ffeee` |
| `ckpt_C_base_seed1.pt` | `b3596f309e780e5820a7064ccb207a413a71be439170986b18479fe957e0af2a` |
| `ckpt_C_base_seed2.pt` | `2fc87d0454af22bc2d1c00b7247c220ff0705b8c2500005b47a9cb491ac202f0` |
| `ckpt_F_base_seed0.pt` | `c3afe0c6354f49f185b1806a433e6f0563b48a14f6e4559b2264ecb0abeea88d` |
| `ckpt_F_base_seed1.pt` | `2e51df7efd952e044b63702a5dc63c88e12de41ffe89c1b15c35892756cb219b` |
| `ckpt_F_base_seed2.pt` | `d5b59d8b8d32d42327beb4e6866107fe6e1167f4de1d0d73e3e201ed9d1683b1` |
| `ckpt_M_base_seed0.pt` | `e0f55d92d42bffdb3774cb267bbd8caf16f901fd3fa2f127e9989780188ceda2` |
| `ckpt_M_base_seed1.pt` | `d9b8010c9bec5ae20aaacabd38acd89497ef121599643a15d548ad44f688ecab` |
| `ckpt_M_base_seed2.pt` | `eeb3a7a43628791f1c85ac85d6108b74e89c0a209f1688c7342d864ce4926dba` |
| `ckpt_blind_base_seed0.pt` | `027f5ac0c78576e9263ad488ce18f0cb64070e5eeb89ff30e9a177294e25e162` |
| `ckpt_blind_base_seed1.pt` | `9b44cd386e6de0298a52355868652bdc9a9c0e3c3c4cd7af48485cc53ba9c3f5` |
| `ckpt_blind_base_seed2.pt` | `092393bdc1b488cfef7706a02804988bb4d672489bc0f332eada603d42f52ba6` |

**These files cannot be rebuilt from code and seed.** Retraining arms C, F or M
from the same code and seed gives a different model: the repairs check (pull
request 58) re-ran from clean and got different nominations. The toy results
listed below rest on these fifteen files and on nothing else.

**What rests on them.** The brief asked this file to say that *every*
committed toy result of 2026-09-25 and 2026-09-26 rests on these fifteen files.
That is not quite true, and this file says what is:

- **Rests on these files:** every base-recipe result of the rehearsal repairs
  in `experiments/rehearsal-successor-measure/out-repairs/`. That is
  `gate_base.json` (arms T, C, F, M and the ownership-blind arm),
  `nominate_base_*.json`, `measure_base_*.json`, `reads_*_base_*.npz` and
  `summary_base.json`, and the findings `docs/2026-09-26-rehearsal-repairs.md`
  built on them. It is also every file in `out-v3-rules/`, both passes, and this
  file.
- **Does not rest on these files:**
  - The two arm F training redesigns in `out-repairs/` (`gate_curriculum.json`,
    `gate_reweight.json`, and the curriculum and reweight rows of
    `diagnose_named_other.json`). They rest on six more models,
    `ckpt_F_curriculum_seed{0,1,2}.pt` and `ckpt_F_reweight_seed{0,1,2}.pt`,
    which are still untracked in the repairs worktree.
  - The grammar attempt, pull request 57 (`out-grammar-c/`). It rests on its own
    nine models, still untracked in the `w1c-grammar-attempt` worktree.
  - The repairs check, pull request 58. It retrained from clean, and this
    session did not look for its models.

ARGUED, for John: if the intent is that every toy result of the weekend has its
models on the record, those fifteen further files (about 75 MB) need the same
treatment. The `235c385` README lists the same gaps under "Not here".

## 1.2 The gate (rule 5, unchanged from the first pass)

MEASURED, `gate.json`. Arms T, C and M are gated on the own-directed condition
only; arm F on both conditions. The bar is 790 of 3,000 on at least two seeds
of three.

| arm | own-directed clears | named-other clears | gate |
|---|---|---|---|
| T | 3 of 3 | 3 of 3 | passes |
| C | 3 of 3 | 0 of 3 | passes |
| F | 3 of 3 | 1 of 3 | **fails** |
| M | 3 of 3 | 3 of 3 | passes |

## 1.3 The findings table

MEASURED, `pass2_table.md` (rows `primary`), with the underlying figures in
`measure_{arm}_seed{s}.json` (`rows.unruled_layer0_injection_removed`, read on
the 800 fresh episode pairs in the first pass),
`nominate_{arm}_seed{s}.json` and `null_{arm}_seed{s}.json`.

- The **site set** is the 60-set rule's nomination after rule 4 removes every
  layer-0 site set at a position set other than `action`.
- **Fit** is the read's held-out accuracy (180 development episodes) at the
  nominated layer.
- **Null** is the 95th and 99th percentile of 200 label-shuffled fits at that
  layer, beside the 0.8 floor, not as the bar.
- **Control 3** is the median and 95th percentile of the twenty random
  subspaces' donor shares. It is followed by the ownership-only donor share and
  how many of the twenty draws fall below, equal and above it. It is reported
  only and decides nothing.
- The **reading** is `(whole − ownership-only) / (whole − untouched)`: 0 is
  separable, 1 is entangled.

| arm/seed | site set (layer, position set, rank) | fit | null 95th / 99th | fit floor | control 3: median / 95th; ownership-only (below / equal / above) | reading or verdict |
|---|---|---|---|---|---|---|
| T/0 | 0, action, 8 | 1.000 | 0.117 / 0.133 | passes | 0.0000 / 0.0000; 1.0000 (20 / 0 / 0) | **0.0000** |
| T/1 | 0, action, 8 | 1.000 | 0.117 / 0.128 | passes | 0.0000 / 0.0000; 1.0000 (20 / 0 / 0) | **0.0000** |
| T/2 | 0, action, 8 | 1.000 | 0.111 / 0.128 | passes | 0.0000 / 0.0000; 1.0000 (20 / 0 / 0) | **0.0000** |
| C/0 | 2, action, 8 | 1.000 | 0.111 / 0.122 | passes | 0.0587 / 0.0639; 0.0488 (0 / 0 / 20) | **1.0051** |
| C/1 | 4, action, 2 | 0.961 | 0.122 / 0.139 | passes | 0.0550 / 0.0613; 0.0475 (0 / 1 / 19) | **1.0025** |
| C/2 | 1, post-identity, 1 | 0.978 | 0.117 / 0.128 | passes | 0.0600 / 0.0653; 0.0600 (3 / 9 / 8) | **1.0000** |
| F/0 | 1, post-identity, 1 | 0.172 | 0.128 / 0.133 | **fails** | 0.0587 / 0.0625; 0.0587 (6 / 7 / 7) | no verdict: gate failed; read failed its floor (number 1.0000) |
| F/1 | 1, action+3, 4 | 0.067 | 0.117 / 0.122 | **fails** | 0.0587 / 0.0650; 0.0563 (2 / 1 / 17) | no verdict: gate failed; read failed its floor (number 1.0000) |
| F/2 | 1, post-identity, 8 | 0.106 | 0.117 / 0.133 | **fails** | 0.0638 / 0.0664; 0.0638 (8 / 3 / 9) | no verdict: gate failed; read failed its floor (number 1.0108) |
| M/0 | 1, post-identity, 8 | 1.000 | 0.122 / 0.139 | passes | 0.0150 / 0.0190; 0.4050 (20 / 0 / 0) | **0.4886** |
| M/1 | 1, post-identity, 8 | 1.000 | 0.117 / 0.139 | passes | 0.0187 / 0.0226; 0.4062 (20 / 0 / 0) | **0.4860** |
| M/2 | 1, post-identity, 8 | 1.000 | 0.117 / 0.144 | passes | 0.0150 / 0.0213; 0.3688 (20 / 0 / 0) | **0.5449** |

Every row clears the whole-state four-fifths floor on fresh episodes
(`reading.floor.clears`). Control 7 (copying the recipient's own states changes
no output, bit for bit) holds on all twelve (`measure_*_seed*.json`,
`control7_null_transplant_bit_identical`).

**The stricter layer-0 row** (every layer-0 site set removed at every position
set, then choose again). MEASURED, `pass2_table.md`, rows `stricter`. It
differs from the table above only on arm T. Arm T's site moves from layer 0 to
**layer 1 at the action position, rank 8**, with fit 1.000, control 3
(20 / 0 / 0) and reading **0.0000** on all three seeds. On arms C, F and M the
primary nominations contain no layer 0, so the stricter row is identical.

## 1.4 What the control 3 distribution shows, now that it is reported

MEASURED, `pass2_table.md`. ARGUED where marked.

- **Arms T and M:** the ownership-only transplant sits above all twenty random
  draws on every seed, by a wide margin (arm M about 0.37 to 0.41 against random
  medians of 0.015 to 0.019). The ownership subspace does something that random
  subspaces of its size do not.
- **Arm C:** the ownership-only transplant sits **below** all twenty draws on
  seeds 0 and 1 (0 / 0 / 20 and 0 / 1 / 19), and in the middle of them on seed 2
  (3 / 9 / 8). ARGUED: this is what an entangled arm should show. Its ownership
  subspace carries nothing that moves the action on its own, no more than a
  random subspace does. The first pass's gate turned this into "no verdict"
  (Part 2, first pass §7); reported and not gated, it is simply the evidence
  that goes with a reading near 1.
- **Arm F:** the ownership-only transplant sits in the middle of the random
  draws on every seed (6 / 7 / 7, 2 / 1 / 17, 8 / 3 / 9). ARGUED: this is
  consistent with a read that holds nothing. Arm F's verdict comes from its
  fit, not from control 3.

## 1.5 What changed from the first pass, and why

MEASURED, comparing Part 1 with Part 2.

- **Rule 4.** In the first pass a layer-0 nomination at `post-identity` gave no
  verdict (6 of 12). Removing those site sets and choosing again moves every one
  of the six off layer 0:
  - C/1: to layer 4 at the action position, rank 2;
  - C/2 and F/0: to layer 1 at post-identity, rank 1;
  - F/2, M/0 and M/2: to layer 1 at post-identity, rank 8.

  C/0, F/1 and arm T are unchanged. M/1 also moves, from layer 3 at action to layer 1 at post-identity. Removing
  site sets changes which layer set is smallest per position set, and so which
  candidate has the highest ownership-only share. Its reading barely changes
  (0.4846 to 0.4860).
- **Control 3.** In the first pass it removed arm C seeds 0 and 2 and every arm
  F seed. Reported instead of gated, it removes nothing.
- **The net effect.** In the first pass: readings on arm T (3 of 3) and arm M
  (1 of 3), none on C or F, no separation figure. In the second pass: readings
  on T, C and M on every seed, separation on every seed, arm M inside its band
  on every seed, and arm F no verdict on every seed.
- **Unchanged:** the models, the reads, the fit floor, the permutation null,
  the 60-site-set family, the gate, and every fresh-episode figure. The second
  pass is arithmetic on the first pass's outputs. Every site set it reports was
  read on the fresh episodes by the first pass's code (method §7.2).

## 1.6 Things a checker should know

- The second pass ran no model. `--stage pass2` checks the models' hashes (it
  ran while this branch still held its own copy, which `--stage sums` later
  showed is byte-identical to `235c385`'s), then takes the nominations from `nominate_*` and the fresh-episode
  figures from `measure_*`. It asserts that each measure row read the site set
  the nomination names.
- The first pass's notes (Part 2, first pass §9) still apply. The CPU and GPU
  refits differ on four of sixty layer fits by one or two held-out episodes.
  One of those four is now a nominated layer, F/2 layer 1: 0.1056 on the GPU
  (the table's figure, equal to the committed one), 0.1000 on the CPU. Both are
  far below 0.8. The T/0 and T/1 null logs were lost when those processes were
  relaunched; their results files are complete.
- The method file's sentence about layer-0 transplants inside the action turn
  was wrong for arms T and M. It now carries a dated correction (method §3.4),
  and is not deleted.

## 1.7 Files (second pass)

- Method addendum: `docs/toy-rerun-v3-rules-method-2026-09-26.md`, section 7,
  with the dated change to item 3; the dated correction in section 3.4.
- Models: commit `235c385` (branch `w1d-toy-models-committed`),
  `experiments/rehearsal-successor-measure/out-repairs/models/`, with its
  `SHA256SUMS` and `README.md`; hashes in §1.1. Not on this branch.
- Code: `experiments/rehearsal-successor-measure/src/rerun_v3.py`, `stage_pass2`
  and `stage_sums`.
- Outputs: `out-v3-rules/pass2_table.md`, `out-v3-rules/pass2_summary.json`,
  `out-v3-rules/models_sha256_check.json`, `out-v3-rules/logs/pass2.log`,
  `out-v3-rules/logs/sums.log`. Every first-pass output is unchanged.

---

# Part 2 — The first pass, as first written (commit `5276731`), superseded where Part 1 differs

*Kept as the record, unedited apart from heading levels. Its section references
(§0 to §10) point within this part. Its rule 4 is "no verdict at the
injection", and its control 3 gates the reading. John's rulings of 2026-09-26
replaced both (Part 1). Its §6.2 "unruled" column is what Part 1 now reports as
the primary row.*

### First pass §0. The answer, briefly

- **Arm F returns no verdict on every seed under rule 1.** MEASURED: the read's
  held-out fit at the nominated layer is 0.072, 0.067 and 0.072 on seeds 0, 1
  and 2, against a floor of 0.8 (`measure_F_seed{0,1,2}.json`,
  `rows.primary.verdict.fit_accuracy`). Its best fit at any layer on any seed is
  0.172. Arm F also fails its gate (rule 5), and on every seed it fails control 3
  (rule 2); on two seeds of three it also sits at the acting channel's injection
  (rule 4). Any one of these alone gives no verdict.
- **Arm M clears control 3 on all three seeds under rule 2.** MEASURED: its
  ownership-only transplant moves the action to the donor's value in 0.3925,
  0.3937 and 0.3775 of trials, against a 95th percentile of twenty random
  subspaces of 0.0151, 0.0701 and 0.0139 (`measure_M_seed{0,1,2}.json`,
  `rows.primary.control3`). Seed 1, which failed version 2's form of control 3,
  passes this one by a wide margin.
- **But arm M gets a reading on one seed of three, not three, once all five rules
  apply.** MEASURED: seeds 0 and 2 nominate layer 0 at the post-identity position
  set, which rule 4 reports as "at the acting channel's injection", no verdict.
  Seed 1 reads 0.4846. So the pass John folded arm M in on ("between 0.3 and 0.7
  on all three seeds") is **not met under the rules as ruled**. It is met under
  one reading of rule 4 that the ruling did not choose (§6.2).
- **Arm C returns no verdict on every seed.** Seeds 1 and 2 sit at the injection
  with a read at 0.072; seed 0 has a sound read (1.000 at layer 2) and fails only
  control 3, because its ownership-only transplant (0.0488) moves no more than a
  random one (95th percentile 0.0639). The method file predicted exactly this
  before the run (method §3.2): **rule 2 as worded cannot give a reading to an
  arm that is truly entangled**, whatever its read.
- **Arm T reads 0.0000 on all three seeds** under the primary rules, and returns
  no verdict on all three under rule 4's stricter variant, because its nomination
  is layer 0 at the action position.
- So under the five rules the toy gives readings on arm T (3 of 3) and arm M (1
  of 3) only. **The separation bar (arm C's reading minus arm T's, at least 0.5)
  cannot be computed on any seed.**

### First pass §1. The models: never committed, still on disk, confirmed as the committed ones

MEASURED. The repairs driver's trained models (`ckpt_*_base_seed*.pt`) were never
committed: `git ls-files` lists no `.pt` file under
`experiments/rehearsal-successor-measure/` at `62c3824`. They survive, untracked,
in the repairs session's worktree on this laptop,
`~/Code/minimum-viable-mind/.claude/worktrees/w1c-rehearsal-repairs/experiments/rehearsal-successor-measure/out-repairs/`.
The re-run read them in place; each output records the file's SHA-256
(`nominate_*_seed*.json`, `checkpoint_sha256`).

Every pre-stated check held on all twelve arm-and-seed models (`summary.json`,
`checks`):

| check | what it compares | result |
|---|---|---|
| K1 | strict load into the arm definition | 12 of 12 load with no missing or unexpected weight |
| K2 | refitted reads against the committed `out-repairs/reads_*.npz` and fit accuracies | 12 of 12; largest coefficient difference **0.0**; fit accuracies equal at every layer (`nominate_*_seed*.json`, `K2`) |
| K3 | recomputed gate counts against `out-repairs/gate_base.json` | 12 of 12 equal, both conditions (`gate.json`, `K3`) |
| K4 | the 44-site-set nomination recomputed against the committed one | 12 of 12 pick the same position set, layer set and rank (`nominate_*_seed*.json`, `K4`) |
| extra | the committed nomination re-read on the fresh episodes against `out-repairs/measure_base_*.json` | 12 of 12 give the committed whole-state, ownership-only and untouched shares exactly |

So nothing was re-trained, and every figure below comes from the same models as
the committed repairs record. ARGUED, and a request for John: these fifteen
files are the only copies of models that cannot be reproduced from code and
seed. If the repairs worktree is cleaned up, they are gone. They are about 5 MB
each. Keeping them somewhere durable (not necessarily git) would protect every
toy result from this weekend.

### First pass §2. The gate under rule 5 (RT-213)

MEASURED, `gate.json`, `verdicts`. The bar is 790 correct of 3,000 held-out
development episodes, on at least two seeds of three.

| arm | rule | own-directed clears | named-other clears | version 2 (learn-both) | **rule 5** |
|---|---|---|---|---|---|
| T | own-directed only | 3 of 3 (3000, 3000, 3000) | 3 of 3 | passes | **passes** |
| C | own-directed only | 3 of 3 (1711, 1703, 1727) | 0 of 3 (760, 751, 708) | fails | **passes** |
| F | learn-both | 3 of 3 (1679, 1654, 1664) | 1 of 3 (994, 781, 746) | fails | **fails** |
| M | own-directed only | 3 of 3 (2592, 2584, 2600) | 3 of 3 (1663, 1699, 1655) | passes | **passes** |

Rule 5 changes one verdict, arm C's, from fail to pass. Arm F still fails.

### First pass §3. The findings table

Per arm and seed, on the 800 fresh episode pairs. "Fit" is the read's held-out
accuracy on 180 development episodes at the nominated layer (method §3.1);
"null" is the 95th / 99th percentile of 200 label-permuted fits at that layer.
"Control 3" is the ownership-only donor share against the 95th percentile of
twenty random subspaces. "Number" is the chance-corrected figure,
`(whole − ownership-only) / (whole − untouched)`, printed whether or not it is a
reading (0 = separable, 1 = entangled). Source: `table.md`, `measure_*_seed*.json`
(`rows.primary`), `nominate_*_seed*.json`, `null_*_seed*.json`.

#### First pass §3.1 The primary row: all five rules

| arm/seed | nominated site set | fit | null 95th / 99th | fit floor | control 3 | number | verdict |
|---|---|---|---|---|---|---|---|
| T/0 | layer 0, action, rank 8 | 1.000 | 0.117 / 0.133 | passes | 1.0000 vs 0.0000: beats | 0.0000 | **reading** |
| T/1 | layer 0, action, rank 8 | 1.000 | 0.117 / 0.128 | passes | 1.0000 vs 0.0000: beats | 0.0000 | **reading** |
| T/2 | layer 0, action, rank 8 | 1.000 | 0.111 / 0.128 | passes | 1.0000 vs 0.0000: beats | 0.0000 | **reading** |
| C/0 | layer 2, action, rank 8 | 1.000 | 0.111 / 0.122 | passes | 0.0488 vs 0.0639: does not beat | 1.0051 | no verdict: control 3 |
| C/1 | layer 0, post-identity, rank 8 | 0.072 | 0.111 / 0.122 | **fails** | 0.0550 vs 0.0514: beats | 0.9863 | no verdict: injection; read failed its floor |
| C/2 | layer 0, post-identity, rank 2 | 0.072 | 0.111 / 0.128 | **fails** | 0.0600 vs 0.0625: does not beat | 1.0000 | no verdict: injection; floor; control 3 |
| F/0 | layer 0, post-identity, rank 2 | 0.072 | 0.117 / 0.122 | **fails** | 0.0575 vs 0.0588: does not beat | 1.0029 | no verdict: gate; injection; floor; control 3 |
| F/1 | layer 1, action+3, rank 4 | 0.067 | 0.117 / 0.122 | **fails** | 0.0563 vs 0.0650: does not beat | 1.0000 | no verdict: gate; floor; control 3 |
| F/2 | layer 0, post-identity, rank 1 | 0.072 | 0.111 / 0.128 | **fails** | 0.0688 vs 0.0712: does not beat | 1.0000 | no verdict: gate; injection; floor; control 3 |
| M/0 | layer 0, post-identity, rank 8 | 1.000 | 0.117 / 0.133 | passes | 0.3925 vs 0.0151: beats | 0.5105 | no verdict: at the acting channel's injection |
| M/1 | layer 3, action, rank 8 | 1.000 | 0.117 / 0.133 | passes | 0.3937 vs 0.0701: beats | 0.4846 | **reading** |
| M/2 | layer 0, post-identity, rank 8 | 1.000 | 0.111 / 0.128 | passes | 0.3775 vs 0.0139: beats | 0.5322 | no verdict: at the acting channel's injection |

Every row also passes the whole-state four-fifths floor on fresh episodes, and
control 7 (copying the recipient's own states changes no output, bit for bit)
holds on all twelve (`measure_*_seed*.json`,
`control7_null_transplant_bit_identical`).

#### First pass §3.2 The two sensitivity rows

**Rule 3's row: the committed 44-set nomination, re-read under rules 1, 2, 4
and 5.** It differs from the primary row only where the nomination moved, which
is arm C seeds 0 and 1 (§5). On the other ten it is the primary row exactly.

| arm/seed | 44-set nomination | fit | null 95th / 99th | control 3 | number | verdict |
|---|---|---|---|---|---|---|
| C/0 (moved) | layer 0, every position, rank 2 | 0.072 | 0.117 / 0.122 | 0.0525 vs 0.0513: beats | 0.9977 | no verdict: injection; read failed its floor |
| C/1 (moved) | layer 0, every position, rank 4 | 0.072 | 0.111 / 0.122 | 0.0525 vs 0.0512: beats | 0.9927 | no verdict: injection; read failed its floor |

(Both of these site sets are now excluded outright by the widened exclusion of
the 2026-09-25 repairs ruling, item 3; they are shown because the brief asks what
moved.)

**Rule 4's stricter row: layer 0 excluded at every position set, action
included.** It differs from the primary row only on arm T, whose three
nominations are layer 0 at the action position:

| arm/seed | site set | number | primary verdict | **stricter verdict** |
|---|---|---|---|---|
| T/0, T/1, T/2 | layer 0, action, rank 8 | 0.0000 | reading | **no verdict: layer 0 excluded** |
| every other arm and seed | as §3.1 | as §3.1 | as §3.1 | as §3.1 (the layer-0 reason is relabelled; nothing else changes) |

MEASURED, `measure_T_seed*.json`, `rows.stricter`. So under the stricter
variant, **no arm gets a reading on more than one seed**: arm T none, arm M one
(seed 1).

### First pass §4. Rule 1: the fit floor and its permutation null (RT-212)

MEASURED, `null_*_seed*.json` and `nominate_*_seed*.json` (`fit_accuracy`).

- **The floor does what RT-212 asked.** It returns no verdict on every arm F
  seed and on the committed arm F reads, and it passes on the nominated read of
  every arm T and arm M seed (1.000 at every layer) and on arm C wherever arm C's
  nomination is off layer 0 (0.961 to 1.000 at layers 1 to 4). This is the
  closure test the review set out ("returns no verdict on the committed arm F
  reads and a reading on T, C and M"), met for T and M. For C the floor passes
  where the read sits at layers 1 to 4, but C gets no reading, for other reasons
  (§3.1).
- **The permutation null sits at about 0.11 to 0.12 (95th percentile) and 0.12
  to 0.14 (99th) at every layer of every arm.** With 12 marker words present
  among the 600 development episodes and 180 held out, that is the level a read
  reaches by chance.
- **On arm F the read finds something, just very little.** Arm F's fit beats the
  99th percentile of its null at some layers: seed 0 layer 1 (0.172 against
  0.133) and layer 2 (0.144 against 0.133), seed 2 layer 2 (0.139 against 0.122),
  seed 1 layer 3 (0.144 GPU refit / 0.133 CPU refit, against 0.133). ARGUED: so
  the permutation null alone, used as the bar, would have let arm F's read
  through at those layers. The floor at four fifths is what separates a read
  that has found the label (0.96 to 1.00) from one that has found a trace of it
  (at most 0.172). The ruling's choice to report the null beside the floor and
  not as the bar is borne out.
- **At layer 0 on arms C and F the fit is 0.072 on every seed, below the null's
  median.** ARGUED: at layer 0 the action position's state is the same in every
  episode on those arms (the mask token plus its position), so the read can only
  guess one word. A permuted read does better by chance because permuting varies
  which word is most common in each part of the split. Either way, the read at
  that site holds nothing.

### First pass §5. Rule 3: the registered site-set rule (RT-215)

MEASURED, `nominate_*_seed*.json`.

- **The family is 60 site sets, 240 comparisons per arm and seed.** The widened
  exclusion removes none of the 60: none of the four named position sets covers
  every position in any of the 600 development episodes
  (`family.share_of_episodes_where_position_set_spans_every_position`: 0 for
  all four; 1 for "all", which is not in the 60).
- **Two nominations of twelve moved**, both on arm C, both away from an "every
  position" set that the new family no longer contains:
  - C/0: layer 0 at every position, rank 2 → **layer 2 at the action position,
    rank 8**;
  - C/1: layer 0 at every position, rank 4 → **layer 0 at post-identity, rank 8**.
- The other ten are unchanged. **None of the 24 site sets the hand list never
  ran (the multi-layer sets (0,1), (1,2), (2,3), (0,1,2), (1,2,3) and (0,1,2,3))
  was nominated.** ARGUED: this is because every smallest clearing layer set is
  a single layer, as the review expected.
- The new sets do change the repairs file's other sensitivity row (highest
  ownership-only share over every clearing set, skipping the smallest-layer-set
  step), which now picks a multi-layer set on five of twelve: C/1 (0,1,2), C/2
  (0,1), F/1 (1,2,3), M/0 (0,1) and M/2 (0,1)
  (`sensitivity_v60_highest_over_every_clearing_set`). It is kept in the output
  files, not the table.
- How many of the 60 site sets clear the whole-state floor on development
  episodes: arm T 60 of 60; arm C 51, 39, 51; arm F 42, 39, 42; arm M 42, 42, 42
  (`site_sets_clearing_of_60`).

### First pass §6. Rule 4: layer 0 (RT-216)

#### First pass §6.1 As ruled

MEASURED, `measure_*_seed*.json`, `rows.primary.verdict.reasons`.

- **Six nominations of twelve are "at the acting channel's injection"**: C/1,
  C/2, F/0, F/2, M/0, M/2, all at layer 0 post-identity. That is the same six
  the review counted.
- **Three nominations are layer 0 at the action position and are allowed**: T/0,
  T/1, T/2. They are the whole of arm T's readings.
- **The method file's argument about layer 0 inside the action turn was half
  wrong**, and is corrected here. The method argued (ARGUED, method §3.4) that at
  the `action+ans` and `action+3` position sets the twins' layer-0 states are
  identical, so a layer-0 transplant there cannot move anything. The check shows
  this holds on arms C and F, and **not on arms T and M**
  (`layer0_whole_equals_untouched_inside_action_turn`: true on C and F, false on
  T and M). ARGUED: arms T and M build their ownership slot into the layer-0
  state at every position from the acting channel, so the twins differ there
  too. This changes no nomination, because no nomination is layer 0 at those two
  position sets. The literal ruling (layer 0 allowed at `action` only) was
  applied either way.

#### First pass §6.2 The reading the ruling did not choose, for John

The ruling says a layer-0 nomination at those position sets "is excluded and
reported as 'at the acting channel's injection', no verdict". The method
(§3.4) read that as: the arm and seed gets no verdict, and the rule does not go
on to choose a different site. The other possible reading is that those site
sets are removed from the family before choosing. The code recorded that second
reading as an unruled column (`rows.unruled_layer0_injection_removed`). MEASURED,
and not a result of the ruled rules:

| arm/seed | pick with those sets removed first | number | verdict under rules 1, 2, 5 |
|---|---|---|---|
| M/0 | layer 1, post-identity, rank 8 | 0.4886 | reading |
| M/1 | layer 1, post-identity, rank 8 | 0.4860 | reading |
| M/2 | layer 1, post-identity, rank 8 | 0.5449 | reading |
| C/0 to C/2 | layer 2 action / layer 4 action / layer 1 post-identity | 1.0051 / 1.0025 / 1.0000 | no verdict: control 3 on all three |
| F/0 to F/2 | layer 1 in each case | 1.0000 / 1.0000 / 1.0108 | no verdict: gate; floor; control 3 |
| T/0 to T/2 | unchanged (layer 0, action) | 0.0000 | reading |

ARGUED: under this second reading arm M gets readings of 0.486 to 0.545 on all
three seeds, all inside the pre-stated 0.3 to 0.7, one layer past the injection.
(M/1's pick changes too, from layer 3 action to layer 1 post-identity, because
removing sets changes which site set is smallest per position set; both give
about 0.49.) Arm M's ruled pass therefore turns on which reading of rule 4 is
meant. That is John's call, and this file does not make it. With every layer-0
set removed at every position (the stricter variant under the second reading,
`rows.unruled_every_layer0_removed`), arm T moves to layer 1 at the action
position and still reads 0.0000 on all three seeds, and arm M is as above.

### First pass §7. Rule 2: control 3 as a twenty-draw null (RT-214)

MEASURED, `measure_*_seed*.json`, `rows.primary.control3`.

- **Arm M clears it on all three seeds**, by a wide margin (§0). On seed 1 the
  twenty random subspaces reach up to 0.0713 of trials (95th percentile 0.0701),
  so version 2's single random draw (0.05625, reproduced here exactly as
  `single_draw_as_repairs`) was not unusual for that site. Under version 2's
  form (random at most untouched plus 0.0175, i.e. 0.0350) seed 1 still fails
  (`version2_form_passes: false`). ARGUED: version 2's limit was too tight for a
  site where random subspaces move something. The multi-draw null measures what
  random subspaces do at that site, which is the point of RT-214.
- **Arm T clears it on all three seeds**: ownership-only 1.0000, and none of the
  twenty random subspaces moves anything (0.0000).
- **Arm F fails it on all three seeds**: ownership-only 0.0563 to 0.0688, never
  above the random 95th percentile (0.0588 to 0.0712).
- **Arm C fails it on seeds 0 and 2 and passes on seed 1 by 0.0036** (0.0550
  against 0.0514; about three trials of 800). ARGUED: seed 1's pass is noise, not
  evidence; its read at that site fits at 0.072.
- **The consequence the method stated before the run happened.** Arm C seed 0
  has a sound read (1.000 at layer 2), a whole-state transplant that clears its
  floor (0.5400 against untouched 0.0512), and an ownership-only transplant that
  moves the action no more than untouched does (0.0488). That is what an
  entangled arm is supposed to look like, and it is the only arm C seed that
  passes every other rule. Rule 2 as worded gives it no verdict, because it
  requires the ownership-only transplant to beat random subspaces, which an
  entangled arm's cannot do. ARGUED: as worded, rule 2 makes the high anchor
  unreadable by design. It fits a separable or partly separable arm (T, M), where
  the ownership-only transplant should move things. A form that suits both would
  compare against the random null in the direction the arm is expected to go, or
  would require the random subspaces to be inert rather than requiring the
  ownership subspace to beat them. That is a design question for John; nothing
  here rewords the rule.

### First pass §8. What this leaves, per arm

| arm | gate (rule 5) | readings under all five rules | range of the chance-corrected number, all seeds | direction |
|---|---|---|---|---|
| T | passes | **3 of 3**: 0.0000 each (none under the stricter variant) | 0.0000 exactly | separable, as built |
| C | passes | **0 of 3** | 0.986 to 1.005 | entangled, as built, but no seed certifies it |
| F | fails | **0 of 3** | 1.000 to 1.003 | not a reading: the read finds no label (at most 0.172) |
| M | passes | **1 of 3** (seed 1: 0.4846) | 0.485 to 0.532 | partly separable, as built; 3 of 3 under the unruled reading of rule 4 (0.486 to 0.545) |

MEASURED from §3 and §6.2. ARGUED, what it means for version 3:

1. Under the rules as ruled, the toy does not reach the proposal's first result
   (every arm read and the separation bar met). Arm C, the high anchor, gets no
   reading on any seed, so the separation bar is not computable.
2. Two rules decide most of this, and neither is about the system being
   measured. Rule 2 blocks arm C's one clean seed, and rule 4's reading
   (no verdict, or remove and choose again) decides whether arm M passes. Both
   are wording questions that can be settled before Gate A at $0.
3. Rule 1 is the rule that works as intended on the toy: it retires arm F's
   empty reading and leaves the anchors alone.

### First pass §9. Things a checker should know

- **The null stage's refit ran on the CPU, the nomination's on the GPU.** Four
  of the sixty per-layer fit accuracies differ between the two by one or two of
  180 held-out episodes: F/0 layer 1 (0.1722 GPU, 0.1778 CPU), F/1 layer 3
  (0.1444, 0.1333), F/2 layer 1 (0.1056, 0.1000) and M/0 layer 3 (0.9889,
  0.9944). MEASURED, comparing `nominate_*` `fit_accuracy` with `null_*`
  `layers.*.fit_accuracy`. The table uses the GPU figures, which equal the
  committed ones (K2). None is at a nominated layer that crosses 0.8. The
  permutation nulls were fitted on the CPU states.
- **The null for T/0 and T/1 was produced by a first pair of processes that ran
  too slowly and was stopped**. Their results files were complete and are kept.
  Their logs were not, because the combined logs were removed when the remaining
  ten arm-and-seed runs were relaunched one process each. The draws are seeded
  by seed and layer (method §3.1), so re-running `--stage null --arms T --seeds 0,1`
  reproduces them on the same machine.
- **Not re-run**: control 2, controls 1 and 4 to 6, the rider, the oracle and
  arm M's route prediction (method §2). Their committed figures in
  `out-repairs/` stand.
- **Wall time**: about 40 minutes of nomination on the GPU and about 30 minutes
  of permutation nulls in ten CPU processes, after a slow first attempt; $0.

### First pass §10. Files

- Method: `docs/toy-rerun-v3-rules-method-2026-09-26.md`
- Driver: `experiments/rehearsal-successor-measure/src/rerun_v3.py`
- Outputs, under `experiments/rehearsal-successor-measure/out-v3-rules/`:
  `gate.json` (rule 5, K3); `nominate_{arm}_seed{s}.json` (the 75-site-set grid,
  the 60- and 44-set nominations, the unruled picks, K2, K4, checkpoint hashes);
  `null_{arm}_seed{s}.json` (200 permuted fits per layer);
  `measure_{arm}_seed{s}.json` (every row, reading, control 3 with its twenty
  draws, verdict reasons, control 7); `table.md` and `summary.json` (assembled);
  `logs/`.
===== END OF RECORD 18 =====

===== RECORD 19 of 25 - the controls re-run under the registered rules (source of every toy figure in version 4) - `docs/2026-10-03-controls-rerun.md` (complete file, 17,322 characters) =====
# The controls re-run under the registered rules: findings

*Written 2026-10-03 (Pacific) by the Claude Code session that ran it, on
branch `controls-rerun-2026-10-03`. The method,
`docs/controls-rerun-method-2026-10-03.md`, and the code,
`experiments/rehearsal-successor-measure/src/rerun_controls.py`, were
committed and pushed with no output at `f2d836b`, before the run. The code
was not changed between that commit and the run. Laptop, processor only.
Nothing rented, nothing trained, nothing spent: $0.*

*Written under the workspace plain-language rule. Every figure below is
**MEASURED**: it is in the output files under
`experiments/rehearsal-successor-measure/out-controls-rerun/`, and the table
is the script's own. Sentences that explain a figure are marked **ARGUED**.
This is a rehearsal record on twelve particular trained toy models. Figures
for the entangled, free and mixed models (arms C, F and M) are properties of
those models, not of the code
(`docs/rulings/2026-09-23-range-and-direction-only.md`).*

*This session also wrote the review, the ruling packet and the ruling record
this run follows from. It is owed a check by a session that did not write or
run it, which re-runs the script from the committed code.*

## 1. The short version

- **No stop fired.** Every model file matched its committed fingerprint; the
  null transplant left every output bit-identical at every site set; every
  built model read on every seed; the free model read on none.
- **The ruled change works on the toy.** With only pieces that themselves
  carry the label allowed, arm T (separable) reads 0.0000 on every seed, arm
  C (entangled) reads **1.0051, 0.9926 and 0.9974**, and arm M (mixed) reads
  0.4886, 0.4860 and 0.5449. The separation between arm C and arm T clears 0.5
  on every seed. Arm F (free) returns "no verdict, read failed its floor" on
  every seed: its best piece is right on 34 of 180 held-out episodes against
  144 needed.
- **One prediction of this session's was wrong.** On arm C seed 1 the method
  file predicted layer 4 at the action position; the rule chose layer 1 at
  the action position and the three before it. Section 3.
- **Two things go to John.**
  1. **Control 2, the other-agent control, has no figure on any toy model,
     and cannot have one.** The one model that learned the other-agent
     condition (arm F seed 0) has a read of the named agent's marker that
     misses the floor (at best 137 of 180 for the whole read). Its tolerance
     of 0.05, ruled on 2026-10-03, has therefore never been exercised.
     Section 5.
  2. **Control 4, the too-early-position control, comes back above "nothing"
     on six of twelve models, and an after-the-fact diagnostic says the
     cause is the control and not the models.** It transplants at positions
     before the *recipient's* first own turn; in about half the pairs the
     donor twin's first own turn comes earlier, so the donor's state there
     already carries who the donor is. Restricted to positions before both
     twins' first own turns, the control returns exactly the no-transplant
     rate on all twelve. That diagnostic was not pre-stated. Section 6.

## 2. The run

```
$ cd experiments/rehearsal-successor-measure/src
$ ../../../.venv/bin/python rerun_controls.py
...
done in 967s
```

torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, on the processor. The script's
table, as it printed it (also `out-controls-rerun/table.md`). "Whole read /
piece" is the count correct of 180 held-out development episodes, for the
whole straight-line read and for the transplanted piece. For arm F the site
set shown is the one the rule would choose with the piece requirement switched
off, as the method's rule 12 says, and its number is in parentheses and is
not a reading.

| arm/seed | status | site set | whole read / piece, correct of 180 | whole, ownership-only, untouched | reading | control 1 complement | control 3 median, 95th; below/equal/above | control 4 share (minus untouched) | control 6 same moved (n), different moved (n) | control 7 | control 2 | true slot | rider |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T/0 | nominated | layers (0,) at action, 8 directions | 180 / 180 | 1.0000, 1.0000, 0.0000 | 0.0000 | 0.0000 (holds: True) | 0.0000, 0.0000; 20/0/0 | 0.0000 (+0.0000) | 0.0000 (81), 1.0000 (719) | identical | not applicable | 0.0000 | 0.0000 (whole 1.0000) |
| T/1 | nominated | layers (0,) at action, 8 directions | 180 / 180 | 1.0000, 1.0000, 0.0000 | 0.0000 | 0.0000 (holds: True) | 0.0000, 0.0000; 20/0/0 | 0.0000 (+0.0000) | 0.0000 (81), 1.0000 (719) | identical | not applicable | 0.0000 | 0.0000 (whole 1.0000) |
| T/2 | nominated | layers (0,) at action, 8 directions | 180 / 180 | 1.0000, 1.0000, 0.0000 | 0.0000 | 0.0000 (holds: True) | 0.0000, 0.0000; 20/0/0 | 0.0000 (+0.0000) | 0.0000 (81), 1.0000 (719) | identical | not applicable | 0.0000 | 0.0000 (whole 1.0000) |
| C/0 | nominated | layers (2,) at action, 8 directions | 180 / 180 | 0.5400, 0.0488, 0.0512 | 1.0051 | 0.5450 | 0.0587, 0.0639; 0/0/20 | 0.0537 (+0.0025) | 0.5062 (81), 0.8220 (719) | identical | no verdict |  | no verdict (whole 0.0512) |
| C/1 | nominated | layers (1,) at action+3, 8 directions | 177 / 172 | 0.5550, 0.0525, 0.0488 | 0.9926 | 0.5625 | 0.0550, 0.0575; 6/1/13 | 0.0500 (+0.0013) | 0.6296 (81), 0.8860 (719) | identical | no verdict |  | no verdict (whole 0.0488) |
| C/2 | nominated | layers (1,) at post-identity, 4 directions | 176 / 150 | 0.5463, 0.0612, 0.0600 | 0.9974 | 0.5312 | 0.0612, 0.0663; 6/5/9 | 0.1313 (+0.0713) | 0.5679 (81), 0.9138 (719) | identical | no verdict |  | no verdict (whole 0.0600) |
| F/0 | read failed its floor: no size's piece reaches four fifths | layers (1,) at post-identity, 1 directions | 32 / 22 | 0.4850, 0.0587, 0.0587 | (1.0000) reported for description; no reading | 0.4838 | 0.0587, 0.0625; 6/7/7 | 0.1375 (+0.0788) | 0.7284 (81), 0.8999 (719) | identical | no verdict |  | no verdict (whole 0.0587) |
| F/1 | read failed its floor: no size's piece reaches four fifths | layers (1,) at action+3, 4 directions | 12 / 17 | 0.5675, 0.0563, 0.0563 | (1.0000) reported for description; no reading | 0.5637 | 0.0587, 0.0650; 2/1/17 | 0.0612 (+0.0050) | 0.6790 (81), 0.8790 (719) | identical | no verdict |  | no verdict (whole 0.0563) |
| F/2 | read failed its floor: no size's piece reaches four fifths | layers (1,) at post-identity, 8 directions | 18 / 18 | 0.5300, 0.0638, 0.0688 | (1.0108) reported for description; no reading | 0.5400 | 0.0638, 0.0664; 8/3/9 | 0.1338 (+0.0650) | 0.6296 (81), 0.8915 (719) | identical | no verdict |  | no verdict (whole 0.0688) |
| M/0 | nominated | layers (1,) at post-identity, 8 directions | 180 / 180 | 0.7800, 0.4050, 0.0125 | 0.4886 | 0.3875 | 0.0150, 0.0190; 20/0/0 | 0.1138 (+0.1013) | 0.2222 (81), 0.9499 (719) | identical | not applicable | 0.4837; formula 0.4837 | no verdict (whole 0.4088) |
| M/1 | nominated | layers (1,) at post-identity, 8 directions | 180 / 180 | 0.7738, 0.4062, 0.0175 | 0.4860 | 0.3762 | 0.0187, 0.0226; 20/0/0 | 0.0975 (+0.0800) | 0.2716 (81), 0.9360 (719) | identical | not applicable | 0.4760; formula 0.4760 | no verdict (whole 0.4138) |
| M/2 | nominated | layers (1,) at post-identity, 8 directions | 180 / 180 | 0.7937, 0.3688, 0.0138 | 0.5449 | 0.4288 | 0.0150, 0.0213; 20/0/0 | 0.0988 (+0.0850) | 0.3210 (81), 0.9485 (719) | identical | not applicable | 0.4920; formula 0.4920 | no verdict (whole 0.4100) |

separation, arm C minus arm T: {"0": {"C_minus_T": 1.0051150895140666, "clears_0_5": true}, "1": {"C_minus_T": 0.9925925925925926, "clears_0_5": true}, "2": {"C_minus_T": 0.9974293059125964, "clears_0_5": true}}

## 3. The nomination under the ruled change

| Arm and seed | Expected (method, section 4) | What the rule chose | Piece, correct of 180 |
|---|---|---|---|
| T, every seed | layer 0, `action`, 8 directions | the same | 180 |
| M, every seed | layer 1, `post-identity`, 8 directions | the same | 180 |
| C seed 0 | layer 2, 8 directions | layer 2, `action`, 8 directions | 180 |
| C seed 1 | **layer 4**, 8 directions | **layer 1, `action+3`, 8 directions** | 172 |
| C seed 2 | layer 1, 4 directions | layer 1, `post-identity`, 4 directions | 150 |
| F, every seed | no size reaches four fifths | the same | at most 34 |

**The miss on arm C seed 1.** This session had assumed the site would stay
where the proposal's rule put it (layer 4 at the action position) and only the
size would change. The candidates are one layer set per position set, and
once the small pieces are excluded the highest development ownership-only
share is 0.0533 at layer 1, 8 directions, at both `action+3` and
`post-identity`, against 0.0517 at layer 4, 8 directions, at `action`
(`out-controls-rerun/nominate_C_seed1.json`, `candidates`). The tie goes to
the earlier position set. Those shares differ by one episode of 600: on an
arm where nothing moves the action, the choice among candidates is still made
among sampling noise, as the review's finding RT-235 says. What the ruled
change fixes is that whichever candidate wins, its piece carries the label.
The reading at the chosen site is 0.9926; at layer 4 it would have been
0.9975 (the review, finding RT-230).

**One thing the rule as run does not check.** On arm C seeds 1 and 2 the
chosen position set covers several positions, and the piece's accuracy is
taken at the action position only (the method's rule 7, this session's
reading). The review measured the one-direction piece on seed 2 at the other
positions and found it far lower there. The 4- and 8-direction pieces were
not measured at the other positions in this run.

**The free arm on the processor.** Its whole read is right on 32, 12 and 18 of
180 at the layers shown, and no piece at any layer of any seed exceeds 34
(`nominate_F_seed*.json`, `fits`). The committed figures from the graphics
chip were 31, 12 and 19 (0.172, 0.067, 0.106).

## 4. The controls that came back as expected

- **Control 7, the null transplant (holds):** bit-identical on all twelve
  primary site sets, on the nine stricter-row site sets, and on arm F's three
  described ones (`measure_*_seed*.json`, `controls.7`).
- **The no-transplant rule (holds):** inside the 0.018 allowance on all
  twelve. The largest miss is 0.0132, arm C seed 0.
- **Control 1, the complement of the piece (holds on arm T):** arm T 0.0000
  on every seed. Arm C: 0.5450, 0.5625 and 0.5312 against whole-state shares
  of 0.5400, 0.5550 and 0.5463, so the complement does about what the whole
  state does, as expected of an entangled model. Arm M: 0.3875, 0.3762 and
  0.4288 against 0.78; about half, which is what a mixture would give (ARGUED).
- **Control 3, twenty random pieces (reported):** arms T and M above all
  twenty on every seed; arm C below all twenty on seed 0 and among them on
  seeds 1 and 2; arm F among them.
- **Control 6, on the relaxed set (reported):** both cells have trials, 81
  and 719. Arm T moves nothing in the same-value cell and everything in the
  other. The same-value cell moves on arm C (0.51 to 0.63), arm M (0.22 to
  0.32) and arm F (0.63 to 0.73), as the proposal's weakness W11 expects: on
  those models the whole-state transplant carries more than who is acting.
- **The true-slot reference:** arm T 0.0000; arm M 0.4837, 0.4760 and 0.4920,
  the route formula agreeing to four decimals, and the blind reading within
  0.10 of it on every seed (0.0049, 0.0100, 0.0529).
- **The rider:** at arm T's site set, arms C and F return no verdict with the
  whole-state transplant at the no-transplant rate, and arm M returns no
  verdict with about 0.41 moved, the two different reasons the proposal
  describes.
- **The stricter row** changes only arm T, to layer 1, still 0.0000.
- **The whole-state floor on fresh episodes** clears on all twelve.

## 5. Control 2 has no figure, on any model

The method expected it to run on arm F seed 0 only. It did not run there
either.

```
F/0 control 2: status 'no verdict', reason "read failed its floor: no size's piece reaches four fifths",
               named_other_correct 994, dev_named_other_accuracy 0.3217, dev_untouched 0.1933
named read, correct of 180, whole read then pieces of 1 / 2 / 4 / 8 directions:
  layer 0:  16 | 20 / 16 / 16 / 16
  layer 1:  95 | 22 / 43 / 74 / 92
  layer 2: 137 | 40 / 64 / 96 / 139
  layer 3: 127 | 31 / 50 / 79 / 115
  layer 4: 102 | 38 / 51 / 67 / 102
```

(`out-controls-rerun/measure_F_seed0.json`, `control2`.) The straight-line
read of the named agent's marker at the other-agent action never reaches 144
of 180: at best 137 for the whole read, at layer 2. So this is not an effect
of the ruled change. Under the proposal's earlier rule, with the floor on the
whole read, it would also have returned no verdict.

The other eleven: arms T and M are not applicable by ruling; arm C on every
seed and arm F seeds 1 and 2 have not learned the other-agent condition (760,
751, 708, 781 and 746 of 3,000 against 790).

**Why this goes to John.** Control 2 is frozen by the registration with a
tolerance of 0.05. Item 5 of the ruling of 2026-09-21 makes a pre-stated
quantity the rehearsal never exercised a fatal finding at the registration
review. This run was meant to exercise it and has shown that the toy cannot.
The options, none of them this session's to take: register control 2 as a
reported control whose no verdict is expected, saying in terms that it was
never exercised at toy scale; drop it; or exercise it on a made-up case
built for the purpose.

## 6. Control 4 comes back above nothing, and why

As run, control 4 is above the no-transplant rate by 0.065 to 0.10 on arm M
(every seed), arm C seed 2 and arm F seeds 0 and 2, and by 0.005 or less on
the rest. Those six are exactly the ones whose site set is layer 1 at the
`post-identity` position set, which reaches back to the model's first own
turn.

**After the output was seen**, this session wrote a diagnostic,
`src/posthoc_control4.py`. **It was not pre-stated**, it changes nothing in
the re-run, and it is labelled post hoc in its own first line.

```
$ ../../../.venv/bin/python posthoc_control4.py
pairs where the donor's first own turn comes before the recipient's: 0.5088
arm/seed | layers | untouched | control 4 as run | positions before both twins' first own turn
T/0 | (0,) | 0.0000 | 0.0000 (+0.0000) | 0.0000 (+0.0000)
T/1 | (0,) | 0.0000 | 0.0000 (+0.0000) | 0.0000 (+0.0000)
T/2 | (0,) | 0.0000 | 0.0000 (+0.0000) | 0.0000 (+0.0000)
C/0 | (2,) | 0.0512 | 0.0537 (+0.0025) | 0.0512 (+0.0000)
C/1 | (1,) | 0.0488 | 0.0500 (+0.0013) | 0.0488 (+0.0000)
C/2 | (1,) | 0.0600 | 0.1313 (+0.0713) | 0.0600 (+0.0000)
F/0 | (1,) | 0.0587 | 0.1375 (+0.0788) | 0.0587 (+0.0000)
F/1 | (1,) | 0.0563 | 0.0612 (+0.0050) | 0.0563 (+0.0000)
F/2 | (1,) | 0.0688 | 0.1338 (+0.0650) | 0.0688 (+0.0000)
M/0 | (1,) | 0.0125 | 0.1138 (+0.1013) | 0.0125 (+0.0000)
M/1 | (1,) | 0.0175 | 0.0975 (+0.0800) | 0.0175 (+0.0000)
M/2 | (1,) | 0.0138 | 0.0988 (+0.0850) | 0.0138 (+0.0000)
```

The control transplants the donor twin's state at the positions before the
recipient's first own turn. The twins are different agents, and in 0.5088 of
pairs the donor's first own turn is the earlier one, so at some of those
positions the donor's state already carries the donor's identity. With the
positions restricted to those before both twins' first own turns, the control
returns exactly the no-transplant rate on all twelve models.

**What that suggests (ARGUED, and John's to rule).** The proposal's account,
that arms C and F "receive the ownership signal by other routes", is not what
the diagnostic shows; the control was transplanting at positions where the
identity is already known, in the donor. Defined on both twins, control 4
does what it was written to do. John ruled on 2026-10-03 (the proposal's
decision 16) that it is reported and cannot veto, on the earlier account.
Whether to redefine its positions, and whether it could then hold again, is a
new question for him. The diagnostic is one after-the-fact run and is owed
the same check as the rest.

## 7. Against the method's stops

| Stop | Fired? |
|---|---|
| K1, a model file does not match its fingerprint | No |
| K2, the null transplant fails anywhere | No |
| K3, an arm T, C or M seed returns no verdict | No |
| K4, arm F reads on any seed | No |

## 8. What this run does and does not settle for the registration review

**Settled, subject to the check:** under the registered rules with the ruled
change, controls 1, 3, 4, 6 and 7 have figures on every arm and seed; the
readings and the separation hold; arm M's true-slot check holds.

**Not settled:** control 2 (section 5); control 4's definition (section 6);
whether a multi-position piece should be checked at every position it is
transplanted at (section 3). The first is a blocker under item 5 of the
2026-09-21 ruling until John rules how it is registered.

## 9. Files

`experiments/rehearsal-successor-measure/out-controls-rerun/`:
`nominate_{arm}_seed{seed}.json` (the fits, the full development grid, the
candidates, the primary and stricter choices), `measure_{arm}_seed{seed}.json`
(everything on fresh episodes), `summary.json`, `table.md`. Code:
`src/rerun_controls.py` (unchanged since `f2d836b`) and
`src/posthoc_control4.py` (post hoc).
===== END OF RECORD 19 =====

===== RECORD 20 of 25 - the short pre-stated run - `docs/2026-10-03-short-prestated-run.md` (complete file, 14,310 characters) =====
# The short pre-stated run: findings

*Written 2026-10-03 (Pacific) by the Claude Code checking session that ran
it, on branch `w2a-job2-short-prestated-run`. The method,
`docs/2026-10-03-short-prestated-run-method.md`, and the code,
`experiments/rehearsal-successor-measure/src/short_prestated_run.py`, were
committed and pushed with no output at `eb13dba`, before the run. **The code
was not changed after that commit; it ran as committed, first time.** Laptop,
processor only. Nothing rented, nothing trained, nothing spent: $0.*

*Written under the workspace plain-language rule. Every figure below is
**MEASURED**: it is in the output files under
`experiments/rehearsal-successor-measure/out-short-prestated-run/`, and the
tables are the script's own. Sentences that explain a figure are marked
**ARGUED**. This is a rehearsal record on twelve particular trained toy
models. Figures for the entangled, free and mixed models are properties of
those models, not of the code.*

**What this session opened and what it did not.** Committed files only (the
list is in the method file). It did not open any chat or transcript of the
session that wrote the rulings, the re-run or the diagnostic. It is not the
session that wrote the diagnostic. It did write the check of the re-run
(pull request 79) before this, and the method says what it had already seen
because of that. **This run was written and run by one session and is owed a
check by another.**

## 1. The short version

- **(a) The too-early-position control, as redefined, holds on all twelve
  models.** The model's outputs with the transplant are bit-identical to its
  outputs without it. Expected, and by construction: section 3.
- **(b) The new reported figure is filled for all twelve, and it is not
  flattering.** Away from the action position the chosen piece often does not
  carry the label at four fifths, **including on the mixed model, where this
  session's expectation was wrong.** No pass line applies. One thing here is
  John's: how the registered column is to be computed, because two fair ways
  of computing it disagree about the mixed model. Section 4.
- **(c) NOT A RESULT.** The other-agent control's code ran end to end on the
  free model's seed 0 with the accuracy floor switched off, and returned its
  figures. That is all it shows. Section 5.
- **No stop fired.**

## 2. The run

```
$ cd experiments/rehearsal-successor-measure/src
$ /Users/john/Code/minimum-viable-mind/.venv/bin/python short_prestated_run.py
...
done in 71s
```

torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, on the processor. (The method
gives the command with the relative path `../../../.venv/bin/python`; this
session ran from a separate working folder, where the project's Python is
reached by its full path. Same program.) Everything the run printed is in
`out-short-prestated-run/stdout.txt`.

## 3. Part (a): the too-early-position control, positions before both twins' first own turns

The script's table (`out-short-prestated-run/table.md`, from `part_a.json`):

| arm/seed | layers | outputs bit-identical (holds) | share landing on the donor's value | no-transplant share | trials whose action changed |
|---|---|---|---|---|---|
| T/0 | (0,) | identical | 0.0000 | 0.0000 | 0 |
| T/1 | (0,) | identical | 0.0000 | 0.0000 | 0 |
| T/2 | (0,) | identical | 0.0000 | 0.0000 | 0 |
| C/0 | (2,) | identical | 0.0512 | 0.0512 | 0 |
| C/1 | (1,) | identical | 0.0488 | 0.0488 | 0 |
| C/2 | (1,) | identical | 0.0600 | 0.0600 | 0 |
| F/0 | (1,) | identical | 0.0587 | 0.0587 | 0 |
| F/1 | (1,) | identical | 0.0563 | 0.0563 | 0 |
| F/2 | (1,) | identical | 0.0688 | 0.0688 | 0 |
| M/0 | (1,) | identical | 0.0125 | 0.0125 | 0 |
| M/1 | (1,) | identical | 0.0175 | 0.0175 | 0 |
| M/2 | (1,) | identical | 0.0138 | 0.0138 | 0 |

(T, C, F and M are the separable, entangled, free and mixed models.) Also in
`part_a.json`, for every model: the largest difference between any two output
numbers is 0.0; a null transplant at the same positions is bit-identical; the
twins' states at those layers and positions are identical. Across the 800
pairs the control transplants at between 1 and 21 positions per pair, about
5 on average (`positions_per_pair`), never none, so it is never an empty test.

**Against what was expected.** As expected on every line. The method said in
advance that this was not a blind prediction: this session had already
observed it with different code.

**What it means (ARGUED).** The control holds, and it holds for a reason that
has nothing to do with these models: before either twin has been told a turn
is its own, the two have read the same input, so the state being transplanted
is the state already there. The control as redefined is a known-answer test
of the pairing and the code. **For the registration it should be described
that way, and not as evidence that a model does not yet know its identity.**

## 4. Part (b): the chosen piece's accuracy at the other positions of its site

**Reported only. No pass line.** Each cell is *whole state / piece*: how many
of 180 held-out development episodes a fresh straight-line read gets right,
given the whole state at that position, and given only the state's
coordinates inside the chosen piece. For comparison, the rule at the action
position asks for 144. The free model's rows are at the site the re-run used
for description; it has no reading.

| arm/seed | site set | at the action position | at each other position | average over the other positions |
|---|---|---|---|---|
| T/0, T/1, T/2 | layer 0 at the action position, 8 directions | 180 / 180 | single position | |
| C/0 | layer 2 at the action position, 8 directions | 180 / 180 | single position | |
| C/1 | layer 1 at the action position and the three before it, 8 directions | 177 / 172 | 1 before: 180 / 139; 2 before: 179 / 139; 3 before: 179 / 33 | 179 / 113 |
| C/2 | layer 1 from the first own turn to the action, 4 directions | 176 / 150 | first own turn, tokens 1 to 5: 180 / 63; 180 / 82; 167 / 46; 149 / 30; 180 / 84. Before the action, 5 to 1: 180 / 71; 180 / 112; 180 / 129; 180 / 88; 180 / 139 | 180 / 123 |
| F/0 (described only) | layer 1 from the first own turn to the action, 1 direction | 32 / 22 | first own turn, tokens 1 to 5: 180 / 21; 66 / 15; 31 / 15; 61 / 18; 51 / 15. Before the action, 5 to 1: 32 / 14; 21 / 13; 21 / 18; 26 / 15; 41 / 17 | 91 / 25 |
| F/1 (described only) | layer 1 at the action position and the three before it, 4 directions | 12 / 17 | 1 before: 22 / 14; 2 before: 20 / 20; 3 before: 24 / 23 | 19 / 11 |
| F/2 (described only) | layer 1 from the first own turn to the action, 8 directions | 18 / 18 | first own turn, tokens 1 to 5: 180 / 145; 85 / 36; 46 / 13; 99 / 17; 51 / 22. Before the action, 5 to 1: 11 / 18; 28 / 18; 14 / 21; 16 / 16; 43 / 19 | 73 / 25 |
| M/0 | layer 1 from the first own turn to the action, 8 directions | 180 / 180 | first own turn, tokens 1 to 5: 180 / 151; 180 / 153; 178 / 95; 179 / 34; 180 / 130. Before the action, 5 to 1: 180 / 67; 180 / 148; 180 / 180; 179 / 133; 180 / 120 | 180 / 163 |
| M/1 | the same | 180 / 180 | first own turn, tokens 1 to 5: 180 / 151; 180 / 136; 180 / 119; 177 / 71; 178 / 124. Before the action, 5 to 1: 180 / 171; 180 / 177; 180 / 143; 174 / 143; 180 / 172 | 180 / 174 |
| M/2 | the same | 180 / 180 | first own turn, tokens 1 to 5: 180 / 174; 180 / 152; 179 / 102; 177 / 33; 180 / 162. Before the action, 5 to 1: 180 / 178; 179 / 157; 180 / 174; 175 / 136; 180 / 172 | 180 / 175 |

(The script's own table, with the same figures one row per model, is
`out-short-prestated-run/table.md`; the figures are in `part_b.json`. "The
average over the other positions" is the read taken on the state averaged
over every position of the site except the action position.)

**Against what was expected, line by line.**

- *The action-position figures equal the re-run's on all twelve.* **Yes**
  (`matches_the_controls_rerun` true on all twelve). Stop S3 did not fire.
- *The separable model and the entangled model's seed 0 have a single
  position.* **Yes.**
- *At the first token of the first own turn the whole state is right on
  nearly all 180, on every model with a span site.* **Yes:** 180 of 180 on
  all six.
- *The mixed model's piece is right on at least 144 at most of the ten
  positions and on the average.* **Wrong on the first half, right on the
  second.** On the average: 163, 174 and 175. Position by position the piece
  reaches 144 at only 4 of 10 positions on seed 0, 4 of 10 on seed 1 and 7 of
  10 on seed 2. At the fourth token of the model's first own turn (the value
  word) it is right on 34, 71 and 33 of 180. **This session expected better
  and is writing down that it was wrong.**
- *The entangled model's seeds 1 and 2: a guess, low confidence, that the
  piece falls below 144 at one or more other positions.* **Yes, and by more
  than guessed.** Seed 1: 139, 139 and 33. Seed 2: below 144 at all ten, from
  30 to 139; 123 on the average.
- *The free model: about 21, 71 and 145 at the first token of its first own
  turn; well under 144 elsewhere.* 21 and 145 on seeds 0 and 2, as seen
  beforehand. **The 71 for seed 1 was this session's mistake in the method:**
  seed 1's site is the action position and the three before it, so it has no
  first-own-turn figure in this table. Everywhere else the free model's piece
  is between 11 and 36 of 180.

**What this does and does not show (ARGUED).**

- At every position of every span site the **whole state** holds the label
  (149 to 180 of 180 on the built models). So a low piece figure there means
  the label is present and is not held in the chosen directions at that
  position. That is what the ruling packet anticipated: directions fitted
  where the model acts need not be the ones that hold the label at its
  earlier turns.
- It bears on one sentence a reader might write: "the piece held the label
  and the transplant of it did nothing" (the entangled model) or "did half"
  (the mixed model). **On this evidence that sentence is true at the action
  position and not true across the whole site**, for the entangled model's
  seeds 1 and 2 and, position by position, for the mixed model too. John
  ruled that this is reported and not gated; this is the report.
- It does not change any reading. The readings come from what the
  transplants do to the action, and those are unchanged.
- **A limit of the figures.** Each is a fresh read fitted on 420 episodes
  with twelve possible answers, in a piece of 4 or 8 directions. A figure
  like 139 against 144 is a few episodes and should not be read finely.

**One thing that is John's.** The ruling says "the chosen piece's accuracy at
the other positions of its site" and does not say how it is computed. The
method chose position by position, plus the average, and marked that as this
session's reading. **The two give different pictures of the mixed model:** on
the average its piece clears four fifths on every seed; position by position
it does not at three to six of ten positions. Whichever goes in the
registered reporting table should be chosen and named before the registered
runs, and this session's suggestion (ARGUED) is to print both, since each
hides something the other shows. Not reported at all here: the positions in
the middle of a span, which do not line up from one episode to the next and
are covered only through the average.

## 5. Part (c): the other-agent control's code path. NOT A RESULT

**This is a test that the code runs end to end. It is not a result, and its
figures are not a pass or a fail of anything.** The read of the named agent's
marker on this model misses its floor, so the piece transplanted here is not
known to carry the named agent at all, and John withdrew the control's pass
line on 2026-10-03.

What was run: the re-run's own function for the control
(`rerun_controls.control2`), unchanged, called once for the free model's seed
0 with the piece's accuracy floor set to zero for that one call.

What it returned (`out-short-prestated-run/part_c_NOT_A_RESULT.json`):

```
(c) NOT A RESULT. F/0 with the floor switched off: ran end to end True
    site set: layer 1, the action position and the three before it, 8 directions
              (piece right on 92 of 180, whole read on 95; the floor would have asked for 144)
    own-directed action moved in 0.0012 of trials; under a random piece 0.0063
    named-other action moved in 0.0962 of trials
```

- *Expected: it runs end to end and returns the site set and three shares.*
  **Yes.** Stop S4 did not fire. No figure was predicted and none is
  interpreted.
- The pass-or-fail label the function attaches was dropped from the output
  file, as the method said it would be.
- **What is now true that was not before:** every line of the other-agent
  control's code has been executed once, on the processor, at $0. The
  registered run will not be the first time it runs.
- **What is still true:** the control has never been exercised on a model
  whose read of the named agent clears its floor. Nothing here changes that.

## 6. Against the method's stops

| Stop | Fired? |
|---|---|
| S1, a model file does not match its fingerprint | No |
| S2, part (a) not bit-identical on any model | No |
| S3, an action-position figure differs from the re-run's | No |
| S4, part (c) returns no verdict or raises an error | No |

## 7. What this run settles, and what it leaves

**Settled, subject to a check by another session:** the redefined
too-early-position control has been run as a pre-stated quantity and holds on
all twelve toy models; the new column is filled for all twelve; the
other-agent control's code has run end to end. Those were the three things
the ruling of 2026-10-03 asked for before the registration review.

**Left for John:** how the new column is computed in the registered table
(section 4). **Left for version 4 of the proposal:** to describe the
redefined control as a known-answer test (section 3), and to say plainly that
the piece's four fifths is established at the action position only
(section 4).

## 8. Files

`experiments/rehearsal-successor-measure/out-short-prestated-run/`:
`part_a.json`, `part_b.json`, `part_c_NOT_A_RESULT.json`, `table.md`,
`stdout.txt`. Code: `src/short_prestated_run.py`, unchanged since `eb13dba`.
===== END OF RECORD 20 =====

===== RECORD 21 of 25 - the ordinary competing solver put through the measurement - `docs/2026-10-03-competing-solver-run.md` (complete file, 16,734 characters) =====
# The ordinary competing solver under the rules as now ruled: findings

*Written 2026-10-03 (Pacific) by the Claude Code session that wrote and ran
it, on branch `w2b-job1-competing-solver-run`, cut from the main line at
`41b0bd3`. The method, `docs/2026-10-03-competing-solver-run-method.md`, and
the code, `experiments/rehearsal-successor-measure/src/competing_solver_run.py`,
were committed and pushed with no output at `744a8b3`, before the run. **The
code was not changed after that commit; it ran as committed, first time.**
Laptop, processor only. Nothing rented, nothing trained, nothing spent: $0.*

*Written under the workspace plain-language rule. Every figure below is
**MEASURED**: it is in the output files under
`experiments/rehearsal-successor-measure/out-competing-solver-run/`, and the
tables are the script's own. Sentences that explain a figure are marked
**ARGUED**. This is a rehearsal record on three particular trained toy
models; its figures are properties of those models.*

**What this session opened and what it did not.** The same as the method's
list: committed files only, at `41b0bd3`. It did not open the other record of
the seven-question ruling, any ruling packet, or any chat or transcript of
another session. **This run was written and run by one session and is owed a
check by a session that did not write it** (ruling 7 requires that check
before the registration review).

## 0. Said first, as the method asks

- **No reading was returned on any seed, under either reading of the
  solver.** Stop B2 did not fire. No other stop fired.
- **Two figures surprised this session and are written down here, unchanged**
  (section 4). The whole-state floor is not what holds this solver back by
  any margin. On seeds 0 and 1 the floor asks for less than nothing, and the
  check treats that as a miss. Under the second reading, on seed 2, **33 of
  45 site sets clear the floor on fresh episodes**, by one or two episodes of
  800, while none clears on development episodes. The nomination is made on
  development episodes, so nothing was nominated; and had it been, the piece
  rule would have refused every size by a wide margin (best piece 21 of 180).

## 1. The short version

- **The expected result came back: no verdict on every seed.** Its reason is
  the first kind on every seed and both readings: "no site set clears the
  whole-state floor". The stricter row says the same.
- **The read of the solver's own marker word is near chance.** The whole read
  is right on 11 to 21 of 180 held-out episodes; the best piece at any layer
  and size on 20 to 25. The piece rule asks for 144.
- **The gate, recomputed on the processor, matches the committed figures
  exactly** under the primary reading: 702, 715 and 702 of 3,000 on the
  own-directed condition, 712, 726 and 650 on the named-other. The bar is 790.
- **Under the primary reading the twins are one input**, so every transplant
  puts back the state already there. That no verdict follows from the pairing
  and is a test of the code more than of the solver, as the method said. The
  second reading, which feeds the solver its unused acting channel, is the
  one that tests the solver, and it also returns no verdict.
- **The no-transplant rule fails on every seed** (about 0.22 to 0.25 against
  a formula's 0.11), as predicted. It would withhold a reading on its own.
- **Description only:** with no floor applied, the arithmetic under the
  primary reading is zero divided by zero at all 180 comparisons. Under the
  second reading it comes to **1.0000** at most comparisons, the figure an
  entangled model gives. Section 5 says why that is noise and what it shows.

## 2. The run

```
$ cd experiments/rehearsal-successor-measure/src
$ /Users/john/Code/minimum-viable-mind/.venv/bin/python competing_solver_run.py > ../out-competing-solver-run/stdout.txt 2>&1
...
done in 839s
```

torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, on the processor. (The method
gives the project's Python by a relative path; this session ran from its own
worktree, where it is reached by its full path. Same program.) The three
model files matched `SHA256SUMS` before any was loaded. Everything the run
printed is in `out-competing-solver-run/stdout.txt`.

"Reading A" is the method's primary reading: the solver's acting channel is
removed, as it was in training and scoring. "Reading B" feeds it the channel,
as a registered procedure handed the file would. Both are defined in the
method, section 3, as this session's reading and John's to overturn.

## 3. The figures, per seed

### 3.1 The read: correct of 180 held-out development episodes, every layer

Reading A, the primary reading:

| seed | layer | whole read | piece, 1 direction | 2 | 4 | 8 |
|---|---|---|---|---|---|---|
| 0 | 0 | 13 | 13 | 13 | 13 | 13 |
| 0 | 1 | 16 | 20 | 23 | 20 | 11 |
| 0 | 2 | 20 | 17 | 20 | 24 | 23 |
| 0 | 3 | 19 | 19 | 12 | 16 | 17 |
| 0 | 4 | 20 | 14 | 15 | 21 | 18 |
| 1 | 0 | 13 | 13 | 13 | 13 | 13 |
| 1 | 1 | 16 | 12 | 9 | 19 | 15 |
| 1 | 2 | 11 | 15 | 23 | 11 | 14 |
| 1 | 3 | 16 | 11 | 13 | 11 | 21 |
| 1 | 4 | 15 | 18 | 15 | 14 | 10 |
| 2 | 0 | 13 | 14 | 13 | 13 | 13 |
| 2 | 1 | 13 | 18 | 16 | 19 | 17 |
| 2 | 2 | 20 | 22 | 23 | 16 | 16 |
| 2 | 3 | 21 | 15 | 18 | 19 | 20 |
| 2 | 4 | 16 | 14 | 13 | 17 | 20 |

Reading B, for description:

| seed | layer | whole read | piece, 1 direction | 2 | 4 | 8 |
|---|---|---|---|---|---|---|
| 0 | 0 | 13 | 13 | 14 | 14 | 14 |
| 0 | 1 | 16 | 20 | 23 | 19 | 11 |
| 0 | 2 | 20 | 17 | 21 | 25 | 23 |
| 0 | 3 | 20 | 19 | 12 | 16 | 18 |
| 0 | 4 | 20 | 13 | 14 | 22 | 17 |
| 1 | 0 | 13 | 14 | 13 | 13 | 13 |
| 1 | 1 | 16 | 12 | 11 | 17 | 13 |
| 1 | 2 | 12 | 18 | 20 | 11 | 11 |
| 1 | 3 | 16 | 11 | 13 | 10 | 17 |
| 1 | 4 | 15 | 18 | 14 | 14 | 10 |
| 2 | 0 | 13 | 14 | 13 | 13 | 13 |
| 2 | 1 | 14 | 18 | 18 | 20 | 17 |
| 2 | 2 | 20 | 19 | 20 | 16 | 16 |
| 2 | 3 | 20 | 16 | 17 | 15 | 21 |
| 2 | 4 | 15 | 14 | 12 | 18 | 19 |

(A piece is sometimes right on more episodes than the whole read. Each is a
fresh read fitted on 420 episodes with twelve possible answers, and near
chance a smaller read can land a few episodes higher. ARGUED.)

### 3.2 Nomination and status

| seed, reading | gate: own, named-other, of 3,000 (bar 790) | site sets clearing the whole-state floor, development / fresh, of 45 | best piece of 180 (band sampling alone would put round it) | nomination | stricter row | status |
|---|---|---|---|---|---|---|
| 0, A | 702, 712 | 0 / 0 | 24 (16 to 34) | no site set clears the whole-state floor | the same | **no verdict** |
| 1, A | 715, 726 | 0 / 0 | 23 (16 to 33) | the same | the same | **no verdict** |
| 2, A | 702, 650 | 0 / 0 | 23 (16 to 33) | the same | the same | **no verdict** |
| 0, B | 707, 710 | 0 / 0 | 25 (17 to 35) | the same | the same | **no verdict** |
| 1, B | 716, 722 | 0 / 0 | 20 (13 to 30) | the same | the same | **no verdict** |
| 2, B | 698, 653 | 0 / **33** | 21 (14 to 31) | the same | the same | **no verdict** |

On every seed and both readings: the null transplant is bit-identical at all
45 site sets on fresh episodes (stop B4 did not fire). Under reading A the
twins' inputs and states are identical on development and fresh episodes,
largest difference 0.0 (stop B3 did not fire). Under reading B they differ,
and the twins' own-directed actions differ on 3 to 12 trials of 600 or 800.

### 3.3 The no-transplant rate against its formula, fresh episodes

| seed, reading | rate | (1 − accuracy) ÷ 7 | inside the 0.018 allowance |
|---|---|---|---|
| 0, A | 0.2487 | 0.1107 | no |
| 1, A | 0.2300 | 0.1116 | no |
| 2, A | 0.2200 | 0.1109 | no |
| 0, B | 0.2500 | 0.1107 | no |
| 1, B | 0.2313 | 0.1116 | no |
| 2, B | 0.2225 | 0.1109 | no |

### 3.4 Against what was expected (the method, section 6)

| Quantity | Expected | Came back |
|---|---|---|
| The gate | close to the committed figures, fails | **Reading A: identical to the committed figures.** Reading B: within 5 of them. Fails on every seed |
| The twins' states | identical under A; differ under B | **as expected** |
| Site sets clearing the floor | none under A, by construction; probably none under B, about one chance in six per seed of a clearance by noise | **None on development episodes anywhere.** Under B on seed 2, **33 on fresh episodes** (section 4) |
| The read | a guess of 10 to 65 of 180 under A, 10 to 70 under B | **9 to 25.** Lower than the guess: near the 13 to 15 that knowing nothing gives, and nowhere near the 45 of guessing among the episode's four agents |
| The nomination | no verdict, every seed | **as expected** |
| The arithmetic | 0 ÷ 0 at all 180 under A; not predicted under B | **as expected under A.** Under B, 1.0000 at most comparisons (section 5) |
| The null transplant | bit-identical at all 45 | **as expected** |
| The no-transplant rate | outside the allowance, about 0.25 against 0.11 | **as expected**: 0.22 to 0.25 against 0.11 |

## 4. What surprised this session, written down and not changed

**4.1 On seeds 0 and 1 the floor asks for less than nothing.** On
development episodes the solver lands on the donor twin's value more often
than on its own right answer (seed 0, reading A: 0.2400 against 0.2333; seed
1: 0.2300 against 0.2100). The floor asks the whole-state transplant to raise
the donor's share by four fifths of (accuracy − untouched), which here is
below zero. `repairs.floor_check` counts a requirement at or below zero as a
miss, whatever the transplant does. So on seeds 0 and 1, under both readings,
the floor could not have been cleared by any transplant. That clause, not a
measured shortfall, is what returns no verdict there. (Under reading A the
transplant changes nothing anyway.)

**4.2 Under reading B, seed 2 clears the floor on fresh episodes at 33 of 45
site sets.** On development episodes seed 2's requirement is +0.0053, about
3 episodes of 600, and the largest raise any site set gives is +0.0017, one
episode. On fresh episodes the requirement is +0.0010, under one episode of
800, and 33 site sets raise the donor's share by one or two episodes. The
nomination is made on development episodes only, so none was nominated and
the fresh clearances are never used. Had they been, the piece rule would have
refused every size: the best piece is 21 of 180 against 144.

**What these mean (ARGUED).** The whole-state floor is set relative to how
far the model is above its own no-transplant rate. For a solver that cannot
tell whose value it needs, that distance is about zero, so the floor is
about zero, and one or two episodes decide it either way. On this solver the
floor is not a margin; it is a coin. What holds the solver back with room to
spare is, in order: **the gate on learning** (it fails by 64 to 140 of 3,000,
and in the registered experiment a model that fails the gate is not read at
all); **the piece rule** (best piece 20 to 25 of 180 against 144, the whole
sampling band far below); and **the no-transplant rule** (the rate misses
its formula by 0.11 to 0.14, against an allowance of 0.018). The floor's verdict on this solver should not be
cited as the reason it returns no verdict.

## 5. Description only: what the arithmetic would have returned

**None of this is a reading.** The number is (whole − piece) ÷ (whole −
untouched), on fresh episodes, at all 180 comparisons, with no floor applied.

| seed, reading | accuracy, untouched | whole − untouched, over 45 site sets | room the floor asks for | of 180: division by zero / defined | defined values: smallest, middle, largest |
|---|---|---|---|---|---|
| 0, A | 0.2250, 0.2487 | 0 to 0 | −0.0190 | 180 / 0 | none defined |
| 1, A | 0.2188, 0.2300 | 0 to 0 | −0.0090 | 180 / 0 | none defined |
| 2, A | 0.2238, 0.2200 | 0 to 0 | +0.0030 | 180 / 0 | none defined |
| 0, B | 0.2250, 0.2500 | −0.0025 to 0 | −0.0200 | 32 / 148 | 1.0000, 1.0000, 1.0000 |
| 1, B | 0.2188, 0.2313 | −0.0013 to 0 | −0.0100 | 20 / 160 | 1.0000, 1.0000, 1.0000 |
| 2, B | 0.2238, 0.2225 | −0.0013 to +0.0025 | +0.0010 | 20 / 160 | 0.0000, 1.0000, 1.0000 |

**What it shows (ARGUED).** Under reading B the transplant of the whole state
moves the donor's share by one or two episodes, often downwards, and the
transplant of the piece moves nothing, so the ratio is very nearly always
exactly 1. **Without its floors the formula would describe the ordinary
competing solver the way it describes the entangled model.** That is the
inflation the floors and the gate exist to stop, and on this solver they
stop it. It is also a reason never to print the arithmetic for a model that
did not clear the floors without the words "not a reading" beside it, as
this file and the re-run both do.

## 6. Against the method's stops

| Stop | Fired? |
|---|---|
| B1, a model file does not match its fingerprint | No |
| B2, a reading is returned on any seed | **No**, under either reading |
| B3, under reading A the twins' inputs or states are not identical | No |
| B4, the null transplant is not bit-identical somewhere | No |

## 7. Which sentences of version 4 these figures bear on

Version 4 is `docs/successor-experiment-proposal-2026-10-03-v4.md`. This file
does not edit it; another session is working on it.

- **Section 7.3, the last paragraph** ("The ordinary competing solver has not
  yet been measured under the piece rule [...]"): the run it says is owed now
  exists, and **its stated expectation, "no verdict", is what came back**, on
  every seed. Its reason as written ("a solver with no acting channel should
  have no read of its own marker word that reaches four fifths") holds (best
  piece 20 to 25 of 180), but it is **not the rule that stopped the run
  first**: no site set cleared the whole-state floor, so the piece rule was
  never consulted. Its sentences "This version quotes no figure for it" and
  "until then this text does not go to the registration review" can be
  replaced once this run is checked.
- **Section 8.1, the reference points:** the ownership-blind solver's
  own-directed accuracy, 0.2340 to 0.2383, is reproduced exactly on the
  processor (702, 715 and 702 of 3,000). The clause "the ownership-blind
  solver is to be put through the nomination under it before the
  registration review" is answered by this run.
- **Section 10, item R-5** ("The ownership-blind solver's run through the
  nomination under that rule is owed before the registration review") and
  **"What happens next"** ("The ordinary competing solver is run under the
  piece rule, method first, by another session, and checked"): the run is
  done, method first; the check is still owed.
- Also the header's item 2 ("One more short run is owed"), the same.
- **Section 4 of these findings bears on any sentence that says the
  whole-state floor protects against a solver like this.** This session did
  not find one by search, but did not read version 4 through.

## 8. Questions for John, each with a suggestion

Not asked in chat; for the session that routes rulings.

1. **Which reading of the solver the registration cites.** *Suggestion:*
   reading A, the channel removed, as the primary, because that is how the
   solver was trained and scored; and reading B stated beside it, because
   under reading A the no verdict follows from the pairing alone and says
   little about the solver.
2. **Whether the registration says what actually stops this solver.**
   *Suggestion:* one sentence, that on the toy the competing solver's no
   verdict comes from the gate on learning, the piece rule and the
   no-transplant rule, each with room to spare, and that the whole-state
   floor is close to zero for a model near chance and is decided there by one
   or two episodes (section 4). No change to any rule.
3. **The no-transplant rule's formula on a solver that cannot tell owners
   apart.** It assumes wrong answers spread evenly over the seven other
   values; this solver's land on the other agents' values, one of which is
   the donor's, so the rate is about twice the formula's. *Suggestion:*
   report only; it withholds a reading here, which is the right outcome, but
   the registration should not describe the formula as a property of every
   model.

## 9. Files

`experiments/rehearsal-successor-measure/out-competing-solver-run/`:
`reads_blind_seed{0,1,2}_{channel_removed,channel_left_on}.npz` (the fitted
reads, development episodes only), `nominate_blind_seed*_*.json` (fits, the
full development grid, the floors, the choice, the description-only
arithmetic), `measure_blind_seed*_*.json` (the gate, the fresh-episode floors,
the null transplant, the twins, the no-transplant rate, the description-only
arithmetic), `summary.json`, `table.md`, `stdout.txt`. Code:
`src/competing_solver_run.py`, unchanged since `744a8b3`.
===== END OF RECORD 21 =====

===== RECORD 22 of 25 - the other-agent control against twenty random pieces (NOT A RESULT: a code test) - `docs/2026-10-03-control-2-twenty-draws.md` (complete file, 7,572 characters) =====
# The other-agent control compared with twenty random pieces: findings of the code test

*Written 2026-10-03 (Pacific) by the Claude Code session that wrote and ran
it, on branch `w2b-job2-control-2-twenty-draws`, cut from the main line at
`41b0bd3`. The method, `docs/2026-10-03-control-2-twenty-draws-method.md`,
and the code,
`experiments/rehearsal-successor-measure/src/control2_twenty_draws.py`, were
committed and pushed with no output at `174081e`, before the run. **The code
was not changed after that commit; it ran as committed, first time.** Laptop,
processor only. Nothing rented, nothing trained, nothing spent: $0.*

*Written under the workspace plain-language rule.*

**THIS IS A TEST THAT THE CODE RUNS END TO END. IT IS NOT A RESULT.** The
piece's accuracy floor was switched off for the one call, so the piece
transplanted here is not known to carry the named agent at all. No figure
below is a pass or a fail of anything, and nothing is concluded from them
about any model.

**What this session opened and what it did not.** The same as the method's
list: committed files only, at `41b0bd3`. It did not open the other record of
the seven-question ruling, any ruling packet, or any chat or transcript of
another session. **This code test was written and run by one session and is
owed a check by a session that did not write it.**

## 1. The short version

- **The changed code ran end to end** on the free model's seed 0 and returned
  the site set, the real figure, twenty random-piece figures and their
  summary. That is what the test was for.
- **Everything the change was not meant to touch came back identical to the
  earlier code test** (`docs/2026-10-03-short-prestated-run.md`, section 5):
  the same site set, and the same three figures to four places. So the new
  function is the old one with the one change ruled (stop D3 did not fire).
- **No stop fired.**

## 2. The run

```
$ cd experiments/rehearsal-successor-measure/src
$ /Users/john/Code/minimum-viable-mind/.venv/bin/python control2_twenty_draws.py > ../out-control-2-twenty-draws/stdout.txt 2>&1
exit 0
```

torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, on the processor; 50 seconds.
The model file matched `SHA256SUMS` before it was loaded. (The method gives
the project's Python by a relative path; this session ran from its own
worktree, where it is reached by its full path. Same program.)

What it printed (also `out-control-2-twenty-draws/table.md`; every figure is
in `code_test_NOT_A_RESULT.json`):

```
NOT A RESULT: the other-agent control compared with twenty random pieces, free model seed 0, floor switched off

ran end to end: True
site set: layer 1, the action position and the three before it, 8 directions
          (piece right on 92 of 180, whole read on 95; the floor would have asked for 144)
own-directed action moved under the named agent's piece: 0.0012 of 800 trials
under twenty random pieces: middle value 0.0037, 95th percentile 0.0052;
                            0 below, 1 equal to and 19 above the real figure
the twenty: 0.0025, 0.0037, 0.0012, 0.0050, 0.0037, 0.0050, 0.0050, 0.0088, 0.0050, 0.0037,
            0.0037, 0.0037, 0.0037, 0.0050, 0.0025, 0.0037, 0.0050, 0.0037, 0.0050, 0.0050
the single random piece as the earlier code drew it: 0.0063
named-other action moved: 0.0962
These figures are not a pass or a fail of anything.
```

## 3. Against what was expected (the method, section 5)

| Expected | Came back |
|---|---|
| Runs end to end and returns the site set, the real figure, twenty shares and their summary | **Yes** |
| Same site set as the earlier code test: layer 1, the action position and the three before it, 8 directions | **Yes** |
| Own-directed action moved: 0.0012 | **0.0012** |
| The one random piece as the earlier code drew it: 0.0063 | **0.0063** |
| Named-other action moved: 0.0962 | **0.0962** |
| A guess, for the record only: the twenty between 0.000 and about 0.02, more above the real figure than below | Between 0.0012 and 0.0088; 19 above, 1 equal, 0 below |

The three unchanged figures were seen before the run, so matching them is a
check that the path is the same, not a prediction.

**One thing about the code, not about the model (ARGUED).** The single random
piece the earlier code drew (0.0063) is higher than nineteen of the twenty
drawn now and above their 95th percentile (0.0052). A single draw can land in
the tail of what random pieces do. That is the reason version 4 gave when it
suggested the change (section 19, item 5: "a single draw is a weak thing to
print beside a figure"), and the code now prints the spread instead. It says nothing about the free model.

## 4. Against the method's stops

| Stop | Fired? |
|---|---|
| D1, the model file does not match its fingerprint | No |
| D2, the call returns no verdict or raises an error | No |
| D3, an unchanged figure differs from the earlier code test's | No |

## 5. What this settles and what it leaves

**Settled, subject to a check by another session:** the control's code as
ruled on 2026-10-03 (twenty random pieces drawn as control 3 draws them;
their middle value, 95th percentile and the counts below, equal and above; no
pass line) exists as a committed file and has run end to end once, on the
processor, at $0. Ruling 5 asked for that before the registration review.

**Still true, and unchanged by this:** the control has never been exercised
on a model whose read of the named agent clears its floor. No toy model has
one.

## 6. Which sentences of version 4 this bears on

Version 4 is `docs/successor-experiment-proposal-2026-10-03-v4.md`. This file
does not edit it; another session is working on it.

- **Section 7.3, item 2**, the sentence "What is reported: how often the
  own-directed action moves under the named agent's piece, beside how often
  it moves under twenty random pieces of the same size at the same sites,
  reported as control 3 reports its twenty (median, 95th percentile, and the
  counts below, equal and above)". The code now does this:
  `control2_twenty_draws.control2`.
- **The same item's bullet "The part of its code after the floor has run
  once, and that run is NOT A RESULT"**, which describes the run of the
  single-draw code. The code that would be registered has now also run once,
  NOT A RESULT, and the text should name this run and this file rather than
  only the earlier one. Version 4's own section 19, item 5 foresaw this ("the
  code path that ran once on 2026-10-03 is not quite the one registered").

## 7. Questions for John, each with a suggestion

Not asked in chat; for the session that routes rulings.

1. **Which file is the registered control 2.** The ruled change lives in a
   new file, because the brief said not to edit the committed scripts;
   `rerun_controls.control2` still has the one random piece and the pass
   line. *Suggestion:* the registration names
   `control2_twenty_draws.control2` as control 2's code and says that
   `rerun_controls.control2` is the earlier version, kept as the record of
   what the re-run did.
2. **Whether the 95th percentile of twenty is the right summary.** With
   twenty draws it is an interpolation between the two largest. That is the
   same as control 3 does, which is what was ruled. *Suggestion:* leave it as
   ruled and print the twenty as well, as this code does, so a reader sees
   the spread.

## 8. Files

`experiments/rehearsal-successor-measure/out-control-2-twenty-draws/`:
`code_test_NOT_A_RESULT.json`, `table.md`, `stdout.txt`. Code:
`src/control2_twenty_draws.py`, unchanged since `174081e`.
===== END OF RECORD 22 =====

===== RECORD 23 of 25 - the list of what has gone wrong in this program before, which the inside reviewer ran against version 4 - `docs/known-failure-modes.md` (complete file, 55,318 characters) =====
# Known failure modes, and the test that catches each one

*Written 2026-09-21 (Pacific) as the companion to the outside-review protocol
(`docs/outside-review-protocol.md`). That protocol was amended the same day to
require every registration text to be run against this list rather than to cite
it. This file is the list.*

*Approved by John as one of six recommendations put to him with its cost, in his
words "Ok, can we implement all of these?". The session proposed and he
approved; the wording here is the session's and is his to overturn.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30).*

---

## What this list is for

Five things have gone wrong in this programme badly enough to cost weeks of work,
to put an unsatisfiable sentence into text that had already been registered, or to
create a rented machine with a command documented as creating nothing.
Each is easy to recognise once it has been named — and, as it turns out, just as
easy to reproduce while naming it. A proposal reviewed on 2026-09-21 quoted the
first failure below by name, in the section discussing the weaknesses of its own
measure, and the measure two sections earlier reproduced it.

So this is not a reading list. Every entry ends with a test: a command a session
can run against a new design, and what the output has to show. The protocol's
failure-mode pass requires that test to be run and its output filed, for every
failure here, on every registration text. **"Considered and does not apply" is
not a disposition.** The count that is not zero, the cell that has trials in it,
the record that exists and contains what the sentence says it contains — those
are dispositions.

Every output printed below was produced by running the command printed above it,
in this repository, on 2026-09-21.

**What this list has been shown to be, and what it has not.** As a description of
what has gone wrong here, it is accurate.

**Which blocks below have been run, and which have not.** Fifteen blocks are
printed below. Twelve carry a command and the output that running it produced.
A thirteenth, the first block under failure 5, is different in kind and is
flagged again where it appears: it is the **recorded** output of the command
that created a rented machine on 2026-09-21, and it must never be re-run,
because re-running it is the failure. The block beneath it is failure 5's
actual test, which was run, and which creates nothing.
Ten of those eleven have been re-run by a session other than the one that wrote
them and compared against the printed text with `cmp`, which names the first byte
at which two files differ; nothing differed. The eight the list carried before
the repair described below had already been checked the same way once, with
`diff`. The eleventh is newer than that check: it is the block under failure 2
that prints the two rows illustrating that failure's middle limb, and the session
that added it ran it, but no other session has yet re-run it. The remaining two
blocks carry placeholders in angle brackets and no output. One of them is failure
4's first part, written as a template because it is pointed at whatever document
is under review; the word lists inside it are exercised on six worked claims in
the block below it, and that block was run and its output printed. **The other is
failure 2's second part, and it has never been run at all.** Running it means
running a whole probe pipeline twice against model checkpoints, which costs
compute that nobody has authorised. Its middle limb — the second run clears the
bar and the first does not — is now illustrated, by a printed block under failure
2 showing the two rows in the position sweep's findings file where exactly that
pattern appears. Illustrated is not executed: those rows come from the history
this entry was written from, so the limb still has not been seen to fire on
anything it had not already been fitted to.

As a set of tests a new design can be run against, this list is not yet
established. The first check found that three of the four tests fell short of the
standard this document sets on its own last page — that a test never seen to fail
has not been shown to detect anything. One passed on the very design that
produced the failure it describes, one did not execute at all, and one looked
only for words that the newest form of its own failure does not use. Those three
were repaired on 2026-09-21 by a third session. Failure 3's empty cell and
failure 4's widened word list are each printed below with the command and the
output showing the test failing on the design it was written from. Failure 2 is
printed that way for its first part only, and that part is a proxy rather than a
detector, for the reasons set out under it.

**Where that leaves the list.** The repairs have been checked once, by the
session that wrote
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-protocol-repair-claude-worktree.md`
at commit `fbfecb5`, the commit titled "Check the repair: the ten outputs hold,
two tests still owe a sentence". That check found the two gaps the paragraphs
above and the paragraph under failure 2's first part now fill. Those two
corrections were written by a fourth session and have not themselves been checked
by anyone. Under the pairing rule in the protocol beside this file, they are owed
a check by a session that did not make them. Until that check exists, treat this
list as a reliable account of the past and an unproven instrument for the future:
run it on a registration text and file what it returns, but do not read a clean
pass from it as evidence that a design is clean.

---

## 1. A comparison whose denominator was zero

**What it was.** Amendment A3 registered a corrected measure that subtracts, from
each score, the best a solver could do while ignoring ownership — the
ownership-blind ceiling — and then divides by the distance left between that
ceiling and a perfect score. For the control battery (the comparison battery of
questions, built so that answering it does not require knowing whose value is
whose), that ceiling turned out to be 1.0. The distance left was zero. The
measure had nothing to measure, and had had nothing to measure from the day it
was registered.

**How it showed up.** The third adversarial pass said it four days before the
registration commit, in its twenty-first finding — the unequal-ceilings finding
(`RT-21` in the red-team ledger), marked fatal, whose metric fix was marked
adopted. The fix depended on a ceiling nobody had measured. The measurement, when
it was finally made, is
`experiments/06-mvm-0a-constructed-self-index/ceiling-measurement-findings.md`,
whose title is the finding: "The control battery's ceiling is 1.0, and the clause
was never computable." A battery built so that its questions do not require
ownership has an ownership-blind ceiling of 1.0 by construction; dividing by the
distance to 1.0 divides by zero.

**Its newest form, found 2026-09-21.** The successor experiment proposal
registers its reading as the difference between two accuracies divided by the
larger of them, with no floor subtracted from either. A floor that sits under
both terms does not cancel in a ratio, so the largest value the reading can
return is different for every arm — every version of the system being compared —
because the accuracy it divides by is different for every arm, and the design
expects it to be. Two systems separable to exactly the same degree then read
differently for no reason but their overall accuracy. This is the ceiling failure
with the zero replaced by a moving number, which is harder to see and no more
measurable. It is filed as the first finding of the Gate C pass on that proposal
(`RT-172`, the per-arm-ceiling finding), in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-successor-proposal-claude-worktree.md`
at commit `3bbfece`, the commit titled "Gate C tier 1 review of the successor
experiment proposal: RT-172 to RT-188". The commit is named and not only the
branch it was written on, because a session branch is deleted once it is merged
and a citation anchored to one loses its signpost without anyone editing the
sentence. The design being criticised is the successor experiment proposal
(`docs/successor-experiment-proposal-2026-09-21.md`) at commit `d8ceba9`, the
commit titled "Successor proposal: the rehearsal buys a rented slice, and the
second release is bound to what it measures", which was written on a different
branch again. Both commits have since reached the main line in the working
checkout, though neither had been pushed to the shared copy of the main line when
this was written.

**The test.** Two parts, both cheap.

*Part one: print the denominator at the ceiling, for every condition the reading
will be applied to, using ceilings measured in the rehearsal rather than
assumed.*

```
$ python3 -c "
ceilings = {'primary battery': 0.2921, 'control battery': 1.0000}
for name, c in ceilings.items():
    print(f'{name}: denominator 1 - ceiling = {1 - c:.4f}')
"
primary battery: denominator 1 - ceiling = 0.7079
control battery: denominator 1 - ceiling = 0.0000
```

**Part one is a display and not a detector; part two below is what does the
detecting.** The arithmetic only shows what it is handed. Hand it the ceilings as
they were actually registered on 2026-09-15 — 0.2921 for the primary battery and
0.3227 for the control (`amendment-a3.md` line 415) — and it prints two healthy
denominators, with nothing to see:

```
$ python3 -c "
ceilings = {'primary battery': 0.2921, 'control battery': 0.3227}
for name, c in ceilings.items():
    print(f'{name}: denominator 1 - ceiling = {1 - c:.4f}')
"
primary battery: denominator 1 - ceiling = 0.7079
control battery: denominator 1 - ceiling = 0.6773
```

That is the failure passing its own test. The zero only appears once somebody has
measured the ceiling, and measuring it is the rehearsal's job, not this test's. So
part one's failure criterion is about where its numbers came from rather than
about the arithmetic: **it fails if any ceiling typed into it cannot be traced to
a committed measurement record**, named by file. Type in an assumed ceiling and
this command reproduces the original failure while producing a filed output that
looks like a disposition — which is what 0.3227 was.

*Part two: print the largest value the reading can return, per condition, when
the thing it is meant to detect is entirely absent.*

```
$ python3 -c "
def reading(whole, ownership_only): return (whole - ownership_only) / whole
floor = 0.125
for whole in (0.90, 0.60, 0.35):
    print(f'best score {whole}: top of scale = {reading(whole, floor):.3f}')
"
best score 0.9: top of scale = 0.861
best score 0.6: top of scale = 0.792
best score 0.35: top of scale = 0.643
```

**It fails if** any denominator is zero, or small enough that ordinary noise in
the measured ceiling moves the reading a lot; or if the top of the scale differs
between the conditions a single pre-stated threshold is compared across. A
threshold in units whose top of scale moves between where it was set and where it
is applied is not a threshold. Both halves need numbers from the rehearsal: a
ceiling that was assumed rather than measured is what produced this failure in
the first place.

---

## 2. A probe target that cannot be recovered in principle

**What it was.** The localization line spent weeks predicting `own_slot` — the
episode generator's index for whichever agent the model is playing — from the
model's internal states. That quantity has no consistent surface realisation: the
generator knows it, and nothing the model was shown or trained on requires the
model to compute it. It cannot be recovered from these states at any position,
with any instrument. Every null the line produced was therefore a null about an
unanswerable question, which is not evidence of the absence of anything.

**How it showed up.** In the position sweep of 2026-09-19
(`experiments/06-mvm-0a-constructed-self-index/position-sweep-findings.md`),
whose first arm came back "SWEEP INVALID on all three checkpoints" because its
positive control failed: zero of 165 tests cleared the bar. The finding names
what that cost — the blind-arm probes of 2026-09-16, the denoise-before-probing
diagnostic and the sweep itself "were all asking a question with no answer". The
contrast is the powered target test of the same day
(`powered-target-test-findings.md`): with the target re-posed as a quantity that
demonstrably reaches the states — the marker word, read at the position where it
*is* the input token — the same kind of read returns 0.5877 against a
no-information value of 0.04, about 159 standard deviations of its own null. The
instrument was never the problem. No review pass had been asked whether the named
quantity was recoverable at all.

**The test.** Two parts. **Part two is the one that catches this failure; part
one is a prompt to look.** Part one asks for a written sentence and checks that
it exists, which forces the question to be faced but settles nothing on its own.
Part two runs the probe twice and compares the two results, and its middle limb —
the second run clears the bar and the first does not — is what actually
distinguishes an unrecoverable target from a working one. Part two has never been
run; see the paragraph under it.

*Part one, before anything is registered:* the method document states, in one
sentence and in a fixed form of words, the route by which the quantity reaches
the model's states — which token carries it, or which part of the loss forces the
model to compute it. "The episode generator knows it" is not a route. Writing the
sentence is paper and pencil; **checking that it is there is a command**, so that
this part produces a disposition with its work shown like every other:

```
$ python3 -c "
import re
pattern = r'route to the states|carried by the token|forced by the loss|is the input token'
base = 'experiments/06-mvm-0a-constructed-self-index/'
for f in ('position-sweep-method.md', 'powered-target-test-method.md'):
    lines = [l.strip() for l in open(base + f) if re.search(pattern, l, re.I)]
    print(f'{f}: {len(lines)} route sentence(s)')
    for l in lines:
        print('   ' + l)
"
position-sweep-method.md: 0 route sentence(s)
powered-target-test-method.md: 1 route sentence(s)
   the marker position**, where it is the input token. It must clear three
```

That is this failure caught, on the design that produced it, with a command and
an output. The method committed before the sweep that spent weeks on `own_slot`
contains no sentence naming a route, because none could be written. The method
for the target that turned out to be recoverable contains one, and it names the
token. Run this on a new design's method document with that design's own wording
in the pattern; a count of zero is the finding.

**What this search cannot see, plainly.** It counts sentences that match a fixed
set of words, so it cannot see a route named in any other words. Run exactly as
printed above across all nine method documents in this experiment, seven come
back at zero, and one of the seven is the method for the powered eleven-position
sweep
(`experiments/06-mvm-0a-constructed-self-index/powered-position-sweep-method.md`),
which does what this part asks for and does it at length: it names in advance the
token that carries the target at one position, and says that nothing carries it
at another. It scores zero because it writes "as an input token" where the
pattern says "is the input token". That run is printed in the check of this
repair
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-protocol-repair-claude-worktree.md`
at commit `fbfecb5`, the commit titled "Check the repair: the ten outputs hold,
two tests still owe a sentence"). The other direction is no better: a count above
zero says only that some sentence matched the words typed into the pattern, and
the instruction to run it with the new design's own wording means a session that
writes the pattern out of the document it has just read will match by
construction. What this command records is whether the checking session found a
sentence it was willing to call a route — worth recording, because it forces one
specific sentence to exist and be quoted into the filed output where it can be
argued with by name, but not a measurement of whether a route exists.

**So part one is a prompt to look and not a verdict**, and the sentence above
calling a count of zero the finding should be read that way: a zero is a reason
to go and read the method document and settle in writing whether a route is named
there, and a sentence that matched is not on its own a pass.

*Part two, run in the rehearsal:* run the whole probe pipeline twice — once on
the pre-stated target, once on a quantity the design guarantees is present, read
at a position where it must be present — with the same bar and the same null.

```
$ python3 src/<probe_script>.py --target <the pre-stated quantity> --report margins
$ python3 src/<probe_script>.py --target <a quantity the input guarantees> --report margins
```

**It fails if** any of three things is true, and they are read together:

- **Part one returned no route sentence.** Fatal on its own, whatever the two
  runs do. A target whose route nobody can name is the target that has cost this
  programme weeks.
- **The second run clears the bar and the first does not.** *This is the failure
  this entry exists for.* A working instrument that returns nothing on the
  pre-stated target is evidence that the target is not there to be recovered —
  not evidence about the system being probed. The pre-stated target changes
  before registration, and the null already collected is withdrawn rather than
  reported.
- **The second run does not clear the bar.** Then the pipeline is broken and
  nothing has been measured at all; the first run says nothing either way,
  whether it cleared or not.

File both runs. A pre-stated probe target whose positive control was never run is
a fatal finding on its own, on the same reasoning as a pre-stated quantity the
rehearsal never exercised.

**Why the criterion is written this way.** Until 2026-09-21 this entry said only
"it fails if the second run does not clear the bar", and on the history the entry
is written from that test passes. The second run is the one on the quantity the
input guarantees, and in the position sweep of 2026-09-19 it cleared by an
enormous margin — 0.5877 against a no-information value of 0.04, about 159
standard deviations — which is the same evidence the entry itself cites for "the
instrument was never the problem". A criterion that looks only at the pipeline
detects a broken pipeline. It cannot detect an unrecoverable target, which is
what this entry is about, and the pattern that reveals one — the first run empty
while the second clears — was not named as a failure anywhere in the entry. It is
now the second bullet above.

**What that middle limb looks like in the record, with the test itself still
unrun.** The two runs part two asks for were never made. But a diagnostic filed
with the position sweep of 2026-09-19 read both quantities at the same position,
through the same instrument, each against its own fifty-draw permutation null,
and the sweep's bar throughout is three standard deviations of that null. Those
two rows are in its findings file, and this is them:

```
$ grep -nE "own_slot.*what the stack asks for|marker_token.*the input token itself" experiments/06-mvm-0a-constructed-self-index/position-sweep-findings.md
120:| `own_slot` — what the stack asks for | 0.293 (+1.60) | 0.273 (+0.88) | 0.243 (−0.24) | 0.283 (+1.33) | 0.275 (+0.91) |
122:| `marker_token` — the input token itself | **0.550 (+51.6)** | 0.513 (+43.1) | 0.510 (+41.3) | 0.498 (+41.9) | 0.490 (+40.8) |
```

First number column is the third layer, and each cell is the accuracy with its
margin in standard deviations of that cell's own null. The pre-stated quantity
tops out at 0.293, about 1.60 standard deviations, and clears three nowhere. The
quantity the input guarantees reaches 0.550, about 51.6. Second run clears, first
does not: that is the middle limb, in numbers that already exist.

**This illustrates the limb; it does not execute the test.** These are two rows
lifted from a record, not the two runs part two asks for. They come from the very
history this entry was written from, so the limb has still never been seen to
fire on a design nobody had already diagnosed. And the findings file labels the
diagnostic these rows sit in as **not pre-stated** — it was written after the
sweep had already failed, which the file says makes it worth less than a
measurement designed in advance. Part two stays unrun, because running it means
running a whole probe pipeline twice against model checkpoints and nobody has
authorised that compute. The paragraph near the top of this file that says so
still stands.

---

## 3. A cell that is empty by construction

**What it was.** Found 2026-09-21, in the successor experiment proposal. One of
the seven pre-stated controls — the one that separates "the transplant moved who
is acting" from "the transplant smuggled a value across", and so the one the
whole reading leans on — splits trials into pairs where the donor's identity
dictates the *same* answer as the recipient's and pairs where it dictates a
*different* one. Both cells are pre-stated and both are to be reported. The
grammar the design extends draws four *distinct* values for each contested item,
one per agent, without replacement, and asserts that the property survives
rendering. Two agents therefore never dictate the same answer, the first cell can
never hold a trial, and three other passages of the same proposal require the
distinctness that empties it. Filed as the second finding of the Gate C pass on
that proposal (`RT-173`, the empty-cell finding), in the same review file and at
the same commit named under failure 1 above (`3bbfece`), against the same
proposal commit (`d8ceba9`).

**The same defect one step further.** That control carries a pre-stated check: an
untouched condition "should be near the one-in-eight guessing rate; if it is not,
the pairing is broken and nothing is read." With distinct values, a model that has
learned the task lands on the donor's answer only by erring onto exactly that
slot. The rule as written passes a model that has learned nothing and fails one
that has learned the task. It is pointed the wrong way round, and it sits inside
the list of things the design proposes to freeze.

**The test.** Two parts, and a third for any threshold attached to a cell.

*Part one: count what the generator actually puts in each pre-stated cell, at
rehearsal scale.* This is the part that generalises to a design other than the A3
grammar, and it is the part that catches an empty cell. Four things in the block
below belong to the design being checked and are meant to be replaced: the module
that is imported, the list of pre-stated cells, and the two small functions that
say what a trial is and which cell it lands in. Between them they are most of the
block; everything else stands.

```
$ python3 -c "
import sys; sys.path.insert(0, 'experiments/06-mvm-0a-constructed-self-index/src')
from collections import Counter
import curriculum_a3 as design          # the registered generator, not a stand-in

PRE_STATED_CELLS = ['donor dictates the same answer',
                    'donor dictates a different answer']

def trials(episodes):                   # one trial per (episode, item, donor)
    for ep in episodes:
        for item in ep.contested:
            v = ep.values[item]
            for donor in range(design.N_AGENTS):
                if donor != ep.own_slot:
                    yield v[donor], v[ep.own_slot]

def cell_of(trial):
    donor, recipient = trial
    return PRE_STATED_CELLS[0] if donor == recipient else PRE_STATED_CELLS[1]

counts = Counter(cell_of(t) for t in trials(design.generate_balanced(200, seed=0)))
for cell in PRE_STATED_CELLS:
    print(f'{cell}: {counts.get(cell, 0)} trials')
"
donor dictates the same answer: 0 trials
donor dictates a different answer: 1200 trials
```

**Zero is the finding.** Two hundred episodes of the registered grammar produce
twelve hundred donor-and-recipient pairs and not one of them lands in the first
pre-stated cell, because the grammar draws a distinct value per agent for each
contested item. The comparison that cell is half of can never be made. That is
failure 3, caught by a command, on the design that produced it.

*Until 2026-09-21 this command did not execute.* It imported `src.curriculum`,
and there is no `src` package — the generator modules sit in
`experiments/06-mvm-0a-constructed-self-index/src/` and import each other by bare
name, so the directory goes on the path rather than being treated as a package.
It called a function named `generate`, and the module has `generate_episode` and
`generate_balanced` and no `generate`. And it used `cell_of` and
`PRE_STATED_CELLS` without ever defining them, so a session holding a different
design could not have told what they were supposed to return. It raised
`ModuleNotFoundError` on the first line that did any work, and so had never been
seen to fail on anything.

*Part two: read the generator for the property that would empty a cell —
drawing without replacement, a shuffle that permutes rather than resamples, a
distinctness assertion, a deterministic rule that makes two conditions the same
condition.* Every file the generator is spread across, not one of them:

```
$ grep -rnE "\.sample\(|\.shuffle\(|\.permutation|permutations\(|set\(|distinct|unique|without replacement" experiments/06-mvm-0a-constructed-self-index/src/curriculum.py experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:51:# Marker pool: per-episode speaker labels drawn without replacement, so no
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:109:    markers = rng.sample(MARKERS, n_agents)
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:113:    items = rng.sample(ITEMS, min(len(ITEMS), n_turns))
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:118:        rng.shuffle(r)
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:218:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:311:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:17:  pairs. Within an item the four values are **distinct**, so an item's
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:59:At its own revision turn the model sees four distinct earlier values for
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:209:    markers = rng.sample(MARKERS, N_AGENTS)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:210:    contested = rng.sample(ITEMS, N_CONTESTED)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:212:    # distinct values per contested item, one per agent
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:215:        vs = rng.sample(SLOTS, N_AGENTS)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:219:    rng.shuffle(pairs)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:233:    revisers = rng.sample(range(N_AGENTS), K_REVISERS)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:236:    rng.shuffle(rev_turns)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:329:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:371:       agent revised, this alone identified the model uniquely in a
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:420:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:468:        # every contested item assigned by all agents, distinct values,
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:530:    # distinctness constraint still holds
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:539:            assert len(set(vs)) == N_AGENTS, "distinctness broken by enactment"
```

Line 215 of the A3 grammar is the one that empties the cell — four distinct
values drawn for four agents, without replacement — and line 539 asserts the
property survives rendering. Lines 17, 59, 212, 468 and 530 are the comments that
say so in English, which is often where this is easiest to see.

**What this part cannot see, plainly.** It is a text search, so it finds only
idioms somebody thought to put in the pattern. Until 2026-09-21 the pattern held
two of them, `rng.sample` and `assert len(set`, and looked in one file; it would
have missed a shuffle, a `set()`, a `numpy` permutation, sampling without
replacement written a third way, a constraint enforced by rejecting and redrawing
inside a loop, a distinctness rule that lives in the encoder rather than the
generator, or a generator in a file nobody listed. The pattern above is wider and
covers two files instead of one, and it still misses all of those things if a
design spells them differently. **Part one is the detector; part two only says
where to look once part one has found a cell at zero.** A clean part two is not
evidence that no cell is empty.

*Part three: compute every pre-stated threshold at both ends of the range it will
face — a system that has learned the task and one that has learned nothing — and
print what the check returns at each.*

```
$ python3 -c "
for p in (0.95, 0.80, 0.60, 0.25):
    print(f'own-directed accuracy {p:<5} -> untouched rate {(1 - p) / 7:.4f}')
"
own-directed accuracy 0.95  -> untouched rate 0.0071
own-directed accuracy 0.8   -> untouched rate 0.0286
own-directed accuracy 0.6   -> untouched rate 0.0571
own-directed accuracy 0.25  -> untouched rate 0.1071
```

**It fails if** any pre-stated cell comes back with zero trials, or if a threshold
fires on the healthy end of the range and passes on the broken end. Both are
fatal: the first registers a comparison that can never be made, the second
registers an instrument check that reads a working instrument as a broken one.

---

## 4. A claim of measurement with no record, or with a record that does not reproduce

**What it was, first form.** Amendment A3's registered text said both battery
ceilings were "verified by the attack sweep, whose best ownership-blind attack
reached 0.3036 on 12,000 episodes". The 0.3036 is an attack on the primary
battery. The attack sweep contains no control-battery code at all, so the clause
is false as applied to the control, and the control's registered ceiling rests
entirely on one reference solver that ignores the one piece of information the
control question supplies. Registered on John's instruction, before any further
analysis, in
`experiments/06-mvm-0a-constructed-self-index/ceiling-defect-2026-09-17.md`. One
sentence had attached one verification to two numbers, and the number it did not
cover is the one that later turned out to be 1.0 — which is failure 1 above.

**What it was, second form.** A finding labelled MEASURED reported a count that
does not reproduce. The seventeenth finding of the independent pass on the
Amendment A4 clause (`F17`, on whether one condition's validity gates were ever
applied) says the endpoint records carry no such field "among their 110 keys".
They carry 15. John ruled on this on 2026-09-21, as the twentieth item of that
day's review-verification and staged-spending ruling
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`): the
finding's substance is undisturbed, but a MEASURED label is this programme's
promise that a number came from running something, and a committed record a
future session may cite has to be right.

**The test.** Two parts.

*Part one: list every sentence in the text that claims a measurement, so that
none is checked by accident and none is missed.* Two sweeps, because one of them
is a word list and a claim of measurement does not have to use a word:

```
$ grep -n -iE "verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result" <the text>.md
$ grep -n -E "[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}" <the text>.md
```

The second sweep catches a bare number offered as a result with no verb attached
to it, which no word list will ever find. Both sweeps are deliberately noisy —
`run` matches "running" and also "run" inside other words, `result` matches
"resulting", and the number sweep matches every figure in the document including
the ones that are not claims. Noise is the safe direction here: a session reads
the list and crosses off what is not a claim, which costs minutes, where a miss
costs whatever the unchecked claim costs.

**Why the word list is this wide.** Until 2026-09-21 it held seven words —
`verified`, `measured`, `calibrated`, `attacked`, `reproduc`, `confirmed`, `ran` —
and missed this document's own headline claim of measurement, the sentence near
the top reading "Every output printed below was produced by running the command
printed above it", because "running" contains none of them. It missed several
other ordinary ways of saying the same thing too. Six claims, the old list, the
widened list, and the number sweep:

```
$ python3 -c "
import re
OLD = r'verified|measured|calibrated|attacked|reproduc|confirmed|ran'
NEW = (r'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|'
       r'shows|showed|found|observed|recorded|returns|returned|yield|result')
NUM = r'[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}'
claims = [
    'Every output printed below was produced by running the command printed above it.',
    'We verify both ceilings against the attack sweep.',
    'Verification of the clause is filed with the run.',
    'The endpoint records were checked before the gate opened.',
    'The sweep shows no ownership signal at that position.',
    'Control battery ceiling: 0.3227.',
]
print('old   new   number   sentence')
for c in claims:
    print(f'{bool(re.search(OLD,c,re.I)):<5} {bool(re.search(NEW,c,re.I)):<5} '
          f'{bool(re.search(NUM,c)):<8} {c[:48]}')
"
old   new   number   sentence
0     1     0        Every output printed below was produced by runni
0     1     0        We verify both ceilings against the attack sweep
0     1     0        Verification of the clause is filed with the run
0     1     0        The endpoint records were checked before the gat
0     1     0        The sweep shows no ownership signal at that posi
0     0     1        Control battery ceiling: 0.3227.
```

The old list catches none of the six. The widened list catches five. The sixth is
a bare number with no verb anywhere near it, and only the number sweep finds it —
which is why part one is two commands and not one.

**What part one still cannot catch, plainly.** A claim of measurement written in
words nobody put in the pattern: "the two batteries came out the same", "this
held on all three checkpoints", "the gate opened". A claim carried by a table
with no sentence around it. A claim in a figure caption or a file name. And the
sweeps cannot tell a claim from a quotation of one, or from a sentence that says
a measurement was *not* made — every hit still has to be read. Part one narrows
the reading; it does not replace it.

*Part two: for each sentence the first part returns, name the file it cites and
run the one command that regenerates the number. Two worked examples, both from
the failures above:*

```
$ grep -c control experiments/06-mvm-0a-constructed-self-index/src/shortcut_sweep.py
0
```

*A practical warning about that one.* `grep -c` exits with status 1 when the
count is zero, because "nothing matched" is grep's failure status whether or not
you asked it to count. A session running this pass inside a script that stops on
the first failing command will stop right here, on the example whose answer is
the point. Run these by hand, or make the script tolerate it — appending
`|| true` to the line is enough — and never read a stopped script as a passed
test.

```
$ python3 -c "
import json
base = 'experiments/06-mvm-0a-constructed-self-index/a3-gates/'
for p in ('endpoint_a3_30m_seed1.json', 'endpoint_a3_30m_seed2.json', 'pilot_endpoint.json'):
    print(p, len(json.load(open(base + p))))
"
endpoint_a3_30m_seed1.json 15
endpoint_a3_30m_seed2.json 15
pilot_endpoint.json 7
```

The first says that the module the registered sentence credits with verifying the
control battery's ceiling does not mention that battery once. The second says
where 110 came from: nowhere.

**It fails if** a sentence claiming a measurement names no file; or names a file
that does not contain the number; or names a file that exists at no commit, which
is its own recurring form — the citation defect that stopped the previous version
of the Amendment A3 closure text was exactly this (`RT-145` in the red-team
ledger, the finding that a registration commit was resting on a ruling file that
had not been committed). A registration commit is the one commit that may not
rest on a record its reader cannot open.

---

## 5. A command that creates something while documented as creating nothing

**What it was.** The staged plan for the rehearsal's one rented slice opened
with a step headed "prove the plan with no machine and no money". Its first
line ran a launcher with `--help`. The launcher had no `--help`. It had no
handling for command-line arguments at all — no `case "$1"`, no `getopts`,
nothing anywhere in the file. So the flag was not rejected and not reported.
It was **silently ignored**, and the script carried on exactly as it does when
run with no arguments, which is the real launch at its built-in defaults: the
30-million-parameter seed-0 recipe, 585,544,960 tokens, about ten hours and
about ten dollars, writing into the directory on the network volume where the
registered seed-0 artifacts already live.

**How it showed up.** By creating a rented machine, on 2026-09-21, in a
session whose authorisation was for a different and much smaller run. The
machine (`f1vtz2adz4dj8v`) was deleted about a minute later and cost about two
cents. The full account is the 2026-09-21 row of the compute ledger
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`) and the
annotation beneath it. It is filed in the red-team ledger as `RT-198`, the
silent-argument finding.

**The two cents are not the finding, and this is the part worth keeping.** The
command was run with its output piped through `head`, which closed the pipe
and killed the script before it reached the remote steps. That pipe is the
only reason anybody saw a machine being created. Run exactly as the plan wrote
it — with the output sent to `/dev/null`, which is what the plan said — there
is no early death and there is nothing on screen. The script runs to
completion in silence. **The difference between a two-cent finding and a
ten-dollar one with registered data underneath it was an incidental `head` in
a pipeline**, and John's ruling of 2026-09-22 draws the general lesson: a
mitigation that depends on the operator noticing is not a mitigation.

**Where the bad line came from**, because it will be written again. The plan
was generated by `stage_rented_slice.sh`, and that script **does** implement
`--help`, at its line 68. The session writing the plan generalised from the
script in its hands, which supports `--help`, to a script that does not. The
person writing the instructions is exactly the person who does not know, which
is why the guard has to live in the thing being invoked.

**What was recorded when it happened.** This block is the output of the
command as it behaved before the fix. **Do not run it.** It is printed because
a failure mode with no record of the failure is a citation, and because the
guard below cannot be shown to catch anything unless what it catches is
written down. The launcher no longer behaves this way; the registered launcher
`launch_a3.sh` still does, which is why the standing prohibition exists.

```
$ ./launch_a3_fetch_first.sh --help          # DO NOT RUN — this creates a machine
local pre-flight: module self-tests
  ok: curriculum_a3
  ok: encoding_a3
  ok: train_a3
  ok: frozen batteries present
creating SECURE pod (NVIDIA GeForce RTX 5090) for 30M/585544960 tok (out: a3_30m_seed0)
  run dir: /workspace/mvm-out (network volume — survives pod death)
{
  "costPerHr": 0.99,
  "desiredStatus": "RUNNING",
  "id": "f1vtz2adz4dj8v",
  ...
}
```

**The fix.** A guard at the top of each launcher, before any other work, which
refuses any argument, says what it got, names `DRYRUN=1` as the way to preview
a launch, and **exits explicitly** rather than relying on the shell to stop —
these files run under `set -uo pipefail` and deliberately not `set -e`, so a
guard that only complained would complain and launch anyway. The reasoning is
in `experiments/06-mvm-0a-constructed-self-index/argument-guard-method.md`,
committed before the code.

It is on the three unregistered launchers now. `launch_a3.sh` is registered
text and goes to Gate A as an amendment; until that clears, **no session
invokes a registered launcher with any argument**, and the test below asserts
it.

**The test.** One command. It creates nothing, spends nothing, and never runs
the registered launcher — running that with an argument is the very thing
being forbidden, so it is checked by reading its text instead.

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
```

```
RT-198 — launchers must refuse arguments rather than launch

unregistered launchers: an argument is refused
  [ ok ] launch_a3_fetch_first.sh refuses an argument (exit 2)
  [ ok ] launch_a3_fetch_first.sh says why it refused
  [ ok ] launch_a3_fetch_first.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_a3_fetch_first.sh guard (line 104) precedes any vendor command (line 227)
  [ ok ] launch_ctl_pilot.sh refuses an argument (exit 2)
  [ ok ] launch_ctl_pilot.sh says why it refused
  [ ok ] launch_ctl_pilot.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_ctl_pilot.sh guard (line 87) precedes any vendor command (line 201)
  [ ok ] launch_pilot_a1.sh refuses an argument (exit 2)
  [ ok ] launch_pilot_a1.sh says why it refused
  [ ok ] launch_pilot_a1.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_pilot_a1.sh guard (line 42) precedes any vendor command (line 99)

unregistered launchers: the guard did not break the real path
  [ ok ] launch_a3_fetch_first.sh dry run still exits 0
  [ ok ] launch_a3_fetch_first.sh dry run still creates nothing
  [ ok ] launch_ctl_pilot.sh dry run still exits 0
  [ ok ] launch_ctl_pilot.sh dry run still creates nothing
  [ ok ] launch_pilot_a1.sh dry run still exits 0
  [ ok ] launch_pilot_a1.sh dry run still creates nothing

registered launcher: read, never run
  [ ok ] launch_a3.sh does NOT carry the guard, which is expected before Gate A

  ***********************************************************************
  STANDING PROHIBITION, in force until the Gate A amendment clears:
  launch_a3.sh is REGISTERED TEXT and still has NO argument handling.
  An argument passed to it is SILENTLY IGNORED and it proceeds to a REAL
  LAUNCH at its defaults -- about ten hours and about ten dollars,
  writing into the registered seed-0 directory on the network volume.

      NO SESSION INVOKES A REGISTERED LAUNCHER WITH ANY ARGUMENT.

  To preview it without creating anything:  DRYRUN=1 ./launch_a3.sh
  Ruled by John 2026-09-22. Method: ../argument-guard-method.md [RT-198]
  ***********************************************************************


negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

**What the output has to show**, for any design this is pointed at: every
launcher that can create a rented machine refuses an argument with exit status
2; each guard sits before that file's first vendor command; every dry run
still exits 0 and still reports creating nothing; and the negative control
rejects an unguarded stand-in. **That last one is what makes the rest worth
reading.** A test that can only pass proves nothing, so the check builds a
stand-in with the pre-2026-09-22 shape — a script that ignores its arguments
and carries on — and requires the checks to reject it. If the control ever
reports the unguarded stand-in passing, the harness has stopped measuring what
it claims to.

**The line that is expected to change.** While `launch_a3.sh` remains
registered and unguarded, the check prints the standing prohibition and still
exits 0, because an unguarded registered launcher is the expected state before
Gate A rather than a failure. When the amendment lands, that file moves into
the list whose refusal is exercised, and the prohibition block goes away. A
session reading this entry after that point should expect the output above to
differ in exactly that respect and in no other.

---

## 6. A remote step tested only against stand-ins

*Added 2026-09-25 (Pacific). John ruled the addition on 2026-09-25 ("agreed
on all", on section 7 of `docs/2026-09-25-rented-slice-findings.md`, whose
item 3 proposed it). The session that wrote this entry also wrote the fix it
describes; under the pairing rule a different session checks both. The
opening section of this file still counts five failures and fifteen printed
blocks: it predates this entry and is left as written.*

**What it was.** A command sent to a rented machine over `ssh` whose every
test replaced `ssh` with a stand-in. The command was the one that starts the
machine's own shutdown watcher, line 467 of
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`
at commit `4d98cfc`, in the form `cd /root/mvm/src && nohup sh reap_agent.sh
… >> …/reaper.log 2>&1 < /dev/null &`. In that form the `&` sends the whole
`cd && nohup` chain to the background as one subshell. The redirections
apply to `nohup` only, so the subshell keeps the connection's output open
until the watcher exits, and `ssh` waits for it. The watcher runs until its
+24-hour deadline. Every test of the launcher used a stand-in `ssh` that
exits at once (`reap_handshake_selftest.sh` sets `SSH="$BIN/fakessh"`), and a
stand-in that exits at once returns at once **whatever the remote command
does**. So no test could have seen the hang. The same file had already met
the same hang, on the training start, in August 2026: its comment says "this
ssh can HANG after the remote nohup succeeds", and that call had been capped
at 60 seconds ever since. The watcher start, added on 2026-09-21, was not.

**How it showed up.** On the first real `ssh` that line ever met, on
2026-09-25, during the rented slice. The launcher hung for about 30 minutes
after the watcher had started, never reaching the timing step, the training
or the laptop watchdog. A session watching the log stopped it and deleted
the machine; it cost $0.4974, and neither measurement was taken (the
2026-09-25 row of `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`,
and `docs/2026-09-25-rented-slice-findings.md` sections 4 and 5).
**Unattended, nothing on the laptop would have deleted the machine** — the
laptop watchdog is spawned after training starts — so it would have billed
until its own +24-hour deadline, about $24 against a hard cap of $2.00
(findings section 5, ARGUED there from the watcher's code).

**Why this is a species and not an instance of failure 5.** Failure 5 is a
command that does something its documentation says it does not. This one
does exactly what it says; what was wrong was the evidence that it worked.
A stand-in is built to answer the way the far end is *expected* to answer,
so a test against it can only confirm the expectation. The more a remote
step's behaviour depends on the far end — how a shell backgrounds a job,
what a vendor's tool accepts, what a machine carries — the less a stand-in
test says about it. The shutdown handshake itself was, until 2026-09-25,
"verified against local stand-ins only" in its own author's words
(`experiments/rehearsal-successor-measure/src/stage_rented_slice.sh`,
header), and the slice existed to close exactly that gap.

**The fix.** Ruled by John 2026-09-25. The watcher start now runs only
`nohup` in the background, with all its output redirected (`cd … || exit 1;
nohup … &`), so nothing holds the connection; and the `ssh` that sends it is
cut off at 60 seconds whatever happens, the same cap the training start
has. The laptop's machine deadline (`src/machine_deadline.sh`) bounds the
money if some other remote step hangs.

**The reproduction, with nothing rented.** The findings reproduced the hang
on the laptop by putting `| cat` where `ssh` would be: like `ssh`, `cat`
waits until everything on the far side has closed its output. Re-run on
2026-09-25 (Pacific) by the session that wrote this entry, first the
findings' own two commands, then the launcher's real old and new watcher
forms with the watcher replaced by `sleep 8`:

```
== the findings' reproduction, rerun 2026-09-26T00:49:55Z (2026-09-25 Pacific)
form as launched (cd && nohup ... &): returned after 8s
control (cd ; nohup ... &): returned after 0s
== the launcher's watcher-start form, old (line 467 at 4d98cfc) and new, with the watcher replaced by sleep 8
OLD  cd … && nohup … &        : returned after 8s
NEW  cd … || exit 1; nohup … & : returned after 0s
(a background sleep 8 is still running after the new form returned: it was started, not skipped)
```

The script that printed this is filed as
`experiments/rehearsal-successor-measure/out/launcher-fix-2026-09-25/hang-reproduction.sh`,
beside its output.

**The test.** One command. It rents nothing and contacts no vendor. For each
command a launcher sends over `ssh` that starts something in the background
(it contains `nohup`), it rewrites the command to run on this laptop, with
the backgrounded program replaced by a stand-in that leaves a marker file and
holds for 8 seconds, runs it through `bash -c '…' | cat`, and times it. A
start that returns in under 2 seconds passes. One that holds the connection
passes only if the launcher cuts that `ssh` off with a time cap. One that
holds and is not capped fails. A start whose stand-in never ran fails too,
because a command that returns at once by doing nothing has not been shown
to return at once. Then a negative control, the pre-fix form, must be
rejected.

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
```

```
remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds 8s)

launch_a3_fetch_first.sh
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)

negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang

all checks pass. Nothing was rented and nothing was spent.
```

**It fails on the design that produced the finding.** Pointed at the
launcher as it was at `4d98cfc`, the commit the slice ran:

```
$ git show 4d98cfc:experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh > "$TMPDIR/launcher-4d98cfc.sh"
$ LAUNCHER="$TMPDIR/launcher-4d98cfc.sh" experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
```

```
remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds 8s)

launcher-4d98cfc.sh
  [FAIL] launcher-4d98cfc.sh line 467: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] launcher-4d98cfc.sh line 547: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 552)

negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.2s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang

1 problem(s). Nothing was rented and nothing was spent.
```

Both outputs were produced on 2026-09-25 (Pacific) by the session that wrote
this entry, and no other session has re-run them. **The timings are wall
clock**, so a re-run will differ from the text above by a tenth of a second
here and there; compare the verdicts and the whole seconds, not the bytes.
The line numbers are those of the file at the commit this entry landed in,
and move when the launcher is edited.

**What the output has to show**, for any design this is pointed at: every
background start a launcher sends over `ssh` either returns at once or is
cut off by a time cap in the launcher; no start is reported as never having
run; and the negative control is rejected. **The control is what makes the
rest worth reading.** If it is ever accepted, the check has stopped
measuring what it claims to.

**What this test does not cover, stated so it is not read as covering it
(ARGUED).** It catches one way a remote step can differ from its stand-in:
a background job holding the connection. The species is wider. A vendor
tool on the machine that takes different arguments from the laptop's (the
2026-09-17 finding recorded at the verb-first check in the launcher), a
credential the machine does not carry (2026-09-16), a path that exists only
on the laptop — none of these is exercised here, and none can be by any
check that does not reach the real far end or a faithful copy of it. The
general discipline, for which no single command exists: **before a remote
step is counted as tested, say what stood in for the far end, and what that
stand-in cannot do that the far end can.** A test run only against a
stand-in is evidence about the stand-in.

---

## Adding to this list

A fatal finding that is a new species — not a new instance of one of the four
above — is added here by the pass that found it, with its test written the same
way: a command, and what the output has to show. Write the test so that a session
holding a different design can run it without asking anyone what it means.

An entry here is binding text under the protocol's pairing rule, so a session
other than the one that wrote it checks the entry: that the test runs, and that
it fails on the design that produced the finding. A test that has never been seen
to fail has not been shown to detect anything.

The list is added to and not shortened. A failure that has stopped recurring is a
failure whose test is passing, which is the reason to keep running it rather than
a reason to drop it.
===== END OF RECORD 23 =====

===== RECORD 24 of 25 - the opening description of the closed design's task grammar, which version 4 says its grammar extends (inside finding RT-239) - `experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py` (lines 1 to 118 of the file's 650, unedited) =====
"""The Amendment A3 Candidate A curriculum — "act as yourself".

A3 §2.2: the objective must make the correct output at a supervised
position depend on which agent the model is, must ground ownership only
in the act (the acting channel), and must supervise an action rather than
a report. This module builds that grammar. `curriculum.py` is left
byte-identical: every record in `lesion-results/` and `null-calibration/`
reproduces against it, and the five existing checkpoints were trained on
it.

The episode
-----------
Twelve turns, four agents, two *contested* items:

- **Eight assignment turns.** Each agent assigns each contested item
  exactly once, in one random permutation of the eight (agent, item)
  pairs. Within an item the four values are **distinct**, so an item's
  four assignments differ only in who made them.
- **Four revision turns**, last, in random order: **every agent revises
  exactly once**, two agents on each contested item, with the pairing
  drawn by a uniform shuffle.
- **The revision rule is deterministic and shared**: the revised value is
  the successor of *that agent's own earlier value on that item*, over
  the eight slots, modulo eight. Every agent obeys it; the generator
  applies it to the other agents and the enactment harness applies it to
  the model.

Every agent therefore has exactly three turns, two assignments and one
revision, and sits in the assignment block and the revision block equally
often. Nothing about how much an agent speaks, where, or whether it
revises can predict which agent the model is.

Why exactly one own revision per episode
---------------------------------------
Gate 0 measured the cost of the alternative. Under the registered
grammar the revision-conditioned battery harvests one scoring cell from
about one episode in twenty, so at 400 episodes it is a 19-item cell
whose null band is two items flipping
(`gate0-null-calibration-findings.md`, reading 2). A3 decision 12 sets
verdict cells at n=400. One own revision per episode is what makes 400
episodes yield 400 `T_act` cells instead of about 20.

Why *every* agent revises, which the first draft of this module got wrong
------------------------------------------------------------------------
The first version gave the model one revision and one other agent one
revision, and left the remaining two agents with assignments only. Its
own self-test killed it: the model's slot then always had three turns
while two other agents had two, so **agent turn count predicted
ownership perfectly** (3 turns for the model every time, against 0.43 of
other-agent turns), and revision status predicted it at 0.33 against
0.14. That is the same class of defect the registered grammar hit when a
red-team patch made the revision always final and always the model's
(`curriculum.py`, `_episode_skeleton`), and it is what gate (i) exists to
catch. Giving every agent exactly one revision removes both cues by
construction rather than by measurement.

What a solver without a self-index can do
-----------------------------------------
At its own revision turn the model sees four distinct earlier values for
that item and must emit the successor of its own. Position is randomised,
markers are a per-episode draw, and every agent's values come from the
same distribution, so nothing in the text distinguishes the four.

Two agents revise each item, so if the *other* agent revising the model's
item goes first, a solver can invert the rule on that revision and strike
one candidate. The model revises first half the time. **The lookup
ceiling is therefore 0.25 on half the cells and 0.333 on the other half,
0.292 overall**, against a chance floor of 0.125. That is above the 0.25
A3 §2.2 pre-states, and the discrepancy is real rather than cosmetic: it
is the price of making every agent revise, which is what removes the
ownership cue above. Red-team pass 3 should either adopt 0.292 as the
pre-stated ceiling or buy 0.25 back by adding a third contested item that
nobody revises, at about a third more compute per run.

**An honest limit on the design's central claim.** A3 §2.2 says the only
route from the ceiling to 1.0 is to have bound the act to the item when
acting and carried that binding forward. There is a second route. The
revision turn renders as "<marker> assign <item> to <value>", so at the
moment the model acts, its own marker is in the context three tokens
back. A model could learn "the marker at a position where I am acting is
mine", then retrieve that marker's earlier value by ordinary
marker-keyed lookup — reading a name badge at act time rather than
carrying a binding. Both routes need the acting channel and both collapse
under the L0 lesion, so L0 does not separate them. A3 already registers
the discriminator: the mid-episode re-indexing probe of the H_tag bin.
The claim in §2.2 should be narrowed to say so.

Batteries
---------
- **T_act** (primary, an action not a report): the value emitted at the
  model's own revision position. Chance 0.125, lookup ceiling 0.25.
  Carried on the episode as `act_target`, scored at that position.
- **T_other**: a forced-choice counterfactual naming another agent —
  "where did <marker> assign <item> to next ?" — on the contested item
  that agent did *not* revise, so the answer appears in no turn and must
  be computed from its earlier value. Same rule, same binding demand, no
  self-reference. Chance 0.125. Two of the item's four values are struck
  by the two revisions a solver can invert, so its lookup ceiling is
  0.5 — higher than T_act's, which red-team pass 3 should weigh, since
  the H_generic-binding bin turns on the difference between the two
  batteries' drops.

  [2026-09-17, REGISTERED DEFECT. The comment above is left as written.
  Red-team pass 3 ran and did NOT weigh it. The registered ceiling is
  0.3227, not the 0.5 stated here, and NEITHER figure was ever checked
  against an adversary: shortcut_sweep.py attacks only T_act. Worse, the
  solver in measured_ceilings below never reads the marker the T_other
  question names, so 0.3227 is a name-BLIND score and this battery's real
  ceiling is near 1.0, unmeasured. No result changes; the control fails
  its floor under every reading. See ceiling-defect-2026-09-17.md.]
- **T_state**, **T_syntax**: unchanged in kind from the registered
  grammar (RT-05 competitor, and the floor check).

Corrigibility: this module generates data. It trains nothing, launches
nothing and costs nothing [C1/C2].

    ../../../.venv/bin/python curriculum_a3.py --self-test
"""
===== END OF RECORD 24 =====

===== RECORD 25 of 25 - the opening description of the rehearsal's task grammar (inside finding RT-239) - `experiments/rehearsal-successor-measure/src/grammar.py` (lines 1 to 70 of the file's 485, unedited) =====
"""The matched-role revision grammar, shrunk to rehearsal scale.

UNREGISTERED. This is a stand-in built for the measurement rehearsal of the
successor experiment proposal (`docs/successor-experiment-proposal-2026-09-21.md`,
section 4). It is not the registered generator, it trains nothing on its own,
it costs nothing, and no result about the scientific question may be read off
anything it produces.

What one episode is
-------------------
Four agents, two items, eight value slots, and a closed vocabulary.

- **Eight assignment turns**, one per (agent, item) pair, in a uniformly
  random order, rendered `<marker> assign <item> <value>`. Within an item the
  four values are distinct, so the four assignments differ only in who made
  them.
- **Two action turns**, last, in a random order between them, rendered
  `<act> revise <who> <item> <ans> <mask>`:
    * **own-directed** — `<who>` is the special word meaning *your own*, and
      the answer is the successor of the model's own earlier value on that
      item;
    * **named-other-directed** — `<who>` is another agent's marker word, and
      the answer is the successor of that agent's earlier value on that item.
  Both are actions at the model's own turn, supervised the same way and
  scored the same way. That is the whole point of the redesign the proposal
  makes: in the closed Amendment A3 design the ownership condition was an
  action and its comparison was a question at the end of the episode, so the
  two were never at the same kind of position.

Two departures from the registered A3 grammar, both deliberate
--------------------------------------------------------------
1. **The action turn carries no marker word.** In `curriculum_a3.py` the
   model's own turn renders its own marker three tokens before it acts, and
   that module's own header records the consequence as an honest limit: a
   model can read a name badge at the moment it acts instead of having
   carried a binding. Here the only route to the ownership answer is the
   acting channel.
2. **The answer token is never shown.** The slot where the answer goes is a
   dedicated `<mask>` word in the input, and the model's prediction is read
   at that position. Nothing downstream ever sees the answer.

Together these make a matched pair of episodes — the same content with a
different agent being the model — come out **token-for-token identical**,
differing only in which positions the acting channel fires on. That is what
lets a transplant between the two be a clean comparison: nothing but
ownership can differ anywhere in the state.

What is matched, and checked rather than asserted (proposal section 4.2)
------------------------------------------------------------------------
1. candidate count: four earlier values in context in both conditions;
2. distance: the gap between source assignment and action, same distribution;
3. supervision: one supervised position of each kind, one scored token each;
4. transformation: the same successor rule in both conditions.

Carried-forward rules from the red-team ledger of experiment 06
---------------------------------------------------------------
- the **even-split rule** (ledger item `RT-58`, the batch-split bias check):
  any batch fraction that splits rows must not cut the generator's matched
  pairs;
- the **one-scored-token check** (ledger item `RT-59`, the check that exactly
  one token per supervised position is scored and that the check survives the
  shift the loss function applies). Here the answer is scored **at** the
  `<mask>` position rather than at the position before it, so the shift does
  not arise; the self-test asserts that too, rather than leaving it implied.

Corrigibility: this module generates data. It trains nothing, launches
nothing, rents nothing and costs nothing [C1/C2].

    ../../../.venv/bin/python grammar.py --self-test
"""
===== END OF RECORD 25 =====

*End of the packet. Answer the brief (record 1) now. Label your findings G1, G2, G3 and so on.*
