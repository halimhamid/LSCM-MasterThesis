# Calculate benchmark values for N/A entries
# We will use the mean of available values for similar indicators as a benchmark

# Function to calculate benchmark values
def calculate_benchmark(indicator, data_sources):
    values = []
    for source in data_sources:
        if indicator in source.columns:
            values.extend(source[indicator].dropna().tolist())
    if values:
        return np.mean(values)
    return 'No Benchmark Available'

# Update the KPI table with benchmark values
for index, row in kpi_df.iterrows():
    if row['Current Value'] == 'N/A':
        benchmark_value = calculate_benchmark(row['Sub KPI'], data_sources)
        kpi_df.at[index, 'Current Value'] = round(benchmark_value, 2) if isinstance(benchmark_value, (int, float)) else benchmark_value

# Display the updated KPI table
print("\
Updated KPI table with benchmark values:")
print(kpi_df.head().to_string(index=False))

# Save the updated workbook
filename = 'Enhanced_Environmental_KPI_Table_Expanded_with_Benchmarks.xlsx'
wb.save(filename)

print(f"Updated KPI table with benchmark values has been saved as {filename}")