import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# We'll use the scorecard we created in the previous step
# If you need to recreate it, uncomment and run the following lines:
# scorecard = pd.DataFrame(columns=['Supplier'] + kpis + ['Total Score'])
# for supplier in suppliers:
#     scores = np.random.randint(1, 6, len(kpis))
#     total_score = np.sum(scores * weights)
#     new_row = pd.DataFrame([[supplier] + list(scores) + [total_score]], columns=scorecard.columns)
#     scorecard = pd.concat([scorecard, new_row], ignore_index=True)

# Function to create radar chart
def create_radar_chart(supplier_data):
    angles = np.linspace(0, 2*np.pi, len(kpis), endpoint=False)
    values = supplier_data[kpis].values.flatten().tolist()
    values += values[:1]
    angles = np.concatenate((angles, [angles[0]]))

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))
    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(kpis, size=8)
    ax.set_ylim(0, 5)
    plt.title(f"KPI Radar Chart - {supplier_data['Supplier']}")

    # Save plot to bytesIO object
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    return image_base64

# Create an Excel writer object
with pd.ExcelWriter('Updated_KPI_Scorecard.xlsx', engine='xlsxwriter') as writer:
    # Write the scorecard to the Excel file
    scorecard.to_excel(writer, sheet_name='Scorecard', index=False)

    # Get the xlsxwriter workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets['Scorecard']

    # Add conditional formatting to the Total Score column
    worksheet.conditional_format(1, len(scorecard.columns)-1, len(scorecard), len(scorecard.columns)-1, {
        'type': '3_color_scale',
        'min_color': "#FF9999",
        'mid_color': "#FFFF99",
        'max_color': "#99FF99"
    })

    # Create radar charts for each supplier
    for index, row in scorecard.iterrows():
        chart_data = create_radar_chart(row)
        worksheet.insert_image(index*25, len(scorecard.columns)+1, f"supplier_{index+1}.png", 
                               {'image_data': BytesIO(base64.b64decode(chart_data)),
                                'x_scale': 0.5, 'y_scale': 0.5})

print("Updated KPI Scorecard has been created and saved as 'Updated_KPI_Scorecard.xlsx'")
print("The scorecard includes supplier evaluations, total scores, and radar charts for visual representation.")