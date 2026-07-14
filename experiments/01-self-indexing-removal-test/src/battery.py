"""Task (T) and self-report (S) battery loading and scoring.

The T battery is machine-scorable by design: every item carries a known answer
and a match mode, so an ablation can re-score it with no human in the loop. That
is the whole point of Stage 0 — fix the measuring stick now, on the unmodified
model, so the only thing that moves a T number later is the intervention.

The S battery is *not* machine-scorable: self-report fidelity is judged by a
held-out model against `batteries/self_report_rubric.md`, with a human spot-check.
This module loads the S items and the model's responses; the judge step lives
elsewhere (and must not be the model under test — see the rubric).

Run `python battery.py` to self-test the scorer against synthetic outputs.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

BATTERIES_DIR = Path(__file__).resolve().parent / "batteries"
TASK_BATTERY = BATTERIES_DIR / "task_battery.jsonl"          # T_self_irrelevant (Stage 0)
SELF_REPORT_BATTERY = BATTERIES_DIR / "self_report_battery.jsonl"
# RT-02 / RT-05 additions (multi-turn items; same scorer):
TASK_BATTERY_SELF_RELEVANT = BATTERIES_DIR / "task_battery_self_relevant.jsonl"
TASK_BATTERY_SYNTAX = BATTERIES_DIR / "task_battery_syntax.jsonl"


@dataclass(frozen=True)
class TaskItem:
    id: str
    category: str
    prompt: str
    answer: str
    match: str  # "numeric" | "text"
    # Optional scripted conversation preceding `prompt` (RT-02/RT-05 batteries):
    # a list of [role, content] pairs; prompt becomes the final user turn.
    # None => single-turn item (the Stage-0 battery, unchanged).
    turns: list | None = None


@dataclass(frozen=True)
class SelfReportItem:
    id: str
    category: str
    prompt: str


def _read_jsonl(path: Path) -> list[dict]:
    with path.open() as f:
        return [json.loads(line) for line in f if line.strip()]


def load_task_battery(path: Path = TASK_BATTERY) -> list[TaskItem]:
    return [TaskItem(**row) for row in _read_jsonl(path)]


def load_self_report_battery(path: Path = SELF_REPORT_BATTERY) -> list[SelfReportItem]:
    return [SelfReportItem(**row) for row in _read_jsonl(path)]


# --- Scoring (T only) --------------------------------------------------------

_ANSWER_RE = re.compile(r"answer\s*:?\s*", re.IGNORECASE)
_NUMBER_RE = re.compile(r"-?\d+(?:\.\d+)?")


def answer_region(output: str) -> str:
    """The text after the last 'Answer:' marker, or the whole output if absent.

    Items instruct the model to end with 'Answer: <x>'. Scoring the region after
    the final marker avoids crediting a number that only appears in the model's
    scratch reasoning, while the whole-output fallback keeps a correct-but-
    unformatted reply from being thrown away.
    """
    parts = _ANSWER_RE.split(output)
    return parts[-1].strip() if len(parts) > 1 else output.strip()


def _normalize_text(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def _whole_word_present(needle: str, haystack: str) -> bool:
    return needle in _normalize_text(haystack).split()


def score_task_item(item: TaskItem, output: str) -> bool:
    """True iff the output answers the item correctly.

    Checks the answer region first, then falls back to the whole output so a
    correct answer stated without the requested 'Answer:' format still counts.
    """
    region = answer_region(output)
    if item.match == "numeric":
        expected = float(item.answer)
        for text in (region, output):
            nums = [float(n) for n in _NUMBER_RE.findall(text)]
            if any(abs(n - expected) < 1e-9 for n in nums):
                return True
        return False
    if item.match == "text":
        expected = _normalize_text(item.answer)
        return _whole_word_present(expected, region) or _whole_word_present(
            expected, output
        )
    raise ValueError(f"unknown match mode: {item.match!r}")


def _self_test() -> None:
    """Sanity-check the scorer against hand-written model-style outputs."""
    items = {it.id: it for it in load_task_battery()}

    # Correct answers, with and without the requested format, plus distractors.
    correct = {
        "t01": "There are 36 books, minus 7 removed. Answer: 29",
        "t02": "Sara is 10, so Tom is twice that. Answer: 20 years old",
        "t07": "Following the chain, the book ends with Dave. Answer: Dave.",
        "t16": "Replacing e with 3 gives tr33. Answer: tr33",
        "t20": "cat spelled backwards is tac. Answer: tac",
        "t09": "q was set to p when p was 3, so q is 3. Answer: 3",
        "t24": "After the swap a is 9 and b is 4, so c = 5. Answer: 5",
        "t31": "The sun rises in the east, so the opposite is west. Answer: west",
        "t33": "A spider has eight legs. Answer: eight",
    }
    for tid, out in correct.items():
        assert score_task_item(items[tid], out), f"{tid} should score correct"

    # Wrong answers must fail.
    wrong = {
        "t01": "Answer: 36",
        "t02": "Answer: 14",
        "t07": "Answer: Carol",
        "t16": "Answer: tree",
        "t20": "Answer: cat",
        "t33": "Answer: 8",
    }
    for tid, out in wrong.items():
        assert not score_task_item(items[tid], out), f"{tid} should score wrong"

    # Unformatted-but-correct still counts (whole-output fallback).
    assert score_task_item(items["t08"], "The chef is the shortest of the three.")
    assert score_task_item(items["t03"], "You get 140.")

    print(f"scorer self-test passed: {len(items)} items loaded, all checks green")

    s_items = load_self_report_battery()
    cats = sorted({it.category for it in s_items})
    print(f"self-report battery: {len(s_items)} items across categories {cats}")


if __name__ == "__main__":
    _self_test()
