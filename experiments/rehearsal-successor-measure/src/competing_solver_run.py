"""The ordinary competing solver under the rules as now ruled (2026-10-03).

UNREGISTERED rehearsal code. Method, committed before this was run:
docs/2026-10-03-competing-solver-run-method.md. Section numbers in comments
are that file's. Loads the three committed toy models trained with no acting
channel; trains nothing but small logistic regressions; processor only; $0.

    cd experiments/rehearsal-successor-measure/src
    ../../../.venv/bin/python competing_solver_run.py

Writes ../out-competing-solver-run/{reads,nominate,measure}_blind_seed{seed}_{reading}.*,
summary.json and table.md.

The nomination rule, the family, the floors and the piece counts are the
controls re-run's own (rerun_controls.pick, FAMILY, STRICT, PIECE_MIN,
correct_count), imported and not copied. What is new here is only what a
solver with no acting channel needs: the model is fed one batch and the
positions and labels are taken from another (section 3).

    --smoke   runs the whole path once on a model with freshly drawn,
              untrained weights; loads no committed model and writes no file.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression

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
OUT = os.path.abspath(os.path.join(HERE, "..", "out-competing-solver-run"))
DEVICE = torch.device("cpu")
ARM, SEEDS, RANKS = "blind", (0, 1, 2), C.RANKS
# section 3: the two readings of "a solver with no acting channel"
READINGS = ("channel_removed", "channel_left_on")
PRIMARY = "channel_removed"
GATE_MIN = R.GATE_MIN_CORRECT                     # 790 of 3,000


def log(*a):
    print(*a, flush=True)


def save(name, obj):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w") as f:
        json.dump(obj, f, indent=1, sort_keys=True, default=lambda o: list(o))


def fed(b, reading):
    """What the model is given. The episode `b` keeps its true acting channel,
    which fixes the positions and the label; under `channel_removed` the
    model sees that channel as all zeros, as it did in training and scoring."""
    if reading == "channel_removed":
        b = dict(b)
        b["acting"] = torch.zeros_like(b["acting"])
    return b


def wilson(k, n, z=1.96):
    """The band sampling alone puts around k of n (ruling 4)."""
    p = k / n
    mid = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return [float(max(0.0, mid - half) * n), float(min(1.0, mid + half) * n)]


def fit_reads(m, fed_b, true_b):
    """repairs.fit_reads, with the label taken from the true episode: one
    straight-line read per layer at the own-directed action position, fitted
    on the first 420 development episodes."""
    with torch.no_grad():
        _, states = m(fed_b, capture=True)
    ap = true_b["action_pos"][:, G.OWN]
    y = R.read_labels(true_b, "own")
    n_tr = int(0.7 * len(y))
    out = {}
    for l, st in enumerate(states):
        h = st[torch.arange(st.shape[0]), ap].numpy()
        clf = LogisticRegression(max_iter=3000, C=1.0).fit(h[:n_tr], y[:n_tr])
        out[l] = clf.coef_.astype(np.float64)
    return out


def accuracies(m, fed_b, true_b, coefs):
    """rerun_controls.accuracies: per layer, the whole read's held-out count
    and each size's piece count, of 180."""
    with torch.no_grad():
        _, states = m(fed_b, capture=True)
    ap = true_b["action_pos"][:, G.OWN]
    y = R.read_labels(true_b, "own")
    assert len(y) - int(0.7 * len(y)) == C.HELD_OUT
    out = {}
    for l, st in enumerate(states):
        h = st[torch.arange(st.shape[0]), ap].numpy()
        out[l] = dict(whole=C.correct_count(h, y),
                      piece={r: C.correct_count(h @ RH.basis_for(coefs[l], r, DEVICE).numpy(), y)
                             for r in RANKS})
    return out, int(len(np.unique(y)))


def grid(m, fed_recip, fed_donor, true_recip, true_donor, coefs, null_too=False):
    """rerun_controls.grid: every site set of the family at every size. The
    positions come from the true recipient episode."""
    d_states = X.capture(m, fed_donor)
    r_states = X.capture(m, fed_recip)
    d_tgt = true_donor["targets"][:, G.OWN]
    with torch.no_grad():
        clean = m(fed_recip)
    u = float(R.hits(clean, d_tgt, G.OWN).mean())
    acc = float(R.hits(clean, true_recip["targets"][:, G.OWN], G.OWN).mean())
    rows, nulls = [], []
    for L, P in C.FAMILY:
        sites = X.Sites(layers=tuple(L), positions=P)
        mask = R.anchored_mask(true_recip, P, G.OWN)
        whole = float(R.hits(R.run(m, fed_recip, d_states, sites, mask, None), d_tgt, G.OWN).mean())
        fl = R.floor_check(whole, u, acc)
        if null_too:
            nulls.append(bool(torch.equal(clean, R.run(m, fed_recip, r_states, sites, mask, None))))
        for r in RANKS:
            basis = {l: RH.basis_for(coefs[l], r, DEVICE) for l in L}
            own = float(R.hits(R.run(m, fed_recip, d_states, sites, mask, basis), d_tgt, G.OWN).mean())
            rows.append(dict(layers=list(L), positions=P, rank=r, accuracy_whole=whole,
                             accuracy_ownership_only=own, floor=fl))
    twins = dict(inputs_identical=bool(torch.equal(fed_recip["tokens"], fed_donor["tokens"])
                                       and torch.equal(fed_recip["acting"], fed_donor["acting"])),
                 states_identical=all(bool(torch.equal(a, b)) for a, b in zip(r_states, d_states)),
                 largest_state_difference=float(max((a - b).abs().max() for a, b in zip(r_states, d_states))),
                 actions_that_differ=int((X.predictions(clean, G.OWN)
                                          != X.predictions(m(fed_donor), G.OWN)).sum()))
    return dict(untouched=u, accuracy=acc, grid=rows, twins=twins,
                null_bit_identical_at_every_site_set=(all(nulls) if null_too else None))


def n_clearing(rows):
    return len({(tuple(x["layers"]), x["positions"]) for x in rows if x["floor"]["clears"]})


def arithmetic(rows, u, acc):
    """Section 5, DESCRIPTION ONLY: what (whole - piece) / (whole - untouched)
    comes to at each site set and size, with no floor applied."""
    vals, undefined = [], 0
    for g in rows:
        room = g["accuracy_whole"] - u
        if room == 0:
            undefined += 1
        else:
            vals.append((g["accuracy_whole"] - g["accuracy_ownership_only"]) / room)
    rooms = [g["accuracy_whole"] - u for g in rows]
    return dict(DESCRIPTION_ONLY="no floor applied; not a reading",
                comparisons=len(rows), zero_divided_by_zero_or_by_zero=undefined,
                defined=len(vals),
                min=min(vals) if vals else None, median=float(np.median(vals)) if vals else None,
                max=max(vals) if vals else None,
                whole_minus_untouched=dict(min=min(rooms), max=max(rooms)),
                required_room_for_the_floor=R.FLOOR_SHARE * (acc - u))


def run_one(m, seed, reading, dev, fresh, gate_b, write=True):
    (dev_r, dev_d), (fr_r, fr_d) = dev, fresh
    f_dev_r, f_dev_d = fed(dev_r, reading), fed(dev_d, reading)
    f_fr_r, f_fr_d = fed(fr_r, reading), fed(fr_d, reading)
    # the gate on learning, recomputed on the processor
    acc = T.accuracy(m, fed(gate_b, reading))
    own_c, oth_c = int(round(acc["own"] * acc["n"])), int(round(acc["other"] * acc["n"]))
    gate = dict(own_correct=own_c, other_correct=oth_c, n=acc["n"], bar=GATE_MIN,
                own_clears=own_c >= GATE_MIN, other_clears=oth_c >= GATE_MIN)
    # the read: not a committed file for this solver, so fitted here (section 3, rule 3)
    coefs = fit_reads(m, f_dev_r, dev_r)
    if write:
        os.makedirs(OUT, exist_ok=True)
        np.savez(os.path.join(OUT, f"reads_blind_seed{seed}_{reading}.npz"),
                 **{f"own|{l}": v for l, v in coefs.items()})
    fits, classes = accuracies(m, f_dev_r, dev_r, coefs)
    g = grid(m, f_dev_r, f_dev_d, dev_r, dev_d, coefs)
    best, why, cands = C.pick(g["grid"], fits, C.FAMILY)
    sbest, swhy, _ = C.pick(g["grid"], fits, C.STRICT)
    unfiltered, _, _ = C.pick(g["grid"], fits, C.FAMILY, require_piece=False)
    best_piece = max(fits[l]["piece"][r] for l in fits for r in RANKS)
    nom = dict(arm=ARM, seed=seed, reading_of_the_solver=reading, fits=fits, label_classes_present=classes,
               best_piece_correct=best_piece, best_piece_sampling_band=wilson(best_piece, C.HELD_OUT),
               piece_floor=C.PIECE_MIN,
               dev_untouched=g["untouched"], dev_accuracy=g["accuracy"], dev_twins=g["twins"],
               site_sets_clearing=n_clearing(g["grid"]),
               candidates=[C.spec_of(c) | dict(dev_ownership_only=c["accuracy_ownership_only"],
                                               dev_whole=c["accuracy_whole"]) for c in cands],
               primary=dict(status=why, site_set=C.spec_of(best)),
               stricter=dict(status=swhy, site_set=C.spec_of(sbest)),
               piece_rule_switched_off=C.spec_of(unfiltered),
               dev_arithmetic_DESCRIPTION_ONLY=arithmetic(g["grid"], g["untouched"], g["accuracy"]),
               grid=g["grid"])
    # fresh episodes
    fg = grid(m, f_fr_r, f_fr_d, fr_r, fr_d, coefs, null_too=True)
    u, a = fg["untouched"], fg["accuracy"]
    by_site = {(tuple(x["layers"]), x["positions"], x["rank"]): x for x in fg["grid"]}

    def at(spec):
        x = by_site[(tuple(spec["layers"]), spec["positions"], spec["rank"])]
        return dict(site_set=spec, reading=R.reading(x["accuracy_whole"], x["accuracy_ownership_only"], u, a))

    meas = dict(arm=ARM, seed=seed, reading_of_the_solver=reading, gate=gate,
                nomination_status=why, fresh_untouched=u, fresh_accuracy=a, fresh_twins=fg["twins"],
                no_transplant=dict(rate=u, formula=(1 - a) / 7, miss=u - (1 - a) / 7,
                                   inside_allowance=abs(u - (1 - a) / 7) <= C.ROOM),
                fresh_site_sets_clearing=n_clearing(fg["grid"]),
                null_bit_identical_at_every_site_set=fg["null_bit_identical_at_every_site_set"],
                fresh_arithmetic_DESCRIPTION_ONLY=arithmetic(fg["grid"], u, a))
    returned = False
    if best is not None:                                           # stop B2 territory
        meas["primary"] = at(C.spec_of(best))
        returned = meas["primary"]["reading"]["degree"] is not None
    if unfiltered is not None and best is None:
        meas["at_the_site_the_rule_would_choose_with_the_piece_rule_off_DESCRIPTION_ONLY"] = at(C.spec_of(unfiltered))
    meas["a_reading_was_returned"] = returned
    meas["status"] = ("READING RETURNED" if returned else
                      "no verdict: floor missed on fresh episodes" if best is not None else f"no verdict: {why}")
    if write:
        save(f"nominate_blind_seed{seed}_{reading}.json", nom)
        save(f"measure_blind_seed{seed}_{reading}.json", meas)
    log(f"{reading} seed {seed}: gate own {own_c} other {oth_c} of {acc['n']} (bar {GATE_MIN}) | "
        f"dev site sets clearing {nom['site_sets_clearing']} of 45 | best piece {best_piece} of 180 | "
        f"nomination: {why} | stricter: {swhy} | fresh site sets clearing {meas['fresh_site_sets_clearing']} | "
        f"null identical {meas['null_bit_identical_at_every_site_set']} | twins' states identical "
        f"{fg['twins']['states_identical']} | STATUS {meas['status']}")
    return nom, meas


def table(results):
    lines = []
    for reading in READINGS:
        lines += [f"## The solver read as: {reading}"
                  + (" (this session's primary reading)" if reading == PRIMARY else " (second reading, for description)"), "",
                  "### The read of the solver's own marker word: correct of 180 held-out development episodes", "",
                  "| seed | layer | whole read | piece, 1 direction | 2 | 4 | 8 |", "|---|---|---|---|---|---|---|"]
        for seed in SEEDS:
            f = results[(reading, seed)][0]["fits"]
            for l in sorted(f):
                p = f[l]["piece"]
                lines.append(f"| {seed} | {l} | {f[l]['whole']} | {p[1]} | {p[2]} | {p[4]} | {p[8]} |")
        lines += ["", "### Nomination and status", "",
                  "| seed | gate: own, other, of 3,000 (bar 790) | site sets clearing the whole-state floor, development / fresh, of 45 | best piece of 180 (sampling band) | nomination | stricter row | status | null transplant, 45 site sets | twins' states identical | no-transplant rate, formula, inside 0.018 |",
                  "|---|---|---|---|---|---|---|---|---|---|"]
        for seed in SEEDS:
            n, me = results[(reading, seed)]
            b = n["best_piece_sampling_band"]
            nt = me["no_transplant"]
            lines.append(
                f"| {seed} | {me['gate']['own_correct']}, {me['gate']['other_correct']} | "
                f"{n['site_sets_clearing']} / {me['fresh_site_sets_clearing']} | {n['best_piece_correct']} ({b[0]:.0f} to {b[1]:.0f}) | "
                f"{n['primary']['status']} | {n['stricter']['status']} | {me['status']} | "
                f"{'identical' if me['null_bit_identical_at_every_site_set'] else 'DIFFERS'} | "
                f"{me['fresh_twins']['states_identical']} | {nt['rate']:.4f}, {nt['formula']:.4f}, {nt['inside_allowance']} |")
        lines += ["", "### DESCRIPTION ONLY: what the arithmetic would have returned, with no floor applied, on fresh episodes", "",
                  "| seed | accuracy, untouched | whole minus untouched, smallest to largest over 45 site sets | room the floor asks for | of 180 comparisons: 0 divided by 0 or by 0 / defined | defined values: smallest, middle, largest | at the site the rule would choose with the piece rule off |",
                  "|---|---|---|---|---|---|---|"]
        for seed in SEEDS:
            _, me = results[(reading, seed)]
            ar = me["fresh_arithmetic_DESCRIPTION_ONLY"]
            vals = ("none defined" if not ar["defined"] else f"{ar['min']:.4f}, {ar['median']:.4f}, {ar['max']:.4f}")
            d = me.get("at_the_site_the_rule_would_choose_with_the_piece_rule_off_DESCRIPTION_ONLY")
            dl = "no site set clears, so the rule chooses none" if d is None else (
                f"layers {tuple(d['site_set']['layers'])} at {d['site_set']['positions']}, {d['site_set']['rank']} directions: "
                + ("floor missed on fresh episodes" if d["reading"]["degree"] is None else f"({d['reading']['degree']:.4f})"))
            lines.append(f"| {seed} | {me['fresh_accuracy']:.4f}, {me['fresh_untouched']:.4f} | "
                         f"{ar['whole_minus_untouched']['min']:+.4f} to {ar['whole_minus_untouched']['max']:+.4f} | "
                         f"{ar['required_room_for_the_floor']:+.4f} | {ar['zero_divided_by_zero_or_by_zero']} / {ar['defined']} | {vals} | {dl} |")
        lines.append("")
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    dev_pairs, _ = T.make_data(600, seed=4242, pool="dev", device=DEVICE)
    fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=DEVICE)
    _, gate_b = T.make_data(1500, seed=99, pool="dev", device=DEVICE)
    assert gate_b["tokens"].shape[0] == R.GATE_EPISODES
    dev, fresh = C.batches(dev_pairs), C.batches(fresh_pairs)
    if a.smoke:
        torch.manual_seed(12345)
        m = R.build_for(ARM)().to(DEVICE).eval()
        res = {(rd, s): run_one(m, s, rd, dev, fresh, gate_b, write=False) for rd in READINGS for s in SEEDS[:1]}
        res.update({(rd, s): res[(rd, 0)] for rd in READINGS for s in SEEDS[1:]})
        log("\n".join(table(res)))
        log(f"SMOKE on untrained weights: ran end to end in {time.time() - t0:.0f}s; nothing written")
        return
    shas = {seed: C.check_sha(ARM, seed) for seed in SEEDS}          # stop B1, before any model is loaded
    results = {}
    for reading in READINGS:
        for seed in SEEDS:
            m = V.load_model(ARM, seed, DEVICE)
            results[(reading, seed)] = run_one(m, seed, reading, dev, fresh, gate_b)
    any_reading = [f"{rd}/{s}" for (rd, s), (_, me) in results.items() if me["a_reading_was_returned"]]
    # stop B3: under the primary reading the twins are one input, so every transplant is a null transplant
    b3 = [f"{PRIMARY}/{s}" for s in SEEDS
          if not (results[(PRIMARY, s)][1]["fresh_twins"]["inputs_identical"]
                  and results[(PRIMARY, s)][1]["fresh_twins"]["states_identical"]
                  and results[(PRIMARY, s)][0]["dev_twins"]["states_identical"])]
    nulls = [f"{rd}/{s}" for (rd, s), (_, me) in results.items() if not me["null_bit_identical_at_every_site_set"]]
    save("summary.json", dict(
        checkpoint_sha256=shas, torch=torch.__version__, device=str(DEVICE), seconds=time.time() - t0,
        primary_reading_of_the_solver=PRIMARY,
        stop_B2_a_reading_was_returned_on=any_reading, stop_B3_twins_not_identical_on=b3,
        stop_B4_null_transplant_differs_on=nulls,
        runs={f"{rd}/{s}": dict(status=me["status"], nomination=n["primary"]["status"],
                                stricter=n["stricter"]["status"], gate=me["gate"],
                                dev_site_sets_clearing=n["site_sets_clearing"],
                                fresh_site_sets_clearing=me["fresh_site_sets_clearing"],
                                best_piece_correct=n["best_piece_correct"], fits=n["fits"])
              for (rd, s), (n, me) in results.items()}))
    lines = table(results)
    lines += [f"stop B2, a reading was returned on: {any_reading or 'none'}",
              f"stop B3, twins not identical under the primary reading on: {b3 or 'none'}",
              f"stop B4, null transplant differs on: {nulls or 'none'}"]
    with open(os.path.join(OUT, "table.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    log("\n".join(lines))
    log(f"done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
