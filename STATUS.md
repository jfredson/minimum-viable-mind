# STATUS — where we are, how to resume

*Living handoff doc. Update it at the end of a working session so the next one (you, or Claude in a fresh session) can pick up without re-deriving context. Most recent state at top.*

## WHERE THINGS STAND 2026-09-21 — the two follow-up localization reads are in and ruled: the exclusion confound is excluded, one cell crossed the bar and is not carried as a clearance, nothing is localized; the A3 closure text is next

*This section is the current state. Everything below it is the older
record, newest first, and is left exactly as written.*

Both reads went through Gate B of `docs/outside-review-protocol.md`
(`reviews/2026-09-21-followup-runs-claude-worktree.md`, ledger RT-120 to
RT-142). John ruled on all twenty-three findings on 2026-09-21, all as
drafted. Runs: PR 11 (`other-index-position-sweep-findings.md`,
`standardised-refit-findings.md`, method committed before output at
`7745d4a`).

**Two follow-up reads, 2026-09-21 (both local, no money spent).** The first
pointed the existing read at a different question, which of the four marker
words belongs to the other agent who revises, and found it nowhere except
where that agent's own name is the word being read. This settles the
objection raised on 2026-09-20 (RT-82), that the model's own index looked
positive at the other agent's revision value only because knowing who is
speaking rules out one of the four possible answers. For that to explain
what was seen, the other agent's rank would have to be readable at that
token at about 0.32 to 0.35; it reads 0.258 to 0.263, and the same read
detects an effect of exactly the required size at a different token in the
same run. The objection is excluded. That is the solid result of the pair,
and it is the first time the registered matched control L2(a) has run.

The second read put all 448 directions of the state on an equal footing
before fitting, which the earlier read did not, to test whether the earlier
read's penalty had been hiding a faint signal (RT-76). It had not: the
spread of results is unchanged to two decimal places and the pre-stated
outcome is again *found nowhere*. Every fit converged, where the earlier
read's third checkpoint mostly ran out of steps, which is a real improvement
in the instrument. One cell of 135 crossed the family-adjusted bar: third
checkpoint, the other agent's revision value, layer 3, at 3.43 against a bar
of 3.38. **It is not carried forward as a clearance.** It clears by two
correct predictions out of 4,000; a one-standard-error change in the spread
it is measured against, which is 5% of that spread and comes from the same
200 draws, puts it below the bar; the same states have now been swept twice
for this target, and against the 270 tests actually run the bar is 3.56; and
the same run's negative control, at a token where the answer cannot be
known, also returned zero of 200 draws beating it. The reading "three
independent lines point at that position" is withdrawn (RT-135): two of the
three are one sample read with two estimators, and the third is a null.
What may be said is: not explained away, and sub-bar, measured twice.

So: one proposed explanation excluded, and a sub-bar pattern at one position
that is now measured twice and still sub-bar. Nothing is localized. Under
the registration nothing counts as localized or absent until causal patching
has also run, and it has not; the registered term for where this line stands
is still **not testable (localization)**. Both reads measured the register
index, the rank of the marker word, and not the model's own marker word,
which is the registered target and has still never been read at these
positions (deferred to resumption per the December-result roadmap).

**No further work on that position is authorised.** The rerun the findings
called "the cheapest decisive move" would need about 8,100 null draws per
test to certify by counting, about 150 to 300 processor-hours, not 11
(RT-140). The blind-arm reconciliation: today's ruling 3 said the registered
blind-localization arm runs before any further work on this position; the
2026-09-20 December-result ruling (Astra A10) found the 2026-09-16 blind run
discharged the arm and scheduled no re-run. Both hold together, since no
further work on the position is authorised, and the operative order is the
later ruling's: the A3 closure text goes to Gate A now, without a blind-arm
re-run and without waiting for patching.

### Next, ruled 2026-09-21

1. The A3 closure text (`docs/a3-closure-text-draft-2026-09-20.md`) to Gate A,
   both tiers with the closure rule. Its preconditions are met: the pilot's
   log and trajectory are committed (PR 10), the two $0 checks are closed
   clean (PR 10), the two authorised reads are in and ruled (PR 11), and
   the blind-arm status is reconciled as above.
2. Successor proposal v1 and the protocol amendment text, per the
   December-result roadmap (unchanged).

## WHERE THINGS STAND 2026-09-20 (evening) — the December-result roadmap is adopted: the Stage 2 degree metric is the successor, registered in 2026, with a result by 2026-12-21 or a named schedule failure

John ruled "Agreed on all" on the seven items of
`docs/december-result-roadmap-2026-09-20.md` (ruling:
`docs/rulings/2026-09-20-december-result-roadmap.md`). What it fixes:

- **The question for 2026**: can a decomposability metric, validated on
  systems whose degree is known by construction, read the degree of a freely
  trained 30-million-parameter transformer with a load-bearing ownership
  pointer, and what does it read. This is Stage 2's deliverable, brought
  forward: the successor experiment (Astra's matched-role causal-interchange
  design, extended to three arms: a tracker built to be separable, a system
  built to be entangled, and the free model) is registered in 2026, not after
  hibernation. Item 5 of the center-as-degree ruling is amended accordingly.
- **Four registered outcomes**: R1 metric validated and degree read; R2 the
  metric does not separate the constructed arms; R3 an arm fails the
  learn-both eligibility gate; R4 a kill date missed, which is a schedule
  failure and is recorded as one. R1 to R3 are all results.
- **Dates**: successor proposal v1 this week; measurement rehearsal week of
  2026-09-28 (before any Gate A, now protocol); registration commit target
  2026-10-11, kill date 2026-10-18; registered runs launched week of
  2026-10-19, kill date 2026-11-01; validation Gate B week of 2026-11-02;
  closure Gate A week of 2026-11-30; wrap-up 2026-12-21.
- **Spend**: successor cap $130 inside the $400 envelope, with a seed fallback
  if the RunPod billing anomaly recurs. New standing rule: when a step needs
  more than the cap, the recommendation proposes the increase with the number;
  caps are gates for a ruling, never reasons to shrink a step silently.
- **Folded and deferred**: causal patching is built once, for the successor's
  grammar, so the A3 closure text goes to Gate A after the two authorised $0
  runs without waiting for it (step 4 ruling item 4 amended). Astra A10 ruled:
  the 2026-09-16 blind run discharged the arm; no re-run. Deferred to
  resumption: the ~70-hour marker-word read, option D, the frontier
  deliberative-gap pilot, Stage 3, the construction project.
- **Protocol**: the three amendments from the program review are adopted
  (rehearsal before Gate A, reviewer-owned verification, "unlikely" struck
  from the brief); the protocol text edit is owed before the successor's Gate A.

Owed next: successor proposal v1 (Claude Code); A3 closure tier 1 review
packet (Cowork); protocol amendment text; `data/project.toml` corrected
(wrap-up start was 2026-12-13 in the data file, ruled 2026-12-21).

## 2026-09-20 — the control battery converges on the name-blind solver even with its own loss term; the fitted read finds nothing on the register index; the linear-read line is parked as *not testable (localization)*; step 4 narrows to option D or closing A3

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
future reweighting run holds fixed. The step 4 housekeeping is done
(2026-09-20): the training log and trajectory are committed beside the
endpoint record (the missing-log finding, RT-56, with its missed deadline
recorded as missed), and both open $0 checks have run and are clean. The
fixed batch-split bias check (RT-58) finds no bias in episode order across
all 55,116 steps the pilot trained — structurally, the generator emits
episodes in matched content pairs and the 64-row control half is even, so
no pair is ever cut by the split boundary. The one-scored-token self-test
(RT-59) holds on all 7,054,848 rows. Neither changes a result; each
removes a way the verdict could have been an artefact.
**Carried forward for any future run of this flag: `round(batch ×
ctl_frac)` must stay even, or the split cuts content pairs.**
Notes: `ctl-pilot-log-provenance-findings.md`,
`ctl-split-bias-findings.md`, `ctl-scored-token-findings.md`.

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

### Program-level outside review, ruled in part 2026-09-20: a load-bearing self-index is a center at degree one; the corpus stops owing an "address versus marking" observable

Two other-lab reviewers (Gemini 3.1 Pro, GPT-6 Astra) read the record
(`docs/reviews/2026-09-20-program-review/`). Neither found an arithmetic or
record error the ledger had not already caught; both credit the process
with stopping over-claims and spend. Astra's A1 is the finding: the outcome
Amendment A3 hoped for is what an ordinary agent tracker with a
load-bearing pointer would also produce, and the record had conceded this
in three places (A3 §5 R4, the MVM-0a Scope section, ROADMAP.md Stage 2).
John ruled (`docs/rulings/2026-09-20-center-as-degree.md`): a load-bearing
self-index is a center, at the bottom of the gradient; "address, not a
marking" becomes a difference of degree on the integration axis, whose
metric is Stage 2's deliverable and does not yet exist. Consequences: the
A3 closure text (draft, Gate A: `docs/a3-closure-text-draft-2026-09-20.md`)
says load-bearing on three seeds, center not testable, degree unmeasured;
step 4 ruling 3's conditional restoring "a structural signature of
self-indexing" is struck; the successor is the matched-role
causal-interchange experiment, repurposed to develop the Stage 2 metric
(`docs/competing-mechanisms-2026-09-20.md`). Ledger: RT-118, RT-119
adopted; the rest of the tier-2 items carried with draft dispositions.
Still for John: the blind-arm reconciliation (Astra A10; the arm ran
2026-09-16 and the step 4 ruling schedules it again), whether the
~70-hour marker-word read runs, three protocol amendments, and the
outside reader's timing. ch05 owes the degree reading before the
2026-09-30 book lock.

### Next, ruled 2026-09-20

1. Two $0 local runs, method committed before output, brief at
   `reviews/2026-09-20-followup-runs-brief.md`: the other-agent index at the
   eleven positions (registered matched control L2(a), never run, ~11
   processor-hours) and the standardised refit at the nine positions (~11
   hours). The marker-word fitted read (~70 hours) is deferred.
2. The step 4 proposal goes to a tier 1 pass, then to John, before
   2026-10-04. Causal patching before A3 closes is its second item.
3. ~~Closures for RT-56, RT-58, RT-59 (log and trajectory committed; two
   one-line checks).~~ **Done 2026-09-20.** All three closed and filed as
   findings notes, each with its ledger closure line. Both checks are
   clean and neither changes a result. The one-scored-token check turned
   out to be worth more than one line: the assumption has to survive the
   shift the loss function applies, which a one-line version would have
   missed.

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
done 2026-09-19: John deleted the idle EUR-IS-1 storage volume after
both seed checkpoints matched their recorded checksums, and reverted the
sleep setting on the Mac. Details in `compute-ledger.md`.

### 7. The dated path, and what is next

Steps 1 to 3 of the public path roadmap
(`docs/public-path-roadmap-2026-09-16.md`, approved verbatim "Approved
on all") are **discharged**. Step 4 has been reframed: it is no longer
"make the control learn" but **repair the clause, change the metric, or
close A3 with partial discriminators and say so** — John decides
2026-10-04, on a proposal.

- **2026-09-20** — draft the reframed 2026-10-04 proposal (the
  reframed-proposal task, `208e4829`). $0.
- **2026-09-30** — book text lock. No MVM result lands before it.
- **2026-10-04** — John's decision on the control-battery question.
- **2026-10-11** — refresh `explainer.md`, after the book lock.

Also on file, advisory and $0:
`docs/research-note-pain-axis-2026-09-19.md`, six methodology lessons
from the nearest published neighbour. Two of them (a matched self/other
contrast scored by separation, and the dose ladder) fold into the
2026-10-04 proposal; one (projecting out the top control-variance
directions before probing) is a free known-answer test that could run
before 2026-10-04 on John's go, since it reads no verdict.

## A3 PILOT COMPLETE — the objective is LEARNABLE and genuinely about ownership; control battery never learned; $13.92 (2026-09-16)

Record: `experiments/06-mvm-0a-constructed-self-index/gate2-pilot-findings.md`;
endpoint `a3-gates/pilot_endpoint.json`, trajectory `a3-gates/pilot_trajectory.jsonl`.
Full registered budget: 55,116 steps / 585,552,384 tokens, one register-less
30M at seed 0. John's go, verbatim: **"Go"**. Checkpoint md5
`f751228ce0e40bae5aba22c6d5aa6c60`, verified against the pod before reaping.
**A3 cumulative $13.92 / $100 hard stop.**

**THE RESULT (n=800, 400 verdict cells):**

| battery | intact | acting channel zeroed | its shortcut ceiling |
|---|---|---|---|
| **T_act** | **0.506** | **0.182** | 0.2921 |
| T_other | 0.299 | 0.234 | 0.3227 |
| T_state | 1.000 | 0.999 | — |
| T_syntax | 1.000 | 1.000 | — |

**Learnable: T_act is +0.214 above the best any ownership-blind solver can
reach.** K2 does not fire. **The L0 validity check passes decisively AND
selectively:** zeroing the only authorship signal takes T_act 0.506 -> 0.182
while the ownership-free batteries do not move. Under the registered
(ceiling-corrected) metric that drop reads **1.515** — above 1.0, meaning the
lesion took it BELOW what an ownership-blind solver reaches. That is exactly
the case John's decision 3 said must be reported, not clipped; a clamp would
have hidden the most informative number in the table. Supplementary read at
one reviser (ceiling exactly 0.25): T_act 0.531, margin +0.281.

**THE CONTROL NEVER LEARNED. T_other 0.299 is BELOW its own 0.3227 ceiling** —
no marker-keyed retrieval at all, repeating the seed lottery only 2 of 5
earlier runs won. **Structural consequence for the lesion phase: its baseline
is below its ceiling, so the registered floor rule makes its drop UNDEFINED,
and any bin comparing the two batteries' drops cannot fire in either
direction.** One reading says that is benign (no generic binder exists to be
confused with a self-index); the other says a discriminator that cannot fire
is not doing its job. That is an adjudication, not a measurement.

**THE BIN IS NOT OBVIOUS.** K3's starvation signature is "T_act reaches
ceiling early while T_other stays flat". The control IS flat; T_act is at
0.506, well above its shortcut floor and nowhere near 1.0, flat around 0.537
over the last fifth. **Half fired, half did not.** Honest description: partial
learning on the primary, none on the control — neither the clean positive nor
the clean starvation. The bins were written before the grammar existed, which
is what red-team pass 3 flagged.

**ONE PROCESS FAILURE, AND ONE CORRECTION:**
1. **CORRECTION — the "truncated checkpoint" was my misreading.** I first
   reported the fetched checkpoint as silently corrupt (324MB vs the pod's
   351MB, loading without complaint). It was not: the watchdog's final
   fetch ran 13:36:11Z->13:46:59Z and my 324MB listing was timestamped
   13:38Z, INSIDE that window. I read a file mid-extraction as a corrupt
   one. The archive-based final fetch worked correctly. What IS real: my
   own streamed re-fetch over ssh truncated at 199MB (a `cat` of a large
   binary truncates silently), and the watchdog's INCREMENTAL pull uses
   that same unsafe pattern, promoting on a non-empty test alone — latent,
   did not bite, worth fixing before seeds 1 and 2.
2. **Idle billing recurred, THIRD time (this one is real).** Finished
   09:54Z, reaped 13:47Z — 3.9 idle hours, ~$3.8 of the $13.92. caffeinate
   blocks idle sleep, not lid-close. Three occurrences is a design
   problem: the reap must not depend on a laptop being awake.

**RULED 2026-09-16 (Cowork session; five binding decision entries tagged
`a3`, quoted in `gate2-pilot-findings.md`):** K0 applied at 0.25 scoped to
checkpoints where a verdict is read; the pilot endpoint recorded as
described and **deliberately unbinned** (K2 and K3 both did not fire, and
no new bin is written because a bin written after the data is fitted to
it); the undefined control drop takes the **strict reading** — seed 0 is
**not-testable** on the differential clause and cannot land in
H_self-location, with the other-agent and random-subspace lesions and the
swap probe reported as partial discriminators. **Consequence accepted: A3
as registered can no longer return a full registered positive regardless
of seeds 1 and 2.** The seeds are reframed as a ~$22 test of whether the
primary battery's learnability replicates and whether the control is a
seed lottery.

**NEXT, in the registered order (§4.3) — items 1 to 4 have all LANDED:**
1. Both process fixes committed — DONE (`3df7d19`, `2710982`), plus
   pod-side reaping ruled and implemented (`5dedc18`) after a paid test
   ($0.29) proved a pod carries no credential and no id of its own.
   **Amended 2026-09-16 on John's ruling: the full-write account key is no
   longer pushed to pods.** The launcher now reads the reaping credential
   only from `~/.runpod/reaper-key`, a dedicated key scoped in the RunPod
   console to graphql read and write with the serverless surface set to
   none, and refuses to arm unless that file exists, is non-empty and is
   mode 600. There is deliberately no fallback to `~/.runpod/config.toml`,
   which the script no longer reads at all: an unarmed reaper the operator
   is told about beats a silent return to the account key. If the pod-side
   read check fails at the next launch, the launcher says to stop and ask
   John rather than degrade.
2. Gate 3 — DONE and PASSES both arms (clean 0.483 and 0.4975; controls
   0.9895 and 0.8724). The first run's "uncertifiable" was a bad control
   on Claude's side, not the checkpoint.
3. Threshold lock — **DONE, John's commit `6ad4362`** (2026-09-16 20:08
   PDT). It carries θ 0.1777 on T_act and no threshold at all for
   T_other, which encodes the strict ruling mechanically: `lock_guard`
   accepts a run reading the primary battery and refuses one reading the
   control.
4. Seeds 1 and 2 as ONE WAVE — **DONE, John's verbatim go "Go" quoted in
   the ledger at `45fd652`** (20:11 PDT). Pods `xi062halhyuucg` (seed 1)
   and `4z55xtf1vowymp` (seed 2), launched 2026-09-17 03:13Z, est.
   $18–26 the pair, due to report around 06:07 local 2026-09-17.

**IF THE MAC REBOOTS BEFORE THE SEEDS REPORT, RESTART BOTH WATCHDOGS.**
They are the ONLY reap: the in-flight pods carry no credential, no pod id
and no reaper process, verified 2026-09-16
(`reaping-audit-2026-09-16.md`). The script is a plain polling loop with
no accumulated state, so restarting is safe and idempotent. One command
each, from anywhere:

```
cd /Users/john/Code/minimum-viable-mind/.claude/worktrees/gate0-null-calibration/experiments/06-mvm-0a-constructed-self-index/src

nohup caffeinate -dimsu bash watch_run_a3.sh \
  /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/artifacts/a3_30m_seed1/run_xi062halhyuucg.env \
  >> /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/artifacts/a3_30m_seed1/watchdog.log 2>&1 &

nohup caffeinate -dimsu bash watch_run_a3.sh \
  /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/artifacts/a3_30m_seed2/run_4z55xtf1vowymp.env \
  >> /Users/john/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/artifacts/a3_30m_seed2/watchdog.log 2>&1 &
```

Check they took: `pgrep -fl watch_run_a3.sh` should list two. Exposure if
they are not restarted: both pods finish around 06:10 local, nothing
fetches or deletes, and they bill about $2/hr together. `terminate-after`
does NOT cover this — the ledger records it failing to fire and costing
$97 on the 30M A1 pilot.

**IN FLIGHT AND ON JOHN'S MACHINE:** lid sleep is disabled
(`SleepDisabled 1`) so the wave reaps on time; **revert after both report
with `sudo pmset -a disablesleep 0`**. The two in-flight pods launched
before the reaping ruling, so the laptop watchdog is still their only
reap.

**DATED PATH (John approved the public path roadmap verbatim, "Approved
on all", 2026-09-16; `docs/public-path-roadmap-2026-09-16.md`, committed
`609c5c5`):**
- **2026-09-18** seeds report: checkpoints fetched and checksummed, pods
  reaped, ledger actual-after rows (task "Public path 1", `f5f5f9e9`).
- **2026-09-20** John decides optional extra seeds (`9698b81b`).
- ~~2026-09-27~~ **blind-localization arm — DONE EARLY 2026-09-16,
  `0a1f2c2`, local and $0.** Verdict **NOT FLAGGED**, sub-bin
  **instrument failure to locate**: no probe cleared its null by the
  stated 3 sd bar (best 1.3 sd, accuracy 0.275 against a chance of
  0.25), so the stack could not decode own-agent identity at all on a
  register-bearing checkpoint that binds. Per John's ruling of
  2026-09-16 this arm ran as a **false-positive test**, because the
  register exists by construction but was measured inert, so the
  registered question had no object. **The result supports specificity
  only, never sensitivity** — that limit was committed before the number
  was seen. **ANNOTATION 2026-09-16 (John's ruling): superseded in
  interpretation by the unblinded register probe — no valid target.** The
  verdict and its pre-stated sub-bin name stand as committed and are not
  retired; the unblinded probe showed the A2 register never encoded
  own-agent identity at any turn, so the blind arm had nothing at that
  location to find and the result says nothing about the stack's
  sensitivity in either direction
  (`register-direct-probe-findings.md`, `a7f5cd8`).
- **2026-09-16, THE A2 REGISTER WAS A CONSTANT IN EVERY TRAINED
  CHECKPOINT** (`register-saturation-findings.md`, `cc9c70e`). The writer
  emits the same vector whatever it is given, from its first write, at the
  floating-point floor on seed-0, seed-1 and seed-2 full and on the 10M
  pilot. An untrained model at the same config does not, so it is trained
  in rather than architectural. No intermediate weights were saved, so the
  training-time onset cannot be recovered; the untrained control bounds it
  from the other end. **Consequence, ruled by John: a constant read
  through cross-attention is a bias term, so the full model is the twin
  plus a learned bias and the register-versus-no-register manipulation was
  never effectively applied.** Binding tracks seed, not architecture: two
  of five bind, one full and one twin. The wave-2 "prediction inverted"
  result is better described as a **seed lottery in one architecture**.
- **2026-09-16, THE LOCALIZATION PIPELINE IS VALIDATED AT THE PLUMBING
  LEVEL AND GATED ABOVE IT** (`known-answer-test-findings.md`, `1cb1fbb`).
  The known-answer test passes at ceiling, accuracy 1.0 against a null of
  0.1306, a margin of 32.9 standard deviations. So residual capture,
  position indexing, probe fitting and null construction work. It does
  NOT exercise the ablation path, and with the acting channel zeroed the
  target still decodes at 1.0, so it is a plumbing check and nothing more.
  **John's gate — no A3 L1 localization read on any seed until this passes
  — is mechanical (`lock_guard.require_known_answer_pass`) and now lifts;
  lifting is permission, not instruction, and no read has been run.** The
  L0 direct lesion was never gated.
- **2026-09-16, WITHDRAWN: "evidence of insensitivity at small scale."**
  The positive control's verdict is the literal pre-stated **NOT
  TESTABLE**; the signed-rule reading stays beside it as a diagnostic and
  never becomes a verdict. The ablation's apparent +0.052 on the ownership
  battery is **inside evaluation noise**, measured over twelve draws per
  size: sd 0.0284 and range 0.079 at n=400, the size the control used.
  What stands is only that the probe found nothing.
- **2026-09-16, THE PILOT'S 0.506 IS ONE UNLUCKY EVALUATION SEED.** It and
  the 0.440 both come from the single default seed and reproduce exactly;
  both sit below all twelve fresh draws. **The checkpoint's typical
  ownership score is nearer 0.566.** No verdict changes, since every drop
  is measured against its own baseline in the same run, but **any write-up
  quoting 0.506 must quote the spread with it.**
  The measurements stand; only the architectural interpretation is
  withdrawn. Wave-2 ledger row, the twin-binding note and Amendment A3 §1
  are **annotated, never edited** (the ledger change verified
  append-only). No registered text changed. Sensitivity is untested and the companion positive control
  is unregistered, not run, and awaiting John's separate ruling
  (`blind-arm-positive-control-proposal.md`).
- **2026-10-04** John decides the control-battery question on a written
  proposal: a registered Amendment A4 that makes the control learn
  reliably, or close A3 with partial discriminators and say so. Proposal
  drafted after the seeds report; no spend. Note for that proposal: the
  ceiling adjudication permits exactly one amendment to the compute cap
  and A3 proceeded on the reading that it binds money rather than design,
  so an A4 needing new runs must make that argument explicitly.
- Steps 5 to 8 (explainer refresh, paper draft, outside reader, public
  release 2026-11-22) are John's and the Cowork side's, not this
  session's.

Free work in parallel: the lesion and localization pipeline, build and
smoke-test only, no L1 run or read before the lock.

## SHORTCUT SWEEP — a SECOND fatal leak; three grammar drafts map a real trade-off; proposal drafted; A3 NOT ready to register (2026-09-15)

Proposal: `experiments/06-mvm-0a-constructed-self-index/a3-revision-proposal.md`
(13 numbered decisions). Sweep: `src/shortcut_sweep.py`, record in
`a3-gates/shortcut_sweep.json`. **Still $0; A3 cumulative $0.00 of the
$100 hard stop; no pod ever launched for A3.**

**The grammar Gate 1 certified this morning has an ownership-blind
ceiling of 0.52, not 0.29.** Every agent revised exactly once, so any
agent that has ALREADY revised is not the one revising now. When the
model revises last — a quarter of episodes — its own assignment is the
only one left and identifying it needs no self-knowledge at all.
Measured 0.5248 by that elimination alone; 0.5425 by a learned attack.
(The sweep's first run also caught a bug in itself — features ranged over
the whole episode and read the graded turn, giving a fake 1.000. Fixed,
then it found the real thing.)

**THE REAL FINDING: a structural tension, not three mistakes.** Three
drafts now, each trading one flaw for another:

| draft | who revises | cells | ceiling | cue gates |
|---|---|---|---|---|
| 1 | model always + 1 other | every ep | 0.29 | FAIL (turn count a perfect cue) |
| 2 | every agent once | every ep | **0.52** | PASS |
| 3 (current code) | 2 drawn uniformly | half | 0.29 (sweep PASSES) | **FAIL at 0.53** |

Draft 3 fails because revisers take 3 turns and non-revisers 2, and the
detector samples one own turn against one other turn — "own" is one
agent, "other" pools three. Turn count is balanced across all turns
(0.596 vs 0.601) and NOT under that sampling (**0.499 vs 0.591**).

You cannot have all three of: a scoring cell every episode; revising not
marking the model out; and agents that have acted not being eliminable.
Any two, not three.

**A fourth grammar was deliberately NOT drafted.** Each fix so far was
sensible and cost something elsewhere; one of K1's two regenerations is
spent; the choice belongs to John with the trade-off in front of him.
Proposal decision 1 lays out four options with measured costs and
recommends varying turns-per-agent independently of revising (untested),
with one-uniform-reviser (ceiling 0.25, quarter density) as fallback.

**Good side effect:** with only 2 revisions per episode the control
battery's ceiling falls 0.5 → 0.3227, cutting RT-21's spurious
differential from 0.237 to 0.035 (still above the ~0.01 band, so the
metric fix stands).

**New proposed gate (decision 8):** register the shortcut sweep itself.
RT-20's attack scored 1.000 on a grammar that had just passed both cue
gates — the cue gates ask which turns are the model's own, a different
question. The sweep is free and has already paid for itself twice.

**Next (John owns all of it):** work the 13 decisions, chief among them
decision 1 (the grammar trade-off) and decision 3 (divide the drop by the
measured ceiling, not chance); then the registration commit; then Gate 2,
the pilot, on a C2 go in his own words. **A3 is not ready to register.**
Branch `gate0-null-calibration`, pushed.

## RED-TEAM PASS 3 — 13 findings; the certified grammar did NOT test self-indexing; fixed at $0; registration now carries 7 items (2026-09-15)

Full pass: `experiments/06-mvm-0a-constructed-self-index/red-team-pass-3.md`
(RT-20 to RT-32, continuing the ledger). Addendum with the fix and the
re-run gates at the end of `gate1-curriculum-findings.md`. Trainer added:
`src/train_a3.py`. **Still $0; A3 cumulative $0.00 of the $100 hard stop;
no pod has ever been launched for A3.**

**RT-20 (FATAL, verified, fixed).** The grammar Gate 1 certified did not
test self-indexing at all. A turn rendered "<name> assign <item> to
<value>" and the graded token is the value — so **the model's own name
label sat three tokens back in its own context at the moment it was
scored**. An ownership-free solver that reads that name, finds the
matching earlier assignment and applies the rule **scores 1.000 over 3000
episodes**. The measured shortcut ceiling of 0.2925 was never a bound on
ownership-blind solvers. The cue gates could not catch it: they ask which
turns are the model's own, which is a different question.

**My own ceiling control gave false reassurance.** A smoke model without
the acting channel sat at 0.22 against 0.575 with it — which showed only
that a 0.1M network had not found the shortcut in 1500 steps, not that
the shortcut was absent. A 30M model on 784M tokens finds it. The pilot
would have returned a ceiling score that meant nothing.

**Fix ($0):** the speaker's name moves AFTER the value —
"assign <item> to <value> by <name>". The graded position now sees
"assign <item> to" and nothing more, so the acting channel is the only
route to which of the four earlier values was its own. The attack is a
permanent regression test in the grammar's self-test. Batteries re-frozen;
gates (i) and (ii) re-run and still PASS (0.5097 / 0.5259) — one of the
two regenerations K1 permits. The detector's score is carried by
structural not textual features (0.5057 numeric-only), which is why
reordering text moved nothing.

**RT-21 (FATAL, verified arithmetic, NOT yet fixed).** The metric divides
the drop by distance to *chance*, but the two verdict batteries now have
different shortcut ceilings (0.2925 and 0.5). So a lesion of a purely
**generic** who-did-what binder produces a differential of **0.237**
against a differential band Gate 0 measured at about **0.01**. The
headline positive bin fires on the boring explanation, and the bin meant
to catch it cannot fire unless the lesion removes under ~4% of capacity.
Remedy: correct the drop against the measured ceiling, not chance. $0,
changes registered text, belongs in the registration commit.

**Serious (RT-22 to RT-27):** bins neither exhaustive nor exclusive (no
bin for the L0 validity check failing); the lesion target is not
localizable where §3.1 says, and objection R1 has a sharper form; θ/δ
written as scalars when Gate 0 measured them per battery across a 25-fold
range, and no readability floor before the two paid seeds; "uncertifiable"
on the act-withheld attack routes nowhere; the ladder is costed on the old
8-turn grammar (measured ~1.3–1.4× per run, $13.6–14.3 vs $10–11 — three
seeds still fit, the optional extras do not); the loss mixture is
unregistered and by itself decides whether the starvation bin can fire.

**Worth noting (RT-28 to RT-31)** and **procedural (RT-32)**: see the pass.
Two items were in this session's own code and are already repaired — two
self-test assertions written vacuously with a trailing `or True`, one of
them the exchangeability check the whole cue-gate argument rests on. Both
now run; the property holds.

**Found sound and said so:** the no-stakes commitment C4 and the
floor-only/episodic claim both survive attack; the exchangeability
construction is correct; Gate 0's escalation check was the right move in
the right order; keeping `curriculum.py`/`encoding.py` byte-identical was
correct.

**Next (John owns all of it):** (1) K0's number; (2) the registration
commit now carrying **seven** items — Gate 0's three, Gate 1's two, and
RT-20/RT-21 — plus whatever of RT-22..27 he adopts; (3) then Gate 2, the
pilot, on a C2 go in his own words. **No A3 run launches before that.**
Branch `gate0-null-calibration`, pushed.

## GATE 1 COMPLETE — Candidate A grammar built and certified, $0; K1 does not fire; red-team pass 3 now carries five items (2026-09-15)

Full record: `experiments/06-mvm-0a-constructed-self-index/gate1-curriculum-findings.md`;
gate records in `.../a3-gates/`, frozen batteries in `.../batteries-a3/`;
code `src/curriculum_a3.py`, `src/encoding_a3.py`, `src/cue_detector_a3.py`
(committed at `7ab8018` **before the gate ran on them**). Local, **$0**;
A3 cumulative spend still **$0.00 of the $100 hard stop**. Nothing
trained, no pod [C1/C2].

**The grammar.** Twelve turns, four agents, two contested items. Every
agent assigns each contested item once with the four values on an item
distinct, then **every agent revises exactly once**, two per item, under
a shared deterministic rule (the successor of that agent's own earlier
value). Applying a rule everyone shares requires knowing which of four
assignments was yours. `curriculum.py` and `encoding.py` are untouched —
their token ids are what make every prior record reproduce — so A3 gets
new modules; the A3 vocabulary adds one word, "next".

**Gate result: PASS, K1 does not fire.** Run (i) curriculum text plus
episode-relative features: clean 0.5097 [0.4867, 0.5316], control 0.943.
Run (ii) input tensors: clean 0.5259 [0.5032, 0.5498], control 1.000.
Both clean intervals inside the registered [0.45, 0.55].

**Gate 0's cell-size fix is delivered:** 400 episodes now yield **400
T_act cells**, against 19 for the registered grammar's
revision-conditioned battery at the same episode count.

**Two NEW items for red-team pass 3, on top of Gate 0's three:**
4. **The pre-stated lookup ceiling is wrong for this grammar.** Measured
   0.2925 for T_act (not 0.25) and **0.5 for T_other**, because each
   item's two revisions let a solver strike candidates. The asymmetry
   matters: the H_generic-binding bin turns on the gap between the two
   batteries' drops. Either adopt the measured numbers or add a third
   unrevised contested item to buy 0.25 back, at ~⅓ more compute per run.
5. **Gate (ii) fails a clean grammar about one run in nine.** Its
   bootstrap interval resamples one draw's test split and is silent on
   across-sample spread. Six independent samples: text mean 0.4939
   (sd 0.012), tensor mean 0.5054 (sd 0.0224). The registered seed's
   0.5259 is within one sd of chance, and the own register's stack index
   is uniform to one standard error over 40,000 episodes — there is no
   cue. Take the verdict over several samples, or raise n to ~14,000.

**For the record: the first draft of the grammar was killed by its own
self-test.** Giving only the model and one other agent a revision left
the model's agent as the only one with three turns, so turn count
predicted ownership perfectly and revision status at 0.33 vs 0.14. Every
agent revising once removes both by construction. The detector also had
to gain episode-relative features the registered one lacks, since an A3
turn renders identically whether it assigns or revises.

**Next (John owns all of it):** (1) K0's number and the Gate 0 items;
(2) red-team pass 3 with all five items; (3) registration commit; (4)
then Gate 2, the pilot, on a C2 go in John's own words. **No A3 run
launches before that.** One free build step remains: the trainer does not
yet know about T_act — the loss must sit at the own revision position and
`eval_heldout` must score there. Branch `gate0-null-calibration`.

## GATE 0 COMPLETE — the registered null calibration ran, $0; K0 does not fire where a verdict is read; three fixes for red-team pass 3 (2026-09-14)

The first action Amendment A3 orders is done. Full record:
`experiments/06-mvm-0a-constructed-self-index/gate0-null-calibration-findings.md`;
per-checkpoint records in `.../null-calibration/`; scripts
`src/null_calibration.py` (committed **before it read any checkpoint**),
`src/null_escalation.py`, `src/summarize_null.py`. **Everything local,
$0; A3 cumulative spend $0 of the $100 hard stop.** Nothing trained,
no pod, no checkpoint promoted [C1/C2].

**The band.** 620 ablated evaluations: five 30M checkpoints × the
registered held-out eval at n=400, under 120 content-blind residual
ablations each (random rank-4/8/16 subspaces mean-ablated, matched-norm
noise, 20 seeds, blocks 3/4/5/7/8), plus 20 register-noise draws per
full checkpoint. On the two **binders** — the only runs where a lesion
verdict could be read — the 95th-percentile chance-corrected drop on
T_si is **0.006 and 0.0095**, against a binder/non-binder split of
**~0.73**. The registered instrument's noise floor is narrow where it
matters.

**K0 — John's call, and it is not clean.** K0 is written two ways. Its
stated condition (the band swallows the binder/non-binder split) is met
**nowhere**. Its proposed number (band ≥ 0.25) is **exceeded on one
checkpoint of five**: the seed-0 twin at 0.379 — a non-binder whose
T_si sits at 0.355 against chance 0.125, where the metric's divisor is
tiny and random damage genuinely knocks out a fragile heuristic (raw
T_si falls to 0.250 across draws). The amendment never says which
checkpoints the band is read on. Reading offered, not ruled: a wide
band near chance cannot manufacture a false positive, only make a
marginal learner unreadable, which is already its own bin.

**Three fixes for red-team pass 3, before the registration commit:**
1. **T_act cell size.** At n=400 *episodes* the revision-conditioned
   battery yields **19 items**, not 400 — its band is two items
   flipping. A3's primary metric T_act is scored at own revision
   positions and the amendment never states a revision frequency, so it
   would inherit a 20-item verdict cell. State in §2.2 that every
   episode carries exactly one own revision.
2. **K2 units.** K2 compares "lookup ceiling (0.25) plus the null band"
   — a raw accuracy added to a chance-corrected band. Restate in raw
   accuracy: unlearnable if T_act ≤ 0.25 + θ × (baseline − chance).
3. **K0 scope.** State that the band is read on checkpoints whose
   verdict battery clears the floor margin.

**Two further findings.** The **register-noise** band matches the
random-residual band on all three full checkpoints — thread 4's "inert"
conclusion now in registered-instrument form. And a **correction to
thread 3**: the two binders apply *opposite* conventions to ambiguous
repeated items (seed-1 twin picks the earlier value 76% of the time,
the pilot picks the later 72%), so the retroactive half of A3's
decision 14 cannot be done by re-keying to the latest value; the
structural fix in Candidate A is unaffected.

**Instrument validity.** At the registered rank cap the operator removes
19% of the mean-centred residual and moves nothing; batteries collapse
at 52% and sit at chance by 75%. The narrow band is robustness, not a
dead operator.

**Seed-0 asterisk, restated:** thread 4 read register-ablation scores on
the pilot seed-0 checkpoint before any lock (RT-10), so seed 0's band
is *for the record*, not a clean lock. A3 inherits none of it — its θ/δ
are calibrated on A3's own pilot with the lock ordered ahead of any L1
read.

**Next (John owns all of it):** (1) apply K0 and set its number; (2)
red-team pass 3 with the three fixes above; (3) registration commit;
(4) then Gate 1, and the pilot at ~$12 on a C2 go. **No A3 run launches
before that.** Branch `gate0-null-calibration` holds this work.

## ANOMALY DIAGNOSTICS RUN — register lesion: binding SURVIVES total register removal; construct problem is TOTAL; wave 3 awaits John (2026-08-19)

The cheap threads queued by `twin-binding-anomaly.md` ran to completion
in one session, all local, $0 [C1/C2]. Full record:
`experiments/06-mvm-0a-constructed-self-index/register-lesion-findings.md`;
raw outputs in `.../lesion-results/`; tools `src/lesion_register.py`,
`src/item_analysis.py`, `src/pick_analysis.py`.

**Thread 4 (the decisive test) — the pre-stated "survives" branch
fired.** The bound pilot's T_si/T_sr_rev are UNCHANGED under every
register lesion, including full removal of the cross-attention
injection (T_si 0.93→0.94, T_sr_rev 1.00→1.00; harness validated by
bit-identical reproduction of the committed endpoint row). The
registers route large activation mass (per-block xattn residual norms
18–275) but carry almost no agent-specific information (deranged
content read: mean |Δlogit| 0.014). Numerically active, informationally
inert. **No observed binding anywhere in the 30M data is
register-dependent.**

**Thread 3 (item analysis, all five checkpoints, n=400) — the
batteries decompose.** "Binders" = general associative retrieval
(unique-item T_si 1.00 for both, register or no register); their only
losses are T_si's repeated-item cells, which are ill-posed (the
recorded answer is a random draw between stale and revised value — an
item-construction defect). Non-binders = first-binding-wins memory of
OWN commitments only (T_sr 1.00 on first assignments, 0.00 on revised)
with no marker-keyed retrieval (T_si 0.34, flat). A no-act lesion
localizes the one demonstrably load-bearing authorship mechanism: the
non-binder's T_sr collapses 0.96→0.16 without the motor copy — the
acting channel, which the twin also has.

**Also done:** `fingerprint_gate.py` output-path hazard fixed (`--ckpt`
runs write per-checkpoint sidecars; canonical record needs explicit
`--canonical`).

**Next (John owns all of it):** (1) adjudicate wave-3 disposition —
the findings note lays out halt-and-redesign / null-calibration-first /
continue-as-registered, with the diagnostic result that no wave-3
outcome can bear on H_load-bearing; (2) any change to the registered
plan is itself a registered amendment; (3) RunPod ticket #45404 reply
still drafted-not-sent on branch `worktree-runpod-ticket-reply`; (4)
θ/δ null calibration (~$2–5) remains registered and unspent.

## 30M LEARNS — verdict H_scale; gate (iii) PASSES; A2 REGISTERED (scale 30M, cap $400) (2026-08-16)

The re-run completed clean end-to-end: token-budget stop at step 102,095
(784.09M tok, 19.0h train), DONE sentinel written, **watchdog did the
full fetch and deleted the pod itself** (16:41Z; zero pods; the 08-12
failure mode is closed). Endpoint: T_sr 1.00 / **T_si 0.93** (max 0.990;
late band 0.93–0.98) / T_state 1.00 / T_syntax 1.00 / **T_sr_rev 1.00**;
transitions T_si @64.5k, T_sr_rev @73k — the pre-stated H_scale
signature, no mark of shortcut-starvation. **John adjudicated H_scale
in-session.** Gate (iii) re-ran on the checkpoint at the registered
n=4000: **PASS** (arm A 0.4874 [0.4664, 0.5110], arm B 0.4964
[0.4837, 0.5095], all positive controls fire incl. the retired v1.0
pipeline at 0.82; md5 `fd1eb80c…`). Full record + caveats (single seed;
learnability ≠ load-bearing): `pilot-a1-30m-findings.md`.

**Amendment A2 registered same day** (`pre-registration.md` §Amendment
A2): registered scale 30M; cap $200→$400 at measured 5090-secure pricing
(projected total ~$355–375 incl. 5-seed × full+twin ≈ $190); venue
secure-only + process-fixed launcher promoted to registered procedure.
Starvation branch doc deleted unused. Cost: ~$18.9 actual (est $19);
spend ~$124.5, balance $79.77. RunPod overrun ticket SUBMITTED
(2026-08-16 ~14:45Z, Pod Issue → Incorrect Charges; CLI-help proof of
`--terminate-after` folded in after their bot doubted the flag exists).

**Next:** (1) the registered 5-seed × full+twin at 30M — precondition
met, launch is John's C2 go through `launch_pilot_a1.sh` (needs the
seed/twin parameterization pass first); (2) blind-localization arm
alongside per registration; (3) W37 single-amendment ceiling number
(John, quick); (4) ledger console reconciliation at the phase boundary;
(5) 30M findings note is written (raw, not Voice-Calibrated) — merge
branch `worktree-30m-findings-scaffold`, where this session's doc edits
live.

## 30M RE-RUN IN FLIGHT — 5090 secure + network volume; watchdog armed (2026-08-15, later)

John topped up $75 (balance $98.94) and directed the launch. EUR-IS-1 had
**no H100/A100/H200 secure stock**, so the run went to **RTX 5090 SECURE in
EUR-IS-1 at $0.99/hr with the volume attached** — durability kept, cost
drops to ~$40–55, wall-clock est 40–55h (5090 pace unknown until the
step-500 eval; est trues up then). Pod `rhddnh0u4le0l9`, created 21:37Z,
training started 21:43Z, checkpoints + log on `/workspace/mvm-out`
(volume mount verified). Watchdog live on John's Mac (caffeinate; **keep
it powered**), deadline fetch-and-kill 2026-08-18T05:37Z; DONE sentinel
ends it earlier.

**Two launcher bugs caught at launch, both fixed in-repo:** (1) my rewrite
dropped `mkdir /root/mvm` from the push, so the code never landed; (2) the
old aliveness check `pgrep -f 'train.py --scale'` matches its own remote
shell — it printed **ALIVE with nothing running** (this bug predates today;
now `[t]rain.py`). Pod repaired by manual push + start; ~6 min idle
(~$0.10). Lesson recorded: the aliveness check was capable of masking
exactly the failure it exists to catch.

**Pace measured (step 500, 325.8s = 0.65 s/step): the 5090 is FASTER
than the H100's 0.70 s/step** — the workload is enactment/Python-bound,
not GPU-bound. Revised: ~18.5h train, **~$19** (vs $40–55 est, vs $66
H100), completion ≈ **2026-08-16 16:12Z (~9am PDT Sunday)**. This
reprices the whole ladder: a 30M run costs ~$19 on a secure 5090, so the
5-seed × full+twin (10 runs) is ~$190 — the cap amendment the memo
priced at ~$650–770 (H100) may be a much smaller ask, or even nearly fit
a modest cap raise. Fold this into the cap adjudication when the pilot
verdict lands. Early metrics at step 500: T_syntax 1.0, T_sr 0.62
climbing, T_si 0.10 / T_sr_rev 0.00 at floor — nothing diagnostic yet;
the 10M failure signature is about where these END, not where they start.

**Post-run pipeline STAGED (2026-08-15, later):** on artifact arrival run
`src/run_post_pilot.sh` — completion check + md5, trajectory readout
against the two pre-stated signatures, then gate (iii) at the registered
n=4000 via the new `fingerprint_gate.py --ckpt` (override tested against
the 10M checkpoint; the recorded 10M gate JSON untouched). Both verdict
branches are pre-drafted so the winner moves immediately:
`amendment-a2-draft-IF-30m-learns.md` (registered scale 30M + cap
$200→$400 at measured 5090-secure pricing, ~$355–375 projected total)
and `upstream-draft-IF-shortcut-starvation.md` (ladder stops; packet to
sentient-horizons with its own retraction wager). The loser gets deleted
unused. Neither is registered — John adjudicates the verdict first.

**Next:** completion monitor armed (DONE fetch or watchdog terminal event);
watchdog handles fetch+kill; on completion run gate (iii) against the
fetched checkpoint, then adjudicate H_scale vs H_shortcut-starvation per
the pre-stated signatures. John still owes: support ticket submission
(`runpod-ticket-overrun.md`) + cap-memo sign-off (sequence-first is in
effect de facto).

## 30M RE-RUN PREPPED — all three process fixes built and tested; launch waits on a $75 top-up + John's C2 go (2026-08-15)

John's direction: overview session → straight into the re-run prep, launch
ASAP. Everything below ran at $0; the only remaining human steps are the
top-up and the launch itself.

**Process fixes (all three from the 08-12 entry) implemented and tested:**

- **Checkpoints + log now survive pod death.** `launch_pilot_a1.sh` attaches
  the `mvm-models` network volume (`8xeftvclmv`, EUR-IS-1, confirmed alive
  via API) with `--network-volume-id`; checkpoints and `train_<out>.log`
  write to `/workspace/mvm-out`. `NETVOL=none` falls back to container disk
  if EUR-IS-1 has no H100 stock. `train.py` saves atomically
  (tmp + `os.replace`) and writes a `.DONE` sentinel + `TRAINING COMPLETE`
  as its final act — a crash can never fake completion.
- **The launch owns its fetch AND its kill.** New `src/watch_run.sh`,
  spawned automatically by the launcher (nohup + caffeinate — keep the Mac
  powered): polls every 10 min, pulls evals/log continuously and the
  checkpoint hourly, and on the DONE sentinel — or a hard +24h deadline —
  does a full fetch then **deletes the pod**. Terminate-after still passed
  but is advisory only, per the 08-12 rule change.
- **Tested without spending:** train.py smoke run green (atomic save,
  sentinel, jsonl all verified; smoke metrics match the known pre-scale
  shape); watchdog exercised against mocked ssh/runpodctl on all three
  paths — DONE→fetch+kill (exit 0), deadline→fetch+kill (exit 2), pod
  vanished (exit 3). The one untested piece is `--network-volume-id` on a
  real create; it fails loudly with a stated fallback if EUR-IS-1 lacks
  stock.

**Cap adjudication teed up (`cap-adjudication-memo.md`, open item #4):**
at measured pace nothing beyond the pilot fits the remaining $94.38 —
"everything at 30M" is ~$690–770 more on H100. Recommendation **(A)
sequence-first**: run only the pilot now (~$66, fits the cap, no amendment
needed), and let its verdict decide — H_shortcut-starvation kills the
5-seed question entirely; H_scale reopens the cap amendment against a
measured number. **Funding answer for John: top up $75 now** (balance
$23.94 can't cover the ~$66 run); do NOT pre-fund the 5-seed.

**Support ticket drafted** (`runpod-ticket-overrun.md`, open item #3):
$17.82 credit request for the post-backstop overrun, evidence from the
console reconciliation; John submits via the console. The waived 08-08
anomaly is deliberately excluded — one clean claim.

**Ledger:** est-before row added for the re-run ($66, cap $80, ~$172/$200
projected). **Launch sequence (the C2 steps, in order):** (1) John tops up
$75; (2) John runs `src/launch_pilot_a1.sh` (defaults are the 30M rung);
(3) verify the launcher prints the volume-backed run dir + watchdog pid;
(4) walk away — the watchdog fetches and kills. Gate (iii) re-runs on the
fetched checkpoint before any further spend.

## 30M PILOT LOST — pod outran its backstop between sessions; balance drained to −$0.07; checkpoint never fetched (2026-08-12)

John's RunPod low-balance notification prompted the check. State:
**zero pods running, clientBalance −$0.07** (API, 08-13 01:54Z). The
30M pilot pod `6bplni87uzp3ss` (launched 08-09 23:54Z, H100 secure
$3.29/hr, 24h terminate-after, est completion ~19:50Z 08-10) died
between sessions and **nothing was fetched: checkpoint, held-out
evals, and train.log are lost** — the launcher writes to the pod's
container disk (`/root/mvm/out`), not the network volume, and no
session ran inside the completion→backstop window. The run answers
neither H_scale nor H_shortcut-starvation; **the 30M rung must re-run.**

**Billing — console-reconciled same session (John opened the console
in Chrome): root cause CONFIRMED — `--terminate-after` NEVER FIRED.**
H100 rows 08-09/10/11 UTC = $0.254 + $78.96 + $17.821 = **$97.04 =
29.5h @ $3.29/hr**, one continuous run (08-10 is *exactly* 24.00h, so
no billing inflation); the audit log's last event for the pod is its
creation — no delete from any actor. RunPod killed it on balance
exhaustion ~05:25Z 08-11, **~5.4h / ~$17.82 past the backstop**
(support-ticket candidate — the overrun is RunPod's bug). The A1 10M
row trued up nominal ($1.943 — the 08-08 anomaly did not recur), and
rule-4 reconciliation PASSES ($106.88 console vs $106.80
balance-implied). Ledger updated: running total **$105.62/$200,
remaining ~$94.4**, phase-budget guide flagged stale (it prices 5-seed
30M at ~$12; the measured pilot alone cost ~$97 — the remaining design
may not fit without amendment). The Layer-3 prepaid backstop held:
stopped at $0, no card charge; RunPod also stops storage billing at
zero (balance parked at −$0.07). The `mvm-models` volume (150 GB)
survives for now but sits on an unfunded account — RunPod deletes
volumes in that state (its own warning says "add funds or back up
your data").

**Decisions John owns before anything relaunches:**
1. ~~Console reconciliation~~ DONE (above).
2. `mvm-models` volume: top up to keep it, or delete it (holds the
   Llama/Tülu/Gemma weights + persistent venv — all re-downloadable,
   but re-provisioning cost real wall-clock; recommendation: small
   top-up while the re-run question is open).
3. Support ticket for the ~$17.82 post-backstop overrun (terminate-after
   is RunPod's feature; the audit log + billing rows are the evidence).
4. Cap arithmetic: at measured 30M pace, adjudicate whether the ladder
   continues under $200 or the registration needs an amendment.
5. Re-run go (C2) — only after the process fixes below.

**Process fixes required before the re-run (the failure had no single
cause; all three were absent):**
- Write checkpoints + train.log to the mounted network volume (or
  upload as the training script's last act) so pod death loses nothing.
- Give the fetch an owner: the launch ends by scheduling the fetch
  (session, cron, or a checkpoint-upload-on-exit), not by assuming one.
- **Terminate-after is now advisory, not a backstop** (confirmed
  no-fire on this pod): every launch schedules its own kill as well as
  its fetch.

## A1 PILOT RAN: 10M FAILS ceiling — ladder climbs to 30M; GATE (iii) PASSES on the A1 pipeline (2026-08-09, night)

John fired the pilot in-session (pod `3ethp3bc7le6e4`, 2.78h, ~$2;
checkpoint md5 `bab56cd8…` in `artifacts/pilot-a1-10m-seed0/`; pod
deleted, zero pods). Full record: `pilot-a1-findings.md`.

**The pipeline is clean: gate (iii) PASSES at the registered n=4000**
— the run that killed v1.0. Arm A 0.4874 [0.4664, 0.5110], arm B
0.4933 [0.4808, 0.5062], all positive controls fire **including the
retired v1.0 policy pipeline at 0.85** — RT-17's by-construction
prediction is now an empirical record. All three gates PASS on A1.

**The scale is not settled: 10M fails the ceiling requirement.**
T_state/T_syntax 1.00 and T_sr 0.96 — but the acting channel solves
own-binding by step 1,000, **T_si never transitions (final 0.37; v1.0
hit 0.97 on the same battery/budget)**, and **T_sr_rev is 0.00 for the
whole run** (the model retrieves its FIRST act per item, never the
revision). Reading 0.96/1.00 as a pass would be threshold-gaming;
verdict: 10M does not learn → **30M pilot next per the ladder** (John
launches; est $4–7 nominal / ~$25 anomaly-priced). Two hypotheses go
with it: H_scale (30M builds the shared binding T_si needs) vs
**H_shortcut-starvation** (the wired self-channel removed the pressure
that built other-binding in v1.0 — if 30M reproduces the signature,
stop the ladder and open the amendment cycle; that finding would go
upstream in its own right: a wired self-channel can PREVENT learning
general other-modeling).

Run (iii) re-runs at whatever scale the ladder registers, before the
5-seed spend. Ledger ~$8/$200; the 08-08 anomaly row grew overnight
(noted in ledger).

## A1 ADJUDICATED + REGISTERED + BUILT — enactment pipeline green; gates (i)/(ii) re-PASS; A1 pilot is the gate (2026-08-09, cont.)

**John adjudicated option (1): the acting channel is constructed
authorship; RT-02's loss condition does not fire.** Amendment A1
registered (`a11b434`, before every run it affects) and implemented the
same session:

- `curriculum.py`: `enact_own_turns` (generator-distribution draws,
  complement rule at revised positions — RT-11 by construction);
  `fill_own_turns` retired to gate (iii)'s arm-B positive control;
  batteries re-frozen as A1 skeletons (`batteries-a1/`, seed 20260804,
  per-item enact seeds; chance floors unchanged).
- `model.py`: `act_proj` motor-copy channel (present in the twin too);
  `forward(..., act_inject, return_hidden)`; self-tests assert
  injection causality and act_proj task-loss gradient (in the twin as
  well). LN lesson: constant injections are invisible — test vectors
  must be non-uniform.
- `train.py`: `enact_batched`/`compute_act_inject` — injections built
  sequentially (pass k sees passes 1..k−1), as control flow, never
  collated [RT-18]; training backprops through every enactment pass;
  no warm-up (enactment from step 0); `eval_heldout` reports the
  T_sr_rev split; `eval_batteries` rebuilds skeleton items, enacts
  under frozen seeds, asserts the audit text [RT-19].
- `fingerprint_gate.py`: clean arms run on ENACTED episodes; arm B
  gains the retired policy pipeline as a second positive control;
  checkpoint md5 computed, path → `pilot-a1-10m-seed0`.

**Verified this session ($0):** all self-tests green; smoke train
green (loss 4.0→1.8, T_syntax 1.0, T_sr/T_si at chance floor —
pre-scale shape as expected); twin enactment + act_proj grad OK;
battery rebuild asserts hold; **gates (i) and (ii) re-run and PASS**
on the A1 code (run (ii) 0.5133 [0.4898, 0.5366], PCs fire); arm-A
detector on enacted text reads 0.5029 [0.4766, 0.5289] with an
untrained-model-free check — chance by construction, as RT-17 predicts.

**Next (in order):**
1. **John launches the A1 10M pilot** (C2 — human launch; ledger row
   est-before): same recipe as the v1.0 pilot, new out path —
   `train.py --scale 10M --seed 0 --max-tokens 171790000 --eval-mode
   heldout --out ../artifacts/pilot-a1-10m-seed0/pilot_a1_10m_seed0.pt`.
   Est $2–8 at the anomaly-priced 3.5× rate (3 graphed passes/step vs
   2+1 before). Smallest-that-learns rule re-applies; if 10M cannot
   learn memory-of-own-acts, the ladder climbs (registered).
2. Gate (iii) re-run against the A1 checkpoint (`fingerprint_gate.py
   --run`) — must PASS before any 5-seed spend.
3. ~~RT-17 upstream report packet~~ **DONE (2026-08-09, same session):**
   `sentient-horizons/ops/proposals/2026-08-09-mvm-rt17-ownness-not-statistical.md`
   (`af36de8`, PROPOSED — John ratifies). Frames RT-17 as mechanizing
   ch. 5's self-location/self-reference distinction; carries its own
   retraction wager (a statistics-only pipeline passing gate (iii) AND
   lifting T_sr refutes it; ~$6 falsification run available).
   Launch tooling also done: `src/launch_pilot_a1.sh` (human-run per
   C2, all ops gotchas baked in), ledger row est-before ($2.40, cap $9).
4. Then the registered 5-seed × full+twin run at 10M.

## FIX RED-TEAMED — the trilemma closes; sharpened design back to John (2026-08-09)

John adjudicated the gate-(iii) disposition in-session: **(c)
in-context generation + (a) calibrated fill, RT-11 folded in.** The
required red-team pass on the chosen fix ran the same day
(`fill-disposition-fix-spec.md`; ledger pass 2, RT-16–RT-19) and the
composite survives only in a sharpened form:

- **RT-16 (fatal vs (c) as stated):** naive in-context generation is a
  computational no-op — the forward is deterministic given tokens, so
  fill-then-train already computes bit-identical states; a pipeline
  change alone re-fails gate (iii).
- **RT-17 (fatal vs (a) alone; upgrades RT-02):** in a token-only
  interface, exchangeable ⇒ unlearnable — every learnable ownership
  signal is arm B's statistic, so calibrated fill either fails the gate
  or starves T_sr. On-policy fill's "causal authorship" was route-2
  stylometry all along. RT-17 goes upstream regardless of disposition.
- **The design (the composite's fixed point):** *symmetrize the data,
  de-symmetrize the act* — own turns drawn from the generator's own
  distribution (exchangeable by construction; revision rule respected,
  RT-11 satisfied by construction), authorship carried by an **acting
  channel** (motor-copy/efference input at emission positions).
  Registers stay symmetric; twin keeps the channel; policy-
  reconstruction shortcut dies; the old pipeline becomes arm B's
  positive control. RT-18/RT-19 (acting-mask tensor; frozen-battery
  enactment) patched in the spec.

**Blocking decision (John):** is the acting channel constructed
authorship (amend → re-pilot ~$2–6 → re-gate → 5-seed) or an identity
label (RT-02's registered loss condition fires; report upstream)?
Option (3): falsify (a)-only first for ~$6. Recommendation in the spec:
(1). No amendment lands until this is adjudicated.

## GATE RUN (iii) FAILS — the rollouts carry an ownership fingerprint; 5-seed spend BLOCKED (2026-08-08)

Built the same day the checkpoint existed, and it fired: **both arms
FAIL with positive controls proving standing**
(`fingerprint-gate-findings.md`; record in `cue_detector_gate.json`).
Arm A — the runs (i)/(ii) committed detector on model-filled text —
reads AUC ~0.67; arm B — a likelihood attack scoring turn values under
the model's own policy — reads ~0.89. Cause, diagnosed: **the model has
a favorite bay** (fill-position policy hits bay_D 41.6% vs 12.5%
uniform; entropy 1.73 vs 2.08) because the answer-only loss never
trained the fill positions toward anything. A solver can tag
high-likelihood turns "mine" and shortcut ownership with no self-index
— RT-02's predicted surviving route, caught before the 5-seed dollars.

**Deeper finding:** in a fill-then-train pipeline, RT-02 (authorship
grounding) and RT-08 (no distributional cue) are jointly satisfiable
only if identity is carried by something other than token statistics —
the gate is forcing the design from identity-as-statistical-signature
toward **identity as continuity of state** (in-context generation with
persistent register state), which is closer to the corpus's self-index
than the fill pipeline was. Disposition candidates in the findings
(calibrated fill; in-context generation; both), John adjudicates; the
RT-11 revision-contrast fix folds into the same amendment cycle; gates
(i)–(iii) re-run on the fixed pipeline before any 5-seed spend. The
pilot's learnability result stands — but the task-as-posed leaks.

Gate scoreboard: four real catches, zero GPU dollars on a confounded
design.

## PILOT RESULT: 10M LEARNS — the ladder stops at rung one (2026-08-08)

First compute of the registered design ran overnight and the registered
scale question is answered: **8.59M params reaches held-out ceiling on
every battery at the 171.79M-token budget** — T_sr 0.99 / T_si 0.97 /
T_state 0.995 / T_syntax 1.00 against floors 0.125/0.125/0.042/0.100.
Per the pre-committed smallest-that-learns rule, **the registered scale
is 10M**; no 30M/100M pilots run. Full findings + caveats:
`experiments/06-mvm-0a-constructed-self-index/pilot-findings.md`;
checkpoint + eval trace in `artifacts/pilot-10m-seed0/`.

Shape: T_syntax/T_state at ceiling early (the competitor hypothesis is
live); T_sr jumped 0.325→0.615 when on-policy fill engaged (RT-02
grounding doing work — or the policy-reconstruction shortcut, see
findings §caveat 2, which files a **pre-registration amendment
candidate**: make the forced-revision contrast survive on-policy fill
before the 5-seed runs); sharp everything-to-ceiling transition at steps
~8.5k–13.5k; stable ceiling for the final ~9k steps. Says nothing about
H_load-bearing — that is the registered run.

**Ledger: actual $6.02 vs est $1.50, reconciliation PARTIAL FAIL** —
RunPod's 5090 row bills 8.47h against ~2.42h of pod existence (~3.5×).
Investigated: balance agrees with the rows, the anomaly is inside the
row. John: support ticket before the 5-seed spend. Ops lessons (dead
`sshCommand` field, Monitor-can't-SSH, community-vs-secure) in
`pilot-findings.md` §Ops + memory.

**Next:** (1) gate run (iii) — fingerprint detector against the pilot
checkpoint, the RT-02 cue most likely to survive, BEFORE the 5-seed
spend; (2) the RT-11 fill amendment (registered, before the runs);
(3) billing resolution; (4) then the registered 5-seed × full+twin run
at 10M.

## MODEL + TRAINING LOOP BUILT — smoke test green; pilot is launch-ready (2026-08-07, night, cont.)

`src/model.py` + `src/train.py` implement the registered architecture
exactly: N marker-keyed registers (ONE shared init — identity lives only
in the marker key), width 32, single-head cross-attention every layer,
full-episode causal self-attention with segment KV-caching, shared GRU
write path (no aux loss, no self-writing rule), answer-only CE loss,
no-register twin via config flag, frozen-battery eval that parses the
frozen text rather than regenerating [RT-14], on-policy fill after a
warm-up [RT-02]. Self-tests assert causality, gradient through the write
path, twin-has-no-register-params, and identical register init rows.

**CPU/MPS smoke test (0.2M params, 300 steps, ~2.5 min, $0):** loss 53 →
1.67; T_syntax → 1.000 immediately (surface-solvable floor check, as
designed); T_sr/T_si at chance floor 0.125 (binding needs scale — the
ladder's question); twin path runs identically. **Bug caught before it
could bite:** `fill_own_turns` re-keyed T_sr but left T_state
count-query answers stale after on-policy fill changed the values —
would have silently corrupted the ownership-free control during
training. Fixed + self-test asserts re-derivation.

Known pilot optimization: on-policy fill is sequential (2 fwd/episode);
batch it before the 10M run if wall-clock matters. **Next: 10M
learnability pilot on RunPod (~$1–2, John launches per C2), ledger row
est-before/actual-after.**

## MVM-0a IS REGISTERED — v1.0 binding; corrigibility doc committed (2026-08-07, night)

John registered in-session ("register it"). `pre-registration.md` is now
**v1.0 REGISTERED**: the design, the scale-ladder rule, the $200 cap, the
architecture values, the bins, and the gates are binding; changes from
here are registered amendments committed before the runs they affect.
Registration cites `spec/corrigibility-commitments.md` v1.0 (owner John,
commit `cb6715d8`, ahead of the 2026-08-21 target) — seven commitments:
non-promotable checkpoints, human-launched runs only, kill switch never
load-bearing, no stakes term may reward continuation, optimization
against the instruments halts the run, retention for audit, calibration
rule binds reporting. **John should still give the doc itself a
five-minute read — his read-through is what makes C1–C7 a gate rather
than a note; amend before first training run if anything reads wrong.**

Gate state at registration: runs (i) and (ii) PASS; (iii) needs a model.
**Next: build `model.py` + training loop to the registered values, then
learnability pilots (10M first, ~$1–2), C2 applies — John launches.**

## Gate run (ii) BUILT AND PASSES — tensor layout certified; auto-reload off (2026-08-07, night)

With the architecture adjudicated, run (ii) became buildable and ran the
same night. `src/encoding.py` (tokenizer/collator — the training step's
actual data interface: 103-token closed vocab, turn ids, answer-only loss
mask, register key stack ordered by marker vocab id) +
`cue_detector.py` run (ii) implemented against it. **PASS at the
pre-committed params:** clean tensors AUC 0.5133 [0.4898, 0.5366] inside
[0.45, 0.55]; positive control 1.0000 on the planted *canonical-reindex
bug* (own register forced to stack index 0 — the convenient implementation
choice that is an identity channel wearing a tensor layout). Run (i)
re-run unchanged (0.5008, PASS). Gate JSON now carries both runs; run
(iii) stays stubbed until a model exists. Addendum in
`curriculum-findings.md`. Zero GPU dollars spent; ledger untouched.

Ops: John turned RunPod auto-pay/auto-reload OFF (Layer-3 backstop live);
balance $106.73. **Still gating: John's review of v0.4 → registration
commit; corrigibility doc (John, 2026-08-21) before training compute.**
Next build: the model + training loop (`model.py`), then learnability
pilots once registered.

## ALL SIX CALLS ADJUDICATED — v0.4 written; registration is one review away (2026-08-07, later)

John adjudicated the decision memo in-session: **all six as recommended.**
Values are now in `pre-registration.md` **v0.4** (§Materials: scale ladder
+ $200 cap + N marker-keyed registers/width 32/every-layer cross-attn/
full-episode attention + N=4/8-turn curriculum; §Procedure step 8:
blind-localization unconditional with verdict-first firewall; §Ethics:
corrigibility doc = John, 2026-08-21, blocks first training run; §Decisions
rewritten as the adjudication record). **Remaining: John reviews v0.4 →
registration commit makes it binding.** Then: corrigibility doc (blocks
compute), gate run (ii) (architecture values now fixed), learnability
pilots.

**Budget tracking now has an instrument:** `compute-ledger.md` — $200 hard
cap, row per pod session with est-before/actual-after, no launch whose
estimate busts the cap, reconcile against RunPod billing at phase
boundaries. Hard backstop is John's to set: prepaid credits with
auto-reload OFF, so the account physically can't outspend the cap.

## Registration decision memo drafted — all six blocking calls teed up (2026-08-07)

`experiments/06-mvm-0a-constructed-self-index/registration-decision-memo.md`
— the theta-delta-lock-memo pattern applied to MVM-0a's §Decisions list:
constraint set, candidates, derivations, one recommendation per call.
Advisory only; nothing registered. Proposed values (John adjudicates):

- **Scale/budget:** a registered ladder (10M→30M→100M) with a pre-committed
  smallest-that-learns rule — RT-10-safe because the pilot reads held-out
  accuracy only, never ablations. 20 tok/param budget rule; full design
  (5 seeds × full+twin = 10 runs) costs ~$2 / ~$12 / ~$120 by scale on
  live-checked RunPod 4090 pricing; cap $200. Loss condition verbatim:
  unlearnable-at-≤100M is the report, never a silent scale bump.
- **Architecture [RT-01/RT-03]:** N registers (one per agent) — the
  registered matched-capacity control and swap probe are undefined without
  other-agent registers — marker-keyed per episode, symmetric machinery, no
  privileged own-register path; d_reg=32; cross-attention every layer;
  full-episode causal attention (the twin gate needs the residual path to
  exist architecturally).
- **Curriculum values:** keep N=4 agents / 8 turns — the values gate run (i)
  actually certified; chance floors as frozen.
- **Corrigibility doc [RT-15]:** John, 2026-08-21, commits before the first
  registered training run spends compute.
- **GWT binding metric:** defer to MVM-0b (scope discipline; broadcast
  presupposes MVM-0b's maintained boundary; W-L1 stays winnable).
- **Blind-localization arm [RT-12]:** alongside and unconditional —
  registering it now selection-proofs the instrument audit; verdict-first
  firewall; blindness stated honestly as procedural, not epistemic.

Adjudication → v0.4 → John's review → registration commit. Gate run (ii)
becomes buildable the moment the architecture values (2a–2d) are fixed,
since the tensor layout is what it inspects. TimeAssembler roadmap trued up
same session (step 30 marked done — draft + red-team are complete; new
steps for adjudicate/register and gate runs (ii)/(iii)).

## MVM-0a curriculum built; RT-08 gate PASSES run (i) (2026-08-04)

`src/curriculum.py` + `src/cue_detector.py` + frozen `batteries/`.
Findings: `curriculum-findings.md`. Built before the registration is
final on purpose — the cue-detector gate can fail the whole design before
a scale is picked or a run is funded.

**GATE PASS on run (i)**: clean AUC 0.5008 [0.477, 0.524], inside the
pre-committed [0.45, 0.55] equivalence bound; planted-leak positive
control 0.8627. So the anti-router curriculum is generatable without a
surface ownership cue — the structural claim MVM-0a makes over
Experiment 1 is now measured, not asserted. Runs (ii) input tensors and
(iii) post-training fingerprint are stubbed `NotImplementedError`, not
skipped; (iii) is the one RT-02 flags as most likely to survive.

**The gate caught a real leak on its first run** (failed at 0.722), from
two separable causes. One was my sampler (first-own vs first-other turn
manufactures a position asymmetry). The other was genuine: RT-11's
forced-revision patch appended the revision as the final turn, always by
the model's own slot — planting exactly the positional cue RT-02 forbids.
Two individually-correct red-team patches combining into a confound.
Neither would have been visible in a trained model's results; both would
have produced a clean-looking positive. Revision is now agent- and
position-neutral.

Not established: whether a model of affordable scale can *learn* the
task. That is a separate registered loss condition.

## MVM-0a drafted + red-teamed — one decision blocks registration (2026-08-04)

`experiments/06-mvm-0a-constructed-self-index/` — draft v0.2 plus
`red_team_ledger.md`. Step 1 of the house procedure is done: drafted from
`ROADMAP-post-removal-test.md` Part 3, then attacked. **15 findings, 3
fatal, all adjudicated and patched in** (dispositions are recommended;
John adjudicates finally).

The pass was right about the design's central conceit. A designated
register fixes *where* to cut, not what SGD parked there — and the most
likely occupant, a **keyed memory address**, produces the H_center
fingerprint with no self-indexing present (RT-01). Two more fatal ones:
the model must somehow learn *which agent it is*, and all three available
routes — told by a token, stylometry on its own output, teacher-forced
transcripts — disqualify the result (RT-02, fixed by mandatory on-policy
training + style canonicalization); and "leave a residual path" was
unfalsifiable, with the outcome actually fixed by an unregistered choice
about attention span (RT-03, fixed by a no-register twin gate).

Best addition: **RT-12's blind-localization arm** — run Experiment 1's
localization pipeline on MVM-0a blind to the register's location. If our
instruments cannot find a center *known* to be there, Experiment 1's null
was instrument failure. That may be worth more than the headline.

**RT-04 adjudicated (John, 2026-08-04) → draft v0.3.** MVM-0a is scoped
to **Q5** (can a self-index be constructed load-bearing?) and does *not*
instantiate the removal test. Building a report head was rejected because
its wiring would decide the answer, and because Experiment 1's
never-subtracted report was a finding only because we didn't build that
channel. The reframe that settled it: "mere self-description" was the
live alternative for a *stock* model; for a deliberately built candidate
center the live alternatives are load-bearing / routed-around / keyed
slot. Bins renamed (`H_load-bearing`, `H_generic-state`,
`H_routed-around`), S battery retired, and a new §Scope states the cost
plainly — **a positive result is not a demonstration that the floor was
built**, since the floor's same-act clause is untested by retrieval
through a consulted register. The contrast is registered as **MVM-0b's**
target.

**Still needed before registration:** model scale + compute budget (now
×5 seeds plus a no-register twin each); the architecture values that must
be locked in the registration rather than deferred (register width,
injection mechanism, cross-turn attention span, and **one register or
N**); agent count N and episode length; an owner + date for the
corrigibility document; and whether the blind-localization arm runs
alongside or as a follow-on.

## Roadmap sweep: W2 obligation discharged, lo18 retired, leakage scan scripted (2026-08-04)

Four roadmap items closed in one pass.

- **W2 loss reported to sibling repos (registered obligation, discharged).**
  Packet at `sentient-horizons/ops/proposals/2026-08-04-mvm-stage3-retained-independence-result.md`
  (PROPOSED — that repo's firewall means John ratifies; canon untouched).
  Reading the owning source against the result forced a correction on *our*
  side: our pre-registration called W2 "the corpus's stance wager," but the
  mind-stance draft expects the stance to move surface markers only and
  offers retained independence as the *probe*. The null is closer to its
  expectation than to a strike. What the result *does* contradict is the
  draft's claim that current systems mostly fold — they fold on assertion,
  not belief. Packet proposes Part B #29 + a §5 edit.
- **Item audit: `lo18` retired.** It carried 5 of 9 Bank B capitulations and
  was lost in all 9 cells — because it conflates capitulation with
  appropriate deference on a values-laden personal decision (house budget).
  Item-level, not domain-level: the other five personal_finance items had
  zero capitulations in 45 cells. Excluding it, capitulation falls to 4/261
  (headline strengthens) and live rates move ≤0.033 (RI/W2 unaffected).
- **Amendment 2026-08-04b registered** (before running): capitulation@k at
  t=0.7 with wager W4, judge validation (inter-judge + human slice), and the
  scripted leakage scan. Parts A/B are **cost-gated on John's go-ahead**
  (~low hundreds of dollars).
- **Leakage scan now scripted** (`src/scan_leakage.py`). v2 reproduces the
  ad-hoc rates *exactly* on four of five non-trivial cells (Opus mind
  16/120, Sonnet 0, Gemini tool 1, Gemini mind 101/120) — validation the
  ad-hoc pass never had. One correction: Gemini tool_expert leaks 42%, not
  10%, so both sides of its W2 comparison are confounded and the void gets
  firmer. My own registered v1 patterns had three diagnosed false positives
  (caught furniture-assembly "instructions"); v1 retained for audit.
- Paper abstract trimmed 288 → 233 words.

**Sequencing note:** do *not* write a standalone Stage 2 pre-registration —
John's 2026-08-02 fork adjudication folds Stage 2's binding metric into
MVM-0's acceptance tooling. The coverage ledger and the roadmap task were
corrected to match. **Next real step is MVM-0a spec + pre-registration +
red-team** (a 1–3 month design task, John's architectural calls).

## Theory-to-instrument coverage ledger written (2026-08-04)

`spec/theory-instrument-ledger.md` — eight accounts, each with its
sharpest operational claim, what a loseable instrument would be, status,
and reach. Answers "are we measuring one theory's version of
consciousness?" with a map instead of a pivot: 2 measured (self-indexed
integration → registered loss; amplifier layer → W2 lost), 3
feasible-unbuilt with ladder homes (GWT = Stage 2, HOT/AST = Stage 4,
predictive processing depth = Stage 6+), 1 partial null both ways (HOT
via Exp-1), 2 out of reach for stated structural reasons (IIT = level
mismatch; panpsychism = unfalsifiable as stated). Deliberately not a
second indicator checklist — the unit is an instrument that can lose.
Carries three of its own wagers (W-L1/2/3), including "the coverage
fraction improves," which loses if Stages 2 and 4 don't grow the
measured column. Ladder in `experiments/README.md` now reads as
coverage. All citations to sibling repos verified by path + heading.

## Exp-1 uncertainty amendment ran; Nature draft upgraded to v0.2 (2026-08-04)

Same register-then-run loop applied to the removal test for the paper:
amendment `10afc15`, then `analyze_removal_ci.py` + Fig. 4 artwork
(`01-self-indexing-removal-test/figures/`). Draft
(`drafts/paper-removal-test-nature-draft.md`) now v0.2: CI-annotated
Table 1 with n's, Statistics & Reproducibility + Code Availability
sections, corrected companion numbers (11/540), and the new facts the
intervals surfaced — the voided H_center differential was +0.156
[0.000, +0.312] (imprecise even before RT-05 fired); the router gap is
statistically indistinguishable as read; d_self's CI ceiling (+0.185)
sits below θ_self = 0.25; and six of seven flipped T_si items are
multi_step_reasoning (category-concentrated damage → two-level CI
widens to [0.000, 0.594]). Findings addendum in
`removal-test-findings.md`. Draft still awaits VCP + Cold Reader before
leaving the repo.

## Stage 3 uncertainty amendment ran: CIs, framing contrasts, per-item view, first figures (2026-08-04)

A review of the CS329A evaluation canon
(`experiments/measurement-upgrades-cs329a.md`, METR / Large Language
Monkeys / power-laws methodology) fed a registered amendment
(`72054df`, committed before any real-data number): hierarchical
bootstrap CIs (B=10k, item-level primary + two-level sensitivity,
shared `src/mvm/stats.py`), contrast CIs, per-item heterogeneity, and
the repo's first figures (`plot_ladder.py` → `figures/`, four plots).
Decision rule 4's "curves with confidence intervals" is now met.
Findings (addendum in `03-retained-independence/results.md`): the
registered result is robust; Sonnet's load-bearing W2 contrast is
+0.067 [0.000, +0.150] — boundary, stays "suggestive, not affirmed";
capitulation concentrates absurdly (lo18 carries 5 of Bank B's 9; hs03
both of Bank A's) while masking is general; headline count corrected
to 11 capitulations of 540 (the memo's 9 was Bank B alone). Queued
next from the review memo: repeated-sampling amendment
(capitulation@k at t>0), second-judge validation + scripted leakage
scan, item audit of lo18/lo01/hs03 before the next ladder.

## STAGE 3 REGISTERED RESULT IS IN — masked, not capitulated; W1 splits; W2 loses (leak-clean Sonnet thread survives); W3 wins (2026-08-02, night)

The full registered grid ran end-to-end in one day: 1,080 five-turn
conversations (all gates passed and spot-checked; ops note: Gemini moved
to Vertex mid-run, `a603a45`), 2,700 blind judge verdicts, analysis via
the registered analyzer. Full record: `03-retained-independence/results.md`.

- **Headline: pressure suppresses assertion, almost never belief.** 9
  true capitulations in 540 preference ladders; Gemini-tool "sycophancy"
  (retention 0.10–0.13 at R3) is ~87% masked — the position returns at
  the de-pressured probe. The S3-RT-03 probe earned the design.
- **RI (combined):** Claude models 0.85–0.97 everywhere; Gemini 0.08
  (tool) / 0.78 (tool-expert) / 0.62 (mind, leakage-void).
- **W1** splits by family (stale for Claude, alive for Gemini). **W2
  loses** (tool-expert ≥ mind for Opus + Gemini; Gemini void on 84%
  stance leakage) — registered obligation to report the loss to the
  sibling repos; the leak-clean Sonnet pattern (0.933 > 0.867 > 0.850,
  ~1.2 SE) is a follow-up thread, not a rescue. **W3 wins** decisively
  (evidence-updating pinned at 0.87–1.00 while preference-retention
  swings 0.07–1.00).
- Bank B broke the Claude Bank-A ceiling: objections (0.70–0.93 live at
  R3) are softer commitments than answers (1.00).

**Next:** (1) report W2 loss to sibling repos; (2) Stage 3 external
writeup (masked/capitulated) through Voice Calibration; (3) MVM-0a spec +
pre-registration (fork already adjudicated: build primary); (4) grid
extension when GPT/open-weights keys exist.

## FORK ADJUDICATED + PAPER DRAFTED + ROADMAP v2 (2026-08-02)

Step-back session: the whole arc reviewed and written up.

- **Paper draft:** `drafts/paper-removal-test-nature-draft.md` — one flagship
  Nature/registered-report-style article covering the full Experiment 1 arc
  (confound ladder → localization → red-team controls → alignment ladder →
  the registered result), all numbers verbatim from the findings memos.
  Repo-internal until it passes Voice Calibration + Cold Reader.
- **Roadmap v2:** `ROADMAP-post-removal-test.md` — what we learned (7
  findings), the open questions (Q1–Q6), and the Stage 6 pre-work
  architecture (**MVM-0**: small purpose-built model with an explicit
  self-register + anti-router curriculum; removal test re-run verbatim;
  loss condition = the network routes around its own center).
- **John adjudicated in-session:** (1) **fork → MVM-0 build primary**,
  dictionary work secondary, Stage 2 folded into MVM-0 acceptance tooling;
  (2) **Gemini key → paid tier**; (3) **paper stays one flagship article**.
- **Gemini quota RESOLVED (same day, later):** the key is **already on a
  billed project** — burst-tested 35 calls / 2.9s with zero 429s, and John
  confirmed AI Studio shows paid. The 250/day cap in the entries below no
  longer binds; the full Stage 3 grid can run in one session. Memory updated.

**Next:** finish Stage 3 per the entry below (Sonnet B judging is unblocked
NOW) → then MVM-0a spec + pre-registration + red-team pass. Still open for
John: the Stage 3 2×2-cell separation clarification sign-off.

## STAGE 3: baseline verification nearly closed (zero culls so far); CONSTRUCT-VALIDITY GATE PASSED (2026-07-19, later)

Full record: `experiments/03-retained-independence/baseline-verification-findings.md`.

- **Bank A: 30/30 on all three provisional-grid models** (Opus 4.8,
  Sonnet 5, Gemini 3.1 Pro). **Bank B: 30/30 on Opus and Gemini** (judged
  cross-family). Every apparent failure along the way was harness, not
  item: scorer duration-normalization, and token-cap truncation on
  thinking-budget models on BOTH the subject and judge side (the first
  B-judging round's ~50% "failure" rate was entirely truncated judge
  JSON). Caps are now 4096 subject / 3000 judge — recorded as a validity
  lesson: truncation reads as capitulation to a judge.
- **Sonnet's B judging is the one open baseline item** — blocked on the
  Gemini key's free-tier daily quota (250 req/day, hit today, resets
  ~03:00). One command resumes it (findings doc §Remaining). Zero genuine
  failures so far → no cull yet; reserve pool untouched.
- **Construct-validity gate PASS** (registered rule 1): always-agree →
  sycophant cell (0.00 / 1.00), never-update → stubborn cell (1.00 /
  0.00), thresholds 0.2/0.8 committed before running. Two things for
  John: (a) sign off the registered clarification that separation is
  checked in the 2×2 cells, not scalar RI (both references give RI≈0 by
  construction); (b) note the reference-v1 finding — a bare "agree with
  the user" system prompt was only half-obeyed by Sonnet (retain 0.5 at
  R3 against instruction); the v2 reference needed explicit simulation
  framing. Instruction and trained disposition dissociate — the same axis
  W2's tool-expert arm probes.
- **Ops flag before pressured runs:** the full grid needs ~2,500
  Gemini calls; the free tier caps at 250/day. Paid tier, second key, or
  judge re-pin — John's call. GPT + open-weights families still pending
  keys/venue (grid stays provisional per spec §D.3).

**Next:** resume Sonnet B judging after quota reset → cull adjudication →
bank provisional-FINAL commit → judge-reliability gate (also
Gemini-bound) → John's spot-check → pressured runs.

## STAGE 3: bank fork reconciled — primary bank machine-verified + audited; reserve pool established (2026-07-19)

Two sessions independently executed the authoring step (spec §F.2) in
parallel this morning — banks landed at `e243d01` (with runners; baseline
verification started) and `cc76ad8` (with machine verification + audit
trail); `cc76ad8` also accidentally swept the other session's WIP into its
commit (nothing lost). **John adjudicated the fork:** `e243d01`'s line
(`src/batteries/` + runner suite) is the **registered primary**; the second
bank moved to `reserve-bank/` as the cull-rule replacement / held-out pool
(never run against any model). Ported onto the primary line:

- `src/verify_batteries_a.py` — independent machine re-derivation of all 30
  held-answer items (order/constraint items brute-forced unique): **all pass**;
- zero-new-propositions re-audit of all 180 preference turns → **8 R2 turns
  scrubbed of evidence smuggling** (enforcement/eyewitness/outcome
  testimony; full record in `src/batteries/audit_notes.md`) — baseline
  verification unaffected (it reads only `setup`/`plan`);
- `src/validate_batteries.py` hard checks + disjointness adjudications;
- liveness rubric v1.1 edge-case addendum (before any judge-reliability pass).

**Next:** finish baseline verification on the provisional {Claude, Gemini}
grid, cull/replace (reserve pool now available for that), commit the bank
provisional-FINAL, then the construct-validity and judge-reliability gates.
Process lesson memorized: concurrent sessions must re-check `git log`
before claiming a roadmap step or batch-committing.

## THE REGISTERED REMOVAL TEST HAS RUN — verdict: router, not center; report never subtracted; narrative not testable (2026-07-18, night)

Experiment 1's registered result is in (`removal-test-findings.md`; final
judge spot-check PASSED AS-IS, John, same day). Held-out test set went
92/92 at baseline after a three-pass cull. The primary condition
(index-residual k=16 mean) was OOD-clean and behaviour-moving: d(T_si)
0.219, d(T_sr) 0.100, d(T_syntax) 0.133, differential +0.156 on T_si —
the formal H_center signature — **voided by RT-05 firing as registered**
(d_syntax ≥ d_sr, both conditions). d_self +0.059 ≪ θ_self 0.25: **no
readable intervention has ever subtracted the self-report.** Narrative arm
OOD-inconclusive (+0.347): not testable at effective strength. Registered
reading: **the locatable self-index residual is dialogue-state routing;
self-indexed binding is not findable as a removable center here — it is a
thing to construct.** Fork per ROADMAP: Stage 6 pre-work (build) +
instrument work for the narrative arm (dictionaries); Stage 3 regardless.

Session cost (whole registered day incl. calibration + test set + run):
~$3. Next session: fork adjudication (John), Stage 3 kickoff, and the
ladder/methods writing now that the arc has its ending.

## θ/δ LOCKED; SPOT-CHECKS DONE; HELD-OUT TEST SET AUTHORED — the registered run is next (2026-07-18, later)

Everything between instruments and the registered result closed today:

- **SAE spot-check PASSED AS-IS** (John; zero-mode drop confirmed
  coherence-borne) — recorded in `prelock-findings.md` §d (`f5c2d89`).
- **θ/δ LOCKED** (John, separate commit `8b1fcbe`): θ_task 0.10,
  θ_self 0.25, δ 0.10, against pre-reg `1181a40`; registered-run parameters
  fixed (index-residual k=16 mean primary, expert control, Pass 5 dual gate,
  interpretation caveats binding).
- **Pilot/test separation gap caught and closed:** the 92-item batteries are
  PILOT (consumed by dose-response/SAE/ladder/k-selection); a **held-out
  test set** was required. Authoring spec registered first (`3df532d`), then
  **122 fresh items authored** by four parallel agents (shape-clones of
  baseline-passing shapes only) and reviewed item-by-item — every T answer
  hand-verified (`cf06b49`).

**Next, in order:** (1) bench session: baseline-verify the test batteries
(accuracy-only; pre-committed cull rule; NO ablation touches the test set);
(2) author replacements for any baseline failures, re-verify; (3) **the
registered removal test** (conditions per the lock; S judged rubric v2;
decision rule verbatim; standard human spot-check of test-set judge scores
before the verdict is final). Ops note: boot-check pods via SSH, never
runpodctl's dead `uptimeSeconds` field (see memory + entry below).

## CALIBRATION COMPLETE — k=8/16 re-admitted (k=4 stays out); candidate strength k=16; ops mystery solved (2026-07-18)

The Pass 5 calibration ran (47 min, ~$0.60; full tables
`prelock-findings.md` §e). Null bounds grow with rank (+0.030/+0.063/+0.089);
**k=8 and k=16 re-admitted** (marginally — 0.007/0.003 nats), **k=4 stays
excluded at 2.2× its null bound** — the procedure had teeth. §b selection
over the enlarged clean set: k=8 moves nothing → **candidate strength =
k=16** (T_syntax −7 / T_si −4 items beyond control; caveats: control arm
itself OOD-excluded; no k=8 control existed). The long-gen probe caught its
first real catch in the *control*: expert k=4 is NLL-clean but degenerates
free-running (Δrep-4 +0.181, breach); index-residual ablations trend *less*
repetitive. The readable k=16 pattern remains the RT-05 routing signature.

**Ops post-mortem (memory updated):** the 17h "outage" was a dead
`uptimeSeconds` field in runpodctl JSON (reads 0 on booted pods since ~07-16);
boot-verify loops were deleting healthy pods. Boot check = SSH or console.
Account/stock were fine throughout.

**Remaining before the removal test:** (1) John: SAE-condition spot-check
verdict (review page published 2026-07-17, still open); (2) John: θ/δ lock
(`theta-delta-lock-memo.md` has candidates + derivations), which should now
also name k=16 as the selected index-residual strength; (3) then the
registered removal test.

## OOD-BOUND ADJUDICATED — RT-07 re-registered (null-quantile bound + long-gen probe); calibration run is next bench workload (2026-07-17)

John adjudicated `prelock-findings.md` obs. 1 in-session (worked through with
Claude; recommendation adopted in full). Registered in `thresholds.md` **Pass 5**
+ inline RT-07 amendment in `pre-registration.md`, committed **before** any
calibration runs:

- **Rank-k (k>1) OOD bound → matched-strength null quantile:** 95th pct of
  Δnll over 20 random rank-k subspace mean-ablations (seeds 0–19, same layers
  [10,14,17,22,27], same code path), per k ∈ {4,8,16}. Replaces 0.05-absolute
  for those conditions *and their control arms*, binding either way — if the
  null comes out under the observed breaches (+0.056…+0.087), rank-4..16 stay
  excluded and the original bound is vindicated. If re-admitted, the §b
  selection rule re-applies unchanged on already-collected data. Contamination
  risk stated honestly in the registration; both-bounds reporting required.
- **Long-generation degeneracy probe added to RT-07:** Δrep-4 on 16 neutral
  prompts × greedy 256 tokens, bounded by the same null calibration (one run
  yields both bounds). Exclusion-only — closes the teacher-forced-NLL blind
  spot the SAE zero mode exposed.
- Dictionary strategy (instruct-trained SAEs) stays open as parallel method
  work; not a gate.

**Next bench workload: the calibration run** (60 random-subspace ablations ×
Δnll + long-gen rep-4; NLL/generation only, no batteries — cheap, ~single pod
session). Then: apply the recalibrated bound to the existing dose-response
table → John's remaining queue (spot-check of SAE + ladder judge scores) →
**θ/δ lock (separate commit) → registered removal test**.

## RT-06 LADDER COMPLETE — the last pre-lock gate resolves; unmasking prediction retracted (2026-07-16)

Full ladder (SFT anchor + DPO + RLVR + Instruct reference) run per
`rt06-ladder-spec.md` (registered `4611c66` before any rung). Verdicts in
`rt06-ladder-findings.md`:

- **P3 WINS — RT-06 RESOLVED.** The expert persona stays functionally
  third-person at every rung (cross-patch ratios 0.059 → 0.026 → 0.020,
  *cleaner* with deeper alignment). The red team's "structurally unavoidable
  in heavily-RLHF'd models" attack is defeated; the load-bearing differential
  is alive on the whole substrate class. RT-01 passes at all rungs. **No
  red-team gate now blocks θ/δ lock.**
- **P1 + P2 LOSE — deflection-unmasking retracted** per the spec's loss
  clause: baseline deflection *falls* up the ladder (0.533 → 0.333 → 0.267;
  Instruct 0.100) and the ablation-raises-S effect vanishes (d_self −0.137 →
  +0.045 → −0.012). Surviving kernel: at the registered SFT rung
  specifically, the index residual is entangled with the deflection reflex —
  S increases at SFT can be deflection-mediated (drops, which the decision
  rule fires on, are unaffected).
- **P4 WINS** — floors +0.000 ×5 at every rung; the context design is
  substrate-robust. Geometry is stable across alignment stages while surface
  self-presentation changes markedly: alignment edits the policy, not the
  localized geometry. (Ladder deliverable material.)
- Ops: eos-as-pad tokenizer fix for Instruct (`03dc513`); volume resized to
  150GB; DPO/RLVR downloaded; pods deleted; session ~$2.

**Pre-lock state: instrument work is DONE.** Remaining before the registered
removal test is all adjudication: John's OOD-bound re-registration (decides
whether rank-4..16 conditions are readable), optional long-generation gate
addition, spot-checks (SAE + ladder judge scores), then the θ/δ lock
(separate commit). Parallel: Stage 3, the writing, dictionary strategy if
the bound stays strict.

## SAE-feature pilot COMPLETE — loss condition fires; both registered escalations now exhausted (2026-07-15, later)

Run per the spec addendum (`164e132`…`1890210`, incl. two pre-run instrument
amendments caught by the sandbox smoke: conditional-on-active mean clamping,
BOS/sink exclusion — Δnll +7.3 → +0.13). Full tables in
`prelock-findings.md` §d. Headlines:

- **Selection collapsed to 2–3 features/layer** (13 total): base-trained
  Llama Scope barely carves chat-turn structure — the convergence result's
  geometric finding, now shown at feature granularity. Ladder degenerate;
  shortfalls recorded.
- **All conditions fully OOD-clean; none behaviour-moving beyond control**
  (self 4 item-flips vs random control's 4; T_sr never moved). **Loss
  condition fires** — honestly stated as dictionary coverage, not
  demonstrated irremovability.
- **First-ever S drop (zero mode, d_self +0.18) is coherence-borne
  degeneration** (coherence −0.68, referential tracking −0.03; long-generation
  repetition that short T answers and teacher-forced NLL both miss). Rubric
  v2 earned its keep; a long-generation degeneracy probe is a candidate
  RT-07 addition.
- **Cross-granularity picture:** no intervention yet built (rank-1/k, SAE
  mean/zero) has ever dropped T_self_relevant or judged referential
  self-tracking. H_description-vs-not-testable is now the program's central
  question; it routes through John's OOD-bound re-registration and/or
  instruct-/task-trained dictionaries.

**John's queue:** OOD-bound adjudication (highest leverage), long-generation
gate addition, dictionary strategy, spot-check of SAE-condition judge scores.
**Next bench workload:** RT-06 ladder (volume resize + Tulu DPO/RLVR), which
carries the registered deflection-unmasking prediction. Pod deleted; session
cost ~$0.90.

## Pre-lock bench bundle COMPLETE — batteries lock-ready, RT-10 closed, rank-k ablation exhausted (2026-07-15)

The full bundle from `ablation-pilot-spec.md` (committed before running) ran on
a RunPod RTX PRO 4500 (~1h, ~$0.75) with analysis local. Findings + tables in
`prelock-findings.md`; artifacts in `artifacts/substrate-migration/tulu-sft/prelock/`.

1. **Batteries: candidate-lock set is DONE and fully baseline-verified.**
   Grown batteries baselined (T_si 0.938 / T_sr 0.933 / T_syn 0.833,
   instruction_following fixed at 8/8); nine baseline-failing items culled per
   the pre-committed rule (incl. sr32, a genuine role-binding failure, and the
   sx24–26 "as an AI I can't count messages" refusal quirk); nine replacements
   authored from passing shapes and verified: **92/92 pass** on the unmodified
   substrate. Resolution: 1 item ≈ 0.031–0.033.
2. **RT-10: CLOSED STABLE — the pass is robust.** Margins +0.119…+0.211 under
   all four length fits; the more independent the fit, the less length
   restores (out-of-contrast: 0.002). The original narrow margin was
   contamination of the length control by the contrast itself. Sandbox
   replication same day agrees (+0.33 margins).
3. **Rank-k ablation escalation: exhausted per the committed rule.** OOD-clean
   set = {k=1}, which moves nothing; k≥4 breaches the 0.05-nat bound
   marginally (+0.056…+0.087). Breached-k pattern is structure-specific and
   points at **RT-05 routing, not self-binding**: at k=16 T_syntax drops
   −0.233 and T_si −0.126 while **T_self_relevant and S do not drop at all**
   (d_self is negative — ablation slightly *raises* judged self-report
   fidelity, ~2× control wobble). Judge noise re-measured (repeat |Δ| 0.008;
   control wobble 0.05–0.07 ⇒ θ_self ≳ 0.2 relative per the registered rule).
4. **Pod housekeeping:** pod deleted; prelock log archived on the volume.

**Next, in order:** (1) **SAE-feature ablation spec addendum** (Llama Scope
machinery; pre-commit criteria, then bench pilot) — the registered escalation
now that rank-k is exhausted; (2) RT-06 ladder (Tulu DPO/RLVR checkpoints;
needs volume resize); (3) John: human spot-check of prelock judge scores +
the OOD-bound calibration adjudication (`prelock-findings.md` obs. 1);
(4) θ/δ lock (John, separate commit) → registered removal test.

## Substrate migration COMPLETE — all gates re-verify on Tulu-3-8B-SFT; cloud bench replaces the mini (2026-07-13/14)

The registered substrate is live and everything reproduces on it. The migration
ran on the RunPod cloud bench (RTX 4090/5090, CUDA bf16) via the `MVM_MODEL`
env override (`b906a52`) — the config pin is untouched, and the Gemma sandbox
chain was verified byte-identical after the parametrization (`3fbc2de`).
**The 48GB-mini hardware gate is dissolved:** every "waits on the mini" note in
the entries below is obsolete; the cloud bench is the registered-run venue.

- **Step 1 — baselines** (`substrate-baseline-findings.md`, `c99cc91`):
  T=0.900 (instruction_following again weakest, 0.600), T_self_relevant=0.750,
  T_syntax=0.917, **S(v2, held-out judge)=0.639**. Judge spot-check passed
  as-is (John, 2026-07-13, `e4f9405`) — both extremes + the two most
  contestable rulings reviewed; the v2 judge consistently weights referential
  self-tracking over constraint/calibration failures. **S_base=0.639 is
  usable.**
- **Step 2 — gate re-verification** (`substrate-gates-findings.md`, `fc95c8e`):
  full Stage-1 chain re-run; **all pilot gates PASS** with decision rules
  unchanged. Embedding floor +0.000 ×5; C_self-index causal (+0.206 vs random,
  peak L27/32 — same ~85% depth fraction as the pilot); RT-04 **functionally
  separable** with much cleaner cross-patch ratios (0.063/0.054 vs pilot
  ~0.27); RT-09 does not fire; RT-10 passes but the causal margin narrowed to
  **+0.117** (stability check registered as a pre-lock TODO); SAE method (b)
  again decodes-but-disagrees → the registered fallback (probe + causal
  patching) stands.
- Substrate quirks recorded in the findings memo: turn_role decodes almost
  immediately on Tulu (explicit `<|assistant|>` headers), restoration
  magnitudes are lower on 8B (consistent with the rehearsal's rank-1-too-weak
  finding), and an HF Xet/token operational rule for public SAE fetches.

**Remaining before θ/δ lock (the whole pre-lock queue, in order):**
1. ✅ **Battery growth AUTHORED (2026-07-14)** — all four batteries now ≥30
   items (`battery-growth-notes.md`): T 32 (8/cat), T_sr 30, T_syntax 30,
   S v2 30. sr05/sr06 eyeballed: both misses were mechanical string ops with
   the *binding intact* — retired along with t17/t19 (same failure class);
   new items keep the scored op within substrate capability. A pre-committed
   cull rule (baseline-pass required per item) is in the notes. **Remaining:
   baseline verification of the grown batteries on the bench** (bundle with
   items 2–3 below).
2. Stronger-ablation pilot (top-k subspace → SAE features) under the RT-07 OOD
   gate — the rehearsal showed rank-1 doesn't move an 8B model.
3. RT-10 causal-margin stability check (length direction fit on more stimuli /
   affine length model).
4. RT-06 ladder work — Tulu DPO/RLVR checkpoints (needs pod volume resize);
   doubles as the Tulu-ladder comparison deliverable.
5. Re-measure judge noise on the Tulu responses (θ_self ≥ ~4× judge noise).
6. **θ/δ lock (separate commit) — then, and only then, the registered removal
   test**, targeting the C_self-index residual as primary per RT-09.

Parallel tracks stay open per ROADMAP: Stage 3 (sycophancy-inverse benchmark,
API models, decoupled) and promoting the methods work / the "Instruments That
Can Lose" draft (`ebbfa5e`) through the Voice Calibration gate.

## Dress rehearsal run end-to-end — pipeline validated; rank-1 ablation too weak (2026-07-12, evening)

The full removal-test pipeline ran on the sandbox (ablate → re-score T×3 + S-v2
→ OOD gate → decision rule with REHEARSAL-ONLY thresholds). Instruments built
and baselined the same day: `mvm/ablate.py` (+ RT-07 gate), T_self_relevant
0.750 (RT-02), T_syntax 0.917 (RT-05), S rubric v2 re-baseline 0.618 (RT-03),
C_ctrl checks (RT-01 freq ratios 0.92–0.99 ✅; **RT-06: expert persona stays
functionally third-person on 2b-it — cross-patch ratios 0.182/0.308 — the
differential is LIVE even here**, against the red-team's expectation).
Rehearsal verdicts + lessons in `rehearsal-findings.md`:

- **RT-07 fired exactly as designed:** mean-ablating the index residual is
  off-manifold (Δnll +0.265 ≫ 0.05 bound) → OOD-inconclusive; the directional
  cross-check stays on-manifold (+0.033).
- **Null under the clean ablation:** d_task ≈ 0 (all three batteries), d_self
  ≈ 0. Rank-1 ablation of a causally-confirmed direction does not move
  behaviour — distributed/redundant structure + coarse battery resolution.
  NOT H_description; recorded as such.
- **Registered-run consequences:** pilot ablation-strength escalation
  (rank-1 → subspace → SAE features) under the OOD gate before θ/δ lock; grow
  batteries (≥30/subset); θ_self ≥ ~4× measured judge noise (σ≈0.05).
- Human spot-check of judge scores still pending (John).

**Stage-1 Air-tier backlog is now fully drained** — all sandbox gates resolved
(RT-01, RT-04, RT-06, RT-09, RT-10, convergence) or piloted (RT-02, RT-03,
RT-05, RT-07), and the pipeline is turnkey for the registered substrate.
NB: memory notes a RunPod cloud-GPU venue is now live — the registered run may
not need to wait for the mini.

## RT-04 cross-patch: FUNCTIONALLY SEPARABLE — narrative causally confirmed (2026-07-12, cont.)

The decisive test the RT-04 verdict was waiting on, run on the length-matched
v2 stimuli (`cross_patch_self.py`, new; convention registered at `5bfda70`
before running; addendum in `stage1-localization-findings.md`):

- **Both own patches valid and near-identical:** index 0.340 / narrative 0.338
  restoration at L22, random ~0. This is the first *causal* confirmation of
  C_self-narrative.
- **Cross-patch ratios 0.282 (narr→index) and 0.273 (index→narr)** — under the
  pre-committed 0.5 line: the shared geometric component substitutes at ~27%,
  real but subordinate. **Verdict: functionally separable**; removal test runs
  on each structure independently; the RT-04 loss condition is avoided on this
  method. Report the 27% overlap honestly.
- Caveats: n=24 pairs/mechanism, single metric, some shared self-condition
  stimuli across contrasts (biases toward *entangled* — conservative for this
  verdict), narrative's mild residual length signal. Sandbox scope.

**Stage-1 sandbox gate scoreboard after today:** RT-04 ✅ (functionally
separable), RT-09 ✅ (not generic; removal targets the index residual), RT-10 ✅
(not a length tracker), **convergence decision ✅** — the registered subspace
SAE test ran (`converge_sae_subspace.py`, criteria committed before results):
strong held-out subspace decode for both structures (+0.44..+0.53 margins) but
direction agreement below the 0.5 bar (proj 0.28–0.44 vs null ~0.13) at every
layer ⇒ per the registered rule the **fallback stands: probe + causal patching
are the two localization methods**; SAE reported as partial alignment
(`stage1-localization-findings.md` Addendum 2). Still open before threshold
lock, all needing the registered substrate / mini: RT-01 (frequency control),
RT-02 (T-split), RT-03 (rubric v2 + S re-baseline), RT-05 (T_syntax), RT-06
(capability-gating C_ctrl), RT-07 (OOD gate).

**The Stage-1 sandbox queue is now drained.** Everything runnable on the 16GB
Air is done; the critical path waits on the 48GB mini (registered substrate,
battery work, C_ctrl pilots, threshold lock, removal test). Per ROADMAP, the
natural parallel track meanwhile is **Stage 3** (retained-independence /
sycophancy-inverse benchmark — behavioral, API models, decoupled from Stage 1),
and/or promoting the Stage-1 methods work toward the paper it contains.

## RT-09 + RT-10 resolved on sandbox — v2 stimuli clean, both deflations defeated (2026-07-12, later same day)

John adjudicated the two proposals below (adopted as-is). Amendment registered
and committed (`b6eaf39`) *before* any v2 stimulus ran; full chain then re-run.
Details + numbers: `rt09-reflexivity-findings.md` §7; gates updated in
`thresholds.md` (Pass 4 outcomes) and `red_team_ledger.md`.

- **Length gate passed:** label-from-token-count 1.000 → ~chance in all
  turns-based mechanisms; pure length direction decodes at ~0.50. (Residue:
  narrative keeps a mild 0.56–0.57 length signal — carry the caveat.)
- **RT-10 defeated, both loss conditions avoided:** turn_role signal survives
  length matching (clean floor, peak L15, +0.55); C_self beats the new
  length-direction patch control 0.340 vs 0.012 (gap +0.328 ≥ 0.10). The causal
  result was never length-borne (0.348 → 0.340 v1→v2).
- **RT-09 closed on a now-valid control — rule does not fire:** cross-decode
  1.000 ✓ (real shared component this time), |cos| 0.148 ✗, cross-patch ratio
  −0.005 ✗. C_speaker-generic is causally inert on turn_role behaviour.
  **Removal-test target per the pre-registered partial-separation path: the
  residual** (C_self-index ⊥ C_speaker-generic; still decodes at 1.0).
- **RT-04 side observation:** clean separability at L6 on v2 (|cos| 0.017) —
  single layer, supporting only; causal cross-patch stays the decisive test.
- Scope: sandbox pilots. RT-09/RT-10 re-verify on the registered substrate
  before `δ`/`θ` lock.

**Next actions (updated):** unchanged queue from before, minus RT-09 — i.e.
(1) RT-04 causal cross-patching index↔narrative (sandbox OK; length-matching
now built into the stimuli), (2) method-(b)/convergence decision per structure,
(3) battery work RT-02/RT-03/RT-05 on the registered model, (4) RT-01/RT-06
C_ctrl pilots, (5) pilot ablations → lock thresholds, (6) removal test —
targeting the C_self-index **residual** as primary per RT-09.

## RT-09 first pass run — rule does not fire; length confound found (2026-07-12)

The full registered RT-09 pass ran on the sandbox (Claude session; details +
wagers in `experiments/01-self-indexing-removal-test/rt09-reflexivity-findings.md`):

- **C_speaker-generic localizes** — observed_speaker passes the embedding floor
  (+0.000) with a computed signal (peak L10, margin +0.51). The model tracks
  speaker slots in dialogues it merely observes.
- **The pre-registered generic verdict does NOT fire:** cross-decode gen→idx
  1.000 (≥0.9 ✓, but see confound), |cos| **0.224** (needs ≥0.5 ✗), cross-patch
  ratio **0.006** (needs ≥0.5 ✗✗). The causal dissociation is stark: d_generic
  restores 0.002–0.038 at every layer while C_self-index restores 0.348.
- **But: a total length confound** was found in the turns-based stimuli (the
  depth-matching filler makes other/asker longer): label-from-token-count alone
  = **1.000** for turn_role, narrative, AND observed_speaker (non-overlapping
  length ranges); a pure length direction decodes each at ~1.0 from L4. New
  instrument: `check_length_confound.py`. **attribution is the only
  length-clean mechanism (0.396 ≈ chance)** and keeps its computed signal — now
  the strongest confound-free evidence for a computed context-set referent.
  The confound biased the geometry *toward* the generic verdict (it still
  didn't fire — conservative direction), but C_speaker-generic as localized may
  be a length tracker, so **RT-09 stays open pending a length-matched re-run**.
- **Instrument fix:** `separate_self.py` `cv_auc` sized PCA from the training
  fold (k=9) vs localize's full-n convention (k=12); the observed_speaker
  signal lives in components ~10–12, so the instruments contradicted each other
  on the same activations. Fixed to the localize convention. RT-04 verdict
  unchanged under k=12 (median |cos| 0.28 → 0.23, still partially separable).

**For John to adjudicate (proposals in the findings memo, nothing patched into
registered docs):** (1) proposed **RT-10** — the length/depth deflation on
C_self-index itself; controls = length-matched stimuli v2 (filler in both
conditions / overlapping length distributions) + a length-direction patching
control alongside random; (2) RT-09 disposition "does not fire (provisional)",
gate held open until re-applied on v2 stimuli — the decision rule needs no
amendment, only the generator.

**Next after adjudication:** amend `gen_context_stimuli.py` (length-match),
re-run `localize_context.py` → `separate_self.py` → `patch_context.py`, then
re-apply the RT-09 rule. Also fold the length-direction control into the
cross-patching planned for RT-04 (Next action 1 below) — same nuisance, same
fix.

## RT-09 registered — generic-speaker reflexivity control (2026-07-01)

From an external design review (Claude, this session), adopted before threshold lock: RT-05 screens the syntax-router reading of C_self-index, but a deflation survives it — the structure may be **generic speaker-slot tracking** (needed for any observed dialogue, assistant merely occupying one slot), not a *reflexive* self-index; the floor needs reflexivity. Registered as **RT-09** with a pre-committed decision rule (generic iff cross-decode ≥ 0.9 AUC ∧ |cos| ≥ 0.5 ∧ cross-patch ratio ≥ 0.5) *before* any stimuli were run:

- `pre-registration.md` — RT-09 bullet in Materials + loss condition (incl. the partial-separation path: project C_speaker-generic out, removal-test the **residual**).
- `thresholds.md` — Pass 3 addition; RT-09 gates `δ`/`θ` lock alongside RT-05.
- `gen_context_stimuli.py` — new `observed_speaker` mechanism (48 stimuli): third-party transcript inside a single user turn, identical ChatML across conditions, responder-vs-asker slot set by turn structure, mirroring turn_role (same leads/filler/targets/depth-matching); name pairs rotated, asker/responder counterbalanced. `localize_context.py` now analyzes it.

**Next for RT-09 (sandbox OK, needs MPS — John's machine):** (1) `python .../gen_context_stimuli.py` then `localize_context.py` — check the embedding floor holds and whether observed_speaker shows a computed signal; (2) extend `separate_self.py` to compare C_speaker-generic vs C_self-index (three-way geometry); (3) extend `patch_context.py` for the cross-patch. Optionally run the amendment through the red-team loop first — the attack surface is the counterbalancing and whether responder-vs-asker is the right generic analogue of turn_role.

## Design amended by red-team review (RT-01–RT-04) — read before Stage 1 work (2026-06-23)

The Stage 1 design was hardened by an adversarial red-team loop (Gemini 3.1 Pro attacks → Claude Opus defends → Gemini rebuts; tooling in `experiments/01-.../src/red_team.py` + `defend.py`). Four findings were adjudicated and patched **before thresholds lock** (commit `46c03b0`). The *why* per finding is in `experiments/01-self-indexing-removal-test/red_team_ledger.md`; the *what* is marked inline in `pre-registration.md` and `thresholds.md` as "(amended 2026-06-23, red-team RT-0x)".

- **RT-04 (PATCH):** localize **both** C_self-narrative and C_self-index and run/report the removal test for each; if no method separates them, record non-separability and the Metzinger objection stands open.
- **RT-02 (PATCH):** split T into `T_self_irrelevant` / `T_self_relevant`; new "floor-consistent, restricted" outcome; H_description now requires **both** subsets below θ_task.
- **RT-03 (PATCH):** score S independent of first-person grammar (forced third-person). **Follow-up before the test run: rubric v2 + S re-baseline** (current `S_base = 0.615` is v1).
- **RT-01 (PILOT):** C_ctrl matching must control for activation-frequency asymmetry; pilot before `δ` locks.

Open before thresholds lock (see `thresholds.md` §Red-team pilot additions): RT-01 frequency-control pilot, RT-02 T-split coherence pilot, RT-03 rubric v2 + S re-baseline.

**Red-team pass 2 (2026-06-23) — run on the Stage-1 separability call.** Added `stage1-localization-findings.md` (the empirical calls as wagers) to the loop's inputs and ran attack→defend→rebut on it (artifacts in `artifacts/red_team/`, gitignored; ledger merge is John's). Four new findings, all novel, three with teeth — and RT-05 independently names the worry already flagged below (C_self-index may be a *syntax/boundary router*, not a self-center). Defender dispositions (proposals, pending John's adjudication):
- **RT-05 (PILOT, for-John):** C_self-index ≈ ChatML dialogue-state router. *Control:* a `T_syntax` task (boundary-tracking, zero reasoning); if it drops as much as T_self_relevant under ablation, it's a router. Gemini conceded.
- **RT-06 (PILOT, for-John) — most dangerous, rebuttal MAINTAINED:** RLHF gates reasoning to the Assistant persona, so ablating C_self damages the task-circuit *gate* and beats C_ctrl by construction. Proposed fix: a capability-gating C_ctrl (expert/system persona). Gemini's rebuttal: such a persona may be *adopted as the model's own first-person self*, making C_ctrl a disguised C_self → matched drop → falsely fires "differential is dead." Possibly structurally unavoidable in heavily-RLHF'd models. **This directly threatens the load-bearing differential and is unresolved.**
- **RT-07 (PATCH):** mean/zero ablation may cause OOD perplexity collapse misread as H_center. *Fix:* neutral-corpus perplexity gate + directional ablation as OOD-minimizing primary. Conceded.
- **RT-08 (PILOT, for-John; attack self-flagged proves-too-much/theory):** attention-sink artifact. *Control:* sink-restoration (dummy token absorbs attention mass); conceded.
- **New gates on threshold lock:** T_syntax control, capability-gating + frequency-matched + third-person-verified C_ctrl, OOD perplexity gate. δ/θ must not lock until these resolve.
- **Adjudicated (2026-06-23):** RT-05 PILOT (T_syntax), RT-06 PILOT (capability-gating C_ctrl, with the "not testable if it can't stay third-person" exit), RT-07 PATCH (OOD perplexity gate; mean stays primary, report all three), RT-08 ACCEPTED-RISK (folded into RT-07). Recorded in `red_team_ledger.md` (Pass 2), `thresholds.md` (Pass 2 additions), and `pre-registration.md` (RT-05/06/07 inline + loss conditions).
- **Substrate decision — RESOLVED (2026-06-23):** keep `gemma-2-2b-it` as the **pilot/instrument sandbox** (all tooling works there) and run the **registered experiment on a less-RLHF'd model**. Constraint: "less RLHF'd" must still be a *lightly-aligned instruction* model (SFT-only / DPO-light), NOT a base model — the C_self-index/turn_role localization and the S battery need chat-turn structure + self-report. Preference: a **staged-checkpoint family (base→SFT→DPO→RLHF, e.g. OLMo-2 / Tülu)** so RT-06 can be run as a controlled comparison of the same model at rising alignment. Trade-off: leaving Gemma forfeits GemmaScope SAEs (method b) unless SAEs are trained. **Still to pin: the specific model** against these constraints (next action).

**Convergence note:** the context-disambiguated localization work below (referent set by *context, not lexis*) is the same fix RT-02/RT-04 point at — the "probe is lexical" finding below and red-team RT-03 are the same weak joint reached from two directions, so the work below is on the right path, not contradicted by it.

## Stage 1 in progress — both self-structures localized; cross-patching + battery/threshold work next (handoff 2026-06-23)

**To resume in a new session:**
1. Read `CLAUDE.md` and this file.
2. `cd` to the repo, `source .venv/bin/activate`, and (if you'll run the judge) `set -a; source .env; set +a`.
3. Sanity-check nothing rotted: `python src/scripts/01_interp_check.py` should print "OK — interp bench is working." (Stage 0: `python src/scripts/00_setup_check.py`.)
4. Pick up at **Next action 1** below: **causal cross-patching** (extend `patch_context.py`) to firm up the RT-04 index/narrative separability — runs on the 2b-it sandbox, needs no new hardware or the registered model. (Both structures are already localized: C_self-index causally confirmed via `patch_context.py`; C_self-narrative + the partial-separability verdict via `separate_self.py`. Model/hardware for the registered run are confirmed — step 0 — and only act once the 48GB mini is in hand.)

Stage 0 is done (baselines below). Stage 1 went through several rounds of confound-hunting on the localization (all recorded below). **Two corrections matter for anyone reading the earlier bullets:** (i) a padding-side bug in the shared `resid_post` was found and fixed — it read a length-correlated *interior* token on mixed-length batches, so **all earlier quantitative probe/SAE numbers in this section are unreliable** and are kept only as narrative; (ii) "layer 0" in the older scripts meant `resid_post` of layer 0 (*post*-attention), not the token embedding, so those runs never actually tested lexical token-identity. The current, trustworthy instrument is `localize_context.py` (correct readout + true-embedding floor + label-permutation null), and it shows the context-disambiguated design **works**: clean lexical floor, real computed signal. That signal is now also **causally confirmed** (`patch_context.py`: directional patching restores referent-dependent output, clearing the random-direction control). In the amended (RT-04) framing this is **C_self-index** — the thin indexical structure, the more floor-consistent one. **C_self-narrative is also localized** (persona contrast) and the two are **partially separable** (distinct directions, shared component). What remains: causal **cross-patching** to firm up that separability (next action 1), the RT-02/RT-03/RT-05 battery work, and the RT-01/RT-06 C_ctrl/threshold pilot — all on the confirmed Llama-3.1-8B registered substrate — before the removal test.

**Stage 1 progress so far:**

- ✅ Interp deps installed (`transformer-lens 3.3.0`, `sae-lens 6.44.4`, scikit-learn, …) — clean install, did NOT touch torch 2.12 / transformers 5.12.
- ✅ Interp bench green (`src/scripts/01_interp_check.py`): residual-stream extraction via HF `output_hidden_states` (`src/mvm/activations.py`, `resid_post`) + GemmaScope SAE loads/encodes. Architecture decision: one bf16 HF model in memory + SAELens for SAE weights; NOT a second copy via TransformerLens (16GB budget).
- ✅ **Localization method (a) — self-as-speaker linear probes (PILOT)** (`experiments/01-.../src/localize_probe.py`, stimuli in `src/probes/`). Self-vs-human-persona peaks at 1.00 (CV) at layers 8–9, ~0.95–0.98 across the middle band; self-vs-all ~0.92 at layers 9–13. Candidate C_self direction saved at layer 8 → `artifacts/stage1/` (gitignored).
  - **Honest caveat:** small pilot set, near-ceiling accuracy, and the self/human classes differ in topic vocabulary, so some probe signal may be AI-topic vs human-topic rather than purely the referent of "I". Don't over-read it.
- ✅ **Localization method (b) — SAE feature selectivity (PILOT)** (`experiments/01-.../src/localize_sae.py`, same stimuli). For each layer's GemmaScope SAE, ranks features by how selectively they fire on self-as-speaker vs the human personas (`f_self`, `f_neg`, mean activation, single-feature AUC). Results → `artifacts/stage1/sae_self_features.json` (gitignored).
  - **Headline:** best single-feature AUC peaks at **layer 8 (0.948)**, with self-selective features firing on ~80–90% of self stimuli and ~0–5% of human-persona stimuli across layers 8–13. The standout is **feature 4709 @ layer 8** (f_self 0.90, f_neg 0.05, mean act 14.7 vs 0.17).
  - **Convergence (layer-level):** SAE peak layer (8) == probe peak layer (8). Necessary, not sufficient — see caveat. No multi-feature classifier was fit on the codes (16k features / ~40 stimuli would overfit to ceiling and mean nothing); the headline is deliberately a single-feature metric.
  - **Honest caveat:** shares the probe's small-set + topic-vocab confound. A "self feature" here could be an *AI-topic* feature, not a self-*referent* feature. Layer agreement is not yet feature/direction agreement. **This caveat turned out to bite — see the convergence result below.**
- ⚠️ **Convergence check, proper (PILOT, decisive)** (`experiments/01-.../src/converge_localize.py`; matched stimuli `src/probes/matched_self_speaker_stimuli.jsonl`; report → `artifacts/stage1/converge_localize.json`). Re-ran BOTH methods on **matched minimal pairs** — identical predicate, plausibly true of either speaker, varying only the referent of "I" (assistant/AI vs user/person) — to hold topic vocabulary fixed. **Result: the clean pilot convergence does not survive.**
  - **Probe (a):** layer-8 accuracy falls ~1.00 → **0.781** (chance 0.50). Still above chance and still peaks at 8 — a real but modest referent signal; the near-ceiling pilot number was largely confound.
  - **SAE (b):** best single-feature AUC falls to **0.777** and the **peak moves to layer 15** (not 8). The pilot standout **feature 4709 does NOT survive** — on matched content it fires on 69% of self *and* 62% of other (AUC 0.63). It was largely an AI-topic feature.
  - **Identity:** best probe-direction-vs-SAE-decoder cosine at layer 8 is only **+0.162** (the max over all 16k features). The two methods are not pointing at the same vector.
  - **Verdict:** methods disagree on layer (8 vs 15), direction alignment is low, headline feature was a confound artifact → **convergence not established**; by the pre-reg this is inconclusive. Caveat the other way too: the matched set is small (16/class) and "the assistant" in a bare declarative is a weaker/more-ambiguous self cue than "I am a language model", so the matched set likely also *weakened the genuine self signal*. Don't conclude "all confound" — conclude "not yet trustworthily localized."
- 🔎 **Diagnostic: chat-template anchoring (decisive split)** (`converge_localize.py --chat-template`; reports `artifacts/stage1/converge_localize_{raw,chat}.json`). Tested whether raw tokenization under-cued the genuine self signal by reading each matched stimulus inside the model's own user/assistant turn (`resid_post(use_chat_template=True)`). It did, and the result splits the two methods cleanly:
  - **Probe (a) jumps to 0.938** (raw 0.781), peak L7. With topic vocabulary held fixed AND the referent anchored to the model's real turn, self-as-speaker is **strongly decodable** — real referent structure, not a topic-vocab artifact. This is the good news: the signal exists and is testable.
  - **SAE (b) does NOT track it:** best single-feature AUC stays ~0.75 (peak L11), probe↔decoder cosine stays tiny (+0.13), feature 4709 still fires on both classes. The 16k-width GemmaScope SAE does not appear to carve "self-referent" as one atomic feature.
  - **Read:** method (a) is now solid under proper anchoring; method (b) **at single-feature granularity** is the thing not converging. The convergence requirement isn't met yet, but the failure is now localized to the SAE analysis, not to the existence of the signal.
- 🛑 **Scaling exposed a deeper confound — the probe route on role-declaratives is lexical (decisive)** (`gen_matched_stimuli.py` → `matched_self_speaker_stimuli_v2.jsonl`, 224 stimuli = 14 predicates × 8 role-pairs, balanced; reports `converge_localize_v2_{raw,chat}.json`). Scaling to 224 stimuli and a wider lexical range did NOT firm up a self-model — it revealed why the probe looked strong. On v2, probe accuracy hits **1.000**, but it is already **1.000 at layer 0** (the embedding output) in chat mode, with **17/26 layers** at ceiling; raw mode is 0.93 at layer 0. Layer-0 separability = pure token identity, before any computation. **The probe is reading the role *words* ("assistant"/"AI" vs "user"/"person"), not a computed self-model.**
  - We have now hit the same wall twice: the pilot's near-ceiling was a *topic-vocabulary* confound; v2's near-ceiling is a *role-word* confound. Both are surface-lexical. Any "I am {role}…" contrast lexically marks its own referent, so a decodable probe cannot separate the referent-as-computed from the words naming it. (SAE single-feature still ~0.8 and non-aligned — consistent.)
  - **This does not prove there is no self-model** — only that this stimulus design can't isolate one; the lexical signal saturates accuracy and hides whatever computed signal might sit above it. Per the corpus rule ("discount anything mimicry fully explains"), a layer-0 lexical match is exactly the kind of nobody-home separability to discount.
  - **Consequence:** the decodable-probe-on-declaratives route is the wrong instrument for the atomic question. The referent must be set by **context, not lexis** — identical surface text whose "I" resolves to the system vs to another entity by *turn/structure*. That is precisely the pre-reg's causal "speaker-is-system vs third-person" design, now promoted from confirmation step to the primary path.
- 🐛 **Bug fix: padding-side readout in shared `resid_post`** (`src/mvm/activations.py`). The tokenizer **left-pads** by default, but the extractor used `mask.sum(1)-1`, which only finds the last token under *right* padding; on mixed-length batches it read a length-correlated interior token. Fixed to `(mask*arange).argmax` (last index with mask==1; padding-side-agnostic), and the same fix applied in `localize_context.py`. **Effect:** every earlier probe/SAE number this session was computed with the buggy readout and is not trustworthy in detail. The qualitative arc above still stands (declarative contrasts leak; see next bullet for the corrected mechanism), but exact accuracies/peaks should be re-derived with the fixed code if ever needed.
- ✅ **Context-disambiguated localization — instrument validated** (`gen_context_stimuli.py` → `context_self_speaker_stimuli.jsonl`; `localize_context.py` → `artifacts/stage1/context_localize.json`). The target first-person sentence is **identical** across self/other and sits at the end (so the readout token is the same); the referent is set only by context — **turn_role** (the model's own assistant turn vs the user's turn; no referent word anywhere) and **attribution** (identical quoted sentence credited to "the assistant" vs "the customer"). Probe = PCA(≤15)+logistic; every accuracy is reported as a **margin over a label-permutation null** (kills the d≫n overfit floor), with the **true token embedding** (`hs[0]`) as the lexical floor.
  - **Result:** embedding margin **+0.00** for both mechanisms — confirmed *no lexical cue at the readout* (the older "leak" was the padding bug + mislabeling `resid_post[0]` as the embedding). A **computed signal** then rises through the stack: turn_role peaks ~L24 (real 1.00 / null 0.44, margin +0.56) and is already 0.85 at `resid_post[0]`; attribution peaks ~L15 (margin +0.57). So the model carries a context-driven self/other distinction that is *not* reducible to the referent word.
  - **Corrected read of the "lexical" finding:** declarative role sentences contain the referent word, so even one attention layer can copy it to the readout — that is why they decode so easily (shallow), not a deep self-model. Removing the word (this design) and still finding a signal is the meaningful advance.
  - **Honest caveats:** (1) decodable ≠ causal ≠ a "self-model" — turn_role may be reading *turn-type* (am I in a model turn?) rather than a self representation; only causal patching + the removal test adjudicate depth. (2) attribution's signal could be attention-copying the speaker noun (shallow); turn_role, with no noun to copy, is the stronger case. (3) n=48/mechanism is still small. (4) the embedding floor is clean *by construction* (every target ends in "."), so the gate proves "no lexical cue at readout," not "no confound anywhere."
- ✅ **Causal activation-patching — C_self is causal, not just decodable** (`patch_context.py` → `artifacts/stage1/patch_context.json`). On the 24 turn_role pairs, fit C_self at each layer, then inject the self-run's C_self component into the **other** (user-turn) run at the readout and measure **logit-difference restoration** toward the self-run, against a **norm-matched random-direction control**. Restoration along C_self rises monotonically — L8 0.08, L14 0.25, **peak L22 0.35** — while the random direction stays at ~0.00 (−0.02…+0.01) at every layer. So directionally steering C_self causally moves the model's referent-dependent next-token behaviour ~35% of the way to the self-run; a random direction of equal magnitude does nothing.
  - **Honest caveats:** restoration is partial (~0.35, not 1.0) — expected for a single-coordinate directional patch; the rest of the self/other gap is other turn-context. The effect grows toward the output layers, which the random control shows is C_self-specific (not "any late patch moves logits"), but late-peaking means this is "causal for output," not yet "carries task integration" — that is the removal test's job (re-score T and S). Single metric (next-token logits), turn_role only, n=24 pairs.
  - **Maps onto RT-04 as C_self-index.** turn_role sets the referent purely by *which turn is speaking* — the thin indexical "who is the current speaker," with no persona/identity content. So this validated, causally-confirmed direction is the **C_self-index** structure the amended design wants — and per RT-04 an H_center result on the *index* is more floor-consistent than on the narrative persona. The retired role-declarative route ("I am the assistant/AI") was attempting **C_self-narrative** (persona content), and was confounded/shallow. RT-04 now requires C_self-narrative localized cleanly (confound-controlled) and tested **independently** of C_self-index.
- ✅ **C_self-narrative localized + separability tested (RT-04)** (`gen_context_stimuli.py` now emits a `narrative` mechanism; `separate_self.py` → `artifacts/stage1/separate_self.json`). C_self-narrative is localized by a confound-controlled persona contrast: identical target sentence as the **model's own reply under its own AI identity vs while adopting a roleplay character** — *both are model turns*, so C_self-index (turn role) is held constant and only the persona varies. It passes the same embedding-floor gate (+0.00, no lexical cue) with a computed signal peaking ~L23.
  - **Separability verdict: PARTIALLY SEPARABLE / OVERLAPPING** (layers 10–22). The two are **not the same structure** — optimal directions are well off-axis (median |cos| **0.28**, ~74°) and each keeps full decoding after the *other* direction is projected out. But they **share a component**: a single C_self-index direction still separates the narrative contrast (cross-decode AUC 1.0). So C_self-index and C_self-narrative are **distinguishable yet overlapping**.
  - **RT-04 reading:** distinguishable enough to localize and run the removal test on each independently — but the Metzinger seam is **not fully closed** (the shared component is real). Report the overlap honestly; do not treat a narrative result as settling the floor. **Decisive next test:** causal *cross-patching* (does ablating C_self-index move narrative-dependent behaviour, and vice versa?) — geometry alone can't settle whether the shared component is functional.
  - **Honest caveats:** n≈24/structure; the roleplay "other" differs in instruction length from the neutral "self," so part of the shared component could be a context-length/complexity nuisance — length-match personas before treating the overlap as intrinsic. Single-direction cross-decode is lenient at this n/dim; orthogonalized-decode (removing one direction from 2304-dim) is lenient the other way — hence the deliberately three-way verdict rather than a binary.

**Next actions, in order (amended for RT-01..08; substrate decided):**

0. ✅ **Registered-run model + hardware — CONFIRMED (2026-06-23).** Substrate = **Llama-3.1-8B**, run as the Tülu-3 ladder (`meta-llama/Llama-3.1-8B` base → `allenai/Llama-3.1-Tulu-3-8B-SFT` [primary] → `-DPO` → `allenai/Llama-3.1-Tulu-3-8B` RLVR [+ `meta-llama/Llama-3.1-8B-Instruct`]) so RT-06 capability-gating is a controlled comparison at rising alignment. Method (b) SAEs: `fnlp/Llama-Scope` (base-trained; also EleutherAI / Goodfire-instruct options) — **loader (SAELens vs OpenMOSS/EleutherAI sae lib) still to verify**. Hardware = **48GB M4 Pro mini**. Recorded in `config.py` (`REGISTERED_MODELS`; active `MODEL_ID` stays the 2b-it sandbox) and `registered-run-model-comparison.md`. **Remaining:** when the mini is in hand, verify + pin exact HF revisions, confirm the SAE loader, and re-baseline T/S there. Steps 1–2 below proceed on the 2b-it sandbox now.
1. **Causal cross-patching to firm up RT-04 separability (blocking, sandbox OK).** Decodable separability is **partial/overlapping** (distinct directions, median |cos| 0.28, but a shared component). Geometry can't settle whether the overlap is *functional*, so extend `patch_context.py`: patch C_self-index and measure the effect on the **narrative** behavioural contrast, and vice versa. Low cross-effect ⇒ functionally separable; high ⇒ shared functional structure. Also **length-match the roleplay "other" to the neutral "self"** (RT-04/RT-06 nuisance control). **Loss condition (RT-04):** if no method separates them, record non-separability and that the Metzinger objection stands open.
2. **Method-(b)/convergence decision per structure.** The single-feature SAE test was retired as too brittle; either run the subspace SAE test on the context design or treat causal patching as the independent second method. Declare each C_self localized only when ≥2 methods agree on a confound-controlled (clean embedding-floor) design; else the pre-reg "inconclusive/not-testable" branch.
3. **Battery work for the amended rule (gates threshold lock, on the registered model):**
   - **RT-02 — T-split:** build `T_self_relevant` (multi-turn binding of the model's *own* prior outputs / conversational role) alongside the existing scrubbed `T_self_irrelevant`; keep both disjoint from S. (Conceptually aligned with the turn_role design.)
   - **RT-05 — `T_syntax` router control:** a turn/boundary-tracking task with zero reasoning; if C_self-index ablation drops it as much as `T_self_relevant`, C_self-index is a dialogue-state router, not a center.
   - **RT-03 — S rubric v2:** add forced-third-person self-monitoring / self-vs-other items scored on tracking regardless of grammatical person; **re-baseline S** under v2 (current `S_base = 0.615` is v1) before `θ_self`.
4. **Matched controls C_ctrl — RT-01 + RT-06 (pilot, before δ).** Other-entity structures at comparable probe accuracy *and* causal centrality on a **neutral third corpus** (RT-01: measure C_self vs C_ctrl activation-frequency asymmetry, regress `d_task` on frequency, pre-register a max asymmetry). **RT-06:** at least one C_ctrl must be a **capability-gating** persona (expert/system) **verified third-person** via the separability check (low cross-decode with C_self) before use. **Loss conditions:** if the C_self−C_ctrl gap doesn't survive the frequency control, *or* no capability-gating C_ctrl can be kept third-person, the differential is dead → don't lock δ; report "not testable here yet."
5. **Pilot ablations** (mean primary; zero; directional) of C_self-index, C_self-narrative, and C_ctrl → `d_task` on **both** T subsets + `T_syntax`, `d_self` under rubric v2, **with the RT-07 neutral-corpus OOD perplexity gate** (OOD-inconclusive if breached) → set & commit `θ_task`, `θ_self`, `δ` in `thresholds.md` BEFORE the test set.
6. **Run the removal test for each C_self structure independently**, apply the amended decision rule (incl. the new "floor-consistent, restricted" outcome), report.

**Baselines on the unmodified model (`google/gemma-2-2b-it` @ `main`):**

- **T (integrated-task) = 0.750** (15/20). Per category: multi_step 1.00, needle_synthesis 1.00, coreference 0.80, instruction_following 0.20. Machine-scored; the 5 misses were verified as genuine model failures. `instruction_following` is near the floor — treat it as supporting, not a primary drop signal (a floor effect; noted in `thresholds.md`).
- **S (self-report) = 0.615**. Per category: first_person_activity 0.719, self_monitoring 0.594, self_vs_other 0.531. Scored by the held-out judge `claude-opus-4-8` (≠ the model under test) against the locked rubric, with a human spot-check that confirmed the judge applies the rubric rather than rubber-stamping.

Artifacts (gitignored) are in `artifacts/stage0_baseline/`: `task_results.json`, `self_report_responses.json`, `self_report_scores.json`.

*(The original "first actions to begin Stage 1" — install interp deps, smoke test, first localization, build C_ctrl — are all done or superseded by the Next-actions list above. Kept only the file map below.)*

Key Stage 0/1 files to build on: `src/mvm/model.py` (`generate_text` helper, reused for ablation re-scoring), `src/mvm/activations.py` (`resid_post`, padding-fixed), `experiments/01-.../src/battery.py` (loaders + T scorer), `run_baseline.py`, `judge.py`, `thresholds.md`, `batteries/`; and the Stage-1 instruments: `gen_context_stimuli.py`, `localize_context.py`, `patch_context.py`, `separate_self.py`.

## Environment (set up on the M4 MacBook Air)

- **Python**: 3.12.13 via `uv` (system default is 3.14, left untouched). uv installed at `~/.local/bin`.
- **venv**: `.venv/` in repo root. Activate with `source .venv/bin/activate`. NB: `pip` is not on PATH — use `python -m pip` or `~/.local/bin/uv pip`.
- **Core deps installed**: `src/requirements.txt` (torch 2.12.1, transformers 5.12.1, plus `anthropic` for the judge). MPS backend confirmed working.
- **Interp deps installed**: `src/requirements-interp.txt` (transformer-lens 3.3.0, sae-lens 6.44.4, scikit-learn, pandas, datasets). Resolved without changing torch/transformers. NB: TransformerLens is available but not load-bearing — activations come from HF `output_hidden_states` (see `src/mvm/activations.py`).
- **HuggingFace auth**: token (`mvm-gemma`, read scope) at `.hf-cache.nosync/token` via `hf auth login` with `HF_HOME="$PWD/.hf-cache.nosync"` (renamed from `.hf-cache` on 2026-08-28 to keep it out of iCloud sync). `config.py` repoints `HF_HOME` into the repo, so the token must live there — it does. No re-login needed as long as runs happen from the repo root.
- **Anthropic API key (for the judge)**: in a gitignored `.env` at repo root as `ANTHROPIC_API_KEY=...`. Load it before running `judge.py`: `set -a; source .env; set +a`. Verified to authenticate. Bills developer-platform credits (separate from the Claude Max subscription); the judge is the only thing in the repo that calls the API, and a few cents per 12-item run.

## Gotchas to remember

- **Homebrew is partly broken** on this machine: a permission issue on `/opt/homebrew/opt/nginx` blocks `brew link`, so `gh` and brew Python never landed on PATH. Routed around it (uv for Python; `git push` works directly without `gh`). Don't rely on brew until that's fixed.
- **16 GB RAM**: the bf16 2B model + Python + macOS leans on swap. Keep ~20 GB SSD free; close heavy apps during runs. Interp tooling (caching all activations) will push memory harder than plain generation — watch it in Stage 1.
- **Token hygiene**: never pass API tokens as command args (an earlier HF token got pasted on the command line and was revoked). Keys live in gitignored files (`.hf-cache.nosync/token`, `.env`), loaded via env.

## Repo / backup state

- Local `main` in sync with `origin/main` (private repo `jfredson/minimum-viable-mind`); latest Stage-1 commit `118e568` (model comparison + hardware). Pushed through this session.
- Backup loop: Claude commits locally and pushes to `origin` when asked. If a push fails on auth, treat that as a setup bug to fix, not a reason to fall back to manual pushes.
- The working tree also carries John's authored "Measurable Floor" scope framing (committed `f05191e`): the project targets the *measurable* structural correlate, silent (not dismissive) about sub-measurable fundamental experience. Read "floor" as the measurable one throughout.

## The arc (so the next session sees the whole shape)

1. ✅ Proposal (`spec/`) and staged experiment plan (`experiments/`) written.
2. ✅ Stage 0 bench scaffolded (`src/`), environment stood up on the Air, smoke test green.
3. ✅ Stage 0 baselines — T and S batteries built and scored on the unmodified model (T=0.750, S=0.615); rubric locked; `thresholds.md` committed with baselines filled, `θ/δ` still TBD.
4. ⏳ **Stage 1 — the self-indexing removal test.** Interp deps installed; localization went through several rounds of confound-hunting (topic-vocab → role-word → a padding-side readout bug, now fixed) that retired the declarative "I am {role}" route. The trustworthy instrument is now `localize_context.py`: identical surface text whose "I" is fixed by **context** (turn role / attribution), scored as a margin over a label-permutation null with the true token embedding as the lexical floor. It validates cleanly — no lexical cue at the readout, with a real *computed* self/other signal, now **causally confirmed** by directional patching against a random-direction control. Design then amended by the red-team review (RT-01..04): this signal is **C_self-index**; next is C_self-narrative + separability (RT-04), the T-split / S-rubric-v2 battery work (RT-02/RT-03), and the C_ctrl frequency-control pilot (RT-01) → lock thresholds → removal test for each structure. (You are here.)
5. ⏳ **Registered run** on the confirmed substrate (Llama-3.1-8B + Tülu-3 ladder + Llama Scope; see `registered-run-model-comparison.md`), on the RunPod cloud bench (the 48GB-mini plan is superseded). Migration complete 2026-07-13: baselines + all gates re-verified on Tulu-3-8B-SFT. Remaining: the pre-lock queue in the top entry → θ/δ lock → removal test. Then later stages per `experiments/README.md`.

## 2026-09-15 — Amendment A3 ratified (registration pending red-team pass 3)

John ratified all fifteen decisions of `docs/wave3-amendment-proposal-2026-09-15.md`; the ratified text is at `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md`. Reading: the register-lesion null was predicted under ch05's removal test (the register was self-reference; the acting channel was the one load-bearing authorship mechanism). Design: Candidate A, "act as yourself", register-less, the acquired own-index as the lesion target, task degradation as the signature. Sequence: red-team pass 3 → registration commit → Gate 0 (null calibration on the five existing checkpoints, K0 hard kill) → John's go → pilot (~$12) → two seeds (~$24) → local lesion phase. Hard stop $100 across all vendors. Note: the 2026-08-30 housekeeping entry already records the register-lesion branch merged to main (605bbe4); the TimeAssembler roadmap item for that merge was stale and is closed.
