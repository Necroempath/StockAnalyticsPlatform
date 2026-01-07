# app/models/stock.py
from sqlalchemy import Column, String, Float, Date, Integer
from app.database import Base

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True, nullable=False)
    date = Column(Date, index=True, nullable=False)
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Float)
    
    price_change = Column(Float, nullable=True)
    sma_5 = Column(Float, nullable=True)
    sma_20 = Column(Float, nullable=True)
