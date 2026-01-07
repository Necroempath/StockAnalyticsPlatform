"""
Visualization module for processed stock data.
Loads processed CSV and generates basic plots.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from ..config import PROCESSED_DATA_DIR, OUTPUT_DIR


def load_processed_data(filename: str) -> pd.DataFrame:
    """
    Load processed stock data from data/processed directory.
    """
    file_path = PROCESSED_DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Processed file not found: {file_path}")

    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])

    return df


def plot_price_and_sma(df: pd.DataFrame, output_name: str):
    """
    Plot close price and SMA indicators.
    """
    OUTPUT_DIR.mkdir(exist_ok=True)

    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Close"], label="Close Price")
    plt.plot(df["Date"], df["sma_5"], label="SMA 5")
    plt.plot(df["Date"], df["sma_20"], label="SMA 20")

    plt.title("Stock Price with Moving Averages")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)

    output_path = OUTPUT_DIR / output_name
    plt.savefig(output_path)
    plt.close()

    print(f"Plot saved to {output_path}")


if __name__ == "__main__":
    df = load_processed_data("sample_stock.csv")
    plot_price_and_sma(df, "price_sma.png")
