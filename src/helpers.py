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

def rename_columns(df):
    """Rename columns to simpler names
    Parameters:
        df : A pandas Dataframe
    Returns: 
        Dataframe with renamed columns
    """
    df = df.copy()
    df = df.rename(columns = {
        "Ref Date": "Year",
        "Geo": "Region",
        "Tenure Including First-Time Homebuyer And Social And Affordable Housing Status": "Tenure",
        "Acceptable Housing": "Housing Status",
        "Value": "Percentage"
    })
    return df

def add_tenure_group(df):
    """Create a simplified tenure group column.
        Parameters:
            df: A pandas DataFrame
        Returns:
            DataFrame with a new simplified tenure group column.
    """
    df = df.copy()

    df["Tenure Group"] = df["Tenure"].replace({
        "Total, by tenure": "Total",
        "Owner household": "Owner",
        "Owner household, first-time homebuyer": "Owner",
        "Owner household, not first-time homebuyer": "Owner",
        "Renter household": "Renter",
        "Renter not in social and affordable housing": "Renter",
        "Renter in social and affordable housing": "Renter"
    })

    return df
    