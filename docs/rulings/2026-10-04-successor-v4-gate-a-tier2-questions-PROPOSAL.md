# Proposal for John, addendum: six more questions, from the outside reviews of proposal version 4 (pages 7 to 12)

*Written 2026-10-06 (Pacific) by a Claude Code session in its own worktree,
on branch `gate-a-v4-tier2-dispositions`. **This is a proposal, not a
ruling. Everything in it is PROPOSED.** It adds to the six pages already
with you (`docs/rulings/2026-10-04-successor-v4-gate-a-questions-PROPOSAL.md`),
and can be ruled in the same sitting. Nothing was rented or spent: $0.*

**What it covers.** Two outside reviews came back. Gemini's nine findings
(G1 to G9) all repeat the inside review's, and asked again it found nothing
new. ChatGPT's thirteen (A1 to A13) repeat four inside findings and add
nine: one fatal, five serious, three worth-noting. The full drafts, with the
exact registration text, are in
`docs/rulings/2026-10-04-successor-v4-gate-a-tier2-dispositions-PROPOSAL.md`.
This addendum asks only what is yours.

**Before relying on it.** This session ran three $0 checks from committed
records (`docs/2026-10-06-gate-a-v4-tier2-dispositions-measurements.md`,
method committed first). Nothing here has been checked by another session
yet; that check is owed before you rely on a number.

**Three questions go to whether the experiment is still worth running:
pages 10, 11 and 12.** They are marked ⚑.

---

## The one-page index

| Page | Question | Recommendation (yours to overturn) | Confidence |
|---|---|---|---|
| — | **The fatal one (A2): the final procedure that withholds bad readings and assigns the outcome has never run end to end.** Not a question, but you should know: **it is not closed.** *Corrected 2026-10-06:* the procedure does exist, in the frozen successor code merged on 2026-10-05, and it has run end to end on the toy (landing on "substrate not a testbed", not the fifth term). What remains: change it to the rules you are about to rule, run made-up failure cases through it, and have another session check it, at $0 | Do that straight after you rule pages 5, 7, 8 and 9 | high |
| 7 | When different seeds pass different conditions, does the arm pass? (A10) | **No: two seeds must each pass everything.** No toy verdict changes | moderate |
| 8 | The no-transplant check would refuse good models (A9). Keep it as a veto? | **No: report it; check the pairing directly instead** | moderate |
| 9 | If the free model fails its learning gate but the two built models separate, is that "substrate not a testbed" (R3) or "metric validated, degree not read"? And what if the middle model misses its band? (A10) | **The latter, with the reason**; the middle model's miss is reported, not a change of outcome. Changes page 5's table | moderate |
| 10 ⚑ | A $0 "decoy" test of whether the read can be fooled by an unused copy of the owner's marker (A6) | **Yes, run it before deciding to register** | moderate |
| 11 ⚑ | The outcome words claim more than the experiment shows (A13). Add a fixed scope phrase, or rename the terms? | **Fixed scope phrase**; renaming is a close second | low |
| 12 ⚑ | The review's kill case: is the narrow result worth the remaining spend? | **Decide after page 10's test** | moderate |
| — | Wording only: control 6 does not tell "who is acting" from "the answer" (A7); the toy is development evidence (A8); no verdict is not absence (A11); the uncertainty is for the raw difference only (A12) | Accept all four as drafted | high |

**What "yes on all" adds before registration:** building and checking the
decision procedure to your rulings, its failure-case run and check (A2),
and the decoy test and its check (page 10). Both
$0, on the laptop. Everything else is wording in version 5.

---

## Page 7 — split seeds (A10)

**The question.** Today each gate condition is counted across seeds
separately: two of three for learning own-directed, two of three for
named-other, and so on. So an arm can pass when every condition passes on
two seeds but **no single seed passes all of them**. Should a seed have to
pass everything to count?

**The facts.** The rehearsal's gate code counts conditions separately
(MEASURED). *Corrected 2026-10-06:* the frozen successor code is partly
joint: learning own-directed and named-other must pass on the same seed,
but the free model's channel-removal check is counted separately, and a
seed that failed the gate can still be one of the two that read. On the
toy no verdict changes either way: arms T, C and M pass every condition on
every seed, and the free model fails named-other on two seeds under both
rules.

**Recommendation: yes, a seed counts only if it passes every condition and
every check that withholds a reading.** The reading is about particular
trained models; a claim resting on three half-qualified models is weaker
than it looks. *Confidence: moderate.* **Alternative:** keep separate counts
and say plainly that the arm-level claim is weaker. *Changes your ruling 6
of 2026-10-03 (late evening), and the gate rows of section 9.*

## Page 8 — the no-transplant check (A9)

**The question.** Before reading, the design checks that an untouched
model lands on the donor's answer about as often as a formula says, and
refuses to read if it is more than 0.018 off. Keep that as a veto?

**The facts (MEASURED).** The reviewer read the formula correctly and the
arithmetic holds. The formula assumes the model's mistakes spread evenly
over all seven wrong values. A good model whose mistakes go to **other
agents'** values (the natural mistake for a model learning who it is) lands
well outside the allowance at any accuracy below about 0.9: on 800 pairs it
would be refused 99% of the time at 80% accuracy. Meanwhile, near the
learning bar, the check catches a genuinely broken pairing only 56% of the
time. The toy's models happened to spread their mistakes evenly, which is
why they passed.

**Recommendation: report the figure, stop using it to refuse a reading, and
test the pairing directly** in the episode generator's self-test, which
cannot refuse a good model. The reading itself already uses the measured
rate, so it does not need the check. *Confidence: moderate.*
**Alternative:** keep the veto as a stated restriction on which models can
be read. *Changes the Gate C ruling RT-222.*

## Page 9 — which outcome wins, and the middle model's band (A10; changes page 5)

**The question, part 1.** The free model is the one most likely to fail its
learning gate (the design's own honest prior). If it does, and the two built
models still learn and separate, is the outcome "substrate not a testbed"
(R3) or "metric validated, degree not read: failed its gate on learning"?
Version 4 calls the toy the second, although the toy's free model failed
its gate. Page 5's table, as drafted, would make it the first.

**Recommendation: the second.** R3 is for the built models failing to
learn; once they have learned and separated, the free model's failure is a
fact about the free model, which the fifth term with its reason states.
This keeps version 4's description of the toy true and matches how the
rehearsal code already treats it. *Confidence: moderate.*
**Alternative:** R3 for any of the three, as page 5 drafted; stricter, but
then the toy and the most likely registered result are both R3.

**Part 2.** If the middle model (arm M) reads but outside its predicted 0.3
to 0.7, or more than 0.10 from its reference: **recommendation: no change of
outcome term; the report says so in the same sentence, and the free model is
placed against the two built models only.** *Confidence: moderate.*

## Page 10 ⚑ — a $0 decoy test (A6)

**The question.** The read looks for where the model keeps "which marker
is mine". If a model also kept an easily read but **unused** copy of it,
the read could pick the copy; transplanting the copy would do nothing; and a
model whose ownership is actually separable would read as fully entangled.
Nothing in the design rules this out, and the high anchor's "entangled"
status rests on the instrument itself failing to find a piece that moves
the action. Should we test it before registering?

**The test.** Take the separable toy model, add extra coordinates holding
an exact unused copy of the owner's marker, and run the registered
nomination and reading unchanged. If it still reads near 0, the read finds
the slot that is used. If it reads near 1, the instrument can be fooled this
simply, and "metric validated" means much less. $0; a few hours on the
laptop; method first; another session checks it. It is a constructed
stand-in, not a trained model.

**Recommendation: yes, run it, and decide page 12 with its result.** The
wording changes to the registration happen either way. *Confidence:
moderate.* **Alternative:** register with the weakness named and no test.

## Page 11 ⚑ — the outcome words (A13)

**The question.** "Metric validated", "degree read" and "known-high anchor"
will be read as a scale of integration. The experiment shows something
narrower: how two transplant procedures compare at chosen sites, on built
systems. Fix the words how?

**Recommendation: keep your terms, and require a fixed phrase beside every
use** ("metric validated **on these constructed systems, for this
intervention procedure**"), in the text, STATUS.md, the paper and in public;
and register the reviewer's table of tempting summaries against what can be
said. *Confidence: low.* **Close alternative:** rename the terms (for
example "metric separates the built anchors"). Cleaner, but it reopens your
ruling of 2026-10-03 on the terms.

## Page 12 ⚑ — the kill case

**The question.** The reviewer's case: the whole spend could separate the
two built models, put the middle one in the middle, and still show only that
the read finds the slot deliberately exposed in the separable model; the
free model could stay unreadable throughout. If that narrow result is not
worth the remaining spend (version 4, section 12, forecasts the whole
successor), stop here.

**Recommendation: don't decide yet. Decide after page 10's test.** Most of
what the review found can be fixed in wording or at $0. What cannot is
whether the read can be fooled by an unused marker, and the decoy test
answers the sharpest form of that for nothing. If it is fooled, this
session would recommend stopping or redesigning before registration; if it
is not, the narrow result is still a delivered, validated-on-its-terms
instrument, which is what the December-result roadmap set out to get.
*Confidence: moderate.*
