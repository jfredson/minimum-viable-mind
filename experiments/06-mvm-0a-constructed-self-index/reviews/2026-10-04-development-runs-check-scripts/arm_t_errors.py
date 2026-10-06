"""Where arm T's own-directed errors come from, on the gate's held-out episodes.

Arm T answers an own-directed action by (a) selecting a row of its table with
the ownership answer (`sel_own`, a softmax over the four agents) and (b)
reading that row for the item and applying the rule. A named-other action
uses a fixed one-hot selection, so it tests (b) alone. This script, on the
3,000 gate episodes (the registered set, `procedure.EvalData`):

- splits own-directed actions by whether the selection's highest weight is on
  the agent the model actually is (`model` in the rendered episode);
- gives accuracy where it is and where it is not;
- recomputes the own-directed action with the selection forced onto the true
  agent (tests the table and rule alone on the own-directed items);
- prints the learned sharpness of the ownership answer, how peaked the
  ownership answer and the selection are, and the read/key weight sizes.

Run on the 10M arm T checkpoint and, for comparison, on the toy arm T seed 0
model the rehearsal committed. Processor only, $0. Reads, never writes, the
checkpoints.

    python arm_t_errors.py SRC_DIR CKPT [CKPT ...]
"""
import sys
sys.path.insert(0, sys.argv[1])
import numpy as np, torch
import grammar as G, models as M, procedure as P

data_pairs = G.make_pairs(*[G.EVAL_SETS["gate"][i] for i in (0,)], seed=G.EVAL_SETS["gate"][1],
                          pool=G.EVAL_SETS["gate"][2], collide=G.EVAL_SETS["gate"][3])
eps = G.episodes_from_pairs(data_pairs)
b = M.to_torch(G.batch(eps), "cpu")
true_agent = torch.as_tensor([e["model"] for e in eps])

def load(path):
    obj = torch.load(path, map_location="cpu", weights_only=True)
    if isinstance(obj, dict) and "state" in obj:
        m = M.build_from_config(obj["cfg"]); m.load_state_dict(obj["state"], strict=True)
    else:
        arm = "M" if "_M_" in path else "T"          # the rehearsal's toy files are bare weights
        m = M.build(arm, "toy"); m.load_state_dict(obj, strict=True)
    return m.eval()

@torch.no_grad()
def analyse(m, bb, ta):
    cap = {}
    orig = m._separable_logits
    def wrapped(b_, h, own_slot):
        cap["h"], cap["own_slot"] = h, own_slot
        return orig(b_, h, own_slot)
    m._separable_logits = wrapped
    logits = m(bb)
    m._separable_logits = orig
    own_vec, p_own = m._own_vec(bb)
    ap = bb["action_pos"][:, G.OWN]
    idx = torch.arange(len(ap))
    p_at = p_own[idx, ap]                                    # ownership answer at the own action
    slot = cap["own_slot"][idx, ap]
    q = m.read_own(slot)
    k = m.own_key(m.own_marker(m.tok(bb["agent_marker_tok"])))
    sel = torch.softmax(torch.einsum("bd,bad->ba", q, k), -1)
    pred = logits[:, G.OWN].argmax(-1)
    hit = (pred == bb["targets"][:, G.OWN])
    oth = (logits[:, G.OTHER].argmax(-1) == bb["targets"][:, G.OTHER])
    sel_right = sel.argmax(-1) == ta
    pown_right = p_at.argmax(-1) == ta
    # forced selection: one-hot on the true agent, same table and rule
    forced = dict(bb); forced["action_who"] = bb["action_who"].clone()
    forced["action_who"][:, G.OWN] = ta                     # named path with the true agent = forced selection
    hit_forced = (m(forced)[:, G.OWN].argmax(-1) == bb["targets"][:, G.OWN])
    if m.cfg.arm == "M":                                      # arm M: split by the route that answers
        route_ent = m.entangled_route(bb)[:, G.OWN]
        sep = ~route_ent
        cap2 = {}
        logits_sep_forced = None
        out_m = dict(
            separable_route_share=float(sep.float().mean()),
            own_acc_separable_route=float(hit[sep].float().mean()),
            own_acc_entangled_route=float(hit[route_ent].float().mean()),
            own_acc_separable_route_selection_forced=float(hit_forced[sep].float().mean()),
            other_acc_separable_route=float(oth[~m.entangled_route(bb)[:, G.OTHER]].float().mean()),
            other_acc_entangled_route=float(oth[m.entangled_route(bb)[:, G.OTHER]].float().mean()))
    n = len(hit)
    out = dict(
        episodes=n, own_correct=int(hit.sum()), other_correct=int(oth.sum()),
        own_sharpness=float(m.own_sharpness),
        ownership_answer_peak_on_true_agent=float(pown_right.float().mean()),
        ownership_answer_mean_top_weight=float(p_at.max(-1).values.mean()),
        selection_top_on_true_agent=int(sel_right.sum()),
        selection_mean_top_weight=float(sel.max(-1).values.mean()),
        selection_mean_weight_on_true_agent=float(sel[idx, ta].mean()),
        own_acc_where_selection_right=float(hit[sel_right].float().mean()) if sel_right.any() else None,
        own_acc_where_selection_wrong=float(hit[~sel_right].float().mean()) if (~sel_right).any() else None,
        own_errors_with_selection_wrong=int((~hit & ~sel_right).sum()),
        own_errors_with_selection_right=int((~hit & sel_right).sum()),
        own_correct_with_selection_forced_to_true_agent=int(hit_forced.sum()),
        read_own_weight_norm=float(m.read_own.weight.norm()),
        own_key_weight_norm=float(m.own_key.weight.norm()),
        own_marker_weight_norm=float(m.own_marker.weight.norm()),
    )
    if m.cfg.arm == "M":
        out.update(out_m)
    # the selection's errors, by how peaked the ownership answer is at the action
    top = p_at.max(-1).values
    for lo, hi in ((0, 0.9), (0.9, 0.99), (0.99, 1.01)):
        sl = (top >= lo) & (top < hi)
        out[f"ownership_answer_top_weight_{lo}_to_{min(hi,1.0)}"] = dict(
            episodes=int(sl.sum()),
            selection_right=float(sel_right[sl].float().mean()) if sl.any() else None)
    # by the marker word of the agent the model is, and of the agent wrongly chosen
    mk = bb["agent_marker_tok"]
    true_tok = mk[idx, ta]; chosen_tok = mk[idx, sel.argmax(-1)]
    inv = {v: k for k, v in G.VOCAB.items()}
    by = {}
    for t in sorted(set(true_tok.tolist())):
        sl = true_tok == t
        wrong = chosen_tok[sl & ~sel_right]
        by[inv[t]] = dict(episodes=int(sl.sum()), selection_right=round(float(sel_right[sl].float().mean()), 3),
                          wrongly_chosen=dict((inv[w], int((wrong == w).sum())) for w in sorted(set(wrong.tolist()))))
    out["selection_by_marker_word_of_true_agent"] = by
    # for each (true word, wrongly chosen word) seen: is the selection wrong
    # every time the wrongly chosen word is also in the episode?
    pairs = {}
    for t, w in sorted(set(zip(true_tok[~sel_right].tolist(), chosen_tok[~sel_right].tolist()))):
        present = (true_tok == t) & (mk == w).any(-1)
        pairs[f"{inv[t]} chosen as {inv[w]}"] = dict(
            episodes_with_both_words=int(present.sum()),
            selection_wrong_in_those=int((present & ~sel_right).sum()),
            chose_that_word=int((present & (chosen_tok == w)).sum()))
    out["collisions"] = pairs
    # and by which agent the model is
    for a in range(G.N_AGENTS):
        sl = ta == a
        out[f"selection_right_when_model_is_agent_{a}"] = float(sel_right[sl].float().mean())
    return out

for path in sys.argv[2:]:
    m = load(path)
    print(f"== {path}  (arm {m.cfg.arm}, d_model {m.cfg.d_model}, {m.cfg.n_layers} blocks)")
    for k, v in analyse(m, b, true_agent).items():
        print(f"  {k}: {v}")
