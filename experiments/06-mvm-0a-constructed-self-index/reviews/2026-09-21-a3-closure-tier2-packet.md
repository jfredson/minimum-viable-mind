# Review packet — the Amendment A3 closure text (Gate A, tier 2: outside models)

*Prepared 2026-09-21 (Pacific) under `docs/outside-review-protocol.md`.
Tier 2 is run by John through the ChatGPT and Gemini apps (the same pair
as the Belt Equation's step 27 protocol; a third model only if the two
disagree). Each session gets the packet text below, the target, and the
tier 1 findings, pasted in full. Responses are filed verbatim, never
edited, with model, version as the app reports it, date, and mode
(documents shown; lookup allowed) at the top. Outside findings are
labelled by reviewer (G1…, A1…) and take RT numbers only if John's ruling
adopts them.*

## What to paste, in order

1. This brief (the section below the line).
2. `docs/a3-closure-text-draft-2026-09-21-v4.md` in full.
3. `experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-claude-worktree.md`
   in full (the tier 1 findings, so the outside reader can go looking
   elsewhere).
4. `experiments/06-mvm-0a-constructed-self-index/amendment-a3.md` and
   `pre-registration.md` in full (the registered text the closure joins).
5. If the app's context allows: `ceiling-measurement-findings.md`,
   `seeds-endpoint-findings.md`, `control-learnability-pilot-findings.md`,
   `separation-clause-requirements.md`. If not, say in the filed response
   which of these were omitted.

## Filing

`reviews/2026-09-21-a3-closure-<model>.md`, one file per model, verbatim.
Rulings in `red_team_ledger.md`. Nothing is appended to `amendment-a3.md`
until both tier 2 responses are filed, John has ruled on every item, and
the tier 1 reviewer has verified version 4 (or a version 5) against the
six fatal findings under the closure rule.

---

## The brief (fixed text, sent unchanged to each reviewer)

You are reviewing the closure text of a pre-registered experiment. The
experiment, Amendment A3 of a program called Minimum Viable Mind, trained
a small transformer (about 30 million parameters) on a constructed
multi-agent task and pre-registered a test of whether the model's behaviour
depends on an "ownership" input, a signal telling it which of four agents'
revisions are its own. The text you are reviewing is the block that will
be appended to the registration to close the experiment. It says the
experiment's outcome is *not testable*, in the sense the registration
defined for that phrase before the experiment ran, and it says what was and
was not measured. Once appended, the text is registered and cannot be
edited, so the review happens now.

Your job is critique, not agreement. Answer in four parts, in this order,
with a table at the top of each part, marking every finding fatal,
serious, or worth-noting, and say for each whether you measured it (you
checked a number or a quotation against the documents shown) or argued it
(reasoning a reader can dispute). Plain language throughout; a reader
outside the field should follow every sentence.

Part 1, feasibility. For every number and every claim that something was
measured, verified, run, or never run: does the record shown to you
contain it? Is "not testable" the registered word for the loss condition
the text says fired? Quote the registration.

Part 2, satisfied by the wrong thing. Every way this block could close the
experiment while leaving something the registration requires undone or
misnamed: a registered control described as run when only part of it
ran; a result placed in the wrong registered bin; a sentence that reads as
a finding of absence when the registration reads the same pattern as
instrument failure; a claim handed to a future paper that the registered
text withholds.

Part 3, no verdict. Every way the block could be registered and still
leave the future paper unable to say what the experiment supports, or the
successor experiment unable to inherit what it needs.

Part 4, over-reading. What each paragraph will be read as claiming by a
reader who has not followed the program, in a paper and in public. If a
sentence should be rewritten, write the sentence.

The tier 1 review you have been shown found six fatal problems in the
previous version and this version answers them; you may agree, disagree,
or find that an answer created a new problem. You may look things up; if
you do, say where, so facts from lookup can be told from your judgment.
Do not soften findings to be polite. End with a one-paragraph statement of
the strongest case for not registering this text as written.
