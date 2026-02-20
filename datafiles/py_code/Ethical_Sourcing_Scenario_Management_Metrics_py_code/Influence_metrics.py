import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the scenario data
df = pd.read_excel('ethical_sourcing_scenarios.xlsx', index_col=0)

# Calculate the correlation matrix as a proxy for influence
influence_matrix = df.corr()

# Plot the influence matrix
plt.figure(figsize=(12, 10))
sns.heatmap(influence_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Influence Matrix of Ethical Sourcing Variables')
plt.tight_layout()
plt.show()

# Save the influence matrix to an Excel file
influence_matrix.to_excel('ethical_sourcing_influence_matrix.xlsx')

print("Influence matrix has been created and saved to 'ethical_sourcing_influence_matrix.xlsx'.")

# Display the influence matrix
print("\
Influence Matrix:")
print(influence_matrix)

# Identify the most influential relationships
threshold = 0.5  # You can adjust this threshold as needed
high_influence = influence_matrix[influence_matrix.abs() > threshold].stack().reset_index()
high_influence.columns = ['Variable 1', 'Variable 2', 'Influence']
high_influence = high_influence[high_influence['Variable 1'] != high_influence['Variable 2']]
high_influence = high_influence.sort_values('Influence', ascending=False)

print("\
Most influential relationships (influence > 0.5):")
print(high_influence)

# Save the high influence relationships to an Excel file
high_influence.to_excel('ethical_sourcing_high_influence_relationships.xlsx', index=False)

print("\
High influence relationships have been saved to 'ethical_sourcing_high_influence_relationships.xlsx'.")