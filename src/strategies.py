
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas_ta as taPanda


class Ema(Strategy):
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

class Rsi(Strategy):
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

class BollingerBands(Strategy):
    n1 = 20
    n2 = 2

    def init(self):
        close = self.data.Close
        self.bbands = self.I(taPanda.bbands, close.s, self.n1, self.n2)

    def next(self):
        price = self.data.Close
        if crossover(price, self.bbands["BBU_20_2.0"]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.bbands["BBL_20_2.0"], price):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

class Macd(Strategy):
    n1 = 12
    n2 = 26
    n3 = 9

    def init(self):
        close = self.data.Close
        self.macd = self.I(taPanda.macd, close.s, self.n1, self.n2, self.n3)

    def next(self):
        price = self.data.Close
        if crossover(self.macd["MACD_12_26_9"], self.macd["SIGNAL_12_26_9"]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.macd["SIGNAL_12_26_9"], self.macd["MACD_12_26_9"]):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

class Stochastic(Strategy):
    n1 = 14
    n2 = 3
    n3 = 3

    def init(self):
        close = self.data.Close
        self.stoch = self.I(taPanda.stoch, close.s, self.n1, self.n2, self.n3)

    def next(self):
        price = self.data.Close
        if crossover(self.stoch["%K_14_3_3"], self.stoch["%D_14_3_3"]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.stoch["%D_14_3_3"], self.stoch["%K_14_3_3"]):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)


class Ichimoku(Strategy):
    n1 = 9
    n2 = 26
    n3 = 52
    n4 = 26

    def init(self):
        close = self.data.Close
        self.ichimoku = self.I(taPanda.ichimoku, close.s, self.n1, self.n2, self.n3, self.n4)

    def next(self):
        price = self.data.Close
        if crossover(price, self.ichimoku["tenkan_sen"]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.ichimoku["kijun_sen"], price):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)


class Aroon(Strategy):
    n1 = 25

    def init(self):
        close = self.data.Close
        self.aroon = self.I(taPanda.aroon, close.s, self.n1)

    def next(self):
        price = self.data.Close
        if crossover(self.aroon["Aroon Up_25"], self.aroon["Aroon Down_25"]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.aroon["Aroon Down_25"], self.aroon["Aroon Up_25"]):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

class AwesomeOscillator(Strategy):
    n1 = 5
    n2 = 34

    def init(self):
        close = self.data.Close
        self.ao = self.I(taPanda.ao, close.s, self.n1, self.n2)

    def next(self):
        price = self.data.Close
        if crossover(self.ao["AO_5_34"], self.ao["AOs_5_34"]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.ao["AOs_5_34"], self.ao["AO_5_34"]):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

class KeltnerChannels(Strategy):
    n1 = 20
    n2 = 2

    def init(self):
        close = self.data.Close
        self.kc = self.I(taPanda.kc, close.s, self.n1, self.n2)

    def next(self):
        price = self.data.Close
        if crossover(price, self.kc["KC_UPPER_20_2.0"]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.kc["KC_LOWER_20_2.0"], price):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

class MassIndex(Strategy):
    n1 = 9
    n2 = 25

    def init(self):
        close = self.data.Close
        self.mi = self.I(taPanda.mi, close.s, self.n1, self.n2)

    def next(self):
        price = self.data.Close
        if crossover(self.mi["Mass Index_9_25"], 25):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(25, self.mi["Mass Index_9_25"]):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

class Vortex(Strategy):
    n1 = 14

    def init(self):
        close = self.data.Close
        self.vortex = self.I(taPanda.vortex, close.s, self.n1)

    def next(self):
        price = self.data.Close
        if crossover(self.vortex["Vortex Indicator_14"], 0):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(0, self.vortex["Vortex Indicator_14"]):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

class TRIX(Strategy):
    n1 = 15
    n2 = 9

    def init(self):
        close = self.data.Close
        self.trix = self.I(taPanda.trix, close.s, self.n1, self.n2)

    def next(self):
        price = self.data.Close
        if crossover(self.trix["TRIX_15_9"], self.trix["MATRIX_15_9"]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.trix["MATRIX_15_9"], self.trix["TRIX_15_9"]):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

class DPO(Strategy):
    n1 = 20

    def init(self):
        close = self.data.Close
        self.dpo = self.I(taPanda.dpo, close.s, self.n1)

    def next(self):
        price = self.data.Close
        if crossover(price, self.dpo["DPO_20"]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.dpo["DPO_20"], price):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)

class KST(Strategy):
    n1 = 10
    n2 = 15
    n3 = 20
    n4 = 30
    n5 = 10
    n6 = 10
    n7 = 10
    n8 = 15
    n9 = 9

    def init(self):
        close = self.data.Close
        self.kst = self.I(taPanda.kst, close.s, self.n1, self.n2, self.n3, self.n4, self.n5, self.n6, self.n7, self.n8, self.n9)

    def next(self):
        price = self.data.Close
        if crossover(self.kst["KST_10_15_20_30_10_10_10_15_9"], self.kst["KSTS_10_15_20_30_10_10_10_15_9"]):
            self.position.close()
            self.buy(sl=0.90 * price, tp=1.25 * price)

        elif crossover(self.kst["KSTS_10_15_20_30_10_10_10_15_9"], self.kst["KST_10_15_20_30_10_10_10_15_9"]):
            self.position.close()
            self.sell(sl=1.10 * price, tp=0.75 * price)