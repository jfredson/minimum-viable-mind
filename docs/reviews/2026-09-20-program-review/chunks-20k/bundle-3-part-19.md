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
