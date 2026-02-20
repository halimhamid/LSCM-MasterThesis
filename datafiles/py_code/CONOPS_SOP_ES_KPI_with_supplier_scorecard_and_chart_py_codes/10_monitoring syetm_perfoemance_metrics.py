# Setting up a monitoring system for the performance metrics

monitoring_system = {
    'Sustainability Integration': {'system': 'Sustainability Dashboard', 'tools': 'Tableau, Power BI', 'responsible': 'Sustainability Manager'},
    'Renewable Energy Adoption': {'system': 'Energy Management System', 'tools': 'Energy Star Portfolio Manager', 'responsible': 'Energy Efficiency Specialist'},
    'Long-term Objective Alignment': {'system': 'Strategic Alignment Tracker', 'tools': 'Balanced Scorecard', 'responsible': 'Chief Sustainability Officer'},
    'Risk Management Effectiveness': {'system': 'Risk Dashboard', 'tools': 'RiskWatch, Risk Management Software', 'responsible': 'Risk Management Team Lead'},
    'KPI Metrics Adoption': {'system': 'KPI Dashboard', 'tools': 'Google Data Studio', 'responsible': 'Data Analytics Manager'},
    'Long-term Planning Integration': {'system': 'Strategic Planning System', 'tools': 'Microsoft Project', 'responsible': 'Strategic Planning Director'},
    'Social Responsibility Impact': {'system': 'CSR Impact Tracker', 'tools': 'CSRHub, Impact Reporting Software', 'responsible': 'Corporate Social Responsibility Manager'},
    'Scenario Planning Effectiveness': {'system': 'Scenario Planning Tool', 'tools': 'WhatIf Analysis Tools', 'responsible': 'Business Strategy Analyst'}
}

# Create a DataFrame for monitoring system
df_monitoring_system = pd.DataFrame.from_dict(monitoring_system, orient='index')
print("Monitoring System for Performance Metrics:")
print(df_monitoring_system)