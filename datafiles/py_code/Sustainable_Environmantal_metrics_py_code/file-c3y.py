import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
df = pd.read_excel('enviroment-levant-all.xlsx')

# Load the indication names from paste.txt
with open('paste.txt', 'r') as file:
    indication_names = [line.strip() for line in file if line.strip()]

# Filter the data for the specified countries and indication names
selected_countries = ['Cyprus', 'Israel', 'Jordan', 'Lebanon', 'Syrian Arab Republic', 'West Bank and Gaza']
filtered_df = df[(df['Country Name'].isin(selected_countries)) & (df['Indicator Name'].isin(indication_names))]

# Get the most recent year for each country and indicator
latest_data = filtered_df.sort_values('Year', ascending=False).groupby(['Country Name', 'Indicator Name']).first().reset_index()

# Pivot the data to create a matrix with countries as rows and indicators as columns
pivot_df = latest_data.pivot(index='Country Name', columns='Indicator Name', values='Value')

# Convert the values to numeric, coercing errors to 
pivot_df = pivot_df.apply(pd.to_numeric, errors='coerce')

# Select a few key indicators for visualization
key_indicators = [
    'Access to electricity (% of population)',
    'Renewable energy consumption (% of total final energy consumption)',
    'CO2 emissions (metric tons per capita)',
    'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)',
    'People using at least basic drinking water services (% of population)'
]

# Create a heatmap for the key indicators
plt.figure(figsize=(15, 10))
sns.heatmap(pivot_df[key_indicators], annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('Sustainable Metrics Heatmap for Selected Countries')
plt.tight_layout()
plt.show()

print("Sustainable metrics framework and visualization complete.")