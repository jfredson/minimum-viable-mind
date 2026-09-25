# Check: the two repairs to the launch precondition, and the finished launcher read end to end

*Written 2026-09-24 (Pacific) by a checking session that wrote none of the work
being checked, under the pairing rule in `docs/outside-review-protocol.md`.*

*Written under the workspace plain-language rule (`~/Documents/Code/CLAUDE.md`,
ruled 2026-08-30).*

**What was checked.** Branch `worktree-agent-a2667f187591fcead` at commit `5913bfa`,
"Tell the operator what the keep-awake cover does not reach", sitting on `32472d1`
("Say when the sleep cover starts, and stop 0 switching the guard off") and the merge
`d4f10fa`, which in turn sit on `aa7b739` ("Refuse to launch when this Mac could fall
asleep"). Two files, both in `experiments/06-mvm-0a-constructed-self-index/src/`: the
derived launcher `launch_a3_fetch_first.sh` and the test beside it,
`sleep_guard_selftest.sh`. The earlier check of `aa7b739` is
`reviews/2026-09-24-sleep-guard-check-claude-worktree.md`, written on branch
`worktree-agent-a0658109b4974cdd4` at commit `a6250de`.

**Nothing was rented, no vendor was contacted, nothing was spent, and this Mac's real
power settings were not changed.** They were read three times and were the same at the
end as at the start: the never-sleep override off (`SleepDisabled 0`), drawing from
wall power, idle sleep timer fifteen minutes on both battery and wall power. Every
exercise of the guard used a stand-in power reader written by this session or supplied
by the test. The staged slice was not run.

**Verdict: yes, merge. Nothing must be fixed first.** This is the fourth round on this
precondition and the first that turns up nothing blocking. Three small things are
carried below as follow-ups, one of them the gap the author named and left, and two of
them inherited from `aa7b739` rather than introduced here.

**Both files were restored after the two deliberate-breakage runs below, and the
restoration is proved twice: comparing the working tree against the commit prints
nothing, and the files hash to**

```
eba17b9810c70f1e3dab524d353a83661ad87fd8b93d5194ee98eb138e0d1ffe  launch_a3_fetch_first.sh
262db325d4accf4ee85494328eee9eca49592120e0d9b30eca5b4f8c139bd928  sleep_guard_selftest.sh
```

---

## 1. The override no longer fails open

The complaint that produced this fix was that the setting was tested for being
non-empty, so `ALLOW_LAPTOP_SLEEP=0` and `=false` switched the guard off — a person
typing "do not allow" got "allow", on a check whose whole job is to stop money being
spent. It now recognises the single value `1`.

This session wrote its own sweep rather than re-running the test's two cases. The power
reader was pointed at a stand-in reporting a Mac that would be refused (never-sleep
override off), and the launcher's local interpreter at a stand-in that always fails, so
even a guard that let everything through could not have reached a command that spends
money. Thirteen values, each one a real launch, not a preview:

| Value given | What the guard did | Did it say the value was seen and not taken? |
|---|---|---|
| `0` | Refused | Yes |
| `false` | Refused | Yes |
| `no` | Refused | Yes |
| `TRUE` | Refused | Yes |
| `True` | Refused | Yes |
| `1` with a leading space | Refused | Yes — and it quoted the value, so the space is visible |
| `1` with a trailing space | Refused | Yes |
| `01` | Refused | Yes |
| `1.0` | Refused | Yes |
| `yes` | Refused | Yes |
| empty, set explicitly | Refused | No — see below |
| unset entirely | Refused | No — see below |
| `1` | **Overrode**, and said so | not applicable |

Every value that is not exactly `1` refused. Only `1` overrode. In no case did the
launcher reach the step that creates a rented machine — checked on every one of the
thirteen by looking for the line the launcher prints immediately before its first
vendor command, and it never appeared.

The refusal names the value. For the leading-space case it printed:

```
  ALLOW_LAPTOP_SLEEP was set to ' 1', which is not 1,
  so it did not override anything. Only the value 1 overrides this.
```

The quotation marks are doing real work there: a stray space is the one mistake that
would otherwise be invisible in the message meant to explain it.

**The two rows that print nothing are right to.** An empty setting and no setting at all
are the same thing to a shell, and neither is a value somebody typed and had ignored.
Saying "you set it to ''" would be inventing a value to complain about.

**The line is missing from the preview path, though.** A preview on a sleepy Mac with a
mistyped override prints "WOULD REFUSE a real launch" and the fix, and never mentions
that the override was seen and not taken. Nothing is at risk — the preview creates
nothing, and the operator is at least not told the override worked — but the preview is
where somebody checks their spelling, and it is the one place the new sentence does not
reach. Carried as a follow-up.

---

## 2. The two line numbers in the comment, read against the file

The comment explaining why the idle timer is not gated on says the keep-awake cover
begins on line 641 and the rented machine exists from line 404. These numbers have
drifted twice in this chain — 597 and 360 when the comment was first written, 639 and
402 after the comment fix, 641 and 404 after the banner fix moved everything below it
by two lines.

**Both are right as the file now stands.** Read directly, not through the test:

- **Line 641** is `nohup caffeinate -dimsu bash "$SRC_DIR/watch_run_a3.sh" "$ENVF" \` —
  the spawn site, and the only place in the file where the keep-awake command is
  started. The whole file was searched: there is no other.
- **Line 404** is `CREATE_OUT=$(runpodctl pod create --name "mvm-$OUT" \` — the
  machine-creation site. Line 381 also contains those words, but it is inside the
  preview block, printing what a real launch *would* run, and it creates nothing. The
  comment names the real one.

The file is 663 lines, so the cover begins twenty-two lines from the end and the
launch window the comment describes is a little over two hundred lines wide.

**The claim the comment makes about the launch window is true.** Between line 404 and
line 641 the launcher creates the machine, pushes the code, installs and verifies the
restricted key, starts the machine's own shutdown watcher, starts training and checks
it is alive — and nothing in that stretch holds the idle timer off. This Mac's idle
timer really is fifteen minutes on both power sources; that was read, not assumed. The
comment's further claim that closing the window wants a keep-awake command started
before the machine is created, and that this has not been done, is also true as read.

---

## 3. The three new assertions, and whether they detect

The author reports that two of the three checks added to the safe-Mac case are
load-bearing and the third passes under both the old and the new banner, and says so in
the test's own comment.

**Reproduced exactly.** The banner was put back to the old wording —
`not relied on — caffeinate covers idle sleep, the override covers the lid)` — and the
safe-Mac case run on its own:

```
case 0 — negative control: a safe Mac must NOT be refused
    pass: the check passed the safe Mac and said so
    pass: it did not refuse
    pass: the launcher ran on past the check to its dry-run block
    pass: it reported the idle timers it read from 'pmset -g custom'
    FAIL: the banner does not say when the idle-sleep cover starts
    FAIL: the banner does not say the launch window is uncovered
    pass: and that the lid is what the override covers

checks passed: 5   failed: 2
```

Exactly two failed, and they are the two the author names. The third — that the override
covers the lid — passed under the old wording, which is right and is the reason to keep
it: the old line got that one thing correct, and a later shortening should not be free
to drop it. The counts, 5 and 2, match the figures written into the test's own comment
to the digit.

Run whole rather than case by case, the same mutation also fails the comment case, for a
reason worth recording: putting the three-line banner back removes two lines, the two
sites move to 639 and 402, and the comment's 641 and 404 go stale. Four failures in
total, two on the banner and two on the numbers. That is the line-number check doing
precisely what it exists for, on a change nobody made for its benefit.

**A second mutation the author did not run.** The banner is only half of `5913bfa`'s
parentage, so the override fix was tested the same way. The value test was put back to
the old non-empty shape, written to occupy the same four lines so the line numbers were
undisturbed — confirmed: they still read 641 and 404 under the mutation, and the comment
case passed throughout. The whole test then reported 52 passed, 7 failed, all seven in
the override cases:

```
case 5 — ALLOW_LAPTOP_SLEEP=0 must NOT switch the guard off
    FAIL: it never said it was refusing
    FAIL: it ran on past the sleep check to the next precondition
    FAIL: 0 switched the guard off, and the banner contradicted itself
    FAIL: it ignored the value silently
case 5b — ALLOW_LAPTOP_SLEEP=false must NOT switch the guard off
    FAIL: it never said it was refusing
    FAIL: it ran on past the sleep check to the next precondition
    FAIL: an unrecognised value switched the guard off
```

Two things in that run are worth keeping. The control case, which requires `1` to still
work, passed throughout — so the seven failures are about the other values and not about
the override having stopped working altogether. And "it exited 1" passed in both failing
cases, exactly as the test's own comment warns: the launcher still exited 1, a few lines
further down, for a reason with nothing to do with sleep. The assertions that saw the
breakage are the refusal's own words and its position in the script.

**The recorded scores were checked too, rather than taken on trust.** The test's closing
narrative gives four figures. All four reproduce: the original pair of files at `aa7b739`
report 38 passed, 0 failed; the pair at `32472d1` report 56 passed, 0 failed; the pair as
committed report 59 passed, 0 failed; and the safe-Mac case under the old banner reports
5 and 2. The two earlier pairs were run from scratch copies, never in place.

Against the standard in `docs/known-failure-modes.md` — that a test never seen to fail
has not been shown to detect anything — every case added across this chain has now been
watched failing by someone who did not write it.

---

## 4. The gap the author named and left: does it have to be closed first?

The test's closing narrative records its own scores and the two line numbers in prose,
by hand, and nothing compares that prose against what a run prints. It is the same
species as the thing the comment case exists to prevent, one level up: a sentence about
the file that the file does not check.

**Judgment: real, and a follow-up rather than a blocker.** Three reasons, in order of
weight.

First, **nothing in that prose is currently wrong.** All four scores were re-derived
above and all four hold. There is no false claim sitting on the record waiting to be
merged; there is a claim that could go stale later.

Second, **most of it cannot be machine-checked even in principle.** The figures are a
history of runs against deliberately broken versions of the launcher — 29 passed and 9
failed against a launcher downgraded to a warning, 46 and 10 against one with neither fix
applied. Those launchers do not exist in the tree and should not. The only figure a
machine could compare against a live run is the last one, and asserting it would mean the
test checking the arithmetic it has just printed itself, which detects nothing.

Third, **the one genuinely drift-prone sentence is already covered by the thing beside
it.** "They read 641 and 404 today" will go stale the next time the launcher is edited —
but the comment case recomputes those numbers on every run and fails on a mismatch, so a
stale pair in the prose cannot survive a run of the test unnoticed. The sentence also
tells its own reader not to lean on the pair, saying in the same breath that the numbers
are recomputed each time.

If it is closed later, the cheap way is to stop writing the pair down: say "the pair the
comment case prints" and let the run supply it. That removes the only copy that can rot
without changing any of the history, which is the part worth keeping.

---

## 5. Everything re-run

| What was run | Result |
|---|---|
| The sleep-guard test, whole | **59 checks passed, 0 failed**, exit 0 — the count the commit claims |
| The launcher argument-guard check | **21 checks, all pass**, exit 0, including its negative control, which still rejects an unguarded stand-in |
| The shutdown-handshake test | **26 checks passed, 0 failed**, exit 0 |
| The three module self-tests — the curriculum, the encoding, the trainer | All three report OK: the curriculum at 10 turns and chance 0.125, the encoding at 105 tokens against 103 registered, the trainer at its untrained baseline |
| A preview run of the launcher | Exit 0, 37 lines, reported creating nothing and spawning nothing |
| The two earlier versions of the pair, from scratch copies | 38 passed / 0 failed at `aa7b739`; 56 passed / 0 failed at `32472d1` |

The argument-guard check is worth more than its row, for the reason the earlier review
gave: it runs a preview of this launcher against this Mac's *real* settings, and this Mac
is one the guard would refuse. It still exited 0 and still reported creating nothing. So
the carve-out that lets a preview report the problem and carry on is exercised against
the real thing by a check that predates the guard, and both repairs leave it intact.

---

## 6. The finished launcher, read end to end

Four sessions have edited this file. This section is the one nobody has done: reading all
663 lines as a single document and asking whether the parts still agree.

**They do.** The five places that talk about this Mac staying awake say one thing between
them, and it is the true thing:

- The **usage header** offers `ALLOW_LAPTOP_SLEEP=1` and calls it a spending choice
  rather than a technical one, pointing at the block that says what it costs.
- The **carried-over process note** says the launch spawns its watchdog under the
  keep-awake command and to keep this Mac powered on. It claims no more than that.
- The **comment** on the precondition says when the cover starts, that the launch window
  is outside it, that closing that window is a separate change nobody has made, and that
  neither the timer nor the keep-awake command survives the lid coming down.
- The **banner the operator reads** now makes the same two points in three short lines,
  in the same order, using the same words.
- The **refusal**, the **override announcement** and the **override instructions** agree
  with each other: one value overrides, the announcement can therefore only ever print
  `=1`, and the refusal names any other value it was handed.

Searched for leftovers, there are none: the old overstatement "caffeinate covers idle
sleep" survives in exactly four places, all of them inside the test — once as the
corrected statement with the qualifier attached, and three times inside quotation marks
as the wording being described. No document outside these two files mentions the override
at all, except the earlier check, which is a dated record of the file as it stood.

**Two claims from earlier in the chain were re-checked and still hold.** The comment now
says the shutdown-policy setting names one value and sends everything else to the
money-safe branch, and that the override's old non-empty test did the opposite; reading
that setting's own branch at the far end of the file confirms it — it names `laptop-only`
and everything else falls through to the trainer deleting the machine itself. And the
header still says three dated blocks have been added since the file was derived; three is
still the right number, since neither of these two commits added a fourth.

**Two small things are inherited and left standing, neither introduced here.**

The test's opening description says "cases 1 to 4 feed it the unsafe readings and require
a refusal", and that "if any of 1 to 4 ever passes, this harness has stopped measuring".
That is wrong about case 4, whose whole point is that a preview and an announced override
*must* be let through — the case would break if it ever refused. The sentence is
unchanged from `aa7b739` and describes cases 1 to 3b correctly. It is one sentence in a
header, and it is the sort of thing a reader trying to understand the test reads first.

The same description now says "two of the checks are on words rather than on behaviour"
and then names two *cases* holding seven checks between them. Reworded in this commit and
slightly looser than what it replaced. Cosmetic.

**Plain-language reading.** The new text in both files holds up. The banner gives the
plain phrase before the name — "the keep-awake command (caffeinate)" — rather than the
other way round, and the refusals speak in ordinary words. The settings named in messages
are named because an operator has to type them, which is the exception the rule allows.
The line numbers 641 and 404 both arrive attached to a phrase saying what is at them, not
bare. No new shorthand is coined. This page is written to the same rule.

---

## Findings

### Must fix before merge

Nothing. This round found no defect that should hold the merge, and that is the honest
result rather than a shortage of looking: thirteen override values, two deliberate
breakages, four recorded scores re-derived, the two line numbers read against the file by
hand, and the whole 663-line launcher read end to end.

### Can follow

1. **The preview path does not say the override value was seen and not taken.** A preview
   with a mistyped override prints "WOULD REFUSE a real launch" and the fix, and never
   mentions the setting. The real refusal does. Nothing is at risk, but the preview is
   where somebody checks their spelling. Two lines, and a case to go with them.

2. **The test's own closing narrative is hand-maintained and unchecked** — its four scores
   and its pair of line numbers. All of it is accurate today, verified above. The one part
   that can rot without anyone noticing is "they read 641 and 404 today"; the cheapest
   close is to delete the pair and point at what the comment case prints on every run.
   This is the gap the author named and left, and leaving it was the right call.

3. **The test's opening description mis-states what case 4 requires** (see section 6),
   and, since this commit, describes two cases as "two of the checks". Both are in a
   header comment, both are inherited or cosmetic, and one sentence fixes the first.

### Still open from the earlier check, and untouched by these two commits

The earlier review's follow-ups 3 through 8 — a reading that is present but unintelligible
reported as "the override is OFF"; only the first of two problems named when both apply;
a charger that has stopped delivering not caught; the power reader's success-or-failure
report ignored; no time limit on the reading; the power-source pattern grabbing too much —
are all still open. None was in scope here and none was made worse. The charger one
remains the largest of them: it is the one route to a flat battery the guard does not
close, and the guard's own stated reason for requiring wall power applies to it word for
word.

The earlier review's item 9, that `reap-shutdown-order-method.md` invites a comparison
against the derivation script that has failed since 2026-09-22, is also still open and
still not this commit's job.

---

## What this check does not establish

It exercised the guard against stand-ins, never against a Mac in any of the states it
refuses. Nobody put this Mac on battery and nobody turned the never-sleep override on or
off. The one real state exercised end to end is the state this Mac is in — override off,
wall power — which the guard refuses and which the preview reports and carries past.

It did not run the staged slice, create anything, or contact any vendor, and it has not
checked anything on the branch beyond the two files named at the top.
