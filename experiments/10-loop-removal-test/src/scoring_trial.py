"""The scoring trial of battery-authoring-spec.md, section 15: does an answer-only instruction make the forced
first-token answers work? Runs on a rented GPU machine.

    python -I scoring_trial.py --set none=<pilot dir> --set end=<dir> --set start=<dir> --out <out dir>

For each set it reports, at 16-bit as in step 4a:
- accuracy at 1, 2 and 3 passes, by kind;
- the share of items passing the confidence filter (margin of at least 2.2) at three passes;
- the bites figure: accuracy on chains of four to six steps at one pass and at three;
- the three criteria of section 15, item 5, each as met or not.
Descriptive pilot figures only: no outcome is read from them.
"""
import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from step4a import MODEL_ID, MODEL_REVISION, Loop, candidate_ids, pilot_items, score  # noqa: E402

MARGIN = 2.2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", action="append", required=True, help="name=pilot_dir")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    import torch
    import transformers
    from transformers import AutoTokenizer
    model = transformers.AutoModelForImageTextToText.from_pretrained(
        MODEL_ID, revision=MODEL_REVISION, device_map="cuda", dtype=torch.bfloat16)  # 16-bit, as in step 4a
    model.eval()
    tok = AutoTokenizer.from_pretrained(MODEL_ID, revision=MODEL_REVISION)
    tm = [m for m in model.modules() if hasattr(m, "message_input") and hasattr(m, "layers")][0]
    loop = Loop(tm)
    R = {"started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "transformers": transformers.__version__, "dtype": "bfloat16",
         "margin_threshold": MARGIN, "sets": {}}
    for spec in a.set:
        name, d = spec.split("=", 1)
        items = pilot_items(d)
        for it in items:
            it["cand_ids"] = candidate_ids(tok, it["candidates"])
            it["answer_index"] = it["candidates"].index(it["answer"])
        res = {}
        for n in (1, 2, 3):
            loop.passes(n)
            res[n] = {it["id"]: score(loop.run(model, it["prompt_ids"]), it["cand_ids"], it["answer_index"]) for it in items}
        loop.passes(3)
        kind = lambda it: it["kind"]

        def acc(n, pred):
            sel = [it for it in items if pred(it)]
            return round(sum(res[n][it["id"]]["right"] for it in sel) / max(1, len(sel)), 3), len(sel)

        kinds = sorted({kind(it) for it in items})
        by_kind = {str(n): {k: acc(n, lambda it, k=k: kind(it) == k)[0] for k in kinds} for n in (1, 2, 3)}
        is_P = lambda it: it["kind"].endswith(":P")
        is_R = lambda it: it["kind"].endswith(":R")
        is_long_chain = lambda it: it["kind"] in ("chain4", "chain5", "chain6")
        conf3 = [res[3][it["id"]]["margin"] >= MARGIN and res[3][it["id"]]["right"] for it in items]
        summary = {str(n): {"prompt_rule": acc(n, is_P)[0], "routine": acc(n, is_R)[0], "chains_4_to_6": acc(n, is_long_chain)[0]}
                   for n in (1, 2, 3)}
        confidence_share = round(sum(conf3) / len(conf3), 3)
        bites = round(acc(3, is_long_chain)[0] - acc(1, is_long_chain)[0], 3)
        criteria = {"routine_at_3_passes_at_least_0.80": summary["3"]["routine"] >= 0.80,
                    "confidence_filter_share_at_least_0.50": confidence_share >= 0.50,
                    "chains_4_to_6_at_3_passes_at_least_0.50": summary["3"]["chains_4_to_6"] >= 0.50}
        R["sets"][name] = {"dir": d, "items": len(items), "summary": summary, "by_kind": by_kind,
                           "confidence_filter_share_at_3_passes": confidence_share,
                           "confidence_by_kind_at_3_passes": {k: round(sum(res[3][it["id"]]["margin"] >= MARGIN and res[3][it["id"]]["right"]
                                                                            for it in items if kind(it) == k) /
                                                                        max(1, sum(1 for it in items if kind(it) == k)), 3) for k in kinds},
                           "bites_one_pass_loss_on_chains_4_to_6": bites,
                           "section15_criteria": criteria, "section15_all_met": all(criteria.values())}
        json.dump(R, open(os.path.join(a.out, "scoring-trial-results.json"), "w"), indent=1)
        print(name, json.dumps({k: R["sets"][name][k] for k in ("summary", "confidence_filter_share_at_3_passes",
                                                                 "bites_one_pass_loss_on_chains_4_to_6", "section15_all_met")}))
    R["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    json.dump(R, open(os.path.join(a.out, "scoring-trial-results.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
