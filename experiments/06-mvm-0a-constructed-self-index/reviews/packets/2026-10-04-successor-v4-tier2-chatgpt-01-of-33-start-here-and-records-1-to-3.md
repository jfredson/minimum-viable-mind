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

*This packet arrives as 33 files pasted into this one conversation, in order.
This is file 1. Do not begin your review until file 33 has arrived: reply to
each file with one short line saying you have it, and nothing else. Read each
file as text, start to finish, rather than searching it. The brief you are
answering is record 1, in this file. Label your findings A1, A2, A3 and so on.*

*If a file arrives cut short, or the app turns one into an attachment you can
only search rather than read, say so at once and name the file, before going
on.*

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

