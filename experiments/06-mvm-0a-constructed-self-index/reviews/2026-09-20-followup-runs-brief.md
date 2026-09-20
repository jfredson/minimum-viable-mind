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
