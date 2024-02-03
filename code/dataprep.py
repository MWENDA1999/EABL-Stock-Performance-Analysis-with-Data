# Import pandas library
import pandas as pd

# Define the relative path to the csv file
csv_path = r"C:\Users\ADMIN\OneDrive\Desktop\EABL\EABL-Stock-Performance-Analysis-with-Data\data\raw\stockdata.csv"


# Read the csv file using pandas
df = pd.read_csv(csv_path)

# Print the first five rows of the dataframe
print(df.head())

import matplotlib.pyplot as plt

class DataExplorer:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
    
    def display_summary(self):
        print("Summary Statistics:")
        print(self.data.describe())
    
    def plot_histogram(self, column):
        plt.hist(self.data[column], bins=20, color='skyblue', edgecolor='black')
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

# Example usage:
if __name__ == "__main__":
    # Instantiate the DataExplorer object with a file path to your data
    explorer = DataExplorer(r"C:\Users\ADMIN\OneDrive\Desktop\EABL\EABL-Stock-Performance-Analysis-with-Data\data\raw\stockdata.csv"
)
    
    # Display summary statistics
    explorer.display_summary()
    
    # Plot a histogram 
    plt.show