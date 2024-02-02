import pandas as pd

# Load the EABL Stock Performance dataset
eabl_stock_path = '/Data/Raw/EABL-2006-2024_JAN_STOCKS.csv'
eabl_stocks = pd.read_csv(eabl_stock_path)

# Display the first few rows of the dataframe to understand its structure
eabl_stocks.head()
