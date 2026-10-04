#!/bin/sh
# Check of proposal version 4: every line that touches one of the four points
# John's reconciliation ruling of 2026-10-03 settled, so that each can be read
# and classed by hand as "states it the new way", "states it the old way" or
# "does not state it". Run from the root of the checkout. Reads one file.
F=docs/successor-experiment-proposal-2026-10-03-v4.md

echo "=== lines marked reconciled"
grep -n -i 'reconcil' "$F" | cut -c1-150

echo
echo "=== point 1: library versions (recorded / pinned)"
grep -n -i -E 'pinn?ed|\bpin\b|pins\b|library versions|versions of torch|versions recorded|recorded in the output' "$F" | cut -c1-170

echo
echo "=== point 2: the separation (seed by seed / per seed / on every seed / two or more seeds)"
grep -n -i -E 'seed by seed|per seed|paired|separation' "$F" | cut -c1-170
echo "--- 'clear(s|ed) ... every seed' and the three per-seed figures given as the separation"
grep -n -i -E 'clear(s|ed)? (0\.5|it) on every seed|0\.5 on every seed|cleared at 1\.0051' "$F" | cut -c1-170

echo
echo "=== point 3: the episode counts and the sampling band"
grep -n -i -E 'sampling|\bband\b|600 development|180 held|last 180|numbers of episodes|episode counts|0\.0056' "$F" | cut -c1-170

echo
echo "=== point 4: the order of the piece rule, and what it can miss"
grep -n -i -E 'after the layer|layers are chosen|layer set is[[:space:]]*$|can miss|never changes[[:space:]]*$|which layers are used|later layer' "$F" | cut -c1-170
