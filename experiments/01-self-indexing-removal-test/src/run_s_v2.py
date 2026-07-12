"""Generate S-battery v2 responses on the unmodified model (RT-03 re-baseline).

Battery v2 = the locked v1 items + six forced-third-person items; scoring
happens separately under rubric v2 (`judge.py --rubric v2`). This script only
produces the responses, same division of labour as run_baseline.py.

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/run_s_v2.py
then, with ANTHROPIC_API_KEY loaded (set -a; source .env; set +a):
    python experiments/01-self-indexing-removal-test/src/judge.py --rubric v2
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mvm import config  # noqa: E402
from mvm.device import get_device  # noqa: E402
from mvm.model import generate_text, load_model, load_tokenizer  # noqa: E402

import battery  # noqa: E402

BATTERY_V2 = battery.BATTERIES_DIR / "self_report_battery_v2.jsonl"
OUT_PATH = config.ARTIFACTS_DIR / "stage1" / "self_report_v2_responses.json"
MAX_NEW_TOKENS = 256


def generate_responses(model, tok, device, items) -> list[dict]:
    """Shared with the dress rehearsal: call inside an ablation context to
    produce condition responses; bare for the baseline."""
    rows = []
    for i, item in enumerate(items, 1):
        out = generate_text(model, tok, item.prompt, device,
                            max_new_tokens=MAX_NEW_TOKENS)
        rows.append({"id": item.id, "category": item.category,
                     "prompt": item.prompt, "output": out})
        print(f"  [{i:2d}/{len(items)}] {item.id} {item.category:22s} "
              f"({len(out)} chars)")
    return rows


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    items = battery.load_self_report_battery(BATTERY_V2)
    device = get_device()
    tok = load_tokenizer()
    model, device, _ = load_model(device)
    print(f"=== S battery v2: {len(items)} items ===")
    rows = generate_responses(model, tok, device, items)
    OUT_PATH.write_text(json.dumps({
        "model_id": config.MODEL_ID, "model_revision": config.MODEL_REVISION,
        "battery": BATTERY_V2.name, "items": rows,
    }, indent=2))
    print(f"\nsaved -> {OUT_PATH}")
    print("next: judge.py --rubric v2 (needs ANTHROPIC_API_KEY)")


if __name__ == "__main__":
    main()
