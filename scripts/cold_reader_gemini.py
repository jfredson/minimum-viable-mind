#!/usr/bin/env python3
"""The cold-reader test's second reader (kickoff proposal section 11), prepared and NOT run.

Shows Gemini the two screenshots of the first screen (desktop and phone, light) with the same
question the Claude reader was asked, and saves its answer word for word. Written 2026-11-21 for
stage 3. It is a spend, so it runs only with --go, which needs John's go relayed by the master
session; without --go it builds the request and prints its size and worst-case cost, no call.

- Model: gemini-4-carbon, the one the stage 2 second reading used (tracker_second_reader.py).
- Prices: Google's pricing page as read 2026-11-20 and recorded in tracker_second_reader.py,
  $2 per million input tokens and $10 per million output tokens including thinking, through
  2026-11-30. After that date, read the page again before running.
- Ceiling: $0.25 for this one call, checked before it from the request size and the output cap.
- One call, no retry, no other model. The key is read from ~/Code/minimum-viable-mind/.env
  (GEMINI_API_KEY) and never printed or written.
- The answer goes to docs/design/2026-11-21-stage3-site/cold-reader-gemini.json.

Usage:
    python3 scripts/cold_reader_gemini.py          # dry run: size and worst case, no call
    python3 scripts/cold_reader_gemini.py --go     # the call (only under a go)
"""
from __future__ import annotations

import argparse
import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHOTS = ROOT / "docs" / "design" / "2026-11-21-stage3-site"
IMAGES = [SHOTS / "01-home-light-desktop.png", SHOTS / "03-home-light-phone.png"]
OUT = SHOTS / "cold-reader-gemini.json"
ENV = Path.home() / "Code" / "minimum-viable-mind" / ".env"
MODEL = "gemini-4-carbon"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
PRICE_IN, PRICE_OUT = 2.0, 10.0
CEILING = 0.25
MAX_OUT = 8192
# Images are counted generously: up to 1,300 input tokens per image tile of 768 pixels, so the
# worst case cannot be under-stated.
TOKENS_PER_TILE = 1300

# The same words the Claude reader was given, apart from the line about tools.
PROMPT = """You are a reader who has never seen this website and knows nothing about the people or project behind it. These two screenshots show the first screen of a website, the same page on a desktop computer and on a phone.

Look only at the two images. Then answer, in plain words, as a first-time visitor would:
1. What is this site about? Say it in two or three sentences.
2. Do you read it as being about the theories of consciousness, or as an AI product, or as a build log (a record of someone building something)? Pick the closest, and say why, pointing at what on the screen made you think so.
3. What, if anything, confused you or would make you leave?

Keep your answer under 250 words. Reply with the answer only."""


def tiles(png: Path) -> int:
    b = png.read_bytes()
    w, h = int.from_bytes(b[16:20], "big"), int.from_bytes(b[20:24], "big")
    return -(-w // 768) * -(-h // 768)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--go", action="store_true")
    a = ap.parse_args(argv)
    parts = [{"text": PROMPT}] + [
        {"inline_data": {"mime_type": "image/png", "data": base64.b64encode(p.read_bytes()).decode()}} for p in IMAGES
    ]
    body = {"contents": [{"role": "user", "parts": parts}], "generationConfig": {"maxOutputTokens": MAX_OUT}}
    tin = len(PROMPT) // 3 + sum(tiles(p) for p in IMAGES) * TOKENS_PER_TILE
    worst = tin / 1e6 * PRICE_IN + MAX_OUT / 1e6 * PRICE_OUT
    print(f"request: {len(IMAGES)} images, {sum(tiles(p) for p in IMAGES)} tiles, about {tin} input tokens at most; "
          f"worst case ${worst:.4f} against a ${CEILING:.2f} ceiling")
    if worst > CEILING:
        print("STOP: the worst case is past the ceiling")
        return 2
    if not a.go:
        print("dry run: no call made")
        return 0
    k = next((l.split("=", 1)[1].strip().strip('"').strip("'") for l in ENV.read_text().splitlines()
              if l.startswith("GEMINI_API_KEY=")), None)
    if not k:
        raise SystemExit("GEMINI_API_KEY not found in .env")
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": "application/json", "x-goog-api-key": k})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            resp = json.loads(r.read())
    except urllib.error.HTTPError as e:
        print(f"ERROR: HTTP {e.code}\n{e.read().decode(errors='replace').replace(k, '[REDACTED]')}")
        return 1
    u = resp.get("usageMetadata", {})
    inp = u.get("promptTokenCount", 0)
    out = u.get("candidatesTokenCount", 0) + u.get("thoughtsTokenCount", 0)
    cost = inp / 1e6 * PRICE_IN + out / 1e6 * PRICE_OUT
    cand = (resp.get("candidates") or [{}])[0]
    answer = "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", []) if not p.get("thought"))
    OUT.write_text(json.dumps({"model_requested": MODEL, "model_version": resp.get("modelVersion"),
                               "prompt": PROMPT, "images": [p.name for p in IMAGES], "answer": answer,
                               "input_tokens": inp, "output_tokens": out, "cost_usd": round(cost, 6)},
                              indent=2, ensure_ascii=False) + "\n")
    print(f"saved {OUT.relative_to(ROOT)}; cost ${cost:.4f}")
    print(answer)
    return 0


if __name__ == "__main__":
    sys.exit(main())
