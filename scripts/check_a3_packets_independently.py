#!/usr/bin/env python3
"""A second, separate check that the two tier 2 packets carry the same material.

The builder checks itself; this does not use the builder. It reads only the
built files and the source files, rebuilds each split record from its parts by
hand, and compares. Run it from the top of the repository.
"""

import glob
import os
import re

P = "experiments/06-mvm-0a-constructed-self-index/reviews/packets/"
GEM = P + "2026-09-21-a3-closure-tier2-gemini.md"

WHOLE = """docs/a3-closure-text-draft-2026-09-21-v4.md
experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-claude-worktree.md
experiments/06-mvm-0a-constructed-self-index/amendment-a3.md
experiments/06-mvm-0a-constructed-self-index/pre-registration.md
experiments/06-mvm-0a-constructed-self-index/seeds-endpoint-findings.md
experiments/06-mvm-0a-constructed-self-index/ceiling-measurement-findings.md
experiments/06-mvm-0a-constructed-self-index/ceiling-defect-2026-09-17.md
experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot-findings.md
experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings.md
experiments/06-mvm-0a-constructed-self-index/fitted-position-sweep-findings-CORRECTION-2026-09-20.md
experiments/06-mvm-0a-constructed-self-index/standardised-refit-findings.md
experiments/06-mvm-0a-constructed-self-index/other-index-position-sweep-findings.md
experiments/06-mvm-0a-constructed-self-index/powered-position-sweep-findings.md
docs/rulings/2026-09-20-center-as-degree.md
docs/rulings/2026-09-20-december-result-roadmap.md
docs/rulings/2026-09-21-followup-runs-and-blind-arm.md
docs/competing-mechanisms-2026-09-20.md
experiments/06-mvm-0a-constructed-self-index/separation-clause-requirements.md""".split()

SPLIT = {
    4: "experiments/06-mvm-0a-constructed-self-index/reviews/2026-09-21-a3-closure-claude-worktree.md",
    5: "experiments/06-mvm-0a-constructed-self-index/amendment-a3.md",
    6: "experiments/06-mvm-0a-constructed-self-index/pre-registration.md",
}

SENTENCE = ("Do not soften findings to be polite, and do not manufacture severity to "
            "look thorough. A pass that finds nothing fatal is a valid result, "
            "reported as what was checked and what held.")


def slurp(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def bodies(text):
    """{(record number, part number): the record text} from a built packet file."""
    out = {}
    for m in re.finditer(r"^===== RECORD (\d+) of 23(?:, part (\d+) of \d+)? - ", text, re.M):
        start = text.index("\n", m.end()) + 1
        end = text.index("\n===== END OF RECORD", start)
        lines = text[start:end].split("\n")
        lines.pop(0)
        for prefix in ("*Source note:", "*This part is"):
            if lines and lines[0].startswith(prefix):
                while lines and lines[0] != "":
                    lines.pop(0)
                lines.pop(0)
        lines.pop()
        out[(int(m.group(1)), int(m.group(2) or 1))] = "\n".join(lines)
    return out


def joined(d, n):
    return "\n".join(v for k, v in sorted(d.items()) if k[0] == n)


def main():
    gem = slurp(GEM)
    cg_paths = sorted(glob.glob(P + "*-chatgpt-*.md"))
    cg_all = "\n".join(slurp(p) for p in cg_paths)

    ok = True
    missing = [f for f in WHOLE if slurp(f).rstrip("\n") not in gem]
    ok = ok and not missing
    print("1. each of the {} whole source files appears unbroken and unedited inside "
          "the Gemini document: {}".format(len(WHOLE), "YES" if not missing else missing))

    cg_bodies = {}
    for p in cg_paths:
        cg_bodies.update(bodies(slurp(p)))
    gm_bodies = bodies(gem)

    for n, f in sorted(SPLIT.items()):
        same = joined(cg_bodies, n) == slurp(f).rstrip("\n")
        ok = ok and same
        print("2. {:<44} rebuilt from its ChatGPT parts equals the file on disk: {}".format(
            os.path.basename(f), "YES" if same else "NO"))

    rg = sorted(set(k[0] for k in gm_bodies))
    rc = sorted(set(k[0] for k in cg_bodies))
    ok = ok and rg == rc and len(rg) == 23
    print("3. records present - Gemini {}, ChatGPT {}, the same 23: {}".format(
        len(rg), len(rc), "YES" if (rg == rc and len(rg) == 23) else "NO"))

    differs = [n for n in rg if joined(gm_bodies, n) != joined(cg_bodies, n)]
    ok = ok and not differs
    print("4. records whose text differs between the two packets: {}".format(
        differs or "none"))

    flat = lambda t: " ".join(t.split())
    checks = [SENTENCE in flat(slurp("docs/outside-review-protocol.md")),
              SENTENCE in flat(gem), SENTENCE in flat(slurp(cg_paths[0]))]
    ok = ok and all(checks)
    print("5. the amended sentence of the brief, word for word, in the protocol, the "
          "Gemini packet and ChatGPT file 01: {}".format(
              "YES" if all(checks) else checks))

    # The word was struck from the brief, not from the records that quote the
    # amendment striking it, so this is scoped to the brief itself (record 2).
    brief = joined(gm_bodies, 2)
    clean = brief == joined(cg_bodies, 2) and "unlikely" not in brief.lower()
    ok = ok and clean
    print("6. the brief carries no trace of the struck word \"unlikely\", in either "
          "packet: {}".format("YES" if clean else "NO"))
    stray = sum(1 for _ in re.finditer("unlikely", gem, re.I))
    print("   (the word survives {} times elsewhere in the packet, inside records that "
          "quote the amendment striking it and one unrelated sentence; those are "
          "verbatim records and are left alone)".format(stray))

    print("")
    print("all checks passed" if ok else "SOMETHING FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
