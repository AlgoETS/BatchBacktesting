import os
import python_dotenv

# Load .env file
python_dotenv.load_dotenv(".env.exemple")


BASE_URL_FMP = "https://financialmodelingprep.com/api/v3"
BASE_URL_BINANCE = "https://fapi.binance.com/fapi/v1/"

FMP_API_KEY = os.environ.get("FMP_API_KEY")
BINANCE_API_KEY = os.environ.get("BINANCE_API_KEY")
