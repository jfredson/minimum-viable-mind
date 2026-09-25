# Method: one launch gate on every launcher that can rent a machine

*Written 2026-09-24 (Pacific), before any code, for the open roadmap step "make
the launcher refuse to rent a machine when the laptop can sleep; every launcher
warns, none checks", and for the launch-checklist item in
`docs/weekend-roadmap-2026-09-24.md` (midweek 2026-10-05 to 09: "launch
checklist made a gate the launcher checks (sleep, scheduled fetch and kill,
ledger row before the pod)"). Unregistered operations code. Nothing here
creates a machine, contacts the rental company (RunPod) or spends money.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30). Findings follow in `launcher-sleep-gate-findings.md` beside
this file.*

---

## 1. What is already true, so the task starts from the right place

The task's premise — "every launcher warns, none checks" — was true until
earlier today and is now only mostly true. Pull request 28's commit `aa7b739`
("Refuse to launch when this Mac could fall asleep") and the two repairs after
it (`32472d1`, `5913bfa`) gave **one** launcher a real refusal:
`src/launch_a3_fetch_first.sh`, the unregistered launcher derived from the
registered one. Two checking sessions passed it
(`reviews/2026-09-24-sleep-guard-check-claude-worktree.md`,
`reviews/2026-09-24-sleep-guard-fixes-check-claude-worktree.md`), the second
with "nothing must be fixed first" and a list of follow-ups.

Four files in the repository contain the command that rents a machine,
`runpodctl pod create` (ruling `docs/rulings/2026-09-22-launcher-argument-guard.md`
§5 establishes that nothing else can):

| launcher | registered? | refuses when the Mac can sleep? | watchdog it spawns |
|---|---|---|---|
| `src/launch_a3.sh` | **yes** — Amendment A3's "What is registered" | no, warns only | `watch_run_a3.sh` |
| `src/launch_a3_fetch_first.sh` | no | **yes, since today** | `watch_run_a3.sh` |
| `src/launch_ctl_pilot.sh` | no | no, warns only | `watch_run_a3.sh` |
| `src/launch_pilot_a1.sh` | no | no, warns only | `watch_run.sh` |

(A fifth file, `src/sleep_guard_selftest.sh`, contains the string only in its
comments.) None of the four checks the other two checklist items: that the
laptop's fetch-and-delete is actually set up to happen inside the time the
machine is allowed to live, or that a ledger row with an estimate exists before
the machine does. Ledger rule 2 in `compute-ledger.md` ("Estimate before
spend") has so far been kept by habit.

## 2. What is changed, and what is not

**One shared gate, `src/launch_gate.sh`, called by the three unregistered
launchers at the point where the fetch-first launcher's sleep check sits today**
— after the settings are read, before the dry-run block and long before the
first rental command. The fetch-first launcher's sleep check moves into it with
its behaviour and its messages unchanged, so the two reviews above still
describe it; the other two launchers gain it.

Why one shared file rather than three copies: **the fetch-first launcher's sleep
block is about 140 lines, mostly the reasons for each decision.** Three copies
would drift, and the drift would be in the direction the repo has already paid
for — the argument guard was added to three launchers by hand and the
derivation script that produced one of them no longer reproduces it
(`launch_a3_fetch_first.sh` header, lines 58–64). Confidence: high. Standard
practice. The strongest alternative is copying the block into each launcher so
each file reads alone, which is what the argument guard did; it was rejected
because this block is long and still being repaired, and the argument guard is
five lines and finished.

**`src/launch_a3.sh` is not touched.** It is registered text. §7 below drafts
the amendment that would give it the same gate; it goes to Gate A with the
argument-guard amendment already drafted in `argument-guard-method.md` §6.
Until then the standing prohibition on invoking it with arguments stands, and
nothing here makes it safer to run.

## 3. The gate: three checks, all run, all reported, then one decision

All three checks run every time and every problem found is listed, rather than
the first one stopping the rest. The earlier review's follow-up 4 is the reason:
an operator who fixes the one problem named and re-runs, only to be refused for
a second problem that was already knowable, learns that the gate is a nuisance.

### 3a. This Mac cannot fall asleep for the run window (carried over)

Unchanged from `launch_a3_fetch_first.sh` at `97ee3c9`: the system-wide
never-sleep setting (`SleepDisabled` in `pmset -g`) must be `1`, and the Mac must
be drawing from wall power (`pmset -g batt`). The idle timers are read and
reported and decide nothing. The reasons are in the carried-over comment and
the two reviews, and are not re-argued here.

**Why a running `caffeinate` (the macOS keep-awake command) is not accepted as
an alternative**, although the task offered it as an example: `caffeinate`
holds off idle sleep and not lid-close sleep, and lid-close is the failure that
has cost money — the four idle-billing occurrences totalling about $10.30
(`STATUS.md` top entry, "Keep the lid open"; ledger rows dated 2026-08-17 and
2026-09-15 in `compute-ledger.md` each name a closed lid or a sleeping Mac).
The reviewed design already chose this and the reviewers agreed. Confidence:
high. The alternative — accept `SleepDisabled 1` **or** a live `caffeinate`
holding a system-sleep assertion — would pass a Mac that sleeps the moment its
lid shuts.

**One addition: a charger that is not keeping up.** The earlier review's
follow-up 5, "the largest of them": with the override on and the Mac reporting
wall power while its battery reads `discharging`, the gate passed. The gate's
own reason for requiring wall power — a flat battery ends the watchdog over a
day-long window — applies word for word. The same `pmset -g batt` reading the
gate already takes prints the word on its next line. So: wall power **and** the
battery line not saying `discharging`. Confidence: medium-high that this is the
right reading (a charger too weak for the load is the known cause on laptops;
`AC attached; not charging` is the Mac's battery-health hold and is safe, so it
must not be caught by a looser pattern). The alternative is to leave it as a
follow-up; rejected because it is three lines and the task is precisely this
failure.

The override stays as reviewed: `ALLOW_LAPTOP_SLEEP=1` and no other value.

### 3b. The fetch and the delete are scheduled inside the run window

**What "the run window" means here** (ARGUED; the roadmap does not define it):
the time between the launch and the moment the machine is guaranteed to be
gone. Two things end it. The laptop's watchdog (`watch_run_a3.sh` or
`watch_run.sh`) fetches the files and deletes the machine on the
finished-marker or at `WATCH_H` hours. The machine's own deadline is `TERM_H`
hours — the on-machine shutdown watcher's hard stop for the fetch-first
launcher, the `sleep; remove` line for the control pilot, and the rental
company's advisory `--terminate-after` for all of them.

The gate refuses unless, **before** the machine exists:

1. **The watchdog this launcher will spawn exists and parses** (`bash -n`). It
   is spawned as the launcher's last act, after the machine exists, with
   `nohup … &` and nobody reads its exit status. A missing or broken watchdog
   there is a machine with no scheduled fetch and no scheduled delete, and the
   launcher prints "watchdog spawned" regardless.
2. **The keep-awake command it is spawned under is present.** The same line
   runs the watchdog under `caffeinate`; if the command is missing, `nohup`
   fails and the watchdog never starts. On a Mac this cannot happen in
   practice, so this is cheap belt-and-braces. The command is named by one
   variable, `CAFFEINATE`, used by both the check and the spawn, so the check
   reads what the spawn will run and a test can point it at a missing file.
3. **Both deadlines are whole numbers of hours, at least 1.** They are used in
   shell arithmetic and in `date -v+NH`; a blank or fractional value produces
   a deadline in the past or a malformed terminate-after, and neither is
   checked anywhere today.
4. **The laptop's delete is due no later than the machine's own:
   `WATCH_H ≤ TERM_H`.** This is the shutdown order the reap-race fix
   (pull request 15, `reap-shutdown-order-method.md`) established — the laptop
   takes the last copy, then the machine goes. If the laptop's deadline falls
   after the machine's, a run that hangs is deleted by the machine before the
   laptop's final fetch, which is the 2026-09-19 failure by another route. The
   defaults are 24 and 24.

Confidence: medium. Items 1–3 are standard and uncontroversial. Item 4 is a
judgment call. The strongest alternative is a ceiling on `WATCH_H` measured
against the run's estimated hours, so the gate bounds idle billing and not
just its order; rejected for now because the ledger's hours column is free
prose (`compute-ledger.md` rows 2026-08-07 to 2026-09-21 read "1–2.5 → 2.4",
"est 11–16 → **29.5**", "≤15 min, hard cap" …) and parsing it would be a
guess. Named in the findings as the obvious next step if John wants it.

**No override.** Every item here is fixed by editing a setting or a file, and
none is a spending trade-off the way the sleep override is.

### 3c. A ledger row with an estimate exists before the machine does

The gate reads `compute-ledger.md` (the `## Ledger` table only) and refuses
unless one row:

1. **names this run's output name** (`OUT`, e.g. `a3_30m_seed1`,
   `slice_handshake`) as a whole word — so `seed1` does not match `seed10`;
2. **is dated today or in the two days before, Pacific.** A row for the same
   output name from an earlier run must not satisfy a new launch; output names
   are reused by construction — `a3_30m_seed0` is the fetch-first launcher's
   default, the name of the registered seed-0 run, and the name the machine
   created by accident on 2026-09-21 ran under (`compute-ledger.md` line 74
   and the annotation at lines 96–118). Two days, not
   one, because the weekend roadmap writes rows on the Saturday for launches
   on the Saturday night or Sunday;
3. **has a dollar figure in its estimate column** (`$ est`);
4. **has not yet had its actual cost written** (`$ actual` column empty, a
   dash, or saying `pending`, `not launched`, `not yet` or `nothing spent`).
   A row whose actual cost is filled in belongs to a launch that has already
   happened; a new launch needs a new row.

~~The columns are counted from the right-hand end of the row, because a `|`
inside the prose of the "what ran" column (the 2026-08-17 row has one) shifts
every column counted from the left.~~

**Corrected 2026-09-24, after the check of pull request 33**
(`reviews/2026-09-24-launch-gate-pr33-check-claude-worktree.md`, section 8).
The struck sentence claimed a record handles a case the record shows it does
not handle. The real 2026-08-17 row has a `|` in its prose **and** an
annotation added as an extra, tenth cell. Counted from the right, that shape
put the actual-cost cell where the estimate should be, so a good row of that
shape dated today was refused for a "missing" dollar figure that was there.
The rule the gate now enforces, stated here as the review asked:

5. **the row has exactly eight cells**, the table's eight columns, once any
   `|` written as `\|` (the table's own escape for a `|` in prose) is set
   aside. A row with more or fewer is refused with "line N has C cells,
   expected 8", naming both likely causes: an unescaped `|` in the prose, or
   an annotation added as a cell, which belongs below the table. The gate
   does not guess which one it is, because nothing in the row tells them
   apart.

And to item 1, **"as a whole word" now means the name does not continue into
more of a name**: `slice_handshake-v2`, `slice_handshake.v2`,
`slice_handshake_v2` and `x-slice_handshake` do not satisfy a launch of
`slice_handshake`, because a hyphen is not a word boundary. The first version
treated one as a boundary, so a row for `slice_handshake-v2` satisfied a
launch of `slice_handshake` (the review's case B11). The only hyphenated
prefix accepted is `mvm-`, the name the launchers give the machine: a row
naming the machine `mvm-slice_handshake` names the run, and the real
2026-09-21 row does exactly that. A full stop ending a sentence still ends
the name.

Confidence: medium. Standard in spirit (the ledger's own rule 2). The strongest
alternative is an explicit key the operator writes into the row and passes to
the launcher (`LEDGER_KEY=…`), which removes the date heuristic; rejected
because it adds a variable the operator must remember, while the output name is
something the launcher already knows. **Most existing rows would not satisfy
this check** — of the rows in the table, only the 2026-09-21 row names an
output name at all (MEASURED: `grep -n 'a3_30m_seed0' compute-ledger.md`
matches line 74 and three annotation lines, and no other row). That does not
matter for past runs; it means every row written from now on must name the
output name, which is a new habit the refusal message states. The gate
does **not** check that John's go is quoted in the row (commitment C2(b)):
whether a sentence is a go is not something a pattern can decide, and a check
that passes on any quotation mark would be decoration.

**No override**, same reason as 3b. The path to the ledger is a variable,
`LEDGER`, so a test can point it at a stand-in; setting it is a deliberate act
in the same way `PMSET` already is.

### 3d. The decision

- Nothing found → one "ok" line per check, carry on.
- A dry run (`DRYRUN=1`) → every problem is printed as "WOULD REFUSE a real
  launch", and the launcher carries on to its dry-run block and exits 0.
  `check_launcher_argument_guard.sh` requires that.
- Only sleep problems, and `ALLOW_LAPTOP_SLEEP=1` → carry on, printing the
  existing "OVERRIDDEN … what it can cost" text.
- Anything else → print "REFUSING TO LAUNCH", every problem and its fix, and
  `exit 1`. The exit is explicit because the launchers run under
  `set -uo pipefail` without `-e` (ruling 2026-09-22 §5), so a gate that only
  printed would print and launch.

## 4. How it is tested without renting anything

A new harness, `src/launch_gate_selftest.sh`, runs **each of the three
unregistered launchers** through each refusal path. Every case stacks three
independent stops so that a broken gate still cannot rent a machine:

1. `pmset`, the ledger and the keep-awake command are stand-ins it writes;
2. a stand-in `runpodctl` is first on the command path, records that it was
   called, and exits 1 — so "the rental command was reached" is observed
   directly, not inferred from printed text;
3. `HOME` points at an empty temporary folder, so even the real `runpodctl`,
   if somehow reached, has no account key to use.

Before each run the harness checks that the command path resolves `runpodctl`
to its stand-in, and stops if it does not.

Each refusal case asserts the refusal's words, its exit status **and** that the
stand-in rental command was never called — the earlier mutation run in
`sleep_guard_selftest.sh` showed that an exit status alone is shared by
unrelated refusals and detects nothing. Each launcher also gets a **negative
control**: a safe Mac, a good ledger row and a sound watchdog, run as a real
launch, must get **past** the gate and reach the stand-in rental command. A
gate that refused everything would fail that case.

**Seen failing before trusted.** After the harness passes, the gate is
deliberately broken three ways — its `exit 1` replaced by a warning; the
ledger check made to accept any row; the deadline-order check removed — and
the harness run against each. The counts are recorded in the findings. A
harness that passes against a broken gate has not been shown to detect
anything (`docs/known-failure-modes.md`, "Adding to this list").

`sleep_guard_selftest.sh` keeps running unchanged against the fetch-first
launcher, except its case 6: it compares two line numbers written in the
launcher's comment with where those lines are, and that comment moves into the
shared gate, which serves three launchers with three different line numbers.
Case 6 is rewritten to check the fact the numbers stood for — in each launcher
the keep-awake spawn comes **after** the rental command — and that the comment
still says the launch window is uncovered. That also closes the second review's
follow-up 2 (the hand-kept line numbers that could rot).

## 5. What would count against this

- **Any case in which a launcher reaches the stand-in rental command while the
  gate should have refused.** That is the property.
- **The negative control refusing.** Then the gate refuses safe launches, and a
  gate that refuses safe launches is one somebody switches off.
- **A real launch next weekend refused for a reason that is wrong.** The ledger
  heuristics (§3c) are the likeliest source: a row written three days ahead,
  or an actual-cost cell holding a word the list does not know. If that
  happens, the fix is the explicit-key alternative, not a looser pattern.
- **A dry run that no longer exits 0**, which would break the argument-guard
  check's own contract.

## 6. What it costs

Nothing in money. In operator time: every real launch now needs a ledger row
naming its output name, dated within two days, before the command is run —
which ledger rule 2 already required. The staged rented slice
(`docs/successor-rented-slice-staging-2026-09-21.md`, output name
`slice_handshake`) has no such row today, so its step 1 will be refused until
one is written. Its go lapsed on 2026-09-22 and a fresh one is to be quoted
in a new row anyway.

## 7. Drafted amendment for the registered launcher — NOT APPLIED

For Gate A, alongside `argument-guard-method.md` §6. Proposed text for
`src/launch_a3.sh`, inserted after its settings block and before its dry-run
block:

```bash
# Amendment (drafted 2026-09-24, not in force until Gate A clears): the launch
# gate. Refuses a real launch when this Mac could sleep, when the fetch and
# the delete are not scheduled inside the run window, or when no ledger row
# with an estimate exists for this run. A dry run reports and carries on.
WATCHDOG="$SRC_DIR/watch_run_a3.sh"
CAFFEINATE="${CAFFEINATE:-caffeinate}"
. "$SRC_DIR/launch_gate.sh"
launch_gate
```

plus changing its watchdog line from `nohup caffeinate -dimsu …` to
`nohup "$CAFFEINATE" -dimsu …`. The case for it, in the argument-guard
amendment's own terms: it does not change what a bare invocation on a safe,
correctly prepared Mac does, which is the only invocation the registration
describes; it turns a launch the registration never contemplated — a sleeping
laptop, no ledger row — into a refusal. **It does change one thing a registered
run depends on:** the registered launcher would then read a file
(`launch_gate.sh`) that is not itself registered. Gate A should decide whether
the gate is registered with it or copied inline.
