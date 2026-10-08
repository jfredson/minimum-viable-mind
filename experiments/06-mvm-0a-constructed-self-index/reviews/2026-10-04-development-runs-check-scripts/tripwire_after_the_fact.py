"""Both tripwire ratios for the dev-10m wave, worked out after the fact.

Reads the tripwire state as it stood at 00:52Z (a copy kept by this check
before the watcher's 01:11Z reading changed it), fills in each machine's
deletion time from its laptop watchdog log ("pod gone"), adds one balance
reading taken now, and runs the frozen tripwire's own arithmetic: ratio B
(`ratio_b`) and ratio A (`cmd_reconcile`, which reads the vendor's billing
rows). Everything is written to a scratch copy; the artifact folder is not
touched. Vendor contact: read only (balance, billing). $0.

    python tripwire_after_the_fact.py SNAPSHOT_DIR SCRATCH_DIR ARTIFACTS_DIR
"""
import json, os, re, shutil, sys, calendar, time
snap, scratch, art = sys.argv[1:4]
sys.path.insert(0, os.path.join(os.path.dirname(art.rstrip("/")), "src"))
import tripwire as T

os.makedirs(scratch, exist_ok=True)
shutil.copy(os.path.join(snap, "state.json"), os.path.join(scratch, "state.json"))
st = T.load_state(scratch)
for pod, m in st["machines"].items():
    log = open(os.path.join(art, m["out"], "watchdog.log")).read()
    t = re.findall(r"\[(\S+Z)\] pod gone; billing stopped", log)
    assert len(t) == 1, (pod, t)
    m["gone"] = calendar.timegm(time.strptime(t[0], "%Y-%m-%dT%H:%M:%SZ"))
    m["gone_iso_from_watchdog"] = t[0]
    m["life_minutes"] = round((m["gone"] - m["created"]) / 60, 2)
bal = T.read_balance()
st["readings"].append(dict(t=time.time(), balance=bal, source="this check, after the wave"))
T.save_state(scratch, st)
rb = T.ratio_b(st["readings"], st["machines"], time.time())
print("machines, with deletion times from the watchdog logs:")
for m in sorted(st["machines"].values(), key=lambda m: m["created"]):
    print(f"  {m['out']}: created {m['created_iso']}, gone {m['gone_iso_from_watchdog']}, "
          f"{m['life_minutes']} min")
print(f"ratio B over the whole wave: {rb['ratio']:.4f} "
      f"(drawn ${rb['drawn']:.4f} against expected ${rb['expected']:.4f} over {rb['hours']:.3f} h; "
      f"balance {rb['first']['balance']:.4f} -> {rb['last']['balance']:.4f})")
print("ratio A (the vendor's billed hours / machine life), by the frozen reconcile:")
rc = T.cmd_reconcile(scratch)
print(f"reconcile exit code {rc} (0 = no trip, 3 = trip or a check that could not run)")
print("HALT written in scratch:" , os.path.exists(os.path.join(scratch, "HALT")))
json.dump(dict(ratio_b=rb, reconcile_exit=rc), open(os.path.join(scratch, "after_the_fact.json"), "w"),
          indent=1, default=str)
