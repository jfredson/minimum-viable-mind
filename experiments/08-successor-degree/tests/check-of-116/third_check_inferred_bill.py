"""Third check: the 0.90 line for a machine whose deletion the alarm only
inferred. Drives the alarm's own commands with a stand-in clock, balance,
machine list and bill. $0.

    python tests/check-of-116/third_check_inferred_bill.py   (from experiments/08-successor-degree)
"""
from __future__ import annotations

import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "src"))
import tripwire as T  # noqa: E402

T0 = 1_900_000_000.0


def quiet(f, *a):
    so = sys.stdout
    sys.stdout = open(os.devnull, "w")
    try:
        return f(*a)
    finally:
        sys.stdout.close()
        sys.stdout = so


def case(name, life_min, billed_min, readings_min, recorded=False):
    """One machine created at minute 0; the watcher reads at readings_min;
    the machine is listed while minute < life_min. Returns the reconcile exit."""
    d = tempfile.mkdtemp()
    clock = [T0]
    T.now = lambda: clock[0]
    T.read_balance = lambda: 75.0 - 0.99 * min((clock[0] - T0) / 3600, life_min / 60)
    T.running_pods = lambda: {"p"} if (clock[0] - T0) / 60 < life_min else set()
    quiet(T.cmd_preflight, d)
    quiet(T.cmd_register, d, "p", 0.99, 1.0, "o")
    if recorded:
        quiet(T.cmd_gone, d, "p", T0 + life_min * 60, "the watchdog")
    for m in readings_min:
        clock[0] = T0 + m * 60
        quiet(T.watch_once, d, False)
    T.billed_hours = lambda pod, since: billed_min / 60
    clock[0] = T0 + 4 * 3600
    rc = quiet(T.cmd_reconcile, d)
    st = T.load_state(d)["machines"]["p"]
    why = (T.halted(d) or "").splitlines()[0][:110] if T.halted(d) else ""
    print(f"  {name}: exit {rc}; inferred {st.get('gone_inferred')}; {why}")
    shutil.rmtree(d, ignore_errors=True)
    return rc


print("The 0.90 line after the third round's correction (honest bills unless stated):")
every5 = [1 + 5 * k for k in range(14)]                     # 1, 6, 11, ... 66
case("20-min machine, deletion inferred at the next reading, honest bill", 20, 20, every5)
case("29-min machine, inferred about 3 min late, honest bill", 29, 29, every5)
case("44-min machine, inferred, honest bill", 44, 44, every5)
case("same 20-min machine, only half its bill posted", 20, 10, every5)
case("same 20-min machine, billed 1.3 times its life", 20, 26, every5)
case("3-min machine, never seen listed by the watcher, inferred, honest bill", 3, 3, every5)
case("3-min machine, deletion recorded by the watchdog, honest bill", 3, 3, every5, recorded=True)
