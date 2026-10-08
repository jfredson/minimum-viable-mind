*This is file 12 of 33 of one review packet, pasted into a single conversation. It contains record 4 part 11 of 12 (THE TEXT UNDER REVIEW - successor experiment proposal, version 4). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 4 of 25, part 11 of 12 - THE TEXT UNDER REVIEW - successor experiment proposal, version 4 - `docs/successor-experiment-proposal-2026-10-03-v4.md` (complete file, 292,507 characters) =====
```
$ .venv/bin/python -c "
import json
O='experiments/rehearsal-successor-measure/out-controls-rerun/'
print('right of 180 held-out episodes, per running state 0 to 4: whole read | best piece of 1, 2, 4 or 8 directions')
for a in 'TCFM':
  for s in '012':
    n=json.load(open(f'{O}nominate_{a}_seed{s}.json'))
    f=n['fits']
    print(f'{a}/{s}', ' '.join(f"{f[l]['whole']:>3}|{max(f[l]['piece'].values()):>3}" for l in sorted(f)), '->', n['primary']['status'])
S=json.load(open(O+'summary.json'))
print('separation:', {s:round(v['C_minus_T'],4) for s,v in S['separation'].items()}, 'all clear 0.5:', all(v['clears_0_5'] for v in S['separation'].values()))
print('arm M readings:', [round(json.load(open(f'{O}measure_M_seed{s}.json'))['primary']['reading']['degree'],4) for s in '012'])
"
right of 180 held-out episodes, per running state 0 to 4: whole read | best piece of 1, 2, 4 or 8 directions
T/0 180|180 180|180 180|180 180|180 180|180 -> nominated
T/1 180|180 180|180 180|180 180|180 180|180 -> nominated
T/2 180|180 180|180 180|180 180|180 180|180 -> nominated
C/0  13| 14 179|180 180|180 180|180 180|180 -> nominated
C/1  13| 14 177|172 174|167 177|175 173|162 -> nominated
C/2  13| 13 176|178 177|175 180|171 180|179 -> nominated
F/0  13| 14  32| 34  26| 30  19| 25  12| 20 -> read failed its floor: no size's piece reaches four fifths
F/1  13| 14  12| 17  21| 18  24| 19  21| 20 -> read failed its floor: no size's piece reaches four fifths
F/2  13| 14  18| 24  25| 29  20| 26  20| 24 -> read failed its floor: no size's piece reaches four fifths
M/0 180|180 180|180 180|180 179|179 178|178 -> nominated
M/1 180|180 180|180 180|180 180|180 180|180 -> nominated
M/2 180|180 180|180 180|180 180|180 180|177 -> nominated
separation: {'0': 1.0051, '1': 0.9926, '2': 0.9974} all clear 0.5: True
arm M readings: [0.4886, 0.486, 0.5449]
```

The middle limb of failure 2, "the second run clears the bar and the first
does not", is exactly the toy's state: on arms T, C and M a piece reaches 144
of 180 at every running state past the injection, and on arm F none does at
any (at most 34). **This is the fatal finding of the review of version 2,
RT-212, and it still fires on the free arm.** What the design does about it
is unchanged in kind and sharper in aim: the floor now sits on the piece that
is transplanted (RT-230), it turns the firing into a registered *no verdict*
on arm F on every seed, and the withdrawn number is not reported as a
reading. The route (b) search for a target the free system does carry found
none at the floor (section 7.2, item 1), so the failure is caught rather than
repaired, and the registration says so. **A second place the same failure
fires, new in this version and stated in it:** the named agent's read that
control 2 needs cannot be recovered at the floor on any toy model (section
7.3, item 2). That control carries no pre-stated number, by ruling.

**3. A cell that is empty by construction. Does not fire on the reading. It
describes control 2 on the toy, which the text says in terms. MEASURED.** Part
one, the cells: control 6's two cells on the relaxed set, the positions
control 4 transplants at, and control 2's reach:

```
$ .venv/bin/python -c "
import json
O='experiments/rehearsal-successor-measure/out-controls-rerun/'
for a in 'TCFM':
  for s in '012':
    c=json.load(open(f'{O}measure_{a}_seed{s}.json'))['primary']['controls']['6']
    print(f' {a}/{s} same-value trials', c['same_value_trials'], 'different-value trials', c['different_value_trials'])
a=json.load(open('experiments/rehearsal-successor-measure/out-short-prestated-run/part_a.json'))
print('control 4 as redefined, positions transplanted per pair:', a['positions_per_pair'])
print('control 2: toy models on which it returned a figure:', sum(1 for a_ in 'CF' for s in '012' if json.load(open(f'{O}measure_{a_}_seed{s}.json'))['control2']['status']!='no verdict'), 'of 6 it applies to')
"
 T/0 same-value trials 81 different-value trials 719
 T/1 same-value trials 81 different-value trials 719
 T/2 same-value trials 81 different-value trials 719
 C/0 same-value trials 81 different-value trials 719
 C/1 same-value trials 81 different-value trials 719
 C/2 same-value trials 81 different-value trials 719
 F/0 same-value trials 81 different-value trials 719
 F/1 same-value trials 81 different-value trials 719
 F/2 same-value trials 81 different-value trials 719
 M/0 same-value trials 81 different-value trials 719
 M/1 same-value trials 81 different-value trials 719
 M/2 same-value trials 81 different-value trials 719
control 4 as redefined, positions transplanted per pair: {'max': 21, 'mean': 5.212500095367432, 'min': 1}
control 2: toy models on which it returned a figure: 0 of 6 it applies to
```

Both of control 6's cells have trials on every arm and seed, so the RT-173
repair holds. Control 4 as redefined transplants at one position or more in
every pair, so it is never an empty test (that line is from the short
pre-stated run; its check added that the transplant does write there, since
noise added to the donor's state changes the outputs on all twelve models).
Control 2 returned
a figure on none of the six toy models it applies to, and has zero clearing
site sets by construction on arms T and M, which the repairs rulings' item 5
records as not applicable. **So control 2's cell is empty at toy scale. The
text does not hide it: the registration says the control never ran, it
carries no pass line, and its no verdict is the expected result.** Whether a
control in that state should be in the registered design at all was John's to
rule and he ruled it stays (section 7.3, item 2). Part two, the generator
property that empties a cell, is section 4.2's distinctness, read and named
there. Part three, thresholds at both ends, for every threshold this version
attaches to a count:

```
$ .venv/bin/python -c "
from fractions import Fraction as Fr
from math import comb
n=3000
def tail(k): return Fr(sum(comb(n,i)*3**(n-i) for i in range(k,n+1)), 4**n)
k=min(k for k in range(760,820) if tail(k)<=Fr(1,20))
print('learn-both bar: smallest k with P(X>=k | n=3000, p=1/4) <= 0.05:', k, 'share %.4f'%(k/n), 'tail %.4f'%float(tail(k)))
print('a fully collapsed arm (own-directed exactly 1/4) is read as NOT collapsed with probability %.4f per seed'%float(tail(k)))
for p in (0.2633, 0.56):
    f=(1-p)/7; print(f'no-transplant rule at own-directed {p}: formula {f:.4f}, broken-pairing rate 0.1250, miss {0.125-f:.4f}, flagged by the 0.018 room: {0.125-f>0.018}, margin {0.125-f-0.018:.4f}')
print('largest measured miss 2026-09-21: %.6f; inside 0.018: %s'%(0.07625-(1-0.589)/7, 0.07625-(1-0.589)/7<=0.018))
print('piece floor on the toy: four fifths of 180 held-out episodes =', Fr(4,5)*180, '; one episode is %.4f of the scale'%(1/180))
"
learn-both bar: smallest k with P(X>=k | n=3000, p=1/4) <= 0.05: 790 share 0.2633 tail 0.0485
a fully collapsed arm (own-directed exactly 1/4) is read as NOT collapsed with probability 0.0485 per seed
no-transplant rule at own-directed 0.2633: formula 0.1052, broken-pairing rate 0.1250, miss 0.0198, flagged by the 0.018 room: True, margin 0.0018
no-transplant rule at own-directed 0.56: formula 0.0629, broken-pairing rate 0.1250, miss 0.0621, flagged by the 0.018 room: True, margin 0.0441
largest measured miss 2026-09-21: 0.017536; inside 0.018: True
piece floor on the toy: four fifths of 180 held-out episodes = 144 ; one episode is 0.0056 of the scale
```

The bar reproduces at 790 of 3,000. The no-transplant rule fires on the
broken end and passes on the working end, and the case the allowance was set
from is inside it; at the bar it detects a broken pairing by 0.0018, which is
printed in the reporting table. The lesion collapse line misreads a fully
collapsed arm 4.85% of the time per seed, which is what the two-of-three
clause of section 8.2 is for. The piece floor is 144 of 180 on the toy,
against a no-information level of about 13 and a best free-arm piece of 34 at
one end and built-arm pieces of 150 to 180 at the other, so it has room on
both ends on the toy; one episode is 0.0056 of the scale, which is why the
device is named and why the caution about 180 held-out episodes is carried
with the ruled counts (section 9). **Control 4's pass line, bit-identical
outputs, has no working end to test: it cannot fail on a correctly built
model. That is said in section 7.3, item 4, and it is why the control is
described as a known-answer test and not as evidence.** The lesion figures
themselves:

```
$ .venv/bin/python -c "
import json
g=json.load(open('experiments/rehearsal-successor-measure/out-repairs/gate_base.json'))['runs']
for k in sorted(g):
    if k[0] in 'TCFM': print(k, 'lesioned own-directed %.4f'%g[k]['lesioned_own'], 'collapses:', g[k]['lesion_collapses_own'])
"
C/base/0 lesioned own-directed 0.1780 collapses: True
C/base/1 lesioned own-directed 0.1830 collapses: True
C/base/2 lesioned own-directed 0.1703 collapses: True
F/base/0 lesioned own-directed 0.1760 collapses: True
F/base/1 lesioned own-directed 0.1850 collapses: True
F/base/2 lesioned own-directed 0.1940 collapses: True
M/base/0 lesioned own-directed 0.2230 collapses: True
M/base/1 lesioned own-directed 0.2190 collapses: True
M/base/2 lesioned own-directed 0.2203 collapses: True
T/base/0 lesioned own-directed 0.2467 collapses: True
T/base/1 lesioned own-directed 0.2510 collapses: True
T/base/2 lesioned own-directed 0.2733 collapses: False
```

And the site-set family this version registers, counted by the rule. The
command and its output are section 18, which prints the list itself: 325 site
sets and 1,300 comparisons on the registered model, 45 and 180 on the toy.

**4. A claim of measurement with no record, or a record that does not
reproduce. Fires on one class of figure, said so in the text. MEASURED.** Part
one, the two sweeps, run on sections 0 to 16 of this file (cut at this
section's heading, because this section's own output blocks match the
patterns and would count themselves):

```
$ grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' "$T/v4-through16.md"
759
$ grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' "$T/v4-through16.md"
233
$ grep -c MEASURED "$T/v4-through16.md"; grep -c ARGUED "$T/v4-through16.md"; wc -l < "$T/v4-through16.md"
68
14
3406
$ grep -c 'checked: the check of the short run' "$T/v4-through16.md"
8
```

Part two was run by reading every MEASURED claim this version adds or changes
against the file named beside it: the controls re-run's findings and its
`table.md`, `summary.json`, `nominate_*` and `measure_*` files; the check of
the re-run; the short pre-stated run's findings and its `table.md`; the
review of version 3; and the three rulings files. The commands in failures 1
to 3 and candidate 7 are the ones that can be shown. **Where it fires, and
what the text does about it:**

- **Every figure taken from the short pre-stated run was unchecked when this
  version was first filed, and is checked now.** The check ran the script
  again and got byte-identical files (main line at `53c8100`). Each such
  figure carries the words "checked: the check of the short run" (the count
  above).
- **The figure on the average over a site does not reproduce to the episode
  under a different order of addition** (three of eight toy figures move by
  one of 180; the check of the short run, finding 11). The text says the toy
  figures are good to an episode or two and requires 64-bit averaging in the
  registered code (section 7.2, item 3).
- **Version 3's figures for arm C's seeds 1 and 2 do not hold under the piece
  rule** and are replaced by the controls re-run's (RT-230).
- **One figure in the controls re-run's own prose does not reproduce to its
  last digit**: the 0.0100 for arm M seed 1, which is 0.0099 (the check of the
  re-run). This version quotes 0.0099.
- **The competing solvers' figures were taken before the piece rule**, and
  the text says so in three places; the run under the rule is owed before the
  registration review, by ruling (section 7.3, the last paragraph).

The repository's own two checkers, run on the whole document as it stands:

```
$ .venv/bin/python scripts/check_citations.py --only docs/successor-experiment-proposal-2026-10-03-v4.md
[CONFIDENT] 0 reference(s) name a file that is not in the repository
  (version 3 had six, all to the label search and its check, which had not merged then; both are on the main line now, and so is the check of the short pre-stated run)
[CONFIDENT] 1 exact figure(s) absent from the one file their sentence cites
  (the count of arm M's entangled gate episodes, in a sentence of section 5.3 carried unchanged from version 3: the file cited holds the share and not the count, which is that share of the gate's episodes)
$ .venv/bin/python scripts/check_single_source.py --only docs/successor-experiment-proposal-2026-10-03-v4.md
[CONFIDENT] Group 1: a dollar figure the ledger does not contain: 0 found
[CONFIDENT] Group 2: in the ledger, but the sentence names another file as source: 2 found
  (both in one sentence of section 12.2, cited to the 2026-09-21 ruling that set the two releases, which is the figures' source; the ledger carries them because the ruling did)
```

That the checkers see so little of this document is a statement about the
checkers, not about the rest being clean.

**5. A command that creates something while documented as creating nothing.
Does not fire on anything this document runs; one gap stated. MEASURED.** The
proposal runs nothing that touches a vendor. The list's own test, run by this
session (the last lines of its output; every line above them is `[ ok ]`):

```
$ experiments/06-mvm-0a-constructed-self-index/src/check_launcher_argument_guard.sh
  ...
negative control: the check must FAIL on an unguarded launcher
  [ ok ] an unguarded launcher is REJECTED (exit 0, no refusal, no guard)
  [ ok ] so these checks detect the property rather than always passing

all checks pass. nothing was created and nothing was spent.
```

The gap is the one RT-228 named and section 5 states: the launcher is named
(`launch_a3_fetch_first.sh`, which carries the guard), the registered
`launch_a3.sh` is not used, and the successor's training entry point for arms
T, C and M on the rented machine does not exist yet.

**6. A remote step tested only against stand-ins. The launcher's check passes;
the design has three such steps, each stated. MEASURED.**

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/src/check_remote_forms.py
remote background starts, run against a real local shell (| cat stands in for ssh; the background program holds 8s)

launch_a3_fetch_first.sh
  [ ok ] launch_a3_fetch_first.sh line 616: returned after 0.0s -- returns at once
  [ ok ] launch_a3_fetch_first.sh line 697: returned after 8.1s -- HOLDS the connection; cut off by the launcher's inline cap 60s (line 702)

negative control: the pre-fix form of 2026-09-25 must be REJECTED
  [rejected] stand-in line 1: returned after 8.1s -- HOLDS the connection and nothing cuts it off: a real ssh would wait for the background program
  [ ok ] the uncapped `cd … && nohup … &` stand-in is rejected, so this check detects the hang

all checks pass. Nothing was rented and nothing was spent.
```

On the design: the handshake's machine half has been tested only against
stand-ins, and the registration says what is true of it, as ruled (W9,
decision 18); arm M's code has never run on the rented machine (W9, step 4 of
section 11); the tripwire does not exist as code yet (section 12.5). All
three are said in the text, and none is counted as tested. **One step of a
different kind is in the same state and is said too: the code that withholds
a reading when a control that holds fails does not exist yet** (section 6.4,
item 5); on the toy every such control passed, so the withholding has never
been exercised.

**Candidate 7. An outcome line a plan states in advance that the design
cannot produce on the path it expects. Fires on one line, which the text
states; does not fire on the others. MEASURED.** The drafted test: for each
pre-stated line, name the code path that prints each signal it needs, and
show that path can run in the order the line requires. Run on the committed
outputs:

- **Arm M's pass line** ("between 0.3 and 0.7 on every seed, and within 0.10
  of its true-slot reading"): produced, both halves, at the registered site
  sets (failure 2's output above; section 5.3).
- **The separation line** (0.5 on every seed): produced (failure 2's output).
- **The fifth outcome term** ("metric validated, degree not read"): produced.
  It is where the toy lands, by the path the text expects: the anchors
  separate and arm F returns "read failed its floor".
- **Control 4's pass line** (bit-identical outputs at the two action
  positions): produced on all twelve, by code committed before its output,
  and reproduced byte for byte by its check (main line at `53c8100`).
- **Control 2's reported description**: **cannot be produced on the path the
  toy offers, on any model.** The text says so in terms and attaches no line
  to it. This is the one place the candidate fires.
- **The lesion description**: "arm T collapses on two of three seeds", which
  is what the path produced (failure 3's output above).
- **The rider**: can produce a reading on arms C, F and M on 0 of 9 toy pairs
  on the path it expects, and the text says so with the two reasons (section
  7.2, item 7). Accepted as the report.
- **The two-of-three rule for an arm whose seeds disagree** (section 3):
  ruled, and **never produced on the toy**, where every arm's three seeds
  agree. The code that applies it does not exist yet. Stated here so that it
  is not counted as rehearsed.
- **The $10 wager** (section 12.8), and the money lines of section 12, which
  no ruling of 2026-10-03 changed:

```
$ .venv/bin/python -c "
spent=228.15; first=44.0; second_no_rerun=84.06+12+23; note_both=161.90
print('ruled split: first release %.2f + second release without its re-run line %.2f = %.2f'%(first,second_no_rerun,first+second_no_rerun))
for lo,hi,label in ((29.70,41.76,'arm M three runs only, 1.94 in the first release'),(32,44,'arm M as ruled, 32 to 44, 1.94 inside')):
    for m in (lo,hi):
        left=450-spent-(first+second_no_rerun)-m
        print(f'  {label}: arm M {m:.2f}: programme after {spent+first+second_no_rerun+m:.2f}, left {left:.2f}, meets the 10 floor: {left>=10}')
for m in (32,44):
    print(f'note split (161.90 + arm M {m}): programme after {spent+note_both+m:.2f}, left {450-spent-note_both-m:.2f}')
print('first release development line, four arms at 1.943 each: %.2f of the 10 line'%(4*1.943))
"
ruled split: first release 44.00 + second release without its re-run line 119.06 = 163.06
  arm M three runs only, 1.94 in the first release: arm M 29.70: programme after 420.91, left 29.09, meets the 10 floor: True
  arm M three runs only, 1.94 in the first release: arm M 41.76: programme after 432.97, left 17.03, meets the 10 floor: True
  arm M as ruled, 32 to 44, 1.94 inside: arm M 32.00: programme after 423.21, left 26.79, meets the 10 floor: True
  arm M as ruled, 32 to 44, 1.94 inside: arm M 44.00: programme after 435.21, left 14.79, meets the 10 floor: True
note split (161.90 + arm M 32): programme after 422.05, left 27.95
note split (161.90 + arm M 44): programme after 434.05, left 15.95
first release development line, four arms at 1.943 each: 7.77 of the 10 line
```

  The wager meets its floor on every split and at both ends of the range.

Whether the candidate is a new species or an instance of failure 3 is John's
ruling, still open; on this version it catches control 2, which failure 3's
test catches too.

**What this pass leaves open, in one place.** The competing solver's run
under the piece rule; the check of this version and of the late-evening
ruling's record; the code owed before step 4 of section 11 (the training
entry point for arms T, C and M, the tripwire, the withholding of a reading
on a failed control, control 2's twenty random pieces, and the two-of-three
rule); and the reviewer's own pass,
which is still owed, as the protocol says.

---

## 18. The printed site list for the registered model

The site list is registered as the rule that generates it (section 7.2, item
2), and the registration prints the list beside the rule. This is the list,
printed by the rule and not typed by hand. A layer set is written as its
first and last running state: "3-5" is states 3, 4 and 5 together. State 0 is
the running state straight after the input embedding, where the acting
channel is added; states 1 to 12 are the outputs of the twelve blocks. Each
row lists every layer set that begins at that state, and the position sets
each of them is a candidate at. Every site set whose layers include state 0
is a candidate at the action position set only; every other layer set is a
candidate at all four position sets (`action`, the action position alone;
`action+ans`, the action position and the answer-marker token just before it;
`action+3`, the action position and the three positions before it;
`post-identity`, every position from the model's first own turn to the
action). No site set spans every position. The toy's list is printed after
it, for comparison with the 45 the controls re-run's code asserts.

```
$ .venv/bin/python -c "
def contiguous(n): return [(a,b) for a in range(n) for b in range(a,n)]
P4=['action','action+ans','action+3','post-identity']
def name(a,b): return str(a) if a==b else f'{a}-{b}'
for label,n in (('registered model: 13 running states (0 = after the input embedding, 1 to 12 = after each block)',13),('toy model: 5 running states',5)):
    L=contiguous(n); total=0
    print(label)
    for a in range(n):
        sets=[name(x,y) for x,y in L if x==a]
        ps=['action'] if a==0 else P4
        total+=len(sets)*len(ps)
        print(f'  first state {a:>2} | at {", ".join(ps)} | layer sets: {", ".join(sets)} | {len(sets)} x {len(ps)} = {len(sets)*len(ps)} site sets')
    print(f'  total: {total} site sets, {4*total} comparisons at sizes 1, 2, 4 and 8')"
registered model: 13 running states (0 = after the input embedding, 1 to 12 = after each block)
  first state  0 | at action | layer sets: 0, 0-1, 0-2, 0-3, 0-4, 0-5, 0-6, 0-7, 0-8, 0-9, 0-10, 0-11, 0-12 | 13 x 1 = 13 site sets
  first state  1 | at action, action+ans, action+3, post-identity | layer sets: 1, 1-2, 1-3, 1-4, 1-5, 1-6, 1-7, 1-8, 1-9, 1-10, 1-11, 1-12 | 12 x 4 = 48 site sets
  first state  2 | at action, action+ans, action+3, post-identity | layer sets: 2, 2-3, 2-4, 2-5, 2-6, 2-7, 2-8, 2-9, 2-10, 2-11, 2-12 | 11 x 4 = 44 site sets
  first state  3 | at action, action+ans, action+3, post-identity | layer sets: 3, 3-4, 3-5, 3-6, 3-7, 3-8, 3-9, 3-10, 3-11, 3-12 | 10 x 4 = 40 site sets
  first state  4 | at action, action+ans, action+3, post-identity | layer sets: 4, 4-5, 4-6, 4-7, 4-8, 4-9, 4-10, 4-11, 4-12 | 9 x 4 = 36 site sets
  first state  5 | at action, action+ans, action+3, post-identity | layer sets: 5, 5-6, 5-7, 5-8, 5-9, 5-10, 5-11, 5-12 | 8 x 4 = 32 site sets
  first state  6 | at action, action+ans, action+3, post-identity | layer sets: 6, 6-7, 6-8, 6-9, 6-10, 6-11, 6-12 | 7 x 4 = 28 site sets
  first state  7 | at action, action+ans, action+3, post-identity | layer sets: 7, 7-8, 7-9, 7-10, 7-11, 7-12 | 6 x 4 = 24 site sets
  first state  8 | at action, action+ans, action+3, post-identity | layer sets: 8, 8-9, 8-10, 8-11, 8-12 | 5 x 4 = 20 site sets
  first state  9 | at action, action+ans, action+3, post-identity | layer sets: 9, 9-10, 9-11, 9-12 | 4 x 4 = 16 site sets
  first state 10 | at action, action+ans, action+3, post-identity | layer sets: 10, 10-11, 10-12 | 3 x 4 = 12 site sets
  first state 11 | at action, action+ans, action+3, post-identity | layer sets: 11, 11-12 | 2 x 4 = 8 site sets
  first state 12 | at action, action+ans, action+3, post-identity | layer sets: 12 | 1 x 4 = 4 site sets
  total: 325 site sets, 1300 comparisons at sizes 1, 2, 4 and 8
toy model: 5 running states
  first state  0 | at action | layer sets: 0, 0-1, 0-2, 0-3, 0-4 | 5 x 1 = 5 site sets
  first state  1 | at action, action+ans, action+3, post-identity | layer sets: 1, 1-2, 1-3, 1-4 | 4 x 4 = 16 site sets
  first state  2 | at action, action+ans, action+3, post-identity | layer sets: 2, 2-3, 2-4 | 3 x 4 = 12 site sets
  first state  3 | at action, action+ans, action+3, post-identity | layer sets: 3, 3-4 | 2 x 4 = 8 site sets
  first state  4 | at action, action+ans, action+3, post-identity | layer sets: 4 | 1 x 4 = 4 site sets
  total: 45 site sets, 180 comparisons at sizes 1, 2, 4 and 8
```

**The count this implies, frozen with the list:** 325 site sets, each at four
sizes of piece, so 1,300 comparisons in the nomination family for each arm
and seed. Under the stricter variant (the sensitivity row) the first row
drops out: 312 site sets and 1,248 comparisons. Both agree with section 7.2,
item 2, and with the review of version 3, which recomputed them ("What was
checked and held"). The registered measurement code asserts the count before
it runs, as the toy code does.

---

## 19. The seven questions put to John, each now ruled as suggested

===== END OF RECORD 4, part 11 =====

