import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-5, 5, 0.1)
plt.plot(x, x, label = "y = x function", color = "blue")
plt.plot(x, x**2, label = "y = x**2 function", color = "red")
plt.plot(x, x**3, label = "y = x**3 function", color = "green")
plt.legend()
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()