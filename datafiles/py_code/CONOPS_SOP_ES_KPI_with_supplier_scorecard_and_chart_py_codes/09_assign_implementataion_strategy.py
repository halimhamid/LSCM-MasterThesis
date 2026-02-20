# Assigning responsibilities for implementation

responsibilities = {
    'Integrate sustainability metrics': 'Sustainability Manager',
    'Embed renewable energy targets': 'Energy Efficiency Specialist',
    'Align with long-term sustainability objectives': 'Chief Sustainability Officer',
    'Enhance risk management': 'Risk Management Team Lead',
    'Adopt KPI metrics methods': 'Data Analytics Manager',
    'Incorporate long-term planning': 'Strategic Planning Director',
    'Expand social responsibility initiatives': 'Corporate Social Responsibility Manager',
    'Incorporate scenario-based planning': 'Business Strategy Analyst'
}

# Create a DataFrame for responsibilities
df_responsibilities = pd.DataFrame.from_dict(responsibilities, orient='index', columns=['Responsible Party'])
print("Implementation Responsibilities:")
print(df_responsibilities)