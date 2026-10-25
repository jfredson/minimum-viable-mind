"""Independent cases for measure.outcome, written from version 5 section 3 by the checking session."""
import sys; sys.path.insert(0, sys.argv[1])
import measure as MS
L = "own-directed learning"
def seed(read=None, learn=True, reason="read failed its floor"):
    chk = {L: MS.PASSED if learn else MS.FAILED}
    if read is None:
        return dict(status=MS.NO_VERDICT, degree=None, reasons=[reason], checks=chk, learning_passes=learn)
    return dict(status="reading", degree=read, reasons=[], checks=chk, learning_passes=learn)
def arm(*seeds): return MS.arm_outcome({i: s for i, s in enumerate(seeds)})
def gates(**a): return {k: v["gate_passes"] if v["gate_decidable"] else None for k, v in a.items()}
T = arm(seed(0.0), seed(0.01), seed(0.0)); C = arm(seed(1.0), seed(0.98), seed(1.01))
Cnv = arm(seed(None), seed(None), seed(0.9)); Tnv = arm(seed(None), seed(None), seed(0.0))
Fr = arm(seed(0.4), seed(0.5), seed(None)); Fnv = arm(seed(None), seed(None), seed(0.4))
Ffail = arm(seed(None, False), seed(None, False), seed(0.4))
Cclose = arm(seed(0.5), seed(0.6), seed(0.7)); Tedge = arm(seed(0.5), seed(0.0), seed(0.0)); Cedge = arm(seed(1.0), seed(1.0), seed(1.0))
Tfail = arm(seed(0.0, False), seed(0.0, False), seed(0.0))
M_in = arm(seed(0.5), seed(0.45), seed(0.55)); M_out = arm(seed(0.9), seed(0.5), seed(0.5)); M_fail = arm(seed(None, False), seed(None, False), seed(0.5))
ok5a = dict(seed=0, passed=True); bad5a = dict(seed=1, passed=False, failed_conditions=["named-other condition"])
cases = [
 ("R1 table row 1", dict(T=T, C=C, F=Fr), ok5a, "R1"),
 ("fifth: F no verdict", dict(T=T, C=C, F=Fnv), ok5a, "fifth"),
 ("R2: no separation", dict(T=T, C=Cclose, F=Fr), ok5a, "R2"),
 ("separation exactly 0.5 clears", dict(T=Tedge, C=Cedge, F=Fr), ok5a, "R1"),
 ("sixth: C no verdict, F reads", dict(T=T, C=Cnv, F=Fr), ok5a, "sixth"),
 ("seventh: C and F no verdict", dict(T=T, C=Cnv, F=Fnv), ok5a, "seventh"),
 ("eighth: T no verdict", dict(T=Tnv, C=C, F=Fr), ok5a, "eighth"),
 ("R3: T fails gate", dict(T=Tfail, C=C, F=Fr), ok5a, "R3"),
 ("R3: F fails at step 5a", dict(T=T, C=C, F=Fr), bad5a, "R3"),
 ("fifth: F passed 5a, fails gate at 5b", dict(T=T, C=C, F=Ffail), ok5a, "fifth"),
 ("seventh: F fails 5b and C no verdict", dict(T=T, C=Cnv, F=Ffail), ok5a, "seventh"),
 ("M dropped does not change term", dict(T=T, C=C, F=Fr, M=M_fail), ok5a, "R1"),
 ("M in band: R1", dict(T=T, C=C, F=Fr, M=M_in), ok5a, "R1"),
 ("M misses band: R1 with note", dict(T=T, C=C, F=Fr, M=M_out), ok5a, "R1"),
 ("F reads on one seed only: fifth", dict(T=T, C=C, F=arm(seed(0.4), seed(None), seed(None))), ok5a, "fifth"),
]
bad = 0
for name, arms, s5, want in cases:
    g = gates(**arms)
    o = MS.outcome(g, arms, {0: 0.5, 1: 0.45, 2: 0.55}, s5)
    hit = o["code"] == want
    bad += not hit
    extra = "; M note present" if "M missed" in (o.get("sentence") or "") else ""
    print(f"[{'ok' if hit else 'DIFFERENT'}] {name}: got {o['code']}, want {want}{extra} | {o.get('reason')}")
# channel-removal failure on arm F withholds the seed
row = dict(gate=dict(bar=790, own_correct=2000, other_correct=1000, lesioned_own_correct=1500,
                     lesioned_candidate_own_correct=2000), nomination_status="nominated", described_only=False,
           reading=MS.reading(0.9, 0.5, 0.05, 0.95), dev_floor_clears=True,
           controls={"7": {"holds": True}, "4": {"holds": True}})
w = MS.withhold(row, "F"); print("F seed whose channel removal did not collapse:", w["status"], w["reasons"])
bad += w["status"] != MS.NO_VERDICT
print("ALL AS WRITTEN" if not bad else f"{bad} DIFFERENT")
