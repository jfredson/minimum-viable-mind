"""Transplanting (activation patching), and its known-answer tests.

UNREGISTERED. The programme has never run this; the code did not exist before
this rehearsal (ruled 2026-09-20, and recorded in section 1 of
`docs/successor-experiment-proposal-2026-09-21.md`). It is built once, here,
and every intervention the successor design leans on is built from the single
hook in `arms.Arm.forward`.

The two transplants (proposal section 6.2)
------------------------------------------
A **site set** is a list of token positions and a list of layers, fixed before
anything is read. At those sites:

- **whole-state transplant** — replace the entire running-state vector with
  the donor's;
- **ownership-only transplant** — at the same sites, replace only the part of
  that vector lying in the nominated ownership subspace.

The second is a **restriction of the first to a subspace**, not a smaller or
different intervention. Both are the same function with a different projection
matrix, and the whole-state transplant is the special case where the
projection is the identity. `self_test` proves that rather than asserting it:
running the subspace form with a complete orthonormal basis reproduces the
whole-state form exactly.

Why the shape matters
---------------------
A reviewer's first objection to a measure of this shape is that the
whole-state transplant trivially wins because it moves more. Defining the two
as subspace and superspace at identical sites is the answer to that objection,
which is why the restriction property is checked as an identity on tensors and
not by eye.

Corrigibility: local, inference only, no network, no rented machine, $0.

    ../../../.venv/bin/python transplant.py --self-test
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np
import torch

import arms as A
import grammar as G


@dataclass(frozen=True)
class Sites:
    """Where a transplant happens. `layers` indexes the running state after
    the input embedding (0) and after each block (1 to n_layers)."""
    layers: tuple
    positions: str

    def label(self) -> str:
        return f"layers {'+'.join(str(l) for l in self.layers)} at {self.positions}"


POSITION_SETS = (
    "action",            # the own-directed action position only
    "action+ans",        # that position and the answer-cue token before it
    "action+3",          # that position and the three tokens before it
    "post-identity",     # every position from the model's first own turn on
    "all",               # every position — the degenerate limit, see below
    "pre-identity",      # before the identity can be known: control 4
)


def position_mask(b: dict, which: str) -> torch.Tensor:
    """(B, S) boolean mask of the positions a site set covers."""
    acting = b["acting"]
    B, S = acting.shape
    dev = acting.device
    ap = b["action_pos"][:, G.OWN]                              # (B,)
    idx = torch.arange(S, device=dev)[None].expand(B, -1)
    if which == "all":
        return torch.ones(B, S, dtype=torch.bool, device=dev)
    # first position at which the acting channel has fired
    first_own = torch.argmax(acting, dim=1)
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


def capture(model: A.Arm, b: dict) -> list:
    with torch.no_grad():
        _, states = model(b, capture=True)
    return states


def patch_fn_factory(donor_states, sites: Sites, mask: torch.Tensor,
                     basis: torch.Tensor | None, alpha: float = 1.0):
    """`basis` is (D, k) with orthonormal columns, a dict of one such matrix
    per layer, or None for the whole state.

    The ownership-only transplant is exactly this function with a rank-k
    basis; the whole-state transplant is exactly this function with the
    identity. Nothing else differs between them."""
    m = mask.unsqueeze(-1)

    def fn(layer_index, state):
        if layer_index not in sites.layers:
            return state
        donor = donor_states[layer_index]
        b = basis[layer_index] if isinstance(basis, dict) else basis
        if b is None:
            moved = donor
        else:
            delta = donor - state
            moved = state + (delta @ b) @ b.T
        if alpha != 1.0:
            moved = state + alpha * (moved - state)
        return torch.where(m, moved, state)

    return fn


def transplanted_logits(model: A.Arm, recipient: dict, donor_states,
                        sites: Sites, mask: torch.Tensor,
                        basis: torch.Tensor | None,
                        alpha: float = 1.0) -> torch.Tensor:
    with torch.no_grad():
        return model(recipient,
                     patch_fn=patch_fn_factory(donor_states, sites, mask, basis, alpha))


def predictions(logits: torch.Tensor, condition: int = G.OWN) -> torch.Tensor:
    """The value word the model emits at one of its two action positions.
    Restricted to the eight value slots, which is what an action in this
    grammar can be."""
    slot_ids = torch.as_tensor(G.SLOT_IDS, device=logits.device)
    sub = logits[:, condition][:, slot_ids]
    return slot_ids[sub.argmax(dim=-1)]


def orthonormal(vectors: np.ndarray) -> torch.Tensor:
    """Orthonormal basis (D, k) for the row space of `vectors` (k, D)."""
    q, _ = np.linalg.qr(vectors.T)
    return torch.as_tensor(np.ascontiguousarray(q), dtype=torch.float32)


# ---------------------------------------------------------------- self-test

def self_test() -> None:
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("transplant.py self-test — the known-answer tests for the patching code")
    torch.manual_seed(0)
    pairs = G.make_pairs(16, seed=3)
    recip = A.to_torch(G.batch([p["recipient"] for p in pairs]), "cpu")
    donor = A.to_torch(G.batch([p["donor"] for p in pairs]), "cpu")

    for arm in A.ARMS:
        m = A.Arm(A.Config(arm=arm)).eval()
        D = m.cfg.d_model
        sites = Sites(layers=(2, 3, 4), positions="action+ans")
        mask = position_mask(recip, sites.positions)
        base = torch.no_grad()
        with torch.no_grad():
            clean = m(recip)

        # --- 1. the null transplant: the recipient's own state into itself
        own_states = capture(m, recip)
        null = transplanted_logits(m, recip, own_states, sites, mask, None)
        check(f"arm {arm} — null transplant leaves every logit bit-identical",
              torch.equal(clean, null))

        # --- 2. the restriction property, proved rather than asserted
        eye = torch.eye(D)
        d_states = capture(m, donor)
        whole = transplanted_logits(m, recip, d_states, sites, mask, None)
        as_subspace = transplanted_logits(m, recip, d_states, sites, mask, eye)
        check(f"arm {arm} — the whole-state transplant is the subspace form at full rank",
              torch.allclose(whole, as_subspace, atol=1e-4),
              f"largest logit difference {float((whole - as_subspace).abs().max()):.2e}")

        # --- 3. a rank-k subspace moves strictly less than the whole state
        rng = np.random.default_rng(0)
        b4 = orthonormal(rng.normal(size=(4, D)))
        part = transplanted_logits(m, recip, d_states, sites, mask, b4)
        d_whole = float((whole - clean).abs().mean())
        d_part = float((part - clean).abs().mean())
        check(f"arm {arm} — a rank-4 subspace moves the output less than the whole state",
              d_part <= d_whole + 1e-6,
              f"mean logit movement: whole {d_whole:.4f}, rank-4 {d_part:.4f}")

        # --- 4. a transplant outside the site set changes nothing
        empty = Sites(layers=(), positions="action")
        none_ = transplanted_logits(m, recip, d_states, empty, mask, None)
        check(f"arm {arm} — an empty site set is a no-op", torch.equal(clean, none_))

    # --- 5. the degenerate limit, named so it cannot be walked into ---------
    m = A.Arm(A.Config(arm="F")).eval()
    all_sites = Sites(layers=tuple(range(m.cfg.n_layers + 1)), positions="all")
    all_mask = position_mask(recip, "all")
    d_states = capture(m, donor)
    everywhere = transplanted_logits(m, recip, d_states, all_sites, all_mask, None)
    with torch.no_grad():
        donor_run = m(donor)
    check("transplanting every layer at every position IS the donor's forward pass",
          torch.allclose(everywhere, donor_run, atol=1e-5),
          "so a whole-state transplant at that site set is not an intervention at "
          "all, and its accuracy is guaranteed by construction rather than measured")

    print(f"\n{len(fails)} failure(s)" if fails else "\nall checks passed")
    if fails:
        raise SystemExit(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test()
    else:
        ap.print_help()
