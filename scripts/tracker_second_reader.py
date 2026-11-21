#!/usr/bin/env python3
"""Send the blind packets to the second reader (Gemini) and record its raw answers.

Run under John's go of 2026-11-20 ("Yes, up to $10", relayed by the master session),
for the 48 packets in data/tracker/packets/, one standard (not batch) call each.

- Model: gemini-4-carbon. The exact model version the API returns is recorded.
- Spend is tracked after every call from the usage the API reports, at the prices on
  Google's pricing page read 2026-11-20 ($2 per million input tokens, $10 per million
  output tokens including thinking, through 2026-11-30). Before each call the script
  checks that the spend so far plus the most the next call could cost (its input plus
  the output cap) stays within the ceiling, and stops if not.
- Any error stops the run; nothing is retried and no other model or route is tried.
- The key is read from ~/Code/minimum-viable-mind/.env (GEMINI_API_KEY) and is never
  printed, logged or written; error text is scrubbed of it.
- Raw answers go to data/tracker/second-reading/<packet-id>.json. A packet that already
  has an answer is skipped, so the run can resume.

Usage:
    python3 scripts/tracker_second_reader.py --dry-run   # build requests, no calls
    python3 scripts/tracker_second_reader.py --limit 1   # one call
    python3 scripts/tracker_second_reader.py             # the rest
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKETS = ROOT / "data" / "tracker" / "packets"
OUT = ROOT / "data" / "tracker" / "second-reading"
ENV = Path.home() / "Code" / "minimum-viable-mind" / ".env"
MODEL = "gemini-4-carbon"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
PRICE_IN, PRICE_OUT = 2.0, 10.0  # USD per million tokens, through 2026-11-30
CEILING = 10.0
MAX_OUT = 16384


def key():
    for line in ENV.read_text().splitlines():
        if line.startswith("GEMINI_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit("GEMINI_API_KEY not found in .env")


def prompt_for(packet):
    material = {k: v for k, v in packet.items() if k not in ("instructions", "packet_id")}
    return packet["instructions"] + "\n\nThe material:\n" + json.dumps(material, indent=2, ensure_ascii=False)


def cost_of(usage):
    inp = usage.get("promptTokenCount", 0)
    out = usage.get("candidatesTokenCount", 0) + usage.get("thoughtsTokenCount", 0)
    return inp / 1e6 * PRICE_IN + out / 1e6 * PRICE_OUT, inp, out


def spent_so_far():
    total = 0.0
    for f in OUT.glob("*.json"):
        total += json.loads(f.read_text())["cost_usd"]
    return total


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args(argv)
    OUT.mkdir(exist_ok=True)
    packets = sorted(PACKETS.glob("*.json"))
    todo = [p for p in packets if not (OUT / p.name).exists()]
    k = None if a.dry_run else key()
    done = 0
    for p in todo:
        packet = json.loads(p.read_text())
        text = prompt_for(packet)
        body = {
            "contents": [{"role": "user", "parts": [{"text": text}]}],
            "generationConfig": {"responseMimeType": "application/json", "maxOutputTokens": MAX_OUT},
        }
        worst = len(text) / 3 / 1e6 * PRICE_IN + MAX_OUT / 1e6 * PRICE_OUT
        spent = spent_so_far()
        if spent + worst > CEILING:
            print(f"STOP before {p.stem}: spent ${spent:.4f}; the next call could cost up to ${worst:.4f}, past the ${CEILING:.2f} ceiling")
            return 2
        if a.dry_run:
            print(f"would send {p.stem}: {len(text)} characters, worst case ${worst:.4f}")
            continue
        req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST",
                                     headers={"Content-Type": "application/json", "x-goog-api-key": k})
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=600) as r:
                resp = json.loads(r.read())
        except urllib.error.HTTPError as e:
            msg = e.read().decode(errors="replace").replace(k, "[REDACTED]")
            print(f"ERROR on {p.stem}: HTTP {e.code}\n{msg}")
            return 1
        except Exception as e:  # network, timeout
            print(f"ERROR on {p.stem}: {str(e).replace(k, '[REDACTED]')}")
            return 1
        usage = resp.get("usageMetadata", {})
        cost, tin, tout = cost_of(usage)
        cand = (resp.get("candidates") or [{}])[0]
        answer = "".join(part.get("text", "") for part in cand.get("content", {}).get("parts", []) if not part.get("thought"))
        record = {
            "packet_id": p.stem,
            "model_requested": MODEL,
            "model_version": resp.get("modelVersion"),
            "response_id": resp.get("responseId"),
            "finish_reason": cand.get("finishReason"),
            "answer_text": answer,
            "usage": usage,
            "cost_usd": round(cost, 6),
            "seconds": round(time.time() - t0, 1),
            "called_on": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        }
        (OUT / p.name).write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n")
        done += 1
        print(f"{p.stem}: {record['model_version']} {record['finish_reason']} in {tin} out {tout} ${cost:.4f}; total ${spent + cost:.4f}", flush=True)
        if a.limit and done >= a.limit:
            break
    print(f"done; total spent ${spent_so_far():.4f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
