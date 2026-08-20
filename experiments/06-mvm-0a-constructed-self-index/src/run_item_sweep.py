"""Driver: item_analysis over all five local 30M checkpoints [thread 3]."""
import json
import subprocess
import sys
from pathlib import Path

ART = Path("/Users/john/Documents/Code/minimum-viable-mind/experiments/"
           "06-mvm-0a-constructed-self-index/artifacts")
RUNS = ["pilot_a1_30m_seed0", "pilot_a1_30m_seed1_twin",
        "pilot_a1_30m_seed1", "pilot_a1_30m_seed0_twin",
        "pilot_a1_30m_seed2"]
OUT = Path(__file__).resolve().parents[1] / "lesion-results"

for name in RUNS:
    ckpt = ART / name / f"{name}.pt"
    print(f"=== {name} ===", flush=True)
    r = subprocess.run([sys.executable, "item_analysis.py",
                        "--ckpt", str(ckpt), "--n", "400",
                        "--out", str(OUT / f"items_{name}.jsonl")],
                       capture_output=True, text=True,
                       cwd=Path(__file__).parent)
    if r.returncode != 0:
        print(f"FAILED {name}\n{r.stderr[-2000:]}", flush=True)
        continue
    # keep the printed summary beside the rows
    (OUT / f"items_{name}.summary.json").write_text(
        r.stdout[:r.stdout.rfind("wrote ")])
    print(r.stdout[-400:], flush=True)
print("ALL DONE")
