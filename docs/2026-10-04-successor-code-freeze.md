# The successor's code, frozen and tested at $0 (2026-10-04)

*Written 2026-10-04 (Pacific) by the Claude Code session that built and ran
it. Laptop only; nothing rented; $0. Method committed before any test ran:
`docs/successor-code-freeze-method-2026-10-04.md` (commit `ee012ca`). Code:
`experiments/08-successor-degree/` (first committed at `c1d343a`; the frozen
commit is the one this pull request merges). Nothing here is a ruling, and
nothing here is a result about the scientific question.*

*Written under the workspace plain-language rule.*

## 1. In short

Step 3 of the successor plan (version 4 of the proposal, section 11) is done
at $0, apart from the check by a session that did not write the code, which
the weekend plan schedules beside the development runs. The task generator,
the four models, the measurement and the trainer for the rented machine are
in one new folder, `experiments/08-successor-degree/`, with the spending
tripwire version 4 asked for and a launcher derived from the one it names.

- **The frozen code is the rehearsal's code where it should be.** All twelve
  committed toy models load into it and give outputs and internal states
  identical to the bit (test T2). The procedure, run on those models with the
  reads the toy record used, reproduces **all 502 figures compared** from the
  committed toy record, with none different (test T3a): every nomination,
  site set, reading, control, true-slot reading, rider, both ways of the
  piece's accuracy elsewhere, control 2 against twenty random pieces, and the
  separation (1.0051, 0.9926 and 0.9974).
- **Fitting the reads once on the processor, as the registered run will,
  changes no decision on the toy** (test T3b): of the 283 figures that decide
  anything, none moves; 25 lesser figures move, all piece counts by at most 7
  held-out episodes of 180, and a few shares on the free model.
- **The site-set rule gives version 4's numbers** (test T4): 325 site sets
  and 1,300 comparisons on the registered model, 312 under the stricter
  variant, row by row as section 18 prints them; 45 and 40 on the toy; 153
  and 144 at 10 million.
- **Everything runs end to end at 10 million and 30 million parameters**
  (test T6), from the trainer the rented machine will run to the outcome term.
- **The launcher creates nothing on a dry run and calls no vendor** (test
  T7), refuses without its settings, and reports a tripwire halt.
- **One thing for the registration text, found by the code and not changed in
  it** (section 4.1): applied as written, version 4's outcome rules put the toy
  on R3, "substrate not a testbed", because the free model fails its learning
  gate; version 4's section 3 says the toy reaches the fifth term.
- **The full-size training recipe is not set by any ruling** (section 4.2).
  The trainer takes it as arguments with defaults this session chose; the
  registration text must fix it.

The go packet for the four development runs and their four ledger rows,
estimates only, are written (section 5). Nothing was launched.

## 2. What was built

| File | What it is | What is new beside the rehearsal |
|---|---|---|
| `src/grammar.py` | the episode generator | the evaluation sets named with the toy's seeds; training episodes streamed per step and never matching an evaluation set; the acting channel fixed on both action turns; a pinned fingerprint of the evaluation sets, so a rented machine whose numpy builds different episodes fails its own pre-flight |
| `src/models.py` | arms T, C, M and F | three sizes by name; the one-scored-token check run on the models' own loss |
| `src/transplant.py` | the transplants | the helpers the later toy scripts added, in one file, with known-answer tests at two depths |
| `src/measure.py` | the reading and the outcome | **withholding a reading** when a control that holds fails; **two of three**; **the separation** as arm C's lowest minus arm T's highest; the outcome terms; the sampling band |
| `src/procedure.py` | the whole measurement | one procedure for any depth, with the reads fitted once on the processor, written to disk and reloaded |
| `src/train_successor.py` | the trainer | new: version 4 listed it as owed |
| `src/tripwire.py` | the spending tripwire | new: version 4 listed it as owed |
| `src/launch_successor.sh` | the launcher | derived from `launch_a3_fetch_first.sh`; everything that keeps money safe carried over |
| `requirements-measure.txt` | the pinned libraries | as ruled the night of 2026-10-03 |

Parameter counts, from the self-test: at the size called 10M, 5.27 million
(arm T) to 6.47 million (arm C); at 30M, 26.07 to 29.33 million. The rung
names are the programme's scale ladder; with a 46-word vocabulary the counts
come in below them.

## 3. The tests, against the pass lines written beforehand

Outputs are in `experiments/08-successor-degree/out-freeze-tests/`.

**T1, every self-test: passes.** 195 checks across seven files
(`t1-self-tests.txt`). Among them the two carried-over rules on the built
generator. The even-split rule (RT-58): the stream and the trainer refuse an
odd batch, and every streamed batch is whole matched pairs. The
one-scored-token check (RT-59): two scored positions per episode, each the
mask word after the answer cue, no value word anywhere in the action turns,
a planted leak and a planted shift both caught, and on every arm the loss is
exactly the cross-entropy at those two positions, with nothing after them
able to change it. On arm T, by construction, the cue before the scored
position cannot change it either; the test said otherwise at first and was
wrong about arm T, not the code.

**T2, the frozen models are the rehearsal's: passes.** Twelve of twelve
(`t2-load-toy-models.txt`).

**T3a, the committed toy figures: passes.** 502 compared, 0 different
(`t3a-committed-reads/comparison.json`). Two things happened on the way and
are on the record. The first run was stopped by a time limit after eleven
models; a later run reused those rows and found four differences: three were
the rider on arm T, which the toy code computed (it equals arm T's reading)
and the frozen code had skipped, now fixed; the fourth is section 4.1. The run
the pass rests on was then made from scratch on the final code.

**T3b, reads fitted fresh on the processor: reported, no pass line.** 502
compared, 25 different (`t3b-fresh-fit/comparison.json`). None is a status,
site set, reading, control verdict, true-slot reading, rider or the
separation (283 such figures, all equal). The 25: piece counts at states and
sizes the rule did not choose, moving by up to 7 of 180; the counts at the
other positions of a site, by a few; on the free model, which returns no
verdict either way, the described-only piece count (19 against 22, and 16
against 17) and two control shares by one trial in 800. The cause is the one
the review of version 3 named (RT-232): the committed directions were fitted
on the graphics chip. Fifty-two of the 200-shuffle null's fits on shuffled
labels stopped at their iteration limit; the null is a reference printed
beside the floor and not a bar, so this is reported and not changed.

**T4, the site-set rule: passes** (`procedure.py --self-test`, in T1).

**T6, the pipeline at 10 million and 30 million: see the end of this
section.** Each arm trained for 30 steps by `train_successor.py` exactly as
the rented machine runs it, then measured with every episode count scaled to
a quarter and three shuffles (so nothing here is a registered figure).
Untrained models are expected to return no verdict, and they do: at 10
million every arm is withheld because it fails its gate, and the outcome is
R3; arms T and M still nominate their built slot at state 0 and pass the
controls that hold for them (7 and 4, and 1 on arm T), which shows the
withholding acting on a model whose arithmetic would otherwise print. At 30 million every arm also runs end to end: each row uses the
family of 325 site sets and 1,300 comparisons, every arm is withheld, and the
outcome is R3. On the untrained entangled and mixed models the no-transplant
rule also fires (a miss of about 0.02 against an allowance of 0.018): an
untrained model's wrong answers are not spread evenly over the other values,
which is what the competing-solver ruling of 2026-10-04 (item 3) said of that
formula. **The test found one bug, now fixed:** the table writer failed when
an arm's true-slot reference itself returned no verdict, which the toy never
produced; it now prints "no verdict", and a self-test case covers it. Two
practical notes: the pipeline job hit the two-hour limit on a background
command while measuring the last 30M arm, which was then measured and the
summary written by separate commands with the same settings
(`t6-stdout.txt` says so); and the 30M measurement takes about 25 minutes per
model on this laptop at a quarter of the episodes, so a full-count measurement
of one full-size model will take hours, not minutes.

**T7, the launcher: passes** (`t7-check-launcher.txt`). The argument guard
refuses and says why, before any vendor command; a dry run exits 0, says it
created nothing, and the stand-in vendor tool on its path was never called;
it refuses without each required setting and refuses the toy size; it
reports a tripwire halt file; experiment 06's remote-start check passes on
it. A dry run on 2026-10-04 also showed that a real launch would be refused
today: **the Mac's never-sleep override is off.**

## 4. What the freeze found for the registration text

### 4.1 The toy's outcome, under the rules as written, is R3, not the fifth term

Version 4, section 3, says: "Under the rules this version registers, the toy
reaches the fifth term: its anchors separate and its free arm is not read."
Applied as the code applies them, the same rules give R3, "substrate not a
testbed": R3 is "one or more arms fail its gate after the one permitted
re-run", and the toy free model fails its learning gate (the named-other
condition clears on one seed of three). Step 5a says the same of the
registered run: a free-model gate failure after the re-run is R3 and nothing
else launches. So the sentence in section 3 is the loose one, and the code
follows the rule: `measure.outcome` returns R3 whenever a gate fails, and the
fifth term only when the free model passes its gate and is still not read.
`procedure.summarise` accepts the gate after a permitted re-run as an input,
so the registered run is not caught by the toy's lack of a re-run. **The
registration text should say which the toy reaches, and in what words.**
This is reported; nothing was changed to make the toy land on the fifth term.

### 4.2 The full-size training recipe is not set

Version 4 says the arms train "on the same token budget" and that "the
training recipe is the rehearsal's unchanged recipe", which together do not
fix a recipe at 30 million parameters. The trainer's defaults, the freeze
session's call (method note, section 3): the rehearsal's optimiser and
schedule unchanged, 96 episodes a step, the closed design's 585,544,960
tokens (108,919 steps), and training episodes generated fresh each step and
kept out of every evaluation set. **The registration text must fix these.**
The development runs use the same defaults at 10 million, so they test the
loop as it would run.

### 4.3 Smaller notes

- The sampling band is printed as the exact 95 per cent interval around the
  count, with the range a piece at exactly four fifths lands in beside it (133
  to 154 of 180). The ruling asked for the band and not its form.
- The registered piece's accuracy and its band are printed in every row; the
  rows also carry the count's distance from the floor in episodes.
- The withholding acts in the output: a withheld row carries "no verdict"
  and every reason, and keeps the arithmetic under a separate name
  (`arithmetic_withheld`) so a reader can see what was not reported.

## 5. The go packet and the ledger

`docs/rulings/2026-10-04-development-runs-go-PROPOSAL.md` asks for one go
naming four runs at 10 million, seed 0, one per arm, arm M first and alone.
Estimate **about $0.60 to $1.25 a run**, about $2.40 to $5.00 for the four,
from the laptop's measured 0.35 seconds a step and the rented card's measured
speed against this laptop; **hard cap $2.50 a run, $10 for the four**, from
the first release's development line. Four rows are in the compute ledger
with those estimates and no actual cost (the launch gate accepts them;
checked). A planning session relayed that John said "the $10 is approved";
this session did not hear it, and the packet asks the launching session to
quote his own words in the rows, as the ledger's rule requires. Before a real
launch the Mac's never-sleep override must be switched on.

## 6. What this does not do

It does not launch anything, register anything, or edit a registered file or
anything in the rehearsal folder. It changes no ruled number. It has not been
checked by a session that did not write it; the weekend plan puts that check
beside the development runs, and it should look first at section 4.1, at the
port of the toy scripts into `procedure.py`, and at the tripwire, which has
only met recorded vendor readings and never the vendor.
