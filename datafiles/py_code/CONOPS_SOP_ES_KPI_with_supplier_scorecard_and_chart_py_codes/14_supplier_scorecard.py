import pandas as pd
import numpy as np

# Create the supplier scorecard dataframe
df = pd.DataFrame({
    'Criterion': [
        'Sustainability Integration',
        'Renewable Energy Adoption',
        'Long-term Sustainability Alignment',
        'Risk Management',
        'KPI Adherence',
        'Long-term Planning',
        'Social Responsibility',
        'Scenario Planning'
    ],
    'Metric': [
        'Percentage of sustainability metrics implemented (0-100%)',
        'Percentage of energy from renewable sources (0-100%)',
        'Degree of alignment with industry sustainability standards (1-5 scale)',
        'Effectiveness of risk mitigation strategies (1-5 scale)',
        'Percentage of relevant KPIs reported accurately (0-100%)',
        'Quality and depth of long-term sustainability plans (1-5 scale)',
        'Impact and scope of social responsibility initiatives (1-5 scale)',
        'Robustness of scenario-based planning approaches (1-5 scale)'
    ],
    'Weight': [0.20, 0.15, 0.15, 0.10, 0.10, 0.10, 0.10, 0.10],
    'Score': [80, 65, 4, 3, 90, 4, 4, 3],  # Example scores
    'Weighted Score': np.nan  # We'll calculate this next
})

# Calculate the Weighted Score
df['Weighted Score'] = df['Score'] * df['Weight']

# Adjust scores for 1-5 scale items to be out of 100
scale_1_5_indices = df.index[df['Metric'].str.contains('1-5 scale')]
df.loc[scale_1_5_indices, 'Score'] *= 20

# Save to Excel
df.to_excel('supplier_scorecard.xlsx', index=False)

print("Supplier scorecard data created and saved to 'supplier_scorecard.xlsx'")
print(df.to_string(index=False))