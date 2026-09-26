# The fifteen trained toy models behind the 2026-09-25 and 2026-09-26 results

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

**Not here.** The six free-arm models from the two training redesigns that
failed (`ckpt_F_curriculum_seed*.pt`, `ckpt_F_reweight_seed*.pt`, behind
`gate_curriculum.json` and `gate_reweight.json`), and the nine models from the
grammar attempt (pull request 57, `out-grammar-c/`). They are still untracked in
their own worktrees.
