"""
Data Processing Service for Crypto/Stock Time-Series.
Transforms raw JSON/CSV into structured DataFrame, adds indicators and saves processed data.
"""

import pandas as pd
import os


def process_stock_data(raw_file_path: str, processed_file_path: str):
    """
    Reads raw stock CSV/JSON, processes it, adds simple indicators, and saves processed CSV.

    Args:
        raw_file_path (str): Path to the raw data file (CSV/JSON)
        processed_file_path (str): Path to save processed data
    """
    # Read raw data
    if raw_file_path.suffix == ".csv":
        df = pd.read_csv(raw_file_path)
    elif raw_file_path.suffix == ".json":
        df = pd.read_json(raw_file_path)
    else:
        raise ValueError("Unsupported file type. Only CSV or JSON allowed.")

    # Ensure timestamp column is datetime
    df['Date'] = pd.to_datetime(df['Date'], utc=True)

    # Sort by timestamp ascending
    df = df.sort_values('Date').reset_index(drop=True)

    # Add basic indicators
    df['price_change'] = df['Close'].pct_change() * 100  # % change
    df['sma_5'] = df['Close'].rolling(window=5).mean()  # Simple Moving Average 5
    df['sma_20'] = df['Close'].rolling(window=20).mean()  # Simple Moving Average 20

    # Save processed data
    os.makedirs(os.path.dirname(processed_file_path), exist_ok=True)
    df.to_csv(processed_file_path, index=False)

    print(f"Processed data saved to {processed_file_path}")
