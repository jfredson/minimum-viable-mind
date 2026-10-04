"""The short pre-stated run of 2026-10-03: three parts, ruled by John in
docs/rulings/2026-10-03-controls-rerun-rulings.md.

UNREGISTERED rehearsal code. Method, committed before this was run:
docs/2026-10-03-short-prestated-run-method.md. Section numbers in comments are
that file's. Loads the twelve committed base-recipe toy models; trains nothing
but small logistic regressions; processor only; $0.

    cd experiments/rehearsal-successor-measure/src
    ../../../.venv/bin/python short_prestated_run.py

Writes ../out-short-prestated-run/{part_a,part_b,part_c_NOT_A_RESULT}.json and
table.md. Reads ../out-controls-rerun/summary.json for each model's site set.

Part (c) is a test that the other-agent control's code runs end to end. IT IS
NOT A RESULT, and its figures are not a pass or a fail of anything.
"""
from __future__ import annotations

import json
import os
import sys
import time

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import arms as A                # noqa: E402
import grammar as G             # noqa: E402
import rehearse as RH           # noqa: E402
import repairs as R             # noqa: E402
import rerun_controls as C      # noqa: E402
import rerun_v3 as V            # noqa: E402
import training as T            # noqa: E402
import transplant as X          # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "out-short-prestated-run"))
DEVICE = torch.device("cpu")
ARMS, SEEDS = C.ARMS, C.SEEDS
OWN_TURN_LEN, ACTION_TURN_BEFORE = 5, 5      # section 4: tokens of an assignment turn; tokens before the action


def log(*a):
    print(*a, flush=True)


def save(name, obj):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w") as f:
        json.dump(obj, f, indent=1, sort_keys=True, default=lambda o: list(o))


def first_own_turn(b):
    """First position at which the 'this turn is yours' signal is on."""
    assert bool((b["acting"].sum(1) > 0).all())
    return torch.argmax(b["acting"], dim=1)


def part_a(summ, fresh):
    """Section 3: the too-early-position control as redefined on both twins."""
    recip, donor = fresh
    B, S = recip["tokens"].shape
    idx = torch.arange(S)[None].expand(B, -1)
    before_both = idx < torch.minimum(first_own_turn(recip), first_own_turn(donor))[:, None]
    d_tgt = donor["targets"][:, G.OWN]
    n_pos = before_both.sum(1)
    out = dict(pairs=B, positions_per_pair=dict(min=int(n_pos.min()), mean=float(n_pos.float().mean()),
                                                max=int(n_pos.max())), models={})
    for arm in ARMS:
        for seed in SEEDS:
            sha = C.check_sha(arm, seed)                                     # stop S1
            m = V.load_model(arm, seed, DEVICE)
            spec = summ[f"{arm}/{seed}"]["primary"]["site_set"]
            L = tuple(spec["layers"])
            sites = X.Sites(L, spec["positions"])
            with torch.no_grad():
                clean = m(recip)
            d_states, r_states = X.capture(m, donor), X.capture(m, recip)
            moved = R.run(m, recip, d_states, sites, before_both, None)
            null = R.run(m, recip, r_states, sites, before_both, None)
            row = dict(
                site_set=spec, checkpoint_sha256=sha,
                described_only=summ[f"{arm}/{seed}"]["primary"]["described_only"],
                outputs_bit_identical=bool(torch.equal(clean, moved)),
                largest_output_difference=float((clean - moved).abs().max()),
                donor_value_share=float(R.hits(moved, d_tgt, G.OWN).mean()),
                no_transplant_share=float(R.hits(clean, d_tgt, G.OWN).mean()),
                trials_whose_action_changed=int((X.predictions(moved, G.OWN) != X.predictions(clean, G.OWN)).sum()),
                null_transplant_at_these_positions_bit_identical=bool(torch.equal(clean, null)),
                twins_states_identical_at_the_sites=all(
                    bool(torch.equal(d_states[l][before_both], r_states[l][before_both])) for l in L))
            row["holds"] = row["outputs_bit_identical"]
            out["models"][f"{arm}/{seed}"] = row
            log(f"(a) {arm}/{seed}: layers {L} | bit-identical {row['outputs_bit_identical']} | "
                f"donor-value share {row['donor_value_share']:.4f} | no transplant {row['no_transplant_share']:.4f} | "
                f"null at these positions {row['null_transplant_at_these_positions_bit_identical']} | "
                f"twins' states identical {row['twins_states_identical_at_the_sites']}")
    return out


def other_positions(positions):
    """Section 4: the positions, other than the action position, a piece's
    accuracy is taken at. Each is (name, anchor, offset): the action position
    plus a negative offset, or the model's first own turn plus an offset."""
    if positions == "action":
        return []
    if positions == "action+ans":
        return [("1 before the action", "action", -1)]
    if positions == "action+3":
        return [(f"{k} before the action", "action", -k) for k in (1, 2, 3)]
    if positions == "post-identity":
        return ([(f"first own turn, token {k + 1} of {OWN_TURN_LEN}", "first", k) for k in range(OWN_TURN_LEN)]
                + [(f"{k} before the action", "action", -k) for k in range(ACTION_TURN_BEFORE, 0, -1)])
    raise ValueError(positions)


def part_b(summ, dev):
    """Section 4: the chosen piece's accuracy at the other positions of its site."""
    y = R.read_labels(dev, "own")
    assert len(y) - int(0.7 * len(y)) == C.HELD_OUT
    B = dev["tokens"].shape[0]
    rows = torch.arange(B)
    ap, fo = dev["action_pos"][:, G.OWN], first_own_turn(dev)
    assert bool((fo + OWN_TURN_LEN - 1 < ap - ACTION_TURN_BEFORE).all())
    out = {}
    for arm in ARMS:
        for seed in SEEDS:
            m = V.load_model(arm, seed, DEVICE)
            spec = summ[f"{arm}/{seed}"]["primary"]["site_set"]
            coefs = {l: v["coef"] for l, v in R.load_reads(arm, "base", seed, DEVICE)["own"].items()}
            with torch.no_grad():
                _, states = m(dev, capture=True)
            L = spec["layers"]
            Q = {l: RH.basis_for(coefs[l], spec["rank"], DEVICE).numpy() for l in L}

            def counts(feature):
                """Worst layer's (whole state, piece) held-out counts, of 180."""
                per = [(C.correct_count(feature(l), y), C.correct_count(feature(l) @ Q[l], y)) for l in L]
                return dict(whole=min(p[0] for p in per), piece=min(p[1] for p in per))

            at_action = counts(lambda l: states[l][rows, ap].numpy())
            entries = []
            for name, anchor, off in other_positions(spec["positions"]):
                where = (ap if anchor == "action" else fo) + off
                entries.append(dict(position=name, **counts(lambda l: states[l][rows, where].numpy())))
            span_mean = None
            if spec["positions"] != "action":
                mask = X.position_mask(dev, spec["positions"])
                mask[rows, ap] = False
                assert bool((mask.sum(1) > 0).all())
                w = mask.float()
                span_mean = counts(lambda l: ((states[l] * w[..., None]).sum(1) / w.sum(1, keepdim=True)).numpy())
            row = dict(site_set=spec, described_only=summ[f"{arm}/{seed}"]["primary"]["described_only"],
                       at_the_action_position=at_action,
                       matches_the_controls_rerun=(at_action["piece"] == spec["piece_correct"]
                                                   and at_action["whole"] == spec["whole_read_correct"]),
                       other_positions=entries, mean_over_the_other_positions=span_mean)
            out[f"{arm}/{seed}"] = row
            log(f"(b) {arm}/{seed}: layers {tuple(L)} at {spec['positions']}, {spec['rank']} directions | action "
                f"{at_action['whole']}/{at_action['piece']} (matches the re-run: {row['matches_the_controls_rerun']}) | "
                + ("single position" if not entries else
                   "; ".join(f"{e['position']} {e['whole']}/{e['piece']}" for e in entries)
                   + f"; mean over the other positions {span_mean['whole']}/{span_mean['piece']}"))
    return out


def part_c(gate, dev, dev_swap, fresh, fresh_swap):
    """Section 5: NOT A RESULT. The other-agent control's committed function,
    rerun_controls.control2, run once on arm F seed 0 with the piece's
    accuracy floor switched off, to see that the code runs end to end."""
    arm, seed = "F", 0
    m = V.load_model(arm, seed, DEVICE)
    reads = R.load_reads(arm, "base", seed, DEVICE)
    floor = C.PIECE_MIN
    C.PIECE_MIN = 0                                      # the floor, switched off
    try:
        raw = C.control2(m, arm, seed, reads, dev[0], dev_swap, fresh[0], fresh_swap,
                         gate["runs"][f"{arm}/{seed}"]["other_correct"])
    finally:
        C.PIECE_MIN = floor
    ran = "own_directed_moved" in raw
    raw.pop("status", None)                              # the withdrawn pass line's label is not reported
    out = dict(NOT_A_RESULT="a test that the code runs end to end, with the accuracy floor switched off; "
                            "its figures are not a pass or a fail of anything",
               arm=arm, seed=seed, ran_end_to_end=ran, returned=raw)
    log(f"(c) NOT A RESULT. F/0 with the floor switched off: ran end to end {ran}"
        + (f" | site set {raw['site_set']} | own-directed action moved {raw['own_directed_moved']:.4f}, under a random "
           f"piece {raw['own_directed_moved_random_piece']:.4f} | named-other action moved {raw['named_other_moved']:.4f}"
           if ran else f" | reason {raw.get('reason')}"))
    return out


def main():
    t0 = time.time()
    summ = json.load(open(os.path.join(C.OUT, "summary.json")))["arms"]
    gate = json.load(open(os.path.join(V.OUT, "gate.json")))
    dev_pairs, _ = T.make_data(600, seed=4242, pool="dev", device=DEVICE)
    fresh_pairs, _ = T.make_data(800, seed=777, pool="fresh", device=DEVICE)
    dev, fresh = C.batches(dev_pairs), C.batches(fresh_pairs)
    dev_swap = A.to_torch(G.batch(R.named_swap(dev_pairs, seed=4243)), DEVICE)
    fresh_swap = A.to_torch(G.batch(R.named_swap(fresh_pairs, seed=781)), DEVICE)
    meta = dict(torch=torch.__version__, device=str(DEVICE))

    a = part_a(summ, fresh)
    save("part_a.json", dict(meta, **a))
    b = part_b(summ, dev[0])
    save("part_b.json", dict(meta, models=b))
    c = part_c(gate, dev, dev_swap, fresh, fresh_swap)
    save("part_c_NOT_A_RESULT.json", dict(meta, **c))

    lines = ["## (a) The too-early-position control as redefined: positions before both twins' first own turns", "",
             "| arm/seed | layers | outputs bit-identical (holds) | share landing on the donor's value | no-transplant share | trials whose action changed |",
             "|---|---|---|---|---|---|"]
    for k, r in a["models"].items():
        lines.append(f"| {k} | {tuple(r['site_set']['layers'])} | {'identical' if r['outputs_bit_identical'] else 'DIFFERS'} | "
                     f"{r['donor_value_share']:.4f} | {r['no_transplant_share']:.4f} | {r['trials_whose_action_changed']} |")
    lines += ["", "## (b) The chosen piece's accuracy at the other positions of its site (reported; no pass line)", "",
              "Each cell is whole state / piece, correct of 180 held-out development episodes.", "",
              "| arm/seed | site set | at the action position | at each other position | mean over the other positions |",
              "|---|---|---|---|---|"]
    for k, r in b.items():
        s = r["site_set"]
        note = " (described only; no reading)" if r["described_only"] else ""
        other = "single position" if not r["other_positions"] else "; ".join(
            f"{e['position']}: {e['whole']} / {e['piece']}" for e in r["other_positions"])
        sm = r["mean_over_the_other_positions"]
        lines.append(f"| {k} | layers {tuple(s['layers'])} at {s['positions']}, {s['rank']} directions{note} | "
                     f"{r['at_the_action_position']['whole']} / {r['at_the_action_position']['piece']} | {other} | "
                     f"{'' if sm is None else str(sm['whole']) + ' / ' + str(sm['piece'])} |")
    lines += ["", "## (c) NOT A RESULT: the other-agent control's code path, arm F seed 0, floor switched off", "",
              f"ran end to end: {c['ran_end_to_end']}"]
    if c["ran_end_to_end"]:
        r = c["returned"]
        lines.append(f"site set {r['site_set']}; own-directed action moved {r['own_directed_moved']:.4f}; under a random "
                     f"piece {r['own_directed_moved_random_piece']:.4f}; named-other action moved {r['named_other_moved']:.4f}. "
                     "These figures are not a pass or a fail of anything.")
    lines.append("")
    with open(os.path.join(OUT, "table.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    log("\n".join(lines))
    log(f"done in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
