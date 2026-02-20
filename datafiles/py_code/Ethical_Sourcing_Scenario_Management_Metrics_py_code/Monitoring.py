import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Simulate a monitoring system
class EthicalSourcingMonitor:
    def __init__(self, scenarios_file):
        self.scenarios = pd.read_excel(scenarios_file, index_col=0)
        self.history = {}
        for column in self.scenarios.columns:
            self.history[column] = []
        self.dates = []

    def update_scenario(self, scenario, variable, new_value):
        self.scenarios.loc[scenario, variable] = new_value
        self.history[variable].append(new_value)
        if len(self.dates) < len(self.history[variable]):
            self.dates.append(datetime.now())

    def generate_report(self):
        report = "Ethical Sourcing Monitoring Report\
"
        report += "=" * 40 + "\
"
        report += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\
\
"
        report += "Current Scenario Status:\
"
        report += str(self.scenarios) + "\
\
"
        report += "Recent Changes:\
"
        for variable in self.history:
            if len(self.history[variable]) > 0:
                report += f"{variable}: {self.history[variable][-1]}\
"
        return report

    def plot_trends(self):
        plt.figure(figsize=(12, 6))
        for variable in self.history:
            if len(self.history[variable]) > 0:
                plt.plot(self.dates, self.history[variable], label=variable)
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.title('Ethical Sourcing Variable Trends')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('ethical_sourcing_trends.png')
        plt.close()

# Initialize the monitor
monitor = EthicalSourcingMonitor('ethical_sourcing_scenarios.xlsx')

# Simulate some changes
monitor.update_scenario('Scenario 1', 'Environmental Impact', 2)
monitor.update_scenario('Scenario 2', 'Transparency', 3)
monitor.update_scenario('Scenario 3', 'Social Responsibility', 1)

# Generate and save report
report = monitor.generate_report()
with open('ethical_sourcing_monitoring_report.txt', 'w') as f:
    f.write(report)

print("Monitoring report has been generated and saved to 'ethical_sourcing_monitoring_report.txt'")

# Generate and save trend plot
monitor.plot_trends()
print("Trend plot has been generated and saved as 'ethical_sourcing_trends.png'")

# Display the report
print("\
Monitoring Report Preview:")
print(report)