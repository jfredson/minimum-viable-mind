"""D0: reproduce the in-use check's route-use figures with the frozen code."""
import json
import time
from common import header, load, gate, P, CKPTS

header("D0: the frozen procedure.route_in_use on EvalData().gate")
b = gate()
print(f"gate episodes: {b['tokens'].shape[0]}")
for name in CKPTS:
    t = time.time()
    m, meta = load(name)
    rec = P.route_in_use(m, m.cfg.arm, b)
    routes = {k: dict(actions=v["actions"], right=v["right_with_true_answer"],
                      still_right_after_swap=v["still_right_with_swapped_answer"],
                      route_use=None if v["route_use"] is None else round(v["route_use"], 4))
              for k, v in rec["routes"].items()}
    print(f"\n{name}  (md5 {meta['md5']}, step {meta.get('step')}, arm {m.cfg.arm}, "
          f"width {m.cfg.d_model}, {m.cfg.n_layers} blocks)")
    print(f"  sharpness {rec['sharpness']}, learned {rec['sharpness_learned']}, "
          f"weight on true agent {rec['weight_on_true_agent']:.4f}, state {rec['state']}")
    print("  routes " + json.dumps(routes))
    print(f"  ({time.time() - t:.1f} s)")
