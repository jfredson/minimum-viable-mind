"""Build the Gate 0 findings tables from the calibration records.

Reads every `null_calibration_*.json` (and `escalation_*.json` when
present) in `../null-calibration/` and prints the markdown tables the
findings note carries, so no number in the note is typed by hand.

    ../../../.venv/bin/python summarize_null.py
"""
from __future__ import annotations

import json
from pathlib import Path

DIR = Path(__file__).resolve().parents[1] / "null-calibration"
ORDER = ["pilot_a1_30m_seed0", "pilot_a1_30m_seed1_twin",
         "pilot_a1_30m_seed1", "pilot_a1_30m_seed0_twin",
         "pilot_a1_30m_seed2"]
LABEL = {"pilot_a1_30m_seed0": "pilot seed-0 full",
         "pilot_a1_30m_seed1_twin": "seed-1 twin",
         "pilot_a1_30m_seed1": "seed-1 full",
         "pilot_a1_30m_seed0_twin": "seed-0 twin",
         "pilot_a1_30m_seed2": "seed-2 full"}
BOUND = {"pilot_a1_30m_seed0": "yes", "pilot_a1_30m_seed1_twin": "yes",
         "pilot_a1_30m_seed1": "no", "pilot_a1_30m_seed0_twin": "no",
         "pilot_a1_30m_seed2": "no"}
BATS = ("T_sr", "T_si", "T_state", "T_syntax", "T_sr_rev")


def load(name: str) -> dict | None:
    p = DIR / f"null_calibration_{name}.json"
    return json.loads(p.read_text()) if p.exists() else None


def cell(th: dict) -> str:
    if th.get("floor"):
        return f"floor (Δacc {th['abs_acc_change_p95']:+.3f})"
    return f"{th['p95_abs_d']:.4f}"


def main() -> None:
    recs = {n: load(n) for n in ORDER}
    have = [n for n in ORDER if recs[n]]

    print("### Baselines reproduced at n=400 (the eval the endpoint rows "
          "report)\n")
    print("| checkpoint | arch | bound? | T_sr | T_si | T_state | T_syntax "
          "| T_sr_rev |")
    print("|---|---|---|---|---|---|---|---|")
    for n in have:
        b = recs[n]["baseline"]
        print(f"| {LABEL[n]} | {recs[n]['arch']} | {BOUND[n]} | "
              + " | ".join(f"{b[x]:.3f}" for x in BATS) + " |")

    print("\n### θ — the null band, 95th percentile of |d| over 120 "
          "content-blind residual ablations\n")
    print("| checkpoint | " + " | ".join(BATS) + " |")
    print("|---|" + "---|" * len(BATS))
    for n in have:
        s = recs[n]["summary"]["theta"]
        print(f"| {LABEL[n]} | " + " | ".join(cell(s[x]) for x in BATS)
              + " |")

    print("\n### δ — the differential band, 95th percentile of "
          "|d(B1) − d(B2)|\n")
    pairs = list(recs[have[0]]["summary"]["delta"].keys())
    print("| checkpoint | " + " | ".join(pairs) + " |")
    print("|---|" + "---|" * len(pairs))
    for n in have:
        s = recs[n]["summary"]["delta"]
        row = []
        for p in pairs:
            v = s[p]
            row.append("floor" if v.get("floor")
                       else f"{v['p95_abs_diff']:.4f}")
        print(f"| {LABEL[n]} | " + " | ".join(row) + " |")

    print("\n### Register-state noise (full checkpoints only, 20 draws; "
          "the original design's own target)\n")
    print("| checkpoint | " + " | ".join(BATS) + " |")
    print("|---|" + "---|" * len(BATS))
    for n in have:
        s = recs[n]["summary"].get("register_theta") or {}
        if not s:
            continue
        row = [f"{s[x]['p95_abs_d']:.4f}" if x in s else "floor"
               for x in BATS]
        print(f"| {LABEL[n]} | " + " | ".join(row) + " |")

    print("\n### K0 — does the band swallow the binder/non-binder split?\n")
    print("| checkpoint | battery | baseline | null band θ | d if the "
          "battery fell to the non-binder level (0.35) | band ≥ 0.25? |")
    print("|---|---|---|---|---|---|")
    for n in have:
        r = recs[n]
        for b in r["pre_commitments"]["verdict_batteries"]:
            th = r["summary"]["theta"][b]
            if th.get("floor"):
                print(f"| {LABEL[n]} | {b} | {r['baseline'][b]:.3f} | "
                      f"at floor, d undefined | — | no |")
                continue
            den = r["baseline"][b] - r["chance"][b]
            d_split = (r["baseline"][b] - 0.35) / den
            print(f"| {LABEL[n]} | {b} | {r['baseline'][b]:.3f} | "
                  f"{th['p95_abs_d']:.4f} | {d_split:.3f} | "
                  f"{'YES — K0 FIRES' if th['p95_abs_d'] >= 0.25 else 'no'} |")

    print("\n### T_si repeated-item rescoring (the A3 decision-14 fix, "
          "$0 side table)\n")
    print("| checkpoint | unique items (n) | acc vs recorded answer | "
          "repeated items (n) | acc vs recorded | acc vs latest value |")
    print("|---|---|---|---|---|---|")
    for n in have:
        t = recs[n]["tsi_rescoring"]
        print(f"| {LABEL[n]} | {t['unique']['n']} | "
              f"{t['unique']['acc_recorded']:.3f} | {t['repeated']['n']} | "
              f"{t['repeated']['acc_recorded']:.3f} | "
              f"{t['repeated']['acc_latest_value']:.3f} |")

    esc = sorted(DIR.glob("escalation_*.json"))
    if esc:
        print("\n### Instrument validity — where the operator does bite "
              "(escalation past the rank cap, not part of the band)\n")
        for p in esc:
            e = json.loads(p.read_text())
            nm = e["checkpoint"].replace(".pt", "")
            L0 = str(min(int(k) for k in e["residual_norms"]))
            print(f"\n**{LABEL.get(nm, nm)}** (d_model {e['d_model']}, "
                  f"registered cap k≤16; residual RMS norm at layer {L0} "
                  f"= {e['residual_norms'][L0]['rms_norm']:.0f}, "
                  f"mean-centred {e['residual_norms'][L0]['rms_centred_norm']:.0f})\n")
            print("| operator | strength | share of residual norm | "
                  + " | ".join(BATS) + " |")
            print("|---|---|---|" + "---|" * len(BATS))
            seen = {}
            for r in e["rows"]:
                key = (r["op"], r["k"], r["mult"])
                seen.setdefault(key, []).append(r)
            for key, rs in seen.items():
                op, k, mult = key
                acc = {b: sum(r["acc"][b] for r in rs) / len(rs)
                       for b in BATS}
                frac = sum(list(r["frac_of_rms_norm"].values())[0]
                           for r in rs) / len(rs)
                fc = sum(list(r["frac_of_centred_norm"].values())[0]
                         for r in rs) / len(rs)
                strength = (f"rank {k}" if mult is None
                            else f"noise ×{mult}")
                print(f"| {op} | {strength} | {frac:.1%} of raw, "
                      f"{fc:.0%} of centred | "
                      + " | ".join(f"{acc[b]:.3f}" for b in BATS) + " |")


if __name__ == "__main__":
    main()
