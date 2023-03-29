def get_max_return(df):
    """
    Get the highest return for each instrument

    Args:
        df (pd.DataFrame): Dataframe containing the data

    Returns:
        pd.DataFrame: Dataframe containing the highest return for each instrument
    """
    return df.groupby("Instrument").max().sort_values("Return [%]", ascending=False)

def get_min_return(df):
    """
    Get the lowest return for each instrument

    Args:
        df (pd.DataFrame): Dataframe containing the data

    Returns:
        pd.DataFrame: Dataframe containing the lowest return for each instrument
    """
    return df.groupby("Instrument").min().sort_values("Return [%]", ascending=True)

def get_max_return_duration(df):
    """
    Get the highest return for each instrument in a specific smallest duration

    Args:
        df (pd.DataFrame): Dataframe containing the data

    Returns:
        pd.DataFrame: Dataframe containing the highest return for each instrument in a specific smallest duration
    """
    return (
        df.groupby("Instrument")
        .max()
        .sort_values("Return [%]", ascending=False)
        .sort_values("Duration", ascending=True)
    )

# get the highest return for each instrument for a strategy

def get_max_return_strategy(df):
    """
    Get the highest return for each instrument for a strategy

    Args:
        df (pd.DataFrame): Dataframe containing the data

    Returns:
        pd.DataFrame: Dataframe containing the highest return for each instrument for a strategy

    """
    df[df["Strategy"] == "Ema"].groupby("Instrument").max().sort_values("Return [%]", ascending=False).head(3)