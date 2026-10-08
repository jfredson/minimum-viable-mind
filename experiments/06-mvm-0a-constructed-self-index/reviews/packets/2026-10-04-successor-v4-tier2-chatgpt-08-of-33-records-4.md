*This is file 8 of 33 of one review packet, pasted into a single conversation. It contains record 4 part 7 of 12 (THE TEXT UNDER REVIEW - successor experiment proposal, version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 4 of 25, part 7 of 12 - THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete file, 292,507 characters) =====
1. the nominated site set (layers, position set, size of piece);
2. **the whole read's held-out count at the nominated layer, and the chosen
   piece's own held-out count at the action position, each as a count of
   held-out episodes on the registered device, with the permutation null's
   95th and 99th percentiles beside them** (RT-212, RT-230, RT-232);
3. **the chosen piece's count at each other position of its site, and its
   count on the average over those positions, each with the whole state's
   count beside it; reported, with no pass line on either** (ruled
   2026-10-03; section 7.2, item 3);
4. whether the fit floor passes, **with the band that sampling alone would
   put around the count printed beside it** (reconciled 2026-10-03, night:
   at 180 held-out episodes one episode is 0.0056, and a piece whose true
   accuracy is exactly four fifths passes about half the time);
5. the whole-state, ownership-only and no-transplant accuracies on fresh
   episodes, the raw difference, and whether the whole-state floor clears in
   both forms, **on development episodes and again on fresh ones** (RT-234);
6. the no-transplant miss against the formula of section 6.4, **and the
   detection margin at the bar** (RT-222);
7. **control 3's twenty-draw null: median and 95th percentile of the random
   donor shares, the ownership-only share, and the counts below, equal and
   above** (RT-214);
8. the reading on the chance-corrected form, or the no verdict with its
   reason;
9. **the stricter layer-0 row**: the same columns with every layer-0 site set
   removed (RT-216);
10. the repairs-style sensitivity row for the whole-state layer set;
11. the rider: the reading at arm T's site set, or its no verdict with which
    of the two reasons applies;
12. the true-slot reference on arms T and M;
13. **the controls that hold, each with its pass or fail: control 7; control
    1 on arm T; control 4 as redefined, with the donor-value share, the
    no-transplant share and the number of trials whose action changed**;
14. **the controls that are reported: control 1 on arms C, M and F; control 2
    as a description (the own-directed action's share moved under the named
    agent's piece, beside twenty random pieces), or its no verdict with the
    reason; control 6's two cells**, each with its pre-stated expectation
    where it has one;
15. the ownership-lesion result;
16. and, across the three seeds of each arm, the across-seed spread of the raw
    difference with the within-seed bootstrap beside it (section 9, 1g).

**The report for the first full-size free-model run (step 5a of section 11)
prints more than its row (the review of version 3, RT-235; accepted
2026-10-03, page 3):** the read's held-out count at every layer, the chosen
piece's own count, and the candidates the nomination chose among. The reason:
on a model where no transplant moves anything, the layer the nomination lands
on is picked among sampling noise, so the stop of step 5a must not be decided
on one number from an arbitrary pick. The procedure has already computed all
three.

---

## 8. The gates every arm passes before it is read

### 8.1 The gate on learning: own-directed only on the constructed arms, both conditions on arm F

**The constructed arms T, C and M are gated on the own-directed condition
only; arm F keeps the learn-both gate (ruled, the Gate C rulings, RT-213,
item 1, refining the queue ruling's page 1b as it applies to arms T, C and M;
the bar itself is unchanged).** The reason recorded: the anchors' ownership
slot is built in by construction, their reading uses only the own-directed
action, and the named-other gate tests whether a free system learned to
represent ownership, which the anchors are not asked to prove. Arm F is not
read mechanistically until it has learned **both** conditions.

- Measured on held-out episodes, at the end of the token budget, on every seed
  carried.
- Reported as raw accuracy on each condition separately, on every arm, with
  its spread across seeds. Not combined into one number, not normalised by
  anything. The named-other condition is reported on arms T, C and M although
  it does not gate them.
- **The threshold, per condition (ruled, the queue ruling, page 1b):** the
  condition's accuracy is above the one-in-four level at the 0.05 level under
  a one-sided binomial test, **on at least two seeds of three**. The ruling
  writes the bar as "above 0.2630"; on 3,000 held-out episodes that is 790 or
  more correct, a share of 0.2633 (MEASURED: the bar's derivation is printed
  in `docs/rehearsal-repairs-method-2026-09-25.md` at `882f252`, and
  `out-repairs/gate_base.json` carries it as the field `bar`; this session
  re-derived it by an exact binomial tail, section 17, failure 3); the
  registered measurement uses the same 3,000, so the bar is 790 there too
  (ruled 2026-10-03, late evening, ruling 4).
- Reference points reported alongside, and they are references and not
  thresholds: one in eight for guessing, one in four for a solver that cannot
  tell whose value it needs, and the **measured** accuracy of two competing
  solvers built at the rehearsal, one that cannot use ownership at all, one
  that uses only the name token (rehearsal item R-5; on the toy the
  ownership-blind solver scored 0.2340 to 0.2383 on the own-directed
  condition and the name-only solver 1.0000 on the named-other condition and
  0.2380 on the own-directed, `out-repairs/gate_base.json` at `882f252`;
  these were taken before the piece rule of 2026-10-03; the ownership-blind
  solver is to be put through the nomination under it before the
  registration review, section 7.3, the last paragraph).
- An arm that fails, after the one permitted re-run, gives outcome R3 for that
  arm, and the registration says which arm and on which condition.
- **What is already on the record about this gate (MEASURED: the earlier
  re-run's findings at `9d9d31a`, Part 1, section 1.2, whose gate counts
  equal `out-repairs/gate_base.json` field for field; the controls re-run of
  2026-10-03 read the gate from that committed file and did not run it
  again):** arm T clears both
  conditions on 3 seeds of 3; arm C clears the own-directed condition on 3 of 3
  and the named-other on 0 of 3 (760, 751 and 708 of 3,000), and passes its
  gate; arm M clears both on 3 of 3 and passes; arm F clears the own-directed
  on 3 of 3 and the named-other on 1 of 3 (994, 781 and 746), and **fails**.
  No training change fixed the free arm's failure (section 4.4).

### 8.2 The ownership-lesion check, for arm F only

Before arm F is read, the acting channel is zeroed at evaluation, the lesion
the existing code already performs. **The pre-stated shape (ruled, the queue
ruling, page 1h; refined by the Gate C rulings, RT-220):**

- **own-directed accuracy falls below the section 8.1 bar**: that is the
  collapse, and it gates;
- **arm F is read if at least two of three seeds collapse, with the third
  reported** (the RT-220 ruling). A separate collapse bar below the learn-both
  bar was considered and not taken, because it adds a second pre-stated
  number nobody has rehearsed. What the two-of-three clause is for: because
  the collapse line *is* the learn-both bar, it sits just above the level a
  fully collapsed arm is expected to reach, and an arm whose lesion drops it
  to exactly one in four is read as "not collapsed" 4.85% of the time per
  seed (MEASURED: section 17, failure 3, the exact binomial tail at 790 of
  3,000). One seed of three misreading that way must not stop arm F being
  read;
- named-other-directed accuracy is **reported and not gated**; the pre-stated
  expectation that it holds is a description, because the rehearsal found
  that shape is architecture-specific (`docs/2026-09-21-successor-measure-rehearsal.md`,
  section 8);
- the ownership-free state and syntax batteries **must hold**.

**What this check does and does not establish, in the closed design's own
registered words: it removes a sense organ, not a structure the network
built.** It is a precondition for reading arm F, since it shows the ownership
answer is load-bearing for the act, which is what makes arm F worth
measuring; it is not evidence of a centre and is never reported as such
(ruled 2026-10-03, decision 10).

Arms T, C and M do not take this check as a gate: their dependence on
ownership is architectural. Their lesion results are computed and reported as
a description of the constructed systems. **On the toy, described honestly
(ruled, the Gate C rulings, RT-220):** arm T collapses on two of three seeds,
at 0.2467 and 0.2510, and its seed 2 reads 0.2733 against the bar of 0.2633,
so under the rule it did not collapse there; arms C and M collapse on all
three (0.1703 to 0.1830 and 0.2190 to 0.2230); arm F, the arm this gate is
for, collapses on all three, at 0.1760 to 0.1940 (MEASURED:
`out-repairs/gate_base.json` at `882f252`, fields `lesioned_own` and
`lesion_collapses_own`; section 17, failure 3, prints them). Version 2's "all
three collapse" was wrong for arm T seed 2 and is replaced.

---

## 9. The numbers, now set

Every number version 1 deliberately left blank is filled from John's rulings
of 2026-09-25, 2026-09-26 and 2026-10-03, each citing the ruling that set it.
**None was invented here.** The registration text freezes them in this form.
The device row and the last row, the numbers of episodes, were open when this
version was first filed and were ruled the same night.

| Number | Set to | Ruled in |
|---|---|---|
| Separation bar between arms T and C (R1 against R2) | **0.5**: the minimum gap between arm C's reading and arm T's, on the chance-corrected form. **Reconciled 2026-10-03 (night): taken as the lowest reading among arm C's seeds that read minus the highest among arm T's, not paired by seed number** | `docs/rulings/2026-09-26-weekend-1-queue.md`, page 1a, which does not say how the gap is taken across seeds; `docs/rulings/2026-10-03-version-4-questions-rulings.md`, ruling 6. On the toy this is 0.9926. **Under this version's rules the toy cleared it on every seed, at 1.0051, 0.9926 and 0.9974** (MEASURED: the controls re-run at `821f154`, section 2, from `out-controls-rerun/summary.json`, `separation`). Version 3's 1.0051, 1.0025 and 1.0000 were read on two seeds through pieces that do not hold the label and are superseded (the review of version 3, RT-230) |
| Gate on learning (R3) | above one in four at the 0.05 level, one-sided binomial, on at least two seeds of three: **0.2633 on 3,000 held-out episodes** (790 or more correct), or the same rule at the registered count; **on the own-directed condition only for arms T, C and M, on both conditions for arm F**; the ownership-blind and name-only solvers reported beside it as references | the queue ruling, page 1b; the Gate C rulings, RT-213, item 1 |
| Fit floor | **four fifths of held-out development episodes, on the piece that is transplanted, at the action position**, per arm and seed, stated as a count (144 of 180 on the toy); only sizes whose piece reaches it may be chosen; the whole read's count printed beside it and not a second floor; the permutation null reported beside it and not used as the bar | the rulings on the review of version 2, RT-212, item 1; per arm and seed, and the read itself, ruled 2026-09-26 (decisions 21 and 23); moved to the piece by `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 1; on the piece only, and applied after the layers are chosen, by `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, rulings 1 and 2 |
| The piece's accuracy at the other positions of its site | **reported both ways, with no pass line on either**: a count at each other position, and a count on the average over them, computed as section 7.2, item 3, states | `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 3; `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling 2 |
| The device and number format of the registered fit | **the laptop's processor; the figure computed there is the registered one.** States in 32-bit, the read fitted in 64-bit by scikit-learn, library versions recorded, **and pinned in a committed file named in the registration (reconciled 2026-10-03, night)** | the review of version 3, RT-232, accepted as the review states it by the rulings of 2026-10-03, page 3; the device by `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, ruling 3 |
| Whole-state floor (whether a site set is usable) | **four fifths of the arm's own own-directed accuracy**, on the chance-corrected scale, **applied on development episodes at nomination and again on the fresh episodes at the reading; a site set that clears the first and misses the second returns no verdict**; the whole-state layer set is **the smallest that clears it, per position set, then the highest ownership-only share among those**; every all-positions site set excluded; every layer-0 site set removed at position sets other than `action` | the queue ruling, page 1c; the repairs rulings, items 3 and 4; the rulings on the review of version 2, RT-216, item 1, as clarified by refinement item 2; the review of version 3, RT-234, accepted 2026-10-03, page 3 |
| Rank cap on the nominated subspace | **8**, with the family reporting caps 1, 2, 4 and 8 | the queue ruling, page 1d |
| Candidate site list and its family correction | the rule of section 7.2, printed for the registered 12-layer model: **325 site sets and 1,300 comparisons** with layer 0 kept at the action position set only (45 and 180 on the toy); the count is the rule's output, not hand arithmetic | the queue ruling, page 1e; the repairs rulings, item 3; the Gate C rulings, RT-215 and RT-216; the reading of the layer-0 exclusion ruled 2026-09-26 (decision 20) |
| Control 3 | **a twenty-draw null, reported and not gated**: median, 95th percentile, and the ownership-only share's place among the draws | the rulings on the review of version 2, RT-214, items 1 and 2, as refined on 2026-09-26, refinement item 1 |
| Control 2, the other-agent control | **no pass line.** A reported description, beside twenty random pieces; the 0.05 tolerance of version 3's decision 15 is withdrawn and not registered; the registration says the control never ran at toy scale | `docs/rulings/2026-10-03-controls-rerun-rulings.md`, ruling 1; the twenty by `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, ruling 5 |
| Control 4, the too-early-position control | **holds; its pass line is that the outputs with the transplant are bit-identical to the outputs without it**, on the positions before both twins' first own turns, at the nominated layers; a failure withholds the reading for that arm and seed | the same file, ruling 2, reversing that morning's ruling on version 3's decision 16 |
| What a no verdict maps to | arm C: the two-arm fallback; arm M: arm M is dropped and carried as an extension; arm F after arms T and C separate: **the fifth registered term, "metric validated, degree not read", satisfactory and stated as weaker than R1** | `docs/rulings/2026-10-03-successor-v3-gate-c-rulings.md`, page 11; `docs/rulings/2026-10-03-fifth-outcome-and-both-figures-rulings.md`, ruling 1 |
| Seed count per arm | **three**; the toy arithmetic implying one seed was not carried across | the queue ruling, page 1f |
| Uncertainty across seeds | **the across-seed spread of the raw difference** is the registered uncertainty; the within-seed bootstrap over matched pairs is reported beside it; neither measures drift between runs of one seed, and the registration says so | the queue ruling, page 1g; on the repairs run the two disagreed by more than two to one on arms C and F (the repairs findings at `882f252`, section 6.2; figures at pre-rule site sets, not carried) |
| Ownership-lesion collapse threshold (whether arm F is read) | own-directed accuracy **below the learn-both bar** with the acting channel zeroed, **on at least two seeds of three, the third reported**; the named-other clause reported and not gated; the ownership-free batteries must hold; gates arm F only | the queue ruling, page 1h; the Gate C rulings, RT-220 |
| The no-transplant allowance | **at most the largest measured miss, rounded up to 0.018**; the detection margin at the bar printed in the reporting table | the queue ruling, page 2; the Gate C rulings, RT-222 |
| The form of the reading | **the chance-corrected form** of section 6.3 | the queue ruling, page 2 |
| The label | **which marker word is the model's own**, the one registered read; the route (b) candidates recorded as exploratory fits only | `docs/rulings/2026-09-23-nomination-label.md`; the queue ruling, page 3; the Gate C rulings, RT-212, item 3; John's ruling of 2026-09-26 on the route (b) result (section 7.2, item 1) |
| Seconds per step, per arm, on the rented machine | **Measured 2026-09-25 for arms T, C and F**: 13.08, 13.52 and 12.53 milliseconds per step, ratios to arm F of 1.044, 1.080 and 1.000, on a secure RTX 5090 at $0.99 an hour, at the registered shape, fifty timed steps after five warm-up steps | `docs/2026-09-25-rented-slice-attempt-2-findings.md` at `9f802db`, section 3, from `experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/bench_arms.json`; checked at `afb5183`, point 5. **Arm M was not timed.** **Fifty timed steps are accepted for the second release's arithmetic; the five-hundred-step figure is taken from the first full-size run, and the later runs are repriced from it before the second release is asked for** (ruled 2026-10-03, decision 17) |
| Arm M's predicted reading | between **0.3 and 0.7** on every seed, and within **0.10** of its true-slot reading on the same fresh episodes (the formula of section 5.3, which is that reading written in route accuracies). On the toy under the registered rules: 0.4886, 0.4860 and 0.5449, within 0.0049, 0.0099 and 0.0529 of the true-slot reading | the queue ruling, page 5 (the band); the repairs method note at `882f252`, section 5 (the formula and the 0.10); the rulings on the review of version 2, RT-223; the toy figures from the review of version 3, RT-231, and the controls re-run at `821f154` |
| The numbers of episodes at the registered size | **the toy's, unchanged: 600 development episodes with the last 180 held out for every fit (the floor is 144 of 180); 800 fresh matched pairs; 800 pairs on the relaxed set; 3,000 held-out episodes for the gates (the bar is 790); 200 shuffles for the permutation null.** The caution carried with it: at 180, one episode is 0.0056 of the scale. **Reconciled 2026-10-03 (night): the band that sampling alone puts around each count against the floor is printed beside it** | `docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`, ruling 4 |
| An arm whose three seeds disagree | **two seeds of three decide, the third reported**: an arm is read if two or more seeds read. **Reconciled 2026-10-03 (night): the separation is the lowest of arm C's readings minus the highest of arm T's, among the seeds that read, and is not compared seed by seed** | the same file, ruling 6 |

---

## 10. The rehearsal: what it was, and where each item stands

A complete measurement rehearsal before any Gate A is protocol
(`docs/outside-review-protocol.md`, "The measurement rehearsal, required
before any Gate A"). It ran in five parts, all at toy scale on the laptop
except one item: the rehearsal of 2026-09-21
(`docs/2026-09-21-successor-measure-rehearsal.md`, code in
`experiments/rehearsal-successor-measure/`, re-run from code on 2026-09-22
with the separable arm reproducing exactly and the other two not); the
repairs of 2026-09-25 (`docs/2026-09-26-rehearsal-repairs.md` at `882f252`,
code and outputs under the same directory's `src/repairs.py` and
`out-repairs/`, checked at `d216dbc`); and the re-run of 2026-09-26 under this
version's rules (`docs/2026-09-26-toy-rerun-v3-rules.md` at `9d9d31a`, code
`src/rerun_v3.py`, outputs `out-v3-rules/`, checked at `70be9fb`); **the
controls re-run of 2026-10-03 under the piece rule**
(`docs/2026-10-03-controls-rerun.md` at `821f154`, method
`docs/controls-rerun-method-2026-10-03.md`, code `src/rerun_controls.py`,
outputs `out-controls-rerun/`, checked at `e184a6e`), which the rulings of
2026-10-03, page 2, made a precondition of the registration review; **and the
short pre-stated run of the same day** (`docs/2026-10-03-short-prestated-run.md`
at `853988f`, method at `9e978d9`, code `src/short_prestated_run.py`, outputs
`out-short-prestated-run/`; checked by a second session, main line at
`53c8100`). The
last two loaded the twelve committed base-recipe models, checked each file's
fingerprint against the committed list before loading it, trained nothing and
spent nothing. The one part that spent money is item R-11. Total spent on the rehearsal so far:
about $0.57, the sum of the compute ledger's three slice rows, of the
rehearsal line's $10 (item 10 of the 2026-09-21 ruling; section 12.3).

**The models every toy result rests on: thirty, all committed.** The fifteen
trained toy models behind the repairs and the re-run (arms T, C, F and M and
the ownership-blind solver, three seeds each) are committed at
`experiments/rehearsal-successor-measure/out-repairs/models/` (main line at
`8038275`, pull request 64), because they cannot be rebuilt from code and
seed (the repairs check at `d216dbc` retrained from clean and got different
nominations) and an uncommitted record the reader cannot open is the form of
ledger item RT-145. The other fifteen are committed too (main line at
`7ed2b0e`, pull request 67): the six free-arm models behind the two training
redesigns that failed (`ckpt_F_curriculum_seed*.pt` and
`ckpt_F_reweight_seed*.pt`, in the same folder) and the nine behind the
grammar attempt (arms T, C and F, three seeds each, at
`experiments/rehearsal-successor-measure/out-grammar-c/models/`). One
fingerprint list, `out-repairs/models/SHA256SUMS`, covers all thirty, with a
`README.md` beside it saying where each file came from. The re-run's
fingerprint check compared three recorded hashes per file with the list for
the first fifteen and found all agree, its check hashed the stored files
themselves and found the same, and the label-search check found all thirty
files on the main line check against the list (MEASURED:
`out-v3-rules/models_sha256_check.json`, `all_agree: true`; the check at
`70be9fb`, section 2.1; the label-search check at `ecd2b6c`, section 4).
**What rests on them: every toy result of 2026-09-25 and 2026-09-26 that
this version quotes.** On the first fifteen: every base-recipe result of the
repairs (`gate_base.json`, `nominate_base_*.json`, `measure_base_*.json`,
`summary_base.json`, the training records `train_*_base_seed*.json` and the
`F/base/*` rows of `diagnose_named_other.json`), the whole of
`out-v3-rules/`, the label search's fits, the whole of
`out-controls-rerun/` and `out-short-prestated-run/` (which use the twelve
models of arms T, C, F and M and not the solver's three), and every toy
figure in sections 3, 5, 7, 8 and 9 of this version. On the six redesign models: the curriculum and
loss re-weighting results of section 4.4 (0 of 3 seeds each). On the nine
grammar-attempt models: the grammar attempt's figures of section 4.4 (774,
730 and 759, and everything in `out-grammar-c/`). Two kinds of figure quoted
in this version are not toy results and rest on no committed model, and are
said to be what they are where they appear: the rented slice's seconds per
step (section 9), a timing of a model that exists on the record as a
checksum only; and the two checks' own re-run figures (the grammar check's
750, 809 and 739; the repairs check's 6 of 12), which are the checks'
verification of a verdict, quoted as such, from retrainings those checks
recorded but did not keep. Decision 22, which asked whether the further
fifteen should be committed, is done.

**A pre-stated quantity the rehearsal never exercised is a fatal finding on
its own** (item 5 of the 2026-09-21 ruling). Each item below therefore says
what exercised it.

===== END OF RECORD 4, part 7 =====

