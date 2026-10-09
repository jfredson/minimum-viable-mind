# The reporting table's layout fix, 2026-10-08

`procedure.table` printed 12 "withheld" cells on a withheld seed where the
header has room for 11, so on those rows the last two columns sat under the
wrong headings. Fixed in `src/procedure.py` (12 to 11). No figure is computed
differently.

Evidence: the page 4 pass at limit 10,000 (`../passB-limit10000/`) was copied
to a scratch folder and re-summarised with the fixed code
(`procedure.py summarise --dir <copy>`). Its `summary.json` is byte-for-byte
identical to the committed one, every row that is not withheld is identical,
and every row of the rebuilt table, `table-passB-rebuilt.md`, has 16 cells,
as the header does (the committed table has 17 on its 9 withheld rows).
