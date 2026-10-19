# Reproducibility verification

Verified 18 October 2026 for the Assessment 4 setup and documentation change.

## Scope and source

The pipeline notebook is unchanged from main commit `46e142f88e0e850c08be687425c209f27b415fd2`. Its SHA-256 is `27de1a1cbe5a5fd0d2787eb9f4d6edd1388993763553380bbdc9e900caa020c1`. A separate fresh virtual environment was created with Python 3.12.14 on macOS arm64. The packages were installed from the updated `requirements.txt`; `pip check` reported no broken requirements. The full resolved environment is captured in `requirements-lock-macos-py312.txt`.

The executed data-preparation path uses the original notebook cells from setup through the model-ready reporting frame. Smoke mode then calls the notebook's model-building code with small, untuned trees to verify API and serialization compatibility. This is a setup/integration check, not a new model experiment. No hyperparameter searches, rolling model backtests or final model selection were rerun. Existing report metrics remain saved notebook results.

## Verified commands

From the repository root, in the isolated Python 3.12 environment:

```bash
python -m pip install -r requirements.txt
python -m pip check
python -m jupyterlab --version
python scripts/run_notebook.py --mode smoke
python scripts/run_notebook.py --mode preparation
```

JupyterLab reported version 4.4.3. The smoke run passed in 68.49 seconds on this host. The machine-readable [smoke report](Notebook_Smoke_Verification.json) records the input hashes, notebook hash, exact package versions, UTC execution time and results. The local executed notebook and smoke bundles are deliberately not committed because notebook previews can contain raw listing details.

## Observed preparation results

| Check | Observed result |
|---|---|
| Raw property records | 15,423 |
| Cleaned, merged and model-ready rows | 8,209 at each stage |
| Initial temporal split | 6,541 train / 1,668 test |
| Cutoff | 12 November 2024 UTC; train dates precede test dates |
| Coordinate sign repairs / scope exclusions | 0 / 209 |
| Population and income lag | 1 year |
| CPI lag | 1 quarter |
| ERP, household income, cash rate, CPI index and annual-change join coverage | 100% for each checked field |
| Duplicate model-ready property IDs | 0 |
| Required numeric missing values after preparation | 0 |
| Derived CSVs checked for absence of `address` | All six cleaning/merge exports plus `model_ready.csv` |
| Linear Regression, Random Forest and XGBoost smoke predictions | 100 finite positive predictions per model |
| Model save/load roundtrip | Predictions preserved for all three models |

The smoke trees use 20 estimators and maximum depth 4. Their outputs are not comparable to the tuned report metrics and must not be deployed as the selected model. The smoke check does not certify every column as free of personal data; the automated export check specifically tests for the `address` column.

## Input snapshot identity

These are the exact checked-in files used, not replacement downloads. Input provenance labels come from the notebook; exact source release IDs, extraction dates and original download URLs still need to be completed by the source owners before refreshing the snapshots.

| File | SHA-256 |
|---|---|
| `data/raw/properties.csv` | `0c4f25577c9ca9b220f82cc23601ccc3f9ca2889bebe8e6e7a4507331a898278` |
| `data/raw/ERP.csv` | `8c6e99c7bf02cfe399a5ce1fa550671409f3aed4d69b01d22783d0e452a1f7bf` |
| `data/raw/annual_household_nt.csv` | `fd359c2e1e65d032a58777e7e6c774a5f7d085ecdc152e90e4baaf7ff8c4d9a9` |
| `data/raw/cash_rates.csv` | `3c70a862bca29cd957cbaeac8d0f377af7f83201ead84c4e8a6ab143957fc2af` |
| `data/raw/cpi_index.csv` | `1e20eb0626d1486c6913c9cd4dd067bd01789a23199727afec5e4048fd776df3` |

## Reproduction boundaries and dashboard handoff

- Full notebook execution remains available through `python scripts/run_notebook.py --mode full --timeout 7200`. It uses the original model parameters and writes the production export set only when those sections are reached. It has not been run as part of this verification.
- The notebook still has a stale-output/narrative warning. A fresh full run and comparison are needed before certifying tuned metrics and final model exports.
- The notebook's upstream IQR filters use a single November 2024 cutoff before earlier rolling evaluations, and observed target-price filters restrict the evaluation population. Setup fixes do not repair those methodological limits.
- Fixed one-year annual and one-quarter CPI lags need release-date validation. They do not establish that every source value was published before each sale.
- The raw properties snapshot contains addresses and agent/listing information; removing `address` from derived CSVs is not anonymisation of the source repository.
- `code/app.py` and `code/plots.ipynb` do not exist on the reviewed main branch. An older app exists on `bipana01-patch-4`, but importing it without matching its model/reference schema would risk an inconsistent deployment. Current dashboard source, dependency pins, deployment commit and matched artifacts are needed from its owner. Live deployment behaviour was not tested.
- Installation and execution were checked on macOS arm64/Python 3.12 only. No Linux or Windows success is claimed.

## Report wording supported by this verification

A fresh Python 3.12 environment successfully installed the pinned dependencies and notebook tools. The unchanged preparation pipeline regenerated 8,209 model-ready rows from 15,423 raw property records, with a 6,541/1,668 temporal split and full coverage of the five checked macro fields. Three small model fits and save/load prediction checks passed. These checks establish setup and preparation compatibility; the complete tuning/backtest run and current dashboard deployment remain unverified.
