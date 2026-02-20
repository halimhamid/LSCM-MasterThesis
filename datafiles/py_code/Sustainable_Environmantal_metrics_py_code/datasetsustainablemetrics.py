# Create a sample dataset for sustainable metrics
import numpy as np

# Define the categories and metrics
categories = ['Energy and Emissions', 'Greenhouse Gas Emissions', 'Agriculture and Land Use', 
              'Water and Sanitation', 'Air Pollution', 'Biodiversity']

metrics = {
    'Energy and Emissions': ['Access to electricity', 'Renewable energy consumption', 'CO2 intensity', 'CO2 emissions'],
    'Greenhouse Gas Emissions': ['Other greenhouse gas emissions', 'Total greenhouse gas emissions'],
    'Agriculture and Land Use': ['Agricultural methane emissions', 'Annual freshwater withdrawals for agriculture'],
    'Water and Sanitation': ['Annual freshwater withdrawals', 'Access to basic drinking water services'],
    'Air Pollution': ['PM2.5 air pollution exposure'],
    'Biodiversity': ['Threatened bird species', 'Threatened fish species', 'Threatened plant species', 'Threatened mammal species']
}

# Create a sample dataframe with hypothetical values
np.random.seed(42)  # For reproducibility

# Generate random data for each metric
data = {}
for category, metric_list in metrics.items():
    for metric in metric_list:
        data[metric] = np.random.rand(10) * 100  # Random values between 0 and 100

# Create a dataframe
sustainable_metrics_df = pd.DataFrame(data)

print("Sample Sustainable Metrics Data:")
print(sustainable_metrics_df.head())

# Visualize the data
sustainable_metrics_df.plot(kind='bar', figsize=(14, 8), legend=False)
plt.title('Sample Sustainable Metrics')
plt.xlabel('Sample Index')
plt.ylabel('Metric Value')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.tight_layout()
plt.show()

print("Sustainable metrics development complete.")