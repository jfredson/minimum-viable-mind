# Ruling 2026-10-12: experiment C stops at its registered stop S4b

*Written 2026-10-12 (Monday, Pacific) by a helper session of the weekend
overseer. Records only: this session ran nothing and spent nothing.
Authorship: **john**. He gave the ruling in his own words; the reading he
accepted was written by a session, and is cited, not restated as his.*

## What was asked

On 2026-10-09, on John's go, the three 10-million reruns of the repaired
built models ran (step 4b of the registered plan): arm T (the separable
built model), arm C (the stirred-in built model) and arm M (the
half-and-half built model), at $1.3032 against the about $1.14 approved.
Their outputs and run record are in pull request 166 (the reruns' outputs
and run record), merged by the overseer on John's word ("merge the ready ones") on 2026-10-12 at 10:03 Pacific.

A session that ran none of it and wrote none of the registration read the
outputs against version 5 of the registration text
(`docs/successor-experiment-proposal-2026-10-07-v5.md`, registered
2026-10-09), and posted its reading as a comment on pull request 166
(https://github.com/jfredson/minimum-viable-mind/pull/166#issuecomment-6089973196).
Route use is the share of right answers about the model's own turn that are
lost when the built-in "which agent am I" answer is swapped; the bar is 0.5.

| Arm | Route use | Against the bar of 0.5 |
|---|---|---|
| T (separable) | 0.986 (2,918 of 2,959) | passes |
| C (stirred-in) | 0.000 (0 of 3,000) | misses |
| M (half-and-half) | 0.024 on its stirred-in items (33 of 1,387); 0.000 on its separable items (0 of 1,190) | misses, on both halves |

All three put 0.999 weight on the true agent (bar 0.9) and passed their
gate on learning, so the miss comes from the route check, not from the
task. In the reader's account the verification fails, and experiment C
stops at its registered stop S4b (the stop for a failed verification of the
built models). The 2026-10-09 evening entry of `STATUS.md` recorded this as
the independent reading, pending John's read, and asked him to say whether
experiment C stops there.

What version 5 says follows, quoted from the registered text:

- Section 5.6: the repaired route "holds" when "arm C and arm M each pass
  the in-use check, both parts, and pass their gate on learning."
- Section 5.6, the stop condition: "If that verification fails, that is, if
  the rerun built models at 10 million parameters do not hold their
  built-in ownership route (the stirred-in model and the half-and-half
  model) or do not do the task, experiment C stops there, before the
  free-arm run at registered size, and the rest of the first release is not
  spent. That ending is reported in the words ruled on 2026-10-08, "the
  built arms as designed are not references; the measure was not reached",
  and is a registered ending of experiment C, not a failure of the year".
- Section 11, stop S4b: "Experiment C stops, before the free-arm run at
  registered size; the rest of the first release is not spent." It is "a
  registered ending of experiment C, reached by its own stop rule", and "the
  redesign of the arms so the built route is the only route is the named
  route to a real reference and needs its own ruling."
- Section 5.6 had said in advance: "With the bar at 0.5 as coded, the
  reruns would very likely fail the verification and experiment C would
  stop at about $1.14."

## John's words

**"accept the stop"**, on 2026-10-12, in reply to the independent reading of
the three reruns.

## What it changes

- Experiment C stops at its registered stop S4b. The verification of the
  repaired built models failed: arm C and arm M do not use their built-in
  route. The ending is reported in the ruled words: **"the built arms as
  designed are not references; the measure was not reached."** It is a
  registered ending of experiment C, reached by its own stop rule, and not
  one of the eight outcome terms, which are unchanged.
- The free-arm run at registered size (step 5a, about $12) does not launch,
  and the rest of the first release is not spent. The second release (about
  $150 to $172) is never asked for. What experiment C spent stands at about
  $1.47 for the development runs and $1.3032 for the reruns.
- The "pending John's read" of the 2026-10-09 evening entry of `STATUS.md`
  is settled. The next step that asked him to read it (N44 in
  `data/project.toml`) and the weekend goal for the reruns' verification
  (W3.3 in `data/roadmap.toml`) are done; the branch goal for the free-arm
  run (W3.4) is not needed.
- Nothing in version 5, in its frozen code, or in any earlier ruling is
  edited. Version 5's sentences above are what governed the stop.

## What it does not decide

- **Whether experiment C continues in a new form.** Rebuilding arms C and M
  so the built route is the only route (option (d) of the verification-bar
  ruling, `docs/rulings/2026-10-08-verification-bar-ruling.md`) is a change
  to what the arms are. It would need its own toy retrain and check, and
  its own ruling. Nothing is started.
- **Arm M's separable half reading 0.000 where the toy models read 1.000.**
  The registration says nothing about what to make of it, and arm T's
  separable slot reads 0.986 in the same reruns. It does not change the
  miss, because arm M's stirred-in half fails on its own. It stays open,
  unexplained.
- The two spends over what was said in advance (the reruns at $1.3032
  against about $1.14; the second review tier of pull request 165 at up to
  about $1.04 against a brief that said to stop before about $1) are not
  ruled on here.
