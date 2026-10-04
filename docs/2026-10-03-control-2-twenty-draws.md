# The other-agent control compared with twenty random pieces: findings of the code test

*Written 2026-10-03 (Pacific) by the Claude Code session that wrote and ran
it, on branch `w2b-job2-control-2-twenty-draws`, cut from the main line at
`41b0bd3`. The method, `docs/2026-10-03-control-2-twenty-draws-method.md`,
and the code,
`experiments/rehearsal-successor-measure/src/control2_twenty_draws.py`, were
committed and pushed with no output at `174081e`, before the run. **The code
was not changed after that commit; it ran as committed, first time.** Laptop,
processor only. Nothing rented, nothing trained, nothing spent: $0.*

*Written under the workspace plain-language rule.*

**THIS IS A TEST THAT THE CODE RUNS END TO END. IT IS NOT A RESULT.** The
piece's accuracy floor was switched off for the one call, so the piece
transplanted here is not known to carry the named agent at all. No figure
below is a pass or a fail of anything, and nothing is concluded from them
about any model.

**What this session opened and what it did not.** The same as the method's
list: committed files only, at `41b0bd3`. It did not open the other record of
the seven-question ruling, any ruling packet, or any chat or transcript of
another session. **This code test was written and run by one session and is
owed a check by a session that did not write it.**

## 1. The short version

- **The changed code ran end to end** on the free model's seed 0 and returned
  the site set, the real figure, twenty random-piece figures and their
  summary. That is what the test was for.
- **Everything the change was not meant to touch came back identical to the
  earlier code test** (`docs/2026-10-03-short-prestated-run.md`, section 5):
  the same site set, and the same three figures to four places. So the new
  function is the old one with the one change ruled (stop D3 did not fire).
- **No stop fired.**

## 2. The run

```
$ cd experiments/rehearsal-successor-measure/src
$ /Users/john/Code/minimum-viable-mind/.venv/bin/python control2_twenty_draws.py > ../out-control-2-twenty-draws/stdout.txt 2>&1
exit 0
```

torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, on the processor; 50 seconds.
The model file matched `SHA256SUMS` before it was loaded. (The method gives
the project's Python by a relative path; this session ran from its own
worktree, where it is reached by its full path. Same program.)

What it printed (also `out-control-2-twenty-draws/table.md`; every figure is
in `code_test_NOT_A_RESULT.json`):

```
NOT A RESULT: the other-agent control compared with twenty random pieces, free model seed 0, floor switched off

ran end to end: True
site set: layer 1, the action position and the three before it, 8 directions
          (piece right on 92 of 180, whole read on 95; the floor would have asked for 144)
own-directed action moved under the named agent's piece: 0.0012 of 800 trials
under twenty random pieces: middle value 0.0037, 95th percentile 0.0052;
                            0 below, 1 equal to and 19 above the real figure
the twenty: 0.0025, 0.0037, 0.0012, 0.0050, 0.0037, 0.0050, 0.0050, 0.0088, 0.0050, 0.0037,
            0.0037, 0.0037, 0.0037, 0.0050, 0.0025, 0.0037, 0.0050, 0.0037, 0.0050, 0.0050
the single random piece as the earlier code drew it: 0.0063
named-other action moved: 0.0962
These figures are not a pass or a fail of anything.
```

## 3. Against what was expected (the method, section 5)

| Expected | Came back |
|---|---|
| Runs end to end and returns the site set, the real figure, twenty shares and their summary | **Yes** |
| Same site set as the earlier code test: layer 1, the action position and the three before it, 8 directions | **Yes** |
| Own-directed action moved: 0.0012 | **0.0012** |
| The one random piece as the earlier code drew it: 0.0063 | **0.0063** |
| Named-other action moved: 0.0962 | **0.0962** |
| A guess, for the record only: the twenty between 0.000 and about 0.02, more above the real figure than below | Between 0.0012 and 0.0088; 19 above, 1 equal, 0 below |

The three unchanged figures were seen before the run, so matching them is a
check that the path is the same, not a prediction.

**One thing about the code, not about the model (ARGUED).** The single random
piece the earlier code drew (0.0063) is higher than nineteen of the twenty
drawn now and above their 95th percentile (0.0052). A single draw can land in
the tail of what random pieces do. That is the reason version 4 gave when it
suggested the change (section 19, item 5: "a single draw is a weak thing to
print beside a figure"), and the code now prints the spread instead. It says nothing about the free model.

## 4. Against the method's stops

| Stop | Fired? |
|---|---|
| D1, the model file does not match its fingerprint | No |
| D2, the call returns no verdict or raises an error | No |
| D3, an unchanged figure differs from the earlier code test's | No |

## 5. What this settles and what it leaves

**Settled, subject to a check by another session:** the control's code as
ruled on 2026-10-03 (twenty random pieces drawn as control 3 draws them;
their middle value, 95th percentile and the counts below, equal and above; no
pass line) exists as a committed file and has run end to end once, on the
processor, at $0. Ruling 5 asked for that before the registration review.

**Still true, and unchanged by this:** the control has never been exercised
on a model whose read of the named agent clears its floor. No toy model has
one.

## 6. Which sentences of version 4 this bears on

Version 4 is `docs/successor-experiment-proposal-2026-10-03-v4.md`. This file
does not edit it; another session is working on it.

- **Section 7.3, item 2**, the sentence "What is reported: how often the
  own-directed action moves under the named agent's piece, beside how often
  it moves under twenty random pieces of the same size at the same sites,
  reported as control 3 reports its twenty (median, 95th percentile, and the
  counts below, equal and above)". The code now does this:
  `control2_twenty_draws.control2`.
- **The same item's bullet "The part of its code after the floor has run
  once, and that run is NOT A RESULT"**, which describes the run of the
  single-draw code. The code that would be registered has now also run once,
  NOT A RESULT, and the text should name this run and this file rather than
  only the earlier one. Version 4's own section 19, item 5 foresaw this ("the
  code path that ran once on 2026-10-03 is not quite the one registered").

## 7. Questions for John, each with a suggestion

Not asked in chat; for the session that routes rulings.

1. **Which file is the registered control 2.** The ruled change lives in a
   new file, because the brief said not to edit the committed scripts;
   `rerun_controls.control2` still has the one random piece and the pass
   line. *Suggestion:* the registration names
   `control2_twenty_draws.control2` as control 2's code and says that
   `rerun_controls.control2` is the earlier version, kept as the record of
   what the re-run did.
2. **Whether the 95th percentile of twenty is the right summary.** With
   twenty draws it is an interpolation between the two largest. That is the
   same as control 3 does, which is what was ruled. *Suggestion:* leave it as
   ruled and print the twenty as well, as this code does, so a reader sees
   the spread.

## 8. Files

`experiments/rehearsal-successor-measure/out-control-2-twenty-draws/`:
`code_test_NOT_A_RESULT.json`, `table.md`, `stdout.txt`. Code:
`src/control2_twenty_draws.py`, unchanged since `174081e`.
