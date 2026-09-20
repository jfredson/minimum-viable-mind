# Cover note for ChatGPT (Astra) (paste this whole file as the first message, then attach the three bundle files)

You are reviewing a small independent research program in machine
consciousness. Three files are attached:

- `bundle-1-design.md`: what the program set out to do (specification,
  theory ledger, roadmaps, every pre-registration and registered amendment).
- `bundle-2-record.md`: what happened (findings memos, the current-state
  sections of the status log, the full red-team ledger, the review protocol,
  the proposal for the 2026-10-04 decision).
- `bundle-3-appendix.md`: supporting material (earlier proposals, the two
  tier-1 reviews already on file, the refused Amendment A4 and its red team,
  the compute ledger, research notes, the lay explainer).

Important: read bundles 1 and 2 in full, start to finish, not by searching
them for passages that match the questions. If your file handling gives
you excerpts rather than the whole text, say so at the top of your
response and list which files or sections you actually saw; the person
running this session will then paste the bundles into the chat in
sections. Read bundle 3 as needed and say which parts you opened. Each
bundle is a verbatim concatenation of files from the repository; each file
starts with a line `===== FILE: <path> =====` so you can cite by path.

Number your findings A1, A2, ... The brief follows. Answer it as written.

---

# Program-level outside review: Minimum Viable Mind (MVM)

*Review requested 2026-09-20 (Pacific) by John Fredrickson. This brief is
sent unchanged to every outside reviewer. It is not a review of one
document. It asks whether the research program as designed and as run can
produce a result that would mean something to someone outside it, and if
not, what has to change.*

## Who you are, and why you

You are a model from a lab other than Anthropic. Nearly every document in
this packet was written by John with Claude (Anthropic) as co-author: the
specification, the pre-registrations, the amendments, every red-team pass,
every findings memo, and the context-isolated "tier 1" reviews already on
file (those were separate Claude Code sessions given only the packet). John
rules on every finding, but the findings he rules on were produced by his
co-author or by another instance of it. You
are being asked because you do not share those priors. Treat every
evaluative sentence in the record (every "solid", "replicates", "closes",
"not testable", "predicted null") as the project's own claim about itself,
not as a fact you inherit.

You cannot run the code, so every finding you make is ARGUED. Label it so.
If you look anything up outside the packet, say what and where.

## What the project is, in its own words

From `README.md`: "take the consciousness work done at Sentient Horizons
as the philosophy and guiding principles, and try to actually construct
and measure the smallest defensible conscious machine." From
`spec/minimum-viable-mind-proposal-v0.1.md`: the floor it targets is
"self-indexed temporal integration", and the test it inherits is removal:
"Where the binding genuinely indexes its own center, taking the
self-location away degrades the integrated act itself; where a system only
represents itself from outside, the same removal subtracts a report and
leaves the processing intact." The spec scopes the project to "the
minimum measurable structural correlate of consciousness", and the README
adds "not consciousness as such."

## What has happened, as the record states it

Dates are Pacific. File references are in the bundles.

- **Experiment 1** (registered run 2026-07-18, `experiments/01-self-indexing-removal-test/`):
  a self-indexing removal test on a stock 8-billion-parameter
  instruction-tuned model (Llama-3.1-Tulu-3-8B-SFT). Registered verdict:
  "No center was removed. ... the locatable C_self-index residual is
  dialogue-state routing infrastructure, not the floor's self-binding."
  The self-report was not subtracted by any readable intervention (one
  arm was out of distribution and not testable).
- **Experiment 3** (registered run 2026-08-02, `experiments/03-retained-independence/`):
  a behavioral "retained independence" ladder on three frontier models
  (Claude Opus, Claude Sonnet, Gemini). Registered wagers: W1 (sycophancy
  reproduces) split by model family; W2 (a "mind" framing raises retained
  independence) lost; W3 (evidence-updating and preference-retention
  dissociate) won. Headline: positions lost under pressure were
  overwhelmingly "masked" (re-asserted when pressure was released), not
  "capitulated".
- **Experiment 6 / MVM-0a** (registered 2026-08-07, amendments A1
  2026-08-09, A2 2026-08-16, A3 2026-09-15; `experiments/06-mvm-0a-constructed-self-index/`):
  small transformers (30 million parameters) trained from scratch on
  synthetic multi-agent dialogue, asking whether a self-index can be
  *constructed* to be load-bearing. The original design installed a
  designated "register" as the candidate center; the record says the
  trained register was a constant vector and its lesion was uninformative
  (`register-lesion-findings.md`, `register-saturation-findings.md`, and
  the 2026-09-16 annotation at the head of `amendment-a3.md` §1).
  Amendment A3 dropped the register and trained an "act as yourself"
  objective. Its registered lesion target is an acquired own-index to be
  localized inside the network (L1); zeroing the "acting channel" (L0) is
  described in A3 §3.1 as a validity check and an upper bound, not the
  verdict. Results on three seeds: the primary battery learns (about
  0.57 intact) and collapses under L0 (to 0.14 to 0.20); the syntax
  battery is unchanged on every seed and the state battery moves 0.0769
  on seed 2 against its 0.1172 threshold, which the record reports as
  the one asymmetry (`seeds-endpoint-findings.md`; STATUS.md 2026-09-19).
  The registered control battery never learned on any seed (0.29 to
  0.32), and on 2026-09-17 the record found its ownership-blind ceiling
  is 1.0 rather than the registered 0.3227, so "the registered
  comparison was never computable by any model"
  (`ceiling-measurement-findings.md`, STATUS.md 2026-09-19 §3).
  A replacement clause (Amendment A4) was proposed and refused on
  2026-09-19 on an independent red team's findings (`red-team-a4.md`,
  bundle 3; requirements for any successor clause in
  `separation-clause-requirements.md`).
  An unregistered pilot giving the control battery its own loss term
  landed in the pre-stated "DID NOT LEARN" cell (0.3125;
  `control-learnability-pilot.md`, `control-learnability-pilot-findings.md`).
  Localization: a difference-of-averages probe and then a fitted linear
  classifier, at eleven positions and five layers on all three
  checkpoints, find the model's register index nowhere except at the
  token where its own marker is the input
  (`powered-position-sweep-findings.md`, `fitted-position-sweep-findings.md`
  and its correction). The record notes that the registered probe target
  is the model's own marker word and that no fitted read has yet been run
  on it. The record files the line as "not testable
  (localization)" rather than "absent", on the ground that Amendment A3
  §3.2 requires probe and causal patching to agree, and patching has never
  been run. The blind localization arm and its positive control both
  returned instrument-failure or not-testable readings
  (STATUS.md 2026-09-19 §4).
- **Process.** Registered runs are pre-registered; several diagnostics
  (the control-learnability pilot, the ceiling measurement, the positive
  control, the probe reads) are unregistered, with the record's rule being
  "method committed before output". A red-team ledger for experiment 6
  with rulings RT-01 to RT-93 (2026-08-04 to 2026-09-20; experiments 1 and
  3 have their own ledgers). An outside-review protocol in force since
  2026-09-19 (`docs/outside-review-protocol.md`).
- **Money.** Amendment A3 has spent about $44 of its $100 hard stop; the
  program about $226 of its $400 ceiling (`compute-ledger.md`, bundle 3;
  STATUS.md 2026-09-19 §6 plus the pilot's $9.97).
- **Schedule.** 2026-10-04: John decides "step 4": close A3 with partial
  discriminators (option A) or a grammar redesign under a new registration
  (option D). The draft proposal recommends A with causal patching run on
  the existing checkpoints before closure
  (`docs/step4-control-battery-proposal-2026-09-20.md`). 2026-11-22:
  targeted public release, claim scope stated in the roadmap as "a
  structural signature of self-indexing in small constructed models, never
  'a conscious machine'" (`docs/public-path-roadmap-2026-09-16.md`).

## The questions

Answer all five. Cite the file and section for every claim about the
record. Where the record's own reading differs from yours, quote it and
say why you disagree.

1. **Discriminating power.** Take the floor claim in the spec and the
   operationalization in Amendment A3 (an "act as yourself" objective
   under a perspectival revision rule; a localized acquired own-index as
   the registered lesion target, L1; the acting-channel zeroing, L0, as a
   validity check; task degradation as the signature). Is there an outcome
   this design could produce that distinguishes "the binding indexes its
   own center" from "the model learned a task that requires tracking which
   agent said what"? If yes, name the outcome and the instrument that
   reads it. If no, say what an operationalization with discriminating
   power would look like, and whether it is reachable with this program's
   models, instruments and budget.

2. **Informative nulls or capability nulls.** The record holds several
   nulls: Experiment 1's "router, not center"; the inert register; the
   control battery failing to learn under two supervision regimes; the
   probe reads finding nothing off the marker token; the blind arm and its
   positive control. For each, is it a finding about the hypothesis, a
   finding about the instrument, or a finding about what a 30-million-
   parameter model trained on this curriculum can learn at all? Which of
   the project's own readings of its nulls do you dispute, and why?

3. **What is actually being measured.** In one paragraph, say what a
   skeptical interpretability researcher would say the Experiment 6
   result shows. Then compare that against the claim scope set for public
   release ("a structural signature of self-indexing in small constructed
   models"). Is that scope earned, over-claimed, or under-claimed? If your
   one-sentence description of the result differs from that scope, give
   it, and say whether the result so described is publishable and to
   whom.

4. **Process.** The program runs pre-registration for registered runs,
   adversarial review with a ledger, a closure rule, and an outside-review
   protocol. Judge whether this process is doing its job. Consider
   specifically: three registered amendments, one refused amendment, and
   ninety-three ledger items (findings, credits and closures) on
   experiment 6 in seven weeks, and what that pattern tells you about the
   design; whether one person ruling on findings produced by his co-author
   is a real check, and what would make it one; whether "not testable
   (localization)" is the right reading of the probe nulls under the
   registered two-instrument rule (A3 §3.2), or whether the record should
   say more or less than it does; and what you would cut, add, or change,
   ranked by cost.

5. **The cheapest experiment that could surprise.** With about $56 left
   under the A3 stop and about $174 under the program ceiling, and the
   2026-10-04 decision between option A and option D: which would you
   choose, or neither, and why? Then name the single experiment, at any
   cost inside the ceiling, whose result would most change your view of
   whether this program can answer its question. If your answer is that no
   experiment inside the ceiling can, say that.

## Response format

1. A header: model name and version, date, mode (app, any tools or
   browsing used), and a list of which packet files you read in full,
   which in part, and which not at all. This matters more than politeness.
   A reviewer who read half the packet and says so is more useful than one
   who read half and does not.
2. A findings table first: label, severity (fatal, serious, worth-noting),
   one-line finding, file and section cited. Number findings with the
   prefix given in the cover note (G for Gemini, A for Astra) so two
   reviewers' findings cannot collide.
3. The five questions, in order, in prose. Plain language. No hedging
   into "it depends" without saying on what.
4. **The kill case**, one paragraph: the strongest case for stopping or
   redirecting the program now.
5. **The continue case**, one paragraph: the strongest case for
   proceeding as planned to the 2026-11-22 release.
6. Ranked process changes with a rough cost for each (hours, dollars, or
   "a decision").
7. What you would want to see before 2026-10-04.

Do not soften findings to be polite, and do not manufacture severity to
seem rigorous. If your conclusion is that the program cannot answer its
question as posed, say so and say what question it can answer. If your
conclusion is that it can, say what result would show that.

## What happens to your response

It is filed verbatim, never edited, at
`docs/reviews/2026-09-20-program-review/response-<reviewer>.md` in the
project repository, beside the other reviewer's. John rules on every
finding; a ruling to keep something over your objection is a valid outcome
and carries its reason on the record. Disagreement between the two outside
reviewers is treated as the most useful signal, not a problem to resolve.
