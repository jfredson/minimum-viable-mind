# PROPOSED annotation beside RT-164 in the red team ledger (not landed)

*Drafted 2026-09-25 (Pacific) by the Claude Code session that wrote version 5
of the Amendment A3 closure text (`docs/a3-closure-text-draft-2026-09-25-v5.md`).
Item 1 of John's ruling of 2026-09-25
(`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`) says a dated
annotation goes beside RT-164's line in the red team ledger saying that "Done in
version 3" was not so, and that the line itself is not edited. This file is that
annotation as a proposal. **It edits nothing.** John lands it, or a session he
names does.*

## Where it goes

In `experiments/06-mvm-0a-constructed-self-index/red_team_ledger.md`, as a new
row directly under the RT-164 row (line 756 at commit `d9f4729`), inside the
same table, whose columns are ID, Finding, Severity, Ruling, and Reason /
closure. The RT-164 row is left exactly as it is. A row keeps the table intact;
a paragraph dropped between two rows would break it.

## The proposed row

```
| — (annotation to RT-164, 2026-09-25) | RT-164's closure note, "Done in version 3", was not so. Neither version 3 nor version 4 of the closure text names hard kill K5 (the registered stop condition "probe-patching convergence fails on all three seeds"); both outside reviewers of version 4 found this independently (Gemini G5, ChatGPT A7), and neither of the two checks of version 4 looked for it | serious | RULED 2026-09-25 by John, item 1 of `docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`: K5 is not reached | K5 tests whether probe and causal patching agree; patching was never built for this design (RT-96), so the test was never run. *Not testable (localization)* rests on §3.2's convergence requirement, and A3 closes under the pre-registration's loss condition with no further A3 seeds. Version 5 of the closure text (`docs/a3-closure-text-draft-2026-09-25-v5.md`) names K5 and says so. The RT-164 row above is not edited. |
```

## What the row rests on

- "Neither version 3 nor version 4 names K5": the proposal's check C1,
  `grep -c "K5"` on both drafts, `0` and `0`
  (`docs/rulings/2026-09-25-a3-closure-tier2-dispositions-PROPOSAL.md`),
  reproduced by the dispositions check
  (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-25-a3-dispositions-check-claude-worktree.md`,
  section 1).
- "Neither of the two checks of version 4 looked for it": check C3 in the same
  two files.
- The two reviewer findings: `reviews/2026-09-21-a3-closure-gemini.md` (G5) and
  `reviews/2026-09-21-a3-closure-chatgpt.md` (A7).
- The ruling's words: item 1 of the ruling file named above.
