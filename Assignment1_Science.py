import random
import matplotlib.pyplot as plt
import numpy as np

def n_random_gen(n):
    arr = []
    i = 0
    while (i < n):
        arr.append(1 if (random.uniform (0, 1) > 0.50) else -1)
        i += 1
    return arr

n = int(input())
steps = n_random_gen(n)
total = sum(steps)
print (steps)

y = steps
x = range(len(steps))
plt.plot(x,y)
plt.show()
