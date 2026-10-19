# Project governance and evidence traceability

Prepared for Lisa Vong (Ngoc Loi Vong), S392159  
Project: Housing Affordability Forecasting System for Greater Darwin  
Assessment: PRT661 Assessment 4

## Purpose and evidence basis

This document consolidates the governance controls described in the supplied AT4 Report, especially Sections 3.10, 3.12 and 3.13. It connects reported technical decisions to their rationale and remaining actions. It is a documentation contribution; it does not attribute implementation of the modelling pipeline, architecture or dashboard to Lisa.

The repository and Jira history have not been independently inspected for this document. Notebook sections, artefact locations and numerical results below are reported in AT4 Report and must be checked against the current repository before this document is merged. A completed documentation review is distinct from a completed implementation or executed test.

## Team responsibilities reported in the final report

| Member | Reported contribution |
| --- | --- |
| Lisa Vong | Governance documentation; consolidation of limitations and future improvements; associated contribution summaries |
| Roshan Neupane | Final modelling pipeline, evaluation, model card and dashboard code |
| Bipana Tripathee | Architecture, shared preparation function and dashboard journey design |
| Aashish Sharma | Deployment, readiness and ethics documentation; report integration |
| Alan Joshi John | Final contribution summary is blank in the supplied team table; confirm with the contributor before completing it |

## Governance controls

| Control | Evidence reported in AT4 Report | Purpose and remaining boundary |
| --- | --- | --- |
| Chronological evaluation | Date split at 12 November 2024; train-only fitting; 12-quarter rolling backtest | Reduce leakage and evaluate repeated quarterly refitting. Final all-data refit is not an untouched test. |
| Explicit adoption rules | Recency weights required more than 1% improvement and benefit in at least 7 folds; rejected after RMSE worsened by 1.10%, helping only 2 of 12 folds | Record rejected changes as well as retained changes. |
| Model documentation | MODEL_CARD.md and 57-item audit trail | Explain intended use, evidence, decisions and limitations. Confirm their tracked paths; generated output is reported as ignored by Git. |
| Feature uncertainty disclosure | Inferred property-type agreement reported as 57–70% | Disclose weak measurement rather than treating an inferred field as verified ground truth. |
| Selection and confirmation | Report describes earlier-fold selection and later-fold confirmation | Preserve the evaluation sequence and distinguish exploratory diagnosis from confirmation. |
| Release artefact consistency | Model bundle and app_reference.json must originate from the same run | Prevent dashboard context from being paired with a different model. |
| Refresh responsibility | Quarterly refit assumption; manual refresh; stale-model warning | A warning does not constitute automated monitoring or retraining. |
| Work tracking | Jira and GitHub referenced in the report | Link an individual's actual issues, commits and PRs rather than relying solely on the project homepage. |

## Proposed workflow for this documentation change

1. Create a Jira task describing the governance and limitations review, assigned to the person carrying it out.
2. Add these documents on a personal branch and make a descriptive commit using the contributor's own account.
3. Open a PR that links the Jira task and identifies the report sections reviewed.
4. Ask a relevant teammate to verify numerical claims, paths and completion statuses against the current code and outputs.
5. Resolve review comments and retain the PR discussion as evidence of review.
6. Add the actual PR, commit and Jira links to the individual contribution page and team evidence table.

This workflow is proposed for this change; it is not a claim that historical PR approvals or Jira transitions have already occurred.

## Completion criteria

- Each technical statement can be traced to an actual file, result or report section.
- Implemented controls and proposed improvements have different statuses.
- Individual attribution matches the work performed.
- Report wording and documentation agree on the final data, model and evaluation.
- Direct evidence links are added after the corresponding issues and PR exist.

## Project references

- [Project repository](https://github.com/alanjoshi/Data_Science_Practice_Grp10)
- [Jira project board](https://vongngocloi.atlassian.net/jira/software/projects/PDSPDT/boards/38/backlog)
- AT4 Report.docx: Sections 3.3, 3.5–3.13 and team contribution summary.
