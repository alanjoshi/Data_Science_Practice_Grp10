# Project Change Log

## Purpose

This document records significant changes made after Assessment 1. The core objective remained unchanged: to analyse and predict Greater Darwin residential property prices. The changes improved technical validity, data compatibility, traceability, and consistency between implementation and reporting.

## Significant Change Register

| ID | Change Area | Assessment 1 Plan | Final Implementation | Justification and Impact | Owner | Status | Evidence |
|---|---|---|---|---|---|---|---|
| CHG-01 | Cloud specification | Generic cloud database | AWS S3, Glue Data Catalog, and Athena | Clarified the services actually implemented and improved documentation accuracy. | Alan Joshi John | Completed | AWS evidence, architecture, Jira, and report |
| CHG-02 | Income data | Single-year 2021 Census household-income snapshot | NT Annual Household Income Accounts covering 1990–2025 | Provided continuous annual context and 100% year matching; variables remain NT-wide rather than suburb-level. | Alan and Roshan | Completed | Source data and `main.ipynb` Sections 2.3, 3.2, and 5 |
| CHG-03 | Population data | Census population by SA2 | Greater Darwin ERP merged by sale year | Avoided unreliable SA2-to-suburb matching and achieved 100% year matching. | Alan and Roshan | Completed | ERP data and `main.ipynb` Sections 3.3 and 5 |
| CHG-04 | Modelling scope | Regression and classification without clear priority | Property-price regression became primary; affordability remained decision-support context | Clarified the objective and aligned the workflow, modelling, and dashboard. | Roshan and team | Completed | Workflow, architecture, notebook, and report |
| CHG-05 | Validation | Final temporal controls not specified | 80/20 chronological split and TimeSeriesSplit tuning | Prevented future-data leakage and produced a more realistic evaluation. | Roshan Neupane | Completed | `main.ipynb` Sections 6–10 |
| CHG-06 | Preprocessing leakage | Preprocessing stage not explicitly controlled | Split first; fit imputation and transformation only on training data | Prevented test-period information from influencing model training. | Roshan Neupane | Completed | Notebook and risk register |
| CHG-07 | Target leakage | `price_per_sqm` available among potential predictors | Removed from all predictor variables | The variable contains target-price information and could artificially inflate performance. | Roshan Neupane | Completed | Notebook, feature list, and risk register |
| CHG-08 | Economic and temporal features | Rate, momentum, and recency features not planned explicitly | Added RBA variables, rate direction, price momentum, and recency weighting | Addressed 2025 underprediction; enhanced Linear Regression R² improved from 0.5374 to 0.6628. | Roshan Neupane | Completed | `main.ipynb` Sections 11 and 14 |
| CHG-09 | Dashboard workflow | Build Power BI only after modelling | Prototype in `plots.ipynb`, then integrate reviewed outputs into Power BI | Allowed visual work during upstream corrections and improved final consistency. | Aashish Sharma | Completed | `plots.ipynb`, Power BI, and PDSPDT-28 |
| CHG-10 | Repository control | Shared GitHub repository without detailed controls | Individual branches, protected main, and pull-request reviews | Improved traceability and reduced unreviewed integration. | Alan and contributors | Completed | GitHub settings, commits, and pull requests |
| CHG-11 | Final progress status | Some tasks previously remained open | Updated status to 37 Done and zero in every other category | All planned work was completed before final report integration. | Lisa Vong | Completed | Final Jira export and Section 3.12 |
| CHG-12 | Governance documentation | Evidence distributed across Jira and report notes | Consolidated four governance Markdown files | Improved transparency and connected responsibilities, decisions, outputs, and evidence. | Lisa Vong | Completed | Governance files, Jira, GitHub, and report |

## Change-Control Process

1. Identify the data, technology, modelling, workflow, scope, or governance issue.
2. Assess its impact on quality, scope, schedule, and dependencies.
3. Discuss possible solutions with affected members.
4. Approve the preferred solution.
5. Update Jira, documentation, architecture, workflow, or report content.
6. Implement, test, and review the change.
7. Retain supporting evidence in Jira, GitHub, AWS, notebooks, datasets, dashboards, or report sections.
8. Record the final status and impact in this change log.

## Final Evaluation

All significant changes were approved, implemented, and evidenced. AWS remained part of the project and was documented more precisely. Data-source changes improved merge reliability, modelling changes prevented leakage and improved evaluation validity, and governance changes strengthened traceability. These changes refined the implementation without replacing the original project objective.
