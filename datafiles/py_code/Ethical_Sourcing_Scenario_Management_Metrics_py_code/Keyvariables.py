import itertools
import random

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

# Print the scenarios
for i, scenario in enumerate(scenarios, 1):
    print(f"\
Scenario {i}:")
    for var, state in zip(variables.keys(), scenario):
        print(f"  {var}: {state}")

# Function to generate a scenario description
def generate_scenario_description(scenario):
    desc = "In this scenario, the humanitarian logistics operation is characterized by "
    highlights = []
    challenges = []
    
    for var, state in zip(variables.keys(), scenario):
        if state in ['High', 'Strong', 'Extensive', 'Active', 'Widespread', 'Long-term focus', 'High priority']:
            highlights.append(f"{var.lower()} is {state.lower()}")
        elif state in ['Low', 'Weak', 'None', 'Minimal', 'Neglected', 'Low priority']:
            challenges.append(f"{var.lower()} is {state.lower()}")
    
    desc += ", ".join(highlights) + ". "
    if challenges:
        desc += "However, the operation faces challenges in terms of " + ", ".join(challenges) + ". "
    
    desc += "This scenario presents unique opportunities and challenges for ethical sourcing in humanitarian logistics."
    return desc

# Print detailed scenario descriptions
for i, scenario in enumerate(scenarios, 1):
    print(f"\
Scenario {i} Description:")
    print(generate_scenario_description(scenario))