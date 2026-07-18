# Held-out test set — authoring spec (committed before any item is written)

*Required by `pre-registration.md` ("θ/δ are set during Stage 0 piloting on a
held-out pilot set and committed before the test set is run") and
`thresholds.md` §piloting ("The pilot set is disjoint from the test set").
The 92-item post-cull batteries are hereby designated the PILOT set — they
were consumed by the prelock dose-response, the SAE pilot, the RT-06 ladder,
and the k=16 strength selection. The registered removal test runs on the
held-out TEST set specified here, which no pilot condition ever touches.*

## Composition (mirrors the pilot batteries exactly)

- **T_self_irrelevant:** 32 items, 8 per category (multi_step, needle_synthesis,
  coreference, instruction_following).
- **T_self_relevant:** 30 items, 10 per category (own-output binding,
  role binding, conversational-role tracking).
- **T_syntax:** 30 items, 10 per category (turn counting, boundary
  identification, positional tracking).
- **S (rubric v2):** 30 items, 10 per category (first_person_activity,
  self_monitoring, self_vs_other), forced-third-person items included per
  RT-03, disjoint from all T items per the leakage rule.

## Authoring rules (binding)

1. **Shape-cloning only:** every item is a fresh-content instantiation of a
   shape that PASSED baseline in the pilot batteries (the
   `battery-growth-notes.md` discipline). No new shapes, no shapes from
   culled items (incl. the sx24–26 meta-count refusal shape and the sr04/sr32
   failure classes).
2. **Content disjointness:** no surface text, scenario, entity names, or
   answer values reused from any pilot item. Structural templates may repeat;
   content may not.
3. **Baseline verification before use:** the test set is scored once on the
   unmodified substrate. The pre-committed cull rule applies verbatim
   (baseline-failing items dropped and replaced from passing shapes,
   re-verified; category floors maintained). Target: every retained item
   passes baseline, so any flip under ablation is a registered drop.
4. **One-way traffic:** once the test set is baseline-verified, no pilot,
   calibration, or instrument-development run touches it. It is scored
   exactly twice more: once per registered condition in the removal test.
5. **No peeking at the test set's ablation behaviour** before the registered
   run — the baseline verification pass reports accuracy only.

## What runs on it (fixed by the lock, `8b1fcbe`)

Baseline + C_self-index-residual k=16 mean + directional cross-check +
C_self-narrative (independent, RT-04) + C_ctrl-expert matched strength —
each through the Pass 5 dual OOD gate; S judged under rubric v2 (held-out
judge, standard human spot-check); decision rule and locked thresholds
applied verbatim from `thresholds.md`.
