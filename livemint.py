import pandas as pd

try:
    df = pd.read_json('livemint_articles.json')
    print(df.head())  # Display the first few rows
except ValueError as e:
    print(f"Error loading JSON: {e}")
