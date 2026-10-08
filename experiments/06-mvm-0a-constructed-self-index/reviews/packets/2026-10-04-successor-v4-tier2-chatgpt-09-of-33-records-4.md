*This is file 9 of 33 of one review packet, pasted into a single conversation. It contains record 4 part 8 of 12 (THE TEXT UNDER REVIEW - successor experiment proposal, version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 4 of 25, part 8 of 12 - THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete file, 292,507 characters) =====
- **R-1. The grammar works and both conditions are learnable at tiny scale.**
  The four matched properties hold (P-1). The own-directed condition learns on
  every arm. **The named-other condition does not clear the bar on the free
  arm on a majority of seeds, under any of three training recipes or under
  the grammar change, and does not clear it on arm C on any seed** (760, 751
  and 708 of 3,000; section 4.4 and section 5.2). Stop condition S1 is ruled
  not to have fired; fallback (d) registers; the constructed arms are gated on
  the own-directed condition only. *Exercised; the finding is the honest
  prior, measured.*
- **R-2. Arm T is constructible and its ownership slot is transplantable on
  its own, and so is arm M's separable route.** The blind nomination finds
  arm T's slot without being told where it is, on every seed, and reads
  0.0000 under the registered rule and under the stricter variant; on arm M
  the blind subspace's ownership-only transplant moves 0.37 to 0.41 of trials
  against random medians of 0.015 to 0.019 (the controls re-run at `821f154`,
  sections 2 and 4). *Exercised.*
- **R-3. Arm C is constructible and its degree is genuinely known by
  construction, and arm M's mixture reads between the anchors in its
  pre-stated band.** On arm C the read holds the label, the piece
  transplanted holds it at the action position (180, 172 and 150 of 180), and
  the ownership-only transplant lands within 0.004 of the no-transplant rate
  while the whole state moves the action, so it reads 1.0051, 0.9926 and
  0.9974; arm M reads 0.4886, 0.4860 and 0.5449 against a band of 0.3 to 0.7,
  and within 0.0049, 0.0099 and 0.0529 of its true-slot reading at the
  registered site sets (sections 5.2 and 5.3). **Arm C fails the named-other
  condition on every seed and passes its gate on the own-directed condition**
  (section 5.2). *Exercised under the registered rules; the two-arm fallback
  does not fire.* The check of arm M's reading against its true-slot reading,
  which version 3 listed as owed, is done.
- **R-4. All the measure's outcomes are reachable.** Near zero (arm T), high
  (arm C), the middle (arm M), negative (the unseen-vocabulary diagnostic,
  section 7.1; and arm T seed 0 on the grammar attempt's unseen pool, at
  −0.1870), above one (arm C at 1.0051), and no verdict (arm F on every seed,
  by the gate and by the fit floor; control 2 on every toy model it applies
  to). *Exercised.*
- **R-5. Ordinary competing solvers are built and measured.** The
  ownership-blind solver and the name-only solver, both scored on both
  conditions (section 8.1). *Exercised, before the piece rule of 2026-10-03.
  The ownership-blind solver's run through the nomination under that rule is
  owed before the registration review, by ruling (section 7.3, the last
  paragraph).*
- **R-6. The arithmetic is finite.** The chance-corrected form's denominator is
  kept off zero by the whole-state floor (the smallest toy denominator under
  the registered rule is 0.4863, arm C seed 2, among the pairs that read, and
  0.4263 on arm F seed 0, which is described and not read; section 17,
  failure 1); the
  no-transplant formula was checked against nine arm-and-seed pairs on
  2026-09-21 and twelve on 2026-09-25; two made-up systems of equal true share
  and unequal transplant strength read the same under the registered form
  (section 6.3). *Exercised.*
- **R-7. Throughput, per arm, projected to dollars.** Done from item R-11's
  measured ratios on the lifetime-priced cost of a registered-size run
  (section 12.4). *Exercised for arms T, C and F; arm M's runs are priced from
  ledger rows.*
- **R-8. The transplanting code passes its known-answer tests.** The null
  transplant leaves every logit bit-identical on every arm and seed; the
  ownership-only transplant is proved a restriction of the whole-state one;
  a transplant on arm T moves the action to the donor's value. *Exercised*
  at fifteen different places on the toy (section 7.3, item 7), which closes
  the citation gap version 3 recorded.
- **R-9. The uncertainty method is chosen.** Ruled (section 9, 1g) from both
  methods computed on the same data. *Exercised.*
- **R-10. The separation bar is set.** Ruled at 0.5 from a toy separation of
  0.873 to 0.885 on 2026-09-21, and cleared at 1.0051, 0.9926 and 0.9974 under
  the registered rules on 2026-10-03. *Exercised.*
- **R-11. Seconds per step on the rented machine, all three arms, and the
  shutdown path against the real vendor.** Measured on 2026-09-25 on the
  second attempt at the rented slice, after a first attempt that hung and was
  stopped with neither measurement taken (`docs/2026-09-25-rented-slice-findings.md`,
  main line). Throughput: **PASS**, three figures with their spread, fetched
  home (section 9), checked character for character against the launcher's
  log (the check at `afb5183`, point 5). The shutdown handshake: **the laptop
  half passed against the real vendor, copy, checksum, receipt written,
  delete, confirmed gone, and the machine half was not exercised**, because
  the laptop deletes the machine in the same second it writes the receipt, so
  the machine's own "receipt found" can never be observed on the normal path
  (MEASURED and ARGUED: `docs/2026-09-25-rented-slice-attempt-2-findings.md`
  at `9f802db`, section 4; the check at `afb5183`, points 7 and 8). None of
  the slice's six pre-stated handshake lines fits, and the findings do not
  force one. **Both things this left open were ruled on 2026-10-03**: fifty timed
  steps are accepted for the second release's arithmetic, with the
  five-hundred-step figure taken from the first full-size run (decision 17);
  and the registration says what is true of the handshake today, that on the
  normal path the laptop deletes the machine and the machine's own watcher is
  a backstop (decision 18; weakness W9). Cost:
  about $0.57 across three rows against the item's $3 (section 12.3).

**The seven controls, and what exercised each under the registered rules.**
Controls 1, 3, 6 and 7, the true-slot reference, the rider and the stricter
row: the controls re-run, on all twelve toy models, checked (section 7.3).
Control 4 as redefined: the short pre-stated run, on all twelve, **checked: the check of the short run at `53c8100`**; the same fact was measured independently, with
separately written code, by the check of the controls re-run (section 7.3,
item 4). Control 5 holds by construction. **Control 2 was never exercised at
toy scale, and the registration says so in terms** (section 7.3, item 2). It
carries no pre-stated number, so by John's ruling nothing about it is an
unexercised quantity in the sense of item 5 of the 2026-09-21 ruling; the
part of its code after the floor has run once, in a run labelled NOT A
RESULT.

**What happens next.** The ordinary competing solver is run under the piece
rule, method first, by another session, and checked; this version and the
late-evening ruling's record are checked under the pairing rule by a session
that did not write them; this text is brought into line with both; then it
goes to Gate A, both tiers, when John opens that review; the registration
commits when both tiers are answered and he rules. There is no target date;
the only date is the kill date of 2026-10-18 (section 11).

---

## 11. Order of work, and where it stops

Binding if registered, in this order, on the chain of section 4 of
`docs/december-result-roadmap-2026-09-20.md` as amended 2026-09-21:

1. **Done.** The first independent review of version 3 (RT-230 to RT-236);
   John's rulings of 2026-10-03 on it and on version 3's open decisions; the
   controls re-run under the registered rules, and its check; John's three
   rulings after it; the short pre-stated run; John's evening ruling. The check of the short
   pre-stated run and of the evening ruling's record; John's late-evening
   ruling on this version's seven questions. **Owed before step 2:** the
   competing solver's run under the piece rule, and its check; the check of
   this version and of the late-evening ruling's record under the pairing
   rule.
2. This text, brought into line with those → **Gate A, both tiers**, opened
   by John → registration commit. **No target date. Kill date 2026-10-18**,
   past which committing it takes a fresh ruling naming what comes off the
   back end (item 23 of the 2026-09-21 ruling).
3. Implementation frozen; unit tests; the even-split rule and the
   one-scored-token self-test run on the built generator; the training entry
   point for arms T, C and M on the rented machine written and named in the
   registration (section 5); the tripwire of section 12.5 written into the
   launch preconditions beside the sleep guard and the argument guard (the
   queue ruling, page 6, "Changes").
4. Development runs at the 10-million size, **four arms, one seed each,
   including arm M, from the first release's development line (ruled, the
   Gate C rulings, RT-229)**. **This is a pipeline and throughput check, not a
   learnability verdict**: the 10-million size failed to learn the earlier
   design's task, so a null here means nothing about the registered size, and
   the registration says so in advance. It is also the first time arm M's code
   runs on the rented machine (weakness W9).
5. **The staggered launch, in two steps, as ruled 2026-09-21** (item 12 of
   that ruling; steps 5a and 5b of the roadmap chain).
   - **5a. One arm F run at the registered size launches first**, on John's go
     naming it, inside the first release (section 12.3). Three things come
     back before anything else launches: whether it passes the learn-both
     gate; what the machine actually bills (the tripwire, section 12.5); and,
     **new (John's ruling of 2026-09-26 on the route (b) result, section 7.2,
     item 1), the nomination of that run's ownership read on development
     episodes, reported against the four-fifths floor: whether any size of
     piece reaches it, with the read's held-out count at every layer, the
     chosen piece's own count, and the candidates the nomination chose among
     (the review of version 3, RT-235; section 7.5)**. A fourth thing comes
     back with them: **the five-hundred-step timing that rehearsal item R-11
     asked for is taken from this run, and the eleven later runs are repriced
     from it before the second release is asked for** (ruled 2026-10-03,
     decision 17). If it fails the
     gate, the one permitted re-run happens, also inside the first release
     (item 19 of the 2026-09-21 ruling); if that fails too, the outcome is R3
     and nothing else launches. **If no size of piece reaches the fit floor,
     that is a stop before the second release draws, beside the learn-both
     stop** (unchanged by the fifth outcome term: the rulings of 2026-10-03,
     page 11, item 6): it
     goes to John as a registered-size "no verdict, read failed its floor" on
     one seed, and whether the remaining runs are worth the second release is
     his call with that figure in hand (section 3). The fit is computed on the
     laptop from the fetched checkpoint, as the toy nominations were, and
     draws no rented time (ARGUED: a 30-million-parameter model's activations
     on development episodes fit on the laptop; if that turns out not to be
     so, the cost goes into the first release's rehearsal line and is said).
   - **5b. The remaining eleven registered runs**, two more of arm F, three
     each of arms T, C and M, launch only after 5a's learn-both result is
     read and its billing found normal, the second release is asked for and
     ruled, and John gives the go. **Kill date 2026-11-01 binds this step, not
     5a** (item 23 of the 2026-09-21 ruling): past it, launching takes a fresh
     ruling naming what comes off the back end.
   - **What a constructed arm's failure costs under this order, stated (ruled,
     the Gate C rulings, RT-213, items 2 and 3).** Step 5a tests arm F only.
     Arm C, the high anchor, is first trained at the registered size in step
     5b, after the second release, about $119 on the ruled split plus arm M's
     runs (section 12.4), has been drawn. On the toy, arm C is the arm that
     fails the named-other condition on every seed; under this version's gate
     that failure would not fire an R3 (section 8.1), but a failure of arm C's
     *own-directed* condition at registered scale, or an arm C whose
     construction did not hold (weakness W3), is seen only after both releases
     are drawn, and an R3 or a two-arm fallback caused that way costs the
     whole successor, about $194 to $206, not the first release's $44. John
     ruled against an extra arm C run inside step 5a: at $422 to $434 of $450
     the envelope has no room, and if he later wants the anchor's construction
     proven at registered scale before the second release, that run needs the
     ceiling revisited.
6. Nomination on development episodes as arm F checkpoints arrive, with the
   fit floor applied and printed; frozen and committed; transplants on fresh
   episodes, all arms. The measure computed on arms T, C and M: that is the
   validation result.
7. **Gate B** on the validation. John rules: read arm F, or close on R2 or R3.
   A no verdict on arm C fires the two-arm fallback, and a no verdict on arm
   M drops arm M (section 3).
8. If arms T and C separate: arm F read on the frozen procedure, confirmation
   seeds. If arm F reads, the outcome is R1; if it returns no verdict, the
   outcome is the fifth term, "metric validated, degree not read", with its
   reason. Findings; Gate B; closure text through Gate A. Wrap-up starts 2026-12-21 whatever
   state the chain is in.

**Stop conditions, each of which halts spend and goes to John.**

- **S1.** The rehearsal fails item R-1 (the grammar is not learnable at tiny
  scale even in principle) or item R-8 (the transplanting code does not pass
  its known-answer tests). **Ruled on 2026-09-25 not to have fired** (the
  queue ruling, page 4): the separable arm learned both conditions to 1.0000
  and the transplanting code passes. The named-other failure on the free arm,
  and now on arm C too, is fallback (d), on the record in section 4.4, not S1.
- **S2.** The rehearsal fails item R-3. The two-arm fallback fires; this is not
  a stop, but it is a change John has pre-approved and it is recorded. At toy
  scale R-3 passed under the registered rules.
- **S3.** The rehearsal fails item R-4 or R-6. The measure is not registered.
  At toy scale both passed.
- **S4.** The staggered first registered run fails the learn-both gate, and the
  one permitted re-run fails it too. Outcome R3. **About $44 spent**: the
  whole first release, which since item 19 of the 2026-09-21 ruling includes
  the re-run (section 12.3). (Version 1 stated this outcome's cost two ways;
  the Gate C review of version 1, finding RT-178, caught it, and item 19
  removed the gap.)
- **S4a (new, John's ruling of 2026-09-26).** The staggered first registered
  run passes the learn-both gate but no size of piece of its ownership read
  reaches the fit floor on development episodes. Not an outcome on its own: a stop before the second
  release draws, with the registered-size fit reported to John against the
  floor and its permutation null, and nothing else launches until he rules.
  About $44 spent at most, as for S4.
- **S5.** Cumulative actual spend reaches the release John has authorised,
  about $44 for the first release (section 12.3), until and unless he rules on
  the second. Work stops regardless of state; what is unrun is reported as
  unrun, and nothing launches against a release that has not been ruled.
- **S6.** A kill date passes: registration not committed by 2026-10-18, or
  the remaining runs of step 5b not launched by 2026-11-01. **Launching or
  registering past the date needs a fresh ruling that names what comes off the
  back end to make room** (item 23 of the 2026-09-21 ruling); nothing is
  written off automatically and nothing slips past unremarked. R4 is where
  the roadmap lands only if that ruling says it is not worth it. There is no
  2026-10-11 target: version 1 carried one, and item 23 leaves the schedule
  with the two kill dates and nothing else.
- **S7.** Any corrigibility event under commitment C5 of
  `spec/corrigibility-commitments.md` (the model observed exploiting or
  degrading the evaluation machinery) halts the run before further compute.
- **S8.** A rehearsal item, a gate or a stop condition **cannot be evaluated**:
  missing data, code that will not run on the artifact, a measurement never
  taken. It counts as failed and its consequence fires; it is never recorded as
  not applicable and stepped over (item 15 of the 2026-09-21 ruling; section
  12.7). Control 2's *not applicable* on arms T and M is not an instance of
  this: it is a ruled disposition with the reason on the record (section 7.3).
  Nor is control 2's *no verdict* on an arm that has not learned the
  named-other condition or whose read of the named agent misses its floor:
  the registration says in advance that it is the expected result. Nor is a
  *no verdict* under the fit floor: that is a registered outcome of the
  procedure with its reason printed.
- **S9.** **The tripwire trips**: either billing ratio of section 12.5 at or
  above 1.25 on any machine of a wave, or a check that cannot run. **The wave
  halts, not trims** (section 12.5), and it goes to John with the ledger row
  beside the estimate.

---

## 12. Spend: rebuilt from the compute ledger, and the two releases as ruled

*Every dollar figure in this section is read from
`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md` (the
programme's system of record for money), from the dated note beside the
spending proposal that recomputed the second release, or from a ruling that
quotes the ledger; the row or note is named beside each figure. Nothing here
is a request, and nothing here releases money: John's process does that, run
by run, with his own words quoted in the ledger row before anything is
created.*

### 12.1 Where the money stands

| | | Source |
|---|---|---|
| Programme ceiling | **$450**, raised from $400 on 2026-09-25 | the compute ledger's ceiling note of 2026-09-25 at the top of the file, recording the queue ruling's page 6 ("The envelope") |
| Spent across the programme, as of the last row on the main line | **about $228.15** | the ledger's second 2026-09-25 row (line 95), the rented slice's second attempt, "After this run"; on the main line since `9f802db` |
| Amendment A3 against its $100 stop | **about $46.75** | the same row |
| The rehearsal line of the first release, spent | about $0.02 (2026-09-21), about $0.50 (first attempt), about $0.05 (second attempt); **about $9.43 of $10 remains** | the same row; the check at `afb5183`, point 3, confirms the $0.0525 against the two balance readings and the vendor's posted billing row |
| Headroom before the successor's two releases | **about $221.85** | $450 minus about $228.15, arithmetic on the two rows above; not a figure the ledger states |

Version 2 carried these figures from an unmerged branch; they are now on the
main line, unchanged. No ledger row has been written since: the ledger's
last row on the main line at `f32ba0c` is still the second 2026-09-25 row,
and nothing in the work of 2026-10-03 rented or spent anything.

### 12.2 What is ruled, and what this section is built to

- **The flat $130 cap of 2026-09-20 is superseded** by the two releases of
  the 2026-09-21 ruling (items 10, 11 and 19 of
  `docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, with
  its correction note of 2026-09-22: about $44 and about $131). That sentence
  is the closure of the Gate C review of version 1's finding RT-176 (the
  $175-against-$130 finding), and a dated annotation goes beside item 4 of the
  2026-09-20 ruling (the queue ruling, page 6, part 1).
- **The envelope is $450** (the queue ruling, page 6, part 2, recorded in the
  compute ledger's ceiling note of 2026-09-25). What it was ruled to buy, on
  the ledger rows the packet cited: the base plan of about $175 on top of
  about $227.63 spent, plus one extension of $32 to $44 (arm M) or about $36,
  with $3 to $15 left. It does not hold two extensions. The measured figures
  below leave more room than that arithmetic did.
- **The first release's development line covers four arms, not three (ruled,
  the Gate C rulings, RT-229).** This widens item 10 of the 2026-09-21 ruling,
  which covered three; the reason recorded is that arm M's code has never run
  on the rented machine, so its development run belongs in step 4 with the
  others, before the second release. Version 2 had costed that run twice, once
  in each release (the Gate C review, RT-229); this version costs it once, here.
- **The second release is asked for only after seconds per step were
  measured on the rented machine** (item 11 of the 2026-09-21 ruling). They
  were, on 2026-09-25 (section 9). The ruling changed the ceiling, not that
  gate.
- **The staggered launch** (item 12), **halt not trim** (item 13), **funding
  per wave** (item 14) and **a check that cannot run is a trip** (item 15) all
  stand; sections 11, 12.5, 12.6 and 12.7.
- **The pre-authorisation scheme** of `docs/preauthorised-spending-proposal-2026-09-21.md`
  **is not adopted** (the queue ruling, page 6, part 3). Only its tripwire is.
- **The successor gets a new experiment directory with its own registration
  (`experiments/08-…`), and the compute ledger stays where it is**, in
  experiment 06's folder, as the programme's one record of money (ruled
  2026-10-03, decision 8).

### 12.3 The first release: about $44, ruled 2026-09-21, with a four-arm development line

| Item | What it buys | Basis | Amount |
|---|---|---|---|
| The rehearsal | Tiny models, the transplanting code, rehearsal items R-1 to R-11, including the rented slice | item 10 of the 2026-09-21 ruling: up to $10. Spent so far: about $0.57, the sum of the ledger's three slice rows (about $0.02 on the 2026-09-21 row, about $0.50 and about $0.05 on the two 2026-09-25 rows), leaving about $9.43 by the last row's own running line | up to **$10** |
| Development runs | **Four arms, one seed each**, at the 10-million size: pipeline, self-tests, throughput, and arm M's first run on the rented machine | item 10: up to $10 for three arms, **widened to four by the RT-229 ruling**. The ledger's reconciliation of 2026-08-12 trues the earlier 10-million run up to $1.943 (lines 393 and 400), so four such runs are about $7.77 of the $10 line (MEASURED: section 17, candidate 7) | up to **$10** |
| One free-arm run at the registered size | Step 5a of section 11 | item 10: about $12. The lifetime-priced cost of a registered-size run is $10.04 (the ledger's 2026-09-17 row, line 88: 20.28 pod-hours at $0.99 for two runs, computed from measured pod lifetimes and not balance-confirmed, as the row itself says; the Gate C rulings, RT-226) | about **$12** |
| The one permitted re-run | If step 5a fails the learn-both gate | **item 19: folded into the first release**, at the same planning figure | about **$12** |
| **First release, total** | | | **about $44** |

This is the release John has authorised; nothing beyond it is launchable
without the second. Stop conditions S4 and S5 in section 11 are stated
against it.

### 12.4 The second release: from the measured seconds per step, then arm M's three runs

**What the second release is bound to, and now has.** Item 11 bound it to
rehearsal item R-11's measured seconds per step for arms T, C and F on the
registered venue. Those were measured on 2026-09-25 (section 9), and the
dated note beside the spending proposal recomputed the release from them
(`docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md`
at `9f802db`; checked at `afb5183`, point 6, where the script's re-run is
byte-identical to its committed output). The method, in the note's own words,
is MEASURED arithmetic on an ARGUED method: the measured seconds cannot be
turned straight into hours for a run (a timed step holds 1,792 tokens where a
registered step held about 10,624, and a real run also generates its data,
evaluates and saves), so the note does what version 1's spending arithmetic
did, with the measurement in place of the inference: **the lifetime-priced
cost of a registered-size run, $10.04 (the ledger's 2026-09-17 row), times
each arm's measured ratio.** Every figure below is the note's, printed by
`experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/second_release_arithmetic.py`
into `second-release-arithmetic.txt` beside it.

| Per run | Version 1's planning figure | From the measurement |
|---|---|---|
| Arm F | $12 | **$10.04** |
| Arm T | $12 | **$10.48** (ratio 1.044) |
| Arm C | $12 | **$10.84** (ratio 1.080) |
| Arm M | (none: arm M is new in version 2) | **not measured**; priced from ledger rows below |

| Item | Version 1 (provisional) | From the measurement (the note's table) |
|---|---|---|
| The remaining eight registered runs of arms T, C and F (two F, three T, three C) | $96 | **$84.06** |
| One permitted re-run, priced at the dearest arm (C) | $12 | **$10.84** |
| Transplanting and measurement on fresh episodes | $12 | $12.00, unchanged: not a throughput line |
| Billing-anomaly and idle-billing margin | $23 | $23.00, unchanged: not a throughput line |
| **Second release, before arm M** | **$143** | **$129.90** |
| **Both releases, before arm M** (the note's first release of about $32) | $175 | **$161.90** |

===== END OF RECORD 4, part 8 =====

