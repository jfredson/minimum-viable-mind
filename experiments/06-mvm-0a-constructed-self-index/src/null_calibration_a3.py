"""The θ/δ null calibration for Amendment A3, with the corrected metric.

`null_calibration.py` is the Gate 0 script and is left untouched: its
records are the registered noise floor for the five existing checkpoints
and they must keep reproducing. This is its A3 sibling. Two things differ,
both ruled by John on 2026-09-15.

**The drop is corrected against the measured shortcut ceiling, not against
chance** (revision proposal, decision 3). The registered metric divided by
the distance from baseline to chance. That was right while guessing was
the only floor. It stopped being right once the batteries acquired
shortcut ceilings, because a lesion that removes ownership cannot push a
battery below its ceiling — an ownership-blind solver still scores that
much — so dividing by baseline-minus-chance divides by a range the
battery cannot traverse.

The damage was that the error differed per battery. With ceilings of
0.2921 and 0.3227 the two verdict batteries could show at most 0.809 and
0.774, so a lesion of a purely generic binder, which hits both equally in
real terms, still reported a differential of 0.035 against a band near
0.01. The bin meant to catch the boring explanation could not fire and the
bin meant to find a self-index fired on it.

So:

    d(B) = (B_base − B_abl) / (B_base − ceiling_B)

**A drop past 1.0 is reported, never clipped.** It means the ablation took
the battery below what an ownership-blind solver achieves, so the lesion
removed more than ownership. That is worth seeing, and hiding it inside a
clamp would turn the most interesting failure into a quiet 1.0.

The ceiling is a measured quantity (`curriculum_a3.measured_ceilings`,
verified by `shortcut_sweep.py`), so it carries its own error. Measured
over thousands of episodes it is tight against the effects involved, and
every record here stores the ceiling it used.

Everything else is carried over from the Gate 0 script verbatim: the
operators, the layer list, the ranks, the seed count, the quantile, the
floor rule, and the whole-eval-under-ablation discipline.

Corrigibility: inference only, local checkpoints, $0 [C1/C2]; results go
to fresh per-checkpoint JSON, never over an existing record [C6].

    ../../../.venv/bin/python null_calibration_a3.py --self-test
    ../../../.venv/bin/python null_calibration_a3.py --ckpt <path> \
        --out ../null-calibration/a3_<name>.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F

import curriculum_a3 as A
import encoding_a3 as E
import null_calibration as NC0
import train_a3 as T
from model import MVM0aModel, Config, SCALES, to_torch

EVAL_N = 800                      # 400 verdict cells at half density
REF_SEED = NC0.REF_SEED
REF_N = NC0.REF_N
ABLATE_LAYERS = NC0.ABLATE_LAYERS
NULL_KS = NC0.NULL_KS
N_SEEDS = NC0.N_SEEDS
QUANTILE = NC0.QUANTILE
FLOOR_MARGIN = NC0.FLOOR_MARGIN
K0_BAND = 0.25                    # pre-stated; kept unchanged after Gate 0
VERDICT_BATTERIES = ("T_act", "T_other")
DIFF_PAIRS = (("T_act", "T_other"), ("T_act", "T_state"),
              ("T_other", "T_state"))
RESIDUAL_OPS = NC0.RESIDUAL_OPS


def ceilings() -> dict[str, float]:
    """The measured shortcut ceilings that form the metric's denominator.
    T_state and T_syntax have no ownership shortcut, so their floor is
    chance and the correction reduces to the registered one."""
    m = A.measured_ceilings()
    out = {"T_act": m["T_act"], "T_other": m["T_other"]}
    eps = A.generate_balanced(2000, 4242)
    acc: dict[str, list] = {b: [] for b in A.BATTERIES}
    for e in eps:
        for q in e.queries:
            acc[q.battery].append(1.0 / q.n_choices)
    for b in ("T_state", "T_syntax"):
        out[b] = float(np.mean(acc[b]))
    return out


def d_metric(base: dict, abl: dict, ceil: dict) -> dict:
    """Ceiling-corrected drop. NOT clipped at 1.0: a value above one means
    the ablation took the battery below what an ownership-blind solver
    reaches, which is a real and interesting outcome."""
    out = {}
    for b in base:
        den = base[b] - ceil[b]
        out[b] = None if den < FLOOR_MARGIN else round(
            (base[b] - abl[b]) / den, 4)
    return out


def run(ckpt: Path, device: str, n: int, n_seeds: int, ks: list[int],
        out: Path | None) -> dict:
    t0 = time.time()
    md5 = hashlib.md5(ckpt.read_bytes()).hexdigest()

    def loader():
        ck = torch.load(ckpt, map_location=device, weights_only=True)
        m = MVM0aModel(Config(**ck["cfg"])).to(device)
        m.load_state_dict(ck["state"])
        return m.eval()

    ceil = ceilings()
    model = loader()
    base = T.eval_heldout(model, device, n=n)
    print(f"baseline {base}", flush=True)
    ref, reg_rms = NC0.collect_reference(model, device, REF_N, REF_SEED)
    floor = {b: base[b] - ceil[b] < FLOOR_MARGIN for b in base}
    draws = []
    record = {
        "gate": "A3 θ/δ null calibration (ceiling-corrected metric)",
        "checkpoint": ckpt.name, "checkpoint_md5": md5, "device": device,
        "metric": "d(B) = (base - abl) / (base - CEILING_B); not clipped "
                  "at 1.0 (John, 2026-09-15, revision proposal decision 3)",
        "ceilings_used": ceil,
        "eval": {"harness": "train_a3.eval_heldout", "n": n},
        "pre_commitments": {"ablate_layers": ABLATE_LAYERS, "ks": ks,
                            "n_seeds": n_seeds, "quantile": QUANTILE,
                            "floor_margin": FLOOR_MARGIN,
                            "k0_band": K0_BAND,
                            "verdict_batteries": VERDICT_BATTERIES},
        "baseline": base, "floor": floor, "draws": draws,
    }

    grid = [(op, k, s) for op in RESIDUAL_OPS for k in ks
            for s in range(n_seeds)]
    for i, (op, k, s) in enumerate(grid):
        model = loader()
        strength = NC0.install_residual(model, op, s, k, ref, device)
        acc = T.eval_heldout(model, device, n=n)
        draws.append({"op": op, "k": k, "seed": s, "acc": acc,
                      "d": d_metric(base, acc, ceil),
                      "strength": strength})
        print(f"{i+1}/{len(grid)} {op} k={k} seed={s} d={draws[-1]['d']}",
              flush=True)
        if out and (i + 1) % 10 == 0:
            out.with_suffix(".partial.json").write_text(
                json.dumps(record, indent=1))

    record["summary"] = summarize(record)
    record["elapsed_sec"] = round(time.time() - t0, 1)
    if out:
        assert not out.exists(), f"refusing to overwrite {out} [C6]"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(record, indent=1))
        p = out.with_suffix(".partial.json")
        p.exists() and p.unlink()
    return record


def summarize(rec: dict) -> dict:
    draws = rec["draws"]
    s: dict = {"theta": {}, "delta": {}}
    for b in rec["baseline"]:
        if rec["floor"][b]:
            s["theta"][b] = {"floor": True}
            continue
        ds = [x["d"][b] for x in draws if x["d"][b] is not None]
        s["theta"][b] = {
            "floor": False, "n_draws": len(ds),
            "p95_abs_d": NC0._pct([abs(v) for v in ds], QUANTILE),
            "max_abs_d": round(max(abs(v) for v in ds), 4) if ds else None,
            "exceeds_one": sum(1 for v in ds if v > 1.0),
        }
    for b1, b2 in DIFF_PAIRS:
        if rec["floor"].get(b1) or rec["floor"].get(b2):
            s["delta"][f"{b1}-{b2}"] = {"floor": True}
            continue
        dd = [abs(x["d"][b1] - x["d"][b2]) for x in draws
              if x["d"][b1] is not None and x["d"][b2] is not None]
        s["delta"][f"{b1}-{b2}"] = {
            "floor": False, "p95_abs_diff": NC0._pct(dd, QUANTILE)}
    k0 = {}
    for b in VERDICT_BATTERIES:
        th = s["theta"][b]
        k0[b] = None if th["floor"] else {
            "p95_abs_d": th["p95_abs_d"],
            "reaches_band": th["p95_abs_d"] >= K0_BAND}
    s["k0_check"] = {
        "band": K0_BAND, "verdict_batteries": k0,
        "note": "0.25 is the PRE-STATED figure and is deliberately "
                "unchanged after Gate 0 measured the band at about 0.01; "
                "moving it either way now would be fitting the rule to "
                "the data. Read only on batteries above the floor margin."}
    return s


def self_test() -> None:
    ceil = {"T_act": 0.2921, "T_other": 0.3227, "T_state": 0.09,
            "T_syntax": 0.083}
    base = {b: 1.0 for b in ceil}
    # a lesion that collapses each battery to its OWN ceiling now reads as
    # exactly 1.0 on both, so a purely generic binder gives no differential
    abl = dict(ceil)
    d = d_metric(base, abl, ceil)
    assert abs(d["T_act"] - 1.0) < 1e-9 and abs(d["T_other"] - 1.0) < 1e-9
    assert abs(d["T_act"] - d["T_other"]) < 1e-9, \
        "unequal ceilings must no longer manufacture a differential"
    # under the OLD chance-corrected metric the same lesion did
    old = {b: (base[b] - abl[b]) / (base[b] - 0.125) for b in ceil}
    assert abs(old["T_act"] - old["T_other"]) > 0.03, \
        "the defect this metric fixes should be visible in the old one"
    # a drop past the ceiling exceeds 1.0 and is NOT clipped
    deep = d_metric(base, {b: 0.125 for b in ceil}, ceil)
    assert deep["T_act"] > 1.0, "a drop past the ceiling must be reported"
    # the floor rule still suppresses d on an unlearned battery
    assert d_metric({"T_act": 0.30}, {"T_act": 0.20},
                    {"T_act": 0.2921})["T_act"] is None
    print(f"null_calibration_a3 self-test OK (generic-binder differential: "
          f"old {abs(old['T_act']-old['T_other']):.4f}, new 0.0000)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--ckpt", default=None)
    ap.add_argument("--n", type=int, default=EVAL_N)
    ap.add_argument("--seeds", type=int, default=N_SEEDS)
    ap.add_argument("--ks", default=",".join(map(str, NULL_KS)))
    ap.add_argument("--device", default="mps" if
                    torch.backends.mps.is_available() else "cpu")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    assert args.ckpt, "--ckpt required"
    rec = run(Path(args.ckpt).resolve(), args.device, args.n, args.seeds,
              [int(k) for k in args.ks.split(",") if k],
              Path(args.out) if args.out else None)
    print(json.dumps(rec["summary"], indent=1))


if __name__ == "__main__":
    main()
