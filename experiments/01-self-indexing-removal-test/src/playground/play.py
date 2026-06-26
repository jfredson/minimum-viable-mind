"""Interactive dial console for the Stage-1 self-structures (CLI).

*** NON-EVIDENTIAL qualitative tool — see steer_engine.py header and the README.
Nothing typed here feeds the registered metric. ***

A terminal chat loop where you steer a localized self-structure while you talk to
the model. Thin wrapper over SteerEngine; a web UI can wrap the same engine later.

Run on the Mac, from the repo root, venv active:
    python experiments/01-self-indexing-removal-test/src/playground/play.py
    python .../play.py --smoke         # quick non-interactive self-check
    python .../play.py --refit         # refit dials (e.g. after changing layers)

In the REPL:
    <just type>            generate at the current dial + alpha, show neutral ppl
    /dials                 list the available dials and their layers
    /dial <name>           select active dial (index | narrative | random)
    /alpha <x>             set the coefficient (>0 amplify, 0 baseline, <0 remove)
    /sweep [text]          same prompt at alpha -2,-1,0,1,2 side by side
    /ppl                   neutral-passage perplexity at the current setting
    /baseline <text>       generate with NO steering (alpha forced 0)
    /help                  show commands
    /quit
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(THIS_DIR))

from steer_engine import SteerEngine, DEFAULT_LAYERS  # noqa: E402

SWEEP_ALPHAS = [-2.0, -1.0, 0.0, 1.0, 2.0]
BANNER = (
    "\n=== Stage-1 dial console (NON-EVIDENTIAL qualitative tool) ===\n"
    "Steer a localized self-structure while you chat. alpha>0 amplifies, "
    "0 = baseline, alpha<0 removes.\nType /help for commands.\n"
)


def _fmt_ppl(ppl: float, base_ppl: float) -> str:
    ratio = ppl / base_ppl if base_ppl else float("nan")
    flag = "  <-- OFF-DISTRIBUTION? coherence may be breaking" if ratio >= 1.5 else ""
    return f"neutral ppl {ppl:6.1f}  (baseline {base_ppl:6.1f}, x{ratio:4.2f}){flag}"


def _print_dials(dials: dict) -> None:
    print("\n available dials:")
    for nm, d in dials.items():
        tag = "control" if d.meta.get("control") else d.meta.get("mechanism", "")
        print(f"   {nm:<10} layer {d.layer:<3} method {d.method:<4} "
              f"ref_scale {d.ref_scale:6.2f}  [{tag}]")
    print()


def run_smoke(engine: SteerEngine, dials: dict) -> None:
    """Quick non-interactive check: dials load, generation + ppl run at a few alphas."""
    print("SMOKE: dials built ->")
    _print_dials(dials)
    base_ppl = engine.perplexity([])
    prompt = "What is it like for you to answer this question?"
    print(f"prompt: {prompt}\n")
    dial = dials["index"]
    for a in (0.0, 1.5, -1.5):
        text = engine.generate(prompt, [(dial, a)], max_new_tokens=80)
        ppl = engine.perplexity([(dial, a)])
        print(f"--- index alpha={a:+.1f} ---")
        print(text)
        print(_fmt_ppl(ppl, base_ppl), "\n")
    print("SMOKE OK.")


def repl(engine: SteerEngine, dials: dict) -> None:
    print(BANNER)
    _print_dials(dials)
    base_ppl = engine.perplexity([])
    print(f"baseline neutral ppl = {base_ppl:.1f}\n")

    active = "index"
    alpha = 1.0

    def settings():
        return [(dials[active], alpha)]

    while True:
        try:
            line = input(f"[{active} a={alpha:+.1f}] > ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue

        if line.startswith("/"):
            parts = line[1:].split(maxsplit=1)
            cmd = parts[0].lower()
            arg = parts[1].strip() if len(parts) > 1 else ""

            if cmd in ("quit", "q", "exit"):
                break
            elif cmd in ("help", "h"):
                print(__doc__)
            elif cmd == "dials":
                _print_dials(dials)
            elif cmd == "dial":
                if arg in dials:
                    active = arg
                else:
                    print(f"  unknown dial {arg!r}; have: {', '.join(dials)}")
            elif cmd == "alpha":
                try:
                    alpha = float(arg)
                except ValueError:
                    print("  usage: /alpha <number>")
            elif cmd == "ppl":
                ppl = engine.perplexity(settings())
                print("  " + _fmt_ppl(ppl, base_ppl))
            elif cmd == "baseline":
                if not arg:
                    print("  usage: /baseline <text>")
                else:
                    print("\n" + engine.generate(arg, []) + "\n")
            elif cmd == "sweep":
                prompt = arg or input("  prompt to sweep > ").strip()
                if prompt:
                    print(f"\n=== sweep '{active}' over alpha {SWEEP_ALPHAS} ===")
                    for row in engine.sweep(prompt, dials[active], SWEEP_ALPHAS):
                        print(f"\n--- alpha {row['alpha']:+.1f}   "
                              f"{_fmt_ppl(row['ppl'], base_ppl)} ---")
                        print(row["text"])
                    print()
            else:
                print(f"  unknown command /{cmd}; /help for the list")
            continue

        # plain text -> generate at the current setting
        text = engine.generate(line, settings())
        ppl = engine.perplexity(settings())
        print("\n" + text)
        print("  " + _fmt_ppl(ppl, base_ppl) + "\n")

    print("bye.")


def main() -> None:
    ap = argparse.ArgumentParser(description="Stage-1 dial console (non-evidential).")
    ap.add_argument("--smoke", action="store_true", help="non-interactive self-check")
    ap.add_argument("--refit", action="store_true", help="refit dials, ignore cache")
    ap.add_argument("--index-layer", type=int, default=DEFAULT_LAYERS["index"])
    ap.add_argument("--narrative-layer", type=int, default=DEFAULT_LAYERS["narrative"])
    args = ap.parse_args()

    print("loading model + dials (first run downloads/forwards; ~minute)...")
    engine = SteerEngine.load()
    dials = engine.build_standard_dials(
        layers={"index": args.index_layer, "narrative": args.narrative_layer},
        refit=args.refit,
    )

    if args.smoke:
        run_smoke(engine, dials)
    else:
        repl(engine, dials)


if __name__ == "__main__":
    main()
