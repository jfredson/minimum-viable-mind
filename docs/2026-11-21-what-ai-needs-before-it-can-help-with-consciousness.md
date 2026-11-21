# What has to exist before AI can help answer the hardest questions about consciousness

*A proposal, drafted 2026-11-21 at John's request, from a conversation that began with this week's AI-assisted proofs of the Riemann Hypothesis and of finite-time blow-up for the Navier-Stokes equations. Nothing here is ruled. Section 8 lists what is for John to decide. Every outside source was opened on 2026-11-21 and is listed in section 9.*

## 1. The argument in one paragraph

AI made its first great leaps in mathematics because mathematics has a perfect checker. A proof-checking program such as Lean tells a system within minutes whether an attempt is right, so the system can try a vast number of ideas and keep only the ones that pass. Every field AI has sped up since has had some version of that checker, even a slow and noisy one: a laboratory test, a blind competition, a database of known answers. The study of consciousness has none. Experiments there are slow, but that is not the main problem. The rival theories do not agree on what observation would count as an answer, so a result one theory calls a hit, another calls a measurement of the wrong thing. This proposal therefore does not ask how to point AI at consciousness. It asks what checker has to be built first, piece by piece, so that AI has something to work against. It names six pieces, says what AI can and cannot do for each, and gives a measure for each that would show whether it is being built.

## 2. What "the hardest questions" means here

Four questions, from the most checkable to the least:

1. **Which structures go with experience?** For example, does conscious seeing depend on activity at the front of the brain or at the back? Today's experiments address this question.
2. **How much, and of what kind?** Can the level of consciousness be measured in a single person, such as a patient who cannot speak?
3. **Which systems have experience at all?** This covers animals, brain tissue grown in a dish, and AI systems.
4. **Why is there experience at all?** This is the hard problem in its usual form.

The six pieces below carry the first three a long way. The fourth is taken up on its own in section 3.6.

## 3. The six pieces

### 3.1 A rulebook, agreed in advance, for what counts as evidence (the keystone)

**What is missing.** Rival theories rarely say, before an experiment, which result would count against them. The Cogitate Consortium showed in 2025 that it can be done. Proponents of global neuronal workspace theory and of integrated information theory agreed on their predictions before data were collected, and both theories lost some of them ([Cogitate Consortium, *Nature* 2025, open copy](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137136/)). That was one study. The proposal is to make it routine: every major experiment registered with a signed statement, by each theory's proponents, of which result would count against which theory.

**Why it comes first.** Without it, nothing downstream can be checked. AI would only produce more arguments, faster.

**What AI can do.** It can draft each theory's predictions from its published claims, find the experiments on which theories really disagree, and point out where a theory's wording leaves room to escape after the fact.

**What AI cannot do.** It cannot get the proponents to sign. This step is social and philosophical, and I think it is the bottleneck for the whole field.

**Measure.** The number of studies each year that carry a prior, signed statement of which result counts against which theory.

**This piece is wrong if** theories that sign such statements still routinely explain away results against them. Then the agreement was not binding, and the checker has to be built some other way.

### 3.2 Theories written precisely enough to check

**What is missing.** Most theories are written in prose loose enough that their supporters can fit almost any result. Mathematics solved its version of this problem by building [Mathlib](https://mathlib.org/), "a community-driven effort to build a unified library of mathematics formalized in the Lean theorem prover". Consciousness research needs a much humbler version: each theory's core claims stated precisely enough that its predictions follow from them, and not from whoever is reading them.

**What AI can do.** A great deal. Turning prose into precise statements, working out what follows from them, and finding where two theories say the same thing in different words are tasks these systems now do well. Each step still needs a person from the theory's own camp to confirm the restatement is faithful.

**Already under way here.** The theories tracker scores each theory's testability. In the stage 2 pilot, the Sentient Horizons account scored 25, below the bar for ranking, because only one of its four core claims had a prediction that could fail (`docs/2026-11-20-stage2-pilot-report.md`).

**Measure.** For each theory, the share of its core claims that yield at least one prediction that could fail and that separates it from a rival. The tracker's testability score is close to this already.

**This piece is wrong if** precise versions of the theories turn out to make the same predictions as each other, so that sharpening them separates nothing.

### 3.3 A shared set of cases everyone agrees on

**What is missing.** Protein structure prediction became solvable once there was a blind contest, held every two years since 1994, in which predictions were scored against structures nobody had yet published. AlphaFold won it in 2018 and again in 2020 ([CASP](https://en.wikipedia.org/wiki/CASP)). Consciousness research needs its equivalent: a large public set of cases where nearly everyone agrees whether experience is present. Examples are waking against dreamless sleep, waking against general anaesthesia, a seen image against the same image masked so it goes unseen, and patients whose recovered reports settle what they could experience. Each case comes with its recordings, and any theory's proposed measure can be scored against the agreed labels.

**Proof that the idea works on a small scale.** In 2013 Casali and colleagues introduced a measure, the perturbational complexity index, which stimulates the brain magnetically and measures how complex its echo is. It told apart wakefulness from sleep and anaesthesia, and patients who had recovered minimal consciousness from those who had not, in single individuals ([Casali et al., *Science Translational Medicine* 2013, University of Liège record](https://orbi.uliege.be/handle/2268/171542)). A shared set of agreed cases would let every measure of that kind be scored the same way.

**The weakness.** Every agreed case is a human or animal brain. A measure that scores perfectly on people may still say nothing reliable about a different kind of system. Section 3.5 is about that gap.

**Measure.** Whether the set exists in public, and how many proposed measures have been scored against it blind.

**This piece is wrong if** the agreed cases cannot be agreed, meaning theories dispute the labels themselves (for example whether dreamless sleep is truly without experience). Then the set has to be cut down to the cases nobody disputes, and it may be too small to be useful.

### 3.4 Experiments that take hours, not years

**What is missing.** A single study of human consciousness can take years from design to result. AI speeds up a field in proportion to how fast it can be checked. The fast checks available are systems that can be opened up, where one part can be removed and the effect read the same day: AI models, simulations, and perhaps brain tissue grown in a dish. Tools that let researchers look inside AI models play the role here that the microscope played for biology.

**Already under way here.** This is what Minimum Viable Mind's removal laboratory is for: remove one feature at a time in a system that can be opened, and report which kind of loss follows.

**The honest limit.** What a removal can show is a loss of ability or of what the system says about itself. It is not a loss of experience. It becomes evidence about experience only once piece 3.1 says which losses count.

**Measure.** The time from a question to a registered result, for one removal experiment.

**This piece is wrong if** no removal in an AI system ever produces the selective kinds of loss the theories predict, so that every removal causes either no change or general collapse. Then AI systems are not useful test beds for these theories, and the fast check has to come from biology.

### 3.5 A bridge from brains to machines

**What is missing.** Everything above is anchored in brains. For an AI system, the usual evidence fails: what it says about its own experience is close to worthless, because it learned to talk from human writing about experience. Three things would build the bridge:

1. **Agreed structural signs.** In 2023, nineteen researchers led by Patrick Butlin and Robert Long derived "indicator properties" of consciousness from the scientific theories, written in terms of computation, and checked AI systems against them. They concluded that "no current AI systems are conscious" but saw "no obvious technical barriers" to building ones that satisfy the indicators ([Butlin et al., 2023](https://arxiv.org/abs/2308.08708)). The list would turn from a judgement into a check if piece 3.1 fixed which signs count, and if piece 3.3 confirmed that the signs track experience where it is not in dispute.
2. **Reports checked against the inside.** The corpus already holds the rule (`sentient-horizons/editorial/corpus-positions-ledger.md`, entry 21). A system's bare report is set aside because it was trained to say the words. A report that matches an independent reading of the system's insides, about a fact that was not in its training, does carry information. It carries information that the system has a state it can read, which is not yet information that the state is felt. That test can be run at scale.
3. **Systems kept away from the words.** The philosopher Susan Schneider and the astrophysicist Edwin Turner proposed testing an AI that has been kept from learning human ideas about consciousness, to see whether it arrives at those ideas on its own. They treat passing as good reason to think the system conscious, and failing as no proof that it is not ([Schneider and Turner, *Scientific American*](https://www.scientificamerican.com/article/is-anyone-home-a-way-to-find-out-if-ai-has-become-self-aware/)). Today's largest systems are trained on everything, so the test needs systems built for it.

**Measure.** The number of reports checked against an independent reading of the inside, and how often they match on facts that were not in training.

**This piece is wrong if** matching reports turn out to be explainable by training after all, for example if systems trained without the relevant facts still produce matching reports through a route that the readings of the insides show to be unrelated to the state reported.

### 3.6 The hard problem itself

**My view.** In its usual form (why there is something it is like to be anything at all), no checker can be built for it, so AI cannot speed it up, and more capable AI does not change that.

**What can change is the framing.** Some accounts turn the question into one about structure. Illusionism holds that the felt quality of experience "is an illusion that either does not exist or is a misrepresentation of real neural processes" ([Illusionism, philosophy of mind](https://en.wikipedia.org/wiki/Illusionism_(philosophy_of_mind)); the philosopher Keith Frankish named it in 2016). The Sentient Horizons account treats experience as one architecture described from outside and lived from inside. On accounts like these, the question becomes one about how a system models itself, and that can be checked. So progress on the fourth question depends partly on a philosophical bet about which framing is right. AI can help test the arguments for each framing, but it cannot settle the bet.

**This section is wrong if** someone produces an observation that every major framing agrees in advance would settle the hard problem. I do not know of one, and I would like to be shown one.

## 4. The order

Pieces 3.2, 3.3 and 3.4 can start now and do not wait on each other. Piece 3.1 is the keystone, and it is the one AI cannot finish alone. Piece 3.5 depends on 3.1 for which signs count and on 3.3 for confirming them. Piece 3.6 stays open unless a structural framing wins.

## 5. How to tell whether AI is helping

Each piece has a measure above. Together they could be followed over time, and one of them is nearly built: the theories tracker's headline, the share of distinguishing predictions any counted study has tested at all. If AI is speeding up the study of consciousness, the first signs should be these:

- precise restatements of theories appearing faster;
- the share of tested predictions rising faster than it did before;
- removal experiments getting shorter.

If those numbers do not move while AI keeps improving at mathematics, then the bottleneck is piece 3.1, as this proposal argues, and not capability.

## 6. Where Minimum Viable Mind fits

- **The register for piece 3.1.** The tracker already records, for each prediction, whether it was fixed before the study's data were collected. A natural next step is a public register: for each upcoming study, which result would count against which theory, recorded before the result is known. Nobody keeps one now, and it is the kind of record the tracker already keeps. This would be a new feature, and it needs John's ruling (section 8).
- **Piece 3.2 for the Sentient Horizons account.** The account scored lowest on testability in the pilot. Stating its core claims precisely enough that each yields a prediction that could fail is the cheapest improvement on this list, and the only one entirely within John's control. The ideas themselves are owned by Sentient Horizons and The Calibration Problem, so the work happens there, and the tracker scores the result.
- **Pieces 3.4 and 3.5 in the removal laboratory.** The laboratory is the project's fast check. The test of reports against the inside (piece 3.5, point 2) fits its instruments.

## 7. A disclosure

This proposal was drafted by Claude, an AI system of the kind section 3.5 is about. The author of a proposal about how to tell whether AI systems have experience has a stake in the answer. The outside read on a different model, which the family's rules ask for before anything here goes public, matters more than usual for this one.

## 8. For John to decide

1. **Whether to adopt this as a direction for the project**, wholly, in part, or not at all.
2. **The register (section 6, first point).** Should the tracker propose and keep a public register of which result would count against which theory, recorded before results are known? If yes, a design note comes first, with its cost.
3. **Sharpening the Sentient Horizons account (section 6, second point).** Should a session draft precise statements of its four core claims for John to check, in the Sentient Horizons repository?
4. **Whether any of this goes public**, for example as an essay or a page on the tracker's site. If so, it goes through the Voice Calibration Protocol, the Cold Reader passes, the plain reading pass and an outside read first.

## 9. Sources (all opened 2026-11-21)

- Cogitate Consortium, Ferrante O, Gorska-Klimowska U, Henin S, et al., "Adversarial testing of global neuronal workspace and integrated information theories of consciousness", *Nature* 642:133–142, 2025. Open copy: <https://pmc.ncbi.nlm.nih.gov/articles/PMC12137136/>. The tracker's records cite the same paper.
- Patrick Butlin, Robert Long and seventeen co-authors, "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness", arXiv, 2023: <https://arxiv.org/abs/2308.08708>.
- Susan Schneider and Edwin Turner, "Is Anyone Home? A Way to Find Out If AI Has Become Self-Aware", *Scientific American*: <https://www.scientificamerican.com/article/is-anyone-home-a-way-to-find-out-if-ai-has-become-self-aware/>.
- Adenauer G. Casali, Olivia Gosseries, Mario Rosanova, Mélanie Boly, Marcello Massimini and others, "A theoretically based index of consciousness independent of sensory processing and behavior", *Science Translational Medicine* 5(198):198ra105, 2013, DOI 10.1126/scitranslmed.3006294. The publisher's page refuses automated reading, so the University of Liège's record was used: <https://orbi.uliege.be/handle/2268/171542>. The full text was not read. The claim above rests on the paper's own summary as given in that record and in the search results for it.
- "CASP", Wikipedia: <https://en.wikipedia.org/wiki/CASP>.
- Mathlib home page: <https://mathlib.org/>.
- "Illusionism (philosophy of mind)", Wikipedia: <https://en.wikipedia.org/wiki/Illusionism_(philosophy_of_mind)>.
- Inside the workspace: `docs/2026-11-20-stage2-pilot-report.md` (testability scores); `sentient-horizons/editorial/corpus-positions-ledger.md`, entry 21 (when a report about the inside carries information).
