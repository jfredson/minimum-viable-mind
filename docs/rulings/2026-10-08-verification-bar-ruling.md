# Ruling: the bar for "the repaired route holds" stays at 0.5 (2026-10-08)

*Recorded 2026-10-08 (Pacific) by a Claude Code session that wrote neither
version 5 of the registration text nor the sharpness-fix findings the bar
comes from. John ruled; the session recorded. Authorship **mixed**: the
session that drafted version 5 recommended this option (its section 21,
open item 1, option (a), confidence moderate), and John chose it in his own
words. Written under the workspace plain-language rule.*

## John's words

> "Rule the verification bar now, keep it at 0.5"

Said on 2026-10-08, after the session's assessment that morning recommended
ruling this item first, before the fifteen branches merge and before the
three reruns launch.

## What is ruled

The verification of the repair, as section 5.6 of version 5 describes it
(`docs/successor-experiment-proposal-2026-10-07-v5.md`, branch
`successor-v5-registration-draft`), keeps the bars the method note stated
before any figure was seen
(`docs/2026-10-06-sharpness-fix-inuse-check-method.md`, section 2, branch
`fix-sharpness-inuse-check` at `644238e`). "The repaired route holds" means,
in figures:

- **Part A, the answer is decisive.** Over the same 3,000 gate episodes as
  the learning gate, the mean weight the built-in answer puts on the agent
  the model actually is, at the own-directed action, is at least **0.9**.
- **Part B, the network uses the answer.** Each gate episode is run again
  with the built-in answer pointed at a different agent; on the own-directed
  actions that go through the built route and that the model got right with
  the true answer, the share it no longer gets right (the route use) is at
  least **0.5 on every built route**: arm T's slot, arm C's stirred-in route,
  and both of arm M's. A route with nothing right to lose "could not be
  evaluated" and a missing field is "not run"; both count against.

A seed counts only when both parts pass and the seed passes its learning
gate. The repaired route holds when arm C and arm M each pass. The three
built arms are retrained once at 10 million parameters, seed 0, with the
sharpness fixed at 4.0 (about $1.14 from the first release's development
line), and each is run through the registered procedure with the in-use
check. These bars are now **ruled**, and the sentence in section 5.6 that
says they "are not ruled" is to be replaced by a pointer to this file when
version 5 is next edited.

## What follows if the bar is not met

The stop condition John added to decision 3 on 2026-10-07 ("Yes, add the
stop condition to decision 3") fires: experiment C stops before the free-arm
run at registered size, the rest of the first release is not spent, and C is
written up as instrument research with the finding that **the built arms as
designed are not references**: a route that carries a quarter of the right
answers is not a known ownership route, and reading it as "entangled by
construction" would be the inflation the project's standing rules forbid.

The record predicts this is the likelier outcome. On the toy models after
the fix, arm C's route use is 0.244 to 0.285 across three seeds and arm M's
stirred-in route is 0.090 to 0.106, all well under 0.5, while arm T passes at
1.000 on the toy and 0.924 at 10 million parameters
(`docs/2026-10-06-sharpness-fix-inuse-check-findings.md`, sections 4 and 5,
same branch). The bar is kept with that in view: the project's own prior
already says the degree experiment most likely ends early, and the
December-result roadmap's registered terms count that ending as a result.

## What is declined

The findings' other options are not taken: (b) a small bar against the free
model's 0.000, such as 0.1, which would detect only a route switched off;
(c) part A alone, which the fixed sharpness passes by construction and so
tests nothing; (d) redesigning arm C and arm M's stirred-in half so the built
route is the only route. Option (d) stays on the record as the named route
to a real reference if the stop fires; it needs its own toy work and its own
ruling and is not authorised here.

## What this does not rule

Open item 6 of version 5 (whether arm T's rerun failing also stops C) and
the other open items stand. Nothing launches on this ruling: the reruns wait
on the registration commit, which waits on version 5's check and the merge
of the branches it cites.

## Where it lands

- This file, on the main line, so that version 5 can cite it at a main-line
  commit.
- Version 5, section 5.6 and section 21 item 1: the checking session writes
  the pointer in; the figures do not change.
- `STATUS.md` (the 2026-10-08 entry's addendum) and `data/project.toml`
  (the next step for this decision closed).
- The TimeAssembler worklog, as a decision entry with authorship mixed, and
  the roadmap task for this decision closed.
