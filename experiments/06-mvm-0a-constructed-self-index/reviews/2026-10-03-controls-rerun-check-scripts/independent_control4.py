"""An independent test of the after-the-fact diagnostic of the too-early-position
control (control 4), written by the checking session of 2026-10-03.

It tests the two central claims of `src/posthoc_control4.py` and section 6 of
`docs/2026-10-03-controls-rerun.md` without using that script, the project's
position-mask function, its transplant function or its scoring function:

  claim 1  in about half the matched pairs the donor twin's first own turn
           comes before the recipient's;
  claim 2  with the transplant restricted to positions before BOTH twins'
           first own turns, it changes nothing.

What is written here from scratch: finding each twin's first own turn (from
the raw episode dictionaries), the position masks, the hook that swaps states,
and the scoring. What is reused, because there is no other way to get them:
the episode generator (`grammar.make_pairs`, same seed as the re-run), the
model loader, and the model's own forward pass.

It also asks three things the diagnostic did not:

  A  are the twins' inputs identical before both first own turns, and are the
     model's internal states there identical, layer by layer? If so the
     restricted transplant puts back what was already there, and "changes
     nothing" is true by construction, for any model.
  B  is the excess of the control as run found only in the pairs where the
     donor's first own turn is the earlier one?
  C  does the excess depend on the position set of the nominated site (which
     the findings say), or only on the layer and the model? The control's own
     positions never depend on the site's position set, so this runs the
     control as run at every single layer of every model.

Laptop, processor only, nothing trained, $0. Run from this folder:

    /Users/john/Code/minimum-viable-mind/.venv/bin/python independent_control4.py
"""
import json
import os
import sys

import numpy as np
import torch

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "..", "..", "rehearsal-successor-measure", "src"))
sys.path.insert(0, SRC)
import arms as A          # noqa: E402
import grammar as G       # noqa: E402
import rerun_v3 as V      # noqa: E402  (model loader only)

DEV = torch.device("cpu")
COMMITTED = os.path.join(SRC, "..", "out-controls-rerun", "summary.json")

pairs = G.make_pairs(800, seed=777, pool="fresh")
n = len(pairs)


def first_own_turn(ep):
    """First position whose 'this turn is yours' signal is on, by a plain scan."""
    for i, a in enumerate(ep["acting"]):
        if a == 1:
            return i
    raise AssertionError("an episode with no own turn")


fr = np.array([first_own_turn(p["recipient"]) for p in pairs])
fd = np.array([first_own_turn(p["donor"]) for p in pairs])
S = len(pairs[0]["recipient"]["tokens"])

print("== claim 1: whose first own turn comes first")
print(f"pairs: {n}")
print(f"donor's first own turn before the recipient's: {int((fd < fr).sum())} of {n} = {(fd < fr).mean():.4f}")
print(f"recipient's before the donor's:                {int((fr < fd).sum())} of {n} = {(fr < fd).mean():.4f}")
print(f"the same position:                             {int((fr == fd).sum())} of {n}")

print("\n== A: are the twins' inputs identical before both first own turns")
tok_same = all(np.array_equal(p["recipient"]["tokens"], p["donor"]["tokens"]) for p in pairs)
print(f"token sequences identical in every pair, at every position: {tok_same}")
lo = np.minimum(fr, fd)
sig_same = all(np.array_equal(p["recipient"]["acting"][:lo[i]], p["donor"]["acting"][:lo[i]])
               for i, p in enumerate(pairs))
print(f"'this turn is yours' signal identical before both first own turns, every pair: {sig_same}")
sig_diff_at = all(p["recipient"]["acting"][lo[i]] != p["donor"]["acting"][lo[i]] for i, p in enumerate(pairs))
print(f"and different at the earlier of the two first own turns, every pair: {sig_diff_at}")

keys = ["tokens", "acting", "assign_value_pos", "assign_marker_pos", "assign_agent_at",
        "agent_marker_tok", "action_pos", "action_item", "action_who", "targets"]


def stack(side):
    return {k: torch.as_tensor(np.stack([p[side][k] for p in pairs]), device=DEV) for k in keys}


recip, donor = stack("recipient"), stack("donor")
pos = torch.arange(S)[None].expand(n, -1)
before_recipient = pos < torch.as_tensor(fr)[:, None]              # the control as run
before_both = pos < torch.as_tensor(lo)[:, None]                   # the diagnostic's version
donor_first = torch.as_tensor(fd < fr)
slot_ids = torch.as_tensor(G.SLOT_IDS)
donor_value = donor["targets"][:, G.OWN]


def chosen_value(logits):
    """The value word chosen at the own-directed action, among the eight values."""
    return slot_ids[logits[:, G.OWN][:, slot_ids].argmax(-1)]


def swap_hook(donor_states, layers, mask):
    def fn(layer, state):
        if layer not in layers:
            return state
        out = state.clone()
        out[mask] = donor_states[layer][mask]
        return out
    return fn


committed = json.load(open(COMMITTED))["arms"]
print("\n== claim 2, A and B, at each model's nominated layers (from the committed summary.json)")
print("arm/seed | layers | no transplant | as run | as run, donor-first pairs | as run, recipient-first pairs | "
      "before both | outputs bit-identical before both | states identical before both, every layer | "
      "share of as-run sites where donor state differs")
rows = {}
for arm in ("T", "C", "F", "M"):
    for seed in (0, 1, 2):
        m = V.load_model(arm, seed, DEV)
        layers = tuple(committed[f"{arm}/{seed}"]["primary"]["site_set"]["layers"])
        with torch.no_grad():
            clean, r_states = m(recip, capture=True)
            _, d_states = m(donor, capture=True)
            as_run = m(recip, patch_fn=swap_hook(d_states, layers, before_recipient))
            both = m(recip, patch_fn=swap_hook(d_states, layers, before_both))
        hit = lambda lg: (chosen_value(lg) == donor_value).float()   # noqa: E731
        u, a, b = hit(clean), hit(as_run), hit(both)
        states_same = all(torch.equal(rs[before_both], ds[before_both]) for rs, ds in zip(r_states, d_states))
        differs = float(np.mean([float((r_states[l][before_recipient] != d_states[l][before_recipient])
                                       .any(-1).float().mean()) for l in layers]))
        # C: the control as run at every single layer
        per_layer = []
        for l in range(len(r_states)):
            with torch.no_grad():
                x = m(recip, patch_fn=swap_hook(d_states, (l,), before_recipient))
            per_layer.append(float(hit(x).mean() - u.mean()))
        rows[f"{arm}/{seed}"] = dict(
            layers=list(layers), untouched=float(u.mean()), as_run=float(a.mean()),
            as_run_donor_first=float(a[donor_first].mean()), untouched_donor_first=float(u[donor_first].mean()),
            as_run_recipient_first=float(a[~donor_first].mean()),
            untouched_recipient_first=float(u[~donor_first].mean()),
            before_both=float(b.mean()), outputs_bit_identical_before_both=bool(torch.equal(clean, both)),
            outputs_bit_identical_as_run_recipient_first=bool(torch.equal(clean[~donor_first], as_run[~donor_first])),
            states_identical_before_both=bool(states_same), as_run_sites_differing=differs,
            as_run_excess_by_single_layer=per_layer,
            nominated_positions=committed[f"{arm}/{seed}"]["primary"]["site_set"]["positions"])
        r = rows[f"{arm}/{seed}"]
        print(f"{arm}/{seed} | {layers} | {r['untouched']:.4f} | {r['as_run']:.4f} ({r['as_run']-r['untouched']:+.4f}) | "
              f"{r['as_run_donor_first']:.4f} (no transplant {r['untouched_donor_first']:.4f}) | "
              f"{r['as_run_recipient_first']:.4f} (no transplant {r['untouched_recipient_first']:.4f}; "
              f"bit-identical {r['outputs_bit_identical_as_run_recipient_first']}) | "
              f"{r['before_both']:.4f} | {r['outputs_bit_identical_before_both']} | "
              f"{r['states_identical_before_both']} | {differs:.4f}")

print("\n== C: the control as run (positions before the recipient's first own turn), one layer at a time")
print("excess over no transplant, at running state 0, 1, 2, 3, 4; the nominated site's position set beside it")
for k, r in rows.items():
    print(f"{k} | nominated: layers {tuple(r['layers'])} at {r['nominated_positions']} | "
          + " ".join(f"{x:+.4f}" for x in r["as_run_excess_by_single_layer"]))

with open(os.path.join(HERE, "independent_control4.json"), "w") as f:
    json.dump(dict(pairs=n, donor_first=int((fd < fr).sum()), recipient_first=int((fr < fd).sum()),
                   tokens_identical=tok_same, signal_identical_before_both=sig_same, models=rows),
              f, indent=1, sort_keys=True)
