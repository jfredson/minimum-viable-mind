"""The grammar attempt of 2026-09-25 (redesign (c)): the driver.

UNREGISTERED. Runs the method committed at
`docs/grammar-attempt-method-2026-09-25.md` before any of this was built. The
one change is in `grammar.py`: `NAMED_OTHER_ACTING = 0`, so the acting channel
is off on the seven tokens of the named-other action turn and nothing else
about an episode changes. Everything else is the rehearsal-repairs driver
(`repairs.py`, recipe `base`) run unchanged, with its output folder pointed at
`../out-grammar-c/`. Local, toy scale, no network, no rented machine, $0
[C1/C2].

    ../../../.venv/bin/python grammar_attempt.py --stage train --arms F,T,C
    ../../../.venv/bin/python grammar_attempt.py --stage gate
    ../../../.venv/bin/python grammar_attempt.py --stage passline
    ../../../.venv/bin/python grammar_attempt.py --stage nominate
    ../../../.venv/bin/python grammar_attempt.py --stage measure
    ../../../.venv/bin/python grammar_attempt.py --stage summary
    ../../../.venv/bin/python grammar_attempt.py --stage diagnose
    ../../../.venv/bin/python grammar_attempt.py --stage outcomes
    ../../../.venv/bin/python grammar_attempt.py --stage invariance
"""
from __future__ import annotations

import argparse
import ast
import inspect
import os
import time

import numpy as np
import torch

import grammar as G

# The change, set before anything below generates an episode.
G.NAMED_OTHER_ACTING = 0

import repairs as R                      # noqa: E402
import training as T                     # noqa: E402
import transplant as X                   # noqa: E402
import diagnose_named_other as DN        # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
R.OUT = os.path.abspath(os.path.join(HERE, "..", "out-grammar-c"))
RECIPE = "base"
ARMS = ("F", "T", "C")

# Method file, section 5 (b): the lowest own-directed accuracy the free arm has
# on either committed record of the unchanged recipe on the old grammar —
# `out/gate.json` (2026-09-21) and `out-repairs/gate_base.json` (PR 52,
# 2026-09-25, F/base/1: 1,654 of 3,000).
OWN_LEVEL = 0.5513
R2_TOLERANCE = 0.1           # method file, section 6, R-2: rehearsal-only
HIGH_LINE = 0.5              # method file, section 6, R-3: the page 1a bar


def log(*a):
    print(*a, flush=True)


# --------------------------------------------------------------- pass line

def stage_passline(device, arms, seeds):
    """Method file, section 5, read off the gate file the repairs gate wrote."""
    g = R.load_json(f"gate_{RECIPE}.json")
    rows = [g["runs"][f"F/{RECIPE}/{s}"] for s in seeds]
    other_clear = [r["other_correct"] >= R.GATE_MIN_CORRECT for r in rows]
    own_mean = float(np.mean([r["own"] for r in rows]))
    a = sum(other_clear) >= 2
    b = own_mean >= OWN_LEVEL
    res = dict(
        arm="F", seeds=list(seeds),
        named_other_correct=[r["other_correct"] for r in rows],
        named_other=[r["other"] for r in rows],
        named_other_seeds_clearing=int(sum(other_clear)),
        a_named_other_clears=bool(a),
        own_directed=[r["own"] for r in rows], own_directed_mean=own_mean,
        own_level=OWN_LEVEL, b_own_directed_not_below=bool(b),
        cleared=bool(a and b),
        bar=g["bar"])
    log(f"  wrote {R.save_json('passline.json', res)}")
    log(f"    named-other correct {res['named_other_correct']} -> "
        f"{res['named_other_seeds_clearing']} of 3 seeds at 790 or more: (a) {a}")
    log(f"    own-directed mean {own_mean:.4f} vs {OWN_LEVEL}: (b) {b}")
    log(f"    PASS LINE CLEARED: {res['cleared']}")


# ----------------------------------------------------------- diagnostic

def stage_diagnose(device, arms, seeds):
    """The repairs diagnostic, pre-stated in this method (section 6)."""
    pairs, b = T.make_data(1500, seed=99, pool="dev", device=device)
    out = {}
    for seed in seeds:
        m = R.load_arm("F", RECIPE, seed, device)
        key = f"F/{RECIPE}/{seed}"
        out[key] = DN.classify(m, pairs, b)
        log(f"    {key}: " + "  ".join(f"{k} {v:.4f}" for k, v in out[key].items()))
    log(f"  wrote {R.save_json('diagnose_named_other.json', out)}")


# ------------------------------------------------------------- outcomes

def _reading_at(m, recip, donor, reads, layers, positions, rank, device):
    d_states = X.capture(m, donor)
    d_tgt = donor["targets"][:, G.OWN]
    with torch.no_grad():
        clean = m(recip)
    u = float(R.hits(clean, d_tgt, G.OWN).mean())
    acc = float(R.hits(clean, recip["targets"][:, G.OWN], G.OWN).mean())
    sites = X.Sites(tuple(layers), positions)
    mask = X.position_mask(recip, positions)
    basis = {l: R.RH.basis_for(reads["own"][l]["coef"], rank, device) for l in layers}
    w = float(R.hits(R.run(m, recip, d_states, sites, mask, None), d_tgt, G.OWN).mean())
    o = float(R.hits(R.run(m, recip, d_states, sites, mask, basis), d_tgt, G.OWN).mean())
    return R.reading(w, o, u, acc)


def _batches(pairs, device):
    recip = R.A.to_torch(G.batch([p["recipient"] for p in pairs]), device)
    donor = R.A.to_torch(G.batch([p["donor"] for p in pairs]), device)
    return recip, donor


def stage_outcomes(device, arms, seeds):
    """R-4 (method file, section 6): the no-verdict case and the negative
    search. The near-zero and high cases are R-2 and R-3, read from the
    measure file."""
    noms = R.load_nominations(RECIPE)
    res = {"no_verdict": {}, "negative_at_nomination": {}, "negative_search": None}

    fresh, _ = T.make_data(800, seed=777, pool="fresh", device=device)
    recip, donor = _batches(fresh, device)
    for seed in seeds:
        m = R.load_arm("T", RECIPE, seed, device)
        reads = R.load_reads("T", RECIPE, seed, device)
        rd = _reading_at(m, recip, donor, reads, (0,), "pre-identity", 2, device)
        res["no_verdict"][f"T/{RECIPE}/{seed}"] = dict(
            site_set=dict(layers=[0], positions="pre-identity", rank=2), reading=rd,
            lands=rd["status"] == "no verdict")
        log(f"    no verdict case, T seed {seed}: whole {rd['accuracy_whole']:.4f} "
            f"-> {rd['status']}")

    uv, _ = T.make_data(800, seed=780, pool="unseen-vocabulary", device=device)
    urec, udon = _batches(uv, device)
    found = []
    for arm in arms:
        key = f"{arm}/{RECIPE}/0"
        spec = noms[key]["ownership"]["nomination"]
        if spec is None:
            res["negative_at_nomination"][key] = dict(status="no nomination")
            continue
        m = R.load_arm(arm, RECIPE, 0, device)
        reads = R.load_reads(arm, RECIPE, 0, device)
        rd = _reading_at(m, urec, udon, reads, spec["layers"], spec["positions"],
                         spec["rank"], device)
        res["negative_at_nomination"][key] = dict(site_set=spec, reading=rd)
        found += [key] if rd["status"] == "negative" else []
        log(f"    unseen vocabulary, {key} at its nomination: whole "
            f"{rd['accuracy_whole']:.4f} ownership-only {rd['accuracy_ownership_only']:.4f}"
            f" -> {rd['status']}" + (f", degree {rd['degree']:.4f}"
                                     if rd["degree"] is not None else ""))
    if not found:
        # method file: widen to every site set and rank cap at seed 0, and say so
        neg = []
        for arm in arms:
            m = R.load_arm(arm, RECIPE, 0, device)
            reads = R.load_reads(arm, RECIPE, 0, device)
            d_states = X.capture(m, udon)
            d_tgt = udon["targets"][:, G.OWN]
            with torch.no_grad():
                clean = m(urec)
            u = float(R.hits(clean, d_tgt, G.OWN).mean())
            acc = float(R.hits(clean, urec["targets"][:, G.OWN], G.OWN).mean())
            for L, P in R.SITE_SETS:
                sites = X.Sites(tuple(L), P)
                mask = X.position_mask(urec, P)
                w = float(R.hits(R.run(m, urec, d_states, sites, mask, None),
                                 d_tgt, G.OWN).mean())
                for r in R.RANK_CAPS:
                    basis = {l: R.RH.basis_for(reads["own"][l]["coef"], r, device)
                             for l in L}
                    o = float(R.hits(R.run(m, urec, d_states, sites, mask, basis),
                                     d_tgt, G.OWN).mean())
                    rd = R.reading(w, o, u, acc)
                    if rd["status"] == "negative":
                        neg.append(dict(arm=arm, layers=list(L), positions=P, rank=r,
                                        reading=rd))
        neg.sort(key=lambda d: d["reading"]["degree"])
        res["negative_search"] = dict(
            widened=True, found=len(neg), most_negative=neg[:5],
            searched="arms F, T, C at seed 0; all 44 site sets; rank caps 1, 2, 4, 8")
        log(f"    negative search widened: {len(neg)} negative configurations"
            + (f", most negative {neg[0]['reading']['degree']:.4f} "
               f"({neg[0]['arm']}, layers {neg[0]['layers']}, {neg[0]['positions']}, "
               f"rank {neg[0]['rank']})" if neg else ""))
    else:
        res["negative_search"] = dict(widened=False, found_at_nomination=found)
    log(f"  wrote {R.save_json('outcomes.json', res)}")


# ----------------------------------------------------------- invariance

def stage_invariance(device, arms, seeds):
    """R-5 and R-6 (method file, section 6): show, rather than assume, what the
    change cannot reach."""
    res = {}

    # R-5: with the acting channel zeroed, both grammars give identical batches,
    # for the blind solver's training sets and for the gate's held-out set.
    def zeroed(setting, n, seed, pool):
        was = G.NAMED_OTHER_ACTING
        G.NAMED_OTHER_ACTING = setting
        try:
            arr = G.batch(G.episodes_from_pairs(G.make_pairs(n, seed=seed, pool=pool)))
        finally:
            G.NAMED_OTHER_ACTING = was
        raw_acting_differs = arr["acting"].copy()
        arr["acting"] = np.zeros_like(arr["acting"])
        return arr, raw_acting_differs

    sets = [(R.TRAIN_PAIRS, 1000 + s, "train") for s in seeds] + [(1500, 99, "dev")]
    r5 = {}
    for n, sd, pool in sets:
        a0, act0 = zeroed(0, n, sd, pool)
        a1, act1 = zeroed(1, n, sd, pool)
        same = all(np.array_equal(a0[k], a1[k]) for k in a0)
        r5[f"{pool} seed {sd} ({n} pairs)"] = dict(
            zeroed_batches_identical=bool(same),
            fields_compared=sorted(a0),
            acting_positions_differing_before_zeroing=int((act0 != act1).sum()))
        log(f"    R-5 {pool} seed {sd}: zeroed batches identical {same}; "
            f"{int((act0 != act1).sum())} acting positions differ before zeroing")
    pairs, _ = T.make_data(1500, seed=99, pool="dev", device=device)
    res["R-5"] = dict(blind_solver_inputs=r5,
                      name_only_solver_recomputed=T.name_only_solver(pairs))
    log(f"    R-5 name-only solver, recomputed: {res['R-5']['name_only_solver_recomputed']}")

    # R-6: the arithmetic does not read the grammar's rendering.
    import measure as M
    names = {}
    for mod, fn in ((M, None), (R, R.reading), (R, R.floor_check)):
        src = inspect.getsource(fn if fn is not None else mod)
        tree = ast.parse(src)
        used = sorted({n.attr for n in ast.walk(tree)
                       if isinstance(n, ast.Attribute)
                       and isinstance(n.value, ast.Name) and n.value.id == "G"})
        names[fn.__name__ if fn is not None else mod.__name__] = used
    res["R-6"] = dict(grammar_attributes_used=names,
                      reaches_rendering=any("render" in v or "make_pairs" in v
                                            or "NAMED_OTHER_ACTING" in v
                                            for v in names.values()))
    log(f"    R-6 grammar attributes used by the arithmetic: {names}")
    log(f"  wrote {R.save_json('invariance.json', res)}")


# ----------------------------------------------------------------- main

STAGES = ("train", "gate", "passline", "nominate", "measure", "summary",
          "diagnose", "outcomes", "invariance")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True, choices=STAGES)
    ap.add_argument("--arms", default=",".join(ARMS))
    ap.add_argument("--seeds", default="0,1,2")
    ap.add_argument("--device", default="auto")
    a = ap.parse_args()
    device = T.pick_device(a.device)
    arms = a.arms.split(",")
    seeds = tuple(int(s) for s in a.seeds.split(","))
    assert G.NAMED_OTHER_ACTING == 0
    os.makedirs(R.OUT, exist_ok=True)
    log(f"\n=== grammar attempt, stage: {a.stage} ({device}); "
        f"NAMED_OTHER_ACTING = {G.NAMED_OTHER_ACTING}; out {R.OUT} ===")
    t0 = time.time()
    if a.stage == "train":
        R.stage_train(device, arms, [RECIPE], seeds)
    elif a.stage == "gate":
        R.stage_gate(device, arms, [RECIPE], seeds)
    elif a.stage in ("nominate", "measure", "summary"):
        getattr(R, f"stage_{a.stage}")(device, arms, RECIPE, seeds)
    else:
        globals()[f"stage_{a.stage}"](device, arms, seeds)
    log(f"  ({time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()
