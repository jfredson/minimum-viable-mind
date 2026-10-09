# Check of pull request 155: the test of a differently coded decoy (weakness W18)

*2026-10-08 (Pacific). Claude Code, as the checker, on branch `check-decoy-w18`,
cut from the main line at `362e2a2`. I wrote none of what I check: not the
method, the test code, the outputs or the findings of pull request 155 (branch
`decoy-test-w18`, head `2cac11c`). Laptop only, processor only, $0: nothing
rented, no paid service called. My scripts, logs and outputs are beside this
file, in `docs/reviews/2026-10-08-decoy-w18-check-scripts/`. I edited nothing on
the pull request's branch, nothing in version 5 of the registration text and
not the red-team ledger.*

*What is checked.* The ruled test of an unused, differently coded copy of "who
owns this" bolted onto the separable toy model (arm T): item 8 of John's
rulings of 2026-10-08 (`docs/rulings/2026-10-08-v5-open-items-rulings.md`),
which asks for a test of weakness W18 in version 5
(`docs/successor-experiment-proposal-2026-10-07-v5.md`, section 13). The
decoy is a "code": 20 extra numbers, one per marker word, added to the model's
running state and thrown away before the model uses the state. The test asks
whether the registered measurement can be pulled into that unused code and so
make a model that is separable by construction read as partly or fully
entangled.

*Where the code ran.* I checked the branch out at its tip into a scratch
folder (a detached git worktree outside this repository) and ran the committed
script there, so its outputs overwrote the committed ones and `git diff`
shows every change. Python 3.12.13, torch 2.12.1, scikit-learn 1.9.0, numpy
2.5.0, scipy 1.18.0, from the main checkout's `.venv`, as pinned. Two runs at
4 threads side by side, as the method allows.

## Verdict

**Pull request 155: ready to merge, after pull request 153 (the last batch
before the registration) merges, since this branch is built on it.** No
must-fix. The method came first and was not changed; the test goes through
the frozen measurement procedure, replacing only the model loader; the decoy
is built as stated and is truly unused (I tested this myself in two ways the
author did not); my re-run of all five variants on all three seeds reproduces
every committed output exactly; and the verdict, "inconclusive", follows the
method's rule as written. Three should-fix items, all about wording in the
findings and the pull request's description that goes a little past the data.
None of them changes the verdict.

## Must-fix

None.

## Should-fix

- **S1. "Nothing computed went above 0.41" and the pull request's "nothing
  computed came near 1" are true only of the readings at the site the
  procedure chose.** The procedure's own search on development pairs computes
  a reading for every site set and size, and on V1 the highest of those is
  0.997, 0.967 and 0.943 on the three seeds (`readings_computed_out.txt`).
  The findings' table also prints 0.93 to 0.98 at 1 direction. The claim
  that matters, that no reading at a site the registered rule would choose
  went above 0.41 (V3, sixteen times the block's size, withheld), holds. The
  wording should say "at the nominated site" (findings section 1, fifth
  bullet, and section 5, item 4; the pull request description, "What was
  tested", last bullet).
- **S2. The high readings at 1 and 2 directions are mostly not made by the
  decoy.** Findings section 3 says "the probe's pattern reproduces (high at
  few directions, low at 8)", and section 1 calls the readings at fewer
  directions "the much higher readings ... that the probe found". But the
  unaltered arm T model (the page 4 re-run's rows,
  `out-ruled-code-changes/passB-limit10000/`) already reads 0.85 to 0.86 at 1
  direction and 0.57 to 0.67 at 2, at state 0, the action position, on
  development pairs; the quarter-size decoy (V2) reads 0.82 to 0.84 at 1 on
  fresh pairs. A read squeezed into one or two directions cannot carry a
  24-number block whatever is bolted on. What the strong decoy adds is at 2
  and 4 directions (on fresh pairs, V1 reads 0.81 to 0.89 and 0.54 to 0.65
  there, against the unaltered model's 0.57 to 0.67 and 0.15 to 0.21 on
  development pairs) and at 8 (0.12 to 0.21 against 0). One sentence should
  say so, so the 0.52-to-0.98 range is not read as the decoy's size. (The
  same range sits in version 5's W18 text, "0.52 to 0.96 at fewer"; that
  text is not this branch's to change, but whoever rewrites W18 should know.)
- **S3. The arm F figure is carried over from arm T and should be labelled as
  argued, not measured.** Findings section 1 ("somewhere around 0.1 to 0.4")
  and section 5, item 3, and the note for John ("could lift a reading by
  roughly 0.1 to 0.4 and nothing would flag it. It could not make a model
  read near 1"), give a size for the free model. Nothing was run on arm F;
  the figure is arm T's withheld arithmetic transferred to a different model,
  whose nominated site and size could differ. Section 5 item 3 does say "on
  these figures", but the note for John drops the hedge, and "could not make
  a model read near 1" is a statement about this one family of decoy on this
  toy, as section 5 item 5 says. The corpus rule is to mark such carry-overs
  ARGUED; doing so in those three places is enough.

A note, not an item: the caller's summary of this result gave the withheld
readings as 0.15 to 0.21. The committed figures (which I reproduced) are
0.1488, 0.2137 and 0.1162, so 0.12 to 0.21, as the findings say.

## 1. Order

    $ git log --format='%h %ad %s' --date=iso origin/main..origin/decoy-test-w18
    2cac11c 2026-10-08 20:33:32 -0700 Findings of the test of a differently coded decoy (weakness W18): inconclusive; ...
    a517316 2026-10-08 19:31:33 -0700 Test code for the differently coded decoy (weakness W18), committed before any of its outputs exist
    ddef906 2026-10-08 19:26:39 -0700 Method for the test of a differently coded decoy (weakness W18), committed before any test code
    6c47c56 2026-10-08 19:21:13 -0700 Last batch before the registration: ... (pull request 153's commit)

    $ git show --stat --format='%h' ddef906 a517316
    ddef906  docs/2026-10-08-decoy-w18-method.md | 341 +++  (1 file)
    a517316  experiments/08-successor-degree/out-decoy-w18/decoy_w18.py | 505 +++  (1 file)

The method commit holds only the method; the code commit holds only the
script; every output and the findings are in the third commit, an hour later.

    $ git diff --stat ddef906 origin/decoy-test-w18 -- docs/2026-10-08-decoy-w18-method.md
    (nothing; exit 0)
    $ git diff --stat a517316 origin/decoy-test-w18 -- experiments/08-successor-degree/out-decoy-w18/decoy_w18.py
    (nothing; exit 0)

So the bands (method section 7: "not fooled" at 0.20 or less on every seed
that reads, with at least two reading; "fooled" at 0.50 or more on two seeds
with the chosen piece more than half in the code; "inconclusive" otherwise)
are the ones committed before any code, and the script was not changed after
its commit. The script's constants (`NEAR_ZERO = 0.20`, `FOOLED_AT = 0.50`,
`MOSTLY_IN_CODE = 0.50`) and its `classify` function encode those bands as
written.

The code commit's message records one tiny pipeline test before the commit
(5 per cent of every set, one seed, into a scratch folder) that found a
misplaced bracket in check (c). That is a pre-commit debugging run of the
code, not a look at any figure at registered counts; I see no problem with it.

The frozen files and the texts the branch says it does not touch:

    $ git diff --stat 6c47c56 origin/decoy-test-w18 -- experiments/08-successor-degree/src \
        docs/successor-experiment-proposal-2026-10-07-v5.md \
        experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md
    (nothing; exit 0)

The diff against main does show `procedure.py` and version 5 changing, but
that is pull request 153's commit `6c47c56` underneath; its only change to
`procedure.py` is the reporting table's cell count (12 to 11), which prints
and computes nothing. Pull request 153 is still open:

    $ git merge-base --is-ancestor 6c47c56 origin/main; echo $?
    1
    $ git merge-tree --write-tree origin/main origin/decoy-test-w18 >/dev/null; echo $?
    0
    $ git merge-tree --write-tree origin/final-batch-before-registration origin/decoy-test-w18 >/dev/null; echo $?
    0

It merges cleanly either way, but it should go in after pull request 153, as
its description says.

## 2. The registered procedure, and the decoy

**Only the model loader is replaced.** `decoy_w18.run` sets
`procedure.load_model` to a function returning the widened model, calls the
frozen `procedure.run_model` unchanged, and restores the original in a
`finally`. `load_model` is called only once in the frozen code, at the top of
`run_model` (`grep -n load_model src/*.py`: line 766, its definition, and line
796, its one call), and `run_model` looks it up by module name, so the swap
takes effect and nothing else is bypassed. Everything after it is the frozen
code: the gate and in-use check, the one fit of the reads (written and
reloaded), the full search, the pick rule with its floor, the fresh-pair
reading, controls 1, 3, 4, 6 and 7, the stricter and sensitivity rows, the
null, and `summarise`, whose `measure.withhold` decides "no verdict". The
script's own additions (`beside`) run after the row is written and only add a
`decoy_w18` section to it; `summarise` is then called on the folder. I
checked that the added section enters no verdict: `withhold` reads only
`gate`, `nomination_status`, `described_only`, `reading`, `dev_floor_clears`
and `controls`.

**The widened model is the committed model.** I read
`CodeDecoyArmT.forward` against arm T's `Arm.forward` in the frozen
`models.py`. The two are line for line the same except that the state is
`[content | code | block]` instead of `[content | block]`, and `_split` drops
the 20 code numbers before every block and before the head. The code is
recomputed from the input at each state, never carried from the patched
state, so a transplant into the code at one state cannot reach the next. The
widened `cfg.d_model` is 180, so the frozen procedure's `d_content` is 156
and its "true-slot reference" (`eye[:, d_content:]`) is the 24-number block
alone, as the findings say.

**The code is built as the method states.** Soft code: the model's own
ownership weights (`_own_vec`'s `p_own`) times a one-hot of each agent's
marker word, times `k`. Hard code: `k` on the agent with the largest
acting-channel tally so far, 0 before the first own turn. `k` is the scale
times the block's root-mean-square size at the own-directed action on the
600 development recipients. For V1 it is 20.5738, 22.2008 and 21.0531 on the
three seeds; the earlier check's probe (`out-decoy-check/p3.json`) has
20.5738 and 22.2008 for seeds 0 and 1, the same.

**My own tests that the code is unused** (`unused_probe.py`, output in
`unused_probe_out.txt`), on seed 0, V1 and V5, on the 800 fresh recipients:

    V1 seed 0 k=20.5738: largest |gradient| of outputs wrt code at any state = 0.0;
       code shuffled across episodes bit-identical = True;
       code slice equals built code at all 5 states = True;
       content+block slices equal committed model's states = True
    V5 seed 0 k=20.5738: (the same four results)

The gradient of every output with respect to the code numbers at all five
states is exactly zero, and shuffling the code between episodes at every
state changes no output bit. This adds to the author's checks (a), (b) and
(b'), which I also reproduced (section 3).

## 3. The re-run

Commands (from `experiments/08-successor-degree/out-decoy-w18/` in the
scratch checkout; wrapped by `runA.sh`):

    python decoy_w18.py --variant V1    # then V3, then V5
    python decoy_w18.py --variant V2    # then V4, then --checks-only (side by side)
    python decoy_w18.py --report

All six exited 0 (`times.txt`: 1,127, 1,377, 1,071, 1,277, 1,190 and 564
seconds). No stop fired, and no fit stopped at the iteration limit of 10,000
in any run (every "stopped at the iteration limit" line in the logs reads 0).

Then I compared every value in every committed output file with the re-run's
(`compare.py`, output `compare_out.txt`): 55 files, every JSON file equal
value for value apart from the run time and the checkpoint's folder path,
every saved read (`.npz`) bit-identical, every table identical text.

    $ git status --short .     # in the scratch checkout, after the re-run
     M V1/row_T_seed0.json ... (the 15 row files only)
    $ git diff -U0 . | grep '^[+-] ' | sed -E 's/: .*//' | sort | uniq -c
      15 + "checkpoint"
      15 + "seconds"
      15 - "checkpoint"
      15 - "seconds"

`checks_only.json`, the five `summary.json` and `table.md` files, the checks
files, the top-level `table.md` and `verdicts.json` came out byte-identical.
So every registered figure, every withheld reading, every control 1 figure
and every piece-share figure in the findings is reproduced exactly. In
particular, V1: no verdict on all three seeds, withheld readings 0.1488,
0.2137 and 0.1162, control 1 at 0.1313, 0.1638 and 0.1038 against an
allowance of 0.018, the chosen piece 0.935, 0.939 and 0.935 in the code; V2:
0.0000 on all three seeds; V3: withheld 0.3500, 0.2788 and 0.4100; V4:
0.0000; V5: withheld 0.1488, 0.2125 and 0.1162.

## 4. The verdict and its reading

**The rule.** V1 has no seed with a reading, so it is "inconclusive" (fewer
than two seeds with a reading). V2 has three seeds at 0.0000, so "not
fooled". Overall: neither is fooled and they are not both "not fooled", so
"inconclusive". The script's `classify` and the overall rule in `report`
match the method's section 7, and the findings report the result as the
method said in advance they would ("inconclusive is not a pass").

**Not stronger than the data, in the direction of the measure.** The
findings do not dress the "no verdict" up as a pass: they say the read was
partly fooled under the refusal (the piece about 94 per cent in the code,
about a fifth of the block's change left unmoved), and they flag that seed 1's
withheld 0.2137 is above 0.20 with the piece mostly in the code, one of the
things the method listed in advance as counting against the measure.

**Not stronger than the data, against the measure.** The claim that control 1
catches V1 on arm T holds: control 1 is the check that transplants everything
except the chosen piece, and it moved 10 to 16 per cent of actions against an
allowance of 1.8 per cent, on every seed of V1, V3 and V5, and was the only
reason any seed was withheld. It is not a near thing.

**Control 1's role on each arm, against version 5, section 7.3.** Section 7.3
says control 1 "on arm T ... holds" and "on arms C, M and F it is reported and
cannot veto", and the frozen code agrees
(`holds=(c1 <= u + MS.CONTROL1_ROOM) if arm == "T" else None`, and
`measure.withhold` adds the control 1 check only `if arm == "T"`). Section
7.3 also gives the reason the findings repeat: on an entangled model the
complement is expected to move the action about as much as the whole state
(arm C 0.53 to 0.56, arm F 0.48 to 0.56 on the toy), so a large control 1
figure there could not tell a decoy from real entanglement. So "nothing
catches it on arms C, M and F" is right, with S3's caveat that the size given
for arm F is carried over, not measured.

**"Nothing computed went above 0.41"** holds at the nominated, stricter and
sensitivity sites on every seed of every variant (`readings_computed_out.txt`);
it does not hold for the whole search (S1).

## 5. The claim that V5 is not a separate test

`v5_probe.py` (output `v5_probe_out.txt`), all three seeds:

    seed 0, own-directed action: soft code's owner-word weight mean 0.9987, min 0.9987;
            largest |soft - hard| / k = 0.0013
    seed 0, named-other action: (the same)
    seed 0: largest |soft - hard| / k at any position = 0.2500;
            soft code from block by one straight-line map, largest residual / k = 1.07e-07
    (seeds 1 and 2 the same to the printed places; residuals 1.12e-07 and 1.11e-07)

At both action positions the soft code puts 0.9987 of its weight on the
owner's word in every episode (the minimum equals the mean), so the hard code
differs from it there by at most 0.13 per cent of `k`. They differ by a
quarter of `k` only before the model's first own turn, where the soft code is
spread evenly and the hard code is zero; the reads are fitted at the action
positions. The readings agree: V5 matches V1 to four places on seeds 0 and 2
and differs by 0.0012 on seed 1 (0.2125 against 0.2137), where the chosen
site includes the step before the action. So the findings are right that V5
does not test a code that is genuinely not a straight-line function of the
block, and right to say that form is still untested. I also confirmed the
method's statement that the soft code is an exact straight-line function of
the block (one fixed map, residual about one ten-millionth of `k`).

## Files

`docs/reviews/2026-10-08-decoy-w18-check-scripts/`:

- `runA.sh`, the wrapper that ran the variants; `times.txt`, exit codes and
  seconds;
- `rerun_V1.log` to `rerun_V5.log` and `rerun_checks_only.log`, the re-run
  logs;
- `compare.py` and `compare_out.txt`, the file-by-file comparison;
- `unused_probe.py` and `unused_probe_out.txt`, my test that the code is
  unused;
- `v5_probe.py` and `v5_probe_out.txt`, my test of the V5 claim;
- `readings_computed.py` and `readings_computed_out.txt`, every reading the
  rows computed, and the unaltered model's search at state 0 for comparison.

`compare.py`, `unused_probe.py` and `v5_probe.py` expect the scratch layout I
used: a `rerun/` checkout of the branch tip and a `committed/` copy of its
`out-decoy-w18/` folder (`git archive`) beside them. `readings_computed.py`
runs from the root of a checkout of the branch.
