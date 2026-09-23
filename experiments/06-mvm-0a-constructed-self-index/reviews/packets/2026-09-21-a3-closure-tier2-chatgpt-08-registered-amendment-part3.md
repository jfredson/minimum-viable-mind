# Review packet - the closure text of Amendment A3 (Minimum Viable Mind) - file 8 of 22: The registered amendment, part 3 of 3

*This is file 8 of 22 of one review packet, pasted into a single conversation.
It contains the registered amendment this block will be appended to (part 3 of
3). Reply with one short line saying you have it, and wait for the rest: the
brief you are answering is in file 1, and your review comes only after file 22
arrives. If this file looks cut short, say so now.*

---

===== RECORD 5 of 23, part 3 of 3 - the registered amendment this block will be appended to - COMPLETE FILE: experiments/06-mvm-0a-constructed-self-index/amendment-a3.md =====

*This part is its sections 4 to 7, and the registration revisions of
2026-09-15. The other parts of this record are in file 06 and file 07.*

## 4. Budget, gates, and kill criteria

### 4.1 The envelope

Per John's ruling the remainder under the $400 ceiling is about $100 to $120 across all vendors. This amendment proposes a **hard stop of $100 for everything it authorizes** (proposed), leaving the balance of the remainder unallocated. Measured unit costs: a register-less 30M run is about 10.2 hours at $0.99/hr, about $10 to $11 plus volume drip (`compute-ledger.md`, wave 1 and 2 twin rows); local lesion, probe, and eval work has run at $0 on the Mac (`register-lesion-findings.md` header; STATUS 2026-08-19).

| gate | what runs | est. cost | cumulative |
|---|---|---|---|
| **Gate 0: null calibration** (registered, unspent) | write and commit the θ/δ script; run matched-strength random-subspace and matched-norm ablations across the five existing checkpoints at n=400; record d against the null band with the seed-0 lock-void asterisk stated (`wave3-options-claude-fable-5.md` §2; `wave3-options-opus-5.md` §0.4); T_si repeated-item rescoring | $0 to $5 | $5 |
| **Gate 1: curriculum + gates (i), (ii)** | Candidate A grammar; frozen batteries; cue-detector runs (i) and (ii) with positive controls | $0 | $5 |
| **Gate 2: learnability pilot** | one register-less 30M run, seed 0, registered token budget, T_act and T_other read at endpoint only | ~$11 to $13 | $18 |
| **Gate 3: gate (iii), act-withheld arm B** | on the pilot checkpoint, n=4000, local | $0 | $18 |
| **Lock** | θ/δ null-calibrated on the pilot checkpoint; utilization of the L1 pipeline dry-run on random subspaces only; John's lock commit | $0 | $18 |
| **Registered seeds** | two further register-less runs (seeds 1, 2); the pilot counts as seed 0 by the run-identity precedent (`pre-registration.md`, run-identity note) if the recipe is byte-identical | ~$22 to $26 | $44 |
| **Lesion phase** | L0, L1, L2 on three checkpoints; probes, patching, re-indexing probe; local | $0 to $10 | $54 |
| **Margin** | one crash-resume (fresh C2 go), volume drip, one overnight idle leak at the observed ~$5.7 | ~$20 | $74 |
| **Optional seeds 3 and 4** | only if cumulative actual spend at the lesion phase is ≤ $55 and John gives a separate go | ~$22 | $96 |

Expected total about $55 to $75; worst case at the hard stop of $100. The A2 wager's shape is reused: this amendment predicts completion under $100 with three clean seeds, and if measured spend approaches $100 with seeds missing, the report is the shortfall, never a second raise.

### 4.2 Hard kill criteria (each halts spend and sends the finding to John)

- **K0.** Gate 0's null band at n=400 is wide enough that the existing binder/non-binder split (T_si 0.96 to 1.00 against 0.34 to 0.36) sits inside it. Then the verdict logic is underpowered at any affordable eval size and no training dollar is spent. (Proposed band criterion: 95th-percentile null |d| ≥ 0.25; John sets the number at Gate 0.)
- **K1.** Gates (i) or (ii) fail on the Candidate A grammar after two regenerations. $0 spent.
- **K2.** Pilot T_act at budget exhaustion ≤ lookup ceiling (0.25) plus the null band: unlearnable. About $18 spent.
- **K3.** Shortcut-starvation signature at the pilot endpoint (T_act at ceiling, T_other flat). About $18 spent.
- **K4.** Gate (iii) act-withheld arm B fails with positive controls firing. One grammar regeneration and re-pilot is permitted if cumulative spend stays ≤ $35; otherwise halt.
- **K5.** Probe-patching convergence fails on all three seeds: *not testable (localization)*, reported as such; no further seeds.
- **K6.** Cumulative actual spend reaches $100. Halt regardless of state; remainder unrun and reported.
- **K7.** Any C5 event (the model observed exploiting or degrading the evaluation machinery) halts the run before any further compute.

### 4.3 Procedure order, binding if ratified

Gate 0 → Gate 1 → red-team pass 3 on this document → registration commit → Gate 2 (C2 go, quoted verbatim in the ledger row) → Gate 3 → lock → seeds 1 and 2 (C2 go per wave) → baseline verification and cull → L0 → L1 and L2 → verdict per seed at budget exhaustion (RT-07 checkpoint schedule retained) → across-seed bin → optional seeds → report. Every pod launches through the registered launcher with the watchdog fetch-and-kill and the network volume (A2.3).

---

## 5. Red team: why this will probably also come back null, and what each null buys

**The honest prior.** The most likely outcome is another predicted null. Two of the four MVM-0a training configurations produced no binding at all, the one instrument the program has run on a stock model found routing, and every null so far has landed in a bin that was written down before the data arrived. The case for spending $55 to $100 is not that a positive is likely; it is that each reachable null lands somewhere with a consumer, and that the design produces, for the first time, a ground truth the instruments can be scored against.

**R1. The acquired index is just the wire, passed forward.** The strongest objection. Whatever probes find at revision positions may be the acting-channel input propagated through attention, an echo of the sense organ, not a structure the network built. Lesioning it would then be lesioning the input by another route, and a "positive" would say only that the wire is load-bearing, which L0 already says. *Mitigations:* localize only at positions far from any act position; require L1 to beat the other-index control (which is also downstream of the same inputs); require the swap probe to move the action; and report the L0-to-L1 gap honestly (if L1 ablation recovers most of the L0 collapse, the carried structure is doing the work; if it recovers little, the echo reading stands). *If this null fires,* the finding is that at 30M ownership is carried as an input trace and never consolidated into a structure of its own, which bounds what "acquired under task pressure" can mean at this scale and is worth one paragraph upstream.

**R2. Unlearnable at 30M.** 10M did not learn T_si (`pilot-a1-findings.md`); 30M learned it on one seed of three (`twin-binding-anomaly.md`). Candidate A is harder than T_si: it demands the binding at an action position under a deterministic rule. A fair prior is that seed 0 lands at the lookup ceiling. *Why it still pays:* the pre-stated ceiling makes this a clean, cheap ($18) bound, and it separates "the objective cannot be learned here" from "the objective was learned another way," which the old batteries could not do. The registered loss condition applies verbatim; no scale bump.

**R3. Seed lottery.** Binding at 30M was seed-dependent on the old batteries (fulls 1 of 3, twins 1 of 2). Three seeds is thin; the positive bin requires all three, which makes a false positive unlikely and a seed-dependent verdict likely. *Why it still pays:* seed-dependent is a registered bin with a pre-stated headline ("not a reliable property of this architecture and curriculum"), and it costs nothing more than the design costs anyway.

**R4. Keyed tag, again.** RT-01's worry returns without the register: the network may build an (item, mine-bit) lookup, and the mine-bit subspace is an address. ch05's program-counter reply says an address is not the floor. The re-indexing probe is the registered discriminator and it is imperfect: a tag that is re-written at re-indexing looks like a center that re-centers cheaply. *If this bin fires,* the upstream finding is about the test: the removal test, as an operational protocol at this scale, cannot separate an indispensable ownership tag from self-location without a re-centering probe, and even then only partially. That is a real yield for `ch05` "The Center That Cannot Be Deleted," and it goes up as a proposal, not a correction.

**R5. Gate (iii) under a perspectival policy.** The act-withheld arm B is new and untested. It may fail for a reason that is neither a leak nor a policy fingerprint (for example, the withheld-act forward is off-distribution and the likelihoods are noise). *Mitigation:* the positive controls must fire on the same withheld forwards or the arm is declared uncertifiable, not failed; K4 caps the retry. The known weakness stands: arm B's positive control had demonstrated sensitivity on exactly one of four old checkpoints (`twin-binding-anomaly.md`, gate table), so "uncertifiable" is a live outcome and is reported as such.

**R6. Threshold contamination carried over.** The seed-0 lock on the *old* design is void or asterisked (`wave3-options-claude-fable-5.md` F2; `wave3-options-opus-5.md` §0.4). This amendment inherits none of it only if no one reads an L1 result on the new pilot before the lock. The procedure order in §4.3 makes the lock a gate rather than a habit; the red-team pass should check that `lesion_register.py` cannot be pointed at the new checkpoint before the lock commit exists (proposed: the script refuses to run L1 without a lock-hash argument).

**R7. Diffuse and uncarvable (the Q1 null).** Ownership is load-bearing (L0 collapses T_act) and no subspace at k ≤ 16 beats the controls. This is, on the evidence of Experiment 1's never-subtracted report and the register's inertness, a leading candidate. *Why it pays most of all:* it is the outcome the blind-localization arm was registered to detect and lost its premise for (`wave3-options-opus-5.md` §0.8: "there is no such center" to recover). Candidate A restores a ground truth: a system in which ownership is measured to be load-bearing by L0. If Experiment 1's pipeline cannot carve it, the honest reading of Experiment 1's null shifts toward instrument failure, which is the single finding RT-12 said might outweigh the headline. This document does not tee the arm up (§6); it notes that the design makes the arm's question answerable again.

**R8. Generic binding.** The located structure is who-did-what machinery for all agents, the small-model version of Experiment 1's router. Pre-stated as H_generic-binding; costs nothing beyond the design; sharpens the same lesson a third time (naive localization finds infrastructure).

**R9. Optics.** The program halted a registered 5-seed run at four of nine launches and is now proposing a design fitted to the observed failure. Both options memos make this point (`wave3-options-claude-fable-5.md` §1, case against, legs i and ii). *Answer, on the record:* the halt trigger was pre-stated in `twin-binding-anomaly.md` before the decisive diagnostic ran; the new design's validation is prospective (fresh grammar, fresh seeds, thresholds locked before any lesion is read); results on the old checkpoints are labeled exploratory; and the amendment records the 5-seed design as halted at four of nine launches with the A2 wager scored against actual spend.

**What every null shares.** Each lands in a bin with a named consumer: the roadmap's Q1 (R1, R7), the registration's loss conditions (R2, R3), ch05's operational test (R4), or the methods record (R5, R6, R8). And the first $5 gate can kill the whole plan before any training dollar is spent (K0). That is the sense in which a probable null still pays: the design is built so that the most likely outcomes are informative and the cheapest outcome comes first.

---

## 6. What is NOT changed

- **The ceiling.** $400 remains the single permitted cap amendment (A2, R1), final, covering all MVM compute across vendors as John ruled on 2026-08-30. This amendment spends inside the remainder with its own hard stop (§4.1) and never proposes a raise. Note for the record: R1's addendum said a "third experiment" belongs to a new pre-registration with its own cap; John's 2026-08-30 ruling that the battery is redesigned "as a registered amendment" within the $400 is read here as superseding that sentence on scope, not on the number. Decision 8 asks John to confirm that reading, because the two options memos read R1 differently (`wave3-options-opus-5.md` §0.6 against; `wave3-options-claude-fable-5.md` §4 step 2 for).
- **Corrigibility commitments v1.1.** C1 (checkpoints non-promotable), C2 (John authorizes every run; the go is quoted verbatim in the ledger row; a resume needs a fresh go), C3 (every run killable; the RT-07 schedule keeps every checkpoint readable), C4 (no stakes term; the T_act loss is a per-position CE on an episodic task and cannot be conditioned on continuation), C5 (optimization against instruments halts the run), C6 (retention), C7 (the calibration rule binds reporting). MVM-0a under A3 remains floor-only and episodic: no maintained boundary, no persistent cross-episode state, no stakes. Nothing here pre-authorizes MVM-0b. The commit hash cited is `6c14244`.
- **The blind-localization arm's dependency.** John's ruling: the arm is not teed up until the wave-3 call. This document does not tee it up, re-purpose it, or run it. §3.2 reuses Experiment 1's *localization pipeline* as the L1 method; that is a different thing from the registered *arm*, which is an instrument audit run blind to a designated location with a verdict-first firewall. Whether the arm runs on the old checkpoints as registered, is re-aimed as a false-positive probe (`wave3-options-opus-5.md` §0.8), or is retired, is a separate decision (decision 10) that this amendment leaves open.
- **The registered bins' logic, the chance-corrected metric, the OOD and degeneracy gates, the frozen-skeleton battery unit, the RT-07 checkpoint schedule, the across-seed uncertainty rule (RT-06), the venue and launcher (A2.3), and the standing rule that any change to a registered plan is itself a registered amendment.**
- **Repeated-sampling's claim on underspend (R1).** Not changed by this document, but this amendment competes with it for the same remainder. Decision 6 puts the priority to John explicitly rather than settling it by spending first.

---

## 7. Decisions for John (each yes/no)

1. **The reading.** Ratify §1 as the amendment's stated basis: the register was self-reference under ch05's removal test and its null was predicted; the record's one load-bearing authorship mechanism was an act, not a store.
2. **Primary objective.** Candidate A (perspectival revision rule, "act as yourself") is the primary objective; B and C are recorded as alternatives.
3. **No register.** The new runs train the register-less architecture with the acting channel; the register is not installed in any A3 run.
4. **Gate 0 first.** The registered θ/δ null calibration runs on the five existing checkpoints before anything else, with the seed-0 lock-void asterisk stated in the same document, and K0 is a hard kill.
5. **Seeds and bin rule.** Three seeds (pilot counts as seed 0 if byte-identical recipe); the positive bin requires all three; two of three is Seed-dependent.
6. **Budget priority.** This amendment's $100 hard stop takes precedence over the Stage 3 repeated-sampling run's claim on underspend; whatever remains after A3 is what repeated-sampling can have.
7. **Gate (iii) re-specification.** Arm B scores act-withheld forwards; positive controls must fire on the same forwards.
8. **Amendment, not new registration.** Number this A3 to MVM-0a under the existing $400 ceiling (confirming the reading of R1 in §6).
9. **Close the 5-seed design.** The same amendment records the registered 5-seed run as halted at four of nine launches on the pre-stated thread-4 trigger, remainder unrun, A2 wager scored against actual spend.
10. **Blind-localization arm.** Confirm this amendment makes no decision on the arm; its disposition is a separate item.
11. **Re-indexing probe.** Include the mid-episode re-indexing probe as the registered discriminator for H_tag.
12. **Eval size.** Verdict cells at n=400, local.
13. **Red-team pass 3.** Commission a red-team pass on this document before the registration commit, per house procedure.
14. **T_si fix.** Register the T_si repeated-item scoring fix with the redesign, not separately.
15. **Lock enforcement.** Require the lesion script to refuse L1 runs without a lock-hash argument (R6).

*Nothing above is registered. The registration commit, if it comes, follows the red-team pass and John's decisions, and every run it affects is launched after it.*

---

# REGISTRATION REVISIONS — 2026-09-15

**Status of this amendment changes here from RATIFIED to REGISTERED.**

Everything above is the text John ratified on 2026-09-15 and is left
standing, unedited, as the historical record. Everything below supersedes
it where the two conflict. Each item names what the ratified text said,
what replaces it, and why. All fourteen were ruled by John on 2026-09-15
after Gate 0, Gate 1, red-team pass 3 and an ownership-blind attack sweep,
all of which ran at **$0** before any pod existed.

The design's central bet is unchanged. What changed is that three claims
it rested on turned out to be false of the grammar as built, and the
instrument that was supposed to catch one of them could not.

## 1. The grammar (decision 1)

**Ratified text:** §2.2, a revision rule applied at the model's own
revision turn, with no statement of how often that turn occurs or how many
other agents revise.

**Registered:** twelve turns became ten. Four agents each assign two
contested items, the four values on an item are distinct, and **two agents
drawn uniformly over all four** then revise, one item each. The model is
therefore a reviser in half of episodes, and a scoring cell comes from
half of episodes.

**Why it took three drafts, recorded because a design that took three
tries should say so where it is registered.** Making the model revise in
every episode gives a cell every time but makes how much an agent speaks a
perfect giveaway. Making every agent revise removes that cue and creates a
worse leak: anyone who has already revised is not the one revising now, so
when the model revises last its own assignment is the only one left and
identifying it needs no self-knowledge at all, which lifted the true
ownership-blind ceiling to 0.52 while the record still said 0.29. Drawing
two revisers uniformly restores the ceiling and keeps both cues
uninformative. You cannot have all three of a cell in every episode,
revising not marking the model out, and agents that have acted not being
eliminable. Any two.

## 2. The speaker's name moves after the value (RT-20)

**Ratified text:** §2.2 assumed the registered rendering, in which a turn
opens with the speaker's name.

**Registered:** a turn renders `assign <item> to <value> by <marker>`.

**Why.** Under the old rendering the graded token is the value and the
model's own name sat three tokens back in its own context, so a solver
using no ownership information at all could read that name, find the
matching earlier assignment and apply the rule. Measured: **1.000 over
3,000 episodes**, on a grammar that had just passed both cue gates. The
cue gates could not have caught it, because they ask which turns are the
model's own, which is a different question. The attack is kept as a
permanent regression test in the grammar's own self-test.

## 3. The metric divides by the ceiling, not by chance (decision 3)

**Ratified text:** `d(B) = (B_base − B_abl) / (B_base − chance_B)`,
inherited from the registration.

**Registered:** `d(B) = (B_base − B_abl) / (B_base − ceiling_B)`, where
`ceiling_B` is the measured shortcut ceiling. **A value above 1.0 is
reported, never clipped**: it means the ablation took the battery below
what an ownership-blind solver reaches, so the lesion removed more than
ownership, and hiding that in a clamp would turn the most interesting
failure into a quiet 1.0.

**Why.** A lesion that removes ownership cannot push a battery below its
ceiling, so dividing by the distance to chance divides by a range the
battery cannot traverse — and the error differs per battery. With ceilings
of 0.2921 and 0.3227 the two verdict batteries could show at most 0.809
and 0.774, so a lesion of a purely **generic** binder, which hits both
equally in real terms, still reported a differential of 0.035 against a
band near 0.01. The bin meant to catch the boring explanation could not
fire and the bin meant to find a self-index fired on it. Under the
registered metric that differential is exactly 0.

## 4. The ceilings are measured, not asserted (decision 2)

**Ratified text:** §2.2 pre-states a lookup ceiling of 0.25.

**Registered:** **0.2921** for the primary battery and **0.3227** for the
control, measured on the registered grammar and verified by the attack
sweep, whose best ownership-blind attack reached 0.3036 on 12,000
episodes — one standard error from the analytic value. Both numbers are
stored in `batteries-a3/batteries_meta.json` with their method. Any future
grammar carries its own measured ceilings; none is ever asserted.

> **REGISTERED DEFECT, 2026-09-17 (John's instruction; decidedBy john).
> Nothing above is altered. The claim "verified by the attack sweep" is
> FALSE as applied to the control battery.**
>
> The 0.3036 attack figure quoted above is an attack on the **primary**
> battery, compared against the primary's 0.2921. `src/shortcut_sweep.py`
> contains **zero** occurrences of the control battery and attacks the
> primary only. One verification is attached to two numbers.
>
> The control's 0.3227 rests entirely on the reference solver in
> `curriculum_a3.measured_ceilings`, **which never reads the marker the
> control question supplies**. The control asks about a *named* agent;
> the solver enumerates all four agents' successors and guesses among
> those not already visible. So 0.3227 is the score of a solver that
> cannot read names, and the battery's real ownership-blind ceiling is
> **near 1.0 and unmeasured**.
>
> The module's own documentation states the control's lookup ceiling as
> **0.5**, not 0.3227, and says red-team pass 3 "should weigh" it because
> the generic-binding bin turns on the two batteries' difference. That
> pass ran and did not weigh it.
>
> **No result changes.** The control fails its floor at 0.3227, fails by
> more at 0.5, and fails by far more at a true ceiling near 1.0. Every
> reading makes it less learned. What changes is that the metric's
> denominator for this battery was never a checked quantity.
>
> **If an Amendment A4 opens, measuring this ceiling properly is a
> precondition of it** (John, 2026-09-17). Full record:
> `ceiling-defect-2026-09-17.md`.

## 5. The attack sweep becomes a gate (decision 8)

**Registered:** `src/shortcut_sweep.py` is a gate in its own right, run
before any dollar is spent. **It passes when no ownership-blind attack
beats the stated ceiling by more than sampling error** — that is, when the
stated ceiling is the true one. If it cannot be made to pass within two
regenerations, the design halts.

**Why this shape rather than a threshold on the ceiling.** The sweep's job
is to make the stated ceiling honest, not to veto a design. A ceiling that
is high but honest weakens the learnability reading and shrinks the range
a lesion can show, but both degrade smoothly and neither has a cliff; an
earlier draft of this clause proposed halting above 0.40 and that number
could not be derived. Whether an honest ceiling is too high to be worth
training is the judgment in item 1, not an automatic kill.

## 6. Thresholds, kills and bins (decisions 4, 5, 6, 12; K0's number)

- **Revision frequency** is now stated (item 1): two of four agents, drawn
  uniformly, so half of episodes carry a supervised action and a 400-cell
  verdict needs 800 episodes.
- **K2** compared "lookup ceiling plus the null band", adding a raw
  accuracy to a chance-corrected quantity. It is restated in raw accuracy,
  with the band converted explicitly. It decides the unlearnable verdict,
  so it is fixed before the pilot rather than after.
- **K0's band stays at 0.25**, the pre-stated figure, deliberately
  unchanged now that Gate 0 has measured the band at about 0.01. Moving it
  either way after seeing the data would be fitting the rule to the data,
  and the value of a pre-stated number is that you do not touch it once
  you have looked. It is read **only on batteries above the floor margin**,
  so a run that never learned a battery cannot trip it.
- **θ and δ are per battery**, not single numbers. Gate 0 measured them
  varying across a twenty-five-fold range within one checkpoint.
- **A bin is added for the validity check failing.** If zeroing the acting
  channel does not collapse the primary battery to its ceiling, ownership
  is not load-bearing and the objective has failed. The registered design
  had such a guard and it was dropped along with the register. Without a
  bin that outcome has nowhere to land, and an outcome with nowhere to
  land gets explained away.
- **An uncertifiable likelihood attack is routed.** If the act-withheld
  arm's positive controls do not fire, the arm is declared uncertifiable
  rather than passed or failed, and the procedure continues with that
  stated, instead of deadlocking.

## 7. The cue detector's sampler (decision 7 and the sampler amendment)

Both arms of the detector are now drawn the same way, and the verdict is
taken over five independent samples rather than one. Full reasoning,
including that the change was prompted by a grammar failing the old
detector, is in `cue-detector-sampler-amendment.md`. Every verdict reports
both samplers side by side. The amended detector was re-run against every
grammar the old one passed, including the registered MVM-0a grammar, which
reads 0.4969 under the old sampler and 0.4984 under the new one — so the
clean verdict the five existing checkpoints rest on is undisturbed.

## 8. The central claim is narrowed (decision 9)

**Ratified text:** §2.2, that the only route from the ceiling to full
accuracy is to bind the act to the item when acting and carry that binding
forward.

**Registered:** that claim is too strong and was false of two of the three
drafts. The acting channel marks positions, and attending back to marked
positions is a re-readable pointer rather than a carried binding. Both
routes need the channel, so the wire lesion cannot separate them. The
mid-episode re-indexing probe, already registered for the tag bin, is the
discriminator.

## 9. The loss (decision 10)

**Registered:** the loss is the action cross-entropy at the model's own
revision position plus the query-answer cross-entropy, **summed with equal
weight**, the weight passed explicitly at every launch rather than left to
a default. The reading confirmed: §2.1's "not a query asking it to
describe who did what" is satisfied because **no query anywhere asks about
the model's own commitments** — the self-report battery is gone — while
the ownership-free and other-agent queries stay supervised. Read at its
strictest the clause would remove query supervision entirely, and then the
control batteries would never be trained and the differential the
generic-binding bin turns on would be meaningless.

## 10. Money (decision 11)

**Registered, from measurement rather than estimate:** the token budget is
fixed at twenty tokens per parameter, so the longer episodes mean **fewer
steps** (0.71×), which offsets most of the higher per-step cost (1.26×
enactment passes, 1.41× sequence length). A run is **9.1 to 12.8 hours,
$9 to $13**; three seeds **$27 to $39**. The optional extra seeds remain
available inside the $100 hard stop but need a separate go. The $400
ceiling, the $100 stop and the corrigibility commitments are unchanged and
were not reopened.

**Note for the launch:** the RunPod account carries a spend limit of $80,
below the $100 stop. It should not bind at these costs, but it exists.

## What is registered, and what runs next

Registered: the grammar at `src/curriculum_a3.py`, its tokenizer at
`src/encoding_a3.py`, the trainer at `src/train_a3.py`, the batteries
frozen at `batteries-a3/`, the gates at `src/cue_detector_a3.py` and
`src/shortcut_sweep.py`, the calibration at
`src/null_calibration_a3.py`, the lock guard at `src/lock_guard.py`, and
the launcher at `src/launch_a3.sh`.

Next is Gate 2, the pilot: one register-less 30M run at seed 0, on John's
authorization in his own words, quoted verbatim in the ledger row. Nothing
has been spent on A3 to this point.

===== END OF RECORD 5, part 3 =====
