#!/bin/sh
# Places outside the three edited files that still describe the weekly
# re-plan, the Sunday handoff, or a dated target as live.
# Run from the repository root:
#   sh experiments/06-mvm-0a-constructed-self-index/reviews/2026-10-04-rulings-opened-and-no-future-dates-check-scripts/stale_timing.sh
grep -n "re-plan\|Sunday-night handoff" CLAUDE.md site/README.md
grep -n "re-plan edits both\|Sunday-night handoff sets" data/roadmap.toml
grep -n "carried to a later weekend\|The weekly re-plan" site/src/pages/roadmap.astro
grep -n "which weekend it moved to" scripts/export_site.py
grep -n "realistic commit date" data/project.toml
grep -n "only a schedule laid over that dated line" STATUS.md
