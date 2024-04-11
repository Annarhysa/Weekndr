import pandas as pd

df = pd.read_csv('data/weekend_plans.csv')
#print(len(df))
#df.drop_duplicates(inplace=True)
#print(len(df))

#df.to_csv('data/weekend_plans.csv', index=False)

unique_cities = df['city'].unique()
print(unique_cities)
with open('data/unique_cities.txt', 'w') as file:
    for city in unique_cities:
        file.write(city + '\n')
