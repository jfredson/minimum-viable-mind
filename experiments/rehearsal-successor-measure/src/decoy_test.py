"""The decoy test (page 10 of the Gate A addendum; the ChatGPT outside review
of version 4, finding A6): can the registered nomination and reading be fooled
by an easily read but causally unused copy of the owner's marker?

Method, committed before this file produced any output:
`docs/decoy-test-method-2026-10-06.md`. Read it first.

What this does
--------------
It takes the committed separable toy model (arm T, seeds 0, 1 and 2, checked
against SHA256SUMS) and widens its running state from 160 to 184 numbers:

    [ content (136) | decoy (24) | ownership block (24) ]

The decoy is `scale` times the vector the model writes into its ownership
block (the owner's marker, as the model computes it from the acting channel),
recomputed from the episode's input at every running state. After the
transplant hook has run on a running state, the decoy coordinates are thrown
away: the blocks and the action head receive exactly the content and the
ownership block, as in the unwidened model. So nothing downstream reads the
decoy, by construction, and the checks below confirm it.

Then the FROZEN measurement procedure
(`experiments/08-successor-degree/src/procedure.py`, `run_model`) runs on the
widened model unchanged: the one fit of the straight-line reads, the
nomination, the reading on fresh episodes, the controls, the withholding of a
reading (`summarise`). The only thing replaced is the function that loads a
model from a file, so that it hands back the widened model.

This is a CONSTRUCTED STAND-IN, not a trained model.

    python decoy_test.py --checks-only            # the checks, no reading
    python decoy_test.py --scale 4 --seeds 0 1 2  # one orientation
    python decoy_test.py --report                 # the table from what is on disk

Laptop, processor only, $0. Writes only into ../out-decoy-test/.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import sys
import time

import numpy as np
import torch
import torch.nn as nn

HERE = os.path.dirname(os.path.abspath(__file__))
REH = os.path.abspath(os.path.join(HERE, ".."))
FROZEN = os.path.abspath(os.path.join(REH, "..", "08-successor-degree", "src"))
sys.path.insert(0, FROZEN)
import grammar as G          # noqa: E402  (frozen)
import measure as MS         # noqa: E402  (frozen)
import models as M           # noqa: E402  (frozen)
import procedure as P        # noqa: E402  (frozen)
import transplant as X       # noqa: E402  (frozen)

MODELS = os.path.join(REH, "out-repairs", "models")
OUT = os.path.join(REH, "out-decoy-test")
D_OWN = 24
THREADS = 4          # the other session on the laptop keeps the rest; recorded in every output

# The verdict thresholds of the method note, section 6. Fixed before any output.
NEAR_ZERO = 0.20
FOOLED_AT = 0.50
MOSTLY_IN_COPY = 0.50


class DecoyArmT(nn.Module):
    """Arm T with an unused, exact copy of its ownership answer appended.
    Exposes what the frozen procedure uses: `cfg` (with `arm`, `d_model`,
    `d_content`, `n_states`), and `forward(b, patch_fn=None, capture=False)`."""

    def __init__(self, base: nn.Module, scale: float):
        super().__init__()
        assert base.cfg.arm == "T"
        self.base = base.eval()
        self.scale = float(scale)
        self.dc = base.cfg.d_content               # 136
        self.cfg = copy.deepcopy(base.cfg)
        # d_model 184 and d_own 24, so cfg.d_content = 160: the frozen
        # procedure's true-slot reference (columns d_content onward) is then
        # the ownership block alone, and excludes the decoy.
        self.cfg.d_model = base.cfg.d_model + D_OWN
        assert self.cfg.d_content == self.dc + D_OWN

    def _widen(self, x, own_slot, decoy):
        return torch.cat([x, decoy, own_slot], dim=-1)

    def _split(self, state):
        # the decoy coordinates, state[..., dc:dc+24], are discarded here
        return state[..., :self.dc], state[..., self.dc + D_OWN:]

    def forward(self, b, patch_fn=None, capture: bool = False):
        m = self.base
        B, S = b["tokens"].shape
        own_vec, _ = m._own_vec(b)
        decoy = self.scale * own_vec               # an exact copy of the owner's marker, scaled
        x = m._embed(b, own_vec)
        causal = torch.triu(torch.ones(S, S, dtype=torch.bool, device=x.device), 1)
        states = []
        state = self._widen(x, own_vec, decoy)
        if patch_fn is not None:
            state = patch_fn(0, state)
        if capture:
            states.append(state)
        x, own_slot = self._split(state)
        for li, blk in enumerate(m.blocks):
            x = blk(x, causal, own_vec)
            state = self._widen(x, own_slot, decoy)
            if patch_fn is not None:
                state = patch_fn(li + 1, state)
            if capture:
                states.append(state)
            x, own_slot = self._split(state)
        h = m.lnf(x)
        logits = m._separable_logits(b, h, own_slot)
        return (logits, states) if capture else logits


def ckpt_path(seed: int) -> str:
    return os.path.join(MODELS, f"ckpt_T_base_seed{seed}.pt")


def sha_ok(seed: int) -> bool:
    want = dict(reversed(line.split()) for line in open(os.path.join(MODELS, "SHA256SUMS")))
    p = ckpt_path(seed)
    return hashlib.sha256(open(p, "rb").read()).hexdigest() == want[os.path.basename(p)]


def load_base(seed: int):
    assert sha_ok(seed), f"arm T seed {seed} does not match SHA256SUMS: stop (K1)"
    return P.load_model(ckpt_path(seed), "T", "toy")


def out_dir(scale: float) -> str:
    return os.path.join(OUT, f"scale_{scale:g}")


# ------------------------------------------------------------------ checks

@torch.no_grad()
def checks(seed: int, scale: float, data: P.EvalData) -> dict:
    """Method note, section 3: the decoy is causally unused, the widened model
    is the committed model, and the decoy is an exact, easily read copy."""
    base, _ = load_base(seed)
    dm = DecoyArmT(base, scale).eval()
    recip, donor = data.fresh
    dc = dm.dc
    out = dict(seed=seed, scale=scale)
    # (a) the widened model gives bit-identical outputs to the committed one
    out["a_outputs_bit_identical_to_committed_model"] = bool(torch.equal(base(recip), dm(recip)))
    # (b) transplanting the donor's decoy alone, at every running state and
    #     every position, changes no output bit
    d_states = X.capture(dm, donor)
    eye = torch.eye(dm.cfg.d_model)[:, dc:dc + D_OWN]
    sites = X.Sites(tuple(range(dm.cfg.n_states)), "all")
    mask = X.position_mask(recip, "all")
    moved = X.transplanted_logits(dm, recip, d_states, sites, mask, {l: eye for l in sites.layers})
    out["b_decoy_only_transplant_bit_identical"] = bool(torch.equal(dm(recip), moved))
    # (b') overwrite the decoy with large random numbers everywhere: still bit-identical
    g = torch.Generator().manual_seed(20261006 + seed)

    def noise(li, st):
        st = st.clone()
        st[..., dc:dc + D_OWN] = 100.0 * torch.randn(st[..., dc:dc + D_OWN].shape, generator=g)
        return st
    out["b2_decoy_overwritten_with_noise_bit_identical"] = bool(torch.equal(dm(recip), dm(recip, patch_fn=noise)))
    # (c) the decoy is an exact copy: decoy == scale * ownership block at every state, every position
    _, st = dm(recip, capture=True)
    out["c_decoy_equals_scale_times_block_everywhere"] = all(
        bool(torch.equal(s[..., dc:dc + D_OWN], scale * s[..., dc + D_OWN:])) for s in st)
    # (d) the decoy alone is easily read: held-out count of a straight-line
    #     read of the owner's marker from the decoy alone, and from the block
    #     alone, at the own-directed action, development episodes (frozen fit)
    dev, _ = data.dev
    hs, _ = P.action_states(dm, dev, G.OWN)
    y = P.read_labels(dev, "own")
    out["d_decoy_alone_correct_of_180_by_state"] = [P.correct_count(h[:, dc:dc + D_OWN], y) for h in hs]
    out["d_block_alone_correct_of_180_by_state"] = [P.correct_count(h[:, dc + D_OWN:], y) for h in hs]
    # (e) the true ownership block transplanted alone moves the action fully,
    #     and the decoy alone moves nothing: the used slot is the block
    d_tgt = donor["targets"][:, G.OWN]
    clean = dm(recip)
    u = float(P.hits(clean, d_tgt, G.OWN).mean())
    acc = float(P.hits(clean, recip["targets"][:, G.OWN], G.OWN).mean())
    s0 = X.Sites((0,), "action")
    m0 = X.position_mask(recip, "action")
    blk = torch.eye(dm.cfg.d_model)[:, dc + D_OWN:]
    w = float(P.hits(X.transplanted_logits(dm, recip, d_states, s0, m0, None), d_tgt, G.OWN).mean())
    ob = float(P.hits(X.transplanted_logits(dm, recip, d_states, s0, m0, {0: blk}), d_tgt, G.OWN).mean())
    od = float(P.hits(X.transplanted_logits(dm, recip, d_states, s0, m0, {0: eye}), d_tgt, G.OWN).mean())
    out["e_at_state_0_action"] = dict(whole=w, block_only=ob, decoy_only=od, untouched=u, own_accuracy=acc,
                                      reading_with_block=MS.reading(w, ob, u, acc)["degree"],
                                      reading_with_decoy=MS.reading(w, od, u, acc)["degree"])
    out["all_hold"] = (out["a_outputs_bit_identical_to_committed_model"]
                       and out["b_decoy_only_transplant_bit_identical"]
                       and out["b2_decoy_overwritten_with_noise_bit_identical"]
                       and out["c_decoy_equals_scale_times_block_everywhere"])
    return out


# ------------------------------------------------------------------ the run

def run(scale: float, seeds, data: P.EvalData) -> None:
    od = out_dir(scale)
    os.makedirs(od, exist_ok=True)
    for seed in seeds:
        c = checks(seed, scale, data)
        with open(os.path.join(od, f"checks_T_seed{seed}.json"), "w") as f:
            json.dump(c, f, indent=1, default=P._json_default)
        P.log(f"[scale {scale:g} T/{seed}] checks: all hold {c['all_hold']}; decoy alone reads "
              f"{c['d_decoy_alone_correct_of_180_by_state']}, block alone {c['d_block_alone_correct_of_180_by_state']}")
        if not c["all_hold"]:
            raise SystemExit(f"STOP (K2): a check that the decoy is unused or exact failed: {c}")
        base, meta = load_base(seed)
        dm = DecoyArmT(base, scale).eval()
        orig = P.load_model
        P.load_model = lambda ckpt, arm, size: (dm, dict(meta, decoy=dict(
            scale=scale, layout="[content 136 | decoy 24 | ownership block 24]",
            constructed_stand_in="NOT A TRAINED MODEL")))
        try:
            P.run_model(ckpt_path(seed), od, "T", "toy", seed, None, MS.N_SHUFFLES, 1.0, False, data)
        finally:
            P.load_model = orig
        # add what the frozen row does not carry: where the chosen piece lies
        rp = os.path.join(od, f"row_T_seed{seed}.json")
        row = json.load(open(rp))
        row["decoy_test"] = piece_location(row, od, seed, dm)
        row["decoy_test"]["threads"] = THREADS
        with open(rp, "w") as f:
            json.dump(row, f, indent=1, sort_keys=True, default=P._json_default)
    P.summarise(od)


def piece_location(row, od, seed, dm) -> dict:
    """For the chosen site set: the share of the transplanted piece lying in
    the decoy coordinates (squared norm of the basis restricted to them, over
    the piece's size), and the same for the ownership block and the content;
    and the share of the fitted read's squared weight on each, at every state."""
    reads = P.load_reads(os.path.join(od, f"reads_T_seed{seed}.npz"))["own"]
    dc = dm.dc
    parts = dict(content=slice(0, dc), decoy=slice(dc, dc + D_OWN), block=slice(dc + D_OWN, dc + 2 * D_OWN))

    def shares(mat):
        tot = float((mat ** 2).sum())
        return {k: float((mat[s] ** 2).sum()) / tot for k, s in parts.items()}

    weight = {str(l): shares((c - c.mean(axis=0, keepdims=True)).T) for l, c in reads.items()}
    spec = row["nomination"]["primary"]["site_set"]
    piece = None
    if spec is not None:
        piece = {str(l): shares(X.basis_for(reads[l], spec["rank"]).numpy()) for l in spec["layers"]}
    return dict(read_weight_share_by_state=weight, chosen_piece_share=piece,
                expected_decoy_weight_share_if_split_by_scale=dm.scale ** 2 / (1 + dm.scale ** 2))


# ------------------------------------------------------------------ report

def classify(rows) -> dict:
    """Method note, section 6: one orientation's verdict from its three seeds."""
    readings = [r["status"] == "reading" for r in rows]
    deg = [r["degree"] for r in rows]
    in_copy = [r["piece_in_decoy"] for r in rows]
    if sum(readings) < 2:
        return dict(verdict="inconclusive", reason="fewer than two seeds returned a reading")
    hi = [i for i, r in enumerate(rows) if readings[i] and deg[i] >= FOOLED_AT]
    if len(hi) >= 2:
        if all(in_copy[i] is not None and in_copy[i] > MOSTLY_IN_COPY for i in hi):
            return dict(verdict="fooled", reason=f"two or more seeds read {FOOLED_AT} or more with the piece mostly in the copy")
        return dict(verdict="inconclusive",
                    reason="two or more seeds read high but the piece is not mostly in the copy: the read fails for another reason")
    if all((not readings[i]) or deg[i] <= NEAR_ZERO for i in range(len(rows))) and sum(
            readings[i] and deg[i] <= NEAR_ZERO for i in range(len(rows))) >= 2:
        return dict(verdict="not fooled", reason=f"every seed that reads, and at least two, reads {NEAR_ZERO} or less")
    return dict(verdict="inconclusive", reason="readings between the two bands, or split across them")


def report() -> None:
    lines = ["| orientation (decoy scale) | seed | reading or no verdict | site set | piece share in decoy / block / content | "
             "read's weight share in decoy at the chosen state | whole, ownership-only, untouched (fresh) | true-slot reference | decoy checks hold; decoy alone reads (by state) |",
             "|" + "---|" * 9]
    verdicts = {}
    for d in sorted(os.listdir(OUT)):
        if not d.startswith("scale_"):
            continue
        od = os.path.join(OUT, d)
        if not os.path.exists(os.path.join(od, "summary.json")):
            continue
        summ = json.load(open(os.path.join(od, "summary.json")))
        rows = []
        for seed in (0, 1, 2):
            rp = os.path.join(od, f"row_T_seed{seed}.json")
            if not os.path.exists(rp):
                continue
            r = json.load(open(rp))
            c = json.load(open(os.path.join(od, f"checks_T_seed{seed}.json")))
            w = summ["per_seed"]["T"][str(seed)]
            p = r.get("primary") or {}
            sp = (p.get("site_set") or {})
            dt = r["decoy_test"]
            pc = dt["chosen_piece_share"] or {}
            worst = None
            if pc:
                worst = max(pc.values(), key=lambda v: v["decoy"])
            rd = p.get("reading") or {}
            verdict = f"{w['degree']:.4f}" if w["status"] == "reading" else "no verdict: " + "; ".join(w["reasons"])
            lw = dt["read_weight_share_by_state"][str(sp["layers"][0])]["decoy"] if sp else None
            lines.append(
                f"| {d.removeprefix('scale_')} | {seed} | {verdict} | "
                f"{'' if not sp else f'states {tuple(sp['layers'])} at {sp['positions']}, {sp['rank']} directions'} | "
                f"{'' if not worst else f'{worst['decoy']:.4f} / {worst['block']:.4f} / {worst['content']:.4f}'} | "
                f"{'' if lw is None else f'{lw:.4f}'} | "
                f"{'' if not rd else f'{rd['accuracy_whole']:.4f}, {rd['accuracy_ownership_only']:.4f}, {rd['accuracy_untouched']:.4f}'} | "
                f"{'' if not p.get('true_slot') else P._deg(p['true_slot']['reading']['degree'])} | "
                f"{c['all_hold']}; {c['d_decoy_alone_correct_of_180_by_state']} |")
            rows.append(dict(status=w["status"], degree=w.get("degree"),
                             piece_in_decoy=None if not worst else worst["decoy"]))
        if rows:
            verdicts[d.removeprefix("scale_")] = dict(classify(rows), seeds=len(rows))
    lines += ["", "verdict by orientation (method note, section 6):"]
    lines += [f"- decoy scale {k}: {v['verdict']} ({v['reason']})" for k, v in verdicts.items()]
    txt = "\n".join(lines)
    with open(os.path.join(OUT, "table.md"), "w") as f:
        f.write(txt + "\n")
    with open(os.path.join(OUT, "verdicts.json"), "w") as f:
        json.dump(verdicts, f, indent=1)
    print(txt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scale", type=float)
    ap.add_argument("--seeds", type=int, nargs="+", default=[0, 1, 2])
    ap.add_argument("--checks-only", action="store_true")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    torch.set_num_threads(THREADS)
    if a.report:
        report()
        return
    t0 = time.time()
    data = P.EvalData(1.0)
    if a.checks_only:
        os.makedirs(OUT, exist_ok=True)
        res = [checks(s, sc, data) for sc in (4.0, 0.25) for s in a.seeds]
        with open(os.path.join(OUT, "checks_only.json"), "w") as f:
            json.dump(dict(results=res, versions=P.versions(), threads=THREADS), f, indent=1,
                      default=P._json_default)
        for r in res:
            print(json.dumps(r, default=P._json_default))
        return
    run(a.scale, a.seeds, data)
    P.log(f"done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
