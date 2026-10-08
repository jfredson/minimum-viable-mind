*This is file 32 of 33 of one review packet, pasted into a single conversation. It contains record 23 part 2 of 3 (the list of what has gone wrong in this program before, which the inside reviewer ran against version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 23 of 25, part 2 of 3 - the list of what has gone wrong in this program before, which the inside reviewer ran against version 4 - `docs/known-failure-modes.md` (complete file, 55,318 characters) =====
*Part one: count what the generator actually puts in each pre-stated cell, at
rehearsal scale.* This is the part that generalises to a design other than the A3
grammar, and it is the part that catches an empty cell. Four things in the block
below belong to the design being checked and are meant to be replaced: the module
that is imported, the list of pre-stated cells, and the two small functions that
say what a trial is and which cell it lands in. Between them they are most of the
block; everything else stands.

```
$ python3 -c "
import sys; sys.path.insert(0, 'experiments/06-mvm-0a-constructed-self-index/src')
from collections import Counter
import curriculum_a3 as design          # the registered generator, not a stand-in

PRE_STATED_CELLS = ['donor dictates the same answer',
                    'donor dictates a different answer']

def trials(episodes):                   # one trial per (episode, item, donor)
    for ep in episodes:
        for item in ep.contested:
            v = ep.values[item]
            for donor in range(design.N_AGENTS):
                if donor != ep.own_slot:
                    yield v[donor], v[ep.own_slot]

def cell_of(trial):
    donor, recipient = trial
    return PRE_STATED_CELLS[0] if donor == recipient else PRE_STATED_CELLS[1]

counts = Counter(cell_of(t) for t in trials(design.generate_balanced(200, seed=0)))
for cell in PRE_STATED_CELLS:
    print(f'{cell}: {counts.get(cell, 0)} trials')
"
donor dictates the same answer: 0 trials
donor dictates a different answer: 1200 trials
```

**Zero is the finding.** Two hundred episodes of the registered grammar produce
twelve hundred donor-and-recipient pairs and not one of them lands in the first
pre-stated cell, because the grammar draws a distinct value per agent for each
contested item. The comparison that cell is half of can never be made. That is
failure 3, caught by a command, on the design that produced it.

*Until 2026-09-21 this command did not execute.* It imported `src.curriculum`,
and there is no `src` package — the generator modules sit in
`experiments/06-mvm-0a-constructed-self-index/src/` and import each other by bare
name, so the directory goes on the path rather than being treated as a package.
It called a function named `generate`, and the module has `generate_episode` and
`generate_balanced` and no `generate`. And it used `cell_of` and
`PRE_STATED_CELLS` without ever defining them, so a session holding a different
design could not have told what they were supposed to return. It raised
`ModuleNotFoundError` on the first line that did any work, and so had never been
seen to fail on anything.

*Part two: read the generator for the property that would empty a cell —
drawing without replacement, a shuffle that permutes rather than resamples, a
distinctness assertion, a deterministic rule that makes two conditions the same
condition.* Every file the generator is spread across, not one of them:

```
$ grep -rnE "\.sample\(|\.shuffle\(|\.permutation|permutations\(|set\(|distinct|unique|without replacement" experiments/06-mvm-0a-constructed-self-index/src/curriculum.py experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:51:# Marker pool: per-episode speaker labels drawn without replacement, so no
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:109:    markers = rng.sample(MARKERS, n_agents)
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:113:    items = rng.sample(ITEMS, min(len(ITEMS), n_turns))
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:118:        rng.shuffle(r)
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:218:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum.py:311:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:17:  pairs. Within an item the four values are **distinct**, so an item's
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:59:At its own revision turn the model sees four distinct earlier values for
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:209:    markers = rng.sample(MARKERS, N_AGENTS)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:210:    contested = rng.sample(ITEMS, N_CONTESTED)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:212:    # distinct values per contested item, one per agent
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:215:        vs = rng.sample(SLOTS, N_AGENTS)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:219:    rng.shuffle(pairs)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:233:    revisers = rng.sample(range(N_AGENTS), K_REVISERS)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:236:    rng.shuffle(rev_turns)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:329:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:371:       agent revised, this alone identified the model uniquely in a
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:420:        rng.shuffle(slots)
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:468:        # every contested item assigned by all agents, distinct values,
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:530:    # distinctness constraint still holds
experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py:539:            assert len(set(vs)) == N_AGENTS, "distinctness broken by enactment"
```

Line 215 of the A3 grammar is the one that empties the cell — four distinct
values drawn for four agents, without replacement — and line 539 asserts the
property survives rendering. Lines 17, 59, 212, 468 and 530 are the comments that
say so in English, which is often where this is easiest to see.

**What this part cannot see, plainly.** It is a text search, so it finds only
idioms somebody thought to put in the pattern. Until 2026-09-21 the pattern held
two of them, `rng.sample` and `assert len(set`, and looked in one file; it would
have missed a shuffle, a `set()`, a `numpy` permutation, sampling without
replacement written a third way, a constraint enforced by rejecting and redrawing
inside a loop, a distinctness rule that lives in the encoder rather than the
generator, or a generator in a file nobody listed. The pattern above is wider and
covers two files instead of one, and it still misses all of those things if a
design spells them differently. **Part one is the detector; part two only says
where to look once part one has found a cell at zero.** A clean part two is not
evidence that no cell is empty.

*Part three: compute every pre-stated threshold at both ends of the range it will
face — a system that has learned the task and one that has learned nothing — and
print what the check returns at each.*

```
$ python3 -c "
for p in (0.95, 0.80, 0.60, 0.25):
    print(f'own-directed accuracy {p:<5} -> untouched rate {(1 - p) / 7:.4f}')
"
own-directed accuracy 0.95  -> untouched rate 0.0071
own-directed accuracy 0.8   -> untouched rate 0.0286
own-directed accuracy 0.6   -> untouched rate 0.0571
own-directed accuracy 0.25  -> untouched rate 0.1071
```

**It fails if** any pre-stated cell comes back with zero trials, or if a threshold
fires on the healthy end of the range and passes on the broken end. Both are
fatal: the first registers a comparison that can never be made, the second
registers an instrument check that reads a working instrument as a broken one.

---

## 4. A claim of measurement with no record, or with a record that does not reproduce

**What it was, first form.** Amendment A3's registered text said both battery
ceilings were "verified by the attack sweep, whose best ownership-blind attack
reached 0.3036 on 12,000 episodes". The 0.3036 is an attack on the primary
battery. The attack sweep contains no control-battery code at all, so the clause
is false as applied to the control, and the control's registered ceiling rests
entirely on one reference solver that ignores the one piece of information the
control question supplies. Registered on John's instruction, before any further
analysis, in
`experiments/06-mvm-0a-constructed-self-index/ceiling-defect-2026-09-17.md`. One
sentence had attached one verification to two numbers, and the number it did not
cover is the one that later turned out to be 1.0 — which is failure 1 above.

**What it was, second form.** A finding labelled MEASURED reported a count that
does not reproduce. The seventeenth finding of the independent pass on the
Amendment A4 clause (`F17`, on whether one condition's validity gates were ever
applied) says the endpoint records carry no such field "among their 110 keys".
They carry 15. John ruled on this on 2026-09-21, as the twentieth item of that
day's review-verification and staged-spending ruling
(`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`): the
finding's substance is undisturbed, but a MEASURED label is this programme's
promise that a number came from running something, and a committed record a
future session may cite has to be right.

**The test.** Two parts.

*Part one: list every sentence in the text that claims a measurement, so that
none is checked by accident and none is missed.* Two sweeps, because one of them
is a word list and a claim of measurement does not have to use a word:

```
$ grep -n -iE "verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result" <the text>.md
$ grep -n -E "[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}" <the text>.md
```

The second sweep catches a bare number offered as a result with no verb attached
to it, which no word list will ever find. Both sweeps are deliberately noisy —
`run` matches "running" and also "run" inside other words, `result` matches
"resulting", and the number sweep matches every figure in the document including
the ones that are not claims. Noise is the safe direction here: a session reads
the list and crosses off what is not a claim, which costs minutes, where a miss
costs whatever the unchecked claim costs.

**Why the word list is this wide.** Until 2026-09-21 it held seven words —
`verified`, `measured`, `calibrated`, `attacked`, `reproduc`, `confirmed`, `ran` —
and missed this document's own headline claim of measurement, the sentence near
the top reading "Every output printed below was produced by running the command
printed above it", because "running" contains none of them. It missed several
other ordinary ways of saying the same thing too. Six claims, the old list, the
widened list, and the number sweep:

```
$ python3 -c "
import re
OLD = r'verified|measured|calibrated|attacked|reproduc|confirmed|ran'
NEW = (r'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|'
       r'shows|showed|found|observed|recorded|returns|returned|yield|result')
NUM = r'[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}'
claims = [
    'Every output printed below was produced by running the command printed above it.',
    'We verify both ceilings against the attack sweep.',
    'Verification of the clause is filed with the run.',
    'The endpoint records were checked before the gate opened.',
    'The sweep shows no ownership signal at that position.',
    'Control battery ceiling: 0.3227.',
]
print('old   new   number   sentence')
for c in claims:
    print(f'{bool(re.search(OLD,c,re.I)):<5} {bool(re.search(NEW,c,re.I)):<5} '
          f'{bool(re.search(NUM,c)):<8} {c[:48]}')
"
old   new   number   sentence
0     1     0        Every output printed below was produced by runni
0     1     0        We verify both ceilings against the attack sweep
0     1     0        Verification of the clause is filed with the run
0     1     0        The endpoint records were checked before the gat
0     1     0        The sweep shows no ownership signal at that posi
0     0     1        Control battery ceiling: 0.3227.
```

The old list catches none of the six. The widened list catches five. The sixth is
a bare number with no verb anywhere near it, and only the number sweep finds it —
which is why part one is two commands and not one.

**What part one still cannot catch, plainly.** A claim of measurement written in
words nobody put in the pattern: "the two batteries came out the same", "this
held on all three checkpoints", "the gate opened". A claim carried by a table
with no sentence around it. A claim in a figure caption or a file name. And the
sweeps cannot tell a claim from a quotation of one, or from a sentence that says
a measurement was *not* made — every hit still has to be read. Part one narrows
the reading; it does not replace it.

*Part two: for each sentence the first part returns, name the file it cites and
run the one command that regenerates the number. Two worked examples, both from
the failures above:*

```
$ grep -c control experiments/06-mvm-0a-constructed-self-index/src/shortcut_sweep.py
0
```

*A practical warning about that one.* `grep -c` exits with status 1 when the
count is zero, because "nothing matched" is grep's failure status whether or not
you asked it to count. A session running this pass inside a script that stops on
the first failing command will stop right here, on the example whose answer is
the point. Run these by hand, or make the script tolerate it — appending
`|| true` to the line is enough — and never read a stopped script as a passed
test.

```
$ python3 -c "
import json
base = 'experiments/06-mvm-0a-constructed-self-index/a3-gates/'
for p in ('endpoint_a3_30m_seed1.json', 'endpoint_a3_30m_seed2.json', 'pilot_endpoint.json'):
    print(p, len(json.load(open(base + p))))
"
endpoint_a3_30m_seed1.json 15
endpoint_a3_30m_seed2.json 15
pilot_endpoint.json 7
```

The first says that the module the registered sentence credits with verifying the
control battery's ceiling does not mention that battery once. The second says
where 110 came from: nowhere.

**It fails if** a sentence claiming a measurement names no file; or names a file
that does not contain the number; or names a file that exists at no commit, which
is its own recurring form — the citation defect that stopped the previous version
of the Amendment A3 closure text was exactly this (`RT-145` in the red-team
ledger, the finding that a registration commit was resting on a ruling file that
had not been committed). A registration commit is the one commit that may not
rest on a record its reader cannot open.

---

## 5. A command that creates something while documented as creating nothing

**What it was.** The staged plan for the rehearsal's one rented slice opened
with a step headed "prove the plan with no machine and no money". Its first
line ran a launcher with `--help`. The launcher had no `--help`. It had no
handling for command-line arguments at all — no `case "$1"`, no `getopts`,
nothing anywhere in the file. So the flag was not rejected and not reported.
It was **silently ignored**, and the script carried on exactly as it does when
run with no arguments, which is the real launch at its built-in defaults: the
30-million-parameter seed-0 recipe, 585,544,960 tokens, about ten hours and
about ten dollars, writing into the directory on the network volume where the
registered seed-0 artifacts already live.

**How it showed up.** By creating a rented machine, on 2026-09-21, in a
session whose authorisation was for a different and much smaller run. The
machine (`f1vtz2adz4dj8v`) was deleted about a minute later and cost about two
cents. The full account is the 2026-09-21 row of the compute ledger
(`experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`) and the
annotation beneath it. It is filed in the red-team ledger as `RT-198`, the
silent-argument finding.

**The two cents are not the finding, and this is the part worth keeping.** The
command was run with its output piped through `head`, which closed the pipe
and killed the script before it reached the remote steps. That pipe is the
only reason anybody saw a machine being created. Run exactly as the plan wrote
it — with the output sent to `/dev/null`, which is what the plan said — there
is no early death and there is nothing on screen. The script runs to
completion in silence. **The difference between a two-cent finding and a
ten-dollar one with registered data underneath it was an incidental `head` in
a pipeline**, and John's ruling of 2026-09-22 draws the general lesson: a
mitigation that depends on the operator noticing is not a mitigation.

**Where the bad line came from**, because it will be written again. The plan
was generated by `stage_rented_slice.sh`, and that script **does** implement
`--help`, at its line 68. The session writing the plan generalised from the
script in its hands, which supports `--help`, to a script that does not. The
person writing the instructions is exactly the person who does not know, which
is why the guard has to live in the thing being invoked.

**What was recorded when it happened.** This block is the output of the
command as it behaved before the fix. **Do not run it.** It is printed because
a failure mode with no record of the failure is a citation, and because the
guard below cannot be shown to catch anything unless what it catches is
written down. The launcher no longer behaves this way; the registered launcher
`launch_a3.sh` still does, which is why the standing prohibition exists.

```
$ ./launch_a3_fetch_first.sh --help          # DO NOT RUN — this creates a machine
local pre-flight: module self-tests
  ok: curriculum_a3
  ok: encoding_a3
  ok: train_a3
  ok: frozen batteries present
creating SECURE pod (NVIDIA GeForce RTX 5090) for 30M/585544960 tok (out: a3_30m_seed0)
  run dir: /workspace/mvm-out (network volume — survives pod death)
{
  "costPerHr": 0.99,
  "desiredStatus": "RUNNING",
  "id": "f1vtz2adz4dj8v",
  ...
}
```

**The fix.** A guard at the top of each launcher, before any other work, which
refuses any argument, says what it got, names `DRYRUN=1` as the way to preview
a launch, and **exits explicitly** rather than relying on the shell to stop —
these files run under `set -uo pipefail` and deliberately not `set -e`, so a
guard that only complained would complain and launch anyway. The reasoning is
in `experiments/06-mvm-0a-constructed-self-index/argument-guard-method.md`,
committed before the code.

It is on the three unregistered launchers now. `launch_a3.sh` is registered
text and goes to Gate A as an amendment; until that clears, **no session
invokes a registered launcher with any argument**, and the test below asserts
it.

**The test.** One command. It creates nothing, spends nothing, and never runs
the registered launcher — running that with an argument is the very thing
being forbidden, so it is checked by reading its text instead.

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
```

```
RT-198 — launchers must refuse arguments rather than launch

unregistered launchers: an argument is refused
  [ ok ] launch_a3_fetch_first.sh refuses an argument (exit 2)
  [ ok ] launch_a3_fetch_first.sh says why it refused
  [ ok ] launch_a3_fetch_first.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_a3_fetch_first.sh guard (line 104) precedes any vendor command (line 227)
  [ ok ] launch_ctl_pilot.sh refuses an argument (exit 2)
  [ ok ] launch_ctl_pilot.sh says why it refused
  [ ok ] launch_ctl_pilot.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_ctl_pilot.sh guard (line 87) precedes any vendor command (line 201)
  [ ok ] launch_pilot_a1.sh refuses an argument (exit 2)
  [ ok ] launch_pilot_a1.sh says why it refused
  [ ok ] launch_pilot_a1.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_pilot_a1.sh guard (line 42) precedes any vendor command (line 99)

unregistered launchers: the guard did not break the real path
  [ ok ] launch_a3_fetch_first.sh dry run still exits 0
  [ ok ] launch_a3_fetch_first.sh dry run still creates nothing
  [ ok ] launch_ctl_pilot.sh dry run still exits 0
  [ ok ] launch_ctl_pilot.sh dry run still creates nothing
  [ ok ] launch_pilot_a1.sh dry run still exits 0
  [ ok ] launch_pilot_a1.sh dry run still creates nothing

registered launcher: read, never run
  [ ok ] launch_a3.sh does NOT carry the guard, which is expected before Gate A

  ***********************************************************************
  STANDING PROHIBITION, in force until the Gate A amendment clears:
  launch_a3.sh is REGISTERED TEXT and still has NO argument handling.
  An argument passed to it is SILENTLY IGNORED and it proceeds to a REAL
  LAUNCH at its defaults -- about ten hours and about ten dollars,
  writing into the registered seed-0 directory on the network volume.

      NO SESSION INVOKES A REGISTERED LAUNCHER WITH ANY ARGUMENT.

  To preview it without creating anything:  DRYRUN=1 ./launch_a3.sh
  Ruled by John 2026-09-22. Method: ../argument-guard-method.md [RT-198]
  ***********************************************************************


negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

**What the output has to show**, for any design this is pointed at: every
launcher that can create a rented machine refuses an argument with exit status
2; each guard sits before that file's first vendor command; every dry run
still exits 0 and still reports creating nothing; and the negative control
rejects an unguarded stand-in. **That last one is what makes the rest worth
reading.** A test that can only pass proves nothing, so the check builds a
stand-in with the pre-2026-09-22 shape — a script that ignores its arguments
and carries on — and requires the checks to reject it. If the control ever
reports the unguarded stand-in passing, the harness has stopped measuring what
it claims to.

**The line that is expected to change.** While `launch_a3.sh` remains
registered and unguarded, the check prints the standing prohibition and still
exits 0, because an unguarded registered launcher is the expected state before
Gate A rather than a failure. When the amendment lands, that file moves into
the list whose refusal is exercised, and the prohibition block goes away. A
session reading this entry after that point should expect the output above to
differ in exactly that respect and in no other.

---

## 6. A remote step tested only against stand-ins

*Added 2026-09-25 (Pacific). John ruled the addition on 2026-09-25 ("agreed
on all", on section 7 of `docs/2026-09-25-rented-slice-findings.md`, whose
item 3 proposed it). The session that wrote this entry also wrote the fix it
describes; under the pairing rule a different session checks both. The
opening section of this file still counts five failures and fifteen printed
blocks: it predates this entry and is left as written.*

**What it was.** A command sent to a rented machine over `ssh` whose every
test replaced `ssh` with a stand-in. The command was the one that starts the
machine's own shutdown watcher, line 467 of
`experiments/06-mvm-0a-constructed-self-index/src/launch_a3_fetch_first.sh`
at commit `4d98cfc`, in the form `cd /root/mvm/src && nohup sh reap_agent.sh
… >> …/reaper.log 2>&1 < /dev/null &`. In that form the `&` sends the whole
`cd && nohup` chain to the background as one subshell. The redirections
apply to `nohup` only, so the subshell keeps the connection's output open
until the watcher exits, and `ssh` waits for it. The watcher runs until its
+24-hour deadline. Every test of the launcher used a stand-in `ssh` that
exits at once (`reap_handshake_selftest.sh` sets `SSH="$BIN/fakessh"`), and a
stand-in that exits at once returns at once **whatever the remote command
does**. So no test could have seen the hang. The same file had already met
the same hang, on the training start, in August 2026: its comment says "this
ssh can HANG after the remote nohup succeeds", and that call had been capped
at 60 seconds ever since. The watcher start, added on 2026-09-21, was not.

**How it showed up.** On the first real `ssh` that line ever met, on
2026-09-25, during the rented slice. The launcher hung for about 30 minutes
after the watcher had started, never reaching the timing step, the training
or the laptop watchdog. A session watching the log stopped it and deleted
the machine; it cost $0.4974, and neither measurement was taken (the
2026-09-25 row of `experiments/06-mvm-0a-constructed-self-index/compute-ledger.md`,
and `docs/2026-09-25-rented-slice-findings.md` sections 4 and 5).
**Unattended, nothing on the laptop would have deleted the machine** — the
laptop watchdog is spawned after training starts — so it would have billed
until its own +24-hour deadline, about $24 against a hard cap of $2.00
(findings section 5, ARGUED there from the watcher's code).

**Why this is a species and not an instance of failure 5.** Failure 5 is a
command that does something its documentation says it does not. This one
does exactly what it says; what was wrong was the evidence that it worked.
A stand-in is built to answer the way the far end is *expected* to answer,
so a test against it can only confirm the expectation. The more a remote
step's behaviour depends on the far end — how a shell backgrounds a job,
what a vendor's tool accepts, what a machine carries — the less a stand-in
test says about it. The shutdown handshake itself was, until 2026-09-25,
"verified against local stand-ins only" in its own author's words
(`experiments/rehearsal-successor-measure/src/stage_rented_slice.sh`,
header), and the slice existed to close exactly that gap.

===== END OF RECORD 23, part 2 =====

