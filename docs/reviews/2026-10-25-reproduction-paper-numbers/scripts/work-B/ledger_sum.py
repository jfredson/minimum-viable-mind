"""Sum the '$ actual' cells of compute-ledger.md rows dated 2026-09-14 .. 2026-09-25 that the ledger counts in 'A3 cumulative'.
Values transcribed from the '$ actual' column (ledger lines 93-104 at dacc7b4)."""
rows = [
 ("2026-09-14 Gate 0 null calibration", 0.00),
 ("2026-09-15 Gate 1 curriculum", 0.00),
 ("2026-09-15 Gate 2 A3 pilot seed 0", 13.92),
 ("2026-09-16 ops self-terminate test", 0.29),
 ("2026-09-17 A3 seeds 1+2", 20.1),
 ("2026-09-19 control-learnability pilot (unregistered)", 9.9),
 ("2026-09-20 checkpoint recovery", 0.067),
 ("2026-09-20 follow-up runs 1+2 (refused, combined)", 1.904),
 ("2026-09-21 rented slice (stated ~0.02; vendor later 0.0077)", 0.02),
 ("2026-09-25 rented slice attempt 1", 0.4974),
 ("2026-09-25 rented slice attempt 2", 0.0525),
]
t = 0
for n, v in rows:
    t += v; print(f"{n:60s} {v:8.4f}  cum {t:8.4f}")
print("A3 cumulative =", round(t, 4), "; with the 09-21 slice at its billed $0.0077:", round(t - 0.02 + 0.0077, 4))
print("of which measurement-rehearsal slices (another experiment's work):", round(0.02+0.4974+0.0525, 4))
print("control pilot $9.9 + recovery $0.067 =", 9.9+0.067)
print("pilot $13.92: balance 126.05 -> 112.12 =", round(126.05-112.12, 2))
print("seeds 1+2 pod-hours 10.16+10.12 =", 10.16+10.12, " x $0.99 =", round((10.16+10.12)*0.99, 2))
