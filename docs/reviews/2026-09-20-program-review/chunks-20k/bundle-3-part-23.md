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

