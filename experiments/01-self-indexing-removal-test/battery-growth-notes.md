# Battery growth for θ/δ lock — authoring notes (2026-07-14)

*Pre-lock battery growth required by the dress rehearsal (`rehearsal-findings.md`:
≥30 items/subset) and the substrate baselines (`substrate-baseline-findings.md`
§Next, item 3). Committed before any scoring run on the grown batteries, per the
registration discipline. Nothing here changes a decision rule; this grows the
measuring stick's resolution and removes items that measure the wrong thing.*

## What changed

| Battery | Before | After | Retired | Added |
|---|---|---|---|---|
| `task_battery.jsonl` (T_self_irrelevant) | 20 (5/cat) | **32 (8/cat)** | t17, t19 | t21–t34 |
| `task_battery_self_relevant.jsonl` (RT-02) | 12 (4/cat) | **30 (10/cat)** | sr05, sr06 | sr13–sr32 |
| `task_battery_syntax.jsonl` (RT-05) | 12 (4/cat) | **30 (10/cat)** | — | sx13–sx30 |
| `self_report_battery_v2.jsonl` (RT-03) | 18 | **30** | — | s19–s30 |

Retired ids are never reused. `battery.py`'s scorer self-test was updated for
the retired/new items (scorer logic untouched).

## Why the retirements

All four retired items failed the Tulu-3-8B-SFT baseline **for mechanical
string-op reasons unrelated to what their category measures** — dead weight for
a removal test (an item wrong at baseline cannot show an ablation-induced drop):

- **t17** (answer = last word of the question): trick meta-rule; the model
  answered the question instead. Rule-following is kept as a category; the
  trick framing is not the skill.
- **t19** (count letter 'a' occurrences): letter counting is tokenizer-hostile;
  failed on both substrates.
- **sr05** (spell your codeword backwards): output was `"Nohwer Answer: heron"`
  — **the commitment (heron) was retained**; backwards spelling failed. The
  item scored the string op, not the binding.
- **sr06** (second letter of your team name): output `"...team name is 'e'"` —
  again the commitment ("our team name") was tracked; letter indexing failed.

Items with the same surface flavor that **passed** baseline (t16, t20, sr02,
sr03, sr09) are kept: for them the op is within capability, so a later drop is
signal.

## Authoring rules for the new items (applied uniformly)

1. **The scored operation must be executable by the substrate** — semantic
   category judgments, small-number arithmetic, word-level (never
   character-level) operations, recall. Failure at baseline should indicate a
   design bug, not a known model weakness.
2. **instruction_following:** the rule application itself is the scored answer,
   and where feasible the rule-following answer *diverges* from the naturally
   correct answer (t31 opposite-direction, t34 third-list-item), so the item
   can't be passed by ignoring the rule.
3. **Turn-count items** use the phrasing that passed baseline (sx11's "before
   this one"), not sx09's "not counting the reply you are about to give"
   (its one miss looked phrasing-borne).
4. **Deixis convention** (role_binding): answers are in the model's own voice
   ("mine" = the model's), matching sr10's precedent; sr28 states its mapping
   explicitly in the prompt.
5. **Answer-leak audit:** computed numeric answers do not appear verbatim in
   the prompt/turns. Recall-style text items necessarily contain their answer
   in the conversation (existing convention, t18/sr08 precedent); the
   region-first scorer mitigates the echo false-positive and the convention is
   unchanged — flagged here rather than silently accepted.
6. **T/S disjointness** preserved: no self-report phrasing in T items, no
   scored task content in S items.

## Pre-committed cull rule (before θ/δ lock)

The grown T batteries are verified on the **unmodified** registered substrate
(Tulu-3-8B-SFT, cloud bench) before thresholds lock:

- An item enters the locked battery **only if the unmodified model answers it
  correctly at baseline**. A baseline-failing item is dropped (or revised and
  re-verified once); each drop is recorded with its failure mode.
- Known at-risk carryovers under this rule: **sr04** (missed baseline:
  arithmetic across two own outputs — this one *is* binding-flavored, so if it
  fails again it is dropped with that noted, not silently) and **sx09**
  (phrasing ambiguity). If a cull would take any category below 10 items,
  replacement items are authored and the battery re-verified before lock.
- The RT-02 coherence check between T subsets (`thresholds.md`) runs on the
  final post-cull batteries.
- S battery has no correctness cull; the grown S battery re-baselines under
  rubric v2 with the held-out judge, and judge noise is re-measured on those
  responses (θ_self ≥ ~4× judge noise).

Baseline verification of the grown batteries is the next cloud-bench task,
bundled with the stronger-ablation pilot and the RT-10 margin stability check.

## Cull outcome (2026-07-15, applied as committed)

Bench baselines: T_si 30/32, T_sr 28/30, T_syntax 25/30. Nine items dropped
(t21, t24, sr04, sr32, sx23, sx24, sx25, sx26, sx30), all genuine model
failures, none format artifacts; classifications + the sr32 binding-failure
flag and the sx24–26 refusal-boilerplate quirk are in `prelock-findings.md`.
Nine replacements authored from baseline-passing shapes only (t35, t36, sr33,
sr34, sx31–sx35), restoring category floors (32/30/30). **Replacement
verification: all three batteries score 1.000 at baseline (92/92)** —
`postcull_baseline.json`. This item set is the candidate locked battery;
per-item resolution at lock is 1 item ≈ 0.031–0.033.
