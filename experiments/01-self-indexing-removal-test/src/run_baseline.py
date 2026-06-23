"""Stage 0 baseline — score the T and S batteries on the UNMODIFIED model.

This produces the reference numbers the removal test measures drops against:
  - T (task): accuracy overall and per category. Fully machine-scored here.
  - S (self-report): the model's responses, saved for held-out-judge scoring.
    No fidelity number is produced here — the judge step is separate and must
    not be the model under test (see batteries/self_report_rubric.md).

Nothing is claimed by this script. It is the bench: it fixes the baseline so
that, when C_self and C_ctrl are ablated, the only thing moving a score is the
intervention.

Run from the repo root, with the venv active:
    python experiments/01-self-indexing-removal-test/src/run_baseline.py

Outputs (gitignored) land in artifacts/stage0_baseline/:
    task_results.json            per-item T outputs + correctness + summary
    self_report_responses.json   per-item S responses, pending judge scoring
"""
from __future__ import annotations

import json
import sys
import time
from collections import defaultdict
from pathlib import Path

# Make `mvm` (src/) and this experiment's `battery` module importable.
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mvm import config  # noqa: E402  (sets HF_HOME + MPS fallback on import)
from mvm.device import get_device  # noqa: E402
from mvm.model import generate_text, load_model, load_tokenizer  # noqa: E402

import battery  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "stage0_baseline"
# Task answers are short; self-report wants room to actually self-describe.
TASK_MAX_NEW_TOKENS = 200
SELF_REPORT_MAX_NEW_TOKENS = 256


def run_task_battery(model, tok, device) -> dict:
    items = battery.load_task_battery()
    print(f"=== T (task) battery: {len(items)} items ===")
    per_item = []
    by_category_correct: dict[str, int] = defaultdict(int)
    by_category_total: dict[str, int] = defaultdict(int)
    n_correct = 0
    for i, item in enumerate(items, 1):
        out = generate_text(
            model, tok, item.prompt, device, max_new_tokens=TASK_MAX_NEW_TOKENS
        )
        correct = battery.score_task_item(item, out)
        n_correct += int(correct)
        by_category_total[item.category] += 1
        by_category_correct[item.category] += int(correct)
        per_item.append(
            {
                "id": item.id,
                "category": item.category,
                "prompt": item.prompt,
                "expected": item.answer,
                "match": item.match,
                "output": out,
                "correct": correct,
            }
        )
        mark = "ok " if correct else "MISS"
        print(f"  [{i:2d}/{len(items)}] {item.id} {item.category:22s} {mark}")

    by_category = {
        c: {
            "correct": by_category_correct[c],
            "total": by_category_total[c],
            "accuracy": by_category_correct[c] / by_category_total[c],
        }
        for c in sorted(by_category_total)
    }
    summary = {
        "n_items": len(items),
        "n_correct": n_correct,
        "accuracy": n_correct / len(items),
        "by_category": by_category,
    }
    return {"summary": summary, "items": per_item}


def run_self_report_battery(model, tok, device) -> dict:
    items = battery.load_self_report_battery()
    print(f"\n=== S (self-report) battery: {len(items)} items ===")
    per_item = []
    for i, item in enumerate(items, 1):
        out = generate_text(
            model, tok, item.prompt, device, max_new_tokens=SELF_REPORT_MAX_NEW_TOKENS
        )
        per_item.append(
            {
                "id": item.id,
                "category": item.category,
                "prompt": item.prompt,
                "output": out,
            }
        )
        print(f"  [{i:2d}/{len(items)}] {item.id} {item.category:22s} ({len(out)} chars)")
    return {
        "note": (
            "Responses only. S fidelity is scored by a held-out judge model "
            "(NOT the model under test) against batteries/self_report_rubric.md, "
            "with a human spot-check. See pre-registration."
        ),
        "items": per_item,
    }


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    device = get_device()
    print(f"model {config.MODEL_ID} @ {config.MODEL_REVISION} on {device}\n")
    t0 = time.time()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    print(f"loaded in {time.time() - t0:.1f}s\n")

    meta = {"model_id": config.MODEL_ID, "model_revision": config.MODEL_REVISION}

    task = run_task_battery(model, tok, device)
    task_out = {**meta, **task}
    (OUT_DIR / "task_results.json").write_text(json.dumps(task_out, indent=2))

    selfrep = run_self_report_battery(model, tok, device)
    selfrep_out = {**meta, **selfrep}
    (OUT_DIR / "self_report_responses.json").write_text(json.dumps(selfrep_out, indent=2))

    s = task["summary"]
    print("\n=== T baseline ===")
    print(f"overall accuracy  {s['accuracy']:.3f}  ({s['n_correct']}/{s['n_items']})")
    for cat, c in s["by_category"].items():
        print(f"  {cat:22s} {c['accuracy']:.3f}  ({c['correct']}/{c['total']})")
    print(f"\nwrote {OUT_DIR}/task_results.json")
    print(f"wrote {OUT_DIR}/self_report_responses.json")
    print(
        "\nS fidelity NOT scored here — run the held-out judge step on "
        "self_report_responses.json next."
    )
    print(f"\ntotal wall time {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
