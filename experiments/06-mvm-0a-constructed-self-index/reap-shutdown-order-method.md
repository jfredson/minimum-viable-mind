# Method: fixing the shutdown order, so a finished run cannot delete its own machine before the files are home

*Written and committed BEFORE the code, per this programme's standing
discipline. Nothing in this note is a ruling. It is an engineering
proposal with one policy question and one provenance question marked for
John at the end.*

Date: 2026-09-21. Repo: `minimum-viable-mind`, experiment 06.

---

## 1. What went wrong, in plain words

A training run rents a machine by the hour. Two separate pieces of
machinery are supposed to shut that machine down when the work is
finished, and on 2026-09-19 they cancelled each other out.

- The **trainer** finishes, writes the model file and a small
  finished-marker file next to it, and then asks the rented machine to
  delete itself. This is in `src/train_a3.py`, function `self_terminate`.
- The **laptop watcher** (`src/watch_run_a3.sh`) wakes about every ten
  minutes, copies files down, and — when it sees the finished-marker —
  does the *last* copy of everything, checks the copy against the
  original, and then deletes the machine.

The trainer asks for deletion within a fraction of a second of writing
the finished-marker. The laptop watcher can only notice the marker on its
next wake-up, up to ten minutes later. So by the time the laptop looks,
the machine is gone, and with it the only way to reach the last version
of the model file.

This is not a near-miss that happened to go badly once. The gap the
laptop has to hit is about a second wide inside a ten-minute cycle, and
it does not get to try again. **On a run that finishes normally, the
laptop's final copy essentially never happens.** The ledger's row for
2026-09-20 calls it a process defect and not bad luck, and that is right.

### The evidence, from the run's own log

From `artifacts/a3ctl_30m_seed0/watchdog.log`:

```
[2026-09-20T06:11:12Z] poll 57: {'step': 54500, ...}
[2026-09-20T06:21:13Z] pod no longer exists (self-terminated on completion, external kill, or crash).
[2026-09-20T06:21:13Z] if the network volume was attached, artifacts survive on it —
[2026-09-20T06:21:13Z] attach it to a throwaway CPU pod to recover; nothing more to do here.
```

Two things are worth correcting against the ledger's summary, which said
the log "simply stops":

1. The laptop watcher did **not** hang or stop. It noticed on the very
   next wake-up that the machine was gone and exited cleanly.
2. It exited down a branch that gives up by design. "Nothing more to do
   here" is the code telling a human to go rent another machine. That
   branch is the manual recovery operation — it cost $0.067 and a
   separate authorisation from John on 2026-09-20.

So the defect is not only the timing. It is that **the give-up branch is
a normal outcome**, reached on every healthy run, and it converts
pre-authorised spending into a manual errand.

The last automatic copy of the model file had happened at 05:40Z, at
step 51,500 of 55,116 — 93.4% of the budget. Full-budget copies come down
only every sixth wake-up (about hourly), so a run that finishes normally
is expected to leave the last hour of training unreachable.

## 2. Why neither piece can simply be deleted

Both earned their place, and the ledger records what each one cost to
learn.

**The trainer's self-delete** exists because waiting on a laptop cost
about $9.50 across three occasions (about $5.70 in wave 2, about $3.80 on
the A3 pilot, plus a fourth occurrence; about $10.30 across four in
total). The laptop stays awake only because `caffeinate` blocks the
idle-sleep timer — it does not block the lid. A closed lid meant the
machine billed for hours after the work was done. Self-delete fixed
exactly that, and it worked: the 2026-09-19 run is **the first in the
programme's history with zero idle billing**.

**The laptop's final copy** exists because a run whose model file is
never copied down is a run that cost money and produced nothing. That is
how $97.04 was lost on 2026-08-12.

Any fix that drops either one re-opens a hole that has already been paid
for.

## 3. The ordering rule the fix has to establish

Stated as a rule the code can be checked against:

> **The rented machine may not be deleted until either (a) the laptop has
> the finished model file locally and has checked it against the copy on
> the machine, or (b) a bounded waiting time has passed AND the file is
> known to be sitting on the network storage volume, which outlives the
> machine.**

Clause (a) is what stops silent loss. Clause (b) is what stops open-ended
billing. Today's code has neither: the trainer deletes on its own
judgement, and the laptop's check never runs.

## 4. Options considered

**Option A — the machine waits for a receipt. CHOSEN.**
After the laptop finishes its last copy and checks it, it writes a small
receipt file back onto the machine. A small script running on the machine
watches for the finished-marker; when it appears, it waits for the
receipt, and deletes the machine the moment the receipt arrives — or when
a bounded wait runs out, but only if the files are on the network volume.

Why this one: it is the only option that makes the two mechanisms
*compose* instead of compete. If the laptop is asleep, the bounded wait
still ends the billing. If the on-machine script dies, the laptop sees
the finished-marker exactly as it did before self-delete existed, and
does its own copy and delete. Each one failing leaves the other's
guarantee standing, which is the precise opposite of today, where each
one *succeeding* destroys the other's.

Cost of the wait, measured from the existing logs rather than guessed: a
full copy of the run directory took 2 minutes 19 seconds on 2026-09-19
(336MB). With a cheap one-minute check for the finished-marker (see
Option C below, adopted as a component), the expected extra machine life
after training ends is about five minutes — roughly $0.08 at $0.99/hour,
about $0.75 across nine runs. The worst case, laptop asleep, is the
bounded wait itself: 30 minutes, about $0.50 per run. Compare that with
the 3.9 and 5.8 hours the old failure actually billed.

**Option B — the machine pushes the files somewhere before deleting
itself. REJECTED as the primary fix.**
The laptop cannot be pushed to: it is behind a home router with no
address the machine can reach. Pushing to cloud storage instead means a
new vendor, a new credential placed on a rented machine, and a new set of
failure modes — and credential placement on rented machines is a decision
John has ruled on twice already and reserved to himself. It also does not
actually satisfy the rule in §3: "uploaded somewhere" is not "the laptop
has it and has checked it". Part of the idea is already in place and kept:
the trainer refuses to delete unless the file is on the network volume.

**Option C — poll faster. REJECTED as a fix, ADOPTED as a component.**
Shortening the wake-up cycle shrinks the window but cannot close it: the
trainer deletes within about a second of writing the marker, so even a
five-second cycle loses most of the time, while making the laptop hold an
ssh session open all night for ten hours. Probability is not a guarantee
and §3 asks for a guarantee. What it *is* good for is shrinking how long
the machine has to wait in Option A. So the fix separates the two things
the cycle currently does: a cheap "is it finished yet" check every minute,
and the expensive file copying on the existing ten-minute and hourly
cadences.

**Option D — treat the network volume as the real home, and make fetching
a separate step. REJECTED as the primary fix.**
This is essentially today's recovery, promoted to routine: after each run,
rent a cheap machine, mount the volume, copy the file down. It is cheap
($0.067 measured) and it works. But every rented machine needs John's go
under the standing rule, so nine runs become nine authorisations and nine
errands — exactly the burden this task exists to remove. It also leaves a
window where the only copy of a ten-hour run sits on a single volume, and
the ledger records a volume being deleted by hand on 2026-09-19. One copy
in one place is not a resting state this programme should design towards.
Kept as the documented fallback when the receipt never arrives.

**Option E — treat a vanished machine as a completion to be reconciled.
ADOPTED as a component, insufficient alone.**
On its own this is only a better error message, since reconciling against
the volume still needs a newly rented machine. As a component it matters:
the give-up branch should leave a loud, machine-readable "this run needs
recovery" file naming the volume, the run and the exact command, instead
of three lines at the end of a log. And it should first confirm that the
machine is really gone rather than believing a single failed API call.

**Option F — have the laptop do the deleting only, and strip self-delete
entirely. REJECTED.**
This is the world before 2026-09-16, which cost about $10.30 in idle
billing across four occurrences. The lid problem is unchanged.

## 5. The design

Three moving parts. Two are new files; one is an edit to an existing
unregistered operations script.

### 5.1 `src/reap_agent.sh` (new) — the machine's own shutdown watcher

Runs detached on the rented machine, installed by the launcher. One loop:

1. If the deadline (+24h) has passed, delete the machine. This replaces
   the bare `sleep 24h; runpodctl remove pod` line the launcher runs
   today, and covers the case nothing else covers: a run that hangs and
   never writes a finished-marker.
2. If the finished-marker exists:
   - **Safety gate, copied from the trainer's `self_terminate`:** refuse
     to delete unless the model file exists and sits under `/workspace/`,
     the network volume. Deleting a machine whose only copy is on its own
     disk is how the 2026-08-12 run was lost.
   - Wait for the receipt file. On seeing it, delete immediately.
   - If the bounded wait runs out first: delete **only if** the model file
     is on the network volume. Log loudly that the local copy may be short
     of the final step and that recovery from the volume is needed.
   - If there is no network volume (`NETVOL=none`), never delete on the
     wait running out — wait for the receipt until the deadline. Losing
     the machine would lose the run.

### 5.2 `src/watch_run_a3.sh` (edited) — four further fixes

This file is not registered text. It is the operations split made on
2026-09-16 and its own header is already a changelog of numbered fixes;
adding fixes 3 to 6 to it continues that. The alternative, a second copy,
would mean two watchdogs that differ and a launcher that picks — a worse
hazard than the edit. The edits are backward-compatible with the
registered launcher `launch_a3.sh`, which spawns this file unchanged:
writing a receipt onto a machine that has no shutdown watcher is harmless,
and the improved give-up branch helps that path too. *(Flagged for John at
§8 as a judgement call he can reverse.)*

- **Fix 3 — write the receipt.** After the final copy is checked against
  the machine, write the receipt file back onto the machine, then delete
  the machine as before. The delete stays, so the laptop remains a real
  reaper when the on-machine watcher is not armed.
- **Fix 4 — never delete on an unchecked copy.** Today the code runs
  `fetch_final; kill_pod` in sequence and deletes the machine even when it
  has just printed "FINAL CHECKPOINT UNVERIFIED". The final copy now
  retries, and the machine is deleted on completion only after the copy
  checks out. Refusing to delete is safe here *only because* the
  on-machine deadline watcher is the spending backstop; that dependency is
  stated in the code.
- **Fix 5 — the give-up branch stops giving up quietly.** Confirm the
  machine is really gone over several checks rather than one (a single
  failed API call currently looks identical to a deleted machine, which
  would abandon a *live, billing* machine — a hazard in the present code
  in the other direction). Then, if what is already local matches the
  finished-marker's step, declare the run complete. Otherwise write a
  `NEEDS-RECOVERY.txt` beside the artifacts naming the volume, the run,
  the last local step and the exact recovery command.
- **Fix 6 — split the cheap check from the expensive copy.** A
  one-minute check for the finished-marker and the machine's continued
  existence; file copying stays on its existing ten-minute and hourly
  cadences. This is what makes the bounded wait in §5.1 short.

### 5.3 `src/launch_a3_fetch_first.sh` (new) — the launcher

**`src/launch_a3.sh` is registered text** — Amendment A3's "What is
registered" section names it, along with the grammar, the tokenizer, the
trainer `src/train_a3.py`, the frozen batteries and the gates. It is not
edited here. The repo's own precedent when a launcher needed changing was
to split a new unregistered file, which is why `launch_ctl_pilot.sh`
exists and says so in its header, and why `launch_a3.sh` was itself split
from `launch_pilot_a1.sh`. That precedent is followed again, and the new
file is derived from `launch_a3.sh` verbatim with the differences listed
in its header.

The trainer is registered too, so **`train_a3.py` is not edited either**.
It does not need to be: it already carries a `--no-self-terminate` switch.
Passing an existing switch is not changing registered text, and it puts
the shutdown policy where it belongs — in the operations scripts, not in
the scientific instrument.

What the new launcher does differently:

- installs `reap_agent.sh` on the machine and **checks it is actually
  running** before training starts;
- passes `--no-self-terminate` to the trainer **only when that check
  passed**, so the machine's shutdown decision moves to the agent;
- if the agent could not be armed, falls back to today's behaviour —
  trainer self-deletes — and says so loudly, because unbounded idle
  billing is the worse of the two failures (see §8, question 1);
- drops the bare `sleep 24h` deadline line, which the agent now covers.

## 6. Failure modes, and what each costs after the fix

| what fails | before | after |
|---|---|---|
| run finishes normally, laptop awake | machine deleted before the final copy; manual recovery each time | laptop copies and checks, writes the receipt, machine goes; about 5 extra minutes of billing |
| run finishes, laptop asleep or lid shut | same manual recovery | bounded wait ends billing (about 30 min, ~$0.50); files safe on the volume; a loud recovery file is written |
| on-machine watcher fails to start | n/a | launcher says so and leaves self-delete on — today's behaviour, no worse |
| on-machine watcher dies mid-run | n/a | laptop sees the finished-marker, copies, checks, deletes — the pre-2026-09-16 behaviour |
| laptop watcher dies mid-run | machine billed until the +24h stop | bounded wait ends billing shortly after the run finishes |
| run hangs, never finishes | covered only by the +24h line | same +24h stop, now inside a loop that also logs |
| network link between the two breaks | machine billed until +24h | bounded wait ends billing; recovery file written locally |
| API call fails once and looks like "machine gone" | laptop exits, live machine keeps billing | confirmed over several checks before believing it |
| final copy is corrupt or short | machine deleted anyway | machine kept, copy retried, no receipt written |

## 7. How this is verified without spending anything

No machine is rented and no vendor is contacted. Verification is a
self-test, `src/reap_handshake_selftest.sh`, that stands up a fake rented
machine as a local directory, a fake `runpodctl` that records deletions
with timestamps, and a fake remote-shell command that runs against the
local directory. It then runs the real `watch_run_a3.sh` and the real
`reap_agent.sh` against it, with the timings compressed to seconds, and
asserts:

1. **Normal completion:** the local model file matches the one on the
   "machine" by checksum, exactly one deletion happened, and the deletion
   happened *after* the receipt was written. This is the property the
   whole fix exists for.
2. **Laptop asleep:** with no laptop watcher running at all, the machine
   deletes itself when the bounded wait runs out, and not before.
3. **Files not on the volume:** the agent refuses to delete when the wait
   runs out, because the machine's disk is the only copy.
4. **Corrupt final copy:** no receipt is written and the machine is not
   deleted.
5. **Machine vanishes mid-run:** the laptop writes the recovery file
   naming volume, run and command, rather than shrugging.
6. **One failed API call:** does not convince the laptop the machine is
   gone.

Plus: `bash -n` on every script, a dry run of the new launcher (which
creates nothing), and the existing module self-tests.

## 8. For John — not decided here

1. **Policy question: what should happen when the on-machine watcher
   cannot be armed?** The proposal falls back to the trainer deleting
   itself — spending stays bounded, and a normal finish then costs one
   manual recovery, as it does today. The alternative is to leave
   self-delete off and accept that a shut lid can bill overnight. The
   proposal chose the money-safe side; the choice is yours, and it is one
   variable at the top of the launcher.
2. **Provenance question: which launcher may produce the nine registered
   runs?** `launch_a3.sh` is named in the registration as the registered
   instrument. The fix cannot be applied through it without editing
   registered text, so it lives in a derived unregistered file. Either
   that derived file is ruled into the register for the successor runs, or
   the one-line change (passing `--no-self-terminate` and installing the
   agent) is ruled into `launch_a3.sh` directly. Someone has to choose;
   it is not mine to choose.
3. **The edit to `watch_run_a3.sh` is in place rather than a new split.**
   Reasoning in §5.2. It is unregistered operations code and no result's
   provenance turns on it, but say the word and it becomes a seventh file.
4. **The bounded wait is 30 minutes by default.** That is a spending
   choice — about $0.50 of worst-case idle per run — not a technical one.

---

## 9. Appendix: what actually happened when it was built

*Added after the code landed. The note above is unchanged; this records
where building it differed from planning it, which is the only honest way
to keep a method file that was committed first.*

**A negative control was added to the self-test, and it matters more than
the rest.** §7 listed six things to assert, all of which assert the fix
working. A test that can only pass proves nothing, so the suite gained a
case 0: it reproduces the old order exactly — save the model file, write
the finished-marker, ask the machine to delete itself, with nothing in
between — and *expects the rule to be broken*. It is. The deletion is
recorded with no receipt and a stale local copy, and the laptop is left
without the final file. If case 0 ever reports the rule holding, the
harness has stopped measuring what it claims to.

**Four timing knobs were added to the laptop watcher** so the whole
sequence runs in seconds instead of hours: the gap between "the machine
did not answer" checks, the wait between final-copy attempts, the settle
time after a delete, and the existing wake-up cycle. They change nothing
at their defaults; they exist so the self-test needs no vendor.

**The derived launcher is produced by a script, not by hand.**
`src/derive_fetch_first_launcher.py` reads the registered launcher, applies
nine named replacements, and asserts each one matched exactly once. That
makes "derived verbatim" a checkable claim rather than a promise: re-run it
and compare. It never writes to the registered file.

**One bug found and fixed in the test harness itself**, worth recording
because it is the kind that hides: stopping a background job with an unset
process number falls through to `kill 0`, which signals the whole process
group and kills the test script. It surfaced as one case simply hanging.

**Result: 26 checks, no failures**, plus a clean dry run of the new
launcher that created nothing, and the three module self-tests passing
unchanged. No machine was rented; no vendor was contacted; nothing was
spent.

---

## 10. Two recommendations about the nine runs

*Added after checking what the nine runs actually are. The December-result
roadmap (`docs/december-result-roadmap-2026-09-20.md`, week 43) schedules
three arms times three seeds at 30M, about $110, and they belong to a
**successor design that has not been registered yet** — proposal v1 goes to
its review gate in week 40.*

**1. The provenance question in §8 mostly dissolves.** Those nine runs are
not A3 runs, so they will not be produced by `launch_a3.sh` whatever
happens here. The clean move is to fold this fix into the successor's
registration: name a launcher that already waits for the receipt, and make
"the trainer does not delete its own machine" part of the registered
recipe rather than an operations afterthought. Then the nine runs are
produced by registered text that has the fix, and nothing is derived.
What is left of §8's question is narrower and less urgent: whether any
*further A3* run may use the derived launcher.

**2. There is already a scheduled, already-budgeted place to test this
against the real vendor.** Week 40's measurement rehearsal is tiny models
at about $0 to $10. A toy run that finishes in minutes exercises the whole
shutdown path for real — the credential on the machine, the agent starting,
the finished-marker, the receipt, the deletion — for a few cents, weeks
before $110 of real runs depend on it. Everything in §7 is a self-test
against fakes; it proves the ordering logic and it cannot prove that
`runpodctl` on the vendor's image behaves as the launcher's comments say it
does. That is the one thing still worth buying, and it is already paid for.

**What to look for when it does run for real.** Three lines, in this order:
`receipt written on the machine` in the laptop's log, `receipt found` in the
machine's own log, and a deletion within seconds of it. If instead the
machine's log says `grace ran out`, the receipt path did not work and the
run should be treated as unattended-unsafe until it is understood.
