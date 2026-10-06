# A2 made-up cases: expected against actual

| # | case | expected | got | all checks | withheld figure found in outputs | term as reported |
|---|---|---|---|---|---|---|
| 1 | toy | R3 | R3 | yes | none | substrate not a testbed: arm F failed its gate on learning |
| 2 | toy-step5a-seed0 | fifth | fifth | yes | none | metric validated, degree not read: failed its gate on learning |
| 3 | toy-step5a-seed1 | R3 | R3 | yes | none | substrate not a testbed: arm F failed its gate on learning at step 5a (seed 1), after its re-run; nothing else launches (stop S4) |
| 4 | r1 | R1 | R1 | yes | none | metric validated, degree read |
| 5 | r2 | R2 | R2 | yes | none | metric does not separate |
| 6 | fallback-read | fallback_read | fallback_read | yes | none | metric checked against the separable model only, degree read |
| 7 | fallback-not-read | fallback_not_read | fallback_not_read | yes | none | metric checked against the separable model only, degree not read: read failed its floor: no size's piece reaches four fifths; reported for description only (the site set was chosen with the piece rule switched off) |
| 8 | T-no-verdict | not_validated | not_validated | yes | none | metric not validated: control 1, the content transplant, on arm T failed |
| 9 | T-and-C-no-verdict | not_validated | not_validated | yes | none | metric not validated: control 1, the content transplant, on arm T failed |
| 10 | split-review-table | fifth | fifth | yes | none | metric validated, degree not read: failed its gate on learning |
| 11 | split-learning-passes | fifth | fifth | yes | none | metric validated, degree not read: read failed its floor: no size's piece reaches four fifths; the channel removal did not collapse own-directed answers below the gate bar; the ownership-free line failed (with the channel zeroed, own-directed answers among the four candidates, line 1,546 of 3,000) |
| 12 | split-one-seed-everything | fifth | fifth | yes | none | metric validated, degree not read: failed its gate on learning (named-other condition: failed); the channel removal did not collapse own-directed answers below the gate bar |
| 13 | overlap-one-seed | R1 | R1 | yes | none | metric validated, degree read |
| 14 | M-outside-band | R1 | R1 | yes | none | metric validated, degree read |
| 15 | M-fails-gate | R1 | R1 | yes | none | metric validated, degree read |
| 16 | withheld-seed | R1 | R1 | yes | none | metric validated, degree read |
| 17 | never-run-line | fifth | fifth | yes | none | metric validated, degree not read: the ownership-free line was not run |
| 18 | never-run-control | fallback_read | fallback_read | yes | none | metric checked against the separable model only, degree read |
| 19 | no-transplant-outside | R1 | R1 | yes | none | metric validated, degree read |
| 20 | F-channel-removal | fifth | fifth | yes | none | metric validated, degree not read: the channel removal did not collapse own-directed answers below the gate bar |
| 21 | T-fails-gate | R3 | R3 | yes | none | substrate not a testbed: arm T failed its gate on learning |
| 22 | F-fails-5a | R3 | R3 | yes | none | substrate not a testbed: arm F failed its gate on learning at step 5a (seed 1), after its re-run; nothing else launches (stop S4) |

Input rows (SHA-256):

- `row_C_seed0.json` 698cc77530016ca2a999dc283504e3d6876e1816bdf5b2df02de529ddf76efc7
- `row_C_seed1.json` 50aeaf8312c209dbb4279f23e7515c34031ba5fba573a850c3bb2ccd7e3caaf1
- `row_C_seed2.json` 25435d4fa0ffb5c99832057f148dde2dbdf5314b710bcfeaf3ced754bb7f14c6
- `row_F_seed0.json` f451e5daffac6c9682a128205c55d48566e65d4ca16cf814c693ca0472e94063
- `row_F_seed1.json` b1f78e094d57a26a111aecaf52dafe50174e45114dd3ff5a7b5c9769c395d35e
- `row_F_seed2.json` 49cde326978c41909bbee91c1550b75be82a72af5891cc96a97f49cac16a5df0
- `row_M_seed0.json` 1827044901b66346f8898b55f1ce80439c76fd512ed4f381f0c143983a72706e
- `row_M_seed1.json` bac5a02800e95bff5333fd27e84951aeb1bb7548d6179152e628e97078c83e26
- `row_M_seed2.json` ef31200b71ed56d49f8843156479f2bce3a78d28e4f20cdc250281bff68108fb
- `row_T_seed0.json` de367b672c33a8adddb820e2074e65139b37854d49d68e8e282c0d96d97c9832
- `row_T_seed1.json` 554439ebb51aec55d4993d90ae46637e57b322d73868021dda60d61695f8f1d6
- `row_T_seed2.json` 8ecb84e9345983a261416794532089b4758375a66aaf9eadf26daa0dafeb91be
