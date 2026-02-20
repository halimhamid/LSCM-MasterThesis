import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the pivot data
pivot_df = pd.read_excel('sustainable_metrics_pivot.xlsx', index_col=0)

# Select key indicators
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

# Print summary statistics
print("\
Summary Statistics:")
print(pivot_df[key_indicators].describe())

# Print correlation matrix
print("\
Correlation Matrix:")
print(pivot_df[key_indicators].corr())