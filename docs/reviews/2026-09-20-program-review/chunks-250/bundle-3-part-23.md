merged PR 4. Read in this order.

Method files (each committed before its run):
- `denoised-direction-method.md`
- `position-sweep-method.md`
- `powered-target-test-method.md`
- `powered-position-sweep-method.md`

Findings files:
- `denoised-direction-findings.md`
- `position-sweep-findings.md` (the sweep found invalid on all three
  checkpoints; the reason was the target)
- `powered-target-test-findings.md` (the anchor result, NOT CARRIED)
- `powered-position-sweep-findings.md` (CARRIED NOWHERE, the result under
  review)

Code the findings were produced by:
- `src/denoised_direction_a3.py`, `src/position_sweep_a3.py`,
  `src/powered_target_test_a3.py`, `src/powered_position_sweep_a3.py`,
  `src/probe_target_diagnostic_a3.py`, `src/marker_legibility_a3.py`

Records: the JSON outputs under `a3-gates/` named `powered_*`,
`probe_target_diagnostic_*` and `denoised_direction_*`.

Registered text the interpretation is read against: `amendment-a3.md` and
`pre-registration.md`.

Do not open: STATUS.md, the compute ledger, any chat transcript, any
uncommitted file, or `docs/`. Say at the top of the findings file what was
opened.

## The brief (fixed text from the protocol)

Four parts, in this order, a table first in each, severity marked fatal,
serious, or worth-noting, and a one-paragraph kill case at the end whether
or not you think the interpretation should stand.

1. **Feasibility.** For every quantity the method files pre-state or
   threshold (the family bar, the 1,000-draw null, the positive and negative
   controls, the anchor reproduction): can it be measured at all with the
   stated instrument, and can the control condition actually reach the
   stated threshold? Cite the committed record that shows so, or say that
   none exists. A "verified" or "measured" claim with no record behind it
   is a fatal finding on its own.
2. **Satisfied by the wrong thing.** Every way "carried nowhere" could be
   returned by a model that does carry own-agent identity linearly at these
   positions (a probe that cannot see it, a target still ill-posed, a null
   that is too wide, an exclusion of positions that removed the ones that
   matter).
3. **No verdict.** Every way the sweep could have failed to return a verdict
   and been read as one anyway.
4. **Over-reading.** What "the linear-read line is closed" will be read as
   claiming in STATUS.md, in the paper, and in public, beyond what was
   measured. Say whether the session's narrower statement above is the
   right wording for STATUS.md, and if not, write the sentence that is.

Label every finding MEASURED (you ran a check and report its output) or
ARGUED (reasoning a reader can dispute). Continue the ledger numbering from
RT-32. Plain language throughout. Lookup allowed and flagged. Do not soften
findings to be polite.

## Filing

Findings to `reviews/2026-09-19-linear-read-closure-claude-worktree.md`,
verbatim, never edited after filing. Rulings go in `red_team_ledger.md`.
Nothing from this review enters STATUS.md until John rules on it.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-19-linear-read-closure-claude-worktree.md =====

# Outside review — the linear-read closure (Gate B, tier 1)

*Filed 2026-09-19 under the outside-review protocol, against the review
packet `2026-09-19-linear-read-closure-packet.md`. Verbatim on filing and
not edited afterwards. Nothing here is a ruling; rulings are John's and go
in the red-team ledger (`red_team_ledger.md`).*

## What was opened

Read at the commit that merged pull request 4 (`eaff1d5`), in a fresh
worktree checked out at that commit. Exactly the packet's list and nothing
else:

- The four method files: the denoised-direction method
  (`denoised-direction-method.md`), the position-sweep method
  (`position-sweep-method.md`), the powered-target-test method
  (`powered-target-test-method.md`), the powered-position-sweep method
  (`powered-position-sweep-method.md`).
- The four findings files with the matching names ending
  `-findings.md`.
- The six code files named in the packet, under `src/`:
  `denoised_direction_a3.py`, `position_sweep_a3.py`,
  `powered_target_test_a3.py`, `powered_position_sweep_a3.py`,
  `probe_target_diagnostic_a3.py`, `marker_legibility_a3.py`.
- The fifteen records under `a3-gates/` whose names begin `powered_`,
  `probe_target_diagnostic_` or `denoised_direction_`.
- Git metadata only — commit dates, messages and the list of files each
  commit touched — used to check the "committed before the run" claim.

**Not opened**, as instructed: the status file (`STATUS.md`), the compute
ledger (`compute-ledger.md`), the `docs/` folder including the research
note the denoising idea came from, the registered texts
(`amendment-a3.md` and `pre-registration.md`), the red-team ledger
(`red_team_ledger.md`), any chat transcript, any uncommitted file, and the
model checkpoint files themselves.

Two consequences of that, stated so they are not mistaken for omissions.
**First**, the packet says the interpretation is read against the
registered texts, and those are on the do-not-open list, so I cannot check
the interpretation against them. Nothing below turns on registered text.
**Second**, I could not read the red-team ledger to see the last number
used, so I have numbered findings from **RT-33**, reading "continue from
RT-32" as meaning RT-32 is taken. If that is off by one, the numbers
renumber trivially.

No outside lookup was used. Every number below either comes from a
committed record or from a check I ran myself, and each is labelled.

**Verdict in one line.** The CARRIED NOWHERE result is sound, correctly
computed and honestly reported — I reproduced every published number from
the records. The sentence built on top of it is not. The stack's own
committed records contain a measurement showing that the read used
throughout the sweep is roughly half as accurate as an ordinary fitted
linear read on the same states, and that measurement appears in none of
the four findings files.

---

# 1. Feasibility

*For every quantity the method files pre-state or threshold: can it be
measured at all, can the control actually reach the threshold, and is
there a committed record behind it?*

| # | pre-stated quantity | can it be measured? | record behind it | severity |
|---|---|---|---|---|
| F1 | the family bar of 3.56 standard deviations | yes | recorded in all three sweep files; arithmetic reproduces | none |
| F2 | the per-test bar of 3.0 standard deviations, reported for continuity | yes | recorded per test | none |
| F3 | the 1,000-draw null | yes | every one of the 330 tests records 1,000 draws and a count | none |
| F4 | the positive control reaching the bar | yes, by a wide margin | +159, +21, +29 standard deviations, no draw beating it | none |
| F5 | the negative control | yes | 30 tests, −2.19 to +0.76, none clears | none |
| F6 | reproducing the earlier anchor result | yes | all 60 shared tests bit-identical | none |
| F7 | the scorer agreeing with the original | yes | differences of exactly 0.0, recorded in every file | none |
| F8 | checkpoints verified by checksum | yes | the three checksums in the records match the ones the method files fixed in advance | none |
| F9 | method committed before output | yes | commit history and recorded runtimes agree | none |
| F10 → RT-37 | **the smallest signal the sweep could detect** | yes | **no record anywhere** | worth-noting |
| F11 → RT-38 | **the degeneracy preconditions** | yes | **fired twice; not reported in the findings** | worth-noting |
| F12 → RT-39 | **the independence the family bar assumes** | yes | **five fold splits shared across all 270 tests** | worth-noting |
| F13 → RT-40 | **the geometry of the states at the ten non-anchor positions** | not from the record | **none exists** | worth-noting |

Nothing in this part is fatal. The packet's fatal trigger — a "verified"
or "measured" claim with no record behind it — is not tripped. I went
looking for it and did not find it. The record is in unusually good shape.

**Everything the two headline sentences claim, reproduces.** MEASURED. I
recomputed the published numbers from the fifteen records rather than
reading them off the tables:

| claim in the findings | recomputed | agrees |
|---|---|---|
| 270 testable tests | 270 (330 total, minus 5 layers × 2 arms × 3 checkpoints for each of the two control positions) | yes |
| largest margin +2.73 | +2.73 (seed 1, marker word, the other agent's revision value, layer 8) | yes |
| smallest margin −2.59 | −2.59 (seed 1, register index, the appended question's answer, layer 3) | yes |
| mean across the 270 is −0.085 | −0.0846 | yes |
| nothing reaches 3.0, let alone 3.56 | confirmed, both | yes |
| zero marginal and zero robust clearances among the testable tests | confirmed | yes |
| positive control +159.08 / +20.66 / +29.45 | exact | yes |
| every one of the 22 rows in the two position tables | all 66 numbers exact | yes |
| the anchor "reproduces the previous run exactly" | all 60 shared tests identical to the last decimal place, including the counts of shuffled draws | yes |
| the powered-anchor ranges (−1.85 to +0.49; 308 to 980 draws; 502 to 980 on arm 1) | exact | yes |

**The pre-commitment is real and independently checkable.** MEASURED. The
method file and the code for the eleven-position sweep went in as one
commit at 17:13 Pacific on 2026-09-19, touching no output. The records and
the findings went in as a separate commit at 18:08, 55 minutes later. Each
checkpoint's recorded runtime is about 53 minutes, and the method file says
the three were run as parallel processes — so the timing fits a run started
immediately after the method was fixed, with no room for a run beforehand.
The only change that commit made to existing code was to pass the family
bar in as a parameter and record which value was used; the statistics were
untouched, which is why the 60 shared tests come back bit-identical. This
is the strongest part of the whole package and it deserves saying so.

**The family-bar arithmetic is right.** MEASURED. Recomputing from
scratch: at a 3.0-standard-deviation bar one test in 741 clears by luck;
across 270 tests the chance of at least one false clearance is 30.6 per
cent; the bar that brings that back to 5 per cent is 3.55, quoted as 3.56.
The earlier runs' figures check out too (15 tests → 2.0 per cent, bar 2.71;
30 tests → 4.0 per cent, bar 2.93; 45 tests → bar 3.05, quoted 3.06; 165
tests → 20.0 per cent, bar 3.42, quoted 3.43). The honesty note about 1,000
draws resolving only to about 3.09 standard deviations is also correct.

### RT-37 — the smallest detectable signal is nowhere on the record

**Worth-noting. MEASURED.** No method file and no findings file states how
big a signal the sweep would have found. I computed it from the recorded
spread of each null. To reach the 3.56 bar, the model's own marker word
would have to be read at 5.23 per cent accuracy against a chance rate of 4
per cent, and the register index at 27.93 per cent against 25 per cent.
Put in plain terms, the sweep would detect an identity that is perfectly
legible in as few as **1.3 per cent of episodes** for the marker word, or
**3.9 per cent** for the register index. That is genuinely good power, and
it is a point in the result's favour.

It should be in the findings. A null result whose stated strength is "270
tests found nothing" is much weaker than one that says "270 tests would
have found a signal present in one episode in eighty, and found nothing."
The second sentence is true and is not written down anywhere.

Two things this number does **not** cover, and they are the subject of
part 2: it assumes the identity sits in the directions this read can see,
and it says nothing about a reader other than a difference of averages.

### RT-38 — two pre-stated preconditions fired and the findings do not say so

**Worth-noting. MEASURED.** The method pre-states that a test whose
accuracy exactly equals the majority-class rate is degenerate and gets no
cell. Two testable tests on the pilot did exactly that — the register
index read before the model's own revision turn at layer 7, and at the
appended question's answer token at layer 8, both landing on 0.2582
against a majority-class rate of 0.2582. Both are flagged in the record
and neither is mentioned in the findings, which report all 270 as tests
that answered.

This changes nothing material: both sat around one standard deviation,
nowhere near any bar, and the cell is a null either way. Strictly the
discovery family was 268, which would move the bar from 3.56 to about
3.55. It is worth a line because the whole point of writing preconditions
down in advance is to report them when they fire, and because the
denoised-direction findings set the right precedent by saying explicitly
that nothing was reported degenerate. The eleven-position sweep dropped
that sentence in the run where it would have been untrue.

### RT-39 — the 270 tests share five fold splits and five sets of shuffles

**Worth-noting. MEASURED.** In the code, each test's fold split and its
1,000 shuffled label draws are seeded by the layer number alone
(`measure(..., seed=Lr)`). So every test at layer 3 — both arms, all
eleven positions, all three checkpoints — uses one identical fold split
and one identical sequence of 1,000 shuffles. There are five distinct
splits across the whole sweep, not 270.

This cuts both ways and neither way is large. The nulls at a given layer
move together, so a lucky or unlucky set of shuffles is shared rather than
averaged out. And the family bar treats 270 tests as independent when five
layers reading the same states and two arms sharing a target are strongly
related, so the true bar is lower than 3.56 and the sweep is stricter than
it needed to be. Both are moot in the event, because the largest margin
anywhere was 2.73 and nothing came near even the unadjusted bar. I record
it because the method file's arithmetic is presented as if the tests were
