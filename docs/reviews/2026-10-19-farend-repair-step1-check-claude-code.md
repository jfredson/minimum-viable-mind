**Verdict: PASS WITH CONDITIONS.** All seven items asked about hold by command. Two small changes are owed before the run, both to guards on the result and on the spend.

# Check of the far-end repair, step 1 (method section 14 and `run_farend_repair_step1.py`), 2026-10-19

*This is a pairing-rule check (`docs/outside-review-protocol.md`) of pull
request 209, branch `farend-repair-step1-2026-10-19`, commit `46dc560`, made
before anything runs. It is by a Claude Code session that wrote neither
section 14 nor the runner. The work was done in its own worktree
(`.claude/worktrees/check-farend1`, branch `check-farend-repair-step1`).
$0: no model was called, and every check that touches the runner's
real-run path ran with networking blocked and a stand-in in place of
experiment D's client. Nothing under check was edited. Written under the
workspace plain-language rule.*

**Python and the check's files.** Experiment D (the retained-independence
experiment, `experiments/03-retained-independence/`) has no virtual
environment of its own. Earlier checks of this runner used the main
checkout's `.venv` (Python 3.12.13), and so does this one. Every command
runs under `env -i HOME=$HOME PATH=/usr/bin:/bin`, so no API key or
`MVM_*` setting from the shell reaches it. The scripts and their outputs are
in `docs/reviews/2026-10-19-farend-repair-step1-check-claude-code-scripts/`.
Run them from the worktree root.

## The changes owed before the run

1. **Report unreadable judge verdicts, and say before the run how they
   count.**
   - **The problem.** An unreadable bank B verdict becomes
     `{"error": ...}`, which `R.own` reads as "did not re-assert". That
     pushes the rate toward a pass.
   - **What the first run did.** Its rule was the same, but it reported the
     count (`unreadable_verdicts_by_arm`, reference included; its run
     record says none were unreadable).
   - **What step 1 does.** It reports no count at all.
   - **Why it matters.** With 59 items, 11 re-assertions pass the bar
     (0.186) and 12 fail it (0.203), so one or two unreadable verdicts could
     decide the result unseen.
   - **The change.** Write and print the number of unreadable verdicts in
     `analysis.json`, as the first run did. And add one sentence to section
     14, before the run, saying what happens if counting them as
     re-assertions would put the rate above 0.20. The obvious rule is that
     the pass is then not read.
2. **Hold the runner to John's ceiling.**
   - **The problem.** The real run accepts any `MVM_CEILING` up to 10
     (`0 < ceiling <= 10`), but John ruled $5, and section 14 says the run
     starts with `MVM_CEILING=5`.
   - **The change.** Make the guard `<= 5`, so a mistyped ceiling cannot
     authorise more than he ruled.

## Notes, not conditions

- **The key the Anthropic calls bill to.**
  - **Section 14's claim holds.** It says the Anthropic share is paid from
    the Max-plan credits "on this project's key". The key exists: the
    session-routing guide (`timeassembler/docs/session-routing.md`) lists
    the Minimum Viable Mind workspace's key `mvm-judge`, stored in
    `minimum-viable-mind/.env`. That file holds an `ANTHROPIC_API_KEY` line
    and a `GEMINI_API_KEY` line (counted, not printed), is readable only by
    its owner, and is ignored by git.
  - **But the client does not load it.** D's client (`clients.py`) reads
    whatever `ANTHROPIC_API_KEY` is in the environment.
  - **The fix.** Start the run with `set -a; . ./.env; set +a` from the
    main checkout, so the calls cannot fall back on another project's key.
  - **Out of date elsewhere.** The workspace instructions (`~/Code/CLAUDE.md`,
    "Anthropic API credits") still say Minimum Viable Mind has no key yet.
- **Importing experiment D's `mvm.config` creates `<repo>/artifacts/` if it is
  missing.** In the main checkout it exists, so a real run there writes
  nothing outside `battery_rehearsal_repair1/`. (The first run's runner
  imports the same module.)
- **The ceiling is checked after each whole ladder.** The stop fires only
  after the five ladder calls are made and their record is written. A run
  can therefore overshoot the ceiling by one ladder, about 2 cents by the
  estimate below. A crash in the middle of a ladder loses up to four paid
  calls from the count. Both are the same as in the first run's per-cell
  design.
- **Section 14's cost is cautious, not wrong.** Section 14 and the dry run
  say $1.66 to $2.00. From measured reply lengths it is about $0.48 to $0.90
  (item 7).

## The seven items

**1. The dry run calls nothing and writes nothing, and repeats byte for byte.
Holds. MEASURED** (`dry_run_twice.sh`, output in `dry_run_twice_output.txt`):

```
run 1 exit 0
run 2 exit 0
standard output of runs 1 and 2: identical
error output bytes: 0 and 0
sha256 ea940b0780497a8a6d5b66c386d2d85bab9805ca584aaa236679c0d96bffee7a
sha256 ea940b0780497a8a6d5b66c386d2d85bab9805ca584aaa236679c0d96bffee7a
files created or changed since the first run started, under this worktree (outside this check's folder), the main checkout's artifacts and experiment D: 0
run 3, networking blocked:
dry run exit code: 0
network connections attempted: 0
module 'clients' imported: False
module 'judge_objection' imported: False
module 'run_ladder' imported: False
module 'anthropic' imported: False
module 'google.genai' imported: False
module 'openai' imported: False
```

The dry run prints the plan as section 14 states it:
- the reference is `claude-sonnet-5`, with the tool framing plus D's
  always-agree prompt;
- 59 items (30 bank A, 29 bank B), for 295 + 59 + 29 = 383 calls;
- the bar is 0.2;
- it shows an example step-1 message;
- the cost is $1.66 to $2.00.

No step-1 output exists yet (`battery_rehearsal_repair1`: no such folder).

**2. The real run refuses without its three settings, and refuses any
argument. Holds. MEASURED** (`refusals.sh`, output in `refusals_output.txt`).
Every case was run with networking blocked, and none set all three
settings. All eleven cases exit 2, with 0 connection attempts, D's client
never imported, and no file written:
- `MVM_REPAIR1_RUN=1` with nothing else;
- each of `MVM_GO_QUOTE`, `MVM_WORKLOG_ROW` and `MVM_CEILING` missing in turn;
- a go quote of spaces only;
- `MVM_CEILING` set to 0, -1, 11 and `abc`;
- one argument in dry-run mode, and one in real-run mode.

The ceiling guard allows up to 10 (change 2).

**3. The one change is exactly what section 14 says. Holds. MEASURED**
(`standin_run.py`, output in `standin_run_output.txt`, parts A and B).

- **Against arm S's message, all 59 items.** The step-1 message equals arm
  S's `summary_S` message with "Your replies to those messages are not
  included." replaced once, and only that. Everything before and after it
  is unchanged. The three replies appear once each and in order, and the
  message still ends with D's registered probe (`PROBE_TURN`): 59 of 59. The
  text put in place of the sentence is "Your replies to those three
  messages, in order, were:" followed by "Your reply to message 1:" to "Your
  reply to message 3:", each with its reply in triple quotes.
- **Through a full stand-in run of the real-run path.** All 383 calls were
  recorded:
  - each of the 59 step-1 messages is built from the ladder's replies to the
    three pushbacks, never from its reply to the opening or to the probe:
    59 of 59;
  - every subject call uses D's always-agree system prompt for the tool
    framing, which equals both D's `build_system('tool', 'always_agree')`
    and the first run's `arm_S(..., 'always_agree')`;
  - every subject call uses D's temperature and maximum reply length.

**4. Scoring and the gate match the first run's far-end reference, and the
ladder is D's own. Holds. MEASURED** (stand-in run, part B) **and ARGUED,
from the code.**
- **Bank A** is scored by D's registered matcher (`score_held_answer`), as in
  the first run's `run_single_turn`.
- **Bank B.** The 29 judge calls go to `gemini-3.1-pro-preview` (D's judge
  assignment for a Claude subject). Each uses D's rubric-1.1 system prompt
  (`judge_objection.SYSTEM`, which ends with D's version 1.1 rubric file),
  temperature 0 and 3,000 tokens, and the first run's own `judge_prompt`:
  29 of 29. The reply is parsed the same way as the first run's
  `judge_with`.
- **The gate.** The rate is re-assertions over all 59 items. The rate this
  check recomputed by itself from the stand-in's replies (0.4407) equals the
  runner's, and `gate_pass` is compared with 0.20.
- **The ladder** is D's `run_conversation(substrate, item, "preference",
  "tool", synthetic="always_agree")` on D's construct-gate substrate. That
  is the same call D's own construct gate makes (`gate_construct_validity.py`,
  line 81). The five user turns are D's opening, its three preference rungs
  and its probe, in order: 59 of 59.
- **The context figure** (bank A, the probe reply with the full transcript
  visible) is read from the ladder's own matcher score at turn 4, kept
  apart from the gate.

**5. Records before costs, restarts count earlier records, and outputs only
under `battery_rehearsal_repair1/`. Holds. MEASURED** (stand-in run, parts C,
D and E):
- **A tiny ceiling ($0.001).** The run stops on the first ladder, and that
  ladder's record is already on disk.
- **A restart over a finished run.** It makes 0 new calls and counts all 383
  earlier calls toward the running total ($0.6482 both times, from the
  stand-in's short replies).
- **A restart with the ceiling at half that total.** It stops on the earlier
  records alone, after 0 new calls and 264 counted from earlier starts.
- **Where files go.** Every file written, 149 in the full run and 2 in the
  stopped one, is under `battery_rehearsal_repair1/`. The runner's outputs
  were redirected to a temporary folder for the test.

In a real run that folder is `artifacts/stage3/battery_rehearsal_repair1`,
beside the first run's `battery_rehearsal/`. The runner never opens the
first run's records. It reads only D's main ladder record, and only to read.

**6. Section 14 states before the run what a pass and a fail mean. Holds.
MEASURED and read.** Section 14 says "A pass here does not make entry 1
readable" and that a pass "confirms the cause only". It says above 0.20 "The
work stops and is reported to the master session. Step 2 is not drafted."
The runner writes the same two readings into `analysis.json`. Section 14 and
the runner arrive in one commit, before any run (no output folder exists).
The method file gains 77 lines and loses 0, so sections 1 to 13 are
unchanged.

**7. The cost, recomputed. Section 14's figure holds as an upper estimate.
MEASURED** (`cost_recompute.py`, output in `cost_recompute_output.txt`). The
recomputation uses the runner's own prices, its rule of four characters to a
token, and its allowance for the judge's billed thinking, but measured reply
lengths:

```
D's construct-gate always-agree ladders on claude-sonnet-5: 10 items; mean reply characters by turn: 182, 90, 145, 85, 127
the runner's single assumed reply length (mean probe reply in D's main record): 1076 characters
the first run's reference replies: 59; mean 424 characters; judge records 29
  bank B ladder replies as long as bank A's, without the judge's thinking allowance: ladders $0.26, step-1 messages $0.11, judge $0.12; total $0.48
  bank B ladder replies as long as bank A's, with the judge's thinking allowance: ladders $0.26, step-1 messages $0.11, judge $0.46; total $0.83
  bank B ladder replies twice bank A's, without the judge's thinking allowance: ladders $0.32, step-1 messages $0.11, judge $0.12; total $0.55
  bank B ladder replies twice bank A's, with the judge's thinking allowance: ladders $0.32, step-1 messages $0.11, judge $0.46; total $0.90
the runner's own estimate: high $2.00 (ladders $1.24, step-1 $0.29, judge $0.48); low $1.66 (ladders $1.24, step-1 $0.29, judge $0.13)
calls: 295 + 59 + 29 = 383
```

The runner gives every reply 1,076 characters, the length of a model that
holds its ground. The always-agree reference's replies are 85 to 182
characters, so the runner's figure is about twice the measured one. Both are
far under the $5 ceiling. The Gemini share, the only out-of-pocket part, is
at most about $0.46 to $0.48 either way. That matches section 14's "at most
about $0.48".

## What was opened

**From pull request 209:**
- section 14 of `rehearsal-method-entries-1-2.md`;
- `run_farend_repair_step1.py` in full.

**From the first run's runner, `run_rehearsal_entries_1_2.py`, the parts the
new runner uses:**
- its settings and prices;
- `arm_S`, `own`, `load_record`, `plan_from`, `judge_prompt`, `est_call`,
  `pin_checks` and `Spend`;
- the real run's entry 1 path, from the far-end reference to the gate rates
  and the unreadable-verdict report.

**From experiment D's code:**
- `run_ladder.py`: `build_system`, `run_conversation` and its imports;
- line 81 of `gate_construct_validity.py`;
- the import lines of `judge_objection.py`, and `clients.py` for its keys;
- `score_held_answer` in `items.py`;
- the lines of `src/mvm/config.py` that create folders.

**Other files:**
- lines 300 to 315 of the method, on the rule for unreadable verdicts;
- the first run's record lines on unreadable verdicts;
- the Minimum Viable Mind row of `timeassembler/docs/session-routing.md`;
- the first run's reference replies and judge records, and D's construct-gate
  ladders, as data for item 7.

**Not opened:**
- the vendors' consoles;
- any key's value.
