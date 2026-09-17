# Reaping audit — the in-flight pods have no reaper of their own

*2026-09-16, late. Read-only checks against both running pods. Prompted
by John asking whether an OS update and reboot would be safe. Nothing was
changed on either pod and nothing was fixed; two defects are reported
here for his ruling.*

## The operational answer first

**The two Mac watchdogs are the only thing that will fetch the
checkpoints and delete the pods.** They are plain polling loops under
`caffeinate`, started 20:13 and 20:15 local. A reboot kills both. The
pods keep training either way, because they are remote.

## Finding 1: the pods carry no reaper, verified four ways

| check | seed 1 | seed 2 |
|---|---|---|
| `/root/mvm/pod_id` present | no | no |
| `~/.runpod/` config directory | absent | absent |
| RunPod environment variables | none | none |
| reaper process in `ps` | none | none |

This is consistent with the paid $0.29 ops test of 2026-09-16, which
established that a pod carries no credential and no identifier of its
own. These two pods were launched before pod-side reaping was armed, so
none of tonight's reaper-key work applies to them.

**A correction to my own check, recorded because it nearly went the other
way.** My first pass used `pgrep -f 'sleep .*runpodctl remove'` and
reported a deadline reaper RUNNING on both pods. That was a **false
positive**: `pgrep -f` matches whole command lines, and the pattern
matched the very SSH command carrying it. Listing processes properly with
`ps` and grepping the output shows no such process on either pod. The
compute ledger already records this family of trap from wave 2. I came
within one sentence of telling John the pods were covered when they are
not.

## Finding 2: the launcher's pod-side verification cannot succeed

This one affects future launches, including the reaper-key change made
earlier tonight.

The pod image ships **runpodctl 1.14.15**, whose command set is the older
verb-first style:

```
Available Commands:
  config   create   exec   get   remove   start   stop   ...
```

There is no `pod` subcommand. Asking for one fails outright:

```
$ runpodctl pod list
Error: unknown command "pod" for "runpodctl"
```

The launcher's verification step calls `runpodctl pod get <id> -o json`,
which is the newer noun-first form. On this image it can only ever fail,
so the launcher would print NOT VERIFIED on every launch. After tonight's
change that is no longer a quiet degrade: it now says to stop and ask
John, which is the right behaviour but would be triggered by a false
alarm rather than by a real credential problem.

The reaper command itself uses `runpodctl remove pod <id>`, which **is**
the correct form for this version. So the shapes are inconsistent with
each other: one verb-first, one noun-first, and only the reaper matches
the tool actually installed.

**Nothing is fixed here.** The proposed fix is a one-line change of the
verification call to the verb-first form, `runpodctl get pod <id>`,
checked against the same harmless-read criterion. It touches no
registered text and costs nothing, but it is a change to the launch path
and no launch is imminent, so it waits for John.

Worth noting honestly: this defect has never bitten, because pod-side
reaping has never actually run. It was implemented, then measured
impossible without a credential, then re-armed on John's ruling, and no
pod has yet been launched with it in force.

## What this means for a reboot

Restarting the watchdogs after a reboot restores full cover, and the
script is a plain polling loop with no accumulated state, so restarting
is safe and idempotent. The commands are in `STATUS.md`.

The exposure if they are not restarted: both pods finish around 06:10
local, nothing fetches the checkpoints, nothing deletes the pods, and
they bill about $2 an hour together until someone acts. The advisory
`terminate-after` does not close this gap; the ledger records it failing
to fire and costing $97 on the 30M A1 pilot.
