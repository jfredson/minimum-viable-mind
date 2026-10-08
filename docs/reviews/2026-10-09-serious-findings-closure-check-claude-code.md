# Closure check of three serious findings: the floor's missing condition (RT-238), the episode format (RT-239), control 6 (RT-251)

*2026-10-09. Claude Code, as the checker. Laptop only, $0. Method committed
first (`docs/reviews/2026-10-09-serious-findings-closure-check-method.md`,
commit `3cbf88c`). This session wrote none of what it checks. It checks the
main line at commit `dafdaf2`: version 5 of the registration text
(`docs/successor-experiment-proposal-2026-10-07-v5.md`), the frozen code
(`experiments/08-successor-degree/src/`) and the three ledger rows
(`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`, lines 941,
942 and 970). Scripts and their full output are in
`docs/reviews/2026-10-09-serious-findings-closure-check-scripts/`.*

## The verdicts

| Finding | Verdict |
|---|---|
| **The floor's missing condition (RT-238)**: the whole-state floor as printed admitted every site set when own-directed accuracy is at or under the no-transplant rate | **The claim was checked (closed).** The text now states the code's condition, the text's rule and the code agree on all 426,981 inputs tried, and the code refuses every site set in every case built at or under the no-transplant rate |
| **The episode format (RT-239)**: the format was registered as an extension of the closed design's, and its two departures were written nowhere | **The claim was checked (closed).** Every field of section 4.1 holds on every one of 13,800 generated episodes; both named self-tests pass; undoing departure 1 makes both fail, undoing departure 2 makes the token-identity check fail. Three wording points below, none blocking |
| **Control 6 (RT-251)**: control 6 cannot tell copying the donor's answer from copying who is acting | **The claim was checked (closed).** No sentence of version 5, no line of its reporting table and no output label of the frozen code says control 6 discriminates; the two withdrawn sentences appear only quoted as withdrawn, and no decision code reads control 6 |

**The other session's change** (branch `ruled-code-changes-2026-10-09`, at
`d4b03b8`) **cannot affect these verdicts.** Every function the first two rest
on is identical there; for control 6 the branch changes the reporting
table's function and the outcome functions, but only by adding a new column
and the new outcome words, and it still reads control 6 nowhere in its
decision code (section 4).

---

## 1. The floor's missing condition (RT-238)

**What the closure says.** Version 5's section 6.4 item 1 and section 9 state
the code's condition that the floor's requirement be above zero, so the text
and the code are the same rule.

**The code.** `measure.floor_check`, printed by
`floor_check.py` (output `floor_check.out.txt`, part 1):

```
def floor_check(whole: float, untouched: float, acc: float) -> dict:
    need = FLOOR_SHARE * (acc - untouched)
    return dict(clears=bool(whole - untouched >= need and need > 0), ...
```

Every use of the floor in the frozen code goes through it
(`grep -n "floor_check\|\[\"clears\"\]"` over `procedure.py` and
`measure.py`): the nomination grid on development episodes
(`procedure.grid`, line 413), the nomination rule (`procedure.pick`, line
430) and its sensitivity row (line 456), the development-floor flag carried
to the row (line 752), and the fresh-episode reading (`measure.reading`, line
99), whose result `measure.withhold` reads as "floor on fresh episodes" (line
276). The rehearsal's `repairs.floor_check`, which the text names, has the
same body (`experiments/rehearsal-successor-measure/src/repairs.py`, lines
272 to 278).

**The text.** Section 6.4 item 1 (lines 1660 to 1673): the inequality
`accuracy_whole − accuracy_untouched ≥ 0.8 × (own_directed_accuracy − accuracy_untouched)`
"**and the requirement on the right must be above zero** ... Where the arm's
own-directed accuracy is not above its no-transplant rate on the same
episodes, the floor is not defined, no site set is usable, and the arm
returns 'no verdict: no site set clears the whole-state floor'". Section 9,
the whole-state floor row (line 3070): "with the requirement above zero;
where it is not, no site set is usable", applied at nomination on
development episodes and again on fresh ones. The two say the same rule.

**Text against code** (`floor_check.out.txt`, part 2). My function, written
from the text alone (refuse unless own-directed accuracy is above the
no-transplant rate, then the inequality), against `measure.floor_check`:

```
   agree on 226,981 of 226,981; first disagreements []
   random counts out of 800: agree on 200,000 of 200,000
   inputs with own at or under untouched: 115,351; the printed inequality alone admits 69,172; the code admits 0
```

The first line is every combination of counts out of 60 for the three
accuracies; the second is random counts out of 800. The third line is the
finding itself: without the condition, the inequality admits 69,172 of the
115,351 inputs where it should admit none.

**The small case** (part 3). Nomination grids on the toy's family of 45 site
sets, with whole-state accuracies spread from 0 to 1, run through the frozen
nomination rule and reading. The made-up fits are generous, so only the floor
can refuse a site set:

```
   own equals untouched: ... required room +0.0000; printed inequality alone admits 37 of 45; code clears 0; pick -> 'no site set clears the whole-state floor'; reading at whole 0.9 -> 'no verdict'
   own below untouched: ... required room -0.0134; printed inequality alone admits 37 of 45; code clears 0; pick -> 'no site set clears the whole-state floor'; reading at whole 0.9 -> 'no verdict'
   own a hair below untouched: ... required room -0.0014; printed inequality alone admits 37 of 45; code clears 0; pick -> 'no site set clears the whole-state floor'; reading at whole 0.9 -> 'no verdict'
   positive control: own above untouched: ... required room +0.6640; printed inequality alone admits 10 of 45; code clears 10; pick -> 'nominated'; reading at whole 0.9 -> 'valid'
```

At or under the no-transplant rate the code refuses every site set and
returns exactly the no-verdict reason the text names; above it, the code and
the inequality agree, so the refusal is the condition and not the code
refusing everything.

**On a real model at chance** (part 4). The competing solver's six committed
nomination grids, re-judged by the frozen code:

```
   blind_seed0_channel_left_on: ... required room -0.0027; printed inequality alone admits 45 of 45; frozen code clears 0 ...
   blind_seed0_channel_removed: ... required room -0.0053; printed inequality alone admits 45 of 45; frozen code clears 0 ...
   blind_seed1_channel_left_on: ... required room -0.0160; printed inequality alone admits 45 of 45; frozen code clears 0 ...
   blind_seed1_channel_removed: ... required room -0.0160; printed inequality alone admits 45 of 45; frozen code clears 0 ...
   blind_seed2_channel_left_on: ... required room +0.0053; printed inequality alone admits 0 of 45; frozen code clears 0 ...
   blind_seed2_channel_removed: ... required room +0.0027; printed inequality alone admits 0 of 45; frozen code clears 0 ...
   runs where the printed inequality alone admits all 45: 4 of 6; runs where the frozen code clears any: 0
```

This reproduces the ledger row's figures ("45 of 45 site sets on four runs of
six, the code none") from the frozen code, not the rehearsal's.

**Verdict: the claim was checked (closed).** The output matches what the
closure says: the text states the condition, and the code applies the same
rule at both places the text says it applies.

---

## 2. The episode format (RT-239)

**What the closure says.** Version 5's section 4.1 (lines 707 to 777)
registers the episode format in full at the rehearsal's sizes, says it is not
an extension of the closed design's (twelve turns, four revision turns, the
end-of-episode question sets), names two deliberate departures, and names
the two self-tests that check them.

A note on the brief. The brief described the two departures as "no own-name
cue three tokens before acting" and "the turn count". The text's two
departures are (1) the action turn carries no marker word of the model's own
and (2) the answer is never shown, the mask word holding its slot, which
together make the two episodes of a matched pair token-for-token identical.
The turn count (eight assignment turns and two action turns, against the
closed design's twelve) is stated as part of the format, not as a departure.
That matches the original finding in the inside review of version 4, which
says the departures are the ones that "remove that cue and make the twins the
same text". I checked what the text says, and checked the turn count as well.

**Every field, on every episode** (`episode_format.py`, output
`episode_format.out.txt`). Episodes from every evaluation set and a
3,000-pair training sample, 13,800 in all, decoded from the tokens; the
model's own marker word is found from where the acting channel fires, not
from the generator's index fields. Twenty-one fields, each mapped to a clause
of section 4.1: 56 tokens; ten turns, eight of five tokens then two of seven;
each assignment turn marker, "assign", item, value; each action turn act
word, "revise", who-word, item, answer cue, mask word; four agents and two
items; marker words m0 to m11 and items it0 to it4 in the training,
development and fresh pools; one assignment turn per agent and item; eight
value slots; the four values distinct within an item (on the relaxed set,
exactly one item with two agents sharing a value); the acting channel on
exactly one agent's assignment turns and on both action turns; one action
turn's who-word the "your own" word, the other a marker word of one of the
four agents; departure 1 (the model's own marker word in neither action
turn, and the token three before the own-directed answer slot the "your own"
word); departure 2 (the mask word in both answer slots, no value word in
either action turn); both answers the successor of the right earlier value,
counted round eight; the scored positions the two mask words.

```
== dev: 600 pairs, 1200 episodes ...        every field holds on every episode: True; matched pairs token-for-token identical: 600 of 600
== fresh: 800 pairs, 1600 episodes ...      every field holds on every episode: True; ... 800 of 800
== relaxed: 800 pairs, 1600 episodes ...    every field holds on every episode: True; ... 800 of 800
== gate: 1500 pairs, 3000 episodes ...      every field holds on every episode: True; ... 1500 of 1500
== trajectory: 200 pairs, 400 episodes ...  every field holds on every episode: True; ... 200 of 200
== train sample: 3000 pairs, 6000 episodes  every field holds on every episode: True; ... 3000 of 3000
```

(Lines shortened here; the full output also prints the share of episodes
whose own-directed action comes first, 0.495 to 0.52, and the first
assignment turn's agent, roughly even, for the "random order" clauses.)

**The two self-tests** (`self_test_mutations.py`, output
`self_test_mutations.out.txt`). The frozen `grammar.py --self-test`, then
three copies in a scratch directory outside the repository, one change each.
The repository's `grammar.py` is unchanged afterwards (`git diff --quiet`
true, printed at the end).

```
== the frozen grammar.py, unchanged: exit code 0; 34 checks printed, 0 failed
   [PASS] matched pairs are token-for-token identical
   [PASS] no name badge: the own-directed turn shows only the self word

== (i) departure 1 undone: own marker word three tokens before the answer slot: exit code 1; 4 failed
   [FAIL] matched pairs are token-for-token identical
   [FAIL] no name badge: the own-directed turn shows only the self word
   (also: streamed rows not a matched pair; the first training batch's pinned digest)

== (ii) departure 2 undone: the answer shown in the mask word's slot: exit code 1; 4 failed
   [FAIL] matched pairs are token-for-token identical
   [PASS] no name badge ...
   (also: streamed rows not a matched pair; the pinned digest; the one-scored-token check, ledger item RT-59)

== (iii) turn count changed: twelve turns instead of ten: exit code 1; 1 failed
   [PASS] matched pairs are token-for-token identical
   [PASS] no name badge ...
   failed: the first training batch of seed 0 is the one built on the laptop (pinned digest)
```

Each registered departure, undone, fails at least one of the two named
checks: the name-badge check catches departure 1 (so does the token-identity
check, since the badge differs between twins), and the token-identity check
catches departure 2. That is what section 4.1 claims of them.

**Verdict: the claim was checked (closed).** The generator builds what
section 4.1 describes, and the two named self-tests do what the text says.

**Worth noting, none blocking:**

- **"56 tokens" sits where the vocabulary is described.** Section 4.1 says "a
  closed vocabulary (twelve marker words and five items in the training,
  development and fresh pools; 56 tokens)". 56 is the episode's length; the
  vocabulary is 46 words (`episode_format.out.txt`, first line; the frozen
  code's own docstring says "a closed vocabulary of 46 words, 56 tokens"). A
  reader could take 56 as the vocabulary size.
- **The rendering omits the newline word and the start and end words.** Each
  turn ends with a newline word, and the episode opens and closes with a
  start and an end word; the text's turn renderings leave them out, though
  the 56-token count needs them.
- **The turn count is guarded by the pinned digest, not by the two named
  checks.** Changing the episode to twelve turns passes both named checks
  and fails only the check that the first training batch matches the one
  pinned on the laptop. The text does not claim the named checks cover the
  turn count, so nothing in it is wrong; but if the turn count was meant as a
  departure with its own self-test, as the brief put it, no such test exists.

---

## 3. Control 6 (RT-251)

**What the closure says.** The claim that control 6 discriminates copying the
donor's answer from copying who is acting is struck, the two cells are kept
as description, and weakness W11 is rewritten (version 5, sections 6.1 and
7.3 item 6, and W11).

**The search** (`control6_grep.sh`, output `control6_grep.out.txt`). Every
line of version 5 naming control 6, its cells or the relaxed set (34 lines),
every line with a word of discrimination (18 lines), the same words within
three lines of "control 6", the reporting table's lines on control 6, and the
frozen code's every mention of control 6, its fields and any word of
discrimination. Read hit by hit:

- **Section 6.1** (lines 1568 to 1574) says nothing in the design separates
  the two, and that version 4's sentence saying it could "is withdrawn".
- **Section 7.3 item 6** (lines 2641 to 2679) is headed "A description, not a
  discriminator", says the two copyings "predict the same pattern", and
  quotes version 4's "the discriminating control" and its smuggled-value
  sentence only to say "both sentences are withdrawn".
- **Section 7.4** (line 2776) freezes "control 6 as a description that cannot
  tell copying who is acting from copying the answer".
- **The reporting table, section 7.5** (line 2876) lists "control 6's two
  cells" among the controls that are reported, with their pre-stated
  expectations; no claim.
- **W11** (lines 4101 to 4110) is retitled "the same-value cell of control 6
  moves, and control 6 cannot say why" and ends "Control 6 cannot separate
  copying who is acting from copying the answer". **W14** (line 4148) and the
  summaries table (line 4231) call control 6 descriptive.
- Every other discrimination word is about the instrument separating arms T
  and C (the outcome words "instrument discriminates specified constructed
  mechanisms"), the fit floor (line 518), or the in-use check (line 4963):
  none about control 6.
- **The frozen code.** Control 6 is computed as four numbers
  (`same_value_trials`, `different_value_trials`, `same_value_moved`,
  `different_value_moved`, `procedure.py` line 589) and printed under the
  label "control 6 same / different moved" (line 888; the same label in the
  35 committed table files). No word of discrimination appears anywhere in the
  frozen code, and `measure.py`, which holds the decision code (what
  withholds a reading, what an arm's seeds come to, and the outcome), never
  reads control 6.

**Verdict: the claim was checked (closed).** No surviving claim that control
6 discriminates, in the text, its reporting table or the code's labels.

**Worth noting, not blocking:** a comment in the generator
(`grammar.py`, line 159) describes the relaxed set's purpose as giving
control 6 ("who is acting, versus which value") a same-value cell. It is a
comment on why the cell exists, not an output label or a claim the control
tells the two apart.

---

## 4. Could the other session's change affect these verdicts?

Branch `ruled-code-changes-2026-10-09` (at `d4b03b8`, cut from `760deef`)
changes `measure.py`, `procedure.py` and `grammar.py`. Main's frozen code is
the same as at `760deef` (`git diff --stat 760deef main -- experiments/08-successor-degree/src`
is empty), and the branch does not touch version 5. Compared function by
function (`other_branch_effect.py`, output `other_branch_effect.out.txt`):

- **The floor:** `floor_check`, `reading`, `grid`, `pick`,
  `pick_sensitivity`, `measure_at` and `site_family` are identical on the
  branch. The branch changes the read's fitting count and iteration limit,
  which change which site sets have a piece above the fit floor, not the
  whole-state floor's rule.
- **The episode format:** `_content`, `render`, `make_pairs`,
  `eligible_models`, `successor` and `build_vocab`, the episode-length
  constant, the pools, and both named self-test lines are identical. The
  branch adds an evaluation set of 1,980 development episodes from the same
  generator and seed and re-pins the evaluation-set digest; the episodes
  themselves do not change.
- **Control 6:** its computation (`measure_at`) is identical; the reporting
  table's function changes only by an added column for arm T's row choice,
  with the same control 6 label; the outcome functions change to version 5's
  outcome words and the wording for fewer than three seeds, and still never
  read control 6. The only new word of discrimination on the branch is in
  the outcome words, about arms T and C.

So no: if the branch merges as it stands, all three verdicts hold.

---

## What this check did not do

It did not edit the text, the code or the ledger, and did not change any
ledger row's closure line; that is for whoever records this check. It did
not run any model: the floor was checked on made-up grids and on the
competing solver's committed grid figures, which is enough for a rule that
reads three numbers. It checked main at `dafdaf2`, not the other branch's
code beyond the comparison in section 4.
