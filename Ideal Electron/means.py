import matplotlib.pyplot as plt
import numpy as np
import random
steps=500000
electrons=100000

positions=np.zeros(electrons)
mean=[]
meansq=[]

fig,ax =plt.subplots(1,3,figsize=(18,6))

walk_line, = ax[0].plot([], [], 'k-', label='x(t) for one electron')
mean_line, = ax[1].plot([], [], 'b-', label='⟨x⟩')
sq_line, = ax[2].plot([], [], 'r-', label='⟨x²⟩')

for a in ax:
    a.grid(True)
    a.legend()
    a.set_xlabel('Step')

ax[0].set_ylabel('Position')
ax[1].set_ylabel('⟨x⟩')
ax[2].set_ylabel('⟨x²⟩')
ax[0].set_title('Sample Electron Walk')
ax[1].set_title('Mean ⟨x⟩')
ax[2].set_title('Mean Squared ⟨x²⟩')

x_sample=[]
for i in range(0,steps):
    num=np.random.choice([1,-1], size=electrons)
    positions+=num

    mean.append(np.mean(positions))
    meansq.append(np.mean(positions**2))
    x_sample.append(positions[0]) 


    if i %500 == 0 or i == steps - 1:
        walk_line.set_data(range(len(x_sample)), x_sample)
        mean_line.set_data(range(len(mean)), mean)
        sq_line.set_data(range(len(meansq)), meansq)

        for a in ax:
            a.relim()
            a.autoscale_view()
        plt.pause(0.05)
plt.show()


