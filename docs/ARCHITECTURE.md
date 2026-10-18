# System Architecture

**Bipana Tripathee** (S388875)
*System Architecture Lead*

Greater Darwin Property-Price Forecasting System - Group Dan1-Theme2

## Purpose and verification scope

This document describes the current notebook pipeline and intended dashboard integration. It is aligned with `code/main.ipynb` at commit `46e142f88e0e850c08be687425c209f27b415fd2`. Figures below are saved notebook outputs, not an independently reproduced training run. The notebook contains a stale-output warning that must be reconciled by a clean run before claiming full reproducibility.

## The eight stages

| # | Stage | Description |
|---|---|---|
| 1 | **Sources** | Homely sales; ABS population; NT-wide household income; RBA cash rate; Darwin CPI |
| 2 | **Clean and merge** | Coordinate and outlier filters; annual income/population lagged one year; cash rate matched by date |
| 3 | **Split preparation** | Imputation, suburb grouping and encoding refitted per split; upstream outlier thresholds reused |
| 4 | **Feature engineering** | Price momentum, rate direction and policy flags; final training sample weighting disabled |
| 5 | **Model comparison** | Linear Regression, Random Forest and XGBoost; time-aware tuning and feature comparisons |
| 6 | **Backtest** | 12 quarterly forecasts in 2023-2025; report upstream filtering and selection limitations |
| 7 | **Final model** | XGBoost + policy; saved output: 8,209 sales through December 2025; export model and metadata |
| 8 | **Dashboard integration** | Intended: price range, repayments, rate sensitivity and suburb comparison; deployment unverified |

## Data timing and cleaning

The five raw inputs are properties.csv, ERP.csv, annual_household_nt.csv, cash_rates.csv and cpi_index.csv under data/raw/. Household income is an NT-wide annual series (1990-2025), not suburb-level income. Annual population and income use a one-year lag; publication-date availability still requires validation. The saved cleaning output reports zero coordinate sign repairs and 209 exclusions outside the configured Greater Darwin bounding box. This is a scope filter, not proof that all excluded coordinates were wrong. The final cleaned dataset contains 8,209 sales.

## Split preparation and leakage limitations

prepare_split() refits imputation, land-area imputation, rare-suburb grouping and suburb encoding on each training split. However, price and land-area IQR thresholds are fitted upstream once using sales through 12 November 2024 and applied before rolling evaluation. Earlier backtests therefore reuse filtering information from later sales. Do not describe the whole pipeline as leakage-free. A future correction should fit these thresholds within each evaluation fold. The saved output also excludes 10% of test-period sales using the price/land filters, so reported errors describe a restricted population.

## Selected model and evaluation

The saved final-model output selects XGBoost with policy features, using 28 numeric and 3 categorical inputs, refitted on 8,209 sales through 31 December 2025. USE_RECENCY_WEIGHTS is False: model-fitting sample weights are disabled for final tuning, backtesting and refitting. Recency weighting was evaluated and its saved comparison raises pooled RMSE by 1.10%, helping 2 of 12 folds. Recency-weighted suburb encoding remains a separate mechanism. The 12-quarter backtest reports RMSE AUD 79,122.65, MAE AUD 57,114.42, MAPE 11.92% and R2 0.7993. Policy comparisons are predictive, not causal.

## Repository and generated artifacts

The reviewed branch contains code/main.ipynb, five data/raw/ CSV inputs, requirements.txt, README.md and documentation. It does not contain code/app.py or code/plots.ipynb. The notebook includes export code for the model bundle, metadata, metrics, predictions, dashboard reference and model card; generated outputs are not tracked on this branch. Export code alone does not establish that a deployment uses the current bundle.

## Dashboard integration and verification

The intended buyer journey covers property selection, a price estimate and nominal 80% interval, repayments, lender-rate sensitivity and suburb comparison. The proposed five tabs are Overview, Model performance, Diagnosis to Fix, Predict and Affordability, and Limitations. The previously documented deployment URL is https://data-science-practice.streamlit.app/; its current availability, source branch and model version have not been verified for this revision. Obtain the dashboard source and deployment commit from its owner before claiming that it uses the current model. The notebook exports context through December 2025; whether the live interface uses and discloses that context remains unverified. Repayment calculations are intended to exclude stamp duty, insurance and fees.

## Remaining work

Perform and record a clean notebook run; resolve stale narrative/output warnings; refit outlier rules within each backtest; validate annual-series publication timing; and verify dashboard source, deployment commit, exported model compatibility and displayed limitations. No live refresh or scheduled retraining is verified. Branch protection and mandatory review settings are not established by this documentation.

---
Last updated: 18 October 2026.
