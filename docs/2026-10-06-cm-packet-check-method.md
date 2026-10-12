# Method: checking the ruling packet on arms C and M (pull request 109)

*Written 2026-10-06 (Pacific) by a Claude Code session that did not write the
packet, in its own worktree on branch `check-cm-packet`, cut from the packet's
branch. Committed before the findings. Honest about order: this session had
already opened the packet and its sources to see what there was to check
before writing this; no finding is written yet. $0: nothing rented, trained
or spent, and no project code is changed.*

## What is being checked

The proposed ruling packet `docs/rulings/2026-10-06-cm-flat-ownership-PROPOSAL.md`
(pull request 109, branch `ruling-packet-cm-flat`). It asks John to rule on
arms C and M (the two built models whose "which agent am I" answer went flat
in the 10-million-parameter development runs) and on four fixes to the
spending alarm. John is to rule from it tonight, so the check puts accuracy
first.

## The sources it is checked against

1. **The check of the development runs** (pull request 106, branch
   `check-dev-10m`): its report
   `experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-development-runs-check-claude-code.md`,
   sections 3 and 6 to 8, and its script outputs
   (`ownership_answer_sharpness_output.txt`), plus the laptop procedure's
   output folder `experiments/08-successor-degree/out-dev-10m-check/`.
2. **The model and training code the runs used** (on the same branch):
   `experiments/08-successor-degree/src/models.py` and `train_successor.py`,
   for what the sharpness is and how weight decay touches it.
3. **The ledger rows for the runs** (pull request 98, merged; commit
   `d7581d9`, the compute ledger), for each machine's lifetime and cost and
   for what is left on the development spending line.
4. **Proposal version 4** (`docs/successor-experiment-proposal-2026-10-03-v4.md`
   on `main`): section 5.2 (arm C and the 2026-09-20 fallback ruling),
   section 11 step 5b, sections 12.5 and 12.7 (the alarm), and weakness W3.
5. **The record of John's 2026-10-06 rulings** (pull request 103, branch
   `rulings-2026-10-06-gate-a-v4`), pages 10 and 12, and the page 12 question
   in the addendum it records.
6. **The decoy test** (pull request 108), only for what the packet says of it.
7. **The kill dates** in `data/project.toml` and `data/roadmap.toml`.

## The five tests, and what counts as passing

1. **Every factual claim and number is supported.** For each figure in the
   packet, find it in a source above, or recompute it from one. A figure
   passes if it matches the source to the packet's rounding. A claim passes
   if a source says it, or it follows directly from one. Anything else is
   listed as an error, with the right figure and where it comes from.
   Specifically: the sharpness values; 41 and 45 of 180 against 144; the
   ratio 0.40 against 0.99; $1.46 against $1.47; 29 minutes; about $0.81 for
   a rerun (recomputed as arm C's plus arm M's machine cost from the ledger);
   $8.53 left; about $194 to $206 for the fallback; the 2026-09-20 ruling;
   the 2026-10-18 deadline; "section 12.5 registers hourly"; "section 12.7
   says a check that cannot run is a trip"; the $2.50 deadline lines; and how
   the runs are described (steps or parameters).
2. **The reasoning holds**, especially that weight decay alone cannot drive
   the sharpness below zero, so option 2 probably does nothing. Tested two
   ways: (a) is the sign argument sound for the optimiser the code uses
   (AdamW, decoupled decay); (b) how far would decay alone move the
   sharpness over this run's actual schedule? (b) is a few lines of
   arithmetic on the recorded recipe (peak learning rate 0.002, decay 0.01,
   one-cycle schedule with a tenth warm-up, 108,919 steps), kept as a script
   beside the findings. No model is loaded or trained.
3. **The options are fairly stated.** Each option's cost, change and risk is
   compared with the source's own list (pull request 106, section 8 item 7,
   options (a) to (d)). Fails if an option is stated weaker than its source,
   if the recommended option's costs (including time before the deadline)
   are left out while the others' are given, or if a reasonable option the
   sources point to is missing.
4. **The page 12 (continue or stop) framing is fair, and nothing is presented
   as already ruled.** Compared word for word with the page 12 ruling and the
   page 10 ruling it depends on.
5. **Plain language** (the workspace rule of 2026-08-30): every pull request,
   section and weakness number carries a plain label; terms of art are either
   replaced or explained at first use. Each bare identifier or unexplained
   term is listed.

## What this check does not do

It does not re-run any model, the laptop procedure or the alarm; every
measured figure is taken from pull request 106 and the ledger, and only
re-derived where the arithmetic is simple. It does not recommend an option
of its own beyond saying whether the packet's recommendation survives the
errors found. It does not change the packet: corrections are listed for the
packet's author or John to apply.

## Output

Findings in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-06-cm-packet-check-claude-code.md`,
with the decay arithmetic in
`experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-06-cm-packet-check-scripts/`.
One pull request, titled with a one-line verdict, not merged.
