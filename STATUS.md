# STATUS — where we are, how to resume

*Living handoff doc. Update it at the end of a working session so the next one (you, or Claude in a fresh session) can pick up without re-deriving context. Most recent state at top.*

## Stage 0 complete — starting Stage 1 (handoff 2026-06-23)

Both Stage 0 baselines are measured, committed, and pushed. The bench works end to end: model loads on MPS, the T and S batteries score, the held-out judge runs.

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
- **Not yet installed**: `src/requirements-interp.txt` (TransformerLens, SAELens, scikit-learn) — install at the start of Stage 1.
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
4. ⏳ **Stage 1 — the self-indexing removal test.** Install interp deps, localize C_self (probes + GemmaScope SAEs, two methods that must converge), build matched controls C_ctrl, pilot ablations → lock thresholds → run the removal test. (You are here.)
5. ⬜ Later stages per `experiments/README.md`; bump to Gemma-2-9B on a 48 GB M4 Pro mini for the registered test run.
