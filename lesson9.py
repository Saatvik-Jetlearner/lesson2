import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('iris.csv')

print(data.head(10))
print(data.shape)
print(data.columns.tolist())




print(data[data["sepal_length"], ["petal_length"], ["species"]])
print(data[data["sepal_length"] > 5.5])
print(data[data["petal_width"] < 0.3])
print(data[data["species"] == "setosa"])