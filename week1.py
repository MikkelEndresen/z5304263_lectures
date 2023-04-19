import pandas as pd


file = open("cars.csv", 'r')
df = pd.DataFrame(file)

print(df)
CAR = df.iloc[:, 1]

print(CAR)