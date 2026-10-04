"""The spending tripwire: 1.25, halt not trim, with the in-flight clause.

FROZEN CODE, NOT YET REGISTERED. Frozen 2026-10-04 under
`docs/successor-code-freeze-method-2026-10-04.md`. It implements section 12.5
of `docs/successor-experiment-proposal-2026-10-03-v4.md`, adopted by John on
2026-09-25 (the queue ruling, page 6, part 3), which says the tripwire is
written into the launch preconditions beside the sleep guard and the argument
guard. It did not exist as code before this.

Two ratios
----------
- **Ratio B, fast:** account-balance drawdown per elapsed hour, divided by
  the posted hourly rate times the machines running (plus the network
  volume's storage drip). Read from `runpodctl user` (`clientBalance`), taken
  cumulatively from the wave's first reading so a charge that lands late is
  not read as a spike.
- **Ratio A, authoritative:** billed hours divided by machine-existence
  hours, per machine, from `runpodctl billing pods` (`timeBilledMs`), at a
  wave boundary.

Either at or above 1.25 is a trip. **A check that cannot run is a trip**
(item 15 of the 2026-09-21 ruling). On a trip:

1. a halt file is written; `preflight`, which the launcher runs before it
   creates any machine, refuses while it exists, so nothing else launches;
2. a machine already running is left to finish only if the funded balance
   covers its projected remaining cost at the measured ratio; otherwise it is
   deleted and the run written off (`in_flight_decision`, arithmetic, not
   taste);
3. the figures for the ledger row (both hours, the ratio, the balance
   reading) are written to a file before anything else;
4. it prints, loudly, that John is to be told the number; every later launch
   needs his own words. Removing the halt file is his decision, not this
   program's.

How the launcher uses it
------------------------
    python tripwire.py preflight --state DIR             # before creating a machine
    python tripwire.py register  --state DIR --pod ID --rate 0.99 --estimate-hours 1.5
    python tripwire.py watch     --state DIR             # spawned once per wave, hourly
    python tripwire.py reconcile --state DIR             # ratio A at the wave boundary

Contacts the vendor only to read the balance, the machine list and billing,
and to delete a machine when the in-flight clause says it must. Creates
nothing [C1/C2].

    python tripwire.py --self-test
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

TRIP_RATIO = 1.25
VOLUME_DRIP_PER_HOUR = 0.01        # the network volume's storage, read as currentSpendPerHr when idle
WATCH_EVERY_S = 3600
HALT = "HALT"
RUNPODCTL = os.environ.get("RUNPODCTL", "runpodctl")


class CheckFailed(Exception):
    """A check that cannot run. It counts as a trip."""


def now() -> float:
    return time.time()


def iso(t: float) -> str:
    return datetime.fromtimestamp(t, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ------------------------------------------------------------ the vendor

def _vendor(args: list) -> object:
    try:
        r = subprocess.run([RUNPODCTL] + args, capture_output=True, text=True, timeout=60)
    except Exception as e:                                   # noqa: BLE001
        raise CheckFailed(f"{RUNPODCTL} {' '.join(args)} could not run: {e}")
    if r.returncode != 0:
        raise CheckFailed(f"{RUNPODCTL} {' '.join(args)} returned {r.returncode}: "
                          f"{(r.stdout + r.stderr).strip()[:200]}")
    try:
        return json.JSONDecoder(strict=False).decode(r.stdout)
    except Exception as e:                                   # noqa: BLE001
        raise CheckFailed(f"{RUNPODCTL} {' '.join(args)} did not return JSON: {e}")


def read_balance() -> float:
    d = _vendor(["user"])
    try:
        return float(d["clientBalance"])
    except Exception as e:                                   # noqa: BLE001
        raise CheckFailed(f"no clientBalance in the account reading: {e}")


def running_pods() -> set:
    d = _vendor(["pod", "list"])
    if not isinstance(d, list):
        raise CheckFailed("the machine list is not a list")
    return {p.get("id") for p in d if isinstance(p, dict) and p.get("id")}


def billed_hours(pod: str, since: str) -> float:
    d = _vendor(["billing", "pods", "--pod-id", pod, "--bucket-size", "hour",
                 "--grouping", "podId", "--start-time", since])
    if not isinstance(d, list):
        raise CheckFailed("the billing reading is not a list")
    return sum(float(x.get("timeBilledMs", 0)) for x in d if x.get("podId") == pod) / 3.6e6


def delete_pod(pod: str) -> str:
    try:
        r = subprocess.run([RUNPODCTL, "pod", "delete", pod], capture_output=True, text=True, timeout=120)
        return f"rc={r.returncode} {(r.stdout + r.stderr).strip()[:200]}"
    except Exception as e:                                   # noqa: BLE001
        return f"could not run: {e}"


# ------------------------------------------------------------ the state

def load_state(d: str) -> dict:
    p = os.path.join(d, "state.json")
    if not os.path.exists(p):
        return dict(machines={}, readings=[])
    with open(p) as f:
        return json.load(f)


def save_state(d: str, st: dict) -> None:
    os.makedirs(d, exist_ok=True)
    tmp = os.path.join(d, "state.json.tmp")
    with open(tmp, "w") as f:
        json.dump(st, f, indent=1, sort_keys=True)
    os.replace(tmp, os.path.join(d, "state.json"))


def halted(d: str) -> str | None:
    p = os.path.join(d, HALT)
    return open(p).read() if os.path.exists(p) else None


def write_halt(d: str, why: str, figures: dict) -> None:
    """Ledger figures first, then the halt file (section 12.5, items 3 and 1)."""
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"ledger-figures-{iso(now()).replace(':', '')}.json"), "w") as f:
        json.dump(dict(figures, reason=why, written=iso(now())), f, indent=1, sort_keys=True)
    with open(os.path.join(d, HALT), "w") as f:
        f.write(f"TRIPPED {iso(now())}: {why}\nNothing launches until John rules. Removing this "
                f"file is his decision.\n")
    print("=" * 70)
    print(f"TRIPWIRE: {why}")
    print("HALT, NOT TRIM. Nothing else launches. Write the ledger row from the figures file,")
    print("then tell John the number; every later launch needs his own words.")
    print("=" * 70, flush=True)


# ------------------------------------------------------------ the arithmetic

def ratio_b(readings: list, machines: dict, t_now: float) -> dict:
    """Cumulative drawdown since the first reading, per hour, against what the
    machines that were running should have cost over the same time."""
    if len(readings) < 2:
        return dict(ratio=None, reason="fewer than two balance readings")
    t0, b0 = readings[0]["t"], readings[0]["balance"]
    t1, b1 = readings[-1]["t"], readings[-1]["balance"]
    hours = (t1 - t0) / 3600
    if hours <= 0:
        return dict(ratio=None, reason="no time between readings")
    expected = VOLUME_DRIP_PER_HOUR * hours
    for m in machines.values():
        start = max(t0, m["created"])
        end = min(t1, m.get("gone") or t1)
        if end > start:
            expected += m["rate"] * (end - start) / 3600
    drawn = b0 - b1
    return dict(ratio=drawn / expected if expected > 0 else None, drawn=drawn, expected=expected,
                hours=hours, first=readings[0], last=readings[-1])


def trips(ratio: float | None) -> bool:
    """Either ratio at or above 1.25 is a trip."""
    return ratio is not None and ratio >= TRIP_RATIO


def ratio_a(billed: float, existed: float) -> float | None:
    return billed / existed if existed > 0 else None


def in_flight_decision(machine: dict, ratio: float, balance: float, t_now: float) -> dict:
    """Section 12.5, item 2: left to finish only if the funded balance covers
    its projected remaining cost at the measured ratio."""
    elapsed = (t_now - machine["created"]) / 3600
    remaining_h = max(0.0, machine["estimate_hours"] - elapsed)
    projected = remaining_h * machine["rate"] * ratio
    keep = balance >= projected
    return dict(pod=machine["pod"], elapsed_hours=elapsed, remaining_hours=remaining_h,
                projected_remaining_cost=projected, balance=balance,
                decision="leave to finish" if keep else "delete and write the run off")


# ------------------------------------------------------------ the commands

def cmd_preflight(d: str) -> int:
    h = halted(d)
    if h:
        print(f"tripwire: REFUSING to launch: the tripwire has tripped and not been cleared.\n{h}")
        return 3
    st = load_state(d)
    try:
        bal = read_balance()
        live = running_pods()
    except CheckFailed as e:
        write_halt(d, f"a check that cannot run is a trip: {e}", dict(state=st))
        return 3
    st["readings"].append(dict(t=now(), balance=bal, source="preflight"))
    save_state(d, st)
    ours = [m for m in st["machines"].values() if m["pod"] in live]
    print(f"tripwire: balance ${bal:.4f}; {len(live)} machine(s) on the account, {len(ours)} of this wave")
    rb = ratio_b(st["readings"], st["machines"], now())
    if ours and rb["ratio"] is not None and rb["hours"] >= 0.5:
        print(f"tripwire: ratio B so far {rb['ratio']:.3f} over {rb['hours']:.2f} hours")
        if trips(rb["ratio"]):
            write_halt(d, f"ratio B {rb['ratio']:.3f} at or above {TRIP_RATIO} before the next machine",
                       dict(ratio_b=rb))
            return 3
    elif ours:
        # before the second machine of a wave: ratio B needs some time to mean anything
        print("tripwire: a machine of this wave is running but ratio B has under half an hour "
              "of readings; launching another now is allowed by the rule, and the watcher keeps reading")
    print("tripwire: ok to launch")
    return 0


def cmd_register(d: str, pod: str, rate: float, estimate_hours: float, out: str) -> int:
    st = load_state(d)
    st["machines"][pod] = dict(pod=pod, rate=rate, estimate_hours=estimate_hours, created=now(),
                               created_iso=iso(now()), out=out, gone=None)
    save_state(d, st)
    print(f"tripwire: registered {pod} at ${rate}/h, estimate {estimate_hours} h")
    return 0


def watch_once(d: str, allow_delete: bool) -> str:
    """One hourly check. Returns "continue", "done" or "tripped"."""
    st = load_state(d)
    try:
        bal = read_balance()
        live = running_pods()
    except CheckFailed as e:
        write_halt(d, f"a check that cannot run is a trip: {e}", dict(state=st))
        return "tripped"
    t = now()
    st["readings"].append(dict(t=t, balance=bal, source="watch"))
    for m in st["machines"].values():
        if m["pod"] in live:
            m["last_seen"] = t
        elif not m.get("gone"):
            m["gone"] = t
    save_state(d, st)
    rb = ratio_b(st["readings"], st["machines"], t)
    shown = "unread" if rb["ratio"] is None else f"{rb['ratio']:.3f}"
    print(f"[{iso(t)}] tripwire: balance ${bal:.4f}; ratio B {shown}", flush=True)
    if rb["ratio"] is not None and rb["hours"] >= 0.9 and trips(rb["ratio"]):
        decisions = [in_flight_decision(m, rb["ratio"], bal, t)
                     for m in st["machines"].values() if m["pod"] in live]
        write_halt(d, f"ratio B {rb['ratio']:.3f} at or above {TRIP_RATIO}",
                   dict(ratio_b=rb, in_flight=decisions))
        for dec in decisions:
            if dec["decision"].startswith("delete"):
                res = delete_pod(dec["pod"]) if allow_delete else "not deleted: --allow-delete not given"
                print(f"tripwire: {dec['pod']}: {dec['decision']} -> {res}", flush=True)
            else:
                print(f"tripwire: {dec['pod']}: left to finish; the funded balance covers its "
                      f"projected remaining ${dec['projected_remaining_cost']:.2f}", flush=True)
        return "tripped"
    if not any(m["pod"] in live for m in st["machines"].values()):
        return "done"
    return "continue"


def cmd_watch(d: str, every: int, allow_delete: bool) -> int:
    while True:
        r = watch_once(d, allow_delete)
        if r != "continue":
            print(f"tripwire watch: {r}", flush=True)
            return 0 if r == "done" else 3
        time.sleep(every)


def cmd_reconcile(d: str) -> int:
    st = load_state(d)
    rows, worst = [], 0.0
    for m in st["machines"].values():
        try:
            b = billed_hours(m["pod"], m["created_iso"][:13] + ":00:00Z")
        except CheckFailed as e:
            write_halt(d, f"a check that cannot run is a trip: ratio A for {m['pod']}: {e}", dict(state=st))
            return 3
        existed = ((m.get("gone") or m.get("last_seen") or now()) - m["created"]) / 3600
        ra = ratio_a(b, existed)
        rows.append(dict(pod=m["pod"], billed_hours=b, existence_hours=existed, ratio_a=ra))
        worst = max(worst, ra or 0)
        print(f"tripwire reconcile: {m['pod']}: billed {b:.3f} h, existed about {existed:.3f} h, "
              f"ratio A {ra if ra is None else round(ra, 3)}")
    with open(os.path.join(d, "reconcile.json"), "w") as f:
        json.dump(rows, f, indent=1)
    if trips(worst):
        write_halt(d, f"ratio A {worst:.3f} at or above {TRIP_RATIO} at the wave boundary", dict(rows=rows))
        return 3
    return 0


# ------------------------------------------------------------ self-test

def self_test() -> None:
    """Every vendor call goes to a stand-in program that prints the committed
    readings of 2026-09-26 (`experiments/rehearsal-successor-measure/out/
    rented-slice-attempt-2-check-2026-09-25/vendor-reading-3.txt`) or fails
    on purpose. Nothing contacts the vendor."""
    import shutil
    import tempfile
    global RUNPODCTL, now
    fails = []

    def check(name, ok, detail=""):
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))
        if not ok:
            fails.append(name)

    print("tripwire.py self-test (stand-in vendor; nothing is contacted)")
    tmp = tempfile.mkdtemp()
    stub = os.path.join(tmp, "runpodctl")
    ctl = os.path.join(tmp, "ctl.json")

    def vendor(balance=75.8450678416, pods=(), fail=None, billed_ms=191063):
        json.dump(dict(balance=balance, pods=list(pods), fail=fail, billed_ms=billed_ms), open(ctl, "w"))

    with open(stub, "w") as f:
        f.write(f"""#!{sys.executable}
import json, sys
c = json.load(open({ctl!r}))
a = sys.argv[1:]
if c["fail"] and c["fail"] in " ".join(a): sys.stderr.write("HTTP 403"); sys.exit(1)
if a[:1] == ["user"]: print(json.dumps({{"clientBalance": c["balance"], "currentSpendPerHr": 0.01}}))
elif a[:2] == ["pod", "list"]: print(json.dumps([{{"id": p}} for p in c["pods"]]))
elif a[:2] == ["pod", "delete"]: open({ctl!r} + ".deleted", "a").write(a[2] + "\\n"); print("deleted")
elif a[:2] == ["billing", "pods"]:
    pid = a[a.index("--pod-id") + 1]
    print(json.dumps([{{"amount": 0.05, "podId": pid, "timeBilledMs": c["billed_ms"]}}]))
else: sys.exit(2)
""")
    os.chmod(stub, 0o755)
    RUNPODCTL = stub
    clock = [1_790_000_000.0]
    now = lambda: clock[0]                                  # noqa: E731
    try:
        d = os.path.join(tmp, "wave")
        vendor()
        check("preflight with nothing running: ok to launch", cmd_preflight(d) == 0)
        check("the committed reading parses: balance 75.8451",
              abs(load_state(d)["readings"][-1]["balance"] - 75.8450678416) < 1e-9)
        cmd_register(d, "podA", 0.99, 1.5, "succ_c_10m_seed0")
        vendor(pods=["podA"])
        # one hour at the posted rate: 0.99 + 0.01 drawn -> ratio 1.0
        clock[0] += 3600
        vendor(balance=75.8450678416 - 1.00, pods=["podA"])
        check("an hour billed at the posted rate is not a trip", watch_once(d, True) == "continue")
        rb = ratio_b(load_state(d)["readings"], load_state(d)["machines"], clock[0])
        check("ratio B reads 1.0 at the posted rate", abs(rb["ratio"] - 1.0) < 1e-6, f"{rb['ratio']:.4f}")
        # the 2026-08-08 anomaly: 3.5 times the rate
        clock[0] += 3600
        vendor(balance=75.8450678416 - 1.00 - 3.5, pods=["podA"])
        r = watch_once(d, True)
        check("billing at 2.25 times the rate over two hours trips", r == "tripped" and halted(d))
        figs = [f for f in os.listdir(d) if f.startswith("ledger-figures")]
        check("the ledger figures are written with the halt", len(figs) == 1)
        check("after a trip, preflight refuses every launch", cmd_preflight(d) == 3)
        dec = in_flight_decision(dict(pod="x", created=0, estimate_hours=10, rate=0.99), 3.5, 5.0, 3600 * 2)
        check("in flight: a machine whose remaining cost at the ratio exceeds the balance is deleted",
              dec["decision"].startswith("delete"), f"projected ${dec['projected_remaining_cost']:.2f} against $5")
        dec2 = in_flight_decision(dict(pod="x", created=0, estimate_hours=2.5, rate=0.99), 1.3, 60.0, 3600 * 2)
        check("in flight: a machine the balance covers is left to finish", dec2["decision"] == "leave to finish")
        check("1.25 exactly trips; 1.2499 does not; an unread ratio does not by itself",
              trips(1.25) and not trips(1.2499) and not trips(None))
        # a check that cannot run is a trip
        d2 = os.path.join(tmp, "wave2")
        vendor(fail="user")
        check("an unreadable balance at preflight is a trip, not a skip", cmd_preflight(d2) == 3 and halted(d2))
        d3 = os.path.join(tmp, "wave3")
        vendor()
        cmd_preflight(d3)
        cmd_register(d3, "podB", 0.99, 1.5, "o")
        vendor(pods=["podB"], fail="pod list")
        clock[0] += 3600
        check("an unreadable machine list in flight is a trip", watch_once(d3, True) == "tripped")
        # ratio A, from the committed billing row: 191,063 ms billed
        d4 = os.path.join(tmp, "wave4")
        vendor()
        cmd_preflight(d4)
        cmd_register(d4, "alpua1c0w6jonx", 0.99, 0.1, "o")
        st = load_state(d4)
        st["machines"]["alpua1c0w6jonx"]["gone"] = st["machines"]["alpua1c0w6jonx"]["created"] + 191.063
        save_state(d4, st)
        check("ratio A from the committed billing row of the second slice reads 1.0",
              cmd_reconcile(d4) == 0 and abs(json.load(open(os.path.join(d4, "reconcile.json")))[0]["ratio_a"] - 1.0) < 1e-6)
        st["machines"]["alpua1c0w6jonx"]["gone"] = st["machines"]["alpua1c0w6jonx"]["created"] + 191.063 / 3.5
        save_state(d4, st)
        check("the 2026-08-08 shape (billed 3.5 times existence) trips at reconcile", cmd_reconcile(d4) == 3)
        # the watcher ends when no machine of the wave is left
        d5 = os.path.join(tmp, "wave5")
        vendor()
        cmd_preflight(d5)
        cmd_register(d5, "podC", 0.99, 1.0, "o")
        clock[0] += 3600
        vendor(balance=75.8450678416 - 0.5, pods=[])
        check("the watcher stops when the wave's machines are gone", watch_once(d5, True) == "done")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print(f"\n{len(fails)} failure(s)" if fails else "\nall checks passed")
    if fails:
        raise SystemExit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    for name in ("preflight", "register", "watch", "reconcile"):
        s = sub.add_parser(name)
        s.add_argument("--state", required=True)
        if name == "register":
            s.add_argument("--pod", required=True)
            s.add_argument("--rate", type=float, required=True)
            s.add_argument("--estimate-hours", type=float, required=True)
            s.add_argument("--out", default="")
        if name == "watch":
            s.add_argument("--every", type=int, default=WATCH_EVERY_S)
            s.add_argument("--allow-delete", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        self_test()
        return
    if a.cmd == "preflight":
        sys.exit(cmd_preflight(a.state))
    if a.cmd == "register":
        sys.exit(cmd_register(a.state, a.pod, a.rate, a.estimate_hours, a.out))
    if a.cmd == "watch":
        sys.exit(cmd_watch(a.state, a.every, a.allow_delete))
    if a.cmd == "reconcile":
        sys.exit(cmd_reconcile(a.state))
    ap.print_help()


if __name__ == "__main__":
    main()
