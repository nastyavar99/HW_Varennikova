import pandas as pd

df = pd.read_csv('tweets.csv')
df = df.dropna()
df = df[df['author_name'].apply(lambda n: len(str(n).split()) >= 2)]
df = df.groupby('author_name').agg({'tweet_content': lambda t: min(t, key=len)})
print(df)

