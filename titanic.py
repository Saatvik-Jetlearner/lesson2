import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw_data = pd.read_csv("titanic.csv")

data = pd.DataFrame(raw_data["data"], columns = raw_data["feature_names"])

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(data)

scaled_data = scaler.transform(data)
print(scaled_data)

from sklearn.preprocessing import PCA
pca = PCA(n_components = 2)
pca.fit(scaled_data)

new_data = pca.transform(scaled_data)
print(scaled_data.shape)
print(new_data.shape)

plt.figure(figsize = (10, 10))
plt.scatter(new_data[:, 0], new_data[:, 1], c = raw_data["target"])
plt.xlabel("First Principal Component")
plt.ylabel("Second Principal Component")
plt.show()


