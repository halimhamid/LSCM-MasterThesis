# Import necessary libraries
import pandas as pd

# Load the Excel file
environment_data = pd.read_excel('enviroment-levant-all.xlsx')

# Display the first few rows of the dataframe to understand its structure
print("Loaded Environment Data:")
print(environment_data.head())

# Display the column names to understand the available data
print("\
Column Names:")
print(environment_data.columns)