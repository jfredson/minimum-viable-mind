# Stage 0 setup — running the bench on the M4 MacBook Air

Goal: get the smoke test (`scripts/00_setup_check.py`) to print **"OK — bench is working."** That confirms the model, device, and tokenizer all work before we build any experiment logic.

Estimated disk after this: ~10 GB (core env + Gemma-2-2B weights). The heavier interpretability deps and SAEs come later and add a few GB more. Everything downloads into `.hf-cache/` and `.venv/` inside the repo, both gitignored, so cleanup is `rm -rf .hf-cache .venv`.

## 1. Python

Use Python 3.11 or 3.12 (3.13 support across the ML stack is still uneven). If you don't have it:

```
brew install python@3.12
```

## 2. Virtual environment + core deps

From the repo root (`~/Documents/Code/minimum-viable-mind`):

```
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r src/requirements.txt
```

## 3. Get access to Gemma (one-time, it's a gated model)

1. Sign in at https://huggingface.co and open https://huggingface.co/google/gemma-2-2b-it — click to accept Google's license. Access is usually granted immediately.
2. Create a read token at https://huggingface.co/settings/tokens.
3. Authenticate locally:

```
pip install -U "huggingface_hub[cli]"
huggingface-cli login    # paste the token
```

## 4. Run the smoke test

```
python src/scripts/00_setup_check.py
```

First run downloads ~5 GB (into `.hf-cache/`) and may take a few minutes. Expected output: environment info, `device  mps`, a one-sentence answer about what a melody is, a peak-memory figure, and `OK — bench is working.`

## 5. When that's green

Install the interpretability stack for the next stages:

```
pip install -r src/requirements-interp.txt
```

Then we move to Stage 0's second half — the task batteries (T and S) and baseline scoring — followed by Experiment 1's localization.

## Notes for the 16 GB Air

- The ~5 GB bf16 model plus Python plus macOS will lean on swap. Close memory-hungry apps during runs; expect generation to be unhurried, which is fine for short prompts and small batteries.
- If an MPS op ever errors, `PYTORCH_ENABLE_MPS_FALLBACK=1` is already set in `config.py` so it falls back to CPU rather than crashing.
- Keep ~20 GB free on the SSD; macOS degrades when it can't swap.

## Moving to the 48 GB M4 Pro mini later

Change `MODEL_ID` to `google/gemma-2-9b-it` and `SAE_RELEASE` to the gemma-scope-9b residual release in `src/mvm/config.py`. Nothing else should need to change. Treat the 2B run here as the pilot and the 9B run there as the registered test (see `experiments/01-self-indexing-removal-test/pre-registration.md`).
