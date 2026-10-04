# Go packet: the four development runs at 10 million parameters (step 4 of the successor plan)

*Prepared 2026-10-04 (Pacific) by the Claude Code session that froze the
successor's code (`docs/successor-code-freeze-method-2026-10-04.md`; findings
`docs/2026-10-04-successor-code-freeze.md`). **This is a packet, not a go.**
Nothing was created, rented or spent preparing it. The four ledger rows it
names were written with estimates and no actual cost, and launch nothing by
themselves.*

*Written under the workspace plain-language rule.*

## 1. What is asked for

Four training runs on rented machines, one per arm, at the 10-million size,
seed 0, each on its own machine:

| Run (the name the ledger row and the launcher use) | Arm | What it is |
|---|---|---|
| `succ_m_10m_seed0` | M | the half-and-half arm; its code has never run on a rented machine (weakness W9) |
| `succ_t_10m_seed0` | T | the separable arm |
| `succ_c_10m_seed0` | C | the entangled arm |
| `succ_f_10m_seed0` | F | the freely trained arm |

This is step 4 of section 11 of version 4 of the proposal: **a pipeline and
throughput check, not a learnability verdict.** The 10-million size failed to
learn the earlier design's task, so a model that learns nothing here means
nothing about the registered size, and the registration says so in advance.
What the runs are for: the frozen trainer runs end to end on the rented
machine for every arm, including arm M for the first time; the shutdown order
(copy, check, receipt, delete) works for each; the new spending tripwire
meets real billing for the first time; and the seconds per step of the real
training loop, data generation included, are measured on the card, which
reprices the later runs.

**What John has said so far, as it reached this session.** A planning session
of 2026-10-04 relayed that John said "the $10 is approved" for these runs, and
recorded it on the TimeAssembler step "Development runs at 10 million
parameters" (task `8130343a`). This session did not hear him say it, and the
ledger's rule is that a launch quotes John's go verbatim in the run's own row
before the machine exists [C2(b)]. **The session that launches should quote
his words from where he said them, or ask him for a line naming these four
runs and this estimate.** Either way this session launched nothing.

## 2. The money

From **the first release's development line, up to $10** (item 10 of the
2026-09-21 ruling, widened from three arms to four by the Gate C rulings,
RT-229). Nothing has been drawn from that line.

| | Per run | Four runs | How it is reached |
|---|---|---|---|
| Machine time, estimate | about 0.6 to 1.25 hours | about 2.5 to 5 hours | see below |
| Cost, estimate | **about $0.60 to $1.25** | **about $2.40 to $5.00** | at $0.99 an hour, the rate of record; read again from the vendor at creation |
| The plan's figure | $1.94 | $7.77 | the ledger's 2026-08-12 reconciliation of an earlier 10-million run, as version 4 section 12.3 carries it |
| **Hard cap, enforced** | **$2.50** | **$10.00** | `HARD_CAP_USD=2.50`: the laptop deletes the machine about 2 hours 31 minutes after creation, whatever it is doing |

**The estimate, and how rough it is (ARGUED from measurements).** A run is
108,919 steps of 96 episodes (the token budget of 585,544,960 tokens; the
method note, section 3). On this laptop's graphics chip the real training
loop at 10 million took 0.345 to 0.376 seconds a step (measured 2026-10-04,
arms C and M, 400 steps, with another test running beside it). The rented
card ran the registered shape about twenty times faster than this laptop on
2026-09-25 (12.5 milliseconds a step against 255), so the loop should take
about 17 milliseconds a step there, about 31 minutes, if the ratio carries.
It may not: at a small size a card is lightly loaded and fixed costs per step
matter more, which is the direction that makes it slower. Adding about 15
minutes for the machine to start, the push, the self-tests and the shutdown
handshake gives 0.6 to 1.25 hours. **If the loop runs at three times the
estimate, a run still finishes inside its cap**; if it runs slower than about
75 milliseconds a step it does not, the cap deletes the machine, and the run
is written off at $2.50. That is the outcome the cap exists to bound.

**The account.** The vendor balance was last read at $75.8645 on 2026-09-26
(the ledger's second 2026-09-25 row). The funding rule tops up to the wave's
estimate plus $20 and no further; at $10 plus $20 nothing needs adding if the
balance is still above $30. Read it again before launching.

**Where the programme stands after it.** About $228.15 spent across the
programme as of the last ledger row; the worst case of this wave, $10, makes
it about $238.15 of the $450 envelope, inside the first release.

## 3. What must be true before the first machine is created

Each is checked by the launcher or named here for the launching session; none
is optional.

1. **This pull request is merged**, so the frozen code is on the main line
   and the launcher runs from the main checkout (its default artifact folder is
   `~/Code/minimum-viable-mind/experiments/08-successor-degree/artifacts/`).
2. **John's go, quoted verbatim** in each run's ledger row (section 1).
3. **The Mac cannot fall asleep.** On 2026-10-04 the launch gate read the
   never-sleep override as **off** (`SleepDisabled 0`), so a real launch
   would be refused today. John sets it with
   `sudo pmset -a disablesleep 1` (and back afterwards with
   `sudo pmset -a disablesleep 0`); the Mac must be on wall power.
4. **The ledger rows are dated within two days of the launch.** The four rows
   are dated 2026-10-04, so the launch gate accepts them through 2026-10-06; a
   later launch re-dates them (the gate refuses an older row).
5. **Zero machines running, the rate and the stock read at creation**, as
   every earlier launch did: `runpodctl pod list` empty; RTX 5090, secure
   cloud, in the volume's region, at $0.99 an hour.
6. **No tripwire halt file** for the wave (`artifacts/tripwire/dev-10m/HALT`);
   the launcher refuses while one exists, and a balance it cannot read is a
   trip.

## 4. The commands

Arm M first, alone: it is the one whose code has never met the rented machine.
Once its training log shows its first evaluation line (step 2,000, a few
minutes in) and the tripwire watcher has logged a reading, the other three
may go, one after another. Each from
`~/Code/minimum-viable-mind/experiments/08-successor-degree/src`, first with
`DRYRUN=1` and read, then without:

```
ARM=M SIZE=10M SEED=0 WAVE=dev-10m ESTIMATE_HOURS=1.25 HARD_CAP_USD=2.50 RATE_PER_HOUR_USD=0.99 RUN_SUBDIR=succ_m_10m_seed0 CLEAR_RUN_SUBDIR=1 ./launch_successor.sh
```

and the same with `ARM=T`, `ARM=C`, `ARM=F` and the matching `RUN_SUBDIR`
(`succ_t_10m_seed0`, `succ_c_10m_seed0`, `succ_f_10m_seed0`). `RUN_SUBDIR`
keeps each run's files in a folder of their own on the network volume, so the
final copy does not bring every earlier model home on the clock.

## 5. What comes back, and what is done with it

For each run, in `artifacts/<run>/`: the checkpoint (checked by the watchdog
against the machine's copy), the training log with its seconds per step, the
trajectory log, the finished-marker, and the shutdown watcher's log. In
`artifacts/tripwire/dev-10m/`: every balance reading and ratio B.

Then, on the laptop, at no cost: `procedure.py model` on each checkpoint at
the registered episode counts, and `procedure.py summarise`. **Nothing is read
from the figures about learning or about the question.** What is reported:
whether every step ran; the seconds per step on the card, which reprices the
later runs; the billed hours against the machine-existence hours at the wave
boundary (`tripwire.py reconcile`); and the ledger's actual-after rows. Version
4's weekend plan has those results checked by a session that did not write the
code.

## 6. What stops it

- **The tripwire trips** (either billing ratio at or above 1.25, or a check
  that cannot run): halt, not trim; the ledger row is written from the figures
  file; John is told the number. (Version 4, section 12.5; stop S9.)
- **Spend reaches the line**: $10 across the four (stop S5).
- **An arm will not run on the rented machine**: that is a finding about the
  design, and it goes back to John before the registration text, as the
  rented slice's go said of the same case.
- **A corrigibility event** (stop S7): halt before further compute.

## 7. What John is asked

One go, in his own words, naming these four runs, the estimate of about $2.40
to $5.00, and the $10 cap; or a change to any of it (for example, arm M alone
first and the other three only after he has seen its figures).
