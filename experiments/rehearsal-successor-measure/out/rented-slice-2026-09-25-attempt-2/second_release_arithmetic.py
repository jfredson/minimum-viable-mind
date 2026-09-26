"""The second release's arithmetic, recomputed from the seconds per step measured
on the rented machine on 2026-09-25 (Pacific). Reads the committed files it
cites; prints every figure the dated note beside the spending proposal uses.

Run from the repository root:
    python3 experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2/second_release_arithmetic.py
"""
import json
import re

HERE = "experiments/rehearsal-successor-measure/out/rented-slice-2026-09-25-attempt-2"
LEDGER = "experiments/06-mvm-0a-constructed-self-index/compute-ledger.md"

bench = json.load(open(f"{HERE}/bench_arms.json"))
assert bench["complete"] is True and bench["device"] == "cuda"
arms = bench["arms"]
ledger = open(LEDGER).read()

# The anchor: the last measured pair of registered-size runs (ledger line 88).
assert "20.28 pod-hours at $0.99 = $20.08" in ledger
per_run_measured = 20.08 / 2  # $10.04, as section 12.3 of the proposal uses it

# The registered A3 run's step size (ledger line 86), for the absolute check.
assert "55,116 steps / 585,552,384 tokens, 9.83h training at 0.645 s/step" in ledger
a3_tokens_per_step = 585_552_384 / 55_116

print("== measured on the rented RTX 5090 (bench_arms.json)")
for a in "TCF":
    r = arms[a]
    print(f"  arm {a}: mean {r['seconds_per_step']*1000:.2f} ms/step, median "
          f"{r['median_seconds_per_step']*1000:.2f}, fastest {r['fastest']*1000:.2f}, "
          f"slowest {r['slowest']*1000:.2f}, {r['steps']} steps, batch {r['batch']}, "
          f"sequence {r['sequence_length']}, {r['parameters']:,} parameters")
ratio = {a: arms[a]["seconds_per_step"] / arms["F"]["seconds_per_step"] for a in "TCF"}
print("  ratio to arm F: " + ", ".join(f"{a} {ratio[a]:.3f}" for a in "TCF"))
print("  the proposal's inferred premium for a constructed arm: 1.55")

print("\n== per-run cost: the measured registered-size run ($10.04) times each arm's measured ratio")
cost = {a: per_run_measured * ratio[a] for a in "TCF"}
for a in "TCF":
    print(f"  arm {a}: ${cost[a]:.2f}")
print(f"  (the same method with the inferred 1.55: ${per_run_measured*1.55:.2f} for each constructed arm)")

print("\n== the second release, section 12.4's table with the run lines repriced")
remaining = {"F": 2, "T": 3, "C": 3}  # nine runs less the one free-arm run in the first release
runs = sum(remaining[a] * cost[a] for a in remaining)
rerun = max(cost.values())  # priced at the worst arm, as section 3.4 of the spending proposal does
transplant, margin = 12.00, 23.00  # unchanged lines of section 12.4
total = runs + rerun + transplant + margin
print(f"  eight remaining runs (2 F, 3 T, 3 C): ${runs:.2f}   (provisional $96)")
print(f"  one permitted re-run, at the dearest arm (C): ${rerun:.2f}   (provisional $12)")
print(f"  transplanting and measurement, unchanged: ${transplant:.2f}")
print(f"  billing-anomaly and idle margin, unchanged: ${margin:.2f}")
print(f"  second release, measured: ${total:.2f}   (provisional $143)")
first = 32.00
print(f"  both releases: ${first + total:.2f}   (provisional $175)")

print("\n== against the programme's money (compute ledger)")
spent_before = 228.1  # the 2026-09-25 first-attempt row's 'after this run' figure
for ceiling in (400, 450):
    print(f"  ceiling ${ceiling}: headroom before this slice about ${ceiling - spent_before:.1f}; "
          f"both releases leave about ${ceiling - spent_before - first - total:.1f}")

print("\n== why the seconds are not turned straight into hours (the absolute check)")
bench_tokens = arms["F"]["batch"] * arms["F"]["sequence_length"]
print(f"  a timed step here: {bench_tokens:,} tokens; a registered A3 step: {a3_tokens_per_step:,.0f} tokens")
steps = 585_552_384 / bench_tokens
hours_F = steps * arms["F"]["seconds_per_step"] / 3600
print(f"  the A3 token budget at this step size: {steps:,.0f} steps; arm F at the timed pace: "
      f"{hours_F:.2f} h, ${hours_F*0.99:.2f}")
real = 0.645 / (a3_tokens_per_step / bench_tokens)
print(f"  the registered A3 run, per {bench_tokens:,} tokens: {real*1000:.1f} ms, "
      f"{real/arms['F']['seconds_per_step']:.1f} times the timed pace")
