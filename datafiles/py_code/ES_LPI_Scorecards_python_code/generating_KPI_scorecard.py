import pandas as pd
import numpy as np

# Load the existing KPI table
df = pd.read_excel('Ethical_Sourcing_KPI_Table _Final.xlsx', header=1)

# Define KPIs and their weights
kpis = ['Environmental Impact', 'Ethical Sourcing', 'Transparency', 'Renewable Energy', 
        'Community Engagement', 'Eco-friendly Practices', 'Sustainability', 'Social Responsibility']
weights = [0.15, 0.15, 0.1, 0.1, 0.1, 0.15, 0.15, 0.1]  # Adjust these weights as needed

# Create a new dataframe for the scorecard
scorecard = pd.DataFrame(columns=['Supplier'] + kpis + ['Total Score'])

# Add sample suppliers and generate random scores (1-5) for each KPI
suppliers = ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D', 'Supplier E']
for supplier in suppliers:
    scores = np.random.randint(1, 6, len(kpis))
    total_score = np.sum(scores * weights)
    new_row = pd.DataFrame([[supplier] + list(scores) + [total_score]], columns=scorecard.columns)
    scorecard = pd.concat([scorecard, new_row], ignore_index=True)

print(scorecard.head())
print("\
Scorecard created successfully.")