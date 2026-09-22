# Audit of the high-speed session's work, 2026-09-21

*Filed 2026-09-21 (Pacific) by Cowork at John's request, after a session
running Opus 5 with parallel Claude Code worktrees worked the MVM (Minimum
Viable Mind) repository from roughly 18:54 to 20:19 Pacific. The question put
to me: does the work still make sense, and is it the right work for the
project. Advisory. Nothing here is a gate, a ruling or a registration, and I
changed no record other than adding this file.*

*Read at commit `b75d1a7` on `main`, plus every unmerged `worktree-*` branch.
Written under the workspace plain-language rule: every code name and shorthand
is explained on first use.*

---

## The short version

The **quality** of the session's output is high and its gate discipline held.
It did not authorise money, it labelled mixed authorship honestly, it committed
methods before code, and its own review sessions found real defects and said so.

The **selection** of work is wrong for the stated goal. The goal given to the
session was to reach the next RunPod runs, where RunPod is the rented-GPU
service the registered training runs on. Almost every commit that landed on
`main` tonight belongs to the A3 closure text, which the roadmap's own order-of-
work table puts in the *in parallel* column for steps 1 and 2, not on the
critical path. Everything that actually gates the runs was written, and then
left in agent worktrees that were never merged.

Five findings follow, ordered by what they cost.

---

## 1. The whole critical path to the runs is unmerged. **Blocking.**

Section 4 of `docs/december-result-roadmap-2026-09-20.md` puts the path to the
runs as: draft the successor proposal (step 1), review it and run the
measurement rehearsal (step 2), write and gate the registration text (step 3),
freeze and run development runs (step 4), launch the registered training
(step 5). Every artifact on that path exists and none of it is on `main`.

| Commit | What it is | Branch it is stranded on |
|---|---|---|
| `473f6a3` | Successor experiment proposal, version 1 (Gate C draft) | `worktree-agent-a9d40b713d469a4e5`, and three others |
| `f9cf509` | Its spend section rewritten to the two-release ruling | `worktree-agent-a053ea4a3be483df5` |
| `d8ceba9` | The rehearsal buys a rented slice; the second release is bound to what that measures | `worktree-agent-a94b8938df2edd88b` |
| `3bbfece` | Gate C tier 1 review of the proposal, findings RT-172 to RT-188 | `worktree-agent-a5e89aa434ea3f396` |
| `9a91c06`, `518bf0e` | Measurement-rehearsal method and its denominator addendum, committed before the code as the discipline requires | `worktree-agent-a827aade30edf9e28` |
| `176efad` | Pre-authorised-spending proposal | `worktree-agent-ade280221b267a01c` |
| `7e88682` and three others | Compute-ledger rows for the two follow-up runs, including actual spend | `worktree-followup-runs-ledger` |

The commits chain correctly among themselves, so this is not divergence, it is
simply that nobody opened a pull request for the line of work that matters.
Meanwhile pull requests 11 through 20 all merged A3 closure text, its review
packets and its ruling records.

`d8ceba9` is worth singling out. It answers, in the proposal, the question the
2026-09-21 ruling left explicitly open, whether the rehearsal buys a short
rented slice to measure seconds per step on all three architectures. That open
question is the one thing standing between the second spending release and a
number resting on measurement rather than inference. The answer is written. It
is not in the repository.

## 2. Two fatal findings stand against the successor proposal. **Blocking, and it is a design fix, not an edit.**

The Gate C tier 1 review at `3bbfece` returns seventeen findings, two of them
fatal, both labelled MEASURED, which in this repository means the reviewer ran
something rather than argued.

- **RT-172.** The registered reading divides by an accuracy that is never
  corrected, so the top of the scale is different for every arm, and the
  separation bar cannot travel from the rehearsal's toy models to the registered
  ones. In plain terms: the number the experiment is built to produce is not
  comparable between the three arms it compares, so the rehearsal cannot set a
  bar the real runs are then read against.
- **RT-173.** The discriminating control's first cell is empty by construction,
  and the pre-stated rule for "the pairing is broken" fires on a model that has
  learned the task and passes on one that has not, which is backwards.

These are defects in the experiment the RunPod money would buy. Registering and
launching as the proposal now stands would spend on the order of $175 on a
metric that cannot separate the thing it was designed to separate. The first
kill date, registration committed by 2026-10-18, leaves room to fix them, but
they need a design pass and a second rehearsal, not a wording change.

## 3. A committed ruling cites a file that does not exist. **Record defect.**

`docs/rulings/2026-09-21-review-verification-and-staged-spending.md`, under
"Recorded elsewhere", says items 10 to 16 were written into section 12 of
`docs/successor-experiment-proposal-2026-09-21.md`. That path has never existed
on `main`. A future session, or a reviewer working from committed files as the
protocol requires, will follow that citation and find nothing. This is the same
class of defect the session's own Gate A review caught in the closure text
(RT-147, a cited figure that was not in the ledger it cited).

## 4. The spend record on main is wrong, and it is wrong in the direction that matters. **Record defect, with a live consequence.**

Money was spent on 2026-09-20 that `main` does not record. Commit `7e88682` on
`worktree-followup-runs-ledger`: "Both pods created, both refused by the
instrument, both deleted: $1.904." The fitted read did not reproduce on rented
hardware. The ledger rows carrying that, with John's verbatim go and a
machine-change annotation written before the spend exactly as rule 2 requires,
are unmerged.

The consequence on `main` as it stands:

- The compute ledger stops at the 2026-09-20 checkpoint recovery, running total
  about $225.70 of $400.
- `STATUS.md`, the record of record, says of the two follow-up reads: "both
  local, no money spent". Two pods were created and $1.904 was billed. The reads
  were redone locally after the rented attempt failed, so the first half of that
  sentence is true and the second half is not.
- The 2026-09-21 ruling, item 16, corrects the spend figures "to the compute
  ledger, which is the system of record" and states headroom of $174.30. True
  headroom, once the unmerged rows land, is about **$172.40**.

For a programme whose entire discipline rests on the ledger being the honest
record, a real charge sitting outside it is the finding I would fix first.

## 5. The spending plan that was ruled breaks two bounds it never reconciles. **Needs John.**

The first release is about $44 after ruling 19 folded the permitted re-run into
it. The second is about $131. That is about $175.

- Against the **$130 successor cap** ruled on 2026-09-20 (item 4), the plan is
  about $45 over. No ruling has superseded that cap in words. The proposal cites
  item 4 as its bound in the preamble and then never reconciles against it. This
  is finding RT-176 in the unmerged Gate C review.
- Against **remaining headroom**, the ruling itself flags an overshoot of about
  seventy cents and leaves it open. With the unmerged $1.904 counted, the
  overshoot is about **$2.60**.

John's own standing rule on spend, ruled 2026-09-20, says a plan that costs more
than the cap in force proposes the increase with the number and what it buys,
and never routes around it or shrinks silently. The familiar failure is a step
trimmed to fit a cap. This is the mirror image, a cap allowed to lapse without a
ruling. Either way the rule's remedy is the same: the number reaches him.

---

## What I would do about it

In this order, because each one unblocks the next.

1. **Merge the seven stranded branches**, `worktree-followup-runs-ledger` first
   so the $1.904 is in the ledger before anything cites the ledger again, then
   the successor chain through `d8ceba9`, then the Gate C review, then the
   rehearsal method notes.
2. **Correct the two record defects** that merge exposes: the "no money spent"
   sentence in `STATUS.md`, and the headroom figure of $174.30 wherever it is
   quoted, which is `data/project.toml`, section 6 of the December-result
   roadmap, and item 16 of the 2026-09-21 ruling. Annotate the ruling rather
   than rewriting it, per its own convention.
3. **Rule on RT-172 and RT-173** before any registration text is drafted. This
   is the real gate to the runs, and it is the one item on this list that cannot
   be delegated.
4. **Rule the cap question**: whether item 4's $130 is superseded, and if not,
   whether to raise it to $175 and what the extra $45 buys, or to take the
   weaker two-arm design that fits.
5. **Retarget the session** at step 2 of the chain, the measurement rehearsal
   and the proposal fixes, and stop adding passes to the A3 closure text. That
   text has reached version 4 with three addenda and two verification rounds in
   under two hours, and it does not gate the runs.

## What the session got right, for the record

Worth saying plainly, because the findings above are all failures of routing
rather than of work. The session did not authorise or spend money. Its ruling
file states in its own words what was *not* ruled, including that "Agreed on
all" is a ruling on a plan and not the verbatim go a named run requires. It
recorded mixed authorship rather than presenting recommendations as John's
drafting. It committed methods before the code they describe. Its review
sessions ran in isolated worktrees that did not read `STATUS.md` or the drafting
session's notes, as the protocol requires, and they returned fatal findings
against work the same programme had just produced, which is the protocol
working. Finding 20 of the ruling, where a "MEASURED" key count of 110 did not
reproduce and was recorded as a defect rather than quietly dropped, is the
discipline behaving exactly as designed.

The problem is not that the work is bad. It is that the fast path was run on the
branch that does not gate the runs, and the branch that does was left on the
floor.
