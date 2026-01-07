from pathlib import Path
from app.models.stock import Stock
from app.database import SessionLocal
from app.repositories.stock_repository import StockRepository
import pandas as pd

def save_processed_to_db(ticker: str, processed_file_path: Path):
    df = pd.read_csv(processed_file_path)
    db = SessionLocal()
    repo = StockRepository(db)

    for _, row in df.iterrows():
        stock = Stock(
            ticker=ticker,
            date=pd.to_datetime(row["Date"]).date(),
            open=row.get("Open"),
            close=row.get("Close"),
            high=row.get("High"),
            low=row.get("Low"),
            volume=row.get("Volume"),
            price_change=row.get("price_change"),
            sma_5=row.get("sma_5"),
            sma_20=row.get("sma_20")
        )
        repo.add_stock(stock)
    db.close()
