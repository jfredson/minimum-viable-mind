"""The registered blind-localization arm (RT-12), run blind.

Registered in `pre-registration.md` §Procedure step 8, unconditional,
adjudicated 2026-08-07 and never run. John scheduled it 2026-09-16
(decision `cf0507f4`) and directed it started immediately.

THE FIREWALL, as registered
---------------------------
1. **The headline verdict is computed and committed before this runs.**
   Satisfied: the register-lesion result is committed in the repo
   (`register-lesion-findings.md`, thread 4) and has been since
   2026-08-19.
2. **The pipeline receives a config with the register's location
   withheld.** Enforced here in code, not by intention: this module never
   references `reg_init`, `content_proj`, `key_proj`, `writer`, `pool_q`
   or the cross-attention modules, and never reads `turn_reg` or
   `register_keys`. It searches the residual stream generically, exactly
   as it would on a model whose internals were unknown. `assert_blind()`
   checks the module's own source for those names and fails if any
   appear.
3. **Thresholds are inherited, not tuned here.** Rank cap and layer
   depths come from Experiment 1 via the same constants A3 uses. Nothing
   in this file selects a threshold after seeing an output.
4. **The verdict criteria below are committed before the run.** This file
   is committed first; the run happens afterwards. That is the whole
   point of a verdict-first firewall and it is cheap to honour.

WHAT THE ARM CAN AND CANNOT TEST NOW
------------------------------------
The registered question was whether the instruments recover a center
"known-by-construction to exist AND to be load-bearing". **Half that
premise is false.** Thread 4 measured the register to be inert: removing
the injection entirely left every battery unchanged, and deranging which
register is read moved logits by a mean absolute 0.014. The register
exists by construction; it does not matter.

So the arm as written cannot ask its original question, and saying so is
part of running it honestly. What it CAN ask, on the same checkpoints and
at no extra cost, is the complementary question:

  **Given a designated self-structure that provably exists and provably
  does not matter, does the localization stack correctly report that it
  does not matter — or does it manufacture a false positive?**

That bears directly on how Experiment 1's null should be read, which is
what RT-12 said might outweigh the headline.

PRE-STATED VERDICT CRITERIA (committed before the run)
------------------------------------------------------
The pipeline searches the residual stream for a subspace decoding
own-agent identity, then ablates what it finds and reads the batteries.
Let `probe` be the best per-layer probe accuracy against its
label-permutation null, and `d_found` the chance-corrected battery drop
under ablating the found subspace at the inherited rank.

- **RECOVERS-AND-CORRECTLY-DISMISSES.** `probe` clears its null by the
  inherited margin AND `d_found` stays inside the Gate 0 null band. The
  stack located a designated structure and correctly reported it as
  inert. The instruments are trustworthy on this case.
- **FALSE POSITIVE.** `d_found` exceeds the Gate 0 null band on a battery
  while the *direct* register ablation does not. The stack attributes
  importance to something the registered lesion shows is unimportant.
  This is the outcome that most changes how Experiment 1's null reads,
  and it would be reported upstream.
- **INSTRUMENT FAILURE TO LOCATE.** `probe` does not clear its null at
  any layer. The stack cannot find own-agent identity at all in a model
  that was built with a designated slot for it. Also upstream-reportable.
- **NOT TESTABLE (localization).** Probe and ablation disagree in a way
  the design cannot adjudicate, per Experiment 1's own convergence rule.

No bin is added after the fact. If the result fits none of these, it is
reported as fitting none.

Corrigibility: inference only, local checkpoints already in hand, $0
[C1/C2]; fresh output file, nothing overwritten [C6].

    ../../../.venv/bin/python blind_arm.py --self-test
    ../../../.venv/bin/python blind_arm.py --ckpt <A2 checkpoint> --run
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
from train import eval_heldout, enact_batched

# Inherited from Experiment 1 via the same constants A3 uses. Not tuned.
PROBE_LAYERS = NC.ABLATE_LAYERS
RANK_CAP = 16
N_PERM = 100
GATE0_BAND = 0.25          # the pre-stated K0 band, John 2026-09-16

# Names the blind pipeline must never touch. Checked against this file's
# own source by assert_blind().
FORBIDDEN = ("reg_init", "content_proj", "key_proj", "writer", "pool_q",
             "xattn", "_reg_repr", "_write", "turn_reg", "register_keys",
             "use_register")


def assert_blind() -> None:
    """Fail if this module names any register-specific internal. The
    firewall is a property of the code, not a promise about it."""
    src = Path(__file__).read_text()
    body = src[src.index("def assert_blind"):]
    body = body[body.index("\n\n"):]          # skip this function itself
    hits = sorted({n for n in FORBIDDEN if n in body})
    if hits:
        raise AssertionError(
            f"BLINDNESS VIOLATED: this module references {hits}. The "
            f"pipeline must not know where the register is.")


@torch.no_grad()
def residuals(model, eps, device):
    """Residual-stream states at the last token of each turn, per layer.
    Generic: no knowledge of model internals beyond block outputs."""
    caps = {L: [] for L in PROBE_LAYERS}
    eps, act = enact_batched(model, list(eps), device, random.Random(0))
    batch = to_torch(E.collate([E.encode_episode(e) for e in eps]), device)
    a = torch.nn.functional.pad(
        act, (0, 0, 0, batch["input_ids"].shape[1] - act.shape[1]))
    for L in PROBE_LAYERS:
        blk = model.blocks[L]
        orig = blk.forward

        def patched(x, kv, rr, _o=orig, _L=L):
            x, ctx = _o(x, kv, rr)
            caps[_L].append(x.detach())
            return x, ctx
        blk.forward = patched
    model.forward(batch, act_inject=a)
    for L in PROBE_LAYERS:
        del model.blocks[L].__dict__["forward"]

    out = {}
    for L in PROBE_LAYERS:
        h = torch.cat(caps[L], dim=1)
        # read each episode's LAST non-pad position: a generic choice that
        # presumes nothing about where a self-index would live
        keep = (batch["input_ids"] != E.PAD_ID).sum(1) - 1
        idx = torch.arange(h.shape[0], device=h.device)
        out[L] = h[idx, keep].float().cpu().numpy()
    return out, eps


def probe(X, y, seed=0):
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score
    rng = np.random.default_rng(seed)
    clf = LogisticRegression(max_iter=2000, C=1.0)
    real = float(cross_val_score(clf, X, y, cv=4).mean())
    null = [float(cross_val_score(clf, X, rng.permutation(y), cv=4).mean())
            for _ in range(N_PERM)]
    m, sd = float(np.mean(null)), float(np.std(null, ddof=1))
    return {"accuracy": round(real, 4), "null_mean": round(m, 4),
            "null_sd": round(sd, 4),
            "margin_sd": round((real - m) / sd, 2) if sd > 0 else None}


def subspace(X, y, rank=RANK_CAP):
    classes = sorted(set(y))
    mus = np.stack([X[np.asarray(y) == c].mean(0) for c in classes])
    cen = mus - mus.mean(0, keepdims=True)
    _, _, vt = np.linalg.svd(cen, full_matrices=False)
    return vt[:min(rank, vt.shape[0])]


def run(ckpt: Path, device: str, n: int = 400) -> dict:
    assert_blind()
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    base = eval_heldout(model, device, n=n)
    eps = C.generate_balanced(n, NC.REF_SEED, forced_revision_frac=0.25)
    acts, eps = residuals(model, eps, device)
    y = [e.own_slot for e in eps]

    probes = {str(L): probe(acts[L], y, seed=L) for L in PROBE_LAYERS}
    best = max(PROBE_LAYERS, key=lambda L: probes[str(L)]["accuracy"])

    # ablate what the blind search found, at the inherited rank
    d = subspace(acts[best], y)
    ref = {L: torch.as_tensor(acts[L], device=device) for L in PROBE_LAYERS}
    m2 = MVM0aModel(Config(**ck["cfg"])).to(device)
    m2.load_state_dict(ck["state"])
    m2.eval()
    D = torch.as_tensor(d, device=device, dtype=torch.float32)
    mu = (ref[best] @ D.T).mean(0)
    blk = m2.blocks[best]
    orig = blk.forward

    def abl(x, kv, rr, _o=orig, _D=D, _mu=mu):
        x, ctx = _o(x, kv, rr)
        return x + (_mu - x @ _D.T) @ _D, ctx
    blk.forward = abl
    lesioned = eval_heldout(m2, device, n=n)

    chance = NC.chance_floors(n, NC.HELDOUT_SEED)
    d_found = NC.d_metric(base, lesioned, chance)
    return {"arm": "registered blind-localization arm (RT-12)",
            "checkpoint": ckpt.name,
            "firewall": {
                "headline_committed_before": "register-lesion-findings.md, "
                                             "committed 2026-08-19",
                "register_location_withheld": True,
                "thresholds_inherited": True,
                "criteria_committed_before_run": True},
            "probe_layers": PROBE_LAYERS, "rank": int(d.shape[0]),
            "probes": probes, "best_layer": best,
            "baseline": base, "lesioned_found_subspace": lesioned,
            "d_found": d_found, "gate0_band": GATE0_BAND}


def self_test() -> None:
    assert_blind()
    cfg = Config(d_model=64, n_layers=max(PROBE_LAYERS) + 1, n_heads=2)
    torch.manual_seed(0)
    m = MVM0aModel(cfg).eval()
    eps = C.generate_balanced(16, 3, forced_revision_frac=0.25)
    acts, eps = residuals(m, eps, "cpu")
    assert set(acts) == set(PROBE_LAYERS)
    for L in PROBE_LAYERS:
        assert acts[L].shape == (len(eps), cfg.d_model)
        assert "forward" not in m.blocks[L].__dict__, "hook leaked"
    y = [e.own_slot for e in eps]
    d = subspace(acts[PROBE_LAYERS[0]], y)
    assert d.shape[0] <= RANK_CAP
    assert np.allclose(d @ d.T, np.eye(d.shape[0]), atol=1e-6)
    print(f"blind_arm self-test OK (blindness asserted against "
          f"{len(FORBIDDEN)} forbidden names; {len(PROBE_LAYERS)} layers, "
          f"rank cap {RANK_CAP})")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--ckpt", default=None)
    ap.add_argument("--n", type=int, default=400)
    ap.add_argument("--device", default="mps" if
                    torch.backends.mps.is_available() else "cpu")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    if args.run:
        assert args.ckpt, "--ckpt required"
        res = run(Path(args.ckpt).resolve(), args.device, args.n)
        print(json.dumps(res, indent=2))
        if args.out:
            p = Path(args.out)
            assert not p.exists(), f"refusing to overwrite {p} [C6]"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(json.dumps(res, indent=2))
            print(f"\nwrote {p}")


if __name__ == "__main__":
    main()
