from src.data_processing import process_stock_data

raw_file = "data/raw/AAPL_20260106_111837.csv"
processed_file = "data/processed/sample_stock.csv"
process_stock_data(raw_file, processed_file)
# df = pd.read_csv(raw_file)
# print(df.columns)
