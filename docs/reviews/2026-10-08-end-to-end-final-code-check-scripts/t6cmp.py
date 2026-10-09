import os, sys, filecmp, json
A, B = sys.argv[1], sys.argv[2]
for size in ("10M", "30M"):
    a, b = f"{A}/{size}", f"{B}/{size}"
    if not os.path.isdir(a) or not os.path.isdir(b): print(size, "missing", os.path.isdir(a), os.path.isdir(b)); continue
    fa = sorted(os.path.relpath(os.path.join(r, f), a) for r, _, fs in os.walk(a) for f in fs)
    fb = sorted(os.path.relpath(os.path.join(r, f), b) for r, _, fs in os.walk(b) for f in fs)
    print(size, "files only in first:", sorted(set(fa) - set(fb)), "only in second:", sorted(set(fb) - set(fa)))
    for f in sorted(set(fa) & set(fb)):
        if f.endswith(".pt") or f.endswith(".log"): continue
        same = filecmp.cmp(f"{a}/{f}", f"{b}/{f}", False)
        print(f"  {f}: {'identical' if same else 'DIFFERS'}")
