"""RT-242: recompute, from the committed label-search fit files, each
candidate's best fit on arm F over the 45 site sets anchored at the action
position (positions 'action', 'action+ans', 'action+3'), per seed. Reads
files only."""
import json, os
B = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                 "../../../rehearsal-successor-measure/out-label-search/")
for n, lab in enumerate(("own-turn-pair", "own-source-turn", "own-value"), 1):
    per = []
    for s in range(3):
        d = json.load(open(f"{B}fit_{lab}_F_seed{s}.json"))
        fx = [x["fit"] for x in d["sites"] if x["positions"] in ("action", "action+ans", "action+3")]
        assert len(fx) == 45
        per.append(round(max(fx), 3))
    print(f"candidate {n} ({lab}), arm F, best over the 45 action-anchored site sets, seeds 0/1/2: {per}; best {max(per)}")
