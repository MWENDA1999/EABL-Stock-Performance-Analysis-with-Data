# Import pandas library
import pandas as pd

# Define the relative path to the csv file
csv_path = csv_path = r"C:\Users\ADMIN\OneDrive\Desktop\EABL\EABL-Stock-Performance-Analysis-with-Data\data\raw\stockdata.csv"


# Read the csv file using pandas
df = pd.read_csv(csv_path)

# Print the first five rows of the dataframe
print(df.head())
