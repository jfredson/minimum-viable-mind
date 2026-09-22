# Ruling 2026-09-22: launchers refuse arguments, and the rented slice's go lapses

*Recorded 2026-09-22 (Pacific). John's rulings in reply to a session that halted
the rehearsal's rented slice and reported that the plan's own step 0 had created
a rented machine. **These are John's own rulings, in his own words, not
recommendations he approved** — he wrote them unprompted in reply to the halt
report, and the wording below follows his. Recorded as his authorship for that
reason. About two cents was spent before the halt, on the machine described in
the 2026-09-21 compute-ledger row; nothing has been spent under this ruling.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`).
Red-team ledger number for the underlying finding: **`RT-198`**.*

---

## What the halt was about

The staged plan for the rented slice opened with a step headed "prove the plan
with no machine and no money". Its first line ran the derived launcher with a
`--help` flag. The launcher has no `--help` and no command-line argument
handling at all, so the flag was silently ignored and the script proceeded to a
real launch at its defaults — the 30-million-parameter seed-0 recipe, about ten
hours and about ten dollars. A machine was created and deleted about a minute
later.

John's assessment of the halt itself, quoted: *"Halting was right, and so was
the shape of the report: the finding, what you did not test, what it cost, and
that you fixed nothing. That is what the rule is for."*

## 1. Step 0 is withdrawn

The `--help` line is removed and replaced with `DRYRUN=1
./launch_a3_fetch_first.sh`, which is the genuinely inert path: the dry-run
guard exits before anything is created, and the launcher's own usage header
already documents that invocation.

In his words: *"Step 0 was right about what it wanted and wrong about how to get
it."*

Done. The plan file is generated, so the change was made in the generator,
`experiments/rehearsal-successor-measure/src/stage_rented_slice.sh`.

## 2. The launchers get an argument guard

Any argument at all is refused, with a message naming `DRYRUN=1` as the way to
dry-run. **The scope differs by file, because registration does.**

- **`launch_a3_fetch_first.sh` is derived and unregistered. Done now, method
  committed before the code, at no cost.** `launch_ctl_pilot.sh` and
  `launch_pilot_a1.sh` carry the property too and are unregistered, so they go
  with the first group. All three are done.
- **`launch_a3.sh` is registered text.** The same guard is drafted and goes
  through Gate A as an amendment. It is not applied here. The case to be made,
  in John's framing: the guard does not change what a bare invocation does,
  which is the only invocation the registration describes, and it turns an
  undefined input into a refusal rather than a launch. The drafted amendment is
  §6 of `experiments/06-mvm-0a-constructed-self-index/argument-guard-method.md`.

**Standing prohibition, in force until the Gate A amendment clears:** no session
invokes a registered launcher with any argument, **and the pre-flight asserts
it.** The assertion is `src/check_launcher_argument_guard.sh`, wired into the
rehearsal staging script's local preconditions.

The principle behind the scope, quoted: *"The fix is a guard in the code, not a
warning in a document. This was caught by an incidental head in a pipeline; as
written the plan would have run to completion in silence. A mitigation that
depends on the operator noticing is not a mitigation."*

## 3. It is filed as a failure mode, exercised rather than cited

A real entry in `docs/known-failure-modes.md` with the command and its output,
not a citation — ruling 22b holds that failure modes are exercised rather than
cited, and this one has both halves: the recorded output of the command that
created the machine, and a test that creates nothing. Filed as failure 5, with
the red-team ledger number `RT-198`.

## 4. The go for the rented slice lapses, and no fresh one is issued yet

John's words: *"My go does not carry over, and I am not issuing a fresh one yet.
It named the staging document by date, and that document is about to change, so
the authorization would stop describing what runs. Nothing was spent, so there
is nothing to preserve."*

**What is owed before a fresh go:** the amended plan, checked by a session other
than the one that amended it, per the pairing rule in
`docs/outside-review-protocol.md`.

This matters beyond this run: it establishes that **an authorisation naming a
document by date lapses when that document changes.** A go describes what runs,
and a go that no longer describes what runs is not an authorisation.

## 5. Two questions he asked, and the answers

**Is `set -uo pipefail` without `-e` deliberate?** Yes. The first launcher was
written with `set -euo pipefail` (commit `f4f206b`) and the `-e` was removed the
next day in commit `d7b1283`, in the same hunk that added the comment recording
that the remote launch command returns an unreliable exit status on a benign
teardown reset; its companion commit `b62a0b1` is titled "launch script:
tolerate benign ssh teardown reset; explicit aliveness check". Every later
launcher inherited the line by being split from that one.

So it is deliberate and its cause is real, and it is **not** being switched
back on: doing so would re-break what it was turned off to fix, on the launch
path, where a spurious abort after the machine exists is a machine nobody is
watching. It is recorded that the fix was **broader than the fault** — one
command returns an unreliable status, and the response stopped the whole script
reacting to any command failing — and that the narrow fix was available and not
taken. Nothing is changed there, because changing it means re-testing the launch
path against the real vendor, which costs money nobody has authorised. It is the
reason the guard exits for itself rather than trusting the shell to stop.

**Does the silent-argument property reach anything else that can spend money?**
No. It reaches the four launchers and stops there.

`runpodctl pod create` appears in those four files and nowhere else in the
repository, so nothing else here can create a rented machine. Every other script
that takes an argument handles it properly: `watch_run_a3.sh`, `watch_run.sh`
and `reap_agent.sh` all demand their argument with `${1:?usage: …}` and stop
without it, which matters in the other direction — those are the machinery that
**ends** billing, so a silently-ignored argument there would cost money by
failing to reap. `reap_handshake_selftest.sh` takes a deliberate optional
filter. `stage_rented_slice.sh` implements `--help` and it works.
`run_post_pilot.sh` takes no arguments and is the one script in the repository
using `set -euo pipefail`. No Python entry point uses `parse_known_args`, which
is the equivalent hazard; every parser rejects an argument it does not
recognise.

## 6. Recorded alongside, not ruled

One latent defect was met while carrying this out and is **not** covered by any
ruling above. The generated plan file bakes in the absolute path of whichever
checkout generated it, so a plan generated inside a working copy that is later
deleted prints commands nobody can run. It has already happened once: the copy
committed before this session pointed into a worktree that no longer exists.
Nothing was changed about it. It is named here so it is not found twice.
