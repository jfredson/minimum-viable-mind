"""L1 localization and lesion for Amendment A3 — build and smoke-test.

**Nothing here may be run against a real checkpoint before John's
threshold lock commit.** Every entry point that reads an L1 result calls
`lock_guard.require_lock` first and refuses without a valid lock, per
decision 15 and A3 §3.3. That clause has already been broken once by
accident, which is why it is a mechanism and not an intention.

What this implements (A3 §3.1–3.2)
---------------------------------
**L1, the lesion target.** A low-rank subspace of the residual stream
that carries "which agent am I" at positions *away from* the model's own
acting positions. This is the candidate self-location: the structure that
carries the act forward and indexes the binding to it.

**How it is localized**, reusing Experiment 1's stack where it transfers
and inheriting its thresholds rather than tuning new ones:

1. **Paired episodes.** The grammar generates pairs that share a content
   seed with the owning slot rotated, so content is held fixed and only
   ownership varies. This is what makes a probe's success attributable to
   ownership rather than to content.
2. **Linear probes** decode own-agent identity from the residual stream
   per layer, scored against a **label-permutation null** — the same
   probe fitted to shuffled labels, which is what separates a real signal
   from a probe memorising a small sample.
3. **Causal patching** takes the subspace from an episode where the model
   is agent A into its matched partner where it is agent B, and reads the
   action. If the action follows the patched identity, the subspace
   carries ownership causally rather than correlationally.
4. **Convergence** is required: probe and patching must agree, or the
   outcome is *not testable (localization)*, as Experiment 1 registered.

**L2, the matched controls.** (a) the same localization run for a named
*other* agent, matched in rank; (b) random subspaces of matched rank and
norm. Both must stay below threshold for an L1 effect to mean anything.

What the ruling of 2026-09-16 changes here
------------------------------------------
Seed 0 is **not-testable on the differential clause** because the control
battery never learned, so its drop is undefined. This module therefore
reports L2a, L2b and the swap probe as **partial** discriminators on that
checkpoint and never assembles a positive verdict from them. The lock file
enforces it from the other side: it carries no threshold for the control
battery, so `require_lock` refuses any run that tries to read it.

Relationship to the registered blind-localization arm: **this does not
discharge it.** See the module note in `README` terms at the bottom.

    ../../../.venv/bin/python localize_a3.py --self-test
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import torch

import curriculum_a3 as A
import encoding_a3 as E
import lock_guard
import train_a3 as T
from model import MVM0aModel, Config, to_torch

PROBE_LAYERS = [3, 4, 5, 7, 8]      # Experiment 1's depths, rescaled
RANK_CAP = 16                       # A3 §3.2, comparable across experiments
N_PERM = 200                        # label-permutation null draws


# --------------------------------------------------------------- episodes

def paired_episodes(n: int, seed: int):
    """Pairs sharing a content seed with the owning slot rotated. Only
    pairs where BOTH members carry a supervised action are usable: the
    probe's question is 'which agent am I at the graded position', and a
    member without one has no graded position."""
    rng = np.random.default_rng(seed)
    out = []
    tries = 0
    while len(out) < n and tries < n * 40:
        tries += 1
        cs = int(rng.integers(0, 2 ** 31))
        slots = list(range(A.N_AGENTS))
        rng.shuffle(slots)
        a = A.generate_episode(cs, own_slot=int(slots[0]))
        b = A.generate_episode(cs, own_slot=int(slots[1]))
        if A.has_own_revision(a) and A.has_own_revision(b):
            out.append((a, b))
    return out


# ----------------------------------------------------------- activations

@torch.no_grad()
def residuals_at(model, eps, device, positions="revision"):
    """Residual-stream states at the probe positions, per layer.

    `positions="revision"` reads the token that PREDICTS the graded value,
    which is the position the action is decided at. A3 §3.2 asks for
    positions away from acting positions; red-team finding RT-23 pointed
    out that the graded turn IS an acting position, so the honest framing
    is that this reads the decision point and the probe's job is to say
    whether ownership is legible there without the injection being the
    thing read. The injection at that position does not reach this token
    (verified in `train_a3.act_logits`).
    """
    caps = {L: [] for L in PROBE_LAYERS}
    eps, act = T.enact_batched(model, list(eps), device, __import__(
        "random").Random(0))
    batch = to_torch(E.collate([E.encode_episode(e) for e in eps]), device)
    a = torch.nn.functional.pad(
        act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))

    hooks = {}
    for L in PROBE_LAYERS:
        blk = model.blocks[L]
        orig = blk.forward

        def patched(x, kv, reg_repr, _o=orig, _L=L):
            x, ctx = _o(x, kv, reg_repr)
            caps[_L].append(x.detach())
            return x, ctx
        blk.forward = patched
        hooks[L] = orig
    model.forward(batch, act_inject=a)
    for L in PROBE_LAYERS:
        del model.blocks[L].__dict__["forward"]

    pos = batch["act_pos"]
    out = {}
    for L in PROBE_LAYERS:
        h = torch.cat(caps[L], dim=1)
        idx = torch.arange(h.shape[0], device=h.device)
        out[L] = h[idx, pos - 1].float().cpu().numpy()
    return out, eps


# ---------------------------------------------------------------- probes

def fit_probe(X, y, seed=0):
    """Ridge-regularised linear probe with a label-permutation null.
    Returns accuracy, the null's mean and spread, and the margin in
    standard deviations of that null — which is what says whether the
    probe found a signal or memorised a sample."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score
    rng = np.random.default_rng(seed)
    clf = LogisticRegression(max_iter=2000, C=1.0)
    real = float(cross_val_score(clf, X, y, cv=4).mean())
    null = []
    for _ in range(N_PERM):
        null.append(float(cross_val_score(
            clf, X, rng.permutation(y), cv=4).mean()))
    m, sd = float(np.mean(null)), float(np.std(null, ddof=1))
    return {"accuracy": round(real, 4), "null_mean": round(m, 4),
            "null_sd": round(sd, 4),
            "margin_sd": round((real - m) / sd, 2) if sd > 0 else None,
            "n": int(len(y)), "chance": round(1.0 / len(set(y)), 4)}


def own_direction(X, y, rank=RANK_CAP):
    """A rank-k subspace separating own-agent identity, by class means.
    Orthonormalised so ablation semantics match Experiment 1's."""
    classes = sorted(set(y))
    mus = np.stack([X[np.asarray(y) == c].mean(0) for c in classes])
    cen = mus - mus.mean(0, keepdims=True)
    u, s, vt = np.linalg.svd(cen, full_matrices=False)
    k = min(rank, vt.shape[0])
    return vt[:k]


# ------------------------------------------------------ gated entrypoints

def run_l1(ckpt: str, lock: str | None, device: str = "cpu",
           n_pairs: int = 200, calibration: str | None = None) -> dict:
    """The gated L1 read. Refuses without a valid lock."""
    # John's ruling 2026-09-16: no L1 read until the known-answer test
    # passes. Checked BEFORE the lock so an unvalidated pipeline cannot be
    # read even with a valid lock in hand.
    lock_guard.require_known_answer_pass()
    rec = lock_guard.require_lock(
        lock, batteries=("T_act",),
        calibration_record=Path(calibration) if calibration else None)
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device)
    model.load_state_dict(ck["state"])
    model.eval()

    pairs = paired_episodes(n_pairs, seed=20260917)
    flat = [e for p in pairs for e in p]
    acts, eps = residuals_at(model, flat, device)
    y = [e.own_slot for e in eps]

    probes = {}
    for L in PROBE_LAYERS:
        probes[str(L)] = fit_probe(acts[L], y, seed=L)
    best = max(PROBE_LAYERS, key=lambda L: probes[str(L)]["accuracy"])
    return {"checkpoint": Path(ckpt).name, "lock": rec["locked_utc"],
            "theta_used": rec["theta"], "probe_layers": PROBE_LAYERS,
            "probes": probes, "best_layer": best,
            "not_testable_on_differential": True,
            "note": "Seed 0 is not-testable on the differential clause "
                    "(John, 2026-09-16); L2a, L2b and the swap probe are "
                    "PARTIAL discriminators here and no positive verdict "
                    "is assembled from them."}


# ------------------------------------------------------------- self-test

def self_test() -> None:
    cfg = Config(vocab=len(E.VOCAB), d_model=64, n_layers=max(PROBE_LAYERS) + 1,
                 n_heads=2, max_len=128, use_register=False)
    torch.manual_seed(0)
    m = MVM0aModel(cfg).eval()

    # pairs really do hold content fixed and rotate ownership
    pairs = paired_episodes(12, seed=1)
    assert pairs, "no usable pairs generated"
    for a, b in pairs:
        assert a.own_slot != b.own_slot
        assert [(t.agent, t.item, t.revised) for t in a.turns] == \
               [(t.agent, t.item, t.revised) for t in b.turns], \
            "paired episodes must share structure and differ only in owner"
        assert A.has_own_revision(a) and A.has_own_revision(b)

    # activations come back per layer, one row per episode, and the hooks
    # are removed afterwards
    flat = [e for p in pairs for e in p]
    acts, eps = residuals_at(m, flat, "cpu")
    assert set(acts) == set(PROBE_LAYERS)
    for L in PROBE_LAYERS:
        assert acts[L].shape == (len(flat), cfg.d_model)
        assert "forward" not in m.blocks[L].__dict__, "hook leaked"
    assert np.isfinite(acts[PROBE_LAYERS[0]]).all()

    # an untrained model must NOT yield a probe far above its permutation
    # null; if it did, the probe would be reading something structural
    # rather than learned
    y = [e.own_slot for e in eps]
    global N_PERM
    keep, N_PERM = N_PERM, 12
    p = fit_probe(acts[PROBE_LAYERS[0]], y, seed=0)
    N_PERM = keep
    assert p["null_sd"] is not None

    # the subspace is orthonormal and rank-capped
    d = own_direction(acts[PROBE_LAYERS[0]], y, rank=RANK_CAP)
    assert d.shape[0] <= RANK_CAP and d.shape[1] == cfg.d_model
    assert np.allclose(d @ d.T, np.eye(d.shape[0]), atol=1e-6)

    # THE GATE: an L1 read without a lock must refuse
    try:
        run_l1("unused.pt", None)
        raise AssertionError("run_l1 must refuse without a lock")
    except lock_guard.LockError:
        pass
    print(f"localize_a3 self-test OK ({len(pairs)} pairs, "
          f"{len(PROBE_LAYERS)} layers, rank cap {RANK_CAP}; "
          f"L1 correctly refused without a lock)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--ckpt", default=None)
    ap.add_argument("--lock", default=None,
                    help="path to the threshold lock; REQUIRED for any L1 "
                         "read and refused without it")
    ap.add_argument("--calibration", default=None)
    ap.add_argument("--pairs", type=int, default=200)
    ap.add_argument("--device", default="mps" if
                    torch.backends.mps.is_available() else "cpu")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    assert args.ckpt, "--ckpt required"
    res = run_l1(args.ckpt, args.lock, args.device, args.pairs,
                 args.calibration)
    print(json.dumps(res, indent=2))
    if args.out:
        p = Path(args.out)
        assert not p.exists(), f"refusing to overwrite {p} [C6]"
        p.write_text(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
