import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-20, 20, 0.1)
m = input("Enter the slope of your equation")
c = input("Enter the y-intercept of your equation")

plt.plot(x, m*x + c, label = "mx + c function", color = "blue")
plt.legend()
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()