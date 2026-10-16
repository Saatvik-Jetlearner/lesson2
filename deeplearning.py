# Import libraries
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# Load the Iris dataset
iris = load_iris()
X = iris.data  # Features: Sepal length, sepal width, petal length, petal width

# Features: Sepal length, sepal width, petal length, petal width
# 1. iris.target
# This contains the labels or species names of each flower in the dataset.
# It's a 1D array like: