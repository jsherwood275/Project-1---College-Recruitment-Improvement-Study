import pandas as pd
import glob

# Path to the directory containing your CSV files
directory_path = 'C:/Users/Justin/Downloads/Results/'

# Get a list of all CSV files in the directory
file_list = glob.glob(directory_path + '*.csv')

# Initialize an empty list to store DataFrames
dfs = []

# Loop through each file and read it into a DataFrame
for file in file_list:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)