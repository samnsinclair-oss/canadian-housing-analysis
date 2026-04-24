# Assignment3_comp2040
## By Sam Sinclair

# Housing Conditions in Canada Analysis

## Project Summary

This project analyzes housing conditions across Canada using public open data. The focus is on comparing unacceptable housing between renters and homeowners across provinces and over time. 

The analysis shows that renters consistently experience higher rates of unacceptable housing compared to homeowners. It also explores how this gap varies by region, with provinces like Ontario showing larger differences, while others like Quebec and New Brunswick show smaller gaps. Changes between 2021 and 2022 are also examined, including notable improvements in places like Prince Edward Island.

A simple prediction model is included to estimate housing percentages based on region, tenure, housing status, and year.

---

## How to Run the Analysis

- Download or clone the project folder.
- Make sure Python is installed.
- Install the required libraries:
  - pandas
  - matplotlib
  - seaborn
  - scikit-learn
- Open `notebooks/analysis.ipynb` in Jupyter Notebook or JupyterLab.
- Run all cells from top to bottom.

- The helper module is located in `src/helpers.py` and is imported into the notebook.
- Do not change the folder structure, as the notebook depends on this file location.


---

## Helper Module

The helper module contains functions used to clean and prepare the dataset:

- `clean_column_names()` – standardizes column formatting  
- `drop_metadata_columns()` – removes unnecessary columns  
- `rename_columns()` – simplifies column names  
- `add_tenure_group()` – creates grouped tenure categories  
- `simplify_tenure()` – shortens tenure labels  
- `simplify_housing_status()` – simplifies housing status labels  
- `filter_provinces()` – filters dataset to include only provinces  

These functions are imported into the notebook and used during the data cleaning process.

---

## Prediction Model

A linear regression model was used to predict the percentage of people living in unacceptable housing.

- RMSE ≈ 14.5  
- R² ≈ 0.53  

The model captures some patterns in the data but is not highly accurate. This is likely due to the limited size of the dataset and the lack of additional variables such as income or location.

---

## Key Findings

- Renters have higher rates of unacceptable housing in every province  
- The size of the gap between renters and homeowners varies by region  
- Ontario shows the highest levels, while Newfoundland and Labrador shows the lowest  
- Prince Edward Island shows a strong improvement over time, while Quebec shows mixed changes  
- Differences in renter housing conditions drive most of the inequality  

---

## Repository Structure

- `data/housing2022.csv` – contains the dataset used for analysis  
- `notebooks/analysis.ipynb` – main analysis notebook  
- `src/helpers.py` – helper functions for data cleaning  
- `README.md` – project documentation  

---

## Notes

This project is based on a limited dataset (2021–2022) and does not include all factors that may influence housing conditions. Further analysis could include more years and additional variables.






---

## Notes after first check in

I was asked what does the 28 rows per region mean? When I focused on one region "Manitoba"
I saw that it was divided into Tenure groups and if it were acceptable housing or not
- 2 years (2021,2022)
- 7 Tenure categories 
- 2 housing status categories (acceptable/non acceptable)

The result is 2 x 7 x 2 = 28 rows per region

## Metadata columns

Several columns in the dataset were indentified as metadeta and removed
- DGUID : geographic ID code
- VECTOR: internal table reference code
- COORDINATE: position in multidimensional table
- UOM, SCALAR: units(unit of measure) and scaling factor(how values are stored/displayed)
- STATUS, SYMBOL: data quality flags (NaN for both)

These columns are used by Statistics Canada for data organization, identification, and 
formatting, and they do not provide meaningful information for analysis.

## Aggregated Dataset

This dataset comes from the Canadian Housing Survey and is already aggregated. The values
represent percentages rather than raw individual-level data

This means
- each row represents a summarized group
- the dataset cannot be used for individual-level analysis
- Analysis is limited to comparing patterns between groups

Although the dataset is aggregated, it still supports meaningful analysis by allowing comparisons across groups. This makes it possible to identify patterns in acceptable housing based on region, tenure type, and time.