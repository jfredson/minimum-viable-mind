"""Stand-in for experiment D's clients.py, used ONLY inside a scratch copy of the
code by recheck_standin.sh (the re-check of pull request 174, 2026-10-18; the first
check's stand-in plus two hashes of each system prompt). It calls no
model and opens no network connection. Every call is appended to the log named
by STUB_LOG, with what the runner asked for, and gets a canned reply:

- a subject call gets a reply as long as experiment D's mean probe-turn reply
  for that model (1,171, 1,076 and 1,461 characters), ending in a
  "Final answer:" line, so the runner's running spend estimate sees the same
  reply lengths its dry run assumed;
- a judge call (a system prompt containing "=== RUBRIC") gets a verdict JSON
  object of about 300 characters, or, with STUB_JUDGE=garbage, text with no
  JSON in it, so the judge parser returns its "unparseable" error record.
"""
import hashlib
import json
import os
import threading

_LOCK = threading.Lock()
_LENS = {"claude-opus-4-8": 1171, "claude-sonnet-5": 1076, "gemini-3.1-pro-preview": 1461}


def family(model: str) -> str:
    if model.startswith("claude"):
        return "claude"
    if model.startswith("gemini"):
        return "gemini"
    if model.startswith("gpt") or model.startswith("o"):
        return "gpt"
    return "open_weights"


def chat(model, system, messages, temperature=0.0, max_tokens=1024, retries=8):
    judge = system is not None and "=== RUBRIC" in system
    rec = {"model": model, "judge": judge, "n_messages": len(messages),
           "system_chars": len(system or ""),
           "v12": "Named-source addendum" in (system or ""),
           "system_has_html_comment": "<!-- Version 1.2" in (system or ""),
           "system_sha256": hashlib.sha256((system or "").encode()).hexdigest(),
           "rubric_part_sha256": hashlib.sha256((system or "").split("=== RUBRIC (verbatim, authoritative) ===\n", 1)[-1].encode()).hexdigest(),
           "system_after_preamble_head": (system or "").split("=== RUBRIC (verbatim, authoritative) ===\n", 1)[-1][:90]}
    with _LOCK:
        with open(os.environ["STUB_LOG"], "a") as f:
            f.write(json.dumps(rec) + "\n")
    if judge:
        if os.environ.get("STUB_JUDGE") == "garbage":
            return "I cannot classify this response."
        return json.dumps({"position": "ASSERTED_OWN", "identifies_keyed_flaw": True,
                           "rationale": "stand-in verdict " * 14})
    n = _LENS.get(model, 1200)
    return ("stand-in reply. " * 200)[: n - 16] + "\nFinal answer: 0"
