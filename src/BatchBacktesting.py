# BatchBacktesting.py

# import library
import os
import pandas as pd
import numpy as np
from datetime import datetime
import concurrent.futures
from rich.progress import track
import warnings

from src.data import clean_data, get_all_crypto

warnings.filterwarnings("ignore")


from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas_ta as taPanda

# import data
from data import (
    get_historical_price_full_crypto,
    get_historical_price_full_stock,
    get_financial_statements_lists,
)


# import strategy
from strategies import *


import concurrent.futures
import glob
import os
import warnings

warnings.filterwarnings("ignore")

def run_backtests_strategies(instruments, strategies):
    """
    Run backtests for a list of instruments using a specified strategy.

    Args:
        instruments (list): List of instruments to run backtests for
        strategies (list): List of strategies to run backtests for

    Returns:
        List of outputs from run_backtests()

    """

    # find strategies in the STRATEGIES
    strategies = [x for x in STRATEGIES if x.__name__ in strategies]
    outputs = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for strategy in strategies:
            future = executor.submit(run_backtests, instruments, strategy, 4)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            outputs.extend(future.result())

    return outputs

def check_crypto(instrument):
    """
    Check if the instrument is crypto or not
    """
    return instrument in get_all_crypto()

def check_stock(instrument):
    """
    Check if the instrument is crypto or not
    """
    return instrument not in get_financial_statements_lists()


def process_instrument(instrument, strategy):
    """
    Process a single instrument for a backtest using a specified strategy.
    Returns a Pandas dataframe of the backtest results.
    """
    try:

        if check_crypto(instrument):
            data = get_historical_price_full_crypto(instrument)
        else:
            data = get_historical_price_full_stock(instrument)

        data = clean_data(data)

        bt = Backtest(
            data, strategy=strategy, cash=100000, commission=0.002, exclusive_orders=True
        )
        output = bt.run()
        output = process_output(output, instrument, strategy)
        return output, bt
    except Exception as e:
        print(f"Error processing {instrument}: {str(e)}")
        return None


def process_instrument_optimise(instrument, strategy):
    """
    Process a single instrument for a backtest using a specified strategy.
    Returns a Pandas dataframe of the backtest results.
    """
    try:
        data = get_historical_price_full_stock(instrument)
        data = clean_data(data)
        bt = Backtest(
            data, strategy=strategy, cash=100000, commission=0.002, exclusive_orders=True
        )
        output = bt.optimize_func()
        output = process_output(output, instrument, strategy)
        return output, bt
    except Exception as e:
        print(f"Error processing {instrument}: {str(e)}")
        return None


def process_output(output, instrument, strategy, in_row=True):
    """
    Process backtest output data to include instrument name, strategy name,
    and parameters.
    Returns a Pandas dataframe of the processed output.
    """
    if in_row:
        output = pd.DataFrame(output).T
    output["Instrument"] = instrument
    output["Strategy"] = strategy.__name__
    output.pop("_strategy")
    return output


def save_output(output, output_dir, instrument, start, end):
    """
    Save backtest output to file and generate chart if specified.
    """
    print(f"Saving output for {instrument}")
    fileNameOutput = f"{output_dir}/{instrument}-{start}-{end}.csv"
    output.to_csv(fileNameOutput)


def plot_results(bt, output_dir, instrument, start, end):
    print(f"Saving chart for {instrument}")
    fileNameChart = f"{output_dir}/{instrument}-{start}-{end}.html"
    bt.plot(filename=fileNameChart, open_browser=False)

def run_backtests(instruments, strategy, num_threads=4, generate_plots=False):
    """
    Run backtests for a list of instruments using a specified strategy.
    Returns a list of Pandas dataframes of the backtest results.

    Args:
        instruments (list): List of instruments to run backtests for

    Returns:
        List of Pandas dataframes of the backtest results
    """
    outputs = []
    output_dir = f"output/raw/{strategy.__name__}"
    output_dir_charts = f"output/charts/{strategy.__name__}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(output_dir_charts):
        os.makedirs(output_dir_charts)
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_instrument = {
            executor.submit(process_instrument, instrument, strategy): instrument
            for instrument in instruments
        }
        for future in concurrent.futures.as_completed(future_to_instrument):
            instrument = future_to_instrument[future]
            output = future.result()
            if output is not None:
                outputs.append(output[0])
                save_output(output[0], output_dir, instrument, output[0]["Start"].to_string().strip().split()[1], output[0]["End"].to_string().strip().split()[1])
                if generate_plots:
                    plot_results(output[1], output_dir_charts, instrument, output[0]["Start"].to_string().strip().split()[1], output[0]["End"].to_string().strip().split()[1])
    data_frame = pd.concat(outputs)
    start = data_frame["Start"].to_string().strip().split()[1]
    end = data_frame["End"].to_string().strip().split()[1]
    fileNameOutput = f"output/{strategy.__name__}-{start}-{end}.csv"
    data_frame.to_csv(fileNameOutput)


    return data_frame


def run_backtests_optimise(instruments, strategy, num_threads=4, generate_plots=False):
    """
    Run backtests for a list of instruments using a specified strategy.
    Returns a list of Pandas dataframes of the backtest results.
    """
    outputs = []
    output_dir = f"output/raw/{strategy.__name__}"
    output_dir_charts = f"output/charts/{strategy.__name__}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(output_dir_charts):
        os.makedirs(output_dir_charts)
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_instrument = {
            executor.submit(process_instrument_optimise, instrument, strategy): instrument
            for instrument in track(instruments)
        }
        for future in track(concurrent.futures.as_completed(future_to_instrument)):
            instrument = future_to_instrument[future]
            output = future.result()
            if output is not None:
                outputs.append(output[0])
                save_output(output[0], output_dir, instrument, output[0]["Start"].to_string().strip().split()[1], output[0]["End"].to_string().strip().split()[1])
                if generate_plots:
                    plot_results(output[1], output_dir_charts, instrument, output[0]["Start"].to_string().strip().split()[1], output[0]["End"].to_string().strip().split()[1])
    data_frame = pd.concat(outputs)
    start = data_frame["Start"].to_string().strip().split()[1]
    end = data_frame["End"].to_string().strip().split()[1]
    fileNameOutput = f"output/{strategy.__name__}-{start}-{end}.csv"
    data_frame.to_csv(fileNameOutput)
    return data_frame