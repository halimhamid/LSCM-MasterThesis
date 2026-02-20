import pandas as pd
import numpy as np

# Load the datasets
tracking_data = pd.read_excel('Tracking_data.xlsx')
pivot_data = pd.read_excel('sustainable_metrics_pivot.xlsx')
levant_data = pd.read_excel('enviroment-levant-all.xlsx', header=1)

# Set correct column names for levant_data
levant_data.columns = ['Country Name', 'Country ISO3', 'Year', 'Indicator Name', 'Indicator Code', 'Value']

# Define key indicators for KPIs
key_indicators = [
    'CO2 emissions (metric tons per capita)',
    'Renewable energy consumption (% of total final energy consumption)',
    'Access to electricity (% of population)',
    'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)',
    'People using at least basic drinking water services (% of population)'
]

# Create a KPI table
kpi_table = pd.DataFrame(columns=['KPI', 'Current Value', 'Target Value', 'Unit', 'Trend', 'Data Source'])

# Function to calculate trend
def calculate_trend(data):
    if len(data) < 2:
        return 'Insufficient Data'
    last_value = data.iloc[-1]
    previous_value = data.iloc[-2]
    if last_value > previous_value:
        return 'Increasing'
    elif last_value < previous_value:
        return 'Decreasing'
    else:
        return 'Stable'

# Populate KPI table
for indicator in key_indicators:
    if indicator in tracking_data.columns:
        current_value = tracking_data[indicator].iloc[-1]
        trend = calculate_trend(tracking_data[indicator])
        data_source = 'Tracking Data'
    elif indicator in pivot_data.columns:
        current_value = pivot_data[indicator].mean()
        trend = 'N/A (Single Time Point)'
        data_source = 'Pivot Data'
    else:
        indicator_data = levant_data[levant_data['Indicator Name'] == indicator]
        if not indicator_data.empty:
            current_value = indicator_data.groupby('Country Name')['Value'].last().mean()
            trend = calculate_trend(indicator_data.groupby('Year')['Value'].mean())
            data_source = 'Levant Data'
        else:
            current_value = np.nan
            trend = 'Data Not Available'
            data_source = 'N/A'
    
    # Set target value (for demonstration, we'll set it to 10% improvement)
    target_value = current_value * 1.1 if 'emissions' not in indicator.lower() else current_value * 0.9
    
    # Extract unit from indicator name
    unit = indicator.split('(')[-1].strip(')') if '(' in indicator else 'No Unit'
    
    # Use pd.concat instead of append
    new_row = pd.DataFrame({
        'KPI': [indicator],
        'Current Value': [round(current_value, 2) if not pd.isna(current_value) else 'N/A'],
        'Target Value': [round(target_value, 2) if not pd.isna(target_value) else 'N/A'],
        'Unit': [unit],
        'Trend': [trend],
        'Data Source': [data_source]
    })
    kpi_table = pd.concat([kpi_table, new_row], ignore_index=True)

# Display the KPI table
print("KPI Table for Continuous Improvement Monitoring:")
print(kpi_table.to_string(index=False))

# Calculate additional metrics for context
print("\
Additional Metrics:")
print(f"Number of countries in analysis: {levant_data['Country Name'].nunique()}")
print(f"Date range of data: {levant_data['Year'].min()} - {levant_data['Year'].max()}")
print(f"Total number of indicators available: {levant_data['Indicator Name'].nunique()}")

# Identify top performing countries for renewable energy
top_renewable = pivot_data.sort_values('Renewable energy consumption (% of total final energy consumption)', ascending=False).head(3)
print("\
Top 3 Countries for Renewable Energy Consumption:")
print(top_renewable[['Country Name', 'Renewable energy consumption (% of total final energy consumption)']])