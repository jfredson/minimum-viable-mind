"""The toy re-run under the version 3 rules (RT-212 to RT-216): the driver.

UNREGISTERED. Runs the method committed at
`docs/toy-rerun-v3-rules-method-2026-09-26.md` before any of this was built.
`repairs.py` is left exactly as merged (pull request 52); this file imports its
helpers and adds the five rule changes John ruled on 2026-09-26. No arm is
trained here: the models are the repairs run's, read in place from the repairs
worktree (method file, section 1). Local, toy scale, no network, $0.

    PY=~/Code/minimum-viable-mind/.venv/bin/python
    $PY rerun_v3.py --stage gate
    $PY rerun_v3.py --stage nominate --arms T,C,F,M
    $PY rerun_v3.py --stage null --arms T          # one process per arm is fine
    $PY rerun_v3.py --stage measure --arms T,C,F,M
    $PY rerun_v3.py --stage table

Outputs go to `../out-v3-rules/`; nothing under `../out-repairs/` is written.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import time

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression

import arms as A
import grammar as G
import rehearse as RH
import repairs as R
import training as T
import transplant as X

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "out-v3-rules"))
COMMITTED = R.OUT                      # ../out-repairs, the committed outputs
CKPT_DIR = os.path.expanduser(
    "~/Code/minimum-viable-mind/.claude/worktrees/w1c-rehearsal-repairs/"
    "experiments/rehearsal-successor-measure/out-repairs")
RECIPE = "base"
SEEDS = (0, 1, 2)
ARMS = ("T", "C", "F", "M")

# ---- rule 3: every contiguous layer set of the five states x four position sets
N_STATES = 5
CONTIGUOUS = [tuple(range(a, b + 1)) for a in range(N_STATES) for b in range(a, N_STATES)]
FOUR_POSITIONS = ["action", "action+ans", "action+3", "post-identity"]
# the tie-break order is the repairs driver's (its POSITION_SETS), unchanged
POS_ORDER = list(R.POSITION_SETS)
assert POS_ORDER == FOUR_POSITIONS + ["all"], POS_ORDER
GRID_SITES = [(L, P) for L in CONTIGUOUS for P in POS_ORDER]            # 75, the union
V60 = {(L, P) for L in CONTIGUOUS for P in FOUR_POSITIONS}               # before the exclusion
OLD44 = {(tuple(L), P) for L, P in R.SITE_SETS}
assert len(CONTIGUOUS) == 15 and len(V60) == 60 and len(OLD44) == 44
assert OLD44 <= set(GRID_SITES)

# ---- rule 1
FIT_FLOOR = 0.8
N_PERM = 200
# ---- rule 2
N_RANDOM = 20
C3_PERCENTILE = 95
V2_ROOM = 0.0175                       # printed beside rule 2 for continuity only
# ---- rule 5
OWN_ONLY_GATE = {"T", "C", "M"}        # arm F keeps learn-both


def log(*a):
    print(*a, flush=True)


def save(name, obj):
    os.makedirs(OUT, exist_ok=True)
    p = os.path.join(OUT, name)
    with open(p, "w") as f:
        json.dump(obj, f, indent=2, sort_keys=True, default=_json_default)
    return p


def load(name, where=OUT):
    with open(os.path.join(where, name)) as f:
        return json.load(f)


def _json_default(o):
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, tuple):
        return list(o)
    raise TypeError(type(o))


def ckpt(arm, seed):
    return os.path.join(CKPT_DIR, f"ckpt_{arm}_{RECIPE}_seed{seed}.pt")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_model(arm, seed, device):
    """K1: strict load, so a missing or unexpected weight raises."""
    m = R.build_for(arm)().to(device)
    m.load_state_dict(torch.load(ckpt(arm, seed), map_location=device), strict=True)
    return m.eval()


def committed_nomination_row(arm, seed):
    for f in ("nominate_base_T_C.json", "nominate_base_F.json", "nominate_base_M.json"):
        d = load(f, COMMITTED)["arms"]
        if f"{arm}/{RECIPE}/{seed}" in d:
            return d[f"{arm}/{RECIPE}/{seed}"]
    raise KeyError((arm, seed))


def dev_batches(device):
    pairs, _ = T.make_data(600, seed=4242, pool="dev", device=device)
    recip = A.to_torch(G.batch([p["recipient"] for p in pairs]), device)
    donor = A.to_torch(G.batch([p["donor"] for p in pairs]), device)
    return recip, donor


def fresh_batches(device):
    pairs, _ = T.make_data(800, seed=777, pool="fresh", device=device)
    recip = A.to_torch(G.batch([p["recipient"] for p in pairs]), device)
    donor = A.to_torch(G.batch([p["donor"] for p in pairs]), device)
    return recip, donor


def committed_reads(arm, seed):
    z = np.load(os.path.join(COMMITTED, f"reads_{arm}_{RECIPE}_seed{seed}.npz"))
    return {int(k.split("|")[1]): z[k] for k in z.files if k.startswith("own|")}


# ------------------------------------------------------------------- gate

def stage_gate(device, arms, seeds):
    """K3 and rule 5."""
    _, dev_b = T.make_data(1500, seed=99, pool="dev", device=device)
    assert dev_b["tokens"].shape[0] == R.GATE_EPISODES
    committed = load("gate_base.json", COMMITTED)["runs"]
    runs, k3 = {}, {}
    for arm in arms:
        for seed in seeds:
            m = load_model(arm, seed, device)
            acc = T.accuracy(m, dev_b)
            own_c = int(round(acc["own"] * acc["n"]))
            oth_c = int(round(acc["other"] * acc["n"]))
            c = committed[f"{arm}/{RECIPE}/{seed}"]
            k3[f"{arm}/{seed}"] = dict(own=own_c, other=oth_c,
                                       committed_own=c["own_correct"],
                                       committed_other=c["other_correct"],
                                       equal=(own_c == c["own_correct"]
                                              and oth_c == c["other_correct"]))
            runs[f"{arm}/{seed}"] = dict(own_correct=own_c, other_correct=oth_c,
                                         own_clears=own_c >= R.GATE_MIN_CORRECT,
                                         other_clears=oth_c >= R.GATE_MIN_CORRECT)
            log(f"    {arm}/{seed}: own {own_c}, named-other {oth_c}   "
                f"(committed {c['own_correct']}, {c['other_correct']})")
    verdicts = {}
    for arm in arms:
        rows = [runs[f"{arm}/{s}"] for s in seeds]
        own_n = sum(r["own_clears"] for r in rows)
        oth_n = sum(r["other_clears"] for r in rows)
        rule = "own-directed only" if arm in OWN_ONLY_GATE else "learn-both"
        passes = own_n >= 2 if arm in OWN_ONLY_GATE else (own_n >= 2 and oth_n >= 2)
        verdicts[arm] = dict(rule=rule, own_seeds_clearing=own_n,
                             other_seeds_clearing=oth_n, passes=passes,
                             version2_learn_both=(own_n >= 2 and oth_n >= 2))
        log(f"  gate {arm} ({rule}): own {own_n}/3, named-other {oth_n}/3 -> "
            f"{'passes' if passes else 'fails'}")
    log(f"  wrote {save('gate.json', dict(runs=runs, verdicts=verdicts, K3=k3, bar=dict(episodes=R.GATE_EPISODES, min_correct=R.GATE_MIN_CORRECT)))}")


# -------------------------------------------------------------- nominate

def pick(grid, allowed):
    """The repairs rule, steps 3 and 4 (repairs.nominate), over the site sets
    `allowed` admits. Nothing in it names an arm."""
    pos_index = {P: i for i, P in enumerate(POS_ORDER)}
    clearing = [g for g in grid if g["floor"]["clears"]
                and allowed((tuple(g["layers"]), g["positions"]))]
    if not clearing:
        return None, None
    smallest = {}
    for g in clearing:
        key = (len(g["layers"]), g["layers"])
        if g["positions"] not in smallest or key < smallest[g["positions"]]:
            smallest[g["positions"]] = key
    cands = [g for g in clearing if (len(g["layers"]), g["layers"]) == smallest[g["positions"]]]
    best = min(cands, key=lambda g: (-g["accuracy_ownership_only"], g["rank"],
                                     pos_index[g["positions"]]))
    sens = min(clearing, key=lambda g: (-g["accuracy_ownership_only"], len(g["layers"]),
                                        g["rank"], pos_index[g["positions"]], g["layers"]))
    return best, sens


def spec_of(g):
    return None if g is None else dict(layers=list(g["layers"]), positions=g["positions"],
                                       rank=g["rank"])


def stage_nominate(device, arms, seeds):
    recip, donor = dev_batches(device)
    # the widened exclusion, checked on the data (method 3.3)
    spans_all = {P: float(X.position_mask(recip, P).all(1).float().mean()) for P in POS_ORDER}
    excluded = {(L, P) for (L, P) in V60 if spans_all[P] > 0}
    family60 = V60 - excluded
    assert len(family60) == 60, (len(family60), spans_all)
    for arm in arms:
        for seed in seeds:
            t0 = time.time()
            m = load_model(arm, seed, device)
            # K2: refit the reads, compare with the committed ones
            refit = R.fit_reads(m, recip, "own", G.OWN)
            com_row = committed_nomination_row(arm, seed)
            com_reads = committed_reads(arm, seed)
            k2 = {}
            for l in range(N_STATES):
                fa, cfa = refit[l]["fit_accuracy"], com_row["fit_accuracy"]["own"][str(l)]
                diff = float(np.abs(refit[l]["coef"] - com_reads[l]).max())
                k2[l] = dict(fit_accuracy=fa, committed_fit_accuracy=cfa,
                             coef_max_abs_diff=diff,
                             equal=(round(fa, 4) == round(cfa, 4) and diff <= 1e-4))
            # the grid, over the union of both families (method 3.3, last item)
            d_states = X.capture(m, donor)
            d_tgt = donor["targets"][:, G.OWN]
            with torch.no_grad():
                clean = m(recip)
            u = float(R.hits(clean, d_tgt, G.OWN).mean())
            acc = float(R.hits(clean, recip["targets"][:, G.OWN], G.OWN).mean())
            grid = []
            for L, P in GRID_SITES:
                sites = X.Sites(layers=L, positions=P)
                mask = X.position_mask(recip, P)
                whole = float(R.hits(R.run(m, recip, d_states, sites, mask, None),
                                     d_tgt, G.OWN).mean())
                fl = R.floor_check(whole, u, acc)
                for r in R.RANK_CAPS:
                    basis = {l: RH.basis_for(com_reads[l], r, device) for l in L}
                    own = float(R.hits(R.run(m, recip, d_states, sites, mask, basis),
                                       d_tgt, G.OWN).mean())
                    grid.append(dict(layers=list(L), positions=P, rank=r,
                                     accuracy_whole=whole, accuracy_ownership_only=own,
                                     floor=fl))
            layer0_noop = {P: next(g["accuracy_whole"] for g in grid
                                   if g["layers"] == [0] and g["positions"] == P) == u
                           for P in ("action+ans", "action+3")}
            old44, old44_sens = pick(grid, lambda s: s in OLD44)
            v60, v60_sens = pick(grid, lambda s: s in family60)
            v60_no_l0_inj, _ = pick(grid, lambda s: s in family60
                                    and not (0 in s[0] and s[1] != "action"))
            v60_no_l0, _ = pick(grid, lambda s: s in family60 and 0 not in s[0])
            com_spec = spec_of(com_row["ownership"]["nomination"])
            k4 = dict(recomputed=spec_of(old44), committed=com_spec,
                      equal=spec_of(old44) == com_spec)
            clear60 = {(tuple(g["layers"]), g["positions"]) for g in grid
                       if g["floor"]["clears"] and (tuple(g["layers"]), g["positions"]) in family60}
            res = dict(
                arm=arm, seed=seed, checkpoint=ckpt(arm, seed),
                checkpoint_sha256=sha256(ckpt(arm, seed)),
                K2=k2, K4=k4,
                fit_accuracy={l: refit[l]["fit_accuracy"] for l in range(N_STATES)},
                untouched=u, arm_accuracy=acc,
                family=dict(site_sets=len(family60), comparisons=len(family60) * len(R.RANK_CAPS),
                            share_of_episodes_where_position_set_spans_every_position=spans_all,
                            excluded_by_widened_rule=sorted(map(list, excluded))),
                layer0_whole_equals_untouched_inside_action_turn=layer0_noop,
                site_sets_clearing_of_60=len(clear60),
                nomination_v60=v60, sensitivity_v60_highest_over_every_clearing_set=v60_sens,
                nomination_old44=old44, sensitivity_old44=old44_sens,
                unruled_v60_with_layer0_injection_sets_removed_before_choosing=v60_no_l0_inj,
                unruled_v60_with_every_layer0_set_removed_before_choosing=v60_no_l0,
                grid=grid)
            p = save(f"nominate_{arm}_seed{seed}.json", res)
            log(f"    {arm}/{seed}: 60-set {spec_of(v60)}; 44-set {spec_of(old44)} "
                f"(committed {com_spec}, K4 {k4['equal']}); K2 "
                f"{all(v['equal'] for v in k2.values())}; {time.time() - t0:.0f}s -> {p}")


# ------------------------------------------------------------------- null

def action_states(m, b):
    with torch.no_grad():
        _, states = m(b, capture=True)
    ap = b["action_pos"][:, G.OWN]
    return [st[torch.arange(st.shape[0], device=st.device), ap].detach().cpu().numpy()
            for st in states]


def fit_score(h, y):
    n_tr = int(0.7 * len(y))
    clf = LogisticRegression(max_iter=3000, C=1.0)
    clf.fit(h[:n_tr], y[:n_tr])
    return float(clf.score(h[n_tr:], y[n_tr:]))


def stage_null(device, arms, seeds):
    """Rule 1's label-permutation null, every layer (method 3.1)."""
    recip, _ = dev_batches(device)
    y = R.read_labels(recip, "own")
    for arm in arms:
        for seed in seeds:
            t0 = time.time()
            m = load_model(arm, seed, device)
            hs = action_states(m, recip)
            layers = {}
            for l, h in enumerate(hs):
                real = fit_score(h, y)
                rng = np.random.default_rng([20260926, seed, l])
                null = np.array([fit_score(h, rng.permutation(y)) for _ in range(N_PERM)])
                layers[l] = dict(fit_accuracy=real, null_p95=float(np.percentile(null, 95)),
                                 null_p99=float(np.percentile(null, 99)),
                                 null_max=float(null.max()), null_mean=float(null.mean()),
                                 share_of_null_at_or_above_real=float((null >= real).mean()),
                                 null=null.tolist())
                log(f"    {arm}/{seed} layer {l}: fit {real:.4f}, null p95 "
                    f"{layers[l]['null_p95']:.4f}, p99 {layers[l]['null_p99']:.4f}")
            p = save(f"null_{arm}_seed{seed}.json",
                     dict(arm=arm, seed=seed, permutations=N_PERM, held_out=len(y) - int(0.7 * len(y)),
                          classes_present=int(len(np.unique(y))), layers=layers))
            log(f"    {arm}/{seed}: {time.time() - t0:.0f}s -> {p}")


# ---------------------------------------------------------------- measure

def random_bases(rank, layers, seed, D, device):
    out = []
    for k in range(N_RANDOM):
        rng = np.random.default_rng([20260926, seed, k])
        out.append({l: X.orthonormal(rng.normal(size=(rank, D))).to(device) for l in layers})
    return out


def read_site(m, recip, donor_states, d_tgt, u, acc, reads, spec, seed, device):
    """Every fresh-episode quantity for one site set (method 4)."""
    D = m.cfg.d_model
    L = tuple(spec["layers"])
    sites = X.Sites(L, spec["positions"])
    mask = X.position_mask(recip, spec["positions"])
    basis = {l: RH.basis_for(reads[l], spec["rank"], device) for l in L}
    w = float(R.hits(R.run(m, recip, donor_states, sites, mask, None), d_tgt, G.OWN).mean())
    o = float(R.hits(R.run(m, recip, donor_states, sites, mask, basis), d_tgt, G.OWN).mean())
    rand = [float(R.hits(R.run(m, recip, donor_states, sites, mask, rb), d_tgt, G.OWN).mean())
            for rb in random_bases(spec["rank"], L, seed, D, device)]
    p95 = float(np.percentile(rand, C3_PERCENTILE))
    # the single draw as the repairs driver made it, for continuity
    rng = np.random.default_rng(seed)
    old = {l: X.orthonormal(rng.normal(size=(spec["rank"], D))).to(device) for l in L}
    old_share = float(R.hits(R.run(m, recip, donor_states, sites, mask, old), d_tgt, G.OWN).mean())
    return dict(site_set=spec, reading=R.reading(w, o, u, acc),
                control3=dict(random_donor_shares=rand, p95=p95, ownership_only=o,
                              passes=o > p95, random_max=max(rand),
                              single_draw_as_repairs=old_share,
                              version2_form_passes=old_share <= u + V2_ROOM))


def verdicts(row_kind, spec, nom, null, gate_pass, read):
    """The order of verdicts in method section 4. None short-circuits another."""
    reasons = []
    if not gate_pass:
        reasons.append("arm failed its gate")
    if spec is None:
        reasons.append("no site set clears the whole-state floor")
        return dict(status="no verdict", reasons=reasons)
    L = spec["layers"]
    if 0 in L and (row_kind == "stricter" or spec["positions"] != "action"):
        reasons.append("layer 0 excluded (stricter variant)" if row_kind == "stricter"
                       else "at the acting channel's injection")
    fits = {l: nom["fit_accuracy"][str(l)] for l in L}
    worst = min(L, key=lambda l: (fits[l], l))
    fit = fits[worst]
    if fit < FIT_FLOOR:
        reasons.append("read failed its floor")
    if not read["reading"]["floor"]["clears"]:
        reasons.append("whole-state transplant misses the four-fifths floor on fresh episodes")
    if not read["control3"]["passes"]:
        reasons.append("control 3: ownership-only does not beat the 95th percentile of 20 random subspaces")
    nl = null["layers"][str(worst)]
    return dict(status="reading" if not reasons else "no verdict", reasons=reasons,
                fit_layer=worst, fit_accuracy=fit, fit_accuracy_per_layer=fits,
                fit_floor_passes=fit >= FIT_FLOOR,
                null_p95=nl["null_p95"], null_p99=nl["null_p99"])


def stage_measure(device, arms, seeds):
    recip, donor = fresh_batches(device)
    d_tgt = donor["targets"][:, G.OWN]
    gate = load("gate.json")["verdicts"]
    for arm in arms:
        for seed in seeds:
            t0 = time.time()
            nom = load(f"nominate_{arm}_seed{seed}.json")
            null = load(f"null_{arm}_seed{seed}.json")
            m = load_model(arm, seed, device)
            reads = committed_reads(arm, seed)
            with torch.no_grad():
                clean = m(recip)
            u = float(R.hits(clean, d_tgt, G.OWN).mean())
            acc = float(R.hits(clean, recip["targets"][:, G.OWN], G.OWN).mean())
            d_states = X.capture(m, donor)
            specs = dict(
                primary=spec_of(nom["nomination_v60"]),
                rule3_sensitivity_old44=spec_of(nom["nomination_old44"]),
                unruled_layer0_injection_removed=spec_of(
                    nom["unruled_v60_with_layer0_injection_sets_removed_before_choosing"]),
                unruled_every_layer0_removed=spec_of(
                    nom["unruled_v60_with_every_layer0_set_removed_before_choosing"]))
            cache, reads_out = {}, {}
            for name, spec in specs.items():
                if spec is None:
                    reads_out[name] = None
                    continue
                key = json.dumps(spec, sort_keys=True)
                if key not in cache:
                    cache[key] = read_site(m, recip, d_states, d_tgt, u, acc, reads, spec,
                                           seed, device)
                reads_out[name] = cache[key]
            gp = gate[arm]["passes"]
            rows = {}
            for kind, name in (("primary", "primary"), ("rule3", "rule3_sensitivity_old44"),
                               ("stricter", "primary")):
                spec = specs[name]
                v = verdicts(kind, spec, nom, null, gp, reads_out[name])
                rows[kind] = dict(site_set=spec, verdict=v, **(
                    {} if spec is None else dict(reading=reads_out[name]["reading"],
                                                 control3=reads_out[name]["control3"])))
            for name in ("unruled_layer0_injection_removed", "unruled_every_layer0_removed"):
                spec = specs[name]
                rows[name] = dict(site_set=spec, verdict=None if spec is None else
                                  verdicts("unruled", spec, nom, null, gp, reads_out[name]),
                                  **({} if spec is None else
                                     dict(reading=reads_out[name]["reading"],
                                          control3=reads_out[name]["control3"])))
            ps = specs["primary"]
            c7 = None
            if ps is not None:
                null_run = R.run(m, recip, X.capture(m, recip),
                                 X.Sites(tuple(ps["layers"]), ps["positions"]),
                                 X.position_mask(recip, ps["positions"]), None)
                c7 = bool(torch.equal(clean, null_run))
            res = dict(arm=arm, seed=seed, checkpoint_sha256=nom["checkpoint_sha256"],
                       gate=gate[arm], untouched_fresh=u, arm_own_accuracy_fresh=acc,
                       n_trials=int(d_tgt.shape[0]),
                       control7_null_transplant_bit_identical=c7, rows=rows)
            p = save(f"measure_{arm}_seed{seed}.json", res)
            pr = rows["primary"]
            log(f"    {arm}/{seed}: primary {ps} -> {pr['verdict']['status']} "
                f"{pr['verdict']['reasons']}; {time.time() - t0:.0f}s -> {p}")


# ------------------------------------------------------------------ table

def stage_table(device, arms, seeds):
    """Pure arithmetic on the files written above."""
    gate = load("gate.json")
    lines, summary = [], {"arms": {}, "gate": gate["verdicts"], "checks": {}}

    def site(s):
        return "none" if s is None else f"layers {tuple(s['layers'])} at {s['positions']}, rank {s['rank']}"

    def cell(row):
        v = row["verdict"]
        if row["site_set"] is None:
            return f"none | – | – | – | – | – | no verdict ({'; '.join(v['reasons'])})"
        rd, c3 = row["reading"], row["control3"]
        deg = rd["degree"]
        num = f"{deg:.4f}" if deg is not None else "none"
        status = "reading" if v["status"] == "reading" else f"no verdict ({'; '.join(v['reasons'])})"
        return (f"{site(row['site_set'])} | {v['fit_accuracy']:.3f} (layer {v['fit_layer']}) | "
                f"{v['null_p95']:.3f} / {v['null_p99']:.3f} | "
                f"{'passes' if v['fit_floor_passes'] else 'fails'} | "
                f"{c3['ownership_only']:.4f} vs {c3['p95']:.4f}: {'beats' if c3['passes'] else 'does not beat'} | "
                f"{num} | {status}")

    hdr = ("| arm/seed | row | site set | fit accuracy | null 95th / 99th | fit floor | "
           "control 3: ownership-only vs null 95th | chance-corrected number | verdict |\n"
           "|---|---|---|---|---|---|---|---|---|")
    lines.append(hdr)
    for arm in arms:
        for seed in seeds:
            ms = load(f"measure_{arm}_seed{seed}.json")
            nom = load(f"nominate_{arm}_seed{seed}.json")
            moved = spec_of(nom["nomination_v60"]) != spec_of(nom["nomination_old44"])
            summary["arms"][f"{arm}/{seed}"] = dict(
                primary=ms["rows"]["primary"]["verdict"],
                rule3=ms["rows"]["rule3"]["verdict"], stricter=ms["rows"]["stricter"]["verdict"],
                primary_site=spec_of(nom["nomination_v60"]),
                old44_site=spec_of(nom["nomination_old44"]), moved=moved,
                control3_primary=ms["rows"]["primary"].get("control3", {}).get("passes"),
                control7=ms["control7_null_transplant_bit_identical"])
            summary["checks"][f"{arm}/{seed}"] = dict(
                K2=all(v["equal"] for v in nom["K2"].values()), K4=nom["K4"]["equal"],
                K3=gate["K3"][f"{arm}/{seed}"]["equal"],
                layer0_noop_inside_action_turn=nom["layer0_whole_equals_untouched_inside_action_turn"])
            for kind, label in (("primary", "primary (60 sets)"),
                                ("rule3", "rule 3 row: 44-set nomination" + (" (moved)" if moved else " (same)")),
                                ("stricter", "rule 4 stricter")):
                lines.append(f"| {arm}/{seed} | {label} | {cell(ms['rows'][kind])} |")
    p = os.path.join(OUT, "table.md")
    with open(p, "w") as f:
        f.write("\n".join(lines) + "\n")
    log(f"  wrote {p}")
    log(f"  wrote {save('summary.json', summary)}")


STAGES = dict(gate=stage_gate, nominate=stage_nominate, null=stage_null,
              measure=stage_measure, table=stage_table)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True, choices=list(STAGES))
    ap.add_argument("--arms", default=",".join(ARMS))
    ap.add_argument("--seeds", default="0,1,2")
    ap.add_argument("--device", default="auto")
    a = ap.parse_args()
    device = T.pick_device(a.device)
    arms = a.arms.split(",")
    seeds = tuple(int(s) for s in a.seeds.split(","))
    log(f"\n=== rerun_v3 stage: {a.stage} ({device}) arms {arms} seeds {seeds} ===")
    t0 = time.time()
    STAGES[a.stage](device, arms, seeds)
    log(f"  ({time.time() - t0:.1f}s)")


if __name__ == "__main__":
    main()
