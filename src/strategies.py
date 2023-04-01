
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas_ta as taPanda


class AbstractStrategy(Strategy):
    def init(self):
        pass

    def next(self):
        pass

    def optimize_parameters(self):
        pass

    def optimize_func(self):
        pass

    def optimize_run(self):
        pass


class EMA(Strategy):
    n1 = 20
    n2 = 80
    n3 = 150

    def init(self):
        close = self.data.Close
        self.ema20 = self.I(taPanda.ema, close.s, self.n1)
        self.ema80 = self.I(taPanda.ema, close.s, self.n2)
        self.ema150 = self.I(taPanda.ema, close.s, self.n3)

    def next(self):
        price = self.data.Close
        if crossover(self.ema20, self.ema80):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.ema80, self.ema20):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

    def optimize_parameters(self):
        self.n1 = self.I(taPanda.ema, self.data.Close.s, self.n1)
        self.n2 = self.I(taPanda.ema, self.data.Close.s, self.n2)
        self.n3 = self.I(taPanda.ema, self.data.Close.s, self.n3)

    def optimize_func(self):
        self.optimize(
            n1=range(10, 30, 5),
            n2=range(10, 30, 5),
            n3=range(10, 30, 5),
            maximize="Equity Final [$]",
        )

    def optimize_run(self, instrument):
        self.optimize_parameters(instrument)
        self.run()

class RSI(Strategy):
    n1 = 14
    n2 = 30
    n3 = 70

    def init(self):
        close = self.data.Close
        self.rsi = self.I(taPanda.rsi, close.s, self.n1)
        self.rsi30 = self.I(taPanda.rsi, close.s, self.n2)
        self.rsi70 = self.I(taPanda.rsi, close.s, self.n3)

    def next(self):
        price = self.data.Close
        if crossover(self.rsi, self.rsi30):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.rsi70, self.rsi):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

    def optimize_parameters(self):
        self.n1 = self.I(taPanda.rsi, self.data.Close.s, self.n1)
        self.n2 = self.I(taPanda.rsi, self.data.Close.s, self.n2)
        self.n3 = self.I(taPanda.rsi, self.data.Close.s, self.n3)

    def optimize_func(self):
        self.optimize(
            n1=range(10, 30, 5),
            n2=range(10, 30, 5),
            n3=range(10, 30, 5),
            maximize="Equity Final [$]",
        )

    def optimize_run(self):
        self.optimize_parameters()
        self.run()

class BollingerBands(Strategy):
    n1 = 20
    n2 = 2

    def init(self):
        close = self.data.Close
        self.bbands = self.I(taPanda.bbands, close.s, self.n1, self.n2)

    def next(self):
        price = self.data.Close
        if crossover(price, self.bbands[0]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.bbands[0], price):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

class MACD(Strategy):
    n1 = 12
    n2 = 26
    n3 = 9

    def init(self):
        close = self.data.Close
        self.macd = self.I(taPanda.macd , close.s, self.n1, self.n2, self.n3)

    def next(self):
        price = self.data.Close
        if crossover(self.macd[0], self.macd[1]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.macd[1], self.macd[0]):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

class LinearRegression(Strategy):
    n1 = 20
    n2 = 2

    def init(self):
        close = self.data.Close
        self.lreg = self.I(taPanda.linreg, close.s, self.n1, self.n2)

    def next(self):
        price = self.data.Close
        if crossover(price, self.lreg):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.lreg, price):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

# class OBV(Strategy):
#     n1 = 14

#     def init(self):
#         close = self.data.Close
#         volume = self.data.Volume
#         self.obv = self.I(taPanda.obv, close.s, self.n1, volume.s)

#     def next(self):
#         price = self.data.Close
#         if self.obv[-1] > self.obv[-2]:
#             self.buy()
#         elif self.obv[-1] < self.obv[-2]:
#             self.sell()
# class ADI(Strategy):
#     n1 = 14

#     def init(self):
#         close = self.data.Close
#         volume = self.data.Volume
#         self.adi = self.I(taPanda.adi, close.s, self.n1, volume.s)

#     def next(self):
#         if self.adi[-1] > self.adi[-2]:
#             self.buy()
#         elif self.adi[-1] < self.adi[-2]:
#             self.sell()

# class ADX(Strategy):
#     n1 = 14

#     def init(self):
#         close = self.data.Close
#         self.adx = self.I(taPanda.adx, close.s, self.n1)

#     def next(self):
#         price = self.data.Close
#         if crossover(price, self.adx):
#             self.position.close()
#             self.buy(
#                 price=price,
#                 stoploss=0.90 * price,
#                 takeprofit=1.25 * price
#             )
#         elif crossover(self.adx, price):
#             self.position.close()
#             self.sell(
#                 price=price,
#                 stoploss=1.10 * price,
#                 takeprofit=0.75 * price
#             )

# class StochasticOscillator(Strategy):
#     n1 = 14
#     n2 = 3
#     n3 = 3

#     def init(self):
#         close = self.data.Close
#         self.stoch = self.I(taPanda.stoch, close.s, self.n1, self.n2, self.n3)

#     def next(self):
#         price = self.data.Close
#         if crossover(price, self.stoch):
#             self.position.close()
#             self.buy(sl=0.90 * price, tp=1.25 * price)

#         elif crossover(self.stoch, price):
#             self.position.close()
#             self.sell(sl=1.10 * price, tp=0.75 * price)

# class AroonOscillator(Strategy):
#     n1 = 14

#     def init(self):
#         close = self.data.Close
#         self.aroon = self.I(taPanda.aroon, close.s, self.n1)

#     def next(self):
#         price = self.data.Close
#         if crossover(price, self.aroon):
#             self.position.close()
#             self.buy(sl=0.90 * price, tp=1.25 * price)

#         elif crossover(self.aroon, price):
#             self.position.close()
#             self.sell(sl=1.10 * price, tp=0.75 * price)

class StandardDeviation(Strategy):
    n1 = 20

    def init(self):
        close = self.data.Close
        self.std = self.I(taPanda.stddev, close.s, self.n1)

    def next(self):
        price = self.data.Close
        if crossover(price, self.std):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.std, price):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)


STRATEGIES = [
    EMA,
    RSI,
    BollingerBands,
    MACD,
    LinearRegression,
    # OBV,
    # ADI,
    # ADX,
    # StochasticOscillator,
    # AroonOscillator,
    StandardDeviation,
]
