# Run record: the three 10-million reruns of arms T, C and M (step 4b), 2026-10-09

*Written 2026-10-09 (Pacific) by the Claude Code session that ran them, a
helper session of the four-day working weekend. This is a record of what ran
and what it cost, with the raw figures the registered code printed. It is not
the reading of the result: whether the repaired route "holds" against the
ruled bar is item 9, for a session that ran none of this.*

## What was run, and on what authority

- **The job:** step 4b of version 5 of the registration text
  (`docs/successor-experiment-proposal-2026-10-07-v5.md`, section 11, and
  section 5.6): the three built arms (T, the separable arm; C, the stirred-in
  or entangled arm; M, the half-and-half arm) retrained once at 10 million
  parameters, seed 0, with the sharpness fixed at 4.0, then each checkpoint
  put through the registered procedure on the laptop, with the in-use check.
- **The code:** the registered frozen code, `experiments/08-successor-degree/src/`
  at `6c47c56`, unchanged on the main line at `e7c6f23` (checked: no
  difference in that folder between the two). Nothing in it was edited.
- **John's go:** "Approved." (2026-10-09, about $1.14 from the development
  money, these three reruns and nothing else), as relayed to this session by
  the overseeing session. This session did not hear it directly. It is quoted
  in the three ledger rows, which were written and committed (`3ba6ff8`)
  before any machine existed.
- **The launcher and its settings:** `launch_successor.sh`, as the
  2026-10-04 go packet ran it, with a new wave name and a tighter hard cap:
  `SIZE=10M SEED=0 WAVE=rerun-10m-2026-10-09 ESTIMATE_HOURS=0.5
  HARD_CAP_USD=1.00 RATE_PER_HOUR_USD=0.99 RUN_SUBDIR=<run>
  CLEAR_RUN_SUBDIR=1`, each with a dry run first. The run names add
  `_rerun` (`succ_t_10m_seed0_rerun` and so on) so that the 2026-10-04
  development checkpoints are not overwritten.
- **The measurement:** `python src/procedure.py model --ckpt <checkpoint>
  --seed 0 --out out-reruns-10m` for each arm, then `procedure.py summarise
  --dir out-reruns-10m`, on the laptop's processor with the pinned library
  versions (torch 2.12.1, scikit-learn 1.9.0, numpy 2.5.0, Python 3.12.13;
  each row records them).

## Machines and times (UTC)

| Run | Machine | Created | Deleted | Life | Training (108,919 steps) |
|---|---|---|---|---|---|
| `succ_m_10m_seed0_rerun` (arm M) | `xp6pphlx9xo4rl` | 18:10:04 | 18:35:30 | 25 min 25 s | 1,391 s, 0.0129 s a step |
| `succ_t_10m_seed0_rerun` (arm T) | `f08ds538z5ld7p` | 18:19:43 | 18:39:47 | 20 min 4 s | 1,075 s, 0.0099 s a step |
| `succ_c_10m_seed0_rerun` (arm C) | `ao52cuhyg8lpor` | 18:34:16 | 18:54:29 | 20 min 12 s | 1,058 s, 0.0098 s a step |

All three were RTX 5090s, secure cloud, region RO, on volume `x9f8pkn58t`.
Each trained to its last step (108,919 steps, 585,548,544 tokens) and wrote
its finished-marker. Each checkpoint was copied home, checked against the
machine's copy, and only then was the receipt written and the machine
deleted. Arm M went first and alone. Arm T followed once M's training log
showed its evaluation lines and the alarm had a reading, and arm C after T.
The laptop measurements ran 18:36Z to about 20:32Z.

Checkpoint checksums, also in `out-reruns-10m/checkpoints.sha256-md5.txt`
(the files themselves are in the main checkout's `artifacts/`, which git does
not track):

- arm T: md5 `c9f2684070a67920577b26f2f1662ffd`
- arm C: md5 `13158e142560a18a9ff4c7ea2cacd37c`
- arm M: md5 `c4701f70e7967e008954640c88e89112`

## Money

- **Rate:** the vendor's creation record said **$1.19 an hour** for all
  three machines, not the $0.99 of record. The alarm and the machine deadline
  both used $1.19, as the code is written to (the deadline came sooner: 50
  minutes rather than 61).
- **By the vendor's own bills (the authoritative figure):** 1.0951 billed hours at $1.19 = **$1.3032** (M $0.5045, T $0.3980, C $0.4007).
- **By arithmetic from the recorded lifetimes:** 1.095 machine-hours at
  $1.19 = **$1.3029** (M $0.5043, T $0.3980, C $0.4007).
- **By the vendor balance:** $71.2191 at 17:56Z before anything was created,
  $69.8935 at 19:20Z and 19:25Z with no machines, a fall of **$1.3256**. About
  $0.015 of that is the network volume's storage over the 1.5 hours ($0.01 an
  hour), which leaves about $1.31 for the machines.
- **Exact spend by source:** **$1.3032 of rented machine time, from the first release's development line, on the rented-machine account; nothing from any other source.** The network volume's storage, about $0.01 an hour, is a standing charge that runs whether or not anything is launched, and is not counted to this wave.
- **Against the approval:** about $1.30 to $1.31 against "about $1.14", which
  is 1.14 to 1.15 times the approved figure. Nearly all of the gap is the
  higher hourly rate: at $0.99 the same lifetimes would have cost $1.08.
  This is under the alarm's 1.25 line, and the alarm compares against the
  posted rate, which is what it is built to do.
- **Source:** the first release's development line, which had $8.53 left
  and now has about $7.23. Programme total about $230.94 of $450.
- **No top-up** of any account before, during or after the wave.

## The spending alarm

- A fresh wave name, `rerun-10m-2026-10-09`, used for the first time.
- The watcher read every 5 minutes from 18:10Z until 19:25Z (30 minutes after
  the last deletion) and stopped by itself. Ratio B, the fast comparison of
  money drawn against what the posted rate predicts, rose from 0.62 to 1.007
  and never reached the 1.25 line. There was no trip and there is no halt file.
- Every deletion was written into the alarm's records by the watchdog at the
  moment it was accepted, and each laptop deadline timer stood down only on a
  confirmed deletion, two of them on the watchdog's record and one on the
  vendor's "not found". This is the first time the fixed alarm has met real
  billing, and every one of its four ruled fixes behaved as written.
- The end-of-wave comparison of billed hours against machine lifetimes
  (`tripwire.py reconcile`) was run no earlier than three hours after the last
  deletion, as the operator rule says. Run at 21:55Z, 3 hours 1 minute after the last deletion. Its result: **ratio A, billed hours against machine lifetime, 1.000 on every machine** (M 0.4239 h billed against 0.4237 h of life; T 0.3345 against 0.3344; C 0.3367 against 0.3367). Every bill had posted in full, so nothing counted as "cannot be checked yet". **No trip, no halt.** Billed: 1.0951 h at $1.19 = **$1.3032**, which agrees with the arithmetic.

## Raw figures the registered procedure printed

These are copied from `out-reruns-10m/` (`stdout_*.txt`, `row_*_seed0.json`,
`table.md`, `summary.json`). They are not read against the bar here.

| Arm | Gate on learning, this seed (own, named-other, of 3,000; bar 790) | In-use check part A: weight on the true agent (bar 0.9) | In-use check part B: route use (bar 0.5) | In-use check as the code records it | What the procedure printed for the seed |
|---|---|---|---|---|---|
| T | 2,959 and 2,980; seed passes | 0.999 | slot 0.986 | passed | reading 0.0000 (states (0,) at the action position, 8 directions, 180 of 180) |
| C | 3,000 and 3,000; seed passes | 0.999 | stirred-in route 0.000 | failed | no verdict: "the built ownership route has gone flat (construction did not hold): the stirred-in route is not in use: route use 0.000, bar 0.5" |
| M | 2,577 and 1,733; seed passes | 0.999 | stirred-in items 0.024; separable items 0.000 | failed | no verdict: the same reason for both routes (route use 0.024 and 0.000, bar 0.5) |

The summary prints "gate not decidable on one seed" for all three arms, as
the ruled reporting change requires with one seed, and "outcome: not
computed: arm F has no records". In every row the sharpness is 4.0 and not
learned. Arm T's row-choice split, reported beside its gate: right row of
episodes 2,934 of 3,000; right where the row was wrong 25 of 66; right with
the row forced 3,000.

## Anything odd

1. **The higher rate**, above. $1.19 rather than $0.99 an hour, which is
   why the spend is about 15 per cent above the approved figure.
2. **No stock at first.** The first arm M launch and two of its retries, then
   one arm T and two arm C attempts, were refused by the vendor ("no longer
   any instances available"). Nothing was created by a refused attempt, and the
   vendor's machine list stayed empty. A small wrapper outside the repository
   re-ran the unchanged launcher every 5 minutes, only while the vendor gave
   that answer. Each attempt ran all of the launcher's pre-flight checks again.
3. **Arm M's separable route reads 0.000.** On the toy models arm M's
   separable half lost 100 per cent (route use 1.000), and arm T's slot reads
   0.986 here. This is a raw figure, written down so that the item 9 reader
   sees it. Nothing has been made of it.
4. **The alarm's first reading** showed ratio B 4.135 over a span of seconds
   with a predicted spend far below the rule's $0.25 floor, so it was not a
   comparison and was not treated as one. Later readings settled near 1.0.

## Where the outputs are

- `experiments/08-successor-degree/out-reruns-10m/`: the three rows, the
  reads, the procedure's printed output per arm, the summary, the table, the
  checksums, and under `runs/` each run's training log, trajectory, finished-marker,
  watchdog log, machine shutdown log, deadline-timer log and deletion record.
- `out-reruns-10m/tripwire-records/`: the alarm's state file and its log
  for this wave, including the reconcile output.
- The compute ledger rows: `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`,
  the three 2026-10-09 rows, now with their actual costs.
