import os
import random
from matplotlib import pyplot as plt
from scipy.spatial import distance


N = 100
thres = 20

os.makedirs('./output', exist_ok=True)

points = [(random.uniform(0,100), random.uniform(0,100)) for i in range(N)]
# points = [(random.normalvariate(0,30), random.normalvariate(0,30)) for i in range(N)]

plt.figure(figsize = [8,8])
plt.rcParams['axes.facecolor'] = 'black'
for i in points:
    for j in points:
        if i == j:
            pass
        dist = distance.euclidean(i, j)
        if dist <= thres:
            plt.plot([i[0],j[0]], [i[1],j[1]], color='blue')
    plt.plot(i[0], i[1], marker='.', color='red', markersize=10)

# plt.axis([25, 75, 25, 75])
plt.show()
# plt.savefig('./output/network3.png')
plt.close()
