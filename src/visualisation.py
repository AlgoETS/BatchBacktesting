
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from src.strategies import STRATEGIES_STR


def plot_strategy_returns_vs_buy_and_hold(df, strategy):
    # get the highest return for each instrument for a strategy vs buy and hold in matplotlib bar chart 2 subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5), sharey=True, gridspec_kw={'width_ratios': [3, 2]})

    df[df["Strategy"] == strategy].groupby("Instrument").max().sort_values("Return [%]", ascending=False).head(5).plot.bar(y="Return [%]", ax=ax1)
    df[df["Strategy"] == strategy].groupby("Instrument").max().sort_values("Return [%]", ascending=False).head(5).plot.bar(y="Buy & Hold Return [%]", ax=ax2)

    ax1.set_title("Highest Return for EMA Strategy")
    ax2.set_title("Highest Buy & Hold Return for EMA Strategy")

    ax1.yaxis.set_major_formatter(ticker.PercentFormatter())
    ax2.yaxis.set_major_formatter(ticker.PercentFormatter())

    plt.show()

def plot_strategies_returns_vs_buy_and_hold(df, strategies):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5), sharey=True, gridspec_kw={'width_ratios': [5, 3]})
    df.groupby("Instrument").max().sort_values("Return [%]", ascending=False).head(5).plot.bar(y="Return [%]", ax=ax1)
    df.groupby("Instrument").max().sort_values("Return [%]", ascending=False).head(5).plot.bar(y="Buy & Hold Return [%]", ax=ax2)

    ax1.set_title("Highest Return for Strategies")
    ax2.set_title("Highest Buy & Hold Return for Strategies")

    ax1.yaxis.set_major_formatter(ticker.PercentFormatter())
    ax2.yaxis.set_major_formatter(ticker.PercentFormatter())

    plt.show()