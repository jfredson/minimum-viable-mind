# The grammar attempt (redesign (c)) — findings

*Written 2026-09-25 (Pacific) by the Claude Code session "MVM W1c grammar
attempt", on branch `worktree-w1c-grammar-attempt`. The file keeps the name the
task gave it (dated 2026-09-26, the Saturday the ruling scheduled the attempt
for); the work ran a day early. **UNREGISTERED.** Nothing here is a result about
the scientific question, nothing here is a bar, and nothing here is a ruling.
The pass line was ruled by John (`docs/rulings/2026-09-25-rehearsal-repairs-rulings.md`
on branch `rulings-2026-09-25-repairs`, commit `e03288c`, item 1) and made exact
in the method note before the run; every other threshold is a rehearsal-only
one fixed in that note.*

*Ran locally on the laptop, on models of about one to one and a third million
parameters. **No machine was rented, no vendor was contacted and nothing was
spent: $0.***

*Method, committed before any code or output:
`docs/grammar-attempt-method-2026-09-25.md`. Code:
`experiments/rehearsal-successor-measure/src/grammar.py` (one new setting) and
`grammar_attempt.py` (the driver); the rehearsal-repairs driver it runs is
carried in unchanged from pull request 52. Every output file:
`experiments/rehearsal-successor-measure/out-grammar-c/`. Nothing in `out/` or
`out-repairs/` was written.*

*Every finding is labelled **MEASURED** (a command was run and its output is
reported, with the committed file it wrote) or **ARGUED** (reasoning a reader
can dispute). Arms C and F do not reproduce from code and seed on this laptop,
so `docs/rulings/2026-09-23-range-and-direction-only.md` limits what may be
quoted from them to a range and a direction; exact per-seed figures below are
the gate counts the ruled pass line is defined on, given as the repairs
findings gave them, and no decimal from those arms is offered as a property of
the code. Written under the workspace plain-language rule.*

---

## 0. What to read if you read nothing else

- **The pass line was not cleared.** On the free arm (arm F, the ordinarily
  trained system), the named-other condition — revise the value of the agent
  the turn names — got **774, 730 and 759 correct of 3,000** on seeds 0, 1 and
  2. The line needed 790 or more on at least two seeds; **none of the three
  reached it**. The other half of the line held: the own-directed condition's
  mean over the three seeds was 0.5654, at or above 0.5513.
  MEASURED, `out-grammar-c/passline.json`.
- **So under the ruling, fallback (d) is what registers.** The ruling's words:
  "if it does not, (d) is what registers". This file does not recommend
  anything beyond saying that.
- **The change made no visible difference to what the free arm does at the
  named-other turn.** It still gives its own value there only about one time
  in twenty, and splits most of the rest across the other agents' values —
  the same pattern as before the change. The method note's wager, made before
  the run, was that the change would not clear, for exactly this reason: the
  model already told the two turns apart and fails at a different step,
  matching the named marker word to that agent's value. MEASURED
  (`out-grammar-c/diagnose_named_other.json`) for the numbers; ARGUED for the
  reading.
- **Rehearsal items R-2, R-3 and R-4 hold on the new grammar; R-5 and R-6 are
  unchanged by construction; R-1 still fails on its named-other half**, on
  arm C (1 seed of 3) as well as arm F (0 of 3). Section 4.

---

## 1. What was committed when

| order | commit | what |
|---|---|---|
| 1 | `271d57c` | the method note, before any code or output |
| 2 | `aa85b5e` | the rehearsal-repairs driver carried in byte-for-byte from `e0626b2` (pull request 52, still open) |
| 3 | `94da045` | the grammar setting, its self-test checks, and the driver (code only) |
| 4 | `53eac6d` | the outputs |
| 5 | this file | the findings |

The method note precedes the first code commit and the first output. One
import check of the driver (it printed the setting, the output folder and the
site-set count, and wrote nothing) was run before commit 3.

---

## 2. The change, and the check that it is the only change

**The change** (method note, section 2.2): on the seven tokens of the
named-other action turn, the acting channel — the input wire that tells the
model "this turn is yours" — is 0 instead of 1. The own-directed action turn,
every assignment turn and every token of every episode are as before. It is a
setting in `grammar.py`, `NAMED_OTHER_ACTING`, whose default of 1 reproduces
the old grammar; the driver sets it to 0.

    ../../../.venv/bin/python grammar.py --self-test --named-other-acting 0

MEASURED, `out-grammar-c/self-tests.txt`: all checks passed, including

- the four matched properties of proposal section 4.2 in the generated data of
  the new grammar, on 3,000 matched pairs: **(1)** four distinct candidate
  values per item in both conditions; **(2)** the distance from the source
  assignment to the action has the same distribution in both conditions,
  largest histogram difference 0.0098 over 6,000 episodes, mean distance 5.010
  own-directed against 4.928 named-other; **(3)** one supervised position of
  each kind, every scored position holding the mask word; **(4)** the same
  successor rule in both conditions;
- matched twins still token-for-token identical and still differing in the
  acting channel;
- the setting moves no token, and changes the acting channel on exactly the
  seven named-other action-turn positions (14,000 positions over 2,000
  episodes);
- the acting channel at the scored positions is 1 for own-directed and 0 for
  named-other.

The same self-test under the default setting also passes, so every earlier
record still reproduces from this code (same file). The arm and measure
self-tests pass unchanged (same file).

---

## 3. The pass line (ruling item 1; method note, section 5)

    ../../../.venv/bin/python grammar_attempt.py --stage train --arms F,T,C
    ../../../.venv/bin/python grammar_attempt.py --stage gate
    ../../../.venv/bin/python grammar_attempt.py --stage passline

MEASURED, `out-grammar-c/gate_base.json` and `passline.json`, on the same
3,000 held-out development episodes the repairs gate used:

| free arm | named-other, correct of 3,000 | clears 790? | own-directed |
|---|---|---|---|
| seed 0 | 774 (0.2580) | no | 0.5733 |
| seed 1 | 730 (0.2433) | no | 0.5553 |
| seed 2 | 759 (0.2530) | no | 0.5677 |
| **verdict** | **0 of 3 seeds** | **(a) not met** | **mean 0.5654 ≥ 0.5513: (b) met** |

**Not cleared**, because part (a) failed.

As a range and a direction, beside the free arm's earlier records on the old
grammar: named-other ran 0.24 to 0.26 here, against 0.24 to 0.27 on
2026-09-21 (`out/gate.json`) and 0.25 to 0.33 on 2026-09-25
(`out-repairs/gate_base.json` on PR 52). Both earlier runs cleared the bar on
one seed; this one on none. The change did not move the condition up.
MEASURED for the figures; the comparison is ARGUED, since these arms drift
between runs of one seed.

**What the free arm answers at the named-other turn**, pre-stated in the method
this time. MEASURED, `out-grammar-c/diagnose_named_other.json`:

| free arm, seed | the named agent's value (right) | its own value | another agent's value in the item | a value not in the item |
|---|---|---|---|---|
| 0 / 1 / 2, new grammar | 0.26 / 0.24 / 0.25 | 0.05 / 0.05 / 0.06 | 0.50 / 0.53 / 0.50 | 0.19 / 0.18 / 0.18 |
| 0 / 1 / 2, old grammar (PR 52, `out-repairs/diagnose_named_other.json`) | 0.33 / 0.26 / 0.25 | 0.06 / 0.07 / 0.05 | 0.39 / 0.48 / 0.51 | 0.22 / 0.18 / 0.19 |

The model still knows which item and still avoids its own value — and still
does not know whose value among the other three. ARGUED: taking away the
shared "this turn is yours" signal removed something the model was not using
at that turn; the step it is missing, binding a marker word to that agent's
assignment, is not supplied by it. This is the wager in the method note
(section 2.5), stated before the run.

---

## 4. Rehearsal items R-1 to R-6, re-read against the new grammar

Labels as pre-stated (method note, section 6): **HOLDS**, **NOW PASSES**,
**FAILS**, **UNCHANGED BY CONSTRUCTION**. "Before" is the latest committed
reading.

| item | before | on the new grammar | label |
|---|---|---|---|
| **R-1** grammar works, both conditions learnable | FAIL on the named-other half (2026-09-21 section 2a; PR 52 section 2) | The four matched properties hold (section 2). Arm T clears both conditions on 3 of 3 seeds; arm C clears own-directed 3 of 3 and named-other **1 of 3**; arm F own-directed 3 of 3 and named-other **0 of 3**. Lesion (acting channel removed): own-directed falls to 0.20 to 0.21 on arms C and F and to 0.25 to 0.27 on arm T. MEASURED, `out-grammar-c/gate_base.json` | **FAILS** — already failing, on the same half |
| **R-2** arm T's ownership answer transplantable on its own | pass, reading 0.0000 on every seed (PR 52, section 6.2) | Nominated on every seed (first layer, the action position, rank 8); reading **0.0000** on every seed, within 0.1 of zero. MEASURED, `out-grammar-c/nominate_base_F_T_C.json`, `measure_base_F_T_C.json` | **HOLDS** |
| **R-3** arm C's degree known by construction | pass, 0.99 to 1.00 (PR 52, section 6.2) | Whole-state transplant clears the floor on every seed; reading **0.99 to 1.00**, at or above 0.5 on every seed. No nomination used an all-positions site set, so the sensitivity row without them is the same site set and the same reading on every seed. MEASURED, same files | **HOLDS** |
| **R-4** all four outcomes reachable | pass (2026-09-21 section 2a) | Near zero: arm T, 0.0000. High: arm C, 0.99 to 1.00. No verdict: arm T at the first layer before the identity can be known, rank 2 — whole-state transplant 0.0000 on every seed, below the floor. Negative: on the unseen-vocabulary pool, arm T seed 0 at its own nomination reads **−0.1870** (whole-state 0.7588, ownership-only 0.8850); the widened search was not needed. MEASURED, `out-grammar-c/outcomes.json`, `measure_base_F_T_C.json` | **HOLDS** |
| **R-5** competing solvers | ownership-blind 0.22 to 0.24 on both conditions; name-only 0.238 own-directed, 1.000 named-other (PR 52 `out-repairs/gate_base.json`) | With the acting channel zeroed — which is how the blind solver trains and is scored — the blind solver's three training sets and the held-out set are **byte-identical** under the old and new grammars (210,000 and 21,000 acting positions differed before zeroing, seven per episode). The name-only solver, recomputed: 0.238 and 1.000. MEASURED, `out-grammar-c/invariance.json` | **UNCHANGED BY CONSTRUCTION** |
| **R-6** the arithmetic is finite | pass (2026-09-21 section 2a) | The measure module, the reading and the floor check use no attribute of the grammar module at all; the measure self-test passes. MEASURED, `out-grammar-c/invariance.json`, `self-tests.txt` | **UNCHANGED BY CONSTRUCTION** |

**Also reported, not items.** The separation between arms C and T clears the
page 1a bar of 0.5 on every seed (0.99 to 1.00; `out-grammar-c/summary_base.json`).
The free arm reads 1.00 on every seed (same file), but it fails the learn-both
gate, so under the ruled numbers it would not be read at all — as on PR 52.
Control 2 as the proposal words it gives no verdict on eight of nine
arm-and-seed pairs and a pass on arm C seed 1 (`measure_base_F_T_C.json`);
the 2026-09-25 ruling (item 5) already records it as not applicable on arm T.
Arm C seed 0's own-directed accuracy came out at 0.7993, well above its other
two seeds and every earlier arm C seed on the same held-out episodes (0.57 to
0.58, `out/gate.json` and PR 52's `out-repairs/gate_base.json`); it is reported as
observed, and nothing is read from one seed of a drifting arm.

---

## 5. The author's run of the known-failure list

This is the author running `docs/known-failure-modes.md` against the method
first, which the protocol allows. **It does not stand in for a reviewer's
pass**; under the pairing rule this work is owed a check by a session that did
not write it. The commands are in
`experiments/rehearsal-successor-measure/out-grammar-c/failure-mode-run.sh`
and their full output in `failure-mode-run.txt` beside it; the results are
summarised here.

**Failure 1, a denominator of zero or one that moves between arms.** The
reading's denominator is the whole-state transplant's room above the untouched
rate. From `out-grammar-c/measure_base_F_T_C.json`, every one of the nine
arm-and-seed pairs has room between 0.4438 and 1.0000, every one clears the
four-fifths floor, and the top of the scale — the reading when the
ownership-only transplant does nothing — is 1.0000 on every arm. The pass line
itself is a count against a fixed bar and divides by nothing. MEASURED.

**Failure 2, a target that cannot be recovered.** The named-other target is
carried by an input token: the method note, line 85, names the `<who>` word
three tokens before the scored position. The search printed that line. The
own-directed target reaches the state through the acting channel, and arm T's
ownership-only transplant recovering it fully (reading 0.0000) is the positive
control. MEASURED.

**Failure 3, a cell empty by construction.** Every gate cell has 3,000
episodes per condition per run (`gate_base.json`); control 6's same-value cell
has 81 trials and its different-value cell 719, on every arm and seed
(`measure_base_F_T_C.json`). No pre-stated cell is empty. MEASURED.

**Failure 4, a claim of measurement with no record.** Every number in this
file names the committed file it came from, except those quoted from PR 52's
branch, which are cited by branch and commit. The list's two sweeps, run on
this file, flag 55 lines by wording and 31 by number; the author read the
number lines against the output files and corrected two (a run time and a
range) before committing. ARGUED — this is the author's own reading, and a
checker should run both sweeps again.

**Failures 5 and 6, a command that creates something, and a remote step
tested only against stand-ins.** A search of `grammar_attempt.py`,
`repairs.py` and `grammar.py` for `ssh`, `runpod`, `vast`, `curl`,
`requests.`, `subprocess`, `launch` and `nohup` returned one line: the
grammar's own docstring saying it "launches nothing". No step here touches a
remote machine. MEASURED.

---

## 6. Where running it differed from planning it

- **Training was slower than one run alone.** Three runs side by side took
  2,236 to 2,640 seconds each (`out-grammar-c/train_*.json`), against 856
  seconds for one free-arm run alone on PR 52. Wall-clock only; the result is
  unaffected. MEASURED.
- **The pass-line verdict was computed twice**, the second time only to put its
  printed output into `out-grammar-c/run-log.txt`; it reads the gate file and
  gave the same answer both times. MEASURED, same file.
- **The virtual environment lives in the main checkout**, so every command ran
  with that interpreter by its full path; the commands above are written in
  the relative form the repository's other findings use.
- Nothing else departed from the method.

---

## 7. What this means, and what it does not

**The pass line was not cleared.** Under the 2026-09-25 ruling, item 1, that
means fallback (d) is what registers, and version 2 of the successor proposal
is not amended with this grammar change. This file makes no recommendation
beyond stating that.

What it does not show: it does not show that no grammar change could work,
only that this one, the smallest that removes the shared acting signal, did
not. And page 4's strongest argument against every toy redesign still stands —
the toy arms may be too small to learn a condition the registered size will
learn. ARGUED.
