"""Where a negative reading comes from, recorded rather than remembered.

UNREGISTERED. Rehearsal item R-4 asks that a negative reading — the
ownership-only transplant beating the whole-state one — be shown to be a real
outcome of this instrument and not an impossible one. Searched over every
architecture, every site set, every reading of the read's label and every rank
cap on **fresh episodes**, no configuration produced one. On the
**unseen-vocabulary** episodes it happens immediately.

That is not a curiosity, it is the condition: a negative reading appears when
the subspace was chosen on data whose vocabulary the reading is then taken on.
The nominated directions were fitted on marker words the arm was trained on;
evaluated on marker words it has never seen, the whole-state transplant is
capped by the arm's own degraded accuracy while the narrow subspace patch,
built out of directions that live in the well-trained part of the space, is
not. The subspace then beats the superspace and the reading goes below zero.

Which is exactly what the proposal says a negative reading is for: a warning
about the instrument, reported as observed and never quietly clipped to zero.

    ../../../.venv/bin/python negative_case.py
"""
from __future__ import annotations

import rehearse as R
import training as T
import transplant as X
import measure as M

POOL = "unseen-vocabulary"


def main():
    device = T.pick_device()
    nom = R.load_json("nominate.json")
    pairs, _ = T.make_data(400, seed=780, pool=POOL, device=device)
    out = {"pool": POOL, "arms": {},
           "why": ("the nominated subspace was chosen on marker words the arm "
                   "was trained on, and the reading is taken on marker words it "
                   "has never seen")}
    for arm in R.A.ARMS:
        for seed in R.SEEDS:
            key = f"{arm}/{seed}"
            m = R.load_arm(arm, seed, device)
            spec = nom["arms"][key]["nomination"]
            sites = X.Sites(tuple(spec["layers"]), spec["positions"])
            recip, donor, d_states, d_tgt = R._states_and_targets(m, pairs, device)
            mask = X.position_mask(recip, spec["positions"])
            reads = R.load_reads(arm, seed)
            basis = {l: R.basis_for(reads[(spec["label"], l)]["coef"],
                                    spec["rank"], device) for l in sites.layers}
            u = R._donor_share(m(recip), d_tgt)
            w = R._donor_share(X.transplanted_logits(
                m, recip, d_states, sites, mask, None), d_tgt)
            o = R._donor_share(X.transplanted_logits(
                m, recip, d_states, sites, mask, basis), d_tgt)
            both = M.both_forms(w, o, u, floor=R.REHEARSAL_FLOOR)
            own_acc = T.accuracy(m, recip)["own"]
            out["arms"][key] = dict(
                accuracy_untouched=u, accuracy_whole=w,
                accuracy_ownership_only=o,
                the_arm_itself_own_directed=own_acc,
                registered_status=both["registered"]["status"],
                registered_degree=both["registered"]["degree"],
                floor_corrected_status=both["floor_corrected"]["status"],
                floor_corrected_degree=both["floor_corrected"]["degree"])
            r = out["arms"][key]
            print(f"  {key:6s} the arm itself {own_acc:.4f}   untouched {u:.4f}  "
                  f"whole {w:.4f}  ownership-only {o:.4f}  -> "
                  f"{r['registered_status']}"
                  + (f" degree {r['registered_degree']:.4f}"
                     if r["registered_degree"] is not None else ""))
    neg = [k for k, v in out["arms"].items() if v["registered_status"] == M.NEGATIVE]
    out["negative_readings"] = neg
    print(f"  negative readings on {len(neg)} of {len(out['arms'])} arm-and-seed "
          f"combinations: {neg}")
    print(f"  wrote {R.save_json('negative_case.json', out)}")


if __name__ == "__main__":
    main()
