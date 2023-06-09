# BatchBacktesting

[
    ![Open in Remote - Containers](https://img.shields.io/static/v1?label=Remote%20-%20Containers&message=Open&color=blue&logo=visualstudiocode)
](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/godatadriven/python-devcontainer-template)

[![GitHub](https://img.shields.io/github/license/godatadriven/python-devcontainer-template?style=for-the-badge)](LICENSE.md)
[![GitHub issues](https://img.shields.io/github/issues/godatadriven/python-devcontainer-template?style=for-the-badge)](https://github.com/AlgoETS/BatchBacktesting/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

[Article](https://nextjournal.com/emaalgoets/exp%C3%A9rimentation-des-indicateurs-technique?change-id=DPRFHNvXwD3MyHorLnHD95)

[EMA with AAPL 2018-04-04 -> 2023-04-03](https://algoets.github.io/BatchBacktesting/output/charts/EMA/AAPL-2018-04-04-2023-04-03.html)


BatchBacktesting is a Python tool that allows users to run backtests on a large number of stocks and strategies in parallel. The results are stored in a csv file for easy analysis.

The results are stored in a CSV file for easy analysis. This tool is useful for those who want to quickly test a large number of trading strategies on different stocks or cryptocurrencies.

## Usage

To use BatchBacktesting, simply navigate to the batch.ipynb file and run the cells. You can change the parameters in the first cell to adjust the backtesting parameters to your liking. The results are then stored in the `<Strategie>`-`<Start>`-`<End>`.csv file.

## Requirements

BatchBacktesting requires the following software and libraries:

- Python 3.6
- Jupyter Notebook
- Pandas
- Numpy
- Matplotlib
- Pandas_ta

## Installation

To install BatchBacktesting, clone the repository to your local machine and install the required libraries using pip:

```bash
git clone https://github.com/username/BatchBacktesting.git
cd BatchBacktesting
pip install -r requirements.txt
```

## Jupyter Notebook

To run the Jupyter Notebook, run the following command:

```bash
jupyter notebook
```

The batch.ipynb file contains a parameter section that allows you to adjust the backtesting parameters to your liking. You can change the list of stocks or cryptocurrencies to be backtested, the trading strategies to be used, the start and end dates for the backtesting period, and other parameters related to the trading strategies.

Once you have set the parameters, you can run the cells to generate the backtesting datasets. The results are then stored in a CSV file with a name in the format `<Strategie>`-`<Start>`-`<End>`.csv, where "Strategie" is the name of the strategy used, and "Start" and "End" are the start and end dates of the backtesting period.

The analyse.ipynb file can be used to analyze the results of the backtesting. You can import the CSV file generated by the batch.ipynb file and use the functions provided in the file to generate charts and statistics on the backtesting results.

## Supported Stocks

BatchBacktesting supports the following stocks:

- S&P 500 (inside stocks)

## Supported Strategies

BatchBacktesting supports the following trading strategies:

- Exponential Moving Average (EMA)
- Relative Strength Index (RSI)
- Bollinger Bands
- Moving Average Convergence Divergence (MACD)
- Linear Regression
- On-Balance Volume (OBV)
- Accumulation/Distribution Line (AD)
- Average Directional Index (ADX)
- Stochastic Oscillator
- Standard Deviation
- Exponential Bollinger Bands with Supertrend (EBSW)
- Triple Exponential Moving Average (TRIX)
- Aberration
- Aroon Oscillator
- Simple Mean Reversion
- Mean Absolute Deviation (MAD)
- Candlestick Pattern Recognition (CDLZ)
- Momentum (MOM)
- Fibonacci's Weighted Moving Average (FWMA)
- Double Exponential Moving Average (DEMA)
- Arnaud Legoux Moving Average (ALMA)
- Relative Vigor Index (RVGI)
- Ichimoku Cloud

## Supported Cryptocurrencies

BatchBacktesting also supports backtesting for the following cryptocurrencies:

- Bitcoin (BTCUSD)
- Ethereum (ETHUSD)
- Litecoin (LTCUSD)
- Bitcoin Cash (BCHUSD)
- Ripple (XRPUSD)
- EOS (EOSUSD)
- Stellar (XLMUSD)
- TRON (TRXUSD)
- Ethereum Classic (ETCUSD)
- Dash (DASHUSD)
- Zcash (ZECUSD)
- Tezos (XTZUSD)
- Monero (XMRUSD)
- Cardano (ADAUSD)
- NEO (NEOUSD)
- NEM (XEMUSD)
- VeChain (VETUSD)
- Dogecoin (DOGEUSD)
- OmiseGO (OMGUSD)
- 0x (ZRXUSD)
- Basic Attention Token (BATUSD)

## Example

Here is an example of BatchBacktesting being used to run backtests on a set of stocks and strategies:

```
# import library
import pandas as pd
import numpy as np
from datetime import datetime

import sys
import os
import httpx

import concurrent.futures
from datetime import datetime
import glob
import warnings
from rich.progress import track
warnings.filterwarnings("ignore")

from src.strategies import *
from src.BatchBacktesting import *
from src.data import *


run_backtests_strategies(["BMO"], STRATEGIES_STR)
```

## Project Structure

```shell
├── analyse.ipynb   # analyse the results of backtesting
├── batch.ipynb    # generate datasets of backtesting
├── requirements.txt  # requirements
└── src
    ├── analyse.py # analyse the results of backtesting
    ├── BatchBacktesting.py # generate datasets of backtesting
    ├── config.py # config
    ├── data.py # data
    ├── main.py # main
    ├── strategies.py  # strategies
    └── utils.py # utils

```

# TODO
    [] Add more strategies
    [] Add more stocks
    [] Add more cryptocurrencies

    [] Add Github Action Every Push to run the backtesting
    [] Add Github Action Every Week to run the backtesting

    [] ADD MORE DOCUMENTATION
    [] Add Visualizations
