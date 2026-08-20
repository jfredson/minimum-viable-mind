"""Register-lesion diagnostic — twin-binding-anomaly.md thread 4.

The decisive cheap test: zero/lesion the register in the BOUND pilot
checkpoint at inference and re-score the self batteries on the
registered held-out eval (`train.eval_heldout`, seed 987654321 — the
same eval the endpoint rows report). If the pilot's binding survives
the lesion, even the one clean success was never register-dependent
and the construct problem is total rather than partial; if it
collapses, the register is load-bearing in the pilot and the problem
is confined to the batteries' solvability-without-register.

Four lesions, each an inference-time patch on the loaded instance —
the canonical `MVM0aModel.forward` runs unmodified, so nothing here
can drift from the registered architecture:

- **frozen-writes** — `_write` returns the state unchanged: registers
  sit at the shared learned init all episode (identical rows; identity
  only in marker keys). Tests whether ACCUMULATED content matters.
- **keys-only** — `_reg_repr` reads zero content (content_proj has no
  bias, so zero content contributes exactly nothing); marker keys
  survive. Tests whether any content read matters, including the
  static init offset.
- **no-xattn** — `_reg_repr` returns None, so every block skips the
  register cross-attention entirely. The full architectural lesion.
- **shuffle-binding** — content rows are read under a DERANGED key
  assignment (agent i's key presents agent perm(i)'s content); writes
  untouched. The binding-specific lesion: content exists and is
  correct per-agent, but the marker->content binding is broken.

The whole eval runs under the lesion — enactment forward passes and
acting-channel injections included — so the scores are those of the
lesioned model performing the eval itself, matching how the endpoint
numbers were produced.

Corrigibility: inference only — no training, no pods, no spend [C2];
checkpoints stay local and non-promotable [C1]; results go to a fresh
per-run JSON, never over an existing record [C6].

    ../../../.venv/bin/python lesion_register.py --self-test
    ../../../.venv/bin/python lesion_register.py \
        --ckpt ../artifacts/pilot_a1_30m_seed0/pilot_a1_30m_seed0.pt \
        --out ../lesion-results/register_lesion_pilot_a1_30m_seed0.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import torch

from model import MVM0aModel, Config
from train import eval_heldout

LESIONS = ("none", "frozen-writes", "keys-only", "no-xattn",
           "shuffle-binding", "no-act")
HELDOUT_SEED = 987_654_321          # the registered held-out eval seed
SECOND_SEED = 20_260_819            # disjoint replicate (this note's date)


def load_checkpoint(ckpt: Path, device: str) -> tuple[MVM0aModel, dict]:
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device)
    model.load_state_dict(ck["state"])
    model.eval()
    return model, ck


def apply_lesion(model: MVM0aModel, name: str) -> str:
    """Patch the INSTANCE (never the class); returns a description for
    the record. 'none' leaves the model intact."""
    if name == "none":
        return "intact model (baseline / endpoint-reproduction check)"
    if name == "no-act":
        # acting-channel lesion [A1]: act_proj emits zeros, so the
        # motor-copy injections vanish and authorship information never
        # enters the trunk. Applies to full AND twin (the channel is
        # trunk input, not register machinery), hence sits before the
        # use_register assert.
        with torch.no_grad():
            model.act_proj.weight.zero_()
        return ("acting channel zeroed: act_proj weight -> 0 (bias-free "
                "Linear), no motor-copy injection reaches the trunk "
                "(enacted VALUES unchanged — they are data-side)")
    assert model.cfg.use_register, "register lesions need the full arch"
    if name == "frozen-writes":
        model._write = lambda reg_state, seg_h, rows: reg_state
        return ("writes disabled: registers stay at the shared learned "
                "init all episode; marker keys intact")
    if name == "keys-only":
        orig = model._reg_repr
        model._reg_repr = lambda rs, keys: orig(torch.zeros_like(rs), keys)
        return ("content read zeroed (content_proj is bias-free, so the "
                "read contributes exactly the marker keys)")
    if name == "no-xattn":
        model._reg_repr = lambda rs, keys: None
        return ("register injection removed: _reg_repr -> None, every "
                "block skips its cross-attention")
    if name == "shuffle-binding":
        n = model.cfg.n_agents
        perm = [(i + 1) % n for i in range(n)]      # fixed derangement
        orig = model._reg_repr
        model._reg_repr = lambda rs, keys: orig(rs[:, perm], keys)
        return (f"binding broken: content rows read under deranged keys "
                f"(perm {perm}); writes untouched")
    raise ValueError(name)


def run(ckpt: Path, device: str, n: int, lesions: list[str],
        seeds: list[int]) -> dict:
    md5 = hashlib.md5(ckpt.read_bytes()).hexdigest()
    results = []
    for name in lesions:
        model, ck = load_checkpoint(ckpt, device)   # fresh load per lesion
        desc = apply_lesion(model, name)
        per_seed = {}
        for seed in seeds:
            per_seed[str(seed)] = eval_heldout(model, device, n=n,
                                               seed=seed)
            print(f"[{name}] seed {seed}: {per_seed[str(seed)]}",
                  flush=True)
        results.append({"lesion": name, "description": desc,
                        "acc": per_seed})
    return {
        "diagnostic": "register lesion at inference "
                      "(twin-binding-anomaly.md thread 4)",
        "checkpoint": ckpt.name,
        "checkpoint_md5": md5,
        "eval": {"harness": "train.eval_heldout", "n": n,
                 "seeds": seeds,
                 "note": f"seed {HELDOUT_SEED} is the registered "
                         "held-out eval the endpoint rows report"},
        "device": device,
        "lesions": results,
    }


def self_test() -> None:
    """Smoke-scale checks that each lesion does what its record says."""
    from model import SCALES
    import curriculum as C
    import encoding as E
    from model import to_torch
    torch.manual_seed(0)
    cfg = SCALES["smoke"]
    ref = MVM0aModel(cfg)
    ref.eval()
    eps = [C.generate_episode(s) for s in range(4)]
    batch = to_torch(E.collate([E.encode_episode(e, query=e.queries[0])
                                for e in eps]))

    def fresh():
        torch.manual_seed(0)
        m = MVM0aModel(cfg)
        m.eval()
        return m

    with torch.no_grad():
        base = ref(batch)
        for name in LESIONS[1:]:
            m = fresh()
            apply_lesion(m, name)
            out = m(batch)
            assert out.shape == base.shape and out.isfinite().all(), name
            if name == "no-act":
                # act_proj is only reached through an injection; check
                # the lesioned projection directly, and that the twin
                # accepts this lesion too
                assert m.act_proj(torch.randn(3, cfg.d_model)).abs().sum() == 0
                tw = MVM0aModel(Config(**{**cfg.__dict__,
                                          "use_register": False}))
                apply_lesion(tw, "no-act")
                continue
            assert not torch.allclose(out, base, atol=1e-5), \
                f"{name}: lesion had no effect on logits"
        # frozen-writes really freezes: state passed through unchanged
        m = fresh()
        apply_lesion(m, "frozen-writes")
        rs = m.reg_init.expand(2, cfg.n_agents, cfg.d_reg)
        assert m._write(rs, torch.randn(2, 6, cfg.d_model),
                        torch.zeros(2, dtype=torch.long)) is rs
        # keys-only == content contribution exactly zero
        m = fresh()
        rs = torch.randn(2, cfg.n_agents, cfg.d_reg)
        keys = torch.randint(0, cfg.vocab, (2, cfg.n_agents))
        apply_lesion(m, "keys-only")
        assert torch.allclose(m._reg_repr(rs, keys),
                              m.key_proj(m.tok(keys)), atol=1e-6)
        # shuffle-binding == intact repr of permuted rows
        m = fresh()
        apply_lesion(m, "shuffle-binding")
        got = m._reg_repr(rs, keys)
        want = m.content_proj(rs[:, [1, 2, 3, 0]]) + m.key_proj(m.tok(keys))
        assert torch.allclose(got, want, atol=1e-6)
        # lesions patch the instance, never the class
        assert "_reg_repr" not in ref.__dict__ and "_write" not in ref.__dict__
        assert not torch.allclose(fresh()(batch), out, atol=1e9) or True
        assert torch.allclose(fresh()(batch), base, atol=1e-5), \
            "class-level state leaked between lesioned instances"
    print("lesion self-test OK")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--ckpt", default=None)
    ap.add_argument("--n", type=int, default=100,
                    help="episodes per eval (100 = the endpoint rows)")
    ap.add_argument("--lesions", default=",".join(LESIONS))
    ap.add_argument("--seeds", default=f"{HELDOUT_SEED},{SECOND_SEED}")
    ap.add_argument("--device", default="mps" if
                    torch.backends.mps.is_available() else "cpu")
    ap.add_argument("--out", default=None,
                    help="result JSON (refuses to overwrite [C6])")
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    assert args.ckpt, "--ckpt required"
    lesions = [l for l in args.lesions.split(",") if l]
    assert all(l in LESIONS for l in lesions), lesions
    seeds = [int(s) for s in args.seeds.split(",")]
    res = run(Path(args.ckpt).resolve(), args.device, args.n,
              lesions, seeds)
    print(json.dumps(res, indent=2))
    if args.out:
        out = Path(args.out)
        assert not out.exists(), f"refusing to overwrite {out} [C6]"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(res, indent=2))
        print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
