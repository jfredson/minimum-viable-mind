*This is file 25 of 33 of one review packet, pasted into a single conversation. It contains record 16 part 3 of 3 (the measurement rehearsal on small stand-in models); record 17 part 1 of 3 (the repairs to the rehearsal). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 16 of 25, part 3 of 3 - the measurement rehearsal on small stand-in models - `docs/2026-09-21-successor-measure-rehearsal.md` (complete file, 56,203 characters) =====
1. **The free arm is not between the anchors; it is at one of them.** Readings
   of 0.886, 0.837 and 0.850 against an entangled arm at 0.873 to 0.885. If
   that holds at the registered size, the promised outcome — "the closure
   sentence *degree unmeasured* is replaced by a number" — is delivered, but
   the number is "as entangled as a system built to be entangled", and the
   measure will not have demonstrated that it **scales** rather than merely
   **detects**. What would separate the two readings is a fourth arm built to
   sit deliberately in the middle, which this rehearsal did not build and which
   the proposal does not have. **Recommendation, for John to rule on: add a
   partially-separable arm to the design, or accept in the registration text
   that a free-arm reading near the entangled anchor cannot be told from a
   ceiling.**
2. **Control 6 fails its pre-stated shape on two of the three arms.** Three
   quarters of the same-value trials move. Until that is understood the
   roughly-0.88 readings are not clean statements about where the ownership
   answer lives.
3. **The whole-state transplant can never beat the arm's own accuracy**, and
   at toy scale that ceiling is about 0.55 on the entangled and free arms
   because that is all those arms can do. Every floor, and every separation
   bar, is therefore a statement about a denominator that is itself bounded by
   how well the arm learned. A floor named as an absolute number would be
   wrong; it has to be named relative to the arm's own accuracy on the same
   episodes. That is a change to the proposal's section 6.4.
4. **The freshness requirement is ambiguous and the strong reading breaks the
   measurement.** Section 7.1 asks for "marker and content combinations that
   appear in neither of the other two sets". Read as *combinations*, the
   separable arm scores 1.0000 and the measure reads 0.0000. Read as *marker
   words the arm has never seen*, the separable arm's own accuracy falls to
   0.7612, 0.6512 and 0.6512, the whole-state transplant is capped there, and
   the reading goes **negative** on two seeds out of three. The registration
   has to say which reading it means. (The strong reading is what produced the
   negative case in section 2, so it is worth keeping as a deliberate
   diagnostic, not as the evaluation set.)
5. **The degenerate site set is real and has to be excluded in writing.**
   Transplanting every layer at every position is not an intervention: it is
   the donor's own forward pass, proved as a tensor identity in the
   transplanting code's self-test. On the separable arm the whole-state
   accuracy is 1.0000 at *every one* of the forty-five site sets, so the
   "smallest layer set that clears the floor" rule the proposal gives has
   nothing to choose between and would pick arbitrarily.
6. **The named-other condition barely learns at toy scale, and doubling the
   training budget does not fix it.** This is what the proposal's own honest
   prior predicts for the whole experiment, reproduced for nothing. See
   section 8.

---

## 8. The learn-both gate, and the condition that did not learn

    ../../../.venv/bin/python rehearse.py --stage gate

| arm and seed | own-directed | named-other-directed | own-directed with the acting channel removed |
|---|---|---|---|
| separable, 0 / 1 / 2 | 1.0000 / 1.0000 / 1.0000 | 1.0000 / 1.0000 / 1.0000 | 0.2467 / 0.2510 / 0.2733 |
| entangled, 0 / 1 / 2 | 0.5817 / 0.5660 / 0.5767 | 0.2590 / 0.2370 / 0.2637 | 0.1717 / 0.1807 / 0.1860 |
| free, 0 / 1 / 2 | 0.5633 / 0.5563 / 0.5890 | 0.2547 / 0.2680 / 0.2393 | 0.1813 / 0.1947 / 0.1857 |

**R-1 fails on the named-other condition, as pre-stated.** The cell fixed
before running was: both conditions above the one-in-four level, significantly
under a binomial test at the 0.05 level, on at least two seeds of three. On
3,000 held-out episodes that bar is 0.2630. The entangled and free arms clear
it on **one seed each**. The own-directed condition clears its bar
comfortably everywhere.

This is not a surprise and it is not a small thing. Section 3 of the proposal
states the honest prior before the work: the most likely outcome of the whole
experiment is that an arm fails the learn-both gate, and **the most likely
reason is the named-other half**. The rehearsal reproduces exactly that
failure, at toy scale, for about two hours of laptop time.

**Is it the budget or the task? Measured, not guessed.**

    ../../../.venv/bin/python budget_check.py

The free arm was trained once more at roughly twice the budget — 5,000 steps
instead of 2,500, on 20,000 matched pairs instead of 15,000. The named-other
condition moved from **0.2547 to 0.2657**, and the own-directed condition from
0.5633 to 0.5737. Doubling the budget bought about one percentage point on the
condition that is failing, which leaves it sitting on the bar rather than
clearing it.

**So the shortfall is not mainly a limit of the training budget.** At this
size, on this grammar, the named-other-directed revision is close to
unlearnable **by the two arms that are not built with the ownership answer in a
slot of its own**, and more steps do not fix it. (The qualifier matters and the
next paragraph turns on it: the separable arm learns the same condition to
1.0000 at the same size on the same grammar.) That does not settle what happens
at the registered size — the ten-million rung failed to learn the earlier
design's task and the thirty-million rung did not — but it does mean the risk
the proposal's honest prior names is real, is reproducible on a laptop for
nothing, and would be worth attacking in the design before about $110 of
registered runs are committed to it.

### Does the proposal's first stop condition fire? Adjudicated here: **no**

The proposal's stop conditions halt spend and go to John. The first of them,
**S1**, is keyed to exactly the item this section marks failed:

> **S1.** The rehearsal fails item R-1 (the grammar is not learnable at tiny
> scale even in principle) or item R-8 (the transplanting code does not pass
> its known-answer tests). Nothing trains. About $10 spent.

A reader going from this file to the proposal will ask whether the line is
supposed to stop here. The question is answered here rather than left to
whoever reads the two documents next, because the proposal's own eighth stop
condition (**S8**, the one that forbids stepping over anything) says a stop
condition is never recorded as not applicable and stepped over.

**The finding: S1 does not fire.** Two measurements settle it, both from
`out/gate.json`.

- **The separable arm reaches 1.0000 on both conditions, on all three seeds.**
  Own-directed 1.0000 / 1.0000 / 1.0000 and named-other-directed 1.0000 /
  1.0000 / 1.0000. A trained model of this size, on this grammar, learns both
  conditions perfectly. S1's own words are "not learnable at tiny scale **even
  in principle**" and "**nothing trains**". Something trains, and it trains to
  the top of the scale.
- **The named-other condition is solvable at this scale by a strategy the
  rehearsal built and scored.** The name-only solver — which reads nothing but
  the name token — reaches **1.0000** on the named-other condition (and 0.2380
  on the own-directed one). So the condition is not unlearnable in principle;
  it is unlearned by two of the three architectures.

What actually failed is narrower than S1's words, and is still serious: on the
two arms that are *not* built with the ownership answer in a slot of its own,
the named-other condition does not clear its pre-stated bar on a majority of
seeds, and doubling the budget does not fix it. That is a fact about those
architectures at this size, not about the grammar in principle.

**The strongest case for the other reading, stated rather than skipped.** Item
R-1 as the proposal words it in section 10 says "both matched conditions are
learnable at tiny scale" without naming an arm; this file marks R-1 a **FAIL**;
and a reader who chains "item R-1 failed" straight to the first stop condition
gets a stop. The eighth stop condition can be read as pushing the same way. The
reason that reading does not carry: the eighth is about an item that **cannot
be evaluated** — missing data, a measurement never taken — and this one was
evaluated, with every number on the record. And the first stop condition is not
keyed to the item's heading but to the state of the world its own parenthesis
names, which the separable arm's 1.0000 contradicts directly. A stop condition
that fired when a model scores perfectly on both conditions would be firing on
the opposite of the thing it names.

**What follows instead.** The consequence the measurement supports is item 5 of
section 12 — a design change for the named-other condition, or a decision to
accept the risk with the number in front of John — not a halt. **This is the
rehearsal's adjudication and not a ruling, and it is John's to overturn.** If he
reads S1 as firing, the line stops and the proposal's own accounting for that
stop is "about $10 spent"; the actual figure so far is **nothing**, because
every number in this file was produced on the laptop.

**The acting-channel lesion behaves as pre-stated on the separable arm and
not on the others.** Removing the channel drops the separable arm's
own-directed accuracy to the one-in-four level (0.2467 to 0.2733) while its
named-other accuracy stays at **1.0000** — textbook. On the entangled and free
arms the lesion drops *both* conditions, because in a system where ownership
modulates everything, removing the channel disturbs everything. The
proposal's section 8.2 pre-states the shape "own-directed collapses,
named-other holds"; that shape is **architecture-specific**, and the
registration should say so rather than apply it to all arms.

---

## 9. Where building it differed from planning it

The method file is unchanged; this is the record of the departures, which is
the only honest way to keep a method that was committed first.

1. **The deliberately broken arm was not built.** The method planned an arm
   with two sign-flipped copies of the ownership answer so that the whole-state
   transplant would cancel itself. Building it showed the idea cannot work:
   because matched pairs differ only in the acting channel, the whole-state
   transplant at a site set is *exactly the donor's state there*, so any
   architecture that is consistent under it cannot be made to cancel. The
   negative outcome was pursued by a systematic search instead, and found —
   section 2, P-5 — with its cause identified. This is a better result than the
   planned one, and it was forced by the building.
2. **The nomination family was widened at one end and narrowed at the other.**
   Three readings of the read's label instead of one, and rank caps to 24
   instead of 8. The pre-stated family is still computed and reported
   separately at every point, so the failure of the procedure *as written* is
   on the record beside the repaired one. 810 comparisons per arm and seed.
   **The narrowing was not recorded when it happened, and is recorded here.**
   The first commit of the rehearsal code (`5fa85e2`), committed before any
   result ran, fixed five rank caps in `rehearse.py` — one, two, **three**,
   four and eight, as the line `RANK_CAPS = [1, 2, 3, 4, 8]`. The final code
   drops the cap of three and counts only caps of one, two, four and eight as
   belonging to the pre-stated family. So the pre-stated family is **180
   comparisons as actually computed** — nine layer sets by five position sets
   by four rank caps by one reading of the label, which is the count of
   pre-stated rows in `out/nominate.json` — and not the 225 an earlier draft of
   this file reported. One pre-stated cell, a rank cap of three under the
   pre-stated reading of the label, is not in the record at all. It does not
   change the finding: under that reading, caps of one, two, four and eight all
   return between 0.0000 and 0.0117 and the fit sits at chance, so there is no
   mechanism by which a cap of three alone would have found the answer. But the
   claim this rehearsal makes is precisely that the procedure *as pre-stated*
   fails, and that claim is owed the whole pre-stated procedure rather than
   four fifths of it.
3. **The fitted reads were frozen.** The first implementation re-fitted the
   straight-line read on the fresh episodes the reading is taken from, which is
   the one thing a data split exists to prevent. Fixed before any result in
   this file was read; the reads are fitted on development episodes, written to
   disk, and reloaded.
4. **The fresh pool was corrected** from unseen marker words to unseen
   combinations of seen words, per section 7 item 4. The stronger pool is kept
   under its own name because its collapse is a finding.
5. **Control 2 was implemented differently from the proposal**, recorded in
   section 6 rather than quietly counted as a pass.
6. **The rehearsal ran as soon as it was built** rather than waiting for a
   slot. Nothing about it was waiting on a calendar.

---

## 10. Throughput, and exactly what still needs the rented machine

    ../../../.venv/bin/python rehearse.py --stage throughput
    ../../../.venv/bin/python bench_arms.py --device auto --steps 20

At the registered configuration's shape — 448 wide, 12 layers — timed on the
laptop's own accelerator, batch 32, twenty steps after warm-up:

| architecture | parameters | seconds per step | median | ratio to the free arm |
|---|---|---|---|---|
| the separable arm | 26,065,471 | 0.2500 | 0.2508 | **0.981** |
| the entangled arm | 29,329,735 | 0.2672 | 0.2678 | **1.049** |
| the free arm | 29,049,735 | 0.2548 | 0.2557 | **1.000** |

**This is the measurement the second release of money was waiting for, and it
is only half of it.** The proposal carried a per-step premium of about 1.55,
inferred from a different experiment's full-versus-twin step times, "to cover
arms T and C being slower per step". Measured, the premium is **about five per
cent on the entangled arm and slightly negative on the separable one**. If
that ratio holds on rented hardware, the constructed arms do not cost
materially more than the free arm, and the second release's arithmetic — the
eight remaining runs at the planning figure — needs no architecture premium at
all.

**What a laptop cannot answer, and no arithmetic here can make it.** Seconds
per step on an Apple M4 does not predict seconds per step on a rented graphics
card. What transfers is the *ratio between the three architectures*; the
absolute figure does not. That is precisely the inference John's ruling of
2026-09-21 declined to build a release on.

So: **the rented slice is still owed, and it is now owed for a smaller
question than before** — not "how much more do the constructed arms cost",
which is answered at 0.98 and 1.05, but "how many seconds does a step take on
the machine we will rent". It is staged, costed and not run:
`docs/successor-rented-slice-staging-2026-09-21.md`, and the plan the staging
script writes is in `experiments/rehearsal-successor-measure/out/rented-slice-plan.txt`.

The same slice exercises the shutdown handshake against the real vendor, which
has never met it, and the pre-stated pass and fail lines for both halves are in
that staging note.

---

## 11. The numbers this rehearsal was told not to invent

Section 9 of the proposal lists nine numbers as outputs of the rehearsal. None
is named here. What each one now has behind it:

| number | what the rehearsal measured | still needed |
|---|---|---|
| the separation bar between the two constructed arms | separation of **0.873 to 0.885** against **0.0000**, across-seed spread 0.019 on the entangled arm and 0.000 on the separable one | John's ruling. A bar anywhere from 0.1 to 0.8 would separate these two at toy scale, so the measurement does not force a choice; what it does is show the choice is not close |
| the learn-both threshold, per condition | measured competitors: ownership-blind at 0.2237 and 0.2253, name-only at 0.2380 and 1.0000 | a decision about the named-other condition, which at toy scale does not clear the one-in-four level on a majority of seeds |
| the floor on the whole-state transplant accuracy | the full curve against site set, per arm, in `out/nominate.json`: the entangled arm runs 0.0517 at the first layer, 0.3467 at the second, and about 0.556 from the third on, which is its own accuracy | John's ruling — and, per section 7 item 3, a floor stated **relative to the arm's own accuracy**, not as an absolute |
| the rank cap on the nominated subspace | on the separable arm, at the site set the nomination picks, averaged across the three seeds: **0.153 at rank 1, 0.355 at rank 2, 0.832 at rank 4 and 1.000 at rank 8** — per seed in section 3, item 3 | John's ruling; the measurement says a low cap silently under-reads |
| the candidate site list and its family correction | 45 site sets × 3 labels × 6 rank caps = **810 comparisons** per arm and seed; the pre-stated family was 225 as planned and **180 as computed**, because the final code dropped the rank cap of three — section 9, departure 2 | John's ruling on which labels are in the family at all |
| the seed count per arm | three seeds gave an across-seed spread of 0.019 and 0.023 on the raw difference; the arithmetic for a half-width of 0.05 implies **one seed** | John's ruling. The toy arms are far more repeatable than registered-size runs will be, so this number should not be carried across without a discount |
| the paired-uncertainty method | both computed on the same data: across-seed spread 0.0189 and 0.0227; the within-seed bootstrap over matched pairs 0.0198 and 0.0203. **They agree closely**, which is itself the useful finding — the choice does not matter much here | John's ruling |
| the ownership-lesion collapse threshold | the separable arm drops to 0.2467 to 0.2733 on the own-directed condition while holding 1.0000 on the named-other one | a decision, plus the section 8 finding that the pre-stated shape is architecture-specific |
| seconds per step, per arm, on the rented machine — the whole of the second release's arithmetic | **nothing.** This rehearsal measured the *ratios* between the three architectures on the laptop (0.981, 1.049 and 1.000) and nothing else; the proposal says in terms that this number is never inferred from a premium and never measured on the Mac | rehearsal item R-11, the one short slice of rented time. Staged, costed and **not run**: it needs John's spoken go naming it. Section 10 |

---

## 12. What would be needed to finish

1. **John's rulings** on the eight numbers above, on which form of the reading
   is registered, and on the nomination label — which is now a
   registration-blocking question rather than a detail.
2. **The rented slice**, which needs his spoken go naming it. About $0.75 to
   $1.00, hard cap $2.00, inside the first release.
3. **Three repairs to the proposal text**, each with a measurement behind it:
   control 1 re-worded so it cannot veto the entangled arm; the no-transplant
   sanity rule replaced with the review's formula; and section 7.1's freshness
   requirement disambiguated.
4. **A decision about the middle of the scale** — a partially separable fourth
   arm, or an admission in the registration text that a free-arm reading at the
   entangled anchor cannot be told from a ceiling.
5. **A design change for the named-other condition, or a decision to accept
   the risk.** Section 8 settles that it is not a budget limit: doubling the
   budget moved it by about a point. This is the single cheapest thing the
   rehearsal found that could sink the registered experiment, and it is worth
   attacking before the money is committed rather than after.
6. **Control 2 built as the proposal states it**, rather than as it was run.

None of the six costs more than a few hours, and only the second costs money.
===== END OF RECORD 16, part 3 =====

===== RECORD 17 of 25, part 1 of 3 - the repairs to the rehearsal - `docs/2026-09-26-rehearsal-repairs.md` (complete file, 33,735 characters) =====
# The rehearsal repairs — findings

*Written 2026-09-25 (Pacific) by the Claude Code session "MVM W1c rehearsal
repairs", session (c) of `docs/weekend-1-session-prompts.md`, on branch
`worktree-w1c-rehearsal-repairs`. The file keeps the name the prompts file gives
it (dated 2026-09-26, the Saturday it was planned for); the work ran a day early
because the rulings it depends on were made on the evening of 2026-09-25.
**UNREGISTERED.** Nothing here is a result about the scientific question, nothing
here is a bar, and nothing here is a ruling. Every bar used below was ruled by
John in `docs/rulings/2026-09-26-weekend-1-queue.md` (the "Weekend 1 queue
ruling"); every other threshold is a rehearsal-only one fixed in the method note
before the run.*

*Ran locally on the laptop, on models of about one to one and a third million
parameters. **No machine was rented, no vendor was contacted and nothing was
spent: $0.***

*Method, committed before any code or output:
`docs/rehearsal-repairs-method-2026-09-25.md`. Code and every output file:
`experiments/rehearsal-successor-measure/src/` (new: `repairs.py`,
`arm_middle.py`, `diagnose_named_other.py`; changed: `training.py`) and
`experiments/rehearsal-successor-measure/out-repairs/`. The 2026-09-21 record in
`out/` and its driver `rehearse.py` are untouched.*

*Every finding is labelled **MEASURED** (a command was run and its output is
reported, with the committed file it wrote) or **ARGUED** (reasoning a reader can
dispute). Figures from the entangled and free arms are quoted as a range and a
direction, as `docs/rulings/2026-09-23-range-and-direction-only.md` requires:
those arms do not reproduce from code and seed on this laptop. Written under the
workspace plain-language rule.*

---

## 0. What to read if you read nothing else

- **Item 1, the named-other condition: neither redesign clears the ruled pass
  line, so page 4's fallback (d) applies.** The curriculum clears the bar on 0
  seeds of 3 and the loss re-weighting on 0 of 3; the unchanged recipe, re-trained
  in this session, clears on 1 of 3, as it did on 2026-09-21. Both redesigns made
  things worse: the curriculum teaches the model to answer the named-other turn
  with **its own** value, and the re-weighting costs the own-directed condition
  without buying the named-other one. MEASURED.
- **Why, most likely: the grammar signals "this is your turn" on both action
  turns**, so the only thing telling the two apart is one word, and the two
  conditions compete for one route. That points at page 4's redesign (c), a
  grammar change, which this session did not attempt. ARGUED.
- **Item 4, the fourth arm: it passes page 5's pre-stated line.** Built to be
  partly separable, it reads **0.48 to 0.53** on the chance-corrected form on all
  three seeds, inside 0.3 to 0.7, and within 0.02 to 0.04 of what its construction
  predicts from its own route accuracies. Folding it into the registration is
  John's call under page 5 and page 6. MEASURED.
- **Item 2, one instrument: done in code, and it exposed two things the ruled
  text does not settle.** The ruled exclusion ("every layer at every position")
  is too narrow, because copying **any** layer at every position hands the donor's
  whole forward pass downstream; the nomination picked such a set on two of arm
  C's three seeds. And the ruled site-list rule does not produce the toy's 176
  comparisons even on the toy: it produces 296. MEASURED.
- **The rider (John's addition): at arm T's site set, arms C, F and M give no
  verdict at all** — their whole-state transplant does not move the action
  there. So what differs between arms is, first, where the procedure has to look.
  MEASURED.
- **Item 3, control 2 as the proposal words it: no verdict on arms T, C and M,
  a pass on arm F that means little.** It needs the arm to carry the named
  agent in its running state and to have learned the named-other condition;
  arm T carries it outside the state by construction, and arms C and F have not
  learned the condition. MEASURED.
- **Item 5, the measure with the ruled form and numbers:** arm T reads 0.0000
  on every seed, exactly as on 2026-09-21; arm C reads at the entangled end
  (0.99 to 1.00); the free arm reads at the entangled end too (1.00 to 1.003),
  and **fails the learn-both gate**, so under the ruled numbers it would not be
  read at all. The separation bar of 0.5 is cleared on every seed. MEASURED.

---

## 1. What was committed when

| order | commit | what |
|---|---|---|
| 1 | `426b6e8` | the method note, before any code or output |
| 2 | `16d75f6` | training options, arm M, the driver's train and gate stages (code only) |
| 3 | `9e341e6` | nomination, measure and summary stages (code only) |
| 4 | `81dc84d` | two additions **not pre-stated**, labelled so in the code (§8) |
| 5 | `004d134` | the outputs |
| 6 | this file | the findings |

The method note precedes the first output commit. Two dry runs of the
measurement code were made on scratch checkpoints outside the repository before
commit 3 (one on untrained models, one on a trained arm T and a 400-step arm M,
on 120 episodes); nothing from them is committed or reported as a result.

---

## 2. Item 1 — the named-other condition (ruling page 4)

===== END OF RECORD 17, part 1 =====

