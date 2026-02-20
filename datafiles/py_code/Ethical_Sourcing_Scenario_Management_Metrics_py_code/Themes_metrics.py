import pandas as pd
import numpy as np
import itertools
import random
import matplotlib.pyplot as plt

# Load the data
df = pd.read_excel('structured_cleaned_data.xlsx')

# Combine all text columns into a single column
df['combined_text'] = df.apply(lambda row: ' '.join(row.astype(str)), axis=1)

# Define key phrases for theme identification
def extract_key_phrases(text):
    key_phrases = [
        'environmental impact', 'ethical sourcing', 'responsible sourcing',
        'sustainability', 'transparency', 'social responsibility',
        'fair trade', 'eco-friendly', 'renewable energy', 'supplier evaluation',
        'ethical practices', 'sustainable procurement', 'waste reduction',
        'carbon footprint', 'human rights', 'labor conditions',
        'community engagement', 'ethical standards', 'supply chain visibility'
    ]
    found_phrases = []
    for phrase in key_phrases:
        if phrase in text.lower():
            found_phrases.append(phrase)
    return found_phrases

# Apply the function to extract key phrases
df['key_phrases'] = df['combined_text'].apply(extract_key_phrases)

# Define the key variables and their possible states
variables = {
    'Environmental Impact': ['High', 'Medium', 'Low'],
    'Ethical Sourcing': ['Strong', 'Moderate', 'Weak'],
    'Transparency': ['High', 'Medium', 'Low'],
    'Renewable Energy': ['Extensive', 'Limited', 'None'],
    'Community Engagement': ['Active', 'Passive', 'Minimal'],
    'Eco-friendly Practices': ['Widespread', 'Partial', 'Minimal'],
    'Sustainability': ['Long-term focus', 'Short-term focus', 'Neglected'],
    'Social Responsibility': ['High priority', 'Medium priority', 'Low priority']
}

# Generate all possible combinations
all_combinations = list(itertools.product(*variables.values()))

# Randomly select 5 distinct scenarios
scenarios = random.sample(all_combinations, 5)

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
scenario_names = [f'Scenario {i+1}' for i in range(len(scenarios))]
metrics = list(variables.keys())

# Create a matrix of scenario metrics
scenario_matrix = np.array([[metric_mapping[state] for state in scenario] for scenario in scenarios])

# Create a DataFrame for the scenarios
scenario_df = pd.DataFrame(scenario_matrix, columns=metrics, index=scenario_names)

# Save the scenario data to an Excel file
scenario_df.to_excel('ethical_sourcing_scenarios.xlsx')

print("Scenarios have been developed and saved to 'ethical_sourcing_scenarios.xlsx'.")