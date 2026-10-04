# Ruling 2026-10-03 (night): the two questions raised by the check of proposal version 4

*Recorded 2026-10-03 (Pacific), night, by the Claude Code coordination
session. **Authorship: mixed.** The check of version 4 (pull request 86,
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-03-proposal-v4-check-claude-code.md`,
section 6) proposed each answer. The coordination session put both questions
to John once, with those suggestions, and he ruled in the words **"Agreed on
both suggestions"**. No compute was launched and no money was spent.*

*Written under the workspace plain-language rule.*

## What was ruled

1. **The other-agent control's code is changed to draw twenty random pieces,
   and its code test is run again on the changed code, before the
   registration review.** This is how the second record of the seven-question
   ruling has it (`docs/rulings/2026-10-03-version-4-questions-rulings.md`,
   ruling 5). The first record had it done with the registered measurement
   (`docs/rulings/2026-10-03-proposal-v4-seven-questions-rulings.md`). Doing
   it before the review satisfies both records. The reconciliation
   (`docs/rulings/2026-10-03-seven-questions-reconciliation.md`) did not list
   this difference. Version 4 follows the first record at lines 1834 to 1836
   and 3866 to 3868. The registration text follows this ruling.

2. **The rule that separates the two built models stays as ruled.** That rule
   is the lowest reading among the entangled model's seeds that return a
   reading, minus the highest among the separable model's, at 0.5 or more,
   with seeds not paired by number. It forgives a seed that returns no
   verdict. It does not forgive a seed that returns an odd reading. The
   registration says so in one sentence. The less strict alternative, which
   would take the middle reading of each model's three seeds, was not taken.

## For John to know, not ruled here

The check found six places where the two records of the seven-question ruling
differ without the reconciliation listing them (section 3.3 of the check). One
of them is question 1 above. On the other five, the second record simply says
more and nothing conflicts. Under the reconciliation's own rule that both
records stand, they stand as written in the second record, and the
registration text carries them.

## What this changes

- The registration text: both rulings above, the five fuller points from the
  second record, and the thirty wording fixes in section 4 of the check.
- Before the registration review: the other-agent control's code with twenty
  random pieces, and its code test re-run. The competing-solver session
  (branch `w2b-job1-competing-solver-run`) already has this change in its
  plan. Its check confirms the change was made.
- Nothing edits version 4, an earlier ruling file, STATUS.md or
  `data/project.toml` here.
