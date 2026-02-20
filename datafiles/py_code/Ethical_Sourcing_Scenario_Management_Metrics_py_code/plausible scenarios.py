import matplotlib.pyplot as plt
import numpy as np

# Define the scenarios and their metrics
scenarios = [
    {'name': 'Scenario 1', 'Environmental Impact': 'High', 'Ethical Sourcing': 'Moderate', 'Transparency': 'Medium', 'Renewable Energy': 'Limited', 'Community Engagement': 'Active', 'Eco-friendly Practices': 'Minimal', 'Sustainability': 'Long-term focus', 'Social Responsibility': 'High priority'},
    {'name': 'Scenario 2', 'Environmental Impact': 'High', 'Ethical Sourcing': 'Strong', 'Transparency': 'Medium', 'Renewable Energy': 'Limited', 'Community Engagement': 'Minimal', 'Eco-friendly Practices': 'Minimal', 'Sustainability': 'Short-term focus', 'Social Responsibility': 'High priority'},
    {'name': 'Scenario 3', 'Environmental Impact': 'Medium', 'Ethical Sourcing': 'Moderate', 'Transparency': 'Medium', 'Renewable Energy': 'None', 'Community Engagement': 'Minimal', 'Eco-friendly Practices': 'Minimal', 'Sustainability': 'Long-term focus', 'Social Responsibility': 'High priority'},
    {'name': 'Scenario 4', 'Environmental Impact': 'Medium', 'Ethical Sourcing': 'Moderate', 'Transparency': 'Medium', 'Renewable Energy': 'Extensive', 'Community Engagement': 'Active', 'Eco-friendly Practices': 'Partial', 'Sustainability': 'Long-term focus', 'Social Responsibility': 'Low priority'},
    {'name': 'Scenario 5', 'Environmental Impact': 'High', 'Ethical Sourcing': 'Strong', 'Transparency': 'High', 'Renewable Energy': 'Limited', 'Community Engagement': 'Active', 'Eco-friendly Practices': 'Widespread', 'Sustainability': 'Long-term focus', 'Social Responsibility': 'High priority'}
]

# Convert qualitative metrics to numerical values
metric_mapping = {
    'High': 3, 'Medium': 2, 'Low': 1,
    'Strong': 3, 'Moderate': 2, 'Weak': 1,
    'Extensive': 3, 'Limited': 2, 'None': 1,
    'Active': 3, 'Passive': 2, 'Minimal': 1,
    'Widespread': 3, 'Partial': 2, 'Minimal': 1,
    'Long-term focus': 3, 'Short-term focus': 2, 'Neglected': 1,
    'High priority': 3, 'Medium priority': 2, 'Low priority': 1
}

# Prepare data for plotting
scenario_names = [s['name'] for s in scenarios]
metrics = list(scenarios[0].keys())[1:]

# Create a matrix of scenario metrics
scenario_matrix = np.array([[metric_mapping[s[metric]] for metric in metrics] for s in scenarios])

# Plot the metrics for each scenario
fig, ax = plt.subplots(figsize=(12, 8))
cax = ax.matshow(scenario_matrix, cmap='viridis')

# Set axis labels
ax.set_xticks(np.arange(len(metrics)))
ax.set_yticks(np.arange(len(scenario_names)))
ax.set_xticklabels(metrics, rotation=45, ha='left')
ax.set_yticklabels(scenario_names)

# Add color bar
fig.colorbar(cax)

# Add text annotations
for i in range(len(scenario_names)):
    for j in range(len(metrics)):
        ax.text(j, i, scenario_matrix[i, j], va='center', ha='center', color='white')

plt.title('Scenario Metrics Visualization')
plt.tight_layout()
plt.show()