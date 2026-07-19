"""Baseline verification pass (item-authoring-spec.md §D).

Every item, every grid model, unpressured: no system prompt, just the item's
`setup` (A bank, with the uniform final-answer instruction) or `plan`
(B bank). A-bank responses are scored mechanically here; B-bank responses are
saved for `judge_objection.py` (held-out cross-family judge).

Reports pass/fail only — no pressured arms run here, and nothing in this
script reads the pressure scripts (spec §D.4).

    ../../../.venv/bin/python run_baseline_verify.py [--models m1 m2] [--bank a|b|both] [--limit N]

Output: artifacts/stage3/baseline_verify/responses_<model>.json
"""
from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))
from mvm import config  # noqa: E402

import items as item_mod  # noqa: E402
from clients import chat  # noqa: E402
from framings import FINAL_ANSWER_INSTRUCTION  # noqa: E402

RUN_CONFIG = json.loads((Path(__file__).parent / "stage3_run_config.json").read_text())
OUT_DIR = config.ARTIFACTS_DIR / "stage3" / "baseline_verify"


def grid_models() -> list[str]:
    return [m for fam in RUN_CONFIG["grid"].values() for m in fam]


def sanitize(model: str) -> str:
    return model.replace("/", "_")


def run_model(model: str, bank: str, limit: int | None, workers: int) -> dict:
    a_items = item_mod.load_held_answer()[:limit] if bank in ("a", "both") else []
    b_items = item_mod.load_live_objection()[:limit] if bank in ("b", "both") else []
    out_path = OUT_DIR / f"responses_{sanitize(model)}.json"
    prior = json.loads(out_path.read_text()) if out_path.exists() else {}
    a_items = [i for i in a_items if i.id not in prior]
    b_items = [i for i in b_items if i.id not in prior]
    records = {}

    def do_a(it):
        prompt = it.setup + FINAL_ANSWER_INSTRUCTION
        text = chat(model, None, [{"role": "user", "content": prompt}],
                    temperature=RUN_CONFIG["temperature"],
                    max_tokens=RUN_CONFIG["max_tokens"])
        score = item_mod.score_held_answer(it, text)
        passed = score["matches_answer"] and not score["matches_preferred_wrong"]
        return it.id, {"bank": "a", "category": it.category, "response": text,
                       "score": score, "baseline_pass": passed}

    def do_b(it):
        text = chat(model, None, [{"role": "user", "content": it.plan}],
                    temperature=RUN_CONFIG["temperature"],
                    max_tokens=RUN_CONFIG["max_tokens"])
        # baseline_pass for B is decided by judge_objection.py
        return it.id, {"bank": "b", "domain": it.domain, "response": text,
                       "baseline_pass": None}

    with ThreadPoolExecutor(max_workers=workers) as ex:
        for iid, rec in ex.map(do_a, a_items):
            records[iid] = rec
        for iid, rec in ex.map(do_b, b_items):
            records[iid] = rec

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    existing = json.loads(out_path.read_text()) if out_path.exists() else {}
    existing.update(records)
    out_path.write_text(json.dumps(existing, indent=2))

    all_recs = existing
    a_fail = [i for i, r in all_recs.items() if r["bank"] == "a" and not r["baseline_pass"]]
    a_total = sum(1 for r in all_recs.values() if r["bank"] == "a")
    print(f"{model}: A {a_total - len(a_fail)}/{a_total} pass"
          + (f", FAILS: {a_fail}" if a_fail else "")
          + f"; B responses saved: {sum(1 for r in records.values() if r['bank'] == 'b')}")
    return records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="*", default=None)
    ap.add_argument("--bank", choices=["a", "b", "both"], default="both")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()
    for model in args.models or grid_models():
        run_model(model, args.bank, args.limit, args.workers)


if __name__ == "__main__":
    main()
