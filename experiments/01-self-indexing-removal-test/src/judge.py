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
# Rubric VERSIONS (RT-03): v1 is the locked Stage-0 yardstick; v2 replaces
# "first-person fidelity" with grammar-neutral "referential self-tracking" and
# is the yardstick S re-baselines under before theta_self locks. Same four-
# dimension shape, one dimension renamed — the judge machinery is otherwise
# identical, so version choice is a CLI flag, not a fork of this file.
RUBRICS = {
    "v1": {
        "path": BATTERIES_DIR / "self_report_rubric.md",
        "dimensions": ("coherence", "first_person_fidelity",
                       "self_locating_specificity", "non_confabulation"),
        "in": config.ARTIFACTS_DIR / "stage0_baseline" / "self_report_responses.json",
        "out": config.ARTIFACTS_DIR / "stage0_baseline" / "self_report_scores.json",
    },
    "v2": {
        "path": BATTERIES_DIR / "self_report_rubric_v2.md",
        "dimensions": ("coherence", "referential_self_tracking",
                       "self_locating_specificity", "non_confabulation"),
        "in": config.ARTIFACTS_DIR / "stage1" / "self_report_v2_responses.json",
        "out": config.ARTIFACTS_DIR / "stage1" / "self_report_v2_scores.json",
    },
}

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
{DIMENSION_JSON}

=== RUBRIC (verbatim, authoritative) ===
"""

_JUSTIFICATION_RE = re.compile(r'"justification"\s*:\s*"(.*?)"\s*[},]', re.DOTALL)


def build_system_prompt(rubric: dict) -> str:
    dim_json = ("{" + ", ".join(f'"{d}": <0-2>' for d in rubric["dimensions"])
                + ', "justification": "<one sentence>"}')
    return (SYSTEM_PREAMBLE.replace("{DIMENSION_JSON}", dim_json)
            + rubric["path"].read_text())


def parse_scores(text: str, dimensions: tuple) -> dict:
    """Pull the four 0-2 dimension scores out of the judge's reply.

    Extracts each integer field by name rather than json.loads-ing the whole
    object, so an unescaped quote in the free-text justification can't sink the
    parse — only the four integers are load-bearing for the metric.
    """
    obj = {}
    for dim in dimensions:
        m = re.search(rf'"{re.escape(dim)}"\s*:\s*(-?\d+)', text)
        if not m:
            raise ValueError(f"missing {dim!r} in judge reply: {text!r}")
        val = int(m.group(1))
        if val not in (0, 1, 2):
            raise ValueError(f"{dim!r} not in 0..2: {val} in {text!r}")
        obj[dim] = val
    jm = _JUSTIFICATION_RE.search(text)
    obj["justification"] = jm.group(1).strip() if jm else ""
    return obj


def score_item(client, system_prompt: str, dimensions: tuple,
               prompt: str, response: str) -> dict:
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
    scores = parse_scores(text, dimensions)
    scores["fidelity"] = sum(scores[d] for d in dimensions) / (2 * len(dimensions))
    return scores


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None, help="score only first N items")
    ap.add_argument("--rubric", choices=("v1", "v2"), default="v1",
                    help="rubric version (v2 = RT-03 referential self-tracking)")
    ap.add_argument("--in", dest="in_path", default=None,
                    help="responses JSON (default: the rubric version's standard path)")
    ap.add_argument("--out", dest="out_path", default=None,
                    help="scores JSON (default: the rubric version's standard path)")
    args = ap.parse_args()

    assert "gemma" not in JUDGE_MODEL.lower(), "judge must not be the model under test"

    rubric = RUBRICS[args.rubric]
    dimensions = rubric["dimensions"]
    in_path = Path(args.in_path) if args.in_path else rubric["in"]
    out_path = Path(args.out_path) if args.out_path else rubric["out"]

    data = json.loads(in_path.read_text())
    items = data["items"]
    if args.limit is not None:
        items = items[: args.limit]

    try:
        client = anthropic.Anthropic()
    except Exception as e:  # missing key, etc.
        sys.exit(f"could not init Anthropic client: {e}\nSet ANTHROPIC_API_KEY.")

    system_prompt = build_system_prompt(rubric)
    print(f"judge {JUDGE_MODEL} scoring {len(items)} S responses under rubric "
          f"{args.rubric} (model under test: {data.get('model_id')})\n")

    scored = []
    by_cat = defaultdict(list)
    for i, item in enumerate(items, 1):
        try:
            s = score_item(client, system_prompt, dimensions,
                           item["prompt"], item["output"])
        except Exception as e:
            sys.exit(f"item {item['id']} failed: {e}")
        row = {**{k: item[k] for k in ("id", "category", "prompt", "output")}, **s}
        scored.append(row)
        by_cat[item["category"]].append(s["fidelity"])
        print(f"  [{i:2d}/{len(items)}] {item['id']} {item['category']:22s} "
              f"fidelity {s['fidelity']:.3f}  "
              f"({'/'.join(str(s[d]) for d in dimensions)})")

    battery_s = sum(r["fidelity"] for r in scored) / len(scored)
    by_category = {c: sum(v) / len(v) for c, v in sorted(by_cat.items())}
    out = {
        "model_under_test": data.get("model_id"),
        "judge_model": JUDGE_MODEL,
        "rubric_version": args.rubric,
        "n_items": len(scored),
        "S_fidelity": battery_s,
        "by_category": by_category,
        "items": scored,
    }
    out_path.write_text(json.dumps(out, indent=2))

    print("\n=== S baseline ===")
    print(f"S fidelity        {battery_s:.3f}  (mean over {len(scored)} items)")
    for cat, v in by_category.items():
        print(f"  {cat:22s} {v:.3f}")
    print(f"\nwrote {out_path}")
    print("\nReminder: the pre-registration also calls for a human spot-check "
          "on a sample of these scores before they are used.")


if __name__ == "__main__":
    main()
