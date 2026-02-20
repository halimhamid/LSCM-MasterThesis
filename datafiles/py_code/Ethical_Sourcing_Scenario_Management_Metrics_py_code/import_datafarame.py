import re

def extract_themes(text):
    ethical_sourcing_keywords = ['ethical', 'sourcing', 'sustainability', 'responsible', 'environmental', 'social responsibility', 'fair trade', 'transparency']
    themes = []
    for keyword in ethical_sourcing_keywords:
        if keyword in text.lower():
            themes.append(keyword)
    return themes

# Extract themes from the combined text
df['ethical_sourcing_themes'] = df['combined_text'].apply(extract_themes)

# Count the frequency of each theme
theme_counts = {}
for themes in df['ethical_sourcing_themes']:
    for theme in themes:
        theme_counts[theme] = theme_counts.get(theme, 0) + 1

# Sort themes by frequency
sorted_themes = sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)

print("Main themes related to ethical sourcing:")
for theme, count in sorted_themes:
    print(f"{theme}: {count}")

# Display some example rows with their themes
print("\
Example rows with ethical sourcing themes:")
print(df[['combined_text', 'ethical_sourcing_themes']].head(10))