# Page 4 toy pass under the ruled code: comparison (written by tests/page4_ruled_compare.py)

- reproduction check, pass A (the ruled code, limit set back to 3,000) against the checked 1,800 record: 29077 values compared, 0 differ; iteration-limit warnings equal on 12 of 12 models: PASSES
- fields present in one record only (not compared): /fits_stopped_at_iteration_limit (new only), /gate/lesioned_candidate_other_correct (new only), /gate/lesioned_candidate_own_correct (new only), /gate/ownership_free_line (new only), /gate/route_in_use (new only), /gate/row_choice (new only), /primary/no_transplant/chance_formula_flags_a_broken_pairing_at_the_bar (new only), /primary/no_transplant/detection_margin_at_the_bar (old only), /primary/no_transplant/share_of_errors_on_donor_answer (new only), /primary/no_transplant/vetoes (new only), /read_split (new only), /sensitivity/no_transplant/chance_formula_flags_a_broken_pairing_at_the_bar (new only), /sensitivity/no_transplant/detection_margin_at_the_bar (old only), /sensitivity/no_transplant/share_of_errors_on_donor_answer (new only), /sensitivity/no_transplant/vetoes (new only), /stricter/no_transplant/chance_formula_flags_a_broken_pairing_at_the_bar (new only), /stricter/no_transplant/detection_margin_at_the_bar (old only), /stricter/no_transplant/share_of_errors_on_donor_answer (new only), /stricter/no_transplant/vetoes (new only)

## The twelve toy models: limit 3,000 (old) against 10,000 (new), both fitted on 1,800

| model | field | old | new | same? |
|---|---|---|---|---|
| T/0 | status | nominated | nominated | yes |
| T/0 | site_set | states (0,) at action, 8 directions | states (0,) at action, 8 directions | yes |
| T/0 | piece_correct | 180 | 180 | yes |
| T/0 | whole_read_correct | 180 | 180 | yes |
| T/0 | reading | 0.0000 | 0.0000 | yes |
| T/0 | untouched_whole_own_accuracy | 0.0000, 1.0000, 1.0000 | 0.0000, 1.0000, 1.0000 | yes |
| T/0 | control1_holds | True | True | yes |
| T/0 | control4_holds | True | True | yes |
| T/0 | control7_holds | True | True | yes |
| T/0 | true_slot | 0.0000 | 0.0000 | yes |
| T/0 | true_slot_distance | 0.0000 | 0.0000 | yes |
| T/0 | rider | 0.0000 | 0.0000 | yes |
| T/0 | stricter | [[1], 'action', 8, 180] | [[1], 'action', 8, 180] | yes |
| T/0 | stricter_reading | 0.0000 | 0.0000 | yes |
| T/0 | best_piece_anywhere | 180 | 180 | yes |
| T/0 | grid_whole_and_best_piece | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 180]] | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 180]] | yes |
| T/0 | piece_elsewhere_mean | — | — | yes |
| T/0 | control2 | not applicable | not applicable | yes |
| T/0 | control2_named_best_piece | — | — | yes |
| T/0 | control2_site_set | — | — | yes |
| T/0 | control2_own_directed_moved | — | — | yes |
| T/0 | control2_random_median | — | — | yes |
| T/1 | status | nominated | nominated | yes |
| T/1 | site_set | states (0,) at action, 8 directions | states (0,) at action, 8 directions | yes |
| T/1 | piece_correct | 180 | 180 | yes |
| T/1 | whole_read_correct | 180 | 180 | yes |
| T/1 | reading | 0.0000 | 0.0000 | yes |
| T/1 | untouched_whole_own_accuracy | 0.0000, 1.0000, 1.0000 | 0.0000, 1.0000, 1.0000 | yes |
| T/1 | control1_holds | True | True | yes |
| T/1 | control4_holds | True | True | yes |
| T/1 | control7_holds | True | True | yes |
| T/1 | true_slot | 0.0000 | 0.0000 | yes |
| T/1 | true_slot_distance | 0.0000 | 0.0000 | yes |
| T/1 | rider | 0.0000 | 0.0000 | yes |
| T/1 | stricter | [[1], 'action', 8, 180] | [[1], 'action', 8, 180] | yes |
| T/1 | stricter_reading | 0.0000 | 0.0000 | yes |
| T/1 | best_piece_anywhere | 180 | 180 | yes |
| T/1 | grid_whole_and_best_piece | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 180]] | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 180]] | yes |
| T/1 | piece_elsewhere_mean | — | — | yes |
| T/1 | control2 | not applicable | not applicable | yes |
| T/1 | control2_named_best_piece | — | — | yes |
| T/1 | control2_site_set | — | — | yes |
| T/1 | control2_own_directed_moved | — | — | yes |
| T/1 | control2_random_median | — | — | yes |
| T/2 | status | nominated | nominated | yes |
| T/2 | site_set | states (0,) at action, 8 directions | states (0,) at action, 8 directions | yes |
| T/2 | piece_correct | 180 | 180 | yes |
| T/2 | whole_read_correct | 180 | 180 | yes |
| T/2 | reading | 0.0000 | 0.0000 | yes |
| T/2 | untouched_whole_own_accuracy | 0.0000, 1.0000, 1.0000 | 0.0000, 1.0000, 1.0000 | yes |
| T/2 | control1_holds | True | True | yes |
| T/2 | control4_holds | True | True | yes |
| T/2 | control7_holds | True | True | yes |
| T/2 | true_slot | 0.0000 | 0.0000 | yes |
| T/2 | true_slot_distance | 0.0000 | 0.0000 | yes |
| T/2 | rider | 0.0000 | 0.0000 | yes |
| T/2 | stricter | [[1], 'action', 8, 180] | [[1], 'action', 8, 180] | yes |
| T/2 | stricter_reading | 0.0000 | 0.0000 | yes |
| T/2 | best_piece_anywhere | 180 | 180 | yes |
| T/2 | grid_whole_and_best_piece | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 180]] | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 180]] | yes |
| T/2 | piece_elsewhere_mean | — | — | yes |
| T/2 | control2 | not applicable | not applicable | yes |
| T/2 | control2_named_best_piece | — | — | yes |
| T/2 | control2_site_set | — | — | yes |
| T/2 | control2_own_directed_moved | — | — | yes |
| T/2 | control2_random_median | — | — | yes |
| C/0 | status | nominated | nominated | yes |
| C/0 | site_set | states (2,) at action, 4 directions | states (2,) at action, 4 directions | yes |
| C/0 | piece_correct | 178 | 178 | yes |
| C/0 | whole_read_correct | 180 | 180 | yes |
| C/0 | reading | 1.0026 | 1.0026 | yes |
| C/0 | untouched_whole_own_accuracy | 0.0512, 0.5400, 0.5487 | 0.0512, 0.5400, 0.5487 | yes |
| C/0 | control1_holds | — | — | yes |
| C/0 | control4_holds | True | True | yes |
| C/0 | control7_holds | True | True | yes |
| C/0 | true_slot | — | — | yes |
| C/0 | true_slot_distance | — | — | yes |
| C/0 | rider | — | — | yes |
| C/0 | stricter | [[2], 'action', 4, 178] | [[2], 'action', 4, 178] | yes |
| C/0 | stricter_reading | 1.0026 | 1.0026 | yes |
| C/0 | best_piece_anywhere | 180 | 180 | yes |
| C/0 | grid_whole_and_best_piece | [[17, 17], [180, 180], [180, 180], [180, 180], [180, 180]] | [[17, 17], [180, 180], [180, 180], [180, 180], [180, 180]] | yes |
| C/0 | piece_elsewhere_mean | — | — | yes |
| C/0 | control2 | no verdict | no verdict | yes |
| C/0 | control2_named_best_piece | — | — | yes |
| C/0 | control2_site_set | — | — | yes |
| C/0 | control2_own_directed_moved | — | — | yes |
| C/0 | control2_random_median | — | — | yes |
| C/1 | status | nominated | nominated | yes |
| C/1 | site_set | states (4,) at action, 8 directions | states (4,) at action, 8 directions | yes |
| C/1 | piece_correct | 178 | 178 | yes |
| C/1 | whole_read_correct | 180 | 180 | yes |
| C/1 | reading | 1.0000 | 1.0000 | yes |
| C/1 | untouched_whole_own_accuracy | 0.0488, 0.5575, 0.5813 | 0.0488, 0.5575, 0.5813 | yes |
| C/1 | control1_holds | — | — | yes |
| C/1 | control4_holds | True | True | yes |
| C/1 | control7_holds | True | True | yes |
| C/1 | true_slot | — | — | yes |
| C/1 | true_slot_distance | — | — | yes |
| C/1 | rider | — | — | yes |
| C/1 | stricter | [[4], 'action', 8, 178] | [[4], 'action', 8, 178] | yes |
| C/1 | stricter_reading | 1.0000 | 1.0000 | yes |
| C/1 | best_piece_anywhere | 180 | 180 | yes |
| C/1 | grid_whole_and_best_piece | [[17, 17], [180, 180], [180, 178], [180, 178], [180, 178]] | [[17, 17], [180, 180], [180, 178], [180, 178], [180, 178]] | yes |
| C/1 | piece_elsewhere_mean | — | — | yes |
| C/1 | control2 | no verdict | no verdict | yes |
| C/1 | control2_named_best_piece | — | — | yes |
| C/1 | control2_site_set | — | — | yes |
| C/1 | control2_own_directed_moved | — | — | yes |
| C/1 | control2_random_median | — | — | yes |
| C/2 | status | nominated | nominated | yes |
| C/2 | site_set | states (1,) at post-identity, 4 directions | states (1,) at post-identity, 4 directions | yes |
| C/2 | piece_correct | 165 | 165 | yes |
| C/2 | whole_read_correct | 180 | 180 | yes |
| C/2 | reading | 1.0000 | 1.0000 | yes |
| C/2 | untouched_whole_own_accuracy | 0.0600, 0.5463, 0.5525 | 0.0600, 0.5463, 0.5525 | yes |
| C/2 | control1_holds | — | — | yes |
| C/2 | control4_holds | True | True | yes |
| C/2 | control7_holds | True | True | yes |
| C/2 | true_slot | — | — | yes |
| C/2 | true_slot_distance | — | — | yes |
| C/2 | rider | — | — | yes |
| C/2 | stricter | [[1], 'post-identity', 4, 165] | [[1], 'post-identity', 4, 165] | yes |
| C/2 | stricter_reading | 1.0000 | 1.0000 | yes |
| C/2 | best_piece_anywhere | 180 | 180 | yes |
| C/2 | grid_whole_and_best_piece | [[17, 17], [180, 180], [180, 180], [180, 180], [180, 179]] | [[17, 17], [180, 180], [180, 180], [180, 180], [180, 179]] | yes |
| C/2 | piece_elsewhere_mean | 137 | 137 | yes |
| C/2 | control2 | no verdict | no verdict | yes |
| C/2 | control2_named_best_piece | — | — | yes |
| C/2 | control2_site_set | — | — | yes |
| C/2 | control2_own_directed_moved | — | — | yes |
| C/2 | control2_random_median | — | — | yes |
| M/0 | status | nominated | nominated | yes |
| M/0 | site_set | states (3,) at action, 8 directions | states (3,) at action, 8 directions | yes |
| M/0 | piece_correct | 180 | 180 | yes |
| M/0 | whole_read_correct | 180 | 180 | yes |
| M/0 | reading | 0.5252 | 0.5252 | yes |
| M/0 | untouched_whole_own_accuracy | 0.0125, 0.8050, 0.8712 | 0.0125, 0.8050, 0.8712 | yes |
| M/0 | control1_holds | — | — | yes |
| M/0 | control4_holds | True | True | yes |
| M/0 | control7_holds | True | True | yes |
| M/0 | true_slot | 0.5000 | 0.5000 | yes |
| M/0 | true_slot_distance | 0.0252 | 0.0252 | yes |
| M/0 | rider | — | — | yes |
| M/0 | stricter | [[3], 'action', 8, 180] | [[3], 'action', 8, 180] | yes |
| M/0 | stricter_reading | 0.5252 | 0.5252 | yes |
| M/0 | best_piece_anywhere | 180 | 180 | yes |
| M/0 | grid_whole_and_best_piece | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 180]] | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 180]] | yes |
| M/0 | piece_elsewhere_mean | — | — | yes |
| M/0 | control2 | not applicable | not applicable | yes |
| M/0 | control2_named_best_piece | — | — | yes |
| M/0 | control2_site_set | — | — | yes |
| M/0 | control2_own_directed_moved | — | — | yes |
| M/0 | control2_random_median | — | — | yes |
| M/1 | status | nominated | nominated | yes |
| M/1 | site_set | states (1,) at post-identity, 8 directions | states (1,) at post-identity, 8 directions | yes |
| M/1 | piece_correct | 180 | 180 | yes |
| M/1 | whole_read_correct | 180 | 180 | yes |
| M/1 | reading | 0.4793 | 0.4793 | yes |
| M/1 | untouched_whole_own_accuracy | 0.0175, 0.7738, 0.8800 | 0.0175, 0.7738, 0.8800 | yes |
| M/1 | control1_holds | — | — | yes |
| M/1 | control4_holds | True | True | yes |
| M/1 | control7_holds | True | True | yes |
| M/1 | true_slot | 0.4760 | 0.4760 | yes |
| M/1 | true_slot_distance | 0.0033 | 0.0033 | yes |
| M/1 | rider | — | — | yes |
| M/1 | stricter | [[1], 'post-identity', 8, 180] | [[1], 'post-identity', 8, 180] | yes |
| M/1 | stricter_reading | 0.4793 | 0.4793 | yes |
| M/1 | best_piece_anywhere | 180 | 180 | yes |
| M/1 | grid_whole_and_best_piece | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 180]] | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 180]] | yes |
| M/1 | piece_elsewhere_mean | 179 | 179 | yes |
| M/1 | control2 | not applicable | not applicable | yes |
| M/1 | control2_named_best_piece | — | — | yes |
| M/1 | control2_site_set | — | — | yes |
| M/1 | control2_own_directed_moved | — | — | yes |
| M/1 | control2_random_median | — | — | yes |
| M/2 | status | nominated | nominated | yes |
| M/2 | site_set | states (1,) at post-identity, 8 directions | states (1,) at post-identity, 8 directions | yes |
| M/2 | piece_correct | 180 | 180 | yes |
| M/2 | whole_read_correct | 180 | 180 | yes |
| M/2 | reading | 0.5208 | 0.5208 | yes |
| M/2 | untouched_whole_own_accuracy | 0.0138, 0.7937, 0.8712 | 0.0138, 0.7937, 0.8712 | yes |
| M/2 | control1_holds | — | — | yes |
| M/2 | control4_holds | True | True | yes |
| M/2 | control7_holds | True | True | yes |
| M/2 | true_slot | 0.4920 | 0.4920 | yes |
| M/2 | true_slot_distance | 0.0288 | 0.0288 | yes |
| M/2 | rider | — | — | yes |
| M/2 | stricter | [[1], 'post-identity', 8, 180] | [[1], 'post-identity', 8, 180] | yes |
| M/2 | stricter_reading | 0.5208 | 0.5208 | yes |
| M/2 | best_piece_anywhere | 180 | 180 | yes |
| M/2 | grid_whole_and_best_piece | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 179]] | [[180, 180], [180, 180], [180, 180], [180, 180], [180, 179]] | yes |
| M/2 | piece_elsewhere_mean | 179 | 179 | yes |
| M/2 | control2 | not applicable | not applicable | yes |
| M/2 | control2_named_best_piece | — | — | yes |
| M/2 | control2_site_set | — | — | yes |
| M/2 | control2_own_directed_moved | — | — | yes |
| M/2 | control2_random_median | — | — | yes |
| F/0 | status | read failed its floor: no size's piece reaches four fifths | read failed its floor: no size's piece reaches four fifths | yes |
| F/0 | site_set | — | — | yes |
| F/0 | piece_correct | — | — | yes |
| F/0 | whole_read_correct | — | — | yes |
| F/0 | reading | 1.0000 | 1.0000 | yes |
| F/0 | untouched_whole_own_accuracy | 0.0587, 0.4850, 0.5587 | 0.0587, 0.4850, 0.5587 | yes |
| F/0 | control1_holds | — | — | yes |
| F/0 | control4_holds | True | True | yes |
| F/0 | control7_holds | True | True | yes |
| F/0 | true_slot | — | — | yes |
| F/0 | true_slot_distance | — | — | yes |
| F/0 | rider | — | — | yes |
| F/0 | stricter | — | — | yes |
| F/0 | stricter_reading | — | — | yes |
| F/0 | best_piece_anywhere | 40 | 40 | yes |
| F/0 | grid_whole_and_best_piece | [[17, 17], [34, 30], [30, 30], [36, 40], [34, 33]] | [[17, 17], [34, 30], [30, 30], [36, 40], [34, 33]] | yes |
| F/0 | piece_elsewhere_mean | 20 | 20 | yes |
| F/0 | control2 | reported; no pass line | reported; no pass line | yes |
| F/0 | control2_named_best_piece | 176 | 176 | yes |
| F/0 | control2_site_set | [[3], 'action', 8, 171] | [[3], 'action', 8, 171] | yes |
| F/0 | control2_own_directed_moved | 0.0000 | 0.0000 | yes |
| F/0 | control2_random_median | 0.0025 | 0.0025 | yes |
| F/1 | status | read failed its floor: no size's piece reaches four fifths | read failed its floor: no size's piece reaches four fifths | yes |
| F/1 | site_set | — | — | yes |
| F/1 | piece_correct | — | — | yes |
| F/1 | whole_read_correct | — | — | yes |
| F/1 | reading | 1.0000 | 1.0000 | yes |
| F/1 | untouched_whole_own_accuracy | 0.0563, 0.5713, 0.5663 | 0.0563, 0.5713, 0.5663 | yes |
| F/1 | control1_holds | — | — | yes |
| F/1 | control4_holds | True | True | yes |
| F/1 | control7_holds | True | True | yes |
| F/1 | true_slot | — | — | yes |
| F/1 | true_slot_distance | — | — | yes |
| F/1 | rider | — | — | yes |
| F/1 | stricter | — | — | yes |
| F/1 | stricter_reading | — | — | yes |
| F/1 | best_piece_anywhere | 19 | 19 | yes |
| F/1 | grid_whole_and_best_piece | [[17, 17], [15, 18], [17, 17], [20, 19], [14, 19]] | [[17, 17], [15, 18], [17, 17], [20, 19], [14, 19]] | yes |
| F/1 | piece_elsewhere_mean | — | — | yes |
| F/1 | control2 | no verdict | no verdict | yes |
| F/1 | control2_named_best_piece | — | — | yes |
| F/1 | control2_site_set | — | — | yes |
| F/1 | control2_own_directed_moved | — | — | yes |
| F/1 | control2_random_median | — | — | yes |
| F/2 | status | read failed its floor: no size's piece reaches four fifths | read failed its floor: no size's piece reaches four fifths | yes |
| F/2 | site_set | — | — | yes |
| F/2 | piece_correct | — | — | yes |
| F/2 | whole_read_correct | — | — | yes |
| F/2 | reading | 1.0000 | 1.0000 | yes |
| F/2 | untouched_whole_own_accuracy | 0.0688, 0.5138, 0.5563 | 0.0688, 0.5138, 0.5563 | yes |
| F/2 | control1_holds | — | — | yes |
| F/2 | control4_holds | True | True | yes |
| F/2 | control7_holds | True | True | yes |
| F/2 | true_slot | — | — | yes |
| F/2 | true_slot_distance | — | — | yes |
| F/2 | rider | — | — | yes |
| F/2 | stricter | — | — | yes |
| F/2 | stricter_reading | — | — | yes |
| F/2 | best_piece_anywhere | 36 | 36 | yes |
| F/2 | grid_whole_and_best_piece | [[17, 17], [25, 24], [39, 36], [30, 27], [27, 28]] | [[17, 17], [25, 24], [39, 36], [30, 27], [27, 28]] | yes |
| F/2 | piece_elsewhere_mean | — | — | yes |
| F/2 | control2 | no verdict | no verdict | yes |
| F/2 | control2_named_best_piece | — | — | yes |
| F/2 | control2_site_set | — | — | yes |
| F/2 | control2_own_directed_moved | — | — | yes |
| F/2 | control2_random_median | — | — | yes |

Separation, lowest of arm C's readings minus highest of arm T's, from each row's arithmetic: old 1.0000, new 1.0000.

Outcome under the current decision code (pass B's summary): substrate not a testbed: arm F failed its gate on learning (named-other condition, on seeds 1 and 2)

## Fits that stopped at the iteration limit

| model | warnings, old (limit 3,000) | warnings, new (limit 10,000) | new, by kind (stopped / fits; most iterations) |
|---|---|---|---|
| T/0 | 0 | 0 | counts elsewhere on the site: 0 / 2; 25; held-out counts (own): 0 / 25; 80; the null (shuffled labels): 0 / 1000; 711; the read (named): 0 / 5; 1699; the read (own): 0 / 5; 37 |
| T/1 | 0 | 0 | counts elsewhere on the site: 0 / 2; 19; held-out counts (own): 0 / 25; 126; the null (shuffled labels): 0 / 1000; 724; the read (named): 0 / 5; 1114; the read (own): 0 / 5; 37 |
| T/2 | 0 | 0 | counts elsewhere on the site: 0 / 2; 30; held-out counts (own): 0 / 25; 158; the null (shuffled labels): 0 / 1000; 655; the read (named): 0 / 5; 1396; the read (own): 0 / 5; 40 |
| C/0 | 0 | 0 | counts elsewhere on the site: 0 / 2; 249; held-out counts (own): 0 / 25; 1272; the null (shuffled labels): 0 / 1000; 2527; the read (named): 0 / 5; 213; the read (own): 0 / 5; 45 |
| C/1 | 0 | 0 | counts elsewhere on the site: 0 / 2; 246; held-out counts (own): 0 / 25; 906; the null (shuffled labels): 0 / 1000; 1523; the read (named): 0 / 5; 927; the read (own): 0 / 5; 80 |
| C/2 | 1 | 0 | counts elsewhere on the site: 0 / 24; 1730; held-out counts (own): 0 / 25; 754; the null (shuffled labels): 0 / 1000; 1807; the read (named): 0 / 5; 3750; the read (own): 0 / 5; 57 |
| M/0 | 132 | 0 | counts elsewhere on the site: 0 / 2; 30; held-out counts (own): 0 / 25; 1139; the null (shuffled labels): 0 / 1000; 7385; the read (named): 0 / 5; 5535; the read (own): 0 / 5; 57 |
| M/1 | 240 | 0 | counts elsewhere on the site: 0 / 24; 2361; held-out counts (own): 0 / 25; 1470; the null (shuffled labels): 0 / 1000; 4815; the read (named): 0 / 5; 3206; the read (own): 0 / 5; 44 |
| M/2 | 99 | 0 | counts elsewhere on the site: 0 / 24; 707; held-out counts (own): 0 / 25; 763; the null (shuffled labels): 0 / 1000; 3536; the read (named): 0 / 5; 4017; the read (own): 0 / 5; 50 |
| F/0 | 2 | 0 | counts elsewhere on the site: 0 / 24; 2785; held-out counts (named): 0 / 25; 1762; held-out counts (own): 0 / 25; 2054; the null (shuffled labels): 0 / 1000; 4736; the read (named): 0 / 5; 1762; the read (own): 0 / 5; 2054 |
| F/1 | 11 | 0 | counts elsewhere on the site: 0 / 2; 876; held-out counts (own): 0 / 25; 2506; the null (shuffled labels): 0 / 1000; 3547; the read (named): 0 / 5; 3191; the read (own): 0 / 5; 2506 |
| F/2 | 10 | 0 | counts elsewhere on the site: 0 / 2; 2960; held-out counts (own): 0 / 25; 2960; the null (shuffled labels): 0 / 1000; 3660; the read (named): 0 / 5; 535; the read (own): 0 / 5; 2960 |

| arm | old warnings | new warnings | new, counted in the rows |
|---|---|---|---|
| T | 0 | 0 | 0 |
| C | 1 | 0 | 0 |
| M | 471 | 0 | 0 |
| F | 23 | 0 | 0 |

## The competing solver: limit 3,000 (old) against 10,000 (new), both fitted on 1,800

| reading / seed | old: best piece, nomination, status | new: best piece, nomination, status |
|---|---|---|
| channel_removed / 0 | 19, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 19, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |
| channel_removed / 1 | 17, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 17, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |
| channel_removed / 2 | 20, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 20, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |
| channel_left_on / 0 | 18, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 18, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |
| channel_left_on / 1 | 17, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 17, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |
| channel_left_on / 2 | 20, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor | 20, no site set clears the whole-state floor, no verdict: no site set clears the whole-state floor |

Solver warnings: old 2, new 0.

## The pre-stated concerns (page 4 method, section 6; this method, section 4)

- A: a built model (arm T, C or M) loses its nomination: no
- B: arm T's reading is not 0.0000, or its control 1 does not hold: no
- C: the separation (arm C's lowest minus arm T's highest) is below 0.5 or missing: no
- D: arm M's reading is outside 0.3 to 0.7 on a seed: no
- D2 (arm M's prediction): further than 0.10 from its true-slot reading on a seed: no
- E: the free model's read reaches the floor (a piece of 144 or more anywhere): no
- F: the solver returns a reading: no
- G: control 7 or control 4 fails anywhere (the chosen, stricter and sensitivity rows): no
- Fields that changed, by model: none
