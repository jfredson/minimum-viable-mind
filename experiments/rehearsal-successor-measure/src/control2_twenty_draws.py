"""The other-agent control (control 2) compared with twenty random pieces
(2026-10-03, ruling 5 of docs/rulings/2026-10-03-version-4-questions-rulings.md).

UNREGISTERED rehearsal code. Method, committed before this was run:
docs/2026-10-03-control-2-twenty-draws-method.md. Section numbers in comments
are that file's. Processor only; $0; trains nothing but small logistic
regressions.

    cd experiments/rehearsal-successor-measure/src
    ../../../.venv/bin/python control2_twenty_draws.py

`control2` below is rerun_controls.control2 with one change: the single
random piece is replaced by twenty, drawn by rerun_v3.random_bases as the
twenty-draw control (control 3) draws them, and no pass or fail is attached.
The committed scripts are not edited.

What `main` runs is A TEST THAT THE CODE RUNS END TO END, on the free model's
seed 0 with the piece's accuracy floor switched off. IT IS NOT A RESULT, and
its figures are not a pass or a fail of anything. It writes
../out-control-2-twenty-draws/code_test_NOT_A_RESULT.json and table.md.

    --smoke   runs the comparison once on a model with freshly drawn,
              untrained weights and a made-up piece; loads no committed model
              or read and writes no file.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import arms as A              # noqa: E402
import grammar as G           # noqa: E402
import rehearse as RH         # noqa: E402
import repairs as R           # noqa: E402
import rerun_controls as C    # noqa: E402
import rerun_v3 as V          # noqa: E402
import training as T          # noqa: E402
import transplant as X        # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "out-control-2-twenty-draws"))
DEVICE = torch.device("cpu")
assert V.N_RANDOM == 20


def log(*a):
    print(*a, flush=True)


def compare(m, seed, spec, coefs, fresh_recip, fresh_swap):
    """Section 3: how often the own-directed action moves under the named
    agent's piece, beside twenty random pieces of the same size at the same
    sites. No pass line."""
    L = tuple(spec["layers"])
    sites = X.Sites(L, spec["positions"])
    mask = R.anchored_mask(fresh_recip, spec["positions"], G.OTHER)
    basis = {l: RH.basis_for(coefs[l], spec["rank"], DEVICE) for l in L}
    s_states = X.capture(m, fresh_swap)
    with torch.no_grad():
        clean = m(fresh_recip)
    own_clean, oth_clean = X.predictions(clean, G.OWN), X.predictions(clean, G.OTHER)
    own_moved = R.moved_share(m, fresh_recip, s_states, sites, mask, basis, G.OWN, own_clean)
    draws = [R.moved_share(m, fresh_recip, s_states, sites, mask, rb, G.OWN, own_clean)
             for rb in V.random_bases(spec["rank"], L, seed, m.cfg.d_model, DEVICE)]
    # the one draw the earlier code made, kept so the two runs can be laid side by side
    rng = np.random.default_rng(100 + seed)
    old = {l: X.orthonormal(rng.normal(size=(spec["rank"], m.cfg.d_model))) for l in L}
    return dict(
        site_set=spec, trials=int(own_clean.shape[0]), own_directed_moved=own_moved,
        random_pieces=dict(draws=len(draws), own_directed_moved=draws,
                           median=float(np.median(draws)), p95=float(np.percentile(draws, 95)),
                           below=sum(x < own_moved for x in draws),
                           equal=sum(x == own_moved for x in draws),
                           above=sum(x > own_moved for x in draws)),
        single_random_piece_as_the_earlier_code_drew_it=R.moved_share(
            m, fresh_recip, s_states, sites, mask, old, G.OWN, own_clean),
        named_other_moved=R.moved_share(m, fresh_recip, s_states, sites, mask, basis, G.OTHER, oth_clean))


def control2(m, arm, seed, reads, dev, dev_swap, fresh_recip, fresh_swap, other_correct):
    """rerun_controls.control2 with the comparison changed (section 3)."""
    if arm in ("T", "M"):
        return dict(status="not applicable", reason="ruled: the named agent is held outside the running state")
    if other_correct < C.OTHER_BAR:
        return dict(status="no verdict", named_other_correct=other_correct,
                    reason="the arm has not learned the named-other condition")
    coefs = {l: v["coef"] for l, v in reads["named"].items()}
    fits = C.accuracies(m, dev, coefs, "named", G.OTHER)
    g = C.grid(m, dev, dev_swap, coefs, G.OTHER)
    best, why, cands = C.pick(g["grid"], fits, C.FAMILY)
    out = dict(named_other_correct=other_correct, named_read_fits=fits,
               dev_untouched=g["untouched"], dev_named_other_accuracy=g["arm_accuracy"],
               candidates=[C.spec_of(c) | dict(dev_ownership_only=c["accuracy_ownership_only"],
                                               dev_whole=c["accuracy_whole"]) for c in cands])
    if best is None:
        out.update(status="no verdict", reason=why)
        return out
    out.update(status="reported; no pass line", **compare(m, seed, C.spec_of(best), coefs, fresh_recip, fresh_swap))
    return out


def lines_for(c):
    out = ["## NOT A RESULT: the other-agent control compared with twenty random pieces, free model seed 0, floor switched off", "",
           f"ran end to end: {c['ran_end_to_end']}"]
    r = c["returned"]
    if c["ran_end_to_end"]:
        rp = r["random_pieces"]
        out += [f"site set {r['site_set']}",
                f"own-directed action moved under the named agent's piece: {r['own_directed_moved']:.4f} of {r['trials']} trials",
                f"under twenty random pieces: middle value {rp['median']:.4f}, 95th percentile {rp['p95']:.4f}; "
                f"{rp['below']} below, {rp['equal']} equal to and {rp['above']} above the real figure",
                "the twenty: " + ", ".join(f"{x:.4f}" for x in rp["own_directed_moved"]),
                f"the single random piece as the earlier code drew it: {r['single_random_piece_as_the_earlier_code_drew_it']:.4f}",
                f"named-other action moved: {r['named_other_moved']:.4f}",
                "These figures are not a pass or a fail of anything."]
    else:
        out.append(f"status {r.get('status')}; reason {r.get('reason')}")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    arm, seed = "F", 0
    fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=DEVICE)
    fresh = C.batches(fresh_pairs)
    fresh_swap = A.to_torch(G.batch(R.named_swap(fresh_pairs, seed=781)), DEVICE)
    if a.smoke:
        torch.manual_seed(12345)
        m = R.build_for(arm)().to(DEVICE).eval()
        coefs = {1: np.random.default_rng(5).normal(size=(12, m.cfg.d_model))}
        r = compare(m, seed, dict(layers=[1], positions="action+3", rank=8), coefs, fresh[0], fresh_swap)
        log("\n".join(lines_for(dict(ran_end_to_end=True, returned=r))))
        log(f"SMOKE on untrained weights and a made-up piece: ran in {time.time() - t0:.0f}s; nothing written")
        return
    gate = json.load(open(os.path.join(V.OUT, "gate.json")))
    dev_pairs, _ = T.make_data(600, seed=4242, pool="dev", device=DEVICE)
    dev = C.batches(dev_pairs)
    dev_swap = A.to_torch(G.batch(R.named_swap(dev_pairs, seed=4243)), DEVICE)
    sha = C.check_sha(arm, seed)                         # stop D1
    m = V.load_model(arm, seed, DEVICE)
    reads = R.load_reads(arm, "base", seed, DEVICE)
    floor = C.PIECE_MIN
    C.PIECE_MIN = 0                                      # the floor, switched off: NOT A RESULT
    try:
        raw = control2(m, arm, seed, reads, dev[0], dev_swap, fresh[0], fresh_swap,
                       gate["runs"][f"{arm}/{seed}"]["other_correct"])
    finally:
        C.PIECE_MIN = floor
    out = dict(NOT_A_RESULT="a test that the code runs end to end, with the accuracy floor switched off; "
                            "its figures are not a pass or a fail of anything",
               arm=arm, seed=seed, checkpoint_sha256=sha, torch=torch.__version__, device=str(DEVICE),
               ran_end_to_end="own_directed_moved" in raw, returned=raw)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "code_test_NOT_A_RESULT.json"), "w") as f:
        json.dump(out, f, indent=1, sort_keys=True, default=lambda o: list(o))
    lines = lines_for(out)
    with open(os.path.join(OUT, "table.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    log("\n".join(lines))
    log(f"done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
