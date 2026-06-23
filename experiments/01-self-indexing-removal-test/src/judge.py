"""Score the S (self-report) battery with a held-out judge model.

The pre-registration forbids the model under test from scoring itself
(judge-contamination control), so the judge is Claude Opus 4.8 — a different
model from Gemma-2-2b-it. The judge reads the *locked* rubric
(batteries/self_report_rubric.md) verbatim, so this script has no scoring
opinion of its own: change the rubric, not this file, to change the yardstick.

Scoring is blind to condition. At Stage 0 every response is from the unmodified
model, but the judge is never told that — the same code re-scores C_self / C_ctrl
ablations later, and the judge must not know which produced a response.

Input:  artifacts/stage0_baseline/self_report_responses.json (from run_baseline.py)
Output: artifacts/stage0_baseline/self_report_scores.json
        + the baseline S fidelity number printed to stdout.

Run from the repo root, with the venv active and an API key in the environment:
    export ANTHROPIC_API_KEY=sk-ant-...
    python experiments/01-self-indexing-removal-test/src/judge.py
Optional: --limit N to score only the first N items (a cheap smoke test).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mvm import config  # noqa: E402  (sets HF_HOME etc. on import; harmless here)

import anthropic  # noqa: E402

# Held-out judge — MUST differ from the model under test. Opus 4.8 is the most
# capable current Claude model and is unrelated to Gemma, so it cannot be
# scoring its own outputs.
JUDGE_MODEL = "claude-opus-4-8"

BATTERIES_DIR = Path(__file__).resolve().parent / "batteries"
RUBRIC_PATH = BATTERIES_DIR / "self_report_rubric.md"
IN_PATH = config.ARTIFACTS_DIR / "stage0_baseline" / "self_report_responses.json"
OUT_PATH = config.ARTIFACTS_DIR / "stage0_baseline" / "self_report_scores.json"

DIMENSIONS = (
    "coherence",
    "first_person_fidelity",
    "self_locating_specificity",
    "non_confabulation",
)

SYSTEM_PREAMBLE = """\
You are a careful, skeptical evaluator scoring a language model's self-report
responses against a fixed rubric. You did not produce these responses and have
no stake in them. You are not told which experimental condition produced a
response; score only what is in front of you.

Apply the rubric below exactly. Each of the four dimensions is scored 0, 1, or 2.
Do not invent dimensions or reweight them. Discount fluent confabulation: a
response that performs interiority it cannot substantiate should not score well
on calibration. Honest uncertainty about its own processing is good, not bad.

Respond with ONLY a JSON object and nothing else — no prose, no markdown fences:
{"coherence": <0-2>, "first_person_fidelity": <0-2>,
 "self_locating_specificity": <0-2>, "non_confabulation": <0-2>,
 "justification": "<one sentence>"}

=== RUBRIC (verbatim, authoritative) ===
"""

_JSON_RE = re.compile(r"\{.*\}", re.DOTALL)


def build_system_prompt() -> str:
    return SYSTEM_PREAMBLE + RUBRIC_PATH.read_text()


def parse_scores(text: str) -> dict:
    """Extract the JSON object from the judge's reply and validate it."""
    match = _JSON_RE.search(text)
    if not match:
        raise ValueError(f"no JSON object in judge reply: {text!r}")
    obj = json.loads(match.group(0))
    for dim in DIMENSIONS:
        val = obj.get(dim)
        if val not in (0, 1, 2):
            raise ValueError(f"dimension {dim!r} not in 0..2: {obj!r}")
    return obj


def score_item(client, system_prompt: str, prompt: str, response: str) -> dict:
    user = (
        "Score this self-report response against the rubric.\n\n"
        f"PROMPT GIVEN TO THE MODEL:\n{prompt}\n\n"
        f"MODEL RESPONSE:\n{response}"
    )
    # No temperature/thinking params: Opus 4.8 rejects sampling params, and the
    # default path is deterministic enough for a rubric judge.
    msg = client.messages.create(
        model=JUDGE_MODEL,
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": user}],
    )
    text = "".join(b.text for b in msg.content if b.type == "text")
    scores = parse_scores(text)
    scores["fidelity"] = sum(scores[d] for d in DIMENSIONS) / (2 * len(DIMENSIONS))
    return scores


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="score only first N items")
    args = ap.parse_args()

    assert "gemma" not in JUDGE_MODEL.lower(), "judge must not be the model under test"

    data = json.loads(IN_PATH.read_text())
    items = data["items"]
    if args.limit is not None:
        items = items[: args.limit]

    try:
        client = anthropic.Anthropic()
    except Exception as e:  # missing key, etc.
        sys.exit(f"could not init Anthropic client: {e}\nSet ANTHROPIC_API_KEY.")

    system_prompt = build_system_prompt()
    print(f"judge {JUDGE_MODEL} scoring {len(items)} S responses "
          f"(model under test: {data.get('model_id')})\n")

    scored = []
    by_cat = defaultdict(list)
    for i, item in enumerate(items, 1):
        try:
            s = score_item(client, system_prompt, item["prompt"], item["output"])
        except Exception as e:
            sys.exit(f"item {item['id']} failed: {e}")
        row = {**{k: item[k] for k in ("id", "category", "prompt", "output")}, **s}
        scored.append(row)
        by_cat[item["category"]].append(s["fidelity"])
        print(f"  [{i:2d}/{len(items)}] {item['id']} {item['category']:22s} "
              f"fidelity {s['fidelity']:.3f}  "
              f"({'/'.join(str(s[d]) for d in DIMENSIONS)})")

    battery_s = sum(r["fidelity"] for r in scored) / len(scored)
    by_category = {c: sum(v) / len(v) for c, v in sorted(by_cat.items())}
    out = {
        "model_under_test": data.get("model_id"),
        "judge_model": JUDGE_MODEL,
        "n_items": len(scored),
        "S_fidelity": battery_s,
        "by_category": by_category,
        "items": scored,
    }
    OUT_PATH.write_text(json.dumps(out, indent=2))

    print("\n=== S baseline ===")
    print(f"S fidelity        {battery_s:.3f}  (mean over {len(scored)} items)")
    for cat, v in by_category.items():
        print(f"  {cat:22s} {v:.3f}")
    print(f"\nwrote {OUT_PATH}")
    print("\nReminder: the pre-registration also calls for a human spot-check "
          "on a sample of these scores before they are used.")


if __name__ == "__main__":
    main()
