# Gate C tier 1 review of the successor proposal, version 2 — RT-212 to RT-229

*Written 2026-09-25 (Pacific) by the Claude Code session "MVM W1d Gate C check",
in its own worktree (branch `worktree-w1d-gate-c-check`, cut from main at
`a96f873`). The file name carries the date the session prompt gave it
(2026-09-27); the work ran on the evening of 2026-09-25. Filed under this
experiment's reviews directory because the successor experiment has no
directory of its own yet, and this is the experiment its text most affects
(`docs/outside-review-protocol.md`, "The pairing rule", the filing fallback).*

*Written under the workspace plain-language rule. Every finding is labelled
**MEASURED** (a command was run, and the command and its output are below) or
**ARGUED** (reasoning a reader can dispute), and carries a severity: **fatal**,
**serious** or **minor** (the protocol's "worth-noting"). Findings continue the
red-team ledger's numbering from its last entry, RT-211
(`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`). No ledger
row is written here: rows are written when John rules.*

**Nothing was rented, created or spent: $0.** No registered text, ruling file,
protocol text or proposal text was edited. The two check scripts that execute
launchers were read before they were run: they run the unregistered launchers
with `DRYRUN=1` (preview mode, which stops before creating anything), and read
the registered launcher without running it.

---

## What this review is, and what it opened

**The target.** `docs/successor-experiment-proposal-2026-09-26-v2.md` at commit
`e88c3c0` on branch `worktree-w1d-proposal-v2` (pull request 54): version 2 of
the proposal for the successor experiment, the one that builds systems whose
"degree" (how far the act can be pulled apart from the answer to "which agent
am I") is fixed by construction, and asks whether a transplant-based measure can
tell them apart and then read a freely trained system. Gate C is the review
attached to a proposal before John rules on it (`docs/outside-review-protocol.md`,
"The gates"); tier 1 is the inside pass by a separate session that can run code.

**Opened, in this order.** `CLAUDE.md`; the top entry of `STATUS.md`;
`docs/outside-review-protocol.md` in full; `docs/known-failure-modes.md` in
full; the proposal in full. Then, as records the proposal cites: the rehearsal
repairs of pull request 52 at `e0626b2` (the findings
`docs/2026-09-26-rehearsal-repairs.md` sections 3, 5 and 6, the code
`experiments/rehearsal-successor-measure/src/repairs.py`, `arms.py`,
`transplant.py`, `rehearse.py`, `grammar.py`, and every output file under
`out-repairs/` that a finding below cites); the repairs ruling of pull request
53 at `e03288c` (`docs/rulings/2026-09-25-rehearsal-repairs-rulings.md`); the
second rented slice of pull request 51 at `7da1946` (its findings section 9, its
timing receipt `bench_arms.json`, its `second-release-arithmetic.txt`, and the
compute ledger on that branch); on the main line, the 2026-09-21 rehearsal
findings and its `out/` files, the 2026-09-23 label ruling, the pilot findings,
page 5 of the Weekend 1 queue-ruling proposal, the compute ledger, and the
citation checker.

**Opened late, and said so.** The author's own failure-mode pass
(`…/reviews/2026-09-26-successor-v2-failure-mode-pass-claude-worktree.md`): only
its opening section (lines 1 to 72), to learn the name of the candidate seventh
failure the task pointed at, and its flag of the two discrepancies. None of its
dispositions was read. The pending check of pull request 52
(`…/reviews/2026-09-26-rehearsal-repairs-check-claude-worktree.md` on branch
`worktree-w1c-repairs-check` at `09c91cb`, an interim record): opened **after**
this session had reproduced the two flagged discrepancies and found RT-212, to
see what that check expects to move. It independently reports the free-arm read
near chance and the 8 of 12; both are this session's own measurements below,
and the agreement is noted, not relied on.

**Not opened.** Any chat of any writing session; the grammar-attempt branch; any
vendor.

**How the unmerged records were read.** Each branch was exported whole with
`git archive <commit>` into a scratch folder and read there: `e88c3c0`
(pull request 54), `origin/worktree-w1c-rehearsal-repairs` = `e0626b2`
(pull request 52), `origin/rulings-2026-09-25-repairs` = `e03288c` (pull
request 53), `7da1946` (pull request 51). Paths below that start `out-repairs/`
mean `experiments/rehearsal-successor-measure/out-repairs/` at `e0626b2`;
`$R` in a command is that folder. The scripts this review ran are committed
beside it, in `reviews/2026-09-27-successor-v2-gate-c-scripts/`.

---

## Findings at a glance

| Number | Severity | Label | Brief part | The finding in one line |
|---|---|---|---|---|
| RT-212 | **fatal** | MEASURED | 1, 2 | On arm F, the arm being read, the ownership read never finds its label (at most 0.172 against a no-information 0.072); the free arm's "entangled" reading is an empty instrument, and no rule in the design catches it |
| RT-213 | **serious** | MEASURED | 3, 4 | Arm C fails the learn-both gate on 0 of 3 toy seeds; the proposal omits it, reads the toy as validating the high anchor, and the staggered launch tests only arm F before the second release |
| RT-214 | **serious** | MEASURED | 3 | Control 3, which "holds", fails on arm M seed 1, so under version 2's own rules arm M's ruled pass "on all three seeds" is not met |
| RT-215 | **serious** | MEASURED | 1 | The registered site-set rule was never run: the toy ran 44 site sets from hand-picked layers, 24 of the rule's 60 never ran and 8 of those run are excluded |
| RT-216 | **serious** | MEASURED, ARGUED | 2 | Weakness W7's mitigation is false: most nominations on arms C, F and M sit at layer 0, which is where the acting channel is injected |
| RT-217 | minor | MEASURED | 4 | The $16 wager already loses at the top of arm M's range: $15.95 on the proposal's figures, $14.79 on the ruled split |
| RT-218 | minor | MEASURED | — | Flagged discrepancy 1, resolved: 8 of 12 pairs pick different site sets; 7 of 12 differ in share; the ruling's "7" counts the second |
| RT-219 | minor | MEASURED | — | Flagged discrepancy 2, resolved: 0.6033 is 1,810 of 3,000 gate episodes, 0.60375 is 483 of 800 fresh trials; the proposal's figure is the right one |
| RT-220 | minor | MEASURED | 3 | "All three collapse" under the lesion is false for arm T seed 2 (0.2733); a fully collapsed arm reads "not collapsed" 4.85% of the time per seed |
| RT-221 | minor | MEASURED | 4 | The separation figures 0.9977 and 0.9927 come from site sets the registered rule excludes; under the rule they are 1.0051 and 0.9863 |
| RT-222 | minor | MEASURED | 3 | The 0.0175 allowance was set from a miss of 0.017536, which fails it; near the learn-both bar it detects a broken pairing by 0.0023 |
| RT-223 | minor | MEASURED | 4 | Arm M's "formula" and its true-slot reading are the same number by algebra; the proposal reports one check as two |
| RT-224 | minor | MEASURED | — | The position set registered by name as "the action position and the answer position after it" is the action and the token *before* it |
| RT-225 | minor | MEASURED | 4 | The rider's no verdict on arm M is not "nothing reached the state": there the whole-state transplant moves 0.41 and misses the floor |
| RT-226 | minor | MEASURED | 1 | Two ledger citations point at the wrong row or overstate it: 8.47/2.42 and the "measured" $10.04 |
| RT-227 | minor | MEASURED | — | 34 references to unmerged files: 21 in pull request 52, 9 in 51, 4 in 53; which break if 52 lands changed |
| RT-228 | minor | ARGUED | 1 | "The same launcher" names no file, and arm M's code has never run on the rented machine |
| RT-229 | minor | ARGUED | 4 | Arm M's development run is costed twice, or the first release's development line was widened to four arms without a ruling |

The ruled numbers mostly hold against their files, and so do the repairs of
version 1's two fatal findings (the per-arm ceiling and the empty cell). The
section "What was checked and held" lists them.

---

## The two discrepancies the author flagged, reproduced from the files

### RT-218 (minor, MEASURED). "7 of 12" and "8 of 12" are both counts, of different things

The two readings of "the smallest layer set that clears the floor" are recorded
in each nomination file: `nomination` (for each position set, the fewest-layer
set that clears the four-fifths floor, then the highest ownership-only share
among those) and `sensitivity` (the highest ownership-only share over every
clearing site set). Compared pair by pair:

```
$ python3 reviews/2026-09-27-successor-v2-gate-c-scripts/recount_readings.py $R/
C/base/0   clearing=38 nominated=((0,), 'all', 2) own=0.0550 | other=((0,), 'all', 2) own=0.0550 | site differs=False gap=0.0000
C/base/1   clearing=35 nominated=((0,), 'all', 4) own=0.0567 | other=((0, 1, 2, 3, 4), 'post-identity', 8) own=0.0633 | site differs=True gap=0.0067
C/base/2   clearing=38 nominated=((0,), 'post-identity', 2) own=0.0550 | other=((0, 1, 2, 3, 4), 'post-identity', 2) own=0.0600 | site differs=True gap=0.0050
F/base/0   clearing=35 nominated=((0,), 'post-identity', 2) own=0.0633 | other=((1,), 'post-identity', 1) own=0.0633 | site differs=True gap=0.0000
F/base/1   clearing=35 nominated=((1,), 'action+3', 4) own=0.0500 | other=((1, 2, 3, 4), 'all', 8) own=0.0533 | site differs=True gap=0.0033
F/base/2   clearing=35 nominated=((0,), 'post-identity', 1) own=0.0700 | other=((1,), 'post-identity', 8) own=0.0733 | site differs=True gap=0.0033
M/base/0   clearing=35 nominated=((0,), 'post-identity', 8) own=0.3683 | other=((2,), 'post-identity', 8) own=0.3883 | site differs=True gap=0.0200
M/base/1   clearing=35 nominated=((3,), 'action', 8) own=0.3783 | other=((1,), 'post-identity', 8) own=0.3950 | site differs=True gap=0.0167
M/base/2   clearing=35 nominated=((0,), 'post-identity', 8) own=0.3700 | other=((0, 1, 2, 3, 4), 'post-identity', 8) own=0.3800 | site differs=True gap=0.0100
T/base/0   clearing=44 nominated=((0,), 'action', 8) own=1.0000 | other=((0,), 'action', 8) own=1.0000 | site differs=False gap=0.0000
T/base/1   clearing=44 nominated=((0,), 'action', 8) own=1.0000 | other=((0,), 'action', 8) own=1.0000 | site differs=False gap=0.0000
T/base/2   clearing=44 nominated=((0,), 'action', 8) own=1.0000 | other=((0,), 'action', 8) own=1.0000 | site differs=False gap=0.0000
pairs: 12 | site set differs: 8 | site set or rank differs: 8 | ownership-only share differs: 7 | largest gap: 0.0200
```

**The two readings pick different site sets on 8 of the 12 arm-and-seed
pairs.** On arm F seed 0 they pick different sites that happen to tie exactly
(gap 0.0000), so **the ownership-only share differs on 7 of 12**. That is almost
certainly where "7" came from. But the findings' sentence ("disagree on 7 of the
12 arm-and-seed pairs (last column)") points at a column that lists eight, and
the repairs ruling's item 4 ("differed on 7 of 12 arm-and-seed pairs by 0.02 or
less") inherited the number without the qualifier. "0.02 or less" holds: the
largest gap is 0.0200 (arm M seed 0). The same count with every all-positions
site set removed, which is the widened exclusion John ruled in item 3, comes out
the same way: 8 of 12 differ in site set, 7 of 12 in share, and the widening
moves the nomination on 2 of 12 pairs (arm C seeds 0 and 1):

```
$ python3 reviews/2026-09-27-successor-v2-gate-c-scripts/recount_widened.py $R/ | tail -1
site sets differ: 8 of 12; ownership-only share differs: 7 of 12; nominations changed by the widening: 2 of 12
```

*Disposition.* It changes no ruling. The proposal (section 7.2 item 4) should say
"8 of 12 by site set, 7 of 12 by share" and drop the word "discrepancy". The
repairs ruling's item 4 needs a dated annotation beside it, not an edit. The
pending check of pull request 52 reports the same 8 of 12 independently (its
section 4.1).

### RT-219 (minor, MEASURED). 0.6033 and 0.60375 are both right, on different episodes

```
$ cd $R
$ python3 -c "import json; r=json.load(open('measure_base_M.json'))['arms']['M/base/0']; print(r['fourth_arm']['entangled_share'], r['n_trials'])"
0.60375 800
$ python3 -c "import json; d=json.load(open('gate_base.json'))['runs']; [print(k, d[k]['own_by_route']['entangled_share'], d[k]['n']) for k in sorted(d) if k.startswith('M')]"
M/base/0 0.6033333333333334 3000
M/base/1 0.6033333333333334 3000
M/base/2 0.6033333333333334 3000
```

**0.60375 is 483 of the 800 fresh measurement trials** (`measure_base_M.json`,
field `fourth_arm.entangled_share`). **0.6033 is 1,810 of the 3,000 held-out
gate episodes** (`gate_base.json`, field `runs.M/base/*.own_by_route.entangled_share`).
The share does not depend on training (which items go through which route is
fixed by construction), so it is the same on every seed within each set. The
findings' section 5 prints the gate-episode figure but cites it to
"`measure_base_M.json`" and "the fresh episodes", which is the wrong file and
the wrong episodes. The arm M formula takes its route accuracies from the fresh
episodes, so the right share for it is 0.60375, **which is the one the proposal
uses.** A third share, 0.6450 over 800 self-test episodes, is in
`out-repairs/self-tests.txt` (the arm M self-test). *Disposition:* no change to
the proposal beyond dropping "discrepancy"; the findings' sentence needs
correcting at its check.

---

## Findings

### RT-212 (fatal, MEASURED). On the free arm the ownership read never finds its label, so the free arm's reading is an empty instrument, and nothing in the design says so

*Brief parts 1 (feasibility) and 2 (satisfied by the wrong thing). Failure 2 of
the known-failure list, in its middle limb.*

The nomination step (section 7.2) fits a straight-line read of "which marker
word is the model's own" at the action position, at every layer, and takes its
leading directions as the candidate ownership subspace. How well that read fits
is recorded, per layer, in every nomination file, and **the proposal never
reports it**:

```
$ cd $R && python3 -c "
import json
for f in ('nominate_base_T_C.json','nominate_base_F.json','nominate_base_M.json'):
    for k,r in sorted(json.load(open(f))['arms'].items()):
        print(k, {l:round(v,3) for l,v in r['fit_accuracy']['own'].items()})"
C/base/0 {'0': 0.072, '1': 0.994, '2': 1.0, '3': 1.0, '4': 1.0}
C/base/1 {'0': 0.072, '1': 0.983, '2': 0.967, '3': 0.983, '4': 0.961}
C/base/2 {'0': 0.072, '1': 0.978, '2': 0.983, '3': 1.0, '4': 1.0}
T/base/0 {'0': 1.0, '1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0}
T/base/1 {'0': 1.0, '1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0}
T/base/2 {'0': 1.0, '1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0}
F/base/0 {'0': 0.072, '1': 0.172, '2': 0.144, '3': 0.106, '4': 0.067}
F/base/1 {'0': 0.072, '1': 0.067, '2': 0.117, '3': 0.144, '4': 0.117}
F/base/2 {'0': 0.072, '1': 0.106, '2': 0.139, '3': 0.111, '4': 0.111}
M/base/0 {'0': 1.0, '1': 1.0, '2': 1.0, '3': 0.989, '4': 0.989}
M/base/1 {'0': 1.0, '1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0}
M/base/2 {'0': 1.0, '1': 1.0, '2': 1.0, '3': 1.0, '4': 1.0}
```

(The read is scored on the held-out 30% of the 600 development pairs, per
`repairs.py`, `fit_reads`. 0.072 is what it scores at layer 0 on arms C and F,
where the action position's state carries nothing episode-specific; that is the
no-information level of this read. There are 20 marker words, `grammar.py` line
85.)

And the same on the main line, from the 2026-09-21 rehearsal, so this has been in
a committed record since before the label was ruled:

```
$ python3 -c "
import json
d=json.load(open('experiments/rehearsal-successor-measure/out/nominate.json'))['arms']
for k in sorted(d): print(k, [round(d[k]['fit_accuracy']['marker-word|%d'%l],3) for l in range(5)])" | grep F/
F/0 [0.072, 0.144, 0.1, 0.122, 0.133]
F/1 [0.072, 0.133, 0.128, 0.117, 0.144]
F/2 [0.072, 0.072, 0.078, 0.111, 0.089]
```

**What this means.** On arms T and M the read fits perfectly, because their
ownership slot is literally built from the own marker word's embedding
(`arms.py`, `_own_vec`, lines 156 to 164: a softmax over agents times
`own_marker(tok(agent_marker_tok))`). On arm C it fits at 0.96 or above from
layer 1, because arm C multiplies that same vector into content (`_embed`, lines
171 to 175). On arm F, the arm the experiment exists to read, **the read never
gets above 0.172 at any layer on any of six trained seeds across two
rehearsals**. So the "ownership-only subspace" on arm F is the leading directions
of a read that has not found what it is reading, and transplanting it does
nothing because it holds nothing. That is exactly what the free arm's reading
shows: its ownership-only accuracy equals the untouched rate to the fourth
decimal on two seeds (`measure_base_F.json`, `reading`: 0.0563 against 0.0563,
0.0688 against 0.0688), and the reading is 1.00 to 1.003.

**Arm F computes ownership without representing the label.** It scores 0.5513 to
0.5597 on the own-directed condition against 0.2340 to 0.2383 for the
ownership-blind solver (`gate_base.json`), and it collapses when the acting
channel is removed (0.1760 to 0.1940). ARGUED from `grammar.py`: an own-directed
action can be solved by attending to the value tokens on the turns the acting
channel marked, with no need to know which marker word those turns carry. So
the second clause of the proposal's route sentence (section 7.2 item 1: "which
of the four marker words is the model's own is forced by the loss at the
own-directed action") is false for a freely trained system. The label was ruled
on 2026-09-23 on arm T alone (`docs/rulings/2026-09-23-nomination-label.md`,
section 4: "Every figure in this file comes from the separable arm"), the one arm
whose slot is made of the label by construction.

**Why fatal.** Section 3's admission says a free-arm reading near 1 "cannot be
told from the instrument's ceiling", and "this measure cannot say which". On the
toy it *can* say which, from a number the procedure already computes. As
written, R1's "arm F gets a reading" is satisfied by a read that fits at no
better than chance, and the registered text would report it as a degree. This is
the second limb of failure 2: a working instrument (it recovers the label on T, M
and C) returns nothing on the pre-stated target, which is evidence that the
target is not there to be recovered, not evidence about the system. Failure 2's
own rule is that "the pre-stated target changes before registration, and the null
already collected is withdrawn rather than reported." The pending check of pull
request 52 reaches the same finding independently (its section 6, item 2); this
session found it from the fit accuracies before opening that check.

**What would close it** (for John; the label is his ruling). Either (a) register
a no-verdict rule that the nominated read must clear a pre-stated fit bar on
development episodes on that arm, with the fit accuracies in the reporting
table, so that an arm F whose read fails returns *no verdict*, not a degree near
1; or (b) re-open the label with a quantity the own-directed loss does force on
a free system (for example, which earlier turns' values are the model's own),
tested on arm F at toy scale before Gate A; or both. A closure must show,
MEASURED, that the chosen rule returns no verdict on the committed arm F reads
and a reading on T, C and M.

### RT-213 (serious, MEASURED). Arm C fails the learn-both gate on every toy seed; the proposal leaves this out, and the money guard does not test it

```
$ cd $R && python3 -c "import json; d=json.load(open('gate_base.json')); [print(k, v) for k,v in sorted(d['verdicts'].items())]; print(d['bar']); print({k:d['runs'][k]['other_correct'] for k in sorted(d['runs']) if k.startswith('C')})"
C/base {'learn_both': False, 'other_passes_the_ruled_line': False, 'other_seeds_clearing': 0, 'own_seeds_clearing': 3, 'seeds': 3}
F/base {'learn_both': False, 'other_passes_the_ruled_line': False, 'other_seeds_clearing': 1, 'own_seeds_clearing': 3, 'seeds': 3}
M/base {'learn_both': True, 'other_passes_the_ruled_line': True, 'other_seeds_clearing': 3, 'own_seeds_clearing': 3, 'seeds': 3}
T/base {'learn_both': True, 'other_passes_the_ruled_line': True, 'other_seeds_clearing': 3, 'own_seeds_clearing': 3, 'seeds': 3}
blind/base {'learn_both': False, 'other_passes_the_ruled_line': False, 'other_seeds_clearing': 0, 'own_seeds_clearing': 0, 'seeds': 3}
{'as_a_share': 0.2633333333333333, 'episodes': 3000, 'min_correct': 790}
{'C/base/0': 760, 'C/base/1': 751, 'C/base/2': 708}
```

Arm C's named-other condition scores 760, 751 and 708 correct of 3,000 against a
bar of 790 (`gate_base.json`, `runs.C/base/*.other_correct`). The findings'
section 6.1 table says so ("fails (named-other 0 of 3)"). The proposal does not.
Section 5.2 presents arm C's toy reading as validating the high anchor; R-3 says
"Exercised; the two-arm fallback does not fire"; section 9 says the toy cleared
the separation bar on every seed; and R-1 says the named-other condition fails
"on the free arm", naming no other arm. Section 5.4 says, of arm F only, that the
registered procedure "would not have read it". Section 8.1's rule ("No arm is
read mechanistically until it has learned both conditions") applies to arm C in
the same words.

**Consequences (ARGUED).** (1) Under the design as written, the toy does not
reach R1. Arms C and F both fail the gate, which makes the toy's outcome R3. (2)
The staggered launch (section 11, step 5a) reads the learn-both result of one arm
F run before anything else launches, and sections 3, 11 (S4) and W5 say this makes
"an R3 cost the first release (about $44)". On the toy record, arm C is the arm
most likely to fail (0 of 3 against arm F's 1 of 3), and arm C is first tested
in step 5b, after the second release, $129.90 plus arm M's $32 to $44, has been
drawn. An R3 caused by arm C costs both releases. (3) Arm C's named-other failure
does not touch its reading, which uses only the own-directed action, yet the gate
as written would still make it an R3. Whether a constructed anchor must learn the
named-other condition at all is a design question the proposal never raises.

*What would close it.* Say it in sections 5.2, 10 and 11, with the numbers; state
the cost of an R3 caused by arm C; and either put one arm C run inside step 5a
(about $10.84, the measured-ratio price in `second-release-arithmetic.txt` at
`7da1946`), or gate the constructed arms on the own-directed condition only, with
the reason written down. John's call.

### RT-214 (serious, MEASURED). Control 3 fails on arm M seed 1, so under version 2's rules the arm M pass that was ruled on is not met

Section 7.3 makes control 3 (a random subspace of the same rank at the same
sites) a control that **holds**: "should not produce the donor's action above the
no-transplant rate plus the 0.0175 room", and "a failure means the reading is not
made for that arm". It quotes toy figures for arms T, C and F only.

```
$ python3 reviews/2026-09-27-successor-v2-gate-c-scripts/candidate7.py $R/ | sed -n 1,15p
1. Holding controls (section 7.3): ...
   M0: control 3 0.0125 vs limit 0.0300; control 7 True; reading made: True
   M1: control 3 0.0563 vs limit 0.0350; control 7 True; reading made: False   <-- a holding control fails: no reading
   M2: control 3 0.0125 vs limit 0.0312; control 7 True; reading made: True
2. Arm M pass line (section 5.3): 0.3 <= reading <= 0.7 on EVERY seed, with holding controls applied.
   readings made: [0.5104669887278582, None, 0.5321543408360129] -> pass on every seed: False
```

(All nine T, C and F rows clear their limits; the full output is in the appendix.)
Arm M seed 1's random subspace moves 0.0563 of trials against a limit of
0.0175 + 0.0175 = 0.0350 (`measure_base_M.json`, `controls.3`,
`accuracy_untouched`). Under the rules this proposal registers, arm M gets no
reading on seed 1, and the pre-stated pass that John folded arm M in on,
"between 0.3 and 0.7 on all three seeds" (repairs ruling item 2; queue ruling page
5), is not met. ARGUED as a likely cause: seed 1 is the one seed whose nomination
sits at layer 3 (the action position), and arm M's state carries arm T's slot as a
few dimensions that a random rank-8 subspace can partly overlap. If so, the limit
is wrong for arms with a small slot, not arm M. Either way, the ruling rests on a
pass the design's own rules would not give. *What would close it:* report control
3 on arm M, and either justify the limit or change it before Gate A, with the
toy result under the new limit.

### RT-215 (serious, MEASURED). The site-set rule being registered was never run, even at toy scale

Section 7.2 item 2 registers the site list as a rule: every contiguous set of the
model's running states, times four named position sets. Section 7.4 freezes it.
The toy never ran that rule.

```
$ grep -n -E '^LAYER_SETS|^POSITION_SETS|^assert len\(SITE_SETS\)' experiments/rehearsal-successor-measure/src/repairs.py   # at e0626b2
198:LAYER_SETS = RH.CANDIDATE_LAYER_SETS       # the rehearsal's nine
199:POSITION_SETS = RH.CANDIDATE_POSITIONS     # the rehearsal's five
204:assert len(SITE_SETS) == 44 and FAMILY_SIZE == 176, (len(SITE_SETS), FAMILY_SIZE)
$ python3 -c "
def contiguous(n): return [tuple(range(a,b+1)) for a in range(n) for b in range(a,n)]
hand=[(0,),(1,),(2,),(3,),(4,),(3,4),(2,3,4),(1,2,3,4),(0,1,2,3,4)]
P4=['action','action+ans','action+3','post-identity']
for name,n in (('toy (embedding + 4 blocks)',5),('registered (embedding + 12 blocks)',13)):
    L=contiguous(n); print(f'{name}: {len(L)} contiguous layer sets; x 4 position sets = {len(L)*4} site sets; x 4 rank caps = {len(L)*16} comparisons')
ran=[(l,p) for l in hand for p in P4+['all'] if not (l==(0,1,2,3,4) and p=='all')]
reg=[(l,p) for l in contiguous(5) for p in P4]
print('toy family as run in repairs.py:', len(ran), 'site sets')
print('toy family under the registered rule:', len(reg), 'site sets')
print('registered-rule site sets the rehearsal never ran:', len(set(reg)-set(ran)), sorted({l for l,p in set(reg)-set(ran)}))
print('site sets the rehearsal ran that the registered rule excludes:', len(set(ran)-set(reg)))"
toy (embedding + 4 blocks): 15 contiguous layer sets; x 4 position sets = 60 site sets; x 4 rank caps = 240 comparisons
registered (embedding + 12 blocks): 91 contiguous layer sets; x 4 position sets = 364 site sets; x 4 rank caps = 1456 comparisons
toy family as run in repairs.py: 44 site sets
toy family under the registered rule: 60 site sets
registered-rule site sets the rehearsal never ran: 24 [(0, 1), (0, 1, 2), (0, 1, 2, 3), (1, 2), (1, 2, 3), (2, 3)]
site sets the rehearsal ran that the registered rule excludes: 8
```

The proposal's counts are right: 60 site sets and 240 comparisons on the toy,
364 and 1,456 on the registered model (section 7.2 item 2). What is not true is
that the rule has been exercised. Every toy nomination, reading, rider and
control figure the proposal quotes came from a 44-set family, a hand-picked
subset of the layer sets plus the all-positions sets the rule now excludes.
ARGUED: the difference may not matter, because every toy nomination is a single
layer and every single layer is in the hand list. But the smallest clearing
layer set for a position set where no single layer clears could now be one of the
six two-to-four-layer sets never tried, and the sensitivity row certainly can
change. The protocol is explicit: "A pre-stated quantity with no rehearsal line
covering it is a fatal finding on its own" (`docs/outside-review-protocol.md`,
the rehearsal section). At this gate that makes it serious; **at Gate A it is
fatal unless the rule is run.** The fix costs $0: re-run the nominate and measure
stages at toy scale with the rule, which can ride on the R-1 to R-6 re-run that
section 4.4 already plans if the grammar attempt clears.

*Beside this, for the ruling file and not the proposal:* the repairs ruling's
item 3 widens the exclusion and in its next sentence prints 296 and 1,816 as
"the site count". Those are the counts under the old, narrow exclusion
((15 × 5 − 1) × 4 = 296; (91 × 5 − 1) × 4 = 1,816). The proposal handles this
correctly, by calling them "the ruled figures before the widening". The ruling
needs an annotation. The pending check of pull request 52 found the same thing
(its section 5).

### RT-216 (serious, MEASURED and ARGUED). Weakness W7's mitigation is contradicted by where the nominations sit

W7 names the objection the closed design registered against itself: the
nomination might find "the acting channel's own trace rather than anything the
network built". Its mitigation ends: "at the first layer at the action position,
which is where arm T's slot sits, the other arms show nothing, so their nominated
sites are downstream of the acting channel's injection and not at it."

Where the acting channel is injected (MEASURED, by reading the code):

```
$ sed -n 166,171p experiments/rehearsal-successor-measure/src/arms.py   # at e0626b2
    def _embed(self, b, own_vec) -> torch.Tensor:
        S = b["tokens"].shape[1]
        pos = torch.arange(S, device=b["tokens"].device)
        x = self.tok(b["tokens"]) + self.pos(pos)[None]
        x = x + self.act_vec[None, None] * b["acting"].float().unsqueeze(-1)
```

Layer 0 in the transplant code is the state `_embed` returns (`forward`, lines
196 to 205), so **layer 0 is the injection**, at every position where the channel
fires. Where the nominations sit, under the widened rule (`recount_widened.py`
output in the appendix): arm C seeds 1 and 2, arm F seeds 0 and 2, and arm M seeds
0 and 2, **six of the nine**, are layer 0 at "post-identity" (every position from
the model's first own turn to the action). That set spans exactly the turns
where the channel was injected. The twins differ *only* in the acting channel
(`arms.py` self-test, "twins differ only in the acting channel"), so at layer 0
the whole-state transplant is a transplant of the acting channel's input, and the
subspace compared against it is, on arms C and F, a read fitted at 0.072 (RT-212).
ARGUED: the nomination rule's tie-breaks (fewest layers, earliest layers first)
send the nomination to layer 0 whenever no subspace moves anything, which is
exactly the case on arms C and F. The rider's no verdict at the *action* position
says nothing about these other positions.

*What would close it.* Strike W7's last sentence. Say plainly that on the toy
most nominations sit at the injection. Decide before Gate A whether layer 0 is a
candidate at all, or whether a layer-0 nomination is reported as "at the acting
channel" and not as a reading.

### RT-217 (minor, MEASURED). The $16 wager is already lost at the top of arm M's range

Section 12.8 wagers that the twelve runs "complete inside the $450 envelope …
with at least $16 left".

```
$ python3 reviews/2026-09-27-successor-v2-gate-c-scripts/candidate7.py $R/ | tail -5
6. The wager (section 12.8): at least $16 left of $450.
   note split, as the proposal carries it, arm M $32: left $27.95  meets $16: True
   note split, as the proposal carries it, arm M $44: left $15.95  meets $16: False
   ruled split, arm M $32: left $26.79  meets $16: True
   ruled split, arm M $44: left $14.79  meets $16: False
```

Spent $228.15 (the ledger's second 2026-09-25 row, `compute-ledger.md` at
`7da1946`, line 95); both releases $161.90 as the note computed them
(`second-release-arithmetic.txt`), or $44 + $119.06 = $163.06 on the split as
ruled (section 12.4's own sentence); arm M $32 to $44. The proposal's own "about
$16 to $28" rounds $15.95 up to the wager's floor. On the ruled split, which the
proposal says is "the same money as ruled", the top of the range leaves $14.79.
*Fix:* state the wager on the ruled split and against the range, or lower the
floor to what the plan can actually meet.

### RT-220 (minor, MEASURED). The lesion description is wrong for arm T seed 2, and the collapse rule misfires at its own design rate

Section 8.2: arms T, C and M's lesion results "are computed and reported as a
description … (on the toy: all three collapse …)". From `gate_base.json`:

```
5. The lesion description (section 8.2): "all three collapse" (arms T, C, M) on the toy.
   arm T: [True, True, False] [0.2467, 0.251, 0.2733]
   arm C: [True, True, True] [0.178, 0.183, 0.1703]
   arm M: [True, True, True] [0.223, 0.219, 0.2203]
```

Arm T seed 2's lesioned own-directed accuracy, 0.2733 (820 of 3,000), is above the
bar, so under the rule section 8.2 registers it did not collapse. Separately,
because the collapse line *is* the learn-both bar, it sits just above the level a
fully collapsed arm is expected to reach:

```
smallest count k with P(X>=k | n=3000, p=1/4) <= 0.05: 790  share 0.2633  tail 0.0485  tail at k-1 0.0529
P(an arm whose own-directed accuracy is exactly 1/4 scores >= 790, i.e. is read as NOT collapsed) = 0.0485
```

(Two lines of the output of the exact-binomial command printed in full in the
appendix.) This reproduces the bar: 790 of 3,000, a
share of 0.2633. It also shows that an arm F whose lesion drops it exactly to
one in four is read as "not collapsed", and so is not read at all, 4.85% of the
time per seed. ARGUED: section 8.2 does not say whether arm F is read when one
seed of three fails to collapse. On the toy, arm F's lesion falls well below one
in four (0.1760 to 0.1940), so it did not bite there.

### RT-221 (minor, MEASURED). The separation figures quoted come from site sets the rule now excludes

Section 9 quotes the toy separation as 0.9977, 0.9927 and 1.0000
(`summary_base.json`, `separation`: reproduced). On seeds 0 and 1 those are arm C
readings at layer 0 over **every position**, which is exactly the site set the
repairs ruling's item 3 excludes. Under the widened rule
(`measure_base_T_C.json`, `sensitivity_without_all_positions.reading.degree`),
arm C reads 1.0051, 0.9863 and 1.0000, so the separation is 1.0051, 0.9863 and
1.0000. It still clears 0.5. The same applies to arm C's "0.99 to 1.00" in
section 5.2, which becomes 0.99 to 1.005. *Fix:* quote the figures the rule
produces, and label the old ones as coming from the pre-widening family.

### RT-222 (minor, MEASURED). The 0.0175 allowance fails the case it was set from, and is thin near the bar

Section 6.4 gives the no-transplant rule room "for a miss of up to 0.0175 …, the
largest miss the rehearsal measured". That miss was 0.07625 − (1 − 0.589)/7 =
**0.017536** (`out/denominator_floor.json`, arm F seed 2), which is more than
0.0175, so under the rule as worded the case the allowance was set from is
flagged as a suspect pairing. Separately, if a pairing is broken so that the
donor's answer is unrelated to the recipient, an untouched model hits it one time
in eight, and the rule's miss is 1/8 − (1 − p)/7:

```
own-directed accuracy 0.2633: formula 0.1052, broken-pairing rate 0.1250, miss 0.0198, flagged by the 0.0175 room: True
own-directed accuracy 0.5600: formula 0.0629, broken-pairing rate 0.1250, miss 0.0621, flagged by the 0.0175 room: True
```

So the rule catches a broken pairing on the broken end and passes on the working
end, as the proposal says. But near the learn-both bar it does so by 0.0023. On
the repairs' fresh episodes every miss is inside 0.0132 (`controls_table.py`
output: "largest no-transplant miss across all 12 pairs: 0.0132"), so the toy is
nowhere near the edge. *Fix:* write the allowance as 0.018, or as "at most the
largest measured miss, rounded up", and print the detection margin at the bar.

### RT-223 (minor, MEASURED). Arm M's formula and its true-slot reading are one number, not two checks

```
$ cd $R && python3 -c "import json; d=json.load(open('measure_base_M.json'))['arms']; [print(s, 'formula %.4f'%d['M/base/'+s]['fourth_arm']['predicted_from_route_accuracies'], ' true slot %.4f'%d['M/base/'+s]['oracle_reading']['degree'], ' blind %.4f'%d['M/base/'+s]['reading']['degree']) for s in '012']"
0 formula 0.4895  true slot 0.4895  blind 0.5105
1 formula 0.4572  true slot 0.4572  blind 0.4846
2 formula 0.4904  true slot 0.4904  blind 0.5322
```

They agree to four decimals on every seed, and by algebra they must. Whole-state
is (1 − p)·a_T + p·a_C, untouched is (1 − p)·u_T + p·u_C, and a true-slot
transplant that carries the separable route fully and the entangled route not at
all gives (1 − p)·a_T + p·u_C. Put into the chance-corrected form, that is the
formula of section 5.3. Section 5.3 reports "within 0.02 to 0.04 of the formula",
and section 7.2 item 6 reports "arm M's true-slot reading was 0.4572 to 0.4904
against its blind 0.48 to 0.53". These are the same comparison twice. What it
shows is real: the blind nomination finds about what the true slot gives, and
catches 0.9211 to 0.9590 of the separable route's effect (`fourth_arm.ownership_only_by_route`).
But it is a check of the nomination against the construction on the same
episodes, not a prediction made in advance. *Fix:* say that the formula is the
true-slot reading written in route accuracies.

### RT-224 (minor, MEASURED). One position set is described backwards

Section 7.2 item 2 registers the position sets "by name". The second is
described as "the action position and the answer position after it". In the code
it is the action position and the one before it:

```
$ sed -n 84,85p experiments/rehearsal-successor-measure/src/transplant.py
    if which == "action+ans":
        return (idx == ap[:, None]) | (idx == (ap - 1)[:, None])
$ sed -n 18p experiments/rehearsal-successor-measure/src/grammar.py
  `<act> revise <who> <item> <ans> <mask>`:
```

The action position is the `<mask>`; the position before it is the `<ans>`
token. Nothing comes after the action inside the turn. *Fix:* "the action
position and the answer-marker token just before it".

### RT-225 (minor, MEASURED). The rider's no verdict on arm M has a different cause from the one given

Section 7.2 item 7 and W2 say the rider returned no verdict for arms C, F and M
because "at the first layer, at the action position, nothing about ownership has
yet reached those arms' running states". True for C and F, where the whole-state
transplant at arm T's site set lands on the untouched rate. Not true for M:

```
4. The rider (section 7.2 item 7): a reading at arm T's site set for every arm and seed.
   arm C: ['no verdict', 'no verdict', 'no verdict']; whole-state at that site [0.0512, 0.0488, 0.06]
   arm F: ['no verdict', 'no verdict', 'no verdict']; whole-state at that site [0.0587, 0.0563, 0.0688]
   arm M: ['no verdict', 'no verdict', 'no verdict']; whole-state at that site [0.4088, 0.4138, 0.41]
```

Arm M carries arm T's slot, so the transplant there moves the separable route's
two fifths. The rider returns no verdict because that misses the four-fifths floor
(`rider_at_arm_T_site_set.reading.floor.clears: false`). The pending check of pull
request 52 notes the same (its section 5). *Fix:* one clause.

### RT-226 (minor, MEASURED). Two ledger citations point at the wrong row or overstate it

- Section 12.5 attributes "8.47 billed against 2.42 existed" to "the ledger's
  2026-08-07/08 row". That row (`compute-ledger.md`, line 78) carries neither
  number. They are in the ledger's note at line 423 and in the 2026-09-21 row
  (line 93), both describing that row:
  `grep -n -F 2.42 compute-ledger.md` → lines 93 and 423 only.
- Sections 12.3 and 12.4 call $10.04 "the measured cost of a registered-size run
  … (the ledger's 2026-09-17 row: $20.08 for two runs)". The row says the $20.1
  was "COMPUTED FROM MEASURED POD LIFETIMES, not balance-confirmed", and gives
  the working: "20.28 pod-hours at $0.99 = $20.08" (line 88). It is a lifetime
  times a rate, not a billed figure. *Fix:* "the lifetime-priced cost".

### RT-227 (minor, MEASURED). The 34 references to files on unmerged branches, and which of them a changed pull request 52 would break

```
$ .venv/bin/python scripts/check_citations.py --only docs/successor-experiment-proposal-2026-09-26-v2.md   # in the export of e88c3c0
[CONFIDENT] 34 reference(s) name a file that is not in the repository
```

Sorted by the branch each file lives on:

- **Pull request 53 (the repairs ruling), 4 references**, at proposal lines 35,
  235, 1073 and 1771.
- **Pull request 51 (the second rented slice), 9 references**, at lines 37 (two),
  541, 1081, 1149, 1334 (two: the note and `second_release_arithmetic.py`), and
  1786 (two).
- **Pull request 52 (the rehearsal repairs), 21 references**, at lines 36, 219,
  235, 359, 371, 426, 452, 488 (two: `arm_middle.py` and the method note), 510,
  518, 560, 764 (`repairs.py`), 883, 1012, 1071, 1088 (three: the findings,
  `src/repairs.py`, `out-repairs/`), and 1780 (two).

Laying each branch's files over the export and re-running:

```
$ (in the export of e0626b2 with the proposal from e88c3c0 laid over it) .venv/bin/python scripts/check_citations.py --only docs/successor-experiment-proposal-2026-09-26-v2.md --part paths
[CONFIDENT] 13 reference(s) name a file that is not in the repository
$ (in the exports of e88c3c0, e0626b2, e03288c and 7da1946 laid together, e88c3c0 last) the same command
[CONFIDENT] 0 reference(s) name a file that is not in the repository
```

So **if pull request 52 lands unchanged, all 21 of its references resolve**, and
with 51 and 53 landed too, none is left. The path half of the check cannot see
whether a *changed* pull request 52 would break a citation, because it checks
only that a file exists. Which of the 21 would break, by what they depend on
(ARGUED from the pending check's stated plan to re-run the rehearsal from clean,
and from the 2026-09-22 finding that arms C and F do not reproduce from code and
seed):

- **Break on any re-run whose outputs replace the committed ones, because arms C,
  F and M do not reproduce:** lines 219 (arm F 1.00 to 1.003), 235 and 359 (0 of 3
  seeds under each redesign, against 1 of 3, a count of free-arm seeds), 452 (arm C
  0.99 to 1.00, 0.052 to 0.060 against 0.50 to 0.59), 518 (arm M 0.48 to 0.53, the
  misses, the gate ranges), 560 (arm F fails, 1 of 3), 883 (control 1's ranges on
  C, F and M) and 1071 (separation 0.9977 and 0.9927). Eight citations. Most of
  the proposal's other arm C, F and M figures cite "the repairs findings, section
  N" with no path, so the checker does not count them (sections 7.2 items 4, 6
  and 7; 7.3 items 2, 3, 4 and 6; 8.1; 9's uncertainty row; W2, W7 and W11). They
  break the same way.
- **Break only if the flagged discrepancies are corrected in the findings text:**
  line 488 (the findings' 0.6033, RT-219) and section 7.2 item 4's "7 of 12"
  (RT-218, not a path).
- **Stable against a re-run, because they do not depend on training that fails
  to reproduce:** line 371 and 426 (arm T, which reproduces exactly), 1012 (the bar,
  790 of 3,000, which is arithmetic), 510 (the method note's formula, committed
  before the run), and the existence-only pointers at 36, 764, 1088 and 1780.
- **Break if pull request 52 is squash-merged, as the recent pull requests on
  main have been** (`git log --format='%h %p %s' -6 main` shows single-parent
  commits for pull requests 45 to 50): every "at `e0626b2`" anchor then names a
  commit that is on no main-line history, reachable only from the branch and the
  pull request's own reference. This is the form of `RT-145` (a registration
  resting on a record its reader cannot open) and it matters at Gate A, not here.
  The same holds for "at `7da1946`" (pull request 51). *Fix at version 3:* cite
  the main-line merge commit once each lands.

### RT-228 (minor, ARGUED). "The same launcher" names no file, and arm M has never run on the far end

Section 5 says all four arms train "with the same launcher, watchdog and network
volume". The only registered launcher is `launch_a3.sh`, which the
argument-guard check still prints as REGISTERED TEXT with NO argument handling,
under a standing prohibition (its output is in the appendix). The unregistered
`launch_a3_fetch_first.sh` carries the guard and the hang fix. The successor has
no training entry point for arms T, C and M on the rented machine yet. Failure 6's
discipline ("before a remote step is counted as tested, say what stood in for the
far end") applies to arm M in particular: its code (`arm_middle.py`) has only run
on this laptop, and the slice timed arms T, C and F only
(`bench_arms.json` at `7da1946` holds three arms). *Fix:* name the launcher file
in the registration, and list arm M's code on the rented machine as untested,
next to the handshake's machine half (W9).

### RT-229 (minor, ARGUED). Arm M's development run is costed twice, or the first release was widened without a ruling

Section 11 step 4 and section 12.3 put "four arms, one seed each, at the
10-million size" in the first release's development line, up to $10, as ruled on
2026-09-21 for three arms. Section 12.4 separately adds "about $1.94 for one
development run at the 10-million size" to arm M's $32 to $44 in the second
release. Either that $1.94 is counted twice, or the first release's development
line now buys a fourth arm it was not ruled for, and arm M's development run
launches in step 4, before the second release that is meant to pay for it. At
$1.94 against the $10 line (the ledger's 2026-08-12 reconciliation, "A1 10M row
trues up to $1.943", lines 393 and 400) the money is small. The ordering is the
point. *Fix:* one sentence saying which release pays for it.

---

## The failure-mode pass, entry by entry

The list (`docs/known-failure-modes.md`) has six entries on main at `a96f873`,
and the author's pass names a seventh candidate, drafted in
`docs/2026-09-25-rented-slice-attempt-2-findings.md` at `7da1946`, section 9
item 2. All seven were run here with this session's own commands.

**1. A comparison whose denominator was zero. Does not fire. MEASURED.** Part one
asks whether the ceilings typed in trace to committed measurements. The
untouched rate is measured on every arm and seed (`measure_base_*.json`,
`reading.accuracy_untouched`), not assumed. Part two asks for the denominator and
the top of the scale when the target is absent:

```
$ python3 reviews/2026-09-27-successor-v2-gate-c-scripts/fm1_denominators.py $R/
arm/seed    untouched  whole   own-acc | denominator  floor-needs | top of scale: registered  version-1
C/base/0    0.0512    0.5850  0.5487 |  0.5337       0.3980    |  1.0000                  0.9124
C/base/1    0.0488    0.5613  0.5813 |  0.5125       0.4260    |  1.0000                  0.9131
C/base/2    0.0600    0.5025  0.5525 |  0.4425       0.3940    |  1.0000                  0.8806
T/base/0    0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000                  1.0000
T/base/1    0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000                  1.0000
T/base/2    0.0000    1.0000  1.0000 |  1.0000       0.8000    |  1.0000                  1.0000
F/base/0    0.0587    0.4850  0.5587 |  0.4263       0.4000    |  1.0000                  0.8789
F/base/1    0.0563    0.5675  0.5663 |  0.5112       0.4080    |  1.0000                  0.9009
F/base/2    0.0688    0.4913  0.5563 |  0.4225       0.3900    |  1.0000                  0.8601
M/base/0    0.0125    0.7887  0.8712 |  0.7762       0.6870    |  1.0000                  0.9842
M/base/1    0.0175    0.7475  0.8800 |  0.7300       0.6900    |  1.0000                  0.9766
M/base/2    0.0138    0.7913  0.8712 |  0.7775       0.6860    |  1.0000                  0.9826
```

The smallest denominator is 0.4225 (arm F seed 2). The top of the scale is 1.0000
on every arm under the registered form, against 0.8601 to 1.0000 under version
1's. **The repair of the per-arm-ceiling finding (RT-172) holds on the measured
data.** One thing to watch, ARGUED: on arm F the denominator clears the floor by
only 0.026 to 0.10.

**2. A probe target that cannot be recovered in principle. Fires. MEASURED.**
Part one, the route-sentence search, with the proposal's own wording in the
pattern:

```
$ python3 reviews/2026-09-27-successor-v2-gate-c-scripts/fm2_fm4_sweeps.py docs/successor-experiment-proposal-2026-09-26-v2.md | sed -n 1,6p
failure 2, part one: 5 route sentence line(s)
   773: 1. **The label, and its route to the states.** The straight-line read is
   774: fitted against **which marker word is the model's own**. *The route by
   776: marker word is the input token at every turn the model's own assignments
   777: are spoken on, so it is carried by the token into the running state, and
   778: which of the four marker words is the model's own is forced by the loss at
```

A route sentence exists. Part two, the two runs: the committed fit accuracies
serve as the positive control and the target run on the same instrument. The read
clears on arms T, M and C (1.0, and 0.96 or above from layer 1) and returns
nothing on arm F (at most 0.172). That is the middle limb: "the second run clears
the bar and the first does not". **RT-212.** The loss clause of the route sentence
fails on arm F (arm F solves own-directed at 0.55 to 0.57 without the label).

**3. A cell that is empty by construction. Does not fire on the reading; its
test's third part fires on thresholds. MEASURED.** Part one, the cells: control
6's two cells hold 81 and 719 trials on every arm and seed of the relaxed set
(`controls_table.py`: "6a same-value cell: trials: 81 … 6b … 719"), so the RT-173
repair holds. Control 2's cell on arms T and M has zero clearing site sets by
construction, which the repairs ruling's item 5 records as not applicable, with
its reason. Part three, thresholds at both ends: the no-transplant rule fires on
the broken end and passes on the working end, though thinly near the bar
(**RT-222**). The lesion collapse line misfires 4.85% per seed on a fully
collapsed arm (**RT-220**). Control 3's limit vetoes arm M seed 1 (**RT-214**).

**4. A claim of measurement with no record, or a record that does not reproduce.
Fires. MEASURED.** Part one:

```
failure 4, part one: word sweep 373 lines; number sweep 112 lines; either 444 lines of 1818
lines carrying the word MEASURED: 33; ARGUED: 8
```

Part two was run on every MEASURED claim the proposal takes from the repairs, the
2026-09-21 rehearsal, the pilot, the slice and the ledger (listed under "What was
checked and held"). It fires on: "7 of 12" (**RT-218**), the findings' 0.6033
(**RT-219**), "all three collapse" (**RT-220**), the separation figures' site sets
(**RT-221**), the rider's cause on arm M (**RT-225**), two ledger citations
(**RT-226**), and the arm C gate omitted from a sentence that reports the gate
(**RT-213**). The citation checker's figure half, run over all three branches laid
together, flags only 0.6033 (a CONFIDENT finding) and 0.2633 (an approximate
match, which is right: 790 / 3,000 = 0.26333). That shows how little of this
document the checker can see, not that the rest is clean.

**5. A command that creates something while documented as creating nothing. Does
not fire on anything this document runs; one gap. MEASURED.** The proposal runs
nothing and contains no command. Before running the guard check, this session read
each unregistered launcher's dry-run exit against its first vendor command. In
all three, the first `runpodctl` line is inside the dry-run's printed text
(`launch_a3_fetch_first.sh` lines 337 to 340; `launch_ctl_pilot.sh` 216 to 219;
`launch_pilot_a1.sh` 114 to 117), and nothing before the exit reaches a vendor.
Then:

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
  [ ok ] launch_a3_fetch_first.sh guard (line 121) precedes any vendor command (line 340)
  [ ok ] launch_ctl_pilot.sh guard (line 93) precedes any vendor command (line 219)
  [ ok ] launch_pilot_a1.sh guard (line 48) precedes any vendor command (line 117)
  ... (every line ok; full output in the appendix)
  [ ok ] launch_a3.sh does NOT carry the guard, which is expected before Gate A
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
all checks pass. nothing was created and nothing was spent.
exit 0
```

The guard lines have moved since the list printed them (104, 87 and 42 there), as
the list says to expect. The gap is **RT-228**: the design names no launcher file,
and the only registered one is unguarded.

**6. A remote step tested only against stand-ins. The launcher's check passes;
the design has two such steps. MEASURED.**

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)
  [rejected] stand-in line 1: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang
all checks pass. Nothing was rented and nothing was spent.
exit 0
```

On the design: the handshake's machine half has been tested only against
stand-ins, which the proposal says openly (W9, decision 18). Arm M's code has
never run on the rented machine, which it does not say (**RT-228**). The tripwire
(the billing check of section 12.5) does not exist as code yet, so it has not been
tested against anything. The proposal says the code is owed before step 5a. By
failure 6's own standard, that step is untested until it has met the real billing
rows.

**Candidate 7. An outcome line a plan states in advance that the design cannot
produce on the path it expects. Fires on four lines. MEASURED.** The drafted
test: for each pre-stated line, name the code path that prints each signal it
needs, and show that path can run in the order the line requires. Run on the
committed toy outputs (full output in the appendix):

- **The rider** (section 7.2 item 7) can produce a reading on arms C, F and M on 0
  of 9 arm-and-seed pairs on the path it expects. The proposal accepts this and
  reframes "no verdict" as the report, which is a fair disposition.
- **Arm M's pass line** ("on every seed"), together with control 3 holding, cannot
  be produced on the toy's path: seed 1 gets no reading (**RT-214**).
- **The lesion description** "all three collapse" is not what the path produced
  (**RT-220**).
- **The $16 wager** is not produced by the plan's own top figure (**RT-217**).

It also shows R1's precondition, every carried arm passing learn-both, failing
on arms C and F on the toy (**RT-213**). Whether the candidate is a new species or
an instance of failure 3 is John's ruling. On this evidence it catches things
failure 3's test does not, because failure 3 counts trials in cells, and none of
these four is a cell.

---

## The arithmetic of both releases, against the ledger (MEASURED)

| Figure in the proposal | Source read | Result |
|---|---|---|
| Spent $228.1 on main | `compute-ledger.md` at `a96f873`, line 94, "After this run": "programme about **$228.1 / $400**" | holds |
| Spent $228.15; A3 $46.75; balance $75.8645; rehearsal line $9.43 left | the same file at `7da1946`, line 95 | holds ($75.864512286 at 01:54:04Z, as section 12.6 says) |
| Rehearsal spent about $0.57 | $0.02 (line 93) + $0.4974 (line 94) + $0.0525 (line 95) = $0.5699 | holds. The vendor now shows the 2026-09-21 machine at $0.0077 (line 94's parenthesis); immaterial |
| Headroom $221.85 | 450 − 228.15 | holds |
| Seconds per step 13.08 / 13.52 / 12.53 ms; ratios 1.044 / 1.080 / 1.000; 50 steps | `bench_arms.json` at `7da1946` | holds; slowest step within 2.9% of the median on arm C (13.90 against 13.51), which bears out W8's "within 3%" |
| Per run $10.48 / $10.84 / $10.04 | $10.04 × ratio, `second-release-arithmetic.txt` | holds (but "measured cost": RT-226) |
| Eight runs $84.06 | $10.04 × (2 + 3 × 1.0443 + 3 × 1.0798) = $84.057; with the rounded per-run figures it is $84.04 | holds to rounding |
| Second release $129.90; both $161.90 | 84.06 + 10.84 + 12 + 23; + $32 | holds |
| Ruled split $44 + $119.06 = $163.06; gap $1.16 | 84.06 + 12 + 23; 12 − 10.84 | holds |
| Arm M $32 to $44 | 3 × $9.9 = $29.70 and 3 × $10.04 = $30.12 (the 2026-09-19 and 2026-09-17 rows); 3 × $13.92 = $41.76 (line 86); + $1.94 (lines 393, 400); page 5 of `docs/rulings/2026-09-26-weekend-1-queue-PROPOSAL.md`, lines 758 to 761 | holds; $31.64 to $43.70 |
| Successor all in $194 to $206; programme $422 to $434; left $16 to $28 | 161.90 + 32…44; + 228.15; 450 − | holds as arithmetic; the $16 floor is really $15.95 (**RT-217**) |
| Envelope arithmetic "$3 to $15 left" | 450 − 227.63 − 175 − 44…32 = $3.37 to $15.37 | holds |

ARGUED, not a defect: arm M is priced at arm F's per-run figures, but arm M
carries both arm T's slot and arm C's entangling, and the measured ratios for
those arms are 1.044 and 1.080. At arm C's ratio the lower end would be 3 ×
$10.84 + $1.94 = $34.46. The range still covers it. And the $0.57 already spent
from the rehearsal line is counted in "spent before it" and again inside the
first release's $10 line, which is conservative by $0.57.

---

## What was checked and held (MEASURED unless marked)

Each of these was read from the file named and matches the proposal's figure.

- **`out-repairs/summary_base.json`** (at `e0626b2`): arm T 0.0000 on every seed;
  arm C 0.99 to 1.00 (before the widening); arm F 1.00 to 1.003; arm M 0.4846,
  0.5105 and 0.5322; the separation 0.9977, 0.9927 and 1.0000 (as figures; see
  RT-221); across-seed spread 0.0466 and 0.0499 against within-seed 0.019 to 0.020.
- **`out-repairs/measure_base_T_C.json`**: arm C ownership-only 0.0525 to 0.0600
  against whole-state 0.5025 to 0.5850.
- **`out-repairs/gate_base.json`**: arm M at 0.8613 to 0.8667 on the own-directed
  condition and 0.5517 to 0.5663 on the named-other one; arm T at 1.0000 on both;
  arm F's named-other condition clearing on 1 seed of 3; the ownership-blind
  solver at 0.2340 to 0.2383; the name-only solver at 1.0000 and 0.2380; the bar
  at 790 of 3,000, a share of 0.2633, which this review re-derived by an exact
  binomial tail (appendix).
- **`out-repairs/self-tests.txt`**: the arm M self-test's seven passes.
- **The `controls` fields of the three `out-repairs/measure_base_*.json` files**
  (`controls_table.py`, appendix): control 1 at 0.0000 on T, and 0.50 to 0.57,
  0.49 to 0.56 and 0.36 to 0.42 on C, F and M; control 3 at 0.049 to 0.071 on C
  and F, against untouched rates of 0.049 to 0.069; control 4 at 0.14 to 0.16 on
  C and 0.06 to 0.15 on F; control 6's cells at 81 and 719 trials, moving 0.000
  and 1.000 on T, 0.59 to 0.72 in the same-value cell on C, and 0.17 to 0.32 on
  M; every no-transplant miss inside 0.0132.
- **`out-repairs/measure_base_M.json`**, field `fourth_arm.ownership_only_by_route`:
  the blind subspace catching 0.92 to 0.96 of arm M's separable route.
- **The `floor` fields of the nomination grids**: zero disagreements between the
  two forms of the floor.
- **`out/denominator_simulated.json`** (main line): 0.4323 and 0.3222 against
  0.5018 and 0.5013.
- **`out/denominator_control6.json`** (main line): 0 of 4,000 same-value trials;
  0.2467 rising to 0.3095.
- **`docs/2026-09-21-successor-measure-rehearsal.md`** (main line): 0.7612,
  0.6512 and 0.6512, with negative readings on two seeds of three (line 598);
  0.5375 against 0.5400 (line 546); 0.873 to 0.885 (line 28).
- **`experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot-findings.md`**
  (main line): 0.2877, 0.3057, 0.3195, 0.3227 and 0.3125.
- **`docs/rehearsal-repairs-method-2026-09-25.md`** (at `e0626b2`), line 337:
  arm M's prediction from the record, 0.4186, 0.4328 and 0.4230, which the
  proposal gives as "0.42 to 0.43".

**The repairs of version 1's two fatal findings hold.** The per-arm ceiling
(RT-172) is repaired: the top of the scale is 1.0000 on every arm (failure 1
above). The empty cell (RT-173) is repaired: the relaxed set puts 81 trials in the
same-value cell on every arm and seed, and the no-transplant rule now points the
right way (failure 3 above).

---

## Kill case

If John rules on this text as it stands, the design most likely to be registered
will read arm F at 1.00, the entangled end, and report it as a degree. That
number comes from an instrument that, on the toy, has recovered nothing on arm F
at any layer on any of six seeds (RT-212). The design's own admission says the
measure cannot tell that case from a real one. The committed files can tell, and
the design does not look at them. Before the reading, the money plan guards the
wrong arm. Arm C, the high anchor, failed the gate on every toy seed, is first
tested after both releases are drawn, and turns a supposedly $44 R3 into one
costing the whole successor, about $194 to $206 by section 12.4's own table
(RT-213). The mid-scale anchor that was folded in "on all three seeds" loses a
seed to one of the design's own controls (RT-214). The site rule being frozen has
never been run (RT-215). And the one weakness that answers "is this just the acting
channel?" rests on a sentence that is false on the toy, since the sites it chose
are the acting channel's injection (RT-216). None of this needs money to fix:
every item is a laptop re-run at $0, a pre-stated rule, or a sentence. But until
RT-212 is closed, registering this text means registering a procedure whose one
reading of the free arm is known to come from an empty subspace.

---

## Appendix — full outputs of the scripts cited above

The scripts are committed in `reviews/2026-09-27-successor-v2-gate-c-scripts/`.
Each takes the exported `out-repairs/` folder (or, for the sweeps, the proposal)
as its argument.

```
$ python3 controls_table.py $R/        (ranges across the three seeds, per arm)
arm T: control 1 0.0000; 2-old 0.2350 to 0.2562; control 3 0.0000; control 4 0.0000; 6a 0.0000 (81 trials); 6b 1.0000 (719); control 7 [True, True, True]; untouched 0.0000; miss 0.0000; own 1.0000
arm C: control 1 0.5038 to 0.5675; 2-old 0.0488 to 0.0663; control 3 0.0488 to 0.0625; control 4 0.1437 to 0.1562; 6a 0.5926 to 0.7160 (81); 6b 0.8971 to 0.9054 (719); control 7 all True; untouched 0.0488 to 0.0600; miss 0.0039 to 0.0132; own 0.5487 to 0.5813
arm F: control 1 0.4888 to 0.5637; 2-old 0.0563 to 0.0650; control 3 0.0587 to 0.0712; control 4 0.0612 to 0.1475; 6a 0.6420 to 0.7407 (81); 6b 0.8790 to 0.8957 (719); control 7 all True; untouched 0.0563 to 0.0688; miss 0.0043 to 0.0057; own 0.5563 to 0.5663
arm M: control 1 0.3638 to 0.4238; 2-old 0.0838 to 0.1013; control 3 0.0125 to 0.0563; control 4 0.0275 to 0.1237; 6a 0.1728 to 0.3210 (81); 6b 0.8456 to 0.9527 (719); control 7 all True; untouched 0.0125 to 0.0175; miss 0.0004 to 0.0059; own 0.8712 to 0.8800
largest no-transplant miss across all 12 pairs: 0.0132
```
*(Condensed from the script's one-line-per-field output into one line per arm;
no figure was changed.)*

```
$ python3 recount_widened.py $R/
C/base/0   clearing=30 nominated=((2,), 'action', 8) 0.0550 | other=((2,), 'action', 8) 0.0550 | differs=False gap=0.0000 | nomination changed by widening=True
C/base/1   clearing=27 nominated=((0,), 'post-identity', 8) 0.0567 | other=((0, 1, 2, 3, 4), 'post-identity', 8) 0.0633 | differs=True gap=0.0067 | nomination changed by widening=True
C/base/2   clearing=30 nominated=((0,), 'post-identity', 2) 0.0550 | other=((0, 1, 2, 3, 4), 'post-identity', 2) 0.0600 | differs=True gap=0.0050 | nomination changed by widening=False
T/base/0   clearing=36 nominated=((0,), 'action', 8) 1.0000 | other=((0,), 'action', 8) 1.0000 | differs=False gap=0.0000 | nomination changed by widening=False
T/base/1   clearing=36 nominated=((0,), 'action', 8) 1.0000 | other=((0,), 'action', 8) 1.0000 | differs=False gap=0.0000 | nomination changed by widening=False
T/base/2   clearing=36 nominated=((0,), 'action', 8) 1.0000 | other=((0,), 'action', 8) 1.0000 | differs=False gap=0.0000 | nomination changed by widening=False
F/base/0   clearing=27 nominated=((0,), 'post-identity', 2) 0.0633 | other=((1,), 'post-identity', 1) 0.0633 | differs=True gap=0.0000 | nomination changed by widening=False
F/base/1   clearing=27 nominated=((1,), 'action+3', 4) 0.0500 | other=((1, 2, 3, 4), 'post-identity', 4) 0.0517 | differs=True gap=0.0017 | nomination changed by widening=False
F/base/2   clearing=27 nominated=((0,), 'post-identity', 1) 0.0700 | other=((1,), 'post-identity', 8) 0.0733 | differs=True gap=0.0033 | nomination changed by widening=False
M/base/0   clearing=27 nominated=((0,), 'post-identity', 8) 0.3683 | other=((2,), 'post-identity', 8) 0.3883 | differs=True gap=0.0200 | nomination changed by widening=False
M/base/1   clearing=27 nominated=((3,), 'action', 8) 0.3783 | other=((1,), 'post-identity', 8) 0.3950 | differs=True gap=0.0167 | nomination changed by widening=False
M/base/2   clearing=27 nominated=((0,), 'post-identity', 8) 0.3700 | other=((0, 1, 2, 3, 4), 'post-identity', 8) 0.3800 | differs=True gap=0.0100 | nomination changed by widening=False
site sets differ: 8 of 12; ownership-only share differs: 7 of 12; nominations changed by the widening: 2 of 12
```

```
$ python3 candidate7.py $R/
1. Holding controls (section 7.3): control 7 bit-identical; control 3 <= untouched + 0.0175; control 1 on arm T <= untouched + 0.0175. A failure means no reading for that arm.
   T0: control 3 0.0000 vs limit 0.0175; control 7 True; reading made: True
   T1: control 3 0.0000 vs limit 0.0175; control 7 True; reading made: True
   T2: control 3 0.0000 vs limit 0.0175; control 7 True; reading made: True
   C0: control 3 0.0500 vs limit 0.0688; control 7 True; reading made: True
   C1: control 3 0.0488 vs limit 0.0663; control 7 True; reading made: True
   C2: control 3 0.0625 vs limit 0.0775; control 7 True; reading made: True
   F0: control 3 0.0587 vs limit 0.0762; control 7 True; reading made: True
   F1: control 3 0.0600 vs limit 0.0738; control 7 True; reading made: True
   F2: control 3 0.0712 vs limit 0.0863; control 7 True; reading made: True
   M0: control 3 0.0125 vs limit 0.0300; control 7 True; reading made: True
   M1: control 3 0.0563 vs limit 0.0350; control 7 True; reading made: False   <-- a holding control fails: no reading
   M2: control 3 0.0125 vs limit 0.0312; control 7 True; reading made: True
2. Arm M pass line (section 5.3): 0.3 <= reading <= 0.7 on EVERY seed, with holding controls applied.
   readings made: [0.5104669887278582, None, 0.5321543408360129] -> pass on every seed: False
3. R1 needs every arm carried to pass the learn-both gate (section 3); the toy gate:
   arm T: named-other clears on 3 of 3, own on 3 of 3, learn-both True
   arm C: named-other clears on 0 of 3, own on 3 of 3, learn-both False
   arm F: named-other clears on 1 of 3, own on 3 of 3, learn-both False
   arm M: named-other clears on 3 of 3, own on 3 of 3, learn-both True
4. The rider (section 7.2 item 7): a reading at arm T's site set for every arm and seed.
   arm C: ['no verdict', 'no verdict', 'no verdict']; whole-state at that site [0.0512, 0.0488, 0.06]
   arm F: ['no verdict', 'no verdict', 'no verdict']; whole-state at that site [0.0587, 0.0563, 0.0688]
   arm M: ['no verdict', 'no verdict', 'no verdict']; whole-state at that site [0.4088, 0.4138, 0.41]
5. The lesion description (section 8.2): "all three collapse" (arms T, C, M) on the toy.
   arm T: [True, True, False] [0.2467, 0.251, 0.2733]
   arm C: [True, True, True] [0.178, 0.183, 0.1703]
   arm M: [True, True, True] [0.223, 0.219, 0.2203]
6. The wager (section 12.8): at least $16 left of $450.
   note split, as the proposal carries it, arm M $32: left $27.95  meets $16: True
   note split, as the proposal carries it, arm M $44: left $15.95  meets $16: False
   ruled split, arm M $32: left $26.79  meets $16: True
   ruled split, arm M $44: left $14.79  meets $16: False
```

```
$ python3 -c "
from fractions import Fraction as Fr
from math import comb
n=3000
den=4**n
def tail(k): return Fr(sum(comb(n,i)*3**(n-i) for i in range(k,n+1)), den)
k=min(k for k in range(760,820) if tail(k)<=Fr(1,20))
print('smallest count k with P(X>=k | n=3000, p=1/4) <= 0.05:', k, ' share %.4f'%(k/n), ' tail %.4f'%float(tail(k)), ' tail at k-1 %.4f'%float(tail(k-1)))
print('P(an arm whose own-directed accuracy is exactly 1/4 scores >= %d, i.e. is read as NOT collapsed) = %.4f'%(k,float(tail(k))))
m=0.07625-(1-0.589)/7
print('free-arm seed 2 miss on 2026-09-21: %.6f; more than 0.0175: %s'%(m, m>0.0175))"
smallest count k with P(X>=k | n=3000, p=1/4) <= 0.05: 790  share 0.2633  tail 0.0485  tail at k-1 0.0529
P(an arm whose own-directed accuracy is exactly 1/4 scores >= 790, i.e. is read as NOT collapsed) = 0.0485
free-arm seed 2 miss on 2026-09-21: 0.017536; more than 0.0175: True
```

