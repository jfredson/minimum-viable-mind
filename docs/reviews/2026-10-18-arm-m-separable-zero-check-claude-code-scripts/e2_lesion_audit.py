"""E2: watch D5, D7 and D9 as they run, and check their in-memory lesion.

Wraps, in this process only, the two places the frozen models read the acting
channel (`_Shared._own_vec`, the built-in answer; `Arm._embed` and
`MiddleArm._embed`, the trunk's input) so that every forward pass records how
many acting flags each of the two saw, and whether `_own_vec` was overridden on
the instance at the time. Then runs each script unchanged (runpy) and checks:

  - in every pass where the trunk saw no acting flags but the built-in answer
    did (the trunk-only lesion), the instance override was in place, and the
    built-in answer read the same number of flags as the real chunk (24 per
    episode);
  - in every other pass, no override was in place (so it was put back);
  - after the script, no model object still carries the override;
  - the script's printed output is identical to its committed output file.

The wrapping only records; it calls the original methods and returns their
results unchanged. No file of the frozen code changes."""
import contextlib
import io
import os
import runpy
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.abspath(os.path.join(HERE, "..", "..", "2026-10-18-arm-m-separable-zero-scripts"))
sys.path.insert(0, SCRIPTS)
os.chdir(SCRIPTS)
import common                     # noqa: E402
M = common.M

EVENTS = []
MODELS = []
_orig_own = M._Shared._own_vec
_orig_embed = {cls: cls._embed for cls in (M.Arm, M.MiddleArm)}


def own_vec(self, b):
    EVENTS.append(("own", int(b["acting"].sum()), int(b["acting"].shape[0])))
    return _orig_own(self, b)


def make_embed(cls):
    def embed(self, b, own_vec):
        if self not in MODELS:
            MODELS.append(self)
        EVENTS.append(("embed", int(b["acting"].sum()), "_own_vec" in self.__dict__))
        return _orig_embed[cls](self, b, own_vec)
    return embed


M._Shared._own_vec = own_vec
for cls in _orig_embed:
    cls._embed = make_embed(cls)

for script in ("d5_trunk_lesion", "d7_flat_choice", "d9_stirred_in_items"):
    EVENTS.clear(); MODELS.clear()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        runpy.run_path(os.path.join(SCRIPTS, script + ".py"), run_name="__main__")
    passes = {"normal": 0, "trunk-only lesion": 0, "acting zeroed everywhere": 0}
    bad = []
    i = 0
    while i < len(EVENTS):
        own, emb = EVENTS[i], EVENTS[i + 1]
        assert own[0] == "own" and emb[0] == "embed", (i, own, emb)
        own_flags, n_ep, emb_flags, override = own[1], own[2], emb[1], emb[2]
        if emb_flags == 0 and own_flags > 0:
            passes["trunk-only lesion"] += 1
            if not override or own_flags != 24 * n_ep:
                bad.append((i, own, emb))
        else:
            passes["normal" if emb_flags == own_flags == 24 * n_ep else "acting zeroed everywhere"] += 1
            if override or emb_flags != own_flags:
                bad.append((i, own, emb))
        i += 2
    left = sum("_own_vec" in m.__dict__ for m in MODELS)
    committed = open(os.path.join(SCRIPTS, script + "_output.txt")).read()
    print(f"{script}: forward passes {sum(passes.values())}: {passes}")
    print(f"  passes that break the rule above: {len(bad)}; models still carrying the override after the run: {left} of {len(MODELS)}")
    print(f"  printed output identical to the committed {script}_output.txt: {buf.getvalue() == committed}")
