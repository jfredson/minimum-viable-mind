# MVM program roadmap (2026-09-20, Pacific)

*Status: APPROVED by John 2026-09-20 (Pacific), verbatim "Agreed on all" on the Cowork discussion this
file records. Supersedes steps 5 to 9 and the constraints section of `docs/public-path-roadmap-2026-09-16.md`.
Steps 1 to 4 of that roadmap are done or ruled and stand as written there. Companion to `ROADMAP.md`
(stage gates), `ROADMAP-post-removal-test.md`, `STATUS.md` (this week) and `docs/outside-review-protocol.md`.*

## What changed and why

The 2026-09-16 roadmap aimed the program at a public release on 2026-11-22, with the paper's claim
shape written in advance. On 2026-09-20 John re-evaluated it. In his words: he prefers the project
to have a science-based goal and less of a publish-by-this-date goal; we do not know which roads
we will have to go down to reach the end goal of learning everything we can about how to evaluate
the presence of an inside experience within machine minds; he would rather it be an ongoing
research experiment that is documented and shared as it unfolds than something with a specific
date and result in mind. The SERE pipeline start (2027-01-04) is a deadline for putting the
project into a hibernation state that can be resumed after he graduates (May 2027), not a
deadline for results. Whatever publishable results come out are evaluated as they come, if they
come.

## What stays

The pre-commitment discipline binds each experiment, not the program, and is compatible with an
open-ended program. All of it stays in force:

- Method committed before output; pre-stated result cells; registered terms for outcomes
  (positive, null, *not testable*, redesign).
- The outside-review protocol (Gate A at registration and amendment, Gate B at direction-changing
  or publication-bound interpretations, Gate C advisory on proposals), the red-team ledger, and the
  closure rule for fatal findings.
- Spend caps as registered. The human gate on spend, launches, and changes to registered or
  protocol text. Free local work on existing data needs its method committed before output, not a go.
- The book text lock, 2026-09-30. The book cites MVM as a program with registered instruments, not
  as a result.

## What is dropped

- 2026-11-22 as a release date, and steps 5 to 9 of the 2026-09-16 roadmap as dated steps.
- "The paper" as the program's scheduled output. The flagship registered-report paper
  (2026-08-02 adjudication, `drafts/paper-removal-test-nature-draft.md`) becomes one possible
  write-up, produced when a line closes with something worth writing up, not on a date.
- Any claim shape fixed before the results exist. The 2026-09-16 sentence "a structural signature
  of self-indexing in small constructed models" is struck (already struck for A3 on 2026-09-20).

## What replaces them

1. **Lines of inquiry, each ending in a ruling.** A line runs until it closes under a registered
   term. Every closing is a ruling by John on a reviewed proposal, and every ruling is a published
   entry. This is the program's cadence in place of dates.
2. **The program log is public as it unfolds.** The site at `site/` (plan:
   `docs/site-plan-2026-09-20.md`) goes public from its first deploy rather than waiting for a
   release; `data/project.toml` is updated whenever `STATUS.md` is. Opening the repository itself
   (registrations, ledger, code) is a launch and stays John's gate; recommended alongside the first
   site deploy, but not date-bound.
3. **State-of-the-program write-ups when a line closes.** Any write-up that makes a public claim
   goes past an outside reader who was not in the room before it goes out (step 7 of the old
   roadmap, kept as a rule rather than a date; shortlist in
   `docs/outside-reader-shortlist-2026-09-19.md`).
4. **Claim rule.** Claims are whatever the registered results support, stated in the terms
   registered for them. Never "a conscious machine".
5. **Hibernation condition, complete by 2027-01-04.** The program is in a hibernation state when:
   - nothing is in flight: no pods running, no experiment mid-run, the compute ledger closed with
     actual-after rows;
   - every open line has a `STATUS.md` entry with its current state, its next step, what that step
     costs, and which gate it needs;
   - `data/project.toml` and the site match `STATUS.md`;
   - registered text, ledger, and checkpoints are committed, checksummed, and stored where a
     resuming session can find them;
   - a `RESUME.md` at the repo root says how to restart, in what order, and what will have
     expired (accounts, API keys, RunPod, subscriptions);
   - any partial draft is marked partial.
   Recommended wrap-up start: 2026-12-13, so nothing new is launched in the last three weeks.
   Resumption after graduation, May 2027, or in pipeline breaks if any exist.

## Near-term schedule (unchanged)

| Step | Owner | Date |
|---|---|---|
| Blind-localization arm, registered, local, $0 | Claude Code session, John schedules | 2026-09-27 |
| Two authorised $0 localization runs (other-agent index control L2(a), standardised refit) | Claude Code session | after step 3, method committed before output |
| Causal patching, designed as new code | Claude Code session, proposal to John | after the two runs |
| Program-level outside review responses (Gemini, ChatGPT Astra) filed, disagreement map and draft rulings | John runs sessions, Cowork drafts | before A3 closure text |
| A3 closure text, registered text, through Gate A | Cowork drafts, John rules | after localization order completes |
| `explainer.md` refresh | Cowork session | after the 2026-09-30 book lock, no date |

## Lines on the table (as of 2026-09-20, not ordered, not dated)

- Localization of the ownership input (blind arm, the two authorised runs, causal patching).
- Grammar redesign, option D, as a successor experiment with its own registration. No longer waits
  on a release.
- Deliberative-gap-width pilot on frontier models (old step 9), design first.
- From `explainer.md`: a binding test (one act or only looks like one); holding a correct answer
  against a user who wants a different one; self-reports checked against what the instruments see.
- The construction project (systems that carry their history forward), behind the committed
  safety document.

Which line runs next is decided per ruling, on what each line can teach for what it costs, with
the site's "next most valuable steps" view as the working list.

## Decisions for John

1. When to open the repository (recommended: with the first site deploy).
2. Confirm the 2026-12-13 wrap-up start, or set another.
