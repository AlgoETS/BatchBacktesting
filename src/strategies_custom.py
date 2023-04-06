
import contextlib
import math
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import numpy as np
import pandas_ta as taPanda
import talib

class DSA(Strategy):
    def init(self):
        self.amount_to_invest_per_day=10
        # liste contenant pour chaque date sa representation en journée de la semaine
        # lundi=0
        self.day_of_week = self.I(
            lambda x: x,
            self.data.Close.s.index.dayofweek,
            plot=False,
        )
    def next(self):
        # If trade_on_close=False, buy signal on tuesday at the closing price, so backtesting will buy at the openning price on wednesday
        # If trade_on_close=True, buy signal on tuesday at the closing price, so backtesting will buy at the closing price on tuesday
        if self.day_of_week[-1] == 1 and self.day_of_week[-2] == 0:
            price = self.data.Close[-1]
            self.buy(size=self.amount_to_invest_per_day / price)
        else:
            self.position.close()


