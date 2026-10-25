"""Rerun spend and ratio A from the committed end-of-wave reconcile record and the
alarm's state file (rate). Usage: python rerun_bills.py CLONE"""
import json, sys, os
d = os.path.join(sys.argv[1], "experiments/08-successor-degree/out-reruns-10m/tripwire-records")
rec = json.load(open(os.path.join(d, "reconcile.json")))
st = open(os.path.join(d, "state.json")).read()
rate = 1.19
assert '"rate": 1.19' in st
names = {"xp6pphlx9xo4rl": "M", "f08ds538z5ld7p": "T", "ao52cuhyg8lpor": "C"}
tb = tl = 0
for r in rec:
    a = names[r["pod"]]; tb += r["billed_hours"]; tl += r["existence_hours"]
    print(a, "billed h %.4f" % r["billed_hours"], "$%.4f" % (r["billed_hours"]*rate), "ratio A %.3f" % r["ratio_a"],
          "life h %.4f" % r["existence_hours"])
print("total billed h %.4f -> $%.4f at 1.19; lifetimes %.4f h -> $%.4f at 1.19, $%.4f at 0.99" % (tb, tb*rate, tl, tl*rate, tl*0.99))
print("over the approved 1.14: x%.3f; at 0.99 the gap would be %.4f" % (tb*rate/1.14, tl*0.99-1.14))
