# Project Planning

## Project Overview

**Project title:** Greater Darwin Residential Property Price Analysis and Prediction  
**Project objective:** Develop a data-driven system for analysing and predicting residential property prices in Greater Darwin using property, population, household-income, economic, and geographical data.

The project combines AWS-supported data management, data engineering, machine-learning modelling, visualisation, and project governance. AWS S3 was used for storage, AWS Glue Data Catalog for metadata management, AWS Athena for SQL querying, Python and Jupyter Notebook for processing and modelling, and Power BI for dashboard delivery.

## Project Objectives

1. Collect and validate relevant property and socioeconomic data.
2. Store and organise raw and processed data using AWS services.
3. Clean, standardise, and integrate the collected datasets.
4. Develop a leakage-controlled machine-learning pipeline.
5. Train and compare Linear Regression, Random Forest, and XGBoost.
6. Evaluate models using RMSE, MAE, R², and MAPE.
7. Build a Power BI dashboard for market analysis and decision support.
8. Maintain transparent task allocation, risk management, change control, and supporting evidence.
9. Complete and review all deliverables before submission.

## Project Scope

### In Scope

- Greater Darwin residential property transactions from 2006 to 2025.
- Property, population, NT household-income, RBA cash-rate, and geographical data.
- AWS S3, Glue Data Catalog, and Athena.
- Data cleaning, integration, feature engineering, and validation.
- Regression-based property-price prediction.
- Model comparison and performance evaluation.
- Power BI dashboard development.
- Jira monitoring, GitHub version control, governance records, and final reporting.

### Out of Scope

- Real-time price prediction.
- Automated purchasing or investment decisions.
- Individual financial advice.
- Personally identifiable information.
- Locations outside Greater Darwin.

## Sprint Plan

| Sprint | Main Activities | Planned Tasks | Final Status |
|---|---|---:|---|
| Sprint 1 – Planning | Establish scope, objectives, Jira, GitHub, timeline, and initial risks. | 3 | Completed |
| Sprint 2 – Research and Design | Review sources and design storage, architecture, pipeline, and workflow. | 5 | Completed |
| Sprint 3 – Assessment 1 | Complete proposal content, evidence, review, and submission checks. | 8 | Completed |
| Sprint 4 – Technical Setup | Update AWS architecture, acquisition, pipeline, allocation, and risks. | 4 | Completed |
| Sprint 5 – Data Processing | Clean and merge data, test the pipeline, and develop three models. | 4 | Completed |
| Sprint 6 – Evaluation | Evaluate models, complete the dashboard, organise GitHub, and finalise governance. | 5 | Completed |
| Sprint 6 – Report Integration | Complete contributions, integrate the report, and verify evidence links. | 8 | Completed |
| **Total** | **All planned project activities** | **37** | **Completed – 100%** |

## Key Deliverables

| Deliverable | Completion Criteria | Final Status |
|---|---|---|
| Cleaned property dataset | Invalid, duplicate, incomplete, and inconsistent records processed. | Completed |
| Integrated dataset | Property, population, income, RBA, and geographical data merged successfully. | Completed |
| Model-ready dataset | Features prepared without target or future-data leakage. | Completed |
| Predictive models | Linear Regression, Random Forest, and XGBoost trained and evaluated. | Completed |
| Power BI dashboard | Reviewed market, prediction, and model results presented interactively. | Completed |
| Governance records | Planning, allocation, progress, risks, and changes documented. | Completed |
| Final report | Technical results, evidence, and individual contributions integrated. | Completed |

## Final Technical Results

- Raw property records: **15,423**
- Model-ready transactions: **8,336**
- Training records: **6,674**
- Test records: **1,662**
- Validation: **80/20 chronological split and TimeSeriesSplit tuning**
- Best final model: **Enhanced Linear Regression**
- RMSE: **$104,813.56**
- MAE: **$74,116.70**
- R²: **0.6628**
- MAPE: **16.54%**

## Governance and Monitoring

Jira was used to allocate and monitor tasks. GitHub recorded branches, commits, pull requests, reviews, and individual contributions. Technical completion was verified using notebooks, datasets, AWS evidence, Power BI outputs, GitHub history, and report content. Significant changes were documented in `Change_Log.md`.

## Final Status

All 37 Jira tasks were completed. No tasks remained In Progress, In Review, or To Do. The project reached the final submission stage with all principal deliverables completed.
