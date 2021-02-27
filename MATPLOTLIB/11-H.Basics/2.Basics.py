import matplotlib.pyplot as plt
import numpy as np

data = [
    np.random.randint(1, 20, 10),
    np.random.randint(1, 20, 10),
    np.random.randint(1, 20, 10)]

print(data)
print(len(data))

for i in range(len(data)):
    plt.plot(data[i],
             label=['A', 'B', 'C'][i],
             marker=['o', 'd', 's'][i],
             markersize=8,
             color=['pink', 'b', 'g'][i],
             lw=3)
    plt.show()
