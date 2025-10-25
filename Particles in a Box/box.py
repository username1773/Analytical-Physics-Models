import numpy as np
import matplotlib.pyplot as plt
import random

x_data=[]
y_data=[]
z_data=[]
positon=[0,0,0]
num=108
size=18.5
radius=1.7
while len(x_data) < num:
    cx, cy, cz = np.random.uniform(-size + radius, size - radius, 3)
    if x_data: 
        distances = np.sqrt((np.array(x_data) - cx)**2 +
                            (np.array(y_data) - cy)**2 +
                            (np.array(z_data) - cz)**2)
        if np.all(distances >= 2*radius):
            x_data.append(cx)
            y_data.append(cy)
            z_data.append(cz)
    else:
        x_data.append(cx)
        y_data.append(cy)
        z_data.append(cz)

x_data = np.array(x_data)
y_data = np.array(y_data)
z_data = np.array(z_data)
U=0
U_data=[]
R=0
ep=0.238
xi=2
function=0
for i in range(num):
    for j in range(i+1,num):
        if(i!=j):
            R=((x_data[i]-x_data[j])**2 + (y_data[i]-y_data[j])**2 + (z_data[i]-z_data[j])**2)**0.5
            if(R>3.4):                
                U=4*((3.4/R)**12-(3.4/R)**6)
                U_data.append(U)
for i in range(num):
    if(i!=2):
        def f(x):
            return ((x-x_data[i])**2+(y_data[xi]-y_data[i])**2+(z_data[xi]-z_data[i])**2)**0.5
        x0 = 5.0
        dx = 1e-6
        df = (f(x_data[xi]+ dx) - f(x_data[xi])) / (dx)
print("U=",U)
print("Fx1=",df)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_data, y_data, z_data, s=5)
plt.show()