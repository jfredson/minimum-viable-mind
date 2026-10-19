"""D1 (H3): is the separable mask the right items, and the route the model answers by?"""
import torch
from common import header, load, gate, chunks, final_parts, G, M

header("D1: bookkeeping of arm M's separable items, on the gate episodes")
b = gate()
m, meta = load("M-10M-rerun")
n = b["tokens"].shape[0]
rows = torch.arange(n)
ap = b["action_pos"][:, G.OWN]
item = b["action_item"][:, G.OWN]
word_before_mask = b["tokens"][rows, ap - 2]
true_agent_any = 0  # the item word of any agent's assignment turn for that item is the same word
assign_item_word = b["tokens"][rows, b["assign_value_pos"][rows, 0, item] - 1]
print(f"(a) own-directed actions: {n}; item word two before the mask differs from the item word "
      f"of the assignment turn for the action's item: {int((word_before_mask != assign_item_word).sum())}")
same_across_agents = all(bool(torch.equal(assign_item_word, b['tokens'][rows, b['assign_value_pos'][rows, a, item] - 1]))
                         for a in range(G.N_AGENTS))
print(f"    the assignment turns of all four agents name the same item word for it: {same_across_agents}")
ent = m.entangled_route(b)[:, G.OWN]
by_word = torch.isin(assign_item_word, torch.tensor(M.ENTANGLED_ITEM_IDS))
print(f"    mask disagreements with 'item word is it1, it2 or it3': {int((ent != by_word).sum())}")
print("    separable actions by item word: " + ", ".join(
    f"{G.IVOCAB[int(t)]} {int(((assign_item_word == t) & ~ent).sum())}" for t in torch.unique(assign_item_word)))
print("    entangled actions by item word: " + ", ".join(
    f"{G.IVOCAB[int(t)]} {int(((assign_item_word == t) & ent).sum())}" for t in torch.unique(assign_item_word)))

bad_sep = bad_ent = 0
for s, sl in chunks(b):
    logits, _, h, slot = final_parts(m, sl)
    a = sl["action_pos"]
    h_act = torch.gather(h, 1, a.unsqueeze(-1).expand(-1, -1, h.shape[-1]))
    l_ent = m.head(h_act)
    l_sep = m._separable_logits(sl, h, slot)
    r = m.entangled_route(sl)
    for c in (G.OWN, G.OTHER):
        bad_sep += int((~torch.isclose(logits[:, c], l_sep[:, c], rtol=0, atol=0).all(-1) & ~r[:, c]).sum())
        bad_ent += int((~torch.isclose(logits[:, c], l_ent[:, c], rtol=0, atol=0).all(-1) & r[:, c]).sum())
print(f"(b) actions (both conditions) where the returned logits are not exactly the separable "
      f"route's on the separable mask: {bad_sep}; not exactly the stirred-in route's on the other: {bad_ent}")
print(f"(c) separable own-directed actions: {int((~ent).sum())} of {n}, share {float((~ent).float().mean()):.4f} "
      f"(expected about 0.4: two of the five items it0 to it4)")
