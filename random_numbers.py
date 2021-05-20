import json
import random

numbers = random.choices(range(0,101), k = 1000)

with open('numbers.json', 'w') as f:
    json.dump(numbers, f)