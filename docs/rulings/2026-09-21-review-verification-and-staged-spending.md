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
  **Answered later the same day — see ruling 19 below: folded into the first
  release now.** The entry stays as written, because it is the record of what was
  open when this file was first recorded.
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
  **Answered later the same day — see ruling 18 below: closed as not run.** The
  entry stays as written, for the same reason.
- **Whether the rehearsal includes a short rented slice** purely to measure
  seconds-per-step on all three architectures. A throughput figure measured on the
  laptop cannot predict the rented hardware every current estimate rests on, so
  without it the second release would rest on the same inference this ruling
  declined to rely on.
  **Answered later the same day — see ruling 21 below: yes, the rehearsal buys the
  slice.** The answer came after this file was committed, which is why the entry
  was written as open; it stays as written, because it is the record of what was
  open when this file was first recorded.

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

## Ruled 2026-09-21 (later the same day): three more items answered

*A second set of recommendations was put to John by the session, each with a
confidence level on it, and he answered "1. agreed. 2. agreed. 3. agreed". Mixed
authorship, on the same footing as the items above: the session proposed them and
he approved them, and none of the wording is his drafting. The numbering carries
on from item 17 so that nothing above is renumbered. No compute was launched and
no money was spent under these rulings either.*

18. **The registered repeated-sampling run is closed as not run.** The run
    registered in advance under amendment 2026-08-04b had been open about seven
    weeks. Its claim on money was always on money left over, and items 10 to 14
    above commit what is left to the successor experiment, so there is no money
    left over for it to claim. It is therefore closed on the record with that
    reason — the money is committed elsewhere and the scope is frozen — rather
    than being left quietly open. Why it mattered enough to rule tonight: letting
    a registered obligation lapse with no stated outcome is the one disposition
    this programme's discipline does not allow, and the hibernation condition
    (`docs/program-roadmap-2026-09-20.md`, item 5) requires every open line to
    carry its current state, its next step and what that step costs. This answers
    the third entry of "Open, and raised but not yet ruled" above.

19. **The one permitted re-run is folded into the first release now.** That makes
    the first release about $44 rather than about $32, which is still inside the
    $174.30 the programme has left and still leaves roughly $130 unauthorised.
    The reasoning accepted: asking for the re-run separately would interrupt John
    exactly when the work is mid-flight, which is the thing releasing the money
    in advance was meant to remove. The cost, recorded honestly rather than
    argued away: it authorises money for a run that may turn out not to be
    needed. This answers the first entry of "Open, and raised but not yet ruled"
    above. It does **not** answer the second entry there — whether the two
    releases together overshoot the headroom by about seventy cents — which
    stands open exactly as written, on the same reasoning as before: the
    measurement that would settle it does not exist yet.

20. **The key count that does not reproduce gets an owner.** The seventeenth
    finding of `experiments/06-mvm-0a-constructed-self-index/red-team-a4.md`
    (F17, on whether condition (f)'s validity gates were ever applied) is
    labelled MEASURED and says the endpoint records for seeds 0 to 2 carry no
    such field "among their 110 keys". That count does not reproduce in any
    committed version of the files it describes. Re-checked while recording this
    ruling: the seed 1 and seed 2 endpoint records
    (`experiments/06-mvm-0a-constructed-self-index/a3-gates/endpoint_a3_30m_seed1.json`
    and the matching `..._seed2.json`) each hold **15** top-level keys, and the
    earlier pilot record (`a3-gates/pilot_endpoint.json`) holds 7. The number 110
    is not any of them. The finding's substance — that the gates were never applied —
    is not disturbed by this; what is wrong is a measured claim that measurement
    does not support. It never entered any registered text and cannot now reach
    the registration, so it is carried as a small task to correct the record
    rather than chased tonight. It matters because it is a committed record a
    future session may cite, and a "MEASURED" label is the programme's promise
    that a number came from running something.

## Ruled 2026-09-21 (later the same day, after items 18 to 20): three more items

*Three further rulings of the same day. Each was put to John by a session with a
confidence level on it and the strongest argument against it, and he approved
each in the words quoted on the item. Mixed authorship, on the same footing as
everything above: the session proposed and he approved, and none of the wording
below is his drafting. The numbering carries on from item 20 so that nothing
above is renumbered. No compute was launched and no money was spent under these
rulings either.*

21. **The measurement rehearsal buys a short slice of rented machine time.**
    Asked whether the rehearsal should pay for real hardware in order to measure
    how long a single training step takes on each of the three architectures,
    John answered "Yes". The reasoning accepted: item 11 above binds the second
    release of money to measured throughput, and a figure measured on a laptop
    cannot predict the rented hardware that every current estimate descends from,
    so without the slice the second release would rest on exactly the inference
    item 11 declined to rely on. A second gain, not the reason but worth
    recording: it is the first occasion on which the fix that stops a finished
    run deleting its own machine before the files are home
    (`experiments/06-mvm-0a-constructed-self-index/reap-shutdown-order-method.md`)
    meets the real vendor rather than a local stand-in. **This ruling was given
    after this file was first committed**, which is why the fourth entry of
    "Open, and raised but not yet ruled" above was written as open; that entry is
    marked answered in place rather than removed. No amount changes here: the
    slice comes out of the rehearsal's own allowance in item 10 above (up to
    $10), and nothing was put to John as an enlargement of either release. How
    long a slice, and on what hardware, is for the rehearsal plan to state.

22. **Four amendments to the outside-review protocol are authorised.** Six
    recommendations were put to John with the cost of each stated, and he
    answered "Ok, can we implement all of these?". Four of them are the protocol
    amendments recorded here; the other two are not recorded in this file, and
    this entry makes no claim about what became of them. The four are:
    a session that writes binding text is always paired with a *different*
    session that checks it; the known failure modes are exercised against each
    design — a command run and its output filed — rather than cited; the
    separation between the session that writes a fix and the session that checks
    it is never traded away for speed; and a document is rebuilt, rather than
    skimmed, when new binding text starts to depend on it. What this ruling
    authorises is the four rules. It does **not** accept any particular wording:
    the text implementing them, together with a companion list of the programme's
    four real failures and the test that catches each, sits on the protocol
    amendments branch (`worktree-agent-a15f7586cfb5553b3`) and has not yet been
    read by a second session. Under the first of the four rules it adds, that
    text is owed a check before anything relies on it, and this entry does not
    stand in for that check. The protocol file itself is not touched by this
    ruling file.

23. **Past a kill date, launching takes a fresh ruling rather than dropping the
    roadmap.** Put to John with its strongest alternative, approved in his words
    "Ok that's fine. Let's go with your recommendation". The two kill dates of
    `docs/december-result-roadmap-2026-09-20.md` used to drop the roadmap to its
    fourth outcome (R4: hibernate with a registered design and a rehearsal, on
    the record as a schedule failure). Past a date, launching is now still
    possible, but only on a fresh ruling that names what comes off the back end
    to make room — a thinner closure, one outside reviewer at the closure gate
    instead of two, no refresh of the explainer, or whatever the real trade turns
    out to be. The dates themselves do not move, and neither does the reason for
    having them: nobody drifts past one quietly, and nobody decides in the moment
    without saying so out loud. The reasoning accepted, recorded so it can be
    attacked later: the kill dates were never really about schedule, but about
    stopping money going on a result that can no longer be finished before
    wrap-up starts on 2026-12-21; as written they would have abandoned a working
    design over a two-day slip, which is a rule nobody would follow, and a rule
    that gets broken is worse than none; the staggered launch of item 12 above
    now bounds the money better than a date can, because the large spend happens
    only after the first run reads out; and what a date still does, which no
    judgment about feasibility made at the moment of spending can do, is decide
    in advance — a judgment made when you want to spend is made by someone who
    wants to spend. **The same ruling settles which step the second kill date
    binds**: the launch of the remaining eight runs (step 5b of the chain in
    section 4 of the roadmap), not the single free-arm run before it (step 5a).
    The December result rests on the arms built to be separable and to be
    entangled, and those are in the second wave; the first run is a precondition
    for launching them, not the milestone. Outcome R4 stays in the roadmap as an
    outcome — it still describes hibernating with a design and no runs — but a
    missed date no longer puts the roadmap there by itself.

## Recorded elsewhere

- TimeAssembler worklog, Minimum Viable Mind: a decision entry of 2026-09-21
  carrying John's words verbatim and the same items.
- `docs/outside-review-protocol.md`: items 3 to 8, landed via pull request 13.
- `docs/successor-experiment-proposal-2026-09-21.md`: section 12, rewritten to
  items 10 to 16.
- `data/project.toml`: item 16.
- `docs/december-result-roadmap-2026-09-20.md`: item 23, landed in section 5
  (the kill dates), section 2 (the definition of outcome R4) and steps 3, 5a and
  5b of the chain in section 4, with a third amendment note at the head of that
  file. The open reading at the end of its section 4 — which step the second kill
  date binds — stays as written there and is marked answered underneath.
- The four amendments of item 22: their text is on the protocol amendments
  branch (`worktree-agent-a15f7586cfb5553b3`), in `docs/outside-review-protocol.md`
  and the companion `docs/known-failure-modes.md`, and is owed a check by a
  second session before it is relied on. No ruling file recorded those four until
  this entry.
