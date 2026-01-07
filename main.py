"""
Entry point for Stock Analytics Platform.
Runs full pipeline: ingestion → processing → visualization.
"""

from pathlib import Path
from datetime import datetime

from app.models.stock import Stock
from app.services.data_ingestion import fetch_stock_data, save_raw_data
from app.services.data_processing import process_stock_data
from app.services.db_service import save_processed_to_db
from app.services.visualization import load_processed_data, plot_price_and_sma
from app.database import Base, engine, SessionLocal


def run_pipeline(ticker: str):
    """
    Runs the full data pipeline for a single stock ticker.
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    raw_path = Path("data/raw") / f"{ticker}_{timestamp}.csv"
    processed_filename = f"{ticker}_{timestamp}_processed.csv"
    processed_path = Path("data/processed") / processed_filename

    # 1. Ingestion
    df_raw = fetch_stock_data(ticker)
    save_raw_data(df_raw, raw_path)
    print(f"Saved raw data to {raw_path}")

    # 2. Processing
    process_stock_data(raw_path, processed_path)
    print(f"Processed data saved to {processed_path}")

    # 3. Saving to DB
    save_processed_to_db(ticker, processed_path)
    print(f"Processed data for {ticker} saved to DB")

    # 4. Visualization
    df_processed = load_processed_data(processed_filename)
    plot_price_and_sma(df_processed, f"{ticker}_{timestamp}_price_sma.png")
    print(f"Plot saved")

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    tickers = ["AAPL", "GOOGL", "MSFT"]

    for ticker in tickers:
        run_pipeline(ticker)
