# app/repositories/stock_repository.py
from sqlalchemy.orm import Session
from app.models.stock import Stock
from typing import List, Optional
from datetime import date

class StockRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_stock(self, stock: Stock):
        self.db.add(stock)
        self.db.commit()
        self.db.refresh(stock)
        return stock

    def get_stock_by_ticker(self, ticker: str, date_: Optional[date] = None) -> List[Stock]:
        query = self.db.query(Stock).filter(Stock.ticker == ticker)
        if date_:
            query = query.filter(Stock.date == date_)
        return query.all()

    def list_stocks(self, skip: int = 0, limit: int = 100) -> List[Stock]:
        return self.db.query(Stock).offset(skip).limit(limit).all()
