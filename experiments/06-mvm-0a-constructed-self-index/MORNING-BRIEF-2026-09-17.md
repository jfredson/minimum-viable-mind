# Morning brief — 2026-09-17

*Written 2026-09-16 22:50 local, at the end of the night's session. Read
this first. Everything is committed and pushed; nothing is uncommitted
anywhere.*

## Do this before anything else

**1. Were the pods reaped?**

```
runpodctl get pod
```

Expect **zero pods**. If any remain, they are billing at about $1/hr each
and should be removed once their checkpoint is confirmed local:

```
runpodctl remove pod <id>
```

**2. Did the checkpoints land, and are they intact?**

```
ls -l ~/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/artifacts/a3_30m_seed{1,2}/*.pt
tail -3  ~/Code/minimum-viable-mind/experiments/06-mvm-0a-constructed-self-index/artifacts/a3_30m_seed{1,2}/watchdog.log
```

A finished run is about 351MB. The watchdog verifies by checksum against
the pod before deleting it, and the log records both.

**3. Revert the sleep setting**, once both have reported:

```
sudo pmset -a disablesleep 0
```

## If the machine was rebooted for the OS update

The two watchdogs die on reboot and **they are the only reap** — the pods
carry no credential, no identifier and no reaper of their own, verified
(`reaping-audit-2026-09-16.md`). If the reboot happened before about
06:00, restart them; the restart commands are in `STATUS.md` and the
script is a plain polling loop, safe to restart.

If the reboot happened after both reported, nothing is needed.

Closing the Claude session alone is harmless: both watchdogs run detached
with parent process 1 and survive it.

## Where the work stands

Training was due to finish around **06:10 local**, roughly ten hours from
a 20:13 start at about 0.65 seconds a step for 585.5M tokens.

Last night was almost entirely instrument audit, run on John's rulings,
all local and free. A3 spend is unchanged at **$14.21 of the $100 stop**,
plus the in-flight wave estimated at $18–26.

**What was established, in order:**

1. The **blind-localization arm** returned NOT FLAGGED, sub-bin
   *instrument failure to locate*. Verdict and name stand as committed,
   with a dated annotation: *superseded in interpretation — no valid
   target.*
2. The **A2 register is a constant** in every trained checkpoint. Its
   writer emits the same vector from the first write. An untrained model
   does not, so it is trained in. Consequence: the full model is the twin
   plus a bias, so wave 2 was a **seed lottery in one architecture**, not
   a prediction inverting. Ledger and notes annotated, never edited.
3. **Amendment A3 §1's** self-reference reading is withdrawn. A constant
   is neither self-reference nor self-location. A3's design and pilot
   result do not depend on it. No registered text changed.
4. The **positive control** is NOT TESTABLE, the literal pre-stated
   verdict, which John ruled authoritative. Its probes all fell below
   their nulls, and its ablation effect is inside evaluation noise.
5. The **known-answer test PASSES at ceiling**, so the pipeline plumbing
   is sound. It does not exercise the ablation path.

**Two defects in criteria I wrote were found and reported, not repaired:**
a zero-spread null, and an absolute value where the question was
degradation.

## Open decisions waiting on John

- Which reading of the positive control governs future runs. The literal
  one governs this run, already ruled.
- The launcher's pod-side verification uses a command form the pod's
  runpodctl does not have, so it can never verify. One-line fix proposed,
  **not applied**.
- Quote the ownership spread wherever **0.506** appears. It and the 0.440
  come from one evaluation seed; twelve draws put the typical value nearer
  **0.566**, with a standard deviation of 0.0284 at n=400.
- Extra A3 seeds (due 2026-09-20) and the control-battery question, A4 or
  close A3 (due 2026-10-04).

## Standing constraints

No registered text changes without John. He authorises every run and his
go is quoted verbatim in the ledger. The $100 A3 hard stop is unchanged.
Annotate, never rewrite. An L1 localization read is gated on the
known-answer test, which now passes, but gate lifted is permission and
not instruction — **no L1 read has been run on any seed.**
