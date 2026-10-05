# Check of the four 10-million development runs: method, committed before any output

*Written 2026-10-04 (Pacific; 2026-10-05 about 01:00Z) by a Claude Code
checking session, on branch `check-dev-10m`, cut from the main line at
`53ae82c` (pull request 97 merged). **Committed and pushed before anything
below is run.** The findings, with the commands and what they printed, are a
later commit. Laptop only. Nothing is rented, nothing is created, nothing is
spent: $0. Vendor contact is limited to reading: the machine list, the
balance and the billing rows.*

*Written under the workspace plain-language rule. The four runs are a
pipeline and speed check, not a verdict on learning (version 4 of the
proposal, section 11, step 4). No figure here is read as a result about the
scientific question.*

**The pairing rule.** This session did not write the successor code (pull
request 97), did not launch the runs, and did not write the ledger rows (pull
request 98, branch `dev-10m-actuals`). This is the check that version 4's
plan and the go packet (`docs/rulings/2026-10-04-development-runs-go-PROPOSAL.md`,
section 5) say a session that did not write the code owes.

## 1. What this session has already seen, said before it runs anything

A prediction of a figure already seen is not a prediction, so this is what
has been seen, all of it by reading files.

- **Every run's training log and trajectory log**, in the main checkout under
  `experiments/08-successor-degree/artifacts/succ_{m,t,c,f}_10m_seed0/`. All
  four end with `TRAINING COMPLETE` and a finished-marker at step 108,919. The
  trajectory figures (a 400-episode watch set, never a registered figure) end
  at: arm M 0.8975 own / 0.6275 other; arm T 0.8925 / 0.9625; arm C 0.595 /
  0.5625; arm F 0.5975 / 0.3225. Seconds per step: T 0.0099, C 0.0100, F
  0.0093, M 0.0145.
- **Arm T's course**: own and other both 1.0 from step 2,000 to 14,000 with
  training loss printed as 0.0; own 0.77 at step 16,000, 0.585 at 20,000, and
  back up to about 0.89 by the end; other stays at 1.0 until about step
  50,000, then drifts down to about 0.96.
- **The laptop watchdog logs**: for each run, in this order, "final fetch OK",
  "final checkpoint VERIFIED (md5 ...)", "receipt written", "deleting pod",
  "pod gone". The machine's own reaper log ends at "waiting for the receipt".
  This session computed the md5 of each local checkpoint and it begins with
  the 12 characters each watchdog printed.
- **The tripwire state** (`artifacts/tripwire/dev-10m/state.json`) and its
  log: four machines registered, no deletion time on any (`gone` empty), five
  balance readings from $73.7742 to $73.6141 between 00:11Z and 00:20Z, one
  watcher line ("ratio B 0.000"). The watcher process (pid 30285, started with
  `--allow-delete`) was still running at 00:52Z, and its next reading is due
  about 01:11Z. A copy of the state as it stood at 00:52Z is kept by this
  session before that reading changes it.
- **Pull request 98's description and ledger annotation**, which say: the
  tripwire took one reading and never worked out a ratio; its state has no
  deletion times; the four laptop deadline processes were stopped by hand.
- **The toy record for arm T**: `out-repairs/gate_base.json` in the rehearsal
  folder, 1.0 own and 1.0 other on all three seeds, after 2,500 steps of
  batch 256 (`out-repairs/train_T_base_seed*.json`). The 10-million run took
  108,919 steps of batch 96, about 16 times the episodes and 44 times the
  steps.

## 2. The four purposes, and what will count as "holds"

Taken from the go packet, section 1. For each, the test is fixed here.

1. **The frozen trainer runs end to end on a rented machine for every arm,
   arm M for the first time.** Holds for an arm if: its log has the recipe
   the packet names (108,919 steps, batch 96, the token budget), every
   evaluation line to step 108,919, no skipped training batches, the
   finished-marker and `TRAINING COMPLETE`; and its checkpoint loads strictly
   into the frozen model code on the laptop and records step 108,919. Arm M's
   is the one that matters most.
2. **The shutdown order (copy, check, receipt, delete) works.** Holds for a
   run if its watchdog log shows the four steps in that order with nothing
   between them failing, the local checkpoint's md5 matches the verified one,
   and the vendor's machine list (read now) holds none of the four machines.
3. **The spending tripwire meets real billing.** Holds only if, while machines
   were running, the tripwire computed at least one billing ratio over a span
   long enough for its own rules to act on it (the watcher acts only on a
   ratio over 0.9 hours or more; preflight on 0.5 hours or more). Anything
   less is "does not hold", whatever the money turned out to be. Separately,
   and not counted as the tripwire holding: this session works out both
   ratios after the fact from the vendor's own figures, by running
   `tripwire.py reconcile` on a **copy** of the state in this session's
   scratch folder, with each machine's deletion time filled in from its
   watchdog log ("pod gone"). The artifact folder is not written to.
4. **The time per step is measured on the card.** Holds if every arm's log
   carries seconds per step from the card for the whole run. Reported: the
   figures against the packet's estimate (about 0.017 seconds), and arm M's
   slower rate examined (section 3, item 3).

## 3. What is run, in order

All with the repository's environment (`~/Code/minimum-viable-mind/.venv`),
on the processor, from this worktree's copy of the frozen code, which is
identical to the code the runs were trained with (pull request 97's merge,
`53ae82c`). Checkpoints are read where they are, in the main checkout, and
never copied into git.

1. **The laptop procedure, at the registered counts** (episode scale 1.0, 200
   null shuffles), one model per command, arm T first because the other arms'
   rider reads arm T's site set from the same folder:

       python src/procedure.py model --ckpt <main checkout>/experiments/08-successor-degree/artifacts/succ_t_10m_seed0/succ_t_10m_seed0.pt --seed 0 --out out-dev-10m-check
       (then C, M, F the same way)
       python src/procedure.py summarise --dir out-dev-10m-check

   Output goes to `experiments/08-successor-degree/out-dev-10m-check/` and is
   committed. If one model takes longer than about 90 minutes, the others are
   run as separate commands (they are already one per command); a model that
   cannot finish in one sitting is reported as such rather than cut short
   silently. **Nothing is read from these figures about learning or about the
   question.** What is reported: that the procedure runs end to end on real
   10-million checkpoints, the gate counts, whether a site set was nominated,
   and arm T's figures for section 4 below.
2. **Read-only vendor reads**: the machine list, the balance, and the billing
   rows for the four machines (through `tripwire.py reconcile` on the copied
   state, as section 2 item 3 says).
3. **Arm M's speed.** A count of the operations one training step performs
   for each arm at 10 million (forward and backward, on the processor, a few
   steps, by the profiler), to see whether arm M's 1.5 times slower step on
   the card is explained by doing more, smaller operations. At this size a
   card is held up by the number of operations more than their size, so a
   ratio of operation counts near 1.5 would explain it; a ratio near 1 would
   point to the machine instead. Either way this is ARGUED, not a measurement
   on the card.
4. **Arm T's own-directed accuracy.** On the final arm T checkpoint, on the
   gate's held-out episodes: split arm T's own-directed errors by where they
   come from. Arm T answers by (a) selecting a row of its table with the
   ownership answer, and (b) reading that row and applying the rule. The
   named-other actions use a fixed selection, so they test (b) alone. The
   script records, for own-directed actions, whether the selection's highest
   weight falls on the right agent, and the accuracy among actions where it
   does and where it does not. It also prints the learned sharpness of the
   ownership answer and the size of the selection's weights. **Expected,
   stated before running:** the own-directed errors sit mostly where the
   selection picks the wrong agent or spreads its weight, since other-directed
   accuracy stayed high while own-directed fell. If instead the selection is
   right and the action still wrong, the fault is in the table or the rule.
   One possible cause, to be named and not tested here: once the loss reached
   zero (steps 4,000 to 14,000) the only force left on the weights was weight
   decay, which shrinks the selection's sharpness until it starts to err; the
   toy never sat at zero loss for long. Testing that would need training,
   which this check does not do.

## 4. Arm T against the toy and against version 4, section 5.1

Version 4 section 5.1 says arm T's degree is zero by construction: the
ownership answer sits in one separate slot, and the action is a lookup with
it. The question for this check is whether what happened at 10 million
threatens that, or the registered runs. It is answered from: the procedure's
reading on arm T (does it still read 0.0000, with its controls holding and its
gate cleared), the split in section 3 item 4, and the toy's 1.0 / 1.0. A
construction that holds but trains less cleanly than the toy is a training
matter; a reading that is no longer 0, or a gate that fails, would be a
threat to the anchor and goes to John before the registration text.

## 5. What the check will say about changes before the registered runs

At least: whether the tripwire needs to read more often than hourly, or at
fixed short intervals during a wave, to meet its purpose on runs this short;
whether the watcher must record deletion times as they happen (from the
watchdog's "pod gone") rather than at its next reading; whether the laptop
deadline processes must stop themselves when their machine is gone; and
anything the procedure run or arm T's figures add.
