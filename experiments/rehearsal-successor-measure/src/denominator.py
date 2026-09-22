"""The denominator question, and the empty control cell, answered rather than
reasoned about.

UNREGISTERED. Runs the four checks D-1 to D-4 of
`docs/successor-measure-rehearsal-method-addendum-denominator-2026-09-21.md`,
committed before this file was written.

**Nothing here chooses a form for the registration text.** Both candidate
forms are computed and both are reported, everywhere. Which one is registered
is John's to rule on, on the evidence these checks produce.

Corrigibility: local, toy scale, no network, no rented machine, $0 [C1/C2].

    ../../../.venv/bin/python denominator.py --stage all
"""
from __future__ import annotations

import argparse
import json
import os

import numpy as np
import torch

import arms as A
import grammar as G
import measure as M
import rehearse as R
import training as T
import transplant as X

ATTENUATIONS = (1.00, 0.75, 0.50, 0.25)


def log(*a):
    print(*a, flush=True)


# ------------------------------------------------------- D-1, the simulation

def simulate(base_rate: float, effectiveness: float, outside_share: float,
             n_trials: int, rng) -> dict:
    """One made-up trial population, built from three numbers that are known
    because they were used to build it.

    - `base_rate` — the share of trials that land on the donor's value for
      reasons that have nothing to do with the transplant;
    - `effectiveness` — how often the whole-state transplant works at these
      sites;
    - `outside_share` — the true share of the identity-driven difference living
      OUTSIDE the nominated subspace. This is the quantity the measure claims
      to report, so it is what a correct form must return.

    Trials are drawn rather than computed from a closed form, so the numbers
    carry the estimator's own spread."""
    base = rng.random(n_trials) < base_rate
    works = rng.random(n_trials) < effectiveness
    inside = rng.random(n_trials) < (1.0 - outside_share)
    return dict(
        accuracy_untouched=float(base.mean()),
        accuracy_whole=float((base | works).mean()),
        accuracy_ownership_only=float((base | (works & inside)).mean()))


def stage_simulated(device=None):
    rng = np.random.default_rng(20260921)
    true_share = 0.5
    base_rate = 0.125          # the rate the proposal's sanity rule assumes
    cases = {
        "strong transplant": 0.8857,      # gives a whole-state accuracy near 0.90
        "weak transplant": 0.2571,        # gives a whole-state accuracy near 0.35
    }
    n_trials, repeats = 2000, 200
    out = {"true_outside_share": true_share, "base_rate": base_rate,
           "trials_per_draw": n_trials, "draws": repeats, "cases": {}}
    log(f"  a made-up population whose true share outside the subspace is "
        f"{true_share:.3f}, drawn {repeats} times at {n_trials} trials")
    for name, eff in cases.items():
        reg, cor, whole = [], [], []
        for _ in range(repeats):
            s = simulate(base_rate, eff, true_share, n_trials, rng)
            b = M.both_forms(s["accuracy_whole"], s["accuracy_ownership_only"],
                             s["accuracy_untouched"], floor=0.05)
            reg.append(b["registered"]["degree"])
            cor.append(b["floor_corrected"]["degree"])
            whole.append(s["accuracy_whole"])
        out["cases"][name] = dict(
            accuracy_whole=float(np.mean(whole)),
            registered_mean=float(np.mean(reg)), registered_sd=float(np.std(reg)),
            floor_corrected_mean=float(np.mean(cor)),
            floor_corrected_sd=float(np.std(cor)))
        c = out["cases"][name]
        log(f"    {name:18s} whole-state accuracy {c['accuracy_whole']:.4f}: "
            f"registered form {c['registered_mean']:.4f} "
            f"(spread {c['registered_sd']:.4f}), "
            f"floor-corrected form {c['floor_corrected_mean']:.4f} "
            f"(spread {c['floor_corrected_sd']:.4f})")
    a, b = out["cases"]["strong transplant"], out["cases"]["weak transplant"]
    reg_gap = abs(a["registered_mean"] - b["registered_mean"])
    cor_gap = abs(a["floor_corrected_mean"] - b["floor_corrected_mean"])
    out["registered_gap_between_the_two_cases"] = reg_gap
    out["floor_corrected_gap_between_the_two_cases"] = cor_gap
    out["registered_spread"] = max(a["registered_sd"], b["registered_sd"])
    out["floor_corrected_recovers_the_true_share"] = bool(
        abs(a["floor_corrected_mean"] - true_share) < 3 * a["floor_corrected_sd"]
        and abs(b["floor_corrected_mean"] - true_share) < 3 * b["floor_corrected_sd"])
    out["verdict"] = (
        "D-1 PASS: the floor-corrected form returns the true share in both cases "
        "and the registered form does not"
        if out["floor_corrected_recovers_the_true_share"]
        and reg_gap > 3 * out["registered_spread"]
        else "D-1 FAIL or no verdict: see the numbers")
    log(f"    {out['verdict']}")
    log(f"    gap between the two cases: registered form {reg_gap:.4f}, "
        f"floor-corrected form {cor_gap:.4f}")
    log(f"  wrote {R.save_json('denominator_simulated.json', out)}")


# -------------------------------------------- D-2, the real forward passes

def stage_attenuated(device):
    """The same question asked of the trained arms. The architecture, the
    sites and the subspace are held fixed, so the true share outside the
    subspace does not change; only how far the state is moved toward the
    donor's does."""
    nom = R.load_json("nominate.json")
    fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=device)
    out = {"attenuations": list(ATTENUATIONS), "arms": {}}
    for arm in A.ARMS:
        for seed in R.SEEDS:
            key = f"{arm}/{seed}"
            m = R.load_arm(arm, seed, device)
            spec = nom["arms"][key]["nomination"]
            sites = X.Sites(tuple(spec["layers"]), spec["positions"])
            recip, donor, d_states, d_tgt = R._states_and_targets(m, fresh_pairs, device)
            mask = X.position_mask(recip, spec["positions"])
            reads = R.fit_reads(m, recip, device)
            basis = {l: R.basis_for(reads[l]["coef"], spec["rank"], device)
                     for l in sites.layers}
            with torch.no_grad():
                untouched = R._donor_share(m(recip), d_tgt)
            rows = []
            for a in ATTENUATIONS:
                w = R._donor_share(X.transplanted_logits(
                    m, recip, d_states, sites, mask, None, alpha=a), d_tgt)
                o = R._donor_share(X.transplanted_logits(
                    m, recip, d_states, sites, mask, basis, alpha=a), d_tgt)
                both = M.both_forms(w, o, untouched, floor=0.02)
                rows.append(dict(attenuation=a, accuracy_whole=w,
                                 accuracy_ownership_only=o,
                                 accuracy_untouched=untouched,
                                 registered=both["registered"]["degree"],
                                 floor_corrected=both["floor_corrected"]["degree"],
                                 registered_status=both["registered"]["status"],
                                 floor_corrected_status=both["floor_corrected"]["status"]))
            reg = [r["registered"] for r in rows if r["registered"] is not None]
            cor = [r["floor_corrected"] for r in rows if r["floor_corrected"] is not None]
            out["arms"][key] = dict(
                site_set=spec, rows=rows,
                registered_range=(max(reg) - min(reg)) if len(reg) > 1 else None,
                floor_corrected_range=(max(cor) - min(cor)) if len(cor) > 1 else None)
            log(f"    {key:8s} whole-state accuracy {rows[0]['accuracy_whole']:.3f}"
                f" -> {rows[-1]['accuracy_whole']:.3f} across attenuation; "
                f"registered form spans "
                f"{out['arms'][key]['registered_range']}, floor-corrected form spans "
                f"{out['arms'][key]['floor_corrected_range']}")
    log(f"  wrote {R.save_json('denominator_attenuated.json', out)}")


# ------------------------------------------------ D-3, the untouched floor

def stage_floor(device):
    """The no-transplant rate, measured against both predictions on the
    record: the proposal's 'near one in eight', and the review's
    (1 - accuracy) / 7."""
    tr = R.load_json("transplant.json")
    gate = R.load_json("gate.json")
    out = {"prediction_in_the_proposal": 1 / 8, "arms": {}}
    for key, v in tr["arms"].items():
        acc = gate["learn_both"][key]["own"]
        review = (1 - acc) / 7
        out["arms"][key] = dict(
            measured_untouched=v["accuracy_untouched"],
            own_directed_accuracy=acc,
            prediction_from_the_review=review,
            proposal_rule_would_pass=abs(v["accuracy_untouched"] - 1 / 8) < 0.05)
        log(f"    {key:8s} measured no-transplant rate {v['accuracy_untouched']:.4f}"
            f"   proposal says {1/8:.4f}, the review's formula says {review:.4f}")
    log(f"  wrote {R.save_json('denominator_floor.json', out)}")


# --------------------------------------- D-4, whether cell one can be filled

def stage_control6(device=None):
    """Whether control 6's same-value cell can be populated at all under a
    grammar that keeps the four values within an item distinct."""
    out = {}

    def count_same(pairs) -> tuple:
        same = 0
        for p in pairs:
            c = p["content"]
            r, d = p["recipient"]["model"], p["donor"]["model"]
            if int(c["values"][r, c["own_item"]]) == int(c["values"][d, c["own_item"]]):
                same += 1
        return same, len(pairs)

    strict = G.make_pairs(4000, seed=4321, pool="fresh")
    s_same, s_n = count_same(strict)
    out["distinctness_preserving_grammar"] = dict(
        same_value_trials=s_same, trials=s_n,
        reason=("within an item the four values are distinct and the successor "
                "rule is one-to-one, so two agents can never dictate the same "
                "answer; the cell is empty by construction, not by bad luck"))
    log(f"    distinctness-preserving grammar: {s_same} same-value trials "
        f"out of {s_n}")

    relaxed = G.make_pairs(4000, seed=4322, pool="fresh", collide=True)
    r_same, r_n = count_same(relaxed)
    # what populating the cell costs: on a trial where two of the four agents
    # share a value, a solver that cannot tell which agent it is lands on the
    # right value one time in two rather than one in four
    rng = np.random.default_rng(99)
    blind_hits_relaxed = blind_hits_strict = 0
    n_rel = n_str = 0
    for p, store in ((relaxed, "rel"), (strict, "str")):
        for pair in p:
            e = pair["recipient"]
            want = G.successor(int(e["values"][e["model"], e["own_item"]]))
            guess = int(rng.integers(G.N_AGENTS))
            got = G.successor(int(e["values"][guess, e["own_item"]]))
            if store == "rel":
                n_rel += 1; blind_hits_relaxed += int(got == want)
            else:
                n_str += 1; blind_hits_strict += int(got == want)
    out["relaxed_grammar"] = dict(
        same_value_trials=r_same, trials=r_n,
        blind_solver_on_the_relaxed_set=blind_hits_relaxed / n_rel,
        blind_solver_on_the_strict_set=blind_hits_strict / n_str,
        note=("relaxing distinctness is the only way found to populate the cell, "
              "and it moves the reference a solver that cannot tell which agent "
              "it is can reach, on exactly the trials it populates"))
    log(f"    relaxed grammar: {r_same} same-value trials out of {r_n}; "
        f"the blind solver's reference moves from "
        f"{blind_hits_strict / n_str:.4f} to {blind_hits_relaxed / n_rel:.4f}")
    out["verdict"] = (
        "D-4 PASS: the cell is empty by construction under distinctness "
        "and can only be filled by relaxing it, at a measured cost"
        if s_same == 0 and r_same > 0 else "D-4 FAIL: see the counts")
    log(f"    {out['verdict']}")
    log(f"  wrote {R.save_json('denominator_control6.json', out)}")


STAGES = dict(simulated=stage_simulated, attenuated=stage_attenuated,
              floor=stage_floor, control6=stage_control6)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", default="all", choices=["all"] + list(STAGES))
    ap.add_argument("--device", default="auto")
    a = ap.parse_args()
    device = T.pick_device(a.device)
    for n in (list(STAGES) if a.stage == "all" else [a.stage]):
        log(f"\n=== check: {n} ===")
        STAGES[n](device)


if __name__ == "__main__":
    main()
