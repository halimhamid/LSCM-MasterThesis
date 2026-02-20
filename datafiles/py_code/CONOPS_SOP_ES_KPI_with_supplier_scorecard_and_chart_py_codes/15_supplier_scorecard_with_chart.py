import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

# Load the data
df = pd.read_excel('supplier_scorecard.xlsx')

# Prepare data for radar chart
categories = df['Criterion'].tolist()
values = df['Score'].tolist()

# Calculate angle for each category
angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False)

# Close the polygon by appending the first value to the end
values = np.concatenate((values, [values[0]]))
angles = np.concatenate((angles, [angles[0]]))

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

# Draw the shape
ax.plot(angles, values)
ax.fill(angles, values, alpha=0.3)

# Set the labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, wrap=True)

# Add title
ax.set_title("Supplier Scorecard Radar Chart")

# Adjust the layout
plt.tight_layout()

# Save the plot to a BytesIO object
img_buffer = BytesIO()
plt.savefig(img_buffer, format='png')
img_buffer.seek(0)

print("Radar chart generated successfully.")

# Add the radar chart to the Excel file
workbook = load_workbook('supplier_scorecard.xlsx')
worksheet = workbook.active

img = Image(img_buffer)
worksheet.add_image(img, 'J2')

# Save the updated Excel file
workbook.save('supplier_scorecard_with_chart.xlsx')
print("Excel file saved with the scorecard template and radar chart as 'supplier_scorecard_with_chart.xlsx'.")

# Display the chart
plt.show()
