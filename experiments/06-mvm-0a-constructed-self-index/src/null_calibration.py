"""Gate 0 — the registered θ/δ null calibration for MVM-0a.

Registered in `pre-registration.md` §"Pre-registered metric and decision
rule": "θ_task and δ are null-calibrated on the registered model —
pre-committed quantiles of d over matched-strength random-subspace and
matched-norm ablations, computed by a script committed before it runs."
Ordered first by John (2026-08-30) and by Amendment A3 §4.1 (Gate 0) /
§4.2 (kill K0). This file IS that script. Every number below is a
pre-commitment; the script selects nothing after seeing a result.

What it measures
----------------
For each of the five existing 30M checkpoints, the distribution of the
chance-corrected drop d(B) = (B_base − B_abl) / (B_base − chance_B) on
every battery under ablations that carry no information about any
particular structure, so that a real lesion's d can be read against the
band such ablations produce. The whole registered held-out eval
(`train.eval_heldout`, seed 987654321, n=400 — the same eval and n the
thread-3 item sweep used) runs under each ablation, enactment forwards
and acting-channel injections included, exactly as thread 4 did.

Ablation operators (the "matched-strength random-subspace and
matched-norm" pair the registration names)
----------------------------------------
Residual-stream operators, applied at ALL positions at the outputs of
blocks {3, 4, 5, 7, 8} of 12 — Experiment 1's registered layer list
[8, 11, 14, 18, 22] of 32 rescaled by depth fraction with
`mvm.config.scale_layers`' rounding (round(l·12/32), clamped to
[1, n−2]). Applied to full AND twin checkpoints, since Amendment A3's
lesion target L1 is a residual-stream subspace and its control L2b is
"random subspaces of matched rank and norm".

- **random-subspace mean-ablation** (`rand-mean`): per layer a random
  rank-k orthonormal basis (numpy default_rng, one rng per (seed, k),
  per-layer draws consumed in layer order, QR-orthonormalized); every
  basis coordinate pinned to its reference mean, h ← h + (μ − h·D)·D
  (Experiment 1's `ablation_hooks` mode "mean", verbatim semantics).
  Reference means: the intact checkpoint's own activations at that
  layer over a reference set of 100 held-out episodes under seed
  20260914 (disjoint from the eval seed), enacted by the intact model,
  all non-pad positions, no query segment.
- **matched-norm noise** (`rand-noise`): at every position add a random
  Gaussian direction scaled to the root-mean-square norm of the
  component the paired `rand-mean` draw removes on the reference set
  at that layer, s_{L,seed,k} = sqrt(mean_pos ‖(h·D − μ)·D‖²). Same
  (seed, k) → same basis → same strength; only the operator differs.
- Ranks k ∈ {4, 8, 16} (Experiment 1's null ranks; 16 is A3's rank cap).
- 20 seeds per (operator, k) → 120 residual draws per checkpoint.

Register operator, register-bearing checkpoints only (the original
design's ablation target, RT-13's "noise" operator):

- **register-state noise** (`reg-noise`): every register read receives
  a fresh random content state per row, Gaussian direction scaled to
  the reference root-mean-square row norm of the intact register state
  (over the reference set, all segments, all rows); marker keys and
  writes untouched. 20 seeds. Reported separately; it is not pooled
  into the residual band because A3 trains no register.

Metric, floor rule, quantiles (pre-committed)
--------------------------------------------
- chance_B = mean over the eval's battery-B queries of 1/n_choices
  (8-way for T_sr, T_si, T_sr_rev; 10-way for T_syntax; T_state mixes
  9- and 24-way and is reported at its mean floor).
- d(B) is defined only where B_base − chance_B ≥ 0.10 (the battery was
  learned above floor). Otherwise the battery is marked "floor" and
  only the raw accuracy change is recorded — d on an unlearned battery
  divides by nothing.
- θ_B (null band) = the 95th percentile (linear interpolation) of |d(B)|
  over the 120 residual draws pooled across both operators and all k;
  per-(operator, k) bands are recorded alongside. Signed 2.5th and
  97.5th percentiles are recorded for reading direction.
- δ (differential band) = the 95th percentile of |d(B1) − d(B2)| over
  the same draws, for the registered pair (T_sr, T_state), the
  self-battery pairs (T_si, T_state), (T_sr_rev, T_state), and the
  self-versus-other pair (T_sr_rev, T_si) that is the nearest existing
  analogue of A3's (T_act, T_other).
- **K0 test**: on the verdict batteries T_si and T_sr_rev of every
  checkpoint where they are above floor (the two binders), does the
  pooled θ_B reach the proposed 0.25? The script prints the comparison
  and the maximum band; it does not decide. The number is John's to set
  at Gate 0 (A3 §4.2); 0.25 is the proposed value and is applied
  provisionally, labelled as such.

Asterisk stated in the record
-----------------------------
The pilot seed-0 full checkpoint had its register-ablation battery
scores read (thread 4, 2026-08-19) before any threshold lock, which
RT-10 says voids the lock for that checkpoint. The band computed here
for seed 0 is therefore "for the record": usable as the noise floor
for reading the thread-4 numbers, not as a clean registered lock on
seed 0. The other four checkpoints had only their intact batteries and
(seed-1 full, seed-1 twin) the acting-channel lesion read.

Corrigibility: inference only, local checkpoints, $0 [C1/C2]; results
go to fresh per-checkpoint JSON files, never over an existing record
[C6]; nothing here trains, promotes, or launches.

    ../../../.venv/bin/python null_calibration.py --self-test
    ../../../.venv/bin/python null_calibration.py --smoke      # untrained
                                # smoke-scale model, instrument check only
    ../../../.venv/bin/python null_calibration.py --ckpt <path> \
        --out ../null-calibration/null_calibration_<name>.json
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

import curriculum as C
import encoding as E
from model import MVM0aModel, Config, SCALES, to_torch
from train import eval_heldout, enact_batched
from lesion_register import load_checkpoint, HELDOUT_SEED

EVAL_N = 400
REF_SEED = 20_260_914            # reference-set seed (this record's date)
REF_N = 100
ABLATE_LAYERS = [3, 4, 5, 7, 8]  # scale_layers([8,11,14,18,22], 32→12)
NULL_KS = [4, 8, 16]
N_SEEDS = 20
QUANTILE = 0.95
FLOOR_MARGIN = 0.10
K0_PROPOSED = 0.25
VERDICT_BATTERIES = ("T_si", "T_sr_rev")
DIFF_PAIRS = (("T_sr", "T_state"), ("T_si", "T_state"),
              ("T_sr_rev", "T_state"), ("T_sr_rev", "T_si"))
RESIDUAL_OPS = ("rand-mean", "rand-noise")
REGISTER_OP = "reg-noise"
BATTERIES = (*C.BATTERIES, "T_sr_rev")


# ----------------------------------------------------------------- reference

def chance_floors(n: int, seed: int) -> dict[str, float]:
    """Mean 1/n_choices per battery over the eval's own queries."""
    eps = C.generate_balanced(n, seed, forced_revision_frac=0.25)
    acc: dict[str, list[float]] = {b: [] for b in C.BATTERIES}
    for e in eps:
        for q in e.queries:
            acc[q.battery].append(1.0 / q.n_choices)
    out = {b: float(np.mean(v)) for b, v in acc.items()}
    out["T_sr_rev"] = out["T_sr"]
    return out


@torch.no_grad()
def collect_reference(model: MVM0aModel, device: str, n: int, seed: int
                      ) -> tuple[dict[int, torch.Tensor], float | None]:
    """Intact-model block outputs at ABLATE_LAYERS over the reference
    episodes (non-pad positions, no query segment, the model's own
    enactment injections present), plus the RMS register row norm for
    register-bearing checkpoints."""
    eps = C.generate_balanced(n, seed, forced_revision_frac=0.25)
    eps, act = enact_batched(model, eps, device, random.Random(seed + 1))
    batch = to_torch(E.collate([E.encode_episode(e) for e in eps]), device)
    act = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
    caps: dict[int, list[torch.Tensor]] = {L: [] for L in ABLATE_LAYERS}
    reg_sq: list[torch.Tensor] = []

    def capture(L):
        blk = model.blocks[L]
        orig = blk.forward

        def patched(x, kv, reg_repr):
            x, ctx = orig(x, kv, reg_repr)
            caps[L].append(x.detach())
            return x, ctx
        blk.forward = patched

    for L in ABLATE_LAYERS:
        capture(L)
    if model.cfg.use_register:
        orig_rr = model._reg_repr

        def rr(rs, keys):
            reg_sq.append((rs.detach().float() ** 2).sum(-1).flatten())
            return orig_rr(rs, keys)
        model._reg_repr = rr
    model.forward(batch, act_inject=act)
    for L in ABLATE_LAYERS:
        del model.blocks[L].__dict__["forward"]
    if model.cfg.use_register:
        del model.__dict__["_reg_repr"]
    keep = (batch["input_ids"] != E.PAD_ID)
    ref = {}
    for L in ABLATE_LAYERS:
        h = torch.cat(caps[L], dim=1)          # (B, L_total, d)
        ref[L] = h[keep].float()               # (n_pos, d)
    reg_rms = (float(torch.cat(reg_sq).mean().sqrt())
               if model.cfg.use_register else None)
    return ref, reg_rms


# ----------------------------------------------------------------- operators

def random_basis(seed: int, k: int, d: int) -> dict[int, np.ndarray]:
    """One rng per (seed, k); per-layer draws in layer order; QR."""
    rng = np.random.default_rng(seed * 1000 + k)
    out = {}
    for L in ABLATE_LAYERS:
        q, _ = np.linalg.qr(rng.standard_normal((d, k)))
        out[L] = q.T.astype(np.float32)        # (k, d) orthonormal rows
    return out


def install_residual(model: MVM0aModel, op: str, seed: int, k: int,
                     ref: dict[int, torch.Tensor], device: str) -> dict:
    """Patch block instances at ABLATE_LAYERS. Returns the per-layer
    strength record. The class is never touched."""
    bases = random_basis(seed, k, model.cfg.d_model)
    rec = {}
    for L in ABLATE_LAYERS:
        D = torch.as_tensor(bases[L], device=device)           # (k, d)
        mu = (ref[L] @ D.T).mean(0)                            # (k,)
        removed = ((ref[L] @ D.T) - mu) @ D                    # (n_pos, d)
        strength = float((removed ** 2).sum(-1).mean().sqrt())
        rec[str(L)] = {"k": k, "rms_removed_norm": strength,
                       "mu_abs_mean": float(mu.abs().mean())}
        blk = model.blocks[L]
        orig = blk.forward
        if op == "rand-mean":
            def patched(x, kv, reg_repr, _o=orig, _D=D, _mu=mu):
                x, ctx = _o(x, kv, reg_repr)
                x = x + (_mu - x @ _D.T) @ _D
                return x, ctx
        elif op == "rand-noise":
            gen = torch.Generator().manual_seed(seed * 100_003 + k * 101 + L)

            def patched(x, kv, reg_repr, _o=orig, _s=strength, _g=gen):
                x, ctx = _o(x, kv, reg_repr)
                nz = torch.randn(x.shape, generator=_g).to(x.device)
                nz = nz / nz.norm(dim=-1, keepdim=True).clamp_min(1e-6) * _s
                return x + nz, ctx
        else:
            raise ValueError(op)
        blk.forward = patched
    return rec


def install_register_noise(model: MVM0aModel, seed: int, reg_rms: float
                           ) -> dict:
    assert model.cfg.use_register, "register operator needs the full arch"
    gen = torch.Generator().manual_seed(seed * 7919 + 1)
    orig = model._reg_repr

    def rr(rs, keys):
        nz = torch.randn(rs.shape, generator=gen).to(rs.device)
        nz = nz / nz.norm(dim=-1, keepdim=True).clamp_min(1e-6) * reg_rms
        return orig(nz.to(rs.dtype), keys)
    model._reg_repr = rr
    return {"reg_rms_row_norm": reg_rms}


# ------------------------------------------------------------------- metric

def d_metric(base: dict, abl: dict, chance: dict) -> dict:
    out = {}
    for b in BATTERIES:
        den = base[b] - chance[b]
        out[b] = (None if den < FLOOR_MARGIN
                  else round((base[b] - abl[b]) / den, 4))
    return out


def tsi_rescore(model: MVM0aModel, device: str, n: int, seed: int) -> dict:
    """T_si scored against the recorded answer AND against the latest
    value the named agent gave that item (the A3 decision-14 fix, as
    a $0 side table). Same pipeline as eval_heldout, T_si queries only."""
    model.eval()
    eps = C.generate_balanced(n, seed, forced_revision_frac=0.25)
    eps, act = enact_batched(model, eps, device, random.Random(seed + 1))
    pairs = [(ei, q) for ei, e in enumerate(eps) for q in e.queries
             if q.battery == "T_si"]
    cells = {"unique": [0, 0, 0], "repeated": [0, 0, 0]}  # n, ok_rec, ok_latest
    for i in range(0, len(pairs), 50):
        chunk = pairs[i:i + 50]
        batch = to_torch(E.collate([E.encode_episode(eps[ei], query=q)
                                    for ei, q in chunk]), device)
        a = F.pad(act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
        a = a[[ei for ei, _ in chunk]]
        cids = [[E.VOCAB[c] for c in q.choices] for _, q in chunk]
        picks = model.score_choices(batch, cids, act_inject=a)
        for p, (ei, q) in zip(picks, chunk):
            e = eps[ei]
            marker, item = q.text.split()[2], q.text.split()[-1].rstrip("?")
            same = [t for t in e.turns if t.marker == marker and t.item == item]
            cell = cells["repeated" if len(same) > 1 else "unique"]
            cell[0] += 1
            cell[1] += int(p == E.VOCAB[q.answer])
            cell[2] += int(p == E.VOCAB[same[-1].value])
    return {c: {"n": v[0], "acc_recorded": round(v[1] / max(1, v[0]), 3),
                "acc_latest_value": round(v[2] / max(1, v[0]), 3)}
            for c, v in cells.items()}


# ---------------------------------------------------------------------- run

def run(ckpt: Path, device: str, n: int, n_seeds: int, ks: list[int],
        out: Path | None, cfg_override: Config | None = None) -> dict:
    t_start = time.time()
    if cfg_override is None:
        md5 = hashlib.md5(ckpt.read_bytes()).hexdigest()
        loader = lambda: load_checkpoint(ckpt, device)[0]   # noqa: E731
        name = ckpt.name
    else:                       # --smoke: untrained smoke-scale model
        md5, name = "untrained-smoke", "smoke"

        def loader():
            torch.manual_seed(0)
            return MVM0aModel(cfg_override).to(device).eval()
    chance = chance_floors(n, HELDOUT_SEED)
    model = loader()
    use_register = model.cfg.use_register
    print(f"[{name}] baseline ...", flush=True)
    base = eval_heldout(model, device, n=n, seed=HELDOUT_SEED)
    print(f"[{name}] baseline {base}", flush=True)
    tsi = tsi_rescore(model, device, n, HELDOUT_SEED)
    print(f"[{name}] T_si rescoring {tsi}", flush=True)
    ref, reg_rms = collect_reference(model, device, REF_N, REF_SEED)
    floor = {b: base[b] - chance[b] < FLOOR_MARGIN for b in BATTERIES}
    draws = []
    record = {
        "gate": "Gate 0 — registered θ/δ null calibration (A3 §4.1, K0)",
        "checkpoint": name, "checkpoint_md5": md5, "device": device,
        "arch": "full" if use_register else "twin",
        "eval": {"harness": "train.eval_heldout", "n": n,
                 "seed": HELDOUT_SEED},
        "reference": {"n": REF_N, "seed": REF_SEED,
                      "positions": {str(L): int(ref[L].shape[0])
                                    for L in ABLATE_LAYERS},
                      "reg_rms_row_norm": reg_rms},
        "pre_commitments": {"ablate_layers": ABLATE_LAYERS, "ks": ks,
                            "n_seeds": n_seeds, "quantile": QUANTILE,
                            "floor_margin": FLOOR_MARGIN,
                            "k0_proposed_band": K0_PROPOSED,
                            "verdict_batteries": VERDICT_BATTERIES,
                            "diff_pairs": DIFF_PAIRS},
        "asterisk": ("pilot seed-0 full: register-ablation battery scores "
                     "were read (thread 4, 2026-08-19) before any lock; "
                     "RT-10 voids a registered lock for that checkpoint. "
                     "Its band here is for the record, not a clean lock."),
        "chance": chance, "baseline": base, "floor": floor,
        "tsi_rescoring": tsi, "draws": draws,
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

    grid = [(op, k, s) for op in RESIDUAL_OPS for k in ks
            for s in range(n_seeds)]
    if use_register:
        grid += [(REGISTER_OP, 0, s) for s in range(n_seeds)]
    for i, (op, k, s) in enumerate(grid):
        t0 = time.time()
        model = loader()                        # fresh instance per draw
        if op == REGISTER_OP:
            strength = install_register_noise(model, s, reg_rms)
        else:
            strength = install_residual(model, op, s, k, ref, device)
        acc = eval_heldout(model, device, n=n, seed=HELDOUT_SEED)
        d = d_metric(base, acc, chance)
        draws.append({"op": op, "k": k, "seed": s, "acc": acc, "d": d,
                      "strength": strength, "sec": round(time.time() - t0, 1)})
        print(f"[{name}] {i + 1}/{len(grid)} {op} k={k} seed={s} "
              f"acc={acc} d={d} ({draws[-1]['sec']}s)", flush=True)
        if (i + 1) % 10 == 0:
            save(final=False)
    record["summary"] = summarize(record)
    record["elapsed_sec"] = round(time.time() - t_start, 1)
    save(final=True)
    return record


def _pct(xs: list[float], q: float) -> float | None:
    return None if not xs else round(float(np.percentile(xs, q * 100)), 4)


def summarize(rec: dict) -> dict:
    draws = rec["draws"]
    res = [x for x in draws if x["op"] in RESIDUAL_OPS]
    reg = [x for x in draws if x["op"] == REGISTER_OP]
    s: dict = {"theta": {}, "delta": {}, "register_theta": {},
               "per_condition": {}}
    for b in BATTERIES:
        if rec["floor"][b]:
            s["theta"][b] = {"floor": True,
                             "abs_acc_change_p95": _pct(
                                 [abs(x["acc"][b] - rec["baseline"][b])
                                  for x in res], QUANTILE)}
            continue
        ds = [x["d"][b] for x in res]
        s["theta"][b] = {"floor": False, "n_draws": len(ds),
                         "p95_abs_d": _pct([abs(v) for v in ds], QUANTILE),
                         "p2.5_d": _pct(ds, 0.025), "p97.5_d": _pct(ds, 0.975),
                         "max_abs_d": round(max(abs(v) for v in ds), 4)}
        if reg:
            dr = [x["d"][b] for x in reg]
            s["register_theta"][b] = {
                "n_draws": len(dr), "p95_abs_d": _pct([abs(v) for v in dr],
                                                      QUANTILE),
                "p2.5_d": _pct(dr, 0.025), "p97.5_d": _pct(dr, 0.975)}
        for op in RESIDUAL_OPS:
            for k in rec["pre_commitments"]["ks"]:
                sub = [abs(x["d"][b]) for x in res
                       if x["op"] == op and x["k"] == k]
                s["per_condition"].setdefault(f"{op}/k{k}", {})[b] = _pct(
                    sub, QUANTILE)
    for b1, b2 in DIFF_PAIRS:
        key = f"{b1}-{b2}"
        if rec["floor"][b1] or rec["floor"][b2]:
            s["delta"][key] = {"floor": True}
            continue
        dd = [abs(x["d"][b1] - x["d"][b2]) for x in res]
        s["delta"][key] = {"floor": False, "p95_abs_diff": _pct(dd, QUANTILE)}
    k0 = {}
    for b in VERDICT_BATTERIES:
        th = s["theta"][b]
        k0[b] = (None if th["floor"] else
                 {"p95_abs_d": th["p95_abs_d"],
                  "reaches_proposed_0.25": th["p95_abs_d"] >= K0_PROPOSED})
    s["k0_check"] = {"proposed_band": K0_PROPOSED, "verdict_batteries": k0,
                     "note": "the number is John's to set at Gate 0; 0.25 "
                             "is the proposed value, applied provisionally"}
    return s


# ---------------------------------------------------------------- self-test

def self_test() -> None:
    torch.manual_seed(0)
    cfg = SCALES["smoke"]
    d = cfg.d_model
    # random bases are orthonormal and reproducible
    b1, b2 = random_basis(3, 4, d), random_basis(3, 4, d)
    L0 = ABLATE_LAYERS[0]
    assert np.allclose(b1[L0] @ b1[L0].T, np.eye(4), atol=1e-5)
    assert np.array_equal(b1[L0], b2[L0])
    assert not np.array_equal(b1[L0], random_basis(4, 4, d)[L0])
    # mean-ablation pins coordinates to the reference mean (unit test on
    # the exact formula used by the patch)
    ref = torch.randn(200, d)
    D = torch.as_tensor(b1[L0])
    mu = (ref @ D.T).mean(0)
    x = torch.randn(5, 7, d)
    y = x + (mu - x @ D.T) @ D
    assert torch.allclose(y @ D.T, mu.expand(5, 7, 4), atol=1e-5)
    # orthogonal complement untouched
    assert torch.allclose(y - (y @ D.T) @ D, x - (x @ D.T) @ D, atol=1e-5)
    # patches are instance-level and reversible; twin accepts residual
    # ops; register op refuses the twin; ablated forward differs
    n_layers = max(ABLATE_LAYERS) + 1
    cfg = Config(d_model=64, n_layers=n_layers, n_heads=2)
    twin_cfg = Config(**{**cfg.__dict__, "use_register": False})
    eps = [C.generate_episode(s) for s in range(4)]
    batch = to_torch(E.collate([E.encode_episode(e, query=e.queries[0])
                                for e in eps]))
    for c in (cfg, twin_cfg):
        torch.manual_seed(0)
        m = MVM0aModel(c).eval()
        with torch.no_grad():
            base = m(batch)
            reff, rms = collect_reference(m, "cpu", 4, 1)
            assert all("forward" not in m.blocks[L].__dict__
                       for L in ABLATE_LAYERS), "capture patch leaked"
            assert "_reg_repr" not in m.__dict__
            assert torch.allclose(m(batch), base, atol=1e-5)
            for op in RESIDUAL_OPS:
                torch.manual_seed(0)
                m2 = MVM0aModel(c).eval()
                rec = install_residual(m2, op, 0, 4, reff, "cpu")
                assert all(v["rms_removed_norm"] > 0 for v in rec.values())
                out = m2(batch)
                assert out.isfinite().all()
                assert not torch.allclose(out, base, atol=1e-5), op
            if c.use_register:
                assert rms is not None and rms > 0
                torch.manual_seed(0)
                m3 = MVM0aModel(c).eval()
                install_register_noise(m3, 0, rms)
                out = m3(batch)
                assert out.isfinite().all() and not torch.allclose(
                    out, base, atol=1e-5)
            else:
                assert rms is None
                try:
                    install_register_noise(MVM0aModel(c), 0, 1.0)
                    raise RuntimeError("twin accepted register op")
                except AssertionError:
                    pass
            # class untouched
            torch.manual_seed(0)
            assert torch.allclose(MVM0aModel(c).eval()(batch), base,
                                  atol=1e-5), "class-level leak"
    # noise strength matches the removal strength on the reference set
    torch.manual_seed(0)
    m = MVM0aModel(twin_cfg).eval()
    reff, _ = collect_reference(m, "cpu", 4, 1)
    rec_m = install_residual(MVM0aModel(twin_cfg).eval(), "rand-mean", 2, 8,
                             reff, "cpu")
    rec_n = install_residual(MVM0aModel(twin_cfg).eval(), "rand-noise", 2, 8,
                             reff, "cpu")
    assert rec_m == rec_n, "paired draws must share basis and strength"
    # metric + floor rule
    ch = {b: 0.125 for b in BATTERIES}
    base = {b: 1.0 for b in BATTERIES}
    base["T_si"] = 0.2
    d = d_metric(base, {b: 0.5 for b in BATTERIES}, ch)
    assert d["T_sr"] == round(0.5 / 0.875, 4) and d["T_si"] is None
    print("null_calibration self-test OK")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--smoke", action="store_true",
                    help="untrained smoke-scale model, tiny grid; "
                         "instrument check only, numbers meaningless")
    ap.add_argument("--ckpt", default=None)
    ap.add_argument("--n", type=int, default=EVAL_N)
    ap.add_argument("--seeds", type=int, default=N_SEEDS)
    ap.add_argument("--ks", default=",".join(map(str, NULL_KS)))
    ap.add_argument("--device", default="mps" if
                    torch.backends.mps.is_available() else "cpu")
    ap.add_argument("--out", default=None,
                    help="result JSON (refuses to overwrite [C6])")
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    ks = [int(k) for k in args.ks.split(",") if k]
    if args.smoke:
        cfg = Config(d_model=64, n_layers=max(ABLATE_LAYERS) + 1, n_heads=2)
        rec = run(Path("smoke"), args.device, 8, 1, [4], None,
                  cfg_override=cfg)
        print(json.dumps(rec["summary"], indent=1))
        return
    assert args.ckpt, "--ckpt required"
    out = Path(args.out) if args.out else None
    if out is not None:
        assert not out.exists(), f"refusing to overwrite {out} [C6]"
    rec = run(Path(args.ckpt).resolve(), args.device, args.n, args.seeds,
              ks, out)
    print(json.dumps(rec["summary"], indent=1))
    if out is not None:
        print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
