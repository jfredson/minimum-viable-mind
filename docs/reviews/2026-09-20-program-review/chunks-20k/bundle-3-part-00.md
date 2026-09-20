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

