import matplotlib.pyplot as plt
import random

def marks():
    marks = []
    for i in range(50):
        score = random.randint(0,100)
        marks.append(score)

marks()

plt.hist = (marks, bins = [0-30, 31-50, 51-70, 71-90, 91-100], color = "blue", edgecolor = "black")

plt.show
