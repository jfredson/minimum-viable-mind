# The paper's readiness checklist (2026-10-18)

*Why this exists. On 2026-10-18 John held the outside-reader step: "I'm not
sure I have the confidence in it yet for that"
(`docs/rulings/2026-10-18-outside-reader-held-ruling.md`). He approved this
plan for getting the paper to the point where sending it feels right. The
plan is the fifth master session's for the tracker sites; this file writes it
down. The paper is `drafts/paper-removal-test-nature-draft.md` (version 0.3,
with his rulings of 2026-10-18 on the title, the router paragraph, the
Discussion and the spelling, pull request 190).*

*The steps run in order. Steps 2 and 3 can start without John, but only once
the battery rehearsal of entries 1 and 2 has reported and its result is in
the paper, and pull request 190 has merged. Steps 1, 4 and 5 are John's.*

| Step | What | Whose | Cost | Done means |
|---|---|---|---|---|
| 1 | John reads the paper end to end | John's | $0; about two hours of his reading | He has a list of every sentence he would not defend aloud to an expert, and each is fixed or cut |
| 2 | Mock peer review | sessions; then an outside model | $0 for the inside reviews; about $1 to $3 by API for the outside model | Three referee reports and an outside one exist, and every major point is fixed or answered in a response file |
| 3 | Reproduction from a clean clone | a fresh session | $0; laptop only | Every number in the paper is regenerated from the repository by its own instructions, or the gap is named |
| 4 | A friendly expert before a senior one | John's | $0 | John has chosen a reader and has the reader's comments |
| 5 | A proportionate first venue | John's | arXiv is free; a workshop may charge registration if accepted | John has chosen the venue, after steps 1 to 4 |

## 1. John reads the paper end to end

**What John gets.** A clean reading copy of the paper as it stands after
pull request 190 and the rehearsal's result, as Markdown and as a PDF, with
no review notes or dated notes in the body. Beside it, a one-page guide to
what changed since version 0.2: the relabelled removal test, the two new
results sections, his four rulings of 2026-10-18, and the rehearsal's result.

**What he does.** He reads it end to end and marks every sentence he would
not defend aloud to an expert in the field.

**What follows.** A session that did not write the sentence fixes each one
or cuts it, and a second session checks the changes.

## 2. Mock peer review

**Inside reviews.** Three sessions that never touched the paper each write a
Nature-style referee report, each on one subject: the method; the
statistics; and whether the claims overreach the record. Each report ends in
one word: accept, revise or reject. The reports are filed under
`docs/reviews/`.

**Outside review.** The same is done with an outside model, under the
existing outside-review protocol (`docs/outside-review-protocol.md`). Tier 2
runs by API, the standing method since the ruling of 2026-10-12, with its
cost recorded in the worklog. It is about $1 to $3, going by the Gate A tier
2 pass of 2026-10-09 (about $1.04 for a packet of about 45,000 tokens).

**Done** means every major point is fixed in the paper or answered in a
response file beside the reports. A session that did not write a fix checks
it.

## 3. Reproduction from a clean clone

A fresh session clones the repository into an empty folder. Following only
the repository's own instructions (its README, the experiments' method and
findings files, the committed scripts), it regenerates every number the paper
cites, from the committed records and outputs, on the laptop.

It rents nothing and calls no model. Any number that would need rented
compute or a paid call to regenerate is listed, with what it would cost, and
not run.

**Done** means a filed record of every figure: reproduced, reproduced with a
difference (and why), or not reproducible from the repository (and what is
missing).

## 4. A friendly expert before a senior one

John chooses one of these:

- **Martin Picard**, his brother-in-law, a scientist outside this field. He
  would read for whether the paper would be taken seriously.
- **A draft posted for comment** where researchers in this area read, such as
  the Alignment Forum.

**Done** means John has the reader's comments and has decided which to act
on.

## 5. A proportionate first venue

After steps 1 to 4, John chooses the first venue: an arXiv preprint, or a
machine-learning workshop paper, before a journal of Nature's standing. The
outside-reader approach note (`docs/outside-reader-approach-note-2026-10-17.md`)
stays held until he says otherwise.
