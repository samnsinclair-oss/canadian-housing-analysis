# Assignment3_comp2040

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