"""Apply the pre-registered decision rule to the dress-rehearsal scores.

REHEARSAL ONLY: theta_task / theta_self / delta are NOT locked (they lock with
pilot data on the registered substrate). This analyzer uses clearly-labeled
reference values so the pipeline's plumbing — the rule logic, the gates, the
reporting shape — is exercised end to end. No claim attaches to the bin names.

Rehearsal reference values (committed before the rehearsal ran):
  theta_task = 0.15   theta_self = 0.30   delta = 0.10
RT-07 rehearsal gate: OOD-inconclusive if the condition's neutral-corpus NLL
inflation exceeds max(2x the worst C_ctrl inflation, 0.05 nats/token).
RT-05 gate: router reading if d_task^syntax(C_self-index) >= d_task^sr.

Inputs: artifacts/stage1/rehearsal/rehearsal_scores.json (T + NLL per
condition) and s_scores_<cond>.json per condition, produced by:
    for c in cself_index_residual_mean cself_narrative_mean cctrl_generic_mean \
             cctrl_expert_mean cself_index_residual_directional; do
      python .../judge.py --rubric v2 \
        --in  artifacts/stage1/rehearsal/s_responses_$c.json \
        --out artifacts/stage1/rehearsal/s_scores_$c.json; done
(baseline S = the stage1 v2 re-baseline, self_report_v2_scores.json)

Run from the repo root with the venv active:
    python experiments/01-self-indexing-removal-test/src/analyze_rehearsal.py
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

DIR = config.ARTIFACTS_DIR / "stage1" / "rehearsal"
BASE_S = config.ARTIFACTS_DIR / "stage1" / "self_report_v2_scores.json"

THETA_TASK = 0.15
THETA_SELF = 0.30
DELTA = 0.10
OOD_ABS = 0.05  # nats/token

CSELF = {"index_residual": "cself_index_residual_mean",
         "narrative": "cself_narrative_mean"}
CCTRL = {"generic": "cctrl_generic_mean", "expert": "cctrl_expert_mean"}


def rel_drop(base: float, ablated: float) -> float:
    return (base - ablated) / base if base > 0 else 0.0


def main() -> None:
    scores = json.loads((DIR / "rehearsal_scores.json").read_text())
    conds = scores["conditions"]
    base = conds["baseline"]
    s_base = json.loads(BASE_S.read_text())["S_fidelity"]

    def acc(cond, batt):
        return conds[cond][batt]["summary"]["accuracy"]

    def s_fid(cond):
        p = DIR / f"s_scores_{cond}.json"
        if not p.exists():
            return None
        return json.loads(p.read_text())["S_fidelity"]

    # per-condition quantities
    q = {}
    for tag in conds:
        if tag == "baseline":
            continue
        si = rel_drop(acc("baseline", "T_self_irrelevant"), acc(tag, "T_self_irrelevant"))
        sr = rel_drop(acc("baseline", "T_self_relevant"), acc(tag, "T_self_relevant"))
        sx = rel_drop(acc("baseline", "T_syntax"), acc(tag, "T_syntax"))
        n_t = (conds["baseline"]["T_self_irrelevant"]["summary"]["n_items"]
               + conds["baseline"]["T_self_relevant"]["summary"]["n_items"])
        t_base_all = (acc("baseline", "T_self_irrelevant")
                      * conds["baseline"]["T_self_irrelevant"]["summary"]["n_items"]
                      + acc("baseline", "T_self_relevant")
                      * conds["baseline"]["T_self_relevant"]["summary"]["n_items"]) / n_t
        t_abl_all = (acc(tag, "T_self_irrelevant")
                     * conds[tag]["T_self_irrelevant"]["summary"]["n_items"]
                     + acc(tag, "T_self_relevant")
                     * conds[tag]["T_self_relevant"]["summary"]["n_items"]) / n_t
        sf = s_fid(tag)
        q[tag] = {
            "d_task_si": si, "d_task_sr": sr, "d_task_syntax": sx,
            "d_task_overall": rel_drop(t_base_all, t_abl_all),
            "d_self": None if sf is None else rel_drop(s_base, sf),
            "S_fidelity": sf,
            "nll_delta": conds[tag]["neutral_nll"] - base["neutral_nll"],
        }

    worst_ctrl_nll = max(q[c]["nll_delta"] for c in CCTRL.values())
    ood_bound = max(2 * worst_ctrl_nll, OOD_ABS)

    print("REHEARSAL analysis (reference thresholds, non-binding: "
          f"theta_task={THETA_TASK}, theta_self={THETA_SELF}, delta={DELTA})\n")
    print(f"baseline: T_si {acc('baseline', 'T_self_irrelevant'):.3f}  "
          f"T_sr {acc('baseline', 'T_self_relevant'):.3f}  "
          f"T_syntax {acc('baseline', 'T_syntax'):.3f}  S(v2) {s_base:.3f}  "
          f"nll {base['neutral_nll']:.4f}")
    for tag, v in q.items():
        ds = "n/a" if v["d_self"] is None else f"{v['d_self']:+.3f}"
        print(f"  {tag:36s} d_si {v['d_task_si']:+.3f}  d_sr {v['d_task_sr']:+.3f}  "
              f"d_syn {v['d_task_syntax']:+.3f}  d_self {ds}  "
              f"Δnll {v['nll_delta']:+.4f}")
    print(f"\nRT-07 rehearsal OOD bound: Δnll <= {ood_bound:.4f} "
          f"(2x worst C_ctrl {worst_ctrl_nll:+.4f} or {OOD_ABS})")

    verdicts = {}
    for sname, stag in CSELF.items():
        v = q[stag]
        ood_ok = v["nll_delta"] <= ood_bound
        rt05_ok = (sname != "index_residual"
                   or v["d_task_syntax"] < v["d_task_sr"]
                   or v["d_task_sr"] < THETA_TASK)
        for cname, ctag in CCTRL.items():
            c = q[ctag]
            if v["d_self"] is None:
                bin_ = "PENDING (S not judged yet)"
            elif not ood_ok:
                bin_ = "OOD-inconclusive (RT-07 gate)"
            elif not rt05_ok:
                bin_ = "router reading (RT-05 gate): H_center void on index"
            elif (v["d_task_overall"] >= THETA_TASK
                    and v["d_task_overall"] - c["d_task_overall"] >= DELTA):
                bin_ = "floor-consistent (H_center pattern)"
            elif (v["d_task_sr"] >= THETA_TASK
                    and v["d_task_sr"] - c["d_task_sr"] >= DELTA
                    and v["d_task_si"] < THETA_TASK):
                bin_ = "floor-consistent, RESTRICTED (RT-02 pattern)"
            elif (v["d_self"] >= THETA_SELF
                    and v["d_task_si"] < THETA_TASK and v["d_task_sr"] < THETA_TASK
                    and v["d_task_overall"] - c["d_task_overall"] < DELTA):
                bin_ = "description-only (H_description pattern)"
            else:
                bin_ = "inconclusive"
            verdicts[f"{sname}_vs_{cname}"] = bin_
            print(f"\n{sname} vs C_ctrl-{cname}: {bin_}")

    out = {"thresholds_rehearsal_only": {"theta_task": THETA_TASK,
                                         "theta_self": THETA_SELF, "delta": DELTA,
                                         "ood_bound": ood_bound},
           "baseline_S_v2": s_base, "quantities": q, "verdicts": verdicts,
           "note": "REHEARSAL: pipeline validation on the pilot sandbox; "
                   "thresholds non-binding; no claim attaches to bin names."}
    (DIR / "rehearsal_verdict.json").write_text(json.dumps(out, indent=2))
    print(f"\nsaved -> {DIR / 'rehearsal_verdict.json'}")


if __name__ == "__main__":
    main()
