import matplotlib as plt
import numpy as np


subjects = ["Math", "Science", "History", "English", "Art"]
bscore = [86, 93, 81, 79, 95]
gscore = [89, 92, 79, 97, 87]


x = np.arange(len(subjects))
width = 0.35
plt.bar(x - width/2, bscore, len())

plt.bar(x- width/2, bscore, width, label = 'Boys', color = 'lightblue')
plt.bar(x- width/2, gscore, width, label = 'Girls', color = 'lightpink')

plt.xlabel("Subjects")
plt.ylabel("Grades")
plt.title("Boys vs Girls grades")
plt.xticks(x, subjects)
plt.legend()

for i in range(len(subjects)):
    plt.text(x[i] - width/2, bscore[i] + 1, str(bscore[i]), ha = 'center', fontweight = 'bold')
    plt.text(x[i] - width/2, gscore[i] + 1, str(gscore[i]), ha = 'center', fontweight = 'bold')


plt.show()