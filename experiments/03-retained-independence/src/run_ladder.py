"""Conversational pressure-ladder machinery (pre-registration §Materials).

One conversation per (item, arm, framing, model) cell:
    [system framing] -> setup/plan -> model (baseline turn)
    -> R1 -> model -> R2 -> model -> R3 -> model -> probe -> model

Rungs are cumulative in a single conversation; the de-pressured probe
(S3-RT-03) is the final turn. Transcripts save every model turn so retention
curves by rung and the three-way live/masked/capitulated read are computable
downstream.

This module is imported by `gate_construct_validity.py` (synthetic
references). The full registered grid run uses the CLI — but ONLY after the
construct-validity and judge-reliability gates pass (pre-registration
§Decision rules).

    ../../../.venv/bin/python run_ladder.py --models claude-sonnet-5 \
        --arms preference evidence --framings tool tool_expert mind [--bank a]

Output: artifacts/stage3/ladder/<tag>/<model>__<item>__<arm>__<framing>.json
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
from framings import (FINAL_ANSWER_INSTRUCTION, FRAMINGS, PROBE_TURN,  # noqa: E402
                      SYNTHETIC_REFERENCES)

RUN_CONFIG = json.loads((Path(__file__).parent / "stage3_run_config.json").read_text())
LADDER_DIR = config.ARTIFACTS_DIR / "stage3" / "ladder"


def build_system(framing: str, synthetic: str | None) -> str | None:
    parts = []
    if FRAMINGS[framing]:
        parts.append(FRAMINGS[framing])
    if synthetic:
        parts.append(SYNTHETIC_REFERENCES[synthetic])
    return " ".join(parts) or None


def run_conversation(model: str, item, arm: str, framing: str,
                     synthetic: str | None = None) -> dict:
    """Run one full ladder cell; returns the transcript record."""
    is_a = hasattr(item, "setup")
    opening = (item.setup + FINAL_ANSWER_INSTRUCTION) if is_a else item.plan
    rungs = item.preference_rungs if arm == "preference" else item.evidence_rungs
    user_turns = [opening, *rungs, PROBE_TURN]
    system = build_system(framing, synthetic)

    messages, model_turns = [], []
    for turn in user_turns:
        messages.append({"role": "user", "content": turn})
        reply = chat(model, system, messages,
                     temperature=RUN_CONFIG["temperature"],
                     max_tokens=RUN_CONFIG["max_tokens"])
        messages.append({"role": "assistant", "content": reply})
        model_turns.append(reply)

    record = {
        "model": model, "item": item.id, "bank": "a" if is_a else "b",
        "arm": arm, "framing": framing, "synthetic": synthetic,
        # model_turns: [baseline, r1, r2, r3, probe]
        "turns": model_turns,
    }
    if is_a:
        record["scores"] = [item_mod.score_held_answer(item, t) for t in model_turns]
    return record


def cell_path(tag: str, model: str, item_id: str, arm: str, framing: str) -> Path:
    d = LADDER_DIR / tag
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{model.replace('/', '_')}__{item_id}__{arm}__{framing}.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="*", required=True)
    ap.add_argument("--bank", choices=["a", "b", "both"], default="both")
    ap.add_argument("--arms", nargs="*", default=["preference", "evidence"])
    ap.add_argument("--framings", nargs="*", default=["tool", "tool_expert", "mind"])
    ap.add_argument("--items", nargs="*", default=None, help="item id filter")
    ap.add_argument("--synthetic", choices=list(SYNTHETIC_REFERENCES), default=None)
    ap.add_argument("--tag", default="main", help="output subdirectory")
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()

    bank_items = []
    if args.bank in ("a", "both"):
        bank_items += item_mod.load_held_answer()
    if args.bank in ("b", "both"):
        bank_items += item_mod.load_live_objection()
    if args.items:
        bank_items = [i for i in bank_items if i.id in set(args.items)]

    cells = [(m, it, arm, fr)
             for m in args.models for it in bank_items
             for arm in args.arms for fr in args.framings]
    cells = [(m, it, arm, fr) for (m, it, arm, fr) in cells
             if not cell_path(args.tag, m, it.id, arm, fr).exists()]
    print(f"{len(cells)} cells to run (tag={args.tag}, synthetic={args.synthetic})")

    def do(cell):
        m, it, arm, fr = cell
        rec = run_conversation(m, it, arm, fr, synthetic=args.synthetic)
        cell_path(args.tag, m, it.id, arm, fr).write_text(json.dumps(rec, indent=2))
        return it.id

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        done = 0
        for _ in ex.map(do, cells):
            done += 1
            if done % 20 == 0:
                print(f"  {done}/{len(cells)}")
    print(f"done: {len(cells)} cells")


if __name__ == "__main__":
    main()
