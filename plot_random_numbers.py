import matplotlib.pyplot as plt
import random

numbers = random.choices(range(0,101), k = 1000)

plt.hist(numbers, bins = 75)
plt.show()

