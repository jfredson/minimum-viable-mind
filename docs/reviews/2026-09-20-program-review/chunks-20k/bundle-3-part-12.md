> amendment, and the recommendation below to run the free thing first.
>
> The October question is no longer whether to make the control learn. It
> is whether the clause can be repaired at all, and whether that repair is
> a metric change rather than a training change. See
> `ceiling-measurement-findings.md`.

**Do the free diagnostic first, then decide between A and C. Do not spend
yet.**

The audit produced a hypothesis with a sharp, free test. The control fails
for one of three reasons: the model cannot do name-keyed retrieval at all,
it can retrieve but not apply the successor rule, or the reversed
rendering defeats the retrieval specifically. **These are distinguishable
on the checkpoints already in hand, locally and for nothing**, by asking
the trained models plain lookup questions without the rule step and
comparing against the control's own score.

That matters because option C is a bet that supervision is the binding
constraint. If the diagnostic shows the models cannot retrieve by name at
all, more supervision on the same rendering is likely to buy little and
option D becomes the honest candidate. If they retrieve well and fail only
at the rule step, C is well targeted and cheap.

**Whichever way the decision goes, register the ceiling defect.** The
control's 0.3227 was never attack-verified, is set by a solver blind to
the name the question supplies, and disagrees with the module's own stated
0.5. That is a defect in the registered instrument, independent of whether
A3 continues, and it belongs on the record either way. If A3 closes, it
belongs in the write-up as a limitation of the comparison that was never
available. If A4 opens, the ceiling must be measured properly first,
because an amendment built on an unverified denominator would inherit the
same problem.

**What I am not recommending.** I am not recommending the eval-side change
that would make the numbers work. It is available, it is free, and it is
the wrong thing to do.

## What this decision does not settle

Where ownership lives. Every result here comes from removing an input
channel, which shows the action depends on ownership without showing the
network built an internal structure carrying it. The localization work
that was meant to answer that is unvalidated at this scale, and no
control-battery decision changes it.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-control-learnability-packet.md =====

# Review packet — the control-learnability pilot (Gate B, tier 1)

*Prepared 2026-09-20 (Pacific) under `docs/outside-review-protocol.md`.
Gate B: an interpretation that changes program direction, reviewed before
it enters STATUS.md's current-state section. This one also feeds public
path step 4, the 2026-10-04 control-battery decision, so under Gate C the
proposal that carries that decision will cite this review.*

## The interpretation under review

From the session that ran the pilot (commits `062636e`, `a569a35`, both
on main):

> The control battery does not learn when properly supervised. It scored
> 0.3125 (sd 0.0240) after an intervention that quadrupled its per-row
> gradient weight and took its share of the query gradient from about a
> third to about two thirds. The three existing checkpoints, with none of
> that, scored 0.2877, 0.3057 and 0.3195. Against the pre-stated cells:
> 0.42 sd below the 0.3227 boundary, 11.98 sd below 0.60. The cell is DID
> NOT LEARN. Both secondary cells pass, so this is a real answer, not a
> failed intervention. Supervision was not the binding constraint. What
> is left are the explanations that are not about supervision: the
> reversed rendering, the missing private route, and an answer that
> appears in no turn.

The session's own qualifications, which the review should test rather
than take on trust: across six evaluation seeds the control ranged
0.2850 to 0.3460, so a rerun could formally land in PARTIAL; and the
control is not inert, since it falls under the lesion from 0.3125 to
0.2613.

## What the reviewer gets, and nothing else

All in `experiments/06-mvm-0a-constructed-self-index/` at commit
`a569a35`. Read in this order.

- `control-learnability-pilot.md` — the pre-statement, committed before
  the code existed (`7eee3c5`). The cells are read against this.
- `control-learnability-pilot-findings.md` — the findings under review.
- `a3-gates/endpoint_a3ctl_30m_seed0.json` — the full-budget endpoint
  (step 55,116), the record the cells are read on.
- `a3-gates/endpoint_a3ctl_30m_seed0_PARTIAL_step51500.json` — the
  partial-checkpoint endpoint, for comparison only.
- The training log and trajectory record for the run, wherever the
  findings file says they are.
- `src/train_a3.py` and `src/launch_ctl_pilot.sh` — the loss change
  (`ee7fc91`) and the launcher; the self-test that claims the off path is
  bit-identical to the old pooled term.
- `compute-ledger.md`, the two rows dated 2026-09-19 (pilot) and
  2026-09-20 (recovery) only.
- `gate2-pilot-findings.md` and `seeds-endpoint-findings.md` — the three
  comparison checkpoints' control scores.
- Registered text the interpretation is read against: `amendment-a3.md`
  (the control battery's definition, its ceiling, and §3.2) and
  `ceiling-defect-2026-09-17.md`.

Do not open: STATUS.md, `docs/`, the A4 files, any chat transcript, any
uncommitted file. Say at the top of the findings file what was opened.

## The brief (fixed text from the protocol)

Four parts, in this order, a table first in each, severity marked fatal,
serious, or worth-noting, and a one-paragraph kill case at the end whether
or not you think the interpretation should stand.

1. **Feasibility.** For every quantity the pre-statement names: is the
   0.3227 boundary the right number (it is the control's ownership-blind
   ceiling as registered; the 2026-09-17 defect says that ceiling was
   never attacked), is the 0.60 boundary reachable by this battery in
   principle, and did the intervention actually deliver the supervision
   it claims (per-row weight, share of rows), citing the training log or
   the code. A "verified" or "measured" claim with no record behind it is
   a fatal finding on its own.
2. **Satisfied by the wrong thing.** Every way DID NOT LEARN could be
   returned by a control battery that would learn under supervision: an
   intervention that did not reach the control's rows, a loss term on
   the wrong scale, an evaluation that cannot see what was learned, a
   ceiling boundary that is itself wrong.
3. **No verdict.** Every way the run could have failed to answer the
   supervision question and been read as answering it, including the
   seed-1-only design and the six-seed spread straddling the boundary.
4. **Over-reading.** What "supervision is not the binding constraint"
   will be read as claiming in STATUS.md, in the step 4 proposal, and in
   the paper, beyond what one seed at one weight setting measured. Say
   whether the finding supports narrowing step 4 to "option D or close
   A3", or whether a cheaper supervision variant is still live. Write the
   sentence that should go in STATUS.md.

Label every finding MEASURED or ARGUED. Continue the ledger numbering
from RT-51. Plain language throughout. Lookup allowed and flagged. Do not
soften findings to be polite.

## Filing

Findings to `reviews/2026-09-20-control-learnability-claude-worktree.md`,
verbatim, never edited after filing. Rulings go in `red_team_ledger.md`.
Nothing from this enters STATUS.md or the step 4 proposal until John
rules on it.


===== FILE: experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-20-control-learnability-claude-worktree.md =====

# Findings — the control-learnability pilot (Gate B, tier 1)

*Filed 2026-09-20 under the outside-review protocol, against the review
packet for the control-learnability pilot
(`reviews/2026-09-20-control-learnability-packet.md`). Verbatim once
filed. Rulings are John's and go in the red-team ledger
(`red_team_ledger.md`); nothing here is a ruling.*

## What was opened, and nothing else

Everything below was read at the commit the packet names — the ledger
commit that closed both spend rows (`a569a35`). I first checked that none
of the listed files changed between that commit and the current tip of the
main branch; none did, so the working copies are the right versions.

Opened, all inside `experiments/06-mvm-0a-constructed-self-index/`:

- the pre-statement (`control-learnability-pilot.md`)
- the findings under review (`control-learnability-pilot-findings.md`)
- the full-budget endpoint record (`a3-gates/endpoint_a3ctl_30m_seed0.json`)
- the partial-checkpoint endpoint record
  (`a3-gates/endpoint_a3ctl_30m_seed0_PARTIAL_step51500.json`)
- the trainer (`src/train_a3.py`) and the pilot launcher
  (`src/launch_ctl_pilot.sh`)
- the compute ledger (`compute-ledger.md`), the two rows dated 2026-09-19
  (the pilot) and 2026-09-20 (the checkpoint recovery)
- the two comparison write-ups (`gate2-pilot-findings.md` and
  `seeds-endpoint-findings.md`)
- the registered text the interpretation is read against: Amendment A3
  (`amendment-a3.md`) — the battery table in §2.5, the lesion protocol in
  §3.1 and §3.2, the pre-stated signatures in §3.5, and registration
  revisions 3 and 4, which carry the metric and the ceilings — and the
  registered ceiling defect (`ceiling-defect-2026-09-17.md`)
- the red-team ledger, to read its last entry number only, so this file
  continues the numbering correctly

**The training log and the trajectory record were not opened, because they
are not in the repository.** The findings file never says where they are,
which is the first thing to record. They do exist on the laptop, in the
run's artifacts folder alongside the checkpoint; I established that by
listing the folder and reading no file in it, because the packet forbids
opening uncommitted files and everything under `artifacts/` is excluded
from the repository by `.gitignore`. See finding RT-56.

**Not opened, as instructed:** the current-state document (`STATUS.md`),
the `docs/` folder, anything to do with the A4 clause, any chat
transcript, any uncommitted file. Two modules I wanted and did not take
because the packet does not list them: the episode generator
(`curriculum_a3.py`) and the encoder (`encoding_a3.py`). Two findings
below (RT-58 and RT-59) are limited by exactly that, and say so.

**Lookup: none.** No web search, no external source. Every number here is
computed from the files listed above, and every computation is shown.

**Severity across this review: eighteen findings — one fatal, ten
serious, five worth-noting, and two checks that came back clean and are
recorded as clean.** Numbering continues from the ledger's last entry
(`RT-51`), so this file runs from `RT-52` to `RT-69`.

---

## 1. Feasibility

*For every quantity the pre-statement names: is the boundary the right
number, is the higher boundary reachable at all, and did the intervention
deliver the supervision it claims.*

| id | finding | label | severity |
|---|---|---|---|
| RT-52 | 0.3227 is not a ceiling, and the registered text naming it is already recorded as defective — but it is still the right number for the cell it was used in | MEASURED | serious |
| RT-53 | The endpoint record states a floor rule the programme corrected three days before the run | MEASURED | serious |
| RT-54 | The 0.60 boundary is reachable in principle; the battery's real limit is near 1.0 | MEASURED | worth-noting |
| RT-55 | The supervision was delivered, exactly as claimed — the findings file cites nothing for it, and the endpoint record does not carry the run's settings | MEASURED | serious |
| RT-56 | The training log and the trajectory record are not in the repository, though the previous run's equivalent is | MEASURED | serious |

### RT-52 — the boundary is the right number wearing the wrong label

**MEASURED. Serious.**

The pre-statement, the findings file and the endpoint record all call
0.3227 the control battery's "ownership-blind ceiling". The programme's
own registered defect of 2026-09-17 says that is false, and says so in
the registered text itself: the attack sweep that Amendment A3 credits
with verifying both ceilings contains no control-battery code at all, so
the claim "verified by the attack sweep" covers the primary battery only.
The 0.3227 comes from one reference solver that never reads the marker
the control question supplies. The question names an agent; the solver
enumerates all four agents' successors on the item, strikes the ones
already visible as revisions, and guesses among the rest.

So 0.3227 is the score of a solver that cannot read names, and the
battery's real ownership-blind ceiling is near 1.0 and unmeasured.

**And yet the number is fit for the cell that used it.** "The control did
not learn name-keyed lookup" means precisely "it scores no better than a
solver that cannot read the name", and 0.3227 is that solver's score. The
pre-statement's own gloss is correct — "a battery at or below it has not
learned the task, whatever else is true." Nothing about the verdict turns
on the mislabel.

What does turn on it: a Gate B interpretation rests on a boundary the
programme formally registered as defective three days before the run, and
**the findings file never mentions the defect.** Anyone reading the
findings alone would take 0.3227 for a checked quantity. It is not one,
and John has already ruled that measuring this ceiling properly is a
precondition of any Amendment A4.

**Fix:** the findings file should cite the ceiling defect
(`ceiling-defect-2026-09-17.md`) and call 0.3227 what it is — the score
of a name-blind reference solver — everywhere it appears.

### RT-53 — the endpoint record carries a superseded rule

**MEASURED. Serious.**

The full-budget endpoint record describes the metric this way:

> floor rule leaves a battery undefined when its baseline is below its own
> ownership-blind ceiling

That is the rule as it was stated before 2026-09-17. The correction of
that date, recorded in the three-seed write-up
(`seeds-endpoint-findings.md`), says the floor rule is not "baseline
below ceiling" but **baseline minus ceiling below 0.10** — so the control
needs **0.4227**, not 0.3227, for its drop to be a defined quantity at
all.

No number moves: the control reads 0.3125, which is below both. But the
artifact that carries the reading encodes a rule the programme corrected
before the run was launched, and the same superseded sentence sits in the
partial-checkpoint record too. The consequence is not arithmetic, it is
that 0.4227 — the number that actually decides whether this battery is any
use to Amendment A3 — appears nowhere in the pilot's pre-statement,
findings or endpoint records. That omission does real work in part 4
below.

### RT-54 — the higher boundary is reachable, on an argument nobody has attacked

**MEASURED. Worth-noting.**

Checked and clear. Amendment A3's battery table puts chance on this
battery at 0.125 — a forced choice among eight. The ceiling defect
establishes that every turn renders the speaker's marker in plain text,
so a solver doing ordinary name-keyed lookup "answers correctly every
time". The battery's attainable score is therefore about 1.0, and the
0.60 boundary sits comfortably inside it. **The LEARNED cell was not set
at an unreachable number.**

The caveat is that "near 1.0" is analytic and explicitly unmeasured — the
defect memo says so in as many words — and the attack sweep has still
never been pointed at this battery. So "reachable in principle" rests on
an argument that has not been adversarially tested, which is the same
weakness RT-52 records at the other end of the scale.

### RT-55 — the supervision was delivered; the findings file cites nothing for it

**MEASURED. Serious, and explicitly not fatal — I found the record.**

The findings file's load-bearing claim is that "its per-row gradient
weight quadrupled and its share of the query gradient went from about a
third to about two thirds." It carries no citation whatsoever. The
packet's rule is that a measured claim with no record behind it is fatal
on its own. **It is not fatal here, because the record exists and I found
it — in the compute ledger's pilot row, dated 2026-09-19. But the findings
file does not point at it, and the endpoint record does not carry the
run's settings either.**

The claim itself is exactly right. I checked it two ways.

**From the code.** With the flag off, the query loss is the total loss on
the answer tokens divided by their count, so each of the 128 rows carries
one one-hundred-and-twenty-eighth of the term, and the round-robin gives
the control battery about one row in three — a share of about a third.
With the flag on at the settings used, half the batch (64 rows) carries
the control question, the control's own term is the average over those 64
rows, and that term is multiplied by 2. So each control row carries two
sixty-fourths, which is one thirty-second: **exactly four times**
one-one-hundred-and-twenty-eighth. By the same arithmetic the control's
total weight is 2.0 against the other batteries' 1.0, so its share of the
query gradient is **exactly two thirds**, up from a third. Both figures in
the findings are right to the digit.

**From the run.** The ledger records the query loss at step 500 as 3.433
for this run against 1.075 for the matched earlier pilot, and notes that
"other-term + 2 × control-term" predicts about 1.1 + 2 × 1.15 = 3.40.
That is direct evidence the split fired on the rented machine and fired at
the right scale, not merely that the flag was typed. The ledger also
quotes John's go verbatim with the two settings in it, records that the
trainer's self-test ran on the pod before any training step, and records
the measured pace at 0.6508 seconds per step against the earlier pilot's
0.6501 — so the flag cost nothing and the run was not short-changed.

**Fix, and it is cheap.** The trainer already saves the run's full
settings into the checkpoint. The endpoint record should echo the two that
matter — the control weight and the control fraction — so the artifact
that carries the reading is self-contained. As it stands, the only thing
tying that record to a run with the flag on is the output name.

### RT-56 — the log and the trajectory are not in the repository

**MEASURED. Serious.**

The packet asked for "the training log and trajectory record for the run,
wherever the findings file says they are." The findings file does not say.
Its only reference to the log is a claim sourced to it — "the trainer's
own log records both acts on consecutive lines" — with no path.

They exist. The run's artifacts folder holds the trainer's log, the
trajectory file and a complete copy of it, alongside both checkpoints.
Everything under `artifacts/` is excluded from the repository by
`.gitignore`, so **none of it can be cited at a commit**, and the packet's
own rule against uncommitted files put all of it outside this review.

Two things make this worse than a filing quibble.

1. **The previous run's equivalent is committed.** The A3 pilot's
   trajectory sits in the gates folder (`a3-gates/pilot_trajectory.jsonl`)
   at about 20 kilobytes. This run's is the same size and is not
   committed. The precedent exists and was not followed.
2. **The trajectory is the only record that could answer several
   questions this review had to leave open** — most of all whether the
   control battery was flat throughout or moved and came back, and what
   the loss did after step 1,000. The ledger preserves two points; the
   file has 109 evaluations.

The claim about the two log lines is itself fine, because the ledger
quotes them verbatim. The fix is one command, and it should be done before
this finding is quoted anywhere.

---

## 2. Satisfied by the wrong thing

*Every way DID NOT LEARN could be returned by a control battery that would
learn under supervision.*

| id | finding | label | severity |
|---|---|---|---|
