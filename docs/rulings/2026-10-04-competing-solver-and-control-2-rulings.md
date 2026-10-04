# Ruling 2026-10-04: seven questions from the competing-solver run, the twenty-piece control and their check

*Recorded 2026-10-04 (UTC; the evening of 2026-10-03, Pacific) by the
Claude Code coordination session. **Authorship: mixed.** Each question and
its suggestion come from the findings of pull request 88
(`docs/2026-10-03-competing-solver-run.md`, section 8), pull request 89
(`docs/2026-10-03-control-2-twenty-draws.md`, section 7) and their check,
pull request 90
(`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-competing-solver-and-control-2-check-claude-code.md`,
section 9). The coordination session put all seven to John once, with the
check's version of each suggestion, and he ruled in the words **"Agreed on
all seven"**. No compute was launched and no money was spent.*

*Written under the workspace plain-language rule.*

## What was ruled

1. **Which reading of the solver the registration cites.** The main reading
   has the acting channel removed, as the solver was trained and scored. The
   reading with the channel left on is stated beside it. The registration
   says plainly that the main reading's "no verdict" comes from how the
   twins are paired: their states are identical, so every transplant is a
   null transplant. It is not evidence about the measure. The reading with
   the channel left on is the one that tests the measure.
2. **The registration says what stopped this solver**, in the check's
   sentence: "On the toy, the ordinary competing solver returned no verdict
   because no site set cleared the floor at nomination; behind that, its
   best piece missed the piece rule by 119 or more of 180 and its untouched
   rate missed the no-transplant rule by 0.11 or more, and it would have
   failed the gate on learning had it been gated as the free model is. For
   a model near chance the floor itself is close to zero and is decided by
   one or two episodes."
3. **The no-transplant formula is reported, not generalised.** It withholds
   a reading here, which is the right outcome. But it assumes wrong answers
   spread evenly over the other values, and this solver's do not, so the
   registration does not describe the formula as true of every model
   (version 4, lines 1178 to 1183).
4. **The registered other-agent control is `control2_twenty_draws.control2`.**
   `rerun_controls.control2` is named as the earlier version, kept as the
   record of the re-run. The full-size registered code takes control 2 from
   the new function, so there is one control 2 at registration.
5. **The 95th percentile of the twenty random pieces stays as the summary**,
   as ruled, and all twenty are printed beside it.
6. **The solver run's explanation is corrected before it is quoted.** The
   solver's findings (section 4 and question 2) and the description of pull
   request 88 say the gate on learning stopped the solver. Version 4 does not
   gate competing solvers. The session that writes the registration text
   uses "would fail the gate if it were gated as the free model is". No
   re-run, and no rule change. Pull request 88 was merged as written.
7. **No new run before the registration review.** The registration's
   section 13 gains a two-sentence weakness: the toy's ordinary competing
   solver fails the task, so its "no verdict" shows only that the measure
   returns nothing on a model that has not learned the task. It does not
   show what the measure does on a model that does the task by another
   route. The alternative, training a solver that learns from another cue
   before the review, was not taken.

## Also merged on John's instruction

Pull requests 88 (the competing-solver run), 89 (the other-agent control
against twenty random pieces, NOT A RESULT) and 90 (their check). All three
are on the main line at `ecf3820`.

## What this changes

All seven rulings go into the registration text, together with version 4,
the thirty wording fixes from the check of version 4, the ruling of
2026-10-03 on that check's two questions, and the changes in section 7 of
the check in pull request 90. Nothing here edits version 4, an earlier
ruling file, STATUS.md or `data/project.toml`.
