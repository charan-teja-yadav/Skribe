import pandas as pd
df = pd.read_json('economics_articles.json')


print(df[df['Published Date'] != None])