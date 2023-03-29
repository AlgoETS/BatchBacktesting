# BatchBacktesting.py

# import library
import sys
import os
import httpx
import pandas as pd
import numpy as np
from datetime import datetime
import concurrent.futures
import glob
from rich.progress import track
import warnings

warnings.filterwarnings("ignore")


from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas_ta as taPanda

from config import BASE_URL_FMP, FMP_API_KEY

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
        None

    """
    return [
        run_backtests(instruments, strategy, 4, False)
        for strategy in track(strategies)
    ]


def run_backtests(instruments, strategy=Ema, num_threads=4, generate_plots=True):
    """Run backtests for a list of instruments using a specified strategy."""

    outputs = []
    metric = "Equity Final [$]"
    # create the output directory if it doesn't exist
    output_dir = f"output/raw/{strategy.__name__}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def process_instrument(instrument):
        fileName = f"{output_dir}/{instrument}-*.csv"
        existingFiles = glob.glob(fileName)
        if existingFiles:
            print(f"{fileName} already exists. Skipping...")
            return None

        try:
            data = get_historical_price_full_stock(instrument)
            data = data["historical"]
            data = pd.DataFrame(data)
            data.columns = [x.title() for x in data.columns]  # uppercase first letter
            data = data.drop(
                [
                    "Adjclose",
                    "Unadjustedvolume",
                    "Change",
                    "Changepercent",
                    "Vwap",
                    "Label",
                    "Changeovertime",
                ],
                axis=1,
            )
            data["Date"] = pd.to_datetime(data["Date"])
            data.set_index("Date", inplace=True)  # date needs to be set as index!
            data = data.iloc[::-1]  # to reverse the order of the dataframe

            # Create a backtest for the instrument using the specified strategy
            bt = Backtest(
                data, strategy=strategy, cash=100000, commission=0.002, exclusive_orders=True
            )
            output = bt.run()
            output = pd.DataFrame(pd.DataFrame(output).T)

            # Add instrument name, strategy name, and parameters to output
            output["Instrument"] = instrument
            output["Strategy"] = strategy.__name__
            output.pop("_strategy")
            output["StrategyParameters"] = strategy.__dict__

            # Append output to list of outputs
            return output

        except Exception as e:
            print(f"Error processing {instrument}: {str(e)}")
            return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_instrument = {
            executor.submit(process_instrument, instrument): instrument
            for instrument in instruments
        }
        for future in concurrent.futures.as_completed(future_to_instrument):
            instrument = future_to_instrument[future]
            output = future.result()
            if output is not None:
                outputs.append(output)

                # Save output to file
                start = output["Start"].to_string().strip().split()[1]
                end = output["End"].to_string().strip().split()[1]
                fileNameOutput = (
                    f"{output_dir}/{instrument}-{start}-{end}.csv"
                )
                output.to_csv(fileNameOutput)

                # Plot and save chart to file
                if generate_plots:
                    fileNameChart = f"{output_dir}/{instrument}-{start}-{end}.html"
                    bt.plot(filename=fileNameChart, open_browser=False)

    # Combine all the dataframes into one
    data_frame = pd.concat(outputs)

    # Save the data to a CSV file
    start = data_frame["Start"].to_string().strip().split()[1]
    end = data_frame["End"].to_string().strip().split()[1]
    fileNameOutput = f"output/{strategy.__name__}-{start}-{end}.csv"
    data_frame.to_csv(fileNameOutput)

    return outputs
