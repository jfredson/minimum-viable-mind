"""Purpose 1: each checkpoint loads strictly into the frozen model code and
records the full run. Prints step, tokens, the recipe's step count and batch,
stream batches skipped, the log length, and the md5 against the watchdog's.
Read only. $0.

    python checkpoints_end_to_end.py SRC_DIR ARTIFACTS_DIR
"""
import hashlib, os, re, sys
sys.path.insert(0, sys.argv[1])
import torch, models as M
art = sys.argv[2]
for a in "mtcf":
    run = f"succ_{a}_10m_seed0"; p = os.path.join(art, run, run + ".pt")
    ck = torch.load(p, map_location="cpu", weights_only=False)
    m = M.build_from_config(ck["cfg"]); m.load_state_dict(ck["state"], strict=True)
    md5 = hashlib.md5(open(p, "rb").read()).hexdigest()
    wd = re.findall(r"VERIFIED \(md5 (\w+)\)", open(os.path.join(art, run, "watchdog.log")).read())
    r = ck["recipe"]
    print(f"{run}: loads strictly (arm {ck['cfg']['arm']}, {M.n_params(m):,} parameters); step {ck['step']} "
          f"of {r['steps']}; tokens {ck['tokens_seen']:,}; batch {r['batch']}; lr {r['lr']}; "
          f"evaluations logged {len(ck['log'])}; stream skipped {ck['stream_skipped']}; "
          f"md5 {md5[:12]} watchdog {wd} match {wd == [md5[:12]]}")
