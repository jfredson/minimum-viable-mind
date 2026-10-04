#!/bin/sh
# Check of proposal version 4: run again the text sweeps its section 17 prints
# (failure 2, part one; failure 4, part one), on the file as it stands on the
# main line, to compare with the output printed there. Run from the root of
# the checkout. Reads one file; writes one temporary copy and removes it.
F=docs/successor-experiment-proposal-2026-10-03-v4.md
T=$(mktemp)
awk '/^## 17\. /{exit} {print}' "$F" > "$T"
echo "--- failure 2, part one (section 17 prints lines 1256, 1257, 1258, 1262)"
grep -n -iE 'route by which|carried by the token|forced by the loss|is the input token' "$T" | cut -c1-90
echo "--- failure 4, part one (section 17 prints 759, 233, 68, 14, 3406, 8)"
grep -c -iE 'verif|measur|calibrat|attack|reproduc|confirm|\brun|\bran\b|check|shows|showed|found|observed|recorded|returns|returned|yield|result' "$T"
grep -c -E '[0-9]+\.[0-9]{2,}|[0-9]{1,3},[0-9]{3}' "$T"
grep -c MEASURED "$T"
grep -c ARGUED "$T"
wc -l < "$T"
grep -c 'checked: the check of the short run' "$T"
rm -f "$T"
