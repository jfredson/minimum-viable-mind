# Failure-mode pass on the successor proposal, version 2 — the author's run

*Filed 2026-09-25 (Pacific) by the Claude Code session "MVM W1d proposal v2",
the session that wrote `docs/successor-experiment-proposal-2026-09-26-v2.md`,
in its own worktree (branch `worktree-w1d-proposal-v2`). The file keeps the
date the session prompts give it (2026-09-26). It is filed under this
experiment's reviews directory because the successor experiment has no
directory of its own yet and this is the experiment its text most affects
(`docs/outside-review-protocol.md`, "The pairing rule", the filing fallback).*

**What this is, and what it is not.** The outside-review protocol's
failure-mode pass belongs to the Gate A tier 1 reviewer, and "an author's run
never stands in for the reviewer's" (`docs/outside-review-protocol.md`, "The
failure-mode pass"). This is the author's run, made so that the reviewer's
hour is not spent on a defect already known. Every disposition below shows its
work: the command that was run and the output it returned, pasted as returned.
Every finding is labelled **MEASURED** (a command was run and its output is
here) or **ARGUED** (reasoning a reader can dispute).

**Six failures, not seven.** The session prompt for this pass said "each of the
seven failures now in `docs/known-failure-modes.md`". The file on the main line
at `a96f873` (the commit this worktree branched from) carries six numbered
entries, and so does every branch this session could reach:

```
$ for b in main rulings-2026-09-25-repairs worktree-w1c-rehearsal-repairs worktree-mvm-w1f-rented-slice-attempt-2 worktree-w1c-repairs-check worktree-mvm-w1f-attempt-2-check; do echo "$b: $(git show $b:docs/known-failure-modes.md | grep -c '^## [0-9]') failures"; done
main: 6 failures
rulings-2026-09-25-repairs: 6 failures
worktree-w1c-rehearsal-repairs: 5 failures
worktree-mvm-w1f-rented-slice-attempt-2: 6 failures
worktree-w1c-repairs-check: 6 failures
worktree-mvm-w1f-attempt-2-check: 6 failures
```

(The repairs branch carries five because it branched before failure 6 landed.)
The seventh the prompt may mean is the **candidate** the rented slice's second
attempt drafted and did not add — "an outcome line a plan states in advance
that the design it tests cannot produce on the path it expects"
(`docs/2026-09-25-rented-slice-attempt-2-findings.md` at `7da1946`, section 9,
item 2), which that document says may be an instance of failure 3 and is
John's to rule. The six are run below in the list's order; the candidate is
run after them, labelled as a candidate and not as an entry. MEASURED.

**What this session opened.** Version 2 as written by this session; the
known-failure list on the main line; the rehearsal code on the main line
(`experiments/rehearsal-successor-measure/src/`) and its 2026-09-21 outputs in
`out/`; the repairs outputs exported from commit `e0626b2` (branch
`worktree-w1c-rehearsal-repairs`, pull request 52, whose check was pending)
into a scratch folder, since that branch is not merged; the rented slice's
timing receipt and arithmetic exported from commit `7da1946` (branch
`worktree-mvm-w1f-rented-slice-attempt-2`, pull request 51, check pending).
**What it did not open:** any chat of the sessions that wrote those documents;
any registered launcher with an argument; any vendor. Nothing was rented,
created or spent, and no registered file, ruling or protocol text was edited.

**Two things this pass turned up in the pending findings, flagged and not
resolved here.** The two readings of "the smallest layer set that clears the
floor" pick different site sets on **8 of 12** arm-and-seed pairs by this
session's count from the nomination files at `e0626b2`, where the findings'
text and the repairs rulings' item 4 say 7 of 12 (the findings' own table
lists eight). And arm M's entangled share is **0.60375** (483 of 800) in
`out-repairs/measure_base_M.json`, where the findings' section 5 prints
0.6033. Both are carried into version 2 as flagged; neither moves any ruling.
MEASURED (the commands are under failures 4 and 1 below).

*The Python used throughout is the repository's own environment,
`/Users/john/Code/minimum-viable-mind/.venv/bin/python` (the worktree has no
copy of it); commands are shown with that path shortened to
`.venv/bin/python`. Paths under `out-repairs/` and the two slice files are the
exported copies named above.*

---

## 1. A comparison whose denominator was zero

**What version 2 registers.** The chance-corrected form,
`(whole − ownership_only) / (whole − untouched)`, with the floor
`whole − untouched ≥ 0.8 × (own_directed_accuracy − untouched)` before any
reading is made (version 2, sections 6.3 and 6.4).

**Part one: every denominator the reading divides by, on ceilings measured in
the rehearsal rather than assumed.** Every number typed in below is read from
a committed record, `out-repairs/measure_base_*.json` at `e0626b2`, not
assumed; that is the test's own failure criterion for part one. MEASURED.

```
$ .venv/bin/python -c "
import json
print('failure 1: the chance-corrected denominator (whole - untouched) per arm and seed, repairs fresh episodes (out-repairs at e0626b2)')
print('arm/seed   whole   untouched  own_acc  denominator  0.8*(own-untouched)  clears_floor  degree   version1_form')
for f in ('measure_base_T_C.json','measure_base_F.json','measure_base_M.json'):
    d=json.load(open('out-repairs/'+f))
    for key,row in sorted(d['arms'].items()):
        r=row['reading']; w=r['accuracy_whole']; u=r['accuracy_untouched']; own=r['arm_own_accuracy']
        den=w-u; fmin=0.8*(own-u)
        print(f'{key:8}  {w:.4f}  {u:.4f}     {own:.4f}   {den:.4f}       {fmin:.4f}              {str(den>=fmin):5}      {r[\"degree\"]:.4f}   {r[\"version1_form\"]:.4f}')
print()
print('top of scale when the ownership-only transplant does nothing (ownership_only = untouched): (w-u)/(w-u) = 1 on every arm; version 1 form (w-u)/w:')
for f in ('measure_base_T_C.json','measure_base_F.json','measure_base_M.json'):
    d=json.load(open('out-repairs/'+f))
    for key,row in sorted(d['arms'].items()):
        r=row['reading']; w=r['accuracy_whole']; u=r['accuracy_untouched']
        print(f'  {key}: chance-corrected top = {(w-u)/(w-u):.3f}   version-1 top = {(w-u)/w:.3f}')
"
failure 1: the chance-corrected denominator (whole - untouched) per arm and seed, repairs fresh episodes (out-repairs at e0626b2)
arm/seed   whole   untouched  own_acc  denominator  0.8*(own-untouched)  clears_floor  degree   version1_form
C/base/0  0.5850  0.0512     0.5487   0.5337       0.3980              True       0.9977   0.9103
C/base/1  0.5613  0.0488     0.5813   0.5125       0.4260              True       0.9927   0.9065
C/base/2  0.5025  0.0600     0.5525   0.4425       0.3940              True       1.0000   0.8806
T/base/0  1.0000  0.0000     1.0000   1.0000       0.8000              True       0.0000   0.0000
T/base/1  1.0000  0.0000     1.0000   1.0000       0.8000              True       0.0000   0.0000
T/base/2  1.0000  0.0000     1.0000   1.0000       0.8000              True       0.0000   0.0000
F/base/0  0.4850  0.0587     0.5587   0.4263       0.4000              True       1.0029   0.8814
F/base/1  0.5675  0.0563     0.5663   0.5112       0.4080              True       1.0000   0.9009
F/base/2  0.4913  0.0688     0.5563   0.4225       0.3900              True       1.0000   0.8601
M/base/0  0.7887  0.0125     0.8712   0.7762       0.6870              True       0.5105   0.5024
M/base/1  0.7475  0.0175     0.8800   0.7300       0.6900              True       0.4846   0.4732
M/base/2  0.7913  0.0138     0.8712   0.7775       0.6860              True       0.5322   0.5229

top of scale when the ownership-only transplant does nothing (ownership_only = untouched): (w-u)/(w-u) = 1 on every arm; version 1 form (w-u)/w:
  C/base/0: chance-corrected top = 1.000   version-1 top = 0.912
  C/base/1: chance-corrected top = 1.000   version-1 top = 0.913
  C/base/2: chance-corrected top = 1.000   version-1 top = 0.881
  T/base/0: chance-corrected top = 1.000   version-1 top = 1.000
  T/base/1: chance-corrected top = 1.000   version-1 top = 1.000
  T/base/2: chance-corrected top = 1.000   version-1 top = 1.000
  F/base/0: chance-corrected top = 1.000   version-1 top = 0.879
  F/base/1: chance-corrected top = 1.000   version-1 top = 0.901
  F/base/2: chance-corrected top = 1.000   version-1 top = 0.860
  M/base/0: chance-corrected top = 1.000   version-1 top = 0.984
  M/base/1: chance-corrected top = 1.000   version-1 top = 0.977
  M/base/2: chance-corrected top = 1.000   version-1 top = 0.983
```

**Part two: the largest value the reading can return when the thing it
detects is entirely absent.** In the same output: 1.000 on every arm and seed
under the registered form, against 0.860 to 1.000 under version 1's. MEASURED.

**The same-true-share check the review asked for** (two systems of equal true
separability and unequal transplant strength must read the same) was run by
the 2026-09-21 rehearsal on made-up populations and is in a committed record
on the main line:

```
$ .venv/bin/python -c "
import json; d=json.load(open('experiments/rehearsal-successor-measure/out/denominator_simulated.json')); print(json.dumps(d, indent=1)[:1500])
"
{
 "base_rate": 0.125,
 "cases": {
  "strong transplant": {
   "accuracy_whole": 0.9007999999999999,
   "floor_corrected_mean": 0.5017998460383064,
   "floor_corrected_sd": 0.013170946317616856,
   "registered_mean": 0.4323199808203894,
   "registered_sd": 0.011886784991531833
  },
  "weak transplant": {
   "accuracy_whole": 0.3496925,
   "floor_corrected_mean": 0.5013454893473477,
   "floor_corrected_sd": 0.022950432996913347,
   "registered_mean": 0.3222244275556022,
   "registered_sd": 0.01813190271057092
  }
 },
 "draws": 200,
 "floor_corrected_gap_between_the_two_cases": 0.0004543566909587238,
 "floor_corrected_recovers_the_true_share": true,
 "registered_gap_between_the_two_cases": 0.1100955532647872,
 "registered_spread": 0.01813190271057092,
 "trials_per_draw": 2000,
 "true_outside_share": 0.5,
 "verdict": "D-1 PASS: the floor-corrected form returns the true share in both cases and the registered form does not"
}
```

The record carries what the findings quote: version 1's form 0.4323 and
0.3222, the chance-corrected form 0.5018 and 0.5013, on a true share of 0.5
(`docs/2026-09-21-successor-measure-rehearsal.md`, section 5). This session
did not re-run the simulation; it read the committed record, and the record
says what version 2 says it says. MEASURED.

**Disposition: does not apply, shown.** The denominator is never zero: on
every arm and seed it is at least 0.4225 on the toy, and the floor rule keeps
it at least four fifths of the arm's own room by construction wherever a
reading is made. The top of scale is 1.000 on every arm, so the separation bar
of 0.5 is applied in the units it was set in. Version 1's form, printed
beside it, is the failure this entry names, with the top of scale moving from
0.860 to 1.000 across arms. **Closed on this design.** MEASURED.

---

## 2. A probe target that cannot be recovered in principle

**What version 2 registers.** The label is which marker word is the model's
own, and section 7.2, item 1, states its route to the states in one sentence.

**Part one: the route sentence exists.** Run with the fixed words the list
prescribes, on version 2 and, as a control, on version 1, which had no such
sentence and left the label unstated. MEASURED.

```
$ .venv/bin/python -c "
import re
pattern = r'route to the states|carried by the token|forced by the loss|is the input token'
f='docs/successor-experiment-proposal-2026-09-26-v2.md'
lines=[(i+1,l.strip()) for i,l in enumerate(open(f)) if re.search(pattern,l,re.I)]
print(f'{f}: {len(lines)} route sentence(s)')
for i,l in lines: print(f'   line {i}: {l}')
"
docs/successor-experiment-proposal-2026-09-26-v2.md: 4 route sentence(s)
   line 773: 1. **The label, and its route to the states.** The straight-line read is
   line 776: marker word is the input token at every turn the model's own assignments
   line 777: are spoken on, so it is carried by the token into the running state, and
   line 778: which of the four marker words is the model's own is forced by the loss at
$ .venv/bin/python -c "  (the same, on version 1)  "
docs/successor-experiment-proposal-2026-09-21.md: 0 route sentence(s)
```

The list says plainly that this part is a prompt to look and not a verdict,
and that a session which writes the pattern out of the document it has just
written will match by construction. The sentence the count found is quoted
into this record so it can be argued with by name: *the marker word is the
input token at every turn the model's own assignments are spoken on, so it is
carried by the token into the running state, and which of the four marker
words is the model's own is forced by the loss at the own-directed action.*
ARGUED that it is a route; MEASURED that it is there and that version 1 had
none.

**Part two: the pipeline run on the pre-stated target and on a quantity the
input guarantees.** The list's part two has never been executed as written,
and this session did not execute it either: it would mean running a probe
pipeline twice against checkpoints, and no such run was authorised. What
exists in a committed record on the main line is the closest thing this
design has: the 2026-09-21 rehearsal ran the nomination on the separable arm
under all three readings of "which agent is acting" — the agent's slot (the
quantity version 1 implicitly named, which nothing in the episode defines),
the marker's rank, and which marker word (the quantity the input carries) —
with the same bar and the same procedure. Read out of that record:

```
$ .venv/bin/python -c "
import json
n=json.load(open('experiments/rehearsal-successor-measure/out/nominate.json'))
print('for each label, the site set with the highest development ownership-only accuracy on arm T (the nomination rule), and the reading (whole - oo)/(whole - 0) it implies; untouched is 0.0000 on arm T')
for seed in range(3):
    g=n['arms'][f'T/{seed}']['grid']
    for label in ('agent-slot','marker-rank','marker-word'):
        best=max((e for e in g if e['label']==label), key=lambda e:(e['accuracy_ownership_only'], -e['rank']))
        w=best['accuracy_whole']; oo=best['accuracy_ownership_only']
        print(f'  T seed {seed}, label {label:12}: best ownership-only {oo:.4f} at whole {w:.4f} (layers {best[\"layers\"]}, positions {best[\"positions\"]}, rank {best[\"rank\"]}) -> reading {(w-oo)/w:.4f}')
"
for each label, the site set with the highest development ownership-only accuracy on arm T (the nomination rule), and the reading (whole - oo)/(whole - 0) it implies; untouched is 0.0000 on arm T
  T seed 0, label agent-slot  : best ownership-only 0.0117 at whole 1.0000 (layers [0], positions action, rank 4) -> reading 0.9883
  T seed 0, label marker-rank : best ownership-only 0.0050 at whole 1.0000 (layers [0], positions action, rank 4) -> reading 0.9950
  T seed 0, label marker-word : best ownership-only 1.0000 at whole 1.0000 (layers [0], positions action, rank 8) -> reading 0.0000
  T seed 1, label agent-slot  : best ownership-only 0.0000 at whole 1.0000 (layers [0], positions action, rank 1) -> reading 1.0000
  T seed 1, label marker-rank : best ownership-only 0.0183 at whole 1.0000 (layers [0], positions action, rank 4) -> reading 0.9817
  T seed 1, label marker-word : best ownership-only 1.0000 at whole 1.0000 (layers [0], positions action, rank 8) -> reading 0.0000
  T seed 2, label agent-slot  : best ownership-only 0.0000 at whole 1.0000 (layers [0], positions action, rank 1) -> reading 1.0000
  T seed 2, label marker-rank : best ownership-only 0.0117 at whole 1.0000 (layers [0], positions action, rank 4) -> reading 0.9883
  T seed 2, label marker-word : best ownership-only 1.0000 at whole 1.0000 (layers [0], positions action, rank 8) -> reading 0.0000
```

This is the entry's middle limb in numbers that already exist: the target
the input guarantees (which marker word) recovers the arm's known degree of
0.0000 exactly on every seed, and the two targets without a route (the
agent's slot, the marker's rank) return the largest wrong answer the scale
allows. It reproduces the table in `docs/rulings/2026-09-23-nomination-label.md`
from the underlying record. These are rows read from a committed record, not
the two runs part two asks for; the limb is illustrated on this design, not
executed as the list prescribes. MEASURED for the rows; the test as written
stays unrun.

**Disposition: closed on the label; part two open as the list itself leaves
it.** The registered target has a stated route, and the one comparison on the
record shows the routed target recovering a known answer where the unrouted
ones did not. What remains is the list's own standing gap: the two-run test
has never been executed on any design. It is not closed by the difficulty of
running it. MEASURED and ARGUED as marked.

---

## 3. A cell that is empty by construction

**What version 2 registers.** Control 6 runs on a separately generated relaxed
set in which one item per episode has two agents sharing a value; the
reading, the gates and every other control run on the distinctness-preserving
set (version 2, sections 4.2 and 7.3). The no-transplant sanity rule is the
review's formula `(1 − p)/7` with room for a miss of 0.0175 (section 6.4).

**Part one: count what the generator puts in each pre-stated cell, on the
rehearsal generator, for both sets.** The cell rule is the one the rehearsal's
own check D-4 uses (`experiments/rehearsal-successor-measure/src/denominator.py`,
the inner function `count_same`). MEASURED.

```
$ cd experiments/rehearsal-successor-measure/src && .venv/bin/python -c "
import sys; sys.path.insert(0,'.')
from collections import Counter
import grammar as design                    # the rehearsal generator, not a stand-in
PRE_STATED_CELLS = ['donor dictates the same answer', 'donor dictates a different answer']
def cell_of(pair):
    c=pair['content']; r=pair['recipient']['model']; d=pair['donor']['model']
    same = int(c['values'][r, c['own_item']]) == int(c['values'][d, c['own_item']])
    return PRE_STATED_CELLS[0] if same else PRE_STATED_CELLS[1]
for name, kw in (('distinctness-preserving fresh set (the reading, gates, controls 1-5 and 7)', dict(pool='fresh', collide=False)),
                 ('relaxed set for control 6 only (one item per episode has two agents sharing a value)', dict(pool='fresh', collide=True))):
    pairs = design.make_pairs(800, seed=778, **kw)
    counts = Counter(cell_of(p) for p in pairs)
    print(name)
    for cell in PRE_STATED_CELLS: print(f'   {cell}: {counts.get(cell,0)} trials of {len(pairs)}')
"
distinctness-preserving fresh set (the reading, gates, controls 1-5 and 7)
   donor dictates the same answer: 0 trials of 800
   donor dictates a different answer: 800 trials of 800
relaxed set for control 6 only (one item per episode has two agents sharing a value)
   donor dictates the same answer: 81 trials of 800
   donor dictates a different answer: 719 trials of 800
```

Zero on the strict set is the failure this entry names, reproduced on
purpose; 81 and 719 on the relaxed set are the trials control 6 runs on. The
same two counts appear on every arm and seed in the repairs' committed
outputs (under failure 4 below: "6a trials 81 … 6b trials 719" on all twelve
rows). MEASURED.

**Part two: read the generator for the property that empties a cell.**
MEASURED.

```
$ grep -nE "\.sample\(|\.shuffle\(|\.permutation|permutations\(|set\(|distinct|unique|without replacement|replace=False|collide" experiments/rehearsal-successor-measure/src/grammar.py | head -30
15:  four values are distinct, so the four assignments differ only in who made
137:def _content(rng: np.random.Generator, pool: str, collide: bool) -> dict:
140:    markers = list(rng.choice(marker_pool, size=N_AGENTS, replace=False))
141:    items = list(rng.choice(item_pool, size=N_ITEMS_PER_EPISODE, replace=False))
145:        values[:, j] = rng.choice(N_SLOTS, size=N_AGENTS, replace=False)
146:    collide_pair = None
147:    if collide:
151:        a, b = rng.choice(N_AGENTS, size=2, replace=False)
154:        collide_pair = (int(a), int(b), j)
156:    order = rng.permutation(N_AGENTS * N_ITEMS_PER_EPISODE)
160:    action_order = list(rng.permutation(2))      # which condition speaks first
165:                collide_pair=collide_pair, pool=pool)
256:               collide: bool = False) -> list[dict]:
265:        content = _content(rng, pool, collide)
267:        r, d = rng.choice(elig, size=2, replace=False)
324:        counts.append(len(set(v[:, p["content"]["own_item"]].tolist())))
325:        counts.append(len(set(v[:, p["content"]["other_item"]].tolist())))
326:    check("matched property 1 — four distinct candidate values per item",
327:          set(counts) == {N_AGENTS}, f"distinct counts seen: {sorted(set(counts))}")
343:    sup_ok = all(len(e["targets"]) == 2 and len(set(e["action_pos"].tolist())) == 2
383:          set(turn_counts.values()) == {2})
384:    who_toks = set()
418:    cp = make_pairs(400, seed=11, pool="dev", collide=True)
```

Line 145 is the draw without replacement that empties the cell; lines 147 to
154 are the relaxation that fills it, under its own switch. The idiom
`rng.choice(..., replace=False)` was not in the list's pattern until this
run added `replace=False`; the list's pattern alone would have missed line
145. ARGUED that the pattern should carry that idiom; MEASURED that it finds
the line once it does.

**Part three: every pre-stated threshold at both ends of the range it will
face.** The no-transplant rule, as version 1 wrote it and as version 2
registers it, on the twelve measured toy rates and on the two arithmetic
ends. MEASURED.

```
$ .venv/bin/python -c "
import json
print('rule as version 1 wrote it: untouched near 1/8 (taken as within 0.03 of 0.125)   rule as version 2 registers it: |untouched - (1-p)/7| <= 0.0175')
print('arm/seed  own_acc(p)  untouched  (1-p)/7   miss     v1 verdict        v2 verdict')
for f in ('measure_base_T_C.json','measure_base_F.json','measure_base_M.json'):
    d=json.load(open('out-repairs/'+f))
    for key,row in sorted(d['arms'].items()):
        r=row['reading']; p=r['arm_own_accuracy']; u=r['accuracy_untouched']; pred=(1-p)/7; miss=u-pred
        v1='pass' if abs(u-0.125)<=0.03 else 'FAIL (pairing broken)'
        v2='pass' if abs(miss)<=0.0175 else 'FAIL (pairing suspect)'
        print(f'{key:8}  {p:.4f}      {u:.4f}     {pred:.4f}   {miss:+.4f}   {v1:20} {v2}')
print()
print('the two ends, by arithmetic: a model that learned nothing (p=0.25) and one that learned the task (p=0.95)')
for p in (0.25,0.95):
    pred=(1-p)/7
    print(f'  p={p}: predicted no-transplant rate {pred:.4f}; version 1 rule (near 1/8): {\"pass\" if abs(pred-0.125)<=0.03 else \"FAIL\"}; version 2 rule passes iff measured within 0.0175 of {pred:.4f}')
"
rule as version 1 wrote it: untouched near 1/8 (taken as within 0.03 of 0.125)   rule as version 2 registers it: |untouched - (1-p)/7| <= 0.0175
arm/seed  own_acc(p)  untouched  (1-p)/7   miss     v1 verdict        v2 verdict
C/base/0  0.5487      0.0512     0.0645   -0.0132   FAIL (pairing broken) pass
C/base/1  0.5813      0.0488     0.0598   -0.0111   FAIL (pairing broken) pass
C/base/2  0.5525      0.0600     0.0639   -0.0039   FAIL (pairing broken) pass
T/base/0  1.0000      0.0000     0.0000   +0.0000   FAIL (pairing broken) pass
T/base/1  1.0000      0.0000     0.0000   +0.0000   FAIL (pairing broken) pass
T/base/2  1.0000      0.0000     0.0000   +0.0000   FAIL (pairing broken) pass
F/base/0  0.5587      0.0587     0.0630   -0.0043   FAIL (pairing broken) pass
F/base/1  0.5663      0.0563     0.0620   -0.0057   FAIL (pairing broken) pass
F/base/2  0.5563      0.0688     0.0634   +0.0054   FAIL (pairing broken) pass
M/base/0  0.8712      0.0125     0.0184   -0.0059   FAIL (pairing broken) pass
M/base/1  0.8800      0.0175     0.0171   +0.0004   FAIL (pairing broken) pass
M/base/2  0.8712      0.0138     0.0184   -0.0046   FAIL (pairing broken) pass

the two ends, by arithmetic: a model that learned nothing (p=0.25) and one that learned the task (p=0.95)
  p=0.25: predicted no-transplant rate 0.1071; version 1 rule (near 1/8): pass; version 2 rule passes iff measured within 0.0175 of 0.1071
  p=0.95: predicted no-transplant rate 0.0071; version 1 rule (near 1/8): FAIL; version 2 rule passes iff measured within 0.0175 of 0.0071
```

Version 1's rule fails every working toy arm and passes a model that learned
nothing: that is the failure, reproduced. Version 2's rule passes all twelve
working rows, with the largest miss 0.0132, inside the 0.0175 room; and at
the broken end it does not pass a model that learned nothing on the strength
of its being broken, because it checks the pairing against the arm's own
accuracy and leaves learning to the learn-both gate. **The "within 0.03" used
to make version 1's "near" a number is this session's choice** (ARGUED); any
reasonable width gives the same verdicts, since the working rows sit at 0.000
to 0.069 against 0.125.

**A second pre-stated threshold, the floor of section 6.4, at both of its
written forms.** The nomination records at `e0626b2` carry a verdict under
both forms for every site set:

```
$ .venv/bin/python -c "
import json
dis=0; total=0
for f in ('nominate_base_T_C.json','nominate_base_F.json','nominate_base_M.json'):
    n=json.load(open('out-repairs/'+f))
    for key,row in sorted(n['arms'].items()):
        for e in row['ownership']['grid']:
            fl=e['floor']; total+=1; dis+= (fl['clears']!=fl['clears_plain_form'])
print('site-set entries with a floor verdict:', total, '; entries where the chance-corrected and plain forms disagree:', dis)
"
site-set entries with a floor verdict: 2112 ; entries where the chance-corrected and plain forms disagree: 0
```

MEASURED: 0 of 2,112, which is what version 2's section 6.4 says.

**Disposition: closed on this design, shown.** Both of control 6's cells have
trials (81 and 719 of 800) on the set it is registered to run on, the strict
set's zero is stated as the reason for the relaxed set, and the one threshold
that was pointed the wrong way round now passes the working end and fires only
on a broken pairing. MEASURED.

---

## 4. A claim of measurement with no record, or with a record that does not reproduce

**Part one: list every sentence that claims a measurement.** Both sweeps, as
the list prescribes, counted rather than pasted (367 and 109 lines; the number
sweep is saved beside this session's scratch and was read line by line for
part two). MEASURED.

```
$ grep -n -iE "verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result" docs/successor-experiment-proposal-2026-09-26-v2.md | wc -l
     367
$ grep -n -E "[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}" docs/successor-experiment-proposal-2026-09-26-v2.md | wc -l
     109
$ grep -c "MEASURED" docs/successor-experiment-proposal-2026-09-26-v2.md; grep -c "ARGUED" docs/successor-experiment-proposal-2026-09-26-v2.md
32
8
```

**Part two, first half: the mechanical check — does every file named exist,
and is every figure in the file its sentence cites.** The repository's own
checker, run on version 2 after its corrections (its first run found four
figures cited to the wrong one of two files in a sentence; the sentences were
split, and the second run is below). MEASURED.

```
$ .venv/bin/python scripts/check_citations.py --only docs/successor-experiment-proposal-2026-09-26-v2.md
[CONFIDENT] 36 reference(s) name a file that is not in the repository
[LOOK AT IT] 0 bare name(s) match more than one file
[LOOK AT IT] 12 name(s) of run-output files that are not in the repository
[LOOK AT IT] 0 reference(s) written with a gap or a wildcard that matched nothing
[NOT CHECKED] 1 reference(s) to files outside this repository
[NOT CHECKED] 0 reference(s) to paths .gitignore keeps out of the repository
PART (b): is a figure given with a citation actually in the file cited?
[CONFIDENT] 0 exact figure(s) absent from the one file their sentence cites
[LOOK AT IT] 0 figure(s) worth a human eye
Confident findings: 36. Things for a human to look at: 12.
```

(The full report, with every reference listed, is pasted into the pull
request that carries this file.) The 36 "not in the repository" references
are, every one, files that live on the three unmerged branches version 2
cites by commit, plus this pass file itself (created after that run), plus
two relative names (`src/repairs.py`, `out-repairs/`) inside a sentence that
gives their full directory. The checker reads the main line's tree and
cannot see a branch. So the existence check was made against the commits
named, which is the form of this failure the closure rule was written for —
"names a file that exists at no commit". MEASURED:

```
$ git cat-file -e e0626b2:docs/2026-09-26-rehearsal-repairs.md && echo "exists ..."   (and so on, one line per file)
exists e0626b2:docs/2026-09-26-rehearsal-repairs.md
exists e0626b2:docs/rehearsal-repairs-method-2026-09-25.md
exists e0626b2:experiments/rehearsal-successor-measure/src/arm_middle.py
exists e0626b2:experiments/rehearsal-successor-measure/src/repairs.py
exists e0626b2:experiments/rehearsal-successor-measure/out-repairs/gate_base.json
exists e0626b2:experiments/rehearsal-successor-measure/out-repairs/gate_curriculum.json
exists e0626b2:experiments/rehearsal-successor-measure/out-repairs/gate_reweight.json
exists e0626b2:experiments/rehearsal-successor-measure/out-repairs/measure_base_M.json
exists e0626b2:experiments/rehearsal-successor-measure/out-repairs/summary_base.json
exists e0626b2:experiments/rehearsal-successor-measure/out-repairs/self-tests.txt
exists 7da1946:docs/2026-09-25-rented-slice-attempt-2-findings.md
exists 7da1946:docs/preauthorised-spending-proposal-2026-09-21-note-2026-09-25-attempt-2.md
exists 7da1946:.../bench_arms.json
exists 7da1946:.../second_release_arithmetic.py
exists 7da1946:.../second-release-arithmetic.txt
exists 7da1946:experiments/06-mvm-0a-constructed-self-index/compute-ledger.md
exists rulings-2026-09-25-repairs:docs/rulings/2026-09-25-rehearsal-repairs-rulings.md
exists 7b15c88:experiments/06-mvm-0a-constructed-self-index/amendment-a3.md
exists 7b15c88:docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md
$ git rev-parse --short rulings-2026-09-25-repairs
e03288c
```

Every file version 2 cites to a branch exists at the commit it names. The
branch `rulings-2026-09-25-repairs` is cited by name rather than by commit in
version 2; its tip when checked was `e03288c` ("Ruling 2026-09-25: the five
decisions from the Weekend 1 rehearsal repairs"), recorded here so the
citation has an anchor if the branch is deleted after merge.

**Part two, second half: regenerate the numbers.** For each figure version 2
quotes from a record, the one command that regenerates it. MEASURED, all
from the exported copies of the records at `e0626b2` and `7da1946`.

*The separation, the per-arm readings, the uncertainty, arm M's band and
formula, and the learn-both bar:*

```
$ .venv/bin/python -c "
import json
s=json.load(open('out-repairs/summary_base.json'))
print(' separation C minus T per seed:', [round(s['separation'][k]['C_minus_T'],4) for k in ('0','1','2')], 'all clear 0.5:', all(s['separation'][k]['clears_0_5'] for k in ('0','1','2')))
for arm in 'TCFM':
    a=s['arms'][arm]; print(f' arm {arm}: degree per seed', [round(x,4) for x in a['per_seed_degree']], 'across-seed sd of raw diff', round(a['across_seed_sd_of_raw_difference'],4), 'within-seed bootstrap', [round(x,4) for x in a['within_seed_bootstrap_se']])
m=json.load(open('out-repairs/measure_base_M.json'))
for k,row in sorted(m['arms'].items()):
    fa=row['fourth_arm']; r=row['reading']
    print(f' {k}: blind {r[\"degree\"]:.4f}, formula on routes {fa[\"predicted_from_route_accuracies\"]:.4f}, miss {abs(r[\"degree\"]-fa[\"predicted_from_route_accuracies\"]):.3f}, entangled share {fa[\"entangled_share\"]:.4f}, in 0.3-0.7: {0.3<=r[\"degree\"]<=0.7}')
g=json.load(open('out-repairs/gate_base.json'))
print(' bar:', g['bar'])
"
 separation C minus T per seed: [0.9977, 0.9927, 1.0] all clear 0.5: True
 arm T: degree per seed [0.0, 0.0, 0.0] across-seed sd of raw diff 0.0 within-seed bootstrap [0.0, 0.0, 0.0]
 arm C: degree per seed [0.9977, 0.9927, 1.0] across-seed sd of raw diff 0.0466 within-seed bootstrap [0.0194, 0.0195, 0.0203]
 arm F: degree per seed [1.0029, 1.0, 1.0] across-seed sd of raw diff 0.0499 within-seed bootstrap [0.0202, 0.0189, 0.0199]
 arm M: degree per seed [0.5105, 0.4846, 0.5322] across-seed sd of raw diff 0.0309 within-seed bootstrap [0.0177, 0.0167, 0.0184]
 M/base/0: blind 0.5105, formula on routes 0.4895, miss 0.021, entangled share 0.6038, in 0.3-0.7: True
 M/base/1: blind 0.4846, formula on routes 0.4572, miss 0.027, entangled share 0.6038, in 0.3-0.7: True
 M/base/2: blind 0.5322, formula on routes 0.4904, miss 0.042, entangled share 0.6038, in 0.3-0.7: True
 bar: {'as_a_share': 0.2633333333333333, 'episodes': 3000, 'min_correct': 790}
$ .venv/bin/python -c "
from math import lgamma, log, exp
def logC(n,k): return lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)
def p_at_least(k,n,p=0.25):
    return sum(exp(logC(n,i)+i*log(p)+(n-i)*log(1-p)) for i in range(k,n+1))
print('one-sided binomial tail at n=3000, p=1/4:')
for k in (788,789,790,791): print(f'  P(X>={k}) = {p_at_least(k,3000):.4f}  ({k/3000:.4f} as a share)')
print('smallest k with P(X>=k) < 0.05:', next(k for k in range(750,900) if p_at_least(k,3000)<0.05))
"
one-sided binomial tail at n=3000, p=1/4:
  P(X>=788) = 0.0575  (0.2627 as a share)
  P(X>=789) = 0.0529  (0.2630 as a share)
  P(X>=790) = 0.0485  (0.2633 as a share)
  P(X>=791) = 0.0445  (0.2637 as a share)
smallest k with P(X>=k) < 0.05: 790
```

The bar reproduces: 790 of 3,000, a share of 0.2633, which the ruling writes
as "above 0.2630" (789 of 3,000 is 0.2630 and does not clear). Arm M's
entangled share regenerates as 0.6038 (0.60375, 483 of 800), not the 0.6033
the findings print — the first discrepancy flagged at the top.

*The gate figures, the solvers, the controls, the rider and control 2:*

```
$ .venv/bin/python -c "
import json
g=json.load(open('out-repairs/gate_base.json'))
for arm in 'TCFM':
    rows=[g['runs'][f'{arm}/base/{sd}'] for sd in range(3)]
    print(f' arm {arm} own', [round(r['own'],4) for r in rows], 'other', [round(r['other'],4) for r in rows], 'other clears', [r['other_clears'] for r in rows], 'lesioned own', [round(r['lesioned_own'],4) for r in rows])
for k in ('blind/base/0','blind/base/1','blind/base/2'):
    v=g['runs'][k]; print(k, 'own', round(v['own'],4), 'other', round(v['other'],4), 'other clears', v['other_clears'])
print('name-only solver:', g['name_only_solver'])
"
 arm T own [1.0, 1.0, 1.0] other [1.0, 1.0, 1.0] other clears [True, True, True] lesioned own [0.2467, 0.251, 0.2733]
 arm C own [0.5703, 0.5677, 0.5757] other [0.2533, 0.2503, 0.236] other clears [False, False, False] lesioned own [0.178, 0.183, 0.1703]
 arm F own [0.5597, 0.5513, 0.5547] other [0.3313, 0.2603, 0.2487] other clears [True, False, False] lesioned own [0.176, 0.185, 0.194]
 arm M own [0.864, 0.8613, 0.8667] other [0.5543, 0.5663, 0.5517] other clears [True, True, True] lesioned own [0.223, 0.219, 0.2203]
blind/base/0 own 0.234 other 0.2373 other clears False
blind/base/1 own 0.2383 other 0.242 other clears False
blind/base/2 own 0.234 other 0.2167 other clears False
name-only solver: {'n': 3000, 'other': 1.0, 'own': 0.238}
$ .venv/bin/python -c "
import json
for f in ('measure_base_T_C.json','measure_base_F.json','measure_base_M.json'):
    d=json.load(open('out-repairs/'+f))
    for key,row in sorted(d['arms'].items()):
        c=row['controls']
        print(f'  {key}: 6a trials {c[\"6a same-value cell: trials\"]}, moved {c[\"6a same-value cell: share whose action moved\"]:.3f}; 6b trials {c[\"6b different-value cell: trials\"]}, moved {c[\"6b different-value cell: share whose action moved\"]:.3f}; c1 {c[\"1 content transplant (the complement subspace)\"]:.4f}; c3 {c[\"3 matched random subspace, same rank\"]:.4f}; c4 {c[\"4 transplant before the identity can be known\"]:.4f}; c7 null identical {c[\"7 null transplant leaves every logit bit-identical\"]}; rider {row[\"rider_at_arm_T_site_set\"][\"reading\"].get(\"status\")} ; control2 {row[\"control2\"][\"full procedure\"].get(\"status\")}')
"
  C/base/0: 6a trials 81, moved 0.716; 6b trials 719, moved 0.898; c1 0.5637; c3 0.0500; c4 0.1562; c7 null identical True; rider no verdict ; control2 no verdict
  C/base/1: 6a trials 81, moved 0.716; 6b trials 719, moved 0.897; c1 0.5675; c3 0.0488; c4 0.1437; c7 null identical True; rider no verdict ; control2 no verdict
  C/base/2: 6a trials 81, moved 0.593; 6b trials 719, moved 0.905; c1 0.5038; c3 0.0625; c4 0.1562; c7 null identical True; rider no verdict ; control2 no verdict
  T/base/0: 6a trials 81, moved 0.000; 6b trials 719, moved 1.000; c1 0.0000; c3 0.0000; c4 0.0000; c7 null identical True; rider valid ; control2 no verdict
  T/base/1: 6a trials 81, moved 0.000; 6b trials 719, moved 1.000; c1 0.0000; c3 0.0000; c4 0.0000; c7 null identical True; rider valid ; control2 no verdict
  T/base/2: 6a trials 81, moved 0.000; 6b trials 719, moved 1.000; c1 0.0000; c3 0.0000; c4 0.0000; c7 null identical True; rider valid ; control2 no verdict
  F/base/0: 6a trials 81, moved 0.741; 6b trials 719, moved 0.896; c1 0.4938; c3 0.0587; c4 0.1475; c7 null identical True; rider no verdict ; control2 pass
  F/base/1: 6a trials 81, moved 0.679; 6b trials 719, moved 0.879; c1 0.5637; c3 0.0600; c4 0.0612; c7 null identical True; rider no verdict ; control2 pass
  F/base/2: 6a trials 81, moved 0.642; 6b trials 719, moved 0.882; c1 0.4888; c3 0.0712; c4 0.1437; c7 null identical True; rider no verdict ; control2 pass
  M/base/0: 6a trials 81, moved 0.235; 6b trials 719, moved 0.946; c1 0.4125; c3 0.0125; c4 0.1237; c7 null identical True; rider no verdict ; control2 no verdict
  M/base/1: 6a trials 81, moved 0.173; 6b trials 719, moved 0.846; c1 0.3638; c3 0.0563; c4 0.0275; c7 null identical True; rider no verdict ; control2 no verdict
  M/base/2: 6a trials 81, moved 0.321; 6b trials 719, moved 0.953; c1 0.4238; c3 0.0125; c4 0.1212; c7 null identical True; rider no verdict ; control2 no verdict
```

Every range version 2 quotes for controls 1, 3, 4 and 6, the rider and
control 2 is inside these rows. One correction was made from this output:
version 2's first draft gave control 4's range as "0.14 to 0.16 on arms C and
F"; arm F's runs 0.0612 to 0.1475, and the sentence now says 0.06 to 0.15 for
arm F.

*The two readings of "the smallest layer set that clears it":*

```
$ .venv/bin/python -c "
import json
pairs_differ=0
for f in ('nominate_base_T_C.json','nominate_base_F.json','nominate_base_M.json'):
    n=json.load(open('out-repairs/'+f))
    for key,row in sorted(n['arms'].items()):
        o=row['ownership']; nom=o.get('nomination'); sens=o.get('sensitivity')
        differ = (nom['layers'],nom['positions'],nom['rank'])!=(sens['layers'],sens['positions'],sens['rank'])
        pairs_differ+=differ
        print(f'  {key}: nominated {nom[\"positions\"]} layers {nom[\"layers\"]} rank {nom[\"rank\"]} oo {nom[\"accuracy_ownership_only\"]:.4f} | sensitivity {sens[\"positions\"]} layers {sens[\"layers\"]} rank {sens[\"rank\"]} oo {sens[\"accuracy_ownership_only\"]:.4f} | differ {differ} | gap {abs(nom[\"accuracy_ownership_only\"]-sens[\"accuracy_ownership_only\"]):.4f}')
print('arm-and-seed pairs where the two readings of smallest-that-clears pick different site sets:', pairs_differ, 'of 12')
"
  C/base/0: nominated all layers [0] rank 2 oo 0.0550 | sensitivity all layers [0] rank 2 oo 0.0550 | differ False | gap 0.0000
  C/base/1: nominated all layers [0] rank 4 oo 0.0567 | sensitivity post-identity layers [0, 1, 2, 3, 4] rank 8 oo 0.0633 | differ True | gap 0.0067
  C/base/2: nominated post-identity layers [0] rank 2 oo 0.0550 | sensitivity post-identity layers [0, 1, 2, 3, 4] rank 2 oo 0.0600 | differ True | gap 0.0050
  T/base/0: nominated action layers [0] rank 8 oo 1.0000 | sensitivity action layers [0] rank 8 oo 1.0000 | differ False | gap 0.0000
  T/base/1: nominated action layers [0] rank 8 oo 1.0000 | sensitivity action layers [0] rank 8 oo 1.0000 | differ False | gap 0.0000
  T/base/2: nominated action layers [0] rank 8 oo 1.0000 | sensitivity action layers [0] rank 8 oo 1.0000 | differ False | gap 0.0000
  F/base/0: nominated post-identity layers [0] rank 2 oo 0.0633 | sensitivity post-identity layers [1] rank 1 oo 0.0633 | differ True | gap 0.0000
  F/base/1: nominated action+3 layers [1] rank 4 oo 0.0500 | sensitivity all layers [1, 2, 3, 4] rank 8 oo 0.0533 | differ True | gap 0.0033
  F/base/2: nominated post-identity layers [0] rank 1 oo 0.0700 | sensitivity post-identity layers [1] rank 8 oo 0.0733 | differ True | gap 0.0033
  M/base/0: nominated post-identity layers [0] rank 8 oo 0.3683 | sensitivity post-identity layers [2] rank 8 oo 0.3883 | differ True | gap 0.0200
  M/base/1: nominated action layers [3] rank 8 oo 0.3783 | sensitivity post-identity layers [1] rank 8 oo 0.3950 | differ True | gap 0.0167
  M/base/2: nominated post-identity layers [0] rank 8 oo 0.3700 | sensitivity post-identity layers [0, 1, 2, 3, 4] rank 8 oo 0.3800 | differ True | gap 0.0100
arm-and-seed pairs where the two readings of smallest-that-clears pick different site sets: 8 of 12
```

Eight, not seven: the second discrepancy flagged at the top. The gaps are
all 0.0200 or less, as the findings say. The nominated site sets in this
output also show the widened exclusion's reason: arm C at seeds 0 and 1 was
nominated at "all" positions (the first layer at every position).

*The site-set counts version 2 prints in section 7.2:*

```
$ .venv/bin/python -c "
def contiguous(n): return [tuple(range(a,b+1)) for a in range(n) for b in range(a,n)]
toy_pos = ['action','action+ans','action+3','post-identity','all']
kept = [p for p in toy_pos if p != 'all']
for name, n_states in (('toy (embedding + 4 blocks)',5), ('registered (embedding + 12 blocks)',13)):
    L = contiguous(n_states)
    before = len(L)*len(toy_pos) - 1
    after  = len(L)*len(kept)
    print(f'{name}: {len(L)} contiguous layer sets; site sets {before} -> {after} after the widened exclusion; comparisons at 4 rank caps {before*4} -> {after*4}')
"
toy (embedding + 4 blocks): 15 contiguous layer sets; site sets 74 -> 60 after the widened exclusion; comparisons at 4 rank caps 296 -> 240
registered (embedding + 12 blocks): 91 contiguous layer sets; site sets 454 -> 364 after the widened exclusion; comparisons at 4 rank caps 1816 -> 1456
```

The ruled figures (296 and 1,816) reproduce as the "before" column; the
figures version 2 prints (240 and 1,456) are the "after" column.

*The second release's arithmetic, from the timing receipt and the ledger's
$10.04:*

```
$ .venv/bin/python -c "
import json
b=json.load(open('bench_arms.json'))
run=10.04   # the compute ledger's 2026-09-17 row: \$20.08 for two registered-size runs
r=b['ratio_to_arm_F']; per={a: round(run*r[a],2) for a in 'TCF'}
print('ratios:', {a: round(r[a],4) for a in 'TCF'}, 'ms per step:', {a: round(b['arms'][a]['seconds_per_step']*1000,2) for a in 'TCF'}, 'steps:', b['arms']['F']['steps'], 'complete:', b['complete'])
print('per run:', per)
eight = 2*per['F'] + 3*per['T'] + 3*per['C']
print('eight remaining runs (2 F, 3 T, 3 C):', round(eight,2), '; re-run at the dearest arm:', per['C'], '; + 12 + 23 ->', round(eight+per['C']+12+23,2), '; both releases with a \$32 first release:', round(32+eight+per['C']+12+23,2))
print('as ruled by item 19 (re-run in the first release at \$12): 44 +', round(eight+12+23,2), '=', round(44+eight+12+23,2))
for m in (32,44): print(f'programme after the successor with arm M at \${m}: 228.15 + 161.90 + {m} =', round(228.15+161.90+m,2), '; left of 450:', round(450-228.15-161.90-m,2))
"
ratios: {'T': 1.0443, 'C': 1.0798, 'F': 1.0} ms per step: {'T': 13.08, 'C': 13.52, 'F': 12.53} steps: 50 complete: True
per run: {'T': 10.48, 'C': 10.84, 'F': 10.04}
eight remaining runs (2 F, 3 T, 3 C): 84.04 ; re-run at the dearest arm: 10.84 ; + 12 + 23 -> 129.88 ; both releases with a $32 first release: 161.88
as ruled by item 19 (re-run in the first release at $12): 44 + 119.04 = 163.04
programme after the successor with arm M at $32: 228.15 + 161.90 + 32 = 422.05 ; left of 450: 27.95
programme after the successor with arm M at $44: 228.15 + 161.90 + 44 = 434.05 ; left of 450: 15.95
```

The note's figures ($84.06, $129.90, $161.90) reproduce to within two cents
of the rounded per-run figures used here ($84.04, $129.88, $161.88), the
difference being rounding of each per-run cost before summing; the note's
script sums before rounding. Version 2 quotes the note's figures. The
programme totals version 2 gives (about $422 to $434, about $16 to $28 left)
reproduce.

**Disposition: closed on this design, with the two discrepancies flagged.**
Every figure version 2 quotes was regenerated from the record it cites, or
read from it; every file it cites exists at the commit named; the two figures
that did not regenerate exactly (7 against 8 of 12; 0.6033 against 0.60375)
are stated in version 2 as discrepancies in the pending findings, not
silently adopted from either side. MEASURED.

---

## 5. A command that creates something while documented as creating nothing

**What version 2 registers.** Nothing in version 2 runs a launcher; it names
the launch preconditions (the argument guard, the sleep guard, the tripwire to
be written) in section 11. The list's test is the guard check, which creates
nothing and never runs the registered launcher. MEASURED.

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
RT-198 — launchers must refuse arguments rather than launch

unregistered launchers: an argument is refused
  [ ok ] launch_a3_fetch_first.sh refuses an argument (exit 2)
  [ ok ] launch_a3_fetch_first.sh says why it refused
  [ ok ] launch_a3_fetch_first.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_a3_fetch_first.sh guard (line 121) precedes any vendor command (line 340)
  [ ok ] launch_ctl_pilot.sh refuses an argument (exit 2)
  [ ok ] launch_ctl_pilot.sh says why it refused
  [ ok ] launch_ctl_pilot.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_ctl_pilot.sh guard (line 93) precedes any vendor command (line 219)
  [ ok ] launch_pilot_a1.sh refuses an argument (exit 2)
  [ ok ] launch_pilot_a1.sh says why it refused
  [ ok ] launch_pilot_a1.sh names DRYRUN=1 as the way to preview
  [ ok ] launch_pilot_a1.sh guard (line 48) precedes any vendor command (line 117)

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

The output differs from the list's printed block only in the guard and
vendor-command line numbers (121/340, 93/219, 48/117 against 104/227, 87/201,
42/99), which the list says move when a launcher is edited; the launcher fix
of 2026-09-25 moved them. The negative control still rejects the unguarded
stand-in.

**Disposition: does not apply to version 2's text, and the guard the design
depends on holds, shown.** Version 2 registers no launcher and runs none;
the launch preconditions it names are in force on every unregistered
launcher. What is not yet in force is the tripwire of section 12.5, which
version 2 says in terms is code work owed before step 5a. The registered
launcher's amendment is still before Gate A, and the standing prohibition
stands. MEASURED.

---

## 6. A remote step tested only against stand-ins

**What version 2 registers.** Nothing in version 2 sends a command to a
machine. Section 10's item R-11 records what the rented slice exercised
against the real vendor and what it did not (the handshake's machine half),
and section 13's weakness W9 carries the gap. The list's test is the
remote-forms check, which rents nothing. MEASURED.

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds 8s)

launch_a3_fetch_first.sh
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)

negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang

all checks pass. Nothing was rented and nothing was spent.
```

Identical to the list's printed block in every verdict and whole second.

**Disposition: does not apply to version 2's text; the launcher it will
depend on passes; and one remote step stays open by the list's own general
discipline.** The list says that before a remote step is counted as tested, a
record must say what stood in for the far end and what the stand-in cannot
do. Version 2 does that for the shutdown handshake in the words the slice
findings used: the laptop half met the real vendor; the machine half did
not, because on the normal path the laptop deletes the machine before the
machine's watcher can be observed finding the receipt. That step is **not
counted as tested** in version 2, is carried as weakness W9, and is decision
18 for John. MEASURED for the check; ARGUED for the disposition of the
handshake, which follows the findings' own reasoning.

---

## The candidate seventh: an outcome line a plan states in advance that the design it tests cannot produce on the path it expects

*Not on the list. Drafted in `docs/2026-09-25-rented-slice-attempt-2-findings.md`
at `7da1946`, section 9, item 2, and not added; run here because the prompt
for this pass counted seven. Its test as drafted: for each pre-stated line,
name the code path that prints each signal it needs and show that path can
run in the order the line requires.*

Version 2's pre-stated lines that need a code path to print a signal, and
whether the path exists on the code the rehearsal ran. ARGUED from reading
the code, with the one thing that can be counted counted:

```
$ git show e0626b2:experiments/rehearsal-successor-measure/src/repairs.py | grep -c "rider_at_arm_T_site_set\|no verdict\|no_transplant_rate_miss\|control2\|clears_plain_form"
12
$ grep -rn "1\.25\|tripwire" experiments/06-mvm-0a-constructed-self-index/src/launch_gate.sh | wc -l
       0
```

- The rider's "no verdict" (section 7.2, item 7), control 2's "not applicable"
  and "no verdict" (section 7.3, item 2), the no-transplant miss (section 6.4,
  rule 2) and the floor in both forms (rule 1): all printed by the repairs
  driver at `e0626b2`, and each was seen to fire on the toy (the rows under
  failure 4). **These lines can be produced.**
- The tripwire (section 12.5): **no code path exists** to print a trip; the
  launch gate carries no 1.25 and no tripwire line. Version 2 says so and
  names it as work owed before step 5a. A pre-stated line whose code does not
  exist is not yet a line that can fire; this stays **open** until the code is
  written and checked.
- The handshake's pass line of version 1's item R-11 ("receipt written", then
  "receipt found", then deletion within seconds) is the case the candidate was
  drafted from: on the normal path the second signal is written where nothing
  fetches it. Version 2 does not re-state that line as a pass condition; it
  records what was and was not exercised and puts the two ways to test the
  machine half to John (decision 18). **Not re-registered in a form that
  cannot fire.**

**Disposition: one open item (the tripwire's code), stated as open.** Whether
this candidate is a new species or an instance of failure 3 is John's ruling;
this pass does not add it to the list.

---

## What this pass leaves open, in one place

1. **Failure 2, part two** — the two-run test — has never been executed on any
   design, and was not executed here. Open as the list itself leaves it.
2. **The tripwire's code** does not exist; its pre-stated line cannot yet fire.
   Version 2 names it as owed before step 5a.
3. **The handshake's machine half** is untested against the real vendor;
   carried as weakness W9 and decision 18, not counted as tested.
4. **Two discrepancies in the pending findings** (8 against 7 of 12; 0.60375
   against 0.6033) are flagged for that findings file's own check.
5. **This is the author's run.** The Gate A tier 1 reviewer's own pass, on
   version 3 (the registration text), is still owed under the protocol, and
   nothing here stands in for it.

No machine was rented, nothing was created and nothing was spent by any
command above. No registered text, ruling file or protocol text was edited.
