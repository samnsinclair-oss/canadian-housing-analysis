# Housing Conditions in Canada Analysis

A Python data-analysis project examining differences in acceptable housing conditions between renters and homeowners across Canadian provinces in 2021 and 2022.

## Project Overview

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

## Author

Sam Sinclair
Data Science and Machine Learning student at RRC Polytech
