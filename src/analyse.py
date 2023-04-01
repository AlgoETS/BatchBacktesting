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

def get_max_return_strategy(df, strategy):
    """
    Get the highest return for each instrument for a strategy

    Args:
        df (pd.DataFrame): Dataframe containing the data

    Returns:
        pd.DataFrame: Dataframe containing the highest return for each instrument for a strategy

    """
    df[df["Strategy"] == strategy].groupby("Instrument").max().sort_values("Return [%]", ascending=False).head(3)


def get_min_return_strategy(df, strategy):
    """
    Get the lowest return for each instrument for a strategy

    Args:
        df (pd.DataFrame): Dataframe containing the data

    Returns:
        pd.DataFrame: Dataframe containing the lowest return for each instrument for a strategy

    """
    df[df["Strategy"] == strategy].groupby("Instrument").min().sort_values("Return [%]", ascending=True).head(3)


def compare_mean_return_and_buy_and_hold(df):
    """
    Compare the mean return of a strategy with the buy and hold strategy

    Args:
        df (pd.DataFrame): Dataframe containing the data

    Returns:
        pd.DataFrame: Dataframe containing the mean return of a strategy with the buy and hold strategy
    """
    if df["Buy & Hold Return [%]"].mean() > df["Return [%]"].mean():
        return "Buy and hold is better"
    return "Strategy is better"

def analyse_all_mean_return(dfs: list, strategies: list):
    """
    Analyse the mean return of all strategies

    Args:
        df (pd.DataFrame): Dataframe containing the data

    Returns:
        pd.DataFrame: Dataframe containing the mean return of all strategies
    """
    for strategy in strategies:
        df = dfs[strategy]
        print(f"Mean return for {strategy}: {df['Return [%]'].mean()}")
        print(f"Mean return for buy and hold for {strategy}: {df['Buy & Hold Return [%]'].mean()}")
        print(f"{compare_mean_return_and_buy_and_hold(df)}")