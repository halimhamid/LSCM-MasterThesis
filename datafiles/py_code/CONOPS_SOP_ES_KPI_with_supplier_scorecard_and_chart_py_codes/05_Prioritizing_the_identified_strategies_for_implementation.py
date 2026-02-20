import pandas as pd
from datetime import datetime, timedelta

# Prioritizing the identified strategies for implementation
strategies = {
    'Integrate sustainability metrics': {'impact': 'High', 'ease': 'Medium', 'urgency': 'High'},
    'Incorporate scenario-based planning': {'impact': 'Medium', 'ease': 'Low', 'urgency': 'Medium'},
    'Embed renewable energy targets': {'impact': 'High', 'ease': 'Medium', 'urgency': 'High'},
    'Align with long-term sustainability objectives': {'impact': 'High', 'ease': 'Medium', 'urgency': 'High'},
    'Adopt KPI metrics methods': {'impact': 'Medium', 'ease': 'Medium', 'urgency': 'High'},
    'Incorporate long-term planning': {'impact': 'Medium', 'ease': 'Medium', 'urgency': 'Medium'},
    'Enhance risk management': {'impact': 'High', 'ease': 'Low', 'urgency': 'High'},
    'Expand social responsibility initiatives': {'impact': 'Medium', 'ease': 'Medium', 'urgency': 'Medium'}
}

# Create a DataFrame
df = pd.DataFrame.from_dict(strategies, orient='index')

# Calculate priority score (simple weighted sum)
df['priority_score'] = (df['impact'].map({'High': 3, 'Medium': 2, 'Low': 1}) * 0.4 +
                        df['ease'].map({'High': 3, 'Medium': 2, 'Low': 1}) * 0.3 +
                        df['urgency'].map({'High': 3, 'Medium': 2, 'Low': 1}) * 0.3)

# Sort by priority score
df_sorted = df.sort_values('priority_score', ascending=False)

print("Prioritized Strategies:")
print(df_sorted)