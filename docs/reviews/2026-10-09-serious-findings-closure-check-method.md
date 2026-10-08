# Closure check of three serious findings (the floor's missing condition, RT-238; the episode format, RT-239; control 6, RT-251): method, written before the check ran

*2026-10-09. Claude Code, as the checker. Laptop only, $0. This session wrote
none of what it checks: not the registration text (version 5 of the
successor experiment's proposal, `docs/successor-experiment-proposal-2026-10-07-v5.md`),
not the frozen code (`experiments/08-successor-degree/src/`), and not the
ledger rows (`experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`).
It checks the main line at commit `dafdaf2`.*

## Why this check exists

John's ruling 4 of 2026-10-09 (`docs/rulings/2026-10-09-ledger-and-closure-packet-rulings.md`,
on branch `rulings-ledger-packet-2026-10-09`, pull request 144) found that
three serious findings were closed in the ledger only as "the argument was
accepted", while the protocol's closure rule (`docs/outside-review-protocol.md`,
"The closure rule") asks that a serious finding be closed the way a fatal one
is, by a measured check run by a session other than the author's, or else be
carried as a named open item. He ruled that one short check by a fresh
session close all three:

- **the floor's missing condition (RT-238):** the whole-state floor's text
  against the code;
- **the episode format (RT-239):** the two self-tests against the registered
  description of the episode;
- **control 6 (RT-251):** the withdrawn claim that control 6 tells copying the
  donor's answer apart from copying who is acting, absent everywhere in
  version 5.

## What I will do, in order

### 1. The floor's missing condition (RT-238)

The finding: the floor as printed admitted every site set, with a divisor of
zero or below, when a model's own-directed accuracy is at or under its
no-transplant rate; only an unwritten clause of the code refused those. The
fix: version 5's section 6.4 item 1 and section 9 state the code's condition
that the floor's requirement be above zero.

- (a) Print the floor function the frozen code uses (`measure.floor_check`),
  every place in `procedure.py` and `measure.py` that calls it or reads its
  `clears` field, and the rehearsal's `repairs.floor_check` that the text
  names, by command.
- (b) Print the text's two statements (section 6.4 item 1 and the section 9
  row for the whole-state floor) by line number, and write the text's rule as
  my own function, from the text alone: a site set clears if and only if
  own-directed accuracy is above the no-transplant rate, and
  `whole − untouched ≥ 0.8 × (own − untouched)`. Compare it with
  `measure.floor_check` on every combination of counts out of 600 on a grid,
  and on random draws. **Pass:** the two agree on every input.
- (c) The small case. Build nomination grids for the toy's 45-site-set family
  (`procedure.site_family(5)`) in which own-directed accuracy equals the
  no-transplant rate, and one in which it is below it, with whole-state
  accuracies spread so that the printed inequality alone admits most site
  sets. Run them through the frozen code's `procedure.pick` (the nomination
  rule) and `measure.reading` (the fresh-episode reading). **Pass:** the code
  clears no site set in either, `pick` returns "no site set clears the
  whole-state floor", and `reading` returns no verdict. A positive control
  with accuracy above the no-transplant rate must clear some site sets, so
  the refusal is not the code refusing everything.
- (d) The same, on recorded figures from a real model at chance: the
  competing solver's six committed nomination grids
  (`experiments/rehearsal-successor-measure/out-competing-solver-run/nominate_blind_seed*_*.json`),
  each row re-judged by the frozen `measure.floor_check` and the whole grid
  by `procedure.pick`. Expected from the ledger row: the printed inequality
  alone admits all 45 site sets on four runs of six, the code none.

### 2. The episode format (RT-239)

The finding: version 4 registered the episode format as an extension of the
closed design's, which has twelve turns and shows the model its own name
three tokens before it acts, and wrote the two departures nowhere. The fix:
version 5's section 4.1 registers the format in full, with two departures
and two named self-tests.

- (a) Quote section 4.1 by line number and list its claims as numbered,
  checkable fields (agents, items, value slots, vocabulary pools, episode
  length, the eight assignment turns and how each is rendered, the two action
  turns and how each is rendered, the "your own" word, the successor rule,
  distinctness and the relaxed set's one collision, departure 1 and
  departure 2, matched pairs token-for-token identical).
- (b) Generate episodes with the frozen generator (`grammar.eval_pairs` for
  every evaluation set, and `grammar.make_pairs` for training) and check each
  field on every episode with my own decoding of the tokens, not the
  generator's own index fields where avoidable. **Pass:** every field holds
  on every episode, and any mismatch in wording between the text and the
  code is listed.
- (c) Run the generator's self-test (`grammar.py --self-test`) and show the
  two named checks, "matched pairs are token-for-token identical" and "no
  name badge", pass.
- (d) Mutations, each in a scratch copy of `grammar.py` outside the
  repository, never in the code: (i) undo departure 1, so the own-directed
  action turn shows the model's own marker word three tokens before the
  answer slot, as the closed design does; (ii) undo departure 2, so the
  answer is shown in the slot the mask word holds. Run the copy's self-test.
  **Pass:** each mutation makes at least one of the two named checks fail,
  and I say which. The brief named the turn count as the second departure;
  the text names the masked answer as the second departure and states the
  turn count (eight plus two, against the closed design's twelve) as part of
  the format. I will check the turn count as a field in (b), and (iii) try a
  third mutation that adds turns, and report what, if anything, catches it.

### 3. Control 6 (RT-251)

The finding: copying the donor's answer gives the same pattern on control 6
as copying who is acting, so control 6 cannot tell them apart. The fix: the
claim is struck, its two cells kept as description, weakness W11 rewritten.

- (a) Grep version 5 for every mention of control 6, its cells, the relaxed
  set, and words that make a discrimination claim ("discriminat", "tell ...
  apart", "separate", "distinguish", "rule out", "smuggl"), and print each
  hit with its line. Read each hit and say whether it claims control 6
  discriminates.
- (b) The same over the reporting table (section 7.5) and the frozen code's
  output labels: the reporting-table header and row in `procedure.py`, the
  control-6 field names, and whether any decision code (`measure.withhold`,
  `measure.arm_outcome`, `measure.outcome`) reads control 6.
- **Pass:** no surviving sentence or label says control 6 discriminates or
  tells the two apart; withdrawn sentences may be quoted as withdrawn.

## The other session's change

Branch `ruled-code-changes-2026-10-09` changes `measure.py`, `procedure.py`
and `grammar.py`. I check main, and I will say from its diff whether it
touches anything a verdict here rests on: `floor_check` and its callers, the
episode rendering and the two self-tests, and the control 6 fields and
labels.

## Verdict form

For each finding: **the claim was checked (closed)**, or **not closed**, with
what is wrong. Findings worth noting that do not block closure are listed
separately. Scripts and their output go beside this note in
`docs/reviews/2026-10-09-serious-findings-closure-check-scripts/`.
