# Wave-3 disposition — options analysis

*Prepared 2026-08-30 by Claude (model: Opus 5, 1M context — `claude-opus-5[1m]`)
at John's request, as one of two independently-run analyses to be read side by
side. **This is analysis, not adjudication.** The wave-3 call is John's; nothing
here is a registered amendment, a verdict on H_load-bearing, or authorization to
spend. Session was read-only: no merges, no file changes but this one, no
compute.*

**Read, in order:** `register-lesion-findings.md` (on
`worktree-register-lesion-diagnostics`, commit `4296ffc`, read in place —
unmerged); `pre-registration.md` v1.0 + A1 + A2 incl. the R1 ceiling addendum
and the run-identity note; `twin-binding-anomaly.md`; `compute-ledger.md`;
`launch-plan-5seed.md`; `spec/corrigibility-commitments.md` v1.1; the branch
diff (lesion + item findings, `fingerprint_gate.py` output-path fix);
`experiments/01-.../theta-delta-lock-memo.md` (threshold-lock precedent); and
the TimeAssembler Minimum Viable Mind worklog, decision entries in full
(2026-08-02 through 2026-08-18) plus the 2026-08-20 diagnostics progress entry.

**Framing.** The memo frames the options as (a) halt the 5-seed remainder and
redirect headroom to a redesigned battery, (b) run the already-registered θ/δ
null calibration first, (c) continue wave 3 as registered. That matches the
framing in the prompt, so I use the memo's wording throughout and flag the one
place where the memo's (a) collides with a binding governance decision.

---

## Part 0 — Seven findings that change the arithmetic before the options are argued

These are load-bearing for all three options, so they go first. Each is marked
**measured** (in the artifacts), **inferred** (a reading I am confident of but
which is not directly in the record), or **derived** (my arithmetic from
committed numbers).

### 0.1 — H_load-bearing is already out of reach under the registered decision rule, on seed count alone. **[measured + derived]**

The registered bin requires the reading to hold "on a pre-committed majority of
seeds (≥ 4/5)" (`pre-registration.md` §Pre-registered metric and decision rule).

- Seed 0's full **is measured to fail it.** The pilot checkpoint was adjudicated
  to *be* the registered seed-0 full run (§Run-identity note, 2026-08-16), and
  thread 4 ran the register lesion on exactly that checkpoint: T_si 0.93 → 0.94,
  T_sr_rev 1.00 → 1.00, and "T_sr / T_state / T_syntax ≥ 0.99 everywhere." So
  `d(T_sr) ≈ 0`, below any positive θ_task. The bin fails on seed 0.
- With seed 0 failing, the bin can reach **at most 4/5**, and only if it holds on
  *all four* of seeds 1, 2, 3, 4.
- Seeds 1 and 2 fulls never learned the binding (endpoint T_si 0.33 / 0.35,
  T_sr_rev 0.00, flat from step 500). The T_sr they do hold (0.95–0.96) is
  localized by the no-act lesion to the **acting channel**, not the register:
  0.96 → 0.16 when the motor copy is zeroed, against an 8-way chance floor of
  0.125. For the bin to hold on them, register ablation would have to degrade a
  capability whose mechanism has already been measured to live somewhere else.

So H_load-bearing now requires a clean 4/4 sweep of the remaining seeds,
including two seeds whose relevant mechanism is already localized off the
register, against a direct null measurement on the one seed that was tested.
**This is not a construct-validity argument — it is the registered decision rule
executing on the data in hand.** It holds regardless of what one thinks of the
lesion diagnostics' epistemic standing, and it is true under all three options.

*Formal gap worth closing, and it is free:* the full four-lesion suite ran on
seed 0 only (`register_lesion_pilot_a1_30m_seed0.json`); seeds 1, 2 and the
twins got only the no-act lesion. Running the register-lesion suite on the s1
and s2 fulls is local, $0, and would convert the inference above into a
measurement.

### 0.2 — The register-utilization gate is where the real verdict lives, and one of its legs has effectively failed. **[measured + inferred]**

The registration is explicit and unusually strict: "**Every bin below is
conditional on the twin gate, the register-utilization gate, and the RT-01
probes having been passed first; a bin reached without them is void.**"

The gate [RT-09] has three legs. Against thread 4:

| leg | registered requirement | evidence in hand | read |
|---|---|---|---|
| attention mass | above a pre-committed per-layer floor | xattn residual norms 18–275 vs 3–14 trunk | likely **pass** (norm ≠ attention mass; not literally the registered measurement) |
| causal path patching | injecting another episode's register content changes **some battery** by a pre-committed margin | removing the injection entirely changes no battery cell (T_si 0.93→0.94); deranging key→content changes none (mean \|Δlogit\| 0.014) | **fail** at any positive margin |
| gradient flow | non-negligible through the write path at end of training | not measured | unknown, cheap to measure |

Leg 2 is inferred rather than measured in the registered form — thread 4 deranged
content *within* an episode and removed the injection outright, rather than
injecting *another episode's* content. But removing the injection entirely is a
strictly stronger perturbation than replacing its contents, and it moved nothing.
A model that does not read the channel informatively will not read foreign
contents informatively either.

**The consequence is the most important thing the memo understates.** If the
utilization gate fails, the registered landing spot is not H_routed-around — the
outcome the registration calls "the outcome worth having," which carries the
upstream reporting obligation to the philosophy repos. H_routed-around
*requires the utilization gate to have passed*. The landing spot is
**"Construction failure (register unused)" [RT-09]**, whose registered
consequence is stated verbatim: "nothing goes upstream; this is a training bug,
not evidence about selves."

That is a much thinner result than the memo's framing implies, and it is the
same result under (a), (b), or (c). The disposition does not change it; only the
registered analysis phase can adjudicate it.

### 0.3 — The one live garden-of-forking-paths hazard, with an incentive attached. **[derived]**

Two thresholds that decide the outcome are **unset**: the utilization gate's
per-layer attention-mass floor and its path-patching margin. The data that
determines which side of them the result falls on is **already known**.

And there is a real incentive on the choice: H_routed-around is substantive,
publishable, and discharges upstream; Construction failure is a training bug
that goes nowhere. A generous attention-mass floor plus a lenient patching
margin is the difference between them.

This is the sharpest procedural hazard in the whole decision and **neither the
memo nor the anomaly note names it.** Whichever option is chosen, those two
numbers should be committed in a script, with their derivation, before they are
run — following the Experiment 1 precedent exactly
(`theta-delta-lock-memo.md`: derive from the measured null band under
interventions that should not move behaviour, propose candidates in a memo, lock
in a separate commit that is John's alone).

### 0.4 — The θ/δ lock may already be void, and the contamination is directionally benign — except at 0.3. **[derived]**

Registered: "θ_task and δ are null-calibrated on the registered model ...
computed by a script committed before it runs. Pilot runs may verify battery
ceiling and nothing else; **any pilot ablation result read before threshold lock
voids the lock.**"

Thread 4 read register-ablation results on the checkpoint that *is* the
registered seed-0 full, before any lock. No calibration script exists in
`experiments/06-.../src/` (verified: the directory holds cue_detector,
curriculum, encoding, fingerprint_gate, model, train, and the launcher/watch
scripts; the branch adds only the lesion/item tools).

Two readings, and they differ in name more than in effect:

- **Narrow:** the clause governs *pilot* runs; the run-identity note converted
  this checkpoint into a registered run, so the clause does not literally fire.
  But then the ablation was run at registered procedure **step 7 before steps 5
  and 6**, which is its own out-of-order problem.
- **Spirit:** the anti-fitting purpose fires either way. Whoever sets θ now knows
  `d ≈ 0`.

**The saving grace, which must be stated plainly in any write-up because a reader
will otherwise assume the usual direction: the contamination is one-directional
and self-harming.** Knowing `d ≈ 0` means H_load-bearing is unreachable at *any*
positive θ. A post-hoc θ cannot manufacture a positive here; it can only
foreclose one. The remaining researcher degrees of freedom on θ/δ can only make
the result worse for the registered prediction. That is an unusually clean
epistemic position.

The exception is 0.3: the utilization-gate thresholds are *not* directionally
benign, because they choose between two failure bins of very different value.
θ/δ are safe to set late; the gate margins are not.

### 0.5 — The memo's "7 runs ≈ $130" is stale by one wave. The true remainder is 5 runs ≈ $65–80. **[derived]**

The run-identity note fixes 9 remaining launches after the pilot. Wave 1 took two
(s0 twin, s1 full); wave 2 took two (s1 twin, s2 full). **Five remain:** s2 twin,
s3 full, s3 twin, s4 full, s4 twin — exactly waves 3, 4 and 5 of
`launch-plan-5seed.md`. "7 runs" was correct on 2026-08-17 and was carried
forward into the 08-18 anomaly note and then into the 08-19 findings memo without
being re-derived.

Costed at measured wave-1/wave-2 rates ($0.99/hr, RTX 5090 SECURE EU-RO-1):

| item | measured basis | cost |
|---|---|---|
| 3 twins | 10.29 h / 10.16 h actual → ~10.2 h each | ~$30.3 |
| 2 fulls | 15.19 h / 15.39 h train actual → ~15.3 h each | ~$30.3 |
| volume drip, ~5 days | `mvm-models-ro` ~$7/mo | ~$1–3 |
| one crash-resume margin | A2's own margin line | ~$15 |
| lid-close idle, if it recurs | ~$5.7 observed in wave 2 | $0–17 |

**Expected ~$65–80; worst case ~$95.** Roughly *half* the memo's figure. This
cuts against halting and in favour of continuing, and it belongs on the record
for exactly that reason.

### 0.6 — The 2026-08-15 blind scope-freeze already answers option (a)'s money question, and not the way the memo assumes. **[measured]**

The memo's (a) is "halt the 5-seed remainder and treat the ~$219 A2 headroom as
available for a redesigned battery."

The binding decision (TimeAssembler worklog, 2026-08-15, taken deliberately
blind; ratified as R1 on 2026-08-16 and recorded in `pre-registration.md`
§Ceiling adjudication addendum) says:

> Exactly one amendment to the $200 compute cap is permitted for MVM-0a. Its
> scope is frozen as of today to the two already-registered runs: the 5-seed run
> [and] repeated-sampling... **Nothing discovered in the 30M result can widen
> that scope. If the result suggests a third experiment, that experiment belongs
> to a new pre-registration with its own gates and its own cap, not to an
> expansion of this one.**

A battery redesigned so that ownership is the only disambiguator is a third
experiment. **Option (a) as worded is unregistrable under the standing rule.**
The A2 headroom is not available for it. R1 anticipated precisely this move and
called re-opening the number "the exact ratchet the blind rule exists to kill."

Two distinctions the memo blurs, both of which matter:

1. **The single-amendment ceiling constrains money, not design.** The blind rule
   is explicitly "one amendment to the *compute cap*." Design amendments that
   cost nothing remain permissible and are in fact required ("any change to the
   registered plan is itself a registered amendment"). So **fixing** the T_si
   repeated-item defect and rescoring the five checkpoints in hand is
   registrable today, at $0. **Redesigning** the battery in a way that needs new
   training runs is not, under A2.
2. **A redesign need not need new training.** A battery where every queried item
   is assigned by multiple agents is an eval-time construct generated from the
   same grammar; the five checkpoints are local and enact their own turns at eval
   (`train.py:172`). Scoring a redesigned battery on the existing checkpoints is
   plausibly $0 — subject to a real caveat, that the training curriculum may not
   contain such items, so a floor score would be ambiguous between "cannot bind"
   and "never saw this distribution." This variant sits inside none of the three
   options as framed and is worth naming.

### 0.7 — Halting is the difference between repeated-sampling running and not running. **[derived]**

Per R1, repeated-sampling (capitulation@k, registered 2026-08-04b, plus judge
validation) "is funded **only** by GPU-side underspend... If it does not fit, it
goes unrun under this cap and the publication states what was not run and why."

Position: ~$181.4 spent of $400; account balance $142.64; headroom ~$218.6.
Registered analysis phase (gate re-runs, ablation passes, RT-01 probes, θ/δ,
blind-localization) budgeted at $30–45 in A2 — though thread 3/4 demonstrate this
class of work runs **locally at $0**, so $0–20 is the realistic figure.

| path | projected total | headroom left for repeated-sampling |
|---|---|---|
| continue waves 3–5 (~$70) + analysis (~$30) | ~$281 | ~$119 |
| halt, analysis only (~$30) | ~$211 | ~$189 |

Against a repeated-sampling estimate R1 records as "~low hundreds," ~$119 is
probably short and ~$189 is plausibly enough. **So the money freed by halting has
a concrete, in-scope, already-registered claimant — and it is not a redesigned
battery.** This is a genuine argument for (a) that the memo does not make, and it
survives 0.6 because repeated-sampling is inside the frozen scope.

Two notes: neither path requires a RunPod top-up on its own (balance covers
either), so top-up pressure arises only if repeated-sampling runs; and RunPod
ticket #45404 ($17.82, drafted-not-sent on `worktree-runpod-ticket-reply`) would
reduce net spend if recovered.

### 0.8 — An item orthogonal to the whole decision: the blind-localization arm's ground truth has evaporated, and it is now worth *more*. **[derived]**

The arm is registered **unconditional** ("runs on the same trained seeds
regardless of which bin the headline reaches"), with a verdict-first firewall,
and the registration says it "may outweigh the headline." Its registered
question: can the instruments "recover a center known-by-construction to exist
and to be load-bearing"?

Thread 4 destroys the premise. There is no such center — the register is
numerically active and informationally inert. The arm cannot be the ground-truth
test it was registered as.

But it converts into something sharper for Q1: **a false-positive calibration.**
Do Experiment 1's localization instruments report a center at the register's
location when the register demonstrably carries no agent-specific information and
no battery depends on it? If they do, that is direct evidence that Experiment 1's
positive localizations were instrument artifacts — which bears on Q1 (and on the
`instruments-that-can-lose` write-up) far more sharply than the registered
version would have. Re-aiming the arm is itself an amendment and a forking path,
and should be recorded as one.

**None of the three options mentions this arm.** It is registered, unconditional,
cheap, and independent of the wave-3 call. It should proceed under any
disposition.

---

## Option (a) — Halt the 5-seed remainder; redesign the batteries

### What the register-lesion result licenses for this option

**Licenses:** that the instrument does not measure what it was registered to
measure. Thread 4's pre-stated branch fired ("if the pilot's binding survives the
lesion, then even the one clean success was never register-dependent and the
construct problem is total") — and it fired on the pre-stated *decisive* test,
against a harness validated by bit-for-bit reproduction of the committed endpoint
row, replicated on a disjoint eval seed, with the null checked against the
alternative that the pathway is dead (it is not: |Δlogit| mean 0.22, max 5.2).
That is about as clean as a null gets. Combined with thread 3, it licenses the
specific diagnosis that the batteries decompose into unique-item lookup (everyone
solves it), marker-keyed retrieval (a seed lottery, register irrelevant), and
revised-item recency — with ownership load-bearing in exactly one place, the
acting channel, which the twin also has.

**Does not license:** the claim that a *better* battery exists. Nothing in the
diagnostics shows that a battery where ownership is the only disambiguator is
learnable at 30M under this curriculum — and RT-17's trilemma (worklog,
2026-08-09: "own-ness is not learnable from exchangeable data in a token-only
interface") is precisely the wall such a battery would run into. It also does not
license spending A2 money on the replacement (0.6). And it does not license the
inference that seeds 3–4 would have been uninformative *about anything*; it
licenses that they are uninformative about **H_load-bearing** specifically.

### Strongest case for

1. **Halting is the registration executing, not a deviation from it.** This is
   the argument that does the real work. The registration says a bin reached
   without the utilization gate is *void*; it defines a "Construction failure"
   bin whose consequence is that nothing goes upstream; and it carries explicit
   loss conditions that retire the experiment. Stopping because a validity gate
   has failed is the pre-registered machinery operating as designed. "We stopped
   when the gate failed" is not the mirror image of "we kept going until we liked
   it" — it is what gates are for.
2. **The registered positive is arithmetically foreclosed (0.1).** Continuing
   cannot reach it under any outcome. Spending to complete a design whose
   headline bin its own decision rule has already ruled out needs a justification
   other than evidence.
3. **The freed money has an in-scope claimant that will otherwise go unfunded
   (0.7).** Repeated-sampling is registered, has an external audience via the
   Stage 3 write-up, and is currently projected not to fit. Halting roughly
   doubles its headroom.
4. **The calendar.** Today is 2026-08-30. Calibration has first claim on writing
   hours through September (worklog, 2026-08-15); W37 is a verification-only
   review on Sep 13; SERE pipeline starts Jan 4 2027. Waves 3–5 are ~5 days of
   lid-open, watchdog-babysat calendar with a demonstrated ~$5.7/wave idle leak,
   for a rate estimate. The write-ups cost no compute and have the audience.
5. **The finding is already the deliverable.** The project's own public
   tradition — `drafts/instruments-that-can-lose.md` — is built to carry exactly
   this: a registered instrument that lost honestly, diagnosed to the mechanism.
   That essay is stronger with a decisive $0 diagnosis than with five more seeds
   of the same.

### Strongest case against

1. **Option (a) as the memo words it cannot be registered (0.6).** The money half
   is blocked by a decision John made *blind*, precisely to stop results from
   widening scope. Adopting (a) in its stated form would be the ratchet R1
   refused. (a) survives only in the reduced form "halt, and let the underspend
   flow to repeated-sampling" — which is a different decision and should be
   named as one.
2. **It halts on unadjudicated evidence.** The findings memo's own status line:
   "diagnostic record, not adjudicated — nothing here is a registered result."
   Killing a registered run mid-flight on the strength of an unregistered
   diagnostic inverts the epistemic hierarchy the registration exists to
   protect. The rebuttal in (a)'s favour is real (point 1 above), but it depends
   on the utilization gate having *actually* failed — which has not been formally
   run (0.2).
3. **The redesign may not exist.** RT-17 closed the question of whether ownership
   is learnable from exchangeable data in a token-only interface: only leakily.
   A battery forcing ownership to be the sole disambiguator may be exactly the
   thing that experiment proved unbuildable. Halting a running design for a
   replacement that may not survive its own red-team leaves the program with
   three fulls and nothing else.
4. **Sunk-cost asymmetry runs the other way here.** ~$181 and the whole 5-seed
   apparatus are spent; the remainder is ~$70, about one-third of a wave-2. The
   marginal cost of completing is small relative to what completion buys in
   procedural standing.

### Costs

- **Money:** saves ~$65–80. Frees ~$189 headroom, but *only* for repeated-sampling
  and the registered analysis phase — not for a redesign (0.6). A redesign needs a
  new pre-registration with its own cap, i.e. new money and a new red-team pass.
- **Time:** saves ~5 days of run-babysitting; costs a full registration cycle
  (draft, red-team, adjudication) before any redesigned battery can be run —
  realistically weeks, in a window where Calibration has priority.
- **Statistical validity:** *this is where (a) is strongest and weakest at once.*
  Strongest: it avoids spending on an instrument with a documented construct
  failure, and the decision rests on a pre-stated branch, which is the opposite
  of a forking path. Weakest: stopping early on unregistered evidence is itself a
  researcher degree of freedom, and a hostile reader will note that the run was
  stopped after the result disappointed. The defence must be that the *stopping
  rule invoked is a registered one* (validity gate failure), which requires
  actually running the gate first — i.e. it requires (b) to have happened.
- **Evidentiary value:** an unregistered change to the plan does not damage the
  *diagnostic* findings, which stand on their own as measurements. It damages the
  claim that MVM-0a completed as registered — which matters for the Nature-track
  write-up, where "we ran the registered design to completion and it lost" is a
  materially stronger sentence than "we ran 60% of it and stopped."

### What would later prove this choice wrong

- A seed-3 or seed-4 full binds **and** its binding is register-dependent under
  the lesion. This is the one outcome that retroactively vindicates continuing,
  and it would directly contradict thread 4's "total" claim. Only running them
  finds out.
- The $0 rescore of the T_si repeated-item defect materially changes the
  binder/non-binder picture — i.e. the instrument was less broken than thread 3
  concluded, and its "defect" was mostly a scoring artifact that a fix repairs.
- The redesigned battery proves unlearnable at 30M, or fails its own red-team on
  the RT-17 wall. Then the halt bought nothing and cost the completed run.
- The utilization gate, run properly, *passes* — putting H_routed-around (with
  its upstream obligation and its seed-reliability requirement) back on the
  table, at which point more seeds mattered after all.

---

## Option (b) — Run the registered θ/δ null calibration first

### What the register-lesion result licenses for this option

**Licenses:** that the noise floor is now the binding unknown for every remaining
reading. Seed-2's late wander (0.26 → 0.43 → 0.31 → 0.35 at n=100) is very likely
inside it; the anomaly note says as much. It also licenses treating the registered
*analysis* phase as the live work — the checkpoints are in hand, the questions
they can answer are cheap, and none of them needs new training.

**Does not license:** the belief that θ_task itself will change any headline. With
`d ≈ 0` measured, no value of θ > 0 alters the H_load-bearing reading (0.1, 0.4).
If (b) is read narrowly as "compute θ and δ, then re-decide," it is close to
procedure theatre: it formalizes a threshold that cannot bind. **The result does
not license the narrow reading of (b); it licenses the wide one** — that the
θ/δ calibration is the *entry point* to the registered analysis stack (registered
ablation operator set + dynamics-matched control, RT-01 probes, utilization gate,
blind-localization arm), which is where the actual adjudicable verdict is.

### Strongest case for

1. **It is the only option that requires no amendment at all.** θ/δ calibration is
   registered, funded, unspent, and sequenced *before* the registered ablation
   run (procedure steps 5–7). Running it is executing the plan. (a) and (c) both
   require John to make a disposition ruling first; (b) does not.
2. **It resolves the question that determines whether wave 3 has any purchase.**
   The bin turns on the utilization gate (0.2). If the gate fails → Construction
   failure → more seeds of a failed construction are worthless, and halting
   becomes the *registered consequence* rather than a judgement call, which is
   exactly the defence (a) needs and does not currently have. If the gate passes
   → H_routed-around is live, and that bin's own reliability clause makes seeds
   matter again, which is exactly the justification (c) needs and does not
   currently have. **(b) is the option that converts the other two from
   judgement calls into consequences.**
3. **It is nearly free.** The memo prices it at ~$2–5 from the A2 phase guide, but
   threads 3 and 4 — which are heavier work — ran locally at **$0**. A null
   calibration is many matched-strength random-subspace and matched-norm
   ablations, each with a battery eval; the item sweep already did n=400 evals
   across five checkpoints on this machine. Expect $0 and hours-to-days of local
   Mac time.
4. **It preserves every option.** Nothing is foreclosed. The five remaining runs
   stay launchable; the redesign stays proposable; ~$219 headroom is untouched.
5. **It is the moment to lock the one dangerous threshold (0.3), while the choice
   can still be documented as principled** rather than as reverse-engineered from
   a bin preference.

### Strongest case against

1. **It can be a way of not deciding.** John's call is the wave-3 disposition; (b)
   defers it by a cycle. If the answer to "does the gate pass?" is as predictable
   as 0.2 suggests, the deferral buys process, not information — and process that
   postpones a decision has a cost the memo does not price.
2. **The lock it produces may not be trustworthy (0.4).** If the θ/δ lock is
   already void by the pre-registration's own clause, (b) delivers a threshold a
   careful reader will discount. Paying for a lock nobody trusts is worse than
   not locking, because it invites the accusation of procedural theatre.
3. **The calibration's own construct problem.** θ/δ are defined over `d(B)`,
   chance-corrected battery drop. Thread 3 shows the batteries are compounds of
   distinguishable sub-tasks with at least one ill-posed cell. A noise floor
   computed over a compound whose components are known to be heterogeneous is a
   number of uncertain meaning. Calibrating an instrument you have just
   diagnosed as mis-specified is defensible only if you also fix the
   specification — which points at doing the T_si item fix *first*, at $0.
4. **Sequencing risk on the runs.** RunPod 5090 SECURE stock has already been
   flaky (wave 1's per-DC sweep, wave 2's failed create). Deferring waves 3–5 by
   weeks is a small but real risk to the ability to complete them on the
   registered venue at the registered price.

### Costs

- **Money:** ~$0 realistically, ~$2–5 at the ledger's registered estimate.
  Against the $400 ceiling: negligible either way, and it is inside frozen scope.
- **Time:** days, not weeks. Requires writing and committing a calibration script
  *before* running it (the registration's explicit requirement), plus — if the
  wide reading is taken — the utilization-gate thresholds and the registered
  ablation operator set. Realistically one to two working sessions.
- **Statistical validity:** the *best* of the three, with one asterisk. It runs
  the registered procedure in the registered order, and it is the only option
  that closes the 0.3 forking path before the data can steer it. The asterisk is
  0.4: the lock's standing is contestable no matter how carefully it is done, and
  honesty requires the write-up to say the lock was set after ablation results
  were read, with the direction of the contamination stated (it can only
  disfavour the registered prediction).
- **Evidentiary value:** highest per dollar of the three. It is what turns a
  "diagnostic record, not adjudicated" into a registered, adjudicated bin — the
  difference between a finding in a repo and a result in a paper.

### What would later prove this choice wrong

- The calibration returns a noise floor so wide that nothing in the 30M record
  is distinguishable from noise — including the binder/non-binder split itself.
  That would retroactively make the n=100 evals the story and would mean the
  whole seed-lottery reading (and thread 3's phenotypes) was over-read. *This is
  a genuine possibility and would be a significant, if deflating, finding.*
- John rules the lock irrecoverably void, in which case (b) produced a number
  that cannot be cited and the sessions were spent for nothing citable.
- The gate outcome turns out not to change John's disposition — i.e. he would
  halt on a pass and halt on a fail. Then (b) was a delay dressed as a decision
  procedure, and the honest move was to rule directly.
- Waves 3–5 become unrunnable at the registered venue/price during the delay,
  converting a deferral into a de facto halt that was never adjudicated.

---

## Option (c) — Continue wave 3 as registered

### What the register-lesion result licenses for this option

**Licenses:** almost nothing about H_load-bearing — the memo is right that no
split of binders and non-binders bears on it, and 0.1 shows the decision rule had
already foreclosed the bin independently. But it does **not** license the stronger
claim that wave 3 is *informationally empty*. Two registered readings remain live:

- **The seed-dependence rate.** The registered "Seed-dependent" bin has a
  pre-stated headline: "centralization of self-binding is not a reliable property
  of this architecture + curriculum." Thread 3 refines what varies (general
  marker-keyed retrieval, a lottery won by 2 of 5 runs so far) but does not
  measure the rate any better. Wave 3–5 takes the sample from 5 runs to 10.
- **The architecture-independence of the lottery.** Currently fulls 1/3, twins
  1/2. Completing gives 5 and 5. If the retrieval lottery is truly
  architecture-independent, that is a cleaner claim with 5+5 than with 3+2.

**Does not license:** treating those as worth $70. See below — the precision gain
is small.

### Strongest case for

1. **Pre-committed-procedure completion is a real defence, and the memo concedes
   it while framing it as thin.** Pre-registration's value comes from the fact
   that the plan is executed whether or not the executor likes the interim
   results. A program that has now amended its scale (A2), its curriculum (A1),
   and would amend its stopping point on the basis of an unadjudicated diagnostic
   is a program whose registrations do progressively less work. "We completed
   what we registered" is a sentence with cumulative value across the whole
   MVM/Experiment-1 program, not just this experiment.
2. **It is cheap — about half what the memo says (0.5).** ~$65–80 of ~$219
   headroom. On the corrected number, the "is this worth it" question is much
   closer than the memo's framing makes it look. This is the strongest new fact
   in favour of (c) and it must not be buried.
3. **The interim reads have already surprised twice.** Wave 1 produced the first
   non-binding full; wave 2 inverted the design's central prediction. This
   curriculum + architecture has a demonstrated capacity to produce outcomes
   nobody predicted. The prior that seeds 3–4 are "more of the same" is exactly
   the prior that has been wrong twice in a row on this run. That is a real
   argument, and it is the best one (c) has.
4. **It is the only option under which the single vindicating outcome is
   reachable.** If a seed-3/4 full binds *and* the binding is register-dependent,
   thread 4's "total" claim falls. Halting makes that permanently unknowable.
5. **Optics of stopping.** Stopping a registered run immediately after a
   disappointing interim result is the pattern reviewers are trained to
   distrust — and the project's public posture is built on running instruments
   that can lose.

### Strongest case against

1. **The registered headline is unreachable (0.1) and the terminal bin is
   probably "training bug" (0.2).** More seeds of a construction that failed its
   own utilization gate produce a better-estimated rate for a phenomenon that,
   per the registration's own text, "goes nowhere upstream."
2. **The statistical purchase is small.** Going from 3 fulls to 5 barely moves a
   binomial interval: 1/3 and 2/5 both carry 95% intervals spanning most of the
   unit line. Across-seed spread is the registered primary uncertainty [RT-06],
   and 5 seeds is a thin sample either way. ~$70 and ~5 days for that increment
   is poor value against the alternatives.
3. **The instrument being sampled is documented as mis-specified.** T_si's
   repeated-item cells are ill-posed by construction (thread 3). Adding seeds
   scored on an instrument with a known scoring defect adds precision to a biased
   estimate. **At minimum, the $0 T_si fix should land before any further runs
   are scored** — otherwise wave 3's data inherits the defect.
4. **It spends the money repeated-sampling needs (0.7).** Under the frozen scope,
   the ~$70 is not neutral: it is drawn from the only pool that can fund the one
   other registered run. Continuing is, in effect, a choice of five more MVM-0a
   seeds over the Stage 3 repeated-sampling arm.
5. **Wave 3 is not currently authorized.** C2 v1.1 requires a fresh per-wave go in
   John's own words, quoted verbatim in the ledger row. Continuing is an
   affirmative act, not a default. The default is that nothing launches.

### Costs

- **Money:** ~$65–80 expected, ~$95 worst case (0.5) — roughly a third of remaining
  headroom, and the swing factor for whether repeated-sampling fits.
- **Time:** ~5 days of calendar with active supervision (lid open overnight —
  wave 2 leaked ~$5.7 to a closed lid), three launch events each needing a fresh
  C2 go, in a month where Calibration has priority claim.
- **Statistical validity:** *the cleanest of the three on forking-path grounds,
  and the weakest on power.* Continuing as registered adds zero researcher
  degrees of freedom — the plan was pre-committed, the batteries are frozen, the
  operators are specified. There is no selection effect to explain, no unregistered
  change to justify, and the evidentiary value of the completed 5-seed run is
  exactly what it was registered to be. Against that: the additional data speaks
  to a bin whose headline is foreclosed, on an instrument with a documented
  construct failure and a known scoring defect. **Valid, and largely
  uninformative** — an unusual and honest combination.
- **Evidentiary value:** the highest for the *procedural* claim ("we ran the
  registered design to completion"), the lowest per dollar for the *scientific*
  claim.

### What would later prove this choice wrong

- Seeds 3 and 4 return the same flat non-binding signature (T_si ~0.33,
  T_sr_rev 0.00, flat from step 500) — the modal outcome. Then ~$70 and ~5 days
  bought a slightly tighter rate estimate on an instrument already known not to
  measure what it was registered to measure.
- The utilization gate, when finally run, fails — and the whole 10-run set lands
  in "Construction failure (register unused)," which the registration says sends
  nothing upstream. Every marginal seed was then spent on a training bug.
- Repeated-sampling turns out to fit under ~$189 but not under ~$119, and goes
  unrun for want of exactly the money wave 3 consumed.
- A cheap $0 battery fix or redesign, run on the checkpoints already in hand,
  turns out to answer the live question better than five more seeds of the
  broken instrument would have.

---

## Recommendation

**(b), taken in its wide reading, and sequenced explicitly as the opening of the
registered analysis phase rather than as a standalone threshold computation.**

Concretely, and in this order — all of it local, all of it $0–5, all of it inside
the registered plan and the frozen scope, none of it requiring an amendment:

1. **Fix the T_si repeated-item scoring defect** and rescore the five checkpoints
   in hand. This is a $0 *design* amendment, which the single-amendment ceiling
   does not constrain (0.6). Do it first: every downstream number is computed on
   this instrument.
2. **Commit the utilization-gate thresholds and the θ/δ calibration script before
   running either** — with derivations reasoned from Experiment 1's precedent and
   the measured null band, not from the lesion numbers. This is the one live
   forking path with an incentive attached (0.3), and it is the difference
   between H_routed-around and "training bug."
3. **Extend the register-lesion suite to the s1 and s2 fulls** ($0), closing the
   ≥4/5 arithmetic (0.1) by measurement rather than inference.
4. **Run the registered ablation operator set** (mean/zero/noise + the
   dynamics-matched control) and the **RT-01 probes** — the diagnostics used
   non-registered operators, so the registered ablation pass is still owed.
5. **Adjudicate the bin.** Then wave 3 follows from it rather than from a
   judgement call: gate fails → halting is the registered consequence, with the
   defence (a) needs; gate passes → H_routed-around is live and its
   seed-reliability clause makes the remaining runs matter, with the
   justification (c) needs.

Separately and under any disposition: **run the blind-localization arm** (0.8).
It is registered unconditional, cheap, orthogonal to this decision, and its
re-aimed question — do the instruments hallucinate a center where one
demonstrably is not? — is now arguably the most valuable thing left in MVM-0a.

Two corrections to carry into whatever is ruled, because they cut in opposite
directions and both belong on the record: the remainder is **5 runs at ~$65–80**,
not 7 at $130 (0.5) — which makes (c) roughly twice as affordable as the memo
implies; and **option (a)'s money premise is blocked** by the 2026-08-15 blind
scope-freeze (0.6) — a redesign is a new pre-registration with its own cap, so
(a) reduces to "halt, and let the underspend flow to repeated-sampling."

**Confidence: moderate-to-high, ~70%.** What carries it is that (b) is the only
option that requires no ruling to begin, forecloses nothing, costs approximately
nothing, and converts the other two options from judgement calls into registered
consequences. What holds it back from higher is 0.4 — a real chance that the
adjudicated verdict it produces will be discounted by a careful reader anyway.

**The single consideration most likely to flip it:** whether the θ/δ lock and the
utilization-gate margin are already *irrecoverably* contaminated by thread 4
having read register-ablation results on the registered seed-0 checkpoint before
any threshold was locked. If John rules them recoverable — on the ground that the
run-identity note made this a registered run rather than a pilot, and that the
contamination can only disfavour the registered prediction (0.4) — (b) delivers a
citable registered verdict and the recommendation stands. **If he rules them
void, (b) collapses:** it would buy a lock nobody can trust, and the honest move
flips to **(a) in its reduced form** — halt, publish the diagnostics as an
unregistered but decisive instrument-failure finding (which
`drafts/instruments-that-can-lose.md` is built to carry), let the underspend go to
repeated-sampling, and put any redesigned battery in a fresh pre-registration with
its thresholds locked before it sees data.

That single question — is the lock recoverable? — is worth resolving before
anything else, because it changes the answer rather than the margin.

---

## Appendix — corrections, gaps, and a merge hazard

**Corrections to the standing record:**

- `twin-binding-anomaly.md` and `register-lesion-findings.md` both say the
  registered remainder is "7 runs ≈ $130." Correct after wave 2: **5 runs
  (s2 twin, s3 full, s3 twin, s4 full, s4 twin) ≈ $65–80.** "7" was accurate on
  2026-08-17 and was carried forward without re-derivation.
- `register-lesion-findings.md` option (a) proposes treating "the ~$219 A2
  headroom as available for a redesigned battery." Per the 2026-08-15 blind
  scope-freeze and R1, it is not. The memo was written without that rule in
  view — which is itself an instance of the process lesson R1 recorded:
  "binding governance decisions must land in `pre-registration.md`, not only the
  worklog." The rule *is* now in `pre-registration.md` (§Ceiling adjudication
  addendum), so the miss is the memo's, not the record's.

**Gaps I could not close from the artifacts:**

- The register-lesion suite ran in full on seed 0 only; s1/s2 fulls and the twins
  have no-act results only. $0 to close.
- Gradient flow through the register write path (utilization gate leg 3) is
  unmeasured.
- No θ/δ calibration script exists in `experiments/06-.../src/`. The lock has
  never been attempted for this experiment.
- The utilization gate's per-layer attention-mass floor and path-patching margin
  are unset. Thread 4 measured residual *norms*, which is not the same
  quantity as attention mass.

**Merge hazard, for whenever the branch is merged (not now):**
`worktree-register-lesion-diagnostics` (`4296ffc`) predates main's `d0589e9` and
its `STATUS.md` / `src/mvm/config.py` / `src/SETUP.md` / `.gitignore` changes
revert the `.hf-cache` → `.hf-cache.nosync` repoint made during the
2026-08-29 iCloud move. A straight merge would regress the cache path in five
places. Worth a look at merge time; nothing was changed here.
