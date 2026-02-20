# Convert the values to numeric, coercing errors to NaN
pivot_df = pivot_df.apply(pd.to_numeric, errors='coerce')

# Create a heatmap for the key indicators again
plt.figure(figsize=(15, 10))
sns.heatmap(pivot_df[key_indicators], annot=True, cmap='YlGnBu', fmt='.2f')
plt.title('Sustainable Metrics Heatmap for Selected Countries')
plt.tight_layout()
plt.show()

print("Sustainable metrics framework and visualization complete.")