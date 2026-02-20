import pandas as pd
import numpy as np

# Load the scenario data and influence matrix
df_scenarios = pd.read_excel('ethical_sourcing_scenarios.xlsx', index_col=0)
influence_matrix = pd.read_excel('ethical_sourcing_influence_matrix.xlsx', index_col=0)

# Key variables identified from the system grid
key_variables = ['Transparency', 'Eco-friendly Practices', 'Social Responsibility']

# Calculate the potential impact of each scenario
impact_scores = []
for index, scenario in df_scenarios.iterrows():
    impact_score = 0
    for var in key_variables:
        # Calculate the impact score based on the influence of key variables
        impact_score += scenario[var] * influence_matrix[var].abs().sum()
    impact_scores.append(impact_score)

# Add the impact scores to the scenarios dataframe
df_scenarios['Impact Score'] = impact_scores

# Sort scenarios by impact score
df_scenarios_sorted = df_scenarios.sort_values(by='Impact Score', ascending=False)

# Save the impact assessment to an Excel file
df_scenarios_sorted.to_excel('ethical_sourcing_scenario_impact_assessment.xlsx')

print("Impact assessment has been completed and saved to 'ethical_sourcing_scenario_impact_assessment.xlsx'.")

# Display the sorted scenarios with impact scores
print("\
Scenarios with Impact Scores:")
print(df_scenarios_sorted[['Impact Score']])