import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the influence matrix
influence_matrix = pd.read_excel('ethical_sourcing_influence_matrix.xlsx', index_col=0)

# Calculate total influence and dependence for each variable
total_influence = influence_matrix.abs().sum(axis=1)
total_dependence = influence_matrix.abs().sum(axis=0)

# Create a dataframe with the results
system_grid = pd.DataFrame({
    'Influence': total_influence,
    'Dependence': total_dependence
})

# Normalize the values to a 0-10 scale for better visualization
system_grid['Influence'] = (system_grid['Influence'] - system_grid['Influence'].min()) / (system_grid['Influence'].max() - system_grid['Influence'].min()) * 10
system_grid['Dependence'] = (system_grid['Dependence'] - system_grid['Dependence'].min()) / (system_grid['Dependence'].max() - system_grid['Dependence'].min()) * 10

# Plot the system grid
plt.figure(figsize=(12, 8))
plt.scatter(system_grid['Dependence'], system_grid['Influence'], s=100)

# Add labels for each point
for i, txt in enumerate(system_grid.index):
    plt.annotate(txt, (system_grid['Dependence'][i], system_grid['Influence'][i]), xytext=(5,5), textcoords='offset points')

plt.xlabel('Dependence')
plt.ylabel('Influence')
plt.title('System Grid: Influence vs Dependence of Ethical Sourcing Variables')

# Add quadrant lines
plt.axvline(x=5, color='gray', linestyle='--')
plt.axhline(y=5, color='gray', linestyle='--')

# Add quadrant labels
plt.text(1, 9, 'Influential Variables', fontsize=10, ha='left', va='center')
plt.text(9, 9, 'Key Variables', fontsize=10, ha='right', va='center')
plt.text(1, 1, 'Autonomous Variables', fontsize=10, ha='left', va='center')
plt.text(9, 1, 'Dependent Variables', fontsize=10, ha='right', va='center')

plt.tight_layout()
plt.show()

# Save the system grid data
system_grid.to_excel('ethical_sourcing_system_grid.xlsx')
print("System grid data has been saved to 'ethical_sourcing_system_grid.xlsx'")

# Display the system grid data
print("\
System Grid Data:")
print(system_grid)

# Categorize variables
def categorize_variable(row):
    if row['Influence'] > 5 and row['Dependence'] > 5:
        return 'Key Variable'
    elif row['Influence'] > 5 and row['Dependence'] <= 5:
        return 'Influential Variable'
    elif row['Influence'] <= 5 and row['Dependence'] > 5:
        return 'Dependent Variable'
    else:
        return 'Autonomous Variable'

system_grid['Category'] = system_grid.apply(categorize_variable, axis=1)

print("\
Variable Categories:")
print(system_grid['Category'])