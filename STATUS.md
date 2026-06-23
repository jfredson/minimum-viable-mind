# STATUS — where we are, how to resume

*Living handoff doc. Update it at the end of a working session so the next one (you, or Claude in a fresh session) can pick up without re-deriving context. Most recent state at top.*

## Resume here → next action

**Confirm the Stage 0 smoke test is green.** On the M4 Air, from the repo root:

```
source .venv/bin/activate
python src/scripts/00_setup_check.py
```

Expected: `device mps`, a one-sentence answer about a melody, and `OK — bench is working.` First successful run downloads ~5 GB into `.hf-cache/`.

- If green → start **Stage 0 second half**: build the T (integrated-task) and S (self-report) batteries and score them on the unmodified model. See `experiments/01-self-indexing-removal-test/pre-registration.md` → "Task batteries."
- If it errors → paste the error to resume debugging. Last error seen was a gated-repo 403; access to `google/gemma-2-2b-it` was being granted on HuggingFace when we paused.

## Environment (already set up on the M4 MacBook Air)

- **Python**: 3.12.13 via `uv` (system default is 3.14, left untouched). uv installed at `~/.local/bin`.
- **venv**: `.venv/` in repo root. Activate with `source .venv/bin/activate` (prompt shows `(.venv)`).
- **Core deps installed**: `src/requirements.txt` (torch 2.12.1, transformers 5.12.1, etc.). MPS backend confirmed working.
- **Not yet installed**: `src/requirements-interp.txt` (TransformerLens, SAELens, scikit-learn, …) — install when Stage 0 second half / Experiment 1 begins.
- **HuggingFace auth**: token (`mvm-gemma`, read scope) saved to `.hf-cache/token` via `hf auth login` run with `HF_HOME="$PWD/.hf-cache"`. Because `config.py` repoints `HF_HOME` into the repo, the token must live there — it does. No re-login needed in future sessions as long as runs happen from the repo root.
- **Gemma access**: license/access form on the model page submitted (was completing this at pause). Verify the page shows "granted" if the download still 403s.

## Gotchas to remember

- **Homebrew is partly broken** on this machine: a permission issue on `/opt/homebrew/opt/nginx` blocks `brew link`, so `gh` and brew Python never landed on PATH. We routed around it (uv for Python, manual `git push` for GitHub). Don't rely on brew until that's fixed (`sudo chown -R $(whoami) /opt/homebrew` would, but it's unneeded for now).
- **16 GB RAM**: the bf16 2B model + Python + macOS leans on swap. Keep ~20 GB SSD free; close heavy apps during runs.
- **Token hygiene**: an earlier token got pasted on the command line and was revoked; the current `mvm-gemma` token is the live one. Never pass tokens as command args.

## Repo / backup state

- Local `main` at `370bfba`, in sync with `origin/main` on GitHub (private repo `jfredson/minimum-viable-mind`).
- Backup loop: Claude commits locally; you run `git push`.
- Commits so far: `4ce86e3` founding proposal + scaffold · `92bda5e` experiment plan + Exp 1 pre-registration · `370bfba` Stage 0 bench.

## The arc (so the next session sees the whole shape)

1. ✅ Proposal (`spec/`) and staged experiment plan (`experiments/`) written.
2. ✅ Stage 0 bench scaffolded (`src/`), environment stood up on the Air.
3. ⏳ **Stage 0 smoke test** — confirming (you are here).
4. ⬜ Stage 0 second half — T/S task batteries + baseline scoring.
5. ⬜ Experiment 1 — localize self-locating structure, ablate, run the removal test (interpretability deps + GemmaScope SAEs).
6. ⬜ Later stages per `experiments/README.md`; bump to Gemma-2-9B on a 48 GB M4 Pro mini for the registered test run.
