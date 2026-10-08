#!/bin/sh
# Closure check of RT-251, control 6: is any claim left, in version 5, its
# reporting table, or the frozen code's output labels, that control 6 tells
# copying the donor's answer apart from copying who is acting?
#
#   sh docs/reviews/2026-10-09-serious-findings-closure-check-scripts/control6_grep.sh
#
# Run from the repository root.
V5=docs/successor-experiment-proposal-2026-10-07-v5.md
SRC=experiments/08-successor-degree/src

echo "== 1. every line of version 5 naming control 6, its cells or the relaxed set"
grep -n -i "control 6\|control six\|same-value\|different-value\|relaxed set" "$V5" | cut -c1-220

echo
echo "== 2. every line of version 5 with a word of discrimination"
grep -n -i -E "discriminat|tell(s)? .{0,40}apart|distinguish|separates? (the two|copying|who)|rule[sd]? out|smuggl" "$V5" | cut -c1-220

echo
echo "== 3. the same words within three lines of 'control 6' (a claim split over lines)"
grep -n -i -B3 -A3 "control 6" "$V5" | grep -i -E "discriminat|apart|distinguish|separat|rule[sd]? out|smuggl" | cut -c1-220

echo
echo "== 4. the reporting table, section 7.5: its lines on control 6"
awk '/^### 7.5 The reporting table/{on=1} /^## 8\./{on=0} on' "$V5" | grep -n -i "control 6\|same-value\|different-value"

echo
echo "== 5. the frozen code: every mention of control 6 and its fields"
grep -n -i "control 6\|control6\|c\[.6.\]\|same_value\|different_value\|relaxed" "$SRC"/*.py | cut -c1-200

echo
echo "== 6. the frozen code: any word of discrimination anywhere"
grep -n -i -E "discriminat|distinguish|tell(s)? .{0,40}apart|smuggl" "$SRC"/*.py | cut -c1-200
echo "(end; nothing above this line means no hit)"

echo
echo "== 7. does any decision code read control 6? (withhold, arm_outcome, outcome)"
grep -n "\"6\"\|'6'" "$SRC"/measure.py || echo "measure.py: no reference to control 6"

echo
echo "== 8. the label control 6 prints under, in the committed reporting tables of the frozen code"
grep -rh -o -i "control 6[^|]*" experiments/08-successor-degree/out-*/ 2>/dev/null | sort | uniq -c
