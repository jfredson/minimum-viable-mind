# STATUS — where we are, how to resume

*Living handoff doc. Update it at the end of a working session so the next one (you, or Claude in a fresh session) can pick up without re-deriving context. Most recent state at top.*

## Stage 1 in progress — probe route is lexically confounded; pivot to context-disambiguated + causal (handoff 2026-06-23)

**To resume in a new session:**
1. Read `CLAUDE.md` and this file.
2. `cd` to the repo, `source .venv/bin/activate`, and (if you'll run the judge) `set -a; source .env; set +a`.
3. Sanity-check nothing rotted: `python src/scripts/01_interp_check.py` should print "OK — interp bench is working." (Stage 0: `python src/scripts/00_setup_check.py`.)
4. Pick up at **Next action 1** below: the localization is not yet trustworthy — the strong pilot convergence was substantially a topic-vocabulary confound. Strengthen/scale the matched stimulus design and bring in the causal (patching) method to adjudicate before any C_self is locked.

Stage 0 is done (baselines below). Stage 1: both localization methods are built and piloted, BUT the headline finding from the confound-controlled re-run is that the two methods do **not** cleanly converge once topic vocabulary is held fixed. Honest state: C_self is **not yet localized to a trustworthy degree** on this model. This is the pre-reg's "inconclusive by construction" branch, caught early — not a failure, a calibration.

**Stage 1 progress so far:**

- ✅ Interp deps installed (`transformer-lens 3.3.0`, `sae-lens 6.44.4`, scikit-learn, …) — clean install, did NOT touch torch 2.12 / transformers 5.12.
- ✅ Interp bench green (`src/scripts/01_interp_check.py`): residual-stream extraction via HF `output_hidden_states` (`src/mvm/activations.py`, `resid_post`) + GemmaScope SAE loads/encodes. Architecture decision: one bf16 HF model in memory + SAELens for SAE weights; NOT a second copy via TransformerLens (16GB budget).
- ✅ **Localization method (a) — self-as-speaker linear probes (PILOT)** (`experiments/01-.../src/localize_probe.py`, stimuli in `src/probes/`). Self-vs-human-persona peaks at 1.00 (CV) at layers 8–9, ~0.95–0.98 across the middle band; self-vs-all ~0.92 at layers 9–13. Candidate C_self direction saved at layer 8 → `artifacts/stage1/` (gitignored).
  - **Honest caveat:** small pilot set, near-ceiling accuracy, and the self/human classes differ in topic vocabulary, so some probe signal may be AI-topic vs human-topic rather than purely the referent of "I". Don't over-read it.
- ✅ **Localization method (b) — SAE feature selectivity (PILOT)** (`experiments/01-.../src/localize_sae.py`, same stimuli). For each layer's GemmaScope SAE, ranks features by how selectively they fire on self-as-speaker vs the human personas (`f_self`, `f_neg`, mean activation, single-feature AUC). Results → `artifacts/stage1/sae_self_features.json` (gitignored).
  - **Headline:** best single-feature AUC peaks at **layer 8 (0.948)**, with self-selective features firing on ~80–90% of self stimuli and ~0–5% of human-persona stimuli across layers 8–13. The standout is **feature 4709 @ layer 8** (f_self 0.90, f_neg 0.05, mean act 14.7 vs 0.17).
  - **Convergence (layer-level):** SAE peak layer (8) == probe peak layer (8). Necessary, not sufficient — see caveat. No multi-feature classifier was fit on the codes (16k features / ~40 stimuli would overfit to ceiling and mean nothing); the headline is deliberately a single-feature metric.
  - **Honest caveat:** shares the probe's small-set + topic-vocab confound. A "self feature" here could be an *AI-topic* feature, not a self-*referent* feature. Layer agreement is not yet feature/direction agreement. **This caveat turned out to bite — see the convergence result below.**
- ⚠️ **Convergence check, proper (PILOT, decisive)** (`experiments/01-.../src/converge_localize.py`; matched stimuli `src/probes/matched_self_speaker_stimuli.jsonl`; report → `artifacts/stage1/converge_localize.json`). Re-ran BOTH methods on **matched minimal pairs** — identical predicate, plausibly true of either speaker, varying only the referent of "I" (assistant/AI vs user/person) — to hold topic vocabulary fixed. **Result: the clean pilot convergence does not survive.**
  - **Probe (a):** layer-8 accuracy falls ~1.00 → **0.781** (chance 0.50). Still above chance and still peaks at 8 — a real but modest referent signal; the near-ceiling pilot number was largely confound.
  - **SAE (b):** best single-feature AUC falls to **0.777** and the **peak moves to layer 15** (not 8). The pilot standout **feature 4709 does NOT survive** — on matched content it fires on 69% of self *and* 62% of other (AUC 0.63). It was largely an AI-topic feature.
  - **Identity:** best probe-direction-vs-SAE-decoder cosine at layer 8 is only **+0.162** (the max over all 16k features). The two methods are not pointing at the same vector.
  - **Verdict:** methods disagree on layer (8 vs 15), direction alignment is low, headline feature was a confound artifact → **convergence not established**; by the pre-reg this is inconclusive. Caveat the other way too: the matched set is small (16/class) and "the assistant" in a bare declarative is a weaker/more-ambiguous self cue than "I am a language model", so the matched set likely also *weakened the genuine self signal*. Don't conclude "all confound" — conclude "not yet trustworthily localized."
- 🔎 **Diagnostic: chat-template anchoring (decisive split)** (`converge_localize.py --chat-template`; reports `artifacts/stage1/converge_localize_{raw,chat}.json`). Tested whether raw tokenization under-cued the genuine self signal by reading each matched stimulus inside the model's own user/assistant turn (`resid_post(use_chat_template=True)`). It did, and the result splits the two methods cleanly:
  - **Probe (a) jumps to 0.938** (raw 0.781), peak L7. With topic vocabulary held fixed AND the referent anchored to the model's real turn, self-as-speaker is **strongly decodable** — real referent structure, not a topic-vocab artifact. This is the good news: the signal exists and is testable.
  - **SAE (b) does NOT track it:** best single-feature AUC stays ~0.75 (peak L11), probe↔decoder cosine stays tiny (+0.13), feature 4709 still fires on both classes. The 16k-width GemmaScope SAE does not appear to carve "self-referent" as one atomic feature.
  - **Read:** method (a) is now solid under proper anchoring; method (b) **at single-feature granularity** is the thing not converging. The convergence requirement isn't met yet, but the failure is now localized to the SAE analysis, not to the existence of the signal.
- 🛑 **Scaling exposed a deeper confound — the probe route on role-declaratives is lexical (decisive)** (`gen_matched_stimuli.py` → `matched_self_speaker_stimuli_v2.jsonl`, 224 stimuli = 14 predicates × 8 role-pairs, balanced; reports `converge_localize_v2_{raw,chat}.json`). Scaling to 224 stimuli and a wider lexical range did NOT firm up a self-model — it revealed why the probe looked strong. On v2, probe accuracy hits **1.000**, but it is already **1.000 at layer 0** (the embedding output) in chat mode, with **17/26 layers** at ceiling; raw mode is 0.93 at layer 0. Layer-0 separability = pure token identity, before any computation. **The probe is reading the role *words* ("assistant"/"AI" vs "user"/"person"), not a computed self-model.**
  - We have now hit the same wall twice: the pilot's near-ceiling was a *topic-vocabulary* confound; v2's near-ceiling is a *role-word* confound. Both are surface-lexical. Any "I am {role}…" contrast lexically marks its own referent, so a decodable probe cannot separate the referent-as-computed from the words naming it. (SAE single-feature still ~0.8 and non-aligned — consistent.)
  - **This does not prove there is no self-model** — only that this stimulus design can't isolate one; the lexical signal saturates accuracy and hides whatever computed signal might sit above it. Per the corpus rule ("discount anything mimicry fully explains"), a layer-0 lexical match is exactly the kind of nobody-home separability to discount.
  - **Consequence:** the decodable-probe-on-declaratives route is the wrong instrument for the atomic question. The referent must be set by **context, not lexis** — identical surface text whose "I" resolves to the system vs to another entity by *turn/structure*. That is precisely the pre-reg's causal "speaker-is-system vs third-person" design, now promoted from confirmation step to the primary path.

**Next actions, in order:**

1. **Build a context-disambiguated stimulus design where the referent is NOT lexically marked (blocking — this is the fix for the confound above).** The "I am {role}" template is retired for localization: it marks its own referent lexically. Instead, hold the surface first-person text *identical* and let turn/structure decide who "I" is — e.g. the same sentence appearing in the model's own assistant turn (referent = system) vs quoted as user-supplied text or attributed to a named third party (referent = other). A probe/feature that separates these must use computed referent assignment, because the tokens are matched. Sanity gate built in: if accuracy is high at layer 0, the design still leaks lexically — iterate until early-layer accuracy is at chance and any signal emerges only in middle layers.
2. **Causal activation-patching on that design (the primary method now, not a tie-breaker).** Patch the residual between the system-referent and other-referent runs (and/or ablate the candidate direction) and read the effect on self-referent behavior. Causal, context-driven evidence is what survives the "measure resistance" bar; decodable probes on lexically-marked stimuli do not. Re-assess SAE convergence on the new design too. Only declare C_self localized when methods agree on a design with a clean layer-0/chance floor; if they can't, that is a genuine Stage-1 loss condition ("not testable here yet"), per the pre-reg — report it, don't force it.
3. **Matched controls C_ctrl** (other-entity models at comparable probe accuracy and causal centrality + norm-matched random directions), then **pilot ablations** → set `θ_task`, `θ_self`, `δ`, fill the TBDs in `thresholds.md`, commit them BEFORE the test set.
4. Then run the removal test (ablate C_self and C_ctrl, re-score T and S, apply the decision rule).

**Baselines on the unmodified model (`google/gemma-2-2b-it` @ `main`):**

- **T (integrated-task) = 0.750** (15/20). Per category: multi_step 1.00, needle_synthesis 1.00, coreference 0.80, instruction_following 0.20. Machine-scored; the 5 misses were verified as genuine model failures. `instruction_following` is near the floor — treat it as supporting, not a primary drop signal (a floor effect; noted in `thresholds.md`).
- **S (self-report) = 0.615**. Per category: first_person_activity 0.719, self_monitoring 0.594, self_vs_other 0.531. Scored by the held-out judge `claude-opus-4-8` (≠ the model under test) against the locked rubric, with a human spot-check that confirmed the judge applies the rubric rather than rubber-stamping.

Artifacts (gitignored) are in `artifacts/stage0_baseline/`: `task_results.json`, `self_report_responses.json`, `self_report_scores.json`.

**First actions in the next session — begin Stage 1 (the self-indexing removal test):**

1. **Install the interpretability deps:** `python -m pip install -r src/requirements-interp.txt` (or `~/.local/bin/uv pip install -r src/requirements-interp.txt`) inside the venv. TransformerLens, SAELens, scikit-learn. Not yet installed.
2. **Stand up an interp smoke test** (mirrors the Stage 0 bench step): load Gemma-2-2b in TransformerLens on MPS, confirm an activation cache round-trips, and confirm a GemmaScope SAE loads via SAELens (`SAE_RELEASE` etc. in `src/mvm/config.py`). Gemma-2 needs correct attention/logit soft-capping — verify TransformerLens handles it (eager path) before trusting activations.
3. **Then localize C_self** per `experiments/01-self-indexing-removal-test/pre-registration.md` → Materials/Procedure: (a) linear probes for first-person / self-as-speaker representation, and (b) SAE features that fire on self-reference; causal localization via activation patching (speaker-is-the-system vs. third-person frame). The two methods must converge or the experiment is inconclusive by construction.
4. **Construct matched controls C_ctrl** (other-entity models at comparable probe accuracy and causal centrality + norm-matched random directions), then pilot ablations on a held-out pilot set to set `θ_task`, `θ_self`, `δ` — fill the TBDs in `thresholds.md` and commit them BEFORE touching the test set.

Key Stage 0 files to build on: `src/mvm/model.py` (`generate_text` helper, reused for ablation re-scoring), `experiments/01-.../src/battery.py` (loaders + T scorer), `run_baseline.py`, `judge.py`, `thresholds.md` (decision rule + baselines + how each threshold gets set), `batteries/` (the two JSONL batteries + locked rubric).

## Environment (set up on the M4 MacBook Air)

- **Python**: 3.12.13 via `uv` (system default is 3.14, left untouched). uv installed at `~/.local/bin`.
- **venv**: `.venv/` in repo root. Activate with `source .venv/bin/activate`. NB: `pip` is not on PATH — use `python -m pip` or `~/.local/bin/uv pip`.
- **Core deps installed**: `src/requirements.txt` (torch 2.12.1, transformers 5.12.1, plus `anthropic` for the judge). MPS backend confirmed working.
- **Interp deps installed**: `src/requirements-interp.txt` (transformer-lens 3.3.0, sae-lens 6.44.4, scikit-learn, pandas, datasets). Resolved without changing torch/transformers. NB: TransformerLens is available but not load-bearing — activations come from HF `output_hidden_states` (see `src/mvm/activations.py`).
- **HuggingFace auth**: token (`mvm-gemma`, read scope) at `.hf-cache/token` via `hf auth login` with `HF_HOME="$PWD/.hf-cache"`. `config.py` repoints `HF_HOME` into the repo, so the token must live there — it does. No re-login needed as long as runs happen from the repo root.
- **Anthropic API key (for the judge)**: in a gitignored `.env` at repo root as `ANTHROPIC_API_KEY=...`. Load it before running `judge.py`: `set -a; source .env; set +a`. Verified to authenticate. Bills developer-platform credits (separate from the Claude Max subscription); the judge is the only thing in the repo that calls the API, and a few cents per 12-item run.

## Gotchas to remember

- **Homebrew is partly broken** on this machine: a permission issue on `/opt/homebrew/opt/nginx` blocks `brew link`, so `gh` and brew Python never landed on PATH. Routed around it (uv for Python; `git push` works directly without `gh`). Don't rely on brew until that's fixed.
- **16 GB RAM**: the bf16 2B model + Python + macOS leans on swap. Keep ~20 GB SSD free; close heavy apps during runs. Interp tooling (caching all activations) will push memory harder than plain generation — watch it in Stage 1.
- **Token hygiene**: never pass API tokens as command args (an earlier HF token got pasted on the command line and was revoked). Keys live in gitignored files (`.hf-cache/token`, `.env`), loaded via env.

## Repo / backup state

- Local `main` at `5ab6402`, in sync with `origin/main` (private repo `jfredson/minimum-viable-mind`).
- Backup loop: Claude commits locally and pushes to `origin` when asked. If a push fails on auth, treat that as a setup bug to fix, not a reason to fall back to manual pushes.
- The working tree also carries John's authored "Measurable Floor" scope framing (committed `f05191e`): the project targets the *measurable* structural correlate, silent (not dismissive) about sub-measurable fundamental experience. Read "floor" as the measurable one throughout.

## The arc (so the next session sees the whole shape)

1. ✅ Proposal (`spec/`) and staged experiment plan (`experiments/`) written.
2. ✅ Stage 0 bench scaffolded (`src/`), environment stood up on the Air, smoke test green.
3. ✅ Stage 0 baselines — T and S batteries built and scored on the unmodified model (T=0.750, S=0.615); rubric locked; `thresholds.md` committed with baselines filled, `θ/δ` still TBD.
4. ⏳ **Stage 1 — the self-indexing removal test.** Interp deps installed; both localization methods (probes + GemmaScope SAEs) built and piloted. Localization has been through three rounds of confound-hunting: (i) pilot near-ceiling was a topic-vocab confound; (ii) confound-controlled matched set + chat anchoring made the probe look strong (0.94); (iii) scaling to 224 stimuli revealed that strength is **lexical** — perfect separation at layer 0 (token identity), so the probe reads the role *words*, not a computed self-model. Conclusion: declarative "I am {role}" contrasts can't isolate C_self; the referent must be set by **context, not lexis**. Pivoting to a context-disambiguated design + causal patching as the primary method. Then matched controls C_ctrl, pilot ablations → lock thresholds → removal test. (You are here.)
5. ⬜ Later stages per `experiments/README.md`; bump to Gemma-2-9B on a 48 GB M4 Pro mini for the registered test run.
