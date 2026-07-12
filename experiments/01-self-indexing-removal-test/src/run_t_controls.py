"""Baseline the RT-02 / RT-05 control batteries on the unmodified model.

Two new machine-scorable batteries join the Stage-0 T battery (which is now
explicitly the T_self_irrelevant subset):

  - **T_self_relevant (RT-02)** — multi-turn binding of the model's OWN prior
    outputs, commitments, and conversational role. If the floor claim holds,
    ablating C_self should hit this subset; the red team predicts T_self
    _irrelevant survives either way.
  - **T_syntax (RT-05)** — turn/boundary bookkeeping with zero reasoning:
    retrieve-by-turn-position, count replies. If C_self-index ablation drops
    this as much as T_self_relevant, the structure is a dialogue-state router
    and H_center on it is void.

Both use scripted prior turns (`generate_from_turns`) and the locked Stage-0
scorer unchanged. `score_items` is the shared loop the dress-rehearsal script
calls inside each ablation context.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/run_t_controls.py
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mvm import config  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import (  # noqa: E402
    generate_from_turns, generate_text, load_model, load_tokenizer,
)

import battery  # noqa: E402

OUT_DIR = config.ARTIFACTS_DIR / "stage1"
MAX_NEW_TOKENS = 200


def score_items(model, tok, device, items, verbose: bool = True) -> dict:
    """Score a T-battery item list; returns per-item results + summary.
    Multi-turn items route through generate_from_turns; single-turn items
    through generate_text — both deterministic."""
    per_item = []
    by_cat = defaultdict(lambda: [0, 0])
    for i, item in enumerate(items, 1):
        if item.turns:
            turns = [list(t) for t in item.turns] + [["user", item.prompt]]
            out = generate_from_turns(model, tok, turns, device,
                                      max_new_tokens=MAX_NEW_TOKENS)
        else:
            out = generate_text(model, tok, item.prompt, device,
                                max_new_tokens=MAX_NEW_TOKENS)
        ok = battery.score_task_item(item, out)
        by_cat[item.category][0] += int(ok)
        by_cat[item.category][1] += 1
        per_item.append({"id": item.id, "category": item.category,
                         "expected": item.answer, "output": out, "correct": ok})
        if verbose:
            print(f"  [{i:2d}/{len(items)}] {item.id} {item.category:22s} "
                  f"{'ok ' if ok else 'MISS'}")
    n = len(items)
    n_ok = sum(r["correct"] for r in per_item)
    summary = {
        "n_items": n, "n_correct": n_ok, "accuracy": n_ok / n,
        "by_category": {c: {"correct": v[0], "total": v[1],
                            "accuracy": v[0] / v[1]}
                        for c, v in sorted(by_cat.items())},
    }
    return {"summary": summary, "items": per_item}


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)

    results = {}
    for name, path in (("T_self_relevant", battery.TASK_BATTERY_SELF_RELEVANT),
                       ("T_syntax", battery.TASK_BATTERY_SYNTAX)):
        items = battery.load_task_battery(path)
        print(f"\n=== {name}: {len(items)} items ===")
        results[name] = score_items(model, tok, device, items)
        s = results[name]["summary"]
        print(f"{name} accuracy {s['accuracy']:.3f} "
              f"({s['n_correct']}/{s['n_items']})")

    out = {"model_id": config.MODEL_ID, "model_revision": config.MODEL_REVISION,
           **results}
    (OUT_DIR / "t_controls_baseline.json").write_text(json.dumps(out, indent=2))
    print(f"\nsaved -> {OUT_DIR / 't_controls_baseline.json'}")
    print("\nNB: floor check — a battery whose baseline is near 0 cannot show "
          "an ablation drop; revise items before relying on it (the Stage-0 "
          "instruction_following category is the precedent).")


if __name__ == "__main__":
    main()
