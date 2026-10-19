"""D3 (H1): with the row forced onto each agent, does the separable head give that
agent's answer, or the model's own answer whatever the row?"""
import torch
from common import header, load, gate, chunks, final_parts, table_rows, true_agent, separable_mask, agent_answers, G

header("D3: the separable head with its row forced onto each agent (gate, own-directed actions)")
b = gate()
for name in ("M-10M-rerun", "T-10M-rerun", "M-toy-seed0", "T-toy-seed0"):
    m, _ = load(name)
    tot = 0
    own_hits = {"true": 0, "wrong": 0}
    that_hits = {"true": 0, "wrong": 0}
    n_forced = {"true": 0, "wrong": 0}
    norms = {"true": [], "wrong": []}
    for s, sl in chunks(b):
        mask = separable_mask(m, sl)
        ta = true_agent(sl)
        ans = agent_answers(sl)
        own_tgt = sl["targets"][:, G.OWN]
        _, _, h, _ = final_parts(m, sl)
        tr = table_rows(m, sl, h).norm(dim=-1)        # (B, 4)
        tot += int(mask.sum())
        for a in range(G.N_AGENTS):
            f = dict(sl)
            f["action_who"] = sl["action_who"].clone()
            f["action_who"][:, G.OWN] = a
            pred = m(f)[:, G.OWN].argmax(-1)
            is_true = (ta == a)
            for key, sel in (("true", is_true & mask), ("wrong", ~is_true & mask)):
                n_forced[key] += int(sel.sum())
                own_hits[key] += int(((pred == own_tgt) & sel).sum())
                # where that agent's answer differs from the own answer, is the output that agent's?
                that_hits[key] += int(((pred == ans[:, a]) & sel).sum())
            norms["true"].append(tr[:, a][is_true & mask]); norms["wrong"].append(tr[:, a][~is_true & mask])
    # how often a wrong agent's answer equals the own answer (they can coincide)
    coincide = 0
    for s, sl in chunks(b):
        mask = separable_mask(m, sl); ta = true_agent(sl); ans = agent_answers(sl)
        for a in range(G.N_AGENTS):
            coincide += int(((ans[:, a] == sl["targets"][:, G.OWN]) & (ta != a) & mask).sum())
    print(f"\n{name}: {tot} separable own-directed actions")
    print(f"  row forced onto the true agent: {n_forced['true']} cases, own answer {own_hits['true']}")
    print(f"  row forced onto a wrong agent:  {n_forced['wrong']} cases, still the model's own answer "
          f"{own_hits['wrong']}, that agent's answer {that_hits['wrong']} "
          f"(the two coincide in {coincide} of the cases)")
    print(f"  table row size (mean norm): true agent's row {float(torch.cat(norms['true']).mean()):.3f}, "
          f"other agents' rows {float(torch.cat(norms['wrong']).mean()):.3f}")
