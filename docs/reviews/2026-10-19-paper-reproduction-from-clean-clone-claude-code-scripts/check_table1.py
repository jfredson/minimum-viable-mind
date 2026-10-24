"""Compare the paper's Table 1 (hand-copied below from the draft) with removal_ci.json."""
import json, sys
from pathlib import Path
repo = Path(sys.argv[1])
ci = json.loads((repo/"experiments/01-self-indexing-removal-test/removal_ci.json").read_text())
paper = {  # condition: [(battery, point, lo, hi)]
 "idxres_mean_k16": [("T_self_irrelevant",.219,.094,.375),("T_self_relevant",.100,.000,.200),("T_syntax",.133,.033,.267),("d_self",.059,-.062,.185)],
 "idxres_directional_k16": [("T_self_irrelevant",.125,.031,.250),("T_self_relevant",.067,.000,.167),("T_syntax",.133,.033,.267),("d_self",-.039,-.136,.051)],
 "narrative_mean_k16": [("T_self_irrelevant",.063,.000,.156),("T_self_relevant",.033,.000,.100),("T_syntax",.067,.000,.167),("d_self",.039,-.060,.146)],
 "expert_mean_k16": [("T_self_irrelevant",.063,.000,.156),("T_self_relevant",.000,.000,.000),("T_syntax",.100,.000,.233),("d_self",.020,-.079,.112)],
}
bad = 0
for c, cells in paper.items():
    for b, p, lo, hi in cells:
        j = ci["cells"][c][b]
        ok = all(abs(round(j[k],3) - v) < 0.0011 for k, v in (("point",p),("lo",lo),("hi",hi)))
        bad += (not ok)
        print("OK    " if ok else "DIFFER", c, b, "paper", (p,lo,hi), "json", (j["point"], j["lo"], j["hi"]))
print("differences:", bad)
d = ci["derived"]
print("differential", d["differential_Tsi_primary_minus_control"], "paper +0.156 [0.000, 0.312]")
print("router gap primary", d["router_gap_idxres_mean_k16"], "paper +0.033 [-0.133,+0.200]")
print("router gap directional", d["router_gap_idxres_directional_k16"], "paper +0.067 [-0.067,+0.233]")
