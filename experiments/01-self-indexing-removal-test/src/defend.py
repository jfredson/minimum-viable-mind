"""Defender / adjudication half of the red-team loop.

`red_team.py` (Gemini, a different model family) attacks the design. This script
runs the other half: a stake-free Claude defender reads the latest findings and
assigns each one exactly ONE disposition — PATCH, ACCEPTED-RISK, ROUTED-UPSTREAM,
or PILOT-REQUIRED — under the verbatim brief in `defend_prompt.md`. Each defense
must carry its own loss condition (the rule the program applies to every claim,
turned on the defender itself).

The defender shares the builder's model family, so it is NOT the arbiter: it
structures each disagreement and flags high-severity / low-confidence findings
for John. Optional --rebut runs one bounded Gemini counter-round so the defender
does not get the last word.

Outputs (to artifacts/red_team/, gitignored):
  adjudication_<stamp>.json   defenses (+ rebuttals if --rebut)
  proposed_ledger_<stamp>.md  ledger rows to MERGE by hand into the committed
                              red_team_ledger.md after you adjudicate.

Run from the repo root, venv active:
    set -a; source .env; set +a            # ANTHROPIC_API_KEY (+ GEMINI for --rebut)
    python experiments/01-self-indexing-removal-test/src/defend.py
Options:
    --findings PATH   adjudicate a specific findings file (default: latest)
    --rebut           one bounded Gemini counter-round on the defenses
    --dry-run         assemble the defender prompt + token estimate; no API call
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from pathlib import Path

SELF_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SELF_DIR))

import red_team  # noqa: E402  (sets up paths + mvm.config on import; reused helpers)

# Stake-free defender. Same family as the builder on purpose is acceptable here:
# independence is the red team's job; the defender's job is rigorous disposition,
# guarded by the Gemini rebuttal round and human adjudication.
DEFENDER_MODEL = "claude-opus-4-8"

PROMPT_PATH = SELF_DIR / "defend_prompt.md"
OUT_DIR = red_team.OUT_DIR


def latest_findings() -> Path:
    hits = sorted(OUT_DIR.glob("findings_*.json"))
    if not hits:
        sys.exit(f"no findings_*.json in {OUT_DIR}. Run red_team.py first.")
    return hits[-1]


def build_defender_content(docs: str, findings_obj: dict) -> str:
    findings = json.dumps(findings_obj.get("findings", []), indent=2)
    return (
        "Adjudicate each red-team finding below against the design documents. "
        "Engage each attack on its merits and assign exactly one disposition, "
        "with its own loss condition, per your brief.\n\n"
        "===== DESIGN DOCUMENTS =====\n" + docs +
        "\n\n===== RED-TEAM FINDINGS (one defense each, same order) =====\n"
        + findings + "\n"
    )


def render_ledger(findings_obj: dict, defenses: dict, stamp: str, src: str) -> str:
    """Build proposed ledger rows by joining findings to their dispositions."""
    by_id = {f.get("id"): f for f in findings_obj.get("findings", [])}
    rows = [
        "| id | sev | target | disposition | for-John | reason |",
        "|----|-----|--------|-------------|----------|--------|",
    ]
    for d in defenses.get("defenses", []):
        f = by_id.get(d.get("id"), {})
        reason = (d.get("reasoning", "") or "").replace("|", "\\|")
        if len(reason) > 100:
            reason = reason[:97] + "..."
        rows.append(
            f"| {d.get('id','?')} | {f.get('severity','?')} | "
            f"{f.get('target','?')} | {d.get('disposition','?')} | "
            f"{'YES' if d.get('needs_human_adjudication') else ''} | {reason} |"
        )
    header = (f"## Proposed rows — {stamp}\n\n"
              f"From `{src}`. Adjudicate, then merge into the table in "
              f"`red_team_ledger.md`. Disposition is the defender's proposal, "
              f"not a decision.\n\n")
    return header + "\n".join(rows) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="Defender/adjudication pass.")
    ap.add_argument("--findings", default=None, help="findings file (default: latest)")
    ap.add_argument("--rebut", action="store_true",
                    help="one bounded Gemini counter-round on the defenses")
    ap.add_argument("--dry-run", action="store_true",
                    help="assemble the defender prompt + token estimate; no API call")
    args = ap.parse_args()

    assert "gemma" not in DEFENDER_MODEL.lower(), "defender must not be the model under test"

    findings_path = Path(args.findings) if args.findings else latest_findings()
    findings_obj = json.loads(findings_path.read_text())
    system_prompt = PROMPT_PATH.read_text()
    docs = red_team.load_docs(red_team.DEFAULT_INPUTS)
    user_content = build_defender_content(docs, findings_obj)

    n = len(findings_obj.get("findings", []))
    full = system_prompt + "\n\n" + user_content
    print(f"defender: {DEFENDER_MODEL}")
    print(f"adjudicating {n} finding(s) from {findings_path.name}")
    print(f"assembled prompt: ~{len(full):,} chars (~{len(full)//4:,} tokens est.)\n")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    if args.dry_run:
        p = OUT_DIR / f"defender_prompt_{stamp}.txt"
        p.write_text(full)
        print(f"[dry-run] no API call made. Full prompt written to:\n  {p}")
        return

    import anthropic  # noqa: E402  (lazy: --dry-run needs no SDK/key)
    try:
        client = anthropic.Anthropic()
    except Exception as e:
        sys.exit(f"could not init Anthropic client: {e}\nSet ANTHROPIC_API_KEY.")

    print("running defense pass...")
    try:
        msg = client.messages.create(
            model=DEFENDER_MODEL,
            max_tokens=8192,
            system=system_prompt,
            messages=[{"role": "user", "content": user_content}],
        )
    except Exception as e:
        sys.exit(f"defender call failed: {e}")
    raw = "".join(b.text for b in msg.content if b.type == "text")
    (OUT_DIR / f"defense_raw_{stamp}.txt").write_text(raw)
    try:
        defenses = red_team.parse_findings(raw)
    except Exception as e:
        sys.exit(f"could not parse defenses: {e}\nRaw saved to defense_raw_{stamp}.txt")

    adjudication = {
        "defender_model": DEFENDER_MODEL,
        "findings_file": findings_path.name,
        "generated_utc": stamp,
        "defenses": defenses.get("defenses", []),
        "defense_summary": defenses.get("summary", ""),
    }

    if args.rebut:
        print("running one bounded Gemini rebuttal round...")
        try:
            from google import genai
            gclient = genai.Client()
            rebut_user = (
                "You raised the findings below. Here are the defender's "
                "dispositions. For EACH finding, either concede the disposition "
                "or maintain your attack with a one-paragraph counter. Respond "
                "with ONLY JSON: {\"rebuttals\":[{\"id\":...,\"stance\":"
                "\"concede\"|\"maintain\",\"counter\":\"...\"}]}\n\n"
                "FINDINGS:\n" + json.dumps(findings_obj.get("findings", []), indent=2)
                + "\n\nDEFENSES:\n" + json.dumps(defenses.get("defenses", []), indent=2)
            )
            r = gclient.models.generate_content(
                model=red_team.RED_TEAM_MODEL,
                contents=rebut_user,
                config={"response_mime_type": "application/json"},
            )
            adjudication["rebuttals"] = red_team.parse_findings(r.text or "").get("rebuttals", [])
        except Exception as e:
            print(f"  (rebuttal round skipped: {e})")

    out_path = OUT_DIR / f"adjudication_{stamp}.json"
    out_path.write_text(json.dumps(adjudication, indent=2))
    ledger_path = OUT_DIR / f"proposed_ledger_{stamp}.md"
    ledger_path.write_text(render_ledger(findings_obj, defenses, stamp, findings_path.name))

    defs = defenses.get("defenses", [])
    from collections import Counter
    disp = Counter(d.get("disposition") for d in defs)
    for_john = [d for d in defs if d.get("needs_human_adjudication")]
    print(f"\n=== adjudication ===")
    for d in defs:
        flag = "  <- for John" if d.get("needs_human_adjudication") else ""
        print(f"  {d.get('id','?'):6s} {d.get('disposition','?'):16s} "
              f"({d.get('confidence','?')}){flag}")
    print(f"\ndispositions: {dict(disp)}; {len(for_john)} flagged for human adjudication")
    if defenses.get("summary"):
        print(f"\nsummary: {defenses['summary']}")
    print(f"\nwrote {out_path}\n      {ledger_path}")
    print("\nNext: adjudicate the for-John rows, then merge proposed_ledger into "
          "the committed red_team_ledger.md. PATCHes must land before thresholds lock.")


if __name__ == "__main__":
    main()
