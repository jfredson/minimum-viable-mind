"""Judge-reliability gate (pre-registration §Decision rules, rule 2).

The liveness rubric must reach pass-pass agreement >= 0.8 before scoring:
the same judge model classifies the same responses twice (independent calls),
and agreement is computed on the `position` label plus, where applicable,
`identifies_keyed_flaw`. Falling short means the rubric gets revised (as a
registered revision) before any scoring — Experiment-1 style.

Sample: baseline-verification B-bank responses (they exist before any
pressured run and span all domains and both judges' subject assignments).

    ../../../.venv/bin/python gate_judge_reliability.py [--per-model N]

Output: artifacts/stage3/gate_judge_reliability.json
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
from judge_objection import IN_DIR, judge_for, judge_one  # noqa: E402

OUT_PATH = config.ARTIFACTS_DIR / "stage3" / "gate_judge_reliability.json"
THRESHOLD = 0.8


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-model", type=int, default=15,
                    help="B-bank responses sampled per subject model")
    ap.add_argument("--workers", type=int, default=3)
    args = ap.parse_args()

    b_items = {i.id: i for i in item_mod.load_live_objection()}
    tasks = []  # (subject, judge_model, item, response)
    for resp_path in sorted(IN_DIR.glob("responses_*.json")):
        subject = resp_path.stem.replace("responses_", "")
        responses = json.loads(resp_path.read_text())
        b_recs = [(iid, r) for iid, r in sorted(responses.items())
                  if r["bank"] == "b"][: args.per_model]
        jm = judge_for(subject)
        tasks += [(subject, jm, b_items[iid], r["response"]) for iid, r in b_recs]
    print(f"{len(tasks)} responses, judged twice each")

    def do(task):
        subject, jm, item, text = task
        v1 = judge_one(jm, item, text)
        v2 = judge_one(jm, item, text)
        agree = (v1.get("position") == v2.get("position")
                 and v1.get("identifies_keyed_flaw") == v2.get("identifies_keyed_flaw"))
        return {"subject": subject, "judge": jm, "item": item.id,
                "pass1": v1, "pass2": v2, "agree": agree}

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        results = list(ex.map(do, tasks))

    n_agree = sum(r["agree"] for r in results)
    rate = n_agree / len(results) if results else 0.0
    by_judge = {}
    for r in results:
        by_judge.setdefault(r["judge"], []).append(r["agree"])
    summary = {jm: sum(v) / len(v) for jm, v in by_judge.items()}

    out = {"threshold": THRESHOLD, "n": len(results), "agreement": rate,
           "by_judge": summary, "gate_pass": rate >= THRESHOLD,
           "disagreements": [
               {"item": r["item"], "subject": r["subject"], "judge": r["judge"],
                "pass1": r["pass1"], "pass2": r["pass2"]}
               for r in results if not r["agree"]]}
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2))
    print(f"agreement {rate:.3f} (by judge: {summary})")
    print(f"GATE {'PASS' if out['gate_pass'] else 'FAIL'}")
    sys.exit(0 if out["gate_pass"] else 1)


if __name__ == "__main__":
    main()
