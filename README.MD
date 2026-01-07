# Stock Analytics Platform

Python platform for fetching, processing, storing, and visualizing stock price data.

---

## Features

- Fetch historical stock data using `yfinance`
- Process raw CSV/JSON and calculate indicators (price change, SMA 5, SMA 20)
- Store processed data in SQLite via SQLAlchemy
- Generate plots of stock prices and indicators using `matplotlib`

---

## Quick Start

```bash
git clone https://github.com/Necroempath/StockAnalyticsPlatform.git
cd stock_analytics_platform
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py