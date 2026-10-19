#!/usr/bin/env bash
# Check 7 of the check of pull request 174 (2026-10-17): what the pull request
# changed in the filtered-battery draft, against the main line, and whether the
# re-taken sweep counts reproduce. Reads only.
#
#   bash docs/reviews/2026-10-17-battery-rehearsal-method-check-scripts/draft_diff.sh
set -u
cd "$(dirname "$0")/../../.."
D=docs/filtered-battery-proposal-2026-10-07.md
BASE=$(git merge-base origin/main HEAD)
echo "branch point $(git rev-parse --short "$BASE"); main line now $(git rev-parse --short origin/main)"
echo "main line commits since the branch point that touch the draft: $(git log --oneline "$BASE"..origin/main -- $D | wc -l | tr -d ' ')"
echo
echo "## lines removed from the draft (every one):"
git diff -U0 "$BASE" HEAD -- $D | grep '^-[^-]' | sed 's/^/  /'
echo "## lines added, outside the new closing section:"
git diff -U0 "$BASE" HEAD -- $D | awk '/^@@/{h=$0} /^\+[^+]/{print h" | "$0}' | grep -v '+1537,\|+1536,' | sed 's/^/  /'
echo "## hunks:"
git diff -U0 "$BASE" HEAD -- $D | grep '^@@' | sed 's/^/  /'
echo
echo "## numbers in the new closing section (dates, the pull request number, entry numbers only?):"
sed -n '/^## Changes after the fourth check/,$p' $D | grep -oE '[0-9][0-9.,-]*' | sort -u | tr '\n' ' '; echo
echo "## words 'band', 'gate', 'reading', 'ruled', '\$' in added lines:"
git diff -U0 "$BASE" HEAD -- $D | grep '^+[^+]' | grep -niE 'band|gate|reading|ruled|\$' | sed 's/^/  /'
echo
echo "## the three sweep counts, re-taken on the pull request's file (the draft says 322, 120 and 17737)"
grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' $D
grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' $D
wc -w < $D | tr -d ' '
echo "route sentences ('carried by the token'): $(grep -c 'carried by the token' $D) (the hand-over note says 9)"
echo "em-dashes and en-dashes in the draft: $(grep -c $'\xe2\x80\x94' $D) and $(grep -c $'\xe2\x80\x93' $D)"
echo "the version 4 header still says the version is owed a check: $(grep -c 'owed a check by a session that wrote neither it nor the third check' $D)"
