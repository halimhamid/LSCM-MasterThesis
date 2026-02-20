# Load the data
df = pd.read_excel('structured_cleaned_data.xlsx')

# Display the column names
print("Column names:")
print(df.columns.tolist())

# Display the first few rows
print("\
First few rows of the dataframe:")
print(df.head())

# Create the combined_text column if it doesn't exist
if 'combined_text' not in df.columns:
    df['combined_text'] = df.apply(lambda row: ' '.join(row.astype(str)), axis=1)

# Display info about the dataframe
print("\
Dataframe info:")
df.info()

# Now let's try to get the first 40 rows of the combined_text column
print("\
First 40 rows of combined_text:")
print(df['combined_text'].head(40))