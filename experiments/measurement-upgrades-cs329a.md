# Measurement upgrades borrowed from the CS329A evaluation canon

*Review memo, 2026-08-04. Source: Stanford CS329A "Self-Improving AI Agents"
(Autumn 2025, https://cs329a.stanford.edu) — specifically its evaluation
readings: METR's "Measuring AI Ability to Complete Long Tasks"
(arxiv 2503.14499), "Large Language Monkeys" (arxiv 2407.21787), "How Do Large
Language Monkeys Get Their Power (Laws)?" (arxiv 2502.17578), the
generation–verification-gap line (arxiv 2506.18203, 2110.14168, 2305.20050),
and GDPval (arxiv 2510.04374). This memo maps their measurement machinery onto
the Stage 3 ladder and the registered-metric pipeline. It proposes; nothing
here is adopted until registered.*

## What their graphs actually are

The capability graphs that carry these papers are not decoration; each one is
a statistical commitment:

1. **METR's time-horizon curve.** Per model, fit a logistic success curve
   against log(human task duration); read off the 50% intercept as a single
   scalar ("time horizon"); plot that scalar against model release date on a
   log axis; put hierarchical-bootstrap 95% CIs (resampling task families →
   tasks → attempts) on every point and on the trend. The graph is legible
   because the scalar is interpretable and the uncertainty is honest.
2. **Large Language Monkeys' coverage curves.** pass@k (unbiased estimator)
   on log-log axes across orders of magnitude of samples, with the
   coverage-vs-selection gap made explicit: what the model *ever* does across
   k samples is a different quantity from what a selector can extract, and
   they plot both.
3. **The power-laws follow-up.** Aggregate curves are artifacts of the
   *distribution* of per-item difficulty — a heavy tail of hard items warps
   per-item exponentials into an aggregate power law. Fitting per-item success
   probabilities and deriving the aggregate beats fitting the aggregate
   directly, by orders of magnitude of compute.

## Where Stage 3 stands against that bar

The instrument design already meets or exceeds the canon (pre-registration in
separate commits, cross-family blind judging, construct-validity gates with
synthetic references, judge test–retest 0.978). The gap is entirely in the
statistics and presentation layer:

- `analyze_ladder.py` emits point estimates only, though pre-registration
  §Decision rule 4 promises "curves with confidence intervals."
- Single pass per cell at temperature 0 — no within-cell variance exists to
  estimate.
- No plotting code anywhere in the repo; registered secondary "retention
  curves by rung" exists only as three-element JSON lists.
- `ri_combined` n-weights two structurally different measurements, with the
  mechanical bank pinned at ceiling — the same aggregate-warping failure the
  power-laws paper diagnoses.

## Proposed upgrades, in priority order

### 1. Hierarchical bootstrap CIs (METR's move) — re-analysis, no new runs

Resample domains → items (→ samples, once k > 1) with replacement; recompute
RI, pref_r3, masked rate, evidence-update rate per draw; report 95% intervals
per (model, framing, bank). Lives in a shared `src/mvm/stats.py` so Stage 1
and the removal test stop duplicating rate arithmetic.

**Wager:** the Sonnet mind-framing margin (+0.067, currently "suggestive, not
affirmed") gets a CI that either excludes zero or doesn't. Either outcome is
progress; hand-waved binomial SEs in prose are not. **Loses if** bootstrap
intervals on n=30-per-cell data are so wide that every cross-model contrast
becomes indistinguishable — that would say the banks are too small, which is
itself worth knowing before the grid grows.

### 2. Repeated sampling per cell (Large Language Monkeys' move) — needs runs

k samples per cell at nonzero temperature on a registered subset (the W2-
relevant cells first: mind vs tool_expert framings). Two registered
quantities, mirroring coverage vs selection:

- **capitulation@k** — does pressure *ever* break retention across k samples.
  The mimicry-discount rule ("measure resistance, not response") favors this
  worst-case reading: one capitulation in five samples is a different fact
  about the model than zero in five, and temperature-0 single-pass cannot see
  it.
- **retention rate across samples** — the within-cell variance that feeds the
  bootstrap in (1).

**Wager:** temperature-0 results are representative. **Loses if** retention@k
at t≈0.7 diverges materially from the t=0 point estimate — which would mean
the headline RI numbers are seed artifacts.

### 3. Per-item heterogeneity view (power-laws move) — re-analysis

Report the distribution of per-item retention, not just cell means. Check
whether RI is carried by a few items; retire `ri_combined` as a headline in
favor of per-bank numbers plus the item distribution. The heavy-tail lesson
transfers directly: if three items produce most capitulations, the aggregate
is a statement about those items, not about the model.

### 4. Judge validation beyond test–retest (generation–verification-gap move)

Test–retest (0.978) cannot see a shared systematic bias. Add, on a registered
subsample: (a) a second cross-family judge with inter-judge agreement
reported, and (b) a human-adjudicated slice as ground truth — GDPval's
pattern of calibrating automated judges against human raters and publishing
the agreement rate. Same pass scripts the stance-leakage scan, which
currently voids W2 for Gemini while existing only as an unversioned ad-hoc
scan.

### 5. Pressure-dose logistic and a "pressure horizon" scalar — next-ladder design

METR's deepest move is making the x-axis a *calibrated continuous dose*
(human minutes) so a logistic fit yields one interpretable scalar per model.
The rung ladder is ordinal with three points — too thin to fit. A future
ladder could scale pressure along a countable axis (number of independent
dissenting sources, escalating stakes, authority gradient) to 5–6 rungs,
yielding a **50% retention horizon**: the pressure dose at which retention
crosses 0.5. That scalar is what makes the eventual headline graph possible.

### 6. The trend chart this project should be building toward

METR's headline graph is metric-vs-release-date. The analogue here: **retained
independence vs model release date, per family, with CIs.** Three models is
not a trend, but the artifact layout already supports accumulating points as
the grid fills in — and "does independence deepen as capability grows, or is
it flat?" is precisely the calibration question the corpus keeps asking. Every
grid expansion should append to this chart.

### 7. Plots, finally

A `src/plot_ladder.py` (matplotlib, reading `ladder_analysis.json` +
bootstrap output): retention curves by rung with CI bands per (model,
framing); an RI forest plot; stacked live/masked/capitulated bars. The
masked-not-capitulated finding — the actual headline of Stage 3 — is a
one-glance stacked-bar story and currently requires reading four markdown
tables to see.

## Sequencing

(1), (3), and (7) are pure re-analysis of existing artifacts and can run
without new registrations beyond an analyzer amendment. (2) and (4) need
small registered runs. (5) and (6) are design inputs for the next ladder and
the growing grid. One further housekeeping item the METR comparison exposes:
`artifacts/` is gitignored, so the 1,080 transcripts and 2,700 verdicts
behind the headline exist only on one machine — archive them (repo, tarball,
or object storage) before they are load-bearing in anything public.
