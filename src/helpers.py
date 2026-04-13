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

def drop_metadata_columns(df):
    """Remove columns that are note useful for analysis
    Parameters: 
        df: A pandas DataFrame
    Returns:
        Dataframe with unnecessary columns removed.
    """
    df = df.copy()
    columns_to_drop = ["Dguid", "Statistics", "Uom", "Uom Id", "Scalar Factor",
        "Scalar Id", "Vector", "Coordinate", "Status", "Symbol",
        "Terminated", "Decimals"]
    df = df.drop(columns = columns_to_drop, errors="ignore")
    return df