"""Known-answer test for the localization pipeline.

RULED BY JOHN, 2026-09-16 Pacific (decidedBy john), quoted:

  "Known-answer test, criteria pre-stated and committed first: same
  pipeline, same null construction, target = the acting-channel input
  value, read at the first layer at the position where it is present.
  Expected near-ceiling. Pass = the pipeline works and tonight's failure
  is about the stack at this scale. Fail = implementation bug; find it,
  report it, fix nothing silently. Precondition as before: non-degenerate
  null."

  And: "no A3 L1 localization read on any seed until the known-answer
  test passes. The L0 direct lesion is unaffected and proceeds as
  registered."

WHY. Tonight the blind pipeline returned five probes BELOW their own
permutation nulls on a checkpoint where ownership is measured to be
load-bearing. Two explanations fit that: a localization stack that is
insensitive at this scale, and a pipeline with a bug in it. Nothing run
so far separates them. This does.

THE TEST IS MEANT TO BE EASY, and that is the point. The enacted value
token sits at the probed position, so a working pipeline must decode it
at or near ceiling. Failing a question this easy means the fault is in the
plumbing — residual capture, position indexing, probe fitting, or null
construction — not in what the model does or does not carry.

WHAT IS PROBED. The first layer's output, at the position where the
acting channel is injected, which is the model's own enacted value
position. The target is the enacted value token there, one of eight
slots, so chance is 0.125.

SAMENESS BY CONSTRUCTION. The probe, the label-permutation null, the
permutation count and the cross-validation are imported from the same
modules the blind pipeline uses, not reimplemented, so "same pipeline,
same null construction" cannot drift.

PRE-STATED CRITERIA (committed before this module produced any output)
----------------------------------------------------------------------
  PRECONDITION, as with the previous two runs: the permutation null must
  be non-degenerate. Zero null spread, an undefined margin, or accuracy
  exactly equal to the majority-class rate means NO verdict is assigned
  and the run reports DEGENERATE.

  PASS.  accuracy >= 0.95 AND the null is non-degenerate AND the probe
         clears null_mean + 3*null_sd.
    Reads: the pipeline works end to end. Tonight's failure to find
    ownership structure is then about the localization stack at this
    scale, not about the code.

  FAIL.  accuracy < 0.95 with a non-degenerate null.
    Reads: IMPLEMENTATION BUG. The pipeline cannot recover a value that is
    present at the probed position. On this outcome the rule is John's:
    find it, report it, FIX NOTHING SILENTLY. Any fix is proposed, not
    applied, and every result that used the broken pipeline is flagged.

The 0.95 bar is a STATED CONVENTION and mine, not inherited from any
registration. It is set near ceiling because the target is present in the
input at the probed position and anything well below ceiling is a defect.
The raw accuracy is reported so a different bar can be applied.

A DIAGNOSTIC WITH NO BIN ATTACHED, so that a pass is not over-read: the
same probe on a forward pass with the acting channel ZEROED. If the target
is decodable either way, the pass shows the plumbing works and says
nothing about the acting channel specifically. That distinction matters
for how a pass is described, and no criterion turns on it.

No bin is added after the fact. A result fitting none of these is reported
as fitting none.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
fresh output file, nothing overwritten.

    ../../../.venv/bin/python known_answer_test_a3.py --self-test
    ../../../.venv/bin/python known_answer_test_a3.py --ckpt <ckpt> --run
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import numpy as np
import torch

import curriculum_a3 as A
import encoding_a3 as E
import train_a3 as T
from model import MVM0aModel, Config, to_torch

# imported, never reimplemented, so the null construction cannot drift
from localize_a3 import fit_probe, N_PERM

FIRST_LAYER = 0
SD_BAR = 3.0
PASS_BAR = 0.95          # stated convention, mine, near ceiling
CHANCE = 1.0 / len(A.SLOTS)


@torch.no_grad()
def first_layer_at_act(model, eps, device, zero_act=False):
    """First-layer output at the acting-channel injection position, with
    the enacted value token there as the target."""
    eps, act = T.enact_batched(model, list(eps), device, random.Random(0))
    batch = to_torch(E.collate([E.encode_episode(e) for e in eps]), device)
    a = torch.nn.functional.pad(
        act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
    if zero_act:
        a = torch.zeros_like(a)

    cap = []
    blk = model.blocks[FIRST_LAYER]
    orig = blk.forward

    def patched(x, kv, rr, _o=orig):
        x, ctx = _o(x, kv, rr)
        cap.append(x.detach())
        return x, ctx

    blk.forward = patched
    try:
        model.forward(batch, act_inject=a)
    finally:
        del model.blocks[FIRST_LAYER].__dict__["forward"]

    h = torch.cat(cap, dim=1)
    p = batch["act_pos"]
    keep = (p >= 0).nonzero().flatten()
    if keep.numel() == 0:
        raise SystemExit("no episode carried an own revision; nothing to "
                         "probe at the acting position")
    pk = p[keep]
    X = h[keep, pk].float().cpu().numpy()
    y = batch["input_ids"][keep, pk].cpu().numpy().tolist()
    return X, y


def degenerate(p, majority_rate):
    bad = []
    if p["null_sd"] == 0:
        bad.append("the label-permutation null has zero spread; the 3-sd "
                   "comparison would compare a number to itself")
    if p.get("margin_sd") is None:
        bad.append("margin in standard deviations is undefined")
    if abs(p["accuracy"] - majority_rate) < 1e-9:
        bad.append("accuracy equals the majority-class rate exactly, the "
                   "score of a constant classifier")
    return bad


def verdict(p, majority_rate):
    bad = degenerate(p, majority_rate)
    if bad:
        return {"verdict": "DEGENERATE — no bin assigned",
                "degeneracy": bad}
    clears = p["accuracy"] >= p["null_mean"] + SD_BAR * p["null_sd"]
    if p["accuracy"] >= PASS_BAR and clears:
        return {"verdict": "PASS", "clears_null_3sd": True,
                "means": ("the pipeline recovers a value present at the "
                          "probed position, so residual capture, position "
                          "indexing, probe fitting and null construction "
                          "all work. Tonight's failure to find ownership "
                          "structure is about the localization stack at "
                          "this scale, not about the code.")}
    return {"verdict": "FAIL — IMPLEMENTATION BUG", "clears_null_3sd": clears,
            "means": ("the pipeline cannot recover a value that is present "
                      "at the probed position. Per John's ruling: find it, "
                      "report it, FIX NOTHING SILENTLY. Any fix is proposed "
                      "rather than applied, and every result produced with "
                      "this pipeline is flagged."),
            "gate": ("no A3 L1 localization read on any seed until this "
                     "passes; the L0 direct lesion is unaffected")}


def run(ckpt: Path, device: str, n: int) -> dict:
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    eps = A.generate_balanced(n, T.HELDOUT_SEED)
    X, y = first_layer_at_act(model, eps, device)
    counts = {int(c): y.count(c) for c in sorted(set(y))}
    majority = max(counts.values()) / len(y)
    p = fit_probe(X, y, seed=0)

    eps2 = A.generate_balanced(n, T.HELDOUT_SEED)
    Xz, yz = first_layer_at_act(model, eps2, device, zero_act=True)
    pz = fit_probe(Xz, yz, seed=1)

    return {
        "test": "known-answer test of the localization pipeline",
        "ruled_by": "john, 2026-09-16 Pacific",
        "registered": False,
        "checkpoint": ckpt.name,
        "probe_layer": FIRST_LAYER,
        "position": "acting-channel injection position (own enacted value)",
        "target": "the enacted value token there",
        "n_classes": len(A.SLOTS),
        "chance": round(CHANCE, 4),
        "pass_bar": PASS_BAR,
        "pass_bar_note": ("a stated convention, mine, not inherited from "
                          "any registration; raw accuracy reported so any "
                          "bar can be applied"),
        "n_probed": len(y),
        "label_counts": counts,
        "majority_class_rate": round(majority, 4),
        "probe": p,
        "verdict": verdict(p, majority),
        "diagnostic_acting_channel_zeroed": pz,
        "diagnostic_note": ("no bin turns on this. If the target decodes "
                            "either way, a pass shows the plumbing works "
                            "and says nothing about the acting channel "
                            "specifically."),
    }


def self_test() -> None:
    ok = {"accuracy": 0.99, "null_mean": 0.125, "null_sd": 0.02,
          "margin_sd": 43.2}
    bad = {"accuracy": 0.30, "null_mean": 0.125, "null_sd": 0.02,
           "margin_sd": 8.7}
    deg = {"accuracy": 0.2, "null_mean": 0.2, "null_sd": 0.0,
           "margin_sd": None}
    assert verdict(ok, 0.2)["verdict"] == "PASS"
    assert verdict(bad, 0.2)["verdict"].startswith("FAIL")
    assert verdict(deg, 0.2)["verdict"].startswith("DEGENERATE")
    # clearing the null is not enough on its own: the bar is near ceiling
    assert verdict(bad, 0.2)["clears_null_3sd"] is True, (
        "a probe well above its null but far below ceiling must still FAIL")
    print("self-test OK — three bins and the near-ceiling bar; no result "
          "inspected")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", type=Path)
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n", type=int, default=400)
    ap.add_argument("--out", type=Path,
                    default=Path("../a3-gates/known_answer_test_a3.json"))
    a = ap.parse_args()
    if not a.run:
        self_test()
        return
    if a.out.exists():
        raise SystemExit(f"{a.out} exists; refusing to overwrite")
    res = run(a.ckpt, a.device, a.n)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, indent=2))
    print(f"written: {a.out}")


if __name__ == "__main__":
    main()
