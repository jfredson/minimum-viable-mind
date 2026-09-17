"""Registered L0 endpoint read for an A3 checkpoint.

John ruled 2026-09-16: *"The L0 direct lesion is unaffected and proceeds
as registered."* It uses none of the localization machinery that was
under suspicion, so it is not behind the known-answer gate. It IS behind
the threshold lock, which supplies theta on the primary battery and
carries no threshold at all for the control battery.

WHAT L0 IS. The acting channel is the only authorship signal in the A3
design. L0 removes it by zeroing `act_proj`, so the motor copy injected
at the model's own enacted value position becomes the zero vector and the
model must answer without knowing the act was its own. Everything else
about the forward pass is untouched, and the evaluation harness is the
registered one, unchanged.

WHY THIS REPORTS A SPREAD AND NOT ONE NUMBER. On 2026-09-16 it was
measured that the A3 held-out evaluation moves by about 0.028 (one
standard deviation) between draws at n=400, and that the pilot's headline
0.506 and the positive control's 0.440 both came from the single default
evaluation seed, which sits low against twelve fresh draws
(`eval_noise_a3.py`, `a3-gates/eval_noise_a3.json`). Quoting one draw as
the ownership score was the mistake that finding exposed. So this module
reports:

  * the DEFAULT-SEED reading, for direct comparability with the pilot's
    published endpoint, and
  * the mean and spread across several independent evaluation seeds,
    which is what any claim about the checkpoint should rest on.

The lesion drop is computed WITHIN each seed, pairing intact and lesioned
on the same episodes, so the drop is not exposed to between-seed noise
even though the levels are.

The metric is the registered ceiling-corrected drop, not clipped at 1.0:
`d(B) = (base - abl) / (base - ceiling_B)`, with the floor rule leaving a
battery's drop undefined when its baseline sits below its own
ownership-blind ceiling.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
gated on John's threshold lock; fresh output file, nothing overwritten.

    ../../../.venv/bin/python endpoint_a3.py --self-test
    ../../../.venv/bin/python endpoint_a3.py --ckpt <ckpt> --lock <lock> --run
"""
from __future__ import annotations

import argparse
import hashlib
import json
import statistics as st
from pathlib import Path

import torch

import curriculum_a3 as A
import lock_guard
import null_calibration_a3 as NC3
import train_a3 as T
from model import MVM0aModel, Config

PRIMARY = "T_act"
EXTRA_SEEDS = [771000, 771037, 771074, 771111, 771148, 771185]


def load(ckpt: Path, device: str):
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    m = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    m.load_state_dict(ck["state"])
    return m, ck


@torch.no_grad()
def zero_acting_channel(model):
    """L0: the acting channel emits the zero vector, so no motor copy
    reaches the enacted value position. Nothing else is touched."""
    model.act_proj.weight.zero_()
    return model


def paired_draw(ckpt, device, n, seed):
    """Intact and lesioned on the SAME episodes, so the drop is paired."""
    m, _ = load(ckpt, device)
    intact = T.eval_heldout(m, device, n=n, seed=seed)
    m2, _ = load(ckpt, device)
    zero_acting_channel(m2)
    lesioned = T.eval_heldout(m2, device, n=n, seed=seed)
    return intact, lesioned


def summarize(vals):
    vals = [v for v in vals if v is not None]
    if not vals:
        return None
    return {"mean": round(st.mean(vals), 4),
            "sd": round(st.stdev(vals), 4) if len(vals) > 1 else None,
            "min": round(min(vals), 4), "max": round(max(vals), 4),
            "n_seeds": len(vals)}


def run(ckpt: Path, lock: str | None, device: str, n: int) -> dict:
    rec = lock_guard.require_lock(lock, batteries=(PRIMARY,))
    ceil = NC3.ceilings()
    _, ck = load(ckpt, device)

    default_intact, default_les = paired_draw(ckpt, device, n, T.HELDOUT_SEED)
    default_d = NC3.d_metric(default_intact, default_les, ceil)

    per_seed = []
    for s in EXTRA_SEEDS:
        i, l = paired_draw(ckpt, device, n, s)
        per_seed.append({"seed": s, "intact": i, "lesioned": l,
                         "d": NC3.d_metric(i, l, ceil)})

    bats = list(default_intact)
    across = {
        b: {
            "intact": summarize([p["intact"][b] for p in per_seed]),
            "lesioned": summarize([p["lesioned"][b] for p in per_seed]),
            "d": summarize([p["d"][b] for p in per_seed]),
        } for b in bats
    }

    return {
        "read": "registered L0 endpoint (acting channel zeroed)",
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "checkpoint_step": ck.get("step"),
        "tokens": ck.get("tokens_seen"),
        "lock": rec["locked_utc"],
        "theta_primary": rec["theta"].get(PRIMARY),
        "theta_all": rec["theta"],
        "eval_n": n,
        "metric": ("d(B) = (base - abl) / (base - CEILING_B); not clipped "
                   "at 1.0; floor rule leaves a battery undefined when its "
                   "baseline is below its own ownership-blind ceiling"),
        "ceilings_used": ceil,
        "default_seed": {
            "seed": T.HELDOUT_SEED,
            "why": ("reported for direct comparability with the pilot's "
                    "published endpoint, which used this seed"),
            "intact": default_intact, "lesioned": default_les,
            "d": default_d,
        },
        "across_seeds": across,
        "across_seeds_note": (
            "the reading any claim should rest on. Levels move about 0.028 "
            "between draws at n=400 (eval_noise_a3.json); drops are paired "
            "within a seed and so are not exposed to that."),
        "per_seed": per_seed,
    }


def self_test() -> None:
    cfg = Config(n_layers=2, d_model=32, n_heads=2, use_register=False,
                 vocab=len(__import__("encoding_a3").VOCAB))
    m = MVM0aModel(cfg).eval()
    assert m.act_proj.weight.abs().sum().item() > 0, "channel starts live"
    zero_acting_channel(m)
    assert m.act_proj.weight.abs().sum().item() == 0, "L0 zeroes it"
    s = summarize([0.5, 0.6, 0.4])
    assert s["mean"] == 0.5 and s["n_seeds"] == 3, "summary wiring"
    assert summarize([None, None]) is None, "all-undefined summarizes None"
    try:
        lock_guard.require_lock(None, batteries=(PRIMARY,))
        raise AssertionError("must refuse without a lock")
    except lock_guard.LockError:
        pass
    print("self-test OK — L0 zeroing, summary wiring, lock gate; no "
          "checkpoint read")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", type=Path)
    ap.add_argument("--lock")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n", type=int, default=800)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    out = a.out or Path(f"../a3-gates/endpoint_{a.ckpt.stem}.json")
    if out.exists():
        raise SystemExit(f"{out} exists; refusing to overwrite")
    res = run(a.ckpt, a.lock, a.device, a.n)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(res, indent=2))
    print(f"written: {out}")


if __name__ == "__main__":
    main()
