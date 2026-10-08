"""Closure check of RT-239: the generator's self-test, and whether its two
named checks would catch each registered departure being undone.

Runs the frozen `grammar.py --self-test` unchanged, then copies `grammar.py`
to a scratch directory outside the repository (the first argument), applies
one mutation per copy, and runs each copy's self-test. Nothing in the
repository's code is changed.

  (i)   departure 1 undone: the own-directed action turn shows the model's own
        marker word where the "your own" word stood, three tokens before the
        answer slot, as the closed design does;
  (ii)  departure 2 undone: the answer is shown in the slot the mask word held;
  (iii) the turn count changed: two more turns, `<marker> revise <item> <value>`
        for the agents listed first and second, before the action turns (twelve
        turns, as the closed design has), with the episode length raised to fit.

The copies cannot reach the rehearsal's generator, so that one comparison is
skipped in them; it is not one of the two named checks.

    ~/Code/minimum-viable-mind/.venv/bin/python \
        docs/reviews/2026-10-09-serious-findings-closure-check-scripts/self_test_mutations.py <scratch dir>
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys

ROOT = os.getcwd()
SRC = os.path.join(ROOT, "experiments/08-successor-degree/src/grammar.py")
PY = sys.executable
NAMED = ("matched pairs are token-for-token identical", "no name badge")


def sub_once(text, old, new):
    assert text.count(old) == 1, (text.count(old), old)
    return text.replace(old, new)


MUTATIONS = {
    "(i) departure 1 undone: own marker word three tokens before the answer slot": [
        ("who_tok, who_idx = VOCAB[SELF], N_AGENTS",
         "who_tok, who_idx = VOCAB[MARKERS[markers[model]]], N_AGENTS"),
    ],
    "(ii) departure 2 undone: the answer shown in the mask word's slot": [
        ("        action_pos[cond] = len(toks)\n        toks.append(MASK_ID)",
         "        action_pos[cond] = len(toks)\n"
         "        toks.append(VOCAB[SLOTS[successor(int(values[src, j]))]])"),
    ],
    "(iii) turn count changed: twelve turns instead of ten": [
        ("SEQ_LEN = 1 + 8 * 5 + 2 * 7 + 1", "SEQ_LEN = 1 + 8 * 5 + 2 * 5 + 2 * 7 + 1"),
        ("    action_pos = np.zeros(2, dtype=np.int64)\n    action_item",
         "    for a in (0, 1):\n"
         "        toks.extend([VOCAB[MARKERS[markers[a]]], VOCAB['revise'], VOCAB[ITEMS[items[0]]],\n"
         "                     VOCAB[SLOTS[successor(int(values[a, 0]))]], VOCAB[NL]])\n"
         "        acting.extend([1 if a == model else 0] * 5)\n"
         "    action_pos = np.zeros(2, dtype=np.int64)\n    action_item"),
    ],
}


def run(path):
    p = subprocess.run([PY, path, "--self-test"], capture_output=True, text=True,
                       cwd=os.path.dirname(path))
    lines = (p.stdout + p.stderr).splitlines()
    checks = [l for l in lines if l.strip().startswith("[")]
    return p.returncode, checks, lines


def report(label, code, checks, lines):
    fails = [c for c in checks if "[FAIL]" in c]
    print(f"\n== {label}: exit code {code}; {len(checks)} checks printed, {len(fails)} failed")
    for n in NAMED:
        hit = [c for c in checks if n in c]
        print(f"   named check '{n}': {hit[0].strip() if hit else 'NOT PRINTED'}")
    for c in fails:
        print(f"   failed: {c.strip()[:160]}")
    if code and not checks:
        print("   " + "\n   ".join(lines[-6:]))


def main():
    scratch = sys.argv[1]
    os.makedirs(scratch, exist_ok=True)
    code, checks, lines = run(SRC)
    report("the frozen grammar.py, unchanged", code, checks, lines)
    original = open(SRC).read()
    for label, edits in MUTATIONS.items():
        text = original
        for old, new in edits:
            text = sub_once(text, old, new)
        d = os.path.join(scratch, re.sub(r"[^a-z0-9]+", "_", label.lower())[:40])
        os.makedirs(d, exist_ok=True)
        path = os.path.join(d, "grammar.py")
        open(path, "w").write(text)
        code, checks, lines = run(path)
        report(label, code, checks, lines)
    # the repository's file is untouched
    assert open(SRC).read() == original
    print("\nthe repository's grammar.py is unchanged:",
          subprocess.run(["git", "diff", "--quiet", "--", SRC], cwd=ROOT).returncode == 0)


if __name__ == "__main__":
    main()
