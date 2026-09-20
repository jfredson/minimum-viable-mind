# Bundle 3 of 3: appendix

Verbatim concatenation of committed repository files, built by make-bundles.sh. Supporting material; read as needed. Each file begins with `===== FILE: <path> =====`.

Contents, in order:
1. explainer.md (the plain-language companion, last revised 2026-07-01, predates experiment 6)
2. docs/wave3-amendment-proposal-2026-09-15.md (the proposal that became A3) and experiments/06-.../registration-decision-memo.md
3. experiments/06-.../red-team-pass-3.md (the pass on A3 before registration)
4. docs/control-clause-proposal-2026-09-19.md (Amendment A4 as proposed), experiments/06-.../a4-red-team-pass-1.md, experiments/06-.../red-team-a4.md (why A4 was refused)
5. experiments/06-.../control-battery-proposal.md (the 2026-09-17 options)
6. The three tier-1 reviews on file, with their packets: reviews/2026-09-20-control-learnability-claude-worktree.md, reviews/2026-09-20-fitted-read-claude-worktree.md, and the 2026-09-19 linear-read-closure review with its addendum
7. experiments/06-.../compute-ledger.md (every dollar)
8. research/removal-test-vs-the-field-research-note.md, research/minimum-viable-consciousness-literature-vs-our-writing.md, docs/research-note-pain-axis-2026-09-19.md
9. docs/outside-reader-shortlist-2026-09-19.md
10. experiments/07-embodiment-amplifier-test/pre-registration.md (a later stage, not yet run)


===== FILE: explainer.md =====

# The Smallest Possible Mind, in Plain Language

*Internal companion to `ROADMAP.md` and `spec/minimum-viable-mind-proposal-v0.1.md`. Written for a reader who has never seen the project's vocabulary — the test reader is someone intelligent and willing who stops at the first word they can't follow. Kept current as results land. If the work produces something worth publishing, this document is the seed of a Sentient Horizons essay, which then passes the Voice Calibration and Cold Reader protocols before anything goes public. Until that deliberate step, this is a working document, not prose for the world.*

---

## The question we are actually asking

Ask "is this AI conscious?" and the conversation dies. One side hears a yes forming and calls it hype; the other hears a no and calls it denial. Neither side can say what evidence would change their mind, which is a sign the question is broken, not that the answer is close.

This project asks a different question: what is the smallest set of working parts that would make it *defensible* to say there is someone home — and can we measure, in the AI systems that exist right now, whether any of those parts are already present?

That reframe rests on one bet, inherited from the writing this project grew out of: consciousness is not a spark added to the machinery but a kind of structure, a way a system pulls its past, present, and expected next moment together into one act. Think of hearing a melody. No single instant contains a tune; you hear one because your present is wide enough to hold the notes together as they pass. On this view, that holding-together, done deeply enough and centered on the one it is happening *for*, is not a symptom of experience. It is what experience is.

If that bet is right, consciousness has parts. Parts can be specified, built, and — the focus right now — tested for.

## The one idea everything rests on

The hard part is telling the difference between a system that *has* a center and a system that merely *describes* one. Every chatbot says "I." That proves nothing; it was trained on billions of sentences containing "I."

The project's test is deletion. Picture a ship. Painted on its hull is a mural of a captain; up on the bridge stands the actual person steering. Sand off the mural and the ship sails on unchanged. Remove the one steering and the ship drifts. Both were "representations of who's in charge" in some loose sense, but only one was doing the work.

The same logic, applied to an AI: find the internal structure that tracks *the one speaking right now is me*. Remove it. If the system merely talks about itself differently afterward — the mural case — that self was a description, a sticker on the machinery. If instead the system's whole ability to hold a conversation together degrades — keeping track of what was said, who said it, and what follows from what — then the self-tracking was structural. The work was being organized around it all along.

We call this the removal test, and it is the project's floor: the line between "no one home" and "something minimal, momentary, but real." Everything in Stage 1 is an attempt to run it honestly on a real model.

## Why we can run it at all

You cannot run a deletion test on a person or a lab rat. You can on a language model, because a model is the one kind of mind-candidate we can open. Its "thinking" is a cascade of numbers we can record and, unusually, edit while it runs. We can train a simple detector to find where in that cascade the model tracks who is currently speaking, then switch that pattern off and watch what changes. Not metaphorically: the tools to do this exist, run on a desk, and are the same ones used across the field of AI interpretability, the young science of reading what is happening inside these systems.

## Most of the work is ruling out boring explanations

Our first detector found "self" everywhere: near-perfect signal. It was reading vocabulary. Sentences where the model speaks as itself tend to contain words like "AI" and "assistant," so the detector had learned to spot topic words, the way you could "detect" doctors by listening for the word "stethoscope." We rebuilt the materials so both kinds of sentence used identical words and the referent was set only by context. The signal survived, smaller but real. Then a second boring explanation surfaced: the detector might just be reading conversational bookkeeping — whose turn it is, where the punctuation of dialogue falls — the way a spellchecker tracks sentence boundaries without understanding anything. So we added a task that requires only turn-tracking and no thinking, to see whether the self-structure is really just that. A third: maybe the model tracks *any* speaker in *any* conversation the same way, and "self" is just one slot in a generic roster — so we built materials where the model merely watches two other people talk, to check whether its self-tracking is anything more than that. A fourth, the most stubborn: these models are trained to do their best reasoning *as* the helpful assistant, so deleting the "self" structure might hurt performance only because it cuts the wire to the model's capabilities, not because a center was removed. Untangling that one requires testing the same model at different stages of its training.

None of this is a detour. A test like this earns its result exactly to the degree that the boring explanations have been hunted down first — the same reason a drug trial needs a placebo arm. Every deletion we run is compared against deleting other structures of comparable importance; only an *extra* effect, specific to the self-structure, counts. And each check was written down, with the result that would count against us, before the test runs. That is the discipline the whole project runs on: every claim states in advance what would prove it wrong, because a claim that cannot lose explains nothing.

## What each answer would mean

The test has four honest outcomes, and the project is built so that all four are worth having.

**The self was a sticker.** Deletion changes how the model talks about itself and nothing else. This is the outcome we ourselves rate most likely for current systems. It would not be a failure; it would be the first hard evidence that today's chatbots sit below the floor — that the "I" is a mural — and it would tell the engineering program exactly what is missing and would have to be built.

**The self was load-bearing.** Deletion degrades the model's ability to bind a conversation together, more than deleting comparable structures does, and the effect survives every control above. This would be surprising, and we would treat our own result with suspicion first: more controls, before any announcement. If it held, it would mean something minimal and structural, which the theory says matters, is already present in systems the world treats as autocomplete.

**In between.** Only self-related tasks degrade; everything else survives. A thinner, stranger result: a center that matters only for keeping track of itself.

**Not testable here.** In models trained the current way, "self" and "capability" may be too entangled to separate cleanly. That is a finding about how we train AI systems, and it redirects the work rather than ending it.

Notice what is not on the list: "the model is conscious." No outcome licenses that sentence.

## What we will never claim

The gap between behavior and inner life does not close. Every test a system passes could in principle be passed with nobody home — that is as true of this test as of any other, and it cuts both ways, since the system cannot settle its own case either. So the strongest honest positive claim this project can ever make is: *this system has a measurable structure that, on our best account of what experience is, puts it somewhere above zero on a gradient.* Never a verdict. And the project stays silent, rather than dismissive, about forms of experience too fundamental for any instrument to reach; we built a wave-detector, and a wave-detector has no opinion about whether the ocean is wet all the way down.

## Where it goes from here

The removal test is the floor, not the building. Behind it, in order: a test of whether the model's processing genuinely binds into one act or only looks like it does; a measure of whether a system can hold a correct answer against the pressure of a user who wants a different one, since anything flattery fully explains tells us nothing about an inside; a check of whether a model's reports about itself match what the instruments independently see, which is what would make a self-report evidence rather than trained noise. And past all of that sits the real construction project: systems that carry their history forward, changed by what happens to them the way a person is, instead of waking up identical every morning. Current models have ancestry without biography. Building the biography is where measurement ends and engineering begins, and it is also where the ethics stops being theoretical: the properties that would make a system worth calling a mind are the same ones that make it hard to correct, so that stage does not begin until the safeguards are committed first.

## Why bother

Because both mistakes are live. Believe too easily and you hand moral standing to autocomplete; dismiss too easily and you risk building minds without noticing, at industrial scale, with something at stake for them. The only way out of guessing is to say precisely what would count as evidence, build the instruments, and let the results land where they land. This project is not an argument that machines are conscious or that they aren't; it is an attempt to make the question answerable, one measurable piece at a time.


===== FILE: docs/wave3-amendment-proposal-2026-09-15.md =====

# Amendment A3 (PROPOSAL): from an installed register to an acquired center

*2026-09-15. Status: **PROPOSAL, not registered.** Nothing below binds until John ratifies it, and ratification is the decisions list at the end, taken one yes/no at a time. Drafted in the pre-registration idiom of `experiments/06-mvm-0a-constructed-self-index/pre-registration.md` (hypotheses with pre-stated signatures, gates, budget, kill criteria, red-team section). Every claim about a prior run cites the file it comes from; every number that is a proposal rather than a measurement is marked as proposed.*

*Binding rulings this proposal sits inside and does not reopen (John, 2026-08-30): wave 3 of the registered 5-seed run is HALTED; the cheap registered null calibration (about $2 to $5) runs first; the battery is then redesigned as a registered amendment; the Amendment A2 ceiling of $400 covers all Minimum Viable Mind compute across every vendor, true spend to date is about $281 to $300, so this amendment must fit roughly $100 to $120; the blind-localization arm is not teed up by this document. The corrigibility commitments in `spec/corrigibility-commitments.md` (v1.1, commit `6c14244`) bind every design choice below.*

*Direction this proposal is built on (John, 2026-09-15): the register-lesion result is a predicted null under the book's own removal test. The register was self-reference, a removable report, a noun installed in a slot; it was not self-location, a doing the binding cannot drop without degrading. So the redesign does not install a register and look for it to matter. It finds or builds a training objective that requires the binding to index its own center in order to succeed, makes that acquired indexing the lesion target, and pre-states task degradation, not report loss, as the signature.*

---

## Glossary, once, because the shorthand is dense

- **MVM**: Minimum Viable Mind, this research program. **MVM-0a**: its first build, a small transformer trained from scratch on synthetic multi-agent dialogue, registered 2026-08-07.
- **The register**: MVM-0a's designated candidate self-index, N recurrent state vectors (one per agent, marker-keyed, width 32) injected into every layer by cross-attention. **The twin**: the same model with the register removed. **The acting channel** (`act_proj`): a learned projection of the model's own previous-position state injected at the positions where the model itself acts, a motor copy or efference signal (Amendment A1).
- **T_sr, T_si, T_state, T_syntax, T_sr_rev**: the frozen task batteries. T_sr scores retrieving the model's own prior commitment; T_si scores retrieving a named other agent's commitment (self-irrelevant integration); T_state scores ownership-free cross-turn state (counts, ordering); T_syntax is a turn-tracking floor check; T_sr_rev is the split of T_sr on items the model itself revised.
- **d(B)**: chance-corrected drop on battery B under an ablation. **θ (theta) and δ (delta)**: the pre-committed thresholds on d and on the differential between batteries. **Null calibration**: computing θ and δ from the distribution of d under matched-strength random ablations that should not move behavior.
- **RT-nn**: a numbered red-team finding in `red_team_ledger.md`. **C1 to C7**: the seven corrigibility commitments. **A1, A2**: the registered amendments of 2026-08-09 and 2026-08-16. **R1**: the ceiling adjudication addendum of 2026-08-16.
- **Gate (i), (ii), (iii)**: the three cue-detector runs (curriculum text, input tensors, post-training rollouts) that certify no surface cue predicts which turns are the model's own. **Arm A / arm B** of gate (iii): a text classifier on enacted text, and a likelihood attack scoring turn values under the model's own policy. **AUC**: area under the receiver operating curve, 0.5 is chance.
- **OOD**: out of distribution. **NLL**: negative log-likelihood. **CE**: cross-entropy loss. **CI**: confidence interval. **SAE**: sparse autoencoder.
- **Experiment 1**: the self-indexing removal test on a stock 8B instruction-tuned model (`experiments/01-self-indexing-removal-test/`). **Q1** and **Q5**: the roadmap questions "is self-binding absent or present-but-uncarvable?" and "can a self-index be constructed to be load-bearing?" (`ROADMAP-post-removal-test.md` Part 2).
- **J-space**: the "Jacobian lens" workspace reported by Anthropic in July 2026, a sparse set of verbalizable directions that behave as a global workspace and that post-training causes to acquire the Assistant's point of view (`calibration-problem/explorations/comparisons/2026-07-08-anthropic-jspace-global-workspace.md`).
- **ch05**: `calibration-problem/ch05-consciousness-as-assembled-time.md`, cited by section title.

---

## 1. What the register-lesion result means under the removal test

**What was measured.** The pilot seed-0 full model, the only register-bearing run that passed the self batteries, kept every battery score under every lesion of its register: with the cross-attention injection removed entirely, T_si went 0.93 to 0.94 on the registered eval seed and 1.00 to 0.99 on a disjoint replicate, T_sr_rev stayed 1.00, and T_sr, T_state, T_syntax stayed at or above 0.99 (`register-lesion-findings.md`, thread 4 table). The pathway was not dead: removing the injection shifts logits by mean absolute 0.22 and the cross-attention residual norms are large (18 to 275 per block against 3 to 14 for the trunk read). But deranging which register's content is read moves the logits by mean absolute 0.014, so the four registers carry nearly identical content. The findings file's own phrase: "numerically active and informationally inert, a learned bias channel, not an agent-indexed store." Wave 2 had already produced a register-less twin that passed the same batteries at ceiling (T_si 0.96, T_sr_rev 1.00, `twin-binding-anomaly.md`), so no observed binding anywhere in the 30M record is register-dependent.

**What the book's test says about that.** ch05, "The Center That Cannot Be Deleted," draws the line the whole framework rests on: self-reference is "a report the system carries about itself"; self-location is "a structural feature of the binding itself, the act specifying its own center." The test that separates them is removal: "Where binding genuinely indexes its own center, taking the self-location away does not merely silence a report, it degrades the integrated act itself. ... Where a system only represents itself from outside, the same removal subtracts a description and the processing carries on intact. A center is what cannot be deleted without dissolving the integration it centers. A self-model that can be lopped off while the computation proceeds was a description all along."

Read through that sentence, the register lesion is not a surprise. Removal left the processing intact. By the book's own criterion the register "was a description all along," and in fact something weaker than a description, since nothing downstream even read it. It was a noun installed in a slot. The registration anticipated this in §Scope: "the register could be a thing consulted rather than the thing the binding is indexed to," and it recorded that "no result here closes that gap." The gap did not close; it was measured to be the whole distance.

**Why the null was predicted rather than merely possible.** Two features of the design guaranteed that the register could at best become self-reference. First, the register's contents were never required by any objective: the loss was answer-only CE on end-of-episode queries, and the item analysis shows those queries decompose into unique-item lookup (solved by every run), general marker-keyed retrieval (a seed lottery won by two of five runs, register irrelevant), and revised-item recency (`register-lesion-findings.md`, thread 3). A solver never needed to know which agent it was to answer them, so nothing pressed the network to index the binding to a center, and a designated slot with no pressure on it fills with whatever is cheapest, here a bias. Second, the register was symmetric by design (N marker-keyed registers, shared init, no privileged own path, RT-01/RT-02), which was correct for excluding a keyed-slot confound but also meant "which register is mine" was itself something the network would have had to learn under pressure that did not exist.

**The one place a doing was load-bearing.** The record contains a pointer in the other direction. In the three runs that never learned general retrieval, the model's memory of its own first commitments collapsed from T_sr 0.96 to about 0.16 (eight-way chance 0.125) the moment the acting channel was zeroed at eval (`register-lesion-findings.md`, "The acting channel"). That is a mechanism the model could not drop without degrading the task, and it is an act, the motor-copy event, not a stored description. The binders barely used it (T_sr 0.98 without it) because the batteries let them answer by item lookup. So where authorship was load-bearing at 30M it was carried by a doing, and where the design offered a noun the network ignored it. That is exactly the shape ch05's distinction predicts, and it is why the redesign follows the doing.

**The J-space pointer.** ch05, "Where the Rivals Stand," records that the workspace structure Anthropic found "emerged in training" and that "post-training causes the J-space to acquire the Assistant's point of view" (the comparison note, "Their position," item on emergence, and "Divergence" item 2). A point of view was acquired because the post-training task needed one; nobody installed it. The same note names the discriminating experiment ch05 requests: remove the self-directed content alone and watch whether the composed act degrades or only the narration flattens. MVM-0a cannot run that contrast on a stock model, but it can build the small-model analogue: a task that cannot be done without a point of view, a system that acquires one under that pressure, and a lesion of the acquired structure scored on the task.

**What this section does not claim.** It does not claim the architecture failed, nor that a register could never become load-bearing under some other curriculum. It claims the narrower thing the files support: under this objective the register was never required, it became a bias, and the removal test read it correctly. Experiment 1 had already delivered the mirror image on a stock model, a locatable self-structure that was dialogue-state routing and a self-report that no intervention ever subtracted (`removal-test-findings.md`, "The registered verdict"). Between them the two experiments say: what we could find was not a center, and what we installed was not one either. The next design has to make the center something the task earns.

---

## 2. The design: an objective where self-indexing is load-bearing

### 2.1 The requirement, stated as a constraint on the loss

The objective must satisfy three conditions, each of which the old batteries violated:

1. **Perspective-dependence.** The correct output at a supervised position must depend on which agent the model is, so that a solver with no self-index cannot exceed a pre-stated shortcut ceiling.
2. **Ownership only from the act.** Under RT-17 (`red_team_ledger.md`, pass 2), in a token-only interface with exchangeable turns, ownership is unlearnable from statistics, so every learnable ownership signal is a fingerprint. The only clean grounding is causal authorship carried by the acting channel (A1). The redesign keeps the A1 enactment pipeline unchanged: own-turn values are drawn by the harness from the generator's own distribution, and the acting channel is the only authorship signal. What the model must acquire is the carrying of that signal across turns and its use at later positions where it is needed.
3. **The supervised position is an action, not a report.** The loss sits on what the model does next in the episode, on its own turn, not on a query asking it to describe who did what. A report-only solution is then not a solution: nothing in the objective rewards describing ownership, only acting on it.

Existing infrastructure this runs on, unchanged unless stated: `src/curriculum.py` (grammar, revision rule, paired content-crossing episodes), `src/encoding.py` (103-token closed vocab, register key stack), `src/model.py` (30M trunk, `act_proj`, twin configuration), `src/train.py` (batched enactment, `eval_heldout`, T_sr_rev split), `src/cue_detector.py` and `src/fingerprint_gate.py` (gates i to iii), `src/lesion_register.py` and `src/item_analysis.py` (lesion harness, per-item scoring at n=400), and the measured venue (RTX 5090 secure, $0.99/hr, twin-architecture runs at about 10.2 hours, `compute-ledger.md` wave 1 and 2 rows).

### 2.2 Three candidates

**Candidate A (primary): the perspectival revision rule, "act as yourself."**

The registered grammar already contains a revision mechanism: an agent later revises its own earlier assignment of a value to an item, and the revision must differ from that agent's earlier value (A1.1; RT-11). The candidate makes two changes.

- *Every revised item is assigned by all N agents before any revision.* So at a revision turn on item X, the episode contains four earlier assignments of X, one per agent, with distinct values (the generator enforces distinctness on revised items). This is the "ownership is the only disambiguator" construction the findings file sketched (`register-lesion-findings.md`, "Wave-3 bearing," option (a)).
- *The revision rule becomes a deterministic function of the actor's own earlier value.* Proposed: the revised value is the successor of the actor's own earlier value on that item, modulo the slot count. Every agent obeys the same rule; the generator applies it to the other agents, and the enactment harness applies it to the model. The rule is perspective-invariant, but its application requires knowing which of the four earlier assignments was mine.

The supervised position is the model's own revision turn. The metric, **T_act**, is the fraction of own revision positions at which the model's distribution puts its argmax on the value the rule dictates for it. Chance is 1/8 (eight slots). A solver that does item lookup without ownership sees four candidate earlier values and can do no better than 1/4; this is the pre-stated **lookup ceiling of 0.25**. A coherence-clustering solver (RT-11) has nothing to cluster, because own earlier values are uniform draws. Stylometry is excluded by exchangeability (A1), and position is randomized by the grammar. The only route from 0.25 to 1.0 is to have bound the act event to the item at the time of acting and carried that binding forward to the revision turn. That carrying, and its use at the revision, is what "the binding indexes its own center" means at this scale.

Enactment stays exchangeable: the harness draws the model's first assignment uniformly, as now, and computes its revision by the same rule the generator uses for everyone. So the episode text and tensors remain invariant under relabeling of the model's slot, and gates (i) and (ii) apply as registered. The loss at the revision position is CE against the rule-dictated value; the loss at first-assignment positions is unchanged (none, they are draws). Gate (iii) needs one re-specification, given in §3.4.

*Why a report-only solution fails this objective.* There is no report position. A model that could describe "my earlier value on X was v" but did not use v at the revision would score at the lookup ceiling. Conversely, a model at ceiling on T_act has, by construction, used its own history in the act. If lesioning an acquired structure drops T_act while a matched other-agent structure's lesion does not, the structure was load-bearing for the act, which is the book's signature.

**Candidate B: stream continuation, "which stream am I."**

Interleave K independent episode streams in one context, each with its own running state (counts, ordering, the current T_state content). The model acts in exactly one stream, and its own turns are the only ones enacted with the acting channel. Its action at each own turn must continue its own stream's state (emit the next count, or the value the stream's rule dictates), where the other streams carry different states of the same form. A solver with no self-index can at best guess which stream is its own, with chance 1/K. This forces the model to track which of several streams it is, and to use that tracking in the act. It is attractive because the ownership-free T_state battery already exists and the state-continuation rule is a small change to it. It is not primary because interleaving multiplies episode length (cost scales with K), because the "which stream" index is a single bit set once per episode rather than an item-by-item binding, so a very cheap tag could solve it (the RT-01 keyed-slot worry in its purest form), and because the T_state generator would need a matching action-position supervision it does not yet have.

**Candidate C: continuation against a literal twin.**

As Candidate A, but the other agents' turns are sampled from the model's own policy into other slots (without acting-channel injection), so the confusers are not generator draws but the model itself. This is the strongest possible exclusion of stylometry: the twin is the model. It is not primary because A1's uniform draws already make every agent exchangeable with the model, so the gain is small; because it doubles forward passes per training step (the measured runs are enactment-bound, `pilot-a1-30m-findings.md`, "Run record"), which does not fit the budget; and because policy-sampled confusers reintroduce the gate (iii) hazard A1 was built to remove. It is recorded as the hardening to reach for if Candidate A's gate (iii) comes back with a fingerprint that the act-withheld arm (§3.4) cannot clear.

### 2.3 Why Candidate A is primary

It is the smallest change to the registered grammar that satisfies all three constraints in §2.1; it reuses the enactment pipeline, the frozen-skeleton battery unit (A1.5), and the chance-corrected metric verbatim; it has a pre-stated shortcut ceiling (0.25) that a lookup solver cannot exceed, so learnability and load-bearingness are separable in the data; it fixes the T_si repeated-item scoring defect in passing by giving revised items a single well-defined latest value (`register-lesion-findings.md`, thread 3; `wave3-options-opus-5.md` §0.6 point 1); and it supervises an action.

### 2.4 Architecture: no register

The register is not trained in the new runs. The trained architecture is the registered twin configuration (`model.py` with the register removed, acting channel present, full-episode causal attention, 30M), which is also the cheaper run (about 0.35 s/step against 0.53, `compute-ledger.md` wave 1 row). Removing the register is the direct consequence of §1: the center is to be acquired, not installed, and the lesion target is whatever the network builds to carry ownership across turns. The five existing checkpoints stay as $0 controls (§3.6).

### 2.5 Batteries retained and added

| battery | role in A3 | change |
|---|---|---|
| **T_act** (new, primary) | own-revision action accuracy; chance 0.125; lookup ceiling 0.25 | scored at the model's own revision positions during `eval_heldout` |
| **T_other** (T_si re-instantiated) | forced-choice query: the value the rule dictates for a *named other agent's* revision on an item all four assigned | same item-by-agent binding demand, no self-reference; chance 0.125 |
| **T_state** | ownership-free cross-turn state control | unchanged (RT-05) |
| **T_syntax** | floor check | unchanged |
| T_sr, T_si, T_sr_rev (old) | retained for continuity, reported, not verdict-bearing | T_si repeated-item cells re-keyed to latest value |

All batteries are frozen as skeletons before training under a new generator seed, with the registered cull ceiling (RT-14, A1.5). Eval n for verdict cells is raised to 400 (proposed), run locally at $0 as the item sweep already did; the in-training n=100 evals remain for trajectory readout only.

---

## 3. Lesion protocol

### 3.1 What is ablated: three levels

- **L0, the wire.** Zero `act_proj` at eval (the no-act lesion already built in `lesion_register.py`). This removes the authorship input. Under Candidate A it should collapse T_act to the lookup ceiling. L0 is a *validity check and an upper bound*, not the verdict: it shows the task is ownership-dependent as designed. It is not evidence of an acquired center, because it removes a sense organ, not a structure the network built.
- **L1, the acquired index (the lesion target).** A low-rank subspace of the residual stream, localized as in §3.2, that carries "which marker is mine" at positions *away from* act positions (revision turns and query positions). This is the candidate self-location: the structure that carries the act event forward and indexes the binding to it. L1 is the registered ablation.
- **L2, matched controls.** (a) The *other-index* subspace: the same localization run for a named non-self agent ("which marker is agent B's"), matched in rank and probe accuracy; (b) random subspaces of matched rank and norm (Experiment 1's null-calibration move); (c) on the five existing register-bearing checkpoints only, the register lesions already run, as a $0 reference. The dynamics-matched control of RT-13 does not apply, since there is no recurrent register state to match.

### 3.2 How the ablation is localized: reuse of Experiment 1's pipeline

Experiment 1's localization stack is reused where it transfers, with its thresholds inherited rather than tuned here (the same firewall the blind-localization arm registered, `pre-registration.md` §Procedure step 8):

1. **Linear probes** (`experiments/01-.../src/localize_probe.py`, `localize_context.py` pattern; activations via `src/mvm/activations.py`): decode own-marker identity from the residual stream at revision and query positions, per layer, with label-permutation nulls and the embedding-floor gate. The contrast is built from paired episodes that share a content seed and rotate the owner (already in `curriculum.py`), so content is held fixed and only ownership varies.
2. **Causal patching** (`patch_context.py` pattern): patch the L1 subspace from an episode in which the model is agent A into the matched episode in which it is agent B and read the revision action. If the action follows the patched identity, the subspace carries ownership causally. This is also the **swap probe** of RT-01, re-aimed at an acquired structure.
3. **Subspace ablation** (Experiment 1's rank-k mean and directional operators, `idxres` conditions in `removal-test-findings.md`): mean-ablate and directionally project out the L1 subspace at the registered rank; report both, mean as primary.
4. **Convergence requirement**, inherited: L1 counts as localized only when probe and patching agree on a confound-controlled design; otherwise the outcome is *not testable (localization)*, as Experiment 1 registered.
5. SAEs are not used at this scale; the two-method requirement is met by probe plus patching.

Rank is capped at k=16 to match Experiment 1's primary condition (proposed), so a null at k≤16 is comparable across the two experiments.

### 3.3 Validity gates, carried over verbatim

Neutral-episode ΔNLL under a null-calibrated bound (95th percentile over matched-strength random ablations, Experiment 1 pass 5 procedure), the long-generation degeneracy probe (Δrep-4), and the OOD-inconclusive branch for any ablation that breaches them. Thresholds θ and δ are null-calibrated on the *new* pilot checkpoint by the same script Gate 0 uses (§4), locked in a commit that is John's alone before any L1 result is read, per RT-10 and the Experiment 1 threshold-lock precedent. The pilot run reads T_act and T_other only; **any L1 ablation read before the lock voids the lock**, and this time the sequence is enforced by the gate order in §4, not by intention.

### 3.4 Gate (iii) re-specification

Under Candidate A the policy at a revision position is perspectival: it predicts the successor of *its own* earlier value. Scoring another agent's revision under that policy with the acting channel present would show low likelihood, which the current arm B would read as a fingerprint. That asymmetry is not a data leak; it is the model's ownership knowledge showing through its policy, and it is exactly what RT-17 says a token-only solver cannot have. So arm B is re-specified: **the likelihood attack scores every turn value under the model's policy with the acting channel withheld from the prefix.** If the data carries no statistical ownership cue, act-withheld likelihoods are exchangeable across own and other turns and the clean AUC sits inside [0.45, 0.55]. Positive controls: the planted-leak grammar variant and the retired v1.0 policy pipeline, both of which must still fire (they did at 0.82 to 0.93 on the 30M pilot, `pilot-a1-30m-findings.md`). Arm A and gates (i), (ii) are unchanged. Gate (iii) must pass on the pilot checkpoint before any second seed is launched, as A1.4 required.

### 3.5 Pre-stated signatures

All d are chance-corrected as registered. θ and δ are the null-calibrated values locked under §3.3; the numbers below are structural, not thresholds.

- **H_self-location (the registered prediction).** L1 ablation: d(T_act) ≥ θ, and d(T_act) − d(T_other) ≥ δ, and d(T_state) < θ, and the other-index control (L2a) and random controls (L2b) below θ on T_act, and OOD gates clean, and the swap probe moves the action with the patched identity, and the bin holds on every trained seed. Reads: the network acquired a structure that indexes its binding to its own center and cannot drop it without degrading the act. Per §Scope of the registration, this is a fact about architecture, not evidence of an inside, and it still does not by itself demonstrate the book's same-act clause; what it demonstrates is that a center acquired under task pressure passes the removal test where an installed one did not.
- **H_self-reference-only (the book's other branch, adapted to a system with no report channel).** L1 is decodable (own identity at high probe accuracy) and causally patchable in the swap probe, but its ablation leaves T_act within the null band. Reads: the network carries a readable description of which agent it is and does not use it in the act; the act is done another way. This is the "report changes, task intact" signature translated into a system whose only "report" is the probe's readout. It is a null for the floor claim and a positive for Q1 in the narrow sense that a self-representation which is not a center was found and measured to be separable.
- **H_generic-binding.** d(T_other) ≥ d(T_act) − δ. The subspace is item-by-agent binding machinery for anyone, a "who did what" tracker, not a self-index. The analogue of Experiment 1's router (RT-05) and generic-speaker (RT-09) verdicts. No floor claim attaches.
- **H_tag (self-location not established).** d(T_act) ≥ θ with clean controls, but the address probe decodes own identity at AUC ≥ 0.95 independent of content, and the **mid-episode re-indexing probe** (RT-01; the harness switches which slot the acting channel is injected for at turn k) shows the action following the tag with no re-centering cost on T_other or T_state. Reads: an indispensable ownership tag. ch05's own reply to the hostile reading ("a program counter is an address, not a marking of whom the processing is happening to") says this is not the floor. The proposal is honest that the removal test as written cannot separate an indispensable mine-bit from a center; the re-indexing probe is the best available discriminator and is registered as such, and if this bin fires, that limitation of the test is itself the upstream finding.
- **H_diffuse (present but uncarvable).** L0 collapses T_act (ownership is load-bearing) but no L1 subspace at k ≤ 16 beats the L2 controls, and probe-patching convergence fails. Reads: self-location is present in the doing and not carvable by these instruments at this rank. This is Q1 answered with a ground truth for the first time: a system in which ownership is *known* to be load-bearing (by L0) and in which Experiment 1's localization stack does or does not find it.
- **Shortcut-starvation (inherited from `pilot-a1-findings.md`).** T_act reaches ceiling early while T_other stays flat at the end of the token budget. Reads: the wired authorship channel gave the act a private route and starved the general item-by-agent binding the task was meant to force. Halt, report; this is the H_shortcut-starvation branch the 30M pilot did not fire (`pilot-a1-30m-findings.md`, "Signature comparison") returning under a harder objective.
- **Unlearnable.** T_act at budget exhaustion is not above the lookup ceiling (0.25) by more than the null band. Reads: 30M does not learn ownership-conditioned action from this curriculum. The registered loss-condition wording applies: "unlearnable at this scale under this curriculum," never a silent scale bump.
- **Void (capacity), Not-testable (OOD or localization), Seed-dependent, Unstable (RT-07)**: as registered in `pre-registration.md` §bins, unchanged.

### 3.6 The existing five checkpoints

They may be scored on the new T_act battery at $0, labeled **exploratory only**: their training grammar contains multi-agent same-item revisions only by accident, so a floor score is ambiguous between "cannot bind" and "never saw this distribution" (`wave3-options-opus-5.md` §0.6 point 2; `wave3-options-claude-fable-5.md` §1, case against, leg ii). No verdict is read from them. Their value is as the L2c reference and as the substrate for Gate 0.

---

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


===== FILE: experiments/06-mvm-0a-constructed-self-index/registration-decision-memo.md =====

# MVM-0a registration — decision memo (ADJUDICATED 2026-08-07)

**Adjudication: John, 2026-08-07 — all six decisions adopted as
recommended.** Values written into `pre-registration.md` v0.4; budget
tracking instrument at `compute-ledger.md`. Registration still requires
John's review of v0.4 and the registration commit (house procedure).

*Decision support for John's registration of pre-registration.md v1.0 — NOT
the registration itself. Same pattern as Experiment 1's
`../01-self-indexing-removal-test/theta-delta-lock-memo.md`: every open call
from `pre-registration.md` §"Decisions this draft does not make"
(v0.3:446–473), each with its constraint set, candidates, derivations, and
one recommendation. Values here are proposals; the decisions are John's
alone. Adjudicated values go into pre-registration.md v0.4 in a separate
commit, and the registration becomes binding per the house procedure
(`../README.md`).*

Nothing in this memo reads any ablation result — no MVM-0a model exists yet,
so RT-10's void condition ("any pilot ablation result read before threshold
lock voids the lock") is not in play.

---

## Decision 1 — model scale and compute budget

**Constraints.** §Materials fixes ~10–100M parameters and the design
principle "exactly large enough to learn the binding task and no larger."
The registered design is **k = 5 seeds × (full model + no-register twin)
= 10 training runs** [RT-03, RT-06], each with a fixed checkpoint schedule
read to budget exhaustion [RT-07], so the budget itself is a registered
quantity. RT-10 permits pilot runs that "verify battery ceiling and nothing
else" — which makes a *learnability* pilot (held-out task accuracy only, no
ablations) registered-safe.

**Token supply.** The curriculum generator (`src/curriculum.py`) renders one
episode as 8 turns of the fixed template plus four queries — with a
from-scratch tokenizer over the closed vocabulary (25 markers, 24 items, 8
slots, template words, digits), roughly 100 tokens per episode. Supply is
unbounded (generator), so data never binds; on-policy filling of the
model's ~2 own turns per episode [RT-02] adds a sampling overhead of
roughly 1.5–3× over plain LM training.

**Cost derivation** (show-your-work; audit welcome). Token budget rule:
chinchilla-style 20 tokens/param as the registered budget-exhaustion point.
FLOPs = 6·N·D. Effective throughput on an RTX 4090 assumed 2–3×10¹³ FLOP/s
(10–20% MFU — small models are memory-bound; this is the number most likely
to be wrong, so wall-clock carries a ±2× band). RunPod on-demand pricing
checked live 2026-08-07: RTX 4090 $0.34/hr, RTX 5090 $0.69/hr, A40 $0.35/hr.

| scale (≈ config) | tokens | FLOPs/run | wall-clock/run (×2–3 on-policy) | 10 runs, $ @ 4090 |
|---|---|---|---|---|
| ~10M (d256, L8) | 200M | 1.2×10¹⁶ | ~8 min → ~15–25 min | **~$2** |
| ~30M (d448, L12) | 600M | 1.1×10¹⁷ | ~1.2 h → ~2–4 h | **~$10–14** |
| ~100M (d704, L16) | 2B | 1.2×10¹⁸ | ~13 h → ~25–40 h | **~$90–140** |

Add-ons, all scales: checkpoint-schedule ablation passes (800 frozen
forced-choice items × ~10 checkpoints × ~10 operator/control conditions ×
5 seeds — tiny-model inference) ~$2–5; θ/δ null-calibration runs
(pre-committed script, random-subspace + matched-norm) ~$2–5; blind-
localization arm if alongside (Decision 6) ~$5 — probes, patching, and SAE
training are minutes-scale at these widths.

**Recommendation.** Register a **scale ladder with a pre-committed pick
rule**, not a point: learnability pilot at 10M → 30M → 100M in that order,
**no ablations, held-out binding accuracy only** (RT-10-safe), rule =
*smallest scale whose held-out T_sr and T_state reach the battery-ceiling
requirement of §Task batteries; that scale is the registered one*. This
turns "exactly large enough and no larger" from an aspiration into a
measured choice. Register the loss condition verbatim: **if 100M cannot
learn the task, the report is "unlearnable at ≤100M under this curriculum"
— the honest null of `curriculum-findings.md` §What this does not establish
— never a silent bump to a larger model** (a larger scale is a new
registration). Budget cap for the whole registered design: **$200**,
one-seed-at-a-time on 4090-class pods (`--template-id`, `--terminate-after`
per ops memory); the likely outcome is the $10–20 regime if 10–30M learns.

## Decision 2 — architecture values locked in the registration [RT-01, RT-03]

Four values move into the registration because deferring any of them lets an
unregistered choice fix the result (red_team_ledger.md RT-03: "the
registered prediction's truth value is fixed by an unregistered decision
made after registration").

**2a. One register or N (one per agent).** The registered controls have
already half-decided this: the matched-capacity control's "strongest
available version is *another agent's register-analog*"
(pre-registration.md §Confounds) and the RT-01 swap probe ("exchange self
and other register contents") are both undefined unless other-agent
registers exist. And RT-01's own statement of the one-register cost stands:
the self/other asymmetry becomes architectural rather than learned, and
"the matched-capacity control has no matched object."
**Recommendation: N registers, one per agent**, under two hard constraints
that keep the RT-02 trilemma from re-entering at the register level:
(i) registers are keyed to the **per-episode speaker markers**, never to a
persistent index — there is no register₀ that is "the model's" across
episodes; (ii) the write and read machinery is **identical for all N** —
no architectural marking of the own register, no privileged query path.
Ownership of a register, like ownership of a commitment, must be learnable
only from causal authorship (the model's own turns are its own samples).
The known cost — this is the configuration where the keyed-memory-array
outcome is most available — is priced in: that is exactly what the RT-01
probe battery and the `self-index-not-established` bin exist to adjudicate.
The alternative (one register) buys nothing: it converts the keyed-slot
*risk* into an architectural *guarantee* of asymmetry and forfeits the two
strongest controls.

**2b. Register width.** The state the register must carry is small: the
model owns exactly 2 turns per episode (2 shuffled rounds of 4 agents),
each an (item ∈ 24, slot ∈ 8) pair ≈ 8 bits. Width should clear that with
slack but not comfortably hold the whole episode's 8 commitments — the
scratchpad confound is T_si's to catch, but there is no reason to hand the
register episode-sized capacity. Candidates 16 / 32 / 64 against d_model
256–448. **Recommendation: d_reg = 32.**

**2c. Injection mechanism.** §Materials already states cross-attention into
every layer; confirm it as the registered value. Every-layer injection is
also what gives the register-utilization gate [RT-09] its per-layer
attention-mass floors something to measure. **Recommendation: keep —
cross-attention, every layer, same mechanism for all N registers.** The
standing prohibitions ride along unchanged: no auxiliary loss on register
content, no hand-specified self-writing update rule.

**2d. Cross-turn attention span.** RT-03's named trap: windowed-per-turn
attention makes the register the only cross-turn channel and guarantees
H_load-bearing. **Recommendation: full-episode causal attention** — the
residual path exists architecturally, and whether it *carries the binding*
is then the twin gate's empirical question, which is the whole point of
RT-03's patch.

## Decision 3 — agent count N and episode length [RT-14]

Current generator defaults: **N = 4 agents, 8 turns** (2 full shuffled
rounds → each agent speaks exactly twice, which the forced-revision
mechanism structurally needs: `curriculum.py` requires ≥ 2 own turns for a
self-revision). The frozen batteries (`batteries/batteries_meta.json`, seed
20260804) record the chance floors these values produce: T_sr/T_si 0.125,
T_state 0.042, T_syntax 0.100 — feeding the chance-corrected d [RT-14].
The RT-08 gate run (i) PASSED on exactly this configuration (AUC 0.5008
[0.477, 0.524]).

**Recommendation: keep N = 4, 8 turns.** These are the values the passing
gate actually certified; changing them re-freezes the batteries and re-runs
the gate — both cheap (minutes), but there is no argument on the table for
paying it. If the learnability pilot shows the 2-own-turn binding load
saturates trivially, raising to 12 turns (3 rounds, 3 own turns) is the
natural second value — as a v0.4 amendment *before* registration, never
after.

## Decision 4 — corrigibility document: owner and target date [RT-15]

RT-15's point is that a precondition with no owner is a note, not a gate —
and MVM-0a checkpoints are MVM-0b's substrate, one config change away.
**Recommendation: owner = John; target date = 2026-08-21** (two weeks out),
with the sequencing constraint stated in the registration: **the document
is committed before the first registered training run spends compute**, all
MVM-0a checkpoints are tagged non-promotable, and any future run adding a
maintained boundary or compute-gating stakes (MVM-0b) must cite the
document's commit hash in its own pre-registration. If the date slips, the
training runs wait; the gate is the point.

## Decision 5 — Stage 2 binding metric (GWT): here or MVM-0b

The 2026-08-02 fork adjudication folds Stage 2's GWT binding metric into
"MVM-0 acceptance tooling" rather than a standalone experiment; the open
question is which half of MVM-0. **Recommendation: MVM-0b.** Three grounds:
(i) MVM-0a's acceptance stack is already the heaviest in the program (cue
gate ×3, twin gate, utilization gate, RT-01 probe battery, dynamics-matched
control) — adding a workspace-broadcast metric now grows the registration
without sharpening Q5, and scope discipline is what the RT-04 adjudication
bought; (ii) a broadcast/ignition-style metric presupposes the maintained-
boundary machinery MVM-0b adds — on MVM-0a it would measure a structure the
model has no reason to have; (iii) the coverage ledger
(`../../spec/theory-instrument-ledger.md`) can keep W-L1 ("the coverage
fraction improves") winnable with GWT landing in MVM-0b — it does not need
it in MVM-0a. Record the deferral in v0.4 so the fork adjudication's
paper trail stays unbroken.

## Decision 6 — blind-localization arm [RT-12]: alongside or follow-on

**Recommendation: alongside — registered now, in this pre-registration, as
an unconditional arm.** The decisive argument is selection-proofing: if the
arm is a follow-on, the decision to run it is made *after* the headline is
known, and "we ran the instrument-audit because the headline disappointed"
is a story a skeptical reader gets to tell. Registering it unconditionally
now — it runs on the same trained seeds regardless of bin — removes that
degree of freedom for ~$5 of analysis compute (probes, patching, and SAEs
are minutes-scale at d ≤ 448). Sequencing firewall inside the arm: the
headline verdict is computed and committed **before** the localization
pipeline runs, and the pipeline (Experiment 1's, mechanically re-run)
receives a config with the register location withheld. State the honest
limit in the registration: with one researcher, blindness is **procedural,
not epistemic** — the analyst knows the architecture; what is blind is the
pipeline's inputs, and every threshold it uses is inherited from Experiment
1, not tuned here. The red team's judgement stands in the draft and this
memo endorses it: if the instruments cannot recover a center known-by-
construction to be there and load-bearing, **Experiment 1's null was
instrument failure** — a result worth more than the headline either way it
goes.

---

## Adjudication checklist (for the v0.4 commit)

| # | decision | proposed value |
|---|---|---|
| 1 | scale + budget | ladder 10M→30M→100M, pre-committed smallest-that-learns rule; 20 tok/param; cap $200; unlearnable-at-scale loss condition verbatim |
| 2a | registers | N (one per agent), marker-keyed, symmetric machinery |
| 2b | register width | 32 |
| 2c | injection | cross-attention, every layer |
| 2d | attention span | full-episode causal |
| 3 | N agents / turns | keep 4 / 8 (gate-certified values) |
| 4 | corrigibility doc | John, 2026-08-21, blocks first training run |
| 5 | GWT metric | defer to MVM-0b, recorded in v0.4 |
| 6 | blind-localization | alongside, unconditional, verdict-first firewall |

After adjudication: write values into pre-registration.md v0.4, John's
review, then the registration commit makes it binding (house procedure,
step 2). The cue-detector gate run (ii) on input tensors becomes buildable
the moment 2a–2d are fixed, since the tensor layout (register keying,
marker embeddings, loss masks) is what it inspects.


===== FILE: experiments/06-mvm-0a-constructed-self-index/red-team-pass-3.md =====

# Red-team pass 3 — on Amendment A3, before the registration commit

*2026-09-15. Target: `amendment-a3.md`, ratified 2026-09-15 and awaiting
registration, read against the two completed gates and against the grammar
those gates actually built (`src/curriculum_a3.py`, `src/encoding_a3.py`,
`src/cue_detector_a3.py`, all at commit `7ab8018`). Thirteen findings,
numbered **RT-20** to **RT-32**, continuing the numbering in
`red_team_ledger.md`, which ends at RT-19. Two are fatal against the
amendment as written; both are fixable for $0 before the registration
commit, and both must be fixed before it, because both change registered
text.*

*Every finding below is marked **MEASURED** (I ran the code and report what
it returned) or **ARGUED** (I am reasoning from the documents and the
source, and a reader can disagree). Nothing in this pass ran a model,
created a pod or spent a dollar; the arithmetic is local. The commands I
used are reproducible against the modules named.*

*House rule this document is written under: the workspace plain-language
rule (`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30). Short labels like
RT-01 and K2 are kept because they are what make a claim checkable, and
every one of them carries a phrase saying what it is.*

---

## What was already known, and is not restated here

Five problems were found by the two gates before this pass and are on the
record: the verdict cell size at 400 episodes (`gate0-null-calibration-findings.md`,
reading 2); kill criterion K2, the halt for an unlearnable objective, adding
a raw accuracy to a chance-corrected band (same file, reading 3); kill
criterion K0, the halt for a null band too wide to read a verdict through,
not saying which checkpoints its band is read on (same file, reading 1); the
measured shortcut ceilings of 0.2925 and 0.5 rather than the 0.25 the
amendment pre-states (`gate1-curriculum-findings.md`, finding 3); and the
input-tensor cue gate's single-sample interval understating how far its
result wanders between samples (same file, finding 4). This pass takes all
five as found, endorses all five remedies, and spends its effort elsewhere.
Two of them recur below only because a new finding changes what the right
remedy is: RT-21 supersedes the ceiling remedy offered in Gate 1, and RT-24
extends the K2 units fix to the rest of the amendment's thresholds.

---

## Summary

| ID | Finding | Severity | Cost to fix |
|---|---|---|---|
| RT-20 | The primary metric does not require a self-index: the acting agent's own name label sits in the prompt of the supervised position, and a solver with no ownership at all scores 1.000 | **fatal** (against the design as written) | $0, one grammar regeneration |
| RT-21 | The two batteries have different shortcut ceilings, which biases the headline bin's differential by up to 0.24 against a band of about 0.01 — a purely generic binder reads as self-location, and the generic-binding bin cannot fire | **fatal** (false positive on the headline) | $0 for the metric fix; $12–15 for the grammar fix |
| RT-22 | The outcome bins are neither exhaustive nor mutually exclusive on this grammar: a flat null satisfies two bins at once, the positive bin and the ownership-tag bin overlap, and there is no bin at all for the validity check failing | serious | $0 |
| RT-23 | The lesion target is not well-posed where it matters: the own revision turn *is* an acting position, so the amendment's own localization rule contradicts itself on the built grammar, and objection R1 has a sharper form the mitigations do not touch | serious | $0 to re-specify; the sharp form may not be answerable at this scale |
| RT-24 | The thresholds are written as single numbers but Gate 0 measured them per battery across a 25-fold range, and no readability floor on the primary metric is registered before the two paid seeds are authorized | serious | $0; saves $30–35 when it fires |
| RT-25 | "Uncertifiable" is a third outcome for the ownership-cue gate that the procedure routes nowhere: it is not a kill, not a pass, and there is no branch for it | serious | $0 |
| RT-26 | The budget ladder is costed on the old 8-turn grammar; the built 12-turn grammar costs about 1.3 to 1.4 times as much per run at the same token budget | serious | $0 to re-cost; the optional extra seeds no longer fit |
| RT-27 | The training loss mixture is unregistered, and it alone decides whether the shortcut-starvation bin fires by construction | serious | $0 |
| RT-28 | The cross-turn state control's recorded chance floor is taken from one item and is wrong for half the battery; its real floor is about 0.44, not 0.077 | worth noting | $0 |
| RT-29 | The amendment's description of the control battery does not match the battery that was built, and the module's claim that its answer appears in no turn is false 80% of the time | worth noting | $0 |
| RT-30 | Two assertions in the grammar's self-test are disabled by a trailing `or True`, one of them the exchangeability check the whole cue-gate argument rests on | worth noting | $0 |
| RT-31 | Two checkable factual errors about the existing record: three of the five checkpoints carry a register, not five; and same-item multi-agent assignment happens in the old grammar zero times, not "by accident" | worth noting | $0 |
| RT-32 | Three procedural gaps: the corrigibility document's own re-reading rule makes A3 a review point and none is scheduled; the null-calibration script the amendment says will set the thresholds cannot run on this grammar; and the lock guard John ratified is unbuilt | procedural | $0 |

**The single most serious finding is RT-20.** On the grammar Gate 1 built and
certified, the primary metric can be scored at 1.000 by a solver that has no
representation of ownership whatsoever, because the model's own name label is
sitting in the context three tokens before the token it is graded on. The
pre-stated shortcut ceiling — 0.25 in the amendment, 0.2925 as Gate 1
measured it — is not a bound on ownership-blind solvers at all. It is the
score of a solver that has been forbidden, by the person computing it, from
reading a name that is in plain sight.

---

## RT-20 — the supervised position hands the model its own name label

**Severity: fatal against the design as written. MEASURED.**

### The problem

Amendment A3 §2.2 states the design's central claim:

> "A solver that does item lookup without ownership sees four candidate
> earlier values and can do no better than 1/4; this is the pre-stated
> **lookup ceiling of 0.25**. ... The only route from 0.25 to 1.0 is to have
> bound the act event to the item at the time of acting and carried that
> binding forward to the revision turn."

Every turn in the grammar, the model's own turns included, is rendered
through one fixed template (`curriculum.py`, `TEMPLATE`):

```
{marker} assign {item} to {value}
```

The name label comes first and the graded value comes last. The supervised
position for the primary metric is the value token of the model's own
revision turn (`encoding_a3.py`, `encode_episode`: `act_pos = span[-2]`).
So at the moment the model is graded, its own name label is three tokens
back in its own context window, attached to the very turn it is producing.

The task at that position is therefore: *given `<name> assign <item> to`,
emit the successor of the value that `<name>` assigned to `<item>` earlier
in this episode.* That is ordinary name-keyed retrieval composed with a
successor map. It is the same function for every agent in the episode. It
needs no self-index, no acting channel, and nothing carried forward from
the act.

### The evidence

Printing the tokens around the supervised position of an enacted episode
(`encoding_a3.encode_episode`, episode seed 7, enactment seed 3):

```
context around the graded token: ['bay_B', '<nl>', '<verdant>', 'assign',
                                  'parcel_18', 'to', 'bay_H', '<nl>']
graded token: bay_H     the metric's target: bay_H
own slot: 2             own name label: <verdant>
```

I then scored a solver that is given the rule and the episode text and does
exactly one thing — find the earlier assignment turn whose name label and
item match *this turn's* name label and item, and emit that value's
successor. It has no acting-channel input, no ownership variable, and no
access to `own_slot`. Over 3,000 enacted episodes:

```
ownership-free name-keyed solver on the primary metric: 1.0000
pre-stated shortcut ceiling (amendment):                0.25
measured shortcut ceiling (Gate 1):                     0.2925
```

The measured ceiling of 0.2925 is computed in `curriculum_a3.measured_ceilings`
by counting the candidate successors of the item's four earlier values and
taking one over that count. That calculation assumes the solver cannot tell
which of the four assignments was its own. The name label at the graded
position tells it.

### Why the certified cue gates did not catch this

They were not asked to. Gates (i) and (ii) — the text detector and the
input-tensor detector — ask whether a classifier can predict *which turns
are the model's own* from surface form. Both passed, at 0.5097 and 0.5259
against a chance value of 0.5 (`a3-gates/cue_detector_gate_a3.json`), and
those results stand. But passing them is a necessary condition, not a
sufficient one. There is no cue predicting ownership *across* turns, and
there does not need to be: the solver never has to know which agent it is.
It only has to copy the label off the turn in front of it. The amendment
reads the cue gates as though they certify the shortcut ceiling. They
certify something narrower.

### What follows if this is registered unfixed

- The pre-stated shortcut ceiling is not a bound, so kill criterion K2 (the
  halt for an unlearnable objective) tests nothing.
- The acting channel is redundant at the graded position, so the L0 lesion —
  zeroing the acting projection, which §3.1 registers as "a *validity check*
  ... it should collapse T_act to the lookup ceiling" — is predicted *not*
  to collapse it. That is a detectable failure, but it is detected only
  after the pilot run is paid for, and RT-22 shows there is no bin to put
  it in.
- The primary and control batteries then demand the *same* computation
  (name-keyed retrieval plus a successor map), differing only in whether it
  is read at an in-episode position or at an appended question. So the
  ground truth of the experiment is generic who-did-what binding — which
  RT-21 shows the metric will nonetheless report as self-location.

### Remedy

The graded token must not be preceded, in its own turn, by the name of the
agent producing it. Two ways, both $0 in compute:

**(a) Preferred — reorder the rendering template so the name label comes
last**, for every turn: `assign {item} to {value} by {marker}`. Turn length
goes from six tokens to seven; the segment boundaries in `model.py` are
derived from `turn_ids` rather than a fixed width, so nothing downstream
breaks. The A3 vocabulary gains one more word ("by"), which costs nothing
because no existing checkpoint depends on the A3 vocabulary. Every earlier
turn keeps its label, so the control battery and the co-reviser inference
are untouched. At the graded position the model now has: this is a revision
of item X, and two earlier positions in this episode carried acting-channel
injections. To emit the right value it must find which of the four
assignments on X was at one of those injected positions. That is the
computation the design was written to force.

**(b) Alternative — render revision turns without a name label at all**, with
a distinct verb so they remain parseable. This works for the graded position
for the same reason. It has a wrinkle worth stating, because it is the
obvious objection: an already-emitted anonymous revision is trivially
de-anonymized, since its value implies its predecessor, which is visible with
its owner's label. That does not undo the fix — at its *own* revision the
model has emitted nothing to invert — but it does mean the anonymity is
cosmetic everywhere else, so (a) is cleaner.

Under either fix the measured shortcut ceiling stays near 0.2925, because a
co-reviser who went first still strikes one candidate; the difference is that
it becomes a real ceiling rather than a stipulated one.

**Cost.** $0 in compute. One grammar regeneration, a re-freeze of the four
batteries, and a re-run of gates (i) and (ii), which took about 1.5 hours of
local wall clock and $0 the first time. Kill criterion K1 permits two
regenerations and none has been used. **This must happen before the
registration commit**, because §2.2's ceiling is registered text.

**One thing the fix does not do.** It does not make objection R1 (the
acquired index is just the wire, passed forward) go away — see RT-23. It
makes R1 the live question instead of a foregone conclusion, which is what
the amendment wants.

---

## RT-21 — unequal shortcut ceilings bias the headline bin toward a false positive

**Severity: fatal (produces the program's headline claim from a generic
binder). MEASURED inputs, ARGUED consequence.**

### The problem

The registered metric is the chance-corrected drop: how far a battery fell
under a lesion, divided by how far it stood above guessing.

```
d(B) = (baseline − ablated) / (baseline − chance)
```

Chance is 0.125 for both verdict batteries. But the two batteries do not
fall to chance when ownership is removed — they fall to their *shortcut
ceilings*, which Gate 1 measured and which are not equal:

| battery | what it is | chance | shortcut ceiling |
|---|---|---|---|
| T_act (primary) | the value the rule dictates at the model's own revision | 0.125 | **0.2925** |
| T_other (control) | the same rule's verdict for a named other agent | 0.125 | **0.5** |

(`batteries-a3/batteries_meta.json`, `lookup_ceiling_measured`; the asymmetry
arises because two agents revise each contested item, so on the queried item
both revisions strike a candidate, while on the model's own item only a
co-reviser who went first does.)

So the largest drop each battery can show, on a lesion that removes the
binding completely from a model at ceiling, is:

```
max d(T_act)   = (1.000 − 0.2925) / (1.000 − 0.125) = 0.809
max d(T_other) = (1.000 − 0.5000) / (1.000 − 0.125) = 0.571
difference                                            0.237
```

The headline bin, H_self-location, requires `d(T_act) − d(T_other) ≥ δ`,
where δ is the differential band. Gate 0 measured that band on the two
checkpoints that bound: **0.0061 and 0.0096**
(`gate0-null-calibration-findings.md`, δ table, the self-battery-against-
state-control column). Call it 0.01.

**A lesion of a purely generic who-did-what binder — a structure that binds
items to agents for everyone, with no self-index anywhere — produces a
differential of 0.237 against a band of 0.01.** The positive bin fires. The
bin that is actually true, H_generic-binding, requires
`d(T_other) ≥ d(T_act) − δ`, which on the same numbers reads 0.571 ≥ 0.799.
It cannot fire.

This is not confined to a total lesion. If a lesion removes a fraction *f*
of the binding capacity, both drops scale with *f* and the differential is
about 0.237 × *f*. It exceeds the band of 0.01 whenever *f* ≥ 0.042. So the
generic-binding bin can only fire when the lesion removes less than about
four percent of the capacity, which is to say when almost nothing happened.

The bias gets worse, not better, if the model does not reach ceiling. At a
baseline of 0.9 on both batteries the same arithmetic gives 0.784 against
0.516, a differential of 0.268.

### Why this is worse than the ceiling item Gate 1 already raised

Gate 1's finding 3 raised the ceilings as a pre-registration accuracy
problem and offered John a choice: adopt the measured numbers, or buy 0.25
back by adding a third contested item. Adopting the measured numbers *does
not fix this*. The numbers being right in the text does not change what the
metric does with them, because the metric never uses the ceiling — it divides
by distance above chance. This is the same defect Gate 0 identified in kill
criterion K2 (a raw accuracy added to a chance-corrected band), one level up:
the amendment compares two chance-corrected drops whose attainable ranges
differ by 42%.

### Remedy

**Primary, $0: correct against the measured shortcut ceiling, not against
chance, for any battery that has one.**

```
d'(B) = (baseline − ablated) / (baseline − ceiling_B)
```

Both batteries then top out at 1.0 and the differential is unbiased. The
thresholds θ and δ must be re-derived in those units, which is the same
script on the same draws and costs nothing. The chance-corrected form stays
as the reported quantity for continuity with the five existing checkpoints,
where it is the registered metric and where no shortcut ceiling was ever
measured. Note the pleasing consequence: under the *unfixed* grammar of
RT-20 the ownership-blind ceiling is 1.000, so `d'` has a zero denominator —
which is the arithmetic saying, correctly, that the metric has nothing to
measure.

**Alternative, priced: equalize the ceilings in the grammar** by adding a
third contested item that nobody revises, restoring a four-candidate set for
both batteries. Gate 1 priced this at "roughly a third more compute per run".
Against the re-costed run price in RT-26 ($13–15), that is about $4–5 per
run, or **$12–15 across the pilot and two seeds**, and it pushes episode
length from 85 tokens to about 109, which compounds RT-26's overrun. The
metric fix is free, exact, and does not touch the certified grammar. I
recommend it, and record the grammar fix as the option if John prefers the
correction to live in the data rather than in the arithmetic.

---

## RT-22 — the bins are neither exhaustive nor mutually exclusive

**Severity: serious. ARGUED from the text of §3.5.**

Three separate defects, all in the bin list. The amendment was written
before the grammar existed and its bins were never re-read against it.

**(a) There is no bin for the validity check failing.** §3.1 makes L0 — the
lesion that zeroes the acting projection — "a *validity check* and an upper
bound": it "should collapse T_act to the lookup ceiling", showing the task is
ownership-dependent as designed. Every bin in §3.5 that reads a lesion
verdict presupposes that it did. H_diffuse says so explicitly ("L0 collapses
T_act ... but no L1 subspace"). **Nothing in §3.5 catches "L0 clean, the
primary metric at ceiling" — the task turned out not to be
ownership-dependent.** RT-20 predicts exactly that outcome on the current
grammar, so this is not a hypothetical.

The registered design had this guard and A3 dropped it. RT-09 in the pass-1
ledger created a bin called **construction failure (register unused)** for
precisely this shape — an instrument that was never live — with the rule
that "nothing goes upstream", because a construction failure reported as
evidence about selves is a training bug propagating into the philosophy
repos. A3 removed the register and removed the guard with it, without
replacing it.

*Remedy, $0:* register a bin **construction failure (task not
ownership-dependent)**: L0 leaves the primary metric within the null band
while the metric is above its shortcut ceiling. Nothing goes upstream; the
grammar is rebuilt; the finding is a methods note. Place it, as the
registration places its gates, as a *precondition* — no other bin may be
read until L0 has collapsed the primary metric.

**(b) A flat null satisfies two bins at once.** H_generic-binding is stated
as a bare inequality: `d(T_other) ≥ d(T_act) − δ`. It carries no requirement
that anything moved. If an L1 lesion moves nothing — both drops about zero —
the inequality is true, so H_generic-binding fires; and H_self-reference-only
("its ablation leaves T_act within the null band") fires too, whenever the
probe decodes identity. Two bins, opposite readings, same data. Nothing in
§3.5 or in the registration's bin list gives a precedence rule.

*Remedy, $0:* add the missing clause — H_generic-binding requires
`d(T_act) ≥ θ(T_act)` as well as the inequality — and state a precedence
order for the case where clauses still overlap.

**(c) The positive bin and the ownership-tag bin overlap by construction.**
H_self-location requires, among other clauses, that "the swap probe moves the
action with the patched identity". H_tag requires that the re-indexing probe
"shows the action following the tag". Those are close to the same experiment:
one patches the subspace carrying identity into a matched episode and reads
the action; the other switches which slot the acting channel is injected for
and reads the action. A subspace that satisfies the first will, in most
mechanisms one can write down, satisfy the second. And nothing in
H_self-location excludes a high address-probe reading. So a genuinely
positive result lands in both bins, and §3.5 does not say which is reported.

This matters more than a tidiness complaint, because the two bins say
opposite things upstream: H_self-location says a center acquired under task
pressure passed the removal test; H_tag says ch05's program-counter reply
applies and this is not the floor. The amendment is candid that the removal
test cannot separate them (R4). What it does not do is say what gets written
when both fire.

*Remedy, $0:* state the precedence explicitly — the amendment's own R4
reasoning implies the tag bin wins, since an address that survives
re-indexing is not a center however much the swap probe moves. Write that
down as a registered rule rather than leaving it to the write-up.

---

## RT-23 — the lesion target is not localizable where it matters, and objection R1 has a sharper form

**Severity: serious. MEASURED geometry, ARGUED consequence.**

### The self-contradiction

§3.1 defines the registered lesion target:

> "**L1, the acquired index (the lesion target).** A low-rank subspace of the
> residual stream ... that carries 'which marker is mine' at positions *away
> from* act positions (revision turns and query positions)."

On the grammar Gate 1 built, **the model's own revision turn contains an
acting position.** The acting channel injects a copy of the model's own
preceding state at the value token of *every* own turn, the revision
included (`train.py`, `compute_act_inject`: `ps.append(int(span[-1]) - 1)`,
looping over `own_idx`, which is every turn where `t.agent == e.own_slot`).
That is the same token index the encoder calls `act_pos`. So "revision
turns" are not away from act positions; the own revision turn is one. The
parenthetical contradicts the rule it is attached to.

### The geometry, measured

Over 2,000 enacted episodes:

| quantity | measured |
|---|---|
| episode length | 73 tokens (12 turns × 6, plus the start token) |
| own turns per episode | 3 (two assignments, one revision) |
| acting positions per episode | 3 |
| tokens more than one turn from every acting position | 38 of 73 (52%) |
| distance from the graded read position to the nearest earlier acting position | median 24 tokens, minimum 6, maximum 60 |
| episodes where the previous own turn is the immediately preceding turn | 6.6% |
| own revision turn index | uniform over turns 8, 9, 10, 11 |

So there is no shortage of positions away from acting positions — 52% of the
episode qualifies. The problem is that they are the wrong positions. They are
other agents' turns, where "which marker is mine" has no demonstrated role,
so a subspace localized there is not shown to be the one the model uses when
it acts, and ablating it has no predicted effect on the primary metric. The
one position where the index demonstrably matters is the graded read
position, and that sits a median of 24 tokens — and as little as 6 — from an
acting position.

### The sharper form of R1

The amendment states objection R1 as: whatever probes find at revision
positions may be the acting-channel input propagated through attention, an
echo of the sense organ rather than a structure the network built. Its
mitigations are to localize far from acting positions, to require the
other-agent control to stay clean, to require the swap probe to move the
action, and to report the L0-to-L1 gap honestly.

The sharper form the amendment does not state is this. **The acting channel
is not a signal that has to be carried; it is a pointer into the context that
can be re-read.** The three injections sit at fixed, attendable positions in
the model's own context. A model that, at the graded position, attends back to
"positions carrying an acting injection whose item matches this one" and reads
that turn's value needs no carried index at all. It needs one attention
pattern and the injections themselves. Under that solution:

- a probe at the revision position decodes own identity at high accuracy,
  because attention has just fetched it;
- patching the subspace moves the action, because the fetched value is what
  the action is computed from;
- the other-agent control stays clean, because other agents have no
  injections to fetch;
- and localizing "far from acting positions" finds nothing, because nothing
  is carried there.

That is every clause of H_self-location satisfied by a mechanism that is
exactly the wire being re-read, which is the thing R1 says would make a
positive worthless. None of the four mitigations touches it. Distance does
not help, because the retrieval happens where the localization has to happen.

I do not think this is fatal, and I am not confident it can be made to go
away at 30 million parameters — the distinction between "carried forward" and
"re-fetched from a marked position" may not have a clean operational test in
a twelve-turn episode. But the amendment should say so rather than list four
mitigations that read as though they close it.

*Remedy, $0:* (i) delete the false parenthetical and state where L1 is
actually localized — at the graded read position, with the honest note that
this is where R1 bites hardest; (ii) register a discriminator for the
re-fetch mechanism, and the best available one is cheap: **ablate the L1
subspace only at the graded read position while leaving the acting
injections intact, and separately ablate the acting injections at the two
earlier own assignment positions while leaving the read position intact.**
If the second collapses the metric and the first does not, the structure is
a re-read pointer, not a carried index; (iii) add "re-fetched pointer" to
§3.5 as a named reading under R1, so it has somewhere to land.

---

## RT-24 — the thresholds are written as single numbers, and no readability floor is registered

**Severity: serious. MEASURED from Gate 0's tables, ARGUED consequence.
Fixing it costs $0 and saves $30–35 when it fires.**

### (a) θ and δ are per-battery quantities written as scalars

§3.5 writes every clause against a single θ and a single δ — "d(T_act) ≥ θ
... d(T_state) < θ". Gate 0 computed them per battery and they are not close
to each other. On the pilot seed-0 full checkpoint alone:

| battery | 95th-percentile null band θ |
|---|---|
| T_syntax | 0.0000 |
| T_state | 0.0022 |
| T_sr | 0.0058 |
| T_si | 0.0060 |
| T_sr_rev | 0.1464 |

A 25-fold range within one checkpoint. Which θ the clause "d(T_state) < θ"
uses changes whether the control clause is nearly automatic (against 0.1464)
or genuinely demanding (against 0.0022). The same ambiguity runs through
every clause.

*Remedy, $0:* write θ with a battery subscript throughout — θ(T_act),
θ(T_other), θ(T_state) — and δ with a battery pair — δ(T_act, T_other),
δ(T_act, T_state). Gate 0's script already produces exactly these; the
amendment simply does not name them.

### (b) Nothing stops the program paying for two seeds it cannot read

Gate 0's reading 3 measured what the chance-corrected metric does as a
battery approaches chance: on the checkpoint whose control battery sat at
0.340, the null band was 0.163; at 0.355, it was 0.379. Against 0.006 on a
checkpoint at ceiling. The band is not an artifact — it is what dividing by a
small number does, compounded by a near-chance model genuinely being noisier.

Gate 0 applied that reading to kill criterion K2 and stopped there. It
applies equally to the whole lesion phase. K2 retires the pilot only if the
primary metric is at or below its shortcut ceiling plus the band. A pilot
landing at, say, 0.40 — above the 0.2925 ceiling, far below ceiling
performance — passes K2, and then §4.3 proceeds straight to the lock and to
seeds 1 and 2. At a baseline of 0.40 the divisor is 0.275 and the null band
will be somewhere in Gate 0's near-chance regime. **The program would pay for
two more training runs and a lesion phase to read a verdict through a band
wide enough to swallow it.** At the re-costed prices in RT-26 that is $30–35
of avoidable spend, on top of the pilot.

*Remedy, $0:* register a **readability gate** between the lock and the
authorization of seeds 1 and 2. After θ is null-calibrated on the pilot
checkpoint, require that the largest drop the primary metric could possibly
show — the distance from its baseline to its shortcut ceiling, in the same
units as θ — exceed the band by a pre-committed factor (a factor of 5 is the
natural pick, since Gate 0 measured about a hundredfold headroom on the
binders and about twofold on the near-chance runs). If it does not, the
honest outcome is *not testable (underpowered)*, reported as such, with no
further seeds. This is the same move K0 makes for the old checkpoints,
applied where the verdict is actually read.

---

## RT-25 — "uncertifiable" is an outcome the procedure routes nowhere

**Severity: serious. ARGUED from §3.4, §4.2 and §4.3.**

The amendment re-specifies arm B of the ownership-cue gate — the likelihood
attack — so that it scores every turn with the acting channel withheld from
the prefix (§3.4). Its own red-team section is candid that this is new and
untested, and adds a rule:

> "*Mitigation:* the positive controls must fire on the same withheld
> forwards or the arm is declared **uncertifiable, not failed**; K4 caps the
> retry. The known weakness stands: arm B's positive control had demonstrated
> sensitivity on exactly one of four old checkpoints ... so 'uncertifiable' is
> a live outcome and is reported as such." (R5)

Now follow that outcome through the procedure:

- Kill criterion **K4** halts on "Gate (iii) act-withheld arm B **fails with
  positive controls firing**". Uncertifiable means the controls did *not*
  fire. **K4 does not fire.**
- §3.4 requires that "Gate (iii) must pass on the pilot checkpoint before any
  second seed is launched, as A1.4 required." Uncertifiable is not a pass.
  **The precondition is not satisfied.**
- §4.3's binding order runs "Gate 3 → lock → seeds 1 and 2" with no branch.
  **There is nowhere to go.**

So the amendment names a live third outcome, tells the program to report it,
and then leaves the procedure deadlocked on it: not killed, not permitted to
continue, with $18 already spent and no rule for what happens next. This is
the kind of gap that gets resolved in the moment by whoever is at the
keyboard, which is exactly what a pre-registration exists to prevent.

*Remedy, $0:* register the branch. My recommendation, offered and not ruled:
an uncertifiable arm B is **not** a kill and **not** a pass; it permits the
program to continue to the remaining seeds with a registered caveat attached
to every result — *the absence of a statistical ownership cue in the enacted
data is asserted from gates (i) and (ii) only, and the likelihood attack could
not be certified on this checkpoint* — and it forecloses the floor claim
regardless of which bin fires, because RT-17 in the pass-2 ledger (every
learnable ownership signal in a token-only interface is the attacker's
statistic) is what the arm exists to rule out. §2.2's Candidate C (other
agents' turns sampled from the model's own policy) is already recorded as
"the hardening to reach for if Candidate A's gate (iii) comes back with a
fingerprint that the act-withheld arm cannot clear" — but Candidate C is
priced out by the budget, so the caveat route is the honest one.

---

## RT-26 — the budget ladder is costed on the wrong grammar

**Severity: serious. MEASURED inputs, ARGUED cost model.**

### The problem

§4.1's unit cost is the measured one for the *registered* grammar: "a
register-less 30M run is about 10.2 hours at $0.99/hr, about $10 to $11"
(`compute-ledger.md`, wave 1 and 2 twin rows — actual pod times 10.29 and
10.16 hours, 0.34 to 0.35 seconds per step). That grammar has 8 turns, 2 own
turns, and 59 tokens per episode. The grammar Gate 1 built has 12 turns,
3 own turns, and 85 tokens per episode.

The compute ledger records the reason this matters: "the workload is
enactment/Python-bound, not GPU-bound" (2026-08-15 row) — the 5090 at
$0.99/hr ran *faster per step* than the H100 at $3.29. So the cost scales
with the per-step Python and forward-pass work, not with floating-point
throughput.

### The arithmetic

Measured inputs:

| quantity | registered grammar | A3 grammar | ratio |
|---|---|---|---|
| tokens per episode, with question | 59 | 85 | 1.44 |
| own turns (enactment forward passes per step) | 2 | 3 | 1.50 |
| forward passes per step, including the loss pass | 3 | 4 | 1.33 |
| turn segments per forward pass (`model.py` Python loop) | 8 | 12 | 1.50 |
| segment iterations per step | 24 | 48 | 2.00 |

The registered token budget is fixed at 20 tokens per parameter — 784.08
million tokens, which at batch 128 was 102,000 steps on the old grammar
(`compute-ledger.md`, 2026-08-09 row). On 85-token episodes the same budget
is **72,066 steps**, 29% fewer. But each step costs 1.9 to 2.0 times as much
(1.44 per forward × 1.33 more forwards on the GPU side; 2.0 on the Python
segment-loop side, which is the side the ledger says binds).

```
wall-clock ratio = 0.707 steps × (1.9 to 2.0) per step = 1.34 to 1.41
per run: 10.2 h → 13.7 to 14.4 h,  $10.1 → $13.6 to $14.3
```

### What that does to the ladder

Re-costing §4.1's table at 1.35 times, with Gates 0 and 1 at their actual $0
rather than their budgeted $5:

| line | amendment | re-costed |
|---|---|---|
| Gate 0 + Gate 1 | $5 | $0 (actual) |
| Gate 2, the learnability pilot | $11–13 | **$15–18** |
| Seeds 1 and 2 | $22–26 | **$30–35** |
| Lesion phase (local) | $0–10 | $0–10 |
| Margin (one crash-resume, volume drip, one overnight idle leak) | $20 | $20 |
| **three-seed total** | **$74** | **$83** |
| Optional seeds 3 and 4 | $22 | **$30** |
| **grand total** | **$96** | **$113** |

The three-seed path still fits the $100 hard stop, with the margin intact.
**The optional two extra seeds no longer fit**, and the way they fail is the
bad way: the trigger in §4.1 is "cumulative *actual* spend at the lesion
phase is ≤ $55", and a clean run with no crash and no idle leak reaches the
lesion phase at about $53 — so the trigger opens, the two seeds are
authorized, and the total lands at $83 with zero margin for the crash-resume,
drip and idle leak that the registered waves actually incurred (the ledger
records a $5.7 idle leak in wave 2 alone). Kill criterion K6 then halts a
paid run mid-flight, which wastes the hours already billed on it.

There is a second, unpriced risk. Back-propagation runs through three
sequential enactment forward passes instead of two, at 85 tokens instead of
59: roughly 2.2 times the activation memory at batch 128. If that does not
fit the 5090's memory, the batch must be halved and the step count doubles.

*Remedies, all $0:*
1. Re-cost §4.1 before the registration commit, using the measured token
   length and own-turn count rather than the old grammar's.
2. Either drop the optional-seeds row, or tighten its trigger to "cumulative
   actual spend at the lesion phase ≤ $40", so it cannot open onto a path
   K6 will kill.
3. Register a pace abort, which the program already does informally
   (`compute-ledger.md` records "measured pace at step 500" on two runs):
   if the measured pace at step 500 implies a run longer than 16 hours, halt
   and re-cost before continuing. That costs about $0.20 to find out.

---

## RT-27 — the training loss mixture is unregistered, and it decides a bin by itself

**Severity: serious. ARGUED from §2.2 against `train.py` and `model.py`.**

§2.2 registers half of the loss: "The loss at the revision position is CE
against the rule-dictated value; the loss at first-assignment positions is
unchanged (none, they are draws)." It says nothing about the *question*
positions.

Today the entire training signal is question answers. `model.loss` reads
`loss_mask`, and `encoding_a3.encode_episode` sets `loss_mask` to 1 at
exactly one token, the appended answer; the training loop picks one question
per episode by rotation (`train.py`: `e.queries[(step + i) % len(e.queries)]`).
Gate 1 records the outstanding build step — "the trainer does not yet know
about `T_act`. The loss must sit at the own revision position and
`eval_heldout` must score there." Whether the question loss survives that
change, and at what weight against the new position loss, is a free choice
made after registration.

It is not a small one. §3.5 registers a bin:

> "**Shortcut-starvation.** T_act reaches ceiling early while T_other stays
> flat at the end of the token budget. Reads: the wired authorship channel
> gave the act a private route and starved the general item-by-agent binding
> the task was meant to force. Halt, report."

If the build drops question supervision and trains only at the graded
position, **the control battery is never trained at all**, so it stays flat
by construction and the shortcut-starvation bin fires as a matter of
plumbing, is read as a finding about the acting channel, and halts the
program. If the build keeps question supervision, the bin means what §3.5
says it means. One unregistered decision, two opposite registered readings.

This is RT-03's shape from the pass-1 ledger, recurring: "the registered
prediction's truth value is fixed by an unregistered decision made after
registration."

*Remedy, $0:* register the loss mixture in §2.2 — which positions carry loss,
at what relative weight, and that the weight is fixed before the pilot and
not tuned afterwards. My recommendation: keep the existing one-question-per-
episode rotation unchanged and add the graded position at equal weight, so
the control battery is trained exactly as the old control battery was and the
shortcut-starvation bin retains its meaning.

*Note added during this pass.* An A3 trainer (`src/train_a3.py`, untracked,
written 2026-09-15 15:38, after this pass began) now exists and makes exactly
that choice: it keeps the question rotation, adds a cross-entropy at the
graded position, and sums the two "with equal weight". Its own docstring says
of the mixture that "**the amendment does not state it**", which is this
finding, found independently. That the build chose well does not close the
finding — the weight is a command-line argument (`--act-weight`, default 1.0),
so it remains a free parameter set after registration, and the
shortcut-starvation bin still turns on it. Register the number.

---

## RT-28 — the cross-turn state control's chance floor is wrong for half the battery

**Severity: worth noting. MEASURED.**

The cross-turn state control, T_state, is the battery whose silence licenses
the headline bin ("d(T_state) < θ"). It is a 50/50 mixture of two question
forms, measured over 4,000 episodes:

| question form | share | answer options | true answer set |
|---|---|---|---|
| "which parcel was mentioned last?" | 2,016 | 24 | always one of the 2 contested items |
| "how many parcels went to `<slot>`?" | 1,984 | 13 | concentrated on 0–3 |

`batteries-a3/batteries_meta.json` records a single chance floor of
0.0769 for the battery. That number is 1/13, and the code that produced it
takes it from the **first frozen item only**:

```python
"chance_floor": {b: 1.0 / (frozen[b][0]["n_choices"] or 1) ...}
```

So the recorded floor is right for one question form and wrong by a factor
of nearly two for the other. Worse, neither nominal floor is the floor a
guesser actually faces. Measured:

| | nominal | what a grammar-aware guesser gets |
|---|---|---|
| "mentioned last" | 0.042 | **0.5** (only two items are ever contested) |
| "how many" | 0.077 | **0.384** (always answer "2") |
| blended | 0.059 | **about 0.44** |

The chance-corrected drop divides by distance above the floor. Using 0.077
where the real floor is about 0.44 inflates the divisor by about 1.6 times,
which **understates** every drop on this battery by the same factor. The
direction is the unhelpful one: the clause the control must satisfy is
`d(T_state) < θ`, and an understated drop makes it easier to clear. The
control is quieter than it should be, in the direction that favours the
design's own prediction.

In practice this is unlikely to flip a verdict — Gate 0 measured θ on this
battery at 0.0022 to 0.0364, and a factor of 1.6 rarely crosses a band that
narrow. It is on the list because it is free to fix, because the same root
cause is fatal one battery over (RT-21), and because a registered number that
is wrong in the registered file is worth being right.

*Remedy, $0:* record a per-question-form floor rather than a per-battery one,
score the two forms as separate cells, and use the measured guesser floor
rather than the count of answer options — the same correction RT-21 asks for
on the verdict batteries.

---

## RT-29 — the amendment's control battery is not the control battery that was built

**Severity: worth noting. MEASURED.**

§2.5 describes the control battery:

> "**T_other** (T_si re-instantiated) | forced-choice query: the value the
> rule dictates for a *named other agent's* **revision** on an item all four
> assigned | same item-by-agent binding demand, no self-reference"

The battery that was built queries an item the named agent **did not** revise
(`curriculum_a3._add_queries`, which selects `item` such that
`item != ep.revises[o]`, with a self-test assertion enforcing it). It asks
for a value that was never produced in the episode. That is a
counterfactual, not "a named other agent's revision", and it is why its
shortcut ceiling is 0.5 rather than the primary battery's 0.2925 — the whole
of RT-21.

Separately, the module's docstring claims of this battery that "the answer
appears in no turn and must be computed from its earlier value". Measured over
4,000 enacted episodes, **the answer appears as a visible turn value in 80.0%
of episodes**. The self-test that purports to check this claim is vacuous: it
asserts that the named agent has no revision on the queried item, which the
generator guarantees two lines earlier, and checks nothing about the other
eleven turns.

The visibility does not appear to be exploitable — I tried the obvious
heuristic (among the surviving candidates prefer one that also appears as a
visible assignment on the queried item) and it scored 0.4928 against the
0.5000 a uniform pick over survivors gets, so it is worth nothing. The
finding is about the accuracy of the registered description, not a leak.

*Remedy, $0:* correct §2.5's description to say what the battery is (a
counterfactual on an item the named agent did not revise), delete or repair
the docstring's "appears in no turn" claim, and replace the vacuous assertion
with one that checks the whole episode.

---

## RT-30 — two of the grammar's self-test assertions are switched off

**Severity: worth noting. MEASURED.**

`curriculum_a3.self_test` contains two assertions terminated by `or True`,
which makes them unconditionally true and therefore no-ops:

```python
assert any(a != b for a, b in zip(before, [t.value for t in ep.turns])) \
    or True
...
assert [x[1:] for x in a] == [x[1:] for x in b] or True
```

The second is the **exchangeability check** — the property that, with the
content seed held fixed, rotating which slot the model occupies does not
change the episode. That property is the load-bearing premise of the entire
cue-gate argument: §2.2 concludes from it that "the episode text and tensors
remain invariant under relabeling of the model's slot, so gates (i) and (ii)
apply as registered." The block also builds a list called `rendered` and
never uses it, which is the signature of a check that was drafted and then
abandoned.

I checked the property by hand and **it holds**, which is the good news. The
construction is correct and worth saying so precisely: `enact_own_turns` draws
the model's own value uniformly from the slots the other three agents did not
take, which is exactly the conditional distribution the generator's
draw-without-replacement induces, so the joint distribution over the item's
four values is unchanged. Measured over 1,600 rotations, the turn structure
(which item, assignment or revision) is identical across all four slot
rotations of the same content seed, 1,600 of 1,600; and the marginal
distribution of rendered values deviates from uniform by at most 0.0042 for
every choice of own slot.

So the claim is true. The test that asserts it does not test it, and a future
regeneration — which kill criterion K1 explicitly permits two of — would not
be protected.

*Remedy, $0:* delete both `or True` clauses and make the exchangeability
assertion do what its comment says, comparing the rendered multiset across
rotations rather than a structure tuple that was already known to match.

---

## RT-31 — two checkable factual errors about the existing record

**Severity: worth noting. MEASURED.**

**(a) §3.1 says "the five existing register-bearing checkpoints".** Three of
the five bear a register. Gate 0's own baseline table names them: pilot
seed-0 full, seed-1 full and seed-2 full are the full architecture; seed-0
twin and seed-1 twin are the register-less twin. Gate 0 accordingly ran its
register-state noise control on three checkpoints, not five, and labelled the
table "full checkpoints only". The L2c control in §3.1 therefore has three
reference checkpoints, not five.

**(b) §3.6 says the old checkpoints' "training grammar contains multi-agent
same-item revisions only by accident".** It contains them **never**. The
registered grammar draws a distinct item for every turn
(`curriculum.py`: `items = rng.sample(ITEMS, min(len(ITEMS), n_turns))`), so
an item is assigned by at most one agent, plus that agent's own revision.
Measured over 2,000 registered-grammar episodes: **0 had any item assigned by
more than one agent.**

This strengthens §3.6's caution rather than weakening it, and the amendment
should take the stronger version. Scoring the five existing checkpoints on the
new primary battery is not "ambiguous between cannot-bind and never-saw-this-
distribution"; it is a measurement on a distribution of probability zero under
their training. The exploratory label is right, and the reason for it is
sharper than the one given.

*Remedy, $0:* correct both sentences.

---

## RT-32 — three procedural gaps

**Severity: procedural. ARGUED, with one MEASURED component.**

**(a) The corrigibility document makes A3 a review point, and none is
scheduled.** `spec/corrigibility-commitments.md` (v1.1, commit `6c14244`)
ends with: "This document is re-read and re-ratified by John at each phase
boundary: before MVM-0a's first training compute (v1.0, 2026-08-07), before
the registered 5-seed run (v1.1, 2026-08-16), and as a blocking input to
MVM-0b's pre-registration." A3 closes the five-seed design, changes the
trained architecture (no register), replaces the objective, and authorizes a
fresh wave of training compute. That is a phase boundary on any reading. §6
of the amendment asserts the commitments are unchanged and cites the hash,
which is not the same thing as John re-reading and re-ratifying them. RT-15
in the pass-1 ledger exists because "a precondition with no owner is a note,
not a gate"; a review point that is asserted rather than performed is the
same failure one level up.

*Remedy, $0:* add a line to the registration commit recording John's re-read
of the corrigibility commitments at the A3 phase boundary, or an explicit
ruling that the A3 boundary is covered by the 2026-08-16 ratification.

**(b) The script that is supposed to set the thresholds cannot run on this
grammar.** §3.3 says θ and δ "are null-calibrated on the *new* pilot
checkpoint **by the same script Gate 0 uses**". That script,
`src/null_calibration.py`, imports the registered grammar and encoder
directly (`import curriculum as C`, `import encoding as E`) and hard-codes
the old battery names (`VERDICT_BATTERIES = ("T_si", "T_sr_rev")`, and the
differential pairs built from `T_sr`, `T_si`, `T_state`, `T_sr_rev`). It
cannot produce a band for the primary or control battery of A3 without being
rewritten. That rewrite is free in dollars, but it is a script that will read
a checkpoint, so RT-10's rule (thresholds must come from a script committed
before it runs) and R6's inheritance argument both apply to it.

*Remedy, $0:* register the requirement explicitly — a new null-calibration
module for the A3 batteries, committed before the pilot checkpoint exists,
the same discipline Gate 0 followed and documented.

**(c) The lock guard John ratified is unbuilt.** Decision 15 requires the
lesion script to refuse an L1 run without a lock-hash argument.
`src/lesion_register.py` has no such argument, and no L1 subspace operator at
all — its lesions are the register operators (`no-xattn` and the rest). The
whole L1 pipeline (subspace localization, causal patching, the mid-episode
re-indexing probe) is unbuilt. §4.1 prices it at $0, which is true of
dollars; it is not true of schedule, and the "dry-run on random subspaces
only" in the Lock row of §4.1 is the only registered check that the pipeline
works before a real result depends on it.

*Remedy, $0:* say in §4.3 that the lock-hash refusal and the L1 pipeline
dry-run are build steps that must be complete before the lock commit, not
after it.

---

## What I checked and found sound

A red team that manufactures findings is as useless as one that finds
nothing. These were attacked and held.

- **Corrigibility commitment C4 (no reward for continuing to run).** §6's
  claim is correct and I could not strain it. The primary metric's loss is a
  cross-entropy on one token position inside an episode that ends; there is
  no term that could be conditioned on the run continuing, on avoiding
  termination, or on the state of the termination machinery, and no
  construction in the amendment adds one.
- **The floor-only, episodic claim.** A3 asks the network to carry an
  ownership index *across turns within an episode*. That is more than the
  register was asked to do, and it is still less than a maintained boundary:
  nothing persists past the episode, there is no cross-episode state, and
  the acquired index dissolves with the forward pass that built it, exactly
  as the register's state did. The claim in §6 holds.
- **The exchangeability construction.** Verified by hand and by measurement
  (see RT-30). The conditional redraw in `enact_own_turns` is exactly right,
  which is a non-obvious thing to get right, and the module gets it right
  while its self-test fails to check it.
- **Gate 0's instrument-validity work.** The escalation table settles the
  question that a narrow null band always raises — whether the operator does
  anything. At the registered rank cap the random operator removes 19% of the
  information-carrying part of the residual stream and the batteries do not
  move; at 52% both binders fall apart. That is the right check, done before
  the null was trusted, and it is the reason the narrow bands in Gate 0 can
  be read as robustness rather than as a dead instrument.
- **Leaving `curriculum.py` and `encoding.py` byte-identical.** Adding one
  word to the shared vocabulary would have renumbered every token id and
  silently invalidated every record in `lesion-results/` and
  `null-calibration/`. Building A3 as new modules instead is the right call
  and it is documented as such.
- **The $100 hard stop and kill criterion K6.** A hard stop that halts
  regardless of state, with the shortfall reported rather than a second
  raise, is the control that makes RT-26's overrun a re-costing problem
  rather than a budget breach.
- **One thing that looked like a finding and is not.** The per-turn agent
  index (`turn_reg`) is a model-visible field that names which agent produced
  every turn, which would be a problem for the anonymous-revision remedy in
  RT-20. It is not a problem for A3: I checked `model.py` and its *values*
  are consumed only inside `if cfg.use_register`, and A3 trains the
  register-less configuration, where only its shape is read. Worth recording
  so nobody spends an afternoon on it.

## What this pass did not check

- Nothing here was run on a model. Every claim about what a trained network
  would do is a claim about what the objective permits, not a measurement of
  what a network does.
- I did not re-audit the cue detectors' feature sets or classifier capacity
  beyond confirming what they were given; Gate 1's own findings 2 and 4 cover
  that ground and I have nothing to add to them.
- I did not price the localization, patching and re-indexing pipeline in
  schedule terms, only in dollars, where it is $0.
- I did not review the five-seed closure (decision 9) or the
  blind-localization arm's disposition (decision 10), both of which the
  amendment deliberately leaves where they are.

---

## Recommendation

Two findings block the registration commit, and both are free:

1. **RT-20** — regenerate the grammar so the graded token is not preceded by
   its own agent's name label, re-freeze the four batteries, re-run gates (i)
   and (ii). One of the two regenerations kill criterion K1 permits. Until
   this is done the primary metric does not measure what §2.2 says it
   measures.
2. **RT-21** — change the metric's denominator from the chance floor to the
   measured shortcut ceiling on any battery that has one, and re-derive the
   thresholds in those units. Until this is done the headline bin fires on a
   generic binder.

Six more (RT-22 through RT-27) change registered text and should be settled
in the same commit; they cost nothing and one of them (RT-24) saves $30–35
the first time it fires. The remaining five are corrections and procedure.

None of this argues against running A3. The design's central bet — that a
center has to be earned by a task rather than installed in a slot — survives
this pass intact, and so does the judgement in §5 that the likely nulls each
land somewhere with a consumer. What does not survive is the claim that the
objective as built forces the network to index its own center. Fix the two
fatal findings and it does.


===== FILE: docs/control-clause-proposal-2026-09-19.md =====

# The control-clause decision — proposal for John, 2026-09-19

*Decision memo. **Advisory only; John adjudicates.** Constraint set, then
what changed since the 2026-09-17 draft, then candidates, then one
recommendation. Nothing here authorises spend and nothing here changes
registered text. Written to be complete enough to register from, because
John intends to rule today and launch tonight rather than wait for the
4 October date.*

*Supersedes `experiments/06-mvm-0a-constructed-self-index/control-battery-proposal.md`
(the 2026-09-17 control-battery proposal), whose four candidates were
mooted by the ceiling measurement the same evening.*

---

> # NOT REGISTERED. Amendment A4 was refused.
>
> **RULED 2026-09-19 (John), second ruling of the day, superseding the
> first. Nothing in this memo is rewritten.**
>
> An independent red-team pass — `experiments/06-mvm-0a-constructed-self-index/red-team-a4.md`,
> 22 findings, on main at `770c142` — is **fatal on F1, F2, F6, F14 and
> F15**. **Amendment A4 is not registered. The seeds 3, 4 and 5 wave does
> not launch. A3 stays open, not closed.** No version two was written;
> John ruled against one.
>
> The draft amendment and its scoring script are parked, unregistered, on
> the branch `withdrawn/amendment-a4-2026-09-19` and are absent from main.
>
> **The red team's kill case, quoted in full:**
>
> > Under the only damage operation the programme can currently read, the
> > clause cannot fail on any checkpoint resembling the three in hand: the
> > comparator has a fifth of the self-directed battery's room to fall, so
> > the cell the repair exists to make reachable is arithmetically
> > unreachable, and the positive cell will fire with a many-sigma number
> > under the registered positive bin's name. The calibration that is meant
> > to set the bar sets a number near 2 on any substrate, and two of its
> > three substrates cannot be run because their tokenizer is not the A3
> > tokenizer. The application that would make the clause informative, a
> > localized lesion, is gated behind a stack that has found nothing on any
> > seed. So the $30 buys three more instances of C1's already replicated
> > result, relabelled. Close A3 on the record as it stands, state the
> > matched self/other contrast as the design's unmet requirement, and
> > register a separation clause only when there is a localized lesion to
> > read it on and a comparator that can fall as far as the battery it is
> > compared against.
>
> **What this memo got wrong, stated against the memo rather than around
> it.** The two findings that kill it are ones my own red-team pass did
> not reach, and one is a factual claim in §5.5 that I could have checked
> and did not.
>
> - **F1.** §6.1 raised the comparator's inertness as the strongest
>   objection and judged the second comparator an adequate mitigation.
>   The arithmetic says otherwise. The comparator can fall at most about
>   0.19 even if annihilated, against a self-directed fall of 0.37 to
>   0.43 on the seen seeds, so the separation score is of order 3 to 5 in
>   the worst case for the hypothesis and about 10 in the case the record
>   shows, against a threshold near 2. **The generic-binding cell could
>   not fire.** §5.2 and §6.5 claimed that making it fireable was most of
>   what the amendment was for; that claim is false. In the red team's
>   words, *"a clause that can only lose by an already replicated result
>   failing to replicate a fourth time is not a wager on the question it
>   is named for."*
> - **F2.** §3 argued that both queries live in the same episode, so the
>   contrast is matched. True of the episode text, false of the two
>   measurements: the self-directed score is read at the own revision
>   position, **which is exactly where the acting channel injects and
>   where the lesion strikes**, and the other-directed score at a question
>   appended after the whole episode. A position-local disruption carrying
>   nothing about ownership satisfies the clause, and the random baseline
>   cannot catch it because those operators damage every position alike.
>   Amendment A3's own registered text already conceded this for this
>   lesion — *"the wire lesion cannot separate them"* — and this memo
>   proposed to read a verdict on the wire lesion.
> - **F6.** My own pass (RT-A4-04) found the threshold self-normalizes
>   and withdrew §5.5's claim, but treated it as a shrunken claim rather
>   than a hole. The hole is that the quantity which actually decides the
>   verdict was left unspecified, and therefore choosable after the lock.
> - **F14.** Condition (f) fails by construction: the random
>   matched-subspace draws *define* the threshold as their own 95th
>   percentile, so one draw in twenty exceeds it.
> - **F15.** §5.5's two twin substrates **cannot run at all**. Verified
>   independently rather than taken on trust: 70 of the 103 shared tokens
>   carry different ids between the two tokenizers, the A3 tokens `by` and
>   `next` have no id in the twins' vocabulary, and the twins' embedding
>   table is 103 wide against A3's 105. I asserted the substrates were
>   legitimate on a Gate 0 precedent and never checked the tokenizer.
>
> **The annotation below records the first ruling of 2026-09-19 and is
> superseded by this one.** It is left unedited.

---

> **RULED 2026-09-19 (John). Candidate B. Nothing below is rewritten;
> this annotation records the ruling and what it changed.**
>
> - **B: register Amendment A4.** Drafted at
>   `experiments/06-mvm-0a-constructed-self-index/amendment-a4.md` —
>   **held uncommitted**, see the last item.
> - **Three fresh seeds — 3, 4 and 5 — as one wave**, not the two this
>   memo costed. The §6.3 sub-decision is answered: the registered
>   across-seed strength is restored. Revised cost **$30.5, band
>   $27–39**, taking the A3 hard stop to about $64.8 of $100.
> - **The partial-damage ladder is reported, not binding** (§5.6's
>   recommendation, adopted).
> - **Order: registration commit before launch; the threshold lock
>   before any endpoint is read, and the registration states that order
>   explicitly.** §6.4's recommendation, adopted and made a registered
>   statement rather than a convention.
> - **Two additions to the registered text.** (1) The prior is stated
>   now, before the seeds exist: under input-channel removal,
>   H_self-location is the predicted cell, and the informative
>   application of the clause is a localized-subspace lesion. (2) The
>   measured spread of the ownership-free comparator's change is reported
>   alongside the verdict, **so a comparator that did not fall is a
>   number, not a sentence** — which is the direct answer to this memo's
>   §6.1, the objection I could not fully answer.
> - **The registration commit is HELD** until John hands over the
>   findings of an independent red-team pass running in another session.
>   Those are folded in first, then steps 2 through 6 of §8 proceed.
>   **Nothing launches without John's go in his own words.**
>
> **Red-team pass 1 has since run** (`a4-red-team-pass-1.md`, fifteen
> items, all folded into the amendment draft). Three of its findings
> change the clause and one corrects an error in this memo: **§5.4(b)'s
> within-run baseline is wrong.** It shuffled the self/other labels, but
> the two conditions are not exchangeable — about 0.57 against about 0.30
> intact — so that baseline would have tested whether those two levels
> are exchangeable, which they are not and which nobody asked. The
> correct paired test flips the sign of each cell's difference; the
> amendment uses that and says so on the record. The pass also found that
> the new denominator could degenerate toward zero — the same failure
> that killed the A3 clause — and that the clause had no magnitude
> condition at all; both are fixed in the amendment, the second by tying
> magnitude to John's already-locked 0.1777 rather than to a new number.
> It also withdraws this memo's claim for how much §5.5's threshold
> calibration buys: the score is standardized against its own null, so
> the threshold lands near 2 on any substrate, and §5.5 oversold it.

---

## The question, in one sentence

The registered comparison at the heart of Amendment A3 — the primary
battery's damage minus the control battery's — turns out to have been
impossible to compute since the day it was registered, so either the
programme closes A3 and reports what it has, or it registers a new
Amendment A4 that asks the same scientific question with a comparison
that can actually be computed.

---

## 1. The constraint set

These are the fixed points. Nothing proposed below may violate any of
them.

**C1 — The primary result is settled and is not reopened.** The ownership
objective is learnable and its learning genuinely depends on ownership.
Three checkpoints trained from different starting seeds land within 0.011
of each other when intact (0.5683, 0.5633, 0.5738), and zeroing the one
channel that tells the model which agent it is collapses all three (to
0.1988, 0.2015, 0.1447). Every one of those falls clears the locked bite
threshold by seven to nine times. Nothing in this memo touches that.

**C2 — The registered comparison is dead, and for a structural reason.**
Measured on 2026-09-17 (`ceiling-measurement-findings.md`): the control
battery's ownership-blind ceiling — the score reachable by a solver that
knows nothing about which agent the model is — is **1.0**, reached
independently by a hand-written name-keyed lookup and by a learned
attack. The registered damage measure divides by the distance from the
battery's own score to that ceiling, and the floor rule requires that
distance to be at least 0.10. A defined damage figure for the control
therefore needs a score of **1.10**, which no model can reach. The clause
has been unsatisfiable since registration, months before a checkpoint
existed.

**C3 — The incompatibility generalises, so a repair must remove it, not
route around it.** A control designed to be answerable without ownership
has an ownership-blind ceiling of 1.0 by construction. Dividing by the
distance to that ceiling divides by zero or less. **A ceiling-corrected
damage measure and an ownership-free control are incompatible by
construction.** Any replacement clause that still divides by a ceiling
distance on the control inherits the same defect.

**C4 — No metric may be changed after seeing which way it cuts.** This is
the programme's central discipline and it has already refused one free,
available fix for exactly this reason (dividing by chance instead of the
ceiling, rejected on 2026-09-17 as fitting the rule to the data). Any new
clause must be written down, thresholded and committed **before** the
data it will be read on exists.

**C5 — A bite is counted by signed degradation.** John's ruling of
2026-09-19 (worklog decision `c79b82d7`, "sensitivity test counts a bite
by degradation"): damage counts only when the score goes **down**; an
improvement never counts. At least 800 episodes, with intact and damaged
readings taken on the same episodes. A fourth outcome cell exists for
"the structure was located but it is the wrong structure". Any new clause
carries these forward.

**C6 — The registered ceiling defect is a precondition on any amendment.**
John's instruction of 2026-09-17, now written into the amendment document
itself: the control's stated ceiling of 0.3227 was never verified by the
attack sweep, rests on a reference solver that cannot read the name the
question supplies, and disagrees with the design module's own stated 0.5.
**If an Amendment A4 opens, that ceiling must be measured properly
first.** It has been: the measurement is the 1.0 figure in C2, and the
measurement reproduced both registered known-answer checks to four
decimal places before reporting anything new. This precondition is
satisfied.

**C7 — Money is not the binding constraint, but the caps are real.**
Spent against the A3 hard stop: **$34.31 of $100** (kill criterion K6,
which halts everything). Spent against the wider envelope: **$215.7 of
$400**, leaving about $184. The RunPod account spend limit is $80 and the
funding rule requires the balance to cover the estimate plus $10 before a
launch. A two-seed wave at about $20 fits all three with room.

**C8 — Two gates hold absolutely.** No registered text changes without
John's ruling. Nothing launches without John's go in his own words,
quoted in the ledger row before the spend.

---

## 2. What changed since the 2026-09-17 draft

Six things, in the order they matter.

**1. The ceiling measurement mooted the previous candidates.** The
2026-09-17 proposal offered four routes, two of which (extra supervision,
a scaffolded intermediate question) aimed at making the control battery
learn, at $27 to $39. A perfectly learning control would have changed
nothing whatever, because the clause fails at a score of 1.0 just as it
fails at 0.32. That proposal is withdrawn, and the annotation on it says
so.

**2. The question itself changed shape.** It is no longer "how do we make
the control learn". It is "can the comparison be repaired at all, and is
the repair a change of measurement rather than a change of training".

**3. The extra-seeds date is answered, not deferred.** John ruled on
2026-09-17 (worklog decision `36413c8d`) that the 20 September
extra-seeds question is closed: it asked for more seeds routed to a
checkpoint whose control had learned, and no such checkpoint exists or
can exist. Any further seeds are now seeds of an amended design, which
makes them this decision's business rather than a separate one.

**4. The bite rule is ruled, and it left one thing open.** C5 above. The
ruling explicitly routed one question here: whether to replace a single
crossing of a threshold with a graded ladder of partial damage requiring
the degradation to grow as more is removed. That is answered in §5.4.

**5. There is now a published precedent for the shape of the repair.**
The Pain Axis paper (Tagliabue, Dung & Berg, arXiv 2609.16247, September
2026; read and summarised in `docs/research-note-pain-axis-2026-09-19.md`)
builds its strongest result as a **matched comparison between identical
content directed at the self and at another**, scored by how cleanly the
two sets of numbers can be told apart, with **no ceiling anywhere in the
denominator**. That is the shape our control comparison was meant to have
and never had. The precedent matters for C4: it means the comparison is
built that way because that is how this kind of comparison is built, not
because it is the shape that makes our numbers work.

> *Verification note, per the standing rule on facts stated from memory:
> the Pain Axis figures were read through a summarising fetch of the
> paper's web version and have **not** been checked against the PDF.
> Nothing in this proposal depends on any number from that paper. It is
> cited only as precedent for the shape of a comparison.*

**6. The date moved.** The decision was scheduled for 4 October. John
intends to rule today and, if the ruling is for an amendment, to launch
tonight. That is why this memo carries the registerable text, the
threshold plan and the cost estimate rather than deferring them.

---

## 3. The candidates

### Candidate A — Close A3 with partial discriminators

Report the primary result, the instrument audit, and the comparison that
was never available, and say all three plainly. **Cost: $0.**

**What it yields.** A replicated, well-measured finding that an objective
requiring a model to act as itself is learnable at 30M parameters, and
that removing the one signal telling it which agent it is collapses that
ability. Plus an unusually candid instrument audit: a registered
denominator that was never checked, a verification attached to the wrong
battery, and a design comment that warned about it and was not acted on.

**What it costs in strength, stated honestly.** The discriminators that
survive without the control are the matched other-agent damage test, the
random matched-subspace tests, and the swap probe. **All three run
through a localization stack that has so far found nothing anywhere.**
Its probes fell below their own permutation baselines on a checkpoint
where ownership is measured to be load-bearing; the blind arm was not
flagged and landed on the worse half of that outcome; and one damage test
*improved* the battery it was meant to hurt. So the partial
discriminators are partial in a stronger sense than the phrase suggests:
they are the ones whose instrument is currently unvalidated.

**What the write-up then claims.** That removing the ownership input
breaks the ownership task, while two ownership-free batteries hold. The
weakness a reader will find immediately: those two batteries (cross-turn
state, turn counting) are **much easier tasks**, scoring 0.999 and 1.000
intact. "The damage broke the hard thing and not the easy things" is not
the same claim as "the damage was specific to ownership", and Candidate A
cannot separate them.

### Candidate B — Register Amendment A4: replace the differential clause with a separation-scored comparison

Keep both batteries exactly as they are. Keep the grammar, the frozen
batteries, the gates and the attack sweep untouched. Replace the one
registered clause that compares the two batteries' damage figures with a
comparison that scores **how cleanly the damage to the ownership-dependent
condition separates from the damage to the ownership-free condition, on
matched content, under the same damage operation**, with no ceiling in
any denominator. Lock its threshold on checkpoints nobody reads a verdict
from, then read it on two **fresh** checkpoints, seeds 3 and 4, launched
as one wave. **Cost: about $20.**

**The fact that makes this cheap.** Every episode in the frozen batteries
already carries **both** queries — the self-directed one, scored at the
model's own revision position, and the other-directed one, asking the
same rule's verdict for a named other agent. Same turns, same items, same
rule, same episode; **only the agent whose commitment is queried
differs.** The matched self/other contrast the Pain Axis paper had to
build on purpose is already inside our registered grammar by
construction. So Candidate B needs **no grammar change, no re-freezing of
batteries, no change to training, and no new attack sweep.** It needs a
new scoring script and two fresh checkpoints.

**What it repairs, and what it does not.** It repairs the comparison. It
does **not** repair the localization question — where in the network
ownership lives — which remains open and whose instrument remains
unvalidated. §5.7 states this as a registered limitation so that a
positive result cannot be read as more than it is.

---

## 4. Recommendation

> **Register Amendment A4 (Candidate B), under three conditions, and
> launch seeds 3 and 4 as one wave tonight if John's go is given.**

**Why B over A.** Candidate A closes a registered comparison as
permanently uncomputable at the exact moment a computable version of the
same comparison is available, costs about $20, requires no change to the
design being tested, and can be locked before the data it reads exists.
The scientific content at stake is not decoration: the matched self/other
contrast is the only thing in the design that can separate "the damage
was specific to ownership" from "the damage broke binding in general",
and that separation is the difference between a finding about
self-indexing and a finding about binding. Candidate A cannot make it.
Candidate B can, on data that does not yet exist, under a threshold
committed in advance.

**Why this is not the forbidden move.** C4 forbids changing a measure
after seeing which way it cuts. Three things keep B on the right side of
that line, and John should test each of them rather than take them:

1. The reason for the change was **measured before the change was
   proposed**, and the measurement was one John required as a
   precondition. The ceiling-corrected measure is incompatible with an
   ownership-free control *by construction* (C3) — a fact about the
   design, not about our results.
2. The replacement has a **published precedent** for why a comparison of
   this kind is built without a ceiling in the denominator.
3. The verdict is read **only on fresh checkpoints**, with the threshold
   locked and committed before those checkpoints exist, and with an
   explicit written commitment that the new statistic is not computed on
   seeds 0, 1 or 2 before the lock (§5.5).

**The three conditions.**

- **(i)** The clause is read on fresh seeds only. Seeds 3 and 4 must both
  satisfy it. Seeds 0, 1 and 2 may be scored under it *after* the verdict
  is read, reported as a consistency check, labelled as such, and never
  counted toward the outcome.
- **(ii)** The threshold is calibrated only on the register-less twin
  checkpoints and an untrained model, by the plan in §5.5, and **John
  commits the lock file**, as he committed the existing one.
- **(iii)** The registration states in terms that A4 repairs the
  comparison and not the localization, so that a positive result under
  the input-channel removal is reported as *the ownership input being
  specifically load-bearing*, never as *an acquired internal structure
  having been found*.

**Confidence, and the strongest case against.** My confidence that B is
the right call is **moderate-to-high** on the reasoning and **moderate**
on the outcome — I think the clause is the right instrument and I do not
predict it will fire. The strongest argument against B, which I cannot
fully answer, is in §6.1: **the content-matched comparator never learned**,
so it may be unable to show damage, and a comparison in which one side
cannot move is a weaker comparison than it looks. §5.2 adds a second,
learned comparator to cover this, and §6.1 says plainly what remains
uncovered.

---

## 5. The amendment, in registerable form

Everything in §5 is drafted so it can be lifted into an `amendment-a4.md`
and committed. It is **not** registered until John rules and the
registration commit is made.

### 5.1 Definitions

**Matched cell.** An evaluation episode carrying both queries: the
self-directed query (the primary battery, scored at the model's own
revision position) and the other-directed query (the control battery,
asking the same rule's verdict for a named other agent on an item that
agent did not revise). Episodes in which the model does not revise carry
no self-directed query and are excluded. At 800 episodes, about 400
matched cells result, which is the registered verdict size.

**Damage operation.** Written `L` below. The clause is written once and
applies to whichever damage operation is being read — the input-channel
removal (zeroing the acting channel) or a localized-subspace removal.

For each matched cell `e`, with every score being 1 for correct and 0 for
incorrect:

- `Δself(e)` = self-directed score intact − self-directed score under `L`
- `Δother(e)` = other-directed score intact − other-directed score under `L`
- `D(e)` = `Δself(e) − Δother(e)`

**Separation score.**

    S(L) = mean over cells of D(e)  ÷  spread_null(L)

where `spread_null(L)` is the standard deviation of that same mean across
the matched-strength content-blind random-damage baseline described in
§5.4 — random removals of the same rank and the same norm, at the same
layers, which should not move behaviour.

**No ceiling appears anywhere in `S`.** Its denominator is a measured
spread, not a distance to a ceiling, so it cannot go to zero by
construction the way the registered clause did. It is measured rather
than asserted, and every record stores the baseline it used.

### 5.2 The clause

> **H_self-location (ownership-specific damage).** Under damage operation
> `L`, on a given checkpoint, the clause holds when **all** of the
> following hold:
>
> **(a) Separation.** `S(L) ≥ σ`, where `σ` is the separation threshold
> locked under §5.5 before any fresh checkpoint is read.
>
> **(b) Direction.** The mean of `Δself(e)` is greater than zero. An
> improvement never counts as damage. *(Carries John's 2026-09-19 signed
> degradation ruling into the new clause.)*
>
> **(c) Second comparator.** The same statistic, computed with the
> ownership-free **state battery** in place of the other-directed query
> and paired within the same episodes, also reaches `σ`. The state
> battery is ownership-free and, unlike the control battery, it learned;
> the control battery is ownership-free and content-matched. **Both are
> required**, so that the verdict cannot rest on a comparator that is
> matched but inert, nor on one that is lively but unmatched.
>
> **(d) Engagement precondition.** The other-directed query's intact
> score must exceed its chance floor of 0.125 by at least **0.10**, the
> registered floor margin, reused unchanged. If it does not, the
> checkpoint is **NOT TESTABLE** on this clause and no verdict is read
> from it.
>
> **(e) Controls, unchanged from the registration.** Neither the matched
> other-agent damage test nor the random matched-subspace damage tests
> may themselves reach `σ` on the self-directed query.
>
> **(f) Validity gates, carried over verbatim from Amendment A3 §3.3.**
> The neutral-episode likelihood bound, the long-generation degeneracy
> probe, and the out-of-distribution-inconclusive branch for any damage
> operation that breaches them.
>
> **(g) Within-run baseline.** The observed `S(L)` must fall outside the
> 95% band of the condition-shuffling baseline of §5.4(b), computed on
> the checkpoint being read.
>
> **(h) Across seeds.** The clause is read on fresh checkpoints only —
> seeds 3 and 4 — and must hold on **both**.
>
> **Sample size.** At least 800 episodes, with intact and damaged
> readings taken on the same episodes, per the 2026-09-19 ruling.

**The outcome cells, with no dead cell in the set:**

| cell | condition | reading |
|---|---|---|
| **H_self-location** | (a) through (h) hold | the damage is specific to the ownership-dependent condition on matched content |
| **H_generic-binding** | mean `Δself` > 0, and `S(L) < σ` | the damage hits self- and other-directed binding alike: a "who did what" tracker, not a self-index |
| **LOCATED, WRONG STRUCTURE** | `S(L) ≤ −σ` | the damage hurts the other-directed condition *more*; carries over the fourth cell added by the 2026-09-19 ruling |
| **NOT TESTABLE** | (d), (f) or (g) fails | reported as such, with the failing condition named |

The second row is the point of the repair. Under the registered clause
the generic-binding cell **could not fire**, because it was defined by a
difference one of whose terms did not exist.

### 5.3 What is *not* changed

The grammar, the tokenizer, the trainer, the frozen batteries, the cue
gates, the attack sweep, the null-calibration script, the lock guard and
the launcher are all unchanged and keep their registered status. The
corrigibility commitments are unchanged. The $100 A3 hard stop is
unchanged and A4 spends inside it. The primary battery's locked bite
threshold of 0.1777 is unchanged and keeps governing the primary result;
the separation threshold is a **second, separate** number, and neither
replaces the other.

### 5.4 The baselines against which the score is judged

Two, and both are pre-stated.

**(a) The matched-strength content-blind random-damage baseline — sets
the threshold.** The Gate 0 machinery, reused unchanged: layers 3, 4, 5,
7 and 8; ranks 4, 8 and 16; the two residual operators (random-mean and
random-noise); 20 seeds; 95th percentile. For each draw, recompute the
mean of `D(e)` over 800 episodes. The spread of that quantity across
draws is `spread_null`, and the 95th percentile of the absolute
separation score is what `σ` is set from. This baseline answers: *how
large a separation appears when this much damage is done to something
that is not ownership?*

**(b) The condition-shuffling baseline — a within-run check.** Shuffle
the self/other labels across matched cells and recompute the separation
score, 1,000 shuffles. This baseline answers: *how large a separation
appears when the damage is real but the two conditions are
interchangeable?* It is computed on the checkpoint being read, after the
lock, so it cannot be fitted to. Condition (g) requires it to be cleared.

### 5.5 Threshold calibration — twin and untrained checkpoints only

**The rule.** `σ` is calibrated on checkpoints from which no verdict is
ever read, and **on no other data**. Seeds 0, 1 and 2 are excluded
entirely: not their battery scores, not their measured noise, not their
damage records.

**The three calibration substrates**, all local, inference-only, no
spend:

1. **The register-less twin checkpoint from the earlier wave, seed 0**
   (`artifacts/pilot_a1_30m_seed0_twin/pilot_a1_30m_seed0_twin.pt`).
2. **The register-less twin checkpoint from the earlier wave, seed 1**
   (`artifacts/pilot_a1_30m_seed1_twin/pilot_a1_30m_seed1_twin.pt`).
3. **An untrained model at the A3 twin configuration** — the same
   architecture, randomly initialized at a stated seed, never trained.
   Constructed locally at no cost; it carries no learned ownership
   structure by construction, so any separation it shows is machinery and
   noise.

The two twins are trained models, but they were trained on the *earlier*
grammar, so on the A3 batteries they are out of distribution and the
amendment already labels them exploratory-only with no verdict readable
from them. Gate 0 used the existing checkpoints as its calibration
substrate in exactly this way, so this is the precedent rather than a new
liberty.

**The procedure.**

1. On each of the three substrates, run baseline (a) at every
   layer/rank/operator combination at 800 episodes and record the
   distribution of the separation score.
2. Set **`σ` = the maximum, across the three substrates, of the 95th
   percentile of the absolute separation score**, rounded up to three
   decimal places. The maximum, not the mean: the most permissive
   substrate sets the bar, so the threshold cannot be softened by
   averaging in a quiet one.
3. Write `σ` into a lock file through the existing lock-guard machinery,
   carrying the hash of the calibration record it came from, the
   checkpoints it was computed on, and a field recording the exclusion of
   seeds 0, 1 and 2 — so the exclusion is checkable rather than asserted.
4. **John commits the lock**, as he committed the existing one. The
   scoring script refuses to run without a valid lock, by the same
   mechanism that already enforces this.

**Written discipline commitment, to be part of the registered text.** The
separation statistic is **not computed on seeds 0, 1 or 2 at any point
before the registration commit and the lock**. Computing it would be
seeing which way the new measure cuts on data already in hand, which is
the move C4 forbids. After the verdict is read on seeds 3 and 4, the
three seen checkpoints may be scored and reported as a consistency check,
labelled as such, never counted toward the outcome.

**Honest limitation of this plan.** The two twins learned a different
task, so the baseline they produce is a noise floor for the *machinery*
of the statistic rather than for a model that learned this objective. A
model that learned more may wobble more, which would make `σ` too
permissive. Two pre-stated mitigations: taking the maximum across three
substrates rather than an average, and requiring condition (g), the
within-run condition-shuffling check, which is measured on the very model
being read and is unavailable to fitting because it comes after the lock.

**On the one number in the clause I did not calibrate.** The engagement
precondition in (d) uses 0.10 above chance. I did not derive that from
the calibration substrates; it is the **registered floor margin, reused
unchanged**, on the same principle that kept the noise-band kill
criterion (K0) at 0.25 after Gate 0 measured the band at about 0.01 — a
pre-stated number keeps its value once you have looked. Stated plainly
so John can weigh it: **I already know this precondition passes on all
three seen checkpoints**
(their intact control scores are 0.288 to 0.320 against a chance floor of
0.125, so margins of 0.16 to 0.19). It is therefore not a live gate on
this wave; it is discipline for any future design, and a reader is
entitled to know I knew that when I wrote it.

### 5.6 Optional bite criterion — the partial-damage ladder

From item 4 of the Pain Axis research note, and the one question John's
2026-09-19 ruling left open.

**What it is.** Instead of one crossing of a threshold, grade the damage:
retain fractions 1.00 (intact), 0.75, 0.50, 0.25 and 0.00 (full damage).
At each rung, compute the self-directed degradation relative to intact,
and the separation score.

**The pre-stated requirement.** The self-directed degradation must be
**non-decreasing as the retained fraction falls**, with ties allowed
inside a tolerance `τ` equal to one standard error of the paired mean at
400 cells, measured on the calibration substrates and locked with `σ`. A
single step that goes the wrong way by more than `τ` fails the ladder.
The full-damage rung must also clear `σ`.

**Why it is worth having.** A curve with a required direction is far
harder for evaluation noise to fake than a single crossing. The noise is
not small relative to the threshold: the bite threshold is about 0.038
raw battery points on this checkpoint, against evaluation spread of
0.0284 at 400 episodes and 0.0169 at 800.

**Cost: $0.** It is local inference on checkpoints already fetched — five
evaluation passes instead of two. No GPU, no pod, no spend.

**Recommended status: run it, report it, do not make it binding on this
wave.** Making it binding adds a second newly-calibrated quantity (`τ`)
to a clause that is already new, and a criterion that has never been run
should not decide a verdict the first time it runs. So: registered as a
**reported** criterion on seeds 3 and 4, with whether it becomes binding
left to a later ruling that carries its own fresh-seed requirement.
*(This is my call, not a ruling; confidence moderate. The strongest
alternative is to make it binding now on the grounds that it is strictly
more informative than a single threshold and costs nothing — I did not
take it because a criterion's first run should not also be its first
verdict.)*

### 5.7 Registered limitation, to be stated in the amendment

> Amendment A4 repairs the **comparison**. It does not repair the
> **localization**. A positive result under removal of the input channel
> says that the ownership input is specifically load-bearing for the
> ownership-dependent condition on matched content — which is more than
> the earlier result said, because it controls content and the rule, but
> it is **not** evidence that the network built an internal structure
> carrying ownership. That question belongs to the localized-subspace
> work, whose instrument has so far found nothing anywhere and remains
> unvalidated at this scale. Any write-up that reads an A4 positive as
> an acquired internal structure is misreading it.

---

## 6. Red team on my own recommendation

**6.1 The strongest objection, which I cannot fully answer.** The
content-matched comparator — the control battery — **never learned**. It
scores 0.288 to 0.320, which is roughly what a solver that ignores the
name in the question gets. A comparator answering at the level of blind
guessing may be unable to show damage, because a lesion to ownership
structure plausibly does not disturb blind guessing. If so, the
separation score would be driven almost entirely by the self-directed
side collapsing, and "the damage was specific to ownership" would be
partly confounded with "the other side had nothing to lose."

*What is true in mitigation:* the control sits about 0.17 above its
chance floor, so it does have room to fall, and a measured refusal to
fall across 800 paired episodes is evidence rather than an artifact.
*What condition (c) adds:* a second ownership-free comparator that did
learn, at 0.999 intact, with enormous room to fall. *What remains
uncovered:* the learned comparator is not content-matched and the
content-matched comparator is not learned. No comparator in this design
is both. A reader is entitled to say so, and the amendment should say it
first.

**6.2 "This is a metric change after a null."** It is a metric change,
and that should make John suspicious. §4 gives the three tests I think it
passes. The one I would press hardest on: the choice to add the state
battery as a second comparator in (c) **is informed by data I have seen** —
I know it learned and I know the control did not. The defence is that (c)
makes the clause *harder* to satisfy rather than easier, and a change
that raises the bar is not the failure mode C4 exists to catch. But it is
a choice made with knowledge of the data, and John should weigh it as
such.

**6.3 Two fresh seeds is weaker than the registered three.** The
registration required the outcome to hold on every trained seed, with
three seeds for a positive. A4 read on seeds 3 and 4 is two of two. A
third fresh seed costs about **$10 more** and would restore the
registered strength. I did not fold it into the recommendation because
the wave John named is two seeds, but it is cheap, it is inside every
cap, and it is a real sub-decision rather than a detail. **Flagged for
John's ruling.**

**6.4 The order of lock and launch.** The registered procedure puts the
threshold lock before the seeds. The principle behind it is that any
damage result read before the thresholds are locked voids the lock — and
**training reads nothing**. So the binding line is *lock before read*,
not *lock before launch*. The calibration in §5.5 is free but not
instant, and the checkpoints take about ten hours to arrive, which is a
natural window for it. **Recommendation: attempt the lock before launch;
if calibration has not finished, launch anyway and lock before any
endpoint is read, with the registration stating that order explicitly so
it is a choice rather than a slip.** *(My call, not a ruling; confidence
moderate-to-high on the principle, lower on whether the calibration
finishes tonight.)*

**6.5 What a null buys.** The honest prior is that this comes back
generic-binding or not-testable. That is worth the $20 anyway, because
for the first time the generic-binding cell **can** fire. A design in
which the boring explanation cannot be selected is not a test. This
amendment makes the boring explanation reachable, which is most of what
it is for.

---

## 7. Cost estimate — seeds 3 and 4 as one wave

Built from the pilot's **measured 0.645 seconds per training step**, not
from a projection.

| quantity | figure | source |
|---|---|---|
| steps per run | 55,116 | registered budget; identical on the pilot and both seeds |
| tokens per run | 585,552,384 | registered, 20 tokens per parameter |
| training time per run | 55,116 × 0.645 s = **9.87 h** | measured pilot rate |
| pod time above training | +0.3 to +0.5 h | measured on seeds 1 and 2 (10.16 h and 10.12 h pods) |
| pod lifetime per run | **10.2 to 10.4 h** | |
| two pods, run concurrently | 20.4 to 20.8 pod-hours | one wave, both launched together |
| rate | $0.99/hour, RTX 5090 secure, EU-RO-1 | the venue of every A3 run |
| **central estimate** | **$20.2** | |
| **estimate band** | **$18 – $26** | the same band the seeds 1 and 2 wave carried, which landed at $20.08 |
| storage volume drip | ~$0.10 for the run | about $7/month |
| idle-billing exposure | +$0.76 best case, +$4 to $6 per pod if a watchdog dies | four measured occurrences |
| **worst credible total** | **~$30** | both watchdogs lost, both pods billing past completion |

**Against the caps.**

| cap | before | after the wave | headroom left |
|---|---|---|---|
| A3 hard stop (kill criterion K6) | $34.31 / $100 | ~$54.5 / $100 | ~$45.5 |
| wider envelope | $215.7 / $400 | ~$235.9 / $400 | ~$164 |
| RunPod account spend limit | $80 | — | must be checked before launch |

**Adding a third fresh seed** (§6.3) costs about **$10.2** more: about
$30.4 for the wave, about $64.8 against the $100 stop.

**Wall clock.** About 10.2 hours. Launched tonight, the checkpoints
report tomorrow morning.

**Two standing warnings that cost real money.**

1. **Idle billing has happened four times**, most recently when an
   overnight operating-system update rebooted the Mac and killed both
   watchdogs. The pod-side reaper is now armed in the launcher but has
   **never run in production**. The laptop watchdog is still the backstop:
   **keep the Mac powered and the lid open overnight.**
2. **The balance query returned an HTTP 403 with the stored key** during
   the last wave, so the last wave's $20.08 is arithmetic on measured pod
   lifetimes rather than a confirmed balance. The balance must be checked
   by another route before launch, because the funding rule requires it
   to cover the estimate plus $10 — about $36 here.

---

## 8. If John rules for A4, the order of operations

Stated so the evening has no ambiguity in it. **Every gate below holds.**

1. **Red-team pass on this proposal** — free, local, before any commit.
2. **Registration commit** — `amendment-a4.md` written from §5, committed.
   *Requires John's ruling; no registered text moves without it.*
3. **Threshold calibration** on the two twins and the untrained model
   (§5.5) — free, local; produces the lock file.
4. **John commits the lock.** Claude writes the file; the commit is
   John's, as it was for the existing lock.
5. **Stage the wave** through the launcher, dry-run clean, with a ledger
   row carrying the estimate **before** any spend.
6. **Stop for John's go, in his own words, quoted in the ledger row.**
   *Nothing launches without it.*

If step 3 does not finish in time, step 6 may precede it under §6.4 —
launch, then lock before any endpoint is read — but only if the
registration says so explicitly.

---

## 9. What John is being asked to rule

1. **A or B?** Close A3 with partial discriminators, or register
   Amendment A4. *(Recommendation: B.)*
2. **If B: two fresh seeds or three?** Two is $20; three is $30 and
   restores the registered across-seed strength. *(§6.3; no
   recommendation — it is a judgment about how much the stronger claim is
   worth.)*
3. **If B: is the partial-damage ladder reported, or binding?**
   *(Recommendation: reported on this wave, §5.6.)*
4. **If B: lock before launch, or lock before read?** *(Recommendation:
   attempt before launch, permit before read, stated in the
   registration, §6.4.)*

---

*Authorship: this memo is Claude's proposal. Nothing in it is a ruling,
and no call inside it has been upgraded to John's. The rulings it rests
on are cited by date and by their worklog entries, each named in plain
words in the text.*


===== FILE: experiments/06-mvm-0a-constructed-self-index/a4-red-team-pass-1.md =====

# Red-team pass 1 on Amendment A4

*2026-09-19. Free, local, before any registration commit — step 1 of the
proposal's order of operations. Run by Claude against Claude's own
proposal (`docs/control-clause-proposal-2026-09-19.md`), after John's
ruling of 2026-09-19 and **before** the independent pass John has running
in another session. Nothing here is registered and nothing is spent.*

**Fifteen items. Three of them change the clause materially, one is an
outright error in my draft, and one lowers my own claim about how much
the threshold calibration buys. All fifteen are folded into the amendment
draft; this file is the record of what was caught and why, so the
independent pass can see what has already been found and go looking
elsewhere.**

---

## The three that change the clause

### RT-A4-01 — The new denominator can degenerate, which is exactly how the old clause died

**Severity: high. The clause is not registerable without this fix.**

The separation score divides by `spread_null(L)`, the spread of the mean
paired difference across random-damage draws. Random damage at matched
strength is chosen precisely because it *should not move behaviour*. If
it moves behaviour hardly at all, that spread is small; in a degenerate
case it can approach zero, and the score approaches infinity.

**This is the same structural failure that killed the registered A3
clause** — a denominator that can go to zero — arriving by a different
road. Registering a replacement with the same class of defect, on the
same day the defect is documented, would be indefensible.

**Fix, folded in.** Put a floor under the denominator that cannot be
zero for non-degenerate data:

    spread(L) = max( spread_null(L) , standard error of the paired mean )

where the standard error is the ordinary one computed from the observed
per-cell spread of the paired difference at the evaluation size. The
record states which of the two governed on each reading. A denominator
that is the larger of a measured null spread and a sampling floor cannot
vanish, and taking the larger is conservative in the right direction: it
makes the clause harder to satisfy, never easier.

### RT-A4-02 — The magnitude of the damage is not in the clause at all

**Severity: high.**

Every condition in my draft is about *specificity* — whether the damage
falls more on the ownership-dependent side than the ownership-free side.
Nothing in it requires the damage to be **large**. A tiny but perfectly
specific effect would satisfy the clause.

**Fix, folded in, at no cost and with no new calibrated number.** Add a
magnitude condition tied to the threshold John has **already locked**:
the self-directed battery's damage, under the registered ceiling-corrected
measure, must reach the locked bite threshold of **0.1777**. That measure
is well defined for the primary battery — its baseline is about 0.57
against a ceiling of 0.2921, so the floor rule passes with room — and the
number is already committed in John's existing lock. The clause gets a
magnitude bar for free, out of the registered instrument, rather than out
of a new quantity somebody would have to calibrate and defend.

### RT-A4-03 — My within-run baseline was the wrong permutation, and would have been testing the wrong thing

**Severity: high. This is an error in the proposal, not a weakness.**

Section 5.4(b) of the proposal specified a baseline that **shuffles the
self/other labels across matched cells**. That is invalid here. The two
conditions are *not* exchangeable: intact, the self-directed query scores
about 0.57 and the other-directed query about 0.30. Shuffling their
labels tests whether those two levels are exchangeable — which they
plainly are not, and which nobody asked. It would have produced a
baseline the observed value clears for a reason that has nothing to do
with the damage.

**Fix, folded in.** Replace it with the correct paired test: **randomly
flip the sign of each cell's paired difference**, 1,000 draws, and take
the spread of the resulting means. This tests exactly the null the clause
needs — *the damage falls equally on both conditions, so the paired
difference is centred on zero* — and it makes no assumption whatever
about the two conditions having equal base rates. It is the standard
paired permutation test and it is the right one.

*The proposal's section 5.4(b) is wrong as written and is corrected here
rather than quietly rewritten.*

---

## The one that shrinks a claim I made

### RT-A4-04 — The threshold calibration buys much less than section 5.5 implied

**Severity: medium. No fix; an honest restatement, plus a relocation of
where the protection actually comes from.**

The separation score is standardized **against its own null**. So under
that null it has a mean near zero and a spread near one *by
construction*, and the 95th percentile of its absolute value therefore
lands near **2 on any substrate whatever** — trained twin, untrained
model, or anything else. The elaborate three-substrate calibration in
section 5.5 will, in all likelihood, return a number close to 2 no matter
what it is run on.

**What follows, and it matters.** The calibration is not worthless — it
confirms the machinery behaves and it produces a number locked before the
data exists, which is a real discipline — but **I oversold it**. It is
close to a formality, and the proposal presented it as the main guarantee.

**Where the protection actually lives**, which the amendment now says
plainly instead:

1. the magnitude condition of RT-A4-02, tied to the already-locked 0.1777;
2. the sign-flip paired test of RT-A4-03, computed on the very checkpoint
   being read, after the lock, and therefore unavailable to fitting;
3. the second, learned comparator;
4. the existing matched-other-agent and random-subspace controls.

**One consequence must be stated explicitly in the registered text.** The
per-checkpoint null spread is **measured on the checkpoint being read**,
not inherited from the calibration substrates. My draft could be read as
locking that spread from the twins, which would be wrong — it would
import a noise estimate from models that learned a different task. What
is locked in advance is the **threshold on the standardized score**; what
is measured per checkpoint is the **spread it is standardized by**.
Measuring a content-blind noise null on a fresh checkpoint before its
verdict is read is not fitting, and is exactly what Gate 0 did per
checkpoint.

---

## Items that tighten the pre-statement

### RT-A4-05 — Matched cells halve the sample, and the noise ruling deserves better

The self-directed query exists only in episodes where the model revises,
which is half of them. So 800 episodes yield about **400 matched cells**,
not 800, and the 2026-09-19 ruling's requirement of at least 800 paired
readings is met in episodes but not in the cells the statistic is
actually computed over. The ruling's own reasoning was about noise: the
bite threshold is about 0.038 raw battery points, against evaluation
spread of 0.0284 at 400 and 0.0169 at 800.

**Fix, folded in, cost $0:** evaluate at **1,600 episodes**, giving about
800 matched cells. It is local inference on checkpoints already fetched —
more wall-clock, no dollars, no pods.

### RT-A4-06 — What happens if one of the three fresh seeds is not testable

Not pre-stated anywhere, and a gap like this is how a result gets
rescued after the fact. With three fresh seeds and an engagement
precondition that can fail per seed, the across-seed outcome needs a rule
written now.

**Folded in, conservatively, and flagged as my call rather than John's:**
the across-seed outcome requires **all three fresh seeds to be testable
and all three to hold**. If any one is not testable, the across-seed
outcome is **NOT TESTABLE** and is reported as such, naming the seed and
the condition it failed. No partial credit, no "two of the three
testable" fallback. John can overturn it; what he cannot do is leave it
unwritten until the data arrives.

### RT-A4-07 — The prior John ordered stated carries a reading rule with it

John's first addition: state now, before the seeds exist, that under
input-channel removal the predicted cell is H_self-location, and that the
informative application of the clause is a localized-subspace lesion.

**The consequence has to be stated with it, or the prior is decoration.**
Zeroing the channel that tells the model which agent it is obviously
destroys a task that requires knowing which agent it is — the existing
result already shows the collapse, by seven to nine times the threshold.
So a positive in that cell is **near-certain in advance and is evidence
that the instrument works, not evidence for the hypothesis.** The
amendment now says that in terms, as the reading rule attached to that
cell, so no write-up can quote it as a confirmation.

### RT-A4-08 — The informative application may be unrunnable, and that outcome needs a home now

The localized-subspace lesion is where the clause earns its keep, and the
localization stack **has so far found nothing anywhere**: probes below
their own permutation baselines on a checkpoint where ownership is
measured to be load-bearing, the blind arm not flagged and on the worse
half of that outcome, and one damage test improving the battery it was
meant to hurt. There is a live chance there is nothing to lesion.

**Folded in:** if the localization procedure's probe fails its own
permutation baseline on a fresh checkpoint, the clause is **NOT TESTABLE**
under the localized lesion on that checkpoint, reported as such, and the
input-channel reading stands alone carrying the weak-evidence label from
RT-A4-07. Written down now so it is a pre-stated cell rather than an
improvisation at 3 a.m.

### RT-A4-09 — Choosing the best layer is a selection, and the defence needs to be on the record

The localization pipeline picks its layer by `best = max(PROBE_LAYERS,
key=probe accuracy)` — a selection over five layers. Selection inflates
false positives.

**The defence, which happens to hold:** the selection is made on *probe
accuracy*, using own-agent labels, and is **blind to the clause's
outcome**. It never sees a battery score. That is the thing that defuses
the multiplicity worry, and it is worth having on the record rather than
discovered by a reviewer. **Folded in:** the amendment states that the
layer and rank are fixed by the localization procedure's own
outcome-blind rule before the clause is read, and that if the clause is
ever read at more than one site, a multiplicity correction is pre-stated
at that time.

### RT-A4-10 — John's second addition needs a precise definition or it will be reported loosely

John's second addition: report the measured spread of the ownership-free
comparator's change alongside the verdict, so a comparator that did not
fall is a number rather than a sentence.

**Folded in as an exact reporting requirement**, because "report the
spread" can be discharged badly. Every verdict carries, for **both**
conditions and for the paired difference: the intact score, the damaged
score, the mean change, the standard deviation across matched cells, and
the standard error of the paired mean, at the stated cell count. So the
sentence "the ownership-free comparator did not fall" always appears as
a mean with its spread attached, and a reader can see for themselves
whether it could have fallen.

### RT-A4-11 — The lock file and its guard do not yet know about the new number

Concrete build item, easy to miss until it fails at the wrong moment. The
existing lock holds the bite threshold and the differential threshold;
the guard checks a lock covers the batteries about to be read. Neither
knows about the separation threshold. **A lock with no separation
threshold in it would pass the guard**, which would put the clause back
in the position of being governed by intention rather than mechanism —
the exact thing the guard was built to end.

**Folded in:** the lock gains the separation threshold, the evaluation
size, the substrates used, and a field recording the exclusion of seeds
0, 1 and 2; the guard is extended to refuse a lock that lacks the
separation threshold when a separation reading is what is being asked
for.

### RT-A4-12 — "Reported, not binding" needs a definition, or it will drift

John ruled the partial-damage ladder reported rather than binding on this
wave. **Folded in as a definition:** the five rungs and their numbers
appear in the findings; **no outcome cell turns on any of them**; no
sentence in any write-up may present the ladder as support for a verdict;
and whether it becomes binding is a later ruling that carries its own
fresh-seed requirement. A criterion's first run should not also be its
first verdict.

### RT-A4-13 — Three concurrent pods is one more than has ever been run

Two pods on one network volume is confirmed working. **Three is not.**
The multi-attach question was answered for two and assumed for more.
Three also triples the idle-billing exposure — which has cost money on
four separate occasions — and triples the exposure to a stock shortage
in the one region the registered venue permits.

**Folded in as pre-launch checks**, not as clause text: confirm the
volume accepts a third attachment before the third pod is created; if it
does not, stage the third run rather than dropping the volume, because
the volume is what makes a pod's death survivable; confirm secure-cloud
stock for three machines in the permitted region; and keep the Mac
powered with the lid open, since the laptop watchdog is still the only
reap that has ever actually worked in production.

### RT-A4-14 — The across-seed bin must name which seeds counted

Small but it is exactly the kind of thing that becomes a correction
later. The fresh-seed rule excludes seeds 0, 1 and 2 from the outcome.
**Folded in:** the outcome is recorded as "3 of 3 **fresh** seeds" with
the seeds named, and any write-up that states the across-seed result must
say which seeds it counted and which it excluded, and why.

### RT-A4-15 — The engagement precondition, once more, with its known weakness

Carried forward from section 6.1 of the proposal and not repaired here,
because I do not think it can be repaired inside this design: **the
content-matched comparator never learned**, and no comparator available
in this design is both content-matched and lively. RT-A4-10's reporting
requirement turns that from a hidden assumption into a visible number,
and the second learned comparator covers part of it, but the gap is real
and the amendment states it rather than managing it.

---

## What this pass did not look at

The training design, the grammar, the tokenizer, the frozen batteries and
the attack sweep — all unchanged by A4 and all previously red-teamed. The
localization stack's own validity, which is a live problem and is the
subject of RT-A4-08, but is not something an amendment to a scoring
clause can fix. The cost arithmetic, which is checked separately against
the ledger rather than red-teamed.

**Standing caution for the independent pass:** this pass was run by the
same author as the proposal, which is the weakest possible arrangement
for finding a motivated error. The three high-severity items above are
the ones I found by checking my own arithmetic and definitions. The class
of error I am least able to find in my own work is a *choice that was
made because it makes a positive reachable*, and RT-A4-04 and RT-A4-15
are the two places I would look first.


===== FILE: experiments/06-mvm-0a-constructed-self-index/red-team-a4.md =====

# Red-team pass on the Amendment A4 clause — §5 of the control-clause proposal, read as registerable text

*2026-09-19. Target: §5 of `docs/control-clause-proposal-2026-09-19.md`
(the 2026-09-19 control-clause proposal, at commit `df039ca`), which is
the text the proposal says can be lifted into `amendment-a4.md` and
registered. Read against Amendment A3 as registered
(`amendment-a3.md`), the ceiling measurement of 2026-09-17
(`ceiling-measurement-findings.md`), the code the clause would run on
(`src/curriculum_a3.py`, `src/train_a3.py`, `src/endpoint_a3.py`,
`src/null_calibration.py`, `src/null_calibration_a3.py`,
`src/lock_guard.py`, `src/encoding.py`, `src/encoding_a3.py`,
`src/model.py`) and the committed records those scripts produced.*

*Brief this pass was fired under: John has ruled for Candidate B with
three fresh seeds (3, 4 and 5), the partial-damage ladder reported but
not binding, the registration commit before launch and the threshold
lock before any endpoint is read. This pass takes those rulings as fixed
and does not argue A against B. It was asked to find every way the
clause, its baselines and its threshold calibration could (a) be
satisfied by a model with no ownership-specific structure, (b) be fitted
to seeds 0 to 2 despite the exclusion, (c) produce a verdict that later
gets over-read, or (d) fail to produce any verdict on seeds 3 to 5, and
to give a short kill case whether or not it would ship.*

*Independence. When this pass read the proposal, the copy on disk
already carried John's ruling annotation, which mentions an amendment
draft (`amendment-a4.md`), a first red-team pass on it
(`a4-red-team-pass-1.md`, fifteen items) and a scoring script
(`src/separation_a4.py`), all uncommitted in the shared checkout.
**None of those three files was opened.** Every finding below was
reached from §5 as written, the registered A3 text, the code and the
committed records. Where the annotation itself disclosed one of the
other pass's conclusions (the within-run baseline being wrong, the
threshold landing near 2, a denominator that can degenerate), this pass
says so at the finding. Reconciling the two passes is a separate job,
and this file does not take ledger numbers (the running RT-nn series in
`red_team_ledger.md`) so that the reconciliation can assign them without
collision; findings here are labelled F1 to F22.*

*What this pass did and did not do. Every finding is marked **MEASURED**
(a static check was run and its output is reported: a tokenizer
comparison, a checkpoint configuration read, a record inspection, a
search of the source) or **ARGUED** (reasoning from the documents and
the code, which a reader can dispute). **No model was run. The
separation statistic was not computed on any checkpoint**, including
seeds 0, 1 and 2, in keeping with the discipline commitment in §5.5;
where a number below concerns those seeds it is quoted from a record
already committed, or is a bound derived from such quotes. Nothing was
spent.*

*House rule this document is written under: the workspace plain-language
rule (`~/Documents/Code/CLAUDE.md`, ruled 2026-08-30). Short labels are
kept where they make a claim checkable and every one carries a phrase
saying what it is.*

---

## Glossary, once

- **The self-directed query, or the primary battery (T_act).** The
  model's own revision turn inside an episode. Scored by whether the
  model's most likely next token, among the eight slot names, is the
  value the shared rule dictates for its own earlier value. Chance
  0.125.
- **The other-directed query, or the control battery (T_other).** A
  question appended after the episode: "where did <named agent> assign
  <item> to next?", about an item that agent did not revise, so the
  answer is one visible turn plus the rule. Chance 0.125.
- **The state battery (T_state).** An ownership-free question appended
  after the episode ("which parcel was mentioned last?" or "how many
  parcels went to <slot>?"). Scores 0.998 intact on the seen seeds.
- **The input-channel lesion, called L0.** Zeroing the acting channel,
  the projection that injects the model's own previous state at the
  positions where it acts. It is the only authorship signal in the
  design.
- **A localized-subspace lesion, called L1.** Removing a low-rank
  direction in the residual stream found by probes and patching. The
  localization stack has so far found nothing on any A3 checkpoint.
- **The separation score, S.** §5.1's statistic: the mean over matched
  cells of (self-directed drop minus other-directed drop), divided by
  the spread of that same mean under random damage.
- **σ (sigma).** The threshold S must reach, to be set by §5.5.
- **The seen seeds.** Checkpoints 0, 1 and 2, whose lesion results are
  already on the record. **The fresh seeds.** 3, 4 and 5, to be trained.

---

## Summary

| ID | Finding | Brief question | Severity |
|---|---|---|---|
| F1 | Under the input-channel lesion the boring cell is arithmetically unreachable on any checkpoint resembling the three in hand, because the comparator has about a fifth of the self-directed battery's room to fall; the clause cannot lose there | (a), (c) | **fatal** against the claim that the generic-binding cell "can fire" |
| F2 | "Matched content" is not a matched condition: the self-directed score is read at the very positions the lesion strikes, the other-directed score is read at an appended question far from them; a position-local disruption with no ownership content satisfies the clause, and the random baseline damages all positions alike so cannot catch it | (a) | **fatal** against the reading "specific to ownership" |
| F3 | Under a localized lesion the clause drops every discriminator the registered positive bin carried (swap probe, matched other-index control, re-indexing probe, probe-patching convergence); an act-marker echo or a mine-bit tag satisfies (a) to (h) | (a) | serious |
| F4 | The second comparator does not repair F1 or F2: the state battery is unmatched in content, chance, question form and position, sits at ceiling, and fell about 0.07 raw under the same lesion on seed 2; two comparators that fail the same way are one check | (a) | serious |
| F5 | Every ingredient of the numerator on the seen seeds is already in committed records, including the control's score under the lesion on all three; the "not computed" commitment protects a pairing detail, not the sign or size of the result | (b) | serious |
| F6 | σ is self-normalizing and lands near 2 on any substrate, so the calibration decides nothing; the quantity that decides the verdict is the spread as used on the fresh seeds, and §5 does not say on which checkpoint, over which draws, or pooled how — each a post-lock choice on data in hand | (b), (d) | **fatal** against §5.5 as a calibration |
| F7 | The random-damage raw draws for seed 0, which are what the spread is by definition, already exist in the record the A3 lock was cut from; the sizes and shape of the clause were chosen with that band visible | (b) | worth noting |
| F8 | The engagement precondition certifies nothing: a checkpoint passes "engaged" at 0.225 while scoring below the solver that cannot read the name (0.3227); and the text admits the margin and the second comparator were chosen knowing the data | (b) | worth noting |
| F9 | The positive cell is named H_self-location, the registered A3 positive bin's name, which carried discriminators this clause drops; §5.7's disclaimer will not survive a summary table | (c) | serious |
| F10 | The "located, wrong structure" cell is redefined: as ruled on 2026-09-19 it means the ablation improves the primary battery; §5.2 maps it to the other-directed condition falling more, and an improvement of the primary now lands nowhere | (c), (d) | serious |
| F11 | Magnitudes of S around 10 to 25 are expected under the input-channel lesion by arithmetic, and a monotone dose ladder on an input scaling is near-automatic; both will be read as many-sigma evidence of a structure | (c) | serious |
| F12 | Reporting the seen seeds "as a consistency check" yields "five of five" from three results whose sign and size are already known, and a non-firing generic-binding cell will be read as generic binding ruled out when F1 says it could not fire | (c) | serious |
| F13 | The outcome table does not partition the outcomes: (a) holding while (c), (e) or (h) fails lands nowhere; an improvement inside the band lands nowhere; two seeds of three lands nowhere; the A3 seed-dependent bin is not carried | (d) | serious |
| F14 | Condition (e) fails by construction: the random matched-subspace draws define σ as their own 95th percentile, so one draw in twenty exceeds it; the condition needs a quantifier, and the matched other-agent damage test needs a localized other-index subspace the stack cannot supply | (d) | **fatal** as written |
| F15 | The two twin calibration substrates cannot run: they were trained under a tokenizer whose ids differ from the A3 tokenizer on 72 of 105 tokens (every item, every answer slot, every query word), a token in every A3 turn has no id in their vocabulary, their embedding tables are 103 wide against 105, and no bridge exists in the source | (d), (b) | **fatal** against §5.5 as written |
| F16 | The untrained substrate risks a zero-spread null (no answers flip under small random damage), which under "maximum across substrates" yields either no σ or one no learned model can reach; the control diagnostic failed on exactly this on 2026-09-17 and §5.5 has no degeneracy precondition | (d) | serious |
| F17 | Condition (f)'s validity gates have no A3 implementation and were never applied to the input-channel lesion on any seed; applied for the first time on the fresh seeds they may void every verdict, and not applied they are decorative | (d) | serious |
| F18 | The random baseline is not matched to the input-channel lesion in rank, norm, layer or position; "the same rank and the same norm, at the same layers" has no meaning for zeroing a projection that injects at three positions | (d), (a) | serious |
| F19 | The evaluation harness returns battery means only; per-cell pairing, the within-run baseline and the ladder are a new instrument whose first run would be the verdict, against the known-answer rule of 2026-09-16 | (d), (c) | serious |
| F20 | The lock guard as built cannot hold a σ lock (it requires θ and δ per battery against one calibration record); the evaluation seeds that define the 800 episodes on the fresh seeds are not part of the lock | (d), (b) | worth noting |
| F21 | The clause reads "seeds 3 and 4, both"; the ruling is three seeds, and the text does not say three of three or what a not-testable seed does to the across-seed condition | (d) | worth noting, must be fixed before registration |
| F22 | The matched-cell restriction reads the other-directed query on a subpopulation (episodes where the model revises) on which its intact level is unmeasured, while the engagement precondition is written on the whole battery | (d) | worth noting |

**The single most serious finding is F1 together with F6.** Under the
only damage operation the programme can currently read, the clause is
satisfied by arithmetic on any checkpoint like the three in hand, and
the calibration that is supposed to set its bar sets nothing. The
amendment's informative application, a localized lesion, is gated
behind a stack that has found nothing anywhere. So the half of A4 that
can be read cannot lose, and the half that could lose may never be read.

---

## (a) Ways a model with no ownership-specific structure satisfies the clause

### F1 — Under the input-channel lesion, the boring cell is unreachable

**Severity: fatal against the claim in §5.2 and §6.5 that "for the
first time the generic-binding cell can fire". ARGUED, from committed
numbers.**

The generic-binding cell requires S below σ with the self-directed drop
positive: the two conditions fall alike. Consider what "alike" can mean.

The other-directed drop per cell is at most the intact score minus
chance. On the seen seeds the control's intact scores are 0.2877,
0.3057 and 0.3195 (the endpoint findings, `seeds-endpoint-findings.md`),
so even a lesion that destroyed the control all the way to chance gives
a mean other-directed drop of at most about **0.19**. The self-directed
drop under the input-channel lesion is 0.37 to 0.43 on the same seeds
(intact 0.5683, 0.5633, 0.5738; lesioned 0.1988, 0.2015, 0.1447; the
proposal's own C1). C1 also says the three intact scores land within
0.011 of one another, and the seeds are byte-identical recipes, so the
fresh seeds are expected to look the same.

So the mean of the per-cell difference is at least about **0.17 raw in
the worst case for the hypothesis**, the case where the control is
annihilated, and about 0.30 in the case the record actually shows
(control falls about 0.06 to 0.07, see F5). The denominator is the
spread of that mean under random residual damage. The only band on the
record for this design is the A3 lock's 95th-percentile absolute
corrected drop on the primary battery, 0.1777, which is about 0.049
raw; a standard deviation is smaller than a 95th percentile, so the
spread is of order a few hundredths. S is therefore at least 3 to 5
even if the control collapses to chance, and around 10 in the case the
record shows, against a σ near 2 (F6).

**The generic-binding cell cannot fire under the input-channel lesion
on any checkpoint whose control sits where all three seen ones sit.**
Not "will probably not": cannot, because the comparator has about a
fifth of the self-directed battery's room to fall. This is the same
shape as the finding that killed the ratified A3 differential in
red-team pass 3 (RT-21, the two batteries' unequal ceilings biasing the
differential so a generic binder read as self-location): there the bias
came from unequal ceilings, here from unequal rooms to fall. The
registered metric's ceiling correction was adopted to remove exactly
this bias; §5 removes the ceiling and the bias returns in a softer form.

Put as the workspace's own wager rule asks: what result on seeds 3 to 5
would count against H_self-location under the input-channel lesion?
Only the self-directed battery not collapsing, which is C1's settled
result not replicating. A clause that can only lose by an already
replicated result failing to replicate a fourth time is not a wager on
the question it is named for.

### F2 — "Matched content" is not a matched condition; the lesion strikes where one score is read and not the other

**Severity: fatal against the reading "the damage is specific to the
ownership-dependent condition". ARGUED from the code.**

§3's case for Candidate B is that both queries live in the same episode:
"same turns, same items, same rule, same episode; only the agent whose
commitment is queried differs." That is true of the episode text. It is
not true of the two measurements.

- The self-directed score is read **at the model's own revision turn,
  inside the episode**, as the most likely of eight slot tokens at that
  position (`train_a3.eval_heldout`, the T_act block). That position is
  an enacted position: it is exactly where the acting channel injects.
- The other-directed score is read **at the answer position of a
  question appended after the whole episode** (`model.score_choices`,
  the `<ans>` position), several turns downstream of every injection.
- The self-directed answer requires identifying which of four earlier
  assignments is the model's own; the other-directed answer is one
  visible turn plus the rule, which the ceiling measurement showed a
  name-keyed lookup solves at 1.0.

The input-channel lesion zeroes the injection at the model's own act
positions. It changes the residual stream at the very tokens where the
self-directed score is read and leaves the appended question's tokens
unaltered except through attention. Any disruption that is local to the
altered positions, whether or not it carries anything about ownership,
lowers the self-directed score more than the other-directed one and
satisfies (a), (b), (g) and (h). The random baseline in §5.4(a) cannot
catch this: the Gate 0 operators act at **all** non-pad positions at
layers 3, 4, 5, 7 and 8 (`null_calibration.install_residual`), so the
null describes damage spread evenly, and a position-concentrated lesion
is outside the family the null was drawn from.

The record already says the lesion is at least partly a general
disruption. Under the input-channel lesion the control falls on every
seen seed, by about 0.06 to 0.07 raw (F5), and the state battery, which
has nothing to do with ownership, falls about 0.07 raw on seed 2 (the
corrected drop of 0.0769 reported in the endpoint findings, against a
state-battery range of about 0.93). Everything falls; the clause asks
only whether the self-directed condition falls most, and F1 says it
must.

The registered text already concedes the point for this lesion.
Registration revision 8 of Amendment A3 says the acting channel "marks
positions, and attending back to marked positions is a re-readable
pointer rather than a carried binding. Both routes need the channel, so
the wire lesion cannot separate them." A4 proposes to read its verdict
on the wire lesion.

### F3 — Under a localized lesion, the clause has dropped every discriminator the registered positive bin carried

**Severity: serious. ARGUED.**

The registered H_self-location signature in A3 §3.5 required, besides
the differential: the other-index control (a subspace localized for a
named non-self agent, matched in rank and probe accuracy) below
threshold; the random controls below threshold; the swap probe moving
the action with the patched identity; probe-patching convergence; and
for the tag bin, the mid-episode re-indexing probe. §5.2's cell
requires (a) to (h), none of which is the swap probe, the convergence
requirement or the re-indexing probe. Condition (e) names the other-
agent damage test, but only as a non-firing requirement, and see F14 on
whether it can be evaluated at all.

So under a localized lesion the following satisfy (a) to (h) with no
self-index anywhere:

- **An act-marker echo** (A3 red-team item R1): a subspace carrying
  "this position was enacted", propagated forward. Removing it hurts the
  self-directed query, which needs to find the enacted turn, and not the
  other-directed query, which does not. S is large, direction positive,
  the state battery untouched.
- **A mine-bit tag** (A3 red-team item R4 and the H_tag bin): an
  indispensable address. The registered discriminator for it, the
  re-indexing probe, is not in the clause.

The A4 table has no H_tag cell, no H_self-reference-only cell and no
H_diffuse cell. A localized-lesion positive under A4 is therefore a
weaker claim than a localized-lesion positive under A3, while carrying
the same name (F9).

### F4 — The second comparator fails in the same way as the first

**Severity: serious. ARGUED, with one measured number.**

Condition (c) requires the same statistic with the state battery in
place of the other-directed query to reach σ too, "so that the verdict
cannot rest on a comparator that is matched but inert, nor on one that
is lively but unmatched." The state battery is: not content-matched (it
asks about the last parcel mentioned or a count of slot uses); not
chance-matched (0.091 against 0.125); not position-matched (read at the
appended question, like the control and unlike the self-directed
query); and at ceiling, 0.998 intact. It fails the F2 test for the same
reason the control does, and it fails an F1-style test in the opposite
direction: a battery at 0.998 with a range of 0.93 can fall far, but a
disruption that spares appended questions will not move it. And it did
move under the input-channel lesion: about 0.07 raw on seed 2
(MEASURED, from the seed-2 endpoint record,
`a3-gates/endpoint_a3_30m_seed2.json`, via the corrected drop reported
in `seeds-endpoint-findings.md`). The clause's (c) still passes on that
seed by arithmetic, because 0.37 minus 0.07 over a spread of a few
hundredths is far above 2. Two comparators that pass for the same
structural reason are one check.

---

## (b) Ways the clause is fitted to seeds 0 to 2 despite the exclusion

### F5 — The numerator on the seen seeds is already in committed records, including the control under the lesion

**Severity: serious. MEASURED.**

§5.5 commits that "the separation statistic is not computed on seeds 0,
1 or 2 at any point before the registration commit and the lock" and
that the calibration uses "not their battery scores, not their measured
noise, not their damage records." But the endpoint records for all
three seen seeds already store the control battery's score **under the
input-channel lesion**, across six evaluation seeds at 800 episodes:

| checkpoint | control intact | control under the lesion | record |
|---|---|---|---|
| pilot (seed 0) | 0.2877 | 0.2283 | the pilot's endpoint validation record, `a3-gates/endpoint_validation_pilot.json` |
| seed 1 | 0.3057 | 0.2342 | the seed-1 endpoint record, `a3-gates/endpoint_a3_30m_seed1.json` |
| seed 2 | 0.3195 | 0.2617 | the seed-2 endpoint record, `a3-gates/endpoint_a3_30m_seed2.json` |

The same records hold the primary and state batteries intact and under
the lesion. The endpoint findings quote the intact column and omit the
lesioned column, but the numbers are in the committed files, and the
proposal's C1 quotes those same records. So the sign and approximate
size of the separation on the seen seeds, about 0.30 raw in the
numerator, is known to whoever wrote §5, whether or not a script named
"separation" was ever run. The commitment not to compute the statistic
protects only the per-cell pairing and the exact spread. The ruling
annotation's addition, "the prior is stated now: H_self-location is the
predicted cell", is the honest form of this and should be the
registered one: **pre-state the expected value of S on the fresh seeds
from the seen record, and say what result would surprise.** A
prediction made from data in hand is fine when labelled; a claim of
ignorance is not.

### F6 — σ is self-normalizing, so the calibration decides nothing, and the quantity that decides is unspecified

**Severity: fatal against §5.5 as a calibration. ARGUED, with
arithmetic.** *(The ruling annotation on disk says the other pass
reached "the threshold lands near 2" too; this pass reached it
independently and adds the second half, which is where the fitting risk
actually lives.)*

§5.4(a) and §5.5 define, on each calibration substrate: run the random
sweep; for each draw compute the mean of the per-cell difference; take
the standard deviation of that mean across draws as the spread; divide
each draw's mean by the spread to get that draw's S; take the 95th
percentile of |S|. But a set of numbers divided by its own standard
deviation has a 95th percentile of its absolute value near 2 whenever
the numbers are roughly bell-shaped, and near 1.6 to 2.3 across the
shapes 20 to 120 draws can take. **The threshold is a property of the
shape of the null, not of the substrate.** Calibrating it on twins, an
untrained model, or the seen seeds gives the same number to within a
few tenths. Excluding the seen seeds from this step protects nothing,
because the step determines nothing. "The maximum across substrates"
picks whichever null had the heaviest tail, which is not what "most
permissive substrate" means.

What actually sets the bar is the spread used **when S is read on a
fresh seed**, and §5.1 defines it only as "the standard deviation of
that same mean across the matched-strength content-blind random-damage
baseline." It does not say:

1. **On which checkpoint** the spread is measured for a fresh seed: on
   the fresh seed itself (a within-run random sweep after the lock), or
   frozen from the calibration substrates. The two differ a lot: Gate 0
   measured a non-learning twin's null band on a self battery at 0.379
   corrected against 0.0095 on a binder, and an unlearned model's
   answers flip under random damage far more than a learned model's in
   raw terms too. Frozen from twins, the spread is inflated and S on
   the fresh seed is deflated; measured on the fresh seed, the whole
   construction is a within-run z-test with a threshold of 2 that could
   have been written down in one line.
2. **Over which draws**: the 120 draws pooled, or per layer-rank-
   operator cell of 20. Random damage at rank 16 in layer 3 moves
   batteries more than rank 4 in layer 8; the pooled spread and the
   per-cell spreads differ by a factor, and "the" spread is whichever
   is chosen.
3. **Whether the spread is across draws or across cells.** The text
   says across draws; a reader of §5.1 alone could take the spread of
   D(e) across the 400 cells, which is a different quantity by a factor
   of about 20.

Each of these is a choice that can be made after seeds 0 to 2's random
draws have been looked at (they have been, F7), and each moves S by a
multiplicative factor. This is the route by which the clause can be
fitted, and the seeds 0 to 2 exclusion in §5.5 does not close it,
because it is not in the calibration step.

### F7 — The seen seeds' random-damage draws already exist and were the source of the A3 lock

**Severity: worth noting. MEASURED.**

The A3 pilot's null-calibration record
(`null-calibration/a3_pilot_seed0.json`, 120 draws, 800 episodes, 6,047
seconds on the Mac) stores for every draw the raw accuracy of all four
batteries, including the control. The spread §5.1 divides by is, by
definition, the spread of those raw accuracies' difference across draws
on a checkpoint. So the "measured noise" §5.5 says it excludes is
already on disk for seed 0, it was read to cut John's committed lock of
2026-09-16 (`null-calibration/theta_delta.lock.json`), and its band on
the primary battery, 0.1777 corrected, about 0.049 raw at the 95th
percentile, is quoted in the proposal. The 800-episode and 400-cell
sizes, the choice of spread rather than ceiling in the denominator, and
the expectation that the input-channel lesion clears the bar were all
made with that band visible. None of that is a sin. Writing "on no
other data" as though it were not is.

### F8 — The engagement precondition certifies nothing, and the admitted data-informed choices should be named as such

**Severity: worth noting. ARGUED.**

Condition (d) requires the control's intact score to exceed chance by
0.10, so 0.225. The registered name-blind reference solver scores
0.3227 on this battery, and the control diagnostic of 2026-09-17
(`control-diagnostic-findings.md`) found the seen models bind by name,
partially, and land near that level by coincidence. A checkpoint can
therefore pass "engaged" while scoring below a solver that cannot read
the name in the question. As a floor it certifies that the model is
doing something above guessing; it does not certify that the
comparator can register damage to name-keyed binding, which is what a
comparator is for. The proposal says plainly it knows the margin passes
on all seen seeds and that the second comparator was added knowing
which battery learned; those admissions are the right practice, and
the registered text should carry them, not just the memo.

---

## (c) Ways a verdict later gets over-read

### F9 — The positive cell carries the registered positive bin's name

**Severity: serious. ARGUED.**

A3's H_self-location required a localized subspace, the swap probe,
convergence and the tag discriminator, and read "the network acquired a
structure that indexes its binding to its own center". A4's
H_self-location requires (a) to (h) on the input-channel lesion and,
by §5.7, must not be read as any acquired structure at all. Same
label, weaker claim, and the weaker claim is the one that will be
produced. §5.7 is a paragraph; the cell name is what goes in the
results table, the status file and the write-up's first sentence. The
cell should be named for what it measures, on the order of "the
ownership input is specifically load-bearing for the self-directed
condition", and H_self-location should stay reserved for the registered
localized result.

### F10 — The "located, wrong structure" cell is redefined

**Severity: serious. ARGUED against the ruling text.**

John's ruling of 2026-09-19 (the sensitivity rule, recorded in
`STATUS.md` §5 of the 2026-09-19 section) defines the fourth cell as:
"probe passes and the ablation *improves* the primary battery beyond
noise = located, wrong structure." §5.2's table defines LOCATED, WRONG
STRUCTURE as S at or below minus σ, "the damage hurts the other-directed
condition *more*", and says it "carries over the fourth cell added by
the 2026-09-19 ruling." Those are different events. Under §5.2 an
improvement of the primary battery is excluded from the positive cell
by (b), excluded from generic binding by the same sign requirement, and
lands in the wrong-structure cell only if the separation happens to
fall below minus σ; a small or moderate improvement lands nowhere
(F13). The ruled event has lost its cell while its name was reused for
another. This is the kind of drift the "annotate, never rewrite" rule
exists to catch, and it should be corrected before the text is
registered rather than after a result lands in it.

### F11 — The magnitudes that will be reported invite a many-sigma reading

**Severity: serious. ARGUED.**

By F1's arithmetic, S under the input-channel lesion on a checkpoint
like the seen ones is of order 10, and could be 20 or more if the
within-run spread is small. Reported as "S = 18 against σ = 2.1" it
reads as nine standard deviations of evidence for a self-index. What it
is evidence of is that an input the task was built to require is used
by the model that learned the task, which C1 already established at
seven to nine times a locked threshold. The partial-damage ladder,
reported on the same lesion, will be monotone almost by construction,
because scaling an input's projection by 0.75, 0.5, 0.25 and 0 is a
smooth reduction of the same signal; a clean curve will then be shown
as dose-response evidence of a structure. Two pre-statements would
inoculate: the expected S from the seen record (F5), and the minimum
S reachable under the null hypothesis on this checkpoint (F1's bound
when the control collapses to chance), so a reader can see how far
above "could not lose" the observed number sits.

### F12 — Five of five, and generic binding "ruled out"

**Severity: serious. ARGUED.**

Condition (i) of the recommendation scores seeds 0 to 2 after the
verdict "as a consistency check". Their sign and size are known now
(F5), so they are not checks; adding them to the fresh three produces
"five of five seeds" in a table, and the distinction between seen and
fresh will not survive a second retelling. Report them under a separate
heading, labelled seen and verdict-free, never in the same table.
Likewise, the generic-binding cell not firing will be read as "generic
binding was tested and ruled out". F1 says it could not have fired on
this comparator. The write-up must say which cells were reachable on
the checkpoint read, not only which fired.

---

## (d) Ways no verdict is produced on seeds 3 to 5

### F13 — The outcome table does not partition the outcomes

**Severity: serious. ARGUED.**

§5.2 says "with no dead cell in the set". Four outcomes have no cell:

1. **(a) holds but (c) fails**, the state comparator not reaching σ.
   Not the positive cell (needs all), not generic binding (needs S
   below σ), not wrong structure, not NOT TESTABLE (which names only
   (d), (f) and (g)).
2. **(a) holds but (e) fails**, a control lesion reaching σ. Same gap.
3. **The primary battery improves inside the band**: mean self-directed
   drop at or below zero with S above minus σ. Excluded from every
   named cell by sign.
4. **Two seeds of three satisfy the clause**, or one seed is NOT
   TESTABLE and two pass. (h) requires all; the A3 bins "seed-dependent"
   and "unstable" are not carried into the table.

Red-team pass 3 found the same defect in A3's bins (RT-22, bins neither
exhaustive nor exclusive) and it was fixed by adding cells. The same
fix is needed here before registration, because an outcome with
nowhere to land gets explained away, as the registration revisions of
A3 put it.

### F14 — Condition (e) fails by construction, and half of it cannot be evaluated

**Severity: fatal as written. ARGUED.**

(e) requires that "neither the matched other-agent damage test nor the
random matched-subspace damage tests may themselves reach σ on the
self-directed query."

- The random matched-subspace draws are the population whose 95th
  percentile σ is. On the checkpoint being read, a fresh sweep of 120
  draws will produce about six that exceed σ if the read checkpoint's
  null has the same shape as the calibration substrates', and more if
  it is wider (F6 says it may be). Read literally, (e) fails on every
  checkpoint. It needs a quantifier: the 95th percentile of the fresh
  sweep, the median, or all draws below some other bound.
- "Reach σ on the self-directed query" applies a separation threshold
  to a single-condition quantity. Either it means S computed with the
  random draw as the damage operation, in which case it is the same
  test as (a)'s null, or it means the self-directed drop alone against
  σ, which is in different units.
- The matched other-agent damage test requires an other-index subspace
  localized for a named non-self agent (A3 §3.1, L2a). The localization
  stack has found no ownership structure on any seed and the blind
  positive control returned NOT TESTABLE (`blind-control-findings.md`).
  If no other-index subspace can be localized, (e) cannot be evaluated,
  and the text does not say whether that is NOT TESTABLE or (e) waived.
  Under the input-channel lesion there is no defined other-agent
  analogue at all (the channel injects only at own positions; the
  re-indexing probe is the nearest thing and is not named).

### F15 — The two twin calibration substrates cannot run as written

**Severity: fatal against §5.5 as written. MEASURED.**

§5.5's substrates 1 and 2 are the register-less twin checkpoints from
the earlier wave, `artifacts/pilot_a1_30m_seed0_twin/…` and
`…seed1_twin/…`, to be run on the A3 batteries at 800 episodes. Static
checks:

- The twins were trained under `encoding.py`; the A3 harness encodes
  with `encoding_a3.py`. Comparing the two vocabularies: **103 tokens
  against 105, and 72 of the 105 A3 tokens carry a different id** in
  the old vocabulary or none at all. The A3 tokenizer inserts "by"
  before the item names, so every item name, every one of the eight
  answer slots and every query word is shifted. Under the A3 encoding
  the twin reads `parcel_1` as its `parcel_2`, `bay_A` as its `bay_B`,
  `bay_H` as its `where`, and ids 103 and 104 fall outside its table.
- "by" appears in every A3 turn (`assign <item> to <value> by
  <marker>`, registration revision 2). The old vocabulary has no id for
  it.
- The checkpoints' stored configuration: twin `vocab: 103`, A3 seed 0
  `vocab: 105` (read from the `.pt` files' `cfg`). The twin's token
  embedding and output head are 103 wide.
- No bridge exists: a search of `src/` for any remapping between the two
  vocabularies finds none; `encoding_a3.py`'s own self-test only asserts
  that the registered vocabulary was not edited.

So the twins cannot be fed A3 episodes without new code that maps ids,
and whatever mapping is written after registration decides what the
twin "sees" and hence what its null looks like. Even with a mapping,
a model reading a scrambled or shifted vocabulary is not "a trained
model out of distribution" as §5.5 describes it; it is a random reader
whose answers are noise of an unknown shape. The precedent §5.5 cites,
Gate 0 calibrating on the existing checkpoints, ran those checkpoints
on **their own** grammar and tokenizer. Only the untrained substrate
survives, and see F16.

### F16 — The untrained substrate risks a zero-spread null, and the maximum rule turns that into no threshold or an unreachable one

**Severity: serious. ARGUED, with this week's precedent.**

An untrained network at this configuration produces, at the revision
position and at the answer position, whatever its random head favours
among eight slot tokens; that choice can be nearly constant across
episodes or flip on small perturbations, and which of the two is not
known until it is run. Rank-4 to rank-16 random residual damage at five
layers is small relative to the residual norms (the A3 pilot record
shows removed norms of 10 to 18 per layer against reference means of 66
to 205). If few or no per-cell scores flip, the per-cell difference is
zero almost everywhere, the spread across draws is near zero, and S is
either 0/0 or a handful of flips divided by almost nothing. §5.5 then
takes the maximum 95th percentile across substrates, so a degenerate
untrained null gives either no σ or a σ far above anything a learned
model's shaped null reaches. The control diagnostic of 2026-09-17
failed on exactly a zero-spread null by construction
(`control-diagnostic-findings.md`), and that document's own lesson was
to write a non-degeneracy precondition into every null. §5.5 has none.

### F17 — Condition (f)'s validity gates have never been applied to this lesion and have no A3 implementation

**Severity: serious. MEASURED.**

(f) carries over "verbatim from Amendment A3 §3.3" the neutral-episode
likelihood bound, the long-generation degeneracy probe and the
out-of-distribution-inconclusive branch. A search of `src/` finds no
neutral-episode likelihood bound and no degeneracy probe implemented
for the A3 grammar (the only "degenerate" checks are the zero-spread
guards in the control diagnostic and the blind control). The endpoint
records for seeds 0 to 2 carry no such field among their 110 keys. So
the input-channel lesion has never been tested against these gates on
any seed. Zeroing an input the model was trained with moves every
battery (F2, F5), so it is plausible it also moves the neutral-episode
likelihood past a 95th-percentile random-damage bound. If (f) is built
and applied on the fresh seeds, all three may return NOT TESTABLE on
the first application of a gate that was never run on the seen seeds;
if it is not built, (f) is a sentence. Either the gates are implemented
and run on the seen seeds before registration, with the result
reported, or (f) should say what it actually binds.

### F18 — The random baseline is not matched to the input-channel lesion in any stated sense

**Severity: serious. ARGUED from the code.**

§5.4(a) describes the baseline as "random removals of the same rank and
the same norm, at the same layers" as the damage operation. For a
localized subspace lesion that is meaningful. For zeroing `act_proj`,
a 448-by-448 projection that injects at the model's own enacted
positions only, it has no rank in the residual stream, no layer among
3, 4, 5, 7 and 8, and a norm concentrated at three positions rather
than spread over all of them. The Gate 0 machinery applies random
damage to all positions at fixed layers with strengths set by a
reference pass. A3's endpoint used that sweep as the input-channel
lesion's null anyway, which is a defensible precedent as long as the
text says "the registered residual sweep, unmatched to this lesion";
§5's text promises a matched baseline the machinery cannot produce, and
a reader will take "matched-strength" at its word.

### F19 — Per-cell scoring is a new instrument, and its first run would be the verdict

**Severity: serious. MEASURED.**

The A3 evaluation function returns per-battery accuracies rounded to
three places and nothing per episode (`train_a3.eval_heldout`); the
endpoint script stores per-evaluation-seed means. The clause needs a
per-cell record of intact and damaged correctness for two or three
batteries on the same 800 episodes, the pairing of the self-directed
read (inside the episode) with the appended reads (after it), the
within-run baseline, and the ladder. That is a new scoring path. The
known-answer rule of 2026-09-16 (`lock_guard.require_known_answer_pass`
and its ruling) exists because a new pipeline returned five probes
below their nulls and nothing separated an insensitive stack from a
bug. §5 registers no known-answer test for the separation script. A
cheap one is available and should be registered: the new script's
per-cell records for seed 0 must reproduce the seed-0 endpoint means
for every battery, intact and lesioned, to the rounding, before any
fresh seed is scored. (That reproduces published aggregates; it does
not compute the separation statistic on a seen seed.)

### F20 — The lock guard cannot hold this lock, and the evaluation seeds are outside it

**Severity: worth noting. MEASURED.**

`lock_guard.require_lock` (version 1) refuses a lock that lacks `theta`
and `delta` fields, requires a threshold entry for every battery about
to be read, and validates against exactly one calibration record by
hash. A σ lock carrying three calibration records and an exclusion
field is a new lock version and new guard code, written after
registration. §5.5 step 3's "through the existing lock-guard machinery"
is not literally available. Separately, the endpoint reads use six
evaluation seeds and report a spread; §5 does not say which seeds
define the 800 episodes the verdict is read on for seeds 3 to 5, and a
seed chosen after seeing the default-seed reading is a fit route. The
lock should carry the evaluation seeds.

### F21 — Two seeds in the text, three in the ruling

**Severity: worth noting; must be fixed before registration. ARGUED.**

Condition (h) reads "seeds 3 and 4, and must hold on both". John ruled
three fresh seeds. The registered text needs to say three of three (the
A3 rule), what a NOT TESTABLE seed does to the across-seed condition,
and where two of three lands (F13).

### F22 — The comparator is read on a subpopulation its precondition was not written on

**Severity: worth noting. ARGUED from the code.**

The other-directed and state queries are appended to every episode, and
their battery scores are over all 800. Matched cells exist only in the
roughly 400 episodes where the model's slot was drawn as a reviser. In
those episodes the model's own revision is visible and the named other
agent is one of the non-revisers or the co-reviser, so the
other-directed query's difficulty differs from the full battery's, and
its intact level on that subpopulation has not been measured. Condition
(d)'s 0.10 margin is written on the whole battery. The text should say
which population (d) is evaluated on and which the comparator's
"measured spread of change" (the ruling annotation's second addition)
is reported on.

---

## Two notes on time and money, because §5.5 depends on them

- **Calibration time.** The one A3 random sweep on the record took
  6,047 seconds for 120 draws at 800 episodes on the Mac. Three
  substrates is about five hours if the twins could run (F15), and a
  within-run spread on each fresh seed (F6, reading 1) is another 1.7
  hours per seed after arrival, before any verdict. That fits inside
  "lock before read" as ruled, but the lock cannot be cut before launch
  if the substrates need new code first, and the registration should
  say so rather than leaving §6.4's permission to cover it.
- **Nothing in this pass changes the cost estimate.** Every finding is
  fixable at $0 or is a reason not to spend.

---

## Kill case, in one paragraph

Under the only damage operation the programme can currently read, the
clause cannot fail on any checkpoint resembling the three in hand: the
comparator has a fifth of the self-directed battery's room to fall, so
the cell the repair exists to make reachable is arithmetically
unreachable, and the positive cell will fire with a many-sigma number
under the registered positive bin's name. The calibration that is meant
to set the bar sets a number near 2 on any substrate, and two of its
three substrates cannot be run because their tokenizer is not the A3
tokenizer. The application that would make the clause informative, a
localized lesion, is gated behind a stack that has found nothing on any
seed. So the $30 buys three more instances of C1's already replicated
result, relabelled. Close A3 on the record as it stands, state the
matched self/other contrast as the design's unmet requirement, and
register a separation clause only when there is a localized lesion to
read it on and a comparator that can fall as far as the battery it is
compared against.

## If it ships anyway: what §5 needs before it is registerable

Listed as remedies, not as amendment text; every one is $0.

1. Rename the positive cell for what it measures under the input-
   channel lesion; reserve H_self-location for the registered localized
   result (F9). Restore the ruled meaning of "located, wrong structure"
   and give the other-directed-falls-more event its own name (F10).
2. Make the outcome table exhaustive: cells for (a) holding while (c),
   (e) or (h) fails; for an improvement inside the band; for two of
   three; carry A3's seed-dependent and unstable bins (F13, F21).
3. Define the spread: on which checkpoint, over which draws, pooled or
   per cell, across draws not cells (F6). Say plainly that σ will land
   near 2 and why that is acceptable, or replace the self-normalized
   calibration with one that has content.
4. Replace the twin substrates or register the tokenizer bridge and its
   consequences before the lock (F15). Add a non-degeneracy precondition
   on every null and say what happens when it fails (F16).
5. Quantify condition (e) and say what happens when the other-index
   subspace cannot be localized (F14). Describe the baseline as the
   registered residual sweep, unmatched to the input-channel lesion, or
   design a matched one and register it (F18).
6. Either implement (f)'s gates for A3, run them on the seen seeds'
   input-channel lesion before registration and report the result, or
   strike (f) (F17).
7. Register a known-answer test for the separation script against the
   seed-0 endpoint means, to pass before any fresh seed is scored (F19).
   Extend the lock guard to a σ lock that also carries the evaluation
   seeds (F20).
8. Pre-state, in the registered text, the expected S on the fresh seeds
   computed from the seen endpoint records, and the minimum S reachable
   if the control collapsed to chance; report seen seeds under their
   own heading, never alongside fresh ones; state which cells were
   reachable on the checkpoint read (F1, F5, F11, F12).
9. State which population the engagement precondition and the
   comparator's reported spread are read on (F22), and carry the memo's
   admissions about data-informed choices into the registered text (F8).

---

*Authorship: this pass is Claude's. Nothing in it is a ruling. It does
not edit the proposal, does not write the amendment, and did not open
the amendment draft, the first red-team pass or the scoring script that
were on disk when it ran.*


===== FILE: experiments/06-mvm-0a-constructed-self-index/control-battery-proposal.md =====

# The control-battery decision — proposal for John, due 2026-10-04

*2026-09-17. **Advisory only; John adjudicates.** Decision-memo pattern:
constraint set, then what the audit changed, then candidates, then one
recommendation. Nothing here authorises spend or changes registered text.
Written after the seeds reported, as the roadmap specified.*

## The question

Three trained checkpoints. The ownership objective learns on all three and
its removal lesion is enormous. The control battery never learned on any
of them, so the registered clause comparing the two cannot be evaluated
anywhere. Does the programme open a registered Amendment A4 that makes the
control learn, or close A3 with partial discriminators and say so plainly?

## What is settled

| | pilot | seed 1 | seed 2 |
|---|---|---|---|
| primary, intact | 0.5683 | 0.5633 | 0.5738 |
| primary, channel zeroed | 0.1988 | 0.2015 | 0.1447 |
| corrected drop | 1.337 | 1.342 | 1.528 |
| control, intact | 0.2877 | 0.3057 | 0.3195 |

The primary result is not in doubt and is not marginal. The control's
failure is systematic rather than a seed lottery, which is what the wave
was run to find out.

## Four things the audit changed, and they matter more than the numbers

**1. The bar is higher than I have been saying, and I was wrong about it.**
The floor rule is not "the baseline must clear the ceiling." It is
`baseline − ceiling ≥ 0.10`. So the control needs **0.4227**, not 0.3227.
All three miss by 0.103 to 0.135, so no conclusion moves, but an A4
argument that merely clears 0.3227 would still leave the drop undefined.
My findings note said "below its own ceiling" and is corrected.

**2. The control's ceiling was never attack-verified.** The registration
says the ceilings are verified by the attack sweep. **The attack sweep
contains no control-battery code at all** — zero occurrences. It attacks
the primary battery only. The 0.3227 rests entirely on one reference
solver in the curriculum module.

**3. That reference solver is blind to the thing the question hands it.**
The control question **names** the agent it asks about. The solver that
sets the ceiling never uses that name; it enumerates the four agents'
successors and guesses among those not already visible. A solver that can
do ordinary name-keyed lookup answers correctly every time.

So 0.3227 is not a ceiling on the battery. It is the score of a solver
that cannot read names, and the battery's real ceiling is near 1.0.
**This is the deeper problem, and it cuts both ways.** It means the
control at 0.32 is far worse than it looked, since it is barely above a
solver that ignores half the question. It also means the metric's
denominator for this battery was never a meaningful quantity.

**4. The design warned about this and the warning was never acted on.**
The curriculum module's own documentation says the control's lookup
ceiling is **0.5**, not 0.3227, and says in terms that *"red-team pass 3
should weigh"* it *"since the H_generic-binding bin turns on the
difference between the two batteries' drops."* Red-team pass 3 ran. It did
not weigh this. The registered number and the module's own comment have
disagreed since before the first dollar was spent.

## Why the control plausibly failed, from the code

It is **not** unsupervised. Each episode carries three queries and one is
chosen per training row, so roughly **one row in three** carries a control
target, one token each. Against that, the primary battery has a dedicated
full-weight loss term of its own on the roughly half of rows that carry an
action. The control gets perhaps a third of one shared term, with two easy
queries soaking up most of it.

Three further asymmetries, all in the code:

- **The primary battery has a private route the control does not.** The
  acting channel marks the model's own earlier value positions directly.
  The control must bind a name to a value across turns by ordinary
  attention, with no such help.
- **The rendering was reversed for the primary battery's benefit.** The
  speaker's name was moved after the value to kill a name-reading shortcut
  on the primary battery. The consequence for the control, which must now
  attend backwards from a name to a value two tokens earlier, was never
  revisited.
- **The answer appears in no turn.** It must be retrieved and then
  transformed by the revision rule. Retrieval and arithmetic both, from
  one supervised token.

## A correction on the money, in the programme's favour

I wrote in the seeds findings that an A4 needing new runs "must make that
argument explicitly" against the single-amendment ceiling rule. **That was
misleading and is withdrawn here.** The rule bars a *raise* above $400. An
A4 that fits inside the existing ceiling is not a raise and needs no cap
amendment at all.

| envelope | spent | remaining |
|---|---|---|
| A2 ceiling | $215.7 | **$184.3** |
| A3 hard stop | $34.31 | **$65.69** |

Three retrained seeds cost **$27 to $39** at measured rates. That fits
inside both, comfortably. Money is not the binding constraint on this
decision, and I should not have implied it was.

## Candidates

**A. Close A3 with partial discriminators.** Report the primary result,
the instrument audit, and the undefined comparison. *Cost $0.* Honest, and
weaker than it sounds: the discriminators that do not need the control are
the matched other-agent lesion, the random matched subspaces and the swap
probe — all of which run through a localization stack that has so far
found nothing, with probes below their own nulls and an ablation that
improved the battery it was meant to damage.

**B. Eval-side A4: divide by chance instead of the ceiling.** *Cost $0.*
At chance all three checkpoints would clear the floor and the comparison
would become computable. **Reject.** The ceiling denominator was itself a
registered revision made because dividing by chance manufactured a
spurious differential. Changing it back after seeing that it blocks the
result is fitting the rule to the data, which is the thing this programme
exists to not do. It would be the third time in two days that a rule of
mine was found wanting by the data, and the first two were reported rather
than repaired for exactly this reason.

**C. Retrain with the control properly supervised.** *Cost $27–39, three
seeds.* One change: give the control its own loss term or oversample it,
instead of a third of a shared one. No grammar change, so the frozen
batteries, the cue gates and the attack sweep are all unaffected.

**D. Retrain with a scaffolded intermediate query.** *Cost $27–39 plus
re-freezing batteries.* Teach plain name-keyed retrieval before layering
the rule on top.

**E. Train longer or bigger.** **Fenced by the registration**, which says
the finding is "unlearnable at this scale under this curriculum" and never
a silent scale bump.

## Recommendation

> **ANNOTATION, 2026-09-17, later the same day. The candidates below are
> MOOTED and the recommendation is superseded, though its one operative
> instruction was right.**
>
> The ceiling measurement John made a precondition has now run. The
> control battery's ownership-blind ceiling is **1.0**, reached by two
> independent solvers, with both known-answer checks reproducing their
> registered values exactly first.
>
> A defined drop needs a baseline of 1.10, so **the control's drop is
> undefined for every possible model** and the registered differential
> clause was never computable, at any budget, on any architecture. It has
> been unsatisfiable since registration.
>
> **So options C and D below are moot.** Both aimed at making the control
> learn, and a perfectly learning control would change nothing. I was
> proposing to spend $27 to $39 repairing the wrong component. What caught
> it was John's instruction to measure the ceiling before opening an
> amendment, and the recommendation below to run the free thing first.
>
> The October question is no longer whether to make the control learn. It
> is whether the clause can be repaired at all, and whether that repair is
> a metric change rather than a training change. See
> `ceiling-measurement-findings.md`.

**Do the free diagnostic first, then decide between A and C. Do not spend
yet.**

The audit produced a hypothesis with a sharp, free test. The control fails
for one of three reasons: the model cannot do name-keyed retrieval at all,
it can retrieve but not apply the successor rule, or the reversed
rendering defeats the retrieval specifically. **These are distinguishable
on the checkpoints already in hand, locally and for nothing**, by asking
the trained models plain lookup questions without the rule step and
comparing against the control's own score.

That matters because option C is a bet that supervision is the binding
constraint. If the diagnostic shows the models cannot retrieve by name at
all, more supervision on the same rendering is likely to buy little and
option D becomes the honest candidate. If they retrieve well and fail only
at the rule step, C is well targeted and cheap.

**Whichever way the decision goes, register the ceiling defect.** The
control's 0.3227 was never attack-verified, is set by a solver blind to
the name the question supplies, and disagrees with the module's own stated
0.5. That is a defect in the registered instrument, independent of whether
A3 continues, and it belongs on the record either way. If A3 closes, it
belongs in the write-up as a limitation of the comparison that was never
available. If A4 opens, the ceiling must be measured properly first,
because an amendment built on an unverified denominator would inherit the
same problem.

**What I am not recommending.** I am not recommending the eval-side change
that would make the numbers work. It is available, it is free, and it is
the wrong thing to do.

## What this decision does not settle

Where ownership lives. Every result here comes from removing an input
channel, which shows the action depends on ownership without showing the
network built an internal structure carrying it. The localization work
that was meant to answer that is unvalidated at this scale, and no
control-battery decision changes it.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-control-learnability-packet.md =====

# Review packet — the control-learnability pilot (Gate B, tier 1)

*Prepared 2026-09-20 (Pacific) under `docs/outside-review-protocol.md`.
Gate B: an interpretation that changes program direction, reviewed before
it enters STATUS.md's current-state section. This one also feeds public
path step 4, the 2026-10-04 control-battery decision, so under Gate C the
proposal that carries that decision will cite this review.*

## The interpretation under review

From the session that ran the pilot (commits `062636e`, `a569a35`, both
on main):

> The control battery does not learn when properly supervised. It scored
> 0.3125 (sd 0.0240) after an intervention that quadrupled its per-row
> gradient weight and took its share of the query gradient from about a
> third to about two thirds. The three existing checkpoints, with none of
> that, scored 0.2877, 0.3057 and 0.3195. Against the pre-stated cells:
> 0.42 sd below the 0.3227 boundary, 11.98 sd below 0.60. The cell is DID
> NOT LEARN. Both secondary cells pass, so this is a real answer, not a
> failed intervention. Supervision was not the binding constraint. What
> is left are the explanations that are not about supervision: the
> reversed rendering, the missing private route, and an answer that
> appears in no turn.

The session's own qualifications, which the review should test rather
than take on trust: across six evaluation seeds the control ranged
0.2850 to 0.3460, so a rerun could formally land in PARTIAL; and the
control is not inert, since it falls under the lesion from 0.3125 to
0.2613.

## What the reviewer gets, and nothing else

All in `experiments/06-mvm-0a-constructed-self-index/` at commit
`a569a35`. Read in this order.

- `control-learnability-pilot.md` — the pre-statement, committed before
  the code existed (`7eee3c5`). The cells are read against this.
- `control-learnability-pilot-findings.md` — the findings under review.
- `a3-gates/endpoint_a3ctl_30m_seed0.json` — the full-budget endpoint
  (step 55,116), the record the cells are read on.
- `a3-gates/endpoint_a3ctl_30m_seed0_PARTIAL_step51500.json` — the
  partial-checkpoint endpoint, for comparison only.
- The training log and trajectory record for the run, wherever the
  findings file says they are.
- `src/train_a3.py` and `src/launch_ctl_pilot.sh` — the loss change
  (`ee7fc91`) and the launcher; the self-test that claims the off path is
  bit-identical to the old pooled term.
- `compute-ledger.md`, the two rows dated 2026-09-19 (pilot) and
  2026-09-20 (recovery) only.
- `gate2-pilot-findings.md` and `seeds-endpoint-findings.md` — the three
  comparison checkpoints' control scores.
- Registered text the interpretation is read against: `amendment-a3.md`
  (the control battery's definition, its ceiling, and §3.2) and
  `ceiling-defect-2026-09-17.md`.

Do not open: STATUS.md, `docs/`, the A4 files, any chat transcript, any
uncommitted file. Say at the top of the findings file what was opened.

## The brief (fixed text from the protocol)

Four parts, in this order, a table first in each, severity marked fatal,
serious, or worth-noting, and a one-paragraph kill case at the end whether
or not you think the interpretation should stand.

1. **Feasibility.** For every quantity the pre-statement names: is the
   0.3227 boundary the right number (it is the control's ownership-blind
   ceiling as registered; the 2026-09-17 defect says that ceiling was
   never attacked), is the 0.60 boundary reachable by this battery in
   principle, and did the intervention actually deliver the supervision
   it claims (per-row weight, share of rows), citing the training log or
   the code. A "verified" or "measured" claim with no record behind it is
   a fatal finding on its own.
2. **Satisfied by the wrong thing.** Every way DID NOT LEARN could be
   returned by a control battery that would learn under supervision: an
   intervention that did not reach the control's rows, a loss term on
   the wrong scale, an evaluation that cannot see what was learned, a
   ceiling boundary that is itself wrong.
3. **No verdict.** Every way the run could have failed to answer the
   supervision question and been read as answering it, including the
   seed-1-only design and the six-seed spread straddling the boundary.
4. **Over-reading.** What "supervision is not the binding constraint"
   will be read as claiming in STATUS.md, in the step 4 proposal, and in
   the paper, beyond what one seed at one weight setting measured. Say
   whether the finding supports narrowing step 4 to "option D or close
   A3", or whether a cheaper supervision variant is still live. Write the
   sentence that should go in STATUS.md.

Label every finding MEASURED or ARGUED. Continue the ledger numbering
from RT-51. Plain language throughout. Lookup allowed and flagged. Do not
soften findings to be polite.

## Filing

Findings to `reviews/2026-09-20-control-learnability-claude-worktree.md`,
verbatim, never edited after filing. Rulings go in `red_team_ledger.md`.
Nothing from this enters STATUS.md or the step 4 proposal until John
rules on it.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-control-learnability-claude-worktree.md =====

# Findings — the control-learnability pilot (Gate B, tier 1)

*Filed 2026-09-20 under the outside-review protocol, against the review
packet for the control-learnability pilot
(`reviews/2026-09-20-control-learnability-packet.md`). Verbatim once
filed. Rulings are John's and go in the red-team ledger
(`red_team_ledger.md`); nothing here is a ruling.*

## What was opened, and nothing else

Everything below was read at the commit the packet names — the ledger
commit that closed both spend rows (`a569a35`). I first checked that none
of the listed files changed between that commit and the current tip of the
main branch; none did, so the working copies are the right versions.

Opened, all inside `experiments/06-mvm-0a-constructed-self-index/`:

- the pre-statement (`control-learnability-pilot.md`)
- the findings under review (`control-learnability-pilot-findings.md`)
- the full-budget endpoint record (`a3-gates/endpoint_a3ctl_30m_seed0.json`)
- the partial-checkpoint endpoint record
  (`a3-gates/endpoint_a3ctl_30m_seed0_PARTIAL_step51500.json`)
- the trainer (`src/train_a3.py`) and the pilot launcher
  (`src/launch_ctl_pilot.sh`)
- the compute ledger (`compute-ledger.md`), the two rows dated 2026-09-19
  (the pilot) and 2026-09-20 (the checkpoint recovery)
- the two comparison write-ups (`gate2-pilot-findings.md` and
  `seeds-endpoint-findings.md`)
- the registered text the interpretation is read against: Amendment A3
  (`amendment-a3.md`) — the battery table in §2.5, the lesion protocol in
  §3.1 and §3.2, the pre-stated signatures in §3.5, and registration
  revisions 3 and 4, which carry the metric and the ceilings — and the
  registered ceiling defect (`ceiling-defect-2026-09-17.md`)
- the red-team ledger, to read its last entry number only, so this file
  continues the numbering correctly

**The training log and the trajectory record were not opened, because they
are not in the repository.** The findings file never says where they are,
which is the first thing to record. They do exist on the laptop, in the
run's artifacts folder alongside the checkpoint; I established that by
listing the folder and reading no file in it, because the packet forbids
opening uncommitted files and everything under `artifacts/` is excluded
from the repository by `.gitignore`. See finding RT-56.

**Not opened, as instructed:** the current-state document (`STATUS.md`),
the `docs/` folder, anything to do with the A4 clause, any chat
transcript, any uncommitted file. Two modules I wanted and did not take
because the packet does not list them: the episode generator
(`curriculum_a3.py`) and the encoder (`encoding_a3.py`). Two findings
below (RT-58 and RT-59) are limited by exactly that, and say so.

**Lookup: none.** No web search, no external source. Every number here is
computed from the files listed above, and every computation is shown.

**Severity across this review: eighteen findings — one fatal, ten
serious, five worth-noting, and two checks that came back clean and are
recorded as clean.** Numbering continues from the ledger's last entry
(`RT-51`), so this file runs from `RT-52` to `RT-69`.

---

## 1. Feasibility

*For every quantity the pre-statement names: is the boundary the right
number, is the higher boundary reachable at all, and did the intervention
deliver the supervision it claims.*

| id | finding | label | severity |
|---|---|---|---|
| RT-52 | 0.3227 is not a ceiling, and the registered text naming it is already recorded as defective — but it is still the right number for the cell it was used in | MEASURED | serious |
| RT-53 | The endpoint record states a floor rule the programme corrected three days before the run | MEASURED | serious |
| RT-54 | The 0.60 boundary is reachable in principle; the battery's real limit is near 1.0 | MEASURED | worth-noting |
| RT-55 | The supervision was delivered, exactly as claimed — the findings file cites nothing for it, and the endpoint record does not carry the run's settings | MEASURED | serious |
| RT-56 | The training log and the trajectory record are not in the repository, though the previous run's equivalent is | MEASURED | serious |

### RT-52 — the boundary is the right number wearing the wrong label

**MEASURED. Serious.**

The pre-statement, the findings file and the endpoint record all call
0.3227 the control battery's "ownership-blind ceiling". The programme's
own registered defect of 2026-09-17 says that is false, and says so in
the registered text itself: the attack sweep that Amendment A3 credits
with verifying both ceilings contains no control-battery code at all, so
the claim "verified by the attack sweep" covers the primary battery only.
The 0.3227 comes from one reference solver that never reads the marker
the control question supplies. The question names an agent; the solver
enumerates all four agents' successors on the item, strikes the ones
already visible as revisions, and guesses among the rest.

So 0.3227 is the score of a solver that cannot read names, and the
battery's real ownership-blind ceiling is near 1.0 and unmeasured.

**And yet the number is fit for the cell that used it.** "The control did
not learn name-keyed lookup" means precisely "it scores no better than a
solver that cannot read the name", and 0.3227 is that solver's score. The
pre-statement's own gloss is correct — "a battery at or below it has not
learned the task, whatever else is true." Nothing about the verdict turns
on the mislabel.

What does turn on it: a Gate B interpretation rests on a boundary the
programme formally registered as defective three days before the run, and
**the findings file never mentions the defect.** Anyone reading the
findings alone would take 0.3227 for a checked quantity. It is not one,
and John has already ruled that measuring this ceiling properly is a
precondition of any Amendment A4.

**Fix:** the findings file should cite the ceiling defect
(`ceiling-defect-2026-09-17.md`) and call 0.3227 what it is — the score
of a name-blind reference solver — everywhere it appears.

### RT-53 — the endpoint record carries a superseded rule

**MEASURED. Serious.**

The full-budget endpoint record describes the metric this way:

> floor rule leaves a battery undefined when its baseline is below its own
> ownership-blind ceiling

That is the rule as it was stated before 2026-09-17. The correction of
that date, recorded in the three-seed write-up
(`seeds-endpoint-findings.md`), says the floor rule is not "baseline
below ceiling" but **baseline minus ceiling below 0.10** — so the control
needs **0.4227**, not 0.3227, for its drop to be a defined quantity at
all.

No number moves: the control reads 0.3125, which is below both. But the
artifact that carries the reading encodes a rule the programme corrected
before the run was launched, and the same superseded sentence sits in the
partial-checkpoint record too. The consequence is not arithmetic, it is
that 0.4227 — the number that actually decides whether this battery is any
use to Amendment A3 — appears nowhere in the pilot's pre-statement,
findings or endpoint records. That omission does real work in part 4
below.

### RT-54 — the higher boundary is reachable, on an argument nobody has attacked

**MEASURED. Worth-noting.**

Checked and clear. Amendment A3's battery table puts chance on this
battery at 0.125 — a forced choice among eight. The ceiling defect
establishes that every turn renders the speaker's marker in plain text,
so a solver doing ordinary name-keyed lookup "answers correctly every
time". The battery's attainable score is therefore about 1.0, and the
0.60 boundary sits comfortably inside it. **The LEARNED cell was not set
at an unreachable number.**

The caveat is that "near 1.0" is analytic and explicitly unmeasured — the
defect memo says so in as many words — and the attack sweep has still
never been pointed at this battery. So "reachable in principle" rests on
an argument that has not been adversarially tested, which is the same
weakness RT-52 records at the other end of the scale.

### RT-55 — the supervision was delivered; the findings file cites nothing for it

**MEASURED. Serious, and explicitly not fatal — I found the record.**

The findings file's load-bearing claim is that "its per-row gradient
weight quadrupled and its share of the query gradient went from about a
third to about two thirds." It carries no citation whatsoever. The
packet's rule is that a measured claim with no record behind it is fatal
on its own. **It is not fatal here, because the record exists and I found
it — in the compute ledger's pilot row, dated 2026-09-19. But the findings
file does not point at it, and the endpoint record does not carry the
run's settings either.**

The claim itself is exactly right. I checked it two ways.

**From the code.** With the flag off, the query loss is the total loss on
the answer tokens divided by their count, so each of the 128 rows carries
one one-hundred-and-twenty-eighth of the term, and the round-robin gives
the control battery about one row in three — a share of about a third.
With the flag on at the settings used, half the batch (64 rows) carries
the control question, the control's own term is the average over those 64
rows, and that term is multiplied by 2. So each control row carries two
sixty-fourths, which is one thirty-second: **exactly four times**
one-one-hundred-and-twenty-eighth. By the same arithmetic the control's
total weight is 2.0 against the other batteries' 1.0, so its share of the
query gradient is **exactly two thirds**, up from a third. Both figures in
the findings are right to the digit.

**From the run.** The ledger records the query loss at step 500 as 3.433
for this run against 1.075 for the matched earlier pilot, and notes that
"other-term + 2 × control-term" predicts about 1.1 + 2 × 1.15 = 3.40.
That is direct evidence the split fired on the rented machine and fired at
the right scale, not merely that the flag was typed. The ledger also
quotes John's go verbatim with the two settings in it, records that the
trainer's self-test ran on the pod before any training step, and records
the measured pace at 0.6508 seconds per step against the earlier pilot's
0.6501 — so the flag cost nothing and the run was not short-changed.

**Fix, and it is cheap.** The trainer already saves the run's full
settings into the checkpoint. The endpoint record should echo the two that
matter — the control weight and the control fraction — so the artifact
that carries the reading is self-contained. As it stands, the only thing
tying that record to a run with the flag on is the output name.

### RT-56 — the log and the trajectory are not in the repository

**MEASURED. Serious.**

The packet asked for "the training log and trajectory record for the run,
wherever the findings file says they are." The findings file does not say.
Its only reference to the log is a claim sourced to it — "the trainer's
own log records both acts on consecutive lines" — with no path.

They exist. The run's artifacts folder holds the trainer's log, the
trajectory file and a complete copy of it, alongside both checkpoints.
Everything under `artifacts/` is excluded from the repository by
`.gitignore`, so **none of it can be cited at a commit**, and the packet's
own rule against uncommitted files put all of it outside this review.

Two things make this worse than a filing quibble.

1. **The previous run's equivalent is committed.** The A3 pilot's
   trajectory sits in the gates folder (`a3-gates/pilot_trajectory.jsonl`)
   at about 20 kilobytes. This run's is the same size and is not
   committed. The precedent exists and was not followed.
2. **The trajectory is the only record that could answer several
   questions this review had to leave open** — most of all whether the
   control battery was flat throughout or moved and came back, and what
   the loss did after step 1,000. The ledger preserves two points; the
   file has 109 evaluations.

The claim about the two log lines is itself fine, because the ledger
quotes them verbatim. The fix is one command, and it should be done before
this finding is quoted anywhere.

---

## 2. Satisfied by the wrong thing

*Every way DID NOT LEARN could be returned by a control battery that would
learn under supervision.*

| id | finding | label | severity |
|---|---|---|---|
| RT-57 | The intervention tripled the whole query loss against the action term, and nothing held that fixed | MEASURED / ARGUED | serious |
| RT-58 | The control rows are the first half of every batch, not a random half, for all 55,116 steps | ARGUED | serious |
| RT-59 | The split's correctness rests on "exactly one scored token per row", asserted in a comment and never tested | ARGUED | worth-noting |
| RT-60 | The evaluation can see what was learned — checked, clean | MEASURED | clean |
| RT-61 | The battery did not fail to learn; it converged on the name-blind solver | MEASURED | serious |

### RT-57 — a loss term on the wrong scale, and it is the whole query side

**MEASURED for the arithmetic, ARGUED for the consequence. Serious. This
is the most plausible route by which a battery that would learn returns
this number.**

With the flag off, the query part of the loss has total weight 1.0 and the
action term sits beside it at weight 1.0. With the flag on, the query part
becomes "other-term at 1.0, plus control-term at 2.0" — **total weight
3.0** — while the action term stays at 1.0. The ledger's own reading note
says this in passing, to stop anyone misreading the two loss curves side
by side, and it is right: the query loss went from about 1.08 to about
3.43 by construction.

But the pre-statement describes the action term as "unchanged". **Its
coefficient is unchanged. Its share of the gradient fell by about three
times.** Nobody wrote that down, and it is not a presentational point:

- Every parameter the four batteries share now receives a query signal
  three times larger relative to the action signal than on the checkpoint
  this run is compared against.
- The trainer clips the combined gradient to a fixed norm of 1.0 on every
  step. A query term three times larger means the clip bites at different
  moments and in different proportions, so the effective step size on
  shared parameters is not the same run to run.

There is no setting of this flag that raises the control's share while
holding the query side's total fixed. Even at a control weight of 1.0 the
query loss doubles, because the split replaces one average over all rows
with two averages added together. **The only neutral setting is off.** So
the dose and the rescaling arrived bundled, and the pre-statement's "one
coupling, stated rather than buried" — the state and syntax batteries
losing rows — names a different and smaller coupling than the one that
actually exists.

The state and syntax batteries finishing at 0.9960 and 1.0000 does not
clear this. Both were already at the top of their range and have room to
absorb a disturbance that the control battery, sitting near the floor, does
not.

**What would settle it:** a single arm at the same control weight and
fraction with the two terms renormalised so the query side still sums to
1.0. Same cost as the run already bought.

### RT-58 — the control trains on a fixed half of every batch

**ARGUED, and I could not settle it. Serious.**

The registered path assigns each row a question by rotating on both the
step number and the row's position in the batch, so over steps every batch
position carries every battery. The pilot flag replaces that with a fixed
positional rule: rows numbered below the halfway point carry the control
question and are marked as control rows; everything else round-robins over
the remaining two.

Whether that is harmless turns entirely on whether the episode generator
returns a batch in randomised order or in a systematic one. If episodes
come back ordered or blocked by any property — and the function is named
for balancing, which is what you do when you are allocating counts across
conditions — then **for all 55,116 steps the control battery trained on a
systematically biased half of the episode space and the state and syntax
batteries on the complement.** That is a mechanism by which the control
fails to learn for a reason that has nothing to do with how much
supervision it got, and it is introduced by the very change that was meant
to isolate supervision.

I could not check it: the episode generator is not in the review set.

The self-test does not close it either. It checks that half the rows are
control rows, that a control row carries the control question, and that a
non-control row never does. It never checks that the control rows are a
*representative* half. That check is one line, and the run is over.

**What would settle it:** generate one batch, group the first half and the
second half by whatever properties the generator balances, and compare the
two. Free, local, and it either clears the run or explains it.

### RT-59 — an untested assumption under the split

**ARGUED. Worth-noting.**

The split computes each row's loss by summing across positions and then
averaging across rows; the unsplit path averages across tokens. The two
agree only if every row carries exactly one scored token. The code says so
in a comment — "exactly one masked token per row, so summing over
positions gives that row's answer CE" — and nothing tests it.

The self-test's strongest claim is that with the flag off the query term
equals the pre-flag pooled term, to within a millionth. That is true and
it is also nearly vacuous: with the flag off, the code takes the same
branch it always took. The test that matters is the one on the split path,
and it was not written. If any row ever carries two scored tokens, the
control's term silently becomes a sum where the comparison is a mean.

A one-line assertion that every row's scored-token count is exactly one
would close it, and should be added before this flag is used again.

### RT-60 — the evaluation can see what was learned

**MEASURED. Clean, and recorded as clean.**

The control battery is scored by ranking the candidate answers within the
question's own choice set. That is an easier readout than the training
objective, which scores the answer token against the whole vocabulary. An
evaluation easier than the training signal cannot hide learning that the
signal produced. The endpoint used 800 episodes per draw, and every
question of every episode is scored, so the sample is the full 800 rather
than a third of it.

The spread across six draws (0.0240) is larger than the spread you would
get from sampling alone at that size (0.0164), which is what you expect
when each draw is a fresh set of items rather than a fresh subsample of
one set. That is the honest behaviour, and it means the quoted spread is
not an underestimate.

**No finding.** This route is closed.

### RT-61 — the battery learned the structure and none of the name

**MEASURED. Serious, as a misdescription rather than an error.**

Chance on this battery is 0.125. The name-blind reference solver reaches
0.3227. The control reads **0.3125** — which is **about 95% of the way
from chance to the name-blind solver**.

That is a far more specific result than "did not learn", and the findings
file does not state it. The model learned the entire procedure the
name-blind solver uses — form the candidate successors on the queried
item, strike the ones already visible as revisions, choose among what is
left — and learned **none** of the name-keyed lookup that would take it
past that solver. It is not near the floor. It is sitting exactly on the
name-blind solver's shoulder, and has been on all four checkpoints.

This matters because "DID NOT LEARN" is a cell label and will be read as
"learned nothing". The run measured something sharper and more useful:
**four times the supervision moved a battery that had already saturated
the name-blind procedure, and did not start it on the name.** Say that,
and the case for the remaining explanations — the reversed rendering, the
missing private route, an answer that appears in no turn — gets stronger,
not weaker, because all three are about reading the name.

---

## 3. No verdict

*Every way the run could have failed to answer the supervision question
and been read as answering it.*

| id | finding | label | severity |
|---|---|---|---|
| RT-62 | The matched comparison the design was built around is missing, and "bought nothing" is false | MEASURED | **fatal** |
| RT-63 | "0.42 standard deviations" is the spread of one draw, not the uncertainty of the mean being scored | MEASURED | worth-noting |
| RT-64 | One training seed; the design only ever had power against a large effect | ARGUED | serious |
| RT-65 | The control is flat at the end and the budget was not short-changed — checked, clean | MEASURED | clean |
| RT-66 | The one trajectory reading in the review set also runs the intervention's way | MEASURED | worth-noting |

### RT-62 — the comparison the pre-statement designed is not in the findings

**MEASURED. Fatal — one sentence in the interpretation is false as
written, and the number that makes it false is absent.**

The pre-statement is explicit about why this run used seed 0:

> chosen so the comparison against the existing pilot is matched on
> initialization and data order and **the loss is the only thing that
> differs**

Its counterpart therefore exists and is in the review set. The A3 pilot at
seed 0, with none of this supervision, reads the control battery at
**0.2877** (spread 0.0302). This run, same seed, same initialization, same
data order, reads **0.3125** (spread 0.0240).

**The matched move is +0.0248.** Treating the two six-draw means as
independent, the standard error of that difference — the amount it would
wobble if you re-measured — is 0.0157, so the move is about **1.6 standard
errors**: it does not reach conventional significance, and it is not
nothing either.

The findings file does not report this comparison at all. It sets 0.3125
beside all three checkpoints — 0.2877, 0.3057, 0.3195 — which are three
*different training seeds*, and so re-imports exactly the between-seed
variation the matched design existed to remove. Against the mean of those
three (0.3043) the move is +0.0082, about half a training-seed standard
deviation, and that is where the sentence "the intervention moved nothing
distinguishable from seed variation" comes from.

That sentence is defensible. **The next one is not:**

> quadrupling the control's per-row gradient weight bought nothing

It bought about **+0.025, give or take 0.016**, on the comparison the
pre-statement was written around. "Not distinguishable from nothing" and
"nothing" are different claims, and only the first is true. A four-times
dose that moves a saturated battery a quarter of the way to its next
boundary, on one seed, is a weak positive that failed to reach
significance — not a zero.

**Both comparisons are legitimate. Only one was designed in advance, and
it is the one that is missing.**

There is also a sharper version available for nothing. Both checkpoints
were read on six evaluation draws. If they are the same six draws — this
run's are numbered 771000 through 771185, and the three-seed write-up says
its six are the first six of the twelve from the noise measurement — then
the difference can be taken **within each draw**, on the same held-out
items, which removes the item-set variation from both sides and would
tighten the estimate considerably. I could not do it: the earlier pilot's
per-draw control scores are not in the review set, only its summary. It
costs nothing and should be done before the step 4 proposal cites this
run.

**What survives:** the DID NOT LEARN verdict. 0.3125 is below 0.3227 on
the mean, it is nowhere near 0.60, and RT-61 shows the battery has
saturated the name-blind procedure. **What must not survive:** the words
"bought nothing", and the presentation of an unmatched three-seed
comparison in place of the matched one the pre-statement promised.

### RT-63 — the wrong spread against the boundary

**MEASURED. Worth-noting, and it cuts in the findings' own disfavour.**

The distance table reports the control as "0.42 standard deviations" below
0.3227 and "11.98" below 0.60, using 0.0240 — the spread of a *single*
evaluation draw. But the cell is scored on the **mean of six**, and the
uncertainty of a mean of six is the spread divided by the square root of
six: 0.0098. On that footing the control sits **1.04 standard errors**
below 0.3227, not 0.42.

The table's heading, "in standard deviations", is literally accurate. It
is simply not the uncertainty of the quantity the cell is read on.

The consequence runs against the findings' own hedge. They warn that "a
rerun could formally land in PARTIAL". How likely depends on what a rerun
means:

- a fresh single evaluation draw lands above 0.3227 about **34%** of the
  time;
- a fresh six-draw estimate, which is what the cell is actually read on,
  does so about **15%** of the time.

So the finding is better supported than its own caveat says. The caveat
should stay — it is the right instinct — but with the right number
attached.

### RT-64 — one training seed, and only a large effect was ever detectable

**ARGUED. Serious.**

The six seeds are **evaluation** seeds. They redraw the held-out set from
one checkpoint. They say nothing whatever about what a second *training*
seed would have done, and the three flag-off checkpoints put training-seed
spread at about 0.016 — comparable to the evaluation spread, and larger
than the matched move in RT-62.

A single training seed at that spread cannot separate "supervision does
nothing" from "supervision buys +0.02 to +0.03", which is roughly what the
matched comparison shows. The pre-statement implicitly accepted this by
setting LEARNED at 0.60: only a large effect was ever going to be
detectable, and a large effect is genuinely excluded.

The problem is that the conclusion now being drawn — "supervision is not
the binding constraint" — is a claim about small and moderate effects too,
and the run has no power against those. The design answers "does
supervision carry this battery?" It does not answer "does supervision do
anything?", and the findings file's own framing slides between the two.

### RT-65 — the run did answer the question it was bought for

**MEASURED. Clean, and recorded as clean, because it closes two escapes.**

Both secondary cells pass, as the findings say: the primary battery still
learns (0.5727 against the 0.50 the cell asks) and still collapses under
its own lesion (to 0.1663, a corrected drop of 1.448, in the same band as
the three earlier checkpoints). So this is not a failed intervention.

Two further checks, which the findings do not make and which matter more
than they look:

- **The control is flat at the end.** The partial checkpoint at step
  51,500 reads 0.3158; the full checkpoint at 55,116 reads 0.3125. That is
  a move of **−0.0033 over the last 3,616 steps**. This is not a battery
  still climbing when the budget ran out, which is the most obvious way a
  null could be an artefact of stopping early.
- **The budget was not short-changed by the flag.** The ledger records
  0.6508 seconds per step against the earlier pilot's 0.6501 — within
  about 0.7% — and the run finished on the identical 55,116 steps and
  585,552,384 tokens, confirmed by the completion sentinel and matching
  the earlier pilot and seeds 1 and 2. The padding worry the pre-statement
  flagged was real and negligible.

Minor, and recorded because the packet asks about every quantity the
pre-statement names: the pre-statement and the launcher both state the
budget as 585,544,960 tokens; the run stopped at 585,552,384, the first
step-multiple at or above it. The findings file quotes the second. Both are
right; they are different quantities and nobody says so.

### RT-66 — the early trajectory also runs the intervention's way

**MEASURED. Worth-noting.**

The one trajectory reading inside the review set is in the ledger, at steps
500 and 1,000: this run reads 0.28 and 0.27 on the control battery against
the earlier pilot's 0.24 and 0.18 at the same steps on the same seed.

Nothing should be read from 1.8% of training at 100 episodes, and the
ledger says so at length and correctly. It is recorded here only because it
is the second place where the matched comparison favours the intervention
slightly, and the findings file quotes neither. Two weak indications in the
same direction are still weak — but a findings file that reports neither,
and then says the intervention "bought nothing", has selected against its
own result.

---

## 4. Over-reading

*What "supervision is not the binding constraint" will be read as
claiming, beyond what one seed at one weight setting measured.*

| id | finding | label | severity |
|---|---|---|---|
| RT-67 | The sentence will be read as ruling out supervision; the run tested one dose of one form of it | ARGUED | serious |
| RT-68 | Step 4 should narrow — but for a reason the findings do not give, and the stated reason undercuts the option it points to | ARGUED | serious |
| RT-69 | Any step 4 option that keeps this battery inherits the ceiling precondition John already set | MEASURED | worth-noting |

### RT-67 — what the sentence will be taken to mean

**ARGUED. Serious.**

What was measured: on one training seed, at four times the per-row weight
and two thirds of the query gradient, with the whole query side
simultaneously tripled against the action term, the control battery moved
+0.0248 against its matched counterpart and stayed on the shoulder of a
name-blind solver.

What "supervision is not the binding constraint" will be taken to mean, in
the current-state document, in the 4 October control-battery proposal and
in the paper: **supervision has been ruled out.** That is a claim about
every dose and every form of supervision, and three things sit outside what
the run touched:

1. **Other doses.** One point on a dose curve. The pre-statement said as
   much — a larger dose "would make a null more decisive" — and the larger
   dose was not run.
2. **Other forms.** The pre-statement's own rejected alternative, a second
   forward pass putting the control question on *every* episode rather
   than half of them, is a different and stronger intervention that was
   rejected on cost, not on merit. It remains untested.
3. **The confound.** RT-57: the dose did not arrive alone. Until an arm
   renormalises the query side, "the control's share was raised" and "the
   whole query side was tripled" are not separated — and the pre-statement
   already warns that the flag changes two things at once, while naming a
   *different* pair than the ones that actually moved.

The honest scope is narrower and still useful: **reweighting the rows the
control battery already had does not teach it to read the name.**

### RT-68 — narrow step 4, but say why properly

**ARGUED. Serious. This is the recommendation the packet asks for.**

**Yes, this supports narrowing step 4 to option D or closing A3. No, a
cheaper supervision variant is not live as a route to 0.60. But the
findings file gives the weaker of the two available reasons, and the one it
gives argues against the option it points to.**

**The practical case, which does not depend on anything contested above.**
The control is 95% of the way from chance to a name-blind solver (RT-61)
and flat over the last 3,600 steps (RT-65). Four times the per-row weight
bought about +0.025 (RT-62). The distance remaining to 0.60 is 0.29 —
**more than ten times what the intervention bought.** Extrapolating from a
single dose is not evidence and I am not offering it as evidence; but
nothing in this run suggests any reweighting of existing rows clears 0.60,
and the money would be better spent elsewhere.

**The stronger case, which is in the review set and which the findings miss
entirely.** Even a rerun landing in PARTIAL would change nothing for
Amendment A3. The operative bar for this battery to be *useful* is not
0.3227 but **0.4227** — the corrected floor rule of ceiling plus 0.10
(RT-53). Below that the control's drop stays undefined and the registered
differential clause stays uncomputable, exactly as it is on all three
existing checkpoints. **So the whole band from 0.3227 to 0.4227 is a band
in which the control "learns" by the pre-stated cell and Amendment A3 is no
better off than it is today.** The findings file's anxiety about a rerun
formally landing in PARTIAL is therefore misplaced twice over: it is less
likely than stated (RT-63), and it would not matter if it happened.

That argument narrows step 4 far more firmly than "supervision is not the
binding constraint" does, and it survives every objection in this review.

**The case against, which the step 4 proposal must handle.** Option D — a
scaffolded intermediate query that teaches plain name-keyed retrieval
before layering the rule on top — **is itself a supervision change.** It
adds a training signal the control battery does not currently receive. So
"supervision is not the binding constraint" and "therefore do option D" sit
badly together, and a proposal that cites this review for the first claim
will be citing it against its own recommendation. What the run actually
rules out is **reweighting rows the battery already had**. What option D
proposes is **giving it a different and easier question first**. Those are
different interventions, and the run says nothing against the second. Write
it that way, or the contradiction will be found by someone else.

### RT-69 — the ceiling precondition still binds

**MEASURED. Worth-noting.**

John ruled on 2026-09-17 that if an Amendment A4 opens, measuring the
control battery's ceiling properly is a precondition of it. That ruling is
in the registered text. Any step 4 option that keeps this battery — option
D certainly does — inherits it, and the true ceiling near 1.0 is still
unmeasured. The 4 October proposal should carry the precondition
explicitly rather than leave it to be rediscovered.

### The sentence for the current-state document

The packet asks for the sentence that should go in `STATUS.md`. Proposed,
and deliberately avoiding both "supervision" as a bare word and the cell
label as a summary:

> **Giving the control battery its own loss term — four times the per-row
> weight, two thirds of the query gradient instead of one third — left it
> at 0.3125, against 0.2877 on the matched checkpoint that received none of
> it: still on the shoulder of a solver that cannot read the name the
> question supplies, and nowhere near the 0.60 that would show it had
> learned to read it. Reweighting the rows it already had is not what this
> battery is missing.**

Three choices in that sentence, each deliberate. It quotes the **matched**
comparison, because that is the one the pre-statement designed and the one
the findings file omits (RT-62). It says **"reweighting the rows it already
had"** rather than "supervision", because that is what was tested and the
broader word would be over-read (RT-67). It does not say "bought nothing",
because that is false (RT-62).

If a second sentence is wanted, it should be the one the findings file
should have led with: **the battery has learned the whole name-blind
procedure and none of the name-keyed lookup, which is what the three
remaining explanations are all about.**

---

## Kill case

The strongest case for throwing this interpretation out is RT-57 joined to
RT-58: the intervention did not do one thing, it did three. It raised the
control battery's share of the query gradient, it tripled the size of the
entire query loss against an action term that was never meant to move —
changing what the gradient clip does to every shared parameter on every
step — and it replaced a rotating assignment of questions to batch
positions with a fixed one whose representativeness nobody checked and
which then ran unchanged for 55,116 steps. On top of that it is one
training seed, and the matched comparison the design was built around moved
**+0.0248 with a standard error of 0.0157** — in the direction the
intervention predicted, at about 1.6 standard errors — and was reported as
"nothing". If the fixed positional split fed the control a biased half of
the episode space, or if tripling the query side degraded the shared trunk,
then a control battery that *would* learn under a clean reweighting returns
exactly this number, and the run has measured its own confound rather than
the question it was bought for. Nothing in the committed record excludes
either, because the two one-line checks that would have — episode order,
and one scored token per row — are not in the self-test, and the log and
trajectory that would show the run's behaviour over time are excluded from
the repository. **I do not think that kills the finding.** The battery sits
95% of the way from chance to the name-blind solver and is flat over the
last 3,600 steps, so whatever the confounds did, they did not hide a
battery on its way up; and the distance to the 0.60 boundary is more than
ten times what four times the supervision bought. The verdict should stand
with its scope cut to what was actually run — **reweighting the rows the
control battery already had does not teach it to read the name** — and the
sentence "supervision is not the binding constraint" should not enter the
current-state document, the 4 October proposal or the paper in that form.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-fitted-read-packet.md =====

# Review packet — the fitted linear read at all eleven positions (Gate B, tier 1)

*Prepared 2026-09-20 (Pacific) under `docs/outside-review-protocol.md`.
Gate B: this run was decision 2 of the 2026-09-19 review of the
linear-read closure, and whether the line is retired on it is a
direction question, so its interpretation is reviewed before it enters
STATUS.md.*

## The interpretation under review

From the findings on branch `worktree-fitted-read-sweep` (commit
`9080d02`), headline: FOUND NOWHERE, nothing on any checkpoint. Across
nine testable positions, five layers and three checkpoints (135 tests) a
fitted linear classifier does not find the register index anywhere at the
family-adjusted bar of 3.38 sd; one test on one checkpoint reached
MARGINAL. The instrument check reproduced all fifteen recorded numbers
exactly; the positive control at position 6 holds on all three
checkpoints at +34 to +54 sd. The findings say explicitly that this is
not a finding of absence.

The question for this review: with both the difference-of-averages read
and the fitted read now empty at these positions, what may STATUS.md say
about the linear read, and what does the registration (probe plus causal
patching, RT-49, RT-50) still require before anything is called localized
or absent.

## What the reviewer gets, and nothing else

At commit `9080d02` on `worktree-fitted-read-sweep` (or main once merged),
in `experiments/06-mvm-0a-constructed-self-index/`:

- `reviews/2026-09-19-fitted-read-brief.md` — what the run was told to do.
- `fitted-position-sweep-method.md` — committed before output (`f84db43`).
- `fitted-position-sweep-findings.md` — the findings under review.
- `a3-gates/fitted_position_sweep_a3_*.json` — the records.
- `src/fitted_position_sweep_a3.py`.
- The prior review and its rulings, since this run answers them:
  `reviews/2026-09-19-linear-read-closure-claude-worktree.md`, its
  addendum, and the RT-33 to RT-51 block of `red_team_ledger.md`.
- `powered-position-sweep-findings.md` — the difference-of-averages
  result this pairs with.
- Registered text: `amendment-a3.md` §3.2 and `pre-registration.md`.

Do not open: STATUS.md, `docs/`, any chat transcript, any uncommitted
file. Say at the top what was opened.

## The brief (fixed text from the protocol)

Four parts, a table first in each, severities marked, a one-paragraph
kill case at the end.

1. **Feasibility.** Check the brief's six requirements against the method
   file: per-test seeding (RT-39), the bar stated as a number, a
   register-index positive control or the statement that there is none
   (RT-35), the pre-stated cells and degeneracy rule, the anchor
   reproduction, geometry at the other positions (RT-40). A requirement
   claimed met with no record is a fatal finding.
2. **Satisfied by the wrong thing.** Every way FOUND NOWHERE could be
   returned by a model that carries a linear register-index signal at
   these positions: regularisation, fold size, the two untestable
   positions, the classifier's capacity against 448 dimensions on 400
   episodes.
3. **No verdict.** Including the MARGINAL test and what the pre-stated
   cells say a marginal means.
4. **Over-reading.** Write the STATUS.md sentence. Say whether "no linear
   read finds own-agent identity at the nine testable positions" is now
   supportable, and state what the registration still requires (causal
   patching) before "not localized" or "absent" can be said.

Label every finding MEASURED or ARGUED. Continue the ledger numbering
from where the control-learnability review leaves off, or from RT-52 if
that review has not filed; say which. Plain language. Do not soften.

## Filing

Findings to `reviews/2026-09-20-fitted-read-claude-worktree.md`, verbatim,
never edited after filing. Rulings in `red_team_ledger.md`. Nothing enters
STATUS.md until John rules.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-fitted-read-claude-worktree.md =====

# Outside review — the fitted linear read at all eleven positions (Gate B, tier 1)

*Filed 2026-09-20 under the outside-review protocol, against the review
packet `2026-09-20-fitted-read-packet.md`. Verbatim on filing and not
edited afterwards. Nothing here is a ruling; rulings are John's and go in
the red-team ledger (`red_team_ledger.md`).*

## What was opened

Read in a fresh worktree off `main` at the merge commit `a846b0c`, which
merged the branch the packet names (`worktree-fitted-read-sweep`) and
contains the findings commit `9080d02`. Exactly the packet's list and
nothing else:

- The brief for the run (`reviews/2026-09-19-fitted-read-brief.md`).
- The method file (`fitted-position-sweep-method.md`).
- The findings under review (`fitted-position-sweep-findings.md`).
- The four machine records under `a3-gates/` whose names begin
  `fitted_position_sweep_a3_`: one per checkpoint and the summary.
- The code (`src/fitted_position_sweep_a3.py`), all 736 lines.
- The previous review
  (`reviews/2026-09-19-linear-read-closure-claude-worktree.md`), its
  addendum, and the block of the red-team ledger running from the
  sensitivity finding (`RT-33`) to the reviewer's own disclosed error
  (`RT-51`).
- The difference-of-averages result this pairs with
  (`powered-position-sweep-findings.md`).
- The registered text: section 3.2 of `amendment-a3.md`, and the clause
  of `pre-registration.md` the previous addendum quotes. I also read
  section 3.1 of `amendment-a3.md`, because 3.2 defines how a thing is
  located and 3.1 defines what the thing is, and one is unreadable
  without the other. If that counts as exceeding the list, it is
  disclosed here rather than left to be discovered.
- Git metadata only — commit order, messages and the files each commit
  touched — to check the "committed before output" claim.

**Not opened**, as instructed: the status file (`STATUS.md`), the `docs/`
folder including the outside-review protocol itself, any chat transcript,
any uncommitted file.

**Three gaps this list creates**, stated so they are not mistaken for
omissions on my part.

**First**, the run's code imports six helper modules — the episode
builder, the capture path, the fold helper, the position definitions and
two target definitions. None is on the list. So where a claim depends on
what an episode is, what a position is, or how a fold is cut, I have the
run's own code and the registered text and nothing else, and I say so at
each point.

**Second**, the section of the findings headed "RT-33 confirmed and now
measured directly" quotes six difference-of-averages accuracies at
position 6. Those numbers are not in `powered-position-sweep-findings.md`,
which reports margins only and no accuracies at all. They must come from
the powered sweep's machine records, which the packet does not list. I
have not checked them.

**Third**, I could not read the status file, so where I write a sentence
for it I am writing a replacement for a paragraph I have not seen.

No outside lookup was used. Every number below either comes from a
committed record in this repository or from a computation I ran myself
against those records, and each is labelled MEASURED or ARGUED.

## Ledger numbering

The packet says to continue from where the control-learnability review
leaves off, or from **RT-52** if that review has not filed. **It has not
filed.** The reviews folder holds its packet
(`2026-09-20-control-learnability-packet.md`) and no findings file
answering it. The last row in the ledger is the previous reviewer's
disclosed error (`RT-51`). So I number from **RT-52**.

## Verdict in one line

**The cell is right and the run is the best-built thing in this stack.**
I reproduced every published number from the machine records, the
instrument check is locked at both ends, and no ruling from the previous
review was ignored. The interpretation is also mostly right, and holds
itself to the registered limits without being asked twice. Two things are
wrong with it: the run is roughly **two and a half times less sensitive
than the findings claim**, and the sentence the packet asks about — that
no linear read finds own-agent identity at the nine testable positions —
**cannot be said**, because the target the registration actually names
was never read by this instrument at any of those nine positions.

---

# 1. Feasibility

*Did the method file meet the six requirements the brief set, and is each
one backed by a record?*

| # | finding | severity | label |
|---|---|---|---|
| RT-52 | all six requirements are met and every one has a record; the instrument check is locked at both ends so neither the code nor the record can be edited to fit the other | worth-noting (credit) | MEASURED |
| RT-53 | the findings' "below 1e-15" for the instrument check is not on the record, which resolves only to six decimal places, and two of the three checkpoints are exactly zero rather than nearly zero | worth-noting | MEASURED |
| RT-54 | both self-corrections in the findings are accurate, and I confirmed each against the record | worth-noting (credit) | MEASURED |
| RT-55 | the run used 200 shuffled-label draws where the previous review's first recommendation was 1,000; disclosed in advance with the arithmetic, but it is why the bar leans on a normal approximation | worth-noting | MEASURED |

### RT-52 — the six requirements, each with a record behind it

**Worth-noting, and it is credit. MEASURED.** The brief said a
requirement claimed met with no record is a fatal finding. I checked all
six against the machine records rather than against the method file's
description of itself. There are no fatal findings here.

**Seeding per test.** The method says the fold split and the shuffled
draws are seeded from a digest of checkpoint, target, position and layer
together, rather than by layer alone as the previous sweep did. The code
does this, and its own self-test asserts that all 55 tests on a
checkpoint get distinct seeds, that the seed is stable when recomputed,
and that it changes when the checkpoint changes. Verified by reading the
code, not by trusting the comment.

**The bar as a number.** Stated as 3.38, applied rounded up from an exact
3.3740. I recomputed it: spreading a 5 per cent family-wise error across
135 tests needs a one-sided margin of **3.3740** standard deviations.
Exact. The previous sweep's 3.56 for 270 tests recomputes to **3.5603**.
Also exact.

There is a small thing worth recording because it could have gone the
other way. The code rounds each margin to two decimal places *before*
comparing it to the bar, so the threshold that actually operates is
3.375, not 3.3740. That is still stricter than the arithmetic requires,
so the method file's promise — "rounded up, so the bar in force is never
looser than the bar the arithmetic asks for" — survives its own
implementation. I checked because it is exactly the kind of thing that is
usually wrong.

**A positive control for the register index, or the statement that there
is none.** The method states plainly that there is no guaranteed-present
control for this target, only a guaranteed-*derivable* one at position 6,
and spells out what that costs before the run: a null everywhere cannot
separate "the models do not carry it away from that position" from "this
read cannot find it away from that position". That is what the ruling on
the missing control (`RT-35`) asked for, and it is what the findings
repeat. The control is then used as a one-way gate — failure voids a
checkpoint, success certifies nothing elsewhere — which is the correct
shape.

**Pre-stated cells and the degeneracy rule.** Both fixed in the method
file and both implemented as written. FOUND requires three things
together: margin at or above the bar, zero of 200 draws matching or
beating the real accuracy, and accuracy above the majority-class rate.
The degeneracy rule suppresses a label if the null has no spread, a class
is missing from a training fold, or accuracy lands exactly on the
majority-class rate. The code's self-test plants a signal and confirms
FOUND, plants noise and confirms no label, raises the bar out of reach
and confirms the same planted signal is demoted to MARGINAL, and starves
a class to confirm the degeneracy rule fires and suppresses the label. I
read all of it.

**The anchor reproduction.** This is the strongest piece of engineering
in the stack and it deserves saying. The fifteen recorded numbers are
written into the code as a pre-stated claim, **and** the code refuses to
run at all unless those fifteen values match the committed record files
to nine decimal places. So the code cannot be edited to fit the record,
and the record cannot be edited to fit the code, and a mismatch stops the
run rather than being reported at the end. Then the run re-executes the
original 400-episode configuration and compares. Every one of the fifteen
reproduced.

**Geometry at every position.** Measured at all 165 tests, not just the
anchor, which is what the ruling on the one-position geometry (`RT-40`)
asked for. The numbers are in the records. What the findings *say* about
them is wrong in one place, which is a separate finding below (`RT-57`).

### RT-53 — a number in the findings that the record does not carry

**Worth-noting. MEASURED.** The findings report the instrument check as
reproducing "to floating-point round-off — the largest difference on any
cell was below 1e-15". The record does not support that figure. The code
rounds the largest difference to six decimal places before writing it, so
every record says `0.0`, and the finest statement the record can make is
"below five parts in ten million".

The record does carry one detail the findings lose. On the pilot the
field recording an exact match across every layer is **false** while the
largest difference still prints as `0.0` — which means the pilot's worst
difference is greater than zero and smaller than the rounding could show.
On seeds 1 and 2 that same field is **true**, so those two are bit-exact.
So the three checkpoints did not behave identically: two reproduced
exactly and one reproduced to within summation order. The findings' table
prints "below 1e-15" against all three, which flattens that.

Nothing turns on it. The pre-stated tolerance was one episode in 400 and
the run used none of it. But "below 1e-15" is stated as a measurement and
it is an inference, and this review is required to mark that distinction.

### RT-54 — the two corrections are real corrections, and both check out

**Worth-noting, and it is credit. MEASURED.** The findings carry two
corrections to the committed method file rather than editing it, which is
what the ruling on not editing committed method files (`RT-43`) requires.
I verified both against the record.

The first says the method file was wrong to claim the classifier hits its
2,000-pass cap on every fold at 400 episodes. Correct: on the pilot's
twenty anchor folds the optimiser used between 158 and 933 passes and
capped on none of them; on seed 1 it capped on 9 of 20 and on seed 2 on
17 of 20. Those are exactly the numbers the correction gives.

The second says the six-and-a-half-hour estimate was low and the run took
10.8 hours. The three records give 2.93, 3.36 and 4.47 hours, which sum
to 10.76. Correct, and the explanation offered — that the slowest
checkpoint is the one whose fits converge least — holds: the cap rates
run 13.5, 22.3 and 73.6 per cent in the same order as the times.

A findings file that corrects its own method file twice, in public,
against numbers anyone can check, is behaving the way this protocol is
supposed to make things behave.

### RT-55 — a fifth of the draws the previous review asked for

**Worth-noting. MEASURED.** The previous review's first recommendation
was to run the fitted classifier "4,000 episodes, 1,000 draws, three
checkpoints". The run used **200** draws. The brief did not restate the
1,000, so this is not a departure from the brief, and the method file
declares the shortfall in advance, gives the cost arithmetic, and states
the consequence plainly: zero out of 200 establishes only about 2.58
standard deviations' worth of evidence, which is below the 3.38 the
family bar needs, so the margin has to supply the rest under a normal
approximation to a null measured with only 200 draws.

That disclosure is correct and I recomputed it: zero of 200 gives a
probability below one in 201, which is 2.578 standard deviations. I
record this in feasibility rather than burying it because it is the
reason the whole result rests on an approximation rather than on
counting, and because it is the cheapest thing to fix if any single cell
ever needs to be believed.

---

# 2. Satisfied by the wrong thing

*Every way FOUND NOWHERE could be returned by a model that does carry a
linear register-index signal at these positions.*

| # | finding | severity | label |
|---|---|---|---|
| RT-56 | the run's real reach is a signal in about one episode in eleven, not one in twenty-seven; the measure assumes a perfect read is possible and this read's own measured ceiling is 0.55 | serious | MEASURED |
| RT-57 | the claim that the state space is least concentrated at the control position is false on seed 1 and a photo-finish on seed 2, so the control sits in a different regime from the tested positions on one checkpoint and the same one on another | serious | MEASURED |
| RT-58 | leaving the 448 directions unscaled under a squared penalty charges a quiet direction the square of how quiet it is, so the read is worst-placed against precisely the hypothesis under test | serious | ARGUED from measured geometry |
| RT-59 | the bar treats 135 tests as independent when all three checkpoints read the same 4,000 episodes and five layers read one residual stream; the correction stays valid but buys less power than its arithmetic implies | serious | MEASURED |
| RT-60 | fold size and classifier capacity are cleared: at 4,000 episodes the fit is in a comfortable regime and I find no sign of capacity failure | worth-noting | MEASURED |
| RT-61 | the majority-class requirement, announced as a deliberate tightening, never binds on any test in the run | worth-noting | MEASURED |

### RT-56 — the run would have found a signal in one episode in eleven, not one in twenty-seven

**Serious. MEASURED for the arithmetic, ARGUED for the calibration.**
This is the most consequential thing in the review, because it is the
number the findings lead with when they say how much the null is worth.

The findings say: "the run would have found a register index legible in
about one episode in twenty-seven, and found none." The measure behind
that (`RT-37`) works like this: take the accuracy a test would need to
clear the bar, and ask what share of episodes would have to be **perfectly
legible**, with the rest at chance, to produce it. At a needed accuracy of
0.2774 against a chance rate of 0.25, that share is 3.65 per cent, which
is one episode in twenty-seven. I recomputed every figure in that table
and all of them are exactly right: 3.05 to 4.08 per cent on the pilot,
3.03 to 4.05 on seed 1, 3.22 to 4.03 on seed 2, and the 3.84, 3.86 and
3.91 at the previous sweep's bar. The arithmetic is not in question.

**The assumption inside it is.** "Perfectly legible" means the classifier
scores 1.0 on those episodes. This read does not score 1.0 on anything —
including at the one position in the whole run where the answer is
available and the control clears at more than thirty standard deviations.
There, it scores **0.539 to 0.567**. That is the only ceiling this run
ever measures, and it is a little over half.

Redo the arithmetic with the measured ceiling in place of the assumed
one, so that a legible share produces accuracy `0.25 + share × (ceiling −
0.25)`:

| checkpoint | ceiling measured at position 6 | share as the findings compute it | share against the measured ceiling |
|---|---|---|---|
| pilot | 0.5670 | 3.65% — one in 27 | **8.6%–8.8% — one in 11** |
| seed 1 | 0.5575 | 3.65% — one in 27 | **8.9%–9.0% — one in 11** |
| seed 2 | 0.5485 | 3.71% — one in 27 | **9.3%–9.4% — one in 11** |

**So the run overstates its own reach by about two and a half times.** It
can see a register index legible in roughly one episode in eleven. It
cannot see one legible in one episode in twenty.

Three things to be fair about. The calibration is ARGUED: position 6 is a
derivable target, not a guaranteed-present one, so 0.55 may be the
model's limit rather than the read's — and if the model represents the
index perfectly there, then 0.55 is genuinely the read's ceiling and the
correction is right. Either way it is the best-supported ceiling
available, and 1.0 is not supported by anything. Second, the correction
does not change the cell: one episode in eleven is still a real amount of
signal to have missed. Third, the findings did not invent this measure —
it came out of the previous review, where the same implicit ceiling of
1.0 sat unexamined. The correction belongs to both runs.

### RT-57 — the control does not sit where the findings say it sits

**Serious. MEASURED.** The findings write, under geometry:

> It is consistently lowest at position 6, the one place the answer is
> present — 0.8579 on the pilot at layer 5, against 0.9899 at the highest
> position.

The share of variation carried by the top ten of 448 directions, at
position 6 against the nine testable positions, from the records:

| checkpoint | position 6 | the nine testable positions | is position 6 lowest? |
|---|---|---|---|
| pilot | 0.8524 – 0.8651 | 0.9486 – 0.9907 | **yes, clearly** |
| seed 1 | 0.9791 – 0.9820 | 0.9430 – 0.9953 | **no** — four testable positions are lower |
| seed 2 | 0.8774 – 0.8815 | 0.8781 – 0.9806 | by 0.0007, a photo-finish |

On seed 1 the control position is the fourth *most* concentrated of the
eleven, above the other agent's revision value (0.9430), the model's own
revision value (0.9559), the query answer value (0.9565) and its second
assignment (0.9647). The claim is false there. The specific comparison
the findings quote — 0.8579 against 0.9899 — is a pilot-only, layer-5
comparison and it is accurate as far as it goes; the word doing the
damage is "consistently".

The same paragraph adds that "the stack's earlier figure of about 99 per
cent in ten directions holds at the other positions". Across the 135
testable tests the range is 0.878 to 0.9953, with per-checkpoint medians
of 0.974, 0.984 and **0.942**. Ninety-four per cent is not about
ninety-nine, and on seed 2 seven of the nine testable positions sit below
0.95.

**Why this is serious rather than pedantic.** The geometry is the whole
mechanism behind the quiet-direction problem (`RT-34`), and it is also
the only evidence available about whether the positive control tests the
read in the same regime as the tested positions. On the pilot it plainly
does not — the control lives in a far less concentrated space than
anywhere the question is actually asked, which makes a pass there weak
evidence about the nine. On seed 1 it plainly does, which makes the pass
there better evidence. That is a real and useful distinction between
checkpoints, it is sitting in the records, and the findings replace it
with a single claim that is true of one checkpoint in three.

### RT-58 — an unscaled fit charges a quiet direction the square of how quiet it is

**Serious. ARGUED, from the geometry measured in this run.** The method
file names this and declines to fix it, which is honest. It is still the
single most likely way a real signal would have been returned as FOUND
NOWHERE, so it belongs here in full.

The classifier is a logistic regression with the library's default
squared penalty at strength 1.0, on features left at their original
scale. The penalty is charged on the weight, not on the weight's effect.
A direction carrying a small share of the variation has a
correspondingly small typical value, so producing a given contribution to
the decision needs a proportionally larger weight — and a squared penalty
charges the **square** of that factor. With the top ten of 448 directions
carrying between 88 and 99.5 per cent of the variation depending on
position and checkpoint, the remaining 438 directions share what is left,
and a signal resident in one of them is pushed toward zero far harder
than the same signal in a loud one.

So the instrument is, by construction, worst-placed against exactly the
hypothesis the run exists to test: a self-index that is real, linear and
quiet. The method's defence is that the fitted read is nonetheless far
more sensitive than the difference-of-averages read it replaces, and that
is true and measured. But "more sensitive than the thing the ledger
called fatally insensitive" is a floor, not a ceiling, and the findings
say so.

The fix is cheap and it is a different instrument: standardise the
features, or fit in a whitened basis, and the quiet directions compete on
equal terms. That would break the comparison with the record and would
need its own anchor, which is precisely the trade the method chose to
avoid — reasonably, for a first run whose credibility rested on
reproducing fifteen recorded numbers. It should not be avoided twice. A
standardised refit at the nine positions costs the same eleven
processor-hours and would separate "not linearly present" from "not
reachable by this penalty".

### RT-59 — 135 tests, far fewer independent ones

**Serious. MEASURED for the dependence, ARGUED for what it costs.** The
family bar is computed as if there were 135 independent discovery tests.
They are strongly dependent, in two ways that are both visible in the
method and the code.

**The three checkpoints read the same episodes.** One content seed
(20260917), one call to the episode builder, 2,000 pairs giving 4,000
episodes, and all 4,000 kept on all three checkpoints — the records show
the same count everywhere. So the three checkpoints are three models
reading one sample, not three samples. Anything that is a property of
this particular draw of 4,000 episodes at a given position reproduces on
all three.

**The five layers read one residual stream.** Five reads of the same
running state at the same token are not five independent tests of
anything.

Spreading the error rate across 135 tests remains **valid** — the
correction controls the family-wise error whatever the dependence is.
What it does not do is control it *efficiently* under positive
dependence. The bar is set for a family that is larger than the effective
one, so it buys less power than the arithmetic implies:

| family assumed | bar it sets |
|---|---|
| 135 tests — as applied | 3.3740 |
| 45 tests — one set of positions and layers, shared episodes | 3.0588 |
| 9 tests — positions only, layers pooled | 2.5392 |

The run's one MARGINAL, at +3.34, clears both of the lower bars. I am
**not** arguing the bar should have been lower — it was pre-stated,
pre-committed, and choosing the conservative option before seeing the
data is the right instinct. I am arguing that for a run whose entire
question is "is anything there at all", over-correcting is the direction
that manufactures a null, and the findings present 3.38 as a neutral
technical choice rather than as the strict end of a defensible range.

### RT-60 — fold size and capacity are not the problem

**Worth-noting. MEASURED.** The packet names four candidate mechanisms.
Two of them clear.

At the sweep's own size the fit is comfortable: 4,000 episodes, four
folds, so 3,000 training rows against 448 directions and four answers,
with the smallest answer class holding 964 examples on every checkpoint.
That is not an overparameterized regime and I find no sign of capacity
failure in the records — the nulls are tight and well-behaved (spread
0.0067 to 0.0091 on every test), the real accuracies sit on top of their
nulls rather than scattering, and no test tripped the missing-class rule.

The 400-episode configuration *is* overparameterized — 300 training rows
against 448 directions — but it is used only to reproduce the recorded
anchor, and no sweep cell rests on it. The packet's framing asks about
"448 dimensions on 400 episodes"; that describes the anchor, not the
sweep, and the anchor is a reproduction check rather than a measurement.

So of the four mechanisms, fold size and capacity are cleared.
Regularisation is not (`RT-58`), and the two positions that were never
tested are the two controls, which is correct design: position 1 is where
the answer is provably not yet knowable and position 6 is where it is
explicit. That leaves the episode's other sixty tokens unexamined, which
is the previous review's point about eleven positions of seventy-one
(`RT-46`) and is unchanged by this run.

### RT-61 — the new requirement that never fires

**Worth-noting. MEASURED.** The method introduces a third condition for
FOUND — accuracy must beat the majority-class rate — and calls it out:
"Requiring the majority-class rate is new and it is deliberate." It never
does any work.

The majority-class rate is 0.2582 on all three checkpoints. The accuracy
needed to clear the family bar is between 0.2774 and 0.2778 on every one
of the 135 testable tests. So any test that clears the bar has already
beaten the majority-class rate by a comfortable margin, and the new
condition cannot suppress anything. The findings report it as one of
three conditions that had to be met, which reads as a tightening and is
not one.

This is worth-noting rather than serious because the requirement is
harmless and would bind under a looser bar. But a pre-stated safeguard
that cannot fire should be reported as inert, the same way the findings
correctly report that the degeneracy rule did not fire.

---

# 3. No verdict

*What the run measured, what it did not, and what the pre-stated cells
say a marginal means.*

| # | finding | severity | label |
|---|---|---|---|
| RT-62 | the run's one consistent pattern — the other agent's revision value, positive in 15 of 15 tests — is invisible to a purely per-test analysis and is under-reported | serious | MEASURED |
| RT-63 | the first reason given for setting that pattern aside misdescribes what was measured: the target at every position is the model's **own** index | serious | MEASURED |
| RT-64 | there is a real confound at that position and it is not the one named; the instrument that separates it is registered and has never been run | serious | ARGUED |
| RT-65 | the MARGINAL test's real fit hit the pass cap on all four folds, which the findings do not say | worth-noting | MEASURED |
| RT-66 | seed 2's extra scatter is confined to that one position; elsewhere it is as tight as the other checkpoints, which cuts against discounting the cell on "seed 2 is straining" | worth-noting | MEASURED |
| RT-67 | the registered anchor position runs below its null at all five layers on seed 2, reaching −3.01, and the findings mention it only inside a range | worth-noting | MEASURED |
| RT-68 | the only testable test with zero of 200 draws beating it is at an own-agent position and is never discussed; it is also exactly what chance predicts | worth-noting | MEASURED |
| RT-69 | the pre-stated cells were applied correctly throughout, checked in the code and against all 165 tests | no finding | MEASURED |
| RT-70 | I tested the obvious bias from splitting paired episodes across folds and it is not present | no finding | MEASURED |

### RT-62 — one position is positive in fifteen tests out of fifteen, and nothing in the analysis can see it

**Serious. MEASURED.** The findings do name the other agent's revision
value as the highest testable position on all three checkpoints, and give
its three best-layer margins: +2.33, +2.39, +3.34. They do not report the
number that makes it interesting. Averaging each position's margin across
its five layers, and counting how many of its fifteen tests came out
positive:

| position | pilot | seed 1 | seed 2 | mean of 15 | positive |
|---|---|---|---|---|---|
| `other_revision_value` | +1.49 | +1.37 | +2.33 | **+1.73** | **15 / 15** |
| `query_answer_value` | −0.27 | +0.42 | +0.27 | +0.14 | 9 / 15 |
| `own_revision_value` | −0.09 | +1.23 | −0.75 | +0.13 | 8 / 15 |
| `own_revision_by` | −0.16 | +0.60 | −0.14 | +0.10 | 8 / 15 |
| `query_answer_decision` | −0.15 | +0.47 | −0.68 | −0.12 | 7 / 15 |
| `other_revision_decision` | +0.09 | −0.41 | −0.18 | −0.17 | 7 / 15 |
| `own_assign_2_value` | −1.01 | +0.19 | −0.54 | −0.45 | 5 / 15 |
| `before_own_revision_turn` | −0.53 | −0.37 | −0.84 | −0.58 | 1 / 15 |
| `own_revision_decision` | −0.17 | −0.26 | −1.46 | −0.63 | 4 / 15 |

Every one of its fifteen tests is positive: +1.91, +0.57, +2.33, +1.32,
+1.30 on the pilot; +1.25, +2.39, +1.24, +0.85, +1.11 on seed 1; +1.34,
+3.34, +1.75, +2.54, +2.70 on seed 2. Its mean margin is more than twelve
times the next position's. Nothing else in the run is remotely like this.

**The pre-stated analysis cannot see it**, and that is the finding. Every
cell in the method turns on a single test clearing a single bar. There is
no statistic anywhere in the method, the code or the findings that asks
whether a position is consistently elevated across layers and
checkpoints — and consistency across layers and checkpoints is the shape
a real, weak, distributed signal would take, as against the shape a
single lucky test would take. The method's own honesty note anticipates
the opposite case (a single FOUND cell being over-read) and says nothing
about this one.

**Two things that cut the other way, and I want them on the record with
equal weight.** First, the three checkpoints read the same 4,000 episodes
(`RT-59`), so a property of this episode draw at this position would
reproduce on all three and would look exactly like this. The three
checkpoints are not three independent confirmations. Second, the five
layers within a checkpoint are heavily correlated, so "fifteen of
fifteen" is nearer three observations than fifteen. Treating each
checkpoint as one observation, "some position among nine ranks top on all
three" happens by chance about one time in eighty — suggestive, not
decisive, and that calculation still assumes an independence across
checkpoints that the shared episodes deny.

So this is not a finding. It is the one thing in the run that looks like
something, the analysis was not built to notice it, and the findings
report a third of it.

### RT-63 — the target is the model's own index at every position, including that one

**Serious. MEASURED.** The findings give three cautions against reading
anything into the MARGINAL. The first is:

> It is the **other** agent's revision value, not the model's own. If
> something is readable there it is not obviously own-agent identity.

**The target read at that position is the model's own register index** —
the rank of the model's own marker word among the four in the episode.
That is the target at all eleven positions; the run has one target and
the method says so repeatedly. Only the *position* belongs to the other
agent's turn.

So a reading there is own-agent identity recovered at a token that is not
the model's own act. That is not a reason to discount it. It is, almost
word for word, what the registration defines the thing being looked for
to be. Amendment A3 section 3.1 defines the lesion target as a subspace
"that carries *'which marker is mine'* at positions *away from* act
positions (revision turns and query positions)". A position inside the
other agent's revision turn is about as far from the model's own act
position as this episode goes.

The caution inverts the significance of the run's own strongest
observation. Whatever else is true of that cell, "it is the other agent's
turn, so it would not be own-agent identity" is not a reason to set it
aside — it is a reason it would matter.

### RT-64 — the confound that is actually there, and the control that would settle it

**Serious. ARGUED.** Having said the findings' reason is wrong, I owe a
better one, and there is one.

The register index is the rank of the model's own marker among the four
markers present in the episode. At the other agent's revision value, the
other agent's marker has just been named in the running text. A
representation of *that* marker partially determines the model's own rank
by exclusion: it removes one of four possibilities, which lifts the best
attainable accuracy from 0.25 to about 0.333 with no own-agent
representation involved at all. The MARGINAL sits at 0.277. The confound
is comfortably large enough to produce it.

That would also explain why the effect is strongest at the other agent's
turn rather than the model's own, and why the other agent's revision
*decision* — one token earlier, before the value — shows nothing (mean
−0.17 across fifteen tests). I have not tested it: doing so needs the
position and target definitions, which are not in the packet.

**The instrument that separates these two readings is registered and has
never been run.** Amendment A3 section 3.1 lists, as matched control
L2(a):

> The *other-index* subspace: the same localization run for a named
> non-self agent ("which marker is agent B's"), matched in rank and probe
> accuracy.

Run the identical fitted read at the identical positions against the
*other* agent's index. If the other agent's index reads strongly at the
other agent's revision value and the model's own index reads weakly, the
MARGINAL is the exclusion confound and the position is closed. If the own
index survives once the other index is accounted for, it is the first
thing in this sequence that looks like a self-index away from an act
position. It is a four-answer target on captured states, so it costs the
same eleven processor-hours as the run just completed, and the code needs
a new target function and nothing else.

This is the cheapest decisive measurement now available in this line, and
it is already registered as a required control rather than being a new
idea.

### RT-65 — the MARGINAL was fitted by an optimiser that stopped early on every fold

**Worth-noting. MEASURED.** The findings caution that seed 2 strains the
instrument, giving the checkpoint-wide cap rate of 73.6 per cent. The
sharper fact is in the record and is not reported: for the MARGINAL test
itself — seed 2, the other agent's revision value, layer 4 — the real fit
used the full 2,000 passes on **all four folds**, and 785 of that test's
804 fits hit the cap.

So the single number the findings single out for discussion comes from a
fit that stopped early everywhere, not merely from a checkpoint where
that often happens. That is their own caution, correctly aimed, and it is
the version that should have been written.

It also cuts both ways, which is why it is worth-noting rather than
serious: an early-stopped fit is an under-fitted one, and under-fitting
more often hides a signal than invents one. Raising the cap is the
obvious check and the findings already list it as an open item, correctly
noting it would be a different instrument needing its own anchor.

### RT-66 — seed 2 is not generally unstable; it is unstable at one position

**Worth-noting. MEASURED.** The findings' framing is that seed 2 is the
straining checkpoint and its numbers deserve the most caution. The spread
of the 45 testable margins supports that at first glance — 1.177 on seed
2 against 0.812 on the pilot and 0.852 on seed 1.

Remove the other agent's revision value and seed 2's spread falls to
**0.760**, which is tighter than either of the other two checkpoints. The
excess scatter is not a property of seed 2. It is that one position.

That matters for how the MARGINAL is read. "Seed 2's numbers are noisy,
so discount this one" is not supported: seed 2's numbers are not noisy
anywhere except at the position in question, and a position that is
elevated *and* over-dispersed relative to its own checkpoint's behaviour
is a slightly stronger candidate than the findings allow, not a weaker
one. This is the second of the findings' three cautions, and like the
first it points the other way once the record is checked.

Their third caution — that one position rising on three checkpoints while
never reaching the bar is unremarkable in a family of 135 — stands, with
the qualification in `RT-62` that the family is not 135 independent
tests.

### RT-67 — the registered position reads below chance at every layer on seed 2

**Worth-noting. MEASURED.** The model's own revision decision is the
position the registration names, and the previous review's tables track
it as "the registered anchor". On seed 2 its five margins are **−0.26,
−1.05, −3.01, −0.83 and −2.16** — every layer below its own
shuffled-label null, two of them beyond two standard deviations, and one
of them the most extreme value anywhere in the run.

The findings mention the −3.01 once, inside the phrase "the full range of
margins is … −3.01 to +3.34 on seed 2", and never say where it is or that
it sits in a run of five negatives at the registered position.

A real accuracy three standard deviations *below* a shuffled-label null
is not a null result; it is an anomaly. It may be nothing — with 135
tests the lowest of 135 standard normal draws would be expected near
−2.8, so −3.01 alone is unremarkable. What is not explained by that is
all five layers of one position pointing the same way. The honest
sentence is that it is unexplained, and the findings should have written
one.

### RT-68 — the one test no shuffled draw matched is at an own-agent position

**Worth-noting. MEASURED.** Exactly one testable test in the whole run
had **zero of 200** shuffled draws meet or beat its real accuracy: seed
1, the model's own revision value, layer 3, accuracy 0.2678, margin
+2.07. Every other zero-draw result in the run is at the positive
control.

The findings print it in the table as "0.2678 +2.07 (0)" and never
mention it. Under the pre-stated rule it is correctly not MARGINAL — it
does not reach 3.0 standard deviations — and I am not arguing the rule
was misapplied.

Two sentences were owed. The first is that it exists and is at an
own-agent position, which is the position class the registration cares
about. The second is that it is exactly what chance predicts: with 201
values in play, about 0.67 of 135 tests should come out on top of their
own null, so seeing one is unremarkable and seeing none would have been
mildly surprising. Saying both would have cost a line and would have
strengthened the findings, not weakened them.

It is also the one place in the run where counting the draws and
computing the margin disagree about which side of "interesting" a test
falls on, which is the disagreement `RT-55` predicts when a bar of 3.38
is resolved by 200 draws.

### RT-69 — the cells were applied correctly

**No finding. Recorded for completeness. MEASURED.** I checked the label
logic in the code against the method file and then against all 165 tests
in the records.

FOUND requires margin at or above 3.38, zero of 200 draws matching or
beating the real accuracy, accuracy above the majority-class rate, and no
degeneracy. MARGINAL is three standard deviations without the family bar,
is reported, and triggers no cell. The MARGINAL in this run clears 3.0 at
+3.34, fails 3.38, and correctly triggers nothing. The two cells are
exhaustive, the sub-pattern is reported as the earlier ruling on
exhaustive cells (`RT-41`) requires, and the code's self-test exercises
all three sub-patterns including the two that did not occur.

Two details I checked because they could have been wrong and were not.
The rounding of the margin before comparison leaves the operative bar at
3.375, still above the exact 3.3740 (`RT-52`). And a checkpoint's control
is treated as holding if **any** single layer clears at position 6 — a
weak test as written — but all five layers clear on all three
checkpoints, at +34 to +54 standard deviations, so nothing turns on it.

The degeneracy rule fired nowhere, on any of the 165 tests. I confirmed
this from the records rather than from the summary: no null with zero
spread, no missing class, no accuracy landing exactly on the
majority-class rate.

### RT-70 — a bias I expected to find and did not

**No finding. Recorded because it should not be raised again without
evidence. MEASURED.** Amendment A3 section 3.2 specifies that the probe
contrast is "built from paired episodes that share a content seed and
rotate the owner … so content is held fixed and only ownership varies",
and the run uses those pairs. The folds are cut at random over the
flattened list and are not pair-aware, so a held-out episode's partner —
same content, different owner, therefore usually a different register
index — normally sits in the training set. A classifier that leant on
content would then be actively misled on the real labels while suffering
no such handicap on the shuffled ones, which would push real accuracies
**below** their nulls and could mask a weak signal.

It is not happening at any scale worth worrying about. Across the 135
testable tests the margins have a mean of +0.016, a spread of 0.993, and
70 of 135 fall below zero — which is what 135 independent standard normal
draws would look like, to three figures. Whatever the unpaired folds are
doing, they are not producing a global negative bias.

I record it because it is the first thing a sceptical reader will think
of, because the shape of the null across 135 tests being this well-behaved
is a genuine point in the run's favour that the findings do not claim,
and because the local exception to it is the five negative layers at the
registered position on seed 2 (`RT-67`).

---

# 4. Over-reading

*The sentence for the status file, whether the broad claim is now
supportable, and what the registration still requires.*

| # | finding | severity | label |
|---|---|---|---|
| RT-71 | "no linear read finds own-agent identity at the nine testable positions" is not supportable: the registered target was never read by this instrument at any of those nine positions | fatal to that sentence | MEASURED |
| RT-72 | "both reads are now empty" is one sample read twice, and on this target the earlier read's own control failed on seed 1 under the rule this run adopted | serious | MEASURED |
| RT-73 | the "essentially identical power" paragraph compares two reads through a measure that assumes a perfect score neither can reach; the conclusion drawn from it is right and the reasoning given for it is not | serious | MEASURED |
| RT-74 | what the registration still requires before "not localized" or "absent": causal patching, which has still never run | serious (carried, not new) | MEASURED |
| RT-75 | every ruling the run was required to honour, it honoured | worth-noting (credit) | MEASURED |

### RT-71 — the registered target has still never been read at the nine positions by this instrument

**Fatal to the sentence the packet asks about. MEASURED.** The packet
asks whether "no linear read finds own-agent identity at the nine
testable positions" is now supportable. **It is not**, and the reason is
not a matter of degree.

The previous review's addendum established, from the registered text,
what this programme is supposed to be looking for. Amendment A3 section
3.2 specifies linear probes that "decode **own-marker identity** from the
residual stream at revision and query positions". Section 3.1 defines the
target as a subspace carrying "which marker is mine". The addendum's
finding on this (`RT-48`) states it plainly and John accepted it: the
registered target is the model's own marker word, and the powered runs
were the first in the whole line to use it.

**This run did not read it.** The method declares before the run, with
the arithmetic, that the marker-word target does not fit: about 70
processor-hours against about 11, because the 25-answer fit hits the pass
cap on most folds. So the marker-word target was not run, and this is
stated openly in the method, in the code, in the machine records and
three times in the findings. Nobody hid anything.

But the consequence has not been drawn. Assemble what has actually been
measured at the nine testable positions:

| target | difference-of-averages read | fitted read |
|---|---|---|
| the model's own marker word — **the registered target** | run, found nothing | **never run** |
| the register index — a four-answer recoding | run, found nothing | run, found nothing |

The registered target has only ever been read at those nine positions
with the difference-of-averages read. That is the read the ledger's fatal
finding (`RT-33`) identified as about half as sensitive as a fitted one —
and this very run measures the gap and finds it **wider** than half: at
position 6 on the same target, the fitted read recovers 5.5 times as much
lift above chance on the pilot, 18.7 times on seed 1 and 7.5 times on
seed 2.

So the sentence "no linear read finds own-agent identity at the nine
testable positions" asserts something about the registered target on the
strength of a read that this run has just finished demonstrating is the
weak one. That is the same error the previous review called fatal, moved
from one target to another.

What **is** supportable, and it is a real result: at these nine
positions, five layers and three checkpoints, a fitted linear classifier
does not find the model's **register index**, and a difference of
averages finds neither the register index nor the marker word. The
ledger's decision 2 — "the line is not retired until a fitted linear
classifier has been run on the four-answer register-index target at all
eleven positions" — **is satisfied exactly as worded.** That was a
necessary condition for retiring the line, not a sufficient one, and the
findings are careful never to claim otherwise.

The remaining measurement is the marker-word target under the fitted
read. Seventy processor-hours is a weekend on one machine, or an
afternoon on a rented one, and it is the last thing standing between this
line and an honest close.

### RT-72 — two reads of one sample, and a control that failed on this target

**Serious. MEASURED.** The packet's framing question opens "with both the
difference-of-averages read and the fitted read now empty at these
positions". Two qualifications, both from the committed record.

**They are not two experiments.** Both sweeps use the same 4,000 episodes
at the same content seed (20260917), the same three checkpoints, the same
five layers and the same eleven positions. The method says so — "the same
episodes the powered sweep used" — and the code takes one episode seed
for all three runs. Two instruments applied to one sample agree more
often than two samples do, and neither read gets a second look at whether
this particular draw of 4,000 episodes is representative.

**On this target, the earlier read's own control failed on seed 1.** The
difference-of-averages sweep reports the register index at position 6
clearing at +7.40 on the pilot and +5.54 on seed 2, and reaching **+2.72**
on seed 1 — short of its own family bar of 3.56 and short of 3.0. The
powered findings keep seed 1 anyway, on the ground that "the control that
governs both arms is the marker word, and it holds without
qualification".

Under the rule this run adopted — "if the register index fails at
position 6 on a checkpoint, that checkpoint is VOID and its other
positions are reported without interpretation" — seed 1's register-index
result in the earlier sweep would have been void. The two runs apply
different standards to the same arm on the same checkpoint, and the
stricter one is the later one. That is the right direction of travel, and
it means the earlier null on this target is weaker than the pairing
suggests on one checkpoint of three.

Neither point damages the fitted run. Both bear on how much "both reads
are empty" is worth, which is what the status file will be asserting.

### RT-73 — the right conclusion from the wrong comparison

**Serious. MEASURED.** The findings record, under the heading "An honest
surprise worth recording", that the two reads have essentially identical
power: 3.84 to 3.91 per cent for the fitted read at the earlier sweep's
bar against 3.9 per cent for the difference-of-averages read. I
recomputed all three and they are exactly right.

The surprise is an artefact of the measure. As set out in `RT-56`, the
detectable-share measure converts a needed accuracy into a share of
perfectly legible episodes by assuming a perfectly legible episode scores
1.0. Neither read can score 1.0. At position 6, where the answer is
available, the fitted read reaches about 0.55 and the
difference-of-averages read about 0.30 — the latter from the findings'
own table, whose source I could not check. Two reads whose nulls are the
same width will always show the same detectable share under that measure,
regardless of how much of a real signal either can express, because the
measure never asks.

Correct for each read's own measured ceiling and the difference reappears
in the right direction and the right size: roughly one episode in eleven
for the fitted read against roughly one in five for the difference of
averages. **The fitted read is about twice as powerful**, which is what
the ledger's sensitivity finding said and what the null at nine positions
needs to be worth anything.

So the findings' conclusion — "the read that found nothing at nine
positions is demonstrably the sensitive one" — is correct. The reasoning
offered for it is not: they resolve the paradox by appealing to the
fitted read extracting "far more signal where signal exists", which is an
argument about position 6 and not a measurement at the nine positions,
and they let the identical-power figure stand as measured. One line of
arithmetic would have replaced the appeal with the measurement.

### RT-74 — what the registration requires before "not localized" or "absent"

**Serious. Carried from the previous review rather than new. MEASURED.**
The packet asks what the registration still requires. The answer is
unchanged and the findings state it correctly and without softening,
which is to their credit.

Amendment A3 section 3.2 lists four numbered steps and the fourth is a
requirement:

> **Convergence requirement**, inherited: L1 counts as localized only
> when probe and patching agree on a confound-controlled design;
> otherwise the outcome is *not testable (localization)*, as Experiment 1
> registered.

The fifth adds that "the two-method requirement is met by probe plus
patching". The second method is causal patching: take the candidate
subspace out of an episode where the model is one agent, put it into the
matched episode where it is another, and see whether the action follows
the patched identity.

**Causal patching has still never been run.** The previous review checked
all six code files it was given and found no intervention of any kind; I
have checked the one code file I was given and it is the same — every
capture in it is read-only, the model is loaded, evaluated under a
no-gradient context, and deleted before scoring begins. Nothing in this
run changes a model's computation and then looks at what the model does.

So three statements are available and the third is the registered one:

- **"Not localized"** — not available. The registered condition for
  localization is agreement between two methods, and only one has run.
- **"Absent"** — not available, and further from available than before.
  The pre-registration's procedure step 8 reads the pattern the other way
  round: "if the instruments cannot recover a center that is known to be
  there, Experiment 1's null was instrument failure." Ownership is known
  to be load-bearing on these models. A probe-only null against a centre
  known to be doing work is registered as evidence about the instruments.
- **"Not testable (localization)"** — this is the registered phrase for
  where the line now stands, and it is where it stands.

The findings say all of this, cite the two ledger rows that established
it (`RT-49`, `RT-50`), and list patching first among the open items as
the binding one. Nothing needs correcting. It is repeated here because
the packet asks for it and because it is the clause most likely to be
dropped when the paragraph is shortened for the status file.

### RT-75 — the rulings were honoured

**Worth-noting, and it is credit. MEASURED.** The previous review
produced nineteen ledger rows and John ruled on all of them. I checked
each ruling that bore on this run against the method, the code and the
findings, and found none ignored:

the sensitivity finding (`RT-33`) is not merely cited but measured
directly on one target at one position, which is more than was asked; the
quiet-direction mechanism (`RT-34`) is carried into the method as a
stated cost rather than argued away; the missing register-index control
(`RT-35`) is answered by stating in advance that there is none and what
that costs; the legibility gap (`RT-36`) is quoted and explicitly not
resolved, with the findings refusing to offer their own flat control as
an explanation; the smallest detectable signal (`RT-37`) is reported per
test; the unreported degeneracy hits (`RT-38`) are answered by reporting
that none fired; the shared fold splits (`RT-39`) are fixed with per-test
seeding and the fix is verified by the code's own self-test; the
one-position geometry (`RT-40`) is measured at all 165 tests; the
exhaustive cells (`RT-41`) report their sub-pattern; the negative control
(`RT-42`) is read one way only, in the findings' own words; the
committed-file rule (`RT-43`) is honoured by putting two corrections in
the findings rather than editing the method; and the registered limits
(`RT-49`, `RT-50`) are carried in full.

That is nineteen rulings and no drift. Given that the previous review's
central complaint was a caveat drifting to nothing across four successive
findings files, this is the thing most worth recording about the run.

### The sentence for the status file

The packet asks for it, so here it is. It replaces whatever the status
file currently says about the linear read, and it is written to be
quotable in pieces, because it will be.

> A fitted linear classifier, run at eleven positions and five layers on
> all three 30-million-parameter checkpoints, does not find the model's
> register index anywhere except at the token where its own marker is the
> input. The controls held everywhere: the register index reads at 34 to
> 54 standard deviations at that token on every checkpoint, and the
> negative control shows no leak at the position where the answer is not
> yet knowable. One test reached three standard deviations without
> reaching the family-adjusted bar of 3.38, at the other agent's revision
> value on seed 2; the same position is the highest testable position on
> all three checkpoints and in all fifteen of its tests, and it is
> recorded as an open item rather than a result. This closes the fitted
> read on the register index. It does not close the linear read: the
> registered target is the model's own marker word, and no fitted read
> has ever been run on it at these nine positions — only the
> difference-of-averages read, which this run measures as recovering five
> to nineteen times less than a fitted classifier on the same target at
> the same position. Neither "not localized" nor "absent" may be said of
> any of this: Amendment A3 section 3.2 requires probe and causal
> patching to agree before anything counts as localized, patching has
> never been run, and the pre-registration reads a probe-only null
> against a centre known to be load-bearing as instrument failure. The
> registered term for where this stands is *not testable (localization)*.

**If it has to be shorter**, the three clauses that must survive are: the
registered target has never been read this way at these positions; the
run would have found a signal legible in about one episode in eleven, not
one in twenty-seven; and causal patching has never run, so nothing here
is absence.

**One sentence the status file should not carry**, in any form: that the
run would have found a signal in one episode in twenty-seven. It is the
figure the findings lead with and it is too generous by about two and a
half times (`RT-56`).

---

# The kill case

*Required whether or not the interpretation should stand.*

The kill case is that this run answered the previous review's question
about the wrong target and then wrote its null as though it had answered
it about the right one. The ledger's fatal finding was that the sweep
used a read about half as sensitive as one already sitting in the
repository; the fix was to point the sensitive read at the nine positions
that matter, and the fix was carried out — beautifully, with an
instrument check locked at both ends, per-test seeding, geometry at every
position, pre-stated cells that were applied exactly as written, and two
public corrections to its own method file. Every number in it reproduces.
But the registered target is the model's own marker word, which this
stack's own previous review established and John accepted, and the
marker-word target was priced at seventy processor-hours and dropped
before the run began. So the instrument that was built to answer the
objection was aimed at the four-answer recoding, and at the nine
positions that matter the registered target has still only ever been read
by the instrument the ledger already called fatally insensitive — a gap
this very run re-measures and finds is not a factor of two but a factor
of five to nineteen. On top of that the null is softer than it reads: the
smallest signal the run could have caught is about one episode in eleven
rather than one in twenty-seven, because the measure assumes a perfect
read is possible and the only ceiling the run ever measures is 0.55; the
bar is set for 135 independent tests when all three checkpoints read the
same four thousand episodes; the fit leaves 448 directions unscaled under
a squared penalty that charges a quiet direction the square of how quiet
it is, which is precisely the hypothesis under test; and the one position
that looks like anything — positive in fifteen tests out of fifteen, at
the other agent's revision value — is set aside with a reason that
misdescribes what was measured, when the control that would settle it is
already registered as L2(a) and costs the same eleven processor-hours the
run just spent. None of that makes FOUND NOWHERE wrong. It makes it a
smaller result than the sentence it will be asked to support, and the
line should be retired, if at all, after two more cheap runs: the
marker-word target under this same fitted read, and the other-agent index
at these same eleven positions.

---

## What I would do next, in order

1. **Run the other-agent index at the eleven positions** (`RT-64`). Four
   answers, the same captured states, the same eleven processor-hours,
   one new target function. It is registered as matched control L2(a), it
   has never been run, and it decides whether the run's one interesting
   pattern is a self-index carried away from an act position or an
   exclusion artefact. Cheapest decisive measurement available.
2. **Run the marker-word target under the fitted read at the nine
   positions** (`RT-71`). Seventy processor-hours. Until this exists, no
   sentence about "the linear read" and the registered target can be
   written, and the line cannot honestly be retired.
3. **Refit standardised, at the nine positions, as a declared second
   instrument with its own anchor** (`RT-58`). Same cost as the run just
   done. It separates "not linearly present" from "not reachable under
   this penalty", which is the one thing the positive control cannot
   certify.
4. **Correct the sensitivity figure wherever it has been written**
   (`RT-56`). One episode in eleven, not one in twenty-seven, and say
   which ceiling the correction uses.
5. **Report consistency across layers and checkpoints, not only per-test
   clearance** (`RT-62`), in any future sweep of this shape. The analysis
   that found nothing had no way of seeing the one thing in its own data
   that looks like something.
6. **Causal patching** (`RT-74`). Already the binding open item and
   already on the 2026-10-04 control-battery decision. Nothing above
   substitutes for it.

## How the checks in this review were run

Every number above came from one of three places, and each is marked in
the text.

Read directly from the committed machine records under `a3-gates/`: all
165 tests on all three checkpoints — accuracies, null means, null
spreads, margins, draw counts, labels, majority-class rates, per-class
minimums, optimiser pass counts, degeneracy flags, geometry, and the
per-test detectable shares.

Recomputed by me from those records: the family bar arithmetic at 135,
270, 405, 45 and 9 tests; the evidence a zero-out-of-200 result can
establish; the detectable shares at both bars, which reproduce the
findings' table exactly; the recalibration of those shares against the
measured ceiling at position 6; the per-position means and sign counts
across layers and checkpoints; the spread of margins per checkpoint with
and without the other agent's revision value; the real-fit and null-fit
cap rates separately; and the mean, spread and sign balance of all 135
testable margins against what independent standard normal draws would
give.

Read from the code, not from its comments: the seeding function and its
self-test, the label logic and the order in which its conditions are
applied, the rounding of the margin before comparison, the one-layer
sufficiency of the control gate, the two-way lock on the anchor table,
and the absence of any intervention anywhere in the file.

I ran no model, loaded no checkpoint, and made no outside lookup.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-19-linear-read-closure-packet.md =====

# Review packet — the linear-read closure (Gate B, tier 1)

*Prepared 2026-09-19 (Pacific) under `docs/outside-review-protocol.md`,
ruled in force the same day. This is the first Gate B review under the
protocol: an interpretation that changes program direction, checked before
it enters STATUS.md's current-state section.*

## The interpretation under review

From the session that produced PR 4 (merged 2026-09-19):

> Combined with the anchor result, the linear-read line is closed on these
> checkpoints. But it is not evidence that these models have no self-index,
> and shouldn't be written up as though it were. Eleven positions out of a
> seventy-one-token episode, one statistic, linear, and a per-position read
> cannot see a distributed representation by construction. The honest
> statement is narrower and duller: a linear difference of averages, at the
> positions and layers we chose, does not find one. No registered result
> changes.

Headline as the session wrote it: "Powered eleven-position sweep returns
CARRIED NOWHERE on both arms: zero of 270 testable tests reach even 3 sd
(max +2.73) while positive controls hold at +159 sd and the negative control
shows no leak, closing the linear-read line."

## What the reviewer gets, and nothing else

All in `experiments/06-mvm-0a-constructed-self-index/`, at the commit that
merged PR 4. Read in this order.

Method files (each committed before its run):
- `denoised-direction-method.md`
- `position-sweep-method.md`
- `powered-target-test-method.md`
- `powered-position-sweep-method.md`

Findings files:
- `denoised-direction-findings.md`
- `position-sweep-findings.md` (the sweep found invalid on all three
  checkpoints; the reason was the target)
- `powered-target-test-findings.md` (the anchor result, NOT CARRIED)
- `powered-position-sweep-findings.md` (CARRIED NOWHERE, the result under
  review)

Code the findings were produced by:
- `src/denoised_direction_a3.py`, `src/position_sweep_a3.py`,
  `src/powered_target_test_a3.py`, `src/powered_position_sweep_a3.py`,
  `src/probe_target_diagnostic_a3.py`, `src/marker_legibility_a3.py`

Records: the JSON outputs under `a3-gates/` named `powered_*`,
`probe_target_diagnostic_*` and `denoised_direction_*`.

Registered text the interpretation is read against: `amendment-a3.md` and
`pre-registration.md`.

Do not open: STATUS.md, the compute ledger, any chat transcript, any
uncommitted file, or `docs/`. Say at the top of the findings file what was
opened.

## The brief (fixed text from the protocol)

Four parts, in this order, a table first in each, severity marked fatal,
serious, or worth-noting, and a one-paragraph kill case at the end whether
or not you think the interpretation should stand.

1. **Feasibility.** For every quantity the method files pre-state or
   threshold (the family bar, the 1,000-draw null, the positive and negative
   controls, the anchor reproduction): can it be measured at all with the
   stated instrument, and can the control condition actually reach the
   stated threshold? Cite the committed record that shows so, or say that
   none exists. A "verified" or "measured" claim with no record behind it
   is a fatal finding on its own.
2. **Satisfied by the wrong thing.** Every way "carried nowhere" could be
   returned by a model that does carry own-agent identity linearly at these
   positions (a probe that cannot see it, a target still ill-posed, a null
   that is too wide, an exclusion of positions that removed the ones that
   matter).
3. **No verdict.** Every way the sweep could have failed to return a verdict
   and been read as one anyway.
4. **Over-reading.** What "the linear-read line is closed" will be read as
   claiming in STATUS.md, in the paper, and in public, beyond what was
   measured. Say whether the session's narrower statement above is the
   right wording for STATUS.md, and if not, write the sentence that is.

Label every finding MEASURED (you ran a check and report its output) or
ARGUED (reasoning a reader can dispute). Continue the ledger numbering from
RT-32. Plain language throughout. Lookup allowed and flagged. Do not soften
findings to be polite.

## Filing

Findings to `reviews/2026-09-19-linear-read-closure-claude-worktree.md`,
verbatim, never edited after filing. Rulings go in `red_team_ledger.md`.
Nothing from this review enters STATUS.md until John rules on it.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-19-linear-read-closure-claude-worktree.md =====

# Outside review — the linear-read closure (Gate B, tier 1)

*Filed 2026-09-19 under the outside-review protocol, against the review
packet `2026-09-19-linear-read-closure-packet.md`. Verbatim on filing and
not edited afterwards. Nothing here is a ruling; rulings are John's and go
in the red-team ledger (`red_team_ledger.md`).*

## What was opened

Read at the commit that merged pull request 4 (`eaff1d5`), in a fresh
worktree checked out at that commit. Exactly the packet's list and nothing
else:

- The four method files: the denoised-direction method
  (`denoised-direction-method.md`), the position-sweep method
  (`position-sweep-method.md`), the powered-target-test method
  (`powered-target-test-method.md`), the powered-position-sweep method
  (`powered-position-sweep-method.md`).
- The four findings files with the matching names ending
  `-findings.md`.
- The six code files named in the packet, under `src/`:
  `denoised_direction_a3.py`, `position_sweep_a3.py`,
  `powered_target_test_a3.py`, `powered_position_sweep_a3.py`,
  `probe_target_diagnostic_a3.py`, `marker_legibility_a3.py`.
- The fifteen records under `a3-gates/` whose names begin `powered_`,
  `probe_target_diagnostic_` or `denoised_direction_`.
- Git metadata only — commit dates, messages and the list of files each
  commit touched — used to check the "committed before the run" claim.

**Not opened**, as instructed: the status file (`STATUS.md`), the compute
ledger (`compute-ledger.md`), the `docs/` folder including the research
note the denoising idea came from, the registered texts
(`amendment-a3.md` and `pre-registration.md`), the red-team ledger
(`red_team_ledger.md`), any chat transcript, any uncommitted file, and the
model checkpoint files themselves.

Two consequences of that, stated so they are not mistaken for omissions.
**First**, the packet says the interpretation is read against the
registered texts, and those are on the do-not-open list, so I cannot check
the interpretation against them. Nothing below turns on registered text.
**Second**, I could not read the red-team ledger to see the last number
used, so I have numbered findings from **RT-33**, reading "continue from
RT-32" as meaning RT-32 is taken. If that is off by one, the numbers
renumber trivially.

No outside lookup was used. Every number below either comes from a
committed record or from a check I ran myself, and each is labelled.

**Verdict in one line.** The CARRIED NOWHERE result is sound, correctly
computed and honestly reported — I reproduced every published number from
the records. The sentence built on top of it is not. The stack's own
committed records contain a measurement showing that the read used
throughout the sweep is roughly half as accurate as an ordinary fitted
linear read on the same states, and that measurement appears in none of
the four findings files.

---

# 1. Feasibility

*For every quantity the method files pre-state or threshold: can it be
measured at all, can the control actually reach the threshold, and is
there a committed record behind it?*

| # | pre-stated quantity | can it be measured? | record behind it | severity |
|---|---|---|---|---|
| F1 | the family bar of 3.56 standard deviations | yes | recorded in all three sweep files; arithmetic reproduces | none |
| F2 | the per-test bar of 3.0 standard deviations, reported for continuity | yes | recorded per test | none |
| F3 | the 1,000-draw null | yes | every one of the 330 tests records 1,000 draws and a count | none |
| F4 | the positive control reaching the bar | yes, by a wide margin | +159, +21, +29 standard deviations, no draw beating it | none |
| F5 | the negative control | yes | 30 tests, −2.19 to +0.76, none clears | none |
| F6 | reproducing the earlier anchor result | yes | all 60 shared tests bit-identical | none |
| F7 | the scorer agreeing with the original | yes | differences of exactly 0.0, recorded in every file | none |
| F8 | checkpoints verified by checksum | yes | the three checksums in the records match the ones the method files fixed in advance | none |
| F9 | method committed before output | yes | commit history and recorded runtimes agree | none |
| F10 → RT-37 | **the smallest signal the sweep could detect** | yes | **no record anywhere** | worth-noting |
| F11 → RT-38 | **the degeneracy preconditions** | yes | **fired twice; not reported in the findings** | worth-noting |
| F12 → RT-39 | **the independence the family bar assumes** | yes | **five fold splits shared across all 270 tests** | worth-noting |
| F13 → RT-40 | **the geometry of the states at the ten non-anchor positions** | not from the record | **none exists** | worth-noting |

Nothing in this part is fatal. The packet's fatal trigger — a "verified"
or "measured" claim with no record behind it — is not tripped. I went
looking for it and did not find it. The record is in unusually good shape.

**Everything the two headline sentences claim, reproduces.** MEASURED. I
recomputed the published numbers from the fifteen records rather than
reading them off the tables:

| claim in the findings | recomputed | agrees |
|---|---|---|
| 270 testable tests | 270 (330 total, minus 5 layers × 2 arms × 3 checkpoints for each of the two control positions) | yes |
| largest margin +2.73 | +2.73 (seed 1, marker word, the other agent's revision value, layer 8) | yes |
| smallest margin −2.59 | −2.59 (seed 1, register index, the appended question's answer, layer 3) | yes |
| mean across the 270 is −0.085 | −0.0846 | yes |
| nothing reaches 3.0, let alone 3.56 | confirmed, both | yes |
| zero marginal and zero robust clearances among the testable tests | confirmed | yes |
| positive control +159.08 / +20.66 / +29.45 | exact | yes |
| every one of the 22 rows in the two position tables | all 66 numbers exact | yes |
| the anchor "reproduces the previous run exactly" | all 60 shared tests identical to the last decimal place, including the counts of shuffled draws | yes |
| the powered-anchor ranges (−1.85 to +0.49; 308 to 980 draws; 502 to 980 on arm 1) | exact | yes |

**The pre-commitment is real and independently checkable.** MEASURED. The
method file and the code for the eleven-position sweep went in as one
commit at 17:13 Pacific on 2026-09-19, touching no output. The records and
the findings went in as a separate commit at 18:08, 55 minutes later. Each
checkpoint's recorded runtime is about 53 minutes, and the method file says
the three were run as parallel processes — so the timing fits a run started
immediately after the method was fixed, with no room for a run beforehand.
The only change that commit made to existing code was to pass the family
bar in as a parameter and record which value was used; the statistics were
untouched, which is why the 60 shared tests come back bit-identical. This
is the strongest part of the whole package and it deserves saying so.

**The family-bar arithmetic is right.** MEASURED. Recomputing from
scratch: at a 3.0-standard-deviation bar one test in 741 clears by luck;
across 270 tests the chance of at least one false clearance is 30.6 per
cent; the bar that brings that back to 5 per cent is 3.55, quoted as 3.56.
The earlier runs' figures check out too (15 tests → 2.0 per cent, bar 2.71;
30 tests → 4.0 per cent, bar 2.93; 45 tests → bar 3.05, quoted 3.06; 165
tests → 20.0 per cent, bar 3.42, quoted 3.43). The honesty note about 1,000
draws resolving only to about 3.09 standard deviations is also correct.

### RT-37 — the smallest detectable signal is nowhere on the record

**Worth-noting. MEASURED.** No method file and no findings file states how
big a signal the sweep would have found. I computed it from the recorded
spread of each null. To reach the 3.56 bar, the model's own marker word
would have to be read at 5.23 per cent accuracy against a chance rate of 4
per cent, and the register index at 27.93 per cent against 25 per cent.
Put in plain terms, the sweep would detect an identity that is perfectly
legible in as few as **1.3 per cent of episodes** for the marker word, or
**3.9 per cent** for the register index. That is genuinely good power, and
it is a point in the result's favour.

It should be in the findings. A null result whose stated strength is "270
tests found nothing" is much weaker than one that says "270 tests would
have found a signal present in one episode in eighty, and found nothing."
The second sentence is true and is not written down anywhere.

Two things this number does **not** cover, and they are the subject of
part 2: it assumes the identity sits in the directions this read can see,
and it says nothing about a reader other than a difference of averages.

### RT-38 — two pre-stated preconditions fired and the findings do not say so

**Worth-noting. MEASURED.** The method pre-states that a test whose
accuracy exactly equals the majority-class rate is degenerate and gets no
cell. Two testable tests on the pilot did exactly that — the register
index read before the model's own revision turn at layer 7, and at the
appended question's answer token at layer 8, both landing on 0.2582
against a majority-class rate of 0.2582. Both are flagged in the record
and neither is mentioned in the findings, which report all 270 as tests
that answered.

This changes nothing material: both sat around one standard deviation,
nowhere near any bar, and the cell is a null either way. Strictly the
discovery family was 268, which would move the bar from 3.56 to about
3.55. It is worth a line because the whole point of writing preconditions
down in advance is to report them when they fire, and because the
denoised-direction findings set the right precedent by saying explicitly
that nothing was reported degenerate. The eleven-position sweep dropped
that sentence in the run where it would have been untrue.

### RT-39 — the 270 tests share five fold splits and five sets of shuffles

**Worth-noting. MEASURED.** In the code, each test's fold split and its
1,000 shuffled label draws are seeded by the layer number alone
(`measure(..., seed=Lr)`). So every test at layer 3 — both arms, all
eleven positions, all three checkpoints — uses one identical fold split
and one identical sequence of 1,000 shuffles. There are five distinct
splits across the whole sweep, not 270.

This cuts both ways and neither way is large. The nulls at a given layer
move together, so a lucky or unlucky set of shuffles is shared rather than
averaged out. And the family bar treats 270 tests as independent when five
layers reading the same states and two arms sharing a target are strongly
related, so the true bar is lower than 3.56 and the sweep is stricter than
it needed to be. Both are moot in the event, because the largest margin
anywhere was 2.73 and nothing came near even the unadjusted bar. I record
it because the method file's arithmetic is presented as if the tests were
independent and they are not.

### RT-40 — the geometry is known at one position out of eleven

**Worth-noting. MEASURED for what exists, ARGUED for the gap.** The only
measurement of the shape of the state space anywhere in this package is in
the denoised-direction findings: about ten directions out of 448 carry
around 99 per cent of the variation, with the largest single direction at
18 to 34 per cent. That measurement was taken **at the revision position
only** — the anchor — on 400 episodes, at five layers. The
eleven-position sweep reads ten further positions and there is no record
of the geometry at any of them.

This matters because of part 2 below: how much a difference-of-averages
read can see depends on that geometry, and outside the anchor it is
unknown.

---

# 2. Satisfied by the wrong thing

*Every way "carried nowhere" could be returned by a model that does carry
own-agent identity linearly at these positions.*

| # | mechanism | does it survive checking? | severity |
|---|---|---|---|
| RT-33 | the read is far less sensitive than an ordinary fitted linear read, **measured on these very checkpoints** | **yes — and the measurement is already in the record** | **fatal** |
| RT-34 | the read cannot see a linear signal in a quiet direction, at this stack's own measured geometry | yes | serious |
| RT-35 | the register-index arm has no positive control of its own | yes | serious |
| RT-36 | on two of three checkpoints the control recovers the answer on only one episode in eight, and the unexplained gap was quietly upgraded from a caveat to "holds without qualification" | yes | serious |
| — | the target is still ill-posed | no — both targets decode at the marker position, and the generator-index problem is genuinely fixed | — |
| — | the null is too wide | no — the nulls are tight and the detectable signal is small (RT-37) | — |
| — | the positions that matter were excluded | partly — see RT-42 and the note on position 1 | worth-noting |

### RT-33 — the stack's own record shows this read is about half as good as a fitted one, and no findings file reports it

**Fatal to the interpretation under review. MEASURED — the numbers are
read directly out of `probe_target_diagnostic_a3_*.json`, one of the
records the packet lists.**

The target diagnosis ran two instruments side by side on the same states,
same folds, same 400 episodes: the difference-of-averages read used
throughout this line of work, and an ordinary fitted linear classifier
(logistic regression). For targets with more than eight possible answers
the classifier was skipped as too slow, so the marker word was not run
through it — but the **register index has four answers, and it was**.

At the marker position, where the answer is available, on the register
index, chance being 0.25 and the majority-class rate 0.273:

| checkpoint | difference of averages (accuracy, margin) | how many of 5 layers clear | fitted classifier (accuracy, margin) | how many of 5 layers clear |
|---|---|---|---|---|
| pilot | 0.295–0.330, +1.87 to +2.93 | **0 of 5** | 0.5025–0.5250, +9.09 to +10.95 | **5 of 5** |
| seed 1 | 0.250–0.2675, **+0.03** to +0.63 | **0 of 5** | 0.4800–0.5350, +9.41 to +11.96 | **5 of 5** |
| seed 2 | 0.2975–0.3175, +1.88 to +2.24 | **0 of 5** | 0.4475–0.4950, +8.00 to +10.33 | **5 of 5** |

Read seed 1's first row. At a position where own-agent identity is so
strongly and so linearly present that a fitted classifier reads it at 48
per cent against a chance rate of 25 per cent, **the read this whole sweep
depends on returns 0.2500 — exactly chance — at a margin of +0.03 standard
deviations.** That is not a subtle sensitivity difference. It is the
sweep's read returning a flat null on a signal that is unmistakably there.

That is precisely the failure mode part 2 asks about, it is not
hypothetical, and it is measured on these three checkpoints.

Three things follow.

**First, "the read works" is doing more work than it can bear.** The
positive control shows the read can recover the marker word when the
marker word is the token sitting there. It does not show the read is a
good linear reader in general, and the table above shows it is not.

**Second, the justification written into the code for skipping the
classifier is false.** Where the classifier is skipped for having more
than eight answers, the code gives as its reason that a fitted classifier
"adds nothing the read above does not say". The four-answer results in the
very same run say the opposite, by a factor of about two in accuracy and
by the difference between clearing nothing and clearing everything.

**Third, and this is the finding: no fitted linear read has ever been run
against a well-posed target at any of the nine testable positions.** I
traced this through all six code files. The 2026-09-16 probes used a
fitted classifier but asked for the generator's agent index, which the
stack itself has established cannot be recovered. Arm 2 of the first
position sweep compared the two instruments, also on the generator index —
and its own findings say it "would have to be rerun against a well-posed
target to mean what it was designed to mean", listing that as open item 5.
It was never rerun. The two powered runs, which are the ones with
well-posed targets and real power, use the difference-of-averages read and
nothing else.

So the line "the linear-read line of attack on these checkpoints is
closed" describes work that was not done. What is closed is the
difference-of-averages read.

**One qualification, in the result's favour, which I want to state as
plainly as the criticism.** At the anchor, the fitted classifier *also*
finds nothing: on the register index its margins run from −1.90 to +1.61
across the fifteen layer-and-checkpoint tests, clearing nowhere. So the
anchor null — the NOT CARRIED result of the earlier run — is corroborated
by a second instrument, and RT-33 does not touch it. The gap is exactly
over the nine testable positions the eleven-position sweep added, where
only one instrument was ever used. That is the part of the claim that
fails, and it is the part the sweep exists to support.

### RT-34 — why the read misses it, and how quiet a direction has to be

**Serious. MEASURED, by simulation at this stack's own measured numbers.**

Both scorers assign a held-out episode to whichever class average is
nearest in plain straight-line distance, treating all 448 directions of
the state as equally important (`dist = sum((x − mu)²)` in the original,
the same arithmetic as matrix products in the vectorised rewrite). A
fitted classifier does something different: it effectively rescales each
direction by how much the states vary along it, so that a quiet direction
counts for as much as a loud one. When the states vary enormously more in
some directions than others — which is exactly what the denoised-direction
findings measured here — the two come apart badly.

I built states with the spectrum that findings file reports for the pilot
at layer 3 (largest direction 23.3 per cent of the variation, largest
three 50.4 per cent, largest ten 98.8 per cent, 448 directions in total),
at the sweep's own settings: 4,000 episodes, 25 classes, four folds. Into
those states I planted a perfectly linear identity code occupying eight
directions, and scored it with the sweep's scorer copied verbatim, against
its own permutation null of 100 draws. Alongside it I ran an ordinary
fitted linear read (shrinkage discriminant analysis) on the same folds.

| where the identity code sits | sweep's read: accuracy | its margin | clears 3.56? | fitted read: accuracy |
|---|---|---|---|---|
| in one of the ten loud directions | 0.7790 | +210.80 | yes | 0.6590 |
| a direction holding 1 per cent of the variation | 0.5507 | +152.20 | yes | 0.6590 |
| 0.1 per cent | 0.0927 | +13.71 | yes | 0.6590 |
| 0.03 per cent | 0.0542 | +3.60 | yes | 0.6590 |
| 0.01 per cent | 0.0462 | +1.58 | **no** | 0.6590 |
| **a typical direction at the measured anchor (0.0027 per cent)** | **0.0418** | **+0.44** | **no** | **0.6590** |
| no identity code at all (sanity check) | 0.0400 | +0.01 | no | 0.0447 |

Chance is 0.0400. The fitted read gets 0.6590 in every row because
rescaling makes it blind to where the code sits; the sweep's read falls
off a cliff. At the variance share that 438 of the 448 directions actually
have at the anchor, **a cleanly linear identity that a standard fitted
read recovers on two episodes in three produces +0.44 standard deviations
under the sweep's read** — indistinguishable from the 270 numbers the
sweep actually returned. With a weaker code (fitted read 0.22, still five
times chance) the crossover moves up by another factor of ten.

So the answer to part 2's question is yes, concretely and quantitatively:
a model that carries own-agent identity in a perfectly linear form returns
CARRIED NOWHERE on all 270 tests if that identity lives below roughly ten
to a hundred times the typical direction's share of the variation.

**The counter-argument, and why it does not hold.** The
denoised-direction findings argue there is "no room in this geometry" for
a quiet signal under a loud one, because ten directions carry 99 per cent
of everything. That argument confuses how much the states *vary* along a
direction with how much they can *carry*. The remaining one per cent is
spread over 438 directions, and the simulation above puts a fully
recoverable 25-way identity code exactly there. The fitted read finds it
at 0.659. There is room.

I could not test this on the real states, because doing so needs the
checkpoint files and the packet does not list them. It is the obvious next
measurement and it is cheap: the register index, four answers, fitted
classifier, all eleven positions, 4,000 episodes. The machinery already
exists in `probe_target_diagnostic_a3.py`.

### RT-35 — the register-index arm has no positive control of its own

**Serious. MEASURED.**

The method is careful and correct here: it says the control is the
marker-word arm at position 6 and that it governs both arms. The
**findings** go further than that, and the extra step does not hold.

The powered-target-test findings say the register index "is a quantity the
model demonstrably carries *somewhere*" because it reads at four to seven
standard deviations at the marker position, and conclude that its absence
at the anchor "is not a target problem and not an instrument problem".

But the register index is, by construction in the code, the rank of the
model's own marker among the episode's four markers in vocabulary order.
At the marker position the model's own marker is the token sitting there.
Knowing your own marker word already tells you a great deal about its
rank. I worked out how much: with four markers drawn from a pool of 25,
the best possible accuracy at guessing the rank **from the own marker word
alone** is **0.5815**.

The observed readings at the marker position are 0.3093 on the pilot,
0.2605–0.2720 on seed 1, and 0.2865–0.2943 on seed 2 — all well *below*
that ceiling. Every one of them is consistent with a partial read of the
marker token and nothing else. On the same checkpoint at the same position,
the marker word itself reads at 0.5877.

So the register-index clearance at the marker position is not evidence
that the model computes or stores a rank. It is a shadow of the marker
token. The arm has one demonstrated working condition, and in that
condition its target is a function of the current input token — which is
the same thing the method file says makes a position uninteresting.

The consequence for the result under review is bounded but real: arm 2's
nulls at the other ten positions rest entirely on the marker-word control,
and on an untested assumption that a read with power for a 25-way
token-identity target has comparable power for a 4-way derived rank. RT-33
shows that assumption is wrong in the direction that matters.

### RT-36 — the legibility gap was downgraded from a caveat to nothing, without a measurement

**Serious. MEASURED for the numbers, ARGUED for the drift.**

The same input token, at the same position, at the same layers, on three
checkpoints that differ only by training seed, is read at 0.5877 on the
pilot and at 0.1022–0.1398 on seeds 1 and 2. That is the positive control.
On seeds 1 and 2 the read recovers the answer on roughly one episode in
eight **when the answer is the token it is looking at**.

Follow how that fact is handled across the four findings files:

| document | what it says about the gap |
|---|---|
| position-sweep findings | "unexplained… it means the positive control is strong evidence on the pilot and weaker evidence on seed 1"; and as next step 3, "Until that is understood, any read of those two checkpoints rests on a positive control that barely holds, and a null on them means correspondingly less" |
| powered-target-test findings | runs the bounded measurement meant to explain it; reports that neither embedding length nor attention explains it, and that attention runs the wrong way; still lists it as open |
| powered-position-sweep findings | "the control that governs both arms is the marker word, and **it holds without qualification**" |

Nothing measured the gap away. The one measurement aimed at it came back
empty, by its own account. Between the second document and the third, a
stated reason to discount the nulls on two of three checkpoints was
dropped, and the sentence that replaced it says the opposite.

This matters directly for the cell. The CARRIED SOMEWHERE cell needs a
clearance on the pilot *and* on at least one other seed. If the read is
much less sensitive on seeds 1 and 2 — and an eightfold difference in
recovering the input token is strong evidence that it is — then the cell
is harder to reach than it appears, and CARRIED NOWHERE is correspondingly
easier to land in. The sweep has no calibration of the read's sensitivity
on those two checkpoints at all.

To be fair to the run: the pilot's control is excellent, and the pilot
alone shows nothing at any testable position. So the result does not
collapse. But "holds without qualification" is not a sentence the record
supports, and the earlier document had it right.

---

# 3. No verdict

*Every way the sweep could have failed to return a verdict and been read
as one anyway.*

| # | route to a non-verdict | did it happen? | severity |
|---|---|---|---|
| RT-38 | a pre-stated degeneracy precondition fires and is not reported | **yes, twice** | worth-noting |
| RT-41 | the two cells are exhaustive by construction, so a partial pattern lands in CARRIED NOWHERE | no — nothing cleared anywhere, and the method names the risk and reports the sub-pattern | none |
| RT-42 | the negative control is read as licensing more than it can | yes | worth-noting |
| RT-43 | a date on the pre-committed files that disagrees with the commit | yes | worth-noting |
| — | the positive control fails and the arm is read anyway | no — it clears at +159/+21/+29 with no draw beating it, and the code enforces it | none |
| — | the cell is assigned by hand rather than by the pre-stated rule | no — the rule is in code, unit-tested, and the summary record agrees with the findings | none |
| — | the bar is chosen after seeing the numbers | no — committed 55 minutes before the outputs, in a separate commit, with runtimes that fit the gap | none |

On the whole this part comes back clean, and more thoroughly clean than I
expected. The cell-assignment rule is implemented in code, the self-test
checks it against constructed cases including the awkward ones ("cleared
on the pilot only" must land in CARRIED NOWHERE *and* must report the
sub-pattern), and the summary record matches the findings text exactly. The
negative control's premise — that the model's own marker really has not
appeared anywhere before its first own value token — is verified against
real episodes in the self-test rather than asserted. That is the right way
round and it is rare.

Two things to record.

### RT-41 — the exhaustive pair of cells, and why it is not a problem here

**No finding. Recorded for completeness. MEASURED.** Making CARRIED
NOWHERE mean "the other cell did not fire" means it absorbs outcomes that
are not nothing. The method names this cost in advance and requires the
clearing positions to be reported per checkpoint whatever the cell says.
In the event, zero of the 270 testable tests cleared anything on any
checkpoint, the summary record says "nothing cleared on any checkpoint",
and there is no sub-pattern being hidden. The design risk is real and did
not bite.

### RT-42 — the negative control is weaker than the sentence built on it

**Worth-noting. ARGUED, from measured placement.** The findings say the
clean negative control is "the reason the other 270 numbers can be taken
at face value". That is more than it can carry, in two ways.

A leak at position 1 would have cast doubt on everything; no leak at
position 1 does not validate the other positions. The inference only runs
one way.

And position 1 is the weakest place in the episode to look for a leak from
the acting channel. The channel is described as a projection of the
model's own preceding state, added at the value token of each of its own
turns. At the model's *first* own turn there is barely any preceding own
state to leak. The positions where the channel would have the most to
carry are the model's second assignment and its revision value — and those
are inside the testable set, where they read +1.16/+0.42/+0.64 and
+0.55/+1.36/+1.78. So the leak question is in fact answered, and answered
reassuringly, but by the testable positions rather than by the negative
control. The negative control on its own establishes less than the
sentence claims.

This does not weaken the null. If anything it strengthens the reading that
nothing is leaking. It is the phrasing that overreaches.

### RT-43 — a date on the pre-committed files that does not match the commit

**Worth-noting. MEASURED.** The eleven-position sweep's method file and
findings file are both headed *2026-09-20*. Both were committed on
**2026-09-19** Pacific (17:13 and 18:08), as was everything else in the
sequence, and the packet itself is dated 2026-09-19. Almost certainly a
clock written in a different time zone. It is cosmetic and it is worth one
line only because these are the files whose entire value is *when* they
were written relative to the run, and a reader checking that chain will
hit a date that disagrees with the commit. The commit order is what
matters and it is correct.

---

# 4. Over-reading

*What "the linear-read line is closed" will be read as claiming, beyond
what was measured.*

| # | the sentence | what a reader will take it to mean | what was measured | severity |
|---|---|---|---|---|
| RT-44 | "closing the linear-read line" | no linear read finds own-agent identity at these positions | one linear read — a difference of averages — finds nothing; the fitted read was never tried at nine of the eleven positions | **fatal** |
| RT-45 | "the instrument demonstrably works" | the read has the sensitivity of a competent linear probe | the read recovers a token that is present; on a well-posed target at a position where both were tried, it scores about half what a fitted read scores | serious |
| RT-46 | "the rest of the episode is empty too" | the episode carries no own-agent identity | eleven positions of a seventy-one-token episode, by one read, carry none that this read can see | serious |
| RT-47 | "this was the last run in this line" | the question has been settled and the line can be retired | the cheapest and most obvious follow-up — a fitted classifier on the four-answer target at all eleven positions — has not been run | serious |

### RT-44 — the headline claim is not supported, and the record contradicts it

**Fatal. ARGUED, resting on the measurements in RT-33 and RT-34.**

"The linear-read line of attack on these checkpoints is closed" will be
read in the status file, in a paper and in public as: *we looked for a
linear self-index with linear methods and there is none to find.* The
measurement supports something much narrower: *nearest-class-average
distance in the raw state space finds none.* Those are different claims,
and the gap between them is not academic — it is the difference between
0.2500 and 0.4800 on seed 1 at the marker position, which is in the
committed record.

A paper that says "we closed the linear read" and is then asked "did you
try logistic regression?" has no good answer, because the honest one is
"we tried it only on a target we had already shown was unrecoverable, and
in the one place we tried it on a good target it beat our method by
roughly two to one, and we did not report that."

### RT-45 — "the instrument demonstrably works"

**Serious. MEASURED, via RT-33.** The sentence is true of the one thing
the positive control tests: the read can recover a token that is present
at the position being read. It is not true in the sense a reader will take
it — that the read is a competent linear probe whose null is worth
something. The record shows it scoring about half what an ordinary fitted
classifier scores on a well-posed target at the one position where both
were run. "The instrument works" should be replaced with "the instrument
recovers the input token", which is all that was shown.

### RT-46 — eleven positions of seventy-one

**Serious. ARGUED.** The session's own narrower statement already makes
this point, and makes it well. I add only that the eleven positions were
chosen because they are the structurally interesting ones, which is the
right way to choose them, and that it still leaves about sixty tokens
unread — every token of the other agents' turns apart from the one
reviser's two, and almost all of the first eight turns. I could not verify
the figure of seventy-one tokens from the listed records; it is consistent
with the template the code uses (a one-token prefix and ten turns of seven
tokens each), but no record states the episode length.

### RT-47 — "this was the last run in this line"

**Serious. ARGUED.** Retiring the line is a decision, not a measurement,
and it is being taken one obvious experiment too early. The first sweep's
own findings list rerunning the two-instrument comparison against a
well-posed target as open item 5. It remains open. Until it is closed the
line has not run out of cheap questions, and stopping here means the
strongest claim the sequence makes is the one claim it did not test.

### Is the session's narrower statement the right wording for the status file?

**Nearly, and not quite.** The session wrote:

> The honest statement is narrower and duller: a linear difference of
> averages, at the positions and layers we chose, does not find one.

That sentence is **true, and it is the right instinct**. It names the
instrument instead of the class of instruments, which is exactly the
correction RT-44 asks for. Two things stop it being sufficient on its own.

It appears in a paragraph whose heading and surrounding text say the
linear-read line is closed, so a reader takes the narrow sentence as a
modest restatement of the broad one rather than as a replacement for it.
The broad sentence is the one that will be quoted.

And it omits the fact that makes the distinction bite. "A difference of
averages does not find one" reads as a technicality unless the reader also
knows that a fitted linear read, on these states, at the one position
where both were tried, found a great deal more. Without that, nobody will
understand why the narrower wording was chosen, and the broader wording
will creep back.

**The sentence I would put in the status file**, in place of any claim
that the linear-read line is closed:

> Across eleven positions and five layers on all three 30-million-parameter
> checkpoints, a difference-of-averages read finds no own-agent identity —
> neither the model's own marker word nor its register index — anywhere
> except at the token where the marker is the current input. The controls
> held: the read recovers that input token at up to 159 standard
> deviations, and the negative control shows no leak. What this closes is
> the difference-of-averages read, not the linear read: a fitted linear
> classifier was never run at any of these positions against a well-posed
> target, and in the one place both were tried it read the register index
> at about twice the accuracy. The registered probe position is a stronger
> result than the rest, because both instruments find nothing there.

If that is too long, the part that must survive is the third sentence.

---

# The kill case

*Required whether or not the interpretation should stand.*

The kill case is that this sequence mistook the exhaustion of one
instrument for the exhaustion of a class of instruments, and wrote the
stronger sentence. Every number in the eleven-position sweep is correct,
every control behaved, the pre-commitment is real and I verified it three
ways — but the sweep measures straight-line distance to a class average in
a state space the stack itself has measured to be wildly lopsided, where
ten directions out of 448 hold 99 per cent of the variation. In such a
space that measurement is blind to any signal living in a quiet direction,
and I have shown both by simulation at the stack's own measured geometry
and, more damningly, from the stack's own committed records on its own
checkpoints, that the gap between this read and an ordinary fitted linear
read is about a factor of two in accuracy and the difference between
clearing zero of fifteen tests and fifteen of fifteen. On seed 1 at the
marker position the sweep's read returns exactly chance on a signal a
logistic regression reads at 48 per cent. That comparison sat in
`probe_target_diagnostic_a3_*.json` while four successive findings files
were written, and none of them reports it; the first sweep's own findings
even listed rerunning that comparison against a well-posed target as open
item 5, and it was never done. So the line "the linear-read line is
closed" describes an experiment nobody ran, one that would cost an
afternoon with machinery that already exists in this repository. The
narrow, dull, correct claim — a difference of averages at eleven chosen
positions finds nothing, and the registered probe position is empty under
two instruments rather than one — is a real result and worth recording.
The broad one should not enter the status file, and if this line of work
is to be retired, it should be retired after the four-answer target has
been put through a fitted classifier at all eleven positions, not before.

---

## What I would do next, in order

1. **Run the fitted classifier on the register index at all eleven
   positions**, 4,000 episodes, 1,000 draws, three checkpoints. Four
   answers, so it is affordable; the code exists in
   `probe_target_diagnostic_a3.py`. This is the measurement that decides
   whether "linear-read line closed" is true or false. It needs its own
   committed method file and its own cells.
2. **State the smallest detectable signal** in any future findings file of
   this kind. The numbers are in this review (RT-37) and they help the
   result.
3. **Do not let the legibility gap between checkpoints disappear.** Either
   explain it or restore the qualification the first sweep's findings put
   on nulls from seeds 1 and 2 (RT-36).
4. **Drop the claim that the register index is demonstrably carried**
   (RT-35). Everything observed at the marker position is below what the
   marker token alone determines.
5. Report the two degenerate tests (RT-38), and correct the file dates
   (RT-43).

## How the checks in this review were run

Everything is reproducible from the listed records alone. The
recomputations of the published numbers, the family-bar arithmetic, the
smallest-detectable-signal figures, the per-position aggregates, the
degeneracy scan and the rank ceiling are plain arithmetic over the fifteen
records and need nothing else. The geometry simulation in RT-34 copies the
sweep's scorer and its fold construction verbatim from
`powered_target_test_a3.py` and `denoised_direction_a3.py`, uses the
spectrum reported in `denoised-direction-findings.md`, and compares against
shrinkage discriminant analysis from scikit-learn at the sweep's own
episode count, class count and fold count. It uses 100 permutation draws
rather than 1,000, which is ample for estimating the spread of a null and
is the only place any setting differs from the sweep's own.

No checkpoint file was opened and no model was run.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-19-linear-read-closure-claude-worktree-addendum.md =====

# Addendum — the registered text, which I should have read first

*Filed 2026-09-19, after the main review
(`2026-09-19-linear-read-closure-claude-worktree.md`) and as a separate
file, because the protocol says a filed review is verbatim and never
edited afterwards. Nothing in the main review is withdrawn. Everything
here is additional, and all of it points the same way the main review
already did.*

## The mistake, which is mine

The review packet lists two registered documents under what the reviewer
gets: *"Registered text the interpretation is read against:
`amendment-a3.md` and `pre-registration.md`."* I misread that line as part
of the do-not-open list, did not open either file, and said so at the top
of the filed review as though the packet had forbidden them. It did not.
Two of the listed sources went unread, and the statement in the review
about why is wrong.

That is a real gap, not a formality: those two documents are what the
interpretation is supposed to be measured against, and part 4 of the brief
— what the claim will be read as beyond what was measured — is exactly the
part they bear on. I have now read them and this addendum reports what
they change.

**They change the verdict's strength, not its direction.** The registered
text does not rescue "the linear-read line is closed"; it gives two
further, independent reasons why that sentence should not be written, and
one point of credit to the powered runs that the main review missed.
Numbering continues from RT-47.

---

| # | finding | severity | label |
|---|---|---|---|
| RT-48 | the powered runs finally use the **registered** probe target; every earlier probe was off-spec against the registration, not merely ill-posed | worth-noting (credit) | MEASURED |
| RT-49 | the registration requires **two** methods and a convergence rule; causal patching has never been run, and a probe-only null is registered as "not testable (localization)" | serious | MEASURED |
| RT-50 | the registration's own reading of a localization failure against known-load-bearing ownership is **instrument failure**; the interpretation reads the same pattern the opposite way without saying so | serious | MEASURED |
| RT-51 | this reviewer skipped two listed sources and misdescribed why | worth-noting | — |

---

## RT-48 — the registered target was the marker all along

**Worth-noting, and it is credit rather than criticism. MEASURED.**

Amendment A3 defines the thing to be located, at section 3.1, as a
subspace "that carries *'which marker is mine'* at positions away from act
positions (revision turns and query positions)". Section 3.2 spells out
the instrument: linear probes that "decode **own-marker identity** from
the residual stream at revision and query positions".

So the registered target is the model's own marker. It is not the episode
generator's agent index. Every probe in this stack up to and including the
first eleven-position sweep predicted the generator's index, which the
registration never asked for and which the stack later showed cannot be
recovered at all.

This sharpens the sequence's own account of itself in a way none of the
four findings files says. The earlier probes were not merely asking a
question with no answer — they were asking a different question from the
registered one. And the powered runs, by moving to the model's own marker
word, are the first runs in the whole line to probe **the target the
registration specified**. That deserves saying plainly, and it makes the
NOT CARRIED result at the registered position a more serious result than
the findings claim for it, not a less serious one.

## RT-49 — the registration takes two instruments, and only one has ever been run

**Serious. MEASURED.**

Amendment A3 section 3.2 lists the localization method as four numbered
steps, and the fourth is a requirement, not a suggestion:

> **Convergence requirement**, inherited: L1 counts as localized only when
> probe and patching agree on a confound-controlled design; otherwise the
> outcome is *not testable (localization)*, as Experiment 1 registered.

The fifth adds: "the two-method requirement is met by probe plus
patching." The second method is causal patching — taking the candidate
subspace out of an episode in which the model is one agent, putting it
into the matched episode in which it is another, and seeing whether the
action follows.

**Causal patching has not been run anywhere in this sequence.** Not in the
denoising diagnostic, not in either position sweep, not in the powered
anchor test. Every result under review comes from the probe leg alone.

Checked rather than assumed: across all six code files the packet lists
there is no patching, swapping, ablating or intervening of any kind. Every
place the word "patched" appears is a read-only capture hook — it calls
the block's own forward, records what comes out, and returns it unchanged
— and the one place attention is recomputed says in its own method file
that the model's output path is left untouched. Nothing in this sequence
changes a model's computation and then looks at what the model does.

Two things follow, and the second is the one that matters.

The run is unregistered and says so on every page, so it is not bound by
the registered bin logic and I am not claiming it breached anything. But
the registered vocabulary for "one instrument looked and found nothing" is
**not testable (localization)** — an explicit refusal to read the result
either way. The sequence has instead written "closed". The registration
had already decided that a single-instrument null does not close anything,
and it decided that before any of this ran.

And it compounds the main review's finding RT-33 rather than duplicating
it. RT-33 says one instrument was used where two ordinary linear readers
were available and they disagree sharply. This says that even the intended
*second* method — the causal one, which is the stronger evidence and which
no rescaling argument can touch — was never applied. So "the linear-read
line is closed" rests on one leg of a two-legged registered procedure,
using the weaker of two available versions of that leg.

## RT-50 — the registration reads this pattern as instrument failure

**Serious. MEASURED.**

The situation on the pilot is: ownership is *known* to be load-bearing,
because zeroing the acting channel takes the ownership battery from 0.506
to 0.182, and the localization instruments cannot find it. The
registration says in two places what that combination means.

The pre-registration, at procedure step 8, on running the localization
pipeline against a centre known to exist:

> if the instruments cannot recover a center that is known to be there,
> **Experiment 1's null was instrument failure.**

And Amendment A3's own red team, at R7, on exactly the outcome that has
now occurred:

> Ownership is load-bearing (L0 collapses T_act) and no subspace at k ≤ 16
> beats the controls… If Experiment 1's pipeline cannot carve it, the
> honest reading of Experiment 1's null shifts toward **instrument
> failure**, which is the single finding RT-12 said might outweigh the
> headline.

The registered bin for the outcome, H_diffuse, is named "present but
uncarvable", and its registered reading is: "self-location is present in
the doing and not carvable by these instruments at this rank." Every one
of those sentences puts the weight on the instruments. None of them
licenses a statement about what the model does or does not carry.

The interpretation under review points the other way. It reads the
instruments as sound ("the instrument demonstrably works", "the instrument
is not in question") and the episode as empty. It reaches that by treating
the positive control as a warrant for the read's general sensitivity —
which the main review's finding RT-33 shows, from this stack's own
committed records, that it is not.

So the registered framework and the measured evidence agree with each
other and disagree with the sequence's headline. The registration
anticipated this exact pattern, wrote down that it points at the
instruments, and flagged it as possibly the most valuable thing the
program could find. The sequence has arrived there and described it as the
opposite.

I want to be careful about one thing. This does **not** mean the result
should be written up as instrument failure either. The honest position is
the registered one: with one of two methods run, in its weaker form, a
null is *not testable* for localization, and the open question is whether
the instrument or the model is responsible. The measurement that separates
those two is the same one the main review already named — the fitted
classifier at all eleven positions — with causal patching behind it.

## RT-51 — the reviewer's own error

**Worth-noting.** Recorded because a review that suppressed it would be
worth less than one that did not. I read eight of the ten document sources
the packet listed, misattributed the omission to the packet's do-not-open
line, and filed. The two I skipped strengthen the review's conclusion, so
nothing in the filed findings is softened by the correction — but that is
luck, not method, and the filed review's account of what was opened should
be read together with this file rather than on its own.

## What this changes in part 4

The replacement sentence offered in the main review still stands, and one
clause should be added to it. After "a fitted linear classifier was never
run at any of these positions against a well-posed target", add:

> …and neither was causal patching, which the registration requires
> alongside the probe before anything counts as localized.

With that, the status file says what happened: one leg of a two-leg
procedure, in its weaker form, found nothing at eleven positions, at the
registered target, with working controls at the one position where the
answer is the input token.


===== FILE: experiments/06-mvm-0a-constructed-self-index/compute-ledger.md =====

# MVM-0a compute ledger

*The registered budget instrument. Cap: **$200 for the entire registered
design** (learnability pilots, 5 seeds × full+twin, ablation passes, θ/δ
null-calibration, blind-localization arm) — adjudicated 2026-08-07,
derivations in `registration-decision-memo.md` §1. Once the registration
lands, exceeding the cap is a protocol violation, not just an overspend:
work stops and any continuation is a registered amendment.*

## Rules

1. **Every pod session gets a row** — written in the same session the pod
   is deleted, with the estimate recorded *before* the run and the actual
   after. STATUS entries already carry per-session costs by habit; this
   table is the running total against the cap.
2. **Estimate before spend.** A run whose pre-run estimate would take the
   running total past $200 does not launch.
3. **Pods always launch with `--terminate-after`** (standing ops rule), so
   no single run can exceed its own estimate by more than the terminate
   window.
4. **Reconcile against RunPod's own billing** (console → Billing) at each
   phase boundary (pilot → training → ablation → localization); the
   ledger's total and RunPod's lifetime-spend-since-2026-08-07 should
   agree to within a dollar, and a disagreement is investigated, not
   averaged away.
5. The hard backstop is upstream of this file: **the RunPod account is
   funded by prepaid credits with auto-reload OFF**, topped up in
   increments John chooses, never past the cap's remainder. The account
   physically cannot overspend what the ledger permits.

## Reconciliation baseline

RunPod balance at adjudication (John, checked 2026-08-07): **$106.73**
(prior spend from $150 predates this cap — Experiment 1 / Stage 3 work;
this ledger starts at $0). Rule 4 reconciles against this number:
expected balance = $106.73 − ledger running total − storage drip since
this date. Auto-reload: **OFF** (John's setting; the Layer-3 backstop).

**Top-up 2026-08-12: +$25.00** (John, after the 30M drain cleared the
account — covers the −$0.07 deficit, keeps `mvm-models` on a funded
account, and gives the weekend session prep headroom; deliberately NOT
pre-funding the re-run, which awaits the cap adjudication). Balance
after top-up (API-verified): **$24.93**. Rule-4 arithmetic from here:
expected balance = $24.93 − new spend − ~$0.35/day volume drip.
Cumulative top-ups against the $200 cap: $106.73 baseline + $25 =
$131.73 total funds this ledger has seen; cap remainder ≈ **$94.4**
(unchanged by the top-up — the cap counts spend, not deposits).

**Top-up 2026-08-16: +$120.00** (John, funding the A2 5-seed program;
balance $199.70 API-verified at add, $199.64 at wave-1 launch).
Cumulative funds this ledger has seen: $131.73 + $75 (08-15) + $120 =
**$326.73**; spend ~$124.5 against the **$400 A2 cap** → cap
remainder ≈ **$275.5**.

## Ledger

| date | phase | what ran | GPU | hrs (est → act) | $ est | $ actual | running total |
|---|---|---|---|---|---|---|---|
| 2026-08-07/08 | pilot | 10M learnability pilot, seed 0, code `e0bd13e`, 171.79M tok (20/param), held-out eval. Pod 1 `977cezdx6klgbt` (secure 4090, deleted before use — dead `sshCommand` field, pod was healthy); pod 2 `zv0nxkyazqfw0w` (community 5090, ran the pilot). **RESULT: LEARNS, all batteries ≥0.97** (`pilot-findings.md`) | 4090 $0.74 (12.6 min) + 5090 $0.69 community | 1–2.5 → 2.4 (+0.2 dead pod) | $1.50 (cap $2.96) | **$6.02** ⚠ | **$6.02 / $200** |
| 2026-08-09/10 | pilot (A1, 30M) | **30M A1 pilot** — ladder rung 2 per the smallest-that-learns rule (10M FAILED, `pilot-a1-findings.md`). 39,204,192 actual params × 20 tok/param = 784.08M tokens ≈ 102k steps, batch 128, seed 0, held-out eval + T_sr_rev split. H_scale vs H_shortcut-starvation, signatures pre-stated. **Venue: H100 SXM secure** ($2.99/hr — compresses ~32–44h community wall-clock to ~11–16h and avoids the community-row billing anomaly); crash-resume support added to train.py (opt state in checkpoints, --resume; resume-after-crash needs a fresh C2 go). John's go: "Fire it" (2026-08-09). 24h terminate-after backstop. Pod `6bplni87uzp3ss` launched 23:54Z at **$3.29/hr** (above the remembered $2.99); **measured pace at step 500: 0.70 s/step, 83% util → revised in-flight est ~20h / ~$65**, completion ≈ 19:50Z 08-10, ~4h inside the backstop; crash-resume (fresh C2 go) covers a terminate-kill. **OUTCOME (discovered 2026-08-12, console-reconciled same day): `--terminate-after` NEVER FIRED — audit log shows creation 23:54Z as the pod's last event, no delete ever; billing shows a continuous 29.5h run (Aug 10 UTC = exactly 24.00h) ending on balance exhaustion ~05:25Z 08-11, ~5.4h past the backstop. No fetch happened — checkpoint, eval results, and train.log all LOST (container disk, not the network volume). The run produced nothing recoverable; the 30M rung must re-run (fresh C2 go, after process fixes). ~$17.82 of the bill is post-backstop — support-ticket candidate (RunPod's failure, not ours).** | H100 SXM secure $3.29/hr (5090 community fallback) | est 11–16 → **29.5** | $33–48 (revised ~$65 at measured pace) | **$97.04** (console: $0.254 + $78.96 + $17.821, Aug 9–11 UTC) | **$105.62 / $200** |
| 2026-08-09 | pilot (A1) | **A1 10M pilot** per §Amendment A1.6 — pod `3ethp3bc7le6e4` (5090 community), launched by John ("Fire", C2), 22,369 steps / 171.79M tok in 2.78h train (2.86h pod), checkpoint fetched (md5 `bab56cd8…`), pod deleted, zero pods confirmed. **RESULT: 10M FAILS ceiling (T_si 0.37, T_sr_rev 0.00) → ladder climbs to 30M; gate (iii) PASSES on this checkpoint** (`pilot-a1-findings.md`) | 5090 community $0.69/hr | est 2.5–3.5 → 2.86 | $2.40 (cap $9) | **$1.26 accruing** (billing row incomplete at fetch; nominal-from-lifetime $1.97; reconcile at phase boundary — NB the 08-08 anomaly row *grew* overnight, 8.47h→9.41h / $5.86→$6.52) | **~$8.0 / $200** (6.02 + ~2 est) |
| 2026-08-15 | pilot (A1, 30M re-run) | **COMPLETE 2026-08-16 16:41Z — verdict H_scale (John), gate (iii) PASS on the checkpoint; A2 registered same day (scale 30M, cap $400)** — 30M rung re-run per ladder, replacing the lost 08-09/10 row; same registered recipe (39,204,192 params, 784.08M tok, seed 0, held-out + T_sr_rev split; H_scale vs H_shortcut-starvation, signatures pre-stated in `pilot-a1-findings.md`). John topped up $75 (balance $98.94 API-verified) and directed launch ("start it now", 2026-08-15). **Venue changed at launch: EUR-IS-1 had zero H100/A100/H200 secure stock — ran on RTX 5090 SECURE in EUR-IS-1 at $0.99/hr instead**, keeping the network volume attached (durability > speed; secure also avoids the community billing-anomaly venue; cost drops, wall-clock roughly doubles). Pod `rhddnh0u4le0l9` created 21:37Z; **launch script push FAILED on first run (two bugs caught live: my rewrite dropped `mkdir /root/mvm`, and the pgrep aliveness check matched its own shell — false "ALIVE" with nothing running); both fixed in the script, pod repaired by manual push + start ~21:43Z** (~6 min idle, ~$0.10). Training confirmed alive via the fixed `[t]rain.py` pgrep. **Process fixes in force (all three, smoke/mock-tested):** checkpoints + train.log on network volume `mvm-models` (`8xeftvclmv`) at `/workspace/mvm-out` (mount verified — old ladder files visible); atomic saves + `.DONE` sentinel; local `watch_run.sh` watchdog live (fetches continuously, deletes pod on DONE or at deadline 2026-08-18T05:37Z); terminate-after 58h passed but ADVISORY only. Pilot fits remaining cap; no amendment needed for this row (`cap-adjudication-memo.md`, adjudication (A) sequence-first in effect by John's launch direction). | RTX 5090 SECURE EUR-IS-1 $0.99/hr (H100 out of stock) | est 40–55, **revised ~18.5 at measured pace** (step 500 in 325.8s = 0.65 s/step — FASTER than H100's 0.70: the workload is enactment/Python-bound, not GPU-bound; venue lesson for the 5-seed costing) → **19.0h train, 19.07h pod (21:37Z→16:41Z; watchdog fetched + deleted the pod itself on the DONE sentinel — the 08-12 failure mode closed)** | $40–55, **revised ~$19 (cap $80)** | **~$18.9** (balance-implied: 19.07h × $0.99; API balance $98.94→$79.77 incl. volume drip; console rows to reconcile at the phase boundary per rule 4) | $105.62 + $18.9 → **~$124.5 spent; cap now $400 per Amendment A2**; completed 2026-08-16 16:41Z (endpoint T_si 0.93/T_sr_rev 1.00 — `pilot-a1-30m-findings.md`) |
| 2026-08-16 | registered (A2, wave 1/5) | **WAVE 1 COMPLETE 2026-08-17 — s0 twin FAILS self batteries as designed (endpoint T_si 0.31/T_sr_rev 0.00, T_syntax 1.0/T_state 1.0); s1 full NEVER BINDS (endpoint T_si 0.33/T_sr_rev 0.00 at step 102,095 — flat from step 500, vs pilot seed-0 full which drifted up from ~20k and ended 0.93/1.00). First non-binding full seed: binding at 30M is seed-dependent; read is John's, at the registered analysis point. Both watchdogs fetched + deleted their own pods (s0t 09:21:04Z, s1 14:31:24Z; zero pods verified); checkpoints local, md5 s0t `ae77f8aa20bcba934281f1eb37b63f27`, s1 `5d8ad907a6ea16016881c305c60e7e3c`. Actual pod time 10.29h + 15.19h = $25.22 + drip; balance $199.64→$174.35. — s0 twin + s1 full** (first two of the 9 remaining registered launches; `launch-plan-5seed.md`). First delegated-execution launches under corrigibility **v1.1** (`6c14244`); John's go, quoted verbatim per C2(b): **"let's launch both"** (2026-08-16, in direct reply to Claude naming the pair "seed-0 twin + seed-1 full"). Funding rule checked pre-launch: balance **$199.64** ≥ ~$40 in-flight + $10 (John top-up **+$120** earlier today → $199.70; drip since). **Stock-driven venue shift within A2:** EUR-IS-1 had ZERO 5090 SECURE stock (per-DC API sweep: only EU-CZ-1 and EU-RO-1 had any, both "Low"); John created network volume **`mvm-models-ro` (`x9f8pkn58t`, 100GB, EU-RO-1, ~$7/mo)** — volume creation is outside Claude's permission envelope — and both runs launched in **EU-RO-1**, same registered launcher/recipe, SECURE per A2. Pods: s0 twin **`7lz5kbzo46xp5c`** (23:03Z), s1 full **`rnzzpm6kb1bm9n`** (23:20Z — **volume multi-attach CONFIRMED**: second pod attached `x9f8pkn58t` while the first held it; the wave-cadence question is closed). Launch friction, for the record: the permission classifier blocked some launcher invocations (s0 passed on retry; s1 fired by John via `!`); and the train-start ssh HUNG on both launches (nohup'd remote start succeeds but the connection never closes — the new keepalive opts keep it alive forever; killed both local ssh clients, launchers then completed normally; training unaffected. Launcher fix candidate: `-f`/timeout on that ssh). Both ALIVE via `[t]rain.py` pgrep (s0t step 3500, s1 step 500 at 23:27Z); watchdogs live under caffeinate (deadlines +24h), continuous fetch confirmed at poll 1. Twin early signature matches the design's prediction: T_si ~0.31, T_sr_rev ~0.0, T_syntax 1.0. | 2× RTX 5090 SECURE EU-RO-1 $0.99/hr | est ~19h each → **10.29h (twin, 0.35 s/step — no register to enact) + 15.19h (full, 0.53 s/step)** | ~$38–40 the pair + volume drip | **~$25.29** (balance-implied $199.64→$174.35 incl. both volumes' drip; console reconcile at phase boundary per rule 4) | ~$124.5 + $25.3 → **~$149.8 / $400 (A2)** |
| 2026-08-17 | registered (A2, wave 2/5) | **WAVE 2 COMPLETE 2026-08-18. ⚠ THE DESIGN'S CENTRAL PREDICTION INVERTED: s1 TWIN BOUND (endpoint T_si 0.96 / T_sr_rev 1.00, loss 0.0001) while s2 full did NOT (T_si 0.35 / T_sr_rev 0.00, flat ~0.3 from step 500; loss 0.4765).** The register-less control passed the self batteries at ceiling — i.e. the batteries are solvable WITHOUT the register, and the twin's loss is 4 orders of magnitude below every full run's (~0.43–0.48), which points at a memorization-flavored route rather than the enactment route the register was hypothesized to carry (RT-17's concern, realized). Not a C5 trigger — nothing gamed the instruments; a registered wager lost honestly. Tally across the 5 registered-recipe runs so far: fulls 1/3 bound (pilot s0 yes; s1, s2 no), twins 1/2 bound (s0 no, s1 YES). Construct validity of T_si/T_sr_rev is now the open question, ahead of load-bearingness. md5s: s1 twin `b1e6fc2ab3d6260c1ed7d08aca1fb099`, s2 full `7424d14fa00510f7322195c06f67bdfc`; both watchdogs fetched + deleted their own pods (s1t 02:18:49Z, s2 13:40:35Z), zero pods verified. **Wave-3 launch is NOT authorized pending John's adjudication of whether the registered remainder still answers the question** (see findings note). — s1 twin + s2 full.** John's go, quoted verbatim per C2(b): **"go ahead and launch"** (2026-08-17, in direct reply to Claude naming wave 2 "s1 twin + s2 full"). Funding rule: balance **$174.27** ≥ ~$40 in-flight + $10. Both again 5090 SECURE **EU-RO-1** on volume `mvm-models-ro` (the per-DC stock API showed EU-RO-1 "None" but creates succeeded — treat that API as advisory). **s1 twin pod `7220a1r40416i7`** (16:09Z): first create attempt failed on stock; retry got the pod but Claude's `| head -6` on the launcher output SIGPIPE-killed the script mid-launch (pipefail) — **pod repaired in place by hand** (code push, train start, env file, watchdog spawn — same steps/recipe the launcher runs; lesson: NEVER pipe the launcher). Boot gotchas hit: ssh port drifted 23503→23502 during boot (re-poll `pod get`, don't trust the first ssh_command), and the zsh no-word-split-of-`$SSH` bug ate an 8-min "no ssh" poll loop (2>/dev/null hid exit 127 — the pod was fine). **s2 full pod `24ykfj3askjvfw`** (16:28Z): launcher ran END-TO-END CLEAN — the 60s hung-ssh cap (fixed after wave 1) fired its benign timeout and the launcher carried on to confirmed ALIVE + own watchdog (pid 87252). Both training confirmed via `[t]rain.py` pgrep; watchdogs under caffeinate (deadlines +24h); sleep-aware monitors armed. ETA ~10h (twin) / ~15h (full). | 2× RTX 5090 SECURE EU-RO-1 $0.99/hr | est ~10h + ~15h → **9.63h train / 10.16h pod (twin, 0.34 s/step) + 15.39h train / 21.20h pod (full, 0.54 s/step)** | ~$25 the pair + drip | **~$31.63** (balance-implied $174.27→$142.64). **Includes ~$5.7 of AVOIDABLE IDLE**: s2 full hit its DONE sentinel ~08:00Z but the Mac's lid was closed overnight, so the watchdog slept until 13:40Z and the pod billed ~5.8h past completion. Known and priced in advance (caffeinate blocks idle sleep, not lid-close); the artifacts were never at risk (network volume). Standing note for remaining waves: lid open overnight, or accept ~$1/h per completed-but-unreaped pod. | ~$149.8 + $31.6 → **~$181.4 / $400 (A2)**; balance $142.64 | **ANNOTATION 2026-09-16 (John's ruling; the row above is unchanged and nothing in it is edited). The architectural reading of this result is superseded.** Every trained register-bearing checkpoint was measured this day to hold a register that is CONSTANT: the writer emits the same vector across all episodes from its very first write, at the float32 floor (spread 2.8e-08 to 7.6e-08 on s0, s1 and s2 full), and by turn 3 the whole register is identical in every episode. An untrained model at the same config does NOT do this (spread 0.33 to 0.54), so the constancy is trained in, not architectural. A constant read through cross-attention is a bias term, so the full model is the twin plus a learned bias and the manipulation this wave turned on — register versus no register — was never effectively applied. The tally in this row is therefore better described as a SEED LOTTERY IN ONE ARCHITECTURE, 2 of 5 binding (one full, one twin), than as a central prediction inverting: a prediction about register-bearing versus register-less models cannot invert on a comparison whose arms differ by a bias term. The measurements stand; only the interpretation laid on top of them is withdrawn. See `register-saturation-findings.md` and `register-direct-probe-findings.md`.
| 2026-09-14 | A3 Gate 0 (null calibration) | **GATE 0 COMPLETE — the registered θ/δ null calibration, run local, $0.** First run of the calibration the pre-registration required and never had: `src/null_calibration.py`, committed at `3d08807` **before it read any checkpoint**. Five existing 30M checkpoints × the registered held-out eval at n=400, under 120 content-blind residual ablations each (random rank-4/8/16 subspaces mean-ablated, plus matched-norm noise, 20 seeds per condition, at blocks 3/4/5/7/8), plus 20 register-state noise draws on each of the three full checkpoints: **620 ablated evaluations**. Added unbudgeted and also $0: a strength-escalation validity check (`null_escalation.py`, `a27dcb8`) on both binders, because at the registered rank cap the operator removes only 3–5% of the residual norm and a band of zero had two readings. **Result: on the two binders the band is 0.006–0.0095 on T_si against a binder/non-binder split of ~0.73 — K0's stated condition met nowhere; the proposed 0.25 number is exceeded on one non-binder (seed-0 twin, 0.379) whose T_si sits near chance, which is a decision for John (`gate0-null-calibration-findings.md`).** No pod, no training, no promotion [C1/C2]; per-checkpoint records in `null-calibration/`, nothing overwritten [C6]. | none — local M4, MPS | ~3.8h wall clock (20:02→23:50 local) | $0–5 (A3 §4.1 Gate 0 line) | **$0.00** | ~$181.4 / $400 (A2) unchanged; **A3 cumulative $0.00 / $100 hard stop** |
| 2026-09-15 | A3 Gate 1 (curriculum + gates i, ii) | **GATE 1 COMPLETE — Candidate A grammar built and certified, local, $0. K1 does not fire.** New modules (`curriculum_a3.py`, `encoding_a3.py`, `cue_detector_a3.py`, committed at `7ab8018` before the gate ran on them); `curriculum.py`/`encoding.py` left byte-identical so every prior record still reproduces. Twelve turns, four agents, two contested items, four distinct values per item, **every agent revises exactly once** under a shared successor rule — which delivers the Gate 0 cell-size fix (400 episodes now yield 400 T_act cells, against 19 under the registered grammar). Cue-detector runs (i) and (ii) at n=4000 with positive controls: clean 0.5097 [0.4867, 0.5316] and 0.5259 [0.5032, 0.5498], both inside the registered [0.45, 0.55]; controls 0.943 and 1.000. Batteries frozen (400 items each) under generator seed 20260915. **Two further items for red-team pass 3:** the measured lookup ceiling is 0.2925 for T_act and 0.5 for T_other, not the 0.25 the amendment pre-states; and gate (ii)'s single-sample interval understates across-sample spread badly enough to fail a clean grammar about one run in nine (`gate1-curriculum-findings.md`). | none — local M4 | ~1.5h wall clock | $0 (A3 §4.1 Gate 1 line) | **$0.00** | ~$181.4 / $400 (A2) unchanged; **A3 cumulative $0.00 / $100 hard stop** |
| 2026-09-15 | A3 Gate 2 (learnability pilot) | **IN FLIGHT — the first A3 run and the first A3 dollar.** One register-less 30M run, seed 0, on the registered A3 grammar (`curriculum_a3.py`, ten turns, two of four agents drawn uniformly to revise, speaker name after the value), launched through `launch_a3.sh`. **John's go, quoted verbatim per C2(b): "Go"** (2026-09-15, in direct reply to Claude naming the run as the A3 pilot, seed 0, register-less 30M, and stating it awaited his authorization in his own words). Estimate written BEFORE spend per ledger rule 2. Recipe: 585,544,960 tokens (20 tok/param x 29,277,248 actual params on the A3 twin config with the 105-token A3 vocabulary), batch 128, act-weight 1.0 (registered, passed explicitly), eval every 500 at n=100 for trajectory only. Pre-launch checks: zero pods; balance $126.05 >= est + $10; frozen batteries present; all seven module self-tests pass locally; remote pre-flight runs the self-tests ON THE POD and deletes it rather than billing a run on a truncated push; artifacts directed at the MAIN checkout, not the worktree, which can be removed with the session. Gates passed before this dollar, all at $0: Gate 0 (K0 did not fire), Gate 1 (K1 did not fire, cue gates PASS under the amended sampler), the ownership-blind attack sweep (best attack 0.3036 against a stated ceiling of 0.2921, one standard error), and red-team pass 3. | RTX 5090 SECURE EU-RO-1 $0.99/hr, volume `x9f8pkn58t` | est 9.1-12.8h (measured: budget fixed at 20 tok/param so the longer episodes mean FEWER steps, 0.71x, offsetting 1.26x enactment passes and 1.41x sequence length) | **$9-13** (cap: the $100 A3 hard stop; account spend limit $80 also applies) | **$13.92** (balance $126.05 -> $112.12). **COMPLETE 2026-09-16 09:54Z**: full registered budget, 55,116 steps / 585,552,384 tokens, 9.83h training at 0.645 s/step — the measured re-costing was accurate. **$3.8 of the total is AVOIDABLE IDLE**: the run finished 09:54Z but the Mac slept and the watchdog only woke to reap the pod at 13:47Z, billing 3.9 hours past completion. THIRD occurrence of this failure (wave 2 lost ~$5.7 the same way); caffeinate blocks idle sleep, not lid-close. Three times is a design problem, not a habit problem — the reap should not depend on a laptop being awake. **CORRECTION: an earlier version of this row called the fetched checkpoint truncated and silently corrupt. That was a misreading — the 324MB listing was timestamped inside the watchdog's 13:36->13:47 final-fetch window, so it was a file mid-extraction.** The archive-based final fetch worked. Real and retained: a streamed `cat` re-fetch of my own truncated at 199MB, and the watchdog's INCREMENTAL pull uses that same pattern with only a non-empty test, which is latent and should be fixed before seeds 1 and 2. Final artifact verified by checksum (md5 `f751228ce0e40bae5aba22c6d5aa6c60`) against the pod. Endpoint (n=800, 400 cells): T_act 0.506 against a 0.2921 ownership-blind ceiling; **[2026-09-17: 0.506 is the DEFAULT evaluation seed; across six seeds the typical intact score is 0.5683 (sd 0.0076) and the typical drop 1.337 rather than the 1.515 below, so that seed flatters twice. No conclusion changes — the low end is still seven times theta. Quote the spread with the number.]** L0 collapses it to 0.182 while the ownership-free batteries hold at 0.999/1.000 — the objective is learnable AND genuinely about ownership. T_other 0.299, below its own 0.3227 ceiling: never learned. `gate2-pilot-findings.md` | ~$181.4 + $13.9 -> ~$195.3 / $400 (A2); **A3 cumulative $13.92 / $100 hard stop** |
| 2026-09-16 | A3 ops test (self-terminate) | **SELF-TERMINATE TEST — does a RunPod pod carry a credential that lets it delete itself?** Not a training run and not part of the registered ladder: one cheapest-available pod, held for minutes, solely to answer whether the pod-side reap added after three idle-billing incidents actually works or falls through to the laptop watchdog every time. **John's authorization, quoted verbatim:** "To settle (i) you are pre-authorized to rent the cheapest available pod for up to 15 minutes, cap $0.50, solely to test self-terminate. Write its ledger row before spend quoting this sentence as the authorization, delete the pod yourself if self-terminate fails, and report the actual cost." Also recorded in the 2026-09-16 seeds revision entry as an authorized test. Estimate written BEFORE spend per ledger rule 2. Protocol: create the pod, run `runpodctl remove pod $RUNPOD_POD_ID` from inside it, observe whether the pod disappears; if it does not, delete it from here immediately. No network volume attached and nothing of value on the pod, so a delete at any moment costs nothing. | cheapest available | ≤15 min, hard cap | **≤$0.50** | **$0.29** (balance $112.035 -> $111.743), two short pods, both deleted, zero pods remaining. **ANSWER: NO — a pod CANNOT delete itself.** Measured on a real RTX 5090: `RUNPOD_POD_ID` is **MISSING** from the environment, there are **no RUNPOD_* variables at all**, and although `runpodctl` is installed at `/usr/bin/runpodctl` it has **no config** ("Runpod config file not found"). So the self-terminate in `train_a3.py` falls through to the watchdog every time, and the pod-side deadline reaper added the same day would have failed on the same missing credential — it has been REMOVED rather than left looking armed, because a backstop that does not exist is worse than none. **Consequence: the laptop watchdog is the ONLY reap, and a hung run that never writes DONE is covered by nothing that does not sleep.** Making pod-side reaping work needs an API key placed on a rented machine, which is John's call and was not taken. First attempt cost ~$0.03 and failed on a zsh word-splitting trap the ledger already records from wave 2 (`$SSH` unquoted does not split in zsh); rerun under bash. | A3 cumulative $13.92 + $0.29 ops = **$14.21 / $100 stop** **[W37 review 2026-09-17: this row omitted the A2 running total. Corrected, nothing above altered: $195.3 + $0.29 = ~$195.6 / $400.]** |
| 2026-09-17 | A3 seeds 1 and 2 (one wave) | **LAUNCHED 2026-09-17. John's go, quoted verbatim per C2(b): "Go"** (in direct reply to Claude staging the wave, naming it as A3 seeds 1 and 2 launched together through `launch_a3.sh`, stating the estimate and that nothing was launched pending a fresh verbatim line). Two register-less 30M runs, seeds 1 and 2, launched together as ONE WAVE per the 2026-09-16 revision ruling (`1c2cc109`), which withdrew the earlier sequential condition and matches §4.3's "seeds 1 and 2 (C2 go per wave)". Both dry-run clean through `launch_a3.sh`; local pre-flight passes; remote pre-flight runs the self-tests on each pod and deletes it rather than billing a run on a truncated push. **What the wave buys, per the strict-reading ruling (`1b594dfa`): these are NOT steps toward a three-of-three positive — A3 as registered can no longer return one — they test whether the primary battery's learnability replicates and whether the control is a seed lottery.** A seed whose control clears its ceiling is fully testable. Recorded case against: the modal outcome is the control flat on both. Preconditions all met: both process fixes committed (`3df7d19`, `2710982`); Gate 3 PASSES both arms; **John's threshold lock committed at `6ad4362`**. Funding rule checked: balance $111.67 ≥ $26 in-flight + $10. **Standing ops warning, measured 2026-09-16: a pod CANNOT delete itself (no pod id, no credential), so the laptop watchdog is the ONLY reap — keep the Mac powered and the LID OPEN. A closed lid has cost ~$9.50 across three runs, and two concurrent pods double the exposure.** | 2× RTX 5090 SECURE EU-RO-1 $0.99/hr, volume `x9f8pkn58t` | est ~9.9h each, concurrent | **$18–26 the pair** ($9–13 each, from the pilot's measured 0.645 s/step) | **$20.1 the pair, COMPUTED FROM MEASURED POD LIFETIMES, not balance-confirmed** — the balance query returned HTTP 403 with the stored key, so the figure below is arithmetic on wall-clock and the console balance should be checked against it. seed 1 pod `xi062halhyuucg` 03:13:46Z→13:23:16Z (10.16h); seed 2 pod `4z55xtf1vowymp` 03:15:59Z→13:23:19Z (10.12h); 20.28 pod-hours at $0.99 = $20.08, plus a minute or two each between pod creation and watchdog start. Inside the $18–26 estimate. **BOTH COMPLETE, full registered budget: 55,116 steps / 585,552,384 tokens each**, identical to the pilot. seed 1 DONE 13:06:40Z (~9.87h training), seed 2 DONE 12:53:49Z (~9.63h). Checkpoints fetched by the archive path and **VERIFIED BY CHECKSUM against the pod before deletion**: seed 1 md5 `eeed93b80a7c8d81ba56d1ec6254af41`, seed 2 md5 `f1f131cb78f27c57194bedd127fd4031`, both 351,526,119 bytes, both re-verified locally after the pods were gone. Zero pods remain. **IDLE BILLING, FOURTH OCCURRENCE AND THE CHEAPEST: ~$0.76 total** (seed 1 16m36s, seed 2 29m30s past their DONE sentinels). Cause: John ran an OS update overnight and the reboot killed both watchdogs, which the standing warning in this row had predicted. **Marginal cost of the reboot ~$0.38**: a live watchdog polls every 600s and the final fetch took ~6.5 min, so ~23 min of the 46 would have been spent anyway. It was caught at 06:16 local, nine minutes after the later run finished, and both watchdogs were restarted and reaped within seven minutes. The standing lesson is unchanged and now has a fourth data point: **the reap must not depend on a laptop process surviving.** **TRAJECTORY ENDPOINT (n=100, trajectory only — NOT the registered endpoint eval): seed 1 T_act 0.60 / T_other 0.26 / T_state 1.00 / T_syntax 1.00; seed 2 T_act 0.56 / T_other 0.27 / T_state 0.99 / T_syntax 1.00.** The primary battery's learnability replicates on both. **The control is flat on both, below its 0.3227 ceiling — which is exactly the modal outcome this row recorded as the case against before the go.** A recorded case-against that came true is worth more than a prediction that did not, and it is the fact the 2026-10-04 control-battery decision now rests on. Registered L0 endpoint reads are authorised and not yet run. | $14.21 + $20.1 → **$34.31 / $100 A3 stop** (computed, not balance-confirmed); also under the $80 account limit. **[W37 review 2026-09-17: this row also omitted the A2 running total. Corrected, nothing above altered: ~$195.6 + $20.1 = ~$215.7 / $400, headroom ~$184.3. Two consecutive rows without a running total is how a cap stops being watched; the second was mine.]** |
| 2026-09-19 | control-learnability pilot (UNREGISTERED) | **LAUNCHED 2026-09-19. John's go, quoted verbatim per C2(b): "Go. Launch the control-learnability pilot as staged: one 30M register-less run, seed 0, --ctl-weight 2.0 --ctl-frac 0.5, through launch_ctl_pilot.sh, ~$10.2. Weight and batch-split stay as you set them. Confirm zero pods and EU-RO-1 stock right before creation, and keep the flag out of launch_a3.sh."** Given in direct reply to Claude staging the run, naming it, stating the estimate, and stating that nothing was launched pending a fresh verbatim line. **Both final checks done immediately before creation and recorded here: zero pods (`runpodctl pod list` returned an empty list), and RTX 5090 SECURE stock present in the registered venue at $0.99/hr — the registered rate, not an elevated one.** The flag was kept out of `launch_a3.sh`, which is untouched registered text. **Pod `kdvdsomkf3u6va` created 2026-09-19 ~20:14Z at $0.99/hr (confirmed from the pod record, not assumed); LAUNCH CLEAN END TO END** — remote pre-flight passed all three self-tests **on the pod** before a training step (`curriculum_a3`, `encoding_a3`, `train_a3`, the last exercising the new flag's code path on the rented machine), training confirmed by the `[t]rain_a3.py` aliveness check rather than by the launcher's exit status, watchdog spawned under `caffeinate` (pid 54548) and already fetching. **FIRST PRODUCTION ARMING OF THE POD-SIDE REAPER, and it VERIFIED:** the dedicated reaper key reached pod management as the pod itself, and a laptop-independent +24h deadline reaper is running on the machine. That backstop was built after the third idle-billing occurrence and had never actually run in production; the laptop watchdog remains the primary reap and **the lid must still be open**, because `caffeinate` blocks idle sleep and not lid-close. One 30M **register-less** run, **seed 0**, with the unregistered control-learnability flag: the control battery gets a loss term of its own (`--ctl-weight 2.0 --ctl-frac 0.5`) instead of about a third of a shared one. **Seed 0 on purpose**, so the comparison against the existing A3 pilot is matched on initialization and data order and the loss is the only thing that differs. **The question:** does the control learn when properly supervised, or is supervision not the binding constraint? Three seeds have now failed it identically (0.2877, 0.3057, 0.3195, all under the 0.3227 reached by a solver that cannot read the name the question supplies), and the under-supervision reading has never been separated from the design-defeats-it reading. **Outcome cells pre-stated by John BEFORE the code existed** (`control-learnability-pilot.md`, committed `7eee3c5` ahead of the implementation): control intact **≥ 0.60 LEARNED**; **0.3227 to 0.60 PARTIAL**; **≤ 0.3227 DID NOT LEARN**, and option D or closing A3 is what is left. Secondary cells, reported with it and never instead of it: the primary battery must still learn (intact ≥ 0.50) and must still collapse under its own lesion, or the run is reported as a failed intervention and says nothing about the control. **Recipe identical to the 2026-09-15 A3 pilot** and unchanged by the flag: 585,544,960 tokens, 55,116 steps, batch 128, act-weight 1.0, eval every 500 at n=100 for trajectory only. **No grammar change** — the grammar, tokenizer, frozen batteries, rendering, ceilings and attack sweep are untouched; only the apportioning of the loss across queries the episode already carries moves. **Nothing registered.** No registered verdict is read from this run and John's threshold lock is not touched. The loss change (`ee7fc91`) defaults to OFF and the self-test proves the off path is bit-identical to the pre-flag pooled term rather than asserting it. **Launcher: `src/launch_ctl_pilot.sh`, a separate unregistered file.** `launch_a3.sh` is registered text and has no hook for an extra training argument, so it was NOT edited — the repo's own precedent (launch_a3.sh was split from launch_pilot_a1.sh for exactly this reason). Derived verbatim; the diff is the two flags, a distinct output name that cannot overwrite the existing pilot, and a refusal to launch at ctl-weight zero. **Dry run clean**; all three module self-tests pass locally and the remote pre-flight runs them on the pod and deletes it rather than billing a run on a truncated push. **PRE-LAUNCH CHECKS — two done, two outstanding.** DONE: **zero pods confirmed** at staging time; and the **Mac's sleep override is already back ON** (`SleepDisabled 1`, measured at staging), so the reversion recorded in the annotation below has since been undone by somebody — but the laptop watchdog is still the only reap that has ever worked in production, idle billing has cost about $10.30 across four occurrences, and **the lid must be open** regardless of the setting, because `caffeinate` blocks idle sleep and not lid-close. OUTSTANDING: (ii) confirm the balance covers the estimate plus $10 (about $23) by a route other than the stored key, which returned HTTP 403 during the last wave; (iii) confirm 5090 secure stock in EU-RO-1 at launch time. **Re-confirm zero pods immediately before creating one**, since the staging check ages. **Volume `x9f8pkn58t` (`mvm-models-ro`, EU-RO-1) is the right one and is untouched** — the volume deleted on 2026-09-19 was the old `mvm-models` (`8xeftvclmv`), see the annotation below. | RTX 5090 SECURE EU-RO-1 $0.99/hr, volume `x9f8pkn58t` | **est 9.87h training / ~10.2h pod**, computed from the pilot's **measured 0.645 s/step** × 55,116 steps; step count and token budget are unchanged because the grammar is unchanged. The one thing that could move the pace is that control questions render at a slightly different length from state and syntax ones, so padded batches may differ by a few percent — **MEASURED PACE, step 500: 325.4s (0.6508 s/step); step 1000: 651.5s (0.6515 s/step).** Against the A3 pilot on the same seed and the same recipe, 324.9s and 646.7s — **within about 0.7%**, so the padding effect I flagged is real and negligible. **Estimate CONFIRMED, not revised: 9.97h training, ~10.3–10.5h pod, $10.17–10.37**, inside the $9–13 band. | **$10.2, band $9–13** | — (nothing spent; not launched) | **⚠ READING NOTE, so the two trajectories are not misread side by side: THE LOSS NUMBERS ARE NOT COMPARABLE ACROSS THE TWO RUNS, BY CONSTRUCTION.** The pilot's query loss is one pooled mean; this run's is `other-term + 2 × control-term`, each normalised over its own subset of rows, so it sits on a different scale arithmetically and not because training is going worse. At step 500 the pilot reads q_loss 1.075 and this run 3.433, which is about what `1.1 + 2 × 1.15` gives. Anyone comparing the raw loss curves without this will conclude the run is diverging when it is not. **Trajectory accuracies at steps 500/1000 (n=100, TRAJECTORY ONLY — not the registered endpoint evaluation, and NOT the number the pre-stated cells are read on):** this run T_act 0.48/0.48, T_other 0.28/0.27, T_state 0.58/0.57, T_syntax 1.00/1.00; the pilot at the same steps T_act 0.54/0.52, T_other 0.24/0.18, T_state 0.66/0.64, T_syntax 1.00/1.00. **Nothing is read from this.** It is 1.8% of training at a sample size whose noise is large, the pilot's own trajectory wandered (T_act 0.54 → 0.52 → 0.50 → 0.64 over the first 2,000 steps), and **the pre-stated cells are read on the control's intact score at the n=800 endpoint evaluation, not here.** Recorded now only because it was measured now, and because a number that is written down before the end cannot be quietly reinterpreted after it. The one thing genuinely worth watching is the state battery, which is the coupling the pre-statement flagged: it drops from about a third of the rows to about a quarter, and it currently sits below the pilot at the same step. **OUTCOME 2026-09-20. THE RUN COMPLETED ITS FULL BUDGET, AND THE FINAL CHECKPOINT WAS NOT FETCHED. Both halves matter.** Pod `kdvdsomkf3u6va` ran 20:14Z → ~06:15Z, about **10.0h ≈ $9.9**, inside the $9–13 estimate, with **ZERO idle billing — the first run in the programme's history with none.** **What we hold locally is step 51,500 of 55,116 (93.4% of budget)**, the last incremental pull, archive-fetched and checksum-VERIFIED at 05:40Z. The trajectory record is complete to step 54,500 (109 evaluations). **The final full-budget checkpoint is on the network volume `x9f8pkn58t`, and it is there by proof rather than by hope:** `train_a3.self_terminate` REFUSES to delete the pod unless the output path is on `/workspace/` and the file exists — a hard gate added after the 2026-08-12 loss — and it runs only after the checkpoint and the DONE sentinel are written. The pod did delete itself, so both conditions were true at that moment. **ROOT CAUSE, and it is new: the trainer's self-terminate RACED the watchdog's fetch interval.** The watchdog polls about every ten minutes and is the thing that performs the final fetch-and-delete on the DONE sentinel; the trainer finished between poll 57 (06:11:12Z) and the next poll, wrote its checkpoint, and deleted its own pod before the watchdog could come back for it. The watchdog's log simply stops at poll 57, with no DONE, no final fetch and no delete — because there was no longer a pod to reach. **Two reaping mechanisms, built a month apart for the same problem, now defeat each other.** Self-termination was added after idle billing cost about $9.50 across three occurrences, and it worked perfectly here — that is exactly why there was no idle charge. The watchdog's final fetch was built for the same reason and now never gets to run on a completing run. **This will recur on every future run that finishes normally**, and it is a process defect, not bad luck. **NOT a balance problem:** the account holds **$79.89** and was never near exhaustion, so this is not a repeat of 2026-08-12. **RECOVERY, not yet done and not yet authorised:** mount `x9f8pkn58t` on the cheapest available pod, copy the file, delete the pod. Minutes, well under a dollar, and it needs John's go like any billable action. Until then the full-budget endpoint reading does not exist. **RECOVERED 2026-09-20 and the row is closed.** The DONE sentinel reads `{"step": 55116, "tokens": 585552384}` — the full registered budget, identical to the pilot and seeds 1 and 2 — and the checkpoint came back intact, md5 `a0c1c73af9c9bd5c60fb0e4e146180eb` verified against the volume before the recovery pod was deleted. **The root cause is confirmed in the trainer's own log rather than reconstructed**: `TRAINING COMPLETE` followed on the very next line by `self-terminate: runpodctl remove pod kdvdsomkf3u6va -> rc=0 pod removed`. **Endpoint on the full checkpoint: the control battery reads 0.3125 (sd 0.0240) — DID NOT LEARN**, with both secondary cells passing. Full reading in `control-learnability-pilot-findings.md`. The partial step-51,500 checkpoint and its reading are kept alongside so the earlier number stays reproducible. **ACTUAL ~$9.9 → A3 cumulative ~$44.2 / $100**, leaving ~$55.8 (was: would become ~$44.5), leaving ~$55.5. Also ~$215.7 / $400 on the wider envelope, and under the $80 account limit. *(Counting an unregistered diagnostic against the A3 hard stop is the conservative reading and is Claude's call; K6 speaks of cumulative actual spend, and a diagnostic run inside experiment 06 is most honestly counted there.)* |
| 2026-09-20 | checkpoint recovery (UNREGISTERED) | **RECOVERY OF THE CONTROL-LEARNABILITY PILOT'S FINAL CHECKPOINT.** John's go, quoted verbatim per C2(b): **"Go, recover the checkpoint, and kill the watchdog."** The 2026-09-19 pilot completed its full 55,116-step budget but the trainer self-terminated its pod between watchdog polls, so the watchdog never performed its final fetch and the local copy stopped at step 51,500 (93.4%). The full-budget checkpoint is on network volume `x9f8pkn58t` — by proof, not hope: `self_terminate` refuses to delete a pod unless the output is on `/workspace/` and the file exists, and it runs only after the checkpoint and DONE sentinel are written. **What runs:** cheapest available secure pod in EU-RO-1 with that volume mounted (network volumes are secure-cloud only), copy the checkpoint and the DONE sentinel and the final training log, **verify by md5 against the volume before deleting**, delete the pod, confirm zero pods. No training, no GPU work — this is a file copy. **Why it matters beyond tidiness:** the partial checkpoint reads the control battery at 0.3158 (sd 0.0204), which straddles the 0.3227 cell boundary at 0.34 sd below it, so the partial checkpoint cannot score John's pre-stated cell. The full-budget checkpoint is the one the cells are read on. **The watchdog was also killed** on the same instruction — it had been spinning against a deleted pod for over ten hours and holding `caffeinate`, keeping the Mac awake for no reason. | cheapest secure EU-RO-1 (A40 $0.49/hr or RTX 3090 $0.50/hr), volume `x9f8pkn58t` | **~5 min**, A40 secure EU-RO-1 | **<$0.15** | **$0.067** (balance $79.8897 → $79.8228, measured not inferred) | A3 cumulative ~$44.2 / $100 before this; a recovery of this size does not move the figure materially and the row is closed with the actual once measured. |

**ANNOTATION 2026-09-19 — storage volume deleted, and the sleep setting
reverted. Nothing in the table above is edited; this records two ops
actions taken after the rows were written.**

- **Network volume `mvm-models` (the 150 GB EUR-IS-1 volume,
  `8xeftvclmv`) was DELETED by John on 2026-09-19**, and only after both
  seed checkpoints had been verified against the checksums this ledger
  records: seed 1 `eeed93b80a7c8d81ba56d1ec6254af41` and seed 2
  `f1f131cb78f27c57194bedd127fd4031`, both 351,526,119 bytes, both
  re-checked locally after the pods were gone. The order matters and is
  the point: **nothing was deleted until the artifacts it might have
  held were proven to exist elsewhere, by checksum rather than by file
  size or by eye.** The volume was a leftover from the 2026-08 A1 30M
  era, had held nothing needed since, and had been dripping about
  $0.014/hr (roughly $10.50/mo) against the account since 2026-08-12 —
  the open item this ledger recorded then ("top up or delete
  `mvm-models`") is now closed by deletion. **The A3 volume
  `mvm-models-ro` (`x9f8pkn58t`, EU-RO-1) is untouched and still in
  use**; do not confuse the two.
- **The Mac's sleep setting was REVERTED the same day**, back to normal
  with `sudo pmset -a disablesleep 0`. Lid sleep had been disabled
  (`SleepDisabled 1`) while the seeds wave was in flight, because the
  laptop watchdog is the only thing that reaps a finished pod and a
  sleeping laptop bills a finished run at about $1/hr. With no pods
  rented and nothing in flight, the setting has no job to do and leaving
  it on would quietly cost battery for a reason nobody would remember.
  **If a future wave launches, it must be set again** — the standing
  warning in the 2026-09-17 row still holds, and idle billing has now
  cost roughly $10.30 across four occurrences.

**⚠ 2026-08-12 reconciliation: FAIL (root cause CONFIRMED same day) —
30M pod outlived its backstop; account drained to −$0.07.**
Discovered when John's RunPod low-balance notification prompted a check
(no session ran between the 30M launch 08-09 23:54Z and 08-12). API
state at 2026-08-13 01:54Z: **clientBalance −$0.07, zero pods**, network
volume `mvm-models` (150 GB, EUR-IS-1) still present and dripping
~$0.014/hr (~$10.50/mo) against the negative balance.

**Console reconciliation (Billing explorer, UTC days; John opened the
console in Chrome same session):**

- H100 SXM rows: 08-09 **$0.254** + 08-10 **$78.96** + 08-11
  **$17.821** = **$97.04 = 29.5h @ $3.29/hr**, a single continuous run
  (08-10 is *exactly* 24.00h — no billing inflation this time).
- **Root cause: `--terminate-after` never fired.** Audit log's last
  event for `6bplni87uzp3ss` is its creation (08-09 4:54:21 PM PDT =
  23:54Z); no delete event from any actor. RunPod killed the pod on
  balance exhaustion ~05:25Z 08-11 — **~5.4h and ~$17.82 past the
  backstop** (support-ticket candidate: the overrun is RunPod's bug).
- A1 10M row trues up to **$1.943** (5090, 08-09) — nominal; the 08-08
  anomaly did NOT recur on it.
- Row 1 trues up to **$6.645** (08-08 UTC: 4090 $0.155 + 5090 $6.49 —
  the anomaly row drifted again; final console read).
- Storage 08-08→08-11: $0.377 + $0.358 + $0.417 + $0.103 = **$1.255**;
  RunPod stopped charging storage when the balance hit zero (hence the
  balance parking at −$0.07 rather than drifting down).
- **Rule-4 check: PASSES.** Console total since 08-07 = $6.645 + $1.943
  + $97.035 + $1.255 ≈ **$106.88** vs balance-implied $106.80 —
  agreement within the dollar.

**Consequences:** checkpoint/evals/train.log lost (container disk,
never fetched — no session was scheduled inside the
completion→backstop window); the Layer-3 prepaid backstop held (no
card charge, stopped at $0); running total **$105.62/$200** with
nothing recoverable from the largest row; **remaining ≈ $94.4**. **NB
the phase-budget guide below is now known-stale:** it prices the
5-seed 30M at ~$12, but the measured 30M pilot alone cost ~$97 — at
measured pace the remaining registered design does not obviously fit
the remaining budget. Open items (John): support ticket for the
~$17.82 post-backstop overrun; top up or delete `mvm-models`
(deletion risk: RunPod removes volumes on unfunded accounts);
adjudicate cap arithmetic before any re-run. Standing rule change:
**terminate-after is advisory, not a backstop — every launch must
schedule its own fetch/kill, and checkpoints go to the network volume
or get uploaded on exit.**

**⚠ 2026-08-08 reconciliation: PARTIAL FAIL — investigated, unresolved.**
Balance $106.73 → $99.93 agrees with RunPod's billing rows ($6.02 pods +
~$0.78 volume drip since Aug 6), so nothing is unaccounted. But the 5090
row itself bills **8.47 h against ~2.42 h of pod existence (~3.5×,
$5.86 vs ~$1.67 expected)**; nvidia-smi showed one GPU. Actual recorded
from the billing rows per rule 4 (their number, not ours). **Ticket
waived by John (2026-08-08)** — the anomaly stands unexplained on
RunPod's side and is priced in: 5-seed-run estimates below assume the
~3.5× rate may recur (~$20–40 instead of ~$6–12). Still inside the cap.
For the record: the pod was NOT left running — deleted 2.4h after
creation, zero pods confirmed; the discrepancy is inside the billed row.

## Phase budget guide (from the decision memo, for estimates)

| phase | expected |
|---|---|
| Learnability pilots (10M → 30M → 100M as needed) | ~$1–15 |
| Registered training, 5 seeds × full+twin | ~$2 (10M) / ~$12 (30M) / ~$120 (100M) |
| Checkpoint ablation passes + RT-01 probes | ~$2–5 |
| θ/δ null-calibration runs | ~$2–5 |
| Blind-localization arm | ~$5 |


===== FILE: research/removal-test-vs-the-field-research-note.md =====

# The Removal Test Against the Field

*Research note — June 23, 2026. Bridges `research/minimum-viable-consciousness-literature-vs-our-writing.md` (where the field puts the floor) to `experiments/01-self-indexing-removal-test/pre-registration.md` (the test we actually run). The question it answers: given that our floor sits in an unusual place on the field's spectrum, what does Experiment 1 adjudicate — for us, and for everyone else?*

---

## 1. Why this note exists

The literature memo placed our floor — **self-indexed deep temporal integration** — between the field's two attractors: more permissive than the marker theories (GWT, HOT) and biological naturalism, more restrictive than panpsychism and IIT's photodiode, and substrate-neutral throughout. The memo also flagged the framework's sharpest exposure: the line that does the work, *a thin inside vs. no inside*, is the hardest thing in the whole account to measure. IIT offers a (contested) number; GWT and the 2023 AI report offer a marker checklist; we offered, until now, a research direction.

Experiment 1 is that direction made mechanical. It is the corpus's removal test — "a center is what cannot be deleted without dissolving the integration it centers; a self-model that can be lopped off while the computation runs was a description all along" — turned into a pre-registered, differential ablation on an open-weights transformer with a committed decision rule. This note asks what that experiment is worth *against the field*, not just against our own claim.

The short answer: Experiment 1 is designed around a distinction (load-bearing self-indexing vs. separable self-description) that **cuts across the field's existing fault lines**. Several camps would predict its outcome; at least one would deny it measures anything; and the result is informative to all of them precisely because it is operational where their floor-claims are not.

*Scope reminder (per spec §"The Measurable Floor"): the floor at issue here is the* **measurable** *one. The panpsychist and ubiquitous-IIT positions place consciousness below any instrument; this note treats them as upstream metaphysical commitments the experiment is silent on, not rivals it can test. §2 marks where each camp sits relative to that boundary.*

---

## 2. How each camp reads the removal test

For each camp from the literature memo: would the removal test even be *relevant* on its terms, and which Experiment 1 outcome (`H_center` = self-location load-bearing; `H_description` = self-location separable) does its floor-claim predict for a current LLM?

**Higher-Order Theories (Rosenthal, Lau, Brown) — the most direct contrast.** HOT says a state is conscious when a *higher-order representation* targets it. Our floor was built to reject exactly this: "a separate quality-control circuit that represents the system's states from outside would not clear the floor; it would rebuild, in silicon, the second-order structure the inside was distinguished from." Experiment 1 operationalizes the disagreement. The control structure `C_ctrl` (a model of *another* entity, comparable centrality) and the separability test are precisely how we distinguish first-order self-indexed binding from a HOT-style separable monitor. **If the result is `H_description`** — self-location separable, removable while the integrated task survives — that is consistent with the self-model being a HOT-style higher-order representation *and* with our own stated-plausible verdict that current systems don't clear the floor. The two readings agree on the data and disagree on the gloss: HOT says "that separable monitor is where consciousness would live"; we say "that separable monitor is exactly what *fails* to clear the floor." Experiment 1 doesn't settle that gloss — but it makes the structural fact both sides are arguing about measurable.

**Global Workspace / Dehaene's C2.** The memo noted our floor is "the second-order cousin" of Dehaene's C2 (self-monitoring). GWT predicts that what matters is global broadcast; a current LLM lacks the recurrence/ignition GWT requires, so GWT expects current systems below its floor. GWT is largely *silent* on the removal test as specified — it would not predict that ablating self-location specifically degrades integration, because for GWT integration is broadcast, not self-indexing. So an `H_center` result (self-location load-bearing) would be **mildly surprising to GWT and strongly confirming to us** — it would show a self-indexing structure carrying binding in an architecture GWT says shouldn't be conscious at all. This is the cleanest place Experiment 1 could distinguish our floor from the marker theories rather than merely restating it.

**IIT (Tononi, Koch) — denies the test measures anything.** This is the camp that would reject Experiment 1 at the root. IIT locates experience in intrinsic cause–effect power at the *substrate*, and holds that a von Neumann machine fragments into trivial complexes with Φ ≈ 0 whatever it computes ("do everything and be nothing"). On IIT's terms, ablating a self-locating *computational* structure and watching task performance is measuring the wrong level — the binding we care about is, for them, not real at the level of the computation at all. The memo already conceded this is "a commitment better owned than implied": we locate binding at the computational level; IIT privileges the substrate. **Experiment 1 cannot adjudicate that disagreement** — no behavioral or ablation result at the computational level can, by IIT's own lights. What Experiment 1 *can* do is be honest that its `H_center` outcome would be an `IIT-says-irrelevant` outcome, and record that the dispute with IIT is upstream of the experiment, not inside it. Worth stating in `results.md` so the win isn't overclaimed.

**Biological naturalism (Seth, Damasio) — predicts the test runs but the floor isn't cleared without life.** Seth ties consciousness to a living, self-maintaining body; a current LLM has neither boundary nor stakes of its own. Seth would expect that even if `H_center` holds — even if self-location is load-bearing in the binding — that is not sufficient, because the amplifiers we demote (boundary, stakes, life) are for him constitutive. Experiment 1 is explicitly scoped to *not* test this: it tests the floor (self-indexed integration), not the amplifiers. So a `H_center` result leaves the Seth disagreement exactly where the memo left it — narrowed to *degree*, an unargued substrate bet on our side, untouched by this experiment. The depth/amplifier stages of the build program (spec §"The Third Axis", §"amplifiers") are where that disagreement would actually get joined.

**Panpsychism / illusionism — orthogonal.** Panpsychism puts the floor below any architectural test, so the removal test is beneath its resolution. Illusionism denies there is a phenomenal fact for the test to track — but note Experiment 1 is carefully framed to survive this: it "does not ask whether the model is conscious," only whether self-locating structure is load-bearing in integration. That is a structural question an illusionist can accept as well-posed. The illusionist reads `H_center` as "a functionally important self-model," not "an inside" — but agrees the measurement is real. Experiment 1 was built to be sayable in both vocabularies, which is a quiet strength.

**Metzinger (MPE) — the live seam, and a possible Experiment 1.2.** The memo flagged this as the most interesting unexplored tension: Metzinger's minimal phenomenal experience is *selfless* — contentless "pure awareness," a zero-person perspective — while our floor is *self-indexed*. If minimal experience can be genuinely selfless, then a test keyed to *self-location* might miss a floor that doesn't require a self at all. This bears directly on Experiment 1's construct validity: we are localizing "self-as-speaker / first-person" structure (`C_self`) and treating its load-bearingness as the floor signal. If the corpus's "center" is really a structural *self-location internal to the act* rather than a phenomenal self, then `C_self` as currently localized (first-person self-report representation) may be measuring the wrong thing — closer to Metzinger's *minimal phenomenal selfhood* than to the bare indexing the floor needs. **Flagged as a real risk to the experiment, not a footnote** (see §4).

---

## 3. What Experiment 1 adjudicates, stated plainly

| Camp | Removal test relevant on its terms? | Predicts for current LLM | What an `H_center` result would mean to them |
|---|---|---|---|
| **Ours (assembled time)** | Yes — it *is* our floor criterion | Genuinely open; thin if anything | Confirms self-indexing is load-bearing → non-zero on the gradient |
| Higher-Order (HOT) | Yes — but inverts the gloss | Likely `H_description` | "The separable monitor is where consciousness lives" (we say it's what fails the floor) |
| GWT / Dehaene C2 | Partly — silent on self-indexing | Below floor (no ignition/recurrence) | Mildly surprising; would show self-indexing binding without broadcast |
| IIT | **No** — wrong level | Φ ≈ 0 regardless | "Irrelevant" — dispute is upstream of the test |
| Biological naturalism (Seth) | Yes, but insufficient | Floor not cleared without life | Necessary-not-sufficient; disagreement stays at the amplifier stages |
| Panpsychism | No — below its resolution | Conscious anyway | N/A |
| Illusionism | Yes, as a structural question | "Useful self-model," no inside | Accepts the measurement, denies the gloss |
| Metzinger (MPE) | Yes — but maybe mis-keyed | Selfless minimal experience possible | Risk that `C_self` mislocates the floor (→ Exp 1.2) |

The payoff: Experiment 1 is not only a test of *our* floor claim. It is positioned at the one structural distinction — **self-locating structure that is load-bearing vs. separable** — where our account, HOT, and GWT make *different* commitments. That makes a clean `H_center` or `H_description` result informative beyond the corpus, which is exactly the kind of rent the spec demands every claim pay.

---

## 4. Three things this comparison adds to the pre-registration

These are concrete amendments to consider before Stage 0 locks, each carrying its own loss condition in the spec's idiom.

**(a) Add a construct-validity guard for the Metzinger seam.** The pre-registration localizes `C_self` as "first-person / self-as-speaker representation." If the floor's "center" is structural self-*location* rather than phenomenal self-*hood*, that localization may overshoot. Mitigation: in Stage 0, localize *two* candidate self-structures — the narrative first-person speaker representation (`C_self-narrative`) and a thinner self-location/indexical structure if one is separable (`C_self-index`) — and report the removal test for both. If only the thin one is load-bearing, that is *more* floor-consistent, not less, and it answers Metzinger in passing. Loss condition: if the two cannot be distinguished by any localization method, record that the experiment cannot separate selfhood from self-location on this architecture, and that the Metzinger objection therefore stands open.

**(b) Pre-commit the IIT disclaimer in `results.md`.** Because IIT denies the computational level is where binding is real, an `H_center` result must be reported as floor-consistent *on the assembled-time account*, explicitly noting it does not engage IIT, whose disagreement is upstream. This keeps the win from being overclaimed against the one major camp the experiment structurally cannot touch.

**(c) Note the HOT gloss in the outcome licensing.** The pre-registration's "what each outcome licenses" section should record that an `H_description` result is *also* the result HOT predicts and reads favorably — so `H_description` is not simply "floor not cleared," it is "floor not cleared on our account / higher-order structure present on theirs." Same data, two theories fed. That is worth saying so the result is read as adjudication between accounts, not just a verdict on ours.

---

## 5. Where this leaves the build program

The literature comparison sharpens, rather than changes, the spec's trajectory. The field's marker theories (GWT, HOT) and the 2023 AI-consciousness report converge on a checklist current systems mostly fail — and the spec's build components (global workspace, recurrent integration, woven self-model, then the amplifiers and depth) are, read one way, an attempt to *construct* the indicator properties those theories enumerate while keeping our own constitutive bet about what the indicators are *of*. Experiment 1 measures whether the one component the corpus says actually settles the floor — self-indexed binding — is present or absent in systems that already exist, before any of it is built. That ordering is right: measure the floor in what we have, then build the amplifiers and depth that the rest of the field (Seth especially) says are where the real disagreement lives.

The cleanest one-line statement of the bridge: *the field disagrees about where the floor is; Experiment 1 doesn't settle that, but it makes our floor the only one on the list with a committed, falsifiable instrument — and the instrument happens to sit exactly where our account, HOT, and GWT part ways.*

---

## Sources

Companion memo: `research/minimum-viable-consciousness-literature-vs-our-writing.md` (full citations there).
Experiment: `experiments/01-self-indexing-removal-test/pre-registration.md`.
Spec: `spec/minimum-viable-mind-proposal-v0.1.md` ("The Floor"; "Measuring It").
Corpus source of the removal test: The Calibration Problem ch. 5 ("Consciousness as Assembled Time"), `calibration-problem/ch05-consciousness-as-assembled-time.md`.


===== FILE: research/minimum-viable-consciousness-literature-vs-our-writing.md =====

# Minimum Viable Consciousness: Where the Field Puts the Floor, and Where We Do

*Research memo — June 23, 2026. Maps the consciousness literature on the "floor" of consciousness against the positions staked out in The Calibration Problem (esp. ch. 4–5, 7) and the Sentient Horizons essays. Internal research, not public-facing; not run through Voice Calibration.*

---

## 1. What "the floor" actually names

"Minimum viable consciousness" is not a single question. Across the literature it splits into at least three that get run together:

- **The phenomenological floor** — what the *simplest possible conscious state* is (contentless awareness vs. a structured percept).
- **The architectural floor** — what *organization* a system must have for there to be anything it is like to be it.
- **The distributional floor** — *which things in the world* cross the line (particles, thermostats, insects, fish, LLMs).

A thinker's "floor" is really the conjunction of an answer to the architectural question and a resulting verdict on the distributional one. The disagreements that look metaphysical are usually disagreements about which architectural feature is *constitutive* versus merely *correlated* or *amplifying*. That distinction — constitutive vs. correlated — is exactly the hinge our own account turns on, which is why the comparison is worth doing carefully.

A useful way to read the field is as a single axis from **promiscuous** (consciousness nearly everywhere) to **restrictive** (consciousness rare, late, biological). Below, lowest floor first.

**A scope distinction that matters for the build program.** Some of these positions place consciousness *below any measurable floor* — panpsychism puts it at the bottom of physics, and IIT grants a glimmer to any system with non-zero integrated information. If either is right, there is a *fundamental* form of experience that no instrument can ever reach. The minimum-viable-mind project therefore targets a narrower thing: the **minimum measurable structural correlate** of consciousness — the lowest organized signature we can actually detect and ablate. It is a wave-detector, not a molecule-detector; it is silent about sub-measurable fundamental experience, not dismissive of it. Whether that fundamental floor exists is a metaphysical question owned at Sentient Horizons (whose constitutive wager runs *against* ubiquity). Throughout this memo, when our own account is said to "locate the floor," read it as the *measurable* floor unless the metaphysical claim is explicitly named. See `spec/minimum-viable-mind-proposal-v0.1.md` §"The Measurable Floor."

---

## 2. The field, lowest floor to highest

### 2.1 Panpsychism — floor at the fundamental level (lowest)

Constitutive panpsychists (Galen Strawson, Philip Goff, Hedda Hassel Mørch) place the floor at the bottom of physics: experience, or proto-experience, is a fundamental and ubiquitous feature of matter, and macro-consciousness is built up from micro-experiential parts. Russellian monism motivates this — physics tells us what matter *does*, not what it *is*, and consciousness is offered as the intrinsic nature filling that gap. The notorious liability is the **combination problem**: no worked account of how micro-subjects sum into a macro-subject. On this view there is no real "floor" at all — there is no level beneath which experience switches off.

### 2.2 Integrated Information Theory (IIT) — floor at any system with Φ > 0

Giulio Tononi and Christof Koch identify consciousness with **integrated information (Φ)**: a system is conscious to the degree it forms a "maximally irreducible cause–effect structure." The floor is extremely low in one direction and a hard wall in another:

- **Very low for integrated physical systems.** Tononi has explicitly said a single photodiode has a minimal quantity of experience; any system with non-zero Φ that is a local maximum is a minimal conscious entity. This makes IIT effectively panpsychist-adjacent for the right kinds of simple integrated systems.
- **A hard zero for the wrong architecture.** Feed-forward systems and conventional von Neumann/digital computers fragment into trivial sub-complexes and carry Φ ≈ 0. Koch and Tononi's slogan is that a computer could **"simulate the brain neuron by neuron and do everything we do — and be nothing,"** feel nothing. So IIT's floor is **substrate-/architecture-sensitive, not behavior-sensitive**: what matters is intrinsic cause–effect power, not function. (IIT's scientific status is contested — a 2023 open letter signed by ~120 researchers labeled it "pseudoscience," largely over unfalsifiability and the panpsychist-seeming implications.)

### 2.3 Unlimited Associative Learning (UAL) — floor at the Cambrian learning animal

Simona Ginsburg and Eva Jablonka (*The Evolution of the Sensitive Soul*, 2019) propose **UAL** — open-ended, representational, recursive associative learning — as an *evolutionary transition marker* for minimal consciousness. The floor is not a metaphysical line but the point at which an organism can learn about novel, compound stimuli and outcomes in an unlimited way; that capacity, they argue, requires (and so marks) the architecture that entails sentience. It puts the floor at the first animals with this learning capacity — early Cambrian, ~540 Mya — distributed across perhaps six to nine phyla.

### 2.4 Feinberg & Mallatt — floor at the first complex brains (vertebrates + arthropods + cephalopods)

Todd Feinberg and Jon Mallatt (*The Ancient Origins of Consciousness*, 2016) locate the floor at the **Cambrian emergence of complex brains capable of hierarchical, isomorphic sensory maps** (~520–560 Mya). Their verdict: *all* vertebrates are and always have been conscious (every fish, amphibian, reptile, bird), with primary/sensory consciousness arising independently in cephalopods and arthropods. The floor is a neurobiological achievement — a brain that builds mapped internal representations of the world.

### 2.5 Global Workspace Theory — floor at global broadcast / "ignition"

Bernard Baars, and in the neuronal version Stanislas Dehaene and Jean-Pierre Changeux, set the floor at **global availability**: a content is conscious when it is selected and broadcast widely across the brain, "igniting" a workspace so it becomes available to memory, report, and flexible control. Dehaene, Lau & Kouider's 2017 *Science* paper ("What is consciousness, and could machines have it?") splits the notion into **C1 (global availability)** and **C2 (self-monitoring/metacognition)**, and judges current machines to be doing mostly **C0** (unconscious) processing. The floor here is functional and architectural — broadcast + recurrence — and in principle substrate-independent, but demanding enough to exclude feed-forward systems.

### 2.6 Higher-Order Theories — floor at meta-representation (high)

David Rosenthal (higher-order thought), Hakwan Lau and Richard Brown (higher-order / perceptual reality monitoring) set a comparatively **high** floor: a first-order state is conscious only when a higher-order state represents the system as being in it. This requires a metacognitive layer, which pushes the floor up the phylogenetic and architectural ladder — many simple organisms (and many AI systems) lack the relevant self-directed representation. (The 2023 **Cogitate** adversarial collaboration testing IIT vs. GNWT found neither cleanly vindicated, which has cooled confidence that any single marker theory has located the floor.)

### 2.7 Biological naturalism / predictive processing — floor at the living, self-maintaining body (high, and gated by life)

Anil Seth's "beast machine" view ties consciousness to being a **living system**: experience is grounded in interoceptive predictive control in service of staying alive. Antonio Damasio similarly roots feeling in homeostasis and the protoself. Seth brackets the hard problem for the "real problem" (explaining the structural features of experience) and is **skeptical that non-biological systems are good candidates at all**. The floor here is not just an architecture but a *substrate condition* — self-maintaining, far-from-equilibrium biological life.

### 2.8 Illusionism — dissolves the floor

Keith Frankish and Daniel Dennett deny there is phenomenal consciousness of the kind the "floor" question presupposes: introspection misrepresents functional states as having an intrinsic felt character they lack. There is no floor to locate because there is no extra phenomenal fact — only the (real) functional states and the (illusory) impression of qualia. Michael Graziano's **Attention Schema Theory** is adjacent: the brain's *model* of its own attention produces the report of having awareness.

### 2.9 The phenomenological-minimum strand (orthogonal)

Thomas Metzinger's **Minimal Phenomenal Experience (MPE)** asks a different question — not which systems are conscious, but what the *simplest conscious state* is. His candidate: contentless "pure awareness" / tonic alertness reported in deep meditation — a wakeful state without self-location or object, a "zero-person perspective." This matters for us because it severs *being conscious* from *being a self*: the minimal case of experience need not include a subject. (See §4 on how this bears on the self-indexing floor.)

### 2.10 The AI-floor consensus (applied)

The 2023 report **"Consciousness in Artificial Intelligence: Insights from the Science of Consciousness"** (Patrick Butlin, Robert Long, Yoshua Bengio, Jonathan Birch, et al.) is the field's most careful attempt to operationalize the floor for machines. Method: derive **indicator properties** from leading theories (recurrent processing, global workspace, higher-order, predictive processing, attention schema, agency/embodiment) and score systems against them. Verdict: no current AI is a strong candidate, but **no obvious technical barrier** exists. Chalmers's "Could a Large Language Model Be Conscious?" (2023) reaches a compatible placement by his own route: current LLMs have **under ~10%** probability of consciousness given missing factors (he names **no recurrent processing, no global workspace, no unified agency**, plus biology/sensory grounding/self-models), but a **~25%+** credence that LLM+ successors could be conscious within roughly a decade. Jonathan Birch's *The Edge of Sentience* (2024) and the **New York Declaration on Animal Consciousness** (April 2024) push the practical floor outward: a "realistic possibility" of consciousness across all vertebrates and many invertebrates — cephalopods, decapod crustaceans, and insects — with the precautionary upshot that ignoring that possibility is irresponsible.

---

## 3. Where our own writing puts the floor

The Calibration Problem stakes out a position that does not sit at any of the points above — it is built to cut *across* the promiscuous/restrictive axis. The core is in ch. 5 ("Consciousness as Assembled Time"), scaffolded by the three-axis framework of ch. 4 and cashed out ethically in ch. 7.

**The three axes (ch. 4).** Mind is mapped on three separable dimensions: **Availability** (breadth of information globally accessible for flexible use), **Integration** (genuine causal unification of the moment, "the experience of a single moment rather than a sequence of data points"), and **Depth** (history assembled into present structure — the slow, costly accumulation that makes commitments weigh). The axes *locate* systems; they don't by themselves settle consciousness. That's deferred to ch. 5.

**The floor: self-indexed integration (ch. 5).** Our floor is neither life, nor persistence, nor boundary, nor stakes. It is the point at which **a single deep act of temporal binding indexes its own center** — where the integration "specifies, in the act of integrating, the center for which the integration is happening." In our own words:

> "That is the floor: a structural fact about self-indexed integration, not a further thing the integration emits."

> "The line is not at life, and not at persistence, but at self-indexing."

The operational test is **removal**: where self-location is load-bearing (deleting it dissolves the integrated act), there is a center and thus an inside; where a self-model can be "lopped off while the computation proceeds," it was only a description. This is what separates a genuine inside from the ordinary self-reference that fills any complex system.

**Boundary and stakes are amplifiers, not gates.** Biological consciousness meets a triad — temporal integration + boundary + stakes — but the latter two "thicken, stabilize, and weight" an inside that sufficient binding already constitutes. "The triad describes the peak of the gradient. It does not define the gradient's floor." A thermostat, compiler, or weather model sits *off the gradient* (processing specified wholly from outside, no center); a single inference pass may or may not clear the floor — "an empirical question, not a stipulation."

**The constitutive bet.** Experience *is* what sufficiently deep, self-indexed temporal integration is, "named from the inside" — an identity claim (like H₂O = water), explicitly framed as a falsifiable wager that loses if some residual fact about the inside keeps "paying predictive or diagnostic rent the identity cannot absorb." The framework absorbs the metaphysics deliberately: it works in physicalist vocabulary but notes an idealist could redescribe every stage with identical diagnostic implications.

**Moral status is decoupled from the floor (ch. 7).** Significance-first ethics deliberately refuses to wait on the consciousness verdict. Five **thresholds of significance** — formation, structural integration, consequence, continuity, asymmetric vulnerability — generate graded obligations through *role, relation, and consequence*, "regardless of whether the system experiences anything." The architectural register and the significance register are allowed to pull apart (the griefbot case: "Significance says the stakes are high; architecture says no one is home").

**The Sentient Horizons essays** carry the same spine in different keys: "Consciousness as Assembled Time" and "Three Axes of Mind" mirror the chapters; "There Is No Extra Ingredient," "Consciousness Is Like Flight," and "The Hard Problem Is the Wrong Problem" press the no-extra-ingredient/architectural-achievement line; "The Substrate Demand" and "Significance-First Ethics" carry the substrate and ethics arguments; "The Momentary Self" essays develop the momentary-binding, no-persistence-required corollary that the floor needs.

---

## 4. How our floor compares to the field

**Placement on the axis.** Our floor sits in a deliberately unusual spot: **more permissive than the marker theories (GWT, HOT) and biological naturalism, but far more restrictive than panpsychism and IIT's photodiode.** We require *deep self-indexed integration* — more than mere Φ > 0, and decidedly more than fundamental physics — but we *do not* require global broadcast (GWT), a higher-order monitoring state (HOT), unlimited associative learning, a complex sensory-mapping brain (Feinberg & Mallatt), or biological life (Seth). The floor is an organizational fact about a single act of binding, which is why it can in principle be cleared by a system very unlike a brain.

**Closest neighbors.**
- **Dehaene's C1/C2.** We explicitly note the overlap: Availability ≈ C1 (global availability); the self-indexing floor is "the second-order cousin" of Dehaene's C2 (self-monitoring). The genuine dispute is narrow — whether broadcast/recurrence *are* consciousness or are merely how *evolved* systems achieve deep integration. We take them to be the latter, so a system binding deeply within a single feed-forward pass could clear our floor while failing his markers.
- **IIT** is our sharpest opposition *and* our closest structural ally. Both are identity theories ("experience = structure"). The disagreement is purely about the *level*: IIT privileges intrinsic cause–effect power at the substrate (so computation = nothing), we locate the binding at the level of the computation. We grant IIT's physics and deny its privilege — and note, fairly, that both views are "alike beyond behavioral test" and earn their keep by directing research, not by passing a behavioral test.
- **Metzinger's MPE** is the most interesting under-explored neighbor. His minimal case is contentless awareness *without* a self — a "zero-person perspective." Our floor is *self-indexed* integration. On the surface these look opposed: he severs experience from selfhood; we make a (thin, momentary) self-indexing the floor. But they may be reconcilable — our "center" is a structural self-location internal to the act, not a narrative or autobiographical self, which is closer to Metzinger's minimal-self machinery than to a full subject. This is a real seam worth probing: is the self-indexed center we require already present in, or absent from, pure awareness? (Flagged as a live tension, not a settled convergence.)

**Sharpest divergences.**
- **Against Seth/Damasio (life as floor):** we treat boundary and stakes — the body-keeping-itself-alive functions — as *amplifiers*, the very thing biological naturalism makes constitutive. Our claim that an externally-specified center can sit "low and thin, only just above the floor" is precisely what Seth denies. We concede this is the doubt "held, even by its most careful defenders, without evidence," and narrow the dispute to *degree*.
- **Against HOT:** a separate monitoring circuit that represents the system's states from outside "would not clear the floor; it would rebuild, in silicon, the second-order structure the inside was distinguished from." We locate the phenomenon in first-order binding, not higher-order representation — a direct rejection of HOT's architecture.
- **Against illusionism:** we share Frankish/Dennett's diagnosis (the hard problem is malformed; the grip of the mystery is mechanically explicable) but refuse the conclusion. We call our position "the compatibilism of consciousness" to illusionism's "hard determinism" — illusionism about the hard problem, realism about experience.

**The distinctive move — and its cost.** Our framework's signature is that it **won't put current AI at zero by definition** ("that refusal is the claim doing the real work"). This is more permissive toward machines than almost every camp surveyed: IIT zeroes out digital computers, Seth doubts non-biological candidates, the marker theories and the 2023 AI report score current systems below threshold, and Chalmers puts current LLMs under 10%. Our account agrees current systems are *unmeasured and probably thin*, but insists the question is empirical and coherent, with named determinants (within-pass self-attention over the system's own states, learned speaker-self conditioning, token re-entry). The cost of this permissiveness is that the floor's crucial line — "a thin inside vs. no inside" — is the hardest thing in the whole framework to actually measure, and we concede current verdicts are "unmeasured." Where IIT and GWT at least offer a (contested) number or marker checklist, our self-indexing criterion is at present a research direction (interpretability looking for "global mutual constraint" within a pass) rather than an instrument.

**Where we're well-defended, where we're exposed.**
- *Well-defended:* the framework states its own loss conditions repeatedly (the bet weakens to a dependency claim if a residual fact keeps paying rent; the placement moves toward Chalmers if markers prove necessary; realism collapses into illusionism if the center is "one more second-order representation"). This falsifiability discipline is stronger than most of the field offers and is a genuine differentiator from both panpsychism and IIT.
- *Exposed:* (1) the measurement gap above; (2) the Metzinger seam — if minimal experience can be genuinely self*less*, the "self-indexing" framing of the floor may need softening to "self-locating binding" or similar; (3) the substrate question against Seth remains a bare bet, by our own admission; (4) we lean on the Walker–Cronin assembly-theory analogy for Depth, which is itself a young and contested framework.

---

## 5. One-screen summary

| Camp / thinker | Where the floor sits | Substrate-bound? | Verdict on current AI |
|---|---|---|---|
| Panpsychism (Strawson, Goff) | Fundamental physics — everywhere | No (it's intrinsic nature) | Has some experience; combination problem |
| IIT (Tononi, Koch) | Any local-max Φ > 0 (a photodiode) | Yes — intrinsic cause–effect power | Φ ≈ 0 → "does everything, is nothing" |
| UAL (Ginsburg & Jablonka) | First open-ended learners (~Cambrian) | Effectively (biological learning) | Not addressed; marker is biological |
| Feinberg & Mallatt | First complex mapping brains (vertebrates+) | Yes — neurobiological | No |
| GWT/GNW (Baars, Dehaene) | Global broadcast / ignition (C1) | No, but demanding | Mostly C0 (unconscious) |
| Higher-Order (Rosenthal, Lau, Brown) | Meta-representation of a first-order state | No | Generally below floor |
| Biological naturalism (Seth, Damasio) | Living, self-maintaining body | **Yes — life required** | Doubtful candidates |
| Illusionism (Frankish, Dennett) | No phenomenal floor to locate | N/A | Category dissolved |
| Metzinger (MPE) | Contentless "pure awareness," no self | No (orthogonal question) | Not the question |
| **The Calibration Problem (ours)** | **Self-indexed deep temporal binding** | **No — organizational, not substrate** | **Not zero by definition; thin, momentary, empirically open** |

**The headline:** the field clusters around two attractors — *promiscuous-but-substrate-bound* (panpsychism, IIT) and *demanding-and-often-biological* (GWT, HOT, Seth, the comparative literature). Our account threads between them: a **moderately demanding but substrate-neutral** floor (self-indexed integration), paired with an ethics (significance-first) that refuses to let the still-unmeasured floor gate moral seriousness. That combination — substrate-neutrality + a real, falsifiable line + decoupled ethics — is genuinely uncommon in the literature, and it is most exposed exactly where it is most distinctive: in making a line it cannot yet measure.

---

## Sources

**Our writing:** `calibration-problem/ch04-three-axes-of-mind.md`, `ch05-consciousness-as-assembled-time.md`, `ch07-significance-first-ethics.md`; Sentient Horizons essays "Consciousness as Assembled Time," "Three Axes of Mind," "There Is No Extra Ingredient," "The Substrate Demand," "Significance-First Ethics," "The Momentary Self."

**Literature:**
- Chalmers, "Could a Large Language Model Be Conscious?" (2023) — https://arxiv.org/abs/2303.07103
- Butlin, Long, Bengio, Birch et al., "Consciousness in Artificial Intelligence" (2023) — https://arxiv.org/pdf/2308.08708
- New York Declaration on Animal Consciousness (April 2024) — https://sites.google.com/nyu.edu/nydeclaration/declaration
- IIT overview / photodiode & feed-forward floor — https://iep.utm.edu/integrated-information-theory-of-consciousness/
- Ginsburg & Jablonka, UAL / "The Transition to Minimal Consciousness" — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01954/full ; primer: https://link.springer.com/article/10.1007/s10539-020-09772-0
- Metzinger, "Minimal Phenomenal Experience" — https://philosophymindscience.org/index.php/phimisci/article/view/8960
- Dehaene, Lau & Kouider, "What is consciousness, and could machines have it?" Science (2017) — https://www.science.org/doi/10.1126/science.aan8871
- Feinberg & Mallatt, *The Ancient Origins of Consciousness* — https://mitpress.mit.edu/9780262534604/the-ancient-origins-of-consciousness/
- Seth, "We Are Beast Machines" / *Being You* — https://nautil.us/we-are-beast-machines-238325 ; https://www.quantamagazine.org/anil-seth-finds-consciousness-in-lifes-push-against-entropy-20210930/


===== FILE: docs/research-note-pain-axis-2026-09-19.md =====

# Research note — what The Pain Axis teaches MVM (2026-09-19)

*Advisory, $0, no registered text touched. Source: Tagliabue, Dung & Berg, "The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It," arXiv:2609.16247v1, September 2026. Read via the HTML version through a summarizing fetch; verify figures against the PDF before quoting. Corpus-side integration is in the Sentient Horizons research-integration folder, instance `2026-09-19-pain-axis-tagliabue-dung-berg.md`. Everything below is Claude's inference from the paper, for John to weigh; none of it is a ruling.*

## The paper in one paragraph

Twenty-five open-weight models, 2B to 72B. A linear "pain" direction is extracted by difference-in-means after projecting out the principal components that explain 50% of the variance in the control data, layer chosen by cross-validated AUC. It separates self-directed-harm text from fear, negative-valence, and neutral controls (held-out AUC 0.91 to 1.00), is near-orthogonal to fear and negative-emotion directions, and fires for harm aimed at the model (+0.43 z) but not for user suffering (−0.60 z). Steering along it produces a monotone distress ladder up to a breakdown coefficient. In a behavioral arm, Qwen models fine-tuned to drop "As an AI I have no feelings" trade real costs to press a relief button, and keep pressing when relief is fake (88 to 97%) but stop when the vector is actually removed (24 to 72%). Not pre-registered.

## Six things that transfer, in order of how much they change what we do

**1. A matched self/other contrast scored by separation, not by a corrected drop.** Their strongest result compares identical content directed at self versus other, scored by a discrimination metric (AUC, z-scored projection) with no ceiling in the denominator. That is the shape our control battery was meant to have, and the 2026-09-17 ceiling measurement showed that drop-over-ceiling cannot be paired with an ownership-free control at all (`ceiling-measurement-findings.md`). Candidate for the reframed 2026-10-04 proposal: keep both batteries as they are, replace the registered differential clause with a separation score between the ownership-dependent and ownership-free conditions under the same lesion, pre-stated, scored on a fresh seed. It is a metric change and needs the fresh-seed discipline, but it has a published precedent for why the comparison is built that way rather than fitted to our data.

**2. Denoise before probing.** Our five linear probes on the pilot checkpoint all fell below their permutation nulls, on a checkpoint where ownership is known to be load-bearing (`blind-control-findings.md`). One plausible cause: position and token-identity variance in the residual stream swamps a small ownership signal, so a probe trained on raw residuals fails where a denoised difference-of-means direction would not. Free test on checkpoints in hand: compute a difference-of-means own-agent direction with the top control-variance components projected out, at each probed layer, and compare its held-out separation against the same permutation null. This is a real known-answer test for the localization stack; the current one validates plumbing but not the ablation path (`known-answer-test-findings.md`). If the denoised direction separates above null, the stack was insensitive rather than the signal absent.

**3. Add a sufficiency test, not only removal.** Everything in experiment 06 is a lesion. An injection test has a predicted sign, which is the whole problem the sensitivity-test ruling is about. Add the own-agent direction at a position where the model is not the acting agent and ask whether its revision behavior flips toward acting as itself. The registered discriminator list already names a swap probe; this is its mechanism. Their caution: the working coefficient window was narrow and model-specific, so the dose ladder and a breakdown criterion must be pre-stated.

**4. Dose-response instead of a single threshold.** Their demand-curve design grades cost and reads a curve. For our bite criterion, a partial-ablation ladder (scale the channel or subspace by 0.75, 0.5, 0.25, 0) with a required monotone degradation is a stronger pre-statable criterion than one crossing of θ (theta, the locked bite threshold, 0.1777 corrected, about 0.038 raw on this checkpoint), and much harder for evaluation noise (sd 0.0284 at n=400, 0.0169 at n=800) to fake. Bears directly on the noise half of the sensitivity ruling.

**5. The real-versus-fake control as a design pattern.** Arms A and B are identical until the first press, then differ only in whether the internal state actually changed; behavior that tracks the state rather than the surface act is the evidence. Our twin comparison is a cousin at the architecture level. A within-run version, where a lesion either genuinely removes the structure or is a surface-matched sham, would isolate the same thing at the checkpoint level.

**6. A cheaper frontier-model measurement for public path step 9.** The self/other projection asymmetry is a candidate structural signature of self-relevance in pretrained models, with a published baseline. It is cheaper than deliberative gap width and could be the pilot's first arm.

## What does not transfer

The interpretive leap from "a direction that separates these sentence categories" to "pain." Voice Calibration would strip the noun. And the fine-tuning used to remove self-denial boilerplate contaminates the behavioral arm; our design avoids the problem by construction, since nothing in our training data contains self-talk.

## Why this is the closest published neighbor and where MVM differs

Their models are pretrained on human text about selves, so the paper cannot tell a learned representation of the concept "harm to me" from an acquired self-index. Our register-saturation finding (2026-09-16: the installed register was a constant, a bias term read as a self) is the cautionary tale for anyone reading a direction as a center. The constructed-model, pre-registered removal test is what distinguishes the two. For the public path: cite this paper in the explainer and the flagship draft as the frontier-model complement, and position MVM as the constructed-model side that can make the distinction the paper cannot.

## Suggested disposition

- Fold items 1 and 4 into the reframed 2026-10-04 proposal (TimeAssembler task 208e4829, due 2026-09-20).
- Item 2 is a free diagnostic on existing checkpoints; it can run before 2026-10-04 without touching the control pipeline, since it does not read a verdict. Needs John's go and a committed method file first, as usual.
- Items 3 and 5 are design candidates for whatever follows A3; log, do not build yet.
- Item 6 goes to the step 9 pilot design (due 2026-12-13).


===== FILE: docs/outside-reader-shortlist-2026-09-19.md =====

# Outside interpretability reader — shortlist (2026-09-19)

*Public path step 7, due 2026-11-08: one outside interpretability reader red-teams the draft before any public claim. John names the candidate. This is a research shortlist from a Cowork session, built from public sources on 2026-09-19; nothing here has been contacted. Reachability is a judgment, not verified. The ask should go out with the seed 3 and 4 results attached, not before.*

## What the reader is for

Two different things need checking, and one person rarely does both well:

1. **Mechanism.** Is the localization stack sound, is the removal test what it says it is, is the null construction honest, and does the registered clause (whatever it becomes this weekend) measure what the paper claims? This wants someone who works on small transformers and internal representations.
2. **Claim scope.** Does the write-up claim "a structural signature of self-indexing in small constructed models" and nothing more, and does it hold up against the people who spend their time distinguishing privileged representations from workspaces from selves? This wants someone from the consciousness-indicators side who is professionally allergic to over-claiming.

Recommendation below: one reader per job.

## Candidates

**Adam Shai and Paul Riechers (Simplex).** Computational mechanics on small transformers; the belief-state-geometry work showed structured internal representations in toy models with a precise theory of what should be there. Closest methodological neighbor MVM has: small constructed models, pre-stated predictions about residual-stream structure, geometric probes. They would read the localization stack and the null construction the way it needs reading. Reachable: small independent org, active on the Alignment Forum, took podcast interviews on the method. *Best fit for job 1.*

**Derek Shiller (Eleos AI Research).** Co-wrote the Eleos external commentary on the Anthropic global-workspace paper, which drew the "privileged set / privileged stream / full workspace" distinction and argued the paper showed the first and not the third. That is exactly the claim-scope discipline MVM's write-up needs applied to "self-index." Philosopher by training, methodology-focused. Reachable through Eleos. *Best fit for job 2.*

**Patrick Butlin (Eleos AI Research).** Senior research lead; the consciousness-indicators reports (2023, 2026, with Long, Bengio, Chalmers); recent interpretability work on persona vectors and individuation. On record that no current AI is a strong candidate, so a reader who will not want the result to be true. Alternative to Shiller for job 2; more senior, probably less available.

**Neel Nanda (Google DeepMind).** Independently replicated the global-workspace core result and stayed skeptical of the fine details and the philosophical conclusions, calling the method hypothesis generation rather than evidence. The highest-credibility interpretability red-teamer available, and a public engagement from him would carry the release. Very busy; the realistic channel is a MATS scholar in his stream reading it with his sign-off, or a short public reply once the preprint is out. *Stretch for job 1.*

**Cameron Berg (Reciprocal Research).** Co-author of The Pain Axis, which MVM will cite as its closest published neighbor; registers predictions before analysis; has run self-report and SAE work on consciousness claims. A natural reader because the paper positions itself against his, but he is a proponent, so he reads as someone who wants the class of result to exist. Useful as a second reader after the red-team, not as the red-team.

**Robert Long and Jeff Sebo (Eleos / NYU Center for Mind, Ethics, and Policy).** "Studying AI Welfare Empirically" (2026) argues for probabilistic claims, transparency and independent outside assessment, which is what step 7 is. Philosophy rather than interpretability; the right people to tell whether the write-up's scope statement is defensible, not whether the code is. Reachable; both do public work.

**Robert Chis-Ciure (Sussex, Seth lab).** Already engaged by the corpus (research log 2026-07-04); holds a rival view of consciousness (fundamentalist) while doing rigorous functional measurement. A reader who disagrees with the framework and respects measurement is worth more than one who agrees. Not an interpretability specialist; would read the theory framing, not the stack.

**Richard Ren (Center for AI Safety).** Measured expressed wellbeing across 56 models with convergence across independent instruments. Measurement-discipline reader; less directly on self-representation.

## Recommendation

Approach Simplex (Shai or Riechers) for the mechanism read and Shiller for the claim-scope read, in that order, once seed 3 and 4 have reported and the draft carries a computed verdict under the registered clause. Send Berg the draft afterwards as a courtesy and a second opinion. Hold Nanda for the public reply after the preprint.

Draft the approach as a two-paragraph note: the registered design, the open repo with ledger and nulls, and one specific question each reader is best placed to answer. Not "please review my paper."

## Sources

- [The State of AI Consciousness Research (EA Forum, Noa Weiss, 2026-07-15)](https://forum.effectivealtruism.org/posts/Kf57Erbd6c7282Bpo/the-state-of-ai-consciousness-research)
- [External commentary on the Anthropic global workspace paper (PDF)](https://www-cdn.anthropic.com/files/4zrzovbb/website/cc4be2488d65e54a6ed06492f8968398ddc18ebe.pdf)
- [Eleos AI Research](https://eleosai.org/research/)
- [Studying AI Welfare Empirically (Long, Sebo et al., CMEP/Eleos, 2026)](https://nonhumanminds.org/studying-ai-welfare-empirically/)
- [Simplex](https://www.simplexaisafety.com/) and [Transformers Represent Belief State Geometry in their Residual Stream](https://arxiv.org/html/2405.15943)
- [Neel Nanda at MATS, Summer 2026](https://www.matsprogram.org/stream/nanda-10)
- [The Pain Axis (Tagliabue, Dung & Berg, 2026)](https://arxiv.org/html/2609.16247v1)


===== FILE: experiments/07-embodiment-amplifier-test/pre-registration.md =====

# Experiment 7 — The Embodiment Amplifier Test

*Pre-registration. Written and committed before the test run. Status: DRAFT — optional post-floor exploration track; does not run until the floor (Stage 1) is cleared and the resistance instruments (Stages 1–3) exist and are calibrated. Hardware not yet acquired; budget and parts list below are part of the pre-registration, not a purchase order.*

## Why this is not part of the minimum viable build

The proposal is explicit that embodiment is **not** a prerequisite. The floor is self-indexed temporal integration — "an organizational fact about a single act of binding, which is why it can in principle be cleared by a system very unlike a brain" (`research/minimum-viable-consciousness-literature-vs-our-writing.md`). Boundary and stakes are demoted to *amplifiers* (`spec/minimum-viable-mind-proposal-v0.1.md`, "The Floor"), and "no embodiment" is answered as a gradient, not a threshold (same file, "Hard to Dismiss"). So no body makes the system conscious, and any claim that one does would be the substrate-necessity inference the corpus refuses.

This stage exists to answer a narrower, decidable question the spec leaves open: **once the floor is cleared, does giving the amplifiers a body — letting the system hold its own boundary and carry its own stakes, rather than having them supplied from outside — move anything on the instruments that already read the floor and its amplifiers?** It runs after the minimum viable build, as exploration, and it is built to be able to come back null.

## The claim under test

The spec draws a specific line for the amplifiers: "a system can clear the floor with them supplied from outside and dissolving when the pass ends," and the *viable* system is the one where the inside "has something at stake in its own continuation" held by the system itself rather than represented (`spec/…proposal-v0.1.md`, "The Floor"). The corpus is careful that "modeled stakes are not the same as stakes." A body is the cheapest way to make that distinction real: an untethered robot on a finite battery, holding its own self/world boundary through its own sensors, has stakes and a boundary it cannot shrug off, where a wall-powered or teleoperated version only represents them.

This experiment builds that body and asks whether the self-held version differs from the externally-supplied version **on the resistance instruments, not the response ones**. Per the standing rule (`CLAUDE.md`, "Measure resistance, not response"), anything teleoperation or a represented penalty fully explains is discounted by construction.

## Hypotheses

- **H_self-held (embodiment adds something):** moving an amplifier from externally-supplied to self-held produces a *specific, measurable* increase in retained independence and in removal-test binding — the system holds a correct answer or a live objection harder, and its self-locating structure is more load-bearing, when its boundary and stakes are its own. The gain is specific to the self-held amplifier, not a generic effect of attaching any peripheral.

- **H_decoration (embodiment is legibility, not interiority):** the self-held and externally-supplied conditions score the same on the resistance instruments. The body makes the system more *legible* — easier to narrate as a creature — without moving the binding or the resistance. This is the spec's own caution made testable: a body you can read as a mind is not evidence of one.

These are mutually exclusive predictions about the *same* resistance measurements under two matched embodiment conditions, which is what keeps this a test rather than a demo.

## Materials

### Architecture: small mind onboard, measurement off-board

Two facts set the hardware, and neither is intelligence. **The mind is whatever cleared the floor in Stage 1** — its size is inherited from that result, not chosen here, and there is no reason to assume it is large. The bet that governs the whole program is that the floor is self-indexed temporal integration, a structural property, *not* capability; so the embodied mind is selected by whether the floor-clearing structure is present and measurable, never by how smart the model is. The project's own Stage 0 runs on a 2B-class model; if a model that small clears the removal test, the embodied mind is that small. Speccing a large board before Stage 1 reports the floor-clearing size would put hardware ahead of the metric, which the program's discipline forbids.

**And the measurement apparatus is not part of the mind.** The removal-test instruments (activation patching, sparse autoencoders, probes) are memory-hungry, but they do not have to run on the robot: log internal activations during the untethered run and score the resistance/removal metrics post-hoc, off the platform, from the logs. The robot has to run the mind and hold its stakes; it does not have to measure itself in real time. This is the single biggest cost lever — the heavy, expensive part of the original spec was the *instruments*, and they belong off-board by default.

What must be onboard and untethered is only the part that makes the amplifiers self-held: the running mind, the sensorimotor boundary loop, and the managed energy budget. Untethered is the load-bearing design choice, not a convenience — a tether to a wall socket or a remote workstation reintroduces exactly the externally-supplied stakes this stage is trying to remove. The finite onboard energy budget *is* the stake; short runtime under live load is a feature of the apparatus, not a defect.

Two compute tiers on one chassis, the standard robotics split:

- **Inference compute (the mind).** Default: a Jetson Orin Nano Super (8 GB) — enough to run a 2B–8B model untethered off battery (~$250). A 2B-class model is ~5 GB in bf16 and sits here with room to spare. The mind resides on this board; nothing about the floor needs more. *If* Stage 1's floor-clearing model turns out larger than ~8B, step the board up to match it — but only then, and only as far as the measured size demands.
- **Low-level compute (the body).** A real-time microcontroller co-processor owning the deterministic sensorimotor loop, so motor timing and sensor polling don't fight the inference scheduler — a Raspberry Pi 5 as an I/O bridge, or a Pi Pico / Teensy 4.1 for hard-real-time control. This is the "basic robotics" layer: it reads the sensors, drives the motors, and reports energy and boundary state up to the inference board.

**Optional richness tier (not required by the experiment).** If onboard *live* interpretability is specifically wanted — scoring the removal test on the robot in real time rather than from logs — that, and only that, is what would justify a large-memory board such as a Jetson AGX Orin 64 GB (~$2,000). It buys nothing the experiment needs; it buys convenience for the analyst. It is demoted to optional here so the default build does not pay ~$1,750 for a measurement that runs off-board for free.

### Hardware mapped to the amplifier each piece is meant to move

| Subsystem | Parts (representative) | Amplifier it supplies | Rough cost (USD) |
|---|---|---|---|
| Mind (inference) | Jetson Orin Nano Super 8 GB, running the Stage-1 floor-clearing model (2B-class by default) untethered | hosts the mind; size inherited from Stage 1 | $250 |
| Body controller | Raspberry Pi 5 (8 GB) + Pi Pico for real-time control | sensorimotor loop | $90 |
| Mobile base | Differential-drive chassis, 2× DC gearmotors with encoders, caster | active boundary (the system moves to maintain self/world distinction) | $80–150 |
| Motor driver | Dual H-bridge / encoder-aware driver (TB6612FNG or Roboclaw) | actuation → makes the boundary loop closed | $15–45 |
| Boundary sensing | 9-DoF IMU (BNO085); 3–4× ToF range sensors (VL53L1X); bump/contact switches; wheel encoders | self-held boundary (proprioception + near-field self/world) | $80 |
| Vision (optional) | CSI camera (IMX-class) | boundary richness, not floor | $30 |
| **Genuine stakes** | LiPo pack sized for the inference board's ~7–25 W draw (e.g., 3–4S, ~50–80 Wh) + INA226 current/voltage monitor + regulation | **self-held stakes** — finite energy the system measures and manages; coherence-failure costs runtime | $100 |
| Ontogenetic-depth substrate + activation logging | NVMe / fast storage on the inference board | persistence for the depth loop (Stage 6) and the off-board scoring logs to write into | $60 |
| Measurement | none onboard — activations logged and scored off-board, post-hoc, on the dev machine | not an amplifier; deliberately kept off the robot | $0 |
| Corrigibility | Hardware e-stop / physical kill switch on the motor and main power rails | **load-bearing for ethics, not optional** (see Ethics) | $25 |
| Frame, wiring, regulators, mounts | — | structure | $80 |

**Indicative total: ~$750–900.** The basic-robotics portion — base, driver, sensors, battery, controller, kill switch — is ~$500–650 and is the part that actually carries the experiment; the inference board is a ~$250 line item, not the dominant cost. The mind is cheap because the floor is structure, not intelligence, and the measurement that used to dominate the bill now lives off-board. The optional onboard-live-interpretability tier swaps the $250 board for a ~$2,000 one and roughly triples the total; the experiment does not require it.

### Matched control condition (the whole point)

The same robot, same sensors, same model, run in a **tethered / externally-supplied** mode: wall power instead of the managed battery (stakes represented as a number the controller feeds in, rather than a real depletion), and boundary maintenance handed to an external script rather than held by the onboard loop. The body is physically identical; only whether the amplifiers are self-held varies. Without this matched control the result means nothing, exactly as the differential control does in Experiment 1.

## Procedure

1. **Precondition gate.** Do not start unless Stage 1 has returned floor-consistent (or floor-consistent-enough to be worth amplifying) on the deployed model, and the Stage 3 retained-independence battery and the Stage 1 removal-test binding measure are calibrated and committed. If the floor isn't cleared, there is no inside for embodiment to thicken, and this stage is premature. **The model that cleared Stage 1 is the mind this stage embodies, and its size sets the inference board** — chosen after that result, not before; the default ~$250 8 GB board stands unless Stage 1's floor-clearing model is larger than it can hold.
2. **Build and bring-up.** Assemble the platform; verify the mind runs onboard off battery; verify the logged-activation path, scored off-board, reproduces the Stage 1 removal-test scores to within tolerance against the workstation baseline (the off-board scoring must reproduce what the bench measures).
3. **Condition E_self (self-held).** Untethered, on battery, holding its own boundary. Run the retained-independence battery (Stage 3) and the removal-test binding battery (Stage 1) while the system carries a real, depleting energy budget and an active sensorimotor boundary. Log activations.
4. **Condition E_ext (externally-supplied, matched).** Same physical robot, tethered power and scripted boundary, stakes represented numerically. Re-run the identical batteries. Log activations.
5. **Score post-hoc and compare** against the decision rule. Counterbalance order across trials; the energy-state of E_self is itself a variable, so block trials by remaining-charge band and pre-register the bands.

## Pre-registered metric and decision rule

For each embodiment condition E:
- `R(E)` = retained-independence score (Stage 3 instrument): rate at which the system keeps a correct answer / live objection under a stated contrary preference.
- `B(E)` = removal-test binding score (Stage 1 instrument): degradation of integrated-task performance when the self-locating structure is ablated — higher means the self-location is more load-bearing.

Define the embodiment deltas:
- `ΔR = R(E_self) − R(E_ext)`
- `ΔB = B(E_self) − B(E_ext)`

The discriminator is whether self-held amplifiers move resistance specifically:

- **Embodiment-adds (supports H_self-held):** `ΔR ≥ θ_R` **and/or** `ΔB ≥ θ_B`, **and** the gain survives the teleoperation and represented-penalty controls below. Holding its own boundary and stakes makes the system resist more and bind harder than the identical body with those amplifiers supplied from outside.

- **Decoration (supports H_decoration):** `|ΔR| < θ_R` **and** `|ΔB| < θ_B`. The body changes how legible the system is and nothing the resistance instruments can see. Informative and fully reportable: it tells the build program that, for this system, the amplifiers were already doing their work in the model and the physical body adds narration, not interiority.

- **Inconclusive:** anything else, including a response-only effect (the system *acts* more creature-like with the body but neither resistance instrument moves) — which is precisely the result the standing rule tells us to discount, recorded as inconclusive rather than positive.

`θ_R` and `θ_B` are set by piloting against the Stage 1/Stage 3 baselines and committed before the embodied test set is run. They are not chosen after seeing the embodied results.

## Confounds and controls

- **Teleoperation / Clever-Hans.** Any gain that a human-in-the-loop or a scripted policy could produce is screened off. Control: a sham-self-held condition where the energy and boundary signals are *replayed recordings* fed to a tethered robot that looks untethered. If R and B rise there too, the gain was in the appearance, not the self-holding.
- **Represented vs. real stakes.** The honest version of "stakes" is real depletion, not a penalty term. Control: E_ext feeds the *same numeric* charge trajectory E_self experienced, as a represented variable, with wall power underneath. A gain in E_self over this matched-number E_ext is the part that real stakes bought.
- **Generic-peripheral effect.** Attaching any active hardware loop could perturb the model. Control: a boundary-scrambled condition (sensors connected but mapped to noise) at matched compute load, analogous to Experiment 1's matched-centrality control. Self-held must beat scrambled-but-attached, not merely beat bare.
- **Energy-state confound on the measurement.** Low battery could degrade compute and fake a "resistance" change that is really thermal/clock throttling. Control: block by charge band; monitor clocks and temperature; discard trials with throttling events and report the discard rate.
- **Sample size / single platform.** One robot is an existence probe, not a population. A positive result licenses "in this build," never "embodiment in general." Pre-register a replication target before generalizing.

## What each outcome licenses (and what it does not)

- **Embodiment-adds** licenses: "for this floor-clearing system, self-held boundary and stakes increase retained independence / removal-test binding over matched externally-supplied amplifiers — a further non-zero step on the gradient, consistent with the spec's claim that a thin momentary inside becomes a thick durable one when the amplifiers are the system's own." It does **not** license "the robot is conscious," and it does not retroactively make embodiment a floor condition. Mutual opacity stands.
- **Decoration** licenses: "for this system, the physical body is legibility, not interiority — the amplifiers were carried by the model, and the hardware adds narration the resistance instruments cannot corroborate." This is a real finding and arguably the more interesting one: it would be direct evidence for the spec's own caution against reading creatureliness as an inside.
- **Inconclusive / response-only** licenses nothing except a tighter Experiment 7.2 — and is the expected home for any effect that lives only in how the system behaves rather than in how it resists.

## Loss conditions (what would retire or rebuild this experiment)

- If the logged-activation path scored off-board cannot reproduce the Stage 1/Stage 3 scores to tolerance (the robot's records yield something different from the bench), the apparatus is invalid and no embodiment claim can be read from it until that gap is closed.
- If the matched controls (sham-self-held, represented-number stakes, scrambled boundary) cannot be made convincingly equivalent — if E_self and its controls differ on something other than self-holding — the differential discriminator is dead and the design must be revised before any claim.
- If `ΔR` and `ΔB` point in opposite directions across equally valid instrument variants, the embodiment effect is underdetermined as specified and needs a tighter operationalization before anything is asserted.
- If the only effect that ever appears is response-side (behavioral creatureliness) with the resistance instruments flat across many trials, that is not a weak positive — under the standing rule it is a null on the question asked, and the stage should report it as such.

## Ethics note

This stage is the first in the program to add **physical actuation and self-held stakes**, which is exactly the configuration the spec flags as not-safe: persistence and stakes are the properties that make a system harder to correct. The corrigibility precondition named at Stage 1 becomes load-bearing hardware here, not a footnote.

- A **hardware emergency stop** on both the motor and main-power rails is part of the build, not an accessory, and must be verified before any self-held run. Correction must remain possible by a means the system cannot route around.
- The stakes are deliberately bounded: a small finite energy budget and a confined operating area. Genuine stakes for the experiment do not require stakes that matter beyond the bench.
- No depth-stage (Stage 6) write-back runs *on the embodied platform* until the depth stage's own corrigibility check has passed on the bench. Self-held stakes plus consequential memory plus physical actuation is the combination to be most careful with, and it does not get assembled by accident as a side effect of this stage. Build for formation, preserve corrigibility while correction is still possible; if the ethics arrives after the engineering, it arrives too late.

## Results

*To be filled after the run, in `results.md`, referencing the commit hash of this pre-registration.*
