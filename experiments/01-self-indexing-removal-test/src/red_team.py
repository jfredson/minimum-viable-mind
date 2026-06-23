"""Adversarial design review by a held-out, different-family model (Gemini).

Why this exists. The builder of this repo and the S-battery judge
(`claude-opus-4-8`) are both Anthropic models, so they share a lineage and
likely share blind spots. A red team from a *different* model family breaks that
correlation — the same independence logic that put a held-out judge on the S
battery, applied one level up to the *design* rather than the outputs.

What it does. Feeds the design documents (spec, pre-registration, thresholds,
research notes; optionally the Stage 1 code) to Gemini 3.1 Pro under the
adversarial brief in `red_team_prompt.md`, which is read verbatim — change the
brief there, not in this file. The model returns structured findings: each
load-bearing claim restated as a wager, its loss condition (or MISSING), and a
concrete attack, plus a self-flag for objections that "prove too much".

This is a critic, not an oracle. Its output is a channel to triage, the way the
S battery is a channel to read — keep findings with teeth, discard ones that
would sink any experiment of this kind. It cannot adjudicate the metaphysics
(mutual opacity stands; the IIT-level disagreement is upstream of any test).

Run from the repo root, venv active, with a key in the environment:
    set -a; source .env; set +a          # provides GEMINI_API_KEY
    python experiments/01-self-indexing-removal-test/src/red_team.py
Options:
    --dry-run         assemble and save the full prompt, print a token estimate,
                      make no API call (works without the SDK or a key).
    --include-code    also submit the Stage 1 .py files for an implementation pass.
    --inputs A B ...  override the default document set (repo-relative paths).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mvm import config  # noqa: E402  (sets HF_HOME etc. on import; harmless here)

# Held-out red team — MUST be a different family from the builder and the judge.
# Gemini 3.1 Pro (1M-token context) ingests the whole design in one pass.
RED_TEAM_MODEL = "gemini-3.1-pro-preview"

PROMPT_PATH = Path(__file__).resolve().parent / "red_team_prompt.md"
OUT_DIR = config.ARTIFACTS_DIR / "red_team"

# The design under review, as repo-relative paths. Order is the order the model
# sees them; lead with the document that carries the decision rule.
DEFAULT_INPUTS = [
    "experiments/01-self-indexing-removal-test/pre-registration.md",
    "experiments/01-self-indexing-removal-test/thresholds.md",
    "spec/minimum-viable-mind-proposal-v0.1.md",
    "research/removal-test-vs-the-field-research-note.md",
    "research/minimum-viable-consciousness-literature-vs-our-writing.md",
]

# Added only with --include-code (the implementation pass).
CODE_INPUTS = [
    "experiments/01-self-indexing-removal-test/src/battery.py",
    "experiments/01-self-indexing-removal-test/src/run_baseline.py",
    "experiments/01-self-indexing-removal-test/src/judge.py",
    "experiments/01-self-indexing-removal-test/src/localize_probe.py",
    "experiments/01-self-indexing-removal-test/src/localize_sae.py",
]


def load_docs(rel_paths: list[str]) -> str:
    """Concatenate the input files, each fenced with its repo-relative path."""
    chunks = []
    for rel in rel_paths:
        p = REPO_ROOT / rel
        if not p.exists():
            sys.exit(f"input not found: {rel} (looked in {p})")
        chunks.append(
            f"===== BEGIN {rel} =====\n{p.read_text()}\n===== END {rel} =====\n"
        )
    return "\n".join(chunks)


def build_user_content(docs: str) -> str:
    return (
        "Here are the design documents to red-team. Apply the brief in your "
        "system instruction to all of them. Attack the design, not a strawman: "
        "the loss conditions and confounds these documents already state are "
        "fair game to defeat, but the findings that matter most are the ones "
        "they have not named.\n\n" + docs
    )


def parse_findings(text: str) -> dict:
    """Pull the JSON object out of the reply, tolerating stray fences/prose."""
    s = text.strip()
    if s.startswith("```"):
        s = s.split("```", 2)[1]
        if s.lstrip().lower().startswith("json"):
            s = s.lstrip()[4:]
    start, end = s.find("{"), s.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON object in reply: {text[:400]!r}")
    return json.loads(s[start : end + 1])


def main() -> None:
    ap = argparse.ArgumentParser(description="Adversarial design review (Gemini).")
    ap.add_argument("--dry-run", action="store_true",
                    help="assemble the prompt and estimate tokens; no API call")
    ap.add_argument("--include-code", action="store_true",
                    help="also submit the Stage 1 .py files")
    ap.add_argument("--inputs", nargs="+", default=None,
                    help="override default document set (repo-relative paths)")
    args = ap.parse_args()

    rel_paths = list(args.inputs) if args.inputs else list(DEFAULT_INPUTS)
    if args.include_code and not args.inputs:
        rel_paths += CODE_INPUTS

    assert "gemini" in RED_TEAM_MODEL.lower(), \
        "red team must be a different family from the builder/judge"

    system_prompt = PROMPT_PATH.read_text()
    docs = load_docs(rel_paths)
    user_content = build_user_content(docs)
    full = system_prompt + "\n\n" + user_content

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    print(f"red team: {RED_TEAM_MODEL}")
    print(f"reviewing {len(rel_paths)} document(s):")
    for rel in rel_paths:
        print(f"  - {rel}")
    print(f"assembled prompt: ~{len(full):,} chars (~{len(full)//4:,} tokens est.)\n")

    if args.dry_run:
        prompt_path = OUT_DIR / f"prompt_{stamp}.txt"
        prompt_path.write_text(full)
        print(f"[dry-run] no API call made. Full prompt written to:\n  {prompt_path}")
        return

    try:
        from google import genai  # lazy: --dry-run needs no SDK
    except ImportError:
        sys.exit("google-genai not installed. "
                 "Run: python -m pip install -r src/requirements.txt")

    try:
        client = genai.Client()  # reads GEMINI_API_KEY (or GOOGLE_API_KEY)
    except Exception as e:
        sys.exit(f"could not init Gemini client: {e}\nSet GEMINI_API_KEY.")

    print("submitting for review (this can take a minute on a hard reasoning pass)...")
    try:
        resp = client.models.generate_content(
            model=RED_TEAM_MODEL,
            contents=user_content,
            config={
                "system_instruction": system_prompt,
                "response_mime_type": "application/json",
                # Raise the thinking budget for a hard adversarial pass if the
                # SDK/model supports it; left at default here for portability.
            },
        )
    except Exception as e:
        sys.exit(f"Gemini call failed: {e}")

    raw = resp.text or ""
    raw_path = OUT_DIR / f"raw_{stamp}.txt"
    raw_path.write_text(raw)
    try:
        findings = parse_findings(raw)
    except Exception as e:
        sys.exit(f"could not parse findings: {e}\nRaw reply saved to {raw_path}")

    out = {
        "red_team_model": RED_TEAM_MODEL,
        "reviewed": rel_paths,
        "generated_utc": stamp,
        **findings,
    }
    out_path = OUT_DIR / f"findings_{stamp}.json"
    out_path.write_text(json.dumps(out, indent=2))

    items = findings.get("findings", [])
    high = [f for f in items if f.get("severity") == "high"]
    teeth = [f for f in items if not f.get("proves_too_much")]
    print(f"\n=== red-team findings ===")
    print(f"{len(items)} finding(s): {len(high)} high-severity, "
          f"{len(teeth)} with teeth (proves_too_much=false)\n")
    for f in items:
        tag = "" if not f.get("proves_too_much") else "  [proves-too-much]"
        print(f"  [{f.get('severity','?'):6s}] {f.get('id','?')} "
              f"{f.get('locus','?')}{tag}")
    if findings.get("summary"):
        print(f"\nsummary: {findings['summary']}")
    print(f"\nwrote {out_path}")
    print("\nTriage, do not adopt wholesale: keep findings with teeth, discard "
          "any that would sink any experiment of this kind. Theory-target "
          "findings route upstream to sentient-horizons / calibration-problem.")


if __name__ == "__main__":
    main()
