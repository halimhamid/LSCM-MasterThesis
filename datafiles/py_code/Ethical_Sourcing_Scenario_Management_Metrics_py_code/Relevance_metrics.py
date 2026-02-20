import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the scenario data
df = pd.read_excel('ethical_sourcing_scenarios.xlsx', index_col=0)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Create a relevance matrix (absolute values of correlations)
relevance_matrix = correlation_matrix.abs()

# Plot the relevance matrix
plt.figure(figsize=(12, 10))
sns.heatmap(relevance_matrix, annot=True, cmap='YlOrRd', vmin=0, vmax=1)
plt.title('Relevance Matrix of Ethical Sourcing Variables')
plt.tight_layout()
plt.show()

# Save the relevance matrix to an Excel file
relevance_matrix.to_excel('ethical_sourcing_relevance_matrix.xlsx')

print("Relevance matrix has been created and saved to 'ethical_sourcing_relevance_matrix.xlsx'.")

# Display the relevance matrix
print("\
Relevance Matrix:")
print(relevance_matrix)

# Identify the most relevant relationships
threshold = 0.5  # You can adjust this threshold as needed
high_relevance = relevance_matrix[relevance_matrix > threshold].stack().reset_index()
high_relevance.columns = ['Variable 1', 'Variable 2', 'Relevance']
high_relevance = high_relevance[high_relevance['Variable 1'] != high_relevance['Variable 2']]
high_relevance = high_relevance.sort_values('Relevance', ascending=False)

print("\
Most relevant relationships (relevance > 0.5):")
print(high_relevance)

# Save the high relevance relationships to an Excel file
high_relevance.to_excel('ethical_sourcing_high_relevance_relationships.xlsx', index=False)

print("\
High relevance relationships have been saved to 'ethical_sourcing_high_relevance_relationships.xlsx'.")