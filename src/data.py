import httpx
from config import BASE_URL_FMP, FMP_API_KEY
import os
import pandas as pd
import numpy as np
import glob


def load_data():
    """
    Load data from the output/raw folder
    """
    path = os.path.join(os.getcwd(), "output", "raw")
    files = glob.glob(os.path.join(path, "*.csv"))
    return pd.concat((pd.read_csv(file) for file in files), ignore_index=True)


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


def get_financial_statements_lists():
    """
    Get financial statements lists

    Returns:
        dict: Dictionary containing the data
    """
    api_endpoint = f"{BASE_URL_FMP}/financial-statement-symbol-lists"
    params = {"apikey": FMP_API_KEY}
    return make_api_request(api_endpoint, params)