import pandas as pd

# Define the structure of the Audit Finding Form
audit_finding_columns = ['Date', 'Supplier Name', 'KPI', 'Finding', 'Evidence', 'Comments', 'Auditor Name']
audit_finding_data = []  # No data, just structure

# Define the structure and sample content for the Evaluation Form
kpis_definitions = {
    'Environmental Impact': 'Impact on natural environments and ecosystems.',
    'Ethical Sourcing': 'Sourcing materials and labor ethically.',
    'Transparency': 'Clarity and openness in operations.',
    'Renewable Energy': 'Utilization of renewable energy sources.',
    'Community Engagement': 'Involvement in community development.',
    'Eco-friendly Practices': 'Environmentally friendly practices.',
    'Sustainability': 'Long-term sustainable operations.',
    'Social Responsibility': 'Accountability for social welfare initiatives.'
}

evaluation_form_columns = ['Supplier Name', 'KPI', 'Definition', 'Score (0-5)', 'Comments/Observations']
evaluation_form_data = [[None, kpi, definition, None, None] for kpi, definition in kpis_definitions.items()]

# Create DataFrames for both forms
audit_finding_df = pd.DataFrame(audit_finding_data, columns=audit_finding_columns)
evaluation_form_df = pd.DataFrame(evaluation_form_data, columns=evaluation_form_columns)

# Save to Excel file
with pd.ExcelWriter('Audit_Evaluation_Templates.xlsx', engine='xlsxwriter') as writer:
    audit_finding_df.to_excel(writer, sheet_name='Audit Finding Form', index=False)
    evaluation_form_df.to_excel(writer, sheet_name='Evaluation Form', index=False)

print("Audit and Evaluation templates have been created and saved in 'Audit_Evaluation_Templates.xlsx'.")