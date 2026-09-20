"""The eleven-position sweep, rerun properly: is identity carried anywhere?

**UNREGISTERED**, diagnostic only. The method is committed in
`powered-position-sweep-method.md`, in the same commit as this file and
before either produced any output. Read that first: it fixes the cells.

WHY. Two things are settled. The generator's agent index cannot be
recovered in principle, so every probe that used it asked an unanswerable
question. And with a well-posed target, adequate power and a null that
resolves the bar, identity is NOT CARRIED at the registered probe
position. What is not settled is whether it is carried ANYWHERE ELSE: the
eleven-position sweep that asked that ran against the unrecoverable
target and came back SWEEP INVALID, answering nothing.

This reruns it: the same eleven positions, the two well-posed targets
(the model's own marker word and its register index), 4,000 episodes,
1,000 draws, all five layers, all three checkpoints. It reports which
positions clear, if any, and stops.

THE POSITIVE CONTROL is position 6, the model's own marker as an input
token. A checkpoint where it fails is VOID.

THE NEGATIVE CONTROL is position 1, and it is new here. At the value
token of the model's FIRST own turn its own marker has not yet appeared
anywhere in the episode — the marker comes two tokens later and no other
agent's turn carries it. So neither target is determinable from anything
the model has seen. A clearance there cannot be carrying; it would mean
something leaks the answer, most plausibly the acting channel, which
injects at exactly that token. It is reported, treated as a leak, and
excluded from the cells.

THE BAR BINDS HERE IN A WAY IT DID NOT LAST TIME. 270 discovery tests
against the previous run's 30. Leaving the bar at three standard
deviations would give a 30.6% chance of a false clearance somewhere,
which for a sweep asking "does anything clear anywhere" is exactly the
wrong error to tolerate. So the cells turn on the family-adjusted bar of
3.56 standard deviations plus zero of 1,000 draws beating the score;
three-standard-deviation clearances are reported as MARGINAL and trigger
no cell.

AND WHAT 1,000 DRAWS CANNOT CERTIFY. Zero of 1,000 establishes a
probability below 0.001, about 3.09 standard deviations — BELOW the 3.56
the family bar needs. The count alone cannot certify a family-safe
clearance across 270 tests; the margin supplies the rest under a normal
approximation. A single ROBUST clearance is suggestive and wants a
targeted rerun at that position with far more draws, not settled.

Corrigibility: inference only, no training, no network, no spend [C1/C2];
gated on the known-answer test, deliberately NOT on the threshold lock;
fresh output per checkpoint, nothing overwritten [C6].

    ../../../.venv/bin/python powered_position_sweep_a3.py --self-test
    ../../../.venv/bin/python powered_position_sweep_a3.py --run \\
        --ckpt ../artifacts/a3_30m_seed0/a3_30m_seed0.pt
    ../../../.venv/bin/python powered_position_sweep_a3.py --summarize
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

import curriculum_a3 as A
import encoding_a3 as E
import lock_guard
import localize_a3 as L
import position_sweep_a3 as S
import powered_target_test_a3 as P
from model import MVM0aModel, Config, to_torch

PROBE_LAYERS = P.PROBE_LAYERS
N_PAIRS = P.N_PAIRS                  # 4,000 episodes
EPISODE_SEED = P.EPISODE_SEED
N_PERM = P.N_PERM                    # 1,000
SD_BAR = P.SD_BAR                    # 3.0, reported for continuity
FAMILY_SD_BAR = 3.56                 # 270 discovery tests, 5% family-wise
CHUNK = P.CHUNK
ARMS = P.ARMS

POSITIONS = S.POSITIONS              # the same eleven, unchanged
POSITIVE_CONTROL = "own_revision_marker"
NEGATIVE_CONTROL = "own_assign_1_value"
TESTABLE = tuple(p for p in POSITIONS
                 if p not in (POSITIVE_CONTROL, NEGATIVE_CONTROL))
PILOT = "a3_30m_seed0.pt"


def key(arm, pos, layer):
    return f"{arm}|{pos}|{layer}"


# --------------------------------------------------------------- capture

@torch.no_grad()
def capture(model, eps, device, with_query, chunk=CHUNK):
    """States at the eleven positions, per layer, in chunks so 4,000
    episodes fit. Mirrors `position_sweep_a3.capture`, which does the same
    thing in one pass and cannot be handed this many episodes."""
    names = [p for p in POSITIONS
             if (p in S.QUERY_POSITIONS) == bool(with_query)]
    out = {(Lr, p): [] for Lr in PROBE_LAYERS for p in names}
    kept = []
    rng = random.Random(0)
    for e in eps:
        A.enact_own_turns(e, rng)
    for start in range(0, len(eps), chunk):
        part = eps[start:start + chunk]
        encs = [E.encode_episode(e, query=(e.queries[0] if with_query
                                           else None)) for e in part]
        lens = [len(x["input_ids"]) for x in encs]
        batch = to_torch(E.collate(encs), device)
        B, Ltok = batch["input_ids"].shape
        act = torch.zeros(B, Ltok, model.cfg.d_model, device=device)
        own_idx = [[i for i, t in enumerate(e.turns) if t.agent == e.own_slot]
                   for e in part]
        for k in range(max(len(o) for o in own_idx)):
            _, h = model.forward(batch, act_inject=act, return_hidden=True)
            bs, ps = [], []
            for b, e in enumerate(part):
                if k < len(own_idx[b]):
                    sp = (batch["turn_ids"][b]
                          == own_idx[b][k]).nonzero().flatten()
                    bs.append(b)
                    ps.append(int(sp[0]) + A.VALUE_WORD_IDX)
            bi = torch.tensor(bs, device=device)
            pi = torch.tensor(ps, device=device)
            act = act.index_put((bi, pi), model.act_proj(h[bi, pi - 1]))

        caps = {Lr: [] for Lr in PROBE_LAYERS}
        for Lr in PROBE_LAYERS:
            blk = model.blocks[Lr]
            orig = blk.forward

            def patched(x, kv, reg_repr, _o=orig, _L=Lr):
                x, ctx = _o(x, kv, reg_repr)
                caps[_L].append(x.detach())
                return x, ctx
            blk.forward = patched
        model.forward(batch, act_inject=act)
        for Lr in PROBE_LAYERS:
            del model.blocks[Lr].__dict__["forward"]

        idx = [S.position_indices(e, lens[b], with_query)
               for b, e in enumerate(part)]
        rows = [b for b, v in enumerate(idx)
                if v is not None and all(0 <= v[p] < lens[b] for p in names)]
        kept += [start + b for b in rows]
        for Lr in PROBE_LAYERS:
            hs = torch.cat(caps[Lr], dim=1)
            bi = torch.tensor(rows, device=hs.device)
            for p in names:
                pos = torch.tensor([idx[b][p] for b in rows],
                                   device=hs.device)
                out[(Lr, p)].append(hs[bi, pos].float().cpu().numpy())
    return {k: np.concatenate(v, axis=0) for k, v in out.items()}, kept


# ----------------------------------------------------------------- cells

def clears(rec):
    """A clearance for cell purposes: the family-adjusted bar AND no
    shuffled draw meeting or beating the real score."""
    a = rec["accuracy"]
    return bool(a.get("label") == "ROBUST")


def arm_cell(per_checkpoint):
    """The two cells fixed in `powered-position-sweep-method.md`.

    `per_checkpoint` maps a checkpoint name to
    {"control_holds": bool, "clearing_positions": [...], "leak": [...]}.
    """
    pilot = per_checkpoint.get(PILOT)
    if pilot is None or not pilot["control_holds"]:
        return {"cell": "VOID — no cell assigned",
                "means": ("the positive control fails on the pilot, so "
                          "nothing in this arm can be interpreted")}
    void = [k for k, v in per_checkpoint.items() if not v["control_holds"]]
    readable = {k: v for k, v in per_checkpoint.items() if v["control_holds"]}
    clearing = {k: v["clearing_positions"] for k, v in readable.items()
                if v["clearing_positions"]}
    others = [k for k in clearing if k != PILOT]
    leaks = {k: v["leak"] for k, v in per_checkpoint.items() if v["leak"]}
    base = {"void_checkpoints": void, "clearing_by_checkpoint": clearing,
            "negative_control_clearances": leaks}
    if PILOT in clearing and others:
        return {**base, "cell": "CARRIED SOMEWHERE",
                "means": ("own-agent identity is linearly present at a "
                          "position where it has to have been carried "
                          "rather than read off the current token. The "
                          "clearing positions are the finding. It does not "
                          "settle red-team objection R1")}
    return {**base, "cell": "CARRIED NOWHERE",
            "sub_pattern": ("nothing cleared on any checkpoint"
                            if not clearing else
                            "cleared on the pilot only" if PILOT in clearing
                            else "cleared on seeds but not the pilot"),
            "means": ("across eleven positions, five layers and three "
                      "checkpoints, identity is not linearly recoverable "
                      "anywhere except where it is present as an input "
                      "token. The cells are exhaustive by construction, so "
                      "the sub-pattern is reported rather than hidden")}


@torch.no_grad()
def run(ckpt: Path, device: str, n_pairs: int) -> dict:
    lock_guard.require_known_answer_pass()
    checks = P.verify_scorer_matches_original()
    t0 = time.time()
    ck = torch.load(ckpt, map_location=device, weights_only=True)
    model = MVM0aModel(Config(**ck["cfg"])).to(device).eval()
    model.load_state_dict(ck["state"])

    pairs = L.paired_episodes(n_pairs, seed=EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    states, kept = capture(model, flat, device, with_query=False)
    qstates, qkept = capture(model, flat, device, with_query=True)
    if kept != qkept:
        raise SystemExit(
            "REFUSING to report: the two capture passes kept different "
            "episodes, so the in-episode and appended-question positions "
            "would not line up episode for episode.")
    states.update(qstates)
    eps = [flat[i] for i in kept]
    tg = P.targets(eps)
    print(f"  captured {len(eps)} episodes at {len(POSITIONS)} positions",
          flush=True)

    results = {}
    for arm in ARMS:
        y = tg[arm]
        for pos in POSITIONS:
            for Lr in PROBE_LAYERS:
                results[key(arm, pos, Lr)] = P.measure(
                    states[(Lr, pos)], y, seed=Lr,
                    family_bar=FAMILY_SD_BAR)
            best = max(PROBE_LAYERS,
                       key=lambda k: results[key(arm, pos, k)]
                       ["accuracy"]["margin_sd"] or -99)
            a = results[key(arm, pos, best)]["accuracy"]
            tag = ("POSITIVE CONTROL" if pos == POSITIVE_CONTROL else
                   "negative control" if pos == NEGATIVE_CONTROL else "")
            print(f"  {arm:15s} {pos:26s} L{best}: acc {a['value']:.4f} "
                  f"({a['margin_sd']:+.2f} sd, {a['draws_beating_real']}"
                  f"/{N_PERM}) {a['label'] or '-'} {tag}", flush=True)

    control_holds = any(
        clears(results[key("marker_word", POSITIVE_CONTROL, Lr)])
        for Lr in PROBE_LAYERS)
    per_arm = {}
    for arm in ARMS:
        per_arm[arm] = {
            "control_holds": bool(control_holds),
            "clearing_positions": sorted({
                pos for pos in TESTABLE for Lr in PROBE_LAYERS
                if clears(results[key(arm, pos, Lr)])}),
            "marginal_positions": sorted({
                pos for pos in TESTABLE for Lr in PROBE_LAYERS
                if results[key(arm, pos, Lr)]["accuracy"]["clears_3sd"]
                and not clears(results[key(arm, pos, Lr)])}),
            "leak": sorted({
                NEGATIVE_CONTROL for Lr in PROBE_LAYERS
                if clears(results[key(arm, NEGATIVE_CONTROL, Lr)])}),
        }

    return {
        "diagnostic": "powered eleven-position sweep, two well-posed targets",
        "registered": False, "verdict_bearing": False,
        "method_file": "powered-position-sweep-method.md",
        "method_committed_before_output": True,
        "checkpoint": ckpt.name,
        "checkpoint_md5": hashlib.md5(ckpt.read_bytes()).hexdigest(),
        "scorer_agrees_with_original": checks,
        "settings": {
            "episodes": len(eps), "permutations": N_PERM,
            "sd_bar": SD_BAR, "family_sd_bar": FAMILY_SD_BAR,
            "family_size": len(ARMS) * len(TESTABLE) * len(PROBE_LAYERS) * 3,
            "probe_layers": PROBE_LAYERS, "positions": list(POSITIONS),
            "testable_positions": list(TESTABLE),
            "positive_control": POSITIVE_CONTROL,
            "negative_control": NEGATIVE_CONTROL,
            "negative_control_note": (
                "at the value of the model's FIRST own turn its own marker "
                "has not yet appeared anywhere, so neither target is "
                "determinable there; a clearance means a leak, not "
                "carrying, and is excluded from the cells"),
            "arms": list(ARMS)},
        "results": results,
        "per_arm": per_arm,
        "positive_control_holds": bool(control_holds),
        "limits": (
            "UNREGISTERED and diagnostic. One statistic, linear, eleven "
            "positions, five layers, three 30-million-parameter "
            "checkpoints on a synthetic grammar. A null everywhere is "
            "consistent with identity being carried non-linearly, or "
            "distributed rather than resident at any one position, or at "
            "a position not on the list. It does not touch red-team "
            "objection R1 and changes no registered result. 1,000 draws "
            "resolve only p<0.001, below the 3.56 the family bar needs, so "
            "a single ROBUST clearance is suggestive and wants a targeted "
            "rerun rather than being settled."),
        "elapsed_sec": round(time.time() - t0, 1),
    }


def summarize(paths) -> dict:
    records = [json.loads(Path(p).read_text()) for p in paths]
    out = {"checkpoints": [r["checkpoint"] for r in records],
           "family_sd_bar": FAMILY_SD_BAR,
           "family_size": records[0]["settings"]["family_size"],
           "arms": {}}
    for arm in ARMS:
        per = {r["checkpoint"]: r["per_arm"][arm] for r in records}
        out["arms"][arm] = {"cell": arm_cell(per)["cell"],
                            "detail": arm_cell(per), "per_checkpoint": per}
    out["note"] = ("diagnostic only; no verdict is read and no registered "
                   "text is touched")
    return out


# ------------------------------------------------------------- self-test

def self_test() -> None:
    P.verify_scorer_matches_original()
    assert POSITIVE_CONTROL in POSITIONS and NEGATIVE_CONTROL in POSITIONS
    assert len(POSITIONS) == 11, "eleven positions"
    assert len(TESTABLE) == 9, "nine testable positions"
    assert POSITIVE_CONTROL not in TESTABLE and NEGATIVE_CONTROL not in TESTABLE

    # THE NEGATIVE CONTROL'S PREMISE, checked against real episodes rather
    # than asserted: at the value of the model's first own turn, its own
    # marker must not have appeared anywhere earlier in the episode.
    pairs = L.paired_episodes(12, seed=EPISODE_SEED)
    flat = [e for p in pairs for e in p]
    for e in flat:
        enc = E.encode_episode(e)
        ids = enc["input_ids"]
        idx = S.position_indices(e, len(ids), False)
        own_marker = E.VOCAB[e.markers[e.own_slot]]
        before = [int(t) for t in ids[:idx[NEGATIVE_CONTROL] + 1]]
        assert own_marker not in before, (
            "the negative control's premise fails: the model's own marker "
            "appears at or before its first own value token")
        # and by the positive control it must be present, as that token
        assert int(ids[idx[POSITIVE_CONTROL]]) == own_marker
        # the anchor sits between them and does not hold the marker
        assert int(ids[idx["own_revision_decision"]]) != own_marker

    # the family bar must actually be stricter than the per-test bar here
    assert FAMILY_SD_BAR > SD_BAR, "otherwise the adjustment is pointless"

    # a ROBUST label requires the family bar AND a clean count
    rng = np.random.default_rng(1)
    n, d, C = 600, 40, 4
    y = np.array([i % C for i in range(n)])
    X = rng.normal(0, 1, (n, d))
    for c in range(C):
        X[y == c, c] += 2.5
    r = P.measure(X, y, seed=0, family_bar=FAMILY_SD_BAR)
    assert clears(r), "a strong planted signal must clear the family bar"
    r2 = P.measure(X, y, seed=0, family_bar=1e6)
    assert not clears(r2) and r2["accuracy"]["label"] == "MARGINAL", \
        "an unreachable family bar must demote the same result"
    Z = rng.normal(0, 1, (n, d))
    assert not clears(P.measure(Z, y, seed=0, family_bar=FAMILY_SD_BAR))

    # the cells
    def cp(control=True, clearing=(), leak=()):
        return {"control_holds": control, "clearing_positions": list(clearing),
                "leak": list(leak)}
    A_ = "own_revision_value"
    assert arm_cell({PILOT: cp(control=False)})["cell"].startswith("VOID")
    assert arm_cell({PILOT: cp(), "b.pt": cp()})["cell"] == "CARRIED NOWHERE"
    c = arm_cell({PILOT: cp(clearing=[A_]), "b.pt": cp(clearing=[A_])})
    assert c["cell"] == "CARRIED SOMEWHERE"
    assert c["clearing_by_checkpoint"][PILOT] == [A_]
    # pilot alone is CARRIED NOWHERE by construction, and must say so
    c = arm_cell({PILOT: cp(clearing=[A_]), "b.pt": cp()})
    assert c["cell"] == "CARRIED NOWHERE"
    assert c["sub_pattern"] == "cleared on the pilot only", \
        "an exhaustive pair of cells must not hide the sub-pattern"
    c = arm_cell({PILOT: cp(), "b.pt": cp(clearing=[A_])})
    assert c["sub_pattern"] == "cleared on seeds but not the pilot"
    # a leak is carried into the summary rather than dropped
    c = arm_cell({PILOT: cp(leak=[NEGATIVE_CONTROL]), "b.pt": cp()})
    assert c["negative_control_clearances"] == {PILOT: [NEGATIVE_CONTROL]}

    try:
        lock_guard.require_known_answer_pass(Path("/nonexistent.json"))
        raise AssertionError("an absent known-answer result must refuse")
    except lock_guard.PipelineUnvalidated:
        pass
    print(f"self-test OK — eleven positions, nine testable; the negative "
          f"control's premise verified against real episodes (the model's "
          f"own marker really is absent before its first own value token); "
          f"the family bar {FAMILY_SD_BAR} binds and demotes; both cells "
          f"including the sub-patterns an exhaustive pair would otherwise "
          f"hide; the known-answer gate. No checkpoint touched")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", dest="self_test", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--summarize", action="store_true")
    ap.add_argument("--ckpt", type=Path, action="append", default=None)
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--n-pairs", type=int, default=N_PAIRS)
    ap.add_argument("--out-dir", type=Path, default=Path("../a3-gates"))
    a = ap.parse_args()
    if a.summarize:
        paths = sorted(a.out_dir.glob("powered_position_sweep_a3_a3_*.json"))
        if not paths:
            raise SystemExit("no per-checkpoint files to summarize")
        s = summarize(paths)
        out = a.out_dir / "powered_position_sweep_a3_summary.json"
        if out.exists():
            raise SystemExit(f"{out} exists; refusing to overwrite")
        out.write_text(json.dumps(s, indent=2))
        print(json.dumps({k: v["cell"] for k, v in s["arms"].items()},
                         indent=2))
        return
    if not a.run:
        self_test()
        return
    if not a.ckpt:
        raise SystemExit("--run needs at least one --ckpt")
    for c in a.ckpt:
        out = a.out_dir / f"powered_position_sweep_a3_{c.stem}.json"
        if out.exists():
            raise SystemExit(f"{out} exists; refusing to overwrite")
        print(f"=== {c.name} ===", flush=True)
        rec = run(c, a.device, a.n_pairs)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(rec, indent=2))
        print(f"written: {out}", flush=True)


if __name__ == "__main__":
    main()
