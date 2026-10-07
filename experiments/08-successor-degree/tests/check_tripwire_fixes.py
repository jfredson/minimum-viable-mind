"""Checks of the four spending-alarm fixes John ruled on 2026-10-06.

Method, thresholds and every expected outcome were committed first, in
docs/2026-10-06-tripwire-fixes-method.md: section 8 (T1 to T16, R) before the
first code, section 11.5 (N, W, L, F) before the corrections that followed
the independent check (pull request 117). $0: every vendor call goes to a stand-in,
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
             fail_at: float | None = None, topup: tuple | None = None) -> dict:
    """Run the alarm through one wave on a fake clock. Readings: a check before
    each machine is created, then the watcher at 1, 6, 11, ... minutes.
    Deletions are written by `gone` at their minute, as the deleting step would."""
    d = tempfile.mkdtemp()
    clock = [T0]
    T.now = lambda: clock[0]
    t_min = lambda: (clock[0] - T0) / 60                                        # noqa: E731
    T.read_balance = lambda: (_ for _ in ()).throw(T.CheckFailed("HTTP 503 (stand-in)")) \
        if fail_at is not None and abs(t_min() - fail_at) < 1e-6 else (B0 - posted(t_min(), machines, m, lag, step, prepay)
                                                                    + (topup[1] if topup and t_min() >= topup[0] else 0))
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
                if T.load_state(d).get("restarts") and "restart_at" not in out:
                    out["restart_at"] = when
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

    def wave(bill, version, life=191.063):
        d = tempfile.mkdtemp()
        json.dump(bill, open(ctl, "w"))
        st = dict(machines={"alpua1c0w6jonx": dict(pod="alpua1c0w6jonx", rate=0.99, estimate_hours=0.1,
                                                    created=1790000000.0, created_iso="2026-09-21T14:13:20Z",
                                                    out="o", gone=1790000000.0 + life)}, readings=[])
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
    print("B1-B4  a bill posted only in part (ruled 2026-10-06: below 0.90 of life is 'cannot be checked yet')")
    p = "alpua1c0w6jonx"
    rc, h = wave(row(p, 566260), T, life=1873)
    check("B1 the recorded partial bill (566,260 ms against 1,873 s, 0.30): a trip, cannot be checked yet",
          rc == 3 and "cannot be checked yet" in (h or ""))
    rc, h = wave(row(p, 566260) + row(p, 1305615), T, life=1873)
    check("B2 the recorded complete bill (1,871,875 ms against 1,873 s, 0.9994): passes", rc == 0 and h is None)
    rc, h = wave(row(p, 900000), T, life=1000)
    rc2, h2 = wave(row(p, 899000), T, life=1000)
    check("B3 billed 0.90 of life passes; 0.899 is a trip, cannot be checked yet",
          rc == 0 and h is None and rc2 == 3 and "cannot be checked yet" in (h2 or ""))
    rc, h = wave(row(p, 3500000), T, life=1000)
    check("B4 billed 3.5 times life: still a trip, over the line", rc == 3 and "at or above 1.25" in (h or ""))
    shutil.rmtree(tmp, ignore_errors=True)


def top_ups() -> None:
    print("U1-U5  a top-up during a wave (ruled 2026-10-06: restart the comparison, record it, do not trip)")
    r = simulate([(0, 40)], m=1.0, lag=8, step=5, topup=(13, 75.0))
    st = T.load_state(r["dir"])
    check("U1 honest wave, lagged, $75 top-up at minute 13: no trip", r["trip_at"] is None)
    check("U1 the restart is recorded at minute 16, with the rise", r.get("restart_at") == 16
          and len(st.get("restarts", [])) == 1 and abs(st["restarts"][0]["rise"] - 75.0) < 0.5,
          f"restart at {r.get('restart_at')}, rise {st.get('restarts', [{}])[0].get('rise', 0):.4f}")
    check("U1 final comparison about 0.895 (0.85 to 0.95)", 0.85 <= (T.rule_d(st["readings"], st["machines"])["rb"]["ratio"]) <= 0.95,
          f"{T.rule_d(st['readings'], st['machines'])['rb']['ratio']:.4f}")
    buf = os.path.join(tempfile.mkdtemp(), "out.txt")
    so = sys.stdout
    sys.stdout = open(buf, "w")
    try:
        d = tempfile.mkdtemp()
        T.now = lambda: 1000.0
        T.read_balance = lambda: 70.0
        T.running_pods = lambda: set()
        T.cmd_preflight(d)
        T.now = lambda: 1300.0
        T.read_balance = lambda: 90.0
        T.watch_once(d, False)
    finally:
        sys.stdout.close()
        sys.stdout = so
    check("U1 the watcher's log says the balance rose, restarts, not a trip",
          "ROSE by $20.0000" in open(buf).read() and "Not a trip" in open(buf).read())
    r = simulate([(0, 60), (3, 63)], m=3.5, lag=8, step=5, topup=(13, 75.0))
    check("U2 overbilled 3.5 times with a top-up: restart at 16, trips in flight at minute 31",
          r.get("restart_at") == 16 and r["trip_at"] == 31 and "rule S" in (r["halt"] or ""), f"tripped at {r['trip_at']}")
    r = simulate([(0, 40)], m=1.4, lag=8, step=5, topup=(13, 75.0))
    st = T.load_state(r["dir"])
    fin = T.rule_d(st["readings"], st["machines"])["rb"]["ratio"]
    check("U3 overbilled 1.4 times with a top-up: NOT caught (the stated cost), final about 1.25",
          r["trip_at"] is None and 1.20 <= fin <= 1.30, f"{fin:.4f}")
    r = simulate([(0, 40)], m=1.0, lag=0, step=1, topup=(13, 75.0))
    st = T.load_state(r["dir"])
    fin = T.rule_d(st["readings"], st["machines"])["rb"]["ratio"]
    check("U4 honest, no lag, with a top-up: no trip, reads low (about 0.62)", r["trip_at"] is None and 0.58 <= fin <= 0.66,
          f"{fin:.4f}")
    keep = T.RESTART_LOOKBACK_S
    T.RESTART_LOOKBACK_S = 0
    try:
        r = simulate([(0, 40)], m=1.0, lag=8, step=5, topup=(13, 75.0))
    finally:
        T.RESTART_LOOKBACK_S = keep
    check("U5 the plain restart (no allowance) would false-trip U1 at minute 56", r["trip_at"] == 56,
          f"tripped at {r['trip_at']}")
    T.now = REAL_NOW


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

SAFE_PATH = "/usr/bin:/bin:/usr/sbin:/sbin"     # never the real vendor tool
# the one recorded answer meaning "this machine does not exist" (2026-09-26, to a delete)
RECORDED_NOTFOUND = '{"error":"api error: {\\"error\\":\\"pod not found to terminate\\",\\"status\\":404} (status 404)"}'
GOOD_EMPTY_LIST = "0|[]"
LIST_WITH_IT = '0|[{"id": "fakepod0000001"}]'


def stub_vendor(tmp: str, delete: str, get: str, lists=(GOOD_EMPTY_LIST,)) -> str:
    """A stand-in `runpodctl`. delete and get answers are 'rc|text' (or
    'hang'); `lists` are the answers to successive `pod list` calls, the last
    one repeated. Every call is logged."""
    b = os.path.join(tmp, "bin")
    os.makedirs(b, exist_ok=True)
    calls = os.path.join(tmp, "calls")
    n = os.path.join(tmp, "list_n")

    def part(spec):
        if spec == "hang":
            return "exec sleep 3600"
        rc, text = spec.split("|", 1)
        return f"printf '%s\\n' '{text}'; exit {rc}"
    arms = "\n".join(f'    {i}) {part(x)} ;;' for i, x in enumerate(lists))
    with open(os.path.join(b, "runpodctl"), "w") as f:
        f.write(f"""#!/bin/bash
echo "$*" >> "{calls}"
case "$1 $2" in
  "pod delete") {part(delete)} ;;
  "pod get") {part(get)} ;;
  "pod list")
    i=$(cat "{n}" 2>/dev/null || echo 0); echo $((i + 1)) > "{n}"
    [ "$i" -ge {len(lists) - 1} ] && i={len(lists) - 1}
    case "$i" in
{arms}
    esac ;;
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
    print("T9/W1-W7  the watchdog's deletion record (corrected after the check: the vendor's own")
    print("          'pod not found ... (status 404)', and two good machine lists without the machine)")
    for name, delete, get, lists, want in (
        ("W1 delete accepted; both lists good, machine absent", "0|pod fakepod0000001 deleted", "1|",
         (GOOD_EMPTY_LIST,), True),
        ("W2 delete accepted; first list read fails", "0|deleted", "1|", ("1|Error: request failed",), False),
        ("W3 delete accepted; first list good, second shows the machine", "0|deleted", "1|",
         (GOOD_EMPTY_LIST, LIST_WITH_IT), False),
        ("W4 delete answered with the recorded 'pod not found ... (status 404)'; lists good", "1|" + RECORDED_NOTFOUND,
         "1|", (GOOD_EMPTY_LIST,), True),
        ("W5 delete fails 'HTTP 503'; lists good and empty", "1|HTTP 503", "1|", (GOOD_EMPTY_LIST,), False),
        ("(T9) a failed delete, machine still listed", "1|HTTP 503", '0|{"id": "fakepod0000001"}', (LIST_WITH_IT,), False),
    ):
        tmp = tempfile.mkdtemp()
        b = stub_vendor(tmp, delete, get, lists)
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
        subprocess.run(["bash", os.path.join(OPS, "watch_run_a3.sh"), envf], capture_output=True, text=True,
                       env=dict(os.environ, PATH=b + ":" + SAFE_PATH, KILL_SETTLE_S="0", FINAL_TRIES="1",
                                GONE_CONFIRM_GAP_S="1"), timeout=60)
        rec = os.path.join(dest, "machine_gone_fakepod0000001")
        m = T.load_state(td)["machines"]["fakepod0000001"]
        if want:
            ok = (os.path.exists(rec) and "machine fakepod0000001 " in open(rec).read()
                  and m.get("gone") and t0 - 1 <= m["gone"] <= time.time() + 1 and m.get("gone_by") == "the watchdog")
        else:
            ok = not os.path.exists(rec) and not m.get("gone")
        check(f"{name}: {'record file and alarm time written' if want else 'no record anywhere'}", ok,
              (open(rec).read().strip()[:110] if os.path.exists(rec) else "no record file"))
        shutil.rmtree(tmp, ignore_errors=True)

    # found gone over three silent checks: the record needs the vendor's own words, then two good lists
    for name, get, want in (("W6 found gone; pod get gives the vendor's words; lists good", "1|" + RECORDED_NOTFOUND, True),
                            ("W7 found gone; pod get gives 'Error: api error: 404 page not found (status 404)'",
                             "1|Error: api error: 404 page not found (status 404)", False),
                            ("(T9) found gone; three failed readings only", "1|HTTP 503", False)):
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
                       env=dict(os.environ, PATH=b + ":" + SAFE_PATH, MISSING_GAP_S="0", PROBE_S="1",
                                GONE_CONFIRM_GAP_S="1"), timeout=60)
        rec = os.path.join(dest, "machine_gone_fakepod0000001")
        check(f"{name}: {'record written' if want else 'no record'}", os.path.exists(rec) == want)
        shutil.rmtree(tmp, ignore_errors=True)


CAP_S = 2


def run_timer(name, get, lists=(GOOD_EMPTY_LIST,), record_for=None, deadline_s=4, want_delete=True,
              trip=False, check_s=1, no_tool=False, quiet=False):
    """One run of the laptop deadline timer against a stand-in. Timing is
    measured against the deadline as WRITTEN (whole seconds), not the
    unrounded clock (the check's problem 7)."""
    tmp = tempfile.mkdtemp()
    b = stub_vendor(tmp, "0|pod fakepod0000001 deleted", get, lists)
    if no_tool:
        os.remove(os.path.join(b, "runpodctl"))
    if record_for:
        open(os.path.join(tmp, "machine_gone_fakepod0000001"), "w").write(
            f"machine {record_for} (x) deleted at 2026-10-05T00:38:01Z (1791161881), confirmed by the watchdog: test\n")
    td = trip_dir_with("fakepod0000001") if trip else None
    now = int(time.time())
    written_deadline = now + deadline_s
    envf = os.path.join(tmp, "machine_deadline_fakepod0000001.env")
    open(envf, "w").write(f"""POD="fakepod0000001"
OUT="t10"
CREATED_AT_EPOCH={now}
DELETE_AT_EPOCH={written_deadline}
HARD_CAP_USD="0.0011"
RATE_PER_HOUR_USD="0.99"
POSTED_RATE="0.99"
POLL_S=1
VENDOR_CHECK_S={check_s}
VENDOR_CAP_S={CAP_S}
""" + (f"""TRIP_PY="{sys.executable}"
TRIP_SCRIPT="{os.path.join(SRC, 'tripwire.py')}"
TRIP_DIR="{td}"
""" if trip else ""))
    t0 = time.time()
    r = subprocess.run(["bash", os.path.join(OPS, "machine_deadline.sh"), envf], capture_output=True, text=True,
                       env=dict(os.environ, PATH=b + ":" + SAFE_PATH), timeout=120)
    end = time.time()
    calls = open(os.path.join(tmp, "calls")).read() if os.path.exists(os.path.join(tmp, "calls")) else ""
    deleted = "pod delete" in calls
    line = "DEADLINE REACHED" in r.stdout
    stood = "STANDING DOWN" in r.stdout
    if no_tool:
        ok = not stood and line and "FAILED" in r.stdout and end >= written_deadline
    elif want_delete:
        ok = deleted and line and not stood and written_deadline <= end <= written_deadline + CAP_S + 3
    else:
        ok = (not deleted) and (not line) and end < written_deadline and r.returncode == 0 and stood
    if not quiet:
        check(name, ok, f"ended {end - written_deadline:+.1f}s from the written deadline, delete called: {deleted}, "
                        f"deadline line: {line}, stood down: {stood}")
    if trip:
        m = T.load_state(td)["machines"]["fakepod0000001"]
        if not quiet:
            check("T15 the alarm's records show the timer's deletion time, by the machine deadline",
                  m.get("gone") is not None and m.get("gone_by") == "the machine deadline" and t0 <= m["gone"] <= end + 1)
    shutil.rmtree(tmp, ignore_errors=True)
    return ok


def deadline_cases() -> None:
    print("T10-T15, N1-N8  the laptop deadline timer")
    run_timer("T10 the watchdog's record names this machine: stands down, no delete, no deadline line",
              "1|HTTP 503", record_for="fakepod0000001", deadline_s=6, want_delete=False)
    run_timer("T11/N4 the recorded 'pod not found ... (status 404)' and a good list without it, two checks: stands down",
              "1|" + RECORDED_NOTFOUND, deadline_s=8, want_delete=False)
    run_timer("T12 a failed vendor reading (error, no 'not found'): keeps running, deletes at the deadline", "1|HTTP 503")
    run_timer("T13 an empty vendor answer: keeps running, deletes at the deadline", "0|")
    run_timer("T14 a record naming another machine: ignored, deletes at the deadline", "1|HTTP 503",
              record_for="someotherpod00")
    run_timer("T15 deletes at its deadline with the alarm configured", '0|{"id": "fakepod0000001"}', trip=True)
    run_timer("(added) a vendor read that hangs: the deadline still deletes, at most the cap late", "hang",
              deadline_s=5)
    # the check's three false-positive answers (pull request 117, problem 1)
    run_timer("N1 'Error: api error: 404 page not found (status 404)', list good: stays armed, deletes",
              "1|Error: api error: 404 page not found (status 404)", deadline_s=5)
    print("      (N2 waits for the timer's three failed delete attempts, about 40 seconds)")
    run_timer("N2 the vendor tool missing from the command path ('command not found'): never stands down",
              "1|unused", deadline_s=5, no_tool=True)
    run_timer("N3 'Config File \"config\" Not Found in \"[/Users/x/.runpod]\"': stays armed, deletes",
              '1|Config File "config" Not Found in "[/Users/x/.runpod]"', deadline_s=5)
    run_timer("N5 the vendor's words, but the machine list fails: stays armed, deletes",
              "1|" + RECORDED_NOTFOUND, lists=("1|Error: request failed",), deadline_s=5)
    run_timer("N6 the vendor's words, but the list shows the machine: stays armed, deletes",
              "1|" + RECORDED_NOTFOUND, lists=(LIST_WITH_IT,), deadline_s=5)
    run_timer("N7 the vendor's words and a good list, but only one check before the deadline: stays armed, deletes",
              "1|" + RECORDED_NOTFOUND, deadline_s=5, check_s=3)
    run_timer("N8 the old T11 answer '{\"error\":\"pod not found\",\"status\":404}': now stays armed, deletes",
              '1|{"error":"pod not found","status":404}', deadline_s=5)
    print("F1  the timing cases, five full runs in a row")
    results = []
    for _ in range(5):
        results += [run_timer("", "1|HTTP 503", quiet=True), run_timer("", "0|", quiet=True),
                    run_timer("", "hang", deadline_s=5, quiet=True),
                    run_timer("", "1|" + RECORDED_NOTFOUND, deadline_s=8, want_delete=False, quiet=True)]
    check("F1 all pass in five runs", all(results), f"{sum(results)} of {len(results)}")


# ---------------------------------------------------------------- the lock (check problem 4)

def lock_cases() -> None:
    print("L1-L3  the lock on the alarm's records (the check's race, reproduced)")
    clock = [1_900_000_000.0]
    T.now = lambda: clock[0]
    d = tempfile.mkdtemp()
    T.read_balance = lambda: 75.0
    T.running_pods = lambda: {"podA"}
    with Quiet():
        T.cmd_preflight(d)
        T.cmd_register(d, "podA", 0.99, 1.0, "o")
    clock[0] += 1800
    deleted_at = clock[0] - 5

    def balance_while_watchdog_writes():
        with Quiet():
            T.cmd_gone(d, "podA", deleted_at, "the watchdog")
        return 74.5
    T.read_balance = balance_while_watchdog_writes
    T.running_pods = lambda: set()
    with Quiet():
        T.watch_once(d, True)
    m = T.load_state(d)["machines"]["podA"]
    check("L1 the watchdog's deletion time, written during the watcher's vendor read, survives",
          m.get("gone_by") == "the watchdog" and m.get("gone") == deleted_at, f"{m.get('gone_by')!r}")

    d2 = tempfile.mkdtemp()
    T.read_balance = lambda: 75.0
    T.running_pods = lambda: {"podA"}
    with Quiet():
        T.cmd_preflight(d2)
        T.cmd_register(d2, "podA", 0.99, 1.0, "o")
    clock[0] += 300

    def balance_while_launcher_registers():
        with Quiet():
            T.cmd_register(d2, "podB", 0.99, 1.0, "o")
        return 74.9
    T.read_balance = balance_while_launcher_registers
    T.running_pods = lambda: {"podA", "podB"}
    with Quiet():
        T.watch_once(d2, True)
    check("L2 a second machine registered during the watcher's vendor read survives",
          "podB" in T.load_state(d2)["machines"])
    T.now = REAL_NOW

    d3 = trip_dir_with("podC")
    holder = subprocess.Popen([sys.executable, "-c",
                               "import fcntl,sys,time; f=open(sys.argv[1],'a'); fcntl.flock(f,fcntl.LOCK_EX); "
                               "print('held',flush=True); time.sleep(2)", os.path.join(d3, "state.lock")],
                              stdout=subprocess.PIPE, text=True)
    holder.stdout.readline()
    t0 = time.time()
    r = subprocess.run([sys.executable, os.path.join(SRC, "tripwire.py"), "gone", "--state", d3, "--pod", "podC",
                        "--at", "1234", "--by", "the watchdog"], capture_output=True, text=True)
    waited = time.time() - t0
    holder.wait()
    check("L3 with the lock held by another program for 2 s, gone waits for it, then records",
          waited >= 1.5 and r.returncode == 0 and T.load_state(d3)["machines"]["podC"]["gone"] == 1234.0,
          f"waited {waited:.1f}s")


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
    top_ups()
    deletion_records()
    watchdog_cases()
    deadline_cases()
    lock_cases()
    replay()
    print(f"\n{len(FAILS)} failure(s): {FAILS}" if FAILS else "\nall checks pass. nothing was rented and nothing was spent.")
    sys.exit(1 if FAILS else 0)
