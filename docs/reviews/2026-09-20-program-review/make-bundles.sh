#!/usr/bin/env bash
# Builds the three review bundles for docs/reviews/2026-09-20-program-review/
# from the committed repository files, verbatim. Run from the repo root:
#   cd ~/Code/minimum-viable-mind && bash docs/reviews/2026-09-20-program-review/make-bundles.sh
# Re-running overwrites the bundles and the two cover prompts; it never edits a source file.
set -euo pipefail

OUT="docs/reviews/2026-09-20-program-review"
E06="experiments/06-mvm-0a-constructed-self-index"

emit() {  # emit <bundle-file> <repo-path>...
  local bundle="$1"; shift
  for f in "$@"; do
    if [ ! -f "$f" ]; then echo "MISSING: $f" >&2; exit 1; fi
    { printf '\n\n===== FILE: %s =====\n\n' "$f"; cat "$f"; } >> "$bundle"
  done
}

status_current() {  # the current-state sections of STATUS.md (everything above the first entry older than 2026-09-19) plus "The arc"
  awk '
    /^## / { n++ }
    n <= 3 { print; next }
    /^## The arc/ { arc=1 }
    arc && /^## 2026-09-15/ { arc=0 }
    arc { print }
  ' STATUS.md
}

# ---------- bundle 1: design ----------
B1="$OUT/bundle-1-design.md"
cat > "$B1" <<'EOF'
# Bundle 1 of 3: what the program set out to do

Verbatim concatenation of committed repository files, built by make-bundles.sh on the date in the file list below. Nothing is edited or abridged. Each file begins with `===== FILE: <path> =====`.

Contents, in order:
1. README.md (repo front page)
2. spec/minimum-viable-mind-proposal-v0.1.md (the founding specification)
3. spec/theory-instrument-ledger.md (which theory each stage adjudicates)
4. spec/corrigibility-commitments.md
5. experiments/README.md (the experiment ladder)
6. ROADMAP.md and ROADMAP-post-removal-test.md
7. experiments/01-self-indexing-removal-test/pre-registration.md
8. experiments/03-retained-independence/pre-registration.md
9. experiments/06-mvm-0a-constructed-self-index/pre-registration.md (MVM-0a, with Amendments A1 and A2)
10. experiments/06-mvm-0a-constructed-self-index/amendment-a3.md (Amendment A3, registered 2026-09-15, with its 2026-09-16 annotation)
11. experiments/06-mvm-0a-constructed-self-index/control-learnability-pilot.md (the pre-statement for the unregistered pilot)
12. docs/public-path-roadmap-2026-09-16.md
EOF
emit "$B1" README.md spec/minimum-viable-mind-proposal-v0.1.md spec/theory-instrument-ledger.md spec/corrigibility-commitments.md \
  experiments/README.md ROADMAP.md ROADMAP-post-removal-test.md \
  experiments/01-self-indexing-removal-test/pre-registration.md \
  experiments/03-retained-independence/pre-registration.md \
  "$E06/pre-registration.md" "$E06/amendment-a3.md" "$E06/control-learnability-pilot.md" \
  docs/public-path-roadmap-2026-09-16.md

# ---------- bundle 2: record ----------
B2="$OUT/bundle-2-record.md"
cat > "$B2" <<'EOF'
# Bundle 2 of 3: what happened

Verbatim concatenation of committed repository files, built by make-bundles.sh. Nothing is edited or abridged except STATUS.md, of which only the current-state sections (2026-09-19 and 2026-09-20) and the short "arc" section are included; the older entries are in the repository's git history and in bundle 3 on request. Each file begins with `===== FILE: <path> =====`.

Contents, in order:
1. STATUS.md, current-state sections only
2. experiments/01-self-indexing-removal-test/removal-test-findings.md
3. experiments/03-retained-independence/results.md
4. experiments/06-.../gate2-pilot-findings.md (A3 pilot)
5. experiments/06-.../seeds-endpoint-findings.md (A3 seeds 1 and 2)
6. experiments/06-.../register-lesion-findings.md, register-saturation-findings.md, register-direct-probe-findings.md
7. experiments/06-.../ceiling-measurement-findings.md and ceiling-defect-2026-09-17.md
8. experiments/06-.../control-learnability-pilot-findings.md
9. experiments/06-.../blind-arm-findings.md and blind-control-findings.md
10. experiments/06-.../powered-position-sweep-findings.md
11. experiments/06-.../fitted-position-sweep-findings.md and its 2026-09-20 correction
12. experiments/06-.../separation-clause-requirements.md
13. experiments/06-.../red_team_ledger.md (RT-01 to RT-93, every ruling)
14. docs/outside-review-protocol.md
15. docs/step4-control-battery-proposal-2026-09-20.md (draft, the 2026-10-04 decision)
16. experiments/06-.../reviews/2026-09-20-followup-runs-brief.md
EOF
{ printf '\n\n===== FILE: STATUS.md (current-state sections and "The arc" only) =====\n\n'; status_current; } >> "$B2"
emit "$B2" experiments/01-self-indexing-removal-test/removal-test-findings.md \
  experiments/03-retained-independence/results.md \
  "$E06/gate2-pilot-findings.md" "$E06/seeds-endpoint-findings.md" \
  "$E06/register-lesion-findings.md" "$E06/register-saturation-findings.md" "$E06/register-direct-probe-findings.md" \
  "$E06/ceiling-measurement-findings.md" "$E06/ceiling-defect-2026-09-17.md" \
  "$E06/control-learnability-pilot-findings.md" \
  "$E06/blind-arm-findings.md" "$E06/blind-control-findings.md" \
  "$E06/powered-position-sweep-findings.md" \
  "$E06/fitted-position-sweep-findings.md" "$E06/fitted-position-sweep-findings-CORRECTION-2026-09-20.md" \
  "$E06/separation-clause-requirements.md" \
  "$E06/red_team_ledger.md" \
  docs/outside-review-protocol.md docs/step4-control-battery-proposal-2026-09-20.md \
  "$E06/reviews/2026-09-20-followup-runs-brief.md"

# ---------- bundle 3: appendix ----------
B3="$OUT/bundle-3-appendix.md"
cat > "$B3" <<'EOF'
# Bundle 3 of 3: appendix

Verbatim concatenation of committed repository files, built by make-bundles.sh. Supporting material; read as needed. Each file begins with `===== FILE: <path> =====`.

Contents, in order:
1. explainer.md (the plain-language companion, last revised 2026-07-01, predates experiment 6)
2. docs/wave3-amendment-proposal-2026-09-15.md (the proposal that became A3) and experiments/06-.../registration-decision-memo.md
3. experiments/06-.../red-team-pass-3.md (the pass on A3 before registration)
4. docs/control-clause-proposal-2026-09-19.md (Amendment A4 as proposed), experiments/06-.../a4-red-team-pass-1.md, experiments/06-.../red-team-a4.md (why A4 was refused)
5. experiments/06-.../control-battery-proposal.md (the 2026-09-17 options)
6. The three tier-1 reviews on file, with their packets: reviews/2026-09-20-control-learnability-claude-worktree.md, reviews/2026-09-20-fitted-read-claude-worktree.md, and the 2026-09-19 linear-read-closure review with its addendum
7. experiments/06-.../compute-ledger.md (every dollar)
8. research/removal-test-vs-the-field-research-note.md, research/minimum-viable-consciousness-literature-vs-our-writing.md, docs/research-note-pain-axis-2026-09-19.md
9. docs/outside-reader-shortlist-2026-09-19.md
10. experiments/07-embodiment-amplifier-test/pre-registration.md (a later stage, not yet run)
EOF
emit "$B3" explainer.md docs/wave3-amendment-proposal-2026-09-15.md "$E06/registration-decision-memo.md" \
  "$E06/red-team-pass-3.md" \
  docs/control-clause-proposal-2026-09-19.md "$E06/a4-red-team-pass-1.md" "$E06/red-team-a4.md" \
  "$E06/control-battery-proposal.md" \
  "$E06/reviews/2026-09-20-control-learnability-packet.md" "$E06/reviews/2026-09-20-control-learnability-claude-worktree.md" \
  "$E06/reviews/2026-09-20-fitted-read-packet.md" "$E06/reviews/2026-09-20-fitted-read-claude-worktree.md" \
  "$E06/reviews/2026-09-19-linear-read-closure-packet.md" "$E06/reviews/2026-09-19-linear-read-closure-claude-worktree.md" "$E06/reviews/2026-09-19-linear-read-closure-claude-worktree-addendum.md" \
  "$E06/compute-ledger.md" \
  research/removal-test-vs-the-field-research-note.md research/minimum-viable-consciousness-literature-vs-our-writing.md docs/research-note-pain-axis-2026-09-19.md \
  docs/outside-reader-shortlist-2026-09-19.md \
  experiments/07-embodiment-amplifier-test/pre-registration.md

# ---------- cover prompts: cover note + the fixed brief ----------
cat "$OUT/cover-gemini.md" "$OUT/brief.md" > "$OUT/PASTE-gemini.md"
cat "$OUT/cover-chatgpt-astra.md" "$OUT/brief.md" > "$OUT/PASTE-chatgpt-astra.md"

# ---------- 20 KB chunks split at line boundaries, for a reviewer whose file tool truncates long output ----------
# (Astra in the Codex app, 2026-09-20: truncated a 40 KB file, so its limit is roughly 7k tokens; 20 KB is about 5k.)
mkdir -p "$OUT/chunks-20k"
for b in 1 2 3; do
  f=$(ls "$OUT"/bundle-$b-*.md)
  awk -v pre="$OUT/chunks-20k/bundle-$b-part-" '
    BEGIN { n=0; sz=0; out=sprintf("%s%02d.md", pre, n) }
    { l=length($0)+1
      if (sz+l > 20000 && sz > 0) { close(out); n++; sz=0; out=sprintf("%s%02d.md", pre, n) }
      print > out; sz+=l }' "$f"
done

echo "Built:"
wc -c "$B1" "$B2" "$B3" "$OUT/PASTE-gemini.md" "$OUT/PASTE-chatgpt-astra.md"
