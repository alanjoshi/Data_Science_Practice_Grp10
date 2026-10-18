# Greater Darwin Property Price Forecasting

**PRT661 Assessment 4 | Group Dan1-Theme2**

This repository contains a notebook pipeline that combines Homely property sales with population, NT household income, RBA cash rates and Darwin CPI. It cleans and joins the inputs, compares regression models, evaluates quarterly forecasts and exports a model bundle and dashboard reference data.

The supported entry point on this branch is **`code/main.ipynb`**. The notebook includes saved results and a warning about stale outputs: run it in a fresh kernel before treating its saved tables as a reproduced result. See [verification scope](#verification-and-known-limits) below.

## Repository layout

```text
code/main.ipynb                 # Complete pipeline, plots, evaluation and exports
data/raw/                      # Five tracked source CSVs
  properties.csv
  ERP.csv
  annual_household_nt.csv
  cash_rates.csv
  cpi_index.csv
data/processed/                # Regenerated cleaning and merge exports (ignored)
data/model_ready/              # Regenerated prepared table (ignored)
data/output/                   # Regenerated model, metrics and reference data (ignored)
  verification/                # Local execution reports, notebooks and smoke models
scripts/run_notebook.py         # Preparation, smoke and full execution commands
requirements.txt               # Pinned packages and Jupyter tools
requirements-lock-macos-py312.txt # Complete resolved verification environment
README.md
```

`code/app.py` and `code/plots.ipynb` are absent from this branch. Plots used by the current pipeline are inside `main.ipynb`. Older branches contain a dashboard, but they are not a verified deployment package for this model. The architecture work is reviewed separately in [PR #24](https://github.com/alanjoshi/Data_Science_Practice_Grp10/pull/24).

## Environment and installation

Use **Python 3.12**. Installation and smoke verification are recorded for macOS arm64; other operating systems are not yet verified. The original notebook metadata names Python 3.13.5, but metadata alone does not establish a tested setup. Model-library versions are preserved from the repository's pinned snapshot. `appnope` is restricted to macOS, and JupyterLab, nbclient, nbformat and nbconvert are explicitly included.

From a terminal, clone the repository and enter its root:

```bash
git clone https://github.com/alanjoshi/Data_Science_Practice_Grp10.git
cd Data_Science_Practice_Grp10
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip check
```

For the complete package snapshot used in the recorded macOS/Python 3.12 verification, install `requirements-lock-macos-py312.txt` instead of `requirements.txt`. That lock is an environment record, not a claim of portability to every platform. If XGBoost reports a missing `libomp` on macOS, install the OpenMP runtime using `brew install libomp`, then retry the import. Do not alter package versions silently when reproducing a model; record any changes and regenerate its outputs.

## Inputs and data handling

All five inputs already exist in `data/raw/`. Use the exact filenames below, including case on systems with case-sensitive filesystems.

| Filename | Meaning and handling |
|---|---|
| `properties.csv` | Homely sale listings; 15,423 raw records in the checked-in snapshot. Prices, dates, coordinates, property IDs and property attributes are cleaned by the notebook. |
| `ERP.csv` | ABS Greater Darwin estimated resident population. Population strings include thousands separators. |
| `annual_household_nt.csv` | NT-wide annual household income accounts. Metadata rows are removed and indicators become numeric. This is regional context, not suburb-level household income. |
| `cash_rates.csv` | RBA cash-rate changes. The first data row supplies the actual header; dates and rate ranges need parsing. |
| `cpi_index.csv` | Quarterly Darwin CPI index and annual percentage change. Quarter labels are parsed before joining. |

The raw snapshots and their hashes are recorded in the [reproducibility verification record](docs/project-governance/Reproducibility_Verification.md). Exact extraction/release provenance is not fully recorded for every snapshot; confirm those details before refreshing the sources.

The pipeline removes undisclosed/missing prices, duplicate property IDs and missing dates/coordinates. It checks a configured Greater Darwin bounding box, limits supported years, and applies price/land IQR filters. Annual population and income are joined using `sale year - 1`, cash rates use the latest event on or before the sale date, and CPI uses the previous quarter. These fixed lags do not replace a release-date audit. Imputation, rare-suburb grouping and target encoding are fitted after the time split.

**Privacy scope:** `data/raw/properties.csv` already contains addresses and other listing fields. The helper removes `address` from derived CSV exports; it does not anonymise the tracked raw snapshot. Executed notebooks can also contain raw preview rows. Keep local verification notebooks out of public uploads and check source permissions before redistributing raw listings.

## Run the notebook interactively

The notebook sets `PROJECT_DIR = Path("..")`. Its kernel must therefore start in **`code/`**, with `data/` in the parent directory:

```bash
cd code
python -m jupyterlab main.ipynb
```

Select the active Python 3.12 environment, then use **Restart Kernel and Run All Cells**. Do not start in the repository root and execute the notebook cells there: that would resolve `../data` to the wrong location. The notebook creates its output folders automatically. Preserve all cells in order because later EDA, preparation and evaluation cells depend on earlier definitions and computed variables.

## Automated verification and regeneration

Run these commands from the repository root with `.venv` activated. The runner sets the notebook working directory to `code/` and uses the Python interpreter that launched it, without modifying your registered Jupyter kernels.

```bash
# Data loading, EDA, cleaning, merging, temporal split and train-only preparation
python scripts/run_notebook.py --mode preparation

# The same preparation, plus small untuned fits for all three model APIs
# and joblib save/load prediction checks
python scripts/run_notebook.py --mode smoke

# Complete notebook: original tuning searches, backtests and final exports
python scripts/run_notebook.py --mode full --timeout 7200
```

The default mode is `preparation`. Smoke models have deliberately small tree counts and are saved under `data/output/verification/smoke_*.joblib`; they are **not** report models or replacements for `model_final.joblib`. Full mode preserves the notebook's modelling parameters. It performs several searches with five temporal CV folds, repeated backtests and bootstrap checks, so allow substantially longer than a preparation or smoke run. The runner limits default process/thread budgets to two where supported; this is not a strict memory limit, and the notebook's nested parallelism can still use substantial resources. Raise the per-cell timeout if a full tuning cell needs longer.

Each mode writes `<mode>_report.json` and `<mode>_executed.ipynb` under `data/output/verification/`, including input and notebook hashes, package versions, scope, timing and pass/fail status. A failure returns a nonzero exit status and retains the partially executed notebook for diagnosis. These files are ignored by Git. Reports are overwritten by another run of the same mode, so copy the report elsewhere if you need to preserve an earlier result.

## Generated outputs

| Directory | Key files and producing stage |
|---|---|
| `data/processed/` | `properties_clean.csv`, `annual_household_clean.csv`, `erp_clean.csv`, `cash_rate_clean.csv`, `cpi_clean.csv`, `merged_raw.csv` from cleaning and joining |
| `data/model_ready/` | `model_ready.csv` from the prepared train/test reporting frame |
| `data/output/` | Baseline/v2 metrics, tuning comparisons, policy experiments, quarterly/pooled backtests, benchmarks, interval and segment checks from Sections 11-15 |
| `data/output/` | `model_final.joblib`, `model_final_metadata.json`, `model_v2_*.joblib`, `predictions_split_A.csv`, `predictions_final_config_splits_A_B.csv` from the final model section |
| `data/output/` | `app_reference.json`, `backtest_final_by_fold.csv`, `feature_importance_final.csv`, `interval_coverage_by_fold.csv`, `MODEL_CARD.md` from the dashboard-reference/model-card sections |

Regenerate the model bundle, metadata and `app_reference.json` together from the same full run. Do not mix an old dashboard reference with a newly fitted model. Treat joblib bundles as executable serialized objects: load only trusted artifacts. A fresh full run is required before claiming that the final export set has been reproduced.

## Verification and known limits

The [verification record](docs/project-governance/Reproducibility_Verification.md) states exactly what was run and its observed results. Passing a smoke run establishes installation, preparation and model API/serialization compatibility; it does not reproduce the tuned backtest metrics or verify a deployment.

The notebook's saved final output reports 8,209 sales and an XGBoost model with policy features, 28 numeric and 3 categorical inputs. `USE_RECENCY_WEIGHTS = False` disables final-model training sample weighting; recency-weighted suburb encoding is a separate mechanism.

Important outstanding modelling limits remain: IQR bounds are calculated once using sales through November 2024 and reused in earlier backtests; target-based filtering excludes part of the evaluation population; annual and quarterly lags need release-date validation; there is no untouched holdout after the final refit; and stale narrative/output warnings require reconciliation after a full run. These are disclosed limitations, not fixed by setup documentation.

## Dashboard handoff

The older `bipana01-patch-4` branch contains `code/app.py`, but its compatibility with the current model/export schema is unverified. The previously documented Streamlit URL alone does not establish which source commit or model is deployed. Ask the dashboard owner for its current app source, dependency pins, deployment commit and paired model/reference artifacts. Then integrate and test them through a separate PR. No Streamlit launch command is provided for a branch that lacks the app. This notebook-only setup does not need `streamlit` or `plotly`; add and pin them alongside the actual app when that integration is ready.
