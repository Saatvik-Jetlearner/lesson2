import pandas as pd

data = pd.Series([10, 20, 30, 40], name = "Numbers")
print(data)
data = pd.read_csv("titanic.csv")

print(data.info())
print(data.shape)
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

count = data[data["Age"] > 60].shape[0]
print("Passengers above 60: {}".format(count))

count2 = data[(data["Sex"] == "female") & (data["Pclass"] == 1) ].shape[0]
print("Female 1st class passengers: {}".format(count2))

avg_fare_third = data[data["Pclass"] == "3"]["Fare"].mean()
print("Average 3rd class ticket fare: {}".format(avg_fare_third))