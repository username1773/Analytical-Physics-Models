import numpy as np
import matplotlib.pyplot as plt
import random

location_data = [0]
step_data = [0]
position = 0
Num = 1000

plt.ion()
fig, ax = plt.subplots()
plt.title("Drunkard")
plt.xlabel("Steps")
plt.ylabel("Location")
plt.grid(True)

for i in range(0, 1000):
    step = random.choice([1, -1])
    position += step
    step_data.append(i)
    location_data.append(position)
    plt.cla()
    plt.plot(step_data, location_data, color='black', linestyle='-')
    plt.plot(i, position, 'o', color='red')
    plt.grid(True)
    plt.pause(0.05)

plt.ioff()
plt.show()
