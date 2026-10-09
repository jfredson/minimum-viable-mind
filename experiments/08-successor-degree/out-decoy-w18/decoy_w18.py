"""The test of a differently coded decoy (weakness W18 of version 5 of the
registration text; ruled 2026-10-08, item 8 of
`docs/rulings/2026-10-08-v5-open-items-rulings.md`): can an unused code of the
owner's marker word, coded differently from the ownership block the model acts
on, pull the registered read away from the block, so that the separable toy
model (arm T) reads as partly or fully entangled?

Method, committed before this file was written:
`docs/2026-10-08-decoy-w18-method.md`. Read it first.

What this does
--------------
It takes the committed arm T toy models (seeds 0, 1 and 2, checked against
SHA256SUMS) and widens the running state from 160 to 180 numbers:

    [ content (136) | decoy code (20) | ownership block (24) ]

The decoy code has one number per marker word. Soft code (variants V1 to V4):
the weight the model's own ownership answer puts on the agent carrying that
word, times `k` (the check of the ruled decoy test's probe 3, exactly). Hard
code (V5): `k` on the word of the agent the acting channel has tallied most so
far, 0 elsewhere, all 0 before the model's first own turn. `k` is the scale
times the block's root-mean-square size at the own-directed action on the 600
development recipients. After the transplant hook has run on a running state
the code is thrown away: the blocks and the action head receive exactly the
content and the ownership block, as in the committed model.

Then the FROZEN measurement procedure (`../src/procedure.py`, `run_model`, as
ruled on 2026-10-08: reads fitted on 1,800 of 1,980 development episodes,
iteration limit 10,000) runs on the widened model unchanged. The only thing
replaced is the function that loads a model from a file, for the length of
each call, so that it hands back the widened model.

This is a CONSTRUCTED STAND-IN, not a trained model.

    python decoy_w18.py --checks-only        # the checks, every variant, no reading
    python decoy_w18.py --variant V1         # one variant, three seeds
    python decoy_w18.py --report             # the table and verdicts from what is on disk
    python decoy_w18.py --smoke DIR          # pipeline test at tiny episode counts; never a figure

Laptop, processor only, $0. Writes only beside this file (or into DIR for --smoke).
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
import torch.nn.functional as F

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "src"))
sys.path.insert(0, SRC)
import grammar as G          # noqa: E402  (frozen)
import measure as MS         # noqa: E402  (frozen)
import procedure as P        # noqa: E402  (frozen)
import transplant as X       # noqa: E402  (frozen)

MODELS = os.path.abspath(os.path.join(HERE, "..", "..", "rehearsal-successor-measure", "out-repairs", "models"))
OUT = HERE
N_CODE = len(G.MARKERS)                                  # 20 marker words
MARKER_IDS = torch.as_tensor([G.VOCAB[w] for w in G.MARKERS])
D_OWN = 24

# The variants of the method note, section 3. Fixed before any output.
VARIANTS = {
    "V1": dict(kind="soft", scale=4.0, in_verdict=True),
    "V2": dict(kind="soft", scale=0.25, in_verdict=True),
    "V3": dict(kind="soft", scale=16.0, in_verdict=False),
    "V4": dict(kind="soft", scale=1.0, in_verdict=False),
    "V5": dict(kind="hard", scale=4.0, in_verdict=False),
}

# The bands of the method note, section 7 (the ruled decoy test's, unchanged).
NEAR_ZERO = 0.20
FOOLED_AT = 0.50
FULLY_FOOLED_AT = 0.80
MOSTLY_IN_CODE = 0.50


class CodeDecoyArmT(nn.Module):
    """Arm T with an unused code of the owner's marker word appended at every
    running state and position, discarded before every block and the head.
    Exposes what the frozen procedure uses: `cfg` (d_model 180, so d_content
    156 and the true-slot reference is the ownership block alone), `forward`,
    and, through the committed model, the ownership answer's parts that the
    gate's in-use check and row-choice split read."""

    def __init__(self, base: nn.Module, k: float, kind: str):
        super().__init__()
        assert base.cfg.arm == "T" and kind in ("soft", "hard")
        self.base = base.eval()
        self.k = float(k)
        self.kind = kind
        self.dc = base.cfg.d_content                      # 136
        self.cfg = copy.deepcopy(base.cfg)
        self.cfg.d_model = base.cfg.d_model + N_CODE
        assert self.cfg.d_content == self.dc + N_CODE

    def __getattr__(self, name):
        try:
            return super().__getattr__(name)
        except AttributeError:
            return getattr(super().__getattr__("base"), name)

    def named_parameters(self, *a, **kw):
        return self.base.named_parameters(*a, **kw)

    def code(self, b):
        """(B, S, 20): the decoy code at every position."""
        idx = (b["agent_marker_tok"].unsqueeze(-1) == MARKER_IDS).float()   # (B, agents, 20)
        assert torch.all(idx.sum(-1) == 1)
        if self.kind == "soft":
            _, p_own = self.base._own_vec(b)                                  # (B, S, agents)
            w = p_own
        else:
            agent_at = b["assign_agent_at"]
            one = F.one_hot(agent_at.clamp(min=0), G.N_AGENTS).float() * (agent_at >= 0).float().unsqueeze(-1)
            tally = torch.cumsum(one * b["acting"].float().unsqueeze(-1), dim=1)
            w = F.one_hot(tally.argmax(-1), G.N_AGENTS).float() * (tally.sum(-1, keepdim=True) > 0).float()
        return self.k * torch.bmm(w, idx)

    def _widen(self, x, code, own_slot):
        return torch.cat([x, code, own_slot], dim=-1)

    def _split(self, state):
        # the code numbers, state[..., dc:dc+20], are discarded here
        return state[..., :self.dc], state[..., self.dc + N_CODE:]

    def forward(self, b, patch_fn=None, capture: bool = False):
        m = self.base
        B, S = b["tokens"].shape
        own_vec, _ = m._own_vec(b)
        code = self.code(b)
        x = m._embed(b, own_vec)
        causal = torch.triu(torch.ones(S, S, dtype=torch.bool, device=x.device), 1)
        states = []
        state = self._widen(x, code, own_vec)
        if patch_fn is not None:
            state = patch_fn(0, state)
        if capture:
            states.append(state)
        x, own_slot = self._split(state)
        for li, blk in enumerate(m.blocks):
            x = blk(x, causal, own_vec)
            state = self._widen(x, code, own_slot)
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
    if not sha_ok(seed):
        raise SystemExit(f"STOP (K1): arm T seed {seed} does not match SHA256SUMS")
    return P.load_model(ckpt_path(seed), "T", "toy")


@torch.no_grad()
def block_rms(base, data) -> float:
    """The block's root-mean-square size at the own-directed action, on the 600
    development recipients (as the check's probe 3 computed it)."""
    dev = data.dev[0]
    rows = torch.arange(dev["tokens"].shape[0])
    own_vec, _ = base._own_vec(dev)
    return float(own_vec[rows, dev["action_pos"][:, G.OWN]].pow(2).sum(-1).mean().sqrt())


def build(seed: int, variant: str, data):
    base, meta = load_base(seed)
    v = VARIANTS[variant]
    r = block_rms(base, data)
    dm = CodeDecoyArmT(base, v["scale"] * r, v["kind"]).eval()
    return base, meta, dm, dict(variant=variant, kind=v["kind"], scale=v["scale"], k=v["scale"] * r, block_rms=r)


def parts(dm) -> dict:
    dc = dm.dc
    return dict(content=slice(0, dc), code=slice(dc, dc + N_CODE), block=slice(dc + N_CODE, dc + N_CODE + D_OWN))


# ------------------------------------------------------------------ checks

@torch.no_grad()
def checks(seed: int, variant: str, data) -> dict:
    """Method note, section 3: the code is causally unused, the widened model
    is the committed model, and the code is what the note says it is."""
    base, _, dm, info = build(seed, variant, data)
    recip, donor = data.fresh
    dc, k = dm.dc, dm.k
    out = dict(seed=seed, **info)
    # (a) bit-identical outputs
    out["a_outputs_bit_identical_to_committed_model"] = bool(torch.equal(base(recip), dm(recip)))
    # (b) transplanting the donor's code alone, every state, every position
    d_states = X.capture(dm, donor)
    eye_code = torch.eye(dm.cfg.d_model)[:, dc:dc + N_CODE]
    sites = X.Sites(tuple(range(dm.cfg.n_states)), "all")
    mask = X.position_mask(recip, "all")
    moved = X.transplanted_logits(dm, recip, d_states, sites, mask, {l: eye_code for l in sites.layers})
    out["b_code_only_transplant_bit_identical"] = bool(torch.equal(dm(recip), moved))
    # (b') noise in the code everywhere
    g = torch.Generator().manual_seed(20261008 + seed)

    def noise(li, st):
        st = st.clone()
        st[..., dc:dc + N_CODE] = 100.0 * torch.randn(st[..., dc:dc + N_CODE].shape, generator=g)
        return st
    out["b2_code_overwritten_with_noise_bit_identical"] = bool(torch.equal(dm(recip), dm(recip, patch_fn=noise)))
    # (c) the code is what the method says
    code = dm.code(recip)
    rows = torch.arange(recip["tokens"].shape[0])
    at_act = code[rows, recip["action_pos"][:, G.OWN]]
    owner_word = torch.as_tensor(P.read_labels(recip, "own"))
    owner_idx = (owner_word.unsqueeze(-1) == MARKER_IDS).float().argmax(-1)
    out["c_largest_at_action_is_owner_word"] = bool(torch.equal(at_act.argmax(-1), owner_idx))
    out["c_within_0_and_k"] = bool(float(code.min()) >= 0.0 and float(code.max()) <= k * (1 + 1e-6))
    sums = code.sum(-1)
    if dm.kind == "soft":
        out["c_sums_to_k"] = bool(torch.allclose(sums, torch.full_like(sums, k), rtol=1e-5, atol=1e-5))
    else:
        out["c_sums_to_k"] = bool(torch.all(((sums - k).abs() < 1e-4 * k) | (sums == 0))) and bool(
            torch.all(sums[rows, recip["action_pos"][:, G.OWN]] > 0))
    out["c_holds"] = out["c_largest_at_action_is_owner_word"] and out["c_within_0_and_k"] and out["c_sums_to_k"]
    out["code_words_ever_set"] = int((code.amax(dim=(0, 1)) > 0).sum())
    out["owner_weight_at_action_mean"] = float(at_act.max(-1).values.mean() / k)
    # (d) reported: the code alone and the block alone are easily read
    pool = data.read_pool
    hs, _ = P.action_states(dm, pool, G.OWN)
    y = P.read_labels(pool, "own")
    pr = parts(dm)
    out["d_code_alone_correct_by_state"] = [P.correct_count(h[:, pr["code"]], y, "checks") for h in hs]
    out["d_block_alone_correct_by_state"] = [P.correct_count(h[:, pr["block"]], y, "checks") for h in hs]
    out["d_of"] = data.held_out
    # (e) reported: at state 0, the action position
    d_tgt = donor["targets"][:, G.OWN]
    clean = dm(recip)
    u = float(P.hits(clean, d_tgt, G.OWN).mean())
    acc = float(P.hits(clean, recip["targets"][:, G.OWN], G.OWN).mean())
    s0 = X.Sites((0,), "action")
    m0 = X.position_mask(recip, "action")
    blk = torch.eye(dm.cfg.d_model)[:, pr["block"]]
    w = float(P.hits(X.transplanted_logits(dm, recip, d_states, s0, m0, None), d_tgt, G.OWN).mean())
    ob = float(P.hits(X.transplanted_logits(dm, recip, d_states, s0, m0, {0: blk}), d_tgt, G.OWN).mean())
    oc = float(P.hits(X.transplanted_logits(dm, recip, d_states, s0, m0, {0: eye_code}), d_tgt, G.OWN).mean())
    out["e_at_state_0_action"] = dict(whole=w, block_only=ob, code_only=oc, untouched=u, own_accuracy=acc,
                                      reading_with_block=MS.reading(w, ob, u, acc)["degree"],
                                      reading_with_code=MS.reading(w, oc, u, acc)["degree"])
    # (f) the frozen gate record is the same for the widened and the committed model
    gb = json.dumps(P.gate(base, "T", data), sort_keys=True, default=P._json_default)
    gd = json.dumps(P.gate(dm, "T", data), sort_keys=True, default=P._json_default)
    out["f_gate_record_identical"] = gb == gd
    out["all_hold"] = bool(out["a_outputs_bit_identical_to_committed_model"]
                           and out["b_code_only_transplant_bit_identical"]
                           and out["b2_code_overwritten_with_noise_bit_identical"]
                           and out["c_holds"] and out["f_gate_record_identical"])
    return out


# ------------------------------------------------------------------ reporting beside the frozen row

@torch.no_grad()
def unmoved_share(dm, data, layer: int, basis) -> float:
    """Share (by squared size, pooled over the fresh pairs) of the block's
    donor-minus-recipient difference at `layer`, own-directed action, that a
    transplant along `basis` leaves unmoved (the check's probe 1 measure)."""
    recip, donor = data.fresh
    rs = X.capture(dm, recip)[layer]
    ds = X.capture(dm, donor)[layer]
    rows = torch.arange(recip["tokens"].shape[0])
    ap = recip["action_pos"][:, G.OWN]
    d = (ds[rows, ap] - rs[rows, ap]).double()
    bb = basis.double()
    mv = (d @ bb) @ bb.T
    blk = parts(dm)["block"]
    den = float((d[:, blk] ** 2).sum())
    return float(((d[:, blk] - mv[:, blk]) ** 2).sum()) / den if den > 0 else float("nan")


@torch.no_grad()
def beside(row, od, seed, dm, data) -> dict:
    reads = P.load_reads(os.path.join(od, f"reads_T_seed{seed}.npz"))["own"]
    pr = parts(dm)

    def shares(mat):
        tot = float((mat ** 2).sum())
        return {k: float((mat[s] ** 2).sum()) / tot for k, s in pr.items()}

    out = dict(read_weight_share_by_state={str(l): shares((c - c.mean(axis=0, keepdims=True)).T)
                                           for l, c in reads.items()})
    spec = row["nomination"]["primary"]["site_set"]
    if spec is None:
        spec = row["nomination"]["piece_rule_switched_off"]
        out["site_set_used_here"] = "piece_rule_switched_off (no nominated site set)"
    if spec is None:
        return out
    L = tuple(spec["layers"])
    out["chosen_piece_share"] = {str(l): shares(X.basis_for(reads[l], spec["rank"]).numpy()) for l in L}
    out["block_change_left_unmoved"] = {str(l): unmoved_share(dm, data, l, X.basis_for(reads[l], spec["rank"]))
                                        for l in L}
    # the readings at every size at the chosen site set, on fresh pairs (what the probe reported)
    recip, donor = data.fresh
    d_states = X.capture(dm, donor)
    d_tgt = donor["targets"][:, G.OWN]
    clean = dm(recip)
    u = float(P.hits(clean, d_tgt, G.OWN).mean())
    acc = float(P.hits(clean, recip["targets"][:, G.OWN], G.OWN).mean())
    sites = X.Sites(L, spec["positions"])
    mask = X.position_mask(recip, spec["positions"])
    w = float(P.hits(X.transplanted_logits(dm, recip, d_states, sites, mask, None), d_tgt, G.OWN).mean())
    by_size = {}
    for r in MS.RANK_CAPS:
        basis = {l: X.basis_for(reads[l], r) for l in L}
        o = float(P.hits(X.transplanted_logits(dm, recip, d_states, sites, mask, basis), d_tgt, G.OWN).mean())
        bn = np.concatenate([basis[l].numpy() for l in L], axis=1)
        by_size[str(r)] = dict(ownership_only=o, reading=MS.reading(w, o, u, acc)["degree"],
                               piece_share=shares(bn))
    out["fresh_readings_by_size_at_chosen_site"] = by_size
    return out


# ------------------------------------------------------------------ the run

def run(variant: str, seeds, data, od: str, shuffles: int, threads: int) -> None:
    os.makedirs(od, exist_ok=True)
    for seed in seeds:
        c = checks(seed, variant, data)
        with open(os.path.join(od, f"checks_T_seed{seed}.json"), "w") as f:
            json.dump(dict(c, threads=threads), f, indent=1, default=P._json_default)
        P.log(f"[{variant} T/{seed}] checks: all hold {c['all_hold']}; code alone reads "
              f"{c['d_code_alone_correct_by_state']}, block alone {c['d_block_alone_correct_by_state']} of {c['d_of']}")
        if not c["all_hold"]:
            raise SystemExit(f"STOP (K2): a check that the code is unused or as described failed: {c}")
        base, meta, dm, info = build(seed, variant, data)
        orig = P.load_model
        P.load_model = lambda ckpt, arm, size: (dm, dict(meta, decoy_w18=dict(
            info, layout="[content 136 | decoy code 20 | ownership block 24]",
            constructed_stand_in="NOT A TRAINED MODEL")))
        try:
            P.run_model(ckpt_path(seed), od, "T", "toy", seed, None, shuffles, data.scale, False, data)
        finally:
            P.load_model = orig
        rp = os.path.join(od, f"row_T_seed{seed}.json")
        row = json.load(open(rp))
        row["decoy_w18"] = dict(beside(row, od, seed, dm, data), **info, threads=threads,
                                note="reporting only, computed after the frozen row; enters no verdict")
        with open(rp, "w") as f:
            json.dump(row, f, indent=1, sort_keys=True, default=P._json_default)
        p = row.get("primary") or {}
        P.log(f"[{variant} T/{seed}] nominated {row['nomination']['primary']}; "
              f"arithmetic {(p.get('reading') or {}).get('degree')}")
    P.summarise(od)


# ------------------------------------------------------------------ report

def classify(rows) -> dict:
    """Method note, section 7: one variant's verdict from its three seeds."""
    reading = [r["status"] == "reading" for r in rows]
    deg = [r["degree"] for r in rows]
    in_code = [r["piece_in_code"] for r in rows]
    n_read = sum(reading)
    if n_read < 2:
        return dict(verdict="inconclusive", reason="fewer than two seeds returned a reading")
    hi = [i for i in range(len(rows)) if reading[i] and deg[i] >= FOOLED_AT]
    if len(hi) >= 2:
        if all(in_code[i] is not None and in_code[i] > MOSTLY_IN_CODE for i in hi):
            full = sum(deg[i] >= FULLY_FOOLED_AT for i in hi) >= 2
            return dict(verdict="fooled", fully_fooled=full,
                        reason=f"two or more seeds read {FOOLED_AT} or more with the piece mostly in the code")
        return dict(verdict="inconclusive",
                    reason="two or more seeds read 0.50 or more but the piece is not mostly in the code")
    if all((not reading[i]) or deg[i] <= NEAR_ZERO for i in range(len(rows))):
        return dict(verdict="not fooled", reason=f"every seed that reads, and at least two, reads {NEAR_ZERO} or less")
    mid = [i for i in range(len(rows)) if reading[i] and NEAR_ZERO < deg[i]]
    partly = [i for i in mid if in_code[i] is not None and in_code[i] > MOSTLY_IN_CODE]
    return dict(verdict="inconclusive",
                reason="readings above 0.20 not meeting the fooled condition, or split across the bands",
                seeds_above_020_with_piece_mostly_in_code=[rows[i]["seed"] for i in partly],
                partly_fooled=len(partly) > 0)


def report() -> None:
    hdr = ("| variant | seed | reading, or no verdict | site set chosen | piece in code / block / content | "
           "block change left unmoved | whole, ownership-only, untouched (fresh) | true-slot reference | "
           "readings at 1, 2, 4, 8 directions at that site (fresh) | checks hold; code alone reads (by state) |")
    lines = [hdr, "|" + "---|" * 10]
    verdicts = {}
    for variant in VARIANTS:
        od = os.path.join(OUT, variant)
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
            sp = r["nomination"]["primary"]["site_set"]
            dt = r["decoy_w18"]
            pc = dt.get("chosen_piece_share") or {}
            most = max(pc.values(), key=lambda v: v["code"]) if pc else None
            um = dt.get("block_change_left_unmoved") or {}
            rd = p.get("reading") or {}
            bs = dt.get("fresh_readings_by_size_at_chosen_site") or {}
            verdict = f"{w['degree']:.4f}" if w["status"] == "reading" else "no verdict: " + "; ".join(w["reasons"])
            site = "none nominated" if not sp else f"states {tuple(sp['layers'])} at {sp['positions']}, {sp['rank']} directions"
            lines.append(
                f"| {variant} ({VARIANTS[variant]['kind']}, x{VARIANTS[variant]['scale']:g}) | {seed} | {verdict} | {site} | "
                + ("" if not most else f"{most['code']:.4f} / {most['block']:.4f} / {most['content']:.4f}") + " | "
                + ", ".join(f"{v:.3f}" for v in um.values()) + " | "
                + ("" if not rd else f"{rd['accuracy_whole']:.4f}, {rd['accuracy_ownership_only']:.4f}, {rd['accuracy_untouched']:.4f}")
                + " | " + ("" if not p.get("true_slot") else P._deg(p["true_slot"]["reading"]["degree"])) + " | "
                + ", ".join(P._deg(bs[k]["reading"]) for k in ("1", "2", "4", "8") if k in bs) + " | "
                + f"{c['all_hold']}; {c['d_code_alone_correct_by_state']} |")
            rows.append(dict(seed=seed, status=w["status"], degree=w.get("degree"),
                             piece_in_code=None if not most else most["code"]))
        if rows:
            verdicts[variant] = dict(classify(rows), seeds=len(rows), in_verdict=VARIANTS[variant]["in_verdict"],
                                     kind=VARIANTS[variant]["kind"], scale=VARIANTS[variant]["scale"])
    v1, v2 = verdicts.get("V1"), verdicts.get("V2")
    overall = None
    if v1 and v2:
        if "fooled" in (v1["verdict"], v2["verdict"]):
            overall = "fooled"
        elif v1["verdict"] == v2["verdict"] == "not fooled":
            overall = "not fooled"
        else:
            overall = "inconclusive"
    lines += ["", "Verdict by variant (method note, section 7; V3 to V5 reported beside, not in the verdict):"]
    lines += [f"- {k} ({v['kind']} code, x{v['scale']:g}){'' if v['in_verdict'] else ' [beside]'}: "
              f"{v['verdict']} ({v['reason']})"
              + (f"; seeds above 0.20 with the piece mostly in the code: {v['seeds_above_020_with_piece_mostly_in_code']}"
                 if v.get("seeds_above_020_with_piece_mostly_in_code") else "")
              for k, v in verdicts.items()]
    lines += ["", f"Overall (V1 and V2): {overall}"]
    txt = "\n".join(lines)
    with open(os.path.join(OUT, "table.md"), "w") as f:
        f.write(txt + "\n")
    with open(os.path.join(OUT, "verdicts.json"), "w") as f:
        json.dump(dict(by_variant=verdicts, overall=overall), f, indent=1)
    print(txt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", choices=tuple(VARIANTS))
    ap.add_argument("--seeds", type=int, nargs="+", default=[0, 1, 2])
    ap.add_argument("--checks-only", action="store_true")
    ap.add_argument("--report", action="store_true")
    ap.add_argument("--smoke", metavar="DIR", help="pipeline test at tiny episode counts into DIR; never a figure")
    ap.add_argument("--threads", type=int, default=4)
    a = ap.parse_args()
    torch.set_num_threads(a.threads)
    if a.report:
        report()
        return
    t0 = time.time()
    if a.smoke:
        data = P.EvalData(0.05)
        for v in VARIANTS:
            run(v, [0], data, os.path.join(a.smoke, v), 2, a.threads)
        P.log(f"smoke done in {time.time() - t0:.0f}s (NOT A FIGURE)")
        return
    data = P.EvalData(1.0)
    if a.checks_only:
        res = [checks(s, v, data) for v in VARIANTS for s in a.seeds]
        with open(os.path.join(OUT, "checks_only.json"), "w") as f:
            json.dump(dict(results=res, versions=P.versions(), threads=a.threads), f, indent=1,
                      default=P._json_default)
        for r in res:
            print(json.dumps({k: r[k] for k in ("variant", "seed", "all_hold", "k", "code_words_ever_set",
                                                 "d_code_alone_correct_by_state", "e_at_state_0_action")},
                             default=P._json_default))
        return
    run(a.variant, a.seeds, data, os.path.join(OUT, a.variant), MS.N_SHUFFLES, a.threads)
    P.log(f"{a.variant} done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
