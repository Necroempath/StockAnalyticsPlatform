"""
Data Ingestion Service
----------------------
This module fetches historical stock price data and saves it to raw CSV files.

Libraries:
- yfinance: for fetching stock time-series data
- pandas: for data manipulation
- os: for file system operations
"""

import os
import pandas as pd
import yfinance as yf
from datetime import datetime

def fetch_stock_data(ticker: str, period: str = "1y") -> pd.DataFrame:
    """
    Fetch historical stock data for a given ticker symbol.

    Args:
        ticker (str): Stock symbol, e.g., 'AAPL', 'GOOGL'
        period (str): Time period for historical data ('1y', '6mo', '1d', etc.)

    Returns:
        pd.DataFrame: DataFrame with historical OHLCV (Open, High, Low, Close, Volume)
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def save_raw_data(df: pd.DataFrame, file_path):
    """
    Save raw DataFrame to CSV at the given path.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path)
    print(f"Saved raw data to {file_path}")
