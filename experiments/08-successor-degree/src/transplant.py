"""Transplanting (activation patching), and its known-answer tests.

FROZEN CODE, NOT YET REGISTERED. Frozen 2026-10-04 under
`docs/successor-code-freeze-method-2026-10-04.md`. What it builds is section
6.2 of `docs/successor-experiment-proposal-2026-10-03-v4.md`.

Copied from the rehearsal's `transplant.py`, with the helpers the later toy
drivers added beside it brought into the one file: the position sets anchored
at the named-other action (`repairs.anchored_mask`, for control 2), the
positions before both twins' first own turns (control 4 as redefined,
`short_prestated_run.part_a`), the directions of a fitted read
(`rehearse.basis_for`) and the twenty random pieces
(`rerun_v3.random_bases`). Nothing they compute is changed.

The two transplants
-------------------
A site set is a list of running states and a set of positions, fixed before
anything is read. The whole-state transplant replaces the whole running state
there with the donor's; the ownership-only transplant replaces only the part
lying in the nominated piece. The second is the first restricted to a
subspace, and the self-test proves that as an identity on tensors: the
subspace form at full rank is the whole-state form.

Corrigibility: local, inference only, no network, no rented machine, $0.

    python transplant.py --self-test
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np
import torch

import grammar as G
import models as M


@dataclass(frozen=True)
class Sites:
    """Where a transplant happens. `layers` indexes the running state after
    the input embedding (0) and after each block (1 to n_layers)."""
    layers: tuple
    positions: str

    def label(self) -> str:
        return f"states {'+'.join(str(l) for l in self.layers)} at {self.positions}"


# The four registered position sets (version 4, section 7.2, item 2; ruled
# 2026-10-03, decision 19), in the rule's order. "all" and "pre-identity" are
# kept for the known-answer tests and the diagnostics; neither is a candidate.
POSITION_SETS = ("action", "action+ans", "action+3", "post-identity")


def _first_own(acting: torch.Tensor) -> torch.Tensor:
    return torch.argmax(acting, dim=1)


def position_mask(b: dict, which: str) -> torch.Tensor:
    """(B, S) boolean mask of the positions a site set covers, anchored at the
    own-directed action."""
    acting = b["acting"]
    B, S = acting.shape
    dev = acting.device
    ap = b["action_pos"][:, G.OWN]
    idx = torch.arange(S, device=dev)[None].expand(B, -1)
    if which == "all":
        return torch.ones(B, S, dtype=torch.bool, device=dev)
    first_own = _first_own(acting)
    if which == "action":
        return idx == ap[:, None]
    if which == "action+ans":
        return (idx == ap[:, None]) | (idx == (ap - 1)[:, None])
    if which == "action+3":
        return (idx <= ap[:, None]) & (idx >= (ap - 3)[:, None])
    if which == "post-identity":
        return (idx >= first_own[:, None]) & (idx <= ap[:, None])
    if which == "pre-identity":
        return idx < first_own[:, None]
    raise ValueError(f"unknown position set: {which}")


def anchored_mask(b: dict, which: str, cond: int) -> torch.Tensor:
    """The position sets anchored at the action of condition `cond`. For the
    own-directed condition this is `position_mask`; for the named-other one the
    action is the named-other action and "post-identity" starts at the named
    agent's first assignment turn (control 2)."""
    if cond == G.OWN:
        return position_mask(b, which)
    B, S = b["tokens"].shape
    dev = b["tokens"].device
    ap = b["action_pos"][:, G.OTHER]
    idx = torch.arange(S, device=dev)[None].expand(B, -1)
    if which == "all":
        return torch.ones(B, S, dtype=torch.bool, device=dev)
    if which == "action":
        return idx == ap[:, None]
    if which == "action+ans":
        return (idx == ap[:, None]) | (idx == (ap - 1)[:, None])
    if which == "action+3":
        return (idx <= ap[:, None]) & (idx >= (ap - 3)[:, None])
    if which == "post-identity":
        named = b["action_who"][:, G.OTHER]
        first = torch.argmax((b["assign_agent_at"] == named[:, None]).int(), dim=1)
        return (idx >= first[:, None]) & (idx <= ap[:, None])
    raise ValueError(which)


def before_both_twins(recip: dict, donor: dict) -> torch.Tensor:
    """Control 4 as redefined (ruled 2026-10-03): every position before both
    twins' first own turns. There the twins' inputs are identical."""
    B, S = recip["tokens"].shape
    idx = torch.arange(S, device=recip["tokens"].device)[None].expand(B, -1)
    return idx < torch.minimum(_first_own(recip["acting"]), _first_own(donor["acting"]))[:, None]


def capture(model, b: dict) -> list:
    with torch.no_grad():
        _, states = model(b, capture=True)
    return states


def patch_fn_factory(donor_states, sites: Sites, mask: torch.Tensor,
                     basis, alpha: float = 1.0):
    """`basis` is (D, k) with orthonormal columns, a dict of one per layer, or
    None for the whole state. The ownership-only transplant is exactly this
    function with a rank-k basis; the whole-state transplant is exactly this
    function with the identity. Nothing else differs between them."""
    m = mask.unsqueeze(-1)

    def fn(layer_index, state):
        if layer_index not in sites.layers:
            return state
        donor = donor_states[layer_index]
        bb = basis[layer_index] if isinstance(basis, dict) else basis
        if bb is None:
            moved = donor
        else:
            delta = donor - state
            moved = state + (delta @ bb) @ bb.T
        if alpha != 1.0:
            moved = state + alpha * (moved - state)
        return torch.where(m, moved, state)

    return fn


def transplanted_logits(model, recipient: dict, donor_states, sites: Sites,
                        mask: torch.Tensor, basis, alpha: float = 1.0) -> torch.Tensor:
    with torch.no_grad():
        return model(recipient,
                     patch_fn=patch_fn_factory(donor_states, sites, mask, basis, alpha))


def predictions(logits: torch.Tensor, condition: int = G.OWN) -> torch.Tensor:
    """The value word the model emits at one of its two action positions,
    restricted to the eight value slots."""
    slot_ids = torch.as_tensor(G.SLOT_IDS, device=logits.device)
    sub = logits[:, condition][:, slot_ids]
    return slot_ids[sub.argmax(dim=-1)]


def orthonormal(vectors: np.ndarray) -> torch.Tensor:
    """Orthonormal basis (D, k) for the row space of `vectors` (k, D)."""
    q, _ = np.linalg.qr(vectors.T)
    return torch.as_tensor(np.ascontiguousarray(q), dtype=torch.float32)


def basis_for(coef: np.ndarray, rank: int, device="cpu") -> torch.Tensor:
    """The piece of a fitted straight-line read: the top `rank` directions of
    its centred coefficient matrix, orthonormalised. The rehearsal's
    `rehearse.basis_for`, unchanged."""
    u, s, vt = np.linalg.svd(coef - coef.mean(axis=0, keepdims=True), full_matrices=False)
    r = min(rank, vt.shape[0])
    q, _ = np.linalg.qr(vt[:r].T)
    return torch.as_tensor(np.ascontiguousarray(q), dtype=torch.float32, device=device)


def random_bases(rank: int, layers, seed: int, D: int, n: int = 20, device="cpu") -> list:
    """Control 3's twenty random pieces of the same size at the same layers.
    The rehearsal's `rerun_v3.random_bases`, unchanged."""
    out = []
    for k in range(n):
        rng = np.random.default_rng([20260926, seed, k])
        out.append({l: orthonormal(rng.normal(size=(rank, D))).to(device) for l in layers})
    return out


def complement_basis(basis: torch.Tensor) -> torch.Tensor:
    """Control 1: every direction of the running state outside the piece."""
    bb = basis.numpy()
    uu, sv, _ = np.linalg.svd(np.eye(bb.shape[0]) - bb @ bb.T)
    return torch.as_tensor(np.ascontiguousarray(uu[:, sv > 1e-6]), dtype=torch.float32)


# ---------------------------------------------------------------- self-test

def self_test(sizes=("toy", "10M")) -> None:
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("transplant.py self-test: the known-answer tests for the patching code")
    torch.manual_seed(0)
    pairs = G.make_pairs(16, seed=3)
    recip = M.to_torch(G.batch([p["recipient"] for p in pairs]), "cpu")
    donor = M.to_torch(G.batch([p["donor"] for p in pairs]), "cpu")

    for size in sizes:
        for arm in M.ARMS:
            m = M.build(arm, size).eval()
            D = m.cfg.d_model
            last = m.cfg.n_states - 1
            sites = Sites(layers=(2, 3, last), positions="action+ans")
            mask = position_mask(recip, sites.positions)
            with torch.no_grad():
                clean = m(recip)
            own_states = capture(m, recip)
            null = transplanted_logits(m, recip, own_states, sites, mask, None)
            check(f"{size} arm {arm}: null transplant leaves every output bit-identical",
                  torch.equal(clean, null))
            d_states = capture(m, donor)
            whole = transplanted_logits(m, recip, d_states, sites, mask, None)
            as_sub = transplanted_logits(m, recip, d_states, sites, mask, torch.eye(D))
            check(f"{size} arm {arm}: the whole-state transplant is the subspace form at full rank",
                  torch.allclose(whole, as_sub, atol=1e-4),
                  f"largest difference {float((whole - as_sub).abs().max()):.2e}")
            rng = np.random.default_rng(0)
            b4 = orthonormal(rng.normal(size=(4, D)))
            comp = complement_basis(b4)
            both = transplanted_logits(m, recip, d_states, sites, mask,
                                       torch.cat([b4, comp], dim=1))
            check(f"{size} arm {arm}: a piece and its complement together are the whole state",
                  torch.allclose(whole, both, atol=1e-4) and comp.shape[1] == D - 4)
            empty = transplanted_logits(m, recip, d_states, Sites((), "action"), mask, None)
            check(f"{size} arm {arm}: an empty site set is a no-op", torch.equal(clean, empty))
            pre = before_both_twins(recip, donor)
            early = transplanted_logits(m, recip, d_states,
                                        Sites(tuple(range(m.cfg.n_states)), "pre"), pre, None)
            check(f"{size} arm {arm}: before both twins' first own turns the twins' states are "
                  f"identical, so a transplant there changes nothing (control 4)",
                  torch.equal(clean, early)
                  and all(torch.equal(d_states[l][pre], own_states[l][pre])
                          for l in range(m.cfg.n_states)))

        m = M.build("F", size).eval()
        all_sites = Sites(layers=tuple(range(m.cfg.n_states)), positions="all")
        everywhere = transplanted_logits(m, recip, capture(m, donor), all_sites,
                                         position_mask(recip, "all"), None)
        with torch.no_grad():
            donor_run = m(donor)
        check(f"{size}: every state at every position IS the donor's forward pass, so it is "
              f"no intervention and the family excludes it", torch.allclose(everywhere, donor_run, atol=1e-5))

    # the basis of a read is orthonormal and has the size asked for
    rng = np.random.default_rng(1)
    coef = rng.normal(size=(12, 160))
    ok = True
    for r in (1, 2, 4, 8):
        q = basis_for(coef, r)
        ok &= q.shape == (160, r) and torch.allclose(q.T @ q, torch.eye(r), atol=1e-5)
    check("a read's piece has orthonormal directions at sizes 1, 2, 4 and 8", ok)
    rb = random_bases(4, (1, 2), seed=0, D=160)
    check("control 3 draws twenty random pieces, reproducibly",
          len(rb) == 20 and torch.equal(rb[3][1], random_bases(4, (1, 2), seed=0, D=160)[3][1]))

    print(f"\n{len(fails)} failure(s)" if fails else "\nall checks passed")
    if fails:
        raise SystemExit(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--sizes", default="toy,10M")
    a = ap.parse_args()
    if a.self_test:
        self_test(tuple(a.sizes.split(",")))
    else:
        ap.print_help()
