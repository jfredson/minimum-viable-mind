# Free-arm label search at toy scale (RT-212 route b) — findings

*Written 2026-09-26 (Pacific) by the Claude Code session "MVM W1d free-arm label
search", on branch `w1d-free-arm-label-search`, cut from main at `62c3824`.
**UNREGISTERED.** Nothing here is a ruling or registers anything, and nothing here
recommends what should be registered: that is John's call. Laptop only, no network,
no rented machine, **$0**. Nothing was retrained.*

*Order of commits:*
1. *the method (`docs/2026-09-26-free-arm-label-search-method.md`, `583b3f2`);*
2. *the code (`experiments/rehearsal-successor-measure/src/label_search.py`, `883bc81`);*
3. *amendment 1 to the method (`88ab899`), then the code change it called for (`53240d4`);*
4. *amendment 2 to the method (`6c82c81`), then its code change (`609260b`);*
5. *the output (`experiments/rehearsal-successor-measure/out-label-search/`: `fd7f5fa`, `63f1ead`, `54ee9b0`);*
6. *this file.*

*Each amendment was committed before the fits it governs. No file under
`experiments/rehearsal-successor-measure/src/` that exists on main was changed;
two files were added (`label_search.py`, `label_search_report.py`).*

---

## 1. The question, and the answer in one line

Route (b) of the ruling on the review finding RT-212 (the ownership read never
finds its label on the free arm) asks for something the own-directed loss forces a
freely trained system to carry, which a fitted straight-line read can recover on
arm F (the freely trained arm) at four fifths.

**None of the three candidates the method allowed clears the four-fifths floor on
arm F, at any site set, on any seed.** Candidates 1 and 3 are carried well above
chance on arm F. Candidate 1 (which two turns are the model's own) reaches 0.789
at best; candidate 3 (the model's own value on the asked item) reaches 0.633.
Neither reaches 0.80.

## 2. What was run

- **Checkpoints:** the rehearsal repairs' `base` runs, arms F, T, C and M, seeds 0,
  1 and 2, loaded from the repairs worktree (they are not in git). Their SHA-256
  hashes are in every `fit_*.json`.
- **Episodes:** the repairs' development set: 600 recipient episodes (seed 4242).
  The first 420 are used to fit and the last 180 are held out to score. This is
  the split the 0.172 figure in RT-212 comes from.
- **Fitter:** the one `repairs.fit_reads` uses
  (`LogisticRegression(max_iter=3000, C=1.0)`).
- **Where:** the registered site-set rule at toy scale. That is 15 contiguous
  layer sets of the five running states (layer 0 is the input embedding with the
  acting channel added; layers 1 to 4 are after each block), times four position
  sets, 60 site sets in all:
  - `action` (the `<mask>`);
  - `action+ans` (and the `<ans>` before it);
  - `action+3` (`<self> <item> <ans> <mask>`);
  - `post-identity` (every position from the model's first own turn to the
    action, averaged).
  The first three are the 45 **fixed-extent** site sets. Their positions do not
  depend on who the model is.
- **Floor:** 0.80 on plain held-out fit accuracy. A site set clears on a seed
  when it scores at least 0.80 **and** beats every one of 200 label shuffles at
  that seed's best site set. A candidate clears on an arm when some site set
  clears on all three seeds.
  - The stop rule used the fixed-extent verdict, because `post-identity` starts
    at one of the model's own turns, so where it starts gives part of the answer
    away (method, section 3).

### 2.1 Things that went differently from the method as first committed

1. **The identity check failed on the first run, and the cause was the processor, not the weights (amendment 1).**
   - Run with the forward pass on the laptop's processor, the check did not
     reproduce the committed fit figures for the ruled label. Arm F seeds 0, 1
     and 2 and arm M seed 0 were off by one or two of 180 held-out episodes
     (`out-label-search/verify_cpu_failed.json`).
   - The committed runs had used the graphics processor (`mps`). Run there, the
     check reproduced all twelve arm-and-seed pairs exactly
     (`out-label-search/verify.json`).
   - Every forward pass since runs on `mps`. Nothing was fitted before this was
     settled.
2. **The null was cut to the best site set, by John's ruling during the run (amendment 2).**
   - As first committed, the null was 100 shuffles at every site set on arm F.
     That took 5,493 seconds for one seed, with other jobs loading the laptop.
   - John ruled 200 shuffles at each arm and seed's single best-fitting site set
     instead, with every site set still fitted. After the change a seed took 2
     to 211 seconds.
   - The superseded seed 0 file is kept
     (`superseded_fit_own-turn-pair_F_seed0_every-site-100-shuffles.json`). Its
     60 fits equal the refit's exactly (largest difference 0).
   - **Correction to amendment 2's text:** it says that file's null 95th
     percentile ran "from 0.056 to 0.067". Over all 60 site sets it runs from
     **0.050** to 0.067. The 0.056 came from reading only the best-fitting sites.
     The highest single shuffle, 0.100, is right.
   - Borrowing the best site's null for the other site sets decided nothing
     here: every site set that reached 0.80 was on a constructed arm, reading
     the ruled label, at 0.8 or more, against nulls whose highest shuffle is
     0.27.

### 2.2 Read against the Gate C rulings that landed on main while this ran

The ruling on RT-212 to RT-229
(`docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`, pull request 60)
reached main after this branch was cut. Two of its items bear on how these results
are read, and neither changes a verdict:

- **The RT-212 fit floor, item 1.** The floor is **absolute, four fifths**, with
  the label-permutation null reported beside it and not used as a bar. This
  search's clearing test was stricter: 0.80 *and* above every shuffle. No arm F
  site set reached 0.80 for any candidate, so the verdicts are the same under
  either reading.
- **The acting-channel exclusion, RT-216 item 1.** Layer 0 stays a candidate
  only at the `action` position set. Every other site set containing layer 0
  is reported as "at the acting channel's injection" and is not a reading. The
  acting channel fires on the whole action turn too, so this takes out
  `action+ans` and `action+3` with layer 0 as well as `post-identity`. With
  those removed, arm F's best per seed is:
  - candidate 1: 0.722 (layer 1, `action+3`), 0.394 (layer 1,
    `post-identity`), 0.783 (layer 1, `post-identity`);
  - candidate 2: 0.444, 0.406 and 0.450, all at layer 1, `post-identity`;
  - candidate 3: 0.611, 0.611 and 0.633 (layer 4 `action+ans`; layers 1–2
    `action`; layers 1–3 `action+ans`);
  - the ruled label: 0.533, 0.456 and 0.406, at layer 1 or layers 1–2,
    `post-identity`.

  All are under 0.80. The exclusion costs candidates 1 and 2 little: their
  layer-1 fits over the same span are nearly as high as the layer-0 ones. The
  span's extent still reaches layer 1 through the averaging, so section 3's
  caution 1 applies there too.

Route (b) of that ruling (its RT-212 item 3) is this investigation.

## 3. The candidates, defined

All labels are facts about the episode, from the generator's own records
(`grammar.render`), never shown to any arm. "Turn k" is the k-th of the eight
assignment turns in text order.

- **Candidate 1 — which two assignment turns are the model's own.** This is the
  review's wording made precise.
  - The label is an unordered pair out of eight. Every agent makes exactly two
    assignment turns, one per item, and a check before the code was committed
    confirmed the pair is exactly the turns the acting channel marks.
  - The read is one softmax over the eight turns, with each training episode
    entered once per own turn. Its prediction is the two highest-scoring turns,
    right only if that exact pair.
  - Blind guessing scores about 1 in 28. The null mean was 0.033 to 0.038.
- **Candidate 2 — which assignment turn holds the model's own value on the asked
  item.** Only the one turn the own-directed action needs, a number from 0 to 7.
  Null mean 0.12 to 0.13.
- **Candidate 3 — the model's own value on the asked item.** One of eight value
  words. The correct answer is its successor, so this read sits close to the
  arm's own output (method, section 2). Null mean 0.12 to 0.13.
- **Reference, not a candidate — the ruled label**, which marker word is the
  model's own. Twelve marker words occur in the development pool. Null mean 0.08
  to 0.09.

For context, each arm's own-directed accuracy on the 3,000 gate episodes
(`out-repairs/gate_base.json`):

| arm | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| F | 0.560 | 0.551 | 0.555 |
| T | 1.000 | 1.000 | 1.000 |
| C | 0.570 | 0.568 | 0.576 |
| M | 0.864 | 0.861 | 0.867 |

## 4. Verdicts

The best fit anywhere is on the left; the best at the 45 fixed-extent site sets is
on the right. Each has seeds 0 / 1 / 2. No cell for any candidate clears 0.80.

| label | arm | clears on the arm? | best fit, all 60 site sets | best fit, fixed-extent 45 |
|---|---|---|---|---|
| candidate 1 | **F** | **no** | 0.733 / 0.483 / 0.789 | 0.733 / 0.383 / 0.478 |
| candidate 1 | T | no | 0.289 / 0.294 / 0.283 | 0.067 / 0.067 / 0.067 |
| candidate 1 | C | no | 0.411 / 0.522 / 0.428 | 0.406 / 0.389 / 0.211 |
| candidate 1 | M | no | 0.311 / 0.372 / 0.411 | 0.083 / 0.150 / 0.244 |
| candidate 2 | **F** | **no** | 0.450 / 0.450 / 0.456 | 0.356 / 0.311 / 0.417 |
| candidate 2 | T | no | 0.411 / 0.400 / 0.400 | 0.228 / 0.194 / 0.200 |
| candidate 2 | C | no | 0.433 / 0.456 / 0.439 | 0.383 / 0.294 / 0.306 |
| candidate 2 | M | no | 0.417 / 0.367 / 0.378 | 0.211 / 0.222 / 0.278 |
| candidate 3 | **F** | **no** | 0.611 / 0.611 / 0.633 | 0.611 / 0.611 / 0.633 |
| candidate 3 | T | no | 0.344 / 0.361 / 0.350 | 0.206 / 0.250 / 0.211 |
| candidate 3 | C | no | 0.578 / 0.600 / 0.578 | 0.578 / 0.600 / 0.578 |
| candidate 3 | M | no | 0.478 / 0.394 / 0.467 | 0.478 / 0.394 / 0.467 |
| reference | **F** | **no** | 0.556 / 0.483 / 0.433 | 0.206 / 0.144 / 0.211 |
| reference | T | yes, 60 of 60 site sets | 1.000 | 1.000 |
| reference | C | yes, 56 of 60 (42 of 45 fixed-extent) | 1.000 | 1.000 |
| reference | M | yes, 60 of 60 | 1.000 | 1.000 |

Every best fit on every arm beats all 200 of its shuffles. On arm F the gap is
wide:
- candidate 1: 0.483 to 0.789 against a highest shuffle of 0.100;
- candidate 2: 0.450 to 0.456 against 0.239;
- candidate 3: 0.611 to 0.633 against 0.239.

So these quantities are carried by arm F, but not at four fifths.

The stop rule fired twice: candidate 1 failed on arm F, so candidate 2 ran; that
failed, so candidate 3 ran. Candidate 3 is the last the method allows. The search
stopped there.

## 5. Things the tables show that a reader should know (MEASURED, read off the tables below)

1. **Where candidate 1 sits on arm F.**
   - It is strongest at layers 0 to 1, in the tokens of the action turn
     (`action+3`: 0.733 on seed 0) or averaged over the post-identity span (0.789
     on seed 2).
   - Layer 1 alone does nearly as well (0.722 and 0.783), while layer 0 alone is
     near chance at the fixed-extent sites (0.028 to 0.039). So the first block
     builds it.
   - It fades with depth: at layer 4 alone the best per seed is 0.478, 0.228 and
     0.600.
   - It varies a lot between seeds. Seed 1 never exceeds 0.483, and only 0.383
     at a fixed-extent site set.
2. **The constructed arms carry candidate 1 weakly, and that is expected.**
   - Arm T reaches only 0.28 to 0.29, and only over the post-identity span. At
     the action it sits at 0.067 or below.
   - Its ownership answer is built from marker words and read through a
     dedicated slot, so it never needs to know which turns are its own at the
     action.
   - This is the mirror image of the ruled label: each arm carries the quantity
     its route to the answer uses.
3. **Candidate 2's best site set is at layer 0, or a layer set starting there,
   over the post-identity span, on every seed of every arm (0.37 to 0.46).**
   - Layer 0 is the input plus the acting channel, before any block has run.
   - What makes it readable there is where the span starts: the model's first
     own turn, which is the asked turn in about half the episodes. This is the
     leak the method named before any output (section 3, caution 1), not
     something the network built.
   - At fixed-extent site sets arm F reaches only 0.31 to 0.42.
4. **The ruled label shows the same leak.**
   - At layer 0 over the post-identity span it reads 0.43 to 0.44 on arm F and
     0.70 to 0.87 on arm C. There the span's first token is the model's own
     marker word.
   - At the fixed-extent site sets on arm F the ruled label's best is 0.14 to
     0.21. Its action-position figures at layer 1 (0.172, 0.067 and 0.106)
     reproduce RT-212.
5. **Candidate 3 on arm F.**
   - Its best is 0.611 to 0.633, at the action or the action and the token
     before it. That is a little above arm F's own-directed accuracy of 0.55 to
     0.56, so the read recovers the own value somewhat more often than the arm
     answers correctly.
   - As the method warned, this read sits beside the output.
   - Arm C is similar (0.58 to 0.60 against 0.57).

## 6. Per-site tables

Generated from the output files by
`experiments/rehearsal-successor-measure/src/label_search_report.py --label <label>`.
Layer sets are written "a–b" for layers a to b inclusive. Under each arm's grid:
the best site set per seed, its null (mean, 95th and 99th percentiles, highest
shuffle, of 200), how many shuffles reached its fit, how many of the 60 site sets
beat every shuffle, and the seconds the seed took.

### candidate 1: which two assignment turns are the model's own

**Arm F** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.028 / 0.028 / 0.028 | 0.028 / 0.028 / 0.028 | 0.039 / 0.039 / 0.033 | 0.233 / 0.233 / 0.239 |
| 0–1 | 0.167 / 0.133 / 0.244 | 0.594 / 0.111 / 0.411 | 0.733 / 0.372 / 0.394 | 0.672 / 0.483 / 0.789 |
| 0–2 | 0.283 / 0.117 / 0.289 | 0.433 / 0.133 / 0.433 | 0.550 / 0.256 / 0.417 | 0.644 / 0.400 / 0.767 |
| 0–3 | 0.278 / 0.144 / 0.333 | 0.333 / 0.111 / 0.411 | 0.400 / 0.189 / 0.350 | 0.611 / 0.306 / 0.728 |
| 0–4 | 0.289 / 0.167 / 0.328 | 0.339 / 0.106 / 0.428 | 0.294 / 0.183 / 0.333 | 0.533 / 0.267 / 0.706 |
| 1 | 0.167 / 0.128 / 0.233 | 0.572 / 0.100 / 0.400 | 0.722 / 0.383 / 0.394 | 0.656 / 0.394 / 0.783 |
| 1–2 | 0.278 / 0.122 / 0.289 | 0.422 / 0.128 / 0.439 | 0.550 / 0.267 / 0.400 | 0.633 / 0.350 / 0.778 |
| 1–3 | 0.289 / 0.150 / 0.333 | 0.333 / 0.111 / 0.422 | 0.378 / 0.183 / 0.367 | 0.611 / 0.278 / 0.694 |
| 1–4 | 0.272 / 0.161 / 0.322 | 0.339 / 0.100 / 0.411 | 0.300 / 0.172 / 0.333 | 0.506 / 0.239 / 0.694 |
| 2 | 0.300 / 0.083 / 0.267 | 0.400 / 0.117 / 0.478 | 0.467 / 0.222 / 0.406 | 0.583 / 0.339 / 0.722 |
| 2–3 | 0.261 / 0.128 / 0.333 | 0.339 / 0.111 / 0.433 | 0.339 / 0.156 / 0.367 | 0.544 / 0.250 / 0.672 |
| 2–4 | 0.272 / 0.128 / 0.322 | 0.317 / 0.094 / 0.417 | 0.256 / 0.156 / 0.344 | 0.478 / 0.233 / 0.683 |
| 3 | 0.194 / 0.106 / 0.289 | 0.300 / 0.111 / 0.356 | 0.361 / 0.178 / 0.372 | 0.533 / 0.267 / 0.644 |
| 3–4 | 0.250 / 0.111 / 0.272 | 0.306 / 0.094 / 0.383 | 0.233 / 0.178 / 0.339 | 0.456 / 0.244 / 0.650 |
| 4 | 0.128 / 0.128 / 0.278 | 0.261 / 0.089 / 0.361 | 0.283 / 0.194 / 0.344 | 0.478 / 0.228 / 0.600 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0–1, action+3 | 0.733 | 0.037 | 0.061 | 0.072 | 0.100 | 0 of 200 | 57 of 60 | 211 |
| 1 | layers 0–1, post-identity | 0.483 | 0.035 | 0.061 | 0.078 | 0.083 | 0 of 200 | 56 of 60 | 46 |
| 2 | layers 0–1, post-identity | 0.789 | 0.036 | 0.061 | 0.072 | 0.078 | 0 of 200 | 57 of 60 | 53 |

**Arm T** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.067 / 0.067 / 0.067 | 0.067 / 0.067 / 0.067 | 0.033 / 0.033 / 0.033 | 0.250 / 0.261 / 0.239 |
| 0–1 | 0.044 / 0.044 / 0.056 | 0.056 / 0.050 / 0.050 | 0.028 / 0.033 / 0.033 | 0.250 / 0.272 / 0.256 |
| 0–2 | 0.039 / 0.039 / 0.033 | 0.033 / 0.033 / 0.039 | 0.022 / 0.022 / 0.017 | 0.261 / 0.267 / 0.272 |
| 0–3 | 0.028 / 0.022 / 0.033 | 0.017 / 0.017 / 0.017 | 0.011 / 0.039 / 0.022 | 0.261 / 0.261 / 0.278 |
| 0–4 | 0.006 / 0.022 / 0.017 | 0.028 / 0.028 / 0.039 | 0.017 / 0.050 / 0.033 | 0.289 / 0.278 / 0.283 |
| 1 | 0.044 / 0.044 / 0.067 | 0.056 / 0.050 / 0.050 | 0.033 / 0.033 / 0.033 | 0.256 / 0.272 / 0.256 |
| 1–2 | 0.039 / 0.039 / 0.039 | 0.033 / 0.033 / 0.039 | 0.022 / 0.022 / 0.017 | 0.250 / 0.278 / 0.267 |
| 1–3 | 0.028 / 0.022 / 0.033 | 0.017 / 0.022 / 0.017 | 0.011 / 0.039 / 0.022 | 0.239 / 0.267 / 0.278 |
| 1–4 | 0.006 / 0.022 / 0.022 | 0.028 / 0.022 / 0.028 | 0.017 / 0.050 / 0.033 | 0.289 / 0.272 / 0.278 |
| 2 | 0.050 / 0.044 / 0.039 | 0.044 / 0.050 / 0.044 | 0.022 / 0.022 / 0.022 | 0.244 / 0.261 / 0.272 |
| 2–3 | 0.028 / 0.033 / 0.033 | 0.022 / 0.022 / 0.022 | 0.011 / 0.033 / 0.022 | 0.250 / 0.283 / 0.283 |
| 2–4 | 0.011 / 0.022 / 0.017 | 0.022 / 0.028 / 0.028 | 0.017 / 0.044 / 0.028 | 0.272 / 0.278 / 0.261 |
| 3 | 0.033 / 0.044 / 0.039 | 0.022 / 0.028 / 0.028 | 0.017 / 0.022 / 0.017 | 0.250 / 0.294 / 0.278 |
| 3–4 | 0.017 / 0.022 / 0.017 | 0.022 / 0.028 / 0.028 | 0.011 / 0.050 / 0.028 | 0.267 / 0.278 / 0.278 |
| 4 | 0.039 / 0.039 / 0.022 | 0.028 / 0.028 / 0.006 | 0.017 / 0.044 / 0.011 | 0.283 / 0.272 / 0.283 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0–4, post-identity | 0.289 | 0.034 | 0.061 | 0.072 | 0.078 | 0 of 200 | 15 of 60 | 33 |
| 1 | layers 3, post-identity | 0.294 | 0.035 | 0.056 | 0.078 | 0.078 | 0 of 200 | 15 of 60 | 16 |
| 2 | layers 0–4, post-identity | 0.283 | 0.033 | 0.056 | 0.078 | 0.083 | 0 of 200 | 15 of 60 | 37 |

**Arm C** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.028 / 0.028 / 0.028 | 0.028 / 0.028 / 0.028 | 0.039 / 0.039 / 0.033 | 0.250 / 0.233 / 0.228 |
| 0–1 | 0.244 / 0.078 / 0.100 | 0.344 / 0.156 / 0.161 | 0.333 / 0.389 / 0.211 | 0.411 / 0.522 / 0.428 |
| 0–2 | 0.361 / 0.067 / 0.100 | 0.400 / 0.122 / 0.144 | 0.283 / 0.278 / 0.150 | 0.339 / 0.322 / 0.339 |
| 0–3 | 0.306 / 0.089 / 0.072 | 0.289 / 0.106 / 0.067 | 0.256 / 0.178 / 0.083 | 0.278 / 0.278 / 0.278 |
| 0–4 | 0.317 / 0.094 / 0.078 | 0.244 / 0.078 / 0.072 | 0.217 / 0.094 / 0.061 | 0.217 / 0.261 / 0.250 |
| 1 | 0.228 / 0.078 / 0.106 | 0.339 / 0.150 / 0.161 | 0.356 / 0.383 / 0.206 | 0.383 / 0.472 / 0.322 |
| 1–2 | 0.372 / 0.061 / 0.083 | 0.406 / 0.117 / 0.139 | 0.283 / 0.278 / 0.156 | 0.317 / 0.306 / 0.289 |
| 1–3 | 0.311 / 0.089 / 0.072 | 0.283 / 0.106 / 0.072 | 0.256 / 0.183 / 0.083 | 0.261 / 0.283 / 0.278 |
| 1–4 | 0.300 / 0.089 / 0.089 | 0.256 / 0.078 / 0.072 | 0.222 / 0.094 / 0.050 | 0.222 / 0.256 / 0.250 |
| 2 | 0.256 / 0.050 / 0.061 | 0.283 / 0.111 / 0.089 | 0.239 / 0.233 / 0.139 | 0.200 / 0.167 / 0.189 |
| 2–3 | 0.267 / 0.094 / 0.072 | 0.256 / 0.094 / 0.078 | 0.211 / 0.139 / 0.078 | 0.228 / 0.217 / 0.178 |
| 2–4 | 0.233 / 0.083 / 0.100 | 0.194 / 0.083 / 0.072 | 0.222 / 0.094 / 0.061 | 0.222 / 0.233 / 0.194 |
| 3 | 0.183 / 0.067 / 0.061 | 0.189 / 0.072 / 0.067 | 0.167 / 0.117 / 0.067 | 0.178 / 0.139 / 0.172 |
| 3–4 | 0.206 / 0.078 / 0.111 | 0.178 / 0.072 / 0.050 | 0.189 / 0.078 / 0.050 | 0.172 / 0.128 / 0.211 |
| 4 | 0.144 / 0.072 / 0.050 | 0.200 / 0.061 / 0.067 | 0.167 / 0.083 / 0.044 | 0.156 / 0.111 / 0.122 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0–1, post-identity | 0.411 | 0.036 | 0.061 | 0.072 | 0.078 | 0 of 200 | 57 of 60 | 40 |
| 1 | layers 0–1, post-identity | 0.522 | 0.038 | 0.061 | 0.078 | 0.100 | 0 of 200 | 31 of 60 | 41 |
| 2 | layers 0–1, post-identity | 0.428 | 0.035 | 0.061 | 0.072 | 0.078 | 0 of 200 | 34 of 60 | 76 |

**Arm M** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.067 / 0.067 / 0.067 | 0.067 / 0.067 / 0.067 | 0.033 / 0.033 / 0.033 | 0.244 / 0.261 / 0.261 |
| 0–1 | 0.050 / 0.033 / 0.083 | 0.067 / 0.150 / 0.178 | 0.061 / 0.100 / 0.244 | 0.311 / 0.372 / 0.411 |
| 0–2 | 0.050 / 0.083 / 0.150 | 0.050 / 0.100 / 0.183 | 0.067 / 0.072 / 0.222 | 0.228 / 0.233 / 0.317 |
| 0–3 | 0.028 / 0.044 / 0.106 | 0.039 / 0.072 / 0.139 | 0.050 / 0.056 / 0.144 | 0.167 / 0.139 / 0.278 |
| 0–4 | 0.039 / 0.078 / 0.083 | 0.033 / 0.061 / 0.100 | 0.078 / 0.050 / 0.111 | 0.133 / 0.133 / 0.250 |
| 1 | 0.039 / 0.039 / 0.083 | 0.067 / 0.144 / 0.172 | 0.067 / 0.106 / 0.244 | 0.289 / 0.278 / 0.350 |
| 1–2 | 0.044 / 0.089 / 0.139 | 0.050 / 0.100 / 0.183 | 0.078 / 0.067 / 0.222 | 0.217 / 0.211 / 0.294 |
| 1–3 | 0.028 / 0.044 / 0.106 | 0.044 / 0.072 / 0.133 | 0.050 / 0.050 / 0.133 | 0.156 / 0.150 / 0.250 |
| 1–4 | 0.039 / 0.078 / 0.089 | 0.033 / 0.056 / 0.122 | 0.072 / 0.044 / 0.100 | 0.128 / 0.139 / 0.239 |
| 2 | 0.056 / 0.050 / 0.144 | 0.061 / 0.083 / 0.156 | 0.083 / 0.067 / 0.211 | 0.139 / 0.122 / 0.228 |
| 2–3 | 0.033 / 0.044 / 0.100 | 0.039 / 0.061 / 0.117 | 0.050 / 0.044 / 0.144 | 0.139 / 0.128 / 0.206 |
| 2–4 | 0.044 / 0.067 / 0.067 | 0.033 / 0.072 / 0.111 | 0.067 / 0.033 / 0.094 | 0.122 / 0.111 / 0.217 |
| 3 | 0.033 / 0.039 / 0.072 | 0.033 / 0.056 / 0.111 | 0.056 / 0.039 / 0.133 | 0.100 / 0.100 / 0.161 |
| 3–4 | 0.050 / 0.067 / 0.067 | 0.028 / 0.083 / 0.083 | 0.056 / 0.017 / 0.111 | 0.094 / 0.122 / 0.156 |
| 4 | 0.039 / 0.044 / 0.106 | 0.044 / 0.089 / 0.072 | 0.056 / 0.022 / 0.111 | 0.094 / 0.094 / 0.139 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0–1, post-identity | 0.311 | 0.036 | 0.061 | 0.072 | 0.078 | 0 of 200 | 16 of 60 | 64 |
| 1 | layers 0–1, post-identity | 0.372 | 0.036 | 0.061 | 0.072 | 0.089 | 0 of 200 | 21 of 60 | 74 |
| 2 | layers 0–1, post-identity | 0.411 | 0.037 | 0.067 | 0.078 | 0.083 | 0 of 200 | 49 of 60 | 47 |

### candidate 2: which assignment turn holds the model's own value on the asked item

**Arm F** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.139 / 0.139 / 0.139 | 0.139 / 0.139 / 0.139 | 0.128 / 0.128 / 0.128 | 0.450 / 0.450 / 0.456 |
| 0–1 | 0.206 / 0.178 / 0.283 | 0.278 / 0.178 / 0.417 | 0.350 / 0.311 / 0.283 | 0.450 / 0.411 / 0.444 |
| 0–2 | 0.244 / 0.200 / 0.311 | 0.283 / 0.156 / 0.328 | 0.356 / 0.250 / 0.311 | 0.422 / 0.333 / 0.433 |
| 0–3 | 0.261 / 0.167 / 0.283 | 0.256 / 0.133 / 0.344 | 0.311 / 0.267 / 0.306 | 0.394 / 0.350 / 0.411 |
| 0–4 | 0.244 / 0.178 / 0.317 | 0.233 / 0.161 / 0.367 | 0.267 / 0.267 / 0.294 | 0.367 / 0.344 / 0.422 |
| 1 | 0.200 / 0.178 / 0.300 | 0.278 / 0.172 / 0.394 | 0.350 / 0.311 / 0.283 | 0.444 / 0.406 / 0.450 |
| 1–2 | 0.250 / 0.200 / 0.317 | 0.289 / 0.156 / 0.328 | 0.344 / 0.272 / 0.317 | 0.433 / 0.328 / 0.444 |
| 1–3 | 0.256 / 0.178 / 0.289 | 0.267 / 0.133 / 0.344 | 0.311 / 0.272 / 0.306 | 0.389 / 0.339 / 0.417 |
| 1–4 | 0.250 / 0.172 / 0.317 | 0.233 / 0.167 / 0.367 | 0.267 / 0.278 / 0.300 | 0.367 / 0.333 / 0.428 |
| 2 | 0.256 / 0.217 / 0.322 | 0.311 / 0.161 / 0.378 | 0.328 / 0.233 / 0.306 | 0.389 / 0.356 / 0.400 |
| 2–3 | 0.250 / 0.217 / 0.283 | 0.244 / 0.150 / 0.350 | 0.289 / 0.261 / 0.289 | 0.361 / 0.333 / 0.383 |
| 2–4 | 0.244 / 0.161 / 0.328 | 0.206 / 0.133 / 0.367 | 0.239 / 0.256 / 0.300 | 0.344 / 0.333 / 0.400 |
| 3 | 0.244 / 0.156 / 0.272 | 0.256 / 0.167 / 0.339 | 0.300 / 0.233 / 0.306 | 0.356 / 0.322 / 0.378 |
| 3–4 | 0.228 / 0.178 / 0.333 | 0.211 / 0.144 / 0.367 | 0.244 / 0.244 / 0.328 | 0.344 / 0.317 / 0.339 |
| 4 | 0.267 / 0.167 / 0.317 | 0.228 / 0.150 / 0.356 | 0.244 / 0.217 / 0.289 | 0.350 / 0.328 / 0.361 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0, post-identity | 0.450 | 0.128 | 0.183 | 0.200 | 0.233 | 0 of 200 | 49 of 60 | 14 |
| 1 | layers 0, post-identity | 0.450 | 0.129 | 0.184 | 0.206 | 0.239 | 0 of 200 | 26 of 60 | 8 |
| 2 | layers 0, post-identity | 0.456 | 0.129 | 0.183 | 0.211 | 0.233 | 0 of 200 | 57 of 60 | 7 |

**Arm T** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.144 / 0.144 / 0.144 | 0.144 / 0.144 / 0.144 | 0.139 / 0.139 / 0.139 | 0.411 / 0.378 / 0.389 |
| 0–1 | 0.156 / 0.139 / 0.156 | 0.156 / 0.161 / 0.144 | 0.178 / 0.183 / 0.200 | 0.400 / 0.400 / 0.389 |
| 0–2 | 0.150 / 0.156 / 0.161 | 0.150 / 0.144 / 0.167 | 0.194 / 0.161 / 0.172 | 0.383 / 0.394 / 0.400 |
| 0–3 | 0.139 / 0.133 / 0.161 | 0.139 / 0.139 / 0.178 | 0.206 / 0.183 / 0.156 | 0.372 / 0.389 / 0.394 |
| 0–4 | 0.128 / 0.144 / 0.172 | 0.144 / 0.167 / 0.167 | 0.228 / 0.172 / 0.139 | 0.367 / 0.372 / 0.389 |
| 1 | 0.156 / 0.139 / 0.156 | 0.150 / 0.167 / 0.150 | 0.178 / 0.183 / 0.194 | 0.383 / 0.361 / 0.389 |
| 1–2 | 0.156 / 0.156 / 0.161 | 0.144 / 0.144 / 0.167 | 0.194 / 0.161 / 0.172 | 0.378 / 0.383 / 0.400 |
| 1–3 | 0.139 / 0.139 / 0.161 | 0.139 / 0.139 / 0.178 | 0.206 / 0.178 / 0.156 | 0.372 / 0.389 / 0.383 |
| 1–4 | 0.139 / 0.144 / 0.172 | 0.144 / 0.161 / 0.167 | 0.228 / 0.172 / 0.139 | 0.383 / 0.389 / 0.383 |
| 2 | 0.139 / 0.161 / 0.156 | 0.150 / 0.133 / 0.167 | 0.189 / 0.167 / 0.172 | 0.367 / 0.361 / 0.389 |
| 2–3 | 0.122 / 0.156 / 0.161 | 0.133 / 0.139 / 0.178 | 0.211 / 0.172 / 0.156 | 0.372 / 0.378 / 0.389 |
| 2–4 | 0.133 / 0.150 / 0.172 | 0.150 / 0.167 / 0.156 | 0.222 / 0.194 / 0.139 | 0.394 / 0.378 / 0.389 |
| 3 | 0.133 / 0.167 / 0.167 | 0.128 / 0.150 / 0.183 | 0.200 / 0.161 / 0.167 | 0.383 / 0.367 / 0.378 |
| 3–4 | 0.133 / 0.144 / 0.156 | 0.139 / 0.156 / 0.161 | 0.211 / 0.194 / 0.144 | 0.383 / 0.383 / 0.372 |
| 4 | 0.133 / 0.144 / 0.172 | 0.144 / 0.144 / 0.183 | 0.200 / 0.167 / 0.156 | 0.394 / 0.367 / 0.383 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0, post-identity | 0.411 | 0.124 | 0.167 | 0.189 | 0.217 | 0 of 200 | 18 of 60 | 7 |
| 1 | layers 0–1, post-identity | 0.400 | 0.129 | 0.172 | 0.200 | 0.200 | 0 of 200 | 15 of 60 | 8 |
| 2 | layers 0–2, post-identity | 0.400 | 0.124 | 0.183 | 0.206 | 0.228 | 0 of 200 | 15 of 60 | 11 |

**Arm C** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.139 / 0.139 / 0.139 | 0.139 / 0.139 / 0.139 | 0.128 / 0.128 / 0.128 | 0.433 / 0.456 / 0.439 |
| 0–1 | 0.378 / 0.172 / 0.217 | 0.383 / 0.244 / 0.256 | 0.328 / 0.294 / 0.300 | 0.361 / 0.394 / 0.361 |
| 0–2 | 0.333 / 0.167 / 0.239 | 0.367 / 0.228 / 0.256 | 0.322 / 0.261 / 0.244 | 0.350 / 0.294 / 0.367 |
| 0–3 | 0.339 / 0.161 / 0.239 | 0.322 / 0.233 / 0.233 | 0.300 / 0.217 / 0.228 | 0.294 / 0.300 / 0.294 |
| 0–4 | 0.311 / 0.206 / 0.189 | 0.356 / 0.183 / 0.222 | 0.306 / 0.217 / 0.200 | 0.261 / 0.328 / 0.283 |
| 1 | 0.372 / 0.172 / 0.222 | 0.383 / 0.256 / 0.256 | 0.333 / 0.294 / 0.306 | 0.328 / 0.378 / 0.311 |
| 1–2 | 0.328 / 0.161 / 0.239 | 0.367 / 0.233 / 0.261 | 0.322 / 0.256 / 0.244 | 0.339 / 0.283 / 0.344 |
| 1–3 | 0.339 / 0.161 / 0.228 | 0.317 / 0.239 / 0.239 | 0.306 / 0.239 / 0.222 | 0.294 / 0.300 / 0.294 |
| 1–4 | 0.311 / 0.206 / 0.189 | 0.361 / 0.183 / 0.233 | 0.294 / 0.222 / 0.200 | 0.261 / 0.322 / 0.283 |
| 2 | 0.306 / 0.167 / 0.189 | 0.356 / 0.239 / 0.250 | 0.306 / 0.239 / 0.244 | 0.306 / 0.256 / 0.322 |
| 2–3 | 0.322 / 0.156 / 0.217 | 0.322 / 0.267 / 0.217 | 0.311 / 0.206 / 0.206 | 0.278 / 0.294 / 0.272 |
| 2–4 | 0.306 / 0.183 / 0.172 | 0.333 / 0.200 / 0.217 | 0.306 / 0.217 / 0.183 | 0.272 / 0.322 / 0.256 |
| 3 | 0.294 / 0.117 / 0.194 | 0.300 / 0.217 / 0.206 | 0.261 / 0.189 / 0.194 | 0.250 / 0.267 / 0.244 |
| 3–4 | 0.267 / 0.172 / 0.161 | 0.328 / 0.200 / 0.222 | 0.289 / 0.194 / 0.172 | 0.267 / 0.311 / 0.228 |
| 4 | 0.283 / 0.183 / 0.144 | 0.333 / 0.183 / 0.211 | 0.311 / 0.206 / 0.189 | 0.267 / 0.283 / 0.233 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0, post-identity | 0.433 | 0.127 | 0.183 | 0.200 | 0.244 | 0 of 200 | 57 of 60 | 4 |
| 1 | layers 0, post-identity | 0.456 | 0.128 | 0.184 | 0.206 | 0.217 | 0 of 200 | 30 of 60 | 5 |
| 2 | layers 0, post-identity | 0.439 | 0.128 | 0.183 | 0.206 | 0.244 | 0 of 200 | 19 of 60 | 7 |

**Arm M** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.144 / 0.144 / 0.144 | 0.144 / 0.144 / 0.144 | 0.139 / 0.139 / 0.139 | 0.417 / 0.367 / 0.378 |
| 0–1 | 0.156 / 0.139 / 0.244 | 0.206 / 0.167 / 0.278 | 0.156 / 0.200 / 0.278 | 0.350 / 0.306 / 0.344 |
| 0–2 | 0.150 / 0.178 / 0.189 | 0.200 / 0.128 / 0.250 | 0.189 / 0.211 / 0.272 | 0.289 / 0.250 / 0.283 |
| 0–3 | 0.161 / 0.144 / 0.172 | 0.161 / 0.144 / 0.194 | 0.156 / 0.161 / 0.272 | 0.194 / 0.272 / 0.278 |
| 0–4 | 0.144 / 0.150 / 0.144 | 0.144 / 0.150 / 0.183 | 0.156 / 0.183 / 0.222 | 0.172 / 0.283 / 0.217 |
| 1 | 0.161 / 0.139 / 0.250 | 0.211 / 0.172 / 0.278 | 0.156 / 0.222 / 0.278 | 0.328 / 0.261 / 0.350 |
| 1–2 | 0.150 / 0.178 / 0.194 | 0.206 / 0.128 / 0.250 | 0.183 / 0.206 / 0.267 | 0.272 / 0.239 / 0.283 |
| 1–3 | 0.161 / 0.144 / 0.172 | 0.161 / 0.144 / 0.194 | 0.156 / 0.161 / 0.272 | 0.200 / 0.267 / 0.278 |
| 1–4 | 0.139 / 0.150 / 0.139 | 0.144 / 0.150 / 0.189 | 0.156 / 0.183 / 0.222 | 0.167 / 0.278 / 0.211 |
| 2 | 0.172 / 0.167 / 0.172 | 0.167 / 0.117 / 0.233 | 0.183 / 0.200 / 0.256 | 0.250 / 0.239 / 0.256 |
| 2–3 | 0.139 / 0.167 / 0.139 | 0.178 / 0.144 / 0.200 | 0.161 / 0.156 / 0.261 | 0.217 / 0.250 / 0.239 |
| 2–4 | 0.133 / 0.133 / 0.117 | 0.144 / 0.139 / 0.178 | 0.144 / 0.178 / 0.217 | 0.178 / 0.294 / 0.222 |
| 3 | 0.133 / 0.133 / 0.150 | 0.156 / 0.150 / 0.161 | 0.150 / 0.139 / 0.244 | 0.172 / 0.250 / 0.233 |
| 3–4 | 0.133 / 0.144 / 0.111 | 0.144 / 0.128 / 0.156 | 0.133 / 0.156 / 0.211 | 0.144 / 0.272 / 0.222 |
| 4 | 0.111 / 0.156 / 0.122 | 0.106 / 0.167 / 0.139 | 0.122 / 0.200 / 0.172 | 0.156 / 0.244 / 0.211 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0, post-identity | 0.417 | 0.124 | 0.172 | 0.183 | 0.194 | 0 of 200 | 12 of 60 | 7 |
| 1 | layers 0, post-identity | 0.367 | 0.124 | 0.172 | 0.189 | 0.194 | 0 of 200 | 21 of 60 | 8 |
| 2 | layers 0, post-identity | 0.378 | 0.123 | 0.178 | 0.183 | 0.189 | 0 of 200 | 39 of 60 | 6 |

### candidate 3: the model's own value on the asked item

**Arm F** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.122 / 0.161 / 0.122 | 0.122 / 0.161 / 0.122 | 0.111 / 0.111 / 0.111 | 0.317 / 0.317 / 0.328 |
| 0–1 | 0.294 / 0.244 / 0.456 | 0.228 / 0.372 / 0.472 | 0.222 / 0.589 / 0.483 | 0.461 / 0.411 / 0.500 |
| 0–2 | 0.489 / 0.600 / 0.556 | 0.478 / 0.561 / 0.533 | 0.483 / 0.572 / 0.550 | 0.528 / 0.450 / 0.556 |
| 0–3 | 0.550 / 0.589 / 0.572 | 0.578 / 0.594 / 0.633 | 0.578 / 0.589 / 0.611 | 0.533 / 0.461 / 0.544 |
| 0–4 | 0.528 / 0.539 / 0.589 | 0.606 / 0.567 / 0.583 | 0.589 / 0.583 / 0.572 | 0.506 / 0.439 / 0.528 |
| 1 | 0.294 / 0.250 / 0.456 | 0.233 / 0.367 / 0.483 | 0.217 / 0.594 / 0.478 | 0.461 / 0.400 / 0.494 |
| 1–2 | 0.489 / 0.611 / 0.556 | 0.478 / 0.556 / 0.539 | 0.489 / 0.572 / 0.544 | 0.506 / 0.456 / 0.550 |
| 1–3 | 0.539 / 0.578 / 0.572 | 0.572 / 0.600 / 0.633 | 0.578 / 0.583 / 0.600 | 0.544 / 0.433 / 0.544 |
| 1–4 | 0.533 / 0.539 / 0.589 | 0.606 / 0.567 / 0.583 | 0.583 / 0.589 / 0.567 | 0.506 / 0.450 / 0.528 |
| 2 | 0.456 / 0.556 / 0.522 | 0.483 / 0.589 / 0.517 | 0.500 / 0.589 / 0.550 | 0.511 / 0.467 / 0.544 |
| 2–3 | 0.533 / 0.589 / 0.600 | 0.561 / 0.611 / 0.628 | 0.583 / 0.583 / 0.628 | 0.544 / 0.439 / 0.567 |
| 2–4 | 0.550 / 0.550 / 0.578 | 0.589 / 0.567 / 0.578 | 0.583 / 0.578 / 0.583 | 0.489 / 0.456 / 0.522 |
| 3 | 0.544 / 0.578 / 0.606 | 0.561 / 0.567 / 0.628 | 0.572 / 0.550 / 0.611 | 0.539 / 0.428 / 0.567 |
| 3–4 | 0.578 / 0.572 / 0.578 | 0.606 / 0.572 / 0.594 | 0.583 / 0.556 / 0.572 | 0.494 / 0.456 / 0.506 |
| 4 | 0.578 / 0.550 / 0.556 | 0.611 / 0.567 / 0.572 | 0.583 / 0.567 / 0.600 | 0.528 / 0.450 / 0.511 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 4, action+ans | 0.611 | 0.125 | 0.167 | 0.178 | 0.189 | 0 of 200 | 57 of 60 | 26 |
| 1 | layers 1–2, action | 0.611 | 0.130 | 0.178 | 0.217 | 0.239 | 0 of 200 | 57 of 60 | 16 |
| 2 | layers 0–3, action+ans | 0.633 | 0.122 | 0.172 | 0.200 | 0.200 | 0 of 200 | 57 of 60 | 52 |

**Arm T** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.111 / 0.094 / 0.094 | 0.106 / 0.094 / 0.094 | 0.111 / 0.111 / 0.111 | 0.289 / 0.306 / 0.289 |
| 0–1 | 0.161 / 0.150 / 0.156 | 0.144 / 0.167 / 0.139 | 0.139 / 0.172 / 0.156 | 0.317 / 0.333 / 0.328 |
| 0–2 | 0.183 / 0.167 / 0.156 | 0.189 / 0.200 / 0.161 | 0.183 / 0.200 / 0.172 | 0.339 / 0.344 / 0.322 |
| 0–3 | 0.194 / 0.211 / 0.183 | 0.183 / 0.228 / 0.189 | 0.206 / 0.222 / 0.161 | 0.344 / 0.350 / 0.333 |
| 0–4 | 0.183 / 0.222 / 0.206 | 0.183 / 0.222 / 0.206 | 0.189 / 0.244 / 0.178 | 0.344 / 0.350 / 0.339 |
| 1 | 0.161 / 0.150 / 0.156 | 0.144 / 0.167 / 0.133 | 0.139 / 0.172 / 0.156 | 0.300 / 0.322 / 0.322 |
| 1–2 | 0.194 / 0.167 / 0.156 | 0.189 / 0.200 / 0.161 | 0.183 / 0.200 / 0.172 | 0.339 / 0.344 / 0.333 |
| 1–3 | 0.194 / 0.211 / 0.183 | 0.183 / 0.228 / 0.189 | 0.206 / 0.222 / 0.167 | 0.333 / 0.361 / 0.333 |
| 1–4 | 0.183 / 0.217 / 0.206 | 0.183 / 0.217 / 0.206 | 0.189 / 0.244 / 0.178 | 0.339 / 0.350 / 0.333 |
| 2 | 0.178 / 0.150 / 0.156 | 0.167 / 0.189 / 0.133 | 0.178 / 0.200 / 0.172 | 0.333 / 0.350 / 0.317 |
| 2–3 | 0.172 / 0.217 / 0.183 | 0.189 / 0.228 / 0.189 | 0.200 / 0.228 / 0.167 | 0.339 / 0.339 / 0.350 |
| 2–4 | 0.189 / 0.228 / 0.200 | 0.194 / 0.222 / 0.211 | 0.200 / 0.239 / 0.172 | 0.339 / 0.350 / 0.339 |
| 3 | 0.172 / 0.194 / 0.139 | 0.200 / 0.228 / 0.194 | 0.189 / 0.239 / 0.167 | 0.322 / 0.339 / 0.333 |
| 3–4 | 0.189 / 0.217 / 0.194 | 0.183 / 0.211 / 0.200 | 0.194 / 0.239 / 0.172 | 0.339 / 0.350 / 0.333 |
| 4 | 0.178 / 0.206 / 0.167 | 0.178 / 0.211 / 0.206 | 0.178 / 0.250 / 0.189 | 0.317 / 0.350 / 0.344 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0–3, post-identity | 0.344 | 0.128 | 0.172 | 0.183 | 0.189 | 0 of 200 | 25 of 60 | 13 |
| 1 | layers 1–3, post-identity | 0.361 | 0.128 | 0.172 | 0.189 | 0.206 | 0 of 200 | 40 of 60 | 13 |
| 2 | layers 2–3, post-identity | 0.350 | 0.126 | 0.172 | 0.183 | 0.200 | 0 of 200 | 21 of 60 | 13 |

**Arm C** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.122 / 0.161 / 0.161 | 0.161 / 0.122 / 0.122 | 0.111 / 0.111 / 0.111 | 0.356 / 0.322 / 0.344 |
| 0–1 | 0.506 / 0.183 / 0.400 | 0.544 / 0.178 / 0.400 | 0.533 / 0.500 / 0.444 | 0.450 / 0.383 / 0.406 |
| 0–2 | 0.500 / 0.256 / 0.539 | 0.550 / 0.306 / 0.533 | 0.528 / 0.522 / 0.572 | 0.467 / 0.356 / 0.467 |
| 0–3 | 0.522 / 0.578 / 0.528 | 0.533 / 0.544 / 0.517 | 0.550 / 0.550 / 0.544 | 0.478 / 0.356 / 0.489 |
| 0–4 | 0.522 / 0.589 / 0.511 | 0.539 / 0.578 / 0.517 | 0.567 / 0.556 / 0.572 | 0.417 / 0.322 / 0.478 |
| 1 | 0.517 / 0.183 / 0.400 | 0.539 / 0.172 / 0.406 | 0.539 / 0.506 / 0.439 | 0.444 / 0.361 / 0.406 |
| 1–2 | 0.489 / 0.267 / 0.528 | 0.539 / 0.306 / 0.533 | 0.533 / 0.533 / 0.572 | 0.461 / 0.328 / 0.467 |
| 1–3 | 0.522 / 0.583 / 0.528 | 0.528 / 0.544 / 0.517 | 0.544 / 0.561 / 0.550 | 0.467 / 0.356 / 0.483 |
| 1–4 | 0.517 / 0.589 / 0.506 | 0.533 / 0.561 / 0.511 | 0.556 / 0.539 / 0.578 | 0.417 / 0.322 / 0.478 |
| 2 | 0.478 / 0.244 / 0.533 | 0.500 / 0.306 / 0.539 | 0.533 / 0.539 / 0.556 | 0.478 / 0.289 / 0.456 |
| 2–3 | 0.528 / 0.589 / 0.528 | 0.533 / 0.544 / 0.522 | 0.578 / 0.561 / 0.544 | 0.450 / 0.311 / 0.467 |
| 2–4 | 0.528 / 0.594 / 0.494 | 0.533 / 0.572 / 0.522 | 0.561 / 0.544 / 0.578 | 0.422 / 0.306 / 0.483 |
| 3 | 0.561 / 0.567 / 0.556 | 0.561 / 0.556 / 0.500 | 0.572 / 0.589 / 0.550 | 0.433 / 0.294 / 0.494 |
| 3–4 | 0.550 / 0.600 / 0.511 | 0.539 / 0.572 / 0.528 | 0.572 / 0.556 / 0.578 | 0.411 / 0.300 / 0.467 |
| 4 | 0.544 / 0.567 / 0.528 | 0.561 / 0.556 / 0.528 | 0.561 / 0.533 / 0.556 | 0.372 / 0.256 / 0.456 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 2–3, action+3 | 0.578 | 0.129 | 0.178 | 0.200 | 0.250 | 0 of 200 | 57 of 60 | 12 |
| 1 | layers 3–4, action | 0.600 | 0.128 | 0.178 | 0.206 | 0.261 | 0 of 200 | 50 of 60 | 6 |
| 2 | layers 1–4, action+3 | 0.578 | 0.124 | 0.172 | 0.189 | 0.211 | 0 of 200 | 57 of 60 | 42 |

**Arm M** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.094 / 0.094 / 0.094 | 0.094 / 0.094 / 0.094 | 0.111 / 0.111 / 0.111 | 0.311 / 0.328 / 0.311 |
| 0–1 | 0.161 / 0.139 / 0.294 | 0.200 / 0.183 / 0.306 | 0.133 / 0.150 / 0.300 | 0.367 / 0.311 / 0.400 |
| 0–2 | 0.389 / 0.311 / 0.422 | 0.333 / 0.322 / 0.422 | 0.406 / 0.344 / 0.400 | 0.317 / 0.289 / 0.422 |
| 0–3 | 0.428 / 0.344 / 0.467 | 0.439 / 0.300 / 0.456 | 0.433 / 0.372 / 0.433 | 0.322 / 0.250 / 0.350 |
| 0–4 | 0.378 / 0.383 / 0.439 | 0.439 / 0.356 / 0.406 | 0.478 / 0.389 / 0.439 | 0.294 / 0.239 / 0.361 |
| 1 | 0.161 / 0.133 / 0.294 | 0.200 / 0.178 / 0.306 | 0.133 / 0.128 / 0.306 | 0.350 / 0.272 / 0.400 |
| 1–2 | 0.383 / 0.311 / 0.433 | 0.328 / 0.322 / 0.422 | 0.400 / 0.350 / 0.400 | 0.311 / 0.267 / 0.428 |
| 1–3 | 0.433 / 0.339 / 0.461 | 0.439 / 0.300 / 0.456 | 0.433 / 0.372 / 0.433 | 0.328 / 0.244 / 0.350 |
| 1–4 | 0.378 / 0.383 / 0.433 | 0.433 / 0.356 / 0.406 | 0.478 / 0.389 / 0.433 | 0.294 / 0.233 / 0.361 |
| 2 | 0.350 / 0.306 / 0.439 | 0.322 / 0.317 / 0.422 | 0.417 / 0.372 / 0.400 | 0.311 / 0.256 / 0.411 |
| 2–3 | 0.450 / 0.333 / 0.433 | 0.428 / 0.311 / 0.456 | 0.433 / 0.350 / 0.422 | 0.361 / 0.239 / 0.350 |
| 2–4 | 0.367 / 0.389 / 0.422 | 0.439 / 0.367 / 0.411 | 0.472 / 0.389 / 0.444 | 0.306 / 0.206 / 0.350 |
| 3 | 0.417 / 0.333 / 0.417 | 0.422 / 0.300 / 0.422 | 0.433 / 0.328 / 0.428 | 0.339 / 0.211 / 0.339 |
| 3–4 | 0.378 / 0.356 / 0.417 | 0.428 / 0.356 / 0.394 | 0.461 / 0.394 / 0.433 | 0.306 / 0.217 / 0.361 |
| 4 | 0.350 / 0.350 / 0.428 | 0.417 / 0.361 / 0.406 | 0.478 / 0.367 / 0.428 | 0.300 / 0.206 / 0.367 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0–4, action+3 | 0.478 | 0.125 | 0.172 | 0.189 | 0.211 | 0 of 200 | 51 of 60 | 46 |
| 1 | layers 3–4, action+3 | 0.394 | 0.127 | 0.178 | 0.194 | 0.206 | 0 of 200 | 49 of 60 | 19 |
| 2 | layers 0–3, action | 0.467 | 0.126 | 0.167 | 0.178 | 0.183 | 0 of 200 | 57 of 60 | 18 |

### reference: which marker word is the model's own (the ruled label)

**Arm F** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.072 / 0.072 / 0.072 | 0.078 / 0.072 / 0.072 | 0.078 / 0.078 / 0.078 | 0.444 / 0.433 / 0.433 |
| 0–1 | 0.172 / 0.061 / 0.106 | 0.200 / 0.094 / 0.211 | 0.150 / 0.122 / 0.167 | 0.556 / 0.483 / 0.428 |
| 0–2 | 0.144 / 0.094 / 0.133 | 0.150 / 0.089 / 0.211 | 0.189 / 0.083 / 0.133 | 0.528 / 0.406 / 0.367 |
| 0–3 | 0.117 / 0.094 / 0.117 | 0.128 / 0.083 / 0.183 | 0.183 / 0.089 / 0.150 | 0.506 / 0.328 / 0.322 |
| 0–4 | 0.100 / 0.106 / 0.133 | 0.122 / 0.106 / 0.172 | 0.156 / 0.072 / 0.161 | 0.483 / 0.267 / 0.272 |
| 1 | 0.172 / 0.067 / 0.106 | 0.200 / 0.094 / 0.211 | 0.150 / 0.128 / 0.172 | 0.511 / 0.456 / 0.406 |
| 1–2 | 0.156 / 0.094 / 0.128 | 0.144 / 0.089 / 0.206 | 0.189 / 0.083 / 0.150 | 0.533 / 0.361 / 0.367 |
| 1–3 | 0.117 / 0.100 / 0.106 | 0.128 / 0.083 / 0.183 | 0.178 / 0.089 / 0.139 | 0.506 / 0.300 / 0.283 |
| 1–4 | 0.100 / 0.100 / 0.133 | 0.128 / 0.106 / 0.172 | 0.156 / 0.078 / 0.161 | 0.472 / 0.256 / 0.272 |
| 2 | 0.144 / 0.117 / 0.139 | 0.150 / 0.078 / 0.183 | 0.206 / 0.056 / 0.156 | 0.489 / 0.322 / 0.283 |
| 2–3 | 0.111 / 0.100 / 0.100 | 0.122 / 0.078 / 0.156 | 0.156 / 0.078 / 0.156 | 0.489 / 0.267 / 0.250 |
| 2–4 | 0.078 / 0.094 / 0.111 | 0.128 / 0.100 / 0.178 | 0.150 / 0.072 / 0.156 | 0.433 / 0.239 / 0.256 |
| 3 | 0.106 / 0.144 / 0.111 | 0.133 / 0.094 / 0.144 | 0.144 / 0.072 / 0.167 | 0.467 / 0.261 / 0.233 |
| 3–4 | 0.100 / 0.111 / 0.117 | 0.122 / 0.100 / 0.161 | 0.144 / 0.067 / 0.144 | 0.422 / 0.233 / 0.222 |
| 4 | 0.067 / 0.117 / 0.111 | 0.133 / 0.083 / 0.172 | 0.122 / 0.078 / 0.133 | 0.400 / 0.217 / 0.233 |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0–1, post-identity | 0.556 | 0.082 | 0.122 | 0.139 | 0.144 | 0 of 200 | 33 of 60 | 36 |
| 1 | layers 0–1, post-identity | 0.483 | 0.083 | 0.117 | 0.139 | 0.156 | 0 of 200 | 15 of 60 | 29 |
| 2 | layers 0, post-identity | 0.433 | 0.079 | 0.117 | 0.122 | 0.156 | 0 of 200 | 32 of 60 | 12 |

**Arm T** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 0–1 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 0–2 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 0–3 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 0–4 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 1 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 1–2 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 1–3 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 1–4 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 2 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 2–3 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 2–4 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 3 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 3–4 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 4 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0, action | 1.000 | 0.085 | 0.211 | 0.261 | 0.267 | 0 of 200 | 60 of 60 | 3 |
| 1 | layers 0, action | 1.000 | 0.086 | 0.217 | 0.261 | 0.267 | 0 of 200 | 60 of 60 | 3 |
| 2 | layers 0, action | 1.000 | 0.086 | 0.211 | 0.261 | 0.267 | 0 of 200 | 60 of 60 | 3 |

**Arm C** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | 0.072 / 0.072 / 0.072 | 0.072 / 0.072 / 0.072 | 0.078 / 0.078 / 0.078 | **0.872** / 0.700 / **0.800** |
| 0–1 | **0.994** / **0.983** / **0.989** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 0–2 | **1.000** / **0.989** / **0.989** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 0–3 | **1.000** / **0.983** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **0.994** / **1.000** |
| 0–4 | **1.000** / **0.989** / **1.000** | **1.000** / **0.989** / **1.000** | **0.994** / **0.994** / **1.000** | **1.000** / **1.000** / **1.000** |
| 1 | **0.994** / **0.983** / **0.978** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 1–2 | **1.000** / **0.983** / **0.989** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 1–3 | **1.000** / **0.983** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **0.994** / **1.000** |
| 1–4 | **1.000** / **0.989** / **1.000** | **1.000** / **0.989** / **1.000** | **0.994** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 2 | **1.000** / **0.967** / **0.983** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 2–3 | **1.000** / **0.983** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **0.994** / **1.000** |
| 2–4 | **1.000** / **0.989** / **1.000** | **1.000** / **0.989** / **1.000** | **0.994** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 3 | **1.000** / **0.983** / **1.000** | **1.000** / **0.994** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **0.994** / **1.000** |
| 3–4 | **1.000** / **0.989** / **1.000** | **0.994** / **0.989** / **1.000** | **0.994** / **0.994** / **1.000** | **1.000** / **1.000** / **1.000** |
| 4 | **1.000** / **0.961** / **1.000** | **0.994** / **0.978** / **1.000** | **0.994** / **0.989** / **1.000** | **0.994** / **1.000** / **1.000** |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0–1, action+ans | 1.000 | 0.082 | 0.128 | 0.150 | 0.156 | 0 of 200 | 57 of 60 | 19 |
| 1 | layers 0–1, action+ans | 1.000 | 0.085 | 0.128 | 0.139 | 0.150 | 0 of 200 | 57 of 60 | 23 |
| 2 | layers 0–1, action+ans | 1.000 | 0.083 | 0.122 | 0.150 | 0.161 | 0 of 200 | 57 of 60 | 34 |

**Arm M** — each cell: held-out fit for seeds 0 / 1 / 2. Bold: the site set clears on that seed (at least 0.80 and above every shuffle at that seed's best site set).

| layers | action | action+ans | action+3 | post-identity |
|---|---|---|---|---|
| 0 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 0–1 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 0–2 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 0–3 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 0–4 | **0.994** / **1.000** / **1.000** | **0.994** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 1 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 1–2 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 1–3 | **0.994** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 1–4 | **0.989** / **1.000** / **1.000** | **0.956** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 2 | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 2–3 | **0.994** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 2–4 | **0.989** / **1.000** / **1.000** | **0.994** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 3 | **0.989** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 3–4 | **0.989** / **1.000** / **1.000** | **0.978** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |
| 4 | **0.989** / **1.000** / **1.000** | **0.994** / **1.000** / **1.000** | **0.972** / **1.000** / **1.000** | **1.000** / **1.000** / **1.000** |

| seed | best site set | fit | null mean | 95th | 99th | highest shuffle | shuffles at or above the fit | site sets above every shuffle | seconds |
|---|---|---|---|---|---|---|---|---|---|
| 0 | layers 0, action | 1.000 | 0.085 | 0.211 | 0.261 | 0.267 | 0 of 200 | 60 of 60 | 2 |
| 1 | layers 0, action | 1.000 | 0.085 | 0.211 | 0.261 | 0.267 | 0 of 200 | 60 of 60 | 2 |
| 2 | layers 0, action | 1.000 | 0.085 | 0.211 | 0.261 | 0.267 | 0 of 200 | 60 of 60 | 2 |


## 7. In plain language

No. The free system carries three things that its own-directed task forces on it:
which of the earlier turns were its own, which of them holds the value it is asked
to revise, and what that value is. A straight-line read recovers each one far
above chance on arm F, but none of them gets to four fifths at any site on any
seed.
- The closest is which two turns were its own. It reaches 0.73 in the tokens of
  the action turn at the first two layers on one seed, and 0.79 averaged over the
  post-identity span on another. That span begins at one of those very turns, so
  the method had already said a fit there proves little. On the third seed it
  never passes 0.48.
- The model's own value on the asked item reaches 0.61 to 0.63 at the action, a
  little above how often the arm answers correctly.
- The ruled label reads perfectly on arms T and M and nearly so on arm C, and is
  near chance at arm F's fixed-extent sites.

At toy scale, then, no read the free system is forced to carry clears the floor on
arm F, on any of the 60 site sets.
