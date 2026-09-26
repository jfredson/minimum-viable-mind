# The thirty trained toy models behind the 2026-09-25 and 2026-09-26 results

*Committed 2026-09-26 under item 3 of "Refinements 2026-09-26, after the toy
re-run" in `docs/rulings/2026-09-26-successor-v2-gate-c-rulings.md`: these
models cannot be rebuilt from code and seed, and an uncommitted record the
reader cannot open is the form of RT-145.*

**What they are.** The models trained by the rehearsal repairs (pull request 52,
main-line commit `882f252`) with the base recipe: arms T, C, F and M, and the
ownership-blind solver, three seeds each. Every committed repairs output in the
folder above (`gate_base.json`, `nominate_base_*.json`, `measure_base_*.json`,
`summary_base.json`) was computed from them, and so was the toy re-run under
the version 3 rules (`docs/2026-09-26-toy-rerun-v3-rules.md`, pull request 62).

**Where they came from.** Copied unchanged from the repairs session's worktree
(`.claude/worktrees/w1c-rehearsal-repairs/experiments/rehearsal-successor-measure/out-repairs/`),
where they had sat untracked since training on 2026-09-25, because `*.pt` is in
`.gitignore`. They are force-added here.

**How to check them.** From this folder:

    shasum -a 256 -c SHA256SUMS

The twelve arm T, C, F and M models match the `checkpoint_sha256` the re-run
recorded in each `out-v3-rules/nominate_*_seed*.json` and
`measure_*_seed*.json` (pull request 62, commit `5276731`). The re-run did not
read the three blind-solver models, so no earlier file records their
fingerprints; they are byte-identical to the repairs originals.

## Added in a second commit: the other fifteen

The fifteen above were the ones the ruling named. Fifteen more trained toy
models sat untracked for the same reason and are committed the same way, with
their fingerprints appended to the same `SHA256SUMS`, so the one command above
checks all thirty.

**The six free-arm models from the two training redesigns that failed**, in
this folder: `ckpt_F_curriculum_seed*.pt` (redesign (b), a curriculum) and
`ckpt_F_reweight_seed*.pt` (redesign (a), loss re-weighting), three seeds each,
trained by the rehearsal repairs on 2026-09-25. The committed
`gate_curriculum.json` and `gate_reweight.json` in the folder above were
computed from them (the 0 of 3 seeds under each redesign in the repairs ruling,
item 1). Copied unchanged from the same repairs worktree.

**The nine models from the grammar attempt**, redesign (c), in
`../../out-grammar-c/models/`: arms T, C and F, base recipe, three seeds each,
trained on the evening of 2026-09-25 by the grammar-attempt session (pull
request 57, main-line commit `ff778ea`). Every committed output in
`out-grammar-c/` was computed from them. They keep the same file names as the
repairs models (`ckpt_C_base_seed0.pt` and so on) but are different models,
trained on the changed grammar, which is why they sit in their own folder.
Copied unchanged from that session's worktree
(`.claude/worktrees/w1c-grammar-attempt/experiments/rehearsal-successor-measure/out-grammar-c/`).
`SHA256SUMS` names them by that relative path.

No committed file records fingerprints for any of these fifteen, so the only
check available is that each copy is byte-identical to the original it was
copied from, which it is. The later check of the grammar attempt (pull request
61) re-trained its own models and did not reproduce the seed count, which is
the plainest evidence that these files cannot be rebuilt from code and seed.
