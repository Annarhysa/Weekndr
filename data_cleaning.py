import pandas as pd

df = pd.read_csv('data/weekend_plans.csv')
print(len(df))
df.drop_duplicates(inplace=True)
print(len(df))

df.to_csv('data/weekend_plans.csv', index=False)