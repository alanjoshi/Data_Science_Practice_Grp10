# PRT661 – Housing Affordability Forecasting System

**Assessment 2 · Group Dan1-Theme2 · Theme 2 — Predictive Analytics and Forecasting**

Forecasting Darwin house prices from property sales data, combined with population, household
income, and RBA cash rate data.

## Project Structure

```
project/
├── notebooks/
│   └── main.ipynb
├── data/
│   ├── raw/            # original files, untouched
│   ├── processed/      # cleaned individual files
│   ├── model_ready/     # final merged table used for modelling
│   └── output/          # predictions, saved models, metrics
```

The notebook expects to be run from a `notebooks/` folder, with `data/` as a sibling folder
(`PROJECT_DIR = Path("..")`). All output folders are created automatically if they don't exist.

## Input Data

Place these four files in `data/raw/` before running:

| File | Description |
|---|---|
| `properties.csv` | Property sales records (price, beds, baths, location, sale date, etc.) |
| `ERP.csv` | ABS Estimated Resident Population for Greater Darwin, one row per year |
| `Annual_Household_NT.csv` | Northern Territory annual household income, one row per year |
| `cash_rates.csv` | RBA cash rate target history, one row per rate change |

## What the Notebook Does

1. **Load** the four raw files.
2. **Explore (EDA)** each one to find data quality issues — missing values, bad formatting,
   inconsistent columns, etc.
3. **Clean** each dataset based on what the EDA found.
4. **Re-run EDA** to confirm the cleaning worked.
5. **Engineer features** — distance from Darwin CBD, sale year/month, property type, etc.
6. **Merge** everything into one table.
7. **Split into train/test by time** (not randomly), since this is a forecasting problem.
8. **Fill in missing values** using training-set statistics only, to avoid data leakage.
9. **Train and compare models**, then dig into where and why predictions go wrong.
10. **Export** predictions, evaluation metrics, and saved model files to `data/output/`.

A running list of data-quality findings ("saw this → did this about it") is logged throughout
the notebook and printed in full near the end, as a simple audit trail.

## Requirements

Install with:

```bash
pip install -r requirements.txt
```

## Running

Open `main.ipynb` in Jupyter and run all cells from top to bottom