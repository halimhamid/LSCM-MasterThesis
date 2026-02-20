import pandas as pd
import numpy as np

# Load the comprehensive metrics table
df = pd.read_csv('comprehensive_metrics_table.csv', index_col=0)

# Step 1: Review the comprehensive metrics table to identify key evaluation criteria for suppliers
key_criteria = [
    'Sustainability Integration',
    'Renewable Energy Adoption',
    'Long-term Sustainability Alignment',
    'Risk Management',
    'KPI Adherence',
    'Long-term Planning',
    'Social Responsibility',
    'Scenario Planning'
]

print("Step 1: Key Evaluation Criteria for Suppliers")
for i, criterion in enumerate(key_criteria, 1):
    print(f"{i}. {criterion}")

# Step 2: Define specific scoring metrics
scoring_metrics = {
    'Sustainability Integration': 'Percentage of sustainability metrics implemented (0-100%)',
    'Renewable Energy Adoption': 'Percentage of energy from renewable sources (0-100%)',
    'Long-term Sustainability Alignment': 'Degree of alignment with industry sustainability standards (1-5 scale)',
    'Risk Management': 'Effectiveness of risk mitigation strategies (1-5 scale)',
    'KPI Adherence': 'Percentage of relevant KPIs reported accurately (0-100%)',
    'Long-term Planning': 'Quality and depth of long-term sustainability plans (1-5 scale)',
    'Social Responsibility': 'Impact and scope of social responsibility initiatives (1-5 scale)',
    'Scenario Planning': 'Robustness of scenario-based planning approaches (1-5 scale)'
}

print("\
Step 2: Specific Scoring Metrics")
for criterion, metric in scoring_metrics.items():
    print(f"{criterion}: {metric}")

# Step 3: Establish a weighting system
weights = {
    'Sustainability Integration': 0.20,
    'Renewable Energy Adoption': 0.15,
    'Long-term Sustainability Alignment': 0.15,
    'Risk Management': 0.10,
    'KPI Adherence': 0.10,
    'Long-term Planning': 0.10,
    'Social Responsibility': 0.10,
    'Scenario Planning': 0.10
}

print("\
Step 3: Weighting System")
for criterion, weight in weights.items():
    print(f"{criterion}: {weight:.2f}")

# Step 4: Create a template for the supplier scorecard
scorecard_template = pd.DataFrame({
    'Criterion': key_criteria,
    'Metric': [scoring_metrics[c] for c in key_criteria],
    'Weight': [weights[c] for c in key_criteria],
    'Score': np.nan,
    'Weighted Score': np.nan
})

print("\
Step 4: Supplier Scorecard Template")
print(scorecard_template.to_string(index=False))

# Save the scorecard template to a CSV file
scorecard_template.to_csv('supplier_scorecard_template.csv', index=False)
print("\
Supplier scorecard template has been saved to 'supplier_scorecard_template.csv'")