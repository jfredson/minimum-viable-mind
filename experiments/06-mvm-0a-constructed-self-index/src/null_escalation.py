"""Gate 0 instrument-validity check — does the null operator have teeth?

Not part of the registered band. Gate 0's band (`null_calibration.py`) is
the pre-committed quantile of the chance-corrected drop under ablations
that carry no information about any structure. A band of zero has two
readings, and the record must say which one it is:

  (a) the trained network is robust to removing a random 3-5% of its
      residual-stream norm, so a real lesion that moves a battery is
      moving it for a reason; or
  (b) the operator is too weak to move anything at all, in which case a
      zero band is an artifact of the instrument and licenses nothing.

Thread 4 made the same move before trusting its null: it verified the
register pathway was numerically live (logit shifts, residual norms)
rather than reporting "no effect" from a dead wire. This script is that
verification for the residual operator.

Method: the same `rand-mean` and `rand-noise` operators at the same
layers, escalated past the registered rank cap — rank k ∈ {16, 32, 64,
128, 256, 448} for mean-ablation (448 = d_model, the whole residual
pinned to its reference mean), and noise at multiples {1, 4, 16, 64} of
the rank-16 matched strength. Three seeds per condition, n=200 episodes
(half the verdict n; this is a dose-response curve, not a verdict cell).
The reported curve is battery accuracy against the fraction of residual
norm perturbed, with the registered k≤16 conditions marked on it.

**Why this does not touch RT-10's lock clause.** Every ablation here is
a random subspace or isotropic noise: content-blind, carrying no
information about the register, the acting channel, or any candidate
self-index, and selecting nothing. Amendment A3 §4.1's Lock row
explicitly permits a dry-run "on random subspaces only" before the lock.
No designated structure is localized, ablated, or read.

Corrigibility: inference only, local checkpoints, $0 [C1/C2]; fresh
output file, no record overwritten [C6].

    ../../../.venv/bin/python null_escalation.py --self-test
    ../../../.venv/bin/python null_escalation.py --ckpt <path> \
        --out ../null-calibration/escalation_<name>.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import torch

import null_calibration as NC
from model import MVM0aModel
from train import eval_heldout
from lesion_register import load_checkpoint, HELDOUT_SEED

ESC_N = 200
ESC_SEEDS = 3
MEAN_KS = [16, 32, 64, 128, 256, 448]     # 448 = d_model (whole residual)
NOISE_MULTS = [1, 4, 16, 64]              # × the rank-16 matched strength
BATTERIES = NC.BATTERIES


def residual_norms(ref: dict[int, torch.Tensor]) -> dict[str, float]:
    """RMS residual norm, and RMS of the mean-centred residual, per layer
    — the denominators the escalation curve is read against."""
    out = {}
    for L, h in ref.items():
        raw = float((h ** 2).sum(-1).mean().sqrt())
        cen = float(((h - h.mean(0)) ** 2).sum(-1).mean().sqrt())
        out[str(L)] = {"rms_norm": round(raw, 2),
                       "rms_centred_norm": round(cen, 2)}
    return out


def install_scaled_noise(model: MVM0aModel, seed: int, mult: float,
                         base_strength: dict[str, float]) -> dict:
    """rand-noise at `mult` × the per-layer rank-16 matched strength."""
    rec = {}
    for L in NC.ABLATE_LAYERS:
        s = base_strength[str(L)] * mult
        rec[str(L)] = {"strength": s, "mult": mult}
        blk = model.blocks[L]
        orig = blk.forward
        gen = torch.Generator().manual_seed(seed * 100_003 + L)

        def patched(x, kv, reg_repr, _o=orig, _s=s, _g=gen):
            x, ctx = _o(x, kv, reg_repr)
            nz = torch.randn(x.shape, generator=_g).to(x.device)
            nz = nz / nz.norm(dim=-1, keepdim=True).clamp_min(1e-6) * _s
            return x + nz, ctx
        blk.forward = patched
    return rec


def run(ckpt: Path, device: str, n: int, out: Path | None) -> dict:
    t0 = time.time()
    md5 = hashlib.md5(ckpt.read_bytes()).hexdigest()
    load = lambda: load_checkpoint(ckpt, device)[0]           # noqa: E731
    model = load()
    chance = NC.chance_floors(n, HELDOUT_SEED)
    base = eval_heldout(model, device, n=n, seed=HELDOUT_SEED)
    print(f"baseline {base}", flush=True)
    ref, _ = NC.collect_reference(model, device, NC.REF_N, NC.REF_SEED)
    norms = residual_norms(ref)
    # per-layer rank-16 matched strength, the noise ladder's unit
    rec16 = NC.install_residual(load(), "rand-mean", 0, 16, ref, device)
    unit = {L: v["rms_removed_norm"] for L, v in rec16.items()}

    rows = []
    record = {
        "check": "Gate 0 instrument validity — strength escalation on "
                 "random subspaces (NOT part of the registered band)",
        "checkpoint": ckpt.name, "checkpoint_md5": md5, "device": device,
        "arch": "full" if model.cfg.use_register else "twin",
        "eval": {"harness": "train.eval_heldout", "n": n,
                 "seed": HELDOUT_SEED},
        "d_model": model.cfg.d_model,
        "registered_rank_cap": 16,
        "residual_norms": norms, "rank16_unit_strength": unit,
        "chance": chance, "baseline": base, "rows": rows,
    }

    def save(final: bool) -> None:
        if out is None:
            return
        target = out if final else out.with_suffix(".partial.json")
        target.parent.mkdir(parents=True, exist_ok=True)
        if final:
            assert not out.exists(), f"refusing to overwrite {out} [C6]"
        target.write_text(json.dumps(record, indent=1))
        if final and out.with_suffix(".partial.json").exists():
            out.with_suffix(".partial.json").unlink()

    grid = ([("rand-mean", k, None) for k in MEAN_KS]
            + [("rand-noise", 16, m) for m in NOISE_MULTS])
    for op, k, mult in grid:
        for s in range(ESC_SEEDS):
            model = load()
            if mult is None:
                st = NC.install_residual(model, op, s, k, ref, device)
                strength = {L: v["rms_removed_norm"] for L, v in st.items()}
            else:
                st = install_scaled_noise(model, s, mult, unit)
                strength = {L: v["strength"] for L, v in st.items()}
            acc = eval_heldout(model, device, n=n, seed=HELDOUT_SEED)
            frac = {L: round(strength[L] / norms[L]["rms_norm"], 4)
                    for L in strength}
            frac_c = {L: round(strength[L] / norms[L]["rms_centred_norm"], 4)
                      for L in strength}
            rows.append({"op": op, "k": k, "mult": mult, "seed": s,
                         "acc": acc,
                         "d": NC.d_metric(base, acc, chance),
                         "frac_of_rms_norm": frac,
                         "frac_of_centred_norm": frac_c})
            print(f"{op} k={k} mult={mult} seed={s} acc={acc} "
                  f"norm_frac~{list(frac.values())[0]}", flush=True)
        save(final=False)
    record["elapsed_sec"] = round(time.time() - t0, 1)
    save(final=True)
    return record


def self_test() -> None:
    from model import Config
    import curriculum as C
    import encoding as E
    from model import to_torch
    cfg = Config(d_model=64, n_layers=max(NC.ABLATE_LAYERS) + 1, n_heads=2)
    torch.manual_seed(0)
    m = MVM0aModel(cfg).eval()
    eps = [C.generate_episode(s) for s in range(4)]
    batch = to_torch(E.collate([E.encode_episode(e, query=e.queries[0])
                                for e in eps]))
    with torch.no_grad():
        base = m(batch)
        ref, _ = NC.collect_reference(m, "cpu", 4, 1)
        norms = residual_norms(ref)
        assert all(v["rms_centred_norm"] <= v["rms_norm"] + 1e-3
                   for v in norms.values())
        unit = {L: v["rms_removed_norm"] for L, v in
                NC.install_residual(MVM0aModel(cfg).eval(), "rand-mean", 0,
                                    4, ref, "cpu").items()}
        # bigger multiplier => bigger deviation from baseline
        devs = []
        for mult in (1, 64):
            torch.manual_seed(0)
            m2 = MVM0aModel(cfg).eval()
            install_scaled_noise(m2, 0, mult, unit)
            devs.append(float((m2(batch) - base).abs().mean()))
        assert devs[1] > devs[0] > 0, devs
        # full-rank mean ablation pins the residual: output must change a lot
        torch.manual_seed(0)
        m3 = MVM0aModel(cfg).eval()
        NC.install_residual(m3, "rand-mean", 0, cfg.d_model, ref, "cpu")
        assert float((m3(batch) - base).abs().mean()) > 0
        # class untouched
        torch.manual_seed(0)
        assert torch.allclose(MVM0aModel(cfg).eval()(batch), base, atol=1e-5)
    print("null_escalation self-test OK")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--ckpt", default=None)
    ap.add_argument("--n", type=int, default=ESC_N)
    ap.add_argument("--device", default="mps" if
                    torch.backends.mps.is_available() else "cpu")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    assert args.ckpt, "--ckpt required"
    out = Path(args.out) if args.out else None
    if out is not None:
        assert not out.exists(), f"refusing to overwrite {out} [C6]"
    run(Path(args.ckpt).resolve(), args.device, args.n, out)
    if out is not None:
        print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
