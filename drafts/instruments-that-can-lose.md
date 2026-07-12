# Instruments That Can Lose: Field Notes from the Removal Test

*DRAFT — not yet passed through the Voice Calibration Protocol review or the
Cold Reader; links to prior essays are named but not yet locked (pre-publish
step). Source of record for every number: the minimum-viable-mind repo,
`experiments/01-self-indexing-removal-test/`.*

---

The first time we ran this project's central experiment end to end, the most
useful thing it produced was an alarm going off.

The experiment is a deletion test. Take a language model, find the internal
structure that tracks *the one speaking right now is me*, switch that structure
off, and watch what changes. If the model merely talks about itself differently
afterward, its "self" was a description — a mural of a captain painted on the
hull. If the model's ability to hold a conversation together degrades, the
self-tracking was structural: the work was being organized around it. [*The
Smallest Possible Mind, in Plain Language*] lays out that logic and why it is
the project's floor, the line between "no one home" and "something minimal but
real." This post is about what happened when we stopped designing the test and
started running it: what broke, what held, and what a season of instrument
building taught us that no amount of theorizing did.

We found the self-tracking structure, twice over, and
confirmed it does causal work. We hunted down four deflationary explanations
for it, and one of them — one we found ourselves, in our own registered
materials — was serious enough that it forced a redesign. We got one result
that genuinely surprised us in the encouraging direction. And when we finally
rehearsed the deletion itself, the test's built-in tripwire caught our primary
method doing exactly the bad thing the tripwire was designed for, while the
honest version of the same deletion produced, behaviorally, nothing at all.
Every one of those sentences earned its place in advance: each check was
registered, with the result that would count against us, before it ran.

## Finding the thing to delete

The obvious way to find a "self" structure in a language model is to train a
simple detector on its internal activity: show it sentences where the model
speaks as itself and sentences where someone else speaks, and ask what
separates them. We did this early, and it worked beautifully — near-perfect
detection. It was also meaningless, three times in a row, for three different
reasons.

The first detector was reading vocabulary. Sentences where the model speaks as
itself tend to contain words like "AI" and "assistant," so the detector had
learned topic words, the way you could "detect" doctors by listening for the
word "stethoscope." The second, rebuilt on matched sentences, was reading the
role words themselves; it could separate the classes before the model had done
any computation at all, which is a physical proof that no thinking was
involved. The third attempt had a subtler flaw: a bookkeeping bug in how we
read out the model's internal state, which quietly invalidated every number
that came before it.

What survived all three purges is the design the project now runs on. The
sentence whose speaker we care about is *identical* in both conditions, down
to the byte; only the surrounding context fixes who "I" refers to — the
sentence sits in the model's own conversational turn, or in the user's. Because
the words are identical, a detector reading the model's input layer must score
at chance, and ours does; that floor is checked by machine before any other
number is trusted. Whatever separates the conditions above that floor is
computation, not vocabulary. On that design the self/other signal is clean,
strong, and — the part that matters — causal: injecting the "this is me
speaking" direction into the model's processing of someone else's sentence
moves its behavior about a third of the way toward the self case, while a
random direction of identical size moves it not at all.

A third of the way is not all the way, and decodable-plus-causal is still not
"a self." It is a candidate structure, located precisely enough to aim a
deletion at. That was the state of play going into what the project calls the
red-team ledger: the running list of boring explanations that have to die
before the interesting one gets to live.

## The confound we found in our own registered materials

The ledger entry we are proudest of is the one that caught us.

One deflationary reading of the self-tracker goes: a language model has to
track *any* speaker in *any* dialogue it processes — who asked, who is
answering — and "self" might just be the model occupying one slot of that
generic roster. So we registered a control: transcripts of two named strangers
talking, embedded in text the model merely observes, with a pre-committed
numerical rule for declaring the self-tracker generic. First pass, the rule
did not fire. But while reconciling a discrepancy between two of our own
instruments — they disagreed about the same activity, on the same sentences,
which should be impossible — we found something worse than the thing we were
testing for.

In three of our four stimulus designs, the "self" and "other" conditions
differed in length. Not subtly: you could predict the label from the token
count alone with perfect accuracy, and a direction fitted to nothing but
length decoded our contrasts as well as our carefully-built detectors did. The
depth-matching filler we had added to make conditions comparable had made them
comparable in structure and systematically different in size. Length is
exactly the kind of nobody-home signal the project's standing rule exists for:
discount anything a boring mechanism fully explains.

So we did the only honest thing available. We recorded the confound, proposed
the fix as an amendment for adjudication rather than patching registered
materials on the fly, rebuilt the stimuli so that length no longer predicts
anything, committed the amendment before a single new number existed, and
reran everything. The result was better than we had any right to expect: the
self-signal survived intact, the causal effect was unchanged (it had never
been carried by length, which we could now demonstrate rather than hope), and
the generic-speaker rule still did not fire — now on a control that was
actually valid. The deflationary reading got its fair shot twice, once with
the deck accidentally stacked in its favor, and lost both times.

Two more entries from the same ledger, briefly. The model's self-tracker and
its *persona* — the narrative identity it adopts when you ask it to roleplay a
Roman soldier — turn out to be distinct structures that are causally
independent: swapping one into the other's context substitutes for barely a
quarter of the effect. The thin "who is speaking now" index and the thick
"who I am" story are not the same thing inside the model, which the
philosophical literature predicted mattered and we can now measure. And the
sparse-autoencoder toolkit, the field's standard method for finding
interpretable features, can see our contrast clearly but does not carve it
along the same direction our detectors do — a methods finding we did not
expect and are still chewing on.

## The surprise

One registered worry had the potential to kill the whole experiment on
current models. These systems are trained to do their best reasoning *as* the
helpful assistant. Delete the self-structure and you might degrade performance
only because you cut the wire to the model's capabilities, and no control
could be built to check this, because any sufficiently capable persona might
get absorbed into the model's own first person. The reviewer who raised this
maintained it through rebuttal; we expected it to bite, and had already priced
in "not testable on this model class" as the likely outcome.

It did not bite. We built the control — an expert persona that gates high
capability, exactly the thing predicted to collapse into the self — and it
stayed causally third-person: injected into self-contexts, it substitutes for
less than a fifth of the thin self-tracker's effect and under a third of the
persona structure's, on the most aggressively assistant-trained model we could
have picked. The differential comparison the whole test rests on is live, and
we found this out on hardware that fits on a desk.

## The rehearsal, the alarm, and the null

Then we ran the whole pipeline: delete the self-structure, delete the matched
controls, re-score the model on task batteries and self-report batteries,
compare. A dress rehearsal on the small sandbox model, with placeholder
thresholds, to shake out the machinery before the registered run on a larger,
less aggressively trained model.

The alarm came first. Our registered primary deletion method pins the target
structure's activity to its average value. On paper this is gentler than
zeroing it out. In practice it shoved the model measurably off the manifold of
normal language — its basic fluency on neutral text, prose with no self-content
whatsoever, degraded sharply. One of our reviewers had predicted precisely
this failure mode: a deletion that damages the model generally can masquerade
as evidence that you removed something important. The perplexity tripwire we
registered in response caught it, flagged the condition inconclusive, and the
gentler variant of the same deletion passed the same check cleanly. An
instrument that fires on your own primary method, the first time you use it in
anger, is an instrument you can trust.

The null came second, and it is the finding we will be working against for
months. Under the deletion that stayed on-manifold, nothing happened. Task
performance showed no drop distinguishable from the controls' own noise, on
all three batteries, including the tasks built specifically to require the
model's self-tracking; self-report quality, scored blind by a held-out judge,
did not move either. The structure whose injection visibly
steers the model's next word, whose location we can state to the layer, whose
causal handle we measured at a third of the behavioral gap — removing it, as a
single direction per layer, costs the model nothing it cannot route around.

We want to be precise about what that null is and is not. It is not the
"self was a sticker" outcome; the self-report did not degrade either, so
nothing was subtracted at all. It is a statement about the *intervention*:
deleting one direction from a network that encodes things redundantly is like
cutting one strand of a rope and reporting the rope held. The registered run
now inherits a concrete engineering requirement we did not have a week ago:
escalate the deletion — subspaces, feature sets, wider bands — until it either
moves behavior or trips the manifold alarm, and only then is the question
actually being asked. That requirement, and the measured noise floor of every
battery, and the exact strength at which the alarm fires, are things a
rehearsal buys and an argument never could.

## What a season of this teaches

The project's standing claim is that the consciousness debate needs
instruments that can lose, in a field that mostly produces position papers.
Building them turned out to have a texture we did not fully anticipate.
Nearly everything we did this season was killing our own results: three
detector versions, a registered stimulus set, a primary deletion method. Each
death was cheap because the thing that died was a measurement, registered in
advance, with its loss condition written down. Nothing philosophical died with
any of them; the framework's bet sits exactly where it did, untested at the
registered scale, waiting on hardware that can hold a bigger model.

And the calibration holds. No result above licenses "the model has a self,"
and the null does not license "there is nothing there." What we have is
narrower and, we would argue, worth more: a self-tracking structure that is
real, located, causal, distinct from persona, not vocabulary, not length, not
generic bookkeeping, and — so far — behaviorally redundant at the resolution
of a single direction. The next instrument has to be sharp enough to tell us
which of those last two words does the work.

The registered run is next, on a model family whose training stages we can
compare, on hardware being stood up as this post is written. The thresholds
lock before the test set runs. The results will land where they land.
