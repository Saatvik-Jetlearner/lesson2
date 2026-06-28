import pandas as pd

data = pd.Series([10, 20, 30, 40], name = "Numbers")
print(data)
data = pd.read_csv("titanic.csv")

print(data.info())

print(data.head())
print(data.head(3))

print(data.tail())
print(data.tail(3))

print(data["Name"])

print(data["Age"].max())
print(data["Age"].min())
print(data["Age"].count())
print(data["Age"].mean())
print(data["Age"].median())


print(data.describe())


print(data[["Name", "Pclass", "Age"]])
print(data[data["Age"] < 18])
print(data[(data["Pclass"] == 1) & (data["Age"] > 18) ])
print(data[data["Age"] > 18])