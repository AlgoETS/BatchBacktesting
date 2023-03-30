import pandas as pd
import pytest
from BatchBacktesting import clean_data

def test_clean_data():
    # create sample data
    data = {
        "date": ["2022-01-01", "2022-01-02"],
        "open": [100, 110],
        "high": [120, 130],
        "low": [90, 95],
        "close": [105, 125],
        "volume": [10000, 15000],
    }
    df = pd.DataFrame(data)

    # test that the function returns the expected output
    expected_output = pd.DataFrame({
        "Open": [100, 110],
        "High": [120, 130],
        "Low": [90, 95],
        "Close": [105, 125],
        "Volume": [10000, 15000]
    }, index=pd.to_datetime(["2022-01-01", "2022-01-02"]))
    pd.testing.assert_frame_equal(clean_data(df), expected_output)
    