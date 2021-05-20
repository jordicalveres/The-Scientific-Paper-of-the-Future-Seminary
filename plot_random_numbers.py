import matplotlib.pyplot as plt
import json

with open('numbers.json') as f:
    numbers = json.load(f)

plt.hist(numbers, bins = 75)
plt.savefig('Bar_Plot_Visualization.png')
plt.show()
