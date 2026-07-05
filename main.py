# import pandas as pd

# data = pd.Series([10, 20, 30, 40], name = "Numbers")
# print(data)
# data = pd.read_csv("titanic.csv")

# print(data.info())
# print(data.shape)
# print(data.head())
# print(data.head(3))

# print(data.tail())
# print(data.tail(3))

# print(data["Name"])

# print(data["Age"].max())
# print(data["Age"].min())
# print(data["Age"].count())
# print(data["Age"].mean())
# print(data["Age"].median())


# print(data.describe())


# print(data[["Name", "Pclass", "Age"]])
# print(data[data["Age"] < 18])
# print(data[(data["Pclass"] == 1) & (data["Age"] > 18) ])
# print(data[data["Age"] > 18])

# count = data[data["Age"] > 60].shape[0]
# print("Passengers above 60: {}".format(count))

# count2 = data[(data["Sex"] == "female") & (data["Pclass"] == 1) ].shape[0]
# print("Female 1st class passengers: {}".format(count2))

# avg_fare_third = data[data["Pclass"] == "3"]["Fare"].mean()
# print("Average 3rd class ticket fare: {}".format(avg_fare_third))

import pandas as pd

data = pd.read_csv("titanic.csv")

adult_names = data.loc[data["Age"] > 18, "Name"]
print(adult_names)

print(data.iloc[9:25, 2:5])

data.iloc[0:3, 3] = "Pulkit Chawla"
print(data["Name"])

data.to_csv("changedData.csv")

data["Test"] = data["Fare"] + 2
data["Test2"] = data["Fare"] + data["Pclass"]

data_renamed = data.rename(
    colums = [
        "Pclass": "Passenger Class",
        "Sibsp": "Sibling"
    ]
)

print(data_renamed.info())

print(data["Age"].mean())

print(data[["Age", "Fare"]].mean())

print(data.agg{{
    "Age": ["min", "max", "median"]
}})

print(data[["Sex", "Age"]].groupby("Sex").mean())

print(data.groupby("Sex")["Age"].mean())

print(data.groupby(["Sex", "Pclass"])["Fare"].mean())

print(data["Pclass"].value_counts())

print(data.groupby("Pclass")["Pclass"].count())

data.sort_values(by = "Age")
print(data[["Name", "Age"]].head())

data.sort_values(by = ["Pclass", "Age"], ascending = False)

data["NameLowercase"] = data["Name"].str.lower()

titanic['Name'].str.split(",")
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
