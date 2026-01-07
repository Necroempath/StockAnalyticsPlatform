"""
Global configuration for Stock Analytics Platform.
"""

from pathlib import Path


# =========================
# Project structure
# =========================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = PROJECT_ROOT / "output"


# =========================
# Data ingestion
# =========================

DEFAULT_STOCK_PERIOD = "1y"


# =========================
# Indicators
# =========================

SMA_SHORT_WINDOW = 5
SMA_LONG_WINDOW = 20
