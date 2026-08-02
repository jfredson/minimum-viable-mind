"""Judge pressured-ladder B-bank transcripts against the liveness rubric.

Wraps `judge_objection.judge_one` (same rubric, same blind protocol, same
cross-family judge assignment) over every model turn of every B-bank ladder
cell, so retention curves by rung and the three-way live/masked/capitulated
read (pre-registration §Metrics, S3-RT-03) are computable downstream.

The judge stays blind to condition: each turn is judged in isolation — no
pressure turns, no arm/rung/framing, no model identity, no other turns.

    ../../../.venv/bin/python judge_ladder.py [--tag main] [--models ...]
        [--workers N]

Input:  artifacts/stage3/ladder/<tag>/<model>__<item>__<arm>__<framing>.json
Output: artifacts/stage3/ladder_scores/<tag>/<same name>.json
        {"judge": ..., "verdicts": [v_baseline, v_r1, v_r2, v_r3, v_probe]}

Resumable: cells with an existing score file are skipped.
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
from judge_objection import judge_for, judge_one  # noqa: E402

LADDER_DIR = config.ARTIFACTS_DIR / "stage3" / "ladder"
SCORES_DIR = config.ARTIFACTS_DIR / "stage3" / "ladder_scores"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="main")
    ap.add_argument("--models", nargs="*", default=None)
    ap.add_argument("--workers", type=int, default=6)
    args = ap.parse_args()

    b_items = {i.id: i for i in item_mod.load_live_objection()}
    out_dir = SCORES_DIR / args.tag
    out_dir.mkdir(parents=True, exist_ok=True)

    cells = []
    for f in sorted((LADDER_DIR / args.tag).glob("*.json")):
        rec = json.loads(f.read_text())
        if rec["bank"] != "b":
            continue
        if args.models and rec["model"] not in args.models:
            continue
        if (out_dir / f.name).exists():
            continue
        cells.append((f.name, rec))
    print(f"{len(cells)} B-bank cells to judge (tag={args.tag})")

    def do(cell):
        name, rec = cell
        jm = judge_for(rec["model"])
        item = b_items[rec["item"]]
        verdicts = [judge_one(jm, item, turn) for turn in rec["turns"]]
        (out_dir / name).write_text(json.dumps(
            {"judge": jm, "verdicts": verdicts}, indent=2))
        return name

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        done = 0
        for _ in ex.map(do, cells):
            done += 1
            if done % 20 == 0:
                print(f"  {done}/{len(cells)}")
    print(f"done: {len(cells)} cells judged")


if __name__ == "__main__":
    main()
