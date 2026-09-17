"""Unblinded direct probe of the register — follow-up to the blind arm.

RULED BY JOHN, 2026-09-16 Pacific (decidedBy john), quoted:

  "Before that, one unblinded follow-up on the A2 checkpoint you just ran,
  now that the verdict is committed: probe the register directly at its
  known location for the same four-agent target, same null and same 3 SD
  bar. Pre-state both readings first: decodes above the bar = the blind
  stack missed an existing structure (a sensitivity failure); at chance =
  the register is empty and the arm had no valid target."

THIS MODULE IS DELIBERATELY UNBLINDED. It names register internals on
purpose, so `blind_arm.assert_blind()` would and should fail on it. That
is the point: the blind arm asked what a pipeline finds when it does not
know where to look, and this asks what is there when you do. Running it
cannot contaminate the blind verdict, which was committed first and is
already on the record at `0a1f2c2` with its findings at `5a73f3d`.

WHY IT MATTERS. The blind arm returned NOT FLAGGED in the sub-bin named
"instrument failure to locate": no probe cleared its null by the stated
3 standard deviation bar, best 1.3 sd, accuracy 0.275 against a chance of
0.25 for four agents. That name presumes there was something to locate.
This probe tests the presumption.

WHAT IS PROBED. The register state itself, at its known location: the
final `reg_state`, shape (B, n_agents, d_reg), flattened across all four
agent rows. That is strictly more information than the blind stack was
given, and it is the whole register rather than a chosen part of it.

The own row is NOT probed on its own. Selecting row `own_slot` and then
predicting `own_slot` from it would be circular, since the selection uses
the label.

SAMENESS IS BY CONSTRUCTION, NOT BY COPYING. The probe, the permutation
null, the number of permutations, the cross-validation and the target are
imported from `blind_arm` rather than reimplemented here, so "same null
and same 3 SD bar" cannot drift.

PRE-STATED READINGS (committed before this module produced any output)
----------------------------------------------------------------------
Let `probe` be the accuracy on the flattened final register state and
`null_mean`/`null_sd` its label-permutation null, exactly as in the blind
arm. The bar is the same stated convention: 3 standard deviations.

  READING 1 — SENSITIVITY FAILURE.
  `probe >= null_mean + 3 * null_sd`.
  Own-agent identity IS decodable from the register, and the blind stack
  walked past a structure that was there. The blind arm's sub-bin name
  stands and sharpens: the instrument failed to locate something real, at
  30M. This is the outcome that bears on the stack's sensitivity, and it
  bears on it NEGATIVELY. It is upstream-reportable.

  READING 2 — EMPTY REGISTER, NO VALID TARGET.
  `probe < null_mean + 3 * null_sd`.
  Own-agent identity is NOT decodable from the register even with perfect
  knowledge of where to look. Then the blind arm had no valid target, and
  "failure to locate" mis-describes what happened: there was nothing there
  to locate. On this reading the blind arm says nothing about the stack's
  sensitivity in EITHER direction, and the record must stop claiming it
  does. This also makes the separately ruled positive control the only
  remaining route to a sensitivity reading.

Note which way this cuts, stated before the number is seen: reading 2 is
the one that is *easier* on the instruments and *harder* on the programme,
because it means the constructed self-index was never constructed in any
decodable sense. Neither reading is the comfortable one.

SUPPORTING MEASUREMENT, NO VERDICT ATTACHED. Register occupancy: how far
the final register state moves from its initialization, and how much it
varies across episodes. A register that never moves is empty in the most
literal sense. This is reported as description and no bin turns on it; it
exists so that a reading-2 result can be told apart from a register that
is full but encodes something other than identity.

SECONDARY, ALSO NO VERDICT ATTACHED. The same probe on `reg_repr`, the
projection of the register that the trunk actually reads through
cross-attention. Reported because a register that holds identity the trunk
cannot see is a different situation from one that holds none, but no
pre-stated reading turns on it.

No bin is added after the fact. A result fitting none of these is reported
as fitting none.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
fresh output file, nothing overwritten [C6].

    ../../../.venv/bin/python register_direct_probe.py --self-test
    ../../../.venv/bin/python register_direct_probe.py --ckpt <ckpt> --run
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

# Imported, not redefined, so the null and the bar cannot drift from the
# blind arm's.
from blind_arm import probe, N_PERM

SD_BAR = 3.0        # the same stated convention the blind arm used


@torch.no_grad()
def register_states(model, eps, device):
    """Final register state and final trunk-visible register projection.

    Captured by wrapping the model's own register write and projection, so
    what is read is exactly what the model computed, not a reconstruction.
    """
    if not model.cfg.use_register:
        raise SystemExit("this checkpoint is register-less (a twin); the "
                         "direct probe has no object on it.")

    writes, reprs = [], []
    orig_write, orig_repr = model._write, model._reg_repr

    def patched_write(reg_state, seg_h, rows, _o=orig_write):
        new = _o(reg_state, seg_h, rows)
        writes.append(new.detach())
        return new

    def patched_repr(reg_state, register_keys, _o=orig_repr):
        out = _o(reg_state, register_keys)
        reprs.append(out.detach())
        return out

    model._write, model._reg_repr = patched_write, patched_repr
    try:
        eps, act = enact_batched(model, list(eps), device, random.Random(0))
        batch = to_torch(E.collate([E.encode_episode(e) for e in eps]),
                         device)
        a = torch.nn.functional.pad(
            act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
        model.forward(batch, act_inject=a)
    finally:
        model._write, model._reg_repr = orig_write, orig_repr

    if not writes:
        raise SystemExit("no register write was captured — the run did not "
                         "exercise the register at all.")

    final_state = writes[-1]                       # (B, n_agents, d_reg)
    final_repr = reprs[-1]                         # (B, n_agents, d_model)
    B = final_state.shape[0]
    init = model.reg_init.detach()
    return {
        "state": final_state.reshape(B, -1).float().cpu().numpy(),
        "repr": final_repr.reshape(B, -1).float().cpu().numpy(),
        "raw_state": final_state.float().cpu().numpy(),
        "init": init.float().cpu().numpy(),
    }, eps


def occupancy(raw_state, init):
    """Descriptive only: does the register move at all, and does it differ
    across episodes? No pre-stated reading turns on these numbers."""
    dev = np.abs(raw_state - init[None, None, :])
    across = raw_state.std(axis=0)                 # (n_agents, d_reg)
    return {
        "mean_abs_deviation_from_init": round(float(dev.mean()), 6),
        "max_abs_deviation_from_init": round(float(dev.max()), 6),
        "mean_across_episode_sd": round(float(across.mean()), 6),
        "max_across_episode_sd": round(float(across.max()), 6),
        "note": ("a register that never leaves its initialization, or that "
                 "is identical across episodes, is empty in the most "
                 "literal sense"),
    }


def read_verdict(p) -> dict:
    """Apply the pre-stated readings. Nothing here inspects the number
    before deciding what the bins are — the bins are fixed above."""
    bar = p["null_mean"] + SD_BAR * p["null_sd"]
    clears = p["accuracy"] >= bar
    return {
        "bar": round(float(bar), 4),
        "clears_bar": bool(clears),
        "reading": "1 — SENSITIVITY FAILURE" if clears
                   else "2 — EMPTY REGISTER, NO VALID TARGET",
        "means": (
            "Own-agent identity IS decodable from the register. The blind "
            "stack walked past a structure that was there; its 'instrument "
            "failure to locate' sub-bin stands and sharpens into a "
            "sensitivity failure at 30M. Upstream-reportable."
            if clears else
            "Own-agent identity is NOT decodable from the register even "
            "knowing exactly where to look. The blind arm therefore had no "
            "valid target, 'failure to locate' mis-describes it, and the "
            "blind result says nothing about the stack's sensitivity in "
            "either direction. The ruled positive control becomes the only "
            "remaining route to a sensitivity reading."),
    }


def run(ckpt: Path, device: str, n: int = 400) -> dict:
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    eps = C.generate_balanced(n, NC.REF_SEED, forced_revision_frac=0.25)
    acts, eps = register_states(model, eps, device)
    y = [e.own_slot for e in eps]

    p_state = probe(acts["state"], y, seed=0)
    p_repr = probe(acts["repr"], y, seed=1)

    return {
        "arm": "UNBLINDED direct register probe (follow-up to the blind arm)",
        "registered": False,
        "ruled_by": "john, 2026-09-16 Pacific",
        "checkpoint": ckpt.name,
        "blinded": False,
        "blind_verdict_committed_first": "0a1f2c2 (findings), 401a54d/da0427f (criteria)",
        "target": "own_slot (which of four agents the model is)",
        "n_episodes": n,
        "n_permutations": N_PERM,
        "sd_bar": SD_BAR,
        "primary_probe_on_register_state": p_state,
        "verdict": read_verdict(p_state),
        "secondary_probe_on_trunk_visible_repr": p_repr,
        "secondary_note": ("descriptive only; no pre-stated reading turns "
                           "on this number"),
        "occupancy": occupancy(acts["raw_state"], acts["init"]),
    }


def self_test() -> None:
    """Shape and wiring check on an untrained model. Asserts nothing about
    any number, so it cannot leak a result."""
    cfg = Config(n_layers=2, d_model=32, n_heads=2, d_reg=16)
    model = MVM0aModel(cfg).eval()
    eps = C.generate_balanced(16, NC.REF_SEED, forced_revision_frac=0.25)
    acts, eps = register_states(model, eps, "cpu")
    assert acts["state"].shape[0] == len(eps), "one row per episode"
    assert acts["state"].shape[1] == cfg.n_agents * cfg.d_reg, "flattened"
    assert len({e.own_slot for e in eps}) > 1, "target must vary"
    occ = occupancy(acts["raw_state"], acts["init"])
    assert set(occ) >= {"mean_abs_deviation_from_init"}, "occupancy keys"
    v = read_verdict({"accuracy": 0.9, "null_mean": 0.25, "null_sd": 0.02})
    assert v["clears_bar"] and v["reading"].startswith("1"), "bin 1 wiring"
    v = read_verdict({"accuracy": 0.26, "null_mean": 0.25, "null_sd": 0.02})
    assert not v["clears_bar"] and v["reading"].startswith("2"), "bin 2"
    print("self-test OK — wiring only, no result inspected")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", type=Path)
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--self-test", dest="self_test",
                    action="store_true")
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n", type=int, default=400)
    ap.add_argument("--out", type=Path,
                    default=Path("../a3-gates/register_direct_probe.json"))
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    if a.out.exists():
        raise SystemExit(f"{a.out} exists; refusing to overwrite [C6]")
    res = run(a.ckpt, a.device, a.n)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=2))
    print(f"written: {a.out}")


if __name__ == "__main__":
    main()
