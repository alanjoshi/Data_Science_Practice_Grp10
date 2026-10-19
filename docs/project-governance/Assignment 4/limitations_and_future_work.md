# Limitations and future work

Prepared for Lisa Vong (Ngoc Loi Vong), S392159  
Project: Housing Affordability Forecasting System for Greater Darwin

## Scope and evidence basis

This register consolidates limitations and future improvements from the supplied AT4 Report, particularly Sections 3.12 and 3.13. It records the effect of each limitation, the proposed response and a suggested acceptance check. These checks are proposals, not tests already executed by Lisa. Evidence descriptions refer to the report; exact repository locations and outputs require teammate verification before merge.

## Limitations register

| ID | Limitation and reported evidence | Practical effect | Proposed response and acceptance check | Status in supplied report |
| --- | --- | --- | --- | --- |
| L01 | Final model refitted on all 8,209 retained sales; pooled 12-quarter backtest RMSE $79,123, MAPE 11.9%, R² about 0.80 | No untouched test remains after final refitting. Backtest performance assumes quarterly refits. | Archive the final model and evaluate genuinely later sales before any next refit; record dates, sample size and errors. | Backtest completed; future-period confirmation outstanding |
| L02 | Market data ends 31 December 2025; rates, CPI and policy context are frozen | Predictions may not reflect subsequent market conditions. | Version refreshed inputs, record source and effective dates, and validate joins before refitting. | Automated/live refresh not started |
| L03 | No broad downturn validation in 2023–2025 | Intervals may be too optimistic during a fall. | Add historical downturn evidence where available and clearly labelled scenario stress tests; report error, bias and coverage. | Outstanding |
| L04 | Property type inferred from address; reported agreement 57–70% | An influential feature is imperfectly measured. | Obtain a more reliable source; assess agreement against verified labels and disclose unmatched records. | Better source open |
| L05 | Income context described as NT-wide, annual and lagged; affordability omits stamp duty, mortgage insurance and fees | Local income differences and total ownership costs are not fully represented. | Verify income fields in code, distinguish model inputs from affordability inputs, add suburb-level income and transparent optional cost assumptions. | More detailed inputs open |
| L06 | Policy flags overlap with the 2025 rate-cutting period; one lacks an out-of-sample check | Predictive association cannot establish a causal policy effect. | Keep association wording and evaluate later periods with adequate active/inactive coverage. | Limitation disclosed; further validation open |
| L07 | Model scope excludes sales outside $22,500–$1,002,500 and land above 1,651.5 m² | Estimates should not be generalised to excluded properties. | Display supported ranges, validate boundary inputs and document any extrapolation. | Scope restriction in place; boundary checks proposed |
| L08 | Improvements diagnosed in the same single window as the reported score | Single-window improvements may be optimistic. | Give rolling-backtest evidence priority; reserve future data for confirmation and log exploratory decisions. | Backtest completed; fresh confirmation outstanding |
| L09 | Refit is manual; no test suite or CI reported | Refresh may be missed and changes may introduce regressions. | Define an owner and quarterly refresh process; add focused prediction and affordability tests with CI. | Automation and CI open |
| L10 | Scraped-listing terms require review before redistribution | Reproducibility and sharing depend on permitted data access. | Record source permissions and provide permitted download instructions or non-sensitive examples. | Rights review outstanding |

## Completed mitigation versus residual risk

The report states that coordinate validation removed 209 records outside Greater Darwin and that the final preparation retained 8,209 records after the full cleaning process. Coordinate validation is therefore a reported completed mitigation, not an entirely unstarted future task. A future improvement is to validate coordinates on every refresh and check the resulting distance features. This document does not independently verify the removed records or claim that all 209 account for the net change from the Assessment 2 dataset.

The report also states that imputation, encoding and outlier fences are fitted using training data only. This is a reported control implemented by the technical team. Lisa's documentation contribution is to record the control and its evidence, not to claim authorship of that implementation.

## Proposed priorities

| Priority | Improvement | Suggested acceptance evidence |
| --- | --- | --- |
| High | Quarterly refit with stored metrics and drift checks | Named owner; dated run log; versioned inputs; stored metrics; matching model and reference artefacts |
| High | Refresh rates, CPI and policy context | Source dates; effective-date checks; dashboard timestamp; versioned assumptions |
| High | Focused unit tests and CI | Passing checks for affordability arithmetic, valid inputs and model save/load consistency |
| Medium | Better property type and suburb-level income | Coverage and agreement results; documented joins; segment evaluation |
| Medium | Downturn testing and interval validation | Clearly separated historical evidence and simulated scenarios; error and coverage summaries |
| Medium | External portal benchmark | Matched property/date sample and documented comparison methodology |
| Exploratory | Lagged regional unemployment | Suitable NT series with release dates; leakage-safe alignment; backtest comparison before adoption |

Priorities and acceptance checks are proposed here; owners and schedules require team agreement. No proposal is marked implemented by this document.

## Wording to resolve before final submission

Section 3.12 says “Income is not included” while elsewhere the report describes four NT income indicators in the feature set. Check the notebook and affordability module, then clarify which income measures are model features and which are affordability inputs. Do not repeat the ambiguous sentence as an established finding.

## Evidence to attach after review

Use the actual documentation commit, PR, linked Jira task and reviewed notebook/output locations. Generic repository links provide navigation but do not independently demonstrate individual authorship.
