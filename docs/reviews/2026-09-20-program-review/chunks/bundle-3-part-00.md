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
