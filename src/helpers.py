import pandas as pd

def clean_column_names(df):
    """Standarize column names.
    Parameters:
        df: A pandas Dataframe
    Returns:
        DataFrame with cleaned column names
    """
    df = df.copy()
    df.columns = [column.lower().replace('_', ' ').title() for column in df.columns]
    return df

