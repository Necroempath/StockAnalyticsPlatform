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

# Directory to save raw data
RAW_DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/raw')

# Ensure the directory exists
os.makedirs(RAW_DATA_DIR, exist_ok=True)


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


def save_raw_data(df: pd.DataFrame, ticker: str):
    """
    Save raw DataFrame to CSV with timestamp in filename.

    Args:
        df (pd.DataFrame): Data to save
        ticker (str): Stock symbol, used in filename
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{ticker}_{timestamp}.csv"
    filepath = os.path.join(RAW_DATA_DIR, filename)

    df.to_csv(filepath)
    print(f"Saved raw data for {ticker} to {filepath}")


# Example usage
if __name__ == "__main__":
    tickers = ["AAPL", "GOOGL", "MSFT"]

    for ticker in tickers:
        df = fetch_stock_data(ticker, period="1y")
        save_raw_data(df, ticker)
