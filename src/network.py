import datetime
import os
import random

from matplotlib import pyplot as plt
import numpy as np


N = 100
thres = 20

dt_now = datetime.datetime.now()

os.makedirs('./output', exist_ok=True)

points = [np.array((random.uniform(0,100), random.uniform(0,100))) for i in range(N)]
# points = [(random.normalvariate(0,30), random.normalvariate(0,30)) for i in range(N)]

plt.figure(figsize = [8,8])
plt.rcParams['axes.facecolor'] = 'black'
for i in points:
    for j in points:
        print(i)
        print(j)

        if np.allclose(i, j):
            pass
        dist = np.linalg.norm(i-j)
        if dist <= thres:
            plt.plot([i[0],j[0]], [i[1],j[1]], color='blue')
    plt.plot(i[0], i[1], marker='.', color='red', markersize=10)

# plt.axis([25, 75, 25, 75])
# plt.show()
plt.savefig(f'./output/network_{dt_now.strftime("%Y-%m-%d_%H-%M-%S")}.png')
plt.close()
