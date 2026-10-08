*This is file 15 of 33 of one review packet, pasted into a single conversation. It contains record 5 part 3 of 4 (the inside reviewer's findings on version 4 (Gate A, tier 1)). Reply with one short line saying you have it, and wait for the rest: the brief is record 1, in file 1, and your review comes only after file 33 arrives. If this file looks cut short, say so now.*

===== RECORD 5 of 25, part 3 of 4 - the inside reviewer's findings on version 4 (Gate A, tier 1) - `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-claude-code.md` (complete file, 80,950 characters) =====
**What was measured.** `registered_shape_timing.py` times, on this laptop's
processor (Apple M4), the forward passes the rule makes over the 600
development pairs, at the toy shape and at the registered shape:

```
$ .venv/bin/python experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-successor-v4-gate-a-scripts/registered_shape_timing.py
torch 2.12.1, threads 4, sequence 56, pairs 600
toy shape (160 wide, 4 blocks): 1,265,191 parameters; capture 0.52 s; one transplant pass over 600 pairs 0.506 s (median of 6); one read fit 0.02 s
   nomination grid: 45 site sets -> 227 passes, 25 fits -> about 1.9 minutes per model and seed (control 2's own grid, where it runs, about doubles it)
registered shape (448 wide, 12 blocks): 29,049,735 parameters; capture 6.55 s; one transplant pass over 600 pairs 4.590 s (median of 6); one read fit 0.09 s
   nomination grid: 325 site sets -> 1627 passes, 65 fits -> about 124.6 minutes per model and seed (control 2's own grid, where it runs, about doubles it)
registered against toy, per model and seed: 65 times
twelve registered models, nomination grids only: about 24.9 hours on this processor
```

**What it shows.** The arithmetic is honest at the toy end: it predicts
about 1.9 minutes per toy model, and the controls re-run this session ran took
1,485 seconds for twelve models with every control, about 2 minutes each. At
the registered shape one model's nomination is about two hours on this
processor; the twelve registered models about a day, more where control 2 runs
its own grid, and more again if the registered episodes are longer than the
toy's 56 tokens (no text fixes that length). So the text's argument holds:
the work fits on the laptop, at a day or two of processor time and $0, and
step 5a's single free-model run is about two hours. It is now a measurement
rather than an argument. One limit: the read was timed on random labels and
may take longer on real ones; it is a small share of the total either way.

**The second half (ARGUED).** Ruling 3 of record B names the device for "the
registered accuracy", the fit. The nomination also chooses among candidate
site sets by their development ownership-only shares, and on the entangled
model seed 1 that choice was decided by one episode in 600 (version 4, lines
776 to 782). A transplant pass on a different device or number format can move
a share by an episode just as a fit can (RT-232 was exactly that for fits). If
the registration names the device for the fit and not for the transplant
passes, the stop at step 5a and every nomination can turn on an unregistered
choice. *Suggestion:* name the device and number format for the whole
nomination and reading, not only for the fit, and carry the timing above (or
the step-4 development runs' own timing) as the measurement behind "it fits on
the laptop".

---

## 2. Satisfied by the wrong thing

| Way the text could be satisfied by a model with none of the structure it claims to detect | Severity | Finding |
|---|---|---|
| A free model reads its own name off the text near the action, if the registered grammar keeps the closed design's rendering, and clears the fit floor through a name cue rather than a carried answer | serious | RT-239 |
| The high anchor reads near 1 through any piece that holds the label and does nothing, which is what "entangled" means operationally; the reading cannot tell entangled from "the answer lives where the read did not look" | (stated by version 4 as weakness W12; not re-filed) | — |
| The whole-state transplant on the entangled and mixed models moves the action even when the donor's identity dictates the same value (control 6), so it carries more than identity | (stated as W11; not re-filed) | — |
| A model at chance passes the printed whole-state floor at every site set | serious | RT-238 |
| The competing-solver test covers a model that fails the task; the toy's free model is a model that does the task by another route, and the weakness ruled on 2026-10-04 does not say so | worth-noting | RT-246 |

### RT-239 (serious; MEASURED that the texts say what is quoted, ARGUED for the consequence). The registration does not state the grammar that removes the model's own name from the act

**What version 4 says.** Section 4.1 (lines 498 to 504): "The grammar extends
the registered Amendment A3 grammar (`curriculum_a3.py`, the episode generator
committed 2026-09-15), which already has the pieces: four agents, a closed
vocabulary, ten turns, eight value slots, every revised item assigned by all
four agents before anyone revises it ... The rehearsal's shrunken version of
it is `experiments/rehearsal-successor-measure/src/grammar.py`." Line 522:
"The grammar is as version 2 had it." Section 1 (lines 133 to 141): the acting
channel "is the only honest source of ownership in this design, because ...
nothing in the text itself can carry it". Section 7.3, item 4 (lines 1890 to
1896): "The twins are the same text. They differ only in which turns carry the
acting channel."

**What the two grammars say about themselves.** The closed design's grammar,
`experiments/06-mvm-0a-constructed-self-index/src/curriculum_a3.py`, header:
"Twelve turns, four agents, two *contested* items: ... Eight assignment turns
... Four revision turns"; and, under "An honest limit on the design's central
claim": "The revision turn renders as "<marker> assign <item> to <value>", so
at the moment the model acts, its own marker is in the context three tokens
back. A model could learn "the marker at a position where I am acting is
mine" ... reading a name badge at act time rather than carrying a binding."
The rehearsal grammar, `grammar.py`, header, "Two departures from the
registered A3 grammar, both deliberate": "1. **The action turn carries no
marker word.** ... Here the only route to the ownership answer is the acting
channel. 2. **The answer token is never shown.** ... Together these make a
matched pair of episodes ... come out **token-for-token identical**, differing
only in which positions the acting channel fires on."

```
$ grep -n -i "mask\b\|<mask>\|name badge\|no marker word\|carries no marker\|departure\|token-for-token\|answer token\|same text" docs/successor-experiment-proposal-2026-10-03-v4.md
1534:   the running state at the mask token of the own-directed action (the
3271:    at the mask token, scored on held-out development episodes; the label
```

So: version 4 says the closed design's grammar has ten turns; it has twelve.
And the two departures that make the act free of the model's own name, and
make the twins the same text, appear in version 4 only as two passing
mentions of "the mask token".

**Why this matters (ARGUED).** The registered generator is still to be written
(section 11, step 3, "the built generator"), and it is written from the
registration text. Read as written, the text points at the closed design's
generator as the base and at the rehearsal's as its shrunken copy, and only
the shrunken copy says the departures exist. A generator built by extending
`curriculum_a3.py` as the text says would show the model its own marker word
three tokens before it acts. Then: the registered read's label, "which marker
word is the model's own", is in the text near the action, so a free model can
clear the fit floor by copying a name rather than by carrying an answer; the
twins are no longer the same text, so the known-answer reasoning of control 4
and of section 6.1 no longer holds as stated; and the ownership signal the
whole design is built to isolate (ledger item RT-17, the finding that any
learnable ownership cue in the tokens is a fingerprint) is back. That is a
reading satisfied by the wrong thing, on the one model the experiment exists
to read.

**What would fix it.** Register the episode format itself, as the rehearsal
grammar's header gives it: the turns and their order, the action-turn
rendering with no marker word, the masked answer, and the property that twins
are token-for-token identical, with the self-test that asserts it named as
part of the registered generator's tests. Correct "ten turns" as a statement
about the closed design's grammar. Say whether the closed design's
end-of-episode question sets are carried (this decides RT-237's doubt).

### RT-246 (worth-noting, ARGUED). The ruled weakness about the competing solver can be stated more exactly

John ruled (2026-10-04, ruling 7) that section 13 gains: "the toy's ordinary
competing solver fails the task, so its 'no verdict' shows only that the
measure returns nothing on a model that has not learned the task. It does not
show what the measure does on a model that does the task by another route."

The toy has such a model: the free model. Version 4, section 5.4 (lines 986 to
999): it scores 0.5513 to 0.5597 on the own-directed condition against 0.2340
to 0.2383 for the ownership-blind solver, and solves it "by attending to the
value tokens on the turns the acting channel marked, with no need to know
which marker word those turns carry", and "the free toy model does not carry
the marker word forward to where it acts". The measure returns no verdict on
it ("read failed its floor"). So the toy does show what the measure does on
one model that does the task by a route other than carrying the registered
label: it returns nothing, and says why. What the toy does not show is a model
that does the task by a route that *also* leaves the label readable where the
model acts, and the obvious such route is the name cue of RT-239. *Suggestion:*
write the weakness with both halves, so a reader learns which "other route"
has been seen and which has not.

---

## 3. No verdict

| Way the registration text could fail to return a verdict on the runs it is written for | Severity | Finding |
|---|---|---|
| The free model's gate cannot be evaluated, so it fails by S8 and the free model is never read | fatal | RT-237 |
| A no verdict on the separable model, or the two-model fallback, has no registered outcome term | serious | RT-241 |
| The entangled model's read misses the floor at the registered width | serious | RT-240 |
| A model at chance reaches the arithmetic with a divisor of zero under the printed floor | serious | RT-238 |
| The processor proves impractical at full size (record B: a fresh question for John) | worth-noting | RT-245 |

### RT-241 (serious, ARGUED). The outcome map has holes

**What version 4 says.** The outcome table (lines 307 to 313); "What a no
verdict maps to" (lines 456 to 467): arm C fires the two-model fallback, arm M
is dropped, arm F after T and C separate is the fifth term; section 7.4 freezes
"the five registered outcome terms of section 3, and what a no verdict on each
arm maps to" (lines 2061 to 2062). Section 8.1 (lines 2188 to 2189): "An arm
that fails, after the one permitted re-run, gives outcome R3 for that arm".
Line 305: "nothing in this document may report an outcome in other words."

**The holes, each a state the registered runs can reach.**

1. **No verdict on arm T, the separable model.** Not in the list of three.
   It can happen: arm T's reading is withheld if control 1 fails on it (a
   control that holds on arm T only), if its no-transplant rate misses, or if
   its floor is missed on fresh episodes. With arm T reading on fewer than two
   seeds, "metric validated" cannot be met (lines 481 to 483), R2 is not met (the
   measure did not fail to separate; it was not computed), R3 is not met (no
   gate failed), and no other term applies. Section 7.4 says the frozen list
   covers "each arm"; it covers three.
2. **The two-model fallback has no term.** A no verdict on arm C "fires the
   two-arm fallback" (line 462). Then R1 and R2 both require separating arms
   T and C, which cannot be done. Lines 820 to 827 say "the R1 sentence is
   correspondingly weaker" and that the registration "says that in those
   words", but no words are registered, and line 305 forbids reporting in
   other words.
3. **"R3 for that arm" against R3 as the experiment's outcome.** R3 in the
   table is the whole experiment's outcome ("this recipe and this size are not
   yet a place to study mechanism"). Line 2188 makes a gate failure "R3 for
   that arm". A gate failure on arm M, a model whose no verdict merely drops
   it, would then be read either as the whole experiment's R3 or as an
   arm-level R3 that the table does not define.
4. **The free model fails its channel-removal check** (fewer than two seeds
   collapse; or RT-237's clause). Section 5.4 says it is then not read. Which
   term follows is not said: R3 if this check is a "gate" (section 8 calls it
   one), the fifth term if it counts as a no verdict.
5. **A built model that fails its gate in step 5b.** R3 is "after the one
   permitted re-run". On the ruled split the re-run is funded only in the first
   release (section 12.3; section 12.4 removes it from the second), and step
   5a's text gives it to the free model. Whether a separable, entangled or
   mixed model that fails at step 5b gets a re-run before R3 is declared, and
   from what money, is not stated.

**What would fix it.** One table in section 3, frozen in section 7.4, with a
row for every arm-level state (reads; no verdict; fails its gate after a
re-run; fails the channel-removal check, for arm F) and the registered term
each combination gives, including the fallback's own term. The ruling that
created the fifth term (2026-10-03, page 11) is the precedent: it closed the
same kind of hole (RT-182, the no-verdict finding on version 1) for three arms
and not the fourth.

---

## 4. Over-reading

| What a result could be read as claiming beyond what it measures | Severity | Finding |
|---|---|---|
| "The label search's three candidates reach 0.733, 0.383 and 0.478" read as three candidates' figures | worth-noting | RT-242 |
| "The two forms of the floor never disagree on the toy" read as a property of the toy, when it holds only where the models have learned the task | worth-noting | RT-243 |
| The ruled sentence about the competing solver's misses | worth-noting | RT-244 |
| "Metric validated" read as validation of a measure of degree in general; it is validation at the sites the procedure nominates, on built models that differ in more than degree, with a middle anchor that is a mixture by item | (stated by version 4 as W1, W2, W10; ARGUED here that the outcome term's own words invite the reading, and the registered report should carry W1's hedge in the same sentence as the term) | — |

### RT-242 (worth-noting, MEASURED). The label-search sentence quotes one candidate's three seeds as three candidates

Version 4, lines 1384 to 1389: "The best is 0.789, from candidate 1 ... and
that from position spans that start at one of the model's own turns ...;
anchored at the action position the three candidates reach 0.733, 0.383 and
0.478." The findings table it cites (`docs/2026-09-26-free-arm-label-search.md`,
section 4) has, for candidate 1 on the free model, "0.733 / 0.483 / 0.789 |
0.733 / 0.383 / 0.478", where the two cells are the best over all 60 site sets
and over the 45 fixed-extent ones, each given as seeds 0 / 1 / 2. From the
committed verdict files (`older_figures.py`):

```
  own-turn-pair    best over all 60 site sets 0.789; best over the fixed-extent 45 0.733; per seed [0.733, 0.483, 0.789]; clears: False
  own-source-turn  best over all 60 site sets 0.456; best over the fixed-extent 45 0.417; per seed [0.45, 0.45, 0.456]; clears: False
  own-value        best over all 60 site sets 0.633; best over the fixed-extent 45 0.633; per seed [0.611, 0.611, 0.633]; clears: False
```

So 0.733, 0.383 and 0.478 are candidate 1 on seeds 0, 1 and 2; the three
candidates' best over those site sets are 0.733, 0.417 and 0.633. The sentence
was carried from version 3 (line 1105). Nothing ruled rests on it and every
figure stays under 0.80. *Fix:* "anchored at the action position, candidate 1
reaches 0.733, 0.383 and 0.478 on seeds 0, 1 and 2, and candidates 2 and 3 at
most 0.417 and 0.633."

### RT-243 (worth-noting, MEASURED). The two forms of the whole-state floor do disagree on the toy, on models near chance

Version 4, lines 1118 to 1125: the plain form "is printed beside it everywhere,
so a reader can see whether the two readings of the ruled sentence ever
disagree; on the toy they never did (MEASURED: 0 disagreements across all site
sets, arms and seeds, the repairs findings at `882f252`, section 3 ...)".
`floor_forms.py` counts every committed floor record that carries both forms:

```
out-repairs/nominate_base_*.json              floor records   4254; the two forms disagree on 576
out-v3-rules/nominate_*.json                  floor records   3672; the two forms disagree on 0
out-controls-rerun/nominate_*.json            floor records   2160; the two forms disagree on 0
out-grammar-c/nominate_base_F_T_C.json        floor records   3188; the two forms disagree on 892
out-competing-solver-run/nominate_*.json      floor records   1080; the two forms disagree on 1080
```

(and 0 in every measurement file). All 576 of the repairs run's disagreements
are in the other-agent control's grids on arms C and F (the named-other
condition, near chance on those models); none is in the own-directed grids
the repairs findings counted. On the competing solver the plain form passes
every row and the registered form none. Each disagreement is the plain form
passing a model near chance. So the sentence is right about the own-directed
grids of the twelve base models, wrong about "the toy", and the record it
misses is the best evidence for the choice the design made: the plain form
would let a model at chance through. *Fix:* narrow the sentence and cite the
disagreements as the reason the corrected form is registered.

### RT-244 (worth-noting, MEASURED). The ruled sentence about the competing solver gets one of its own figures wrong

The sentence ruled into the registration text on 2026-10-04 (ruling 2):
"... its best piece missed the piece rule by 119 or more of 180 and its
untouched rate missed the no-transplant rule by 0.11 or more ...".
`solver_sentence.py` against the committed outputs:

```
piece rule missed by: 119 to 124 of 180  -> '119 or more': True
untouched rate against the formula: 0.1091 to 0.1393  -> '0.11 or more': False
untouched rate beyond the rule's room: 0.0911 to 0.1213  -> '0.11 or more': False
```

The run's own findings had already corrected the same slip in one place
(commit `3d55865`, which the check of pull requests 88 and 89 confirms: "outside
the allowance it is 0.09 to 0.12"); the check's suggested sentence, which John
adopted, reintroduced it. And its first clause, "no site set cleared the floor
at nomination", is true under the code's floor and false under the floor as
version 4 prints it (RT-238). *Fix:* "its untouched rate was 0.109 or more
above the formula, and 0.09 or more outside the rule's allowance", and close
RT-238 so the first clause is true of the text.

---

## The failure-mode pass

One section per entry of `docs/known-failure-modes.md`, in order. Each shows
the command run by this session and what it returned. The author's own pass
(version 4, section 17) was read after this pass was run; nothing below is
copied from it.

### Failure 1. A comparison whose denominator was zero — **fires on the printed floor for a model at chance (RT-238); does not fire on any model that learned the task**

*Part one, where every no-transplant rate comes from.* `failure_mode_pass.py`
prints each of the twelve, with the file and field it was read from
(`out-controls-rerun/measure_{arm}_seed{seed}.json`, `primary.reading`): T 0.0000
on every seed; C 0.0512, 0.0488, 0.0600; F 0.0587, 0.0563, 0.0688; M 0.0125,
0.0175, 0.0138. None is typed in; each is measured.

*Part two, the divisor and the top of the scale at the chosen site set:*

```
  T/0: denominator 1.0000; top of scale 1.0000; reads        (and T/1, T/2 the same)
  C/0: denominator 0.4888; top of scale 1.0000; reads
  C/1: denominator 0.5063; top of scale 1.0000; reads
  C/2: denominator 0.4863; top of scale 1.0000; reads
  F/0: denominator 0.4263; top of scale 1.0000; described only
  F/1: denominator 0.5112; top of scale 1.0000; described only
  F/2: denominator 0.4613; top of scale 1.0000; described only
  M/0: denominator 0.7675; top of scale 1.0000; reads
  M/1: denominator 0.7563; top of scale 1.0000; reads
  M/2: denominator 0.7800; top of scale 1.0000; reads
  smallest denominator among those that read: (0.48625, 'C/2')
```

*The case the printed floor admits:*

```
  solver seed 0 channel_removed : floor asks -0.0053; rows the printed formula admits 180 of 180; denominators among them +0.0000 to +0.0000
  solver seed 0 channel_left_on : floor asks -0.0027; rows the printed formula admits 180 of 180; denominators among them -0.0017 to +0.0017
  solver seed 1 channel_removed : floor asks -0.0160; rows the printed formula admits 180 of 180; denominators among them +0.0000 to +0.0000
  solver seed 1 channel_left_on : floor asks -0.0160; rows the printed formula admits 180 of 180; denominators among them +0.0000 to +0.0033
  solver seed 2 channel_removed : floor asks +0.0027; rows the printed formula admits 0 of 180
  solver seed 2 channel_left_on : floor asks +0.0053; rows the printed formula admits 0 of 180
```

**Disposition.** The top of the scale is the same, 1, on every arm, and the
smallest divisor among the models that read is 0.4863: the per-arm-ceiling
repair (ledger item RT-172) holds. The entry fires on the floor's printed
formula, which admits a divisor of zero or below on a model whose own-directed
accuracy is at or under its no-transplant rate: RT-238.

### Failure 2. A probe target that cannot be recovered in principle — **fires on the free model, and a registered rule catches it**

*Part one, a route sentence, in this design's own words, sections 0 to 16:*

```
  1277: own**. *The route by which that quantity reaches the model's states, in one
  1278: sentence:* the marker word is the input token at every turn the model's own
  1279: assignments are spoken on, so it is carried by the token into the running
  1283: claim, that which marker word is the model's own is forced by the loss at
```

(Line numbers are those of `git show d19f914:...`, which counts from the same
file; the fourth match is the sentence striking version 2's loss claim, not a
route.) A route sentence exists, and it names the token. It names a route to
the state at the model's own assignment turns; it does not name one to the
action position, where the registered read is fitted.

*Part two, the same read and the same bar at the position where the marker
word is the input token, and at the registered action position* (from the
short pre-stated run's committed `part_b.json`; the toy has no separate run of
the first kind, so this is the nearest committed pair of runs):

```
  C/2: whole state at the marker's own token 180; whole read at the action position 176 -> both clear
  F/0: whole state at the marker's own token 180; whole read at the action position 32 -> second clears, first does not
  F/2: whole state at the marker's own token 180; whole read at the action position 18 -> second clears, first does not
  M/0: whole state at the marker's own token 180; whole read at the action position 180 -> both clear
  (T, C/0, C/1 and F/1 have a single-position site and the first own turn is not reported for them;
   their action-position counts are 180, 180, 177 and 12)
  the named agent's read (control 2) on arm F seed 0, per running state (whole, best piece):
    {'0': (16, 20), '1': (95, 92), '2': (137, 139), '3': (127, 115), '4': (102, 102)} -> best 139 of 144 needed
```

**Disposition.** The middle limb, "the second run clears the bar and the first
does not", is the free model's state: the label is fully in the state where it
is spoken and absent where the model acts. This is the fatal finding of the
review of version 2 (RT-212, the empty read on the free model), still firing.
The design catches it, not repairs it: the fit floor on the piece turns it
into a registered "no verdict, read failed its floor", the number the
arithmetic would have returned is withdrawn, and the route (b) search found no
other label at the floor. The same limb fires on control 2's named-agent read
(139 against 144), which carries no line by ruling. Nothing new fires here;
what is new is that the route sentence would change if RT-239 were left open
(the marker word could then also be "the input token" three tokens before the
action).

### Failure 3. A cell that is empty by construction — **fires on one gate clause (RT-237); not on any reported cell**

*Part one, every pre-stated cell, counted:*

```
  control 6, T/0: same-value 81, different-value 719        (C/0, F/0, M/0 the same; every seed the same, per section 17's own block)
  control 4 as redefined, positions per pair: {'max': 21, 'mean': 5.212500095367432, 'min': 1}
  control 2: toy models on which it returned a figure: 0 of 12
  the two-of-three rule: arms whose three seeds disagree on the toy: 0 of 4
  the lesion clause 'the ownership-free state and syntax batteries must hold': fields the gate file records: ['lesion_collapses_own', 'lesioned_other', 'lesioned_own', 'n', 'other', 'other_clears', 'other_correct', 'own', 'own_by_route', 'own_clears', 'own_correct']
  grep of the rehearsal code for a state or syntax battery: (no file)
```

*Part two, the generator property that empties a cell.* Distinct values per
item, drawn without replacement (`grammar.py`, `_content`, `replace=False`),
which is why control 6 runs on the separately generated relaxed set; its 0 of
4,000 on the distinct grammar recomputes from `out/denominator_control6.json`
(`older_figures.out.txt`).

*Part three, every threshold at both ends:*

===== END OF RECORD 5, part 3 =====

