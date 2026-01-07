"""
Data Processing Service for Stock Time-Series.
Validates raw data, adds indicators, and saves processed CSV.
"""

from pathlib import Path
import pandas as pd
from config import SMA_SHORT_WINDOW, SMA_LONG_WINDOW

REQUIRED_COLUMNS = {"Date", "Close"}


def validate_raw_data(df: pd.DataFrame) -> None:
    """
    Validates that raw data contains required columns.

    Raises:
        ValueError: if required columns are missing
    """
    missing = REQUIRED_COLUMNS - set(df.columns)

    if missing:
        raise ValueError(
            f"Raw data is missing required columns: {missing}. "
            f"Available columns: {list(df.columns)}"
        )


def process_stock_data(raw_file_path: Path, processed_file_path: Path) -> None:
    """
    Reads raw stock CSV/JSON, validates, processes it, and saves processed CSV.
    """
    if raw_file_path.suffix == ".csv":
        df = pd.read_csv(raw_file_path)
    elif raw_file_path.suffix == ".json":
        df = pd.read_json(raw_file_path)
    else:
        raise ValueError("Unsupported file type. Only CSV or JSON allowed.")

    # Data contract validation
    validate_raw_data(df)

    # Normalize and sort
    df["Date"] = pd.to_datetime(df["Date"], utc=True)
    df = df.sort_values("Date").reset_index(drop=True)

    # Indicators
    df["price_change_pct"] = df["Close"].pct_change() * 100
    df["sma_5"] = df["Close"].rolling(SMA_SHORT_WINDOW).mean()
    df["sma_20"] = df["Close"].rolling(SMA_LONG_WINDOW).mean()

    processed_file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(processed_file_path, index=False)

    print(f"Processed data saved to {processed_file_path}")
