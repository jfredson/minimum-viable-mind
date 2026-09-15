"""Driver: Gate 0 null calibration over the five local 30M checkpoints
(A3 §4.1). Binders first, since K0 turns on their verdict batteries.
Checkpoints live in the main checkout's gitignored artifacts dir; the
records land in this checkout's null-calibration/ [C6: fresh files]."""
import subprocess
import sys
import time
from pathlib import Path

ART = Path("/Users/john/Code/minimum-viable-mind/experiments/"
           "06-mvm-0a-constructed-self-index/artifacts")
RUNS = ["pilot_a1_30m_seed1_twin", "pilot_a1_30m_seed0",
        "pilot_a1_30m_seed1", "pilot_a1_30m_seed0_twin",
        "pilot_a1_30m_seed2"]
OUT = Path(__file__).resolve().parents[1] / "null-calibration"

for name in RUNS:
    ckpt = ART / name / f"{name}.pt"
    out = OUT / f"null_calibration_{name}.json"
    if out.exists():
        print(f"=== {name}: record exists, skipping [C6] ===", flush=True)
        continue
    print(f"=== {name} === {time.strftime('%H:%M:%S')}", flush=True)
    r = subprocess.run([sys.executable, "null_calibration.py",
                        "--ckpt", str(ckpt), "--out", str(out)],
                       cwd=Path(__file__).parent)
    print(f"=== {name} exit {r.returncode} === {time.strftime('%H:%M:%S')}",
          flush=True)
print("ALL DONE", flush=True)
