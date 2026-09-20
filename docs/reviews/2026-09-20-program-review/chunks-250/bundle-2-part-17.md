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


===== FILE: docs/step4-control-battery-proposal-2026-09-20.md =====

# Public path step 4 — the control-battery decision (2026-10-04): proposal

*Drafted 2026-09-20 (Pacific) in a Cowork session. Status: DRAFT. Under
Gate C of `docs/outside-review-protocol.md` this proposal gets a tier 1
pass (a context-isolated Claude Code session, packet at
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-step4-proposal-packet.md`)
before it reaches John. Nothing here is registered text and no spend is
authorised by it. Written under the workspace plain-language rule.*

## The question as the roadmap states it

Public path step 4 (`docs/public-path-roadmap-2026-09-16.md`): decide the
control-battery question, a registered amendment that makes the control
learn reliably, or close Amendment A3 with partial discriminators and say
so. Without this no future run can return a full verdict.

## What has been settled since the roadmap was written

1. **The registered differential clause is uncomputable for any model.**
   The control battery's true ownership-blind ceiling is 1.0
   (`ceiling-measurement-findings.md`, 2026-09-17), so under the
   registered floor rule its drop is undefined at every possible score.
   The clause has been unsatisfiable since registration. This is a
   property of the clause, not of the training.
2. **Amendment A4, the separation-scored replacement clause, was refused**
   on 2026-09-19 on the independent red team's findings (`red-team-a4.md`,
   F1 to F22). What any replacement clause must satisfy is written down in
   `separation-clause-requirements.md` (H1 to H6), with three pre-stated
   tiers for reading the control-learnability pilot.
3. **The control-learnability pilot landed in Tier C.** The pre-stated
   tiers (Part 2 of the requirements, written before the pilot reported)
   say a separation clause is registerable only if the control's intact
   score, mean minus one spread, reaches 0.375. The pilot read 0.3125
   (sd 0.0240), so 0.2885 against the bar. Tier C, in the requirements'
   own words: "the control does not learn enough for any comparison to
   move; the result is reported as the matched contrast remaining unmet,
   and the next design question is the grammar, not the clause."
4. **What the pilot did and did not show** (Gate B review, ledger RT-52 to
   RT-69, ruled 2026-09-20). Reweighting the rows the control already had,
   four times the per-row weight and two thirds of the query gradient,
   moved it from 0.2877 to 0.3125 on the matched seed, about 1.6 standard
   errors, less than a tenth of the way to 0.60. The battery has learned
   the whole name-blind procedure (95% of the way from chance to the
   name-blind solver's 0.3227) and none of the name-keyed lookup. One seed,
   one dose. The run says nothing about a different and easier question
   taught first (option D), which is a grammar change, not a reweighting.
5. **The corrected floor rule.** Even under the old 0.3227 reference, the
   control needed 0.4227 for its drop to be defined
   (`control-battery-proposal.md`), so the whole band a rerun could land in
   would change nothing for A3. Under the true ceiling of 1.0 the point is
   moot: nothing changes A3.
6. **The ceiling precondition** ruled 2026-09-17 stands: any option that
   keeps this battery measures its ceiling properly first.

## The options, narrowed

Options B (eval-side change to the denominator) and E (train longer or
bigger) were rejected and fenced on 2026-09-17 and stay so. Option C
(reweight the existing rows) is what the pilot ran and it is closed. Two
remain.

**A. Close Amendment A3 with partial discriminators.** Report the primary
result (learnable, ownership-specific, replicates on three seeds), the
instrument audit (the clause was never computable; the control never
learned the name-keyed lookup under two supervision regimes), and the
comparison that was never available, all plainly. Cost $0. What the paper
can then claim: a structural signature of ownership-specific learning in
small constructed models, with the matched contrast unmet. The
discriminators that do not need the control (the matched other-agent
lesion, the random matched subspaces, the swap probe) run through the
localization stack, which is parked at *not testable (localization)*
until causal patching runs; so A is honest and thin unless patching runs
too.

**D. A grammar redesign with a scaffolded intermediate query, under a new
registration.** Teach plain name-keyed retrieval first, then the rule.
This is not an amendment to A3: the requirements document says a clause
built on a changed loss "belongs to a redesign with its own
registration", and a grammar change re-freezes the batteries, the cue
gates and the attack sweep. Cost: three seeds at $27 to $39 plus the
re-freeze, inside the A3 headroom ($55.7 of the $100 stop) only if the
redesign is charged there; otherwise a new line in the ledger. What it
buys: a control battery that can reach Tier A or B, and with it a
separation clause meeting H1 to H6, and a full verdict. What it risks:
the three non-supervision explanations (reversed rendering, missing
private route, answer in no turn) are all about the grammar, and D
addresses only the first of them directly.

## Recommendation

**A, with causal patching run before closure, and D deferred to a
successor experiment after public release.**

Reasons, in order of weight:

1. The release date is 2026-11-22 and the pipeline resumes 2027-01-04. D
   is a new registration (Gate A, both review tiers, closure rule), a
   re-freeze, three seeds, endpoint reads, and its own Gate B, in the same
   window as the paper draft (step 6, 2026-10-25) and the outside reader
   (step 7, 2026-11-08). It does not fit without moving the release.
2. Tier C was pre-stated as "the next design question is the grammar".
   A grammar redesign is a new experiment and should be numbered as one,
   with its own pre-registration, not folded into A3's closure.
3. What A lacks is not the control; it is the second leg of the
   localization requirement. Amendment A3 §3.2 needs probe and causal
   patching to agree before anything counts as localized, and patching
   has never run (ledger RT-49, RT-92). Running it on the existing
   checkpoints is local and $0 (the lesion machinery exists) and turns
   "not testable (localization)" into either a localized result or a
   registered null with both instruments. That is worth more to the paper
   than a learned control would be.
4. D's honest cost is the risk that it also lands in Tier C, for the
   reasons the pilot could not test. That risk is better taken after the
   first paper is out, when a null costs a section rather than the
   release.

## What John is asked to rule

1. A or D.
2. If A: authorise the causal-patching design as a $0 local item, method
   committed before output, with its own Gate B; and the A3 closure text
   goes through Gate A (it is registered text).
3. If D: which experiment number it takes, which ledger line it is charged
   to, and whether the release date moves.
4. Either way: the two open $0 closures from the pilot review (RT-56,
   RT-58, RT-59) land before the closure text is drafted.

## What this proposal does not decide

The linear-read line (parked, two follow-up runs authorised 2026-09-20);
the paper's claim scope (step 8, unchanged: a structural signature of
self-indexing in small constructed models, never "a conscious machine");
the outside reader (step 7).


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-followup-runs-brief.md =====

# Brief — two follow-up runs after the fitted-read review

*Ruled 2026-09-20 (Pacific) as decision 3 on the Gate B review of the
fitted read (ledger RT-76 and RT-82; review file RT-58 and RT-64). Both
runs are local, $0, inference only, on captured states that already exist.
Under the execution-gates ruling of 2026-09-19 each needs its method
committed before any output, not a fresh go. The marker-word fitted read
(ledger RT-89, ~70 processor-hours) is deferred and is not part of this
brief.*

## Run 1 — the other-agent index at the eleven positions (registered matched control L2(a))

**Question.** The fitted read's one consistent pattern is at the other
agent's revision value: positive in fifteen tests of fifteen, one test on
seed 2 reaching MARGINAL. Is that a self-index carried away from an act
position, or an artefact of how own and other are excluded from each
other's positions? Amendment A3 §L2(a) registers the instrument that
separates them: the same localization run for a named non-self agent
("which marker is agent B's"), matched in rank and probe accuracy. It has
never been run.

**What to run.** `src/fitted_position_sweep_a3.py` unchanged except for
one new target function: the other agent's register index instead of the
model's own. Same eleven positions, five layers, three checkpoints, same
per-test seeding, same 200-draw null, same family-adjusted bar recomputed
for the tests actually run, same instrument check (the anchor numbers must
reproduce before any sweep number is computed). About eleven
processor-hours.

**Method file must pre-state:** the cells; what "the other-agent index is
found where the own index is not" would mean and what "found at the same
positions" would mean; the exclusion rule for positions where the other
agent's marker has not yet appeared; and that this run reads no verdict.

## Run 2 — the standardised refit at the nine positions (a declared second instrument)

**Question.** The fitted read leaves the 448 residual directions unscaled
under a squared penalty, which charges a quiet direction the square of
how quiet it is; the stack's own geometry measurement says ten directions
carry about 99% of the variation. Does a read that standardises each
direction first find anything the unscaled read could not?

**What to run.** The same sweep on the own register index, with each
residual direction standardised to unit variance on the training folds
before the fit, declared as a second instrument with its own anchor
reproduction (it will not reproduce the unscaled anchor numbers and must
not be read as failing the instrument check for that reason). Same
positions, layers, checkpoints, seeding, null, bar. About eleven
processor-hours.

**Method file must pre-state:** the standardisation (per fold, training
statistics only), the regularisation strength and how it was chosen
without looking at sweep results, the new anchor and its tolerance, and
the cells.

## Both runs

Report every cell, the detectable-signal size calibrated against the
read's own measured ceiling (not 1.0; see
`fitted-position-sweep-findings-CORRECTION-2026-09-20.md`), degeneracy
hits, and the geometry at each position if it is cheap. Findings may say
where each read finds the target and where it does not. They may not say
the linear-read line is closed or that anything is absent; the registered
term for the line's state is *not testable (localization)* until causal
patching runs. Both go through Gate B before entering STATUS.md.
