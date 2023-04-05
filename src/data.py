import httpx
from config import BASE_URL_BINANCE, BASE_URL_FMP, FMP_API_KEY
import os
import pandas as pd
import numpy as np
import glob
import datetime as dt



def load_data():
    """
    Load data from the output/raw folder

    Returns:
        pd.DataFrame: Dataframe containing all the data

    """
    path = os.path.join(os.getcwd(), "output", "raw")
    files = glob.glob(os.path.join(path, "*.csv"))
    return pd.concat((pd.read_csv(file) for file in files), ignore_index=True)


def make_api_request(api_endpoint, params):
    with httpx.Client() as client:
        # Make the GET request to the API
        response = client.get(api_endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        print("Error: Failed to retrieve data from API")
        return None

def get_historical_price_full_crypto(symbol):
    """
    Get historical price full crypto

    Args:
        symbol (str): Symbol of the crypto

    Returns:
        dict: Dictionary containing the data
    """
    api_endpoint = f"{BASE_URL_FMP}/historical-price-full/crypto/{symbol}"
    params = {"apikey": FMP_API_KEY}
    return make_api_request(api_endpoint, params)

def get_historical_ohlc_data(symbol,past_days=None,interval=None):
    """
    This function returns historical klines for a given symbol and interval, for a specified number of past days.

    Parameters:

    symbol: the trading symbol for which the klines are requested
    interval: the time interval for which the klines are requested (default: '1h')
    past_days: the number of days for which historical data is requested (default: 30)
    Returns:

    A pandas DataFrame containing the requested klines data, with columns for the symbol, open date and time, opening price, highest price, lowest price, closing price, trading volume, number of trades, taker base volume, and taker quote volume.
    """

    if not interval:
        interval='1h' # default interval 1 hour
    if not past_days:
        past_days=30  # default past days 30.

    # Calculate start date based on past_days parameter
    start_str = str((pd.to_datetime('today') - pd.Timedelta(f'{str(past_days)} days')).date())

    # Request klines data from Binance API
    api_endpoint = f"{BASE_URL_BINANCE}/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "startTime": start_str}
    klines = make_api_request(api_endpoint, params)

    # Convert klines data to pandas DataFrame and format columns
    df = pd.DataFrame(klines)
    df.columns = ['open_time','open', 'high', 'low', 'close', 'volume', 'close_time', 'qav', 'num_trades', 'taker_base_vol', 'taker_quote_vol','is_best_match']
    df['open_date_time'] = [dt.datetime.fromtimestamp(x/1000) for x in df.open_time]
    df['symbol'] = symbol
    df = df[['symbol', 'open_date_time', 'open', 'high', 'low', 'close', 'volume', 'num_trades', 'taker_base_vol', 'taker_quote_vol']]

    return df


def get_historical_price_full_stock(symbol):
    """
    Get historical price full stock

    Args:
        symbol (str): Symbol of the stock

    Returns:
        dict: Dictionary containing the data
    """
    api_endpoint = f"{BASE_URL_FMP}/historical-price-full/{symbol}"
    params = {"apikey": FMP_API_KEY}

    return make_api_request(api_endpoint, params)


def get_financial_statements_lists() -> dict:
    """
    Get financial statements lists

    Returns:
        dict: Dictionary containing the data
    """
    api_endpoint = f"{BASE_URL_FMP}/financial-statement-symbol-lists"
    params = {"apikey": FMP_API_KEY}
    return make_api_request(api_endpoint, params)



def get_available_financials(sector: str) -> dict:
    """
    Get available financials

    Args:
        sector (str): Sector of the company

    Returns:
        dict: Dictionary containing the data
    """
    api_endpoint = f"{BASE_URL_FMP}/available-financials/{sector}"
    params = {"apikey": FMP_API_KEY}
    return make_api_request(api_endpoint, params)


def get_financial_statement_growth(symbol: str, statement: str) -> dict:
    """
    Get financial statement growth

    Args:
        symbol (str): Symbol of the company
        statement (str): Statement of the company

    Returns:
        dict: Dictionary containing the data
    """
    api_endpoint = f"{BASE_URL_FMP}/financial-statement-growth/{symbol}"
    params = {"apikey": FMP_API_KEY, "statement": statement}
    return make_api_request(api_endpoint, params)

def get_SP500():
    """
    Get S&P 500 companies

    Returns:
        dict: Dictionary containing the data
    """
    api_endpoint = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    data = pd.read_html(api_endpoint)
    return list(data[0]['Symbol'])

def get_all_crypto():
    """
    All possible crypto symbols
    """
    return [
        "BTCUSD",
        "ETHUSD",
        "LTCUSD",
        "BCHUSD",
        "XRPUSD",
        "EOSUSD",
        "XLMUSD",
        "TRXUSD",
        "ETCUSD",
        "DASHUSD",
        "ZECUSD",
        "XTZUSD",
        "XMRUSD",
        "ADAUSD",
        "NEOUSD",
        "XEMUSD",
        "VETUSD",
        "DOGEUSD",
        "OMGUSD",
        "ZRXUSD",
        "BATUSD"
        "USDTUSD",
        "LINKUSD",
        "BTTUSD",
        "BNBUSD",
        "ONTUSD",
        "QTUMUSD",
        "ALGOUSD",
        "ZILUSD",
        "ICXUSD",
        "KNCUSD",
        "ZENUSD",
        "THETAUSD",
        "IOSTUSD",
        "ATOMUSD",
        "MKRUSD",
        "COMPUSD",
        "YFIUSD",
        "SUSHIUSD",
        "SNXUSD",
        "UMAUSD",
        "BALUSD",
        "AAVEUSD",
        "UNIUSD",
        "RENBTCUSD",
        "RENUSD",
        "CRVUSD",
        "SXPUSD",
        "KSMUSD",
        "OXTUSD",
        "DGBUSD",
        "LRCUSD",
        "WAVESUSD",
        "NMRUSD",
        "STORJUSD",
        "KAVAUSD",
        "RLCUSD",
        "BANDUSD",
        "SCUSD",
        "ENJUSD",
    ]


def get_Vanguard_Canada():
    """
    Get Vanguard Canada companies

    Returns:
        dict: Dictionary containing the data
    """
        # VCN: Vanguard FTSE Canada All Cap Index ETF
        # VFV: Vanguard S&P 500 Index ETF
        # VUN: Vanguard US Total Market Index ETF
        # VEE: Vanguard FTSE Emerging Markets All Cap Index ETF
        # VAB: Vanguard Canadian Aggregate Bond Index ETF
        # VSB: Vanguard Canadian Short-Term Bond Index ETF
        # VXC: Vanguard FTSE Global All Cap ex Canada Index ETF
        # VIU: Vanguard FTSE Developed All Cap ex North America Index ETF
        # VGG: Vanguard US Dividend Appreciation Index ETF
    return ['VCN', 'VFV', 'VUN', 'VEE', 'VAB', 'VSB', 'VXC', 'VIU', 'VGG']