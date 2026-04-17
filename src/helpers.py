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

def simplify_tenure(df):
    """Shorten tenure labels while keeping important meaning
        Parameters:
            df: A pandas DataFrame
        Returns:
            DataFrame with a simplified tenure column
    """
    df = df.copy()

    df["Tenure"] = df["Tenure"].replace({
        "Total, by tenure": "Total",
        "Owner household": "Owner",
        "Owner household, first-time homebuyer": "Owner (First-time)",
        "Owner household, not first-time homebuyer": "Owner (Not first-time)",
        "Renter household": "Renter",
        "Renter not in social and affordable housing": "Renter (Non-social)",
        "Renter in social and affordable housing": "Renter (Social)"
    })

    return df

def simplify_housing_status(df):
    """Shorten housing status labels
        Parameters:
            df: A pandas DataFrame
        Returns:
            DataFrame with a simplified tenure column
    """
    df = df.copy()

    df["Housing Status"] = df["Housing Status"].replace({
        "Does not live in acceptable housing": "Not Acceptable",
        "Lives in acceptable housing": "Acceptable"
    })

    return df

def filter_provinces(df):
    """Return only the provincial rows from the dataset.
    Parameters:
        df: A Pandas Dataframe
    Returns:
        Dataframe containing only province rows.
    """
    df = df.copy()

    provinces = [
        "Newfoundland and Labrador",
        "Prince Edward Island",
        "Nova Scotia",
        "New Brunswick",
        "Quebec",
        "Ontario",
        "Manitoba",
        "Saskatchewan",
        "Alberta",
        "British Columbia"]
    
    df = df[df["Region"].isin(provinces)]
    
    return df