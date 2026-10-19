Assessment 4 Data Quality Checklist

## Purpose

This checklist records the data-quality checks that should be completed before the model is re-run for Assessment 4. The priority is to fix known issues that may affect distance features, property-type features, model evaluation and dashboard outputs.

## Priority Checks

### 1. Coordinate validation

Some listings produced impossible distances from the Darwin CBD. Before re-running the model, property coordinates should be checked against a Greater Darwin boundary and a maximum distance rule.

Recommended checks:

- Flag rows with missing latitude or longitude.
- Flag coordinates outside a Greater Darwin bounding box.
- Recompute distance from the Darwin CBD after invalid coordinates are corrected or removed.
- Compare the maximum, minimum and median distance before and after the fix.
- Re-run the train/test split and backtest after distance values are corrected.

Expected outcome:

- Impossible distance values are removed or corrected.
- The distance feature better represents real Greater Darwin locations.
- Updated model results can be compared against the current Assessment 3 results.

### 2. Property-type validation

The current property-type signal is derived from available text fields and is only partly consistent. A stronger type signal is needed before the next model update.

Recommended checks:

- Compare address-derived property type against land-area availability.
- Flag records where the two signals disagree.
- Create a clear category for unknown or unreliable property type.
- Investigate whether an external or manually checked property-type field can be added.
- Add a new-versus-established flag if a reliable source can be found.

Expected outcome:

- Property type is less dependent on address text guessing.
- Model inputs better represent differences between houses, units and townhouses.
- The dashboard can explain property-type limitations more clearly.

### 3. Market-context refresh

The current dashboard context is frozen at the last training sale in December 2025. Assessment 4 should refresh the model and dashboard context if newer sales or market data are available.

Recommended checks:

- Add any newer property sales before retraining.
- Refresh cash-rate, CPI, income and population inputs if newer values are available.
- Re-run the model pipeline after data refresh.
- Update dashboard reference tables after the final model is selected.
- Clearly record the latest data date shown in the dashboard.

Expected outcome:

- Dashboard outputs reflect the latest available project data.
- Users can see the period covered by the model.
- Limitations about frozen market context are reduced or updated.

### 4. Result consistency checks

Before submission, reported figures should be checked across the notebook, presentation, dashboard and report.

Recommended checks:

- Confirm the final modelling row count.
- Confirm train/test or backtest counts.
- Confirm RMSE, MAPE and R-squared values.
- Confirm the 80 percent prediction range used in the dashboard.
- Confirm that dashboard numbers match the exported model outputs.
- Keep separate labels for single test-window results and rolling backtest results.

Expected outcome:

- Presentation and report numbers match the final notebook outputs.
- The dashboard does not show outdated values.
- Technical claims are easier to defend during the demonstration.

## Assessment 4 Order Of Work

1. Run coordinate checks and fix invalid location records.
2. Recompute distance from the CBD.
3. Review and improve property-type features.
4. Refresh market data if newer files are available.
5. Re-run the full modelling pipeline.
6. Re-run the backtest and select the final model again.
7. Update dashboard reference tables.
8. Check that all report and presentation numbers match the final outputs.

## Evidence To Retain

- Before-and-after coordinate summary.
- Number of rows flagged by each data-quality check.
- Updated modelling row count.
- Updated model metrics.
- Updated dashboard screenshots.
- Notes explaining any data-quality issues that remain unresolved.
