BatchBacktesting
BatchBacktesting is a Python tool that allows users to run backtests on a large number of stocks and strategies in parallel. The results are stored in a csv file for easy analysis.

Usage
To use BatchBacktesting, simply navigate to the batch.ipynb file and run the cells. You can change the parameters in the first cell to adjust the backtesting parameters to your liking. The results are then stored in the results.csv file.

Requirements
BatchBacktesting requires the following software and libraries:
- Python 3.6
- Jupyter Notebook
- Pandas
- Numpy
- Matplotlib
- Pandas_ta
- 
Installation
To install BatchBacktesting, clone the repository to your local machine and install the required libraries using pip:

```bash
git clone https://github.com/username/BatchBacktesting.git
cd BatchBacktesting
pip install -r requirements.txt
```

Supported Strategies
BatchBacktesting supports the following trading strategies:

Exponential Moving Average (EMA)
Relative Strength Index (RSI)
Bollinger Bands
Moving Average Convergence Divergence (MACD)
Linear Regression
On-Balance Volume (OBV)
Accumulation/Distribution Line (AD)
Average Directional Index (ADX)
Stochastic Oscillator
Standard Deviation
Exponential Bollinger Bands with Supertrend (EBSW)
Triple Exponential Moving Average (TRIX)
Aberration
Aroon Oscillator
Simple Mean Reversion
Mean Absolute Deviation (MAD)
Candlestick Pattern Recognition (CDLZ)
Momentum (MOM)
Fractal Weighted Moving Average (FWMA)
Double Exponential Moving Average (DEMA)
Arnaud Legoux Moving Average (ALMA)
Relative Vigor Index (RVGI)
Ichimoku Cloud
Supported Cryptocurrencies
BatchBacktesting also supports backtesting for the following cryptocurrencies:

Bitcoin (BTCUSD)
Ethereum (ETHUSD)
Litecoin (LTCUSD)
Bitcoin Cash (BCHUSD)
Ripple (XRPUSD)
EOS (EOSUSD)
Stellar (XLMUSD)
TRON (TRXUSD)
Ethereum Classic (ETCUSD)
Dash (DASHUSD)
Zcash (ZECUSD)
Tezos (XTZUSD)
Monero (XMRUSD)
Cardano (ADAUSD)
NEO (NEOUSD)
NEM (XEMUSD)
VeChain (VETUSD)
Dogecoin (DOGEUSD)
OmiseGO (OMGUSD)
0x (ZRXUSD)
Basic Attention Token (BATUSD)


Example
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
