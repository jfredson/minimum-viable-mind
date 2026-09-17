"""Is the register constant in every register-bearing checkpoint?

RULED BY JOHN, 2026-09-16 Pacific (decidedBy john), quoted:

  "Check whether the register is constant in the other register-bearing
  checkpoints (pilot seed 0 full, s1 full, s2 full), and at any saved
  intermediate steps, to see when it saturated. Report per checkpoint."

The unblinded direct probe found that on the seed-0 full checkpoint the
register collapses to a vector identical across every episode after the
third write of a forward pass, and encodes no own-agent identity even
before that. This asks whether that is one checkpoint's accident or a
property of the architecture as trained.

WHAT IS MEASURED, per checkpoint and per turn: the across-episode spread
of the register state. If every episode produces the same register, that
spread is at the floating-point floor and the register carries no
episode-specific information at all. Also the distance the register has
travelled from its initialization, which separates "saturated" from
"never written".

Descriptive throughout. No bin, no threshold that a verdict turns on. The
one number with a stated meaning is the collapse turn, defined as the
first turn at which across-episode spread falls below 1e-5, which is four
orders of magnitude under the pre-collapse spread actually observed and
two above float32 noise. That boundary is reported alongside the raw
per-turn numbers so anyone can pick a different one.

The twins are register-less by construction and have no register to
measure. They are listed and skipped, not silently absent.

Corrigibility: inference only, no training, no network, no spend [C1/C2].

    ../../../.venv/bin/python register_saturation_survey.py --run
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import numpy as np
import torch

import curriculum as C
import encoding as E
import null_calibration as NC
from model import MVM0aModel, Config, to_torch
from train import enact_batched

COLLAPSE_FLOOR = 1e-5      # stated convention, reported with the raw numbers
ART = Path('/Users/john/Code/minimum-viable-mind/experiments/'
           '06-mvm-0a-constructed-self-index/artifacts')

# The five local 30M A2 checkpoints. "full" is register-bearing; "twin" is
# register-less by construction [RT-03].
CHECKPOINTS = [
    ("pilot seed-0 full", ART / 'pilot_a1_30m_seed0/pilot_a1_30m_seed0.pt'),
    ("pilot seed-1 full", ART / 'pilot_a1_30m_seed1/pilot_a1_30m_seed1.pt'),
    ("pilot seed-2 full", ART / 'pilot_a1_30m_seed2/pilot_a1_30m_seed2.pt'),
    ("pilot seed-0 twin", ART / 'pilot_a1_30m_seed0_twin/'
                                'pilot_a1_30m_seed0_twin.pt'),
    ("pilot seed-1 twin", ART / 'pilot_a1_30m_seed1_twin/'
                                'pilot_a1_30m_seed1_twin.pt'),
    ("10M pilot (A1)", ART / 'pilot-a1-10m-seed0/pilot_a1_10m_seed0.pt'),
    ("10M pilot (pre-A1)", ART / 'pilot-10m-seed0/pilot_10m_seed0.pt'),
]


@torch.no_grad()
def per_turn_spread(model, eps, device):
    """Across-episode spread of the register state after each write of the
    graded forward pass, plus distance travelled from initialization."""
    writes = []
    orig = model._write

    def patched(reg_state, seg_h, rows, _o=orig):
        new = _o(reg_state, seg_h, rows)
        writes.append(new.detach())
        return new

    eps, act = enact_batched(model, list(eps), device, random.Random(0))
    batch = to_torch(E.collate([E.encode_episode(e) for e in eps]), device)
    a = torch.nn.functional.pad(
        act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
    model._write = patched               # capture ONLY the graded pass
    try:
        model.forward(batch, act_inject=a)
    finally:
        model._write = orig

    init = model.reg_init.detach().float().cpu().numpy()
    turns = []
    for i, w in enumerate(writes):
        x = w.reshape(w.shape[0], -1).float().cpu().numpy()
        raw = w.float().cpu().numpy()
        turns.append({
            "turn": i,
            "across_episode_sd_mean": float(x.std(0).mean()),
            "across_episode_sd_max": float(x.std(0).max()),
            "distinct_rows": int(len(np.unique(x, axis=0))),
            "mean_abs_deviation_from_init": float(
                np.abs(raw - init[None, None, :]).mean()),
        })
    return turns, eps


def collapse_turn(turns):
    """First turn whose across-episode spread is under the stated floor,
    and None if the register never collapses within the pass."""
    for t in turns:
        if t["across_episode_sd_mean"] < COLLAPSE_FLOOR:
            return t["turn"]
    return None


def survey_one(label, path, device, n):
    if not path.exists():
        return {"checkpoint": label, "path": str(path),
                "status": "NOT PRESENT LOCALLY"}
    ck = torch.load(path, map_location=device, weights_only=True)
    cfg = Config(**ck["cfg"])
    if not cfg.use_register:
        return {"checkpoint": label, "file": path.name,
                "architecture": "twin (register-less by construction)",
                "status": "SKIPPED — no register to measure"}
    model = MVM0aModel(cfg).to(device).eval()
    try:
        model.load_state_dict(ck["state"])
    except RuntimeError as e:
        # An older checkpoint whose architecture differs from the current
        # module: loading it non-strictly would measure randomly
        # initialized parameters and report the number as if it were the
        # checkpoint's. Skipped and the mismatch recorded instead.
        return {"checkpoint": label, "file": path.name,
                "architecture": "full (register-bearing)",
                "status": "SKIPPED - architecture predates the current "
                          "module and will not load strictly",
                "load_error": str(e).split("\n")[0],
                "note": ("not loaded non-strictly on purpose: that would "
                         "measure random weights and report them as this "
                         "checkpoint's")}
    eps = C.generate_balanced(n, NC.REF_SEED, forced_revision_frac=0.25)
    turns, eps = per_turn_spread(model, eps, device)
    ct = collapse_turn(turns)
    return {
        "checkpoint": label,
        "file": path.name,
        "architecture": "full (register-bearing)",
        "d_model": cfg.d_model, "n_layers": cfg.n_layers,
        "d_reg": cfg.d_reg, "n_agents": cfg.n_agents,
        "training_step": ck.get("step"),
        "n_episodes": n,
        "collapse_turn": ct,
        "constant_after_collapse": ct is not None,
        "per_turn": turns,
    }


@torch.no_grad()
def survey_untrained(device, n, ref_cfg):
    """An UNTRAINED model at the same configuration.

    No intermediate-step weights were saved, so the training-time onset of
    saturation cannot be read off disk. This bounds it from the other end
    instead: if a randomly initialized model already collapses, saturation
    is a property of the architecture present from step 0 rather than
    something training produced. If it does not collapse, training caused
    it. Either answer is informative and neither needs a checkpoint that
    does not exist.
    """
    torch.manual_seed(20260916)
    model = MVM0aModel(ref_cfg).to(device).eval()
    eps = C.generate_balanced(n, NC.REF_SEED, forced_revision_frac=0.25)
    turns, eps = per_turn_spread(model, eps, device)
    ct = collapse_turn(turns)
    return {
        "checkpoint": "UNTRAINED control (same config, random init)",
        "architecture": "full (register-bearing)",
        "training_step": 0,
        "n_episodes": n,
        "collapse_turn": ct,
        "constant_after_collapse": ct is not None,
        "per_turn": turns,
        "why": ("bounds the training-time onset, which cannot be measured "
                "directly because no intermediate weights were saved"),
    }


def run(device: str, n: int) -> dict:
    out = [survey_one(lbl, p, device, n) for lbl, p in CHECKPOINTS]
    ref = next((r for r in out if r.get("architecture", "").startswith("full")),
               None)
    if ref is not None:
        out.append(survey_untrained(
            device, n,
            Config(d_model=ref["d_model"], n_layers=ref["n_layers"],
                   d_reg=ref["d_reg"], n_agents=ref["n_agents"])))
    fulls = [r for r in out if r.get("architecture", "").startswith("full")
             and not str(r["checkpoint"]).startswith("UNTRAINED")
             and "status" not in r]
    collapsed = [r for r in fulls if r.get("constant_after_collapse")]
    return {
        "survey": "register saturation across register-bearing checkpoints",
        "ruled_by": "john, 2026-09-16 Pacific",
        "registered": False,
        "descriptive_only": True,
        "collapse_floor": COLLAPSE_FLOOR,
        "collapse_floor_note": (
            "a stated convention, not an inherited threshold; the raw "
            "per-turn spreads are reported so another boundary can be "
            "applied"),
        "n_register_bearing": len(fulls),
        "n_collapsing": len(collapsed),
        "constant_in_all_register_bearing": len(fulls) > 0
                                            and len(collapsed) == len(fulls),
        "checkpoints": out,
        "intermediate_steps": (
            "No intermediate-step weight checkpoints were saved by any A2 "
            "run; only final weights exist locally, so the TRAINING-time "
            "onset of saturation cannot be measured from what is on disk. "
            "What is measured here is the WITHIN-EPISODE onset, the turn at "
            "which the register stops varying across episodes. An UNTRAINED "
            "control at the same configuration is included to bound the "
            "training-time onset from the other end."),
    }


def self_test() -> None:
    cfg = Config(n_layers=2, d_model=32, n_heads=2, d_reg=16)
    model = MVM0aModel(cfg).eval()
    eps = C.generate_balanced(16, NC.REF_SEED, forced_revision_frac=0.25)
    turns, eps = per_turn_spread(model, eps, "cpu")
    assert turns and "across_episode_sd_mean" in turns[0], "per-turn shape"
    assert collapse_turn([{"turn": 0, "across_episode_sd_mean": 1.0},
                          {"turn": 1, "across_episode_sd_mean": 1e-9}]) == 1
    assert collapse_turn([{"turn": 0, "across_episode_sd_mean": 1.0}]) is None
    print("self-test OK — wiring only, no checkpoint read")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--out", type=Path,
                    default=Path("../a3-gates/register_saturation_survey.json"))
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    res = run(a.device, a.n)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=2))
    print(f"written: {a.out}")


if __name__ == "__main__":
    main()
