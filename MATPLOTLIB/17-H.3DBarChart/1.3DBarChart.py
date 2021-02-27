import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

colors = ['r', 'b', 'g', 'm', 'c', 'orange']

for col1, col2, z in zip(colors[:3], colors[3:], [3, 2, 1]):
    x1 = np.arange(20)
    y1 = np.random.rand(20)
    c1 = [col1] * len(x1)

    x2 = np.arange(20)
    y2 = np.random.rand(20)
    c2 = [col2] * len(x2)

    ax1.bar(x1, y1, zs=z, zdir='y', color=c1, alpha=.8)
    ax2.bar(x2, y2, zs=z, zdir='x', color=c2, alpha=.8)

# plt.tight_layout()
plt.show()
