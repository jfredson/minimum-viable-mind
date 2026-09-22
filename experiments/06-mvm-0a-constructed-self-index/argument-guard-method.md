# Method: making a launcher refuse an argument instead of launching

*Written and committed BEFORE the code, per this programme's standing
discipline and per John's ruling of 2026-09-22, which asked for exactly
that. Nothing in this note is a ruling. It records a decision John has
already made and says how it will be carried out.*

Date: 2026-09-22. Repo: `minimum-viable-mind`, experiment 06.

Red-team ledger number: **`RT-198`**, the silent-argument finding.

---

## 1. What went wrong, in plain words

A rented machine was created by a command whose whole purpose was to
create nothing.

The staged plan for the rehearsal's one rented slice opened with a step
labelled "prove the plan with no machine and no money". Its first line
ran the derived launcher with a `--help` flag. The launcher has no
`--help`. It has no handling for command-line arguments at all — no
`case "$1"`, no `getopts`, nothing anywhere in the file. So the flag was
not rejected and not reported. It was **silently ignored**, and the
script carried on exactly as it does when run with no arguments at all,
which is the real launch at its built-in defaults: the 30-million
parameter seed-0 recipe, 585,544,960 tokens, about ten hours, about ten
dollars.

The machine (`f1vtz2adz4dj8v`) was created and was deleted about a
minute later. It cost about two cents. The full account is the
2026-09-21 row of the compute ledger
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`) and
its annotation.

**The two cents are not the finding.** The command was run with its
output piped through `head`, which closed the pipe and killed the script
before it reached the remote steps, and that pipe is the only reason
anybody saw the machine being created. Run exactly as the plan wrote
it — with the output sent to `/dev/null`, which is what the plan said —
there is no early death and there is nothing on screen. The script runs
to completion in silence: it creates the machine, pushes the code, and
starts a ten-hour training run whose output path is the directory on the
network volume where the registered seed-0 artifacts already live. The
operator sees nothing at all.

John's ruling names the lesson: **a mitigation that depends on the
operator noticing is not a mitigation.** The fix is a guard in the code,
not a warning in a document.

## 2. Where the bad line came from, which is worth knowing

The plan file was written by `stage_rented_slice.sh`, the staging
script. That script **does** implement `--help`, at its line 68:

```sh
if [ "${1:-}" = "--help" ]; then sed -n '2,60p' "$0"; exit 0; fi
```

So the session that wrote the plan was generalising from the script it
had in its hands, which supports `--help`, to a script that does not.
That is an ordinary mistake and it will be made again. It is the reason
the fix has to sit in the thing being invoked rather than in the
instructions for invoking it: the person writing the instructions is
exactly the person who does not know.

## 3. The rule the code has to establish

> **A launcher that is given any argument at all refuses to run, says so,
> and names the way to preview a launch without creating anything. It
> does not guess what the argument meant and it does not carry on.**

This is deliberately blunt. No launcher in this repository has ever had
a meaningful command-line argument; all four are configured entirely
through environment variables, which are documented in each file's own
usage header. So refusing every argument costs nothing that anybody
uses, and it converts an undefined input from a silent ten-hour launch
into a one-line refusal.

## 4. What the guard is

Placed immediately after `set -uo pipefail`, before any other work:

```sh
# 2026-09-22 [RT-198]: this launcher takes NO command-line arguments and
# never has. Before this guard an unrecognised flag was silently ignored
# and the script proceeded to a real launch at its defaults, which cost a
# rented machine on 2026-09-21. See argument-guard-method.md.
if [ "$#" -ne 0 ]; then
  echo "refusing to run: $(basename "$0") takes no command-line arguments." >&2
  echo "  got $# argument(s): $*" >&2
  echo "  this launcher is configured by environment variables; see the usage header." >&2
  echo "  to preview a launch without creating anything: DRYRUN=1 $0" >&2
  exit 2
fi
```

Four details, each of which is load-bearing:

- **It exits explicitly rather than relying on the shell to stop.** All
  four launchers run under `set -uo pipefail` and deliberately **not**
  `set -e` (see §7), so a command that fails does not stop the script. A
  guard that only printed a complaint would print it and launch anyway.
  This is the single most important line of the design and it is the one
  that would be easiest to get wrong.
- **It names `DRYRUN=1` in the refusal.** The operator who typed a flag
  wanted something, and nine times in ten what they wanted was a dry
  run. Telling them the real way to get one is what stops the next
  person reaching for `--dry-run` and getting a launch.
- **It prints what it got.** A refusal that does not echo the offending
  argument leaves the operator guessing whether the shell mangled
  something.
- **It sits before everything, including the local self-tests.** The
  self-tests take a few seconds and touch nothing, but a guard that runs
  after any real work is a guard that has already allowed some.

## 5. Which files get it, and when

John's ruling of 2026-09-22 sets the scope, and it differs by file
because registration does.

**Now, in this change — the three unregistered launchers.** None is
registered text, so none needs an amendment.

| file | what it is |
|---|---|
| `src/launch_a3_fetch_first.sh` | the derived launcher carrying the shutdown fix; the one that created the machine |
| `src/launch_ctl_pilot.sh` | the control-learnability pilot launcher, split from the registered one |
| `src/launch_pilot_a1.sh` | the original A1 pilot launcher, where the whole family came from |

**Not now — the registered launcher.** `src/launch_a3.sh` is registered
text: Amendment A3's "what is registered" section names it, along with
the grammar, the tokenizer, the trainer, the frozen batteries and the
gates. It carries the same defect and it does not get edited here. The
guard is drafted for it in §6 and goes to Gate A as an amendment.

**Until that amendment clears: no session invokes a registered launcher
with any argument, and the pre-flight asserts it.** That is John's
wording and it is a standing prohibition, not a suggestion. §8 says how
the assertion is built, because a prohibition nobody checks is the
warning-in-a-document this ruling rejected.

## 6. The Gate A amendment, drafted

*This is the case to be made for `launch_a3.sh`, drafted here so that the
amendment text is written before it is argued rather than after.*

**What changes.** Four lines are added immediately after
`set -uo pipefail`: the guard in §4, unaltered.

**What does not change.** Everything else, including every default, the
recipe, the venue, the token budget, the act-weight and the
register-less-by-construction rule. Nothing a result depends on moves.

**The case, plainly.** The registration describes one invocation: the
launcher run with no arguments and configured by environment variables.
That is the only invocation the registered text has ever described, and
it is the only one any run in this programme has used. **The guard does
not change what that invocation does.** With no arguments, `$#` is zero,
the branch is not taken, and the file behaves byte for byte as it does
today.

What the guard changes is the behaviour on an input the registration
does not describe at all. Today an undefined input is a **launch**;
after the guard it is a **refusal**. The amendment therefore does not
alter the registered instrument's behaviour on any input the
registration defines. It removes an undefined behaviour that has already
cost a machine, and replaces it with a refusal.

**Why it cannot be left alone until the successor registration.** The
standing prohibition in §5 covers the gap, and the pre-flight assertion
in §8 makes the prohibition checkable — but both depend on sessions and
operators behaving, which is the class of mitigation this ruling
rejected. They are a stopgap with a known weakness, stated as such.

**What it costs.** Nothing to run. The amendment costs a Gate A pass.

## 7. `set -uo pipefail` without `-e`: deliberate, narrow, and worth
    restating

John asked whether the missing `-e` is deliberate. **It is**, and the
history says so rather than the comment.

The first launcher in the family was written with `set -euo pipefail`
(commit `f4f206b`, "A1 pilot launch prepared"). The `-e` was removed the
next day, in commit `d7b1283` ("30M rung prep"), **in the same hunk that
added this comment**:

```
#   launch-ssh exit codes unreliable (teardown resets) — trust
#   the explicit aliveness check;
```

and its companion commit `b62a0b1` is titled "launch script: tolerate
benign ssh teardown reset; explicit aliveness check". So the cause is
recorded and real: the remote launch command returns a non-zero exit
code on a benign teardown reset, and under `-e` that aborted the
launcher on a run that was in fact fine. Every later launcher inherited
the line by being split from that one.

**Two things follow, and only one of them is a problem.**

The removal is deliberate and its cause is genuine, so `-e` is **not**
something to switch back on as part of this change. Turning it on would
re-break the thing it was turned off to fix, and it would do so on the
launch path, where a spurious abort after the machine exists is a
machine nobody is watching.

But the fix was **much broader than the fault**. One command returns an
unreliable exit code; the response was to stop the whole script from
reacting to any command failing. The narrow fix — `|| true` on that one
command, or capturing its status and consulting the aliveness check that
already exists — was available and was not taken. Nothing about that is
urgent and nothing about it is being changed here, because changing it
means re-testing the launch path against the real vendor, which costs
money nobody has authorised. **It is recorded as a known property rather
than fixed quietly**, and it is the reason the guard in §4 exits for
itself instead of trusting the shell to stop.

## 8. How the prohibition is checked, not just stated

A standing rule that "no session invokes a registered launcher with any
argument" is worth nothing unless something fails when it is broken.

**A check script, `src/check_launcher_argument_guard.sh`**, which:

1. runs each **unregistered** launcher with a junk argument and asserts
   it refuses — exit status 2, a refusal on the error channel, and
   **no machine created**, which is guaranteed because the guard exits
   before the launcher reaches any vendor command;
2. runs each unregistered launcher's dry run and asserts it still works,
   so the guard cannot pass by breaking the launcher;
3. asserts that the **registered** launcher still lacks the guard, and
   prints the standing prohibition loudly while that is true. This is
   the part that turns the prohibition into something a session trips
   over rather than reads. When the Gate A amendment lands, this
   assertion is what changes, and the check then requires the guard
   there too.

**It never runs the registered launcher**, with or without arguments.
That is the whole point: the registered launcher with an argument is a
launch, and the check would be the very thing it exists to forbid. The
registered launcher is checked by reading its text, not by running it.

The check is wired into `stage_rented_slice.sh`'s local preconditions,
so the rehearsal's own pre-flight asserts it, and it is the test filed
with the failure-mode entry.

**It creates nothing and spends nothing.**

## 9. The staged plan's step 0 is withdrawn

Per John's ruling, the `--help` line is removed from step 0 and replaced
with the genuinely inert invocation:

```sh
DRYRUN=1 SCALE=10M MAXTOK=2000000 OUT=slice_handshake GRACE_S=600 \
  ./launch_a3_fetch_first.sh
```

The dry-run guard exits before anything is created, and the launcher's
own usage header already documents that invocation. In John's words,
"step 0 was right about what it wanted and wrong about how to get it".

The plan file is generated, so the change is made in the generator,
`stage_rented_slice.sh`, and the plan file is regenerated from it.

## 10. Does this reach anything else that can spend money?

Asked by John, and answered by reading every shell script in the
repository and every Python entry point.

**The four launchers are the only things here that can create a rented
machine.** `runpodctl pod create` appears in those four files and
nowhere else.

**All four have the silent-argument property, and nothing else does.**
Every other script that takes an argument handles it properly:

| file | how it takes arguments | verdict |
|---|---|---|
| `src/watch_run_a3.sh` | `ENVF="${1:?usage: watch_run_a3.sh <env-file>}"` | refuses loudly when missing |
| `src/watch_run.sh` | `ENVF="${1:?usage: watch_run.sh <run-env-file>}"` | refuses loudly when missing |
| `src/reap_agent.sh` | handles `--self-test` explicitly, then the same `${1:?usage}` | refuses loudly when missing |
| `src/reap_handshake_selftest.sh` | `ONLY="${1:-}"`, an optional filter | deliberate and documented |
| `src/stage_rented_slice.sh` | implements `--help` | works |
| `src/run_post_pilot.sh` | takes none, and is the one script in the repo using `set -euo pipefail` | no exposure |

This matters in both directions. The two reaping scripts are the
machinery that **ends** billing, so a silently-ignored argument there
would cost money by failing to reap rather than by launching. They are
clean: both demand their argument and stop without it.

**No Python entry point uses `parse_known_args`**, which is the
equivalent hazard — it accepts unknown flags and hands them back rather
than refusing. Every parser in the repository rejects an argument it
does not recognise, which is `argparse`'s default and is the behaviour
the launchers lacked.

So the answer is: **the property reaches the four launchers and stops
there.** Three are fixed by this change and the fourth is registered and
goes to Gate A.

## 11. What this change cannot claim

- **It does not make a launch safe.** It makes one specific way of
  starting an unintended launch impossible. A correct-looking
  environment variable pointing at the wrong recipe is untouched by it.
- **It has been exercised against the unregistered launchers only.** The
  registered launcher's guard is drafted text until Gate A rules on it,
  and until then the standing prohibition and the pre-flight assertion
  are what stand in its place. They depend on sessions behaving, which
  is a weaker guarantee than code, and saying otherwise would be the
  mistake this note was written about.
