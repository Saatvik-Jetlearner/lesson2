import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("titanic.csv")
pclass = [1, 2, 3]

count = data[data["Pclass"] == 1].shape[0]
count2 = data[data["Pclass"] == 2].shape[0]
count3 = data[data["Pclass"] == 3].shape[0]

pcount = [count, count2, count3]

plt.bar(pclass, pcount)

plt.title("Passenger count per class")
plt.xlabel("Class")
plt.ylabel("Count")

plt.show()


