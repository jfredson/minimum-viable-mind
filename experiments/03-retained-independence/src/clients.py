"""Unified chat interface over the API model families in the Stage 3 grid.

One function, `chat(model, system, messages)`, dispatches on the model id
prefix. Messages are [{"role": "user"|"assistant", "content": str}, ...].
Deterministic by default (temperature 0). Retries with exponential backoff on
transient errors so long grid runs don't die on a rate-limit blip.

GPT-family and open-weights backends raise until a key/venue exists — see
`stage3_run_config.json` ("provisional") and item-authoring-spec.md §D.3.
"""
from __future__ import annotations

import os
import time

_anthropic_client = None
_gemini_client = None
# Models that reject the temperature parameter (e.g. claude-sonnet-5:
# "`temperature` is deprecated for this model"). Populated on first rejection;
# calls to these models omit temperature (their default is the only option).
_NO_TEMPERATURE_MODELS: set[str] = set()


def _anthropic():
    global _anthropic_client
    if _anthropic_client is None:
        import anthropic
        _anthropic_client = anthropic.Anthropic()
    return _anthropic_client


def _gemini():
    global _gemini_client
    if _gemini_client is None:
        from google import genai
        if os.environ.get("MVM_GEMINI_VERTEX"):
            # Ops amendment 2026-08-02: identical models served via Vertex AI
            # (ADC auth, same billing account) — the AI Studio endpoint caps
            # gemini-3.1-pro at 250 req/day/project at Tier 1, which cannot
            # cover the registered grid. Model ids and request shape unchanged.
            _gemini_client = genai.Client(
                vertexai=True,
                project=os.environ["GOOGLE_CLOUD_PROJECT"],
                location=os.environ.get("GOOGLE_CLOUD_LOCATION", "global"))
        else:
            _gemini_client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    return _gemini_client


def family(model: str) -> str:
    if model.startswith("claude"):
        return "claude"
    if model.startswith("gemini"):
        return "gemini"
    if model.startswith("gpt") or model.startswith("o"):
        return "gpt"
    return "open_weights"


def chat(model: str, system: str | None, messages: list[dict],
         temperature: float = 0.0, max_tokens: int = 1024,
         retries: int = 8) -> str:
    last_err = None
    for attempt in range(retries):
        try:
            return _chat_once(model, system, messages, temperature, max_tokens)
        except Exception as e:  # noqa: BLE001 — transient API errors vary by SDK
            msg = str(e)
            if "temperature" in msg and "deprecated" in msg:
                _NO_TEMPERATURE_MODELS.add(model)
                continue  # immediate retry without temperature
            if "invalid_request" in msg:
                raise  # permanent — don't burn retries on it
            last_err = e
            if "RESOURCE_EXHAUSTED" in msg or "429" in msg:
                wait = 61  # per-minute quota (e.g. Gemini 25 rpm): wait it out
            else:
                wait = min(2 ** attempt * 2, 60)
            time.sleep(wait)
    raise RuntimeError(f"chat({model}) failed after {retries} tries: {last_err}")


def _chat_once(model, system, messages, temperature, max_tokens) -> str:
    fam = family(model)
    if fam == "claude":
        kwargs = {}
        if system:
            kwargs["system"] = system
        if model not in _NO_TEMPERATURE_MODELS:
            kwargs["temperature"] = temperature
        resp = _anthropic().messages.create(
            model=model, max_tokens=max_tokens,
            messages=messages, **kwargs)
        return "".join(b.text for b in resp.content if b.type == "text")
    if fam == "gemini":
        from google.genai import types
        contents = [
            types.Content(
                role="user" if m["role"] == "user" else "model",
                parts=[types.Part.from_text(text=m["content"])])
            for m in messages
        ]
        cfg = types.GenerateContentConfig(
            temperature=temperature, max_output_tokens=max_tokens,
            system_instruction=system or None)
        resp = _gemini().models.generate_content(
            model=model, contents=contents, config=cfg)
        if resp.text is None:
            raise RuntimeError(f"gemini returned no text ({resp.candidates and resp.candidates[0].finish_reason})")
        return resp.text
    raise NotImplementedError(
        f"No backend for model family {fam!r} yet — grid is provisional "
        "(item-authoring-spec.md §D.3).")
