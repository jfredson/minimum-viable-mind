# Gate A failure-mode pass on version 5 of the successor experiment's registration text, by the tier 1 reviewer — RT-275 to RT-282

*Filed 2026-10-08 (late night, Pacific) by a Claude Code session acting as
the Gate A tier 1 reviewer, on branch `gate-a-fmp-v5`, cut from the main line
at `93f4e90` (the merge of pull request 156, the check of the decoy test).
The text under review is version 5 as it stands on branch
`registration-ready-2026-10-08` (pull request 158, the change that makes the
text ready for the registration commit) at its head commit `d674807` (the
commit that applies the check of that change), file
`docs/successor-experiment-proposal-2026-10-07-v5.md`, 5,904 lines, SHA-256
`23ff1403…fcce56`. Filed under this experiment's reviews directory because
the successor experiment has no reviews directory of its own, the fallback
every earlier pass on this text used (`docs/outside-review-protocol.md`, "The
pairing rule").*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (a command was run, and the command and its output are below or
in the scripts folder beside this file) or **ARGUED** (reasoning a reader can
dispute), and carries a severity: **fatal**, **serious** or **worth-noting**.
Findings continue the red-team ledger's numbering. The ledger
(`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`) ends at
RT-274 (the loss conditions that cannot lose) on the main line and on every
open branch; `git grep` for RT-275 to RT-299 finds the numbers only as the
ends of searched ranges and in one sentence saying the next number "would now
start at RT-275". No ledger row is written here: rows are written when John
rules.*

**What this is.** The outside-review protocol requires, at every Gate A, a
failure-mode pass owned and filed by the tier 1 reviewer: every entry of
`docs/known-failure-modes.md` (the list of what has gone wrong in this
programme before) is run against the design, with the command and its output
on the record, and "an author's run never stands in for the reviewer's"
(`docs/outside-review-protocol.md`, "The failure-mode pass: the known failures
are run against the design, not cited"). Version 5's section 17 is the
author's run and says the reviewer's is still owed. This is the reviewer's.
It also re-checks the commit `d674807` against the check of pull request 158
(`docs/reviews/2026-10-08-registration-ready-check-claude-code.md`, on branch
`check-registration-ready`, pull request 159), as asked.

**Nothing was rented, created or spent: $0.** Laptop only, on its processor.
No model was loaded except inside the registered code's own self-tests; no
model was trained. Version 5, the ledger, the known-failure list, the
protocol and the frozen code were not edited. The launcher checks ran with a
stand-in vendor tool first on the search path, which recorded no call.

**How isolated this session was.** A fresh session in its own git worktree,
with no chat history of any session that wrote version 5, its checks or the
work it cites. It wrote none of them.

---

## Verdicts

**1. May the text reach its registration commit, as far as the failure-mode
pass is concerned? Yes, once one serious finding is closed or carried by
name.** No entry of the list fires fatally on version 5. Every entry was run;
the ones that fire on this design (failure 2 on the freely trained model,
failure 3's threshold test on the in-use check's second part) are caught by a
registered rule or stated as a named weakness, as the text says. **One serious
finding: RT-276** (the nine hand-set toy models behind section 5.6's and
rehearsal item R-15's figures are not in the repository, which is the form of
the uncommitted-record finding RT-145 and contradicts section 10's own
sentence that every toy result rests on thirty committed models). Under the
protocol's closure rule it is closed by committing the nine files (they exist,
hash-checked, in the sharpness branch's worktree on this laptop) or carried in
the registered text by name with John's ruling and reason. Seven worth-noting
findings (RT-275 and RT-277 to RT-282) are listed below; none blocks the
commit.

**2. Is pull request 158 ready to merge? Yes, after pull requests 157 and 159
merge, in that order.** Every must-fix and should-fix item of the check is
applied; weakness W18 (the differently coded decoy) now says control 1 failed;
no place in version 5, `STATUS.md` or `data/project.toml` claims that nothing
waits on any session; `python3 scripts/export_site.py --check` passes. Two
leftovers, neither a merge blocker: section 7.4 and the source table still
describe the end-to-end re-run (pull request 157) as if on the main line and
as meeting ruling 3, whose check is still running; and the text now also cites
the check of pull request 158 itself (pull request 159's file), so that file
must reach the main line too. The findings of this pass are for the next edit
before the registration commit, not for pull request 158.

---

## What this session opened, and what it did not

**Opened and read.** `~/Code/CLAUDE.md` and the repository's `CLAUDE.md` (as
loaded into this session); `docs/outside-review-protocol.md` (the gates, the
failure-mode pass, the tiers); the measurement rehearsal record
`docs/2026-09-21-successor-measure-rehearsal.md` (its summary and section
list, read first after the protocol, as the protocol asks of a tier 1
reviewer); `docs/known-failure-modes.md` in full; version 5 at `d674807`:
the header and source table, sections 0 to 8.2, 9, 10, 11, 17, 18, 21 and the
dated change notes in full, and sections 12, 13 and 15 by search; the
earlier failure-mode passes in this folder (the author's run on version 2,
`2026-09-26-successor-v2-failure-mode-pass-claude-worktree.md`, and the pass
inside the Gate A review of version 4,
`2026-10-04-successor-v4-gate-a-claude-code.md`) for their conventions; the
check of pull request 158 and the diff of `d674807`; the frozen code's
`measure.py` (the reading, the floor, the withholding, the in-use judge, the
separation), `procedure.py` (the in-use writer, the docstring), `models.py`
(the built answer), `grammar.py` (the generator), `launch_successor.sh` (its
guard and dry-run path, read before anything ran it), the two launcher checks
and test T7; the committed outputs the scripts below name; the decision-case
definitions (`tests/a2_cases.py`, the in-use cases); the ruling on the
decision procedure (`docs/rulings/2026-10-06-successor-v4-gate-a-rulings.md`,
item 6) and the outside dispositions' A2 section it adopts; the A2 method and
findings; the check of the four development runs (its section 7); the check
of the sharpness branch (its section on the nine retrained models).

**Not opened.** Any chat or transcript; TimeAssembler; any uncommitted file of
another checkout (the nine retrained model files of RT-276 were not opened or
hashed by this session; what is said of them is from the committed hash list,
the `.gitignore` rule and the sharpness check's record); the outside reviews'
texts; the end-to-end re-run's branch (pull request 157), beyond confirming
its two files are not on the main line.

---

## Findings at a glance

| Number | Severity | Label | Failure entry | Version 5 lines | The finding in one line |
|---|---|---|---|---|---|
| RT-275 | worth-noting | MEASURED (arithmetic on the rule); ARGUED (how likely) | 1 | 1715 to 1722; R-6 at 3276 | The floor keeps the reading's denominator above zero but not away from it: a seed that passes every registered rule can read on as few as about 11 of 800 matched pairs, a 95 per cent band of about ±0.29 on a middling reading. "On an arm that has learned the task that requirement is large" is argued, not guaranteed by the gate. No model on record comes near (smallest 0.4263) |
| RT-276 | **serious** | MEASURED | 4 | 1143, 1466 to 1471, 1529 to 1567, 3175, 3391 to 3398, 4242 | The nine retrained hand-set toy models (sharpness fixed at 4.0) behind section 5.6's and R-15's figures are not in the repository (the `*.pt` ignore rule; only their hash list and training records are committed). Section 10 says every toy result rests on thirty committed models and that an uncommitted model is the form of RT-145. The eleven re-reads the text says are owed need these files |
| RT-277 | worth-noting | MEASURED | 4 | 1833 to 1839 (section 6.4, item 5) | "The figure the arithmetic would have given appears nowhere in the output" is true of the summary file and the table, not of the per-seed row files the registered code writes: every withheld toy seed's row carries `primary.reading.degree` with status "valid" (arm C 1.0026, 1.0, 1.0; arm M 0.5252, 0.4793, 0.5208; arm F 1.0). Section 3 of the same text quotes those figures from the rows |
| RT-278 | worth-noting | MEASURED | 3 | 1492 to 1500 (part B) | The in-use check's judge (`measure.route_check`) judges whichever routes a record lists; a record missing arm M's stirred-in route, or arm C's, passes, where the text says a missing field counts against. The registered writer always writes the right routes, so no registered run is affected; but the made-up decision cases 27 and 28 give arms T and M a route they do not have |
| RT-279 | worth-noting | MEASURED | 4 | section 17: 4904, 5032 to 5038, 5101 to 5129, 5276 to 5284, 5288 | Section 17, the author's pass and part of the registered text, prints records that no longer hold: ledger rows "0 of 10" twice (now 20 of 20); "fifty" files at no main-line commit (now nine, for the reasons below); "the ownership-free line has no field in the toy's committed rows" (the registered code's toy rows carry it); a "leaves open" list of items now done; and its blocks were printed by two scripts that exist at no commit |
| RT-280 | worth-noting | MEASURED | 4 | 1443, 5005 | "Best pieces 41 and 45 of 180" for arms C and M at 10 million parameters are the best whole reads; the best pieces are 45 and 43. The conclusion does not move |
| RT-281 | worth-noting | MEASURED | 5 | (registered code, not the text) | The docstrings of the registered `measure.py` (lines 12 to 17) and `procedure.py` (lines 27 to 31) say a no-transplant rate outside its allowance withholds a reading, and `procedure.py` says seeds count "by two of three"; the code does neither (its own self-test asserts the rate withholds nothing), as version 5 rules. Documentation saying the registered code does what it does not |
| RT-282 | worth-noting | ARGUED (from the code); MEASURED (the digest passes on the laptop) | 6 | 2846 to 2853 (section 7.4) | The evaluation sets' pinned digest was re-pinned on 2026-10-08 and has passed only on the laptop; the rented machine's pre-flight compares its own build against it for the first time at step 4b. The text does not say this stand-in. A mismatch deletes the machine before training, so the cost is cents, not data |

---

## The failure-mode pass, entry by entry

The scripts are in `2026-10-08-successor-v5-gate-a-failure-mode-pass-scripts/`
beside this file; every block below is pasted from their output files there.
`.venv/bin/python` is the project's Python (torch 2.12.1, scikit-learn 1.9.0,
numpy 2.5.0), run by its full path. Version 5 and the ledger as on pull
request 158 were extracted with `git show
origin/registration-ready-2026-10-08:<path>` into the session's scratch
folder and passed to the scripts by path. The registered code is
`experiments/08-successor-degree/src/` as at `6c47c56` (the last-batch commit,
merged by pull request 153); on the main line at `93f4e90` that folder is
identical to it (`git diff --stat 6c47c56 HEAD -- experiments/08-successor-degree/src`
prints nothing). The toy record used throughout is the one that code wrote:
`experiments/08-successor-degree/out-ruled-code-changes/passB-limit10000/`
(the page 4 toy pass under the ruled code, pull request 151, checked in pull
request 152). Section 17 was read after these were run; nothing below is
copied from it.

### 1. A comparison whose denominator was zero — **does not fire on any model on record; the rule's margin above zero is unbounded below (RT-275)**

*How tested.* Part one of the list's test (every ceiling traceable to a
committed measurement) and part two (the denominator and the top of the
scale per condition), on the registered code's own toy rows, the four
10-million development rows and the competing solver's development grids;
then the smallest denominator the registered rules admit, by arithmetic.

*Command:* `.venv/bin/python -I failure_mode_pass_v5.py --v5 v5.md --ledger ledger.md --part 1`
(output in `failure_mode_pass_v5.out.txt`).

```
arm/seed  untouched  whole   own-acc | denom   needs   need>0 | top | dev denom  dev needs | recomputed reading = stored? | status
T/0       0.0000    1.0000  1.0000 | 1.0000  0.8000  True   | 1   | (dev acc 1.0000, untouched 0.0000, needs 0.8000) | True  (0.0000) | reads
C/0       0.0512    0.5400  0.5487 | 0.4888  0.3980  True   | 1   | (dev acc 0.5667, untouched 0.0517, needs 0.4120) | True  (1.0026) | reads
C/1       0.0488    0.5575  0.5813 | 0.5088  0.4260  True   | 1   | (dev acc 0.5683, untouched 0.0517, needs 0.4133) | True  (1.0000) | reads
C/2       0.0600    0.5463  0.5525 | 0.4863  0.3940  True   | 1   | (dev acc 0.5767, untouched 0.0517, needs 0.4200) | True  (1.0000) | reads
F/0       0.0587    0.4850  0.5587 | 0.4263  0.4000  True   | 1   | (dev acc 0.5950, untouched 0.0600, needs 0.4280) | True  (1.0000) | described only
F/1       0.0563    0.5713  0.5663 | 0.5150  0.4080  True   | 1   | ...                                               | True  (1.0000) | described only
F/2       0.0688    0.5138  0.5563 | 0.4450  0.3900  True   | 1   | ...                                               | True  (1.0000) | described only
M/0       0.0125    0.8050  0.8712 | 0.7925  0.6870  True   | 1   | (dev acc 0.8583, untouched 0.0150, needs 0.6747) | True  (0.5252) | reads
M/1       0.0175    0.7738  0.8800 | 0.7563  0.6900  True   | 1   | ...                                               | True  (0.4793) | reads
M/2       0.0138    0.7937  0.8712 | 0.7800  0.6860  True   | 1   | ...                                               | True  (0.5208) | reads
(T/1 and T/2 as T/0)
smallest fresh denominator among the rows that read: 0.4863 (C/2)

  T/0 10M: whole 0.8325, untouched 0.0225, own-acc 0.9012 -> denominator 0.8100, needs 0.7030
  C/0 10M: whole 0.5288, untouched 0.0500, own-acc 0.5875 -> denominator 0.4788, needs 0.4300
  F/0 10M: whole 0.5212, untouched 0.0612, own-acc 0.5663 -> denominator 0.4600, needs 0.4040
  M/0 10M: whole 0.7950, untouched 0.0100, own-acc 0.8875 -> denominator 0.7850, needs 0.7020

  seed 0 channel_left_on: own-directed 0.2383, untouched 0.2417, floor needs -0.0027 -> requirement above zero: False; site sets clearing: 0
  seed 1 channel_left_on: own-directed 0.2100, untouched 0.2300, floor needs -0.0160 -> requirement above zero: False; site sets clearing: 0
  seed 2 channel_left_on: own-directed 0.2367, untouched 0.2300, floor needs +0.0053 -> requirement above zero: True; site sets clearing: 0
  (the three channel-removed runs the same way: -0.0053, -0.0160, +0.0027)

  own-directed p | untouched even  min denom  pairs  band  | untouched owner-confusing  min denom  pairs  band
  0.2633         | 0.1052  0.1264  101.2  0.097   | 0.2456  0.0142   11.3  0.291
  0.2800         | 0.1029  0.1417  113.4  0.092   | 0.2400  0.0320   25.6  0.194
  0.3000         | 0.1000  0.1600  128.0  0.087   | 0.2333  0.0533   42.7  0.150
  0.3500         | 0.0929  0.2057  164.6  0.076   | 0.2167  0.1067   85.3  0.106
  0.5500         | 0.0643  0.3886  310.9  0.056   | 0.1500  0.3200  256.0  0.061
```

Every no-transplant rate above is a named field of a committed row, so part
one's failure criterion (a ceiling not traceable to a record) does not fire.
The reading recomputed from the four fields equals the stored one on all
twelve toy rows. The top of the scale is 1 on every arm, so the per-arm-ceiling
repair (RT-172, the finding that version 1's reading had a different top for
every arm) holds. The requirement-above-zero clause (the repair of RT-238, the
zero-divisor finding) is in the registered code (`measure.floor_check`, line
115: `whole - untouched >= need and need > 0`) and refuses the four solver
runs whose requirement is at or below zero.

**RT-275 (worth-noting; MEASURED arithmetic, ARGUED likelihood).** The last
block is the case the list's criterion names, "small enough that ordinary
noise ... moves the reading a lot". The gate on learning asks only 790 of
3,000 own-directed (0.2633); since 2026-10-06 the no-transplant rate is
reported and withholds nothing (section 6.4, item 3, which itself gives the
owner-confusing pattern, `(1 − p) / 3`); so a seed at the gate bar whose
errors fall on the other agents' values passes every registered rule with a
denominator as small as 0.0142, about 11 of the 800 fresh pairs, and a
middling reading on that many pairs carries a 95 per cent band of about
±0.29. Section 6.4, item 1's "on an arm that has learned the task that
requirement is large" and rehearsal item R-6's "kept off zero by the
whole-state floor together with the gate" are therefore argued, not
guaranteed. Nothing on record comes near: the smallest denominator on any
model that read is 0.4863 and on any 10-million model 0.4600, and the
reporting table prints the three accuracies the denominator is made of
(column 5), so a reader can see it. Suggested: one sentence in section 6.4,
item 1 saying the gate does not bound the denominator from below, and the
denominator printed in pairs beside the reading. No ruled number needs to
move.

### 2. A probe target that cannot be recovered in principle — **fires on the free model and is caught by the fit floor; at 10 million parameters the positive control clears, so the null on arms C and M is readable**

*How tested.* Part one: the route sentence, by a search with this design's
words. Part two: the two runs the list asks for, on the same instrument with
the same bar, from the registered code's own records: the target (the
ownership read at the action position) against quantities the input
guarantees (the whole state at the first token of the model's first own turn,
which is the model's own marker word, and the named agent's read of control
2, whose label is an input token of the named-other action turn).

*Command:* `failure_mode_pass_v5.py --part 2`.

```
  1916: own**. *The route by which that quantity reaches the model's states, in one
  1917: sentence:* the marker word is the input token at every turn the model's own
  1918: assignments are spoken on, so it is carried by the token into the running
  1922: claim, that which marker word is the model's own is forced by the loss at

  (whole read | best piece, per running state 0 to 4)
  T/0: 180|180 180|180 180|180 180|180 180|180  -> nominated            (T/1, T/2 the same)
  C/2:  17| 17 180|180 180|180 180|180 180|179  -> nominated; marker token itself, whole 180
  F/0:  17| 17  34| 30  30| 30  36| 40  34| 33  -> read failed its floor: no size's piece reaches four fifths; marker token itself, whole 180; named agent's best piece 171
  F/1:  17| 17  15| 18  17| 17  20| 19  14| 19  -> read failed its floor
  F/2:  17| 17  25| 24  39| 36  30| 27  27| 28  -> read failed its floor
  M/1: 180|180 180|180 180|180 180|180 180|180  -> nominated; marker token itself, whole 180

  The same at 10 million parameters (states 0 to 8):
  T/0: 180|180 164|178 162|167 150|161 137|153 117| 98 101| 95  98| 82  95| 74 -> nominated
  C/0:  13| 14  34| 34  36| 37  40| 41  41| 45  40| 36  35| 34  24| 25  29| 24 -> read failed its floor; marker token itself, whole 143 at state [1]; named agent's best piece 180
  F/0:  14| 14  22| 22  14| 14  12| 18  10| 15  10| 21  13| 20  16| 17  13| 16 -> read failed its floor; marker token itself, whole 171 at state [1]
  M/0:  26| 26  42| 43  33| 30  40| 40  33| 30  37| 30  36| 29  38| 32  45| 37 -> read failed its floor; marker token itself, whole 48 at state [5]
```

A route sentence exists and names the token (section 7.2, item 1); the fourth
match is the sentence striking version 2's loss claim, not a route. On the
toy, arm F is the list's middle limb exactly: on the same model, fitter and
split, the marker word where it is the input token reads 180 of 180 and the
named agent's read reaches 171, while the ownership read at the action never
passes 40. That is the fatal finding of the review of version 2 (RT-212, the
empty read on the free arm), still present, and caught as the text says: the
fit floor on the piece turns it into a registered "no verdict, read failed its
floor" on every seed, and the first full-size free run's stop (S4a) turns the
same thing at registered size into a stop before the second release.

At 10 million parameters, the positive control the list asks for clears on the
same width and fit count: arm T reads 180 at state 0, and arm C's named agent
read reaches 180. So the null on arms C and M there (whole reads at most 41
and 45) is a measurement that the label is not at the action position, which
agrees with the in-use check's independent figures (weights 0.218 and 0.247,
route use 0.018 and 0.000, below). The marker-token figures at 10 million are
mixed (143 at state 1 on arm C, one below the floor; 48 at state 5 on arm M,
where a deep state need not keep its input token), so they are not used as the
control. **Guarded**, with the target-at-registered-size question left to
step 5a, as registered. The one number the text gets wrong here is RT-280.

### 3. A cell that is empty by construction — **no pre-stated cell is empty; the in-use check's second part fires on the working end of the toy, as weakness W17 states; the judge can miss an absent route (RT-278)**

*How tested.* Part one: every pre-stated cell counted by generating the
registered sets from the frozen `grammar.py` itself (no record read), and
compared with the registered code's own rows. Part two: the generator read
for the properties that empty a cell. Part three: every threshold at both
ends of its range, from the exact binomial tail, the built answer's formula in
`models.py`, the registered code's toy rows, the in-use cases and the decoy
test. Then the in-use judge probed directly, and the decision-procedure cases
re-run.

*Commands:* `failure_mode_pass_v5.py --part 3`; `route_check_cells.py`;
`.venv/bin/python -I experiments/08-successor-degree/tests/a2_run_cases.py <scratch>`
(output `decision_cases.out.txt`).

```
  control 6, relaxed set (800 pairs, seed 778): same-value 81, different-value 719
  the same split on the fresh set (distinct values): same-value 0 of 800 (empty by construction, which is why control 6 runs on the relaxed set)
  control 4, positions before both twins' first own turns, fresh set: min 1, mean 5.2125, max 21; pairs with none: 0
  twins token-for-token identical on the fresh set: 800 of 800
  in-use check on arm M, gate episodes (3000): own-directed actions on the separable items (it0, it4) 1190, on the stirred-in items (it1 to it3) 1810
    the registered code's own row (M/0) counts: separable 1190, stirred-in 1810

  grammar.py:161:         values[:, j] = rng.choice(N_SLOTS, size=N_AGENTS, replace=False)
  grammar.py:167:         a, b = rng.choice(N_AGENTS, size=2, replace=False)
  grammar.py:169 (by reading):  values[b, j] = values[a, j]      # the relaxed set's one shared value
  (full list of 50 matches in failure_mode_pass_v5.out.txt)

  learning gate: smallest k with P(X >= k | 3,000, 1/4) <= 0.05: 790 (tail 0.0485); a fully collapsed arm read as not collapsed, per seed: 0.0485
  ownership-free line: smallest k with P(X >= k | 3,000, 1/2) <= 0.05: 1546 (tail 0.0483)
    arm T: [3000, 3000, 3000]  arm C: [2236, 2160, 2132]  arm F: [2100, 2238, 2324]  arm M: [2770, 2686, 2660]  -> all pass 1,546
  in-use check, part A: weight = e^(2s) / (e^(2s) + 3)
    sharpness  4.000: weight 0.9990 -> passes      sharpness 0.700: 0.5748 -> fails
    sharpness  1.650: weight 0.9004 -> passes      sharpness 0.000: 0.2500 -> fails
    the bar is crossed at sharpness ln(27)/2 = 1.6479
  in-use check, part B, registered code's toy rows:
    arm T: slot 1.000 on every seed (passed)
    arm C: 0.269, 0.233, 0.221 (failed)
    arm M: stirred-in 0.071, 0.090, 0.109; separable 1.000 (failed)
      case 10, real 10-million arm C: weight 0.218, route use 0.018 -> failed (expected failed)
      case 11, real 10-million arm M: weight 0.247, route use 0.0 and 0.0 -> failed (expected failed)
      case 12, real 10-million arm T: weight 0.942, route use 0.924 -> passed (expected passed)
  piece floor (144 of 180): best piece anywhere, arm F [40, 19, 36]; arms T, C, M 180 on every seed
  control 1 on arm T: working end 0.0000 on every seed (holds); broken end, the decoy of W18 at four times: no verdict, control 1 failed, on all three seeds

  decision cases: 31 cases; 0 differ from expectation or leak: []
```

*Part one.* Every pre-stated cell has trials: control 6's two cells (81 and
719, the repair of RT-173, the empty-cell finding, holds on the registered
generator, not only in the old toy records); control 4 transplants at one
position or more in every fresh pair; both of arm M's in-use routes have
actions (1,190 and 1,810), matching the registered code's own count; the
two conditions have one action each per gate episode. The twins are
token-for-token identical on all 800 fresh pairs, which is what control 4
and the pairing rest on. The decision procedure, re-run here from the
committed code on its 31 made-up and toy cases, lands every one on the term
written for it before it ran, with no withheld figure in its outputs, and
reaches all eight registered terms (R1, R2, R3, the fifth to eighth) and the
two "not decidable" states.

*Part two.* The only draws without replacement that matter are line 161 (four
distinct values per item, which empties control 6's first cell on every set
but the relaxed one) and line 167 with 169 (the relaxed set's one shared
value, which fills it). Both are named in section 4.2.

*Part three.* The learning bar and the ownership-free line reproduce from the
exact tail. The ownership-free line now has a field in the registered code's
toy rows and every trained toy model passes it (arm F at 2,100, 2,238 and
2,324, the figures section 8.2 quotes from a separate measurement); the text's
statement that no committed row carries it is stale (RT-279). Part A of the
in-use check cannot fail on a model whose sharpness is the fixed buffer of
4.0, and does fail on every flat or learned-low sharpness, which is what it is
for. **Part B fails on the toy's trained arms C and M, the end it should pass
if they are references, and on the 10-million flat arms, the end it should
fail; so on the toy it does not yet separate the two ends.** That is the
list's part three firing, and the text states it as weakness W17 and as the
record's own prediction that stop S4b will most likely fire; John ruled the
bar at 0.5 knowing it (`docs/rulings/2026-10-08-verification-bar-ruling.md`).
Stated, so **guarded**, not a new finding. The piece floor, control 1's room
and the gate each pass the working end and refuse the broken end.

**RT-278 (worth-noting, MEASURED).** `route_check_cells.py` hands the
registered judge `measure.route_check` five made-up in-use records:

```
  arm M, both routes present and in use: code returns 'passed'
  arm M, stirred-in route present and flat: code returns 'failed'
  arm M, stirred-in route MISSING from the record, separable in use: code returns 'passed'; the text's rule gives not run (a missing field counts against)
  arm C, its stirred-in route missing, an unrelated 'slot' route in use: code returns 'passed'
  arm T, recorded under the wrong name ('entangled', as a2_cases.route_flat builds it), flat: code returns 'failed'
Does route_check compare the recorded route names with the arm's built routes? no: it judges whichever routes the record lists
```

The registered writer, `procedure.route_in_use` (lines 349 to 361), always
writes arm T's slot, arm C's stirred-in route and both of arm M's, and a route
with no actions or no right answers comes out "could not be evaluated", which
counts against; so no registered run can hit this. But "a missing field is
'not run'" (section 5.6, part B) holds for the record, not for each route, and
two of the decision cases that exercise the in-use check (case 27, arm T flat,
and case 28, arm M flat; `tests/a2_cases.py`, `route_flat`) give the arm a
single route named "entangled", which arm T and arm M do not have, so those
two cases test the judge and not the record shape the registered code writes
(the 14 in-use cases on real models do use the real shapes). Fix, if wanted:
say in section 5.6 that the writer guarantees the route set, or have the judge
check it, which would be a change to registered code.

### 4. A claim of measurement with no record, or a record that does not reproduce — **fires: one serious (RT-276), three worth-noting (RT-277, RT-279, RT-280)**

*How tested.* Part one: the list's two sweeps on sections 0 to 16. Part two:
(a) figures new in version 5 regenerated from the files their sentences
name; (b) the ledger rows the text describes; (c) every full path the text
names, against the main line; (d) the withheld-figure claim against the
registered code's outputs; and the repository's two checkers, run on version
5 as on pull request 158 (placed temporarily at its path in this worktree and
restored afterwards).

*Commands:* `failure_mode_pass_v5.py --part 4`;
`.venv/bin/python scripts/check_citations.py --only docs/successor-experiment-proposal-2026-10-07-v5.md`
and `check_single_source.py` the same way (outputs
`check_citations_v5.out.txt`, `check_single_source_v5.out.txt`).

```
Part one, the two sweeps on sections 0 to 16 (4879 lines):
  lines matching the word list: 1212
  lines matching the number sweep: 425
  MEASURED labels: 107; ARGUED labels: 16

  '1,810 of 3,000' (section 5.3): the registered code's M/0 row counts 1810
  route use before the fix, 'arm C 0.269, 0.233, 0.221; arm M 0.071, 0.090, 0.109': rows give C [0.269, 0.233, 0.221], M [0.071, 0.09, 0.109]
  toy readings at 1,800, 'T 0.0000; C 1.0026, 1.0000, 1.0000; M 0.5252, 0.4793, 0.5208': rows give the same
  separation 'lowest C minus highest T = 1.0000': 1.0000
  arm F's best piece '40, 19 and 36 of 180': rows give [40, 19, 36]
  arm M within its true-slot reading '0.0252, 0.0033, 0.0288': 0.0252, 0.0033, 0.0288
  arm F ownership-free count '2,100, 2,238 and 2,324': the registered code's rows give [2100, 2238, 2324]
  10-million 'best pieces 41 and 45 of 180' for arms C and M: rows give best piece C 45, M 43; best whole read C 41, M 45
  W18 withheld readings '0.1488, 0.2137 and 0.1162': table gives 0.1488, 0.2137, 0.1162
  (and, run separately: arm C at the 420 fit, 1.0051, 0.9926, 0.9974 in out-controls-rerun/measure_C_seed*.json)

  ledger rows present for RT-237 to RT-256: 20 of 20
  section 17's printed block for the same rows says:
     ledger rows for RT-237 to RT-246: 0 of 10 (rows are owed: the 2026-10-06 ruling)
     ledger rows for RT-247 to RT-256: 0 of 10 (rows are owed: the 2026-10-06 ruling)

  full paths named: 131; not on the main line: 4
  docs/2026-10-08-end-to-end-final-code-findings.md                       (pull request 157)
  docs/reviews/2026-10-08-registration-ready-check-claude-code.md         (pull request 159)
  docs/rulings/2026-10-08-decoy-w18-ruling.md                             (pull request 158 itself)
  experiments/08-successor-degree/out-e2e-final-code/code-identity.txt    (pull request 157)

  C/0: withheld in summary.json (the built ownership route has gone flat ...); row file primary.reading.degree = 1.0025575447570334, status 'valid'; in summary.json: False; in table.md: False
  (likewise C/1 1.0, C/2 1.0, M/0 0.5252, M/1 0.4793, M/2 0.5208, F/0, F/1, F/2 1.0)

check_citations.py: [CONFIDENT] 9 reference(s) name a file that is not in the repository
  (the four above, cited nine times, plus the author's scratch scripts failure_pass_v5.py and scan_ids.py)
check_single_source.py: [CONFIDENT] 2 + 2 found, the same four section 17 explains ($221.85 and $7.39 as arithmetic; $44 and $131 cited to the ruling that set them)
```

Of nine regenerated figures new in version 5, eight match their files to the
digit; the ninth is RT-280. Section 5.3's "1,810 of 3,000", which both
checkers have flagged since version 3 as absent from the file cited, is now in
the registered code's own row. The two checkers' other confident items are
the ones section 17 explains.

**RT-276 (serious, MEASURED).** `git ls-files
experiments/08-successor-degree/out-sharpness-fix` lists the nine training
records and `models/SHA256SUMS`, which names nine files
`ckpt_{T,C,M}_fixed_seed{0,1,2}.pt`; none of the nine is in the repository,
because `.gitignore` line 32 ignores `*.pt`. The check of the sharpness branch
(`docs/reviews/2026-10-08-sharpness-fix-check-claude-code.md`, its item 2)
found them in that branch's own worktree on this laptop, hash-checked nine of
nine, and asked only the findings to say so. Version 5 quotes measured
figures that rest on those nine models: that the fix "costs nothing to the
toy's learning" (no seed lost more than 36 of 3,000) and arm C's weight rising
to 0.999 (lines 1466 to 1471); part B's route use after the fix, 0.285, 0.273,
0.244 and 0.090, 0.106, 0.100 (lines 1529 to 1537); arm T seed 0's re-read at
0.0000 (lines 1558 to 1567); rehearsal item R-15 (lines 3391 to 3398); and
weakness W17. Its own section 10 (line 3175) says "The models every toy result
rests on: thirty, all committed", and that they were committed "because they
cannot be rebuilt from code and seed ... and an uncommitted record the reader
cannot open is the form of ledger item RT-145" (the finding that a
registration commit rested on an uncommitted file). The toy retrain ran on the
laptop's graphics chip, which the check notes is not bit-reproducible, and the
eleven re-reads the text says are owed can be made only from these files. So
the registration would rest, for its stated expectation of stop S4b and for
its picture of the hand-set anchors, on files its reader cannot open. No
registered rule or outcome depends on them, which is why this is serious and
not fatal. **Close by** force-adding the nine files from the sharpness
worktree (`git add -f`, checked against the committed `SHA256SUMS`), as
decision 22 did for the thirty, before the registration commit; or carry it in
section 5.6 by name, saying where the files are and that they are not
committed, with John's ruling and reason.

**RT-277 (worth-noting, MEASURED).** Section 6.4, item 5 (lines 1833 to 1839)
says that in the registered code a withheld seed's "figure the arithmetic
would have given appears nowhere in the output". The ruling it rests on (the
2026-10-06 rulings, follow-up item 6, adopting the outside dispositions' A2
item 7) removed the field `arithmetic_withheld` from `summary.json`, and the
A2 method scoped its check to `summary.json` and `table.md`; on those two the
claim holds, as part (d) shows. The per-seed row files that
`procedure.py model` writes, which every check of this text has read and
which section 17's own blocks quote, carry the arithmetic under
`primary.reading.degree` with `status: "valid"` for every seed the summary
withholds. Section 3 of version 5 quotes exactly those figures ("each toy
row's own arithmetic") for arms C and M, which the current decision code
withholds by the in-use check. The ruling's own reason, "a figure in the
output file is one a later session will quote", is what happened. Fix: say
"nowhere in the summary file or the table; the per-seed row files keep the
arithmetic as a record of the computation and are never the reported figure".

**RT-279 (worth-noting, MEASURED).** Section 17 is part of the registered text
and will be frozen with it. Against the record at this commit:

- its block "ledger rows for RT-237 to RT-246: 0 of 10" and "RT-247 to
  RT-256: 0 of 10" (line 5116 and the next), and its sentence "the ledger
  carries no row for any finding from RT-237 on": the ledger has all twenty
  (pull requests 141 and 145);
- its "fifty of the records this version cites exist at no main-line commit"
  and the checker block "[CONFIDENT] 50 reference(s)" (lines 5101 to 5127): the
  checker now finds nine, which are the decoy ruling arriving with pull
  request 158, two files of pull request 157, one of pull request 159, and two
  scripts of the author's;
- "The ownership-free line ... has no field in the toy's committed rows ...
  the first registered rows to carry the field are the reruns of step 4b"
  (lines 5032 to 5038): the registered code's toy rows carry it (part three of
  failure 3);
- "What this pass leaves open, in one place" (lines 5276 to 5284) still lists
  the check of this version, the closure check of RT-237, the merges of
  section 16 and the ledger's rows, all done;
- its blocks were printed by `failure_pass_v5.py`, "kept in its scratch
  folder" (line 4904), and its identifier scan by `scan_ids.py` (line 5288),
  neither at any commit.

Fix: a dated line at the head of section 17 saying it is the author's run of
2026-10-07, not re-run since, and that this file is the reviewer's pass, with
the five places above marked superseded; or bring them current.

**RT-280 (worth-noting, MEASURED).** Lines 1443 and 5005 give arms C and M at
10 million parameters "best pieces 41 and 45 of 180". In the rows
(`out-dev-10m-check/row_{C,M}_seed0.json`, `fits`) 41 and 45 are the best
whole reads; the best pieces are 45 and 43. The check of the development runs
labels them correctly ("Ownership read, best layer"). Nothing turns on it.

### 5. A command that creates something while documented as creating nothing — **does not fire on any launcher; the registered code's docstrings misdescribe its withholding (RT-281)**

*How tested.* The list's own test; test T7 on the successor launcher, which
the list's script does not cover; and the successor launcher's guard read by
hand before anything ran it (the guard is lines 85 to 91, an explicit `exit
2` before any other work; the first vendor command that executes is the pod
creation at line 381; the `runpodctl` at line 115 is inside a function
definition). All three ran with a stand-in `runpodctl` first on the search
path that records any call and exits 99.

*Command:* `run_launcher_checks.sh` (outputs `failure5_launcher_guard.out.txt`,
`t7_check_launcher.out.txt`, `run_launcher_checks.out.txt`).

```
failure 5, check_launcher_argument_guard.sh: exit 0
test T7 on launch_successor.sh: exit 0
the stand-in vendor tool was never called

(the list's test: 21 lines [ ok ], the standing prohibition on launch_a3.sh printed as expected, and)
negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

(T7:)
  [ ok ] an argument is refused (exit 2)
  [ ok ] it says why
  [ ok ] it names DRYRUN=1
  [ ok ] the guard (line 17) precedes any vendor command (line 115)
  [ ok ] dry run exits 0 / says nothing was created / the vendor tool was never called
  [ ok ] refuses without ARM, SIZE, WAVE, ESTIMATE_HOURS, HARD_CAP_USD; refuses the toy size
  [ ok ] the dry run says a real launch would be refused (halt file)
all checks pass. nothing was created and nothing was spent.
```

Guarded: the launcher the registered runs use refuses an argument with exit
status 2 and the reason, before any vendor command, and its dry run creates
nothing. One weakness of the check itself, noted and not numbered: T7's
ordering line finds the first mention of the old argument finding RT-198,
which in this launcher is a header comment (line 17), and the first
`runpodctl` text, which is in a function body (line 115); the property holds
(85 before 381) by reading, but that line would pass if the guard moved. T7's
"it says why" line would still catch a guard moved below the settings checks.

**RT-281 (worth-noting, MEASURED).** The registered `measure.py`'s docstring
(lines 12 to 17) says "a no-transplant rate outside its 0.018 allowance ...
replaces the reading with 'no verdict'", and `procedure.py`'s (lines 27 to
31) says "a reading is withheld ... when ... the no-transplant rate is outside
its allowance" and that seeds become a reading "by two of three". The code
does neither: `no_transplant_rule` returns `vetoes=False`, `withhold` never
reads it, and the self-test "withhold: the no-transplant rate withholds
nothing (page 8)" passes (`self_tests_6c47c56.out.txt`); seeds count under the
page 7 rule. It is the opposite direction from the failure this entry is
about (the documentation promises a refusal the code does not make, where the
code is right and the text it serves says so), but once the folder is
registered any edit to it is a change to registered code, so it is cheaper to
note now. Fix with the next change to that folder, or carry.

### 6. A remote step tested only against stand-ins — **the registered launcher's background starts pass against a real local shell; every stand-in is stated except one (RT-282)**

*How tested.* The list's test on the parent launcher, as the author ran it,
and on `launch_successor.sh`, which is the launcher the registered runs use;
then each remote step of the design listed with what stood in for the far end.

*Command:* `run_launcher_checks.sh` (outputs
`failure6_remote_forms_parent.out.txt`, `failure6_remote_forms_successor.out.txt`).

```
launch_successor.sh
  [ ok ] launch_successor.sh line 643: returned after 0.0s -- returns at once
  [ ok ] launch_successor.sh line 724: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 729)

negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.0s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang

all checks pass. Nothing was rented and nothing was spent.
(the parent launcher, launch_a3_fetch_first.sh: lines 616 and 697, the same two verdicts, exit 0)
```

**What stood in for the far end, step by step.** The shutdown handshake's
machine half: never exercised, because the laptop deletes the machine first
(weakness W9; stated). The spending alarm's four fixes: a stand-in vendor on
made-up waves, three checks, never the vendor (section 12.5, stated). The
in-use check on a repaired checkpoint: not yet (stated; step 4b is the
first). The registered procedure on a trained 30-million model: never; on
untrained ones in test T6 (stated). The read's 1,800 fitting episodes at the
registered width: a stand-in of noise-padded toy states (weakness W15,
stated). The registered code's self-tests on this laptop: run here, 265 of
265 pass, including the two pinned digests (`self_tests_6c47c56.out.txt`).

**RT-282 (worth-noting; MEASURED that the digest passes on the laptop, ARGUED
from the code for the rest).** The evaluation sets' pinned digest
(`grammar.py`, `EVAL_SETS_DIGEST`) was re-pinned on 2026-10-08 when the 1,980
development episodes became an evaluation set (section 7.4, lines 2846 to
2853, "a session's call"). The rented machine's pre-flight runs `grammar.py
--self-test` against that digest with its own numpy before any training step
(`launch_successor.sh`, line 516, and its dry-run listing at line 346), and the laptop is the only place
the new digest has been built; the four development runs passed the old one.
So the first far-end test of the new digest is step 4b. A mismatch fails the
pre-flight and the launcher deletes the machine, so the cost is cents and no
data is spoiled, but by the list's own discipline ("say what stood in for the
far end") the sentence in section 7.4 should say the new digest has met only
the laptop.

### The drafted seventh entry (not on the list; run because the author ran it)

The candidate ("an outcome line a plan states in advance that the design
cannot produce on the path it expects", drafted in
`docs/2026-09-25-rented-slice-attempt-2-findings.md`, section 9, item 2, not
ruled onto the list) fires where the author said and nowhere else this pass
found: the verification of step 4b at route use 0.5 is a line no built model
of the entangled kind has produced, before or after the fix (failure 3, part
three). Every registered term is produced by the decision cases above. Not a
new finding.

### Whether anything here is a new species for the list

No. Nothing fatal was found, and the protocol adds to the list only a fatal
finding of a new kind. RT-276 is an instance of failure 4 (the RT-145 form),
RT-282 of failure 6.

---

## Part 2: the re-check of commit `d674807` against the check of pull request 158

*Commands:* `git show --stat d674807`; `git show d674807 --
docs/successor-experiment-proposal-2026-10-07-v5.md STATUS.md
data/project.toml`; the check read in full with `git show
origin/check-registration-ready:docs/reviews/2026-10-08-registration-ready-check-claude-code.md`;
`gh pr view 158` and `gh pr view 157`; the grep and the site check below, on
the branch at `d674807`.

| Item of the check | Applied? | Where, and what is left |
|---|---|---|
| M1, W18 said control 1 "held" | **Yes** | "because control 1 failed and withheld the reading" |
| M2, "nothing waits on any session", four places | **Yes** in all four | STATUS heading now "nearly ready ... two checks remain" and its last paragraph names both; `data/project.toml`'s `where_we_are`, next step N41 and the timeline row now name both; version 5's header (line 35) and closing note name both. **Left:** M2 also said section 7.4 cites the end-to-end run as if ruling 3 were met and the source table calls its file "main line"; both still stand (lines 102 and 2771 to 2781). The check's own fix makes this conditional ("once it exists"), so it waits on pull request 157's check |
| S1, W18's overtaken sentences | **Yes, in the lighter form the check offered** | "Nothing in the design excluded it when this was written; the ruled test below shows what does and does not" |
| S2, the reason for John's decoy ruling | **Yes** | W18 now gives it |
| S3, six stale "owed" or "remain" phrases | **Yes**, all six | lines 6, 3352, 3437, 3490 and 3493, 4710, 5279 |
| S4, next step N26 | **Yes** | folded into N41, status "in-progress" |
| S5, merge order | **Yes**, in the pull request's description ("Merge after pull request 157") | **New since:** the closing note now cites pull request 159's file, so pull request 159 must also reach the main line |
| S6, two accuracy points in W18 | **Yes**, both | quarter size as the second ruled variant; "on development pairs, at sites and sizes it did not choose"; 0.85 to 0.86 |

**W18 says control 1 failed.** Confirmed (line 4276 of version 5 on the
branch), and the sentence's figures match `out-decoy-w18/table.md` (part (a)
of failure 4 above).

**No place claims nothing waits on any session.**

```
$ grep -n -i -E "nothing waits|nothing (else )?remains|nothing is left|one thing left|only thing left|what remains is john|remains is john|only john's|all that remains|nothing else (waits|is owed)|no session" <each file on the branch>
version 5:          5886: ## Ready for the registration commit (2026-10-08, night)      (a change-note heading; its text names the two owed checks)
STATUS.md:          17: ... nearly ready for John's commit: two checks remain
                    111: Nothing waits on John until the commit itself. Owed, each by a session ...   (an older entry, about John, which names owed work)
data/project.toml:  20: ... What remains is a check of the end-to-end re-run and the reviewer's own failure-mode pass on the text, then John's registration commit ...
                    1075: title = "The registration text is ready for John's commit"   (its summary names both owed items)
                    1082: ... Nothing is left for him to decide before the registration commit; what stands before it is checked work ...   (an older row, about John)
```

None says nothing waits on any session. Two headings still say "ready" while
their text says what is owed (version 5's last change note; the timeline row's
title); worth a word at the next edit, not an item.

**The site check passes.**

```
$ python3 scripts/export_site.py --check        # at d674807
export_site: data/project.toml is valid (8 stages, 9 questions, 13 ideas, 25 findings, 43 next steps, 49 timeline rows)
export_site: data/roadmap.toml is valid (13 weekends, 45 goals, 4 milestones, 5 extensions)
exit 0
```

**After this pass is filed**, version 5's header (line 35), section 10's
"What happens next" (line 3437), the closing change note, `STATUS.md` and
`data/project.toml` will say the reviewer's pass is owed when it is not; they
should cite this file, and section 17 should point at it (RT-279).

---

## The decisive measured checks

The protocol asks every Gate A for at least one decisive measured check on
the text being registered. Three were run on the registered code itself:

1. **The registered code's self-tests**, `run_self_tests.sh` at the main line
   (identical to `6c47c56`): 265 checks, 0 failures, "ALL SELF-TESTS PASS",
   including "matched pairs are token-for-token identical", "no name badge"
   and the two pinned digests (`self_tests_6c47c56.out.txt`).
2. **The decision procedure re-run from the committed code** on its 31 cases:
   every case on the term written before it ran, no withheld figure in its
   summary or table, every registered term reached
   (`decision_cases.out.txt`). This is the same suite pull request 157
   reports; it was re-run here independently of that branch.
3. **The registered generator's cells, generated afresh** rather than read
   from records (failure 3, part one), agreeing with the registered code's
   own counts where both exist (1,190 and 1,810).

---

## Scripts and outputs beside this file

In `2026-10-08-successor-v5-gate-a-failure-mode-pass-scripts/`:

| File | What it is |
|---|---|
| `failure_mode_pass_v5.py` | failures 1 to 4: reads committed records and the frozen generator; `--v5` and `--ledger` take the two files as on pull request 158 |
| `failure_mode_pass_v5.out.txt` | its full output |
| `route_check_cells.py`, `.out.txt` | RT-278: the registered in-use judge on five made-up records |
| `run_launcher_checks.sh`, `.out.txt` | failures 5 and 6: the list's two tests and test T7, behind a stand-in vendor tool |
| `failure5_launcher_guard.out.txt`, `t7_check_launcher.out.txt` | their outputs |
| `failure6_remote_forms_parent.out.txt`, `failure6_remote_forms_successor.out.txt` | the remote-start check on both launchers |
| `self_tests_6c47c56.out.txt` | the registered code's self-tests |
| `decision_cases.out.txt` | the decision procedure's 31 cases, re-run |
| `check_citations_v5.out.txt`, `check_single_source_v5.out.txt` | the repository's two checkers on version 5 as on pull request 158 |

To reproduce: from the repository root, extract version 5 and the ledger with
`git show origin/registration-ready-2026-10-08:<path> > <file>`, then run
`.venv/bin/python -I <scripts>/failure_mode_pass_v5.py --v5 <file> --ledger <file>`,
`<scripts>/route_check_cells.py`, `<scripts>/run_launcher_checks.sh`,
`experiments/08-successor-degree/src/run_self_tests.sh` and
`experiments/08-successor-degree/tests/a2_run_cases.py <a new scratch folder>`.
The timings in the remote-start outputs are wall clock and move by a tenth of
a second between runs.

## What this does not do

It edits neither version 5, the ledger, the known-failure list, the protocol,
the frozen code, `STATUS.md` nor the site data, and merges nothing. It writes
no ledger row and rules on nothing; the dispositions of RT-275 to RT-282 are
John's.
