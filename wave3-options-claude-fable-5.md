# Wave-3 disposition — options analysis

*2026-08-30. Written by Claude Fable 5 (`claude-fable-5`), read-only session, for
John's adjudication. Sources read in full: `register-lesion-findings.md` (on the
unmerged branch `worktree-register-lesion-diagnostics`, read in place),
`pre-registration.md` v1.0 + A1 + A2 + the R1 ceiling addendum,
`twin-binding-anomaly.md`, `compute-ledger.md`, `launch-plan-5seed.md`,
`registration-decision-memo.md`, STATUS.md, the branch diff (lesion/item code +
the `fingerprint_gate.py` sidecar fix), and the TimeAssembler worklog decision
entries for Minimum Viable Mind (latest binding state: 2026-08-18 "wave 3 NOT
authorized pending John's adjudication"; 2026-08-15/16 single-amendment cap rule,
$400 final). The findings memo frames the options exactly as your prompt does —
(a) halt + redesign, (b) θ/δ null first, (c) continue as registered — so no
re-framing is needed and I use the memo's framing throughout. Nothing below is a
verdict on H_load-bearing; the disposition is yours.*

---

## 0. Facts that constrain all three options

These are load-bearing for every argument below, so I state them once, with
where each comes from.

**F1. H_load-bearing is already arithmetically unreachable — wave 3 cannot
produce the positive verdict no matter what it shows.** The registered bin
requires the pattern to hold on ≥4/5 seeds (`pre-registration.md` §bins). Fulls
so far: seed-0 bound, seeds 1 and 2 at battery floor (T_si ~0.33–0.35, T_sr_rev
0.00 — below any baseline-ceiling requirement, so those seeds cannot carry the
bin). Even if seeds 3 and 4 both bind *and* bind register-dependently, that is
3/5. The best reachable headline bins are **Seed-dependent** ("centralization of
self-binding is not a reliable property of this architecture + curriculum") or
one of the failure/void bins. This is decisive context: the argument for (c)
must survive knowing the registered win condition is already off the table.

**F2. The registered threshold lock is arguably already void, by the
registration's own text.** RT-10's clause is verbatim: *"any pilot ablation
result read before threshold lock voids the lock."* θ/δ were never locked (no
calibration script exists in `src/` — I checked both main and the branch), and
thread 4 of the diagnostics read battery scores under register ablation on the
pilot checkpoint — which, per the run-identity note, *is* the registered seed-0
full. The no-xattn lesion is strictly stronger than any registered operator
(mean/zero/noise), so the registered quantity d(T_si), d(T_sr_rev) under
register ablation for seed 0 is now known to be ≈0 before any lock. A narrow
reading says the clause targeted pilot-phase threshold-fitting and an openly
recorded anomaly diagnostic is different in kind; the plain reading says the
lock is void. Either way, **any θ/δ locked from here carries a permanent
asterisk on seed 0**, and every option below inherits that asterisk — it is not
a cost that choosing (c) avoids or that choosing (a) creates. Mitigation, also
on the record: the lesion's decision branch was pre-stated in a committed doc
(`twin-binding-anomaly.md` thread 4: "If the pilot's binding survives the
lesion, then even the one clean success was never register-dependent and the
construct problem is total") *before* the lesion ran. That pre-statement is the
single most important procedural fact in this whole decision.

**F3. Gate (iii) cannot currently certify new checkpoints.** Its positive
control has demonstrated sensitivity on exactly one checkpoint — the pilot —
and failed on all three registered-run checkpoints (`twin-binding-anomaly.md`
gate table). Wave-3 checkpoints would very likely arrive uncertifiable either
way (no evidence of a fingerprint anywhere, but no demonstrated sensitivity
either). An instrument problem, unresolved, sits in front of any continued
registered analysis.

**F4. The blind-localization arm's registered premise is now false.** It was
registered unconditionally as a ground-truth test: can Experiment 1's
instruments recover *"a center known-by-construction to exist and to be
load-bearing"*? Thread 4 shows the register is numerically active but
informationally inert — there is no known load-bearing center to recover. The
arm survives only re-purposed (as a false-*positive* probe: do the instruments
"find" a center that is causally inert? — genuinely useful for Q1, arguably
more useful than the original design), but that re-purposing is itself an
unregistered change to the arm's interpretation. No option escapes this.

**F5. Money.** Ledger: ~$181.4 spent against the $400 A2 cap; headroom ≈ $219;
$400 is final and single-amendment (R1, blind-pre-committed 08-15, adjudicated
08-16). Note a discrepancy worth resolving before any cost-based ruling: both
the anomaly note and the findings memo price the remainder at "7 runs ≈ $130,"
but the launch plan's arithmetic says 9 post-pilot launches, of which waves 1–2
ran 4, leaving **5** (s2 twin, s3 full+twin, s4 full+twin) ≈ $60–75 at measured
rates ($10/twin, $15/full, + drip), or ≈ $95 at A2's $19/run upper bound. The
"7" appears to be a slip carried from the anomaly note into the findings memo.
On either number the remainder fits headroom; the difference matters mainly for
what's left after (see F6). Full (c) — runs + ablation passes + RT-01 probes +
θ/δ + localization arm (~$30–45) — totals roughly $95–175.

**F6. What competes for the headroom.** The R1 adjudication earmarks GPU-side
underspend first for the Stage 3 repeated-sampling run ("funded only by
underspend; if it does not fit, it goes unrun"). Halting wave 3 *creates* that
underspend; running wave 3 mostly consumes it. And the memo's option (a)
assumes the ~$219 is "available for a redesigned battery" — but R1 froze the
$400's scope to the 5-seed run + repeated-sampling, so spending headroom on a
redesign is not automatic: it needs its own adjudication (either an A3 design
amendment re-scoping, or a fresh registration with its own cap). That
governance step is real work inside option (a), not a formality.

**F7. Time.** Waves 3–5 are ~3 sequential ~19h pair-waves: ~3–4 days of
Mac-lid-open watchdog babysitting, low cognitive load. A redesign is the
opposite shape: days-to-weeks of John-time (grammar/battery design, red-team
pass, registration) and near-zero GPU time until a new training decision. Which
resource is scarcer right now is your call, not derivable from the repo.

---

## 1. Option (a) — halt the 5-seed remainder; redesign the batteries

### What the register-lesion result does and does not license here

It **does** license: the pilot's battery success is computed entirely in the
trunk (four lesions, two eval seeds, logit-level verification that the pathway
is active but content-inert); combined with waves 1–2, *no observed binding
anywhere in the 30M record is register-dependent*; the batteries decompose into
unique-item lookup + a general-retrieval seed lottery + a T_si repeated-item
scoring defect; and the one demonstrably load-bearing authorship mechanism (the
non-binders' first-commitment memory) lives in the acting channel, which the
twin also has. That is a measured, multi-legged case that **the instrument does
not measure what it was registered to license** — which is precisely the kind
of finding that justifies stopping an instrument.

It does **not** license: "no 30M run could ever bind through the register."
The lesion is n=1 on bound fulls, because only one bound full exists. Seeds 3–4
are two more draws that could, in principle, produce the first
register-dependent binder. It also does not license "the *architecture* failed"
— the acting-channel result is a genuine positive finding about where
authorship lives; what failed is the batteries' ability to force the register
to matter. Halting the *runs* is licensed by the instrument findings; deciding
the *construction* is hopeless would be an over-read.

### Strongest case for

The live question changed and the registered runs don't address it. The
registered remainder measures the seed-rate of a general-retrieval lottery on
batteries whose self-reading is invalidated on every leg (memo's summary
paragraph), on a design whose positive bin is arithmetically unreachable (F1),
with a gate that can't certify the new checkpoints (F3). The redesign the memo
sketches — every queried item assigned by multiple agents, so ownership is the
*only* disambiguator; plus the T_si repeated-item fix — attacks exactly the
failure the item analysis measured: it makes lookup-without-binding score at
chance by construction. And critically, **the halt is not outcome-driven
optional stopping in the damning sense**: the stop branch was pre-stated before
the decisive diagnostic ran (F2), the diagnostics were queued in a committed
note, cost $0, and touched no registered record. The registration's own loss
conditions contemplate instrument failure; treating "the instrument is measured
not to measure the construct" as a stop-and-redesign trigger is the design
working, not the design being abandoned.

### Strongest case against

Three legs. **(i) Optional-stopping optics are real even when the stopping is
principled.** This program's entire epistemic identity — "every claim is a
wager" — rests on completing registered procedures especially when the data
disappoints. An outside reader sees: 5-seed design registered, wave 1 fails to
bind, wave 2 inverts the central prediction, diagnostics run, design halted at
4/9 launches. However good the internal justification, that *pattern* is
indistinguishable from "stopped when it stopped flattering the hypothesis,"
and the defense requires trusting the project's own committed timeline. (You
have that timeline, and it is genuinely exculpatory — but the critique writes
itself and the rebuttal takes a paragraph.) **(ii) The redesigned battery is
fit to the observed failure.** It is being designed *after* item-level analysis
of all five checkpoints; it is guaranteed by construction to separate the
phenotypes already seen. Results of the new battery on the *existing*
checkpoints therefore have sharply reduced evidentiary standing (instrument
tuned to data), and the existing checkpoints are probably off-distribution for
it anyway (in the training grammar, items repeat only under same-agent
revision, so multi-agent same-item episodes are outside training support —
failures on them are uninterpretable). A clean test needs retraining under a
grammar that supports the new battery: real money, plausibly most of the
remaining headroom, and a fresh red-team + registration cycle first. **(iii)
Scope/governance friction (F6):** the headroom isn't automatically available
for a redesign, and the redesign competes with the repeated-sampling run R1
earmarked. Option (a) is not "stop spending"; it is "start a new, John-time-
expensive project phase with contested funding."

### Costs

- **Money now:** $0. **Money later:** new-curriculum training runs — a 30M
  full at measured pace is ~$15–19; even a modest 3-seed full+twin redesign
  pilot is ~$75–100, i.e., most of what wave 3 would have cost, against
  the same finite headroom, pending the F6 adjudication.
- **Time:** the expensive kind — design, red-team pass 3, registration,
  adjudications. Weeks of calendar at this project's historical pace.
- **Statistical validity:** the halt itself is well-protected (pre-stated
  branch, committed diagnostics). The exposure is downstream: the new
  instrument's design is conditioned on everything observed, so its
  validation must be *prospective* (fresh seeds, thresholds locked before any
  ablation is read — this time actually before). Any attempt to claim results
  from re-scoring existing checkpoints on the new battery would be a
  garden-of-forking-paths harvest and should be pre-labeled exploratory.
- **Evidentiary value of the change:** an A3 amendment recording the halt,
  its pre-stated trigger, and the diagnostic evidence keeps the paper trail
  unbroken. The registered 5-seed design ends as "halted at 4/9 launches on
  measured instrument invalidity; remainder unrun" — reported, not spun.

### What evidence would later prove (a) wrong

- A future run under the *redesigned* battery where a register-less twin again
  passes at ceiling — i.e., the problem was never the battery's lookup
  loophole but something deeper (the acting channel suffices for any
  behavioral ownership test), meaning the redesign spend re-bought the same
  lesson thread 4 already taught.
- Seeds 3–4, if ever run for another reason, producing a full that binds *and*
  whose binding dies under the lesion harness — the register-dependent
  exemplar existed two draws away and the halt walked past it (see option (c)
  for the plausibility read).
- The redesign stalling in governance/red-team long enough that the program
  loses its cadence — in which case completing the mechanical remainder would
  have preserved momentum at trivial cognitive cost.

---

## 2. Option (b) — run the registered θ/δ null calibration first (~$2–5)

### What the register-lesion result does and does not license here

It **does** license the expectation that the calibration's downstream use is
mostly ceremonial for seed 0: we already know register ablation moves the
batteries by ≈0, so the only question the null answers there is whether 0 sits
inside the null band (it will). It does **not** license skipping the
calibration as worthless: the null band is also the yardstick for (i) the
seed-2 late-checkpoint wander (0.26→0.43→0.31→0.35 at n=100 — the anomaly note
already suspects this is inside noise), (ii) any future lesion-harness reading
on new checkpoints, and (iii) the *record* — it converts thread 4's diagnostic
"≈0" into a registered-instrument statement "d = x, null band [−y, +y],
verdict: indistinguishable from null" that the halt memo (if (a) follows) or
the final report (if (c) follows) can cite without asking the reader to trust
an unregistered harness.

### Strongest case for

It is already registered, so it requires no amendment; it is the single
cheapest item in the whole program (~$2–5, minutes-scale at these widths per
the decision memo); and it is the only option that *improves the record no
matter what is decided next*. If (a) follows, the halt is documented with a
quantified instrument reading rather than a diagnostic one. If (c) follows,
the analysis phase needs θ/δ anyway and the script must be written and
committed regardless. It also honors the registration's shape: the calibration
was always supposed to run before verdicts were read, and running it now is
the closest available approximation to the registered sequence. Sequencing it
first costs essentially nothing and forecloses nothing.

### Strongest case against

**(b) is not a disposition — it is a deferral with a $3 fig leaf.** The
memo's own framing gives it away: "for the record before any redesign." The
actual decision (halt vs continue) is untouched by any possible output of the
calibration: no null band, wide or narrow, changes F1 (H_load-bearing
unreachable), F2 (lock asterisk), or the construct findings. If the
calibration result cannot change the next action, running it "first" is
motion, not progress — and there is a mild pathology risk in a program this
procedure-conscious of accumulating ritual completions whose outputs nothing
consumes. Second: the lock-void problem (F2) means the θ/δ produced now are
locked *after* the seed-0 ablation results were read. For seed 0 the
calibration can never be clean; the honest label is "null calibration for the
record, thresholds not usable as a registered lock for seed 0," and that label
must be written down or the calibration *manufactures* a false appearance of
procedural cleanliness — which would be worse than not running it. Third, the
script does not exist yet; "committed before it runs" is satisfiable going
forward, but it is a small piece of new work, not a button press.

### Costs

- **Money:** ~$2–5 (local/tiny-model inference; possibly $0 if it runs on the
  local checkpoints like the lesion work did).
- **Time:** hours — write the script, commit, run, record.
- **Statistical validity:** positive on net (a real noise floor for every
  n=100 swing in the record) *provided* the seed-0 asterisk is stated. The
  selection-effect exposure is nil — the calibration is content-blind
  (random-subspace and matched-norm ablations, pre-committed quantiles).
- **Evidentiary value:** modestly positive; converts one more diagnostic
  claim into a registered-instrument claim.

### What evidence would later prove (b) wrong

- Its output is never cited by any subsequent document — the pure-ritual
  outcome (cheap, but a data point that the program is completing procedures
  rather than answering questions).
- The null band comes out wide enough (at n=100) that even the *binders'*
  d-values from any future ablation are inside it — revealing the registered
  eval size was never adequate for the verdict logic, which would have been
  worth knowing before wave 1, and makes the choice to run more n=100-adjudicated
  seeds (option c) look worse in hindsight, not better.

---

## 3. Option (c) — continue wave 3 as registered

### What the register-lesion result does and does not license here

It does **not** license continuing *as evidence-buying for H_load-bearing* —
the memo says this outright and F1 makes it arithmetic: no wave-3 outcome
reaches the positive bin, and thread 4 + the wave-2 twin sever battery success
from the register on every observed exemplar. But it also does **not** license
the claim that wave 3 is informationally empty, on two counts. First, the
lesion result is n=1 on bound fulls; seeds 3–4 are two more draws at a binder,
and the lesion harness now exists, is local, and costs $0 to run on any new
binder. A wave-3 full that binds and *loses* its binding under the lesion
would be the program's first register-dependent exemplar — not enough for the
registered bin, but qualitatively the most important single observation the
program could make. Second, the seed-rate itself (currently "2 of 5 runs found
general retrieval") is a real quantity with a huge CI; 10 runs halve nothing
but do tighten the "is binding a lottery or a near-miss" read that any
redesign's power analysis will want.

### Strongest case for

**Pre-commitment integrity is the program's spine, and it is worth paying for
even when the payment buys no new headline.** The whole corpus stakes its
credibility on registered designs that run to completion regardless of interim
disappointment; the strongest version of (c) says: the time to decide whether
mid-design diagnostics can halt a registered run was *before* registering, and
the registration contains no such stopping rule — so the runs complete, the
bins are read as registered (landing in Seed-dependent or a failure bin,
honestly), and the construct critique is published *alongside* a completed
design rather than in place of one. That is maximally legible to a hostile
reader: no forking paths, no discretion exercised, the anomaly and the
completion both on the record. Secondary supports: the marginal cost is small
(F5: ~$60–95 for the runs; ~$95–175 all-in) and fits headroom; the cognitive
cost is near-zero (watchdogged pair-waves); the A2 wager ("completes under
$400 with ≥5 clean seeds") gets a clean win/loss reading instead of a
"neither"; and the two extra full-seed draws carry the small-but-real option
value described above, with free lesion follow-up on any binder.

### Strongest case against

It buys procedure, not evidence, and the memo's own sentence is the honest
label: "defensible only as a pre-committed-procedure completion, not as
evidence-buying." Concretely: (i) the headline bins reachable after wave 3 are
already known to within noise — Seed-dependent, or a utilization-gate failure
(thread 4's shuffle result predicts the path-patching leg of the
register-utilization gate fails: register content changes nothing, so even
H_routed-around may be blocked in favor of "construction failure (register
unused)"); (ii) the checkpoints arrive gate-uncertifiable (F3); (iii) the
analysis phase those runs feed presumes a threshold lock that F2 has already
asterisked; and (iv) every dollar spent is a dollar the R1-earmarked
repeated-sampling run and any redesign cannot spend (F6) under a cap that can
never be raised. There is also a subtler integrity cost on (c)'s own terms:
*completing* a design whose instrument the project has already measured to be
construct-invalid, and then reporting bins computed by that instrument, is not
obviously the more honest posture — it manufactures registered-looking output
downstream of a known-broken license. The forking-paths norm exists to stop
data-driven *cherry-picking*; it was never meant to compel spending on an
instrument after a pre-stated diagnostic branch measured the instrument's
license to be false on every leg.

### Costs

- **Money:** runs ~$60–95 (resolve the 5-vs-7 count, F5); all-in with the
  registered analysis ~$95–175 of the ~$219 headroom — leaving perhaps
  $45–125 for everything else, ever, under this cap.
- **Time:** ~3–4 days wall-clock babysitting; low John-cognition; plus the
  analysis phase.
- **Statistical validity:** no selection-effect exposure in the runs
  themselves (that is (c)'s whole virtue). The exposure is interpretive:
  reporting registered bins from an instrument with measured construct
  invalidity invites over-reading by others even if the report is carefully
  hedged; and the gate/threshold asterisks (F2, F3) attach to every number
  produced.
- **Evidentiary value:** the completed design's value for H_load-bearing is
  ≈0 by F1; its value is the seed-rate estimate, the option on a
  register-dependent binder, and the legibility of completion.

### What evidence would later prove (c) wrong

- Seeds 3–4 come back as three more lottery draws (the modal outcome: fulls
  are 1/3 binders so far, and both observed binders were trunk-based), the
  bins land Seed-dependent-with-asterisks as predicted, and the redesign then
  needs exactly the money wave 3 spent — the foreclosure scenario, made
  irreversible by the never-moves-up cap.
- The redesign, once run, shows the ownership-only battery is learnable and
  discriminating at 30M — demonstrating the answerable question was available
  in August and wave 3 postponed it for a quantity (lottery seed-rate on an
  invalid instrument) no later document ever cites.

---

## 4. Recommendation

**Run (b) now, as the on-ramp to (a); do not run wave 3.** Concretely, in
order: (1) write and commit the θ/δ null-calibration script, run it (~$2–5)
across all five local checkpoints, and record the d-values against the null
band with the seed-0 lock-void asterisk stated in the same document; (2)
register an A3 *design* amendment (the single-amendment rule froze the cap,
not the design — A1 is precedent) that halts the 5-seed remainder, citing the
pre-stated thread-4 branch as the trigger and F1–F4 as the findings; the
registered 5-seed design closes as "halted at 4/9 launches on measured
construct invalidity; remainder unrun," with the A2 wager scored against
actual spend; (3) adjudicate the F6 headroom question (redesign vs
repeated-sampling) before any new GPU dollar; (4) take the redesigned battery
through red-team and a fresh registration with thresholds locked before any
ablation is read — actually before, this time.

The decisive weights: wave 3 cannot reach the positive bin (F1), so (c)'s
entire case is procedural legibility — and that case is substantially covered
at zero GPU cost by the fact that the halt branch was pre-stated in a
committed document before the decisive diagnostic ran, then closed out through
a registered amendment rather than a quiet stop. Meanwhile (c)'s spend is
large relative to a cap that can never be raised and directly competes with
the two things that still answer live questions (the redesign; repeated-
sampling). Option (b) alone is a deferral, but as step one of a halt it is
cheap, already registered, and makes the halt memo quantitative.

**Confidence: ~0.75** that (b)→(a) is the choice you'd endorse after full
deliberation. The residual sits almost entirely on one consideration.

**The single consideration most likely to flip it:** how much you weigh
*unconditional completion of registered designs* as a program-level
credibility norm — the rule that a registered run is never stopped by
mid-design judgment, however well-evidenced, because the norm's whole value is
that it admits no judgment calls. If you hold that norm strictly, (c) is
correct, the ~$60–95 is the price of the norm, and everything above about
information value is beside the point; the runs complete, the bins are read,
and the redesign follows anyway with its credibility enhanced by the
completion. What softens the flip — and why I still recommend against (c) — is
that the halt trigger was itself pre-stated before the evidence arrived, which
is the same commitment device the norm exists to enforce; a program that
pre-states its stopping branches and then honors them is keeping the norm, not
breaking it. Secondary flip (downward, toward pure-(a)): if you judge the
seed-0 asterisk makes the θ/δ record more misleading than clarifying, skip (b)
and halt directly — nothing in the (a) case depends on (b) running.

---

## Appendix: small items surfaced while reading, for the amendment's accuracy

- **The "7 runs ≈ $130" figure** in `twin-binding-anomaly.md` and
  `register-lesion-findings.md` conflicts with `launch-plan-5seed.md`'s
  arithmetic (9 post-pilot launches − 4 completed = **5** remaining: s2t, s3f,
  s3t, s4f, s4t ≈ $60–95). Whichever document the amendment cites should use
  the reconciled number.
- **The blind-localization arm needs its own disposition line** in any
  amendment: its registered premise (recover a center known to be
  load-bearing) is false per thread 4 (F4). Re-purposing it as a
  false-positive probe on the inert-but-active register is cheap (~$5) and
  genuinely bears on Q1/Experiment 1's null, but that re-purposing is an
  unregistered change and should be registered as such if kept.
- **The gate-script sidecar fix** (`fingerprint_gate.py --canonical` guard) and
  the lesion/item artifacts live only on the unmerged branch; the amendment
  should merge or cite that branch so the record it leans on is on main.
- **T_si repeated-item scoring defect** (coin-flip answer key on revised
  items) is a scoring bug independent of any disposition; fixing it is
  uncontroversial under any option but changes battery numbers, so the fix
  should be registered with the redesign, not slipped in.
