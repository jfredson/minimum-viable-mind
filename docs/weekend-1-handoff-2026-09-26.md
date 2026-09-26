# Weekend 1 handoff, Saturday 2026-09-26 morning

*Written 2026-09-26 06:45 Pacific by the Cowork planning session that ran
Friday 2026-09-25, for the Cowork session that resumes Saturday. Plain
language; every pointer is a path or a pull request number. Nothing here is a
ruling. Read this, then the top of `STATUS.md`, then
`docs/weekend-roadmap-2026-09-24.md` section 7. The working rules of Friday
are at the end.*

## Where Weekend 1 stands against its four outcomes

1. **A3 closed: done.** Amendment A3 is registered closed as *not testable* by
   the registration commit `7b15c88` (pull request 49), after two outside
   reviews (Gemini 3.1 Pro, ChatGPT 6 Astra Medium), John's dispositions
   (`docs/rulings/2026-09-25-a3-closure-tier2-dispositions.md`), version 5 of
   the closure text, a tier 1 check and re-check, and John's rulings on the
   check (`docs/rulings/2026-09-25-a3-closure-v5-tier1-rulings.md`). Ledger
   rows RT-204 to RT-211 and the $450 ceiling line are on main.
2. **Every blocking decision ruled: done.** The nine pages are ruled in
   `docs/rulings/2026-09-26-weekend-1-queue.md` (main), checked on pull
   request 41. The five follow-on decisions from the rehearsal repairs are in
   `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md` on **pull request
   53, open**, and need four sentences annotated (see item 3 below).
3. **Version 2 through tier 1: not done, and the tier 1 review is fatal.**
   Version 2 (`docs/successor-experiment-proposal-2026-09-26-v2.md`, pull
   request 54, open) was reviewed at Gate C tier 1 on pull request 56 (open):
   one fatal, four serious, RT-212 to RT-229. This is Saturday's first ruling.
4. **The rented slice's figure in the release arithmetic: done.** Second
   attempt (pull request 51, merged) measured seconds per step on the rented
   card: arm T 13.08 ms, arm C 13.52 ms, arm F 12.53 ms; the constructed arms
   cost 1.044 and 1.080 times the free arm, not 1.55. Second release recomputed
   to $129.90; both releases $161.90. Total rented spend Friday: $0.4974 (first
   attempt, stopped at a launcher hang, since billed at $0.5162) plus $0.0525.
   Checked on pull request 55 (merged).

## The science as of Saturday morning (all MEASURED in the files named)

- At toy scale, the ruler reads its separable anchor (arm T) at 0.0000 exactly
  and reproducibly. On the other three arms it does not read reliably:
  - **RT-212 (fatal, pull request 56):** the fitted straight-line read of
    "which marker word is mine" on the free arm never exceeds 0.172 at any
    layer or seed, against 0.072 by chance (1.0 on arms T and M). So the free
    arm's toy reading of "fully entangled" comes from a subspace carrying
    nothing, and nothing in the design catches it. The repairs check (pull
    request 58) found the same independently. The 2026-09-23 label ruling was
    made on arm T alone.
  - **RT-213 (serious):** arm C, the entangled anchor, fails the learn-both
    gate on 0 of 3 toy seeds; the staggered launch tests only arm F before the
    second release, so an R3 from arm C would cost the whole successor.
  - **RT-214:** control 3 fails on arm M seed 1, so arm M's "pass on all three
    seeds" is not met under the proposal's own rules.
  - **RT-215:** the site-set rule being registered was never run (24 of its 60
    sets never ran); $0 to fix on the laptop; fatal at Gate A if not.
  - **RT-216:** weakness W7 is false; 6 of 9 nominations sit at layer 0, where
    the acting channel is injected.
- **The named-other condition does not learn at toy scale by any route tried:**
  curriculum 0 of 3, loss re-weighting 0 of 3, unchanged recipe 1 of 3 (pull
  request 52), and the grammar change (acting channel off on the named-other
  turn) 0 of 3 at 774/730/759 of 3,000 against 790 (pull request 57, open,
  its check not yet run). Under John's ruling of 2026-09-25 item 1, fallback
  (d) registers. The grammar session's diagnosis: the model tells the turns
  apart and fails at matching the named marker to that agent's value.
- **Arm M works as built:** 0.48 to 0.53 (re-run 0.52 to 0.53), a mixture by
  item, about three fifths entangled. John ruled it folded in.
- **The repairs check (pull request 58, open, 2026-09-26):** every verdict
  reproduces; decimals on arms C, F and M do not, as the 2026-09-23 ruling
  expects; three procedure facts are properties of one run (which arm hit the
  degenerate set; 6 vs 7 vs 8 of 12; control 2 on 2 vs 3 free-arm seeds).
  Three errors in the findings (7 of 12 is 8; arm M's rider "no verdict" is a
  floor miss with about 0.41 moved; two seeds transposed). Four sentences of
  the repairs ruling need annotating: $161.90 cited a file then unmerged (now
  on main via pull request 51); "about $434" is the top of $422 to $434;
  "7 of 12" and "within 0.04" (0.042); item 3's site counts under its own
  widened exclusion are 240 and 1,456, not 296 and 1,816.

## Open pull requests and what each waits on

| PR | what | waits on |
|---|---|---|
| 52 | rehearsal repairs findings | its check is 58; merge 52 then 58 |
| 53 | repairs rulings (five decisions) | four annotations, then merge |
| 54 | successor proposal version 2 | John's Gate C rulings; then version 3 |
| 56 | Gate C tier 1 review of version 2 | merge as filed (it is a review) |
| 57 | grammar attempt findings | a checker session, then merge |
| 58 | check of 52 | merge after 52 |

## Saturday, in order

1. Merge 52, 58, 56 (reviews and findings; nothing in them is ruled).
2. Annotate the four sentences in `docs/rulings/2026-09-25-rehearsal-repairs-rulings.md`
   on pull request 53 (a small writer session), merge 53.
3. Checker for pull request 57 (grammar attempt), then merge.
4. **John rules RT-212 to RT-229** with the review open
   (`experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-27-successor-v2-gate-c-claude-worktree.md`
   on pull request 56). The design question under RT-212: how the registration
   certifies that the nomination found something before a reading counts
   (a pre-stated floor on the fitted read's accuracy against its
   label-permutation null is the obvious candidate), and what the toy record
   is allowed to say about arms C and F given that.
5. Version 3 of the proposal from those rulings (Fable), with RT-215's site
   rule actually run ($0), then Gate C tier 1 on version 3.
6. Sunday: Gate A tier 1 on the registration text if version 3's Gate C is
   clean; the Sunday-night handoff (STATUS.md, `data/project.toml`, the
   roadmap's section 7, the TimeAssembler Weekend 1 and 2 steps, the tasks
   the rulings closed: `6aea06f0`, `588ac12c`, and the RT-198 label collision
   to rule).

## Weekend 2 items already identified

Handshake option (a) (the watchdog waits for the machine's acknowledgement);
the four deadline-script gaps and its misleading ledger line after a normal
finish; annotate both attempts' ledger rows with settled billing ($0.5162 and
$0.0525); rehearsal item R-11's 500-step timing rides on the first
registered-size run; reconcile RT-172 to RT-203.

## Working rules learned Friday (in addition to those in the roadmap)

- Every fresh session prompt opens with `Name this session "<name>".`; Claude
  Agents picks that up as the row name. Sessions cannot rename themselves.
- Writer's pull request first, then its check, when the check was cut from
  main; the reverse when the check was based on the writer's branch, and a
  squash-merge of a check that carried the writer's commits will conflict.
- Never hand John a prompt with a placeholder; wait for the hash and fill it.
- The dispositions session and the plan-check session were started before
  their inputs existed; check the input file is on disk before launching.
- Rented runs: stop a launcher by process number, never its process group;
  confirm the vendor's machine list is empty by hand afterwards; never-sleep
  override on (`sudo pmset -a disablesleep 1`) before a go and off after.
