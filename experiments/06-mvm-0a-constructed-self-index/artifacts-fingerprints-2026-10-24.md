# Experiment 06's model files: fingerprints, and the duplicates removed on 2026-10-24

*Written 2026-10-24 (Pacific) on John's ruling of that day (`docs/rulings/2026-10-24-revised-theory-next-steps-ruling.md`, item 5): remove the exact duplicates (estimated at 8.4 GB), keep one copy of each, and commit the list of fingerprints.*

**What was done.**
- The `artifacts/` folder beside this file is kept out of git, so this list is the only record in the repository of what it holds.
- Before the removal the folder held 37 model files (`.pt`). Each was fingerprinted with SHA-256, a checksum of its contents, so two files with the same fingerprint are byte-for-byte the same.
- They came to 15 distinct files. The 22 extra copies were deleted, about 8.69 GB counted in units of 1,000 (the proposal's "8.4 GB" was an estimate from folder sizes). The folder went from 13 GB to 4.6 GB.
- Copies were matched by fingerprint, not by name. This matters because the same name is used for different files: `pilot_a1_30m_seed1.pt` and `pilot_a1_30m_seed2.pt` each exist in two different versions.
- The copy kept from each group is the one in the folder of the same name, for example `a3_30m_seed0/a3_30m_seed0.pt`. Every group had one.
- Before deleting, the main line was searched for any record citing a deleted path, and none did.
- After the removal, the 15 remaining files were fingerprinted again, and all 15 fingerprints are distinct.
- Nothing else was moved or deleted.

| SHA-256 | Size (bytes) | Kept at | Removed copies |
|---|---|---|---|
| `ff8716418e7c9da340a6b6097fd5c884fdcda45ba9544557be6b65c97b394bda` | 351,526,119 | `a3_30m_seed0/a3_30m_seed0.pt` | `a3_30m_seed1/a3_30m_seed0.pt`, `a3_30m_seed2/a3_30m_seed0.pt` |
| `816caa079f5d16aa5672dc4bcfc7cb85d23f6ea9d6c5d4bb2dee7a7fc1e46d84` | 351,533,445 | `pilot_a1_30m_seed0_twin/pilot_a1_30m_seed0_twin.pt` | `a3_30m_seed0/pilot_a1_30m_seed0_twin.pt`, `a3_30m_seed1/pilot_a1_30m_seed0_twin.pt`, `a3_30m_seed2/pilot_a1_30m_seed0_twin.pt`, `pilot_a1_30m_seed1/pilot_a1_30m_seed0_twin.pt`, `pilot_a1_30m_seed1_twin/pilot_a1_30m_seed0_twin.pt`, `pilot_a1_30m_seed2/pilot_a1_30m_seed0_twin.pt` |
| `c976899bf6ebd235190f46e23a6384ce60c64f223be0bd5ce811872add072648` | 470,762,819 | `pilot_a1_30m_seed1/pilot_a1_30m_seed1.pt` | `a3_30m_seed0/pilot_a1_30m_seed1.pt`, `a3_30m_seed1/pilot_a1_30m_seed1.pt`, `a3_30m_seed2/pilot_a1_30m_seed1.pt`, `pilot_a1_30m_seed1_twin/pilot_a1_30m_seed1.pt`, `pilot_a1_30m_seed2/pilot_a1_30m_seed1.pt` |
| `a4393b60095533e890181ca7cd52f4b587ba576c1e12ba50db9a3fcb1f5008a4` | 351,533,445 | `pilot_a1_30m_seed1_twin/pilot_a1_30m_seed1_twin.pt` | `a3_30m_seed0/pilot_a1_30m_seed1_twin.pt`, `a3_30m_seed1/pilot_a1_30m_seed1_twin.pt`, `a3_30m_seed2/pilot_a1_30m_seed1_twin.pt`, `pilot_a1_30m_seed2/pilot_a1_30m_seed1_twin.pt` |
| `b16afc589cc05db3e9f21d394f0b9edd838dd1d09399908a2b7493c82a087294` | 470,762,819 | `pilot_a1_30m_seed2/pilot_a1_30m_seed2.pt` | `a3_30m_seed0/pilot_a1_30m_seed2.pt`, `a3_30m_seed1/pilot_a1_30m_seed2.pt`, `a3_30m_seed2/pilot_a1_30m_seed2.pt` |
| `8825554587a042d51acfe00b091530e74f94e5a79665c47db68d48f5010d239c` | 351,526,119 | `a3_30m_seed1/a3_30m_seed1.pt` | `a3_30m_seed2/a3_30m_seed1.pt` |
| `8e969708e9eb35c4bf8fbea1cdb4a2a46021a8dabff22d4e6f0592c4678328f1` | 351,526,119 | `a3_30m_seed2/a3_30m_seed2.pt` | `a3_30m_seed1/a3_30m_seed2.pt` |
| `9d2af2747e2485cb03376981cfb693b76676d6307ce128ff1e79c0744111972b` | 351,527,989 | `a3ctl_30m_seed0/a3ctl_30m_seed0.pt` | none |
| `982396e7dc9f817662827aab7f0fe673cd5871ee048075d03d0171a59b3d610a` | 351,526,773 | `a3ctl_30m_seed0/a3ctl_30m_seed0_PARTIAL_step51500.pt` | none |
| `5abbeef70d3cb4e6b0dff85be3038f7f4e6f659261f1f29a9f21caafb06cce11` | 34,416,855 | `pilot-10m-seed0/pilot_10m_seed0.pt` | none |
| `9484770d62883294e845f74501c1a556d3be54f17afeca06efd158597ea57e64` | 34,680,454 | `pilot-a1-10m-seed0/pilot_a1_10m_seed0.pt` | none |
| `5e150a36d92ccdf57d7a3f28e5e04bdcd6c1e886dd6ca879306b8c86f1d26844` | 470,762,819 | `pilot_a1_30m_seed0/pilot_a1_30m_seed0.pt` | none |
| `ef746e769289894b4bfd380e3704f8c47b7b5447f553af062c9ed7197456c359` | 470,753,091 | `pilot_a1_30m_seed0_twin/pilot_a1_30m_seed1.pt` | none |
| `a3261ac280b12f252e46bdb74cd79895cef0dcbf27353361616d6f4cd604e149` | 470,751,939 | `pilot_a1_30m_seed1_twin/pilot_a1_30m_seed2.pt` | none |
| `e7d5e443e5c95e0d8c9c6fe32efe6ff908f1cb88e41a8be00146ffec1beada2d` | 77,450,933 | `slice_handshake/slice_handshake.pt` | none |
