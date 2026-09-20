   clean, and a ledger row carrying the estimate **before** any spend.
4. **Stop for John's go, in his own words.** Nothing launches without it.

**Nothing in this document is registered.** It is a pre-statement for an
unregistered diagnostic, and its value is entirely that it was written
down before the code existed and before the number came back.


===== FILE: docs/public-path-roadmap-2026-09-16.md =====

# MVM public path roadmap (drafted 2026-09-16, Pacific)

*Status: APPROVED by John 2026-09-16 (Pacific), verbatim: "Approved on all". Proposed by Claude (Cowork session); steps and dates stand as written.
Companion to `ROADMAP.md` (stage gates), `ROADMAP-post-removal-test.md` (the fork and the paper shape)
and `STATUS.md` (this week). This file covers only one thing: getting from the current experimental
state to something usable in public discourse. It builds on the 2026-08-02 adjudication that the
writeup is one flagship registered-report-style paper (`drafts/paper-removal-test-nature-draft.md`).*

## Why this path matters

1. The Calibration Problem's chapter 1 thesis contract says the wager (self-indexed temporal
   integration as the floor of an inside) and the Part III ethics fail separately. MVM is where the
   wager is exposed to evidence.
2. Public AI-consciousness discourse runs mostly on assertion. Pre-registered instruments that can
   lose, an open ledger and published nulls are the differentiator for Sentient Horizons.
3. The essays, Appendix B ("Running the Instrument") and a possible video series need a concrete
   story. The registered results, including the nulls, are that story.

## Already handled (verified in the repo 2026-09-16, branch gate0-null-calibration)

- Threshold lock committed by John: `6ad4362` (2026-09-16 20:08 PDT).
- John's verbatim go for the A3 seeds 1 and 2 wave: `45fd652` (20:11 PDT). Two pods in flight.
- Pod-side reaping ruled and implemented for future launches: `5dedc18` (20:24 PDT).
- Both process fixes, Gate 3 (passes both arms), L1 localization pipeline built and smoke-tested.
- Ruled 2026-09-16: seed 0 is not-testable on the differential clause, so Amendment A3 as registered
  can no longer return a full registered positive. Seeds 1 and 2 test whether primary-battery
  learnability replicates and whether the control battery is a seed lottery.

## Steps from here

| # | Step | Owner | Proposed date |
|---|---|---|---|
| 1 | Seeds 1 and 2 report, checkpoints fetched and checksummed, pods reaped, ledger actual-after rows | Claude Code session | 2026-09-18 |
| 2 | DECIDE: optional extra seeds (bounded by the $100 A3 stop and the $80 RunPod limit) | John | 2026-09-20 |
| 3 | Blind-localization arm (registered, unconditional): run blind on one of the five A2 register-bearing 30M checkpoints, local, $0. The A3 L1 pipeline does not discharge it | Claude Code session, John schedules | 2026-09-27 |
| 4 | DECIDE the control-battery question: a registered Amendment A4 that makes the control learn reliably, or close A3 with partial discriminators and say so. Without this no future run can return a full verdict | John, on a proposal | 2026-10-04 | **RULED EARLY 2026-09-20: Amendment A3 closes as *not testable* (the pre-registered loss condition on a non-self control at ceiling has fired). Proposal v2 in `docs/step4-control-battery-proposal-2026-09-20-v2.md`; Gate C review RT-94 to RT-117. Grammar redesign deferred to a successor experiment after release. Closure text still to be drafted, after step 3 and the two authorised localization runs, through Gate A.**
| 5 | Refresh `explainer.md` (last touched 2026-07-01, predates the registered removal-test result, MVM-0 and A3). After the 2026-09-30 book text lock | Cowork session | 2026-10-11 |
| 6 | Fold experiment 06 (constructed self-index, A3) into the flagship paper draft, nulls and kills included; Voice Calibration and Cold Reader passes | John + Claude | 2026-10-25 |
| 7 | One outside interpretability reader red-teams the draft before any public claim. John names the candidate | John | 2026-11-08 |
| 8 | Public release: repo opened with registrations and ledger, paper preprint, one Sentient Horizons essay seeded from the explainer. Claim scope: a structural signature of self-indexing in small constructed models, never "a conscious machine" **(REVISED 2026-09-20: this sentence holds only if the localization line produces a localized result before step 6; otherwise the claim is that the ownership input is load-bearing for the primary battery on three seeds and the matched contrast could not be run)** | John | 2026-11-22 |
| 9 | Deliberative-gap-width pilot design on frontier models, the bridge to the systems public discourse is about | Claude Code session | 2026-12-13 |

## Constraints

- The book text lock is 2026-09-30. No MVM result lands before it, so the book cites MVM as a
  program with registered instruments, not as a result.
- SERE pipeline starts 2027-01-04. Step 8 should be out before then; step 9 can be design-only.
- Spend stays under the registered caps; none of steps 5 to 8 cost compute.
