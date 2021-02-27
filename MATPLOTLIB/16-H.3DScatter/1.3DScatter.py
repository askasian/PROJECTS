import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

x1 = np.random.randint(1, 50, 20)
y1 = np.random.randint(1, 50, 20)
z1 = np.random.randint(1, 50, 20)
x2 = np.random.randint(1, 50, 20)
y2 = np.random.randint(1, 50, 20)
z2 = np.random.randint(1, 50, 20)

ax1.scatter(x1, y1, z1, c='r', marker='o', s=175, zdir='z')
ax1.scatter(x2, y2, z2, c='c', marker='o', s=175, zdir='z')
ax1.legend(['red ball', 'blue ball'], loc=(0.2, 1.1))

x1 = np.random.randint(1, 50, 20)
y1 = np.random.randint(1, 50, 20)
z1 = np.random.randint(1, 50, 20)
x2 = np.random.randint(1, 50, 20)
y2 = np.random.randint(1, 50, 20)
z2 = np.random.randint(1, 50, 20)

ax2.scatter(x1, y1, z1, c='g', marker='o', s=175, zdir='z')
ax2.scatter(x2, y2, z2, c='y', marker='o', s=175, zdir='z')
ax2.legend(['green ball', 'yellow ball'], loc=(0.2, 1.1))

plt.show()
