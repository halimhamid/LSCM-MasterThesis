import pandas as pd
import re
from collections import Counter

# Assuming df is already loaded with the data

# Function to extract key phrases related to ethical sourcing
def extract_key_phrases(text):
    # List of key phrases to look for
    key_phrases = [
        'environmental impact', 'ethical sourcing', 'responsible sourcing',
        'sustainability', 'transparency', 'social responsibility',
        'fair trade', 'eco-friendly', 'renewable energy', 'supplier evaluation',
        'ethical practices', 'sustainable procurement', 'waste reduction',
        'carbon footprint', 'human rights', 'labor conditions',
        'community engagement', 'ethical standards', 'supply chain visibility'
    ]
    
    found_phrases = []
    for phrase in key_phrases:
        if phrase in text.lower():
            found_phrases.append(phrase)
    return found_phrases

# Apply the function to the combined_text column
df['key_phrases'] = df['combined_text'].apply(extract_key_phrases)

# Count the frequency of each key phrase
all_phrases = [phrase for phrases in df['key_phrases'] for phrase in phrases]
phrase_counts = Counter(all_phrases)

# Sort phrases by frequency
sorted_phrases = sorted(phrase_counts.items(), key=lambda x: x[1], reverse=True)

print("Key variables and their frequencies:")
for phrase, count in sorted_phrases:
    print(f"{phrase}: {count}")

# Display some example rows with their key phrases
print("\
Example rows with key phrases:")
print(df[['combined_text', 'key_phrases']].head(10))

# Calculate the percentage of documents mentioning each key phrase
total_documents = len(df)
print("\
Percentage of documents mentioning each key phrase:")
for phrase, count in sorted_phrases:
    percentage = (count / total_documents) * 100
    print(f"{phrase}: {percentage:.2f}%")