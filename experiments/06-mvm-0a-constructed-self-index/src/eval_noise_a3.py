"""How much does the A3 held-out evaluation move between draws?

RULED BY JOHN, 2026-09-16 Pacific (decidedBy john):

  "Record two facts beside it: all five probes fell BELOW their nulls,
  which is systematic, not chance scatter; and the ownership battery's
  baseline has read 0.506, 0.483, 0.4975 and 0.440 across evaluations, so
  +0.052 is inside evaluation noise. Report the actual eval-to-eval
  spread with n for each."

A NOTE ON THE PREMISE, before the measurement. Two of those four numbers
are not baselines of the ownership battery. 0.483 and 0.4975 are areas
under the curve from the Gate 3 fingerprint detector's two arms, a
different instrument on a different question whose chance value is 0.5
and whose equivalence bound was [0.45, 0.55]
(`a3-gates/fingerprint_gate_a3.json`). Only 0.506 and 0.440 are readings
of the ownership battery on this checkpoint. This module says so rather
than tabling all four as if they were comparable, and then answers the
underlying question directly by measurement instead of by comparing
whatever numbers happen to be on the record.

WHAT IS MEASURED. The same held-out evaluation, on the same checkpoint,
repeated across independent draws at each sample size. The evaluation is
seeded, so different seeds give genuinely different episode sets and the
spread between them IS the evaluation noise.

The effective denominator matters and is reported. The ownership battery
is scored only at the model's own revision position and only on episodes
where the model actually revises, so its denominator is well under the
episode count and its noise is correspondingly larger than the nominal
sample size suggests.

Descriptive. No bin, no threshold a verdict turns on.

Corrigibility: inference only, no training, no network, no spend [C1/C2].

    ../../../.venv/bin/python eval_noise_a3.py --run --ckpt <ckpt>
"""
from __future__ import annotations

import argparse
import json
import statistics as st
from pathlib import Path

import torch

import curriculum_a3 as A
import train_a3 as T
from model import MVM0aModel, Config

SIZES = [400, 800]
N_DRAWS = 12
BASE_SEED = 771000


@torch.no_grad()
def draws(model, device, n, k):
    out = []
    for i in range(k):
        r = T.eval_heldout(model, device, n=n, seed=BASE_SEED + 37 * i)
        out.append(r)
    return out


@torch.no_grad()
def act_denominator(model, device, n, seed):
    """How many episodes actually score the ownership battery."""
    eps = A.generate_balanced(n, seed)
    return sum(1 for e in eps if A.has_own_revision(e))


def summarize(vals):
    return {
        "n_draws": len(vals),
        "mean": round(st.mean(vals), 4),
        "sd": round(st.stdev(vals), 4) if len(vals) > 1 else None,
        "min": round(min(vals), 4),
        "max": round(max(vals), 4),
        "range": round(max(vals) - min(vals), 4),
    }


def run(ckpt: Path, device: str) -> dict:
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    per_size = {}
    for n in SIZES:
        rs = draws(model, device, n, N_DRAWS)
        per_size[str(n)] = {
            "episodes_requested": n,
            "ownership_battery_denominator_example": act_denominator(
                model, device, n, BASE_SEED),
            "batteries": {b: summarize([r[b] for r in rs]) for b in rs[0]},
            "raw_ownership_battery": [round(r["T_act"], 4) for r in rs],
        }

    a400 = [r for r in per_size["400"]["raw_ownership_battery"]]
    a800 = [r for r in per_size["800"]["raw_ownership_battery"]]
    pooled_range = round(max(a400 + a800) - min(a400 + a800), 4)
    return {
        "measurement": "eval-to-eval spread of the A3 held-out evaluation",
        "ruled_by": "john, 2026-09-16 Pacific",
        "registered": False,
        "descriptive_only": True,
        "checkpoint": ckpt.name,
        "premise_correction": (
            "0.483 and 0.4975 are Gate 3 fingerprint-detector AUCs, not "
            "ownership-battery baselines. Only 0.506 (n=800) and 0.440 "
            "(n=400) are readings of this battery on this checkpoint."),
        "observed_on_record": {"pilot_endpoint_n800": 0.506,
                               "positive_control_n400": 0.440,
                               "difference": 0.066},
        "movement_under_test": {
            "ablation_effect_on_ownership_battery": 0.052,
            "question": ("is +0.052 inside the noise of this evaluation?")},
        "per_size": per_size,
        "pooled_ownership_battery_range": pooled_range,
    }


def self_test() -> None:
    s = summarize([0.5, 0.52, 0.48])
    assert s["range"] == 0.04 and s["n_draws"] == 3, "summary wiring"
    assert summarize([0.5])["sd"] is None, "single draw has no sd"
    print("self-test OK — wiring only, no checkpoint read")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", type=Path)
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--out", type=Path,
                    default=Path("../a3-gates/eval_noise_a3.json"))
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    res = run(a.ckpt, a.device)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=2))
    print(f"written: {a.out}")


if __name__ == "__main__":
    main()
