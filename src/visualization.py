"""
Visualization Service for Stock Analytics Platform.

Responsible for reading processed stock data and
generating visual reports (price trends, indicators).
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def load_processed_data(file_path: str) -> pd.DataFrame:
    """
    Load processed stock data from CSV file.
    """
    full_path = PROJECT_ROOT / file_path

    if not full_path.exists():
        raise FileNotFoundError(f"Processed file not found: {full_path}")

    df = pd.read_csv(full_path)
    df['Date'] = pd.to_datetime(df['Date'])

    return df

def plot_price_with_indicators(
    df: pd.DataFrame,
    ticker: str,
    output_dir: str = "reports"
):
    """
    Plot closing price with simple moving averages.

    Args:
        df (pd.DataFrame): Processed stock DataFrame
        ticker (str): Stock ticker symbol
        output_dir (str): Directory to save plot image
    """
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(12, 6))

    plt.plot(df['Date'], df['Close'], label="Close Price", linewidth=2)
    plt.plot(df['Date'], df['sma_5'], label="SMA 5", linestyle="--")
    plt.plot(df['Date'], df['sma_20'], label="SMA 20", linestyle="--")

    plt.title(f"{ticker} Price Analysis")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{ticker}_price_analysis_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)

    plt.savefig(filepath)
    plt.close()

    print(f"Visualization saved to {filepath}")


# Example usage for local testing
if __name__ == "__main__":
    sample_file = "data/processed/sample_stock.csv"
    sample_ticker = "AAPL"

    data = load_processed_data(sample_file)
    plot_price_with_indicators(data, sample_ticker)
