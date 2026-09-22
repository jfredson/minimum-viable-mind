# Ruling 2026-09-21: review verification widened, spending released in two stages, and the halt rule

*Recorded 2026-09-21 (Pacific). John's rulings on a set of recommendations put to
him with a confidence level on each, given in his words as "Agreed on all",
followed by "Go" authorising the work to proceed. The recommendations were made
by the session; he approved them. Recorded as mixed authorship for that reason,
never as his own drafting. Where an item extends or overrides an earlier ruling,
the earlier ruling is annotated, not rewritten. No compute was launched and no
money was spent under this ruling.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`).
The session that put these items to him used the word "tranche"; the rule says to
translate borrowed vocabulary from finance even when it is our own, so this file
says **first release** and **second release** throughout.*

---

## 1. The Amendment A3 closure text

1. **The citation defects are fixed before the outside tier 2 sessions run**, not
   after, so a scarce reviewer hour is not spent on a defect already known. The
   failing finding was that version 4 cited item 7 of
   `docs/rulings/2026-09-20-december-result-roadmap.md` for facts carried by
   item 1.
2. **The fixes are verified by a session other than the one that made them**, per
   the closure rule.

## 2. The outside-review protocol (the judgment calls raised by the session that wrote the amendment text)

3. **Reviewer-owned verification runs at every Gate A**, whether or not a fatal
   finding exists — not only on the closure of a fatal finding. **This extends
   item 6 of the 2026-09-20 ruling**, which named fatal closures only. The reason
   given and accepted: the programme's worst failure was not a missed finding but
   that nobody ever ran anything to confirm a fix. The narrower reading stands as
   what was ruled on 2026-09-20; this file is the amendment to it.
4. **The rehearsal requirement sits after the gates**, not inside the closure
   rule, because it governs when a gate may open rather than what closes a
   finding.
5. **A pre-stated quantity the rehearsal never exercised is a fatal finding on its
   own.** This was the writing session's own addition, not the reviewer's, and is
   ruled here for the first time.
6. **The replacement for the struck "unlikely" sentence stands**, including its new
   prohibition on manufacturing severity to look thorough.
7. **The protocol amendment text does not need its own Gate A pass.** It is checked
   at the successor's Gate A, which is the reading of item 6 of the 2026-09-20
   ruling.
8. **Filing paths, the stated size of a rehearsal, and the historical headings
   stand** as written.

## 3. Review capacity

9. **Two outside reviewers at Gate A; one at Gate B and Gate C.** A registration
   commit is hard to reverse, so both outside models run there. Interpretations
   and proposals can be revisited, so one is enough. The fixed brief already named
   this alternative and priced it as halving John's session time at the cost of
   the disagreement signal.

## 4. Spending — released in two stages

10. **The first release covers the measurement rehearsal (up to $10), the
    development runs (up to $10), and one free-arm run at the registered size
    (about $12).** About $32 against the $174.30 the programme has left. **The
    $400 ceiling is untouched** and the ruling of 2026-08-16 that $400 is final
    stands.
11. **The second release is requested only after the week-40 rehearsal has
    measured seconds-per-step for all three arms**, so its number rests on
    measurement rather than on the 1.55× premium inferred from a different
    experiment's full-versus-twin step times.
12. **The staggered launch is adopted**: one free-arm run goes first and its
    learn-both result is read before the remaining eight are committed to. On the
    proposal's own prior this makes the most likely outcome cost about $32 rather
    than about $140, and it doubles as the billing-anomaly check.
13. **"Halt, not trim" replaces the seed fallback of week 43.** Dropping seeds does
    not answer a tripled unit cost: at the anomalous rate the trimmed plan still
    spends about $326, which is more than the programme has left. Halting on the
    first machine that bills anomalously bounds exposure to roughly one machine's
    overrun.
14. **The account is funded per wave, not per cap** — topped up to the wave's
    estimate plus $20 and no further, so no anomaly of any size can cost more,
    because there is nothing else there to spend. This is the only control in the
    programme's history that held when everything else failed (2026-08-12).
15. **A check that cannot run counts as a trip, not a skip.** The precedent is the
    balance query returning an error on 2026-09-17.
16. **The stale spend figures are corrected to the compute ledger**, which is the
    system of record: about **$225.70 of $400** spent, headroom **$174.30**.
    `data/project.toml` and section 6 of the December-result roadmap both carried
    $215.70, which was the figure before the control-learnability pilot (~$9.90)
    and the checkpoint recovery ($0.067).

## 5. The project's own description

17. **The mission line is rewritten** to match the ruling of 2026-09-20, dropping
    "working toward a publishable result" — the phrase that ruling struck.

---

## What was NOT ruled here

- **No money was authorised for any named run, and none was spent.** This
  programme requires a verbatim go naming the run, and the corrigibility
  commitments require that go name a specific registered batch. "Agreed on all"
  is a ruling on a plan; it is not that go. Nothing is registered yet in any
  case — the successor proposal is a Gate C draft — so there is nothing
  launchable. The go is owed at the moment a named run is staged.
- **The twelve design decisions inside the successor proposal are not ruled.**
  They belong to a document that has not yet had its Gate C tier 1 pass, and the
  protocol says John rules on text that has already been attacked.

## Open, and raised but not yet ruled

- **The one permitted re-run has no home.** The first release names one run at the
  registered size, but the most likely branch on the proposal's own prior needs
  the re-run (about $12). Either it is asked for as a small separate release when
  that branch fires, or it is folded into the first release now, making it about
  $44 and still leaving about $130.30 unauthorised.
- **The two releases together come to about $175 against $174.30** — seventy cents
  past everything the programme has left. Three ways to answer it: the rehearsal
  measures the per-run cost lower; the seed count falls out of the rehearsal; or
  the $400 ceiling itself is reopened. None is chosen here, because choosing
  before the measurement exists is what the two-stage scheme was ruled to prevent.
- **The registered repeated-sampling run** (amendment 2026-08-04b, registered
  before running) has been open about seven weeks and its claim was always on
  underspend, which this ruling commits elsewhere. It needs an outcome on the
  record — closed as not run with the reason, or kept open with a stated
  condition. Silence is the one disposition the programme's discipline does not
  allow.
- **Whether the rehearsal includes a short rented slice** purely to measure
  seconds-per-step on all three architectures. A throughput figure measured on the
  laptop cannot predict the rented hardware every current estimate rests on, so
  without it the second release would rest on the same inference this ruling
  declined to rely on.

## Annotated 2026-09-21 (later the same day): task time, not calendar time

*The items above stand exactly as ruled. This annotation records a later ruling
of the same day that changes how two of them state their timing, and nothing
about what they require.*

John ruled that work is measured in task time rather than calendar time — in his
words, "Let's stop measuring things in calendar time and measure them in task
time... We are not working on a delayed calendar. We are working on a finish
every task as quickly as possible mode." Two items above name a week of the
calendar that the December-result roadmap used to run on; that roadmap's
section 4 is now an ordered chain of what must finish before what, so those
names now read as follows. No dependency, amount, owner or condition changes.

- **Item 11**, "the second release is requested only after the week-40 rehearsal
  has measured seconds-per-step for all three arms": the rehearsal is step 2 of
  the chain in section 4 of `docs/december-result-roadmap-2026-09-20.md`. The
  condition is unchanged — the second release is requested only after that
  rehearsal has measured seconds-per-step for all three arms, whenever it runs.
- **Item 13**, "'halt, not trim' replaces the seed fallback of week 43": the
  seed fallback belonged to the registered-training launch, which is step 5 of
  that chain. The replacement is unchanged.

The dates elsewhere in this file are untouched, because none of them is a pacing
choice: the amounts and headroom of item 16, and the dated precedents cited in
items 14, 15 and the open questions, are all records of what happened.

## Recorded elsewhere

- TimeAssembler worklog, Minimum Viable Mind: a decision entry of 2026-09-21
  carrying John's words verbatim and the same items.
- `docs/outside-review-protocol.md`: items 3 to 8, landed via pull request 13.
- `docs/successor-experiment-proposal-2026-09-21.md`: section 12, rewritten to
  items 10 to 16.
- `data/project.toml`: item 16.
