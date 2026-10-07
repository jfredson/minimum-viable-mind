"""Checks of the four spending-alarm fixes John ruled on 2026-10-06.

Method, thresholds and every expected outcome were committed first, in
docs/2026-10-06-tripwire-fixes-method.md (section 8); the test numbers below
(T1 to T16, R) are that section's. $0: every vendor call goes to a stand-in,
either a Python function patched into the alarm or a small program put first
on the command path. Nothing is rented and nothing contacts the vendor.

    python tests/check_tripwire_fixes.py          (from experiments/08-successor-degree)
"""
from __future__ import annotations

import importlib.util
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import calendar

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src")
OPS = os.path.join(HERE, "..", "..", "06-mvm-0a-constructed-self-index", "src")
FIX = os.path.join(HERE, "fixtures", "dev-10m-2026-10-04")
sys.path.insert(0, SRC)
import tripwire as T  # noqa: E402

FAILS: list = []
REAL_NOW = T.now


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(name)


class Quiet:
    """Hide the alarm's own printing (its loud halt banner) inside a case."""
    def __enter__(self):
        self._o = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, *a):
        sys.stdout.close()
        sys.stdout = self._o


# ---------------------------------------------------------------- made-up waves

RATE, DRIP, B0, T0 = 0.99, 0.01, 75.0, 1_800_000_000.0


def accrued(x: float, machines: list) -> float:            # minutes -> dollars
    a = DRIP * max(0.0, x) / 60
    for c, g in machines:
        a += RATE * max(0.0, min(x, g) - c) / 60
    return a


def posted(t: float, machines: list, m: float, lag: float, step: float, prepay: float | None) -> float:
    """The stand-in vendor: charges `lag` minutes late, in `step`-minute lumps,
    at `m` times the posted rate; or, with `prepay`, each block charged at its start."""
    if prepay:
        a = DRIP * t / 60
        for c, g in machines:
            if t > c:
                a += RATE * min(math.ceil((t - c) / prepay) * prepay, g - c) / 60
        return m * a
    x = t - lag
    if x <= 0:
        return 0.0
    return m * accrued(math.floor(x / step) * step, machines)


def simulate(machines: list, m: float = 1.0, lag: float = 0, step: float = 1, prepay=None,
             fail_at: float | None = None) -> dict:
    """Run the alarm through one wave on a fake clock. Readings: a check before
    each machine is created, then the watcher at 1, 6, 11, ... minutes.
    Deletions are written by `gone` at their minute, as the deleting step would."""
    d = tempfile.mkdtemp()
    clock = [T0]
    T.now = lambda: clock[0]
    t_min = lambda: (clock[0] - T0) / 60                                        # noqa: E731
    T.read_balance = lambda: (_ for _ in ()).throw(T.CheckFailed("HTTP 503 (stand-in)")) \
        if fail_at is not None and abs(t_min() - fail_at) < 1e-6 else B0 - posted(t_min(), machines, m, lag, step, prepay)
    T.running_pods = lambda: {f"pod{i}" for i, (c, g) in enumerate(machines) if c <= t_min() < g}
    events = [(c, 0, "create", i) for i, (c, g) in enumerate(machines)]
    events += [(g, 1, "gone", i) for i, (c, g) in enumerate(machines)]
    events += [(1 + 5 * k, 2, "watch", None) for k in range(40)]
    out = dict(trip_at=None, done_at=None, log=[], halt=None, rule=None)
    for when, _, kind, i in sorted(events):
        clock[0] = T0 + when * 60
        with Quiet():
            if kind == "create":
                rc = T.cmd_preflight(d)
                if rc:
                    out["trip_at"] = when
                    break
                T.cmd_register(d, f"pod{i}", RATE, 1.0, f"run{i}")
            elif kind == "gone":
                T.cmd_gone(d, f"pod{i}", T0 + when * 60, "the watchdog")
            else:
                r = T.watch_once(d, allow_delete=False)
        if kind != "watch":
            continue
        st = T.load_state(d)
        rb = T.ratio_b(st["readings"], st["machines"], clock[0])
        out["log"].append((when, rb.get("ratio")))
        out["final"] = rb.get("ratio")
        if r == "tripped":
            out["trip_at"] = when
            out["halt"] = T.halted(d)
            break
        if r == "done":
            out["done_at"] = when
            break
    out["dir"] = d
    return out


def made_up_waves() -> None:
    print("T1  honest wave, lagged (8 min) and lumpy (5-min steps), two machines")
    r = simulate([(0, 30), (3, 33)], m=1.0, lag=8, step=5)
    check("no trip at any reading", r["trip_at"] is None)
    check("the watcher ends at minute 66, 30 minutes after the last deletion", r["done_at"] == 66, f"ended {r['done_at']}")
    check("final comparison 0.99 to 1.01", 0.99 <= r["final"] <= 1.01, f"{r['final']:.4f}")

    print("T2  overbilled wave, 3.5 times the rate, same machines")
    r = simulate([(0, 30), (3, 33)], m=3.5, lag=8, step=5)
    check("trips at minute 26, while both machines still run", r["trip_at"] == 26, f"tripped at {r['trip_at']}")
    check("by rule S, two readings in a row", r["halt"] is not None and "rule S" in r["halt"], (r["halt"] or "").splitlines()[0][:90])
    check("ledger figures written with the halt", any(f.startswith("ledger-figures") for f in os.listdir(r["dir"])))
    with Quiet():
        rc = T.cmd_preflight(r["dir"])
    check("the check before a next machine then refuses", rc == 3)

    print("T3  mild overcharge (1.4 times) hidden by an 8-minute lag, one 20-minute machine")
    r = simulate([(0, 20)], m=1.4, lag=8, step=5)
    check("rule S never trips; rule D trips at minute 36, 15 minutes after the deletion",
          r["trip_at"] == 36 and "rule D" in (r["halt"] or ""), f"tripped at {r['trip_at']}: {(r['halt'] or '').splitlines()[0][:80] if r['halt'] else ''}")
    check("ratio about 1.39", 1.35 <= r["final"] <= 1.43, f"{r['final']:.4f}")

    print("T4  honest but lumpy: ten minutes charged in advance at each ten-minute mark")
    r = simulate([(0, 30)], m=1.0, prepay=10)
    over = [w for w, ratio in r["log"] if w < 30 and ratio is not None]
    check("no trip", r["trip_at"] is None, f"ratios in flight: " + ", ".join(f"{w:g}:{x:.2f}" for w, x in r["log"][:7]))
    check("final comparison 1.00", 0.995 <= r["final"] <= 1.005, f"{r['final']:.4f}")

    print("T5  honest, long lag (14 min), one 20-minute machine")
    r = simulate([(0, 20)], m=1.0, lag=14, step=5)
    check("no trip", r["trip_at"] is None)
    check("final comparison 0.98 to 1.00", 0.98 <= r["final"] <= 1.00, f"{r['final']:.4f}")

    print("T6  failed vendor reading in flight (balance read errors at minute 11)")
    r = simulate([(0, 30)], m=1.0, lag=8, step=5, fail_at=11)
    check("trip at minute 11, a check that cannot run", r["trip_at"] == 11 and "cannot run" in (r["halt"] or ""))


# ---------------------------------------------------------------- bills (fix 3)

def empty_bills() -> None:
    print("T7  empty bills at the end of a wave")
    T.now = REAL_NOW
    tmp = tempfile.mkdtemp()
    stub = os.path.join(tmp, "runpodctl")
    ctl = os.path.join(tmp, "bill.json")
    with open(stub, "w") as f:
        f.write(f"#!{sys.executable}\nimport json,sys\nprint(open({ctl!r}).read())\n")
    os.chmod(stub, 0o755)

    def wave(bill, version):
        d = tempfile.mkdtemp()
        json.dump(bill, open(ctl, "w"))
        st = dict(machines={"alpua1c0w6jonx": dict(pod="alpua1c0w6jonx", rate=0.99, estimate_hours=0.1,
                                                    created=1790000000.0, created_iso="2026-09-21T14:13:20Z",
                                                    out="o", gone=1790000000.0 + 191.063)}, readings=[])
        version.save_state(d, st)
        version.RUNPODCTL = stub
        with Quiet():
            rc = version.cmd_reconcile(d)
        return rc, version.halted(d)

    row = lambda pod, ms: [{"amount": 0.05, "podId": pod, "timeBilledMs": ms}]   # noqa: E731
    for name, bill in (("an empty bill ([])", []), ("a bill of zero hours", row("alpua1c0w6jonx", 0)),
                       ("a bill with no row for this machine", row("someotherpod00", 191063))):
        rc, h = wave(bill, T)
        check(f"{name}: a trip, cannot be checked yet", rc == 3 and "cannot be checked yet" in (h or ""))
    rc, h = wave(row("alpua1c0w6jonx", 191063), T)
    rows = None
    check("a real row (191,063 ms against 191.063 s of life) passes at 1.0", rc == 0 and h is None)
    old = old_tripwire()
    rc, h = wave([], old)
    check("the old code passed the empty bill (the fault being fixed)", rc == 0 and h is None, f"old exit {rc}")
    shutil.rmtree(tmp, ignore_errors=True)


def old_tripwire():
    """The alarm as it stands on the main line before these fixes."""
    tmp = tempfile.mkdtemp()
    p = os.path.join(tmp, "tripwire_main.py")
    src = subprocess.run(["git", "-C", HERE, "show", "origin/main:experiments/08-successor-degree/src/tripwire.py"],
                         capture_output=True, text=True, check=True).stdout
    open(p, "w").write(src)
    spec = importlib.util.spec_from_file_location("tripwire_main", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------- deletion records

def deletion_records() -> None:
    print("T8  deletion records in the alarm")
    T.now = REAL_NOW
    d = tempfile.mkdtemp()
    with Quiet():
        T.cmd_register(d, "podA", 0.99, 1.0, "o")
    st = T.load_state(d)
    T.record_gone(st, "podA", 1000.0, "the watcher: not in the machine list", inferred=True)
    T.record_gone(st, "podA", 1200.0, "the watchdog")
    check("a recorded time replaces an inferred one, even a later one",
          st["machines"]["podA"]["gone"] == 1200.0 and not st["machines"]["podA"]["gone_inferred"])
    T.record_gone(st, "podA", 1300.0, "the machine deadline")
    check("between two recorded times the earlier is kept", st["machines"]["podA"]["gone"] == 1200.0)
    T.record_gone(st, "podA", 900.0, "the watcher: not in the machine list", inferred=True)
    check("an inferred time never replaces a recorded one", st["machines"]["podA"]["gone"] == 1200.0)
    T.save_state(d, st)
    with Quiet():
        rc = T.cmd_gone(d, "notours", 1.0, "x")
    check("a machine this wave never registered is reported, not added",
          rc == 1 and "notours" not in T.load_state(d)["machines"])
    out = subprocess.run([sys.executable, os.path.join(SRC, "tripwire.py"), "gone", "--state", d, "--pod", "podA",
                          "--at", "1100", "--by", "the watchdog"], capture_output=True, text=True)
    m = T.load_state(d)["machines"]["podA"]
    # added after the method was written (not pre-stated): a machine the
    # vendor's list misses once, then lists again, must not stay "deleted"
    d2 = tempfile.mkdtemp()
    clock = [T0]
    T.now = lambda: clock[0]
    T.read_balance = lambda: B0
    with Quiet():
        T.cmd_preflight(d2)
        T.cmd_register(d2, "podL", 0.99, 1.0, "o")
        T.running_pods = lambda: set()
        clock[0] += 1
        T.watch_once(d2, False)
        T.running_pods = lambda: {"podL"}
        clock[0] += 300
        T.watch_once(d2, False)
    check("(added) a machine missing from one list and listed again is not left marked deleted",
          T.load_state(d2)["machines"]["podL"]["gone"] is None)
    T.now = REAL_NOW
    check("the command line records the time and who", out.returncode == 0 and m["gone"] == 1100.0
          and m["gone_by"] == "the watchdog", out.stdout.strip()[:90])


# ---------------------------------------------------------------- the shell helpers

def stub_vendor(tmp: str, delete: str, get: str) -> str:
    """A stand-in `runpodctl` whose delete and get answers are given as
    'rc|text'. Every call is logged."""
    b = os.path.join(tmp, "bin")
    os.makedirs(b, exist_ok=True)
    calls = os.path.join(tmp, "calls")
    def part(spec):
        rc, text = spec.split("|", 1)
        return f"printf '%s\\n' '{text}'; exit {rc}"
    with open(os.path.join(b, "runpodctl"), "w") as f:
        f.write(f"""#!/bin/bash
echo "$*" >> "{calls}"
case "$1 $2" in
  "pod delete") {part(delete)} ;;
  "pod get") {part(get)} ;;
  *) exit 2 ;;
esac
""")
    os.chmod(os.path.join(b, "runpodctl"), 0o755)
    return b


def trip_dir_with(pod: str) -> str:
    d = tempfile.mkdtemp()
    T.now = REAL_NOW
    with Quiet():
        T.cmd_register(d, pod, 0.99, 1.0, "o")
    return d


def watchdog_cases() -> None:
    print("T9  the watchdog's delete writes the deletion record")
    NOTFOUND = '{"error":"api error: {\\"error\\":\\"pod not found to terminate\\",\\"status\\":404}"}'
    for name, delete, get, want in (
        ("an accepted delete", "0|pod fakepod0000001 deleted", "1|", True),
        ("a delete answered not found (404)", "1|" + NOTFOUND, "1|", True),
        ("a failed delete, machine still listed", "1|HTTP 503", '0|{"id": "fakepod0000001"}', False),
        ("a failed delete, then a failed reading", "1|HTTP 503", "1|HTTP 503", False),
    ):
        tmp = tempfile.mkdtemp()
        b = stub_vendor(tmp, delete, get)
        dest = os.path.join(tmp, "dest")
        os.makedirs(dest)
        td = trip_dir_with("fakepod0000001")
        envf = os.path.join(tmp, "run.env")
        open(envf, "w").write(f"""POD="fakepod0000001"
SSH="false"
RUN_DIR="/nowhere"
OUT="t9"
DEST="{dest}"
DEADLINE_EPOCH={int(time.time()) - 10}
NETVOL="test"
GRACE_S=1
TRIP_PY="{sys.executable}"
TRIP_SCRIPT="{os.path.join(SRC, 'tripwire.py')}"
TRIP_DIR="{td}"
""")
        t0 = time.time()
        r = subprocess.run(["bash", os.path.join(OPS, "watch_run_a3.sh"), envf], capture_output=True, text=True,
                           env=dict(os.environ, PATH=b + ":" + os.environ["PATH"], KILL_SETTLE_S="0",
                                    FINAL_TRIES="1"), timeout=60)
        rec = os.path.join(dest, "machine_gone_fakepod0000001")
        m = T.load_state(td)["machines"]["fakepod0000001"]
        if want:
            ok = (os.path.exists(rec) and "machine fakepod0000001 " in open(rec).read()
                  and m.get("gone") and t0 - 1 <= m["gone"] <= time.time() + 1 and m.get("gone_by") == "the watchdog")
        else:
            ok = not os.path.exists(rec) and not m.get("gone")
        check(f"{name}: {'record file and alarm time written' if want else 'no record anywhere'}", ok,
              (open(rec).read().strip()[:100] if os.path.exists(rec) else "no record file"))
        shutil.rmtree(tmp, ignore_errors=True)

    # found gone over three silent checks: the record needs one "not found"
    for name, get, want in (("found gone, the vendor says not found", "1|pod not found", True),
                            ("found gone, three failed readings only", "1|HTTP 503", False)):
        tmp = tempfile.mkdtemp()
        b = stub_vendor(tmp, "1|unused", get)
        dest = os.path.join(tmp, "dest")
        os.makedirs(dest)
        envf = os.path.join(tmp, "run.env")
        open(envf, "w").write(f"""POD="fakepod0000001"
SSH="false"
RUN_DIR="/nowhere"
OUT="t9b"
DEST="{dest}"
DEADLINE_EPOCH={int(time.time()) + 3600}
""")
        subprocess.run(["bash", os.path.join(OPS, "watch_run_a3.sh"), envf], capture_output=True, text=True,
                       env=dict(os.environ, PATH=b + ":" + os.environ["PATH"], MISSING_GAP_S="0",
                                PROBE_S="1"), timeout=60)
        rec = os.path.join(dest, "machine_gone_fakepod0000001")
        check(f"{name}: {'record written' if want else 'no record'}", os.path.exists(rec) == want)
        shutil.rmtree(tmp, ignore_errors=True)


def deadline_cases() -> None:
    print("T10-T15  the laptop deadline timer")
    NOTFOUND = '{"error":"pod not found","status":404}'

    def run(name, get, record_for=None, deadline_s=4, want_delete=True, trip=False):
        tmp = tempfile.mkdtemp()
        b = stub_vendor(tmp, "0|pod fakepod0000001 deleted", get)
        if record_for:
            open(os.path.join(tmp, f"machine_gone_fakepod0000001"), "w").write(
                f"machine {record_for} (x) deleted at 2026-10-05T00:38:01Z (1791161881), confirmed by the watchdog: test\n")
        td = trip_dir_with("fakepod0000001") if trip else None
        now = int(time.time())
        envf = os.path.join(tmp, "machine_deadline_fakepod0000001.env")
        open(envf, "w").write(f"""POD="fakepod0000001"
OUT="t10"
CREATED_AT_EPOCH={now}
DELETE_AT_EPOCH={now + deadline_s}
HARD_CAP_USD="0.0011"
RATE_PER_HOUR_USD="0.99"
POSTED_RATE="0.99"
POLL_S=1
VENDOR_CHECK_S=1
""" + (f"""TRIP_PY="{sys.executable}"
TRIP_SCRIPT="{os.path.join(SRC, 'tripwire.py')}"
TRIP_DIR="{td}"
""" if trip else ""))
        t0 = time.time()
        r = subprocess.run(["bash", os.path.join(OPS, "machine_deadline.sh"), envf], capture_output=True, text=True,
                           env=dict(os.environ, PATH=b + ":" + os.environ["PATH"]), timeout=60)
        took = time.time() - t0
        calls = open(os.path.join(tmp, "calls")).read() if os.path.exists(os.path.join(tmp, "calls")) else ""
        deleted = "pod delete" in calls
        line = "DEADLINE REACHED" in r.stdout
        if want_delete:
            ok = deleted and line and took >= deadline_s - 0.5
        else:
            ok = (not deleted) and (not line) and took < deadline_s and r.returncode == 0 and "STANDING DOWN" in r.stdout
        check(name, ok, f"{took:.1f}s, delete called: {deleted}, deadline line: {line}")
        if trip:
            m = T.load_state(td)["machines"]["fakepod0000001"]
            check("T15 the alarm's records show the timer's deletion time, by the machine deadline",
                  m.get("gone") is not None and m.get("gone_by") == "the machine deadline" and t0 <= m["gone"] <= time.time() + 1)
        shutil.rmtree(tmp, ignore_errors=True)

    run("T10 the watchdog's record names this machine: stands down, no delete, no deadline line",
        "1|HTTP 503", record_for="fakepod0000001", deadline_s=6, want_delete=False)
    run("T11 the vendor says pod not found (404): stands down, no delete", "1|" + NOTFOUND, deadline_s=6,
        want_delete=False)
    run("T12 a failed vendor reading (error, no 'not found'): keeps running, deletes at the deadline", "1|HTTP 503")
    run("T13 an empty vendor answer: keeps running, deletes at the deadline", "0|")
    run("T14 a record naming another machine: ignored, deletes at the deadline", "1|HTTP 503",
        record_for="someotherpod00")
    run("T15 deletes at its deadline with the alarm configured", '0|{"id": "fakepod0000001"}', trip=True)


# ---------------------------------------------------------------- the replay

def iso_epoch(s: str) -> float:
    return float(calendar.timegm(time.strptime(s, "%Y-%m-%dT%H:%M:%SZ")))


def replay() -> None:
    print("R   the development run's recorded readings through the new alarm")
    lines = open(os.path.join(FIX, "watchdog-deletion-lines.txt")).read().splitlines()
    snap = json.load(open(os.path.join(FIX, "state-0052Z.json")))
    by_out = {m["out"]: pod for pod, m in snap["machines"].items()}
    times = {}
    for ln in lines:
        mo = re.match(r"(\S+): \[(\S+Z)\] (deleting pod|pod gone; billing stopped)", ln)
        if mo:
            times.setdefault(mo.group(1), {})["delete" if mo.group(3) == "deleting pod" else "gone"] = iso_epoch(mo.group(2))
    t_check = snap["readings"][0]["t"] + 0.753 * 3600          # the check's reading, about 00:56:28
    after = json.load(open(os.path.join(FIX, "state-after-0111Z.json")))
    t_1111, b_1111 = after["readings"][-1]["t"], after["readings"][-1]["balance"]

    def run(which: str) -> list:
        d = tempfile.mkdtemp()
        T.save_state(d, json.loads(json.dumps(snap)))
        clock = [0.0]
        T.now = lambda: clock[0]
        T.running_pods = lambda: set()
        for out, pod in by_out.items():
            with Quiet():
                T.cmd_gone(d, pod, times[out][which], "the watchdog")
        res = []
        for t, bal in ((t_check, 72.3178), (t_1111, b_1111)):
            clock[0] = t
            T.read_balance = lambda bal=bal: bal
            with Quiet():
                r = T.watch_once(d, allow_delete=False)
            st = T.load_state(d)
            rb = T.ratio_b(st["readings"], st["machines"], t)
            dd = T.rule_d(st["readings"], st["machines"])
            res.append((T.iso(t), r, rb["ratio"], rb["drawn"], rb["expected"], dd["applies"], T.halted(d)))
        return res

    for which, label in (("gone", 'deletion times from the "pod gone" lines'),
                         ("delete", 'deletion times from the "deleting pod" lines')):
        res = run(which)
        print(f"      {label}:")
        for t, r, ratio, drawn, exp, applies, h in res:
            print(f"        {t}: ratio B {ratio:.4f} (drawn ${drawn:.4f}, predicted ${exp:.4f}); "
                  f"comparison at deletion applies: {applies}; watcher says {r}; halt: {bool(h)}")
        (t1, r1, x1, *_ , h1), (t2, r2, x2, *__, h2) = res
        if which == "gone":
            check("with the check's 00:56 reading: 0.9899, no trip", abs(x1 - 0.9899) < 0.0005 and not h1, f"{x1:.4f}")
            check("with the 01:11:20 reading: about 0.995, no trip, the watcher finishes",
                  0.99 <= x2 <= 1.00 and not h2 and r2 == "done", f"{x2:.4f}")
        else:
            check("with the earlier edge of each delete: no trip at either reading", not h1 and not h2)
            within = 0.98 <= x1 <= 1.00 and 0.98 <= x2 <= 1.00
            # Pre-stated 0.98 to 1.00 in section 8 of the method; the first run read
            # 0.9988 and 1.0038. Reported as a missed prediction (method, section 10),
            # not counted as a fault in the code, and the range is not widened.
            print(f"  [{'PASS' if within else 'MISS'}] pre-stated range 0.98 to 1.00 for both readings"
                  f"  ({x1:.4f}, {x2:.4f}){'' if within else ': a missed prediction, see the method, section 10'}")
    old = old_tripwire()
    rb = old.ratio_b(after["readings"], after["machines"], t_1111)
    check("the old code's arithmetic, deletions inferred at 01:11: 0.401 (as its watcher logged)",
          abs(rb["ratio"] - 0.401) < 0.0005, f"{rb['ratio']:.4f}")


if __name__ == "__main__":
    print("Checks of the spending-alarm fixes ruled 2026-10-06 (stand-in vendor; $0)")
    made_up_waves()
    empty_bills()
    deletion_records()
    watchdog_cases()
    deadline_cases()
    replay()
    print(f"\n{len(FAILS)} failure(s): {FAILS}" if FAILS else "\nall checks pass. nothing was rented and nothing was spent.")
    sys.exit(1 if FAILS else 0)
