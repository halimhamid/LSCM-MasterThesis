# Filter the data for the specified countries
selected_countries = ['Cyprus', 'Israel', 'Jordan', 'Lebanon', 'Syrian Arab Republic', 'West Bank and Gaza']
filtered_data = environment_data[environment_data['Country Name'].isin(selected_countries)]

# Display the first few rows of the filtered data
print("Filtered Data for Selected Countries:")
print(filtered_data.head())

# Extract unique indicator names for these countries
unique_indicators = filtered_data['Indicator Name'].unique()

print("\
Unique Indicators for Selected Countries:")
print(unique_indicators)