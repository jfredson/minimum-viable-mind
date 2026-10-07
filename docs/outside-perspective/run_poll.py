#!/usr/bin/env python3
"""Run the outside-model poll on the brief, by API, and save every reply as the record.

What it does, per model family (Gemini, OpenAI, Anthropic), in one conversation each:
  round one: the round-one paste file + the book's argument summary -> saved
  round two: the round-two paste file, in the same conversation         -> saved
Each reply is written word for word to replies/<date>-<family>-round-<n>.md.
A manifest (replies/<date>-manifest.json) records the exact model id, the
version the provider reports, timestamps, token usage and the SHA-256 of
every input, so a later session can check what was sent and what came back.

Keys are read at run time and never printed or written anywhere:
  GEMINI_API_KEY and ANTHROPIC_API_KEY from the environment, falling back to
  the repository's gitignored .env and then the shell start-up files; OPENAI_API_KEY from
  ~/Documents/.agi-zeitgeist/credentials.env (the same file the AGI Zeitgeist
  cross-family script reads).

Usage, from the repository root:
  .venv/bin/python docs/outside-perspective/run_poll.py [--families gemini,openai,anthropic] [--dry-run]
A --dry-run assembles the inputs, checks each key and model, writes the
manifest's input section and sends nothing.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import time
import traceback
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ROUND_ONE = HERE / "PASTE-round-one.md"
ROUND_TWO = HERE / "PASTE-round-two.md"
BOOK_SUMMARY = Path.home() / "Code" / "calibration-problem" / "editorial" / "argument-summary-2026-10-07.md"
OUT = HERE / "replies"

MODELS = {
    "gemini": "gemini-3.1-pro-preview",
    "openai": "gpt-6-astra",
    "anthropic": "claude-opus-5-5",
}
MAX_OUTPUT_TOKENS = 16000
RETRY_WAITS = (0, 60, 180)

ROUND_ONE_PREFACE = (
    "Below are two documents. The first is a brief addressed to you. The second is a "
    "summary of the book the brief refers to, written as background. Read both, then "
    "answer the brief's questions as it asks: disagree where you disagree, say how "
    "confident you are, and do not soften things to be polite.\n\n"
)
SEPARATOR = "\n\n" + ("=" * 72) + "\n\nTHE BOOK SUMMARY\n\n"


# ----------------------------------------------------------------- keys
def _from_rc(name: str) -> str | None:
    pat = re.compile(r"^\s*(?:export\s+)?" + re.escape(name) + r"=(.+?)\s*$")
    for rc in (".zshenv", ".zshrc", ".zprofile", ".bash_profile", ".profile"):
        p = Path.home() / rc
        if not p.exists():
            continue
        for line in p.read_text(errors="ignore").splitlines():
            m = pat.match(line)
            if m:
                return m.group(1).strip().strip('"').strip("'")
    return None


def _from_repo_env(name: str) -> str | None:
    """The repository's gitignored .env, where STATUS.md says the Anthropic key lives."""
    p = ROOT / ".env"
    if not p.exists():
        return None
    for line in p.read_text(errors="ignore").splitlines():
        if line.strip().startswith(name + "="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def key_env(name: str) -> str:
    v = os.environ.get(name) or _from_repo_env(name) or _from_rc(name)
    if not v:
        raise SystemExit(f"stopped: {name} not found in the environment, the repository .env, or the shell start-up files")
    return v


def key_openai() -> str:
    path = Path.home() / "Documents" / ".agi-zeitgeist" / "credentials.env"
    if not path.exists():
        raise SystemExit("stopped: the OpenAI credentials file is not where the Zeitgeist script reads it")
    for line in path.read_text().splitlines():
        if line.startswith("OPENAI_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("stopped: OPENAI_API_KEY not found in the credentials file")


# ----------------------------------------------------------------- inputs
def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def load_inputs() -> dict:
    for p in (ROUND_ONE, ROUND_TWO, BOOK_SUMMARY):
        if not p.exists():
            raise SystemExit(f"stopped: missing input {p}")
    r1 = ROUND_ONE.read_text()
    r2 = ROUND_TWO.read_text()
    book = BOOK_SUMMARY.read_text()
    round_one_message = ROUND_ONE_PREFACE + r1 + SEPARATOR + book
    round_two_message = (
        "Thank you. Here is the second round, from the same author. Please read it and "
        "answer its question at the end: which of the two readings does your first "
        "answer support, and did anything in it change on seeing these, and on seeing "
        "the two Claude sessions' views?\n\n" + r2
    )
    return {
        "round_one_message": round_one_message,
        "round_two_message": round_two_message,
        "inputs": {
            "round_one_paste": {"path": str(ROUND_ONE.relative_to(ROOT)), "sha256": sha(r1), "words": len(r1.split())},
            "round_two_paste": {"path": str(ROUND_TWO.relative_to(ROOT)), "sha256": sha(r2), "words": len(r2.split())},
            "book_summary": {"path": str(BOOK_SUMMARY), "sha256": sha(book), "words": len(book.split())},
            "round_one_message_sha256": sha(round_one_message),
            "round_two_message_sha256": sha(round_two_message),
        },
    }


# ----------------------------------------------------------------- http helper
def http_json(req: urllib.request.Request, timeout: int = 900) -> dict:
    last = ""
    for wait in RETRY_WAITS:
        if wait:
            time.sleep(wait)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "ignore")[:300]
            if e.code in (429, 500, 502, 503, 529):
                last = f"HTTP {e.code}: {body}"
                continue
            raise RuntimeError(f"HTTP {e.code}: {body}")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            last = f"connection problem: {e}"
            continue
    raise RuntimeError(f"kept refusing or timing out after back-offs (last: {last})")


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ----------------------------------------------------------------- families
class Gemini:
    family = "gemini"

    def __init__(self, dry: bool):
        from google import genai  # installed in the repo environment
        self.genai = genai
        self.client = genai.Client(api_key=key_env("GEMINI_API_KEY"))
        self.model = MODELS["gemini"]
        info = self.client.models.get(model=self.model)
        self.version = getattr(info, "version", None)
        self.chat = None if dry else self.client.chats.create(model=self.model)

    def send(self, text: str) -> tuple[str, dict]:
        last = None
        for wait in RETRY_WAITS:
            if wait:
                time.sleep(wait)
            try:
                resp = self.chat.send_message(text)
                parts = resp.candidates[0].content.parts
                out = "".join((p.text or "") for p in parts if not getattr(p, "thought", False))
                um = resp.usage_metadata
                usage = {"input_tokens": getattr(um, "prompt_token_count", None),
                         "output_tokens": getattr(um, "candidates_token_count", None),
                         "thinking_tokens": getattr(um, "thoughts_token_count", None)}
                return out, usage
            except Exception as e:  # rate limits and transient faults
                last = e
                if "429" in str(e) or "503" in str(e) or "500" in str(e):
                    continue
                raise
        raise RuntimeError(f"Gemini kept failing: {last}")


class OpenAI:
    family = "openai"

    def __init__(self, dry: bool):
        self.key = key_openai()
        self.model = MODELS["openai"]
        req = urllib.request.Request(f"https://api.openai.com/v1/models/{self.model}",
                                     headers={"Authorization": f"Bearer {self.key}"})
        self.version = http_json(req, timeout=60).get("created")
        self.previous_id = None

    def send(self, text: str) -> tuple[str, dict]:
        body = {"model": self.model,
                "input": [{"role": "user", "content": [{"type": "input_text", "text": text}]}],
                "reasoning": {"effort": "high"},
                "max_output_tokens": MAX_OUTPUT_TOKENS}
        if self.previous_id:
            body["previous_response_id"] = self.previous_id
        req = urllib.request.Request("https://api.openai.com/v1/responses", data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json",
                                              "Authorization": f"Bearer {self.key}"})
        data = http_json(req)
        self.previous_id = data.get("id")
        out = "".join(c.get("text", "") for o in data.get("output", []) if o.get("type") == "message"
                      for c in o.get("content", []) if c.get("type") == "output_text")
        u = data.get("usage", {}) or {}
        usage = {"input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
                 "reasoning_tokens": (u.get("output_tokens_details") or {}).get("reasoning_tokens"),
                 "status": data.get("status"), "response_id": data.get("id")}
        return out, usage


class Anthropic:
    family = "anthropic"

    def __init__(self, dry: bool):
        import anthropic
        # Use John's own key against the public endpoint, not any gateway set in this shell.
        os.environ.pop("ANTHROPIC_BASE_URL", None)
        self.client = anthropic.Anthropic(api_key=key_env("ANTHROPIC_API_KEY"))
        self.model = MODELS["anthropic"]
        info = self.client.models.retrieve(self.model)
        self.version = getattr(info, "created_at", None)
        self.version = str(self.version) if self.version else None
        self.history: list[dict] = []

    def send(self, text: str) -> tuple[str, dict]:
        self.history.append({"role": "user", "content": text})
        last = None
        for wait in RETRY_WAITS:
            if wait:
                time.sleep(wait)
            try:
                resp = self.client.messages.create(model=self.model, max_tokens=MAX_OUTPUT_TOKENS,
                                                   messages=self.history)
                break
            except Exception as e:
                last = e
                name = type(e).__name__
                if name in ("RateLimitError", "InternalServerError", "APIConnectionError", "OverloadedError"):
                    continue
                raise
        else:
            raise RuntimeError(f"Anthropic kept failing: {last}")
        out = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
        self.history.append({"role": "assistant", "content": out})
        usage = {"input_tokens": resp.usage.input_tokens, "output_tokens": resp.usage.output_tokens,
                 "stop_reason": resp.stop_reason}
        return out, usage


FAMILIES = {"gemini": Gemini, "openai": OpenAI, "anthropic": Anthropic}


# ----------------------------------------------------------------- run
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--families", default="gemini,openai,anthropic")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--date", default=dt.date.today().isoformat())
    args = ap.parse_args()
    families = [f.strip() for f in args.families.split(",") if f.strip()]
    for f in families:
        if f not in FAMILIES:
            raise SystemExit(f"stopped: unknown family {f!r}")

    OUT.mkdir(exist_ok=True)
    manifest_path = OUT / f"{args.date}-manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    data = load_inputs()
    manifest["inputs"] = data["inputs"]
    manifest.setdefault("runs", {})
    manifest["script"] = str(Path(__file__).resolve().relative_to(ROOT))

    def save():
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")

    print(f"inputs: round one {data['inputs']['round_one_paste']['words']} words + book summary "
          f"{data['inputs']['book_summary']['words']} words; round two {data['inputs']['round_two_paste']['words']} words")
    save()

    for fam in families:
        run = manifest["runs"].setdefault(fam, {})
        try:
            client = FAMILIES[fam](args.dry_run)
        except SystemExit as e:
            print(f"[{fam}] {e}")
            run["error"] = str(e)
            save()
            continue
        except Exception as e:
            print(f"[{fam}] could not set up: {type(e).__name__}: {str(e)[:200]}")
            run["error"] = f"setup: {type(e).__name__}: {str(e)[:300]}"
            save()
            continue
        run.update({"model": client.model, "provider_version": client.version})
        print(f"[{fam}] model {client.model}, provider version {client.version}")
        save()
        if args.dry_run:
            continue
        for n, text in (("one", data["round_one_message"]), ("two", data["round_two_message"])):
            if run.get(f"round_{n}", {}).get("saved"):
                print(f"[{fam}] round {n} already saved; skipping")
                continue
            started = now()
            try:
                reply, usage = client.send(text)
            except Exception as e:
                run[f"round_{n}"] = {"started": started, "error": f"{type(e).__name__}: {str(e)[:400]}"}
                print(f"[{fam}] round {n} FAILED: {type(e).__name__}: {str(e)[:200]}")
                traceback.print_exc(limit=1)
                save()
                break
            path = OUT / f"{args.date}-{fam}-round-{n}.md"
            header = (f"# Round {n} reply: {client.model}\n\n*Saved word for word by `{manifest['script']}` on "
                      f"{args.date}. Provider version {client.version}. Started {started}, finished {now()} UTC. "
                      f"Usage: {json.dumps(usage)}. Input SHA-256 "
                      f"{data['inputs'][f'round_{n}_message_sha256']}.*\n\n---\n\n")
            path.write_text(header + reply.strip() + "\n")
            run[f"round_{n}"] = {"started": started, "finished": now(), "usage": usage,
                                 "saved": str(path.relative_to(ROOT)), "words": len(reply.split())}
            print(f"[{fam}] round {n} saved: {path.name} ({len(reply.split())} words)")
            save()
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
