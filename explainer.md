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
