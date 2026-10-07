# Method: training leaves out fresh and relaxed pairings outright (2026-10-06)

*Written 2026-10-06 (Pacific) by the Claude Code session that makes the change,
before any code is changed or run. Laptop only; $0. Written under the workspace
plain-language rule.*

## 1. What was ruled, and why

John ruled on 2026-10-06 (TimeAssembler worklog, the decision to guarantee
rather than sample the training exclusion, `9fbca0db`) that training must leave
out every fresh and relaxed episode **by its pairing**, so that the registered
claim "no such pairing occurs in the training stream" holds by construction and
is not merely checked on a sample. He chose option (a): change the frozen
training code, at $0, and test the frozen code again.

The related ruling on the generator's self-test (TimeAssembler worklog, the
decision that the self-test checks the pairing and not only the whole episode,
`f4aa2083`) is being carried out in the A2 decision-procedure work (pull
requests 105 and 107). This change does not repeat that work; it uses the same
meaning of "pairing", so the two agree.

## 2. What "pairing" means here

An episode's **pairing** is its assignment table: the set of eight
(marker word, item word, value word) triples, one for each agent and item,
saying which marker holds which value on which item. It ignores the order of
the turns, which agent the action turns name, which items they ask about, the
order of the two action turns, and the order in which agents and items happen
to be listed inside the generator. This is the same definition the A2 branch's
"stricter control 5" check uses (`table(c)` in its `grammar.py` self-test), and
what version 4 of the proposal, section 7.1, calls an unseen combination of
marker words, items and values.

## 3. What changes

All in `experiments/08-successor-degree/src/grammar.py`:

1. A function `pairing(content)` that returns the table above, built only from
   the markers, items and values.
2. A function `held_out_pairings()` that returns the pairings of every episode
   in the fresh set (800 pairs) and the relaxed set (800 pairs).
3. `TrainingStream` gains a second exclusion list, `excluded_pairings`, which by
   default is `held_out_pairings()`, and one method, `admits(content)`, which is
   the whole exclusion in one place: a content is admitted only if its whole
   content is not in any evaluation set (the old rule, kept for the
   development, gate and trajectory sets) **and** its pairing is not a fresh or
   relaxed pairing (the new rule). `pairs_for_step` yields a content only after
   `admits` passes it; anything else is skipped and counted, as now.
4. The module's opening description, the README's line on the stream, and the
   trainer's one-line description of its data say so.

Nothing else changes: the episodes, the evaluation sets, the models, the
measurement and the trainer's recipe stay as frozen. The four 10-million
development runs used the old exclusion; they stay development evidence only
and are not run again.

## 4. Which self-test asserts it

New checks in `grammar.py --self-test`, which the launcher already runs on the
rented machine before any training step:

- **G1, the list is complete.** The default stream's pairing exclusion list is
  exactly the set of pairings of the 1,600 fresh and relaxed episodes, worked
  out separately inside the test from the evaluation sets.
- **G2, the exclusion function blocks every one, however it is dressed.** For
  every fresh and relaxed episode, `admits` refuses the episode itself and all
  48 ways of re-listing it (every order of the four agents times both orders of
  the two items), each with its turn order, named agent, asked-about items and
  action order changed. That is 1,600 x 49 = 78,400 contents, all refused. This
  tests the exclusion function directly, not a sample of the stream.
- **G3, the stream goes through the function.** A training content from step 7
  of seed 0, planted only in the pairing list (whole-content list empty), is
  skipped exactly once and its pairing does not come out; and the same holds
  when what is planted is the pairing of a re-listed copy of it, which no
  whole-content rule could match.
- **G4, made-up cases, with the results expected now:**

| Case | How it is made | Old whole-content rule | New pairing rule |
|---|---|---|---|
| A | The first fresh pair's content, with the agents listed in reverse, the items listed in reverse (values moved to match, so every triple is unchanged), the turn order reversed, the named agent moved on by one, both asked-about items switched and the action order flipped | **lets it through** (its whole content is in no evaluation set) | **blocks it** (its pairing is the first fresh episode's) |
| B | The same, made from the first relaxed pair | **lets it through** | **blocks it** |
| C | Case A with the values of the first two listed agents swapped on the first listed item, so two triples change | lets it through | **lets it through** (its pairing is no fresh or relaxed pairing) |

Case C is there so that a rule which refused everything could not pass. Case B
cannot arise from the training generator anyway (training episodes never give
two agents the same value on an item, and every relaxed episode does), but it
is blocked all the same.

## 5. What "pass" means

- Every G1 to G4 check prints PASS, with cases A, B and C landing exactly as in
  the table above. A different result on any case is reported as a finding; the
  expected results are not edited after the run.
- The full existing self-test suite of the frozen code
  (`src/run_self_tests.sh`, test T1 of the freeze method) ends with
  "ALL SELF-TESTS PASS". In particular the pinned digest of seed 0's first
  training batch stays as it is. If it does not (only possible if step 1 of
  seed 0 drew a fresh pairing), that is reported and the digest is not quietly
  updated.
- The launcher's dry-run test (T7, `tests/check_launcher.sh`) still passes; it
  creates nothing.

## 6. Also measured, for information only

How many training contents the old stream for seed 0 (which all four
development runs used) gave over its 108,919 steps of 48 pairs that carry a
fresh or relaxed pairing. This needs only the generator, not a model, and
changes nothing about those runs' status. Expected, worked out before running:
about 0.3 such contents in total (5.2 million contents, each with a chance of
about 800 in 14 billion of matching a fresh pairing; relaxed pairings cannot
occur at all), so most likely none, and possibly one.
