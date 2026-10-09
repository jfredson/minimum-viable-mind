"""Compare a re-run's summarised folders against an earlier run's (the
end-to-end test on the final code, method
docs/2026-10-08-end-to-end-final-code-method.md). Written after the method,
before its output was read.

For every folder holding a table.md: summary.json (and steps.json, where
present) must be byte-identical; every table line that differs must differ
only by one fewer "withheld" cell (the 2026-10-08 table-layout fix); and every
table row in the new run must have as many cells as its header.

    python tests/e2e_compare_tables.py OLD_DIR NEW_DIR
"""
import os
import sys

old_root, new_root = sys.argv[1], sys.argv[2]


def cells(line):
    return line.strip().strip("|").split("|")


problems, n_folders, n_changed, n_rows = [], 0, 0, 0
for dirpath, _, files in sorted(os.walk(new_root)):
    if "table.md" not in files:
        continue
    rel = os.path.relpath(dirpath, new_root)
    od = os.path.join(old_root, rel)
    n_folders += 1
    for f in ("summary.json", "steps.json"):
        if os.path.exists(os.path.join(dirpath, f)) or os.path.exists(os.path.join(od, f)):
            try:
                a = open(os.path.join(od, f), "rb").read()
                b = open(os.path.join(dirpath, f), "rb").read()
            except FileNotFoundError as e:
                problems.append(f"{rel}/{f} missing on one side: {e}")
                continue
            if a != b:
                problems.append(f"{rel}/{f} differs")
    old = open(os.path.join(od, "table.md")).read().splitlines()
    new = open(os.path.join(dirpath, "table.md")).read().splitlines()
    if len(old) != len(new):
        problems.append(f"{rel}/table.md: line count {len(old)} -> {len(new)}")
        continue
    header = None
    for o, n in zip(old, new):
        if n.startswith("|"):
            if header is None:
                header = len(cells(n))
            elif len(cells(n)) != header:
                problems.append(f"{rel}/table.md: row has {len(cells(n))} cells, header {header}: {n[:40]}")
            else:
                n_rows += 1
        if o != n:
            n_changed += 1
            if o.replace("| withheld ", "", 1) != n:
                problems.append(f"{rel}/table.md: a line changed beyond one withheld cell: {n[:40]}")
print(f"{n_folders} folders compared; {n_rows} table rows (separator rows included) match their header's cell count; "
      f"{n_changed} table lines changed, each by one withheld cell; problems: {problems}")
sys.exit(1 if problems else 0)
