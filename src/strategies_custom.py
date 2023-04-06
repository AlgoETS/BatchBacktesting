
import contextlib
import math
from backtesting import Backtest, Strategy
from backtesting.lib import SignalStrategy
from backtesting.lib import crossover, compute_stats
from backtesting.lib import crossover
import numpy as np
import pandas as pd
import pandas_ta as taPanda
import talib


class DSA(Strategy):
    def init(self):
        self.amount_to_invest_per_day = 10
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


class Funding(Strategy):
    def init(self):
        self.close = self.data.Close
        self.funding = self.data.fundingRate
        self.pctChange = self.data.pctChange
        self.daily_average = self.data['8h Average Sentiment']

    def next(self):
        # funding negatif= les shorts paient les longs

        if self.funding < 0 and self.pctChange > 0 and self.daily_average > 0:
            # open the long position
            self.buy(sl=0.90*self.close, tp=1.15*self.close)

        elif self.funding > 0 and self.pctChange < 0 and self.daily_average > 0:
            # open the short  position
            self.sell(sl=1.10*self.close, tp=0.90*self.close)

class SR(SignalStrategy):
        # https://colab.research.google.com/drive/1l4Ki7tcdlhjEqfcuhdETdxbupIwyB6KS#scrollTo=eeW5F93eqtXa
        #
        # SR Strategy is a simple strategy that uses the standard deviation of the returns to determine the entry and exit points.
        threshold = 0.5
        n = 5
        def init(self):
            super().init()

            # Precompute the two moving averages
            DR = pd.Series(self.data.Close).pct_change()*100
            MA = DR.rolling(window=self.n).mean()
            MAstd = DR.rolling(window=self.n).std(ddof= 1)
            Z = (DR - MA)/MAstd

            # Precompute signal
            signal_long = (Z > self.threshold) & (Z.shift() < self.threshold)
            signal_short = (Z < -self.threshold) & (Z.shift() > -self.threshold)

            # combine signal
            signal = signal_long
            signal[signal_short] = -1

            # add signal
            entry_size = signal * 0.9999999
            self.set_signal(entry_size = entry_size)

        def next(self):
            super().next()