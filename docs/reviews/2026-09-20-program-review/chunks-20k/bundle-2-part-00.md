# Bundle 2 of 3: what happened

Verbatim concatenation of committed repository files, built by make-bundles.sh. Nothing is edited or abridged except STATUS.md, of which only the current-state sections (2026-09-19 and 2026-09-20) and the short "arc" section are included; the older entries are in the repository's git history and in bundle 3 on request. Each file begins with `===== FILE: <path> =====`.

Contents, in order:
1. STATUS.md, current-state sections only
2. experiments/01-self-indexing-removal-test/removal-test-findings.md
3. experiments/03-retained-independence/results.md
4. experiments/06-.../gate2-pilot-findings.md (A3 pilot)
5. experiments/06-.../seeds-endpoint-findings.md (A3 seeds 1 and 2)
6. experiments/06-.../register-lesion-findings.md, register-saturation-findings.md, register-direct-probe-findings.md
7. experiments/06-.../ceiling-measurement-findings.md and ceiling-defect-2026-09-17.md
8. experiments/06-.../control-learnability-pilot-findings.md
9. experiments/06-.../blind-arm-findings.md and blind-control-findings.md
10. experiments/06-.../powered-position-sweep-findings.md
11. experiments/06-.../fitted-position-sweep-findings.md and its 2026-09-20 correction
12. experiments/06-.../separation-clause-requirements.md
13. experiments/06-.../red_team_ledger.md (RT-01 to RT-93, every ruling)
14. docs/outside-review-protocol.md
15. docs/step4-control-battery-proposal-2026-09-20.md (draft, the 2026-10-04 decision)
16. experiments/06-.../reviews/2026-09-20-followup-runs-brief.md


===== FILE: STATUS.md (current-state sections and "The arc" only) =====

# STATUS — where we are, how to resume

*Living handoff doc. Update it at the end of a working session so the next one (you, or Claude in a fresh session) can pick up without re-deriving context. Most recent state at top.*

## WHERE THINGS STAND 2026-09-20 — the control battery converges on the name-blind solver even with its own loss term; the fitted read finds nothing on the register index; the linear-read line is parked as *not testable (localization)*; step 4 narrows to option D or closing A3

*This section is the current state. Everything below it is the older
record, newest first, and is left exactly as written.*

Both entries below went through Gate B of `docs/outside-review-protocol.md`
before entering here. Reviews: `reviews/2026-09-20-control-learnability-claude-worktree.md`
(PR 7, ledger RT-52 to RT-69) and `reviews/2026-09-20-fitted-read-claude-worktree.md`
(PR 8, ledger RT-70 to RT-93). John ruled on all forty-two findings on
2026-09-20; every ruling is in `red_team_ledger.md`.

### The control-learnability pilot (unregistered, $9.97, ruled for the record)

Giving the control battery its own loss term, four times the per-row weight
and two thirds of the query gradient instead of one third (`ee7fc91`,
`launch_ctl_pilot.sh`, one 30M register-less run, seed 0, full 55,116-step
budget), left it at 0.3125 (sd 0.0240 across six evaluation seeds), against
0.2877 on the matched checkpoint that received none of it: still on the
shoulder of a solver that cannot read the name the question supplies, and
nowhere near the 0.60 that would show it had learned to read it.
Reweighting the rows it already had is not what this battery is missing.
The battery has learned the whole name-blind procedure, 95% of the way from
chance (0.125) to the name-blind solver (0.3227), and none of the name-keyed
lookup, which is what the three remaining explanations are all about (the
reversed rendering, the missing private route, an answer that appears in no
turn). Pre-stated cell: DID NOT LEARN. Both secondary cells pass: the primary
battery learns at 0.5727 and collapses under its lesion to 0.1663. One seed,
one dose; the matched comparison moved +0.0248 at a standard error of 0.0157,
in the intervention's direction and not significant. The intervention also
tripled the whole query loss against the action term (RT-57), which any
future reweighting run holds fixed. Two $0 checks are open (RT-58, RT-59)
and the training log and trajectory are to be committed (RT-56).

What this settles for public path step 4 (2026-10-04): the operative bar
for this battery to be useful is 0.4227, not 0.3227 (the corrected floor
rule, `control-battery-proposal.md`), so any control below 0.4227 leaves
Amendment A3 exactly where it is today, and a rerun landing in PARTIAL would
change nothing. Step 4 narrows to option D (a scaffolded query that teaches
plain name-keyed retrieval first, which is a different and easier question,
not more supervision of the same rows) or closing A3 with partial
discriminators. Any option that keeps this battery inherits the 2026-09-17
ceiling precondition. Proposal: `docs/step4-control-battery-proposal-2026-09-20.md`
(draft, goes through a tier 1 pass before John rules, per Gate C).

### The fitted linear read at eleven positions (unregistered, $0, ruled for the record)

A fitted linear classifier, run at eleven positions and five layers on all
three 30-million-parameter checkpoints (`fitted-position-sweep-findings.md`,
PR 6), does not find the model's register index anywhere except at the
token where its own marker is the input. The controls held everywhere: the
register index reads at 34 to 54 standard deviations at that token on every
checkpoint, and the negative control shows no leak at the position where the
answer is not yet knowable. One test reached three standard deviations
without reaching the family-adjusted bar of 3.38, at the other agent's
revision value on seed 2; the same position is the highest testable position
on all three checkpoints and in all fifteen of its tests, and it is recorded
as an open item rather than a result. The run would have found a signal
legible in about one episode in eleven, not one in twenty-seven as the
findings state (RT-74; correction note beside the findings). This closes the
fitted read on the register index. It does not close the linear read: the
registered target is the model's own marker word, and no fitted read has
ever been run on it at these nine positions, only the difference-of-averages
read, which this run measures as recovering five to nineteen times less than
a fitted classifier on the same target at the same position. Neither "not
localized" nor "absent" may be said of any of this: Amendment A3 §3.2
requires probe and causal patching to agree before anything counts as
localized, patching has never been run, and the pre-registration reads a
probe-only null against a centre known to be load-bearing as instrument
failure. The registered term for where this stands is *not testable
(localization)*.

### Public path step 4, ruled early on 2026-09-20: Amendment A3 closes as *not testable*

The step 4 decision (dated 2026-10-04 on the roadmap) was ruled on
2026-09-20 on proposal version 2
(`docs/step4-control-battery-proposal-2026-09-20-v2.md`), after a Gate C
review of version 1 (`reviews/2026-09-20-step4-proposal-claude-worktree.md`,
PR 9, ledger RT-94 to RT-117, three fatal, all accepted). Rulings:

1. **Amendment A3 closes.** The grammar redesign with a scaffolded
   name-keyed query (option D) is a successor experiment with its own
   registration, after public release.
2. **The pre-registered loss condition has fired**: no non-self cross-turn
   control can be built that is state-requiring at ceiling (the
   2026-09-17 measurement: an ownership-free control and a
   ceiling-corrected metric are incompatible by construction). The
   registered word for the outcome is ***not testable***, and the closure
   text uses it, not "closed" and not "partial discriminators".
3. **Claim scope for A3**: the ownership input is load-bearing for the
   primary battery on three seeds (intact 0.5683 / 0.5633 / 0.5738,
   collapsing to 0.1988 / 0.2015 / 0.1447 under the input-channel lesion),
   and the matched contrast could not be run. "A structural signature of
   ownership-specific learning" is struck: the amendment's own text says
   the input-channel lesion removes a sense organ, not a structure the
   network built. Roadmap step 8's claim scope ("a structural signature of
   self-indexing in small constructed models") holds only if the
   localization line produces a localized result before the paper draft
   (step 6, 2026-10-25); otherwise the paper claims the sentence above.
4. **Localization order before any closure text**: the registered,
   unconditional blind-localization arm (step 3, 2026-09-27, $0), then the
   other-agent index control and the standardised refit (authorised
   2026-09-20, in progress), then causal patching designed as new code
   with its target and null written before it runs. Each through Gate B.
   Version 1's claim that patching was free with existing machinery was
   wrong: no patching code exists for this design.
5. **Before the closure text is drafted**: commit the pilot's training
   log and trajectory (the earlier deadline, before the proposal was
   filed, was missed and is recorded as missed in the ledger); run the
   two open $0 checks from the pilot review. The closure text is
   registered text and goes through Gate A.

### Next, ruled 2026-09-20

1. Two $0 local runs, method committed before output, brief at
   `reviews/2026-09-20-followup-runs-brief.md`: the other-agent index at the
   eleven positions (registered matched control L2(a), never run, ~11
   processor-hours) and the standardised refit at the nine positions (~11
   hours). The marker-word fitted read (~70 hours) is deferred.
2. The step 4 proposal goes to a tier 1 pass, then to John, before
   2026-10-04. Causal patching before A3 closes is its second item.
3. Closures for RT-56, RT-58, RT-59 (log and trajectory committed; two
   one-line checks).

## WHERE THINGS STAND 2026-09-19 (evening) — the eleven-position sweep finds nothing under a difference-of-averages read; the outside review says that closes one read, not the linear read; the outside-review protocol is in force


**The outside-review protocol is in force** (`docs/outside-review-protocol.md`,
ruled 2026-09-19). Interpretations that change direction go through a
context-isolated review before they enter this section. This entry is the
first to do so: the review is `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-19-linear-read-closure-claude-worktree.md`
with its addendum (PR 5), rulings RT-33 to RT-51 in `red_team_ledger.md`.

### The result, as ruled for the record

Across eleven positions and five layers on all three 30-million-parameter
checkpoints, a difference-of-averages read finds no own-agent identity,
neither the model's own marker word nor its register index, anywhere except
at the token where the marker is the current input (PR 4,
`powered-position-sweep-findings.md`). Zero of 270 testable tests reach 3
standard deviations, let alone the family-adjusted bar of 3.56; the largest
margin is +2.73. These are the first runs to use the registered probe
target, the marker word (RT-48). The sweep had real power: it would have
detected an identity legible in as few as 1.3% of episodes for the marker
word and 3.9% for the register index (RT-37). The controls held: the read
recovers the input token at up to 159 standard deviations, and the negative
control at the first own turn shows no leak there, and licenses no more than
that (RT-42). The positive control is strong on the pilot and weak on seeds
1 and 2, where it recovers the input token on about one episode in eight,
so a null on those two checkpoints means correspondingly less (RT-36).

**What this closes is the difference-of-averages read, not the linear
read.** A fitted linear classifier was never run at any of these positions
against a well-posed target, and in the one place both were tried, the
register index at the marker position, it read at about twice the accuracy
(0.48 to 0.535 against 0.25 to 0.33; `probe_target_diagnostic_a3_*.json`,
RT-33). Neither was causal patching, which the registration requires
alongside the probe before anything counts as localized (Amendment A3 §3.2,
RT-49). The registered probe position is the stronger result, because both
instruments find nothing there. Under the registered text, a null from one
leg of a two-leg procedure against ownership that is known to be
load-bearing reads as instrument failure, not absence, until patching has
run (RT-50). No registered result changes.

### Next, ruled 2026-09-19

1. The fitted linear classifier on the four-answer register-index target at
   all eleven positions, five layers, three checkpoints. Local, $0, existing
   code. Method committed before output. The line is retired, if at all, on
   what it returns. Brief: `reviews/2026-09-19-fitted-read-brief.md`.
2. Whether causal patching runs before A3 closes is added to the 2026-10-04
   control-battery decision (public path step 4) as its second item.
3. The pilot-versus-seeds legibility gap (RT-36) stays open.

## WHERE THINGS STAND 2026-09-19 — branch merged to main; the seeds replicate; the registered comparison turns out never to have been computable; the sensitivity rule is ruled, for future runs only


**The code is now on `main`.** The working branch
`gate0-null-calibration` — 63 commits, everything from Gate 0 through the
2026-09-17 ceiling measurement — was merged into `main` on 2026-09-19.
It is a **real merge, not a fast-forward**: `main` carried four commits
of its own (the RunPod support-ticket correspondence log, the wave-3
options memos and the week-37 review, and the ROADMAP v2 note that the
Stage 3 two-by-two clarification was signed off on 2026-08-02). **There
were no conflicts.** The branch is kept, not deleted.

### 1. The primary battery replicates on all three seeds

Registered endpoint reads, run locally at $0 against John's committed
threshold lock, which sets the bite threshold at 0.1777 on the primary
battery (`seeds-endpoint-findings.md`). Six independent evaluation
seeds, 800 episodes each, reported as a spread rather than one draw:

| checkpoint | intact | acting channel zeroed | corrected drop | vs the threshold |
|---|---|---|---|---|
| pilot (seed 0) | 0.5683 (sd 0.0076) | 0.1988 | 1.337 | 7.5× |
| seed 1 | 0.5633 (sd 0.0316) | 0.2015 | 1.342 | 7.6× |
| seed 2 | 0.5738 (sd 0.0284) | 0.1447 | 1.528 | 8.6× |

Three checkpoints trained from different seeds land within 0.011 of each
other intact, and removing the one authorship signal collapses all three
by seven to nine times the threshold. A drop above 1.0 means the lesion
pushed the battery **below** what a solver that knows nothing about
ownership can reach. The ownership-free batteries do not move: the
syntax battery is unchanged on every checkpoint, and the state battery
moves 0.0769 on seed 2 against its own 0.1172 threshold — reported
because it is the only asymmetry in the table, not because it fires.

**The objective is learnable and the learning genuinely depends on
ownership. That much is solid and replicated.**

### 2. The control battery never learned — on any seed

| checkpoint | intact | its ownership-blind ceiling | learned? |
|---|---|---|---|
| pilot (seed 0) | 0.2877 (sd 0.0302) | 0.3227 | no |
| seed 1 | 0.3057 (sd 0.0281) | 0.3227 | no |
| seed 2 | 0.3195 (sd 0.0150) | 0.3227 | no |

Three seeds, one outcome: **the control is not a seed lottery, it simply
does not learn under this design.** That was the modal case the ledger
wrote down against the wave *before* the go was given, and it came true.

Note the corrected bar recorded on 2026-09-17: the floor rule is not
"baseline below ceiling" but "baseline minus ceiling below 0.10", so the
control needs **0.4227**, not 0.3227, for its drop to be defined. The
three checkpoints miss by 0.135, 0.117 and 0.103 — four to forty times
wider than the raw ceiling gap suggests.

### 3. THE REGISTERED COMPARISON WAS NEVER COMPUTABLE BY ANY MODEL

The 2026-09-17 ceiling measurement (`ceiling-measurement-findings.md`,
method committed before running, no checkpoint loaded, $0) found that
**the control battery's ownership-blind ceiling is 1.0000, not the
registered 0.3227.** Two independent solvers reach a perfect score
without touching the model's own slot or the acting channel: a
hand-written one that reads the marker in the question and applies the
shared revision rule, and a learned one given only ownership-blind
features that found the same structure by itself. The harness proved
itself first, reproducing both registered reference values exactly to
four decimal places.

**Verdict A — structurally unsatisfiable.** With a ceiling of 1.0, a
defined drop needs a baseline of 1.10, and accuracy cannot exceed 1.0.
So the control's drop is undefined for *every possible model*, including
a hypothetical perfect one. The registered signature needs the primary
battery's drop minus the control's; one of its two terms can never
exist. **The clause has been dead since registration** — not since this
result, not since these seeds. This also moots candidates C and D of
`control-battery-proposal.md`, which tried to make the control learn:
making it learn was never the binding problem.

### 4. The localization instruments have no validated positive control

- **Registered blind-localization arm: NOT FLAGGED**, sub-bin
  *instrument failure to locate* (`blind-arm-findings.md`). No probe
  cleared its permutation null by the required three standard
  deviations; the best reached 1.3. Per John's 2026-09-16 ruling the
  committed verdict and its name **stand as written**, with a dated
  annotation beside them recording that the *interpretation* is
  superseded: the unblinded probe showed the register never encoded
  own-agent identity at any turn, so there was nothing at that location
  to find. Annotate, never rewrite.
- **Unregistered positive control: NOT TESTABLE** by the letter of the
  cells committed before the run (`blind-control-findings.md`). Every
  probe sat *below* its own null at all five depths. The ablation
  cleared the threshold in magnitude (−0.3516 against 0.1777) but with
  the **wrong sign** — it made the primary battery *better*, which a
  sensitivity test should never count as a bite.

**Consequence: no localization work runs until the stack has a validated
positive control.** The 2026-09-16 not-testable verdict is not reopened.

### 5. RULED 2026-09-19 — a bite is a degradation, and the rule binds future runs only

John ratified the proposal in conversation ("Yes to your view"). Four
parts, committed into the criteria file
(`src/blind_control_a3.py`, successor to the criteria first committed at
`a3c5fbf`) with the ruling quoted, before anything executes:

1. **Sign.** The ablation bites only when the **signed** corrected drop
   on the primary battery reaches the threshold. An improvement never
   counts.
2. **Noise.** Evaluate at **800 episodes or more**, with intact and
   ablated readings paired on the same evaluation seed. The threshold is
   about 0.038 raw battery points here; evaluation noise is sd 0.0284 at
   400 episodes (1.3 sd) and 0.0169 at 800 (2.2 sd).
3. **A fourth cell**, to be added before the next run: probe passes and
   the ablation *improves* the primary battery beyond noise =
   **located, wrong structure**. Neither pass, nor insensitive, nor not
   testable.
4. **Process.** Committed to the criteria file first, ruling quoted. **No
   registered text changes; the control stays unregistered.**

**The executable cells in that module still implement the 2026-09-16
letter** (they take an absolute value, and the episode count defaults to
400). The amendment is documentation until the code is changed, which
must happen before the next run.

Open and not ruled: whether to replace the single-threshold bite with a
partial-ablation dose ladder requiring steady worsening. That belongs to
the reframed 2026-10-04 proposal.

### 6. Where the money is

**A3 $34.31 of its $100 hard stop; the whole program about $216 of
$400.** Everything since 2026-09-17 has been local and $0. Ops cleanup
