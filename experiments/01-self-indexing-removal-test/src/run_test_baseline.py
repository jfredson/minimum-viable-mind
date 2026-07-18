"""Held-out test set — baseline verification (test-set-authoring-spec.md rule 3).

Scores the three held-out T test batteries ONCE on the unmodified substrate,
accuracy only. No ablation, no S generation, no gate probes — the test set's
behaviour under any intervention stays unseen until the registered removal
test (one-way-traffic rule). Output feeds the pre-committed cull rule:
baseline-failing items are replaced from passing shapes and re-verified.

Cloud bench: MVM_MODEL=allenai/Llama-3.1-Tulu-3-8B-SFT MVM_N_LAYERS=32
    python experiments/01-self-indexing-removal-test/src/run_test_baseline.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mvm import config  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import load_model, load_tokenizer  # noqa: E402

import battery  # noqa: E402
from run_t_controls import score_items  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "test_set"
BATTERIES = {
    "T_self_irrelevant": THIS_DIR / "batteries" / "test_task_battery.jsonl",
    "T_self_relevant": THIS_DIR / "batteries" / "test_task_battery_self_relevant.jsonl",
    "T_syntax": THIS_DIR / "batteries" / "test_task_battery_syntax.jsonl",
}


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)

    results = {"model_id": config.MODEL_ID, "purpose": "test-set baseline verification",
               "batteries": {}}
    for name, path in BATTERIES.items():
        items = battery.load_task_battery(path)
        print(f"[{name}] {len(items)} items...", flush=True)
        r = score_items(model, tok, device, items, verbose=False)
        results["batteries"][name] = r
        fails = [it["id"] for it in r["items"] if not it["correct"]]
        print(f"[{name}] accuracy {r['summary']['accuracy']:.3f} "
              f"({len(items)-len(fails)}/{len(items)}); fails: {fails or 'none'}",
              flush=True)
    out = OUT_DIR / "test_baseline.json"
    out.write_text(json.dumps(results, indent=2))
    print(f"saved -> {out}")


if __name__ == "__main__":
    main()
