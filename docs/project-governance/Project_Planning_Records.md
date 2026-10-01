# Project Planning Records

## Purpose

This document records project reviews, decisions, progress updates, and final completion. It demonstrates how the team monitored the project and responded to technical findings after Assessment 1.

## 1. Project Initiation Review

**Topics reviewed:** Project objectives, Greater Darwin scope, data requirements, team roles, Jira, GitHub, timeline, and initial risks.

**Decisions:**

- Property-price regression would be the primary analytical objective.
- Jira would manage task allocation and progress.
- GitHub would support version control and contribution evidence.
- AWS would support storage, catalogue management, and querying.
- Every activity would have an accountable owner.
- Risks and significant changes would be documented.

**Outcome:** The team established the initial scope, responsibilities, tools, and planning baseline.

## 2. Research and Design Review

**Topics reviewed:** Property data, population and income indicators, RBA data, geographical features, AWS services, architecture, workflow, and integration risks.

**Decisions:**

- Use AWS S3 for raw and processed storage.
- Use AWS Glue Data Catalog for metadata management.
- Use AWS Athena for SQL querying and validation.
- Align annual socioeconomic variables with transactions by sale year.
- Retain raw data separately from processed data for traceability.

**Outcome:** The team documented the data sources, architecture, and end-to-end workflow.

## 3. Assessment 1 Review

**Topics reviewed:** Proposal completeness, objectives, data sources, technologies, modelling workflow, timeline, risks, and evidence.

**Decisions:**

- Assessment 1 would serve as the planning baseline.
- Significant later changes would require justification and evidence.
- Generic technology descriptions would be replaced with implemented tools.
- Changes would be recorded in `Change_Log.md`.

**Outcome:** Assessment 1 was completed and retained as the baseline for progress evaluation.

## 4. Technical Setup Review

**Topics reviewed:** AWS implementation, data acquisition, pipeline design, GitHub controls, task allocation, and technical risks.

**Decisions:**

- Explicitly identify S3, Glue Data Catalog, and Athena.
- Use individual GitHub branches and pull-request reviews.
- Exclude credentials and API keys from the public repository.
- Require evidence for completed Jira tasks.

**Outcome:** Technical design, repository controls, and responsibilities were aligned with implementation.

## 5. Data Processing Review

**Topics reviewed:** Missing values, duplicates, formats, suburb consistency, dataset integration, temporal coverage, and leakage risks.

**Decisions:**

- Remove invalid or unusable records using documented rules.
- Merge annual socioeconomic variables by sale year.
- Use Greater Darwin ERP instead of unreliable SA2-to-suburb matching.
- Use NT Annual Household Income Accounts instead of a single-year snapshot.
- Split chronologically before imputation and transformation.
- Fit preprocessing only to the training data.
- Exclude `price_per_sqm` from predictors.

**Outcome:** The pipeline transformed 15,423 raw records into 8,336 model-ready transactions and implemented appropriate leakage controls.

## 6. Model Development and Evaluation Review

**Topics reviewed:** Chronological splitting, three models, TimeSeriesSplit, evaluation metrics, recent-price underprediction, and temporal feature improvements.

**Decisions:**

- Use an 80/20 chronological split: 6,674 training and 1,662 test records.
- Evaluate Linear Regression, Random Forest, and XGBoost.
- Consider RMSE, MAE, R², and MAPE together.
- Add economic and temporal features to improve recent predictions.
- Select Enhanced Linear Regression as the strongest valid final model.

| Metric | Final Result |
|---|---:|
| RMSE | $104,813.56 |
| MAE | $74,116.70 |
| R² | 0.6628 |
| MAPE | 16.54% |

**Outcome:** Three models were evaluated, and Enhanced Linear Regression was selected after leakage correction and feature enhancement.

## 7. Dashboard Review

**Decisions:**

- Prototype visualisations in `plots.ipynb`.
- Integrate only reviewed data and model outputs into Power BI.
- Check dashboard results against the final notebook.
- Retain screenshots and task references as evidence.

**Outcome:** The visualisation prototype and Power BI dashboard were completed and aligned with reviewed outputs.

## 8. Final Governance and Report Review

**Topics reviewed:** Jira status, GitHub organisation, governance records, changes, risks, contributions, references, evidence links, and technical consistency.

**Decisions:**

- Check completed Jira tasks against evidence.
- Verify report values against `main.ipynb`.
- Summarise significant changes in Sections 3.8 and 3.12.
- Verify Jira, GitHub, AWS, notebook, dataset, and dashboard evidence.

**Outcome:** All 37 tasks were confirmed as Done. No tasks remained In Progress, In Review, or To Do. The report and supporting evidence were prepared for submission.

## Final Progress Summary

| Jira Status | Tasks | Percentage |
|---|---:|---:|
| Done | 37 | 100% |
| In Progress | 0 | 0% |
| In Review | 0 | 0% |
| To Do | 0 | 0% |
| **Total** | **37** | **100%** |
