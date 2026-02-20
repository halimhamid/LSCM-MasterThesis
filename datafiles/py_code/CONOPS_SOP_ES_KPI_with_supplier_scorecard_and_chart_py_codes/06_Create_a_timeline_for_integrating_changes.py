import pandas as pd
from datetime import datetime, timedelta

# Create a timeline for integrating changes
start_date = datetime(2024, 10, 1)  # Assuming we start on October 1, 2024
timeline = {
    'Integrate sustainability metrics': {'duration': 60, 'dependencies': []},
    'Embed renewable energy targets': {'duration': 90, 'dependencies': ['Integrate sustainability metrics']},
    'Align with long-term sustainability objectives': {'duration': 120, 'dependencies': ['Integrate sustainability metrics']},
    'Enhance risk management': {'duration': 90, 'dependencies': ['Integrate sustainability metrics']},
    'Adopt KPI metrics methods': {'duration': 45, 'dependencies': []},
    'Incorporate long-term planning': {'duration': 60, 'dependencies': ['Align with long-term sustainability objectives']},
    'Expand social responsibility initiatives': {'duration': 75, 'dependencies': ['Align with long-term sustainability objectives']},
    'Incorporate scenario-based planning': {'duration': 90, 'dependencies': ['Enhance risk management']}
}

# Calculate start and end dates
current_date = start_date
for strategy, info in timeline.items():
    if not info['dependencies']:
        info['start_date'] = current_date
    else:
        dep_end_dates = [timeline[dep]['end_date'] for dep in info['dependencies']]
        info['start_date'] = max(dep_end_dates) + timedelta(days=1)
    info['end_date'] = info['start_date'] + timedelta(days=info['duration'])

# Create a DataFrame
df_timeline = pd.DataFrame.from_dict(timeline, orient='index')
df_timeline['start_date'] = df_timeline['start_date'].dt.strftime('%Y-%m-%d')
df_timeline['end_date'] = df_timeline['end_date'].dt.strftime('%Y-%m-%d')

print("Integration Timeline:")
print(df_timeline[['start_date', 'end_date', 'duration', 'dependencies']])