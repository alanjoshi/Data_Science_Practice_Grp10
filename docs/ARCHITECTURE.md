# System Architecture

**Bipana Tripathee** (S388875)
*System Architecture Lead*

Greater Darwin Property-Price Forecasting System — Group Dan1-Theme2

## Purpose

This document describes the current eight-stage pipeline architecture. It was redesigned following Assessment 2 feedback indicating that the original workflow diagram lacked clarity, and is intended to serve as the authoritative reference for how data moves through the system, from acquisition through to the buyer-facing dashboard.

## The Eight Stages

| # | Stage | Description | Output |
|---|---|---|---|
| 1 | **Sources** | Homely property sales, ABS Estimated Resident Population, ABS Household Income (NT-wide, 1990–2025), RBA cash rate, Darwin CPI | Five raw datasets |
| 2 | **Clean & merge** | Each dataset cleaned individually, then merged by year (or by sale date for the cash rate) | One merged, raw-clean table |
| 3 | **Train-only preparation** | Gap-filling, rare-suburb grouping, and suburb encoding — all fitted on training rows only, so nothing leaks from the future | Leak-safe prepared table |
| 4 | **Feature engineering** | Price momentum, interest-rate direction, and recency weighting added on top of the cleaned base features | Model-ready feature set |
| 5 | **Model training** | Linear Regression, Random Forest, and XGBoost trained and tuned with time-aware cross-validation | Three candidate models |
| 6 | **Backtest** | Twelve quarterly forecasts, each one using only sales that happened before that quarter | Backtest error per model |
| 7 | **Final model** | XGBoost, refit on all 8,296 cleaned sales after being selected by the backtest | Saved model bundle |
| 8 | **Dashboard** | Turns the saved model into a price estimate, an 80% range, repayments, rate sensitivity, and suburb comparison | Buyer-facing prediction |

## Design Rationale: Re-runnable Pipeline

The shared prepare-split function is structured so that every learned step (imputation, suburb encoding, rare-category grouping) is **re-fitted on training rows only**, every time the pipeline runs — not fitted once and reused. This is what makes it possible to:

- Re-run the whole pipeline at a different cutoff date without hand-editing anything
- Test the 4-cutoff robustness checks used in the modelling section
- Run the 12-quarter rolling-origin backtest, where each fold needs its own clean train/test split

## Dashboard Design

The dashboard was designed around a single buyer journey, split into five screens:

1. **Choose a property** — suburb, type, beds, baths, cars, land area
2. **Price and range** — the model's estimate plus the measured 80% range
3. **Repayments** — deposit, loan, weekly/monthly repayment, repayment-to-income
4. **Rate sensitivity** — test different lender margins against the 30% stress line
5. **Suburb comparison** — same property and income, compared across every suburb

Underneath these, the dashboard has five tabs: Overview, Model performance, Diagnosis to Fix, Predict and Affordability, and Limitations.

## Known Limitation

The dashboard's market context (most recent sale, interest rate, CPI) is **frozen at the last training sale date (December 2025)** rather than updating in real time. This constraint is disclosed directly on screen rather than concealed, and is recorded as priority item five in the Assessment 4 work plan (retrain on new sales and refresh market context).

---
*Last updated: October 2026*
