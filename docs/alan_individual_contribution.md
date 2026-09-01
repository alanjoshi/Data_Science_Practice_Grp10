# Alan Joshi John - Individual Contribution

## Role

Data Engineer

## Contribution Summary

My contribution focused on supporting data acquisition, raw data storage, processed data preparation, workflow/data pipeline design, and GitHub repository organisation for the Housing Affordability Forecasting System for the Greater Darwin Region.

The main property sales dataset was collected by Roshan from Homely. My datasets support that main dataset by adding ABS population density, income, rent, and household context for Northern Territory and Greater Darwin suburb-level analysis.

## Work Completed

- Uploaded the raw ABS population components workbook used to extract Northern Territory population density data.
- Uploaded the raw ABS 2021 Census General Community Profile SAL DataPack used to prepare suburb-level income and household features.
- Uploaded the processed Northern Territory population density dataset.
- Uploaded the processed ABS Census suburb income and household features dataset.
- Organised my files into the `data/raw` and `data/processed` folders in the GitHub repository.
- Identified additional ABS personal income tables for 2018-19 to 2022-23 as possible time-based income context for later project work.
- Contributed workflow and data pipeline design evidence from Assignment 1 for use in Assignment 2.
- Supported GitHub repository organisation by checking file placement against the README structure.

## Uploaded Evidence

- `data/raw/abs_population_components_2024_2025.xlsx`
- `data/raw/abs_2021_gcp_sal_nt_short_header.zip`
- `data/processed/Population density -NT.xlsx`
- `data/processed/abs_census_nt_suburb_income_household_features.csv`
- `docs/workflow/Workflow Diagram(PRT661).drawio`
- `docs/architecture/Data_pipeline_data_science_practice_xx.drawio`

## Pending / Team Discussion

- Roshan's Homely property sales dataset is the main modelling dataset.
- My ABS datasets are supporting datasets for demographic and affordability context.
- The 2021 Census income and household dataset is a Census-year snapshot, so it should be treated as static suburb-level context unless the team agrees to add newer income time-series data.
- Additional ABS personal income tables for 2018-19 to 2022-23 may help with yearly income trends, but they measure personal income rather than household income.

## Relevance To Project

The ABS population density dataset helps provide geographic and demographic context for Greater Darwin suburbs. The ABS Census income and household features dataset adds suburb-level affordability indicators such as median household income, median rent, household size, and income distribution. These supporting datasets can be combined with the main Homely property sales dataset to improve modelling, affordability analysis, and dashboard visualisations.
