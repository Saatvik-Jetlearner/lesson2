import matplotlib.pyplot as plt

traffic_count = [10, 8, 11, 6, 12]
hours = [1, 2, 4, 5, 8]


plt.bar(hours, traffic_count)
plt.title("Vehicles per hour in a city")
plt.xlabel("Hours of the day")
plt.ylabel("Traffic count")

plt.show()

plt.plot(hours, traffic_count, label = "Traffic growth over the hours")
plt.title("Traffic Growth throughout the day")
plt.xlabel("Hours")
plt.ylabel("Traffic count")

plt.show()
